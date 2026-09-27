# arXiv / Preprint Roadmap

This roadmap converts the recovered historical paper list into a defensible publishing sequence. It deliberately prioritizes repositories with inspectable experiments over concept-only manuscripts.

## Stage 0 — repository evidence

Before a paper:

1. freeze the research question;
2. tag a reproducible software release;
3. generate experiment artifacts from code;
4. keep raw outputs / seeds / configurations;
5. document negative results;
6. write limitations before writing the conclusion.

## Stage 1 — strongest near-term empirical manuscripts

### A. Evidence-Gated Autonomy / agent evidence

Candidate focus:
- confidence-only vs evidence-gated action authorization;
- source independence;
- correlated verification;
- provenance/trust-root compromise;
- human escalation.

Primary repositories:
- `EXIM-AI-Evidence-Gated-Autonomy`
- `agent-evidence-probes`

### B. EXIM document truth

Candidate focus:
- extraction correctness vs evidence consistency;
- missing/stale/conflicting trade documents;
- correlated-document provenance;
- consequences for automated downstream action.

Primary repositories:
- `exim-document-truth-bench`
- `exim-copilot-core`

### C. Persistent agent memory governance

Candidate focus:
- TTL and stale-memory reuse;
- selective forgetting/supersession;
- scope/sensitivity controls;
- memory poisoning and auditability.

Primary repository:
- `memory-governor`

### D. Runtime action gating / safe RL baseline

Candidate focus:
- intervention policy;
- constraint violations prevented;
- model mismatch;
- future comparison with CBF / LQR / residual RL.

Primary repository:
- `safe-rl-action-gate`

### E. Multilingual reliability

Candidate focus:
- matched English/Bengali/Hindi task sets;
- accuracy vs abstention;
- unsupported-answer rate;
- preprocessing-induced evaluation artifacts.

Primary repository:
- `multilingual-reliability-bench`

## Stage 2 — simulation papers after stronger experiment suites

- logistics multi-objective routing;
- berth/port operations simulation;
- multi-agent logistics coordination;
- cold-chain digital twin;
- underwater Li-Fi channel simulation;
- privacy-aware recommendation constraints.

## Stage 3 — backlog requiring substantial new implementation

- Koopman-based control;
- LQR + deep RL;
- Bayesian linear priors for safe RL;
- uncertainty-aware RL;
- formal control barrier functions;
- 6G/solar-fiber concepts;
- real cargo scanner fusion;
- hardware Li-Fi experiments.

## Historical EXIM publication sequence recovered from older planning

1. Short public whitepaper / technical report.
2. Expand into a 4–6 page preprint with methods and reproducible experiments.
3. Link code and paper.
4. Submit to arXiv when manuscript quality and category/endorsement requirements are satisfied.
5. Maintain DOI/preprint/profile links consistently after publication.

Historical title:
**EXIM AI Co-Pilot: A Multimodal Cargo Scanning & Customs Automation Framework (Concept & Prototype)**

Historical review-paper direction:
**AI in Customs & Logistics: State of the Art**

## Important

Zenodo, arXiv, Google Scholar, ResearchGate, conference submission, and DOI records are **publication actions**, not README decorations. They should be added to repository citation metadata only after the record actually exists.
