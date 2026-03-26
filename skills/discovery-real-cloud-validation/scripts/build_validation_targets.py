#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys

HEADER = [
    "vendor",
    "account_code",
    "resource_type",
    "region",
    "zone",
    "expected_result",
    "task_id",
    "result",
    "returned_count",
    "evidence_level",
    "note",
]


def main() -> None:
    if len(sys.argv) != 3:
        print("usage: build_validation_targets.py <input.tsv> <output.csv>")
        raise SystemExit(1)

    source, target = sys.argv[1:]
    with open(source, "r", encoding="utf-8") as src, open(target, "w", encoding="utf-8", newline="") as dst:
        writer = csv.writer(dst)
        writer.writerow(HEADER)
        for raw in src:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            while len(parts) < len(HEADER):
                parts.append("")
            writer.writerow(parts[: len(HEADER)])


if __name__ == "__main__":
    main()
