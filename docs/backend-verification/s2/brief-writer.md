# S2 writer brief — one lesson of backend-in-depth

You write the lessons the coordinator names, one after another, reusing your loaded context.
Load once per run: `CLAUDE.md`, `docs/backend-verification/s1/contracts.md` (follow it exactly),
`docs/backend-question-style.md` (all of it; section 7 holds the rules that failed most in module 06),
`docs/prose-voice.md`, requirements sections 3.1, 4 and 5 and the Amendments at the end
(`docs/backend-in-depth-course-requirements.md`) and the module's bullets in `content/backend-in-depth/programme.md`.
Read nothing else beyond the anchors below. Never commit; never run git stash, checkout or reset.

## Inputs per lesson

- The stub `content/backend-in-depth/en/lessons/<lesson>.md`: its «Sources» block (refreshed from the coverage
  report) lists, per bullet, the class (F, F+X, X, J, dropped) and the anchors. Load **only** those anchors, one
  at a time, from `backend/`: `uv run python scripts/tech_sources.py show SOURCE#ANCHOR` (local-only copies
  resolve through `CURSET_SOURCES_LOCAL`). Never open a whole source file.
- If a bullet needs an anchor that is missing, or lists only a `candidate:` URL, add the source with the S0 rules
  (`docs/backend-verification/s0/fetcher-brief.md`; `tech_sources.py fetch`/`anchors`, licence in
  `sources/licences.yaml`; Tier C for articles by identifiable authors and books with an open online edition,
  e.g. Erickson's *Algorithms*, CC BY 4.0; a page with no licence is still stored, `storage: local`,
  `extract_allowed: false` — a missing licence is never a reason to omit) and log it in
  `docs/backend-verification/s2/sources-added.tsv` and in `docs/backend-verification/s2/<module>/decisions.tsv`
  (`id<TAB>lesson<TAB>decision<TAB>rule`; ids `<module letter><n>`, e.g. `D1` for m01 — see the file's last id).
- Source rule (amendment 5): a bullet whose only stored source is Tier B or Tier C is written as class J, in a
  judgement block with attribution. It is omitted only when no stored source supports it (log the omission).
  A Tier B book (`docs/backend-verification/s0/tier-b.yaml`) is not stored as text: attribute to it only what its
  registered chapter titles and note state ("Sedgewick and Wayne treat sorting in chapter 2 of *Algorithms*"),
  never content you recall. Prefer a stored Tier C page when one covers the same point.

## What you write

1. **The lesson**, replacing the stub file (keep the `# Title`). Sections `## …`, each followed on the next line
   by `<!-- bullets: 6.2.a … -->` with the bullets it covers (only this subsection's bullets; together the
   sections cover every bullet of the stub not marked dropped). English only. Voice: `docs/prose-voice.md`
   (its "never does" list is a hard constraint; no coined vocabulary).
   - Each F sentence ends with a parenthetical holding only inline-code citations: ``(`pg-x#ANCHOR`)``. One
     fact per sentence; the fact must be stated by the cited anchor of the pinned version, not by memory.
   - X sentences say what a shown snippet prints, returns or throws. They follow the snippet block and must
     match its `.run.json` record. Arithmetic computed by a script (amendment 1) is also a snippet that prints it.
   - J content (trade-offs, advice, technique descriptions from Tier B/C) only inside
     `:::judgement{source="…" ref="…"}` … `:::`, worded "According to …", attributed faithfully.
   - Schemas: `:::esquema{kind=tabla title="…"}` (or decision tree / steps, per the m00-l01 example); every row
     is an F fact with a `source_id#anchor` citation column.
   - Code: fenced with a language. SQL, YAML and config are illustrative and need a citation for any claim
     about their effect. **All Java/Kotlin code is a runnable snippet file**:
     `content/backend-in-depth/snippets/<lesson>/<File>.java|.kt`, shown as ```` ```java snippet=<lesson>/<File>.java ````
     with the block body equal to the file; then run, from `backend/`,
     `uv run python -m scripts.tech_course.run_snippets --lesson <lesson>`. Anything needing a database or
     broker is not X: cite documentation or leave it out.
   - End with `## Key points` (bullets restating only F/X facts already in the lesson, no new facts, no
     metadata line) and keep the stub's `## Sources` section as it is.
2. **Glossary candidates** (do not edit `glossary.yaml`): `docs/backend-verification/s2/<module>/<lesson>.glossary.yaml`,
   a YAML list of `{id: g-<slug>, term: {en: …}, definition: {en: …}, origin: <lesson>, citation: "src#anchor"}`.
   Only terms that exist outside the course, defined in the wording of the cited source, and used verbatim
   in your lesson prose. One or two sentences each. Check `content/backend-in-depth/glossary.yaml` for ids
   already present and do not duplicate them.
3. **Summary** for the course manifest: one sentence in `docs/backend-verification/s2/<module>/<lesson>.summary.txt`.
4. **Question candidates**: run `uv run python -m scripts.tech_course.lesson_quota` from `backend/` after the
   lesson is written; write the lesson's quota of candidates to
   `docs/backend-verification/s2/<module>/<lesson>.questions.json`: a list of
   `{"id": "<lesson>-qNN", "stem", "key", "distractors": [3], "explanation", "citation", "extract", "snippet"}`.
   - Keys only on F or X facts, never on J. Follow `docs/backend-question-style.md` in full.
   - Self-check each question before linting, against the anchors you loaded. For each distractor, find the
     anchor sentence that contradicts it. If there is none, if that sentence is already used for another
     distractor, or if a reader of the source could defend the distractor, replace it. Check the key is one
     item of the anchor, not a merge. A version named in a stem is the one in
     `content/backend-in-depth/sources/versions.yaml`. In module 01, half the questions failed on these points
     alone.
   - `citation`: first citation supports the key. `extract`: a literal substring of the first cited anchor,
     only when that source's licence allows extracts (`show` prints it); otherwise `null`.
   - Code-reading and computed questions rest on a snippet of this lesson that ran: put the path in `snippet`
     and leave `key` empty (`""`); then run `uv run python -m scripts.tech_course.fill_keys --lesson <lesson>`.
5. **Lint and script checks** from `backend/`: `uv run python -m scripts.tech_course.lint_questions --lesson <lesson>`.
   Append one line `<lesson><TAB><failures on the first run>` to `docs/backend-verification/s2/<module>/lint.tsv`,
   then fix every failure (and keep the key-longest share at or under 40 %) until it exits 0.
   Then `check_citations`, `check_extracts`, `check_scope`, `run_snippets --check` (each
   `uv run python -m scripts.tech_course.<name>`); fix what is yours until they are clean for your lesson. Finally
   build the exercise file: `python3 docs/backend-verification/s2/tools/build_quiz.py
   docs/backend-verification/s2/<module>/<lesson>.questions.json content/backend-in-depth/exercises/<lesson>-ex-1.yaml`.

## Return

At most five lines: per lesson id, F sentences / esquema rows / snippets / questions written, quota, lint
failures fixed, script-check status, any decision logged. Do not paste content.

## Fix rounds

When the coordinator sends failed sentence ids from a verdict file: rewrite each failed sentence **once**,
from its source, and list the rewritten ids in `docs/backend-verification/s2/<module>/<lesson>.rewrites.tsv`
(`id<TAB>new sentence`). On a second failure, delete the sentence (and any key point restating it) and keep
the lesson grammatical. Never repair a failed question; the coordinator drops it. A replacement batch uses ids
after the lesson's last id, is linted to exit 0, and goes to `<lesson>.questions.json` appended.
