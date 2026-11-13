# Question bank plan — aeat-agentes-hacienda (round R3, stage 2)

2026-11-12. Requirements v1.1 § 6 (R6.1), R2.3 (provenance), R3.5 (annual figures); style guide `docs/aeat-exam-style.md`
(§ 12 reviewer checklist, statistics); ledger `docs/aeat-bank-ledger.md`. Working files and reports:
`docs/age-verification/aeat/bank/` (`tools/`, `writer-spec.md`, `verify-spec.md`, `style-check-brief.md`, `derived/`,
`delta/`, `style/`, `verify/`, `provenance/`). Method as `docs/age-c2-bank-plan.md`.

## 1. Size and shares at publication

5,000 questions for the first exercise, four options, one correct, a quarter-point penalty (BOE-A-2025-27056, base 6.2).
Quotas are the kept count each tema must reach; a tema may end slightly above its quota after its last replacements.

| Part | Quota | Share |
|---|---|---|
| I (I.1–I.7) | 800 | 16.0 % |
| II (II.1–II.5) | 693 | 13.9 % |
| III (III.1–III.20) | 3,507 | 70.1 % |

## 2. Per-tema quotas

Weights are the questions per tema of the last four convocatorias (OEP 2022–2025 with the 2022 extraordinario; ledger
«Questions per tema per exam», total column, 462 questions). 5,000 is apportioned in proportion, floor 50, largest
remainders (`tools/quotas.py`; no tema needed the floor: III.6 and III.17, the lightest, get 87).

| Tema | Weight | Quota | | Tema | Weight | Quota |
|---|---|---|---|---|---|---|
| I.1 | 9 | 97 | | III.1 | 9 | 97 |
| I.2 | 9 | 97 | | III.2 | 9 | 97 |
| I.3 | 13 | 141 | | III.3 | 13 | 141 |
| I.4 | 13 | 141 | | III.4 | 32 | 346 |
| I.5 | 10 | 108 | | III.5 | 22 | 238 |
| I.6 | 9 | 97 | | III.6 | 8 | 87 |
| I.7 | 11 | 119 | | III.7 | 16 | 173 |
| II.1 | 9 | 97 | | III.8 | 23 | 249 |
| II.2 | 14 | 152 | | III.9 | 16 | 173 |
| II.3 | 14 | 152 | | III.10 | 10 | 108 |
| II.4 | 15 | 162 | | III.11 | 11 | 119 |
| II.5 | 12 | 130 | | III.12 | 24 | 260 |
| | | | | III.13 | 20 | 217 |
| | | | | III.14 | 18 | 195 |
| | | | | III.15 | 24 | 260 |
| | | | | III.16 | 16 | 173 |
| | | | | III.17 | 8 | 87 |
| | | | | III.18 | 15 | 162 |
| | | | | III.19 | 19 | 206 |
| | | | | III.20 | 11 | 119 |

## 3. Stem-form mix, article naming, negatives, key position

Per tema, each stem form ends within ±10 points of the 2025 share (style guide § 2), classified by `tools/aeat_stats.py`
(a writer's own `stem_form` field wins):

| Form | 2025 % |
|---|---|
| según el artículo X … (completar, «:») | 39 |
| señale la respuesta CORRECTA / INCORRECTA | 23 |
| pregunta directa ¿…? | 11 |
| supuesto breve con datos | 10 |
| según el artículo X …, ¿…? | 9 |
| ¿cuál de las siguientes…? | 9 |
| norma sin artículo / enunciado a completar | 0 |

The article is named in 91 % of 2025 stems (target, ±10). Negative stems: at most one in 20 of a tema, in capitals. The
key is the longest option in about a quarter of a tema (±3); slot and length-edge z within ±1.5 per tema (C1 guards).
Options: four, one correct; never «ninguna», «todas», a combination or an article number.

## 4. Derivation first (common temas I.1–II.5), writing second (the delta and all of III)

1. **Script-derived candidates** (`tools/derive_candidates.py`, no model): every kept C1 and C2 question (built YAML)
   whose citation resolves to an anchor of an AEAT common lesson fed from the question's lesson (R2 `derivation.yaml`),
   with every cited file at the same sha256 in both snapshots and a PASS report for its id in its origin course. Text
   verbatim; record «verificado en C1|C2: <report>». A question in both origins is taken once. First run: 2,087
   candidates (`derivation.md`).
2. **Mechanical style** (`tools/mechanical_style.py`: checklist 2 acronyms, 4, 5, 10) → `drops.tsv`. Then up to 1.3 ×
   quota candidates per tema are pooled (anchors round-robin, forms up to share + 10, keys-not-longest first); the rest
   stay in `held.tsv` («not pooled») as a reserve and are style-checked only if a pooled one fails and a replacement
   is needed.
3. **AEAT style check** of the pool (Sonnet, `style-check-brief.md`): failing candidates are dropped, never rewritten.
4. **Trim to quota** (`plan_delta.py kept`); the surplus goes to the reserve (`held.tsv`, «over quota»).
5. **Writers (Sonnet)** author the delta of I/II and all of III, per tema and part (`writer-spec.md`), source = the
   lesson's cited text in this snapshot. **Verifiers (Opus, blind)**, batches of 60 grouped by cited unit
   (`verify-spec.md`): key, uniqueness, citation, style, not official, computations recomputed. A FAIL drops the
   question; replacements are re-verified; verified questions are never deleted.
6. **Holds.** No question on a precept RDL 29/2026 changed (`tools/rdl_held.py` and the verifiers); held ones are listed
   in the ledger. The six doubtful official keys are not a source of facts.

## 5. Build (all behind the build step; the course stays published without exercises until then)

Nothing under `content/aeat-agentes-hacienda/` changes until the final build: drafts, kept sets and provenance live in
`docs/age-verification/aeat/bank/`. The build (`tools/build_exercises.py`, C2's, course-parameterised) writes the exercise
YAML, the `exercises:` entries in `course.yaml`, `exercise_types: [quiz]`, `lesson_practice: true`, the excerpts and the
provenance records; then the cross-reference, bias guards, goldens read, and `docs/age-verification/aeat/tools/close_round.sh`
(backend, frontend, `tsc -b`, Android bundle byte-identical, C1, C2 and crypto-futures unchanged).

## 6. Estimate

Common temas: ~1,300 candidates style-checked, ≈ 300 to author (II.1–II.5, I.6 gap). Tax temas: 3,507 to author, ≈ 4,030
written to absorb drops, ≈ 4,300 verified. About 3–5 windows (requirements § 9).
