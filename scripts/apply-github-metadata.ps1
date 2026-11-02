$ErrorActionPreference = "Stop"

$owner = "Hafiz-IIT"

$repos = @(
    @{
        Name = "agent-evidence-probes"
        Description = "Evaluation probes for evidence sufficiency, independence, conflict and action authorization in autonomous AI agents."
        Topics = @("ai-safety","agentic-ai","evaluation","provenance","python")
    },
    @{
        Name = "memory-governor"
        Description = "Persistent-memory governance for AI agents: provenance, scope, sensitivity, expiry, invalidation and audit."
        Topics = @("ai-agents","memory","ai-safety","security","python")
    },
    @{
        Name = "safe-rl-action-gate"
        Description = "Runtime action shielding plus LQR, residual-control, Koopman-inspired and Bayesian dynamics research baselines."
        Topics = @("reinforcement-learning","control-systems","ai-safety","robotics","python")
    },
    @{
        Name = "multilingual-reliability-bench"
        Description = "Benchmark scaffold for accuracy, abstention and unsupported-answer reliability gaps across languages."
        Topics = @("multilingual-ai","evaluation","nlp","ai-safety","python")
    },
    @{
        Name = "exim-document-truth-bench"
        Description = "Synthetic benchmark for cross-document consistency, missing evidence, stale authorization and EXIM truth validation."
        Topics = @("exim","document-ai","evaluation","trade","python")
    },
    @{
        Name = "exim-copilot-core"
        Description = "Governed EXIM workflow core with document requirements, discrepancies, verification and ACT/ASK/VERIFY/ESCALATE."
        Topics = @("exim","ai-agents","workflow","trade","python")
    },
    @{
        Name = "secure-doc-rag-agent"
        Description = "Traceable document retrieval with provenance-preserving chunks, sensitivity filters and evidence sufficiency gates."
        Topics = @("rag","document-ai","privacy","provenance","python")
    },
    @{
        Name = "cargo-scan-consistency-lab"
        Description = "Synthetic declaration-vs-observation consistency and multimodal evidence-fusion lab for cargo inspection research."
        Topics = @("exim","multimodal-ai","computer-vision","logistics","python")
    },
    @{
        Name = "hafs-os-core"
        Description = "Governance and orchestration core for ~haf.s__ OS: tasks, permissions, evidence, risk, memory and agent authority."
        Topics = @("ai-agents","orchestration","ai-safety","automation","python")
    },
    @{
        Name = "agency-qa-orchestrator"
        Description = "Requirements-to-artifact traceability, acceptance criteria, verification evidence and delivery gating for AI-assisted builds."
        Topics = @("ai-agents","software-quality","automation","verification","python")
    },
    @{
        Name = "logistics-optimization-lab"
        Description = "Multi-objective logistics routing sandbox balancing monetary cost, travel time and operational risk."
        Topics = @("logistics","optimization","routing","algorithms","python")
    },
    @{
        Name = "cold-chain-digital-twin"
        Description = "Cold-chain thermal digital twin for temperature drift, cooling-control and excursion analysis."
        Topics = @("digital-twin","cold-chain","logistics","simulation","python")
    },
    @{
        Name = "port-operations-simulator"
        Description = "Berth-allocation and vessel-queue simulator for port waiting time, scheduling and utilization research."
        Topics = @("ports","logistics","simulation","scheduling","python")
    },
    @{
        Name = "multi-agent-logistics-sim"
        Description = "Capacity-aware multi-agent logistics allocation simulator for coordination and routing research."
        Topics = @("multi-agent-systems","logistics","optimization","simulation","python")
    },
    @{
        Name = "traffic-incident-routing-lab"
        Description = "Incident-aware routing simulator with road closures, delay penalties and dynamic path selection."
        Topics = @("smart-city","routing","traffic","optimization","python")
    },
    @{
        Name = "college-ops-copilot-core"
        Description = "Administrative college copilot core for request validation, office routing, missing evidence and SLA hints."
        Topics = @("education","ai-agents","workflow","automation","python")
    },
    @{
        Name = "hospital-ops-helpdesk"
        Description = "Administrative hospital helpdesk router with explicit emergency escalation and a hard non-clinical boundary."
        Topics = @("healthcare-operations","workflow","helpdesk","automation","python")
    },
    @{
        Name = "predictive-intelligence-platform"
        Description = "Transparent forecasting and anomaly-detection baselines with reproducible statistical evaluation."
        Topics = @("forecasting","anomaly-detection","data-science","time-series","python")
    },
    @{
        Name = "privacy-aware-recommender-lab"
        Description = "Recommendation lab constrained to explicit opt-in preferences and minimum cohort-support safeguards."
        Topics = @("recommender-systems","privacy","responsible-ai","machine-learning","python")
    },
    @{
        Name = "underwater-lifi-simulator"
        Description = "Underwater optical-link simulator for attenuation, received power, SNR and approximate OOK bit-error rate."
        Topics = @("lifi","optical-communication","simulation","wireless","python")
    },
    @{
        Name = "institutional-evidence-tracker"
        Description = "Evidence, dependency, decision-owner and next-action tracker for auditable multi-step institutional workflows."
        Topics = @("workflow","evidence","audit","governance","python")
    }
)

