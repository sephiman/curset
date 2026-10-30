# Excerpt check — case questions (R4, 2026-10-30)

The question and verdicts of `docs/age-verification/excerpts/verifier-spec.md` (read it): does `excerpt_text` contain
the fact the key rests on — the text a reader needs to see that the marked option is right? Judge `excerpt_text`
alone; note separately whether `excerpt_full` contains it.

- **yes**: the fact is in `excerpt_text`.
- **full-only**: not in `excerpt_text`, but in `excerpt_full`.
- **no**: in neither. Say what the excerpt shows instead and where the fact is (another article or apartado of the
  same norm, another norm, the scenario only).

Case questions differ from bank questions in one way: the answer comes from the norm **applied to the scenario's
facts**. The excerpt only has to hold the rule the key applies (the plazo, the percentage, the organ, the
condition), not the case's dates or figures; a date computation is «yes» when the excerpt states the plazo and its
kind of day as the explanation uses them. The scenario is in each item for context only.

Also flag, whatever the verdict: garbled text (words run together or split, page headers inside, markers such as
«►M1») or an excerpt that is not the unit its heading names.

Input: `batch-NN.jsonl` in this folder. Work from the batch; open the source files under
`content/age-administrativo-c1/sources/` only to say where a missing fact is. Do not read the extractor's code.

Output: `report-NN.md` per batch — one row per item `n | key | verdict | note` — then the misses and flags grouped by
cause.
