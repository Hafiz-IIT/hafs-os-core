# Portfolio Verification Matrix

Generated from GitHub Actions evidence on 2026-10-30.

## Status vocabulary

- **CI-VERIFIED** — a completed GitHub Actions run succeeded and its run SHA matches the current `main` HEAD.
- **INSPECTED** — repository structure/docs inspected without an execution claim.
- **MANUSCRIPT-INTEGRITY-VERIFIED** — manuscript companion integrity workflow succeeded at current HEAD; this is not an empirical experiment result.
- **SMOKE-VERIFIED** — application smoke test succeeded at current HEAD.
- **SYNTAX-VERIFIED** — syntax validation succeeded at current HEAD.

## Current evidence

| Repository | Current HEAD / verified SHA | Verification | Evidence |
|---|---|---|---|
| EXIM-AI-Evidence-Gated-Autonomy | `622c1ace9b78a0f98cb9e77808c32c47b6074372` | **CI-VERIFIED** | Manuscript Build run 41042970862; benchmark generation, integrity verification, table reproduction, LaTeX compilation all succeeded |
| agent-evidence-probes | `53f1711341743e028a4a654c1c2dfc1ffdb66137` | **CI-VERIFIED** | Run 37742319401; unit-tests succeeded |
| memory-governor | `5a2956d42426a9109d11cb78938229933c51fb26` | **CI-VERIFIED** | Run 37742328005; unit-tests succeeded |
| safe-rl-action-gate | `38c38d58b8b9d67872e9919060d7ee0391da6b9b` | **CI-VERIFIED** | Run 37742336670; unit-tests succeeded |
| multilingual-reliability-bench | `9fc99da3a2c16ad779d0eccfaac1b0b706b9f09f` | **CI-VERIFIED** | Run 37742346598; unit-tests succeeded |
| exim-document-truth-bench | `d4239ee61d29865e95b75d7897ee47433474e364` | **CI-VERIFIED** | Run 37742354909; deterministic tests succeeded |
| exim-copilot-core | `4aa03724efd0a30f1a100e7da3386ba20aec5d3b` | **CI-VERIFIED** | Run 37742370097; deterministic tests succeeded |
| secure-doc-rag-agent | `e6472c80a2fc4ea93772b15a957f8ae54026fc2f` | **CI-VERIFIED** | Run 37742380829; deterministic tests succeeded |
| cargo-scan-consistency-lab | `04173b697ddf3c88fcc96e29470431a1e5dcb5c8` | **CI-VERIFIED** | Run 37742390858; unit-tests succeeded |
| agency-qa-orchestrator | `d7d736ca048dc8af2b42b30a7802a4a3331960a6` | **CI-VERIFIED** | Run 37742399262; deterministic tests succeeded |
| logistics-optimization-lab | `2dea366c41d86a81c1c97281ccb8c1308eb0baca` | **CI-VERIFIED** | Run 37742406381; deterministic tests succeeded |
| cold-chain-digital-twin | `baa431211fa693de92f4acac1bc14e258cad8c30` | **CI-VERIFIED** | Run 37742422107; unit-tests succeeded |
| port-operations-simulator | `415fc2aabab1f265d5c991ee715256594dc2ddd6` | **CI-VERIFIED** | Run 37742431271; deterministic tests succeeded |
| multi-agent-logistics-sim | `d9f52f63346b7d2f05e6fb4d2ad92cbb6b225c45` | **CI-VERIFIED** | Run 37742438873; deterministic tests succeeded |
| traffic-incident-routing-lab | `7a837ddae1dd2e5fd99b3e360ed9c002e76680a8` | **CI-VERIFIED** | Run 37742447350; deterministic tests succeeded |
| college-ops-copilot-core | `37af4473068608509a36ac726c0d40179a904532` | **CI-VERIFIED** | Run 37742459297; deterministic tests succeeded |
| hospital-ops-helpdesk | `bff9d37d5c2b085be185b514d3c26784bba7388b` | **CI-VERIFIED** | Run 37742473939; deterministic tests succeeded |
| predictive-intelligence-platform | `6d94bd1191b4a95b54d6fc0c28e66add93e3b49c` | **CI-VERIFIED** | Run 37742484309; unit-tests succeeded |
| privacy-aware-recommender-lab | `023fc06b7b81729743e08dd352c49e456058bc45` | **CI-VERIFIED** | Run 37742492537; unit-tests succeeded |
| underwater-lifi-simulator | `56283fdb1136c97cb66f27a5f338b13503f89eed` | **CI-VERIFIED** | Run 37742501613; deterministic tests succeeded |
| institutional-evidence-tracker | `9356fe140f27cd29d1a303b7b037d17360664bb4` | **CI-VERIFIED** | Run 37742510159; deterministic tests succeeded |
| residual-rl-linear-priors | `14b5c22b2dfc9b7a3bbad429cb8094edaca28dfb` | **CI-VERIFIED** | Run 41042292844; deterministic tests succeeded |
| koopman-control-lab | `06391224f53b9974161999a0e942cc01666e4e18` | **CI-VERIFIED** | Run 41042305313; deterministic tests succeeded |
| bayesian-safe-rl-lab | `81f7b5ed7b5bc68b2ca2de46ad57d21cdb91e8f4` | **CI-VERIFIED** | Run 41042320255; deterministic tests succeeded |
| hybrid-lqr-rl-control | `31c9a75db3eaf8c6c8b9292a56b20e51f32e5b27` | **CI-VERIFIED** | Run 41042330805; deterministic tests succeeded |
| residual-rl-linear-priors-paper | `abe0487e9610e62843faecb6d13b30d090ae74b2` | **MANUSCRIPT-INTEGRITY-VERIFIED** | Run 37742789504; integrity job succeeded |
| koopman-control-paper | `ef20d85510b0e72d44d2f9131b3f07692dd3d64` | **MANUSCRIPT-INTEGRITY-VERIFIED** | Run 41042185365; integrity job succeeded |
| bayesian-safe-rl-paper | `4573fab1ac8f473212867662e3056a1d5be7ea40` | **MANUSCRIPT-INTEGRITY-VERIFIED** | Run 41042213446; declared manuscript-file verification succeeded |
| hybrid-lqr-rl-paper | `80214800288b3a7748f1c7ac44546be1114ac6b2` | **MANUSCRIPT-INTEGRITY-VERIFIED** | Run 41042236939; declared manuscript-file verification succeeded |
| exim-multimodal-cargo-framework-paper | `4265f4af9dd6fec2f5333b28bcecdb25008ecf35` | **MANUSCRIPT-INTEGRITY-VERIFIED** | Run 41042248738; declared manuscript-file verification succeeded |
| resturant-order-management | `756f8ef1acfa0c03d12177984fbe3e11621f000a` | **SYNTAX-VERIFIED** | Run 37742681750; JavaScript syntax check succeeded |
| Smart-City-Management-Management | `e3513072df247858627d7f81f5256313717ce824` | **SMOKE-VERIFIED** | Run 37742699007; dependency install and demo smoke tests succeeded |

## Documentation-only portfolio layers

- **hafs-os-core** — portfolio architecture/index; documentation and orchestration layer, not a single executable research experiment.
- **Hafiz-IIT** — GitHub profile README repository; presentation layer.

## Important interpretation boundary

CI verification means the repository's configured checks passed at the recorded current HEAD. It does **not** mean the research claims are externally validated, production deployed, scientifically peer reviewed, or safe for consequential real-world use.

The portfolio therefore keeps the evidence ladder explicit:

**concept → architecture → implementation → tested → reproducible → experimentally validated → externally validated → deployed**
