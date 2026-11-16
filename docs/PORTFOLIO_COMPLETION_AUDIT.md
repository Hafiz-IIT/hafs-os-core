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

**Potential policy correctness issue**
- In `src/core.py`, the `complete` feature checks only whether the declaration exists. It does not require the invoice and packing list to be present as well.
- The current synthetic missing-evidence family removes the declaration or authorization, but does not systematically test missing invoice and missing packing-list cases.
- A case with a missing packing list may therefore pass the completeness check if the remaining visible documents and other signals agree. Add explicit regression tests and expand the benchmark before relying on this gate.

**Required EGA work**
1. Reconstruct and version the missing experiment runners.
2. Freeze the exact policies, stochastic assumptions, seeds, and cost matrix.
3. Regenerate all result tables from source, not from the checked-in CSVs.
4. Make the benchmark generator and committed manifest schema consistent.
5. Add missing-invoice, missing-packing-list, duplicate-document, and corrupted-provenance cases.
6. Correct the completeness rule and rerun all experiments under a new benchmark/policy version.
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

## Research sequence — decision

Do not begin by adding more repositories. The order should be:

1. **Repair EGA reproducibility first.** It is the most mature existing research candidate, but its current result tables cannot all be regenerated from the committed source.
2. **Start the first new controlled experiment with Koopman lifted dynamics.** It has the clearest bounded prediction task and can be evaluated with persistence and linear-regression baselines, polynomial dictionary ablations, multiple seeds, held-out state ranges, and multi-step error. Decide after results whether to extend it to MPC/control or retitle the manuscript to match a prediction contribution.
3. **Then residual control.** First define a valid nominal controller and implement a genuinely trainable residual policy; do not call the fixed residual an RL agent.
4. **Then Bayesian uncertainty gating.** Measure calibration, false-allow/false-block trade-offs, prior misspecification, and distribution shift.
5. **Then hybrid LQR + RL.** It depends on a valid LQR baseline and trained residual policy, so it should not precede those foundations.
6. **Only after reproducible evidence:** conduct the novelty review, revise mathematical claims, and decide which manuscript merits arXiv submission.

For every experiment, preserve exact code revision, configuration, seeds, raw per-run outputs, aggregate results, baseline implementations, and negative findings. A result is not complete merely because a workflow passes.

## Metadata status

Repository descriptions have been manually entered by the user. Topics remain optional housekeeping and can be added later in each repository's About panel. No local PowerShell or GitHub CLI installation is required for the remaining topic edits.
