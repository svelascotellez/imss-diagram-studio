# Diccionario Glosario de Términos: Framework SDD v6.6

## Specification-Driven Development (Enterprise Regulatory & Compliance Hardened Edition)

Este glosario define los conceptos, acrónimos, metodologías y componentes técnicos empleados en la arquitectura y operación de **SDD v6.6**.

---

## Índice Temático

1. [Metodologías y Paradigmas de Desarrollo](#1-metodologías-y-paradigmas-de-desarrollo)
2. [Especificación y Requisitos Formales](#2-especificación-y-requisitos-formales)
3. [Gobernanza Criptográfica y Control de Cambios](#3-gobernanza-criptográfica-y-control-de-cambios)
4. [Arquitectura de Software y Código](#4-arquitectura-de-software-y-código)
5. [UI/UX Pro Max y Diseño Accesible](#5-uiux-pro-max-y-diseño-accesible)
6. [Ecosistema Agéntico: Hooks, Skills y Arnés](#6-ecosistema-agéntico-hooks-skills-y-arnés)
7. [Infraestructura, Portabilidad, Herramientas y DevOps](#7-infraestructura-portabilidad-herramientas-y-devops)

---

## 1. Metodologías y Paradigmas de Desarrollo

### **SDD (Specification-Driven Development)**

*Desarrollo Guiado por Especificaciones*. Metodología que establece que ninguna línea de código de producción puede redactarse sin un documento de especificación formal previo (`spec.md`), aprobado por un humano y sellado criptográficamente. Su principio rector es: *"La especificación manda, el código obedece y la criptografía gobierna"*.

### **BDD (Behavior-Driven Development)**

*Desarrollo Guiado por el Comportamiento*. Enfoque de ingeniería que formaliza los requisitos del sistema en términos de comportamientos esperados y legibles tanto por humanos como por motores de prueba, estructurados mediante la sintaxis *Given-When-Then* (Dado-Cuando-Entonces).

### **TDD (Test-Driven Development) & Double-Loop TDD**

*Desarrollo Guiado por Pruebas*. Ciclo iterativo donde primero se escribe una prueba automatizada que falla (*Red*), luego se escribe el código mínimo para superarla (*Green*), y finalmente se optimiza la estructura (*Refactor*). En **Double-Loop TDD**, el bucle exterior valida el escenario BDD completo y el bucle interior valida las funciones unitarias de Clean Architecture.

### **Greenfield vs. Brownfield**

- **Greenfield:** Desarrollo de un proyecto nuevo desde cero, con arquitectura limpia desde el primer día.
- **Brownfield:** Proyecto con una base de código preexistente o heredada (*legacy*). En SDD se aborda con la skill `sdd-reverse-spec` para extraer especificaciones retroactivas sin romper la compatibilidad.

---

## 2. Especificación y Requisitos Formales

### **EARS (Easy Approach to Requirements Syntax)**

Sintaxis estandarizada de ingeniería de requisitos diseñada para eliminar ambigüedades en el lenguaje natural. Utiliza patrones rigurosos (Ubicuos, Conducidos por Eventos, Estados, Opciones o Respuestas a Errores):

- Ejemplo: *"When [evento], the [sistema] shall [acción]"*.
- En SDD, cada criterio recibe un identificador único e inmutable (ej. `AC-1.1`).

### **Gherkin**

Lenguaje formal estructurado en bloques `Given-When-Then` para describir el comportamiento esperado del software. En SDD v6.6 existe paridad estricta 1:1 entre cada criterio `AC-X.Y` y una etiqueta `@AC-X.Y` en `scenarios.feature`.

---

## 3. Gobernanza Criptográfica y Control de Cambios

### **Candado Criptográfico HMAC-SHA256 (Pilar 3 & Gate 0)**

Firma digital generada con una clave secreta de 256 bits generada aleatoriamente mediante CSPRNG y persistida en `.specify/.sdd_key`. Sella conjuntamente la tríada inmutable: `spec.md + scenarios.feature + plan.md`.

### **Human-in-the-Loop (HITL)**

Aprobación humana formal y obligatoria. Ningún agente de IA puede auto-aprobar una especificación. Toda aprobación captura la identidad del usuario (`user.name <email>`), la marca de tiempo UTC y el algoritmo utilizado.

### **Spec Tampering (Adulteración de Especificación o Plan)**

Cualquier modificación no autorizada realizada sobre los archivos protegidos tras la firma HITL. Rompe el sello criptográfico e invoca el bloqueo inmediato de Gate 0 y de los hooks fail-closed.

### **Allowed Files (Lista Blanca de Archivos Permitidos)**

Sección de `plan.md` auditada por Gate 1 que declara exhaustivamente las únicas rutas relativas que el agente o desarrollador puede crear o editar durante la implementación.

---

## 4. Arquitectura de Software y Código

### **Clean Architecture Concéntrica Políglota**

Modelo arquitectónico en 4 capas concéntricas:

1. **Domain (Núcleo Puro):** Entidades y reglas de negocio, 100% independiente de librerías externas o frameworks.
2. **Application (Casos de Uso):** Orquestación y contratos de interfaces (puertos).
3. **Presentation (Adaptadores de Entrada):** Controladores REST, comandos CLI, interfaces gráficas.
4. **Infrastructure (Adaptadores de Salida):** Bases de datos, clientes HTTP, integraciones con la nube.

Regla de dependencia: las capas externas conocen a las internas, **nunca a la inversa**.

### **Anti-Fake Tests (Gate 5)**

Algoritmo de análisis estático dentro del arnés que detecta y bloquea técnicas de simulación complacientes producidas por agentes de IA: cuerpos de prueba con `pass`, aserciones triviales tipo `assert True == True` o decoradores `@skip` no autorizados.

---

## 5. UI/UX Pro Max y Diseño Accesible

### **Design Tokens Semánticos (`design-tokens.json`)**

Variables atómicas de diseño validadas para garantizar un contraste mínimo algorítmico de $\ge 4.5:1$ (WCAG 2.1 AA) en componentes y los 5 estados obligatorios (default, hover, active, focus, disabled).

### **Frontend Design Skill**

Habilidad agéntica especializada para crear interfaces gráficas de alto impacto, evitando patrones genéricos y asegurando coherencia semántica en sistemas visuales modernos.

---

## 6. Ecosistema Agéntico: Hooks, Skills y Arnés

### **Hooks Fail-Closed (`harness/hooks/`)**

Ganchos de ciclo de vida del agente:

- **`session-start.ps1`:** Inyecta en la memoria del agente el backlog, el grafo DAG y las reglas constitucionales.
- **`pre-tool-enforce.ps1`:** Interceptor fail-closed que bloquea físicamente la ejecución de herramientas de edición en `src/` si no hay un sello HMAC válido o si el archivo no está en `Allowed Files`.
- **`post-tool-check.ps1`:** Auditor silencioso post-edición que comprueba que las reglas de Clean Architecture se mantengan intactas.

### **El Auditor Nónuplo Reforzado (`spec-gate.ps1`)**

Motor de auditoría algorítmica que evalúa 10 compuertas inflexibles antes de autorizar el cierre formal de una funcionalidad:

- **Gate 0:** Verificación del Candado HMAC-SHA256 tridocumental.
- **Gate 1:** Contención de alcance (Allowed Files y cero Spec Drift).
- **Gate 2:** Paridad BDD 1:1 en Gherkin.
- **Gate 3:** Cobertura de pruebas unitarias TDD en dominio.
- **Gate 4:** Integridad de Clean Architecture sin fugas de infraestructura.
- **Gate 5:** Detección estricta de Fake Tests y mocks complacientes.
- **Gate 6:** Escaneo defensivo de seguridad OWASP y secretos.
- **Gate 7:** Análisis estático de código y linting.
- **Gate 8:** Trazabilidad, bitácora HITL en `CHECKPOINTS.md` y guía de usuario.
- **Gate 9:** Resiliencia SLA y benchmark de carga k6 (P95 < 200ms).

---

## 7. Infraestructura, Portabilidad, Herramientas y DevOps

### **Universal CLI Runner (`tools/sdd_cli.py` & `tools/sdd.sh`)**

CLI multiplataforma en Python y runner POSIX en Bash que permite ejecutar las operaciones centrales de gobernanza (status, approve, gate) de forma nativa en Linux, macOS y Docker sin requerir PowerShell.

### **Instalador One-Liner (`install.ps1` / `install.sh`)**

Scripts de despliegue rápido que permiten instalar o actualizar el framework SDD en segundos mediante un solo comando web (`curl` o `irm`).

### **DevContainer y Dockerfile (`.devcontainer/`)**

Configuración de contenedor reproducible para VS Code y GitHub Codespaces que preinstala PowerShell Core, Python 3.11, Chromium headless, k6 y la suite Pester 6, eliminando toda fricción de onboarding.

### **Radar de Gobernanza en IDE (`tools/sdd-status.ps1` & `.vscode/tasks.json`)**

Herramienta de inspección rápida integrada al editor que visualiza el estado del candado criptográfico y las compuertas duras en la consola mediante atajos de teclado del IDE.

### **Scaffolder Parity Engine (`tools/build_scaffolder.py`)**

Herramienta que verifica y garantiza la paridad estructural, de líneas y de habilidades entre el generador de PowerShell (`setup-sdd-project-v66.ps1`) y el generador de Python (`setup-sdd-project-v66.py`).

### **Pipeline de Compilación Documental (`tools/build_docs.py`)**

Mecanismo automatizado que compila y mapea la documentación fuente en Markdown hacia entregables en HTML5 interactivo y PDF vectorial mediante navegadores headless.
