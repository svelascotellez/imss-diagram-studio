# Matriz de Trazabilidad Bidireccional: [FEAT-002] Conectores Dinamicos, Puntos de Anclaje y Enrutamiento Ortogonal

> **Generado automaticamente por SDD v6.6 al completar formalmente la funcionalidad.**

- **Fecha de Cierre**: 2026-11-08T19:59:22Z
- **Approval SHA**: D726E24370BFBA55F01EAFAAB478E722F6C7658625C49FDD9BF17E26A40B35DE
- **Completion SHA**: 263994C4B29EFB1CB55E84754150363C921279038E617D150A66CD32D1F832B6

| Criterio EARS | Escenario Gherkin | Test Automatizado | Archivos de Implementacion | Documentacion de Usuario |
| :--- | :--- | :--- | :--- | :--- |
| `AC-2.1 (Conexion exitosa con trayectoria ortogonal y flechas)` | `@AC-2.1` | `tests/acceptance/connector-interaction.spec.ts` | `src/domain/entities/connector.entity.ts, src/application/use-cases/create-connector.use-case.ts, src/presentation/components/Canvas.ts` | [user_guide_FEAT-002.md](user_guide_FEAT-002.md) |
| `AC-2.2 (Bloqueo de auto-bucles y puertos invalidos)` | `@AC-2.2` | `tests/unit/domain/connector.test.ts` | `src/domain/entities/connector.entity.ts, src/application/use-cases/create-connector.use-case.ts` | [user_guide_FEAT-002.md](user_guide_FEAT-002.md) |
| `AC-2.3 (Recalculo automatico en tiempo real de trayectoria ortogonal)` | `@AC-2.3` | `tests/unit/application/connector-use-cases.test.ts` | `src/application/use-cases/route-connector.use-case.ts, src/domain/value-objects/routing-path.vo.ts` | [user_guide_FEAT-002.md](user_guide_FEAT-002.md) |
| `AC-2.4 (Eliminacion en cascada de conectores asociados)` | `@AC-2.4` | `tests/unit/application/connector-use-cases.test.ts` | `src/application/use-cases/delete-shape-cascade.use-case.ts, src/infrastructure/repositories/in-memory-connector-state.repository.ts` | [user_guide_FEAT-002.md](user_guide_FEAT-002.md) |
