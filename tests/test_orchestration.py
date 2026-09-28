import unittest

from orchestration import ApprovalLedger, DependencyCycle, TaskGraph


class OrchestrationTests(unittest.TestCase):
    def test_ready_tasks_respect_dependencies(self):
        graph = TaskGraph()
        graph.add_dependency("deploy", "test")
        graph.add_dependency("test", "build")
        self.assertEqual(graph.ready_tasks(set()), ["build"])
        self.assertEqual(graph.ready_tasks({"build"}), ["test"])

    def test_cycle_rejected(self):
        graph = TaskGraph()
        graph.add_dependency("a", "b")
        with self.assertRaises(DependencyCycle):
            graph.add_dependency("b", "a")

    def test_designated_approver_required(self):
        ledger = ApprovalLedger()
        ledger.request("t1", requested_by="agent-a", approver="human")
        with self.assertRaises(PermissionError):
            ledger.approve("t1", actor="agent-b")
        ledger.approve("t1", actor="human")
        self.assertTrue(ledger.is_approved("t1"))


if __name__ == "__main__":
    unittest.main()
