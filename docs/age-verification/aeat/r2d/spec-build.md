# AEAT round R2d — build pass (replaces the reduction pass), 2026-11-17

Juanjo's method: **build, do not cut.** Each lesson is rebuilt from its pre-R2d text (git HEAD) by adding whole
sentences copied byte-identical from the verified expansion. You are a builder (Sonnet). No questions. Do not spawn
sub-agents. Read once: this file; the «Platform constraint» of `r2d/spec-write.md`; `docs/prose-voice.md`.

## Inputs per lesson

- Base: `git show HEAD:content/aeat-agentes-hacienda/es/lessons/<lesson>.md` — start by writing it to the lesson file,
  unchanged.
- Pool: `docs/age-verification/aeat/r2d/expansion/<lesson>.md` — the R2d expansion. Every sentence in it passed a
  blind check (the checker proves it; anything you copy that did not pass shows up as «not in pool»).
- Map: `docs/age-verification/aeat/r2d/<lesson>-map.md` (ranges, article rows, review items, R2b removals, «Coordinator
  notes»), and the audit `docs/age-verification/aeat/r2d/audit/<lesson>.md`.

## What to add (whole sentences, byte-identical, never trimmed, merged or reworded)

a. Everything R2b removed that the map places inside an epígrafe's range.
b. For each review item the map confirmed: the sentences that state it.
c. **Every article inside the range that HEAD does not treat (or treats in part): at least the whole sentences that
   state its rule, its conditions and its exceptions** — usually two to four. If no small set of whole sentences does
   that, take the shortest set that does and note it. Completeness wins over size: no article ends «not treated» or
   «listed, not developed», nothing is dropped for size.
d. The «No confundir» blocks and (III.15) the estimación objetiva paragraph, as written in the pool.
e. A HEAD sentence that the pool holds in a corrected form (a verifier's fix, a removed `m03-lNN` id, the RDL 29/2026
   convalidation wording, a completed clause) is replaced by its pool version.

A «sentence» is what the provenance splitter cuts (ends at «.», «:», «;» followed by a capital or line end; a list item
is one unit; a table row is one unit). You may take some sentences of a pool paragraph and not others, and place a
sentence in a new paragraph, but each sentence's bytes stay exactly as in the pool. You may add headings (`##`,
`###`) to place added material in the norm's order; you write no prose of your own.

## Enumerations

A legal enumeration is complete, as an esquema: one row per item with its citation. If the pool already has an
esquema for it, copy those rows. Otherwise build rows from the pool's verified list items:
`| <letter or ordinal> | <the item's text exactly as in the pool, without its leading marker> | <the citation of the
lead-in sentence> |` under `:::esquema{kind=tabla title="<what the list is>"}` and a header row. The prose keeps one
verified sentence introducing the list (with its citation, which the rows repeat — platform constraint).

## Size

Target: 1.6 × the HEAD word count, esquema rows excluded. It is a target, not a limit: when a lesson passes it, keep
added articles to their rule/conditions/exceptions sentences and every enumeration in an esquema, and report the size.

## Normativa, «Lo que más cae», readability

- «Normativa»: rebuild each line from what the built lesson cites (format of R2's spec; «nombrado en …» lines and the
  final «… no figuran en `normativa.yaml`» line as the pool has them, kept only for norms the built lesson names). New
  Normativa lines are the one place new text is expected: list them in your notes.
- «Lo que más cae»: HEAD's ten lines; take a pool version of a line only under (e).
- Readability: run `cd backend && uv run python ../docs/age-verification/aeat/r2d/tools/split_paragraphs.py <lesson>`
  at the end (it keeps every sentence's bytes).

## Checks and notes

1. `cd backend && uv run python ../docs/age-verification/aeat/r2d/tools/build_check.py <lesson>` — must end with «not in
   pool» listing only your new «Normativa» lines (anything else: replace it with pool text or remove it).
2. `uv run python ../docs/age-verification/aeat/r2-tax/tools/cites.py <lesson>` (0 unresolved) and
   `uv run python scripts/index_sources.py --course aeat-agentes-hacienda` (no validation error naming your lesson).
3. Append to the map `docs/age-verification/aeat/r2d/<lesson>-map.md` a section «## After build (2026-11-17)»: one
   row per article of the ranges: treated (full) / treated (rule, conditions, exceptions) / chapter level / out (the
   map's allowed reason). No «not treated» inside a range.
4. Write `docs/age-verification/aeat/r2d/<lesson>/build.md`: words HEAD → built (and esquema-row words separately),
   ratio to HEAD (excl. esquema rows) and to the 1.6 target; sentences added by category (a)–(e); enumerations as
   esquemas; the build_check line; the «not in pool» lines.

Final message: per lesson words HEAD → built (excl. rows), ratio, sentences added per category, «not in pool» count.

## Clarifications (2026-11-17, after the first three builds)

- (c) means the sentences that state an article's rule, its conditions and its exceptions — usually two to four whole
  sentences per article, not every pool sentence of the article. Completeness wins over size only in this sense: every
  article gets those sentences, and every legal enumeration stays complete (as an esquema).
- Nested enumerations become esquemas too: one row per item or sub-item (`| 20.Uno.8.º a) | <sub-item text exactly as
  in the pool> | art. 20.Uno LIVA |`). The checker accepts a row whose cell is a verbatim contiguous part of a verified
  item («verbatim sub-item»).
- Nothing is left out «for size». Within an added article, a pool sentence is left out only because it does not state
  the rule, a condition or an exception (development, procedure, repetition); the build notes say so per sentence.
