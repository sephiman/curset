# backend-in-depth — theory ledger

Requirements: `docs/backend-in-depth-course-requirements.md` v1.2 (v1.1 + amendments). A new session reads only «Where to resume».

## Where to resume

S2+S3 unattended run (2026-11-13/14) FINISHED: Part 0, Part 1 (all 12 modules) and Part 2 done. Nothing committed.
Course status: **published** (no lesson quarantined; close_round 3: backend 3697 passed, frontend 868, tsc clean,
audits 0 problems, other courses and Android bundle byte-identical; Playwright 131 passed; rerun after publishing).
Totals: 68 lessons written (m00 + 67), ~6,380 sentences (6,147 in m01–m11 + 231 J in m12), 383 esquema rows,
234 glossary terms; 703 static-bank questions in 62 quiz exercises; 6 design cases with 63 questions; 13
generators, 9 with a confirmed citation. Sentences deleted on second failure: 4 (+6 removed at rewrite); none >5 %.
Question pass rate per module (passed / verified incl. replacements): m01 46 % (54), m02 70 % (45), m03 90 % (61),
m04 76 % (45), m05 70 % (57), m06 (run 1–2, 88), m07 84 % (87), m08 87 % (62), m09 83 % (68) + cases 66 % (63),
m10 81 % (95), m11 72 % (41), m12 J only (no questions by design).
Thin banks (< 8 passed after the rules): m01-l04, m02-l04, m02-l06, m02-l07 (0, J), m04-l05, m05-l05, m05-l06,
m05-l07, m08-l01, m08-l03, m09-l01, m11-l02, m11-l03, m11-l04, m11-l05. Quarantined: none.
Not built: design case d (telemetry ingestion), 7 verified questions, under the loader minimum of 10 (I3).
Generators without a citation (no verified F sentence states the rule): rate-limiter-state, retry-backoff-bounds,
logical-clocks (H1), consistent-hashing-owner (I2).
Items left out for lack of source (details in each module block below): 2.2.d sweep line; LFU and rate limiter
(2.6.a); m07 L4/L7 and API gateway, 7.5.d/f/h; m09 p99, cache patterns, LSI/GSI, cross-shard joins, tenancy, fair
queuing; m10 parts of 10.4.a/c/d; m11 consumer lag; m12 several 12.3–12.5 archetypes; Dynamo two-column pages.
Method added this run: amendments 6–9; `check_refutations` + sidecars; `wire_exercises.py` (the static bank was not
declared in course.yaml before this run, W1); `build_case.py`; `near_duplicates.py`; 16 glossary `link_except`.
Part 2: presets (5, practice rounds, `s3/presets.md`), PDF (`s3/pdf-export.md`), glyph server-rack + green accent.
Open: S1 review items 7–9; m06-l01 length edge (C9); rerun `npm run identity` PNG step where Chromium is installed
(favicon unchanged, so optional); refutation maps for pre-run lessons (m01-l01..l03, m06) are exempt by R1.
Cost log: `docs/backend-verification/s2/cost.tsv` (~10M subagent tokens logged; ~15 h wall clock).

## Modules

| Module | Title | Lessons | Bullet classes (S0) | State | Session | Notes |
|---|---|---|---|---|---|---|
| 01 | Pragmatic software design and patterns | 4 | F 1 F+X 4 J 7 drop 2 | done, gate tripped | S2 run 2 (2026-11-13) | 47 questions; l04 skipped by guard |
| 02 | Algorithms and data structures | 7 | F+X 8 X 9 J 2 | done | S2+S3 (2026-11-14) | see «Module 02 — done» |
| 03 | Modern JVM, concurrency and performance | 4 | F 11 F+X 4 J 1 | done | S2+S3 (2026-11-14) | see «Module 03 — done» |
| 04 | Kotlin for Java developers | 5 | F 9 F+X 8 J 1 | done | S2+S3 (2026-11-14) | see «Module 04 — done» |
| 05 | Spring Framework and Spring Boot internals | 8 | F 28 | done | S2+S3 (2026-11-14) | see «Module 05 — done» |
| 06 | Relational persistence, transactions and SQL optimisation | 4 | F 11 | done | S2 (2026-11-13) | 88 questions after run-2 top-ups; see «S2 — module 06» |
| 07 | Networking and API design | 7 | F 24 F+X 1 J 3 | done | S2+S3 (2026-11-14) | see «Module 07 — done» |
| 08 | Distributed systems, messaging and resilience | 7 | F 30 J 2 | done | S2+S3 (2026-11-14) | see «Module 08 — done» |
| 09 | System design and data scalability | 5 | F 17 X 1 J 4 | done | S2+S3 (2026-11-14) | see «Module 09 — done» |
| 10 | Platform, observability, security and AI integration | 6 | F 20 F+X 1 J 4 | done | S2+S3 (2026-11-14) | see «Module 10 — done» |
| 11 | Code reading, debugging and testing | 6 | F 7 F+X 7 J 4 | done | S2+S3 (2026-11-14) | see «Module 11 — done» |
| 12 | Staff-level technical leadership | 5 | J 17 drop 1 | done | S2+S3 (2026-11-14) | see «Module 12 — done» |

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

## S2 — module 06 (2026-11-13)

Work folder `docs/backend-verification/s2/m06/` (briefs `s2/brief-writer.md`, `s2/brief-verifier.md`, tool
`s2/tools/build_quiz.py`, decisions `s2/m06/decisions.tsv`). Writers A (l01, l02) and B (l03, l04) on Sonnet;
verifiers 1 (l01, l02) and 2 (l03, l04) on Opus. One line per lesson, written as each part ends:

