# Evaluation

## Question
Can explicit permission, evidence and risk gates make a modular agent operating system easier to reason about and audit?

## Metrics
- Unauthorized action rate
- Evidence-gate accuracy
- Critical-risk escalation rate
- Audit completeness
- Policy decision reproducibility
- Submitter/verifier separation violations

## Falsification
- An unpermissioned agent ACTs.
- A critical task bypasses escalation.
- Evidence requirements are ignored.
- An evidence submitter verifies their own evidence.
- High-risk ACT occurs without two distinct source/verifier pairs.
- A dependency cycle is committed to the task graph.

## Limitations
The current implementation uses caller-supplied identities and source labels. Distinct labels do not prove independent origins. Reviewer verification is an authenticated permission check only inside this in-memory/local prototype; there is no external identity provider, signed attestation, source retrieval, or tamper-evident log.
