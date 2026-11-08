# Guía de Usuario: FEAT-001 - Canvas Interactivo y Motor de Renderizado

## 1. Proposito y Descripcion General

El módulo **FEAT-001** proporciona la infraestructura base de diagramación técnica soberana para los equipos de arquitectura y desarrollo de la **DIDT del IMSS**. Permite crear, visualizar, redimensionar, seleccionar y desplazar formas geométricas vectoriales en un canvas interactivo de alto rendimiento, asegurando una experiencia visual alineada con la identidad gráfica institucional y los estándares de accesibilidad internacional.

## 2. Requisitos Previos y Configuracion

- Navegador web moderno compatible con SVG y estándares ECMAScript 2022+ (Google Chrome, Microsoft Edge, Mozilla Firefox o Safari).
- El proyecto debe tener configurado el arquetipo `IMSS Institucional DIDT` definido en `.specify/design-system/design-tokens.json`.
- Resolución mínima de pantalla recomendada: 1280x720 px con soporte para puntero o teclado.

## 3. Flujos de Trabajo Paso a Paso

### 3.1. Creacion de Formas en el Canvas (`AC-1.1`)

1. Seleccione la herramienta o tipo de forma deseada (Rectángulo, Elipse, Rombo, Contenedor o Texto).
2. Haga clic en el lienzo o arrastre para posicionar el nodo.
3. El sistema instanciará la forma inmediatamente aplicando el color institucional Verde IMSS (`#006341`), fondo blanco y tipografía legible `Inter`.

### 3.2. Redimensionamiento y Proteccion de Limites (`AC-1.2`)

1. Al seleccionar una forma, se activarán los manejadores en las esquinas y bordes.
2. Arrastre cualquier manejador para ajustar el ancho y alto.
3. Si intenta reducir la forma por debajo de **20x20 píxeles**, el sistema acotará automáticamente las dimensiones al umbral mínimo, evitando la pérdida de visibilidad de etiquetas y contenido técnico.

### 3.3. Seleccion Multiple por Area y Atributos Accesibles (`AC-1.3`)

1. Haga clic en un área vacía del canvas y arrastre el cursor para trazar un recuadro de selección.
2. Todas las formas intersecadas por el recuadro quedarán seleccionadas en tiempo real.
3. Cada forma seleccionada actualizará su atributo accesible `aria-selected="true"`.
4. El sistema trazará un bounding box unificado enmarcado con el acento dorado institucional (`#B38E5D`).

### 3.4. Desplazamiento Sincronizado y Atomico (`AC-1.4`)

1. Con una o más formas seleccionadas, arrastre cualquiera de ellas con el ratón o utilice las teclas de flecha (<kbd>&larr;</kbd>, <kbd>&rarr;</kbd>, <kbd>&uarr;</kbd>, <kbd>&darr;</kbd>).
2. Todos los nodos seleccionados se moverán en sincronía manteniendo exactamente la distancia relativa original entre ellos.

## 4. Preguntas Frecuentes y Solucion de Problemas

- **¿Qué ocurre si muevo una forma fuera del área visible?**
  Las coordenadas cartesianas están protegidas para no admitir valores negativos inválidos (`x >= 0`, `y >= 0`).
- **¿Cómo deselecciono todos los elementos?**
  Haga clic en cualquier espacio vacío del canvas o presione la tecla <kbd>Escape</kbd>.

## 5. Accesibilidad y Atajos de Teclado (WCAG 2.1 AA)

| Tecla / Combinación | Acción Ejecutada |
| :--- | :--- |
| <kbd>Tab</kbd> / <kbd>Shift</kbd>+<kbd>Tab</kbd> | Navegar secuencialmente entre las formas del canvas |
| <kbd>Flechas</kbd> (<kbd>&larr;</kbd>, <kbd>&rarr;</kbd>, <kbd>&uarr;</kbd>, <kbd>&darr;</kbd>) | Desplazar las formas seleccionadas en pasos de 5 px |
| <kbd>Shift</kbd> + Clic | Agregar o quitar una forma individual a la selección múltiple |
| <kbd>Escape</kbd> | Limpiar la selección activa |
| <kbd>Supr</kbd> / <kbd>Backspace</kbd> | Eliminar las formas seleccionadas |
