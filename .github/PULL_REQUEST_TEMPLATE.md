## Descripción del Cambio

<!-- Describe de forma concisa qué problema resuelve este Pull Request o qué funcionalidad incorpora. -->

## Tipo de Cambio

- [ ] `fix`: Corrección de un fallo en el arnés, compuertas o hooks.
- [ ] `feat`: Nueva funcionalidad, pilar o capacidad agéntica.
- [ ] `docs`: Modificación o enriquecimiento de documentación técnica.
- [ ] `test`: Ampliación de la suite de pruebas de gobernanza (Pester/unitarias).
- [ ] `refactor`: Refactorización de código sin cambio de comportamiento observable.

## Lista de Verificación de Gobernanza SDD

- [ ] Los cambios en `setup-sdd-project-v66.ps1` tienen su paridad exacta en `setup-sdd-project-v66.py`.
- [ ] Se ejecutó `python lint_md.py` con **0 violaciones de markdownlint**.
- [ ] Se ejecutó `tests/v66-governance.Tests.ps1` pasando el 100% de las pruebas en Pester 6.
- [ ] El candado criptográfico HMAC-SHA256 y la política HITL no han sido debilitados ni omitidos.
- [ ] No se incluyen secretos, tokens ni contraseñas en texto plano.
- [ ] Se actualizó la documentación relevante (Libro Blanco, Guía de Setup o README) si aplica.

