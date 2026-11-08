import { ShapeEntity, ShapeType } from '../../domain/entities/shape.entity.js';
import { Point } from '../../domain/value-objects/point.vo.js';
import { Dimensions } from '../../domain/value-objects/dimensions.vo.js';
import { ICanvasStateRepository } from '../../domain/repositories/canvas-state.repository.js';

export interface ICreateShapeDTO {
  id?: string;
  type: ShapeType;
  x: number;
  y: number;
  width: number;
  height: number;
  label?: string;
}

export class CreateShapeUseCase {
  constructor(private readonly repository: ICanvasStateRepository) {}

  async execute(dto: ICreateShapeDTO): Promise<ShapeEntity> {
    const id = dto.id ?? `shape_${Date.now()}_${Math.random().toString(36).substring(2, 9)}`;
    const position = new Point(dto.x, dto.y);
    const dimensions = new Dimensions(dto.width, dto.height);

    const shape = new ShapeEntity({
      id,
      type: dto.type,
      position,
      dimensions,
      label: dto.label
    });

    await this.repository.save(shape);
    return shape;
  }
}
