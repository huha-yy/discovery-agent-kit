#!/usr/bin/env python3
from __future__ import annotations

import json
import sys


def main() -> None:
    if len(sys.argv) != 5:
        print("usage: scaffold_pack.py <pack_code> <vendor> <domain> <resource_type>")
        raise SystemExit(1)

    pack_code, vendor, domain, resource_type = sys.argv[1:]
    payload = {
        "pack_code": pack_code,
        "pack_name": pack_code.replace("-", " ").title(),
        "cloud_vendor": vendor,
        "resource_domain": domain,
        "resource_type": resource_type,
        "pack_type": "CAPI",
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
