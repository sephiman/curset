# Platform delta — handoff (exam presets, cases, source links, results by lesson, esquemas)

Round of 2026-10-18 for `docs/curset-platform-delta-exams.md` v1.2, sections A–E. Nothing committed. Steps 1–9
of the round prompt are done in one session; the inventory written first is `docs/platform-delta-inventory.md`.

## Status by step

| Step | State |
|---|---|
| 1 Inventory | `docs/platform-delta-inventory.md` |
| 2 A presets | done; crypto-futures golden written before the move and unchanged after it |
| 3 B case | done (schema, loader, practice view, exam "choose one of N", reports, PDF + bijection, per-question shuffle, stats per tema) |
| 4 C links | done; AGE regenerated (step 8) |
| 5 D by lesson | done (exam results, lists, Progress cumulative, retroactive) |
| 6 E esquema | done (four kinds, web + PDF, checks) |
| 7 Tests | done, counts below |
| 8 AGE regenerate | done: anchors for every citation, text unchanged, existing goldens unmoved |
| 9 CI, goldens, stability, Android | done, results below |

## Schema reference

### `exams:` in `course.yaml`

```yaml
exams:
- id: simulacro            # permanent; a sitting stores it
  version: 1               # bump when the rules change; a sitting stores it and a snapshot of the rules
  title: {es: Simulacro}
  time_limit_minutes: 100  # whole exam, parts run together; omit for untimed
  parts:
  - id: parte-1
    title: {es: Primera parte}
    source: course         # course | cases | {block: id} | {module: id} | {lesson: id} | {each: block|module|lesson}
    draw: random           # random (default) | per-module (one per module with a bank; no `questions`)
    questions: 70          # counted questions (per case, for a case part)
    reserve: 2             # shown last, never counted
    penalty: 1/3           # 0 | 1/4 | 1/3 per wrong answer
    blank: free            # free | wrong (a blank is penalized like a wrong answer)
    scoring: {max: 50, pass_minimum: 25, minimum_raw: 35}   # CPS transform; omit for raw only
  - id: parte-2
    source: cases
    choose: 2              # cases offered; exactly one must be marked to grade the part
    questions: 20
    penalty: 1/3
    scoring: {max: 50, pass_minimum: 25, minimum_raw: 10}
    requires_previous_pass: true
```

