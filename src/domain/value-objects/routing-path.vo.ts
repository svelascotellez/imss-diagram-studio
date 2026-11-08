import { Point } from './point.vo.js';

export class RoutingPath {
  readonly waypoints: ReadonlyArray<Point>;

  constructor(waypoints: Point[]) {
    if (waypoints.length < 2) {
      throw new Error('RoutingPath must contain at least 2 waypoints');
    }
    this.waypoints = Object.freeze([...waypoints]);
    Object.freeze(this);
  }

  toSvgPathData(): string {
    return this.waypoints.reduce((acc, pt, idx) => {
      return idx === 0 ? `M ${pt.x} ${pt.y}` : `${acc} L ${pt.x} ${pt.y}`;
    }, '');
  }

  isOrthogonal(): boolean {
    for (let i = 0; i < this.waypoints.length - 1; i++) {
      const p1 = this.waypoints[i];
      const p2 = this.waypoints[i + 1];
      // Cada segmento debe ser perfectamente horizontal o vertical
      const isHorizontal = Math.abs(p1.y - p2.y) < 0.001;
      const isVertical = Math.abs(p1.x - p2.x) < 0.001;
      if (!isHorizontal && !isVertical) {
        return false;
      }
    }
    return true;
  }
}
