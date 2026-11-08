# Guía de Contribución al Framework SDD

Agradecemos el interés en colaborar con el framework **Specification-Driven Development (SDD)**. Como estándar de ingeniería con orientación a entornos de alta regulación, cualquier aportación debe cumplir rigurosos criterios de calidad, arquitectura y gobernanza.

---

## 1. Principios de Contribución

1. **Determinismo y Contención:** Ninguna modificación debe debilitar las compuertas de auditoría (`spec-gate.ps1`) ni flexibilizar el candado HMAC-SHA256.
2. **Paridad Políglota:** Cualquier mejora introducida en el generador de PowerShell (`setup-sdd-project-v66.ps1`) debe reflejarse fielmente en el generador Python (`setup-sdd-project-v66.py`).
3. **Cero Violaciones de Markdownlint:** Toda documentación técnica debe superar el script `lint_md.py` sin errores ni excepciones.
4. **Validación Formal con Pester 6:** Ningún Pull Request será aceptado sin pruebas de regresión en `tests/v66-governance.Tests.ps1`.

---

## 2. Flujo de Trabajo Recomendado

1. **Crear un Fork** del repositorio en GitHub: `https://github.com/svelascotellez/ssd-projects`.
2. **Crear una rama temática** para tu trabajo:
   ```bash
   git checkout -b feature/nueva-mejora
   ```
3. **Realizar los cambios** siguiendo la arquitectura limpia y estándares del proyecto.
4. **Ejecutar las validaciones locales:**
   ```powershell
   # 1. Validar Markdown
   python lint_md.py

   # 2. Ejecutar suite de pruebas de gobernanza en Pester
   Invoke-Pester -Path .\tests\v66-governance.Tests.ps1 -Output Detailed
   ```
5. **Crear un Pull Request** hacia la rama `main` del repositorio original, completando la plantilla requerida.

---

## 3. Estándares de Commits (Conventional Commits)

Utilizamos el estándar [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` Nuevas funcionalidades, compuertas o habilidades agénticas.
- `fix:` Corrección de fallos en hooks, scripts de arnés o cálculo de hashes.
- `docs:` Actualizaciones en el Libro Blanco, Guías de Setup o diagramas.
- `test:` Nuevas pruebas automatizadas en Pester o scripts de verificación.
- `refactor:` Mejoras internas sin alteración de comportamiento observable.
- `chore:` Tareas rutinarias de mantenimiento de repositorio o archivado.

---

## 4. Código de Conducta

Nos comprometemos a mantener un entorno inclusivo, respetuoso y profesional para todos los colaboradores, libre de acoso o discriminación de cualquier índole.

