# Defect sweep — literal text of the lessons (edition step 2, before the layer)

You work on the lessons assigned to you, in `content/aeat-agentes-hacienda/es/lessons/<lesson>.md`. Read `docs/prose-voice.md` and
`CLAUDE.md` first. The pool (the full R2d lesson, every sentence verified) is `docs/age-verification/aeat/pool/<lesson>.md`.
Cited article text: `uv run --project backend python docs/age-verification/aeat/edition/tools/article_text.py <lesson>` only covers
what the explanation layer cites; for any other article use `source-index.json` (content/aeat-agentes-hacienda/) with
`pdftotext -f P -l P -layout <pdf> -` as that script does (import its `article(pdf, number)`; run from `edition/tools`).

Four kinds of defect to find and FIX (smallest edit that cures it), then report counts:
1. **Worked example not one unit.** Each «### Ejemplo: …» section must be whole: a scenario with facts, ALL its steps in
   order and numbered 1..n without gaps, and the result. If steps/scenario are missing or orphaned: restore the whole example
   byte-identical from the pool if the pool has it whole; otherwise remove the whole example section (heading and everything).
   Never leave a stub, a gap in numbering, or a step without its scenario. Check every step's arithmetic and dates.
2. **Esquema vs prose.** Every `:::esquema` (tabla, etc.) and the prose/bullets about the same article must agree on every
   figure, plazo, percentage, condition. Where they differ, read the norm text and correct the WRONG one (edit the minimum
   words; a corrected figure keeps the sentence otherwise as is). Do not "average" — the norm decides.
3. **Sentence under the wrong heading.** A sentence about article X sits under the heading of article/topic X. A sentence
   that states art. 188.2 or 27.2 under «Principio de responsabilidad», say, moves under the heading of its own article
   (move whole sentences; if no heading fits, put it at the end of the section that treats its article). Moving keeps text.
4. **Calificación missing.** Where the norm gives a calificación (leve/grave/muy grave) or a sanction scale for an
   infraction, the infraction's esquema row/sentence must carry it. Add it from the norm text, quoting the norm, with
   citation. (E.g. arts. 191.4, 193.4 LGT.)

Rules: you may only change sentences by (a) moving them, (b) deleting a whole example, (c) restoring from the pool, or
(d) a minimal correction/addition whose wording is lifted from the norm text and ends with the same kind of citation
«(art. N LGT)». Spanish Peninsular, no invented terms. Do not touch «Normativa», overviews, `:::note` blocks beyond what a
defect needs. Do not run provenance, do not commit, do not run test suites. Do not use git checkout/stash/reset.

Log: write `docs/age-verification/aeat/edition/defects/<lesson>.md` for each lesson: a section per defect `## D<n> kind <1-4>`
with: where (heading), what was wrong (quote), the norm text that decides (quote), the fix; and under `### Changed sentences`
a list `- BEFORE: … / AFTER: …` for every sentence whose text changed or is new (not for pure moves, deletions or byte-identical
restores). If nothing found for a lesson, write «none» for each kind. Also state for each lesson: number of examples
checked, esquemas checked.
Reply with counts per kind per lesson, and the list of changed sentences' count.
