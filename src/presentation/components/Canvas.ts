import { ICanvasStateRepository } from '../../domain/repositories/canvas-state.repository.js';
import { IConnectorStateRepository } from '../../domain/repositories/connector-state.repository.js';
import { IStencilCatalogRepository } from '../../domain/repositories/stencil-catalog.repository.js';
import { CreateShapeUseCase } from '../../application/use-cases/create-shape.use-case.js';
import { SelectShapesUseCase } from '../../application/use-cases/select-shapes.use-case.js';
import { MoveShapesUseCase } from '../../application/use-cases/move-shapes.use-case.js';
import { CreateConnectorUseCase } from '../../application/use-cases/create-connector.use-case.js';
import { RouteConnectorUseCase } from '../../application/use-cases/route-connector.use-case.js';
import { DeleteShapeCascadeUseCase } from '../../application/use-cases/delete-shape-cascade.use-case.js';
import { InstantiateStencilUseCase } from '../../application/use-cases/instantiate-stencil.use-case.js';
import { ExportDrawioXmlUseCase } from '../../application/use-cases/export-drawio-xml.use-case.js';
import { ImportDrawioXmlUseCase, IImportDrawioXmlResult } from '../../application/use-cases/import-drawio-xml.use-case.js';
import { ExportSvgDiagramUseCase } from '../../application/use-cases/export-svg-diagram.use-case.js';
import { DiagramExportVO } from '../../domain/value-objects/diagram-export.vo.js';
import { ShapeEntity } from '../../domain/entities/shape.entity.js';
import { ConnectionPort, PortPosition } from '../../domain/value-objects/connection-port.vo.js';

export interface ICanvasConfig {
  width?: number;
  height?: number;
  backgroundColor?: string;
  gridSize?: number;
}

export class Canvas {
  private width: number;
  private height: number;
  private backgroundColor: string;
  private gridSize: number;
  public readonly createUseCase: CreateShapeUseCase;
  public readonly selectUseCase: SelectShapesUseCase;
  public readonly moveUseCase: MoveShapesUseCase;
  public readonly createConnectorUseCase?: CreateConnectorUseCase;
  public readonly routeConnectorUseCase?: RouteConnectorUseCase;
  public readonly deleteCascadeUseCase?: DeleteShapeCascadeUseCase;
  public readonly instantiateStencilUseCase?: InstantiateStencilUseCase;
  public readonly exportDrawioUseCase?: ExportDrawioXmlUseCase;
  public readonly importDrawioUseCase?: ImportDrawioXmlUseCase;
  public readonly exportSvgUseCase?: ExportSvgDiagramUseCase;

  constructor(
    private readonly shapeRepository: ICanvasStateRepository,
    private readonly connectorRepository?: IConnectorStateRepository,
    private readonly stencilRepository?: IStencilCatalogRepository,
    config: ICanvasConfig = {}
  ) {
    this.width = config.width ?? 1920;
    this.height = config.height ?? 1080;
    this.backgroundColor = config.backgroundColor ?? '#F8FAFC';
    this.gridSize = config.gridSize ?? 8; // 8px grid SDD design tokens

    this.createUseCase = new CreateShapeUseCase(this.shapeRepository);
    this.selectUseCase = new SelectShapesUseCase(this.shapeRepository);
    this.moveUseCase = new MoveShapesUseCase(this.shapeRepository);

    if (this.connectorRepository) {
      this.createConnectorUseCase = new CreateConnectorUseCase(this.shapeRepository, this.connectorRepository);
      this.routeConnectorUseCase = new RouteConnectorUseCase(this.shapeRepository, this.connectorRepository);
      this.deleteCascadeUseCase = new DeleteShapeCascadeUseCase(this.shapeRepository, this.connectorRepository);
      this.exportDrawioUseCase = new ExportDrawioXmlUseCase(this.shapeRepository, this.connectorRepository);
      this.importDrawioUseCase = new ImportDrawioXmlUseCase(this.shapeRepository, this.connectorRepository);
      this.exportSvgUseCase = new ExportSvgDiagramUseCase(this.shapeRepository, this.connectorRepository);
    }

    if (this.stencilRepository) {
      this.instantiateStencilUseCase = new InstantiateStencilUseCase(this.stencilRepository, this.shapeRepository);
    }
  }

