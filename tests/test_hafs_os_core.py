import unittest

from hafs_os_core import Decision, HafsOSCore


class HafsOSCoreTests(unittest.TestCase):
    def test_missing_permission_asks(self):
        core = HafsOSCore()
        task = core.create_task("x", "low", "write", 0)
        self.assertEqual(core.decide(task, "agent"), Decision.ASK)

    def test_missing_evidence_verifies(self):
        core = HafsOSCore()
        core.grant("agent", "write")
        task = core.create_task("x", "medium", "write", 1)
        self.assertEqual(core.decide(task, "agent"), Decision.VERIFY)

    def test_low_risk_verified_action_acts(self):
        core = HafsOSCore()
        core.grant("agent", "write")
        task = core.create_task("x", "low", "write", 1)
        core.add_evidence(task, "source-a", "ok", verified=True)
        self.assertEqual(core.decide(task, "agent"), Decision.ACT)

    def test_critical_always_escalates(self):
        core = HafsOSCore()
        core.grant("agent", "write")
        task = core.create_task("x", "critical", "write", 0)
        self.assertEqual(core.decide(task, "agent"), Decision.ESCALATE)


if __name__ == "__main__":
    unittest.main()
