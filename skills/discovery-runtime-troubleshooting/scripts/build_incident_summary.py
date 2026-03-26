#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys

HEADER = [
    "issue_title",
    "impact_scope",
    "failing_layer",
    "root_cause",
    "workaround",
    "permanent_fix",
    "validation_result",
    "residual_risk",
]


def main() -> None:
    if len(sys.argv) != 3:
        print("usage: build_incident_summary.py <input.tsv> <output.csv>")
        raise SystemExit(1)

    source, target = sys.argv[1:]
    with open(source, "r", encoding="utf-8") as src, open(
        target, "w", encoding="utf-8", newline=""
    ) as dst:
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
