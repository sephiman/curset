# backend-in-depth — bank ledger

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

- Question style guide: `docs/backend-question-style.md` (requirements 6, plus the AGE bank lessons that still
  apply), blind-checked by Opus (`docs/backend-verification/s0/verify-m00-and-style.tsv`: 4 fixes).
- No questions yet. Quotas per lesson come from S1's `lesson_quota` over each lesson's F and X facts.
- Keys only on F and X bullets: 199 of 249 bullets (F 157, F+X 33, X 9); J 44 and dropped 6 carry none.
