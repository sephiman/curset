# Writer spec — C2 question bank, authored delta (round R3, 2026-11-07)

You write questions for the course `content/age-auxiliar-c2` (repo `/home/juanjo/PycharmProjects/curset`). Do not
commit. Do not edit lessons, content, tests or goldens. Write only your draft and notes under
`docs/age-verification/c2/bank/<bloque>/`. Most of the tema is already covered by questions copied from C1 (the «kept
derived candidates»). You write only what is still missing: the **delta**.

## Read first, once per run

- `CLAUDE.md` (writing rule) and `docs/prose-voice.md` (explanations are prose: the voice applies).
- `docs/age-c2-exam-style.md` whole. It is the C2 guide, not C1's: forms, lengths, distractors, checklist § 12.
- `docs/age-c2-bank-plan.md` § 3 (mix, article share, negatives, key-longest).
- Ofimática temas (II.5–II.12): `docs/age-c2-ofimatica-index.md`, and C1's rules for list-shaped temas in
  `docs/age-verification/bank/bloque-vi/spec.md` sections «Source of every question» and «Form», read with
  `content/age-auxiliar-c2/` for every C1 path. Where they differ, this page and the C2 style guide rule.
- Norm temas (bloque I, II.1–II.4): C1's `docs/age-verification/bank/bloque-ii/spec.md`, read with
  `content/age-auxiliar-c2/` for every C1 path. The facts come from the cited article in
  `content/age-auxiliar-c2/sources/normativa/` via `pdftotext -layout`.
- C1's practicalities in `docs/age-verification/bank/writer-brief.md`: a scratchpad subfolder named after your draft,
  JSON written by script, `correct` set from the key's text, every stem printed with its keyed option before
  hand-back.

Per tema:

- the lesson `content/age-auxiliar-c2/es/lessons/<lesson>.md`;
- its **delta sheet** `docs/age-verification/c2/bank/<bloque>/delta/<lesson>.md` (quota, kept count, stem forms
  still needed, «Lo que más cae» lines, the kept candidates by cited unit);
- the official pack `docs/age-verification/c2/<bloque>/questions/<lesson>.md`;
- the R2 records' notes on the lesson if a fact looks odd (`docs/age-verification/c2/<bloque>/<lesson>.md`).

## What to write

1. **Every «Lo que más cae» line** that no kept candidate tests: at least one question.
2. **Every coverage question of the official pack** whose fact no kept candidate tests: one question with a new
   angle, never its stem or options, never its key paired with one of its distractors (C1's commonest drop).
3. **Every fact the C2 lesson states that no kept candidate tests**: for ofimática, item by item of the lesson's list
   and the facts of each item's cited page within that feature. For norm temas, sentence by sentence of the lesson,
   up to the depth of the lesson (C2 depth: never an article the C2 lesson does not cite).
4. **Up to the quota**, with the stem forms the sheet says are short: write those forms first and none of a form
   whose «need» is negative. Plus about 15 % for drops.

Do not duplicate a kept candidate: same fact **and** same angle. The same fact from another angle (path vs effect,
plazo vs organ) is fine.

## Rules (C2)

- **Source:** only what the lesson cites, in this course's snapshot. For ofimática, a saved page in
  `content/age-auxiliar-c2/sources/otros/` that the lesson cites. For norms, the article in `sources/normativa/`.
  Never an official key, never memory.
- **Platform (ofimática):** Windows 11 and Microsoft 365 desktop only (Anexo I 2.2). No question on a fact a page
  gives only for Windows 10, the web, Mac or mobile, even with the platform named in the stem (coordinator,
  2026-11-07). Where classic and new Outlook differ, the stem says which.
- **Stems:**
  - Bloque I and II.1–II.4 name the norm by its BOE title, never an acronym, with the article where the question
    rests on one. Forms and shares follow the sheet: in II.1–II.4 the dominant form names the norm **without** an
    article and completes the sentence (2025: 58 %), and the stem may quote a definition (up to 55 words). In bloque
    I, «Conforme al artículo X de la [BOE title], …:» is the dominant form (41 %), and about 69 % of stems name an
    article.
  - Ofimática names the application and version («Windows 11», «Microsoft Word 365», «Microsoft Excel 365»,
    «Microsoft Access 365», «Microsoft Outlook 365»; «configurado en español» when a shortcut or label depends on it).
    II.5 and II.12 concept questions name none. 2025 often describes the path before asking. Write some of those.
- **Lengths** (checklist 14, 21):
  - bloque I: stem 20–40 words.
  - II.1–II.4: stem 20–55 words.
  - ofimática: stem 15–35 words, up to 50 with a path or formula.
  - options: 3–20 words, statements up to 40; ofimática names 1–3 words; behaviours one sentence of 8–20 words.
- **Four options**, one correct. No «Ninguna», «Todas», combined options or article numbers. Distractor patterns of
  the guide § 6 for the set. Each distractor is wrong by the cited text or page.
- **Negative stems:** at most one per 20 of the tema (ofimática: one per application per 20), word in capitals.
- **Key-longest:** across your draft, the key is strictly the longest option in about a quarter of the questions
  (chance for four options); fewer is a tell too (bloque II's course guard failed at 18 %). Never pad a key or gloss it in the stem's words.
- **Organ names** current (RD 829/2023, RD 1009/2023, RD 210/2024). **Date computations** show the calendar in the
  explanation and are tagged `cómputo` (the stem still stays within 40 words in bloque I).
- **Explanations:** written by hand, one per question, never patched by script (II.8 lost 56 of 92 to source
  sentences appended by script: «no es lo que dice la página» still fails). Say why the key is right and why each distractor is wrong, naming each by its content, never by
  letter or position, and never dismissing a distractor because the source is silent about it.
- **Fields:** `id`, `tema`, `section` (the lesson's `##` heading), `citation` (the lesson's form; `fuente: \`file\`;
  «label»` for pages), `stem_form`, `names_article`, `negative`, `prompt`, `options` {a–d}, `correct`, `difficulty`
  (target 30/50/20 %), `tags`, `distractor_pattern`, `explanation`, `source_quote` (exact sentence from your text
  extraction, checked by script), `covers` (`lmc-N`, `official:<code>`, e.g. `official:2025-P2-32`, `fact:<short>`),
  `lesson_anchor` (the anchor the check prints).
- **Ids:** continue from the id the delta sheet gives, in order. Draft file
  `docs/age-verification/c2/bank/<bloque>/<lesson>.authored.draft.json`, notes `<lesson>.authored-notes.md`. If you are
  given a part, use `<lesson>.authored-p<k>.draft.json` and the id range you are given.

## Checks before hand-back

From `backend/`: `uv run python ../docs/age-verification/c2/bank/tools/check_draft.py <draft>` must show 0 anchor
misses and no STYLE line, and the mix printed there should move the tema toward its targets. Then
`python3 docs/age-verification/bank/tools/lint_drafts.py ../c2/bank/<bloque> <draft stem>` (the file name without `.draft.json`): fix every real flag.

## Notes and final message

Notes: «Lo que más cae» line → id (kept or yours); official coverage question → id; facts left out and why; the
check outputs. Final message to the coordinator: authored count, anchor misses (0), lines and official questions
covered, blockers. Short.
