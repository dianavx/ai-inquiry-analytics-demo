"""Run with: python -m unittest discover -s tests -v"""
import json
import unittest
from pathlib import Path
from src.analyze import summarize


class SummarizeTests(unittest.TestCase):
    def setUp(self):
        self.records = json.loads(Path("examples/inquiries.json").read_text(encoding="utf-8"))

    def test_summary_metrics(self):
        summary = summarize(self.records)
        self.assertEqual(summary["total_inquiries"], 8)
        self.assertEqual(summary["identified_opportunity_count"], 4)
        self.assertEqual(summary["follow_up_count"], 5)
        self.assertEqual(summary["by_channel"]["voice"], 3)

    def test_empty_dataset(self):
        self.assertEqual(summarize([])["follow_up_rate_pct"], 0.0)

    def test_duplicate_id_fails(self):
        with self.assertRaises(ValueError):
            summarize(self.records + [self.records[0]])

    def test_invalid_category_fails(self):
        bad = [dict(self.records[0], category="invented")]
        with self.assertRaises(ValueError):
            summarize(bad)


if __name__ == "__main__":
    unittest.main()
