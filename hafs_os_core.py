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
                evidence_required INTEGER NOT NULL CHECK(evidence_required >= 1),
                status TEXT NOT NULL DEFAULT 'pending'
            );
            CREATE TABLE IF NOT EXISTS permissions(
                agent TEXT NOT NULL,
                permission TEXT NOT NULL,
                PRIMARY KEY(agent, permission)
            );
            CREATE TABLE IF NOT EXISTS evidence(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id INTEGER NOT NULL REFERENCES tasks(id),
                source TEXT NOT NULL,
                claim TEXT NOT NULL,
                verified INTEGER NOT NULL DEFAULT 0 CHECK(verified IN (0, 1))
            );
            CREATE TABLE IF NOT EXISTS audit(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id INTEGER,
                event TEXT NOT NULL,
                at REAL NOT NULL
            );
            """
        )

    @staticmethod
    def _required_text(name: str, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{name} must be a non-empty string")

    def grant(self, agent: str, permission: str) -> None:
        self._required_text("agent", agent)
        self._required_text("permission", permission)
        self.db.execute("INSERT OR IGNORE INTO permissions VALUES (?, ?)", (agent, permission))
        self._audit(None, f"permission-granted:{agent}:{permission}")
        self.db.commit()

    def create_task(self, description: str, risk: str, required_permission: str,
                    evidence_required: int = 1) -> int:
        self._required_text("description", description)
        self._required_text("required_permission", required_permission)
        if risk not in RISK_ORDER:
            raise ValueError("unknown risk")
        if isinstance(evidence_required, bool) or not isinstance(evidence_required, int) or evidence_required < 1:
            raise ValueError("evidence_required must be a positive integer")
        cur = self.db.execute(
            "INSERT INTO tasks(description,risk,required_permission,evidence_required) VALUES (?,?,?,?)",
            (description, risk, required_permission, evidence_required),
        )
        task_id = int(cur.lastrowid)
        self._audit(task_id, "task-created")
        self.db.commit()
        return task_id

    def add_evidence(self, task_id: int, source: str, claim: str, verified: bool = False) -> int:
        self._required_text("source", source)
        self._required_text("claim", claim)
        if verified:
            raise ValueError("evidence cannot self-assert verification; use verify_evidence()")
        if self.db.execute("SELECT 1 FROM tasks WHERE id=?", (task_id,)).fetchone() is None:
            raise KeyError(task_id)
        cur = self.db.execute(
            "INSERT INTO evidence(task_id,source,claim,verified) VALUES (?,?,?,0)",
            (task_id, source, claim),
        )
        evidence_id = int(cur.lastrowid)
        self._audit(task_id, f"evidence-added:{evidence_id}:{source}:unverified")
        self.db.commit()
        return evidence_id

    def verify_evidence(self, evidence_id: int, verifier: str) -> None:
        self._required_text("verifier", verifier)
        permitted = self.db.execute(
            "SELECT 1 FROM permissions WHERE agent=? AND permission='verify_evidence'",
            (verifier,),
        ).fetchone()
        if permitted is None:
            raise PermissionError(f"{verifier} lacks verify_evidence permission")
        row = self.db.execute("SELECT task_id FROM evidence WHERE id=?", (evidence_id,)).fetchone()
        if row is None:
            raise KeyError(evidence_id)
        self.db.execute("UPDATE evidence SET verified=1 WHERE id=?", (evidence_id,))
        self._audit(row["task_id"], f"evidence-verified:{evidence_id}:{verifier}")
        self.db.commit()

    def decide(self, task_id: int, agent: str) -> Decision:
        self._required_text("agent", agent)
        task = self.db.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()
        if task is None:
            raise KeyError(task_id)

        permitted = self.db.execute(
            "SELECT 1 FROM permissions WHERE agent=? AND permission=?",
            (agent, task["required_permission"]),
        ).fetchone() is not None

        verified_count = self.db.execute(
            "SELECT COUNT(DISTINCT source) AS n FROM evidence WHERE task_id=? AND verified=1",
            (task_id,),
        ).fetchone()["n"]

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

    def audit(self, task_id: int) -> list[str]:
        return [
            row["event"]
            for row in self.db.execute("SELECT event FROM audit WHERE task_id=? ORDER BY id", (task_id,))
        ]

    def close(self) -> None:
        self.db.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        self.close()

    def _audit(self, task_id: int | None, event: str) -> None:
        self.db.execute("INSERT INTO audit(task_id,event,at) VALUES (?,?,?)", (task_id, event, time.time()))


if __name__ == "__main__":
    core = HafsOSCore()
    core.grant("Veyra", "draft")
    core.grant("Verifier", "verify_evidence")
    task = core.create_task("Draft a low-risk brief", "low", "draft", 1)
    evidence_id = core.add_evidence(task, "source-a", "requirements confirmed")
    core.verify_evidence(evidence_id, "Verifier")
    print(core.decide(task, "Veyra"))
