import { ICanvasStateRepository } from '../../domain/repositories/canvas-state.repository.js';
import { IConnectorStateRepository } from '../../domain/repositories/connector-state.repository.js';
import { MxGraphXmlParser } from '../../infrastructure/serializers/mxgraph-xml-parser.js';
import { ShapeEntity } from '../../domain/entities/shape.entity.js';
import { ConnectorEntity } from '../../domain/entities/connector.entity.js';
import { Point } from '../../domain/value-objects/point.vo.js';
import { Dimensions } from '../../domain/value-objects/dimensions.vo.js';
import { PortPosition } from '../../domain/value-objects/connection-port.vo.js';

export interface IImportDrawioXmlRequest {
  xmlContent: string;
  clearExisting?: boolean;
}

export interface IImportDrawioXmlResult {
  success: boolean;
  importedShapesCount: number;
  importedConnectorsCount: number;
}

export class ImportDrawioXmlUseCase {
  private readonly parser: MxGraphXmlParser;

  constructor(
    private readonly canvasRepo: ICanvasStateRepository,
    private readonly connectorRepo: IConnectorStateRepository
  ) {
    this.parser = new MxGraphXmlParser();
  }

  async execute(request: IImportDrawioXmlRequest): Promise<IImportDrawioXmlResult> {
    // 1. Parseo y validación de seguridad (falla atómicamente antes de tocar el canvas)
    const parsedGraph = this.parser.parse(request.xmlContent);

    const clearExisting = request.clearExisting ?? true;
    if (clearExisting) {
      await this.connectorRepo.clear();
      await this.canvasRepo.clear();
    }

    const createdShapesMap = new Map<string, ShapeEntity>();

    // 2. Instanciar e insertar formas
    for (const v of parsedGraph.vertices) {
      const shape = new ShapeEntity({
        id: v.id,
        type: v.type,
        position: new Point(v.x, v.y),
        dimensions: new Dimensions(v.width, v.height),
        label: v.value,
        style: {
          stroke: v.stroke,
          fill: v.fill,
          strokeWidth: v.strokeWidth
        }
      });
      await this.canvasRepo.save(shape);
      createdShapesMap.set(shape.id, shape);
    }

    // 3. Instanciar e insertar conectores
    let connectorCount = 0;
    for (const e of parsedGraph.edges) {
      const sourceShape = createdShapesMap.get(e.source);
      const targetShape = createdShapesMap.get(e.target);

      // Si las formas origen y destino existen en el modelo importado
      if (sourceShape && targetShape) {
        // Asignación heurística de puertos basada en posiciones relativas
        let sourcePort: PortPosition = 'east';
        let targetPort: PortPosition = 'west';

        if (Math.abs(targetShape.position.x - sourceShape.position.x) < 50) {
          if (targetShape.position.y > sourceShape.position.y) {
            sourcePort = 'south';
            targetPort = 'north';
          } else {
            sourcePort = 'north';
            targetPort = 'south';
          }
        }

        const connector = new ConnectorEntity({
          id: e.id,
          sourceShapeId: e.source,
          sourcePort,
          targetShapeId: e.target,
          targetPort,
          routingType: 'orthogonal',
          stroke: e.stroke,
          strokeWidth: e.strokeWidth,
          label: e.value
        });

        await this.connectorRepo.save(connector);
        connectorCount++;
      }
    }

    return {
      success: true,
      importedShapesCount: createdShapesMap.size,
      importedConnectorsCount: connectorCount
    };
  }
}
