# Requirements — Course "Administrativo del Estado (C1), turno libre, OEP 2026"

Version 1.2 · 16 October 2026 · requirements, not design. Content course for Curset, Spanish only. Builds on docs/curset-multicourse-requirements.md (R3.x: course structure, test-only courses, common pipeline).

## 1. Goal

A complete preparation course for the Cuerpo General Administrativo de la Administración del Estado (subgroup C1), ingreso libre, aimed at the exam of the convocatoria derived from the OEP 2026: the whole official programme summarised to what is examinable, and a bank of several thousand multiple-choice questions in the style of the official exams, plus practical cases (supuestos) and full exam simulations that score exactly like the real one.

## 2. Course identity

- R2.1 Slug: `age-administrativo-c1` (permanent). Title: "Administrativo del Estado (C1)". Subtitle: "Ingreso libre · convocatoria OEP 2026". Languages: `[es]`. Exercise types: multiple-choice only. No figures, no generated calculations. Status `draft` until section 9's acceptance criteria pass; then `published`.
- R2.2 Glyph and accent per the identity rules (R2a.3 of the platform requirements); chosen in the identity round, not here.

## 3. Source of truth

- R3.1 The programme and exam rules are those of the latest published convocatoria: Resolución de 18 de diciembre de 2025 (BOE-A-2025-26262, BOE núm. 306, 22-12-2025), Anexo III, until the OEP 2026 convocatoria is published in the BOE (expected before 31-12-2026). When it is, a "convocatoria diff" round (section 8, R0b) updates programme, rules and every affected lesson and question before anything else moves.
- R3.2 Exam rules to encode (Anexo III as of the 2025 convocatoria): one exercise, two compulsory eliminatory parts taken together, 100 minutes total. Part 1: up to 70 questions, 40 from bloques I–V and 30 from bloque VI, plus up to 5 reserve questions. Part 2: one practical case chosen from two, 20 questions each, on bloques II–V, plus up to 5 reserve. Four-option questions with one correct answer (confirm option count from the official questionnaires in R3.4). Wrong answer: minus one third of a correct answer; blank: no penalty. Each part scored 0–50, minimum 25 to pass; part 2 is only graded if part 1 reaches the CPS cut-off (not below 30% of the maximum raw score). Final mark 0–100. Ofimática questions refer to Windows 11 and Microsoft 365 desktop.
- R3.3 Programme: 45 temas in 6 bloques — I Organización del Estado y de la Administración pública (11), II Organización de oficinas públicas (4), III Derecho administrativo general (7), IV Gestión de personal (9), V Gestión financiera (6), VI Informática básica y ofimática (8). The lesson tree mirrors the official numbering exactly (bloque → tema); the agent extracts the full programme text verbatim from the BOE PDF into `content/age-administrativo-c1/sources/programa.md`, one entry per tema, and never paraphrases it there.
- R3.4 Official exams as style reference, stored under `sources/examenes-oficiales/`: the 2026 questionnaires (modelo A and B, 23-05-2026, and the llamamiento extraordinario of 24-07-2026) with their definitive answer keys, the "criterios de corrección, valoración y superación" note and the score-transformation note, all from sede.inap.gob.es; and the questionnaires and keys of the 2024 and 2023 convocatorias if obtainable. Juanjo downloads them into the repo (the INAP site refuses automated access); the agent does not scrape it.
- R3.5 Legislation: the applicable legislation is the one in force on the exam date (norma común 11.1). Every tema lists the norms it rests on, each with its BOE consolidated-text identifier and the consolidation date used, in `sources/normativa.yaml`. Lessons and questions cite articles from those versions only. Primary norms expected across the programme: CE 1978; LO 2/1979 (TC); LO 3/1981 (Defensor del Pueblo); LO 6/1985 (LOPJ); Ley 50/1997 (Gobierno); Ley 19/2013 (transparencia); Ley 39/2015 (LPAC); Ley 40/2015 (LRJSP); Ley 29/1998 (LJCA); Ley 7/1985 (LBRL); TREBEP (RDL 5/2015); Ley 30/1984; RD 364/1995; RD 365/1995; RD 462/2002 (indemnizaciones); Ley 47/2003 (LGP); Ley 9/2017 (contratos); LO 3/2007 (igualdad); LO 1/2004 (violencia de género); Ley 4/2023 (LGTBI); RDL 1/2013 (discapacidad); Ley 39/2006 (dependencia); LO 3/2018 and RGPD (datos); Ley 40/2015 and RD 203/2021 (administración electrónica); EU treaties for bloque I tema 11. The agent completes and corrects this list from the programme text, not from memory, and flags any norm it cannot locate in the BOE consolidated collection.

## 4. Theory: the summarised programme

