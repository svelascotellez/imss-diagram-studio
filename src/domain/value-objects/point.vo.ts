export class Point {
  readonly x: number;
  readonly y: number;

  constructor(x: number, y: number) {
    if (!Number.isFinite(x) || !Number.isFinite(y)) {
      throw new Error('Coordinates must be finite numbers');
    }
    this.x = Math.max(0, x);
    this.y = Math.max(0, y);
    Object.freeze(this);
  }

  translate(dx: number, dy: number): Point {
    return new Point(this.x + dx, this.y + dy);
  }

  distanceTo(other: Point): number {
    return Math.hypot(this.x - other.x, this.y - other.y);
  }

  equals(other: Point): boolean {
    return this.x === other.x && this.y === other.y;
  }
}
