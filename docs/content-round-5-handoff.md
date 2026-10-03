<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# Content round 5 — handoff

Four content fixes ending in one bundle regeneration. **Nothing is committed.** The file list is at the
end.

| Phase | What | Result |
| --- | --- | --- |
| P0 | Baseline | bundle exported before any edit (fingerprint `f38c211e…`), per-file hashes kept |
| P1 | Book-metaphor leftovers | 2 lessons and the m35 manifest entry rewritten in ES and EN; every remaining hit justified below |
| P2 | Glossary coverage audit | `docs/glossary-candidates.md` written; `g-narrative` became two senses; nothing else added |
| P3 | Emphasis cleanup | 1737 spans per locale, every one in `docs/content-round-5-emphasis-ledger.tsv` |
| P4 | Bundle (format 2) and verifiers | all green: bundle `8fa38345…`, goldens zero diff, 90 fingerprints hold, 1300 + 458 tests pass |

---

## P1 — book-metaphor leftovers

The brief's grep was `libro|capítulo|capitulo|página|pagina|lector|manual`, case-insensitive. EN got
the same treatment with `book|chapter|page|reader|manual`.

### What changed

The real book metaphors were in two lessons and in the manifest. Lessons are named by display id.

**m35-l1, the epilogue (ES and EN).** 16 edits per locale. The full before/after texts are in the
appendix so the lesson can be read as a whole.

| # | ES before | ES after | EN before | EN after |
| --- | --- | --- | --- | --- |
| 1 | `# Después de este libro` | `# Después de este curso` | `# After this book` | `# After this course` |
| 2 | El libro se acaba aquí, así que toca decir con precisión qué te llevas, qué no te llevas y qué caminos salen de esta página. … después de cerrarlo. | El curso se acaba aquí. Esta lección dice qué te llevas, qué no te llevas y por dónde seguir. … después de terminarlo. | The book ends here, so it is worth saying precisely what you take with you, what you do not, and which roads lead off this page. … after you close it. | The course ends here. This lesson says what you take with you, what you do not, and where to go next. … after you finish it. |
| 3 | la pregunta que este libro ha repetido | la pregunta que este curso ha repetido | the question this book has repeated | the question this course has repeated |
| 4 | material que este libro no cubre | material que este curso no cubre | material this book does not cover | material this course does not cover |
| 5 | Ninguna página te ha dado experiencia, y no hay forma de que lo haga: | El curso no te ha dado experiencia, y no puede dártela: | No page has given you experience, and no page can: | The course has not given you experience, and it cannot: |
| 6 | Lo que sí te ha dado este libro | Lo que sí te ha dado este curso | What this book has given you | What this course has given you |
| 7 | un libro que cambia sus reglas en la última página sin avisar | un curso que cambia sus reglas al final sin avisar | a book that changes its rules on the last page without saying so | a course that changes its rules at the end without saying so |
| 8 | el que este libro recomienda | el que este curso recomienda | the one this book recommends | the one this course recommends |
| 9 | las lecturas de este libro | las lecturas de este curso | the reads in this book | the reads in this course |
| 10 | este libro no es el primer peldaño | este curso no es el primer peldaño | this book is the first rung of neither | this course is the first rung of neither |
| 11 | Donde este libro puso ojos y proceso | Donde este curso puso ojos y proceso | Where this book put eyes and process | Where this course put eyes and process |
| 12 | por eso este libro va primero | por eso este curso va primero | why this book comes first | why this course comes first |
| 13 | Sigue siendo verdad en la última página. | Sigue siendo verdad al final del curso. | That is still true on the last page. | That is still true at the end of the course. |
| 14 | el mismo día que cierres el libro. | el mismo día que termines el curso. | the same day you close the book. | the same day you finish the course. |
| 15 | el win rate que este libro se ha negado a poner en ninguna página. | el win rate que este curso se ha negado a poner en ninguna lección. | the win rate this book has refused to put on any page. | the win rate this course has refused to put in any lesson. |
| 16 | Así que el libro se cierra donde empezó | Así que el curso termina donde empezó | So the book closes where it opened | So the course ends where it began |

Edits 3, 4, 6 and 8–12 only swap the noun; the rest of each sentence already read well. The three
sentences that mentioned a page (2, 5, 13) are rewritten short and plain, and 15 uses "lección", the
app's own unit. The lesson already says "tú"/"you" throughout, so there was no "el lector" to replace.

**m23-l1, scalping bullet (ES and EN).**

| | before | after |
| --- | --- | --- |
| ES | toda la disciplina de este libro tiene menos holgura | toda la disciplina de este curso tiene menos holgura |
| EN | every discipline in this book has the least room | every discipline in this course has the least room |

**`content/course.yaml`, module m35 and lesson m35-l1, both locales.**

| Field | before | after |
| --- | --- | --- |
| module title | After this book / Después de este libro | After this course / Después de este curso |
| module summary | …with the tool the book gave you. / …que te ha dado el libro. | …with the tool the course gave you. / …que te ha dado el curso. |
| lesson title | After this book / Después de este libro | After this course / Después de este curso |
| lesson summary, sentence 1 | What you take from the book is… / Lo que te llevas del libro es… | What you take from the course is… / Lo que te llevas del curso es… |
| lesson summary, sentence 2 | No page has given you experience, so… / Ninguna página te ha dado experiencia, así que… | The course has not given you experience, so… / El curso no te ha dado experiencia, así que… |

Left alone in `course.yaml`: the YAML **comments** that say "book" (line 12 is about the PDF, which is
a book; the comments around block f and the epilogue are editorial notes). They are not shipped.

### What was deliberately left: every remaining hit, justified

After the rewrite the grep returns only these, and none of them calls this course a book.

