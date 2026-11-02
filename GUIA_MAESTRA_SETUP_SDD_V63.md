# Guia Maestra Definitiva: Arquitectura, Artefactos y Gobierno de Setup SDD (v6.3)

## Enterprise Security, CI/CD Governance & Cockpit DAG Suite Edition: Spec-Driven Development + BDD + Clean Architecture + Secure Coding + Interactive DAG Viewer + Live Server + Cloud PR Gates

---

## 1. Introduccion y Fundamentos Metodologicos

El script `setup-sdd-project-v63.ps1` (y su homologo generador `setup-sdd-project-v63.py`) es el inicializador oficial de entornos de desarrollo gobernados bajo la metodologia **Spec-Driven Development (SDD v6.3)**. Configura en segundos un ecosistema corporativo dotado de aislamiento arquitectonico, control criptografico Humano en el Bucle (HITL), escaneo estatico de ciberseguridad defensiva (STRIDE/OWASP), observabilidad ejecutiva en tiempo real mediante un Cockpit Web y Visor DAG interactivo con servidor en vivo (`-Live`), y compuertas de gobernanza en la nube para GitHub Actions y GitLab CI.

### Los 8 Pilares de SDD v6.3

1. **Spec-First & Perimetro Cerrado (Anti-Drift)**: Especificaciones EARS inmutables y lista blanca de archivos (`allowed_files`).
2. **TDD/BDD Invertido (Rojo-Verde-Refactor)**: Pruebas Given-When-Then antes de cualquier codigo de produccion.
3. **Clean Architecture Poliglota**: Aislamiento total del Dominio respecto a infraestructura y librerias externas.
4. **Control Criptografico HITL**: Sellos SHA-256 de aprobacion y complecion verificados matematicamente.
5. **Auditor Octuple Reforzado**: 8 aduanas automaticas ejecutadas por `harness/spec-gate.ps1`.
6. **Ciberseguridad Defensiva**: Escaneo SAST con `harness/verify-security.ps1` y modelado de amenazas STRIDE.
7. **Cockpit Ejecutivo & Visor DAG Interactivo**: Servidor HTTP en vivo con auto-recarga, pan/zoom, orientacion dinamica (LR/TD) y auditor SHA-256 en navegador.
8. **Gobernanza Cloud CI/CD**: Automatizacion de compuertas en Pull Requests mediante GitHub Actions y GitLab CI.

---

## 2. Mapa Completo del Arbol de Directorios y Archivos

Al ejecutar el inicializador, la estructura resultante en el repositorio es la siguiente:

