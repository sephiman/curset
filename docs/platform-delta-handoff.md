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

# Round F — solution panel with the norm's text (delta v1.4, section F, 2026-10-28)

Nothing committed. F1–F6 built; the AGE course regenerated and verified on a sample.

## Excerpt schema (`content/<slug>/excerpts.json`, from `scripts/extract_excerpts.py`)

Generated at build time from the course's own snapshot (pypdf for PDFs, stdlib `html.parser` for HTML/XML,
plain text for `.txt`); serving only reads it. Keyed by question: a quiz question's own id (`m06-l02-q351`), a case question's id under its case key (`m02-ex-3/q01`) — since 2026-10-28; before, every key carried its exercise key, which a rebuild could change.
`sources` holds the sha256 of every file read (a test fails when one changes). Each question has its `citation`
(as built, whitespace collapsed) and either `excerpt` or `none` (the reason).

```json
{"sources": {"sources/normativa/lpac-extracto.html": "462d…", "sources/otros/guia-recursos.html": "4522…"},
 "questions": {
  "plazo-alzada": {"citation": "art. 122.1 LPAC", "excerpt": {
    "heading": "Art. 122.1 LPAC",
    "text": "1. El plazo para la interposición del recurso de alzada será de un mes, si el acto fuera expreso.",
    "full": "Artículo 122. Plazos.\n\n1. El plazo … expreso.\n\n2. El plazo máximo para dictar y notificar la resolución será de tres meses.",
    "source": {"file": "sources/normativa/lpac-extracto.html", "fragment": "#a1-22"}}},
  "recursos-19": {"citation": "fuente: `guia-recursos.html`; «Recursos administrativos»", "excerpt": {
    "heading": "Recursos administrativos",
    "text": "El recurso de alzada se dirige al órgano superior jerárquico. El de reposición, al mismo órgano que dictó el acto.",
    "attribution": "Guía de recursos administrativos (fixture), consultado el 2026-10-28",
    "source": {"file": "sources/otros/guia-recursos.html", "fragment": ""}}},
  "recursos-20": {"citation": "fuente: `guia-recursos.html`; «Plazos de los recursos»", "none": "label not found"}}}
```

`text` has paragraphs separated by a blank line, at most 200 words (cut at a sentence end that keeps at least
half, marked «[…]»). `full` is the whole unit with its heading, present only when it differs from `text` and has
at most 1,500 words; `fullTooLong: true` when it has more (the web's «Ver artículo completo» then opens the
source). Reasons: `the question cites nothing`, `the citation names no norm of normativa.yaml`, `the norm has no
source file`, `source not text-extractable`, `heading not found`, `label not found`, `no paragraph of the page
holds what the explanation says`, `citation not understood`.

API: `GradeResponse`, `AttemptReviewResponse` (practice, case questions) and the exam review's questions carry
`excerpt: {heading, text, full, fullTooLong, href, attribution} | null`; `href` is the served source with its
fragment («Texto consolidado»). Null before answering, on an open exam, and in courses without `normativa.yaml`.

Build check: `load_registry` fails for a course with `normativa.yaml` when `excerpts.json` is missing, a question
has no entry, or an entry was built for another citation (`check_excerpts=False` only for the build script).

## What moved where

- Backend: `citations/excerpts.py` (pure extraction: PDF/HTML/text to paragraphs, unit and apartado location,
  saved-page sentences, caps — the F2 contract is pinned in its docstring), `citations/excerpt_build.py` (build
  time: every question → excerpt or reason), `citations/excerpt_store.py` (what serving reads),
  `scripts/extract_excerpts.py` (writes the file, prints per-course counts and every no-excerpt with its reason).
  `grammar.cited_parts` (apartados and letters a citation names inside a unit; the one parser still).
  `sources.heading_unit` reads spelled-out article numbers («Artículo veintidós.», «Artículo veintinueve bis.»)
  and two-word ordinals («Disposición transitoria vigésima sexta» → `dt-vigesimosexta`).
