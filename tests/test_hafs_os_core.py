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
        core.grant("reviewer", "verify_evidence")
        evidence_id = core.add_evidence(task, "source-a", "ok", submitted_by="trader")
        core.verify_evidence(evidence_id, verifier="reviewer")
        self.assertEqual(core.decide(task, "agent"), Decision.ACT)

    def test_evidence_cannot_be_self_marked_verified(self):
        core = HafsOSCore()
        task = core.create_task("x", "low", "write", 1)
        evidence_id = core.add_evidence(task, "source-a", "ok", submitted_by="trader")
        with self.assertRaises(PermissionError):
            core.verify_evidence(evidence_id, verifier="untrusted")
        self.assertEqual(core.decide(task, "agent"), Decision.ASK)

    def test_high_risk_requires_distinct_sources_and_verifiers(self):
        core = HafsOSCore()
        core.grant("agent", "write")
        core.grant("reviewer", "verify_evidence")
        task = core.create_task("x", "high", "write", 1)
        first = core.add_evidence(task, "source-a", "ok", submitted_by="trader")
        second = core.add_evidence(task, "source-b", "ok", submitted_by="trader")
        core.verify_evidence(first, verifier="reviewer")
        core.verify_evidence(second, verifier="reviewer")
        self.assertEqual(core.decide(task, "agent"), Decision.ESCALATE)

    def test_source_verifier_pairs_require_one_to_one_matching(self):
        core = HafsOSCore()
        core.grant("agent", "write")
        for verifier in ("v1", "v2", "v3"):
            core.grant(verifier, "verify_evidence")
        task = core.create_task("x", "medium", "write", 3)
        evidence = [
            ("source-a", "v1"),
            ("source-a", "v2"),
            ("source-a", "v3"),
            ("source-b", "v1"),
            ("source-c", "v1"),
        ]
        for source, verifier in evidence:
            evidence_id = core.add_evidence(task, source, "ok", submitted_by="trader")
            core.verify_evidence(evidence_id, verifier=verifier)
        self.assertEqual(core.decide(task, "agent"), Decision.VERIFY)

    def test_action_agent_cannot_count_as_its_own_independent_verifier(self):
        core = HafsOSCore()
        core.grant("agent", "write")
        core.grant("agent", "verify_evidence")
        core.grant("reviewer", "verify_evidence")
        task = core.create_task("x", "high", "write", 2)
        first = core.add_evidence(task, "source-a", "ok", submitted_by="trader")
        second = core.add_evidence(task, "source-b", "ok", submitted_by="trader")
        core.verify_evidence(first, verifier="agent")
        core.verify_evidence(second, verifier="reviewer")
        self.assertEqual(core.decide(task, "agent"), Decision.VERIFY)

    def test_submitter_cannot_verify_own_evidence(self):
        core = HafsOSCore()
        core.grant("trader", "verify_evidence")
        task = core.create_task("x", "low", "write", 1)
        evidence_id = core.add_evidence(task, "source-a", "ok", submitted_by="trader")
        with self.assertRaises(PermissionError):
            core.verify_evidence(evidence_id, verifier="trader")

    def test_task_status_tracks_gate_decision(self):
        core = HafsOSCore()
        core.grant("agent", "write")
        task = core.create_task("x", "medium", "write", 1)
        self.assertEqual(core.decide(task, "agent"), Decision.VERIFY)
        self.assertEqual(core.task_status(task), "awaiting_evidence")

    def test_critical_always_escalates(self):
        core = HafsOSCore()
        core.grant("agent", "write")
        task = core.create_task("x", "critical", "write", 0)
        self.assertEqual(core.decide(task, "agent"), Decision.ESCALATE)


if __name__ == "__main__":
    unittest.main()