- R4.1 One lesson per tema, 45 lessons, titled exactly as the official programme, plus one introductory lesson "Cómo es el examen" (rules of R3.2, timing strategy as fact only, how the raw score is transformed, what the cut-off meant in the last convocatoria from the published minimums).
- R4.2 Each lesson summarises what is examinable: it follows the structure of the governing norm (títulos, capítulos, artículos) so a reader can go from the summary to the article, and it states every fact the exams ask — plazos, mayorías, quórums, órganos competentes, numbers of members, exceptions, dates of entry into force — explicitly and verbatim from the norm, never approximated. Prose follows docs/prose-voice.md and CLAUDE.md: short sentences, no invented vocabulary, no filler, no closers.
- R4.3 Length: 1,500–4,000 words per tema in bloques I–V, in proportion to exam weight. Bloque VI lessons are short and list-shaped: per application, the features the programme names, where each lives (menu path with Spanish-locale labels), its shortcut, and the one or two behaviours the exams ask about; 600–1,500 words. The bank carries the weight of bloque VI. The lesson summary (course.yaml) is three sentences at most.
- R4.4 Every lesson ends with a "Normativa" block listing the articles it rests on (norm + article ranges), generated from the citations in the text, and a "Lo que más cae" block of at most ten facts, each tied to a question in the bank that tests it.
- R4.5 Glossary: one entry per legal or administrative term with a precise meaning (acto firme, silencio administrativo, grado personal, crédito ampliable, …), with the article that defines it when one exists. Never-coins and the no-invented-vocabulary rule apply; terms must exist outside the course with the same sense. Target 250–400 entries.
- R4.6 Bloque VI (ofimática): text only. Describe menus, commands, shortcuts and behaviours of Windows 11 and Microsoft 365 desktop as the exams ask them; no screenshots. Where the exam style relies on exact UI labels, use the Spanish-locale labels.

## 5. The question bank

