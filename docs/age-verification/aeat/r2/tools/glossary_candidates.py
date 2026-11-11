"""C2/C1 glossary entries the AEAT common temas can copy under R2.3: term used in an AEAT lesson, cited files identical.

C2 is tried first, then C1. Kept under C1's rule: two AEAT lessons use the term, or one does and the definition cites
the article that defines it. Origin: the first AEAT lesson (programme order) that uses the term. Writes the candidates
as TSV to stdout; `--write` also rewrites glossary.yaml and the provenance record docs/age-verification/aeat/r2/glossary.md.
"""

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "backend"))
from scripts.provenance import GlossaryEntry  # noqa: E402
from tests.pipeline_courses import course_dir, pipeline_courses  # noqa: E402
from tradeschool.content.yaml_file import read_yaml  # noqa: E402

RECORD = ROOT / "docs/age-verification/aeat/r2/glossary.md"
OVERRIDES = yaml.safe_load((ROOT / "docs/age-verification/aeat/r2/glossary-overrides.yaml").read_text())
C2_REPORT = "docs/age-verification/c2/bloque-i/glossary.md"
CITES_ARTICLE = re.compile(r"\((?:art|arts|disposición)\.? ")


def main(write: bool) -> None:
    courses = {c.slug: c for c in pipeline_courses()}
    target = courses["aeat-agentes-hacienda"]
    root = course_dir(target)
    lessons = {p.stem: p.read_text().lower() for p in sorted((root / "es/lessons").glob("m0[12]-l*.md"))}
    c1_record = {
        line.split("`")[1]: line
        for line in (ROOT / C2_REPORT).read_text().splitlines()
        if line.startswith("- `g-")
    }
    chosen: dict[str, tuple[str, dict[str, object], str]] = {}
    for tag, slug in (("C2", "age-auxiliar-c2"), ("C1", "age-administrativo-c1")):
        source = courses[slug]
        source_root = course_dir(source)
        for raw in read_yaml(source_root / "glossary.yaml")["terms"]:  # type: ignore[index]
            if raw.get("alias_of") or raw["id"] in chosen:
                continue
            term = str(raw["es"]).lower()
            pattern = re.compile(r"(?<!\w)" + re.escape(term) + r"(?!\w)")
            using = [lid for lid, text in lessons.items() if pattern.search(text)]
            if not using:
                continue
            here = GlossaryEntry.of(raw, target.citations.norms, root)
            there = GlossaryEntry.of(raw, source.citations.norms, source_root)
            same = here.keys is not None and (here.texts, here.keys) == (there.texts, there.keys)
            definition = str(raw.get("definition", {}).get("es", ""))
            keep = same and (len(using) >= 2 or bool(CITES_ARTICLE.search(definition)))
            print(f"{raw['id']}\t{tag}\t{'keep' if keep else 'skip'}\t{','.join(using)}")
            if keep:
                chosen[str(raw["id"])] = (tag, raw, using[0])
    if not write:
        return
    order = {lid: n for n, lid in enumerate(lessons)}
    terms = []
    record = []
    for gid, (tag, raw, origin) in sorted(chosen.items(), key=lambda kv: (order[kv[1][2]], kv[0])):
        entry = {k: v for k, v in raw.items() if k not in ("link_except",)}
        entry["origin"] = origin
        entry.update(OVERRIDES.get(gid, {}))
        terms.append(entry)
        if tag == "C2":
            # C2's own glossary entries are all inherited from C1 (C2 R2); the C1 report stands, through C2.
            line = c1_record.get(gid, "")
            report = line.split("verificado en C1: ")[1].split(" · ")[0] if line else C2_REPORT
            record.append(f"- `{gid}` · verificado en C2: {C2_REPORT} · C2 origin {raw.get('origin')} · C1 {report}")
        else:
            record.append(f"- `{gid}` · verificado en C1: docs/age-theory-ledger.md · C1 origin {raw.get('origin')}")
    head = (
        "# SPDX-License-Identifier: AGPL-3.0-only\n"
        "# aeat-agentes-hacienda glossary. Same rules as content/crypto-futures/glossary.yaml: the glossary refers, it does\n"
        "# not teach; ids are permanent; origin names the lesson that teaches the term; the glossary never coins.\n"
        "# Round R2, common part (2026-11-11): entries copied from age-auxiliar-c2 or age-administrativo-c1 under R2.3 (same\n"
        "# term, definition, citations and cited-file sha256); provenance in docs/age-verification/aeat/r2/glossary.md.\n"
    )
    (root / "glossary.yaml").write_text(
        head + yaml.safe_dump({"terms": terms}, allow_unicode=True, sort_keys=False, width=120)
    )
    RECORD.write_text(
        "# Registro de procedencia — glosario de aeat-agentes-hacienda (parte común)\n\n"
        "R2.3: cada entrada copiada de C2 o de C1 con el mismo término, la misma definición, las mismas citas y los "
        "ficheros citados con el mismo sha256 lleva «verificado en C2» o «verificado en C1». Generado por "
        "`docs/age-verification/aeat/r2/tools/glossary_candidates.py --write`; lo comprueba "
        "`backend/tests/test_provenance.py`.\n\n"
        f"Entradas: {len(terms)} · heredadas: {len(terms)} · verificadas: 0.\n\n" + "\n".join(record) + "\n"
    )
    print(f"{len(terms)} entries written", file=sys.stderr)


if __name__ == "__main__":
    main("--write" in sys.argv)
