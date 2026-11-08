import { describe, it, expect } from 'vitest';
import { ConnectorEntity } from '../../../src/domain/entities/connector.entity.js';
import { ConnectionPort } from '../../../src/domain/value-objects/connection-port.vo.js';
import { RoutingPath } from '../../../src/domain/value-objects/routing-path.vo.js';
import { Point } from '../../../src/domain/value-objects/point.vo.js';
import { IBoundingBox } from '../../../src/domain/entities/shape.entity.js';

describe('FEAT-002 Unit Tests: Conectores y Value Objects', () => {
  describe('@AC-2.2: Bloqueo de auto-bucles y puertos invalidos', () => {
    it('debe arrojar error si se intenta instanciar un conector con la misma forma como origen y destino (auto-bucle)', () => {
      expect(() => {
        new ConnectorEntity({
          id: 'conn-self',
          sourceShapeId: 'shape-1',
          sourcePort: 'north',
          targetShapeId: 'shape-1', // Auto-bucle prohibido
          targetPort: 'south'
        });
      }).toThrowError(/Self-connections \(auto-bucles\) are not allowed/);
    });

    it('ConnectionPort debe arrojar error si la posicion no es valida', () => {
      expect(() => {
        new ConnectionPort('invalid-pos' as any);
      }).toThrowError(/Invalid port position/);
    });

    it('ConnectionPort debe calcular correctamente los puntos cardinales absolutos', () => {
      const box: IBoundingBox = { x: 100, y: 100, width: 200, height: 80 };

      const north = new ConnectionPort('north').computeAbsolutePoint(box);
      expect(north.x).toBe(200); // 100 + 100
      expect(north.y).toBe(100);

      const south = new ConnectionPort('south').computeAbsolutePoint(box);
      expect(south.x).toBe(200);
      expect(south.y).toBe(180); // 100 + 80

      const east = new ConnectionPort('east').computeAbsolutePoint(box);
      expect(east.x).toBe(300); // 100 + 200
      expect(east.y).toBe(140); // 100 + 40

      const west = new ConnectionPort('west').computeAbsolutePoint(box);
      expect(west.x).toBe(100);
      expect(west.y).toBe(140);
    });
  });

  describe('RoutingPath e Invariantes Ortogonales', () => {
    it('debe validar que una secuencia de waypoints con angulos rectos es ortogonal', () => {
      const p1 = new Point(100, 100);
      const p2 = new Point(200, 100); // horizontal
      const p3 = new Point(200, 300); // vertical
      const p4 = new Point(400, 300); // horizontal

      const path = new RoutingPath([p1, p2, p3, p4]);
      expect(path.isOrthogonal()).toBe(true);
      expect(path.toSvgPathData()).toBe('M 100 100 L 200 100 L 200 300 L 400 300');
    });

    it('debe rechazar como no ortogonal un trazado con segmentos diagonales arbitrarios', () => {
      const p1 = new Point(100, 100);
      const p2 = new Point(250, 180); // diagonal no ortogonal

      const path = new RoutingPath([p1, p2]);
      expect(path.isOrthogonal()).toBe(false);
    });
  });
});
