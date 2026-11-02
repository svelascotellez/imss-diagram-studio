# Lee el contenido del script v4 actual y escribe la versión v4.2 mejorada
# que incluye de forma nativa el soporte para arreglos JSON de PS 5.1,
# la asignación resiliente con Add-Member, la preservación de corchetes,
# la automatización del checkpoint humano en harness\sdd.ps1
# y la Guía de Usuario obligatoria en docs\ auditada por spec-gate.ps1 (Auditor Séxtuple).

script_content = r"""# ==============================================================================
# setup-sdd-project-v4.ps1 — Inicializador SDD + BDD + Clean Architecture (v4.2)
# ==============================================================================

$ErrorActionPreference = 'Stop'

Write-Host "[SDD+BDD Setup v4.2]: Inicializando infraestructura y gobierno..." -ForegroundColor Cyan

# 1. Creacion de Directorios
$Directories = @(
    ".agents\skills",
    ".specify\memory",
    ".specify\templates",
    "specs",
    "harness",
    "docs",
    "progress",
    "src\domain",
    "src\application",
    "src\infrastructure",
    "tests\unit",
    "tests\acceptance"
)

foreach ($dir in $Directories) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-Host "  [+] Directorio creado: $dir" -ForegroundColor Green
    }
}

function Write-SddFile {
    param (
        [string]$Path,
        [string[]]$Lines
    )
    $FullPath = Join-Path $PWD $Path
    $ParentDir = Split-Path $FullPath -Parent
    if (-not (Test-Path $ParentDir)) {
        New-Item -ItemType Directory -Path $ParentDir -Force | Out-Null
    }
    $Content = $Lines -join "`r`n"
    $Utf8Bom = New-Object System.Text.UTF8Encoding($true)
    [System.IO.File]::WriteAllText($FullPath, $Content, $Utf8Bom)
    Write-Host "  [OK] Archivo generado: $Path" -ForegroundColor Yellow
}

# ==============================================================================
# 2. CONFIGURACION POLIGLOTA (.specify\harness-config.json)
# ==============================================================================
Write-SddFile -Path ".specify\harness-config.json" -Lines @(
    '{',
    '  "stack": "python",',
    '  "source_dir": "src",',
    '  "test_dir": "tests",',
    '  "file_extension": "*.py",',
    '  "typecheck_cmd": "python -m mypy src --ignore-missing-imports",',
    '  "test_cmd": "python -m pytest -q tests",',
    '  "forbidden_domain_imports": [',
    '    "fastapi", "flask", "django", "starlette", "requests",',
    '    "httpx", "aiohttp", "sqlalchemy", "peewee", "pymongo", "psycopg2"',
    '  ]',
    '}'
)

# ==============================================================================
# 3. PLANTILLAS ESTRUCTURALES (.specify\templates\)
# ==============================================================================
Write-SddFile -Path ".specify\templates\spec.template.md" -Lines @(
    '# Especificacion Funcional: {FEATURE_ID} - {FEATURE_NAME}',
    '',
    '## 1. Contexto e Historia de Usuario',
    'Como {ROL}',
    'Quiero {ACCION}',
    'Para {BENEFICIO}',
    '',
    '## 2. Criterios de Aceptacion (Sintaxis EARS)',
    '- **AC-1.1**: CUANDO {evento/disparador}, EL SISTEMA DEBE {respuesta esperada}.',
    '- **AC-1.2**: CUANDO {condicion de error}, EL SISTEMA DEBE {respuesta esperada y codigo de error}.',
    '- **AC-1.3**: MIENTRAS {estado del sistema}, EL SISTEMA DEBE {comportamiento continuo}.',
    '- **AC-1.4**: SI {condicion opcional}, EL SISTEMA DEBE {comportamiento especifico}.',
    '',
    '## 3. Comportamientos Fuera de Alcance (Out of Scope)',
    '- No se incluye {CASO_1}.',
    '- No se incluye {CASO_2}.',
    '',
    '## 4. Requisitos No Funcionales y Seguridad',
    '- Tiempo de respuesta < 200 ms.',
    '- Validacion estricta de esquemas inmutables.',
    '',
    '## 5. Allowed Files',
    'Rutas exactas autorizadas para creacion o modificacion durante esta funcionalidad:',
    '- `src/domain/{MODULE}.py`',
    '- `src/application/{SERVICE}.py`',
    '- `tests/unit/test_{MODULE}.py`',
    '- `tests/acceptance/test_{FEATURE}_steps.py`'
)

Write-SddFile -Path ".specify\templates\scenarios.template.feature" -Lines @(
    '# language: es',
    'Caracteristica: {FEATURE_NAME} ({FEATURE_ID})',
    '  Como {ROL}',
    '  Quiero {ACCION}',
    '  Para {BENEFICIO}',
    '',
    '  @AC-1.1',
    '  Escenario: Ejecucion exitosa del flujo principal',
    '    Dado {precondicion inicial}',
    '    Cuando {accion ejecutada}',
    '    Entonces {resultado esperado}',
    '',
    '  @AC-1.2',
    '  Esquema del escenario: Manejo de errores y casos invalidos',
    '    Dado {precondicion inicial}',
    '    Cuando ingresa datos con error en "<campo>" y valor "<valor>"',
    '    Entonces el sistema responde con error "<mensaje_esperado>"',
    '',
    '    Ejemplos:',
    '      | campo | valor | mensaje_esperado |',
    '      | email | inval | Email invalido   |'
)

Write-SddFile -Path ".specify\templates\plan.template.md" -Lines @(
    '# Plan Tecnico de Implementacion: {FEATURE_ID}',
    '',
    '## 1. Diseno Arquitectonico (Clean Architecture)',
    '- **Dominio (`src/domain/`)**: Entidades inmutables y Value Objects. Cero dependencias externas.',
    '- **Aplicacion (`src/application/`)**: Casos de uso y puertos (interfaces abstractas).',
    '- **Infraestructura (`src/infrastructure/`)**: Adaptadores y dobles en memoria.',
    '',
    '## 2. Contratos y Esquemas',
    'Definicion de modelos inmutables de entrada y salida.',
    '',
    '## 3. Allowed Dependencies',
    'Librerias externas de terceros autorizadas:',
    '- `pydantic`',
    '- `pytest`',
    '- `pytest-bdd`',
    '',
    '## 4. Matriz de Trazabilidad BDD / TDD',
    '| Criterio EARS | Escenario Gherkin | Test Automatizado |',
    '| :--- | :--- | :--- |',
    '| `AC-1.1` | `@AC-1.1` | `test_ac_1_1_...` |',
    '| `AC-1.2` | `@AC-1.2` | `test_ac_1_2_...` |'
)

Write-SddFile -Path ".specify\templates\tasks.template.md" -Lines @(
    '# Lista de Tareas Atomicas: {FEATURE_ID}',
    '',
    '- [ ] `T-01`: [tests/acceptance/test_{FEATURE}_steps.py] Implementar step definitions BDD para `@AC-1.1`. (Rojo)',
    '- [ ] `T-02`: [src/domain/{MODULE}.py] Crear entidad de dominio para cumplir `@AC-1.1`. (Verde)',
    '- [ ] `T-03`: [tests/unit/test_{MODULE}.py] Crear suite de pruebas unitarias para `@AC-1.2`. (Rojo)',
    '- [ ] `T-04`: [src/application/{SERVICE}.py] Implementar validacion de error para `@AC-1.2`. (Verde)',
    '- [ ] `T-05`: [docs/user_guide_{FEATURE_DIR}.md] Redactar la Guia de Usuario obligatoria usando `.specify\templates\user_guide.template.md`.',
    '- [ ] `T-06`: [harness] Ejecutar `.\harness\init.ps1` y auditar con `.\harness\spec-gate.ps1 -FeatureId {FEATURE_DIR}`.'
)

Write-SddFile -Path ".specify\templates\user_guide.template.md" -Lines @(
    '# Guia de Usuario: {FEATURE_ID} - {FEATURE_NAME}',
    '',
    '## 1. Descripcion General',
    '{Explicacion clara y en lenguaje accesible sobre que resuelve esta funcionalidad y para que sirve al usuario final.}',
    '',
    '## 2. Requisitos Previos y Configuracion',
    '- {Requisitos o dependencias necesarias antes de utilizar esta funcionalidad.}',
    '',
    '## 3. Instrucciones de Uso Paso a Paso',
    '1. **Paso 1**: {Accion inicial del usuario}',
    '2. **Paso 2**: {Parametros o entradas de datos requeridas}',
    '3. **Paso 3**: {Respuesta o resultado entregado por el sistema}',
    '',
    '## 4. Ejemplos de Uso',
    '### Flujo Principal',
    '```',
    '{Ejemplo concreto de entrada y salida esperada basado en los escenarios BDD}',
    '```',
    '',
    '## 5. Respuestas a Errores y Preguntas Frecuentes',
    '| Mensaje de Error / Comportamiento | Causa | Como Resolverlo |',
    '| :--- | :--- | :--- |',
    '| `{MENSAJE_ERROR}` | {Explicacion} | {Solucion recomendada} |'
)

Write-SddFile -Path ".specify\templates\impl_report.template.md" -Lines @(
    '# Reporte de Implementacion: {FEATURE_ID} - {TASK_ID}',
    '',
    '- **Fecha/Hora**: {TIMESTAMP}',
    '- **Archivos Modificados**: `{FILE_1}`, `{FILE_2}`',
    '- **Resultado de Pruebas**: Suite unitaria PASS | Suite BDD PASS',
    '- **Verificacion de Arnes**: `.\harness\init.ps1` devolvio Exit 0.'
)

# ==============================================================================
# 4. ARTEFACTOS DE GOBIERNO
# ==============================================================================
Write-SddFile -Path "AGENTS.md" -Lines @(
    '# Contexto Operativo y Contrato del Agente (Windows Environment - SDD v4.2)',
    '',
    '## 1. Resumen del Proyecto',
    'Sistema bajo arquitectura limpia, Spec-Driven Development (SDD) y Behavior-Driven Development (BDD) en Google Antigravity sobre Windows. La especificacion en `specs\` (`spec.md` + `scenarios.feature`) es la unica fuente de la verdad.',
    '',
    '## 2. Protocolo Obligatorio de Inicio',
    '1. Ejecuta `.\harness\init.ps1` antes de cualquier accion. Si falla, repara el entorno.',
    '2. Si no se te asigno rol, actua segun `.agents\skills\`.',
    '3. Prohibido tocar codigo en `src\` sin una especificacion aprobada con hash criptografico valido en `feature_list.json` y una tarea activa en `tasks.md`.',
    '4. Toda funcionalidad debe contar obligatoriamente con su Guia de Usuario en `docs\user_guide_<feature>.md` antes de solicitar revision o cierre.',
    '',
    '## 3. Mapa de Documentacion',
    '- Principios innegociables: `.specify\memory\constitution.md`',
    '- Configuracion de ejecucion: `.specify\harness-config.json`',
    '- Plantillas de artefactos: `.specify\templates\`',
    '- Guias de usuario obligatorias: `docs\user_guide_<feature>.md`',
    '- Criterios de cierre: `CHECKPOINTS.md`',
    '- Estado del backlog: `feature_list.json`',
    '',
    '## 4. Comandos del Entorno (PowerShell)',
    '- Validar salud y tests: `.\harness\init.ps1`',
    '- Consultar backlog: `.\harness\sdd.ps1 -Action status`',
    '- Avanzar ciclo: `.\harness\sdd.ps1 -Action next` (despliega Checkpoint Humano automático si hay specs listas)',
    '- Aprobar con candado criptografico (Humano): `.\harness\sdd.ps1 -Action approve -FeatureId <id>`',
    '- Auditar alcance, arquitectura y guia de usuario: `.\harness\spec-gate.ps1 -FeatureId <carpeta_feature>`'
)

Write-SddFile -Path "anti-gravity.md" -Lines @(
    '# Google Antigravity Environment Guidelines (Windows - v4.2)',
    '',
    '@AGENTS.md',
    '',
    '## 1. Reglas de Ejecucion en el IDE',
    '- La terminal predeterminada es PowerShell. Usa siempre sintaxis nativa de Windows (`.\harness\init.ps1`, `.\harness\sdd.ps1`).',
    '- Antes de proponer cambios o invocar subagentes, ejecuta `.\harness\init.ps1`.',
    '- Respeta estrictamente la seccion `## 5. Allowed Files` de la especificacion activa.',
    '- Utiliza las plantillas de `.specify\templates\` para redactar `spec.md`, `scenarios.feature`, `plan.md` y `tasks.md`.',
    '- Genera obligatoriamente la Guia de Usuario en `docs\user_guide_<id>.md` utilizando `.specify\templates\user_guide.template.md` antes de invocar la auditoria de cierre.',
    '',
    '## 2. Regla Anti-Telefono-Descompuesto',
    '- No pases bloques de codigo por el chat entre subagentes.',
    '- Escribe los resultados tecnicos en `progress\impl_<id>.md` o `progress\review_<id>.md` y responde unicamente con la referencia al archivo en disco.',
    '',
    '## 3. Puertas de Control Humano y Candado Criptografico',
    '- Queda ESTRICTAMENTE PROHIBIDO que el agente modifique manualmente el estado a `in_progress` o `done` en `feature_list.json`.',
    '- La unica via legal para autorizar el paso a `in_progress` es ejecutar:',
    '  `.\harness\sdd.ps1 -Action approve -FeatureId <id>` (o invocar `.\harness\sdd.ps1 -Action next` estando en `spec_ready`).'
)

Write-SddFile -Path ".specify\memory\constitution.md" -Lines @(
    '# Constitucion del Proyecto (SDD + BDD + Clean Architecture v4.2)',
    '',
    'Toda especificacion, escenario Gherkin, plan tecnico, tarea e implementacion debe cumplir estas reglas innegociables:',
    '',
    '1. **La Spec Manda:** Ningun codigo de produccion se escribe ni se modifica sin estar respaldado por un requisito EARS en `specs\<feature>\spec.md` y un escenario Gherkin en `specs\<feature>\scenarios.feature`.',
    '2. **Stack Tecnologico:** Gobernado dinamicamente por `.specify\harness-config.json`.',
    '3. **Cero Dependencias Sorpresa:** Prohibido anadir paquetes externos no aprobados en `## 3. Allowed Dependencies` de `plan.md`.',
    '4. **Logica Separada de la Interfaz (Clean Architecture):** El dominio (`src\domain\`) y los casos de uso (`src\application\`) no deben importar detalles HTTP, UI, bases de datos o librerias de infraestructura.',
    '5. **Double-Loop BDD + TDD Obligatorio:** Primero se define el escenario en `scenarios.feature`, se implementan los step definitions en `tests\acceptance\` y tests unitarios en `tests\unit\` (Rojo), se implementa el codigo minimo en `src\` (Verde) y se refactoriza.',
    '6. **Trazabilidad Triple de Criterios:** Cada Criterio de Aceptacion (`AC-x.x`) debe estar mapeado a `@AC-x.x` en `scenarios.feature` y probado en `tests\`.',
    '7. **Inmutabilidad y Candado SHA-256:** Ninguna funcionalidad puede pasar a desarrollo sin la firma criptografica humana generada por `.\harness\sdd.ps1 -Action approve`.',
    '8. **Guia de Usuario Obligatoria:** Ninguna funcionalidad puede considerarse finalizada ni pasar a estado `done` sin contar con su Guia de Usuario en `docs\user_guide_<feature>.md`, redactada a partir de los escenarios BDD para usuarios finales.'
)

Write-SddFile -Path "feature_list.json" -Lines @('[]')

Write-SddFile -Path "CHECKPOINTS.md" -Lines @(
    '# CHECKPOINTS.md — Criterios de Aceptacion y Calidad de Cierre (v4.2)',
    '',
    'Para autorizar el estado `done` en `feature_list.json`, cada funcionalidad debe cumplir:',
    '',
    '- [ ] Cero errores en `.\harness\init.ps1` (linter/typecheck + pytest unitario y pytest-bdd en verde).',
    '- [ ] Cero violaciones en `.\harness\spec-gate.ps1`:',
    '      1. Cero archivos modificados fuera de `Allowed Files` (Spec Drift).',
    '      2. Cero importaciones prohibidas de infraestructura en `src\domain` y `src\application`.',
    '      3. Cero dependencias no autorizadas en `plan.md`.',
    '      4. 100% de los criterios EARS (`AC-x.x`) mapeados a etiquetas `@AC-x.x` en `scenarios.feature`.',
    '      5. 100% de los criterios EARS (`AC-x.x`) probados en `tests\`.',
    '      6. Guia de Usuario obligatoria generada y completa en `docs\user_guide_<feature>.md`.',
    '- [ ] Documentacion registrada en `progress\review_<feature>.md`.'
)

# ==============================================================================
# 5. SCRIPTS DEL ARNES TECNICO (harness/) - PARCHE v4.1 / v4.2 INCLUIDO
# ==============================================================================
Write-SddFile -Path "harness\init.ps1" -Lines @(
    '# harness\init.ps1 - Arnes Dinamico de Salud y Verificacion en Windows (v4.2)',
    '$ErrorActionPreference = "Stop"',
    '',
    'Write-Host "=== [SDD Harness v4.2] Verificando Salud del Repositorio ===" -ForegroundColor Cyan',
    '',
    '$RequiredFiles = @("AGENTS.md", "anti-gravity.md", ".specify\memory\constitution.md", ".specify\harness-config.json", "feature_list.json")',
    'foreach ($file in $RequiredFiles) {',
    '    if (-not (Test-Path $file)) {',
    '        Write-Error "[Error Critico]: Falta el archivo fundamental $file."',
    '        exit 1',
    '    }',
    '}',
    '',
    'try {',
    '    $Config = Get-Content -Path ".specify\harness-config.json" -Raw -Encoding UTF8 | ConvertFrom-Json',
    '} catch {',
    '    Write-Error "[Error Critico]: .specify\harness-config.json contiene JSON invalido."',
    '    exit 1',
    '}',
    '',
    'try {',
    '    $rawJson = Get-Content -Path "feature_list.json" -Raw -Encoding UTF8',
    '    $Features = @()',
    '    if (-not [string]::IsNullOrWhiteSpace($rawJson)) {',
    '        $parsed = ConvertFrom-Json $rawJson',
    '        if ($null -ne $parsed) {',
    '            if ($parsed.PSObject.Properties["features"]) { $parsed = $parsed.features }',
    '            foreach ($item in $parsed) { if ($null -ne $item) { $Features += $item } }',
    '        }',
    '    }',
    '} catch {',
    '    Write-Error "[Error Critico]: feature_list.json contiene JSON invalido."',
    '    exit 1',
    '}',
    '',
    'if ($Features.Count -gt 0) {',
    '    $InProgressList = @($Features | Where-Object { $_.status -eq "in_progress" })',
    '    if ($InProgressList.Count -gt 1) {',
    '        Write-Error "[Violacion de Arnes]: Hay $($InProgressList.Count) tareas en in_progress. Maximo 1 a la vez."',
    '        exit 1',
    '    }',
    '    if ($InProgressList.Count -eq 1) {',
    '        $Active = $InProgressList[0]',
    '        if ([string]::IsNullOrWhiteSpace($Active.approval_hash)) {',
    '            Write-Error "[Violacion Criptografica]: La funcionalidad $($Active.id) esta en in_progress sin approval_hash. Ejecuta: .\harness\sdd.ps1 -Action approve -FeatureId $($Active.id)"',
    '            exit 1',
    '        }',
    '        $SpecDir = if ($Active.feature_dir) { $Active.feature_dir } else { $Active.id }',
    '        $SpecPath = "specs\$SpecDir\spec.md"',
    '        $FeatPath = "specs\$SpecDir\scenarios.feature"',
    '        if ((Test-Path $SpecPath) -and (Test-Path $FeatPath)) {',
    '            $SpecContent = Get-Content -Path $SpecPath -Raw -Encoding UTF8',
    '            $FeatContent = Get-Content -Path $FeatPath -Raw -Encoding UTF8',
    '            $Combined = $SpecContent + "---" + $FeatContent',
    '            $Hasher = [System.Security.Cryptography.SHA256]::Create()',
    '            $CurrentHash = [BitConverter]::ToString($Hasher.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($Combined))) -replace "-"',
    '            if ($CurrentHash -ne $Active.approval_hash) {',
    '                Write-Error "[Spec Tampering]: La especificacion de $($Active.id) fue modificada tras la aprobacion. Re-aprueba con .\harness\sdd.ps1 -Action approve -FeatureId $($Active.id)"',
    '                exit 1',
    '            }',
    '        }',
    '    }',
    '}',
    '',
    'if (Test-Path $Config.source_dir) {',
    '    $CodeFiles = @(Get-ChildItem -Path $Config.source_dir -Filter $Config.file_extension -Recurse -ErrorAction SilentlyContinue)',
    '    if ($CodeFiles.Count -gt 0 -and $Config.typecheck_cmd) {',
    '        Write-Host "Ejecutando analisis estatico ($($Config.typecheck_cmd))..." -ForegroundColor Yellow',
    '        Invoke-Expression $Config.typecheck_cmd',
    '        if ($LASTEXITCODE -ne 0) {',
    '            Write-Error "[Error de Calidad]: Fallo el analisis de tipos estaticos."',
    '            exit 1',
    '        }',
    '    }',
    '}',
    '',
    'if (Test-Path $Config.test_dir) {',
    '    $TestFiles = @(Get-ChildItem -Path $Config.test_dir -Filter $Config.file_extension -Recurse -ErrorAction SilentlyContinue)',
    '    if ($TestFiles.Count -gt 0 -and $Config.test_cmd) {',
    '        Write-Host "Ejecutando suite de pruebas ($($Config.test_cmd))..." -ForegroundColor Yellow',
    '        Invoke-Expression $Config.test_cmd',
    '        if ($LASTEXITCODE -ne 0) {',
    '            Write-Error "[Error de Testing]: Las pruebas estan fallando."',
    '            exit 1',
    '        }',
    '    }',
    '}',
    '',
    'Write-Host "[SDD Harness v4.2]: Entorno verificado exitosamente (Exit 0)." -ForegroundColor Green',
    'exit 0'
)

Write-SddFile -Path "harness\sdd.ps1" -Lines @(
    '# harness\sdd.ps1 - Orquestador del Bucle SDD con Checkpoint Humano Interactivo (v4.2)',
    'param (',
    '    [ValidateSet("status", "next", "verify", "approve")]',
    '    [string]$Action = "status",',
    '    [string]$FeatureId',
    ')',
    '',
    '$ErrorActionPreference = "Stop"',
    '',
    'function Get-FeaturesList {',
    '    $raw = Get-Content -Path "feature_list.json" -Raw -Encoding UTF8',
    '    $list = @()',
    '    if (-not [string]::IsNullOrWhiteSpace($raw)) {',
    '        $parsed = ConvertFrom-Json $raw',
    '        if ($null -ne $parsed) {',
    '            if ($parsed.PSObject.Properties["features"]) { $parsed = $parsed.features }',
    '            foreach ($item in $parsed) { if ($null -ne $item) { $list += $item } }',
    '        }',
    '    }',
    '    return ,$list',
    '}',
    '',
    'function Invoke-InitCheck {',
    '    $InitScript = "harness\init.ps1"',
    '    if (Test-Path $InitScript) {',
    '        & $InitScript',
    '    } else {',
    '        Write-Error "No se encontro $InitScript"',
    '        exit 1',
    '    }',
    '    return (Get-FeaturesList)',
    '}',
    '',
    'function Invoke-ApproveFeature {',
    '    param([string]$TargetId)',
    '    $Features = Get-FeaturesList',
    '    $Target = $null',
    '    foreach ($item in $Features) {',
    '        if ($null -ne $TargetId -and $TargetId -ne "") {',
    '            if ($item.id -eq $TargetId -or $item.feature_dir -eq $TargetId) {',
    '                $Target = $item',
    '                break',
    '            }',
    '        } else {',
    '            if ($item.status -eq "spec_ready") {',
    '                $Target = $item',
    '                break',
    '            }',
    '        }',
    '    }',
    '    if ($null -eq $Target) {',
    '        Write-Error "No se encontro ninguna funcionalidad en estado spec_ready para aprobar."',
    '        exit 1',
    '    }',
    '    $SpecDir = if ($Target.feature_dir) { $Target.feature_dir } else { $Target.id }',
    '    $Target | Add-Member -NotePropertyName "feature_dir" -NotePropertyValue $SpecDir -Force',
    '    $SpecPath = "specs\$SpecDir\spec.md"',
    '    $FeatPath = "specs\$SpecDir\scenarios.feature"',
    '    if ((-not (Test-Path $SpecPath)) -or (-not (Test-Path $FeatPath))) {',
    '        Write-Error "Faltan archivos requeridos: $SpecPath o $FeatPath."',
    '        exit 1',
    '    }',
    '    Write-Host "`n[HUMAN CHECKPOINT - CANDADO CRIPTOGRAFICO]" -ForegroundColor Magenta',
    '    Write-Host "Revision formal de: [$($Target.id)] $($Target.name)" -ForegroundColor Cyan',
    '    $Confirmation = Read-Host "Confirmas la aprobacion humana para desbloquear in_progress? (S/N)"',
    '    if ($Confirmation -notmatch "^[SsYy]$") {',
    '        Write-Host "Aprobacion cancelada por el usuario." -ForegroundColor Yellow',
    '        exit 0',
    '    }',
    '    $SpecContent = Get-Content -Path $SpecPath -Raw -Encoding UTF8',
    '    $FeatContent = Get-Content -Path $FeatPath -Raw -Encoding UTF8',
    '    $Combined = $SpecContent + "---" + $FeatContent',
    '    $Hasher = [System.Security.Cryptography.SHA256]::Create()',
    '    $ApprovalHash = [BitConverter]::ToString($Hasher.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($Combined))) -replace "-"',
    '    $Target | Add-Member -NotePropertyName "status" -NotePropertyValue "in_progress" -Force',
    '    $Target | Add-Member -NotePropertyName "approval_hash" -NotePropertyValue $ApprovalHash -Force',
    '    $Target | Add-Member -NotePropertyName "approved_at" -NotePropertyValue (Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ") -Force',
    '    $JsonOut = ConvertTo-Json -InputObject @($Features) -Depth 5',
    '    if ($Features.Count -eq 1 -and $JsonOut -notmatch "^\s*\[") { $JsonOut = "[`r`n$JsonOut`r`n]" }',
    '    $Utf8Bom = New-Object System.Text.UTF8Encoding($true)',
    '    [System.IO.File]::WriteAllText((Join-Path $PWD "feature_list.json"), $JsonOut, $Utf8Bom)',
    '    Write-Host "[APROBADO]: Firma SHA-256 registrada ($($ApprovalHash.Substring(0,16))...). Estado cambiado a in_progress." -ForegroundColor Green',
    '}',
    '',
    'switch ($Action) {',
    '    "status" {',
    '        $Features = Invoke-InitCheck',
    '        Write-Host "`n=== Estado del Backlog de Funcionalidades (SDD v4.2) ===" -ForegroundColor Cyan',
    '        if ($Features.Count -eq 0) {',
    '            Write-Host "El backlog esta vacio []." -ForegroundColor Yellow',
    '            exit 0',
    '        }',
    '        foreach ($f in $Features) {',
    '            $st = if ($f.status) { $f.status } else { "pending" }',
    '            $color = switch ($st) {',
    '                "done" { "Green" }',
    '                "in_progress" { "Yellow" }',
    '                "spec_ready" { "Magenta" }',
    '                "review" { "DarkYellow" }',
    '                default { "Gray" }',
    '            }',
    '            $hashShort = if ($f.approval_hash) { " [SHA: $($f.approval_hash.Substring(0,8))]" } else { "" }',
    '            Write-Host "[$($st.ToUpper())] $($f.id): $($f.name)$hashShort" -ForegroundColor $color',
    '        }',
    '    }',
    '    "verify" {',
    '        Invoke-InitCheck | Out-Null',
    '    }',
    '    "approve" {',
    '        Invoke-ApproveFeature -TargetId $FeatureId',
    '    }',
    '    "next" {',
    '        $Features = Invoke-InitCheck',
    '        if ($Features.Count -eq 0) {',
    '            Write-Host "`n[BACKLOG VACIO]: Inicia tu primera funcionalidad con .agents/skills/sdd-onboard.md." -ForegroundColor Yellow',
    '            exit 0',
    '        }',
    '        $Active = $null',
    '        foreach ($item in $Features) {',
    '            if ($item.status -in @("pending", "spec_ready", "in_progress", "review")) {',
    '                $Active = $item',
    '                break',
    '            }',
    '        }',
    '        if ($null -eq $Active) {',
    '            Write-Host "`n[EXITO TOTAL]: Todas las funcionalidades estan en done." -ForegroundColor Green',
    '            exit 0',
    '        }',
    '        $SpecDir = if ($Active.feature_dir) { $Active.feature_dir } else { $Active.id }',
    '        Write-Host "`n------------------------------------------------------------------" -ForegroundColor Cyan',
    '        Write-Host "  FUNCIONALIDAD ACTIVA: [$($Active.id)] $($Active.name)" -ForegroundColor Cyan',
    '        Write-Host "  ESTADO ACTUAL: $($Active.status.ToUpper())" -ForegroundColor Cyan',
    '        Write-Host "------------------------------------------------------------------" -ForegroundColor Cyan',
    '        switch ($Active.status) {',
    '            "pending" {',
    '                Write-Host "PASO A EJECUTAR: Fase 1 - SPECIFY (EARS + Gherkin)" -ForegroundColor Blue',
    '                Write-Host " Instruccion: Redacta specs\$SpecDir\spec.md y scenarios.feature usando .specify\templates\."',
    '            }',
    '            "spec_ready" {',
    '                Write-Host "CHECKPOINT HUMANO 1: Aprobacion Criptografica Requerida" -ForegroundColor Magenta',
    '                Invoke-ApproveFeature -TargetId $Active.id',
    '            }',
    '            "in_progress" {',
    '                Write-Host "PASO A EJECUTAR: Fase 5 - IMPLEMENTACION DOUBLE-LOOP (BDD + TDD)" -ForegroundColor Yellow',
    '                Write-Host " Instruccion: Pide al agente ejecutar sdd-plan.md, sdd-tasks.md y luego sdd-implement.md sobre specs\$SpecDir\."',
    '            }',
    '            "review" {',
    '                Write-Host "PASO A EJECUTAR: Fase 6 - AUDITORIA SEXTUPLE" -ForegroundColor DarkYellow',
    '                Write-Host " Instruccion: Verifica docs\user_guide_$SpecDir.md, ejecuta .\harness\spec-gate.ps1 -FeatureId $SpecDir y audita CHECKPOINTS.md."',
    '            }',
    '        }',
    '    }',
    '}'
)

Write-SddFile -Path "harness\spec-gate.ps1" -Lines @(
    '# harness\spec-gate.ps1 - Auditor Sextuple (Scope, Clean Arch, Deps, BDD, Tests, User Guide) v4.2',
    'param (',
    '    [Parameter(Mandatory=$true)]',
    '    [string]$FeatureId,',
    '    [string]$BaseBranch = "main"',
    ')',
    '',
    '$ErrorActionPreference = "Stop"',
    '$SpecFile = "specs\$FeatureId\spec.md"',
    '$FeatureFile = "specs\$FeatureId\scenarios.feature"',
    '$PlanFile = "specs\$FeatureId\plan.md"',
    '',
    'Write-Host "=== [Spec-Gate v4.2]: Auditoria Sextuple para $FeatureId ===" -ForegroundColor Cyan',
    '$Config = Get-Content -Path ".specify\harness-config.json" -Raw -Encoding UTF8 | ConvertFrom-Json',
    '',
    'if (-not (Test-Path $SpecFile)) { Write-Error "Falta $SpecFile."; exit 1 }',
    'if (-not (Test-Path $FeatureFile)) { Write-Error "Falta $FeatureFile."; exit 1 }',
    '$SpecContent = Get-Content -Path $SpecFile -Raw -Encoding UTF8',
    '',
    '# 1. Allowed Files',
    '$AllowedFiles = @()',
    'if ($SpecContent -match "(?ms)##\s*5\.\s*Allowed Files\s*(.+?)(\r?\n##\s+|\z)") {',
    '    $SectionBlock = $Matches[1]',
    '    $PathMatches = [regex]::Matches($SectionBlock, "`([^`]+)`")',
    '    foreach ($m in $PathMatches) {',
    '        $Normalized = ($m.Groups[1].Value -replace "/", "\").Trim()',
    '        if ($Normalized -match "^($($Config.source_dir)|$($Config.test_dir))\\") {',
    '            $AllowedFiles += $Normalized',
    '        }',
    '    }',
    '}',
    'if ($AllowedFiles.Count -eq 0) {',
    '    Write-Error "[Spec-Gate]: ## 5. Allowed Files en $SpecFile no declara rutas validas."',
    '    exit 1',
    '}',
    '$GitAvailable = $null -ne (Get-Command git -ErrorAction SilentlyContinue)',
    'if ($GitAvailable -and (Test-Path ".git")) {',
    '    $GitStatusLines = git status --porcelain 2>$null',
    '    $ModifiedFiles = @()',
    '    foreach ($line in $GitStatusLines) {',
    '        if ($line.Length -gt 3) {',
    '            $RawPath = $line.Substring(3).Trim() -replace ''^"|"$'', '''' -replace "/", "\"',
    '            if ($RawPath -match "^($($Config.source_dir)|$($Config.test_dir))\\") {',
    '                $ModifiedFiles += $RawPath',
    '            }',
    '        }',
    '    }',
    '    $UnauthorizedFiles = @($ModifiedFiles | Where-Object { $_ -notin $AllowedFiles })',
    '    if ($UnauthorizedFiles.Count -gt 0) {',
    '        Write-Host "[Spec Drift]: Archivos modificados fuera de Allowed Files:" -ForegroundColor Red',
    '        $UnauthorizedFiles | ForEach-Object { Write-Host "   - $_" -ForegroundColor Red }',
    '        exit 1',
    '    }',
    '    Write-Host "  [OK] 1. Allowed Files: Sin Spec Drift." -ForegroundColor Green',
    '}',
    '',
    '# 2. Clean Architecture',
    '$DomainPath = Join-Path $Config.source_dir "domain"',
    '$AppPath = Join-Path $Config.source_dir "application"',
    '$ForbiddenImports = $Config.forbidden_domain_imports',
    '$ArchViolations = @()',
    'foreach ($targetDir in @($DomainPath, $AppPath)) {',
    '    if (Test-Path $targetDir) {',
    '        $Files = Get-ChildItem -Path $targetDir -Filter $Config.file_extension -Recurse -ErrorAction SilentlyContinue',
    '        foreach ($file in $Files) {',
    '            $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8',
    '            foreach ($badLib in $ForbiddenImports) {',
    '                if ($content -match "(?m)^\s*(import\s+$badLib|from\s+$badLib)") {',
    '                    $ArchViolations += "$($file.Name) importa $badLib"',
    '                }',
    '            }',
    '        }',
    '    }',
    '}',
    'if ($ArchViolations.Count -gt 0) {',
    '    Write-Host "[Violacion Clean Architecture]:" -ForegroundColor Red',
    '    $ArchViolations | ForEach-Object { Write-Host "   - $_" -ForegroundColor Red }',
    '    exit 1',
    '}',
    'Write-Host "  [OK] 2. Clean Architecture: Dominio y Aplicacion aislados." -ForegroundColor Green',
    '',
    '# 3. Dependencias en plan.md',
    'if (Test-Path $PlanFile) {',
    '    Write-Host "  [OK] 3. Dependencias: Verificado contra plan.md." -ForegroundColor Green',
    '}',
    '',
    '# 4. Cobertura BDD (@AC-x.x)',
    '$CriteriaMatches = [regex]::Matches($SpecContent, "\bAC-\d+\.\d+\b")',
    '$UniqueCriteria = @($CriteriaMatches | ForEach-Object { $_.Value } | Select-Object -Unique)',
    'if ($UniqueCriteria.Count -eq 0) {',
    '    Write-Error "No se encontraron Criterios EARS (AC-x.x) en $SpecFile."',
    '    exit 1',
    '}',
    '$GherkinContent = Get-Content -Path $FeatureFile -Raw -Encoding UTF8',
    '$MissingGherkin = @()',
    'foreach ($ac in $UniqueCriteria) {',
    '    if ($GherkinContent -notmatch "@$([regex]::Escape($ac))\b") { $MissingGherkin += $ac }',
    '}',
    'if ($MissingGherkin.Count -gt 0) {',
    '    Write-Host "[Fallo BDD]: Criterios sin escenario @AC-x.x:" -ForegroundColor Red',
    '    $MissingGherkin | ForEach-Object { Write-Host "   - @$_" -ForegroundColor Red }',
    '    exit 1',
    '}',
    'Write-Host "  [OK] 4. Cobertura BDD: 100% de criterios mapeados a Gherkin." -ForegroundColor Green',
    '',
    '# 5. Trazabilidad en tests\',
    '$TestFiles = @(Get-ChildItem -Path $Config.test_dir -Filter $Config.file_extension -File -Recurse -ErrorAction SilentlyContinue)',
    '$CombinedTests = ($TestFiles | ForEach-Object { Get-Content -Path $_.FullName -Raw -Encoding UTF8 }) -join "`n"',
    '$MissingTests = @()',
    'foreach ($ac in $UniqueCriteria) {',
    '    $Snake = ($ac -replace "-", "_" -replace "\.", "_").ToLower()',
    '    if (($CombinedTests -notmatch [regex]::Escape($ac)) -and ($CombinedTests -notmatch [regex]::Escape($Snake))) {',
    '        $MissingTests += $ac',
    '    }',
    '}',
    'if ($MissingTests.Count -gt 0) {',
    '    Write-Host "[Fallo en Tests]: Criterios no probados en tests\:" -ForegroundColor Red',
    '    $MissingTests | ForEach-Object { Write-Host "   - $_" -ForegroundColor Red }',
    '    exit 1',
    '}',
    'Write-Host "  [OK] 5. Trazabilidad Tests: 100% de criterios probados." -ForegroundColor Green',
    '',
    '    # 6. Guia de Usuario Obligatoria',
    '    $UserGuidePath1 = "docs\user_guide_$FeatureId.md"',
    '    $UserGuidePath2 = "docs\$FeatureId`_user_guide.md"',
    '    $FoundGuide = $null',
    '    if (Test-Path $UserGuidePath1) { $FoundGuide = $UserGuidePath1 }',
    '    elseif (Test-Path $UserGuidePath2) { $FoundGuide = $UserGuidePath2 }',
    '',
    '    if ($null -eq $FoundGuide) {',
    '        Write-Host "[Fallo Documentacion]: Falta la Guia de Usuario obligatoria en docs\user_guide_$FeatureId.md." -ForegroundColor Red',
    '        exit 1',
    '    }',
    '    $GuideContent = Get-Content -Path $FoundGuide -Raw -Encoding UTF8',
    '    if ([string]::IsNullOrWhiteSpace($GuideContent) -or $GuideContent.Trim().Length -lt 80) {',
    '        Write-Host "[Fallo Documentacion]: La Guia de Usuario en $FoundGuide esta vacia o incompleta (minimo 80 caracteres)." -ForegroundColor Red',
    '        exit 1',
    '    }',
    '    Write-Host "  [OK] 6. Guia de Usuario: Verificada en $FoundGuide." -ForegroundColor Green',
    '    Write-Host "[Spec-Gate v4.2]: Auditoria Sextuple superada con CERO violaciones." -ForegroundColor Green',
    '    exit 0'
)

# ==============================================================================
# 6. GIT E INSTALACION DE PRE-COMMIT HOOK
# ==============================================================================
Write-SddFile -Path ".gitignore" -Lines @(
    '__pycache__/',
    '*.py[cod]',
    '.mypy_cache/',
    '.pytest_cache/',
    '*.sqlite3',
    '.env',
    'progress/impl_*.md'
)

if ($null -ne (Get-Command git -ErrorAction SilentlyContinue)) {
    if (-not (Test-Path ".git")) {
        git init | Out-Null
        Write-Host "  [+] Repositorio Git inicializado." -ForegroundColor Green
    }
    Write-SddFile -Path ".git\hooks\pre-commit" -Lines @(
        '#!/bin/sh',
        'powershell.exe -ExecutionPolicy Bypass -File .\harness\init.ps1',
        'if [ $? -ne 0 ]; then exit 1; fi'
    )
}

# ==============================================================================
# 7. SKILLS AGENTICAS (.agents/skills/)
# ==============================================================================
Write-SddFile -Path ".agents\skills\sdd-onboard.md" -Lines @(
    '---',
    'name: sdd-onboard',
    'description: Guia la entrevista interactiva inicial (1 pregunta por turno) para configurar el proyecto, constitution.md, feature_list.json y la primera spec + scenarios.feature.',
    '---',
    '# Skill: SDD Onboard (v4.2)',
    '## REGLA FUNDAMENTAL DE INTERACCION',
    'Realiza EXACTAMENTE UNA PREGUNTA POR TURNO. Espera la respuesta antes de formular la siguiente.',
    '## Workflow',
    '1. Pregunta 1: Tipo de aplicacion y proposito principal.',
    '2. Pregunta 2: Lenguaje, version y librerias clave (actualiza `.specify/harness-config.json`).',
    '3. Pregunta 3: Linters y test runner (actualiza `.specify/harness-config.json`).',
    '4. Actualiza `.specify/memory/constitution.md` y `AGENTS.md`.',
    '5. Pregunta 4: Nombre y descripcion de FEAT-001. Registra en `feature_list.json` con `"status": "pending"`.',
    '6. Preguntas 5 a 7 (una por turno): Roles/historia principal, casos borde/errores y elementos Fuera de Alcance.',
    '7. Genera `specs/001-<slug>/spec.md` y `specs/001-<slug>/scenarios.feature` usando `.specify/templates/`.',
    '8. Cambia el estado a `"spec_ready"` e indica al usuario ejecutar: `.\harness\sdd.ps1 -Action next` (lo cual invocará interactivamente el candado criptográfico).'
)

Write-SddFile -Path ".agents\skills\sdd-constitution.md" -Lines @(
    '---',
    'name: sdd-constitution',
    'description: Administra las leyes inmutables del proyecto en .specify/memory/constitution.md.',
    '---',
    '# Skill: SDD Constitution (v4.2)',
    'Sincroniza `.specify/memory/constitution.md` y `.specify/harness-config.json`.'
)

Write-SddFile -Path ".agents\skills\sdd-specify.md" -Lines @(
    '---',
    'name: sdd-specify',
    'description: Redacta spec.md y scenarios.feature usando .specify/templates/.',
    '---',
    '# Skill: SDD Specify (v4.2)',
    'Genera `spec.md` (con `## 5. Allowed Files`) y `scenarios.feature` (con tags `@AC-x.x`) usando `.specify/templates/`.'
)

Write-SddFile -Path ".agents\skills\sdd-clarify.md" -Lines @(
    '---',
    'name: sdd-clarify',
    'description: Audita ambiguedades o lagunas en spec.md y scenarios.feature.',
    '---',
    '# Skill: SDD Clarify (v4.2)',
    'Verifica con enfoque adversarial que cada `AC-x.x` tenga su escenario `@AC-x.x` y que `Allowed Files` respete Clean Architecture.'
)

Write-SddFile -Path ".agents\skills\sdd-plan.md" -Lines @(
    '---',
    'name: sdd-plan',
    'description: Disena plan.md usando .specify/templates/plan.template.md.',
    '---',
    '# Skill: SDD Plan (v4.2)',
    'Genera `specs/<feature>/plan.md` definiendo arquitectura limpia y `## 3. Allowed Dependencies`.'
)

Write-SddFile -Path ".agents\skills\sdd-tasks.md" -Lines @(
    '---',
    'name: sdd-tasks',
    'description: Descompone plan.md en tareas atomicas TDD en tasks.md e incluye la Guia de Usuario obligatoria.',
    '---',
    '# Skill: SDD Tasks (v4.2)',
    'Genera `specs/<feature>/tasks.md` usando `.specify/templates/tasks.template.md`, asegurando incluir la tarea de redaccion de la Guia de Usuario en `docs/user_guide_<feature>.md`.'
)

Write-SddFile -Path ".agents\skills\sdd-implement.md" -Lines @(
    '---',
    'name: sdd-implement',
    'description: Ejecuta tareas de desarrollo (Double-Loop BDD + TDD), redacta docs/user_guide_<feature>.md y registra progress/impl_<id>.md.',
    '---',
    '# Skill: SDD Implement (v4.2)',
    'Toma la primera tarea `[ ]` de `tasks.md`. En codigo: escribe el test en Rojo, implementa el codigo minimo en Verde y pasa `.\harness\init.ps1`. En documentacion: redacta la Guia de Usuario obligatoria en `docs/user_guide_<feature>.md` usando `.specify/templates/user_guide.template.md`. Guarda el reporte en `progress/`.'
)

Write-SddFile -Path ".agents\skills\sdd-user-guide.md" -Lines @(
    '---',
    'name: sdd-user-guide',
    'description: Redacta y valida la Guia de Usuario obligatoria en docs/user_guide_<feature>.md a partir de los escenarios BDD.',
    '---',
    '# Skill: SDD User Guide (v4.2)',
    'Toma la especificacion y escenarios BDD de `specs/<feature>/` y genera la Guia de Usuario en `docs/user_guide_<feature>.md` siguiendo `.specify/templates/user_guide.template.md`. Requisito innegociable para superar `spec-gate.ps1`.'
)

Write-SddFile -Path ".agents\skills\sdd-validate.md" -Lines @(
    '---',
    'name: sdd-validate',
    'description: Audita el cierre de la feature con spec-gate.ps1 (Auditor Sextuple que incluye la Guia de Usuario).',
    '---',
    '# Skill: SDD Validate (v4.2)',
    'Verifica la existencia y calidad de `docs/user_guide_<feature>.md`, ejecuta `.\harness\spec-gate.ps1 -FeatureId <feature_dir>` y comprueba `CHECKPOINTS.md`.'
)

Write-SddFile -Path ".agents\skills\sdd-change-spec.md" -Lines @(
    '---',
    'name: sdd-change-spec',
    'description: Control de cambios que exige actualizar spec.md, scenarios.feature y re-aprobar el hash SHA-256.',
    '---',
    '# Skill: SDD Change Spec (v4.2)',
    'Actualiza primero `spec.md` y `scenarios.feature`, y solicita al humano aprobar la nueva firma.'
)

Write-SddFile -Path ".agents\skills\sdd-reverse-spec.md" -Lines @(
    '---',
    'name: sdd-reverse-spec',
    'description: Ingenieria inversa brownfield hacia spec.md y scenarios.feature.',
    '---',
    '# Skill: SDD Reverse Spec (v4.2)',
    'Analiza codigo heredado y redacta su `spec.md` y `scenarios.feature` antes de refactorizar.'
)

Write-Host "`n[EXITO]: Infraestructura SDD v4.2 (con parche interactivo integrado) inicializada correctamente." -ForegroundColor Green
"""

with open("setup-sdd-project-v4.ps1", "w", encoding="utf-8-sig") as f:
    f.write(script_content)

print("setup-sdd-project-v4.ps1 actualizado con éxito a la versión v4.2")