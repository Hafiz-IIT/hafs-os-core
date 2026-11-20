import unittest

from hafs_os_core import Decision, HafsOSCore


class HafsOSCoreTests(unittest.TestCase):
    def test_missing_permission_asks(self):
        core = HafsOSCore()
        task = core.create_task("x", "low", "write", 1)
        self.assertEqual(core.decide(task, "agent"), Decision.ASK)
        self.assertEqual(core.task_status(task), "awaiting_permission")

    def test_missing_evidence_verifies(self):
        core = HafsOSCore()
        core.grant("agent", "write")
        task = core.create_task("x", "medium", "write", 1)
        self.assertEqual(core.decide(task, "agent"), Decision.VERIFY)
        self.assertEqual(core.task_status(task), "awaiting_evidence")

    def test_evidence_cannot_self_assert_verification(self):
        core = HafsOSCore()
        core.grant("agent", "write")
        task = core.create_task("x", "low", "write", 1)
        with self.assertRaises(ValueError):
            core.add_evidence(task, "source-a", "ok", verified=True)
        evidence_id = core.add_evidence(task, "source-a", "ok")
        self.assertEqual(core.decide(task, "agent"), Decision.VERIFY)
        core.grant("reviewer", "verify_evidence")
        with self.assertRaises(PermissionError):
            core.verify_evidence(evidence_id, "agent")
        core.verify_evidence(evidence_id, "reviewer")
        self.assertEqual(core.decide(task, "agent"), Decision.ACT)
        self.assertEqual(core.task_status(task), "authorized")

    def test_evidence_required_must_be_positive(self):
        core = HafsOSCore()
        with self.assertRaises(ValueError):
            core.create_task("x", "low", "write", 0)
        with self.assertRaises(ValueError):
            core.create_task("x", "low", "write", -1)

    def test_evidence_requires_existing_task(self):
        core = HafsOSCore()
        with self.assertRaises(Exception):
            core.add_evidence(999, "source", "claim")

    def test_high_risk_requires_two_distinct_verified_sources(self):
        core = HafsOSCore()
        core.grant("agent", "write")
        core.grant("reviewer", "verify_evidence")
        task = core.create_task("x", "high", "write", 1)
        first = core.add_evidence(task, "same-source", "claim one")
        second = core.add_evidence(task, "same-source", "claim two")
        core.verify_evidence(first, "reviewer")
        core.verify_evidence(second, "reviewer")
        self.assertEqual(core.decide(task, "agent"), Decision.ESCALATE)
        third = core.add_evidence(task, "independent-source", "claim three")
        core.verify_evidence(third, "reviewer")
        self.assertEqual(core.decide(task, "agent"), Decision.ACT)

    def test_critical_always_escalates(self):
        core = HafsOSCore()
        core.grant("agent", "write")
        task = core.create_task("x", "critical", "write", 1)
        self.assertEqual(core.decide(task, "agent"), Decision.ESCALATE)
        self.assertEqual(core.task_status(task), "escalated")


if __name__ == "__main__":
    unittest.main()