```text
mi-proyecto/
|-- .agents/
|   |-- hooks.json                       # Configuracion de ganchos del IDE
|   +-- skills/                          # 18 Skills Canonicas
|       |-- sdd-orchestrator/SKILL.md    # Orquestador del bucle SDD
|       |-- sdd-onboard/SKILL.md         # Entrevista y configuracion inicial
|       |-- sdd-constitution/SKILL.md    # Cumplimiento de principios constitucionales
|       |-- sdd-specify/SKILL.md         # Especificaciones EARS y STRIDE
|       |-- sdd-clarify/SKILL.md         # Preguntas de resolucion de dudas
|       |-- sdd-ui-ux/SKILL.md           # Heuristica de interfaces de usuario
|       |-- sdd-design-system/SKILL.md   # Tokens de diseno accesibles WCAG
|       |-- sdd-preview-design/SKILL.md  # Wireframes y prototipos visuales
|       |-- sdd-plan/SKILL.md            # Planificacion en capas Clean Architecture
|       |-- sdd-tasks/SKILL.md           # Tareas atomicas de implementacion
|       |-- sdd-implement/SKILL.md       # Ciclo Rojo-Verde-Refactor
|       |-- sdd-user-guide/SKILL.md      # Documentacion para el usuario final
|       |-- sdd-validate/SKILL.md        # Verificacion con Auditor Octuple
|       |-- sdd-change-spec/SKILL.md     # Modificacion controlada de especificaciones
|       |-- sdd-reverse-spec/SKILL.md    # Ingenieria inversa de codigo existente
|       |-- sdd-secure-coding/SKILL.md   # SAST, sinks y OWASP Top 10
|       |-- sdd-dashboard/SKILL.md       # Cockpit interactivo y servidor HTTP Live
|       +-- sdd-cicd/SKILL.md            # Pipelines de CI/CD y resumenes de PR
|-- .github/workflows/
|   +-- sdd-gate.yml                     # Pipeline CI para GitHub Actions
|-- .gitlab-ci.yml                       # Pipeline CI para GitLab CI
|-- .specify/
|   |-- harness-config.json              # Metadatos del stack y directorios
|   |-- design-system/design-tokens.json # Paleta de colores y tokens accesibles
|   |-- memory/constitution.md           # 10 Reglas constitucionales inviolables
|   |-- memory/onboard-state.json        # Estado del asistente de onboarding
|   +-- templates/                       # Plantillas markdown oficiales
|-- docs/                                # Matrices de trazabilidad BDD
|-- harness/
|   |-- sdd.ps1                          # Orquestador maestro por consola
|   |-- dashboard.ps1                    # Generador de Cockpit Web y servidor en vivo
|   |-- spec-gate.ps1                    # Auditor Octuple (8 Hard Gates)
|   |-- verify-security.ps1              # Analisis SAST y detector de sinks
|   |-- pr-summary.ps1                   # Generador de reportes de Pull Request
|   |-- preview-design.ps1               # Servidor de prototipos de diseno
|   |-- init.ps1                         # Comprobador de runtime y tests
|   +-- hooks/                           # Implementacion fisica de hooks
|-- progress/
|   |-- sdd_dashboard.html               # Panel visual interactivo y visor DAG
|   +-- pr_summary.md                    # Reporte generado para Pull Requests
|-- feature_list.json                    # Backlog criptografico de funcionalidades
|-- CHECKPOINTS.md                       # Bitacora formal de hitos y criterios done
|-- AGENTS.md                            # Guia de comportamiento para el agente
+-- anti-gravity.md                      # Reglas operativas y convenciones
```

---

## 3. El Cockpit Ejecutivo & Visor DAG v6.3 (`harness/dashboard.ps1`)

El dashboard de SDD v6.3 revoluciona la observabilidad visual del backlog mediante un conjunto de herramientas interactivas de grado empresarial:

### 3.1. Capacidades del Lienzo DAG Interactivo

- **Pan y Zoom Fluido**: Arrastre con el raton y ampliacion/reduccion continua con la rueda del raton o los botones `+ Zoom` y `- Zoom`. El boton `↺ Reset` restablece la escala al 100% y centra el grafo.
- **Alternador de Orientacion**: El boton `↔ Orientacion` permite alternar al instante entre orientacion horizontal (`LR`) y vertical (`TD`) sin necesidad de reejecutar scripts en la consola.
- **Ruta Critica y Aislamiento de Dependencias**: Al pulsar sobre cualquier nodo del grafo, se ilumina el nodo en cyan (`#06b6d4`), sus dependencias upstream en morado (`#8b5cf6`) y sus dependencias downstream en ambar (`#f59e0b`), atenuando todos los nodos no relacionados.
- **Ficha Tecnica Desplegable (Drawer)**: Al seleccionar un nodo o pulsar "Ver Ficha" en la tabla, se abre un panel lateral con los metadatos completos: estado, descripcion, dependencias navegables, lista de archivos autorizados y candados SHA-256.
- **Exportacion**: Botones directos para copiar la sintaxis Mermaid limpia al portapapeles o descargar el diagrama renderizado en formato SVG.

### 3.2. Servidor HTTP Nativo en Vivo (`-Live`)

Para habilitar la sincronizacion en tiempo real mientras se desarrolla:

