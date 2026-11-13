# backend-in-depth — theory ledger

Requirements: `docs/backend-in-depth-course-requirements.md` v1.1. A new session reads only «Where to resume».

## Where to resume

S0 done (2026-11-13). Next: S1 (platform deltas N1–N5, the 13 generators, the build scripts of 8.3), then S2
module 06, then 01–05 and 07–12. Start from this table; sources are read only through
`backend/scripts/tech_sources.py show ID#ANCHOR`; each lesson stub's «Sources» block lists its bullets' anchors.
Open for S1: the esquema citation check (`citations/course.py`) demands a norm and article on every esquema row
of every course; this course cites `source#anchor`, so S1 must teach it that grammar before any esquema is written.
The scope audit must exempt `m00-l01` (it covers no programme bullet).

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
| 09 | System design and data scalability | 5 | F 17 J 3 drop 2 | pending | — | |
| 10 | Platform, observability, security and AI integration | 6 | F 20 F+X 1 J 4 | pending | — | |
| 11 | Code reading, debugging and testing | 6 | F 6 F+X 7 J 4 drop 1 | pending | — | |
| 12 | Staff-level technical leadership | 5 | J 17 drop 1 | pending | — | |

## S0 — setup (2026-11-13)

- **Programme lock:** `content/backend-in-depth/programme.md`, section 9 copied by script; 68 subsections, 249
  bullets with ids `<subsection>.<letter>`, 34 marked `[J]` (the (J) entries and all of module 12).
- **Versions:** `sources/versions.yaml`, 53 products (26 of requirements 3.1 + 27 programme extras) and 17 JEPs,
  each quote a literal substring of its stored evidence page (`sources/evidence/`, `evidence.yaml`). Java 25 LTS
  (25.0.5). JEP 505 is the fifth preview in 25 (525 and 533 later); 506, 514, 515 final in 25. An Opus audit
  corrected Spring Framework to 7.0.10 and GraalVM to 25.5.5.0.3 and refetched 44 pages at versioned URLs
  (`docs/backend-verification/s0/version-audit.tsv`; ~133 sources kept unversioned where the site has no versions).
- **Sources:** 619 in `sources/sources.yaml` (595 Tier A, 24 Tier C), 17,834 anchors. 12 Tier B books in
  `docs/backend-verification/s0/tier-b.yaml`; 65 Tier C candidates cited by URL only in `tier-c-candidates.yaml`.
- **Licences:** 108 site rules in `sources/licences.yaml` (53 allow extracts), each from a stored terms page.
  Default used: a copy whose rule does not allow extracts is kept outside git (`storage: local`, 254 sources,
  `~/PycharmProjects/curset-saved-originals/backend-in-depth/local/`), hashes and anchors in the repo. Oracle's
  Java SE docs, Elastic and the Dynamo paper forbid copying in their terms; Spring Boot/Security, Micrometer and
  RabbitMQ allow personal non-commercial use only.
- **Coverage:** `docs/backend-verification/s0/source-coverage.md` — F 157, F+X 33, X 9, J 44, dropped 6
  (1.4.a, 1.4.c, 9.1.b, 9.1.d, 11.6.g, 12.4.a); 1,342 anchor refs, all resolve
  (`s0/scripts/check_coverage_refs.py`). Default rules logged in `s0/default-rules.tsv`: R1 61, R2 44 (mostly
  unsupported parts of a bullet left out), R3 6 (6.3.b, 3.3.c, 8.6.c, 8.6.e, 10.5.h, 10.6.c).
- **Skeleton:** `course.yaml` (`status: draft`, the platform's unpublished state), `m00-l01` written and
  blind-checked (`s0/verify-m00-and-style.tsv`: 8 fails, all fixed), 68 stubs from `s0/scripts/skeleton.py`.
- **Tooling:** `backend/scripts/tech_sources.py` (+ `fetch_rendered.cjs`): fetch, anchors, show, list,
  apply-licences.
