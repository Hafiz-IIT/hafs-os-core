# ~haf.s__ OS Core

> **A governance spine for agentic work: tasks, permissions, evidence, risk, authority, and audit.**

The broader ~haf.s__ OS / Personal AI / Life Copilot concept needs a layer that decides not what an agent *can generate*, but what it is *authorized to do*. This repository implements that minimal governance core.

## Implemented
- SQLite-backed task state
- agent permission registry
- risk levels
- per-task evidence requirements
- verified evidence records
- ACT/ASK/VERIFY/ESCALATE authority gate
- audit trail

## Structure
- `hafs_os_core.py` — core
- `tests/` — tests
- `examples/` — reproducible example
- `docs/architecture.md` — architecture
- `docs/research-agenda.md` — experiments + manuscript lineage
- `STATUS.md` — maturity/claims
- `CITATION.cff` — citation metadata

## Run
```bash
python -m unittest discover -s tests -v
python hafs_os_core.py
```

## Pipeline
**task → risk + permission → evidence requirement → verified-source count → authority gate → decision → audit**

## Research lineage
This is the smallest implemented core of the long-running Personal AI Copilot / Life OS / ~haf.s__ OS idea: persistent context, modular agents, privacy, action authority, and act/ask/verify/escalate oversight.

## Evaluation
Construct task sets across permission/risk/evidence combinations and test whether authority is monotonic with verified evidence while critical tasks remain escalated.

## Maturity
**Research prototype.** This is not a complete personal operating system, autonomous browser, production multi-agent runtime, or integrated life-management product.
