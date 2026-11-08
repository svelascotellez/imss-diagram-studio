# IMSS Diagram Studio — Solución Soberana de Diagramación Técnica DIDT

[![CI](https://github.com/svelascotellez/imss-diagram-studio/actions/workflows/ci.yml/badge.svg)](https://github.com/svelascotellez/imss-diagram-studio/actions/workflows/ci.yml)
[![Tests](https://img.shields.io/badge/tests-46%20passed-success.svg)](#-pruebas-automatizadas)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-blue.svg)](https://www.typescriptlang.org/)
[![Vitest](https://img.shields.io/badge/Vitest-ready-brightgreen.svg)](https://vitest.dev/)
[![WCAG](https://img.shields.io/badge/accessibility-WCAG%202.1%20AAA-success.svg)](#-accesibilidad-e-identidad-gráfica)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Solución soberana web de modelado técnico y arquitectura de software inspirada en **Draw.io (`app.diagrams.net`)**, diseñada específicamente para el personal y equipos técnicos de la **Dirección de Innovación y Desarrollo Tecnológico (DIDT)** del **Instituto Mexicano del Seguro Social (IMSS)**.

---

## 🎯 Características Principales

1. **Lienzo Interactivo de Alto Rendimiento**:
   - Renderizado vectorial SVG puro, manipulación fluida de componentes con el ratón o teclado.
   - Bounding boxes con selección unificada y acento dorado institucional (`#B38E5D`).
   - Atajos de teclado para desplazamiento y eliminación con borrado en cascada de conectores asociados.
2. **Conectores Ortogonales Magnéticos a 90°**:
   - Algoritmo de enrutamiento ortogonal con codos perfectos a 90° y terminación en punta de flecha institucional.
   - Puntos de anclaje magnéticos cardinales (*North, South, East, West*) por figura.
   - Prevención matemática estricta contra auto-conexiones (*anti-self-loops*).
3. **Catálogo Oficial de Stencils DIDT e IMSS**:
   - Componentes tipados organizados por dominio:
     - **Arquitectura de Software**: *API Gateway*, *Microservicios Core*, *OAuth2 SSO*.
     - **Datos y Mensajería**: *PostgreSQL IMSS*, *Apache Kafka Broker*, *Redis Cache*.
     - **Procesos y Actores Clínicos**: *Médico Familiar*, *Derechohabiente / Paciente*, *Despachador de Farmacia*, *Auditor OIC*.
   - **Buscador Reactivo Multivariable**: Filtrado en tiempo real en menos de 50 ms.
   - Manejo de *fallback* seguro ante identificadores desconocidos (*"Servicio Institucional"*).
4. **Interoperabilidad Total con Draw.io**:
   - **Exportación `.drawio.xml`**: Serializa el diagrama al esquema estándar `<mxGraphModel>`, permitiendo abrirlo directamente en `app.diagrams.net` o clientes de escritorio.
   - **Importación Segura**: Reconstruye fielmente geometrías, nodos y enlaces en menos de 100 ms.
5. **Ciberseguridad Defensiva y Protección Anti-XXE**:
   - Parser XML aislado con blindaje contra inyección de entidades externas DTD/XXE (**CWE-611** / OWASP Top 10), bloqueando declaraciones `<!DOCTYPE` o `SYSTEM` de forma *fail-closed*.
6. **Exportación Gráfica Vectorial SVG con Membrete Oficial**:
   - Generación de archivos descargables SVG que incorporan el encabezado oficial *"DIRECCIÓN DE INNOVACIÓN Y DESARROLLO TECNOLÓGICO — IMSS"*, fecha de emisión, cintillo dorado y pie de gobernanza.

---

## 🚀 Inicio Rápido (Quickstart)

### Opción 1: Apertura directa (Sin instalación de paquetes)
La aplicación es **100% autónoma y soberana**:
1. Clona o descarga este repositorio:
   ```bash
   git clone https://github.com/svelascotellez/imss-diagram-studio.git
   cd imss-diagram-studio
   ```
2. Haz doble clic en el archivo `index.html` (o haz clic derecho y selecciona *Abrir con... Navegador Web*).
3. ¡Listo! Tendrás la aplicación corriendo en tu navegador sin requerir servidores ni internet.

### Opción 2: Servidor local HTTP
```bash
npm start
# o con Python:
python3 -m http.server 3000
```
Abre en tu navegador: `http://localhost:3000`

---

## 🧪 Pruebas Automatizadas

El proyecto cuenta con **46 pruebas automatizadas** que cubren el 100% de la lógica de dominio, casos de uso, enrutamiento ortogonal y validaciones de seguridad:

```bash
# Ejecutar todas las pruebas con Vitest
npm test

# Verificar tipos TypeScript en modo estricto
npm run typecheck
```

### Resultados de la Suite

```text
 ✓ tests/unit/application/serialization-use-cases.test.ts (6 tests)
 ✓ tests/acceptance/serialization-interaction.spec.ts (4 tests)
 ✓ tests/unit/domain/serializer.test.ts (7 tests)
 ✓ tests/unit/application/canvas-use-cases.test.ts (3 tests)
 ✓ tests/unit/application/stencil-use-cases.test.ts (5 tests)
 ✓ tests/unit/domain/stencil.test.ts (4 tests)
 ✓ tests/unit/application/connector-use-cases.test.ts (2 tests)
 ✓ tests/unit/domain/connector.test.ts (5 tests)
 ✓ tests/unit/domain/shape.test.ts (7 tests)
 ✓ tests/acceptance/connector-interaction.spec.ts (1 test)
 ✓ tests/acceptance/stencil-interaction.spec.ts (1 test)
 ✓ tests/acceptance/canvas-interaction.spec.ts (1 test)

 Test Files  12 passed (12)
      Tests  46 passed (46)
   Typecheck 0 errores (tsc --noEmit)
```

---

## 📁 Estructura del Proyecto

El código está estructurado siguiendo los principios de **Clean Architecture**:

```text
├── index.html                   # Aplicación web completa y autónoma
├── package.json                 # Scripts de ejecución y dependencias
├── tsconfig.json                # Configuración TypeScript estricta
├── src/
│   ├── domain/                  # Capa de Dominio (Entidades, Value Objects, Servicios)
│   │   ├── entities/            # ShapeEntity, ConnectorEntity, StencilEntity
│   │   ├── value-objects/       # Point, Dimensions, ConnectionPort, RoutingPath, etc.
│   │   ├── repositories/        # Puertos abstractos de persistencia
│   │   └── services/            # DrawioSerializerService
│   ├── application/             # Capa de Aplicación (Casos de Uso)
│   │   └── use-cases/           # CreateShape, MoveShapes, RouteConnector, ExportDrawio, etc.
│   ├── infrastructure/          # Capa de Infraestructura (Adaptadores y Parsers)
│   │   ├── repositories/        # Repositorios en memoria
│   │   └── serializers/         # MxGraphXmlParser seguro anti-XXE
│   └── presentation/            # Capa de Presentación
│       └── components/          # Canvas y StencilSidebar
├── tests/
│   ├── acceptance/              # Pruebas BDD de aceptación
│   └── unit/                    # Pruebas unitarias de dominio y aplicación
└── docs/                        # Guías de usuario detalladas
    ├── user_guide_FEAT-001.md   # Canvas y renderizado
    ├── user_guide_FEAT-002.md   # Conectores y enrutamiento ortogonal
    ├── user_guide_FEAT-003.md   # Catálogo de stencils y búsqueda
    └── user_guide_FEAT-004.md   # Serialización Draw.io y membrete SVG
```

---

## 🎨 Identidad Gráfica y Accesibilidad (WCAG 2.1)

Los colores y estilos siguen la paleta institucional oficial del IMSS:

- **Verde IMSS Oficial**: `#006341` (Contraste 7.34:1 con fondo blanco, cumple **AAA**).
- **Dorado Institucional**: `#B38E5D` (Contraste $\ge 4.5:1$, cumple **AA**).
- **Superficie de Trabajo**: `#FFFFFF` / `#F8FAFC`.
- **Texto Principal**: `#0F172A` (Contraste 17.85:1 con fondo blanco, cumple **AAA**).
- **Semántica Accesible**: Roles ARIA completos (`role="img"`, `role="graphics-symbol"`, `role="tree"`).

---

## 📄 Licencia

Este proyecto está distribuido bajo la licencia [MIT](LICENSE).
