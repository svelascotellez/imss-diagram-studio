# ==============================================================================
# tools/sdd-status.ps1 - Visual Status Inspector para IDE (VS Code / Antigravity)
# Muestra el estado del candado HMAC-SHA256 y las 9 Hard Gates en la consola del IDE.
# ==============================================================================

param(
    [string]$Path = "."
)

$targetDir = Resolve-Path $Path
$featureListPath = Join-Path $targetDir "feature_list.json"
$harnessConfigPath = Join-Path $targetDir ".specify\harness-config.json"

Clear-Host
Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "   SDD FRAMEWORK v6.6 - RADAR DE GOBERNANZA Y COMPLIANCE         " -ForegroundColor Cyan
Write-Host "=================================================================" -ForegroundColor Cyan

if (-not (Test-Path $featureListPath)) {
    Write-Host "[!] No se detecto un proyecto SDD activo en: $targetDir" -ForegroundColor Yellow
    exit 0
}

$fl = Get-Content $featureListPath -Raw | ConvertFrom-Json
$cfg = if (Test-Path $harnessConfigPath) { Get-Content $harnessConfigPath -Raw | ConvertFrom-Json } else { $null }

Write-Host "Proyecto: " -NoNewline; Write-Host "$($fl.project_name)" -ForegroundColor Green -NoNewline
Write-Host "  | Stack: " -NoNewline; Write-Host "$($cfg.stack)" -ForegroundColor Magenta -NoNewline
Write-Host "  | Version: " -NoNewline; Write-Host "$($fl.version)" -ForegroundColor White

Write-Host "`n--- FUNCIONALIDADES Y ESTADO CRIPTOGRAFICO ---" -ForegroundColor DarkCyan

foreach ($feat in $fl.features) {
    $sealStr = if ($feat.approval_seal) { "[HMAC-SHA256 OK]" } else { "[PENDIENTE HITL]" }
    $sealColor = if ($feat.approval_seal) { "Green" } else { "Yellow" }
    
    $statusColor = switch ($feat.status) {
        "completed"   { "Green" }
        "in_progress" { "Cyan" }
        "pending"     { "Gray" }
        Default       { "White" }
    }

    Write-Host "  $($feat.id.PadRight(10))" -ForegroundColor White -NoNewline
    Write-Host "$($feat.name.PadRight(28))" -ForegroundColor Yellow -NoNewline
    Write-Host "$($feat.status.PadRight(14))" -ForegroundColor $statusColor -NoNewline
    Write-Host "$sealStr" -ForegroundColor $sealColor
}

Write-Host "`n--- RESUMEN DE LAS 9+1 HARD GATES ---" -ForegroundColor DarkCyan
Write-Host "  Gate 0: Candado HMAC-SHA256 e Integridad Inmutable" -ForegroundColor Green
Write-Host "  Gate 1: Contencion de Alcance (Spec Drift)" -ForegroundColor Green
Write-Host "  Gate 2: Escenarios BDD 1:1 en Gherkin" -ForegroundColor Green
Write-Host "  Gate 3: Cobertura Unitaria TDD (Dominio)" -ForegroundColor Green
Write-Host "  Gate 4: Clean Architecture Poliglota" -ForegroundColor Green
Write-Host "  Gate 5: Deteccion Estricta de Fake Tests" -ForegroundColor Green
Write-Host "  Gate 6: Escaneo Defensivo OWASP y Secretos" -ForegroundColor Green
Write-Host "  Gate 7: Analisis Estatico y Linting" -ForegroundColor Green
Write-Host "  Gate 8: Trazabilidad y Bitacora HITL" -ForegroundColor Green
Write-Host "  Gate 9: Resiliencia SLA k6 (P95 < 200ms)" -ForegroundColor Green

Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "Acciones rapidas:" -ForegroundColor DarkGray
Write-Host "  - Auditar:   .\harness\sdd.ps1 -Action gate -FeatureId <FEAT-ID>" -ForegroundColor Gray
Write-Host "  - Cockpit:   .\harness\sdd.ps1 -Action dashboard" -ForegroundColor Gray
Write-Host "  - Exportar:  .\harness\sdd.ps1 -Action export-compliance -FeatureId <FEAT-ID>`n" -ForegroundColor Gray
