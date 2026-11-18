#!/usr/bin/env python3
"""Validate a SHA-256 artifact manifest. Never writes to a device."""
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "target.json"

def main() -> int:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    manifest = ROOT / cfg["outputs"]["manifest"]
    if not manifest.exists():
        print(f"No manifest found: {manifest}")
        print("No build artifacts are registered yet.")
        return 1
    data = json.loads(manifest.read_text(encoding="utf-8"))
    if data.get("baseline") != "0100":
        print("ERROR: manifest baseline is not 0100")
        return 2
    artifacts = data.get("artifacts", [])
    if not artifacts:
        print("Manifest has no artifacts.")
        return 1
    ok = True
    for item in artifacts:
        rel = item.get("path", "")
        expected = item.get("sha256", "").lower()
        path = (ROOT / rel).resolve()
        if not path.is_relative_to(ROOT.resolve()):
            print(f"ERROR: path escapes repository: {rel}")
            ok = False
            continue
        if not path.is_file():
            print(f"MISSING: {rel}")
            ok = False
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            print(f"HASH MISMATCH: {rel}")
            ok = False
        else:
            print(f"OK: {rel} ({path.stat().st_size} bytes)")
    return 0 if ok else 2

if __name__ == "__main__":
    sys.exit(main())
