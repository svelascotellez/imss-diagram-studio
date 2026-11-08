# Matriz de Trazabilidad Bidireccional: [FEAT-004] Serializacion XML Draw.io y Exportacion SVG/PNG

> **Generado automaticamente por SDD v6.6 al completar formalmente la funcionalidad.**

- **Fecha de Cierre**: 2026-11-08T20:23:00Z
- **Approval SHA**: E52932FC88F6B06C1A7CF0DCC9CC75742AE01D7D4EB1AF0291564BADDD0D53B6
- **Completion SHA**: EFD2304BB52ED41063A575E047D831E9F69D46C97CFC1FA8F845E70ADD2ECF70

| Criterio EARS | Escenario Gherkin | Test Automatizado | Archivos de Implementacion | Documentacion de Usuario |
| :--- | :--- | :--- | :--- | :--- |
| `AC-4.1 (Exportacion Draw.io XML mxGraphModel)` | `@AC-4.1` | `tests/acceptance/serialization-interaction.spec.ts` | `src/application/use-cases/export-drawio-xml.use-case.ts, src/domain/services/drawio-serializer.service.ts, src/domain/value-objects/diagram-export.vo.ts` | [user_guide_FEAT-004.md](user_guide_FEAT-004.md) |
| `AC-4.2 (Deserializacion e importacion en < 100 ms)` | `@AC-4.2` | `tests/acceptance/serialization-interaction.spec.ts` | `src/application/use-cases/import-drawio-xml.use-case.ts, src/infrastructure/serializers/mxgraph-xml-parser.ts` | [user_guide_FEAT-004.md](user_guide_FEAT-004.md) |
| `AC-4.3 (Exportacion SVG con membrete oficial DIDT)` | `@AC-4.3` | `tests/acceptance/serialization-interaction.spec.ts` | `src/application/use-cases/export-svg-diagram.use-case.ts, src/presentation/components/Canvas.ts` | [user_guide_FEAT-004.md](user_guide_FEAT-004.md) |
| `AC-4.4 (Bloqueo de XML malformado y proteccion anti-XXE)` | `@AC-4.4` | `tests/unit/application/serialization-use-cases.test.ts` | `src/infrastructure/serializers/mxgraph-xml-parser.ts, src/application/use-cases/import-drawio-xml.use-case.ts` | [user_guide_FEAT-004.md](user_guide_FEAT-004.md) |
