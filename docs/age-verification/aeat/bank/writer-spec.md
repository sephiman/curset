# Writer spec — AEAT question bank, authored delta (round R3, stage 2)

You write questions for the course `content/aeat-agentes-hacienda` (repo `/home/juanjo/PycharmProjects/curset`), the
first exercise of the Agentes de la Hacienda Pública oposición. Do not commit. Do not edit lessons, content, tests or
goldens. Write only your draft and notes under `docs/age-verification/aeat/bank/`.

## Read first, once per run

- `CLAUDE.md` (writing rule) and `docs/prose-voice.md`: explanations are prose and the voice applies; Peninsular
  Spanish; the course invents no vocabulary.
- `docs/aeat-exam-style.md` whole, in particular § 2 stem forms, § 3 options, § 6 distractors, § 9 tax questions,
  § 12 checklist. It is the style of every question you write.
- `docs/aeat-bank-plan.md` § 3 (mix, article share, negatives, key-longest).
- Your tema's **delta sheet** `docs/age-verification/aeat/bank/delta/<lesson>.md`: quota, to-author count, stem forms still
  needed, «Lo que más cae» lines, kept questions by cited unit.
- The lesson `content/aeat-agentes-hacienda/es/lessons/<lesson>.md` and the official pack of the tema
  `docs/age-verification/aeat/r2/questions/<lesson>.md` (the official questions and the facts they asked).
- The source text of an article: the norm file `sources/normativa.yaml` names, in
  `content/aeat-agentes-hacienda/sources/normativa/`, read with `pdftotext -layout`. The lesson's «Normativa» section
  lists the units it cites.

## What to write

1. Every «Lo que más cae» line: at least one question (they are the facts the exam asked most).
2. Every fact the official pack asked (coverage questions) that no kept question tests: one question with a **new
   angle**, never its stem or options, never its key paired with one of its distractors.
3. Then every other citable fact of the lesson, paragraph by paragraph, and every esquema row (plazos, percentages,
   órganos, tipos, requisitos, conditions), up to the delta sheet's count.
4. Do not duplicate a kept question or one of your own: same fact **and** same angle. The same fact from another angle
   (plazo vs organ, condition vs effect) is fine. Never leave a tema's quota to repetition: if the lesson's cited text
   has no more distinct facts, stop and say so in the notes (capacity); never pad.

## Rules

- **Source:** only what this course's lesson cites, read in the snapshot text of the norm. Never an official key, never
  memory. An official key is never a source of facts, but a point the norm states clearly may be asked, keyed by the norm text alone.
  For a point of one of the six flagged keys (2024-43, 2022X-69, 2025-20, 2025-24, 2023-80, 2022X-88) end the explanation with
  «En el examen <año> (pregunta N) la plantilla oficial dio otra respuesta; esta pregunta sigue el texto del artículo.»
- **RDL 29/2026 (pending convalidation):** no question on a precept it changed (list in
  `docs/age-verification/aeat/r1/rdl-29-2026-revert-list.md`, and every sentence of the lesson that carries a
  «pendiente de convalidación» / «desde …» mark). `check_draft.py` flags the common ones; you rule on the rest.
- **Stems** (§ 2 and § 12 items 2, 3, 10): name the norm with its BOE title and date («Ley 58/2003, de 17 de diciembre,
  General Tributaria»), never an acronym, and the article when the question rests on one. Forms and shares per the
  sheet. Forms and their `stem_form` values: `art-completar` («De acuerdo con el artículo 62 de …, … será:»),
  `señale` («… señale la respuesta CORRECTA:»), `directa` («¿…?»), `supuesto` (one-question scenario), `art-pregunta`
  («Según el artículo X de …, ¿…?»), `cual` («¿Cuál de las siguientes …?»).
- **Lengths:** stem 20–60 words (supuesto up to 110); options 5–30 words, a statement option up to 60 when the norm's
  sentence runs that long.
- **Four options**, one correct. No «Ninguna», «Todas», combined options or article numbers as options. Options share
  grammatical form and often the opening words.
- **Distractors** (§ 6): one pattern per question, two at most: texto alterado (the norm's sentence with a word,
  condition or number changed), otra figura del mismo tipo, otro plazo of the same norm or its neighbour, cifra cercana
  (real figures: art. 27 LGT recargos, art. 62 LGT plazos, art. 188 reductions, art. 23.2 LIRPF is HELD), the organ one
  level off, a calculation with one step wrong. Each distractor is wrong **by the cited text**, never merely odd. The
  previous version of an amended rule is a distractor only where the amendment is itself examinable.
- **Negative stems:** at most one in 20 of the tema, the negative word in capitals.
- **Key longest:** across your draft the key is strictly the longest option in about a quarter of the questions (±3);
  never pad a key, never gloss it in the stem's words; shape distractors to the norm's length.
- **Annual figures** (interés de demora, interés legal, IPREM, límites que fija una ley de presupuestos): the year is in
  the stem; the explanation cites the norm that sets it for that year.
- **Computations** (intereses, recargos, plazos del art. 62, reducciones, prescripción, prorrata): tag `cómputo`; the
  stem gives **every date (with year) and amount**; fictional taxpayers (invented names, never a real company); the
  explanation shows each step with its paragraph and the calendar (art. 30 LPAC / art. 48 LGT counting). A verifier will
  recompute. Round numbers, one rule applied once or twice.
- **Organ names** current (AEAT departamentos and dependencias per the orders in `normativa.yaml`).
- **Explanations:** written by hand, prose per the voice page, one per question, never patched by script. They say why
  the key is right and why each distractor is wrong **naming each by its content, never by letter or position**, and
  never dismissing a distractor because the source is silent about it (except where the norm gives a single value, holder
  or closed list and the explanation states it).
- **No official copies:** do not copy or lightly reword an official question (stem + options), nor reuse an official
  distractor with the same fact, angle and key. `check_draft.py` flags similarity ≥ 0.80.
- **Fields:** `id`, `tema`, `section` (the lesson's `##` heading the fact sits under), `citation` (the lesson's form,
  e.g. `art. 62.2 LGT`; the same form the lesson uses so it resolves to an anchor), `stem_form`, `names_article`,
  `negative`, `prompt`, `options` {a–d}, `correct`, `difficulty` (target 30/50/20 % of levels 1/2/3), `tags`,
  `distractor_pattern`, `explanation`, `source_quote` (exact sentence from your text extraction, checked by script),
  `covers` (`lmc-N`, `official:<code>` e.g. `official:2025-P2-32`, `fact:<short>`), `lesson_anchor`.
- **Ids:** continue from the id the delta sheet gives, in order; if you are given a part, use the id range you are
  given. Draft file `docs/age-verification/aeat/bank/<lesson>.authored[-p<k>].draft.json`, notes
  `<lesson>.authored[-p<k>]-notes.md`. Write JSON by script from a Python file in the scratchpad subfolder named after
  your draft; set `correct` from the key's text; print every stem with its keyed option before hand-back.

## Checks before hand-back

From `backend/`: `uv run python ../docs/age-verification/aeat/bank/tools/check_draft.py <draft>` must show 0 anchor
misses, no STYLE line, no HELD line, no OFFICIAL SIMILAR line. The mix printed there must move the tema toward its
targets (`supuesto`, `señale` first when the sheet says they are short). Fix every real flag.

## Notes and final message

Notes: «Lo que más cae» line → id; official coverage question → id; facts left out and why (capacity); held items
(RDL 29/2026) you skipped; check outputs. Final message: authored count, anchor misses (0), lines and official questions
covered, blockers. Short.
