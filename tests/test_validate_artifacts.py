import importlib.util
from pathlib import Path
import hashlib
import json
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_artifacts", ROOT / "scripts/validate_artifacts.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)

class ArtifactValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "build/artifacts").mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def write_manifest(self, data):
        (self.root / "build/artifacts/manifest.json").write_text(json.dumps(data), encoding="utf-8")

    def test_valid_manifest_hash(self):
        artifact = self.root / "build/artifacts/sample.txt"
        artifact.write_text("test artifact", encoding="utf-8")
        digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
        self.write_manifest({"baseline": "0100", "artifacts": [{"path": "build/artifacts/sample.txt", "sha256": digest}]})
        ok, errors = module.validate(self.root)
        self.assertTrue(ok, errors)

    def test_rejects_wrong_baseline(self):
        self.write_manifest({"baseline": "0101", "artifacts": [{"path": "x", "sha256": "0"*64}]})
        ok, errors = module.validate(self.root)
        self.assertFalse(ok)
        self.assertIn("Manifest baseline is not 0100.", errors)

    def test_rejects_path_escape(self):
        outside = self.root.parent / "outside.txt"
        outside.write_text("outside", encoding="utf-8")
        digest = hashlib.sha256(outside.read_bytes()).hexdigest()
        self.write_manifest({"baseline": "0100", "artifacts": [{"path": "../outside.txt", "sha256": digest}]})
        ok, errors = module.validate(self.root)
        self.assertFalse(ok)
        self.assertTrue(any("Path escapes repository" in error for error in errors))

    def test_rejects_hash_mismatch(self):
        artifact = self.root / "build/artifacts/sample.txt"
        artifact.write_text("actual", encoding="utf-8")
        self.write_manifest({"baseline": "0100", "artifacts": [{"path": "build/artifacts/sample.txt", "sha256": "0"*64}]})
        ok, errors = module.validate(self.root)
        self.assertFalse(ok)
        self.assertTrue(any("Hash mismatch" in error for error in errors))

if __name__ == "__main__":
    unittest.main()