Transform (pinned by `exams/scoring.py` and the m00-l01 example, 46 raw → 34,35): `d < M: P·d/M`;
`d ≥ M: P + (d − M)(E − P)/(N − M)`; negative raw → 0. The load fails if a fixed preset's pool cannot supply
it or a parametric one has no target that can. API: `GET /exams/presets`, `POST /exams {presetId, target}`
(the old `{scope, blockId}` still maps to crypto's two presets), `PUT /exams/{id}/parts/{part}/cases
{exerciseIds}`; sessions carry `deadline` and `serverNow`.

### `case` exercise

```yaml
type: case
title: {es: El permiso denegado}
scenario: {es: "Una funcionaria … recibe el 3 de marzo una resolución expresa …"}   # Markdown, no figures
questions:                       # 10–25, fixed order
- id: q01
  lesson: m01-l1                 # lesson KEY it counts under and links to
  prompt: {es: "¿Ante quién se interpone el recurso?"}
  options:
  - {id: a, text: {es: "Ante el órgano superior jerárquico."}, correct: true}
  - {id: b, text: {es: "Ante el mismo órgano."}}
  explanation: {es: "…"}
  citation: "art. 121.1 LPAC"
  difficulty: 2
  tags: [órgano]
```

Quiz variants now take `citation`, `difficulty`, `tags` too (excluded from the Android dump). Practice:
`POST /exercises/{id}/case-attempts` opens one attempt per question (`attempts.question_id`, migration
`e7f8a9b0c1d2`), each answered through `/attempts/{id}/answer`.

### Citation anchors

Lesson text «… plazo de un mes (art. 122.1 LPAC).» → the API's lesson detail ships

```json
{"text": "art. 122.1 LPAC", "section": "prose", "ids": ["lpac-art-122"],
 "href": "/api/courses/fixture-oposiciones/sources/normativa/lpac-extracto.html#a1-22",
 "title": "Ley 39/2015, de 1 de octubre, … (texto consolidado a 2024-11-06)"}
```

Anchor = `<norm slug>-<unit>`: norm slug is the acronym in `short` (`lpac`, `ce`), else the number form
(`lo-3-1981`), else the short name (`codigo-civil`); units are `art-67`, `art-610-bis`, `da-cuarta`,
`dt-unica`, `df`, `dd-1`, `anexo-i`, `apartado-9`, `preambulo`; source files are `fuente-<file>`. The first
prose citation of an anchor carries the DOM id. A question's citation resolves to its own anchor, or to the
first `arts. a–b` range covering it. `normativa.yaml` entries accept an optional `aliases: [...]`.

### Source page index (`content/<slug>/source-index.json`, from `scripts/index_sources.py`)

```json
{"files": {
  "sources/normativa/lpac-extracto.html": {"sha256": "462d…", "units": {"art-121": "a1-21", "art-122": "a1-22"}},
  "sources/normativa/lrjsp-extracto.pdf":  {"sha256": "fff7…", "units": {"art-9": 2, "art-10": 3}}}}
```

PDF units come from body headings («Artículo 67.», «Disposición adicional cuarta», «Preámbulo», «ANEXO I»),
skipping index pages (three or more dot-leader lines); HTML units from BOE block ids followed by their `<h5>`.
A test fails when an indexed file's sha256 no longer matches. Sources are served at
`/api/courses/{course}/sources/{normativa|otros}/{file}` (auth; HTML with `Content-Security-Policy: sandbox`).

### `::esquema`

```markdown
:::esquema{kind=tabla title="Los dos recursos administrativos"}
| Recurso | Ante quién se presenta | Plazo con acto expreso | Artículo |
|---|---|---|---|
| Alzada | Órgano superior jerárquico | Un mes | art. 122.1 LPAC |
:::

:::esquema{kind=plazos title="Plazos del recurso de alzada"}
1. Interposición — un mes (art. 122.1 LPAC)
2. Resolución — tres meses (art. 122.2 LPAC)
:::

:::esquema{kind=pasos title="Cómo se interpone una alzada"}
1. Presentación — escrito de recurso — órgano que dictó el acto o el que debe resolverlo (art. 121.2 LPAC)
:::

:::esquema{kind=arbol title="Quién decide"}
- Órgano delegante (art. 9.1 LRJSP)
  - Órgano delegado — sus resoluciones se consideran dictadas por el delegante (art. 9.4 LRJSP)
:::
```

All four live in `backend/tests/fixtures/content/fixture-oposiciones/es/lessons/m02-l1.md`.

## What moved where

- Backend: `exams/presets.py` (schema), `exams/draw.py` (pools, draws, load check), `exams/scoring.py`,
  `exams/results.py` (stored result; the old blob kept byte for byte for unscored presets), `exams/layout.py`,
  `exams/service.py` (rewritten around presets), `exercises/case.py`, `citations/` (`grammar.py` — the one
  citation parser, `norms.py`, `lesson.py`, `sources.py`, `course.py`), `content/esquema.py`, `content/text.py`
  (LocalizedText moved out of `schema.py` to break an import cycle), `stats/by_lesson.py`,
  `scripts/index_sources.py`; `pypdf` added to the dev group (build-time indexing only).
- Frontend: `lib/citations/annotate.ts` (marks the backend's citations; never detects), `lib/esquema.ts` +
  `lib/EsquemaBlock.tsx`, `features/exams/*` (presets list, clock, parts, case marks, scores),
  `features/byLesson/ByLessonTable.tsx`, `features/exercises/{CaseExercise,CaseScenario,LessonLink}.tsx`,
  PDF in `lib/pdf/{markdown,exercises,document,labels}.ts`.
- Content: crypto-futures `course.yaml` gets its two presets; the fixture course gains m02, banks, two cases,
  presets, sources, `lesson_noun: tema`, goldens. AGE: only generated files added
  (`source-index.json`, `citations.es.txt`).
- Fixed on the way: every single-choice question shared one radio group name, so on a page with two quizzes
  (or a case) a choice in one cleared another (`CaseExercise.test.tsx` fails without the fix).

## Tests

- Backend: 1,449 passed, 20 skipped (full suite, testcontainers). New: `test_exam_crypto_golden` 1,
  `test_exam_presets` 12, `test_cases` 9, `test_citations` 32, `test_exam_scoring` 12, `test_esquema` 9.
- Frontend: 592 passed, 51 skipped. New: `lib/citations/annotate.test.ts` 7 (incl. every AGE and fixture
  golden row placed with no text change), `ExamReview.test.tsx` 5, `CaseExercise.test.tsx` 4,
  `markdown.citations.test.tsx` 5, `lib/pdf/case-esquema.test.ts` 6, `ExamPage.test.tsx` +2 (rewritten for presets).
- ruff, ruff format, mypy (strict) clean; `npm run build` (tsc + vite) clean.

## AGE (step 8)

Regenerated as draft. 3,204 prose citations (2,777 to norms, 427 to `sources/otros/` files) and 208 «Normativa»
norms; every citation has an anchor: 1,441 distinct anchor names, 1,589 anchor ids across 45 lessons. 2,605 of
the 2,777 norm citations open at a page or HTML anchor, 122 at the file's top (unit not indexed: `dd-1`,
`apartado-*`), 50 nowhere: their norm is not in `normativa.yaml` (Ley 4/2026, RD 707/2026, the 2026 CE reform,
the TJUE Statute) or is written with an abbreviation no lesson declares (`LGS` 27, `TRLCPE` 13). The web places
every row and the readable text of every lesson is unchanged; `glossary-links.es.txt` and `lesson-refs.es.txt`
did not move. The course's next round should add `aliases: [LGS]`, `aliases: [TRLCPE]` (and the missing norms)
to `normativa.yaml`, regenerate `citations.es.txt`, and add `exams:` and `lesson_noun: {es: tema}` to its
`course.yaml` — this round was not allowed to touch either file.

## Step 9

- Android bundle re-exported to scratch: byte-identical to `dist/bundle`, fingerprint
  `9c95cf4a6bf269f1a9ef51756bbc42fa11313b1115b20c969b460c5c32670adc`; label catalogs identical.
- `dist/contracts` re-exported: every data file identical; the generation-goldens README differs in one line
  that records the local CPython patch (3.14.8 now, 3.14.7 when last exported) — the machine, not this round.
  `dist/` was not rewritten.
- `verify_golden_stability.py`: exit 0, 90 committed fingerprints hold, digest
  `f0ae701b30569a03eaa9397d5bd52dc323f69b165da4e24ecf182de93b1bcaea`.
- Not done: the app was not run in a browser, so the mobile layouts (sticky/collapsible scenario, table
  scroll, stacked esquema rows) are covered by markup assertions only.

## Interpretations

1. Crypto's exams needed a source the delta does not list: `draw: per-module` (one question per module).
   Parametric presets (`each:`) cover "Bloque N" / "Tema" and crypto's per-block exam.
2. A random draw picks distinct *questions*: quiz variants count one each (a seed is searched that selects the
   variant), other generators one per exercise. Composite draws (AGE part 1: 40 from I–V + 30 from VI) are not
   in the delta and not built; that preset needs them before the course's R5.
3. Reserve on a case part = the last `reserve` questions of each case.
4. «Passed» for `requires_previous_pass` = transformed score ≥ the previous part's `pass_minimum`. The results
   page shows only raw, transformed and why a part was not graded.
5. D2 lists: three lessons with ≥3 questions to rank lessons, else three modules with ≥3 to rank modules (said
   so), else no lists; each list holds up to three and never shares an entry (k = min(3, n // 2)). Only graded
   parts' questions count; reserves and unmarked cases are left out.
6. «Por tema» vs «Por lección» comes from a new optional `lesson_noun` in `course.yaml` (default «lección»).
7. C1 in practice shows «Ver en la lección» only when it leads somewhere (an anchor or another lesson); exam
   review shows it for every question, crypto included.
8. A citation without a norm takes the previous prose citation's norm; the «Normativa» block's parentheticals
   are not read as citations — its norm names are linked instead. Glossary or reference marks inside a citation
   become plain text there (one case in AGE) so links never nest.
9. Case questions' answer shuffle is the quiz's per-question shuffle (tested); the aggregate bias suite
   (`test_quiz_answer_bias.py`) still runs on crypto only — run it over AGE's cases once real ones exist (R4).

# Mini-round — composite draw and citation parser fixes (2026-10-18)

Delta v1.3 A8/A9 and the parser findings of `docs/age-theory-ledger.md` («Esquemas bloque III/IV/V/I»). Nothing
committed. Each parser fix has a test that failed before it (`test_citations.py`, `esquema.test.ts`).

## A8/A9 — composite draw and draw modes

```yaml
- id: parte-1
  sources:                         # instead of source/draw/questions; two or more
  - source: {modules: [m01, m02, m03, m04, m05]}   # new source kind: a set of modules, one pool
    questions: 40                  # draw: random (default) | per-module | all, per source
  - source: {module: m06}
    questions: 30
  reserve: 5                       # drawn after the counted questions from what the random sources left
```

- The counted questions of every source are shuffled together into one part (one clock, one score row); reserves
  stay last. Each question keeps its exercise, so «Por tema» attributes it to its lesson as before (D).
- `draw: all` takes every question of the source (no `questions`, no `reserve`); it is valid on a single-source
  part too. `per-module` and `random` behave as before. A composite source may not be `cases` or `each`.
- Load check (`pool_shortfalls`): each source's pool must cover its count, no two sources may share a question,
  and the random sources must leave enough for the reserve. `minimum_raw` is now checked against the counted
  total for every question part.
- The single-source path draws exactly as before (same calls on the random stream), so the crypto golden holds.
- Fixed on the way: a `per-module` draw could pick a **case** exercise (it read the module's playable exercises,
  cases included). crypto has no cases, so it never showed; the fixture's m02 does
  (`test_each_source_of_a_part_draws_its_own_count_in_its_own_mode` fails without the fix).
- Fixture: `simulacro` v2, part 1 = 40 from `{modules: [m01]}` + 30 from `{module: m02}` + 2 reserve, 100 minutes
  shared with the case part. The fixture has two modules, so the «set of modules» source is proven on a
  two-module set in `test_a_set_of_modules_draws_from_every_module_in_it`.
- A stored preset snapshot re-validates with every field present, so «`source` or `sources`, not both» reads the
  values, not the fields set (an earlier draft refused every stored sitting).

## Citation parser

a. **A letter + «)» inside a citation.** An uppercase letter after a dot or a dash («21.C)», «23.Uno.B)»,
   «B)–D)») and a lowercase letter after a dash («a)–b)») now continue the citation like «f)» did. A capital after
   a space is a word, so «(… título I) Siguiente» still closes. An esquema row's trailing citation is found with the
   same rule, on both sides: `grammar.trailing_parenthetical` (backend) and `trailingCitation` in `lib/esquema.ts`
   (web), so «(art. 159.4.f) LCSP)» no longer breaks a `plazos`/`pasos`/`arbol` row.
b. **Sub-ranges under `arts.`.** After an item with a paragraph, a dash runs over paragraphs: «arts. 23.2 y 24.1–2»
   is articles 23 and 24, «24.1–24.2» is article 24; «arts. 14–38» and «arts. 12.1–13.2» are still article ranges.
c. **Rules of sources without articles.** New leads `regla`/`reglas` + number and `nota`/`notas` + number, and
   `apartado` with an ordinal word: «regla 34.II.a.1 IOC» → `regla-34`, «regla 59 bis» → `regla-59-bis`,
   «apartado sexto.1 Orden …» → `apartado-sexto`, «nota 34 anexo I Orden …» and «anexo I, nota 34, Orden …» →
   `anexo-i-nota-34`. «regla general» and «nota del BOE al art. 29» stay prose. The source index gains «Regla N.»
   headings, ordinal apartado headings («Sexto.  Delimitación.») and an annex's numbered notes (an unbroken run
   from 1 after each «ANEXO» heading); a unit the index cannot place opens the norm's file.

## AGE regenerated

`source-index.json`: only additions (no file hash or existing unit moved). `citations.es.txt`, against HEAD, before
the re-link edits — every changed row is one of these:

| Fix | Rows | What changed |
|---|---|---|
| b | 2 (m03-l03) | «arts. 30.2–3 y 68.1 LPAC», «arts. 30.4–5 y 122.1 LPAC» lose the false `art-3` / `art-5` anchors |
| a | 3 (m03-l04, m04-l05, m04-l07) | «art. 39.2.a)–b) LCSP», «art. 49.a)–c) TREBEP», «art. 8.1.a)–b) RDL 4/2000» were cut at the first letter («art. 39.2.a») and borrowed the previous citation's norm; now whole, norm named. Same anchor and page |
| c | 2 (m05-l06) | «anexo I, nota 34.II.a.1, Orden de documentos contables» re-linked from the annex (p. 10) to note 34 (p. 15) |
| c | 55 new (m05-l02 3, m05-l03 24, m05-l04 1, m05-l05 20, m05-l06 7) | 37 «regla … IOC» and 18 «apartado <ordinal> … Orden» (13 PRE/1576/2002, 5 documentos contables) were not read as citations; all open at their page |

Header: 3,216 → 3,271 prose citations, 1,434 → 1,464 anchors, 496 esquema rows, 5 naming a norm `normativa.yaml`
lacks (unchanged). No lesson text changed in this step; `annotate.test.ts` places every row of the new golden.

**Re-linked rows: 9**, the esquema list rows that dropped a letter because the old row grammar could not end in one
(ledger bloque III item 2). Only the citation in each row changed:
- m03-l04 `plazos` l. 281: «art. 159.4 LCSP» → «art. 159.4.f) LCSP».
- m05-l02 `arbol` l. 72–77: «art. 40.1 LGP» → «40.1.a)» (orgánica), «40.1.b)» (programas), «40.1.c)» (económica
  and its capítulos, artículos, conceptos) — the letters the prose cites for each.
- m05-l03 `pasos` l. 261–262: «art. 155 LGP» → «155.a)» (intervención delegada), «155.b)» (Consejo de Ministros).

Anchors are per article, so these rows keep their target. Rows cited **without the rule: 0** — no esquema row had
been rewritten onto another norm to stand in for a regla, apartado or nota; the ledger records those facts as left
out instead (the fases del gasto table, bloque V), and adding them is content work for a later R2c pass. The two
prose rows that cited the note only through its annex were re-linked by fix c itself (table above). The prose
rewordings made earlier for «21.C)» and «23.Uno.B)» (m04-l01, m04-l03, m05-l04) parse either way and were left
as they are. Table rows citing an article where the prose cites a letter (m04-l07 21.1, m05-l04 arts. 33–34
Ley 33/1987) were never affected by the bug and are not counted.

Ledger open items this closes: bloque III item 2, bloque V item 3 (platform), bloque I «arts. X y Y.1–2».

## CI, goldens, Android

- Backend: `ruff check .` clean, `mypy src` (strict) clean, `pytest` 1,489 passed, 20 skipped (1,449 before; +40:
  `test_citations` +27, `test_exam_scoring` +11, `test_exam_presets` +2). The crypto exam golden holds unchanged.
- Frontend: `npm run build` (tsc + vite) clean; `npm test` 593 passed, 51 skipped (+1, `lib/esquema.test.ts`).
- Android bundle re-exported to scratch: byte-identical to `dist/bundle`, label catalogs identical to `dist/i18n`.
  `verify_golden_stability.py`: 90 fingerprints hold, digest `f0ae701b…bcaea`, unchanged. Nothing under
  `content/crypto-futures/` or `dist/` changed.
- `ruff format` over the whole backend: HEAD was not clean outside `src/`; 35 files (scripts and tests) were
  reformatted, layout only. `ruff format --check .` is now clean.
