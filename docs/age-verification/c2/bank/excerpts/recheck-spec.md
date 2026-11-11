# Blind recheck of re-cited excerpts — age-auxiliar-c2 (round R3, 2026-11-10)

Questions whose excerpt missed the fact were re-cited: the citation now names the page's own sentence or table row
that holds the fact (question text and key unchanged). `<bloque>/recheck/batch-NN.jsonl` holds the rebuilt excerpts,
same fields as `spec.md`. One question per item: does `excerpt_text` contain the fact the key rests on, i.e. the text
a reader needs to see that the marked option is right? **yes** / **no**; for **no**, say in one line what is missing.
Flag garbled text or an excerpt that is not the unit its heading names. Work from the item and the cited file under
`content/age-auxiliar-c2/sources/` only: no code, no other reports.

Output `<bloque>/recheck/report-NN.md`: `n | key | verdict | note` per item, then the counts.
