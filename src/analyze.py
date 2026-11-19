"""A small, dependency-free demonstration of an inquiry analytics workflow.

All example records are synthetic. This is not production VOIXE code.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

CATEGORIES = {"new_booking", "existing_booking", "service_request", "sales", "other"}
PRIORITIES = {"urgent", "normal", "low"}


def summarize(records: list[dict]) -> dict:
    """Validate normalized inquiries and calculate useful operational metrics."""
    seen = set()
    categories = Counter()
    channels = Counter()
    priorities = Counter()
    followups = []
    opportunities = []
    for record in records:
        required = {"id", "channel", "category", "priority", "follow_up_required", "opportunity"}
        missing = required - record.keys()
        if missing:
            raise ValueError(f"Record missing fields: {', '.join(sorted(missing))}")
        if record["id"] in seen:
            raise ValueError(f"Duplicate record ID: {record['id']}")
        seen.add(record["id"])
        if record["category"] not in CATEGORIES:
            raise ValueError(f"Unsupported category: {record['category']}")
        if record["priority"] not in PRIORITIES:
            raise ValueError(f"Unsupported priority: {record['priority']}")
        if not isinstance(record["follow_up_required"], bool) or not isinstance(record["opportunity"], bool):
            raise ValueError("follow_up_required and opportunity must be booleans")
        categories[record["category"]] += 1
        channels[record["channel"]] += 1
        priorities[record["priority"]] += 1
        if record["follow_up_required"]:
            followups.append(record["id"])
        if record["opportunity"]:
            opportunities.append(record["id"])
    total = len(records)
    return {
        "total_inquiries": total,
        "by_channel": dict(sorted(channels.items())),
        "by_category": dict(sorted(categories.items())),
        "by_priority": dict(sorted(priorities.items())),
        "follow_up_count": len(followups),
        "follow_up_rate_pct": round(len(followups) / total * 100, 1) if total else 0.0,
        "identified_opportunity_count": len(opportunities),
        "identified_opportunity_rate_pct": round(len(opportunities) / total * 100, 1) if total else 0.0,
        "follow_up_ids": followups,
        "opportunity_ids": opportunities,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize synthetic multichannel inquiries")
    parser.add_argument("input", type=Path, help="JSON file with normalized inquiry records")
    parser.add_argument("--output", type=Path, help="Optional JSON output path")
    args = parser.parse_args()
    records = json.loads(args.input.read_text(encoding="utf-8"))
    if not isinstance(records, list):
        parser.error("Input JSON must be a list")
    result = summarize(records)
    payload = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
        print(f"Summary written to {args.output}")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
