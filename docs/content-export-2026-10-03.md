# Content export — 2026-10-03 (run 2026-10-04)

**Outcome: exported.** The bundle (format 2) is in `dist/bundle/`, with fingerprint
**`7a9fae8205c6503c9685e467bf56307b5c7711081ff8ae86af454bc70bd7d633`**. The answer-label and
chart-label catalogs are in `dist/i18n/` (section 7). The contracts in `dist/contracts/` were
regenerated and are byte-identical to round 7.

The first run of this session stopped at the suite: two lessons had broken lists. With authorisation,
the breaks were fixed with markers and whitespace only, and a committed check now catches that class
(section 2.2). Then the full suite ran green and the export went ahead. A follow-up aligned EN m09-l2's
body with its summary and re-exported (section 2.4). A second follow-up fixed a decimal comma in EN
m27-l1, added the label catalogs to the export and re-exported (section 2.5).

- Tree: HEAD `bdc11d0` ("bundle prepared", which holds the list repair, the new check and the reports),
  plus the uncommitted EN m09-l2 change listed in section 6.4.
- Baseline: `eecbf11` ("Round 7 of improvements"). It is the last commit whose handoff records a bundle
  export (`docs/content-round-7-handoff.md`, fingerprint `9e7facd5f0a3502d…`). A copy of that export
  was taken before anything was overwritten, and every comparison below is against it.

---

## 1. What changed since the last export (`eecbf11` → now)

### Lesson files

All 44 lessons changed in **both** locales: `content/{en,es}/lessons/*.md`, m01-l1 … m35-l1, every
file. Most of it is prose pass 1.2 (`fbe5735`, `5bdb083`, `0b3f02c`, `f4937e1`, `e160d34`, `ac227fb`,
`e8e9f26`). This session adds the list repair in m22-l1 and m23-l1, both locales (section 2.1). **No
lesson file was touched in one locale only.**

### `course.yaml`

44 field changes. Lesson ids are display ids, with the permanent key in brackets where it differs.

| Entity | Field | Locales |
| --- | --- | --- |
| m05-l1, m08-l1, m08-l2, m11-l1, m12-l1 | summary | en + es |
| m15-l2 [m31-l2], m16-l1 [m32-l1], m18-l1 [m16-l1], m19-l1 [m17-l1], m19-l2 [m17-l2] | summary | en + es |
| m22-l2 [m19-l2], m23-l2 [m20-l2], m26-l1 [m23-l1], m30-l1 [m26-l1], m34-l1 [m30-l1] | summary | en + es |
| module m16 [m32], module m18 [m16], module m34 [m30] | summary | en + es |
| module m34 [m30], lesson m34-l1 [m30-l1] | title | en + es |
| **m09-l2** | summary | **en only** |
| **m21-l1 [m34-l1]** | summary | **es only** |
| **m27-l1 [m24-l1]** | summary | **es only** |
| **module m27 [m24]** | summary | **es only** |

### The four one-locale summary changes

None was changed in this session.

| Summary | Commit | Change | Ledger entry | Why one locale only | Other locale needs it? |
| --- | --- | --- | --- | --- | --- |
| m09-l2, EN | `ba3bd5c` | "a stab below support" → "a brief dip below support" | `prose-pass-ledger.md:3472` (final step, session 6: "the m09 lesson summary, EN…"); the decision itself is at `:64` («estocada» / "stab" → «caída breve» / "brief dip") | the ES summary never had «estocada». It says «pinchazo», the word its own lesson uses (`es/m09-l2.md:20, 58, 132`) | **ES: no.** The EN lesson body still said "stab" four times, against its own summary. **Resolved by your decision: the body now follows the summary** (section 2.4) |
| m21-l1, ES | `0b3f02c` | «un carry concurrido» → «un carry saturado» | `prose-pass-ledger.md:1985`: "«carry concurrido» → «carry saturado» (body and summary). EN "crowded carry" stays, because it is the standard English term" | «concurrido» was a coined ES term (decisions table, `:221`); "crowded" is standard EN | **No** |
| m27-l1, ES | `fbe5735` (pilot) | «un freno diario fijado» → «un límite de pérdida diaria fijado» | `prose-pilot-ledger.md:14` | «freno diario» was a coined ES term; EN "daily stop" is the standard term and `g-daily-stop`'s EN form (`prose-pilot-ledger.md:13`) | **No** |
| module m27, ES | `fbe5735` | «el freno diario que termina…» → «el límite de pérdida diaria que termina…» | `prose-pass-ledger.md:262` | same as m27-l1 | **No** |

