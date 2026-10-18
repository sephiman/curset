# Platform delta — inventory (step 1)

Written 2026-10-18 before any change, for the platform round of `docs/curset-platform-delta-exams.md`
v1.2 (sections A–E). It records where the things the delta changes live today. File paths are relative to
the repository root.

## 1. Where exam rules are hard-coded

There is one exam kind today: "one question per module", unscored beyond correct/total, untimed, no
penalty, no parts. Every rule below is a literal in code, not data.

| Rule | Where | What it fixes |
|---|---|---|
| Scopes `global` / `block` | `backend/src/tradeschool/exams/service.py` (`Scope`, `start_exam`), `exams/schemas.py` (`ExamStartRequest.scope: Literal["global","block"]`) | the only two exam kinds; a block exam takes `blockId` |
| One exercise per module | `exams/service.py::_scope_modules`, `start_exam` (`secrets.choice(registry.playable_module_exercises(...))`) | question count = number of playable modules in scope |
| Order = canonical module order, frozen | `exams/service.py` (`QUESTION_ORDER` in the `rules` JSONB, `_frozen_order`) | review order survives renumbering |
| Same-scope restart abandons | `exams/service.py::start_exam` | one open sitting per (scope, block) |
| Scoring | `exams/service.py::submit_exam` | `score = correct / total`, unanswered = incorrect; per-block `{correct,total,score}`; per-module `{correct,unanswered}` list |
| No time limit, no penalty, no parts, no reserve questions | (absent) | — |
| Session storage | `exam_sessions.rules` JSONB (`exams/models.py`) | `{scope, blockId, status, questionOrder, result}`; no preset id or version |
| History item | `exams/schemas.py::ExamHistoryItem` | scope, block, score, correct/total |
| Exam list UI | `frontend/src/features/exams/ExamPage.tsx` | a "global" button + one button per block with exercises (`examinable`) |
| Runner UI | `frontend/src/features/exams/ExamRunner.tsx` | free navigation, no timer, no parts |
| Results UI | `frontend/src/features/exams/ExamReview.tsx` | percentage, "por bloque", "por módulo" ✓/✗ list, per-question review |
| Copy | `frontend/src/i18n/{es,en}.json` → `exam.*` (`intro`, `startGlobalHint`: "una pregunta por módulo") | the rules restated in prose |
| API types | `frontend/src/api/exams.ts` (`ExamScope`, `ExamResult`) | mirror of the above |

Not involved: the PDF (prints no exams), stats (`stats/service.py::_answered` excludes exam attempts —
the "separate lane" rule), Android contracts (`backend/scripts/export_contracts_to_android.py` and
`export_bundle.py` export no exam rules; grep finds none).

## 2. How lessons carry citations and blocks today

- Lessons are Markdown served raw (`content/registry.py::lesson_detail` → `markdown`). There is no
  backend AST.
- The **lesson AST is the frontend's mdast**: `frontend/src/lib/markdown.tsx` parses with
  `remark-gfm` + `lib/directives.ts` (block directives only: `:::note`, `::figure`, `::exercise`), then
  runs the ONE annotator (`lib/glossary/annotate.ts`) which plants two node kinds, `glossaryTerm` and
  `lessonRef`, and finally `remarkDirectiveToHast`. The Android bundle ships the same mdast at the same
  tap point (`lib/bundle/ast.ts`), for crypto-futures only.
- **Citations have no representation.** «(art. 67 CE)» is plain text inside a text node; nothing parses
  it on either side. The age-administrativo-c1 lessons carry about 3,200 parentheticals that look like
  citations (survey of 2026-10-18): 2,590 `(art. …)`, 66 `(arts. …)`, 61 `(disposición …)`, 28
  `(anexo …)`, 28 `(apartado(s) …)`, 7 `(preámbulo …)`, and 416 bloque VI `(fuente: `file`)` whose file
  name is inline code. Article designators include `4.1.b)` (a letter closed by its own parenthesis),
  `14.2.d) y e)`, `610 bis.2`, `148.1.8.ª`, ranges `14–38` and lists `74.2, 145.2 y 158.2`; about 280 name
  no norm and inherit the one cited before them. Norms are written about 90 ways (`CE`, `LPAC`,
  `Ley 19/2013`, `RD 364/1995`, `Real Decreto 829/2023, de 20 de noviembre, por el que…`, `Convenio
  único`, …) and are matched to `sources/normativa.yaml` entries, whose `short` names are not the
  lesson forms (`Ley 39/2015 (LPAC)`, `LOPJ (LO 6/1985)`).
