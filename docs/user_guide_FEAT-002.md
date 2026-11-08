# Guía de Usuario: FEAT-002 - Conectores Dinamicos, Puntos de Anclaje y Enrutamiento Ortogonal

## 1. Proposito y Descripcion General

El módulo **FEAT-002** proporciona las capacidades de enlace relacional y modelado de flujos técnicos entre componentes arquitectónicos en la herramienta de diagramación de la **DIDT del IMSS**. Permite conectar formas geométricas mediante puertos magnéticos ubicados en los puntos cardinales (Norte, Sur, Este y Oeste), aplicando automáticamente un algoritmo de enrutamiento ortogonal (ángulos rectos de 90°) y flechas direccionales.

## 2. Requisitos Previos y Configuracion

- Tener implementado el motor base de formas vectoriales (`FEAT-001`).
- Disponer de al menos dos formas geométricas instanciadas en el canvas institucional.

## 3. Flujos de Trabajo Paso a Paso

### 3.1. Trazado y Enlace de Conectores (`AC-2.1`)

1. Sitúe el cursor sobre cualquiera de las formas existentes en el canvas para visualizar sus 4 puertos magnéticos de anclaje (círculos dorados `#B38E5D`).
2. Haga clic sobre el puerto de origen deseado (por ejemplo, el puerto Este de un microservicio) y arrastre el cursor hacia el puerto receptor de la forma destino.
3. Al aproximarse al puerto destino, el sistema aplicará atracción magnética y trazará la trayectoria ortogonal con una flecha institucional Verde IMSS (`#006341`).
4. Suelte el cursor para consolidar la conexión en el modelo de dominio.

### 3.2. Bloqueo de Conexiones Invalidas (`AC-2.2`)

1. Si intenta conectar un puerto hacia la misma forma (auto-bucle), el sistema rechazará la operación.
2. Si suelta el conector en un espacio vacío sin un puerto receptor válido, el conector provisional se descartará inmediatamente sin alterar el canvas.

### 3.3. Recalculo Dinamico al Mover Formas (`AC-2.3`)

1. Seleccione y desplace cualquiera de los nodos conectados mediante el ratón o las teclas de flecha.
2. La ruta ortogonal del conector se recalculará automáticamente en tiempo real (< 10 ms), adaptando los quiebres a 90 grados y manteniendo anclados los extremos a los puertos cardinales correspondientes.

### 3.4. Eliminacion en Cascada (`AC-2.4`)

1. Al seleccionar una forma geométrica y presionar la tecla <kbd>Supr</kbd> o invocar el comando de borrado, el sistema eliminará la forma y purgará en cascada todos los conectores vinculados a ella, evitando líneas huérfanas en el diagrama.

## 4. Preguntas Frecuentes y Solucion de Problemas

- **¿Puedo cambiar la etiqueta o texto descriptivo de un conector?**
  Sí, cada conector admite una etiqueta textual centrada a lo largo del segmento principal.
- **¿Qué ocurre si muevo una forma a una distancia lejana?**
  El algoritmo ortogonal recalcula el punto medio de quiebre (*waypoint*) de forma determinista para garantizar que los segmentos sigan siendo paralelos a los ejes X e Y.

## 5. Accesibilidad y Atajos de Teclado (WCAG 2.1 AA)

| Elemento / Accion | Comportamiento Accesible |
| :--- | :--- |
| `role="graphics-connector"` | Identificación semántica del enlace para tecnologías de asistencia |
| `aria-label` | Lectura de origen, destino y etiqueta descriptiva del conector |
| Foco por Teclado | Posibilidad de seleccionar un conector mediante navegación secuencial |
| Contraste Visual | Línea de conector con ratio superior a 4.5:1 sobre el fondo del canvas |
