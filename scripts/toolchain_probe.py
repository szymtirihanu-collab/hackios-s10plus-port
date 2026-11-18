#!/usr/bin/env python3
"""Report host tool availability and versions. Read-only; does not install anything."""
from pathlib import Path
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "build" / "logs" / "toolchain-probe.json"
TOOLS = {
    "python3": ["--version"],
    "git": ["--version"],
    "make": ["--version"],
    "clang": ["--version"],
    "cmake": ["--version"],
    "ninja": ["--version"],
    "jq": ["--version"],
    "file": ["--version"],
}

def probe(name, args):
    path = shutil.which(name)
    if not path:
        return {"available": False, "path": None, "version": None}
    try:
        proc = subprocess.run([path, *args], capture_output=True, text=True, timeout=5, check=False)
        first = (proc.stdout or proc.stderr).splitlines()
        return {"available": True, "path": path, "version": first[0] if first else "unknown", "exit_code": proc.returncode}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"available": True, "path": path, "error": str(exc)}

def main():
    report = {"scope": "host-only; read-only", "tools": {name: probe(name, args) for name, args in TOOLS.items()}}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\\n", encoding="utf-8")
    for name, result in report["tools"].items():
        print(f"{name}: {result.get('version') or ('available' if result['available'] else 'missing')}")
    print(f"Report: {OUT.relative_to(ROOT)}")
    print("No packages were installed and no device was accessed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
