# AEAT round R2d, step 3 — blind verifier spec

2026-11-14. Course `aeat-agentes-hacienda`. You are a blind verifier (Opus). You did not write the lesson and you have
not seen any writer's notes or earlier report for it: do not open `r2d/<lesson>/writer.md` or any earlier
`verify*.md`. Never edit a lesson.

Read once per run: `docs/age-verification/aeat/r2-tax/spec.md` § «Verifier (blind)» (checks 1–6 and the report table
format apply unchanged); `docs/prose-voice.md` (never-does list); `docs/aeat-agentes-course-requirements.md` R4.4,
R4.7–R4.8; `normativa.yaml` header (unconvalidated RDLs) and the entries of the norms the sentences cite.

Input per lesson: `docs/age-verification/aeat/r2d/<lesson>/pending.md` (every sentence with neither an inherited origin
nor a PASS: the new and changed ones) and the lesson for context. Batches of 60 rows, in order; write the report after
each batch.

On top of R2's checks:

1. **Enumerations.** A list item or esquema row that belongs to a legal enumeration: open the article and compare the
   whole list, count and wording. A list presented as the article's list that lacks items, adds items, or reorders
   ordinals FAILs on the row that introduces it (the lead-in), with the missing items named. The words «entre otros»,
   «entre otras», «etc.» standing for items of a legal list FAIL.
2. **«No confundir»** lines: each rule verbatim (or a faithful cut that keeps every condition) with its own citation; a
   line that interprets, compares or adds a mnemonic FAILs.
3. **Worked examples**: recompute every step (amounts, dates, weekdays with `python3`).
4. **Split paragraphs**: a list item that came from a split paragraph must still read as a sentence with its citation.

Output: `docs/age-verification/aeat/r2d/<lesson>/verify.md`, or `verify-recheck-N.md` for a re-check (N given by the
coordinator), in R2's exact table shape, ending «PASS n · FAIL m». A FAIL gives the full replacement sentence in the
article's words, or «drop».

## Added 2026-11-14 (after the first passes)

- A FAIL's replacement is the full corrected sentence (or «drop») and nothing else: no instructions («Mantener…»,
  «Same sentence, moved…»), no «[Normativa: …]» notes. Structural fixes (blank line, move, nesting) and Normativa
  additions go in the note column. `r2dprov.py apply` now refuses replacements that look like instructions.
- Also FAIL: paragraphs that render inside the wrong list item, citations after the full stop as fragments, wrong
  apartado at paragraph level, PDF line-break artefacts («declaración- liquidación», stray numerals, «▼», «—————»,
  bare «(Derogado)»), and «Normativa» lines missing an article the prose cites or a norm it names («nombrado en …»).
- Use your own scratch subfolder for extracted texts.
- «Normativa» lines (coordinator ruling, 2026-11-14, as R2's spec): a line lists exactly the articles the lesson cites
  in its citations (parentheticals, esquema «Cita» cells, «art. N» citations the parser reads) and names every norm
  the prose names. An article of the same law that the lesson only mentions inside copied law text («conforme al
  artículo 14 de esta Ley») does not have to be listed; a different norm named that way does (own «nombrado en …»
  line, or the final «… no figuran en `normativa.yaml`» line).
- Numbered items written «- 10\. …» (escaped dot) are the course's form for a norm's numeral inside a bullet; they
  render as text, not as a nested ordered list.
- Reduced lessons (depth correction, `spec-reduce.md`): FAIL, with the full corrected sentence in the article's words,
  any fragment, any rule sentence that lost a condition, exception, plazo or organ the article attaches to it, any
  esquema row that misstates its item, any enumeration esquema missing an item. A shortened sentence or row that keeps
  the rule and its conditions PASSes although the article says more.