### Other inputs changed in the same range

These are not lesson text. They are why more of the bundle moved than the brief expected (section 3).

- `content/glossary.yaml`: `g-overrun` removed, `g-origin-zone` → `g-order-block` (alias deleted),
  definition rewording. Terms 256 → 254.
- 49 exercise YAMLs and 10 figure YAMLs: the coined-term replacements of `ba3bd5c` (prompts, options,
  explanations, captions).
- `content/figure-coupling.yaml` (`fbe5735`).
- `content/glossary-links.{en,es}.txt` and `content/lesson-refs.{en,es}.txt` were regenerated with the
  prose, and again in this session (section 2.1).
- `content/README.md`: the alias example. It is not an export input.

---

## 2. Suite results

### 2.1 The two list breaks, found and fixed

The first run found both breaks. Both came in with `0b3f02c` ("Prose improvement l17 to l24"). At
`5bdb083` both lists were intact. Neither was caught by any committed check: the bundle's block diff
compares the bundle with the page the web renders, and both carried the same damage. That is blind
spot 2 in `verification-blind-spots.md`.

| Lesson | Locale | Where (before the fix) | What the reader saw | Fix |
| --- | --- | --- | --- | --- |
| m23-l1 | ES | `es/m23-l1.md:165` | `…antes de que actúes. 2.` closed item 1's paragraph, and item 2 (line 166) ran on as part of item 1 | `2. ` back at the start of its own line |
| m23-l1 | EN | `en/m23-l1.md:152` | `…before you act on it. 2. **Know which session…**` inside item 1 | the same |
| m22-l1 | EN | `en/m22-l1.md:106, 108` | `…\`mmr = 0.5%\`: - At 5×: …` and `…this trade. - At 20×: …` as running text | the two nested `  - ` sub-items restored, as at `eecbf11` |
| m22-l1 | ES | `es/m22-l1.md:117, 119` | `…\`mmr = 0,5%\`: - A 5×: …` and `…operación. - A 20×: …` | the same |

The fix is markers and whitespace only. For each of the four files, the whitespace-split token sequence
is **identical** to HEAD, so every word, number and markup token is unchanged and in the same order. In
m23-l1, item 1 also lost its stray leading space, and the continuation lines of both items got the
3-space indent they had at `eecbf11`.

Effects of the fix:
- The bundle's prose token counts drop by exactly 3 per locale (EN 71393 → 71390, ES 78095 → 78092).
  Those are the stray `2.`, `-` and `-`, which are list markers again rather than words.
- The AST list counts are back to round 7 in both lessons and both locales.
- The bold rule in m23-l1 is a lead-in again, so the emphasis-rule hit is gone.

The four report goldens were regenerated:
- `UPDATE_GLOSSARY_LINKS=1 npx vitest run src/lib/glossary/report.test.ts`
- `UPDATE_LESSON_REFS=1 npx vitest run src/lib/refs/report.test.ts`

Every (lesson, term) and (lesson, target) row is **identical to HEAD**. Only the quoted context moved,
on one line per file:
- `glossary-links.*.txt`: m20-l1 `g-confirmation`, where the quote no longer ends in the stray "2.";
- `lesson-refs.*.txt`: m19-l1 → m06, where the quote no longer runs into ": - At 5×:".

