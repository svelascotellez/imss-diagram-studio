# tests\v66-governance.Tests.ps1 - Suite de Pruebas de Gobernanza SDD v6.6
# Valida la implementacion de las recomendaciones P0, P1 y P2 de 'Analisis Sdd V65'

Describe "SDD v6.6 Suite de Gobernanza y Compliance Hardened" {
    BeforeAll {
        $global:TestSandbox = Join-Path ([System.IO.Path]::GetTempPath()) "sdd-v66-pester-$([Guid]::NewGuid().ToString('N'))"
        New-Item -ItemType Directory -Path $global:TestSandbox -Force | Out-Null
        
        $ScriptDir = Split-Path -Parent $PSScriptRoot
        $SetupScript = Join-Path $ScriptDir "setup-sdd-project-v66.ps1"
        
        # Scaffolding de proyecto de prueba
        & $SetupScript -ProjectName "test-gov" -Stack "python" -DestinationPath $global:TestSandbox -NoAutoLaunch | Out-Null
        $global:ProjectDir = Join-Path $global:TestSandbox "test-gov"
    }

    AfterAll {
        if ($global:TestSandbox -and (Test-Path $global:TestSandbox)) {
            Remove-Item -Recurse -Force $global:TestSandbox -ErrorAction SilentlyContinue
        }
    }

    BeforeEach {
        Set-Location $global:ProjectDir
    }

    Context "Candado HMAC-SHA256, Gestion de Llaves e Identidad (P0.1, P0.2, P1.1)" {
        It "Crea una funcionalidad e incluye @AC-1.4 para paridad BDD 1:1 (P0.3)" {
            & ".\harness\sdd.ps1" -Action create -FeatureId "FEAT-100" -FeatureName "Auth Test" | Out-Null
            Test-Path "specs\FEAT-100\spec.md" | Should -BeTrue
            Test-Path "specs\FEAT-100\scenarios.feature" | Should -BeTrue
            Test-Path "specs\FEAT-100\plan.md" | Should -BeTrue
            
            $featContent = Get-Content "specs\FEAT-100\scenarios.feature" -Raw
            $featContent | Should -Match "@AC-1.4"
        }

        It "Sella la funcionalidad con HMAC-SHA256 y registra la identidad del aprobador (P0.1, P1.1)" {
            & ".\harness\sdd.ps1" -Action approve -FeatureId "FEAT-100" -Force | Out-Null
            
            Test-Path ".specify\.sdd_key" | Should -BeTrue
            $keyBytes = [System.IO.File]::ReadAllBytes((Convert-Path ".specify\.sdd_key"))
            $keyBytes.Length | Should -BeGreaterOrEqual 32
            
            $feats = Get-Content "feature_list.json" -Raw | ConvertFrom-Json
            $f = $feats | Where-Object { $_.id -eq "FEAT-100" }
            $f.status | Should -Be "in_progress"
            $f.algorithm | Should -Be "HMAC-SHA256"
            $f.approval_hash | Should -Not -BeNullOrEmpty
            $f.approved_by | Should -Not -BeNullOrEmpty
            $f.approved_at | Should -Not -BeNullOrEmpty
        }

        It "Detecta alteracion en plan.md (Spec Tampering) y bloquea Gate 0 (P0.2)" {
            Add-Content -Path "specs\FEAT-100\plan.md" -Value "`n<!-- Inyeccion no autorizada -->"
            
            $gateOutput = powershell -NoProfile -ExecutionPolicy Bypass -Command "Set-Location '$global:ProjectDir'; & .\harness\spec-gate.ps1 -FeatureId FEAT-100"
            $LASTEXITCODE | Should -Be 1
            ($gateOutput -join "`n") | Should -Match "Candado criptografico invalido"
            
            # Restaurar plan.md
            $cleanLines = (Get-Content "specs\FEAT-100\plan.md") | Where-Object { $_ -notmatch "Inyeccion no autorizada" }
            $cleanLines | Set-Content "specs\FEAT-100\plan.md" -Encoding UTF8
        }
    }

    Context "Gate 1 - Cero falsos positivos de Spec Drift (P0.4)" {
        It "No reporta k6_benchmark.js como archivo no autorizado en Gate 1" {
            $gateOutput = powershell -NoProfile -ExecutionPolicy Bypass -Command "Set-Location '$global:ProjectDir'; & .\harness\spec-gate.ps1 -FeatureId FEAT-100"
            ($gateOutput -join "`n") | Should -Not -Match "tests\\performance\\k6_benchmark\.js"
            ($gateOutput -join "`n") | Should -Match "1\. Allowed Files: Sin Spec Drift"
        }
    }

    Context "Gate 9 y verify-performance.ps1 (P1.3)" {
        It "Reporta estado SKIPPED_LOCAL y advertencia clara cuando k6 no esta en PATH local" {
            $perfOutput = & ".\harness\verify-performance.ps1" -FeatureId "FEAT-100" 2>&1
            Test-Path "progress\performance_report.json" | Should -BeTrue
            
            $json = Get-Content "progress\performance_report.json" -Raw | ConvertFrom-Json
            $hasK6 = $null -ne (Get-Command k6 -ErrorAction SilentlyContinue)
            if (-not $hasK6) {
                $json.status | Should -Be "SKIPPED_LOCAL"
                $json.sla_certified | Should -BeFalse
            } else {
                $json.status | Should -Be "PASSED"
                $json.sla_certified | Should -BeTrue
            }
        }
    }

    Context "Soporte para Stack Java Maven/Gradle (P1.2)" {
        It "Configura exitosamente el stack java-maven" {
            & ".\harness\sdd.ps1" -Action configure-stack -Stack "java-maven" | Out-Null
            $cfg = Get-Content ".specify\harness-config.json" -Raw | ConvertFrom-Json
            $cfg.stack | Should -Be "java"
            $cfg.dependency_manifest | Should -Be "pom.xml"
            $cfg.test_cmd | Should -Be "mvn test"
            $cfg.typecheck_cmd | Should -Be "mvn compile -q"
            $cfg.source_dir | Should -Be "src/main/java"
            $cfg.test_dir | Should -Be "src/test/java"
        }
    }

    Context "Matriz Poliglota de Stacks Empresariales (Node, DotNet, Go, Rust)" {
        It "Configura correctamente el stack node/typescript" {
            & ".\harness\sdd.ps1" -Action configure-stack -Stack "node" | Out-Null
            $cfg = Get-Content ".specify\harness-config.json" -Raw | ConvertFrom-Json
            $cfg.stack | Should -Be "typescript"
            $cfg.dependency_manifest | Should -Be "package.json"
            $cfg.test_cmd | Should -Be "npx vitest run"
        }

        It "Configura correctamente el stack dotnet/csharp" {
            & ".\harness\sdd.ps1" -Action configure-stack -Stack "dotnet" | Out-Null
            $cfg = Get-Content ".specify\harness-config.json" -Raw | ConvertFrom-Json
            $cfg.stack | Should -Be "dotnet"
            $cfg.dependency_manifest | Should -Be "*.csproj"
            $cfg.test_cmd | Should -Be "dotnet test"
        }

        It "Configura correctamente el stack go" {
            & ".\harness\sdd.ps1" -Action configure-stack -Stack "go" | Out-Null
            $cfg = Get-Content ".specify\harness-config.json" -Raw | ConvertFrom-Json
            $cfg.stack | Should -Be "go"
            $cfg.dependency_manifest | Should -Be "go.mod"
            $cfg.test_cmd | Should -Be "go test ./..."
        }

        It "Configura correctamente el stack rust" {
            & ".\harness\sdd.ps1" -Action configure-stack -Stack "rust" | Out-Null
            $cfg = Get-Content ".specify\harness-config.json" -Raw | ConvertFrom-Json
            $cfg.stack | Should -Be "rust"
            $cfg.dependency_manifest | Should -Be "Cargo.toml"
            $cfg.test_cmd | Should -Be "cargo test"
        }

        It "Restaura el stack de prueba a python para subsecuentes pruebas" {
            & ".\harness\sdd.ps1" -Action configure-stack -Stack "python" | Out-Null
            $cfg = Get-Content ".specify\harness-config.json" -Raw | ConvertFrom-Json
            $cfg.stack | Should -Be "python"
        }
    }

    Context "Higiene Estricta Markdown - 9 Reglas (MD003, MD009, MD022, MD029, MD031, MD032, MD040, MD047, MD058)" {
        It "Sanea automaticamente violaciones de las 9 reglas con sdd.ps1 -Action fix-markdown" {
            $dirtyMd = @(
                'Introductory line',
                'Titulo Setext H1',
                '====',
                'Subtitulo Setext H2',
                '----',
                '### Heading sin espacio abajo ',
                '- Item de lista sin blanco arriba',
                '1. Primer item',
                '3. Item desfasado MD029',
                '```',
                'code sin lenguaje MD040 y sin blancos MD031',
                '```',
                '| Col1 | Col2 |',
                '| --- | --- |',
                '| A | B |',
                'Texto pegado a tabla MD058',
                '',
                ''
            ) -join "`r`n"
            [System.IO.File]::WriteAllText((Join-Path $global:ProjectDir "docs\dirty_test.md"), $dirtyMd, [System.Text.Encoding]::UTF8)

            & ".\harness\sdd.ps1" -Action fix-markdown | Out-Null

            $fixedContent = Get-Content "docs\dirty_test.md" -Raw
            $fixedContent | Should -Match '(?m)^# Titulo Setext H1\r?$'
            $fixedContent | Should -Match '(?m)^## Subtitulo Setext H2\r?$'
            $fixedContent | Should -Match '(?m)^```text\r?$'
            $fixedContent | Should -Match '(?m)^2\. Item desfasado MD029\r?$'
            $fixedContent | Should -Not -Match ' \r?$'
        }
    }

    Context "Cockpit Web Dashboard & DAG Interactivo (harness\dashboard.ps1)" {
        It "Genera sdd_dashboard.html con sintaxis JavaScript 100% valida y auto-fit del DAG" {
            & ".\harness\dashboard.ps1" -NoBrowser | Out-Null
            Test-Path "progress\sdd_dashboard.html" | Should -BeTrue

            $html = Get-Content "progress\sdd_dashboard.html" -Raw -Encoding UTF8
            $html | Should -Match "function fitToScreen\(\)"
            $html | Should -Match "function switchTab\(tabId, btnEl\)"
            $html | Should -Not -Match "translate\(px, px\)"

            $match = [regex]::Match($html, '(?s)<script>\s*(mermaid\.initialize.*?)</script>')
            $match.Success | Should -BeTrue
            $tempJs = Join-Path $global:TestSandbox "dashboard_syntax_check.js"
            [System.IO.File]::WriteAllText($tempJs, $match.Groups[1].Value, [System.Text.Encoding]::UTF8)
            & node --check $tempJs
            $LASTEXITCODE | Should -Be 0
        }
    }
}
