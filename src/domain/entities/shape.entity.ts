import { Point } from '../value-objects/point.vo.js';
import { Dimensions } from '../value-objects/dimensions.vo.js';

export type ShapeType = 'rectangle' | 'ellipse' | 'diamond' | 'container' | 'text';

export interface IShapeStyle {
  readonly stroke: string;
  readonly fill: string;
  readonly strokeWidth: number;
}

export interface IBoundingBox {
  readonly x: number;
  readonly y: number;
  readonly width: number;
  readonly height: number;
}

export interface IShapeProps {
  id: string;
  type: ShapeType;
  position: Point;
  dimensions: Dimensions;
  zIndex?: number;
  isSelected?: boolean;
  style?: Partial<IShapeStyle>;
  label?: string;
}

export class ShapeEntity {
  readonly id: string;
  readonly type: ShapeType;
  private _position: Point;
  private _dimensions: Dimensions;
  private _zIndex: number;
  private _isSelected: boolean;
  private _style: IShapeStyle;
  private _label: string;

  public static readonly DEFAULT_IMSS_STYLE: IShapeStyle = {
    stroke: '#006341', // Verde IMSS Oficial
    fill: '#FFFFFF',
    strokeWidth: 2
  };

  constructor(props: IShapeProps) {
    this.id = props.id;
    this.type = props.type;
    this._position = props.position;
    this._dimensions = props.dimensions;
    this._zIndex = props.zIndex ?? 1;
    this._isSelected = props.isSelected ?? false;
    this._label = props.label ?? '';
    this._style = {
      ...ShapeEntity.DEFAULT_IMSS_STYLE,
      ...props.style
    };
  }

  get position(): Point {
    return this._position;
  }

  get dimensions(): Dimensions {
    return this._dimensions;
  }

  get zIndex(): number {
    return this._zIndex;
  }

  get isSelected(): boolean {
    return this._isSelected;
  }

  get style(): IShapeStyle {
    return { ...this._style };
  }

  get label(): string {
    return this._label;
  }

  get boundingBox(): IBoundingBox {
    return {
      x: this._position.x,
      y: this._position.y,
      width: this._dimensions.width,
      height: this._dimensions.height
    };
  }

  move(dx: number, dy: number): void {
    this._position = this._position.translate(dx, dy);
  }

  moveTo(x: number, y: number): void {
    this._position = new Point(x, y);
  }

  resize(newWidth: number, newHeight: number): void {
    this._dimensions = this._dimensions.resize(newWidth, newHeight);
  }

  setSelected(selected: boolean): void {
    this._isSelected = selected;
  }

  setLabel(newLabel: string): void {
    this._label = newLabel;
  }

  setZIndex(index: number): void {
    this._zIndex = Math.max(0, index);
  }

  intersectsBox(box: { startX: number; startY: number; endX: number; endY: number }): boolean {
    const minX = Math.min(box.startX, box.endX);
    const maxX = Math.max(box.startX, box.endX);
    const minY = Math.min(box.startY, box.endY);
    const maxY = Math.max(box.startY, box.endY);

    const shapeMaxX = this._position.x + this._dimensions.width;
    const shapeMaxY = this._position.y + this._dimensions.height;

    return !(
      this._position.x > maxX ||
      shapeMaxX < minX ||
      this._position.y > maxY ||
      shapeMaxY < minY
    );
  }
}