### 2.2 The new check

`frontend/src/lib/refs/listShape.ts` and `listShape.test.ts` sit beside the cross-reference check, so
`npm test` and CI run them. They parse each lesson with the same remark processor `refs/report.ts` uses
and assert two things:

- **Parity, per lesson:** ES and EN have the same count of list items, nested list items and numbered
  items.
- **No stray marker, per locale:** no `N.`, `-` or `*` right after a sentence end (`.`, `:`, `;`,
  `!`, `?`, `»`, `”`, `"`, `)`) in a prose text node. Code spans are not text nodes, so a formula like
  `a - b` is never matched. A failure names `lesson:line`, the marker and its context.

Unit cases cover the two real damage shapes (trimmed from m23-l1 and m22-l1) and two non-hits (a
hyphen in a code span, a number ending a sentence).

**Shown red first.** With the four lessons put back to HEAD, the check failed on exactly the six spots
above, and on nothing else:

```
m22-l1:106 «-» …: - At 5×: …                      m22-l1:117 «-» …: - A 5×: …
m22-l1:108 «-» …irrelevant to this trade. - At 20×: …   m22-l1:119 «-» …para esta operación. - A 20×: …
m23-l1:152 «2.» …before you act on it. 2. …         m23-l1:165 «2.» …antes de que actúes. 2. …
Tests  2 failed | 48 passed (50)
```

The parity half stayed green on the broken tree, because both locales broke the same way. The
stray-marker half is what catches this class. **Over all 44 lessons after the fix: 50 / 50 pass, and no
other hit.** `tsc -b` is clean. The project has no ESLint config.

The root `README.md` gained one paragraph about this guard, next to the lesson-refs golden.

### 2.3 Results on the final tree

| Check | Result |
| --- | --- |
| backend `pytest` (whole suite, Docker up) | **1300 passed, 20 skipped**, exit 0. Rerun after the m09-l2 follow-up: **1300 passed, 20 skipped** again |
| frontend `vitest run` (whole suite) | **508 passed, 1 skipped** (`src/lib/pdf/emit.test.ts`, opt-in), exit 0. That is round 7's 458 plus the 50 new list-shape cases. Rerun after the m09-l2 follow-up: the same |
| glossary-link report test | pass, both locales |
| cross-reference check (`lib/refs/report.test.ts`) | pass, both locales: 228 references each, 0 dangling, no self-links, locale parity |
| list structure (`lib/refs/listShape.test.ts`) | pass: 44 lessons in parity, 0 stray markers in either locale |
| figure/prose coupling (`test_figure_prose_coupling.py`) | pass (inside pytest) |
| `export_bundle.py --verify-only` (on `dist/bundle`) | **exit 0**: text diff 0 (prose and glossary multisets, all 88 lessons block for block), block inventory OK (88 ASTs), exercise refs OK (242 marks), fingerprint `109ff2c3…` verified against 98 files. After the m09-l2 follow-up: fingerprint `a49624d8…`, exit 0 again |
| `verify_golden_stability.py` | **exit 0**: 90 committed fingerprints hold (84 golden + 6 pinned). Digest `f0ae701b30569a03…`; see the note below |
| glossary-term presence ((lesson, term) pairs vs `eecbf11`) | moved; every move is explained in the table below. Identical to HEAD |
| lead-in / emphasis rules (round-5 classifier, re-run) | pass: ES 491 and EN 496 bold spans, the same totals as round 5. No lesson gained a bold span that is neither a lead-in nor its kept emphasis. The other differences from `eecbf11` are wording inside existing spans |

### Glossary-term presence: (lesson, term) pairs vs `eecbf11`

The lesson column is the lesson **key**. Every move is recorded in `docs/prose-pass-ledger.md` or
`docs/prose-pilot-ledger.md`. None is from this session.

