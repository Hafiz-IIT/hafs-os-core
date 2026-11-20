# Portfolio Verification Matrix

**Current as of:** 2026-11-20  
**Scope:** 33 project repositories plus the GitHub profile repository. The profile README is excluded from analysis and edits.

The canonical, current portfolio audit is maintained in:

[docs/PORTFOLIO_DEEP_AUDIT_2026-11-18.md](docs/PORTFOLIO_DEEP_AUDIT_2026-11-18.md)

That report contains:
- Repository purpose and research-maturity boundaries.
- GitHub Actions evidence and current focused verification links.
- Confirmed defects, repairs, and remaining blockers.
- Separate treatment of synthetic conformance, real-LLM API evaluation, manuscript builds, and external validation.

## Verification vocabulary

- **CI green:** The configured tests/builds passed at the recorded commit.
- **Synthetic conformance:** Deterministic software behavior on authored test fixtures.
- **Empirical model evaluation:** Actual provider API responses with raw traces and model metadata.
- **Research protocol:** An experiment design or manuscript awaiting execution.
- **Externally validated:** Independent replication or real-world validation; not claimed by CI.

## Portfolio-wide interpretation

A passing workflow proves only that the configured checks passed. It does not prove formal safety, scientific novelty, generalization, production security, or operational deployment.

The evidence ladder remains:

**concept → architecture → implementation → tested → reproducible → experimentally validated → independently validated → deployed**

Do not promote a repository to a higher evidence level without the corresponding artifact and verification record.
