#!/usr/bin/env python3
"""Host-only project preflight. Does not access or modify a connected device."""
from pathlib import Path
import json
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "target.json"

def main() -> int:
    if not CONFIG.is_file():
        print(f"ERROR: missing target config: {CONFIG}")
        return 2
    try:
        cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR: invalid JSON: {exc}")
        return 2
    print(f"Project: {cfg.get('project')}")
    print(f"Baseline: {cfg.get('baseline')}")
    device = cfg.get("device", {})
    print(f"Target: {device.get('model')} ({device.get('codename')}) / {device.get('architecture')}")
    if cfg.get("baseline") != "0100":
        print("ERROR: baseline lock violated; only 0100 is allowed")
        return 3
    if cfg.get("device_operations", {}).get("automated_flash", True):
        print("ERROR: automated flashing must remain disabled")
        return 3
    for tool in ("python3", "git"):
        found = shutil.which(tool)
        print(f"{tool}: {found or 'NOT FOUND'}")
    print("Preflight passed (host-only). Source/toolchain availability is not yet established.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