- Frontend: `features/exercises/SolutionPanel.tsx` (collapsed `<details>` «Ver solución»: answer, explanation,
  excerpt, «Tema N: título», «Texto consolidado», report), used by `ExercisePlayer`, `CaseExercise` and
  `ExamReview`; `AttemptResult` split into `Verdict` + `SolutionBody`. i18n `solution.*` in es and en. Chart
  exercises keep their inline result (they are not cited questions). PDF unchanged.
- Fixture: `m02-ex-2` variants `recursos-19` (saved-page excerpt) and `recursos-20` (no excerpt: «label not
  found») re-cited; `sources/otros/fuentes.yaml` added for the attribution; `excerpts.json` generated.
- AGE: `excerpts.json` added; `source-index.json` regenerated (articles with spelled-out numbers now placed;
  seven one-word ordinal entries such as `dt-vigesima` replaced by their compound forms); `citations.es.txt`:
  133 rows gain a page fragment, nothing else moved (anchors and text unchanged).

## AGE result (step 4)

First build: 251 of 5,200 without excerpt (4.83 %): 231 «heading not found» (laws that spell article numbers,
EUR-Lex/DOUE PDFs where every line ends in a space), 19 labels, 1 file. After the extractor fixes (no citation
was changed): **21 of 5,200 (0.40 %)**, all «no paragraph of the page holds what the explanation says»: an XML
listing (1), an English OECD PDF (3), Transparencia plan listings (3), UN pages where the fact is an aggregate (4),
NIST tables in English (9), one Windows shortcuts table (1). Listed by the script; `test_excerpts.py` fails above 1 %.

Verification (`docs/age-verification/excerpts/`): 100 at random, two blind opus verifiers: 94 yes, 1 full-only,
5 no. Fixed: 4 of the 6 misses (table rows, dotted sub-apartados, doc-page steps) and 5 flags (BOE editorial
notes, unaccented «CAPITULO», hard breaks after «artículo», list item without its opening). Open: item 7 (the fact
is in another paragraph) and item 58 (the list item `&p` does not score). Details in `fixes.md`; no second
verifier pass was run on the fixes.

## Tests, CI, goldens, Android

- Backend: `ruff check .`, `ruff format --check .`, `mypy src` (strict) clean; `pytest -n auto` 1,528 passed,
  20 skipped (1,489 before; `test_excerpts.py` new). Crypto exam golden unchanged.
- Frontend: `npm run build` clean; `npm test` 601 passed, 51 skipped (`SolutionPanel.test.tsx` 7 new, incl. the
  running-exam test; the report test now asserts the button inside the panel, F6).
- Android bundle re-exported to scratch: byte-identical to `dist/bundle`; label catalogs identical to `dist/i18n`.
  `verify_golden_stability.py`: 90 fingerprints hold, digest `f0ae701b…bcaea`, unchanged. Nothing under
  `content/crypto-futures/` or `dist/` changed.
- Not done: the app was not run in a browser; the mobile layout (wrapping links, `break-words` text, full-width
  `<details>`) is covered by markup only.

## Interpretations

1. «The paragraph that contains the cited label» for saved pages: the label locates the section; within it (or
   on the whole page when the section does not hold it) the paragraph and up to two sentences are those holding
   what the explanation quotes, else its first sentence's content words. Most labels are section headings, whose
   own «paragraph» is the heading itself. A pick ending in «:» shows that sentence and the list item that matches.
2. Cited letters narrow the excerpt to the apartado's opening and the letters only when the apartado exceeds
   200 words; a whole unit longer than 200 words whose opening does not hold the explanation's quotation shows the
   paragraph that does. Both keep the fact under the cap.
