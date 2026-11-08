import { ICanvasStateRepository } from '../../domain/repositories/canvas-state.repository.js';
import { IBoundingBox } from '../../domain/entities/shape.entity.js';

export interface ISelectionBoxInput {
  startX: number;
  startY: number;
  endX: number;
  endY: number;
}

export interface ISelectionResult {
  selectedCount: number;
  selectedIds: string[];
  unifiedBoundingBox: IBoundingBox | null;
}

export class SelectShapesUseCase {
  constructor(private readonly repository: ICanvasStateRepository) {}

  async executeByBox(box: ISelectionBoxInput): Promise<ISelectionResult> {
    const allShapes = await this.repository.findAll();
    const selectedIds: string[] = [];

    let minX = Infinity;
    let minY = Infinity;
    let maxX = -Infinity;
    let maxY = -Infinity;

    for (const shape of allShapes) {
      const isInteracting = shape.intersectsBox(box);
      shape.setSelected(isInteracting);
      await this.repository.save(shape);

      if (isInteracting) {
        selectedIds.push(shape.id);
        const bb = shape.boundingBox;
        minX = Math.min(minX, bb.x);
        minY = Math.min(minY, bb.y);
        maxX = Math.max(maxX, bb.x + bb.width);
        maxY = Math.max(maxY, bb.y + bb.height);
      }
    }

    const unifiedBoundingBox: IBoundingBox | null =
      selectedIds.length > 0
        ? {
            x: minX,
            y: minY,
            width: maxX - minX,
            height: maxY - minY
          }
        : null;

    return {
      selectedCount: selectedIds.length,
      selectedIds,
      unifiedBoundingBox
    };
  }

  async executeByIds(ids: string[], toggle: boolean = false): Promise<ISelectionResult> {
    const allShapes = await this.repository.findAll();
    const idSet = new Set(ids);
    const selectedIds: string[] = [];

    let minX = Infinity;
    let minY = Infinity;
    let maxX = -Infinity;
    let maxY = -Infinity;

    for (const shape of allShapes) {
      if (idSet.has(shape.id)) {
        shape.setSelected(toggle ? !shape.isSelected : true);
      } else if (!toggle) {
        shape.setSelected(false);
      }

      await this.repository.save(shape);

      if (shape.isSelected) {
        selectedIds.push(shape.id);
        const bb = shape.boundingBox;
        minX = Math.min(minX, bb.x);
        minY = Math.min(minY, bb.y);
        maxX = Math.max(maxX, bb.x + bb.width);
        maxY = Math.max(maxY, bb.y + bb.height);
      }
    }

    const unifiedBoundingBox: IBoundingBox | null =
      selectedIds.length > 0
        ? {
            x: minX,
            y: minY,
            width: maxX - minX,
            height: maxY - minY
          }
        : null;

    return {
      selectedCount: selectedIds.length,
      selectedIds,
      unifiedBoundingBox
    };
  }

  async clearSelection(): Promise<void> {
    const allShapes = await this.repository.findAll();
    for (const shape of allShapes) {
      if (shape.isSelected) {
        shape.setSelected(false);
        await this.repository.save(shape);
      }
    }
  }
}
