"""Download the BOE daily summaries between two dates and save (date, id, section, department, title) rows as JSON."""

import datetime as dt
import json
import subprocess
import sys
import time
from pathlib import Path

UA = "Mozilla/5.0 (X11; Linux x86_64) curset-sources-check"


def items(node: object) -> list[dict[str, object]]:
    if isinstance(node, list):
        return [x for n in node for x in items(n)]
    if not isinstance(node, dict):
        return []
    found = [node] if "identificador" in node and "titulo" in node else []
    return found + [x for k, v in node.items() if k != "identificador" for x in items(v)]


def main() -> None:
    out, start, end = Path(sys.argv[1]), dt.date.fromisoformat(sys.argv[2]), dt.date.fromisoformat(sys.argv[3])
    rows = []
    day = start
    while day <= end:
        raw = subprocess.run(["curl", "-s", "-A", UA, "-H", "Accept: application/json",
                              f"https://www.boe.es/datosabiertos/api/boe/sumario/{day:%Y%m%d}"],
                             capture_output=True, text=True).stdout
        try:
            data = json.loads(raw).get("data", {})
        except ValueError:
            data = {}
        for it in items(data):
            rows.append({"date": day.isoformat(), "id": it["identificador"], "titulo": it["titulo"]})
        day += dt.timedelta(days=1)
        time.sleep(0.3)
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=0))
    print(len(rows), "items")


if __name__ == "__main__":
    main()
