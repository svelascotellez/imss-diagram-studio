# Guía Maestra de Inicialización y Operación: SDD Framework v6.5

> **Manual Operativo Paso a Paso para la Creación de Proyectos, Verificación de SLAs k6 y Generación de Expedientes Regulatorios PDF**
> **Versión:** 6.5
> **Fecha:** 2026-10-30
> **Compatibilidad:** Windows 10/11, PowerShell 5.1+, PowerShell 7+, Linux/macOS (bash/pwsh)

---

## 1. Introducción y Novedades de la Versión 6.5

La versión **6.5 - Regulatory & Compliance Edition** incorpora el **Pilar 10: Expediente Regulatorio y Compliance PDF**, brindando a los equipos de desarrollo las siguientes capacidades:

- **Dossier de Auditoría Oficial en PDF y HTML**: Compilación automatizada de especificaciones EARS, escenarios BDD, sellos criptográficos SHA-256, dictamen de seguridad SAST y reportes de rendimiento k6.
- **Acreditación Normativa Internacional**: Mapeo directo de evidencia contra ISO/IEC 27001:2022, FDA 21 CFR Part 11, SOC 2 Type II, HIPAA Security Rule y CMMI Nivel 5.
- **Acción Unificada en el Arnés**: Nuevo comando `.\harness\sdd.ps1 -Action export-compliance` con soporte para formatos `-Format pdf|html|md|all` y apertura automática `-Open`.
- **Compilador Chromium Headless Integrado**: Utiliza Microsoft Edge o Google Chrome instalados en el sistema operativo para generar PDFs vectoriales de alta resolución sin requerir librerías externas pesadas.
- **Skill Canónica #20 (`sdd-compliance`)**: Agente especialista en auditoría regulatoria ubicado en `.agents/skills/sdd-compliance/SKILL.md`.
- **Integración Completa en CI/CD**: Generación automática y almacenamiento de expedientes regulatorios en GitHub Actions y GitLab CI.

---

## 2. Requisitos Previos e Instaladores Disponibles

### Requisitos del Sistema

1. **PowerShell**: Versión 5.1 (incluida en Windows 10/11) o PowerShell Core 7+.
2. **Git**: Versión 2.30 o superior en el PATH del sistema.
3. **Navegador Web para Generación de PDF (Edge o Chrome)**:
   - Microsoft Edge (preinstalado en Windows 10 y 11) o Google Chrome.
   - Si no se detecta ningún navegador headless, el arnés emite el expediente en HTML interactivo con estilos de impresión `@media print` para exportación manual (Ctrl+P).
4. **k6 (Opcional)**: Para ejecución de benchmarks de rendimiento en vivo.

### Scripts de Inicialización Disponibles

- `setup-sdd-project-v65.ps1`: Inicializador nativo en PowerShell.
- `setup-sdd-project-v65.py`: Inicializador multiplataforma en Python.

---

## 3. Guía Paso a Paso para Inicializar un Proyecto

### Paso 1: Ejecutar el Inicializador

Abra una consola de PowerShell en la carpeta raíz y ejecute:

```powershell
powershell -ExecutionPolicy Bypass -File .\setup-sdd-project-v65.ps1 -ProjectName "MiSistemaRegulado" -Stack "python" -AutoLaunch "none"
```

Parámetros admitidos:

- `-ProjectName <string>`: Nombre del directorio de trabajo a crear.
- `-Stack <string>`: Stack tecnológico (`python`, `typescript`, `csharp`, `golang`, `flutter`, `java`).
- `-GitInit`: Inicializa automáticamente un repositorio Git y configura el hook pre-commit.
- `-AutoLaunch <auto|ide|cli|none>`: Controla el lanzamiento del agente Antigravity tras la inicialización.

### Paso 2: Verificar la Estructura Generada

