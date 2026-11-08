import { IStencilCatalogRepository } from '../../domain/repositories/stencil-catalog.repository.js';
import { StencilEntity } from '../../domain/entities/stencil.entity.js';
import { StencilCategoryType } from '../../domain/value-objects/stencil-category.vo.js';

export class InMemoryStencilCatalogRepository implements IStencilCatalogRepository {
  private stencils: Map<string, StencilEntity> = new Map();

  constructor() {
    this.initializeDefaultCatalog();
  }

  private initializeDefaultCatalog(): void {
    const defaultStencils: StencilEntity[] = [
      // Categoría: Arquitectura de Software
      new StencilEntity({
        id: 'stencil-api-gateway',
        name: 'API Gateway DIDT',
        category: 'architecture',
        baseShapeType: 'rectangle',
        defaultWidth: 160,
        defaultHeight: 70,
        keywords: ['gateway', 'api', 'proxy', 'reverse proxy', 'didt', 'inbound'],
        description: 'Punto de entrada unificado y enrutamiento perimetral para servicios DIDT IMSS.'
      }),
      new StencilEntity({
        id: 'stencil-microservice',
        name: 'Microservicio IMSS',
        category: 'architecture',
        baseShapeType: 'rectangle',
        defaultWidth: 150,
        defaultHeight: 65,
        keywords: ['microservicio', 'service', 'backend', 'api rest', 'dominio'],
        description: 'Servicio desacoplado bajo Clean Architecture para trámites del Seguro Social.'
      }),
      new StencilEntity({
        id: 'stencil-auth-oauth2',
        name: 'Servicio Auth / OAuth2',
        category: 'architecture',
        baseShapeType: 'rectangle',
        defaultWidth: 160,
        defaultHeight: 65,
        keywords: ['auth', 'seguridad', 'jwt', 'oauth2', 'credenciales', 'sso'],
        description: 'Módulo centralizado de autenticación y federación de identidad institucional.'
      }),

      // Categoría: Datos y Eventos
      new StencilEntity({
        id: 'stencil-db-postgres',
        name: 'Base de Datos PostgreSQL',
        category: 'data_events',
        baseShapeType: 'rectangle',
        defaultWidth: 150,
        defaultHeight: 70,
        keywords: ['database', 'db', 'sql', 'postgresql', 'postgres', 'persistencia'],
        description: 'Base de datos relacional para expedientes clínicos y registros del IMSS.'
      }),
      new StencilEntity({
        id: 'stencil-kafka',
        name: 'Bus de Eventos Kafka',
        category: 'data_events',
        baseShapeType: 'rectangle',
        defaultWidth: 160,
        defaultHeight: 65,
        keywords: ['kafka', 'event', 'bus', 'mensajeria', 'queue', 'stream'],
        description: 'Transmisión distribuida de eventos en tiempo real para recetas y alertas.'
      }),
      new StencilEntity({
        id: 'stencil-redis',
        name: 'Memoria Caché Redis',
        category: 'data_events',
        baseShapeType: 'rectangle',
        defaultWidth: 140,
        defaultHeight: 60,
        keywords: ['redis', 'cache', 'en memoria', 'sesiones', 'fast'],
        description: 'Capa de almacenamiento en memoria para sesiones activas y catálogos.'
      }),

      // Categoría: Procesos y Actores IMSS
      new StencilEntity({
        id: 'stencil-actor-medico',
        name: 'Médico Familiar IMSS',
        category: 'imss_processes',
        baseShapeType: 'ellipse',
        defaultWidth: 140,
        defaultHeight: 70,
        keywords: ['medico', 'doctor', 'consulta', 'medicina familiar', 'receta'],
        description: 'Actor clínico facultado para emitir recetas y diagnósticos médicos.'
      }),
      new StencilEntity({
        id: 'stencil-actor-derechohabiente',
        name: 'Paciente / Derechohabiente',
        category: 'imss_processes',
        baseShapeType: 'ellipse',
        defaultWidth: 150,
        defaultHeight: 70,
        keywords: ['paciente', 'derechohabiente', 'usuario', 'afiliado', 'ciudadano'],
        description: 'Beneficiario y receptor de atención médica en unidades de medicina familiar.'
      }),
      new StencilEntity({
        id: 'stencil-actor-farmacia',
        name: 'Despachador de Farmacia',
        category: 'imss_processes',
        baseShapeType: 'rectangle',
        defaultWidth: 160,
        defaultHeight: 65,
        keywords: ['farmacia', 'despacho', 'surtido', 'medicamentos', 'almacen'],
        description: 'Operador de farmacia hospitalaria encargado de la validación y surtido.'
      }),
      new StencilEntity({
        id: 'stencil-actor-oic',
        name: 'Auditor OIC IMSS',
        category: 'imss_processes',
        baseShapeType: 'diamond',
        defaultWidth: 130,
        defaultHeight: 70,
        keywords: ['auditor', 'oic', 'control interno', 'compliance', 'supervision'],
        description: 'Órgano Interno de Control para auditoría de cumplimiento regulatorio.'
      })
    ];

    for (const s of defaultStencils) {
      this.stencils.set(s.id, s);
    }
  }

  async findById(id: string): Promise<StencilEntity | null> {
    return this.stencils.get(id) ?? null;
  }

  async findAll(): Promise<StencilEntity[]> {
    return Array.from(this.stencils.values());
  }

  async findByCategory(category: StencilCategoryType): Promise<StencilEntity[]> {
    return Array.from(this.stencils.values()).filter(s => s.category.type === category);
  }

  async search(term: string): Promise<StencilEntity[]> {
    return Array.from(this.stencils.values()).filter(s => s.matchesQuery(term));
  }
}
