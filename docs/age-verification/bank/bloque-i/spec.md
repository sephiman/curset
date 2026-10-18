# Writer spec — question bank, bloque I (R3, 2026-10-18)

Shared by every writer of a bloque I tema. Read in full before writing: `CLAUDE.md`, `docs/prose-voice.md`,
`docs/age-exam-style.md` (whole file; § 12 is the reviewer's checklist), `docs/age-bank-plan.md` (§ 3 targets),
the tema's lesson `content/age-administrativo-c1/es/lessons/m01-lTT.md`, the tema's official questions
`docs/age-verification/bank/official/I.TT.md`, and the norm entries for the tema in
`content/age-administrativo-c1/sources/normativa.yaml`.

## Source of every question

- The fact comes from the article the lesson cites, read in the norm file in `sources/normativa/`
  (`pdftotext -layout`), or from the saved page in `sources/otros/` the lesson cites. Use the version the course cites:
  where `normativa.yaml` lists `cambios_pendientes`, the later version.
- Never from an official key, never from memory. If the lesson and the norm disagree, the norm wins and you report it.
- The citation must be one the lesson's prose also cites (same norm, same article): the platform rejects a question
  whose citation its lesson never cites. Write it as the lesson writes it: «art. 167.1 CE», «art. 33.2 LOTC»,
  «art. 2.1 LO 3/1981», «art. 24.6 Ley 19/2013», «art. 16.4 TUE», «disposición adicional cuarta Ley 19/2013»,
  «(fuente: `file.html`)» only for a saved page. One article per citation; add the apartado and letter when the fact
  sits there.

## Coverage order

1. Every line of the lesson's «Lo que más cae» block: at least one question each (two where the line holds two facts).
2. Every fact asked by an official question filed under the tema (`official/I.TT.md`, 2022–2025 first, then 2020):
   at least one question, never with the official stem and options; change the angle (ask the other half of the
   article, another distractor set, another stem form).
3. The rest of the lesson's citable facts, section by section, in lesson order, until the quota.

Do not ask about a fact the lesson does not state. Do not ask the same fact twice with the same angle.

## Form (style guide § 2–7, § 12)

- Four options a)–d), exactly one correct under the cited text and under every other norm in force.
- Stem: a sentence to complete ending in «:» or a question «¿…?». Name the norm with its BOE title the way the official
  exams do («la Constitución Española de 1978», «la Ley Orgánica 2/1979, de 3 de octubre, del Tribunal
  Constitucional», «la Ley 50/1997, de 27 de noviembre, del Gobierno»). Name the article where the mix calls for it.
  Follow the tema's stem-form targets (plan § 3, profile N; I.6 profile G). Stem 15–40 words.
- No negative stem unless you are using the tema's allowance (at most 1 in 20; capitals: «NO», «INCORRECTA»).
- No option is an article number, «Ninguna de las anteriores», «Todas son correctas» or a letter combination.
- Options share grammatical form and register, 5–20 words (statements up to 40). None absurd or wrong on spelling.
- The correct option is the norm's wording or a faithful reduction. Distractors from one or two patterns: the norm's
  sentence with one word changed («texto alterado»), a sibling figure, another plazo or number from the same norm, the
  organ one level off, the superseded rule (only where the amendment is itself examinable). Each distractor must be
  wrong by the cited text, not merely unusual. Never a distractor that is also correct.
- Length: across your tema, the key is the strictly longest option in about a quarter of the questions (20–28 %).
  Vary it on purpose; never always-longest, never always-shortest.
- Organ names: current names (RD 829/2023). A question about an old name only if the norm text still says it, and then
  the stem quotes the norm.
- Spanish: Peninsular, correct accents and typography («», no stray characters). The explanation follows the voice page.

## Fields per question (JSON)

One file per tema: `docs/age-verification/bank/bloque-i/m01-lTT.draft.json`, a list of objects:

```json
{
  "id": "m01-l01-q001",
  "tema": "I.1",
  "section": "La reforma de la Constitución",
  "citation": "art. 167.1 CE",
  "stem_form": "art-completar",
  "names_article": true,
  "negative": false,
  "prompt": "De acuerdo con el artículo 167 de la Constitución Española de 1978, …:",
  "options": {"a": "…", "b": "…", "c": "…", "d": "…"},
  "correct": "d",
  "difficulty": 2,
  "tags": ["mayoría"],
  "distractor_pattern": "cifra-cercana",
  "explanation": "…",
  "source_quote": "Los proyectos de reforma constitucional deberán ser aprobados por una mayoría de tres quintos de cada una de las Cámaras.",
  "covers": ["lmc-1", "official:conv2025_A·P1·1"]
}
```

- `stem_form`: one of `art-completar`, `art-pregunta`, `directa`, `cual`, `enunciado`, `senale`, `norma-sin-art`
  (plan § 3, in that order).
- `tags`: from `plazo`, `órgano`, `mayoría`, `cantidad`, `composición`, `concepto`, `competencia`, `procedimiento`,
  `fecha`, `requisito`, `efecto`, `estructura`, `excepción`; one to three.
- `difficulty`: 1 the fact is a «Lo que más cae» line or a headline number; 2 a detail of the article; 3 an exception,
  a second apartado or a fine distinction between neighbouring rules. Target 30/50/20 %.
- `distractor_pattern`: `texto-alterado`, `otra-figura`, `otro-plazo`, `cifra-cercana`, `organo-nivel`,
  `norma-anterior`, `mixto`.
- `explanation`: one paragraph: why the key is right (quoting the norm briefly) and why each distractor is wrong.
- `source_quote`: the exact sentence(s) of the norm that contain the answer, copied from the pdftotext output.
- `covers`: `lmc-N` for the N-th «Lo que más cae» line it tests; `official:<code>·<part>·<n>` for an official
  question whose fact it tests (as headed in `official/I.TT.md`).
- Spread the key evenly over a–d across the tema: the build keeps the authored order (the platform shuffles per
  learner). The explanation names options by content, never by letter or position.
- Ids run from `q001` in authoring order. A replacement for a dropped question takes the next free number.

## What you hand back

The draft file, plus `m01-lTT.writer-notes.md`: lesson/norm disagreements found, facts left out and why, and the
coverage list (each «Lo que más cae» line and each official question → question ids).
