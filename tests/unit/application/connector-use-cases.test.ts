import { describe, it, expect, beforeEach } from 'vitest';
import { InMemoryCanvasStateRepository } from '../../../src/infrastructure/repositories/in-memory-canvas-state.repository.js';
import { InMemoryConnectorStateRepository } from '../../../src/infrastructure/repositories/in-memory-connector-state.repository.js';
import { CreateShapeUseCase } from '../../../src/application/use-cases/create-shape.use-case.js';
import { CreateConnectorUseCase } from '../../../src/application/use-cases/create-connector.use-case.js';
import { RouteConnectorUseCase } from '../../../src/application/use-cases/route-connector.use-case.js';
import { DeleteShapeCascadeUseCase } from '../../../src/application/use-cases/delete-shape-cascade.use-case.js';
import { MoveShapesUseCase } from '../../../src/application/use-cases/move-shapes.use-case.js';

describe('FEAT-002 Application Use Cases: Enrutamiento Reactivo y Cascada', () => {
  let shapeRepo: InMemoryCanvasStateRepository;
  let connectorRepo: InMemoryConnectorStateRepository;
  let createShape: CreateShapeUseCase;
  let createConnector: CreateConnectorUseCase;
  let routeConnector: RouteConnectorUseCase;
  let deleteCascade: DeleteShapeCascadeUseCase;
  let moveShapes: MoveShapesUseCase;

  beforeEach(() => {
    shapeRepo = new InMemoryCanvasStateRepository();
    connectorRepo = new InMemoryConnectorStateRepository();
    createShape = new CreateShapeUseCase(shapeRepo);
    createConnector = new CreateConnectorUseCase(shapeRepo, connectorRepo);
    routeConnector = new RouteConnectorUseCase(shapeRepo, connectorRepo);
    deleteCascade = new DeleteShapeCascadeUseCase(shapeRepo, connectorRepo);
    moveShapes = new MoveShapesUseCase(shapeRepo);
  });

  describe('@AC-2.3: Recalculo automatico en tiempo real de trayectoria ortogonal al mover formas', () => {
    it('debe recalcular los waypoints ortogonales reactivamente cuando se desplaza la forma destino', async () => {
      const s1 = await createShape.execute({ type: 'rectangle', x: 100, y: 100, width: 100, height: 60 });
      const s2 = await createShape.execute({ type: 'rectangle', x: 400, y: 100, width: 100, height: 60 });

      const conn = await createConnector.execute({
        sourceShapeId: s1.id,
        sourcePort: 'east',
        targetShapeId: s2.id,
        targetPort: 'west'
      });

      // Ruta inicial recta horizontal (ambos en y=130)
      const initialPath = await routeConnector.computePath(conn.id);
      expect(initialPath.isOrthogonal()).toBe(true);
      expect(initialPath.waypoints[0].y).toBe(130);
      expect(initialPath.waypoints[initialPath.waypoints.length - 1].y).toBe(130);

      // Desplazar s2 verticalmente a (400, 300)
      s2.moveTo(400, 300);
      await shapeRepo.save(s2);

      // Recalcular ruta: debe generar un trayecto ortogonal escalonado con angulos de 90 grados
      const updatedPath = await routeConnector.computePath(conn.id);
      expect(updatedPath.isOrthogonal()).toBe(true);
      expect(updatedPath.waypoints.length).toBe(4);

      // Waypoint inicial en s1 (este: 200, 130)
      expect(updatedPath.waypoints[0].x).toBe(200);
      expect(updatedPath.waypoints[0].y).toBe(130);

      // Waypoint final en s2 (oeste: 400, 330)
      expect(updatedPath.waypoints[3].x).toBe(400);
      expect(updatedPath.waypoints[3].y).toBe(330);

      // Puntos intermedios de quiebre ortogonal en x=300 (punto medio entre 200 y 400)
      expect(updatedPath.waypoints[1].x).toBe(300);
      expect(updatedPath.waypoints[1].y).toBe(130);
      expect(updatedPath.waypoints[2].x).toBe(300);
      expect(updatedPath.waypoints[2].y).toBe(330);
    });
  });

  describe('@AC-2.4: Eliminacion en cascada de conectores dependientes', () => {
    it('debe eliminar la forma y todos los conectores vinculados para evitar referencias huerfanas', async () => {
      const gateway = await createShape.execute({ type: 'diamond', x: 200, y: 200, width: 80, height: 80 });
      const micro1 = await createShape.execute({ type: 'rectangle', x: 50, y: 200, width: 80, height: 60 });
      const micro2 = await createShape.execute({ type: 'rectangle', x: 350, y: 200, width: 80, height: 60 });

      // 2 conectores vinculados al gateway
      const conn1 = await createConnector.execute({
        sourceShapeId: micro1.id,
        sourcePort: 'east',
        targetShapeId: gateway.id,
        targetPort: 'west'
      });

      const conn2 = await createConnector.execute({
        sourceShapeId: gateway.id,
        sourcePort: 'east',
        targetShapeId: micro2.id,
        targetPort: 'west'
      });

      expect((await connectorRepo.findAll()).length).toBe(2);

      // Eliminar el Gateway
      const result = await deleteCascade.execute(gateway.id);
      expect(result.shapeDeleted).toBe(true);
      expect(result.connectorsDeletedCount).toBe(2);

      // El repositorio de formas ya no debe contener el gateway
      expect(await shapeRepo.findById(gateway.id)).toBeNull();

      // Ambos conectores dependientes deben haber sido purgados en cascada
      expect(await connectorRepo.findById(conn1.id)).toBeNull();
      expect(await connectorRepo.findById(conn2.id)).toBeNull();
      expect((await connectorRepo.findAll()).length).toBe(0);
    });
  });
});
