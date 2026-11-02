import os
import lint_md

doc_maestro_content = """# Documento Maestro: Metodología SDD v6.4 (v6.e) - Performance & SLA Edition

> **Framework de Desarrollo Guiado por Especificaciones (Spec-Driven Development + BDD + Clean Architecture + Secure Coding + Cockpit Web + CI/CD Governance + k6 SLA Gate)**
> **Autor:** Salvador Velasco & Antigravity (Google DeepMind Team)
> **Versión:** 6.4 (v6.e)
> **Fecha:** 2026-10-30
> **Estado:** Aprobado para Producción Corporativa

---

## 1. Resumen Ejecutivo y Visión General v6.4 (v6.e)

La versión **6.4 (v6.e)** de la metodología SDD institucionaliza la **Compuerta de Rendimiento y Resiliencia SLA (k6 Benchmark)** como la **Novena Aduana Obligatoria (Aduana 9 / SLA Gate)** del marco de gobernanza.

En el desarrollo asistido por modelos de inteligencia artificial, es frecuente que los agentes de codificación generen soluciones que satisfacen al 100% las especificaciones funcionales y pruebas unitarias/BDD, pero introducen inadvertidamente cuellos de botella severos: consultas de base de datos $N+1$, serialización JSON ineficiente, saturación de hilos o algoritmos con complejidad $O(N^2)$.

SDD v6.4 resuelve de raíz este riesgo integrando una compuerta matemática inmutable: ninguna funcionalidad puede sellarse ni promoverse a producción si no demuestra que su latencia en el percentil 95 ($P_{95}$) es inferior o igual a 200 ms y su tasa de error bajo concurrencia es estrictamente 0.0%.

### Los 9 Pilares Fundamentales de SDD v6.4

```mermaid
flowchart TD
    P1["1. Especificacion Viva (EARS)"] --> P2["2. BDD Riguroso (Gherkin 1:1)"]
    P2 --> P3["3. Clean Architecture Poliglota"]
    P3 --> P4["4. Integridad Criptografica (SHA-256)"]
    P4 --> P5["5. Control de Tareas (Fase 1-6)"]
    P5 --> P6["6. Secure Coding & OWASP"]
    P6 --> P7["7. Cockpit Web & DAG Viewer"]
    P7 --> P8["8. Gobernanza CI/CD Cloud"]
    P8 --> P9["9. Compuerta de Rendimiento k6 (Aduana 9)"]
```

1. **Pilar 1: Especificación Viva (EARS y Allowed Files)**: Reglas declarativas con sintaxis EARS (`[Ubiquitous]`, `[Event-driven]`, `[State-driven]`) y delimitación estricta de archivos permitidos contra el Spec Drift.
2. **Pilar 2: BDD Riguroso (Gherkin 1:1)**: Trazabilidad bidireccional exacta entre criterios de aceptación EARS y escenarios ejecutables en `specs/<feature>/scenarios.feature`.
3. **Pilar 3: Clean Architecture Políglota**: Aislamiento estricto de capas (Dominio, Aplicación, Presentación e Infraestructura) verificado mediante regex de importación para Python, TypeScript, C#, Go y Dart.
4. **Pilar 4: Integridad Criptográfica (SHA-256)**: Sello digital HMAC/SHA-256 generado al aprobar la especificación (`approval_hash`) y al sellar el cierre (`completion_hash`).
5. **Pilar 5: Control de Tareas y Fases**: Ejecución ordenada en 6 fases operativas sin saltos de disciplina.
6. **Pilar 6: Secure Coding & Threat Modeling**: Detección de secretos (TruffleHog), modelado de amenazas STRIDE y auditoría de vulnerabilidades conocidas (pip-audit / npm audit).
7. **Pilar 7: Cockpit Web Dashboard & DAG Suite**: Panel interactivo HTML5 en tiempo real con visor de dependencias TopoSort y métricas ejecutivas.
8. **Pilar 8: Gobernanza de Integración Continua (CI/CD)**: Pipelines listos para producción en GitHub Actions (`.github/workflows/sdd-gate.yml`) y GitLab CI (`.gitlab-ci.yml`).
9. **Pilar 9: Compuerta de Rendimiento y Resiliencia SLA (k6 Benchmark)**: Auditoría automatizada de latencia percentil ($P_{95} \\le 200\\text{ ms}$, $P_{99} \\le 500\\text{ ms}$) y tasa de error nula ($0.0\\%$) bajo carga sostenida.

---

## 2. El Auditor Nónuplo: Las 9 Hard Gates

El script de aduana `harness/spec-gate.ps1` evoluciona del Auditor Óctuplo al **Auditor Nónuplo (9 Hard Gates)**. Cada compuerta actúa como un candado que detiene la integración ante la menor anomalía:

| Aduana | Nombre de Compuerta | Tipo de Verificación | Condición de Aprobación |
| :--- | :--- | :--- | :--- |
| **Gate 1** | **Allowed Files & Anti-Drift** | Integridad de Repositorio | Solo archivos declarados en `plan.md` fueron modificados o commiteados. |
| **Gate 2** | **Cobertura BDD 1:1** | Trazabilidad Funcional | Cada EARS `AC-x.x` tiene correspondencia exacta con escenarios Gherkin y tests. |
| **Gate 3** | **Clean Architecture Políglota** | Pureza Arquitectónica | Capa Dominio con 0 dependencias externas; Presentación sin acoplamiento a Infra. |
| **Gate 4** | **Firma Criptográfica Approval** | Validez de Especificación | Hash SHA-256 de `spec.md`, `scenarios.feature` y `plan.md` coincide con el sello. |
| **Gate 5** | **Completitud de Tareas** | Progreso Estructurado | Todas las tareas de `tasks.md` están marcadas `[x]` sin pendientes. |
| **Gate 6** | **Guía de Usuario Viva** | Documentación de Entrega | `docs/user_guide_<feature>.md` existe, tiene ejemplos y cumple markdownlint. |
| **Gate 7** | **Candado Inmutable Completion** | Sellado de Cierre | Hash SHA-256 inmutable emitido y registrado en `feature_list.json` y `CHECKPOINTS.md`. |
| **Gate 8** | **Seguridad OWASP & Secret Scan** | Ciberseguridad Defensiva | Cero credenciales hardcodeadas, cero inyecciones SQL y 0 CVEs High/Critical. |
| **Gate 9** | **Performance & SLA Gate (k6)** | Rendimiento y Resiliencia | Latencia $P_{95} \\le 200\\text{ ms}$, $P_{99} \\le 500\\text{ ms}$ y tasa de fallos $= 0.0\\%$. |

---

## 3. Arquitectura y Ciclo de Vida de la Aduana 9 (k6)

La Aduana 9 evalúa las propiedades de tiempo de respuesta y concurrencia del software bajo un esquema declarativo:

```mermaid
sequenceDiagram
    autonumber
    actor Dev as Desarrollador / Agente AI
    participant Arn as Arnés SDD (sdd.ps1)
    participant Perf as verify-performance.ps1
    participant K6 as Motor k6 / Runner CI
    participant Rep as Reporte (JSON/MD)
    participant Gate as spec-gate.ps1

    Dev->>Arn: .\\harness\\sdd.ps1 -Action verify-performance -FeatureId feat-01
    Arn->>Perf: Ejecuta script de rendimiento
    Perf->>Perf: Valida existencia y estructura de tests/performance/feat-01.js
    alt k6 CLI Instalado en Local / CI Runner
        Perf->>K6: k6 run --summary-export progress/k6_summary_raw.json
        K6-->>Perf: Telemetria (P95, P99, Error Rate, VUs)
    else k6 CLI No Detectado
        Perf->>Perf: Auditoria Estatica Pre-flight de Umbrales Declarativos
    end
    Perf->>Rep: Emite progress/performance_report.json y .md
    Perf-->>Arn: Codigo de Salida 0 (SLA Aprobado)
    Dev->>Arn: .\\harness\\sdd.ps1 -Action complete -FeatureId feat-01
    Arn->>Gate: Ejecuta Auditor Nonuplo (Check 1/9 a 9/9)
    Gate->>Gate: Verifica Aduana 9 (k6 Benchmark)
    Gate-->>Arn: 9 Aduanas Aprobadas -> Emite Completion Seal
```

### Especificación Declarativa del Benchmark en k6

Cada funcionalidad cuenta con un archivo de prueba en `tests/performance/<feature>.js` o utiliza el benchmark global `tests/performance/k6_benchmark.js`:

```javascript
// tests/performance/feat-01.js - Benchmark SLA Declarativo SDD v6.4
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,
  duration: '10s',
  thresholds: {
    // SLA Gate: 95% de solicitudes por debajo de 200ms
    http_req_duration: ['p(95)<200', 'p(99)<500'],
    // SLA Gate: Tasa de error estricta al 0%
    http_req_failed: ['rate==0'],
  },
};

export default function () {
  const res = http.get('http://localhost:8080/health');
  check(res, {
    'status is 200': (r) => r.status === 200,
    'latency below 200ms': (r) => r.timings.duration < 200,
  });
  sleep(1);
}
```

### Formato del Reporte Estructurado (`progress/performance_report.json`)

```json
{
  "version": "6.4",
  "feature_id": "feat-01",
  "target_script": "tests/performance/feat-01.js",
  "status": "PASSED",
  "sla_thresholds": {
    "latency_p95_ms": 200,
    "latency_p99_ms": 500,
    "error_rate_pct": 0.0,
    "vus": 10,
    "duration": "10s"
  },
  "timestamp": "2026-10-30T17:09:30"
}
```

---

## 4. Catálogo Canónico de las 19 Skills de Inteligencia Artificial

Antigravity IDE y sus agentes interactúan con el proyecto mediante 19 habilidades especializadas ubicadas en `.agents/skills/`:

| # | Skill Canónica | Rol Operativo | Entregables y Responsabilidades |
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

---

## 5. Matriz de Comandos del Arnés (`harness/sdd.ps1`)

El arnés centraliza la operación del desarrollador humano y los agentes mediante comandos unificados:

```powershell
# ==============================================================================
# COMANDOS DE RENDIMIENTO Y RESILIENCIA (v6.4)
# ==============================================================================
# Ejecuta la compuerta de rendimiento con parametros por defecto (10 VUs, 10s, P95 <= 200ms)
.\harness\sdd.ps1 -Action verify-performance

# Ejecuta para una funcionalidad especifica con umbral estricto
.\harness\sdd.ps1 -Action verify-performance -FeatureId feat-01 -Vus 20 -Duration "15s" -ThresholdP95 150

# Invocacion directa al verificador del arnes
powershell -ExecutionPolicy Bypass -File .\harness\verify-performance.ps1 -ThresholdP95 200

# ==============================================================================
# COCKPIT WEB DASHBOARD & VISOR DAG (v6.3)
# ==============================================================================
# Genera el dashboard estatico
.\harness\sdd.ps1 -Action dashboard -NoBrowser

# Inicia el Cockpit interactivo con servidor en vivo y recarga automatica
.\harness\sdd.ps1 -Action dashboard -Live -Port 8080

# ==============================================================================
# GOBERNANZA CI/CD Y REPORTES DE PR (v6.2)
# ==============================================================================
# Inicializa o refresca pipelines CI/CD
.\harness\sdd.ps1 -Action init-cicd

# Genera el resumen enriquecido de Pull Request con el checklist de 9 Aduanas
.\harness\sdd.ps1 -Action pr-summary

# ==============================================================================
# CIBERSEGURIDAD DEFENSIVA (v6.1)
# ==============================================================================
# Ejecuta escaneo de secretos y dependencias vulnerables
.\harness\sdd.ps1 -Action verify-security

# ==============================================================================
# CICLO DE VIDA DE FUNCIONALIDADES (SDD CORE)
# ==============================================================================
# Consulta el estado del backlog
.\harness\sdd.ps1 -Action status

# Crea una nueva funcionalidad
.\harness\sdd.ps1 -Action create -FeatureId feat-02 -Title "Catalogo de Productos"

# Sella la aprobacion de especificaciones (Approval Seal)
.\harness\sdd.ps1 -Action approve -FeatureId feat-01

# Ejecuta la auditoria nonupla y sella el cierre definitivo (Completion Seal)
.\harness\sdd.ps1 -Action complete -FeatureId feat-01

# Higiene y correccion automatica de markdown
.\harness\sdd.ps1 -Action fix-markdown
```

---

## 6. Integración en Pipelines CI/CD y Cockpit Dashboard

### GitHub Actions (`.github/workflows/sdd-gate.yml`)

El pipeline de GitHub Actions incorpora el paso de k6 SLA Benchmark Gate:

```yaml
- name: Application Security Audit (SAST & Secret Scanning)
  shell: powershell
  run: |
    .\harness\sdd.ps1 -Action verify-security

- name: Performance & SLA Benchmark Gate (k6)
  shell: powershell
  run: |
    .\harness\sdd.ps1 -Action verify-performance

- name: Run Test Suite & Build Verification
  shell: powershell
  run: |
    .\harness\sdd.ps1 -Action verify -FeatureId ${{ env.ACTIVE_FEATURE }}

- name: SDD Spec-Gate Nonuple Audit
  shell: powershell
  run: |
    powershell -ExecutionPolicy Bypass -File .\harness\spec-gate.ps1 -FeatureId ${{ env.ACTIVE_FEATURE }}
```

### Telemetría de Rendimiento en el Cockpit Dashboard

El archivo `progress/sdd_dashboard.html` visualiza:

1. **Card de Métricas de 9 Aduanas**: Indicador 9/9 con estado en tiempo real.
2. **Tarjeta de la Aduana 9 (Performance & SLA Gate)**: Muestra el estado del benchmark k6, latencia $P_{95}$, tasa de errores y concurrencia evaluada.
3. **Píldora de Comando Rápido**: Permite copiar y ejecutar al instante `.\harness\sdd.ps1 -Action verify-performance`.

---

## 7. Diagrama de Interacción Humano-Agente-Arnés v6.4

```mermaid
sequenceDiagram
    autonumber
    actor H as Desarrollador Humano
    participant A as Agente de IA (Antigravity)
    participant Hrn as Arnes SDD (sdd.ps1)
    participant Sec as verify-security.ps1
    participant Perf as verify-performance.ps1
    participant Gate as spec-gate.ps1
    participant CI as GitHub Actions / GitLab CI

    H->>A: "Implementa el modulo de autenticacion OAuth2"
    A->>Hrn: .\\harness\\sdd.ps1 -Action create -FeatureId feat-auth
    A->>A: Redacta spec.md, scenarios.feature y plan.md
    H->>Hrn: .\\harness\\sdd.ps1 -Action approve -FeatureId feat-auth
    Hrn-->>H: Approval Seal emitido (SHA-256 inmutable)
    A->>A: Implementa codigo en capa domain, application e infra
    A->>Sec: .\\harness\\sdd.ps1 -Action verify-security
    Sec-->>A: [OK] Cero secretos, cero CVEs criticos (Aduana 8)
    A->>Perf: .\\harness\\sdd.ps1 -Action verify-performance
    Perf-->>A: [OK] Latencia P95 <= 200ms, Error Rate = 0% (Aduana 9)
    A->>Gate: .\\harness\\sdd.ps1 -Action complete -FeatureId feat-auth
    Gate-->>H: Auditor Nonuplo superado exitosamente (9/9 Gates)
    H->>CI: git push origin feat-auth -> Pull Request
    CI-->>H: CI/CD Gate verde (9 Aduanas certificadas en cloud)
```

---

## 8. Conclusiones y Certificación de Versión

La versión **6.4 (v6.e) - Performance & SLA Edition** eleva el estándar industrial del desarrollo de software asistido por inteligencia artificial. Mediante la sinergia entre especificaciones EARS, BDD, Clean Architecture, ciberseguridad defensiva y compuertas matemáticas de rendimiento con k6, los equipos de ingeniería logran entregar software corporativo robusto, resiliente y de alto desempeño.
"""

