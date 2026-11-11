"""Build content/aeat-agentes-hacienda/sources/normativa.yaml and its snapshot files (round R0a, 2026-11-11).

Run from this folder: python3 -I build.py <normbuild scratch folder>. The scratch folder holds currency_raw.json and
extra/currency_raw.json (fetch_boe.py), dl/ (fresh BOE downloads), eu/ (Cellar downloads) and the coordinator's
read-only norms/ folder sits next to it.
"""

import copy
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

TODAY = "2026-11-11"
REPO = Path("/home/juanjo/PycharmProjects/curset")
C1 = REPO / "content/age-administrativo-c1/sources"
C2 = REPO / "content/age-auxiliar-c2/sources"
OUT = REPO / "content/aeat-agentes-hacienda/sources"
CHECKS = REPO / "docs/age-verification/aeat/r0a/checks"
HERE = Path(__file__).resolve().parent
SCRATCH = Path(sys.argv[1])
NORMS = SCRATCH.parent / "norms"

# Publication dates of never-amended norms (the consolidated PDF says «sin modificaciones»).
PUBLISHED = {"BOE-A-2021-671": "2021-01-16", "BOE-A-2023-8119": "2023-03-31",
             "BOE-A-2025-25272": "2025-12-11", "BOE-A-2026-23174": "2026-11-05"}

# Original texts of the amending norms that cambios_pendientes point to.
AMENDERS = {"BOE-A-2026-20823": "BOE-A-2026-20823_rdl-29-2026_2026-10-07.pdf",
            "BOE-A-2026-23602": "BOE-A-2026-23602_rdl-33-2026_2026-11-11.pdf",
            "BOE-A-2026-23604": "BOE-A-2026-23604_rdl-35-2026_2026-11-11.pdf",
            "BOE-A-2026-23605": "BOE-A-2026-23605_rdl-36-2026_2026-11-11.pdf",
            "BOE-A-2026-7295": "BOE-A-2026-7295_rd-238-2026-factura-electronica_2026-03-31.pdf"}

