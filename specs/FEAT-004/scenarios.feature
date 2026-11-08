# language: es
Caracteristica: Serializacion XML (Compatible con Draw.io) y Exportacion SVG/PNG (FEAT-004)
  Como Arquitecto de Software o Lider Tecnico de la DIDT del IMSS
  Quiero importar y exportar diagramas en formato estandar XML de Draw.io y generar descargas vectoriales SVG con membrete institucional
  Para garantizar interoperabilidad total, soberania tecnica y emitir diagramas listos para auditorias

  @AC-4.1
  Escenario: Exportacion exitosa de canvas a XML compatible con Draw.io
    Dado un canvas con dos formas y un conector activo entre ellas
    Cuando el usuario solicita exportar el diagrama a formato Draw.io XML
    Entonces el sistema genera una cadena XML valida con la etiqueta raiz "<mxGraphModel>"
    Y el XML contiene las definiciones "mxCell" correspondientes a los nodos y al enlace conectivo con sus coordenadas

  @AC-4.2
  Escenario: Deserializacion e importacion exitosa de archivo Draw.io XML hacia el canvas
    Dado un archivo XML valido bajo el esquema "<mxGraphModel>" que contiene 3 formas y 2 conectores
    Cuando el usuario importa el documento XML al sistema
    Entonces el canvas es poblado fielmente con las 3 formas en sus posiciones exactas
    Y los 2 conectores son reconstruidos con sus extremos enlazados a las formas respectivas en menos de 100 ms

  @AC-4.3 @UI-UX
  Escenario: Exportacion vectorial a SVG con membrete oficial DIDT IMSS
    Dado un diagrama con componentes arquitectonicos en el canvas
    Cuando el usuario exporta el diagrama en formato SVG vectorial
    Entonces el documento SVG resultante incluye el membrete "DIRECCION DE INNOVACION Y DESARROLLO TECNOLOGICO — IMSS"
    Y el documento incorpora metadatos accesibles WCAG 2.1 AA y fecha de emision

  @AC-4.4
  Esquema del escenario: Bloqueo de XML malformado y proteccion anti-XXE
    Dado un intento de importacion con un payload "<tipo_payload>"
    Cuando el usuario intenta cargar el contenido corrupto
    Entonces el sistema rechaza la carga notificando un error de sintaxis segura
    Y el canvas mantiene su estado previo sin alteraciones

    Ejemplos:
      | tipo_payload         |
      | xml_incompleto       |
      | entidad_externa_xxe  |
      | no_es_mxgraph        |
