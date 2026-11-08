import { ShapeEntity } from '../entities/shape.entity.js';

export interface ICanvasStateRepository {
  save(shape: ShapeEntity): Promise<void>;
  saveMany(shapes: ShapeEntity[]): Promise<void>;
  findById(id: string): Promise<ShapeEntity | null>;
  findAll(): Promise<ShapeEntity[]>;
  findSelected(): Promise<ShapeEntity[]>;
  delete(id: string): Promise<boolean>;
  clear(): Promise<void>;
}