```powershell
.\harness\sdd.ps1 -Action dashboard -Live
```

El servidor web embebido:

1. Se ejecuta sobre el puerto `8080` (o el especificado con `-Port <numero>`).
2. Despliega la aplicacion localmente y abre el navegador por defecto.
3. Monitorea modificaciones en `feature_list.json` y `CHECKPOINTS.md`.
4. Al registrarse un cambio, regenera el HTML y ordena al navegador recargar la vista mediante sondeo reactivo a `/api/status`.
5. Permite una finalizacion limpia mediante `Ctrl+C` en la terminal.

### 3.3. Pestañas Operativas Integradas

- **📊 Visor DAG & Backlog**: Vista principal con metricas ejecutivas, progreso porcentual, grafo interactivo, filtros y tabla de backlog con buscador en vivo.
- **📋 Matriz de Trazabilidad BDD**: Cuadro de correspondencia entre funcionalidades, criterios EARS y escenarios de prueba.
- **🔒 Auditor Criptografico SHA-256**: Validador embebido con Web Crypto API para verificar la integridad de `spec.md` contra firmas registradas.
- **🛡️ Gobernanza CI/CD & 8 Aduanas**: Checklist visual de los 8 Hard Gates y estado de los workflows cloud.

---

## 4. Extensión de Gobernanza a CI/CD (GitHub Actions y GitLab CI)

SDD v6.3 automatiza la proteccion de ramas principales mediante compuertas en la nube:

### 4.1. Inicializacion y Comprobacion de Pipelines

Para inicializar o actualizar los archivos de CI/CD:

```powershell
.\harness\sdd.ps1 -Action init-cicd
```

Este comando genera:

- `.github/workflows/sdd-gate.yml`: Pipeline para GitHub Actions configurado para ejecutarse en Pull Requests hacia `main` o `master`.
- `.gitlab-ci.yml`: Pipeline para GitLab CI estructurado en 5 etapas (`lint`, `security`, `test`, `spec-gate`, `dashboard`).

### 4.2. Generacion de Reportes de Pull Request

El comando:

```powershell
.\harness\sdd.ps1 -Action pr-summary
```

Invoca `harness/pr-summary.ps1` y genera `progress/pr_summary.md`, un informe visual estructurado con:

- Metricas globales de avance del backlog.
- Checklist verificado de las 8 aduanas del Auditor Octuple.
- Estado de los sellos criptograficos SHA-256.
- Resumen de pruebas unitarias y BDD.
- Enlaces directos a los artefactos generados.

---

## 5. Los 8 Comprobadores del Auditor Octuple (`harness/spec-gate.ps1`)

Cada funcionalidad en transicion debe aprobar rigurosamente las 8 aduanas:

```powershell
.\harness\spec-gate.ps1 -FeatureId feat-01
```

1. **Aduana 1 (Git Hygiene)**: Valida que ningun archivo fuera de `allowed_files` haya sido modificado.
2. **Aduana 2 (Clean Architecture)**: Confirma la pureza de las capas `Domain` y `Application`.
3. **Aduana 3 (SAST & Ciberseguridad)**: Detecta sinks vulnerables de inyeccion y credenciales hardcodeadas.
4. **Aduana 4 (Candado SHA-256)**: Re-calcula y valida el hash criptografico de `spec.md`.
5. **Aduana 5 (Paridad BDD 1:1)**: Exige correspondencia biunivoca entre criterios EARS y pruebas ejecutables.
6. **Aduana 6 (Higiene Markdown)**: Audita cero violaciones en las reglas de markdownlint.
7. **Aduana 7 (Contratos & User Guide)**: Exige documentacion de uso actualizada.
8. **Aduana 8 (Candado de Complecion)**: Requiere el sello final de complecion emitido por el humano.

---

## 6. Comandos Operativos y CLI de Gobernanza (`harness/sdd.ps1`)

