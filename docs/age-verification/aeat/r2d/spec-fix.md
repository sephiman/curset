# AEAT round R2d — standalone reader and fixer (build pass), 2026-11-17

You are a reader-fixer (Sonnet). No questions. Do not spawn sub-agents. Read once: `spec-build.md`, the «Platform
constraint» of `spec-write.md`, `docs/prose-voice.md`. Edit only your lessons.

## 1. Read (only where `r2d/<lesson>/standalone.md` does not exist yet)

Read the whole built lesson in order. Flag every sentence (or esquema row) that does not stand on its own where it now
sits: a pronoun, «ese/esa/estos», «el artículo», «este apartado», «la letra b)» or an elided subject whose referent is
missing or is only in an esquema, citation or far-away paragraph; a list with no lead-in; a lead-in that claims more
than the list it introduces; a repetition two items apart; a «Normativa» line that lists an article the lesson never
cites or misses one it cites. The builder's own list in `build.md` is a starting point, not the answer. Write
`r2d/<lesson>/standalone.md`: `| id | line | sentence (start) | problem | minimal fix |`, ending «Flagged n».

## 2. Fix (every flag), in this order of preference

1. **Move** the sentence next to its referent, or **add** the verified pool sentence (`r2d/expansion/<lesson>.md`,
   byte-identical) that supplies the referent. No new text: nothing for Opus to check.
2. **Minimal rewording**: replace only the dangling words with the noun, article or apartado they stand for, taken from
   the law (open the article in `content/aeat-agentes-hacienda/sources/`). Keep every other byte; never shorten.
3. Normativa lines: rebuild to exactly what the lesson cites (R2's ruling in `spec-verify.md`).

A repeated rule is removed (keep the fuller copy). «entre otros/as» that is the article's own wording stays (the legal
list is open; removing it makes it read as closed — Opus FAIL, III.5). Only an «entre otros/as» the course added in place
of missing items is a flag: complete the list from the pool.

## 3. After the fixes

- `cd backend && uv run python ../docs/age-verification/aeat/r2d/tools/build_check.py <lesson>`: «not in pool» must
  list exactly your reworded sentences and the Normativa lines — nothing else.
- `uv run python ../docs/age-verification/aeat/r2-tax/tools/cites.py <lesson>` (0 unresolved) and
  `uv run python scripts/index_sources.py --course aeat-agentes-hacienda` (no error naming your lesson).
- Append to `standalone.md` a section «## Fixes»: per flag, moved / pool sentence added / reworded (old → new, with
  the article checked) / removed. The reworded ones go to a blind Opus check.

Final message: per lesson, flags n, moved n, pool-added n, reworded n, removed n, and the build_check line.
