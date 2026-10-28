# Lesson-fix blind check brief — session 5 (2026-10-23)

You check lesson changes made under `lesson-fixes-brief.md` (repo /home/juanjo/PycharmProjects/curset). You did not
make them. Do not commit; edit nothing except your report.

Read first: `CLAUDE.md`, `docs/prose-voice.md` (its «never does» list is a hard constraint), `lesson-fixes-brief.md`
(the rules), and the theory ledger's «Decisions applied after bloque I».

**What to check.** Take the items listed in `lesson-fixes/<module>/writer.md`, but judge each one from the lesson text
itself (`git diff HEAD -- <lesson>` shows the change) and from the norm, which you open yourself in `sources/normativa/`
(`pdftotext -layout`; the file named in `normativa.yaml`, the later version where `cambios_pendientes` applies). Do not
trust the record's quotes. In m02, ignore hunks that `bloque-ii/prose-gaps/writer.md` records; they were checked
before.

For each item, PASS or FAIL on:
1. **Faithful:** the sentence states what the norm says, with every condition kept and nothing wider; numbers, plazos
   and organs match.
2. **Cited:** the parenthesised citation names the article (and apartado) that holds the fact, and it resolves:
   `CourseCitations.build(...)._anchor(lesson, citation, 'es')` from `backend/`, as
   `docs/age-verification/bank/tools/check_anchors.py` does.
3. **Placed and scoped:** it sits where the fact belongs. A correction changes only what was wrong. A «(hoy: …)» note
   names the organ in force under the norm it cites.
4. **Voice:** it follows the voice page and invents no vocabulary; Peninsular Spanish.

Also check the record's «not done» items: is the reason true (the source really missing, or the item really not a
gap)?

Write `lesson-fixes/<module>/check.md`: a table with item, lesson and lines, the four checks, verdict and a one-line
reason (quote the norm where it is about content), then the counts. A FAIL proposes the exact replacement wording in
one line, so the coordinator can apply it. Final message: short, with counts and the FAIL items.
