# S0 fetcher brief — sources and coverage drafts (backend-in-depth)

Read `docs/backend-verification/s0/agent-brief.md` first; it applies in full. Pinned versions:
`content/backend-in-depth/sources/versions.yaml` (read it once). Programme: `content/backend-in-depth/programme.md`.
Already stored sources: `content/backend-in-depth/sources/sources.yaml` (do not re-fetch an id that exists unless
you need a different page; reuse it in your rows).

## Per module you are given

1. For every bullet of the module, find the Tier A pages (requirements 3.1) that state what the bullet teaches, for
   the pinned version. Fetch each with `fetch --tier A`. One file per page or chapter; Javadoc one page per class;
   RFCs one file per RFC; papers as the author's or publisher's free PDF (`--kind pdf`).
2. With `list ID`, pick the anchors that carry each bullet's content. Spot-check with `show` only when the heading
   does not make it clear. Never read whole pages.
3. Where a bullet has no Tier A page, look for Tier C (requirements 3.1: company engineering handbooks and career
   ladders, books with an open online edition, articles by identifiable authors on their own or their employer's
   site). Fetch Tier C with `--tier C` only when the site is in `content/backend-in-depth/sources/licences.yaml`
   with `extract_allowed: true`; otherwise list it in `docs/backend-verification/s0/tier-c-candidates.yaml`
   (`url`, `title`, `author`, `site`, `bullets`) without fetching. Register books (Tier B) in
   `docs/backend-verification/s0/tier-b.yaml` (see agent brief), one key per book, e.g. `ddia-2e`.
4. Write `docs/backend-verification/s0/coverage/mNN.tsv` (tab-separated, header row):
   `bullet	proposed_class	tier_a	tier_bc	mismatch	note`
   - `bullet`: the id from programme.md (`6.2.b`), every bullet of the module, in order.
   - `proposed_class`: `F` (Tier A anchors state it), `X` (the claims are what JDK-only Java or Kotlin code
     prints, returns or throws; add Tier A anchors when Javadoc or the JLS states the behaviour), `J` (no Tier A;
     Tier B or C only, or the programme marks it J), `drop` (no acceptable source found).
   - `tier_a`: `source#anchor` refs separated by `; ` (as many as the bullet needs, typically 1–8).
   - `tier_bc`: Tier B keys and Tier C source ids or candidate URLs, separated by `; `.
   - `mismatch`: empty, or ≤25 words where the programme's wording disagrees with the pinned documentation
     (a renamed API, a removed feature, a changed default, a JEP status different from the wording), with the
     anchor that shows it. Do not resolve it; a separate Opus pass decides.
   - `note`: ≤15 words, optional.
5. Write the TSV after each module (a cut loses at most one module). Then go to the next module.

## Limits

- Keep sources to what the bullets need. A typical module needs 15–40 pages.
- A site that refuses both plain fetch and Playwright: record the URL in the `note` column and move on; do not
  try other headers or workarounds.
- Final reply: at most five lines (modules done, sources fetched, drops, mismatches flagged, blockers).
