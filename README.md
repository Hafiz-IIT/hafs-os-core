# ~haf.s__ OS Core

A compact implementation of the governance spine behind the broader personal/company AI operating-system concept.

The core idea is simple: agents should not receive unlimited authority. Tasks carry risk, agents carry permissions, actions require evidence, and the system can choose **ACT / ASK / VERIFY / ESCALATE**.

## Implemented
- persistent SQLite task store
- agent permission registry
- evidence records
- risk levels
- decision gate: ACT / ASK / VERIFY / ESCALATE
- audit trail
- tests for permission, evidence and high-risk escalation

## Run
```bash
python -m unittest discover -s tests -v
python hafs_os_core.py
```

## Scope
This is the core governance/state layer, not the complete ~haf.s__ OS product. It does not claim production integrations, autonomous browsing, or deployed multi-agent infrastructure.
