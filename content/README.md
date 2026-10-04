<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# Course content

The canonical source of every course: one directory per course, `content/<slug>/`, all with the same
structure and run through the same pipeline. Nothing is shared between courses — no glossary, no
lesson, no exercise. Inside a course, structure lives in the manifest; prose and generator configs
live in parallel trees, all keyed by stable IDs.

```
<slug>/
course.yaml           the manifest: course → blocks → modules → lessons → exercises (order = list position)
<lang>/lessons/*.md   lesson prose, one tree per language the course declares — one file per lesson id
exercises/*.yaml      generator config per exercise id (server-generated + server-graded)
figures/*.yaml        lesson figure specs embedded via ::figure{id=…}           (courses with figures only)
figure-coupling.yaml  which lesson numbers approximate which figure's values  (courses with figures only)
glossary.yaml         the term list: one or two sentences per term, plus its origin lesson
glossary-links.*.txt  GENERATED, reviewed, frozen: every term occurrence the annotator marks, per locale
lesson-refs.*.txt     GENERATED, reviewed, frozen: every mXX / mXX-lN mention in lesson prose and the
                      module/lesson it links to, per locale — zero dangling, asserted in suite
```

## Lesson markdown

GFM plus exactly three **block** directives: `:::note{type=info|warning|tip}` … `:::` for a callout,
`::figure{id=…}` and `::exercise{id=…}` on their own line. Many lessons carry no figure; exactly one
carries no `::exercise` either — `m35-l1`, the epilogue — and that absence is declared in the lesson's
own prose and in the manifest rather than left to be noticed. There is no inline `:name` dialect — it is
deleted in `frontend/src/lib/directives.ts` — so prose may write a colon followed by anything (`03:00`,
`3:1`, `R:R`) and every surface prints it whole. A colon in prose was NOT always safe: the inline
dialect used to eat `:00`, and the fix is a parser one, so nothing here needs escaping.

### The app can render exactly these blocks, and the export enforces it

The native Android app reads lessons from a bundle, not from this backend, and it has a renderer for a
**closed** list of block kinds: h1-h3, paragraphs, bold, italic, inline code, bullet and numbered
lists, blockquotes, GFM tables (with column alignment), the three callout tones, the two slots, and the
annotator's glossary and lesson-reference marks. Anything else renders as *nothing* — a hole in the
page, with no error anywhere.

So `backend/scripts/export_bundle.py` refuses to write a bundle containing another kind, naming the
lesson and the node. In practice that means: **no fenced code blocks, no images, no links, no hard line
breaks, no horizontal rules, no raw HTML, no strikethrough, no footnotes, and no `####`.** None of them
appears in the course today, which is why the list is closed rather than aspirational; if a lesson needs
one, the app needs a renderer for it first. See `phase-w2-bundle-and-contracts.md`.

## The glossary

`glossary.yaml` **refers, it does not teach.** Every entry distils the lesson that teaches the term
into one or two sentences and points back at it; anything longer belongs in the lesson. Glossary ids
join the same permanent namespace as everything else in the course (`g-funding`, `g-premium`), and
the loader rejects a collision.

Three shapes: a plain `definition`; `senses` for a term the course genuinely uses in more than one
sense (`premium` has three), optionally under a lead `definition` for the "one mechanic, several
instruments" case (`absorption`); and `alias_of` for a second name the course uses for something it
already defines (`CHoCH` → `change of character`, `liquidity grab` → `sweep`), which defers the
definition rather than repeating it.

The hard rule is that **the glossary never coins**: startup fails if a term does not appear in the
prose of its own locale. So a term is added to the glossary only after the prose uses it — and where
the two locales disagreed on a term, the prose was unified first (see the canonical forms in
`GLOSSARY-PROPOSAL.md` at the repo root).

### Linking the prose into the glossary

An entry may carry three optional keys that decide which occurrences of the term in lesson prose
become a link (a tooltip in the app, an internal jump in the PDF). All three take either one value
for both locales or one per locale, because the two languages meet different homonyms:

```yaml
  match:                     # the surface forms to look for. Default: the term + a naive plural.
    en: [longs, go long]     # "a lo largo de" and "a long wick" are not the position.
    es: [largos, en largo]
  link: {es: false}          # this term is never linked in ES ("base" is "base de datos" everywhere)
  link_except: [m02-l1]      # …or only in these lessons ("smart contracts" is not the contract)
```

