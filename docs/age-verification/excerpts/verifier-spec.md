# Excerpt verification — spec (platform delta F3, 2026-10-28)

Each question of `age-administrativo-c1` now shows, after it is answered, an excerpt of the source it cites
(the norm's text, or two sentences of a saved documentation page). The excerpt is extracted by a program from
the course's own copies of the sources. This check measures the extractor, not the questions.

## Input

`sample-1.jsonl` and `sample-2.jsonl` in this folder: 100 excerpts drawn at random (seed 20261028) from the
5,184 the extractor produced. One JSON object per line:

| field | meaning |
|---|---|
| `n` | item number, 1–100 |
| `key` | question id |
| `prompt`, `options` | the question; `correct: true` marks the key |
| `explanation` | the question's explanation |
| `citation` | what the question cites |
| `excerpt_heading` | heading shown above the excerpt |
| `excerpt_text` | the excerpt as shown (at most 200 words; «[…]» marks a cut) |
| `excerpt_full` | the whole unit, shown behind «Ver artículo completo»; null when the excerpt is the whole unit or the unit is too long |
| `attribution` | page title and date, documentation pages only |

## The question to answer per item

Does `excerpt_text` contain the fact the key rests on, i.e. the text a reader needs to see that the marked
option is right? Judge `excerpt_text` alone; note separately whether `excerpt_full` contains it.

- **yes**: the fact is in `excerpt_text`.
- **full-only**: not in `excerpt_text`, but in `excerpt_full`.
- **no**: in neither. Say what the excerpt shows instead (wrong article, wrong paragraph, cut before the fact,
  navigation text, a heading only, garbled text) — that is the extractor bug to fix.

Also flag, whatever the verdict: text that is garbled (words run together or split, page headers or footers
inside, markers such as «►M1»), or an excerpt that is not the unit its heading names.

Work from the sample only; do not read the extractor's code. The source files are under
`content/age-administrativo-c1/sources/` if you need to see what the right text would have been.

## Output

`report-<part>.md` in this folder: one table row per item — `n | key | verdict | note` — then a short list of
the misses and flags grouped by cause.

## Pass 2 (2026-10-29)

Same question and the same verdicts as above. Inputs, built from the rebuilt `excerpts.json`:

- `sample-3.jsonl`, items 101–126: 26 excerpts re-drawn on purpose (they are not random). Judge them exactly as
  the others.
- `sample-4.jsonl`, items 127–176: 50 excerpts at random (seed 20261029) from bloque VI (`m06-*`), none of them
  in samples 1–2.

Output: `report-3.md` and `report-4.md`, same format.
- `sample-5.jsonl`, items from 177: the excerpts whose text changed after a verifier last judged them (re-drawn on
  purpose). Output `report-5.md`.
- `sample-6.jsonl`, items 188–237: 50 at random (seed 20261030) from bloque VI, none of them in samples 1–5.
  Output `report-6.md`.
- `sample-7.jsonl`, items 238–287: 50 at random (seed 20261031) from bloque VI, none of them in samples 1–6.
  Output `report-7.md`.
- `sample-8.jsonl`, items 301–400: 100 at random (seed 20261101) from the norm (BOE, DOUE) excerpts of bloques I–V,
  none of them in samples 1–7. Output `report-8.md`.