L = "Ley 31/2022 (prorrogada)"
COMMON: list[tuple[str, str, list[str], str | None]] = [
    ("BOE-A-1978-31229", "c2", ["I.1", "I.2", "I.3", "I.4", "II.1", "III.1"],
     "Citada en 82 preguntas de 2020–2025. La reforma de 2026 cambia el número de senadores por las Illes Balears (I.2). "
     "Texto de la reforma: sources/normativa/BOE-A-2026-10881_reforma-ce-art-69-3_2026-05-20.pdf (su disposición "
     "transitoria única pospone las circunscripciones de Ibiza y Formentera hasta la convocatoria de las primeras elecciones "
     "al Senado tras su entrada en vigor). Principios impositivos (art. 31) y potestad tributaria (arts. 133 y 134): III.1."),
    ("BOE-A-2024-3099", "c2", ["I.1"], None),
    ("BOE-A-1979-23709", "c2", ["I.1"], None),
    ("BOE-A-1981-10325", "c2", ["I.2"], None),
    ("BOE-A-1982-5196", "c2", ["I.2"],
     "Fuente de 'funcionamiento' del Congreso en I.2. El título en boe.es es el de la Resolución que ordena su publicación."),
    ("BOE-A-1994-10830", "c2", ["I.2"], None),
    ("BOE-A-2026-10881", "c2", ["I.2"], None),
    ("BOE-A-1985-12666", "c2", ["I.2"],
     "La organización judicial de I.2 cambió con la LO 1/2025 (juzgados sustituidos por tribunales de instancia, en tres "
     "fases). Comprobar en boe.es la versión vigente a la fecha del examen."),
    ("BOE-A-1988-29622", "c2", ["I.2"],
     "Incluida porque I.2 pide 'la organización judicial española'; los anexos de planta cambian a menudo y no son materia "
     "de examen."),
    ("BOE-A-2025-76", "c2", ["I.2"], None),
    ("BOE-A-1997-25336", "c2", ["I.3", "II.1"], None),
    ("BOE-A-2015-10566", "c2", ["I.3", "I.5"],
     "Núcleo de I.3 (Administración central y periférica; tipos de entes públicos: sector público institucional) y del "
     "funcionamiento electrónico del sector público de I.5 (arts. 38 a 46). 14 preguntas de 2020–2025."),
    ("BOE-A-2023-23537", "c2", ["I.3"], "Incluido para I.3: fija los ministerios existentes."),
    ("BOE-A-2023-24842", "c2", ["I.3"],
     "Incluido para I.3 (órganos superiores y directivos de cada ministerio). Cambia con frecuencia: solo sirve para "
     "ejemplos, no para preguntas de detalle."),
    ("BOE-A-1985-5392", "c2", ["I.4"],
     "Entidades Locales (I.4). Hay cuestiones y recursos de inconstitucionalidad pendientes sobre la DA 2.7 y la DA 18. "
     "Las Comunidades Autónomas de I.4 se apoyan en la CE y en los 17 Estatutos, que no se listan uno a uno."),
    ("12016M/TXT", "c2", ["I.4", "II.1"], None),
    ("12016E/TXT", "c2", ["I.4", "II.1"], None),
    ("32009D0937", "c2", ["I.4"], None),
    ("12016E/PRO/03", "c2", ["I.4"], None),
    ("12016E/PRO/06", "c2", ["I.4"], None),
    ("BOE-A-2015-10565", "c2", ["I.5", "II.1", "II.2", "II.3", "II.4", "II.5"],
     "Base de I.5 y del bloque II (72 preguntas de 2020–2025). Sin modificaciones de 2025-2026 en boe.es; última "
     "actualización 06-11-2024. STC 55/2018: los arts. 129 (salvo los párrafos segundo y tercero del apartado 4), 130, 132 "
     "y 133 son contrarios al orden constitucional de competencias en los términos de sus FJ 7 b) y c), y son nulos los "
     "incisos «o Consejo de Gobierno respectivo» y «o de las consejerías del Gobierno» del art. 129.4 (notas del texto "
     "consolidado; II.1)."),
    ("BOE-A-2021-5032", "c2", ["I.5", "II.3"], None),
    ("BOE-A-2021-20477", "c2", ["I.5"], "Registro electrónico (I.5). Sin modificaciones: la fecha es la de publicación."),
    ("BOE-A-2013-12887", "c2", ["I.5"],
     "Gobierno abierto, transparencia, acceso a la información y buen gobierno (I.5). El plan de Gobierno Abierto vigente "
     "es un documento, no una norma, y no está en sources/."),
    ("BOE-A-2024-15944", "c2", ["I.5"], None),
    ("BOE-A-2018-16673", "c2", ["I.5"], None),
    ("32016R0679", "c2", ["I.5"], None),
    ("BOE-A-2007-6115", "c2", ["I.6"], None),
    ("BOE-A-2004-21760", "c2", ["I.6"], None),
    ("BOE-A-2022-11589", "c2", ["I.6"], "Igualdad de trato y no discriminación (I.6)."),
    ("BOE-A-2023-5366", "c2", ["I.6"], None),
    ("BOE-A-2013-12632", "c2", ["I.6"], None),
    ("BOE-A-2006-21990", "c2", ["I.6"], None),
    ("BOE-A-2026-20528", "c2", ["I.6"], None),
    ("BOE-A-2015-11719", "c2", ["I.7"], None),
    ("BOE-A-1984-17387", "c2", ["I.7"], None),
    ("BOE-A-1995-8729", "c2", ["I.7"], None),
    ("BOE-A-1995-8730", "c2", ["I.7"], None),
    ("BOE-A-1985-151", "c1", ["I.7"], "Incompatibilidades (I.7; 2021-17, 2023-39). No está en C2."),
    ("BOE-A-1985-7820", "c1", ["I.7"], "Desarrollo de la Ley 53/1984 (I.7). No está en C2."),
    ("BOE-A-1986-1216", "c2", ["I.7"], None),
    ("BOE-A-2023-25758", "c2", ["I.7"], None),
    ("BOE-A-1975-13887", "c2", ["I.7"], None),
    ("BOE-A-2000-12140", "c2", ["I.7"], None),
    ("BOE-A-2003-7527", "c2", ["I.7"], None),
    ("BOE-A-1997-9874", "c2", ["I.7"], None),
    ("BOE-A-1987-12636", "c2", ["I.7"], None),
    ("BOE-A-2015-11724", "c2", ["I.7"], None),
    ("BOE-A-1889-4763", "c1", ["II.1"],
     "Título preliminar (arts. 1 a 7: fuentes, jerarquía y aplicación de las normas), para II.1. No está en C2."),
    ("BOE-A-1998-16718", "c2", ["II.5"],
     "Objeto de la jurisdicción y plazos de interposición del recurso contencioso-administrativo (II.5: arts. 1 a 5 y 46)."),
    ("BOE-A-2003-21614", "c2", ["III.1"], "Hacienda Pública estatal (art. 5; 2020-36), para III.1."),
    ("BOE-A-2022-22128", "c2", ["III.1", "III.3", "III.9", "III.11"], None),
]

sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()  # noqa: E731
copied: dict[str, dict[str, str]] = {}
fresh: dict[str, dict[str, str]] = {}


def copy_from(course: str, name: str) -> str:
    src = (C1 if course == "c1" else C2) / "normativa" / name
    dst = OUT / "normativa" / name
    shutil.copy2(src, dst)
    assert sha(src) == sha(dst), name
    copied[name] = {"from": f"age-{'administrativo-c1' if course == 'c1' else 'auxiliar-c2'}", "sha256": sha(dst)}
    return f"sources/normativa/{name}"


def place_fresh(src: Path, name: str, how: str) -> str:
    dst = OUT / "normativa" / name
    shutil.copy2(src, dst)
    fresh[name] = {"source": how, "sha256": sha(dst)}
    return f"sources/normativa/{name}"


def pdf_date(pdf: Path) -> str | None:
    text = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True).stdout
    m = re.search(r"Última modificación: (sin modificaciones|(\d+) de (\w+) de (\d{4}))", text)
    if not m:
        return None
    if m.group(1) == "sin modificaciones":
        return "sin"
    months = "enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split()
    return f"{m.group(4)}-{months.index(m.group(3)) + 1:02d}-{int(m.group(2)):02d}"


def analysis_lines(rows: list[dict[str, str]]) -> list[str] | None:
    keep = []
    for r in rows:
        rel = r["rel"].strip()
        if rel.startswith("SE DICTA") or rel in ("Recurso", "Cuestión") or "convalidación" in rel:
            continue
        text = re.sub(r"\s+", " ", f"{rel.capitalize()} {r['texto']}").replace(" ,", ",")
        keep.append(f"{text} ({r['id']})")
    return keep or None


def key_of(e: dict[str, object]) -> str:
    return str(e.get("boe_id") or e.get("celex"))