`origin` and `link_except` name lessons by their permanent **key**, not their display id (identical
for anything created after the 2026-08-10 renumbering; the registry renders keys as display ids).

**The two exclusions are not the same thing.** A term is never marked in its own **origin** lesson —
and that occurrence still *spends* the term's one slot in the book, which is why a term the course
first uses inside the lesson that teaches it carries no PDF link anywhere (correct: the reader met it
where it is explained). A `link_except` lesson is the opposite: there the word is a **false friend**,
so it is not an occurrence at all and the next real one is still linked.

`glossary-links.<locale>.txt` is the record of every decision that produces — one line per marked
occurrence, in course reading order, with `W` for a web tooltip and `WP` for one the book links too.
**It is generated, reviewed by hand, and then frozen**: any content change that moves, adds or drops
a link shows up as a diff there, which is where a false positive gets caught before a reader sees it.
Regenerate with:

```
cd frontend && UPDATE_GLOSSARY_LINKS=1 npx vitest run src/lib/glossary/report.test.ts
```

and read the diff. Never hand-edit the file: fix the prose, or the entry's `match`/`link`/
`link_except`, and regenerate.

### Lesson cross-references in prose

Prose that names another module or lesson by id (`m22`, `m19-l2`) becomes a link on both surfaces —
a titled navigation link in the app, an internal jump in the PDF — detected by the same annotator
that marks glossary terms and resolved in one place (`frontend/src/lib/refs/registry.ts`): a lesson
mention to that lesson, a module mention to the module page, or straight to its only lesson when the
module has just one. A mention of the page it sits on stays plain text. Editorially, the FIRST
mention of another module within a lesson carries the module's short topic as an apposition in the
prose ("m22, la gestión del riesgo") unless the sentence already names what the reference teaches —
that apposition is the affordance the printed book gets, where there is no hover.

`lesson-refs.<locale>.txt` records every mention (source lesson and target both by permanent key),
under the same generated-reviewed-frozen discipline as the glossary links. Its suite asserts there
are **zero dangling references** and that the two locales carry the same references mention for
mention. Regenerate with:

```
cd frontend && UPDATE_LESSON_REFS=1 npx vitest run src/lib/refs/report.test.ts
```

The manifest's root is a single **course**; its blocks follow at the top level:

```yaml
course:
  id: crypto-futures          # the slug: permanent, and the name of this directory
  title: {en: …, es: …}       # one value per language the course declares, no more, no fewer
  subtitle: {en: …, es: …}
  description: {en: …, es: …}
  languages: [en, es]         # [es] for a Spanish-only course; the first is the fallback
  status: published           # draft: loaded and checked, never served to users
  exercise_types: [quiz, calculation, synthetic_chart, pattern_chart]
```

Every localized text in the course — manifest, exercises, figures, glossary — must carry exactly the
declared languages. A Spanish-only course has no `en/` tree, and the loader rejects an English string
left in it. Its ES/EN parity checks simply do not apply. A course without figures (the oposiciones
courses are multiple-choice only) has no `figures/`, no `figure-coupling.yaml` and no `figures.tsv`,
and the loader rejects one that carries them. `subtitle` is the book's short name: the cover, the app header and the PDF's document properties
print the full title, and the PDF's running footer prints the subtitle, which fits on one line.

## ID convention (read before adding content)

**Content IDs are unique inside their course** — another course may use `m01`, `m01-l1` or
`g-funding` for something else. The manifest validator rejects any duplicate id at any level inside a
course (course, block, module, lesson, exercise), and figure and glossary ids share that course's
namespace. Since 2026-08-10 every module, lesson, exercise and figure also carries a permanent
**`key`** in that same namespace — and it is the key, not the id, that reconciliation,
progress/attempts data, print seeds and glossary origins hang off. The database keys every row by
`(course, key)`.

Rules:

- **`key` is the permanent identity: chosen once at creation, NEVER renamed.** It defaults to the id
  (so most entries never write it), and a new entity SHOULD get a human-chosen semantic slug
  (`validation`, `carry`, `multi-timeframe`) so it never tempts anyone to "fix" it. Everything durable
  hangs off it: `print_seed`, the DB skeleton and all learner progress, exam-result blobs, glossary
  `origin`/`link_except` (which store lesson keys, rendered as display ids), and the
  `glossary-links.*.txt` goldens' lesson column.
- **Ids are display labels, permanent again from here on.** Display order is list position, and since
  the 2026-08-10 renumbering id order == display order. Keep it that way: new content APPENDS to its
  block (or as a new block) and takes the next free number; if a future module's position is ever
  load-bearing enough to break numeric order, say why in the manifest — the key layer means no data
  moves either way, but the badge cost is real and the comment is the price.
