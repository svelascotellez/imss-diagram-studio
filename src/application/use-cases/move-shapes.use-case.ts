import { ICanvasStateRepository } from '../../domain/repositories/canvas-state.repository.js';
import { ShapeEntity } from '../../domain/entities/shape.entity.js';

export interface IMoveResult {
  movedCount: number;
  movedShapes: ShapeEntity[];
}

export class MoveShapesUseCase {
  constructor(private readonly repository: ICanvasStateRepository) {}

  async executeSelected(dx: number, dy: number): Promise<IMoveResult> {
    const selected = await this.repository.findSelected();
    
    // AC-1.4: Desplazamiento atómico en una única transacción de estado preservando distancias relativas
    for (const shape of selected) {
      shape.move(dx, dy);
    }

    await this.repository.saveMany(selected);

    return {
      movedCount: selected.length,
      movedShapes: selected
    };
  }

  async executeShapeById(id: string, dx: number, dy: number): Promise<ShapeEntity | null> {
    const shape = await this.repository.findById(id);
    if (!shape) return null;

    shape.move(dx, dy);
    await this.repository.save(shape);
    return shape;
  }
}
