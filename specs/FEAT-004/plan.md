# Plan Tecnico de Implementacion: FEAT-004

## 1. Diseno Arquitectonico (Clean Architecture)

- **Dominio (`src/domain/`)**:
  - `services/drawio-serializer.service.ts`: Servicio de dominio para serialización y mapeo entre entidades (`ShapeEntity`, `ConnectorEntity`) y modelos de celda `<mxGraphModel>`.
  - `value-objects/diagram-export.vo.ts`: Value object inmutable que encapsula el payload exportado (tipo de formato, contenido, timestamp, metadatos institucionales).
- **Aplicacion (`src/application/`)**:
  - `use-cases/export-drawio-xml.use-case.ts`: Caso de uso para serializar el estado del canvas a XML Draw.io estándar.
  - `use-cases/import-drawio-xml.use-case.ts`: Caso de uso para parsear e importar modelos `<mxGraphModel>` con validación estricta y protección anti-XXE.
  - `use-cases/export-svg-diagram.use-case.ts`: Caso de uso para generar SVG vectorial con membrete oficial institucional DIDT IMSS.
- **Infraestructura (`src/infrastructure/`)**:
  - `serializers/mxgraph-xml-parser.ts`: Parser seguro XML (libree de XXE) para decodificar `<mxGraphModel>`, `<root>`, `<mxCell>` y `<mxGeometry>`.
- **Presentacion (`src/presentation/`)**:
  - Actualización de `Canvas.ts` para soportar importación y exportación de archivos locales.

## 2. UI/UX Design System Specification (Design-System First)

- **Arquetipo Visual**: `IMSS Institucional DIDT`
- **Membrete Vectorial Oficial para SVG**:
  - Encabezado: Franja Verde IMSS (`#006341`) con texto institucional "DIRECCIÓN DE INNOVACIÓN Y DESARROLLO TECNOLÓGICO — IMSS".
  - Tipografía: `Inter, sans-serif` en blanco (`#FFFFFF`) con ratio de contraste 7.34:1 (Cumple AAA).
  - Pie de página: Fecha UTC, versión del diagrama y etiqueta de gobernanza SDD v6.6.
- **Accesibilidad**: WCAG 2.1 AA (`role="img"`, `aria-label="Diagrama de Arquitectura Técnica DIDT IMSS"`).

## 3. Contratos y Esquemas

```typescript
export interface IMxCellNode {
  id: string;
  value: string;
  isVertex: boolean;
  isEdge: boolean;
  parent?: string;
  source?: string;
  target?: string;
  x?: number;
  y?: number;
  width?: number;
  height?: number;
  style?: string;
}

export interface IDiagramExportResult {
  format: 'drawio_xml' | 'svg' | 'json';
  content: string;
  filename: string;
  mimeType: string;
}
```

## 4. Allowed Dependencies

Librerias externas de terceros autorizadas:

- `vitest`
- `typescript`

## 5. Security & Threat Modeling (STRIDE / OWASP Sinks)

- **Trust Boundaries (‖)**: Carga de archivo externo del usuario ‖ Parser XML en Memoria.
- **Evaluacion STRIDE**:
  - **Spoofing**: N/A para archivos locales importados por el operador.
  - **Tampering**: Validación de estructura contra esquema `<mxGraphModel>`; celdas huérfanas o malformadas son descartadas.
  - **Repudiation**: Inclusión de hash de integridad y fecha en los metadatos exportados.
  - **Information Disclosure / XXE (CWE-611)**: El parser prohíbe explícitamente declaraciones `<!DOCTYPE` con `SYSTEM` o `PUBLIC`, bloqueando cualquier vector de ataque XXE o expansión de billones de risas (*Billion Laughs*).
  - **Denial of Service**: Límite de tamaño máximo de archivo importado (5 MB) y límite de profundidad de nodos XML (máximo 5 niveles).
  - **Elevation of Privilege**: El parser opera en memoria estricta sin acceso al sistema de archivos del host.
