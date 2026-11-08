import { describe, it, expect, beforeEach } from 'vitest';
import { InMemoryCanvasStateRepository } from '../../src/infrastructure/repositories/in-memory-canvas-state.repository.js';
import { InMemoryConnectorStateRepository } from '../../src/infrastructure/repositories/in-memory-connector-state.repository.js';
import { CreateShapeUseCase } from '../../src/application/use-cases/create-shape.use-case.js';
import { CreateConnectorUseCase } from '../../src/application/use-cases/create-connector.use-case.js';
import { RouteConnectorUseCase } from '../../src/application/use-cases/route-connector.use-case.js';

describe('FEAT-002 Acceptance Tests: Conectores Dinamicos y Enrutamiento Ortogonal', () => {
  let shapeRepo: InMemoryCanvasStateRepository;
  let connectorRepo: InMemoryConnectorStateRepository;
  let createShape: CreateShapeUseCase;
  let createConnector: CreateConnectorUseCase;
  let routeConnector: RouteConnectorUseCase;

  beforeEach(() => {
    shapeRepo = new InMemoryCanvasStateRepository();
    connectorRepo = new InMemoryConnectorStateRepository();
    createShape = new CreateShapeUseCase(shapeRepo);
    createConnector = new CreateConnectorUseCase(shapeRepo, connectorRepo);
    routeConnector = new RouteConnectorUseCase(shapeRepo, connectorRepo);
  });

  it('@AC-2.1: Conexion exitosa entre dos formas con trayectoria ortogonal y marcadores', async () => {
    // Dado un canvas con dos formas geometricas "Servicio A" en (100, 100, 100x60) y "Servicio B" en (300, 100, 100x60)
    const shapeA = await createShape.execute({
      type: 'rectangle',
      x: 100,
      y: 100,
      width: 100,
      height: 60,
      label: 'Servicio A'
    });

    const shapeB = await createShape.execute({
      type: 'rectangle',
      x: 300,
      y: 100,
      width: 100,
      height: 60,
      label: 'Servicio B'
    });

    // Cuando el usuario traza un conector desde el puerto "east" de shapeA hacia el puerto "west" de shapeB
    const connector = await createConnector.execute({
      sourceShapeId: shapeA.id,
      sourcePort: 'east',
      targetShapeId: shapeB.id,
      targetPort: 'west',
      label: 'Invoca gRPC'
    });

    // Entonces el conector es persistido en el modelo de dominio
    expect(connector).toBeDefined();
    expect(connector.id).toBeDefined();
    expect(connector.sourceShapeId).toBe(shapeA.id);
    expect(connector.sourcePort).toBe('east');
    expect(connector.targetShapeId).toBe(shapeB.id);
    expect(connector.targetPort).toBe('west');

    const saved = await connectorRepo.findById(connector.id);
    expect(saved).not.toBeNull();

    // Y el conector traza segmentos ortogonales perpendiculares con flecha direccional en el extremo receptor
    const path = await routeConnector.computePath(connector.id);
    expect(path.waypoints.length).toBeGreaterThanOrEqual(2);
    expect(path.waypoints[0].x).toBe(200); // 100 + 100 (borde este de shapeA)
    expect(path.waypoints[0].y).toBe(130); // 100 + 60/2 (centro vertical de shapeA)
    expect(path.waypoints[path.waypoints.length - 1].x).toBe(300); // borde oeste de shapeB
    expect(path.waypoints[path.waypoints.length - 1].y).toBe(130); // centro vertical de shapeB
    expect(connector.hasEndArrow).toBe(true);
  });
});
