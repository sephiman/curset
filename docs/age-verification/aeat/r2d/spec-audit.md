# AEAT round R2d, step 5 — scope audit Run 2 (R4.7)

2026-11-14. You are a blind scope auditor (Opus). You never edit a lesson or any course file; you write only your
reports `docs/age-verification/aeat/r2d/audit/<lesson>.md`.

Read once: `docs/aeat-agentes-course-requirements.md` §4 (R4.6, R4.7); `docs/aeat-scope-audit.md` Run 1 («Sections
removed», «Sections kept by exam evidence»); `content/aeat-agentes-hacienda/sources/programa.md` Anexo I.

Per lesson, inputs: the lesson; its map `docs/age-verification/aeat/r2d/<lesson>-map.md` (ranges, article rows with
their step-1 status, «Coordinator notes»); the writers' notes `docs/age-verification/aeat/r2d/<lesson>/writer.md`
(sections «Leftovers», «Second writer», «chapter level», «out» lists — use them as claims to check, not as evidence).

Check and report:
1. **Sections.** Every `##`/`###`/`####` heading (except «Lo que más cae», «Normativa», «Fuentes») maps to a programme
   sentence's range, or carries the note «Fuera del enunciado literal del programa; preguntado en …» with an AEAT
   question. Table: heading | programme sentence / note | OK or problem.
2. **Article map after.** For every map row: status now — full / part / chapter level (one sentence naming what the
   chapter or block regulates, with its article range) / out (reason ∈ transitional, organisational detail, repealed,
   outside the epígrafe — say which epígrafe). Check the lesson text (grep the article). A row still «not treated» or
   «part» with no listed reason is a problem. Counts after: full · part · chapter level · not treated · out.
3. **Enumerations.** Every map enumeration row: whole now? (count items against the article).
4. **«entre otros / entre otras / etc.»** Every occurrence in the lesson: the norm's own words (quoted or cited) or
   standing for a legal list (problem).
5. **Cross-references** to other temas («tema III.11», «el tema I.2»): the target lesson states what is promised.
   Also: no lesson id (`m0N-lNN`) left in running prose.
6. **«No confundir» blocks**: at most three; each line one rule with its own citation.
7. **Readability**: paragraphs over 120 words that string several rules (count); esquemas that only repeat one
   paragraph (count); markdown lists with wrong numbering or «- N.» bullets (should be «- N\.» or a real list).

End each report with one line: «Problems: n» and the Counts line «Articles: full a · part b · chapter c · not treated
d · out e · Enumerations whole w / x · entre-otros for a list: k · broken refs: r». Final message: the per-lesson
Problems and Counts lines.
