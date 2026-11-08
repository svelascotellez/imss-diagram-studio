import { IStencilCatalogRepository } from '../../domain/repositories/stencil-catalog.repository.js';
import { StencilCategoryType } from '../../domain/value-objects/stencil-category.vo.js';
import { SearchStencilsUseCase } from '../../application/use-cases/search-stencils.use-case.js';
import { StencilEntity } from '../../domain/entities/stencil.entity.js';

export interface ICategoryState {
  expanded: boolean;
  name: string;
}

export class StencilSidebar {
  private searchQuery: string = '';
  private categoryStates: Map<StencilCategoryType, ICategoryState> = new Map([
    ['architecture', { expanded: true, name: 'Arquitectura de Software' }],
    ['data_events', { expanded: true, name: 'Datos y Eventos' }],
    ['imss_processes', { expanded: true, name: 'Procesos y Actores IMSS' }]
  ]);
  private searchUseCase: SearchStencilsUseCase;

  constructor(private readonly catalogRepository: IStencilCatalogRepository) {
    this.searchUseCase = new SearchStencilsUseCase(this.catalogRepository);
  }

  setSearchQuery(query: string): void {
    this.searchQuery = query;
  }

  toggleCategory(category: StencilCategoryType): boolean {
    const current = this.categoryStates.get(category);
    if (!current) return false;
    current.expanded = !current.expanded;
    return current.expanded;
  }

  isCategoryExpanded(category: StencilCategoryType): boolean {
    return this.categoryStates.get(category)?.expanded ?? false;
  }

  async getFilteredStencils(): Promise<StencilEntity[]> {
    const result = await this.searchUseCase.execute({ query: this.searchQuery });
    return result.stencils;
  }

  async renderHtml(): Promise<string> {
    const allStencils = await this.getFilteredStencils();

    const categories: StencilCategoryType[] = ['architecture', 'data_events', 'imss_processes'];

    let categoriesHtml = '';

    for (const cat of categories) {
      const state = this.categoryStates.get(cat)!;
      const catStencils = allStencils.filter(s => s.category.type === cat);

      if (this.searchQuery && catStencils.length === 0) {
        continue;
      }

      const stencilsCards = catStencils.map(s => `
        <div class="stencil-item" role="button" tabindex="0" data-stencil-id="${s.id}"
             aria-label="${s.name}" title="${s.description}">
          <div class="stencil-icon">${this.renderStencilIcon(s)}</div>
          <span class="stencil-name">${s.name}</span>
        </div>
      `.trim()).join('\n        ');

      categoriesHtml += `
      <section class="stencil-category" role="region" aria-label="${state.name}">
        <button class="category-header" aria-expanded="${state.expanded ? 'true' : 'false'}"
                onclick="toggleCategory('${cat}')">
          <span class="cat-title">${state.name} (${catStencils.length})</span>
          <span class="cat-arrow">${state.expanded ? '▾' : '▸'}</span>
        </button>
        <div class="category-content ${state.expanded ? 'open' : 'collapsed'}"
             style="display: ${state.expanded ? 'grid' : 'none'};">
          ${stencilsCards || '<div class="empty-cat" role="status">Sin elementos</div>'}
        </div>
      </section>`.trim() + '\n';
    }

    if (allStencils.length === 0) {
      categoriesHtml = `
      <div class="empty-search" role="status">
        <p>No se encontraron stencils coincidentes con "<strong>${this.escapeHtml(this.searchQuery)}</strong>".</p>
      </div>`.trim();
    }

    return `
<aside class="stencil-sidebar" role="navigation" aria-label="Catálogo Oficial de Stencils DIDT IMSS">
  <div class="search-box">
    <input type="search" role="searchbox" aria-label="Buscar stencils IMSS"
           placeholder="Buscar microservicio, base de datos, actor..."
           value="${this.escapeHtml(this.searchQuery)}" />
  </div>
  <div class="categories-container" role="tree">
    ${categoriesHtml}
  </div>
</aside>`.trim();
  }

  private renderStencilIcon(stencil: StencilEntity): string {
    switch (stencil.baseShapeType) {
      case 'rectangle':
        return `<svg width="24" height="16"><rect width="22" height="14" rx="2" fill="#006341" stroke="#B38E5D" stroke-width="1.5"/></svg>`;
      case 'ellipse':
        return `<svg width="24" height="16"><ellipse cx="12" cy="8" rx="11" ry="7" fill="#006341" stroke="#B38E5D" stroke-width="1.5"/></svg>`;
      case 'diamond':
        return `<svg width="20" height="16"><polygon points="10,1 19,8 10,15 1,8" fill="#006341" stroke="#B38E5D" stroke-width="1.5"/></svg>`;
      default:
        return `<svg width="24" height="16"><rect width="22" height="14" rx="2" fill="#FFFFFF" stroke="#006341" stroke-width="1.5"/></svg>`;
    }
  }

  private escapeHtml(str: string): string {
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }
}
