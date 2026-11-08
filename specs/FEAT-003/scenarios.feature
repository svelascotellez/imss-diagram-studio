# language: es
Caracteristica: Catalogo de Stencils Arquitectonicos DIDT y Procesos IMSS (FEAT-003)
  Como Arquitecto de Software, Desarrollador o Diseñador de Procesos de la DIDT del IMSS
  Quiero disponer de un panel lateral con catalogo estructurado de stencils arquitectonicos y actores de procesos
  Para acelerar la diagramacion tecnica reutilizando componentes estandarizados oficiales del IMSS

  @AC-3.1
  Escenario: Instanciacion exitosa de un stencil arquitectonico hacia el canvas
    Dado un catalogo inicializado con la coleccion oficial de stencils de la DIDT
    Cuando el usuario solicita instanciar el stencil con id "stencil-api-gateway" en las coordenadas (200, 150)
    Entonces se crea una entidad de forma en el canvas con tipo "rectangle" y etiqueta "API Gateway DIDT"
    Y la forma incorpora dimensiones optimas 160x70 px y estilo institucional IMSS

  @AC-3.2
  Esquema del escenario: Filtrado y busqueda reactiva de stencils
    Dado un catalogo con stencils de diversas categorias
    Cuando el usuario busca el termino "<termino_busqueda>"
    Entonces el resultado contiene exactamente los stencils que coinciden con "<resultado_esperado>"
    Y el tiempo de filtrado es menor a 50 milisegundos

    Ejemplos:
      | termino_busqueda | resultado_esperado       |
      | Kafka            | Bus de Eventos Kafka     |
      | PostgreSQL       | Base de Datos PostgreSQL |
      | Farmacia         | Despachador de Farmacia  |

  @AC-3.3 @UI-UX
  Escenario: Categorizacion y accesibilidad ARIA en el arbol de stencils
    Dado el panel lateral de stencils con categorias "Arquitectura de Software" y "Procesos IMSS"
    Cuando el usuario colapsa o expande una categoria
    Entonces el contenedor actualiza el atributo "aria-expanded" de forma reactiva
    Y los elementos mantienen foco accesible por teclado con contraste superior a 4.5:1

  @AC-3.4
  Escenario: Fallback seguro ante solicitud de stencil desconocido
    Dado un catalogo oficial de stencils
    Cuando el usuario solicita instanciar un identificador inexistente "stencil-fantasma-999" en (100, 100)
    Entonces el sistema recurre al fallback seguro creando una forma estandar "Servicio Institucional"
    Y la aplicacion no arroja excepciones fatales
