# Scope audit (C2 R2b, part A) — auditor spec

Date 2026-11-06. Course `age-auxiliar-c2`. Method: C1's scope audit (`docs/age-verification/audit-2026-10/scope/spec.md`),
with the C2 inputs below. Read-only: edit no lesson and no repo file other than your own report; commit nothing.

**Inputs.**

- Programme: `content/age-auxiliar-c2/sources/programa.md`, section «Anexo I — 3. Programa» (bloque I, temas 1–16;
  bloque II, temas 1–12).
- Lessons: `content/age-auxiliar-c2/es/lessons/mBB-lTT.md` (m01 = bloque I, m02 = bloque II; tema TT).
- Official questionnaires (Auxiliar, all eight): `docs/age-verification/c2/r0a/parsed/*_cuestionario.json` (list of
  `{sec, n, stem, opts, ctx}`; `sec` P1 / P2 / R1 / R2 for reserve), keys in `docs/age-verification/c2/r0a/keys/`.
  The ledger `docs/age-c2-official-exams-ledger.md` gives each question's tema and estado. Exams 2022–2025:
  `conv2022`, `conv2024_modeloA` (modelo B repeats A in another order: do not count it), `conv2024_extraordinario`,
  `2026-05-23_conv2025_modeloA`. `conv2020` and `conv2020_extraordinario` are the OEP 2020 exams («programa
  anterior»): they count as exam evidence for keeping a section; say which.
- Depth rule (requirements `docs/age-auxiliar-course-requirements.md` R4.1): C2 covers the articles its own exams ask.

**Programme sentences.** Split the tema's paragraph into its sentences (at «. »). A sentence that lists elements after
a colon or with commas («Las partes: capacidad, legitimación, representación y defensa») is split into its elements,
numbered S1, S1a, S1b… Quote each one verbatim.

**Sections.** Every heading (`##`, `###`, `####`) of the lesson body, except the fixed blocks «Lo que más cae»,
«Normativa» and «Fuentes». For each section decide:

- **mapped → Sn**: its content is part of the legal regime (or, in bloque II ofimática temas 5–12, the feature set)
  that sentence Sn names: the articles of the governing norm that regulate that subject, its organs, plazos,
  exceptions and effects. A `###` under a mapped `##` is mapped only if its own content also falls within Sn (or
  another sentence): check each.
- **mapped (instrumental) → Sn**: content that no sentence names but that is needed to state a mapped fact (a
  definition the next section relies on, the scope article of the governing norm). Say in a few words what it is
  needed for. Use sparingly; when in doubt, use «unmapped».
- **mapped → other tema X.Y Sn**: belongs to another tema's sentence. Say whether that tema's lesson also covers it.
- **unmapped**: none of the above. For each unmapped section, search all eight questionnaires for its key terms and
  list every question that asks its content: exam, part, nº, the stem's first words, the key, and the ledger's estado.
  Give the verdict **keep (preguntado en …)** or **remove**. A question counts only if answering it needs the
  section's content, not a word in common. A section that already opens with the note «Fuera del enunciado literal
  del programa; preguntado en …» is audited the same way: confirm or reject the evidence it names.

**Gaps.** For every programme sentence (and element) of the tema, say which section covers it. When no section of the
lesson covers it: say whether another C2 lesson covers it (lesson and heading, and whether this lesson points there),
or **gap** if no lesson does. For each gap, name the norm articles (or official pages) that govern it (from
`content/age-auxiliar-c2/sources/normativa.yaml` and `sources/otros/fuentes.yaml`) and how much the eight
questionnaires asked it (questions as above).

**Intro lessons.** `m00-l01` («Cómo es el examen»): map its sections to the points of Anexo I (normas del ejercicio,
in the same `programa.md`) and requirement R4.1. `ps-l01` («Cómo son los psicotécnicos»): map its sections to Anexo I
punto 2.1 and requirement R6.4.

**Report** `docs/age-verification/c2/r2b/scope/<name given in your prompt>.md`, per tema:

1. `### Tema X.Y — mBB-lTT` and the programme sentences, numbered and quoted.
2. Table `| Section (heading as printed) | Level | Verdict | Programme sentence | Note |`.
3. Table `| Sentence | Covered by | Status (covered / other lesson / gap) | Note |`.
4. Unmapped sections with the exam evidence found (or «no question of 2020–2025 asks it»).

End with a summary table: per tema, sections total, mapped, instrumental, other tema, unmapped-keep, unmapped-remove,
gaps. Be exhaustive and literal: quote headings and sentences exactly. Do not propose rewrites. Write the report as
you go (one tema at a time), so a cut run loses at most one tema.
