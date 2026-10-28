# Requirements delta — Curset platform: exam presets, grouped cases, source links, results by lesson

Version 1.4 · 28 October 2026 · delta to docs/curset-multicourse-requirements.md. Four platform changes. A and B are required by the AGE course (docs/age-administrativo-course-requirements.md, R6.1 and R7.1) and precede that course's R5. C and D apply to every course and can run as their own rounds at any time after A.

## A. Exam presets per course

- A1 Today the exam rules (question count, time, scoring) are fixed in the platform. They become per-course presets declared in `course.yaml` under `exams:`, each with: id, title, parts (one or more), and per part: question count, source (whole course, bloque N, tema N, case pool), time limit (per exam, not per part, when parts run together), penalty per wrong answer as a fraction of a correct one (0, 1/4, 1/3), blank-answer rule, score range, pass minimum, and whether the part is graded only if the previous part passed its minimum.
- A2 A part can be a "choose one case of N": the exam presents N cases, the user marks one, and only that one is graded; an exam with no case marked, or two marked, is not graded for that part, as the real exam does.
- A3 Reserve questions: a preset may declare R extra questions per part; they are shown at the end of the part and counted only if a question before them is voided. The platform never voids questions on its own; this exists so the simulation matches the official count and timing.
- A4 Scoring: raw score per part = correct − penalty × wrong; transformed score per the formula the preset declares (linear map from the preset's minimum raw to the pass minimum and from maximum raw to the maximum score, which is the CPS formula); total = sum of parts. The results page shows raw and transformed per part and in total, and nothing else about cut-offs.
- A5 `crypto-futures` keeps its current exams as its presets, declared the same way; its behaviour and scores are byte-for-byte unchanged (goldens prove it).
- A6 The exam list in the Exams tab shows the course's presets with title, parts, question count and time. Past exams store the preset id and version they were taken with.
- A8 Composite draw: a part may declare several sources with a count each («40 from modules I–V, 30 from module VI»), drawn and shuffled together into one part with one time and one score. The results page still attributes each question to its lesson (D). Needed for the AGE part 1; the fixture course gets a two-source part to prove it.
- A9 Draw modes recognised: `all`, `per-module` (one question per module, as crypto-futures uses), `random` from a lesson, module, set of modules or case pool; declared per source.
- A7 Progress rules (fractions below ten, no ranking under three exercises, no aggregate under three people) are unchanged and apply per preset.

## B. Grouped case exercise (supuesto práctico)

- B1 A new exercise kind `case`: a scenario text (one page, Markdown, no figures) plus an ordered list of 10–25 multiple-choice questions that share it. Each question has the same fields as a standalone question (citation, explanation, difficulty, tags).
- B2 In practice mode, the scenario stays visible (sticky or collapsible on mobile) while the user answers the questions in order; answers are submitted per question as today, and the case counts as done when every question is answered.
- B3 In exam mode, a case is a unit: it is chosen as a whole (A2), presented with the scenario first, and graded as a part.
- B4 Report link: per question, as today; the report carries the case id and the scenario title.
- B5 PDF: the case prints as scenario followed by its questions, with the answer key in the key section; the exercise/key bijection check covers cases.
- B6 Answer-order shuffle and bias guards apply per question; the question order within a case is fixed.
- B7 Progress: case questions count as exercises of their tema for stats; the case itself is not a separate stat unit.

## C. Links from question to lesson and from lesson to source

- C1 Every exercise already names its lesson (tema). In practice, once answered, and in the review of a submitted exam, each question shows a link «Ver en la lección» that opens the lesson. When the question carries a citation (norm + article, as AGE questions do), the link opens the lesson at the first paragraph that cites that article; otherwise at the top of the lesson.
- C2 Lessons get stable anchors per cited article: an inline citation such as «(art. 67 CE)» is rendered as a link and carries an anchor derived from norm short name + article (`#ce-art-67`). The anchor set of a lesson is generated from its citations and listed in the lesson's AST, so questions can target it and the cross-reference check can verify that a question's citation resolves to an anchor in its lesson (a question citing an article its lesson never cites is a check failure, reported per question).
- C3 From lesson to source: each citation link opens the consolidated text of the norm from the course's `sources/normativa/` snapshot (the file named in `normativa.yaml`), at the article when the format allows it: for HTML sources, the article's own anchor; for PDFs, the page where the article starts, resolved once at build time by searching the text and stored in the manifest (`#page=N`). The "Normativa" block at the end of a lesson links every norm it lists the same way. Sources are served by the platform as static files of the course (public official documents); a course without `normativa.yaml` (crypto-futures) shows no citation links and nothing else changes for it.
- C4 Exam mode shows none of these links; they appear only after submission.
- C5 PDF export: citations print as plain text with the norm and article; the "Normativa" block prints the norm titles and consolidation dates. No hyperlinks to local files in the PDF.
- C6 Report link (8a of the platform requirements): the report email includes the lesson anchor and the citation, so a wrong question can be traced to its source in one click.

## D. Exam results by lesson

- D1 The results page of a submitted exam adds a section «Por tema» (or «Por lección» in courses without bloques): one row per lesson that had at least one question in the exam, with questions, correct, wrong, blank and the percentage of correct answers, sortable, each row linking to the lesson. Rows are grouped by module (bloque) with module totals.
- D2 Two short lists above the table: «Donde más brillas» and «Donde más tienes que preparar»: the lessons with the highest and lowest percentage among those with at least three questions in this exam. When fewer than three lessons qualify, the lists aggregate by module instead and say so; when nothing qualifies (a 20-question tema exam), the lists are omitted and only the table shows. No lesson is ranked on one or two questions, in keeping with the progress honesty rules.
- D3 Blank answers count as not correct for the percentage but are shown separately, because in exams with penalties a blank is a decision.
- D4 The Progress tab gets the same «Por tema» view cumulative over every exam and practice attempt of the course (already per course), with the same thresholds (at least three attempts per lesson to appear in the two lists). It replaces nothing: the existing stats stay.
- D5 Case exercises (B) count their questions under the lesson each question cites, not under the case.
- D6 Reserve questions (A3) that were not counted do not appear in the table.
- D7 The data needed (lesson per question, correct/wrong/blank per answer) already exists per attempt; this section adds the aggregation and the view. Past exams get the view retroactively, since their answers are stored.

## E. Esquema block

- E1 A new lesson block `::esquema` with fields: kind (`tabla` | `plazos` | `arbol` | `pasos`), title, and rows; each row carries one or more cells (for `tabla`), or a label and detail (for `plazos`, `arbol`, `pasos`), plus a citation (norm short name + article) and, for `arbol`, a parent reference. Rows are verbatim fragments; the block has no free prose.
- E2 Rendering: `tabla` as a table with a header row; `plazos` as an ordered timeline (step, plazo, article); `arbol` as an indented tree; `pasos` as a numbered stepper with document/organ columns. Each row's citation renders as the same citation link as inline citations (C2–C3). Mobile: tables scroll horizontally inside their own container; trees and steppers stack.
- E3 PDF: every kind prints as a table; citations print as text.
- E4 Checks: every row has a citation; every citation in an esquema also appears as an inline citation in the same lesson's prose (otherwise a cross-reference failure naming the row); list-shape and never-coins run over esquema text; reading-time counts esquema words.
- E5 Glossary links are annotated inside esquema cells as in prose.
- E6 crypto-futures has no esquemas and is unchanged; a fixture lesson with one block of each kind proves rendering, PDF and the checks, including a failing citation.

## F. Solution panel with the norm's own text

- F1 After a question is answered in practice (right or wrong), and for every question in the review of a submitted exam, a collapsed panel «Ver solución» opens with, in this order: the correct option marked; the explanation; the **cited text of the norm, verbatim**, under a heading with norm short name and article («Art. 30.4 LPAC»); then the links «Tema N: <title>» (to the lesson anchor, as in C1) and «Texto consolidado» (to the source at the article or page, as in C3). Never shown before answering; never in exam mode before submission.
- F2 The excerpt is extracted at build time from the course's own snapshot (sources/normativa/ or sources/otros/), not fetched live, and stored with the exercise in the generated AST. Unit of extraction: the cited paragraph(s) when the citation names them («art. 30.4»), else the whole article; capped at 200 words with a «Ver artículo completo» expansion that shows the full article (capped at 1,500 words, else the link only). For HTML sources the article's element; for PDF sources the page text between the article heading and the next heading, via the existing page index; for saved documentation pages (bloque VI), the paragraph that contains the cited label, at most two sentences, with the page title and date as attribution.
- F3 Build check: every question gets an excerpt or an explicit «no excerpt» marker with a reason (heading not found, source not text-extractable). The build report lists the no-excerpt questions per course; the round that adds this feature must bring age-administrativo-c1 to under 1 % no-excerpt, fixing the extractor or the citation form where it fails. A verifier samples 100 excerpts and confirms each contains the fact the key rests on; misses are extractor bugs, not content bugs.
- F4 Esquema rows and «Lo que más cae» lines are not affected. Case questions (B) get the panel per question. The PDF does not print excerpts (the key section stays as it is).
- F5 Courses without normativa.yaml (crypto-futures) show the panel with the explanation only; nothing else changes for them.
- F6 Report link (8a) sits inside the panel, after the excerpt, so a reader who sees the norm and still disagrees can report with one click.

## Acceptance

- `crypto-futures` exams and goldens unchanged.
- A Spanish-only test course with a two-part preset (70 + choose-one-of-two cases of 20, 100 minutes, 1/3 penalty) runs end to end, grades only the chosen case, refuses to grade part 2 with no or two cases marked, and shows raw and transformed scores.
- A `case` exercise renders in practice, exam and PDF; its questions report, shuffle and count like any other.
- An answered AGE question links to its lesson at the cited article's anchor; the citation in the lesson opens the consolidated text at the article (HTML) or page (PDF); a question citing an article its lesson does not cite fails the cross-reference check. crypto-futures shows no citation links and its goldens are unchanged.
- A lesson with the four esquema kinds renders on web and in the PDF; an esquema row citing an article the prose does not cite fails the check with the row named.
- An answered AGE question shows the solution panel with the verbatim cited text under its article heading, the tema link and the source link; a crypto-futures question shows the explanation only; fewer than 1 % of AGE questions lack an excerpt and each of those says why.
- A submitted simulation shows the per-lesson table and the two lists; a tema exam of 20 questions shows the table only; the Progress tab shows the cumulative view; no lesson appears in a list with fewer than three questions.