foreach ($repo in $repos) {
    $full = "$owner/$($repo.Name)"
    Write-Host "Updating $full"
    gh repo edit $full --description $repo.Description

    foreach ($topic in $repo.Topics) {
        gh repo edit $full --add-topic $topic
    }
}

Write-Host "Done. Verify with: gh repo list $owner --limit 100"

# Second research-paper and project batch
$additionalRepos = @(
    @{ Name = "Hafiz-IIT"; Description = "Research and engineering portfolio covering reliable AI systems, agent governance, EXIM intelligence, control and logistics simulation."; Topics = @("portfolio","artificial-intelligence","ai-safety","research","python") },
    @{ Name = "residual-rl-linear-priors"; Description = "Scalar residual-control research prototype combining a linear prior, bounded nonlinear correction and deterministic rollouts."; Topics = @("reinforcement-learning","control-systems","robotics","simulation","python") },
    @{ Name = "residual-rl-linear-priors-paper"; Description = "Manuscript and experiment protocol for residual reinforcement learning with linear statistical priors; research in preparation."; Topics = @("research-paper","reinforcement-learning","robotics","control-theory") },
    @{ Name = "koopman-control-lab"; Description = "EDMD-style scalar lifted-dynamics laboratory with polynomial dictionaries, ridge fitting and multi-step prediction."; Topics = @("koopman-operator","control-theory","dynamical-systems","simulation","python") },
    @{ Name = "koopman-control-paper"; Description = "Manuscript and evaluation protocol for Koopman-based linear embeddings for automated-agent control; research in preparation."; Topics = @("research-paper","koopman-operator","control-theory","robotics") },
    @{ Name = "bayesian-safe-rl-lab"; Description = "Scalar Bayesian uncertainty update and conservative ALLOW/VERIFY/BLOCK action-gating prototype."; Topics = @("bayesian-methods","safe-reinforcement-learning","ai-safety","uncertainty","python") },
    @{ Name = "bayesian-safe-rl-paper"; Description = "Manuscript and evaluation protocol for Bayesian uncertainty models as priors for safe reinforcement learning."; Topics = @("research-paper","bayesian-methods","safe-reinforcement-learning","robotics") },
    @{ Name = "hybrid-lqr-rl-control"; Description = "Synthetic scalar hybrid-control simulator combining linear feedback with a bounded nonlinear residual."; Topics = @("lqr","control-systems","reinforcement-learning","robotics","simulation") },
    @{ Name = "hybrid-lqr-rl-paper"; Description = "Manuscript and experiment protocol for hybrid LQR and learned-residual control architectures; research in preparation."; Topics = @("research-paper","lqr","robotics","control-theory") },
    @{ Name = "exim-multimodal-cargo-framework-paper"; Description = "Architecture manuscript for evidence-preserving EXIM document intelligence and multimodal cargo discrepancy review."; Topics = @("exim","customs","document-ai","multimodal-ai","research-paper") }
)

foreach ($repo in $additionalRepos) {
    $full = "$owner/$($repo.Name)"
    Write-Host "Updating $full"
    gh repo edit $full --description $repo.Description
    foreach ($topic in $repo.Topics) {
        gh repo edit $full --add-topic $topic
    }
}

# Earlier software projects and flagship repository topics
$legacyRepos = @(
    @{ Name = "EXIM-AI-Evidence-Gated-Autonomy"; Description = "Reproducible research testbed for evidence-gated autonomy, verification, provenance, and escalation in high-consequence AI workflows."; Topics = @("ai-safety","agentic-ai","verification","provenance","exim") },
    @{ Name = "Smart-City-Management-Management"; Description = "Software prototype for urban incident records, sensor-style data, API workflows, and map-oriented operational monitoring."; Topics = @("smart-city","urban-operations","python","software-prototype") },
    @{ Name = "resturant-order-management"; Description = "Full-stack restaurant operations project with a Node.js and Express API, MongoDB persistence, menu and order workflows, and JWT-based admin authentication."; Topics = @("nodejs","express","mongodb","rest-api","software-project") }
)
foreach ($repo in $legacyRepos) {
    $full = "$owner/$($repo.Name)"
    Write-Host "Updating $full"
    gh repo edit $full --description $repo.Description
    foreach ($topic in $repo.Topics) {
        gh repo edit $full --add-topic $topic
    }
}
