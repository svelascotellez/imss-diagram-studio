# Plan Tecnico de Implementacion: FEAT-003

## 1. Diseno Arquitectonico (Clean Architecture)

- **Dominio (`src/domain/`)**:
  - `entities/stencil.entity.ts`: Entidad de stencil (id, nombre, categoría, tipo de forma base, dimensiones sugeridas, icono SVG, etiquetas de búsqueda).
  - `value-objects/stencil-category.vo.ts`: Value object inmutable que define categorías normalizadas (`architecture`, `data`, `process_actors`).
  - `repositories/stencil-catalog.repository.ts`: Interfaz abstracta del catálogo de stencils.
- **Aplicacion (`src/application/`)**:
  - `use-cases/search-stencils.use-case.ts`: Filtrado y búsqueda por texto/categoría en < 50 ms.
  - `use-cases/instantiate-stencil.use-case.ts`: Instanciación hacia el canvas (`ICanvasStateRepository`) con fallback seguro (`@AC-3.4`).
- **Infraestructura (`src/infrastructure/`)**:
  - `repositories/in-memory-stencil-catalog.repository.ts`: Catálogo pre-cargado con stencils oficiales de la DIDT y el IMSS.
- **Presentacion (`src/presentation/`)**:
  - `components/StencilSidebar.ts`: Componente interactivo de panel lateral con buscador reactivo, acordeón de categorías y accesibilidad ARIA (`role="tree"`, `aria-expanded`).

## 2. UI/UX Design System Specification (Design-System First)

- **Arquetipo Visual**: `IMSS Institucional DIDT`
- **Tokens de Color y Estructura**:
  - Fondo Sidebar: `#1E293B`
  - Tarjetas de Stencil: `#0F172A` con borde `#334155` y hover `#B38E5D`.
  - Iconos vectoriales: Trazo `#006341` (Verde IMSS) y `#B38E5D` (Dorado Institucional).
  - Texto títulos: `#FFFFFF`, texto secundario `#94A3B8`.
- **Estados Obligatorios de Interfaz**:
  - `default`: Tarjeta compacta con icono y etiqueta legible.
  - `hover`: Elevación ligera, borde dorado `#B38E5D` y cursor `pointer`.
  - `active / dragging`: Sombra pronunciada y reducción de opacidad (0.8).
  - `empty_state`: Mensaje ilustrado cuando la búsqueda no coincide con ningún stencil.
- **Accesibilidad**: WCAG 2.1 AA (contraste >= 4.5:1, soporte de navegación con flechas y Enter).

## 3. Contratos y Esquemas

```typescript
export type StencilCategoryType = 'architecture' | 'data_events' | 'imss_processes';

export interface IStencilDefinition {
  id: string;
  name: string;
  category: StencilCategoryType;
  baseShapeType: 'rectangle' | 'ellipse' | 'diamond' | 'container' | 'text';
  defaultWidth: number;
  defaultHeight: number;
  iconSvg: string;
  keywords: string[];
  description?: string;
}
```

## 4. Allowed Dependencies

Librerias externas de terceros autorizadas:

- `vitest`
- `typescript`

## 5. Security & Threat Modeling (STRIDE / OWASP Sinks)

- **Trust Boundaries (‖)**: Entrada de búsqueda del usuario ‖ Catálogo de Stencils en Memoria.
- **Evaluacion STRIDE**:
  - **Spoofing**: N/A para catálogo estático local.
  - **Tampering**: Definiciones de stencils inmutables (`Object.freeze`) para evitar modificación en tiempo de ejecución.
  - **Repudiation**: Trazabilidad de instanciaciones en el historial del canvas.
  - **Information Disclosure**: Los stencils contienen únicamente metadatos arquitectónicos públicos sin secretos institucionales.
  - **Denial of Service**: Algoritmo de búsqueda acotado en memoria O(N) sin expresiones regulares catastróficas (ReDoS seguro mediante búsqueda por subcadenas).
  - **Elevation of Privilege**: El catálogo opera exclusivamente como metadatos de configuración visual.