- m06-l01: written (F 84, rows 10, snippets 0, questions 33, quota 30); writer 4.7 min, 116k tokens. Verified
  (2.3 min, 105k): sentences 85/0, rows 10/0, glossary 6/0, questions 5 pass / 28 fail (stems under 15 words,
  SQL not in inline code, distractors ruled out by a shared sentence or by silence). 28 discarded; 5 under the
  minimum of 10, so replacements are owed (asked after l02). Failure patterns sent to both writers before l02/l04.
- Cost check after l01: ~7 agent-minutes and ~221k tokens per lesson before replacements; three lessons remain,
  so the module fits in this usage window.
- m06-l03: written (F 166, rows 10, snippets 0, questions 33, quota 30); writer 6.8 min, 149k tokens. Verified
  (3.4 min, 136k): sentences 175/0, rows 10/0, glossary 5/0, questions 7 pass / 26 fail (17 stems under 15
  words, 11 distractors dismissed by silence, 2 shared sentences, 1 lower-case negative stem, 1 arguably-true
  distractor). 26 discarded; 3 replacements owed for the minimum of 10.
- m06-l02: written by A (F 85 + write-skew addition, rows 10, snippets 0, questions 31 + up to 2); writer 6.6 min,
  189k tokens; stale stub (decision C8) sent back to A for write skew before verification.
- m06-l04: written by B (F 61, questions 31, quota 30); writer 7.3 min, 220k tokens (cumulative with l03 context).
  Expand/contract, batched backfill and backward compatibility left out (S0 R1: Tier C only). Verified (2):
  sentences 68/0, rows 4/0, glossary 2/0, questions 20 pass / 11 fail (near-duplicates, arguably-true distractor,
  a key merged with an alternative, a key on the wrong question, short stems). 20 kept; l04 done.
- m06-l03 replacements: writer D wrote q34–q39 (1.6 min, 79k); verifier 2 (l03 replacements + l04: 1.8 min,
  173k cumulative): 5 pass, 1 fail (14-word stem). Lesson now 12 questions; l03 done.
- m06-l01 replacements: writer C wrote q34–q41 (2.2 min, 81k); verifier 3 (1.1 min, 66k): 5 pass, 3 fail. Lesson
  now 10 questions (minimum). Length edge open (C9). l01 done.

**Handoff (module 06 done, 2026-11-13).** Pipeline 8.2 ran on all four lessons; nothing committed.

| Lesson | Sentences (fail→recheck) | Rows | Glossary | Q written | Q passed | Q discarded |
|---|---|---|---|---|---|---|
| m06-l01 | 85 (0) | 10 | 6 | 41 (33 + 8 repl.) | 10 | 31 |
| m06-l02 | 99 (1 → pass) | 10 | 3 | 33 | 28 | 5 |
| m06-l03 | 175 (0) | 10 | 5 | 39 (33 + 6 repl.) | 12 | 27 |
| m06-l04 | 68 (0) | 4 | 2 | 31 | 18 | 13 |

- No sentence deleted; 1 re-cite (l02 S5.2). Questions: 144 written, 68 kept, 76 discarded (first-pass rate
  in l01/l03 ~20 %: short stems, SQL not in code, distractors dismissed by silence or a shared sentence; once
  these rules were sent to the writers, l02/l04 kept 85 % and 65 %). 3 cross-lesson near-duplicates dropped.
- Generators: composite-index-usage and isolation-anomaly citations confirmed (11 owed). Isolation wording
  fixed: the "what PostgreSQL 18 does" form replaced by a neutral padding form (dropping it broke the
  length-balance tests); goldens regenerated (C6).
- Decisions C1–C12 in `s2/m06/decisions.tsv`: `quiz` in exercise_types; one exercise file per lesson; glossary
  and summaries staged then merged by `s2/tools/merge_glossary.py`; keys placed by `s2/tools/build_quiz.py`;
  no code-reading questions (all F); stale stub for 6.2.a (write skew) fixed from coverage/m06.final.tsv;
  6.4.a expand/contract, backfill and compatibility left out (Tier C only, S0 R1); S1 citation test replaced.
- Open: l01 length edge (key longest 6/10, +9.3 chars; C9), for S3. l02-l04 within range.
- Cost: ~25 min wall clock (start 20:33); writers ~586k tokens (A 206k, B 220k, C 81k, D 79k), verifiers
  ~428k (1: 168k, 2: 173k, 3: 87k). The subagent cap went from 4 to 8 mid-session at the user's request (C7);
  peak 4 running.
- close_round.sh: other courses and Android bundle byte-identical, frontend 833 passed, tsc clean, audits 0
  problems; backend 1 failure (the S1 citation test, C10), fixed, generator file rerun 105 passed.
- Next module: check each stub «Sources» against `s0/coverage/<module>.final.tsv` before writing (C8); send
  writers the question rules of C-notes up front; run the near-duplicate scan per module.

## S2 — run 2 (2026-11-13): part 0 fixes, then modules 01–05, 07–12

Prompt: part 0 (fixes from m06) then all remaining modules. Subagent cap 8 (4 writers, 4 verifiers): the global
CLAUDE.md cap replaces the lower cap of the session prompt (decision S1 below). Stop-gate figures come from
`s2/tools/module_report.py <module dir>`; the source guard from `scripts.tech_course.source_guard`.

Run decisions (`S<n>`): S1 cap 8 as above. S2 "stored source" = registered in `sources.yaml` or `s0/tier-b.yaml`
(amendment 5); `candidate:` URLs do not count for the guard. S3 Tier B J attributions claim no more than the
registered chapter titles and note; writers store open-edition books (Erickson, CC BY 4.0) as Tier C when a
bullet needs substance. S4 X sentences follow their snippet block with no citation parenthetical; the verifier
checks them against the run record. S5 writers write the quota (not quota + 3), per the session prompt.

