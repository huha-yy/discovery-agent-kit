#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys


def main() -> None:
    if len(sys.argv) != 3:
        print("usage: build_coverage_matrix.py <input.tsv> <output.csv>")
        raise SystemExit(1)

    source, target = sys.argv[1:]
    with open(source, "r", encoding="utf-8") as src, open(target, "w", encoding="utf-8", newline="") as dst:
        writer = csv.writer(dst)
        writer.writerow(["vendor", "resource_type", "evidence_level", "evidence_source", "notes"])
        for raw in src:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            while len(parts) < 5:
                parts.append("")
            writer.writerow(parts[:5])


if __name__ == "__main__":
    main()
