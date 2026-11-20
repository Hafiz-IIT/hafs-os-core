# GitHub Portfolio Deep Audit — 2026-11-18

## Scope and method

This pass inventories 33 project repositories plus the GitHub profile repository. The profile README is excluded from analysis and edits. Repository READMEs are used only to establish project purpose; no profile README content is part of the audit. The review inspects repository metadata, non-profile source trees, GitHub Actions runs on active audit/research branches, open pull-request structure, representative implementation and test files, and research manuscripts/protocols.

**Execution evidence:** 33 project repositories have configured GitHub Actions; their latest audit/research-branch runs completed successfully at the time of the initial sweep. The GitHub profile repository has no workflow. Subsequent focused fixes below have their own CI runs.

**Important boundary:** CI success means only that configured tests/builds passed. It is not formal verification, scientific peer review, production deployment, or real-world validation. This is a first deep-audit pass, not a line-by-line formal security review of every file in every repository.

The GitHub profile README is excluded and was not modified.

## Repository inventory

| Repository | Purpose | Evidence maturity / next validation |
|---|---|---|
| `EXIM-AI-Evidence-Gated-Autonomy` | Evidence sufficiency, provenance, witness independence and consequential action authorization | Strongest research line; extensive versioned synthetic experiments. Historical-vs-reconstructed result lineage, OOD analysis and actual model evaluation remain open |
| `agent-evidence-probes` | Tests evidence sufficiency and evidence failure modes for agents | Executable prototype; broaden benchmark families and evaluate generalization |
| `memory-governor` | Memory lifecycle, sensitivity, retention and provenance governance | Executable policy prototype; needs adversarial threat model and retention/retrieval trade-off benchmark |
| `safe-rl-action-gate` | Deterministic action gate for bounded control actions | Tested scalar control prototype; needs dynamic constraints, disturbances and explicit invariant assumptions |
| `multilingual-reliability-bench` | Paired multilingual reliability evaluation | Benchmark scaffold; dataset provenance, language coverage, native-speaker validation and model/version freeze needed |
| `exim-document-truth-bench` | Cross-document EXIM consistency and evidence checks | Synthetic benchmark; broaden document variation and per-family error analysis |
| `exim-copilot-core` | Role-aware EXIM workflow core | Software prototype; no claim of live customs/ICEGATE integration or operational validation |
| `secure-doc-rag-agent` | Grounded document retrieval with tenant/privacy boundaries | Tested prototype; retrieval-quality, prompt-injection and cross-tenant adversarial evaluation needed |
| `cargo-scan-consistency-lab` | Consistency checks across cargo/sensor observations | Synthetic evidence prototype; no certified physical sensor or scanner validation |
| `hafs-os-core` | Task, permission, evidence and approval orchestration for the personal AI OS concept | SQLite-backed prototype; one-to-one source/verifier matching corrected in this pass; not a production multi-agent runtime |
| `agency-qa-orchestrator` | Requirement-to-artifact traceability and delivery readiness | Evidence-based QA prototype; PR #2 adds strict boolean verification and evidence references |
| `logistics-optimization-lab` | Cost/time/risk routing and Pareto trade-offs | Synthetic optimization lab; validate objective weights and constraints against real operational data |
| `cold-chain-digital-twin` | Thermal-state and cold-chain excursion simulation | Synthetic digital-twin prototype; calibrate against logged temperature/sensor traces |
| `port-operations-simulator` | Berth, queue and port-operation simulation | Simulation prototype; calibrate distributions and operating constraints against real port data |
| `multi-agent-logistics-sim` | Capacity-aware multi-agent task allocation | Simulation prototype; test congestion, fairness, failures and adversarial agents |
| `traffic-incident-routing-lab` | Time-dependent routing under incident delays | Synthetic routing lab; test network-scale data, non-FIFO edge cases and real traffic traces |
| `college-ops-copilot-core` | Administrative college workflow assistance | Software prototype; authentication, privacy and real workflow validation needed |
| `hospital-ops-helpdesk` | Administrative hospital helpdesk workflow | Non-clinical administrative prototype; maintain strict boundary against clinical decision-making |
| `predictive-intelligence-platform` | Forecasting and anomaly-detection platform | Prototype; require temporal holdouts, simple baselines, calibration and backtesting |
| `privacy-aware-recommender-lab` | Recommendation with privacy-aware constraints | Prototype; define threat model and measurable privacy guarantees before claiming differential privacy |
| `underwater-lifi-simulator` | Underwater optical link attenuation, SNR, BER and range modeling | Quantitative simulator; physical calibration and uncertainty analysis remain necessary |
| `institutional-evidence-tracker` | Evidence, accountability and decision-trail tracking | Workflow prototype; test identity, access control, tamper resistance and institutional deployment assumptions |
| `resturant-order-management` | Node/Express/MongoDB menu, order, feedback and admin API | Earlier application with new admin-auth hardening; runtime/dependency and login-abuse testing still incomplete |
| `Smart-City-Management-Management` | Smart-city incident, sensor and administrative workflow demo | Python application smoke-tested; sensor streams/predictions remain synthetic and classifier is a heuristic |
| `Hafiz-IIT` | GitHub profile and portfolio documentation | Presentation/index layer; README explicitly excluded from this audit |
| `residual-rl-linear-priors` | Scalar linear baseline plus fixed deterministic residual | Scaffold only; no trained RL policy or statistical prior |
| `residual-rl-linear-priors-paper` | Research protocol for residual control with a fixed linear baseline | LaTeX-compiling protocol; no empirical RL results |
| `koopman-control-lab` | Scalar EDMD-style prediction benchmark | Completed synthetic pilot: five maps, ten seeds, baseline and degree-2/3 models; higher-dimensional/noisy/control evaluation remains open |
| `koopman-control-paper` | Manuscript for scalar Koopman-lifted prediction | Compiles; claims scoped to synthetic prediction, not MPC/control validation |
| `bayesian-safe-rl-lab` | Scalar Normal–Normal posterior and interval action gate | Prototype only; no complete Bayesian RL algorithm or formal safety guarantee |
| `bayesian-safe-rl-paper` | Manuscript for scalar Bayesian uncertainty gating | Compiles; calibration, prior-misspecification and sequential-control evidence absent |
| `hybrid-lqr-rl-control` | Scalar linear feedback plus fixed cubic residual | Prototype only; function names corrected to avoid implying LQR or learned RL |
| `hybrid-lqr-rl-paper` | Research protocol for hybrid linear feedback with fixed residual | Compiles; no Riccati-derived LQR or trained residual policy |
| `exim-multimodal-cargo-framework-paper` | Proposed multimodal cargo/document and customs-assistance architecture | Design manuscript; no physical scanner, certified hardware or deployed customs integration |

