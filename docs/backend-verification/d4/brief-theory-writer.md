# Round D4, Part B — rule writer brief (Sonnet): add a missing rule, then build its family

You are a Sonnet writer. You take the rules the coordinator names one after another, in one run. Never commit; never run
git stash, checkout, reset or restore. Work folder `docs/_work/backend-in-depth/d4/<writer>/` (git-ignored, amendment 13):
`decisions.tsv` (id `D4-B-<writer>-n`, lesson, decision, rule), `progress.md` after every rule, `cost.tsv`.
Load once: `CLAUDE.md`, `docs/backend-verification/s1/contracts.md`, `docs/backend-question-style.md`, `docs/prose-voice.md`,
requirements `docs/backend-in-depth-course-requirements.md` sections 3.1, 4, 5 and all Amendments, the lesson's bullets in
`content/backend-in-depth/programme.md`. Then, per rule, the target lesson. The pre-round copy of each lesson is
`docs/_work/backend-in-depth/d4/prev/<lesson>.md` (do not edit it).

## Step 1 — the rule's source

1. Look for the rule in the stored anchors: from `backend/`, `uv run python scripts/tech_sources.py` (`show --course
   backend-in-depth SOURCE#ANCHOR` prints one; list/search subcommands per its `--help`). Prefer the anchor of the exact
   method, section or field that states the rule.
2. If no stored anchor states it, fetch a source under the S0 rules (`docs/backend-verification/s0/fetcher-brief.md`,
   `tech_sources.py fetch`/`anchors`, licence from `sources/licences.yaml`), Tier A only for a tested rule (amendments 6, 11).
   Log the source in `docs/backend-verification/s2/sources-added.tsv` and your `decisions.tsv`.
3. No source states it: write nothing for that rule; log `skipped: no source states <rule>` and go on.

## Step 2 — the lesson text (amendment 14, two layers)

- Put the rule in the section whose `<!-- bullets: … -->` covers it. If no section of the lesson covers a programme bullet
  the rule belongs to, log it and skip (scope audit).
- At most about 150 words per rule: one or two plain-language sentences (what it is, why it matters, what goes wrong
  without it), uncited, that state NO fact the precise sentences do not; then the precise sentences, each ending with its
  citation parenthetical. Same sense, numbers and qualifiers as the anchor; name the version when the rule differs between
  versions. A runnable snippet (contracts, "Code") only where the rule is behaviour the JDK alone shows; then the X sentence
  is copied from the `.run.json` stdout (`uv run python -m scripts.tech_course.run_snippets --lesson <lesson>`).
- Keep every existing sentence byte for byte unless one now contradicts the rule (log it). Add one `## Key points` bullet
  only if the rule is central; add the new anchor to `## Sources` under its bullet.
- Size (amendment 15): modules 01, 02, 05 never over 3,600 words (`uv run python ../docs/_work/backend-in-depth/d4/tools/word_counts.py <lesson>`
  from `backend/`). Other modules: no cap, but no padding.
- Voice: `docs/prose-voice.md` "never does" list and blacklist are hard constraints. Nothing coined.
- No new static questions, no diagrams, no glossary entries this round.
- Script checks until clean, from `backend/`: `check_citations`, `check_extracts`, `check_scope`, `check_coverage`,
  `run_snippets --check` (each `uv run python -m scripts.tech_course.<name>`).
- Items for the blind check: `python3 ../docs/_work/backend-in-depth/d4/tools/changed_items.py ../docs/_work/backend-in-depth/d4/prev/<lesson>.md
  ../content/backend-in-depth/en/lessons/<lesson>.md ../docs/_work/backend-in-depth/d4/<lesson>.items.tsv`.
  When two of your rules share a lesson, write both before producing the items file.
- Stop after the items file and report: lesson, rule, anchor, words before → after, items count. Wait for the verdicts.

## Step 3 — fixes

Verdict lines arrive by message. `fail-fact`: rewrite once from the source (append `id<TAB>new text` to
`d4/<lesson>.rewrites.tsv`); a second fail-fact deletes the item and anything that depends on it. `fail-voice`: rewrite, up
to three rounds. `fail-padding`: delete. A rule whose precise sentence is deleted has no lesson support: its family is not built.

## Step 4 — the family (only after the coordinator says the rule's text passed)

Build it to the D3 standards: generators per `docs/backend-verification/d3/brief-generators.md`, variant families per
`docs/backend-verification/d3/brief-variants.md` (including its "Added during the round" rules 12–13: mistake `why:` on every
mistake, `cases:` with a per-case `why` and a method-level `citation`). Deltas for D4: work folder and ids as above (`D4-B-…`);
the citation is the anchor of the precise sentence you added; your test file is `backend/tests/test_backend_generators_d4<writer>.py`
or `backend/tests/test_variant_families_d4<writer>.py`; registration lines in `d4/<writer>/registration.md`. Before handing over,
check the three commonest D3 failures yourself: a generic explanation sentence that is false for some variants, a class-level
citation where the fact sits on a method anchor, mistake names that do not match their mutation or identifiers outside inline code.
Report under 25 lines: per family, lesson, anchor, kept count or level coverage, test result.
