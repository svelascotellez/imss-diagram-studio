# Guía Maestra Definitiva: Arquitectura, Artefactos y Gobierno de Setup SDD (v5.4)

---

## 1. Introducción y Fundamentos Metodológicos

El framework **Setup SDD (Specification-Driven Development v5.4)** es una infraestructura integral de ingeniería de software diseñada para gobernar el ciclo de vida del desarrollo asistido por Inteligencia Artificial (IA) en entornos profesionales. Su premisa operativa fundamental es: **ninguna línea de código de producción puede existir sin una especificación formal aprobada, verificable y criptográficamente sellada**.

A diferencia de los entornos convencionales donde los agentes de IA generan código de forma no controlada, SDD v5.4 establece compuertas duras (*hard gates*), inspección de AST/expresiones regulares, validación matemática de diseño y ganchos de ciclo de vida (*hooks*) nativos en **Google Antigravity IDE**.

### Los 5 Pilares de SDD v5.4

```text
┌────────────────────────────────────────────────────────────────────────┐
│                          SDD v5.4 PILARES                             │
├─────────────────┬─────────────────┬─────────────────┬──────────────────┤
│ 1. Spec-First   │ 2. BDD Riguroso │ 3. Clean Arch   │ 4. UI/UX Pro Max │
│    & Anti-Drift │    EARS/Gherkin │    Políglota    │    Matemático    │
├─────────────────┴─────────────────┴─────────────────┴──────────────────┤
│           5. Criptografía Human-in-the-Loop & Gobernanza DAG           │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Spec-Driven Development (SDD) & Anti-Spec Drift:** Cada funcionalidad nace en un documento de especificación formal (`spec.md`) que declara taxativamente la lista blanca de archivos permitidos (`## 5. Allowed Files`). Cualquier modificación fuera de esta lista bloquea físicamente la ejecución del agente.
2. **Behavior-Driven Development (BDD) Bidireccional:** Los requisitos se redactan bajo la sintaxis **EARS** (*Easy Approach to Requirements Syntax*) con identificadores únicos (`AC-x.x`). Estos criterios se mapean en relación 1:1 con escenarios **Gherkin** (`@AC-x.x`) y funciones de prueba automatizadas.
3. **Clean Architecture Políglota Estricta:** Separación matemática de responsabilidades en cuatro capas concéntricas (`domain`, `application`, `infrastructure` y `presentation`), con soporte nativo para **Python**, **TypeScript**, **Go**, **C# .NET** y **Rust**, impidiendo el acoplamiento directo y garantizando la inversión de dependencias.
4. **UI/UX Pro Max con Verificación Matemática:** Gobernanza formal del diseño mediante tokens (`design-tokens.json`). Valida algorítmicamente el ratio de contraste de luminancia relativa **WCAG 2.1 AA** ($\ge 4.5:1$), exige los 5 estados interactivos obligatorios y erradica los códigos hexadecimales mágicos (*magic hex codes*).
5. **Criptografía Human-in-the-Loop y Gobernanza de Dependencias:** El agente tiene prohibido auto-aprobarse. Sólo un operador humano puede emitir el candado criptográfico **SHA-256** (`harness/sdd.ps1 -Action approve -Reason <motivo>`). Además, el backlog modela un Grafo Acíclico Dirigido (DAG) mediante `depends_on`, impidiendo que se trabaje en funcionalidades cuyas dependencias no estén formalmente concluidas.

---

## 2. Mapa Completo del Árbol de Directorios y Archivos

Al inicializar un proyecto con `setup-sdd-project-v54.ps1` o `setup-sdd-project-v54.py`, se genera la siguiente topología de archivos:

```text
<RAÍZ_DEL_PROYECTO>/
│
├── .agents/                                    # Configuración de Hooks y Skills nativas del IDE
│   ├── hooks.json                              # Declaración de hooks SessionStart, PreToolUse y PostToolUse
│   └── skills/                                 # 15 Skills operativas canónicas (carpetas con SKILL.md + alias .md)
│       ├── sdd-orchestrator/SKILL.md           # Orquestador del ciclo de vida y navegación entre fases
│       ├── sdd-onboard/SKILL.md                # Entrevista guiada socrática (1 pregunta por turno)
│       ├── sdd-constitution/SKILL.md           # Gestión de leyes inmutables de calidad y stack
│       ├── sdd-specify/SKILL.md                # Redacción de especificaciones EARS y Gherkin
│       ├── sdd-clarify/SKILL.md                # Auditoría adversarial de ambigüedades
│       ├── sdd-ui-ux/SKILL.md                  # Inteligencia de diseño UI/UX Pro Max y accesibilidad WCAG
│       ├── sdd-design-system/SKILL.md          # Tokens de diseño UI/UX y tokens semánticos
│       ├── sdd-preview-design/SKILL.md         # Previsualización y renderizado de componentes UI
│       ├── sdd-plan/SKILL.md                   # Plan técnico Clean Arch + Dependencias permitidas
│       ├── sdd-tasks/SKILL.md                  # Desglose en tareas atómicas TDD
│       ├── sdd-implement/SKILL.md              # Implementación Double-Loop TDD/BDD
│       ├── sdd-user-guide/SKILL.md             # Redacción de la Guía de Usuario en 4 secciones
│       ├── sdd-validate/SKILL.md               # Auditoría previa con el Auditor Séptuple
│       ├── sdd-change-spec/SKILL.md            # Gestión de cambios formales con versionado de hashes
│       └── sdd-reverse-spec/SKILL.md           # Ingeniería inversa brownfield para código heredado
│
├── .specify/                                   # Memoria, tokens y plantillas maestras
│   ├── memory/
│   │   ├── constitution.md                     # Constitución inmutable: reglas arquitectónicas del proyecto
│   │   └── onboard-state.json                  # Memoria persistente de progreso de la Entrevista Adaptativa SDD 2.0
│   ├── design-system/
│   │   └── design-tokens.json                  # Tokens UI/UX: paleta, tipografía, espaciado y estados
│   ├── templates/                              # Plantillas maestras estructurales
│   │   ├── spec.template.md                    # Plantilla EARS con sección Allowed Files
│   │   ├── scenarios.template.feature          # Plantilla Gherkin con etiquetas @AC-x.x
│   │   ├── plan.template.md                    # Plantilla de arquitectura, dependencias y tokens
│   │   ├── tasks.template.md                   # Plantilla de tareas atómicas TDD
│   │   ├── user_guide.template.md              # Plantilla obligatoria de Guía de Usuario (4 secciones)
│   │   └── impl_report.template.md             # Plantilla de reporte de implementación TDD
│   └── harness-config.json                     # Configuración políglota de linter, tests y capas
│
├── harness/                                    # Núcleo de gobernanza, pruebas y compuertas
│   ├── init.ps1                                # Verificador dinámico de salud y ejecutor de tests/linters
│   ├── sdd.ps1                                 # CLI central del backlog, candado SHA-256 y matriz
│   ├── spec-gate.ps1                           # Auditor Séptuple automatizado de cierre de feature
│   ├── preview-design.ps1                      # Generador HTML interactivo de Design System + contraste WCAG
│   └── hooks/                                  # Scripts ejecutados por el motor de Antigravity IDE
│       ├── session-start.ps1                   # Hook SessionStart: auto-onboarding e inyección de estado activo
│       ├── pre-tool-enforce.ps1                # Hook PreToolUse: interceptor físico de escritura en src/
│       └── post-tool-check.ps1                 # Hook PostToolUse: auditoría continua de Clean Architecture
│
├── specs/                                      # Directorio de especificaciones por funcionalidad
│   └── <feature_id>/                           # Ej: FEAT-001/ o 001-tablero-kanban/
│       ├── spec.md                             # Especificación funcional EARS con Allowed Files
│       ├── scenarios.feature                   # Escenarios BDD Gherkin ejecutables
│       ├── plan.md                             # Plan técnico con capas, dependencias y design tokens
│       └── tasks.md                            # Checklist de tareas atómicas TDD
│
├── docs/                                       # Documentación de cara al usuario y trazabilidad
│   ├── user_guide_<feature_id>.md              # Guía de usuario obligatoria (4 secciones estructurales)
│   └── traceability_<feature_id>.md            # Matriz de trazabilidad bidireccional auto-generada
│
├── progress/                                   # Trazabilidad técnica del desarrollo y vistas previas
│   ├── impl_<id>.md                            # Informes de ciclo TDD (Rojo -> Verde -> Refactor)
│   ├── arch_alerts.log                         # Registro automático de violaciones detectadas en PostToolUse
│   └── design_system_preview.html              # Vista interactiva generada por preview-design.ps1
│
├── src/                                        # Código fuente bajo Clean Architecture estricta
│   ├── domain/                                 # Entidades puras, Value Objects y Reglas de Negocio
│   ├── application/                            # Casos de Uso, Puertos y DTOs
│   ├── infrastructure/                         # Adaptadores de DB, repositorios y clientes externos
│   └── presentation/                           # Componentes visuales, vistas y controladores
│
├── tests/                                      # Suite de pruebas automatizadas
│   ├── unit/                                   # Pruebas unitarias de dominio y aplicación
│   └── acceptance/                             # Step definitions BDD y pruebas de integración
│
├── .git/hooks/
│   └── pre-commit                              # Hook Git nativo que dispara harness/init.ps1
│
├── .gitattributes                              # Normalización universal de saltos de línea (LF/CRLF)
├── .gitignore                                  # Exclusiones estándar para entornos de desarrollo
├── AGENTS.md                                   # Directivas operativas y reglas para agentes en Windows
├── anti-gravity.md                             # Protocolos de interacción específicos de Antigravity IDE
├── feature_list.json                           # Base de datos central del backlog con DAG y hashes
└── CHECKPOINTS.md                              # Libro contable de auditorías humanas inmutables
```