| Comando | Descripcion Operativa |
| :--- | :--- |
| `.\harness\sdd.ps1 -Action status` | Muestra el estado del backlog, la funcionalidad activa y metricas clave. |
| `.\harness\sdd.ps1 -Action list` | Lista todas las funcionalidades con ID, estado, dependencias y candados. |
| `.\harness\sdd.ps1 -Action create -FeatureId <id> -FeatureName <nombre>` | Registra una nueva funcionalidad en `feature_list.json`. |
| `.\harness\sdd.ps1 -Action set-active -FeatureId <id>` | Activa una funcionalidad pendiente para iniciar su ciclo de especificacion. |
| `.\harness\sdd.ps1 -Action approve -FeatureId <id> -Reason <motivo>` | Sella criptograficamente la especificacion y calcula el `approval_hash`. |
| `.\harness\sdd.ps1 -Action complete -FeatureId <id>` | Sella formalmente la funcionalidad y emite el `completion_hash`. |
| `.\harness\sdd.ps1 -Action next` | Selecciona automaticamente la siguiente funcionalidad desbloqueada. |
| `.\harness\sdd.ps1 -Action dashboard [-Live] [-Port <num>]` | Genera y despliega el Cockpit Web y Visor DAG (con soporte de servidor en vivo). |
| `.\harness\sdd.ps1 -Action verify-security` | Ejecuta el escaner de ciberseguridad SAST buscando sinks y secretos. |
| `.\harness\sdd.ps1 -Action init-cicd` | Inicializa los flujos de CI/CD para GitHub Actions y GitLab CI. |
| `.\harness\sdd.ps1 -Action pr-summary` | Genera el informe consolidado para Pull Requests en `progress/pr_summary.md`. |
| `.\harness\sdd.ps1 -Action fix-markdown` | Escanea y corrige automaticamente violaciones de formato Markdown en todo el proyecto. |

---

## 7. Como Inicializar un Proyecto con SDD v6.3

### Inicializacion en PowerShell

```powershell
powershell -ExecutionPolicy Bypass -File .\setup-sdd-project-v63.ps1 -ProjectName "mi-sistema" -Stack "python" -GitInit
```

### Inicializacion en Python

```powershell
python setup-sdd-project-v63.py
```

### Parametros Soportados

- `-ProjectName <string>`: Nombre del proyecto y directorio a inicializar.
- `-Stack <string>`: Stack tecnologico base (`python`, `typescript`, `dotnet`, `go`, `flutter`, `rust`, `java`). Por defecto: `python`.
- `-GitInit`: Inicializa automaticamente un repositorio Git con hook de pre-commit y `.gitignore`.
- `-AutoLaunch <auto|ide|cli|none>`: Controla el inicio automatico de sesion de chat con el agente en Antigravity IDE o terminal.

---

## 8. Higiene de Documentacion y Reglas Markdownlint

Todo documento o archivo `.md` generado bajo SDD v6.3 debe cumplir de manera estricta e inviolable con las 7 reglas de markdownlint:

1. **MD009 / no-trailing-spaces**: Prohibidos espacios en blanco al final de las lineas.
2. **MD022 / blanks-around-headings**: Todo encabezado (`#`, `##`, etc.) debe estar rodeado por exactamente una linea en blanco arriba y una abajo.
3. **MD031 / blanks-around-fences**: Los bloques de codigo cercados (fenced code blocks) deben estar rodeados por lineas en blanco.
4. **MD032 / blanks-around-lists**: Las listas deben estar separadas de parrafos, encabezados o reglas horizontales por una linea en blanco.
5. **MD040 / fenced-code-language**: Todo bloque de codigo cercado debe especificar su lenguaje (`powershell`, `markdown`, `json`, `html`, `mermaid`, etc.).
6. **MD047 / single-trailing-newline**: El archivo debe finalizar con exactamente un caracter de salto de linea al final.
7. **MD058 / blanks-around-tables**: Todas las tablas markdown deben estar rodeadas por lineas en blanco arriba y abajo.
