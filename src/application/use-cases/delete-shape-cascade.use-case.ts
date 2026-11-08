import { ICanvasStateRepository } from '../../domain/repositories/canvas-state.repository.js';
import { IConnectorStateRepository } from '../../domain/repositories/connector-state.repository.js';

export interface IDeleteCascadeResult {
  shapeDeleted: boolean;
  connectorsDeletedCount: number;
}

export class DeleteShapeCascadeUseCase {
  constructor(
    private readonly shapeRepository: ICanvasStateRepository,
    private readonly connectorRepository: IConnectorStateRepository
  ) {}

  async execute(shapeId: string): Promise<IDeleteCascadeResult> {
    // AC-2.4: Eliminación en cascada de todos los conectores vinculados para evitar referencias huérfanas
    const connectorsDeletedCount = await this.connectorRepository.deleteByShapeId(shapeId);
    const shapeDeleted = await this.shapeRepository.delete(shapeId);

    return {
      shapeDeleted,
      connectorsDeletedCount
    };
  }
}
