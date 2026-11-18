# AEAT round R2d — pool-gap writer, 2026-11-18

Juanjo's rule: completeness wins; every article inside an epígrafe's range is treated with at least its rule, conditions
and exceptions. The build took only verified pool sentences, so the articles listed in `r2d/pool-gaps.md` are still
untreated or only partly treated. You close them. You are a writer (Sonnet). No questions. Do not spawn sub-agents.

Read once: this file; `r2d/spec-write.md` (all of it: «Rules for every sentence», enumerations, Normativa ruling,
«Platform constraint»); `docs/age-verification/aeat/r2-tax/spec.md` § «Writer» → «Rules for every sentence»;
`docs/prose-voice.md`. Per lesson: its row in `r2d/pool-gaps.md`, its map (`r2d/<lesson>-map.md`, including
«Coordinator notes» and «After build»), `r2d/<lesson>/build.md`, and the lesson.

## For each gap, in this order of preference

1. **The pool has the sentence (no PASS yet):** copy it byte-identical from `r2d/expansion/<lesson>.md` into its place
   in the norm's order. If it is the same text as a sentence that FAILed in a report, take the report's replacement
   instead.
2. **The pool has nothing:** write the rule, its conditions and its exceptions in the norm's words (a faithful cut that
   keeps every condition, plazo, amount, organ and «salvo»), each with its citation, from the saved text in
   `content/aeat-agentes-hacienda/sources/` only — never memory, never academy material. Usually two to four
   sentences per article; a legal enumeration complete as an esquema (`| Elemento | Contenido | Cita |`, each row's
   citation one the prose cites, no prose inside the block).
3. **Chapter-level rows** (whole titles of a Reglamento or law the map treats at chapter level): one sentence per
   article stating its rule, unless the map's «Coordinator notes» fix a depth rule for that block — follow them.
4. A source you cannot read: leave the article out and list it.

Never reword or remove existing lesson text, except a lead-in that now claims less than the list it introduces.
Rebuild the «Normativa» lines for what the lesson now cites (R2's format and ruling). No «No confundir», no worked
examples, no «Lo que más cae» changes.

## Checks and notes

- `cd backend && uv run python ../docs/age-verification/aeat/r2-tax/tools/cites.py <lesson>` (0 unresolved) and
  `uv run python scripts/index_sources.py --course aeat-agentes-hacienda` right after writing; if it fails on your
  lesson, fix it at once (other agents depend on it).
- Append «## Gap fill (2026-11-18)» to `r2d/<lesson>-map.md`: per gap article, «pool sentence added», «written», or
  «left out: <reason>».
- Write `r2d/<lesson>/gaps.md`: every sentence or row you added (first 80 characters, line), marked pool / written.

Never touch other lessons, `course.yaml`, the glossary, C1, C2 or other courses. Never `pkill`; no git stash. Final
message: per lesson, gaps closed (pool / written), left out with reason, words before → after.

## Added 2026-11-18

- A pool sentence that is byte-identical to a sentence of a C1 or C2 lesson (`content/age-administrativo-c1/`,
  `content/age-auxiliar-c2/`) is already verified there (inherited provenance): `build_check.py` now accepts it. In the
  common part (m01-*, m02-*), first add every such pool sentence of the range the build left out (it states a rule,
  condition or exception), then the rest.
