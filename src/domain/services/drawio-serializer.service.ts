import { ShapeEntity } from '../entities/shape.entity.js';
import { ConnectorEntity } from '../entities/connector.entity.js';

export interface IDrawioSerializationOptions {
  grid?: number;
  gridSize?: number;
  pageWidth?: number;
  pageHeight?: number;
}

export class DrawioSerializerService {
  /**
   * Escapa caracteres especiales para atributos y valores XML seguros
   */
  public static escapeXml(text: string): string {
    return text
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&apos;');
  }

  /**
   * Genera el estilo visual compatible con mxGraph según el tipo y colores de la forma
   */
  public static deriveMxStyle(shape: ShapeEntity): string {
    const stroke = shape.style.stroke || '#006341';
    const fill = shape.style.fill || '#FFFFFF';
    const strokeWidth = shape.style.strokeWidth || 2;

    let shapeStyle = 'whiteSpace=wrap;html=1;';
    switch (shape.type) {
      case 'ellipse':
        shapeStyle += 'ellipse;';
        break;
      case 'diamond':
        shapeStyle += 'rhombus;';
        break;
      case 'container':
        shapeStyle += 'swimlane;';
        break;
      case 'rectangle':
      default:
        shapeStyle += 'rounded=1;';
        break;
    }

    return `${shapeStyle}strokeColor=${stroke};fillColor=${fill};strokeWidth=${strokeWidth};`;
  }

  /**
   * Serializa formas y conectores en un documento XML estándar <mxGraphModel>
   */
  public serialize(
    shapes: ShapeEntity[],
    connectors: ConnectorEntity[],
    options?: IDrawioSerializationOptions
  ): string {
    const gridSize = options?.gridSize ?? 10;
    const pageWidth = options?.pageWidth ?? 827;
    const pageHeight = options?.pageHeight ?? 1169;

    let xml = `<mxGraphModel dx="1422" dy="794" grid="1" gridSize="${gridSize}" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="${pageWidth}" pageHeight="${pageHeight}" math="0" shadow="0">\n`;
    xml += '  <root>\n';
    xml += '    <mxCell id="0"/>\n';
    xml += '    <mxCell id="1" parent="0"/>\n';

    // Serializar Shapes (Nodos)
    for (const shape of shapes) {
      const escapedValue = DrawioSerializerService.escapeXml(shape.label);
      const style = DrawioSerializerService.deriveMxStyle(shape);
      const x = Math.round(shape.position.x);
      const y = Math.round(shape.position.y);
      const width = Math.round(shape.dimensions.width);
      const height = Math.round(shape.dimensions.height);

      xml += `    <mxCell id="${shape.id}" value="${escapedValue}" style="${style}" vertex="1" parent="1">\n`;
      xml += `      <mxGeometry x="${x}" y="${y}" width="${width}" height="${height}" as="geometry"/>\n`;
      xml += '    </mxCell>\n';
    }

    // Serializar Conectores (Edges)
    for (const conn of connectors) {
      const escapedValue = DrawioSerializerService.escapeXml(conn.label);
      const stroke = conn.stroke || '#475569';
      const strokeWidth = conn.strokeWidth || 2;
      const arrowStyle = conn.hasEndArrow ? 'endArrow=classic;' : 'endArrow=none;';
      const style = `edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=${stroke};strokeWidth=${strokeWidth};${arrowStyle}`;

      xml += `    <mxCell id="${conn.id}" value="${escapedValue}" style="${style}" edge="1" parent="1" source="${conn.sourceShapeId}" target="${conn.targetShapeId}">\n`;
      xml += '      <mxGeometry relative="1" as="geometry"/>\n';
      xml += '    </mxCell>\n';
    }

    xml += '  </root>\n';
    xml += '</mxGraphModel>';

    return xml;
  }
}
