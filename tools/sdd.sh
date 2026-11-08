#!/usr/bin/env bash
# ==============================================================================
# tools/sdd.sh - Universal POSIX Harness Runner for SDD Framework v6.6
# Permite invocar el arnés de gobernanza SDD en Linux, macOS y Docker.
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# Si pwsh está disponible, delegar al arnés PowerShell para compatibilidad total
if command -v pwsh >/dev/null 2>&1; then
    exec pwsh -NoProfile -ExecutionPolicy Bypass -File "${REPO_ROOT}/harness/sdd.ps1" "$@"
fi

# Si pwsh no está disponible, usar el CLI universal en Python
if command -v python3 >/dev/null 2>&1; then
    exec python3 "${SCRIPT_DIR}/sdd_cli.py" "$@"
elif command -v python >/dev/null 2>&1; then
    exec python "${SCRIPT_DIR}/sdd_cli.py" "$@"
fi

echo "[ERROR]: Se requiere PowerShell Core ('pwsh') o Python 3 ('python3') para ejecutar el arnés SDD." >&2
exit 1

