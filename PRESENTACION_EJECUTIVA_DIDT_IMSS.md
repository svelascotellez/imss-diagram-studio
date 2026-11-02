# Presentación Ejecutiva: Gobernanza de Desarrollo Asistido por IA

## Dirección de Innovación y Desarrollo Tecnológico (DIDT) — IMSS

### Adopción del Framework SDD v6.0 Enterprise Security Edition para Sistemas Institucionales

---

### Diapositiva 1: Portada y Propósito Institucional

**Título:** Transformación Digital Segura, Auditable y Acelerada en el IMSS
**Subtítulo:** Marco de Gobernanza, Calidad y Ciberseguridad de Software Asistido por Inteligencia Artificial para la DIDT

* **Institución:** Instituto Mexicano del Seguro Social (IMSS)
* **Área:** Dirección de Innovación y Desarrollo Tecnológico (DIDT)
* **Objetivo:** Adoptar el potencial acelerador de los Agentes de Inteligencia Artificial en el desarrollo de software institucional, asegurando al 100% el cumplimiento normativo, la trazabilidad ante órganos fiscalizadores (OIC / ASF), la protección de datos personales de salud (LGPDPPSO / NOM-024-SSA3) y la estabilidad de los servicios de salud y prestaciones sociales.

---

### Diapositiva 2: El Contexto y Desafío de la DIDT

**Título:** Sistemas de Misión Crítica para Más de 70 Millones de Derechohabientes

* **La Responsabilidad del IMSS:** Los sistemas del Instituto gestionan citas médicas, expedientes clínicos electrónicos, recetas médicas, recaudación patronal y pensiones. Un error o vulnerabilidad en producción no es solo una falla técnica; afecta la salud, la privacidad y los derechos de la población derechohabiente.
* **El Reto de la IA Generativa sin Control:** La adopción libre o no gobernada de herramientas de IA en desarrollo introduce riesgos inaceptables para el sector público:
  * **Alucinaciones y Drift:** Creación de código innecesario o no contemplado en los requerimientos institucionales.
  * **Falta de Trazabilidad:** Dificultad para demostrar a los órganos de control (OIC / ASF) qué se programó, por qué y con qué autorización.
  * **Brechas de Ciberseguridad:** Exposición de secretos, inyecciones SQL en bases de datos clínicas y paquetes de dependencias con vulnerabilidades conocidas (CVEs).
  * **Código Espagueti y Deuda Técnica:** Pérdida de soberanía tecnológica y altos costos de mantenimiento.

---

### Diapositiva 3: La Respuesta Institucional — Framework SDD v6.0

**Título:** "La Especificación Manda": Ingeniería Determinista y Blindada para el Sector Público

* **Axioma de Gobierno Institucional:** En la DIDT, **ninguna línea de código de producción puede existir sin una especificación formal aprobada, trazable, sellada criptográficamente por un servidor público responsable y blindada contra vulnerabilidades de seguridad**.
* **Los 6 Pilares Institucionales v6.0:**
  1. **Control y Soberanía Humana (Human-in-the-Loop):** La IA sugiere y acelera; el personal técnico del IMSS aprueba y gobierna con firma SHA-256.
  2. **Arquitectura Limpia y Desacoplada (Clean Architecture):** Independencia de proveedores de nube y modularidad total en 4 capas concéntricas puras.
  3. **Accesibilidad Universal (WCAG 2.1 AA):** Garantía algorítmica de interfaces legibles para adultos mayores y personas con discapacidad visual ($\ge 4.5:1$).
  4. **Blindaje Físico Anti-Drift:** Interceptores nativos que impiden a la IA modificar archivos críticos fuera de la lista blanca permitida.
  5. **Gobernanza DAG de Dependencias:** Grafo acíclico dirigido que impide avanzar funcionalidades secundarias sin que las dependencias base estén auditadas y selladas.
  6. **Ciberseguridad y Protección de Datos (NUEVO v6.0):** Modelado preventivo de amenazas STRIDE, escaneo estático SAST, detección de secretos y cero inyecciones SQL.

---

### Diapositiva 4: Transparencia y Fiscalización (OIC / ASF)

**Título:** Auditoría Continua y Trazabilidad Criptográfica Inalterable

* **El Candado Digital SHA-256:**
  * Al autorizar los requerimientos de una nueva función, se emite una firma digital criptográfica inmutable.
  * Si la especificación sufre la más mínima alteración posterior, el sistema bloquea automáticamente la ejecución de la IA.
* **Matriz de Trazabilidad Bidireccional:**
  * Generación automática de reportes que vinculan en un solo hilo conductor:
    $$\text{Norma Institucional} \longleftrightarrow \text{Requerimiento EARS} \longleftrightarrow \text{Escenario BDD} \longleftrightarrow \text{Prueba Automatizada} \longleftrightarrow \text{Código en Producción}$$

* **Cumplimiento sin Burocracia:** Evidencia documental y técnica lista al instante para solventar observaciones del Órgano Interno de Control (OIC) y la Auditoría Superior de la Federación (ASF).

---

### Diapositiva 5: Calidad de Misión Crítica — Las 8 Aduanas Institucionales

**Título:** El Auditor Óctuple: Cero Tolerancia a Fallos y Cero Vulnerabilidades

Antes de que una nueva funcionalidad se libere hacia los ambientes de pruebas y producción del IMSS, debe superar 8 compuertas duras automatizadas (`harness/spec-gate.ps1`):