3. A cited apartado missing under the first heading of its unit is looked for under a later one (an annexed
   reglamento's own «Artículo 1»); an untitled preamble is the text between the enacting formula and the first
   heading; «anexo IV, art. 63» is that article inside the annex.
4. Heading: the citation as written, first letter capitalised («Art. 30.4 LPAC»); for a saved page, its label
   (or the page title when cited without one). «Tema N» is the course's `lesson_noun` and the lesson's place in
   its module; the link reads «Ver en la lección» while the course tree is loading.
5. «Texto consolidado» reads «Página guardada» for a saved page. In the practice player, the lesson link inside
   the panel follows C1 rule 7 (shown only when it leads somewhere). Exam review: chart questions keep their
   separate «Ver en la lección» line and no panel.

## Closing F (2026-10-29)

- Items 7 and 58 fixed by extractor changes only (no citation touched); a second verifier pass and a 50-item
  bloque VI sample found 5 further misses, all fixed and re-checked (`docs/age-verification/excerpts/fixes.md`,
  `report-3.md` to `report-5.md`). Saved-page extraction now also weighs the explanation's first sentence (its
  quotes, codes such as «&p», numbers, runs of words) and can show a two-part fact as «… […] …».
- «Sin extracto»: `excerpts.json` keeps, for a question without text, the source it looked in
  (`"source": {file, fragment}` next to `none`). The API ships `noExcerpt: {reason, href} | null` beside
  `excerpt` (practice, cases, exam review); reason codes `no-citation`, `no-norm`, `no-file`, `not-text`,
  `no-heading`, `no-label`, `no-match`, `no-parse`, worded in the `noExcerptReason` i18n namespace (es/en). The
  panel then shows the explanation, «Tema N: …», «Página guardada» / «Texto consolidado», «Sin extracto: …» and
  the report button. The 21 AGE questions are listed in `docs/age-bank-ledger.md` for a later round.
- Tests: backend 1,530 passed, 20 skipped (`test_excerpts.py` adds the pinned-seed API test of a no-excerpt
  question and a registry check over all 21); frontend 602 passed, 51 skipped. ruff, format, mypy (strict), tsc,
  vite build clean. Android bundle and label catalogs identical; golden digest `f0ae701b…bcaea`, 90 fingerprints.

## Bloque VI excerpts verified in full (2026-10-30)

Decision of 2026-10-30, steps 1–5. Nothing committed.

1. **F2 amended** for saved pages: the whole paragraph when it is under 120 words, two sentences only when longer
   (`WHOLE_PARAGRAPH`; the delta's F2 text updated). The build also flags `links-only` (a cited label whose section
   is only link titles) and `fallback` (nothing in the section matched; first paragraph shown); flags print in the
   build report and sit in `excerpts.json` as `flag`.
2. **Cited text as label.** A citation may now name the page's own text: `fuente: \`f.html\`; «<sentence>»` where the
   sentence (six words or more, ending in «.», «:», «?» or «!») or the table row («cell — cell») is copied from one
   paragraph of the page. The panel shows that paragraph or row under the nearest page heading; a row of a table with
   three or more columns comes after the header row that names its columns; a lead-in ending in «:» brings the list it
   opens. The rule applies only to such labels; no excerpt verified before it changed.
3. **Full pass**: every bloque VI excerpt (1,843) plus the 12 bloque I saved-page excerpts the F2 amendment changed,
   1,855 in 31 batches of 60, blind opus verifiers (`docs/age-verification/excerpts/full/`): 1,687 yes, 168 no, every
   «no» with the fact on the page. 141 re-cited (130 by the verifier's quoted sentence, placed mechanically; 9 by a
   sonnet writer; 2 norms re-cited to one article), question text and key unchanged, bank drafts edited and the
   exercises rebuilt (only `citation:` lines and two anchor comments moved). Blind re-check of the re-cited
   (`recheck/`): 113 yes on first check, 7 more after the lead-in rule; 21 still short → «sin extracto» (20 on re-check, 1 whose list is a run of sub-headings). The 12 bloque
   I and 27 other bloque I–II saved-page excerpts the amendment touched were also checked (35 yes, 4 → «sin extracto»).
   Accepted residual: **no bloque VI excerpt is shown that a blind verifier did not judge «yes»** (audited by text).
