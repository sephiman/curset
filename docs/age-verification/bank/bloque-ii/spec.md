# Writer spec — question bank, bloques II–V (R3, session 3, 2026-10-19)

Bloque I's spec (`../bloque-i/spec.md`) with the lessons it taught. Shared by every writer of a tema in bloques II–V;
`<n>` is the bloque folder (`bloque-ii` … `bloque-v`), `mBB-lTT` the tema's lesson. Read in full before writing:
`CLAUDE.md`, `docs/prose-voice.md`, `docs/age-exam-style.md` (whole file; § 12 is the reviewer's checklist),
`docs/age-bank-plan.md` (§ 3 targets), the tema's lesson `content/age-administrativo-c1/es/lessons/mBB-lTT.md`, the
tema's official questions `docs/age-verification/bank/official/<tema>.md`, the norm entries for the tema in
`content/age-administrativo-c1/sources/normativa.yaml`, and the theory ledger's standing conventions
(`docs/age-theory-ledger.md`, «Decisions applied after bloque I» and, for bloque IV, «Which rule applies (TREBEP and the
pre-TREBEP texts)»).

## Source of every question

- The fact comes from the article the lesson cites, read in the norm file in `sources/normativa/`
  (`pdftotext -layout`), or from the saved page in `sources/otros/` the lesson cites. Use the version in force on the
  exam date, i.e. the version the course cites: where `normativa.yaml` lists `cambios_pendientes`, the later version.
- Never from an official key, never from memory. If the lesson and the norm disagree, the norm wins, you leave the fact
  out and you report it in your notes.
- The citation must be one the lesson's prose (or an esquema row) also cites: same norm, same article. The platform
  rejects a question whose citation its lesson never cites. Write it as the lesson writes it: «art. 21.3 LPAC»,
  «art. 16.1 RD 951/2005», «art. 48.3 LOPDGDD», «art. 12.3 RGPD», «disposición adicional cuarta Ley 39/2015»; a saved
  page as «fuente: `file.html`» (the lesson's own form). One article per citation; add the apartado and letter when
  the fact sits there.
- Check every citation before you hand back: from `backend/`, `uv run python ../docs/age-verification/bank/tools/check_anchors.py <n> mBB`
  prints the citations that resolve to no anchor. Zero misses.

## Coverage order

1. Every line of the lesson's «Lo que más cae» block: at least one question each (two where the line holds two facts).
2. Every fact asked by an official question filed under the tema (`official/<tema>.md`, 2022–2025 first, then 2020):
   at least one question, never with the official stem and options. Change the angle: ask the other half of the
   article, another distractor set, another stem form. Never carry the official key together with an official
   distractor into the same question.
3. The rest of the lesson's citable facts, esquema rows included, section by section, in lesson order, until the quota
   plus about 15 % (drops are expected).

Do not ask about a fact the lesson does not state. Do not ask the same fact twice with the same angle. If the tema
cannot reach its quota from citable facts, say so in your notes with the list of what is missing.

## Form (style guide § 2–7, § 12)

- Four options a)–d), exactly one correct under the cited text **and under every other norm in force**. A stem that
  names no norm is read against all of them: if another norm in force makes a distractor true, name the norm in the
  stem or change the distractor.
- Stem: a sentence to complete ending in «:» or a question «¿…?». Name the norm with its BOE title the way the official
  exams do («la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas»,
  «el Real Decreto 951/2005, de 29 de julio, …»). Name the article where the mix calls for it. Follow the stem-form
  targets (plan § 3, profile N). Stem 15–40 words (a date-computation stem may run to 50).
- No negative stem unless you are using the tema's allowance (at most 1 in 20; capitals: «NO», «INCORRECTA»).
- No option is an article number, «Ninguna de las anteriores», «Todas son correctas» or a letter combination.
- Options share grammatical form and register, 5–20 words (statements up to 40). None absurd or wrong on spelling.
- The correct option is the norm's wording or a faithful reduction. Distractors from one or two patterns: the norm's
  sentence with one word changed («texto alterado»), a sibling figure, another plazo or number from the same norm, the
  organ one level off, the superseded rule (only where the amendment is itself examinable). Each distractor must be
  wrong by the cited text, not merely unusual. Never a distractor that is also correct.
- **Length.** Across your tema the key is the strictly longest option in 20–28 % of questions and the strictly shortest
  in no more than about 30 %. The key must not be systematically longer *or* shorter than the distractors: run
  `python3 docs/age-verification/bank/tools/bank_stats.py <n> mBB-lTT` on your draft and hand back only with the
  length-edge z and the longest-is-correct z both within ±1.5 (the course guard fails at ±2). Fix by writing the
  options to similar lengths, not by padding the key.
- **Old organ names.** Current names (RD 829/2023 and later structure decrees) in stems and options. An old name only
  where the norm text still says it, and then the stem quotes the norm («… lo que el artículo X llama "…"»).
