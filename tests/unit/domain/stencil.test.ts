import { describe, it, expect } from 'vitest';
import { StencilEntity } from '../../../src/domain/entities/stencil.entity.js';
import { StencilCategory } from '../../../src/domain/value-objects/stencil-category.vo.js';

describe('FEAT-003 Unit Tests: StencilEntity y StencilCategory', () => {
  describe('StencilCategory Value Object', () => {
    it('debe crear categorías válidas y mapear el nombre legible institucional', () => {
      const arch = new StencilCategory('architecture');
      expect(arch.type).toBe('architecture');
      expect(arch.displayName).toBe('Arquitectura de Software');

      const data = new StencilCategory('data_events');
      expect(data.displayName).toBe('Datos y Eventos');

      const proc = new StencilCategory('imss_processes');
      expect(proc.displayName).toBe('Procesos y Actores IMSS');
    });

    it('debe arrojar error ante tipo de categoría desconocido', () => {
      expect(() => {
        new StencilCategory('invalid-cat' as any);
      }).toThrowError(/Invalid stencil category type/);
    });
  });

  describe('StencilEntity', () => {
    it('debe evaluar coincidencia de consulta por nombre, descripción o palabras clave', () => {
      const stencil = new StencilEntity({
        id: 's-kafka',
        name: 'Bus de Eventos Kafka',
        category: 'data_events',
        baseShapeType: 'rectangle',
        defaultWidth: 160,
        defaultHeight: 65,
        keywords: ['queue', 'mensajeria', 'streaming'],
        description: 'Plataforma distribuida de mensajeria'
      });

      expect(stencil.matchesQuery('kafka')).toBe(true);
      expect(stencil.matchesQuery('streaming')).toBe(true);
      expect(stencil.matchesQuery('mensajeria')).toBe(true);
      expect(stencil.matchesQuery('Datos y Eventos')).toBe(true);
      expect(stencil.matchesQuery('Oracle')).toBe(false);
    });

    it('la entidad StencilEntity debe ser inmutable', () => {
      const stencil = new StencilEntity({
        id: 's-1',
        name: 'Test',
        category: 'architecture',
        baseShapeType: 'rectangle',
        defaultWidth: 100,
        defaultHeight: 50
      });

      expect(Object.isFrozen(stencil)).toBe(true);
    });
  });
});
