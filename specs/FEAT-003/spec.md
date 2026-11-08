# Especificacion Funcional: FEAT-003 - Catalogo de Stencils Arquitectonicos DIDT y Procesos IMSS

## 1. Contexto e Historia de Usuario

Como Arquitecto de Software, Desarrollador o Diseñador de Procesos de la DIDT del IMSS
Quiero disponer de un panel lateral con catalogo estructurado de stencils arquitectonicos (microservicios, gateways, bases de datos, colas) y actores de procesos institucionales (medicos, pacientes, farmacia, auditoria)
Para acelerar la diagramacion tecnica reutilizando componentes estandarizados con metadatos y representacion grafica oficial del IMSS.

## 2. Criterios de Aceptacion (Sintaxis EARS)

- **AC-3.1**: CUANDO el usuario selecciona o arrastra un stencil del catalogo institucional hacia el canvas, EL SISTEMA DEBE instanciar una forma geometrica con sus dimensiones predeterminadas, icono vectorial, etiqueta descriptiva y estilo semantico institucional.
- **AC-3.2**: CUANDO el usuario escribe un termino de busqueda en el panel de stencils, EL SISTEMA DEBE filtrar en tiempo real en menos de 50 ms los componentes coincidentes por nombre o palabra clave en todas las categorias.
- **AC-3.3**: MIENTRAS el usuario navega entre categorias (Arquitectura de Software, Datos y Eventos, Actores IMSS), EL SISTEMA DEBE reflejar el estado expandido/colapsado con atributos de accesibilidad WCAG 2.1 AA (`aria-expanded`, `role="region"`) y paleta visual institucional.
- **AC-3.4**: SI se solicita instanciar un identificador de stencil desconocido o no registrado, EL SISTEMA DEBE aplicar un fallback seguro generando un nodo estandar ("Servicio Institucional") sin interrumpir la sesion ni emitir errores fatales.

## 3. Comportamientos Fuera de Alcance (Out of Scope)

- No se incluye persistencia remota ni importacion de archivos externos `.vsdx` de Visio (corresponde a iteraciones futuras).
- No se incluye la serializacion bidireccional XML Draw.io ni exportacion a SVG final con membrete oficial (corresponde a FEAT-004).
- No se incluye edicion avanzada del codigo SVG interno de los iconos dentro del canvas.

## 4. Requisitos No Funcionales, UI/UX y Accesibilidad

- Filtrado y renderizado del catalogo en menos de 50 ms para un minimo de 100 elementos.
- Cumplimiento de accesibilidad WCAG 2.1 AA con navegacion por teclado completa en el sidebar (<kbd>Tab</kbd>, <kbd>&uarr;</kbd>, <kbd>&darr;</kbd>, <kbd>Enter</kbd> para insertar).
- Tokens visuales alineados con `.specify/design-system/design-tokens.json` (Verde IMSS `#006341`, Acento `#B38E5D`, Fondo `#F8FAFC`, Texto `#0F172A`).
- Estados obligatorios: default, hover, focus-visible, empty_state (busqueda sin resultados).

## 5. Allowed Files

Rutas exactas autorizadas para creacion o modificacion durante esta funcionalidad:

- `src/domain/entities/stencil.entity.ts`
- `src/domain/value-objects/stencil-category.vo.ts`
- `src/domain/repositories/stencil-catalog.repository.ts`
- `src/application/use-cases/instantiate-stencil.use-case.ts`
- `src/application/use-cases/search-stencils.use-case.ts`
- `src/infrastructure/repositories/in-memory-stencil-catalog.repository.ts`
- `src/presentation/components/StencilSidebar.ts`
- `src/presentation/components/Canvas.ts`
- `tests/unit/domain/stencil.test.ts`
- `tests/unit/application/stencil-use-cases.test.ts`
- `tests/acceptance/stencil-interaction.spec.ts`
