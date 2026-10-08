# Portfolio Verification Matrix

Generated from GitHub Actions evidence on 2026-10-08. This is an evidence snapshot, not a claim that every repository has production or external validation.

## Status vocabulary

- **CI-VERIFIED** — a GitHub Actions run for the recorded current HEAD completed successfully.
- **CI-VERIFIED / SYNTAX** — CI executed JavaScript syntax checks; this is not full application/runtime validation.
- **CI-VERIFIED / SMOKE** — CI executed the repository's documented smoke test.
- **CI-VERIFIED / INTEGRITY** — CI verified the declared manuscript scaffold/integrity files; this is not experimental validation.
- **CI-VERIFIED / MANUSCRIPT-BUILD** — CI built the manuscript/reproducibility pipeline successfully.
- Historical failures remain in GitHub Actions history and are not hidden; only the recorded current-head result is used for the status below.

## Matrix

| Repository | Current HEAD verified | Evidence | Scope |
|---|---|---|---|
| agent-evidence-probes | `53f1711341743e028a4a654c1c2dfc1ffdb66137` | run 37742319321 | CI unit tests |
| memory-governor | `5a2956d42426a9109d11cb78938229933c51fb26` | run 37742328004 | CI unit tests |
| safe-rl-action-gate | `38c38d58b8b9d67872e9919060d7ee0391da6b9b` | run 37742336693 | CI unit tests |
| multilingual-reliability-bench | `9fc99da3a2c16ad779d0eccfaac1b0b706b9f09f` | run 37742346678 | CI unit tests |
| exim-document-truth-bench | `d4239ee61d29865e95b75d7897ee47433474e364` | run 37742354909 | CI unit tests |
| exim-copilot-core | `4aa03724efd0a30f1a100e7da3386ba20aec5d3b` | run 37742370097 | CI unit tests |
| secure-doc-rag-agent | `e6472c80a2fc4ea93772b15a957f8ae54026fc2f` | run 37742380829 | CI unit tests |
| cargo-scan-consistency-lab | `04173b697ddf3c88fcc96e29470431a1e5dcb5c8` | run 37742390873 | CI unit tests |
| agency-qa-orchestrator | `d7d736ca048dc8af2b42b30a7802a4a3331960a6` | run 37742399262 | CI unit tests |
| logistics-optimization-lab | `2dea366c41d86a81c1c97281ccb8c1308eb0baca` | run 37742406381 | CI unit tests |
| cold-chain-digital-twin | `baa431211fa693de92f4acac1bc14e258cad8c30` | run 37742422143 | CI unit tests |
| port-operations-simulator | `415fc2aabab1f265d5c991ee715256594dc2ddd6` | run 37742431271 | CI unit tests |
| multi-agent-logistics-sim | `d9f52f63346b7d2f05e6fb4d2ad92cbb6b225c45` | run 37742438873 | CI unit tests |
| traffic-incident-routing-lab | `7a837ddae1dd2e5fd99b3e360ed9c002e76680a8` | run 37742447350 | CI unit tests |
| college-ops-copilot-core | `37af4473068608509a36ac726c0d40179a904532` | run 37742459297 | CI unit tests |
| hospital-ops-helpdesk | `bff9d37d5c2b085be185b514d3c26784bba7388b` | run 37742473939 | CI unit tests |
| predictive-intelligence-platform | `6d94bd1191b4a95b54d6fc0c28e66add93e3b49c` | run 37742484299 | CI unit tests |
| privacy-aware-recommender-lab | `023fc06b7b81729743e08dd352c49e456058bc45` | run 37742492595 | CI unit tests |
| underwater-lifi-simulator | `56283fdb1136c97cb66f27a5f338b13503f89eed` | run 37742501613 | CI unit tests |
| institutional-evidence-tracker | `9356fe140f27cd29d1a303b7b037d17360664bb4` | run 37742510159 | CI unit tests |
| resturant-order-management | `756f8ef1acfa0c03d12177984fbe3e11621f000a` | run 37742681750 | CI JavaScript syntax |
| Smart-City-Management-Management | `e3513072df247858627d7f81f5256313717ce824` | run 37742699007 | CI Windows smoke test |
| residual-rl-linear-priors | `315ae8c8e5fb9ee4ca3695321c1cf0910382a661` | run 37742642983 | CI tests + documented demo |
| koopman-control-lab | `4431ee6cfb7f4c4a30be11f8636024c83e3845ee` | run 37742648993 | CI tests + documented demo |
| bayesian-safe-rl-lab | `d68f245b6b26a2ecaa697e65243f07c57d7246c9` | run 37742654565 | CI tests + documented demo |
| hybrid-lqr-rl-control | `adbe726d19ea086937e138d107521cdd15e3ebef` | run 37742661205 | CI tests + documented demo |
| residual-rl-linear-priors-paper | `abe0487e9610e62843faecb6d13b30d090ae74b2` | run 37742789504 | CI manuscript integrity |
| koopman-control-paper | `b2743a80d4e9a422131ccc544937c4a3ec6e2407` | run 37742797711 | CI manuscript integrity |
| bayesian-safe-rl-paper | `173861764c3742fe26b5513cc73b1609cc33a006` | run 37742808497 | CI manuscript integrity |
| hybrid-lqr-rl-paper | `b843eead8a247e1aa9710603bcdf335678975381` | run 37742958847 | CI manuscript integrity |
| exim-multimodal-cargo-framework-paper | `947e14f87ca217e2374caafed342204c3b45f6f1` | run 37742817883 | CI manuscript integrity |
| EXIM-AI-Evidence-Gated-Autonomy | `e6e554969ba63dfe69c5b9f08c35ceb3eb165fa8` | run 37737747859 | CI manuscript build + reproducibility |
| hafs-os-core | `7b0b6fa160ffe54314db5863b856ca7806f333f5` | run 37742844256 | CI unit tests |

## Important boundaries

- CI verification means the recorded automated checks executed successfully at the recorded commit. It does **not** mean production deployment, external validation, publication acceptance, regulatory approval, safety certification, or real-world hardware validation.
- Smart City was repaired after a genuine Windows checkout blocker was identified: the repository contained a file literally named `Install:`, which is invalid on Windows. That file was removed and the smoke-test workflow subsequently passed.
- The restaurant repository has no package manifest/lockfile in the inspected tree, so its CI was changed from an invalid npm-install assumption to JavaScript syntax verification. This does **not** constitute full application/runtime validation.
- Historical failing workflow runs remain visible. They were not rewritten or deleted.
- The Python portfolio CI failure pattern was traced to a custom status-publishing step rather than the test suites themselves. The status-publishing step was removed so workflow conclusions now reflect actual test execution.
- Research and manuscript repositories remain bounded by their documented prototype/simulation/scaffold status.

## Machine-readable snapshot

```json
{
  "generated": "2026-10-08",
  "total_repositories": 33,
  "current_head_ci_verified": 33,
  "production_validated": 0,
  "external_validation_claimed": 0,
  "hardware_validation_claimed": 0,
  "fabricated_green_pass_claimed": 0,
  "notes": [
    "CI verification is not production validation.",
    "Restaurant verification is syntax-only.",
    "Smart City verification is smoke-test scoped.",
    "Manuscript verification is integrity/build scoped.",
    "EGA verification includes manuscript build and reproducibility pipeline."
  ]
}
```
