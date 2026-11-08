# ==============================================================================
# install.ps1 - Instalador One-Liner para SDD Framework v6.6
# Uso: irm https://raw.githubusercontent.com/svelascotellez/ssd-projects/main/install.ps1 | iex
# ==============================================================================

param(
    [string]$Destination = "$HOME/.sdd"
)

$ErrorActionPreference = 'Stop'
Write-Host "=== [SDD Framework v6.6]: Instalando en $Destination... ===" -ForegroundColor Cyan

if (-not (Test-Path $Destination)) {
    New-Item -ItemType Directory -Path $Destination -Force | Out-Null
}

$BaseUrl = "https://raw.githubusercontent.com/svelascotellez/ssd-projects/main"
$FilesToDownload = @(
    "setup-sdd-project-v66.ps1",
    "setup-sdd-project-v66.py",
    "README.md",
    "LICENSE"
)

foreach ($file in $FilesToDownload) {
    $targetPath = Join-Path $Destination $file
    Write-Host "  [+] Descargando $file..." -ForegroundColor Gray
    Invoke-RestMethod -Uri "$BaseUrl/$file" -OutFile $targetPath
}

Write-Host "`n[OK] SDD Framework v6.6 instalado exitosamente en $Destination." -ForegroundColor Green
Write-Host "Para inicializar un nuevo proyecto, ejecuta:" -ForegroundColor Yellow
Write-Host "  & `"$Destination\setup-sdd-project-v66.ps1`" -ProjectName `"MiProyecto`" -Stack `"python`"`n" -ForegroundColor White

