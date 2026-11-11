"""Print the boe.es analysis of each BOE id given: entry-into-force note, materias skipped, all later references."""

import json
import subprocess
import sys
from pathlib import Path

UA = "Mozilla/5.0 (X11; Linux x86_64) curset-sources-check"
OUT = Path(sys.argv[1])


def rows(block: object, key: str) -> list[dict[str, object]]:
    block = block[0] if isinstance(block, list) and block else block
    got = block.get(key, []) if isinstance(block, dict) else []
    return [got] if isinstance(got, dict) else got


for boe_id in sys.argv[2:]:
    dest = OUT / "api" / f"{boe_id}_analisis.json"
    subprocess.run(["curl", "-s", "-A", UA, "-H", "Accept: application/json", "-o", str(dest),
                    f"https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/{boe_id}/analisis"], check=True)
    try:
        data = json.loads(dest.read_text())["data"][0]
    except (ValueError, KeyError, IndexError, TypeError):
        print("=====", boe_id, "NO ANALYSIS (not in the consolidated collection)")
        continue
    print("=====", boe_id, "| nota:", json.dumps(data.get("notas"), ensure_ascii=False))
    for r in rows(data["referencias"].get("posteriores"), "posterior"):
        print("   post", r["id_norma"], r["relacion"]["texto"], "|", r["texto"][:300])
    if "-v" in sys.argv[1:2]:
        continue