- **A key belongs to its course forever** — never reuse one for something else inside that course.
- **A new course starts its own namespace** at `block-a`, `m01`, `m01-l1`, `m01-ex-1`, `g-…`; no
  prefix is needed, because every reference to a module, lesson, term or figure implies its course.
- The course slug itself is unique across the repository (it is a directory name) and is permanent.
- The id-versus-position licence still covers ids out of sequence *inside* a lesson (`m19-ex-4`, with
  the reason on file in the manifest).

### The 2026-08-10 renumbering (one-time, deliberate)

The original rule was "ids are never renumbered", and it produced badges reading `M22 → M33 → M23`
after the mid-block insertions of m31–m34. On 2026-08-10 the ids were renumbered ONCE so that id
order equals reading order — also fixing two dependency bugs the old display order had (old `m34-l2`
pointed *forward* at tokenomics as taught, and old `m33` leaned on m23/m24 before the reader met
them; both now sit after their dependencies). Every renumbered entity's old id lives on as its `key`,
so every seed, every printed exercise instance and every learner's progress survived unchanged. The
full module map (lessons, exercises and `fig-*` ids followed their module):

| old | new | | old | new | | old | new | | old | new |
|-----|-----|-|-----|-----|-|-----|-----|-|-----|-----|
| m31 | m15 | | m17 | m19 | | m20 | m23 | | m24 | m27 | 
| m32 | m16 | | m18 | m20 | | m21 | m24 | | m33 | m28 |
| m15 | m17 | | m34 | m21 | | m22 | m25 | | m25 | m29 |
| m16 | m18 | | m19 | m22 | | m23 | m26 | | m26 | m30 |

…and m27→m31, m28→m32, m29→m33, m30→m34. This was the LAST renumbering: the `key` layer exists so a
future reorder is a pure display change, and ids are permanent from here on regardless.

### Ids are unique per course (since 2026-10-04)

Until a second course existed the rule was "ids are globally unique, and a second course
self-namespaces (`spot-m01`)". The multi-course platform (Curset) reversed it: a course is a complete,
independent unit, and its authors should not have to prefix every id. The cost was paid once, in
migration `c3d4e5f6a7b8`: every skeleton table's primary key became `(course_id, id)`, and
`attempts`, `lesson_completions` and `exam_sessions` carry their course. The existing rows all
belonged to `crypto-futures` and kept their keys, so no seed, printed instance or learner's progress
moved.

### What a second course would touch

The API is already course-scoped (`/api/courses/{course}/…`, see the root README), so URLs are not in
the way. What is still single-course:

- **This directory.** Today `course.yaml`, `glossary.yaml` and `es/`/`en/` sit at the top; a second
  course means `content/courses/{slug}/…` with today's tree moving under `crypto-futures/`.
- **`load_registry(dir) -> CourseRegistry`** becomes `load_registries(dir) -> dict[slug, CourseRegistry]`.
- **Three spots in app state**: `app.state.registry` (→ keyed by slug), the print cache keyed by
  locale (→ by course + locale), and `reconcile(app.state.registry.manifest, …)` (→ per course).
- **`current_course`** stops resolving an absent slug to "the only course", which is the moment the
  deprecated unscoped aliases must be removed rather than merely discouraged.

Both the API and the SPA are already course-scoped (`/api/courses/{course}/…` and
`/courses/{course}/…`), so a bookmarked lesson survives the arrival of a second course. What is
deliberately **not** built yet is a course catalog or switcher, and the SPA declares its routes with
the literal slug rather than a `:course` param — the UI stays single-course until a second course
actually exists. This document plus the root `course` entity and the `courses` table are
the structural groundwork so that day is additive, not a migration of ids.

## Worked numbers next to a figure

Where a lesson teaches with worked numbers beside a generated figure, **the figure is the source of
truth.** Figures keep their frozen seeds and exact generated prices; the prose quotes rounded,
human-readable approximations of those values ("cerca de 25.900" for a level drawn at 25911.85),
introduced as approximations (*cerca de*, *en torno a*, `~`). Any arithmetic the prose performs on
them — widths, distances, ratios — is recomputed from the adapted numbers, and `es/` and `en/` always
adapt together in the same change.

Two escape hatches, both deliberate:

