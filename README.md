# ~haf.s__ OS Core

<p align="center"><strong>An Evidence-Governed Operating Spine for AI Agents</strong><br/><sub>Tasks, permissions, evidence, risk and action authority in one inspectable control layer.</sub></p>

<p align="center"><img src="https://img.shields.io/badge/status-research%20prototype-blue" alt="Prototype"/> <img src="https://img.shields.io/badge/control-ACT%20%2F%20ASK%20%2F%20VERIFY%20%2F%20ESCALATE-purple" alt="Action governance"/></p>

## Core idea

The long-term `~haf.s__ OS` vision is a personal/company AI operating system. This repository isolates one concrete question:

> **How should a multi-agent system decide whether an agent has authority to perform an action?**

```
Task
 ↓
Risk classification
 ↓
Permission check
 ↓
Evidence requirement
 ↓
ACT / ASK / VERIFY / ESCALATE
 ↓
Audit
```

## Try it

```bash
python hafs_os_core.py
python -m unittest discover -s tests -v
```

The orchestration layer additionally provides dependency-aware task execution and a designated human approval ledger.

## Implemented

- SQLite task persistence
- agent permission registry
- risk levels
- evidence records
- evidence-count gates
- ACT / ASK / VERIFY / ESCALATE
- audit trail
- task dependency graph
- cycle detection
- designated approval ledger

## Portfolio role

This is the **control spine** connecting several research directions in this portfolio:

[Agent Evidence Probes](https://github.com/Hafiz-IIT/agent-evidence-probes) · [Memory Governor](https://github.com/Hafiz-IIT/memory-governor) · [Safe RL Action Gate](https://github.com/Hafiz-IIT/safe-rl-action-gate) · [Agency QA Orchestrator](https://github.com/Hafiz-IIT/agency-qa-orchestrator)

## Research boundary

Prototype only. It is not an autonomous company operating system, production agent platform, or claim of safe general autonomy.
