# Edition step 1 — decisions taken without asking, and where to resume

Dates 2026-11-18/19. Tools in `edition/tools/`; per-step outputs in `edition/` (budget.json, coverage-a.json, b/, reader/, restore/, selection/, patches.json, swap.json, report.md).

## Decisions taken without asking

1. **Tags rebuilt.** `r2d/tags/` had 9 of 33 files, and `tag_origins.py` read «pre-R2d» as `git show HEAD`, which is now the R2d commit. It reads `r2d/base-commit.txt` now; all 33 files regenerated (`edition/tools/fast_tags.py`: the same tagger without the quadratic row-twin scan and the backtracking regex that made the run take hours). A stale tag run from another terminal was killed because it would have overwritten the new files.
2. **Words.** «Prose» = sentences of paragraphs and list items; esquema rows, tables outside `:::esquema` (treated as esquemas), headings and fences excluded; «Lo que más cae» and «Normativa» lines included in «now». Budget = 1.1 × pre-R2d prose (`aeat-edition-plan.md`). m00-l01 is unchanged.
3. **Concepts** = the lesson title (the programme sentence, verbatim) split mechanically at sentence ends, commas and colons; eight Sonnet readers refined them by reading each lesson outline (`b-brief.md`). Rank 1–2 picks are forced (never cut); rank 3 only while the budget lasts.
4. **«The estimación objetiva paragraph»** = the pool paragraph of III.15 that opens «Los contribuyentes que reúnan las circunstancias previstas en las normas reguladoras de la estimación objetiva» (category d).
5. **Esquemas** stay when an official question rests on them, a reader listed them, a restore needs them, or they gather two or more cited units that the kept prose cites; a kept lead-in (a sentence that ends in «:») brings the list items or esquema that follow it, and the other way round. No esquema was dropped for lack of an anchor.
6. **«Lo que más cae»** items stay when every unit they cite is cited in kept content, or an official question rests on them. They count in «now».
7. **Bank anchors.** The registry's own citation check (paragraph level, parenthesised citations only) is the oracle: `anchors.py` loops write → check → restore the shortest pool sentence that carries the lost citation, until clean. Restored sentences are category a.
8. **Reader flags** (130): 127 solved by restoring the neighbouring pool sentence; 3 left as they are because they are verbatim norm text (m03-l16 «el requisito del apartado 1», m03-l18 «artículo 14» inside a LIVA art. 25 cell, m03-l19 a pool row whose item d) the pool never had) — `reader-unsolved.md`.
9. **Cross-references.** The pool had reworded the id form («m02-l01») into «tema II.1». The platform test `pdf/lessonRefLabels` needs the id form, so in m02-l02 the two pool sentences are swapped for their pre-R2d versions (`swap.json`); targets verified to hold the content.
10. **List-marker fixes** (the user's «fix list markers in content»): 14 table rows (a cell ending «: 5.», a flattened «- 1.º», a cell that was only «e) -») lose the marker only; `Normativa` lines that end in a bare article number take no final period. Logged per lesson in `selection/<lesson>.json` (`marker_fixes`).
11. **«Normativa»** is derived text: first rebuilt by script from the kept citations, then every line blind-checked by Opus (three rounds), and the verifiers' corrected lines applied (`patches.json`, 94 swaps, 2 drops). Prose sentences whose citation had been carried by a cut lead-in (m01-l07, m01-l02, m01-l03) were replaced by the verifier's cited version; these are the only new wording in the course and each passed a recheck. After the last check the generator is not re-run: a rebuild would undo the corrected lines.
12. **Summaries** in `course.yaml` were left alone: only one lesson summary would have lost a sentence, and that one (m01-l01) already describes the exercises, not the Constitution (existing error, listed for Juanjo).
13. **Glossary.** Five entries whose origin lesson no longer uses the term went to `glossary-waiting.md`; `r2/glossary.md` rebuilt; links golden regenerated.
14. **Not mine.** `backend/tests/conftest.py` (a registry cache for the test suite) appeared in the working tree during the session; it was left untouched.

## Left open (not fixed)

- About 30 norms that the lessons cite or name have no «Normativa» line (the verifiers list them in the notes of `r2d/<lesson>/verify-edition*.md`: e.g. TRLCPE, RD 829/2023 in I.7; seven laws in III.1; Orden PRE/3581/2007 in III.2; Reglamento interno del Consejo and Protocolo 6 in I.4; Orden HAC/1161/2026 in III.15…).
- Norms named only inside copied law text have no «nombrado en» line.
- The «Normativa» generator mis-credited units between similarly named norms before the verifiers corrected it; it should be rewritten before any rerun (citations → norm by the full norm name, not the first token).

## Where to resume

1. The explanation layer (R4.11) goes on the assembled lessons; the budget left is the difference to 1.4 × pre-R2d: 272k − 221k, about 51k words.
2. Rewrite `normativa.py`, then give every cited norm its line.
3. `reserve/` holds what was left out per lesson (sentence id, origin tag, report path); `pool/` holds the full R2d lessons.
