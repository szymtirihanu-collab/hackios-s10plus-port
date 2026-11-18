#!/usr/bin/env python3
"""Validate a SHA-256 artifact manifest. Host-only; never writes to a device."""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

def validate(root: Path):
    root = root.resolve()
    manifest = root / "build" / "artifacts" / "manifest.json"
    if not manifest.is_file():
        return False, ["No manifest found; no artifacts are registered."]
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return False, [f"Invalid manifest: {exc}"]
    if data.get("baseline") != "0100":
        return False, ["Manifest baseline is not 0100."]
    artifacts = data.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        return False, ["Manifest has no artifact entries."]
    errors = []
    for item in artifacts:
        if not isinstance(item, dict):
            errors.append(f"Invalid entry: {item!r}")
            continue
        rel = item.get("path", "")
        expected = item.get("sha256", "")
        if not isinstance(rel, str) or not rel or not isinstance(expected, str) or not re.fullmatch(r"[a-fA-F0-9]{64}", expected):
            errors.append(f"Invalid entry: {item!r}")
            continue
        path = (root / rel).resolve()
        if not path.is_relative_to(root):
            errors.append(f"Path escapes repository: {rel}")
            continue
        if not path.is_file():
            errors.append(f"Missing artifact: {rel}")
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected.lower():
            errors.append(f"Hash mismatch: {rel}")
    return not errors, errors

def main() -> int:
    try:
        ok, messages = validate(ROOT)
    except (OSError, KeyError, TypeError, ValueError) as exc:
        print(f"ERROR: {exc}")
        return 2
    for message in messages:
        print(message)
    if ok:
        print("Artifact manifest validation passed.")
        return 0
    return 2

if __name__ == "__main__":
    sys.exit(main())