- R5.1 Size: 5,000 questions at publication, growing afterwards. Distribution follows exam weight: bloque VI (ofimática) holds at least 35% of the bank, because it is 30 of the 70 questions of part 1 and the only bloque where the official exams repeat forms and facts year after year; bloques I–V share at least 50%; the rest are case questions (R6). Within a bloque, no tema has fewer than 50 questions.
- R5.1b Ofimática in depth. Before authoring bloque VI, the agent indexes every ofimática question in the official exams of 2026, 2024 and 2023 (and earlier if available) by application, feature and question form, and reports which features recur and which have never been asked. Bloque VI authoring covers every recurring feature with at least five questions and every listed feature of the programme with at least one; questions about features that no longer exist in Windows 11 or Microsoft 365 desktop are not written, and official ones about them are marked obsolete (R5.5).
- R5.2 Style is derived from the official exams, not assumed. Round R0 (section 8) produces `docs/age-exam-style.md` from the questionnaires in R3.4: option count, stem forms ("Según el artículo…", "¿Cuál de las siguientes afirmaciones es correcta?", negative stems, "Señale la respuesta incorrecta"), how often options are article numbers, dates, organs or quantities, whether "ninguna de las anteriores" appears and how often, average stem and option length, and the share of questions per tema in each exam. Every generated question follows that guide; the guide is the test the reviewer applies.
- R5.3 Each question carries: id, bloque, tema, the exact citation it is answerable from (norm + article + paragraph), difficulty (1–3), the correct option, a one-paragraph explanation stating why the correct option is right and why each distractor is wrong, and tags (plazo, órgano, mayoría, concepto, ofimática-menú, …). Distractors are plausible: adjacent articles, the other plazo in the same norm, the organ one level up or down, the previous version of the law when it changed. Never a distractor that is also correct.
- R5.4 Every question is verified against the cited text before it enters the bank: a separate verification pass (as in the prose pass's blind reviewer) reads norm text + question and answers: is the key correct by that text? is exactly one option correct? does the citation really contain the answer? Questions that fail are dropped, not fixed in place; the ledger records how many were dropped per tema and why.
- R5.5 No authored question reproduces an official exam question verbatim. Official exams are also offered to the user as a separate practice set, "Exámenes oficiales", one per convocatoria, attributed to the INAP with the date and the model, with their definitive answer keys. Before an official question enters that set, the agent checks it against the current programme and the current consolidated norms: a question on a tema no longer in the programme, or whose correct answer has changed because the law changed, or about a software feature that no longer exists, is excluded from the set and listed in the ledger with the reason ("fuera de temario", "norma modificada: art. X", "función retirada"). Questions whose answer is unchanged keep the original key. The set says at the top how many questions were excluded and why.
- R5.6 Questions are hand-authored data, not generated variants: the exercise YAML holds the stem, options and key as fixed text; the answer-order shuffle and the no-bias guards of the platform still apply.
- R5.7 Recency: each question's citation names a consolidated version; when R0b (convocatoria diff) or a legislative change updates a norm, every question citing an affected article is re-verified or retired.

## 6. Practical cases (supuestos prácticos)

- R6.1 At least 20 cases at publication, each a one-page scenario (an office, a file, a citizen's request, a staff situation, a payment) followed by 20 questions on bloques II–V, as in part 2 of the exam. Cases are the platform's grouped exercise kind: the 20 questions share the scenario and are presented together.
- R6.2 Case questions follow the same rules as R5.3–R5.4; the scenario itself is fictional, uses no real people or real entities beyond organs of the AGE, and states every fact the questions need.
- R6.3 The exam simulation (R7) offers two cases and grades only the chosen one, as the real exam does.

## 7. Exams and simulation

- R7.1 Exam presets for this course, declared in course.yaml and honoured by the platform's exam engine: "Simulacro oficial" (70 + 20, 100 min, one third penalty, blank free, two cases to choose from, part 2 graded only if part 1 passes the cut-off, 0–50 per part, 0–100 total); "Parte 1" alone; "Parte 2" alone; "Bloque N" (per bloque, 40 questions, 45 min); "Tema" (per tema, 20 questions). The platform's current fixed exam rules (R8.3 of the platform doc) must become per-course presets: this is a platform change and goes in its own round before the course's exam round.
- R7.2 Scoring shows the raw score and the official-style transformed score per part and in total (formula from the CPS note in R3.4). No comparison with cut-offs and no pass/fail verdict beyond the fixed 25-point minimum per part that the convocatoria itself states.
- R7.3 Review after submission shows, per question, the citation and the explanation, and the "Report this question" link.

## 8. Rounds and process

Each round is its own Claude Code session (or chain of sessions with a resumable ledger, as in the prose pass), reads docs/ first, writes a handoff, commits nothing.

- R0a Sources and style. Juanjo places the PDFs of R3.1 and R3.4 in `sources/`. The agent extracts the programme (R3.3), writes `sources/normativa.yaml` (R3.5) with consolidated-text identifiers verified against boe.es, and writes `docs/age-exam-style.md` (R5.2). Stop.
- R0b Convocatoria diff (runs whenever a new convocatoria is published): compare programme and rules against the stored ones, list every changed tema and rule, and the lessons and questions affected. Stop for decision.
- R1 Skeleton: course.yaml (45 lessons + intro, summaries empty), lesson stubs with the "Normativa" block pre-filled from normativa.yaml, glossary empty, exercise folders empty. Pipeline green with the course as draft. Stop.
- R2 Theory, bloque by bloque (six sessions): write the lessons, the glossary entries they need, and the "Lo que más cae" facts. A verification pass per lesson checks every number, plazo and organ against the norm text. Stop after each bloque; Juanjo reads one lesson per bloque.
- R3 Questions, bloque by bloque: author to the quotas of R5.1, verify per R5.4, link "Lo que más cae" facts to questions. Ledger with per-tema counts (authored, dropped, kept).
- R4 Cases: 20 scenarios, 400 questions, same verification.
- R5 Exam presets (after the platform round of R7.1), simulation, scoring display, review page. Full pipeline, PDF without figures, CI green. Status → published.
- R6 Growth: a recurring "100 more questions" round per bloque, with the same verification, until the bank reaches the size Juanjo wants.

## 9. Acceptance criteria

- The lesson tree equals the official programme: 6 bloques, 45 temas, titles verbatim.
- Every fact in every lesson that is a number, plazo, majority, organ or date matches the cited consolidated text; a sampled 5% check by Juanjo finds zero errors.
- Bank ≥ 5,000 questions, every one with a citation, an explanation and a passed verification; distribution per R5.1; no official question copied.
- 20 cases × 20 questions in place; a simulation with two cases grades only the chosen one.
- A full simulation takes 100 minutes, applies the one-third penalty, and shows raw and transformed scores, 0–50 per part and 0–100 total.
- Course is Spanish-only, passes the common pipeline with "no figures", PDF exports, CI green, and `crypto-futures` goldens unchanged.
- The style guide exists and every question in a random sample of 50 complies with it on inspection.

## 10. Decisions taken

1. Bank size at publication: 5,000 (R5.1).
2. Bloque VI gets the largest share of the bank, built from an index of past official ofimática questions (R5.1b).
3. Official exams are offered as a practice set, filtered against the current programme and law (R5.5).
4. Scoring shows raw and transformed scores only; no cut-off comparison (R7.2).
5. Bloque VI lessons are short and list-shaped; the bank carries that bloque (R4.3).
6. Platform rounds for exam presets per course and the grouped case exercise go ahead before R5.

## 11. Open decisions

None. The two platform rounds (exam presets per course, grouped case exercise) are confirmed and precede this course's R5; their requirements are written separately as a delta to docs/curset-multicourse-requirements.md.