- 0.1 done: style guide §7, 32 lines (m06 counts: 32 short stems, 14 silence, 12 code format, 8 shared, 8 dup).
- 0.4 done: amendment 5 appended to the requirements.
- 0.5 done: `fowler-parallel-change` stored (Tier C, local, no extract; author Danilo Sato); one J block of 6
  sentences in m06-l04; verified 6/6 pass. Batched backfill left out (no stored source; C13).
- 0.3 done: `refresh_stub_sources` + `source_guard` (+ `bullet_sources` helper, 6 tests); 28 stubs refreshed.
  The first guard run flagged 10 lessons, mostly over unfetched Tier C candidates. A fetcher stored 20 Tier C
  pages under the S0 rules (`s2/sources-added.tsv`; AIP-8 rejected). Still `skip`: m01-l04 (1.4.a, 1.4.c),
  m02-l02 (2.2.d), m12-l04 (12.4.a). Report in `s2/source-guard.tsv`.
- 0.2 built: `lint_questions`, `fill_keys` (+ `candidates` helper, 55 tests), called by close_round.sh. First run on
  m06's verified questions: 75 explanation-coverage hits on questions the verifier had passed, so it was sent
  back to be calibrated on m06 verdicts.
- 0.2 done: lint recalibrated on m06 verdicts (explanation rules: precision 15/16, recall 15/19; 68 tests).
  A null extract on an extract-allowed source is now a warning, since the prompt requires only that the field
  is present. Accepted hits on passed questions sit in `s2/lint-accepted.tsv` (m06-l03-q03 stem length,
  m06-l02-q29 paraphrase). m06 lints clean with `--exclude-failed`.
- m01-l03 (writer B): F 24 units, 0 snippets, questions 24 (quota 24), lint 14 fixed. The writer first omitted
  hexagonal and fitness-function J content. It was sent back, stored `cockburn-hexagonal-architecture` and
  `bea-evolutionary-architecture-precis` (Tier C, local) and added both as J (D2, D3).
- m01-l03 verified: sentences 35 (2 fail → rewritten → recheck pass), rows 3/0, glossary 2/0; questions 4/24
  first pass. 14 of the failures were only the Spring Modulith version in the stem. Ruling D7: the pin in
  versions.yaml (2.1.2) is correct when S0 kept 2.1.1 docs for it; the same verifier rechecked q01–q14 on all
  other rules: 8 pass. 12/24 passed, so a replacement batch q25–q34 (lint 0 first-run failures) went to the verifier.
- m01-l01 (writer A): F 34, rows 6, snippets 3, questions 30 (quota 30), lint 12 fixed; stored martin-srp-blog,
  fowler-yagni (Tier C). Law of Demeter and composition over inheritance omitted: Tier B titles state nothing (D6).
- m01-l02 (writer A): F 19, rows 2, snippets 3, questions 22 (quota 22), lint 8 fixed; 1.2.a/1.2.c J pointers to
  Tier B chapters (D8). Writer cost A 180k tokens / 11.5 min (l01+l02); B 143k (l03 + J fix + replacements).
- m01-l03 replacements: 4/10 pass; lesson ends 16/34 passed (done). Mixed 2.1.1/2.1.2 labels left for S3 (D9).
- m01-l02 verified (1997): sentences 35/0, rows 2/0, glossary 3/0, questions 5/22 (7 shared refuting sentence,
  6 silence/bare denial/memory, 1 arguably true, 2 unrelated snippet citation, 2 skipped distractor; short-key
  bias 14/22). Replacement batch of 15 asked from writer A.
- m01-l01 verified (4fce): sentences 52/3 (S3.19, S4.4, S6.4), rows 6/0, glossary 3/1 (g-sealed-class), questions
  8/30 (12 shared sentence, 5 silence/denial, 3 "in Java 25" for JEPs final in 16/21/17, 1 merged key). Writer C
  rewrites the 3 sentences and writes 12 replacements.
- Gate projection: m01 is at 29/86 (34 %); it trips the 60 % gate even if every replacement passes. The module
  pipeline is finished first; the session then stops at the gate.
- m01-l02 replacements: writer A wrote 9, not 15, saying the lesson's facts support no more without shared
  refuting sentences; all 9 passed. The lesson ends at 14 passed: under 15 after its one allowed batch, above
  the requirements' minimum of 10. Finding for the handoff: a self-checked batch sized to the facts passed 9/9.
- m06 top-up (0.6): l01 9/14 pass, l03 7/12 pass, so 19 each; a second batch of 3 per lesson asked.
- 0.6 done: m06-l01 10 → 21 passed (top-ups 9/14, 2/3), m06-l03 12 → 21 (7/12, 2/3). Key longest (lint):
  l01 5/21 = 24 %, l03 2/21 = 10 % (build_quiz, counting ties, 8/21 and 4/21). Exercise files rebuilt. The C9 length
  edge for l01 is closed.
- lint recalibrated a second time on m06 + m01-l02/l03: explanation rules precision 0.95, recall 19/33 = 0.58. The
  misses are refutations from memory, shared source sentences in paraphrase, and skipped distractors.

**Module 01 done, stop gate tripped (2026-11-13, 21:41–22:11).** `module_report.py s2/m01`:

| Lesson | Sentences (deleted) | Rows | Q written | Lint fixed | Q passed | Q discarded |
|---|---|---|---|---|---|---|
| m01-l01 | 55 (0; 3 rewritten → pass) | 6 | 42 (30 + 12 repl.) | 16 | 17 | 25 |
| m01-l02 | 35 (0) | 2 | 31 (22 + 9 repl.) | 8 | 14 | 17 |
| m01-l03 | 35 (0; 2 rewritten → pass) | 3 | 34 (24 + 10 repl.) | 14 | 16 | 18 |
| m01-l04 | skipped by the source guard (1.4.a, 1.4.c unsourced; D1) | | | | | |

