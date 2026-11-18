#!/usr/bin/env python3
"""Create a host-side build workspace only. No device access and no image writes."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "target.json"

def main() -> int:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    if cfg.get("baseline") != "0100":
        raise SystemExit("Refusing to prepare workspace: baseline is not 0100")
    out = ROOT / cfg["outputs"]["directory"]
    out.mkdir(parents=True, exist_ok=True)
    (ROOT / "build" / "logs").mkdir(parents=True, exist_ok=True)
    (ROOT / "build" / "tmp").mkdir(parents=True, exist_ok=True)
    marker = out / "BUILD_STATUS.txt"
    marker.write_text(
        "Workspace prepared only. No source build has run and no bootable/flashable image exists.\n"
        "Baseline: 0100\n",
        encoding="utf-8"
    )
    print(f"Host workspace prepared: {out}")
    print("No device was accessed. No image was produced.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
