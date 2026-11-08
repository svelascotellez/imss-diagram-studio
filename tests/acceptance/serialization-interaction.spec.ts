import { describe, it, expect, beforeEach } from 'vitest';
import { InMemoryCanvasStateRepository } from '../../src/infrastructure/repositories/in-memory-canvas-state.repository.js';
import { InMemoryConnectorStateRepository } from '../../src/infrastructure/repositories/in-memory-connector-state.repository.js';
import { ShapeEntity } from '../../src/domain/entities/shape.entity.js';
import { ConnectorEntity } from '../../src/domain/entities/connector.entity.js';
import { Point } from '../../src/domain/value-objects/point.vo.js';
import { Dimensions } from '../../src/domain/value-objects/dimensions.vo.js';
import { ExportDrawioXmlUseCase } from '../../src/application/use-cases/export-drawio-xml.use-case.js';
import { ImportDrawioXmlUseCase } from '../../src/application/use-cases/import-drawio-xml.use-case.js';
import { ExportSvgDiagramUseCase } from '../../src/application/use-cases/export-svg-diagram.use-case.js';

describe('FEAT-004 Acceptance Tests: Serializacion Bidireccional y Exportacion con Membrete DIDT', () => {
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

  it('@AC-4.1: Exportacion exitosa de canvas a XML compatible con Draw.io', async () => {
    // Dado un canvas con dos formas y un conector activo entre ellas
    const shapeA = new ShapeEntity({
      id: 'shape-gateway',
      type: 'rectangle',
      position: new Point(100, 150),
      dimensions: new Dimensions(160, 70),
      label: 'API Gateway DIDT'
    });
    const shapeB = new ShapeEntity({
      id: 'shape-db',
      type: 'rectangle',
      position: new Point(360, 150),
      dimensions: new Dimensions(140, 60),
      label: 'Base de Datos IMSS'
    });
    await canvasRepo.save(shapeA);
    await canvasRepo.save(shapeB);

    const connector = new ConnectorEntity({
      id: 'conn-1',
      sourceShapeId: 'shape-gateway',
      sourcePort: 'east',
      targetShapeId: 'shape-db',
      targetPort: 'west',
      routingType: 'orthogonal'
    });
    await connectorRepo.save(connector);

    // Cuando el usuario solicita exportar el diagrama a formato Draw.io XML
    const exportResult = await exportXmlUseCase.execute({ title: 'Diagrama Arquitectura DIDT' });

    // Entonces el sistema genera una cadena XML valida con la etiqueta raiz "<mxGraphModel>"
    expect(exportResult.format).toBe('drawio_xml');
    expect(exportResult.content).toContain('<mxGraphModel');
    expect(exportResult.content).toContain('</mxGraphModel>');
    expect(exportResult.content).toContain('<root>');
    expect(exportResult.content).toContain('<mxCell id="0"/>');
    expect(exportResult.content).toContain('<mxCell id="1" parent="0"/>');

    // Y el XML contiene las definiciones "mxCell" correspondientes a los nodos y al enlace conectivo
    expect(exportResult.content).toContain('id="shape-gateway"');
    expect(exportResult.content).toContain('value="API Gateway DIDT"');
    expect(exportResult.content).toContain('id="shape-db"');
    expect(exportResult.content).toContain('value="Base de Datos IMSS"');
    expect(exportResult.content).toContain('id="conn-1"');
    expect(exportResult.content).toContain('source="shape-gateway"');
    expect(exportResult.content).toContain('target="shape-db"');
    expect(exportResult.content).toContain('edge="1"');
  });

  it('@AC-4.2: Deserializacion e importacion exitosa de archivo Draw.io XML hacia el canvas', async () => {
    // Dado un archivo XML valido bajo el esquema "<mxGraphModel>" con 2 formas y 1 conector
    const validXml = `
      <mxGraphModel>
        <root>
          <mxCell id="0"/>
          <mxCell id="1" parent="0"/>
          <mxCell id="node-1" value="Microservicio Afiliacion" vertex="1" parent="1" style="strokeColor=#006341;">
            <mxGeometry x="120" y="80" width="160" height="70" as="geometry"/>
          </mxCell>
          <mxCell id="node-2" value="Servicio de Autenticacion" vertex="1" parent="1" style="strokeColor=#006341;">
            <mxGeometry x="400" y="80" width="160" height="70" as="geometry"/>
          </mxCell>
          <mxCell id="edge-1" edge="1" parent="1" source="node-1" target="node-2">
            <mxGeometry relative="1" as="geometry"/>
          </mxCell>
        </root>
      </mxGraphModel>
    `;

    const startTime = performance.now();
    // Cuando el usuario importa el documento XML al sistema
    const result = await importXmlUseCase.execute({ xmlContent: validXml });
    const elapsedTime = performance.now() - startTime;

    // Entonces el canvas es poblado fielmente con las formas en sus posiciones exactas en menos de 100 ms
    expect(result.success).toBe(true);
    expect(elapsedTime).toBeLessThan(100);

    const shapes = await canvasRepo.findAll();
    expect(shapes.length).toBe(2);
    const shape1 = await canvasRepo.findById('node-1');
    expect(shape1).toBeDefined();
    expect(shape1?.label).toBe('Microservicio Afiliacion');
    expect(shape1?.position.x).toBe(120);
    expect(shape1?.position.y).toBe(80);

    // Y el conector es reconstruido con sus extremos enlazados
    const connectors = await connectorRepo.findAll();
    expect(connectors.length).toBe(1);
    expect(connectors[0].id).toBe('edge-1');
    expect(connectors[0].sourceShapeId).toBe('node-1');
    expect(connectors[0].targetShapeId).toBe('node-2');
  });

  it('@AC-4.3: Exportacion vectorial a SVG con membrete oficial DIDT IMSS', async () => {
    // Dado un diagrama con componentes arquitectonicos en el canvas
    const shape = new ShapeEntity({
      id: 'shape-portal',
      type: 'rectangle',
      position: new Point(50, 100),
      dimensions: new Dimensions(180, 80),
      label: 'Portal Ciudadano IMSS Digital'
    });
    await canvasRepo.save(shape);

    // Cuando el usuario exporta el diagrama en formato SVG vectorial
    const svgResult = await exportSvgUseCase.execute({ title: 'Arquitectura IMSS Digital' });

    // Entonces el documento SVG resultante incluye el membrete oficial institucional
    expect(svgResult.format).toBe('svg');
    expect(svgResult.content).toContain('<svg');
    expect(svgResult.content).toContain('DIRECCION DE INNOVACION Y DESARROLLO TECNOLOGICO');
    expect(svgResult.content).toContain('IMSS');

    // Y el documento incorpora metadatos accesibles WCAG 2.1 AA y fecha de emision
    expect(svgResult.content).toContain('role="img"');
    expect(svgResult.content).toContain('aria-label="Diagrama de Arquitectura DIDT IMSS"');
    expect(svgResult.content).toContain('#006341'); // Color Verde IMSS institucional
  });

  it('@AC-4.4: Bloqueo de XML malformado o con entidad externa XXE preservando el estado del canvas', async () => {
    // Dado un canvas con una forma existente
    const initialShape = new ShapeEntity({
      id: 'initial-shape',
      type: 'rectangle',
      position: new Point(20, 20),
      dimensions: new Dimensions(100, 50),
      label: 'Estado Inicial Seguro'
    });
    await canvasRepo.save(initialShape);

    // Caso A: XML malformado (sin cierre de tags)
    const malformedXml = '<mxGraphModel><root><mxCell id="0">';
    await expect(importXmlUseCase.execute({ xmlContent: malformedXml })).rejects.toThrow();

    // Caso B: Ataque XXE con declaracion DOCTYPE externa
    const xxeXml = `<?xml version="1.0" encoding="ISO-8859-1"?>
      <!DOCTYPE foo [  
      <!ELEMENT foo ANY >
      <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
      <mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/></root></mxGraphModel>`;
    await expect(importXmlUseCase.execute({ xmlContent: xxeXml })).rejects.toThrow(/seguridad|xxe|doctype/i);

    // Caso C: No es mxGraphModel
    const notMxGraph = '<svg><rect x="0" y="0"/></svg>';
    await expect(importXmlUseCase.execute({ xmlContent: notMxGraph })).rejects.toThrow(/mxGraphModel/i);

    // Y el canvas mantiene su estado previo sin alteraciones
    const shapesAfter = await canvasRepo.findAll();
    expect(shapesAfter.length).toBe(1);
    expect(shapesAfter[0].id).toBe('initial-shape');
  });
});
