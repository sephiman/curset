# Question style — backend-in-depth

Rules for writers and verifiers of every multiple-choice question in the course: static bank (6.1),
variant families (6.2), generators (6.3) and system-design cases (6.4). The voice of
`docs/prose-voice.md` applies to stems, options and explanations, and its "never does" list is a hard
constraint. The course is English only. Section numbers refer to
`docs/backend-in-depth-course-requirements.md`.

## 1. Form rules

Each rule is a check a verifier can answer yes or no.

- Four options, exactly one correct. No "all of the above", "none of the above" or "both A and B".
- The stem is one question or one statement to complete, 15 to 40 words (20 to 50 in a case). It carries every condition
  the answer depends on.
- Every option fits the stem grammatically and has the same shape as the others.
- A negative stem writes NOT or INCORRECT in capitals, or is rephrased positively.
- The key is not systematically the longest option, nor the shortest. Aim for the key being longest in
  about a quarter of the questions. The build script reports the length-edge and longest-is-correct
  statistics; both stay within ±1.5 standard deviations per lesson.
- Key position is balanced across a lesson. Set `correct` in the generating script from the key's text,
  never by hand, and print each stem with its keyed option before handing back.
- Each distractor is a real misconception, one a reader holds or a plausible neighbouring fact. A cited
  fact contradicts it. A distractor that is also arguably true fails the question.
- The explanation states why the key is right, then names each distractor by its content and gives the
  fact that rules it out. It never refers to an option by letter or position, because options are
  shuffled per learner.
- A distractor is never dismissed by the source's silence ("the documentation does not say so"). A
  sentence of the source must contradict it.
- One sentence is not reused for several distractors.
- Code in a stem or an option is formatted as code (inline backticks, or a fenced block in the stem).
  Identifiers, flags, SQL and HTTP methods in prose are inline code too.
- A fact that differs between versions names the version in the stem: "since Java 24", "in Spring Boot
  4", "in PostgreSQL 17". A stem without the version fails when another version changes the answer.
- Every question carries a citation that resolves to an anchor of the pinned version.
- The `extract` is present only when the source has `extract_allowed`. It is a literal substring of the
  cited anchor, checked by script. Without a licence, no extract.
- A question that fails verification is discarded, not repaired. A replacement is written only when the
  lesson falls under its minimum quota.
- No near-duplicates. Two questions on the same fact differ in angle and in distractors, or one goes.
- No streaks, points or engagement wording in any text.

## 2. Class rules

- A question is keyed only to an F or X fact. A J (judgement) statement is never the key.
- A J statement may appear in a stem only as an attributed premise ("According to …"). Verification checks
  the attribution, not the truth.
- F key: the explanation cites the stored Tier A anchor for the pinned version.
- X key: the evidence is the snippet, the command and the sha256 of its output, stored with the question.
  The snippet needs only the JDK and the Kotlin compiler. A claim that needs a database, a broker or
  another service is not X; it is F from documentation, or it is dropped.
- A fact is taken from the stored source or from an execution record, never from memory.
- A stem that names no source or version is read against every version and framework in the course. If
  another one changes the answer, the stem fails.

## 3. Code-reading questions (6.1, 6.2)

Four kinds: what the code prints, which line holds the bug, what the complexity is, which refactoring
preserves behaviour.

- The snippet compiles and runs on the pinned JDK (or Kotlin compiler). The recorded output is the key.
- A snippet that is deliberately broken says so in the stem, and the compiler or runtime error is
  recorded as its evidence.
- What-it-prints questions: the key is the exact output, including line order and the exception type when
  one is thrown. Distractors are outputs a real mistake produces: off-by-one, wrong evaluation order,
  ignored integer overflow, autoboxing identity, mutated shared state.
- Which-line-holds-the-bug: one defect only. Line numbers are those printed in the snippet. The other
  lines are correct under the pinned version.
- Complexity: the stem states what n is. Distractors are the neighbouring classes (n log n for n, n for
  n squared), each wrong for a stated reason.
- Refactoring: the key preserves behaviour on every input the stem allows. Each distractor changes
  behaviour on a named input, and the explanation gives that input and the result.
- Nondeterminism is out: no thread-timing, hash-order or wall-clock dependence unless the stem fixes it.
- Variant families: the script instantiates, runs and records the key. Distractors are computed by
  script from typical mistakes. No variant is accepted whose distractor equals the key.

## 4. System-design cases and generators

- A case has a scenario and 10 to 20 keyed questions. Each answer follows from an F fact. No free text.
- Case questions do not depend on one another, so the scheduler can show them alone. Figures a question
  needs are repeated in its stem.
- A generator cites the F fact its rule comes from, is seeded and deterministic, and has golden seeds.
- A generator explanation shows the computation: the inputs, each step with its number, the result. It
  states the formula once and then applies it.
- Numbers are chosen so the arithmetic is mentally tractable, and every distractor is the result of a
  named mistake (wrong unit, forgotten factor, off-by-one on `w + r > n`), not a random value.
