$ErrorActionPreference = "Stop"

$owner = "Hafiz-IIT"

$repos = @(
    "residual-rl-linear-priors",
    "residual-rl-linear-priors-paper",
    "koopman-control-lab",
    "koopman-control-paper",
    "bayesian-safe-rl-lab",
    "bayesian-safe-rl-paper",
    "hybrid-lqr-rl-control",
    "hybrid-lqr-rl-paper",
    "exim-multimodal-cargo-framework-paper"
)

foreach ($repo in $repos) {
    Write-Host "Creating $owner/$repo"
    gh repo create "$owner/$repo" --public
}

Write-Host "Repository shells created."
