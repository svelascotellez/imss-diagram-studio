import { ICanvasStateRepository } from '../../domain/repositories/canvas-state.repository.js';
import { IConnectorStateRepository } from '../../domain/repositories/connector-state.repository.js';
import { RoutingPath } from '../../domain/value-objects/routing-path.vo.js';
import { ConnectionPort } from '../../domain/value-objects/connection-port.vo.js';
import { Point } from '../../domain/value-objects/point.vo.js';

export class RouteConnectorUseCase {
  constructor(
    private readonly shapeRepository: ICanvasStateRepository,
    private readonly connectorRepository: IConnectorStateRepository
  ) {}

  async computePath(connectorId: string): Promise<RoutingPath> {
    const connector = await this.connectorRepository.findById(connectorId);
    if (!connector) {
      throw new Error(`Connector '${connectorId}' not found`);
    }

    const sourceShape = await this.shapeRepository.findById(connector.sourceShapeId);
    if (!sourceShape) {
      throw new Error(`Source shape '${connector.sourceShapeId}' not found for connector`);
    }

    const targetShape = await this.shapeRepository.findById(connector.targetShapeId);
    if (!targetShape) {
      throw new Error(`Target shape '${connector.targetShapeId}' not found for connector`);
    }

    const sourcePortVo = new ConnectionPort(connector.sourcePort);
    const targetPortVo = new ConnectionPort(connector.targetPort);

    const startPoint = sourcePortVo.computeAbsolutePoint(sourceShape.boundingBox);
    const endPoint = targetPortVo.computeAbsolutePoint(targetShape.boundingBox);

    const waypoints = this.calculateOrthogonalWaypoints(
      startPoint,
      connector.sourcePort,
      endPoint,
      connector.targetPort
    );

    return new RoutingPath(waypoints);
  }

  private calculateOrthogonalWaypoints(
    start: Point,
    startPort: string,
    end: Point,
    endPort: string
  ): Point[] {
    // Si ya están alineados horizontal o verticalmente
    if (Math.abs(start.x - end.x) < 0.001 || Math.abs(start.y - end.y) < 0.001) {
      return [start, end];
    }

    // Algoritmo Ortogonal Z/L en ángulos rectos de 90 grados
    if (startPort === 'east' || startPort === 'west') {
      const midX = Math.round((start.x + end.x) / 2);
      return [
        start,
        new Point(midX, start.y),
        new Point(midX, end.y),
        end
      ];
    } else {
      const midY = Math.round((start.y + end.y) / 2);
      return [
        start,
        new Point(start.x, midY),
        new Point(end.x, midY),
        end
      ];
    }
  }
}
