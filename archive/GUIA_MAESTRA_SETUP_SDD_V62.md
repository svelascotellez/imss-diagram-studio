# Guía Maestra Definitiva: Arquitectura, Artefactos y Gobierno de Setup SDD (v6.2)

## Enterprise Security, CI/CD Governance & Interactive Dashboard Edition: Spec-Driven Development + BDD + Clean Architecture + Secure Coding + DAG Viewer + Cloud PR Gates

---

## 1. Introducción y Fundamentos Metodológicos

El framework **Setup SDD (Specification-Driven Development v6.2 Enterprise Security, CI/CD Governance & Interactive Dashboard Edition)** es una infraestructura integral de ingeniería de software diseñada para gobernar el ciclo de vida del desarrollo asistido por Inteligencia Artificial (IA) en entornos profesionales, de nube y de misión crítica.

Su premisa rectora inquebrantable es:

> **"Ninguna línea de código de producción puede existir sin una especificación formal aprobada, verificable criptográficamente, blindada contra vulnerabilidades OWASP, visualizable en el grafo DAG, validada en pipelines de CI/CD y sellada por un humano."**

### Los 8 Pilares de SDD v6.2

```text
+----------------------------------------------------------------------------------------------------+
|                                    LOS 8 PILARES DE SDD v6.2                                       |
+----------------------------------------------------------------------------------------------------+
| 1. Spec-First (EARS)      : Especificaciones formales con disparadores y criterios deterministas.  |
| 2. BDD Bidireccional      : Escenarios Gherkin con correspondencia 1:1 con tests automatizados.   |
| 3. Clean Architecture     : Dominio puro, Regla de Dependencias absoluta y cero fugas de framework|
| 4. Candado Criptográfico  : Firmas SHA-256 obligatorias de Aprobación y Cierre en CHECKPOINTS.md.  |
| 5. UI/UX Pro Max          : Design System First, tokens contrastados WCAG 2.1 AA y preview HTML.   |
| 6. Secure Coding & OWASP  : STRIDE PR-sized, sanitización de sinks, escaneo SAST y cero secretos. |
| 7. Observabilidad & DAG   : Panel interactivo (SDD Web Dashboard) y Visor DAG en tiempo real.     |
| 8. Gobernanza en CI/CD    : Compuertas en la nube (GitHub Actions / GitLab CI) y PR summaries.    |
+----------------------------------------------------------------------------------------------------+
```

---

## 2. Mapa Completo del Árbol de Directorios y Archivos

Al ejecutar `setup-sdd-project-v62.ps1` o `setup-sdd-project-v62.py`, se despliega la siguiente topología de archivos y directorios:

```text
<directorio-del-proyecto>/
│
├── .github/                                # Integración Continua en GitHub
│   └── workflows/
│       └── sdd-gate.yml                    # Pipeline de gobernanza y auditoría en PRs
│
├── .gitlab-ci.yml                          # Pipeline de gobernanza para GitLab CI
│
├── .agents/                                # Gobernanza nativa de Antigravity IDE
│   ├── hooks.json                          # Configuración de hooks del ciclo de vida
│   └── skills/                             # 18 Skills Canónicas
│       ├── sdd-orchestrator/SKILL.md       # Orquestador del bucle SDD y CI/CD
│       ├── sdd-onboard/SKILL.md            # Entrevista adaptativa en 5 fases
│       ├── sdd-constitution/SKILL.md       # Gobernanza de la constitución
│       ├── sdd-specify/SKILL.md            # Redacción de spec.md (EARS)
│       ├── sdd-clarify/SKILL.md            # Detección y resolución de ambigüedades
│       ├── sdd-ui-ux/SKILL.md              # Diseño de interfaces y accesibilidad
│       ├── sdd-design-system/SKILL.md      # Tokens de diseño y 5 estados
│       ├── sdd-preview-design/SKILL.md     # Previsualizador HTML del Design System
│       ├── sdd-plan/SKILL.md               # Arquitectura limpia y STRIDE
│       ├── sdd-tasks/SKILL.md              # Desglose en tareas atómicas TDD
│       ├── sdd-implement/SKILL.md          # Implementación estricta en Allowed Files
│       ├── sdd-user-guide/SKILL.md         # Guía de usuario en 4 secciones
│       ├── sdd-validate/SKILL.md           # Validación de suite de tests y types
│       ├── sdd-change-spec/SKILL.md        # Control de cambios en especificaciones
│       ├── sdd-reverse-spec/SKILL.md       # Ingeniería inversa de código preexistente
│       ├── sdd-secure-coding/SKILL.md      # Threat modeling y auditoría OWASP
│       ├── sdd-dashboard/SKILL.md          # Panel interactivo y Visor DAG
│       └── sdd-cicd/SKILL.md               # Skill Canónica #18: Gobernanza CI/CD
│
├── .specify/                               # Artefactos de memoria y plantillas
│   ├── harness-config.json                 # Configuración del stack tecnológico
│   ├── memory/
│   │   ├── constitution.md                 # 10 Principios innegociables de gobierno
│   │   └── onboard-state.json              # Estado de la entrevista adaptativa
│   ├── design-system/
│   │   └── design-tokens.json              # Tokens de color, tipografía y contraste
│   └── templates/                          # Plantillas estructurales obligatorias
│       ├── spec.template.md                # Plantilla de especificación (5 secciones)
│       ├── plan.template.md                # Plantilla de plan (Clean Architecture)
│       ├── tasks.template.md               # Plantilla de tareas atómicas
│       ├── user_guide.template.md          # Plantilla de guía de usuario
│       └── impl_report.template.md         # Plantilla de reporte de implementación
│
├── harness/                                # Arnés de verificación y automatización
│   ├── init.ps1                            # Inicializador y validador de entorno
│   ├── sdd.ps1                             # CLI unificada de gestión del backlog
│   ├── spec-gate.ps1                       # Auditor Óctuple reforzado (8 Hard Gates)
│   ├── verify-security.ps1                 # Auditoría de seguridad SAST y secretos
│   ├── preview-design.ps1                  # Previsualizador HTML del Design System
│   ├── dashboard.ps1                       # Generador del Dashboard Web y Visor DAG
│   ├── pr-summary.ps1                      # Generador del resumen de Pull Request
│   └── hooks/                              # Scripts ejecutados por hooks
│       ├── session-start.ps1               # Hook al iniciar sesión de chat
│       └── pre-tool-enforce.ps1            # Hook de bloqueo físico en tiempo real
│
├── specs/                                  # Especificaciones por funcionalidad
│   └── <feature_id>/                       # Carpeta aislada de la funcionalidad
│       ├── spec.md                         # Especificación funcional EARS
│       ├── scenarios.feature               # Escenarios BDD/Gherkin
│       ├── plan.md                         # Plan de arquitectura y STRIDE
│       └── tasks.md                        # Desglose de tareas TDD
│
├── docs/                                   # Documentación técnica y de usuario
│   ├── user_guide_<feature>.md             # Guía de usuario generada
│   └── traceability_<feature>.md           # Matriz de trazabilidad bidireccional
│
├── progress/                               # Artefactos visuales y de CI
│   ├── design_system_preview.html          # Previsualización del Design System
│   ├── sdd_dashboard.html                  # Panel Visual Interactivo y Visor DAG
│   └── pr_summary.md                       # Resumen visual para Pull Requests
│
├── src/                                    # Código de producción (Clean Architecture)
│   ├── domain/                             # Entidades y reglas de negocio puras
│   ├── application/                        # Casos de uso y puertos
│   ├── infrastructure/                     # Adaptadores externos, repositorios, APIs
│   └── presentation/                       # Controladores, vistas, CLI
│
├── tests/                                  # Batería de pruebas automatizadas
│   ├── unit/                               # Pruebas unitarias de dominio y casos de uso
│   └── acceptance/                         # Pruebas de aceptación BDD (Gherkin)
│
├── feature_list.json                       # Registro del backlog y candados SHA-256
├── CHECKPOINTS.md                          # Registro inmutable de checkpoints
├── README.md                               # Documentación principal del proyecto
├── CLAUDE.md                               # Directrices operativas para asistentes
├── AGENTS.md                               # Instrucciones de ejecución para agentes
└── anti-gravity.md                         # Configuración de compatibilidad Antigravity
```

---

## 3. Extensión de Gobernanza a CI/CD (GitHub Actions y GitLab CI)