---

## 3. Descripción Meticulosa de Cada Artefacto y Archivo

### 3.1. Artefactos de la Raíz del Proyecto

#### `feature_list.json`

Base de datos declarativa del backlog del proyecto. Es leída y modificada de forma segura por `harness/sdd.ps1`.

- **Estructura JSON**:

  ```json
  [
    {
      "id": "FEAT-002",
      "name": "Servicio de Facturación",
      "status": "in_progress",
      "feature_dir": "FEAT-002",
      "depends_on": ["FEAT-001"],
      "created_at": "2026-10-26T18:00:00Z",
      "approval_hash": "A3F0F5DC51A3CBAF1B9479492B0A44888048C2BD10993574640A85F8E0B86294",
      "approval_history": [
        {
          "approval_hash": "A3F0F5DC51A3CBAF1B9479492B0A44888048C2BD10993574640A85F8E0B86294",
          "approved_at": "2026-10-26T18:05:00Z",
          "reason": "Aprobación inicial de arquitectura"
        }
      ],
      "completion_hash": "B31CACC992D32E6EFF8E6A9BFA6994F706BD01D02C0F2B371D7E3A700845F56D",
      "completed_at": "2026-10-26T19:00:00Z"
    }
  ]
  ```

- **Campos Principales**:
  - `id`: Identificador canónico (`FEAT-xxx`).
  - `status`: Estados permitidos: `pending`, `spec_ready`, `in_progress`, `done`.
  - `depends_on`: Arreglo de IDs de las funcionalidades prerrequisito que deben estar en estado `done`.
  - `approval_hash`: Hash SHA-256 de `spec.md` al momento de la autorización humana.
  - `approval_history`: Arreglo inmutable con el historial cronológico de aprobaciones, hashes y motivos (`-Reason`).
  - `completion_hash`: Hash SHA-256 generado al sellar la funcionalidad con `spec-gate.ps1` y emitir la matriz de trazabilidad.

#### `CHECKPOINTS.md`

Bitácora humana de auditoría. Cada vez que se aprueba o se completa una funcionalidad, `harness/sdd.ps1` adjunta una fila con la marca temporal ISO 8601, el identificador, la acción, el hash y el motivo.

#### `.gitattributes`

Configuración que fuerza la normalización universal de saltos de línea para evitar diferencias en el cómputo de hashes entre sistemas operativos:

```gitattributes
* text=auto eol=lf
*.ps1 text eol=crlf
*.bat text eol=crlf
```

#### `AGENTS.md` y `anti-gravity.md`

Contratos operativos que instruyen al LLM sobre cómo desenvolverse en el proyecto:

- Reglas estrictas de ejecución de PowerShell en Windows (`-NoProfile -ExecutionPolicy Bypass`).
- Prohibición de editar código sin aprobación formal previa.
- Obligación de consultar las skills especializadas en `.agent/skills/`.

---

### 3.2. Integración Nativa con Antigravity IDE (`.agents/hooks.json` y `harness/hooks/`)

SDD v5.4 implementa la API de ganchos (*Hooks API*) nativa de Google Antigravity IDE mediante el descriptor `.agents/hooks.json`.

```json
{
  "sdd-governance": {
    "SessionStart": [
      {
        "type": "command",
        "command": "powershell.exe -ExecutionPolicy Bypass -File ./harness/hooks/session-start.ps1",
        "timeout": 15
      }
    ],
    "PreToolUse": [
      {
        "matcher": "write_file|edit_file",
        "hooks": [
          {
            "type": "command",
            "command": "powershell.exe -ExecutionPolicy Bypass -File ./harness/hooks/pre-tool-enforce.ps1",
            "timeout": 15
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "write_file|edit_file",
        "hooks": [
          {
            "type": "command",
            "command": "powershell.exe -ExecutionPolicy Bypass -File ./harness/hooks/post-tool-check.ps1",
            "timeout": 15
          }
        ]
      }
    ]
  }
}
```

#### `harness/hooks/session-start.ps1`

Se dispara al inicio de cada sesión del agente. Valida:

