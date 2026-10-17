# Scope audit (R2b, Part A) — auditor spec

Date 2026-10-17. Read-only: edit no lesson and no repo file other than your own report; commit nothing.

**Inputs.** Programme: `content/age-administrativo-c1/sources/programa.md` (2025 text, Anexo III, punto 3). Lessons:
`content/age-administrativo-c1/es/lessons/mBB-lTT.md` (bloque BB, tema TT; m00-l01 is the intro lesson, see below).
Exams ledger: `docs/age-official-exams-ledger.md` (tema per question). Questionnaires as text (`pdftotext -layout`):
`SP/exams/*_cuestionario.txt`, keys in `SP/exams/*_plantilla-definitiva.txt` (SP is given in your prompt).

**Programme sentences.** Split the tema's paragraph into its sentences (at «. »). A sentence that lists elements after
a colon or with commas («Las partes: capacidad, legitimación, representación y defensa») is split into its elements,
numbered S1, S1a, S1b… Quote each one verbatim.

**Sections.** Every heading (`##`, `###`, `####`) of the lesson body, except the fixed blocks «Lo que más cae»,
«Normativa» and «Fuentes». For each section decide:

- **mapped → Sn**: its content is part of the legal regime (or, in bloque VI, the feature set) that sentence Sn names:
  the articles of the governing norm that regulate that subject, its organs, plazos, exceptions and effects. A `###`
  under a mapped `##` is mapped only if its own content also falls within Sn (or another sentence): check each.
- **mapped (instrumental) → Sn**: content that is not named by any sentence but is needed to state a mapped fact
  (a definition the next section relies on, the scope article of the governing norm, «Qué norma se aplica»). Say in
  a few words what it is needed for. Use sparingly; when in doubt, use «unmapped».
- **mapped → other tema X.Y Sn**: belongs to another tema's sentence. Say whether that tema's lesson also covers it.
- **unmapped**: none of the above. For each unmapped section, search the questionnaires of 2022–2025 (files
  `conv2022*`, `conv2024*`, `2026-*conv2025*`, and `conv2020*`, which was sat in 2022 but is «programa anterior»;
  say which) for its key terms, and list every question that asks its content: exam, part, nº, the stem's first words,
  the key, and the ledger's estado. Give the verdict **keep (preguntado en …)** or **remove**. A question counts only if
  answering it needs the section's content, not a word in common.

**Gaps.** For every programme sentence (and element) of the tema, say which section covers it. When no section of
the lesson covers it: say whether another lesson covers it (lesson and heading, and whether this lesson points there),
or **gap** if no lesson does. For each gap, name the norm articles that govern it (from `sources/normativa.yaml` and
the files under `sources/normativa/`) and how much the exams of 2022–2025 asked it (questions as above).

**Intro lesson m00-l01** («Cómo es el examen»): map its sections to the points of Anexo III (normas del ejercicio) and
requirement R4.1 (`docs/age-administrativo-course-requirements.md`) instead of the programme.

**Report** `docs/age-verification/audit-2026-10/scope/mBB.md` (one file per bloque you were given), per tema:

1. `### Tema X.Y — mBB-lTT` and the programme sentences, numbered and quoted.
2. Table `| Section (heading as printed) | Level | Verdict | Programme sentence | Note |`.
3. Table `| Sentence | Covered by | Status (covered / other lesson / gap) | Note |`.
4. Unmapped sections with the exam evidence found (or «no question of 2022–2025 asks it»).

End with a bloque summary: per tema, sections total, mapped, instrumental, other tema, unmapped-keep, unmapped-remove,
gaps. Be exhaustive and literal: quote headings and sentences exactly. Do not propose rewrites.
