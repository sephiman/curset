"""Write checks/norm_currency.json: boe.es state of every entry on 2026-11-11, the C1/C2 snapshots boe.es has overtaken,
the decree-laws awaiting convalidation and the annual figures. Run after build.py: python3 -I currency.py <normbuild>."""

import json
import sys
from pathlib import Path

import yaml

REPO = Path("/home/juanjo/PycharmProjects/curset")
SCRATCH = Path(sys.argv[1])
COURSES = {"c1": "age-administrativo-c1", "c2": "age-auxiliar-c2"}

# Decree-laws this snapshot relies on; status read from the boe.es analysis and the BOE summaries 2026-09-28..2026-11-11.
RDL = [
    {"norma": "Real Decreto-ley 7/2026, de 20 de marzo", "boe_id": "BOE-A-2026-6544", "estado": "convalidado (BOE-A-2026-7125)"},
    {"norma": "Real Decreto-ley 22/2026, de 1 de septiembre", "boe_id": "BOE-A-2026-18429", "estado": "convalidado (BOE-A-2026-19420)"},
    {"norma": "Real Decreto-ley 3/2026, de 3 de febrero", "boe_id": "BOE-A-2026-2548", "estado": "convalidado (BOE-A-2026-4668)"},
    {"norma": "Real Decreto-ley 26/2026, de 29 de septiembre", "boe_id": "BOE-A-2026-20266",
     "estado": "derogado por el Congreso (Resolución de 2-10-2026, BOE-A-2026-20526); sustituido por el RDL 29/2026"},
    {"norma": "Real Decreto-ley 29/2026, de 6 de octubre", "boe_id": "BOE-A-2026-20823",
     "estado": "en vigor 08-10-2026; sin acuerdo de convalidación ni de derogación publicado a 11-11-2026"},
    {"norma": "Real Decreto-ley 31/2026, de 20 de octubre", "boe_id": "BOE-A-2026-21872",
     "estado": "en vigor 21-10-2026; sin acuerdo de convalidación ni de derogación publicado a 11-11-2026"},
    {"norma": "Real Decreto-ley 33/2026, de 10 de noviembre", "boe_id": "BOE-A-2026-23602", "estado": "publicado 11-11-2026, en vigor 12-11-2026"},
    {"norma": "Real Decreto-ley 35/2026, de 10 de noviembre", "boe_id": "BOE-A-2026-23604", "estado": "publicado 11-11-2026, en vigor 12-11-2026"},
    {"norma": "Real Decreto-ley 36/2026, de 10 de noviembre", "boe_id": "BOE-A-2026-23605", "estado": "publicado 11-11-2026, en vigor 12-11-2026"},
    {"norma": "Reales Decretos-leyes 9/2024, 16/2025 y 2/2026", "boe_id": "RDL 16/2025 BOE-A-2025-26458; RDL 2/2026 BOE-A-2026-2547",
     "estado": "derogados (Resoluciones BOE-A-2025-1136, BOE-A-2026-2024, BOE-A-2026-4667): sus cambios tributarios, entre ellos la "
               "prórroga a 2025 y 2026 de los límites de módulos de 250.000/125.000 euros, quedaron sin efecto"},
]


def main() -> None:
    cur: dict[str, dict[str, object]] = {}
    for f in ("currency_raw.json", "extra/currency_raw.json", "others/currency_raw.json"):
        cur.update(json.loads((SCRATCH / f).read_text()))
    snaps = {c: {e["boe_id"]: e for e in yaml.safe_load((REPO / f"content/{n}/sources/normativa.yaml").read_text()) if e.get("boe_id")}
             for c, n in COURSES.items()}
    entries = yaml.safe_load((REPO / "content/aeat-agentes-hacienda/sources/normativa.yaml").read_text())
    rows = []
    for e in entries:
        i = e.get("boe_id")
        c = cur.get(i, {}) if i else {}
        rows.append({
            "short": e["short"], "id": i or e.get("celex"),
            "boe_es_ultima_actualizacion": c.get("ultima"), "boe_es_encontrada": c.get("found"), "boe_es_derogada": c.get("derogada"),
            "consolidated_as_of": e["consolidated_as_of"],
            "snapshot_c1": snaps["c1"].get(i, {}).get("consolidated_as_of") if i else None,
            "snapshot_c2": snaps["c2"].get(i, {}).get("consolidated_as_of") if i else None,
            "origen": e.get("origen"),
            "amended_2025_2026_boe_es": c.get("amended_2025_2026") if i else e.get("amended_2025_2026"),
            "cambios_pendientes": [{"norma": p["norma"], "en_vigor": p["en_vigor"], "articulos": p["articulos"]}
                                   for p in e.get("cambios_pendientes") or []],
            "cifras_anuales": e.get("cifras_anuales"),
        })
    newer = []
    for c, by in snaps.items():
        for i, e in by.items():
            u = cur.get(i, {}).get("ultima")
            if u and u != e.get("consolidated_as_of"):
                newer.append({"curso": COURSES[c], "id": i, "short": e["short"], "snapshot": e["consolidated_as_of"], "boe_es": u})
    report = {
        "checked": "2026-11-11",
        "method": "act.php «Última actualización publicada el» + API legislacion-consolidada/id/<ID>/analisis; BOE daily summaries "
                  "2026-09-28..2026-11-11 for convalidation/derogation agreements; EU: Publications Office SPARQL "
                  "(consolidated versions and amending acts of 32013R0952, 32015R2446, 32015R2447; C2's EU norms re-read: "
                  "no consolidation newer than the snapshot).",
        "pge": "No Ley de PGE for 2024, 2025 or 2026 in the consolidated collection; the newest budget item is Orden HAC/557/2026 "
               "(rules for drafting the 2027 budget). Ley 31/2022 (PGE 2023) applies prorrogued (art. 134.4 CE).",
        "entries": rows,
        "c1_c2_snapshots_older_than_boe_es": newer,
        "c1_c2_all_boe_ids_checked": sum(len(v) for v in snaps.values()),
        "decretos_ley": RDL,
    }
    (REPO / "docs/age-verification/aeat/r0a/checks/norm_currency.json").write_text(json.dumps(report, ensure_ascii=False, indent=1))
    print(len(rows), "entries;", len(newer), "C1/C2 snapshots older than boe.es")


if __name__ == "__main__":
    main()