1. Existencia y contenido de `feature_list.json` y `.specify/memory/onboard-state.json`, así como detección automática de código heredado en `src/` (*Brownfield*).
2. Si el backlog está vacío (`[]`) o `onboard-state.json` tiene `completed: false`, inyecta automáticamente un `systemMessage` para iniciar (o reanudar exactamente en la fase guardada `current_phase`) la **Entrevista Adaptativa SDD 2.0** con `sdd-onboard`.
3. Notifica al agente cuál es la funcionalidad activa y su estado actual.

#### `harness/hooks/pre-tool-enforce.ps1` (Interceptor Físico)

Se invoca en tiempo real antes de que el agente ejecute cualquier herramienta de escritura o edición (`write_file`, `edit_file`).

- **Inspección de Argumentos**: Lee el JSON de entrada enviado por el IDE a través de `stdin`.
- **Regla 1 (Candado SHA-256)**: Si el archivo objetivo pertenece a `src/`, verifica que la funcionalidad activa tenga `status: "in_progress"` y que el hash actual de `spec.md` + `scenarios.feature` coincida exactamente con `approval_hash`. Si no coincide o no está aprobada, emite:

  ```json
  {"decision": "deny", "reason": "[SDD GOBIERNO VIOLADO]: No hay ninguna funcionalidad en estado 'in_progress' aprobada con candado criptografico..."}
  ```

- **Regla 2 (Grafo de Dependencias `depends_on`)**: Verifica que todas las funcionalidades listadas en `depends_on` estén en estado `"done"`. Si alguna no lo está, bloquea la acción.
- **Regla 3 (Allowed Files)**: Si el archivo en `src/` no está explícitamente listado en la sección `## 5. Allowed Files` del `spec.md`, rechaza la edición por *Spec Drift*.

#### `harness/hooks/post-tool-check.ps1`

Se dispara inmediatamente después de la edición de un archivo. Inspecciona con expresiones regulares políglotas que `src/domain/` y `src/application/` no importen librerías de infraestructura o presentación, y que `src/presentation/` no sufra acoplamiento inverso hacia `src/infrastructure/`, registrando alertas en `progress/arch_alerts.log`.

---

### 3.3. Las 15 Skills Canónicas de Antigravity (`.agents/skills/`)

Cada habilidad reside en su propio subdirectorio con un archivo `SKILL.md` (y un alias `.md` de compatibilidad) que incluye frontmatter estándar de Antigravity:

| Skill | Directorio | Propósito Operativo |
| :--- | :--- | :--- |
| **`sdd-orchestrator`** | `.agents/skills/sdd-orchestrator/` | Controlador principal de flujo; guía al agente a través de las fases del ciclo de vida. |
| **`sdd-onboard`** | `.agents/skills/sdd-onboard/` | Entrevista Adaptativa SDD 2.0 en 5 fases (usa `ask_question`, ramificación *headless*, vista previa WCAG en vivo, propuesta de Mapa DAG `depends_on`, co-diseño proactivo EARS y persistencia en `onboard-state.json`). |
| **`sdd-constitution`** | `.agents/skills/sdd-constitution/` | Define y salvaguarda las leyes inmutables del proyecto en `.specify/memory/constitution.md`. |
| **`sdd-specify`** | `.agents/skills/sdd-specify/` | Redacta `spec.md` con sintaxis formal EARS y escenarios BDD `scenarios.feature`. |
| **`sdd-clarify`** | `.agents/skills/sdd-clarify/` | Ejecuta análisis adversarial de requerimientos para erradicar supuestos y ambigüedades. |
| **`sdd-ui-ux`** | `.agents/skills/sdd-ui-ux/` | Inteligencia de Diseño UI/UX Pro Max adaptada a SDD (5 estados, WCAG 2.1 AA, tokens). |
| **`sdd-design-system`**| `.agents/skills/sdd-design-system/` | Administra la paleta, tipografía, espaciados y tokens en `.specify/design-system/design-tokens.json`. |
| **`sdd-preview-design`**| `.agents/skills/sdd-preview-design/` | Genera vistas HTML interactivas para previsualizar componentes UI y verificar contraste WCAG. |
| **`sdd-plan`** | `.agents/skills/sdd-plan/` | Redacta `plan.md` definiendo capas de Clean Architecture, dependencias autorizadas y tokens. |
| **`sdd-tasks`** | `.agents/skills/sdd-tasks/` | Desglosa la implementación en una lista de tareas TDD atómicas ordenadas por capas. |
| **`sdd-implement`** | `.agents/skills/sdd-implement/` | Guía el ciclo Double-Loop TDD/BDD (Rojo -> Verde -> Refactor) dentro de `src/`. |
| **`sdd-user-guide`** | `.agents/skills/sdd-user-guide/` | Redacta la documentación de usuario obligatoria con 4 secciones estructurales completas. |
| **`sdd-validate`** | `.agents/skills/sdd-validate/` | Invoca de forma previa `harness/spec-gate.ps1` para diagnosticar los 7 comprobadores. |
| **`sdd-change-spec`** | `.agents/skills/sdd-change-spec/` | Control formal de modificaciones; fuerza nueva aprobación humana y registra `approval_history`. |
| **`sdd-reverse-spec`** | `.agents/skills/sdd-reverse-spec/` | Diseñada para proyectos brownfield; reconstruye specs formales a partir de código preexistente. |

