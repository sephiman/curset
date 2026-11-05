# Requirements — Course "Auxiliar Administrativo del Estado (C2), turno libre, OEP 2026"

Version 1.1 · 5 November 2026 · requirements, not design. Second oposiciones course for Curset, Spanish only. Written as a delta to docs/age-administrativo-course-requirements.md (the C1 course): everything not stated here is as there, with "C1" read as "C2" and the slugs, programme and exam rules below.

## 1. Goal

A complete preparation course for the Cuerpo General Auxiliar de la Administración del Estado (subgroup C2), ingreso libre, for the exam of the convocatoria derived from the OEP 2026: the official programme summarised to what is examinable, a bank of several thousand multiple-choice questions in the style of the official exams, a generator of psicotécnico items like the exam's, and full simulations that score exactly like the real one. Smaller than C1 (fewer temas, no supuestos), with one part C1 does not have: the psicotécnico.

## 2. Course identity

- R2.1 Slug: `age-auxiliar-c2`. Title: "Auxiliar Administrativo del Estado (C2)". Subtitle: "Ingreso libre · convocatoria OEP 2026". Languages: `[es]`. Exercise types: multiple-choice and psicotécnico (section 6). No figures. Status `draft` until acceptance, then `published`.
- R2.2 Glyph and accent per the identity rules; a distinct glyph from C1's, same family.
- R2.3 Independence: the course shares nothing with `age-administrativo-c1` at the file level (R3.1 of the platform requirements). Its lessons, glossary and questions are its own. The C1 lessons and bank may be used as a reference by writers, since every fact there is cited and verified, but every C2 fact is re-cited from the C2 course's own sources snapshot and re-verified; nothing is copied without that.

## 3. Source of truth

- R3.1 Same convocatoria as C1 (Resolución de 18 de diciembre de 2025, BOE-A-2025-26262, BOE 22-12-2025), Anexo I (Cuerpo General Auxiliar, ingreso libre), until the OEP 2026 convocatoria is published; then the convocatoria diff round. The agent extracts the programme and the exam rules verbatim from the PDF already in the C1 course's sources into `content/age-auxiliar-c2/sources/programa.md`.
- R3.2 Exam rules to encode, to be confirmed verbatim from Anexo I by R0a (what public summaries say of the 2025 convocatoria): one exercise, two compulsory eliminatory parts taken together, about 90 minutes total. Part 1: 60 questions, 30 on bloque I (Organización pública) and 30 psicotécnicas on the aptitudes of the post, plus up to 5 reserve. Part 2: up to 50 questions on bloque II (Actividad administrativa y ofimática), plus reserve. Four options, one correct; wrong answers penalise; blank does not; minimums per part and the CPS transformation as the convocatoria and the CPS notes state; final 0–100. Software versions as the convocatoria states (the agent records whether it says Windows 10 or 11 and which Microsoft 365).
- R3.3 Programme: two bloques, extracted verbatim; the lesson tree mirrors the official numbering.
- R3.4 Official exams: the Auxiliar questionnaires and definitive answer sheets of the 2025 convocatoria (exam 23-05-2026, modelo A/B, and the extraordinario if any), the CPS criterios and minimums notes, and earlier convocatorias (2024, 2022, 2020) as available, from the INAP sede page of the Cuerpo General Auxiliar, ingreso libre. Juanjo downloads them into `sources/examenes-oficiales/` with the C1 naming scheme; the psicotécnico questions are part of those questionnaires and are the style reference for section 6.
- R3.5 Legislation and currency: as C1 (normativa.yaml with consolidated snapshots, cambio-pendiente, version in force on the exam date). Many norms are the same as C1's; the files are copied into this course's snapshot with their dates, not referenced across courses.

## 4. Theory

- R4.1 One lesson per tema plus «Cómo es el examen». Same rules as C1 section 4 (verbatim facts, citations, no word ceilings, «Lo que más cae», «Normativa», esquemas, glossary). Depth is the C2 exam's: the official questions are the measure; where C1 covers the same norm, C2 covers the articles its own exams ask and not the rest.
- R4.2 Bloque II ofimática lessons: list-shaped, as C1's bloque VI, built from the saved official Microsoft pages (the C1 snapshot pages may be re-saved into this course's sources/otros/; same URL, same sha256 check).

## 5. The question bank

