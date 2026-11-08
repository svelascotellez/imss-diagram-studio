import { StencilCategory, StencilCategoryType } from '../value-objects/stencil-category.vo.js';
import { ShapeType } from './shape.entity.js';

export interface IStencilProps {
  id: string;
  name: string;
  category: StencilCategory | StencilCategoryType;
  baseShapeType: ShapeType;
  defaultWidth: number;
  defaultHeight: number;
  iconSvg?: string;
  keywords?: string[];
  description?: string;
}

export class StencilEntity {
  readonly id: string;
  readonly name: string;
  readonly category: StencilCategory;
  readonly baseShapeType: ShapeType;
  readonly defaultWidth: number;
  readonly defaultHeight: number;
  readonly iconSvg: string;
  readonly keywords: ReadonlyArray<string>;
  readonly description: string;

  constructor(props: IStencilProps) {
    this.id = props.id;
    this.name = props.name;
    this.category = props.category instanceof StencilCategory
      ? props.category
      : new StencilCategory(props.category);
    this.baseShapeType = props.baseShapeType;
    this.defaultWidth = props.defaultWidth;
    this.defaultHeight = props.defaultHeight;
    this.iconSvg = props.iconSvg ?? '';
    this.keywords = Object.freeze([...(props.keywords ?? [])]);
    this.description = props.description ?? '';
    Object.freeze(this);
  }

  matchesQuery(term: string): boolean {
    if (!term || term.trim() === '') return true;
    const clean = term.toLowerCase().trim();
    if (this.name.toLowerCase().includes(clean)) return true;
    if (this.description.toLowerCase().includes(clean)) return true;
    if (this.category.displayName.toLowerCase().includes(clean)) return true;
    return this.keywords.some(kw => kw.toLowerCase().includes(clean));
  }
}
