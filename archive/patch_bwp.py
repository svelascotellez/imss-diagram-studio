with open('build_white_paper_v65.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace trailing spaces with <br>
text = text.replace(
    "> **Autor:** Salvador Velasco & Antigravity (Google DeepMind Team)  \n"
    "> **Versión Oficial:** 6.5  \n"
    "> **Fecha de Publicación:** 30 de Octubre de 2026  \n"
    "> **Clasificación:** Estándar Metodológico Corporativo y de Ingeniería de Software  \n"
    "> **Estado:** Aprobado para Producción y Auditorías Regulatorias Internacionales",
    "> **Autor:** Salvador Velasco & Antigravity (Google DeepMind Team)<br>\n"
    "> **Versión Oficial:** 6.5<br>\n"
    "> **Fecha de Publicación:** 30 de Octubre de 2026<br>\n"
    "> **Clasificación:** Estándar Metodológico Corporativo y de Ingeniería de Software<br>\n"
    "> **Estado:** Aprobado para Producción y Auditorías Regulatorias Internacionales"
)

# Ensure single trailing newline
text = text.replace(
    'content_full = "\\n".join(sections) + "\\n"',
    'content_full = "\\n".join(sections).strip() + "\\n"'
)

with open('build_white_paper_v65.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated build_white_paper_v65.py")
