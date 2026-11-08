export class Dimensions {
  readonly width: number;
  readonly height: number;

  public static readonly MIN_DIMENSION = 20;

  constructor(width: number, height: number) {
    if (!Number.isFinite(width) || !Number.isFinite(height)) {
      throw new Error('Dimensions must be finite numbers');
    }
    // AC-1.2: Acotamiento estricto al límite mínimo permitido (20x20 px)
    this.width = Math.max(Dimensions.MIN_DIMENSION, Math.round(width));
    this.height = Math.max(Dimensions.MIN_DIMENSION, Math.round(height));
    Object.freeze(this);
  }

  resize(width: number, height: number): Dimensions {
    return new Dimensions(width, height);
  }

  scale(factor: number): Dimensions {
    if (factor <= 0) return this;
    return new Dimensions(this.width * factor, this.height * factor);
  }

  equals(other: Dimensions): boolean {
    return this.width === other.width && this.height === other.height;
  }
}
