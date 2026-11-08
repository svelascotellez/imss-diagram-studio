import { IStencilCatalogRepository } from '../../domain/repositories/stencil-catalog.repository.js';
import { StencilEntity } from '../../domain/entities/stencil.entity.js';
import { StencilCategoryType } from '../../domain/value-objects/stencil-category.vo.js';

export interface ISearchFilterDTO {
  query?: string;
  category?: StencilCategoryType;
}

export interface ISearchResult {
  stencils: StencilEntity[];
  totalCount: number;
  durationMs: number;
}

export class SearchStencilsUseCase {
  constructor(private readonly catalogRepository: IStencilCatalogRepository) {}

  async execute(filters: ISearchFilterDTO = {}): Promise<ISearchResult> {
    const startTime = performance.now();

    let results = filters.category
      ? await this.catalogRepository.findByCategory(filters.category)
      : await this.catalogRepository.findAll();

    if (filters.query && filters.query.trim() !== '') {
      const q = filters.query.trim();
      results = results.filter(s => s.matchesQuery(q));
    }

    const durationMs = performance.now() - startTime;

    return {
      stencils: results,
      totalCount: results.length,
      durationMs
    };
  }
}
