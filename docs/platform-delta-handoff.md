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