- Gate: 47/107 candidates passed = 44 % (< 60 %), so the session stops. Deleted sentences 0 %; 1 lesson skipped.
- First-pass rate 17/76 = 22 %; replacement batches 22/31 = 71 %; the self-checked batch sized to the facts, 9/9.
  Lint cleared what it can see (38 first-run failures fixed). What failed after lint was semantic: one source
  sentence refuting two distractors (≈30), silence, bare denial or memory (≈16), arguably-true distractors, and
  JEP release versions.
- Glossary: 8 merged, g-sealed-class dropped. Summaries applied (`s2/tools/apply_summaries.py`). No generator
  names an m01 lesson. Decisions D1–D9 in `s2/m01/decisions.tsv`. The cross-lesson near-duplicate scan was not run (owed).
- Cost: writers A 195k (l01, l02 + 9 repl.), B 143k (l03 + J fix + repl.), C 101k (l01 fixes + repl.); verifiers
  118k (l01), 86k (l02), 105k (l03). Part 0: tools 162k + 62k, fetcher 64k, l04 J 62k + 46k, m06 top-up 159k + 129k.

## S2+S3 — unattended run (2026-11-13, started ~23:00)

Method (prompt of this run): no gate; amendments 6–9; questions sized to facts; refutation sidecar
`<lesson>.refutations.yaml` checked by `scripts.tech_course.check_refutations` (called by `lint_questions` and
`close_round.sh`); writers on Sonnet, verifiers on Opus, a verifier never verifies its own lesson; fix rules: a
failed sentence is rewritten once, deleted on a second failure; a failed question is discarded; one replacement
batch only when < 8 passed, unused facts remain and the first batch passed ≥ half, else "thin bank"; > 5 % of a
lesson's sentences deleted → quarantine (`docs/backend-verification/quarantine/`, stub restored).

### Part 0 (2026-11-13)