- R5.1 Size at publication: 5,000 questions; bloque II (ofimática, up to 50 of 110 questions) at least 45 %; bloque I at least 50 %; the rest psicotécnico calibration items (section 6). Growth later towards 15,000 by variant rounds (same approach as planned for C1: coverage map per citable unit, minimal duplicate guard that drops only identical stem + key + distractors, variants in other stem forms and distractor sets allowed). Floors per tema as C1. Style guide derived from the Auxiliar questionnaires (R0a), not reused from C1: the C2 exams have their own forms.
- R5.2 Everything else as C1 section 5 (sources, verification, drop-not-fix, bias guards, verified excerpts, stable ids, official exams as a filtered practice set, no copies).

## 6. Psicotécnicos

- R6.1 The 30 psicotécnico questions of part 1 test aptitudes, not knowledge: numeric series, alphanumeric series, verbal reasoning (synonyms, antonyms, odd one out, analogies), basic arithmetic and percentages, attention and perception (finding differences, counting symbols, checking codes), table and chart reading, administrative tasks (ordering records alphabetically or by number, matching, error detection in copied data), spatial and logical reasoning. R0a classifies every psicotécnico question of the official questionnaires by type and counts them per exam; that index fixes which types exist and their weights.
- R6.2 Items are generated, not hand-authored: the platform already has generators with goldens, fingerprints and stability checks for the crypto course; psicotécnico generators are a new family (platform delta, section L): each type gets a generator that produces an item from a seed (stem, four options, one correct, explanation showing the rule or the count), with difficulty parameters, and the official-exam style of that type (R0a). Items are never stored as content; the course declares which generators it uses and their weights for the simulation and for practice.
- R6.3 Verification of generators, not of items: each generator has a solver (the item's answer is computed, never guessed), property tests (exactly one correct option, distractors distinct from the key and from each other, no ambiguous series: the rule must be the unique simplest rule under the generator's own definition), goldens of 50 seeded items per generator reviewed by a blind reader once, and the answer-bias guards over 1,000 seeded items.
- R6.4 Practice: «Psicotécnicos» as a practice entry in the course tree (not a lesson): choose a type or all, timed or not, with the solution panel showing the rule. A short lesson «Cómo son los psicotécnicos» explains each type with one worked example, citing the official exam that used it.
- R6.5 Exam: the simulation's part 1 draws 30 knowledge questions from bloque I and 30 generated psicotécnico items in the type weights of the last official exam; the printable exam prints the generated items with a key sheet; the official-exams practice set keeps the real psicotécnico questions as printed.
- R6.6 Results by type: the results page's «Por tema» table gets one row per psicotécnico type, and the two lists treat types like lessons (same three-question threshold).

## 7. Exams

- R7.1 Presets: «Simulacro oficial» (60 + up to 50, time and penalty per Anexo I, pause never, tema labels hidden), «Parte 1», «Parte 2», «Bloque N», «Tema», «Psicotécnicos» (30 items, timed as the exam's share), and the official-exam sets. Composite draw across sources already exists; a part mixing stored questions and generated items is a platform change (section L).
- R7.2 Scoring per the convocatoria and the CPS notes for the Auxiliar (its own minimums and formula values, extracted by R0a, exact fractions as in C1).

## 8. Rounds

- R0a Sources, programme, normativa, exam style guide, ofimática index, psicotécnico index (type, count per exam, examples), official-exams ledger. Stop.
- R1 Skeleton. R2 Theory bloque by bloque (two bloques; each may take two sessions). R2b scope/coverage/currency audit. R2c esquemas.
- R3 Question bank (bloque I, bloque II). R3p Psicotécnico generators (platform delta L first, then the generators per type with their goldens).
- R5 Presets, official sets, simulation, publication. No R4 (no supuestos).

## 9. Acceptance

- As C1's, with: bank ≥ 5,000; every psicotécnico type of the official index has a generator with solver, property tests, reviewed goldens and bias guards; a simulation draws 30 + 30 for part 1 and up to 50 for part 2 and scores per the convocatoria; the official sets include the real psicotécnico questions; no file is shared with age-administrativo-c1.

## 10. Decisions taken

1. Bank size: 5,000 at publication; 15,000 later via variant rounds (also planned for C1).

## 11. Open decisions

1. **Psicotécnico types**: all types the official index finds, or the recurring ones first and the rare ones in a later round.
2. **Ofimática pages**: re-save C1's Microsoft page snapshots into this course (fast, identical sha256) or fetch fresh (catches changes; costs a currency check on C1 too).
