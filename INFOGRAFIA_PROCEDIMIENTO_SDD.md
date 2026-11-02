# Infografía: Procedimiento Operativo de Creación de Aplicaciones

## Framework SDD v6.0 (Specification-Driven Development)

### Ciclo Determinista de Desarrollo de Software Asistido por Inteligencia Artificial • Enterprise Security Edition

---

```text
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                INFOGRAFÍA DEL PROCEDIMIENTO SDD v6.0                                   │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                        │
│  [00. SETUP v6.0] ───> [01. ONBOARDING] ───> [02. SPEC & BDD] ───> [03. CANDADO SHA-256]              │
│  Scaffolding y         Entrevista Socrática   EARS (AC-x.x)        Firma Humana HITL                   │
│  16 Skills + Arnés     1 pregunta/turno       Allowed Files        Inmutable                           │
│       │                                                                                                │
│       ▼                                                                                                │
│  [04. PLAN & STRIDE] ─> [05. TDD LOOP] ─> [06. GUÍA USUARIO] ─> [07. AUDITOR ÓCTUPLE]                  │
│  Clean Arch + STRIDE     Double-Loop TDD   Manual 4 Secciones    spec-gate.ps1 (8 Compuertas)          │
│  Threat Modeling         PreToolUse Hook   Cero placeholders     0 Secretos / 0 Inyecciones SQL        │
│                                                                        │                               │
│                                                                        ▼                               │
│                                                              [08. CIERRE & DAG]                        │
│                                                              Completion Hash                           │
│                                                              Matriz Trazabilidad                       │
│                                                              Desbloqueo Grafo DAG                      │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Desglose Paso a Paso del Procedimiento

### Paso 00: Inicialización y Scaffolding de Infraestructura v6.0

* **Actor:** Desarrollador (PowerShell o Python).
* **Acción:** Ejecución única del comando:

  ```powershell
  powershell -ExecutionPolicy Bypass -File .\setup-sdd-project-v6.ps1 -ProjectName "MiProyecto" -Stack "python" -GitInit
  ```

* **Resultado:** Despliega el árbol Clean Architecture, 16 skills operativas canónicas en `.agents/skills/` (incluyendo `sdd-secure-coding`), plantillas maestras, arnés de seguridad (`verify-security.ps1`) y los interceptores físicos de ciclo de vida (`hooks.json`).

---

### Paso 01: Descubrimiento Socrático (Onboarding Adaptativo SDD 2.0)

* **Actor:** Desarrollador + Agente en el chat de Antigravity IDE (`sdd-onboard`).
* **Regla de Oro:** **1 pregunta o fase por turno**.
* **Las 5 Fases:**
  1. *Propósito y Usuarios:* Greenfield vs. Brownfield y resultado clave esperado.
  2. *Tipo de Interfaz y Stack:* Web, Headless API, CLI o Móvil + presets (`java-spring`, `python-pytest`, `ts-vitest`, etc.).
  3. *Identidad Visual UI/UX:* Arquetipo visual y accesibilidad WCAG 2.1 AA ($\ge 4.5:1$).
  4. *Mapa DAG del Backlog Inicial:* Propuesta visible en chat con dependencias (`depends_on`).
  5. *Detalle de `FEAT-001`:* Historia de usuario y 4 criterios EARS.

---

### Paso 02: Especificación Formal & Escenarios BDD

* **Actor:** Agente (`sdd-specify` y `sdd-clarify`).
* **Artefactos Generados:**
  * `specs/FEAT-001/spec.md`: Criterios de aceptación EARS (`AC-1.1` a `AC-1.4`) y lista cerrada `## 5. Allowed Files`.
  * `specs/FEAT-001/scenarios.feature`: Escenarios ejecutables Gherkin mapeados 1:1 (`@AC-1.1` a `@AC-1.4`).
* **Blindaje:** Cualquier modificación fuera de `Allowed Files` es ilegal y bloqueada.

---

### Paso 03: El Candado Humano (Firma Criptográfica SHA-256)

* **Actor:** Desarrollador / Líder Técnico (Human-in-the-Loop).
* **Comando:**

  ```powershell
  .\harness\sdd.ps1 -Action approve -FeatureId FEAT-001 -Reason "Especificación validada"
  ```

* **Gobernanza:** Se genera un hash inmutable. La IA **tiene prohibido físicamente tocar código en `src/` sin este candado**.

---

### Paso 04: Plan Técnico, Arquitectura Limpia y Modelado STRIDE

* **Actor:** Agente (`sdd-plan`, `sdd-secure-coding` y `sdd-tasks`).
* **Acciones:**
  * Define las 4 capas de Clean Architecture (`domain`, `application`, `infrastructure`, `presentation`).
  * Modela amenazas en **Sección 5 STRIDE / OWASP**: Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege.
  * Verifica Trust Boundaries (`‖`) y ausencia de la Tríada Letal.
  * Genera el checklist atómico TDD en `tasks.md`.

---

### Paso 05: Implementación en Doble Bucle TDD

* **Actor:** Agente (`sdd-implement`).
* **Flujo:** Bucle exterior (BDD / Aceptación) + Bucle interior (TDD unitario): **Rojo $\rightarrow$ Verde $\rightarrow$ Refactor**.
* **Protección Activa:** El hook nativo `PreToolUse` inspecciona cada `write_file` y `edit_file`. Si el archivo no está en `Allowed Files`, la herramienta aborta físicamente en tiempo real.

---

### Paso 06: Documentación Obligatoria del Usuario Final

* **Actor:** Agente (`sdd-user-guide`).
* **Artefacto:** `docs/user_guide_FEAT-001.md`.
* **Regla Estricta:** Debe contener las 4 secciones canónicas (*Quick Start, Core Workflows, Error Handling, FAQ*) con **cero placeholders** (`TODO`, `TBD`).

---

### Paso 07: La Aduana Final — El Auditor Óctuple

* **Actor:** Arnés de Calidad (`harness/spec-gate.ps1`).
* **Las 8 Compuertas Duras:**
  1. *Spec Drift:* Cero cambios fuera de `Allowed Files` (workspace y commits).
  2. *BDD 1:1:* Cobertura total de criterios EARS en escenarios Gherkin y tests.
  3. *Clean Architecture:* Dominio 100% puro; cero dependencias de base de datos o frameworks en `domain`.
  4. *Candado Criptográfico:* Hash SHA-256 intacto respecto a la aprobación humana.
  5. *Anti-Fake Tests:* Cero `skip`, `pass` o pruebas vacías; corrida dinámica real exitosa con `init.ps1`.
  6. *Guía de Usuario:* 4 secciones completas en `docs/` sin texto provisional.
  7. *UI/UX Pro Max:* Tokens obligatorios y contraste WCAG AA verificado por algoritmo.
  8. *Secure Coding (NUEVO v6.0):* Cero secretos hardcodeados, cero concatenaciones SQL dinámicas, análisis SAST y dependencias limpias de CVEs.

---

### Paso 08: Cierre Formal & Sellado del Grafo DAG

* **Actor:** Arnés de Calidad (`harness/sdd.ps1 -Action complete`).
* **Acciones:**
  * Valida que las 8 compuertas del Auditor Óctuple estén aprobadas al 100%.
  * Calcula el `completion_hash` final.
  * Registra el hito en `CHECKPOINTS.md`.
  * Genera la **Matriz de Trazabilidad Bidireccional** en `docs/traceability_FEAT-001.md`.
  * Desbloquea las funcionalidades dependientes en `feature_list.json`.
