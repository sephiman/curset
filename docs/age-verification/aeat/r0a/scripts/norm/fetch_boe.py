"""Fetch boe.es act.php («Última actualización publicada el», title, derogation) and the /analisis JSON for each BOE id on stdin."""

import json
import re
import subprocess
import sys
import time
from html import unescape
from pathlib import Path

UA = "Mozilla/5.0 (X11; Linux x86_64) curset-sources-check"
OUT = Path(sys.argv[1])


def curl(url: str, dest: Path, accept: str | None = None) -> str:
    cmd = ["curl", "-s", "-A", UA, "-o", str(dest), url]
    if accept:
        cmd[1:1] = ["-H", f"Accept: {accept}"]
    subprocess.run(cmd, check=True)
    return dest.read_text(encoding="utf-8", errors="replace")


def page_facts(boe_id: str) -> dict[str, object]:
    html = curl(f"https://www.boe.es/buscar/act.php?id={boe_id}", OUT / "pages" / f"{boe_id}.html")
    title = re.search(r'<h3 class="documento-tit">(.*?)</h3>', html, re.S)
    last = re.search(r"Última actualización publicada el (\d\d)/(\d\d)/(\d{4})", html)
    repealed = re.search(r"(Norma derogada|DEROGAD[OA]|Texto derogado|Vigencia agotada)", html)
    pub = re.search(r"«BOE» núm\. (\d+), de (\d+) de (\w+) de (\d{4})", html)
    return {
        "id": boe_id,
        "title": unescape(re.sub(r"\s+", " ", title.group(1))).strip() if title else None,
        "ultima": f"{last.group(3)}-{last.group(2)}-{last.group(1)}" if last else None,
        "derogada": repealed.group(1) if repealed else None,
        "boe_num": pub.group(0) if pub else None,
        "found": bool(title),
    }


def amendments(boe_id: str) -> list[dict[str, str]]:
    raw = curl(f"https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/{boe_id}/analisis",
               OUT / "api" / f"{boe_id}_analisis.json", "application/json")
    try:
        data = json.loads(raw)["data"][0]
        post = data["referencias"]["posteriores"]
    except (ValueError, KeyError, IndexError, TypeError):
        return []
    block = post[0] if isinstance(post, list) and post else post
    rows = block.get("posterior", []) if isinstance(block, dict) else []
    rows = [rows] if isinstance(rows, dict) else rows
    return [{"id": r["id_norma"], "rel": r["relacion"]["texto"], "texto": r["texto"]}
            for r in rows if r["id_norma"][6:10] in ("2025", "2026")]


def main() -> None:
    (OUT / "pages").mkdir(parents=True, exist_ok=True)
    (OUT / "api").mkdir(parents=True, exist_ok=True)
    result = {}
    for line in sys.stdin:
        boe_id = line.strip()
        if not boe_id:
            continue
        facts = page_facts(boe_id)
        facts["amended_2025_2026"] = amendments(boe_id)
        result[boe_id] = facts
        print(boe_id, facts["ultima"], facts["derogada"], (facts["title"] or "NOT FOUND")[:90], flush=True)
        time.sleep(0.4)
    (OUT / "currency_raw.json").write_text(json.dumps(result, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
