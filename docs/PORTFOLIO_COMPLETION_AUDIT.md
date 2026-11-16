# Portfolio and Repository Audit — 2026-11-17

## Inventory and audit scope

The linked GitHub account exposes **34 repositories**:
- 1 profile repository: [Hafiz-IIT](https://github.com/Hafiz-IIT/Hafiz-IIT)
- 33 project repositories, including the implementation, EXIM, agent-governance, logistics, control, and manuscript work.

The canonical inventory remains in [PORTFOLIO_INDEX.md](PORTFOLIO_INDEX.md).

This review inventoried all 34 repository trees, examined the primary implementation modules in the executable projects, inspected representative tests and CI workflows, and reviewed the five new manuscript sources, protocols, claims ledgers, and result manifests. This is an engineering/research audit pass, not a claim that every line of every file has received formal verification.

## Repository metadata

The user has manually added repository descriptions through GitHub in Chrome. Topics remain pending. The connected GitHub tooling can inspect repository contents and Actions, but does not expose a repository About/topics write operation. Topics therefore need to be added through each repository's About settings when convenient; this does not block research work.

The profile README's education and domain-background wording is user-protected and must not be changed without explicit permission.

## Verified corrections made during this audit

### Restaurant Order Management

Repository: [resturant-order-management](https://github.com/Hafiz-IIT/resturant-order-management)

- Corrected the case-sensitive import of the menu route and its controller.
- Created `server/routes/admin.routes.js`, updated the server import, and removed the incorrectly named `admin.routes,js`.
- Corrected the admin model import to match `Admin.model.js`.
- Removed the committed local `server/.env` file. The inspected values were development placeholders, not evidence of real production credentials.
- Added a root `.gitignore` for local environment files, dependencies, and generated files.
- Latest observed GitHub Actions syntax-check run passed.

Remaining concerns:
- The workflow currently checks JavaScript syntax; it does not install dependencies or boot the Express application. The repository tree does not contain a `package.json` or lockfile, so runtime verification remains outstanding.
- The admin model/controller store passwords without hashing and expose admin listing/creation routes without visible authentication/authorization middleware. Do not deploy this application with real user data until these are addressed.
- The README already acknowledges the plaintext-password limitation; it must remain a prototype until the security work is complete.

### Smart City Management

Repository: [Smart-City-Management-Management](https://github.com/Hafiz-IIT/Smart-City-Management-Management)

- Corrected Python imports to match the actual `App/` directory capitalization.
- Corrected the template directory to `App/Templates`.
- Removed the mount for a nonexistent static directory.
- Replaced the Windows-only demo-seeder CI job with an Ubuntu application-import/route smoke test and added a test module.
- Latest observed GitHub Actions application smoke test passed.

Remaining concerns:
- Sensor streams and traffic/waste predictions are generated randomly. They are synthetic demonstrations, not trained forecasting models or live sensor integrations.
- The current incident classifier is a keyword heuristic with a default category; it is not a validated incident classifier.

## Research-critical findings

### Evidence-Gated Autonomy (EGA)

Repository: [EXIM-AI-Evidence-Gated-Autonomy](https://github.com/Hafiz-IIT/EXIM-AI-Evidence-Gated-Autonomy)

This is still the portfolio's strongest existing research line because it has a defined benchmark, multiple result tables, adversarial/provenance analyses, a manuscript, and explicit limitations. However, its current reproducibility claim needs repair before any preprint submission.

**Blocking reproducibility gap**
- The repository contains result CSVs for Experiments 1A–1D and 2A–2E, but the tree does not contain the experiment-runner source needed to regenerate the stochastic, OOD, provenance-attack, trust-root, and separation-of-duties result tables.
- `scripts/reproduce_all.py` runs benchmark generation, benchmark integrity verification, and table printing. It does not rerun the experiments that produced the checked-in result CSVs.
- `scripts/reproduce_tables.py` reads and prints the existing CSVs; it does not independently recompute the reported metrics.
- `generate_benchmark.py` writes a smaller manifest than the richer committed `data/benchmark/manifest.json`. Running the generator overwrites some of the committed manifest metadata in the working tree.
- The current CI therefore demonstrates benchmark regeneration, integrity checks, table loading, and LaTeX compilation—not full regeneration of every experimental result.

**Policy correctness issue — fix implemented, dataset coverage still pending**
- The previous `src/core.py` completeness feature checked only whether the declaration existed. That allowed a missing packing list to be treated as complete.
- The rule is now corrected to require invoice, packing list, and declaration. Regression tests cover missing invoice, missing packing list, and missing declaration; the complete clean case remains allowed.
- Policy regression tests, benchmark generation, integrity checks, existing-table loading, and LaTeX compilation passed in GitHub Actions: [run 43946899874](https://github.com/Hafiz-IIT/EXIM-AI-Evidence-Gated-Autonomy/actions/runs/43946899874).
- The current v0.3 synthetic benchmark still does not systematically include missing-invoice and missing-packing-list cases. The new tests validate policy behaviour, but historical result tables do not measure those cases.

**Required EGA work**
1. Reconstruct and version the missing experiment runners.
2. Freeze the exact policies, stochastic assumptions, seeds, and cost matrix.
3. Regenerate all result tables from source, not from the checked-in CSVs.
4. Keep the generator and committed manifest schemas consistent.
5. Add missing-invoice, missing-packing-list, duplicate-document, and corrupted-provenance cases in a new benchmark version.
6. Rerun all experiments under the new benchmark/policy version.
7. Reconcile every paper claim and result table against regenerated outputs.

The current synthetic findings remain synthetic. They do not establish real-world or production safety.

### Four control and robotics research labs

The four code labs and their companion manuscripts compile and have successful CI histories. Their current implementations are deliberately limited:

| Research line | What the code currently does | What it does not yet establish |
|---|---|---|
| [Residual RL](https://github.com/Hafiz-IIT/residual-rl-linear-priors) | Scalar linear baseline plus a fixed bounded nonlinear residual | No trained RL policy, statistical prior, robotics result, or learned improvement |
| [Koopman control](https://github.com/Hafiz-IIT/koopman-control-lab) | Scalar monomial lifting and ridge-regularized EDMD-style fit | No invariant-subspace result, controller/MPC evaluation, high-dimensional system, or physical validation |
| [Bayesian safe RL](https://github.com/Hafiz-IIT/bayesian-safe-rl-lab) | Scalar Normal-Normal posterior and interval threshold gate | No complete Bayesian RL algorithm, sequential control study, calibrated safety guarantee, or formal certificate |
| [Hybrid LQR + RL](https://github.com/Hafiz-IIT/hybrid-lqr-rl-control) | Scalar proportional feedback plus fixed cubic residual | No Riccati-solved LQR controller, trained deep-RL residual, robustness proof, or robot experiment |

All four companion paper result manifests remain `not_run`. LaTeX compilation is not evidence that the experiment protocols have been executed.

The manuscript sources also need contribution/title alignment:
- The Koopman paper currently studies prediction, not a control or MPC result.
- The residual paper title refers to statistical priors, while the current implementation is a fixed linear-feedback baseline plus a fixed residual.
- The hybrid paper title refers to LQR and deep RL, while the current implementation is neither a Riccati-solved LQR nor a trained RL policy.
- The Bayesian paper is explicit about its scalar heuristic limitation, but does not yet implement reinforcement learning.

### Other executable prototypes

The following are useful engineering demonstrations, but their current evidence is not sufficient for production or publication claims:

- **Agent Evidence Probes:** confidence aggregation assumes independence between declared groups; conflict detection treats any distinct fresh claim strings as a conflict. The benchmark test set is very small.
- **Memory Governor:** poisoning detection is a phrase screen, not robust prompt-injection detection. TTL and policy input validation and atomic superseding need stronger tests.
- **Safe RL Action Gate:** checks a discrete next state, not continuous/intermediate trajectories; it has no formal safety guarantee and needs finite-value/input validation.
- **Multilingual Reliability Bench:** uses normalized exact-match scoring. The parallel wrapper does not currently carry the `supported` label through to evaluation.
- **EXIM Document Truth Bench:** duplicate document kinds are silently overwritten in the kind-indexed dictionary; validation and duplicate detection need to be explicit.
- **EXIM Copilot Core:** in-memory workflow state and role checks are prototypes, not authenticated multi-user authorization or durable audit.
- **Secure Document RAG:** lexical token overlap is not semantic RAG; caller-supplied sensitivity labels are not a complete access-control boundary.
- **Cargo Scan Consistency Lab:** synthetic comparison/fusion heuristics are not calibrated sensor models or physical scanner validation.
- **Logistics Optimization:** Dijkstra requires non-negative edge weights, but edge inputs are not validated; the public edge-creation method does not expose its blocked flag.
- **Cold Chain Digital Twin:** simplified Euler thermal simulation; parameters and energy proxy are not physically calibrated.
- **Port Operations Simulator:** simple berth scheduling prototype; vessel time inputs need validation and the scheduler is not a full port-operations optimizer.
- **Multi-Agent Logistics:** greedy sequential assignment, not a globally optimized multi-agent allocation method; task and capacity inputs need validation.
- **Traffic Incident Routing:** the time-dependent route function evaluates every road at the departure hour rather than updating incident state at each road's arrival time.
- **College Ops Copilot:** static service rules and field-presence checks; no institutional-system integration or authenticated workflow.
- **Hospital Ops Helpdesk:** administrative routing only. Emergency detection is keyword-based and must never be represented as clinical triage.
- **Predictive Intelligence Platform:** basic moving-average/smoothing methods; comparing windows on the same backtest results can create model-selection bias.
- **Privacy-Aware Recommender:** explicit preference filtering is useful, but this is not differential privacy or a formal privacy guarantee.
- **Underwater Li-Fi Simulator:** simplified exponential attenuation and BER model; the SNR convention and physical assumptions require validation against established channel models.
- **Institutional Evidence Tracker:** verification is a mutable boolean, and the completion flag can override unresolved evidence/dependencies; packet hashing is not a digital signature.
- **HAFS OS Core:** callers can mark evidence verified, and distinct source strings are treated as distinct evidence without authenticated independence.
- **Agency QA Orchestrator:** a criterion can be marked passed without attached test evidence; artifact paths are not checked for existence.

These are logged as limitations and repair targets, not silently treated as completed research contributions.

## Manuscript status

The five new manuscript repositories have successful LaTeX/integrity workflows. The three control-paper introduction formatting errors and the residual-control equation's notation typo were corrected during this audit.

- Four control/robotics result manifests remain `not_run`.
- The EXIM multimodal cargo manuscript remains an architecture/evaluation proposal with no real customs integration, certified scanner, or operational validation.
- EGA contains reported synthetic results, but the missing experiment runners described above block a full reproducibility claim.
- None of these five manuscripts should be described as submitted, peer-reviewed, or published.

## Work completed after the first audit pass

### Koopman scalar prediction pilot

The first new controlled experiment was executed in [koopman-control-lab](https://github.com/Hafiz-IIT/koopman-control-lab).

- Updated the lifting dictionary to include the constant observable.
- Added operator/input validation and tests for affine fitting, lifted rollout, and malformed inputs.
- Added a fixed-seed experiment runner with five synthetic scalar maps, ten seeds, persistence and affine-linear baselines, and degree-two/degree-three EDMD ablations.
- Generated 200 per-seed model evaluations, aggregate means/standard deviations/95% t-intervals, and SHA-256 hashes for the generated CSVs.
- Updated the companion manuscript to report the actual pilot and renamed it to reflect prediction rather than unsupported control claims.
- Latest observed lab CI run passed and archived the full CSV outputs as the `koopman-scalar-benchmark` artifact.

The pilot is explicitly limited to synthetic scalar prediction. It does not establish Koopman invariance or control/MPC utility. Ridge sensitivity, sample-size/coverage sweeps, noise, higher-dimensional systems, and closed-loop evaluation remain outstanding.

The observed negative results are retained: degree-three lifting worsened OOD error on the tanh system relative to the affine baseline and worsened 20-step error on the piecewise regime-shift system despite improving one-step error.

### Manuscript and application corrections

- Updated the Koopman companion paper's protocol, abstract, results, limitations, reproducibility note, and claims ledger to match the executed pilot.
- Corrected the residual, Koopman, and hybrid LaTeX formatting issues identified in the first audit pass.
- Corrected the restaurant and Smart City application issues listed above; their latest observed application CI runs passed.

## Research sequence — decision

Do not add more repositories. The current order is:

1. **EGA reproducibility repair remains the highest publication blocker.** The existing result tables cannot all be regenerated from committed experiment-runner source. Reconstruct the runners, fix the incomplete evidence gate, and rerun the benchmark before any EGA submission decision.
2. **Koopman is the first new dynamics research line and its v0.1 scalar prediction pilot is complete.** Next run ridge sensitivity, sample-size/coverage sweeps, noisy dynamics, and then decide whether to extend to MPC/control or keep the paper scoped to prediction.
3. **Residual control next.** Define and solve a valid nominal controller, then implement a genuinely trainable residual policy. Do not call the current fixed residual an RL agent.
4. **Bayesian uncertainty gating.** Measure calibration, false-allow/false-block trade-offs, prior misspecification, and distribution shift.
5. **Hybrid LQR + RL.** It depends on a valid LQR baseline and trained residual policy, so it should not precede those foundations.
6. **Only after reproducible evidence:** conduct a current literature/novelty review, revise mathematical claims, and decide which manuscript merits arXiv submission.

For every experiment, preserve exact code revision, configuration, seeds, raw per-run outputs, aggregate results, baseline implementations, output hashes, and negative findings. A result is not complete merely because a workflow passes.

## Metadata status

Repository descriptions have been manually entered by the user. Topics remain optional housekeeping and can be added later in each repository's About panel. The connected GitHub tools do not expose a repository topics write operation, so topics still need to be added manually. No local PowerShell or GitHub CLI installation is required.
