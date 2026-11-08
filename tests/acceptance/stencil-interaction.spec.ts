import { describe, it, expect, beforeEach } from 'vitest';
import { InMemoryCanvasStateRepository } from '../../src/infrastructure/repositories/in-memory-canvas-state.repository.js';
import { InMemoryStencilCatalogRepository } from '../../src/infrastructure/repositories/in-memory-stencil-catalog.repository.js';
import { InstantiateStencilUseCase } from '../../src/application/use-cases/instantiate-stencil.use-case.js';

describe('FEAT-003 Acceptance Tests: Catalogo de Stencils DIDT e IMSS', () => {
  let canvasRepo: InMemoryCanvasStateRepository;
  let catalogRepo: InMemoryStencilCatalogRepository;
  let instantiateUseCase: InstantiateStencilUseCase;

  beforeEach(() => {
    canvasRepo = new InMemoryCanvasStateRepository();
    catalogRepo = new InMemoryStencilCatalogRepository();
    instantiateUseCase = new InstantiateStencilUseCase(catalogRepo, canvasRepo);
  });

  it('@AC-3.1: Instanciacion exitosa de un stencil arquitectonico hacia el canvas', async () => {
    // Dado un catalogo inicializado con la coleccion oficial de stencils de la DIDT
    const stencil = await catalogRepo.findById('stencil-api-gateway');
    expect(stencil).not.toBeNull();
    expect(stencil?.name).toBe('API Gateway DIDT');

    // Cuando el usuario solicita instanciar el stencil con id "stencil-api-gateway" en (200, 150)
    const shape = await instantiateUseCase.execute({
      stencilId: 'stencil-api-gateway',
      x: 200,
      y: 150
    });

    // Entonces se crea una entidad de forma en el canvas con tipo "rectangle" y etiqueta "API Gateway DIDT"
    expect(shape).toBeDefined();
    expect(shape.type).toBe('rectangle');
    expect(shape.label).toBe('API Gateway DIDT');
    expect(shape.position.x).toBe(200);
    expect(shape.position.y).toBe(150);

    // Y la forma incorpora dimensiones optimas 160x70 px y estilo institucional IMSS
    expect(shape.dimensions.width).toBe(160);
    expect(shape.dimensions.height).toBe(70);
    expect(shape.style.stroke).toBe('#006341'); // Verde IMSS

    // Y queda persistida en el repositorio del canvas
    const saved = await canvasRepo.findById(shape.id);
    expect(saved).not.toBeNull();
  });
});