| Locale | Change | Cause |
| --- | --- | --- |
| en | − m08-l1 `g-overrun` | entry removed by decision (ledger, "Outside lessons") |
| en + es | + m17-l1 `g-cascade`, + m17-l1 `g-liquidation` | new wording in m19-l1 (display id) |
| en | + m31-l1 `g-stop-loss` | "stop cluster" in m15-l1 (display id) |
| en | + m32-l1 `g-liquidation-price`; en + es − m32-l1 `g-liquidity` | m16-l1 (display id) rewording |
| en | + m34-l1 `g-leverage` | "leverage-mania" lost its hyphen in m21-l1 (display id) |
| es | + m23-l1 `g-daily-stop` | pilot: the ES term became «límite de pérdida diaria» |
| en + es | m11-l1 `g-sideways-market` W → WP | PDF policy only (first occurrence in the book). The origin lesson m10-l1 (EN) dropped "sideways market", so it no longer claims the book-wide slot. The web/app mark is unchanged |
| es | m16-l1 `g-listing` W → WP | the same: the earlier «listado» in the m17-l1 file was reworded |

EN: 1117 → 1120 rows. ES: 1053 → 1055 rows. The lesson-ref (lesson, target) pairs are identical to
`eecbf11` in both locales (228 / 228).

### Note on the generation digest

Round 7 recorded `6999679392b682a2…`. This machine prints `f0ae701b…`, and it prints the same value
over the `eecbf11` content tree (`CONTENT_DIR=<git archive eecbf11 content>`). So no content edit
moved it. The difference is environmental: Python 3.14.7, numpy 2.5.1, SIMD X86_V3. The 90 committed
pins hold, and that is what the exit code certifies. The digest is not committed anywhere.

### 2.4 Follow-up: EN m09-l2 aligned with its summary

The decision was «estocada» / "stab" → «caída breve» / "brief dip" (`prose-pass-ledger.md:64`). It
reached the EN m09-l2 summary in `ba3bd5c`, but not the EN lesson body. On instruction, the body now
follows the summary. ES is unchanged: its lesson and its summary both use «pinchazo».

