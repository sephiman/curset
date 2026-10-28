# Blind check of re-cited excerpts (2026-10-30)

141 questions whose excerpt missed the fact in the full pass were re-cited: the citation now points at the page's own
sentence or table row that holds the fact (question text and key unchanged). `batch-01..03.jsonl` hold the rebuilt
excerpts. Same question as the full pass: does `excerpt_text` (or, for a norm, `excerpt_full`) contain the fact the
key rests on? Verdicts **yes** / **no**; for **no**, say what is missing. Work from the item and the cited source
under `content/age-administrativo-c1/sources/` only; no code, no reports. Return the «no» rows and counts that match.
