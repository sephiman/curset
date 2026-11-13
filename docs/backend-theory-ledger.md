# backend-in-depth — theory ledger

Requirements: `docs/backend-in-depth-course-requirements.md` v1.2 (v1.1 + amendments). A new session reads only «Where to resume».

## Where to resume

S2 run 2 (2026-11-13) STOPPED at the gate after module 01: 47/107 candidates passed (44 % < 60 %). Nothing committed.
Done: S0, S1, m06 (88 q), m01 (47 q; l04 skipped by guard). Next: m02, then 03–05, 07–12. Totals so far: 7 lessons,
135 questions, 0 sentences deleted. Details: «S2 — run 2» below; decisions `s2/m01/decisions.tsv`, run rules S1–S5.
Part 0 done: style guide §7; `lint_questions`, `fill_keys` (in close_round.sh, accepted hits in `s2/lint-accepted.tsv`);
`refresh_stub_sources`, `source_guard` (`s2/source-guard.tsv`); amendment 5; m06-l04 J block (6/6); m06-l01/l03 at 21.
Guard skips (one per module, under the gate): m01-l04 (1.4.a, 1.4.c), m02-l02 (2.2.d), m12-l04 (12.4.a).
20 Tier C pages stored for flagged bullets (`s2/sources-added.tsv`); writers store `candidate:` URLs as they go.
Tools: `s2/brief-writer.md`, `brief-verifier.md` (with "Coordinator rulings"), `s2/tools/` build_quiz (recheck-aware),
merge_glossary, apply_summaries, module_report (gate figures). Verdict files: a `recheck` line replaces the first.

Why the gate tripped: Sonnet first-pass question rate in m01 was 22 %. Lint fixed 38 mechanical failures, but
the semantic ones remain: one source sentence refuting two distractors, refutation by silence or memory,
arguably-true distractors. Replacement batches passed 71 %, and a batch the writer sized to the facts passed 9/9.
What the next run needs before m02 (the user decides; the gate is in the prompt):
1. Size question quotas to the facts: lessons with many J bullets (m01, m02, m12) can't support quota-sized banks.
   Let writers write fewer, or lower lesson_quota for J-heavy lessons.
2. Add a refutation map: each distractor names its own anchor sentence (a stored, unshown field), checked by a
   script for distinctness. This is the failure lint can't see (recall 0.58).
3. Or reconsider the 60 % gate for first-pass candidates. With replacements counted, m01 sits at 44 %.
Owed: m01 cross-lesson near-duplicate scan; unify Spring Modulith 2.1.1/2.1.2 stem labels (D9); 11 generator
citations (`export_backend_goldens.py --citations`); S1 open review items 7–9; S3 items listed in «S2 — module 06».
close_round (22:30): other courses and Android bundle byte-identical; backend 3662 passed; tsc clean; audits 0
problems; lint 0 failures. Frontend: 1 failure, the glossary link golden: 8 new m01 terms are listed as unlinked
and no mark moved. Regenerated (UPDATE_GLOSSARY_LINKS=1); file rerun 40 passed.
Requirements v1.2 + amendment 5. Subagent cap used: 8 (global CLAUDE.md); peak 4 running.

## Modules

| Module | Title | Lessons | Bullet classes (S0) | State | Session | Notes |
|---|---|---|---|---|---|---|
| 01 | Pragmatic software design and patterns | 4 | F 1 F+X 4 J 7 drop 2 | done, gate tripped | S2 run 2 (2026-11-13) | 47 questions; l04 skipped by guard |
| 02 | Algorithms and data structures | 7 | F+X 8 X 9 J 2 | pending | — | |
| 03 | Modern JVM, concurrency and performance | 4 | F 11 F+X 4 J 1 | pending | — | |
| 04 | Kotlin for Java developers | 5 | F 9 F+X 8 J 1 | pending | — | |
| 05 | Spring Framework and Spring Boot internals | 8 | F 28 | pending | — | |
| 06 | Relational persistence, transactions and SQL optimisation | 4 | F 11 | done | S2 (2026-11-13) | 88 questions after run-2 top-ups; see «S2 — module 06» |
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
