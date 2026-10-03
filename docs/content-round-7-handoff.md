<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# Content round 7 — fixes from the prose inventory, handoff

These are the four content errors listed in `docs/prose-inventory.md`, section "Out of scope but found while
reading". **Nothing is committed.** Six lesson files changed, one line each. Nothing else under
`content/` moved.

## 1. m11-l1 S098: the wrong side of the RSI trade (both locales)

**Confirmed.** The paragraph before it is the worked example of the overbought reflex: a beginner shorts
an alt in a strong uptrend at 1,20 / 1,35 / 1,50 «porque está en sobrecompra» and gets stopped out three
times. S098 then says «El reflejo funciona al revés igual de caro», so it should describe the mirror case:
going **long** into a strong downtrend because RSI is oversold. Instead the sentence said to go *short*.
That is a trade with the trend, and it is no reason to act on an oversold reading at all. The rest of the
paragraph ("an extreme reading tells you the move is one-sided; it never tells you the move is about to
end") argues against fading the trend in either direction, so the fix is the direction word only.

| | before | after |
| --- | --- | --- |
| ES | El reflejo funciona al revés igual de caro: ponerte **corto** contra una tendencia bajista fuerte porque "el RSI está en sobreventa" simplemente le regala tu stop a la tendencia. | El reflejo funciona al revés igual de caro: ponerte **largo** contra una tendencia bajista fuerte porque "el RSI está en sobreventa" simplemente le regala tu stop a la tendencia. |
| EN | The reflex runs in reverse just as expensively — **shorting** into a strong downtrend because "RSI is oversold" simply hands your stop to the trend. | The reflex runs in reverse just as expensively — **going long** into a strong downtrend because "RSI is oversold" simply hands your stop to the trend. |

Every other word is unchanged. «Largo» and «going long» are not glossary match forms. `g-long` matches
«largos / en largo / un largo» and «longs / go long / long position(s)», so no glossary mark moved. EN
"going long" mirrors ES «ponerte largo».

## 2. m12-l1 ES: «e mostrar» → «y mostrar»

> …seguir subiendo, mostrar otra, seguir subiendo **y** mostrar una tercera; …

## 3. m17-l1 ES: duplicated «riesgo»

> …sube cuando los inversores están cómodos asumiendo riesgos ~~riesgo~~ y baja cuando huyen hacia la seguridad…

The EN line («comfortable taking risk») was already right.

## 4. m10-l1: the cut idiom (both locales)

The intended idiom is «las dos caras de la misma moneda» / "two sides of the same coin". The sentence says
two mistakes are one error seen from two sides, and the next sentence names the two versions (whipsaw and
buying late).

| | before | after |
| --- | --- | --- |
| ES | Los dos errores clásicos son en realidad la misma moneda. | Los dos errores clásicos son en realidad las dos caras de la misma moneda. |
| EN | The two classic mistakes are really the same coin. | The two classic mistakes are really two sides of the same coin. |

These two lines now run past the usual ~100-column wrap. I left them unwrapped so the diff stays one line
per fix. No check enforces the width.

## Verification

All green. Everything outside the expected set is byte-identical.

| Check | Result |
| --- | --- |
| `export_bundle.py`, format **2**, to `dist/bundle/` | Exit 0. Text diff 0 (prose and glossary multisets, every lesson block for block). Block inventory OK (88 ASTs). Exercise refs OK (242 marks). Fingerprint `b752db33e7004dfa…` (round 6b) → **`9e7facd5f0a3502d…`** |
| per-file diff against the round-6b bundle | **8 files moved, all expected:** `ast/en/{m10-l1,m11-l1}.json`, `ast/es/{m10-l1,m11-l1,m12-l1,m17-l1}.json`, `manifest.json` (fingerprint + `files` hashes; nothing else in it changed) and `reading-seconds.json`. Everything else is byte-identical |
| `reading-seconds.json` | Only **m10-l1** moved: ES 670 → 671, EN 593 → 594 (three added words). m11-l1, m12-l1 and m17-l1 changed by 0 or ±1 word, which does not move their rounded seconds |
| `export_generation_goldens.py` | `exercise-mode.tsv`, `figures.tsv`, `formatter-cases.tsv`, `configs/`: **zero diff** against the pre-round copy. No recapture |
| `verify_golden_stability.py` | Exit 0. **90 committed fingerprints hold** (84 golden + 6 pinned). Generation digest `6999679392b682a2…`, unchanged |
| `glossary-links.{es,en}.txt` | **byte-identical**. Not regenerated; the report test passes against them |
| `lesson-refs.{es,en}.txt` | **byte-identical**. The refs report test passes |
| figure/prose coupling | `test_figure_prose_coupling.py` passes inside the backend suite. No figure-anchored number or guard phrase is near these edits |
| backend `pytest` (whole suite) | **1300 passed, 20 skipped** |
| frontend `vitest` (whole suite, incl. both report tests) | **458 passed, 1 skipped** |

No guard, threshold, pin or golden was changed.

## Files

Modified: `content/es/lessons/{m10-l1,m11-l1,m12-l1,m17-l1}.md`, `content/en/lessons/{m10-l1,m11-l1}.md`.
New: `docs/content-round-7-handoff.md`. The bundle was re-exported to `dist/bundle/` (gitignored).
`docs/prose-inventory.md` (the previous session's untracked output) is untouched. Its appendix still quotes
the pre-fix sentences, because it is a snapshot of `f0d0e68`.
