"""Read title, publication and «Última actualización publicada el» from boe.es for each BOE id given (one per line on stdin)."""

import json
import re
import subprocess
import sys
import time
from html import unescape

UA = "Mozilla/5.0 (X11; Linux x86_64) curset-sources-check"


def fetch(boe_id: str) -> dict[str, str | None]:
    html = subprocess.run(
        ["curl", "-s", "-A", UA, f"https://www.boe.es/buscar/act.php?id={boe_id}"], capture_output=True, text=True
    ).stdout
    title = re.search(r'<h3 class="documento-tit">(.*?)</h3>', html, re.S)
    last = re.search(r"Última actualización publicada el (\d\d)/(\d\d)/(\d{4})", html)
    repealed = re.search(r"(Norma derogada|DEROGAD[OA]|Texto derogado)", html)
    return {
        "id": boe_id,
        "title": unescape(re.sub(r"\s+", " ", title.group(1))).strip() if title else None,
        "ultima": f"{last.group(3)}-{last.group(2)}-{last.group(1)}" if last else None,
        "derogada": repealed.group(1) if repealed else None,
        "found": bool(title),
    }


def main() -> None:
    out = []
    for line in sys.stdin:
        boe_id = line.strip()
        if not boe_id:
            continue
        out.append(fetch(boe_id))
        print(json.dumps(out[-1], ensure_ascii=False), flush=True)
        time.sleep(0.3)


if __name__ == "__main__":
    main()
