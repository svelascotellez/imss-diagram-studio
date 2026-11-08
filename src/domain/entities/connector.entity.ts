import { PortPosition } from '../value-objects/connection-port.vo.js';

export interface IConnectorProps {
  id: string;
  sourceShapeId: string;
  sourcePort: PortPosition;
  targetShapeId: string;
  targetPort: PortPosition;
  routingType?: 'orthogonal' | 'straight' | 'curved';
  stroke?: string;
  strokeWidth?: number;
  hasEndArrow?: boolean;
  label?: string;
}

export class ConnectorEntity {
  readonly id: string;
  readonly sourceShapeId: string;
  readonly sourcePort: PortPosition;
  readonly targetShapeId: string;
  readonly targetPort: PortPosition;
  readonly routingType: 'orthogonal' | 'straight' | 'curved';
  private _stroke: string;
  private _strokeWidth: number;
  private _hasEndArrow: boolean;
  private _label: string;

  public static readonly DEFAULT_STROKE = '#475569';
  public static readonly ACTIVE_STROKE = '#006341'; // Verde IMSS

  constructor(props: IConnectorProps) {
    if (props.sourceShapeId === props.targetShapeId) {
      throw new Error('Self-connections (auto-bucles) are not allowed');
    }

    this.id = props.id;
    this.sourceShapeId = props.sourceShapeId;
    this.sourcePort = props.sourcePort;
    this.targetShapeId = props.targetShapeId;
    this.targetPort = props.targetPort;
    this.routingType = props.routingType ?? 'orthogonal';
    this._stroke = props.stroke ?? ConnectorEntity.DEFAULT_STROKE;
    this._strokeWidth = props.strokeWidth ?? 2;
    this._hasEndArrow = props.hasEndArrow ?? true;
    this._label = props.label ?? '';
  }

  get stroke(): string {
    return this._stroke;
  }

  get strokeWidth(): number {
    return this._strokeWidth;
  }

  get hasEndArrow(): boolean {
    return this._hasEndArrow;
  }

  get label(): string {
    return this._label;
  }

  setStroke(stroke: string): void {
    this._stroke = stroke;
  }

  setLabel(label: string): void {
    this._label = label;
  }

  involvesShape(shapeId: string): boolean {
    return this.sourceShapeId === shapeId || this.targetShapeId === shapeId;
  }
}