- **Exception figures.** Where the prose's own numbers *are* the teaching — a ratio, a sizing chain
  chosen to divide cleanly, a separation the figure exaggerates on purpose — the prose keeps them and
  gains a lead-in **before** the figure telling the reader it is a generated instance carrying its own
  prices.
- **Panels that share a seed.** When a two-panel figure exists to say "identical chart, one
  difference" (m08's breakout vs fakeout, m14's volume read, m19's OI read), both panels run the *same*
  seed, so the comparison is literally true rather than merely suggestive. The duplicate-level-price
  test exempts panels within one figure precisely for this.

`figure-coupling.yaml` declares every coupled number and every exception, and
`backend/tests/test_figure_prose_coupling.py` enforces both directions of the deal: a figure that
moves fails the test with the list of lessons needing a prose pass, and prose edited away from its
figure fails it too. **Reseeding a coupled figure, or changing an injector that feeds one, means
re-running the worked-number pass for the lessons the manifest names** — the test will not let that
step be skipped.

Coupling also crosses lessons: where one lesson *reuses* another's worked numbers by name (m04-l1
quotes m06-l1's entry, 10× liquidation and cascade wick), `backend/tests/test_cross_lesson_numbers.py`
derives the reused values from the same coupled anchors and demands both lessons print them — so a
re-anchor of the source lesson fails naming the borrower, instead of quietly stranding it (which is
exactly what the 2026-08-02 pass did to m04 until 2026-08-10).

### Doc comments on the code behind all this

The house rule is **one line** — Python docstrings and TS `/** */` alike, no `Args:`/`@param` block
restating a signature, no design history (git has that), with one extra clause allowed when a real
trap would cause a bug if forgotten. That is the rule for functions, classes and methods, and it is
what the code does. **Module** headers are the standing exception, and the exception is earned rather
than granted: a `patterns/*.py` injector opens with several paragraphs because that header IS the
injector's contract — which lesson it serves, the label families an exercise may ask for, the negative
control that makes the question falsifiable, what is generated versus derived from it, and which way
the geometry mirrors — and that narrative has nowhere else to live, since the manifest only names ids
and the tests only assert consequences. The same licence covers a module in `content/` that owns a
cross-cutting invariant (`numbers.py`, `print_export.py`). Everything below module level stays one
line unless it is recording a trap: `patterns/base.py`'s `Diagonal`, `diagonals.py`'s
`clamp_close_inside` and `multi_timeframe.py`'s `aggregate` are what "a trap worth a clause" looks
like in practice, and they are the shape to copy — not the length.

## Exercise numbers: friendly by design (the mental-cost guard)

Calculation exercises draw random parameters, so the digits a learner meets are a property of the
GRID, not of any instance — and since 2026-08-22 the grids are co-designed so that **every drawable
combination** lands every solver-visible value (intermediates and final) at mental cost:
multiplicative results terminate at ≤1 decimal (≤2 below 10) and fit — themselves or their double —
in 3 significant digits; additive steps only need alignment. The same guard demands that all three
named-mistake distractors survive dedupe on every draw (a collapsed one used to ship as a generic
"arithmetic slip" filler) and that options stay ≥4 display quanta apart.

`backend/tests/test_mental_cost.py` enforces all of it over the full parameter space of every
calculation exercise. When adding or editing one: pick step sizes and rate choices **jointly** (round
inputs alone do not qualify — 60.000 × a 0,005% rate is still ugly), run the guard, and adjust the
grid until it is green. The structurally-heavy trio (m23-ex-5 and quiz variants m23-ex-2
`three-bills`, m24-ex-4 `slippage-worked`) is exempted BY NAME in the test with its flag note — an
exemption that stops matching real content fails the suite.

### Numbers follow the locale's own conventions

Every number in a locale's text is written the way that locale writes numbers: `60,300` / `0.1 BTC` /
`3.7R` in `en/`, `60.300` / `0,1 BTC` / `3,7R` in `es/` — in lesson prose AND in `exercises/*.yaml`,
whose per-locale strings you write by hand (the figure-coupling test only formats the numbers it
anchors). The 2026-08-22 correctness pass found m27's EN prose and its four EN exercise texts written
in Spanish conventions and converted them; a change there shows up as context-snippet churn in
`glossary-links.en.txt` / `lesson-refs.en.txt`, which is expected and reviewed, never a moved link.

