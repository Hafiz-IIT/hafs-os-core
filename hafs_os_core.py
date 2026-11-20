from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import sqlite3
import time


class Decision(str, Enum):
    ACT = "ACT"
    ASK = "ASK"
    VERIFY = "VERIFY"
    ESCALATE = "ESCALATE"


RISK_ORDER = {"low": 0, "medium": 1, "high": 2, "critical": 3}


@dataclass(frozen=True)
class Task:
    id: int
    description: str
    risk: str
    required_permission: str
    evidence_required: int
    status: str


class HafsOSCore:
    def __init__(self, path: str = ":memory:"):
        self.db = sqlite3.connect(path)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys = ON")
        self.db.executescript(
            """
            CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                risk TEXT NOT NULL,
                required_permission TEXT NOT NULL,
                evidence_required INTEGER NOT NULL,
                status TEXT NOT NULL DEFAULT 'pending'
            );
            CREATE TABLE IF NOT EXISTS permissions(
                agent TEXT NOT NULL,
                permission TEXT NOT NULL,
                PRIMARY KEY(agent, permission)
            );
            CREATE TABLE IF NOT EXISTS evidence(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id INTEGER NOT NULL,
                source TEXT NOT NULL,
                claim TEXT NOT NULL,
                verified INTEGER NOT NULL DEFAULT 0,
                submitted_by TEXT NOT NULL DEFAULT '',
                verified_by TEXT,
                verified_at REAL,
                FOREIGN KEY(task_id) REFERENCES tasks(id) ON DELETE CASCADE
            );
            CREATE TABLE IF NOT EXISTS audit(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id INTEGER,
                event TEXT NOT NULL,
                at REAL NOT NULL
            );
            """
        )
        task_columns = {row["name"] for row in self.db.execute("PRAGMA table_info(tasks)")}
        if "status" not in task_columns:
            self.db.execute("ALTER TABLE tasks ADD COLUMN status TEXT NOT NULL DEFAULT 'pending'")
        evidence_columns = {row["name"] for row in self.db.execute("PRAGMA table_info(evidence)")}
        if "submitted_by" not in evidence_columns:
            self.db.execute("ALTER TABLE evidence ADD COLUMN submitted_by TEXT NOT NULL DEFAULT ''")
        if "verified_by" not in evidence_columns:
            self.db.execute("ALTER TABLE evidence ADD COLUMN verified_by TEXT")
        if "verified_at" not in evidence_columns:
            self.db.execute("ALTER TABLE evidence ADD COLUMN verified_at REAL")
        self.db.commit()

    def grant(self, agent: str, permission: str) -> None:
        if not isinstance(agent, str) or not agent.strip() or not isinstance(permission, str) or not permission.strip():
            raise ValueError("agent and permission must be non-empty strings")
        agent, permission = agent.strip(), permission.strip()
        cur = self.db.execute("INSERT OR IGNORE INTO permissions VALUES (?, ?)", (agent, permission))
        if cur.rowcount:
            self._audit(None, f"permission-granted:{agent}:{permission}")
        self.db.commit()

    def create_task(self, description: str, risk: str, required_permission: str, evidence_required: int = 1) -> int:
        if not isinstance(risk, str) or risk.strip().lower() not in RISK_ORDER:
            raise ValueError("unknown risk")
        risk = risk.strip().lower()
        if not isinstance(description, str) or not description.strip():
            raise ValueError("task description is required")
        if not isinstance(required_permission, str) or not required_permission.strip():
            raise ValueError("required permission is required")
        required_permission = required_permission.strip()
        if not isinstance(evidence_required, int) or isinstance(evidence_required, bool) or evidence_required < 0:
            raise ValueError("evidence_required must be a non-negative integer")
        cur = self.db.execute(
            "INSERT INTO tasks(description,risk,required_permission,evidence_required) VALUES (?,?,?,?)",
            (description, risk, required_permission, evidence_required),
        )
        task_id = int(cur.lastrowid)
        self._audit(task_id, "task-created")
        self.db.commit()
        return task_id

    def add_evidence(self, task_id: int, source: str, claim: str, *, submitted_by: str) -> int:
        if isinstance(task_id, bool) or not isinstance(task_id, int) or task_id < 1:
            raise ValueError("task_id must be a positive integer")
        if not isinstance(source, str) or not source.strip() or not isinstance(claim, str) or not claim.strip():
            raise ValueError("evidence source and claim must be non-empty strings")
        if not isinstance(submitted_by, str) or not submitted_by.strip():
            raise ValueError("submitted_by identity is required")
        task = self.db.execute("SELECT 1 FROM tasks WHERE id=?", (task_id,)).fetchone()
        if task is None:
            raise KeyError(task_id)
        with self.db:
            cur = self.db.execute(
                "INSERT INTO evidence(task_id,source,claim,verified,submitted_by) VALUES (?,?,?,0,?)",
                (task_id, source.strip(), claim.strip(), submitted_by.strip()),
            )
            evidence_id = int(cur.lastrowid)
            self._audit(task_id, f"evidence:{source.strip()}:unverified")
        return evidence_id

    def verify_evidence(self, evidence_id: int, *, verifier: str) -> None:
        if isinstance(evidence_id, bool) or not isinstance(evidence_id, int) or evidence_id < 1:
            raise ValueError("evidence_id must be a positive integer")
        if not isinstance(verifier, str) or not verifier.strip():
            raise ValueError("verifier identity is required")
        verifier = verifier.strip()
        permitted = self.db.execute(
            "SELECT 1 FROM permissions WHERE agent=? AND permission='verify_evidence'",
            (verifier,),
        ).fetchone() is not None
        if not permitted:
            raise PermissionError("verifier lacks verify_evidence permission")
        with self.db:
            row = self.db.execute(
                "SELECT task_id, verified, submitted_by FROM evidence WHERE id=?", (evidence_id,)
            ).fetchone()
            if row is None:
                raise KeyError(evidence_id)
            if not row["submitted_by"]:
                raise PermissionError("legacy evidence without submitter attribution cannot be verified")
            if row["submitted_by"] == verifier.strip():
                raise PermissionError("an evidence submitter cannot verify their own evidence")
            if row["verified"]:
                raise ValueError("evidence has already been verified")
            self.db.execute(
                "UPDATE evidence SET verified=1, verified_by=?, verified_at=? WHERE id=?",
                (verifier, time.time(), evidence_id),
            )
            self._audit(row["task_id"], f"evidence-verified:{evidence_id}:by:{verifier}")

    @staticmethod
    def _maximum_independent_source_verifier_pairs(edges: list[tuple[str, str]]) -> int:
        """Return the maximum one-to-one matching between evidence sources and verifiers."""
        adjacency: dict[str, set[str]] = {}
        for source, verifier in edges:
            adjacency.setdefault(source, set()).add(verifier)

        verifier_to_source: dict[str, str] = {}

        def augment(source: str, visited: set[str]) -> bool:
            for verifier in sorted(adjacency[source]):
                if verifier in visited:
                    continue
                visited.add(verifier)
                previous_source = verifier_to_source.get(verifier)
                if previous_source is None or augment(previous_source, visited):
                    verifier_to_source[verifier] = source
                    return True
            return False

        for source in sorted(adjacency):
            augment(source, set())
        return len(verifier_to_source)

    def decide(self, task_id: int, agent: str) -> Decision:
        if isinstance(task_id, bool) or not isinstance(task_id, int) or task_id < 1:
            raise ValueError("task_id must be a positive integer")
        if not isinstance(agent, str) or not agent.strip():
            raise ValueError("acting agent identity is required")
        agent = agent.strip()
        task = self.db.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()
        if task is None:
            raise KeyError(task_id)

        permitted = self.db.execute(
            "SELECT 1 FROM permissions WHERE agent=? AND permission=?",
            (agent, task["required_permission"]),
        ).fetchone() is not None

        evidence_rows = self.db.execute(
            """SELECT DISTINCT source, verified_by
               FROM evidence
               WHERE task_id=? AND verified=1
                 AND verified_by IS NOT NULL AND verified_by <> ?""",
            (task_id, agent),
        ).fetchall()
        independent_edges = [(row["source"], row["verified_by"]) for row in evidence_rows]
        verified_count = self._maximum_independent_source_verifier_pairs(independent_edges)

        if RISK_ORDER[task["risk"]] >= RISK_ORDER["critical"]:
            decision = Decision.ESCALATE
        elif not permitted:
            decision = Decision.ASK
        elif verified_count < task["evidence_required"]:
            decision = Decision.VERIFY
        elif RISK_ORDER[task["risk"]] >= RISK_ORDER["high"] and verified_count < 2:
            decision = Decision.ESCALATE
        else:
            decision = Decision.ACT

        status = {
            Decision.ACT: "authorized",
            Decision.ASK: "awaiting_permission",
            Decision.VERIFY: "awaiting_evidence",
            Decision.ESCALATE: "escalated",
        }[decision]
        self.db.execute("UPDATE tasks SET status=? WHERE id=?", (status, task_id))
        self._audit(task_id, f"decision:{agent}:{decision.value}")
        self.db.commit()
        return decision

    def task_status(self, task_id: int) -> str:
        row = self.db.execute("SELECT status FROM tasks WHERE id=?", (task_id,)).fetchone()
        if row is None:
            raise KeyError(task_id)
        return str(row["status"])

    def audit_events(self) -> list[str]:
        return [row["event"] for row in self.db.execute("SELECT event FROM audit ORDER BY id")]

    def close(self) -> None:
        self.db.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        self.close()

    def audit(self, task_id: int) -> list[str]:
        return [
            row["event"]
            for row in self.db.execute("SELECT event FROM audit WHERE task_id=? ORDER BY id", (task_id,))
        ]

    def _audit(self, task_id: int | None, event: str) -> None:
        self.db.execute("INSERT INTO audit(task_id,event,at) VALUES (?,?,?)", (task_id, event, time.time()))


if __name__ == "__main__":
    core = HafsOSCore()
    core.grant("Veyra", "draft")
    core.grant("Reviewer", "verify_evidence")
    task = core.create_task("Draft a low-risk brief", "low", "draft", 1)
    evidence_id = core.add_evidence(task, "source-a", "requirements confirmed")
    core.verify_evidence(evidence_id, verifier="Reviewer")
    print(core.decide(task, "Veyra"))