| Line | Before | After |
| --- | --- | --- |
| `en/m09-l2.md:20` | …the churn, the stab below support that recovers… | …the churn, the brief dip below support that recovers… |
| `en/m09-l2.md:55` | price stabs *below* support | price dips *below* support (the next sentence already says it snaps back within three or four candles) |
| `en/m09-l2.md:57` | That stab-and-recovery is the spring | That dip-and-recovery is the spring (the brevity is stated just before) |
| `en/m09-l2.md:122` | A stab below support that keeps falling… | A brief dip below support that keeps falling… (the summary's own wording) |

Every other word is untouched. "a brief dip below support" is the form m29-l1 and m30-l1 already use.

Checks after the change:
- "dip" is not a glossary match form, and no guard phrase or coupling note quotes "stab".
- The four reports were regenerated and are **byte-identical**: no mark or reference sits near these
  words.
- The list check passes 50 / 50.
- Vitest: 508 passed, 1 skipped. Pytest: 1300 passed, 20 skipped.

Re-export:
- **Only `ast/en/m09-l2.json` moved**, and the fingerprint went from `109ff2c3…` to **`a49624d8…`**.
- EN prose tokens rose by exactly 2 (71390 → 71392), the two added "brief".
- reading-seconds.json and every other manifest field are unchanged.

Out of scope and left as they are: four plain-verb uses of "stab" for price action elsewhere —
`en/m04-l1.md:55` ("stabbed straight through the level"), `en/m04-l1.md:107`, `en/m06-l1.md:122`, and
the matching `exercises/m04-ex-3.yaml:193`. They describe a candle moving through a price, not the
spring.

### 2.5 Follow-up: EN m27-l1 decimal, and the label catalogs

The Android import showed five label entries per locale out of date: m34 exercise 1, m08 exercise 5
(ES), the m34 figure and the ES "shelf" level. The app's `ExerciseStrings.kt` and `ChartStrings.kt`
are hand copies of the web's i18n files, which changed in the same export. The web's i18n text was
already right and is unchanged. The fix on this side is to export those entries, so the app can import
them instead of keeping copies (section 7). The stale copies are fixed in the Android repo.

| Line | Before | After |
| --- | --- | --- |
| `en/m27-l1.md:48` | it is the 0,618 retracement of the last leg | it is the 0.618 retracement of the last leg |

The other comma-grouped numbers in EN lessons (`60,000`, `30,500`, …) are thousands separators and stay.

Re-export:
- **Only `ast/en/m27-l1.json` moved in the bundle**, with `manifest.json` (its hash and the
  fingerprint). The fingerprint went from `a49624d8…` to **`7a9fae82…`**. The token counts did not
  change (EN prose 71392): "0,618" and "0.618" are one token each.
- New, outside the bundle: the four files in `dist/i18n/`.
- `--verify-only`: exit 0, text diff 0, 88 ASTs, 242 marks, the fingerprint verified against 98 files,
  and the label catalogs match the i18n source.

Checks after the change:
- The EN glossary-link golden failed on its first run: two rows quote the m27-l1 sentence (m24-l1
  `g-resistance` and `g-support`, by key). Regenerated with
  `UPDATE_GLOSSARY_LINKS=1 npx vitest run src/lib/glossary/report.test.ts`. Only the quoted context
  moved ("0,618" → "0.618"); every (lesson, term) row is identical. The other three reports did not move.
- Backend `pytest`: **1305 passed, 20 skipped** (1300 before, plus the 5 tests in
  `tests/test_label_catalogs.py`).
- Frontend `vitest run`: **508 passed, 1 skipped**.
- `verify_golden_stability.py`: exit 0.
- `ruff check` and `mypy` are clean on the new and changed backend files.

---

## 3. Bundle per-file comparison (`dist/bundle` vs the round-7 export)

**97 of 98 files moved, plus `manifest.json`. Byte-identical: `error-phrases.json`**, which is built
from code, and no code changed.

**The brief's expectation does not hold for this range, and the reason is known.** The brief expected
only the lesson ASTs, the manifest, the glossary and reading-seconds to move. But the commits since the
last export also changed exercise YAML, figure YAML, `figure-coupling.yaml` and the glossary entries.
So these moved as well, each one tied to its source in section 6.2:
- `exercises/configs.json`
- `exercises/references.json`
- `figures/specs.json`
- `figure-coupling.yaml`
- `ast/index.json` (node census)
- `README.md` (generated; the term count)

**Every AST moved because every lesson changed.** No AST moved for a lesson outside section 1.

**What had to stay byte-identical:**

| Expected identical | Result |
| --- | --- |
| `figures.tsv` | **identical** |
| `exercise-mode.tsv` | **identical** (with `formatter-cases.tsv` and `configs/`: `dist/contracts/generation-goldens/` matches round 7 under `diff -r`) |
| the fingerprints | **hold**: 90 / 90 committed |
| `glossary-links.*.txt` (same terms in the same lessons) | **not identical to round 7.** The prose pass moved 8 EN and 6 ES rows, all explained above. **Identical to HEAD** in every (lesson, term) pair, and this session moved only quoted context |

**Structural comparison of the lesson ASTs with round 7** (node counts per lesson):
- m22-l1 and the list counts of m23-l1 now match round 7 exactly.
- The rest are symmetric paragraph −1 changes in m16-l1, m21-l1, m23-l1, m23-l2 and m35-l1, both
  locales. They are short announcer paragraphs the prose pass removed or folded under the voice rules
  (e.g. "Two rules come out of this." / «De aquí salen dos reglas.», "Here is the half no course-seller
  mentions."). A scan for round-7 blocks that now sit mid-paragraph finds **none**.
- EN m27-l1 has one list fewer, which is a repair. At `eecbf11`, line 124 began with `  + 0.6 × 3.7R…`.
  Markdown read that `+` as a list marker and split an inline code span into a stray list in the round-7
  bundle. The prose-pass rewrap moved the `+` up a line, and the span is whole again.

**Against the pre-fix candidate** (built in the first run), only these moved: `ast/{en,es}/m22-l1.json`,
`ast/{en,es}/m23-l1.json`, `ast/index.json` and `reading-seconds.json`. In reading-seconds, only EN
m23-l1 changed: 725 → 724, one word fewer, because the stray "2." was being counted as a word.

---

## 4. Other Android inputs

From `export_contracts_to_android.py` (`DELIVERED_DIRS`, `REQUIRED_CONTRACT_DIRS`) and the README
section "The Android bundle and the port's contracts":

| Input | Producer | Changed vs round 7? | Regenerated? |
| --- | --- | --- | --- |
| `dist/bundle/` | `export_bundle.py` | yes, see section 3 | **yes** |
| `dist/contracts/generation-goldens/` | `export_generation_goldens.py` | **no**: byte-identical | **yes** |
| `dist/contracts/prng-vectors/` | `export_prng_vectors.py` | **no**: byte-identical (code-only input) | **yes** |
| `dist/contracts/libm-parity/` | `export_libm_parity.py` | **no**: byte-identical (copies committed artifacts) | **yes** |
| `dist/i18n/` (section 7) | `export_bundle.py` | new | **yes** |
| bundle format version | `export_bundle.py` | **no**, still **2**: no shape change, so `bundle-format-changelog.md` needs no entry | n/a |
| `EXPORT_MANIFEST.json` + the copy into the Android repo (`bundle/`, `contracts/`, `i18n/`) | `export_contracts_to_android.py --target …` | n/a | **no**. It is a separate, deliberate transfer into `~/IdeaProjects/tradeschool-android`, and it records whether this repo's tree was dirty (it is, see section 6.4) |

---

## 5. Export path and exact commands

Written to `/home/juanjo/PycharmProjects/tradeschool/dist/` on 2026-10-04 08:37–08:38, from `backend/`:

```bash
uv run python scripts/export_bundle.py                    # -> dist/bundle/ (format 2, fingerprint 7a9fae82…) + dist/i18n/
uv run python scripts/export_bundle.py --verify-only      # exit 0
uv run python scripts/export_generation_goldens.py        # -> dist/contracts/generation-goldens/
uv run python scripts/export_prng_vectors.py              # -> dist/contracts/prng-vectors/
uv run python scripts/export_libm_parity.py               # -> dist/contracts/libm-parity/
uv run python scripts/verify_golden_stability.py          # exit 0, 90/90
```

All six exited 0. The bundle export and `--verify-only` were rerun after the m09-l2 follow-up, and both
exited 0. The contract exporters and the stability script were not rerun: a lesson body is not one of
their inputs, and `dist/contracts/` is still byte-identical to round 7. The bundle export and
`--verify-only` were rerun again after the m27-l1 follow-up (09:45), and both exited 0. The transfer to the app is the next step, and it was not run:
`uv run python scripts/export_contracts_to_android.py --target ~/IdeaProjects/tradeschool-android`.

---

## 6. Completeness check

### 6.1 Source → bundle

Every changed file the export reads, from `git diff --name-only eecbf11` plus this session's working
tree:

| Input | Count | Bundle file that moved | Coverage |
| --- | --- | --- | --- |
| `content/{en,es}/lessons/*.md` | 88 | `ast/{en,es}/<lesson>.json`, `ast/index.json` (node census), `reading-seconds.json` | 88 / 88 ASTs moved; all 88 reading estimates moved |
| `content/course.yaml` | 44 field changes | `manifest.json` | exactly those 44 fields differ in the manifest, plus `contentFingerprint` and `counts.glossaryTerms` (256 → 254). Nothing missing, nothing extra |
| `content/glossary.yaml` | 1 | `glossary/glossary.{en,es}.json`; `README.md` (term count) | moved |
| `content/exercises/*.yaml` | 49 | `exercises/configs.json` | 49 / 49 entries moved, none extra |
| the same | 6 of 49 carry module refs | `exercises/references.json` | m08-ex-7, m16-ex-3, m21-ex-1, m23-ex-9, m34-ex-3, m34-ex-4: offsets moved with the reworded strings. Still 242 marks |
| `content/figures/*.yaml` | 10 | `figures/specs.json` | 10 / 10 specs moved, none extra |
| `content/figure-coupling.yaml` | 1 | `figure-coupling.yaml` (copied verbatim) | moved |
| `content/glossary-links.*.txt`, `content/lesson-refs.*.txt` | 4 | none directly: review goldens that pin the annotator | the AST marks equal them (`ast.test.ts`, green) |
| `content/README.md` | 1 | none: not an export input | n/a |

**Inputs that changed with no bundle file moving: none.**

The 49 exercise YAMLs: m03-ex-4, m04-ex-3, m04-ex-4, m05-ex-3, m05-ex-4, m08-ex-1, m08-ex-3 … m08-ex-7,
m09-ex-4, m09-ex-6, m11-ex-5, m13-ex-4, m14-ex-4, m15-ex-2, m15-ex-3, m15-ex-4, m15-ex-7, m16-ex-3,
m17-ex-3, m17-ex-4, m18-ex-3, m18-ex-4, m19-ex-3 … m19-ex-6, m21-ex-1, m22-ex-4, m22-ex-5, m22-ex-6,
m23-ex-2, m23-ex-3, m23-ex-4, m23-ex-8, m23-ex-9, m25-ex-4, m27-ex-1, m27-ex-3, m27-ex-5, m30-ex-2,
m30-ex-3, m31-ex-1, m32-ex-3, m34-ex-1, m34-ex-3, m34-ex-4.

The 10 figure YAMLs: fig-m03-trend-vs-range, fig-m08-breakout-vs-fakeout, fig-m08-market-structure,
fig-m08-rejection-vs-open-space, fig-m08-reversal-forms, fig-m10-ema-signatures, fig-m15-channel,
fig-m19-liquidity-sweep, fig-m34-imbalance, fig-m34-origin-zone.

### 6.2 Bundle → source

| Bundle file(s) that moved | Source cause |
| --- | --- |
| `ast/{en,es}/*.json` (88) | the 88 lesson files (prose pass; m22-l1 and m23-l1 also this session's list repair; EN m09-l2 also the "stab" alignment) |
| `ast/index.json` | the per-locale node census changed with the lessons |
| `manifest.json` | the 44 `course.yaml` fields, the term count and the fingerprint |
| `glossary/glossary.{en,es}.json` | `glossary.yaml` |
| `exercises/configs.json` | 49 exercise YAMLs |
| `exercises/references.json` | 6 of those YAMLs, as above |
| `figures/specs.json` | 10 figure YAMLs |
| `figure-coupling.yaml` | `content/figure-coupling.yaml` |
| `reading-seconds.json` | the lesson word counts (all 88 values moved) |
| `README.md` (generated) | `counts.glossaryTerms` 256 → 254 |

**Bundle files that moved with no source cause: none.**

### 6.3 Outside the bundle

See section 4. All three contracts directories were regenerated and are byte-identical to round 7. The
format version is still 2, and the changelog needs no entry. The Android repo itself was not touched.

### 6.4 State of the tree

**Not clean.** HEAD is `6fa5a19` ("bundle prepared"), which holds the m09-l2 follow-up. The current
`dist/bundle` (fingerprint `7a9fae82…`) and `dist/i18n/` were exported from `6fa5a19` **plus** these
uncommitted changes:

```
 M README.md                           dist/i18n/ paragraph
 M backend/README.md                   dist/i18n/ in the exporter list
 M backend/scripts/export_bundle.py    writes and verifies dist/i18n/
 M backend/scripts/export_contracts_to_android.py   delivers i18n/ as well
 M backend/tests/test_export_contracts_to_android.py
?? backend/scripts/label_catalogs.py   builds the catalogs
?? backend/tests/test_label_catalogs.py
 M content/en/lessons/m27-l1.md        "0,618" → "0.618" (section 2.5)
 M content/glossary-links.en.txt       the same sentence, quoted in two rows (not an export input)
 M docs/content-export-2026-10-03.md   this file (not an export input)
```

**Fingerprint `7a9fae82…` cannot be reproduced from `6fa5a19`**, which exports `a49624d8…`. Commit
`content/en/lessons/m27-l1.md` exactly as it is to make the export reproducible.
`export_contracts_to_android.py` records a dirty tree and lists its paths, so commit before running the
transfer.

---

## 7. Label catalogs: `dist/i18n/`

`export_bundle.py` writes these beside the bundle, in the same run (`backend/scripts/label_catalogs.py`
builds them):

```
dist/
├── bundle/                       the course (fingerprinted, format 2)
└── i18n/
    ├── exercise-labels.en.json
    ├── exercise-labels.es.json
    ├── chart-labels.en.json
    └── chart-labels.es.json
```

| File | i18n namespaces (`frontend/src/i18n/{en,es}.json`) | Replaces in the app |
| --- | --- | --- |
| `exercise-labels.<locale>.json` | `chartLabel`, `divergence` (58 + 5 = 63 keys) | `ExerciseStrings.kt`'s chart labels and divergences |
| `chart-labels.<locale>.json` | `band`, `candle`, `chartMarker`, `diagonal`, `level`, `overlay` (52 keys) | `ChartStrings.kt`'s maps and candle parts |

Format:
- One JSON object per file: flat `"namespace.key": "text"`, the same dotted path i18next resolves
  (`band.origin`, `chartLabel.zone_respected`). The namespace stays in the key because the same key
  can exist in two namespaces (`band.origin` and `chartMarker.origin` say different things).
- The bundle's one serialization (`canonical_bytes`): keys sorted, no whitespace, UTF-8 unescaped, one
  trailing newline. The same input always gives the same bytes.
- Text is copied verbatim, `{{…}}` placeholders included.
- The two locales of a catalog have the same keys. A key present in only one locale, a missing
  namespace or a non-string value fails the export (exit 2, `BUNDLE EXPORT FAILED`) before anything is
  written.

What it leaves out:
- `exercise.*` UI copy: the app adapts it rather than transcribing it.
- `ChartStrings.kt`'s `openInterestPane`, `cumulativeVolumeDeltaPane`, `expandChart`, `closeChart` and
  `zoomHint`: these have no i18n entry on the web.

The files are **not** in the bundle's manifest or fingerprint. A label change does not move the
fingerprint, so the app must not rely on it to detect one. The transfer's `EXPORT_MANIFEST.json` does
list their digests (below). `--verify-only` checks that `dist/i18n/`
still matches the i18n source.

**Delivery.** `export_contracts_to_android.py` copies `dist/i18n/` with `bundle/` and `contracts/`.
It lands at the Android repo's root, next to the other two:

```
~/IdeaProjects/tradeschool-android/
├── bundle/
├── contracts/
├── i18n/                         exercise-labels.{en,es}.json, chart-labels.{en,es}.json
└── EXPORT_MANIFEST.json          lists every i18n/ file with its sha256; counts.i18n = 4
```

Like the other two directories, `i18n/` is replaced rather than merged, so a catalog an older export
left behind does not survive. A `dist/` with no `i18n/` stops the whole delivery (`DELIVERY REFUSED`),
so the app cannot receive a new bundle beside old labels. The transfer was not run in this session.
