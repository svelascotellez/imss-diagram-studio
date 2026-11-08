# Lista de Tareas Atomicas: FEAT-003

- [x] `T-01`: [tests/acceptance/stencil-interaction.spec.ts] Implementar suite de aceptacion BDD para `@AC-3.1` (instanciacion de stencils). (Verde)
- [x] `T-02`: [src/domain/value-objects/stencil-category.vo.ts, src/domain/entities/stencil.entity.ts] Implementar Value Object y Entidad Stencil. (Verde)
- [x] `T-03`: [src/domain/repositories/stencil-catalog.repository.ts, src/infrastructure/repositories/in-memory-stencil-catalog.repository.ts] Implementar puerto y repositorio en memoria con stencils oficiales DIDT e IMSS. (Verde)
- [x] `T-04`: [tests/unit/domain/stencil.test.ts] Implementar pruebas unitarias de dominio y validacion de categorias. (Verde)
- [x] `T-05`: [tests/unit/application/stencil-use-cases.test.ts] Implementar pruebas unitarias para filtrado reactivo (`@AC-3.2`) y fallback seguro (`@AC-3.4`). (Verde)
- [x] `T-06`: [src/application/use-cases/search-stencils.use-case.ts] Implementar busqueda reactiva y filtrado en < 50 ms. (Verde)
- [x] `T-07`: [src/application/use-cases/instantiate-stencil.use-case.ts] Implementar caso de uso de instanciacion hacia el canvas con fallback seguro a Servicio Institucional. (Verde)
- [x] `T-08`: [src/presentation/components/StencilSidebar.ts] Implementar componente visual StencilSidebar con categorias accesibles ARIA (`@AC-3.3`). (Verde)
- [x] `T-09`: [src/presentation/components/Canvas.ts] Integrar StencilSidebar con Canvas interactivo. (Verde)
- [x] `T-10`: [docs/user_guide_FEAT-003.md] Redactar la Guia de Usuario obligatoria para la biblioteca de stencils DIDT e IMSS.
- [x] `T-11`: [harness] Ejecutar suite de pruebas vitest y auditar compuertas de gobernanza.