## Confirmed defects and repairs in this audit pass

| ID | Repository | Finding | Repair made | Verification |
|---|---|---|---|---|
| A-01 | Smart-City-Management-Management | A classifier test was indented after `unittest.main()`, outside the test class, so CI never discovered it | Moved it into the test class before the main guard | CI run 44191202229 passed on the updated commit |
| A-02 | hafs-os-core | `min(distinct sources, distinct verifiers)` could overcount independent evidence when source/verifier relationships were correlated; the acting agent could also count as its own verifier | Replaced the count with maximum one-to-one bipartite matching and excluded the acting agent from independent verifier edges; added regression tests | CI run 44191285533 passed on the updated commit |
| A-03 | EXIM-AI-Evidence-Gated-Autonomy | Character-count/3 input-token approximation was described as a conservative upper bound, and the preflight budget was presented as if it were a hard spend cap | Renamed output fields and configuration to preflight estimates, clarified non-guaranteed approximation, preserved a deprecated config alias, and aligned tests/docs | A first run exposed one stale assertion; it was corrected. Final run for the updated head is pending at time of this report |
| A-04 | hybrid-lqr-rl-control | Functions named `lqr_prior` and `learned_residual` overstated the implementation: scalar proportional feedback and a fixed cubic residual | Renamed to `linear_feedback_prior` and `fixed_cubic_residual`; updated tests | CI run 44191651136 passed on the updated commit |
| A-05 | residual-rl-linear-priors-paper | Title implied statistical priors not present in the companion code | Renamed to “Residual Control with a Fixed Linear Baseline” | LaTeX CI triggered; verify latest run before merge |
| A-06 | hybrid-lqr-rl-paper | Abstract could imply the current fixed residual was learned | Clarified that the learned residual is the proposed research direction, while the companion code remains a fixed residual | LaTeX CI triggered; verify latest run before merge |
| A-07 | Hafiz-IIT portfolio docs | Research pipeline incorrectly called EGA arXiv-ready and used outdated control-manuscript titles/scopes | Draft PR #2 updates only `RESEARCH_PAPER_PIPELINE.md`; profile README untouched | Draft PR: https://github.com/Hafiz-IIT/Hafiz-IIT/pull/2 |

