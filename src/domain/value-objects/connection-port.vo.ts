import { Point } from './point.vo.js';
import { IBoundingBox } from '../entities/shape.entity.js';

export type PortPosition = 'north' | 'south' | 'east' | 'west';

export class ConnectionPort {
  readonly position: PortPosition;

  constructor(position: PortPosition) {
    if (!['north', 'south', 'east', 'west'].includes(position)) {
      throw new Error(`Invalid port position: ${position}`);
    }
    this.position = position;
    Object.freeze(this);
  }

  computeAbsolutePoint(boundingBox: IBoundingBox): Point {
    const { x, y, width, height } = boundingBox;
    switch (this.position) {
      case 'north':
        return new Point(x + width / 2, y);
      case 'south':
        return new Point(x + width / 2, y + height);
      case 'east':
        return new Point(x + width, y + height / 2);
      case 'west':
        return new Point(x, y + height / 2);
    }
  }

  equals(other: ConnectionPort): boolean {
    return this.position === other.position;
  }
}
