# Excerpt re-check after platform delta v2.1 M (2026-11-12)

The citation grammar now reads compound disposición ordinals («trigésima segunda») and the C1 source index now places
`art-unico`. Rebuilding `excerpts.json` changed the text of two C1 excerpts: `m05-l04-q037` (it quoted DA 30.ª, now
DA 32.ª) and `m04-l07-q001` (the preámbulo no longer runs on into «Artículo único»). C2's `m01-l14-q356` is the same
question as C1's `m05-l04-q037` and is checked in `c2/bank/excerpts/m-round/`.

Input: `sample.jsonl` (items 401–402), fields as in `../verifier-spec.md`, plus `source_file`. Question and verdicts as
in `../verifier-spec.md` (yes / full-only / no, plus flags). Output: `report.md`, one row per item.