def common_entries(currency: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    sources = {c: {key_of(e): e for e in yaml.safe_load((p / "normativa.yaml").read_text())}
               for c, p in (("c1", C1), ("c2", C2))}
    out = []
    for key, course, temas, note in COMMON:
        e = copy.deepcopy(sources[course][key])
        e["temas"] = temas
        if note:
            e["note"] = note
        e["origen"] = f"copiado de age-{'administrativo-c1' if course == 'c1' else 'auxiliar-c2'} (mismo nombre y sha256)"
        c = currency.get(key)
        newer = bool(c and c["ultima"] and c["ultima"] != e["consolidated_as_of"])
        refs = set(re.findall(r"((?:BOE-A|CELEX)-[\w.-]+\.(?:pdf|html))", yaml.safe_dump(e, allow_unicode=True)))
        if newer:
            assert key in ("BOE-A-2006-21990", "BOE-A-2015-11724"), (key, c["ultima"], e["consolidated_as_of"])
            refs.discard(Path(str(e["file"])).name)
        for r in sorted(refs):
            if ((C1 if course == "c1" else C2) / "normativa" / r).exists():
                copy_from(course, r)
        e.setdefault("cambios_aplicados", e.get("cambios_aplicados") or [])
        out.append(e)
    return out


def refresh_dependency_and_lgss(by: dict[str, dict[str, object]], currency: dict[str, dict[str, object]]) -> None:
    dep, lgss = by["BOE-A-2006-21990"], by["BOE-A-2015-11724"]
    for e, slug, amender, amend_line, pend in (
        (dep, "ley-dependencia", "BOE-A-2026-23605",
         "Real Decreto-ley 36/2026, de 10 de noviembre (BOE-A-2026-23605): disposición final 1.ª, apartados 2 y 3 (plazo "
         "máximo de tres meses para resolver la prestación de dependencia; PENDIENTE: en vigor el 12-11-2026)",
         {"norma": "Real Decreto-ley 36/2026, de 10 de noviembre", "boe_id": "BOE-A-2026-23605",
          "precepto_modificador": "disposición final primera", "publicada": "2026-11-11", "en_vigor": "2026-11-12",
          "articulos": ["disposición final 1.ª, apartados 2 y 3 (plazo de tres meses desde la solicitud para resolver el "
                        "reconocimiento de la prestación y fecha de generación del derecho)"]}),
        (lgss, "lgss", "BOE-A-2026-23604",
         "Real Decreto-ley 35/2026, de 10 de noviembre (BOE-A-2026-23604): art. 71.1.h) (datos de títulos de familias "
         "numerosas y monoparentales; PENDIENTE: en vigor el 12-11-2026)",
         {"norma": "Real Decreto-ley 35/2026, de 10 de noviembre", "boe_id": "BOE-A-2026-23604",
          "precepto_modificador": "disposición final tercera", "publicada": "2026-11-11", "en_vigor": "2026-11-12",
          "articulos": ["art. 71.1.h) (suministro de datos de las comunidades autónomas a las entidades gestoras)"]}),
    ):
        key = key_of(e)
        ultima = str(currency[key]["ultima"])
        src = SCRATCH / "dl" / f"{key}-consolidado.pdf"
        assert pdf_date(src) == ultima, key
        old = e["consolidated_as_of"]
        e["consolidated_as_of"] = ultima
        e["file"] = place_fresh(src, f"{key}_{slug}_{ultima}.pdf", f"https://www.boe.es/buscar/pdf/{key[6:10]}/{key}-consolidado.pdf")
        e["origen"] = (f"descarga nueva el {TODAY}: boe.es tiene una consolidación posterior a la copia de C2 ({old}); "
                       "los demás ficheros que cita la entrada, copiados de age-auxiliar-c2 (mismo nombre y sha256)")
        e["amended_2025_2026"] = list(e.get("amended_2025_2026") or []) + [amend_line]
        pend["file"] = place_fresh(SCRATCH / "dl" / f"{amender}.pdf", AMENDERS[amender],
                                   f"https://www.boe.es/boe/dias/2026/11/11/pdfs/{amender}.pdf")
        e["cambios_pendientes"] = list(e.get("cambios_pendientes") or []) + [pend]
        e["tags"] = ["cambio-pendiente"]
    dep["note"] = ((dep.get("note") or "") + " RDL 36/2026 publicado el 11-11-2026, en vigor el 12-11-2026, pendiente de "
                   "convalidación.").strip()
    dep["version_vigente"] = {
        "consolidated_as_of": dep["consolidated_as_of"],
        "note": "Ley 4/2026 en vigor desde el 23-10-2026 (integrada). El fichero integra sin aviso la redacción de la "
                "disposición final 1.ª.2 y 3 del RDL 36/2026, que rige desde el 12-11-2026; el texto vigente el 11-11-2026 "
                "de esos apartados no está en el fichero (comprobado 2026-11-11)."}
    lgss["note"] = ("Régimen de Seguridad Social de los funcionarios (I.7). RDL 31/2026 (BOE-A-2026-21872) en vigor el 21-10-2026 y RDL 35/2026 "
                    "(BOE-A-2026-23604) en vigor el 12-11-2026: ninguno convalidado por el Congreso (art. 86.2 CE) en el BOE "
                    "a 11-11-2026; si se derogan, sus preceptos vuelven a la redacción anterior.")
    lgss["version_vigente"] = {
        "consolidated_as_of": lgss["consolidated_as_of"],
        "note": "Como en C2: los preceptos del RDL 31/2026 con efectos futuros (arts. 144.4, 169.1.a), 171, 172, 173.1 y "
                "309.1) llevan el aviso «Téngase en cuenta…» y la «Redacción anterior», vigente hoy (comprobado 2026-11-11). "
                "El art. 71.1.h) en la redacción del RDL 35/2026 (en vigor 12-11-2026) va integrado sin aviso."}


def pge(e: dict[str, object]) -> None:
    e["tags"] = ["anual"]
    e["note"] = ("No hay Ley de PGE para 2024, 2025 ni 2026 en boe.es (búsqueda en la API de legislación consolidada, "
                 "2026-11-11; la última orden de elaboración es la de los PGE para 2027, Orden HAC/557/2026): rige la de "
                 "2023 prorrogada (CE art. 134.4). Sus disposiciones adicionales fijan las cifras anuales de este curso "
                 "(cifras_anuales). El RDL 3/2026 (BOE-A-2026-2548, convalidado) prorroga para 2026 los títulos IV y VIII "
                 "(pensiones y cotizaciones). La API marca una actualización de 10-11-2026 que act.php aún no muestra "
                 "(«Última actualización publicada el 30/09/2026»).")
    e["cifras_anuales"] = [
        {"cifra": "Interés legal del dinero", "valor_2026": "3,25 %", "norma": L, "boe_id": "BOE-A-2022-22128",
         "precepto": "disposición adicional cuadragésima segunda, apartado Uno", "desde": "2023-01-01",
         "nota": "Fijado «hasta el 31 de diciembre del año 2023» y aplicado desde entonces por la prórroga de los PGE; "
                 "ninguna norma de 2024–2026 fija otro (análisis de la Ley 31/2022 en boe.es)."},
        {"cifra": "Interés de demora tributario (art. 26.6 LGT)", "valor_2026": "4,0625 %", "norma": L,
         "boe_id": "BOE-A-2022-22128", "precepto": "disposición adicional cuadragésima segunda, apartado Dos",
         "desde": "2023-01-01", "nota": "Igual que el interés legal: aplicado por la prórroga."},
        {"cifra": "Interés de demora de las subvenciones (art. 38.2 Ley 38/2003)", "valor_2026": "4,0625 %", "norma": L,
         "boe_id": "BOE-A-2022-22128", "precepto": "disposición adicional cuadragésima segunda, apartado Tres",
         "desde": "2023-01-01"},
        {"cifra": "Indicador público de renta de efectos múltiples (IPREM)",
         "valor_2026": "20 euros/día; 600 euros/mes; 7.200 euros/año; 8.400 euros/año cuando la norma sustituida se refiere "
                       "al SMI anual sin excluir las pagas extraordinarias",
         "norma": L, "boe_id": "BOE-A-2022-22128", "precepto": "disposición adicional nonagésima", "desde": "2023-01-01",
         "nota": "Fijado «durante 2023» y aplicado por la prórroga. Búsqueda de texto completo en la legislación consolidada "
                 "publicada de 2025-01-01 a 2026-11-11 («indicador público de renta de efectos múltiples»): ninguna norma "
                 "fija otra cuantía."},
    ]


def new_entries(currency: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    data = yaml.safe_load((HERE / "aeat_new.yaml").read_text())
    out = []
    for d in data:
        if d.get("celex"):
            out.append(eu_entry(d))
            continue
        i = d["boe_id"]
        c = currency[i]
        assert c["found"] and not c["derogada"], i
        if d["src"] == "norms":
            stage = SCRATCH / "dl" / f"{i}-consolidado.pdf"
            shutil.copy2(NORMS / f"{i}.pdf", stage)
            how = f"https://www.boe.es/buscar/pdf/{i[6:10]}/{i}-consolidado.pdf (descargado el {TODAY})"
        else:
            stage = SCRATCH / "dl" / f"{i}-consolidado.pdf"
            how = f"https://www.boe.es/buscar/pdf/{i[6:10]}/{i}-consolidado.pdf"
        date = c["ultima"] or PUBLISHED[i]
        got = pdf_date(stage)
        assert got == (c["ultima"] or "sin"), (i, got, c["ultima"])
        e: dict[str, object] = {"short": d["short"]}
        if d.get("aliases"):
            e["aliases"] = d["aliases"]
        e.update({"title": c["title"], "boe_id": i, "url": f"https://www.boe.es/buscar/act.php?id={i}",
                  "consolidated_as_of": date, "temas": d["temas"],
                  "amended_2025_2026": analysis_lines(c["amended_2025_2026"]), "note": d["note"], "unverified": False})
        e["file"] = place_fresh(stage, f"{i}_{d['slug']}_{date}.pdf", how)
        pend = copy.deepcopy(d.get("cambios_pendientes") or [])
        for p in pend:
            name = AMENDERS[p["boe_id"]]
            place_fresh(SCRATCH / "dl" / f"{p['boe_id']}.pdf", name, "PDF del diario oficial (boe.es/boe/dias/…)")
        e["tags"] = (["cambio-pendiente"] if pend else []) + d.get("extra_tags", [])
        vv: dict[str, object] = {"consolidated_as_of": date}
        if d.get("version_vigente_note"):
            vv["note"] = d["version_vigente_note"]
        e["version_vigente"] = vv
        e["cambios_pendientes"] = pend
        e["cambios_aplicados"] = []
        e["origen"] = f"descarga nueva el {TODAY} (ni C1 ni C2 la tienen)"
        if d.get("cifras_anuales"):
            e["cifras_anuales"] = d["cifras_anuales"]
        out.append(e)
    return out


def eu_entry(d: dict[str, object]) -> dict[str, object]:
    e: dict[str, object] = {"short": d["short"], "aliases": d["aliases"], "title": d["title"], "boe_id": None,
                            "celex": d["celex"], "url": f"https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:{d['celex']}",
                            "consolidated_as_of": d["consolidated_as_of"], "temas": d["temas"],
                            "amended_2025_2026": d["amended_2025_2026"], "note": d["note"], "unverified": False}
    consol = re.search(r"CELEX-(\w+-\d{8})", str(d["eu_file"])).group(1)
    e["file"] = place_fresh(SCRATCH / str(d["eu_src"]), str(d["eu_file"]),
                            f"http://publications.europa.eu/resource/celex/{consol} (Cellar, {TODAY})")
    pend = d.get("cambios_pendientes") or []
    e["tags"] = ["cambio-pendiente"] if pend else []
    e["version_vigente"] = {"consolidated_as_of": d["consolidated_as_of"], "note": d["version_vigente_note"]}
    e["cambios_pendientes"] = pend
    e["cambios_aplicados"] = []
    e["origen"] = f"descarga nueva el {TODAY} (ni C1 ni C2 la tienen)"
    return e


ORDER = ["short", "aliases", "title", "boe_id", "celex", "url", "consolidated_as_of", "temas", "amended_2025_2026", "note",
         "unverified", "file", "tags", "version_vigente", "cambios_pendientes", "cambios_aplicados", "origen", "cifras_anuales"]
BLOQUES = {"I": "Organización del Estado y funcionamiento de la Administración General del Estado",
           "II": "Derecho Administrativo General",
           "III": "Organización de la Hacienda Pública y Derecho Tributario"}


def tema_key(t: str) -> tuple[int, int]:
    b, n = t.split(".")
    return (["I", "II", "III"].index(b), int(n))


def main() -> None:
    (OUT / "normativa").mkdir(parents=True, exist_ok=True)
    currency = json.loads((SCRATCH / "currency_raw.json").read_text())
    currency.update(json.loads((SCRATCH / "extra" / "currency_raw.json").read_text()))
    common = common_entries(currency)
    by = {key_of(e): e for e in common}
    refresh_dependency_and_lgss(by, currency)
    pge(by["BOE-A-2022-22128"])
    entries = common + new_entries(currency)
    entries = [{k: e[k] for k in ORDER if k in e} | {k: v for k, v in e.items() if k not in ORDER} for e in entries]
    for e in entries:
        e["temas"] = sorted(e["temas"], key=tema_key)
    entries.sort(key=lambda e: tema_key(min(e["temas"], key=tema_key)))
    header = (HERE / "header.txt").read_text().replace("@@COPIED@@", str(len(copied))).replace("@@FRESH@@", str(len(fresh)))
    body, last = "", None
    for e in entries:
        b = min(e["temas"], key=tema_key).split(".")[0]
        if b != last:
            body += f"\n# {'=' * 70}\n# Bloque {b}. {BLOQUES[b]}\n# {'=' * 70}\n\n"
            last = b
        body += yaml.safe_dump([e], allow_unicode=True, sort_keys=False, width=200) + "\n"
    (OUT / "normativa.yaml").write_text(header + body)
    files_on_disk = sorted(p.name for p in (OUT / "normativa").iterdir())
    referenced = sorted({Path(f).name for f in re.findall(r"((?:BOE-A|CELEX)-[\w.-]+\.(?:pdf|html))", body)})
    report = {
        "built": TODAY,
        "entries": len(entries),
        "entries_boe": sum(1 for e in entries if e.get("boe_id")),
        "entries_eu": sum(1 for e in entries if e.get("celex")),
        "entries_not_located": sum(1 for e in entries if not e.get("file")),
        "entries_list": [{"short": e["short"], "id": key_of(e), "temas": e["temas"], "consolidated_as_of": e["consolidated_as_of"],
                          "file": e.get("file"), "tags": e.get("tags"), "origen": e.get("origen")} for e in entries],
        "copied": copied,
        "fresh": fresh,
        "files_on_disk": len(files_on_disk),
        "files_not_referenced_in_yaml": sorted(set(files_on_disk) - set(referenced)),
        "files_referenced_missing": sorted(set(referenced) - set(files_on_disk)),
        "unverified": [{"short": e["short"], "id": key_of(e), "note": e.get("note")} for e in entries if e.get("unverified")],
        "cambio_pendiente": [{"short": e["short"], "id": key_of(e),
                              "pendientes": [{"norma": p["norma"], "en_vigor": p["en_vigor"], "articulos": p["articulos"]}
                                             for p in e["cambios_pendientes"]]}
                             for e in entries if e.get("cambios_pendientes")],
    }
    (CHECKS / "norm_build_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=1))
    print("entries", len(entries), "copied", len(copied), "fresh", len(fresh), "on disk", len(files_on_disk),
          "unreferenced", report["files_not_referenced_in_yaml"], "missing", report["files_referenced_missing"])


if __name__ == "__main__":
    main()