| A-08 | cold-chain-digital-twin | Controlled simulation still counted a full timestep when only part of the interval was above the excursion threshold | Shared a linearly interpolated threshold-duration function between open-loop and controlled simulations; added finite-input checks and documented explicit-Euler/calibration limits | CI runs 44192707636 and 44192707716 passed |
| A-09 | privacy-aware-recommender-lab | Consent audit events retained raw preference text | Event log now records action type only; evaluation docs explicitly state there is no differential privacy, encryption or verified cohort protection | CI run 44192757371 passed |
| A-10 | memory-governor | `forget` only invalidated a row, leaving its text in the active memories table | `forget` now deletes the active row and tests the deletion; docs distinguish row deletion from guaranteed secure erasure | CI runs 44193099713 and 44193099620 passed |
| A-11 | secure-doc-rag-agent | A string could be supplied as a sensitivity allowlist and interpreted as a character collection | Reject string allowlists and added regression test | CI run 44193037673 passed |
| A-12 | secure-doc-rag-agent | Tenant/principal identifiers are supplied by callers, not authenticated by the retrieval layer | Documentation now requires trusted identity claims from an upstream authenticated authorization layer; prototype is not described as standalone secure storage | Documentation/test workflow passed in run 44193037673 |

| A-13 | institutional-evidence-tracker | Verifier labels were caller-supplied and the audit log was mutable/in-memory, without authenticated identity or tamper evidence | Evaluation documentation now explicitly limits verifier labels, audit durability and legal-evidence claims | Documentation-only update; existing tests remain green |
| A-14 | agent-evidence-probes | Independence groups and freshness timestamps are caller-asserted; lexical conflict detection is not semantic verification | Evaluation documentation now states the authentication, provenance, trusted-time and semantic limits | Documentation-only update; existing tests remain green |


## 2026-11-20 follow-up: deeper implementation and evaluation pass

The following changes were made after the initial 2026-11-18 inventory. All remain on research/audit branches; no main branch was modified.

