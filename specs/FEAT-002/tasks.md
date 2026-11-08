# Lista de Tareas Atomicas: FEAT-002

- [x] `T-01`: [tests/acceptance/connector-interaction.spec.ts] Implementar suite de aceptacion BDD para `@AC-2.1` (conexion ortogonal con flechas). (Verde)
- [x] `T-02`: [src/domain/value-objects/connection-port.vo.ts, src/domain/value-objects/routing-path.vo.ts, src/domain/entities/connector.entity.ts] Implementar Value Objects y Entidad Connector. (Verde)
- [x] `T-03`: [src/domain/repositories/connector-state.repository.ts, src/application/use-cases/create-connector.use-case.ts] Implementar puerto y caso de uso de creacion de conectores. (Verde)
- [x] `T-04`: [tests/unit/domain/connector.test.ts] Implementar suite de pruebas unitarias para validacion y bloqueo de auto-bucles y puertos invalidos (`@AC-2.2`). (Verde)
- [x] `T-05`: [src/application/use-cases/create-connector.use-case.ts] Implementar validaciones anti-auto-bucle y control de precondiciones. (Verde)
- [x] `T-06`: [tests/unit/application/connector-use-cases.test.ts] Implementar pruebas unitarias para recalculo automatico de ruta ortogonal ante movimiento (`@AC-2.3`). (Verde)
- [x] `T-07`: [src/application/use-cases/route-connector.use-case.ts] Implementar algoritmo de enrutamiento ortogonal reactivo Manhattan. (Verde)
- [x] `T-08`: [src/application/use-cases/delete-shape-cascade.use-case.ts] Implementar eliminacion en cascada de conectores asociados (`@AC-2.4`). (Verde)
- [x] `T-09`: [src/presentation/components/Canvas.ts] Actualizar componente Canvas para renderizado de conectores SVG y puertos magneticos interactivos. (Verde)
- [x] `T-10`: [docs/user_guide_FEAT-002.md] Redactar la Guia de Usuario obligatoria para conectores y enrutamiento dinamico.
- [x] `T-11`: [harness] Ejecutar suite de pruebas vitest y auditar compuertas de gobernanza.
