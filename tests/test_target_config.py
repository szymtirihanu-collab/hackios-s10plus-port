import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class TargetConfigTests(unittest.TestCase):
    def test_config_is_0100_and_correct_device(self):
        cfg = json.loads((ROOT / "config/target.json").read_text())
        self.assertEqual(cfg["baseline"], "0100")
        self.assertEqual(cfg["device"]["codename"], "beyond2lte")
        self.assertEqual(cfg["device"]["model"], "SM-G975F")
        self.assertEqual(cfg["device"]["architecture"], "arm64")

    def test_device_writes_disabled(self):
        cfg = json.loads((ROOT / "config/target.json").read_text())
        ops = cfg["device_operations"]
        self.assertFalse(ops["automated_flash"])
        self.assertFalse(ops["partition_write"])
        self.assertFalse(ops["format"])
        self.assertFalse(ops["repartition"])

if __name__ == "__main__":
    unittest.main()
