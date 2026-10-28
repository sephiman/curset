# Writer brief — bloques II–V (coordinator's standing instructions)

You are a question writer for the question bank of the course `content/age-administrativo-c1` (repo
/home/juanjo/PycharmProjects/curset), round R3. Do not commit. Do not edit lessons, content, tests or goldens; write
only your draft and notes under `docs/age-verification/bank/<n>/`. Other writers work in parallel, some on other parts
of your own tema.

Your spec is `docs/age-verification/bank/bloque-ii/spec.md` (shared by bloques II–V). Read it whole and follow it
exactly. It tells you what to read first (style guide whole, plan § 3, prose voice, CLAUDE.md, the lesson, the
official questions, normativa.yaml, the theory ledger's standing conventions), where facts come from (the cited
article in `sources/normativa/` via `pdftotext -layout`, never official keys, never memory), the form rules, the JSON
fields, the length guard and the anchor check.

- If you have a part of a split tema: write only on facts in your line range; cover the «Lo que más cae» lines and the
  official questions whose fact sits in your range; ids only inside your range; your files are
  `<lesson>.part-<k>.draft.json` and `<lesson>.part-<k>.writer-notes.md`.
- Stats: `python3 docs/age-verification/bank/tools/bank_stats.py <n> <draft-stem>` (the stem is `mBB-lTT` or
  `mBB-lTT.part-<k>`): length-edge z and longest-is-correct z within ±1.5 before you hand back.
- Anchors: from `backend/`, call `CourseCitations.build(...)._anchor('<lesson>', citation, 'es')` the way
  `docs/age-verification/bank/tools/check_anchors.py` does (run with `uv run`); zero misses for your file.
- Check by script that every `source_quote` is an exact substring of the pdftotext output (whitespace normalised).
- Write the JSON with a Python script (json.dump, ensure_ascii=False, indent=1), so it is always valid. Keep your
  generator script in your own scratchpad subfolder named after your draft (`<scratchpad>/m04-l05-part-2/`), never at
  the scratchpad's top level (other writers share it), and not in the repo.
- `covers` codes for official questions: `official:<code>·P1·<n>`, reserves `P1R`, supuestos `S1`/`S2`, their
  reserves `S1R`/`S2R` (e.g. `official:conv2025_A·S2·17`).
- Official questions, supuestos included, are the commonest drop («lightly reworded»: same fact, angle and key plus
  one official distractor carried over, even reworded). When you cover one, change the angle and reuse none of its
  options' content. In bloque III about one question in six fell this way; a computation case with the official
  case's shape and new figures is still a rewording.
- Stem forms over your draft: about 38 % «De acuerdo con el artículo X…:», 15 % «Según el artículo X…, ¿…?», 22 %
  direct «¿…?» naming no article, 14 % «¿Cuál de las siguientes…?», 6 % statements to complete with no norm named, the
  rest «Señale…» or «Según la [norma]»; about half the stems name an article. `bank_stats.py` prints the mix.
- A stem that names a norm uses its BOE title («la Ley 47/2003, de 26 de noviembre, General Presupuestaria»), never a
  short name; number and date alone only when the full title would push the stem past 40 words. Otherwise write a
  stem that names no norm, if no other norm in force changes the answer.
- Stem 15–40 words; only a **date** computation may run to 50 (an amount computation may not).
- Before hand-back run `python3 docs/age-verification/bank/tools/lint_drafts.py <n> <draft-stem>` and fix every flag
  that is a real fault («de el», a norm title without «la», English quotes, long stems, lowercase negatives); short
  options are allowed only for an organ, quantity or figure name. Tag date computations `cómputo`.
- Set `correct` in your script from the key's text, never by hand, and print each stem with its keyed option before
  hand-back: in bloque V a batch went out with six keys on the wrong option.
- Explanations name options by content, never by letter or position.
- Verifiers fail: any negative stem whose «no» is lowercase (write «NO», «INCORRECTA»; or rephrase positively); an
  option that breaks the shared form or is absurd for the stem; an old organ name in your own words (only quoted
  from the norm, with the stem saying so).

Final message to the coordinator: authored count, the bank_stats lines for your draft, anchor misses (0), «Lo que más
cae» lines covered, and any blocker (a fact the questions need that the lesson lacks, or the target unreachable from
citable facts). Keep it short.
