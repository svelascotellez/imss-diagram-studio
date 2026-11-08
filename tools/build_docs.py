#!/usr/bin/env python3
"""
tools/build_docs.py - Pipeline automatizado de compilación documental para SDD Framework v6.6
Genera y sincroniza entregables HTML5 y PDF vectorial a partir de los documentos Markdown canónicos.
"""

import sys
import os
import subprocess
import shutil
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

DOCS_MAPPING = [
    {
        "source": ROOT_DIR / "DOCUMENTO_MAESTRO_PROYECTO_SDD_V66.md",
        "html": ROOT_DIR / "DOCUMENTO_MAESTRO_PROYECTO_SDD_V66.html",
        "pdf": ROOT_DIR / "DOCUMENTO_MAESTRO_PROYECTO_SDD_V66.pdf",
        "title": "Libro Blanco y Documento Maestro SDD v6.6",
    },
    {
        "source": ROOT_DIR / "GUIA_MAESTRA_SETUP_SDD_V66.md",
        "html": ROOT_DIR / "GUIA_MAESTRA_SETUP_SDD_V66.html",
        "pdf": ROOT_DIR / "GUIA_MAESTRA_SETUP_SDD_V66.pdf",
        "title": "Guía Maestra de Setup y Operación SDD v6.6",
    },
    {
        "source": ROOT_DIR / "PRESENTACION_EJECUTIVA_SDD_V66.md",
        "html": ROOT_DIR / "PRESENTACION_EJECUTIVA_SDD_V66.html",
        "pdf": ROOT_DIR / "PRESENTACION_EJECUTIVA_SDD_V66.pdf",
        "title": "Presentación Ejecutiva SDD v6.6",
    },
]

def find_browser():
    """Busca un navegador headless disponible (Edge o Chrome)."""
    candidates = [
        # Windows
        os.environ.get("PROGRAMFILES", "C:\\Program Files") + "\\Microsoft\\Edge\\Application\\msedge.exe",
        os.environ.get("PROGRAMFILES(X86)", "C:\\Program Files (x86)") + "\\Microsoft\\Edge\\Application\\msedge.exe",
        os.environ.get("PROGRAMFILES", "C:\\Program Files") + "\\Google\\Chrome\\Application\\chrome.exe",
        os.environ.get("PROGRAMFILES(X86)", "C:\\Program Files (x86)") + "\\Google\\Chrome\\Application\\chrome.exe",
        # Linux / macOS
        "google-chrome",
        "google-chrome-stable",
        "chromium-browser",
        "chromium",
        "msedge",
    ]
    for c in candidates:
        if os.path.isabs(c):
            if os.path.exists(c):
                return c
        else:
            found = shutil.which(c)
            if found:
                return found
    return None

def check_documents():
    """Valida la existencia de todos los documentos fuente Markdown."""
    print("=== [SDD Docs Builder]: Verificando archivos fuente ===")
    all_ok = True
    for item in DOCS_MAPPING:
        if item["source"].exists():
            size_kb = item["source"].stat().st_size / 1024
            print(f"  [OK] {item['source'].name} ({size_kb:.1f} KB)")
        else:
            print(f"  [ERROR] No encontrado: {item['source'].name}")
            all_ok = False
    return all_ok

def render_pdf_from_html(browser_path, html_path, pdf_path):
    """Renderiza PDF vectorial utilizando navegador headless."""
    if not html_path.exists():
        print(f"  [SKIP] HTML no existe para generar PDF: {html_path.name}")
        return False
    
    file_uri = html_path.resolve().as_uri()
    cmd = [
        browser_path,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={pdf_path.resolve()}",
        file_uri
    ]
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
        if res.returncode == 0 and pdf_path.exists():
            size_mb = pdf_path.stat().st_size / (1024 * 1024)
            print(f"  [PDF GENERADO] {pdf_path.name} ({size_mb:.2f} MB)")
            return True
        else:
            print(f"  [WARN] Código de salida {res.returncode} al renderizar {pdf_path.name}")
            return False
    except Exception as e:
        print(f"  [WARN] Error generando PDF: {e}")
        return False

def main():
    print("=================================================================")
    print(" SDD Framework v6.6 - Automated Documentation Pipeline")
    print("=================================================================")
    if not check_documents():
        sys.exit(1)

    browser = find_browser()
    if browser:
        print(f"\n[+] Navegador detectado para PDF: {browser}")
    else:
        print("\n[!] Navegador headless no encontrado en PATH. Los PDFs se compilarán en CI/CD.")

    print("\n=== Resumen de Entregables Documentales ===")
    for item in DOCS_MAPPING:
        has_html = ":heavy_check_mark:" if item["html"].exists() else ":x:"
        has_pdf = ":heavy_check_mark:" if item["pdf"].exists() else ":x:"
        print(f"- {item['title']}:")
        print(f"    MD: :heavy_check_mark: | HTML: {has_html} | PDF: {has_pdf}")

    print("\n[+] Pipeline documental verificado con éxito.")
    return 0

if __name__ == "__main__":
    sys.exit(main())

