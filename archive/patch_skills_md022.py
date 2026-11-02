with open('setup-sdd-project-v6.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update sdd-specify
sp_target = "'Genera `spec.md` (con `## 5. Allowed Files`) y `scenarios.feature` (con tags `@AC-x.x`) usando `.specify/templates/`.'"
sp_repl = """'Genera `spec.md` (con `## 5. Allowed Files`) y `scenarios.feature` (con tags `@AC-x.x`) usando `.specify/templates/`.',
    '',
    'REGLA DE FORMATO MARKDOWNLINT (MD022): Todo encabezado (#, ##, ###) en spec.md debe tener obligatoriamente una linea en blanco arriba y abajo. Nunca coloques texto contiguo a un encabezado.'"""

if sp_target in text:
    text = text.replace(sp_target, sp_repl, 1)
    print("1. Updated sdd-specify with MD022 rule.")
else:
    print("1. Target not found for sdd-specify.")

# 2. Update sdd-plan
plan_target = "'Genera `specs/<feature>/plan.md` definiendo Clean Architecture (incluyendo `src/presentation/` si aplica), seccion 2 de UI/UX Design System Specification y `## 4. Allowed Dependencies`.'"
plan_repl = """'Genera `specs/<feature>/plan.md` definiendo Clean Architecture (incluyendo `src/presentation/` si aplica), seccion 2 de UI/UX Design System Specification y `## 4. Allowed Dependencies`.',
    '',
    'REGLA DE FORMATO MARKDOWNLINT (MD022): En plan.md deja SIEMPRE una linea en blanco antes y despues de cada encabezado (#, ##, ###). Prohibido texto o tablas contiguas a encabezados.'"""

if plan_target in text:
    text = text.replace(plan_target, plan_repl, 1)
    print("2. Updated sdd-plan with MD022 rule.")
else:
    print("2. Target not found for sdd-plan.")

# 3. Update sdd-tasks
tasks_target = "'Genera `specs/<feature>/tasks.md` usando `.specify/templates/tasks.template.md`, asegurando incluir la tarea de redaccion de la Guia de Usuario en `docs/user_guide_<feature>.md`.'"
tasks_repl = """'Genera `specs/<feature>/tasks.md` usando `.specify/templates/tasks.template.md`, asegurando incluir la tarea de redaccion de la Guia de Usuario en `docs/user_guide_<feature>.md`.',
    '',
    'REGLA DE FORMATO MARKDOWNLINT (MD022): En tasks.md separa cada encabezado (#, ##, ###) con lineas en blanco arriba y abajo.'"""

if tasks_target in text:
    text = text.replace(tasks_target, tasks_repl, 1)
    print("3. Updated sdd-tasks with MD022 rule.")
else:
    print("3. Target not found for sdd-tasks.")

# 4. Update sdd-user-guide
ug_target = "'Toma la especificacion y escenarios BDD de `specs/<feature>/` y genera la Guia de Usuario en `docs/user_guide_<feature>.md` siguiendo `.specify/templates/user_guide.template.md`. Requisito innegociable para superar `spec-gate.ps1`.'"
ug_repl = """'Toma la especificacion y escenarios BDD de `specs/<feature>/` y genera la Guia de Usuario en `docs/user_guide_<feature>.md` siguiendo `.specify/templates/user_guide.template.md`. Requisito innegociable para superar `spec-gate.ps1`.',
    '',
    'REGLA DE FORMATO MARKDOWNLINT (MD022): La Guia de Usuario debe cumplir al 100% la regla MD022: exactamente una linea en blanco antes y despues de cada encabezado (#, ##, ###). Prohibido colocar tablas, listas o parrafos inmediatamente contiguos a un titulo.'"""

if ug_target in text:
    text = text.replace(ug_target, ug_repl, 1)
    print("4. Updated sdd-user-guide with MD022 rule.")
else:
    print("4. Target not found for sdd-user-guide.")

with open('setup-sdd-project-v6.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Skills updated in setup-sdd-project-v6.py.")
