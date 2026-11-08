# Plan Tecnico de Implementacion: FEAT-001

## 1. Diseno Arquitectonico (Clean Architecture)

- **Dominio (`src/domain/`)**:
  - `entities/shape.entity.ts`: Entidad de forma vectorial (id, tipo, posición, dimensiones, zIndex, estilo, estado de selección).
  - `value-objects/point.vo.ts`: Value object inmutable para coordenadas cartesianas (x, y) con validación de valores no negativos.
  - `value-objects/dimensions.vo.ts`: Value object inmutable con validación de límite mínimo (20x20 px).
  - `repositories/canvas-state.repository.ts`: Interfaz abstracta del estado del canvas.
- **Aplicacion (`src/application/`)**:
  - `use-cases/create-shape.use-case.ts`: Caso de uso para crear y añadir formas al canvas.
  - `use-cases/move-shapes.use-case.ts`: Caso de uso para desplazamiento atómico de selección múltiple.
  - `use-cases/select-shapes.use-case.ts`: Caso de uso para cálculo de intersección de selección rectangular y selección puntual.
- **Infraestructura (`src/infrastructure/`)**:
  - Dobles en memoria y adaptadores para estado del canvas.
- **Presentacion (`src/presentation/`)**:
  - `components/Canvas.ts`: Componente interactivo que renderiza el SVG/DOM con eventos de puntero (pointerdown, pointermove, pointerup), caja de selección y enfoque accesible.

## 2. UI/UX Design System Specification (Design-System First)

- **Arquetipo Visual**: `IMSS Institucional DIDT`
- **Tokens de Color**:
  - Verde IMSS Primario: `#006341`
  - Verde IMSS Hover: `#004D32`
  - Acento Dorado IMSS: `#B38E5D`
  - Fondo Canvas: `#F8FAFC`
  - Superficie Nodos: `#FFFFFF`
  - Texto Nodos: `#0F172A`
- **Estados Obligatorios de Interfaz**:
  - `default`: Nodo renderizado en superficie blanca con borde institucional gris y tipografía accesible.
  - `hover`: Resalte con borde Verde IMSS (`#006341`) y cursor apropiado (move/resize).
  - `active / selected`: Bounding box con 8 manejadores en esquinas y lados, borde de enfoque `#006341`.
  - `focus-visible`: Contorno de teclado accesible conforme a WCAG 2.1 AA.
  - `empty_state`: Mensaje amigable cuando el canvas no contiene elementos con botón rápido de inserción.
  - `error_state`: Notificación no intrusiva ante operaciones con valores fuera de rango.
- **Accesibilidad**: WCAG 2.1 AA (contraste >= 4.5:1, atributos `role="graphics-document"`, `aria-selected`, navegación completa por teclado con Tab y Flechas).

## 3. Contratos y Esquemas

```typescript
export type ShapeType = 'rectangle' | 'ellipse' | 'diamond' | 'container' | 'text';

export interface IShapeState {
  id: string;
  type: ShapeType;
  x: number;
  y: number;
  width: number;
  height: number;
  zIndex: number;
  isSelected: boolean;
  stroke: string;
  fill: string;
  label?: string;
}

export interface ISelectionBox {
  startX: number;
  startY: number;
  endX: number;
  endY: number;
}
```

## 4. Allowed Dependencies

Librerias externas de terceros autorizadas:

- `vitest`
- `typescript`

## 5. Security & Threat Modeling (STRIDE / OWASP Sinks)

- **Trust Boundaries (‖)**: Usuario / Navegador ‖ Canvas DOM / Estado en Memoria.
- **Evaluacion STRIDE**:
  - **Spoofing**: N/A para capa de canvas local en memoria.
  - **Tampering**: Validación inmutable en Value Objects (`Dimensions` y `Point`), impidiendo dimensiones negativas o de tamaño cero mediante invariantes de dominio.
  - **Repudiation**: Registro estructurado en consola de depuración de acciones del usuario (adición, movimiento, redimensión).
  - **Information Disclosure**: Sanitización de etiquetas de texto en nodos para evitar inyección de scripts (XSS en SVG).
  - **Denial of Service**: Acotamiento de tamaño máximo del canvas y restricción de límite de coordenadas (máximo 50,000 px).
  - **Elevation of Privilege**: El motor de canvas opera exclusivamente en el sandbox del navegador sin ejecución de código arbitrario.
