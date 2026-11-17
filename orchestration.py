from __future__ import annotations

from dataclasses import dataclass


class DependencyCycle(ValueError):
    pass


class TaskGraph:
    def __init__(self):
        self.dependencies: dict[str, set[str]] = {}

    def add_task(self, task_id: str) -> None:
        self.dependencies.setdefault(task_id, set())

    def add_dependency(self, task_id: str, prerequisite_id: str) -> None:
        if any(not isinstance(value, str) or not value.strip() for value in (task_id, prerequisite_id)):
            raise ValueError("task identifiers must be non-empty strings")
        snapshot = {key: set(value) for key, value in self.dependencies.items()}
        try:
            self.add_task(task_id)
            self.add_task(prerequisite_id)
            self.dependencies[task_id].add(prerequisite_id)
            self.topological_order()
        except Exception:
            self.dependencies = snapshot
            raise

    def ready_tasks(self, completed: set[str]) -> list[str]:
        return sorted(
            task
            for task, prerequisites in self.dependencies.items()
            if task not in completed and prerequisites <= completed
        )

    def topological_order(self) -> list[str]:
        remaining = {k: set(v) for k, v in self.dependencies.items()}
        order: list[str] = []

        while remaining:
            ready = sorted(task for task, deps in remaining.items() if not deps)
            if not ready:
                raise DependencyCycle("task dependency graph contains a cycle")
            for task in ready:
                order.append(task)
                del remaining[task]
            for deps in remaining.values():
                deps.difference_update(ready)

        return order


@dataclass
class Approval:
    task_id: str
    requested_by: str
    approver: str
    approved: bool = False


class ApprovalLedger:
    def __init__(self):
        self._approvals: dict[str, Approval] = {}

    def request(self, task_id: str, *, requested_by: str, approver: str) -> Approval:
        if any(not isinstance(value, str) or not value.strip() for value in (task_id, requested_by, approver)):
            raise ValueError("task, requester and approver identifiers are required")
        if requested_by == approver:
            raise ValueError("requester and approver must be different actors")
        if task_id in self._approvals:
            raise ValueError("an approval request already exists for this task")
        approval = Approval(task_id, requested_by, approver, False)
        self._approvals[task_id] = approval
        return approval

    def approve(self, task_id: str, *, actor: str) -> None:
        approval = self._approvals.get(task_id)
        if approval is None:
            raise KeyError(task_id)
        if actor != approval.approver:
            raise PermissionError("actor is not the designated approver")
        if approval.approved:
            raise ValueError("approval has already been granted")
        approval.approved = True

    def is_approved(self, task_id: str) -> bool:
        approval = self._approvals.get(task_id)
        return bool(approval and approval.approved)
