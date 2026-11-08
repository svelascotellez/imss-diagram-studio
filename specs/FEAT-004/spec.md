# Especificacion Funcional: FEAT-004 - Serializacion XML (Compatible con Draw.io) y Exportacion SVG/PNG

## 1. Contexto e Historia de Usuario

Como Arquitecto de Software o Lider Tecnico de la DIDT del IMSS
Quiero importar y exportar diagramas en formato estandar XML de Draw.io (app.diagrams.net) y generar descargas vectoriales SVG con membrete institucional
Para garantizar interoperabilidad total con herramientas de la industria, asegurar la soberania de los datos tecnicos del Seguro Social y emitir diagramas listos para auditorias tecnicas.

## 2. Criterios de Aceptacion (Sintaxis EARS)

- **AC-4.1**: CUANDO el usuario solicita exportar el diagrama activo a formato Draw.io, EL SISTEMA DEBE serializar todas las formas y conectores en un documento XML valido bajo el esquema estandar `<mxGraphModel>` con coordenadas relativas y etiquetas compatibles para su apertura directa en app.diagrams.net.
- **AC-4.2**: CUANDO el usuario importa un archivo XML valido con estructura `<mxGraphModel>`, EL SISTEMA DEBE deserializar las celdas, instanciar las entidades correspondientes en el canvas y restablecer las conexiones ortogonales en menos de 100 ms.
- **AC-4.3**: MIENTRAS el usuario solicita la exportacion grafica a formato SVG vectorial, EL SISTEMA DEBE generar el archivo descargable incorporando el membrete oficial institucional "DIRECCION DE INNOVACION Y DESARROLLO TECNOLOGICO — IMSS", fecha de emision y metadatos accesibles conforme a WCAG 2.1 AA.
- **AC-4.4**: SI el usuario intenta importar un archivo XML malformado, con sintaxis corrupta o con declaraciones de entidades externas DTD/XXE no autorizadas, EL SISTEMA DEBE bloquear de forma segura la carga, notificar el error de sintaxis y preservar inalterado el diagrama actual.

## 3. Comportamientos Fuera de Alcance (Out of Scope)

- No se incluye integracion directa con APIs de Google Drive / Microsoft OneDrive en la nube (la herramienta opera en almacenamiento local/soberano).
- No se incluye conversion de formatos privativos binarios `.vsdx` de Microsoft Visio.
- No se incluye encriptacion de payloads de exportacion (la seguridad se garantiza mediante controles perimetrales de la DIDT).

## 4. Requisitos No Funcionales, UI/UX y Accesibilidad

- Tiempo de serializacion y deserializacion XML menor a 100 ms para diagramas con hasta 200 elementos.
- Sanitizacion estricta contra inyecciones de entidades XML externas (OWASP XXE Prevention).
- Documento SVG exportado con roles semanticos ARIA (`role="img"`, `aria-label="Diagrama de Arquitectura DIDT IMSS"`).
- Membrete institucional con contraste minimo WCAG 2.1 AA (Verde IMSS `#006341` y fondo `#FFFFFF`, ratio 7.34:1).

## 5. Allowed Files

Rutas exactas autorizadas para creacion o modificacion durante esta funcionalidad:

- `src/domain/services/drawio-serializer.service.ts`
- `src/domain/value-objects/diagram-export.vo.ts`
- `src/application/use-cases/export-drawio-xml.use-case.ts`
- `src/application/use-cases/import-drawio-xml.use-case.ts`
- `src/application/use-cases/export-svg-diagram.use-case.ts`
- `src/infrastructure/serializers/mxgraph-xml-parser.ts`
- `src/presentation/components/Canvas.ts`
- `tests/unit/domain/serializer.test.ts`
- `tests/unit/application/serialization-use-cases.test.ts`
- `tests/acceptance/serialization-interaction.spec.ts`
