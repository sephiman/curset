# Full pass: norm excerpts of the affected kinds (step 5, 2026-10-30)

The 2026-10-30 sample of 100 norm excerpts of bloques I–V (`../report-8.md`) missed 4 %, all in two kinds of
citation: several articles in one citation («arts. 43.2 y 44.2 LGP»), and units of an annex (classification codes,
notes). `batch-01.jsonl` holds every bloque I–V question of those two kinds: 56 excerpts.

Per item: does `excerpt_text` contain the fact the key rests on? **yes** / **full-only** (only in `excerpt_full`) /
**no**. For full-only and no, open the norm under `content/age-administrativo-c1/sources/normativa/` and give
**where**: the article, annex entry or paragraph that holds the fact, quoted; or **not in the norm**.
Work from the item and the norm only; no code, no reports. Return the non-«yes» rows and counts that match them.
