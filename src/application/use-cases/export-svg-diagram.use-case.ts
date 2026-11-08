import { ICanvasStateRepository } from '../../domain/repositories/canvas-state.repository.js';
import { IConnectorStateRepository } from '../../domain/repositories/connector-state.repository.js';
import { DiagramExportVO } from '../../domain/value-objects/diagram-export.vo.js';
import { DrawioSerializerService } from '../../domain/services/drawio-serializer.service.js';
import { RouteConnectorUseCase } from './route-connector.use-case.js';

export interface IExportSvgDiagramRequest {
  title?: string;
  author?: string;
}

export class ExportSvgDiagramUseCase {
  private readonly router: RouteConnectorUseCase;

  constructor(
    private readonly canvasRepo: ICanvasStateRepository,
    private readonly connectorRepo: IConnectorStateRepository
  ) {
    this.router = new RouteConnectorUseCase(canvasRepo, connectorRepo);
  }

  async execute(request?: IExportSvgDiagramRequest): Promise<DiagramExportVO> {
    const title = request?.title || 'Diagrama de Arquitectura DIDT IMSS';
    const author = request?.author || 'Dirección de Innovación y Desarrollo Tecnológico (DIDT)';
    const shapes = await this.canvasRepo.findAll();
    const connectors = await this.connectorRepo.findAll();

    // Calcular dimensiones globales
    let minX = 0;
    let minY = 0;
    let maxX = 1200;
    let maxY = 800;

    if (shapes.length > 0) {
      minX = Math.min(...shapes.map(s => s.position.x)) - 60;
      minY = Math.min(...shapes.map(s => s.position.y)) - 100;
      maxX = Math.max(...shapes.map(s => s.position.x + s.dimensions.width)) + 60;
      maxY = Math.max(...shapes.map(s => s.position.y + s.dimensions.height)) + 100;
    }

    const canvasWidth = Math.max(1200, maxX - Math.min(0, minX));
    const canvasHeight = Math.max(800, maxY - Math.min(0, minY));
    const nowIso = new Date().toISOString().split('T')[0];

    let svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${canvasWidth} ${canvasHeight}" width="${canvasWidth}" height="${canvasHeight}" role="img" aria-label="Diagrama de Arquitectura DIDT IMSS">\n`;
    svg += '  <defs>\n';
    svg += '    <style>\n';
    svg += '      .imss-title { font-family: Inter, system-ui, sans-serif; font-size: 15px; font-weight: 700; fill: #FFFFFF; }\n';
    svg += '      .imss-sub { font-family: Inter, system-ui, sans-serif; font-size: 11px; fill: #E2E8F0; }\n';
    svg += '      .imss-node-label { font-family: Inter, system-ui, sans-serif; font-size: 12px; font-weight: 600; fill: #0F172A; text-anchor: middle; dominant-baseline: middle; }\n';
    svg += '      .imss-footer { font-family: Inter, system-ui, sans-serif; font-size: 10px; fill: #64748B; }\n';
    svg += '    </style>\n';
    svg += '    <marker id="arrowhead-imss" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">\n';
    svg += '      <polygon points="0 0, 10 3.5, 0 7" fill="#006341" />\n';
    svg += '    </marker>\n';
    svg += '    <pattern id="imss-grid" width="20" height="20" patternUnits="userSpaceOnUse">\n';
    svg += '      <circle cx="2" cy="2" r="1" fill="#CBD5E1" opacity="0.5" />\n';
    svg += '    </pattern>\n';
    svg += '  </defs>\n';

    // Fondo del lienzo y rejilla
    svg += `  <rect width="${canvasWidth}" height="${canvasHeight}" fill="#F8FAFC" />\n`;
    svg += `  <rect y="70" width="${canvasWidth}" height="${canvasHeight - 110}" fill="url(#imss-grid)" />\n`;

    // 1. Membrete Superior Institucional Oficial
    svg += `  <g id="imss-letterhead">\n`;
    svg += `    <rect x="0" y="0" width="${canvasWidth}" height="64" fill="#006341" />\n`;
    svg += `    <rect x="0" y="64" width="${canvasWidth}" height="4" fill="#B38E5D" />\n`;
    svg += `    <text x="24" y="28" class="imss-title">DIRECCION DE INNOVACION Y DESARROLLO TECNOLOGICO — IMSS</text>\n`;
    svg += `    <text x="24" y="48" class="imss-sub">${DrawioSerializerService.escapeXml(title)} | Emisión: ${nowIso} | Autor: ${DrawioSerializerService.escapeXml(author)}</text>\n`;
    svg += `  </g>\n`;

    // 2. Conectores Ortogonales
    svg += '  <g id="imss-connectors">\n';
    for (const conn of connectors) {
      try {
        const route = await this.router.computePath(conn.id);
        const d = route.toSvgPathData();
        svg += `    <path d="${d}" fill="none" stroke="${conn.stroke || '#006341'}" stroke-width="${conn.strokeWidth || 2}" marker-end="url(#arrowhead-imss)" />\n`;
      } catch {
        // En caso de que alguna forma haya sido borrada
      }
    }
    svg += '  </g>\n';

    // 3. Formas (Nodos)
    svg += '  <g id="imss-shapes">\n';
    for (const shape of shapes) {
      const x = shape.position.x;
      const y = shape.position.y;
      const w = shape.dimensions.width;
      const h = shape.dimensions.height;
      const stroke = shape.style.stroke || '#006341';
      const fill = shape.style.fill || '#FFFFFF';
      const strokeWidth = shape.style.strokeWidth || 2;
      const label = DrawioSerializerService.escapeXml(shape.label);

      if (shape.type === 'ellipse') {
        const rx = w / 2;
        const ry = h / 2;
        const cx = x + rx;
        const cy = y + ry;
        svg += `    <ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="${fill}" stroke="${stroke}" stroke-width="${strokeWidth}" />\n`;
      } else if (shape.type === 'diamond') {
        const points = `${x + w / 2},${y} ${x + w},${y + h / 2} ${x + w / 2},${y + h} ${x},${y + h / 2}`;
        svg += `    <polygon points="${points}" fill="${fill}" stroke="${stroke}" stroke-width="${strokeWidth}" />\n`;
      } else {
        svg += `    <rect x="${x}" y="${y}" width="${w}" height="${h}" rx="6" fill="${fill}" stroke="${stroke}" stroke-width="${strokeWidth}" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.06))" />\n`;
      }

      if (label) {
        svg += `    <text x="${x + w / 2}" y="${y + h / 2}" class="imss-node-label">${label}</text>\n`;
      }
    }
    svg += '  </g>\n';

    // 4. Pie de Página Institucional
    svg += `  <g id="imss-footer" transform="translate(0, ${canvasHeight - 36})">\n`;
    svg += `    <rect x="0" y="0" width="${canvasWidth}" height="36" fill="#F1F5F9" />\n`;
    svg += `    <rect x="0" y="0" width="${canvasWidth}" height="2" fill="#CBD5E1" />\n`;
    svg += `    <text x="24" y="22" class="imss-footer">INSTITUTO MEXICANO DEL SEGURO SOCIAL | GOBERNANZA SDD v6.6 REGULATORY HARDENED EDITION | CONFIDENCIAL DIDT</text>\n`;
    svg += `  </g>\n`;

    svg += '</svg>';

    const sanitizedFilename = title
      .toLowerCase()
      .replace(/[^a-z0-9_-]/g, '_')
      .replace(/_+/g, '_');

    return new DiagramExportVO({
      format: 'svg',
      content: svg,
      filename: `${sanitizedFilename}.svg`,
      mimeType: 'image/svg+xml',
      title
    });
  }
}
