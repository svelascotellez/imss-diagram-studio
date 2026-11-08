import { StencilEntity } from '../entities/stencil.entity.js';
import { StencilCategoryType } from '../value-objects/stencil-category.vo.js';

export interface IStencilCatalogRepository {
  findById(id: string): Promise<StencilEntity | null>;
  findAll(): Promise<StencilEntity[]>;
  findByCategory(category: StencilCategoryType): Promise<StencilEntity[]>;
  search(term: string): Promise<StencilEntity[]>;
}
