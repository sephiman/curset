# AEAT round R2d — depth correction (reduction pass), 2026-11-17

Juanjo's correction (R4.7: exam history decides depth; what no exam asked is there, more briefly). Applies to every
lesson that more than doubled in R2d or exceeds 15,000 words (`r2d/words.md`, column «Rule»: REDUCE).

You are a reducer (Sonnet). Read once: this file; `docs/age-verification/aeat/r2d/spec-write.md` («Rules for every
sentence», «Platform constraint»); `docs/prose-voice.md`. No questions. Do not spawn sub-agents. Edit only your
lessons and append to their `r2d/<lesson>/writer.md` a section «Reduction pass».

## What to reduce

Only text added in R2d: `git diff HEAD -- content/aeat-agentes-hacienda/es/lessons/<lesson>.md` shows it (lines with
`+`). Text present at HEAD (before R2d) is not reduced.

1. **Protected articles** keep their full treatment: (a) every article an official question of the pack asks —
   `docs/age-verification/aeat/r2/questions/<lesson>.md`, coverage and reference questions: the «Norma»/evidence
   lines name the article —; (b) every article the lesson's «Lo que más cae» lines cite. List them first in your notes.
2. **Every other article added in R2d** is reduced to its rule, its conditions and its exceptions: two to four
   sentences, verbatim fragments of the article with its citation («(art. 70.Uno.4.º LIVA)»), never the reproduction
   of the whole article. Keep the article's key numbers, plazos, organs and conditions exactly; drop procedural
   detail, repetitions and sub-rules that only develop the rule. Do not paraphrase: cut, keeping the article's words.
3. **Legal enumerations** stay complete (every item, its letter or ordinal, in the norm's words, shortened only by
   cutting trailing detail of an item, never by dropping an item) but move from running prose or long bullet lists into
   an esquema, one row per item:

   ```
   La LIVA declara exentas estas operaciones (art. 20.Uno LIVA):

   :::esquema{kind=tabla title="Exenciones del artículo 20.Uno LIVA"}
   | Número | Operación exenta | Cita |
   |---|---|---|
   | 1.º | Las prestaciones de servicios y las entregas de bienes accesorias a ellas que constituyan el servicio postal universal … | art. 20.Uno LIVA |
   :::
   ```
   Every row's «Cita» must be a unit the prose cites (the lead-in sentence above cites it): use the article/apartado
   the lead-in cites, not the item's sub-unit. An enumeration of a protected article keeps its prose too only if the
   pack asks a single item; otherwise the esquema alone carries it.
4. **Chapter-level sentences** for organisational blocks stay as they are.
5. **Nothing leaves the article map**: a reduced article is still «treated». Do not delete an article's last mention.
6. «No confundir» blocks, worked examples, «Lo que más cae», «Normativa» lines stay; update «Normativa» only if an
   article you cut is no longer cited anywhere in the lesson (it should not happen: keep one citing sentence).

## After each lesson

`cd backend && uv run python ../docs/age-verification/aeat/r2-tax/tools/cites.py <lesson>` (0 unresolved) and
`uv run python scripts/index_sources.py --course aeat-agentes-hacienda` (no validation error naming your lesson).
Notes: protected articles; per reduced article, words before → after; enumerations moved to esquemas; words of the
lesson before → after (`wc -w`). Final message: per lesson words before → after.

## Corrections after the first reducer (2026-11-17)

- **Protection is per unit, not per article.** Protected = the apartado, number or letter an official question asks
  (e.g. art. 20.Uno.9.º LIVA, not the whole art. 20) and the units «Lo que más cae» cites. The rest of the same article
  is reduced like any other added text.
- **Cut by judgement, never by position.** Keep the sentences that state the rule, its conditions and its exceptions
  (plazos, amounts, organs, «salvo…», «siempre que…»); drop development, repetition, procedural steps. «First N
  sentences» cuts are not acceptable.
- **Esquema rows are short.** Each row gives the item's letter/ordinal and its operative words (the thing listed, cut
  at the first clause that only develops it), not the item's whole text; a protected item may keep its full text.
- **Target size.** Aim for about twice the lesson's pre-R2d length or 15,000 words, whichever is larger. Protected
  units may push a lesson above it; say so in the notes.

> DISCARDED 2026-11-17 by Juanjo; superseded by `spec-build.md`. Kept for the record.
