import { describe, it, expect, beforeEach } from 'vitest';
import { InMemoryCanvasStateRepository } from '../../../src/infrastructure/repositories/in-memory-canvas-state.repository.js';
import { CreateShapeUseCase } from '../../../src/application/use-cases/create-shape.use-case.js';
import { SelectShapesUseCase } from '../../../src/application/use-cases/select-shapes.use-case.js';
import { MoveShapesUseCase } from '../../../src/application/use-cases/move-shapes.use-case.js';

describe('FEAT-001 Application Use Cases: Seleccion y Movimiento Atomico', () => {
  let repository: InMemoryCanvasStateRepository;
  let createUseCase: CreateShapeUseCase;
  let selectUseCase: SelectShapesUseCase;
  let moveUseCase: MoveShapesUseCase;

  beforeEach(() => {
    repository = new InMemoryCanvasStateRepository();
    createUseCase = new CreateShapeUseCase(repository);
    selectUseCase = new SelectShapesUseCase(repository);
    moveUseCase = new MoveShapesUseCase(repository);
  });

  describe('@AC-1.3: Seleccion multiple por area rectangular y feedback accesible', () => {
    it('debe seleccionar exactamente las formas intersecadas por el rectangulo de seleccion', async () => {
      // 3 formas distribuidas
      const s1 = await createUseCase.execute({ type: 'rectangle', x: 50, y: 50, width: 60, height: 40 });
      const s2 = await createUseCase.execute({ type: 'ellipse', x: 150, y: 70, width: 50, height: 50 });
      const s3 = await createUseCase.execute({ type: 'diamond', x: 500, y: 500, width: 80, height: 80 });

      // Seleccion que cubre s1 y s2 pero no s3
      const result = await selectUseCase.executeByBox({
        startX: 40,
        startY: 40,
        endX: 220,
        endY: 150
      });

      expect(result.selectedCount).toBe(2);
      expect(result.selectedIds).toContain(s1.id);
      expect(result.selectedIds).toContain(s2.id);
      expect(result.selectedIds).not.toContain(s3.id);

      // Debe calcular el bounding box unificado
      expect(result.unifiedBoundingBox).toEqual({
        x: 50,
        y: 50,
        width: 150, // de 50 a 150+50 = 200 -> ancho 150
        height: 70  // de 50 a 70+50 = 120 -> alto 70
      });
    });

    it('debe permitir seleccionar y deseleccionar formas por ID especifico', async () => {
      const s1 = await createUseCase.execute({ type: 'rectangle', x: 10, y: 10, width: 50, height: 50 });
      
      await selectUseCase.executeByIds([s1.id], false);
      const updatedS1 = await repository.findById(s1.id);
      expect(updatedS1?.isSelected).toBe(true);

      await selectUseCase.clearSelection();
      const clearedS1 = await repository.findById(s1.id);
      expect(clearedS1?.isSelected).toBe(false);
    });
  });

  describe('@AC-1.4: Desplazamiento sincronizado y atomico de nodos seleccionados', () => {
    it('debe desplazar atomicamente todas las formas seleccionadas preservando su distancia relativa', async () => {
      // 2 formas con distancia horizontal de 80 px (100 a 180)
      const s1 = await createUseCase.execute({ type: 'rectangle', x: 100, y: 100, width: 60, height: 40 });
      const s2 = await createUseCase.execute({ type: 'rectangle', x: 180, y: 100, width: 60, height: 40 });

      // Seleccionar ambas
      await selectUseCase.executeByIds([s1.id, s2.id], false);

      const initialDistance = s2.position.x - s1.position.x;
      expect(initialDistance).toBe(80);

      // Desplazar seleccion con vector (+50, +30)
      const moveResult = await moveUseCase.executeSelected(50, 30);

      expect(moveResult.movedCount).toBe(2);
      const movedS1 = await repository.findById(s1.id);
      const movedS2 = await repository.findById(s2.id);

      expect(movedS1?.position.x).toBe(150);
      expect(movedS1?.position.y).toBe(130);
      expect(movedS2?.position.x).toBe(230);
      expect(movedS2?.position.y).toBe(130);

      // La distancia relativa se mantiene inalterada
      const newDistance = movedS2!.position.x - movedS1!.position.x;
      expect(newDistance).toBe(80);
    });
  });
});
