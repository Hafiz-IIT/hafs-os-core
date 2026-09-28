# ~haf.s__ OS Core

> Governance and task-orchestration spine for ~haf.s__ OS: permissions, evidence requirements, risk tiers, audit and action authority.

## Status
**Reproducible prototype** with executable Python, tests, CI, architecture docs, evaluation criteria, roadmap, and citation metadata.

## Problem
A multi-agent personal/company AI operating system needs explicit authority boundaries. Agents should not inherit unlimited permission merely because they can generate a plausible action.

## Architecture
Task creation → risk classification → permission check → verified-evidence count → ACT / ASK / VERIFY / ESCALATE → persistent audit.

## Run
```bash
python -m unittest discover -s tests -v
python hafs_os_core.py
```

## Implemented
- SQLite task store
- Agent permission registry
- Risk levels
- Evidence records
- Evidence-count gate
- ACT / ASK / VERIFY / ESCALATE policy
- Audit history
- Tests and CI

## Research lineage
- *Scalable Architectures for Distributed Intelligent Agents*
- *Human–AI Symbiosis: Toward Next-Generation Consumer Applications*
- *Modular AI Frameworks for Multi-Vertical Startup Innovation*

## Evaluation
Tests cover missing permission, insufficient evidence, low-risk authorized action and mandatory critical-risk escalation.

## Limitations
- Core governance/state layer only
- No production multi-agent runtime
- No external tool credentials
- No browser/action integrations bundled

## License
MIT.

## Extended implementation

- `orchestration.py` — task dependency graph, cycle detection and designated approval ledger.
- `docs/PORTFOLIO_INDEX.md` — canonical public portfolio map.
- `docs/RECOVERED_RESEARCH_MAP.md` — recovered 35-paper research map with publication boundaries.
- `docs/RECOVERED_100_PRODUCT_ECOSYSTEM.md` — long-term product vision, explicitly not an implementation claim.
- `docs/GITHUB_PROFILE_README_DRAFT.md` — staged evidence-based GitHub profile README.
- `scripts/apply-github-metadata.ps1` — sets descriptions/topics for the 21 public repositories using GitHub CLI.
- `scripts/create-next-repos.ps1` — creates the next project/paper repository shells.
