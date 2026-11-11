# Scope audit (AEAT R2b, part A) — auditor spec

Date 2026-11-11. Course `aeat-agentes-hacienda`. Method: C2's scope audit (`docs/age-verification/c2/r2b/scope/spec.md`,
`docs/age-c2-scope-audit.md` Run 1), with the AEAT inputs below. Read-only: edit no lesson and no repo file other than
your own report; commit nothing.

**Inputs.**

- Programme: `content/aeat-agentes-hacienda/sources/programa.md`, section «Anexo I — Programa» (I. temas 1–7; II. temas
  1–5; III. temas 1–20). Lessons: `content/aeat-agentes-hacienda/es/lessons/mBB-lTT.md` (m01 = I, m02 = II, m03 = III;
  tema TT). `m00-l01` is the intro lesson.
- Official questionnaires (AEAT Agentes, first exercise, 680 questions): `docs/age-verification/aeat/r0a/parsed/master.json`
  (list of `{id, exam, date, n, stem, opts, key}`; `id` like `2024-33`, `2022X-30` for the 2022 extraordinario). The
  ledger `docs/aeat-official-exams-ledger.md` gives each question's tema and estado. Per-lesson packs (questions already
  classified to the tema, coverage and reference): `docs/age-verification/aeat/r2/questions/<lesson>.md`. Exams 2022–2025
  (OEP 2022, 2022 extraordinario, 2023, 2024, 2025) are the coverage set; OEP 2020 and 2021 count as exam evidence for
  keeping a section; say which. A question classified `fuera de temario`, `anulada` or `norma modificada` is not
  evidence. Questions from other courses' exams (Administrativo, Auxiliar) are **not** evidence here: a section that
  already carries a «Fuera del enunciado literal del programa; preguntado en …» note naming such an exam must be
  re-audited against the AEAT questionnaires only.
- Norm texts if you need them: `content/aeat-agentes-hacienda/sources/normativa.yaml` and `sources/normativa/`
  (`pdftotext -layout <file> -`).
- Depth rule (requirements `docs/aeat-agentes-course-requirements.md` R4.3, R4.6): the measure is the official first
  exercise; a fact an official question asked is never cut.

**Programme sentences.** Split the tema's paragraph into its sentences (at «. »). A sentence that lists elements after a
colon or with commas («Las garantías de la deuda tributaria: tipos y ejecución de garantías») is split into its
elements, numbered S1, S1a, S1b… Quote each one verbatim.

**Sections.** Every heading (`##`, `###`, `####`) of the lesson body, except the fixed blocks «Lo que más cae»,
«Normativa» and «Fuentes». Worked examples (`### Ejemplo: …`) are mapped to the sentence whose rule they apply. For each
section decide:

- **mapped → Sn**: its content is part of the legal regime that sentence Sn names: the articles of the governing norm
  that regulate that subject, its organs, plazos, exceptions and effects. A `###` under a mapped `##` is mapped only if
  its own content also falls within Sn (or another sentence): check each.
- **mapped (instrumental) → Sn**: content that no sentence names but that is needed to state a mapped fact (a definition
  the next section relies on, the scope article of the governing norm). Say in a few words what it is needed for. Use
  sparingly; when in doubt, use «unmapped».
- **mapped → other tema X.Y Sn**: belongs to another tema's sentence. Say whether that tema's lesson also covers it.
- **unmapped**: none of the above. For each unmapped section, search all 680 questions (`master.json`) for its key terms
  and list every question that asks its content: id, the stem's first words, the key, and the ledger's estado. Give the
  verdict **keep (preguntado en …)** or **remove**. A question counts only if answering it needs the section's content,
  not a word in common. A section that already opens with the note «Fuera del enunciado literal del programa;
  preguntado en …» is audited the same way: confirm or reject the evidence it names (see Inputs).

**Gaps.** For every programme sentence (and element) of the tema, say which section covers it. When no section of the
lesson covers it: say whether another AEAT lesson covers it (lesson and heading, and whether this lesson points there),
or **gap** if no lesson does. For each gap, name the norm articles that govern it (from `normativa.yaml`) and how many
of the 680 questions asked it (ids).

**Intro lesson.** `m00-l01`: map its sections to the points of `programa.md` (Base 6, normas de los ejercicios) and
requirement R4.1.

**Report** `docs/age-verification/aeat/r2b/scope/<name given in your prompt>.md`, per tema:

1. `### Tema X.Y — mBB-lTT` and the programme sentences, numbered and quoted.
2. Table `| Section (heading as printed) | Level | Verdict | Programme sentence | Note |`.
3. Table `| Sentence | Covered by | Status (covered / other lesson / gap) | Note |`.
4. Unmapped sections with the exam evidence found (or «no question of 2020–2025 asks it»).

End with a summary table: per tema, sections total, mapped, instrumental, other tema, unmapped-keep, unmapped-remove,
gaps. Be exhaustive and literal: quote headings and sentences exactly. Do not propose rewrites. Write the report as you
go (one tema at a time), so a cut run loses at most one tema.
