# Política de Seguridad y Divulgación de Vulnerabilidades (SDD Framework)

El framework **Specification-Driven Development (SDD)** está concebido como un estándar metodológico de alta regulación y contención determinista para el desarrollo de software asistido por agentes de Inteligencia Artificial. La seguridad criptográfica y la contención arquitectónica son el núcleo de este marco de trabajo.

---

## 1. Versiones con Soporte Activo de Seguridad

Las siguientes versiones del framework SDD reciben parches de seguridad y auditoría continua:

| Versión | Edición / Estado | Soporte de Seguridad |
| :---: | :--- | :---: |
| **6.6.x** | **Regulatory & Compliance Hardened Edition** | :white_check_mark: Activo (Primario) |
| **6.5.x** | Legacy Hardened | :warning: Solo fallos críticos |
| < 6.5 | Deprecated / Archivado | :x: No soportado |

---

## 2. Áreas de Criticidad y Superficie de Ataque

Consideramos reportes de alta prioridad aquellos que impacten directamente los pilares de contención del framework:

1. **Vulnerabilidades en el Candado HMAC-SHA256 (Gate 0):**
   - Evasión de la verificación criptográfica del sello (`.approval_seal`).
   - Debilidades en la generación, almacenamiento o rotación de claves (`.specify/.sdd_key` o `$env:SDD_HMAC_KEY`).
   - Manipulación de archivos aprobados sin invalidación del hash (`spec.md`, `scenarios.feature`, `plan.md`).

2. **Evasión de Hooks Fail-Closed (`harness/hooks/`):**
   - Modificación inadvertida o deliberada de archivos bajo `src/` saltándose el hook `pre-tool-enforce.ps1`.
   - Inyección de comandos o ejecución arbitraria de código mediante parámetros del CLI (`sdd.ps1` o scripts de scaffolding).

3. **Falsos Negativos en Detección de Pruebas Falsas (Gate 5):**
   - Técnicas de evasión en pruebas complacientes (`Fake Tests`) no detectadas por el analizador estático.

4. **Fuga de Secretos o Credenciales:**
   - Fallos en los filtros de sanitización anti-hardcoding o persistencia indebida de secretos en expedientes de evidencia regulatoria.

---

## 3. Proceso para Notificar una Vulnerabilidad

**Por favor, NO abras un issue público en GitHub para reportar vulnerabilidades de seguridad.**

Para coordinar una divulgación responsable:

1. Envía un correo electrónico a **salvador.velasco@gmail.com** con el asunto:
   `[SDD-SECURITY] Reporte de vulnerabilidad: <Breve descripción>`
2. Incluye en tu reporte:
   - Descripción detallada del vector de vulnerabilidad.
   - Pasos reproducibles o script de Prueba de Concepto (PoC).
   - Componentes afectados (`setup-sdd-project-v66.ps1`, `harness/spec-gate.ps1`, hooks, etc.).
   - Impacto estimado según el estándar CVSS v3.1.
3. Se confirmará la recepción del reporte en un plazo máximo de **48 horas laborables**.
4. Se mantendrá al remitente informado sobre el progreso de mitigación y la publicación del parche correspondiente.

---

## 4. Compromiso de Respuesta y Cumplimiento

Nos comprometemos a:
- Evaluar la severidad técnica en un plazo no mayor a 5 días hábiles.
- Generar un hotfix verificado formalmente mediante la suite Pester 6 antes de su liberación pública.
- Dar crédito público al investigador que descubrió la vulnerabilidad (salvo que solicite permanecer anónimo).