  async getShapes(): Promise<ShapeEntity[]> {
    return this.shapeRepository.findAll();
  }

  async renderSvgString(): Promise<string> {
    const shapes = await this.shapeRepository.findAll();
    const selected = shapes.filter(s => s.isSelected);
    const connectors = this.connectorRepository ? await this.connectorRepository.findAll() : [];

    if (shapes.length === 0 && connectors.length === 0) {
      return `
<svg width="${this.width}" height="${this.height}" viewBox="0 0 ${this.width} ${this.height}"
     role="graphics-document" aria-label="Canvas de Diagramación DIDT IMSS"
     tabindex="0" style="background-color: ${this.backgroundColor};">
  <g role="status" aria-live="polite">
    <text x="${this.width / 2}" y="${this.height / 2}" text-anchor="middle"
          fill="#475569" font-family="Inter, sans-serif" font-size="16">
      No hay formas en el canvas. Selecciona una herramienta para comenzar.
    </text>
  </g>
</svg>`.trim();
    }

    const shapeElements = shapes.map(s => this.renderShapeSvg(s)).join('\n  ');

    let connectorElements = '';
    if (this.routeConnectorUseCase && connectors.length > 0) {
      const renderedConns: string[] = [];
      for (const conn of connectors) {
        try {
          const path = await this.routeConnectorUseCase.computePath(conn.id);
          const pathData = path.toSvgPathData();
          renderedConns.push(`
  <g id="${conn.id}" role="graphics-connector" aria-label="Conexion ${conn.label || conn.id}">
    <path d="${pathData}" fill="none" stroke="${conn.stroke}" stroke-width="${conn.strokeWidth}"
          marker-end="url(#arrowhead-imss)" />
    ${conn.label ? `<text x="${(path.waypoints[0].x + path.waypoints[path.waypoints.length - 1].x) / 2}" y="${(path.waypoints[0].y + path.waypoints[path.waypoints.length - 1].y) / 2 - 6}" fill="#0F172A" font-family="Inter, sans-serif" font-size="11" text-anchor="middle">${conn.label}</text>` : ''}
  </g>`.trim());
        } catch {
          // Si el conector está en estado huérfano provisional
        }
      }
      connectorElements = renderedConns.join('\n  ');
    }

    let selectionOverlay = '';
    if (selected.length > 0) {
      let minX = Infinity;
      let minY = Infinity;
      let maxX = -Infinity;
      let maxY = -Infinity;

      for (const s of selected) {
        const bb = s.boundingBox;
        minX = Math.min(minX, bb.x);
        minY = Math.min(minY, bb.y);
        maxX = Math.max(maxX, bb.x + bb.width);
        maxY = Math.max(maxY, bb.y + bb.height);
      }

      const selW = maxX - minX;
      const selH = maxY - minY;

      selectionOverlay = `
  <!-- AC-1.3: Overlay de selección unificado con acento institucional dorado #B38E5D -->
  <g class="selection-overlay" role="presentation">
    <rect x="${minX - 4}" y="${minY - 4}" width="${selW + 8}" height="${selH + 8}"
          fill="none" stroke="#B38E5D" stroke-width="1.5" stroke-dasharray="4 4" />
    <circle cx="${minX - 4}" cy="${minY - 4}" r="4" fill="#006341" stroke="#FFFFFF" />
    <circle cx="${maxX + 4}" cy="${minY - 4}" r="4" fill="#006341" stroke="#FFFFFF" />
    <circle cx="${maxX + 4}" cy="${maxY + 4}" r="4" fill="#006341" stroke="#FFFFFF" />
    <circle cx="${minX - 4}" cy="${maxY + 4}" r="4" fill="#006341" stroke="#FFFFFF" />
  </g>`;
    }

    return `
<svg width="${this.width}" height="${this.height}" viewBox="0 0 ${this.width} ${this.height}"
     role="graphics-document" aria-label="Canvas de Diagramación DIDT IMSS"
     tabindex="0" style="background-color: ${this.backgroundColor};">
  <defs>
    <pattern id="grid-pattern" width="${this.gridSize * 2}" height="${this.gridSize * 2}" patternUnits="userSpaceOnUse">
      <path d="M ${this.gridSize * 2} 0 L 0 0 0 ${this.gridSize * 2}" fill="none" stroke="#E2E8F0" stroke-width="0.5"/>
    </pattern>
    <!-- Marcador de flecha institucional IMSS -->
    <marker id="arrowhead-imss" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#006341" />
    </marker>
  </defs>
  <rect width="100%" height="100%" fill="url(#grid-pattern)" />
  ${connectorElements}
  ${shapeElements}
  ${selectionOverlay}
</svg>`.trim();
  }