```text
MiSistemaRegulado/
├── .agents/
│   └── skills/                   # 20 Skills Canonicas (incluyendo sdd-compliance)
├── .github/
│   └── workflows/
│       └── sdd-gate.yml          # Pipeline GitHub Actions con etapa compliance
├── .gitlab-ci.yml                # Pipeline GitLab CI con etapa compliance
├── .specify/
│   ├── harness-config.json       # Configuracion del proyecto y Allowed Files
│   ├── memory/                   # Constitucion inmutable
│   └── templates/                # Plantillas EARS, BDD y planes tecnicos
├── docs/                         # Guias de usuario vivas
├── harness/
│   ├── dashboard.ps1             # Cockpit Dashboard y Servidor DAG
│   ├── export-compliance.ps1     # Generador de Expediente Regulatorio PDF/HTML
│   ├── pr-summary.ps1            # Resumen de PR con Checklist de 9 Aduanas
│   ├── sdd.ps1                   # Arnes de linea de comandos unificado
│   ├── spec-gate.ps1             # Auditor Nonuplo (9 Hard Gates)
│   ├── verify-performance.ps1    # Verificador de Rendimiento k6 (Aduana 9)
│   └── verify-security.ps1       # Verificador de Seguridad SAST y Secretos
├── progress/                     # Reportes de auditoria, PDF y dashboard
├── specs/                        # Especificaciones de funcionalidades (EARS + BDD)
├── tests/
│   └── performance/              # Benchmarks de carga k6
├── CHECKPOINTS.md                # Registro inmutable de firmas criptograficas
└── feature_list.json             # Backlog formal con dependencias y estados
```

---

## 4. Guía Operativa: Generación del Expediente Regulatorio

### Exportación del Expediente Completo del Proyecto

```powershell
# Exporta el dossier en formato PDF oficial
.\harness\sdd.ps1 -Action export-compliance -Format pdf

# Exporta en todos los formatos (PDF, HTML, Markdown) y lo abre inmediatamente
.\harness\sdd.ps1 -Action export-compliance -Format all -Open
```

Los artefactos resultantes se generan en:

- `progress/compliance_dossier.pdf`: Documento PDF oficial de alta resolución.
- `progress/compliance_dossier.html`: Documento web con diseño de carátula ejecutiva y estilos de impresión.
- `progress/compliance_dossier.md`: Resumen ejecutivo en Markdown.

### Exportación Enfocada en una Funcionalidad Específica

Para generar el expediente técnico de una funcionalidad particular:

```powershell
.\harness\sdd.ps1 -Action export-compliance -FeatureId feat-01 -Format all -Open
```

El arnés compilará `specs/feat-01/spec.md`, `scenarios.feature`, `plan.md`, `docs/user_guide_feat-01.md`, su historial de firmas criptográficas y sus reportes de seguridad y rendimiento.

---

## 5. Visualización en el Cockpit Web Dashboard

Para visualizar el avance del backlog y el estado de las compuertas de auditoría:

```powershell
# Genera el reporte estatico
.\harness\sdd.ps1 -Action dashboard -NoBrowser

# Abre el Cockpit interactivo con servidor en vivo
.\harness\sdd.ps1 -Action dashboard -Live -Port 8080
```

El Cockpit incluye un botón de comando rápido para generar el expediente regulatorio con un solo clic.

---

## 6. Resolución de Problemas Frecuentes (FAQ)

### ¿Cómo solucionar la falta de un navegador headless para generar PDF?

Si el sistema no cuenta con Edge o Chrome en las rutas estándar, el arnés genera automáticamente el archivo HTML en `progress/compliance_dossier.html`. Puede abrirlo en cualquier navegador web moderno y presionar `Ctrl + P` seleccionando la opción **"Guardar como PDF"**.

### ¿Por qué aparece "Pendiente" en las firmas criptográficas del expediente?

Las firmas de aprobación (`approval_hash`) y cierre (`completion_hash`) se generan al ejecutar:

1. `.\harness\sdd.ps1 -Action approve -FeatureId <id>`: Al finalizar el diseño de la especificación.
2. `.\harness\sdd.ps1 -Action complete -FeatureId <id>`: Tras superar las 9 compuertas del Auditor Nónuplo.

Asegúrese de seguir el flujo formal de trabajo para que el expediente refleje las firmas SHA-256 inmutables.
