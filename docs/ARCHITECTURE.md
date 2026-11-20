# Architecture

## Flow
Task creation → risk classification → permission check → evidence submission → independent reviewer verification → source/verifier quorum check → ACT / ASK / VERIFY / ESCALATE → task-state update and audit event.

## Invariants
1. An agent without the required permission cannot ACT.
2. Evidence is unverified on submission; it cannot self-assert its verified state.
3. The evidence submitter cannot verify their own evidence.
4. High-risk actions require at least two distinct source/verifier pairs, and the acting agent cannot count as one of those verifiers.
5. Critical-risk tasks escalate regardless of nominal permission.
6. Dependency graph changes that introduce a cycle are rolled back.
7. Approval requests require a distinct requester and designated approver; duplicate requests are rejected.

## Trust boundary
Agent, submitter, verifier and source identifiers are supplied by callers. The prototype checks string identity and permission records; it does not authenticate those identities, validate source independence cryptographically, or prove that a verifier actually inspected the source. SQLite audit events are append-only through this API but are not hash-chained or tamper-evident against direct database modification.
