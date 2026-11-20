import unittest
from dataclasses import FrozenInstanceError

from orchestration import ApprovalLedger, DependencyCycle, TaskGraph


class OrchestrationTests(unittest.TestCase):
    def test_ready_tasks_respect_dependencies(self):
        graph = TaskGraph()
        graph.add_dependency("deploy", "test")
        graph.add_dependency("test", "build")
        self.assertEqual(graph.ready_tasks(set()), ["build"])
        self.assertEqual(graph.ready_tasks({"build"}), ["test"])

    def test_empty_task_identifier_rejected(self):
        graph = TaskGraph()
        with self.assertRaises(ValueError):
            graph.add_task(" ")

    def test_dependency_snapshot_cannot_mutate_internal_graph(self):
        graph = TaskGraph()
        graph.add_dependency("deploy", "test")
        snapshot = graph.dependencies
        with self.assertRaises(AttributeError):
            snapshot["deploy"].add("untrusted")
        self.assertEqual(graph.dependencies["deploy"], frozenset({"test"}))

    def test_cycle_rejected_without_corrupting_graph(self):
        graph = TaskGraph()
        graph.add_dependency("a", "b")
        before = {key: set(value) for key, value in graph.dependencies.items()}
        with self.assertRaises(DependencyCycle):
            graph.add_dependency("b", "a")
        self.assertEqual(graph.dependencies, before)
        self.assertEqual(graph.topological_order(), ["b", "a"])

    def test_designated_approver_required(self):
        ledger = ApprovalLedger()
        approval = ledger.request("t1", requested_by="agent-a", approver="human")
        with self.assertRaises(FrozenInstanceError):
            approval.approved = True
        with self.assertRaises(PermissionError):
            ledger.approve("t1", actor="agent-b")
        ledger.approve("t1", actor="human")
        self.assertTrue(ledger.is_approved("t1"))
        with self.assertRaises(ValueError):
            ledger.approve("t1", actor="human")

    def test_requester_cannot_approve_own_request(self):
        ledger = ApprovalLedger()
        with self.assertRaises(ValueError):
            ledger.request("t1", requested_by="same", approver="same")

    def test_duplicate_approval_request_is_rejected(self):
        ledger = ApprovalLedger()
        ledger.request("t1", requested_by="agent", approver="human")
        with self.assertRaises(ValueError):
            ledger.request("t1", requested_by="agent", approver="other-human")


if __name__ == "__main__":
    unittest.main()
