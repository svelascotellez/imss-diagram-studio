import os
import lint_md

print("=== Generando LIBRO BLANCO Y DOCUMENTO MAESTRO: FRAMEWORK SDD v6.5 ===")

# Secciones del documento maestro
sections = []

sections.append("""# LIBRO BLANCO Y DOCUMENTO MAESTRO: FRAMEWORK SDD v6.5

## Specification-Driven Development (Enterprise Regulatory & Compliance Edition)

### Marco de Gobernanza, Arquitectura Limpia Políglota, Candado Criptográfico, Ciberseguridad Defensiva, Resiliencia k6 y Dossier Regulatorio PDF para el Desarrollo con Agentes de Inteligencia Artificial

> **Autor:** Salvador Velasco & Antigravity (Google DeepMind Team)<br>
> **Versión Oficial:** 6.5<br>
> **Fecha de Publicación:** 30 de Octubre de 2026<br>
> **Clasificación:** Estándar Metodológico Corporativo y de Ingeniería de Software<br>
> **Estado:** Aprobado para Producción y Auditorías Regulatorias Internacionales

---

## 1. Resumen Ejecutivo y Visión Estratégica

### 1.1. El Dilema del Desarrollo Asistido por Inteligencia Artificial

La adopción masiva de modelos de lenguaje grande (LLMs) y agentes autónomos de codificación en entornos empresariales ha incrementado exponencialmente la velocidad de generación de código, pero ha introducido una crisis silenciosa de gobernanza, deuda técnica oculta y riesgos de seguridad:

1. **Alucinaciones Funcionales y Desviación de Alcance (*Spec Drift*)**: Los agentes tienden a resolver problemas agregando dependencias innecesarias, alterando contratos de API existentes o modificando archivos no autorizados en el repositorio.
2. **Pruebas Falsas (*Fake Tests*)**: Es habitual que los agentes generen suites de pruebas complacientes (`assert true == true`, mocks triviales o aserciones vacías) para simular una cobertura del 100% sin validar la lógica de negocio.
3. **Erosión Arquitectónica y Código Espagueti**: Al carecer de visión global de largo plazo, los agentes rompen las capas de abstracción, inyectando llamadas directas a base de datos en controladores web o importando librerías de infraestructura en el dominio puro.
4. **Vulnerabilidades y Secretos Filtrados**: Generación inadvertida de credenciales hardcodeadas, inyecciones SQL/NoSQL y uso de paquetes de software con CVEs conocidos.
5. **Degradación de Desempeño y Latencia**: Algoritmos $O(N^2)$, consultas $N+1$ en bases de datos relacionales y serializaciones JSON ineficientes que aprueban pruebas unitarias pero colapsan bajo concurrencia.
6. **Invalidez Regulatoria y Rechazo en Auditorías**: En industrias reguladas (Fintech, Salud, Farmacéutica, Gobierno y Defensa), el código sin trazabilidad matemática formal, sin firmas inmutables de aprobación humana (HITL) y sin expediente técnico estructurado resulta legalmente inaceptable.

### 1.2. El Paradigma SDD: "La Especificación Manda, el Código Obedece y la Criptografía Gobierna"

El **Specification-Driven Development (SDD v6.5)** resuelve de raíz estas vulnerabilidades mediante un principio arquitectónico inmutable: **el código no es el soberano; la especificación formal es la única fuente de verdad**.

Bajo el marco SDD, ningún agente de IA ni desarrollador humano puede escribir una sola línea de código ejecutable sin antes haber redactado, clarificado y sellado criptográficamente una especificación funcional formal basada en sintaxis **EARS** (*Easy Approach to Requirements Syntax*) y escenarios **BDD** (*Behavior-Driven Development*). Una vez sellada mediante un hash SHA-256 HMAC inmutable, un arnés de software determinista (*The Harness*) audita de forma implacable que el código implementado respete estrictamente los archivos declarados (*Allowed Files*), preserve la pureza de las capas de Clean Architecture, supere análisis de ciberseguridad, cumpla umbrales de latencia $P_{95} \\le 200\\text{ ms}$ y emita un expediente regulatorio en PDF válido para auditorías internacionales.

### 1.3. Evolución del Framework: De v1.0 a v6.5

```mermaid
flowchart LR
    V1["v1.0 - v4.3: EARS + BDD Core"] --> V5["v5.0 - v5.4: Clean Arch + Sha-256"]
    V5 --> V60["v6.0: Secure Coding (OWASP)"]
    V60 --> V62["v6.2: CI/CD Governance"]
    V62 --> V63["v6.3: Cockpit Web & DAG"]
    V63 --> V64["v6.4: k6 SLA Gate"]
    V64 --> V65["v6.5: Expediente Regulatorio PDF"]
```

- **SDD v1.0 - v4.3**: Introducción de EARS formal, escenarios Gherkin, plantillas estructuradas y control de fases básicas.
- **SDD v5.0 - v5.4**: Incorporación de Clean Architecture, aislamiento de capas, candados criptográficos SHA-256 (Approval y Completion Seals) y pre-commit hooks.
- **SDD v6.0 - v6.1**: Ciberseguridad Defensiva, modelado de amenazas STRIDE, escaneo de secretos (TruffleHog) y auditoría de CVEs (pip-audit / npm audit).
- **SDD v6.2**: Gobernanza de Integración Continua con pipelines en GitHub Actions y GitLab CI, y resúmenes automatizados de Pull Request.
- **SDD v6.3**: Observabilidad Ejecutiva con el Cockpit Web Dashboard interactivo y visor visual del grafo DAG de dependencias (TopoSort).
- **SDD v6.4 (v6.e)**: Compuerta de Rendimiento y Resiliencia SLA (k6 Benchmark), elevando la verificación al Auditor Nónuplo (9 Hard Gates).
- **SDD v6.5 (Edición Actual)**: Expediente Regulatorio y Compliance PDF (Pilar 10), compilador Chromium Headless, acreditación ISO 27001 / FDA / SOC 2 / HIPAA y catálogo de 20 skills canónicas.

---

## 2. Los 10 Pilares Fundamentales de SDD v6.5

El framework SDD v6.5 se fundamenta en 10 pilares sinérgicos que garantizan la calidad integral del ciclo de vida del software:

```mermaid
flowchart TD
    P1["Pilar 1: Especificacion Viva (EARS & Anti-Drift)"] --> P2["Pilar 2: BDD Riguroso (Gherkin 1:1)"]
    P2 --> P3["Pilar 3: Clean Architecture Poliglota"]
    P3 --> P4["Pilar 4: Integridad Criptografica (SHA-256)"]
    P4 --> P5["Pilar 5: Control de Tareas y Fases"]
    P5 --> P6["Pilar 6: Secure Coding & OWASP"]
    P6 --> P7["Pilar 7: Observabilidad Ejecutiva & Cockpit Web"]
    P7 --> P8["Pilar 8: Gobernanza CI/CD Cloud"]
    P8 --> P9["Pilar 9: Compuerta de Rendimiento k6"]
    P9 --> P10["Pilar 10: Expediente Regulatorio PDF"]
```

### 2.1. Pilar 1: Especificación Viva (EARS y Allowed Files)

Todo requisito debe ser formalizado en `specs/<feature>/spec.md` utilizando sintaxis EARS estricta:

- `[Ubiquitous]`: El sistema siempre deberá cumplir con la propiedad.
- `[Event-driven]`: **WHEN** [evento] **THE SYSTEM SHALL** [acción].
- `[State-driven]`: **WHILE** [estado] **THE SYSTEM SHALL** [acción].
- `[Optional]`: **WHERE** [condición opcional] **THE SYSTEM SHALL** [acción].
- `[Unwanted]`: **IF** [error o excepción] **THEN THE SYSTEM SHALL** [recuperación segura].

Adicionalmente, el documento `specs/<feature>/plan.md` define de forma obligatoria la sección `## Allowed Files`. Cualquier archivo creado o modificado fuera de esta lista provoca la detención inmediata del proceso de compilación y commit (Aduana 1).

### 2.2. Pilar 2: BDD Riguroso & Trazabilidad 1:1

Cada criterio de aceptación EARS `AC-x.x` debe mapearse exactamente contra un escenario ejecutable en `specs/<feature>/scenarios.feature` redactado en Gherkin (`Given-When-Then`), y a su vez contra una prueba unitaria/integración en el directorio de pruebas. La cobertura debe ser bidireccional, exhaustiva y del 100%.

### 2.3. Pilar 3: Clean Architecture Políglota

El código debe organizarse en cuatro capas concéntricas con regla de dependencia unidireccional estricta hacia el centro:

1. **Domain (`src/domain/`)**: Entidades puras de negocio y reglas corporativas. Cero librerías de infraestructura, frameworks web o bases de datos.
2. **Application (`src/application/`)**: Casos de uso, orquestación y contratos de interfaces (puertos).
3. **Presentation (`src/presentation/`)**: Controladores REST, UI, CLI o vistas. Desacoplada de detalles de infraestructura.
4. **Infrastructure (`src/infrastructure/`)**: Adaptadores para bases de datos, redes, sistemas de archivos y servicios cloud.

El arnés valida esta pureza arquitectónica mediante expresiones regulares de importación adaptadas a cada stack (Python, TypeScript, C#, Go, Java, Dart).

### 2.4. Pilar 4: Integridad Criptográfica (SHA-256 HMAC)

El desarrollo asistido por IA exige inmutabilidad matemática:

- **Approval Seal (`approval_hash`)**: Cuando el desarrollador humano aprueba la especificación (`sdd.ps1 -Action approve`), el arnés calcula el hash SHA-256 de `spec.md`, `scenarios.feature` y `plan.md`. Si un agente intenta alterar la especificación a posteriori para justificar un código erróneo, el hash se invalida y el arnés bloquea el proceso.
- **Completion Seal (`completion_hash`)**: Tras aprobar las 9 compuertas de calidad, se genera un hash criptográfico de cierre que se sella en `feature_list.json` y se archiva en `CHECKPOINTS.md`.

### 2.5. Pilar 5: Control de Tareas y Fases Operativas

El progreso se desglosa en subtareas atómicas dentro de `specs/<feature>/tasks.md`. El arnés guía la ejecución a través de 6 fases secuenciales sin permitir saltos arbitrarios.

### 2.6. Pilar 6: Ciberseguridad Defensiva y Threat Modeling

Integración de modelado de amenazas **STRIDE** (*Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege*), escaneo automatizado de credenciales con **TruffleHog**, detección de patrones de inyección (SQL, Command, Path Traversal) y auditoría de vulnerabilidades en dependencias mediante `pip-audit` o `npm audit` (Aduana 8).

### 2.7. Pilar 7: Observabilidad Ejecutiva & Cockpit Web

Panel interactivo HTML5 en tiempo real (`progress/sdd_dashboard.html`) servido mediante un servidor HTTP local en PowerShell (`sdd.ps1 -Action dashboard -Live`). Permite inspeccionar el backlog, la salud de las 9 compuertas y el grafo DAG de dependencias ordenado mediante clasificación topológica (*TopoSort*).

### 2.8. Pilar 8: Gobernanza de Integración Continua Cloud (CI/CD)

Workflows estandarizados para **GitHub Actions** (`.github/workflows/sdd-gate.yml`) y **GitLab CI** (`.gitlab-ci.yml`) que ejecutan de forma automática la auditoría de seguridad, higiene Markdown, pruebas BDD, compuerta k6 y compilación del expediente regulatorio, emitiendo un reporte enriquecido de Pull Request (`harness/pr-summary.ps1`).

### 2.9. Pilar 9: Compuerta de Rendimiento y Resiliencia SLA (k6 Benchmark)

Asegura que el software cumpla umbrales de servicio críticos antes de su despliegue:

- Latencia en el percentil 95: $P_{95} \\le 200\\text{ ms}$.
- Latencia en el percentil 99: $P_{99} \\le 500\\text{ ms}$.
- Tasa de errores HTTP/red: $\\text{Error Rate} = 0.0\\%$.
- Arquitectura dual: Si el ejecutable `k6` está presente en el host, corre la prueba en vivo; si no, realiza una validación estática de umbrales declarativos y certifica el script para los runners de CI/CD.

### 2.10. Pilar 10: Expediente Regulatorio y Compliance PDF

Consolidación automatizada de toda la evidencia documental, funcional, arquitectónica y de ciberseguridad en un **Dossier Oficial de Auditoría** en formato PDF nativo y HTML para acreditación ante comités de certificación y entes regulatorios (ISO 27001, FDA 21 CFR Part 11, SOC 2, HIPAA, CMMI Nivel 5).

---

## 3. Topología Canónica del Repositorio SDD v6.5

Un proyecto estructurado bajo SDD v6.5 presenta la siguiente organización jerárquica de archivos:

```text
<RootProject>/
├── .agents/                      # Inteligencia Artificial y Extensiones de IDE
│   ├── hooks.json                # Definicion de Hooks (SessionStart, PreToolUse, PostToolUse)
│   └── skills/                   # Las 20 Skills Canonicas de SDD v6.5
│       ├── sdd-orchestrator/     # Skill #1: Orquestador general del ciclo SDD
│       ├── sdd-onboard/          # Skill #2: Onboarding e inicializacion de proyecto
│       ├── sdd-constitution/    # Skill #3: Guardián de reglas constitucionales
│       ├── sdd-specify/         # Skill #4: Redactor formal EARS
│       ├── sdd-clarify/         # Skill #5: Entrevistador y clarificador de ambigüedades
│       ├── sdd-ui-ux/           # Skill #6: Disenador de interfaz y accesibilidad
│       ├── sdd-design-system/   # Skill #7: Catalogo de tokens y estilos
│       ├── sdd-preview-design/  # Skill #8: Prototipador visual interactivo
│       ├── sdd-plan/            # Skill #9: Arquitecto Clean Arch y Allowed Files
│       ├── sdd-tasks/           # Skill #10: Desglosador de tareas atomicas
│       ├── sdd-implement/       # Skill #11: Desarrollador de codigo de produccion
│       ├── sdd-user-guide/      # Skill #12: Redactor de guias vivas de usuario
│       ├── sdd-validate/        # Skill #13: Auditor de calidad y 9 aduanas
│       ├── sdd-change-spec/     # Skill #14: Gestor de RFCs y cambios formales
│       ├── sdd-reverse-spec/    # Skill #15: Ingeniero inverso de sistemas legados
│       ├── sdd-secure-coding/   # Skill #16: Oficial de ciberseguridad y SAST
│       ├── sdd-dashboard/       # Skill #17: Gestor del Cockpit Web y DAG
│       ├── sdd-cicd/            # Skill #18: Ingeniero de pipelines CI/CD
│       ├── sdd-performance/     # Skill #19: Especialista en benchmarks k6 y SLAs
│       └── sdd-compliance/      # Skill #20: Oficial de cumplimiento y expediente PDF
├── .github/
│   └── workflows/
│       └── sdd-gate.yml          # Workflow GitHub Actions con las 9 Aduanas y PDF
├── .gitlab-ci.yml                # Pipeline GitLab CI con etapas completas
├── .specify/
│   ├── harness-config.json       # Configuracion del proyecto, stack y Allowed Files
│   ├── memory/                   # Memoria constitucional persistente
│   │   └── constitution.md       # Principios inmutables del proyecto
│   ├── design-system/            # Tokens de color, espaciado y tipografia
│   └── templates/                # Plantillas estandarizadas EARS, BDD y planes
├── docs/                         # Guias de usuario vivas y matrices de trazabilidad
├── harness/                      # Arnés determinista de gobernanza y auditoria
│   ├── dashboard.ps1             # Servidor web local y Cockpit Dashboard
│   ├── export-compliance.ps1     # Generador de Expediente Regulatorio PDF/HTML
│   ├── hooks/                    # Scripts de hooks para el IDE
│   ├── init.ps1                  # Configurador y gestor de dependencias
│   ├── pr-summary.ps1            # Generador de resumen de gobernanza para Pull Requests
│   ├── sdd.ps1                   # Comando CLI unificado del arnes
│   ├── spec-gate.ps1             # Auditor Nonuplo (9 Hard Gates)
│   ├── verify-performance.ps1    # Verificador de Rendimiento k6 (Aduana 9)
│   └── verify-security.ps1       # Verificador de Seguridad OWASP y SAST (Aduana 8)
├── progress/                     # Reportes generados, telemetria y dashboards
│   ├── compliance_dossier.html   # Expediente regulatorio en HTML (@media print)
│   ├── compliance_dossier.pdf    # Expediente regulatorio oficial en PDF
│   ├── performance_report.json   # Metricas de latencia y errores k6
│   ├── pr_summary.md             # Resumen auditado de Pull Request
│   └── sdd_dashboard.html        # Cockpit visual interactivo
├── specs/                        # Especificaciones de funcionalidades
│   └── <feature_id>/
│       ├── spec.md               # Requisitos formales EARS
│       ├── scenarios.feature     # Escenarios Gherkin 1:1
│       ├── plan.md               # Plan arquitectonico y Allowed Files
│       └── tasks.md              # Lista de tareas secuenciales [ ] / [x]
├── src/                          # Codigo fuente (Clean Architecture)
│   ├── domain/                   # Capa 1: Entidades puras y reglas de negocio
│   ├── application/              # Capa 2: Casos de uso y puertos
│   ├── presentation/             # Capa 3: Controladores, vistas y APIs
│   └── infrastructure/           # Capa 4: Adaptadores, persistencia y red
├── tests/
│   ├── unit/                     # Pruebas unitarias
│   ├── bdd/                      # Pruebas de aceptacion BDD
│   └── performance/              # Scripts k6 de pruebas de carga y SLAs
├── CHECKPOINTS.md                # Bitacora inmutable de firmas criptograficas
└── feature_list.json             # Backlog formal con estados y dependencias
```

---

## 4. El Ciclo de Vida Operativo de 6 Fases

El proceso de desarrollo en SDD v6.5 se ejecuta a través de 6 fases deterministas:

```mermaid
sequenceDiagram
    autonumber
    actor H as Desarrollador Humano (HITL)
    participant A as Agente de IA (Antigravity)
    participant Hrn as Arnés SDD (sdd.ps1)
    participant Gate as spec-gate.ps1
    participant Exp as export-compliance.ps1
    participant CI as Pipeline CI/CD

    Note over H,A: Fase 1 & 2: Especificación y Clarificación Formal
    H->>A: "Solicito implementar modulo de pagos tokenizados"
    A->>Hrn: sdd.ps1 -Action create -FeatureId feat-pay
    A->>A: Redacta spec.md (EARS), scenarios.feature (BDD) y plan.md (Allowed Files)
    H->>Hrn: sdd.ps1 -Action approve -FeatureId feat-pay
    Hrn-->>H: Approval Seal emitido (SHA-256 inmutable)

    Note over H,A: Fase 3, 4 & 5: Implementación, Seguridad y Rendimiento
    A->>A: Escribe codigo en domain, application, presentation e infra
    A->>Hrn: sdd.ps1 -Action verify-security
    Hrn-->>A: [OK] Cero secretos, cero CVEs (Aduana 8 superada)
    A->>Hrn: sdd.ps1 -Action verify-performance -FeatureId feat-pay
    Hrn-->>A: [OK] P95 <= 200ms, Error Rate = 0% (Aduana 9 superada)

    Note over H,CI: Fase 6: Auditoría Nónupla, Cierre y Certificación
    A->>Hrn: sdd.ps1 -Action complete -FeatureId feat-pay
    Hrn->>Gate: Ejecuta Auditor Nonuplo (Gates 1/9 a 9/9)
    Gate-->>Hrn: 9 Aduanas Aprobadas -> Emite Completion Seal
    Hrn->>Exp: sdd.ps1 -Action export-compliance -Format all
    Exp-->>H: Genera compliance_dossier.pdf (Expediente Oficial)
    H->>CI: git push origin feat-pay -> Pull Request
    CI-->>H: Pipeline CI/CD Aprobado (9 Aduanas + Dossier Certificado)
```

### Detalle de las Fases Operativas:

1. **Fase 1: Especificación Formal**: El agente analiza el requerimiento del usuario y redacta `specs/<id>/spec.md` estructurando los criterios de aceptación en sintaxis formal EARS.
2. **Fase 2: Clarificación y Aprobación Humana**: El desarrollador humano revisa la especificación y ejecuta `sdd.ps1 -Action approve -FeatureId <id>`, emitiendo el **Approval Seal (SHA-256)** que bloquea cualquier modificación no autorizada al alcance.
3. **Fase 3: Implementación Disciplinada**: El agente y el desarrollador construyen el código fuente ciñéndose estrictamente a la lista de `Allowed Files` y las capas de Clean Architecture.
4. **Fase 4: Verificación de Ciberseguridad Defensiva**: Se ejecuta `sdd.ps1 -Action verify-security` para asegurar la ausencia de credenciales expuestas, inyecciones SQL o paquetes vulnerables.
5. **Fase 5: Validación de Rendimiento y SLAs**: Se ejecuta `sdd.ps1 -Action verify-performance` para certificar que la solución responde en menos de 200 ms ($P_{95}$) bajo concurrencia.
6. **Fase 6: Auditoría Nónupla y Expediente Regulatorio**: Se ejecuta `sdd.ps1 -Action complete -FeatureId <id>` para validar las 9 compuertas y emitir el **Completion Seal**. Posteriormente, `sdd.ps1 -Action export-compliance -Format all` compila el expediente regulatorio en PDF.

---

## 5. El Auditor Nónuplo: Las 9 Hard Gates Infranqueables

El script `harness/spec-gate.ps1` actúa como aduana estricta de control de calidad. Si una sola de las 9 compuertas no cumple sus condiciones de aprobación, el proceso se interrumpe con código de error 1:

| Aduana | Nombre de Compuerta | Tipo de Verificación | Condición de Aprobación |
| :--- | :--- | :--- | :--- |
| **Gate 1** | **Allowed Files & Anti-Drift** | Integridad de Repositorio | Solo archivos declarados en `plan.md` fueron modificados en el workspace y en commits de Git. |
| **Gate 2** | **Cobertura BDD 1:1** | Trazabilidad Funcional | Cada EARS `AC-x.x` tiene correspondencia exacta con escenarios Gherkin y pruebas ejecutables. |
| **Gate 3** | **Clean Architecture Políglota** | Pureza Arquitectónica | Capa Dominio con 0 dependencias externas; Presentación desacoplada de Infraestructura. |
| **Gate 4** | **Firma Criptográfica Approval** | Validez de Requisitos | Hash SHA-256 de `spec.md`, `scenarios.feature` y `plan.md` coincide con el sello inicial. |
| **Gate 5** | **Completitud de Tareas** | Progreso Estructurado | Todas las tareas de `tasks.md` están marcadas `[x]` sin pendientes. |
| **Gate 6** | **Guía de Usuario Viva** | Documentación de Entrega | `docs/user_guide_<feature>.md` existe, incluye ejemplos y cumple las 7 reglas de markdownlint. |
| **Gate 7** | **Candado Inmutable Completion** | Sellado de Cierre | Hash SHA-256 inmutable registrado en `feature_list.json` y archivado en `CHECKPOINTS.md`. |
| **Gate 8** | **Seguridad OWASP & Secret Scan** | Ciberseguridad Defensiva | Cero credenciales hardcodeadas, cero inyecciones SQL y 0 CVEs High/Critical en dependencias. |
| **Gate 9** | **Performance & SLA Gate (k6)** | Rendimiento y Resiliencia | Latencia $P_{95} \\le 200\\text{ ms}$, $P_{99} \\le 500\\text{ ms}$ y tasa de fallos $= 0.0\\%$. |

---

## 6. El Expediente Regulatorio y Compliance PDF (Pilar 10)

El script `harness/export-compliance.ps1` materializa la evidencia de calidad y gobierno en un entregable corporativo de alta resolución.

### 6.1. Mecanismo de Compilación Chromium Headless

En lugar de depender de librerías externas que requieren entornos pesados (Java, Python o compiladores de C++), SDD v6.5 aprovecha el motor Chromium instalado de forma nativa en los sistemas operativos modernos (**Microsoft Edge** en Windows o **Google Chrome**):

```powershell
# Invocacion del motor Chromium headless para renderizar PDF vectorial
$pArgs = @(
    "--headless=new",
    "--disable-gpu",
    "--no-first-run",
    "--no-default-browser-check",
    "--run-all-compositor-stages-before-draw",
    "--print-to-pdf=$FullPdfPath",
    $FullHtmlPath
)
Start-Process -FilePath $browserPath -ArgumentList $pArgs -Wait -NoNewWindow
```

Este procedimiento produce un documento PDF vectorial, nítido y compatible con los estándares de impresión A4 (`@media print`), con márgenes de 18 mm y numeración automática de folios.

### 6.2. Mapeo contra Estándares Regulatorios

El expediente consolida y certifica la adherencia formal a:

1. **ISO/IEC 27001:2022 (Control A.14)**: Gestión de cambios controlada y análisis de código seguro.
2. **FDA 21 CFR Part 11**: Firmas electrónicas inmutables y cadena de custodia con registros de auditoría HITL.
3. **SOC 2 Type II**: Confidencialidad e integridad del procesamiento de datos en reposo y en tránsito.
4. **HIPAA Security Rule (45 CFR Part 164)**: Auditoría de accesos y prevención de fugas de credenciales.
5. **CMMI Maturity Level 5**: Gestión cuantitativa y mejora continua guiada por métricas de rendimiento y SLAs.

---

## 7. El Catálogo Canónico de las 20 Skills de Inteligencia Artificial

Antigravity IDE orquesta el desarrollo mediante 20 habilidades canónicas versionadas en `.agents/skills/`:

| # | Skill Canónica | Rol Operativo | Entregables y Responsabilidades Principales |
| :--- | :--- | :--- | :--- |
| 1 | `sdd-orchestrator` | Director de Orquesta SDD | Guía el ciclo de vida, transiciones de estado y derivación de agentes. |
| 2 | `sdd-onboard` | Inicializador de Proyecto | Configura el entorno, detecta el stack y presenta el backlog inicial. |
| 3 | `sdd-constitution` | Guardián Constitucional | Aplica los principios rectores inmutables del proyecto. |
| 4 | `sdd-specify` | Analista de Requisitos | Redacta `spec.md` con sintaxis formal EARS y criterios de aceptación. |
| 5 | `sdd-clarify` | Validador de Requisitos | Resuelve ambigüedades mediante entrevistas interactivas. |
| 6 | `sdd-ui-ux` | Diseñador de Interfaces | Modela la experiencia de usuario y arquitectura de información. |
| 7 | `sdd-design-system` | Gestor del Sistema de Diseño | Define tokens de diseño, paletas y tipografías consistentes. |
| 8 | `sdd-preview-design` | Visualizador Visual | Genera wireframes interactivos en HTML para validación humana. |
| 9 | `sdd-plan` | Arquitecto de Software | Diseña `plan.md`, capas Clean Architecture y `Allowed Files`. |
| 10 | `sdd-tasks` | Planificador de Tareas | Desglosa la implementación en subtareas atómicas en `tasks.md`. |
| 11 | `sdd-implement` | Desarrollador Principal | Escribe el código fuente en estricta conformidad con `Allowed Files`. |
| 12 | `sdd-user-guide` | Documentador Técnico | Redacta la guía viva de usuario en `docs/user_guide_<feature>.md`. |
| 13 | `sdd-validate` | Auditor de Calidad | Ejecuta `spec-gate.ps1` y valida las 9 aduanas obligatorias. |
| 14 | `sdd-change-spec` | Ingeniero de Cambios | Controla la evolución de especificaciones mediante RFC estructurado. |
| 15 | `sdd-reverse-spec` | Ingeniero Inverso | Reconstruye especificaciones EARS a partir de bases de código legadas. |
| 16 | `sdd-secure-coding` | Oficial de Seguridad | Ejecuta SAST, escaneo de secretos y modelado de amenazas STRIDE. |
| 17 | `sdd-dashboard` | Gestor del Cockpit Web | Actualiza el panel interactivo y servidor DAG local en tiempo real. |
| 18 | `sdd-cicd` | Ingeniero de Integración | Configura y mantiene pipelines CI/CD en GitHub Actions y GitLab CI. |
| 19 | `sdd-performance` | Ingeniero de SLAs y Carga | Modela benchmarks k6, audita latencias P95/P99 y certifica la Aduana 9. |
| 20 | `sdd-compliance` | Oficial de Cumplimiento | Compila el expediente regulatorio oficial en PDF y valida ISO/FDA/SOC2. |

### Los 3 Hooks Nativos del IDE (`.agents/hooks.json`):

1. **`SessionStart`**: Al abrir Antigravity IDE, detecta si el proyecto ha sido inicializado y activa automáticamente el agente de onboarding.
2. **`PreToolUse`**: Intercepta comandos de edición de archivos y bloquea cualquier intento de escribir en ficheros no declarados en `Allowed Files`.
3. **`PostToolUse`**: Audita la integridad de los hashes criptográficos tras operaciones críticas en el repositorio.

---

## 8. Compatibilidad Políglota y Reglas de Importación Limpia

El framework implementa detectores heurísticos y reglas de expresiones regulares adaptadas a los stacks tecnológicos corporativos más extendidos:

| Lenguaje / Stack | Ubicación de Dominio | Patrón de Expresión Regular para Detección de Violaciones Arquitectónicas |
| :--- | :--- | :--- |
| **Python** | `src/domain/` | `(?m)^\s*(?:from\s+(?:presentation|infrastructure)\b|import\s+(?:presentation|infrastructure)\b)` |
| **TypeScript / Node.js** | `src/domain/` | `(?:from\s+['"].*(?:presentation|infrastructure)['"]|require\(['"].*(?:presentation|infrastructure)['"]\))` |
| **C# / .NET** | `src/Domain/` | `(?m)^\s*using\s+(?:global::)?(?:.*Presentation|.*Infrastructure)` |
| **Go** | `src/domain/` | `(?m)^\s*(?:import\s+"(?:[^"]*\/)?(?:presentation|infrastructure)"|"(?:[^"]*\/)?(?:presentation|infrastructure)")` |
| **Dart / Flutter** | `lib/domain/` | `(?m)^\s*import\s+['"].*(?:presentation|infrastructure).*['"]` |
| **Java / Spring Boot** | `src/main/java/.../domain/` | `(?m)^\s*import\s+(?:.*\.presentation\..*|.*\.infrastructure\..*);` |

---

## 9. Cockpit Web Dashboard & Servidor DAG en Vivo

El script `harness/dashboard.ps1` genera un entorno visual interactivo en HTML5 (`progress/sdd_dashboard.html`):

- **Panel de KPIs de Gobernanza**: Métricas en tiempo real de funcionalidades completadas, pendientes, estado de las 9 compuertas y candados criptográficos.
- **Visor Visual del Grafo DAG**: Renderizado visual de las relaciones de precedencia (`depends_on`) entre funcionalidades mediante ordenación topológica (*TopoSort*).
- **Consola de Comandos Rápidos**: Botones interactivos con copia en un clic al portapapeles para comandos frecuentes:
  - `.\harness\sdd.ps1 -Action status`
  - `.\harness\sdd.ps1 -Action verify-security`
  - `.\harness\sdd.ps1 -Action verify-performance`
  - `.\harness\sdd.ps1 -Action export-compliance -Format pdf`
- **Servidor HTTP Embebido**: Permite iniciar un servidor web ligero en PowerShell mediante `.\harness\sdd.ps1 -Action dashboard -Live -Port 8080` con recarga automática ante cambios en `feature_list.json`.

---

## 10. Gobernanza CI/CD Cloud y Protección de Ramas

Los archivos `.github/workflows/sdd-gate.yml` y `.gitlab-ci.yml` protegen las ramas principales (`main`, `develop`) ejecutando en cada Pull Request:

1. **Higiene de Formato**: Validación estricta de las 7 reglas de markdownlint con `sdd.ps1 -Action fix-markdown`.
2. **Ciberseguridad y Secret Scanning**: Escaneo SAST con `sdd.ps1 -Action verify-security`.
3. **Compuerta de Rendimiento**: Validación de SLAs con `sdd.ps1 -Action verify-performance`.
4. **Ejecución de Pruebas**: Suite de pruebas BDD y unitarias con `init.ps1 -Mode test`.
5. **Auditoría Nónupla**: Evaluación de las 9 compuertas en funcionalidades activas con `spec-gate.ps1`.
6. **Expediente Regulatorio**: Compilación de `compliance_dossier.pdf` con `sdd.ps1 -Action export-compliance -Format all`.
7. **Publicación de Artefactos**: Resumen automático de Pull Request (`progress/pr_summary.md`) y dashboard visual archivados por 30 días.

---

## 11. Manual de Operaciones y Referencia de Comandos del Arnés (`harness/sdd.ps1`)

| Comando | Parámetros Opcionales | Descripción Operativa |
| :--- | :--- | :--- |
| `.\harness\sdd.ps1 -Action status` | Ninguno | Muestra el estado actual del backlog, features y firmas. |
| `.\harness\sdd.ps1 -Action create` | `-FeatureId <id> -Title <str>` | Inicializa una nueva funcionalidad con sus plantillas EARS y BDD. |
| `.\harness\sdd.ps1 -Action approve` | `-FeatureId <id>` | Valida la especificación y sella el **Approval Seal (SHA-256)**. |
| `.\harness\sdd.ps1 -Action verify-security` | Ninguno | Ejecuta escaneo de secretos y auditoría de vulnerabilidades SAST. |
| `.\harness\sdd.ps1 -Action verify-performance` | `-FeatureId <id> -Vus <int> -Duration <str>` | Ejecuta el benchmark de carga k6 y audita latencias P95/P99. |
| `.\harness\sdd.ps1 -Action complete` | `-FeatureId <id>` | Ejecuta el Auditor Nónuplo (9 Gates) y emite el **Completion Seal**. |
| `.\harness\sdd.ps1 -Action export-compliance` | `-FeatureId <id> -Format <pdf|html|md|all> -Open` | Compila el Expediente Regulatorio oficial en PDF y HTML. |
| `.\harness\sdd.ps1 -Action dashboard` | `-NoBrowser -Live -Port <int>` | Genera o inicia el Cockpit Dashboard interactivo con visor DAG. |
| `.\harness\sdd.ps1 -Action init-cicd` | Ninguno | Configura o refresca los workflows de GitHub Actions y GitLab CI. |
| `.\harness\sdd.ps1 -Action pr-summary` | `-OutputFile <path>` | Genera el informe consolidado de Pull Request con el checklist de 9 Gates. |
| `.\harness\sdd.ps1 -Action fix-markdown` | Ninguno | Corrige de forma automática las 7 reglas de markdownlint. |

---

## 12. Diccionario Exhaustivo de Términos SDD (Glosario Oficial)

### Categoría 1: Metodologías y Paradigmas

- **Spec-Driven Development (SDD)**: Metodología formal de ingeniería de software donde la especificación precede, delimita y gobierna matemáticamente la implementación de código ejecutable.
- **Human-in-the-Loop (HITL)**: Principio de gobernanza que exige validación y aprobación humana explícita en puntos críticos de decisión antes de permitir la transición de estados.
- **Anti-Drift**: Mecanismo que impide que el código generado se desvíe del alcance formalmente especificado y aprobado.

### Categoría 2: Especificación y Requisitos

- **EARS (Easy Approach to Requirements Syntax)**: Notación formal para redacción de requisitos de software que elimina la ambigüedad mediante estructuras sintácticas rigurosas.
- **BDD (Behavior-Driven Development)**: Técnica de desarrollo donde los requisitos se expresan como escenarios de comportamiento ejecutables en lenguaje natural estructurado (Gherkin).
- **Allowed Files**: Declaración explícita e inmutable de los únicos archivos que pueden ser modificados o creados para implementar una funcionalidad específica.

### Categoría 3: Criptografía y Gobernanza

- **Approval Seal**: Hash SHA-256 HMAC inmutable calculado sobre la tríada documental (`spec.md`, `scenarios.feature`, `plan.md`) al momento de la aprobación humana.
- **Completion Seal**: Hash SHA-256 definitivo emitido tras aprobar satisfactoriamente las 9 compuertas del Auditor Nónuplo.
- **Checkpoints Log (`CHECKPOINTS.md`)**: Registro cronológico inmutable que documenta la cadena de custodia y los eventos de firma digital del proyecto.

### Categoría 4: Arquitectura y Rendimiento

- **Clean Architecture**: Patrón arquitectónico que organiza el código en capas concéntricas con regla de dependencia estricta hacia el centro (Dominio puro).
- **Auditor Nónuplo (9 Hard Gates)**: Conjunto de 9 verificaciones automatizadas obligatorias que auditan alcance, BDD, arquitectura, criptografía, tareas, documentación, cierre, seguridad y rendimiento.
- **Percentil 95 ($P_{95}$)**: Métrica estadística que establece que el 95% de las solicitudes deben completarse en un tiempo inferior al umbral contractual ($\\le 200\\text{ ms}$).

### Categoría 5: Compliance y Regulación

- **Compliance Dossier**: Expediente técnico oficial emitido en PDF y HTML que consolida toda la evidencia documental, de seguridad y de pruebas para auditorías regulatorias.
- **FDA 21 CFR Part 11**: Regulación federal de EE. UU. que establece los criterios para que los registros electrónicos y firmas digitales sean considerados equivalentes a registros en papel.
- **ISO/IEC 27001**: Estándar internacional para sistemas de gestión de seguridad de la información.

---

## 13. Conclusiones y Beneficios Estratégicos

El **Framework SDD v6.5** consolida la transición desde el desarrollo asistido por IA empírico y desordenado hacia una disciplina de ingeniería formal, reproducible y auditable.

### Principales Beneficios Obtenidos:

1. **Cero Desviación de Alcance**: Eliminación del Spec Drift mediante el control de Allowed Files y los hooks del IDE.
2. **Calidad y Cobertura Certificada**: Trazabilidad matemática 1:1 entre requisitos EARS, escenarios Gherkin y suites de pruebas automatizadas.
3. **Ciberseguridad Integrada en el Diseño**: Detección temprana de secretos, prevención de inyecciones OWASP y remediación de dependencias vulnerables.
4. **Garantía Contractual de SLAs**: Pruebas de carga automáticas que certifican latencias inferiores a 200 ms bajo concurrencia sostenida.
5. **Preparación Regulatoria Inmediata**: Dossiers de auditoría en PDF generados con un solo clic, listos para certificación internacional ante entes gubernamentales y comités de cumplimiento.
""")

content_full = "\n".join(sections).strip() + "\n"

# Lint validation
violations = lint_md.lint_markdown(content_full)
print(f"Total violations found: {len(violations)}")
for vi in violations:
    print(f"  {vi}")

if len(violations) == 0:
    target_ws = "LIBRO_BLANCO_Y_DOCUMENTO_MAESTRO_FRAMEWORK_SDD_V65.md"
    with open(target_ws, "w", encoding="utf-8") as f:
        f.write(content_full)
    print(f"Archivo guardado exitosamente en workspace: {target_ws} ({len(content_full)} caracteres)")
    
    # Tambien actualizar DOCUMENTO_MAESTRO_PROYECTO_SDD_V65.md para mantener consistencia
    target_doc_maestro = "DOCUMENTO_MAESTRO_PROYECTO_SDD_V65.md"
    with open(target_doc_maestro, "w", encoding="utf-8") as f:
        f.write(content_full)
    print(f"Archivo actualizado exitosamente en workspace: {target_doc_maestro}")
else:
    print("Corregir violaciones antes de guardar.")
    exit(1)