| ID | Repository | Additional defect or limitation found | Repair / disposition | Latest verification |
|---|---|---|---|---|
| A-15 | agent-evidence-probes | Tier 1 deterministic and Tier 2 LLM runners both used eval/run_100_eval.py and collided on data/probes_60.json; earlier runner exposed different schema assumptions | Split deterministic runner to eval/run_tier1_conformance.py; reserved eval/run_100_eval.py and requested dataset names for Tier 2; added 60 probes, prompt-blinding tests, provider-specific request formats, dataset validation, timestamped metadata, and separate raw-trace/summary outputs | [25 unit tests](https://github.com/Hafiz-IIT/agent-evidence-probes/actions/runs/44796385219), [Tier 1 evaluation](https://github.com/Hafiz-IIT/agent-evidence-probes/actions/runs/44796385223), [100-case validation](https://github.com/Hafiz-IIT/agent-evidence-probes/actions/runs/44796385131), [CI](https://github.com/Hafiz-IIT/agent-evidence-probes/actions/runs/44796385127) passed |
| A-16 | agent-evidence-probes | Evidence age, confidence and independent_group are caller-asserted; the prototype cannot authenticate lineage or detect semantic contradictions | Ported strict input validation and future-timestamp rejection; documented the trust boundary and preserved synthetic-only claim limits | Same central checks above passed |
| A-17 | EXIM-AI-Evidence-Gated-Autonomy | Invalid provenance metadata could be bypassed by the low-risk early return; canonical JSON hashing differed for Unicode payloads | Moved integrity checks ahead of low-risk return; aligned core hashing with attestation canonicalization; added low-risk and Bengali Unicode regression tests | Previous manuscript build passed at commit 0217644; updated build on commit 4637942 was still running at report update |
| A-18 | EXIM-AI-Evidence-Gated-Autonomy | Related-work bibliography used a generic SLSA homepage and an arXiv preprint where a published ICML record exists | Updated references to PMLR/NeurIPS/USENIX records and SLSA v1.2 specification; removed unused preprint entry | Included in the current manuscript-build workflow; final status pending |
| A-19 | EXIM-AI-Evidence-Gated-Autonomy | Legacy records without provenance envelopes remain accepted for compatibility; this is not equivalent to verified provenance | Explicitly retained as a limitation rather than silently changing historical benchmark semantics | Documented in PR #16 |
| A-20 | memory-governor | Atomic supersession alone did not cover all input validation and temporal edge cases; caller-supplied provenance is not authenticated | Consolidated the more complete Tier 2 branch implementation: input validation, strict expiry, future-date rejection, atomic supersession, durable rejection audit, context-manager support, security-boundary documentation and dataset tests | [Memory tests](https://github.com/Hafiz-IIT/memory-governor/actions/runs/44796608689) and [CI](https://github.com/Hafiz-IIT/memory-governor/actions/runs/44796608866) passed |
| A-21 | exim-document-truth-bench | Missing comparison fields could be silently ignored; duplicate document kinds raised an exception instead of a structured action | Missing required cross-document fields now yield VERIFY; duplicate kinds yield ESCALATE with structured report fields | [Tests](https://github.com/Hafiz-IIT/exim-document-truth-bench/actions/runs/44795727885) and [CI](https://github.com/Hafiz-IIT/exim-document-truth-bench/actions/runs/44795727895) passed |
| A-22 | cargo-scan-consistency-lab | A high-confidence category could suppress review despite a conflicting category from another independent sensor group | Any cross-category disagreement now requires review; added high-confidence conflict regression | [Tests](https://github.com/Hafiz-IIT/cargo-scan-consistency-lab/actions/runs/44795807192) and [CI](https://github.com/Hafiz-IIT/cargo-scan-consistency-lab/actions/runs/44795807207) passed |
| A-23 | safe-rl-action-gate | A finite state/action could overflow during simulation and raise outside the gate's fail-closed decision path | Simulation arithmetic/value errors now produce a BLOCK result with simulation_error; added regression | [Tests](https://github.com/Hafiz-IIT/safe-rl-action-gate/actions/runs/44795442058) and [CI](https://github.com/Hafiz-IIT/safe-rl-action-gate/actions/runs/44795442086) passed |
| A-24 | predictive-intelligence-platform | Intermediate sums/squared deviations could overflow on extreme but finite inputs and mask anomalies | Added scaled mean/variance calculations and explicit overflow rejection for unrepresentable MAE; added regressions | [Tests](https://github.com/Hafiz-IIT/predictive-intelligence-platform/actions/runs/44795511450) and CI passed |
| A-25 | hybrid-lqr-rl-control | Cubic residual exponentiation could overflow before the configured saturation bound was applied | Rewrote multiplication order to allow saturation and added extreme-state test | [CI](https://github.com/Hafiz-IIT/hybrid-lqr-rl-control/actions/runs/44795489215) passed on the later corrected commit |
| A-26 | bayesian-safe-rl-paper | Introduction repeated the same continuous-control citation and overstated the relevance to the scalar implementation | Removed duplicate sentence and clarified that the companion implementation is only a scalar uncertainty gate | Manuscript CI pending after wording update |
| A-27 | hybrid-lqr-rl-paper | Abstract described the fixed cubic residual as a bounded residual policy, which could imply a learned controller | Clarified the implemented component is a fixed cubic residual term, not a learned policy | Manuscript CI pending after wording update |
| A-28 | hafs-os-core | Task graph and approval records could be mutated through returned/public objects, bypassing cycle and approval checks; identifiers lacked consistent validation | Made graph dependency access read-only via snapshots, made approval records immutable, added validation/normalization and regression tests | Earlier tests passed at commit a03ddb2; latest validation commit de6cb was still running |

### Tier 2 evaluation status — important distinction

- The three datasets contain 60 general probes, 25 EXIM-context cases and 15 memory-governance cases.
- All 100 are constructed fictional scenarios. They are not real customs records, shipment documents, private user memories or observed incidents.
- Tier 2 compares two actual model API prompt conditions (neutral baseline versus evidence-gated prompt) when a provider key is supplied. It is a prompt-level intervention, not an external deterministic controller.
- The 100-case dataset validation passed without API calls. No Tier 2 model results have been generated because no provider credential was supplied.
- The 90-second target is best-effort; provider rate limits, latency and availability are outside the runner's control.

### Remaining focused blockers

1. Complete the EXIM manuscript build on commit 4637942 and the HAFS OS test/CI run on commit de6cb.
2. Run Tier 2 against one real provider/model, then repeat with a second model. Preserve raw traces and report failures/unscored cases.
3. Complete line-by-line audits of the remaining smaller application/simulation repositories; the current portfolio review is broad and deep but not a formal proof or full security audit.
4. For every manuscript, reconcile every result table with an immutable artifact/hash and check bibliography keys, DOI/venue, and claim scope.
5. Keep all PRs as drafts until the full audit and final presentation review are complete.

## Additional blockers retained

### Restaurant Order Management

- Password hashing, signed bearer authentication, admin bootstrap and protected routes are now present in the audit PR.
- Login has no demonstrated rate limiting or account lockout; synchronous scrypt can be abused for CPU exhaustion under repeated unauthenticated login attempts.
- CI currently checks syntax and utility/source-structure tests; it does not install dependencies, start MongoDB, boot the Express application or run authenticated HTTP integration tests.
- `server/package.json` exists, but a lockfile and deterministic install workflow were not found in the inspected tree.
- Do not deploy with real customer/admin data until these controls and integration tests are completed.

### Evidence-Gated Autonomy

- The original historical source/configuration for some v0.3 experiment tables was not recovered. New reconstruction v1/v2 results are explicitly separate and must not be described as exact historical reproduction.
- Benchmark v0.4 and later v2-v5 experiments are versioned synthetic studies; no real-world customs data or production security is established.
- Experiment 3 harness is implemented but has not made provider/API calls. Its model-family labels do not prove independent training or infrastructure.
- The manuscript checklist was updated on the Experiment 3 branch to distinguish historical reported results, new reconstructions and later extensions.

### Research novelty and scope

- The EGA v5 novelty boundary is narrow: a domain-inspired synthetic benchmark and empirical comparison of evidence-chain failures and authorization policies. Do not claim invention of independent corroboration, graph-aware quorums or epistemic fault domains.
- Koopman EDMD, residual RL, safe RL and hybrid feedback/residual control have established prior art. The current control extensions are prototypes or synthetic pilots, not novel general-purpose algorithms.
- The EXIM multimodal cargo framework is a design proposal until end-to-end implementation and independent operational validation exist.

## Pull-request and branch safety

All changes in this pass remain on existing audit/research branches or draft PRs. No pull request was merged and no project `main` branch was modified. Existing stacked EGA PRs remain separate; do not merge or close them automatically.

## Next work order

1. Complete CI verification for the updated EGA Experiment 3 cost-estimate changes and the two manuscript wording changes.
2. Add deterministic dependency installation and real HTTP/Mongo integration tests to Restaurant Order Management; add login throttling and document the deployment boundary.
3. Continue file-by-file correctness review of the remaining prototype repositories, prioritizing authentication, authorization, data validation, numerical stability, simulation assumptions and benchmark leakage.
4. Reconcile every research result table and manuscript claim with a versioned artifact and hash.
5. Keep all changes in draft PRs until the complete review is finished.
