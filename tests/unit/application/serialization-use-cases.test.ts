import { describe, it, expect, beforeEach } from 'vitest';
import { InMemoryCanvasStateRepository } from '../../../src/infrastructure/repositories/in-memory-canvas-state.repository.js';
import { InMemoryConnectorStateRepository } from '../../../src/infrastructure/repositories/in-memory-connector-state.repository.js';
import { ExportDrawioXmlUseCase } from '../../../src/application/use-cases/export-drawio-xml.use-case.js';
import { ImportDrawioXmlUseCase } from '../../../src/application/use-cases/import-drawio-xml.use-case.js';
import { ExportSvgDiagramUseCase } from '../../../src/application/use-cases/export-svg-diagram.use-case.js';
import { ShapeEntity } from '../../../src/domain/entities/shape.entity.js';
import { Point } from '../../../src/domain/value-objects/point.vo.js';
import { Dimensions } from '../../../src/domain/value-objects/dimensions.vo.js';

describe('Application Unit Tests: Serialization Use Cases', () => {
  let canvasRepo: InMemoryCanvasStateRepository;
  let connectorRepo: InMemoryConnectorStateRepository;
  let exportXmlUseCase: ExportDrawioXmlUseCase;
  let importXmlUseCase: ImportDrawioXmlUseCase;
  let exportSvgUseCase: ExportSvgDiagramUseCase;

  beforeEach(() => {
    canvasRepo = new InMemoryCanvasStateRepository();
    connectorRepo = new InMemoryConnectorStateRepository();
    exportXmlUseCase = new ExportDrawioXmlUseCase(canvasRepo, connectorRepo);
    importXmlUseCase = new ImportDrawioXmlUseCase(canvasRepo, connectorRepo);
    exportSvgUseCase = new ExportSvgDiagramUseCase(canvasRepo, connectorRepo);
  });

  describe('ExportDrawioXmlUseCase', () => {
    it('debe generar un nombre de archivo normalizado y contenido valido', async () => {
      const shape = new ShapeEntity({
        id: 'node-alpha',
        type: 'rectangle',
        position: new Point(50, 50),
        dimensions: new Dimensions(120, 60),
        label: 'Alpha Service'
      });
      await canvasRepo.save(shape);

      const result = await exportXmlUseCase.execute({ title: 'Diagrama Especial: Módulo Citas!' });
      expect(result.format).toBe('drawio_xml');
      expect(result.mimeType).toBe('application/xml');
      expect(result.filename).toBe('diagrama_especial_m_dulo_citas_.drawio.xml');
      expect(result.content).toContain('id="node-alpha"');
    });
  });

  describe('ImportDrawioXmlUseCase', () => {
    it('debe rechazar un payload vacio', async () => {
      await expect(importXmlUseCase.execute({ xmlContent: '' })).rejects.toThrow('inválido o vacío');
    });

    it('debe rechazar ataques XXE (CWE-611)', async () => {
      const maliciousPayload = `
        <!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///etc/shadow"> ]>
        <mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/></root></mxGraphModel>
      `;
      await expect(importXmlUseCase.execute({ xmlContent: maliciousPayload })).rejects.toThrow(
        /Violación de seguridad: Declaración DOCTYPE\/XXE/
      );
    });

    it('debe rechazar XML que no corresponde al esquema mxGraphModel', async () => {
      const genericXml = '<document><title>Hola</title></document>';
      await expect(importXmlUseCase.execute({ xmlContent: genericXml })).rejects.toThrow(
        /mxGraphModel válida/
      );
    });

    it('debe importar y permitir anexionar sin borrar el canvas si clearExisting es false', async () => {
      // Estado previo
      const existing = new ShapeEntity({
        id: 'existing-shape',
        type: 'rectangle',
        position: new Point(10, 10),
        dimensions: new Dimensions(100, 50),
        label: 'Existente'
      });
      await canvasRepo.save(existing);

      const xmlToAdd = `
        <mxGraphModel>
          <root>
            <mxCell id="0"/>
            <mxCell id="1" parent="0"/>
            <mxCell id="new-node" value="Nuevo Nodo" vertex="1" parent="1">
              <mxGeometry x="250" y="250" width="140" height="70" as="geometry"/>
            </mxCell>
          </root>
        </mxGraphModel>
      `;

      const res = await importXmlUseCase.execute({ xmlContent: xmlToAdd, clearExisting: false });
      expect(res.success).toBe(true);
      expect(res.importedShapesCount).toBe(1);

      const all = await canvasRepo.findAll();
      expect(all.length).toBe(2);
      expect(all.map(s => s.id)).toContain('existing-shape');
      expect(all.map(s => s.id)).toContain('new-node');
    });
  });

  describe('ExportSvgDiagramUseCase', () => {
    it('debe generar membrete institucional con accesibilidad y fecha', async () => {
      const shape1 = new ShapeEntity({
        id: 's1',
        type: 'ellipse',
        position: new Point(100, 100),
        dimensions: new Dimensions(100, 80),
        label: 'Evento Inicio'
      });
      const shape2 = new ShapeEntity({
        id: 's2',
        type: 'diamond',
        position: new Point(300, 100),
        dimensions: new Dimensions(80, 80),
        label: 'Validacion'
      });
      await canvasRepo.save(shape1);
      await canvasRepo.save(shape2);

      const svgResult = await exportSvgUseCase.execute({
        title: 'Proceso de Consulta Digital',
        author: 'Equipo DIDT'
      });

      expect(svgResult.format).toBe('svg');
      expect(svgResult.mimeType).toBe('image/svg+xml');
      expect(svgResult.content).toContain('DIRECCION DE INNOVACION Y DESARROLLO TECNOLOGICO — IMSS');
      expect(svgResult.content).toContain('Proceso de Consulta Digital');
      expect(svgResult.content).toContain('Equipo DIDT');
      expect(svgResult.content).toContain('<ellipse');
      expect(svgResult.content).toContain('<polygon');
      expect(svgResult.content).toContain('role="img"');
      expect(svgResult.content).toContain('aria-label="Diagrama de Arquitectura DIDT IMSS"');
      expect(svgResult.content).toContain('#006341'); // Verde IMSS
      expect(svgResult.content).toContain('#B38E5D'); // Acento Dorado IMSS
    });
  });
});
