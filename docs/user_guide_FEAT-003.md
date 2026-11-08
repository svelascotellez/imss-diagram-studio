# Guía de Usuario: FEAT-003 - Catalogo de Stencils Arquitectonicos DIDT y Procesos IMSS

## 1. Proposito y Descripcion General

El módulo **FEAT-003** ofrece una biblioteca estandarizada y tipada de componentes técnicos y procesos institucionales para el personal de la **DIDT del IMSS**. Permite a los arquitectos de soluciones y modeladores arrastrar o seleccionar componentes listos para usar (como *API Gateway*, *Microservicios*, *Kafka*, *PostgreSQL*, y actores del IMSS como *Médico Familiar*, *Derechohabiente* y *Despachador de Farmacia*) garantizando coherencia visual y metadatos predefinidos.

## 2. Requisitos Previos y Configuracion

- Disponer del canvas interactivo institucional activo (`FEAT-001`).
- El catálogo se inicializa automáticamente con la colección de stencils canónicos de la DIDT.

## 3. Flujos de Trabajo Paso a Paso

### 3.1. Exploracion del Catalogo por Categorias (`AC-3.1`)

1. Localice la barra lateral izquierda del estudio de diagramación.
2. Observe las tres categorías principales:
   - **Arquitectura de Software**: API Gateway, Microservicios, OAuth2 SSO.
   - **Datos y Eventos**: PostgreSQL, Apache Kafka, Memoria Caché Redis.
   - **Procesos y Actores IMSS**: Médico Familiar, Paciente / Derechohabiente, Despachador de Farmacia, Auditor OIC.
3. Haga clic sobre la tarjeta de cualquier stencil para añadirlo inmediatamente al canvas con sus dimensiones óptimas, etiqueta descriptiva y paleta institucional.

### 3.2. Busqueda y Filtrado Reactivo en Tiempo Real (`AC-3.2`)

1. Utilice el campo de búsqueda situado en la parte superior del panel lateral.
2. Escriba el nombre o palabra clave del componente (por ejemplo, `Kafka`, `Postgres` o `Farmacia`).
3. El panel filtrará los resultados en menos de 50 ms ocultando las categorías sin coincidencias.

### 3.3. Gestion de Acordeon y Accesibilidad (`AC-3.3`)

1. Haga clic en el encabezado de cualquier categoría para colapsar o expandir su contenido.
2. Los lectores de pantalla anunciarán el cambio de estado mediante el atributo accesible `aria-expanded`.
3. Todos los componentes admiten navegación mediante teclado con la tecla <kbd>Tab</kbd> y selección mediante <kbd>Enter</kbd>.

### 3.4. Manejo de Fallback Seguro (`AC-3.4`)

1. Si una integración solicita instanciar un identificador de stencil desconocido o corrupto, el sistema generará automáticamente un nodo institucional genérico denominado *"Servicio Institucional"*, evitando errores o cierres inesperados de la sesión.

## 4. Preguntas Frecuentes y Solucion de Problemas

- **¿Puedo cambiar las dimensiones o nombre del stencil una vez agregado?**
  Sí, al situar el stencil en el canvas este opera como una forma vectorial editable que conserva sus manejadores de redimensionamiento y edición de texto.
- **¿Qué contraste visual ofrecen las tarjetas del catálogo?**
  Las tarjetas y textos del catálogo cumplen con el umbral WCAG 2.1 AA ($\ge 4.5:1$).

## 5. Accesibilidad y Atajos de Teclado (WCAG 2.1 AA)

| Elemento / Accion | Comportamiento Accesible |
| :--- | :--- |
| <kbd>Tab</kbd> / <kbd>Shift</kbd>+<kbd>Tab</kbd> | Navegar secuencialmente entre las tarjetas del catálogo |
| <kbd>Enter</kbd> / <kbd>Espacio</kbd> | Instanciar el stencil enfocado en el canvas |
| `role="searchbox"` | Campo de búsqueda optimizado para tecnologías de asistencia |
| `role="region"` | Estructura semántica para cada categoría de stencils |
