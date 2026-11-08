# Especificacion Funcional: FEAT-002 - Conectores Dinamicos, Puntos de Anclaje y Enrutamiento Ortogonal

## 1. Contexto e Historia de Usuario

Como Arquitecto de Software o Ingeniero de la DIDT del IMSS
Quiero conectar formas mediante puertos magneticos de anclaje (norte, sur, este, oeste) y lineas de conexion ortogonales con flechas direccionales
Para modelar flujos de interaccion, dependencias entre servicios y diagramas de arquitectura tecnica con recalculado dinamico automatico al desplazar elementos.

## 2. Criterios de Aceptacion (Sintaxis EARS)

- **AC-2.1**: CUANDO el usuario arrastra desde un puerto de conexion de una forma origen hacia un puerto valido de una forma destino, EL SISTEMA DEBE instanciar un conector persistente con direccion origen-destino y trazar la trayectoria ortogonal con marcadores de flecha en el extremo receptor.
- **AC-2.2**: CUANDO el usuario intenta conectar un puerto hacia si mismo (auto-bucle no admitido) o soltar la conexion en el canvas sin un puerto destino valido, EL SISTEMA DEBE cancelar la operacion, descartar el conector provisional y mantener el estado previo sin errores.
- **AC-2.3**: MIENTRAS cualquiera de las formas conectadas (origen o destino) sea desplazada o redimensionada en el canvas, EL SISTEMA DEBE recalcular automaticamente en tiempo real las coordenadas de los puertos de anclaje y los segmentos ortogonales de la trayectoria.
- **AC-2.4**: SI una forma geometrica vinculada a uno o mas conectores es eliminada del canvas, EL SISTEMA DEBE eliminar en cascada todos los conectores asociados para prevenir referencias huerfanas en el estado del dominio.

## 3. Comportamientos Fuera de Alcance (Out of Scope)

- No se incluye la barra de stencils especializados de arquitectura de microservicios ni bases de datos de la DIDT (corresponde a FEAT-003).
- No se incluye persistencia remota ni exportacion a XML Draw.io / SVG (corresponde a FEAT-004).
- No se incluye enrutamiento con evasion de colisiones de obstaculos complejos o saltos de puente de linea (planificado para iteraciones posteriores).

## 4. Requisitos No Funcionales, UI/UX y Accesibilidad

- Recalculo de trayectoria y renderizado de conectores en menos de 10 ms por actualizacion para mantener 60 FPS.
- Grosor y contraste visual de lineas alineado con WCAG 2.1 AA (borde de conector >= 3:1 respecto al fondo del canvas).
- Los puertos de anclaje deben presentar feedback visual interactivo: color de acento `#B38E5D` al situar el cursor (hover) y verde `#006341` al conectar exitosamente.
- Atributos accesibles ARIA (`role="graphics-connector"`, `aria-label="Conexion desde {origen} hacia {destino}"`).

## 5. Allowed Files

Rutas exactas autorizadas para creacion o modificacion durante esta funcionalidad:

- `src/domain/entities/connector.entity.ts`
- `src/domain/value-objects/connection-port.vo.ts`
- `src/domain/value-objects/routing-path.vo.ts`
- `src/domain/repositories/connector-state.repository.ts`
- `src/application/use-cases/create-connector.use-case.ts`
- `src/application/use-cases/route-connector.use-case.ts`
- `src/application/use-cases/delete-shape-cascade.use-case.ts`
- `src/presentation/components/Canvas.ts`
- `tests/unit/domain/connector.test.ts`
- `tests/unit/application/connector-use-cases.test.ts`
- `tests/acceptance/connector-interaction.spec.ts`
