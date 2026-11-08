import { describe, it, expect } from 'vitest';
import { ShapeEntity } from '../../../src/domain/entities/shape.entity.js';
import { Dimensions } from '../../../src/domain/value-objects/dimensions.vo.js';
import { Point } from '../../../src/domain/value-objects/point.vo.js';

describe('FEAT-001 Unit Tests: ShapeEntity y Value Objects', () => {
  describe('@AC-1.2: Validacion de dimensiones minimas y limites validos de coordenadas', () => {
    it('debe acotar dimensiones menores a 20x20 al limite minimo permitido (5x10 -> 20x20)', () => {
      const dim = new Dimensions(5, 10);
      expect(dim.width).toBe(20);
      expect(dim.height).toBe(20);
    });

    it('debe acotar valores cero y negativos al umbral minimo de 20 (0x-15 -> 20x20)', () => {
      const dim = new Dimensions(0, -15);
      expect(dim.width).toBe(20);
      expect(dim.height).toBe(20);
    });

    it('debe mantener anchos mayores a 20 y acotar unicamente la dimension menor a 20 (50x15 -> 50x20)', () => {
      const dim = new Dimensions(50, 15);
      expect(dim.width).toBe(50);
      expect(dim.height).toBe(20);
    });

    it('al redimensionar una forma existente, debe aplicar el acotamiento a 20x20 sin arrojar error', () => {
      const shape = new ShapeEntity({
        id: 'shape-1',
        type: 'rectangle',
        position: new Point(50, 50),
        dimensions: new Dimensions(100, 100)
      });

      shape.resize(10, 8);
      expect(shape.dimensions.width).toBe(20);
      expect(shape.dimensions.height).toBe(20);
    });

    it('las coordenadas de Point deben acotarse a valores no negativos', () => {
      const p = new Point(-30, -50);
      expect(p.x).toBe(0);
      expect(p.y).toBe(0);
    });
  });

  describe('Invariantes y Funcionalidad del Dominio', () => {
    it('debe permitir mover la forma mediante traslacion delta', () => {
      const shape = new ShapeEntity({
        id: 'shape-move',
        type: 'ellipse',
        position: new Point(10, 20),
        dimensions: new Dimensions(60, 40)
      });

      shape.move(15, 25);
      expect(shape.position.x).toBe(25);
      expect(shape.position.y).toBe(45);
    });

    it('debe alternar estado de seleccion correctamente', () => {
      const shape = new ShapeEntity({
        id: 'shape-sel',
        type: 'diamond',
        position: new Point(0, 0),
        dimensions: new Dimensions(40, 40)
      });

      expect(shape.isSelected).toBe(false);
      shape.setSelected(true);
      expect(shape.isSelected).toBe(true);
    });
  });
});
