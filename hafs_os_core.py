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
                verified INTEGER NOT NULL DEFAULT 0
            );
            CREATE TABLE IF NOT EXISTS audit(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id INTEGER,
                event TEXT NOT NULL,
                at REAL NOT NULL
            );
            """
        )

    def grant(self, agent: str, permission: str) -> None:
        self.db.execute("INSERT OR IGNORE INTO permissions VALUES (?, ?)", (agent, permission))
        self.db.commit()

    def create_task(self, description: str, risk: str, required_permission: str, evidence_required: int = 1) -> int:
        if risk not in RISK_ORDER:
            raise ValueError("unknown risk")
        cur = self.db.execute(
            "INSERT INTO tasks(description,risk,required_permission,evidence_required) VALUES (?,?,?,?)",
            (description, risk, required_permission, evidence_required),
        )
        task_id = int(cur.lastrowid)
        self._audit(task_id, "task-created")
        self.db.commit()
        return task_id

    def add_evidence(self, task_id: int, source: str, claim: str, verified: bool = False) -> None:
        self.db.execute(
            "INSERT INTO evidence(task_id,source,claim,verified) VALUES (?,?,?,?)",
            (task_id, source, claim, int(verified)),
        )
        self._audit(task_id, f"evidence:{source}:{'verified' if verified else 'unverified'}")
        self.db.commit()

    def decide(self, task_id: int, agent: str) -> Decision:
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

        self._audit(task_id, f"decision:{agent}:{decision.value}")
        self.db.commit()
        return decision

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
    task = core.create_task("Draft a low-risk brief", "low", "draft", 1)
    core.add_evidence(task, "source-a", "requirements confirmed", verified=True)
    print(core.decide(task, "Veyra"))