- Distractors are distinct from the key and from each other after rounding.

## 5. Lessons carried over from the AGE bank

Ledger = `docs/age-bank-ledger.md`.

- Explanations that named options by letter had to be rewritten: 66 in one pass (ledger, Session 2
  summary).
- Explanations that skipped a distractor, or dismissed it by silence, were the commonest drop: 289 flagged,
  25 questions lost (ledger, "R3 closing steps", point 3).
- A distractor that is arguably true sinks the question; q219 was dropped for it (ledger, "Questions without
  an excerpt").
- A key that merges two items of the source, or rewords one, is dropped (ledger, same section, q350).
- Built as written, the bank had keys 1.6 characters longer than distractors (z = +3.07); check the
  statistics after each build, not at the end (ledger, Session 2 summary).
- Fixing the length edge by making every key short only moves the bias; keep both ends in range (ledger,
  Session 1 summary, lessons learned).
- Keys set by hand went onto the wrong option in a whole batch; set them from the key text (ledger, Bloque V).
- A stem with no version or norm is true under one version and false under another; name it (ledger,
  "R3 close", bloque VI drops: 291, mostly stems without the version).
- Official or reference questions are the commonest "lightly reworded" drop: new angle, new distractors
  (ledger, Bloque III). Here it applies to any question lifted from a source's own quiz or exam.
- Near-duplicates are found late; check them per lesson before verification (ledger, Bloque IV and V:
  q264, q265, q080).
- Options under five words fail unless they are a name, a quantity or a figure (ledger, Session 3
  summary). In this course a short option is fine when it is an identifier, a keyword, a status code or a
  complexity class.
- A verifier does not read the writer's notes before giving verdicts (ledger, verifier brief).
- Progress is logged after every part, so a cut window loses at most one part (ledger, Session 6 progress).

Not carried over:

- Currency audits against legal changes (BOE, RDL, "desde" rulings): the course pins versions instead.
- Spanish-language rules: Peninsular "tú", calque sweeps, the bilingual hour motif, ES plural gaps.
- Norm titles in stems, article-share targets, organ names and date-computation rules.
- Saved Microsoft pages and ofimática screenshots as sources.
- The official-exam presets, exam sheets and the `shuffle: false` rule: there is no official exam here.

## 6. Verifier verdict format

The verifier is an Opus agent that did not write the questions. It loads the questions and only the cited
anchors, and does not read the writer's notes first.

- One line per question: `<question id> pass` or `<question id> fail <reason>`.
- The reason is at most fifteen words and names the rule broken (for example "distractor 3 also true in
  Java 24" or "explanation names an option by letter").
- No question is repaired in the verdict. A failing question is discarded.
- A question passes only when the key follows from the cited anchor or the recorded execution, every
  distractor is contradicted by a cited fact, and every rule in sections 1 to 4 holds.
- The verdict file ends with the counts: checked, passed, failed.

## 7. Writer rules from module 06

Module 06 kept 68 of 144 candidates. Of the 76 failures, 32 had a stem under 15 words, 14 dismissed a
distractor by silence or bare denial, 12 left SQL or an identifier outside code, 8 ruled out two
distractors with one sentence, and 8 were near-duplicates (`docs/backend-verification/s2/m06/*.verdicts.tsv`).
Once these rules reached the writers, the pass rate rose from about 20 % to 65–85 %.
`scripts.tech_course.lint_questions` checks the mechanical ones; run it and fix every failure before a
verifier sees the batch.

- Count the stem's words before handing over: 15 to 40 (20 to 50 in a case). A short stem is lengthened
  with a condition the answer depends on (the version, the isolation level, the input size), never with
  padding.
- Every SQL keyword, statement, command, configuration key, class, method, annotation, flag, header and
  status code is inline code, in the stem, the options and the explanation: `VACUUM`, `UPDATE … WHERE`,
  `@Transactional`, `max_connections`, `ConcurrentHashMap`, `409`. Multi-line code is a fenced block.
- The explanation has one sentence for the key and one sentence per distractor. Each distractor sentence
  names the distractor by its content and states the cited fact that contradicts it.
- Two distractors are never ruled out by one sentence, and one source sentence is not reused for two
  distractors. If two distractors fall to the same fact, replace one.
- "The documentation does not say so", "nothing indicates" and bare denials ("this is not the case") are
  not refutations. If no cited sentence contradicts a distractor, replace the distractor.
- A distractor taken from the same source must be false under the pinned version, not merely less
  complete than the key. Read it as a learner who knows the source: if it could be defended, drop it.
- The key states one item of the source in the source's sense. It never merges two items or adds an
  alternative.
- Before handing over, compare the batch with itself and with the lesson's other questions: same fact
  and same distractors means a near-duplicate; keep one.
- Keep the key the longest option in at most a third of the lesson's questions. Shorten the key or
  lengthen a distractor with a real condition; do not trim every key to the shortest.
- Code-reading and computed questions leave `key` empty and name the `snippet`; `fill_keys` copies the
  recorded output into the key. Distractors still come from named mistakes.