| Aduana | Enfoque DIDT | Impacto en el IMSS |
| :---: | :--- | :--- |
| **1. Cero Desvíos (Spec Drift)** | La IA solo modifica la lista blanca de archivos permitidos. | Protección de sistemas existentes; cero efectos secundarios. |
| **2. Cobertura BDD 100%** | Cada regla médica o administrativa tiene una prueba asociada. | Certeza de que la regla de negocio institucional se cumple fielmente. |
| **3. Clean Architecture** | Separación estricta de la lógica médica y las bases de datos. | Mantenimiento ágil, soberanía tecnológica y cero acoplamiento. |
| **4. Integridad del Candado** | Hash SHA-256 verificado matemáticamente contra el sello humano. | Garantía jurídica de que solo se programó lo formalmente aprobado. |
| **5. Anti-Fake Tests** | Detección y bloqueo de pruebas falsas o simuladas con `pass`/`skip`. | Rigor técnico real; verificación comprobable en ejecución dinámica. |
| **6. Guía de Usuario Obligatoria** | Manual operativo en 4 secciones sin textos provisionales. | El personal médico y administrativo sabe operar el sistema desde el día 1. |
| **7. Accesibilidad Ciudadana** | Contraste visual verificado matemáticamente ($\ge 4.5:1$). | Servicios digitales inclusivos para toda la derechohabiencia (WCAG AA). |
| **8. Ciberseguridad OWASP (NUEVO)** | Escaneo de secretos, SAST, CVEs y modelado de amenazas STRIDE. | Protección de datos clínicos (NOM-024) y blindaje contra fugas de información. |

---

### Diapositiva 6: Inclusión Ciudadana — Accesibilidad WCAG 2.1 AA

**Título:** IMSS Digital para Toda la Población, sin Barreras

* **La Realidad de Nuestros Usuarios:** Gran parte de los usuarios de IMSS Digital son adultos mayores, personas pensionadas o ciudadanos con debilidad visual.
* **Verificación Matemática de Diseño:**
  * SDD v6.0 incorpora un motor algorítmico que calcula la luminancia relativa y el contraste de colores según la norma internacional **WCAG 2.1 AA**.
  * Si un botón o texto no alcanza el ratio mínimo de **4.5 a 1**, el arnés bloquea físicamente la liberación.
* **Diseño Resiliente en 5 Estados:** Obliga a contemplar: reposo, foco accesible, carga, estados vacíos y manejo claro de fallas de conexión o interrupciones de red.

---

### Diapositiva 7: Ciberseguridad Defensiva y Protección de Datos Personales

**Título:** Blindaje de Datos Sensibles de Salud y Cumplimiento Normativo (NOM-024)

* **Protección del Expediente Clínico:**
  * El arnés inspecciona de forma estricta que ninguna consulta a bases de datos (PostgreSQL, Oracle, SQL Server) utilice concatenación de texto dinámica; el uso de consultas parametrizadas o repositorios con tipos seguros es obligatorio.
* **Alerta Temprana ante la Tríada Letal:**
  * Monitoreo riguroso en puntos del sistema donde interactúan: **Datos Médicos Sensibles + Entrada de Datos Externa + Canales de Red o Exportación**.
* **Escáner Preventivo Institucional (`verify-security.ps1`):**
  * Detección automática de llaves criptográficas o contraseñas hardcodeadas antes de cualquier confirmación de código.
  * Auditoría de dependencias de terceros para bloquear librerías con vulnerabilidades críticas (CVEs).

---

### Diapositiva 8: Soberanía Tecnológica y Eficiencia Presupuestal

**Título:** Maximizar el Valor del Gasto Público en Innovación

* **Reducción Radical de Costos por Retrabajo:** Detectar inconsistencias en la fase de especificación previa cuesta minutos; corregir fallas en sistemas hospitalarios activos cuesta millones de pesos y horas críticas de atención médica.
* **Independencia de Proveedores y Stacks Políglotas:** Compatible con arquitecturas corporativas del IMSS (Spring Boot Java 21, Angular 21, PostgreSQL 17, .NET, Python, etc.) bajo Clean Architecture pura.
* **Aceleración de Entregas (Time-to-Value):** Los equipos de desarrollo de la DIDT pueden entregar módulos y trámites digitales hasta 3 veces más rápido, manteniendo un estándar de calidad y seguridad uniforme y auditable.

---

### Diapositiva 9: Conclusión y Hoja de Ruta de Implementación

**Título:** Innovar con Responsabilidad de Estado

* **Conclusión Estratégica:**
  > *"El Framework SDD v6.0 permite a la DIDT del IMSS capitalizar la revolución de la Inteligencia Artificial, transformándola de un riesgo potencial a una palanca institucional de excelencia técnica, ciberseguridad, transparencia y servicio público a la salud mexicana."*

* **Siguientes Pasos Sugeridos para la DIDT:**
  1. **Piloto Controlado:** Implementar SDD v6.0 en una iniciativa o trámite digital prioritario de la DIDT.
  2. **Capacitación de Células de Desarrollo:** Habilitar a los desarrolladores institucionales en Google Antigravity IDE con las 16 habilidades (*skills*) canónicas.
  3. **Adopción como Norma Técnica Interna:** Institucionalizar el arnés, las 8 aduanas y el candado criptográfico como estándar formal de entrega para desarrollos internos y de terceros.