---

### 3.4. Memoria y Plantillas Maestras (`.specify/`)

- **`.specify/memory/constitution.md`**: Reglas no negociables de la organización: cobertura mínima de tests, estándares de estilo, política de dependencias cero y arquitectura base.
- **`.specify/design-system/design-tokens.json`**: Fuente única de verdad visual:
  - `archetype`: Arquetipo de diseño (ej. "Corporate Clean", "Cyberpunk Modern").
  - `color_palette`: Hexadecimales de fondo, superficie, texto primario/secundario, acciones primarias, contraste y bordes.
  - `typography`: Familias tipográficas y escalas modulares.
  - `components`: Especificación de componentes con sus 5 estados obligatorios (`default`, `hover`, `focus`, `active`, `disabled`).
- **`.specify/harness-config.json`**: Configuración técnica políglota para el harness:
  - Extensiones de archivo (`.py`, `.ts`, `.go`, `.cs`, `.rs`).
  - Directorios de código fuente y tests.
  - Comandos de linter/análisis estático y motor de pruebas.

---

### 3.5. Núcleo de Gobernanza y Scripts (`harness/`)

#### `harness/sdd.ps1` (El CLI Orquestador)

Es la herramienta de control por línea de comandos para humanos y agentes. Comandos principales:

- `sdd.ps1 -Action list`: Muestra la tabla del backlog con estados, dependencias y hashes.
- `sdd.ps1 -Action create -FeatureId <id> -FeatureName <nombre> [-DependsOn "FEAT-001,FEAT-002"]`: Inicializa los directorios y plantillas en `specs/<id>/`.
- `sdd.ps1 -Action set-active -FeatureId <id>`: Define la funcionalidad activa en el contexto.
- `sdd.ps1 -Action approve -FeatureId <id> [-Reason <motivo>] [-Force]`:
  - **Inspección de Dependencias**: Valida que todas las dependencias en `depends_on` estén en estado `"done"`. Si no, emite un error y aborta.
  - **Cálculo Criptográfico**: Computa el SHA-256 de `spec.md`.
  - **Actualización de Historial**: Almacena el hash en `approval_hash` e inserta una nueva entrada en `approval_history` con fecha ISO y motivo.
  - **Transición de Estado**: Cambia `status` de `spec_ready` a `in_progress`.
- `sdd.ps1 -Action complete -FeatureId <id>`:
  - Ejecuta la auditoría exhaustiva de `harness/spec-gate.ps1`.
  - Si los 7 comprobadores pasan, genera la **Matriz de Trazabilidad Bidireccional** en `docs/traceability_<id>.md`.
  - Calcula el `completion_hash` sellando el código y la documentación.
  - Cambia `status` a `"done"` y actualiza `CHECKPOINTS.md`.

#### `harness/init.ps1` (El Guardián de Salud)

- Valida la integridad del repositorio y ejecuta dinámicamente el análisis estático (`mypy`, `tsc`, `go vet`, `dotnet build`, `cargo check`) y la suite de pruebas automatizadas (`pytest`, `npm test`, `go test`, `dotnet test`, `cargo test`).
- Es invocado automáticamente por el hook Git `pre-commit` y por el Check 5 de `spec-gate.ps1`.

---

## 4. Los 7 Comprobadores del Auditor Séptuple (`spec-gate.ps1`)

El script `harness/spec-gate.ps1` actúa como compuerta de calidad insalvable (*Quality Gate*) antes de permitir el cierre de cualquier funcionalidad.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                      AUDITOR SÉPTUPLE (spec-gate.ps1)                  │
├────────────────────────────────────────────────────────────────────────┤
│ Check 1: Allowed Files & Spec Drift (Workspace + Git History)          │
│ Check 2: Clean Architecture Políglota (Límites de Capas Estrictos)     │
│ Check 3: Lista Blanca de Dependencias (100% autorizadas en plan.md)    │
│ Check 4: Cobertura BDD EARS -> Gherkin (Mapeo exacto 1:1)              │
│ Check 5: Trazabilidad y Anti-Fake Tests (Aserciones y Suite en Verde)  │
│ Check 6: Guía de Usuario Exhaustiva (4 Secciones y Cero Placeholders)  │
│ Check 7: UI/UX Pro Max (WCAG 2.1 AA Luminancia, 5 Estados, Sin Hex)    │
└────────────────────────────────────────────────────────────────────────┘
```

### Check 1: Allowed Files & Spec Drift Prevention

- **Doble Inspección**:
  1. Examina el espacio de trabajo actual: los archivos en `src/` deben coincidir estrictamente con los declarados en `## 5. Allowed Files` de `spec.md`.
  2. Examina el historial de commits mediante `git log`: detecta si en commits anteriores de la feature se introdujeron o eliminaron archivos fuera de la lista permitida.

