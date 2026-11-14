# Requirements — Course "Agentes de la Hacienda Pública (C1, AEAT), turno libre"

Version 1.2 · 14 November 2026 · requirements, not design. Third oposiciones course for Curset, Spanish only. A delta to docs/age-administrativo-course-requirements.md (C1) and docs/age-auxiliar-course-requirements.md (C2: provenance rule R2.3): everything not stated here is as there.

## 1. Goal and staging

A preparation course for the Cuerpo General Administrativo de la Administración del Estado, especialidad de Agentes de la Hacienda Pública (AEAT), acceso libre. It is built and published in stages:

- **Stage 1 (this document's main scope): theory.** The official programme summarised to what is examinable, with esquemas, glossary, citations to the consolidated norms and the scope/coverage/currency audit. The course is **published when stage 1 is done**, without a question bank.
- **Stage 2 (later, its own go-ahead): question bank and first-exercise simulation.** Same method as C1/C2 (R3, R5).
- **Out of scope for now: the second exercise (supuestos prácticos de desarrollo).** It is a written exercise of short reasoned answers that the platform cannot grade honestly, and good model answers need an expert's review. The course explains what it is and which temas it draws on; it offers no practice for it. This is revisited only on Juanjo's decision.

## 2. Course identity

- R2.1 Slug: `aeat-agentes-hacienda`. Title: "Agentes de la Hacienda Pública (C1)". Subtitle: "AEAT · acceso libre · convocatoria OEP 2026". Languages `[es]`. Exercise types in stage 1: none. No figures. Status `draft` until stage 1's acceptance, then `published`.
- R2.2 Glyph and accent per the identity rules, distinct from C1 and C2, same family; accent in two shades.
- R2.3 Independence with provenance, as C2's R2.3: nothing shared at file level; sentences, esquema rows and glossary entries identical to a C1 or C2 item (same text, same citation, cited file with the same sha256 in both snapshots) inherit that course's verification with a provenance record; everything else is verified here. Either course may be the origin; the record names it.

## 3. Source of truth

- R3.1 Convocatoria: Resolución de 22 de diciembre de 2025, de la Presidencia de la AEAT (BOE-A-2025-27056, BOE 30-12-2025), acceso libre y promoción interna, until the OEP 2026 convocatoria is published; then the convocatoria diff round. The programme and the exam rules are extracted **verbatim from the BOE PDF by R0a**; nothing in this document about counts, times or scoring is authoritative (public summaries disagree with each other on the time and the penalty of the first exercise and on whether the programme has 32 or 34 temas; the BOE decides).
- R3.2 What public summaries say, to be confirmed by R0a: two eliminatory exercises. First: a multiple-choice questionnaire of 80 questions on the whole programme, with a penalty per wrong answer. Second: ten practical cases on «Organización de la Hacienda Pública y Derecho Tributario», answered in writing with short reasoned answers, about two and a half hours. Programme in three parts: Organización del Estado y funcionamiento de la AGE; Derecho Administrativo General; Organización de la Hacienda Pública y Derecho Tributario (the largest). The first exercise of the 2025 convocatoria was held on 21-03-2026.
- R3.3 All sources are found and downloaded by Claude Code, not by Juanjo: the convocatoria PDF from boe.es; the first-exercise questionnaires and definitive answer keys of the 2025 convocatoria and of earlier ones (2024, 2023/2022, 2021…) and any correction criteria, from the AEAT's sede (empleo público / procesos selectivos) or wherever the AEAT publishes them; the second-exercise papers too, for reference only. Plain fetch first, the Playwright browser (as check_pages.py) where the site refuses; every file recorded with URL, date and sha256; nothing from academies, forums or third-party mirrors. If an official file cannot be obtained automatically, the round lists exactly which and from which page, and continues without it.
- R3.4 Legislation: normativa.yaml and consolidated snapshots as C1. Norms shared with C1/C2 are copied with the same sha256. The tax block rests on norms C1/C2 lack (expected: Ley 58/2003 General Tributaria and its reglamentos — RD 1065/2007 gestión e inspección, RD 939/2005 recaudación, RD 2063/2004 sancionador, RD 520/2005 revisión —, Ley 35/2006 IRPF and RD 439/2007, Ley 37/1992 IVA and RD 1624/1992, Ley 27/2014 Sociedades, Ley 38/1992 Impuestos Especiales, the AEAT's organisation — art. 103 Ley 31/1990 and its structure orders —, Ley 47/2003, Ley 7/2012, customs basics if the programme names them); R0a builds the list from the programme text and the exams, not from this sentence.
- R3.5 Currency matters more here than in C1/C2: tax law changes every year (budget laws, annual orders, interest rates, thresholds, IPREM, modules). Every figure that a yearly norm sets is stated with the year and the norm that sets it; normativa.yaml records which figures are annual; the monthly currency audit covers this course from publication; the convocatoria diff round re-checks all annual figures for the exam year.

## 4. Theory (stage 1)

- R4.1 One lesson per tema, titles verbatim, plus «Cómo es el proceso selectivo» (both exercises as the BOE describes them; what the course covers and what it does not: no practice for the second exercise).
- R4.2 Rules as C1 section 4: verbatim facts with inline citations, structure following the governing norm, no word ceilings, a fact an official question asked is never cut, «Lo que más cae» from the official first-exercise questionnaires, «Normativa», glossary with never-coins, «(hoy: …)» notes, cambio-pendiente marks, prose per docs/prose-voice.md.
- R4.3 Depth: the measure is the official first exercise (R0a's ledger and style guide). The common temas are derived from C1/C2 lessons at the depth this exam asks, with provenance. The tax temas are written new.
- R4.4 Tax-specific rules: every amount, percentage, plazo and threshold verbatim with its article; computations (interest, surcharges of art. 27 LGT, sanctions and reductions, prescription dates, plazos de pago of art. 62 LGT) shown as worked examples only where the norm's own rule is applied step by step and each step cites its paragraph; examples use fictional taxpayers and state every date; no tax advice, no planning.
- R4.5 Esquemas as C1 4a, especially: plazos de pago in voluntary and executive period; recargos; types of sanctions and reductions; procedures of gestión, inspección and recaudación with their plazos and effects; órganos of the AEAT; the structure of each tax (hecho imponible, sujeto pasivo, base, tipo, devengo).
- R4.7 Coverage by programme (added after the external review of November 2026; supersedes the «unmapped and unasked → cut» reading of R4.6 inside an epígrafe). The measure of what a lesson must contain is the programme sentence and the norms that govern it, not only what past exams asked:
  - For each programme sentence the round fixes its governing article range. Every article in the range is either treated in the lesson or listed in the article map with the reason for leaving it out (transitional, organisational detail, repealed, outside the epígrafe).
  - Enumerations the norm gives are given whole: no «entre otros», «entre otras» or «etc.» standing in for items of a legal list (exemptions, infractions with their sanctions, motives, requisites, organs, documents). A long list may be an esquema, but it is complete.
  - Exam history decides depth and order, never presence: what four convocatorias asked is developed most and flagged in «Lo que más cae»; what they did not ask is still there, more briefly.
  - Content outside every epígrafe's range stays out, unless an official exam asked it (then the note «Fuera del enunciado literal…»).
  - A lesson never refers the reader to another lesson for content that lesson does not have (checked by the cross-reference audit).
- R4.8 Contrast notes. Where two neighbouring rules are routinely confused (two plazos, two organs, two procedures, two recargos), the lesson may add a short block «No confundir» stating both rules side by side, each verbatim with its citation. No interpretation, no mnemonics; verified like any sentence.
- R4.9 Glossary sense. An inherited glossary entry is kept only if its definition is the sense the term has in this course's lessons; otherwise it is rewritten from the norm that governs its use here, or removed. Origin lessons point to a lesson of this course that uses the term in that sense.
- R4.6 Audit before publication, as C1 4b: scope (every section maps to a programme sentence or carries exam evidence), coverage (every vigente first-exercise question of the last four convocatorias has its fact in its lesson), currency (norms and annual figures).

## 5. Publishing with theory only (platform)

- R5.1 A published course may have no exercises. For such a course: the Exámenes tab shows a default page («Este curso aún no tiene exámenes. La teoría está completa; el banco de preguntas llegará después.») with no button; lessons show no «Practicar»; Progreso shows reading progress only (lessons marked read, time), with the same honesty rules; the course selector, settings and sign-up list it like any other. Nothing else changes; C1, C2 and crypto-futures are untouched. This is a small platform change (delta section M) and precedes publication.
- R5.2 The PDF export of the theory works as for any course without figures.

## 6. Stage 2 (not started by this document)

- R6.1 Question bank for the first exercise: 5,000 questions at its publication, as C1 and C2; common temas by provenance from the C1/C2 banks (script-derived, C2's cost rule), tax temas authored and verified, verified excerpts, style guide from the AEAT questionnaires. Growth later towards 15,000 by variant rounds, as planned for C1 and C2 (coverage map per citable unit; minimal duplicate guard that drops only identical stem + key + distractors; variants in other stem forms and distractor sets allowed).
- R6.2 Presets: «Primer ejercicio» with the BOE's counts, time, penalty and scoring; «Tema»; «Bloque»; official first-exercise sets filtered by the ledger.
- R6.3 Second exercise: still out of scope unless decided otherwise.

## 7. Rounds for stage 1

- R0a Sources (found and downloaded by the agent), programme and exam rules verbatim, normativa.yaml with snapshots, exam style guide and official-exams ledger for the first exercise, a note on what the second exercise asks (for the intro lesson). Stop.
- R1 Skeleton with the intro lesson written.
- R2 Theory: common part (provenance from C1/C2), then the tax part in groups of temas; blind verification of everything not inherited.
- R2b Scope, coverage, currency. R2c Esquemas.
- M Platform: published course without exercises (R5.1).
- P Publication: glyph and accent, status published, browser checks, deploy notes.

## 8. Acceptance for stage 1

- Lesson tree equals the BOE programme; every non-inherited sentence passed a blind check; every inherited one has a provenance record that the pipeline test accepts.
- Coverage: every vigente first-exercise question of the last four convocatorias has its fact in its lesson, or is listed with the reason.
- Every annual figure names its year and norm; no norm is behind its latest consolidation.
- The course is published with no exercises and the platform shows the default states of R5.1; C1, C2, crypto-futures and Android are unchanged.

## 9. Estimate (stage 1)

Windows of about 4.5–5M tokens, writers on sonnet, verifiers on opus, derivation by script where provenance applies:

| Round | Windows |
| --- | --- |
| R0a sources, programme, normativa, style guide, ledger | ~0.5 |
| R1 skeleton | <0.5 |
| R2 common temas (high provenance) | ~0.5 |
| R2 tax temas (new, dense: LGT and reglamentos, IRPF, IVA, Sociedades, IIEE, AEAT) | 2–2.5 |
| R2b audit + R2c esquemas | ~1 |
| M platform + P publication | <0.5 |
| **Total to publish the theory** | **4.5–5.5** |

Stage 2 later: 3–5 windows for a 5,000 bank (common part mostly inherited, tax part authored).

## 10. Open decisions

1. Start date of stage 2 (bank of 5,000, then growth to 15,000): after stage 1 is published, on Juanjo's go-ahead.
2. Promoción interna: this course is acceso libre; whether to mark which temas the promoción interna programme omits (if the BOE gives a reduced programme) is a small addition R0a can report on.
