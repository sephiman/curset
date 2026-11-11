# Question bank plan — age-auxiliar-c2 (round R3)

2026-11-07. Requirements v1.2 section 5 (R5.1, R5.2 → C1 section 5) and R2.3 (provenance); style guide
`docs/age-c2-exam-style.md` (reviewer checklist § 12, statistics); ledger `docs/age-c2-bank-ledger.md`. Working files
and reports: `docs/age-verification/c2/bank/`.

## 1. Size and shares at publication

| Part | Questions | Share | Requirement |
|---|---|---|---|
| Bloque I (knowledge, part 1) | 2,582 | 51.6 % | ≥ 50 % |
| Bloque II (knowledge, part 2) | 2,384 | 47.7 % | ≥ 45 % |
| Psicotécnico calibration items | 34 | 0.7 % | the rest |
| **Total** | **5,000** | | 5,000 |

Quotas are the kept count each tema must reach. A tema may end slightly above its quota after the replacements of
its last batch. Neither bloque may end below its share.

**Calibration items.** One stored item per generator level: 13 generators, 34 levels (tablas-lectura, the four cálculo
types, serie-numerica, verbal-definicion and administrativo-clasificacion have three; administrativo-ordenacion,
atencion-codificacion and the sinónimos, antónimos and ortografía types have two). Each is a generated item frozen with its seed, level and computed key. They are used only by the
official-exam practice set and the tests, never by a draw: simulations and «Psicotécnicos» practice keep generating.
They are built last, after bloque I, so they come from the generators as reviewed (codificación recalibrated
2026-11-07). The platform side (a stored item of type `psicotecnico` outside the draw pools) is checked then. If it
needs a platform change, that change goes to the next platform round and the items wait.

Amended 2026-11-07 (Juanjo): bloque II built at 2,384 to pass the course-level answer-bias guard; bloque I's quota
rises by 66 to keep 5,000 (ledger «Bloque II built»). The 66 go to I.13 (+31) and I.14 (+35), filled from their
held, already style-checked C1 candidates (ledger «Session 2»); the other bloque I quotas are unchanged.

## 2. Per-tema quotas

The weights are the questions per tema in 2022–2025 (style guide, «Questions per tema per exam», total column). The
OEP 2020 sets are «programa anterior» and are not counted. Each bloque's total is apportioned in proportion to them,
with a floor of 50 (largest remainders). No tema needed the floor: I.12, the lightest, gets 58.

| Tema | Weight | Quota | | Tema | Weight | Quota |
|---|---|---|---|---|---|---|
| I.1 | 7 | 136 | | II.1 | 9 | 100 |
| I.2 | 9 | 174 | | II.2 | 11 | 123 |
| I.3 | 6 | 116 | | II.3 | 11 | 122 |
| I.4 | 7 | 135 | | II.4 | 16 | 178 |
| I.5 | 10 | 194 | | II.5 | 23 | 256 |
| I.6 | 5 | 97 | | II.6 | 14 | 156 |
| I.7 | 7 | 135 | | II.7 | 24 | 267 |
| I.8 | 11 | 213 | | II.8 | 21 | 234 |
| I.9 | 6 | 116 | | II.9 | 26 | 290 |
| I.10 | 8 | 155 | | II.10 | 20 | 223 |
| I.11 | 15 | 290 | | II.11 | 20 | 223 |
| I.12 | 3 | 58 | | II.12 | 25 | 278 |
| I.13 | 9 | 205 | | | | |
| I.14 | 10 | 229 | | | | |
| I.15 | 8 | 155 | | | | |
| I.16 | 9 | 174 | | | | |
| **I** | **130** | **2,582** | | **II** | **220** | **2,450** |

## 3. Stem-form mix and article naming

Per tema, each stem-form share ends within ±10 points of the 2025 share of its set (style guide § Statistics),
classified from the stem by `tools/c2_stats.py`:

| Form | Bloque I | II.1–II.4 | Ofimática (II.5–II.12) |
|---|---|---|---|
| según el artículo X … (completar) | 41 | 8 | – |
| según la norma (sin artículo) … (completar) | 6 | 58 | – |
| ¿cuál de las siguientes…? | 22 | 0 | 37 |
| según el artículo X … ¿? | 6 | 0 | – |
| señale/marque la correcta | 12 | 0 | 5 |
| según la norma (sin artículo) … ¿? | 6 | 0 | – |
| enunciado a completar | 3 | 0 | 2 |
| pregunta directa ¿…? | 3 | 33 | 56 |

The stems naming an article are the share the guide states for 2025: bloque I 69 % (22 of 32), II.1–II.4 8 % (1 of 12),
ofimática none. These shares are targets checked per tema like the mix (±10). Negative stems: at most one per 20
questions of a tema, with the negative word in capitals. In ofimática, at most one per application per 20. The key is
the longest option in no more than about a quarter of a tema's questions. Bias guards are as in C1 (slot z and
length-edge z within ±1.5 per tema before the build).

## 4. Derivation first, writing second

