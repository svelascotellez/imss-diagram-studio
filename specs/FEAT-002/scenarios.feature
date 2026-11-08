# language: es
Caracteristica: Conectores Dinamicos, Puntos de Anclaje y Enrutamiento Ortogonal (FEAT-002)
  Como Arquitecto de Software o Ingeniero de la DIDT del IMSS
  Quiero conectar formas mediante puertos magneticos de anclaje y lineas ortogonales con flechas direccionales
  Para modelar flujos de interaccion, dependencias entre servicios y diagramas de arquitectura tecnica con recalculado dinamico

  @AC-2.1
  Escenario: Conexion exitosa entre dos formas con trayectoria ortogonal y marcadores
    Dado un canvas con dos formas geometricas "Servicio A" y "Servicio B"
    Cuando el usuario traza un conector desde el puerto "este" de "Servicio A" hacia el puerto "oeste" de "Servicio B"
    Entonces el conector es persistido en el modelo de dominio
    Y el conector traza segmentos ortogonales perpendiculares con flecha direccional en el extremo receptor

  @AC-2.2
  Esquema del escenario: Bloqueo de auto-bucles y conexiones sin puerto receptor valido
    Dado un canvas con una forma geometrica "Nodo Origen"
    Cuando el usuario intenta conectar el puerto "norte" hacia el destino "<destino_invalido>"
    Entonces el sistema descarta la operacion de conexion sin generar cambios en el repositorio
    Y el canvas no arroja excepciones de ejecucion

    Ejemplos:
      | destino_invalido  |
      | mismo_nodo        |
      | espacio_vacio     |
      | puerto_inexistente|

  @AC-2.3 @UI-UX
  Escenario: Recalculo automatico en tiempo real de trayectoria ortogonal al mover formas
    Dado un conector activo entre la forma "Modulo A" en (100, 100) y "Modulo B" en (400, 100)
    Cuando el usuario desplaza "Modulo B" a la coordenada (400, 300)
    Entonces los waypoints del conector se recalculan de forma reactiva manteniendo la conexion entre puertos
    Y los segmentos preservan angulos rectos de 90 grados

  @AC-2.4
  Escenario: Eliminacion en cascada de conectores asociados al eliminar un nodo
    Dado una forma "Gateway" que posee 2 conectores vinculados hacia otros nodos
    Cuando el usuario elimina la forma "Gateway" del canvas
    Entonces la forma es removida del repositorio
    Y los 2 conectores dependientes son eliminados en cascada del repositorio sin dejar referencias huerfanas