4. **«Sin extracto»** for a verified miss: `content/<slug>/excerpt-exclusions.yaml` lists the question and the reason;
   the build gives it `none` with the code `no-fact` («el verificador no encontró el dato en el extracto ni en otro
   lugar de la página»). Count: 89 in the course (21 extraction, 68 verifier), bloque VI 57 of 1,853. The F3 test now
   caps extraction failures at 1 % (21, 0.40 %) and reports verifier exclusions apart.
5. **Norms (bloques I–V)**: a fresh sample of 100 (`report-8.md`): 96 yes, 1 full-only, 3 no (4 %), all in two kinds,
   multi-article citations and annex code lists. Full pass of those kinds (56, `full-boe/`): 40 yes, 16 no; 2 re-cited
   to the one article that holds the fact (then failed their re-check: the key needs both articles), 14 to «sin
   extracto». The remaining norm kinds were not passed in full: their sample miss rate was 0 of 96.
6. Sample 7's fixes, re-checked within the full pass: 255, 265, 271 and 280 yes; 240 (q036), 243 (q174), 260 (q205),
   263 (q247) were misses there and went through re-citation or «sin extracto».

Counts by bloque (questions, with excerpt, «sin extracto»): I 675/661/14, II 264/262/2, III 775/775/0, IV 988/988/0,
V 645/629/16, VI 1,853/1,796/57. Content flags for the course round (not excerpt matters, keys unchanged):
`full/content-flags.tsv` (m06-l02-q350 key wording vs the page; m06-l03-q219 a distractor close to the page's text).

### Before commit (2026-10-30)

- m06-l02-q350 dropped (key «fórmulas» where the page says «formas»), replaced by m06-l02-q359; m06-l03-q219 checked
  blind: distractor b is arguably true by the page, so dropped and replaced by m06-l03-q276. Both replacements passed
  the bank's five checks (`bank/bloque-vi/m06-l0[23].r1.verify-1.md`). Their excerpts are the page sentences the
  verifiers quoted for the key. The rebuild moved m06-l02-q351 from exercise 10 to exercise 9; its text is unchanged,
  but its key changed, so earlier practice attempts no longer point at it (the course is a draft). Fixed
  2026-10-28: keys and attempts name the question by its own id (README, «Question identity»).
- Rebuilt: bloque VI 1,853 questions, 1,797 with excerpt, 56 «sin extracto»; course 88 (21 extraction, 67 verifier).
  Excerpt audit: 1,843 saved-page excerpts shown, 0 not judged «yes».

## Delta G & H — exam clock, pause, per-question time, option letters & extractor fixes (2026-10-30)

Platform round of 2026-10-30 implementing sections G (clock, pause, time per question) and H (option letters) of `docs/curset-platform-delta-exams.md`, plus the two excerpt-extractor fixes from `docs/age-cases-ledger.md`. Nothing committed.

### Preset `pause` field & exam clock (Delta G)
- **Preset `pause` field (`pause: between-questions | never`)**: Added to `ExamPreset` (`backend/src/tradeschool/exams/presets.py`). Defaults: «Simulacro oficial» (when present) defaults to `never`; «Tema» and «Bloque» presets default to `between-questions`; crypto-futures presets default to `between-questions`.
- **Clock and session state**: Sitting responses (`ExamSession`) carry `pause`, `paused`, and `activeSeconds`. Active time is tracked server-side and client-side; starts at the first question, stops at submission. Reloading resumes with the exact active time used.
- **Pause control**: The pause button is enabled only once the current question has an answer recorded. Pausing stops the clock and covers the questions with a pause card (`pausedNotice`, `pausedExplanation`, `resumeSitting` button); resuming reveals the next question. Attempting to answer questions or mark cases while paused is refused by the server with 409 `EXAM_PAUSED`. Presets with `never` show no pause control, and time continues running if the page is closed.
- **Auto-submission on deadline**: Reaching the time limit auto-submits with whatever answers were given, accompanied by `autoSubmittedNotice` in review; reserve questions run under the same overall limit.
- **Attempt time fields**: Added `time_seconds: Float | None` to the `attempts` table (Alembic migration `a1b2c3d4e5f6`). Answer mutation sends `timeSeconds` and `clockUsedSeconds`. For blank questions, moving on records the time spent until the learner moved on.
- **Time aggregation in results & Progress**: Results record `totalActiveSeconds` and per-part `activeSeconds` (for scored presets, keeping crypto-futures goldens identical); review displays per-question `timeSeconds`; the «Por tema» table and the cumulative Progress page include the per-lesson `averageSeconds`.

### Option letters (Delta H)
- **Flag `option_labels: letters`**: Course-level metadata in `course.yaml`, enabled for `age-administrativo-c1`.
- **On-screen assignment**: Letters A–D are assigned to options in their shuffled on-screen order across practice, case exercises, exam sessions, and exam review.
- **Solution panel & feedback**: Shows «Correcta: C» (or corresponding letter) and marks the option in the solution panel when `option_labels: letters` is active.
- **Question reports & email**: Reports store the formatted lettered options (`A) ...`, `B) ...`), and notification emails include the lettered options the learner saw.
- **PDF export**: Printed order and answer key sheet maintain bijection and use matching letters A–D.
- **Course isolation**: Courses without the flag (`crypto-futures`, `fixture-oposiciones`) remain completely unchanged (no letters, byte-identical goldens).

### Extractor fixes (Table A & Table C)
- **BOE page header furniture (Table A, 16 questions)**: Strip BOE headers (`BOLETÍN OFICIAL DEL ESTADO`, `Núm. ...`, `Sec. ...`, `Pág. ...`) leaking into norm excerpts across four BOE-original PDFs (Orden HFP/793/2023, Orden HAC/557/2026, RDL 14/2025).
- **Sub-number focusing for long articles (Table C, 19 questions)**: Added lettered subsection detection in `_is_sub_part` and focused extraction for cited sub-articles (e.g. `art. 76.2.b EBEP`, `art. 67.2 TREBEP`). Removed now-unnecessary manual exclusions from `excerpt-exclusions.yaml` (`sp-01/q26`, `sp-15/q09`).
- **Rebuilt excerpts**: Exactly 33 questions changed in `content/age-administrativo-c1/excerpts.json` (16 Table A + 17 Table C present in the course); all 35 verified to show the required legal fact. Zero citation changes, zero regressions in previously verified excerpts.

## Delta I — question number, tema label & copyable reference (2026-10-30)

Platform round implementing section I of `docs/curset-platform-delta-exams.md`. Nothing committed.

### Question number & Tema label (Delta I1 & I2)
- **Question number (I1)**: Every question displays «Pregunta N de M» (or «Question N of M») across practice rounds, case exercises, all exam sessions, and exam review.
- **Tema label (I2)**: Formatted as «Tema <Roman>.<Order> · <Title>» (e.g., «Tema III.3 · El acto administrativo»).
  - Shown during **practice**, **case exercises**, in **«Tema»** and **«Bloque»** exam sittings, and in **every exam review**.
  - **Suppressed during exam sitting** for simulation presets («Simulacro oficial», «Parte 1», «Parte 2») to match official exam conditions where questions are unlabeled. The tema label is revealed upon submitting in the exam review.
- **Course isolation (I4)**: Courses without `lesson_noun` (`crypto-futures`) display the question number only («Question N of M»), preserving existing presentation and test suites.

### Copyable reference (Delta I3)
- **Format**: `«<short-course> · <Roman>.<Order> · <short-question-id>»` (e.g. `age-c1 · III.3 · q127`).
- **Surfaces**: Displayed in the `SolutionPanel` footer (for practice, cases, and review) and beside each question's status badge in `ExamReview`.
- **Copy interaction**: `CopyableReference` component copies the reference string to the system clipboard and displays inline confirmation feedback («Copiado» / checkmark) for 2 seconds.
- **Schema & API**: `AttemptInstance` and `GradeResponse` expose `questionId` (`opened.attempt.question_id or opened.attempt.variant_id`) across the attempts and exams endpoints.

## Delta R5 — official simulation presets, official exams practice set & printable PDF (2026-10-30)

Platform round implementing the official simulation presets, the ten official exam practice sets (2020–2025 convocatorias), and printable PDF documents for `age-administrativo-c1`. Nothing committed.

### Preset Schema Extensions & Preset Examples

`backend/src/tradeschool/exams/presets.py` and `backend/src/tradeschool/exams/draw.py` extended to support:
- `exercise: str | None`: single exercise target for a preset source (used by official exam presets).
- `case_pairs: list[list[str]] | None`: pairs of cases where a sitting randomly offers one pair (`[case_a, case_b]`) and grades only the marked case.
- `official: bool`: exercise manifest flag ensuring official questionnaire exercises never pollute normal bank draws, solved question metrics, or citations.
- `shuffle: bool` in `QuizConfig`: when `false`, options preserve printed exam order (A–D) without runtime randomization.

#### 1. «Simulacro oficial»
Composite draw: Part 1 = 70 questions (40 from modules m01–m05 + 30 from m06) + 5 reserve questions placed last (`reserve=True`); Part 2 = 1 of 2 cases offered from the ten R4 case pairs (20 questions + 5 reserve); 100 minutes shared clock; `pause: never`; wrong = −1/3 of a correct answer, blank = 0; each part 0–50 points (minimum 25); Part 2 graded only if Part 1 ≥ 25; final score 0–100 with CPS transformation formula; tema labels hidden during the sitting; option letters A–D.

```yaml
- id: simulacro
  version: 1
  title: {es: Simulacro oficial}
  description:
    es: "Cuestionario teórico de 70 preguntas ordinarias más 5 de reserva y supuesto práctico de 20 preguntas más 5 de reserva a elegir entre dos opciones, con las reglas y baremo de la Comisión Permanente de Selección."
  time_limit_minutes: 100
  pause: never
  parts:
  - id: parte-1
    title: {es: Primera parte}
    kind: questions
    questions: 70
    reserve: 5
    sources:
    - {modules: [m01, m02, m03, m04, m05], questions: 40}
    - {module: m06, questions: 30}
    penalty: 1/3
    blank: free
    scoring: {max: 50, pass_minimum: 25, minimum_raw: 95/3}   # printed 31,67
  - id: parte-2
    title: {es: Segunda parte}
    kind: cases
    choose: 1
    questions: 20
    reserve: 5
    case_pairs:
    - [sp-01, sp-02]
    - [sp-03, sp-04]
    - [sp-05, sp-06]
    - [sp-07, sp-08]
    - [sp-09, sp-10]
    - [sp-11, sp-12]
    - [sp-13, sp-14]
    - [sp-15, sp-16]
    - [sp-17, sp-18]
    - [sp-19, sp-20]
    penalty: 1/3
    blank: free
    scoring: {max: 50, pass_minimum: 25, minimum_raw: 38/3}   # printed 12,67
    requires_previous_pass: true
```

#### 2. «Parte 1» and «Parte 2» standalone
Standalone sittings for learners practicing each half independently, 50 minutes each (explicit assumption: the official convocatoria establishes one 100-minute shared block; 50 minutes represents half the shared allotment).

```yaml
- id: parte-1
  version: 1
  title: {es: Primera parte (teoría)}
  description:
    es: "Primera parte del ejercicio oficial: 70 preguntas ordinarias más 5 de reserva (40 de materias comunes y 30 de informática). Tiempo estimado de 50 minutos (la convocatoria oficial asigna 100 minutos conjuntos para ambas partes)."
  time_limit_minutes: 50
  pause: never
  parts:
  - id: parte-1
    title: {es: Primera parte}
    kind: questions
    questions: 70
    reserve: 5
    sources:
    - {modules: [m01, m02, m03, m04, m05], questions: 40}
    - {module: m06, questions: 30}
    penalty: 1/3
    blank: free
    scoring: {max: 50, pass_minimum: 25, minimum_raw: 95/3}   # printed 31,67

- id: parte-2
  version: 1
  title: {es: Segunda parte (supuesto)}
  description:
    es: "Segunda parte del ejercicio oficial: supuesto práctico de 20 preguntas más 5 de reserva a elegir entre dos opciones. Tiempo estimado de 50 minutos (la convocatoria oficial asigna 100 minutos conjuntos para ambas partes)."
  time_limit_minutes: 50
  pause: never
  parts:
  - id: parte-2
    title: {es: Segunda parte}
    kind: cases
    choose: 1
    questions: 20
    reserve: 5
    case_pairs:
    - [sp-01, sp-02]
    - [sp-03, sp-04]
    - [sp-05, sp-06]
    - [sp-07, sp-08]
    - [sp-09, sp-10]
    - [sp-11, sp-12]
    - [sp-13, sp-14]
    - [sp-15, sp-16]
    - [sp-17, sp-18]
    - [sp-19, sp-20]
    penalty: 1/3
    blank: free
    scoring: {max: 50, pass_minimum: 25, minimum_raw: 38/3}   # printed 12,67
```

#### 3. «Exámenes oficiales» (conv2025-a .. conv2020-x)
10 presets covering all official examinations 2020–2025. 1,187 valid questions included (1,141 `vigente` + 46 `vigente-con-nota`), 63 non-current questions excluded (`anulada`, `dudosa`, `fuera de temario`, `norma modificada`, `función retirada`). Each preset includes an attribution header, exclusion note, keys from the definitive answer sheets, original option sequence without shuffle (`shuffle: false`), official letters A–D, and full solution panel with notes.

Example preset:
```yaml
- id: conv2025-a
  version: 1
  title: {es: "Convocatoria 2025 — Modelo A"}
  description:
    es: "Cuestionario oficial del proceso selectivo para ingreso en el Cuerpo General Administrativo de la Administración del Estado (convocatoria 2025, ejercicio celebrado el 14 de diciembre de 2024, Modelo A). Fuente: INAP / Comisión Permanente de Selección. 119 preguntas vigentes (6 preguntas excluidas por el tribunal o modificación normativa: anulación oficial de preguntas 74 y 103; preguntas 115, 116, 117 y 118 de LibreOffice fuera del temario vigente)."
  time_limit_minutes: 100
  pause: never
  parts:
  - id: oficial
    title: {es: "Cuestionario oficial"}
    kind: questions
    questions: 119
    source: {exercise: ofi-conv2025-a}
    penalty: 1/3
    blank: free
```

### Printable Exam Export (Delta A, B, H)
- **Backend export**: `GET /exams/presets/{preset_id}/print` returning structured JSON (`build_exam_print`) with counted questions, reserve questions, both cases of the drawn pair (scenario + questions), lettered options (A–D), and complete key sheet.
- **Frontend PDF typesetting**: `frontend/src/lib/pdf/examDocument.ts` typesetting the exam with `pdfmake` using Liberation Sans fonts, headers, footers with page numbering, scenarios in callout panels, unbreakable question blocks, and clean multi-column key tables. Accessible via «Descargar PDF» on the Exams page.


