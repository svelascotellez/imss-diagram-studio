with open('setup-sdd-project-v6.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update ValidateSet
vs_target = '[ValidateSet("status", "list", "create", "set-active", "next", "verify", "approve", "complete", "configure-stack", "preview-design", "verify-security")]'
vs_repl = '[ValidateSet("status", "list", "create", "set-active", "next", "verify", "approve", "complete", "configure-stack", "preview-design", "verify-security", "fix-markdown")]'

if vs_target in text:
    text = text.replace(vs_target, vs_repl, 1)
    print("1. Updated ValidateSet with fix-markdown.")
else:
    print("1. Target not found for ValidateSet.")

# 2. Update Check 6 in spec-gate.ps1 lines array
check6_target = "    'Write-Host \"  [OK] 6. Guia de Usuario: 4 Secciones completas y CERO placeholders residuales.\" -ForegroundColor Green',"

check6_replacement = """    '# 6C. Validacion y Auto-Reparacion Markdownlint MD022 (Lineas en blanco alrededor de encabezados)',
    '$AllMdFiles = @($FoundGuide, $SpecFile, $PlanFile)',
    'if (Test-Path "specs\\$FeatureId\\tasks.md") { $AllMdFiles += "specs\\$FeatureId\\tasks.md" }',
    '$Md022FixedCount = 0',
    'foreach ($mdPath in $AllMdFiles) {',
    '    if (Test-Path $mdPath) {',
    '        $rawLines = [System.IO.File]::ReadAllLines((Resolve-Path $mdPath).Path)',
    '        $fixedLines = [System.Collections.Generic.List[string]]::new()',
    '        $inCodeFence = $false',
    '        $fileChanged = $false',
    '        for ($li = 0; $li -lt $rawLines.Count; $li++) {',
    '            $curLine = $rawLines[$li]',
    '            if ($curLine -match ''^\\s*```'') { $inCodeFence = -not $inCodeFence }',
    '            if (-not $inCodeFence -and $curLine -match ''^\\s{0,3}#{1,6}\\s+'') {',
    '                if ($fixedLines.Count -gt 0 -and $fixedLines[$fixedLines.Count - 1].Trim() -ne '''') {',
    '                    $fixedLines.Add('''')',
    '                    $fileChanged = $true',
    '                    $Md022FixedCount++',
    '                }',
    '                $fixedLines.Add($curLine)',
    '                if ($li + 1 -lt $rawLines.Count -and $rawLines[$li + 1].Trim() -ne '''') {',
    '                    $fixedLines.Add('''')',
    '                    $fileChanged = $true',
    '                    $Md022FixedCount++',
    '                }',
    '            } else {',
    '                $fixedLines.Add($curLine)',
    '            }',
    '        }',
    '        if ($fileChanged) {',
    '            [System.IO.File]::WriteAllLines((Resolve-Path $mdPath).Path, $fixedLines, [System.Text.Encoding]::UTF8)',
    '            Write-Host "  [Auto-Fix MD022]: Se corrigieron encabezados sin linea en blanco en $mdPath." -ForegroundColor Yellow',
    '        }',
    '    }',
    '}',
    'Write-Host "  [OK] 6. Guia y Documentacion: 4 Secciones completas, 0 placeholders y 100% cumplimiento MD022." -ForegroundColor Green',"""

if check6_target in text:
    text = text.replace(check6_target, check6_replacement, 1)
    print("2. Added Check 6C MD022 Auto-Fixer to spec-gate.ps1.")
else:
    print("2. Target not found for Check 6.")

with open('setup-sdd-project-v6.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("setup-sdd-project-v6.py updated.")
