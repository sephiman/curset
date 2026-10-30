"""Write kept-index.tsv: every kept case question (case, id, tema, citation, key), so writers see what is taken."""

import json
from pathlib import Path

from case_check import CASES, kept

rows = ["case\tid\ttema\tcitation\tkey\tprompt"]
for draft in sorted(CASES.glob("sp-[0-9][0-9].draft.json")):
    case = json.loads(draft.read_text(encoding="utf-8"))
    for q in kept(case):
        rows.append("\t".join([case["case"], q["id"], q["tema"], q["citation"], q["options"][q["correct"]],
                               " ".join(q["prompt"].split())[:160]]))
(CASES / "kept-index.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
print(len(rows) - 1, "kept questions indexed")
