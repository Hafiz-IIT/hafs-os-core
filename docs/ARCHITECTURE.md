# Architecture

## Flow
Task creation → risk classification → permission check → verified-evidence count → ACT / ASK / VERIFY / ESCALATE → persistent audit.

## Invariants
1. An agent without the required permission cannot ACT.
2. Evidence requirements are checked before authorization.
3. Critical-risk tasks escalate regardless of nominal permission.

## Governance rule
Authority, evidence, state transitions and failure reasons should remain explicit and auditable.