| Category | Hits | Where |
| --- | ---: | --- |
| order book ("libro de órdenes", "un libro fino / poco profundo", "el libro") | 146 | ES, across 30 lessons; trading vocabulary (`g-order-book`) |
| "de manual", the idiom for "a textbook case" | 11 | ES m08-l1:206, m08-l2:67, m09-l1:126, m12-l1:30, m13-l1:69, m15-l2:58, m20-l1:120, m23-l2:86, m27-l2:31, m32-l1:50, m32-l1:95 |
| "el manual", the general canon, not this course | 2 | ES m09-l1:161, m09-l2:80 |
| "libros de texto", textbooks in general | 1 | ES m13-l1:113 |
| ledger / accounting books | 3 | ES m01-l1:12 ("libro contable"), m02-l1:20 ("libros internos"), m02-l1:114 ("los libros del exchange") |
| trading book (a desk's positions) | 1 | ES m21-l1:64 |
| "manual" as a method, "manualmente", "manually" | 5 | ES and EN m28-l1:16 ("backtest manual" / "manual backtest"); ES m27-l1:155; EN m27-l1:146, m32-l1:111 |
| `selector` (contains `lector`) | 4 | ES m22-l1:93, 101; EN m22-l1:86, 94 |

EN, outside the brief's grep but checked for parity: every remaining "book" is the order book;
"by-the-book" (m27-l2:30) is the idiom whose ES twin is "de manual"; "reader" in m23-l2:154, m30-l1:8
and m34-l1:167 is a generic chart reader, not the course's reader.

### Cross-references

All 228 references per locale in `content/lesson-refs.{es,en}.txt` were read against the **current**
title of their target. Every target exists (the suite already asserts that), and every one is the
right target for what the sentence says about it. Checks that needed the target opened, not just its
title:

* m27-l1's "temporalidades anidadas (m03-l2)" and the zoom warning: m03-l2 lines 68–72 teach both.
* m22-l1's "aritmética de rachas … m25-l1": m25-l1's "Las rachas de pérdidas son normales, y calculables".
* m08-l2's "m13, paso 4": step 4 of m13-l1's checklist is "wait for price to react at the level".
* m34-l1's "24/7 (m10-l1)": m10-l1's "Serie sin huecos, libros más finos".

ES and EN carry the same (lesson, mention) pairs, 228 for 228.

References written in words were checked the same way, and all are right after the 2026-08-10
renumbering:

* "lección siguiente / anterior", "next / previous lesson" in m03-l1, m03-l2, m22-l1, m22-l2.
* "lección 1 / 2" inside m19.
* "el módulo anterior" in m05-l1 (→ m04, the linear contract) and m31-l1 (→ m30, absorption).
* EN "the next module" in m05-l1 (→ m06, liquidation).
* "más adelante" in m02-l1, m03-l2 and m22-l1 (perpetual futures, funding, expectancy, each taught
  later than the lesson that says it).

The one `lesson-refs.es.txt` line that moved is context text only (m23-l1's "de este libro" → "de este
curso").

---

## P2 — glossary coverage audit

**`docs/glossary-candidates.md`** is a proposal only. It holds:

* a curated table of **125** candidate terms: ES term, EN term, lesson count **in each locale**, bold
  yes/no, and a one-line proposed definition. Rows that belong to an existing entry (an alias, a match
  form or a new sense) say so in the definition instead of proposing a new id;
* appendix A, every bold span in both locales with the lessons it appears in;
* appendix B, the 1818 ES words in 3+ lessons not in the glossary;
* appendix C, the 160 ES two-word phrases (no stopword in either word) in 3+ lessons not in the
  glossary.

Three curated terms would coin in EN today, because the EN prose does not use them yet: *zona de
interés / area of interest*, *pérdida acotada / capped loss*, *sesgo de supervivencia / survivorship
bias*. The counts columns show it.

**`g-narrative` is now two senses.** No new id, no other glossary change.

1. Origin `m01-l1`: the existing definition, unchanged (the story of why a single token should be worth
   something).
2. Origin `m15-l1`, the key of display **m17-l1** (*Macro and capital flow*). New:
   "The story that moves capital into a whole sector or asset class: AI tokens, memecoins, real-world
   assets (RWA). Money follows it for as long as people believe it." /
   "El relato que lleva capital hacia un sector o una clase de activo entera: tokens de IA, memecoins,
   activos del mundo real (RWA). El dinero lo sigue mientras la gente se lo crea."

The format allows a second origin: each sense carries its own, as `g-premium` already does. m17-l1 is
the lesson about stories moving capital between asset classes (rotation, "alt season", the "digital
gold" story, under "Tres narrativas que cuestan dinero"). **Two things to know:**

* That lesson uses "narrativa" only in that heading, and the annotator skips headings. So the new origin
  vetoes no occurrence, and no link moved because of it.
* The course prose never names AI, RWA or memecoins as sectors. The definition uses them as the examples
  the brief asked for. The loader only checks that *terms* don't coin, so this passes, but it is the one
  place where the glossary says something the lessons do not.

---

## P3 — emphasis cleanup

The rule, in the order the classifier applies it (first match wins):

1. **lead-in**: bold stays. A `**` span at the very start of a paragraph or list item (after `-`, `*`,
   `1.` or `>`; never a continuation line of a paragraph), followed by **"." or ":"**, inside the span or
   right after it. **Two additions to the brief's definition, flagged:** an **em dash** after the span
   (`- **Market order** — …`), and a span ending in **"?"** (`**Who bought before?**`). Without them, EN —
   which writes definition bullets with " —" where ES writes ":" — would keep the label in ES and lose it
   in EN. The counts are below, and the ledger's `delimiter` column marks every lead-in, so dropping
   either addition is a filter on that column.
2. **warning-callout**: bold removed, outside the budget. Inline bold inside `:::note{type=warning}`.
   Lead-ins inside a warning callout stay lead-ins (43 per locale), because they are structure there too.
3. **glossary**: bold removed. The span's text, minus trailing punctuation, is a glossary term or
   `match` form in that locale, or `X (Y)` where either half is one. No markup is needed to turn these
   into glossary references: the annotator already marks terms, bold or not, by its usual rules (first
   occurrence in a lesson, never in the origin lesson).
4. **kept**: bold stays. The one risk warning or must-remember rule of a lesson, chosen by hand.
5. **removed**: everything else.

Lesson **summaries** (`course.yaml`) were in scope under the same rules. They contain **zero** `**`
spans, so there was nothing to do. Exercise YAMLs were not touched.

### Counts

| | ES | EN |
| --- | ---: | ---: |
| `**` spans before | 1737 | 1737 |
| became glossary references (bold removed) | 226 | 233 |
| kept as emphasis | 18 | 18 |
| lead-ins kept (reported separately) | 473 | 478 |
| — of which "." or ":" (the brief's rule) | 437 | 411 |
| — of which em dash (addition) | 33 | 64 |
| — of which "?" (addition) | 3 | 3 |
| removed inside warning callouts | 37 | 37 |
| removed, other | 983 | 971 |
| `**` spans after (lead-ins + kept) | 491 | 496 |

Every one of the 3474 spans is a row of `docs/content-round-5-emphasis-ledger.tsv`: locale, lesson,
line before the cleanup, outcome, lead-in delimiter, span text. Re-running the classifier on the cleaned
files finds only lead-ins and kept spans, the same 473 + 18 and 478 + 18.

**Lead-in parity is close, not exact** (473 vs 478). The remaining differences are wording, not the
rule. For example, m09-l1 has EN "**Markup** —" bullets with no matching bullet label in ES, and m15-l1
has EN "**The body decides, not the wick.**" where ES bolds a phrase mid-sentence. m27-l2 has one more
EN lead-in.

### Kept emphasis: one per lesson, and no lesson has more than one

18 lessons keep one span in each locale, the same span in both. The other 26 keep none: their bold was
vocabulary, numbers or worked-example values, not a warning or a rule. **No lesson is flagged for more
than one kept emphasis.**

| Lesson | Locale | Kept span |
| --- | --- | --- |
| m02-l1 | es | mientras tus monedas estén en un exchange, es el exchange quien las guarda por ti. |
| m02-l1 | en | for as long as your coins sit on an exchange, the exchange is holding them for you. |
| m03-l2 | es | "¿tendencia o rango, en mi temporalidad?" |
| m03-l2 | en | "trending or ranging, on my timeframe?" |
| m08-l1 | es | espera al cierre, y a que ese cierre aguante. |
| m08-l1 | en | wait for the close, and for that close to hold. |
| m08-l2 | es | el significado de una vela viene, sobre todo, de dónde ocurre. |
| m08-l2 | en | a candle's meaning comes overwhelmingly from where it happens. |
| m09-l1 | es | «¿quién está absorbiendo, y en qué lado?» |
| m09-l1 | en | "who is doing the absorbing, and on which side?" |
| m15-l1 | es | la diagonal es el instrumento más débil de este curso. |
| m15-l1 | en | the diagonal is the weakest instrument in this course. |
| m16-l1 | es | un mercado tranquilo no es un mercado seguro. Es un mercado que todavía no se ha movido. |
| m16-l1 | en | a quiet market is not a safe market. It is a market that has not moved yet. |
| m18-l1 | es | Los extremos pueden persistir durante semanas o meses. |
| m18-l1 | en | Extremes can persist for weeks or months. |
| m19-l1 | es | nunca leas el OI sin el precio |
| m19-l1 | en | never read OI without price |
| m21-l1 | es | Te quedas con la pata ganadora de una cobertura cuya pata perdedora ha sido cerrada al peor precio posible |
| m21-l1 | en | You are left holding the winning leg of a hedge whose losing leg has been closed at the worst possible price |
| m22-l1 | es | El stop define el riesgo; el riesgo define el tamaño. |
| m22-l1 | en | The stop defines the risk; the risk defines the size. |
| m22-l2 | es | En un drawdown, las correlaciones de cripto saltan hacia +1: |
| m22-l2 | en | In a drawdown, crypto correlations snap toward +1: |
| m23-l2 | es | un nivel es un precio, y un precio es el mismo número en todos los gráficos. |
| m23-l2 | en | a level is a price, and a price is the same number on every chart. |
| m24-l1 | es | tu orden no se ejecuta |
| m24-l1 | en | you do not fill |
| m26-l1 | es | decide peor en el momento y mejor por adelantado |
| m26-l1 | en | decided worst in the moment and best in advance |
| m28-l1 | es | pon a prueba la afirmación antes de pagar por saberla. |
| m28-l1 | en | test the claim before you pay to find out. |
| m34-l1 | es | no hay un sistema nuevo, hay tres mecánicas con más nombres. |
| m34-l1 | en | there is no new system, there are three mechanics with more names. |
| m35-l1 | es | sabes distinguir una afirmación con mecanismo de una que no lo tiene. |
| m35-l1 | en | you can tell a claim with a mechanism from one without. |

Considered and **not** kept because the lesson had a stronger candidate: m22-l1's "la liquidación nunca
debe ser tu stop efectivo" (kept: "El stop define el riesgo; el riesgo define el tamaño."), and m35-l1's
"El curso no te ha dado experiencia" (kept: the claim-with-a-mechanism sentence).

### Per lesson (ES / EN)

| Lesson | glossary | kept | lead-in | warning-callout | removed | total |
| --- | --- | --- | --- | --- | --- | --- |
| m01-l1 | 5 / 5 | 0 / 0 | 5 / 5 | 0 / 0 | 11 / 11 | 21 / 21 |
| m02-l1 | 8 / 8 | 1 / 1 | 14 / 14 | 1 / 1 | 11 / 11 | 35 / 35 |
| m03-l1 | 14 / 11 | 0 / 0 | 5 / 5 | 0 / 0 | 25 / 28 | 44 / 44 |
| m03-l2 | 9 / 9 | 1 / 1 | 6 / 6 | 0 / 0 | 20 / 20 | 36 / 36 |
| m04-l1 | 11 / 11 | 0 / 0 | 12 / 12 | 1 / 1 | 18 / 18 | 42 / 42 |
| m05-l1 | 6 / 6 | 0 / 0 | 8 / 8 | 2 / 2 | 4 / 5 | 20 / 21 |
| m06-l1 | 4 / 5 | 0 / 0 | 11 / 11 | 3 / 3 | 7 / 6 | 25 / 25 |
| m07-l1 | 4 / 4 | 0 / 0 | 17 / 17 | 1 / 1 | 16 / 16 | 38 / 38 |
| m08-l1 | 6 / 7 | 1 / 1 | 4 / 4 | 0 / 0 | 28 / 27 | 39 / 39 |
| m08-l2 | 2 / 2 | 1 / 1 | 14 / 14 | 0 / 0 | 17 / 17 | 34 / 34 |
| m09-l1 | 17 / 15 | 1 / 1 | 12 / 14 | 1 / 1 | 16 / 16 | 47 / 47 |
| m09-l2 | 8 / 8 | 0 / 0 | 17 / 17 | 0 / 0 | 32 / 32 | 57 / 57 |
| m10-l1 | 10 / 10 | 0 / 0 | 7 / 7 | 0 / 0 | 16 / 16 | 33 / 33 |
| m11-l1 | 10 / 10 | 0 / 0 | 8 / 8 | 0 / 0 | 45 / 45 | 63 / 63 |
| m12-l1 | 4 / 4 | 0 / 0 | 3 / 3 | 2 / 2 | 28 / 28 | 37 / 37 |
| m13-l1 | 1 / 5 | 0 / 0 | 9 / 9 | 0 / 0 | 17 / 13 | 27 / 27 |
| m14-l1 | 2 / 2 | 0 / 0 | 11 / 11 | 0 / 0 | 11 / 11 | 24 / 24 |
| m15-l1 | 2 / 2 | 1 / 1 | 7 / 9 | 0 / 0 | 25 / 23 | 35 / 35 |
| m15-l2 | 0 / 0 | 0 / 0 | 8 / 8 | 1 / 1 | 18 / 18 | 27 / 27 |
| m16-l1 | 6 / 6 | 1 / 1 | 3 / 3 | 0 / 0 | 25 / 25 | 35 / 35 |
| m17-l1 | 3 / 4 | 0 / 0 | 8 / 8 | 1 / 1 | 16 / 15 | 28 / 28 |
| m18-l1 | 3 / 4 | 1 / 1 | 15 / 15 | 1 / 1 | 21 / 21 | 41 / 42 |
| m19-l1 | 2 / 3 | 1 / 1 | 15 / 15 | 2 / 2 | 25 / 24 | 45 / 45 |
| m19-l2 | 3 / 4 | 0 / 0 | 13 / 13 | 1 / 1 | 30 / 29 | 47 / 47 |
| m20-l1 | 4 / 4 | 0 / 0 | 16 / 16 | 2 / 2 | 30 / 30 | 52 / 52 |
| m21-l1 | 2 / 2 | 1 / 1 | 8 / 8 | 0 / 0 | 20 / 20 | 31 / 31 |
| m21-l2 | 0 / 0 | 0 / 0 | 14 / 14 | 0 / 0 | 16 / 17 | 30 / 31 |
| m22-l1 | 4 / 4 | 1 / 1 | 24 / 24 | 1 / 1 | 62 / 62 | 92 / 92 |
| m22-l2 | 2 / 2 | 1 / 1 | 7 / 7 | 0 / 0 | 16 / 16 | 26 / 26 |
| m23-l1 | 9 / 10 | 0 / 0 | 16 / 16 | 1 / 1 | 42 / 41 | 68 / 68 |
| m23-l2 | 1 / 1 | 1 / 1 | 9 / 9 | 1 / 1 | 33 / 33 | 45 / 45 |
| m24-l1 | 14 / 15 | 1 / 1 | 5 / 5 | 5 / 5 | 29 / 27 | 54 / 53 |
| m25-l1 | 4 / 4 | 0 / 0 | 6 / 6 | 0 / 0 | 19 / 19 | 29 / 29 |
| m26-l1 | 7 / 6 | 1 / 1 | 19 / 19 | 1 / 1 | 19 / 20 | 47 / 47 |
| m27-l1 | 3 / 2 | 0 / 0 | 17 / 17 | 3 / 3 | 40 / 41 | 63 / 63 |
| m27-l2 | 1 / 1 | 0 / 0 | 22 / 23 | 0 / 0 | 8 / 7 | 31 / 31 |
| m28-l1 | 1 / 1 | 1 / 1 | 9 / 9 | 2 / 2 | 24 / 24 | 37 / 37 |
| m29-l1 | 8 / 8 | 0 / 0 | 14 / 14 | 0 / 0 | 7 / 7 | 29 / 29 |
| m30-l1 | 4 / 4 | 0 / 0 | 12 / 12 | 1 / 1 | 25 / 24 | 42 / 41 |
| m31-l1 | 7 / 7 | 0 / 0 | 6 / 6 | 2 / 2 | 7 / 7 | 22 / 22 |
| m32-l1 | 1 / 1 | 0 / 0 | 12 / 12 | 0 / 0 | 7 / 7 | 20 / 20 |
| m33-l1 | 5 / 5 | 0 / 0 | 5 / 5 | 0 / 0 | 8 / 8 | 18 / 18 |
| m34-l1 | 9 / 11 | 1 / 1 | 11 / 11 | 1 / 1 | 66 / 63 | 88 / 87 |
| m35-l1 | 0 / 0 | 1 / 1 | 9 / 9 | 0 / 0 | 23 / 23 | 33 / 33 |

### What the cleanup moved in the glossary links

Bold splits text nodes, so a glossary phrase split across a bold boundary could not match. Removing the
bold fixed two such cases, in both locales:

* **m26-l1** (key `m23-l1`): "precio de **liquidación**" / "**liquidation** price" is now one text node,
  so `g-liquidation-price` gains one web mark (ES 579 → 580, EN 661 → 662; PDF links unchanged at
  57 / 67).
* **m24-l1** (key `m21-l1`): "orden de **mercado**" is now unsplit, so the first occurrence of
  `g-market-order` (ES) and `g-taker` (EN) comes earlier in the lesson and its line moved up one place
  in the report. Same term, same lesson, same policy.

Every other line that changed in `glossary-links.{es,en}.txt` changed its **context text only**,
because each context is taken from one text node and the nodes got longer. Apart from those two,
(lesson, policy, term) is identical, line for line.

---

## P4 — bundle and verifiers

All green. The bundle and the goldens were exported to a scratch directory and compared there;
`dist/` was not overwritten.

| Check | Result |
| --- | --- |
| `export_bundle.py` (format **2**) | exit 0. Text diff 0 (prose and glossary multisets, every lesson block for block), block inventory OK (88 ASTs), exercise refs OK (242 marks). Fingerprint `f38c211e0eb4a1f1…` → **`8fa3834501ef93a0…`** |
| per-file bundle diff against the P0 export | **92 files moved, as expected:** `ast/{es,en}/*.json` (all 88: every lesson lost bold), `ast/index.json`, `glossary/glossary.{es,en}.json` (only `g-narrative`), `reading-seconds.json` (only m35-l1: ES 453 → 449, EN 451 → 449). `manifest.json` changed only in the m35 module and lesson titles and summaries. No file was added or removed |
| `export_generation_goldens.py` | `exercise-mode.tsv` (3915), `figures.tsv` (33), `formatter-cases.tsv` and `configs/` (107) **byte-identical** to the existing copy. Zero diff, no recapture |
| `verify_golden_stability.py` | exit 0, **90 committed fingerprints hold** (84 golden + 6 pinned). Generation digest `6999679392b682a2…`, the same as the cleanup lote recorded |
| frozen reports (`glossary-links`, `lesson-refs`) | regenerated and reviewed; the only changes in link decisions are the two described in P3 |
| backend `pytest` (whole suite, incl. `test_glossary`, `test_content_manifest`, `test_figure_prose_coupling`, `test_export_bundle`) | **1300 passed, 20 skipped** |
| frontend `vitest` (whole suite, incl. both report tests) | **458 passed, 1 skipped**, 43 files |

No guard, threshold, pin or golden was changed.

### Recaptures, enumerated

There are no generation-golden recaptures. The deliberate re-records are all **content artifacts**:

* bundle ASTs for **all 44 lessons in both locales**: m01-l1, m02-l1, m03-l1, m03-l2, m04-l1, m05-l1,
  m06-l1, m07-l1, m08-l1, m08-l2, m09-l1, m09-l2, m10-l1, m11-l1, m12-l1, m13-l1, m14-l1, m15-l1, m15-l2,
  m16-l1, m17-l1, m18-l1, m19-l1, m19-l2, m20-l1, m21-l1, m21-l2, m22-l1, m22-l2, m23-l1, m23-l2, m24-l1,
  m25-l1, m26-l1, m27-l1, m27-l2, m28-l1, m29-l1, m30-l1, m31-l1, m32-l1, m33-l1, m34-l1, m35-l1. Every
  one lost bold. m35-l1 and m23-l1 also carry the P1 rewrite;
* `glossary-links.{es,en}.txt` and `lesson-refs.es.txt`, as described above;
* reading time for m35-l1 only.

## Side task — voice page and writing rule

Both files were created during this round, at your request mid-round:

* **`docs/prose-voice.md`**: your text, verbatim, with the "Reference paragraphs" section filled in and
  the blacklist left empty.
* **`CLAUDE.md`** at the repo root: the project had **no** `CLAUDE.md`, so this file was created holding
  only the "Writing rule (always)" section. Nothing else is in it.

Reference paragraphs chosen. Each is unchanged since the last commit and carries no bold. Every lesson
file lost bold somewhere this round, so "not touched" was read at the paragraph level.

* **m01–m08: m05-l1, paragraph 7.** "Los principiantes citan su apalancamiento como si fuera su
  beneficio. No lo es. …"
* **m10–m20: none.** The only paragraph that passed the screen, m16-l1 paragraph 29, ends on a calque
  ("difieren en si está pasando algo siquiera"). It is a near miss, so the page says so instead of
  pasting it.
* **m25+: m28-l1, paragraph 22.** "Ya tienes tu histórico y tus reglas, y los resultados son mediocres.
  Así que ajustas. …"

### Two of this round's own sentences, checked against the voice page

The voice page arrived after P1 and the narrativa entry were written. Two sentences from this round
trip its "rhythmic triads" rule if read strictly. Both are flagged here and left unchanged:

* m35-l1, the new opening: "Esta lección dice qué te llevas, qué no te llevas y por dónde seguir." (EN:
  "what you take with you, what you do not, and where to go next"). The three items are the lesson's
  three parts, not rhythm; the sentence it replaced had the same three.
* `g-narrative` sense 2: "tokens de IA, memecoins, activos del mundo real (RWA)". These are the three
  examples the brief asked for.

---

## Files

Modified:

* `content/es/lessons/*.md`, `content/en/lessons/*.md`: all 88 (emphasis cleanup); m35-l1 and m23-l1
  also in P1
* `content/course.yaml`: m35 module and lesson titles and summaries
* `content/glossary.yaml`: `g-narrative` → two senses
* `content/glossary-links.es.txt`, `content/glossary-links.en.txt`: regenerated, reviewed above
* `content/lesson-refs.es.txt`: regenerated, one context line

New:

* `docs/glossary-candidates.md`
* `docs/content-round-5-emphasis-ledger.tsv`
* `docs/content-round-5-handoff.md` (this file)
* `docs/prose-voice.md`, `CLAUDE.md` (side task, below)

Not touched: exercise YAMLs, figure specs, the READMEs (no feature, endpoint or content rule changed),
and `dist/`. The bundle and the goldens were exported to a scratch directory for the comparison.
Re-exporting `dist/bundle` and re-copying the Android contracts (`export_contracts_to_android.py`) are
left for whoever commits this, as last round.

---

## Appendix — m35-l1 in full

### ES, before

```markdown
# Después de este libro

El libro se acaba aquí, así que toca decir con precisión qué te llevas, qué no te llevas y qué caminos
salen de esta página. Sin inflar nada: un curso que exagera lo que ha enseñado deja mal preparado para
lo primero que pasa después de cerrarlo.

## Lo que te llevas

Sabes leer un gráfico por mecanismos en lugar de por formas: qué órdenes hay en reposo en un nivel y
por qué se acumulan ahí, qué le hace la venta forzada a un libro fino, qué esconde una vela cuando la
miras como el agregado que es. Sabes dimensionar una posición desde la distancia al stop y no desde el
apalancamiento (**m22**), lo que significa que sabes cuánto puedes perder antes de abrirla y que ese
número lo eliges tú. Sabes que un proceso se valida antes de pagarlo con dinero real, y con qué tamaño
de muestra empieza a decir algo (**m28**). Y sabes montar una operación completa de principio a fin,
con el motivo escrito antes de la entrada y no después del resultado.

Pero la posesión más valiosa de todas es la que menos se parece a una técnica: **sabes distinguir una
afirmación con mecanismo de una que no lo tiene.** Es la pregunta que este libro ha repetido en cada
módulo —qué órdenes hay ahí, quién las puso, qué las obliga a ejecutarse— y es la única que seguirá
sirviendo con material que este libro no cubre, incluido el que se escriba el año que viene. Las
técnicas caducan cuando cambia el mercado que las produjo; el criterio no.

Y ahora el límite, con la misma franqueza. **Ninguna página te ha dado experiencia**, y no hay forma de
que lo haga: saber cómo se comporta un libro fino a las 3 de la madrugada de un domingo no es lo
mismo que haber tenido una posición abierta a esa hora. Lo que sí te ha dado este libro es el criterio
para acumular esa experiencia sin arruinarte mientras la acumulas —el tamaño que sobrevive a una racha
mala, el stop decidido antes de la entrada, el diario que convierte una operación en un dato en vez de
en un recuerdo—, y eso es justo lo que separa a quien llegará a mil operaciones de quien se queda en
veinte.

:::note{type=info}
Esta lección no tiene ejercicios, y es a propósito. Lo decimos claramente, porque un libro que cambia
sus reglas en la última página sin avisar es peor que uno que las cambia y lo dice: todo lo demás aquí
se examina porque todo lo demás se puede comprobar. Un epílogo no examina nada. Te devuelve el
bolígrafo.
:::

## El camino por defecto: profundizar aquí

Hay un camino que no necesita nada nuevo, y es el que este libro recomienda: **quedarte donde estás y
hacerlo más veces.**

- **Horas de pantalla.** Ninguna de las lecturas de este libro —una absorción, un barrido, una
  compresión que precede a una expansión— se reconoce a la primera. Se reconocen después de haberlas
  visto muchas veces, incluidas todas las que parecían serlo y no lo eran.
- **El diario, creciendo.** El diario que **m27-l2** te hizo empezar es lo único que convierte horas de
  pantalla en muestra, y la muestra es exactamente lo que **m28** exigía para poder decir algo de tu
  sistema. Veinte operaciones no distinguen tu ventaja de una moneda al aire; doscientas empiezan a
  hacerlo. La distancia entre esos dos números se mide en meses, y no hay atajo que los salte.
- **Releer.** Una lección leída antes de haber operado y releída después no es la misma lección: la
  segunda vez tienes ejemplos propios contra los que ponerla. La app te deja **desmarcar** una lección
  ya completada justo para esto, sin perder nada de lo que llevas hecho.

Y ahora el aviso que protege todo lo anterior, porque es el error clásico del día después de terminar
un curso: la tentación es buscar **más tácticas**. Otro patrón, otro indicador, otro setup con nombre
propio. Fíjate en lo que eso es en realidad: añadir mandos a un sistema cuya muestra no ha crecido. Es
el sobreajuste de **m28** en versión humana —la misma operación de ajustar el ruido, hecha con la
carrera de uno en lugar de con una hoja de cálculo— y tiene el mismo síntoma: cada racha mala produce
una regla nueva, y así ninguna regla llega a acumular las operaciones que harían falta para saber si
servía. Más tácticas sobre la misma muestra no es más sistema; es menos.

## Las dos escaleras que existen, y que no son esta

Si en algún momento quieres subir un escalón de verdad, hay dos escaleras, y este libro no es el primer
peldaño de ninguna: son edificios distintos. Nombrarlas es más útil que fingir que no están ahí.

### La escalera cuantitativa

Seis áreas, una frase cada una, ninguna enseñada aquí:

- **Costes de transacción modelados** —la comisión, el slippage y el impacto que tu propia orden tiene
  en el precio, cada uno como una función del tamaño de la orden y no como una constante—, que es lo
  que **m24** te hizo estimar a mano.
- **Dimensionamiento fraccional** —qué fracción del capital arriesgar por operación, derivada de la
  ventaja medida en lugar de fijada por regla, del tipo de la fórmula de Kelly—, sobre el porcentaje
  fijo de **m22**.
- **Microestructura medida** —el libro de órdenes y el flujo agresor procesados como series de datos en
  vez de leídos en pantalla—, que es **m31** con un histórico donde tú tenías una foto.
- **Arbitraje estadístico** —dos instrumentos que se mueven juntos y la diferencia entre ellos operada
  cuando se estira—, la prima de **m32** convertida en un negocio.
- **Validación walk-forward** —entrenar en una ventana, probar en la siguiente, avanzar y repetir—, que
  es la mitad de prueba de **m28** hecha muchas veces en lugar de una sola.
- **Clasificación de régimen** —un modelo que decide en qué estado está el mercado antes de aplicar la
  regla que corresponde a ese estado—, los ciclos de volatilidad de **m16** medidos en vez de vistos.

La honestidad que importa aquí: **es otra profesión.** Donde este libro puso ojos y proceso, esa
escalera pone código, estadística y datos, y los tres se aprenden aparte. No es el nivel dos de esto:
es otro edificio, con su propia planta baja. Lo que sigue valiendo dentro de él es lo de siempre —una
ventaja medida, un tamaño que sobrevive a la racha, un criterio de abandono escrito antes de
necesitarlo—, y por eso este libro va primero aunque no lleve allí.

### La escalera de los otros instrumentos

El vecino natural son las **opciones**. **m21-l2** ya las nombró —los vencimientos grandes concentran
flujo forzado en el perpetuo— y allí mismo declaró la frontera: la mecánica de una opción, cómo se
dimensiona una cobertura y por qué cambia al moverse el precio, es un segundo curso y no una nota al
pie de este. Sigue siendo verdad en la última página. Lo que cambia al pasar de un instrumento a otro
es la forma en que se gana y se pierde dinero; lo que no cambia es que hay que saber, antes de abrir,
cuánto puedes perder y qué te haría cerrar.

## Lo que vas a tener enfrente

Queda una cosa por decir, y hace falta el mismo día que cierres el libro.

Ahí fuera hay un ecosistema entero esperándote: grupos de señales, canales VIP, gente que se ofrece a
operar tu cuenta y el curso que **sí** promete, el que pone el win rate que este libro se ha negado a
poner en ninguna página. No hace falta desconfiar de todo eso por principio: hace falta leerlo con la
herramienta que ya tienes. **Pide el mecanismo.** Qué órdenes hay ahí, quién las puso, qué las obliga
a ejecutarse. Una señal que no puede contestar eso es la misma afirmación sin mecanismo
que **m34** desmontó en el dialecto de la masa, con otro disfraz, y se responde igual: si ninguna
observación la contradice, no predice nada.

Y hay un mecanismo que puedes leer siempre, incluso cuando te esconden el de la estrategia: **el de
quien te la vende.** Quien vive de venderte la señal ingresa cuando te suscribes, no cuando ganas; y
quien cobra un porcentaje del volumen que mueves ingresa con tu actividad, no con tu resultado. Eso no
convierte a nadie en un estafador —un negocio puede ser honesto y tener sus incentivos igual—, pero es
un dato, y es un dato que ya sabes leer, porque es la misma pregunta de siempre aplicada a una persona
en vez de a un nivel. Y todo ese ecosistema está construido sobre la psicología que describe **m26**:
la prisa, el FOMO, la racha ajena vista de cerca y la propia vista de lejos.

Así que el libro se cierra donde empezó, con el proceso en tus manos y en las de nadie más. Elige tu
temporalidad, dimensiona desde el stop, escribe antes de mirar, y que la única campana de cierre que
tengas siga siendo la que te construyes tú.
```

### ES, after

```markdown
# Después de este curso

El curso se acaba aquí. Esta lección dice qué te llevas, qué no te llevas y por dónde seguir. Sin
inflar nada: un curso que exagera lo que ha enseñado deja mal preparado para lo primero que pasa después
de terminarlo.

## Lo que te llevas

Sabes leer un gráfico por mecanismos en lugar de por formas: qué órdenes hay en reposo en un nivel y
por qué se acumulan ahí, qué le hace la venta forzada a un libro fino, qué esconde una vela cuando la
miras como el agregado que es. Sabes dimensionar una posición desde la distancia al stop y no desde el
apalancamiento (m22), lo que significa que sabes cuánto puedes perder antes de abrirla y que ese
número lo eliges tú. Sabes que un proceso se valida antes de pagarlo con dinero real, y con qué tamaño
de muestra empieza a decir algo (m28). Y sabes montar una operación completa de principio a fin,
con el motivo escrito antes de la entrada y no después del resultado.

Pero la posesión más valiosa de todas es la que menos se parece a una técnica: **sabes distinguir una
afirmación con mecanismo de una que no lo tiene.** Es la pregunta que este curso ha repetido en cada
módulo —qué órdenes hay ahí, quién las puso, qué las obliga a ejecutarse— y es la única que seguirá
sirviendo con material que este curso no cubre, incluido el que se escriba el año que viene. Las
técnicas caducan cuando cambia el mercado que las produjo; el criterio no.

Y ahora el límite, con la misma franqueza. El curso no te ha dado experiencia, y no puede
dártela: saber cómo se comporta un libro fino a las 3 de la madrugada de un domingo no es lo
mismo que haber tenido una posición abierta a esa hora. Lo que sí te ha dado este curso es el criterio
para acumular esa experiencia sin arruinarte mientras la acumulas —el tamaño que sobrevive a una racha
mala, el stop decidido antes de la entrada, el diario que convierte una operación en un dato en vez de
en un recuerdo—, y eso es justo lo que separa a quien llegará a mil operaciones de quien se queda en
veinte.

:::note{type=info}
Esta lección no tiene ejercicios, y es a propósito. Lo decimos claramente, porque un curso que cambia
sus reglas al final sin avisar es peor que uno que las cambia y lo dice: todo lo demás aquí
se examina porque todo lo demás se puede comprobar. Un epílogo no examina nada. Te devuelve el
bolígrafo.
:::

## El camino por defecto: profundizar aquí

Hay un camino que no necesita nada nuevo, y es el que este curso recomienda: quedarte donde estás y
hacerlo más veces.

- **Horas de pantalla.** Ninguna de las lecturas de este curso —una absorción, un barrido, una
  compresión que precede a una expansión— se reconoce a la primera. Se reconocen después de haberlas
  visto muchas veces, incluidas todas las que parecían serlo y no lo eran.
- **El diario, creciendo.** El diario que m27-l2 te hizo empezar es lo único que convierte horas de
  pantalla en muestra, y la muestra es exactamente lo que m28 exigía para poder decir algo de tu
  sistema. Veinte operaciones no distinguen tu ventaja de una moneda al aire; doscientas empiezan a
  hacerlo. La distancia entre esos dos números se mide en meses, y no hay atajo que los salte.
- **Releer.** Una lección leída antes de haber operado y releída después no es la misma lección: la
  segunda vez tienes ejemplos propios contra los que ponerla. La app te deja desmarcar una lección
  ya completada justo para esto, sin perder nada de lo que llevas hecho.

Y ahora el aviso que protege todo lo anterior, porque es el error clásico del día después de terminar
un curso: la tentación es buscar más tácticas. Otro patrón, otro indicador, otro setup con nombre
propio. Fíjate en lo que eso es en realidad: añadir mandos a un sistema cuya muestra no ha crecido. Es
el sobreajuste de m28 en versión humana —la misma operación de ajustar el ruido, hecha con la
carrera de uno en lugar de con una hoja de cálculo— y tiene el mismo síntoma: cada racha mala produce
una regla nueva, y así ninguna regla llega a acumular las operaciones que harían falta para saber si
servía. Más tácticas sobre la misma muestra no es más sistema; es menos.

## Las dos escaleras que existen, y que no son esta

Si en algún momento quieres subir un escalón de verdad, hay dos escaleras, y este curso no es el primer
peldaño de ninguna: son edificios distintos. Nombrarlas es más útil que fingir que no están ahí.

### La escalera cuantitativa

Seis áreas, una frase cada una, ninguna enseñada aquí:

- **Costes de transacción modelados** —la comisión, el slippage y el impacto que tu propia orden tiene
  en el precio, cada uno como una función del tamaño de la orden y no como una constante—, que es lo
  que m24 te hizo estimar a mano.
- **Dimensionamiento fraccional** —qué fracción del capital arriesgar por operación, derivada de la
  ventaja medida en lugar de fijada por regla, del tipo de la fórmula de Kelly—, sobre el porcentaje
  fijo de m22.
- **Microestructura medida** —el libro de órdenes y el flujo agresor procesados como series de datos en
  vez de leídos en pantalla—, que es m31 con un histórico donde tú tenías una foto.
- **Arbitraje estadístico** —dos instrumentos que se mueven juntos y la diferencia entre ellos operada
  cuando se estira—, la prima de m32 convertida en un negocio.
- **Validación walk-forward** —entrenar en una ventana, probar en la siguiente, avanzar y repetir—, que
  es la mitad de prueba de m28 hecha muchas veces en lugar de una sola.
- **Clasificación de régimen** —un modelo que decide en qué estado está el mercado antes de aplicar la
  regla que corresponde a ese estado—, los ciclos de volatilidad de m16 medidos en vez de vistos.

La honestidad que importa aquí: es otra profesión. Donde este curso puso ojos y proceso, esa
escalera pone código, estadística y datos, y los tres se aprenden aparte. No es el nivel dos de esto:
es otro edificio, con su propia planta baja. Lo que sigue valiendo dentro de él es lo de siempre —una
ventaja medida, un tamaño que sobrevive a la racha, un criterio de abandono escrito antes de
necesitarlo—, y por eso este curso va primero aunque no lleve allí.

### La escalera de los otros instrumentos

El vecino natural son las opciones. m21-l2 ya las nombró —los vencimientos grandes concentran
flujo forzado en el perpetuo— y allí mismo declaró la frontera: la mecánica de una opción, cómo se
dimensiona una cobertura y por qué cambia al moverse el precio, es un segundo curso y no una nota al
pie de este. Sigue siendo verdad al final del curso. Lo que cambia al pasar de un instrumento a otro
es la forma en que se gana y se pierde dinero; lo que no cambia es que hay que saber, antes de abrir,
cuánto puedes perder y qué te haría cerrar.

## Lo que vas a tener enfrente

Queda una cosa por decir, y hace falta el mismo día que termines el curso.

Ahí fuera hay un ecosistema entero esperándote: grupos de señales, canales VIP, gente que se ofrece a
operar tu cuenta y el curso que sí promete, el que pone el win rate que este curso se ha negado a
poner en ninguna lección. No hace falta desconfiar de todo eso por principio: hace falta leerlo con la
herramienta que ya tienes. Pide el mecanismo. Qué órdenes hay ahí, quién las puso, qué las obliga
a ejecutarse. Una señal que no puede contestar eso es la misma afirmación sin mecanismo
que m34 desmontó en el dialecto de la masa, con otro disfraz, y se responde igual: si ninguna
observación la contradice, no predice nada.

Y hay un mecanismo que puedes leer siempre, incluso cuando te esconden el de la estrategia: el de
quien te la vende. Quien vive de venderte la señal ingresa cuando te suscribes, no cuando ganas; y
quien cobra un porcentaje del volumen que mueves ingresa con tu actividad, no con tu resultado. Eso no
convierte a nadie en un estafador —un negocio puede ser honesto y tener sus incentivos igual—, pero es
un dato, y es un dato que ya sabes leer, porque es la misma pregunta de siempre aplicada a una persona
en vez de a un nivel. Y todo ese ecosistema está construido sobre la psicología que describe m26:
la prisa, el FOMO, la racha ajena vista de cerca y la propia vista de lejos.

Así que el curso termina donde empezó, con el proceso en tus manos y en las de nadie más. Elige tu
temporalidad, dimensiona desde el stop, escribe antes de mirar, y que la única campana de cierre que
tengas siga siendo la que te construyes tú.
```

### EN, before

```markdown
# After this book

The book ends here, so it is worth saying precisely what you take with you, what you do not, and which
roads lead off this page. Without inflating any of it: a course that overstates what it taught leaves
you badly prepared for the first thing that happens after you close it.

## What you now have

You can read a chart by mechanism rather than by shape: which orders are resting at a level and why
they pile up there, what forced selling does to a thin book, what a candle hides when you look at it as
the aggregate it is. You can size a position from the distance to the stop rather than from the
leverage (**m22**), which means you know what you can lose before you open it, and that the number is
one you choose. You know a process gets validated before it is paid for with real money, and at what
sample size it starts to say anything (**m28**). And you can assemble a complete trade end to end,
with the reason written down before the entry instead of after the outcome.

But the most valuable possession of the lot is the one that looks least like a technique: **you can
tell a claim with a mechanism from one without.** It is the question this book has repeated in every
module — which orders are there, who put them there, what forces them to fill — and it is the only one
that keeps working on material this book does not cover, including material written next year.
Techniques expire when the market that produced them changes; the criterion does not.

And now the limit, with the same frankness. **No page has given you experience**, and no page can:
knowing how a thin book behaves at 3 a.m. on a Sunday is not the same as having had a position open at
that hour. What this book has given you is the criteria to accumulate that experience without ruining
yourself while you accumulate it — a size that survives a bad streak, a stop decided before the entry,
a journal that turns a trade into a data point instead of a memory — and that is exactly what separates
someone who will reach a thousand trades from someone who stops at twenty.

:::note{type=info}
This lesson has no exercises, and that is deliberate. Said plainly, because a book that changes its
rules on the last page without saying so is worse than one that changes them and says it: everything
else here is examined because everything else can be checked. An epilogue examines nothing. It hands
back the pen.
:::

## The default path: go deeper here

There is one path that requires nothing new, and it is the one this book recommends: **stay where you
are and do it more times.**

- **Screen time.** None of the reads in this book — an absorption, a sweep, a compression ahead of an
  expansion — is recognised the first time. They are recognised after you have seen them many times,
  including every one that looked like it and was not.
- **The journal, growing.** The journal **m27-l2** made you start is the only thing that turns screen
  time into sample, and sample is exactly what **m28** demanded before anything could be said about
  your system. Twenty trades cannot tell your edge from a coin flip; two hundred begin to. The distance
  between those two numbers is measured in months, and there is no shortcut past them.
- **Re-reading.** A lesson read before you had traded and re-read afterwards is not the same lesson:
  the second time you have examples of your own to hold it against. The app lets you **un-mark** a
  completed lesson for exactly this, without losing anything else you have done.

And now the warning that protects everything above, because it is the classic mistake of the day after
finishing a course: the temptation is to look for **more tactics**. Another pattern, another indicator,
another setup with a name of its own. Notice what that actually is: adding knobs to a system whose
sample has not grown. It is **m28**'s overfitting in human form — the same act of fitting the noise,
performed with a career instead of a spreadsheet — and it has the same symptom: every bad streak
produces a new rule, so no rule ever accumulates the trades it would take to know whether it helped.
More tactics over the same sample is not more system; it is less.

## The two ladders that exist, and are not this one

If at some point you want to climb a genuine step up, there are two ladders, and this book is the first
rung of neither: they are different buildings. Naming them is more use than pretending they are not
there.

### The quantitative ladder

Six areas, one sentence each, none of them taught here:

- **Modelled transaction costs** — the fee, the slippage and the impact your own order has on the
  price, each as a function of order size rather than as a constant — which is what **m24** had you
  estimate by hand.
- **Fractional sizing** — what fraction of capital to risk per trade, derived from the measured edge
  instead of fixed by rule, of the kind the Kelly formula gives — over the fixed percentage of **m22**.
- **Measured microstructure** — the order book and the aggressor flow processed as data series rather
  than read on screen — which is **m31** with a history where you had a snapshot.
- **Statistical arbitrage** — two instruments that move together, and the difference between them
  traded when it stretches — the premium of **m32** turned into a business.
- **Walk-forward validation** — train on one window, test on the next, advance and repeat — which is
  **m28**'s test half done many times instead of once.
- **Regime classification** — a model that decides what state the market is in before applying the rule
  that belongs to that state — the volatility cycles of **m16**, measured instead of seen.

The honesty that matters here: **it is another profession.** Where this book put eyes and process, that
ladder puts code, statistics and data, and all three are learned elsewhere. It is not level two of
this: it is another building, with its own ground floor. What still holds inside it is what always held
— a measured edge, a size that survives the streak, an abandonment criterion written before you need it
— which is why this book comes first even though it does not lead there.

### The other-instruments ladder

The natural neighbour is **options**. **m21-l2** already named them — large expiries concentrate forced
flow into the perpetual — and declared the frontier in the same breath: the mechanics of an option, how
a hedge is sized and why it changes as price moves, are a second course and not a footnote in this one.
That is still true on the last page. What changes from one instrument to another is the shape of how
money is made and lost; what does not change is that you have to know, before you open, what you can
lose and what would make you close.

## What you will be swimming against

One thing is left to say, and it is needed the same day you close the book.

Out there is an entire ecosystem waiting for you: signal groups, VIP channels, people offering to trade
your account, and the course that **does** promise — the one that puts a number on the win rate this
book has refused to put on any page. None of that has to be distrusted on principle. It has to be read
with the tool you already have: **ask for the mechanism.** Which orders are there, who put them there,
what forces them to fill. A signal that cannot answer that is the same claim without a mechanism that
**m34** took apart in the crowd's dialect, wearing a different costume, and it is answered the same
way: if no observation would contradict it, it predicts nothing.

And there is one mechanism you can always read, even when the strategy's own is kept from you: **the
mechanism of whoever is selling it to you.** Someone who lives off selling you the signal is paid when
you subscribe, not when you win; someone paid a share of the volume you move is paid by your activity,
not by your result. That makes nobody a fraud — a business can be honest and still have its incentives
— but it is a fact, and it is a fact you already know how to read, because it is the same old question
applied to a person instead of to a level. And the whole of that ecosystem is built on the psychology
**m26** describes: the hurry, the FOMO, someone else's streak seen up close and your own seen from far
away.

So the book closes where it opened, with the process in your hands and in nobody else's. Choose your
timeframe, size from the stop, write before you look, and may the only closing bell you get remain the
one you build yourself.
```

### EN, after

```markdown
# After this course

The course ends here. This lesson says what you take with you, what you do not, and where to go next.
Without inflating any of it: a course that overstates what it taught leaves you badly prepared for the
first thing that happens after you finish it.

## What you now have

You can read a chart by mechanism rather than by shape: which orders are resting at a level and why
they pile up there, what forced selling does to a thin book, what a candle hides when you look at it as
the aggregate it is. You can size a position from the distance to the stop rather than from the
leverage (m22), which means you know what you can lose before you open it, and that the number is
one you choose. You know a process gets validated before it is paid for with real money, and at what
sample size it starts to say anything (m28). And you can assemble a complete trade end to end,
with the reason written down before the entry instead of after the outcome.

But the most valuable possession of the lot is the one that looks least like a technique: **you can
tell a claim with a mechanism from one without.** It is the question this course has repeated in every
module — which orders are there, who put them there, what forces them to fill — and it is the only one
that keeps working on material this course does not cover, including material written next year.
Techniques expire when the market that produced them changes; the criterion does not.

And now the limit, with the same frankness. The course has not given you experience, and it cannot:
knowing how a thin book behaves at 3 a.m. on a Sunday is not the same as having had a position open at
that hour. What this course has given you is the criteria to accumulate that experience without ruining
yourself while you accumulate it — a size that survives a bad streak, a stop decided before the entry,
a journal that turns a trade into a data point instead of a memory — and that is exactly what separates
someone who will reach a thousand trades from someone who stops at twenty.

:::note{type=info}
This lesson has no exercises, and that is deliberate. Said plainly, because a course that changes its
rules at the end without saying so is worse than one that changes them and says it: everything
else here is examined because everything else can be checked. An epilogue examines nothing. It hands
back the pen.
:::

## The default path: go deeper here

There is one path that requires nothing new, and it is the one this course recommends: stay where you
are and do it more times.

- **Screen time.** None of the reads in this course — an absorption, a sweep, a compression ahead of an
  expansion — is recognised the first time. They are recognised after you have seen them many times,
  including every one that looked like it and was not.
- **The journal, growing.** The journal m27-l2 made you start is the only thing that turns screen
  time into sample, and sample is exactly what m28 demanded before anything could be said about
  your system. Twenty trades cannot tell your edge from a coin flip; two hundred begin to. The distance
  between those two numbers is measured in months, and there is no shortcut past them.
- **Re-reading.** A lesson read before you had traded and re-read afterwards is not the same lesson:
  the second time you have examples of your own to hold it against. The app lets you un-mark a
  completed lesson for exactly this, without losing anything else you have done.

And now the warning that protects everything above, because it is the classic mistake of the day after
finishing a course: the temptation is to look for more tactics. Another pattern, another indicator,
another setup with a name of its own. Notice what that actually is: adding knobs to a system whose
sample has not grown. It is m28's overfitting in human form — the same act of fitting the noise,
performed with a career instead of a spreadsheet — and it has the same symptom: every bad streak
produces a new rule, so no rule ever accumulates the trades it would take to know whether it helped.
More tactics over the same sample is not more system; it is less.

## The two ladders that exist, and are not this one

If at some point you want to climb a genuine step up, there are two ladders, and this course is the first
rung of neither: they are different buildings. Naming them is more use than pretending they are not
there.

### The quantitative ladder

Six areas, one sentence each, none of them taught here:

- **Modelled transaction costs** — the fee, the slippage and the impact your own order has on the
  price, each as a function of order size rather than as a constant — which is what m24 had you
  estimate by hand.
- **Fractional sizing** — what fraction of capital to risk per trade, derived from the measured edge
  instead of fixed by rule, of the kind the Kelly formula gives — over the fixed percentage of m22.
- **Measured microstructure** — the order book and the aggressor flow processed as data series rather
  than read on screen — which is m31 with a history where you had a snapshot.
- **Statistical arbitrage** — two instruments that move together, and the difference between them
  traded when it stretches — the premium of m32 turned into a business.
- **Walk-forward validation** — train on one window, test on the next, advance and repeat — which is
  m28's test half done many times instead of once.
- **Regime classification** — a model that decides what state the market is in before applying the rule
  that belongs to that state — the volatility cycles of m16, measured instead of seen.

The honesty that matters here: it is another profession. Where this course put eyes and process, that
ladder puts code, statistics and data, and all three are learned elsewhere. It is not level two of
this: it is another building, with its own ground floor. What still holds inside it is what always held
— a measured edge, a size that survives the streak, an abandonment criterion written before you need it
— which is why this course comes first even though it does not lead there.

### The other-instruments ladder

The natural neighbour is options. m21-l2 already named them — large expiries concentrate forced
flow into the perpetual — and declared the frontier in the same breath: the mechanics of an option, how
a hedge is sized and why it changes as price moves, are a second course and not a footnote in this one.
That is still true at the end of the course. What changes from one instrument to another is the shape of how
money is made and lost; what does not change is that you have to know, before you open, what you can
lose and what would make you close.

## What you will be swimming against

One thing is left to say, and it is needed the same day you finish the course.

Out there is an entire ecosystem waiting for you: signal groups, VIP channels, people offering to trade
your account, and the course that does promise — the one that puts a number on the win rate this
course has refused to put in any lesson. None of that has to be distrusted on principle. It has to be read
with the tool you already have: ask for the mechanism. Which orders are there, who put them there,
what forces them to fill. A signal that cannot answer that is the same claim without a mechanism that
m34 took apart in the crowd's dialect, wearing a different costume, and it is answered the same
way: if no observation would contradict it, it predicts nothing.

And there is one mechanism you can always read, even when the strategy's own is kept from you: the
mechanism of whoever is selling it to you. Someone who lives off selling you the signal is paid when
you subscribe, not when you win; someone paid a share of the volume you move is paid by your activity,
not by your result. That makes nobody a fraud — a business can be honest and still have its incentives
— but it is a fact, and it is a fact you already know how to read, because it is the same old question
applied to a person instead of to a level. And the whole of that ecosystem is built on the psychology
m26 describes: the hurry, the FOMO, someone else's streak seen up close and your own seen from far
away.

So the course ends where it began, with the process in your hands and in nobody else's. Choose your
timeframe, size from the stop, write before you look, and may the only closing bell you get remain the
one you build yourself.
```
