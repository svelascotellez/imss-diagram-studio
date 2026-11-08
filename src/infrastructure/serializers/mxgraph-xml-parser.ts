export interface IParsedMxVertex {
  id: string;
  value: string;
  type: 'rectangle' | 'ellipse' | 'diamond' | 'container';
  x: number;
  y: number;
  width: number;
  height: number;
  stroke?: string;
  fill?: string;
  strokeWidth?: number;
}

export interface IParsedMxEdge {
  id: string;
  value: string;
  source: string;
  target: string;
  stroke?: string;
  strokeWidth?: number;
}

export interface IParsedMxGraph {
  vertices: IParsedMxVertex[];
  edges: IParsedMxEdge[];
}

export class MxGraphXmlParser {
  private static readonly MAX_PAYLOAD_SIZE = 5 * 1024 * 1024; // 5 MB

  /**
   * Valida la seguridad del payload XML y bloquea ataques XXE o expansión de entidades
   */
  public static validateSecurity(xmlContent: string): void {
    if (!xmlContent || typeof xmlContent !== 'string') {
      throw new Error('Payload XML inválido o vacío');
    }

    if (xmlContent.length > this.MAX_PAYLOAD_SIZE) {
      throw new Error('El archivo XML excede el límite máximo permitido de 5 MB');
    }

    const lower = xmlContent.toLowerCase();

    // Bloqueo estricto anti-XXE (CWE-611)
    if (
      lower.includes('<!doctype') ||
      lower.includes('<!entity') ||
      lower.includes('system') && lower.includes('dtd') ||
      lower.includes('public') && lower.includes('dtd')
    ) {
      throw new Error('Violación de seguridad: Declaración DOCTYPE/XXE no autorizada en el XML');
    }

    // Validar esquema mxGraphModel
    if (!xmlContent.includes('<mxGraphModel') || !xmlContent.includes('</mxGraphModel>')) {
      throw new Error('El documento no contiene una estructura mxGraphModel válida');
    }

    if (!xmlContent.includes('<root>') || !xmlContent.includes('</root>')) {
      throw new Error('El documento mxGraphModel carece del elemento <root> obligatorio');
    }
  }

  /**
   * Decodifica entidades XML estándar
   */
  private static unescapeXml(text: string): string {
    return text
      .replace(/&apos;/g, "'")
      .replace(/&quot;/g, '"')
      .replace(/&gt;/g, '>')
      .replace(/&lt;/g, '<')
      .replace(/&amp;/g, '&');
  }

  /**
   * Parsea el contenido XML mxGraphModel extrayendo vértices y aristas
   */
  public parse(xmlContent: string): IParsedMxGraph {
    MxGraphXmlParser.validateSecurity(xmlContent);

    const vertices: IParsedMxVertex[] = [];
    const edges: IParsedMxEdge[] = [];

    // Extraer bloques <mxCell>...</mxCell> o <mxCell .../>
    const cellRegex = /<mxCell\b([^>]*?)(?:\/>|>([\s\S]*?)<\/mxCell>)/g;
    let match: RegExpExecArray | null;

    while ((match = cellRegex.exec(xmlContent)) !== null) {
      const attributesStr = match[1] || '';
      const innerContent = match[2] || '';

      const id = this.extractAttribute(attributesStr, 'id');
      // Ignorar celdas raíz 0 y 1
      if (!id || id === '0' || id === '1') {
        continue;
      }

      const isVertex = this.extractAttribute(attributesStr, 'vertex') === '1';
      const isEdge = this.extractAttribute(attributesStr, 'edge') === '1';
      const source = this.extractAttribute(attributesStr, 'source');
      const target = this.extractAttribute(attributesStr, 'target');
      const rawValue = this.extractAttribute(attributesStr, 'value') ?? '';
      const value = MxGraphXmlParser.unescapeXml(rawValue);
      const style = this.extractAttribute(attributesStr, 'style') ?? '';

      if (isEdge || (source && target)) {
        if (!source || !target) {
          continue; // descartar aristas huérfanas
        }

        const stroke = this.extractStyleProperty(style, 'strokeColor') ?? '#475569';
        const strokeWidthStr = this.extractStyleProperty(style, 'strokeWidth');
        const strokeWidth = strokeWidthStr ? parseFloat(strokeWidthStr) : 2;

        edges.push({
          id,
          value,
          source,
          target,
          stroke,
          strokeWidth
        });
      } else if (isVertex || innerContent.includes('<mxGeometry')) {
        // Extraer geometría
        const geomMatch = /<mxGeometry\b([^>]*?)\/?>/.exec(innerContent);
        const geomAttrs = geomMatch ? geomMatch[1] : '';

        const xStr = this.extractAttribute(geomAttrs, 'x') ?? '0';
        const yStr = this.extractAttribute(geomAttrs, 'y') ?? '0';
        const wStr = this.extractAttribute(geomAttrs, 'width') ?? '120';
        const hStr = this.extractAttribute(geomAttrs, 'height') ?? '60';

        const x = parseFloat(xStr) || 0;
        const y = parseFloat(yStr) || 0;
        const width = Math.max(20, parseFloat(wStr) || 120);
        const height = Math.max(20, parseFloat(hStr) || 60);

        // Detectar tipo
        let type: 'rectangle' | 'ellipse' | 'diamond' | 'container' = 'rectangle';
        if (style.includes('ellipse')) {
          type = 'ellipse';
        } else if (style.includes('rhombus')) {
          type = 'diamond';
        } else if (style.includes('swimlane')) {
          type = 'container';
        }

        const stroke = this.extractStyleProperty(style, 'strokeColor') ?? '#006341';
        const fill = this.extractStyleProperty(style, 'fillColor') ?? '#FFFFFF';
        const strokeWidthStr = this.extractStyleProperty(style, 'strokeWidth');
        const strokeWidth = strokeWidthStr ? parseFloat(strokeWidthStr) : 2;

        vertices.push({
          id,
          value,
          type,
          x,
          y,
          width,
          height,
          stroke,
          fill,
          strokeWidth
        });
      }
    }

    return { vertices, edges };
  }

  private extractAttribute(attrString: string, attrName: string): string | null {
    const regex = new RegExp(`\\b${attrName}="([^"]*)"`, 'i');
    const match = regex.exec(attrString);
    return match ? match[1] : null;
  }

  private extractStyleProperty(styleString: string, propName: string): string | null {
    const regex = new RegExp(`(?:^|;)${propName}=([^;]+)`, 'i');
    const match = regex.exec(styleString);
    return match ? match[1].trim() : null;
  }
}
