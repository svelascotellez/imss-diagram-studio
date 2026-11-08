import { ICanvasStateRepository } from '../../domain/repositories/canvas-state.repository.js';
import { IConnectorStateRepository } from '../../domain/repositories/connector-state.repository.js';
import { DrawioSerializerService } from '../../domain/services/drawio-serializer.service.js';
import { DiagramExportVO } from '../../domain/value-objects/diagram-export.vo.js';

export interface IExportDrawioXmlRequest {
  title?: string;
}

export class ExportDrawioXmlUseCase {
  private readonly serializer: DrawioSerializerService;

  constructor(
    private readonly canvasRepo: ICanvasStateRepository,
    private readonly connectorRepo: IConnectorStateRepository
  ) {
    this.serializer = new DrawioSerializerService();
  }

  async execute(request?: IExportDrawioXmlRequest): Promise<DiagramExportVO> {
    const title = request?.title || 'Diagrama Arquitectura DIDT IMSS';
    const shapes = await this.canvasRepo.findAll();
    const connectors = await this.connectorRepo.findAll();

    const xmlContent = this.serializer.serialize(shapes, connectors);
    const sanitizedFilename = title
      .toLowerCase()
      .replace(/[^a-z0-9_-]/g, '_')
      .replace(/_+/g, '_');

    return new DiagramExportVO({
      format: 'drawio_xml',
      content: xmlContent,
      filename: `${sanitizedFilename}.drawio.xml`,
      mimeType: 'application/xml',
      title
    });
  }
}
