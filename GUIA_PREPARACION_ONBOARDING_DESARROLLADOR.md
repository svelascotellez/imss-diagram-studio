# Guía de Preparación: Entrevista de Onboarding SDD 2.0

## Requisitos, Decisiones y Datos Previos para el Desarrollador (v5.4)

> **Destinatarios:** Desarrolladores, Arquitectos de Software y Líderes Técnicos
> **Entorno:** Google Antigravity IDE • Framework SDD v5.4
> **Propósito:** Disponer de toda la información requerida antes de iniciar la interacción con el agente agéntico (`sdd-onboard`), permitiendo completar el onboarding y emitir el primer candado criptográfico SHA-256 en menos de 5 minutos y sin fricción.

---

## 1. Introducción al Proceso de Onboarding

Al abrir un nuevo proyecto gobernado por SDD v5.4 en **Google Antigravity IDE**, el gancho de ciclo de vida nativo `SessionStart` detecta que el backlog (`feature_list.json`) se encuentra vacío y activa de inmediato la habilidad canónica `.agents/skills/sdd-onboard/SKILL.md`.

La entrevista opera bajo la regla de **«Exactamente 1 fase por turno»**, garantizando que el desarrollador no sea abrumado con formularios extensos. El proceso consta de **5 fases adaptativas**.

```text
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ Fase 1:         │ ──> │ Fase 2:         │ ──> │ Fase 3:         │ ──> │ Fase 4:         │ ──> │ Fase 5:         │
│ Propósito &     │     │ Interfaz &      │     │ Identidad UI/UX │     │ Mapa DAG del    │     │ Detalle FEAT-001│
│ Contexto        │     │ Stack Tech      │     │ (Solo con UI)   │     │ Backlog Inicial │     │ & Candado SHA   │
└─────────────────┴─────────────────┴─────────────────┴─────────────────┴─────────────────┘
```

---

## 2. Información Requerida por Fase

---

### FASE 1: Propósito, Usuarios y Contexto del Proyecto

En esta fase el agente realiza preguntas abiertas para entender la esencia del sistema y determinar si se trata de un desarrollo nuevo o sobre código existente.

* **1.1. Contexto de Código (Greenfield vs. Brownfield):**
  * **Greenfield:** Proyecto nuevo desde cero.
  * **Brownfield:** Proyecto con código previo en `src/`. En este caso, el desarrollador debe decidir si desea aplicar ingeniería inversa (`sdd-reverse-spec`) para documentar lo existente o si arrancará especificando nuevos módulos.
* **1.2. Propósito Central del Sistema:**
  * Descripción concisa (2 o 3 oraciones) del problema de negocio que el software resuelve.
* **1.3. Usuarios Objetivo (*Personas*):**
  * Identificación de los roles que interactuarán con el sistema (ej. *médico familiar, paciente derechohabiente, administrador de plataforma, auditor del OIC*).
* **1.4. Resultado de Mayor Valor:**
  * Qué beneficio medible o entregable tangible se espera obtener al término de la primera versión.

> **Ejemplo de Preparación para Fase 1:**
> *"Es un proyecto nuevo (Greenfield). El sistema gestionará la emisión y validación de Recetas Médicas Electrónicas para evitar duplicidades de surtido en farmacias hospitalarias. Los usuarios principales son los médicos en consulta externa y los despachadores de farmacia. El resultado clave es que una receta no pueda ser surtida dos veces en diferentes unidades."*

---

### FASE 2: Tipo de Interfaz y Stack Tecnológico

El agente desplegará una ventana modal interactiva (`ask_question`) para seleccionar el tipo de interfaz y el conjunto de herramientas de calidad.

* **2.1. Tipo de Interfaz:**
  * `Web Application / SaaS`: Aplicación web con frontend gráfico.
  * `API / Backend Service (Headless)`: Microservicio o API REST/gRPC sin interfaz gráfica. *(Salta automáticamente la Fase 3).*
  * `CLI / Terminal Utility`: Herramienta de línea de comandos interactiva. *(Salta la Fase 3).*
  * `Mobile / Desktop App`: Aplicación nativa o multiplataforma (Flutter / .NET MAUI).
