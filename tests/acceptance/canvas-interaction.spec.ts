import { describe, it, expect } from 'vitest';
import { CreateShapeUseCase } from '../../src/application/use-cases/create-shape.use-case.js';
import { InMemoryCanvasStateRepository } from '../../src/infrastructure/repositories/in-memory-canvas-state.repository.js';

describe('FEAT-001 Acceptance Tests: Canvas Interactivo y Motor de Renderizado', () => {
  it('@AC-1.1: Creacion y renderizado exitoso de una forma geometrica institucional', async () => {
    // Dado un canvas institucional inicializado en estado vacio
    const repository = new InMemoryCanvasStateRepository();
    const useCase = new CreateShapeUseCase(repository);

    // Cuando el usuario solicita crear una forma de tipo "rectangle" en (100, 150) con 160x80
    const shape = await useCase.execute({
      type: 'rectangle',
      x: 100,
      y: 150,
      width: 160,
      height: 80,
      label: 'Servicio DIDT'
    });

    // Entonces la entidad es instanciada en el modelo de dominio
    expect(shape).toBeDefined();
    expect(shape.id).toBeDefined();
    expect(shape.type).toBe('rectangle');
    expect(shape.position.x).toBe(100);
    expect(shape.position.y).toBe(150);
    expect(shape.dimensions.width).toBe(160);
    expect(shape.dimensions.height).toBe(80);

    // Y el nodo se renderiza con el color primario IMSS "#006341", borde institucional y manejadores de transformacion activos
    expect(shape.style.stroke).toBe('#006341');
    expect(shape.style.fill).toBe('#FFFFFF');
    expect(shape.boundingBox).toEqual({
      x: 100,
      y: 150,
      width: 160,
      height: 80
    });
  });
});