- **TREBEP versus an earlier rule.** Where the fact is a TREBEP rule that differs from Ley 30/1984, RD 364/1995, RD
  365/1995 or RD 33/1986 (or the other way round), the stem names the norm; never leave the candidate to guess which
  text applies. Follow the theory ledger's «Which rule applies».
- **Date computations** (plazos, cómputo, silencio, caducidad, prescripción: III.3, IV.4–IV.6, V.2–V.3 and wherever
  else one fits). The stem gives every date the count needs (notification, publication, presentation) and the kind of
  day if the norm leaves it open. The explanation shows the count step by step («el plazo de diez días hábiles empieza
  el día siguiente, martes 3 de marzo de 2026; excluidos sábados y domingos, el décimo día hábil es el lunes 16 de
  marzo»). Check the calendar with Python (`datetime`), never by hand. Rules: art. 30 LPAC (hábiles exclude sábados,
  domingos and festivos; months and years from date to date, and if the month has no such day, the last day of the
  month; a last day inhábil moves to the next hábil; August is hábil in administrative procedure), art. 48 LPAC
  scope rules, and the special rule of the norm itself where there is one (Ley 29/1998 art. 128 August inhábil for the
  contencioso; Código Civil art. 5 where cited). Choose dates whose window holds no national festivo (1 Jan, 6 Jan,
  Viernes Santo, 1 May, 15 Aug, 12 Oct, 1 Nov, 6 Dec, 8 Dec, 25 Dec) and none of the common regional or local ones
  (19 Mar, Jueves Santo, Lunes de Pascua, 24 Jun, 25 Jul, 11 Sep, 9 Oct, 9 Nov…), or name the festivo in the stem.
  The calendar year is real (2025–2027); the weekday you write must be the true one.
- Spanish: Peninsular, «tú» never used in stems (exam register is impersonal), correct accents and typography («», no
  stray characters). The explanation follows the voice page.

## Fields per question (JSON)

One file per tema: `docs/age-verification/bank/<n>/mBB-lTT.draft.json`, a list of objects (several writers of one
engine tema write `mBB-lTT.part-<k>.draft.json` with their own id range; the coordinator merges them):

```json
{
  "id": "m02-l01-q001",
  "bloque": "II",
  "tema": "II.1",
  "section": "Quejas y sugerencias",
  "citation": "art. 16.1 RD 951/2005",
  "stem_form": "art-completar",
  "names_article": true,
  "negative": false,
  "prompt": "De acuerdo con el artículo 16.1 del Real Decreto 951/2005, de 29 de julio, …:",
  "options": {"a": "…", "b": "…", "c": "…", "d": "…"},
  "correct": "d",
  "difficulty": 2,
  "tags": ["plazo"],
  "distractor_pattern": "otro-plazo",
  "explanation": "…",
  "source_quote": "…",
  "covers": ["lmc-3", "official:conv2024_A·P1·21"]
}
```

- `section`: the lesson's `##` heading the fact sits under (exercises are grouped by it, in lesson order).
- `stem_form`: one of `art-completar`, `art-pregunta`, `directa`, `cual`, `enunciado`, `senale`, `norma-sin-art`.
- `tags`: from `plazo`, `órgano`, `mayoría`, `cantidad`, `composición`, `concepto`, `competencia`, `procedimiento`,
  `fecha`, `requisito`, `efecto`, `estructura`, `excepción`, `cómputo`; one to three.
- `difficulty`: 1 the fact is a «Lo que más cae» line or a headline number; 2 a detail of the article; 3 an exception,
  a second apartado, a fine distinction between neighbouring rules, or a date computation with a trap (weekend,
  month end, suspension). Target 30/50/20 %.
- `distractor_pattern`: `texto-alterado`, `otra-figura`, `otro-plazo`, `cifra-cercana`, `organo-nivel`,
  `norma-anterior`, `mixto`.
- `explanation`: one paragraph: why the key is right (quoting the norm briefly) and why each distractor is wrong.
  **Name every option by its content, never by its letter or position** («la opción del Consejo de Ministros», not
  «la b»): the platform shuffles the options per learner and the PDF prints the shuffled letters.
- `source_quote`: the exact sentence(s) of the norm that contain the answer, copied from the pdftotext output.
- `covers`: `lmc-N` for the N-th «Lo que más cae» line it tests; `official:<code>·<part>·<n>` for an official question
  whose fact it tests (as headed in `official/<tema>.md`; reserves `P1R`).
- Spread the key evenly over a–d across the tema (each 25 % ± 5): the build keeps the authored order.
- Ids run from `q001` (or the first id of your assigned range) in authoring order.

## What you hand back

The draft file, plus `mBB-lTT.writer-notes.md` (or `.part-<k>.writer-notes.md`): lesson/norm disagreements found,
facts left out and why, the `bank_stats.py` output for your draft, the anchor check result, and the coverage list
(each «Lo que más cae» line and each official question → question ids). Your final message to the coordinator is
short: counts, the stats line, any blocker.
