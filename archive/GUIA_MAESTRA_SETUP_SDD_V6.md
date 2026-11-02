# Guía Maestra Definitiva: Arquitectura, Artefactos y Gobierno de Setup SDD (v6.0)

## Enterprise Security Edition: Spec-Driven Development + BDD + Clean Architecture + Secure Coding

---

## 1. Introducción y Fundamentos Metodológicos

El framework **Setup SDD (Specification-Driven Development v6.0 Enterprise Security Edition)** es una infraestructura integral de ingeniería de software diseñada para gobernar el ciclo de vida del desarrollo asistido por Inteligencia Artificial (IA) en entornos profesionales de misión crítica.

Su premisa rectora inquebrantable es:
**«Ninguna línea de código de producción puede existir sin una especificación formal aprobada, verificable criptográficamente, blindada contra vulnerabilidades OWASP y sellada por un humano.»**

### Los 6 Pilares de SDD v6.0

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                  SDD v6.0 PILARES                                      │
├────────────────────┬────────────────────┬────────────────────┬─────────────────────────┤
│ 1. Spec-First      │ 2. BDD Riguroso    │ 3. Clean Arch      │ 4. UI/UX Pro Max        │
│    & Anti-Drift    │    EARS/Gherkin    │    Políglota       │    WCAG 2.1 AA Mat.     │
├────────────────────┴────────────────────┼────────────────────┴─────────────────────────┤
│ 5. Criptografía HITL & Gobernanza DAG   │ 6. Secure Coding & OWASP Hard Gates (NUEVO) │
└─────────────────────────────────────────┴──────────────────────────────────────────────┘
```

1. **Spec-Driven Development (SDD) & Anti-Spec Drift:** Cada funcionalidad declara taxativamente `## 5. Allowed Files`. Cualquier modificación fuera de esta lista blanca bloquea físicamente la ejecución del agente.
2. **Behavior-Driven Development (BDD) Bidireccional:** Requisitos redactados bajo sintaxis **EARS** (`AC-x.x`) correlacionados 1:1 con escenarios **Gherkin** (`@AC-x.x`) y suites de test ejecutables.
3. **Clean Architecture Políglota Estricta:** Separación matemática de responsabilidades en cuatro capas concéntricas (`domain`, `application`, `infrastructure`, `presentation`), con soporte para Python, TypeScript, Go, C# .NET, Flutter/Dart y Rust.
4. **UI/UX Pro Max con Verificación Matemática:** Gobernanza formal del diseño vía `design-tokens.json`. Valida algorítmicamente el ratio de contraste de luminancia relativa **WCAG 2.1 AA** ($\ge 4.5:1$), exige los 5 estados obligatorios y erradica los *magic hex codes*.
5. **Criptografía Human-in-the-Loop y Gobernanza de Dependencias DAG:** Candado criptográfico **SHA-256** inmutable emitido exclusivamente por personas reales (`harness/sdd.ps1 -Action approve`), con grafo acíclico dirigido (`depends_on`) que previene iniciar tareas con dependencias inconclusas.
6. **Secure Coding & OWASP Hard Gates (Nuevo en v6.0):** Modelado de amenazas ligero **STRIDE** en `plan.md` (`## 5. Security & Threat Modeling`), detección de la *lethal trifecta*, control estricto de fronteras de confianza (`‖`), erradicación de secretos y credenciales en código, y compuerta dura de seguridad (Check 8 en `spec-gate.ps1`).

---

## 2. Mapa Completo del Árbol de Directorios y Archivos

Al inicializar un proyecto con `setup-sdd-project-v6.ps1` o `setup-sdd-project-v6.py`, se genera la siguiente topología de archivos:

```text
<RAÍZ_DEL_PROYECTO>/
│
├── .agents/                                    # Configuración de Hooks y Skills nativas del IDE
│   ├── hooks.json                              # Declaración de hooks SessionStart, PreToolUse y PostToolUse
│   └── skills/                                 # 16 Skills operativas canónicas
│       ├── sdd-orchestrator/SKILL.md           # Orquestador del ciclo de vida y navegación entre fases
│       ├── sdd-onboard/SKILL.md                # Entrevista guiada socrática adaptativa (SDD 2.0)
│       ├── sdd-constitution/SKILL.md           # Gestión de leyes inmutables de calidad y stack
│       ├── sdd-specify/SKILL.md                # Redacción de especificaciones EARS y Gherkin
│       ├── sdd-clarify/SKILL.md                # Auditoría adversarial de ambigüedades
│       ├── sdd-ui-ux/SKILL.md                  # Inteligencia de diseño UI/UX Pro Max y accesibilidad WCAG
│       ├── sdd-design-system/SKILL.md          # Tokens de diseño UI/UX y tokens semánticos
│       ├── sdd-preview-design/SKILL.md         # Previsualización y renderizado de componentes UI
│       ├── sdd-plan/SKILL.md                   # Plan técnico Clean Arch + STRIDE Security Modeling
│       ├── sdd-tasks/SKILL.md                  # Desglose en tareas atómicas TDD
│       ├── sdd-implement/SKILL.md              # Implementación Double-Loop TDD/BDD
│       ├── sdd-secure-coding/                  # [NUEVO v6.0] Skill de Seguridad Defensiva y OWASP
│       │   ├── SKILL.md                        # Directrices de revisión de seguridad y correcciones
│       │   └── references/                     # Guías canónicas por temática y stack
│       │       ├── threat-modeling.md          # STRIDE ligero en PRs y trust boundaries (‖)
│       │       ├── owasp-by-stack.md           # OWASP Top 10 para FastAPI, Next.js, Go y Flutter
│       │       ├── authn-authz.md              # Sesiones, JWT fijado, OAuth2 PKCE y RBAC
│       │       └── secrets-and-supply-chain.md # Gestión de secretos y auditoría de dependencias
│       ├── sdd-user-guide/SKILL.md             # Redacción de la Guía de Usuario en 4 secciones
│       ├── sdd-validate/SKILL.md               # Auditoría previa con el Auditor Óctuple
│       ├── sdd-change-spec/SKILL.md            # Gestión de cambios formales con versionado de hashes
│       └── sdd-reverse-spec/SKILL.md           # Ingeniería inversa brownfield para código heredado
│
├── .specify/                                   # Memoria, tokens y plantillas maestras
│   ├── memory/
│   │   ├── constitution.md                     # Constitución inmutable: 11 leyes arquitectónicas y de higiene Markdown (MD022/MD047)
│   │   └── onboard-state.json                  # Memoria persistente de progreso de la Entrevista Adaptativa SDD 2.0
│   ├── design-system/
│   │   └── design-tokens.json                  # Tokens UI/UX: paleta, tipografía, espaciado y estados
│   ├── templates/                              # Plantillas maestras estructurales
│   │   ├── spec.template.md                    # Plantilla EARS con sección Allowed Files
│   │   ├── scenarios.template.feature          # Plantilla Gherkin con etiquetas @AC-x.x
│   │   ├── plan.template.md                    # Plantilla Clean Arch + Sección 5: Security & STRIDE
│   │   ├── tasks.template.md                   # Plantilla de tareas atómicas TDD
│   │   ├── user_guide.template.md              # Plantilla obligatoria de Guía de Usuario (4 secciones)
│   │   └── impl_report.template.md             # Plantilla de reporte de implementación TDD
│   └── harness-config.json                     # Configuración políglota de linter, tests y capas
│
├── harness/                                    # Núcleo de gobernanza, pruebas y compuertas
│   ├── init.ps1                                # Verificador dinámico de salud y ejecutor de tests/linters
│   ├── verify-security.ps1                     # [NUEVO v6.0] Escáner de secretos, SAST y CVEs de dependencias
│   ├── sdd.ps1                                 # CLI central del backlog, candado SHA-256 y matriz
│   ├── spec-gate.ps1                           # Auditor Óctuple automatizado de cierre de feature (8 Checks)
│   ├── preview-design.ps1                      # Generador HTML interactivo de Design System + contraste WCAG
│   └── hooks/                                  # Scripts ejecutados por el motor de Antigravity IDE
│       ├── session-start.ps1                   # Hook SessionStart: auto-onboarding e inyección de estado activo
│       ├── pre-tool-enforce.ps1                # Hook PreToolUse: interceptor físico de escritura en src/
│       └── post-tool-check.ps1                 # Hook PostToolUse: auditoría continua de Clean Architecture
│
├── specs/                                      # Directorio de especificaciones por funcionalidad
│   └── <feature_id>/                           # Ej: FEAT-001/ o 001-autenticacion-pacientes/
│       ├── spec.md                             # Especificación funcional EARS con Allowed Files
│       ├── scenarios.feature                   # Escenarios BDD Gherkin ejecutables
│       ├── plan.md                             # Plan técnico con capas, dependencias y STRIDE Security
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
│   ├── application/                            # Casos de Uso, Orquestación y Puertos (Interfaces)
│   ├── infrastructure/                         # Adaptadores de BD, APIs externas, Criptografía y Mensajería
│   └── presentation/                           # Controladores, UI, CLI o Vistas (Aislamiento visual)
│
└── tests/                                      # Batería de pruebas automatizadas
    ├── unit/                                   # Pruebas unitarias de dominio y aplicación
    └── acceptance/                             # Pruebas de aceptación BDD (Step definitions de Gherkin)
```

