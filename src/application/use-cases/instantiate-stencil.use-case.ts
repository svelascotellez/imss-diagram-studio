import { IStencilCatalogRepository } from '../../domain/repositories/stencil-catalog.repository.js';
import { ICanvasStateRepository } from '../../domain/repositories/canvas-state.repository.js';
import { ShapeEntity, ShapeType } from '../../domain/entities/shape.entity.js';
import { Point } from '../../domain/value-objects/point.vo.js';
import { Dimensions } from '../../domain/value-objects/dimensions.vo.js';

export interface IInstantiateStencilDTO {
  stencilId: string;
  x: number;
  y: number;
  customLabel?: string;
}

export class InstantiateStencilUseCase {
  constructor(
    private readonly catalogRepository: IStencilCatalogRepository,
    private readonly canvasRepository: ICanvasStateRepository
  ) {}

  async execute(dto: IInstantiateStencilDTO): Promise<ShapeEntity> {
    const stencil = await this.catalogRepository.findById(dto.stencilId);

    // AC-3.4: Fallback seguro ante stencil desconocido o inexistente
    let shapeType: ShapeType = 'rectangle';
    let label = dto.customLabel ?? 'Servicio Institucional';
    let width = 140;
    let height = 65;

    if (stencil) {
      shapeType = stencil.baseShapeType;
      label = dto.customLabel ?? stencil.name;
      width = stencil.defaultWidth;
      height = stencil.defaultHeight;
    }

    const id = `shape_${Date.now()}_${Math.random().toString(36).substring(2, 9)}`;
    const position = new Point(dto.x, dto.y);
    const dimensions = new Dimensions(width, height);

    const shape = new ShapeEntity({
      id,
      type: shapeType,
      position,
      dimensions,
      label,
      style: {
        stroke: '#006341', // Verde IMSS Oficial
        fill: '#FFFFFF',
        strokeWidth: 2
      }
    });

    await this.canvasRepository.save(shape);
    return shape;
  }
}
