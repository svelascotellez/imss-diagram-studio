export type StencilCategoryType = 'architecture' | 'data_events' | 'imss_processes';

export class StencilCategory {
  readonly type: StencilCategoryType;
  readonly displayName: string;

  private static readonly CATEGORY_MAP: Record<StencilCategoryType, string> = {
    architecture: 'Arquitectura de Software',
    data_events: 'Datos y Eventos',
    imss_processes: 'Procesos y Actores IMSS'
  };

  constructor(type: StencilCategoryType) {
    if (!StencilCategory.CATEGORY_MAP[type]) {
      throw new Error(`Invalid stencil category type: ${type}`);
    }
    this.type = type;
    this.displayName = StencilCategory.CATEGORY_MAP[type];
    Object.freeze(this);
  }

  equals(other: StencilCategory): boolean {
    return this.type === other.type;
  }
}
