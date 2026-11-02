import re

with open('setup-sdd-project-v6.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update constitution.md in setup-sdd-project-v6.py
law_10_target = "'10. **Secure Coding by Design & Cero Vulnerabilidades OWASP:** Toda funcionalidad que procese entradas externas, datos de usuario, autenticacion, tokens o acceso a infraestructura debe modelar amenazas (STRIDE) en la seccion 5 de plan.md. Queda terminantemente prohibido el uso de f-strings en SQL, shell=True, eval/exec o secretos hardcodeados. El Auditor Octuple valida que no existan credenciales ni patrones vulnerables OWASP antes del cierre formal.'"

law_10_replacement = """'10. **Secure Coding by Design & Cero Vulnerabilidades OWASP:** Toda funcionalidad que procese entradas externas, datos de usuario, autenticacion, tokens o acceso a infraestructura debe modelar amenazas (STRIDE) en la seccion 5 de plan.md. Queda terminantemente prohibido el uso de f-strings en SQL, shell=True, eval/exec o secretos hardcodeados. El Auditor Octuple valida que no existan credenciales ni patrones vulnerables OWASP antes del cierre formal.',
    '',
    '11. **Higiene Estricta de Markdown (Regla MD022 / blanks-around-headings):** Todo documento Markdown generado en el proyecto (specs, planes, tareas, guias de usuario, matrices de trazabilidad, changelog) debe cumplir rigurosamente la regla MD022: cada encabezado (#, ##, ###) DEBE estar obligatoriamente precedido y seguido por exactamente una linea en blanco. Prohibido colocar texto, listas, tablas o bloques de codigo contiguos a un encabezado sin salto de linea vacio intermedio.'"""

if law_10_target in text:
    text = text.replace(law_10_target, law_10_replacement, 1)
    print("1. Added Law 11 to constitution.md template.")
else:
    print("Warning: law_10_target not found.")

# 2. Add Check 6C in spec-gate.ps1
check_6_target = """    Write-Host "  [OK] 6. Guia de Usuario: 4 Secciones completas y CERO placeholders residuales." -ForegroundColor Green"""

check_6_replacement = """    # 6C. Validacion y Auto-Reparacion Markdownlint MD022 (Lineas en Blanco Alrededor de Encabezados)
    $AllMdFiles = @($FoundGuide, $SpecFile, $PlanFile)
    if (Test-Path "specs\\$FeatureId\\tasks.md") { $AllMdFiles += "specs\\$FeatureId\\tasks.md" }
    $Md022FixedCount = 0
    foreach ($mdPath in $AllMdFiles) {
        if (Test-Path $mdPath) {
            $rawLines = [System.IO.File]::ReadAllLines((Resolve-Path $mdPath).Path)
            $fixedLines = [System.Collections.Generic.List[string]]::new()
            $inCodeFence = $false
            $fileChanged = $false
            for ($li = 0; $li -lt $rawLines.Count; $li++) {
                $curLine = $rawLines[$li]
                if ($curLine -match '^\\s*```') { $inCodeFence = -not $inCodeFence }
                if (-not $inCodeFence -and $curLine -match '^\\s{0,3}#{1,6}\\s+') {
                    if ($fixedLines.Count -gt 0 -and $fixedLines[$fixedLines.Count - 1].Trim() -ne '') {
                        $fixedLines.Add('')
                        $fileChanged = $true
                        $Md022FixedCount++
                    }
                    $fixedLines.Add($curLine)
                    if ($li + 1 -lt $rawLines.Count -and $rawLines[$li + 1].Trim() -ne '') {
                        $fixedLines.Add('')
                        $fileChanged = $true
                        $Md022FixedCount++
                    }
                } else {
                    $fixedLines.Add($curLine)
                }
            }
            if ($fileChanged) {
                [System.IO.File]::WriteAllLines((Resolve-Path $mdPath).Path, $fixedLines, [System.Text.Encoding]::UTF8)
                Write-Host "  [Auto-Fix MD022]: Se corrigieron encabezados sin linea en blanco en $mdPath." -ForegroundColor Yellow
            }
        }
    }
    Write-Host "  [OK] 6. Guia y Documentacion: 4 Secciones, 0 placeholders y 100% cumplimiento MD022." -ForegroundColor Green"""

if check_6_target in text:
    text = text.replace(check_6_target, check_6_replacement, 1)
    print("2. Added Check 6C MD022 Auto-Fixer to spec-gate.ps1.")
else:
    print("Warning: check_6_target not found.")

# 3. Add fix-markdown action to sdd.ps1 in setup script
action_target = """    [ValidateSet("status", "next", "approve", "complete", "list", "preview-design", "verify-security")]"""
action_replacement = """    [ValidateSet("status", "next", "approve", "complete", "list", "preview-design", "verify-security", "fix-markdown")]"""

if action_target in text:
    text = text.replace(action_target, action_replacement)
    print("3. Added fix-markdown to ValidateSet in sdd.ps1.")
else:
    print("Warning: action_target not found.")

# 4. Add switch case for fix-markdown in sdd.ps1
switch_target = """    "verify-security" {"""
switch_addition = """    "fix-markdown" {
        Write-Host "=== [SDD Fix-Markdown]: Escaneando y corrigiendo violaciones MD022 en documentos... ===" -ForegroundColor Cyan
        $mdFiles = Get-ChildItem -Path "." -Filter "*.md" -Recurse -File | Where-Object { $_.FullName -notmatch "\\\\(\\.git|node_modules|venv|\\.venv)\\\\" }
        $totalFixed = 0
        foreach ($file in $mdFiles) {
            $rawLines = [System.IO.File]::ReadAllLines($file.FullName)
            $fixedLines = [System.Collections.Generic.List[string]]::new()
            $inCodeFence = $false
            $fileChanged = $false
            for ($li = 0; $li -lt $rawLines.Count; $li++) {
                $curLine = $rawLines[$li]
                if ($curLine -match '^\\s*```') { $inCodeFence = -not $inCodeFence }
                if (-not $inCodeFence -and $curLine -match '^\\s{0,3}#{1,6}\\s+') {
                    if ($fixedLines.Count -gt 0 -and $fixedLines[$fixedLines.Count - 1].Trim() -ne '') {
                        $fixedLines.Add('')
                        $fileChanged = $true
                        $totalFixed++
                    }
                    $fixedLines.Add($curLine)
                    if ($li + 1 -lt $rawLines.Count -and $rawLines[$li + 1].Trim() -ne '') {
                        $fixedLines.Add('')
                        $fileChanged = $true
                        $totalFixed++
                    }
                } else {
                    $fixedLines.Add($curLine)
                }
            }
            if ($fileChanged) {
                [System.IO.File]::WriteAllLines($file.FullName, $fixedLines, [System.Text.Encoding]::UTF8)
                Write-Host "  [MD022 Fixed]: $($file.FullName -replace [regex]::Escape($PWD.Path + '\\'), '')" -ForegroundColor Yellow
            }
        }
        if ($totalFixed -gt 0) {
            Write-Host "[OK]: Se corrigieron exitosamente $totalFixed encabezados en el proyecto." -ForegroundColor Green
        } else {
            Write-Host "[OK]: Todos los documentos Markdown cumplen al 100% la regla MD022 (0 violaciones)." -ForegroundColor Green
        }
    }
    "verify-security" {"""

if switch_target in text:
    text = text.replace(switch_target, switch_addition, 1)
    print("4. Added switch block for fix-markdown in sdd.ps1.")
else:
    print("Warning: switch_target not found.")

# Save updated setup-sdd-project-v6.py
with open('setup-sdd-project-v6.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("setup-sdd-project-v6.py patched successfully!")
