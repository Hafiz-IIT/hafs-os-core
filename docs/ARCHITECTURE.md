# Architecture

## Flow
Task creation → risk classification → permission check → verified-evidence count → ACT / ASK / VERIFY / ESCALATE → persistent audit.

## Invariants
1. An agent without the required permission cannot ACT.
2. Evidence requirements are checked before authorization.
3. Critical-risk tasks escalate regardless of nominal permission.

## Trust boundary
Evidence is added unverified and can only be verified by an agent granted the `verify_evidence` permission. This is an application-level role check; source identity and independence labels remain caller-supplied and are not cryptographically authenticated.

## State invariants
- Every task requires at least one evidence item.
- Evidence cannot self-assert its verified state.
- High-risk tasks require two distinct verified source labels.
- Decision outcomes update the persisted task status.

## Governance rule
Authority, evidence, state transitions and failure reasons should remain explicit and auditable.
