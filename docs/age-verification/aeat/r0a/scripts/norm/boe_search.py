"""Search the BOE consolidated-legislation API by a query_string and print id, update stamp, vigencia and title."""

import json
import subprocess
import sys

UA = "Mozilla/5.0 (X11; Linux x86_64) curset-sources-check"
API = "https://www.boe.es/datosabiertos/api/legislacion-consolidada"


def search(query: str, limit: int = 30) -> list[dict[str, object]]:
    q = json.dumps({"query": {"query_string": {"query": query}}, "sort": [{"fecha_publicacion": "desc"}]})
    out = subprocess.run(
        ["curl", "-s", "-G", "-A", UA, "-H", "Accept: application/json",
         "--data-urlencode", f"query={q}", "--data-urlencode", f"limit={limit}", API],
        capture_output=True, text=True,
    ).stdout
    data = json.loads(out).get("data") or []
    return data if isinstance(data, list) else []


if __name__ == "__main__":
    for row in search(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 30):
        print(row["identificador"], row.get("fecha_publicacion"), str(row.get("fecha_actualizacion", ""))[:8],
              "agotada" if row.get("vigencia_agotada") == "S" else "", (row.get("estatus_derogacion") or ""),
              str(row["titulo"])[:170])
