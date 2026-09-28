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
