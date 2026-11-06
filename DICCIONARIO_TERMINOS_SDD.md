# Diccionario Glosario de Términos: Framework SDD v5.4

## Specification-Driven Development para Ingeniería de Software con Agentes de IA

Este glosario define los conceptos, acrónimos, metodologías y componentes técnicos empleados en la arquitectura y operación de **SDD v5.4**.

---

## Índice Temático

1. [Metodologías y Paradigmas de Desarrollo](#1-metodologías-y-paradigmas-de-desarrollo)
2. [Especificación y Requisitos Formales](#2-especificación-y-requisitos-formales)
3. [Gobernanza Criptográfica y Control de Cambios](#3-gobernanza-criptográfica-y-control-de-cambios)
4. [Arquitectura de Software y Código](#4-arquitectura-de-software-y-código)
5. [UI/UX Pro Max y Diseño Accesible](#5-uiux-pro-max-y-diseño-accesible)
6. [Ecosistema Antigravity IDE: Hooks, Skills y Arnés](#6-ecosistema-antigravity-ide-hooks-skills-y-arnés)

---

## 1. Metodologías y Paradigmas de Desarrollo

### **SDD (Specification-Driven Development)**

*Desarrollo Guiado por Especificaciones*. Metodología que establece que ninguna línea de código de producción puede redactarse sin un documento de especificación formal previo (`spec.md`), aprobado por un humano y verificado algorítmicamente. Su principio rector es: *"La especificación manda"*.

### **BDD (Behavior-Driven Development)**

*Desarrollo Guiado por el Comportamiento*. Enfoque de ingeniería que formaliza los requisitos del sistema en términos de comportamientos esperados y legibles tanto por humanos como por motores de prueba, estructurados mediante la sintaxis *Given-When-Then* (Dado-Cuando-Entonces).

### **TDD (Test-Driven Development) & Double-Loop TDD**

*Desarrollo Guiado por Pruebas*. Ciclo iterativo donde primero se escribe una prueba automatizada que falla (*Red*), luego se escribe el código mínimo para superarla (*Green*), y finalmente se optimiza la estructura (*Refactor*). En **Double-Loop TDD**, el bucle exterior valida el escenario BDD completo y el bucle interior valida las funciones unitarias de Clean Architecture.

### **Greenfield vs. Brownfield**

* **Greenfield:** Desarrollo de un proyecto nuevo desde cero, con arquitectura limpia desde el primer día.
* **Brownfield:** Proyecto con una base de código preexistente o heredada (*legacy*). En SDD se aborda con la skill `sdd-reverse-spec` para extraer especificaciones retroactivas sin romper la compatibilidad.

---

## 2. Especificación y Requisitos Formales

### **EARS (Easy Approach to Requirements Syntax)**

Sintaxis estandarizada de ingeniería de requisitos diseñada para eliminar ambigüedades en el lenguaje natural. Utiliza patrones rigurosos (Ubicuos, Conducidos por Eventos, Estados, Opciones o Respuestas a Errores):

* Ejemplo: *"When [evento], the [sistema] shall [acción]"*.
* En SDD, cada criterio recibe un identificador único e inmutable (ej. `AC-1.1`).

### **Gherkin**

Lenguaje formal legible por humanos y máquinas (utilizado por herramientas como Cucumber, Behave o SpecFlow) basado en palabras clave (`Feature`, `Scenario`, `Given`, `When`, `Then`, `And`). En SDD, cada escenario lleva la etiqueta correspondiente a su criterio EARS (ej. `@AC-1.1`).

### **Spec Drift (Dispersión de la Especificación)**

Fenómeno no deseado en el que el código fuente diverge de la especificación original debido a que el desarrollador o el agente de IA añade funciones no solicitadas, altera firmas o modifica archivos fuera del alcance estipulado.

### **Allowed Files (Lista Blanca de Archivos)**

Sección obligatoria (`## 5. Allowed Files`) dentro de `spec.md`. Declara la lista cerrada de rutas de archivo que el agente de IA tiene autorización explícita para crear o modificar durante una funcionalidad.

### **Hard Gate (Compuerta Dura)**

Mecanismo de validación física e infranqueable. A diferencia de una advertencia o *warning*, una compuerta dura detiene y aborta de inmediato la ejecución si no se satisface una condición matemática, criptográfica o estructural.

---

## 3. Gobernanza Criptográfica y Control de Cambios

### **Candado Criptográfico SHA-256**

Firma digital calculada mediante el algoritmo hash seguro **SHA-256** sobre el contenido normalizado del archivo `spec.md`. Garantiza que el documento no ha sido alterado ni una sola coma desde el momento en que fue revisado y aprobado por el operador humano.

### **Human-in-the-Loop (HITL)**

Principio de gobernanza que prohíbe que el agente de IA se autoapruebe planes o especificaciones. Requiere forzosamente la intervención y confirmación explícita de un ser humano para avanzar de fase.

### **DAG (Directed Acyclic Graph / Grafo Acíclico Dirigido)**

Estructura matemática de dependencias donde las aristas tienen una dirección y no existen ciclos infinitos. En SDD, el backlog (`feature_list.json`) se modela como un DAG mediante `depends_on`: una funcionalidad (ej. `FEAT-002`) queda bloqueada por el arnés hasta que su prerrequisito (ej. `FEAT-001`) esté completamente finalizado y sellado.

### **Completion Hash**

Hash criptográfico final generado durante el comando de cierre formal (`harness\sdd.ps1 -Action complete`). Sella el estado conjunto de especificación, código, pruebas y documentación en el historial inmutable `CHECKPOINTS.md`.

### **Matriz de Trazabilidad Bidireccional**

Documento auto-generado (`docs/traceability_<feature>.md`) que traza de ida y vuelta la correlación exacta entre:
$$\text{Requisito EARS } (AC\text{-}x.x) \longleftrightarrow \text{Escenario Gherkin } (@AC\text{-}x.x) \longleftrightarrow \text{Función de Test } \longleftrightarrow \text{Código en } src/$$

---

## 4. Arquitectura de Software y Código

### **Clean Architecture (Arquitectura Limpia)**

Patrón arquitectónico propuesto por Robert C. Martin que organiza el software en capas concéntricas con la regla fundamental de dependencia: *las capas internas nunca conocen nada de las capas externas*.

* **`domain/` (Capa de Dominio):** Entidades, reglas de negocio y Value Objects puros. Cero dependencias externas o de base de datos.
* **`application/` (Capa de Aplicación):** Casos de uso, orquestación del negocio e interfaces (puertos).
* **`infrastructure/` (Capa de Infraestructura):** Implementación técnica concreta: bases de datos, APIs de terceros, repositorios y sistemas de archivos.
* **`presentation/` (Capa de Presentación):** Interfaz gráfica de usuario (UI), endpoints REST o interfaces de consola (CLI). Nunca importa infraestructura de forma directa.

### **Inversión de Dependencias (Dependency Inversion Principle - DIP)**

Principio SOLID que exige que los módulos de alto nivel no dependan de módulos de bajo nivel; ambos deben depender de abstracciones (interfaces o protocolos).

### **AST (Abstract Syntax Tree / Árbol de Sintaxis Abstracta)**

Representación en árbol de la estructura sintáctica del código fuente producida por los compiladores e intérpretes. En SDD, el arnés inspecciona el AST de los archivos para auditar los `imports` y detectar violaciones arquitectónicas.

---

## 5. UI/UX Pro Max y Diseño Accesible

### **Design Tokens (Tokens de Diseño)**

Valores atómicos de diseño (colores, fuentes, sombras, espaciados, radios de borde) centralizados en formato de datos estructurado (`.specify/design-system/design-tokens.json`). Permite desacoplar el diseño de la tecnología concreta y reutilizarlo en web, móvil o desktop.

### **WCAG 2.1 AA (Web Content Accessibility Guidelines)**

Estándar internacional de accesibilidad web nivel AA promovido por el W3C. Exige que el contraste entre el texto y su fondo cumpla con un ratio de luminancia relativa mínimo de **4.5:1** para texto normal y **3.0:1** para texto grande.

### **Luminancia Relativa ($L$)**

Brillo relativo de cualquier punto en un espacio de color, normalizado de 0 para el negro más oscuro a 1 para el blanco más claro, calculado matemáticamente según la fórmula de la W3C:
$$\text{Ratio de Contraste} = \frac{L_1 + 0.05}{L_2 + 0.05} \ge 4.5:1$$

### **Magic Hex Codes (Códigos Hexadecimales Mágicos)**

Mala práctica consistente en escribir códigos de color hexadecimales arbitrarios (ej. `#3B82F6` o `#FA4512`) directamente en componentes de presentación. SDD v5.4 prohíbe los magic hex codes y obliga a consumir variables semánticas de diseño.

### **Los 5 Estados UI Obligatorios**

Regla de UX de SDD que exige diseñar y documentar formalmente el comportamiento de los componentes en sus cinco estados de interacción:

1. **Default:** Estado base o de reposo.
2. **Hover / Focus:** Interacción al pasar el cursor o navegar mediante teclado (accesibilidad).
3. **Loading:** Retroalimentación visual mientras se procesan datos asíncronos.
4. **Empty State:** Pantalla informativa amigable cuando no existen datos para mostrar, con llamada a la acción.
5. **Error State:** Comunicación clara de fallos con opciones de reintento y remediación.

---

## 6. Ecosistema Antigravity IDE: Hooks, Skills y Arnés

### **Scaffolding (Andamiaje)**

Generación automática de la estructura completa de carpetas, configuraciones, ganchos e interfaces de un proyecto para evitar el trabajo manual repetitivo.

### **Hooks (Ganchos de Ciclo de Vida)**

Scripts automáticos que se interceptan y disparan ante eventos del IDE:

* **`SessionStart`:** Inicializa la sesión del agente, lee la memoria del proyecto y retoma el contexto de trabajo.
* **`PreToolUse`:** Interceptor de seguridad que inspecciona llamadas a herramientas (`write_file`, `edit_file`) antes de que se ejecuten. Si el archivo destino no está en `Allowed Files`, aborta la operación físicamente.
* **`PostToolUse`:** Revisa silenciosamente tras cada cambio que las reglas de Clean Architecture se mantengan intactas.
* **`Git pre-commit`:** Impide confirmar cambios en el repositorio si los tests o el arnés de calidad fallan.

### **Skills (Habilidades Agénticas Canónicas y de Extensión)**

Módulos de instrucciones especializadas ubicados en `.agents/skills/<nombre>/SKILL.md` que enseñan al agente de IA cómo ejecutar una fase concreta del desarrollo (ej. `sdd-onboard`, `sdd-specify`, `sdd-plan`, `sdd-implement`, etc.). Incluye skills especializadas del ecosistema como **`frontend-design`** (de Anthropic) para erradicar patrones genéricos de IA, definir tokens tipográficos intencionales y construir interfaces gráficas de alto impacto con accesibilidad WCAG 2.1 AA.

### **Harness (Arnés de Calidad)**

Conjunto de herramientas de CLI y validación ubicadas en la carpeta `harness/` del proyecto:

* `init.ps1`: Ejecuta diagnósticos de entorno, tests automatizados y linters.
* `sdd.ps1`: CLI central para gestionar el backlog, aprobar candados criptográficos y consultar el estado del DAG.
* `spec-gate.ps1`: Motor de auditoría y ejecución de compuertas duras.
* `preview-design.ps1`: Generador de visualizaciones interactivas HTML del sistema de diseño.

### **Auditor Séptuple**

Suite de 7 verificaciones duras automáticas ejecutadas por `spec-gate.ps1` que deben aprobarse con 100% de éxito antes de poder cerrar una funcionalidad:

1. **Spec Drift:** Cero modificaciones fuera de `Allowed Files`.
2. **BDD 1:1:** Cobertura total de criterios EARS en escenarios Gherkin y tests.
3. **Clean Architecture:** Cero acoplamientos impuros y dependencias declaradas.
4. **Candado Criptográfico:** Coincidencia exacta del hash SHA-256 de `spec.md`.
5. **Anti-Fake Tests:** Prohibición de tests simulados o triviales.
6. **Guía de Usuario:** Manual obligatorio completo en 4 secciones sin texto de relleno.
7. **UI/UX Pro Max:** Validación algorítmica de contrastes WCAG AA y uso exclusivo de tokens.

### **Anti-Fake Tests (Detección Anti-Pruebas Falsas)**

Algoritmo dentro del arnés que inspecciona los archivos de prueba para detectar técnicas fraudulentas generadas por IA, como pruebas vacías, uso de `pass`, `skip` injustificado o aserciones triviales tipo `assert True == True`.
