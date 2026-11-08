#!/usr/bin/env bash
# ==============================================================================
# install.sh - One-Liner Installer for SDD Framework v6.6 (POSIX / Linux / macOS)
# Usage: curl -fsSL https://raw.githubusercontent.com/svelascotellez/ssd-projects/main/install.sh | bash
# ==============================================================================

set -euo pipefail

DESTINATION="${HOME}/.sdd"
BASE_URL="https://raw.githubusercontent.com/svelascotellez/ssd-projects/main"

echo "=== [SDD Framework v6.6]: Installing to ${DESTINATION}... ==="
mkdir -p "${DESTINATION}"

FILES=(
    "setup-sdd-project-v66.py"
    "setup-sdd-project-v66.ps1"
    "tools/sdd_cli.py"
    "tools/sdd.sh"
    "README.md"
    "LICENSE"
)

for file in "${FILES[@]}"; do
    target="${DESTINATION}/${file}"
    mkdir -p "$(dirname "${target}")"
    echo "  [+] Downloading ${file}..."
    curl -fsSL "${BASE_URL}/${file}" -o "${target}"
done

chmod +x "${DESTINATION}/tools/sdd.sh" "${DESTINATION}/tools/sdd_cli.py" || true

echo ""
echo "[OK] SDD Framework v6.6 installed successfully in ${DESTINATION}."
echo "To initialize a new project, run:"
echo "  python3 ${DESTINATION}/setup-sdd-project-v66.py --project-name 'MyProject' --stack 'python'"
echo ""

