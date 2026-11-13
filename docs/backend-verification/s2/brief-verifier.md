# S2 verifier brief — blind check of one lesson of backend-in-depth

You did not write this lesson. Load once per run: `docs/backend-verification/s1/contracts.md`,
`docs/backend-question-style.md` (sections 1, 2, 3 and 6 are your checklist), `docs/prose-voice.md` (its
"never does" list). Do not read writer notes (`decisions.tsv`, `*.rewrites.tsv`, return lines) before your verdicts.

## Per lesson

Load the lesson `content/backend-in-depth/en/lessons/<lesson>.md`, its candidates
`docs/backend-verification/s2/<module>/<lesson>.questions.json`, its glossary candidates
`<lesson>.glossary.yaml`, its snippets and `.run.json` records, and **only the anchors they cite**, from
`backend/`: `uv run python scripts/tech_sources.py show SOURCE#ANCHOR`. Never open whole source files.

Write `docs/backend-verification/s2/<module>/<lesson>.verdicts.tsv`, one line per item, tab-separated:

    <item id>	pass
    <item id>	fail	<reason, at most fifteen words>

Item ids:

- Sentences of prose: `S<section>.<n>` — section = position of the `##` section (1-based, `## Key points`
  included, `## Sources` excluded), n = sentence position in it — followed by a tab and the sentence's first
  six words in quotes, so the writer can find it: `S2.3	"PostgreSQL never shows uncommitted rows"	pass`.
  Every sentence gets a line, including sentences inside judgement callouts.
- Esquema rows: `R<k>.<n>` (k = esquema position in the lesson, n = row) with the first cell quoted.
- Glossary entries: their `g-…` id. Questions: their `<lesson>-qNN` id.

Pass/fail rules:

- F sentence or row: passes only when the cited anchor (pinned version) states the fact; a claim beyond the
  anchor, a wrong version, or a missing/irrelevant citation fails. A sentence that breaks the voice page's
  "never does" list or coins vocabulary fails.
- J (inside `:::judgement`): check only that the attribution is faithful to the named source/ref.
- Key points: pass only if each restates an F/X fact already in the lesson.
- Snippet blocks and code-reading claims: pass only if they match the `.run.json` stdout/exit code.
- Glossary: passes when the term is used in the lesson, exists outside the course, and the definition follows
  the cited anchor.
- Question: passes only when the key follows from the cited anchor or execution record, every distractor is
  contradicted by a cited fact (not by silence), the version is named where it matters, and every rule of the
  style guide holds. Do not repair anything.

End the file with `# checked N, passed P, failed F`. Return at most five lines: lesson id and the counts
(sentences, rows, glossary, questions: passed/failed).

## Re-verification rounds

When asked to re-verify rewritten sentences, read `<lesson>.rewrites.tsv` and the cited anchors, and append to the
verdict file lines `<id>	recheck	pass` or `<id>	recheck	fail	<reason>`.
