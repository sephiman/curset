# Explanation rewrite brief — R3 close (2026-10-27)

User decision: an explanation that repeats one sentence for several distractors, or rules a distractor out only by the
source's silence («la página no menciona…», «el artículo no recoge…», «no figura en…»), does not meet the style guide
(`docs/age-exam-style.md` § 12, item 17: why the key is right and why **each** distractor is wrong). Rewrite the
**explanation only** — never the stem, options, key, citation or any other field.

Input: a list `style-scan-<set>.json` of question ids flagged by a scan (pattern `silence` and/or `repeat`). The
questions are in `<bloque>/<lesson>.draft.json` (bloque VI: `bloque-vi/m06-lNN.draft.json`).

For each id:
1. Read the question and its cited source (the norm article with `pdftotext -layout`, or the saved page in
   `content/age-administrativo-c1/sources/otros/` — extract HTML to text).
2. Decide:
   - **rewrite** — some distractor is dismissed only by silence, or the same sentence is reused for several
     distractors. Write a new explanation in the course voice (`docs/prose-voice.md`; Peninsular Spanish): say why the
     key is right (quote the source briefly), then **for each distractor, name it by its content and give the source
     sentence that makes it wrong** — the key's own figure, organ or rule when the source states it ("el artículo fija
     un mes; quince días no es ese plazo" is acceptable only if the article's sentence is quoted or paraphrased), or
     another sentence of the same source or of another saved page/norm the lesson cites. Every claim must be on the
     source. If, for some distractor, no source sentence makes it wrong, do not invent one: mark the id **unsupported**
     with the distractor and stop for that id (the coordinator will have it re-verified).
   - **keep** — the flagged phrase is there but each distractor already has a positive reason and no sentence is
     reused. Say which reason covers each distractor.
3. No explanation names an option by letter or position, and none uses a bare demonstrative («Esa opción…»).

Output: `style-rewrites-<set>.json`, a list of `{"id", "decision": "rewrite"|"keep"|"unsupported", "old", "new"
(rewrite only), "note"}`; written by script (`json.dump`, `ensure_ascii=False`, `indent=1`). Keep scripts and
extracts in your scratchpad subfolder. Append one line per 50 ids to the end of `docs/age-bank-ledger.md` with `>>`.
Final message: counts by decision, and the unsupported ids with their distractor.
