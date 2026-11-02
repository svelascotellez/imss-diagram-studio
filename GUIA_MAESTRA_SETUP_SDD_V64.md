# Guía Maestra de Inicialización y Operación: SDD Framework v6.4 (v6.e)

> **Manual Operativo Paso a Paso para la Creación de Proyectos, Verificación de SLAs k6 y Gobernanza de Código**
> **Versión:** 6.4 (v6.e)
> **Fecha:** 2026-10-30
> **Compatibilidad:** Windows 10/11, PowerShell 5.1+, PowerShell 7+, Linux/macOS (bash/pwsh)

---

## 1. Introducción y Novedades de la Versión 6.4 (v6.e)

La versión **6.4 (v6.e) - Performance & SLA Edition** introduce capacidades avanzadas de modelado de rendimiento y resiliencia para aplicaciones corporativas:

- **Aduana 9 (Performance & SLA Gate)**: Verificación obligatoria de percentiles de latencia ($P_{95} \le 200\text{ ms}$, $P_{99} \le 500\text{ ms}$) y tasa de error ($0.0\%$) mediante scripts k6 declarativos.
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

### ¿Qué hacer si falla la Aduana 9 ($P_{95} > 200\text{ ms}$)?

1. **Consultas SQL $N+1$**: Inspeccione la capa de infraestructura. Reemplace bucles de consultas individuales por consultas por lotes (`JOIN FETCH` o `WHERE id IN (...)`).
2. **Operaciones Síncronas Bloqueantes**: Asegúrese de utilizar llamadas asíncronas (`async/await`) en todas las operaciones de red y acceso a disco.
3. **Serialización Ineficiente**: Reduzca el tamaño de los payloads eliminando campos no requeridos en los DTOs de respuesta.

### ¿Cómo corregir inconsistencias de formato Markdown?

Ejecute la herramienta de higiene automatizada:

```powershell
.\harness\sdd.ps1 -Action fix-markdown
```

Esta acción audita y corrige de forma automática las 7 reglas de markdownlint (MD009, MD022, MD031, MD032, MD040, MD047, MD058).
