# Verifier spec — question bank, bloques II–V (R3, session 3, 2026-10-19)

Bloque I's verifier spec with its rulings. You did not write the questions you check. Requirements R5.4; the test is
`docs/age-exam-style.md` § 12.

Read first: `docs/age-exam-style.md` (whole), `docs/age-bank-plan.md` § 3, `docs/prose-voice.md`, the tema's lesson
`content/age-administrativo-c1/es/lessons/mBB-lTT.md`, and the tema's official questions
`docs/age-verification/bank/official/<tema>.md`. Do not read the writer's notes before you finish your verdicts.

## Per question

Open the cited article yourself in `content/age-administrativo-c1/sources/normativa/` (`pdftotext -layout`; the file
named in `sources/normativa.yaml`, later version where `cambios_pendientes` applies) or the cited saved page in
`sources/otros/`. Do not trust the draft's `source_quote`; find the text yourself. Answer five checks:

1. **Key.** Is the keyed option correct by the cited text?
2. **Unique.** Is exactly one option correct? A distractor that is defensible under the cited text or **another norm
   in force**, or true in a reading a candidate could reasonably take, fails. A stem that names no norm is read
   against every norm in force (for bloque IV: the TREBEP and the pre-TREBEP texts still in force for what the TREBEP
   leaves to them).
3. **Citation.** Does the cited norm + article (+ apartado) contain the answer? Is the lesson citing that same article
   (search the lesson for it)?
4. **Style.** Checklist § 12 items 1–11, 16, 17: stem form and «:»/«¿…?»; norm named by title; no article-number
   option, no «ninguna/todas»/combined option; negative stem only in capitals; correct option is the norm's wording or
   a faithful reduction; distractors from one or two § 6 patterns, each wrong by the text; options share form, none
   absurd; lengths (stem 15–40 words, a date-computation stem to 50; options 5–20, statements to 40); current organ
   names (an old one only quoted from the norm); Peninsular Spanish with no typos; explanation says why the key is
   right and why each distractor is wrong, and is itself correct. **The explanation names options by content: a
   reference to an option by letter («la a», «opción c») or position («la primera», «las dos últimas») fails.**
   **Date computations:** recompute every count with Python `datetime` (art. 30 LPAC unless the norm says otherwise:
   hábiles exclude sábados, domingos and festivos; months date to date; last day inhábil → next hábil; August hábil in
   administrative procedure, inhábil in the contencioso per art. 128 LJCA). A wrong weekday, a festivo in the window
   the stem does not account for, or a wrong count in the explanation fails.
5. **Not official.** The question is not an official question (in `official/<tema>.md`) copied or lightly reworded:
   same stem with the same option set, or the same options re-ordered, fails. Testing the same fact from another angle
   passes.

Rulings (apply them, do not re-open them):
- Option length (checklist 10): an organ, a quantity or a figure name of under five words, of the kind the style
  guide's own § 3 examples show («Diecisiete objetivos.», «Al Delegado del Gobierno.»), does not fail on length alone.
- «Lightly reworded» (check 5) includes: same fact and same angle, the official key, and an official distractor carried
  over, even if the rest of the option set is new.
- A stem that names the norm by a description («la legislación básica estatal de régimen local») counts as the «no
  norm named» form.
- **Stems that name no norm are allowed** (plan § 3 targets about 22 % direct questions and 6 % statements with no norm
  named). Checklist item 2 (norm named by title) applies only when the stem names a norm. A no-norm stem fails only
  if another norm in force makes a distractor true (check 2) or the answer depends on which norm applies.
- A norm named by its number and date («el Real Decreto 203/2021, de 30 de marzo», «el Real Decreto 366/2007, de 16 de
  marzo»), or by the name of the text it approves, counts as named by title when the full BOE title would push the stem
  past 40 words; the official exams do the same.
- Only a **date** computation stem may run to 50 words; an amount computation stays within 40.
- The key being the shortest option is not a style failure on its own; the aggregate length guard is the authority.
- **Check 5 compares stem and options, not the fact** (user decision, 2026-10-22). A question on a norm's own
  sentence that an official question also asks is not a copy when its stem form and its distractors are new; it fails
  only under the «lightly reworded» ruling above.
- **Check 3, a key on two texts:** if part of the key rests on another article or norm that the citation does not
  name, the question fails check 3. Another apartado of the same cited article passes.
- A stem naming the norm by its number alone («la Ley 30/1984») or by an acronym («la IOC») fails checklist 2. The
  short names the official exams use without number («la Ley General Presupuestaria») count as the title.

Any FAIL drops the question. You do not fix it and do not propose a corrected question; state the reason in one line
(quoting the norm where it is about content).

## Report

Write `docs/age-verification/bank/<n>/mBB-lTT.verify-<batch>.md`:

| id | 1 key | 2 unique | 3 citation | 4 style | 5 not official | verdict | reason |
|---|---|---|---|---|---|---|---|

Then a summary: checked, PASS, FAIL by first failing check (key, unique, citation, style, official). Also list, as
notes that do not change a verdict, any lesson sentence you found at odds with the norm. Append one line per FAIL to
`docs/age-verification/bank/<n>/drops.tsv` (columns `id	tema	batch	check	reason`, tab-separated; create the file with
that header if it does not exist; append with `>>`, never rewrite it: other verifiers write to it too). Your final message is short: counts and the failing ids with their check.
