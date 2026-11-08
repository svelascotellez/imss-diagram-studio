import { ICanvasStateRepository } from '../../domain/repositories/canvas-state.repository.js';
import { ShapeEntity } from '../../domain/entities/shape.entity.js';

export class InMemoryCanvasStateRepository implements ICanvasStateRepository {
  private shapes: Map<string, ShapeEntity> = new Map();

  async save(shape: ShapeEntity): Promise<void> {
    this.shapes.set(shape.id, shape);
  }

  async saveMany(shapes: ShapeEntity[]): Promise<void> {
    for (const shape of shapes) {
      this.shapes.set(shape.id, shape);
    }
  }

  async findById(id: string): Promise<ShapeEntity | null> {
    return this.shapes.get(id) ?? null;
  }

  async findAll(): Promise<ShapeEntity[]> {
    return Array.from(this.shapes.values());
  }

  async findSelected(): Promise<ShapeEntity[]> {
    return Array.from(this.shapes.values()).filter(s => s.isSelected);
  }

  async delete(id: string): Promise<boolean> {
    return this.shapes.delete(id);
  }

  async clear(): Promise<void> {
    this.shapes.clear();
  }
}