Two numbers must also agree ACROSS locales: the same facts, and the same count of them. An ES option
that quietly drops a figure its EN twin states (m30-ex-3's `800`) leaves the two readers with
different evidence for the same keyed answer.

#### GENERATED numbers are formatted for you (2026-08-22)

The rule above is about text you type. Numbers a generator *substitutes* — a calculation prompt's
`{notional}`, its option labels, its worked solution — used to print raw Python in both books
(`70000 USDT`, `0.0005`, `35.00` inside Spanish prose). They now go through one formatter,
`backend/src/tradeschool/content/numbers.py`, which the app, the PDF and the answer key all read
downstream of; nothing formats a number in TypeScript. So when authoring a calculation:

* **Write the prompt around the substitution, not around a shape.** `{notional}` arrives as `70,000`
  or `70.000` already. Never pre-format inside the template, and never add your own separators.
* **State rates as rates.** A parameter listed in its formula's `percent_args` is *held* as a fraction
  (`0.0005` — what the arithmetic multiplies by) and *stated* as a percentage (`0.05%` — what an
  exchange shows). The prompt sentence must read correctly with a percentage in the slot: "the taker
  fee is **{fee_rate}**" gives "the taker fee is 0.02%", and in ES the article has to follow ("es
  **del** {fee_rate}"). Which args are rates is declared on the FORMULA in `formulas.py`, not in the
  YAML, so a prompt cannot drift from the units its own arithmetic uses.
* **ES percent spacing is `0,05%`, not `0,05 %`.** Split house convention, settled 2026-08-22 on the
  lessons this layer quizzes against: m04-l1, m19-l1, m21-l1, m22-l1 and m21-ex-1 all print no space.
  m07-l1, m23-l1 and m32-l1 use one and were left alone — they are authored prose, not generated.
* `win_rate` (m25) is deliberately NOT a percentage: both prompts define it as "the fraction of trades
  that end in profit". Recorded in `test_exercise_numbers.py` so a later sweep re-decides it rather
  than assuming it was an oversight.

`backend/tests/test_exercise_numbers.py` holds the layer: no generated string carries the other
locale's number form, the answer key quotes a label the option list actually shows, and every rate
reaches the prompt as a percentage with the worked solution converting it back exactly once.

#### …and so is the prose hung off them (2026-08-22)

Localizing the numbers left an ES worked solution ending on `= 0,6 units` and `= 35 (you pay)`. The
prose a step hangs off its formula — a unit on the result, a verdict in parentheses, a closing
sentence about what the number does *not* tell you — now comes from `LocalizedText` constants in
`formulas.py`, collected in `LOCALIZED_PROSE`. Adding a new one is a two-language constant or it
does not compile into a phrase at all, which is the failure mode the sibling `MISTAKE_TRANSLATIONS_ES`
table (English-keyed, silent English fallback) still has — its one gap, m23-ex-5's `charge the taker
fee on one fill instead of both`, was found and filled in the same pass and is now guarded.

**What stays English on purpose:** the formula skeleton's *identifiers* (`funding`, `notional`,
`gross`, `taker buy volume`) and the glosses inside an expression (`(price move)`, `(distance from
entry to stop)`, `round-trips`). Those are the **formula reminder's** vocabulary, and it already
renders them in Spanish (`bruto = cantidad × (var. precio)`) — so an ES learner currently reads a
Spanish reminder above an English-skeleton solution. Closing that is one decision about identifiers
across every line of every `explain`, not a phrase sweep; half-translating an expression line
(`cost = fee×notional×2 × idas y vueltas`) reads worse than either end of it. Flagged, not done.

### `tolerance` is retired (2026-08-24, one-time)

Every calculation YAML but one used to declare `tolerance: { rel: … }` or `{ abs: … }` — how close a
free-typed answer had to be to count as correct. That input mode is gone: `calculation` has graded by
CHOICE for a long time (four shuffled options, three of them named mistakes), so the field was
validated on load and then never read by anything. It has been removed from the schema and from the
17 YAMLs that carried it.

Removed rather than kept as a statement of intent, for two reasons: a schema field nothing reads
invites the belief that it does something, and the Android port would otherwise have copied it into
the exercise bundle. Nothing about grading changed — there was nothing to change.

If free numeric input ever returns, its tolerance belongs beside that input's own contract, with a
test in the same commit. Until then `RETIRED_EXERCISE_FIELDS` in
`backend/tests/test_generators.py` asserts both halves of the retirement: the schema rejects the
field, and no `content/exercises/*.yaml` still ships it. The reasoning also sits beside the schema it
left, in `backend/src/tradeschool/exercises/calculation.py`.