* **2.2. Preset de Stack Tecnológico y Test Runner:**
  * `python-pytest`: Python 3.10+ • Linter `mypy` • Tests `pytest` y `pytest-bdd`.
  * `ts-vitest`: TypeScript / Node • Tipos `tsc --noEmit` • Tests `vitest`.
  * `dotnet-xunit`: C# .NET 8+ • Build `dotnet build` • Tests `xUnit`.
  * `go-test`: Go 1.20+ • Analizador `go vet` • Tests `go test`.
  * `flutter-test`: Dart / Flutter • Analizador `dart analyze` • Tests `flutter test`.
  * `rust-cargo`: Rust 2021 • Chequeo `cargo check` • Tests `cargo test`.

---

### FASE 3: Identidad Visual y UI/UX Pro Max (Solo Proyectos con UI)

Si la aplicación cuenta con interfaz gráfica, el agente pedirá seleccionar el arquetipo visual para garantizar cumplimiento del estándar internacional **WCAG 2.1 AA** (ratio de contraste algorítmico $\ge 4.5:1$).

* **3.1. Arquetipos Visuales Disponibles:**
  * `Modern Clean SaaS`: Primario `#2563EB` (Azul corporativo), fondo `#FFFFFF`, texto `#0F172A`.
  * `Minimalist Editorial`: Primario `#18181B` (Negro neutro), fondo `#FFFFFF`, texto `#09090B`.
  * `Bento Grid High-Contrast`: Primario `#0284C7` (Cian profesional), fondo `#F8FAFC`, texto `#0F172A`.
  * `Enterprise Analytics`: Primario `#4F46E5` (Índigo institucional), fondo `#FFFFFF`, texto `#1E293B`.
* **3.2. Colores Institucionales Personalizados (Opcional):**
  * Si el proyecto pertenece a una institución con identidad gráfica corporativa (ej. verde IMSS `#006341`), tener preparado el código hexadecimal primario para su ajuste en `.specify/design-system/design-tokens.json`.

---

### FASE 4: Mapa DAG del Backlog Inicial (`depends_on`)

El agente **no usará modales en esta fase**, sino que imprimirá directamente en el chat una propuesta de tabla Markdown y un diagrama Mermaid con las primeras funcionalidades (`FEAT-001`, `FEAT-002`, `FEAT-003`).

* **Qué debe tener listo el desarrollador:**
  1. **Lista de 3 a 4 funcionalidades mínimas** que conformarán el primer ciclo de desarrollo.
  2. **Dependencias técnicas y de negocio (`depends_on`):** Cuál funcionalidad bloquea a cuál.
  3. **Capa predominante de Clean Architecture:** `domain`, `application`, `infrastructure` o `presentation`.

> **Ejemplo de Preparación para Fase 4:**

> * `FEAT-001`: Autenticación y Perfil de Usuario (`depends_on: []` | Capa: `application`).
> * `FEAT-002`: Registro y Firma de Receta Médica (`depends_on: ["FEAT-001"]` | Capa: `domain`).
> * `FEAT-003`: Surtido y Validación en Farmacia (`depends_on: ["FEAT-002"]` | Capa: `application`).

---

### FASE 5: Detalle de `FEAT-001` y Candado Criptográfico SHA-256

El agente presentará en el chat el borrador completo de `specs/FEAT-001/spec.md` y `specs/FEAT-001/scenarios.feature` para su revisión y sellado humano.

* **5.1. Historia de Usuario:**
  * Formato: *Como [Rol], quiero [Acción concreta], para [Beneficio de negocio].*
