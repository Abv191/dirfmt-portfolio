param(
    [string]$Action = "all"
)

$ErrorActionPreference = "Stop"

function Write-Status($msg) {
    Write-Host "[deploy] $msg" -ForegroundColor Cyan
}

function Deploy-LandingPage {
    Write-Status "Deploying landing page to GitHub Pages..."
    $landingDir = Join-Path $PSScriptRoot ".." | Join-Path -ChildPath "landing"
    $buildDir = Join-Path $PSScriptRoot ".." | Join-Path -ChildPath ".gh-pages"

    if (Test-Path $buildDir) {
        Remove-Item $buildDir -Recurse -Force
    }
    Copy-Item $landingDir $buildDir -Recurse -Force

    Write-Status "Landing page ready at .gh-pages/"
    Write-Status "Push to GitHub Pages via: gh pages deploy .gh-pages"
}

function Build-Tools {
    Write-Status "Building Python CLI packages..."
    pushd (Join-Path $PSScriptRoot ".." | Join-Path -ChildPath "dirfmt")
    python -m build
    popd

    Write-Status "Building Node.js CLI packages..."
    pushd (Join-Path $PSScriptRoot ".." | Join-Path -ChildPath "readmegen")
    npm pack
    popd

    Write-Status "All packages built successfully"
}

function Run-Tests {
    Write-Status "Running Playwright tests..."
    $testDir = Join-Path $PSScriptRoot ".." | Join-Path -ChildPath "tests"
    python -m pytest $testDir -v
    Write-Status "All tests passed"
}

function Publish-PyPI {
    Write-Status "Publishing dirfmt to PyPI..."
    pushd (Join-Path $PSScriptRoot ".." | Join-Path -ChildPath "dirfmt")
    pip install twine
    twine upload dist/*
    popd
}

function Publish-Npm {
    Write-Status "Publishing readmegen to npm..."
    pushd (Join-Path $PSScriptRoot ".." | Join-Path -ChildPath "readmegen")
    npm login
    npm publish
    popd
}

switch ($Action) {
    "landing" { Deploy-LandingPage }
    "build" { Build-Tools }
    "test" { Run-Tests }
    "pypi" { Publish-PyPI }
    "npm" { Publish-Npm }
    default {
        Deploy-LandingPage
        Build-Tools
        Run-Tests
        Write-Status "Deployment complete. Review before publishing to PyPI/npm."
    }
}