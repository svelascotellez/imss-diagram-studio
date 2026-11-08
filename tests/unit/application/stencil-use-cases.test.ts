import { describe, it, expect, beforeEach } from 'vitest';
import { InMemoryCanvasStateRepository } from '../../../src/infrastructure/repositories/in-memory-canvas-state.repository.js';
import { InMemoryStencilCatalogRepository } from '../../../src/infrastructure/repositories/in-memory-stencil-catalog.repository.js';
import { SearchStencilsUseCase } from '../../../src/application/use-cases/search-stencils.use-case.js';
import { InstantiateStencilUseCase } from '../../../src/application/use-cases/instantiate-stencil.use-case.js';

describe('FEAT-003 Application Use Cases: Busqueda, Filtrado y Fallback Seguro', () => {
  let canvasRepo: InMemoryCanvasStateRepository;
  let catalogRepo: InMemoryStencilCatalogRepository;
  let searchUseCase: SearchStencilsUseCase;
  let instantiateUseCase: InstantiateStencilUseCase;

  beforeEach(() => {
    canvasRepo = new InMemoryCanvasStateRepository();
    catalogRepo = new InMemoryStencilCatalogRepository();
    searchUseCase = new SearchStencilsUseCase(catalogRepo);
    instantiateUseCase = new InstantiateStencilUseCase(catalogRepo, canvasRepo);
  });

  describe('@AC-3.2: Filtrado y busqueda reactiva de stencils', () => {
    it('debe filtrar stencils coincidentes con "Kafka" en menos de 50 ms', async () => {
      const result = await searchUseCase.execute({ query: 'Kafka' });
      expect(result.stencils.length).toBeGreaterThanOrEqual(1);
      expect(result.stencils.some(s => s.name.includes('Kafka'))).toBe(true);
      expect(result.durationMs).toBeLessThan(50);
    });

    it('debe filtrar stencils coincidentes con "PostgreSQL" en menos de 50 ms', async () => {
      const result = await searchUseCase.execute({ query: 'PostgreSQL' });
      expect(result.stencils.length).toBeGreaterThanOrEqual(1);
      expect(result.stencils.some(s => s.name.includes('PostgreSQL'))).toBe(true);
      expect(result.durationMs).toBeLessThan(50);
    });

    it('debe filtrar stencils de farmacia en menos de 50 ms', async () => {
      const result = await searchUseCase.execute({ query: 'Farmacia' });
      expect(result.stencils.length).toBeGreaterThanOrEqual(1);
      expect(result.stencils.some(s => s.name.includes('Farmacia'))).toBe(true);
      expect(result.durationMs).toBeLessThan(50);
    });

    it('debe filtrar por categoria especifica (data_events)', async () => {
      const result = await searchUseCase.execute({ category: 'data_events' });
      expect(result.stencils.length).toBe(3); // PostgreSQL, Kafka, Redis
      expect(result.stencils.every(s => s.category.type === 'data_events')).toBe(true);
    });
  });

  describe('@AC-3.4: Fallback seguro ante stencil desconocido', () => {
    it('debe crear un nodo fallback "Servicio Institucional" sin arrojar error cuando el id no existe', async () => {
      const shape = await instantiateUseCase.execute({
        stencilId: 'stencil-fantasma-999',
        x: 100,
        y: 100
      });

      expect(shape).toBeDefined();
      expect(shape.label).toBe('Servicio Institucional');
      expect(shape.type).toBe('rectangle');
      expect(shape.dimensions.width).toBe(140);
      expect(shape.dimensions.height).toBe(65);
      expect(shape.style.stroke).toBe('#006341'); // Verde IMSS

      const saved = await canvasRepo.findById(shape.id);
      expect(saved).not.toBeNull();
    });
  });
});
