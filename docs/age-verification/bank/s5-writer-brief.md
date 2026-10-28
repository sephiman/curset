# Session-5 writer brief: replacements and table facts (R3, 2026-10-23)

You write new questions for one lesson of bloques IV–V. Read `writer-brief.md` and `bloque-ii/spec.md` whole and
follow them; this page only says what to write and where. Do not commit; do not edit lessons, content, tests, goldens,
other drafts or `drops.tsv`.

**Your file:** `<bloque>/<lesson>.s5.draft.json` plus `<lesson>.s5.writer-notes.md`. Ids start at the first id named in
your prompt and run up from there. Keep scripts in `<scratchpad>/<lesson>-s5/`.

**What to write**, in this order:
1. **Replacements.** For each id your prompt lists as failed, read its row in `<bloque>/drops.tsv` (the reason) and
   the question in the lesson's draft. Write one new question for the same fact, from a new angle and with new options.
   Do not reuse the failed stem. Avoid the fault named in the reason. Where the failed question claimed a `covers`
   code, the replacement claims it too, so the codes `tools/lost_coverage.py <bloque> <lesson>` prints come back.
   Check `official/<tema>.md` for that code first: same fact, but never the official key together with an official
   distractor.
2. **Table facts.** Markdown table cells that hold only citations now anchor (`art. 64.1 RD 364/1995` in a «Cita»
   column resolves like a parenthesised citation). For every table row in your lesson whose fact no kept question asks
   (the kept questions are those in the drafts whose id is not in `drops.tsv`), write one question citing the row's
   cell as written. Your prompt names the tables.
3. Anything else your prompt names, such as held questions.

**Rules that tightened in re-verification** (verifiers fail these):
- Citation (check 3): if half the key rests on a second article or norm, the citation must name it, or the question
  must be on one half only. The citation field takes one article. So ask one half; never key «both texts say…» on
  one citation.
- Explanations are checked like the key. Every claim about a distractor must hold under the norm. Do not write a rule
  the norm does not state.
- A stem names the norm by its BOE title, or by number and date when the title would push past 40 words. Never by
  number alone («la Ley 30/1984») and never by an acronym («la IOC», «la LGP»).
- Unexpanded acronyms (IGAE, LGP, IOC) do not go in options or stems.
- Stem and options read as one grammatical sentence. Do not repeat the stem's last words in every option.
- No option rules itself out by its own wording («… y no constituya falta muy grave»).
- Keep option wording parallel, so the key is not the only option with or without a qualifier.
- Organs: an option naming an organ is wrong only if the norm gives the act to another organ. Check that no
  distractor's organ can also perform the act asked (e.g. a Director general who can both start and sanction).

**Do not use** lesson sentences added or changed in this session's lesson fixes: `git diff HEAD -- <lesson file>`
shows them, and they are unchecked. Questions on them come in a later pass. Use only text that is the same as in HEAD.

Before hand-back, for your `.s5` file:
- run `lint_drafts.py` and `bank_stats.py` (pass the stem `<lesson>.s5`);
- run the anchor check (`check_anchors.py` reads `mBB-l*.draft.json`; call `_anchor` directly on your file the same
  way);
- check every `source_quote` against the pdftotext output;
- print each stem with its keyed option.

Final message: count by kind (replacement / table fact / other), covers restored, covers you could not restore and
why, anchor misses (0). Keep it short.
