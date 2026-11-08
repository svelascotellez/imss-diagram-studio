import { ConnectorEntity } from '../../domain/entities/connector.entity.js';
import { PortPosition } from '../../domain/value-objects/connection-port.vo.js';
import { ICanvasStateRepository } from '../../domain/repositories/canvas-state.repository.js';
import { IConnectorStateRepository } from '../../domain/repositories/connector-state.repository.js';

export interface ICreateConnectorDTO {
  id?: string;
  sourceShapeId: string;
  sourcePort: PortPosition;
  targetShapeId: string;
  targetPort: PortPosition;
  routingType?: 'orthogonal' | 'straight' | 'curved';
  label?: string;
}

export class CreateConnectorUseCase {
  constructor(
    private readonly shapeRepository: ICanvasStateRepository,
    private readonly connectorRepository: IConnectorStateRepository
  ) {}

  async execute(dto: ICreateConnectorDTO): Promise<ConnectorEntity> {
    // AC-2.2: Bloqueo de auto-bucles (conectar un puerto hacia sí mismo)
    if (dto.sourceShapeId === dto.targetShapeId) {
      throw new Error('Self-loop connection is not allowed on the same shape');
    }

    const validPorts: PortPosition[] = ['north', 'south', 'east', 'west'];
    if (!validPorts.includes(dto.sourcePort) || !validPorts.includes(dto.targetPort)) {
      throw new Error(`Invalid port specified: ${dto.sourcePort} -> ${dto.targetPort}`);
    }

    // Verificar que ambas entidades existan en el canvas
    const sourceShape = await this.shapeRepository.findById(dto.sourceShapeId);
    if (!sourceShape) {
      throw new Error(`Source shape '${dto.sourceShapeId}' does not exist on canvas`);
    }

    const targetShape = await this.shapeRepository.findById(dto.targetShapeId);
    if (!targetShape) {
      throw new Error(`Target shape '${dto.targetShapeId}' does not exist on canvas`);
    }

    const id = dto.id ?? `conn_${Date.now()}_${Math.random().toString(36).substring(2, 9)}`;

    const connector = new ConnectorEntity({
      id,
      sourceShapeId: dto.sourceShapeId,
      sourcePort: dto.sourcePort,
      targetShapeId: dto.targetShapeId,
      targetPort: dto.targetPort,
      routingType: dto.routingType ?? 'orthogonal',
      label: dto.label
    });

    await this.connectorRepository.save(connector);
    return connector;
  }
}
