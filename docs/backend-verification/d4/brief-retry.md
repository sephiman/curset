# Round D4, Part C — one retry of a dropped family (Sonnet writer)

You rebuild families that D3 dropped. Each gets ONE build and ONE blind check; a family that fails that check is dropped for
good (no fix pass). So get it right before handing over. Never commit; never run git stash, checkout, reset or restore.
Work folder `docs/_work/backend-in-depth/d4/<writer>/`: `decisions.tsv` (id `D4-C-<writer>-n`, lesson, decision, rule),
`progress.md` after every family, `cost.tsv`, `registration.md`.

Load once: `CLAUDE.md`, `docs/prose-voice.md`, `docs/backend-question-style.md`, `docs/backend-verification/s1/contracts.md`,
then the D3 brief for the kind: variant families `docs/backend-verification/d3/brief-variants.md` (all 13 rules apply, with
`cases:` per-case `why` and `citation`, and `why:` on every mistake); generators `docs/backend-verification/d3/brief-generators.md`
(rules 2–9 apply; ids `D4-C-…`). Builder `backend/scripts/tech_course/build_variants.py` (read, do not edit; the coordinator owns it).

Before each family, read why it was dropped: the rows of `docs/backend-verification/d3/decisions.tsv` that name it, and the
verifier lines in `docs/_work/backend-in-depth/d3/v-<writer>/verdicts*.txt` (`v-a2` for the two generators; `v-b2`, `v-b3`,
`v-b4` for the variants). The family files were deleted at the drop; you write them again.

Per family, beyond the D3 rules:
1. The lesson must state the fact in a verified, cited sentence; cite that sentence's anchor, or a method-level anchor present in
   `content/backend-in-depth/sources/` that states the exact fact (per case through `cases:` when facts differ by case). If none,
   skip and log. Never edit a lesson.
2. Every per-case `why`, every mistake `why` and every explanation sentence must be true for EVERY variant it appears in. Before
   handing over, print ten variants spread over the exercise (stem, snippet, key, each wrong option with its sentence) and read
   each sentence against that variant's code and output. Fix anything that is true only for some variants.
3. Identifiers, literals, types and outputs in any sentence (stem, why, explanation) are inline code, never bare (`x`, `5`,
   `int`, `BigDecimal`, `"1.0"`).
4. Each mistake is applied where its name says (if the name is "dropping the scale", it changes every place the scale is set,
   not one line) and its output really is that mistake's output; a mistake that compounds two errors is two mistakes or none.
5. Keep 30 to 40 variants; generators cover both levels or log the level trimmed.
6. Tests in `backend/tests/test_variant_families_d4<writer>.py` or `backend/tests/test_backend_generators_d4<writer>.py`, written
   first; `ruff check`, `ruff format`, `mypy` clean on your files.
Report under 25 lines: per family, lesson, anchor, kept, what changed against the D3 failure, test result.
