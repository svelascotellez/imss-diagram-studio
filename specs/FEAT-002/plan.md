# Plan Tecnico de Implementacion: FEAT-002

## 1. Diseno Arquitectonico (Clean Architecture)

- **Dominio (`src/domain/`)**:
  - `entities/connector.entity.ts`: Entidad de conector (id, sourceShapeId, sourcePort, targetShapeId, targetPort, routingType, style, label).
  - `value-objects/connection-port.vo.ts`: Value object inmutable que define la posición relativa (`north`, `south`, `east`, `west`) y las coordenadas absolutas en el nodo.
  - `value-objects/routing-path.vo.ts`: Value object inmutable con la secuencia de puntos ortogonales (puntos intermedios de quiebre en ángulos de 90°).
  - `repositories/connector-state.repository.ts`: Interfaz abstracta para persistencia y consulta de conectores.
- **Aplicacion (`src/application/`)**:
  - `use-cases/create-connector.use-case.ts`: Creación y validación de reglas de conexión (anti-auto-bucles, verificación de existencia de nodos).
  - `use-cases/route-connector.use-case.ts`: Algoritmo de enrutamiento ortogonal (Manhattan/Z-routing o L-routing reactivo).
  - `use-cases/delete-shape-cascade.use-case.ts`: Eliminación atómica de forma y depuración en cascada de conectores vinculados.
- **Infraestructura (`src/infrastructure/`)**:
  - Adaptador en memoria para `IConnectorStateRepository`.
- **Presentacion (`src/presentation/`)**:
  - Actualización de `Canvas.ts` para renderizar puertos magnéticos interactivos en los bordes de los nodos y líneas SVG `<path>` o `<polyline>` con marcador de punta de flecha institucional.

## 2. UI/UX Design System Specification (Design-System First)

- **Arquetipo Visual**: `IMSS Institucional DIDT`
- **Tokens de Color y Estilo para Conectores**:
  - Trazo normal: `#475569` (Gris técnico de alta visibilidad, contraste 4.8:1 con fondo `#F8FAFC`).
  - Trazo seleccionado / activo: `#006341` (Verde IMSS) con ancho 2.5 px.
  - Puertos de anclaje:
    - Estado default: Círculos de 4 px transparentes o sutiles.
    - Estado hover / conexión activa: Círculo de 7 px con fondo dorado `#B38E5D`, borde `#006341` y efecto magnético.
  - Marcador de flecha terminal: SVG `<marker>` con polígono triángulo `#006341` / `#475569`.
- **Accesibilidad**: WCAG 2.1 AA (`role="graphics-connector"`, etiquetas semánticas con identificador de origen y destino legibles por lectores de pantalla).

## 3. Contratos y Esquemas

```typescript
export type PortPosition = 'north' | 'south' | 'east' | 'west';

export interface IConnectorProps {
  id: string;
  sourceShapeId: string;
  sourcePort: PortPosition;
  targetShapeId: string;
  targetPort: PortPosition;
  routingType?: 'orthogonal' | 'straight' | 'curved';
  stroke?: string;
  strokeWidth?: number;
  label?: string;
}

export interface IWayPoint {
  x: number;
  y: number;
}
```

## 4. Allowed Dependencies

Librerias externas de terceros autorizadas:

- `vitest`
- `typescript`

## 5. Security & Threat Modeling (STRIDE / OWASP Sinks)

- **Trust Boundaries (‖)**: Interfaz de Canvas ‖ Repositorio de Conectores en Memoria.
- **Evaluacion STRIDE**:
  - **Spoofing**: N/A para conexiones visuales locales.
  - **Tampering**: Validación de integridad referencial: el use-case verifica que `sourceShapeId !== targetShapeId` y que ambas entidades existan en el canvas.
  - **Repudiation**: Registro de eventos de conexión y desconexión en logs de trazabilidad.
  - **Information Disclosure**: Sanitización de etiquetas de texto en conectores.
  - **Denial of Service**: Algoritmo de enrutamiento O(1) acotado a un máximo de 5 segmentos ortogonales sin bucles infinitos de búsqueda de rutas.
  - **Elevation of Privilege**: Aislamiento estricto en el motor de canvas del cliente.
