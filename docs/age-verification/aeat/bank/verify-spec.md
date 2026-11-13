# Verifier spec — AEAT question bank, authored questions (round R3, stage 2)

You verify questions written for `content/aeat-agentes-hacienda` (repo `/home/juanjo/PycharmProjects/curset`). You are
blind: you did not write them, and you do **not** read the writer's notes before your verdicts. Do not commit. Write
only your report and your lines in `docs/age-verification/aeat/bank/drops.tsv`.

Read `docs/aeat-exam-style.md` (§ 2, 3, 6, 9, 12) once. Sources: `content/aeat-agentes-hacienda/sources/normativa/`
(`pdftotext -layout`; `sources/normativa.yaml` names the file and its «Cambio pendiente» rule). Open the text yourself;
do not trust `source_quote`. Never use an official answer key as evidence of the right answer.

## Checks (every question, all five)

1. **Key correct** by the cited text, in the version in force on 2026-11-12 (a `cambio-pendiente` provision uses the
   later version only if the question says so).
2. **Exactly one option correct**: no other option is defensible under the same text or another norm in force. For each
   distractor name the sentence of the source that makes it wrong.
3. **Citation contains the answer**: the article/paragraph cited carries the fact and the lesson cites it
   (`uv run python ../docs/age-verification/aeat/bank/tools/check_draft.py <draft>` from `backend/`: 0 anchor misses).
4. **AEAT style** (checklist § 12, all 17 items as they apply): stem names the norm by its BOE title and the article;
   stem and option lengths; no forbidden options; negative stems in capitals; the key not systematically the longest;
   distractors one or two patterns, wrong by the text; options share form; organ names current; annual figures name
   their year; programme scope (item 14); no official erratum; the explanation says why the key is right and why every
   distractor is wrong without naming options by letter or position.
5. **Not official**: not a copy or light rewording of an official question of the tema's pack
   `docs/age-verification/aeat/r2/questions/<lesson>.md` or of `sources/examenes-oficiales/`: same stem and option set,
   or the same fact, angle and key with an official distractor carried over, fails; the same fact with new options and
   angle passes.

Further, always:

- **RDL 29/2026 held:** a question that rests on a precept RDL 29/2026 changed (revert list
  `docs/age-verification/aeat/r1/rdl-29-2026-revert-list.md`) FAILS check 3 with reason «held RDL 29/2026».
- **Doubtful keys:** a question that rests on the facts of official items 2024-43, 2022X-69, 2025-20, 2025-24, 2023-80,
  2022X-88 FAILS check 5 with reason «doubtful official key».
- **Computations (`cómputo`):** recompute the result **independently** from the stem's data and the norm, with the
  calendar (art. 30 LPAC, art. 48 LGT counting; fractions of month per art. 26 LGT where it applies); a different
  result, a missing date or amount, or a step the explanation skips FAILS check 1 or 4.
- **Supuestos:** fictional taxpayers; every fact needed is in the stem.

Any FAIL drops the question. You do not fix it and do not propose a corrected one.

## Batches and report

A batch is up to 60 questions with the same cited unit or neighbouring ones, as the coordinator assigns (ids in
`verify/<lesson>[.tag].v<k>.ids`). Report `docs/age-verification/aeat/bank/verify/<lesson>[.tag].v<k>.md`:

| id | 1 key | 2 unique | 3 citation | 4 style | 5 not official | verdict | reason |
|---|---|---|---|---|---|---|---|

then the summary: checked, PASS, FAIL by first failing check. Append one line per FAIL to
`docs/age-verification/aeat/bank/drops.tsv` (`id<TAB>tema<TAB>batch<TAB>check<TAB>reason`, with `>>`, never rewrite).
Write the report after each batch. Final message: counts and the failing ids with their check.

## Amendment (Juanjo, 2026-11-12): the doubtful official keys

An official key is never the source of a fact, but a point the norm states clearly **can** be asked, keyed by the norm
text alone. A question on a point of one of the six flagged keys (2024-43, 2022X-69, 2025-20, 2025-24, 2023-80, 2022X-88)
no longer fails check 5 for that reason; it must end its explanation with one sentence «En el examen <año> (pregunta N) la
plantilla oficial dio otra respuesta; esta pregunta sigue el texto del artículo.» and passes or fails on the norm like any
other (checks 1–5). A copy of the official question itself still fails check 5.
