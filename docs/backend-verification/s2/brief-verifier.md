# S2 verifier brief — blind check of one lesson of backend-in-depth

You did not write this lesson. Load once per run: `docs/backend-verification/s1/contracts.md`,
`docs/backend-question-style.md` (sections 1, 2, 3, 6 and 7 are your checklist), `docs/prose-voice.md` (its
"never does" list). Helper scripts go only in your own folder `<scratchpad>/<your lesson ids>/`; the scratchpad is shared.
Do not read writer notes (`decisions.tsv`, `*.rewrites.tsv`, return lines) before your verdicts.

## Per lesson

Load the lesson `content/backend-in-depth/en/lessons/<lesson>.md`, its fact list `<lesson>.facts.tsv`, its
candidates `docs/backend-verification/s2/<module>/<lesson>.questions.json` with their refutation map
`<lesson>.refutations.yaml`, its glossary candidates
`<lesson>.glossary.yaml`, its snippets and `.run.json` records, and **only the anchors they cite**, from
`backend/`: `uv run python scripts/tech_sources.py show --course backend-in-depth SOURCE#ANCHOR`. Never open whole source files.

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
- J (inside `:::judgement`): check only that the attribution is faithful to the named source/ref. A Tier B book
  (`docs/backend-verification/s0/tier-b.yaml`) is not stored: its attribution passes only when it claims no more
  than the registered title, authors, chapter titles and note.
- X sentence (after a snippet block): passes only when it matches the snippet code and its `.run.json` record.
- Code-reading question: the key must equal the recorded stdout (or error) of its `snippet`.
- Key points: pass only if each restates an F/X fact already in the lesson.
- Snippet blocks and code-reading claims: pass only if they match the `.run.json` stdout/exit code.
- Glossary: passes when the term is used in the lesson, exists outside the course, and the definition follows
  the cited anchor.
- Question: passes only when the key is the only defensible answer and follows from the map's key sentence (or
  execution record), each refutation sentence of the map really rules out its wrong option (not by silence, not
  merely "less complete"), entries marked `exclusive: true` name values that are mutually exclusive with the
  key's, the version is named only where it matters and by major (amendment 9), and every rule of the style
  guide holds. A script already checked that each sentence is a literal substring of its anchor. Do not repair
  anything.
- J content: check only the attribution (the named author wrote what is attributed), not the truth.

End the file with `# checked N, passed P, failed F`. Return at most five lines: lesson id and the counts
(sentences, rows, glossary, questions: passed/failed).

## Re-verification rounds

When asked to re-verify rewritten sentences, read `<lesson>.rewrites.tsv` and the cited anchors, and append to the
verdict file lines `<id>	recheck	pass` or `<id>	recheck	fail	<reason>`.

## Coordinator rulings

- Versions: a stem naming the version pinned in `content/backend-in-depth/sources/versions.yaml` is correct even
  when the stored page states an earlier patch release that the S0 version audit kept for that pin
  (`docs/backend-verification/s0/version-audit.tsv`, `kept-states-…`). Check the pin there before failing a version.
- Code-reading options may show the recorded output in a fenced or inline code block; the text inside must
  equal the `.run.json` stdout (or the recorded error).
- Exclusive groups (S2+S3 run, ruling C001): wrong options whose map entries are all `exclusive: true` and share one
  sentence may be ruled out together by one explanation sentence that names each of them. That is not a
  "shared sentence" failure. Check instead that their values exclude each other and the key (one default, one
  version, one count). Options that are not marked exclusive still need one explanation sentence each.
