import { describe, it, expect } from 'vitest';
import { DiagramExportVO } from '../../../src/domain/value-objects/diagram-export.vo.js';
import { DrawioSerializerService } from '../../../src/domain/services/drawio-serializer.service.js';
import { ShapeEntity } from '../../../src/domain/entities/shape.entity.js';
import { ConnectorEntity } from '../../../src/domain/entities/connector.entity.js';
import { Point } from '../../../src/domain/value-objects/point.vo.js';
import { Dimensions } from '../../../src/domain/value-objects/dimensions.vo.js';

describe('Domain Unit Tests: Serializer & DiagramExportVO', () => {
  describe('DiagramExportVO', () => {
    it('debe crear un DiagramExportVO con valores validos', () => {
      const vo = new DiagramExportVO({
        format: 'drawio_xml',
        content: '<mxGraphModel></mxGraphModel>',
        filename: 'diagrama.drawio.xml',
        mimeType: 'application/xml',
        title: 'Arquitectura IMSS'
      });

      expect(vo.format).toBe('drawio_xml');
      expect(vo.content).toBe('<mxGraphModel></mxGraphModel>');
      expect(vo.filename).toBe('diagrama.drawio.xml');
      expect(vo.mimeType).toBe('application/xml');
      expect(vo.title).toBe('Arquitectura IMSS');
      expect(vo.exportedAt).toBeInstanceOf(Date);
      expect(vo.byteLength).toBeGreaterThan(0);
    });

    it('debe rechazar contenido vacio o solo espacios', () => {
      expect(() => {
        new DiagramExportVO({
          format: 'svg',
          content: '   ',
          filename: 'diagrama.svg',
          mimeType: 'image/svg+xml'
        });
      }).toThrow('Export content cannot be empty');
    });

    it('debe rechazar filename vacio', () => {
      expect(() => {
        new DiagramExportVO({
          format: 'svg',
          content: '<svg></svg>',
          filename: '',
          mimeType: 'image/svg+xml'
        });
      }).toThrow('Export filename cannot be empty');
    });
  });

  describe('DrawioSerializerService', () => {
    const serializer = new DrawioSerializerService();

    it('debe escapar correctamente caracteres especiales XML', () => {
      const input = 'Servicio & Proceso <Seguridad> "DIDT" \'IMSS\'';
      const escaped = DrawioSerializerService.escapeXml(input);
      expect(escaped).toBe('Servicio &amp; Proceso &lt;Seguridad&gt; &quot;DIDT&quot; &apos;IMSS&apos;');
    });

    it('debe derivar estilos mxGraph segun el tipo de forma', () => {
      const rect = new ShapeEntity({
        id: '1',
        type: 'rectangle',
        position: new Point(10, 10),
        dimensions: new Dimensions(100, 50)
      });
      const ellipse = new ShapeEntity({
        id: '2',
        type: 'ellipse',
        position: new Point(10, 10),
        dimensions: new Dimensions(100, 50)
      });
      const diamond = new ShapeEntity({
        id: '3',
        type: 'diamond',
        position: new Point(10, 10),
        dimensions: new Dimensions(100, 50)
      });
      const container = new ShapeEntity({
        id: '4',
        type: 'container',
        position: new Point(10, 10),
        dimensions: new Dimensions(200, 150)
      });

      expect(DrawioSerializerService.deriveMxStyle(rect)).toContain('rounded=1;');
      expect(DrawioSerializerService.deriveMxStyle(ellipse)).toContain('ellipse;');
      expect(DrawioSerializerService.deriveMxStyle(diamond)).toContain('rhombus;');
      expect(DrawioSerializerService.deriveMxStyle(container)).toContain('swimlane;');
    });

    it('debe serializar un canvas vacio con la raiz valida de mxGraphModel', () => {
      const xml = serializer.serialize([], []);
      expect(xml).toContain('<mxGraphModel');
      expect(xml).toContain('</mxGraphModel>');
      expect(xml).toContain('<mxCell id="0"/>');
      expect(xml).toContain('<mxCell id="1" parent="0"/>');
    });

    it('debe serializar formas y conectores preservando atributos y geometrias', () => {
      const shape = new ShapeEntity({
        id: 'shape-100',
        type: 'rectangle',
        position: new Point(150, 220),
        dimensions: new Dimensions(180, 90),
        label: 'Modulo de Pagos IMSS'
      });
      const conn = new ConnectorEntity({
        id: 'conn-100',
        sourceShapeId: 'shape-100',
        sourcePort: 'south',
        targetShapeId: 'shape-200',
        targetPort: 'north',
        label: 'HTTPS / REST'
      });

      const xml = serializer.serialize([shape], [conn]);
      expect(xml).toContain('id="shape-100"');
      expect(xml).toContain('value="Modulo de Pagos IMSS"');
      expect(xml).toContain('x="150" y="220" width="180" height="90"');
      expect(xml).toContain('id="conn-100"');
      expect(xml).toContain('value="HTTPS / REST"');
      expect(xml).toContain('source="shape-100" target="shape-200"');
    });
  });
});
