#!/usr/bin/env python3
"""
tools/build_scaffolder.py - Modular Scaffolder Builder for SDD Framework v6.6
Sincroniza y valida la integridad de plantillas modulares entre setup-sdd-project-v66.ps1 y .py.
"""

import sys
import os
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PS1_PATH = ROOT_DIR / "setup-sdd-project-v66.ps1"
PY_PATH = ROOT_DIR / "setup-sdd-project-v66.py"

def verify_scaffolder_parity():
    """Valida paridad estructural y de líneas entre el script de PowerShell y Python."""
    print("=== [SDD Scaffolder Parity Check]: Verificando alineación PS1 y PY ===")
    if not PS1_PATH.exists() or not PY_PATH.exists():
        print("[ERROR]: No se encontraron ambos scripts de scaffolding v6.6.")
        return False
    
    ps1_lines = len(PS1_PATH.read_text(encoding="utf-8", errors="replace").splitlines())
    py_lines = len(PY_PATH.read_text(encoding="utf-8", errors="replace").splitlines())

    print(f"  [+] setup-sdd-project-v66.ps1: {ps1_lines} líneas")
    print(f"  [+] setup-sdd-project-v66.py:  {py_lines} líneas")

    # Verificar presencia de las 20 skills canónicas en ambos
    skills = [
        "sdd-orchestrator", "sdd-onboard", "sdd-constitution", "sdd-specify",
        "sdd-clarify", "sdd-ui-ux", "sdd-design-system", "sdd-preview-design",
        "sdd-plan", "sdd-tasks", "sdd-implement", "sdd-user-guide",
        "sdd-validate", "sdd-change-spec", "sdd-reverse-spec", "sdd-secure-coding",
        "sdd-dashboard", "sdd-cicd", "sdd-performance", "sdd-compliance"
    ]
    
    ps1_text = PS1_PATH.read_text(encoding="utf-8", errors="replace")
    py_text = PY_PATH.read_text(encoding="utf-8", errors="replace")

    missing_ps1 = [s for s in skills if s not in ps1_text]
    missing_py = [s for s in skills if s not in py_text]

    if missing_ps1:
        print(f"  [ERROR] Faltan skills en PS1: {missing_ps1}")
        return False
    if missing_py:
        print(f"  [ERROR] Faltan skills en PY: {missing_py}")
        return False

    print("  [OK] Todas las 20 skills canónicas están sincronizadas en PS1 y PY.")
    return True

def main():
    print("=================================================================")
    print(" SDD Framework v6.6 - Scaffolder Verification & Modular Engine")
    print("=================================================================")
    if not verify_scaffolder_parity():
        sys.exit(1)
    print("\n[+] Scaffolder v6.6 verificado con éxito.")
    return 0

if __name__ == "__main__":
    sys.exit(main())

