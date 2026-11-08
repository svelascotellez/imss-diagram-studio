export type ExportFormat = 'drawio_xml' | 'svg' | 'json';

export interface IDiagramExportProps {
  format: ExportFormat;
  content: string;
  filename: string;
  mimeType: string;
  exportedAt?: Date;
  title?: string;
}

export class DiagramExportVO {
  readonly format: ExportFormat;
  readonly content: string;
  readonly filename: string;
  readonly mimeType: string;
  readonly exportedAt: Date;
  readonly title: string;

  constructor(props: IDiagramExportProps) {
    if (!props.content || props.content.trim().length === 0) {
      throw new Error('Export content cannot be empty');
    }
    if (!props.filename || props.filename.trim().length === 0) {
      throw new Error('Export filename cannot be empty');
    }

    this.format = props.format;
    this.content = props.content;
    this.filename = props.filename;
    this.mimeType = props.mimeType;
    this.exportedAt = props.exportedAt ?? new Date();
    this.title = props.title ?? 'Diagrama DIDT IMSS';
  }

  get byteLength(): number {
    return new TextEncoder().encode(this.content).length;
  }
}
