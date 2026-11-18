# AEAT round R2d, step 2 — writer spec (restore and write)

2026-11-14. Course `aeat-agentes-hacienda`. Requirements v1.2 (R4.7–R4.9, R3.5, R4.4). You are a writer (Sonnet). You
write the lesson `content/aeat-agentes-hacienda/es/lessons/<lesson>.md` and your notes
`docs/age-verification/aeat/r2d/<lesson>/writer.md`. Touch no other file (never `normativa.yaml`, `glossary.yaml`,
`course.yaml`, a norm, another course, the platform or the bank).

## Read once per run

This file; `docs/age-verification/aeat/r2-tax/spec.md` § «Writer» → «Rules for every sentence» and «Lesson shape» items
3–6 (they still apply, with the changes below); `docs/prose-voice.md`; `CLAUDE.md` (writing rule);
`docs/aeat-agentes-course-requirements.md` §4. Per tema: its map `docs/age-verification/aeat/r2d/<lesson>-map.md` (the
work list is your task list), the lesson, its pack `docs/age-verification/aeat/r2/questions/<lesson>.md`, the
`normativa.yaml` entries of its norms and the header (unconvalidated RDLs), and
`docs/age-verification/aeat/r1/rdl-29-2026-revert-list.md` for III.1, III.4, III.6, III.15, III.16, III.18.
The coordinator may add a «Coordinator notes» section at the end of the map: it wins over the work list.

Norm texts: `pdftotext -layout content/aeat-agentes-hacienda/sources/normativa/<file> -`; `.html` → strip tags with
`python3 -I -c` and `html.parser`. Only the snapshot, never memory. The external review and any academy material are
never a source and are never quoted or paraphrased.

## What changed from R2 (R4.7)

- **Presence is decided by the programme, depth by exam weight.** Every article the map places inside a range and marks
  «not treated» or «part» is treated, at least: the rule, its conditions and exceptions, with citation. Weight: full
  tema → whole articles in the norm's order; standard → every rule, plazo, amount, organ, list; focused → one or two
  sentences per article. In doubt, include it briefly with its citation.
- **Enumerations whole.** A legal list (exemptions, infractions with sanción and graduación, motives, requisites,
  organs, documents, deductions with percentages and limits) is given item by item, in the norm's words, with its
  letters/ordinals: as a list in prose or as an esquema (`:::esquema{kind=tabla …}` with a «Cita» column). No «entre
  otros», «entre otras» or «etc.» standing for items of a legal list; where the norm itself says «entre otros», keep it
  inside quotation marks or with its citation so it reads as the norm's words.
- **Restore R2b removals** the map puts inside a range: rewrite from the snapshot (the old text is in git, `git show
  HEAD~0:<path>` of an earlier commit if useful, but every sentence is re-read against the article: it will be verified
  again). Remove the «Fuera del enunciado literal…» note of any section the map now places inside a range.
- **Keep verified content.** Do not delete or reword a sentence the work list does not name. In doubt between keeping
  and cutting: keep.
- **«No confundir»** (R4.8), only where the work list names two neighbouring rules; at most three per lesson:

  ```
  :::note{type=warning}
  **No confundir.**

  - <rule A in the article's words> (art. … LGT).
  - <rule B in the article's words> (art. … RGR).
  :::
  ```
  No interpretation, no mnemonic, no sentence of your own beyond «**No confundir.**».
- **Readability without rewording.** A paragraph over 120 words that strings several rules becomes a list: each item
  keeps its words and its citation (a lead-in sentence may be cut at its colon). An esquema that only repeats a single
  paragraph is removed (an esquema must gather at least two paragraphs or articles). Ids `(`m03-lNN`)` / `` `m03-lNN` ``
  in running prose are removed, keeping the reference («en el tema III.11»). Markdown numbered lists numbered
  consecutively (1., 2., 3. …).
- **Cross-references** («en el tema III.11») only where the target lesson states the fact (the map checked them; a fix
  in another tema's lesson is listed in your notes for that tema's writer, not made by you).
- **Annual figures and decree-laws**: year and norm as `cifras_anuales`; a precept changed by an unconvalidated RDL
  carries «(redacción del Real Decreto-ley N/2026, convalidación pendiente)». A figure whose source is not in the
  snapshots is left out and listed in your notes.
- **Worked examples** only where the norm's own rule is applied step by step, as R2 (dates checked with `python3`).
- **«Lo que más cae»** stays ten lines from the pack (change only if a line's anchor moved). **«Normativa»**: re-derive
  the articles cited after your changes, same format as R2.

## Writer's notes (`r2d/<lesson>/writer.md`)

1. Work list: item → done (section, lines) / not done (reason).
2. Words before / after (`wc -w`).
3. Articles treated now that were «not treated» / «part» in the map (list).
4. Enumerations completed (article, items before → after).
5. «No confundir» blocks (lines, the two articles).
6. Sentences deleted or reworded that the work list did not name: none, or each with its reason.
7. Facts added that no pack question asks (one line each, with article) — for the bank's next round.
8. Glossary proposals (defined legal terms the added text teaches; never-coins; YAML as R2's spec).
9. Course summary for `course.yaml` if the lesson's scope changed: at most three sentences.
10. Sources missing, figures left out, cross-reference fixes owed by other temas, unresolved citations
    (`cd backend && uv run python ../docs/age-verification/aeat/r2-tax/tools/cites.py <lesson>` must list none you
    introduced).

Write the lesson tema by tema and update your notes after each work item, so a cut loses at most one item.

## Platform constraint (added 2026-11-14)

Every citation in an esquema row must also be cited, with the same unit, in the lesson's prose; otherwise the course
does not validate («citation cross-references that do not hold»). After each tema run
`cd backend && uv run python scripts/index_sources.py --course aeat-agentes-hacienda` (it validates the course at the
end) besides `cites.py`.
