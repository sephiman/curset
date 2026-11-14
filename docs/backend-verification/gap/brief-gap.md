# Gap round brief (2026-11-14) — addendum to `s2/brief-writer.md` and `s2/brief-verifier.md`

Same rules as S2+S3: Sonnet writers, Opus verifiers, never commit, never run git stash/checkout/reset, other
courses and the Android bundle untouched, shared TSVs appended to only. Lessons here are already verified, so
work is additive and must not change a passed sentence, row or question.

## Added prose (G2, G4)

- Insert new sentences where they belong (a new `## ` section with its `<!-- bullets: … -->` line, or new sentences
  in an existing section). Do not edit existing sentences. Add a `## Key points` bullet only when it restates an
  added F sentence.
- List every added sentence, row and key point in `docs/backend-verification/s2/<module>/<lesson>.additions.tsv`:
  `A<n><TAB>section heading<TAB>exact sentence` (ids continue after the file's last `A` id; create it if absent).
- Append each added testable fact to `<lesson>.facts.tsv` with the next free `fNN`, same five columns.
- Verifier: append to `<lesson>.verdicts.tsv` one line per `A<n>` (`A3<TAB>pass` / `A3<TAB>fail<TAB>reason`), then
  the new questions, then `# gap: checked N, passed P, failed F`.
- Fix: a failed added sentence is rewritten once (`<lesson>.rewrites.tsv`, id `A<n>`), rechecked, deleted on a
  second failure.

## Added questions (G3, G4, G5)

- Appended to `<lesson>.questions.json` and `<lesson>.refutations.yaml` with ids after the lesson's last `qNN`,
  only from facts no earlier question used (written or discarded: check the `fact` field of every entry).
- One batch per lesson, sized to the unused facts that support three refutable wrong options; never forced.
  Judgement content (J blocks, Tier B/C) is never a key. If no unused fact supports a question, write none and
  say so in the return line.
- `lint_questions --lesson <lesson>` (with refutations) must exit 0 before handing over; append the first-run
  failure count to `<module>/lint.tsv` as `<lesson> gap<TAB>n`.
- Decisions: append to the module's `decisions.tsv` with ids `GAP<n>` (check the last `GAP` id in all
  `s2/*/decisions.tsv` files first; a race is harmless, the coordinator renumbers).

## Sources (G2, G4)

- One fetch attempt per item, under `s0/fetcher-brief.md` and amendments 5 and 6 (tool:
  `backend/scripts/tech_sources.py fetch|anchors|apply-licences`; licence rule from `sources/licences.yaml`; a page
  without a licence is stored `storage: local`, `extract_allowed: false`). Log each stored source in
  `s2/sources-added.tsv` and each attempt (stored or not, with the reason) in `gap/fetch-attempts.tsv`:
  `item<TAB>lesson<TAB>url<TAB>result<TAB>source_id or reason`.
- Not sources: forums, Q&A sites, aggregators, anonymous blogs, tutorials, model output.
- Tier A (primary docs, RFCs, papers by their authors, open textbooks per amendment 6) can support F; Tier C only
  supports J (`:::judgement{source="<actual author>" ref="src#anchor"}`, worded "According to …").
- A PDF whose text extracts as interleaved columns may be re-extracted (for example `pdftotext` without
  `-layout`, or per-column cropping) and registered as a new source id with its own anchors; never rewrite the
  anchors of a source that existing lessons already cite.
