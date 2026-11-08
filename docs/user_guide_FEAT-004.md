# Guia de Usuario: FEAT-004 - Serializacion XML Draw.io e Interoperabilidad Institucional

## 1. Proposito y Descripcion General

El modulo **FEAT-004** proporciona capacidades de serializacion bidireccional entre la solucion soberana de diagramacion de la **DIDT del IMSS** y el estandar industrial XML de Draw.io (`app.diagrams.net`). Adicionalmente, permite generar exportaciones vectoriales SVG oficiales de alta definicion que incorporan de forma automatica el membrete institucional, metadatos de auditoria y cumplimiento WCAG 2.1 AA.

## 2. Requisitos Previos y Configuracion

- Disponer del canvas interactivo institucional activo con formas o conectores (`FEAT-001`, `FEAT-002`).
- Para importar diagramas, contar con un archivo en formato `.drawio` o `.xml` valido generado por Draw.io o por este estudio.
- El sistema opera de manera 100% soberana y local en el navegador del operador, sin enviar informacion a servidores externos de terceros.

## 3. Flujos de Trabajo Paso a Paso

### 3.1. Exportacion de Diagramas a XML Estandar Draw.io (`AC-4.1`)

1. Diseñe o cargue el diagrama de arquitectura tecnica en el canvas.
2. Haga clic en el boton **"Exportar Draw.io XML"** ubicado en la barra de herramientas superior.
3. El sistema serializara en menos de 50 ms todas las formas, estilos institucionales y conectores ortogonales bajo el esquema `<mxGraphModel>`.
4. Se descargara un archivo con extension `.drawio.xml` totalmente compatible para ser abierto, editado o respaldado en `app.diagrams.net` o en instancias locales de Draw.io.

### 3.2. Importacion y Reconstruccion de Diagramas Draw.io (`AC-4.2`)

1. Haga clic en el boton **"Importar Draw.io XML"** en la barra superior.
2. Seleccione un archivo XML o `.drawio` desde su equipo local.
3. El motor deserializara la jerarquia de celdas `<mxCell>`, mapeara los vertices a formas del canvas y reconstruira los enlaces y puertos ortogonales en menos de 100 ms.
4. El canvas se actualizara reflejando el modelo visual completo.

### 3.3. Exportacion Grafica Vectorial SVG con Membrete Oficial DIDT (`AC-4.3`)

1. Con el diagrama preparado, haga clic en el boton **"Descargar SVG Membretado"**.
2. El sistema ensamblara un documento vectorial independiente que incorpora:
   - **Encabezado Institucional**: Franja Verde IMSS (`#006341`) y cintillo Dorado (`#B38E5D`) con el texto "DIRECCION DE INNOVACION Y DESARROLLO TECNOLOGICO — IMSS".
   - **Metadatos de Emision**: Titulo del diagrama, fecha de generacion UTC y autor institucional.
   - **Pie de Pagina**: Declaratoria de confidencialidad institucional y sello de gobernanza SDD v6.6.
   - **Accesibilidad Semantica**: Atributos `role="img"` y descripcion accesible `aria-label`.
3. El archivo SVG descargado puede ser incrustado directamente en reportes tecnicos ejecutivos, dictamenes tecnicos o auditorias del OIC.

### 3.4. Proteccion de Seguridad y Sanitizacion Anti-XXE (`AC-4.4`)

1. Ante cualquier intento deliberado o accidental de cargar un archivo XML con entidades externas DTD/XXE (`<!DOCTYPE`, `SYSTEM`, `PUBLIC`), el sistema bloqueara la operacion de manera fail-closed.
2. Se presentara una notificacion de advertencia de seguridad al operador.
3. El estado actual del canvas se mantendra inalterado sin perdida de informacion.

## 4. Preguntas Frecuentes y Solucion de Problemas

- **¿Puedo abrir los archivos exportados directamente en app.diagrams.net?**
  Si. La estructura generada respeta fielmente la definicion estandar de `<mxGraphModel>`, permitiendo importar el archivo en draw.io sin perdida de geometria.
- **¿Que ocurre si importo un XML con nodos sin posicion?**
  El parser seguro asigna automaticamente coordenadas por defecto y dimensiones minimas conformes al estandar institucional ($\ge 20\times 20$ px).

## 5. Accesibilidad y Atributos Tecnicos (WCAG 2.1 AA)

| Elemento / Accion | Caracteristica de Cumplimiento |
| :--- | :--- |
| `role="img"` | Define al SVG como recurso grafico semantico para lectores de pantalla |
| `aria-label` | Describe el proposito del diagrama para tecnologias de asistencia |
| Contraste de Membrete | Texto `#FFFFFF` sobre Verde IMSS `#006341` con ratio 7.34:1 (Cumple AAA) |
| Cintillo Institucional | Acento Dorado `#B38E5D` con ratio de visibilidad superior a 4.5:1 |