La versión 6.2 resuelve la necesidad de garantizar que el código desarrollado no solo cumpla localmente, sino que sea evaluado de manera independiente en la nube antes de cualquier fusión (*merge*).

### 3.1. Arquitectura del Pipeline de Integración Continua

El flujo de trabajo en CI/CD ejecuta 6 etapas rigurosas:

1. **Higiene Markdown (Linting)**: Escanea el repositorio para verificar el estricto cumplimiento de las reglas MD009 a MD058.
2. **Auditoría de Seguridad y Secretos**: Ejecuta `harness/verify-security.ps1` detectando secretos expuestos, llaves privadas y vulnerabilidades SAST críticas.
3. **Ejecución de Pruebas Unitarias y de Tipos**: Corre la batería de tests y comprobación de tipos definida en `.specify/harness-config.json`.
4. **Evaluación de las 8 Compuertas del Auditor Óctuple**: Ejecuta `harness/spec-gate.ps1` sobre cada funcionalidad activa o modificada en el PR.
5. **Generación del Resumen de Pull Request**: Ejecuta `harness/pr-summary.ps1` generando `progress/pr_summary.md` y vinculándolo al resumen del runner (`$GITHUB_STEP_SUMMARY`).
6. **Compilación y Publicación del Dashboard**: Genera `progress/sdd_dashboard.html` y lo publica como artefacto del pipeline o en GitHub Pages / GitLab Pages.

### 3.2. Configuración en GitHub Actions (`.github/workflows/sdd-gate.yml`)

El pipeline se activa automáticamente en:

- Creación o actualización de Pull Requests hacia ramas principales (`main`, `master`, `develop`).
- Pushes directos a ramas protegidas.
- Ejecución manual mediante `workflow_dispatch`.

---

## 4. Los 8 Comprobadores del Auditor Óctuple (`harness/spec-gate.ps1`)

El script `harness/spec-gate.ps1` es la aduana de control más estricta del framework. Se ejecuta tanto en local como en los runners de CI:

```text
+--------+------------------------------------+-----------------------------------------------------+
| Aduana | Nombre del Gate                    | Condición de Aprobación                             |
+--------+------------------------------------+-----------------------------------------------------+
| Gate 1 | Spec Drift & Git Enforcement       | Cero archivos modificados fuera de 'Allowed Files'. |
| Gate 2 | BDD 1:1 Coverage                   | 100% de escenarios Gherkin tienen tests vinculados. |
| Gate 3 | Clean Architecture Imports         | Dominio puro sin dependencias de infraestructura.   |
| Gate 4 | Candado Criptográfico SHA-256      | Hash de especificación intacto y no alterado.       |
| Gate 5 | Anti-Fake Tests                    | Tests con aserciones reales (prohibido 'pass/true').|
| Gate 6 | Guía de Usuario en 4 Secciones     | Documento 'docs/user_guide_<feat>.md' completado.   |
| Gate 7 | UI/UX Pro Max WCAG 2.1 AA          | Tokens de color con ratio de contraste >= 4.5:1.    |
| Gate 8 | Secure Coding & OWASP Compliance   | Cero secretos expuestos, sinks seguros y SAST OK.   |
+--------+------------------------------------+-----------------------------------------------------+
```

---

## 5. El Panel Visual Interactivo y Visor DAG (`harness/dashboard.ps1`)

El dashboard web autónomo (`progress/sdd_dashboard.html`) proporciona un centro de comando visual para desarrolladores, líderes técnicos y evaluadores en CI:

- **Grafo Acíclico Dirigido (DAG Viewer)**: Mapea las relaciones `depends_on` con Mermaid.js v10 y asigna colores WCAG 2.1 AA a cada nodo según su estado (`done`, `in_progress`, `spec_ready`, `pending`, `review`).
- **Métricas Ejecutivas**: Barra hero de avance porcentual, conteo de candados criptográficos y balance de estados.
- **Explorador Interactivo del Backlog**: Tabla viva con filtrado en tiempo real y botones para copiar comandos del arnés.
- **Publicación en CI/CD**: Integrado automáticamente en las acciones de GitHub y GitLab para descarga como artefacto de auditoría.

---

## 6. Comandos Operativos y CLI de Gobernanza (`harness/sdd.ps1`)

El arnés `harness/sdd.ps1` centraliza todas las operaciones del bucle de desarrollo:

| Comando | Acción | Descripción |
| :--- | :--- | :--- |
| `.\harness\sdd.ps1 -Action status` | `status` | Muestra el estado del backlog en terminal con colores y hashes. |
| `.\harness\sdd.ps1 -Action next` | `next` | Analiza el backlog y guía al siguiente paso lógico. |
| `.\harness\sdd.ps1 -Action dashboard` | `dashboard` | Genera y abre el Dashboard Web interactivo y Visor DAG. |
| `.\harness\sdd.ps1 -Action init-cicd` | `init-cicd` | Genera o actualiza los pipelines CI/CD (GitHub Actions y GitLab). |
| `.\harness\sdd.ps1 -Action pr-summary` | `pr-summary` | Genera el informe de gobernanza para Pull Request en Markdown. |
| `.\harness\sdd.ps1 -Action create -FeatureId <id> -FeatureName <nombre> -DependsOn <deps>` | `create` | Registra una nueva funcionalidad en el backlog con sus dependencias. |
| `.\harness\sdd.ps1 -Action set-active -FeatureId <id>` | `set-active` | Activa una funcionalidad y establece el candado de trabajo. |
| `.\harness\sdd.ps1 -Action approve -FeatureId <id> -Reason <motivo>` | `approve` | Sella el candado criptográfico SHA-256 de aprobación humana. |
| `.\harness\sdd.ps1 -Action verify-security` | `verify-security` | Ejecuta el escaneo SAST de seguridad, secretos y dependencias. |
| `.\harness\spec-gate.ps1 -FeatureId <id>` | `spec-gate` | Ejecuta la auditoría óctuple reforzada (8 Hard Gates). |
| `.\harness\sdd.ps1 -Action complete -FeatureId <id>` | `complete` | Valida el auditor óctuple, sella el candado de cierre y genera trazabilidad. |
| `.\harness\sdd.ps1 -Action fix-markdown` | `fix-markdown` | Escanea y autocorrige violaciones MD009 a MD058 en todos los `.md`. |
| `.\harness\sdd.ps1 -Action preview-design` | `preview-design` | Genera la previsualización HTML del Design System y WCAG. |
| `.\harness\sdd.ps1 -Action configure-stack -Stack <preset>` | `configure-stack` | Configura el preset tecnológico (Python, TypeScript, .NET, Go, Rust, Flutter). |

---

## 7. Cómo Inicializar un Proyecto con SDD v6.2

Para inicializar un nuevo proyecto empresarial gobernado por SDD v6.2:

### Inicialización en PowerShell

```powershell
.\setup-sdd-project-v62.ps1 -ProjectName "MiProyectoEmpresarial" -Stack "python" -GitInit
```

### Inicialización en Python

```bash
python setup-sdd-project-v62.py
```

### Parámetros Soportados

- `-ProjectName <nombre>`: Nombre de la carpeta del proyecto a crear.
- `-Stack <preset>`: Preset tecnológico inicial (`python`, `typescript`, `dotnet`, `go`, `flutter`, `rust`).
- `-GitInit`: Inicializa automáticamente el repositorio local de Git si no existe.
- `-AutoLaunch <modo>`: Modalidad de inicio automático (`auto`, `ide`, `cli`, `none`).

---

## 8. Higiene de Documentación y Reglas Markdownlint

Para garantizar que los documentos generados no generen advertencias en linters profesionales de CI/CD, todos los archivos cumplen rigurosamente con las siguientes 7 reglas:

- **MD009 (no-trailing-spaces)**: Cero espacios en blanco residuales al final de cualquier línea.
- **MD022 (blanks-around-headings)**: Exactamente una línea en blanco por encima y por debajo de cada encabezado Markdown.
- **MD031 (blanks-around-fences)**: Bloques de código cercados con triples acentos graves (` ``` `) rodeados por líneas en blanco.
- **MD032 (blanks-around-lists)**: Listas numeradas y no numeradas rodeadas por líneas en blanco antes y después.
- **MD040 (fenced-code-language)**: Idioma explícito especificado en cada bloque de código cercado.
- **MD047 (single-trailing-newline)**: Todos los archivos terminan exactamente con un único carácter de salto de línea.
- **MD058 (blanks-around-tables)**: Tablas Markdown rodeadas por líneas en blanco antes y después.