- Lesson blocks: GFM tables and lists render through `markdown.tsx`; the PDF renders the same mdast
  through `lib/pdf/markdown.ts`, where a directive with no print rule prints nothing. Reading time
  (`content/reading.py`) strips directive fences and keeps the text inside them, so a container
  directive's words already count.
- Lesson checks that run over the text: never-coins and summaries-never-coin (`content/registry.py`,
  at load), list shape (`lib/refs/listShape.ts`, vitest), lesson refs with a dangling guard
  (`lib/refs/report.ts`, golden), glossary links (`lib/glossary/report.ts`, golden).
- Sources: `content/age-administrativo-c1/sources/normativa/` (101 PDF + 1 HTML, 59 MB) and
  `sources/otros/` (≈230 files, 52 MB). Nothing serves them. BOE PDFs print each article as a line
  `Artículo N.` in the body (the index pages use dot leaders); the one BOE HTML carries `id="a3-8"`
  block anchors whose `<h5 class="articulo">` says which article it is.

## 3. Goldens that cover crypto-futures exams and lessons

- **Exams: none.** `backend/tests/test_exams.py` (16 tests) and `test_exam_ordering.py` (3) assert
  behaviour (one question per module, block scoping, deferred answers, submit reveal, same-scope
  abandon, ordering frozen) but nothing freezes an exam result byte for byte. This round adds that
  golden before moving the rules (section A5).
- Lessons: `content/crypto-futures/glossary-links.{es,en}.txt` (`lib/glossary/report.test.ts`),
  `lesson-refs.{es,en}.txt` (`lib/refs/report.test.ts`), the list-shape test, the bundle AST and its
  text diff (`backend/scripts/export_bundle.py` → `frontend/scripts/export-ast.mjs`, `dist/bundle/`),
  and the bundle `contentFingerprint`.
- Exercises: `dist/contracts/generation-goldens/` (configs + digests, `test_generation_goldens.py`,
  `test_generation_config_freeze.py`), `exercise-mode.tsv` (`test_golden_exercise_mode.py`), the quiz
  bias suite (`test_quiz_answer_bias.py`), the print bijection (`test_print_exercises.py`,
  `frontend/src/lib/pdf/document.test.ts`).
- age-administrativo-c1 has `glossary-links.es.txt` and `lesson-refs.es.txt`; no exercises yet.

## 4. Data already stored that D needs

Each exam attempt row has `exercise_id` (key), `given_answer` (null = blank), `is_correct`, and the
manifest gives exercise → lesson → module. Past exams can therefore be re-aggregated per lesson
(D7) without a migration.

## 5. Plan of record (decisions taken while inventorying)

- **Presets** live in `course.yaml` under `exams:`; the engine reads them, nothing else is a literal.
  crypto-futures declares its two current kinds as presets with a `draw: per-module` source, so their
  sampling and result blob do not change; the result golden is written before the move.
- **Case** is a new exercise type `case`. A practice case opens one attempt per question (new nullable
  `attempts.question_id`, additive migration), so stats and reports stay per question.
- **Citations**: one grammar, in Python (`content/citations.py`). The backend computes each lesson's
  citations and anchors at load and ships them with the lesson; the web annotator marks those exact
  spans in the mdast (resolution-driven, no second grammar) as a third node kind, `citation`. A
  per-course golden `citations.<locale>.txt` (Python) freezes every citation, its anchors and its
  source target; a vitest reads the same golden and proves every row is located in the mdast with the
  AST text unchanged. Source page/anchor index: `content/<slug>/source-index.json`, generated by a
  script at build time.
- **Esquema** is a container directive `:::esquema{kind=… title="…"}` whose body is a GFM table
  (`tabla`, last column = citation) or a list (`plazos`, `pasos`, `arbol`; trailing «(cita)» per row),
  so the glossary annotator, list shape and reading time see its text as they see prose.
