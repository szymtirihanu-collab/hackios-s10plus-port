import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("toolchain_probe", ROOT / "scripts/toolchain_probe.py")
probe_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(probe_module)

class ToolchainProbeTests(unittest.TestCase):
    def test_probe_list_is_stable_and_host_only(self):
        self.assertEqual(list(probe_module.TOOLS), ["python3", "git", "make", "clang", "cmake", "ninja", "jq", "file"])
        self.assertTrue(all(isinstance(args, list) for args in probe_module.TOOLS.values()))

    def test_missing_tool_is_reported_without_exception(self):
        result = probe_module.probe("definitely-not-a-real-tool-name", ["--version"])
        self.assertFalse(result["available"])
        self.assertIsNone(result["path"])

if __name__ == "__main__":
    unittest.main()
