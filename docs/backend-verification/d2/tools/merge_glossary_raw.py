# SPDX-License-Identifier: AGPL-3.0-only
"""Append verified glossary candidates to the course glossary: merge_glossary_raw.py MODULE (reads d2 work files).

Candidates are read as raw text because a definition holds commas inside a flow mapping; ids with a fail line in
<module>.glossary.verdicts.tsv, and ids already present, are skipped.
"""

import glob
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[4]
D = REPO / "docs/_work/backend-in-depth/d2"
module = sys.argv[1]
failed = {line.split("\t")[0] for line in (D / f"{module}.glossary.verdicts.tsv").read_text().splitlines() if "\tfail" in line}
path = REPO / "content/backend-in-depth/glossary.yaml"
text = path.read_text(encoding="utf-8")
present = {t["id"] for t in yaml.safe_load(text)["terms"]}
blocks = []
for f in sorted(glob.glob(str(D / f"{module}-l*.glossary.yaml"))):
    entry: dict[str, str] = {}
    for line in Path(f).read_text(encoding="utf-8").splitlines() + ["- id: END"]:
        m = re.match(r"- id: (\S+)", line)
        if m:
            if entry.get("id") and entry["id"] not in failed | present and "definition" in entry:
                body = yaml.safe_dump([{"id": entry["id"], "en": entry["term"], "origin": entry["origin"],
                                        "definition": {"en": entry["definition"]}}], allow_unicode=True,
                                       sort_keys=False, width=110)
                blocks.append(f"# {entry['citation']}\n{body}")
                present.add(entry["id"])
            entry = {"id": m.group(1)}
            continue
        for key, pattern in (("term", r"\s+term: \{en: (.*)\}\s*$"), ("definition", r"\s+definition: \{en: (.*)\}\s*$")):
            m = re.match(pattern, line)
            if m:
                entry[key] = m.group(1).strip().strip('"')
        for key in ("origin", "citation"):
            m = re.match(rf"\s+{key}: (.*)$", line)
            if m:
                entry[key] = m.group(1).strip().strip('"')
path.write_text(text.rstrip("\n") + "\n\n" + "\n".join(blocks), encoding="utf-8")
print(f"{module}: merged {len(blocks)}")
