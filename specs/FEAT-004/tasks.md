# Lista de Tareas Atomicas: FEAT-004

- [x] `T-01`: [tests/acceptance/serialization-interaction.spec.ts] Implementar suite de aceptacion BDD para `@AC-4.1` a `@AC-4.4`. (Verde)
- [x] `T-02`: [src/domain/value-objects/diagram-export.vo.ts] Implementar Value Object inmutable para metadatos y payloads de exportacion. (Verde)
- [x] `T-03`: [src/domain/services/drawio-serializer.service.ts] Implementar Servicio de Dominio para serializacion mxGraphModel. (Verde)
- [x] `T-04`: [src/infrastructure/serializers/mxgraph-xml-parser.ts] Implementar parser seguro anti-XXE para deserializacion de modelos mxGraph. (Verde)
- [x] `T-05`: [src/application/use-cases/export-drawio-xml.use-case.ts] Implementar caso de uso de exportacion Draw.io XML (`@AC-4.1`). (Verde)
- [x] `T-06`: [src/application/use-cases/import-drawio-xml.use-case.ts] Implementar caso de uso de importacion Draw.io XML con validacion y rollback seguro (`@AC-4.2`, `@AC-4.4`). (Verde)
- [x] `T-07`: [src/application/use-cases/export-svg-diagram.use-case.ts] Implementar caso de uso de exportacion SVG con membrete oficial institucional DIDT IMSS (`@AC-4.3`). (Verde)
- [x] `T-08`: [tests/unit/domain/serializer.test.ts] Implementar pruebas unitarias de dominio para serializacion y value objects. (Verde)
- [x] `T-09`: [tests/unit/application/serialization-use-cases.test.ts] Implementar pruebas unitarias de aplicacion y proteccion anti-XXE. (Verde)
- [x] `T-10`: [src/presentation/components/Canvas.ts] Integrar metodos de serializacion en el componente Canvas. (Verde)
- [x] `T-11`: [docs/user_guide_FEAT-004.md] Redactar la Guia de Usuario obligatoria para interoperabilidad y membrete institucional. (Verde)
- [x] `T-12`: [harness] Ejecutar suite de pruebas vitest y auditar compuertas de gobernanza SDD v6.6. (Verde)