  private renderShapeSvg(shape: ShapeEntity): string {
    const { x, y, width, height } = shape.boundingBox;
    const stroke = shape.isSelected ? '#004D32' : shape.style.stroke;
    const strokeWidth = shape.isSelected ? 3 : shape.style.strokeWidth;
    const fill = shape.style.fill;
    const ariaSelected = shape.isSelected ? 'true' : 'false';

    let shapeGeometry = '';
    switch (shape.type) {
      case 'rectangle':
      case 'container':
        shapeGeometry = `<rect x="${x}" y="${y}" width="${width}" height="${height}" rx="4" ry="4" fill="${fill}" stroke="${stroke}" stroke-width="${strokeWidth}"/>`;
        break;
      case 'ellipse':
        shapeGeometry = `<ellipse cx="${x + width / 2}" cy="${y + height / 2}" rx="${width / 2}" ry="${height / 2}" fill="${fill}" stroke="${stroke}" stroke-width="${strokeWidth}"/>`;
        break;
      case 'diamond':
        const points = `${x + width / 2},${y} ${x + width},${y + height / 2} ${x + width / 2},${y + height} ${x},${y + height / 2}`;
        shapeGeometry = `<polygon points="${points}" fill="${fill}" stroke="${stroke}" stroke-width="${strokeWidth}"/>`;
        break;
      case 'text':
        shapeGeometry = `<text x="${x}" y="${y + height / 2}" fill="#0F172A" font-family="Inter, sans-serif" font-size="14">${shape.label || 'Texto'}</text>`;
        break;
    }

    const labelText = shape.label
      ? `<text x="${x + width / 2}" y="${y + height / 2}" text-anchor="middle" dominant-baseline="middle" fill="#0F172A" font-family="Inter, sans-serif" font-size="12" font-weight="500">${shape.label}</text>`
      : '';

    // Puertos magnéticos de conexión (Norte, Sur, Este, Oeste)
    const ports: PortPosition[] = ['north', 'south', 'east', 'west'];
    const portCircles = ports.map(p => {
      const pt = new ConnectionPort(p).computeAbsolutePoint(shape.boundingBox);
      return `<circle class="port port-${p}" cx="${pt.x}" cy="${pt.y}" r="4" fill="#B38E5D" stroke="#006341" stroke-width="1.5" opacity="0.8"/>`;
    }).join('');

    return `
  <g id="${shape.id}" role="graphics-symbol" aria-selected="${ariaSelected}" tabindex="0">
    ${shapeGeometry}
    ${labelText}
    <g class="ports-container" opacity="0.6">
      ${portCircles}
    </g>
  </g>`.trim();
  }

  async handleKeyNudge(direction: 'up' | 'down' | 'left' | 'right', delta: number = 5): Promise<void> {
    const dx = direction === 'left' ? -delta : direction === 'right' ? delta : 0;
    const dy = direction === 'up' ? -delta : direction === 'down' ? delta : 0;
    await this.moveUseCase.executeSelected(dx, dy);
  }

  async exportToDrawioXml(title?: string): Promise<DiagramExportVO> {
    if (!this.exportDrawioUseCase) {
      throw new Error('ExportDrawioXmlUseCase no está configurado (falta connectorRepository)');
    }
    return this.exportDrawioUseCase.execute({ title });
  }

  async importFromDrawioXml(xmlContent: string, clearExisting: boolean = true): Promise<IImportDrawioXmlResult> {
    if (!this.importDrawioUseCase) {
      throw new Error('ImportDrawioXmlUseCase no está configurado (falta connectorRepository)');
    }
    return this.importDrawioUseCase.execute({ xmlContent, clearExisting });
  }

  async exportSvgWithLetterhead(title?: string, author?: string): Promise<DiagramExportVO> {
    if (!this.exportSvgUseCase) {
      throw new Error('ExportSvgDiagramUseCase no está configurado (falta connectorRepository)');
    }
    return this.exportSvgUseCase.execute({ title, author });
  }
}