* **5.2. Los 4 Criterios de Aceptación EARS Obligatorios:**
  * **`AC-1.1` (Flujo Exitoso Principal):** Qué ocurre cuando los datos son válidos y la operación concluye con éxito (*"CUANDO..., EL SISTEMA DEBE..."*).
  * **`AC-1.2` (Control de Errores y Validaciones):** Qué mensajes y bloqueos se activan ante datos inválidos o fallos (*"CUANDO..., EL SISTEMA DEBE..."*).
  * **`AC-1.3` (Feedback Accesible / Estado Activo):** Indicadores visuales durante procesos asíncronos o reglas de concurrencia (*"MIENTRAS..., EL SISTEMA DEBE..."*).
  * **`AC-1.4` (Regla de Negocio / Caso Borde):** Comportamiento en condiciones límite (duplicidad, límite de intentos, timeout) (*"SI..., EL SISTEMA DEBE..."*).
* **5.3. Fuera de Alcance (*Out of Scope*):**
  * Lista explícita de lo que **NO** se programará en esta entrega inicial para evitar el desvío de alcance (*scope drift*).
* **5.4. Autorización del Candado Criptográfico:**
  * El desarrollador debe estar listo para responder *"Apruebo la especificación"* en el chat, permitiendo al agente invocar internamente `harness\sdd.ps1 -Action approve` para emitir la firma SHA-256.

---

## 3. Ficha Desprendible de Trabajo (Checklist Rápido)

Imprime o copia esta ficha para rellenarla antes de iniciar la sesión de chat con el agente:

```text
================================================================================
FICHA DE PREPARACIÓN DE ONBOARDING — SDD v5.4
================================================================================

1. FASE 1: CONTEXTO Y PROPÓSITO
   [ ] Tipo de Código: ( ) Greenfield [Nuevo]   ( ) Brownfield [Existente]
   [ ] Problema que resuelve: __________________________________________________
   [ ] Usuarios clave (Roles): ________________________________________________
   [ ] Resultado de mayor valor: ______________________________________________

2. FASE 2: INTERFAZ Y STACK
   [ ] Tipo de Interfaz: ( ) Web App   ( ) API/Headless   ( ) CLI   ( ) Móvil
   [ ] Preset Tecnológico:
       ( ) python-pytest    ( ) ts-vitest     ( ) dotnet-xunit
       ( ) go-test          ( ) flutter-test  ( ) rust-cargo

3. FASE 3: IDENTIDAD VISUAL (Omitir si es API / CLI)
   [ ] Arquetipo: ( ) Modern Clean SaaS  ( ) Minimalist  ( ) Bento  ( ) Analytics
   [ ] Color Primario Institucional (Opcional): #_______________

4. FASE 4: MAPA DAG DEL BACKLOG
   - Funcionalidad 1 (Base): ________________________ (depends_on: [])
   - Funcionalidad 2:        ________________________ (depends_on: [FEAT-001])
   - Funcionalidad 3:        ________________________ (depends_on: [FEAT-002])

5. FASE 5: PRIMERA FUNCIONALIDAD (FEAT-001)
   [ ] Historia: Como ____________ quiero ________________ para _______________
   [ ] AC-1.1 (Éxito):     CUANDO ________________ EL SISTEMA DEBE ____________
   [ ] AC-1.2 (Errores):   CUANDO ________________ EL SISTEMA DEBE ____________
   [ ] AC-1.3 (Feedback):  MIENTRAS ______________ EL SISTEMA DEBE ____________
   [ ] AC-1.4 (Borde):     SI ____________________ EL SISTEMA DEBE ____________
   [ ] Fuera de Alcance:   1. __________________  2. __________________________
================================================================================
```

---

## 4. Buenas Prácticas para el Desarrollador

1. **Sé concreto en las respuestas:** Respuestas breves y directas facilitan que el agente genere especificaciones precisas sin ambigüedades.
2. **Aprovecha el Co-Diseño Proactivo:** Si no tienes claros los 4 criterios EARS al inicio, describe la funcionalidad con tus palabras; el agente propondrá el borrador formal EARS y tú solo tendrás que afinarlo o confirmarlo.
3. **No te preocupes por la consola:** En Antigravity IDE no necesitas abrir terminales externas para aprobar checkpoints; el agente interactúa contigo en el chat y ejecuta los comandos de arnés (`harness/sdd.ps1`) en segundo plano tras tu autorización.
