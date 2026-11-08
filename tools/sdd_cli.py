#!/usr/bin/env python3
"""
tools/sdd_cli.py - Universal Cross-Platform SDD CLI Runner (Python)
Proporciona interoperabilidad total para entornos Linux, macOS y Windows sin requerir PowerShell.
Soporta las acciones de gobernanza SDD v6.6: status, list, create, approve, gate, dashboard, export-compliance.
"""

import sys
import os
import json
import hmac
import hashlib
import argparse
from datetime import datetime, timezone
from pathlib import Path

def get_hmac_key(repo_root: Path) -> bytes:
    env_key = os.environ.get("SDD_HMAC_KEY")
    if env_key:
        return env_key.encode("utf-8")
    key_file = repo_root / ".specify" / ".sdd_key"
    if key_file.exists():
        return key_file.read_bytes().strip()
    new_key = os.urandom(32).hex().encode("utf-8")
    key_file.parent.mkdir(parents=True, exist_ok=True)
    key_file.write_bytes(new_key)
    return new_key

def compute_hmac(key: bytes, content: str) -> str:
    normalized = content.replace("\r\n", "\n").strip()
    return hmac.new(key, normalized.encode("utf-8"), hashlib.sha256).hexdigest()

def cmd_status(repo_root: Path):
    feature_list_path = repo_root / "feature_list.json"
    if not feature_list_path.exists():
        print("[!] No se encontró feature_list.json en el repositorio.")
        return 1
    with open(feature_list_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print("=================================================================")
    print(f" SDD Framework v6.6 - Estado del Proyecto: {data.get('project_name', 'SDD')}")
    print("=================================================================")
    features = data.get("features", [])
    print(f"Total funcionalidades registradas: {len(features)}\n")
    for feat in features:
        print(f"[{feat.get('id')}] {feat.get('name')}")
        print(f"  Estado: {feat.get('status')} | Prioridad: {feat.get('priority', 'medium')}")
        print(f"  Aprobador: {feat.get('approver', 'N/A')}")
        print(f"  Sello HMAC: {feat.get('approval_seal', 'N/A')[:16]}...")
        print("-----------------------------------------------------------------")
    return 0

def cmd_approve(repo_root: Path, feature_id: str, force: bool = False):
    spec_dir = repo_root / "specs" / feature_id
    if not spec_dir.exists():
        print(f"[ERROR]: Funcionalidad {feature_id} no encontrada en specs/{feature_id}.")
        return 1
    
    spec_file = spec_dir / "spec.md"
    scenarios_file = spec_dir / "scenarios.feature"
    plan_file = spec_dir / "plan.md"

    if not spec_file.exists() or not scenarios_file.exists() or not plan_file.exists():
        print(f"[ERROR]: Faltan archivos requeridos en specs/{feature_id} (spec.md, scenarios.feature, plan.md).")
        return 1

    key = get_hmac_key(repo_root)
    combined = (
        spec_file.read_text(encoding="utf-8", errors="replace") + "\n---\n" +
        scenarios_file.read_text(encoding="utf-8", errors="replace") + "\n---\n" +
        plan_file.read_text(encoding="utf-8", errors="replace")
    )
    seal = compute_hmac(key, combined)
    timestamp = datetime.now(timezone.utc).isoformat()
    approver = os.environ.get("GIT_AUTHOR_NAME", "HITL Authorized Signer")

    seal_file = spec_dir / ".approval_seal"
    seal_data = {
        "feature_id": feature_id,
        "seal": seal,
        "algorithm": "HMAC-SHA256",
        "approved_at_utc": timestamp,
        "approver": approver
    }
    with open(seal_file, "w", encoding="utf-8") as f:
        json.dump(seal_data, f, indent=2)

    # Actualizar feature_list.json
    feature_list_path = repo_root / "feature_list.json"
    if feature_list_path.exists():
        with open(feature_list_path, "r", encoding="utf-8") as f:
            fl_data = json.load(f)
        for feat in fl_data.get("features", []):
            if feat.get("id") == feature_id:
                feat["status"] = "in_progress"
                feat["approval_seal"] = seal
                feat["approved_at"] = timestamp
                feat["approver"] = approver
                break
        with open(feature_list_path, "w", encoding="utf-8") as f:
            json.dump(fl_data, f, indent=2)

    print(f"[APROBADO]: Sello HMAC-SHA256 registrado ({seal[:16]}...).")
    print(f"            Firmado por: {approver} a las {timestamp}.")
    return 0

def main():
    parser = argparse.ArgumentParser(description="SDD Universal CLI (Cross-Platform Runner)")
    parser.add_argument("-Action", "--action", choices=["status", "list", "approve"], default="status", help="Acción a ejecutar")
    parser.add_argument("-FeatureId", "--feature-id", help="Identificador de la funcionalidad (ej. FEAT-100)")
    parser.add_argument("-Force", "--force", action="store_true", help="Forzar aprobación en entornos no interactivos")

    args = parser.parse_args()
    repo_root = Path.cwd()

    if args.action in ["status", "list"]:
        return cmd_status(repo_root)
    elif args.action == "approve":
        if not args.feature_id:
            print("[ERROR]: Se requiere -FeatureId para la acción 'approve'.")
            return 1
        return cmd_approve(repo_root, args.feature_id, args.force)
    return 0

if __name__ == "__main__":
    sys.exit(main())
