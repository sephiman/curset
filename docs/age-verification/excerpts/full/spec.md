# Full verification of saved-page excerpts (2026-10-30)

Every bloque VI excerpt of `age-administrativo-c1`, plus the 12 bloque I saved-page excerpts the 2026-10-30
extractor change touched: 1,855 excerpts in `batch-01.jsonl` … `batch-31.jsonl`, 60 per batch. Each excerpt is what
the solution panel shows after the question is answered: text extracted by a program from the course's saved copy
of the page the question cites.

## One question per item

Does `excerpt_text` contain the fact the key rests on, i.e. the text a reader needs to see that the marked option
is right?

- **yes**: it does (garbled spacing copied from the page does not matter).
- **no**: it does not. Then open the cited file under `content/age-administrativo-c1/sources/otros/` (or
  `sources/normativa/`) and give **where**: the sentence of the page that holds the fact, quoted, and the text of
  the nearest heading above it; or **not on page** if the saved page does not state it.

Work from the item and the cited file only; do not read code, other batches' reports or anything else.

## Output (returned as text; the coordinator saves it as `report-NN.md`)

`n | key | verdict | where (for no)` — one row per item, then the counts.