1. **Script-derived candidates** (`tools/derive_candidates.py`, no model). Every kept C1 question, from the bank and
   the cases, is mapped to the C2 lessons its C1 lesson feeds (the R2 bloque specs' mapping). It becomes a candidate
   when its citation resolves to an anchor of that C2 lesson and every cited file has the same sha256 in both
   snapshots. Stem, options, key, explanation and citation are copied verbatim. The record reads «verificado en C1:
   <report>», where the report is the newest C1 report with a PASS row for that id. First run: bloque I 2,115
   candidates, bloque II 1,603 (`c2/bank/<bloque>/derivation.md`).
2. **C2 style check of every candidate.** First `tools/mechanical_style.py`, for the checklist items a script decides:
   2 (stem ending), 3 (forbidden options), 14 and 21 (lengths), and 6 (flag only). Then a Sonnet check for the rest
   of the C2 checklist: 2, 4, 6, 7 against the C2 official pack of the tema, 8, 9, 10, 13, 15, 16 and the
   Windows 10 / one-Outlook part of 17. A question must also stand without a case scenario. A failing candidate is
   dropped, never rewritten. Items 1, 11, 12, 18 and 19 are not checked again: C1's verification of the same text
   against the same file stands (R2.3).
3. **Trim to quota.** Where a tema's surviving candidates exceed its quota (bloque I: I.11, I.13, I.14, I.15 on the
   first run), a script keeps up to the quota. It fills each stem form only up to its target share plus 10, chooses
   round-robin across the lesson's anchors so coverage stays wide, and prefers candidates whose key is not the
   longest option. The rest are **held, not dropped** (`held.tsv`), available to the variant rounds. Without the trim,
   bloque I would end near 3,000 and bloque II below 45 %.
4. **Writers (Sonnet) author only the delta.** They write the facts the C2 lesson states that no kept candidate tests,
   every «Lo que más cae» line not yet tested, the C2 official facts of the tema (the R2 question packs), and the stem
   forms the mix still needs. Rules are C1's R3: the source is the lesson's cited text in this course's snapshot,
   never the official keys; four options; distractor patterns of the guide (§ 6); no official copies; explanations
   name options by content, never by letter; keys not systematically longest; fields `id`, `tema`, `section`,
   `citation`, `stem_form`, `names_article`, `negative`, `prompt`, `options`, `correct`, `difficulty`, `tags`,
   `distractor_pattern`, `explanation`, `source_quote`, `covers`, `lesson_anchor`; old organ names current; date
   computations show the calendar. Ids continue each lesson's numbering after the derived candidates. Dropped ids are
   never reused.
5. **Verification (Opus, blind, batches of up to 60 grouped by cited unit).** Every authored question goes through
   the five checks: the key is correct by the cited text; exactly one option is correct; the citation contains the
   answer; C2 style (checklist § 12); not an official copy. Derived candidates skip the five checks by provenance.
   Failures are dropped, not fixed, and replacements are verified again.
6. **Bias and distribution** per tema after verification (`c2_stats.py`, the C1 slot and length-edge guards).
7. **Build per bloque.** Exercise YAML and course.yaml entries (the C1 builder taking the course as a parameter),
   loader, cross-reference (every citation resolves in its own lesson), bias guards, i18n, excerpts. Authored
   questions' excerpts are checked blind. A derived question inherits C1's excerpt check when the excerpt text is
   identical, and is checked otherwise. Goldens are read. C1, crypto-futures and Android must stay unchanged. Full
   suites run via `docs/age-verification/c2/tools/close_round.sh`.

## 5. Order and sessions

Bloque II first: the largest derivation, from C1's bloque VI. Bloque I second, then the calibration items. Inside a
bloque the order is tema by tema, and a session stops at a tema boundary. Agents follow `CLAUDE.md`: writers Sonnet,
verifiers Opus (the step-2 style check is Sonnet, as the round brief says), at most four at once (two writers, two
checkers). Progress goes to the ledger after every part.

## 6. Bloque I built short of quota (Juanjo, 2026-11-10)

Bloque I is built at **2,312** (quota 2,582). The writers stopped where the C2 lesson ran out of facts at C2 depth
(every further question would have repeated a fact from an angle already used), and verification dropped what
failed. Variant rounds close the gap: other stem forms and angles of facts already tested (R5.1), and facts any
later lesson round adds.

| Tema | Kept | Quota | Short | Reason |
|---|---|---|---|---|
| I.1 | 101 | 136 | 35 | lesson out of facts at C2 depth |
| I.2 | 131 | 174 | 43 | lesson out of facts at C2 depth |
| I.4 | 129 | 135 | 6 | lesson out of facts at C2 depth (art. 561.1's catch-all left out) |
| I.5 | 96 | 194 | 98 | lesson out of facts at C2 depth |
| I.8 | 187 | 213 | 26 | lesson out of facts at C2 depth |
| I.10 | 119 | 155 | 36 | lesson out of facts at C2 depth |
| I.16 | 112 | 174 | 62 | lesson out of facts at C2 depth |

The other nine temas are at or over quota. With bloque II at 2,384 and 34 calibration items, the bank is 4,730 and
bloque I's share 48.9 %, under § 1's 50 % until the variant rounds. Residuals left for the variant round to
rebalance (recorded, within the course limit ±3): length-edge z I.1 −2.59, I.4 −1.82, I.16 +1.86; I.6 stem mix
(art-completar 15/41, señale 26/12; the lesson has few articles); I.7 art-completar 52/41 and I.11 directa 14/3
(one point over each).
