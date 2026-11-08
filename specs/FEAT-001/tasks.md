# Lista de Tareas Atomicas: FEAT-001

- [x] `T-01`: [tests/acceptance/canvas-interaction.spec.ts] Implementar suite de aceptacion BDD para `@AC-1.1` (creacion y renderizado de formas). (Rojo -> Verde)
- [x] `T-02`: [src/domain/value-objects/point.vo.ts, src/domain/value-objects/dimensions.vo.ts, src/domain/entities/shape.entity.ts] Implementar Value Objects inmutables y Entidad de forma vectorial. (Verde)
- [x] `T-03`: [src/domain/repositories/canvas-state.repository.ts, src/application/use-cases/create-shape.use-case.ts] Implementar puerto de repositorio y caso de uso de creacion de formas. (Verde)
- [x] `T-04`: [tests/unit/domain/shape.test.ts] Implementar pruebas unitarias para validacion y acotamiento de limites minimos 20x20 px (`@AC-1.2`). (Verde)
- [x] `T-05`: [src/domain/value-objects/dimensions.vo.ts, src/domain/entities/shape.entity.ts] Implementar acotamiento estricto a umbral minimo en entidad y value objects. (Verde)
- [x] `T-06`: [tests/unit/application/canvas-use-cases.test.ts] Implementar pruebas unitarias para seleccion rectangular y feedback accesible (`@AC-1.3`). (Verde)
- [x] `T-07`: [src/application/use-cases/select-shapes.use-case.ts] Implementar calculo de interseccion por area y seleccion múltiple reactiva. (Verde)
- [x] `T-08`: [src/application/use-cases/move-shapes.use-case.ts] Implementar desplazamiento atomico sincronizado preservando distancias relativas (`@AC-1.4`). (Verde)
- [x] `T-09`: [src/presentation/components/Canvas.ts] Implementar componente Canvas con paleta institucional IMSS (#006341, #B38E5D) y atributos accesibles ARIA. (Verde)
- [x] `T-10`: [docs/user_guide_FEAT-001.md] Redactar la Guia de Usuario obligatoria con manual de operacion del canvas.
- [x] `T-11`: [harness] Ejecutar suite de pruebas vitest y validar compuertas de gobernanza.
