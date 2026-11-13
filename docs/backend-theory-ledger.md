# backend-in-depth — theory ledger

Requirements: `docs/backend-in-depth-course-requirements.md` v1.2 (v1.1 + amendments). A new session reads only «Where to resume».

## Where to resume

S0 and S1 done (2026-11-13; S1 parts A, B and C all done, nothing committed). Next: S2 module 06, then 01–05
and 07–12. Requirements are v1.2: read the four amendments at the end (X covers script arithmetic,
`CURSET_SOURCES_LOCAL`, esquema rows cite `source_id#anchor`, `m00-l01` exempt from scope).
Writers follow `docs/backend-verification/s1/contracts.md`: citations as inline code `source_id#anchor`;
`<!-- bullets: … -->` under each `##`; `:::judgement{source= ref=}` for J; snippets in
`content/backend-in-depth/snippets/<lesson>/` with `.run.json` records, shown as ```` ```java snippet=… ````.
Sources only through `backend/scripts/tech_sources.py show ID#ANCHOR`; each stub's «Sources» block lists anchors.
Per lesson (8.2 step 2), from `backend/`: `uv run python -m scripts.tech_course.run_snippets` (pinned JDK 25.0.5,
Kotlin 2.4.21 cached in ~/.cache/curset/toolchains, no network), `build_variants`, `check_extracts`,
`check_citations`, `check_scope`, `check_coverage`, `lesson_quota`. Close each round with
`docs/backend-verification/tools/close_round.sh <scratch>` (S1 close: exit 0, all green).
S1 built: loader `source#anchor` esquema check + `course-requirements` source (m00-l01 esquema restored);
N1 code highlighting, N2 judgement callout, N3 extract gating (`extract:`/`snippet:` on quiz questions);
N4 scheduler (`practice_scheduler: spaced`, `POST /practice/review`); N5 + 13 generators in
`backend/src/tradeschool/psicotecnico/backend/`. Decisions D1–D100 in `s1/decisions.tsv`; reports `s1/part-*.md`.
Part A: write skew restored on Tier A (Berenson 1995, Ports & Grittner 2012); 9.1.b X, 9.1.d J, 11.6.g F/J
restored; 1.4.a, 1.4.c, 12.4.a dropped. DDIA 1st ed. and CLRS 4th ed. registered as Tier B.
Owed by S2 modules: confirm each generator's citation (`uv run python scripts/export_backend_goldens.py
--citations` lists the 13 placeholders; the module whose lesson a generator names fills it).
Owed by S3: preset UI (mixed review button, by module, code reading only, generators only); glyph and colour;
PDF code blocks print in sans (no monospace font embedded); solution panel's correct-answer line is plain text.
Open review items (`s1/review.md` «Fixes»): 7 (`solve()` reuses `correct()`), 8 (raw option text in
AttemptResult/PDF), 9 (`languages[0]`), the isolation generator's "what PostgreSQL 18 does" wording, and
`run_snippets --check` not comparing the `isolation` field. Known limit: esquema list rows whose anchor holds `)`
may mis-parse (tabla rows are safe); editing requirements section 4 changes `course-requirements` hashes.
Subagent cap is now 8 (4 writers, 4 verifiers; CLAUDE.md and requirements 8.4, 10).

## Modules

| Module | Title | Lessons | Bullet classes (S0) | State | Session | Notes |
|---|---|---|---|---|---|---|
| 01 | Pragmatic software design and patterns | 4 | F 1 F+X 4 J 7 drop 2 | pending | — | |
| 02 | Algorithms and data structures | 7 | F+X 8 X 9 J 2 | pending | — | |
| 03 | Modern JVM, concurrency and performance | 4 | F 11 F+X 4 J 1 | pending | — | |
| 04 | Kotlin for Java developers | 5 | F 9 F+X 8 J 1 | pending | — | |
| 05 | Spring Framework and Spring Boot internals | 8 | F 28 | pending | — | |
| 06 | Relational persistence, transactions and SQL optimisation | 4 | F 11 | pending | — | |
| 07 | Networking and API design | 7 | F 24 F+X 1 J 3 | pending | — | |
| 08 | Distributed systems, messaging and resilience | 7 | F 30 J 2 | pending | — | |
| 09 | System design and data scalability | 5 | F 17 X 1 J 4 | pending | — | |
| 10 | Platform, observability, security and AI integration | 6 | F 20 F+X 1 J 4 | pending | — | |
| 11 | Code reading, debugging and testing | 6 | F 7 F+X 7 J 4 | pending | — | |
| 12 | Staff-level technical leadership | 5 | J 17 drop 1 | pending | — | |

## S0 — setup (2026-11-13)

- **Programme lock:** `content/backend-in-depth/programme.md`, section 9 copied by script; 68 subsections, 249
  bullets with ids `<subsection>.<letter>`, 34 marked `[J]` (the (J) entries and all of module 12).
- **Versions:** `sources/versions.yaml`, 53 products (26 of requirements 3.1 + 27 programme extras) and 17 JEPs,
  each quote a literal substring of its stored evidence page (`sources/evidence/`, `evidence.yaml`). Java 25 LTS
  (25.0.5). JEP 505 is the fifth preview in 25 (525 and 533 later); 506, 514, 515 final in 25. An Opus audit
  corrected Spring Framework to 7.0.10 and GraalVM to 25.5.5.0.3 and refetched 44 pages at versioned URLs
  (`docs/backend-verification/s0/version-audit.tsv`; ~133 sources kept unversioned where the site has no versions).
- **Sources:** 623 in `sources/sources.yaml` after S1 part A (597 Tier A, 26 Tier C; S0 ended at 619), 17,834 anchors. 12 Tier B books in
  `docs/backend-verification/s0/tier-b.yaml`; 65 Tier C candidates cited by URL only in `tier-c-candidates.yaml`.
- **Licences:** 108 site rules in `sources/licences.yaml` (53 allow extracts), each from a stored terms page.
  Default used: a copy whose rule does not allow extracts is kept outside git (`storage: local`, 254 sources,
  `~/PycharmProjects/curset-saved-originals/backend-in-depth/local/`), hashes and anchors in the repo. Oracle's
  Java SE docs, Elastic and the Dynamo paper forbid copying in their terms; Spring Boot/Security, Micrometer and
  RabbitMQ allow personal non-commercial use only.
- **Coverage:** `docs/backend-verification/s0/source-coverage.md` — F 158, F+X 33, X 10, J 45, dropped 3
  (1.4.a, 1.4.c, 12.4.a; S1 Part A restored 6.2.a's 'write skew', 9.1.b as X, 9.1.d as J, 11.6.g as F); 1,351
  anchor refs, all resolve
  (`s0/scripts/check_coverage_refs.py`). Default rules logged in `s0/default-rules.tsv`: R1 61, R2 44 (mostly
  unsupported parts of a bullet left out), R3 6 (6.3.b, 3.3.c, 8.6.c, 8.6.e, 10.5.h, 10.6.c).
- **Skeleton:** `course.yaml` (`status: draft`, the platform's unpublished state), `m00-l01` written and
  blind-checked (`s0/verify-m00-and-style.tsv`: 8 fails, all fixed), 68 stubs from `s0/scripts/skeleton.py`.
- **Tooling:** `backend/scripts/tech_sources.py` (+ `fetch_rendered.cjs`): fetch, anchors, show, list,
  apply-licences.