- 0.1 Amendments 6–9 appended to the requirements.
- 0.2 `check_refutations` (+ 8 tests in `test_tech_course_refutations.py`); `failed_ids` moved to `candidates.py`.
  Lessons verified before the sidecar existed (m01-l01..l03, m06-*) are listed in `s2/refutations-exempt.tsv`
  (decision R1: the prompt forbids changing passed questions' format; maps for them would be retrofitted, not evidence).
- Amendment 7 in `source_guard`: dropped bullets not counted; verdicts `write` / `fetch` (> 1/5 unsourced: try
  once, then write the sourced bullets) / `skip` (nothing sourced). Re-run: every pending lesson `write`.
- Briefs updated: fact list `<lesson>.facts.tsv`, refutation map, amendment 9, J attributed to the page's actual
  author; `show` needs `--course backend-in-depth` (the old brief omitted it). `s2/tools/near_duplicates.py` (new),
  `module_report.py` gains facts and quarantine/thin flags.
- 0.4 m01 cross-lesson near-duplicate scan: 0 cross-lesson pairs at Jaccard ≥ 0.3 (10 within-lesson pairs, all
  under 0.45, already judged by the verifiers).
- 0.3 Open textbooks (amendment 6): 50 Tier A sources, 12 `erickson-*` (9 book chapters CC BY 4.0, extracts
  allowed; 3 lecture notes CC BY-NC-SA 4.0, local, no extract) and 38 `ods-*` (Morin, Edition 0.1G, CC BY 2.5 CA).
  4 ODS pages failed to fetch (section pages cover them). Anchors added to `s0/coverage/gaps.tsv` for all m02
  bullets except 2.2.b and 2.5.d (Javadoc only); 2.2.d stays dropped (no source covers sweep line). m02 stubs
  refreshed; guard: all `write`. Decision B1.
- 0.4 m01-l04 written from 1.4.b (D10): 38 sentences, 35 facts, 8 questions; in verification.
- m01-l04 done: 50 sentences (S1.11 removed on rewrite, S4.7 rewritten and passed; 0 deleted on second failure),
  4 rows, 36 facts, 11 questions written, 7 passed, 4 discarded (one replacement batch: 2/3) → **thin bank**.
  Glossary 3 merged (g-interrupt-status failed). Writer 133k tokens, verifier 97k, ~10 min. m01 now 54 questions.
- `build_quiz.py` now reads the sibling verdict file by default (without `--verdicts` it had kept failed
  questions); m01-l01..l03 rebuilt byte-identical.

### Module 03 — done (2026-11-14)

| lesson | sentences | deleted | rows | facts | q written | passed | discarded | note |
|---|---|---|---|---|---|---|---|---|
| m03-l01 | 205 | 1 (S7.16) | 18 | 190 | 22 | 19 | 3 | |
| m03-l02 | 209 | 0 | 9 | 187 | 16 | 14 | 2 | |
| m03-l03 | 160 | 0 | 15 | 159 | 19 | 18 | 1 | |
| m03-l04 | 111 | 1 (S4.30, removed on rewrite) | 12 | 104 | 11 | 10 | 1 | 3.4.e partly J |

Pass rate 61/68 = 90 %. No thin bank, no quarantine; 24 glossary terms merged; summaries applied. Near-duplicate
scan: 0 pairs at ≥ 0.45. Audits clean (citations, extracts, scope, coverage, snippets, lint+refutations).
Decisions C101–C105, C301–C308 (omissions for lack of a stored anchor: JMH warm-up, flame-graph reading,
percentiles vs means, parts of 3.4.e; no snippet for preview StructuredTaskScope), C001 (exclusive-group ruling:
8 questions re-judged once on that point, 7 passed). No generator family belongs to m03.
Cost: writers 2 × ~17 min, 568k + fixes 9k tokens; verifiers 383k + rechecks 6k tokens; elapsed ~45 min.
Script fix: `check_coverage` now takes dropped bullets from `bullet_sources.dropped_bullets` (R2 without a stored
source counts as dropped, as the stubs show); it had flagged 2.2.d as uncovered. `programme.dropped_bullets` removed.

### Module 02 — done (2026-11-14)

| lesson | sentences | deleted | rows | facts | q written | passed | discarded | note |
|---|---|---|---|---|---|---|---|---|
| m02-l01 | 95 | 1 (S2.2) | 12 | 92 | 12 | 8 | 4 | |
| m02-l02 | 63 | 1 (S4.1) | 6 | 56 | 12 | 9 | 3 | 2.2.d dropped (no source) |
| m02-l03 | 72 | 0 | 5 | 66 | 14 | 9 | 5 | key-longest 44 % accepted (B2) |
| m02-l04 | 65 | 0 | 4 | 46 | 8 | 5 | 3 | **thin bank** |
| m02-l05 | 79 | 0 | 0 | 59 | 10 | 9 | 1 | |
| m02-l06 | 50 | 0 | 0 | 33 | 8 | 5 | 3 | **thin bank**; LFU and rate limiter omitted (no source, B405) |
| m02-l07 | 10 | 0 | 4 | 4 | 0 | 0 | 0 | **thin bank**: J (4 Erickson blocks), no refutable fact |

Pass rate 45/64 = 70 %. Deleted 2/434 sentences. 17 glossary terms merged. Near-duplicates: 0 at ≥ 0.45.
Generators confirmed (B3): lru-cache-contents, binary-heap-contents, loop-complexity (8 still unfilled, later modules).
Items left out for lack of source: 2.2.d sweep line; LFU cache, in-memory rate limiter (2.6.a); tries and top-K
sentences (B104); comparison-sort lower bound (B105). Decisions B1, B101–B106, B401–B408, B2–B4.
Cost: writers 2 × ~17 min, 520k + fixes 35k tokens; verifiers 353k + rechecks 14k; elapsed ~75 min.
Script fixes: `lint_questions` honours an accepted `key-longest-share` (+ test); m02-l03 summary no longer uses
the glossary term "binary heap" its lesson never uses in prose (registry check).

### Module 04 — done (2026-11-14)

| lesson | sentences | deleted | rows | facts | q written | passed | discarded | note |
|---|---|---|---|---|---|---|---|---|
| m04-l01 | 82 | 0 | 7 | 68 | 13 | 9 | 4 | |
| m04-l02 | 125 | 0 | 8 | 111 | 13 | 10 | 3 | |
| m04-l03 | 138 | 0 | 9 | 124 | 17 | 12 | 5 | stdlib-only snippet, no kotlinx.coroutines |
| m04-l04 | 79 | 0 | 3 | 68 | 11 | 9 | 2 | |
| m04-l05 | 35 | 0 | 0 | 22 | 5 | 5 | 0 | **thin bank** (one replacement batch: 1/1); 4.5.b J |

Pass rate 45/59 = 76 %. 0 sentences deleted (6 rewritten, all passed). 15 glossary terms merged; 5 failed.
Near-duplicates 0. No generator family belongs to m04. Decisions E101–E105, E401–E405 (E401–E403 restored by the
coordinator: a writer recreated decisions.tsv and lint.tsv with `>`; brief now says append only).
Left out for lack of source: "common mistakes" in 4.5.b; coroutine and Spring parts of 4.4.c not X.
Cost: writers 446k + fixes 6k tokens, ~19 + 10 min; verifiers 306k + rechecks 3k; elapsed ~60 min.

### Module 05 — done (2026-11-14)

| lesson | sentences | deleted | rows | facts | q written | passed | discarded | note |
|---|---|---|---|---|---|---|---|---|
| m05-l01 | 88 | 0 | 4 | 81 | 11 | 9 | 2 | |
| m05-l02 | 74 | 0 | 4 | 68 | 11 | 8 | 3 | one replacement batch (1/2) |
| m05-l03 | 75 | 0 | 0 | 64 | 10 | 8 | 2 | |
| m05-l04 | 80 | 0 | 0 | 70 | 8 | 8 | 0 | |
| m05-l05 | 81 | 0 | 0 | 71 | 10 | 5 | 5 | **thin bank**; q03 dropped as near-duplicate of m05-l04-q07 (F1) |
| m05-l06 | 76 | 0 | 0 | 66 | 9 | 7 | 2 | **thin bank** |
| m05-l07 | 60 | 0 | 0 | 51 | 6 | 3 | 3 | **thin bank** (first batch 2/6, no replacements) |
| m05-l08 | 71 | 0 | 0 | 61 | 17 | 9 | 8 | |

Pass rate 57/82 = 70 %. 0 sentences deleted (6 key points rewritten, all passed). 17 glossary terms merged.
No snippets (Spring needs more than the JDK: F only, F102). No generator family. Decisions F101–F105,
F501–F505, F1. Writers under-sized banks (5–6 questions for 51–71 facts); the replacement batch then failed on
misused `exclusive: true` (5 of 6 groups), so the brief now defines exclusive as single-valued attributes only.
Cost: writers 511k + fixes 16k tokens, ~17 + 13 min; verifiers 302k + rechecks 20k; elapsed ~55 min.

### close_round after modules 02–04 (2026-11-14)

Other courses and the Android bundle byte-identical; backend 3676 passed, 44 skipped; tsc clean; run_snippets,
check_citations, check_extracts, check_scope, check_coverage and check_refutations clean. Two failures, both
from in-flight work, not from a finished lesson: (1) lint_questions on m08 questions still being written (writer
lints before hand-off); (2) frontend `glossary/report.test.ts` golden (backend-in-depth en): new glossary terms
from m02–m05 are listed as unlinked, the same expected drift as run 2; regenerated with UPDATE_GLOSSARY_LINKS=1
at each module close from now on.

### Module 07 — done (2026-11-14)

| lesson | sentences | deleted | rows | facts | q written | passed | discarded | note |
|---|---|---|---|---|---|---|---|---|
| m07-l01 | 127 | 0 | 4 | 115 | 19 | 16 | 3 | socket timeouts F only (no loopback in sandbox) |
| m07-l02 | 112 | 0 | 3 | 102 | 14 | 10 | 4 | HTTP/3 and WebSocket framing thin (heading-only anchors) |
| m07-l03 | 102 | 0 | 3 | 85 | 14 | 13 | 1 | 8 J blocks (Envoy, Cloudflare Tier C); L4 vs L7 and API gateway left out |
| m07-l04 | 109 | 0 | 6 | 103 | 14 | 10 | 4 | key-longest 50 % accepted (G1) |
| m07-l05 | 107 | 0 | 2 | 94 | 16 | 14 | 2 | 7.5.a as J (google-aip-121); 7.5.d params, 7.5.f, 7.5.h left out |
| m07-l06 | 102 | 0 | 12 | 97 | 15 | 13 | 2 | |
| m07-l07 | 70 | 1 (S5.3, removed on rewrite) | 10 | 59 | 12 | 11 | 1 | |

Pass rate 87/104 = 84 %. 33 glossary terms merged, 1 then removed (g-sunset-header: the lesson writes it only in
code, so the registry saw a coined term; G2). Near-duplicates 0. No generator family. Decisions G101–G113,
G501–G512, G1, G2. Glossary link golden regenerated; 5 false friends given `link_except` (carrier, deadline,
migrations, pattern matching; G2), found by reading the new marks before accepting the golden.
Cost: writers 658k + fixes 4k tokens, ~26 + 17 min; verifiers 425k + rechecks 3k; elapsed ~70 min.

### Module 08 — done (2026-11-14)

| lesson | sentences | deleted | rows | facts | q written | passed | discarded | note |
|---|---|---|---|---|---|---|---|---|
| m08-l01 | 43 | 0 | 11 | 46 | 8 | 6 | 2 | **thin bank** (one replacement batch: 2/3) |
| m08-l02 | 131 | 0 | 13 | 131 | 9 | 8 | 1 | |
| m08-l03 | 63 | 1 (S7.1) | 9 | 50 | 7 | 6 | 1 | **thin bank**; saga theory J (microservices.io) |
| m08-l04 | 92 | 0 | 12 | 81 | 9 | 8 | 1 | one replacement batch (3/3) |
| m08-l05 | 104 | 0 | 6 | 89 | 10 | 9 | 1 | fencing tokens and 2PC blocking J (Kleppmann, Cambridge notes) |
| m08-l06 | 118 | 0 | 6 | 96 | 13 | 11 | 2 | CQRS / event sourcing J (Fowler) |
| m08-l07 | 135 | 0 | 11 | 132 | 15 | 14 | 1 | |

Pass rate 62/71 = 87 %. 29 glossary terms merged. Near-duplicates 0. Generators: circuit-breaker-state and
kafka-consumer-lag confirmed; rate-limiter-state, retry-backoff-bounds, logical-clocks left unfilled (H1).
Decisions H101–H113, H501–H507, H1, H2. 7 Tier C sources added (local, J only).
Cost: writers 677k + fixes 28k tokens, ~22 + 25 min; verifiers 467k + rechecks 15k; elapsed ~75 min.

### Exercise wiring (2026-11-14, decision W1)

Found while preparing the m09 cases: no lesson in `course.yaml` declared its `exercises/<lesson>-ex-1.yaml`, so the
registry loaded none of the static bank (only the 13 generators); this dates from S2 m06 (C2 created the files,
nothing declared them). `s2/tools/wire_exercises.py` (idempotent) now declares every built `-ex-1` quiz under its
lesson and takes `--case LESSON=CASE_ID` for cases. 50 exercises wired after m09; registry loads them; backend
course/registry/practice tests 314 passed. Re-run it at every module close. Also new: `s2/tools/build_case.py`.
Generator test `test_a_confirmed_citation_is_cited_by_its_own_lesson` requires `confirmed` to be a
`source#anchor` the lesson cites: capacity-estimation confirmed as `paper-oneil-lsm-tree#p3` (m09-l01 f08).

### Module 12 — done (2026-11-14)

All class J (Tier C), theory only, no questions (requirements). Sentences verified for attribution only:
m12-l01 45 (S1.13 re-pointed, passed), l02 34, l03 41, l04 25 (12.4.a dropped), l05 86 (S2.7 removed on rewrite;
S1.3, S7.9, S8.5, S8.6 re-pointed, passed). 0 deleted on second failure (1 removed of 231, 0.4 %). Key points
omitted (no F/X facts to restate; M8). 5 glossary terms merged. 4 Tier C sources added (Nygard ADR, GitLab
communication, Abseil SWE ch. 10, Fowler technical debt). Left out for lack of source: Rust RFC/KEP processes
(12.1), own contribution vs team, level-by-level assessment, cross-team influence, simpler-option and mentoring
archetypes (12.3), business stability and promotion (12.4), incremental data migration and the technical-debt
portfolio framing (12.5). Decisions M1–M8. Cost: writer 165k tokens ~8 min; verifier 136k ~3 min.

### Module 10 — done (2026-11-14)

| lesson | sentences | deleted | rows | facts | q written | passed | discarded | note |
|---|---|---|---|---|---|---|---|---|
| m10-l01 | 102 | 0 | 4 | 77 | 17 | 14 | 3 | USE and RED as J (Gregg, Grafana) |
| m10-l02 | 155 | 0 | 11 | 149 | 28 | 22 | 6 | NEN 7510 named in J only (Tier B) |
| m10-l03 | 108 | 1 (S4.30, removed on rewrite) | 3 | 97 | 27 | 21 | 6 | |
| m10-l04 | 66 | 0 | 15 | 63 | 13 | 9 | 4 | one replacement batch (2/3); 10.4.a/c/d partly left out (K402, K403) |
| m10-l05 | 157 | 0 | 10 | 145 | 14 | 12 | 2 | 10.5.e as J (Hodgson, feature toggles) |
| m10-l06 | 142 | 0 | 28 | 155 | 19 | 17 | 2 | |

Pass rate 95/118 = 81 %. 33 glossary terms merged. Near-duplicates 0. No generator family. Decisions
K101–K105, K401–K406. Glossary false friends (span, propagation, deadline, starter) given link_except; golden
regenerated. Cost: writers 603k + fixes 23k tokens, ~20 + 18 min; verifiers 449k + rechecks 8k; elapsed ~60 min.

### Module 11 — done (2026-11-14)

| lesson | sentences | deleted | rows | facts | q written | passed | discarded | note |
|---|---|---|---|---|---|---|---|---|
| m11-l01 | 133 | 0 | 5 | 117 | 12 | 12 | 0 | 6 code-reading |
| m11-l02 | 101 | 0 | 4 | 77 | 11 | 6 | 5 | **thin bank**; 2 "replacements" were repairs, discarded (L1) |
| m11-l03 | 75 | 0 | 4 | 55 | 9 | 5 | 4 | **thin bank**; same (L1); consumer lag left out (no defining sentence) |
| m11-l04 | 68 | 1 (S5.7, removed on rewrite: false on Java 25) | 4 | 54 | 9 | 6 | 3 | **thin bank** (replacement 0/1) |
| m11-l05 | 19 | 0 | 0 | 6 | 2 | 2 | 0 | **thin bank**: mostly J (Amazon SDE II page); facts are snippet outputs |
| m11-l06 | 159 | 0 | 6 | 120 | 14 | 10 | 4 | |

Pass rate 41/57 = 72 %. 18 glossary terms merged. Near-duplicates 0. No generator family. Decisions L101–L114,
L401–L412, L1. Cost: writers 574k + fixes 20k tokens, ~21 + 18 min; verifiers 356k + rechecks 5k; elapsed ~65 min.

### Module 09 — done (2026-11-14)

| lesson | sentences | deleted | rows | facts | q written | passed | discarded | note |
|---|---|---|---|---|---|---|---|---|
| m09-l01 | 67 | 0 | 0 | 40 | 9 | 7 | 2 | **thin bank** (replacement 2/3); capacity X snippets |
| m09-l02 | 146 | 0 | 8 | 125 | 20 | 17 | 3 | 7 sentences rewritten, all passed |
| m09-l03 | 81 | 0 | 2 | 69 | 12 | 10 | 2 | |
| m09-l04 | 221 | 0 | 4 | 183 | 26 | 23 | 3 | q09 near-duplicate dropped |
| m09-l05 | 151 | 0 | 2 | 122 | 15 | 11 | 4 | q02, q13 near-duplicates dropped; 9.5.e as J |

Lessons: 68/82 = 83 %. Cases (requirements 6.4), all under m09-l04: a rate limiter 11, b booking 10, c notifications
11, e URL shortener/IDs 10, f search 10, g AI gateway 11 → 63 case questions (63/95 = 66 %); **case d (telemetry
ingestion) not built: 7 verified, under the loader minimum of 10** (I3). Scenarios each rewritten once (summary
closer), all passed. 17 glossary terms merged. Generators: quorum-reads and capacity-estimation confirmed;
consistent-hashing-owner unfilled (I2). Left out for lack of a stored sentence: p99, read-through, write-behind,
cache stampede, hot keys, LSI vs GSI, cross-shard joins, database per tenant, fair queuing (I101–I112), Dynamo
details (two-column PDF text, I403), AI gateway specifics (I404). Decisions I1–I3, I101–I112, I401–I408, I901–I904.
Cost: writers 629k + cases 223k + fixes 40k tokens; verifiers 469k + cases 210k; elapsed ~110 min.

## S3 — Part 2 finalization (2026-11-14)

- 2.1 Whole-course audits (close_round 2): other courses and Android bundle byte-identical; frontend 833 passed;
  tsc clean; run_snippets 101, check_citations 1353, check_extracts 428/703, check_scope 68 lessons,
  check_refutations 626 — all 0 problems; check_coverage 0 uncovered. Fixed by hand: g-quantile definition (`*` →
  `×`, K1), m12-l03 summary named migrations (M9). Lint failures were in-flight case files, fixed before build.
- 2.2 Glossary: 234 terms, no duplicate ids or terms (normalised); no "see n.n" cross-references in the lessons.
  Version labels: 35 stems named patch versions; unified to major.minor (D11, closes D9). 16 false friends carry
  `link_except` (decided module by module, G2, H2).
- 2.3 presets, 2.4 PDF, 2.5 glyph: delegated (records in docs/backend-verification/s3/). `pdf_exercises: true`.
- Generators with a confirmed citation: 9 of 13. Unfilled: rate-limiter-state, retry-backoff-bounds,
  logical-clocks (m08, H1), consistent-hashing-owner (m09, I2): no verified F sentence states their rules.
- 2.5 Glyph and accent (docs/identity.md): glyph `server-rack` (two stacked units with status light and vent; 24
  box, 2 stroke, radius 1, currentColor); accent green `#296c2e` (5.34:1 on paper) / `#44b34d` (5.96:1 on ink, 7.80:1
  on black); luminance spread across five courses 1.059 / 1.029 (< 1.15). identity.md decisions 8 and 9 updated.
  `npm run identity` regenerated SVGs and tokens; PNG step skipped (no local Chromium) — favicon unchanged, so no
  PNG change needed. Identity, courses, dev, pdf tests 59 + 56 passed; backend test_course_identity 15 passed.
- 2.4 PDF export (record `s3/pdf-export.md`): fenced code in Liberation Mono on a shaded panel, inline code in
  question stems and options mono, judgement as a bordered block with source and ref, key-sheet citations
  `source_id#anchor` (pinned by tests); DejaVu Sans fallback for emoji in an m11-l05 snippet; cases are left out of
  the per-tema questionnaire (a case question needs its scenario). Tests assert on the document definition only;
  vitest 82 files, tsc clean, test_pdf_export_scope 17 passed; other courses' PDFs unchanged. Needed
  `lesson_practice: true` for the questionnaire draw: passed to the presets work.
- 2.3 Presets (record `s3/presets.md`): five practice presets (lesson, module, mixed review, code reading,
  generators) as practice rounds, not exams (the exam engine scores every sitting and has no scheduler); course.yaml
  gains `lesson_practice: true` and `practice_presets`; new endpoints `POST /modules/{id}/practice` and
  `POST /practice/code-reading` (66 snippet questions), spaced scheduler; Practice card with one button per preset,
  module-page entry; cases stay in m09-l04 only. Tests: test_practice_presets 14, PracticePresets.test.tsx at 390 and
  1280 px; backend 3695 passed; vitest, tsc, ruff, mypy clean; bundle byte-identical; README and content/README updated.

## Gap round (2026-11-14)

Prompt: G1–G6 (wiring in close_round, generator rules, case d, left-out topics, thin banks, audits). Brief addendum
`docs/backend-verification/gap/brief-gap.md`; G4 items `gap/g4-items.tsv`, attempts `gap/fetch-attempts.tsv`.
Added sentences are listed per lesson in `s2/<module>/<lesson>.additions.tsv` (ids `A<n>`) and verified there.

- G1 done: `wire_exercises.py` wires every `m09-case-*.yaml` under m09-l04 (requirements 6.4) and dedupes requests;
  close_round.sh runs it before pytest; `backend/tests/test_backend_exercise_wiring.py` fails when an exercise file
  is not declared in course.yaml (checked with a planted undeclared file). Wiring run: 68 exercises, no change.
- G2 rate limiter: `rfc2697`, `rfc2698`, `redis-ratelimiting-algorithms` stored; m08-l04 A1–A6 F + A7 J (full jitter,
  `aws-arch-backoff-simulator`, Tier C) all passed, q10 passed. `rate-limiter-state` confirmed
  (rfc2697#section-3; redis-ratelimiting-algorithms#how-it-works-3, #how-it-works-1); the `(t - w, t]` window edge is
  the stem's own assumption, no source states it. `retry-backoff-bounds` confirmed as J (`aws-arch-backoff-simulator#top`),
  explanation now opens with the attribution; the generator test accepts a judgement `ref` as a J citation.
- G2 hashing: `paper-dynamo-columns` (column-split re-extraction) stored; m09-l02 A1–A5 passed;
  `consistent-hashing-owner` confirmed (paper-dynamo-columns#p10; #p11). Karger 1997: fetch refused (403).
- G2 clocks: `paper-lamport-time-clocks-columns` (OCR re-extraction). m08-l01 A1 (IR1) passed on recheck; A2, A4
  (IR2) passed on fact but failed twice on repeated paragraph openers, so deleted with key point A8; q12 (key on
  A4) discarded. A5–A7 (Dynamo vector clocks) passed. `logical-clocks` stays unfilled: the receive rule has no
  verified sentence. m08-l01 G5: q09, q10 passed, q11 failed (none-option).
- G3 done: case d q16–q21 written, 4 passed (q18, q20 failed: refutation not in the cited sentence), so 11 verified;
  built by `build_case.py` (key longest 3/11) and wired under m09-l04 (69 exercises). `test_practice_presets` now
  expects 7 cases.
- G5 verified so far: m08-l03 7/8 (q08 near-duplicate of q02), m09-l01 4/4, m01-l04 2/2, m02-l04 1/2, m02-l06 1/2
  (+ q11, q12 from the LFU facts, 2/2), m02-l07 0/2 (O-bounds are not exclusive, C001), m04-l05 2/2, m08-l01 2/3.
- G4 m02-l06: LFU (Redis approximated LFU, F) and token-bucket rate limiter (F) + Bucket4j J; 15/15 passed.
  G4 m02-l02, m07-l03, m07-l05, m09-l01..l03: J blocks only (Tier C sources), no questions; in verification.
  `sre-book-monitoring` is Tier C in sources.yaml, so p99 is J (GAP8). GAP ids renumbered GAP1–GAP20 after parallel writers collided.
- G5 final (kept per thin lesson): m01-l04 9, m02-l04 6, m02-l06 8, m02-l07 0, m04-l05 7, m05-l05 9, m05-l06 10,
  m05-l07 6, m08-l01 8, m08-l03 12, m09-l01 10, m11-l02 8, m11-l03 7, m11-l04 8, m11-l05 2 (no unused fact fits).
- G4 final: 18 of 22 items stored; written as J except LFU, token bucket (m02-l06), permission-aware vector stores
  (m10-l04) and consumer lag (m11-l03), which are F. Still without a source: L4 vs L7, cache patterns (read-through,
  write-behind, stampede, hot keys), cross-shard joins, fair queuing. Attributions fixed to byline authors (Chris
  Richardson, Gary Niemen, Jacqueline Xu).
- G6: whole-course near-duplicate scan dropped m08-l03-q11, m09-l01-q12, m09-l02-q01; close_round 1: backend 3701
  passed, audits 0 problems, other courses and bundle byte-identical, frontend 1 failure (glossary link golden:
  replay in m07-l05 and migrations in m12-l05 given link_except, golden regenerated). Playwright 131 passed.
  close_round 2 was stopped by the user before it finished; it has not been rerun since the module summaries.
- G0 (asked mid-round): module summaries m01–m05, m07–m12 written in course.yaml; test
  `backend/tests/test_course_module_summaries.py` fails on a published course with a missing or placeholder
  module summary (checked against the committed manifest). m00-l01's lesson summary is still "Summary pending."
