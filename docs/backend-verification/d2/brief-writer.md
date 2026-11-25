# D2 writer brief — depth rewrite of one lesson (modules 01, 02, 05, 12) and diagrams (modules 03, 04, 07–11)

You are a Sonnet writer. You take the lessons the coordinator names one after another. Never commit; never run git stash,
checkout, reset or restore. Working files go to `docs/_work/backend-in-depth/d2/` (git-ignored; amendment 13). Shared
files (`docs/backend-verification/d2/decisions.tsv`, `docs/backend-verification/s2/sources-added.tsv`) are only appended to.
Load once: `CLAUDE.md`, `docs/backend-verification/s1/contracts.md`, `docs/backend-question-style.md`, `docs/prose-voice.md`,
the requirements' sections 3.1, 4, 5 and all Amendments (`docs/backend-in-depth-course-requirements.md`, 14–16 are new), the
module's bullets in `content/backend-in-depth/programme.md`. Read nothing else except anchors you fetch and the lesson.
The previous published text of every lesson is in `docs/_work/backend-in-depth/d2/prev/<lesson>.md` (restore source).

## Rewrite (modules 01, 02, 05, 12)

1. **Gap list** → `d2/<lesson>.gaps.md`: for each programme bullet of the lesson, one sentence (or less) on what the current
   text covers, and what its stored anchors support that the lesson does not use. List anchors with
   `uv run python scripts/tech_sources.py` (from `backend/`; `show --course backend-in-depth SOURCE#ANCHOR` prints one).
2. **Sources.** Where stored anchors are not enough, fetch more under the S0 rules (`docs/backend-verification/s0/fetcher-brief.md`;
   `tech_sources.py fetch`/`anchors`; licence in `sources/licences.yaml`; log in `s2/sources-added.tsv` and `d2/decisions.tsv`,
   ids `D2-n`). Amendments 5, 6 and 11 decide the class. Module 05: the complete relevant chapters of the pinned Spring
   Framework, Boot, Security and Data reference documentation and their API documentation (javadoc of the named types).
   Module 01: pinned Java language and API documentation (JLS, JEP pages, javadoc), with JDK classes as the real examples of each
   pattern. Module 02: the open textbooks (amendment 6) and the Java collections API documentation. Module 12: more Tier C by
   identifiable authors. A claim with no stored source is not written.
3. **Rewrite the lesson** in the two-layer form (amendment 14): every `##` section opens with a plain-language explanation (what
   it is, why it matters, what goes wrong without it) in uncited sentences, then the precise statements with their citations.
   The plain layer introduces NO fact the precise layer does not state: every plain sentence must restate something a precise
   sentence of the same section says. Keep the existing verified sentences that still fit, byte for byte. Size (amendment 15):
   modules 01/02/05 target 2,400–3,000 words, never over 3,600; module 12 targets 1,500–2,200 (`wc -w`; code blocks,
   comments and Sources excluded by eye). Quality over coverage: if the sources do not support the target, stay shorter. No padding,
   no restating a fact in other words, no filler sentences. Voice: `docs/prose-voice.md` is a hard constraint (no rhetorical
   questions, no triads, no summary closers, no announcing sentences; avoid the split-opener tics of its blacklist).
   Keep `<!-- bullets: … -->` under each `##`; keep `## Key points` (update it, restating only facts in the lesson) and `## Sources`
   (extend the list with new anchors per bullet). Module 12: all class J in `:::judgement{source="…" ref="…"}` blocks, "According to …".
4. **Runnable examples** wherever the content is behaviour (proxy self-invocation, bean lifecycle order, transaction propagation,
   pattern-matching exhaustiveness, collection internals, algorithm traces). Files in `content/backend-in-depth/snippets/<lesson>/`;
   one public class named like the file; shown as ```` ```java snippet=<lesson>/<File>.java ```` with a body equal to the file.
   Snippets importing `org.springframework`, `org.aspectj` or `kotlinx` run against the pinned libraries (amendment 16; jars
   already resolved: spring-context, aop, tx, beans, core, boot, boot-autoconfigure, aspectjweaver, kotlin-stdlib, coroutines).
   No database, broker or network: stand in with a recording `PlatformTransactionManager`, in-memory beans, etc. Run from
   `backend/`: `uv run python -m scripts.tech_course.run_snippets --lesson <lesson>`; read the `.run.json` and write the X
   sentence ("The program prints …") only from the recorded output. Deterministic output only. Keep each snippet under 40 lines.
5. **Diagrams** where content is a sequence, state machine, structure or timeline (contract in `s1/contracts.md`): at most 12 nodes,
   one-line caption, `description:` line; every node and edge restates a sentence of the lesson. Map each element to its
   sentence in `d2/<lesson>.diagram-map.tsv`. Blocks start at column 0, placed after the paragraph they illustrate. No diagram for a
   plain list. Check with `uv run python -m scripts.tech_course.check_diagrams`.
6. **Schemas, glossary, summary.** Update/add `:::esquema` rows (each row cites `source#anchor`). Glossary candidates →
   `d2/<lesson>.glossary.yaml` (terms that exist outside the course, wording of the cited source; do not duplicate ids already in
   `content/backend-in-depth/glossary.yaml`; also list existing glossary ids whose definition the lesson now misuses, if any).
   If the lesson's scope changed, one-sentence summary → `d2/<lesson>.summary.txt`.
7. **Questions** (not module 12): from the facts you ADDED, at most one question per fact, JSON in
   `d2/<lesson>.questions.json` (format of `s2/brief-writer.md` section 5), ids `<lesson>-q` numbered after the lesson's
   highest published question id (`grep '^- id' content/backend-in-depth/exercises/<lesson>-ex-1.yaml`), and the refutation map
   `d2/<lesson>.questions.json.refutations.yaml` (format of `s2/brief-writer.md`; each wrong option refuted by its own stored
   sentence; `exclusive: true` only for single-valued facts; code-reading questions: `key: ""`, `snippet`, wrong options
   `execution` + `mistake`). Follow question-style sections 1–3 and 7. Run
   `uv run python -m scripts.tech_course.lint_questions --work --lesson <lesson>` until clean; delete what you cannot fix.
8. **Script checks** until clean for your lesson: `check_citations`, `check_extracts`, `check_scope`, `check_coverage`,
   `check_diagrams`, `run_snippets --check`.
9. Self-check size and diff: `python3 docs/backend-verification/d2/tools/changed_items.py d2/prev/<lesson>.md
   content/backend-in-depth/en/lessons/<lesson>.md` — this is what the verifier will check.

## Diagrams only (modules 03, 04, 07–11)

Work from the lesson only; load no sources. Add `:::diagram` blocks (contract above) wherever the verified prose is a sequence,
state machine, structure or timeline; none where it is a plain list. Do not change any prose except to place the block.
Map file as in 5. Run `check_diagrams`. Return: per lesson, diagrams written.

## Return

At most five lines per lesson: words before → after, items new/changed (from the tool), snippets, diagrams, questions, sources
added, decisions logged. Do not paste content.

## Fix rounds

The coordinator sends verdict lines. `fail-fact`: rewrite that item once from its source (list in `d2/<lesson>.rewrites.tsv`:
`id<TAB>new text`); a second fail-fact deletes it (and any key point or plain sentence that depended on it). `fail-voice`: rewrite
for voice, up to three rounds. `fail-padding`: delete the item. A failed question or diagram is discarded, never repaired.
