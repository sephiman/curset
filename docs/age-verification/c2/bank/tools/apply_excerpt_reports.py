"""Apply blind excerpt-check reports: re-cite a miss to the verifier's label, or record it as «sin extracto».

Run from the repo root: `python3 docs/age-verification/c2/bank/tools/apply_excerpt_reports.py <bloque> <report.md> …`.
A «no» row with a label (or «cite: <citation>», for a norm) rewrites the question's citation to «fuente: `file`; «label»» in every draft JSON of the bloque
that holds the id (text and key unchanged) and logs it in `excerpts/<bloque>-recited.tsv`; a «none: reason» row is
added to `content/age-auxiliar-c2/excerpt-exclusions.yaml`. Idempotent.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
BANK = ROOT / "docs" / "age-verification" / "c2" / "bank"
EXCLUSIONS = ROOT / "content" / "age-auxiliar-c2" / "excerpt-exclusions.yaml"
ROW = re.compile(r"^\|?\s*\d+\s*\|\s*([\w-]+-q\d+)\s*\|\s*(yes|no)\s*\|\s*(.*?)\s*\|(.*)$")
SOURCE = re.compile(r"^fuente: `([^`]+)`")


def rows(report: Path) -> list[tuple[str, str, str]]:
    out = []
    for line in report.read_text(encoding="utf-8").splitlines():
        match = ROW.match(line)
        if match:
            out.append((match.group(1), match.group(2), match.group(3).strip()))
    return out


def recite(folder: Path, qid: str, label: str, whole: str | None = None) -> tuple[str, str]:
    """Point the citation at `label` on the cited page, or replace it by `whole` (a norm unit)."""
    old = new = ""
    for path in sorted(folder.glob("*.json")):
        questions = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for q in questions:
            if q["id"] != qid:
                continue
            match = SOURCE.match(q["citation"])
            if whole is None and not match:
                raise ValueError(f"{qid}: a label for a norm citation: {q['citation']}")
            old = q["citation"]
            new = whole if whole is not None else f"fuente: `{match.group(1)}`; «{label}»"  # type: ignore[union-attr]
            changed = q["citation"] != new
            q["citation"] = new
        if changed:
            path.write_text(json.dumps(questions, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    assert new, f"{qid} not found in {folder}"
    return old, new


def main(bloque: str, reports: list[str]) -> None:
    folder = BANK / bloque
    log = BANK / "excerpts" / f"{bloque}-recited.tsv"
    logged = log.read_text(encoding="utf-8").splitlines() if log.exists() else ["id\told citation\tnew citation\treport"]
    data = yaml.safe_load(EXCLUSIONS.read_text(encoding="utf-8")) if EXCLUSIONS.exists() else None
    exclusions = (data or {}).get("questions") or []
    excluded = {e["question"] for e in exclusions}
    recited = none = 0
    for report in map(Path, reports):
        for qid, verdict, answer in rows(report):
            if verdict == "yes":
                continue
            if answer.startswith("none"):
                if qid not in excluded:
                    reason = answer.split(":", 1)[1].strip() if ":" in answer else answer
                    exclusions.append({"question": qid, "reason": f"blind excerpt check: {reason}"})
                    excluded.add(qid)
                none += 1
                continue
            try:
                if answer.startswith("cite:"):
                    old, new = recite(folder, qid, "", answer.split(":", 1)[1].strip())
                else:
                    old, new = recite(folder, qid, answer)
            except ValueError as problem:
                print(f"skipped: {problem}")
                continue
            logged = [r for r in logged if not r.startswith(qid + "\t")] + [f"{qid}\t{old}\t{new}\t{report.name}"]
            recited += 1
    log.write_text("\n".join(logged) + "\n", encoding="utf-8")
    header = (
        "# SPDX-License-Identifier: AGPL-3.0-only\n"
        "# Questions a blind verifier found no citable paragraph for: built as «sin extracto» (reason code no-fact).\n"
        "# Reports: docs/age-verification/c2/bank/excerpts/.\n"
    )
    EXCLUSIONS.write_text(header + yaml.safe_dump({"questions": exclusions}, allow_unicode=True, sort_keys=False),
                          encoding="utf-8")
    print(f"re-cited {recited}, sin extracto {none}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