---

## 3. Los 8 Comprobadores del Auditor Óctuple (`harness/spec-gate.ps1`)

Para que una funcionalidad sea marcada como **COMPLETED** y sellada criptográficamente en el Grafo DAG, debe superar las **8 compuertas duras** automatizadas sin una sola advertencia no resuelta:

| Check | Dimensión | Criterio de Verificación Automatizado |
| :---: | :--- | :--- |
| **1** | **Spec Drift & Git** | Compara el estado del workspace y los commits contra `## 5. Allowed Files` en `spec.md`. Tocar cualquier archivo fuera de la lista aborta la compuerta. |
| **2** | **Cobertura BDD 1:1** | Todos los criterios EARS (`AC-x.x`) declarados en `spec.md` deben existir como escenarios etiquetados `@AC-x.x` en `scenarios.feature` y contar con métodos de test implementados. |
| **3** | **Clean Architecture & Dependencies** | Inspección de AST de imports: `src/domain` y `src/application` no deben importar infraestructura. Las dependencias externas deben estar declaradas en `## 4. Allowed Dependencies` de `plan.md`. |
| **4** | **Firma Criptográfica SHA-256** | El hash del archivo `spec.md` se normaliza y verifica contra el candado sellado por el operador humano en `feature_list.json`. |
| **5** | **Anti-Fake Tests** | Detección estricta de pruebas simuladas (`skip`, `pass`, aserciones vacías o `assert True == True`) y ejecución dinámica real en verde con `init.ps1`. |
| **6** | **Guía de Usuario Obligatoria** | Verifica la existencia de `docs/user_guide_<feature>.md` con sus 4 secciones estructurales completas y **cero placeholders** (`TODO`, `TBD`, texto provisional). |
| **7** | **UI/UX Pro Max Compliance** | Si la funcionalidad toca `src/presentation`, verifica los 5 estados obligatorios, tokens semánticos en `plan.md`, ausencia de *magic hex codes* y contraste **WCAG 2.1 AA** ($\ge 4.5:1$). |
| **8** | **Secure Coding & OWASP Compliance (NUEVO)** | **Auditoría de Seguridad Integral:**<br>1. Declaración obligatoria de `## 5. Security & Threat Modeling` en `plan.md` para funcionalidades de infraestructura o presentación.<br>2. Escaneo anti-secretos: detección de API keys, tokens JWT, contraseñas y llaves privadas hardcodeadas en código.<br>3. Escaneo SAST contra inyecciones OWASP: detección de concatenación en queries SQL, `shell=True`, `os.system()`, `eval()`, `exec()` o XSS sin sanitizar.<br>4. Ejecución del script `harness/verify-security.ps1` con detección de CVEs en dependencias. |

---

## 4. La Nueva Skill: `sdd-secure-coding`

La skill de seguridad de SDD v6.0 (`.agents/skills/sdd-secure-coding/SKILL.md`) proporciona inteligencia defensiva de nivel bancario e institucional para los desarrolladores y el agente de IA:

### 1. La Tríada Letal (*Lethal Trifecta*)

Alerta de inmediato sobre cualquier controlador o manejador donde confluyen tres elementos:
$$\text{Datos Privados} \;+\; \text{Entrada No Confiable} \;+\; \text{Canal de Exfiltración}$$

### 2. Fronteras de Confianza (*Trust Boundaries* `‖`)

Exige mapear los puntos de cruce donde los datos no confiables ingresan a componentes protegidos:
$$\text{Cliente} \;\Vert\; \text{API / Edge} \;\Vert\; \text{Lógica de Negocio} \;\Vert\; \text{Base de Datos} \;\Vert\; \text{Terceros}$$
Toda defensa debe vivir en el lado confiable (servidor), jamás en el cliente.

### 3. Modelado de Amenazas STRIDE Ligero en `plan.md`

En cada funcionalidad crítica se documentan los controles específicos:

* **Spoofing (Suplantación):** Sesión verificada en servidor o JWT con algoritmo explícitamente fijado (rechazo de `alg:none`).
* **Tampering (Manipulación):** Valores calculados en servidor, validación estricta de esquemas, firmas HMAC y restricciones `CHECK`/`UNIQUE` en base de datos.
* **Repudiation (Repudio):** Bitácora de auditoría inmutable estructurada con `user_id` y marcas de tiempo confiables.
* **Information Disclosure (Fuga de Información):** Listas blancas de campos en DTOs de salida y consultas acotadas a propiedad (`WHERE owner_id = :current_user`).
* **Denial of Service (Denegación de Servicio):** Límites de tasa (*rate limiting*), límites de tamaño de carga útil y timeouts en consultas.
* **Elevation of Privilege (Elevación de Privilegios):** Autorización basada en el principio de menor privilegio (*deny-by-default*) aplicada a nivel de objeto en cada solicitud.

---

## 5. Comandos Operativos y CLI de Gobernanza (`harness/sdd.ps1`)

| Acción | Comando PowerShell | Propósito en el Ciclo |
| :--- | :--- | :--- |
| **Diagnóstico del Entorno** | `.\harness\init.ps1` | Verifica linters, analizador de tipos y pruebas unitarias/BDD. |
| **Estado del Backlog** | `.\harness\sdd.ps1 -Action status` | Muestra el tablero de funcionalidades, estados y dependencias DAG. |
| **Aprobación de Candado** | `.\harness\sdd.ps1 -Action approve -FeatureId <id> -Reason "<motivo>"` | Sella la especificación con hash SHA-256 e historial inmutable. |
| **Auditoría de Seguridad (NUEVO)** | `.\harness\sdd.ps1 -Action verify-security` | Ejecuta el escáner de secretos, patrones SAST y CVEs de dependencias. |
| **Saneamiento Markdown** | `.\harness\sdd.ps1 -Action fix-markdown` | Escanea y auto-repara violaciones MD022 (encabezados) y MD047 (salto final único). |
| **Previsualización UI/UX** | `.\harness\sdd.ps1 -Action preview-design` | Genera la vista previa interactiva HTML del sistema de diseño y contrastes. |
| **Auditoría de Cierre** | `.\harness\spec-gate.ps1 -FeatureId <id>` | Ejecuta las 8 compuertas duras del Auditor Óctuple. |
| **Cierre Formal** | `.\harness\sdd.ps1 -Action complete -FeatureId <id>` | Sella `completion_hash`, genera Matriz de Trazabilidad y desbloquea el DAG. |

---

## 6. Cómo Inicializar un Proyecto con SDD v6.0

Para crear un nuevo proyecto gobernado bajo el estándar v6.0:

```powershell
# En PowerShell
powershell -ExecutionPolicy Bypass -File .\setup-sdd-project-v6.ps1 -ProjectName "SistemaCritico" -Stack "python" -GitInit

# O mediante Python
python .\setup-sdd-project-v6.py
```

Al inicializarse, el IDE activará el hook `SessionStart`, desplegará las 16 skills canónicas (incluyendo `sdd-secure-coding` con sus guías OWASP/STRIDE) y configurará el interceptor `PreToolUse` para garantizar un desarrollo blindado desde la primera interacción.
