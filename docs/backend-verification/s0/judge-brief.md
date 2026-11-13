# S0 coverage judge brief (Opus) — backend-in-depth

Read `docs/backend-verification/s0/agent-brief.md` first; it applies in full. Then requirements
`docs/backend-in-depth-course-requirements.md` sections 3.3 and 4 (lines 64–82). You did not draft the coverage.

## Input

`docs/backend-verification/s0/coverage/mNN.tsv` (fetcher drafts: `bullet proposed_class tier_a tier_bc mismatch
note`), the programme `content/backend-in-depth/programme.md`, and the anchors themselves through
`tech_sources.py show ID#ANCHOR`. Load only the anchors a row cites; never whole sources.

## Per bullet

1. Read the bullet text and each cited Tier A anchor. Keep an anchor only if it states part of what the bullet
   teaches for the pinned version. Drop anchors that do not; you may add an anchor of an already stored source
   (`list ID`) if the fetcher missed the obvious one. Do not fetch.
2. Decide the class:
   - `F`: kept Tier A anchors support the bullet's teachable facts.
   - `X`: the bullet's claims are what JDK-only Java/Kotlin code prints, returns or throws (anchors optional).
   - `F+X` when both apply.
   - `J`: the programme marks it J, or no Tier A support but an acceptable Tier B or C source (default rule R1).
   - `drop`: no acceptable source at all (default rule R2).
   - A bullet partly supported: class by the supported part; list the unsupported parts in `note`
     ("unsupported: …"), each later taught as J if a Tier B/C source exists, otherwise left out.
3. Mismatch (default rule R3): if the programme's wording disagrees with the pinned documentation, the
   documentation wins. Write in `pinned` (≤30 words) the pinned behaviour the lesson must state, with the anchor.
   Also check yourself for the obvious ones even if the fetcher left `mismatch` empty (a JEP not final in the
   pinned JDK, a renamed or removed API, a changed default).
4. Tier C sources must be acceptable under requirements 3.1 (identifiable author or company, own site); reject
   aggregators, anonymous blogs, tutorials.

## Output

Per module, `docs/backend-verification/s0/coverage/mNN.final.tsv` with header
`bullet	class	tier_a	tier_bc	rule	pinned	note` (`rule`: empty or `R1`/`R2`/`R3`, several separated by `,`).
Append one row per rule use to `docs/backend-verification/s0/default-rules.tsv`
(`bullet	rule	reason`, reason ≤20 words; create with header if absent).

Before the modules: run `tech_sources.py apply-licences`; for every host it reports without a rule, read that
site's terms page, store it with `fetch --evidence --id lic-<site> …`, and append a rule to
`content/backend-in-depth/sources/licences.yaml` in the file's existing format (same criteria as the existing
rules: unclear means `extract_allowed: false`); then run `apply-licences` again. Hosts that only appear in
`evidence.yaml` (version pages, licence pages) need no rule.

Final reply ≤5 lines: per module counts F / X / F+X / J / drop, R3 uses.
