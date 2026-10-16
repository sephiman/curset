# Requirements delta — Curset platform: exam presets per course and grouped case exercises

Version 1.0 · 16 October 2026 · delta to docs/curset-multicourse-requirements.md. Two platform changes required by the AGE course (docs/age-administrativo-course-requirements.md, R6.1 and R7.1). Both are their own Claude Code rounds and precede that course's R5.

## A. Exam presets per course

- A1 Today the exam rules (question count, time, scoring) are fixed in the platform. They become per-course presets declared in `course.yaml` under `exams:`, each with: id, title, parts (one or more), and per part: question count, source (whole course, bloque N, tema N, case pool), time limit (per exam, not per part, when parts run together), penalty per wrong answer as a fraction of a correct one (0, 1/4, 1/3), blank-answer rule, score range, pass minimum, and whether the part is graded only if the previous part passed its minimum.
- A2 A part can be a "choose one case of N": the exam presents N cases, the user marks one, and only that one is graded; an exam with no case marked, or two marked, is not graded for that part, as the real exam does.
- A3 Reserve questions: a preset may declare R extra questions per part; they are shown at the end of the part and counted only if a question before them is voided. The platform never voids questions on its own; this exists so the simulation matches the official count and timing.
- A4 Scoring: raw score per part = correct − penalty × wrong; transformed score per the formula the preset declares (linear map from the preset's minimum raw to the pass minimum and from maximum raw to the maximum score, which is the CPS formula); total = sum of parts. The results page shows raw and transformed per part and in total, and nothing else about cut-offs.
- A5 `crypto-futures` keeps its current exams as its presets, declared the same way; its behaviour and scores are byte-for-byte unchanged (goldens prove it).
- A6 The exam list in the Exams tab shows the course's presets with title, parts, question count and time. Past exams store the preset id and version they were taken with.
- A7 Progress rules (fractions below ten, no ranking under three exercises, no aggregate under three people) are unchanged and apply per preset.

## B. Grouped case exercise (supuesto práctico)

- B1 A new exercise kind `case`: a scenario text (one page, Markdown, no figures) plus an ordered list of 10–25 multiple-choice questions that share it. Each question has the same fields as a standalone question (citation, explanation, difficulty, tags).
- B2 In practice mode, the scenario stays visible (sticky or collapsible on mobile) while the user answers the questions in order; answers are submitted per question as today, and the case counts as done when every question is answered.
- B3 In exam mode, a case is a unit: it is chosen as a whole (A2), presented with the scenario first, and graded as a part.
- B4 Report link: per question, as today; the report carries the case id and the scenario title.
- B5 PDF: the case prints as scenario followed by its questions, with the answer key in the key section; the exercise/key bijection check covers cases.
- B6 Answer-order shuffle and bias guards apply per question; the question order within a case is fixed.
- B7 Progress: case questions count as exercises of their tema for stats; the case itself is not a separate stat unit.

## Acceptance

- `crypto-futures` exams and goldens unchanged.
- A Spanish-only test course with a two-part preset (70 + choose-one-of-two cases of 20, 100 minutes, 1/3 penalty) runs end to end, grades only the chosen case, refuses to grade part 2 with no or two cases marked, and shows raw and transformed scores.
- A `case` exercise renders in practice, exam and PDF; its questions report, shuffle and count like any other.