guia_setup_content = """# Guía Maestra de Inicialización y Operación: SDD Framework v6.4 (v6.e)

> **Manual Operativo Paso a Paso para la Creación de Proyectos, Verificación de SLAs k6 y Gobernanza de Código**
> **Versión:** 6.4 (v6.e)
> **Fecha:** 2026-10-30
> **Compatibilidad:** Windows 10/11, PowerShell 5.1+, PowerShell 7+, Linux/macOS (bash/pwsh)

---

## 1. Introducción y Novedades de la Versión 6.4 (v6.e)

La versión **6.4 (v6.e) - Performance & SLA Edition** introduce capacidades avanzadas de modelado de rendimiento y resiliencia para aplicaciones corporativas:

- **Aduana 9 (Performance & SLA Gate)**: Verificación obligatoria de percentiles de latencia ($P_{95} \\le 200\\text{ ms}$, $P_{99} \\le 500\\text{ ms}$) y tasa de error ($0.0\\%$) mediante scripts k6 declarativos.
- **Auditor Nónuplo Reforzado**: El script `harness/spec-gate.ps1` valida de forma estricta las 9 compuertas de gobernanza.
- **Acción Unificada en el Arnés**: Nuevo comando `.\harness\sdd.ps1 -Action verify-performance` con soporte de parámetros de concurrencia (`-Vus`), duración (`-Duration`) y umbral (`-ThresholdP95`).
- **Skill Canónica #19 (`sdd-performance`)**: Instrucciones completas para que los agentes de IA modelen benchmarks de carga y solucionen cuellos de botella.
- **Checklist de 9 Aduanas en Pull Requests**: Integrado en `harness/pr-summary.ps1` y los pipelines de GitHub Actions y GitLab CI.
- **Cockpit Web con Métricas de SLAs**: Visualización instantánea del estado de la Aduana 9 en `progress/sdd_dashboard.html`.

---

## 2. Requisitos Previos e Instalación

### Requisitos del Sistema

1. **PowerShell**: Versión 5.1 (incluida en Windows 10/11) o PowerShell Core 7+.
2. **Git**: Versión 2.30 o superior instalada y en el PATH del sistema.
3. **k6 (Opcional pero recomendado para pruebas locales)**:
   - Descarga directa o mediante gestor de paquetes: `winget install k6` o `choco install k6`.
   - *Nota de compatibilidad*: Si `k6` no está instalado en el equipo local, el arnés ejecuta una auditoría estática de umbrales declarativos y certifica el script para los runners cloud de CI/CD.

### Scripts de Inicialización Disponibles

El framework puede inicializarse mediante dos instaladores equivalentes:

- `setup-sdd-project-v64.ps1`: Inicializador nativo de PowerShell (recomendado en entornos Windows).
- `setup-sdd-project-v64.py`: Inicializador políglota en Python.

---

## 3. Guía Paso a Paso para Inicializar un Proyecto

### Paso 1: Ejecutar el Instalador

Abra una consola de PowerShell en la carpeta raíz donde desea crear su proyecto y ejecute:

```powershell
# Inicializacion con nombre de proyecto y stack tecnologico especifico
powershell -ExecutionPolicy Bypass -File .\setup-sdd-project-v64.ps1 -ProjectName "MiProyectoCorporativo" -Stack "python" -AutoLaunch "none"
```

Parámetros admitidos por `setup-sdd-project-v64.ps1`:

- `-ProjectName <string>`: Nombre del directorio de trabajo a crear.
- `-Stack <string>`: Stack del proyecto (`python`, `typescript`, `csharp`, `golang`, `flutter`, `java`).
- `-GitInit`: Inicializa automáticamente un repositorio Git y configura el hook pre-commit.
- `-AutoLaunch <auto|ide|cli|none>`: Controla el lanzamiento del agente Antigravity tras la inicialización.

### Paso 2: Verificar la Estructura Generada

El inicializador genera la siguiente arquitectura de archivos:

```text
MiProyectoCorporativo/
├── .agents/
│   └── skills/                   # 19 Skills Canonicas (incluyendo sdd-performance)
├── .github/
│   └── workflows/
│       └── sdd-gate.yml          # Pipeline GitHub Actions con etapa k6 SLA Gate
├── .gitlab-ci.yml                # Pipeline GitLab CI con etapa performance
├── .specify/
│   ├── harness-config.json       # Configuracion del proyecto y Allowed Files
│   ├── memory/                   # Constitucion inmutable
│   └── templates/                # Plantillas EARS, BDD y planes tecnicos
├── docs/                         # Guias de usuario vivas
├── harness/
│   ├── dashboard.ps1             # Cockpit Dashboard y Servidor DAG
│   ├── pr-summary.ps1            # Resumen de PR con Checklist de 9 Aduanas
│   ├── sdd.ps1                   # Arnes de linea de comandos unificado
│   ├── spec-gate.ps1             # Auditor Nonuplo (9 Hard Gates)
│   ├── verify-performance.ps1    # Verificador de Rendimiento k6 (Aduana 9)
│   └── verify-security.ps1       # Verificador de Seguridad SAST y Secretos
├── progress/                     # Reportes de auditoria y dashboard
├── specs/                        # Especificaciones de funcionalidades (EARS + BDD)
├── tests/
│   └── performance/              # Scripts de Benchmark k6
│       └── k6_benchmark.js       # Benchmark global de rendimiento
├── CHECKPOINTS.md                # Registro inmutable de firmas criptograficas
└── feature_list.json             # Backlog formal con dependencias y estados
```

---

## 4. Flujo Operativo: De la Especificación a la Aduana 9

### Fase 1: Creación de la Funcionalidad

```powershell
.\harness\sdd.ps1 -Action create -FeatureId feat-01 -Title "Autenticacion JWT"
```

El arnés creará la carpeta `specs/feat-01/` con plantillas para:

- `spec.md`: Requisitos funcionales con sintaxis EARS.
- `scenarios.feature`: Escenarios BDD en Gherkin.
- `plan.md`: Arquitectura limpia y lista de `Allowed Files`.

### Fase 2: Aprobación Humana y Firma Criptográfica

Una vez refinada la especificación con el agente, el desarrollador humano otorga su aprobación formal:

```powershell
.\harness\sdd.ps1 -Action approve -FeatureId feat-01
```

El arnés calcula el hash SHA-256 de la tríada documental y genera el `approval_hash` inmutable.

### Fase 3: Implementación y Pruebas Unitarias/BDD

El agente y el desarrollador construyen el código fuente respetando las capas de Clean Architecture y la lista de `Allowed Files`.

### Fase 4: Auditoría de Seguridad (Aduana 8)

```powershell
.\harness\sdd.ps1 -Action verify-security
```

Valida que no existan secretos expuestos ni dependencias con CVEs críticos.

### Fase 5: Auditoría de Rendimiento y SLAs k6 (Aduana 9)

```powershell
# Ejecucion basica del benchmark de rendimiento
.\harness\sdd.ps1 -Action verify-performance -FeatureId feat-01

# Ejecucion con parametros personalizados
.\harness\sdd.ps1 -Action verify-performance -FeatureId feat-01 -Vus 20 -Duration "15s" -ThresholdP95 150
```

El verificador generará:

- `progress/performance_report.json`: Datos estructurados para observabilidad.
- `progress/performance_report.md`: Resumen ejecutivo en Markdown.

### Fase 6: Auditoría Nónupla y Cierre Definitivo

```powershell
.\harness\sdd.ps1 -Action complete -FeatureId feat-01
```

El Auditor Nónuplo (`spec-gate.ps1`) ejecuta en secuencia las 9 compuertas. Si todas aprueban:

1. Se genera el `completion_hash` SHA-256 inmutable.
2. El estado de la funcionalidad pasa a `done` en `feature_list.json`.
3. Se actualiza `CHECKPOINTS.md`.

---

## 5. Visualización Ejecutiva: Cockpit Web Dashboard

Para visualizar el avance del backlog, el grafo DAG y el estado de las 9 compuertas:

```powershell
# Genera el reporte estatico
.\harness\sdd.ps1 -Action dashboard -NoBrowser

# Abre el Cockpit interactivo con servidor en vivo
.\harness\sdd.ps1 -Action dashboard -Live -Port 8080
```

Abra su navegador en `http://localhost:8080` para interactuar con la consola visual.

---

## 6. Resolución de Problemas Frecuentes (FAQ)

### ¿Qué hacer si falla la Aduana 9 ($P_{95} > 200\\text{ ms}$)?

1. **Consultas SQL $N+1$**: Inspeccione la capa de infraestructura. Reemplace bucles de consultas individuales por consultas por lotes (`JOIN FETCH` o `WHERE id IN (...)`).
2. **Operaciones Síncronas Bloqueantes**: Asegúrese de utilizar llamadas asíncronas (`async/await`) en todas las operaciones de red y acceso a disco.
3. **Serialización Ineficiente**: Reduzca el tamaño de los payloads eliminando campos no requeridos en los DTOs de respuesta.

### ¿Cómo corregir inconsistencias de formato Markdown?

Ejecute la herramienta de higiene automatizada:

```powershell
.\harness\sdd.ps1 -Action fix-markdown
```

Esta acción audita y corrige de forma automática las 7 reglas de markdownlint (MD009, MD022, MD031, MD032, MD040, MD047, MD058).
"""

# Lint validation
v_doc = lint_md.lint_markdown(doc_maestro_content)
print(f"Linting DOCUMENTO_MAESTRO_PROYECTO_SDD_V64.md: {len(v_doc)} violations")
for vi in v_doc:
    print(f"  {vi}")

v_guia = lint_md.lint_markdown(guia_setup_content)
print(f"Linting GUIA_MAESTRA_SETUP_SDD_V64.md: {len(v_guia)} violations")
for vi in v_guia:
    print(f"  {vi}")

if len(v_doc) == 0 and len(v_guia) == 0:
    # Write to workspace
    with open("DOCUMENTO_MAESTRO_PROYECTO_SDD_V64.md", "w", encoding="utf-8") as f:
        f.write(doc_maestro_content)
    print("DOCUMENTO_MAESTRO_PROYECTO_SDD_V64.md written to workspace.")

    with open("GUIA_MAESTRA_SETUP_SDD_V64.md", "w", encoding="utf-8") as f:
        f.write(guia_setup_content)
    print("GUIA_MAESTRA_SETUP_SDD_V64.md written to workspace.")
else:
    print("Fix violations before writing!")
    exit(1)
