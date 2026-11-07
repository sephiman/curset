# SPDX-License-Identifier: AGPL-3.0-only
"""Currency audit, norms: each BOE entry of C2's normativa.yaml against its «Última actualización» on boe.es."""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.request
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[5]
NORMATIVA = REPO / "content" / "age-auxiliar-c2" / "sources" / "normativa.yaml"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) curset-currency-audit"
LAST_UPDATE = re.compile(r"ltima actualizaci(?:ó|&oacute;)n,? publicada el (\d{2})/(\d{2})/(\d{4})")


def fetch(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8", "replace")


def latest(boe_id: str) -> str | None:
    match = LAST_UPDATE.search(fetch(f"https://www.boe.es/buscar/act.php?id={boe_id}"))
    return f"{match[3]}-{match[2]}-{match[1]}" if match else None


def main(out: Path) -> None:
    rows = []
    for entry in yaml.safe_load(NORMATIVA.read_text(encoding="utf-8")):
        boe_id = entry.get("boe_id")
        if not boe_id:
            continue
        try:
            live = latest(boe_id)
        except OSError as error:
            live = f"error: {error}"
        rows.append({"short": entry["short"], "boe_id": boe_id, "stored": entry.get("consolidated_as_of"), "live": live})
        time.sleep(1)
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
