# S0 agent brief — backend-in-depth (2026-11-13)

Common rules for every S0 subagent. The course requirements are `docs/backend-in-depth-course-requirements.md`
(sections 3, 4 and 8.4 apply to you); the programme with bullet ids is `content/backend-in-depth/programme.md`.

## Rules

- Nothing from memory. A version, a JEP status, a licence, a chapter list or a page's coverage is written only
  after you read the page that states it in this session. If you cannot reach a page, write that; do not fill in.
- Sources: primary documentation only (requirements 3.1). Never forums, Q&A sites, aggregators, anonymous blogs,
  tutorials or model output.
- Work from the repo root `/home/juanjo/PycharmProjects/curset`. Run the tool from `backend/`:
  `cd backend && uv run python scripts/tech_sources.py <command> --course backend-in-depth …`
- Do not commit. Do not touch other courses. Do not edit `scripts/tech_sources.py`; report a tool bug instead.
- Write your outputs to files. Your final reply is a status of at most five lines.

## Tool

- `fetch --id ID --url URL --tier A|C --product P --version V --title "T" [--kind pdf] [--evidence]` downloads one
  page (plain curl first, headless Chromium if refused or empty), stores it stripped under
  `content/backend-in-depth/sources/docs/` (or `sources/evidence/` with `--evidence`), registers it in
  `sources/sources.yaml` (or `sources/evidence.yaml`) with sha256 and date, and splits it into anchors
  (`sources/anchors/ID.json`). Re-fetching the same id replaces it. Prints one line.
- `list ID` prints each anchor: name, length in characters, heading.
- `show ID#ANCHOR` prints one anchor's text. Read anchors, never whole files; do not `cat` stored pages.

## Ids and granularity

- Source ids are lowercase, stable and version-free: `jep-444`, `jls-17`, `javadoc-hashmap`, `pg-mvcc-intro`,
  `rfc9110`, `kafka-docs-design`, `spring-fw-transaction`. The version goes in `--version`.
- One stored file per documentation page or chapter, for the pinned version (`content/backend-in-depth/sources/
  versions.yaml`). Prefer the versioned URL over `current`/`latest` when the site offers one. Do not download a
  whole manual when the programme needs three chapters of it; do not download single paragraphs either.
- Tier B (books): never downloaded. Register them in `docs/backend-verification/s0/tier-b.yaml` (title, authors,
  edition, publisher, year, the chapters that orient the bullets, the publisher page you read them from).