### Check 2: Fronteras de Clean Architecture Políglota

- Analiza las importaciones en todo el árbol de `src/` según el stack configurado:
  - **Dominio (`src/domain/`)**: Debe ser completamente agnóstico. Prohibido importar de `application`, `infrastructure` o `presentation`.
  - **Aplicación (`src/application/`)**: Contiene orquestación y casos de uso. Prohibido importar de `infrastructure` o `presentation`.
  - **Presentación (`src/presentation/`)**: Componentes visuales y controladores. Prohibido importar directamente de `infrastructure` (debe comunicarse a través de interfaces/puertos en `application` o `domain`).
- Compatible con sintaxis: `import`/`from` (Python), `import`/`require` (TypeScript), `import` (Go), `using` (C#), `use` (Rust).

### Check 3: Lista Blanca de Dependencias Autorizadas

- Extrae la lista declarada en la sección `## 4. Allowed Dependencies` de `plan.md`.
- Escanea todos los archivos de implementación y verifica que ninguna librería externa o paquete de terceros sea utilizado a menos que esté formalmente autorizado en el plan.

### Check 4: Cobertura BDD EARS a Gherkin

- Lee los criterios de aceptación EARS en `spec.md` (`### AC-x.x: ...`).
- Verifica que en `scenarios.feature` exista exactamente un escenario Gherkin decorado con la etiqueta correspondiente (`@AC-x.x`).
- Prohíbe divergencias, criterios huérfanos o escenarios sin respaldo formal.

### Check 5: Trazabilidad y Anti-Fake Tests

- **Inspección Estática**: Busca que cada criterio `AC-x.x` tenga su correspondiente función de prueba en `tests/` y analiza el cuerpo de la función verificando que contenga aserciones legítimas (`assert`, `expect`, `should`, `Assert.`, etc.). Rechaza pruebas vacías con `pass` o pruebas ficticias (*fake tests*).
- **Ejecución Dinámica**: Ejecuta `harness/init.ps1`. Si el linter falla o si algún test resulta en rojo, el Check 5 es rechazado.

### Check 6: Guía de Usuario Exhaustiva (Novedad v5.4)

- Localiza `docs/user_guide_<feature>.md`.
- **4 Secciones Estructurales Obligatorias**:
  1. `## 1. Propósito`
  2. `## 2. Requisitos Previos`
  3. `## 3. Guía Paso a Paso`
  4. `## 4. Solución de Problemas`
- **Cero Placeholders Residuales**: Escanea el documento con la expresión regular `\{[A-Z0-9_\-\s]{2,}\}`. Si detecta etiquetas de plantilla sin rellenar (como `{ERROR_COMUN}`, `{Paso 1}` o `{PARAMETRO}`), bloquea la aprobación de la auditoría.

### Check 7: UI/UX Pro Max y Verificación Matemática de Diseño

- Aplica si existen componentes en `src/presentation/` o si `plan.md` define diseño visual:
  1. **Cobertura de Tokens**: Valida la presencia de `tokens.archetype`, `tokens.color_palette.primary_action`, etc.
  2. **Contraste de Luminancia Relativa WCAG 2.1 AA**:
     Calcula la luminancia relativa de cada color:
     $$L = 0.2126 \times R + 0.7152 \times G + 0.0722 \times B$$
     Donde cada canal sRGB normalizado $C \in \{R, G, B\}$ se ajusta según:
     $$C = \begin{cases} \frac{C_{\text{srgb}}}{12.92} & \text{si } C_{\text{srgb}} \le 0.04045 \\ \left(\frac{C_{\text{srgb}} + 0.055}{1.055}\right)^{2.4} & \text{en caso contrario} \end{cases}$$
     Evalúa que el ratio entre el color de acción/texto y el fondo cumpla:
     $$\text{Ratio} = \frac{L_1 + 0.05}{L_2 + 0.05} \ge 4.5:1$$

  3. **5 Estados Obligatorios**: Todo componente interactivo debe tener definidos sus estados `default`, `hover`, `focus`, `active` y `disabled`.
  4. **Cero Magic Hex Codes**: Escanea `src/presentation/` buscando valores hexadecimales (`#[0-9a-fA-F]{3,8}`). Cualquier color que no provenga de `design-tokens.json` o variables CSS tokenizadas es rechazado.

---

## 5. Gobernanza del Backlog, Trazabilidad y Criptografía

### Grafo de Dependencias (`depends_on`)

El desarrollo desordenado donde los agentes implementan pantallas o servicios antes de que la capa de datos o el núcleo esté listo queda erradicado.

- Cada funcionalidad en `feature_list.json` puede declarar: `"depends_on": ["FEAT-001", "FEAT-002"]`.
- Al invocar `sdd.ps1 -Action approve`, el sistema comprueba que cada dependencia esté en estado `"done"`. Si alguna no lo está, la aprobación humana se detiene.
- De forma análoga, el gancho `harness/hooks/pre-tool-enforce.ps1` impide que el agente modifique archivos en `src/` para una funcionalidad si sus prerrequisitos no han sido cerrados formalmente.

### Inmutabilidad de Cambios y `approval_history`

Cuando una especificación aprobada requiere ajustes debido a nuevos descubrimientos:

1. Se utiliza la skill `sdd-change-spec`.
2. Se modifica `spec.md`. En este instante, el `approval_hash` almacenado deja de coincidir con el archivo, bloqueando inmediatamente la edición de `src/`.
3. El operador humano revisa los cambios y re-aprueba con un motivo explícito:

   ```powershell
   powershell -ExecutionPolicy Bypass -Command ".\harness\sdd.ps1 -Action approve -FeatureId FEAT-002 -Reason 'Ajuste en Criterio AC-1.2 por cambio en API externa' -Force"
   ```

4. `feature_list.json` registra la nueva entrada en `approval_history`, conservando la auditoría completa e histórica de quién autorizó el cambio, cuándo y por qué.

### Matriz de Trazabilidad Bidireccional (`docs/traceability_<feature>.md`)

Al completarse la funcionalidad mediante `sdd.ps1 -Action complete`, se compila automáticamente una matriz en Markdown que consolida toda la cadena de valor:

```markdown
# Matriz de Trazabilidad Bidireccional: [FEAT-002] Servicio de Facturación

> **Generado automáticamente por SDD v5.4 al completar formalmente la funcionalidad.**
- **Fecha de Cierre**: 2026-10-26T19:07:22Z
- **Approval SHA**: A3F0F5DC51A3CBAF1B9479492B0A44888048C2BD10993574640A85F8E0B86294
- **Completion SHA**: B31CACC992D32E6EFF8E6A9BFA6994F706BD01D02C0F2B371D7E3A700845F56D

| Criterio EARS | Escenario Gherkin | Test Automatizado | Archivos de Implementacion | Documentacion de Usuario |
| :--- | :--- | :--- | :--- | :--- |
| `AC-1.1 (Cálculo IVA)` | `@AC-1.1` | `test_tax.py::test_ac_1_1_calc` | `src/domain/tax.py` | [user_guide_FEAT-002.md](user_guide_FEAT-002.md) |
| `AC-1.2 (Emisión Factura)` | `@AC-1.2` | `test_invoice.py::test_ac_1_2_emit` | `src/application/invoice.py` | [user_guide_FEAT-002.md](user_guide_FEAT-002.md) |
```

---

## 6. Guía de Uso del CLI y Comandos Operativos

Todos los comandos se ejecutan a través de PowerShell con bypass de directivas:

```powershell
# 1. Consultar el estado general del backlog y dependencias
powershell -NoProfile -ExecutionPolicy Bypass -File .\harness\sdd.ps1 -Action list

# 2. Crear una nueva funcionalidad con dependencias explícitas
powershell -NoProfile -ExecutionPolicy Bypass -File .\harness\sdd.ps1 -Action create -FeatureId FEAT-003 -FeatureName "Pasarela de Pagos" -DependsOn "FEAT-001,FEAT-002"

# 3. Activar una funcionalidad en el espacio de trabajo
powershell -NoProfile -ExecutionPolicy Bypass -File .\harness\sdd.ps1 -Action set-active -FeatureId FEAT-003

# 4. Aprobar la especificación (Candado Criptográfico Humano con motivo)
powershell -NoProfile -ExecutionPolicy Bypass -File .\harness\sdd.ps1 -Action approve -FeatureId FEAT-003 -Reason "Aprobación de arquitectura y contratos EARS"

# 5. Ejecutar la suite de salud y verificación estática/dinámica
powershell -NoProfile -ExecutionPolicy Bypass -File .\harness\init.ps1

# 6. Auditar la funcionalidad con el Auditor Séptuple
powershell -NoProfile -ExecutionPolicy Bypass -File .\harness\spec-gate.ps1 -FeatureId FEAT-003

# 7. Sellar y completar formalmente la funcionalidad (Genera Matriz de Trazabilidad)
powershell -NoProfile -ExecutionPolicy Bypass -File .\harness\sdd.ps1 -Action complete -FeatureId FEAT-003
```

---

## 7. Flujo de Trabajo Operativo Paso a Paso (End-to-End)

El siguiente diagrama ilustra la secuencia operativa formal desde el requerimiento en bruto hasta el despliegue verificado:

```text
[FASE 0: Onboarding] ──> sdd-onboard (Entrevista Socrática)
       │
       ▼
[FASE 1: Especificar] ──> sdd-specify (spec.md EARS + scenarios.feature Gherkin)
       │
       ▼
[FASE 2: Planificar] ──> sdd-plan & sdd-tasks (Clean Arch + Allowed Files + Design Tokens)
       │
       ▼
[FASE 3: Candado] ────> sdd.ps1 -Action approve -Reason "..." (HUMANO: SHA-256 Checkpoint)
       │
       ▼
[FASE 4: Desarrollar] ──> sdd-implement (Double Loop TDD en src/ bajo PreToolUse Hook)
       │
       ▼
[FASE 5: Documentar] ──> sdd-user-guide (docs/user_guide_<id>.md: 4 secciones y 0 placeholders)
       │
       ▼
[FASE 6: Auditar] ────> harness/spec-gate.ps1 (Auditor Séptuple: Checks 1 al 7)
       │
       ▼
[FASE 7: Completar] ───> sdd.ps1 -Action complete (Matriz de Trazabilidad + Sello SHA)
```

---

## 8. Matriz de Configuración Políglota de Stacks

| Preset / Parámetro Stack | Lenguaje | Extensiones | Linter / Análisis Estático | Motor de Pruebas BDD / Unitarias |
| :--- | :--- | :--- | :--- | :--- |
| `python` / `python-pytest` (Default) | Python 3.10+ | `.py` | `python -m mypy src --ignore-missing-imports` | `python -m pytest -q tests` |
| `typescript` / `ts-vitest` | TypeScript / Node | `.ts`, `.tsx` | `npx tsc --noEmit` | `npx vitest run` |
| `dotnet` / `dotnet-xunit` | C# .NET 8.0+ | `.cs` | `dotnet build --no-incremental` | `dotnet test` |
| `go` / `go-test` | Go 1.20+ | `.go` | `go vet ./...` | `go test ./...` |
| `flutter` / `flutter-test` | Flutter / Dart | `.dart` | `dart analyze` | `flutter test` |
| `rust` / `rust-cargo` | Rust 2021 | `.rs` | `cargo check` | `cargo test` |

Para inicializar un proyecto en cualquiera de estos stacks y activar el auto-lanzamiento inteligente de la entrevista:

```powershell
# Inicialización con auto-lanzamiento híbrido automático (abre Antigravity IDE o agy)
powershell -NoProfile -ExecutionPolicy Bypass -File .\setup-sdd-project-v54.ps1 -ProjectName "MiPlataforma" -Stack typescript -GitInit

# Inicialización forzando apertura en Antigravity IDE
powershell -NoProfile -ExecutionPolicy Bypass -File .\setup-sdd-project-v54.ps1 -ProjectName "MiPlataforma" -AutoLaunch ide

# Inicialización forzando entrevista en la misma terminal con la CLI agy
powershell -NoProfile -ExecutionPolicy Bypass -File .\setup-sdd-project-v54.ps1 -ProjectName "MiPlataforma" -AutoLaunch cli

# Inicialización sin auto-lanzamiento (ideal para scripts desatendidos o CI/CD)
powershell -NoProfile -ExecutionPolicy Bypass -File .\setup-sdd-project-v54.ps1 -ProjectName "MiPlataforma" -NoAutoLaunch
```

---

## 9. Conclusión y Garantías de Calidad

Con la culminación de **Setup SDD v5.4**, el ecosistema de desarrollo guiado por especificaciones alcanza su madurez arquitectónica plena. Las 20 mejoras estructuradas a lo largo de las versiones v5.0 a v5.4 garantizan:

1. **Cero Alucinaciones en Código**: Los archivos de código sólo pueden crearse si están pre-autorizados en la especificación formal.
2. **Cero Código Roto en Producción**: Las pruebas automatizadas genuinas y los linters se validan antes de cada commit y en el cierre de la funcionalidad.
3. **Cero Desacoplamiento Arquitectónico**: Las fronteras de Clean Architecture son verificadas algorítmicamente en cada lenguaje.
4. **Cero Deuda de Documentación**: La guía de usuario con 4 secciones y la matriz de trazabilidad bidireccional son requisitos obligatorios para poder cerrar cualquier entrega.
5. **Control Total del Operador Humano**: El agente de IA actúa con absoluta autonomía técnica dentro del área delimitada por los candados criptográficos, pero la dirección y la aprobación formal permanecen siempre en manos humanas.
