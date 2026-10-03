# Prose pass 1.2: inventory

Stage A (inventory) and stage B (pilot proposal) of prose pass 1.2. This was taken on 2026-10-03 against
commit `f0d0e68`, with `content/` clean. **Nothing in `content/` was changed.** This file is the only
output.

## Scope and method

**In scope:** lesson prose in `content/{es,en}/lessons/*.md` (44 lessons per locale), plus each lesson's
`summary` in `course.yaml`. The summary is counted as the lesson's last unit and is marked "summary" in the
appendix.

**Out of scope, removed before counting:** headings, tables, `:::note` callouts (treated as `::` blocks),
`::figure` / `::exercise` lines, exercises, YAML other than the lesson summaries, and glossary definitions.
Bold or italic lead-in labels at the start of a paragraph or bullet are structure and are removed before
the sentence is read. Examples: `**Por qué importa:**`, `*En la práctica:*`, `**Qué es.**`.
Blockquoted pull rules (`> **Nada de esto predice la dirección…**`) are prose and are counted.

**Units.** Each paragraph, bullet item, blockquote and summary is split into sentences. Every sentence gets
an id `S###`: the in-scope sentences of one lesson and locale, numbered in reading order. Every hit in this
file quotes its sentence. ES and EN ids usually line up, but they drift where one locale splits a sentence
differently. Inline code counts as one word.

**How each pattern was counted.**

| # | Pattern | How |
|---:|---|---|
| 1 | Filler | Regex for the seed list. It found **0 hits** in either locale: the seed fillers are already gone. The hits come from the additions below. Each candidate was read in context and kept only where deleting it loses nothing. Reviewers also added fillers the regex missed (announcer sentences, "calladamente/quietly"). |
| 2 | Rhythmic triad | Read in context. Not counted: lists of distinct required facts (three prices, a formula's parts), numbered steps and bullet lists. Counted: three parallel frames across consecutive sentences or paragraphs. |
| 3 | Rhetorical question | Every `?` sentence, sorted by hand. **Counted:** questions the author asks and then answers ("¿Por qué pesa tanto esa primera ruptura?"). **Not counted:** questions the reader is told to ask, checklist questions, and quoted questions. |
| 4 | Closer | Read in context. Applied to the last sentence of each paragraph or blockquote with 2+ sentences, to the lesson's last prose sentence, and to the summary's last sentence. Kinds: restate, motivate, editorial ("Ese es el límite honesto."), ahead (scope announcements, figure pointers after the content). |
| 5 | Over 30 words | Mechanical. **Aside-only** means the sentence drops to ≤ 30 words once the text between em-dashes and in parentheses is removed. Those get split, not rewritten. |
| 6 | Stacked hedge | A clause scan for two distinct hedge words in one clause, verified by hand, plus whatever the reviewers found. An ability modal next to a quantifier ("can sweep a level almost at will") does not count. |
| 7 | No solo / not only | Only the amplifying form: "no solo X; (sino) Y" / "not just X — it is Y". The tail contrast "…, no solo durante" / "…, not just the stake" is a plain contrast and is not counted (4 ES, 5 EN). |
| 8 | Repeated opener | Mechanical. The first two words of each paragraph, 3+ paragraphs, **one hit per opener**. Bare labels such as "Una lectura resuelta:" and "Worked example." are excluded. |
| 9 | Coined term | Regex for every seed occurrence, plus reviewer rows for seed variants (estante, charco, pocket) and non-seed terms. Occurrences are counted, not sentences. Seed hits in another sense are excluded (listed in the coined-terms section). |
| 10 | Metaphor then gloss | Read in context: a metaphor explained in the same or the next sentence. |
| 11 | Synonym rotation | Read in context. **One hit per concept per lesson** with 3+ names, attached to the first sid. The variants are in the appendix note. |

Patterns 1, 2, 4, 10, 11, 6 (beyond the clause scan) and the non-seed part of 9 were judged by six parallel
readers, each covering a contiguous block of lessons in both locales. All of them worked to one written brief
that quoted the voice page. Each locale was judged on its own text. Patterns 3, 7 and 8 were sorted by hand
by me. Pattern 5 and the seed part of 9 are mechanical.

**Filler additions** (the seed list found nothing). The phrase counts only where it is an intensifier,
announcer or tag that carries no content:

- ES: *de verdad* (emphatic, not "dinero de verdad"), *honesto / honesta / honestidad* applied to a reading,
  limit, rule, answer or test ("la lectura honesta", "el límite honesto"), *exactamente / precisamente /
  justamente* not pinning a quantity or identity, *simplemente / sencillamente*, *en realidad / realmente*
  (no contrast), *fíjate en que* as an announcer, *nada más / sin más* as a tag, *merece la pena / vale la
  pena*, *literalmente*, *claramente*, *básicamente*, *calladamente*, and announcer sentences ("Pongámosle
  números.", "Aquí está la trampa", "Queda una cosa por decir").
- EN: *actually / really / genuinely / truly* (emphatic), *honest / honestly* on the same objects,
  *exactly / precisely* not pinning a quantity, *simply*, *notice that / note that*, *literally*,
  *basically*, *crucially*, *quietly* (as a tic), and the mirror announcer sentences.
- The biggest groups, ES / EN: **announcer sentences** 78 / 80; **"de verdad" / "actually"** 61 / 52;
  **"honesto" / "honest"** 47 / 49, in 27 lessons, nearly always applied to a reading or a limit;
  **"exactamente" / "exactly"** 44 / 81. EN uses "exactly" where ES often has no adverb at all.

**Density** is hits per 100 in-scope sentences. Pattern 5 is 41% of ES hits and 33% of EN hits. It tracks sentence length
more than voice, so every table also shows density without it.

**Contents:** per-lesson table · per-pattern totals · 10 worst lessons · light-touch lessons ·
course-coined terms · ES vs EN density · absolutes · counting notes · appendix (every hit, quoted) ·
**Pilot proposal** (at the end).

## Per-lesson table

Each cell is **ES·EN**. Pattern numbers follow the brief (1 filler … 11 synonym rotation). Column 5 counts every sentence over 30 words; the aside-only ones are a subset, shown in brackets. Density = hits per 100 sentences, all patterns; "excl. 5" leaves out pattern 5.

| Lesson | 1 | 2 | 3 | 4 | 5 [aside-only] | 6 | 7 | 8 | 9 | 10 | 11 | Total | Sentences | Density | Density excl. 5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| m01-l1 | 12·12 | 1·1 | 0·0 | 3·3 | 25·16 [3·3] | 0·0 | 0·0 | 0·0 | 0·0 | 0·0 | 1·0 | 42·32 | 47·48 | 89.4·66.7 | 36.2·33.3 |
| m02-l1 | 11·11 | 0·0 | 0·0 | 4·4 | 16·7 [1·1] | 0·0 | 0·0 | 1·0 | 0·0 | 0·0 | 1·1 | 33·23 | 90·91 | 36.7·25.3 | 18.9·17.6 |
| m03-l1 | 11·11 | 1·1 | 0·0 | 5·5 | 14·11 [3·2] | 0·0 | 0·0 | 0·0 | 2·2 | 0·0 | 1·2 | 34·32 | 76·76 | 44.7·42.1 | 26.3·27.6 |
| m03-l2 | 5·5 | 1·1 | 0·0 | 4·4 | 19·12 [3·2] | 0·0 | 0·0 | 0·0 | 1·1 | 1·1 | 1·1 | 32·25 | 75·76 | 42.7·32.9 | 17.3·17.1 |
| m04-l1 | 15·16 | 0·0 | 0·0 | 5·5 | 17·11 [3·2] | 0·0 | 0·0 | 0·0 | 3·3 | 1·1 | 3·3 | 44·39 | 67·67 | 65.7·58.2 | 40.3·41.8 |
| m05-l1 | 6·7 | 2·2 | 0·0 | 3·3 | 13·8 [1·1] | 0·0 | 0·0 | 0·0 | 3·3 | 2·1 | 3·3 | 32·27 | 67·67 | 47.8·40.3 | 28.4·28.4 |
| m06-l1 | 3·3 | 1·1 | 0·0 | 4·4 | 14·7 [2·1] | 0·0 | 0·0 | 0·0 | 5·5 | 2·1 | 2·2 | 31·23 | 52·52 | 59.6·44.2 | 32.7·30.8 |
| m07-l1 | 4·4 | 0·0 | 0·0 | 6·6 | 11·5 [3·1] | 0·0 | 0·0 | 0·0 | 1·1 | 1·1 | 1·1 | 24·18 | 59·59 | 40.7·30.5 | 22.0·22.0 |
| m08-l1 | 13·13 | 3·3 | 3·3 | 11·11 | 27·22 [8·7] | 0·0 | 0·0 | 0·0 | 19·19 | 2·2 | 3·4 | 81·77 | 103·103 | 78.6·74.8 | 52.4·53.4 |
| m08-l2 | 8·8 | 2·2 | 0·0 | 5·5 | 11·8 [1·0] | 0·0 | 1·1 | 1·0 | 8·8 | 3·3 | 1·2 | 40·37 | 69·69 | 58.0·53.6 | 42.0·42.0 |
| m09-l1 | 4·4 | 2·2 | 0·0 | 5·5 | 15·8 [3·0] | 0·0 | 0·0 | 0·0 | 4·4 | 0·0 | 1·2 | 31·25 | 87·87 | 35.6·28.7 | 18.4·19.5 |
| m09-l2 | 4·4 | 1·1 | 0·0 | 7·7 | 24·14 [6·1] | 0·0 | 0·0 | 0·0 | 0·0 | 1·1 | 0·0 | 37·27 | 70·70 | 52.9·38.6 | 18.6·18.6 |
| m10-l1 | 9·9 | 0·0 | 0·0 | 8·8 | 22·13 [4·3] | 0·0 | 0·0 | 0·0 | 3·3 | 1·1 | 4·2 | 47·36 | 89·89 | 52.8·40.4 | 28.1·25.8 |
| m11-l1 | 21·22 | 2·2 | 1·1 | 13·13 | 34·21 [4·2] | 0·0 | 0·0 | 0·0 | 4·4 | 0·0 | 4·4 | 79·67 | 118·118 | 66.9·56.8 | 38.1·39.0 |
| m12-l1 | 6·7 | 0·0 | 0·0 | 9·9 | 10·8 [1·0] | 0·0 | 0·0 | 1·0 | 4·4 | 1·1 | 3·2 | 34·31 | 69·69 | 49.3·44.9 | 34.8·33.3 |
| m13-l1 | 4·4 | 1·1 | 2·2 | 1·1 | 14·6 [5·3] | 0·0 | 1·1 | 0·0 | 0·1 | 2·2 | 2·2 | 27·20 | 75·75 | 36.0·26.7 | 17.3·18.7 |
| m14-l1 | 7·6 | 1·1 | 0·0 | 5·5 | 11·9 [3·1] | 1·2 | 0·1 | 0·0 | 2·2 | 0·0 | 2·2 | 29·28 | 65·65 | 44.6·43.1 | 27.7·29.2 |
| m15-l1 | 6·6 | 0·0 | 0·0 | 8·8 | 13·12 [4·5] | 0·0 | 0·0 | 0·0 | 7·6 | 0·0 | 1·1 | 35·33 | 69·69 | 50.7·47.8 | 31.9·30.4 |
| m15-l2 | 2·2 | 1·1 | 0·0 | 5·5 | 10·8 [0·0] | 0·0 | 0·0 | 0·0 | 4·4 | 1·1 | 2·2 | 25·23 | 50·50 | 50.0·46.0 | 30.0·30.0 |
| m16-l1 | 12·12 | 1·1 | 0·0 | 2·2 | 9·9 [1·1] | 0·0 | 0·0 | 0·1 | 3·2 | 1·1 | 0·0 | 28·28 | 65·64 | 43.1·43.8 | 29.2·29.7 |
| m17-l1 | 7·9 | 3·3 | 3·3 | 7·7 | 28·20 [3·2] | 1·0 | 0·0 | 1·0 | 3·3 | 3·3 | 2·2 | 58·50 | 100·99 | 58.0·50.5 | 30.0·30.3 |
| m18-l1 | 11·11 | 4·4 | 0·0 | 8·8 | 18·16 [3·2] | 0·0 | 0·0 | 0·0 | 2·2 | 2·2 | 2·2 | 47·45 | 80·80 | 58.8·56.2 | 36.2·36.2 |
| m19-l1 | 7·8 | 0·0 | 2·2 | 7·7 | 27·22 [3·3] | 0·0 | 1·2 | 0·0 | 17·7 | 3·3 | 4·4 | 68·55 | 94·93 | 72.3·59.1 | 43.6·35.5 |
| m19-l2 | 7·7 | 1·1 | 0·0 | 5·5 | 14·11 [2·2] | 0·0 | 1·1 | 0·0 | 22·22 | 1·1 | 1·1 | 52·49 | 75·75 | 69.3·65.3 | 50.7·50.7 |
| m20-l1 | 8·9 | 2·2 | 0·0 | 5·5 | 15·9 [4·0] | 0·0 | 0·0 | 0·0 | 0·0 | 2·2 | 2·1 | 34·28 | 79·79 | 43.0·35.4 | 24.1·24.1 |
| m21-l1 | 9·11 | 2·2 | 2·2 | 7·7 | 14·9 [0·0] | 0·0 | 0·0 | 0·0 | 0·0 | 1·1 | 1·1 | 36·33 | 72·72 | 50.0·45.8 | 30.6·33.3 |
| m21-l2 | 16·16 | 1·1 | 1·1 | 7·7 | 10·9 [2·2] | 0·0 | 0·1 | 0·0 | 2·3 | 0·0 | 1·1 | 38·39 | 61·61 | 62.3·63.9 | 45.9·49.2 |
| m22-l1 | 14·13 | 0·0 | 0·0 | 9·9 | 26·18 [5·2] | 0·0 | 0·0 | 0·0 | 1·0 | 1·1 | 2·2 | 53·43 | 125·126 | 42.4·34.1 | 21.6·19.8 |
| m22-l2 | 7·7 | 2·2 | 0·0 | 3·3 | 8·7 [1·1] | 0·0 | 0·0 | 0·0 | 4·4 | 0·0 | 1·1 | 25·24 | 52·52 | 48.1·46.2 | 32.7·32.7 |
| m23-l1 | 11·12 | 4·4 | 0·0 | 7·7 | 26·19 [5·3] | 0·0 | 0·0 | 0·0 | 5·5 | 3·3 | 2·2 | 58·52 | 105·105 | 55.2·49.5 | 30.5·31.4 |
| m23-l2 | 17·20 | 5·5 | 0·0 | 6·6 | 16·13 [1·1] | 0·0 | 0·0 | 0·1 | 4·4 | 4·4 | 3·3 | 55·56 | 91·92 | 60.4·60.9 | 42.9·46.7 |
| m24-l1 | 12·11 | 0·0 | 0·0 | 7·7 | 21·14 [3·1] | 0·0 | 0·0 | 0·0 | 0·0 | 0·0 | 1·0 | 41·32 | 77·77 | 53.2·41.6 | 26.0·23.4 |
| m25-l1 | 7·7 | 1·1 | 0·0 | 6·6 | 12·9 [1·0] | 0·0 | 0·0 | 0·0 | 0·0 | 0·0 | 1·1 | 27·24 | 81·84 | 33.3·28.6 | 18.5·17.9 |
| m26-l1 | 16·16 | 4·4 | 0·0 | 7·7 | 20·16 [3·2] | 0·0 | 0·0 | 0·0 | 3·3 | 6·6 | 1·1 | 57·53 | 95·96 | 60.0·55.2 | 38.9·38.5 |
| m27-l1 | 13·12 | 2·2 | 0·0 | 6·6 | 22·16 [5·3] | 0·0 | 0·0 | 0·0 | 9·5 | 3·2 | 4·4 | 59·47 | 102·102 | 57.8·46.1 | 36.3·30.4 |
| m27-l2 | 10·10 | 0·0 | 0·0 | 4·4 | 15·10 [2·1] | 0·0 | 0·0 | 0·0 | 0·0 | 3·3 | 1·1 | 33·28 | 62·64 | 53.2·43.8 | 29.0·28.1 |
| m28-l1 | 18·21 | 0·0 | 0·0 | 5·5 | 12·13 [0·1] | 0·0 | 0·0 | 0·0 | 0·0 | 1·1 | 1·1 | 37·41 | 81·81 | 45.7·50.6 | 30.9·34.6 |
| m29-l1 | 9·10 | 1·1 | 0·0 | 5·5 | 8·4 [1·0] | 0·0 | 0·1 | 0·0 | 4·4 | 0·0 | 1·1 | 28·26 | 78·78 | 35.9·33.3 | 25.6·28.2 |
| m30-l1 | 10·10 | 2·2 | 0·0 | 8·8 | 10·9 [1·1] | 0·0 | 0·0 | 0·0 | 5·5 | 0·0 | 1·1 | 36·35 | 74·74 | 48.6·47.3 | 35.1·35.1 |
| m31-l1 | 11·14 | 2·2 | 0·0 | 8·8 | 17·10 [2·2] | 0·0 | 0·0 | 0·0 | 1·1 | 1·1 | 1·0 | 41·36 | 70·70 | 58.6·51.4 | 34.3·37.1 |
| m32-l1 | 5·6 | 1·1 | 0·0 | 4·4 | 12·8 [1·1] | 0·0 | 0·0 | 0·0 | 0·0 | 0·0 | 0·0 | 22·19 | 53·53 | 41.5·35.8 | 18.9·20.8 |
| m33-l1 | 9·9 | 1·1 | 0·0 | 6·6 | 17·13 [1·2] | 0·0 | 0·0 | 0·0 | 0·0 | 0·0 | 0·0 | 33·29 | 55·55 | 60.0·52.7 | 29.1·29.1 |
| m34-l1 | 9·12 | 1·1 | 0·0 | 8·8 | 26·20 [2·0] | 0·0 | 0·0 | 0·0 | 18·18 | 1·1 | 2·2 | 65·62 | 103·104 | 63.1·59.6 | 37.9·40.4 |
| m35-l1 | 10·10 | 4·4 | 0·0 | 7·7 | 19·19 [1·1] | 0·0 | 0·0 | 0·0 | 2·2 | 1·1 | 1·1 | 44·44 | 57·57 | 77.2·77.2 | 43.9·43.9 |

## Per-pattern course totals

| # | Pattern | ES | EN | Lessons with ≥1 hit (ES·EN) |
|---:|---|---:|---:|---|
| 1 | Filler | 416 | 437 | 44·44 |
| 2 | Rhythmic triad | 63 | 63 | 33·33 |
| 3 | Rhetorical question | 14 | 14 | 7·7 |
| 4 | Summary/uplift closer | 265 | 265 | 44·44 |
| 5 | Sentence over 30 words (aside-only: 111·69) | 742 | 529 | 44·44 |
| 6 | Stacked hedge | 2 | 2 | 2·1 |
| 7 | No solo / not only | 4 | 8 | 4·7 |
| 8 | Repeated paragraph opener | 4 | 2 | 4·2 |
| 9 | Course-coined term | 175 | 160 | 32·32 |
| 10 | Metaphor then gloss | 55 | 52 | 29·29 |
| 11 | Synonym rotation | 72 | 69 | 40·37 |
| | **All patterns** | **1812** | **1601** | |

Sentences in scope: ES 3384, EN 3393. Course density: ES 53.5, EN 47.2 hits per 100 sentences; without pattern 5, ES 31.6, EN 31.6.

## The 10 worst lessons by density

Ranked by combined density (ES+EN hits ÷ ES+EN sentences × 100), all patterns. The "excl. 5" rank leaves out long sentences, which dominate the raw count.

| Rank | Lesson | Density (ES+EN) | ES | EN | Density excl. 5 | Rank excl. 5 |
|---:|---|---:|---:|---:|---:|---:|
| 1 | m01-l1 | 77.9 | 89.4 | 66.7 | 34.7 | 15 |
| 2 | m35-l1 | 77.2 | 77.2 | 77.2 | 43.9 | 5 |
| 3 | m08-l1 | 76.7 | 78.6 | 74.8 | 52.9 | 1 |
| 4 | m19-l2 | 67.3 | 69.3 | 65.3 | 50.7 | 2 |
| 5 | m19-l1 | 65.8 | 72.3 | 59.1 | 39.6 | 8 |
| 6 | m21-l2 | 63.1 | 62.3 | 63.9 | 47.5 | 3 |
| 7 | m04-l1 | 61.9 | 65.7 | 58.2 | 41.0 | 7 |
| 8 | m11-l1 | 61.9 | 66.9 | 56.8 | 38.6 | 11 |
| 9 | m34-l1 | 61.4 | 63.1 | 59.6 | 39.1 | 9 |
| 10 | m23-l2 | 60.7 | 60.4 | 60.9 | 44.8 | 4 |

### m01-l1

- **Rhythmic triad** (ES S028): «El valor en cripto viene de los mismos sitios aburridos de siempre: demanda por un uso real (la red hace algo que la gente quiere de verdad: una forma fiable de mover valor, un mercado que funciona, una plataforma sobre la que otros construyen), escasez creíble (la oferta es limitada *y* el límite es genuinamente difícil de cambiar; una escasez que el equipo puede deshacer a voluntad no es escasez) y efectos de red (una cadena sobre la que ya construye y contra la que ya cotiza todo el mundo es difícil de desplazar, porque su utilidad crece con el número de personas que la usan).»
- **Summary/uplift closer** (EN S032): «Never confuse the two.»
- **Filler** (ES S022): «Altcoins es literalmente todo lo que no es Bitcoin: desde plataformas serias con uso real hasta tokens que existen solo para vendértelos.»

### m35-l1

- **Course-coined term** (ES S048): «Una señal que no puede contestar eso es la misma afirmación sin mecanismo que m34 desmontó en el dialecto de la masa, con otro disfraz, y se responde igual: si ninguna observación la contradice, no predice nada.»
- **Metaphor then gloss** (EN S024): «Notice what that actually is: adding knobs to a system whose sample has not grown.»
- **Rhythmic triad** (ES S023): «Otro patrón, otro indicador, otro setup con nombre propio.»

### m08-l1

- **Course-coined term** (ES S068): «Una escalera, dos clases de ruptura.»
- **Rhetorical question** (EN S047): «Why bother naming the staircase?»
- **Metaphor then gloss** (ES S012): «Un soporte no es magia en el número: es un estante de órdenes de compra en reposo que las últimas visitas enseñaron a la gente a dejar.»

### m19-l2

- **Course-coined term** (ES S036): «Se carga el combustible.»
- **Metaphor then gloss** (EN S013): «Below a recent low sits a shelf of long stop-losses — a long's protective sell order goes *just under* the low that "should hold.»
- **Rhythmic triad** (ES S019): «El mínimo obvio, el número redondo, el nivel que aguantó dos veces: ahí es donde "pon tu stop justo pasado ese punto" envía miles de órdenes al mismo puñado de ticks.»

### m19-l1

- **Course-coined term** (ES S048): «La lectura honesta es "preparado para un desagüe violento", no "súmate a los ganadores".»
- **Rhetorical question** (EN S037): «How big is the payment?»
- **Metaphor then gloss** (ES S058): «Así que una prima sostenida es un termómetro de la manía del apalancamiento: largos concurridos pagando por el privilegio, con la factura de funding a juego.»

### m21-l2

- **Course-coined term** (ES S052): «Aquí se cierran dos costuras, y se cierran fuerte:»
- **Rhetorical question** (EN S038): «So why do dated contracts and options expiries move the perp?»
- **Rhythmic triad** (ES S040): «Un contrato con fecha converge al spot cuando vence, y todo lo construido sobre la diferencia entre él y el perpetuo —operaciones de carry, spreads de calendario, toda m21-l1— hay que cerrarlo o rolarlo en ese momento.»

### m04-l1

- **Course-coined term** (ES S044): «El amarre no es magia; es un incentivo pagado.»
- **Metaphor then gloss** (EN S039): «A traditional future has a built-in anchor: at expiry it *must* equal spot, or there is free money, so arbitrage drags the two together as the date approaches.»
- **Summary/uplift closer** (ES S044): «El amarre no es magia; es un incentivo pagado.»

### m11-l1

- **Course-coined term** (ES S115): «Un oscilador que coincide con un nivel que ya vigilabas vale mucho más que uno que grita en espacio abierto.»
- **Rhetorical question** (EN S022): «Why is a *difference of averages* a momentum read at all?»
- **Rhythmic triad** (ES S059): «Es frecuente, salta a menudo y puede ocurrir muchas veces dentro de una misma tendencia sin que la tendencia esté nunca en duda.»

### m34-l1

- **Course-coined term** (ES S095): «El dialecto no se gana una excepción; se gana la misma prueba.»
- **Metaphor then gloss** (EN S053): «m08-l1 taught you the ladder — higher highs and higher lows — and named the break that ends it: the change of character, CHoCH, the first lower low in an uptrend.»
- **Rhythmic triad** (ES S076): «Puedes discutirlo, comprobarlo y equivocarte con él.»

### m23-l2

- **Course-coined term** (ES S027): «Una repisa en 25.900 (m03-l2, m08-l1) está en 25.900 en el diario, en el de 1h y en el de 1 minuto.»
- **Metaphor then gloss** (EN S005): «It has its frame's opinion.**»
- **Rhythmic triad** (ES S074): «Dirección, estructura y los niveles que importan.»

## Light-touch lessons

**No lesson has fewer than 3 hits in either locale**, with or without pattern 5. The lowest totals (ES·EN hits, density):

- m32-l1: 22·19 hits, density 41.5·35.8 (excl. 5: 10·11)
- m07-l1: 24·18 hits, density 40.7·30.5 (excl. 5: 13·13)
- m13-l1: 27·20 hits, density 36.0·26.7 (excl. 5: 13·14)
- m15-l2: 25·23 hits, density 50.0·46.0 (excl. 5: 15·15)
- m22-l2: 25·24 hits, density 48.1·46.2 (excl. 5: 17·17)
- m25-l1: 27·24 hits, density 33.3·28.6 (excl. 5: 15·15)

## Course-coined terms

Pattern 9 in full. The seed terms come first, then every other term the readers found used as a term with no standard meaning outside the course. Lesson ids are display ids, and ×N gives occurrences. **Bold** in Notes marks a coupling that makes the replacement more than a prose edit.

### Seed terms

| Term (ES / EN) | ES hits | ES lessons | EN hits | EN lessons | Proposed replacement | Notes |
|---|---:|---|---:|---|---|---|
| lente / lens | 7 | m09-l1, m14-l1, m17-l1, m27-l1, m29-l1×2, m30-l1 | 7 | m09-l1, m14-l1, m17-l1, m27-l1, m29-l1×2, m30-l1 | «lectura», «contexto» or «otra fuente / otra lectura independiente» by sentence (decisions table: «lectura» / «forma de leer el gráfico»). EN «read», «context», «independent input». |  |
| escalera / staircase, ladder (HH/HL trend) | 19 | m03-l1, m03-l2, m08-l1×11, m23-l2, m34-l1×5 | 19 | m03-l1, m03-l2, m08-l1×11, m23-l2, m34-l1×5 | «secuencia de máximos y mínimos crecientes/decrecientes» or «estructura» (decisions table). EN «sequence of higher highs and higher lows», «structure». | m08-l1 owns 11 of the hits and **names** it on purpose (S047). The figure-coupling note for `fig-m08-market-structure` says «a staircase you could describe to somebody over the phone», which is YAML, not prose, but it should change with the prose. EN m08-l1 switches from «staircase» to «ladder» at S067 while ES keeps «escalera». |
| repisa, estante / shelf | 17 | m06-l1, m08-l1×4, m15-l1, m17-l1, m19-l2×9, m23-l2 | 18 | m06-l1, m08-l1×4, m13-l1, m15-l1, m17-l1, m19-l2×9, m23-l2 | S/R sense: «zona» / «nivel» (decisions table: «nivel» / «zona de consolidación»). Stop-cluster sense (m19-l2): «cúmulo de stops». Liquidation sense (m17-l1, m19-l2 S047): «cúmulo de precios de liquidación». | ES rotates «repisa» (m06, m17, m19-l2, m23-l2) and «estante» (m08-l1, m15-l1). EN always says «shelf», plus m13-l1, where ES says «soporte antiguo». There are three senses: S/R zone, stop cluster, and liquidation cluster. |
| flujo forzado / forced flow | 12 | m06-l1×3, m09-l1, m19-l1×5, m19-l2×2, m35-l1 | 13 | m06-l1×3, m09-l1, m19-l1×5, m19-l2×2, m21-l2, m35-l1 | «flujo de liquidaciones» / «ventas (compras) forzadas» (decisions table). EN «liquidation flow», «forced selling / forced buying». | m16-l1 «participante forzado / órdenes forzadas» was judged standard and is not counted. ES also writes «flujo forzoso» (m06-l1). |
| bolsa de liquidez / liquidity pool (stop-cluster sense) | 11 | m15-l1, m16-l1, m19-l2×6, m23-l1, m34-l1×2 | 11 | m15-l1, m16-l1, m19-l2×6, m23-l1, m34-l1×2 | «cúmulo de stops» (decisions table). EN «stop cluster». | Variants: ES «charco» (m09-l1), «bolsa de stops / de órdenes de venta en reposo / de liquidaciones de cortos»; EN «pocket» (m15-l1, m16-l1, m23-l1, m34-l1), «pool of forced sell orders». m19-l2 / m16-l1 «bolsa finita de posiciones atrapadas» stretches the term to the trapped positions. m32-l1 «bolsa de capital / de compradores» is the ordinary sense and is not counted. |
| combustible / fuel | 12 | m03-l1, m08-l1, m12-l1, m14-l1, m17-l1, m19-l1×2, m19-l2×4, m31-l1 | 12 | m03-l1, m08-l1, m12-l1, m14-l1, m17-l1, m19-l1×2, m19-l2×4, m31-l1 | Name what is meant, which differs by lesson: «volumen / participación» (m03-l1, m14-l1), «stops y órdenes de ruptura» (m08-l1), «posicionamiento apalancado concurrido / interés abierto nuevo» (m17, m19), «el libro / la liquidez en reposo» (m31-l1). «Se queda sin combustible» (m12-l1) → «pierde momentum». | There are four senses in eight lessons, which is the main argument for replacing it. The glossary's heatmap definition also says «combustible / fuel», and the round-6 definitions deliberately avoided it. |

### Other course-coined terms (additions to the seed)

| Term (ES / EN) | ES hits | ES lessons | EN hits | EN lessons | Proposed replacement | Notes |
|---|---:|---|---:|---|---|---|
| asomo / the poke | 3 | m08-l1×3 | 3 | m08-l1×3 | «la primera vela que cruza el nivel», «la ruptura inicial» / «the first candle through the level», «the initial break» |  |
| amarre, correa / tether (funding) | 3 | m04-l1×2, m07-l1 | 3 | m04-l1×2, m07-l1 | «el funding mantiene el perpetuo cerca del spot» / «funding keeps the perp close to spot» | ES also rotates «ancla». |
| lado tranquilo / quiet side | 1 | m04-l1 | 1 | m04-l1 | «el lado contrario a la mayoría», «el lado que cobra el funding» / «the uncrowded side» |  |
| precio de entrada / price of admission; eviction line (margins) | 2 | m05-l1×2 | 2 | m05-l1×2 | «lo que pagas para abrir» / «umbral de liquidación» — «what it costs to open» / «liquidation threshold» | ES «precio de entrada» collides with entry price, which the same lesson uses in S005–S006. |
| riesgo por acierto / risk per correct call | 1 | m05-l1 | 1 | m05-l1 | «riesgo por operación» / «risk per trade» |  |
| distancia de supervivencia / survival distance | 1 | m06-l1 | 1 | m06-l1 | «distancia hasta la liquidación» / «distance to liquidation» |  |
| overrun | 6 | m08-l2×6 | 6 | m08-l2×6 | «vela envolvente», «vela de impulso / de cuerpo amplio» / «engulfing», «wide-range candle» | **Glossary entry `g-overrun`** (origin m08-l2). Replacing it means renaming or removing the entry in the same change (never-coins guard). |
| espacio abierto / open space | 6 | m08-l2×2, m11-l1, m12-l1×3 | 6 | m08-l2×2, m11-l1, m12-l1×3 | «lejos de cualquier nivel», «en mitad del rango» / «away from any level», «mid-range» | Also used in summaries. |
| firma / signature (MA regime) | 3 | m10-l1×3 | 3 | m10-l1×3 | «lo que muestra cada régimen», «las tres lecturas» / «what each regime looks like», «the three reads» | One word, two senses within m10-l1. |
| bache de momentum / momentum wobble | 3 | m11-l1×3 | 3 | m11-l1×3 | «cambio de momentum a corto plazo» / «short-term momentum shift» | Also in a glossary definition (the MACD entry). |
| cosecha / harvest (stops) | 2 | m09-l1×2 | 2 | m09-l1×2 | «barrer los stops» / «sweep the stops» | Borderline: one lesson. |
| ritmo / rhythm (as a term) | 8 | m15-l1×4, m15-l2×4 | 8 | m15-l1×4, m15-l2×4 | «pendiente», «ritmo de subida» / «slope», «rate of advance» | Only the noun-term use is counted, not «ritmo constante de avance». |
| squeeze de liquidez / liquidity squeeze | 2 | m16-l1×2 | 1 | m16-l1 | «short squeeze», «cascada de liquidaciones» / «liquidation cascade» | Standard «liquidity squeeze» means a funding or credit crunch, so this is a wrong sense rather than an invented word. |
| zona contraria / contrarian zone | 2 | m18-l1×2 | 2 | m18-l1×2 | «extremo de sentimiento» / «sentiment extreme» | Also in the summary. |
| desagüe (ES only) | 1 | m19-l1 | 0 | — | «cascada de liquidaciones», «barrido de largos» | EN «flush» is standard. |
| concurrido (ES only; calque of «crowded») | 10 | m15-l1, m19-l1×9 | 0 | — | «saturado» (m18-l1 ES already says «lado saturado») | **Reviewers disagreed.** b3 counted it, b4 did not (m19-l2), and the glossary's g-funding and g-squeeze definitions use it. Counted only in m15-l1 and m19-l1. Your call: if it stays, drop 10 ES hits. |
| arder / burn | 1 | m19-l2 | 1 | m19-l2 | name the event: «cascada de liquidaciones» / «liquidation cascade» | An extension of «combustible». |
| desposicionamiento / un-positioning | 1 | m21-l2 | 1 | m21-l2 | «el cierre de posiciones» / «the unwind» | The same lesson says «deshacer / unwound» at S039. |
| costuras / seams (module links) | 1 | m21-l2 | 1 | m21-l2 | «Esto conecta con dos módulos anteriores» / «This connects to two earlier modules» | Also in m23-l2 (not counted there). |
| freno diario (ES only) | 5 | m22-l1, m27-l1×4 | 0 | — | «límite de pérdida diaria» (or «stop diario») | **Glossary entry `g-daily-stop`** (ES term «freno diario», origin key m24-l1 = m27-l1), also in the g-overtrading definition and the m27-l1 summary and heading. EN «daily stop» is standard and stays. Changing the ES term is a glossary + m22-l1 + m27-l1 + summary change in one go. |
| apuesta con N trajes / bet wearing N costumes | 4 | m22-l2×4 | 4 | m22-l2×4 | «una sola apuesta repartida en N posiciones» / «one bet split across N positions» | Also in the summary. |
| peaje / toll (fees) | 4 | m23-l1×4 | 4 | m23-l1×4 | «comisiones y spread» / «fees and spread» | Also once in m19-l1 (not counted). |
| marco macro / micro — macro / micro frame | 4 | m27-l1×4 | 4 | m27-l1×4 | «temporalidad superior / inferior» / «higher / lower timeframe», which the same lesson already uses at S014 | There are lead-in labels «Marco macro → / Marco micro →» too (structure, not counted, but they would change with it). |
| yo del momento / in-the-moment self | 3 | m26-l1×3 | 3 | m26-l1×3 | «tú en caliente» (vs «tú en frío») / «you in a hot state» |  |
| ir de compras (con pasos intermedios) / timeframe shopping (with extra steps) | 2 | m23-l2×2 | 2 | m23-l2×2 | «buscar la temporalidad que te dé la razón» / «confirmation bias across timeframes» | EN «timeframe shopping» is borderline slang. ES «ir de compras» and «con pasos intermedios» (from the «with extra steps» meme) are calques. |
| zona de origen (del impulso) / (the impulse's) origin zone | 4 | m34-l1×4 | 4 | m34-l1×4 | «order block» (the lesson already maps it), or «zona de demanda/oferta» / «demand/supply zone» | **Glossary entry `g-origin-zone`** (origin key m30-l1 = m34-l1), with order block as its alias. m34-l1 coins it on purpose («aquí la llamamos…»). This is a decision about the SMC lesson's whole stance, not a word swap. |
| dialecto / dialect (SMC vocabulary) | 8 | m34-l1×7, m35-l1 | 8 | m34-l1×7, m35-l1 | «SMC», «la terminología SMC» / «SMC terminology» | There are 10 uses in glossary definitions (the SMC entries). |
| estocada / stab (spring) | 3 | m29-l1, m30-l1×2 | 3 | m29-l1, m30-l1×2 | «ruptura breve bajo el soporte», «shakeout» / «brief break below support» |  |
| una capa más cerca de las operaciones / one layer closer to the trades | 3 | m29-l1, m30-l1×2 | 3 | m29-l1, m30-l1×2 | «medida sobre las operaciones ejecutadas, no sobre el precio» / «measured on executed trades, not on price» |  |



### Seed words in another sense (not counted)

- **escalera / ladder**: «escalera de profundidad / de precios», «depth / price ladder» = the DOM, which is a standard term (m29-l1 S064, m31-l1 S051, S056); the career «dos escaleras… primer peldaño» in m35-l1 (S027, S037); the BTC → ETH → alts rotation «se baja toda la escalera / el siguiente peldaño» in m17-l1 (S034, S056) (a one-off figure, but «curva de riesgo», which the lesson already uses at S040, would do); EN-only «declare the ladder proven» = the A/B/C grading scale in m27-l2 (S039), where ES says «escala».
- **bolsa / pool**: «bolsa de capital / de compradores», «pool of capital / of buyers» in m32-l1 is the ordinary sense.
- **forzado / forced**: «venta forzada / forced selling» (m09-l1, m34-l1, m35-l1) and «participante forzado / órdenes forzadas» (m16-l1) are standard and are not counted.

### Looked at and not counted as coined

«tell / pista», «price magnet / imán», «coil», «risk dial / mando del riesgo» (counted as metaphor + gloss where glossed), «termómetro / thermometer» (a repeated metaphor, counted as M where glossed), «botón de entrada», «factura que aún no ha llegado», «mecánica / mechanic» as a countable noun (watch it: m08-l2, m34-l1, m35-l1), «lado impaciente / impatient side» (close to Harris-style microstructure usage), «prima entre exchanges», «punto de cruce», «Delta neutral no es margen neutral».

## ES vs EN density

**No lesson differs by more than 2×** between locales, with or without pattern 5. The largest gaps (all patterns):

| Lesson | ES | EN | Ratio | Main driver |
|---|---:|---:|---:|---|
| m02-l1 | 36.7 | 25.3 | 1.45 | Sentence over 30 words (+9 ES vs EN) |
| m09-l2 | 52.9 | 38.6 | 1.37 | Sentence over 30 words (+10 ES vs EN) |
| m13-l1 | 36.0 | 26.7 | 1.35 | Sentence over 30 words (+8 ES vs EN) |
| m06-l1 | 59.6 | 44.2 | 1.35 | Sentence over 30 words (+7 ES vs EN) |
| m01-l1 | 89.4 | 66.7 | 1.34 | Sentence over 30 words (+9 ES vs EN) |
| m07-l1 | 40.7 | 30.5 | 1.33 | Sentence over 30 words (+6 ES vs EN) |

Course-wide, ES carries 742 long sentences against EN's 529; that is the only systematic locale difference.

## Absolutes for manual review

Every lesson with nunca / siempre / debe (ES, counting debe, debes, deben, debería, deberías, deberían) or never / always / must (EN) in a prose or summary sentence. Counts are sentences (occurrences in brackets). The sentences are quoted per lesson in the appendix under "A".

| Lesson | ES sentences [occ.] | ES words | EN sentences [occ.] | EN words |
|---|---:|---|---:|---|
| m01-l1 | 3 [3] | siempre 2, nunca 1 | 2 [2] | never 2 |
| m02-l1 | 8 [10] | nunca 6, siempre 3, debes 1 | 7 [7] | never 6, always 1 |
| m03-l1 | 2 [2] | nunca 1, siempre 1 | 2 [2] | never 1, always 1 |
| m03-l2 | 3 [3] | siempre 2, nunca 1 | 3 [3] | always 2, never 1 |
| m04-l1 | 9 [11] | nunca 9, siempre 1, deberías 1 | 11 [12] | never 10, must 1, always 1 |
| m05-l1 | 5 [5] | nunca 2, debes 2, siempre 1 | 5 [5] | never 2, must 2, always 1 |
| m06-l1 | 2 [2] | debes 1, nunca 1 | 2 [2] | must 1, never 1 |
| m07-l1 | 3 [3] | nunca 3 | 4 [4] | never 3, always 1 |
| m08-l1 | 2 [3] | nunca 2, siempre 1 | 3 [4] | never 3, always 1 |
| m08-l2 | 4 [4] | siempre 2, nunca 2 | 3 [3] | never 2, always 1 |
| m09-l1 | 1 [1] | nunca 1 | 1 [1] | never 1 |
| m09-l2 | 2 [2] | siempre 1, nunca 1 | 3 [3] | never 2, always 1 |
| m10-l1 | 8 [9] | siempre 4, nunca 4, debe 1 | 8 [10] | always 4, never 4, must 2 |
| m11-l1 | 10 [10] | nunca 8, debería 2 | 9 [9] | never 9 |
| m12-l1 | 5 [5] | nunca 2, debe 1, siempre 1, debería 1 | 3 [3] | never 2, always 1 |
| m13-l1 | 3 [3] | nunca 2, siempre 1 | 3 [3] | must 1, always 1, never 1 |
| m14-l1 | 2 [2] | debería 1, nunca 1 | 1 [1] | never 1 |
| m15-l1 | 3 [3] | nunca 3 | 3 [3] | never 3 |
| m16-l1 | 1 [1] | nunca 1 | 1 [1] | never 1 |
| m17-l1 | 5 [5] | nunca 4, siempre 1 | 6 [8] | never 4, must 3, always 1 |
| m18-l1 | 6 [6] | nunca 3, debes 1, siempre 1, deberías 1 | 5 [6] | never 4, always 1, must 1 |
| m19-l1 | 5 [5] | nunca 4, deberías 1 | 5 [6] | never 5, must 1 |
| m19-l2 | 5 [6] | nunca 3, deben 2, debería 1 | 3 [4] | must 2, never 2 |
| m20-l1 | 1 [1] | nunca 1 | 1 [1] | never 1 |
| m21-l1 | 2 [2] | nunca 1, siempre 1 | 1 [1] | never 1 |
| m21-l2 | 5 [5] | nunca 3, siempre 2 | 3 [3] | never 3 |
| m22-l1 | 5 [5] | nunca 4, debes 1 | 6 [7] | never 5, must 2 |
| m22-l2 | 1 [1] | nunca 1 | 1 [1] | never 1 |
| m23-l1 | 6 [8] | siempre 4, nunca 3, debe 1 | 5 [7] | always 4, never 3 |
| m23-l2 | 4 [4] | nunca 3, siempre 1 | 4 [4] | never 3, always 1 |
| m24-l1 | 10 [11] | nunca 7, debe 2, siempre 1, debería 1 | 9 [9] | never 8, always 1 |
| m25-l1 | 8 [8] | nunca 4, debes 1, debe 1, deberías 1, siempre 1 | 7 [7] | never 4, must 2, always 1 |
| m26-l1 | 15 [16] | nunca 10, siempre 4, debes 1, debe 1 | 12 [13] | never 8, always 4, must 1 |
| m27-l1 | 8 [8] | nunca 6, siempre 2 | 7 [7] | never 5, always 1, must 1 |
| m27-l2 | 6 [8] | nunca 7, siempre 1 | 6 [9] | never 8, always 1 |
| m28-l1 | 6 [7] | nunca 4, siempre 2, debería 1 | 6 [6] | never 5, always 1 |
| m29-l1 | 3 [4] | nunca 3, siempre 1 | 3 [4] | never 3, always 1 |
| m30-l1 | 1 [1] | debería 1 | 1 [1] | must 1 |
| m31-l1 | 1 [1] | nunca 1 | 2 [2] | must 1, never 1 |
| m32-l1 | 2 [2] | debería 1, nunca 1 | 1 [1] | never 1 |
| m33-l1 | 3 [3] | siempre 2, debería 1 | 3 [4] | always 2, must 2 |
| m34-l1 | 7 [7] | nunca 4, siempre 3 | 9 [9] | never 6, always 3 |
| m35-l1 | 3 [3] | siempre 3 | 2 [2] | always 2 |

Total: ES 194 sentences, EN 182 sentences, in 44 lessons.

## Counting notes: what I was unsure how to count

**Extraction**
- **Lead-ins that are half a sentence.** Some labels run straight into the sentence:
  `**Por qué una regla mecánica y no criterio:** por *quién* tendría…` (m27-l1 and others). The label
  is removed, so the sentence is counted from «por *quién*…». This shortens it, so no false long hit.
- **Missed splits before a module id.** The splitter needs a capital letter after the full stop, so 19
  sentence pairs where the second opens with a module id («…su propio estado. m26's answer…») are counted
  as one sentence. The 8 that were long only because of this were dropped from pattern 5. Sentence counts
  run about 0.3% low.
- **Bold lead-ins hide a few hits.** Labels are structure by the brief, so a filler or coined word inside
  a label is not counted: m11-l1 «El funding es la pista de agotamiento más honesta», m03-l2 «El
  apalancamiento amontonado añade combustible», m27-l1 «Marco macro → / Marco micro →». They still change
  if the term changes.
- **`:::note` callouts** are treated as the `::` blocks the brief puts out of scope. Some of them carry
  coined terms (m22-l1 «punto de cruce») that a term sweep should still touch.

**Judgement calls**
- **m05-l1 S014 «…nada más»** sits in the voice page's reference paragraph. The reviewer marked it as
  filler under the «nada más as a tag» rule. I overrode that and **did not count it**: the reference
  paragraph defines the voice. The other «nada más» tags stand.
- **Scope announcements** («El objetivo de esta lección es…», «Esta lección recorre…», «Este módulo
  trata de…») are counted as closers (ahead) when they end the opening paragraph. If you want lesson intros
  to keep a scope sentence, that is about 1 hit per lesson to discount.
- **Figure pointers** that end a paragraph after the content are counted as closers (ahead). A pointer
  that also adds a fact is not.
- **Closers vs rules.** A short final sentence that states a rule («En cuanto la escalera se detiene, se
  detiene también la suposición») was sometimes counted as editorial. I let it stand where the rule repeats
  the paragraph. Treat pattern 4 as the noisiest judged pattern, ±10%.
- **«exactamente / exactly».** These were not counted where they pin a quantity, an identity («los dos
  paneles son el mismo gráfico» is the m08-l1 figure guard, see the pilot) or an execution detail («por
  dónde entro exactamente»).
- **«concurrido».** b3 counted it as a calque of «crowded» (10 ES hits) and b4 did not (m19-l2). It is
  inconsistent across batches. Decide, then either drop those 10 or add m19-l2's.
- **Synonym rotation.** This is one hit per concept per lesson, so a lesson with four names for a stop
  cluster scores the same as one with three. The variants are in the appendix notes.
- **Repeated openers.** «Un exchange…» ×3 (m02-l1) and «Una divergencia…» ×4 (m12-l1) are the term as
  subject of its own definition. They are counted as the mechanical rule says, but they are probably fine
  under the voice page («repeating "precio" five times is fine»). The bare labels «Una lectura resuelta:»
  ×4 (m11-l1), «Desarróllalo.» (m11-l1) and «Worked example.» ×3 (m24-l1) were excluded as structure. Flag
  them if you consider them openers.
- **m35-l1 «Sabes… / Sabes… / Sabes… / Y sabes…»** is four bullets, so it is not a paragraph opener. It is
  counted once as a triad (same frame).
- **Hedges** are almost absent: 2 per locale course-wide. The course over-asserts rather than
  over-hedges, which is why the absolutes list matters more.

**Out of scope but found while reading (not counted, not fixed)**
- **m11-l1 S098, both locales: probable content error.** «ponerte corto contra una tendencia bajista
  fuerte porque "el RSI está en sobreventa"» / «shorting into a strong downtrend because "RSI is
  oversold"». The mirror of selling overbought into an uptrend is **buying** oversold into a downtrend.
  Oversold is no reason to short.
- m12-l1 ES: «seguir subiendo **e** mostrar una tercera» → «y mostrar».
- m17-l1 ES: «asumiendo riesgos **riesgo**» (doubled word).
- m10-l1 S077, both locales: «la misma moneda / the same coin» is a truncated idiom («las dos caras de la
  misma moneda»).

## Appendix — every hit, per lesson

Sentence ids (`S###`) number the in-scope sentences of that lesson and locale in reading order, lesson summary last; EN ids drift from ES where a paragraph splits differently. Pattern 9 counts occurrences, so a sentence with two coined words appears twice. "A" lists the absolutes (not a pattern; not in the counts).

### m01-l1

**ES** — 42 hits, 47 sentences, density 89.4

- **1 Filler** (12)
  - S002 [other filler: "genuinamente útiles"] «Cripto no es dinero mágico de internet ni es una estafa por definición: es un conjunto de tecnologías con propiedades concretas, algunas genuinamente útiles y otras vendidas muy por encima de su valor.»
  - S003 [de verdad: emphatic ("¿qué respalda esto?")] «El objetivo de esta lección es darte un modelo mental que funcione, para que cuando alguien te agite después un gráfico o una "narrativa" delante puedas hacer la única pregunta que importa: *¿qué respalda esto de verdad?*»
  - S009 [En la práctica: introduces an illustration, no theory contrast] «En la práctica, nadie puede "llamar a Bitcoin" y pedir que se duplique la emisión; cambiar una regla básica exige convencer a toda la red, algo lento y raro por diseño.»
  - S015 [exactamente: emphatic "exactamente así"] «Así que pierde la clave y las monedas quedan congeladas para siempre (millones de BTC se han perdido exactamente así); fíltrala y te las roban al instante, sin nada que revertir.»
  - S021 [En la práctica: tic, no theory contrast] «En la práctica, casi todas las demás monedas se cotizan y se miden mentalmente contra BTC: cuando alguien dice que "las alts sangran contra Bitcoin", quiere decir que BTC aguanta su valor mientras el resto caen respecto a él.»
  - S022 [literalmente: intensifier] «Altcoins es literalmente todo lo que no es Bitcoin: desde plataformas serias con uso real hasta tokens que existen solo para vendértelos.»
  - S027 [de verdad: "que el emisor tenga de verdad lo que dice", emphatic] «Las honestas afirman tener reservas (dólares y deuda pública a corto plazo) una a una, de modo que cada token es canjeable por un dólar real; su estabilidad depende por completo de que el emisor tenga de verdad lo que dice.»
  - S028 [de verdad: "la gente quiere de verdad", emphatic] «El valor en cripto viene de los mismos sitios aburridos de siempre: demanda por un uso real (la red hace algo que la gente quiere de verdad: una forma fiable de mover valor, un mercado que funciona, una plataforma sobre la que otros construyen), escasez creíble (la oferta es limitada *y* el límite es genuinamente difícil de cambiar; una escasez que el equipo puede deshacer a voluntad no es escasez) y efectos de red (una cadena sobre la que ya construye y contra la que ya cotiza todo el mundo es difícil de desplazar, porque su utilidad crece con el número de personas que la usan).»
  - S028 [other filler: "genuinamente difícil de cambiar"] «El valor en cripto viene de los mismos sitios aburridos de siempre: demanda por un uso real (la red hace algo que la gente quiere de verdad: una forma fiable de mover valor, un mercado que funciona, una plataforma sobre la que otros construyen), escasez creíble (la oferta es limitada *y* el límite es genuinamente difícil de cambiar; una escasez que el equipo puede deshacer a voluntad no es escasez) y efectos de red (una cadena sobre la que ya construye y contra la que ya cotiza todo el mundo es difícil de desplazar, porque su utilidad crece con el número de personas que la usan).»
  - S034 [realmente: "que realmente cambia de manos", deletable] «El market cap no es más que `precio × oferta total`, y ese precio lo fija la *última operación de la porción, por pequeña que sea, que realmente cambia de manos*.»
  - S036 [de verdad: "solo circula de verdad", deletable] «Pero supón que solo circula de verdad el 1 % de la oferta —10 millones de tokens— y que el libro de órdenes tiene quizá 200 000 USD de compras reales.»
  - S043 [other filler: "justo cuando más necesitas" (emphatic justo)] «La conclusión no es "no toques nunca las stablecoins" —las usarás constantemente— sino que una stablecoin es una exposición de crédito a un emisor, no efectivo sin riesgo, y una paridad puede romperse justo cuando más necesitas que aguante.»
- **2 Rhythmic triad** (1)
  - S028 [uses: "una forma fiable de mover valor, un mercado que funciona, una plataforma sobre la que otros construyen" — drop "un mercado que funciona"] «El valor en cripto viene de los mismos sitios aburridos de siempre: demanda por un uso real (la red hace algo que la gente quiere de verdad: una forma fiable de mover valor, un mercado que funciona, una plataforma sobre la que otros construyen), escasez creíble (la oferta es limitada *y* el límite es genuinamente difícil de cambiar; una escasez que el equipo puede deshacer a voluntad no es escasez) y efectos de red (una cadena sobre la que ya construye y contra la que ya cotiza todo el mundo es difícil de desplazar, porque su utilidad crece con el número de personas que la usan).»
- **4 Summary/uplift closer** (3)
  - S003 [ahead: intro paragraph ends on "El objetivo de esta lección es…" (scope announcement)] «El objetivo de esta lección es darte un modelo mental que funcione, para que cuando alguien te agite después un gráfico o una "narrativa" delante puedas hacer la única pregunta que importa: *¿qué respalda esto de verdad?*»
  - S032 [restate: "No confundas las dos." repeats the narrative-vs-value distinction just drawn] «No confundas las dos.»
  - S043 [restate: "La conclusión no es… sino…" sums up the stablecoin paragraph] «La conclusión no es "no toques nunca las stablecoins" —las usarás constantemente— sino que una stablecoin es una exposición de crédito a un emisor, no efectivo sin riesgo, y una paridad puede romperse justo cuando más necesitas que aguante.»
- **5 Sentence over 30 words** (25)
  - S002 [33w] «Cripto no es dinero mágico de internet ni es una estafa por definición: es un conjunto de tecnologías con propiedades concretas, algunas genuinamente útiles y otras vendidas muy por encima de su valor.»
  - S003 [37w] «El objetivo de esta lección es darte un modelo mental que funcione, para que cuando alguien te agite después un gráfico o una "narrativa" delante puedas hacer la única pregunta que importa: *¿qué respalda esto de verdad?*»
  - S005 [42w] «Las transacciones se agrupan en bloques, y cada bloque apunta criptográficamente al anterior, de modo que la cadena es un historial a prueba de manipulaciones: no puedes alterar en silencio una entrada antigua sin que todos los bloques posteriores dejen de encajar.»
  - S008 [37w] «Esto importa porque ninguna parte puede emitir monedas de más, congelar tu saldo ni revertir un pago para complacer a un regulador o a un amigo: las reglas las hace cumplir todo el mundo a la vez.»
  - S009 [31w] «En la práctica, nadie puede "llamar a Bitcoin" y pedir que se duplique la emisión; cambiar una regla básica exige convencer a toda la red, algo lento y raro por diseño.»
  - S010 [40w] «Una vez confirmada y enterrada bajo suficientes bloques posteriores, revertirla es, en la práctica, imposible: deshacerla obligaría a reescribir todos los bloques apilados encima más rápido que el resto de la red honesta, algo económicamente absurdo en una cadena grande.»
  - S013 [32w **aside-only** (29w without asides)] «La propiedad se prueba con una clave privada —un número secreto— porque la cadena no tiene ninguna noción de "tu cuenta" ligada a tu nombre; solo sabe qué clave autorizó una transferencia.»
  - S015 [31w **aside-only** (23w without asides)] «Así que pierde la clave y las monedas quedan congeladas para siempre (millones de BTC se han perdido exactamente así); fíltrala y te las roban al instante, sin nada que revertir.»
  - S020 [38w] «Se trata como el activo de reserva del espacio porque tiene el historial más largo, la distribución más amplia y ninguna empresa o fundación a la que apretar: lo más parecido a un patrón neutral que tiene cripto.»
  - S021 [39w] «En la práctica, casi todas las demás monedas se cotizan y se miden mentalmente contra BTC: cuando alguien dice que "las alts sangran contra Bitcoin", quiere decir que BTC aguanta su valor mientras el resto caen respecto a él.»
  - S023 [38w] «El rango de calidad es enorme porque lanzar un token es casi gratis y no pide permiso a nadie: cualquiera puede crear uno en una tarde, así que "es una altcoin" no te dice *nada* sobre su calidad.»
  - S024 [33w] «Una cadena sobre la que construyen miles de desarrolladores y una moneda que un desconocido te promocionó en los comentarios son ambas "altcoins": sigues teniendo que juzgar cada una por sus propios méritos.»
  - S026 [59w] «Existen porque no puedes tener dólares de verdad con facilidad en una blockchain, y saltar a un banco entre operaciones es lento o imposible en un mercado 24/7: por eso son el componente de efectivo del trading cripto, donde aparcas valor entre operaciones y, en las plataformas de futuros, normalmente el colateral con el que se margina tu posición.»
  - S027 [41w] «Las honestas afirman tener reservas (dólares y deuda pública a corto plazo) una a una, de modo que cada token es canjeable por un dólar real; su estabilidad depende por completo de que el emisor tenga de verdad lo que dice.»
  - S028 [106w **aside-only** (23w without asides)] «El valor en cripto viene de los mismos sitios aburridos de siempre: demanda por un uso real (la red hace algo que la gente quiere de verdad: una forma fiable de mover valor, un mercado que funciona, una plataforma sobre la que otros construyen), escasez creíble (la oferta es limitada *y* el límite es genuinamente difícil de cambiar; una escasez que el equipo puede deshacer a voluntad no es escasez) y efectos de red (una cadena sobre la que ya construye y contra la que ya cotiza todo el mundo es difícil de desplazar, porque su utilidad crece con el número de personas que la usan).»
  - S029 [37w] «Cada una de estas cosas es una razón para que alguien siga queriendo el activo mañana, al margen del humor de hoy; y "alguien seguirá queriendo esto" es lo único que sostiene un precio con el tiempo.»
  - S030 [49w] «Lo que *no* da valor duradero: una web bonita, el respaldo de un famoso, el anuncio de una "colaboración", un market cap enorme que en realidad es una oferta circulante minúscula multiplicada por un precio de fantasía, o el simple hecho de que el precio subiera la semana pasada.»
  - S031 [36w] «Un token puede dispararse por pura narrativa y volver hasta el punto de partida: la narrativa es una fuerza real a lo largo de días y semanas, y un colateral inútil a lo largo de años.»
  - S035 [34w] «Hazte la cuenta: un token se cotiza a 2 USD con una oferta total de 1000 millones de tokens, así que la cifra titular de capitalización de mercado es de 2000 millones de USD.»
  - S037 [41w] «Esos "2000 millones" son casi por completo una oferta circulante minúscula por un precio de fantasía; un gran tenedor que intentara vender aunque fueran unos pocos cientos de miles de dólares hundiría el libro poco profundo mucho antes de poder salir.»
  - S041 [35w] «En mayo de 2022, la stablecoin algorítmica UST, sostenida por un mecanismo en lugar de reservas reales, perdió su paridad y se desplomó hacia cero en cuestión de días, borrando decenas de miles de millones.»
  - S042 [39w] «Incluso una moneda bien respaldada puede tambalearse: en marzo de 2023, USDC llegó a cotizarse cerca de 0,88 USD cuando parte de sus reservas estaban en un banco que quebraba, y solo se recuperó cuando se garantizaron esos fondos.»
  - S043 [39w] «La conclusión no es "no toques nunca las stablecoins" —las usarás constantemente— sino que una stablecoin es una exposición de crédito a un emisor, no efectivo sin riesgo, y una paridad puede romperse justo cuando más necesitas que aguante.»
  - S045 [39w] «Una blockchain es un libro contable compartido sin operador central, con transacciones irreversibles y una propiedad que se prueba con una clave privada: las tres propiedades que te dan a la vez la autocustodia y ninguna red de seguridad.»
  - S046 [32w] «Bitcoin, altcoins y stablecoins no son la misma clase de activo, y el valor duradero solo viene de la demanda por un uso real, la escasez creíble y los efectos de red.»
- **11 Synonym rotation** (1)
  - S030 [market cap: market cap (S030), capitalización de mercado (S035), "cap" (S039)] 
- **A absolutes** (3)
  - S015 [siempre] «Así que pierde la clave y las monedas quedan congeladas para siempre (millones de BTC se han perdido exactamente así); fíltrala y te las roban al instante, sin nada que revertir.»
  - S028 [siempre] «El valor en cripto viene de los mismos sitios aburridos de siempre: demanda por un uso real (la red hace algo que la gente quiere de verdad: una forma fiable de mover valor, un mercado que funciona, una plataforma sobre la que otros construyen), escasez creíble (la oferta es limitada *y* el límite es genuinamente difícil de cambiar; una escasez que el equipo puede deshacer a voluntad no es escasez) y efectos de red (una cadena sobre la que ya construye y contra la que ya cotiza todo el mundo es difícil de desplazar, porque su utilidad crece con el número de personas que la usan).»
  - S043 [nunca] «La conclusión no es "no toques nunca las stablecoins" —las usarás constantemente— sino que una stablecoin es una exposición de crédito a un emisor, no efectivo sin riesgo, y una paridad puede romperse justo cuando más necesitas que aguante.»

**EN** — 32 hits, 48 sentences, density 66.7

- **1 Filler** (12)
  - S002 [genuinely: "some genuinely useful"] «Crypto is not magic internet money and it is not a scam by definition — it is a set of technologies with specific properties, some genuinely useful and some wildly oversold.»
  - S003 [actually: "what is actually backing this?"] «The aim of this lesson is a working mental model, so that when someone later waves a chart or a "narrative" at you, you can ask the only question that matters: *what is actually backing this?*»
  - S009 [In practice: introduces an illustration, no theory contrast] «In practice, nobody can "call Bitcoin" and ask for the supply to be doubled; changing a core rule takes convincing the whole network, which is slow and rare by design.»
  - S015 [exactly: "gone exactly this way", emphatic] «So lose the key and the coins are frozen forever (millions of BTC are gone exactly this way); leak it and they are stolen instantly, with nothing to reverse.»
  - S021 [In practice: tic] «In practice, most other coins are quoted and mentally measured against BTC: when people say "alts are bleeding against Bitcoin," they mean BTC is holding value while the rest fall relative to it.»
  - S022 [literally: intensifier] «Altcoins are literally everything that is not Bitcoin — from serious platforms with real usage down to tokens that exist only to be sold to you.»
  - S027 [actually: "the issuer actually holding what they claim"] «The honest ones claim to hold reserves (dollars and short-term government debt) one-for-one so each token is redeemable for a real dollar; their stability depends *entirely* on the issuer actually holding what they claim.»
  - S028 [actually: "people actually want"] «Value in crypto comes from the same boring places it comes from anywhere: demand for a real use (the network does something people actually want — a reliable way to move value, a functioning market, a platform others build on), credible scarcity (supply is limited *and* the limit is genuinely hard to change — scarcity a team can undo at will is not scarcity), and network effects (a chain everyone already builds on and quotes against is hard to displace, because its usefulness grows with the number of people using it).»
  - S028 [genuinely: "genuinely hard to change"] «Value in crypto comes from the same boring places it comes from anywhere: demand for a real use (the network does something people actually want — a reliable way to move value, a functioning market, a platform others build on), credible scarcity (supply is limited *and* the limit is genuinely hard to change — scarcity a team can undo at will is not scarcity), and network effects (a chain everyone already builds on and quotes against is hard to displace, because its usefulness grows with the number of people using it).»
  - S034 [actually: "actually changes hands"] «Market cap is just `price × total supply`, and that price is set by the *last trade of whatever thin slice actually changes hands*.»
  - S036 [really: "really circulates"] «But suppose only 1% of the supply — 10 million tokens — really circulates, and the order book holds perhaps 200,000 USD of genuine bids.»
  - S044 [exactly: "exactly when you most need it", emphatic] «The takeaway is not "never touch stablecoins" — you will use them constantly — but that a stablecoin is a credit exposure to an issuer, not risk-free cash, and a peg can break exactly when you most need it to hold.»
- **2 Rhythmic triad** (1)
  - S028 [uses: "a reliable way to move value, a functioning market, a platform others build on" — drop "a functioning market"] «Value in crypto comes from the same boring places it comes from anywhere: demand for a real use (the network does something people actually want — a reliable way to move value, a functioning market, a platform others build on), credible scarcity (supply is limited *and* the limit is genuinely hard to change — scarcity a team can undo at will is not scarcity), and network effects (a chain everyone already builds on and quotes against is hard to displace, because its usefulness grows with the number of people using it).»
- **4 Summary/uplift closer** (3)
  - S003 [ahead: intro paragraph ends on "The aim of this lesson is…" (scope announcement)] «The aim of this lesson is a working mental model, so that when someone later waves a chart or a "narrative" at you, you can ask the only question that matters: *what is actually backing this?*»
  - S032 [restate: "Never confuse the two." repeats the distinction just drawn] «Never confuse the two.»
  - S044 [restate: "The takeaway is not… but…" sums up the stablecoin paragraph] «The takeaway is not "never touch stablecoins" — you will use them constantly — but that a stablecoin is a credit exposure to an issuer, not risk-free cash, and a peg can break exactly when you most need it to hold.»
- **5 Sentence over 30 words** (16)
  - S003 [36w] «The aim of this lesson is a working mental model, so that when someone later waves a chart or a "narrative" at you, you can ask the only question that matters: *what is actually backing this?*»
  - S005 [36w] «Transactions are bundled into blocks, and each block cryptographically points back to the previous one, so the chain is a tamper-evident history — you cannot quietly alter an old entry without every later block no longer fitting.»
  - S008 [32w] «This matters because no single party can print extra coins, freeze your balance, or reverse a payment to please a regulator or a friend — the rules are enforced by everyone at once.»
  - S010 [41w] «Once a transaction is confirmed and buried under enough later blocks, reversing it is, in practice, impossible — undoing it would mean out-running the entire honest network to rewrite every block stacked on top, which is economically absurd on a large chain.»
  - S013 [31w **aside-only** (28w without asides)] «Ownership is proven by a private key — a secret number — because the chain has no notion of "your account" tied to your name; it only knows which key authorised a transfer.»
  - S020 [39w] «It is treated as the reserve asset of the space because it has the longest track record, the widest distribution, and no company or foundation that can be leaned on — the closest thing crypto has to a neutral benchmark.»
  - S021 [33w] «In practice, most other coins are quoted and mentally measured against BTC: when people say "alts are bleeding against Bitcoin," they mean BTC is holding value while the rest fall relative to it.»
  - S026 [54w] «They exist because you cannot easily hold real dollars on a blockchain, and hopping to a bank between trades is slow or impossible in a 24/7 market — so they are the cash leg of crypto trading, where you park value between trades and, on futures venues, usually the collateral your positions are margined in.»
  - S027 [34w **aside-only** (29w without asides)] «The honest ones claim to hold reserves (dollars and short-term government debt) one-for-one so each token is redeemable for a real dollar; their stability depends *entirely* on the issuer actually holding what they claim.»
  - S028 [89w **aside-only** (21w without asides)] «Value in crypto comes from the same boring places it comes from anywhere: demand for a real use (the network does something people actually want — a reliable way to move value, a functioning market, a platform others build on), credible scarcity (supply is limited *and* the limit is genuinely hard to change — scarcity a team can undo at will is not scarcity), and network effects (a chain everyone already builds on and quotes against is hard to displace, because its usefulness grows with the number of people using it).»
  - S029 [33w] «Each of these is a reason someone will still want the asset tomorrow, independent of today's mood — and "someone will still want this" is the only thing that supports a price over time.»
  - S030 [41w] «What does *not* confer durable value: a slick website, a celebrity endorsement, a "partnership" announcement, a large market cap that is really a tiny float multiplied by a fantasy price, or the mere fact that a price went up last week.»
  - S037 [35w] «That "2 billion" is almost entirely a tiny float times a fantasy price; a large holder trying to sell even a few hundred thousand dollars' worth would collapse the thin book long before getting out.»
  - S043 [32w] «Even a well-reserved coin can wobble: in March 2023 USDC briefly traded near 0.88 USD when part of its reserves sat in a failing bank, recovering only once those funds were backstopped.»
  - S044 [39w] «The takeaway is not "never touch stablecoins" — you will use them constantly — but that a stablecoin is a credit exposure to an issuer, not risk-free cash, and a peg can break exactly when you most need it to hold.»
  - S046 [33w] «A blockchain is a shared ledger with no central operator, settlement that is final, and ownership proven by a private key — the three properties that give you both self-custody and no safety net.»
- **A absolutes** (2)
  - S032 [never] «Never confuse the two.»
  - S044 [never] «The takeaway is not "never touch stablecoins" — you will use them constantly — but that a stablecoin is a credit exposure to an issuer, not risk-free cash, and a peg can break exactly when you most need it to hold.»

### m02-l1

**ES** — 33 hits, 90 sentences, density 36.7

- **1 Filler** (11)
  - S004 [de verdad: "quién controla de verdad tu dinero", emphatic] «Este módulo trata de cómo funciona el trading y, sobre todo, de quién controla de verdad tu dinero en cada paso.»
  - S007 [other filler: "que es justo lo que lo hace rápido" (emphatic justo)] «un único operador puede emparejar órdenes en microsegundos, tener un servicio de atención al cliente y deshacer sus propios errores, que es justo lo que lo hace rápido y familiar.»
  - S019 [sencillamente: intensifier] «El spot es el caso simple: tu ganancia o pérdida es sencillamente el precio de la moneda, y nunca pueden cerrarte a la fuerza, porque no le debes nada a nadie.»
  - S028 [exactamente: "muestra exactamente cuánto cuesta", not pinning a quantity] «El libro de órdenes de abajo muestra exactamente cuánto cuesta eso.»
  - S036 [de verdad: "el que conseguiste de verdad", deletable] «La diferencia entre el precio que esperabas y el que conseguiste de verdad es el slippage (deslizamiento).»
  - S044 [de verdad: "que de verdad se ofrecían a 2,00", deletable] «Una compra limitada a 2,00 habría ejecutado en cambio solo las 500 unidades que de verdad se ofrecían a 2,00 y habría dejado las otras 1.500 esperando a que los vendedores bajaran a tu precio.»
  - S048 [precisamente: emphatic "precisamente porque"] «*Por qué es cómoda y frágil:* la empresa puede reiniciar tu contraseña y arreglar tus errores precisamente porque controla las monedas, lo que significa que igual de bien puede congelarlas, perderlas o gastarlas.»
  - S061 [simplemente: "simplemente desaparecen"] «*En la práctica:* envía un retiro a una dirección equivocada, o por la red equivocada, y las monedas simplemente desaparecen; no hay contracargo ni ticket de soporte que las traiga de vuelta.»
  - S072 [de verdad: "los permisos que de verdad necesita"] «*Por qué:* cualquier clave puede filtrarse, o el programa que la guarda puede sufrir una brecha, así que le concedes solo los permisos que de verdad necesita.»
  - S076 [de verdad: "sacar de verdad las monedas"] «*Por qué:* rompe el último paso de casi cualquier robo de cuenta: sacar de verdad las monedas.»
  - S087 [sencillamente: "sencillamente es deshonesto"] «Si ese tercero sufre una brecha o sencillamente es deshonesto, la clave retira los fondos directamente, y como la transferencia se confirma on-chain es definitiva antes de que te des cuenta.»
- **4 Summary/uplift closer** (4)
  - S004 [ahead: intro paragraph ends announcing what the module is about] «Este módulo trata de cómo funciona el trading y, sobre todo, de quién controla de verdad tu dinero en cada paso.»
  - S028 [ahead: "El libro de órdenes de abajo muestra exactamente cuánto cuesta eso." points forward] «El libro de órdenes de abajo muestra exactamente cuánto cuesta eso.»
  - S045 [editorial: "Esa es toda la elección en una sola imagen: …" restates the two outcomes] «Esa es toda la elección en una sola imagen: la orden de mercado consiguió las 2.000 pero a peor media; la orden limitada protegió el precio pero podría no completarse nunca.»
  - S055 [editorial: "Ese es el día en que la diferencia… deja de ser académica."] «Ese es el día en que la diferencia entre "monedas" y "un pagaré por monedas" deja de ser académica.»
- **5 Sentence over 30 words** (16)
  - S009 [33w] «Al depositar, tus monedas van a las carteras *del exchange* y tu saldo pasa a ser un número en la base de datos de la empresa: una promesa de pago, no las monedas.»
  - S014 [41w] «no hay cuenta ni empresa que retenga tus fondos, pero tampoco hay atención al cliente, ni recuperación de contraseña, y sí un conjunto distinto de riesgos: contratos con fallos, comisiones de red y errores que son definitivos porque los firmaste tú.»
  - S019 [31w] «El spot es el caso simple: tu ganancia o pérdida es sencillamente el precio de la moneda, y nunca pueden cerrarte a la fuerza, porque no le debes nada a nadie.»
  - S021 [31w] «En un CEX ese BTC sigue siendo un pagaré hasta que lo retiras a tu propia cartera, pero económicamente eres el dueño del activo y de toda su oscilación de precio.»
  - S035 [33w] «una orden de mercado recorre el libro ejecutándose contra cada nivel por turno, así que una orden grande en un libro con poca profundidad obtiene precios cada vez peores a medida que avanza.»
  - S044 [35w] «Una compra limitada a 2,00 habría ejecutado en cambio solo las 500 unidades que de verdad se ofrecían a 2,00 y habría dejado las otras 1.500 esperando a que los vendedores bajaran a tu precio.»
  - S045 [31w] «Esa es toda la elección en una sola imagen: la orden de mercado consiguió las 2.000 pero a peor media; la orden limitada protegió el precio pero podría no completarse nunca.»
  - S048 [33w] «*Por qué es cómoda y frágil:* la empresa puede reiniciar tu contraseña y arreglar tus errores precisamente porque controla las monedas, lo que significa que igual de bien puede congelarlas, perderlas o gastarlas.»
  - S054 [36w] «Exchanges que parecían intocables han congelado los retiros de la noche a la mañana y han entrado en quiebra, dejando a los clientes esperando años a que un tribunal les devuelva unos céntimos por cada dólar.»
  - S058 [38w] «Mantener fondos en un exchange para operar es un compromiso razonable; guardar ahí tus *ahorros* es, sin darte cuenta, convertir a esa empresa en tu banco, uno sin regulación y sin ninguna de las garantías de un banco.»
  - S061 [32w] «*En la práctica:* envía un retiro a una dirección equivocada, o por la red equivocada, y las monedas simplemente desaparecen; no hay contracargo ni ticket de soporte que las traiga de vuelta.»
  - S064 [31w] «*En la práctica:* la liquidez adelgaza de madrugada y los fines de semana, así que la misma orden de mercado desliza más y el precio puede dar saltos bruscos mientras duermes.»
  - S081 [31w] «Los códigos por mensaje de texto parecen seguridad, pero van montados sobre tu número de teléfono, y un atacante que engañe a tu operadora para portar ese número recibe cada código.»
  - S087 [31w] «Si ese tercero sufre una brecha o sencillamente es deshonesto, la clave retira los fondos directamente, y como la transferencia se confirma on-chain es definitiva antes de que te des cuenta.»
  - S089 [33w] «Una orden de mercado compra certeza de ejecución a costa del precio y una orden limitada hace lo contrario, y la profundidad del libro de órdenes decide cuánto slippage te cuesta esa elección.»
  - S090 [40w **aside-only** (26w without asides)] «Las medidas de la cuenta —app de autenticación, API keys con permisos limitados, lista blanca de direcciones de retiro— existen todas por una razón: no para ser imposible de hackear, sino para que un solo fallo no vacíe la cuenta.»
- **8 Repeated paragraph opener** (1)
  - S001 ["Un exchange" ×3 (S001, S005, S012) — term as subject] 
- **11 Synonym rotation** (1)
  - S009 [CEX balance as a claim: promesa de pago (S009), pagaré (S021), pasivo en los libros del exchange (S049), derecho de cobro sobre una empresa (S057)] 
- **A absolutes** (8)
  - S002 [siempre] «Esa parte suena sencilla, y operar lo es casi siempre.»
  - S013 [nunca] «Operas directamente desde tu propia cartera; la operación se confirma on-chain y las monedas nunca salen de tu control salvo para completar el intercambio.»
  - S018 [nunca] «el spot es lo contrario de los futuros que veremos más adelante, donde aportas margen y nunca tomas posesión de la moneda: solo saldas la diferencia de precio.»
  - S019 [nunca, debes] «El spot es el caso simple: tu ganancia o pérdida es sencillamente el precio de la moneda, y nunca pueden cerrarte a la fuerza, porque no le debes nada a nadie.»
  - S026 [siempre, nunca] «*Por qué:* fijas tu precio y esperas, así que controlas el precio que pagas, pero la orden puede quedarse sin ejecutar para siempre si el mercado nunca lo alcanza.»
  - S027 [siempre] «El compromiso es siempre el mismo: una orden de mercado compra certeza de *ejecución* a costa de la certeza de *precio*; una orden limitada hace lo contrario.»
  - S045 [nunca] «Esa es toda la elección en una sola imagen: la orden de mercado consiguió las 2.000 pero a peor media; la orden limitada protegió el precio pero podría no completarse nunca.»
  - S078 [nunca] «Así, ni siquiera un atacante que entre como tú podrá enviar monedas a una dirección que nunca aprobaste.»

**EN** — 23 hits, 91 sentences, density 25.3

- **1 Filler** (11)
  - S004 [actually: "who actually controls your money"] «This module is about how the trading works and, more importantly, who actually controls your money at each step.»
  - S007 [exactly: "which is exactly what makes it fast"] «a single operator can match orders in microseconds, run a support desk, and undo its own mistakes — which is exactly what makes it fast and familiar.»
  - S020 [simply: "is simply the coin's price"] «Spot is the plain case: your gain or loss is simply the coin's price, and you can never be force-closed, because you owe nobody anything.»
  - S029 [exactly: "shows exactly what that costs"] «The order book below shows exactly what that costs.»
  - S037 [actually: "the price you actually got"] «The gap between the price you expected and the price you actually got is slippage.»
  - S045 [actually: "the 500 units actually offered"] «A limit buy at 2.00 would instead have filled only the 500 units actually offered at 2.00 and left the other 1,500 waiting until sellers came down to your price.»
  - S049 [precisely: emphatic "precisely because"] «*Why it is convenient and fragile:* the company can reset your password and fix your mistakes precisely because it controls the coins — which means it can equally freeze, lose, or spend them.»
  - S062 [simply: "the coins are simply gone"] «*In practice:* send a withdrawal to a wrong address, or over the wrong network, and the coins are simply gone; there is no chargeback and no support ticket that brings them back.»
  - S073 [actually: "the powers it actually needs"] «*Why:* any key can be leaked, or the program holding it can be breached, so you grant it only the powers it actually needs.»
  - S077 [actually: "actually moving the coins out"] «*Why:* it breaks the last step of almost every account takeover — actually moving the coins out.»
  - S088 [simply: "or simply dishonest"] «If that third party is breached or simply dishonest, the key withdraws the funds directly, and because the transfer settles on-chain it is final before you even notice.»
- **4 Summary/uplift closer** (4)
  - S004 [ahead: intro paragraph ends announcing what the module is about] «This module is about how the trading works and, more importantly, who actually controls your money at each step.»
  - S029 [ahead: "The order book below shows exactly what that costs." points forward] «The order book below shows exactly what that costs.»
  - S046 [editorial: "That is the whole choice in one picture: …"] «That is the whole choice in one picture: the market order got all 2,000 but at a worse average; the limit order protected the price but might never complete.»
  - S056 [editorial: "That is the day the difference… stops being academic."] «That is the day the difference between "coins" and "an IOU for coins" stops being academic.»
- **5 Sentence over 30 words** (7)
  - S015 [33w] «That same design removes the safety net — no support desk, no password reset, and a different set of risks: buggy contracts, network fees, and mistakes that are final because you signed them yourself.»
  - S049 [32w] «*Why it is convenient and fragile:* the company can reset your password and fix your mistakes precisely because it controls the coins — which means it can equally freeze, lose, or spend them.»
  - S052 [32w] «*Why it is powerful and unforgiving:* no company can freeze or lose your coins for you — and no company can help you if you lose the keys or sign a bad transaction.»
  - S059 [31w] «Keeping funds on an exchange to trade is a reasonable trade-off; keeping your *savings* there is quietly making that company your bank — an unregulated one, with none of a bank's guarantees.»
  - S062 [32w] «*In practice:* send a withdrawal to a wrong address, or over the wrong network, and the coins are simply gone; there is no chargeback and no support ticket that brings them back.»
  - S090 [34w] «A market order buys certainty of execution at the cost of price and a limit order does the reverse, while the depth of the order book decides how much slippage that choice costs you.»
  - S091 [32w **aside-only** (22w without asides)] «The account controls here — an authenticator app, scoped API keys, a withdrawal address whitelist — all exist for one reason: not to be un-hackable, but to stop a single failure emptying the account.»
- **11 Synonym rotation** (1)
  - S009 [CEX balance as a claim: a promise to pay (S009), IOU (S022), a liability on the exchange's books (S050), a claim on a company (S058)] 
- **A absolutes** (7)
  - S013 [never] «You trade directly from your own wallet; the trade settles on-chain and the coins never leave your control except to complete the swap.»
  - S019 [never] «spot is the opposite of the futures contracts covered later, where you post margin and never take possession of the coin — you only settle the price difference.»
  - S020 [never] «Spot is the plain case: your gain or loss is simply the coin's price, and you can never be force-closed, because you owe nobody anything.»
  - S027 [never] «*Why:* you name your price and wait, so you control the price you pay — but the order may sit unfilled forever if the market never reaches it.»
  - S028 [always] «The trade-off is always the same: a market order buys certainty of *execution* at the cost of certainty of *price*; a limit order does the reverse.»
  - S046 [never] «That is the whole choice in one picture: the market order got all 2,000 but at a worse average; the limit order protected the price but might never complete.»
  - S079 [never] «Then even an attacker who logs in as you cannot send coins to an address you never approved.»

### m03-l1

**ES** — 34 hits, 76 sentences, density 44.7

- **1 Filler** (11)
  - S002 [realmente: "lo que realmente se operó", deletable] «Es un registro de lo que realmente se operó: a qué precio, cuándo y cuánto.»
  - S005 [nada más: tag at sentence end] «El mercado no "quiere" nada ni te está enviando mensajes; un gráfico es la suma de las huellas de gente que compra y vende, nada más.»
  - S017 [other filler: announcer sentence "Ahora el porqué."] «Ahora el porqué.»
  - S021 [en la práctica: whole sentence is an announcer ("Esto es lo que parece en la práctica.")] «Esto es lo que parece en la práctica.»
  - S034 [En la práctica: tic opening an example] «En la práctica, una jornada que aparece como una modesta vela roja en el gráfico diario son cientos de velas —subidas, caídas, pánico y recuperación— en el de 5 minutos.»
  - S044 [En la práctica: tic opening an example] «En la práctica, compara dos rupturas a un nuevo máximo de aspecto idéntico.»
  - S051 [de verdad: "como si el precio 'perteneciera' de verdad a ese nivel"] «Una mecha es precio *rechazado*, pero los principiantes tratan rutinariamente el extremo que alcanza como si el precio "perteneciera" de verdad a ese nivel — colocando un stop un pelo más allá de la punta de una mecha, o entrando en pánico cuando una mecha perfora brevemente un nivel y vuelve de golpe.»
  - S057 [other filler: announcer "de formas que conviene nombrar"] «Todo lo anterior vale para cualquier mercado, pero en cripto la mecánica cambia de formas que conviene nombrar.»
  - S059 [simplemente: intensifier] «Cripto no cierra nunca: se opera 24 horas al día, 7 días a la semana, así que una vela "diaria" simplemente abarca una ventana fija de 24 horas, por convención de 00:00 a 00:00 UTC.»
  - S064 [simplemente: intensifier] «Nada está roto; simplemente han cortado la misma secuencia continua en puntos diferentes.»
  - S070 [precisamente: emphatic "por eso precisamente"] «La mayor parte del tiempo los mercados están en rango; las tendencias son la excepción, y por eso precisamente vale la pena el esfuerzo de identificarlas.»
- **2 Rhythmic triad** (1)
  - S038 ["más velas, más vaivenes y una relación señal-ruido mucho peor" — drop "más vaivenes" (overlaps noise)] «Los principiantes suelen recurrir a una temporalidad muy baja porque *parece* más información, cuando la mayor parte es más ruido: más velas, más vaivenes y una relación señal-ruido mucho peor.»
- **4 Summary/uplift closer** (5)
  - S007 [ahead: intro paragraph ends on what the next lesson covers] «Cómo se organiza el precio a lo largo de muchas velas —tendencia, rango y soportes/resistencias— tiene su propio tratamiento, más a fondo, en la lección siguiente.»
  - S020 [restate: "Una mecha larga es el mercado diciendo 'probamos este nivel y no cuajó'." repeats S019 (rejected prices)] «Una mecha larga es el mercado diciendo "probamos este nivel y no cuajó".»
  - S027 [editorial: "No lo son."] «No lo son.»
  - S049 [restate: "El volumen es contexto, no una señal por sí mismo." repeats S040] «El volumen es contexto, no una señal por sí mismo.»
  - S073 [ahead: lesson's last prose unit ends pointing to the next lesson] «Desarrollaremos tendencia, rango y soportes/resistencias como es debido en la lección siguiente; por ahora quédate con la distinción: una vela es un dato, pero muchas velas juntas forman *estructura*, y la estructura es adonde va la lección siguiente.»
- **5 Sentence over 30 words** (14)
  - S018 [45w] «De los cuatro números, el cierre es al que la mayoría de los traders da más peso, porque es el precio que ambos lados estuvieron dispuestos a dejar sobre la mesa cuando el reloj se agotó: la tregua temporal, no los gritos de por medio.»
  - S023 [32w **aside-only** (27w without asides)] «El cuerpo es diminuto (100→101), pero la mecha inferior es larga (baja hasta 96): el precio se hundió con fuerza y luego se compró de vuelta por completo antes del cierre.»
  - S029 [34w] «En un gráfico de 1 minuto cada vela es un minuto; en uno de 4 horas, cuatro horas; en uno diario cada vela es una jornada entera de operativa comprimida en una sola barra.»
  - S032 [46w] «Cuanto más alta es la temporalidad, más participantes y más dinero han formado esa vela — una vela diaria es el veredicto asentado de todos los que operaron ese día, mientras que una vela de 1 minuto puede ser una sola orden grande en un momento tranquilo.»
  - S036 [34w] «Amplía a 5 minutos y ese mismo día puede ser una escalera de bajada, un rebote brusco de vuelta a 59.500 y un deslizamiento hacia el cierre — decenas de pequeños "giros", casi todos ruido.»
  - S042 [31w] «Un movimiento con volumen alto significa que se comprometió mucho capital a esos precios, así que cuesta más deshacerlo: mucha gente sostiene ahora posiciones ahí y tiene un motivo para defenderlas.»
  - S046 [31w] «En la segunda, ese mismo nuevo máximo se imprime con la mitad del volumen medio — un puñado de operaciones en una hora tranquila empujando el precio hacia arriba sin nadie detrás.»
  - S051 [52w] «Una mecha es precio *rechazado*, pero los principiantes tratan rutinariamente el extremo que alcanza como si el precio "perteneciera" de verdad a ese nivel — colocando un stop un pelo más allá de la punta de una mecha, o entrando en pánico cuando una mecha perfora brevemente un nivel y vuelve de golpe.»
  - S058 [51w] «Las bolsas de acciones cierran por la noche y los fines de semana, así que la vela diaria de una acción tiene una apertura real (la subasta de campana) y un cierre real, y el precio puede dar un *gap* entre el cierre de un día y la apertura del siguiente.»
  - S059 [35w] «Cripto no cierra nunca: se opera 24 horas al día, 7 días a la semana, así que una vela "diaria" simplemente abarca una ventana fija de 24 horas, por convención de 00:00 a 00:00 UTC.»
  - S066 [41w] «Un libro más fino hace que la misma orden empuje más el precio, así que los movimientos de fin de semana pueden verse muy acusados en el gráfico aunque representen muchos menos participantes que un movimiento entre semana del mismo tamaño.»
  - S069 [48w **aside-only** (21w without asides)] «Está en tendencia —avanzando de forma neta en una dirección, imprimiendo máximos más altos y mínimos más altos (tendencia alcista) o máximos más bajos y mínimos más bajos (tendencia bajista)— o está en rango, moviéndose de lado entre un techo aproximado y un suelo aproximado sin avance neto.»
  - S073 [38w] «Desarrollaremos tendencia, rango y soportes/resistencias como es debido en la lección siguiente; por ahora quédate con la distinción: una vela es un dato, pero muchas velas juntas forman *estructura*, y la estructura es adonde va la lección siguiente.»
  - S074 [35w **aside-only** (30w without asides)] «Una vela resume un periodo con cuatro números —apertura, máximo, mínimo y cierre— y la distinción entre cuerpo y mecha es casi toda la lectura: una mecha es precio que se tocó y fue rechazado.»
- **9 Course-coined term** (2)
  - S036 [escalera [seed]] «Amplía a 5 minutos y ese mismo día puede ser una escalera de bajada, un rebote brusco de vuelta a 59.500 y un deslizamiento hacia el cierre — decenas de pequeños "giros", casi todos ruido.»
  - S045 [combustible [seed]] «En la primera, la vela de ruptura opera el triple del volumen medio reciente: muchos participantes están comprando la ruptura y el movimiento tiene combustible.»
- **11 Synonym rotation** (1)
  - S028 [timeframe: temporalidad (S028), ventana (S030), nivel de zoom (S037, S055)] 
- **A absolutes** (2)
  - S059 [nunca] «Cripto no cierra nunca: se opera 24 horas al día, 7 días a la semana, así que una vela "diaria" simplemente abarca una ventana fija de 24 horas, por convención de 00:00 a 00:00 UTC.»
  - S068 [siempre] «Aléjate de la vela individual y el precio casi siempre está haciendo una de dos cosas.»

**EN** — 32 hits, 76 sentences, density 42.1

- **1 Filler** (11)
  - S002 [actually: "what actually traded"] «It is a record of what actually traded: at what price, when, and how much.»
  - S005 [nothing more: tag at sentence end] «The market does not "want" anything and it is not sending you messages; a chart is the summed footprints of people buying and selling, nothing more.»
  - S017 [other filler: announcer sentence "Now the why."] «Now the why.»
  - S021 [in practice: whole sentence is an announcer ("Here is what that looks like in practice.")] «Here is what that looks like in practice.»
  - S034 [In practice: tic opening an example] «In practice, a day that shows up as one modest red candle on the daily chart is hundreds of candles — rallies, dips, panic and recovery — on the 5-minute chart.»
  - S044 [In practice: tic opening an example] «In practice, compare two identical-looking breakouts to a new high.»
  - S051 [other filler: "as if price meaningfully 'belonged' there"] «A wick is *rejected* price, but beginners routinely treat the extreme it reaches as if price meaningfully "belonged" there — placing a stop a hair past a wick's tip, or panicking when a wick briefly pierces a level and snaps back.»
  - S057 [other filler: announcer "in ways worth naming"] «Everything above applies to any market, but crypto changes the mechanics in ways worth naming.»
  - S059 [simply: intensifier] «Crypto never closes: trading runs 24 hours a day, 7 days a week, so a "daily" candle simply spans a fixed 24-hour window, conventionally 00:00 to 00:00 UTC.»
  - S064 [simply: intensifier] «Nothing is broken; they have simply cut the same continuous tape at different points.»
  - S070 [exactly: emphatic "exactly why"] «Most of the time markets range; trends are the exception, which is exactly why identifying them is worth the effort.»
- **2 Rhythmic triad** (1)
  - S038 ["more candles, more wiggles, and a far worse signal-to-noise ratio" — drop "more wiggles"] «Beginners often reach for a very low timeframe because it *feels* like more information, when mostly it is more noise: more candles, more wiggles, and a far worse signal-to-noise ratio.»
- **4 Summary/uplift closer** (5)
  - S007 [ahead: intro paragraph ends on what the next lesson covers] «How price organises itself over many candles — trend, range, and support/resistance — gets its own, deeper treatment in the next lesson.»
  - S020 [restate: "A long wick is the market saying 'we tried this level and it didn't stick.'" repeats S019] «A long wick is the market saying "we tried this level and it didn't stick."»
  - S027 [editorial: "They are not."] «They are not.»
  - S049 [restate: "Volume is context, not a signal by itself." repeats S040] «Volume is context, not a signal by itself.»
  - S073 [ahead: lesson's last prose unit ends pointing to the next lesson] «We will build out trend, range, and support/resistance properly in the next lesson; for now just hold the distinction: one candle is a data point, but many candles together form *structure*, and structure is where the next lesson goes.»
- **5 Sentence over 30 words** (11)
  - S018 [41w] «Of the four numbers, the close is the one most traders weight most heavily, because it is the price both sides were willing to leave on the table when the clock ran out — the temporary truce, not the shouting in between.»
  - S029 [31w] «On a 1-minute chart each candle is one minute; on a 4-hour chart, four hours; on a daily chart each candle is a full day of trading compressed into one bar.»
  - S032 [42w] «The higher the timeframe, the more participants and more money went into forming that candle — a daily candle is the settled verdict of everyone who traded that day, while a 1-minute candle can be a single large order in a quiet moment.»
  - S036 [33w] «Zoom to 5-minute and that same day might be a staircase down, a sharp bounce back to 59,500, and a slide into the close — dozens of little "reversals," almost all of them noise.»
  - S042 [35w] «A move on high volume means a lot of capital was committed at those prices, so it is harder to unwind — plenty of people now hold positions there and have a reason to defend them.»
  - S051 [40w] «A wick is *rejected* price, but beginners routinely treat the extreme it reaches as if price meaningfully "belonged" there — placing a stop a hair past a wick's tip, or panicking when a wick briefly pierces a level and snaps back.»
  - S058 [38w] «Stock markets shut overnight and at weekends, so a stock's daily candle has a real open (the auction at the bell) and a real close, and price can *gap* between one day's close and the next day's open.»
  - S066 [32w] «A thinner book means the same order pushes price further, so weekend moves can look dramatic on the chart while representing far fewer participants than a weekday move of the same size.»
  - S069 [43w **aside-only** (21w without asides)] «It is trending — making net progress in one direction, printing higher highs and higher lows (an uptrend) or lower highs and lower lows (a downtrend) — or it is ranging, moving sideways between a rough ceiling and a rough floor with no net progress.»
  - S073 [39w] «We will build out trend, range, and support/resistance properly in the next lesson; for now just hold the distinction: one candle is a data point, but many candles together form *structure*, and structure is where the next lesson goes.»
  - S074 [31w **aside-only** (26w without asides)] «A candle summarises one period with four numbers — open, high, low and close — and the body-versus-wick distinction is most of the reading: a wick is price that was touched and rejected.»
- **9 Course-coined term** (2)
  - S036 [staircase/ladder [seed]] «Zoom to 5-minute and that same day might be a staircase down, a sharp bounce back to 59,500, and a slide into the close — dozens of little "reversals," almost all of them noise.»
  - S045 [fuel [seed]] «In the first, the breakout candle trades three times the recent average volume: many participants are buying the breakout, and the move has fuel.»
- **11 Synonym rotation** (2)
  - S016 [wick rejection: rejected (S016, S051), refused (S019), pushed back (S053)] 
  - S028 [timeframe: timeframe (S028), window (S030), zoom level (S037, S055)] 
- **A absolutes** (2)
  - S059 [never] «Crypto never closes: trading runs 24 hours a day, 7 days a week, so a "daily" candle simply spans a fixed 24-hour window, conventionally 00:00 to 00:00 UTC.»
  - S068 [always] «Zoom out from the single candle and price is almost always doing one of two things.»

### m03-l2

**ES** — 32 hits, 75 sentences, density 42.7

- **1 Filler** (5)
  - S010 [other filler: announcer "El porqué es sencillo:"] «El porqué es sencillo: una tendencia existe solo mientras un lado sigue ganando la subasta.»
  - S026 [other filler: emphatic "que es justo por lo que"] «Las tendencias son la excepción, porque un desequilibrio sostenido hacia un solo lado es caro de mantener y poco frecuente, que es justo por lo que una tendencia real merece la pena montarla cuando la encuentras.»
  - S039 [other filler: announcer sentence "Aquí está el *porqué*, mecánicamente:"] «Aquí está el *porqué*, mecánicamente:»
  - S056 [exactamente: "que es exactamente lo que hace el precio en un borde"] «Léelo como una banda y esa misma mecha es solo el precio testeando el borde, que es exactamente lo que hace el precio en un borde.»
  - S068 [other filler: emphatic "que es justo por lo que importa el volumen"] «La ruptura parece real en el gráfico pero casi no tuvo volumen ni participación detrás (que es justo por lo que importa el volumen de la lección anterior).»
- **2 Rhythmic triad** (1)
  - S059 ["promedia a la baja…, se salta el stop y le entrega su cuenta al mercado" — drop "le entrega su cuenta al mercado" (rhythmic third)] «Un nivel es una *probabilidad*, no un muro, y el trader que trata el soporte como un suelo garantizado promedia a la baja en una posición perdedora en largo «porque tiene que rebotar aquí», se salta el stop y le entrega su cuenta al mercado cuando no rebota.»
- **4 Summary/uplift closer** (4)
  - S003 [motivate: intro ends "es la pregunta más importante que puedes hacerle a un gráfico"] «No es un adorno sobre la lección anterior; es la pregunta más importante que puedes hacerle a un gráfico, porque decide qué tácticas tienen siquiera sentido.»
  - S016 [restate: "Una sola caída no basta; hace falta un mínimo más bajo." repeats S012/S015] «Una sola caída no basta; hace falta un *mínimo más bajo*.»
  - S061 [motivate: "Tu trabajo es estar posicionado para el día en que este lo haga."] «Tu trabajo es estar posicionado para el día en que este lo haga.»
  - S072 [editorial: lesson's last prose unit ends "Otra falsa ruptura disfrazada de estructural."] «Otra falsa ruptura disfrazada de estructural.»
- **5 Sentence over 30 words** (19)
  - S006 [32w **aside-only** (28w without asides)] «Un máximo de giro (swing high) es un pico con velas más bajas a ambos lados; un mínimo de giro (swing low) es un valle con velas más altas a ambos lados.»
  - S014 [33w] «El precio sube a 100, retrocede a 92 y luego empuja hasta 108: 108 supera el máximo anterior y 92 queda por encima del mínimo previo, así que la tendencia alcista está sana.»
  - S015 [33w **aside-only** (26w without asides)] «Si el siguiente retroceso corta hasta 89 —por debajo de ese mínimo de 92—, la secuencia de mínimos crecientes se rompe, y "tendencia alcista intacta" deja de ser un hecho que puedas afirmar.»
  - S026 [36w] «Las tendencias son la excepción, porque un desequilibrio sostenido hacia un solo lado es caro de mantener y poco frecuente, que es justo por lo que una tendencia real merece la pena montarla cuando la encuentras.»
  - S027 [38w] «Por ejemplo, que BTC pase dos semanas rebotando entre unos 59.000 y 62.000, imprimiendo tres máximos cerca de 62k y tres mínimos cerca de 59k, es un rango, aunque cualquier día suelto dentro de él parezca una mini-tendencia.»
  - S034 [32w] «Es **"¿tendencia o rango, en mi temporalidad?"** — y esa última coletilla importa, porque un mercado puede ser una tendencia alcista limpia en el diario construida a partir de decenas de rangos horarios.»
  - S036 [31w] «Elige la temporalidad en la que operas y lee la estructura en *esa*, de forma consistente, en vez de saltar entre niveles de zoom para justificar una posición que ya tienes.»
  - S042 [43w] «Una zona funciona por la memoria: los traders recuerdan dónde reaccionó el precio antes y vuelven a actuar allí, lo que es en parte una profecía autocumplida — los compradores colocan órdenes en un soporte antiguo porque esperan que *otros* compradores hagan lo mismo.»
  - S044 [35w] «Cuando el precio rompe de forma convincente *a través* de una zona, esa zona suele darse la vuelta: una resistencia rota tiende a convertirse en soporte, y un soporte roto tiende a convertirse en resistencia.»
  - S045 [37w] «El porqué es humano: los traders que vendieron en la vieja resistencia y vieron al precio marcharse sin ellos ahora quieren una segunda oportunidad, así que compran el retest, convirtiendo el viejo techo en un nuevo suelo.»
  - S051 [37w] «Usa el grupo de reacciones: deja que los *cuerpos* de las velas definan el núcleo de la zona y las *mechas* marquen su borde exterior, ya que una mecha es precio que se tocó y fue rechazado.»
  - S052 [40w] «Y pondera por temporalidad: una zona trazada con giros diarios la vigilan muchos más participantes que una que encontraste en el gráfico de 1 minuto, así que merece mucho más respeto (la misma lógica de temporalidad de la lección anterior).»
  - S059 [48w] «Un nivel es una *probabilidad*, no un muro, y el trader que trata el soporte como un suelo garantizado promedia a la baja en una posición perdedora en largo «porque tiene que rebotar aquí», se salta el stop y le entrega su cuenta al mercado cuando no rebota.»
  - S067 [38w] «Con menos órdenes en reposo, una venta a mercado relativamente pequeña —o una caza de stops deliberada— puede empujar el precio limpiamente *a través* de una zona de soporte y devolverlo de golpe en una o dos velas.»
  - S070 [40w] «En una altcoin de baja capitalización la liquidez en reposo es tan fina que un solo actor grande puede barrer un nivel casi a voluntad, así que allí las zonas son mucho menos fiables que las mismas zonas en BTC.»
  - S071 [51w] «En un perpetuo con tendencia fuerte, cuando el posicionamiento se vuelve de un solo lado (ver el funding, más adelante), un movimiento brusco puede disparar una cascada de cierres forzosos —liquidaciones— que perfora un nivel mucho más allá de donde lo llevaría el flujo de órdenes genuino, y luego se recupera.»
  - S073 [33w **aside-only** (26w without asides)] «Una tendencia es una secuencia, no una dirección —máximos más altos y mínimos más altos—, y se rompe solo cuando un retroceso perfora el mínimo más alto anterior, no cuando el precio cae.»
  - S074 [41w] «Un rango es equilibrio y el estado por defecto del mercado, y las tácticas son opuestas: operar a favor de la tendencia y contra los extremos del rango, así que la primera pregunta es siempre "¿tendencia o rango, en mi temporalidad?".»
  - S075 [40w] «Los soportes y las resistencias son bandas, no líneas, se invierten de rol al romperse, y en un libro poco profundo 24/7 una ruptura solo por la mecha conviene esperarla hasta que una vela cierre más allá de la zona.»
- **9 Course-coined term** (1)
  - S018 [escalera [seed]] «A la izquierda, una tendencia: una escalera de máximos y mínimos crecientes.»
- **10 Metaphor then gloss** (1)
  - S018 ["una escalera de máximos y mínimos crecientes" — metaphor glossed in the same breath] «A la izquierda, una tendencia: una escalera de máximos y mínimos crecientes.»
- **11 Synonym rotation** (1)
  - S002 [S/R area: zonas (S002, S044), banda (S040, S050), nivel (S038, S059)] 
- **A absolutes** (3)
  - S033 [nunca] «Así que la primera pregunta nunca es "¿arriba o abajo?".»
  - S057 [siempre] «La segunda es más cara: que un nivel siempre aguanta.»
  - S074 [siempre, summary] «Un rango es equilibrio y el estado por defecto del mercado, y las tácticas son opuestas: operar a favor de la tendencia y contra los extremos del rango, así que la primera pregunta es siempre "¿tendencia o rango, en mi temporalidad?".»

**EN** — 25 hits, 76 sentences, density 32.9

- **1 Filler** (5)
  - S010 [other filler: announcer "The why is simple:"] «The why is simple: a trend exists only while one side keeps winning the auction.»
  - S026 [exactly: "which is exactly why"] «Trends are the exception, because a sustained one-sided imbalance is expensive to maintain and rare — which is exactly why a real trend is worth riding when you find one.»
  - S039 [other filler: announcer sentence "Here is *why*, mechanically:"] «Here is *why*, mechanically:»
  - S056 [exactly: "which is exactly what price does at an edge"] «Read it as a band and that same wick is just price testing the edge — which is exactly what price does at an edge.»
  - S069 [exactly: "which is exactly why volume… matters"] «The break looks real on the chart but had almost no volume or participation behind it (which is exactly why volume from the last lesson matters).»
- **2 Rhythmic triad** (1)
  - S059 ["adds to a losing long…, skips the stop, and hands the market their account" — drop "hands the market their account"] «A level is a *probability*, not a wall, and the trader who treats support as a guaranteed floor adds to a losing long "because it has to bounce here," skips the stop, and hands the market their account when it doesn't.»
- **4 Summary/uplift closer** (4)
  - S003 [motivate: intro ends "it is the single most important question you can put to a chart"] «It is not decoration on top of the last lesson; it is the single most important question you can put to a chart, because it decides which tactics even make sense.»
  - S016 [restate: "One dip does not do it; a *lower low* does." repeats S012/S015] «One dip does not do it; a *lower low* does.»
  - S061 [motivate: "Your job is to be positioned for the day this one does."] «Your job is to be positioned for the day this one does.»
  - S073 [editorial: lesson's last prose unit ends "Another false break dressed up as a structural one."] «Another false break dressed up as a structural one.»
- **5 Sentence over 30 words** (12)
  - S003 [31w] «It is not decoration on top of the last lesson; it is the single most important question you can put to a chart, because it decides which tactics even make sense.»
  - S027 [36w] «For example, BTC spending two weeks bouncing between roughly 59,000 and 62,000, printing three highs near 62k and three lows near 59k, is ranging — even though any single day inside it might look like a mini-trend.»
  - S042 [36w] «A zone works because of memory: traders remember where price reacted before and act there again, which is partly self-fulfilling — buyers place bids into an old support because they expect *other* buyers to do the same.»
  - S045 [36w] «The why is human — the traders who sold at the old resistance and watched price leave without them now want a second chance, so they buy the retest, turning the old ceiling into a new floor.»
  - S051 [32w] «Use the cluster of reactions: let the candle *bodies* define the core of the zone and the *wicks* mark its outer edge, since a wick is price that was touched and rejected.»
  - S052 [38w **aside-only** (30w without asides)] «And weight by timeframe — a zone drawn from daily swings is watched by far more participants than one you found on the 1-minute chart, so it deserves far more respect (the same timeframe logic from the last lesson).»
  - S059 [41w] «A level is a *probability*, not a wall, and the trader who treats support as a guaranteed floor adds to a losing long "because it has to bounce here," skips the stop, and hands the market their account when it doesn't.»
  - S068 [31w **aside-only** (26w without asides)] «With fewer resting orders, a relatively small market sell — or a deliberate stop hunt — can spike price cleanly *through* a support zone and snap right back within one or two candles.»
  - S071 [35w] «On a small-cap altcoin the resting liquidity is so thin that a single large player can sweep a level almost at will, so zones there are far less trustworthy than the same zones on BTC.»
  - S072 [39w] «In a strongly trending perpetual, when positioning gets one-sided (see funding, later), a sharp move can trigger a cascade of forced closes — liquidations — that briefly pierces a level far past where genuine order flow would take it, then recovers.»
  - S075 [36w] «A range is balance and the market's default state, and the tactics are opposites: trade with a trend, fade the edges of a range, so the first question is always "trending or ranging, on my timeframe?".»
  - S076 [35w] «Support and resistance are bands, not lines, they flip roles once broken, and on a thin 24/7 book a break on the wick alone is worth waiting out until a candle closes beyond the zone.»
- **9 Course-coined term** (1)
  - S018 [staircase/ladder [seed]] «On the left, a trend: a staircase of higher highs and higher lows.»
- **10 Metaphor then gloss** (1)
  - S018 ["a staircase of higher highs and higher lows" — metaphor glossed in the same breath] «On the left, a trend: a staircase of higher highs and higher lows.»
- **11 Synonym rotation** (1)
  - S002 [S/R area: zones (S002, S044), band (S040, S050), level (S038, S059)] 
- **A absolutes** (3)
  - S033 [never] «So the first question is never "up or down?»
  - S057 [always] «The second is more expensive: that a level always holds.»
  - S075 [always, summary] «A range is balance and the market's default state, and the tactics are opposites: trade with a trend, fade the edges of a range, so the first question is always "trending or ranging, on my timeframe?".»

### m04-l1

**ES** — 44 hits, 67 sentences, density 65.7

- **1 Filler** (15)
  - S001 [de verdad: "el instrumento que de verdad usa la mayoría" (brief's own example)] «Un futuro perpetuo —un "perp"— es el instrumento que de verdad usa la mayoría de traders de cripto, y apenas existe fuera de cripto.»
  - S004 [exactamente: "sigue exactamente donde estaba"] «Compras el contrato y ganas cuando ese precio sube; la moneda en sí no se mueve —sigue exactamente donde estaba, en la cartera de otra persona—.»
  - S006 [simplemente: "un perp simplemente sigue corriendo"] «Un futuro tradicional liquida un día fijado; un perp simplemente sigue corriendo, indefinidamente.»
  - S007 [honesto: "mantiene honesto a un futuro", figurative honesty applied to an instrument (= tied to spot)] «Esa única decisión de diseño —la de no vencer— es la semilla de todo lo que viene abajo, porque elimina la fuerza natural que normalmente mantiene honesto a un futuro, y hay que inventar algo que la sustituya.»
  - S012 [exactamente: "exactamente tan nativo como un largo", emphatic] «No has pedido prestada ni vendido ninguna moneda real para hacerlo; el contrato es simétrico, así que un corto es exactamente tan nativo como un largo.»
  - S022 [simplemente: intensifier] «El último precio (last) es simplemente el precio de la operación más reciente *en ese exchange concreto*.»
  - S026 [other filler: "—lo más importante—" interjected intensifier] «Tu PnL no realizado y —lo más importante— tu nivel de liquidación se miden contra el precio de marca, no contra el último precio.»
  - S029 [justamente: emphatic "existe justamente para que"] «El precio de marca existe justamente para que una operación manipulada o accidental no pueda terminar tu posición.»
  - S031 [de verdad: "que aquel gráfico marca de verdad"] «Ahora una plataforma fina imprime una mecha de último precio hasta 8.500 durante un segundo —por debajo de tu número de 8.597,50— mientras el índice entre plataformas, y por tanto el precio de marca, nunca baja del 9.314 que aquel gráfico marca de verdad.»
  - S033 [de verdad: "el único precio que de verdad puede disparar"] «El último precio atravesó de lleno el nivel que *parece* tu liquidación, pero el único precio que de verdad puede disparar el cierre forzoso —el mark— se quedó cómodamente por encima.»
  - S043 [exactamente: "es exactamente lo que lo empuja"] «Si el funding es fuertemente positivo, un trader puede ponerse corto en el perp para cobrar el funding mientras compra spot para cubrir el riesgo de precio, y esa venta extra del perp es exactamente lo que lo empuja de nuevo hacia el spot.»
  - S061 [other filler: announcer "Esto tiene implicaciones prácticas reales:"] «Esto tiene implicaciones prácticas reales: una posición saturada sigue pagando funding durante todo el fin de semana mientras los mercados tradicionales duermen, y la escasa liquidez de las madrugadas y los festivos es justo cuando más probable es que aparezca una mecha del último precio, que es justo cuando más importa el precio de marca.»
  - S061 [other filler: emphatic "es justo cuando… que es justo cuando" (twice)] «Esto tiene implicaciones prácticas reales: una posición saturada sigue pagando funding durante todo el fin de semana mientras los mercados tradicionales duermen, y la escasa liquidez de las madrugadas y los festivos es justo cuando más probable es que aparezca una mecha del último precio, que es justo cuando más importa el precio de marca.»
  - S064 [de verdad: "el número que de verdad puede terminar tu posición"] «Y nunca planifiques tu riesgo según el último precio: el número que de verdad puede terminar tu posición es el precio de marca.»
  - S065 [exactamente: "exactamente tan nativo como un largo"] «Un futuro perpetuo es un contrato sin fecha de vencimiento: nunca tocas la moneda, el exchange solo liquida la diferencia en el valor del contrato y un corto es exactamente tan nativo como un largo.»
- **4 Summary/uplift closer** (5)
  - S020 [restate: "El contrato es una transferencia de suma cero…; la moneda quedó intacta todo el tiempo." repeats S018-S019] «El contrato es una transferencia de suma cero entre los dos lados; la moneda quedó intacta todo el tiempo.»
  - S029 [restate: "El precio de marca existe justamente para que…" repeats S027-S028] «El precio de marca existe justamente para que una operación manipulada o accidental no pueda terminar tu posición.»
  - S033 [restate: repeats S031-S032 (last wick crossed, mark held)] «El último precio atravesó de lleno el nivel que *parece* tu liquidación, pero el único precio que de verdad puede disparar el cierre forzoso —el mark— se quedó cómodamente por encima.»
  - S044 [editorial: "El amarre no es magia; es un incentivo pagado."] «El amarre no es magia; es un incentivo pagado.»
  - S064 [restate: lesson's last prose unit ends re-stating the mark-price rule taught in blocks 11-12] «Y nunca planifiques tu riesgo según el último precio: el número que de verdad puede terminar tu posición es el precio de marca.»
- **5 Sentence over 30 words** (17)
  - S007 [38w] «Esa única decisión de diseño —la de no vencer— es la semilla de todo lo que viene abajo, porque elimina la fuerza natural que normalmente mantiene honesto a un futuro, y hay que inventar algo que la sustituya.»
  - S014 [33w] «Eso es lo que te permite ponerte corto con la misma facilidad que largo: no hay ninguna moneda que localizar y pedir prestada antes, solo un contrato del que tomar el otro lado.»
  - S024 [31w **aside-only** (22w without asides)] «El precio de marca (mark) es un valor justo suavizado, construido a partir del índice más amplio de precios spot en varias plataformas (más un pequeño ajuste basado en el funding).»
  - S028 [35w] «Si el nivel de cierre forzoso siguiera la última operación, una sola mecha momentánea en una plataforma fina podría cerrar a la fuerza miles de posiciones que por lo demás estaban sanas, en un instante.»
  - S031 [44w] «Ahora una plataforma fina imprime una mecha de último precio hasta 8.500 durante un segundo —por debajo de tu número de 8.597,50— mientras el índice entre plataformas, y por tanto el precio de marca, nunca baja del 9.314 que aquel gráfico marca de verdad.»
  - S033 [31w **aside-only** (29w without asides)] «El último precio atravesó de lleno el nivel que *parece* tu liquidación, pero el único precio que de verdad puede disparar el cierre forzoso —el mark— se quedó cómodamente por encima.»
  - S039 [33w] «Un futuro tradicional tiene un ancla incorporada: al vencimiento *tiene* que igualar al spot, o hay dinero gratis, así que el arbitraje arrastra a ambos juntos a medida que se acerca la fecha.»
  - S042 [32w] «Al hacer que el lado saturado pague al otro lado, hace dos cosas a la vez: desanima a la multitud de amontonarse y paga a los arbitrajistas por tomar el lado contrario.»
  - S043 [44w] «Si el funding es fuertemente positivo, un trader puede ponerse corto en el perp para cobrar el funding mientras compra spot para cubrir el riesgo de precio, y esa venta extra del perp es exactamente lo que lo empuja de nuevo hacia el spot.»
  - S051 [40w] «En un rally eufórico la tasa puede dispararse a +0,1% por ventana: ahora `10.000 × 0,001 = 10 USDT` cada ocho horas, 30 USDT/día —el 0,3% de tu nocional cada día—, sangrando de un largo saturado se mueva el precio a tu favor o no.»
  - S056 [62w **aside-only** (24w without asides)] «Dos cosas que la gente pasa por alto por esto: no siempre eres el que paga (en el lado impopular *cobras* funding, que es un ingreso real, aunque pequeño), y nunca deberías presupuestarlo como una comisión fija —una tasa que es ruido una semana puede convertirse sin hacer ruido en el mayor coste de una posición de varios días a la siguiente—.»
  - S059 [46w] «Los mercados de futuros tradicionales cierran los fines de semana y por la noche y liquidan en fechas fijas; el perpetuo —con un amarre de funding en lugar de un vencimiento— se popularizó en los exchanges de cripto y encaja con un mercado que nunca cierra.»
  - S061 [55w] «Esto tiene implicaciones prácticas reales: una posición saturada sigue pagando funding durante todo el fin de semana mientras los mercados tradicionales duermen, y la escasa liquidez de las madrugadas y los festivos es justo cuando más probable es que aparezca una mecha del último precio, que es justo cuando más importa el precio de marca.»
  - S063 [33w] «Una tasa pequeña es ruido; una grande y persistente es el mercado cobrándote alquiler por quedarte en una operación saturada, y de vez en cuando un ingreso, si estás en el lado tranquilo.»
  - S065 [35w] «Un futuro perpetuo es un contrato sin fecha de vencimiento: nunca tocas la moneda, el exchange solo liquida la diferencia en el valor del contrato y un corto es exactamente tan nativo como un largo.»
  - S066 [40w] «Como no hay vencimiento que lo ancle al spot, el funding —un pago entre largos y cortos cada ocho horas— es el sustituto fabricado, y el lado saturado puede pagar el 0,3% de su nocional al día por estar ahí.»
  - S067 [32w] «Las liquidaciones siguen el precio de marca y nunca el último precio, y por eso una mecha en una sola plataforma fina no termina una posición que el gráfico hace parecer condenada.»
- **9 Course-coined term** (3)
  - S044 [non-seed "amarre" (tether): "El amarre no es magia; es un incentivo pagado."] «El amarre no es magia; es un incentivo pagado.»
  - S059 [non-seed "amarre de funding": "con un amarre de funding en lugar de un vencimiento"] «Los mercados de futuros tradicionales cierran los fines de semana y por la noche y liquidan en fechas fijas; el perpetuo —con un amarre de funding en lugar de un vencimiento— se popularizó en los exchanges de cripto y encaja con un mercado que nunca cierra.»
  - S063 [non-seed "lado tranquilo" (quiet side) used as a name for the uncrowded side] «Una tasa pequeña es ruido; una grande y persistente es el mercado cobrándote alquiler por quedarte en una operación saturada, y de vez en cuando un ingreso, si estás en el lado tranquilo.»
- **10 Metaphor then gloss** (1)
  - S039 ["un ancla incorporada: al vencimiento *tiene* que igualar al spot" — metaphor glossed after colon] «Un futuro tradicional tiene un ancla incorporada: al vencimiento *tiene* que igualar al spot, o hay dinero gratis, así que el arbitraje arrastra a ambos juntos a medida que se acerca la fecha.»
- **11 Synonym rotation** (3)
  - S007 [perp-to-spot anchoring: "fuerza natural que mantiene honesto a un futuro" (S007), ancla (S039, S040), amarre (S044, S059)] 
  - S026 [liquidation: nivel de liquidación (S026), nivel de cierre forzoso (S028, S030), terminar tu posición (S029, S064)] 
  - S042 [non-crowded side: el otro lado / lado contrario (S042), lado impopular (S056), lado tranquilo (S063)] 
- **A absolutes** (9)
  - S002 [nunca] «No es una moneda y nunca tocas el activo subyacente.»
  - S013 [nunca] «Como nunca posees el activo, el exchange solo liquida la diferencia en el valor del contrato, normalmente en una stablecoin como USDT.»
  - S031 [nunca] «Ahora una plataforma fina imprime una mecha de último precio hasta 8.500 durante un segundo —por debajo de tu número de 8.597,50— mientras el índice entre plataformas, y por tanto el precio de marca, nunca baja del 9.314 que aquel gráfico marca de verdad.»
  - S040 [nunca] «Un perp nunca vence, así que ese ancla desaparece: nada arrastra *automáticamente* su precio de vuelta hacia el spot.»
  - S056 [siempre, nunca, deberías] «Dos cosas que la gente pasa por alto por esto: no siempre eres el que paga (en el lado impopular *cobras* funding, que es un ingreso real, aunque pequeño), y nunca deberías presupuestarlo como una comisión fija —una tasa que es ruido una semana puede convertirse sin hacer ruido en el mayor coste de una posición de varios días a la siguiente—.»
  - S059 [nunca] «Los mercados de futuros tradicionales cierran los fines de semana y por la noche y liquidan en fechas fijas; el perpetuo —con un amarre de funding en lugar de un vencimiento— se popularizó en los exchanges de cripto y encaja con un mercado que nunca cierra.»
  - S064 [nunca] «Y nunca planifiques tu riesgo según el último precio: el número que de verdad puede terminar tu posición es el precio de marca.»
  - S065 [nunca, summary] «Un futuro perpetuo es un contrato sin fecha de vencimiento: nunca tocas la moneda, el exchange solo liquida la diferencia en el valor del contrato y un corto es exactamente tan nativo como un largo.»
  - S067 [nunca, summary] «Las liquidaciones siguen el precio de marca y nunca el último precio, y por eso una mecha en una sola plataforma fina no termina una posición que el gráfico hace parecer condenada.»

**EN** — 39 hits, 67 sentences, density 58.2

- **1 Filler** (16)
  - S001 [actually: "the instrument most crypto traders actually use"] «A perpetual future — a "perp" — is the instrument most crypto traders actually use, and it barely exists outside crypto.»
  - S004 [exactly: "it stays exactly where it was"] «Buy the contract and you profit when that price rises; the coin itself never moves — it stays exactly where it was, in someone else's wallet.»
  - S006 [other filler: "a perp just keeps running"] «A traditional future settles on a set day; a perp just keeps running, indefinitely.»
  - S007 [honest: "keeps a future honest", figurative honesty applied to an instrument] «That single design choice — no expiry — is the seed of everything below, because it removes the natural force that normally keeps a future honest, and something has to be invented to replace it.»
  - S012 [exactly: "exactly as native as a long", emphatic] «You did not borrow or sell any real coin to do this; the contract is symmetric, so a short is exactly as native as a long.»
  - S022 [simply: intensifier] «Last price is simply the price of the most recent trade *on that one exchange*.»
  - S026 [other filler: "— critically —" interjected intensifier] «Your unrealised PnL and — critically — your liquidation level are measured against the mark price, not the last price.»
  - S029 [precisely: emphatic "exists precisely so that"] «The mark price exists precisely so that one manipulated or accidental print cannot end your position.»
  - S031 [actually: "that chart actually prints"] «Now one thin exchange prints a last-price wick down to 8,500 for a second — below your 8,597.50 number — while the cross-venue index, and therefore the mark price, never drops under the 9,314 that chart actually prints.»
  - S033 [actually: "the only price that can actually trigger"] «The last price stabbed straight through the level that *looks* like your liquidation, but the only price that can actually trigger the forced close — the mark — stayed comfortably above it.»
  - S043 [exactly: "is exactly what pushes it back"] «If funding is strongly positive, a trader can short the perp to collect the funding while buying spot to hedge the price risk — and that extra selling of the perp is exactly what pushes it back down toward spot.»
  - S061 [exactly: "is exactly when a last-price wick is most likely"] «That has practical edges: a crowded position keeps paying funding straight through the weekend while traditional markets sleep, and the thin liquidity of late nights and holidays is exactly when a last-price wick is most likely to appear — which is exactly when the mark price matters most.»
  - S061 [exactly: "which is exactly when the mark price matters most"] «That has practical edges: a crowded position keeps paying funding straight through the weekend while traditional markets sleep, and the thin liquidity of late nights and holidays is exactly when a last-price wick is most likely to appear — which is exactly when the mark price matters most.»
  - S061 [other filler: announcer "That has practical edges:"] «That has practical edges: a crowded position keeps paying funding straight through the weekend while traditional markets sleep, and the thin liquidity of late nights and holidays is exactly when a last-price wick is most likely to appear — which is exactly when the mark price matters most.»
  - S064 [actually: "the number that can actually end your position"] «And never plan your risk around the last price: the number that can actually end your position is the mark price.»
  - S065 [exactly: "exactly as native as a long"] «A perpetual future is a contract with no expiry date: you never touch the coin, the exchange settles only the difference in the contract's value, and a short is exactly as native as a long.»
- **4 Summary/uplift closer** (5)
  - S020 [restate: "The contract is a zero-sum transfer…; the coin sat untouched the whole time." repeats S018-S019] «The contract is a zero-sum transfer between the two sides; the coin sat untouched the whole time.»
  - S029 [restate: "The mark price exists precisely so that…" repeats S027-S028] «The mark price exists precisely so that one manipulated or accidental print cannot end your position.»
  - S033 [restate: repeats S031-S032] «The last price stabbed straight through the level that *looks* like your liquidation, but the only price that can actually trigger the forced close — the mark — stayed comfortably above it.»
  - S044 [editorial: "The tether is not magic; it is a paid incentive."] «The tether is not magic; it is a paid incentive.»
  - S064 [restate: lesson's last prose unit ends re-stating the mark-price rule] «And never plan your risk around the last price: the number that can actually end your position is the mark price.»
- **5 Sentence over 30 words** (11)
  - S007 [33w] «That single design choice — no expiry — is the seed of everything below, because it removes the natural force that normally keeps a future honest, and something has to be invented to replace it.»
  - S031 [36w] «Now one thin exchange prints a last-price wick down to 8,500 for a second — below your 8,597.50 number — while the cross-venue index, and therefore the mark price, never drops under the 9,314 that chart actually prints.»
  - S042 [31w] «By making the crowded side pay the other side, it does two jobs at once: it discourages the crowd from piling on, and it pays arbitrageurs to take the opposite side.»
  - S043 [39w] «If funding is strongly positive, a trader can short the perp to collect the funding while buying spot to hedge the price risk — and that extra selling of the perp is exactly what pushes it back down toward spot.»
  - S051 [38w] «In a euphoric rally the rate can run to +0.1% per window: now `10,000 × 0.001 = 10 USDT` every eight hours, 30 USDT/day — 0.3% of your notional every day, bleeding out of a crowded long whether or not price moves your way.»
  - S056 [57w] «Two things people miss because of this: you are not always the payer (on the unpopular side you *receive* funding, which is a real, if small, income), and you should never budget it like a fixed commission — a rate that is noise one week can quietly become the single largest cost of a multi-day position the next.»
  - S059 [35w **aside-only** (27w without asides)] «Traditional futures markets close on weekends and overnight and settle on fixed dates; the perpetual — with a funding tether instead of an expiry — was popularised on crypto exchanges and fits a market that never closes.»
  - S061 [47w] «That has practical edges: a crowded position keeps paying funding straight through the weekend while traditional markets sleep, and the thin liquidity of late nights and holidays is exactly when a last-price wick is most likely to appear — which is exactly when the mark price matters most.»
  - S063 [32w] «A small rate is noise; a persistently large one is the market charging you rent to sit in a crowded trade — and occasionally an income, if you are on the quiet side.»
  - S065 [35w] «A perpetual future is a contract with no expiry date: you never touch the coin, the exchange settles only the difference in the contract's value, and a short is exactly as native as a long.»
  - S066 [36w **aside-only** (27w without asides)] «Because no expiry anchors it to spot, funding — a payment between longs and shorts every eight hours — is the manufactured replacement, and the crowded side can pay 0.3% of its notional a day for the privilege.»
- **9 Course-coined term** (3)
  - S044 [non-seed "tether": "The tether is not magic; it is a paid incentive."] «The tether is not magic; it is a paid incentive.»
  - S059 [non-seed "funding tether": "with a funding tether instead of an expiry"] «Traditional futures markets close on weekends and overnight and settle on fixed dates; the perpetual — with a funding tether instead of an expiry — was popularised on crypto exchanges and fits a market that never closes.»
  - S063 [non-seed "the quiet side" used as a name for the uncrowded side] «A small rate is noise; a persistently large one is the market charging you rent to sit in a crowded trade — and occasionally an income, if you are on the quiet side.»
- **10 Metaphor then gloss** (1)
  - S039 ["a built-in anchor: at expiry it *must* equal spot" — metaphor glossed after colon] «A traditional future has a built-in anchor: at expiry it *must* equal spot, or there is free money, so arbitrage drags the two together as the date approaches.»
- **11 Synonym rotation** (3)
  - S007 [perp-to-spot anchoring: "the natural force that normally keeps a future honest" (S007), anchor (S039, S040), tether (S044, S059)] 
  - S026 [liquidation: liquidation level (S026), forced-close level (S028, S030), end your position (S029, S064)] 
  - S042 [non-crowded side: the other/opposite side (S042), the unpopular side (S056), the quiet side (S063)] 
- **A absolutes** (11)
  - S002 [never] «It is not a coin, and you never touch the underlying asset.»
  - S004 [never] «Buy the contract and you profit when that price rises; the coin itself never moves — it stays exactly where it was, in someone else's wallet.»
  - S013 [never] «Because you never own the asset, the exchange only ever settles the difference in the contract's value, usually in a stablecoin like USDT.»
  - S031 [never] «Now one thin exchange prints a last-price wick down to 8,500 for a second — below your 8,597.50 number — while the cross-venue index, and therefore the mark price, never drops under the 9,314 that chart actually prints.»
  - S039 [must] «A traditional future has a built-in anchor: at expiry it *must* equal spot, or there is free money, so arbitrage drags the two together as the date approaches.»
  - S040 [never] «A perp never expires, so that anchor is gone — nothing *automatically* pulls its price back toward spot.»
  - S056 [always, never] «Two things people miss because of this: you are not always the payer (on the unpopular side you *receive* funding, which is a real, if small, income), and you should never budget it like a fixed commission — a rate that is noise one week can quietly become the single largest cost of a multi-day position the next.»
  - S059 [never] «Traditional futures markets close on weekends and overnight and settle on fixed dates; the perpetual — with a funding tether instead of an expiry — was popularised on crypto exchanges and fits a market that never closes.»
  - S064 [never] «And never plan your risk around the last price: the number that can actually end your position is the mark price.»
  - S065 [never, summary] «A perpetual future is a contract with no expiry date: you never touch the coin, the exchange settles only the difference in the contract's value, and a short is exactly as native as a long.»
  - S067 [never, summary] «Liquidation tracks the mark price and never the last price, which is why a wick on one thin venue does not end a position the chart makes look doomed.»

### m05-l1

**ES** — 32 hits, 67 sentences, density 47.8

- **1 Filler** (6)
  - S008 [de verdad: "lo que aportas de verdad"] «El margen es lo que aportas de verdad: un depósito que el exchange retiene como colateral.»
  - S010 [exactamente: "es exactamente la proporción", emphatic in a definition] «El apalancamiento es exactamente la proporción entre el nocional que controlas y el margen que aportas.»
  - S019 [justamente: emphatic "es justamente la fracción"] «Por qué: el apalancamiento es justamente la fracción del nocional que el exchange te obliga a financiar por adelantado.»
  - S037 [other filler: announcer sentence "Aquí está lo que el marketing cuenta mal."] «Aquí está lo que el marketing cuenta mal.»
  - S054 [realmente: "el dinero realmente en riesgo", contrast already carried by the sentence] «La cantidad que tenía en mente y el dinero realmente en riesgo nunca fueron la misma cifra.»
  - S064 [exactamente: "ante exactamente la misma noticia", emphatic] «Una posición que habría sobrevivido un día entre semana puede cerrarse a la fuerza durante el fin de semana ante exactamente la misma noticia.»
- **2 Rhythmic triad** (2)
  - S043 ["Corta por ambos lados, siempre, y de forma idéntica" — drop "y de forma idéntica" (overlaps "por ambos lados")] «Corta por ambos lados, siempre, y de forma idéntica.»
  - S062 ["no hay cierre diario ni cortacircuitos… ni un hueco de sesión tras el que resguardarse" — drop "ni un hueco de sesión" (overlaps cierre diario)] «Cripto opera 24/7, así que no hay cierre diario ni cortacircuitos que pausen un movimiento, ni un hueco de sesión tras el que resguardarse: pueden liquidarte a las 3 de la madrugada de un domingo.»
- **4 Summary/uplift closer** (3)
  - S025 [ahead: "(Calcular ese precio de liquidación exacto es el próximo módulo.)"] «(Calcular ese precio de liquidación exacto es el próximo módulo.)»
  - S036 [restate: repeats the isolated/cross bullets just above] «El aislado limita el daño de una sola posición; el cruzado usa todo tu saldo para mantener las posiciones vivas, a costa de poner todo ese saldo en juego.»
  - S040 [restate: "Una buena operación es buena y una mala es mala, tanto a 2× como a 50×." repeats S038-S039] «Una buena operación es buena y una mala es mala, tanto a 2× como a 50×.»
- **5 Sentence over 30 words** (13)
  - S011 [38w **aside-only** (20w without asides)] «Ese depósito es a su vez un activo con su propio riesgo —la stablecoin que lo guarda puede perder su paridad, y el bloque de fundamentos ya mostró dos casos—, así que "colateral" nunca es una cifra neutra.»
  - S020 [37w] «El margen de mantenimiento es el capital mínimo que debes conservar para *mantener* la posición abierta: una fracción pequeña del nocional fijada por el exchange (a menudo en torno al 0,5%), muy por debajo del margen inicial.»
  - S022 [33w] «Por qué existe: es el colchón de seguridad del exchange, el punto en el que te cierra *antes* de que tus pérdidas puedan volver negativo tu saldo y dejarle a él la factura.»
  - S024 [53w] «El hueco entre ambos es tu margen de maniobra: en la operación a 10× depositaste 2.000 y te cierran cuando el capital cae a 100, así que tu pérdida puede crecer hasta unos 1.900 USDT —aproximadamente un movimiento adverso del 9,5% sobre un nocional de 20.000— antes de que la posición se liquide.»
  - S033 [33w] «El truco: si el movimiento continúa, la pérdida sigue comiéndose esos 3.000 completos; una sola mala operación puede arrastrar *todo* tu saldo a la liquidación, no solo la cantidad que tenías en mente.»
  - S042 [37w] «En la operación con 2.000 de margen a 10×, un movimiento del 1% a tu favor son 200 USDT sobre el nocional de 20.000: eso es +10% sobre tu margen; un 1% en tu contra es −10%.»
  - S047 [32w] «En cuanto sumas las comisiones y el riesgo de que te liquide el ruido normal *antes* de que tu tesis se cumpla, un apalancamiento alto suele empeorar los resultados esperados, no mejorarlos.»
  - S050 [31w] «Lo único que cambió es que ahora un vaivén diez veces menor lo liquida, y una posición cerrada con pérdida no se recupera cuando el precio vuelve, porque ya no existe.»
  - S059 [38w] «Como las multitudes se agolpan en precios de liquidación parecidos por usar apalancamiento alto, un cierre forzoso es una orden a mercado que empuja el precio hacia el siguiente cúmulo, que fuerza el siguiente cierre, y así sucesivamente.»
  - S062 [35w] «Cripto opera 24/7, así que no hay cierre diario ni cortacircuitos que pausen un movimiento, ni un hueco de sesión tras el que resguardarse: pueden liquidarte a las 3 de la madrugada de un domingo.»
  - S063 [34w] «La liquidez también se adelgaza los fines de semana y festivos, así que un movimiento repentino en un fin de semana tranquilo puede atravesar todo un cúmulo de precios de liquidación con mucho deslizamiento.»
  - S066 [50w] «No aumenta el rendimiento esperado de una operación —el precio sigue teniendo que moverse en la misma dirección y la misma cantidad—: escala ganancias y pérdidas de forma simétrica y acerca tu liquidación a la entrada, hasta que a 50× todo el colchón es en torno al 2% del precio.»
  - S067 [42w] «El margen inicial es el precio de entrada y el de mantenimiento el umbral de liquidación forzosa; el margen aislado limita el daño a la cantidad que elegiste, mientras que el cruzado pone sin avisar todo el saldo detrás de la posición.»
- **9 Course-coined term** (3)
  - S023 [non-seed "precio de entrada" for initial margin (calque of "price of admission"), collides with entry price] «Así que el margen inicial es el precio de entrada; el margen de mantenimiento es el umbral de liquidación forzosa.»
  - S051 [non-seed "riesgo por acierto", italicised as a label] «Más apalancamiento es más *riesgo por acierto*, no más ventaja.»
  - S067 [non-seed "precio de entrada" for initial margin (summary)] «El margen inicial es el precio de entrada y el de mantenimiento el umbral de liquidación forzosa; el margen aislado limita el daño a la cantidad que elegiste, mientras que el cruzado pone sin avisar todo el saldo detrás de la posición.»
- **10 Metaphor then gloss** (2)
  - S022 ["el colchón de seguridad del exchange, el punto en el que te cierra…" — metaphor glossed in apposition] «Por qué existe: es el colchón de seguridad del exchange, el punto en el que te cierra *antes* de que tus pérdidas puedan volver negativo tu saldo y dejarle a él la factura.»
  - S060 ["este bucle de realimentación se pasa de frenada con violencia: la 'mecha de liquidación'…" — metaphor glossed after colon] «En un libro poco profundo de alts, este bucle de realimentación se pasa de frenada con violencia: la "mecha de liquidación" que se dispara y se recupera al instante.»
- **11 Synonym rotation** (3)
  - S003 [being liquidated: barrerte (S003), liquidar (S024), te saca a la fuerza (S044), cierre forzoso (S046)] 
  - S021 [maintenance threshold: suelo (S021), umbral de liquidación forzosa (S023), nivel de mantenimiento (S044)] 
  - S024 [distance to liquidation: hueco (S024), margen de maniobra (S024), colchón (S044, S045, S057)] 
- **A absolutes** (5)
  - S011 [nunca] «Ese depósito es a su vez un activo con su propio riesgo —la stablecoin que lo guarda puede perder su paridad, y el bloque de fundamentos ya mostró dos casos—, así que "colateral" nunca es una cifra neutra.»
  - S016 [debes] «El margen inicial es lo que debes depositar para *abrir* la posición: el nocional dividido entre tu apalancamiento.»
  - S020 [debes] «El margen de mantenimiento es el capital mínimo que debes conservar para *mantener* la posición abierta: una fracción pequeña del nocional fijada por el exchange (a menudo en torno al 0,5%), muy por debajo del margen inicial.»
  - S043 [siempre] «Corta por ambos lados, siempre, y de forma idéntica.»
  - S054 [nunca] «La cantidad que tenía en mente y el dinero realmente en riesgo nunca fueron la misma cifra.»

**EN** — 27 hits, 67 sentences, density 40.3

- **1 Filler** (7)
  - S008 [actually: "what you actually put up"] «The margin is what you actually put up: a deposit the exchange holds as collateral.»
  - S010 [exactly: "is exactly the ratio", emphatic in a definition] «Leverage is exactly the ratio between the notional you control and the margin you post.»
  - S014 [nothing more: sentence-final tag (voice page reference paragraph in ES)] «It is the size of the lever between these two numbers, nothing more.»
  - S019 [precisely: emphatic "is precisely the fraction"] «Why: leverage is precisely the fraction of the notional the exchange makes you fund up front.»
  - S037 [other filler: announcer sentence "Here is the part the marketing gets wrong."] «Here is the part the marketing gets wrong.»
  - S054 [actually: "the money actually at risk"] «The stake they had in mind and the money actually at risk were never the same number.»
  - S064 [other filler: "the very same news", intensifier] «A position that would have survived a weekday can be force-closed over a weekend on the very same news.»
- **2 Rhythmic triad** (2)
  - S043 ["It cuts both ways, always, and identically" — drop "and identically"] «It cuts both ways, always, and identically.»
  - S062 ["no daily close or circuit breaker… and no session gap to hide behind" — drop "no session gap"] «Crypto trades 24/7, so there is no daily close or circuit breaker to pause a move and no session gap to hide behind — you can be liquidated at 3 a.m. on a Sunday.»
- **4 Summary/uplift closer** (3)
  - S025 [ahead: "(Computing that liquidation price exactly is the next module.)"] «(Computing that liquidation price exactly is the next module.)»
  - S036 [restate: repeats the isolated/cross bullets] «Isolated caps the damage from one position; cross uses your full balance to keep positions alive, at the cost of putting that full balance on the line.»
  - S040 [restate: "A good trade is good and a bad trade is bad, at 2× or at 50×." repeats S038-S039] «A good trade is good and a bad trade is bad, at 2× or at 50×.»
- **5 Sentence over 30 words** (8)
  - S011 [32w **aside-only** (17w without asides)] «That deposit is itself an asset with its own risk — the stablecoin holding it can lose its peg, which the foundations block showed happening twice — so "collateral" is never a neutral number.»
  - S024 [46w] «The gap between them is your breathing room: on the 10× trade you posted 2,000 and are closed when equity falls to 100, so your loss can grow to about 1,900 USDT — roughly a 9.5% adverse move on a 20,000 notional — before the position is liquidated.»
  - S033 [34w] «The catch: if the move keeps going, the loss keeps eating into that full 3,000 — a single bad trade can drag your *entire* balance to liquidation, not just the stake you had in mind.»
  - S042 [32w] «On the 2,000-margin trade at 10×, a 1% move in your favour is 200 USDT on the 20,000 notional — that is +10% on your margin; a 1% move against you is −10%.»
  - S050 [31w] «All they changed is that a wiggle ten times smaller now liquidates them — and a position closed at a loss can't recover when price comes back, because it no longer exists.»
  - S062 [33w] «Crypto trades 24/7, so there is no daily close or circuit breaker to pause a move and no session gap to hide behind — you can be liquidated at 3 a.m. on a Sunday.»
  - S066 [47w] «It does not raise the expected return of a trade — the price still has to move the same direction by the same amount — it scales gains and losses symmetrically and moves your liquidation closer to entry, until at 50× the whole cushion is about 2% of price.»
  - S067 [34w] «Initial margin is the price of admission and maintenance margin the eviction line; isolated margin caps the damage at the stake you chose, while cross margin quietly puts the entire balance behind the position.»
- **9 Course-coined term** (3)
  - S023 [non-seed "eviction line" (and "price of admission") as names for maintenance/initial margin] «So initial margin is the price of admission; maintenance margin is the eviction line.»
  - S051 [non-seed "risk per correct call", italicised as a label] «More leverage is more *risk per correct call*, not more edge.»
  - S067 [non-seed "eviction line" / "price of admission" (summary)] «Initial margin is the price of admission and maintenance margin the eviction line; isolated margin caps the damage at the stake you chose, while cross margin quietly puts the entire balance behind the position.»
- **10 Metaphor then gloss** (1)
  - S022 ["the exchange's safety buffer, the point at which it closes you…" — metaphor glossed in apposition] «Why it exists: it is the exchange's safety buffer, the point at which it closes you *before* your losses can turn your balance negative and leave it holding the bill.»
- **11 Synonym rotation** (3)
  - S003 [being liquidated: wiped out (S003), eviction line (S023), liquidated (S024), forces you out (S044), forced close (S046)] 
  - S021 [maintenance threshold: floor (S021), eviction line (S023), maintenance level (S044)] 
  - S024 [distance to liquidation: gap (S024), breathing room (S024), cushion (S044, S045, S057)] 
- **A absolutes** (5)
  - S011 [never] «That deposit is itself an asset with its own risk — the stablecoin holding it can lose its peg, which the foundations block showed happening twice — so "collateral" is never a neutral number.»
  - S016 [must] «Initial margin is what you must post to *open* the position — the notional divided by your leverage.»
  - S020 [must] «Maintenance margin is the minimum equity you must keep to *hold* the position open — a small, exchange-set fraction of the notional (often around 0.5%), well below the initial margin.»
  - S043 [always] «It cuts both ways, always, and identically.»
  - S054 [never] «The stake they had in mind and the money actually at risk were never the same number.»

### m06-l1

**ES** — 31 hits, 52 sentences, density 59.6

- **1 Filler** (3)
  - S028 [de verdad: "lo que el apalancamiento cambia de verdad"] «La misma operación, con una distancia de supervivencia radicalmente distinta: eso es lo que el apalancamiento cambia de verdad.»
  - S030 [de verdad: "tiene que cerrar de verdad la posición en el mercado" (contrast already carried by "en el mercado")] «Una liquidación no es un apunte sobre el papel: el exchange tiene que cerrar de verdad la posición en el mercado.»
  - S044 [other filler: "es directamente temerario", intensifier] «El mismo apalancamiento que en BTC es solo arriesgado, en una alt fina es directamente temerario.»
- **2 Rhythmic triad** (1)
  - S029 ["ni tu entrada, ni tu dirección, ni el mercado" — drop "ni el mercado" (rhythmic third)] «El apalancamiento no cambia tu entrada, ni tu dirección, ni el mercado; solo cambia *cuánto aire tiene el precio para respirar antes de matarte*.»
- **4 Summary/uplift closer** (4)
  - S004 [motivate: "Si no, el apalancamiento te controla a ti."] «Si no, el apalancamiento te controla a ti.»
  - S009 [restate: repeats S008 (exchange closes before balance goes negative)] «La liquidación es el exchange protegiéndose a sí mismo primero; el colchón de margen de mantenimiento es la porción que se reserva para que el cierre forzoso ocurra *antes* de que tu equity llegue a cero, no después.»
  - S023 [restate: "La fórmula no es más que…" re-says S022] «La fórmula no es más que "cuánto puede moverse el precio antes de que mi margen aportado, menos el colchón del exchange, se agote".»
  - S029 [editorial: "solo cambia cuánto aire tiene el precio para respirar antes de matarte" re-says S027-S028] «El apalancamiento no cambia tu entrada, ni tu dirección, ni el mercado; solo cambia *cuánto aire tiene el precio para respirar antes de matarte*.»
- **5 Sentence over 30 words** (14)
  - S008 [46w] «En cuanto tu capital neto (equity) cae hasta ese suelo, el exchange cierra la posición para evitar que tu saldo se vuelva negativo, porque en una posición apalancada tus pérdidas pueden superar lo que aportaste, y es el exchange, no tú, quien responde por el déficit.»
  - S009 [38w] «La liquidación es el exchange protegiéndose a sí mismo primero; el colchón de margen de mantenimiento es la porción que se reserva para que el cierre forzoso ocurra *antes* de que tu equity llegue a cero, no después.»
  - S019 [36w] «La misma operación en margen cruzado, respaldada por un saldo de 2.000 USDT, puede seguir sangrando hasta consumir buena parte de esos 2.000: la pérdida ya no está acotada por lo que asignaste a la operación.»
  - S020 [43w **aside-only** (28w without asides)] «Para un perpetuo lineal (margen en USDT), ignorando comisiones, el precio de liquidación aislado depende de dos tasas: la tasa de margen inicial (= 1 / apalancamiento) y la tasa de margen de mantenimiento `mmr` (una fracción pequeña fijada por el exchange, p. ej. 0,5%).»
  - S022 [49w] «Con 10× aportas `1/10 = 10%` del nocional, así que un movimiento en contra del 10% borra ese 10%, salvo que el exchange se queda con el último 0,5% (el `mmr`) antes de que desaparezca del todo, por lo que la posición muere a un 9,5% de distancia, no al 10%.»
  - S025 [32w] «Tu colchón de margen es `1/10 = 10%` del precio, menos el 0,5% que retiene el exchange, así que el precio solo tiene que caer alrededor de un 9,5% antes de que te liquiden:»
  - S033 [41w] «En un libro poco profundo o desequilibrado, esa venta forzosa empuja el precio *hacia abajo*, lo que arrastra el precio hasta el siguiente cúmulo de precios de liquidación de longs, que disparan *más* ventas forzosas, que empujan el precio aún más.»
  - S036 [33w] «por esto las "mechas de liquidación" se pasan de frenada tan violentamente y luego vuelven de golpe: el pico es flujo forzoso agotando un libro poco profundo, no información nueva sobre el valor.»
  - S037 [31w] «Y por esto colocar tu propio precio de liquidación *justo dentro* de una zona de liquidación concurrida es peligroso: te pones en fila para ser una de las fichas de dominó.»
  - S043 [34w] «Los pares principales como BTC absorben el flujo forzoso razonablemente bien; las altcoins pequeñas tienen libros poco profundos donde una ola modesta de liquidaciones puede abrir un hueco de varios puntos porcentuales en segundos.»
  - S046 [45w] «El mismo flujo de liquidaciones forzosas que un libro entre semana absorbería empuja el precio mucho más lejos, produciendo las famosas "mechas" de fin de semana que clavan hacia abajo (o hacia arriba), barren un cúmulo de precios de liquidación y se recuperan minutos después.»
  - S050 [46w] «La liquidación es el exchange cerrando a la fuerza una posición porque el equity cayó al margen de mantenimiento, y en un perpetuo lineal su precio es una cuenta que puedes hacer antes de entrar: `entrada × (1 − 1/apalancamiento + mmr)` para un long, y la imagen espejo para un short.»
  - S051 [36w **aside-only** (26w without asides)] «A más apalancamiento, más fino el colchón —alrededor de un 9,5% a 10×, un 1,5% a 50×—, y así es como una cuenta muere dentro del ruido normal con la dirección bien acertada desde el principio.»
  - S052 [32w] «Y como un cierre forzoso es una orden real contra el libro, cada liquidación alimenta la siguiente en una cascada, peor en libros finos de alts y en fines de semana tranquilos.»
- **9 Course-coined term** (5)
  - S024 [repisa [seed]] «Intuición con números, sobre la misma repisa que dibuja la figura de más abajo: compras el rebote y entras en long a 9.500 con 10× de apalancamiento y `mmr = 0,5%`.»
  - S028 [non-seed "distancia de supervivencia" for distance to liquidation price] «La misma operación, con una distancia de supervivencia radicalmente distinta: eso es lo que el apalancamiento cambia de verdad.»
  - S036 [seed flujo forzoso: "el pico es flujo forzoso agotando un libro poco profundo" = liquidation market orders] «por esto las "mechas de liquidación" se pasan de frenada tan violentamente y luego vuelven de golpe: el pico es flujo forzoso agotando un libro poco profundo, no información nueva sobre el valor.»
  - S043 [seed flujo forzoso: "absorben el flujo forzoso razonablemente bien"] «Los pares principales como BTC absorben el flujo forzoso razonablemente bien; las altcoins pequeñas tienen libros poco profundos donde una ola modesta de liquidaciones puede abrir un hueco de varios puntos porcentuales en segundos.»
  - S046 [seed flujo forzoso (variant): "el mismo flujo de liquidaciones forzosas"] «El mismo flujo de liquidaciones forzosas que un libro entre semana absorbería empuja el precio mucho más lejos, produciendo las famosas "mechas" de fin de semana que clavan hacia abajo (o hacia arriba), barren un cúmulo de precios de liquidación y se recuperan minutos después.»
- **10 Metaphor then gloss** (2)
  - S021 ["Tu margen *es* el colchón." then S022 explains the cushion in numbers] «Tu margen *es* el colchón.»
  - S036 ["se pasan de frenada tan violentamente…: el pico es flujo forzoso agotando un libro poco profundo" — metaphor glossed after colon] «por esto las "mechas de liquidación" se pasan de frenada tan violentamente y luego vuelven de golpe: el pico es flujo forzoso agotando un libro poco profundo, no información nueva sobre el valor.»
- **11 Synonym rotation** (2)
  - S021 [distance to liquidation: colchón (S021, S025), distancia de supervivencia (S028), aire para respirar (S029)] 
  - S034 [liquidation chain: cascada (S034), ola (S034, S043), fichas de dominó (S037)] 
- **A absolutes** (2)
  - S007 [debes] «El exchange además te exige mantener un pequeño margen de mantenimiento: un mínimo de equity que debes conservar para mantener la posición abierta.»
  - S039 [nunca] «Las acciones pausan por la noche y se detienen ante movimientos extremos; los perpetuos no cierran nunca y rara vez se detienen.»

**EN** — 23 hits, 52 sentences, density 44.2

- **1 Filler** (3)
  - S028 [actually: "the thing leverage actually changes"] «Same trade, wildly different survival distance — that is the thing leverage actually changes.»
  - S030 [actually: "has to actually close the position in the market"] «A liquidation is not a paper event — the exchange has to actually close the position in the market.»
  - S044 [genuinely: "genuinely reckless", intensifier] «The same leverage that is merely risky on BTC is genuinely reckless on a thin alt.»
- **2 Rhythmic triad** (1)
  - S029 ["your entry, your direction, or the market" — drop "or the market"] «Leverage does not change your entry, your direction, or the market; it changes only *how much room price has to breathe before it kills you*.»
- **4 Summary/uplift closer** (4)
  - S004 [motivate: "If you can't, leverage controls you."] «If you can't, leverage controls you.»
  - S009 [restate: repeats S008] «Liquidation is the exchange protecting itself first; the maintenance-margin buffer is the sliver it keeps so the forced close lands *before* your equity hits zero, not after.»
  - S023 [restate: "The formula is nothing more than…" re-says S022] «The formula is nothing more than "how far can price move before my posted margin, minus the exchange's buffer, is used up".»
  - S029 [editorial: "it changes only how much room price has to breathe before it kills you" re-says S027-S028] «Leverage does not change your entry, your direction, or the market; it changes only *how much room price has to breathe before it kills you*.»
- **5 Sentence over 30 words** (7)
  - S008 [44w] «Once your equity would fall to that floor, the exchange closes the position to avoid your balance going negative — because on a leveraged position your losses can exceed what you put in, and the exchange, not you, is on the hook for the shortfall.»
  - S019 [39w] «The same trade in cross margin, backed by a 2,000 USDT balance, can keep bleeding until it has drawn down a large chunk of that 2,000 — the loss is no longer bounded by what you assigned to the trade.»
  - S020 [34w **aside-only** (25w without asides)] «For a linear (USDT-margined) perpetual, ignoring fees, the isolated liquidation price is driven by two rates: the initial margin rate (= 1 / leverage) and the maintenance margin rate `mmr` (a small exchange-set fraction, e.g. 0.5%).»
  - S022 [39w] «At 10× you post `1/10 = 10%` of the notional, so a 10% adverse move wipes out that 10% — except the exchange grabs the last 0.5% (the `mmr`) before it's fully gone, so the position dies about 9.5% away, not 10%.»
  - S033 [32w] «In a thin or one-sided book, that forced sell pushes price *down*, which drags price into the next cluster of long liquidation prices, which fire *more* forced sells, which push price further.»
  - S046 [35w] «The same forced-liquidation flow that a weekday book would absorb instead shoves price far further, producing the notorious weekend "wicks" that stab down (or up), sweep a cluster of liquidation prices, and recover minutes later.»
  - S050 [36w] «Liquidation is the exchange force-closing a position because equity fell to the maintenance margin, and on a linear perpetual its price is arithmetic you can do before entering: `entry × (1 − 1/leverage + mmr)` for a long, mirrored for a short.»
- **9 Course-coined term** (5)
  - S024 [shelf [seed]] «Worked intuition, on the same shelf the figure below draws: you buy the bounce and enter a long at 9,500 with 10× leverage and `mmr = 0.5%`.»
  - S028 [non-seed "survival distance" for distance to liquidation price] «Same trade, wildly different survival distance — that is the thing leverage actually changes.»
  - S036 [forced flow [seed]] «this is why "liquidation wicks" overshoot so violently and then snap back — the spike is forced flow exhausting a thin book, not new information about value.»
  - S043 [forced flow [seed]] «Major pairs like BTC absorb forced flow reasonably well; small altcoins have shallow books where a modest wave of liquidations can gap the price several percent in seconds.»
  - S046 [seed forced flow (variant): "the same forced-liquidation flow"] «The same forced-liquidation flow that a weekday book would absorb instead shoves price far further, producing the notorious weekend "wicks" that stab down (or up), sweep a cluster of liquidation prices, and recover minutes later.»
- **10 Metaphor then gloss** (1)
  - S021 ["Your margin *is* the cushion." then S022 explains it in numbers] «Your margin *is* the cushion.»
- **11 Synonym rotation** (2)
  - S021 [distance to liquidation: cushion (S021, S025), buffer (S009, S023), survival distance (S028), room to breathe (S029)] 
  - S034 [liquidation chain: cascade (S034), wave (S034, S043), dominoes (S037)] 
- **A absolutes** (2)
  - S007 [must] «The exchange also requires you to keep a small maintenance margin: a minimum equity you must retain to keep the position open.»
  - S039 [never] «Stocks pause overnight and halt on extreme moves; perpetuals never close and rarely halt.»

### m07-l1

**ES** — 24 hits, 59 sentences, density 40.7

- **1 Filler** (4)
  - S003 [de verdad: "el número que de verdad te quedas"] «Esta lección trata del hueco entre ambas —y de cómo calcular el número que de verdad te quedas—.»
  - S010 [other filler: emphatic "es justo lo que el exchange vigila"] «Y la asimetría juega en tu contra: la *pérdida* no realizada es justo lo que el exchange vigila para decidir si tu margen todavía cubre la posición.»
  - S037 [other filler: announcer sentence "Pongámosle números reales."] «Pongámosle números reales.»
  - S049 [other filler: announcer sentence "Ahora dale la vuelta."] «Ahora dale la vuelta.»
- **4 Summary/uplift closer** (6)
  - S003 [ahead: intro paragraph ends "Esta lección trata del hueco entre ambas…" (scope announcement)] «Esta lección trata del hueco entre ambas —y de cómo calcular el número que de verdad te quedas—.»
  - S008 [restate: "la operación ha terminado" re-says S007] «El número deja de moverse porque ya no queda nada que marcar: la operación ha terminado.»
  - S012 [restate: "Lo no realizado es provisional a tu favor pero decisivo en tu contra." sums up S009-S011] «Lo no realizado es provisional a tu favor pero decisivo en tu contra.»
  - S018 [editorial: "La diferencia de comisión es el exchange pagando por su propia liquidez." re-says S016-S017] «La diferencia de comisión es el exchange pagando por su propia liquidez.»
  - S048 [restate: "Tres porcentajes distintos para una sola operación…" sums up S046-S047] «Tres porcentajes distintos para una sola operación —bruto-sobre-nocional, neto-sobre-nocional y neto-sobre-margen— y solo el último es el cambio en tu cuenta.»
  - S051 [editorial: "Un número bruto verde, un saldo rojo."] «Un número bruto verde, un saldo rojo.»
- **5 Sentence over 30 words** (11)
  - S004 [36w] «El PnL no realizado es la ganancia o pérdida de una posición que sigue abierta; el PnL realizado es lo que fijas en el momento en que la cierras, o la parte de ella que cierres.»
  - S006 [32w] «El exchange lo recalcula tick a tick contra el precio de marca para saber en todo momento cuánto vale tu posición, pero nada se ha materializado y no se ha movido dinero.»
  - S007 [31w] «El PnL realizado es lo contrario: en el instante en que cierras, la estimación deja de ser una estimación y se convierte en un cambio final y contabilizado en tu saldo.»
  - S017 [33w **aside-only** (21w without asides)] «Por eso el exchange premia al que *aporta* profundidad —el maker— con la tarifa más baja (a veces cero, en ocasiones un pequeño rebate), y cobra más al que la *consume* —el taker—.»
  - S021 [31w **aside-only** (26w without asides)] «Primero, la comisión se cobra sobre el nocional (tamaño de la posición × precio), no sobre tu margen, así que el apalancamiento multiplica su mordisco en relación con el capital que pusiste.»
  - S023 [43w] «En una posición de 20.000 USDT a la tarifa taker del 0,055 %, son 11 USDT al abrir y unos 11 USDT al cerrar —alrededor de 22 USDT, o el 0,11 % del nocional— que se van antes de que el precio haya justificado nada.»
  - S028 [47w] «El funding es la correa: cuando el perpetuo cotiza por encima del spot la tasa se vuelve positiva y los longs pagan a los shorts, lo que desincentiva a los longs y empuja el perpetuo hacia abajo; cuando cotiza por debajo del spot, el pago se invierte.»
  - S050 [32w **aside-only** (29w without asides)] «Si esos mismos tres días de aguante hubieran producido solo un movimiento de +0,15 % (+30 USDT brutos), los ~22 de comisiones y los 18 de funding convertirían una operación "ganadora" en `30 − 22 − 18 = −10 USDT`.»
  - S054 [33w] «Antes de entrar, conoce tu comisión taker y recuerda que la pagas en la entrada *y* en la salida, sobre el nocional, así que presupuesta la ida y vuelta, no un solo tramo.»
  - S055 [31w] «Para cualquier cosa mantenida más de unas horas, mete también el funding en el resultado esperado, recordando que se sigue devengando de noche y los fines de semana mientras no miras.»
  - S058 [41w] «Lo que los separa son dos comisiones y el funding: la tarifa taker se cobra sobre el nocional al abrir y otra vez al cerrar, y el funding se devenga cada ocho horas, de madrugada y en fin de semana incluidos.»
- **9 Course-coined term** (1)
  - S028 [non-seed "la correa" (leash) for funding's anchoring role; same family as m04 "amarre"] «El funding es la correa: cuando el perpetuo cotiza por encima del spot la tasa se vuelve positiva y los longs pagan a los shorts, lo que desincentiva a los longs y empuja el perpetuo hacia abajo; cuando cotiza por debajo del spot, el pago se invierte.»
- **10 Metaphor then gloss** (1)
  - S028 ["El funding es la correa: cuando el perpetuo cotiza por encima del spot…" — metaphor glossed after colon] «El funding es la correa: cuando el perpetuo cotiza por encima del spot la tasa se vuelve positiva y los longs pagan a los shorts, lo que desincentiva a los longs y empuja el perpetuo hacia abajo; cuando cotiza por debajo del spot, el pago se invierte.»
- **11 Synonym rotation** (1)
  - S005 [displayed unrealised figure: estimación a precio de mercado (S005), foto (S009), número verde grande (S052), pico verde (S056)] 
- **A absolutes** (3)
  - S002 [nunca] «Cambia de significado según si la posición está abierta o cerrada, y la cifra que el exchange te pinta en verde casi nunca es la que aterriza en tu saldo.»
  - S027 [nunca] «Un perpetuo no vence nunca, así que no hay fecha de liquidación que arrastre su precio de vuelta a la línea del spot.»
  - S056 [nunca] «Y luego juzga la operación por su PnL neto realizado —`bruto − comisiones − funding`—, nunca por el pico verde que te mostró mientras estaba abierta.»

**EN** — 18 hits, 59 sentences, density 30.5

- **1 Filler** (4)
  - S003 [actually: "the number you actually keep"] «This lesson is about the gap between the two — and how to compute the number you actually keep.»
  - S010 [exactly: "is exactly what the exchange watches"] «And the asymmetry cuts against you: unrealized *loss* is exactly what the exchange watches to decide whether your margin still covers the position.»
  - S037 [other filler: announcer sentence "Put real numbers on it."] «Put real numbers on it.»
  - S049 [other filler: announcer sentence "Now flip it."] «Now flip it.»
- **4 Summary/uplift closer** (6)
  - S003 [ahead: intro paragraph ends "This lesson is about the gap…" (scope announcement)] «This lesson is about the gap between the two — and how to compute the number you actually keep.»
  - S008 [restate: "the trade is over" re-says S007] «The number stops moving because there is nothing left to mark — the trade is over.»
  - S012 [restate: "Unrealized is provisional in your favour but decisive against you." sums up S009-S011] «Unrealized is provisional in your favour but decisive against you.»
  - S018 [editorial: "The fee gap is the exchange paying for its own liquidity." re-says S016-S017] «The fee gap is the exchange paying for its own liquidity.»
  - S048 [restate: "Three different percentages for one trade…" sums up S046-S047] «Three different percentages for one trade — gross-on-notional, net-on-notional, and net-on-margin — and only the last is the change in your account.»
  - S051 [editorial: "A green gross number, a red balance."] «A green gross number, a red balance.»
- **5 Sentence over 30 words** (5)
  - S004 [33w] «Unrealized PnL is the profit or loss on a position that is still open; realized PnL is what you lock in the moment you close it, or the part of it you close.»
  - S017 [32w **aside-only** (22w without asides)] «So the exchange rewards the trader who *supplies* that depth — the maker — with the lower rate (sometimes zero, occasionally a small rebate), and charges the trader who *consumes* it — the taker — more.»
  - S023 [36w] «On a 20,000 USDT position at the 0.055% taker rate, that is 11 USDT to open and about 11 USDT to close — roughly 22 USDT, or 0.11% of notional, gone before the price has justified anything.»
  - S028 [35w] «Funding is the tether: when the perp trades above spot the rate turns positive and longs pay shorts, which discourages longs and pulls the perp back down; when it trades below spot the payment flips.»
  - S058 [34w] «What separates them is two fees and funding — the taker rate is charged on notional at the open and again at the close, and funding accrues every eight hours, overnight and at weekends included.»
- **9 Course-coined term** (1)
  - S028 [non-seed "the tether" for funding's anchoring role (also m04)] «Funding is the tether: when the perp trades above spot the rate turns positive and longs pay shorts, which discourages longs and pulls the perp back down; when it trades below spot the payment flips.»
- **10 Metaphor then gloss** (1)
  - S028 ["Funding is the tether: when the perp trades above spot…" — metaphor glossed after colon] «Funding is the tether: when the perp trades above spot the rate turns positive and longs pay shorts, which discourages longs and pulls the perp back down; when it trades below spot the payment flips.»
- **11 Synonym rotation** (1)
  - S005 [displayed unrealised figure: mark-to-market estimate (S005), snapshot (S009), big green number (S052), peak green number (S056)] 
- **A absolutes** (4)
  - S002 [never] «It changes meaning depending on whether the position is open or closed, and the figure the exchange flashes in green is almost never the figure that lands in your balance.»
  - S006 [always] «The exchange recomputes it tick by tick against the mark price so it always knows what your position is worth, but nothing has settled and no money has moved.»
  - S027 [never] «A perpetual never expires, so there is no settlement date to drag its price back in line with spot.»
  - S056 [never] «Then judge the trade by its net realized PnL — `gross − fees − funding` — and never by the peak green number it showed you while it was open.»

### m08-l1

**ES** — 81 hits, 103 sentences, density 78.6

- **1 Filler** (13)
  - S002 [honesta: "la lectura de gráfico más honesta" (honest applied to a reading)] «Deja un registro visible de dónde pelearon compradores y vendedores, y ese registro —la estructura— es la lectura de gráfico más honesta que puedes hacer, porque es el precio en sí, no un indicador derivado de él.»
  - S021 [de verdad: "los swings que de verdad giraron"] «Traza la zona a partir de los cuerpos y mechas de los swings que de verdad giraron, y espera que el precio reaccione *en algún punto dentro de ella*, no en un número exacto.»
  - S029 [other filler: announcer sentence "Ambos tienen un mecanismo, y conviene entenderlo en vez de memorizarlo."] «Ambos tienen un mecanismo, y conviene entenderlo en vez de memorizarlo.»
  - S033 [exactamente: "es exactamente donde se apilan"] «Un fakeout ocurre porque el nivel obvio es exactamente donde se apilan las órdenes en reposo justo más allá de él: los stops de los traders posicionados contra el nivel, y las órdenes de compra de los traders de ruptura que dejan instrucciones de "compra si rompe".»
  - S037 [literalmente: "son literalmente el mismo gráfico"] «En concreto, con los números de la figura de abajo: la resistencia está en torno a 2.130, y los dos paneles son literalmente el mismo gráfico —el mismo rango, las mismas velas— hasta el momento de la decisión.»
  - S071 [honesta: "la explicación honesta de cuánto más débil…"] «La misma estructura también puede describirse con líneas *inclinadas* —líneas de tendencia y canales— y m15-l1 lo retoma, incluida la explicación honesta de cuánto más débil es la afirmación de la versión inclinada.»
  - S078 [precisamente: "el asomo es precisamente de lo que está hecho un fakeout"] «Pero el asomo es precisamente de lo que está hecho un fakeout: has comprado el estallido de stops disparados y órdenes de ruptura al peor precio posible, instantes antes de que se gire de vuelta dentro.»
  - S084 [de verdad: "¿ha cambiado de verdad el control?"] «Trata el CHoCH como una pregunta —*¿ha cambiado de verdad el control?*— y espera la respuesta: un máximo más bajo tras el mínimo más bajo, un intento fallido de recuperar el nivel, una segunda ruptura que confirme.»
  - S087 [other filler: emphatic "se concentran justo en estas ventanas"] «Menos órdenes en reposo significa que hace falta mucho menos tamaño para empujar el precio más allá de un nivel obvio, así que las falsas rupturas se concentran justo en estas ventanas.»
  - S088 [simplemente: "puede que el nivel simplemente se haya atravesado"] «Una "ruptura" impresa a las 4 de la madrugada de un domingo merece más recelo que la misma ruptura en una sesión concurrida de un día laborable; puede que el nivel simplemente se haya atravesado empujando aire vacío y vuelva de golpe cuando regrese el volumen real.»
  - S092 [honesta: "la única lectura honesta"] «Por eso la mecha que asoma por tu nivel suele ser más larga y más traicionera en cripto que la versión de manual, y por eso el cierre, nunca el extremo, es la única lectura honesta de si un nivel rompió de verdad.»
  - S092 [de verdad: "si un nivel rompió de verdad"] «Por eso la mecha que asoma por tu nivel suele ser más larga y más traicionera en cripto que la versión de manual, y por eso el cierre, nunca el extremo, es la única lectura honesta de si un nivel rompió de verdad.»
  - S100 [honesto: "el aviso honesto más temprano"] «El cambio de carácter es el aviso honesto más temprano; ni uno antes.»
- **2 Rhythmic triad** (3)
  - S009 [same frame x3: "Los traders que compraron…" / "Los que se perdieron…" / "Los que compraron demasiado arriba…" (S009-S011) — each a distinct group; if trimmed, drop the second] «Los traders que compraron el último rebote y lo vieron funcionar dejan órdenes de compra para volver a hacerlo.»
  - S042 ["rumor / titular sin confirmar / noticia" — drop "titular sin confirmar"] «Una mecha que atraviesa un nivel es un rumor; unas pocas velas cerrando al otro lado son un titular sin confirmar —el panel de la derecha las tiene y aun así fracasa—; un cuerpo que cierra más allá y *se queda* es la noticia.»
  - S077 ["la ruptura parece obvia, la vela es verde y rápida, y el miedo… ahoga el plan" — drop "la vela es verde y rápida"] «La ruptura parece obvia, la vela es verde y rápida, y el miedo a perdérsela ahoga el plan, así que compras el asomo.»
- **3 Rhetorical question** (3)
  - S007 «¿Por qué la compra reaparece de forma fiable en el mismo sitio?»
  - S047 «¿Para qué molestarse en nombrar la escalera?»
  - S063 «¿Por qué pesa tanto esa primera ruptura?»
- **4 Summary/uplift closer** (11)
  - S003 [ahead: intro ends "Todo lo de esta lección es una forma de leer ese registro…" (scope announcement)] «Todo lo de esta lección es una forma de leer ese registro: dónde se frenó el precio, dónde rompió y si las rupturas significaron algo.»
  - S006 [editorial: "La palabra que hay que retener es *zona*."] «La palabra que hay que retener es *zona*.»
  - S032 [editorial: "El retest es el mercado votando por segunda vez."] «El retest es el mercado votando por segunda vez.»
  - S036 [restate: "La falsa ruptura no falló por accidente…" re-says S033-S035] «La falsa ruptura no falló por accidente: se quedó sin las mismas órdenes que la provocaron.»
  - S040 [restate: "Mismo nivel, mismas primeras velas…" re-says S037-S039] «Mismo nivel, mismas primeras velas: solo el cierre *que aguanta* y lo que viene después los distinguen.»
  - S051 [editorial: "En cuanto la escalera se detiene, se detiene también la suposición."] «En cuanto la escalera se detiene, se detiene también la suposición.»
  - S053 [editorial: "…una escalera que podrías describirle a alguien por teléfono."] «Cada mínimo por encima del mínimo anterior, cada máximo por encima del máximo anterior: una escalera que podrías describirle a alguien por teléfono.»
  - S069 [ahead: "Ese vocabulario… se mapea sobre esta misma mecánica en m34-l1." after the content ended] «Ese vocabulario —y el resto del dialecto que lo acompaña— se mapea sobre esta misma mecánica en m34-l1.»
  - S080 [restate: "La primera vela pasada un nivel es la vela más cara de operar."] «La primera vela pasada un nivel es la vela más cara de operar.»
  - S092 [restate: "Por eso… el cierre, nunca el extremo, es la única lectura honesta…" re-says the lesson's close rule] «Por eso la mecha que asoma por tu nivel suele ser más larga y más traicionera en cripto que la versión de manual, y por eso el cierre, nunca el extremo, es la única lectura honesta de si un nivel rompió de verdad.»
  - S100 [editorial: lesson's last prose unit ends "El cambio de carácter es el aviso honesto más temprano; ni uno antes."] «El cambio de carácter es el aviso honesto más temprano; ni uno antes.»
- **5 Sentence over 30 words** (27)
  - S002 [37w] «Deja un registro visible de dónde pelearon compradores y vendedores, y ese registro —la estructura— es la lectura de gráfico más honesta que puedes hacer, porque es el precio en sí, no un indicador derivado de él.»
  - S018 [50w **aside-only** (15w without asides)] «Caso concreto: supón que BTC ha girado al alza tres veces en el mismo vecindario —una vez pinchó con la mecha hasta 58.050 y cerró de vuelta en 58.600, otra vez hizo base en torno a 58.300 durante varias velas, otra cayó a 58.150 en el intradía y se recuperó—.»
  - S021 [34w] «Traza la zona a partir de los cuerpos y mechas de los swings que de verdad giraron, y espera que el precio reaccione *en algún punto dentro de ella*, no en un número exacto.»
  - S024 [36w **aside-only** (26w without asides)] «Una ruptura genuina cierra con decisión más allá del nivel —un cuerpo de vela entero al otro lado— y luego aguanta ahí, idealmente volviendo a *retestear* el antiguo nivel como nuevo soporte (o resistencia) y rebotando.»
  - S030 [59w] «Una ruptura genuina suele retestear y aguantar por *inversión de roles*: los vendedores que defendían la antigua resistencia han sido arrollados y muchos cierran sus cortos en el retroceso hacia el nivel, convirtiendo a los antiguos vendedores en compradores; mientras tanto, los compradores que se negaron a perseguir el precio consiguen por fin su entrada en la antigua línea.»
  - S033 [47w] «Un fakeout ocurre porque el nivel obvio es exactamente donde se apilan las órdenes en reposo justo más allá de él: los stops de los traders posicionados contra el nivel, y las órdenes de compra de los traders de ruptura que dejan instrucciones de "compra si rompe".»
  - S037 [38w] «En concreto, con los números de la figura de abajo: la resistencia está en torno a 2.130, y los dos paneles son literalmente el mismo gráfico —el mismo rango, las mismas velas— hasta el momento de la decisión.»
  - S039 [37w **aside-only** (22w without asides)] «A la derecha, un fakeout: el mismo asomo llega a 2.166, aguanta media docena de velas por encima y luego las pierde —cierra de vuelta bajo 2.130, pierde 2.035 en pocas velas y sigue cayendo desde ahí—.»
  - S042 [44w] «Una mecha que atraviesa un nivel es un rumor; unas pocas velas cerrando al otro lado son un titular sin confirmar —el panel de la derecha las tiene y aun así fracasa—; un cuerpo que cierra más allá y *se queda* es la noticia.»
  - S044 [31w **aside-only** (29w without asides)] «Una tendencia alcista es una escalera de máximos más altos (HH) y mínimos más altos (HL): cada subida supera el pico anterior y cada retroceso hace suelo por encima del anterior.»
  - S052 [36w **aside-only** (25w without asides)] «Una tendencia alcista limpia podría leerse así: mínimo en 100, máximo en 110, retroceso a 104 (un mínimo más alto), máximo en 118 (un máximo más alto), retroceso a 109 (mínimo más alto), máximo en 126.»
  - S055 [35w] «Existe porque no todos actúan a la vez: algunos compradores toman ganancias durante la subida, algunos vendedores tardíos prueban suerte, y el precio devuelve parte del último tramo antes de que la tendencia se reanude.»
  - S066 [38w] «En la escalera de arriba, el precio cayendo desde 126, pasando por 109, hasta un mínimo de 106 es un cambio de carácter: el primer mínimo más bajo en una serie que solo había hecho mínimos más altos.»
  - S067 [50w] «Al gemelo de ese giro también le han puesto nombre, aunque este curso no lo necesite para explicar la escalera: cada máximo más alto que se lleva por delante el máximo anterior es una ruptura de estructura (BOS), la ruptura que *confirma* el patrón, frente al CHoCH, que lo rompe.»
  - S071 [33w **aside-only** (28w without asides)] «La misma estructura también puede describirse con líneas *inclinadas* —líneas de tendencia y canales— y m15-l1 lo retoma, incluida la explicación honesta de cuánto más débil es la afirmación de la versión inclinada.»
  - S073 [44w **aside-only** (21w without asides)] «Cada panel es una instancia generada con sus propios precios —los números de la escalera de arriba son proporciones para que la secuencia se pueda seguir de memoria, no una cotización que buscar—; lo que hay que leer es la forma y las etiquetas.»
  - S074 [31w] «El cambio de carácter no es una promesa de que la tendencia se haya girado; es el primer *indicio* de que la regla de la vieja tendencia ha dejado de funcionar.»
  - S078 [36w] «Pero el asomo es precisamente de lo que está hecho un fakeout: has comprado el estallido de stops disparados y órdenes de ruptura al peor precio posible, instantes antes de que se gire de vuelta dentro.»
  - S084 [37w] «Trata el CHoCH como una pregunta —*¿ha cambiado de verdad el control?*— y espera la respuesta: un máximo más bajo tras el mínimo más bajo, un intento fallido de recuperar el nivel, una segunda ruptura que confirme.»
  - S086 [32w **aside-only** (14w without asides)] «Sin campana de cierre, las horas muertas —los fines de semana y el tramo en que todas las zonas horarias importantes duermen a la vez— funcionan con un libro de órdenes fino.»
  - S087 [32w] «Menos órdenes en reposo significa que hace falta mucho menos tamaño para empujar el precio más allá de un nivel obvio, así que las falsas rupturas se concentran justo en estas ventanas.»
  - S088 [47w] «Una "ruptura" impresa a las 4 de la madrugada de un domingo merece más recelo que la misma ruptura en una sesión concurrida de un día laborable; puede que el nivel simplemente se haya atravesado empujando aire vacío y vuelva de golpe cuando regrese el volumen real.»
  - S089 [40w] «El apalancamiento concentra los stops y los precios de liquidación justo más allá de los máximos y mínimos de swing obvios: todos miran los mismos niveles, así que las órdenes de protección de todos acaban en la misma banda estrecha.»
  - S090 [55w] «En un libro poco profundo, un participante grande puede empujar el precio hasta esa banda, disparar los stops apilados y forzar la liquidación de los traders sobreapalancados, absorber la avalancha de órdenes resultante y dejar que el precio vuelva de golpe, dejando una mecha larga que perforó el nivel y cerró muy lejos de él.»
  - S092 [43w] «Por eso la mecha que asoma por tu nivel suele ser más larga y más traicionera en cripto que la versión de manual, y por eso el cierre, nunca el extremo, es la única lectura honesta de si un nivel rompió de verdad.»
  - S102 [40w] «Una ruptura solo es genuina cuando un cuerpo cierra más allá del nivel y aguanta —a menudo retesteándolo por inversión de roles—, mientras que un fakeout asoma por las órdenes apiladas justo pasado el nivel y cierra de vuelta dentro.»
  - S103 [40w] «La secuencia de swings dice quién va ganando sin preguntarle a ningún indicador: HH/HL arriba, LH/LL abajo, y el primer swing que la viola es un cambio de carácter, que es una pregunta sobre el control y no una respuesta.»
- **9 Course-coined term** (19)
  - S012 [seed repisa/shelf (ES "estante"): S/R as a shelf of resting orders] «Un soporte no es magia en el número: es un estante de órdenes de compra en reposo que las últimas visitas enseñaron a la gente a dejar.»
  - S013 [seed shelf ("estante"): resistance as the same shelf] «La resistencia es el mismo estante, hecho de órdenes de venta.»
  - S020 [seed shelf ("estante"): "Hay un estante de unos 58.000–58.400 de ancho."] «Hay un estante de unos 58.000–58.400 de ancho.»
  - S035 [combustible [seed]] «Cuando ese combustible se agota, el precio cae de vuelta dentro, y quienes compraron el asomo quedan ahora atrapados por encima del nivel y motivados para vender.»
  - S039 [non-seed "asomo": "el mismo asomo llega a 2.166"] «A la derecha, un fakeout: el mismo asomo llega a 2.166, aguanta media docena de velas por encima y luego las pierde —cierra de vuelta bajo 2.130, pierde 2.035 en pocas velas y sigue cayendo desde ahí—.»
  - S044 [escalera [seed]] «Una tendencia alcista es una escalera de máximos más altos (HH) y mínimos más altos (HL): cada subida supera el pico anterior y cada retroceso hace suelo por encima del anterior.»
  - S047 [escalera [seed]] «¿Para qué molestarse en nombrar la escalera?»
  - S051 [escalera [seed]] «En cuanto la escalera se detiene, se detiene también la suposición.»
  - S053 [escalera [seed]] «Cada mínimo por encima del mínimo anterior, cada máximo por encima del máximo anterior: una escalera que podrías describirle a alguien por teléfono.»
  - S059 [escalera [seed]] «Una tendencia sigue intacta mientras la escalera continúa.»
  - S066 [escalera [seed]] «En la escalera de arriba, el precio cayendo desde 126, pasando por 109, hasta un mínimo de 106 es un cambio de carácter: el primer mínimo más bajo en una serie que solo había hecho mínimos más altos.»
  - S067 [escalera [seed]] «Al gemelo de ese giro también le han puesto nombre, aunque este curso no lo necesite para explicar la escalera: cada máximo más alto que se lleva por delante el máximo anterior es una ruptura de estructura (BOS), la ruptura que *confirma* el patrón, frente al CHoCH, que lo rompe.»
  - S068 [escalera [seed]] «Una escalera, dos clases de ruptura.»
  - S072 [escalera [seed]] «La figura pone esa comparación lado a lado, con cada swing etiquetado: a la izquierda una escalera que sigue subiendo, a la derecha la misma escalera cuyo último swing falla.»
  - S072 [escalera [seed]] «La figura pone esa comparación lado a lado, con cada swing etiquetado: a la izquierda una escalera que sigue subiendo, a la derecha la misma escalera cuyo último swing falla.»
  - S073 [escalera [seed]] «Cada panel es una instancia generada con sus propios precios —los números de la escalera de arriba son proporciones para que la secuencia se pueda seguir de memoria, no una cotización que buscar—; lo que hay que leer es la forma y las etiquetas.»
  - S077 [non-seed "asomo": "así que compras el asomo"] «La ruptura parece obvia, la vela es verde y rápida, y el miedo a perdérsela ahoga el plan, así que compras el asomo.»
  - S078 [non-seed "asomo": "el asomo es precisamente de lo que está hecho un fakeout"] «Pero el asomo es precisamente de lo que está hecho un fakeout: has comprado el estallido de stops disparados y órdenes de ruptura al peor precio posible, instantes antes de que se gire de vuelta dentro.»
  - S101 [seed shelf ("estantes"): summary] «Los soportes y las resistencias son estantes de órdenes en reposo que deja la memoria, y por eso son zonas de unas cuantas velas de ancho y no líneas.»
- **10 Metaphor then gloss** (2)
  - S012 ["es un estante de órdenes de compra en reposo que las últimas visitas enseñaron a la gente a dejar" — metaphor glossed in the same sentence] «Un soporte no es magia en el número: es un estante de órdenes de compra en reposo que las últimas visitas enseñaron a la gente a dejar.»
  - S044 ["una escalera de máximos más altos (HH) y mínimos más altos (HL): cada subida supera…" — metaphor glossed after colon] «Una tendencia alcista es una escalera de máximos más altos (HH) y mínimos más altos (HL): cada subida supera el pico anterior y cada retroceso hace suelo por encima del anterior.»
- **11 Synonym rotation** (3)
  - S004 [S/R area: zona (S004), estante (S012), banda (S014), nivel (S016), vecindario (S018)] 
  - S026 [fakeout: fakeout (S026, S033), falsa ruptura (S036, S087), trampas (S079)] 
  - S058 [CHoCH: primera grieta (S058), cambio de carácter (S060), primer indicio (S074), patrón roto (S082), aviso honesto (S100)] 
- **A absolutes** (2)
  - S085 [nunca, siempre] «Los mercados tradicionales cierran; el cripto nunca lo hace, y ese libro de órdenes siempre activo cambia cómo se comporta la estructura.»
  - S092 [nunca] «Por eso la mecha que asoma por tu nivel suele ser más larga y más traicionera en cripto que la versión de manual, y por eso el cierre, nunca el extremo, es la única lectura honesta de si un nivel rompió de verdad.»

**EN** — 77 hits, 103 sentences, density 74.8

- **1 Filler** (13)
  - S002 [honest: "the most honest chart-reading you can do"] «It leaves a visible record of where buyers and sellers fought, and that record — the structure — is the most honest chart-reading you can do, because it is the price itself, not an indicator derived from it.»
  - S021 [actually: "the swings that actually turned"] «Draw the zone from the bodies and wicks of the swings that actually turned, and expect price to react *somewhere inside it*, not at one exact number.»
  - S029 [other filler: announcer sentence "Both have a mechanism, and it is worth understanding rather than memorising."] «Both have a mechanism, and it is worth understanding rather than memorising.»
  - S033 [exactly: "is exactly where resting orders pile up"] «A fakeout happens because the obvious level is exactly where resting orders pile up just beyond it: the stop-losses of traders positioned into the level, and the buy orders of breakout traders who leave "buy if it breaks" instructions.»
  - S037 [literally: "are literally the same chart"] «Concretely, using the numbers in the figure below: resistance sits around 2,130, and the two panels are literally the same chart — the same range, the same candles — right up to the decision.»
  - S071 [honest: "the honest account of how much weaker…"] «The same structure can also be described with *sloped* lines — trendlines and channels — and m15-l1 takes that up, including the honest account of how much weaker the sloped version's claim is.»
  - S078 [exactly: "the poke is exactly what a fakeout is made of"] «But the poke is exactly what a fakeout is made of: you have bought the burst of triggered stops and breakout orders at the worst possible price, moments before it reverses back inside.»
  - S084 [actually: "has control actually changed?"] «Treat the CHoCH as a question — *has control actually changed?* — and wait for the answer: a lower high after the lower low, a failed attempt to reclaim, a second confirming break.»
  - S087 [exactly: "cluster in exactly these windows"] «Fewer resting orders means far less size is needed to shove price through an obvious level, so false breaks cluster in exactly these windows.»
  - S088 [simply: "may simply have been pushed through"] «A "breakout" printed at 4 a.m. on a Sunday deserves more suspicion than the same break in a busy weekday session; the level may simply have been pushed through empty air and will snap back when real volume returns.»
  - S092 [honest: "the only honest reading"] «This is why the wick that pokes your level is often longer and nastier in crypto than the textbook version — and why the close, never the extreme, is the only honest reading of whether a level actually broke.»
  - S092 [actually: "whether a level actually broke"] «This is why the wick that pokes your level is often longer and nastier in crypto than the textbook version — and why the close, never the extreme, is the only honest reading of whether a level actually broke.»
  - S100 [honest: "the earliest honest warning"] «The change of character is the earliest honest warning — no earlier.»
- **2 Rhythmic triad** (3)
  - S009 [same frame x3: "Traders who bought…" / "Traders who missed…" / "Traders who bought too high…" (S009-S011) — each a distinct group; if trimmed, drop the second] «Traders who bought the last bounce and watched it work leave bids to buy it again.»
  - S042 ["rumour / unconfirmed headline / news" — drop "unconfirmed headline"] «A wick through a level is a rumour; a few candles closing on the other side are an unconfirmed headline — the right-hand panel has them and still fails; a body that closes beyond and *stays* is the news.»
  - S077 ["The break looks obvious, the candle is green and fast, and the fear… drowns out the plan" — drop "the candle is green and fast"] «The break looks obvious, the candle is green and fast, and the fear of missing it drowns out the plan — so you buy the poke.»
- **3 Rhetorical question** (3)
  - S007 «Why does buying reliably reappear at the same place?»
  - S047 «Why bother naming the staircase?»
  - S063 «Why does that first break carry so much weight?»
- **4 Summary/uplift closer** (11)
  - S003 [ahead: intro ends "Everything in this lesson is a way of reading that record…"] «Everything in this lesson is a way of reading that record: where price stalled, where it broke, and whether the breaks meant anything.»
  - S006 [editorial: "The word to hold onto is *area*."] «The word to hold onto is *area*.»
  - S032 [editorial: "The retest is the market voting a second time."] «The retest is the market voting a second time.»
  - S036 [restate: "The false break didn't fail by accident…" re-says S033-S035] «The false break didn't fail by accident; it ran out of the very orders that caused it.»
  - S040 [restate: "Same level, same first candles…" re-says S037-S039] «Same level, same first candles; only the close *that holds* and what follows tell them apart.»
  - S051 [editorial: "The moment the staircase stops, so does the assumption."] «The moment the staircase stops, so does the assumption.»
  - S053 [editorial: "…a staircase you could describe to someone over the phone."] «Each low above the previous low, each high above the previous high — a staircase you could describe to someone over the phone.»
  - S069 [ahead: "…is mapped onto this same mechanic in m34-l1." after the content ended] «That vocabulary, and the rest of the dialect it comes with, is mapped onto this same mechanic in m34-l1.»
  - S080 [restate: "The first candle past a level is the single most expensive candle to trade."] «The first candle past a level is the single most expensive candle to trade.»
  - S092 [restate: "This is why… the only honest reading…" re-says the close rule] «This is why the wick that pokes your level is often longer and nastier in crypto than the textbook version — and why the close, never the extreme, is the only honest reading of whether a level actually broke.»
  - S100 [editorial: lesson's last prose unit ends "The change of character is the earliest honest warning — no earlier."] «The change of character is the earliest honest warning — no earlier.»
- **5 Sentence over 30 words** (22)
  - S002 [36w] «It leaves a visible record of where buyers and sellers fought, and that record — the structure — is the most honest chart-reading you can do, because it is the price itself, not an indicator derived from it.»
  - S018 [40w] «Concrete case: say BTC has turned up three times in the same neighbourhood — once it wicked down to 58,050 and closed back at 58,600, once it based around 58,300 for several candles, once it dipped to 58,150 intraday and recovered.»
  - S024 [36w **aside-only** (26w without asides)] «A genuine breakout closes decisively beyond the level — a full candle body on the far side — and then holds there, ideally coming back to *retest* the old level as new support (or resistance) and bouncing away.»
  - S030 [53w] «A genuine breakout tends to retest and hold because of *role reversal*: the sellers who defended the old resistance have been overrun, and many cover their shorts on the pullback to the level, turning former sellers into buyers; meanwhile the buyers who refused to chase finally get their entry at the old line.»
  - S033 [39w] «A fakeout happens because the obvious level is exactly where resting orders pile up just beyond it: the stop-losses of traders positioned into the level, and the buy orders of breakout traders who leave "buy if it breaks" instructions.»
  - S037 [32w **aside-only** (26w without asides)] «Concretely, using the numbers in the figure below: resistance sits around 2,130, and the two panels are literally the same chart — the same range, the same candles — right up to the decision.»
  - S039 [38w] «On the right, a fakeout: the same poke reaches 2,166, holds half a dozen candles above the line, then loses them — it closes back under 2,130, gives up 2,035 within a few candles, and keeps sliding from there.»
  - S042 [38w] «A wick through a level is a rumour; a few candles closing on the other side are an unconfirmed headline — the right-hand panel has them and still fails; a body that closes beyond and *stays* is the news.»
  - S052 [31w **aside-only** (23w without asides)] «A clean uptrend might read: low at 100, high at 110, dip to 104 (a higher low), high at 118 (a higher high), dip to 109 (higher low), high at 126.»
  - S055 [33w] «It exists because not everyone acts at once: some buyers take profit into strength, some late sellers try their luck, and price gives back part of the last leg before the trend resumes.»
  - S066 [34w] «In the staircase above, price falling from 126 down through 109 to a low of 106 is a change of character — the first lower low in a run that had made only higher ones.»
  - S067 [46w] «That break's twin has a name too, though this course does not need it to explain the ladder: every higher high that takes out the previous high is a break of structure (BOS) — the break that *confirms* the pattern, as against the CHoCH, which breaks it.»
  - S071 [31w **aside-only** (28w without asides)] «The same structure can also be described with *sloped* lines — trendlines and channels — and m15-l1 takes that up, including the honest account of how much weaker the sloped version's claim is.»
  - S073 [47w **aside-only** (20w without asides)] «Each panel is a generated instance carrying its own prices — the numbers in the ladder above are proportions, chosen so the sequence is one you can hold in your head, not a quote to go looking for — so what to read is the shape and the labels.»
  - S078 [33w] «But the poke is exactly what a fakeout is made of: you have bought the burst of triggered stops and breakout orders at the worst possible price, moments before it reverses back inside.»
  - S084 [31w **aside-only** (27w without asides)] «Treat the CHoCH as a question — *has control actually changed?* — and wait for the answer: a lower high after the lower low, a failed attempt to reclaim, a second confirming break.»
  - S088 [39w] «A "breakout" printed at 4 a.m. on a Sunday deserves more suspicion than the same break in a busy weekday session; the level may simply have been pushed through empty air and will snap back when real volume returns.»
  - S089 [31w] «Leverage concentrates stop-loss orders and liquidation prices just beyond the obvious swing highs and lows — everyone watches the same levels, so everyone's protective orders end up in the same narrow band.»
  - S090 [49w] «In a thin book a large player can push price into that band, trip the clustered stops and force the liquidation of over-leveraged traders, absorb the resulting flood of orders, and let price snap back — leaving a long wick that pierced the level and closed far away from it.»
  - S092 [38w] «This is why the wick that pokes your level is often longer and nastier in crypto than the textbook version — and why the close, never the extreme, is the only honest reading of whether a level actually broke.»
  - S102 [36w **aside-only** (30w without asides)] «A breakout is genuine only once a body closes beyond the level and holds — often retesting it in role reversal — while a fakeout pokes through the orders piled just past the level and closes back inside.»
  - S103 [37w] «The swing sequence says who is winning without asking an indicator: HH/HL up, LH/LL down, and the first swing to violate it is a change of character, which is a question about control rather than an answer.»
- **9 Course-coined term** (19)
  - S012 [shelf [seed]] «A support is not magic in the number — it is a shelf of resting buy orders that the last few visits taught people to leave.»
  - S013 [shelf [seed]] «Resistance is the same shelf built from sell orders.»
  - S020 [shelf [seed]] «There is a shelf roughly 58,000–58,400 wide.»
  - S035 [fuel [seed]] «Once that fuel is spent, price falls back inside, and the ones who bought the poke are now trapped above the level and motivated to sell.»
  - S039 [non-seed "the poke": "the same poke reaches 2,166"] «On the right, a fakeout: the same poke reaches 2,166, holds half a dozen candles above the line, then loses them — it closes back under 2,130, gives up 2,035 within a few candles, and keeps sliding from there.»
  - S044 [staircase/ladder [seed]] «An uptrend is a staircase of higher highs (HH) and higher lows (HL): each rally exceeds the last peak, and each dip bottoms above the last dip.»
  - S047 [staircase/ladder [seed]] «Why bother naming the staircase?»
  - S051 [staircase/ladder [seed]] «The moment the staircase stops, so does the assumption.»
  - S053 [staircase/ladder [seed]] «Each low above the previous low, each high above the previous high — a staircase you could describe to someone over the phone.»
  - S059 [staircase/ladder [seed]] «A trend stays intact as long as the staircase continues.»
  - S066 [staircase/ladder [seed]] «In the staircase above, price falling from 126 down through 109 to a low of 106 is a change of character — the first lower low in a run that had made only higher ones.»
  - S067 [staircase/ladder [seed]] «That break's twin has a name too, though this course does not need it to explain the ladder: every higher high that takes out the previous high is a break of structure (BOS) — the break that *confirms* the pattern, as against the CHoCH, which breaks it.»
  - S068 [staircase/ladder [seed]] «One ladder, two kinds of break.»
  - S072 [staircase/ladder [seed]] «The figure puts that comparison side by side with every swing labelled: on the left a staircase that keeps climbing, on the right the same ladder whose final swing fails.»
  - S072 [staircase/ladder [seed]] «The figure puts that comparison side by side with every swing labelled: on the left a staircase that keeps climbing, on the right the same ladder whose final swing fails.»
  - S073 [staircase/ladder [seed]] «Each panel is a generated instance carrying its own prices — the numbers in the ladder above are proportions, chosen so the sequence is one you can hold in your head, not a quote to go looking for — so what to read is the shape and the labels.»
  - S077 [non-seed "the poke": "so you buy the poke"] «The break looks obvious, the candle is green and fast, and the fear of missing it drowns out the plan — so you buy the poke.»
  - S078 [non-seed "the poke": "the poke is exactly what a fakeout is made of"] «But the poke is exactly what a fakeout is made of: you have bought the burst of triggered stops and breakout orders at the worst possible price, moments before it reverses back inside.»
  - S101 [shelf [seed]] «Support and resistance are shelves of resting orders that memory leaves behind, which is why they are zones a few candles wide rather than lines.»
- **10 Metaphor then gloss** (2)
  - S012 ["a shelf of resting buy orders that the last few visits taught people to leave" — metaphor glossed in the same sentence] «A support is not magic in the number — it is a shelf of resting buy orders that the last few visits taught people to leave.»
  - S044 ["a staircase of higher highs (HH) and higher lows (HL): each rally exceeds…" — metaphor glossed after colon] «An uptrend is a staircase of higher highs (HH) and higher lows (HL): each rally exceeds the last peak, and each dip bottoms above the last dip.»
- **11 Synonym rotation** (4)
  - S004 [S/R area: area (S004), shelf (S012), zone (S014), band (S014), level (S016), neighbourhood (S018)] 
  - S026 [fakeout: fakeout (S026, S033), false break (S036, S087), traps (S079)] 
  - S043 [uptrend swing structure: sequence of swings (S043, S048), staircase (S044, S047, S051…), ladder (S067, S068, S072, S073)] 
  - S058 [CHoCH: first crack (S058), change of character (S060), first evidence (S074), broken pattern (S082), earliest honest warning (S100)] 
- **A absolutes** (3)
  - S038 [never] «On the left, a genuine break: price closes beyond the line, pushes on to 2,225, and never comes back.»
  - S085 [never, always] «Traditional markets close; crypto never does, and the always-on order book changes how structure behaves.»
  - S092 [never] «This is why the wick that pokes your level is often longer and nastier in crypto than the textbook version — and why the close, never the extreme, is the only honest reading of whether a level actually broke.»

### m08-l2

**ES** — 40 hits, 69 sentences, density 58.0

- **1 Filler** (8)
  - S016 ["sin más": tag after "arrollando al otro"] «Donde un rechazo es una batalla *ganada en un extremo*, un overrun es un lado arrollando al otro sin más.»
  - S033 ["exactamente": emphatic, "dice igual de poco" carries it] «Este mismo fenómeno existe a dos escalas mayores, y dice exactamente igual de poco en cada una: a lo largo de una serie de barras es la cuña y el triángulo de m15-l2, y a lo largo de un régimen de mercado entero es el ciclo de volatilidad de m16-l1.»
  - S034 [other filler: "Aquí está la regla que gobierna todo lo anterior:" announcer] «Aquí está la regla que gobierna todo lo anterior: **el significado de una vela viene, sobre todo, de dónde ocurre.**»
  - S038 ["exactamente": emphatic before a cross-reference] «Es exactamente la postura de m13, "el fib no crea el nivel": la vela tampoco crea la señal.»
  - S049 [other filler: "La conclusión es directa:" announcer] «La conclusión es directa: no hay 60 patrones, hay dos mecánicas con 60 nombres.»
  - S050 ["precisamente": emphatic before "porque"] «Y como con los niveles autocumplidos de m13, un nombre muy vigilado importa *un poco* más precisamente porque miles de traders lo leen igual y actúan sobre él, lo que también es su límite: la ventaja es ajustada, está masificada y nunca sustituye al nivel de debajo.»
  - S051 ["nada más": tag] «Siempre que este curso usa un nombre, es una abreviatura de "esta mecánica, en esta ubicación", nada más.»
  - S060 [other filler: "y punto" tag] «Un doji en un punto cualquiera es indecisión, y punto.»
- **2 Rhythmic triad** (2)
  - S050 ["ajustada, está masificada y nunca sustituye al nivel": ajustada/masificada overlap; drop "está masificada"] «Y como con los niveles autocumplidos de m13, un nombre muy vigilado importa *un poco* más precisamente porque miles de traders lo leen igual y actúan sobre él, lo que también es su límite: la ventaja es ajustada, está masificada y nunca sustituye al nivel de debajo.»
  - S053 [frame triad across paragraphs: "La versión simple… La versión aplicada… (S056) La versión ilusa… (S059)"; drop the frame, not the content] «La versión simple es ver un martillo o una envolvente de manual en *cualquier sitio* y tomarlo.»
- **4 Summary/uplift closer** (5)
  - S002 [ahead: announces what the lesson will do] «Esta lección por fin dice qué aspecto tiene una *reacción*.»
  - S021 [restate: re-tells the engulfing just described (also a "no solo…" construction)] «Los compradores no solo empujaron el precio; arrollaron todo lo que los vendedores del periodo anterior habían construido.»
  - S039 [restate: repeats S036–S038 (no level, no signal)] «Es una reacción *a* algo, y si no hay nada a lo que reaccionar, no hay señal.»
  - S051 [restate/editorial: repeats the "dos mecánicas con 60 nombres" point] «Siempre que este curso usa un nombre, es una abreviatura de "esta mecánica, en esta ubicación", nada más.»
  - S069 [restate: summary ends on the slogan "no hay sesenta patrones, hay dos mecánicas con sesenta nombres", already said in S067] «La ubicación es el 90 % de la señal, así que el mismo martillo es información en un nivel defendido y ruido en espacio abierto: no hay sesenta patrones, hay dos mecánicas con sesenta nombres.»
- **5 Sentence over 30 words** (11)
  - S001 [44w] «Una y otra vez este curso te dice que "esperes a que el precio reaccione en el nivel": en un soporte roto durante el retest (m08), en un retroceso de Fibonacci (m13, paso 4), en el spring que testea un rango de Wyckoff (m09).»
  - S003 [40w] «El truco es dejar de pensar en las velas como un catálogo de formas que memorizar y empezar a leerlas como la huella del flujo de órdenes: un registro compacto de quién intentó qué en ese periodo y quién ganó.»
  - S013 [32w] «Es una mecha inferior de ~600 puntos bajo un cuerpo diminuto: los vendedores empujaron el precio ~1% por debajo del soporte, los compradores absorbieron todo el empuje y lo devolvieron por encima.»
  - S033 [50w] «Este mismo fenómeno existe a dos escalas mayores, y dice exactamente igual de poco en cada una: a lo largo de una serie de barras es la cuña y el triángulo de m15-l2, y a lo largo de un régimen de mercado entero es el ciclo de volatilidad de m16-l1.»
  - S035 [35w] «Una mecha de rechazo en el retroceso 0,618, sobre un soporte antiguo que ya ha aguantado dos veces, es información, porque el *nivel* es lo que los compradores defendían y la mecha los muestra defendiéndolo.»
  - S050 [47w] «Y como con los niveles autocumplidos de m13, un nombre muy vigilado importa *un poco* más precisamente porque miles de traders lo leen igual y actúan sobre él, lo que también es su límite: la ventaja es ajustada, está masificada y nunca sustituye al nivel de debajo.»
  - S061 [31w] «La gente se convence de un "doji de giro" a posteriori; en directo, es el mercado diciéndote que no ha decidido, lo cual no es permiso para decidir tú por él.»
  - S063 [46w] «Los mercados funcionan 24/7, así que muchísimas velas se forman en libros poco profundos de fin de semana y de madrugada, donde un *puñado* de órdenes puede dejar una mecha muy pronunciada que parece un rechazo de peso y en realidad es un vacío de liquidez.»
  - S065 [34w] «Y como el apalancamiento amontona stops y liquidaciones justo pasados los niveles obvios, una mecha larga que atraviesa un nivel es a menudo un stop-hunt: flujo de órdenes real, pero fabricado, no convicción orgánica.»
  - S067 [38w **aside-only** (29w without asides)] «Una vela es la huella del flujo de órdenes, y casi todo se reduce a dos mecánicas: un rechazo —una mecha larga empujada hasta un precio y devuelta— y un overrun, un cuerpo envolvente que arrolla al anterior.»
  - S069 [34w] «La ubicación es el 90 % de la señal, así que el mismo martillo es información en un nivel defendido y ruido en espacio abierto: no hay sesenta patrones, hay dos mecánicas con sesenta nombres.»
- **7 No solo / not only** (1)
  - S021 «Los compradores no solo empujaron el precio; arrollaron todo lo que los vendedores del periodo anterior habían construido.»
- **8 Repeated paragraph opener** (1)
  - S053 ["La versión" ×3 (S053, S056, S059)] 
- **9 Course-coined term** (8)
  - S004 ["overrun" as a named candle mechanic (standard term: engulfing / momentum candle)] «Casi todo lo que necesitas se reduce a dos mecánicas: un rechazo (el precio fue empujado a un precio y devuelto) y un overrun (un lado arrolló al otro).»
  - S016 ["overrun"] «Donde un rechazo es una batalla *ganada en un extremo*, un overrun es un lado arrollando al otro sin más.»
  - S036 ["espacio abierto" = price away from any level (standard: tierra de nadie / zona media)] «La misma mecha en espacio abierto, sin apoyarse en ningún nivel, es ruido con una mecha.»
  - S040 ["overrun"] «Así que la lectura son siempre dos preguntas, en orden: *cuál es la mecánica* (rechazo, overrun o nada) y —la que decide su peso— *dónde ocurrió*.»
  - S045 ["overrun"] «un *overrun* (un cuerpo se traga el rango anterior).»
  - S054 ["overrun"] «Un rechazo que no rechazó nada, un overrun que no arrolló nada que nadie defendiera: saltan constantemente y por sí solos casi no significan nada.»
  - S067 ["overrun"] «Una vela es la huella del flujo de órdenes, y casi todo se reduce a dos mecánicas: un rechazo —una mecha larga empujada hasta un precio y devuelta— y un overrun, un cuerpo envolvente que arrolla al anterior.»
  - S069 ["espacio abierto"] «La ubicación es el 90 % de la señal, así que el mismo martillo es información en un nivel defendido y ruido en espacio abierto: no hay sesenta patrones, hay dos mecánicas con sesenta nombres.»
- **10 Metaphor then gloss** (3)
  - S003 [metaphor "la huella del flujo de órdenes", glossed after the colon ("un registro compacto de…")] «El truco es dejar de pensar en las velas como un catálogo de formas que memorizar y empezar a leerlas como la huella del flujo de órdenes: un registro compacto de quién intentó qué en ese periodo y quién ganó.»
  - S008 [metaphor "fósil de una batalla perdida", glossed by S009] «Una mecha larga es el fósil de una batalla perdida.»
  - S052 [metaphor "el mismo error con ropa distinta", glossed after the colon] «Las tres formas en que este conocimiento se vuelve en tu contra son el mismo error con ropa distinta: leer la forma y olvidar la ubicación.»
- **11 Synonym rotation** (1)
  - S008 [buyer/seller contest at the wick: batalla (S008), transacción (S010), pelea (S014), lucharon (S027)] 
- **A absolutes** (4)
  - S040 [siempre] «Así que la lectura son siempre dos preguntas, en orden: *cuál es la mecánica* (rechazo, overrun o nada) y —la que decide su peso— *dónde ocurrió*.»
  - S042 [nunca] «Conviene que sepas entender esa lengua franca, así que aquí tienes el diccionario, mapeado sobre las dos mecánicas más la ubicación, nunca como señales por sí solas:»
  - S050 [nunca] «Y como con los niveles autocumplidos de m13, un nombre muy vigilado importa *un poco* más precisamente porque miles de traders lo leen igual y actúan sobre él, lo que también es su límite: la ventaja es ajustada, está masificada y nunca sustituye al nivel de debajo.»
  - S051 [siempre] «Siempre que este curso usa un nombre, es una abreviatura de "esta mecánica, en esta ubicación", nada más.»

**EN** — 37 hits, 69 sentences, density 53.6

- **1 Filler** (8)
  - S016 ["simply": intensifier] «Where a rejection is a battle *won at an extreme*, an overrun is one side simply steamrolling the other.»
  - S033 ["exactly": emphatic, "says as little" carries it] «This same phenomenon exists at two larger scales, and says exactly as little at each: across a run of bars it is the wedge and the triangle of m15-l2, and across a whole market regime it is the volatility cycle of m16-l1.»
  - S034 [other filler: "Here is the rule that governs everything above:" announcer] «Here is the rule that governs everything above: **a candle's meaning comes overwhelmingly from where it happens.**»
  - S038 ["exactly": emphatic before a cross-reference] «This is exactly m13's stance that "the fib doesn't create the level": the candle doesn't create the signal either.»
  - S049 [other filler: "The takeaway is blunt:" announcer] «The takeaway is blunt: there aren't 60 patterns, there are two mechanics wearing 60 names.»
  - S050 ["precisely": emphatic before "because"] «And like m13's self-fulfilling levels, a widely watched name matters *a little* more precisely because thousands of traders are reading it the same way and acting on it — which is also its limit: the edge is thin, crowded, and never a substitute for the level underneath.»
  - S051 ["nothing more": tag] «Whenever this course uses a name, it's shorthand for "this mechanic, at this location" — nothing more.»
  - S060 [other filler: "full stop" tag] «A doji at a random spot is indecision, full stop.»
- **2 Rhythmic triad** (2)
  - S050 ["thin, crowded, and never a substitute": thin/crowded overlap; drop "crowded"] «And like m13's self-fulfilling levels, a widely watched name matters *a little* more precisely because thousands of traders are reading it the same way and acting on it — which is also its limit: the edge is thin, crowded, and never a substitute for the level underneath.»
  - S053 [frame triad across paragraphs: "The plain version… The studious version… (S056) The wishful version… (S059)"] «The plain version is spotting a textbook hammer or engulfing *anywhere* and taking it.»
- **4 Summary/uplift closer** (5)
  - S002 [ahead: announces what the lesson will do] «This lesson finally says what a *reaction* looks like.»
  - S021 [restate: re-tells the engulfing just described ("didn't just… they overran")] «Buyers didn't just nudge price; they overran everything the last period's sellers built.»
  - S039 [restate: repeats S036–S038] «It's a reaction *to* something, and if there's nothing to react to, there's no signal.»
  - S051 [restate/editorial: repeats the "two mechanics wearing 60 names" point] «Whenever this course uses a name, it's shorthand for "this mechanic, at this location" — nothing more.»
  - S069 [restate: summary ends on the slogan already said in S067] «Location is 90% of the signal, so the same hammer is information at a defended level and noise in open space — there are not sixty patterns, there are two mechanics wearing sixty names.»
- **5 Sentence over 30 words** (8)
  - S001 [40w] «Over and over this course tells you to "wait for price to react at the level" — at a broken support on the retest (m08), at a Fibonacci pullback (m13 step 4), at the spring that tests a Wyckoff range (m09).»
  - S003 [38w] «The trick is to stop thinking of candles as a catalogue of shapes to memorise and start reading them as the footprint of order flow — a compact record of who tried what in that period, and who won.»
  - S033 [42w] «This same phenomenon exists at two larger scales, and says exactly as little at each: across a run of bars it is the wedge and the triangle of m15-l2, and across a whole market regime it is the volatility cycle of m16-l1.»
  - S035 [33w] «A rejection wick at the 0.618 retracement, over an old support that has already held twice, is information — because the *level* is what buyers were defending, and the wick shows them defending it.»
  - S050 [46w] «And like m13's self-fulfilling levels, a widely watched name matters *a little* more precisely because thousands of traders are reading it the same way and acting on it — which is also its limit: the edge is thin, crowded, and never a substitute for the level underneath.»
  - S063 [37w] «Markets run 24/7, so a great many candles form in thin weekend and overnight books where a *handful* of orders can print a dramatic wick that looks like a heavyweight rejection and is really a liquidity vacuum.»
  - S067 [41w] «A candle is the footprint of order flow, and almost all of it reduces to two mechanics: a rejection — a long wick pushed to a price and thrown back — and an overrun, an engulfing body that steamrolled the one before it.»
  - S069 [33w] «Location is 90% of the signal, so the same hammer is information at a defended level and noise in open space — there are not sixty patterns, there are two mechanics wearing sixty names.»
- **7 No solo / not only** (1)
  - S021 «Buyers didn't just nudge price; they overran everything the last period's sellers built.»
- **9 Course-coined term** (8)
  - S004 ["overrun" as a named candle mechanic] «Almost everything you need reduces to two mechanics: a rejection (price was pushed to a price and thrown back) and an overrun (one side steamrolled the other).»
  - S016 ["overrun"] «Where a rejection is a battle *won at an extreme*, an overrun is one side simply steamrolling the other.»
  - S036 ["open space" = price away from any level] «The identical wick in open space, leaning on no level, is noise with a wick.»
  - S040 ["overrun"] «So the read is always two questions, in order: *what is the mechanic* (rejection, overrun, or nothing), and — the one that decides its weight — *where did it happen*.»
  - S045 ["overrun"] «an *overrun* (one body swallows the prior range).»
  - S054 ["overrun"] «A rejection that rejected nothing, an overrun that overran nothing anyone was defending — these fire constantly and mean almost nothing on their own.»
  - S067 ["overrun"] «A candle is the footprint of order flow, and almost all of it reduces to two mechanics: a rejection — a long wick pushed to a price and thrown back — and an overrun, an engulfing body that steamrolled the one before it.»
  - S069 ["open space"] «Location is 90% of the signal, so the same hammer is information at a defended level and noise in open space — there are not sixty patterns, there are two mechanics wearing sixty names.»
- **10 Metaphor then gloss** (3)
  - S003 [metaphor "the footprint of order flow", glossed after the dash] «The trick is to stop thinking of candles as a catalogue of shapes to memorise and start reading them as the footprint of order flow — a compact record of who tried what in that period, and who won.»
  - S008 [metaphor "the fossil of a lost battle", glossed by S009] «A long wick is the fossil of a lost battle.»
  - S052 [metaphor "the same error wearing different clothes", glossed after the colon] «All three ways this knowledge backfires are the same error wearing different clothes: reading the form and forgetting the location.»
- **11 Synonym rotation** (2)
  - S004 [the overrun action: steamrolled (S004, S016), run over (S018), overran (S021), swallowing (S020)] 
  - S008 [buyer/seller contest at the wick: battle (S008), exchange (S010), fight (S014), fought to a draw (S027)] 
- **A absolutes** (3)
  - S040 [always] «So the read is always two questions, in order: *what is the mechanic* (rejection, overrun, or nothing), and — the one that decides its weight — *where did it happen*.»
  - S042 [never] «You should be able to parse that lingua franca, so here is the dictionary — mapped onto the two mechanics plus location, never as standalone signals:»
  - S050 [never] «And like m13's self-fulfilling levels, a widely watched name matters *a little* more precisely because thousands of traders are reading it the same way and acting on it — which is also its limit: the edge is thin, crowded, and never a substitute for the level underneath.»

### m09-l1

**ES** — 31 hits, 87 sentences, density 35.6

- **1 Filler** (4)
  - S040 [other filler: "clave" in "la pregunta clave" is an intensifier] «Por eso la pregunta clave nunca es «¿está yendo de lado?», sino **«¿quién está absorbiendo, y en qué lado?»**»
  - S065 [other filler: "justo" in "son justo la liquidez" is emphatic] «La lógica de ambos es la misma trampa: una ruptura que todos ven atrae órdenes, y esas órdenes son justo la liquidez que un gran participante necesita para terminar su posición en el lado *contrario*.»
  - S071 [other filler: "justo cuando" emphatic] «Un rango que una acción construiría en 30 sesiones puede formarse y resolverse en un solo fin de semana, justo cuando la liquidez es más fina y un movimiento encuentra menos resistencia.»
  - S087 [other filler: "justo las órdenes" emphatic] «Las dos pistas son el spring —una falsa ruptura por debajo del soporte que se recupera, dentro de la acumulación— y el upthrust por encima de la resistencia dentro de la distribución; ambos son la misma trampa, porque una ruptura que todos ven atrae justo las órdenes que un gran participante necesita en el lado contrario.»
- **2 Rhythmic triad** (2)
  - S002 ["fondos, mesas de trading, cualquiera que mueva tamaño": the third subsumes the first two; drop "mesas de trading" (or the two examples)] «La idea central es que los grandes participantes —fondos, mesas de trading, cualquiera que mueva tamaño— no pueden comprar ni vender todo de golpe sin mover el precio en su contra.»
  - S003 ["en silencio, a lo largo del tiempo, dentro de un rango lateral": "en silencio" overlaps "a lo largo del tiempo" (patient); drop "en silencio"] «Así que trabajan en silencio, a lo largo del tiempo, dentro de un rango lateral.»
- **4 Summary/uplift closer** (5)
  - S008 [editorial: meta line about the lesson's goal] «Aquí el objetivo es ver cómo encajan las piezas.»
  - S031 [ahead: points to the schematic after the paragraph's content ended at S030] «El esquema de abajo traza una vuelta completa: una tendencia bajista previa que se estanca en un rango, las fases A–E, el spring en la fase C y el markup que lo resuelve.»
  - S040 [editorial: "Por eso la pregunta clave…" reframes S036–S039 as a question] «Por eso la pregunta clave nunca es «¿está yendo de lado?», sino **«¿quién está absorbiendo, y en qué lado?»**»
  - S043 [editorial: "Para el mapa, con esto basta."] «Para el mapa, con esto basta.»
  - S067 [ahead: points to the distribution schematic after the content ended at S066] «El esquema de distribución de abajo muestra el espejo del de acumulación: una tendencia alcista previa, el rango y un upthrust (UTAD) en la fase C.»
- **5 Sentence over 30 words** (15)
  - S002 [31w **aside-only** (23w without asides)] «La idea central es que los grandes participantes —fondos, mesas de trading, cualquiera que mueva tamaño— no pueden comprar ni vender todo de golpe sin mover el precio en su contra.»
  - S012 [51w] «Tiene dos opciones: pagar de más barriendo todas las ofertas de arriba —moviendo el precio un 8–10% en su contra y anunciando su intención a todo el mercado— o ir metiendo órdenes pequeñas durante días y semanas, comprando 100–200 cada vez en cada caída, dejando que los vendedores acudan a ella.»
  - S017 [31w **aside-only** (11w without asides)] «Wyckoff describe el mercado como un ciclo repetido de cuatro etapas (que aquí mantenemos distintas de las *fases* con letra A–E que describen la vida de un rango concreto, más abajo):»
  - S031 [33w] «El esquema de abajo traza una vuelta completa: una tendencia bajista previa que se estanca en un rango, las fases A–E, el spring en la fase C y el markup que lo resuelve.»
  - S034 [38w] «Lo que sostiene Wyckoff es que pasa muchísimo: un gran participante necesita muchas sesiones de ir y venir para llenar una orden grande sin disparar el precio, de modo que el rango *es* la acumulación o la distribución.»
  - S052 [32w **aside-only** (28w without asides)] «Mantén separados los dos vocabularios: las etapas (acumulación → markup → distribución → markdown) nombran el *ciclo* por el que pasa el mercado entero; las fases A–E nombran la *vida interior de un solo rango*.»
  - S058 [38w] «*En concreto:* el soporte aguanta en 1.800 durante dos semanas; un estallido de ventas hunde el precio a 1.745 y dispara los stops apilados justo bajo 1.800; en una o dos sesiones el precio reconquista 1.800 y aguanta.»
  - S064 [43w] «El upthrust decisivo de la fase C que marca el techo de una distribución tiene nombre propio —el UTAD (upthrust after distribution, «empuje tras la distribución»)— para distinguirlo de los upthrusts menores y no concluyentes que pueden aparecer antes, en la fase B.»
  - S065 [35w] «La lógica de ambos es la misma trampa: una ruptura que todos ven atrae órdenes, y esas órdenes son justo la liquidez que un gran participante necesita para terminar su posición en el lado *contrario*.»
  - S066 [37w] «Un soporte visible con stops aparcados debajo es un charco de órdenes de venta forzada esperando a ser recolectado; una resistencia visible con compradores de ruptura encima es un charco de demanda esperando a que le vendan.»
  - S071 [32w] «Un rango que una acción construiría en 30 sesiones puede formarse y resolverse en un solo fin de semana, justo cuando la liquidez es más fina y un movimiento encuentra menos resistencia.»
  - S072 [41w] «En un libro de órdenes poco profundo de una altcoin, una venta a mercado relativamente pequeña puede hacer una mecha del 5–8% por debajo del soporte, barrer los stops y los niveles de liquidación agrupados justo debajo y darse la vuelta.»
  - S076 [43w] «Ese amontonamiento es lo que hace la falsa ruptura una cosecha tan fiable, y también significa que un «markup» que sale de un spring puede no ser más que un short squeeze: cortos amontonados a los que fuerzan a cerrar, no demanda real.»
  - S085 [31w] «Wyckoff lee un rango lateral como un gran participante trabajando una orden en porciones, porque el tamaño no se compra ni se vende de golpe sin mover el precio en contra.»
  - S087 [56w] «Las dos pistas son el spring —una falsa ruptura por debajo del soporte que se recupera, dentro de la acumulación— y el upthrust por encima de la resistencia dentro de la distribución; ambos son la misma trampa, porque una ruptura que todos ven atrae justo las órdenes que un gran participante necesita en el lado contrario.»
- **9 Course-coined term** (4)
  - S005 [lente [seed]] «Wyckoff es una lente para leer esa forma, no una señal mecánica ni una garantía.»
  - S066 [seed "charco" (= liquidity pool in the stop-cluster sense): "charco de órdenes de venta forzada", "charco de demanda"] «Un soporte visible con stops aparcados debajo es un charco de órdenes de venta forzada esperando a ser recolectado; una resistencia visible con compradores de ruptura encima es un charco de demanda esperando a que le vendan.»
  - S066 ["recolectado" / "cosecha" (S076): stop clusters as a harvest, a repeated metaphor not standard vocabulary] «Un soporte visible con stops aparcados debajo es un charco de órdenes de venta forzada esperando a ser recolectado; una resistencia visible con compradores de ruptura encima es un charco de demanda esperando a que le vendan.»
  - S076 ["cosecha": the false break as "una cosecha tan fiable"] «Ese amontonamiento es lo que hace la falsa ruptura una cosecha tan fiable, y también significa que un «markup» que sale de un spring puede no ser más que un short squeeze: cortos amontonados a los que fuerzan a cerrar, no demanda real.»
- **11 Synonym rotation** (1)
  - S058 [stop cluster below support: stops apilados (S058), charco de órdenes de venta forzada (S066), agrupados (S072), amontonan (S075), amontonamiento (S076)] 
- **A absolutes** (1)
  - S040 [nunca] «Por eso la pregunta clave nunca es «¿está yendo de lado?», sino **«¿quién está absorbiendo, y en qué lado?»**»

**EN** — 25 hits, 87 sentences, density 28.7

- **1 Filler** (4)
  - S040 ["The key": intensifier, "The question is never…" carries it] «The key question is therefore never "is it going sideways?" but **"who is doing the absorbing, and on which side?"**»
  - S065 ["exactly": emphatic] «The logic behind both is the same trap: a break that everyone can see attracts orders, and those orders are exactly the liquidity a big player needs to finish their position on the *opposite* side.»
  - S071 ["precisely": emphatic, not pinning a quantity] «A range a stock might build over 30 sessions can form and resolve over a single weekend — precisely when liquidity is thinnest and a move meets the least resistance.»
  - S087 ["exactly": emphatic] «The two tells are the spring — a false break below support that recovers, inside accumulation — and the upthrust above resistance inside distribution; both are the same trap, because a break everyone can see attracts exactly the orders a big player needs on the opposite side.»
- **2 Rhythmic triad** (2)
  - S002 ["funds, desks, anyone moving size": the third subsumes the first two; drop "desks" (or the two examples)] «The core idea is that big players — funds, desks, anyone moving size — cannot buy or sell everything at once without moving the price against themselves.»
  - S003 ["quietly, over time, inside a sideways range": "quietly" overlaps "over time"; drop "quietly"] «So they work quietly, over time, inside a sideways range.»
- **4 Summary/uplift closer** (5)
  - S008 [editorial: meta line about the lesson's goal] «Here the goal is to see how the pieces fit.»
  - S031 [ahead: points to the schematic after the paragraph's content ended at S030] «The schematic below traces one full turn — a prior downtrend stalling into a range, the phases A–E, the spring at phase C, and the markup that resolves it.»
  - S040 [editorial: "The key question is therefore…" reframes S036–S039 as a question] «The key question is therefore never "is it going sideways?" but **"who is doing the absorbing, and on which side?"**»
  - S043 [editorial: "For the map, this is enough"] «For the map, this is enough:»
  - S067 [ahead: points to the distribution schematic after the content ended at S066] «The distribution schematic below shows the mirror of the accumulation one: a prior uptrend, the range, and an upthrust (UTAD) at phase C.»
- **5 Sentence over 30 words** (8)
  - S012 [46w] «It has two choices: pay up through every offer above — moving the price 8–10% against itself and announcing its intent to the whole market — or feed small orders in over days and weeks, buying 100–200 at a time on every dip, letting sellers come to it.»
  - S034 [35w] «Wyckoff's claim is that a great deal is happening: a large player needs many sessions of two-way churn to fill a big order without spiking the price, so the range *is* the accumulation or distribution.»
  - S058 [33w] «*Concretely:* support holds at 1,800 for two weeks; a burst of selling flushes price to 1,745, tripping the stops stacked just under 1,800; within a session or two price reclaims 1,800 and holds.»
  - S064 [36w] «The decisive phase-C upthrust that marks the top of a distribution has its own name — the UTAD (upthrust after distribution) — to set it apart from the smaller, inconclusive upthrusts that can appear earlier, in phase B.»
  - S065 [35w] «The logic behind both is the same trap: a break that everyone can see attracts orders, and those orders are exactly the liquidity a big player needs to finish their position on the *opposite* side.»
  - S066 [37w] «A visible support with stops parked beneath it is a pool of forced sell orders waiting to be harvested; a visible resistance with breakout buyers above it is a pool of demand waiting to be sold into.»
  - S076 [37w] «That crowding is what makes the false break so reliable a harvest — and it also means a "markup" out of a spring can be nothing more than a short squeeze: crowded shorts being force-closed, not real demand.»
  - S087 [45w] «The two tells are the spring — a false break below support that recovers, inside accumulation — and the upthrust above resistance inside distribution; both are the same trap, because a break everyone can see attracts exactly the orders a big player needs on the opposite side.»
- **9 Course-coined term** (4)
  - S005 [lens [seed]] «Wyckoff is a lens for reading that shape, not a mechanical signal and not a guarantee.»
  - S066 [seed "pool" (liquidity pool in the stop-cluster sense): "a pool of forced sell orders", "a pool of demand"] «A visible support with stops parked beneath it is a pool of forced sell orders waiting to be harvested; a visible resistance with breakout buyers above it is a pool of demand waiting to be sold into.»
  - S066 ["harvested" / "harvest" (S076): stop clusters as a harvest, a repeated metaphor not standard vocabulary] «A visible support with stops parked beneath it is a pool of forced sell orders waiting to be harvested; a visible resistance with breakout buyers above it is a pool of demand waiting to be sold into.»
  - S076 ["harvest": the false break as "so reliable a harvest"] «That crowding is what makes the false break so reliable a harvest — and it also means a "markup" out of a spring can be nothing more than a short squeeze: crowded shorts being force-closed, not real demand.»
- **11 Synonym rotation** (2)
  - S002 [large participant: big players (S002), a desk (S010), large players (S019), a large player (S034), a big player (S065)] 
  - S058 [stop cluster below support: stops stacked (S058), pool of forced sell orders (S066), clustered (S072), pile (S075), crowding (S076)] 
- **A absolutes** (1)
  - S040 [never] «The key question is therefore never "is it going sideways?" but **"who is doing the absorbing, and on which side?"**»

### m09-l2

**ES** — 37 hits, 70 sentences, density 52.9

- **1 Filler** (4)
  - S008 ["exactamente": emphatic, "una instancia generada de esta forma" says the same] «La figura de aquí abajo es una instancia generada con exactamente esta forma, y los números de esta lección son sus valores redondeados: las dos líneas que verás dibujadas son ese soporte y esa resistencia, y todo lo que contamos a partir de ahora ocurre entre ellas.»
  - S021 ["de verdad": emphatic ("el trabajo de verdad")] «aquí es donde ocurre el trabajo de verdad.»
  - S030 [other filler: "justo" in "son justo la última oferta barata" is emphatic] «Un mínimo nuevo y visible activa los stops que descansan bajo el soporte y tienta a cortos nuevos, y esas órdenes de venta son justo la última oferta barata que un gran comprador necesita para terminar.»
  - S059 [other filler: "La simetría es exacta:" announcer] «La simetría es exacta: un spring es una falsa ruptura *por debajo* del soporte que insinúa un *markup*; un upthrust es una falsa ruptura *por encima* de la resistencia que avisa de un *markdown*.»
- **2 Rhythmic triad** (1)
  - S004 ["de 2.050 a 1.800 en varias semanas, una tendencia bajista limpia, con los vendedores al mando": the last two overlap; drop "con los vendedores al mando"] «Toma una moneda que ha caído con fuerza: de unos 2.050 a 1.800 en varias semanas, una tendencia bajista limpia, con los vendedores al mando.»
- **4 Summary/uplift closer** (7)
  - S003 [motivate: goal statement ("para que reconozcas la forma…") closing the intro] «El objetivo no es memorizar un esquema, sino ver *por qué* cada fase tiene el aspecto que tiene, para que reconozcas la forma cuando los números sean otros y el gráfico esté más sucio.»
  - S012 [restate: S011 already showed the fall stopping and both boundaries forming] «A partir de ahí, la caída libre se ha terminado y existen los dos límites del rango.»
  - S015 [restate: "el rango no aparece de la nada, lo construyen un suelo… y un techo…" re-tells S014] «Esos dos eventos *dibujan* las líneas de soporte y resistencia: el rango no aparece de la nada, lo construyen un suelo que aguanta y un techo que tapa.»
  - S017 [restate: "después tienes una caja" re-tells the example] «Antes de la fase A tenías un mercado que caía; después tienes una caja.»
  - S034 [editorial: "El spring hizo su trabajo."] «El spring hizo su trabajo.»
  - S040 [editorial: "…es un mercado que ha cambiado de manos" sums up S037–S039] «Un mercado que ya no necesita bajar a 1.800 para encontrar compradores es un mercado que ha cambiado de manos.»
  - S047 [editorial: "El rango fue la causa; el markup es el efecto."] «El rango fue la causa; el markup es el efecto.»
- **5 Sentence over 30 words** (24)
  - S002 [46w] «Esta lección va más despacio y recorre un único rango de acumulación de principio a fin, fase por fase, con números aproximados para que cada etapa sea concreta; luego le da la vuelta a todo para mostrar que la distribución es la misma historia del revés.»
  - S003 [34w] «El objetivo no es memorizar un esquema, sino ver *por qué* cada fase tiene el aspecto que tiene, para que reconozcas la forma cuando los números sean otros y el gráfico esté más sucio.»
  - S008 [47w] «La figura de aquí abajo es una instancia generada con exactamente esta forma, y los números de esta lección son sus valores redondeados: las dos líneas que verás dibujadas son ese soporte y esa resistencia, y todo lo que contamos a partir de ahora ocurre entre ellas.»
  - S009 [31w] «Léela de izquierda a derecha según avanzamos: la tendencia bajista hacia el rango, el ir y venir, el pinchazo por debajo del soporte que se recupera y la salida al alza.»
  - S011 [36w] «La caída pierde fuelle al llegar a 1.930 y el precio entra en el rango; el primer tramo dentro baja hasta 1.800 y encuentra compra; el rebote sube otra vez hasta 1.930 y se frena ahí.»
  - S014 [36w] «El rebote desde 1.800 es la primera señal de que los compradores pueden absorber todo lo que les echen; que la subida se pare exactamente donde se paró la anterior dice que arriba hay oferta esperando.»
  - S022 [39w] «Un gran comprador no puede levantar el precio de 1.800 a 1.930 de una sola vez sin dispararlo en su contra, así que compra con paciencia en las caídas y deja que vuelva a subir, una y otra vez.»
  - S026 [32w **aside-only** (23w without asides)] «cerca del final del rango, el precio pincha *por debajo* del soporte —hasta 1.745, un 3% bajo el suelo de 1.800— y luego vuelve rápido hacia dentro, en tres o cuatro velas.»
  - S030 [36w] «Un mínimo nuevo y visible activa los stops que descansan bajo el soporte y tienta a cortos nuevos, y esas órdenes de venta son justo la última oferta barata que un gran comprador necesita para terminar.»
  - S033 [42w] «la mecha hasta 1.745 dispara los stops de todos; el precio está de nuevo por encima de 1.800 tres velas después; y a partir de ahí ninguna caída vuelve a perder el soporte —la más profunda de todas se queda en 1.810—.»
  - S036 [31w **aside-only** (19w without asides)] «Se asienta en una banda estrecha en torno a 1.870 —a media altura del rango, unos 70 puntos por encima del soporte— y se queda ahí hasta el final del rango.»
  - S039 [31w] «El manual dibuja eso como mínimos crecientes apoyándose en el techo; lo que siempre se cumple, y lo que ves aquí, es lo otro: el suelo del rango deja de tocarse.»
  - S048 [42w **aside-only** (30w without asides)] «un cierre por encima de 1.930 que no vuelve a caer hacia dentro, seguido de una tendencia al alza que llega hasta 2.210 —por encima incluso de los 2.050 donde había empezado toda la caída—: la recompensa de toda esa compra paciente.»
  - S051 [33w] «La figura de abajo es, otra vez, una instancia generada de esa forma, con sus propios precios: un rango entre un soporte en torno a 28.140 y una resistencia en torno a 29.640.»
  - S053 [33w **aside-only** (27w without asides)] «La fase A es la subida perdiendo fuelle al llegar a 29.640, una reacción a la baja hasta 28.140 y un rebote que vuelve a frenarse arriba —lo que dibuja las dos líneas—.»
  - S055 [31w **aside-only** (27w without asides)] «La fase C es el upthrust: el precio asoma sobre la resistencia hasta 30.590 —un 3% por encima—, atrapa a los compradores de ruptura y luego fracasa y vuelve hacia dentro.»
  - S056 [40w] «El upthrust decisivo de la fase C que marca el techo tiene nombre propio —el UTAD (upthrust after distribution, «empuje tras la distribución»)— para distinguirlo de los asomos menores y no concluyentes que pueden ocurrir antes, en la fase B.»
  - S057 [36w] «En la fase D el precio deja de visitar el techo y se asienta en torno a 29.000: ningún rebote posterior vuelve a alcanzar la resistencia, y el más alto de todos se queda en 29.350.»
  - S059 [34w] «La simetría es exacta: un spring es una falsa ruptura *por debajo* del soporte que insinúa un *markup*; un upthrust es una falsa ruptura *por encima* de la resistencia que avisa de un *markdown*.»
  - S062 [77w] «En un libro de órdenes fino de una altcoin hace falta muy poco tamaño para empujar el precio más allá de un nivel de soporte o resistencia, así que una mecha de caza de stops —un pico rápido que activa el racimo de stops que descansan justo más allá del límite y que incluso puede provocar la liquidación forzosa de posiciones sobreapalancadas— es fácil de fabricar y fácil de confundir con un spring o un upthrust auténtico.»
  - S065 [39w] «Primera: la *profundidad* de un spring o un upthrust importa menos en cripto que la *recuperación*; una mecha profunda en un libro poco profundo es barata de producir, así que exige un rebote limpio hacia dentro antes de fiarte.»
  - S066 [35w **aside-only** (27w without asides)] «Segunda: como el mercado funciona 24/7 sin campana de cierre, estas pruebas suelen ocurrir en horas de baja liquidez —fines de semana y tiempos muertos entre sesiones— cuando una orden pequeña mueve más el precio.»
  - S068 [65w] «Un rango de acumulación recorrido de principio a fin: la fase A detiene la tendencia bajista previa y dibuja los dos límites, la fase B es el ir y venir largo que construye la causa, la fase C es el spring y su prueba, la fase D es el precio dejando de visitar el suelo, y la fase E es el markup abandonando el rango.»
  - S070 [34w] «La habilidad es leer la tendencia previa y la recuperación antes del movimiento que te daría la razón: un pinchazo bajo el soporte que sigue cayendo nunca fue un spring, fue una ruptura bajista.»
- **10 Metaphor then gloss** (1)
  - S029 [metaphor "es un cebo", glossed by S030 (stops trip, shorts tempted, big buyer fills)] «la ruptura por debajo de 1.800 es un cebo.»
- **A absolutes** (2)
  - S039 [siempre] «El manual dibuja eso como mínimos crecientes apoyándose en el techo; lo que siempre se cumple, y lo que ves aquí, es lo otro: el suelo del rango deja de tocarse.»
  - S070 [nunca, summary] «La habilidad es leer la tendencia previa y la recuperación antes del movimiento que te daría la razón: un pinchazo bajo el soporte que sigue cayendo nunca fue un spring, fue una ruptura bajista.»

**EN** — 27 hits, 70 sentences, density 38.6

- **1 Filler** (4)
  - S008 ["exactly": emphatic, "one generated instance of this shape" says the same] «The figure just below is one generated instance of exactly this shape, and this lesson's numbers are its values rounded off: the two lines you will see drawn are that support and that resistance, and everything we describe from here on happens between them.»
  - S021 [other filler: "real" in "the real work" is emphatic] «this is where the real work happens.»
  - S030 ["exactly": emphatic] «A visible new low trips the stop-losses resting under support and tempts fresh shorts, and those sell orders are exactly the last cheap supply a big buyer needs to finish.»
  - S059 [other filler: "The symmetry is exact:" announcer] «The symmetry is exact: a spring is a fake break *below* support that hints at a *markup*; an upthrust is a fake break *above* resistance that warns of a *markdown*.»
- **2 Rhythmic triad** (1)
  - S004 ["from 2,050 down to 1,800 over several weeks — a clean downtrend, sellers in control": the last two overlap; drop "sellers in control"] «Take a coin that has fallen hard: from about 2,050 down to 1,800 over several weeks — a clean downtrend, sellers in control.»
- **4 Summary/uplift closer** (7)
  - S003 [motivate: goal statement ("so you can recognise the shape…") closing the intro] «The point is not to memorise a schematic; it is to see *why* each phase looks the way it does, so you can recognise the shape when the numbers are different and the chart is messier.»
  - S012 [restate: S011 already showed the fall stopping and both boundaries forming] «After that, the freefall is over and the two boundaries of the range exist.»
  - S015 [restate: "the range does not appear from nowhere, it is built by a floor… and a ceiling…" re-tells S014] «Those two events *draw* the support and resistance lines — the range does not appear from nowhere, it is built by a floor that holds and a ceiling that caps.»
  - S017 [restate: "after it you have a box" re-tells the example] «Before phase A you had a falling market; after it you have a box.»
  - S034 [editorial: "The spring did its job."] «The spring did its job.»
  - S040 [editorial: "…is a market that has changed hands" sums up S037–S039] «A market that no longer needs to go down to 1,800 to find buyers is a market that has changed hands.»
  - S047 [editorial: "The range was the cause; the markup is the effect."] «The range was the cause; the markup is the effect.»
- **5 Sentence over 30 words** (14)
  - S002 [41w] «This lesson slows down and walks a single accumulation range from start to finish, phase by phase, with rough numbers so each stage is concrete — then flips the whole thing over to show that distribution is the same story upside down.»
  - S003 [36w] «The point is not to memorise a schematic; it is to see *why* each phase looks the way it does, so you can recognise the shape when the numbers are different and the chart is messier.»
  - S008 [44w] «The figure just below is one generated instance of exactly this shape, and this lesson's numbers are its values rounded off: the two lines you will see drawn are that support and that resistance, and everything we describe from here on happens between them.»
  - S011 [34w] «The fall loses its momentum as it reaches 1,930 and price enters the range; the first leg inside drops to 1,800 and finds buyers; the bounce carries back up to 1,930 and stalls there.»
  - S014 [34w] «The bounce off 1,800 is the first sign that buyers can absorb everything thrown at them; the rally stopping at exactly the price the last one stopped at says there is supply waiting above.»
  - S022 [33w] «A large buyer cannot lift 1,800 to 1,930 in one go without spiking the price against themselves, so they buy patiently on the dips and let it drift back up, over and over.»
  - S033 [34w] «the wick to 1,745 fires everyone's stops; price is back above 1,800 three candles later; and from then on no dip ever loses the support again — the deepest of them all stops at 1,810.»
  - S039 [31w] «The textbook draws that as higher lows leaning on the ceiling; what always holds, and what you see here, is the other half: the floor of the range stops being touched.»
  - S048 [34w] «a close above 1,930 that does not fall back inside, followed by a trend up that reaches 2,210 — above even the 2,050 where the whole fall started: the payoff for all that patient buying.»
  - S056 [32w **aside-only** (27w without asides)] «The decisive phase-C upthrust that marks the top has its own name — the UTAD (upthrust after distribution) — to set it apart from smaller, inconclusive pokes that can happen earlier in phase B.»
  - S062 [57w] «In a thin alt-coin book, it takes very little size to push price through a support or resistance level, so a stop-hunt wick — a fast spike that trips the cluster of stop-losses resting just beyond the boundary and can even force-liquidate over-leveraged positions — is easy to manufacture and easy to mistake for a genuine spring or upthrust.»
  - S065 [36w] «First, the *depth* of a spring or upthrust means less in crypto than the *recovery*: a deep wick on a thin book is cheap to produce, so demand a clean snap-back inside before you trust it.»
  - S068 [54w] «One accumulation range walked end to end: phase A stops the prior downtrend and draws the two boundaries, phase B is the long churn that builds the cause, phase C is the spring and its test, phase D is price no longer visiting the floor, and phase E is the markup leaving the range.»
  - S070 [33w] «The skill is reading the prior trend and the recovery before the move that would prove you right: a stab below support that keeps falling was never a spring, it was a breakdown.»
- **10 Metaphor then gloss** (1)
  - S029 [metaphor "is bait", glossed by S030] «the break below 1,800 is bait.»
- **A absolutes** (3)
  - S039 [always] «The textbook draws that as higher lows leaning on the ceiling; what always holds, and what you see here, is the other half: the floor of the range stops being touched.»
  - S042 [never] «Phase B goes down to 1,800 over and over; phase D never once trades below 1,810.»
  - S070 [never, summary] «The skill is reading the prior trend and the recovery before the move that would prove you right: a stab below support that keeps falling was never a spring, it was a breakdown.»

### m10-l1

**ES** — 47 hits, 89 sentences, density 52.8

- **1 Filler** (9)
  - S008 ["simplemente": intensifier on "se cae por detrás"] «Esa ponderación igual tiene un coste oculto: cuando el cierre más antiguo sale de la ventana, sale *del todo*, así que la línea puede dar un tirón en una vela en la que hoy no ha pasado nada; un precio grande de hace exactamente N velas simplemente se cae por detrás.»
  - S009 [other filler: "justo" in "justo hasta el instante" emphatic] «Un cierre de hace N velas manda tanto como el de ayer, justo hasta el instante en que ya no manda nada.»
  - S018 [other filler: "El compromiso lo resume todo:" announcer] «El compromiso lo resume todo: la EMA reacciona más rápido (menos retardo), pero esa velocidad también la hace más ruidosa: gira ante movimientos que se quedan en nada.»
  - S032 [other filler: "justo" in "que es justo cuando" emphatic] «El precio picoteando a un lado y otro de un par *plano* y entrelazado es el mercado diciéndote que no hay tendencia que operar, que es justo cuando las medias móviles funcionan peor (abajo).»
  - S043 [other filler: "Pero aquí está por qué…" announcer] «Pero aquí está *por qué la señal siempre llega tarde*: para que una línea de 50 periodos suba por encima de una de 200, los precios recientes ya han tenido que arrastrar un promedio de 50 velas por encima de uno de 200, y eso requiere una subida sostenida que, por definición, ya tiene decenas de velas.»
  - S046 ["honesto": "el orden honesto" applied to an order of teaching] «Nada de lo anterior dice qué N usar, y ese es el orden honesto: primero la lectura.»
  - S077 ["en realidad": emphatic] «Los dos errores clásicos son en realidad la misma moneda.»
  - S082 ["de verdad": emphatic, "promedia cincuenta días seguidos" carries it] «Cripto opera 24/7, así que la serie de precios es ininterrumpida: una EMA50 en diario promedia de verdad cincuenta días seguidos, sin saltos en la línea provocados por huecos.»
  - S086 [other filler: "La consecuencia práctica:" announcer] «La consecuencia práctica: para lograr la misma suavidad que te daría un periodo dado en bolsa, en cripto sueles necesitar un periodo *más largo*.»
- **4 Summary/uplift closer** (8)
  - S004 [restate: "es un promedio del pasado" repeats S001–S003] «Todo lo útil y todo lo peligroso de una media móvil se desprende de ese único hecho: es un promedio del pasado.»
  - S017 [restate: re-tells the worked numbers just given] «Los mismos datos, pero la EMA ha admitido casi todo el movimiento antes de que la SMA llegue a la mitad.»
  - S020 [editorial: "Más rápida no es mejor; es otro ajuste del mismo mando."] «Más rápida no es mejor; es otro ajuste del mismo mando.»
  - S038 [editorial: "…es la habilidad que entrena este módulo"] «Aprender a reconocer esas tres imágenes de un vistazo es la habilidad que entrena este módulo.»
  - S056 [restate: repeats S054–S055 (works because watched)] «Funciona mientras la línea esté concurrida, no porque el número acierte.»
  - S072 [restate: repeats the lag/noise trade-off of S071] «Siempre estás cambiando lo uno por lo otro: no hay un ajuste que sea a la vez rápido y suave.»
  - S076 [restate: "una ristra de pérdidas disfrazadas de señales" re-tells the whipsaw of S075] «Una media móvil se gana el sueldo solo cuando hay una tendencia que suavizar; dale un mercado lateral y te devolverá una ristra de pérdidas disfrazadas de señales.»
  - S079 [editorial: "la línea es un espejo retrovisor"] «Ambos vienen de olvidar que la línea es un espejo retrovisor.»
- **5 Sentence over 30 words** (22)
  - S008 [51w] «Esa ponderación igual tiene un coste oculto: cuando el cierre más antiguo sale de la ventana, sale *del todo*, así que la línea puede dar un tirón en una vela en la que hoy no ha pasado nada; un precio grande de hace exactamente N velas simplemente se cae por detrás.»
  - S012 [32w **aside-only** (27w without asides)] «Los precios antiguos nunca desaparecen del todo —su peso solo decae geométricamente—, así que la EMA nunca da un tirón por una salida brusca y, como los cierres recientes dominan, gira antes.»
  - S015 [39w **aside-only** (28w without asides)] «La SMA10 sube en línea recta —se cambia un 100 antiguo por un 110 en cada vela—, así que marca 101, 102, 103… y solo llega a 110 tras diez velas, cuando toda la ventana son por fin 110.»
  - S028 [32w] «Cuando una MM rápida se sitúa *por encima* de una lenta, los precios recientes son más altos que los antiguos: la tendencia de corto plazo es más fuerte que la de largo.»
  - S032 [34w] «El precio picoteando a un lado y otro de un par *plano* y entrelazado es el mercado diciéndote que no hay tendencia que operar, que es justo cuando las medias móviles funcionan peor (abajo).»
  - S042 [33w] «La lógica es sólida: la línea rápida refleja los precios recientes, así que gira primero, y cuando supera a la lenta la tendencia de corto plazo se ha impuesto a la de largo.»
  - S043 [57w] «Pero aquí está *por qué la señal siempre llega tarde*: para que una línea de 50 periodos suba por encima de una de 200, los precios recientes ya han tenido que arrastrar un promedio de 50 velas por encima de uno de 200, y eso requiere una subida sostenida que, por definición, ya tiene decenas de velas.»
  - S048 [42w **aside-only** (30w without asides)] «Un scalper o un day trader que trabaja del gráfico de 1 minuto al de 15 necesita líneas que giren dentro de la sesión, así que los periodos son cortos —y, por el intercambio entre retraso y ruido de más arriba, ruidosos—.»
  - S049 [39w] «20 y 50, para swing trading, leídas en el de 4 horas y en el diario: lo bastante largas para encogerse de hombros ante una vela mala, lo bastante cortas para girar dentro de una tenencia de varios días.»
  - S051 [36w] «el par lento y más citado, y de donde les vienen el nombre al cruce dorado y al cruce de la muerte, que casi siempre se refieren a la de 50 días cruzando la de 200.»
  - S054 [45w] «Importan por la misma razón que da m13 para los niveles de Fibonacci: bastante gente vigila las mismas líneas y las órdenes en reposo se amontonan a su alrededor, así que un nivel sin ningún mecanismo detrás acaba siendo un sitio donde el precio reacciona.»
  - S058 [45w] «Las tres firmas —orden, pendiente y dónde está el precio respecto al par— tienen el mismo aspecto en un gráfico de 1 minuto con el 9/21 que en un diario con el 50/200, y por eso este módulo enseña la imagen y no los ajustes.»
  - S060 [37w] «Un cruce 9/21 en el gráfico de 5 minutos es una afirmación sobre la próxima hora, y se dará la vuelta antes de comer con la frecuencia suficiente para que un swing trader haga bien en ignorarlo.»
  - S063 [34w] «En una tendencia en marcha, el precio suele retroceder, tocar una media móvil y reanudar, así que la MM actúa como un suelo móvil en una tendencia alcista o un techo en una bajista.»
  - S064 [37w] «Parte de esto es real: la MM sigue aproximadamente el coste medio de los compradores recientes, así que un retroceso hasta ella es un retroceso hasta donde entró el tenedor promedio, y ahí suelen entrar compradores nuevos.»
  - S065 [36w] «Parte es una profecía autocumplida: todo el mundo mira las mismas EMA de 20, 50 y 200, así que las órdenes se agolpan en torno a ellas y el nivel "funciona" en parte porque está vigilado.»
  - S066 [40w] «Trátalo como una zona a vigilar, no una línea que tenga que aguantar: en un giro de verdad el precio la atraviesa de lado a lado, y la misma MM que era soporte pasa a ser resistencia en la vuelta.»
  - S075 [38w] «Sin tendencia, una MM plana queda cortada a un lado y otro, las líneas rápida y lenta se cruzan una y otra vez, y cada uno de esos cruces es una señal falsa; esto es el whipsaw (latigazo).»
  - S081 [35w] «Las acciones cierran por la noche y los fines de semana, así que una MM diaria tiene que digerir un hueco cada lunes y promedia un "cierre" que se salta la mayor parte del día.»
  - S085 [36w] «Una MM rápida sobre una altcoin volátil da latigazos constantes, generando cruces que un mercado más tranquilo nunca produciría, y una mecha de fin de semana con poca liquidez puede sacudir una EMA corta sin motivo.»
  - S087 [54w] «Una media móvil condensa los últimos N cierres en una línea que sigue al precio por detrás: una SMA pondera igual cada cierre de su ventana y da un tirón cuando el más antiguo sale, mientras que una EMA deja decaer los precios antiguos y por eso gira antes, a costa de más ruido.»
  - S088 [39w **aside-only** (23w without asides)] «Lee el régimen con tres cosas —la pendiente, dónde está el precio y el orden de una línea rápida y una lenta— y trata un cruce dorado o de la muerte como una confirmación rezagada, no como una entrada.»
- **9 Course-coined term** (3)
  - S034 ["firma" as a name for the regime's MA picture / the three cues; not standard vocabulary] «Lee la *firma* que deja cada régimen.»
  - S058 ["las tres firmas"] «Las tres firmas —orden, pendiente y dónde está el precio respecto al par— tienen el mismo aspecto en un gráfico de 1 minuto con el 9/21 que en un diario con el 50/200, y por eso este módulo enseña la imagen y no los ajustes.»
  - S062 ["las mismas tres firmas"] «Ajusta el par a tu periodo de tenencia (m23-l1, los estilos de trading) y luego léelo con las mismas tres firmas que usarías en cualquier otro sitio.»
- **10 Metaphor then gloss** (1)
  - S077 [metaphor "la misma moneda", glossed by S078 (the whipsaw version / the buying-late version); also a truncated idiom ("las dos caras de la misma moneda")] «Los dos errores clásicos son en realidad la misma moneda.»
- **11 Synonym rotation** (4)
  - S018 [MA lag: retardo (S018), retraso (S048), va por detrás (S070), rezagado (S078)] 
  - S018 [lag/noise trade-off: compromiso (S018), intercambio entre retraso y ruido (S048), cambiando lo uno por lo otro (S072)] 
  - S021 [the three regime cues: tres cosas (S021), lecturas (S030), firma (S034), imágenes (S038), firmas (S058)] 
  - S032 [price chopping across flat MAs: picoteando (S032), las sierra (S037), queda cortada a un lado y otro (S075), latigazos (S085)] 
- **A absolutes** (8)
  - S003 [siempre] «No hace nada más: no predice y, por construcción, siempre mira hacia atrás.»
  - S012 [nunca, nunca] «Los precios antiguos nunca desaparecen del todo —su peso solo decae geométricamente—, así que la EMA nunca da un tirón por una salida brusca y, como los cierres recientes dominan, gira antes.»
  - S043 [siempre] «Pero aquí está *por qué la señal siempre llega tarde*: para que una línea de 50 periodos suba por encima de una de 200, los precios recientes ya han tenido que arrastrar un promedio de 50 velas por encima de uno de 200, y eso requiere una subida sostenida que, por definición, ya tiene decenas de velas.»
  - S044 [nunca] «Ambas líneas son promedios de precios que ya ocurrieron, así que un cruce confirma un cambio que ya está en marcha: nunca canta el giro.»
  - S051 [siempre] «el par lento y más citado, y de donde les vienen el nombre al cruce dorado y al cruce de la muerte, que casi siempre se refieren a la de 50 días cruzando la de 200.»
  - S053 [debe] «Ningún mercado le debe nada a una media de 200 días, y no hay cálculo que haga la de 21 mejor que la de 19.»
  - S072 [siempre] «Siempre estás cambiando lo uno por lo otro: no hay un ajuste que sea a la vez rápido y suave.»
  - S085 [nunca] «Una MM rápida sobre una altcoin volátil da latigazos constantes, generando cruces que un mercado más tranquilo nunca produciría, y una mecha de fin de semana con poca liquidez puede sacudir una EMA corta sin motivo.»

**EN** — 36 hits, 89 sentences, density 40.4

- **1 Filler** (9)
  - S008 ["simply": intensifier on "falls off the back"] «That equal weighting has a hidden cost: when the oldest close drops out of the window, it drops out *completely*, so the line can lurch on a bar when nothing happened today — a big price from exactly N bars ago simply falls off the back.»
  - S009 [other filler: "right" in "right up until" emphatic] «A close from N bars ago has as much say as yesterday's, right up until the instant it has none.»
  - S018 [other filler: "The trade-off is the whole story:" announcer] «The trade-off is the whole story: the EMA reacts faster (less lag), but that speed also makes it noisier — it turns on moves that fizzle.»
  - S032 ["exactly": emphatic] «Price chopping across a *flat*, intertwined pair is the market telling you there is no trend to trade — which is exactly when moving averages are at their worst (below).»
  - S043 [other filler: "But here is why…" announcer] «But here is *why the signal is always late*: for a 50-period line to climb above a 200-period line, recent prices must already have dragged a 50-bar average above a 200-bar average — and that takes a sustained rally that is, by definition, already dozens of bars old.»
  - S046 ["honest": "the honest order" applied to an order of teaching] «Nothing above says what N to use, and that is the honest order — the reading comes first.»
  - S077 ["really": emphatic] «The two classic mistakes are really the same coin.»
  - S082 ["genuinely": emphatic, "averages fifty continuous days" carries it] «Crypto trades 24/7, so the price series is unbroken: an EMA50 on the daily genuinely averages fifty continuous days, with no gap-driven jumps in the line.»
  - S086 [other filler: "The practical upshot:" announcer] «The practical upshot: to get the same smoothness you would from a given period on equities, you usually need a *longer* period on crypto.»
- **4 Summary/uplift closer** (8)
  - S004 [restate: "it is an average of the past" repeats S001–S003] «Everything useful and everything dangerous about a moving average follows from that one fact: it is an average of the past.»
  - S017 [restate: re-tells the worked numbers just given] «Same data — but the EMA has admitted most of the move before the SMA is halfway there.»
  - S020 [editorial: "Faster is not better; it is a different setting on the same dial."] «Faster is not better; it is a different setting on the same dial.»
  - S038 [editorial: "…is the skill this module trains"] «Learning to recognise those three pictures at a glance is the skill this module trains.»
  - S056 [restate: repeats S054–S055] «It works while the line is crowded, not because the number is right.»
  - S072 [restate: repeats the trade-off of S071] «You are always trading one against the other: there is no setting that is both fast and smooth.»
  - S076 [restate: "a string of losses dressed up as signals" re-tells the whipsaw of S075] «A moving average earns its keep only when there is a trend for it to smooth; hand it a sideways market and it will hand you a string of losses dressed up as signals.»
  - S079 [editorial: "the line is a rear-view mirror"] «Both come from forgetting that the line is a rear-view mirror.»
- **5 Sentence over 30 words** (13)
  - S008 [45w] «That equal weighting has a hidden cost: when the oldest close drops out of the window, it drops out *completely*, so the line can lurch on a bar when nothing happened today — a big price from exactly N bars ago simply falls off the back.»
  - S015 [37w **aside-only** (27w without asides)] «The SMA10 climbs in a straight line — one old 100 is swapped for a 110 each bar — so it reads 101, 102, 103… and only reaches 110 after ten bars, when the whole window is finally 110s.»
  - S043 [47w] «But here is *why the signal is always late*: for a 50-period line to climb above a 200-period line, recent prices must already have dragged a 50-bar average above a 200-bar average — and that takes a sustained rally that is, by definition, already dozens of bars old.»
  - S054 [39w] «They matter for the same reason m13 gives for Fibonacci levels: enough people watch the same lines that resting orders pile up around them, so a level with no mechanism behind it still becomes a place where price reacts.»
  - S058 [40w **aside-only** (30w without asides)] «The three signatures — order, slope, and where price sits relative to the pair — look the same on a 1-minute chart with 9/21 as on a daily with 50/200, which is why this module teaches the picture and not the settings.»
  - S060 [32w] «A 9/21 cross on the 5-minute chart is a claim about the next hour, and it will be reversed by lunchtime often enough that a swing trader is right to ignore it.»
  - S063 [31w] «In a running trend, price often pulls back, touches a moving average, and resumes — so the MA acts like a moving floor in an uptrend or a ceiling in a downtrend.»
  - S064 [38w] «Part of this is real: the MA tracks roughly the average cost of recent buyers, so a pullback to it is a pullback to where the average holder got in, and fresh buyers tend to step in there.»
  - S066 [36w] «Treat it as a zone to watch, not a line that must hold: in a genuine reversal price cuts straight through it, and the same MA that was support becomes resistance on the way back down.»
  - S075 [31w] «With no trend, a flat MA gets sliced back and forth, the fast and slow lines cross repeatedly, and every one of those crosses is a false signal — this is whipsaw.»
  - S076 [34w] «A moving average earns its keep only when there is a trend for it to smooth; hand it a sideways market and it will hand you a string of losses dressed up as signals.»
  - S087 [48w] «A moving average collapses the last N closes into one line that trails price: an SMA weights every close in its window equally and lurches when the oldest one drops out, while an EMA lets old prices decay and so turns sooner, at the cost of more noise.»
  - S088 [35w **aside-only** (21w without asides)] «Read the regime from three things — slope, where price sits, and the order of a fast and a slow line — and treat a golden or death cross as a lagging confirmation rather than an entry.»
- **9 Course-coined term** (3)
  - S034 ["signature" as a name for the regime's MA picture / the three cues; not standard vocabulary] «Read the *signature* each regime leaves.»
  - S058 ["the three signatures"] «The three signatures — order, slope, and where price sits relative to the pair — look the same on a 1-minute chart with 9/21 as on a daily with 50/200, which is why this module teaches the picture and not the settings.»
  - S062 ["the same three signatures"] «Match the pair to your holding period (m23-l1, trading styles), then read it with the same three signatures you would use anywhere.»
- **10 Metaphor then gloss** (1)
  - S077 [metaphor "the same coin", glossed by S078; truncated idiom ("two sides of the same coin")] «The two classic mistakes are really the same coin.»
- **11 Synonym rotation** (2)
  - S021 [the three regime cues: three things (S021), reads (S030), signature (S034), pictures (S038), signatures (S058)] 
  - S032 [price chopping across flat MAs: chopping (S032), saws (S037), gets sliced back and forth (S075), whips (S085)] 
- **A absolutes** (8)
  - S003 [always] «It does nothing else — it does not predict, and by construction it always looks backwards.»
  - S012 [never, never] «Old prices never leave entirely — their weight just decays geometrically — so the EMA never lurches from a drop-off, and because recent bars dominate, it turns sooner.»
  - S043 [always, must] «But here is *why the signal is always late*: for a 50-period line to climb above a 200-period line, recent prices must already have dragged a 50-bar average above a 200-bar average — and that takes a sustained rally that is, by definition, already dozens of bars old.»
  - S044 [never] «Both lines are averages of prices that have already happened, so a cross confirms a change that is already underway — it never calls the turn.»
  - S051 [always] «the slow, most-quoted pair, and where the golden cross and death cross got their names: those two terms almost always mean the 50-day crossing the 200-day.»
  - S066 [must] «Treat it as a zone to watch, not a line that must hold: in a genuine reversal price cuts straight through it, and the same MA that was support becomes resistance on the way back down.»
  - S072 [always] «You are always trading one against the other: there is no setting that is both fast and smooth.»
  - S085 [never] «A fast MA on a volatile alt whips constantly, throwing crosses that a calmer market would never produce, and a weekend low-liquidity wick can jerk a short EMA on nothing.»

### m11-l1

**ES** — 79 hits, 118 sentences, density 66.9

- **1 Filler** (21)
  - S004 ["exactamente": emphatic ("una vez que sabes qué calculan")] «Ambos son genuinamente útiles una vez que sabes exactamente qué calculan, y ambos se malinterpretan sin parar por quienes los tratan como botones de compra y venta.»
  - S004 [other filler: "genuinamente" in "genuinamente útiles"] «Ambos son genuinamente útiles una vez que sabes exactamente qué calculan, y ambos se malinterpretan sin parar por quienes los tratan como botones de compra y venta.»
  - S014 ["Fíjate en lo que…": announcer] «Fíjate en lo que ese número *no* dice: nada sobre si un 0,9 % es un movimiento grande, nada sobre que el precio esté alto o bajo en términos absolutos, solo que la acción reciente se ha inclinado al alza 3 a 1.»
  - S015 [other filler: "justo" in "son justo donde" emphatic] «Las bandas convencionales son por encima de 70 = sobrecompra y por debajo de 30 = sobreventa, pero sigue leyendo, porque esas dos palabras son justo donde la mayoría de los principiantes pierde dinero.»
  - S021 ["sencillamente": intensifier] «Es, sencillamente, la *distancia* entre las dos líneas.»
  - S025 ["exactamente": emphatic] «Eso es exactamente lo que significa "momentum" aquí.»
  - S036 ["precisamente": emphatic before "porque"] «Como la línea de señal no es más que una media rezagada de la línea MACD, este cruce tiene un significado puramente mecánico: la línea MACD cruzó por encima de su señal precisamente porque la línea MACD giró al alza, y cruzó por debajo porque giró a la baja.»
  - S037 ["nada más": tag] «Es una afirmación sobre *las últimas velas de momentum*, nada más.»
  - S046 ["Fíjate en el número…": announcer] «Fíjate en el número que no se movió: la línea MACD se mantuvo positiva todo el tiempo (+360 y luego +410).»
  - S050 ["sin más": tag after "ha cruzado a la de 26"] «La línea MACD *es* la EMA rápida menos la lenta, así que la línea MACD en cero significa que esas dos medias son iguales, y que la línea MACD cruce el cero significa que la EMA de 12 ha cruzado a la de 26 sin más.»
  - S076 [other filler: "y ahí está la clave" tag] «Fíjate en el panel izquierdo: esto ocurre varias veces dentro de una misma tendencia sin que la tendencia esté nunca en duda, y ahí está la clave.»
  - S080 ["exactamente": emphatic before a cross-reference] «Esta es exactamente la advertencia de m10 sobre los cruces de medias en un rango, y no podría ser de otro modo: el MACD *son* dos medias móviles.»
  - S084 [other filler: "Aquí está el malentendido más caro de este módulo." announcer sentence] «Aquí está el malentendido más caro de este módulo.»
  - S088 ["exactamente": emphatic ("es esta trampa")] «El gráfico de arriba es exactamente esta trampa: el RSI salta por encima de 70 cerca del *inicio* del movimiento y sencillamente se queda ahí, imprimiendo una lectura de sobrecompra tras otra mientras el precio sube todo el tiempo.»
  - S088 ["sencillamente": intensifier on "se queda ahí"] «El gráfico de arriba es exactamente esta trampa: el RSI salta por encima de 70 cerca del *inicio* del movimiento y sencillamente se queda ahí, imprimiendo una lectura de sobrecompra tras otra mientras el precio sube todo el tiempo.»
  - S089 [other filler: "justo" in "es justo lo que cabría esperar" emphatic] «Sobrecompra no significa caro y no significa vender: significa que el momentum ha sido fuertemente unilateral, que en una tendencia es justo lo que cabría esperar y a menudo una señal de *fuerza*, no de agotamiento.»
  - S098 ["simplemente": intensifier] «El reflejo funciona al revés igual de caro: ponerte corto contra una tendencia bajista fuerte porque "el RSI está en sobreventa" simplemente le regala tu stop a la tendencia.»
  - S099 ["fíjate": announcer; the whole sentence announces S100] «Y fíjate exactamente en lo que el indicador hizo y no hizo aquí.»
  - S099 ["exactamente": emphatic] «Y fíjate exactamente en lo que el indicador hizo y no hizo aquí.»
  - S105 [other filler: "justo" in "justo las condiciones que atrapan" emphatic] «En un alt de baja capitalización, una cantidad modesta de compra mueve el precio mucho, así que un tirón impulsado por la narrativa puede mantener el RSI en un extremo mucho más arriba y mucho más tiempo que cualquier gran capitalización: justo las condiciones que atrapan el reflejo de "vender la sobrecompra".»
  - S106 ["de verdad": emphatic ("Cuando quieras saber…")] «Cuando de verdad quieras saber si una subida se está recalentando, mira el funding antes que el RSI: en estas carreras eufóricas el funding se vuelve marcadamente positivo (los largos pagan a los cortos para mantener la posición abierta), y *ese* apiñamiento sí es una señal real de una operación tensada, cosa que "el RSI está en 82" no es.»
- **2 Rhythmic triad** (2)
  - S059 ["Es frecuente, salta a menudo y puede ocurrir muchas veces…": all three say "often"; keep one ("salta a menudo dentro de una misma tendencia…")] «Es frecuente, salta a menudo y puede ocurrir muchas veces dentro de una misma tendencia sin que la tendencia esté nunca en duda.»
  - S061 ["más raro, más tardío y hace falta un movimiento sostenido": built to mirror S059; "raro" overlaps "hace falta un movimiento sostenido"; drop "más raro"] «Es más raro, más tardío y hace falta un movimiento sostenido para producirlo: el mismo retraso que m10 mostraba para cualquier cruce de medias.»
- **3 Rhetorical question** (1)
  - S022 «¿Por qué una *diferencia de medias* es una lectura de momentum?»
- **4 Summary/uplift closer** (13)
  - S004 [editorial: "ambos son genuinamente útiles… y ambos se malinterpretan" closes the intro with a verdict] «Ambos son genuinamente útiles una vez que sabes exactamente qué calculan, y ambos se malinterpretan sin parar por quienes los tratan como botones de compra y venta.»
  - S025 [editorial: "Eso es exactamente lo que significa momentum aquí."] «Eso es exactamente lo que significa "momentum" aquí.»
  - S031 [restate: repeats the growing/shrinking histogram of S028–S029] «Un histograma que *crece* indica que el movimiento se acelera; uno que *se encoge* indica que pierde fuerza aunque el precio todavía suba.»
  - S034 [editorial: "No son noticias del mismo tamaño."] «No son noticias del mismo tamaño.»
  - S037 [restate: repeats S036's "purely mechanical" meaning] «Es una afirmación sobre *las últimas velas de momentum*, nada más.»
  - S048 [restate: repeats S046–S047 (trend unchanged)] «Nada cambió en la tendencia: solo se tambaleó y se recuperó el empuje de corto plazo dentro de ella.»
  - S056 [restate: S055 already said the 12-bar average is above the 26] «La tendencia de corto plazo se ha impuesto a la de largo.»
  - S072 [editorial: "No es una orden de venta." (refrain repeated at S111)] «No es una orden de venta.»
  - S083 [restate: confirmation in trend vs noise in range, already said in S075–S080] «Un cruce que coincide con una tendencia que ya habías identificado es confirmación; el mismo cruce en un rango es ruido con forma.»
  - S087 [restate: repeats S086 (RSI stays above 70)] «Cada vela que "debería" haber sido el giro fue solo otro tramo al alza.»
  - S097 [editorial: "La tendencia no pagó ninguna."] «La tendencia no pagó ninguna.»
  - S102 [restate: repeats S100 (never says the move is about to end)] «Solo que jamás dijo que estuviera *acabado*.»
  - S115 [restate: lesson's last prose unit; repeats S114 (confirmation of a level you already have)] «Un oscilador que coincide con un nivel que ya vigilabas vale mucho más que uno que grita en espacio abierto.»
- **5 Sentence over 30 words** (34)
  - S001 [37w] «Un oscilador es un indicador, derivado del precio, que se mueve dentro de un rango acotado e intenta describir el *momentum*: con qué rapidez y con cuánta unilateralidad se ha movido el precio últimamente, no dónde está.»
  - S002 [40w **aside-only** (26w without asides)] «Como el rango es fijo (de 0 a 100 en el RSI, una línea de cero en el MACD), puedes comparar la lectura de hoy con la del mes pasado en la misma escala, y ahí está todo su atractivo.»
  - S005 [42w] «El RSI (Índice de Fuerza Relativa) compara el tamaño medio de las subidas recientes con el tamaño medio de las bajadas recientes, sobre un periodo de referencia (por defecto 14 velas), y comprime el resultado en una escala de 0 a 100.»
  - S010 [35w] «Así que el RSI es una medida *relativa*, y está acotada por una razón mecánica: el RS puede ir de 0 a infinito, y la proyección `100 − 100 ÷ (1 + RS)` pliega todo ese rango limpiamente en el 0–100.»
  - S014 [42w] «Fíjate en lo que ese número *no* dice: nada sobre si un 0,9 % es un movimiento grande, nada sobre que el precio esté alto o bajo en términos absolutos, solo que la acción reciente se ha inclinado al alza 3 a 1.»
  - S015 [32w] «Las bandas convencionales son por encima de 70 = sobrecompra y por debajo de 30 = sobreventa, pero sigue leyendo, porque esas dos palabras son justo donde la mayoría de los principiantes pierde dinero.»
  - S026 [37w] «Una lectura resuelta: en una subida, la EMA de 12 está en 30.500 y la de 26 en 30.000, así que la línea MACD vale +500: el precio está muy por encima de su base más lenta.»
  - S029 [38w] «Si en cambio la línea MACD se estanca en +500 mientras la señal la alcanza en +480, el histograma *se encoge* a +20: el precio puede seguir cerca de sus máximos, pero la fuerza detrás se está apagando.»
  - S036 [49w] «Como la línea de señal no es más que una media rezagada de la línea MACD, este cruce tiene un significado puramente mecánico: la línea MACD cruzó por encima de su señal precisamente porque la línea MACD giró al alza, y cruzó por debajo porque giró a la baja.»
  - S040 [35w **aside-only** (18w without asides)] «La línea de señal —la EMA de 9 de la línea MACD, que todavía promedia las lecturas mayores de la subida— está más arriba, en +392, con lo que el histograma es 360 − 392 = −32.»
  - S042 [31w] «Dos velas después el precio se reanuda: la EMA de 12 salta a 30.430 mientras la de 26 solo ha subido a 30.020, así que la línea MACD vuelve a +410.»
  - S050 [46w] «La línea MACD *es* la EMA rápida menos la lenta, así que la línea MACD en cero significa que esas dos medias son iguales, y que la línea MACD cruce el cero significa que la EMA de 12 ha cruzado a la de 26 sin más.»
  - S051 [33w **aside-only** (29w without asides)] «Ese es el cruce dorado (o de la muerte) de m10, sobre el par 12/26, reportado en el panel del oscilador: un cambio de *régimen* de tendencia, no un bache dentro de una.»
  - S052 [37w] «Una lectura resuelta: una tendencia bajista tiene la EMA de 12 en 29.400 y la de 26 en 29.900, así que la línea MACD marca −500: la media reciente está decididamente por debajo de la más antigua.»
  - S054 [31w] «La EMA de 12, ponderada hacia los precios nuevos, escala más rápido: en 29.850 frente a una EMA de 26 que solo ha llegado a 29.700, la línea MACD vale +150.»
  - S055 [33w] «Cruzó el cero por el camino, y lo que ese cruce registra es que el precio medio de las últimas 12 velas está ahora *por encima* de la media de las últimas 26.»
  - S066 [35w] «El histograma es la *distancia* entre las dos líneas, así que un histograma que se encoge es el cruce acercándose: que el histograma llegue a cero y que el cruce ocurra son el mismo evento.»
  - S069 [43w] «El precio puede seguir raspando nuevos máximos todo ese tiempo, pero las barras que hay detrás son cada vez más cortas, y si la línea MACD se queda plana mientras la señal sigue subiendo, el próximo cambio de signo es aritmética, no opinión.»
  - S070 [48w] «Que el precio haga nuevos máximos mientras el histograma los hace más pequeños es una divergencia del histograma del MACD: el mismo desacuerdo entre precio y momentum sobre el que se construye m12, captado un paso antes, en el histograma en lugar de en los máximos del precio.»
  - S075 [47w] «El mismo cruce alcista de la línea de señal dentro de una tendencia alcista establecida es indicio de *continuación*: un retroceso puso el histograma en negativo, ese retroceso ya ha terminado, la tendencia que estuvo intacta todo el tiempo se reanuda, y el cruce te dice cuándo.»
  - S079 [38w] «En un mercado lateral la línea MACD oscila a un lado y otro del cero, así que los cruces saltan una y otra vez, cada uno exactamente igual al de la izquierda, y ninguno lleva a ninguna parte.»
  - S088 [39w] «El gráfico de arriba es exactamente esta trampa: el RSI salta por encima de 70 cerca del *inicio* del movimiento y sencillamente se queda ahí, imprimiendo una lectura de sobrecompra tras otra mientras el precio sube todo el tiempo.»
  - S089 [36w] «Sobrecompra no significa caro y no significa vender: significa que el momentum ha sido fuertemente unilateral, que en una tendencia es justo lo que cabría esperar y a menudo una señal de *fuerza*, no de agotamiento.»
  - S094 [35w] «Un alt de baja capitalización se dispara de 1,00 a 1,60 en dos semanas; el RSI cruza el 70 hacia 1,15 y no vuelve a mirar atrás, quedándose entre 78 y 85 toda la subida.»
  - S095 [54w] «Un principiante que sigue la regla se pone corto en 1,20 ("está en sobrecompra") y le salta el stop en 1,28; se pone corto otra vez en 1,35 y salta en 1,44; se pone corto una tercera vez en 1,50 con más tamaño para "recuperar", y el empujón hasta 1,60 se lleva la cuenta.»
  - S104 [49w] «Una acción tiene un cierre diario y un hueco nocturno que dejan enfriarse el momentum; un perpetuo de cripto cotiza cada hora de cada día, así que un movimiento parabólico puede mantener el RSI por encima de 80 una semana entera sin ninguna pausa de sesión que lo interrumpa.»
  - S105 [52w] «En un alt de baja capitalización, una cantidad modesta de compra mueve el precio mucho, así que un tirón impulsado por la narrativa puede mantener el RSI en un extremo mucho más arriba y mucho más tiempo que cualquier gran capitalización: justo las condiciones que atrapan el reflejo de "vender la sobrecompra".»
  - S106 [60w] «Cuando de verdad quieras saber si una subida se está recalentando, mira el funding antes que el RSI: en estas carreras eufóricas el funding se vuelve marcadamente positivo (los largos pagan a los cortos para mantener la posición abierta), y *ese* apiñamiento sí es una señal real de una operación tensada, cosa que "el RSI está en 82" no es.»
  - S107 [35w] «El mismo libro poco profundo que dejó levitar al precio hace brutal la caída posterior, así que quien tuvo "razón" sobre la sobrecompra una semana demasiado pronto rara vez sigue solvente para disfrutar de tenerla.»
  - S110 [37w] «Vigila el histograma del MACD en busca de cambios de momentum: un histograma que se encoge avisa de que un movimiento se desacelera antes de que el precio gire, y te avisa de que viene un cruce.»
  - S112 [35w] «Un cruce de la línea de señal es un bache de momentum; un cruce de la línea de cero es la EMA de 12 y la de 26 cambiando de orden, un cambio de régimen.»
  - S116 [43w] «El RSI compara el tamaño medio de las subidas recientes con el de las bajadas y pliega el cociente en una escala de 0 a 100, así que mide cuán desequilibradas han sido las últimas 14 velas, no si el precio está alto.»
  - S117 [52w] «El MACD es la distancia entre una EMA rápida y una lenta más una línea de señal y un histograma, y sus dos cruces son noticias distintas: el de la línea de señal es un bache de momentum, el de la línea de cero es que las dos EMAs cambian de orden.»
  - S118 [39w **aside-only** (25w without asides)] «La lectura cara es "sobrecompra = vender" —en una tendencia fuerte el RSI se queda clavado en su extremo durante semanas—, así que lee un oscilador como contexto que confirma un nivel que ya tenías, nunca como un disparador autónomo.»
- **9 Course-coined term** (4)
  - S051 ["bache" as the name for a signal-line cross ("no un bache dentro de una")] «Ese es el cruce dorado (o de la muerte) de m10, sobre el par 12/26, reportado en el panel del oscilador: un cambio de *régimen* de tendencia, no un bache dentro de una.»
  - S112 ["bache de momentum"] «Un cruce de la línea de señal es un bache de momentum; un cruce de la línea de cero es la EMA de 12 y la de 26 cambiando de orden, un cambio de régimen.»
  - S115 ["espacio abierto" = away from any level (same term as m08-l2)] «Un oscilador que coincide con un nivel que ya vigilabas vale mucho más que uno que grita en espacio abierto.»
  - S117 ["bache de momentum"] «El MACD es la distancia entre una EMA rápida y una lenta más una línea de señal y un histograma, y sus dos cruces son noticias distintas: el de la línea de señal es un bache de momentum, el de la línea de cero es que las dos EMAs cambian de orden.»
- **11 Synonym rotation** (4)
  - S001 [one-sided momentum: unilateralidad (S001), desequilibradas (S011), se ha inclinado (S014), desigual (S101)] 
  - S007 [RSI stuck at an extreme: se clava (S007), se queda ahí (S088), aparca (S090), mantener (S104), clavado (S118)] 
  - S029 [momentum fading: la fuerza se está apagando (S029), pierde fuerza (S031), se desacelera (S071, S110)] 
  - S064 [a non-binding hint: pista (S064, S071, S111), indicio (S075), señal de fuerza (S089)] 
- **A absolutes** (10)
  - S047 [nunca] «La EMA de 12 nunca cayó por debajo de la de 26.»
  - S059 [nunca] «Es frecuente, salta a menudo y puede ocurrir muchas veces dentro de una misma tendencia sin que la tendencia esté nunca en duda.»
  - S062 [nunca] «Confirma un régimen que ya está en marcha; nunca canta el giro.»
  - S076 [nunca] «Fíjate en el panel izquierdo: esto ocurre varias veces dentro de una misma tendencia sin que la tendencia esté nunca en duda, y ahí está la clave.»
  - S087 [debería] «Cada vela que "debería" haber sido el giro fue solo otro tramo al alza.»
  - S091 [debería] «"El RSI está por encima de 70, así que debería vender".»
  - S100 [nunca] «Una lectura extrema te dice que el movimiento es unilateral; nunca te dice que esté a punto de terminar.»
  - S101 [nunca] «La lectura nunca estuvo *equivocada*: decía con verdad que el movimiento era desigual.»
  - S114 [nunca] «Trata los cruces y los cruces de banda como *confirmación de una tesis que ya tienes* a partir de la estructura y los niveles, nunca como señales autónomas.»
  - S118 [nunca, summary] «La lectura cara es "sobrecompra = vender" —en una tendencia fuerte el RSI se queda clavado en su extremo durante semanas—, así que lee un oscilador como contexto que confirma un nivel que ya tenías, nunca como un disparador autónomo.»

**EN** — 67 hits, 118 sentences, density 56.8

- **1 Filler** (22)
  - S004 ["genuinely": intensifier] «Both are genuinely useful once you know exactly what they compute, and both are misread constantly by people who treat them as buy and sell buttons.»
  - S004 ["exactly": emphatic] «Both are genuinely useful once you know exactly what they compute, and both are misread constantly by people who treat them as buy and sell buttons.»
  - S014 [other filler: "Notice what…" announcer] «Notice what that number does *not* say: nothing about whether 0.9% is a big move, nothing about price being high or low in absolute terms — only that recent action has leaned up by 3-to-1.»
  - S015 ["exactly": emphatic] «The conventional bands are above 70 = overbought and below 30 = oversold, but read on, because those two words are exactly where most beginners lose money.»
  - S021 ["simply": intensifier] «It is simply the *gap* between the two lines.»
  - S025 ["exactly": emphatic] «That is exactly what "momentum" means here.»
  - S036 ["precisely": emphatic before "because"] «Because the signal line is just a lagging average of the MACD line, this cross has a purely mechanical meaning: the MACD line crossed above its signal precisely because the MACD line turned up, and crossed below because it turned down.»
  - S037 ["nothing more": tag] «It is a statement about the *last few bars of momentum*, nothing more.»
  - S046 [other filler: "Notice the number…" announcer] «Notice the number that never moved: the MACD line stayed positive the whole time (+360, then +410).»
  - S076 [other filler: "which is the point" tag] «Note on the left panel that this happens several times in one trend without the trend ever being in doubt — which is the point.»
  - S080 ["precisely": emphatic before a cross-reference] «This is precisely m10's whipsaw warning about MA crosses in a range — of course it is, since the MACD *is* two moving averages.»
  - S080 ["of course": tag ("of course it is")] «This is precisely m10's whipsaw warning about MA crosses in a range — of course it is, since the MACD *is* two moving averages.»
  - S084 [other filler: "Here is the single most expensive misunderstanding in this module." announcer sentence] «Here is the single most expensive misunderstanding in this module.»
  - S088 ["precisely": emphatic] «The chart above is precisely this trap: RSI vaults above 70 near the *start* of the move and simply stays there, printing overbought reading after overbought reading while price climbs the entire time.»
  - S088 ["simply": intensifier on "stays there"] «The chart above is precisely this trap: RSI vaults above 70 near the *start* of the move and simply stays there, printing overbought reading after overbought reading while price climbs the entire time.»
  - S089 ["exactly": emphatic] «Overbought does not mean expensive and it does not mean sell — it means momentum has been strongly one-sided, which in a trend is exactly what you would expect, and is often a sign of *strength*, not exhaustion.»
  - S098 ["simply": intensifier] «The reflex runs in reverse just as expensively — shorting into a strong downtrend because "RSI is oversold" simply hands your stop to the trend.»
  - S099 ["precisely": emphatic; the whole sentence announces S100] «And notice precisely what the indicator did and did not do here.»
  - S099 [other filler: "notice" announcer] «And notice precisely what the indicator did and did not do here.»
  - S105 [other filler: "exact" in "the exact conditions" emphatic] «In a low-cap alt, a modest amount of buying moves price a long way, so a narrative-driven rip can keep RSI at an extreme far higher and far longer than any large-cap would — the exact conditions that trap the "sell the overbought" reflex.»
  - S106 ["genuinely": emphatic] «When you genuinely want to know whether an up-move is overheating, watch funding rather than RSI: in these euphoric runs funding turns sharply positive (longs paying shorts to keep the position open), and *that* crowding is a real sign of a stretched trade in a way that "RSI is 82" simply is not.»
  - S106 ["simply": intensifier ("simply is not")] «When you genuinely want to know whether an up-move is overheating, watch funding rather than RSI: in these euphoric runs funding turns sharply positive (longs paying shorts to keep the position open), and *that* crowding is a real sign of a stretched trade in a way that "RSI is 82" simply is not.»
- **2 Rhythmic triad** (2)
  - S059 ["Common, fires often, and can happen many times…": all three say "often"; keep one] «Common, fires often, and can happen many times inside one trend without the trend ever being in question.»
  - S061 ["Rarer, later, and it takes a sustained move": built to mirror S059; "rarer" overlaps "takes a sustained move"; drop "rarer"] «Rarer, later, and it takes a sustained move to produce — the same lag m10 showed for any MA cross.»
- **3 Rhetorical question** (1)
  - S022 «Why is a *difference of averages* a momentum read at all?»
- **4 Summary/uplift closer** (13)
  - S004 [editorial: closes the intro with a verdict on both indicators] «Both are genuinely useful once you know exactly what they compute, and both are misread constantly by people who treat them as buy and sell buttons.»
  - S025 [editorial: "That is exactly what momentum means here."] «That is exactly what "momentum" means here.»
  - S031 [restate: repeats the growing/shrinking histogram of S028–S029] «A histogram that is *growing* means the move is accelerating; a *shrinking* histogram means it is losing steam even while price is still rising.»
  - S034 [editorial: "They are not the same size of news."] «They are not the same size of news.»
  - S037 [restate: repeats S036's "purely mechanical" meaning] «It is a statement about the *last few bars of momentum*, nothing more.»
  - S048 [restate: repeats S046–S047] «Nothing about the trend changed — only the short-term push inside it wobbled and recovered.»
  - S056 [restate: S055 already said the 12-bar average is above the 26] «The short-term trend has taken over the longer-term one.»
  - S072 [editorial: "It is not a command to sell." (refrain repeated at S111)] «It is not a command to sell.»
  - S083 [restate: confirmation in trend vs noise in range, already said in S075–S080] «A cross that agrees with a trend you had already identified is confirmation; the identical cross in a range is noise with a shape.»
  - S087 [restate: repeats S086] «Every bar that "should" have been the reversal was just another leg up.»
  - S097 [editorial: "The trend paid none of them."] «The trend paid none of them.»
  - S102 [restate: repeats S100] «It just never said the move was *done*.»
  - S115 [restate: lesson's last prose unit; repeats S114] «An oscillator that agrees with a level you were already watching is worth far more than one shouting in open space.»
- **5 Sentence over 30 words** (21)
  - S001 [33w] «An oscillator is an indicator, derived from price, that moves within a bounded range and tries to describe *momentum* — how fast and how one-sidedly price has been moving lately, not where it sits.»
  - S005 [37w **aside-only** (29w without asides)] «RSI (Relative Strength Index) compares the average size of recent *up* moves to the average size of recent *down* moves, over a lookback period (the default is 14 bars), and squeezes the result onto a 0–100 scale.»
  - S010 [32w] «So RSI is a *relative* measure, and it is bounded for a mechanical reason: RS can range from 0 to infinity, and the `100 − 100 ÷ (1 + RS)` mapping folds that whole range neatly into 0–100.»
  - S014 [34w] «Notice what that number does *not* say: nothing about whether 0.9% is a big move, nothing about price being high or low in absolute terms — only that recent action has leaned up by 3-to-1.»
  - S029 [34w] «If instead the MACD line stalls at +500 while the signal catches up to +480, the histogram *shrinks* to +20 — price may still be near its highs, but the push behind it is fading.»
  - S036 [41w] «Because the signal line is just a lagging average of the MACD line, this cross has a purely mechanical meaning: the MACD line crossed above its signal precisely because the MACD line turned up, and crossed below because it turned down.»
  - S050 [37w] «The MACD line *is* the fast EMA minus the slow EMA, so the MACD line at zero means those two averages are equal, and the MACD line crossing zero means the 12-EMA has crossed the 26-EMA outright.»
  - S069 [38w] «Price may still be grinding to new highs the whole time — but the bars behind it are getting shorter, and if the MACD line stays flat while the signal keeps climbing, the next flip is arithmetic, not opinion.»
  - S070 [37w] «Price making new highs while the histogram makes smaller ones is a MACD-histogram divergence — the same disagreement between price and momentum that m12 builds on, caught one step earlier, at the histogram rather than the swing highs.»
  - S075 [39w] «The same bullish signal-line cross inside an established uptrend is *continuation* evidence: a pullback turned the histogram negative, that pullback is now over, the trend that was intact the whole time is resuming, and the cross tells you when.»
  - S079 [35w] «In a sideways market the MACD line saws back and forth across zero, so crosses fire again and again, each one looking exactly like the one on the left, and none of them leads anywhere.»
  - S088 [33w] «The chart above is precisely this trap: RSI vaults above 70 near the *start* of the move and simply stays there, printing overbought reading after overbought reading while price climbs the entire time.»
  - S089 [37w] «Overbought does not mean expensive and it does not mean sell — it means momentum has been strongly one-sided, which in a trend is exactly what you would expect, and is often a sign of *strength*, not exhaustion.»
  - S095 [44w] «A beginner following the rule shorts at 1.20 ("it's overbought"), gets stopped out at 1.28; shorts again at 1.35, stopped at 1.44; shorts a third time at 1.50 with a bigger size to "make it back", and the push to 1.60 takes the account.»
  - S104 [44w] «A stock gets a daily close and an overnight gap that let momentum cool off; a crypto perpetual trades every hour of every day, so a parabolic move can hold RSI above 80 for a week straight with no session break to interrupt it.»
  - S105 [43w] «In a low-cap alt, a modest amount of buying moves price a long way, so a narrative-driven rip can keep RSI at an extreme far higher and far longer than any large-cap would — the exact conditions that trap the "sell the overbought" reflex.»
  - S106 [53w] «When you genuinely want to know whether an up-move is overheating, watch funding rather than RSI: in these euphoric runs funding turns sharply positive (longs paying shorts to keep the position open), and *that* crowding is a real sign of a stretched trade in a way that "RSI is 82" simply is not.»
  - S107 [33w] «The same thin book that let price levitate makes the eventual drop brutal — so the trader who was "right" about overbought a week too early is rarely still solvent to enjoy being right.»
  - S116 [37w] «RSI compares the average size of recent up moves with recent down moves and folds the ratio onto a 0–100 scale, so it measures how lopsided the last 14 bars have been, not whether price is high.»
  - S117 [41w] «MACD is the gap between a fast and a slow EMA plus a signal line and a histogram, and its two crosses are different news: a signal-line cross is a momentum wobble, a zero-line cross is the two EMAs changing order.»
  - S118 [36w **aside-only** (24w without asides)] «The expensive misreading is "overbought = sell" — in a strong trend RSI stays pinned at its extreme for weeks — so read an oscillator as context that confirms a level you already had, never as a standalone trigger.»
- **9 Course-coined term** (4)
  - S051 ["wobble" as the name for a signal-line cross ("not a wobble within one")] «That is m10's golden cross (or death cross), on the 12/26 pair, reported in the oscillator pane: a change of trend *regime*, not a wobble within one.»
  - S112 ["momentum wobble"] «A signal-line cross is a momentum wobble; a zero-line cross is the 12- and 26-EMA changing order, a regime change.»
  - S115 ["open space" = away from any level (same term as m08-l2)] «An oscillator that agrees with a level you were already watching is worth far more than one shouting in open space.»
  - S117 ["momentum wobble"] «MACD is the gap between a fast and a slow EMA plus a signal line and a histogram, and its two crosses are different news: a signal-line cross is a momentum wobble, a zero-line cross is the two EMAs changing order.»
- **11 Synonym rotation** (4)
  - S001 [one-sided momentum: one-sidedly (S001), lopsided (S011, S101), leaned up (S014), one-sided (S089, S100)] 
  - S007 [RSI stuck at an extreme: pins (S007), stays there (S088), parks (S090), hold (S104), stays pinned (S118)] 
  - S029 [momentum fading: the push is fading (S029), losing steam (S031), decelerating (S071, S110)] 
  - S064 [a non-binding hint: clue (S064, S071, S111), evidence (S075), sign (S089, S106)] 
- **A absolutes** (9)
  - S046 [never] «Notice the number that never moved: the MACD line stayed positive the whole time (+360, then +410).»
  - S047 [never] «The 12-EMA never fell below the 26-EMA.»
  - S062 [never] «It confirms a regime that is already underway; it never calls the turn.»
  - S094 [never] «A low-cap alt rips from 1.00 to 1.60 in two weeks; RSI crosses 70 at around 1.15 and never looks back, sitting between 78 and 85 the whole climb.»
  - S100 [never] «An extreme reading tells you the move is one-sided; it never tells you the move is about to end.»
  - S101 [never] «The reading was never *wrong*: it truthfully said the move was lopsided.»
  - S102 [never] «It just never said the move was *done*.»
  - S114 [never] «Treat crosses and band-crossings as *confirmation for a thesis you already hold* from structure and levels, never as standalone signals.»
  - S118 [never, summary] «The expensive misreading is "overbought = sell" — in a strong trend RSI stays pinned at its extreme for weeks — so read an oscillator as context that confirms a level you already had, never as a standalone trigger.»

### m12-l1

**ES** — 34 hits, 69 sentences, density 49.3

- **1 Filler** (6)
  - S004 ["en realidad": emphatic] «Toda la lección trata en realidad de una sola habilidad: saber cuánto vale esa pista y cuándo no vale nada.»
  - S038 [other filler: "El truco para no liarse:" announcer] «El truco para no liarse: la divergencia regular compara los extremos y espera un giro; la oculta aparece en el retroceso y espera que la tendencia se reanude.»
  - S046 ["sencillamente": intensifier ("y no lo está")] «El momentum "debería" estar agotado y sencillamente no lo está: una tendencia decidida sigue atrayendo compradores nuevos más rápido de lo que se cansan los viejos.»
  - S053 [other filler: "La diferencia concreta:" announcer] «La diferencia concreta: una divergencia bajista que aparece justo cuando el precio toca el máximo exacto que frenó las tres últimas subidas es una señal; la divergencia idéntica a medio camino entre niveles, en espacio abierto, es ruido disfrazado de señal.»
  - S064 [other filler: "Lo más importante:" announcer] «Lo más importante: los movimientos parabólicos del cripto son el cementerio de quienes operan divergencias.»
  - S066 [other filler: "justo" in "puede financiar justo esto" emphatic] «Un funding persistente puede financiar justo esto: mientras los largos estén dispuestos a seguir pagando por mantener la posición, la tendencia puede desafiar a un momentum "agotado" mucho más tiempo del que la cuenta de un principiante puede aguantar en corto en contra.»
- **4 Summary/uplift closer** (9)
  - S004 [editorial: "Toda la lección trata… de una sola habilidad"] «Toda la lección trata en realidad de una sola habilidad: saber cuánto vale esa pista y cuándo no vale nada.»
  - S007 [restate: repeats the definition of S001] «Cuando esas dos historias dejan de coincidir, estás ante una divergencia.»
  - S015 [restate: repeats S014 (fewer, tired participants → trend running out of buyers)] «Una tendencia que ya no puede hacer nuevos máximos *con convicción* es una tendencia a punto de quedarse sin compradores.»
  - S023 [restate: "más bajo en precio pero más alto en momentum" repeats S022's numbers] «El nuevo mínimo es *más bajo en precio pero más alto en momentum*: los vendedores llegaron más lejos y sacaron menos de ello.»
  - S031 [editorial: "es el motivo… no una advertencia en su contra" re-tells S030] «El oscilador de aspecto aterrador es el *motivo* por el que la tendencia puede continuar, no una advertencia en su contra.»
  - S037 [restate: repeats S036] «El rebote parece fuerte en el oscilador, pero la estructura nunca dejó de caer.»
  - S044 [editorial: "Ese margen de adelanto es toda la ventaja que ofrece una divergencia."] «Ese margen de adelanto es toda la ventaja que ofrece una divergencia.»
  - S048 [restate: repeats S047 (a statement about momentum, not a dated top)] «La costumbre más cara de todo este tema es tratar "el momentum se está apagando" como "ya está el techo".»
  - S054 [restate: repeats S053 (same reading, different value; the level does the work)] «La misma lectura del oscilador, un valor completamente distinto, porque el trabajo lo hace el nivel, no el oscilador.»
- **5 Sentence over 30 words** (10)
  - S030 [34w] «Cuando el oscilador se hunde a un mínimo más bajo pero el precio aguanta un mínimo más alto, el mercado ha sacudido a las manos débiles y ha recargado: la caída cumplió su función.»
  - S033 [33w **aside-only** (26w without asides)] «El precio aguanta un mínimo más alto en 28.250 (el mínimo del swing anterior fue 26.900), pero el RSI se hunde hasta 28, por debajo del 38 que marcó en el mínimo anterior.»
  - S041 [39w] «En un punto de giro auténtico, el último empujón a un nuevo extremo casi siempre lo hace menos gente: los compradores ansiosos ya están dentro, así que el tramo final es más lento aunque el precio todavía marque máximos.»
  - S053 [41w] «La diferencia concreta: una divergencia bajista que aparece justo cuando el precio toca el máximo exacto que frenó las tres últimas subidas es una señal; la divergencia idéntica a medio camino entre niveles, en espacio abierto, es ruido disfrazado de señal.»
  - S062 [42w] «Los mercados funcionan 24/7, así que las divergencias se forman en velas de fin de semana y de madrugada que son finas y fáciles de malinterpretar: una "divergencia" con poco volumen de sábado suele evaporarse cuando la liquidez real vuelve el lunes.»
  - S063 [38w] «En libros de alts poco profundos, un puñado de órdenes puede llevar el precio a un máximo nuevo mientras el oscilador apenas se mueve, fabricando divergencias que reflejan un libro tranquilo y no una convicción que se apaga.»
  - S065 [33w] «Una moneda en plena manía puede mostrar una divergencia bajista limpia, seguir subiendo, mostrar otra, seguir subiendo e mostrar una tercera; cada una parece el techo, cada una falla, a veces durante semanas.»
  - S066 [43w] «Un funding persistente puede financiar justo esto: mientras los largos estén dispuestos a seguir pagando por mantener la posición, la tendencia puede desafiar a un momentum "agotado" mucho más tiempo del que la cuenta de un principiante puede aguantar en corto en contra.»
  - S067 [33w] «Una divergencia es un desacuerdo entre el precio y un oscilador de momentum: la regular compara dos extremos y avisa de un giro, la oculta aparece en un retroceso y apunta a continuación.»
  - S068 [38w] «Funciona porque un oscilador mide un ritmo de cambio y ve antes que el precio que el último empujón lo hacen menos participantes; y falla en una tendencia fuerte, capaz de imprimir divergencia tras divergencia y seguir adelante.»
- **8 Repeated paragraph opener** (1)
  - S001 ["Una divergencia" ×4 (S001, S008, S024, S049) — term as subject] 
- **9 Course-coined term** (4)
  - S003 [combustible [seed]] «Esa negativa es una pista de que el movimiento se está quedando sin combustible: no una garantía, una pista.»
  - S053 ["espacio abierto" = away from any level] «La diferencia concreta: una divergencia bajista que aparece justo cuando el precio toca el máximo exacto que frenó las tres últimas subidas es una señal; la divergencia idéntica a medio camino entre niveles, en espacio abierto, es ruido disfrazado de señal.»
  - S060 ["espacio abierto"] «Una divergencia en un nivel relevante es una señal; una divergencia en espacio abierto es ruido disfrazado de señal.»
  - S069 ["espacio abierto"] «En espacio abierto una divergencia es ruido; la misma divergencia contra un nivel que el gráfico ya respeta es una señal, porque el trabajo lo hace el nivel.»
- **10 Metaphor then gloss** (1)
  - S064 [metaphor "el cementerio de quienes operan divergencias", glossed by S065] «Lo más importante: los movimientos parabólicos del cripto son el cementerio de quienes operan divergencias.»
- **11 Synonym rotation** (3)
  - S003 [momentum fading: quedándose sin combustible (S003), se está apagando (S013), desaceleración (S042), agotado (S046)] 
  - S006 [the momentum behind a move: cuánto esfuerzo (S006), fuerza (S011), convicción (S015)] 
  - S014 [fewer buyers on the last push: menos participantes (S014), una multitud más delgada (S019), menos gente (S041)] 
- **A absolutes** (5)
  - S029 [debe] «en una tendencia alcista sana, un retroceso debe reiniciar el momentum sin romper la estructura.»
  - S034 [nunca] «En el oscilador la caída parece peor que antes; en el precio, la tendencia nunca se rompió.»
  - S037 [nunca] «El rebote parece fuerte en el oscilador, pero la estructura nunca dejó de caer.»
  - S041 [siempre] «En un punto de giro auténtico, el último empujón a un nuevo extremo casi siempre lo hace menos gente: los compradores ansiosos ya están dentro, así que el tramo final es más lento aunque el precio todavía marque máximos.»
  - S046 [debería] «El momentum "debería" estar agotado y sencillamente no lo está: una tendencia decidida sigue atrayendo compradores nuevos más rápido de lo que se cansan los viejos.»

**EN** — 31 hits, 69 sentences, density 44.9

- **1 Filler** (7)
  - S004 ["really": emphatic] «The whole lesson is really about one skill: knowing what that clue is worth, and when it is worth nothing at all.»
  - S038 [other filler: "The trick that keeps people straight:" announcer] «The trick that keeps people straight: regular divergence compares the extremes and expects a turn; hidden divergence appears on the retracement and expects the trend to resume.»
  - S046 ["simply": intensifier ("and isn't")] «Momentum "should" be exhausted and simply isn't — a determined trend keeps attracting fresh buyers faster than the old ones tire.»
  - S053 [other filler: "The concrete difference:" announcer] «The concrete difference: a bearish divergence that appears as price taps the exact high that capped the last three rallies is a signal; the identical divergence halfway between levels, in open space, is noise wearing a signal's costume.»
  - S064 [other filler: "Most important:" announcer] «Most important: crypto parabolic moves are the graveyard of divergence traders.»
  - S065 ["genuine": intensifier on "mania"] «A coin in a genuine mania can print a clean bearish divergence, keep going, print another, keep going, and print a third — each one looking like the top, each one wrong, sometimes for weeks.»
  - S066 ["exactly": emphatic] «Persistent funding can bankroll exactly this: as long as longs are willing to keep paying to hold, the trend can defy "exhausted" momentum far longer than a beginner's account can stay short against it.»
- **4 Summary/uplift closer** (9)
  - S004 [editorial: "The whole lesson is really about one skill"] «The whole lesson is really about one skill: knowing what that clue is worth, and when it is worth nothing at all.»
  - S007 [restate: repeats the definition of S001] «When those two stories stop matching, you are looking at a divergence.»
  - S015 [restate: repeats S014] «A trend that can no longer make new highs *with conviction* is a trend close to running out of buyers.»
  - S023 [restate: "lower in price but higher in momentum" repeats S022's numbers] «The new low is *lower in price but higher in momentum*: sellers reached further and got less for it.»
  - S031 [editorial: "is the reason… not a warning against it" re-tells S030] «The scary-looking oscillator is the *reason* the trend can continue, not a warning against it.»
  - S037 [restate: repeats S036] «The bounce looks strong on the oscillator, but structure never stopped falling.»
  - S044 [editorial: "That lead time is the entire edge a divergence offers."] «That lead time is the entire edge a divergence offers.»
  - S048 [restate: repeats S047] «The single most expensive habit in this whole topic is treating "momentum is fading" as "the top is in."»
  - S054 [restate: repeats S053] «Same oscillator reading, completely different value — because the level, not the oscillator, is doing the work.»
- **5 Sentence over 30 words** (8)
  - S041 [38w] «At a genuine turning point, the last push to a new extreme is almost always made by fewer participants: the eager buyers are already in, so the final leg up is slower even though price still ticks higher.»
  - S053 [38w] «The concrete difference: a bearish divergence that appears as price taps the exact high that capped the last three rallies is a signal; the identical divergence halfway between levels, in open space, is noise wearing a signal's costume.»
  - S062 [32w] «Markets run 24/7, so divergences form on weekend and overnight candles that are thin and easy to misread — a "divergence" on low weekend volume often evaporates when real liquidity returns on Monday.»
  - S063 [31w] «On thin alt books, a handful of orders can jam price to a new high while the oscillator barely moves, manufacturing divergences that reflect a quiet book rather than fading conviction.»
  - S065 [34w] «A coin in a genuine mania can print a clean bearish divergence, keep going, print another, keep going, and print a third — each one looking like the top, each one wrong, sometimes for weeks.»
  - S066 [34w] «Persistent funding can bankroll exactly this: as long as longs are willing to keep paying to hold, the trend can defy "exhausted" momentum far longer than a beginner's account can stay short against it.»
  - S067 [33w] «A divergence is a disagreement between price and a momentum oscillator: a regular divergence compares two extremes and warns of a reversal, a hidden divergence appears on a pullback and points to continuation.»
  - S068 [39w] «It works because an oscillator measures rate of change, so it sees the last push being made by fewer participants before price does — and it fails in a strong trend, which can print divergence after divergence and keep going.»
- **9 Course-coined term** (4)
  - S003 [fuel [seed]] «That refusal is a clue that the move is running out of fuel — not a guarantee, a clue.»
  - S053 ["open space" = away from any level] «The concrete difference: a bearish divergence that appears as price taps the exact high that capped the last three rallies is a signal; the identical divergence halfway between levels, in open space, is noise wearing a signal's costume.»
  - S060 ["open space"] «A divergence at a meaningful level is a signal; a divergence in open space is noise dressed as a signal.»
  - S069 ["open space"] «In open space a divergence is noise; the same divergence into a level the chart already respects is a signal, because the level is doing the work.»
- **10 Metaphor then gloss** (1)
  - S064 [metaphor "the graveyard of divergence traders", glossed by S065] «Most important: crypto parabolic moves are the graveyard of divergence traders.»
- **11 Synonym rotation** (2)
  - S003 [momentum fading: running out of fuel (S003), fading (S013), slowdown (S042), rolls over (S043), exhausted (S046)] 
  - S006 [the momentum behind a move: how hard it had to work (S006), force (S011), conviction (S015)] 
- **A absolutes** (3)
  - S034 [never] «On the oscillator the dip looks worse than before; on price, the trend never broke.»
  - S037 [never] «The bounce looks strong on the oscillator, but structure never stopped falling.»
  - S041 [always] «At a genuine turning point, the last push to a new extreme is almost always made by fewer participants: the eager buyers are already in, so the final leg up is slower even though price still ticks higher.»

### m13-l1

**ES** — 27 hits, 75 sentences, density 36.0

- **1 Filler** (4)
  - S032 [claramente: intensifier on "intacta"] «Porque un retroceso sano dentro de una tendencia real suele devolver *entre* la mitad y en torno a dos tercios del movimiento: lo bastante superficial para que la tendencia siga claramente intacta, lo bastante profundo para sacudir a las manos débiles y dejar que las órdenes en reposo se repongan.»
  - S036 [other: announcer sentence "Aquí está la parte que la mayoría de los tutoriales se salta"] «Aquí está la parte que la mayoría de los tutoriales se salta.»
  - S059 [exactamente: emphatic, no quantity pinned] «Ese solapamiento es de la confluencia más limpia que encontrarás: nuestro 0,618 en 2.201, pegado sobre 2.200, es exactamente ese tipo de emparejamiento.»
  - S072 [de verdad: emphatic; the contrast "no dónde esperabas" already carries it] «Tu tarea es leer dónde aterrizó de verdad el retroceso, no dónde esperabas que lo hiciera.»
- **2 Rhythmic triad** (1)
  - S049 [se pasa de largo / mecha a través / se queda corto: first two overlap (overshoot); drop "mecha a través" or "se pasa de largo"] «No lo hará: eso es una *zona*, no una línea de láser, y el precio se pasa de largo, mecha a través y gira con toda naturalidad, o se queda corto antes de llegar.»
- **3 Rhetorical question** (2)
  - S031 «¿Por qué esa banda y no otra?»
  - S039 «Entonces, ¿por qué hacen algo estos niveles?»
- **4 Summary/uplift closer** (1)
  - S028 [restate: the swap was just shown in S027; adds only "toda lectura es errónea"] «Tus niveles superficial y profundo se intercambian de sitio, y toda lectura que hagas sobre ellos es errónea.»
- **5 Sentence over 30 words** (14)
  - S002 [31w] «Los retrocesos de Fibonacci son un conjunto de niveles horizontales que los traders dibujan sobre ese movimiento para estimar *hasta dónde llegará el retroceso* antes de que la tendencia se reanude.»
  - S004 [32w **aside-only** (16w without asides)] «Dibujas la herramienta sobre un tramo de impulso limpio —un swing fuerte de un mínimo a un máximo, o de un máximo a un mínimo— y esta divide ese rango en ratios.»
  - S019 [31w **aside-only** (25w without asides)] «Más allá del rango de retroceso están las extensiones —1,272 y 1,618 son las habituales—, que proyectan *hasta dónde podría llegar el siguiente tramo* si la tendencia supera el extremo anterior.»
  - S032 [50w] «Porque un retroceso sano dentro de una tendencia real suele devolver *entre* la mitad y en torno a dos tercios del movimiento: lo bastante superficial para que la tendencia siga claramente intacta, lo bastante profundo para sacudir a las manos débiles y dejar que las órdenes en reposo se repongan.»
  - S033 [36w] «Un retroceso que se frena por encima del 0,5 apenas puso a prueba la tendencia; uno que atraviesa limpiamente el 0,618 te avisa de que el movimiento quizá haya terminado, no de que solo esté descansando.»
  - S034 [34w] «La figura muestra el caso de manual: un impulso al alza y, después, un retroceso que se adentra en la zona dorada y reacciona en el 0,618 antes de que la tendencia se reanude.»
  - S044 [31w] «Supón que nuestro 0,618 en 2.201 cae justo por encima de un número redondo en 2.200 al que todos se anclan, y encima de un soporte antiguo de la semana pasada.»
  - S049 [34w] «No lo hará: eso es una *zona*, no una línea de láser, y el precio se pasa de largo, mecha a través y gira con toda naturalidad, o se queda corto antes de llegar.»
  - S050 [39w **aside-only** (27w without asides)] «Si pones un stop un tick más allá del 0,618 (2.201) esperando un giro perfecto, el ruido normal asomándose hasta 2.186 —justo lo que hace la mecha del retroceso en la figura— te sacará y luego girará sin ti.»
  - S057 [34w **aside-only** (23w without asides)] «Los traders de cripto se anclan mucho a las cifras redondas grandes —60.000, 65.000, 70.000 en BTC; 1,00 o 0,50 en una alt— y las órdenes en reposo se amontonan ahí de todos modos.»
  - S061 [41w **aside-only** (26w without asides)] «Cripto no cierra nunca, así que un mismo nivel de fib puede sondearse una y otra vez —en libros poco profundos de fin de semana, en las horas tranquilas de la madrugada— antes de que por fin aguante o se rompa.»
  - S063 [41w] «Esa liquidez escasa fuera de horas también hace que los excesos más allá del nivel sean mayores que en un mercado profundo de horario normal: un motivo más para tratar el 0,618 como una zona con holgura, no como una línea.»
  - S073 [42w] «Los retrocesos de Fibonacci dividen un tramo de impulso limpio en ratios que estiman hasta dónde llega un retroceso —0,382 superficial, 0,5 el punto medio, 0,618 el profundo "dorado"—, y el 0,5–0,618 se lee como una zona y no como una línea.»
  - S075 [44w] «Ningún mecanismo obliga a un mercado a respetar el 61,8 %; los niveles funcionan porque están vigilados y porque a veces coinciden con un número redondo o un soporte antiguo, así que un fib sin nada más cerca es una conjetura con un decimal pegado.»
- **7 No solo / not only** (1)
  - S026 «Dibuja nuestro tramo 2.017→2.499 al revés —como si fuera una tendencia bajista de 2.499 a 2.017— y los números no solo se desplazan, se invierten.»
- **10 Metaphor then gloss** (2)
  - S003 ["no una bola de cristal" then glossed: "te dicen dónde suele... no dónde tiene que"] «Son una herramienta de medida, no una bola de cristal: te dicen dónde *suele* quedarse sin recorrido un retroceso, no dónde *tiene* que hacerlo.»
  - S049 ["no una línea de láser" then glossed by what price does around it] «No lo hará: eso es una *zona*, no una línea de láser, y el precio se pasa de largo, mecha a través y gira con toda naturalidad, o se queda corto antes de llegar.»
- **11 Synonym rotation** (2)
  - S001 [impulse leg: movimiento (S001), tramo de impulso (S004), swing (S004), impulso (S005), tramo (S013)] 
  - S029 [zona 0,5–0,618: banda (S029), zona dorada (S029), región (S035), zona (S049)] 
- **A absolutes** (3)
  - S001 [nunca] «Tras un movimiento fuerte, el precio casi nunca avanza en línea recta: empuja, retrocede y (a menudo) continúa.»
  - S025 [siempre] «La dirección importa más de lo que espera un principiante: siempre arrastras desde el inicio del impulso hasta su final.»
  - S061 [nunca] «Cripto no cierra nunca, así que un mismo nivel de fib puede sondearse una y otra vez —en libros poco profundos de fin de semana, en las horas tranquilas de la madrugada— antes de que por fin aguante o se rompa.»

**EN** — 20 hits, 75 sentences, density 26.7

- **1 Filler** (4)
  - S032 [other: "clearly" intensifier on "still intact"] «Because a healthy pullback in a real trend usually gives back *between* a half and roughly two-thirds of the move: shallow enough that the trend is clearly still intact, deep enough to shake out weak hands and let resting orders refill.»
  - S036 [other: announcer sentence "Here is the part most tutorials skip"] «Here is the part most tutorials skip.»
  - S059 [exactly: emphatic, no quantity pinned] «That overlap is some of the cleanest confluence you will find: our 0.618 at 2,201, snug above 2,200, is exactly that kind of pairing.»
  - S072 [actually: emphatic; "not where you hoped" already carries the contrast] «Your job is to read where the pullback actually landed — not where you hoped it would.»
- **2 Rhythmic triad** (1)
  - S049 [overshoots / wicks through and reverses / stops short: first two overlap; drop "overshoots" or "wicks through"] «It won't — that is a *zone*, not a laser line, and price routinely overshoots, wicks through and reverses, or stops short before it.»
- **3 Rhetorical question** (2)
  - S031 «Why that band and not some other?»
  - S039 «So why do these levels do anything at all?»
- **4 Summary/uplift closer** (1)
  - S028 [restate: the swap was just shown in S027; adds only "every read is wrong"] «Your shallow and deep levels swap places, and every read you take off them is wrong.»
- **5 Sentence over 30 words** (6)
  - S004 [31w **aside-only** (16w without asides)] «You draw the tool across one clean impulse leg — a strong swing from a low to a high, or a high to a low — and it slices that range into ratios.»
  - S032 [41w] «Because a healthy pullback in a real trend usually gives back *between* a half and roughly two-thirds of the move: shallow enough that the trend is clearly still intact, deep enough to shake out weak hands and let resting orders refill.»
  - S050 [38w **aside-only** (28w without asides)] «If you place a stop one tick beyond 0.618 (2,201) expecting a perfect turn, normal noise poking down to 2,186 — exactly what the pullback's wick does in the figure — will stop you out and then reverse without you.»
  - S063 [34w] «That thin off-hours liquidity also makes overshoots past the level larger than you would see in a deep, regular-hours market — one more reason to treat 0.618 as a zone with slack, not a line.»
  - S073 [39w **aside-only** (29w without asides)] «Fibonacci retracements slice one clean impulse leg into ratios that estimate how deep a pullback runs — 0.382 shallow, 0.5 the midpoint, 0.618 the deep golden one — and 0.5 to 0.618 is read as a zone rather than a line.»
  - S075 [43w] «No mechanism forces a market to respect 61.8%; the levels work because they are watched and because they sometimes coincide with a round number or an old support, so a fib with nothing else near it is a guess with a decimal attached.»
- **7 No solo / not only** (1)
  - S026 «Draw our 2,017→2,499 leg backwards — as if it were a downtrend from 2,499 to 2,017 — and the numbers don't just shift, they invert.»
- **9 Course-coined term** (1)
  - S044 [shelf [seed]] «Suppose our 0.618 at 2,201 lands a hair above a round number at 2,200 that everyone anchors to, and right on an old support shelf from last week.»
- **10 Metaphor then gloss** (2)
  - S003 ["not a crystal ball" then glossed: "they tell you where a pullback tends to..."] «They are a measuring tool, not a crystal ball: they tell you where a pullback *tends* to run out of room, not where it *must*.»
  - S049 ["not a laser line" then glossed by what price does around it] «It won't — that is a *zone*, not a laser line, and price routinely overshoots, wicks through and reverses, or stops short before it.»
- **11 Synonym rotation** (2)
  - S001 [impulse leg: move (S001), impulse leg (S004), swing (S004), impulse (S005), leg (S013)] 
  - S029 [0.5–0.618 zone: band (S029), golden zone (S029), region (S035), zone (S049)] 
- **A absolutes** (3)
  - S003 [must] «They are a measuring tool, not a crystal ball: they tell you where a pullback *tends* to run out of room, not where it *must*.»
  - S025 [always] «The direction matters more than beginners expect: always drag from the start of the impulse to its end.»
  - S061 [never] «Crypto never closes, so a single fib level can be probed over and over — through thin weekend books, through the quiet overnight hours — before it finally holds or breaks.»

### m14-l1

**ES** — 29 hits, 65 sentences, density 44.6

- **1 Filler** (7)
  - S003 [de verdad: emphatic on "le importó"] «Es el número de unidades negociadas en un periodo, dibujado como una barra debajo del precio, y es lo más parecido que tienes a una medida de *participación*: de cuánto le importó de verdad un movimiento al mercado.»
  - S011 [de verdad: emphatic; "una multitud" after 4,5× says it] «Si la media de 20 barras es de 10.000 contratos por hora y la barra actual marca 45.000, eso es unas 4,5 veces la participación habitual: una multitud de verdad.»
  - S025 [other: "mismísimo" intensifier on "ese cierre"] «Compáralo con ese mismísimo cierre en 2.195 pero con las barras en algo más de la mitad de esa media: la misma línea cruzada, pero casi nadie vino.»
  - S027 [other: "justo" emphatic in "es justo el material"] «El volumen fuerte no *garantiza* que el movimiento continúe, pero una ruptura sin participación detrás es justo el material del que se hace un fakeout.»
  - S028 [exactamente: emphatic, no quantity pinned] «Los dos paneles de arriba muestran exactamente esto, y no es que se parezcan: son el mismo gráfico.»
  - S032 [literalmente: emphatic; S028 already said they are the same chart] «Las dos rupturas son literalmente el mismo suceso; el volumen que hay debajo es toda la historia.»
  - S050 [honesta: "la lectura honesta" applied to a reading] «Cuando las tres discrepan —una ruptura en un buen nivel pero con volumen muerto— la lectura honesta es *todavía no*.»
- **2 Rhythmic triad** (1)
  - S053 [sin parar / sin campana de cierre / sin dato oficial de volumen diario: first two say the same; drop "sin parar"] «Las criptomonedas se negocian sin parar, sin campana de cierre y sin un dato oficial de volumen diario, y eso cambia cómo lees las barras.»
- **4 Summary/uplift closer** (5)
  - S013 [restate: noise vs ratio-to-normal repeats S009–S010] «La cifra absoluta es ruido; lo que es señal es la *proporción respecto a lo normal*.»
  - S015 [editorial: "es la mayor parte de lo que es el análisis de volumen"] «Esa única comparación —esta barra contra sus vecinas— es la mayor parte de lo que es el análisis de volumen.»
  - S032 [restate/editorial: "el mismo suceso" repeats S028; "el volumen es toda la historia"] «Las dos rupturas son literalmente el mismo suceso; el volumen que hay debajo es toda la historia.»
  - S046 [restate: S045's "aviso, no cita con fecha" retold as fuel/tank metaphor] «Te dice que queda poco combustible; no te dice el minuto en que se vacía el depósito.»
  - S051 [editorial: what confluence does and does not do, after the rule was stated] «La confluencia no te hace tener razón; inclina las probabilidades a tu favor y filtra el ruido que cualquier señal aislada genera por su cuenta.»
- **5 Sentence over 30 words** (11)
  - S003 [38w] «Es el número de unidades negociadas en un periodo, dibujado como una barra debajo del precio, y es lo más parecido que tienes a una medida de *participación*: de cuánto le importó de verdad un movimiento al mercado.»
  - S008 [36w] «Lo que mide es convicción: una vela verde grande con volumen alto significa que muchos participantes estuvieron de acuerdo con la subida y actuaron; la misma vela con volumen escaso significa que casi nadie lo hizo.»
  - S017 [32w **aside-only** (22w without asides)] «Cuando el precio rompe un nivel —por encima de una resistencia, por debajo de un soporte— el movimiento del precio en sí se ve igual lo empujara un trader o diez mil.»
  - S024 [42w] «En el cuarto intento el precio cierra por encima, en 2.195, con las barras de volumen a unas tres veces su media reciente —la más alta de todas llega a casi cinco veces—: cientos de participantes votando que ese nivel ha caído.»
  - S030 [43w] «Y hasta ese punto la única diferencia está debajo, en las barras de volumen: un pico de participación a la izquierda, tras el que la ruptura tiene continuidad, y unas barras finas y sin ganas a la derecha, tras las que se deshace.»
  - S036 [35w **aside-only** (23w without asides)] «Los vendedores golpean el mercado con fuerza y, aun así, un gran comprador en reposo sigue rellenando una orden de compra en 2.125 —un "iceberg" que absorbe cada oleada de ventas tan rápido como llega—.»
  - S044 [41w] «Igual que las divergencias de momentum del módulo del oscilador, un perfil de volumen que se adelgaza es una lectura temprana de la participación, y la participación se apaga antes que el precio: los últimos compradores en llegar son los menos.»
  - S058 [41w] «Una ruptura en un domingo tranquilo supera un listón mucho más bajo para contar como "volumen fuerte", así que los movimientos de fin de semana exageran su propia convicción y son más propensos a deshacerse cuando vuelve la multitud entre semana.»
  - S061 [41w **aside-only** (29w without asides)] «Algunos exchanges han inflado históricamente sus cifras con wash trading —la misma entidad comprándose y vendiéndose a sí misma para fingir actividad—, así que el volumen bruto en un exchange poco profundo o no regulado puede ser en gran parte ficción.»
  - S063 [37w] «El volumen cuenta transacciones, así que mide participación y nunca dirección, y solo significa algo leído contra su propia media reciente, porque la cifra absoluta es ruido y la señal es la proporción respecto a lo normal.»
  - S065 [43w] «Mucho volumen sin movimiento es absorción, un volumen que se adelgaza hacia nuevos máximos avisa de que la participación se apaga, y el hábito que lo une todo es la confluencia: que la estructura, el indicador y el volumen coincidan antes de actuar.»
- **6 Stacked hedge** (1)
  - S040 [debería + más o menos] «El volumen debería acompañar más o menos al movimiento al que pertenece.»
- **9 Course-coined term** (2)
  - S046 [combustible [seed]] «Te dice que queda poco combustible; no te dice el minuto en que se vacía el depósito.»
  - S048 [lente [seed]] «La estructura (un nivel o una tendencia real y ya testeada), un indicador (RSI o MACD) y el volumen son tres lentes distintas.»
- **11 Synonym rotation** (2)
  - S003 [participation: participación (S003), multitud (S004), convicción (S008), gente (S002)] 
  - S042 [falling volume into highs: se encoge (S042), va tirando con las reservas (S043), se adelgaza (S044), se apaga (S044)] 
- **A absolutes** (2)
  - S040 [debería] «El volumen debería acompañar más o menos al movimiento al que pertenece.»
  - S063 [nunca, summary] «El volumen cuenta transacciones, así que mide participación y nunca dirección, y solo significa algo leído contra su propia media reciente, porque la cifra absoluta es ruido y la señal es la proporción respecto a lo normal.»

**EN** — 28 hits, 65 sentences, density 43.1

- **1 Filler** (6)
  - S003 [actually: emphatic on "cared"] «It is the number of units traded in a period, drawn as a bar under the price, and it is the closest thing you have to a measure of *participation* — of how much the market actually cared about a move.»
  - S011 [genuine: emphatic; "a crowd" after 4.5× says it] «If the 20-bar average is 10,000 contracts an hour and the current bar prints 45,000, that is roughly 4.5× the usual participation: a genuine crowd.»
  - S025 [other: "very" intensifier in "the very same close"] «Compare that to the very same close at 2,195 with the bars at a little over half that average: the same line crossed, but almost nobody came.»
  - S028 [exactly: emphatic, no quantity pinned] «The two panels above show exactly this, and they do not merely resemble each other — they are the same chart.»
  - S032 [literally: emphatic; S028 already said they are the same chart] «The two breaks are literally the same event; the volume beneath them is the whole story.»
  - S050 [honest: "the honest read" applied to a reading] «When the three disagree — a break at a good level but on dead volume — the honest read is *not yet*.»
- **2 Rhythmic triad** (1)
  - S053 [around the clock / no closing bell / no official daily volume print: first two say the same; drop "around the clock"] «Crypto trades around the clock, with no closing bell and no official daily volume print, and that changes how you read the bars.»
- **4 Summary/uplift closer** (5)
  - S013 [restate: noise vs ratio-to-normal repeats S009–S010] «The absolute figure is noise; the *ratio to normal* is the signal.»
  - S015 [editorial: "is most of what volume analysis is"] «That single comparison — this bar against its neighbours — is most of what volume analysis is.»
  - S032 [restate/editorial: "the same event" repeats S028; "the volume is the whole story"] «The two breaks are literally the same event; the volume beneath them is the whole story.»
  - S046 [restate: S045's "warning, not a dated appointment" retold as fuel/tank metaphor] «It tells you the fuel is running low; it does not tell you the minute the tank runs dry.»
  - S051 [editorial: what confluence does and does not do, after the rule was stated] «Confluence does not make you right; it stacks the odds in your favour and filters out the noise that any single signal throws up on its own.»
- **5 Sentence over 30 words** (9)
  - S003 [40w] «It is the number of units traded in a period, drawn as a bar under the price, and it is the closest thing you have to a measure of *participation* — of how much the market actually cared about a move.»
  - S008 [35w] «What it measures is conviction: a large green candle on heavy volume means a lot of participants agreed with the up-move and acted on it; the same candle on thin volume means almost nobody did.»
  - S024 [37w] «On the fourth attempt price closes above it, at 2,195, with the volume bars running about three times their recent average — the tallest of them nearly five times: hundreds of participants voting that the level is gone.»
  - S030 [39w] «And up to that point the only difference is underneath, in the volume bars: a surge of participation on the left, after which the break follows through, and thin, half-hearted bars on the right, after which it comes undone.»
  - S044 [32w] «Like the momentum divergences from the oscillator module, a thinning volume profile is an early read on participation, and participation fades before price does — the last buyers to arrive are the fewest.»
  - S058 [34w] «A breakout on a quiet Sunday clears a much lower bar to count as "strong volume," so weekend moves overstate their own conviction and are more prone to unwinding when the weekday crowd returns.»
  - S061 [34w **aside-only** (23w without asides)] «Some exchanges have historically inflated their figures with wash trading — the same entity buying and selling to itself to fake activity — so raw volume on a thin or unregulated venue can be largely fiction.»
  - S063 [35w] «Volume counts transactions, so it measures participation and never direction — and it only means anything read against its own recent average, because the absolute figure is noise and the ratio to normal is the signal.»
  - S065 [37w] «Heavy volume with no movement is absorption, thinning volume into new highs is a warning that participation is fading, and the habit that ties it all together is confluence — structure, indicator and volume agreeing before you act.»
- **6 Stacked hedge** (2)
  - S040 [should + roughly] «Volume should roughly keep pace with the move it belongs to.»
  - S061 [can + largely] «Some exchanges have historically inflated their figures with wash trading — the same entity buying and selling to itself to fake activity — so raw volume on a thin or unregulated venue can be largely fiction.»
- **7 No solo / not only** (1)
  - S028 «The two panels above show exactly this, and they do not merely resemble each other — they are the same chart.»
- **9 Course-coined term** (2)
  - S046 [fuel [seed]] «It tells you the fuel is running low; it does not tell you the minute the tank runs dry.»
  - S048 [lens [seed]] «Structure (a real, tested level or trend), an indicator (RSI or MACD), and volume are three different lenses.»
- **11 Synonym rotation** (2)
  - S003 [participation: participation (S003), crowd (S004), conviction (S008), people (S002)] 
  - S042 [falling volume into highs: shrinks (S042), running on fumes (S043), thinning (S044), fades (S044)] 
- **A absolutes** (1)
  - S063 [never, summary] «Volume counts transactions, so it measures participation and never direction — and it only means anything read against its own recent average, because the absolute figure is noise and the ratio to normal is the signal.»

### m15-l1

**ES** — 35 hits, 69 sentences, density 50.7

- **1 Filler** (6)
  - S010 [honesto: "lo honesto es fijarse en que" = honest + announcer] «Eso es una afirmación sobre una *regularidad de la demanda*, y lo honesto es fijarse en que nadie está obligado a mantenerla.»
  - S019 [other: "justo" emphatic in "el ritmo es justo lo que puede pararse"] «Es una *descripción de un ritmo que se ha cumplido*, y el ritmo es justo lo que puede pararse sin que se rompa nada.»
  - S031 [exactamente: emphatic; "la regla de m08-l1" already identifies it] «Decide el cuerpo, no la mecha, exactamente la regla de m08-l1 para un nivel horizontal.»
  - S042 [claramente: intensifier; the numbers (10.575 vs 10.740) already show the distance] «La decisión es la vela que cierra en 10.575 contra una línea proyectada en 10.740 —un cuerpo claramente al otro lado— con un volumen de más del triple de la referencia tranquila del ritmo anterior.»
  - S044 [precisamente: emphatic "precisamente por"] «La línea obvia es peligrosa precisamente por obvia.»
  - S057 [honesto: announcer sentence whose only content is "keeps this honest"] «Y aquí está la frase que mantiene esto honesto.»
- **4 Summary/uplift closer** (8)
  - S003 [restate: "El nivel recuerda." sums up S001–S002] «El nivel recuerda.»
  - S023 [restate: repeats the rule's own label (two touches propose, third validates)] «Hasta entonces tienes una candidata, no una línea de tendencia.»
  - S027 [editorial: "Es una elección, y la decimos para que puedas reclamárnosla"] «Es una elección, y la decimos para que puedas reclamárnosla; es coherente con lo que la sección siguiente hace con una ruptura.»
  - S038 [restate: S036–S037 already showed it is less information] «Es aún menos información de lo habitual.»
  - S048 [restate: repeats S034's fakeout line with "caza de stops"] «Una ruptura de una línea concurrida con volumen fino es el material del que se hace una caza de stops.»
  - S050 [editorial: "No es un segundo hallazgo: es la misma línea, copiada"] «No es un segundo hallazgo: es la misma línea, copiada.»
  - S056 [restate: which line broke = which ending, already implied by S054] «Por qué línea se fue el precio es lo que te dice cuál de las dos pasó.»
  - S061 [editorial: "uno bien trazado parece una máquina"] «Un canal es especialmente bueno escondiendo eso, porque uno bien trazado parece una máquina.»
- **5 Sentence over 30 words** (13)
  - S006 [42w] «Esta lección enseña la herramienta igualmente, porque la mitad de lo que leerás sobre gráficos está trazado con ella, y la enseña diciendo su debilidad en voz alta en vez de enterrarla: **la diagonal es el instrumento más débil de este curso.**»
  - S026 [34w] «Este curso se ancla en los cierres, así que las líneas de estas figuras van justo por debajo de los cierres de un mercado alcista y las mechas se meten por debajo de ellas.»
  - S040 [34w **aside-only** (24w without asides)] «El precio volvió cuatro veces a la misma línea ascendente —cerca de 9.550, luego 9.935, luego 10.300 y luego 10.570— y giró cada vez, así que en la tercera visita la línea quedó validada.»
  - S042 [35w **aside-only** (29w without asides)] «La decisión es la vela que cierra en 10.575 contra una línea proyectada en 10.740 —un cuerpo claramente al otro lado— con un volumen de más del triple de la referencia tranquila del ritmo anterior.»
  - S045 [37w] «Si todo el mundo ve el mismo soporte ascendente, todo el mundo pone su stop justo por debajo, y eso es una bolsa de órdenes de venta en reposo en un sitio conocido, que es todo m19-l2.»
  - S046 [32w] «Un movimiento hasta ahí las dispara, y el estallido de ventas forzadas puede imprimir una vela directamente a través de la línea antes de que el precio cierre otra vez por encima.»
  - S054 [39w **aside-only** (28w without asides)] «El precio puede acelerar y salir por la línea a la que iba —el borde lejano, en el sentido que el canal ya llevaba— o el ritmo puede agotarse y ceder por la línea sobre la que estaba construido.»
  - S055 [31w] «Ninguna de las dos está prometida, y ninguna es propiedad de la pendiente: un canal alcista puede perder su suelo con la misma facilidad con la que puede quedarse sin techo.»
  - S065 [35w **aside-only** (23w without asides)] «Crees que la tendencia sigue intacta, así que encuentras los anclajes que la mantienen intacta —un mínimo menor aquí, una mecha en vez de un cuerpo allá— y la línea te da obedientemente la razón.»
  - S066 [40w] «Ajusta la tesis a la línea, nunca la línea a la tesis; y si no puedes trazar una que sobreviva a la regla 3, la respuesta es que no hay línea, no que te haga falta otro par de anclajes.»
  - S067 [43w] «Un nivel horizontal afirma que un precio importó; una línea de tendencia afirma un ritmo constante de avance, y la orden de nadie descansa en un precio que se mueve, y por eso la diagonal es el instrumento más débil de este curso.»
  - S068 [32w] «Trázala con disciplina: dos toques proponen y el tercero valida, declara si te anclas en mechas o en cuerpos y mantenlo, y una línea que redibujas cada semana nunca fue una línea.»
  - S069 [36w] «Lee la ruptura como cualquier otra, por el cuerpo y por la participación que la acompaña, y recuerda que un canal solo describe una regularidad que se ha cumplido: operarlo es la apuesta de que continúa.»
- **9 Course-coined term** (7)
  - S014 [seed shelf (as "estante"): "Si un estante aguantó dos veces" = a horizontal support/resistance level] «Si un estante aguantó dos veces, la razón por la que podría aguantar una tercera es que algunas de esas mismas órdenes —y otras nuevas puestas *porque* aguantó— siguen ahí.»
  - S019 [non-seed ritmo: "una descripción de un ritmo que se ha cumplido" = trend's rate of advance] «Es una *descripción de un ritmo que se ha cumplido*, y el ritmo es justo lo que puede pararse sin que se rompa nada.»
  - S042 [non-seed ritmo: "la referencia tranquila del ritmo anterior"] «La decisión es la vela que cierra en 10.575 contra una línea proyectada en 10.740 —un cuerpo claramente al otro lado— con un volumen de más del triple de la referencia tranquila del ritmo anterior.»
  - S045 [seed bolsa de liquidez (as "bolsa de órdenes de venta en reposo"): stop cluster under an obvious line] «Si todo el mundo ve el mismo soporte ascendente, todo el mundo pone su stop justo por debajo, y eso es una bolsa de órdenes de venta en reposo en un sitio conocido, que es todo m19-l2.»
  - S048 [non-seed concurrido (calque of "crowded"): "una línea concurrida" = a line everyone watches] «Una ruptura de una línea concurrida con volumen fino es el material del que se hace una caza de stops.»
  - S051 [non-seed ritmo: "un ritmo que puedes leer por los dos lados" (channel)] «Lo que añade un canal es un *ritmo que puedes leer por los dos lados*: el precio se va del suelo, llega al techo, vuelve.»
  - S054 [non-seed ritmo: "el ritmo puede agotarse"] «El precio puede acelerar y salir por la línea a la que iba —el borde lejano, en el sentido que el canal ya llevaba— o el ritmo puede agotarse y ceder por la línea sobre la que estaba construido.»
- **11 Synonym rotation** (1)
  - S004 [trendline: línea de tendencia (S004), diagonal (S006), línea ascendente (S040), soporte ascendente (S045)] 
- **A absolutes** (3)
  - S024 [nunca] «Mechas o cuerpos, nunca mezclados.»
  - S066 [nunca] «Ajusta la tesis a la línea, nunca la línea a la tesis; y si no puedes trazar una que sobreviva a la regla 3, la respuesta es que no hay línea, no que te haga falta otro par de anclajes.»
  - S068 [nunca, summary] «Trázala con disciplina: dos toques proponen y el tercero valida, declara si te anclas en mechas o en cuerpos y mantenlo, y una línea que redibujas cada semana nunca fue una línea.»

**EN** — 33 hits, 69 sentences, density 47.8

- **1 Filler** (6)
  - S010 [honest: "the honest thing to notice is" = honest + announcer] «That is a claim about a *regularity of demand*, and the honest thing to notice is that nobody is obliged to maintain it.»
  - S031 [exactly: emphatic; "m08-l1's rule" already identifies it] «exactly m08-l1's rule for a horizontal level.»
  - S042 [other: "clearly" intensifier; the numbers already show the distance] «The decision is the candle that closes at 10,575 against a projected line at 10,740 — a body clearly through it — on volume more than three times the quiet baseline of the rhythm before it.»
  - S044 [precisely: emphatic "precisely because"] «The obvious line is dangerous precisely because it is obvious.»
  - S055 [exactly: "exactly as easily", emphatic, no quantity] «Neither is promised, and neither is a property of the slope: a rising channel can lose its floor exactly as easily as it can run out of its ceiling.»
  - S057 [honest: announcer sentence whose only content is "keeps this honest"] «And here is the sentence that keeps this honest.»
- **4 Summary/uplift closer** (8)
  - S003 [restate: "The level remembers." sums up S001–S002] «The level remembers.»
  - S023 [restate: repeats the rule's own label (two touches propose, third validates)] «Until then you have a candidate, not a trendline.»
  - S027 [editorial: "That is a choice, stated so you can hold it against us"] «That is a choice, stated so you can hold it against us — and it is consistent with what the next section does with a break.»
  - S038 [restate: S036–S037 already showed it is less information] «It is even less information than usual.»
  - S048 [restate: repeats S034's fakeout line with "stop hunt"] «A break through a crowded line on thin volume is the setup a stop hunt is made of.»
  - S050 [editorial: "It is not a second discovery — it is the same line, copied"] «It is not a second discovery — it is the same line, copied.»
  - S056 [restate: which line broke = which ending, already implied by S054] «Which line price left through is what tells you which of the two happened.»
  - S061 [editorial: "a well-drawn one looks like a machine"] «A channel is unusually good at hiding that, because a well-drawn one looks like a machine.»
- **5 Sentence over 30 words** (12)
  - S006 [41w] «This lesson teaches the tool anyway, because half of what you will read about charts is drawn with it — and it teaches it with the weakness said out loud rather than buried: **the diagonal is the weakest instrument in this course.**»
  - S014 [32w **aside-only** (24w without asides)] «If a shelf held twice, the reason it might hold a third time is that some of the same orders — and some new ones placed *because* it held — are still sitting there.»
  - S028 [32w] «If each new candle moves your anchor, what you have is a curve fitted to the past, and it will keep fitting the past for as long as you keep refitting it.»
  - S040 [31w **aside-only** (23w without asides)] «Price came back to the same rising line four times — near 9,550, then 9,935, then 10,300, then 10,570 — and turned each time, so by the third visit the line was validated.»
  - S042 [34w **aside-only** (29w without asides)] «The decision is the candle that closes at 10,575 against a projected line at 10,740 — a body clearly through it — on volume more than three times the quiet baseline of the rhythm before it.»
  - S045 [35w] «If everybody can see the same rising support, everybody puts their stop just under it — and that is a pocket of resting sell orders sitting at a known place, which is the whole of m19-l2.»
  - S054 [35w **aside-only** (24w without asides)] «Price can accelerate out through the line it was heading for — the far edge, in the direction the channel was already going — or the rhythm can give out through the line it was built on.»
  - S065 [33w **aside-only** (22w without asides)] «You believe the trend is intact, so you find the anchors that keep it intact — a lower low here, a wick instead of a body there — and the line obediently agrees with you.»
  - S066 [39w] «Fit the thesis to the line, never the line to the thesis, and if you cannot draw one that survives rule 3, the answer is that there is no line, not that you need a different pair of anchors.»
  - S067 [35w] «A horizontal level claims a price mattered; a trendline claims a constant rate of advance, and nobody's order rests at a moving price — which is why the diagonal is the weakest instrument in this course.»
  - S068 [33w] «Draw it with discipline: two touches propose and the third validates, declare whether you anchor on wicks or bodies and keep it, and a line you redraw every week was never a line.»
  - S069 [38w] «Read a break the way you read any other, by the body and by the participation behind it, and remember that a channel only describes a regularity that has held — trading it is the bet that it persists.»
- **9 Course-coined term** (6)
  - S014 [shelf [seed]] «If a shelf held twice, the reason it might hold a third time is that some of the same orders — and some new ones placed *because* it held — are still sitting there.»
  - S019 [non-seed rhythm: "a description of a rhythm that has held" = trend's rate of advance] «It is a *description of a rhythm that has held*, and the rhythm is the thing that can stop without anything breaking.»
  - S042 [non-seed rhythm: "the quiet baseline of the rhythm before it"] «The decision is the candle that closes at 10,575 against a projected line at 10,740 — a body clearly through it — on volume more than three times the quiet baseline of the rhythm before it.»
  - S045 [seed liquidity pool (as "pocket of resting sell orders"): stop cluster under an obvious line] «If everybody can see the same rising support, everybody puts their stop just under it — and that is a pocket of resting sell orders sitting at a known place, which is the whole of m19-l2.»
  - S051 [non-seed rhythm: "a rhythm you can read on both sides" (channel)] «What a channel adds is a *rhythm you can read on both sides*: price leaves the floor, reaches the ceiling, comes back.»
  - S054 [non-seed rhythm: "the rhythm can give out"] «Price can accelerate out through the line it was heading for — the far edge, in the direction the channel was already going — or the rhythm can give out through the line it was built on.»
- **11 Synonym rotation** (1)
  - S004 [trendline: trendline (S004), diagonal (S006), rising line (S040), rising support (S045)] 
- **A absolutes** (3)
  - S024 [never] «Wicks or bodies, never mixed.»
  - S066 [never] «Fit the thesis to the line, never the line to the thesis, and if you cannot draw one that survives rule 3, the answer is that there is no line, not that you need a different pair of anchors.»
  - S068 [never, summary] «Draw it with discipline: two touches propose and the third validates, declare whether you anchor on wicks or bodies and keep it, and a line you redraw every week was never a line.»

### m15-l2

**ES** — 25 hits, 50 sentences, density 50.0

- **1 Filler** (2)
  - S009 [merece la pena: announcer "merece la pena quedarse con ello"] «Lo que separa a sus miembros es cómo se reparte la convergencia entre las dos líneas, y merece la pena quedarse con ello porque convierte seis patrones con nombre en un solo objeto visto desde seis ángulos:»
  - S034 [exactamente: emphatic "que es exactamente lo que dice m13"] «Es estadística sin mecanismo, que es exactamente lo que dice m13 de una proporción de Fibonacci y m10-l1 de la media de 200 días.»
- **2 Rhythmic triad** (1)
  - S001 [cuerpo pequeño / mechas pequeñas / una barra en la que casi no pasó nada: the third restates the first two; drop it] «m08-l2 te enseñó una sola vela cuyo rango se desploma: cuerpo pequeño, mechas pequeñas, una barra en la que casi no pasó nada.»
- **4 Summary/uplift closer** (5)
  - S005 [restate: "La misma mecánica, otra escala" repeats S003] «La misma mecánica, otra escala; y como tarda veinte barras en vez de una, puedes verlo ocurrir.»
  - S008 [editorial: "Eso es toda la familia."] «Eso es toda la familia.»
  - S029 [restate: "Dice que el ritmo se está apagando" repeats S027–S028] «Dice que el ritmo se está apagando.»
  - S039 [editorial: "Eso no es una predicción: es lo que la compresión es"] «Eso no es una predicción: es lo que la compresión *es*, y es la misma afirmación que hace m16 sobre un régimen de mercado entero.»
  - S047 [restate: last prose unit; repeats S045 "convención, no promesa"] «Nada en la anchura inicial de una figura obliga al movimiento posterior a medir eso.»
- **5 Sentence over 30 words** (10)
  - S009 [37w] «Lo que separa a sus miembros es cómo se reparte la convergencia entre las dos líneas, y merece la pena quedarse con ello porque convierte seis patrones con nombre en un solo objeto visto desde seis ángulos:»
  - S027 [37w] «En una cuña ascendente los compradores están avanzando y les cuesta más cada vez: cada nuevo máximo es un paso más corto, contra un techo que cede terreno más despacio de lo que lo gana el suelo.»
  - S028 [32w] «Eso es *agotamiento observable de un ritmo*, la misma lectura que te da la divergencia precio/volumen de m14, y dice algo real: quien esté comprando tiene que trabajar más para conseguir menos.»
  - S033 [52w] «Todos los porcentajes de manual asociados a esto —del tipo «el 68 % de las cuñas ascendentes se resuelve a la baja»— salen de un patrón que alguien contó sobre un conjunto de gráficos que eligió, con una definición de «cuña» que eligió, y no se apoya en ningún mecanismo que puedas señalar.»
  - S043 [36w] «Una compresión es silenciosa por construcción, así que el volumen cae a lo largo de ella, lo que hace que el repunte de una ruptura genuina sea fácil de ver, y su ausencia igual de fácil.»
  - S044 [33w] «El objetivo convencional es la altura de la base proyectada desde la ruptura: mide la parte más ancha de la figura y suma esa distancia al punto por donde el precio se fue.»
  - S046 [34w] «Es una forma razonable de elegir un primer objetivo porque mucha gente usa la misma, que es el mismo argumento autocumplido que hace m13 con el 0,618, y tiene la misma fecha de caducidad.»
  - S048 [46w] «Una cuña o un triángulo es la vela estrecha de m08-l2 a escala de patrón: veinte barras de compresión entre dos líneas que convergen, y las seis figuras con nombre son un solo objeto visto desde seis ángulos, separadas solo por cómo se reparte la convergencia.»
  - S049 [34w] «El «las cuñas ascendentes rompen a la baja» del canon son dos afirmaciones en una: el agotamiento de un ritmo es observable y real, la dirección en que se resuelve es estadística sin mecanismo.»
  - S050 [54w] «La compresión se resuelve en expansión porque eso es lo que la compresión es, pero una compresión que aún no se ha resuelto no es una señal: lee la ruptura por el cuerpo y el volumen, y trata el objetivo de la altura de la base como una convención y no como una promesa.»
- **9 Course-coined term** (4)
  - S028 [non-seed ritmo: "agotamiento observable de un ritmo" = the trend's rate of advance] «Eso es *agotamiento observable de un ritmo*, la misma lectura que te da la divergencia precio/volumen de m14, y dice algo real: quien esté comprando tiene que trabajar más para conseguir menos.»
  - S029 [non-seed ritmo: "el ritmo se está apagando"] «Dice que el ritmo se está apagando.»
  - S032 [non-seed ritmo: "el ritmo se acaba"] «La convergencia te dice que el ritmo se acaba; no te dice qué bando queda en pie cuando eso ocurra.»
  - S049 [non-seed ritmo: "el agotamiento de un ritmo es observable y real"] «El «las cuñas ascendentes rompen a la baja» del canon son dos afirmaciones en una: el agotamiento de un ritmo es observable y real, la dirección en que se resuelve es estadística sin mecanismo.»
- **10 Metaphor then gloss** (1)
  - S046 ["tiene la misma fecha de caducidad", glossed in S047 (nothing obliges the move to measure that)] «Es una forma razonable de elegir un primer objetivo porque mucha gente usa la misma, que es el mismo argumento autocumplido que hace m13 con el 0,618, y tiene la misma fecha de caducidad.»
- **11 Synonym rotation** (2)
  - S004 [pattern compression: líneas que se van cerrando (S004), convergencia (S009), compresión (S021)] 
  - S028 [buyers tiring: agotamiento observable de un ritmo (S028), el ritmo se está apagando (S029), el ritmo se acaba (S032), los compradores se están cansando (S036)] 

**EN** — 23 hits, 50 sentences, density 46.0

- **1 Filler** (2)
  - S009 [other: announcer "that is worth holding onto"] «What separates its members is how the convergence is shared between the two lines, and that is worth holding onto because it turns six named patterns into one object seen from six angles:»
  - S034 [exactly: emphatic "which is exactly what m13 says"] «It is statistics without a mechanism, which is exactly what m13 says about a Fibonacci ratio and m10-l1 about the 200-day average.»
- **2 Rhythmic triad** (1)
  - S001 [a small body / small wicks / a bar where almost nothing happened: the third restates the first two; drop it] «m08-l2 taught you a single candle whose range collapses: a small body, small wicks, a bar where almost nothing happened.»
- **4 Summary/uplift closer** (5)
  - S005 [restate: "Same mechanic, different scale" repeats S003] «Same mechanic, different scale — and, because it takes twenty bars instead of one, you can watch it happen.»
  - S008 [editorial: "That is the whole family."] «That is the whole family.»
  - S029 [restate: "It says the rhythm is running down" repeats S027–S028] «It says the rhythm is running down.»
  - S039 [editorial: "That much is not a prediction — it is what compression is"] «That much is not a prediction — it is what compression *is*, and it is the same statement m16 makes about a whole market regime.»
  - S047 [restate: last prose unit; repeats S045 "convention, not a promise"] «Nothing about a coil's opening width obliges the move that follows to be that size.»
- **5 Sentence over 30 words** (8)
  - S009 [33w] «What separates its members is how the convergence is shared between the two lines, and that is worth holding onto because it turns six named patterns into one object seen from six angles:»
  - S027 [36w] «In a rising wedge, buyers are making progress and it is costing them more each time: every new high is a smaller step, against a ceiling giving ground more slowly than the floor is gaining it.»
  - S028 [31w] «That is *observable exhaustion of a rhythm* — the same reading m14's price/ volume divergence gives you, and it says something real: whoever is buying is having to work harder for less.»
  - S033 [45w] «Every textbook percentage attached to this — the "68% of rising wedges resolve downward" kind — comes from a pattern somebody counted on a chart set they chose, with a definition of "wedge" they chose, and it is not built on a mechanism you can point at.»
  - S046 [37w] «It is a reasonable way to pick a first target because a lot of people use the same one, which is the same self-fulfilling argument m13 makes about the 0.618 — and it has the same expiry date.»
  - S048 [43w] «A wedge or a triangle is m08-l2's narrow candle at the scale of a pattern: twenty bars of compression between two converging lines, and the six named shapes are one object seen from six angles, separated only by how the convergence is shared.»
  - S049 [31w] «The canon's "rising wedges break down" is two claims in one coat — the exhaustion of a rhythm is observable and real, the direction it resolves in is statistics without a mechanism.»
  - S050 [43w] «Compression resolves into expansion because that is what compression is, but a coil that has not resolved yet is not a signal: read the break by the body and the volume, and treat the base-height target as a convention rather than a promise.»
- **9 Course-coined term** (4)
  - S028 [non-seed rhythm: "observable exhaustion of a rhythm" = the trend's rate of advance] «That is *observable exhaustion of a rhythm* — the same reading m14's price/ volume divergence gives you, and it says something real: whoever is buying is having to work harder for less.»
  - S029 [non-seed rhythm: "the rhythm is running down"] «It says the rhythm is running down.»
  - S032 [non-seed rhythm: "the rhythm is ending"] «The convergence tells you the rhythm is ending; it does not tell you which side is standing when it does.»
  - S049 [non-seed rhythm: "the exhaustion of a rhythm is observable and real"] «The canon's "rising wedges break down" is two claims in one coat — the exhaustion of a rhythm is observable and real, the direction it resolves in is statistics without a mechanism.»
- **10 Metaphor then gloss** (1)
  - S046 ["it has the same expiry date", glossed in S047 (nothing obliges the move to be that size)] «It is a reasonable way to pick a first target because a lot of people use the same one, which is the same self-fulfilling argument m13 makes about the 0.618 — and it has the same expiry date.»
- **11 Synonym rotation** (2)
  - S004 [pattern compression: lines closing on each other (S004), convergence (S009), coil (S021), compression (S038)] 
  - S028 [buyers tiring: observable exhaustion of a rhythm (S028), the rhythm is running down (S029), the rhythm is ending (S032), buyers are tiring (S036)] 

### m16-l1

**ES** — 28 hits, 65 sentences, density 43.1

- **1 Filler** (12)
  - S004 [de verdad: "información de verdad" — deletable; the contrast with "casi no lo sea" carries it] «Eso no es folclore: es una de las regularidades estadísticas más robustas de cualquier mercado negociado, y es la razón de que «lleva tres semanas en calma» sea información de verdad mientras que «lleva tres semanas subiendo» casi no lo sea.»
  - S010 [other: "Esa es toda la construcción." editorial tic] «Esa es toda la construcción.»
  - S014 [nada más: tag "y no es nada más"] «La anchura es una lectura de la volatilidad realizada, de lo que ya ha pasado, y no es nada más.»
  - S015 [Vale la pena: announcer "Vale la pena ser tajante con lo que no es"] «Vale la pena ser tajante con lo que *no* es, porque este indicador atrae más mitología que la mayoría.»
  - S022 [other: announcer "y ahí está lo interesante"] «Esas dos cosas se separan, y ahí está lo interesante.»
  - S026 [other: announcer sentence "Eso es lo que hace que merezca la pena dibujar esta comparación"] «Eso es lo que hace que merezca la pena dibujar esta comparación:»
  - S028 [de verdad: announcer sentence "Lee lo que dice de verdad esa condición"] «Lee lo que dice de verdad esa condición.»
  - S039 [Fíjate en: announcer] «Fíjate en lo que añade el panel: nada que el panel de precio de arriba no contenga ya.»
  - S043 [other: announcer "Esta es la desambiguación que hay que hacer bien"] «**Esta es la desambiguación que hay que hacer bien, porque la colisión es total y los dos mecanismos no tienen nada que ver el uno con el otro.**»
  - S057 [honesto: "Ese es el límite honesto."] «Ese es el límite honesto.»
  - S058 [exactamente: "exactamente igual que", emphatic] «Un squeeze es una afirmación sobre el *tamaño* del próximo movimiento, no sobre su dirección: exactamente igual que un interés abierto creciente te dice que se están añadiendo posiciones sin decirte de quién, y el funding te dice qué bando paga sin decirte qué bando tiene razón.»
  - S060 [fíjate en: announcer "Y fíjate en el modo de fallo"] «Y fíjate en el modo de fallo que sale directamente de ahí.»
- **2 Rhythmic triad** (1)
  - S046 [ningún participante forzado / ninguna liquidación / nadie en el lado equivocado: overlap; drop "nadie en el lado equivocado"] «No hay ningún participante forzado, ninguna liquidación, nadie en el lado equivocado.»
- **4 Summary/uplift closer** (2)
  - S042 [restate: S039 already said the panel adds nothing] «Cuando los puntos se apagan, las bandas ya te lo habían dicho.»
  - S053 [editorial: "los dos significados posibles difieren en si está pasando algo siquiera" restates S050–S052] «Si alguien dice «se está formando un squeeze», los dos significados posibles difieren en si está pasando algo siquiera.»
- **5 Sentence over 30 words** (9)
  - S004 [41w] «Eso no es folclore: es una de las regularidades estadísticas más robustas de cualquier mercado negociado, y es la razón de que «lleva tres semanas en calma» sea información de verdad mientras que «lleva tres semanas subiendo» casi no lo sea.»
  - S017 [40w] «Significa que el precio está dos desviaciones típicas por encima de su propia media reciente, que en un mercado en tendencia es donde vive el precio: el mismo error que m11 nombró para un RSI sobrecomprado, con otra envolvente encima.»
  - S025 [31w] «Ahora imagina una tendencia constante de barras pequeñas y ordenadas: el ATR es bajo y los cierres están repartidos a lo largo de todo el movimiento, así que es al revés.»
  - S034 [32w **aside-only** (30w without asides)] «Luego los cierres se juntan mientras las barras siguen moviéndose, la banda de Bollinger se mete dentro —el squeeze— y el precio se queda cerca de 1.902 sin ir a ninguna parte.»
  - S036 [49w] «La versión empaquetada que te encontrarás con nombres como *Squeeze Momentum* pone las dos ideas en un solo panel: una fila de puntos sobre una línea de cero que indica si el squeeze está activo, y un histograma con signo que muestra la dirección y la fuerza del movimiento.»
  - S058 [47w] «Un squeeze es una afirmación sobre el *tamaño* del próximo movimiento, no sobre su dirección: exactamente igual que un interés abierto creciente te dice que se están añadiendo posiciones sin decirte de quién, y el funding te dice qué bando paga sin decirte qué bando tiene razón.»
  - S062 [43w] ««El squeeze está a punto de dispararse» no es una dirección, así que una posición dimensionada como si lo fuera es una posición dimensionada a partir de nada, que es m22, la gestión del riesgo, y m26, la psicología del error, otra vez.»
  - S064 [46w] «Bollinger mide cuánto se dispersan los cierres y Keltner cuánto recorre una barra, y lo interesante es que las dos reglas se separen: cuando la banda de Bollinger queda enteramente dentro del canal de Keltner el mercado está en squeeze, y la salida es la expansión.»
  - S065 [38w] «La compresión dice que viene una expansión y nunca dice hacia dónde, así que la dirección la lees de la ruptura; y mantén este squeeze aparte del de liquidez de m19-l2, que comparte la palabra y ningún mecanismo.»
- **9 Course-coined term** (3)
  - S047 [non-seed squeeze de liquidez: used for a short squeeze/liquidation cascade; standard "liquidity squeeze" = funding/credit crunch] «Squeeze de liquidez / short squeeze (m19-l2): un *suceso de mercado*.»
  - S048 [seed bolsa de liquidez (as "bolsa de liquidaciones de cortos"): cluster of short liquidation prices] «El precio sube hasta una bolsa de liquidaciones de cortos, esos cortos se recompran a la fuerza, esa compra empuja el precio más arriba y eso liquida más cortos.»
  - S065 [non-seed squeeze de liquidez: "el de liquidez de m19-l2"] «La compresión dice que viene una expansión y nunca dice hacia dónde, así que la dirección la lees de la ruptura; y mantén este squeeze aparte del de liquidez de m19-l2, que comparte la palabra y ningún mecanismo.»
- **10 Metaphor then gloss** (1)
  - S041 ["leerlo como un oráculo", glossed: "es leer el reempaquetado de dos medias como si supiera algo"] «Es una comodidad —un panel en vez de cuatro líneas— y leerlo como un oráculo es leer el reempaquetado de dos medias como si supiera algo.»
- **A absolutes** (1)
  - S065 [nunca, summary] «La compresión dice que viene una expansión y nunca dice hacia dónde, así que la dirección la lees de la ruptura; y mantén este squeeze aparte del de liquidez de m19-l2, que comparte la palabra y ningún mecanismo.»

**EN** — 28 hits, 64 sentences, density 43.8

- **1 Filler** (12)
  - S004 [genuine: "genuine information" — deletable; the contrast with "mostly is not" carries it] «That is not a piece of folklore — it is one of the most robust statistical regularities in any traded market, and it is why "it has been calm for three weeks" is genuine information while "it went up for three weeks" mostly is not.»
  - S010 [other: "That is the whole construction." editorial tic] «That is the whole construction.»
  - S014 [other: tag "and that is all it is"] «The width is a read of realized volatility — of what already happened — and that is all it is.»
  - S015 [other: announcer "It is worth being blunt about what it is not"] «It is worth being blunt about what it is *not*, because this indicator attracts more mythology than most.»
  - S022 [other: announcer "the way they come apart is the point"] «Those come apart, and the way they come apart is the point.»
  - S026 [other: announcer sentence "That is what makes this comparison worth drawing at all"] «That is what makes this comparison worth drawing at all:»
  - S028 [actually: announcer sentence "Read what that condition actually says"] «Read what that condition actually says.»
  - S039 [other: announcer "Notice what the pane adds"] «Notice what the pane adds: nothing the price panel above it does not already contain.»
  - S043 [other: announcer "This is the disambiguation to get right"] «**This is the disambiguation to get right, because the collision is total and the two mechanisms have nothing to do with each other.**»
  - S056 [honest: "That is the honest limit."] «That is the honest limit.»
  - S057 [exactly: "exactly as", emphatic] «A squeeze is a statement about the *size* of the next move, not its direction — exactly as rising open interest tells you positions are being added without saying by whom, and funding tells you which side is paying without saying which side is right.»
  - S059 [other: announcer "And note the failure mode"] «And note the failure mode that follows directly.»
- **2 Rhythmic triad** (1)
  - S046 [no forced participant / no liquidation / nobody on the wrong side: overlap; drop "nobody on the wrong side"] «There is no forced participant, no liquidation, nobody on the wrong side.»
- **4 Summary/uplift closer** (2)
  - S042 [restate: S039 already said the pane adds nothing] «When the dots go dim, the bands had already told you.»
  - S052 [editorial: "the two possible meanings differ on whether anything is happening at all" restates S049–S051] «If somebody says "there's a squeeze setting up", the two possible meanings differ on whether anything is happening at all.»
- **5 Sentence over 30 words** (9)
  - S004 [44w] «That is not a piece of folklore — it is one of the most robust statistical regularities in any traded market, and it is why "it has been calm for three weeks" is genuine information while "it went up for three weeks" mostly is not.»
  - S017 [34w] «It means price is two standard deviations above its own recent mean, which in a trending market is where price lives — the same error m11 named for an overbought RSI, wearing a different envelope.»
  - S025 [32w] «Now picture a steady trend of small, orderly bars: the ATR is low and the closes are strung out all the way up the move, so it is the other way round.»
  - S036 [44w] «The packaged version you will meet under names like *Squeeze Momentum* puts the two ideas in one pane: a row of dots on a zero line showing whether the squeeze is on, and a signed histogram showing the direction and force of the move.»
  - S047 [31w **aside-only** (30w without asides)] «Liquidity squeeze / short squeeze (m19-l2): a *market event* — price rises into a pocket of short liquidations, those shorts are forcibly bought back, that buying pushes price higher, which liquidates more shorts.»
  - S057 [44w] «A squeeze is a statement about the *size* of the next move, not its direction — exactly as rising open interest tells you positions are being added without saying by whom, and funding tells you which side is paying without saying which side is right.»
  - S061 [36w] «"The squeeze is about to fire" is not a direction, so a position sized as though it were is a position sized on nothing — which is m22, risk management, and m26, the psychology of mistakes, again.»
  - S063 [47w] «Bollinger measures how far the closes scatter and Keltner how far a bar travels, and the two rulers coming apart is the point: when the Bollinger band sits entirely inside the Keltner channel the market is in a squeeze, and the exit from it is the expansion.»
  - S064 [38w] «Compression says an expansion is coming and never says which way, so read the direction from the break — and keep this squeeze apart from the liquidity squeeze of m19-l2, which shares the word and no mechanism at all.»
- **8 Repeated paragraph opener** (1)
  - S004 ["That is" ×4 (S004, S010, S026, S056)] 
- **9 Course-coined term** (2)
  - S047 [non-seed liquidity squeeze: used for a short squeeze/liquidation cascade; standard "liquidity squeeze" = funding/credit crunch; same sentence has seed "pocket of short liquidations"] «Liquidity squeeze / short squeeze (m19-l2): a *market event* — price rises into a pocket of short liquidations, those shorts are forcibly bought back, that buying pushes price higher, which liquidates more shorts.»
  - S064 [non-seed liquidity squeeze: "the liquidity squeeze of m19-l2"] «Compression says an expansion is coming and never says which way, so read the direction from the break — and keep this squeeze apart from the liquidity squeeze of m19-l2, which shares the word and no mechanism at all.»
- **10 Metaphor then gloss** (1)
  - S041 ["reading it as an oracle", glossed: "is reading a repackaging of two averages as though it knew something"] «It is a convenience — one pane instead of four lines — and reading it as an oracle is reading a repackaging of two averages as though it knew something.»
- **A absolutes** (1)
  - S064 [never, summary] «Compression says an expansion is coming and never says which way, so read the direction from the break — and keep this squeeze apart from the liquidity squeeze of m19-l2, which shares the word and no mechanism at all.»

### m17-l1

**ES** — 58 hits, 100 sentences, density 58.0

- **1 Filler** (7)
  - S011 [other: announcer sentence "Aquí está la parte que atrapa a la gente, con números"] «Aquí está la parte que atrapa a la gente, con números.»
  - S016 [simplemente: tic] «A Bitcoin no le pasó nada bueno; las alts simplemente sangraron más rápido.»
  - S033 [claramente: intensifier; 0,05 → 0,059 already shows it] «Si en cambio Ether hubiera corrido hasta 2.600 mientras Bitcoin solo llegaba a 44.000, el ratio sería `2.600 / 44.000 = 0,059`, claramente al alza: Ether rinde mejor, el apetito se calienta.»
  - S075 [precisamente: emphatic "precisamente porque"] «A veces se pasa de frenada, precisamente porque reacciona en solitario.»
  - S091 [other: "justo cuando los querrías profundos", emphatic justo] «En los minutos previos a una publicación conocida, los creadores de mercado que normalmente cotizan un libro profundo retiran sus órdenes para que la reacción no los arrolle, así que los spreads se ensanchan y el libro se afina justo cuando los querrías profundos.»
  - S094 [other: announcer "la regla es sencilla:"] «Así que la regla es sencilla: ponte plano o pequeño ante un evento que no puedes valorar.»
  - S097 [de verdad: emphatic "los que de verdad puedes leer"] «Reduce el tamaño o hazte a un lado; los setups que merece la pena operar son los que de verdad puedes leer.»
- **2 Rhythmic triad** (3)
  - S009 [más líquido / más listado / más comprendido: "más listado" overlaps "más líquido"; drop it] «El capital nuevo que llega a cripto tiende a entrar primero por Bitcoin: es el activo más líquido, más listado y más comprendido, la reserva del espacio y la compra natural de quien acaba de entrar.»
  - S050 [los últimos / con más fuerza / de la forma más seductora: third is rhythm; drop "de la forma más seductora"] «Un token de pequeña capitalización tiene poco capital dentro, así que la misma entrada de dinero que mueve a Bitcoin un pequeño porcentaje puede duplicar un micro-cap, y por eso los tokens pequeños suben los últimos, con más fuerza y de la forma más seductora.»
  - S076 [las instituciones / los creadores de mercado / buena parte del flujo profesional: third overlaps the first two; drop it] «El volumen se adelgaza los fines de semana: las instituciones, los creadores de mercado y buena parte del flujo profesional se retiran.»
- **3 Rhetorical question** (3)
  - S007 «¿Por qué importa siquiera una cuota?»
  - S026 «¿Por qué cotizar una cripto frente a otra en vez de frente al dólar?»
  - S046 «¿Por qué viaja el capital en este orden y no todo a la vez?»
- **4 Summary/uplift closer** (7)
  - S003 [ahead: "Este módulo trata de leer esa marea..." module overview] «Este módulo trata de leer esa marea: dónde está el dinero, hacia dónde tiende a fluir después y cómo respira todo el espacio al compás de la economía tradicional que hay fuera.»
  - S006 [editorial: "y ese único hecho es el origen de casi todos los errores"; "proporción" repeats "cuota"] «Es una *proporción*, no un precio, y ese único hecho es el origen de casi todos los errores que se cometen con ella.»
  - S017 [editorial: "La misma aritmética, y es la razón por la que..."] «La misma aritmética, y es la razón por la que dominancia y precio no son la misma afirmación.»
  - S024 [restate: "El mismo número, el ánimo opuesto" repeats S021–S023] «El mismo número, el ánimo opuesto; el mercado total es lo que los distingue.»
  - S082 [motivate: "ese contexto merece tenerse antes de mirar siquiera un solo gráfico"] «Lo que te dan es el tiempo meteorológico —una idea de si operas con el viento a favor o de cara—, y ese contexto merece tenerse antes de mirar siquiera un solo gráfico.»
  - S093 [restate: "La liquidez de la que dependes se evapora con horario" repeats S090–S092] «La liquidez de la que dependes se evapora con horario.»
  - S097 [restate/motivate: last prose unit; repeats S094's rule, ends on "los que de verdad puedes leer"] «Reduce el tamaño o hazte a un lado; los setups que merece la pena operar son los que de verdad puedes leer.»
- **5 Sentence over 30 words** (28)
  - S002 [48w] «El capital no se queda quieto en cripto: se mueve entre Bitcoin, las grandes alternativas y la larga cola de tokens pequeños siguiendo patrones que se repiten lo bastante como para merecer conocerlos, y de forma lo bastante irregular como para que nunca los trates como un reloj.»
  - S003 [32w] «Este módulo trata de leer esa marea: dónde está el dinero, hacia dónde tiende a fluir después y cómo respira todo el espacio al compás de la economía tradicional que hay fuera.»
  - S009 [36w] «El capital nuevo que llega a cripto tiende a entrar primero por Bitcoin: es el activo más líquido, más listado y más comprendido, la reserva del espacio y la compra natural de quien acaba de entrar.»
  - S010 [39w] «Así que el dinero que entra suele aparecer como dominancia *al alza* antes que en ningún otro sitio; el dinero que se vuelve atrevido aparece como dominancia *a la baja* a medida que se reparte hacia todo lo demás.»
  - S019 [41w] «Ocurre en dos estados de ánimo opuestos: una huida risk-off, en la que los traders venden alts por la seguridad relativa de BTC, y la primera parte de un mercado alcista, en la que el dinero nuevo entra primero por Bitcoin.»
  - S028 [38w] «Casi todo en cripto sube y baja *con* Bitcoin en cierta medida; medir Ether en BTC cancela ese movimiento común y deja solo la parte que es Ether ganando o perdiendo terreno específicamente frente al activo de reserva.»
  - S034 [34w] «Un ETH/BTC al alza significa que Ether rinde mejor que Bitcoin; suele leerse como un apetito por el riesgo que se calienta, dinero dispuesto a salir del activo de reserva hacia el siguiente peldaño.»
  - S050 [45w] «Un token de pequeña capitalización tiene poco capital dentro, así que la misma entrada de dinero que mueve a Bitcoin un pequeño porcentaje puede duplicar un micro-cap, y por eso los tokens pequeños suben los últimos, con más fuerza y de la forma más seductora.»
  - S051 [57w] «Cuando vuelve el miedo, la rotación funciona a la inversa: el dinero sube de nuevo por la curva hacia Bitcoin, y los tokens más pequeños y menos líquidos sangran primero y peor: el libro poco profundo que amplificó la subida amplifica la caída, y a menudo no hay ninguna orden de compra (bid) a la que vender.»
  - S055 [35w] «Las alts grandes reciben compras; luego, en las últimas semanas, alts pequeñas y desconocidas se triplican mientras la multitud declara permanente la "alt season", con la dominancia tocando fondo justo cuando el riesgo hace techo.»
  - S059 [44w] «En los últimos años Bitcoin ha cotizado en gran medida como un activo risk-on: sube cuando los inversores están cómodos asumiendo riesgos riesgo y baja cuando huyen hacia la seguridad, moviéndose en sintonía laxa con las acciones tecnológicas en vez de en su contra.»
  - S062 [44w] «Cuando los bancos centrales los suben, el efectivo y los bonos de Estado a corto plazo pagan más por cero riesgo, así que todo activo especulativo —cripto muy incluida— tiene que competir contra un rendimiento sin riesgo más alto y parece relativamente menos atractivo.»
  - S065 [31w] «La demostración reciente más clara fue 2022: los bancos centrales subieron los tipos con fuerza para combatir la inflación y cripto cayó con dureza al mismo compás que las acciones tecnológicas.»
  - S068 [40w **aside-only** (21w without asides)] «Un dólar al alza endurece las condiciones financieras globales —los dólares se vuelven más escasos y valiosos, y los activos de riesgo cotizados en dólares tienden a debilitarse—; un dólar a la baja las relaja y suele coincidir con fortaleza.»
  - S071 [43w] «Las relaciones macro anteriores las comparte con las acciones, pero cripto reacciona a ellas de forma distinta por una razón estructural: cotiza 24 horas al día, 7 días a la semana, mientras que los mercados de acciones y bonos guardan horario de oficina.»
  - S073 [31w **aside-only** (17w without asides)] «UU. (un dato de inflación, un informe de empleo, una decisión de un banco central) se publica en horario de Wall Street, cripto salta en el mismo instante que las acciones.»
  - S074 [56w] «Pero cuando la noticia salta de noche o en fin de semana —la quiebra de un banco, un shock geopolítico—, cripto es a menudo el *único* mercado grande y líquido abierto, así que se mueve primero y se convierte en un indicador en vivo del apetito global por el riesgo hasta que reabren los mercados tradicionales.»
  - S077 [36w] «La misma orden mueve el precio más lejos dentro de un libro poco profundo, así que los movimientos de fin de semana pueden exagerarse y luego deshacerse en parte cuando la liquidez plena vuelve el lunes.»
  - S078 [42w] «Los mercados regulados que *sí* cierran, como los futuros de Bitcoin de CME, reabren con un hueco respecto a donde derivó el precio al contado durante el fin de semana, un hueco que suele rellenarse en las primeras horas de la semana.»
  - S082 [33w **aside-only** (20w without asides)] «Lo que te dan es el tiempo meteorológico —una idea de si operas con el viento a favor o de cara—, y ese contexto merece tenerse antes de mirar siquiera un solo gráfico.»
  - S085 [32w] «Importan dos capas del reloj: los *eventos* del calendario, aquí abajo, y el ritmo diario y semanal recurrente de cuándo hay liquidez de verdad, que es el mapa de sesiones de m23-l1.»
  - S088 [40w] «Los eventos propios de cripto son la misma idea desde dentro: un gran unlock de tokens (ver m20) suelta nueva oferta en una fecha publicada, y los incidentes de exchange (una caída, un delisting, un depeg) golpean el mercado directamente.»
  - S091 [44w] «En los minutos previos a una publicación conocida, los creadores de mercado que normalmente cotizan un libro profundo retiran sus órdenes para que la reacción no los arrolle, así que los spreads se ensanchan y el libro se afina justo cuando los querrías profundos.»
  - S092 [31w] «Una orden a mercado en ese hueco se ejecuta lejos de donde esperabas, y un stop puede saltarse limpiamente cuando el precio pega un salto hasta la siguiente orden en reposo.»
  - S096 [39w] «Y nunca te sientes *justo dentro de una repisa de liquidación ante un anuncio*: una posición apalancada cuyo precio de liquidación queda pasado un cúmulo visible de stops (ver m19-l2) es combustible esperando la chispa que aporta el dato.»
  - S098 [44w] «La dominancia de Bitcoin es una cuota, no un precio: puede subir del 50% al 56% mientras el propio Bitcoin cae un 10%, porque las alts sangraron más rápido, así que solo significa algo leída junto a si el mercado total sube o baja.»
  - S099 [40w] «El ratio ETH/BTC elimina el movimiento que todo el espacio comparte y sirve de termómetro del apetito por el riesgo, y el capital tiende a rotar BTC → ETH → alts grandes → alts pequeñas, que es una tendencia y nunca un calendario.»
  - S100 [48w] «Cripto cotiza como activo risk-on frente a los tipos y al dólar, no cierra nunca y por eso reacciona sola a la macro de noche y en fin de semana, y parte de la volatilidad está programada: ponte plano o pequeño ante un evento que no puedes valorar.»
- **6 Stacked hedge** (1)
  - S062 [parece + relativamente] «Cuando los bancos centrales los suben, el efectivo y los bonos de Estado a corto plazo pagan más por cero riesgo, así que todo activo especulativo —cripto muy incluida— tiene que competir contra un rendimiento sin riesgo más alto y parece relativamente menos atractivo.»
- **8 Repeated paragraph opener** (1)
  - S007 ["¿Por qué" ×3 (S007, S026, S046)] 
- **9 Course-coined term** (3)
  - S079 [lente [seed]] «Todo lo anterior es una lente para el *contexto*, y cada parte se convierte en una forma de perder dinero en cuanto lo tratas como una señal para actuar directamente.»
  - S096 [repisa [seed]] «Y nunca te sientes *justo dentro de una repisa de liquidación ante un anuncio*: una posición apalancada cuyo precio de liquidación queda pasado un cúmulo visible de stops (ver m19-l2) es combustible esperando la chispa que aporta el dato.»
  - S096 [combustible [seed]] «Y nunca te sientes *justo dentro de una repisa de liquidación ante un anuncio*: una posición apalancada cuyo precio de liquidación queda pasado un cúmulo visible de stops (ver m19-l2) es combustible esperando la chispa que aporta el dato.»
- **10 Metaphor then gloss** (3)
  - S001 ["una marea mayor", glossed in S002 (el capital se mueve entre Bitcoin, alts...)] «Cuando operas una moneda estás operando también, te guste o no, su lugar dentro de una marea mayor.»
  - S036 ["Es un termómetro, no un detonante", glossed in S037 (te dice la temperatura...; no el minuto en que actuar)] «Es un termómetro, no un detonante.»
  - S082 ["el tiempo meteorológico", glossed inside the dashes (viento a favor o de cara)] «Lo que te dan es el tiempo meteorológico —una idea de si operas con el viento a favor o de cara—, y ese contexto merece tenerse antes de mirar siquiera un solo gráfico.»
- **11 Synonym rotation** (2)
  - S001 [capital rotation: marea (S001), fluir (S003), viaja el capital (S046), rotación (S051)] 
  - S010 [risk appetite/mood: el dinero que se vuelve atrevido (S010), estados de ánimo (S019), ánimo (S024), apetito por el riesgo (S029), confianza (S043)] 
- **A absolutes** (5)
  - S002 [nunca] «El capital no se queda quieto en cripto: se mueve entre Bitcoin, las grandes alternativas y la larga cola de tokens pequeños siguiendo patrones que se repiten lo bastante como para merecer conocerlos, y de forma lo bastante irregular como para que nunca los trates como un reloj.»
  - S021 [siempre] «Como la dominancia es una *cuota*, siempre hay que leerla junto a si el mercado total sube o baja.»
  - S096 [nunca] «Y nunca te sientes *justo dentro de una repisa de liquidación ante un anuncio*: una posición apalancada cuyo precio de liquidación queda pasado un cúmulo visible de stops (ver m19-l2) es combustible esperando la chispa que aporta el dato.»
  - S099 [nunca, summary] «El ratio ETH/BTC elimina el movimiento que todo el espacio comparte y sirve de termómetro del apetito por el riesgo, y el capital tiende a rotar BTC → ETH → alts grandes → alts pequeñas, que es una tendencia y nunca un calendario.»
  - S100 [nunca, summary] «Cripto cotiza como activo risk-on frente a los tipos y al dólar, no cierra nunca y por eso reacciona sola a la macro de noche y en fin de semana, y parte de la volatilidad está programada: ponte plano o pequeño ante un evento que no puedes valorar.»

**EN** — 50 hits, 99 sentences, density 50.5

- **1 Filler** (9)
  - S011 [other: announcer sentence "Here is the part that traps people, shown with numbers"] «Here is the part that traps people, shown with numbers.»
  - S016 [simply: tic] «Nothing good happened to Bitcoin; the alts simply bled faster.»
  - S033 [other: "clearly" intensifier; 0.05 → 0.059 already shows it] «If instead Ether had run to 2,600 while Bitcoin only reached 44,000, the ratio would be `2,600 / 44,000 = 0.059`, clearly rising: Ether outperforming, appetite warming.»
  - S050 [exactly: emphatic "which is exactly why"] «A small-cap token has little capital sitting in it, so the same inflow that nudges Bitcoin a few percent can double a micro-cap — which is exactly why small tokens moon last, hardest, and most seductively.»
  - S074 [precisely: emphatic "precisely because"] «It sometimes overshoots, precisely because it is reacting alone.»
  - S084 [actually: "when liquidity is actually present", emphatic] «Two layers of the clock matter: the *events* on the calendar, below — and the recurring daily and weekly rhythm of when liquidity is actually present, which is the session map in m23-l1.»
  - S090 [exactly: "exactly when you would want them deep", emphatic] «In the minutes ahead of a known release the market makers who normally quote a tight, deep book pull their orders rather than be run over by the reaction — so spreads widen and the book thins exactly when you would want them deep.»
  - S093 [other: announcer "the rule is simple:"] «So the rule is simple: be flat or small around an event you cannot price.»
  - S096 [actually: emphatic "the ones you can actually read"] «Cut size or step aside; the setups worth trading are the ones you can actually read.»
- **2 Rhythmic triad** (3)
  - S009 [most liquid / most widely listed / most understood: "most widely listed" overlaps "most liquid"; drop it] «Fresh capital arriving in crypto tends to enter through Bitcoin first — it is the most liquid, most widely listed and most understood asset, the reserve of the space and the natural first purchase for someone stepping in.»
  - S050 [last / hardest / most seductively: third is rhythm; drop "most seductively"] «A small-cap token has little capital sitting in it, so the same inflow that nudges Bitcoin a few percent can double a micro-cap — which is exactly why small tokens moon last, hardest, and most seductively.»
  - S075 [institutions / market makers / much of the professional flow: third overlaps the first two; drop it] «Volume thins out on weekends: institutions, market makers and much of the professional flow step back.»
- **3 Rhetorical question** (3)
  - S007 «Why does a share matter at all?»
  - S026 «Why quote one crypto in terms of another instead of in dollars?»
  - S046 «Why does capital travel in this order rather than all at once?»
- **4 Summary/uplift closer** (7)
  - S003 [ahead: "This module is about reading that tide..." module overview] «This module is about reading that tide: where money sits, where it tends to flow next, and how the whole space breathes with the traditional economy outside it.»
  - S006 [editorial: "that single fact is the source of almost every mistake"; "ratio" repeats "share"] «It is a *ratio*, not a price, and that single fact is the source of almost every mistake made with it.»
  - S017 [editorial: "Same arithmetic, and it is why..."] «Same arithmetic, and it is why dominance and price are not the same statement.»
  - S024 [restate: "Same number, opposite mood" repeats S021–S023] «Same number, opposite mood; the total market is what tells them apart.»
  - S081 [motivate: "that context is worth having before you ever look at a single chart"] «What they give you is the weather — a sense of whether you are trading with the wind at your back or in your face — and that context is worth having before you ever look at a single chart.»
  - S092 [restate: "The liquidity you rely on evaporates on schedule" repeats S089–S091] «The liquidity you rely on evaporates on schedule.»
  - S096 [restate/motivate: last prose unit; repeats S093's rule, ends on "the ones you can actually read"] «Cut size or step aside; the setups worth trading are the ones you can actually read.»
- **5 Sentence over 30 words** (20)
  - S002 [43w] «Capital does not sit still in crypto: it moves between Bitcoin, the big alternatives and the long tail of small tokens in patterns that repeat often enough to be worth knowing — and irregularly enough that you must never treat them as a clock.»
  - S009 [37w] «Fresh capital arriving in crypto tends to enter through Bitcoin first — it is the most liquid, most widely listed and most understood asset, the reserve of the space and the natural first purchase for someone stepping in.»
  - S019 [34w] «That happens in two opposite moods: a risk-off flight, where traders sell alts for the relative safety of BTC, and the early part of a bull run, where fresh money enters through Bitcoin first.»
  - S028 [37w] «Almost everything in crypto rises and falls *with* Bitcoin to some degree; pricing Ether in BTC cancels that common move and leaves only the part that is Ether specifically gaining or losing ground against the reserve asset.»
  - S050 [35w] «A small-cap token has little capital sitting in it, so the same inflow that nudges Bitcoin a few percent can double a micro-cap — which is exactly why small tokens moon last, hardest, and most seductively.»
  - S051 [45w] «When fear returns the rotation runs in reverse: money climbs back up the curve toward Bitcoin, and the smallest, least liquid tokens bleed first and worst — the thin book that amplified the rise amplifies the fall, and there is often no bid to sell into.»
  - S059 [40w] «Over the last several years Bitcoin has traded largely as a risk-on asset: it rises when investors are happy to hold risk and falls when they flee to safety, moving in loose sympathy with tech stocks rather than against them.»
  - S062 [35w] «When central banks raise them, cash and short-term government bonds pay more for zero risk, so every speculative asset — crypto very much included — must compete against a higher risk-free return and looks relatively less attractive.»
  - S068 [31w] «A rising dollar tightens global financial conditions — dollars become scarcer and more valuable, and dollar-priced risk assets tend to weaken; a falling dollar loosens them and tends to coincide with strength.»
  - S071 [36w] «The macro relationships above are shared with stocks, but crypto reacts to them differently for one structural reason: it trades 24 hours a day, 7 days a week, while stock and bond markets keep office hours.»
  - S073 [42w] «But when news breaks at night or over a weekend — a bank failure, a geopolitical shock — crypto is often the *only* large, liquid market open, so it moves first and becomes a live proxy for global risk sentiment until traditional markets reopen.»
  - S077 [34w] «Regulated venues that *do* close, such as CME Bitcoin futures, reopen with a gap to wherever spot drifted over the weekend — a gap that often gets filled in the first hours of the week.»
  - S081 [38w **aside-only** (21w without asides)] «What they give you is the weather — a sense of whether you are trading with the wind at your back or in your face — and that context is worth having before you ever look at a single chart.»
  - S084 [32w] «Two layers of the clock matter: the *events* on the calendar, below — and the recurring daily and weekly rhythm of when liquidity is actually present, which is the session map in m23-l1.»
  - S087 [34w **aside-only** (26w without asides)] «Crypto-native events are the same idea from inside: a large token unlock (see m20) drops new supply on a published date, and exchange incidents (an outage, a delisting, a depeg) hit the tape directly.»
  - S090 [43w] «In the minutes ahead of a known release the market makers who normally quote a tight, deep book pull their orders rather than be run over by the reaction — so spreads widen and the book thins exactly when you would want them deep.»
  - S095 [36w] «And never sit *just inside a liquidation shelf into an announcement*: a leveraged position whose liquidation price is parked past a visible cluster of stops (see m19-l2) is fuel waiting for the spark the print provides.»
  - S097 [40w] «Bitcoin dominance is a share, not a price: it can rise 50% to 56% while Bitcoin itself falls 10%, because the alts bled faster — so it only means something read next to whether the total market is rising or falling.»
  - S098 [38w] «The ETH/BTC ratio strips out the move the whole space shares and works as a thermometer for risk appetite, and capital tends to rotate BTC → ETH → large caps → small caps, which is a tendency and never a timetable.»
  - S099 [40w] «Crypto trades as a risk-on asset against rates and the dollar, it never closes so it reacts to macro alone at night and at weekends, and some volatility is scheduled: be flat or small into an event you cannot price.»
- **9 Course-coined term** (3)
  - S078 [lens [seed]] «Everything above is a lens for *context*, and each part of it becomes a way to lose money the moment you treat it as a signal to act on directly.»
  - S095 [shelf [seed]] «And never sit *just inside a liquidation shelf into an announcement*: a leveraged position whose liquidation price is parked past a visible cluster of stops (see m19-l2) is fuel waiting for the spark the print provides.»
  - S095 [fuel [seed]] «And never sit *just inside a liquidation shelf into an announcement*: a leveraged position whose liquidation price is parked past a visible cluster of stops (see m19-l2) is fuel waiting for the spark the print provides.»
- **10 Metaphor then gloss** (3)
  - S001 ["a larger tide", glossed in S002 (capital moves between Bitcoin, alts...)] «When you trade one coin you are also, whether you like it or not, trading its place inside a larger tide.»
  - S036 ["It is a thermometer, not a trigger", glossed in S037 (tells you the temperature...; not the minute to act)] «It is a thermometer, not a trigger.»
  - S081 ["the weather", glossed inside the dashes (wind at your back or in your face)] «What they give you is the weather — a sense of whether you are trading with the wind at your back or in your face — and that context is worth having before you ever look at a single chart.»
- **11 Synonym rotation** (2)
  - S001 [capital rotation: tide (S001), flow (S003), capital travel (S046), rotation (S051)] 
  - S010 [risk appetite/mood: money getting adventurous (S010), moods (S019), mood (S024), risk appetite (S029), confidence (S043)] 
- **A absolutes** (6)
  - S002 [must, never] «Capital does not sit still in crypto: it moves between Bitcoin, the big alternatives and the long tail of small tokens in patterns that repeat often enough to be worth knowing — and irregularly enough that you must never treat them as a clock.»
  - S021 [must, always] «Because dominance is a *share*, you must always read it next to whether the total market is rising or falling.»
  - S062 [must] «When central banks raise them, cash and short-term government bonds pay more for zero risk, so every speculative asset — crypto very much included — must compete against a higher risk-free return and looks relatively less attractive.»
  - S095 [never] «And never sit *just inside a liquidation shelf into an announcement*: a leveraged position whose liquidation price is parked past a visible cluster of stops (see m19-l2) is fuel waiting for the spark the print provides.»
  - S098 [never, summary] «The ETH/BTC ratio strips out the move the whole space shares and works as a thermometer for risk appetite, and capital tends to rotate BTC → ETH → large caps → small caps, which is a tendency and never a timetable.»
  - S099 [never, summary] «Crypto trades as a risk-on asset against rates and the dollar, it never closes so it reacts to macro alone at night and at weekends, and some volatility is scheduled: be flat or small into an event you cannot price.»

### m18-l1

**ES** — 47 hits, 80 sentences, density 58.8

- **1 Filler** (11)
  - S004 [exactamente: emphatic "sabes exactamente qué mide"] «La más conocida en cripto es el índice de miedo y codicia y, como toda herramienta de este curso, solo es útil cuando sabes exactamente qué mide y qué no.»
  - S022 [Fíjate: announcer "Fíjate bien en los dos primeros ingredientes"] «Fíjate bien en los dos primeros ingredientes.»
  - S025 [other: announcer "Eso es lo más importante que debes recordar de él:"] «Eso es lo más importante que debes recordar de él: *no* es una segunda opinión independiente que confirme lo que hace el precio.»
  - S030 [fíjate en: announcer] «Pero fíjate en lo que ocurrió de verdad: el precio al subir *alimentó la mayoría de esos ingredientes*.»
  - S030 [de verdad: emphatic "lo que ocurrió de verdad"] «Pero fíjate en lo que ocurrió de verdad: el precio al subir *alimentó la mayoría de esos ingredientes*.»
  - S041 [honesta: "sencilla y honesta" applied to a logic] «La lógica contraria es sencilla y honesta: si casi todo el que quería comprar ya ha comprado, quedan pocos compradores para empujar el precio más arriba, y muchos largos tardíos y nerviosos que venderán rápido a la primera caída.»
  - S053 [other: tic "De nuevo, eso sí:"] «De nuevo, eso sí: esto es una zona de interés, un sitio donde *buscar* setups, no una orden de comprar.»
  - S054 [other: announcer sentence "Este es el error que le cuesta dinero a la gente."] «Este es el error que le cuesta dinero a la gente.»
  - S061 [de verdad: "para entrar de verdad", emphatic] «El trigger para entrar de verdad tiene que venir de tus propias herramientas: estructura, un nivel, confirmación.»
  - S064 [exactamente: emphatic "son exactamente la forma en que"] «"Índice en 8, a comprar a saco" e "índice en 92, a cortar" son exactamente la forma en que los contrarios acaban liquidados antes de tiempo: se plantan delante de una tendencia que todavía se está alimentando, apoyados en un número que solo dice que la masa está desequilibrada, no que el desequilibrio esté a punto de terminar.»
  - S073 [precisamente: emphatic "se nutren precisamente de esas cosas"] «Un solo hilo viral, la llamada de un influencer o el listado en un nuevo exchange pueden disparar a la vez el volumen social, el interés de búsqueda y el precio, y recuerda que tres de los ingredientes del índice se nutren precisamente de esas cosas, así que una sola narrativa puede empujar todo el indicador a codicia extrema muy rápido.»
- **2 Rhythmic triad** (4)
  - S039 [confiada / apalancada / ya larga: "confiada" repeats "eufórica"; drop it] «Cuando el índice está en codicia extrema, la masa está eufórica: confiada, apalancada y ya larga.»
  - S043 [reduce tamaño / aprieta el riesgo / deja de perseguir el precio: first two overlap; drop "aprieta el riesgo"] «Así que la codicia extrema no significa "vende ahora": significa el terreno está saturado: reduce tamaño, aprieta el riesgo y deja de perseguir el precio.»
  - S052 [pánico / ventas forzosas / un pico de miedo: "pánico" and "pico de miedo" overlap; drop "pánico"] «Ese lavado —pánico, ventas forzosas y un pico de miedo, todo a la vez— es lo que puede ser un suelo de capitulación.»
  - S077 [más local / más rápido / más extremo: third for rhythm (S076 already said "con violencia"); drop "más extremo"] «En las alts, el sentimiento es aún más local, más rápido y más extremo de lo que sugiere el único número del panel.»
- **4 Summary/uplift closer** (8)
  - S004 [editorial: "como toda herramienta de este curso, solo es útil cuando sabes exactamente qué mide y qué no"] «La más conocida en cripto es el índice de miedo y codicia y, como toda herramienta de este curso, solo es útil cuando sabes exactamente qué mide y qué no.»
  - S026 [restate: repeats S024 ("reetiquetada como sentimiento" = "disfrazada de emoción")] «La mayor parte del tiempo es la misma información que ya tienes del gráfico, reetiquetada como sentimiento.»
  - S032 [restate: "el mismo suceso descrito dos veces" repeats S030–S031] «Por eso un nuevo máximo de precio y una lectura de codicia extrema casi siempre llegan juntos: son en buena parte el mismo suceso descrito dos veces.»
  - S034 [editorial: "Es un resumen real y útil del estado de ánimo actual de la masa."] «Es un resumen real y útil del estado de ánimo actual de la masa.»
  - S050 [restate: "Por eso el miedo más profundo tiende a aparecer cerca de los suelos" repeats S048] «Por eso el miedo más profundo tiende a aparecer cerca de los suelos, no de los techos.»
  - S062 [restate: "nunca te dice cuándo" repeats S059–S060] «El sentimiento te dice *qué lado es peligroso*; nunca te dice *cuándo*.»
  - S068 [restate: "no es un segundo testigo" repeats S067] «El índice no es un segundo testigo de lo que ya te está diciendo el precio.»
  - S077 [restate: last prose unit; repeats S076 (alt sentiment is more extreme than the index)] «En las alts, el sentimiento es aún más local, más rápido y más extremo de lo que sugiere el único número del panel.»
- **5 Sentence over 30 words** (18)
  - S019 [31w **aside-only** (23w without asides)] «*Por qué:* en un susto, el dinero huye al rincón "seguro" de cripto (la dominancia sube → miedo); cuando la masa se siente valiente, persigue alts más arriesgadas (la dominancia baja → codicia).»
  - S028 [40w] «Observa las agujas: la volatilidad es baja y ordenada (codicia), el momentum y el volumen están fuertes y estirados (codicia), las redes se llenan de euforia y objetivos de precio (codicia) y las búsquedas de "comprar bitcoin" se disparan (codicia).»
  - S038 [45w] «Como sus ingredientes de mayor peso se calculan a partir de un precio que *ya* se ha impreso, el índice solo puede decirte cómo se ha sentido el pasado reciente: es una lectura rezagada y retrospectiva de *cómo se ha sentido últimamente*, no un pronóstico.»
  - S041 [39w] «La lógica contraria es sencilla y honesta: si casi todo el que quería comprar ya ha comprado, quedan pocos compradores para empujar el precio más arriba, y muchos largos tardíos y nerviosos que venderán rápido a la primera caída.»
  - S044 [57w] «En concreto, así es como *se ve* un techo de codicia desde dentro: el índice lleva una semana por encima de 90, el funding es muy positivo (los largos pagan a los cortos cada pocas horas solo por mantener la posición), tu feed es un muro de objetivos de precio y cada caída se compra en minutos.»
  - S047 [43w] «En el otro extremo, el miedo extremo significa que la masa está asustada, y su punto final es la capitulación: el momento en que los tenedores por fin se rinden y venden con pérdidas solo para dejar de sufrir viendo cómo cae más.»
  - S048 [39w] «Por la misma lógica, invertida: una vez que quienes iban a entrar en pánico ya han vendido, la presión vendedora que empujaba el precio a la baja está casi agotada y el precio suele estar cerca de un mínimo.»
  - S051 [54w] «La capitulación suele verse como una única sesión violenta: BTC cae un 15% en unas horas con un volumen enorme, una cascada de liquidaciones (cierres forzosos de largos sobreapalancados) vuelca aún más oferta sobre un libro poco profundo, el índice se desploma hasta 6 y las redes giran a "se acabó, cripto está muerto".»
  - S058 [39w **aside-only** (30w without asides)] «Al contrarian que se puso corto en la *primera* lectura de "codicia extrema" —o que compró en la *primera* de "miedo extremo"— lo arrolló el mercado: la masa siguió desequilibrada mucho más tiempo del que su cuenta podía sobrevivir.»
  - S064 [58w] «"Índice en 8, a comprar a saco" e "índice en 92, a cortar" son exactamente la forma en que los contrarios acaban liquidados antes de tiempo: se plantan delante de una tendencia que todavía se está alimentando, apoyados en un número que solo dice que la masa está desequilibrada, no que el desequilibrio esté a punto de terminar.»
  - S067 [37w] «Como la mitad del índice es precio disfrazado, un principiante "confirmará" una ruptura alcista del precio señalando la codicia en aumento, y creerá que tiene dos razones independientes cuando en realidad tiene una razón contada dos veces.»
  - S071 [47w] «El sentimiento se acumula durante las sesiones nocturnas y de fin de semana con escasa liquidez, y un extremo puede alcanzarse *y* deshacerse mientras duermes: el índice que miras en el desayuno puede haber pasado ya del pánico al alivio y estar rezagado respecto a ambos movimientos.»
  - S073 [61w] «Un solo hilo viral, la llamada de un influencer o el listado en un nuevo exchange pueden disparar a la vez el volumen social, el interés de búsqueda y el precio, y recuerda que tres de los ingredientes del índice se nutren precisamente de esas cosas, así que una sola narrativa puede empujar todo el indicador a codicia extrema muy rápido.»
  - S074 [37w] «Un funding positivo persistente puede luego financiar esa codicia: mientras los largos estén dispuestos a seguir pagando por mantener, el estado eufórico y saturado puede durar mucho más de lo que sugiere el "tiene que estar agotado".»
  - S076 [40w **aside-only** (22w without asides)] «Una sola alt puede tener una masa propia salvajemente eufórica o aterrorizada —sobre un libro poco profundo, donde un puñado de órdenes mueve el precio y el sentimiento con violencia— mientras el índice del conjunto del mercado se lee tranquilo.»
  - S078 [51w] «El índice de miedo y codicia es un compuesto de 0 a 100, y en torno a la mitad de su peso —la volatilidad, y el momentum y el volumen— se calcula a partir del propio precio, así que es en buena medida el gráfico que ya tienes, reetiquetado como sentimiento.»
  - S079 [38w] «La codicia extrema dice que el lado comprador ya está dentro del todo y el miedo extremo que la venta de pánico está casi agotada, lo que hace de cada uno una zona contraria y no un momento.»
  - S080 [40w] «Los extremos persisten durante semanas, así que no trates nunca el 8 o el 92 como un botón de entrada, ni cuentes una lectura de codicia como confirmación independiente de un precio que sube: es una razón contada dos veces.»
- **9 Course-coined term** (2)
  - S059 [non-seed zona contraria: "El sentimiento marca una zona contraria" used as a named zone] «El sentimiento marca una zona contraria: una región donde las probabilidades y el riesgo/beneficio empiezan a cambiar, y donde deberías volverte *más prudente* con el lado saturado.»
  - S079 [non-seed zona contraria: "lo que hace de cada uno una zona contraria y no un momento"] «La codicia extrema dice que el lado comprador ya está dentro del todo y el miedo extremo que la venta de pánico está casi agotada, lo que hace de cada uno una zona contraria y no un momento.»
- **10 Metaphor then gloss** (2)
  - S001 ["las personas se mueven en manada", glossed in S002 (casi todo el mundo siente lo mismo al mismo tiempo)] «El precio lo fijan personas, y las personas se mueven en manada.»
  - S024 ["disfrazada de emoción", glossed in S025 (no es una segunda opinión independiente)] «Así que el índice es, en buena medida, una redescripción de la acción de precio reciente disfrazada de emoción.»
- **11 Synonym rotation** (2)
  - S003 [crowd sentiment: sentimiento de masas (S003), estado de ánimo (S003), emoción (S024), tono (S033), ánimo (S070)] 
  - S043 [crowded positioning: el terreno está saturado (S043), el lado comprador ya está dentro del todo (S045), desequilibrada (S058), lado saturado (S059)] 
- **A absolutes** (6)
  - S025 [debes] «Eso es lo más importante que debes recordar de él: *no* es una segunda opinión independiente que confirme lo que hace el precio.»
  - S032 [siempre] «Por eso un nuevo máximo de precio y una lectura de codicia extrema casi siempre llegan juntos: son en buena parte el mismo suceso descrito dos veces.»
  - S059 [deberías] «El sentimiento marca una zona contraria: una región donde las probabilidades y el riesgo/beneficio empiezan a cambiar, y donde deberías volverte *más prudente* con el lado saturado.»
  - S062 [nunca] «El sentimiento te dice *qué lado es peligroso*; nunca te dice *cuándo*.»
  - S070 [nunca] «Los mercados tradicionales cierran; cripto funciona 24/7, así que el ánimo nunca recibe un reinicio nocturno.»
  - S080 [nunca, summary] «Los extremos persisten durante semanas, así que no trates nunca el 8 o el 92 como un botón de entrada, ni cuentes una lectura de codicia como confirmación independiente de un precio que sube: es una razón contada dos veces.»

**EN** — 45 hits, 80 sentences, density 56.2

- **1 Filler** (11)
  - S004 [exactly: emphatic "know exactly what it measures"] «The best known in crypto is the Fear & Greed index, and like every tool in this course it is useful only once you know exactly what it measures and what it doesn't.»
  - S022 [other: announcer "Look hard at the first two inputs."] «Look hard at the first two inputs.»
  - S025 [other: announcer "That is the single most important thing to remember about it:"] «That is the single most important thing to remember about it: it is *not* an independent second opinion that confirms what price is doing.»
  - S030 [actually: emphatic, inside an announcer ("notice what actually happened")] «But notice what actually happened: the rising price *fed most of those inputs*.»
  - S031 [simply: "the index simply put a name on it"] «The index did not independently discover euphoria; the price did the work, and the index simply put a name on it.»
  - S041 [honest: "simple and honest" applied to a logic] «The contrarian logic is simple and honest: if almost everyone who wanted to buy has already bought, there are few buyers left to push price higher, and a lot of nervous late longs who will sell fast the moment it dips.»
  - S053 [other: tic "Again, though:"] «Again, though: this is a zone of interest, a place to *look* for setups, not a command to buy.»
  - S054 [other: announcer sentence "Here is the mistake that costs people money."] «Here is the mistake that costs people money.»
  - S061 [actually: "to actually enter", emphatic] «The trigger to actually enter still has to come from your own tools: structure, a level, confirmation.»
  - S064 [exactly: emphatic "are exactly how"] «"Index at 8, back up the truck" and "index at 92, short it" are exactly how contrarians get liquidated early: they are standing in front of a trend that is still being fed, on the strength of a number that only says the crowd is lopsided — not that the lopsidedness is about to end.»
  - S073 [exactly: emphatic "feed on exactly those things"] «A single viral thread, an influencer call, or a new exchange listing can spike social volume, search interest, and price *at the same time* — and remember three of the index's inputs feed on exactly those things, so one narrative can push the whole gauge into extreme greed fast.»
- **2 Rhythmic triad** (4)
  - S039 [confident / leveraged / already long: "confident" repeats "euphoric"; drop it] «When the index sits in extreme greed, the crowd is euphoric — confident, leveraged, and already long.»
  - S043 [size down / tighten risk / stop chasing: first two overlap; drop "tighten risk"] «So extreme greed does not mean "sell now" — it means the ground is crowded: size down, tighten risk, stop chasing.»
  - S052 [panic / forced selling / a spike of fear: "panic" and "spike of fear" overlap; drop "panic"] «That flush — panic, forced selling, and a spike of fear all at once — is what a capitulation low can look like.»
  - S077 [more local / faster / more extreme: third for rhythm (S076 already said "violently"); drop "more extreme"] «In alts, sentiment is even more local, faster, and more extreme than the one number on the dashboard suggests.»
- **4 Summary/uplift closer** (8)
  - S004 [editorial: "like every tool in this course it is useful only once you know exactly what it measures"] «The best known in crypto is the Fear & Greed index, and like every tool in this course it is useful only once you know exactly what it measures and what it doesn't.»
  - S026 [restate: repeats S024 ("relabelled as a feeling" = "wearing an emotional label")] «Much of the time it is the same information you already have from the chart, relabelled as a feeling.»
  - S032 [restate: "the same event described twice" repeats S030–S031] «That is why a fresh price high and an extreme-greed reading almost always arrive together — they are largely the same event described twice.»
  - S034 [editorial: "That is a real, useful summary of the crowd's current mood."] «That is a real, useful summary of the crowd's current mood.»
  - S050 [restate: "That is why the deepest fear tends to appear near bottoms" repeats S048] «That is why the deepest fear tends to appear near bottoms, not tops.»
  - S062 [restate: "it never tells you when" repeats S059–S060] «Sentiment tells you *which side is dangerous*; it never tells you *when*.»
  - S068 [restate: "not a second witness" repeats S067] «The index is not a second witness to what price is telling you.»
  - S077 [restate: last prose unit; repeats S076 (alt sentiment is more extreme than the index)] «In alts, sentiment is even more local, faster, and more extreme than the one number on the dashboard suggests.»
- **5 Sentence over 30 words** (16)
  - S004 [32w] «The best known in crypto is the Fear & Greed index, and like every tool in this course it is useful only once you know exactly what it measures and what it doesn't.»
  - S028 [31w **aside-only** (27w without asides)] «Watch the needles: volatility is low and orderly (greedy), momentum and volume are strong and stretched (greedy), timelines fill with celebration and price targets (greedy), and "buy bitcoin" searches spike (greedy).»
  - S038 [39w] «Because its heaviest inputs are computed from price that has *already* printed, the index can only ever tell you how the recent past felt — it is a lagging, backward-looking read of *how it has felt lately*, not a forecast.»
  - S041 [41w] «The contrarian logic is simple and honest: if almost everyone who wanted to buy has already bought, there are few buyers left to push price higher, and a lot of nervous late longs who will sell fast the moment it dips.»
  - S044 [50w] «Concretely, this is what a greedy top *looks* like from the inside: the index has sat above 90 for a week, funding is deeply positive (longs are paying shorts every few hours just to hold the position), your feed is wall-to-wall price targets, and every dip is bought within minutes.»
  - S047 [37w] «At the other end, extreme fear means the crowd is scared, and its endpoint is capitulation — the moment holders finally give up and sell at a loss just to stop the pain of watching it fall further.»
  - S048 [34w] «By the same logic inverted: once the people who were going to panic have already sold, the selling pressure that was driving price down is largely spent, and price is often near a low.»
  - S051 [50w] «Capitulation usually looks like a single violent session: BTC drops 15% in a few hours on enormous volume, a cascade of liquidations (forced closes of over-leveraged longs) dumps even more supply into a thin book, the index gaps down to 6, and social flips to "it's over, crypto is dead.»
  - S064 [54w] «"Index at 8, back up the truck" and "index at 92, short it" are exactly how contrarians get liquidated early: they are standing in front of a trend that is still being fed, on the strength of a number that only says the crowd is lopsided — not that the lopsidedness is about to end.»
  - S067 [36w] «Because half the index is price in disguise, a beginner will "confirm" a bullish price breakout by pointing at rising greed — and think they have two independent reasons when they really have one reason counted twice.»
  - S071 [40w] «Sentiment compounds through overnight and weekend sessions on thin liquidity, and an extreme can be reached *and* unwound while you sleep — the index you check at breakfast may already have swung from panic to relief and be lagging both moves.»
  - S073 [48w] «A single viral thread, an influencer call, or a new exchange listing can spike social volume, search interest, and price *at the same time* — and remember three of the index's inputs feed on exactly those things, so one narrative can push the whole gauge into extreme greed fast.»
  - S074 [33w] «Persistent positive funding can then bankroll that greed: as long as longs are willing to keep paying to hold, the crowded, euphoric state can last far longer than "it must be exhausted" suggests.»
  - S076 [34w **aside-only** (20w without asides)] «A single alt can have a wildly euphoric or terrified crowd of its own — on a thin book, where a handful of orders moves price and sentiment violently — while the market-wide index reads calm.»
  - S078 [39w] «The Fear & Greed index is a composite from 0 to 100, and about half its weight — volatility, and momentum and volume — is computed from price itself, so it is largely the chart you already have, relabelled as a feeling.»
  - S080 [33w] «Extremes persist for weeks, so never treat 8 or 92 as an entry button, and never count a greedy reading as independent confirmation of a rising price — that is one reason counted twice.»
- **9 Course-coined term** (2)
  - S059 [non-seed contrarian zone: "Sentiment marks a contrarian zone" used as a named zone] «Sentiment marks a contrarian zone — a region where the odds and the risk/reward start to shift, and where you should get *more careful* about the crowded side.»
  - S079 [non-seed contrarian zone: "which makes each a contrarian zone rather than a moment"] «Extreme greed says the buy side is already all-in and extreme fear says the panic selling is largely spent, which makes each a contrarian zone rather than a moment.»
- **10 Metaphor then gloss** (2)
  - S001 ["people move in herds", glossed in S002 (almost everyone feels the same way at the same time)] «Price is set by people, and people move in herds.»
  - S024 ["wearing an emotional label", glossed in S025 (not an independent second opinion)] «So the index is, to a large degree, a re-description of recent price action wearing an emotional label.»
- **11 Synonym rotation** (2)
  - S003 [crowd sentiment: mass sentiment (S003), mood (S003), emotional label (S024), feeling (S026), tone (S033)] 
  - S043 [crowded positioning: the ground is crowded (S043), the buy side is already all-in (S045), lopsided (S058), crowded side (S059)] 
- **A absolutes** (5)
  - S032 [always] «That is why a fresh price high and an extreme-greed reading almost always arrive together — they are largely the same event described twice.»
  - S062 [never] «Sentiment tells you *which side is dangerous*; it never tells you *when*.»
  - S070 [never] «Traditional markets close; crypto runs 24/7, so the mood never gets a nightly reset.»
  - S074 [must] «Persistent positive funding can then bankroll that greed: as long as longs are willing to keep paying to hold, the crowded, euphoric state can last far longer than "it must be exhausted" suggests.»
  - S080 [never, never, summary] «Extremes persist for weeks, so never treat 8 or 92 as an entry button, and never count a greedy reading as independent confirmation of a rising price — that is one reason counted twice.»

### m19-l1

**ES** — 68 hits, 94 sentences, density 72.3

- **1 Filler** (7)
  - S002 [honestidad: "Leídos con honestidad" applied to reading data] «Leídos con honestidad, estos datos te dicen lo *convencido* y lo *concurrido* que está el mercado: si un movimiento tiene dinero de verdad detrás y si un lado se ha vuelto peligrosamente unilateral.»
  - S023 [other: "justo" emphatic in "es justo lo que el OI llevaba rato anunciando"] «Velas idénticas hasta ahí, significado opuesto: lo que las separa llega después, y es justo lo que el OI llevaba rato anunciando.»
  - S029 [other: announcer "La frase que hay que quedarse:"] «La frase que hay que quedarse: el OI te dice si un movimiento está respaldado por posiciones nuevas o solo por gente que deshace las viejas.»
  - S048 [honesta: "La lectura honesta"] «La lectura honesta es "preparado para un desagüe violento", no "súmate a los ganadores".»
  - S056 [precisamente: emphatic (italicised) "es precisamente lo que hace"] «Porque la base y el funding son un mismo hecho visto dos veces: que el perpetuo cotice caro sobre el spot es *precisamente* lo que hace el funding positivo, y el funding es el peaje que se cobra por esa carestía.»
  - S076 [honesto: "el estado honesto del mercado"] «Usados solos parecen señales y se comportan como caras o cruces; usados juntos, y leídos contra el precio, te dicen el estado honesto del mercado.»
  - S079 [other: "genuinamente" intensifier in "un instrumento genuinamente nuevo"] «Si vienes de las acciones, este es un instrumento genuinamente nuevo, no uno reetiquetado.»
- **3 Rhetorical question** (2)
  - S007 «¿Por qué es informativo siquiera?»
  - S037 «¿De cuánto es el pago?»
- **4 Summary/uplift closer** (7)
  - S023 [restate: "Velas idénticas hasta ahí, significado opuesto" repeats S021–S022] «Velas idénticas hasta ahí, significado opuesto: lo que las separa llega después, y es justo lo que el OI llevaba rato anunciando.»
  - S049 [editorial: "Los datos no predijeron una caída; describieron un mercado inclinado..."] «Los datos no predijeron una caída; describieron un mercado inclinado con la fuerza suficiente a un lado como para que una caída sea fácil de disparar.»
  - S053 [editorial: "Todo lo anterior leía la corrección; esto lee el hueco en sí."] «Todo lo anterior leía la corrección; esto lee el hueco en sí.»
  - S066 [ahead: second half "m21-l1 se mete a vivir dentro de ella..." after the paragraph's point] «Y ese arbitraje no es solo el mecanismo que topa la prima: es una estrategia que hay quien lleva con tamaño. m21-l1 se mete a vivir dentro de ella —quién la hace, qué gana y por qué lo de «casi sin riesgo» esconde una pata corta que puede liquidarse en un rally que su propia pata de spot está ganando—.»
  - S072 [ahead: "La lección 2 desmonta ese mecanismo fase por fase."] «La lección 2 desmonta ese mecanismo fase por fase.»
  - S076 [editorial: "te dicen el estado honesto del mercado"] «Usados solos parecen señales y se comportan como caras o cruces; usados juntos, y leídos contra el precio, te dicen el estado honesto del mercado.»
  - S087 [restate: repeats S086's rule as a question] «Misma ventana, los dos a la vez: ¿el movimiento está respaldado por posiciones nuevas o solo se cierran las viejas?»
- **5 Sentence over 30 words** (27)
  - S002 [33w] «Leídos con honestidad, estos datos te dicen lo *convencido* y lo *concurrido* que está el mercado: si un movimiento tiene dinero de verdad detrás y si un lado se ha vuelto peligrosamente unilateral.»
  - S010 [38w] «Así que el *cambio* del OI es un recuento limpio de posiciones que se crean o se destruyen: un OI que sube significa que se abren posiciones nuevas; un OI que baja significa que se cierran posiciones existentes.»
  - S021 [38w] «La figura muestra los dos casos de precio al alza uno junto al otro, y los dos paneles no es que se parezcan: son la misma serie de precio, vela por vela, hasta el final del tramo común.»
  - S022 [44w **aside-only** (19w without asides)] «A la izquierda el OI sube con el precio —dinero nuevo respaldando el movimiento, así que continúa—; a la derecha el OI cae mientras el precio sube —un rally de cobertura de cortos sin nada fresco detrás, así que se estanca y se gira—.»
  - S026 [38w] «En el de la izquierda el open interest sube junto con él, de 10.000 a 13.000 contratos: unos 3.000 contratos de convicción fresca entraron con el movimiento, la tendencia tiene combustible y el precio sigue subiendo hasta 2.670.»
  - S027 [33w] «En el de la derecha el precio hace exactamente lo mismo pero el OI *cae*, de 10.000 a 7.750 contratos: no llegó dinero nuevo; la subida son cortos atrapados que compran para salir.»
  - S031 [31w] «Un futuro normal tiene fecha de vencimiento, y a medida que esa fecha se acerca su precio es arrastrado hacia el spot porque los dos *tienen* que coincidir en el vencimiento.»
  - S032 [38w] «Un perpetuo no tiene vencimiento y, por tanto, ninguna fuerza natural que lo devuelva al spot, así que los exchanges construyeron una: el funding rate, un pequeño pago que se intercambian directamente largos y cortos cada pocas horas.»
  - S036 [42w] «El funding es, por tanto, un anclaje que se autocorrige, y su *signo* es una lectura del posicionamiento: el lado que paga es el lado concurrido y ansioso, el que está dispuesto a sangrar un poco con tal de mantener su apuesta.»
  - S044 [43w] «Y el posicionamiento concurrido es posicionamiento *frágil*: si casi todos están ya largos, queda poca compra nueva para empujar el precio más arriba, y un bloque grande de esos largos está sentado cerca del precio al que se les cerraría por la fuerza.»
  - S047 [33w] «Eso no es una señal de compra: es el mercado diciéndote que la operación en la que ya está todo el mundo es *esta*, y que el combustible (compradores nuevos) está casi agotado.»
  - S056 [41w] «Porque la base y el funding son un mismo hecho visto dos veces: que el perpetuo cotice caro sobre el spot es *precisamente* lo que hace el funding positivo, y el funding es el peaje que se cobra por esa carestía.»
  - S063 [46w] «Las grandes suelen quedarse bastante por debajo de una décima de punto porcentual, porque el hueco es un arbitraje: vender el perpetuo caro, comprar el spot barato, y los dos precios quedan empujados el uno hacia el otro a cambio de una diferencia casi sin riesgo.»
  - S064 [41w] «Por tanto, una prima del 0,5% significa que la demanda de largos apalancados va por delante de ese arbitraje, y deberías esperar encontrar el funding fuertemente positivo en ese mismo momento, porque es la misma saturación medida desde el otro lado.»
  - S065 [36w **aside-only** (27w without asides)] «Compara el perpetuo contra el spot o el precio índice de *su propia* plataforma; un hueco entre dos exchanges distintos suele ser fricción operativa —comisiones, fricciones de transferencia, un creador de mercado atascado— y no posicionamiento.»
  - S066 [60w **aside-only** (29w without asides)] «Y ese arbitraje no es solo el mecanismo que topa la prima: es una estrategia que hay quien lleva con tamaño. m21-l1 se mete a vivir dentro de ella —quién la hace, qué gana y por qué lo de «casi sin riesgo» esconde una pata corta que puede liquidarse en un rally que su propia pata de spot está ganando—.»
  - S068 [50w] «En un squeeze (lección 2) el flujo forzado cae sobre el *perpetuo*, no sobre el spot: un corto liquidado es una compra forzada del contrato, así que el perpetuo puede dispararse un punto porcentual o más por encima del spot durante minutos mientras la moneda en sí apenas se mueve.»
  - S070 [39w] «La demanda orgánica del activo aparece en el spot y arrastra al perpetuo detrás; que el perpetuo se pase del spot significa que la demanda es *forzada*, y la demanda forzada sale de una bolsa finita de posiciones atrapadas.»
  - S071 [45w] «Así que lee un pico salvaje de prima dentro de un movimiento rápido como agotamiento local —más cerca del final de ese movimiento forzado que del comienzo de una tendencia— y espera que la base se derrumbe hacia cero a medida que el flujo termina.»
  - S074 [33w] «La misma trampa atrapa al OI: "el OI sube, así que compro" ignora que el mismo aumento son largos nuevos en un movimiento al alza y cortos nuevos en uno a la baja.»
  - S080 [48w] «La mayoría de las plataformas cobran funding tres veces al día en un horario fijo (habitualmente a las 00:00, 08:00 y 16:00 UTC); algunas usan intervalos de 4 horas o de 1 hora, y una plataforma puede subir la frecuencia cuando el perpetuo se aleja mucho del spot.»
  - S084 [37w] «Un perpetuo fino de una alt de baja capitalización es distinto: un libro poco profundo se desequilibra deprisa, así que su funding puede dispararse a números que nunca verías en BTC, en cualquiera de las dos direcciones.»
  - S090 [51w] «Deja que los dos coincidan antes de apoyarte en ninguno: un precio que sube con OI que sube *y* funding aún tranquilo es una tendencia sana con margen para correr, mientras que un precio que sube con OI que baja y funding ya disparado es un movimiento concurrido viviendo de prestado.»
  - S091 [50w] «Y lee la base junto al funding: un perpetuo que cotiza caro sobre el spot mientras el funding ya está alto es una misma saturación contada dos veces, y un pico violento de prima dentro de un movimiento rápido es flujo forzado, que, a diferencia de la convicción, se agota.»
  - S092 [47w] «El open interest cuenta los contratos abiertos, así que su cambio dice si un movimiento está respaldado por posiciones nuevas o son solo viejas que se deshacen, y no significa nada hasta que lo lees contra el precio en la misma ventana, lo que da cuatro lecturas.»
  - S093 [41w] «El funding rate es el anclaje fabricado que mantiene un perpetuo cerca del spot, y su signo nombra al lado concurrido, el que está dispuesto a sangrar por seguir dentro: el número diario es un coste, el extremo es la información.»
  - S094 [38w] «La base es esa misma saturación medida directamente como el precio del perpetuo menos el spot, y un pico violento de prima dentro de un movimiento rápido es flujo forzado, que a diferencia de la convicción se agota.»
- **7 No solo / not only** (1)
  - S066 «Y ese arbitraje no es solo el mecanismo que topa la prima: es una estrategia que hay quien lleva con tamaño. m21-l1 se mete a vivir dentro de ella —quién la hace, qué gana y por qué lo de «casi sin riesgo» esconde una pata corta que puede liquidarse en un rally que su propia pata de spot está ganando—.»
- **9 Course-coined term** (17)
  - S002 [non-seed concurrido (calque of "crowded"): "lo concurrido que está el mercado"] «Leídos con honestidad, estos datos te dicen lo *convencido* y lo *concurrido* que está el mercado: si un movimiento tiene dinero de verdad detrás y si un lado se ha vuelto peligrosamente unilateral.»
  - S026 [combustible [seed]] «En el de la izquierda el open interest sube junto con él, de 10.000 a 13.000 contratos: unos 3.000 contratos de convicción fresca entraron con el movimiento, la tendencia tiene combustible y el precio sigue subiendo hasta 2.670.»
  - S036 [non-seed concurrido: "el lado concurrido y ansioso"] «El funding es, por tanto, un anclaje que se autocorrige, y su *signo* es una lectura del posicionamiento: el lado que paga es el lado concurrido y ansioso, el que está dispuesto a sangrar un poco con tal de mantener su apuesta.»
  - S043 [non-seed concurrido: "el lado largo está tan concurrido"] «Nadie paga eso como coste de mantener la posición; significa que el lado largo está tan concurrido que los largos están dispuestos a sangrar mucho con tal de seguir dentro.»
  - S044 [non-seed concurrido: "el posicionamiento concurrido es posicionamiento frágil"] «Y el posicionamiento concurrido es posicionamiento *frágil*: si casi todos están ya largos, queda poca compra nueva para empujar el precio más arriba, y un bloque grande de esos largos está sentado cerca del precio al que se les cerraría por la fuerza.»
  - S047 [combustible [seed]] «Eso no es una señal de compra: es el mercado diciéndote que la operación en la que ya está todo el mundo es *esta*, y que el combustible (compradores nuevos) está casi agotado.»
  - S048 [non-seed desagüe: "preparado para un desagüe violento" = long liquidation flush/cascade] «La lectura honesta es "preparado para un desagüe violento", no "súmate a los ganadores".»
  - S058 [non-seed concurrido: "largos concurridos pagando por el privilegio"] «Así que una prima sostenida es un termómetro de la manía del apalancamiento: largos concurridos pagando por el privilegio, con la factura de funding a juego.»
  - S059 [non-seed concurrido: "un lado corto concurrido y temeroso"] «Y un descuento sostenido es la misma lectura invertida, un lado corto concurrido y temeroso.»
  - S068 [flujo forzado [seed]] «En un squeeze (lección 2) el flujo forzado cae sobre el *perpetuo*, no sobre el spot: un corto liquidado es una compra forzada del contrato, así que el perpetuo puede dispararse un punto porcentual o más por encima del spot durante minutos mientras la moneda en sí apenas se mueve.»
  - S070 [seed flujo forzado (as "demanda forzada") and seed bolsa (as "una bolsa finita de posiciones atrapadas")] «La demanda orgánica del activo aparece en el spot y arrastra al perpetuo detrás; que el perpetuo se pase del spot significa que la demanda es *forzada*, y la demanda forzada sale de una bolsa finita de posiciones atrapadas.»
  - S071 [seed flujo forzado (as "ese movimiento forzado")] «Así que lee un pico salvaje de prima dentro de un movimiento rápido como agotamiento local —más cerca del final de ese movimiento forzado que del comienzo de una tendencia— y espera que la base se derrumbe hacia cero a medida que el flujo termina.»
  - S082 [non-seed concurrido: "una posición concurrida"] «Mantener una posición concurrida durante un fin de semana largo puede costar, sin que te des cuenta, varios intervalos de funding.»
  - S090 [non-seed concurrido: "un movimiento concurrido viviendo de prestado"] «Deja que los dos coincidan antes de apoyarte en ninguno: un precio que sube con OI que sube *y* funding aún tranquilo es una tendencia sana con margen para correr, mientras que un precio que sube con OI que baja y funding ya disparado es un movimiento concurrido viviendo de prestado.»
  - S091 [flujo forzado [seed]] «Y lee la base junto al funding: un perpetuo que cotiza caro sobre el spot mientras el funding ya está alto es una misma saturación contada dos veces, y un pico violento de prima dentro de un movimiento rápido es flujo forzado, que, a diferencia de la convicción, se agota.»
  - S093 [non-seed concurrido: "su signo nombra al lado concurrido"] «El funding rate es el anclaje fabricado que mantiene un perpetuo cerca del spot, y su signo nombra al lado concurrido, el que está dispuesto a sangrar por seguir dentro: el número diario es un coste, el extremo es la información.»
  - S094 [flujo forzado [seed]] «La base es esa misma saturación medida directamente como el precio del perpetuo menos el spot, y un pico violento de prima dentro de un movimiento rápido es flujo forzado, que a diferencia de la convicción se agota.»
- **10 Metaphor then gloss** (3)
  - S047 ["el combustible (compradores nuevos)", glossed in the parenthesis] «Eso no es una señal de compra: es el mercado diciéndote que la operación en la que ya está todo el mundo es *esta*, y que el combustible (compradores nuevos) está casi agotado.»
  - S056 ["el funding es el peaje que se cobra por esa carestía", glossed in S057 (lo que ese sobreprecio le cuesta por intervalo)] «Porque la base y el funding son un mismo hecho visto dos veces: que el perpetuo cotice caro sobre el spot es *precisamente* lo que hace el funding positivo, y el funding es el peaje que se cobra por esa carestía.»
  - S058 ["un termómetro de la manía del apalancamiento", glossed after the colon] «Así que una prima sostenida es un termómetro de la manía del apalancamiento: largos concurridos pagando por el privilegio, con la factura de funding a juego.»
- **11 Synonym rotation** (4)
  - S002 [crowded positioning: concurrido (S002), unilateral (S002), inclinado (S049), saturación (S064)] 
  - S014 [new positions: posiciones nuevas (S014), convicción fresca (S016), dinero fresco (S018), dinero nuevo (S022)] 
  - S045 [long liquidation flush: expulsar a toda la masa de golpe (S045), desagüe violento (S048), caída fácil de disparar (S049)] 
  - S053 [perp premium over spot: hueco (S053), prima (S054), carestía (S056), sobreprecio (S057)] 
- **A absolutes** (5)
  - S030 [nunca] «Los futuros perpetuos nunca vencen.»
  - S064 [deberías] «Por tanto, una prima del 0,5% significa que la demanda de largos apalancados va por delante de ese arbitraje, y deberías esperar encontrar el funding fuertemente positivo en ese mismo momento, porque es la misma saturación medida desde el otro lado.»
  - S078 [nunca] «El swap perpetuo, un futuro sin vencimiento, se popularizó en el cripto, y el funding es la maquinaria que hace que un contrato que nunca vence se comporte.»
  - S084 [nunca] «Un perpetuo fino de una alt de baja capitalización es distinto: un libro poco profundo se desequilibra deprisa, así que su funding puede dispararse a números que nunca verías en BTC, en cualquiera de las dos direcciones.»
  - S086 [nunca] «Una regla manda sobre las demás: **nunca leas el OI sin el precio**.»

**EN** — 55 hits, 93 sentences, density 59.1

- **1 Filler** (8)
  - S002 [honestly: "Read honestly" applied to reading data] «Read honestly, this data tells you how *committed* and how *crowded* the market is — whether a move has real money behind it, and whether one side has become dangerously one-sided.»
  - S023 [exactly: emphatic "it is exactly what the OI had been signalling"] «Identical candles up to there, opposite meaning: what separates them comes afterwards, and it is exactly what the OI had been signalling all along.»
  - S029 [other: announcer "The one line to keep:"] «The one line to keep: OI tells you whether a move is backed by new positions or just by people unwinding old ones.»
  - S040 [exactly: "Which is exactly why", emphatic] «Which is exactly why the day-to-day number is not something to trade off — it is noise.»
  - S048 [honest: "The honest read"] «The honest read is "primed for a violent flush," not "join the winners.»
  - S056 [precisely: emphatic (italicised) "is precisely what makes"] «Because the basis and funding are one fact seen twice: a perp trading rich over spot is *precisely* what makes funding positive, and funding is the toll charged for that richness.»
  - S075 [honest: "the honest state of the market"] «Used alone they feel like signals and behave like coin flips; used together, and read against price, they tell you the honest state of the market.»
  - S078 [genuinely: intensifier "a genuinely new instrument"] «If you came from stocks, this is a genuinely new instrument, not a relabelled one.»
- **3 Rhetorical question** (2)
  - S007 «Why is it informative at all?»
  - S037 «How big is the payment?»
- **4 Summary/uplift closer** (7)
  - S023 [restate: "Identical candles up to there, opposite meaning" repeats S021–S022] «Identical candles up to there, opposite meaning: what separates them comes afterwards, and it is exactly what the OI had been signalling all along.»
  - S049 [editorial: "The data didn't predict a drop; it described a market leaning..."] «The data didn't predict a drop; it described a market leaning hard enough to one side that a drop is easy to trigger.»
  - S053 [editorial: "Everything above read the correction — this reads the gap itself."] «Everything above read the correction — this reads the gap itself.»
  - S065 [ahead: second half "m21-l1 goes and lives inside it..." after the paragraph's point] «And that arbitrage is not only the mechanism that caps the premium — it is a strategy people run at size. m21-l1 goes and lives inside it: who does it, what it earns, and why "nearly risk-free" hides a short leg that can be liquidated in a rally its own spot leg is winning.»
  - S071 [ahead: "Lesson 2 takes that mechanism apart phase by phase."] «Lesson 2 takes that mechanism apart phase by phase.»
  - S075 [editorial: "they tell you the honest state of the market"] «Used alone they feel like signals and behave like coin flips; used together, and read against price, they tell you the honest state of the market.»
  - S086 [restate: repeats S085's rule as a question] «Same window, both at once — is the move backed by new positions, or just old ones closing?»
- **5 Sentence over 30 words** (22)
  - S010 [31w] «So the *change* in OI is a clean count of positions being created or destroyed: rising OI means fresh positions are being opened; falling OI means existing positions are being closed.»
  - S021 [36w] «The figure shows the two rising-price cases side by side, and the two panels do not merely resemble each other: they are the same price series, candle for candle, to the end of the shared leg.»
  - S022 [37w **aside-only** (21w without asides)] «On the left OI climbs with price — new money backing the move, so it continues; on the right OI falls while price rises — a short-covering rally with nothing fresh behind it, so it stalls and rolls over.»
  - S026 [34w] «On the left, open interest climbs alongside it, from 10,000 to 13,000 contracts: about 3,000 contracts of fresh conviction came in with the move, the trend has fuel, and price keeps going to 2,670.»
  - S028 [32w] «Same candle, opposite meaning — and the second one runs out of buyers the moment the shorts have finished covering: it hands back the entire leg and ends at 2,020, where it began.»
  - S032 [34w] «A perpetual has no expiry and therefore no natural force pulling it back to spot — so exchanges built one: the funding rate, a small payment exchanged directly between longs and shorts every few hours.»
  - S036 [36w] «Funding is therefore a self-correcting tether, and its *sign* is a read on positioning: the side that is paying is the crowded, eager side — the one willing to bleed a little to keep its bet on.»
  - S044 [41w] «And crowded positioning is *fragile* positioning: if almost everyone is already long, there is little new buying left to push price higher, and a large block of those longs are sitting close to the price at which they would be force-closed.»
  - S056 [31w] «Because the basis and funding are one fact seen twice: a perp trading rich over spot is *precisely* what makes funding positive, and funding is the toll charged for that richness.»
  - S058 [35w **aside-only** (23w without asides)] «So a sustained premium is a leverage-mania thermometer — crowded longs paying for the privilege, with a funding bill to match — and a sustained discount is the same reading inverted, a crowded and fearful short side.»
  - S062 [36w] «Majors normally sit well inside a tenth of a percent, because the gap is an arbitrage: sell the rich perp, buy the cheap spot, and the two prices get pulled together for a nearly risk-free difference.»
  - S063 [35w] «A 0.5% premium therefore means leveraged-long demand is outrunning that arbitrage — and you should expect to find funding strongly positive at the same moment, because it is the same crowding measured from the other side.»
  - S065 [53w] «And that arbitrage is not only the mechanism that caps the premium — it is a strategy people run at size. m21-l1 goes and lives inside it: who does it, what it earns, and why "nearly risk-free" hides a short leg that can be liquidated in a rally its own spot leg is winning.»
  - S067 [42w] «In a squeeze (lesson 2) the forced flow lands on the *perpetual*, not on spot: a liquidated short is force-bought on the contract, so the perp can rip a percent or more above spot for minutes while the coin itself barely moves.»
  - S069 [37w] «Organic demand for the asset shows up in spot and drags the perp along behind it; a perp overshooting spot means the bid is *forced*, and forced bids come out of a finite pool of trapped positions.»
  - S070 [39w **aside-only** (26w without asides)] «So read a wild premium spike inside a fast move as local exhaustion — nearer the end of that forced move than the start of a trend — and expect the basis to collapse back toward zero as the flow finishes.»
  - S079 [38w] «Most venues charge funding three times a day on a fixed schedule (commonly 00:00, 08:00 and 16:00 UTC); some use 4-hour or 1-hour intervals, and a venue can raise the frequency when the perp runs far from spot.»
  - S089 [43w] «Let the two agree before you lean on either: price rising on rising OI *and* still-calm funding is a healthy trend with room to run, while price rising on falling OI with funding already screaming is a crowded move living on borrowed time.»
  - S090 [40w] «And read the basis alongside the funding — a perp trading rich over spot while funding is already high is one crowding counted twice, and a violent premium spike inside a fast move is forced flow, which, unlike conviction, runs out.»
  - S091 [42w] «Open interest counts contracts currently open, so its change says whether a move is backed by fresh positions or is just old ones unwinding — and it means nothing until you read it against price over the same window, which gives four readings.»
  - S092 [39w] «The funding rate is the manufactured tether that holds a perpetual near spot, and its sign names the crowded side, the one willing to bleed to stay in: the daily number is a cost, the extreme is the information.»
  - S093 [31w] «The basis is that same crowding measured directly as the perp's price minus spot, and a violent premium spike inside a fast move is forced flow, which unlike conviction runs out.»
- **7 No solo / not only** (2)
  - S021 «The figure shows the two rising-price cases side by side, and the two panels do not merely resemble each other: they are the same price series, candle for candle, to the end of the shared leg.»
  - S065 «And that arbitrage is not only the mechanism that caps the premium — it is a strategy people run at size. m21-l1 goes and lives inside it: who does it, what it earns, and why "nearly risk-free" hides a short leg that can be liquidated in a rally its own spot leg is winning.»
- **9 Course-coined term** (7)
  - S026 [fuel [seed]] «On the left, open interest climbs alongside it, from 10,000 to 13,000 contracts: about 3,000 contracts of fresh conviction came in with the move, the trend has fuel, and price keeps going to 2,670.»
  - S047 [fuel [seed]] «That is not a buy signal — it is the market telling you the trade everyone is already in is *this one*, and that the fuel (new buyers) is nearly spent.»
  - S067 [forced flow [seed]] «In a squeeze (lesson 2) the forced flow lands on the *perpetual*, not on spot: a liquidated short is force-bought on the contract, so the perp can rip a percent or more above spot for minutes while the coin itself barely moves.»
  - S069 [seed forced flow (as "forced bids") and seed liquidity pool (as "a finite pool of trapped positions")] «Organic demand for the asset shows up in spot and drags the perp along behind it; a perp overshooting spot means the bid is *forced*, and forced bids come out of a finite pool of trapped positions.»
  - S070 [seed forced flow (as "that forced move")] «So read a wild premium spike inside a fast move as local exhaustion — nearer the end of that forced move than the start of a trend — and expect the basis to collapse back toward zero as the flow finishes.»
  - S090 [forced flow [seed]] «And read the basis alongside the funding — a perp trading rich over spot while funding is already high is one crowding counted twice, and a violent premium spike inside a fast move is forced flow, which, unlike conviction, runs out.»
  - S093 [forced flow [seed]] «The basis is that same crowding measured directly as the perp's price minus spot, and a violent premium spike inside a fast move is forced flow, which unlike conviction runs out.»
- **10 Metaphor then gloss** (3)
  - S047 ["the fuel (new buyers)", glossed in the parenthesis] «That is not a buy signal — it is the market telling you the trade everyone is already in is *this one*, and that the fuel (new buyers) is nearly spent.»
  - S056 ["funding is the toll charged for that richness", glossed in S057 (what the overpayment costs them per interval)] «Because the basis and funding are one fact seen twice: a perp trading rich over spot is *precisely* what makes funding positive, and funding is the toll charged for that richness.»
  - S058 ["a leverage-mania thermometer", glossed after the dash] «So a sustained premium is a leverage-mania thermometer — crowded longs paying for the privilege, with a funding bill to match — and a sustained discount is the same reading inverted, a crowded and fearful short side.»
- **11 Synonym rotation** (4)
  - S002 [crowded positioning: crowded (S002), one-sided (S002), leaning hard to one side (S049), crowding (S063)] 
  - S014 [new positions: fresh positions (S014), fresh conviction (S016), fresh money (S018), new money (S022)] 
  - S045 [long liquidation flush: tip the whole crowd out (S045), violent flush (S048), a drop easy to trigger (S049)] 
  - S053 [perp premium over spot: gap (S053), premium (S054), richness (S056), overpayment (S057)] 
- **A absolutes** (5)
  - S030 [never] «Perpetual futures never expire.»
  - S031 [must] «A normal futures contract has a settlement date, and as that date approaches its price is dragged toward spot because the two *must* meet at expiry.»
  - S077 [never, never] «The perpetual swap, a futures contract that never settles, was popularised in crypto, and funding is the machinery that makes a never-settling contract behave.»
  - S083 [never] «A thin, low-cap alt perp is different: a shallow book gets one-sided fast, so its funding can spike to numbers you would never see on BTC — in either direction.»
  - S085 [never] «One rule outranks the rest: **never read OI without price**.»

### m19-l2

**ES** — 52 hits, 75 sentences, density 69.3

- **1 Filler** (7)
  - S002 [del todo (not in cand): "se acerca del todo", intensifier] «Esta lección se acerca del todo al libro de órdenes: *dónde* se apilan las salidas y las órdenes de protección, por qué el precio se ve tan a menudo atraído a atravesarlas y cómo, cuando el lado concurrido está apalancado, esa carrera se convierte en una cascada que se alimenta a sí misma: un squeeze.»
  - S009 [nada más: tag after "un cierre forzoso"] «Un cierre forzoso, y nada más.»
  - S026 [exactamente: emphatic, no quantity] «Una repisa de stops es exactamente esa bolsa.»
  - S041 [simplemente: intensifier] «Sin más órdenes forzadas detrás, el movimiento que era pura mecánica simplemente se detiene, y normalmente rebota, porque nunca hubo nada duradero impulsándolo.»
  - S070 [de verdad: emphatic ("corriendo de verdad")] «Cuando un squeeze está corriendo de verdad, la verdadera ventaja está en operar el agotamiento —contra la cascada—, nunca en perseguirla; y si no distingues en qué fase estás, la operación correcta es ninguna.»
  - S070 [verdadera (not in cand): "la verdadera ventaja", intensifier] «Cuando un squeeze está corriendo de verdad, la verdadera ventaja está en operar el agotamiento —contra la cascada—, nunca en perseguirla; y si no distingues en qué fase estás, la operación correcta es ninguna.»
  - S075 [honesta: "ventaja honesta"] «Un barrido se convierte en un squeeze cuando la bolsa está concurrida y apalancada —acumulación, disparo, cascada, agotamiento—, así que la ventaja honesta es operar el agotamiento y nunca perseguir una cascada cuyo combustible es una bolsa finita de posiciones atrapadas.»
- **2 Rhythmic triad** (1)
  - S019 [el mínimo obvio / el número redondo / el nivel que aguantó dos veces; "mínimo obvio" and "nivel que aguantó dos veces" overlap; drop "el mínimo obvio"] «El mínimo obvio, el número redondo, el nivel que aguantó dos veces: ahí es donde "pon tu stop justo pasado ese punto" envía miles de órdenes al mismo puñado de ticks.»
- **4 Summary/uplift closer** (5)
  - S004 [editorial: framing line after "Nada de esto predice la dirección" (fuel/burn metaphor)] «Traza el combustible y te muestra dónde suele arder el mercado.»
  - S011 [restate: repeats "mantenlas separadas" (S005) and the two definitions] «Se apilan juntas, y por eso se enredan las palabras, pero no son lo mismo, y esta lección usa cada una en sentido literal.»
  - S020 [restate: restates S018 "todos miran el mismo gráfico"] «El mapa no es aleatorio; lo construye un razonamiento compartido y predecible.»
  - S044 [editorial: "La misma máquina, en espejo"] «La misma máquina, en espejo.»
  - S072 [restate: repeats S003/S004 (no predice dirección; mercado preparado para arder)] «Los datos siguen sin predecir la chispa: te muestran un mercado preparado para arder.»
- **5 Sentence over 30 words** (14)
  - S002 [55w] «Esta lección se acerca del todo al libro de órdenes: *dónde* se apilan las salidas y las órdenes de protección, por qué el precio se ve tan a menudo atraído a atravesarlas y cómo, cuando el lado concurrido está apalancado, esa carrera se convierte en una cascada que se alimenta a sí misma: un squeeze.»
  - S016 [43w **aside-only** (29w without asides)] «Encima de un máximo reciente se sitúa una repisa de stop-loss de cortos —la orden de compra protectora de un corto se coloca *justo encima* del máximo— más los precios de liquidación de los cortos apalancados, que quedan por encima de la entrada.»
  - S019 [31w] «El mínimo obvio, el número redondo, el nivel que aguantó dos veces: ahí es donde "pon tu stop justo pasado ese punto" envía miles de órdenes al mismo puñado de ticks.»
  - S022 [31w] «Los largos por todas partes ponen sus stops justo debajo, en torno a 25.850; los largos apalancados abiertos cerca del mínimo tienen precios de liquidación repartidos por debajo, hasta unos 25.400.»
  - S029 [61w] «En su lugar, en una sola vela el precio se hunde desde los 26.200 en los que cotizaba hasta 25.350, atravesando la repisa entera: los stop-loss de los largos se disparan como ventas a mercado, los largos apalancados de ahí abajo se liquidan (más venta forzada) y toda esa venta la absorben las órdenes de compra en reposo del jugador grande.»
  - S031 [34w **aside-only** (27w without asides)] «Eso es un barrido (un "stop run" o "toma de liquidez"): quienes fueron expulsados por su stop y liquidados vendieron justo el mínimo, y sus órdenes fueron la liquidez que otro aprovechó para ejecutar.»
  - S032 [47w] «Un barrido se convierte en un squeeze cuando la bolsa que se dispara es una *concurrida y apalancada*, de modo que las órdenes que se activan no son solo stops voluntarios sino liquidaciones, y cada cierre forzoso empuja el precio hasta el siguiente clúster de cierres forzosos.»
  - S065 [31w] «Los clústeres son densos y saltan con movimientos minúsculos: una mecha de ~1% puede liquidar una posición de 100×, así que el disparo de la fase 2 casi no necesita nada.»
  - S067 [36w] «Las sesiones de fin de semana y festivos con libros poco profundos, y las alts de baja capitalización cualquier día, producen las cascadas más violentas: la mecha se excede porque no había nada ahí para absorberla.»
  - S068 [32w] «Lee el mapa como zonas de volatilidad y barridos probables, no como objetivos hacia los que operar: un clúster te dice dónde puede ponerse violento, no hacia qué lado termina el día.»
  - S070 [34w] «Cuando un squeeze está corriendo de verdad, la verdadera ventaja está en operar el agotamiento —contra la cascada—, nunca en perseguirla; y si no distingues en qué fase estás, la operación correcta es ninguna.»
  - S073 [37w] «La liquidez son órdenes en reposo esperando ejecutarse; la liquidación es el exchange cerrando a la fuerza una posición apalancada, y se apilan en los mismos sitios, que es por lo que las dos palabras se enredan.»
  - S074 [41w] «Los stops y los precios de liquidación se agrupan justo pasados el máximo y el mínimo obvios porque todos razonan igual, y un jugador grande que necesita ejecutar tamaño barre esa bolsa y recupera el nivel en una o dos velas.»
  - S075 [41w] «Un barrido se convierte en un squeeze cuando la bolsa está concurrida y apalancada —acumulación, disparo, cascada, agotamiento—, así que la ventaja honesta es operar el agotamiento y nunca perseguir una cascada cuyo combustible es una bolsa finita de posiciones atrapadas.»
- **7 No solo / not only** (1)
  - S032 «Un barrido se convierte en un squeeze cuando la bolsa que se dispara es una *concurrida y apalancada*, de modo que las órdenes que se activan no son solo stops voluntarios sino liquidaciones, y cada cierre forzoso empuja el precio hasta el siguiente clúster de cierres forzosos.»
- **9 Course-coined term** (22)
  - S004 [combustible [seed]] «Traza el combustible y te muestra dónde suele arder el mercado.»
  - S013 [repisa [seed]] «Debajo de un mínimo reciente se sitúa una repisa de stop-loss de largos: la orden de venta protectora de un largo se coloca *justo debajo* del mínimo que "debería aguantar".»
  - S016 [repisa [seed]] «Encima de un máximo reciente se sitúa una repisa de stop-loss de cortos —la orden de compra protectora de un corto se coloca *justo encima* del máximo— más los precios de liquidación de los cortos apalancados, que quedan por encima de la entrada.»
  - S023 [repisa [seed]] «Toda esa banda es una repisa densa de órdenes de venta en reposo: una bolsa de liquidez justo debajo del precio.»
  - S023 [bolsa de liquidez [seed]] «Toda esa banda es una repisa densa de órdenes de venta en reposo: una bolsa de liquidez justo debajo del precio.»
  - S025 [seed bolsa (de órdenes contrarias) — stop-cluster sense] «Necesita una bolsa de órdenes contrarias contra la que ejecutar sin hacer ruido.»
  - S026 [repisa [seed]] «Una repisa de stops es exactamente esa bolsa.»
  - S029 [repisa [seed]] «En su lugar, en una sola vela el precio se hunde desde los 26.200 en los que cotizaba hasta 25.350, atravesando la repisa entera: los stop-loss de los largos se disparan como ventas a mercado, los largos apalancados de ahí abajo se liquidan (más venta forzada) y toda esa venta la absorben las órdenes de compra en reposo del jugador grande.»
  - S032 [seed bolsa (stop/liquidation cluster)] «Un barrido se convierte en un squeeze cuando la bolsa que se dispara es una *concurrida y apalancada*, de modo que las órdenes que se activan no son solo stops voluntarios sino liquidaciones, y cada cierre forzoso empuja el precio hasta el siguiente clúster de cierres forzosos.»
  - S036 [combustible [seed]] «Se carga el combustible.»
  - S039 [repisa [seed]] «Ese flujo forzado empuja el precio hasta la siguiente repisa, que se dispara, que empuja el precio otra vez: se alimenta a sí mismo.»
  - S039 [flujo forzado [seed]] «Ese flujo forzado empuja el precio hasta la siguiente repisa, que se dispara, que empuja el precio otra vez: se alimenta a sí mismo.»
  - S047 [repisa [seed]] «El máximo reciente es 3.000; los precios de liquidación de los cortos se apilan en repisas por encima: en torno a 3.050, 3.150 y 3.300.»
  - S050 [repisa [seed]] «Esa compra sube el precio a 3.150 y golpea la siguiente repisa; esas compras forzadas lo llevan a 3.300 y golpean la siguiente.»
  - S057 [seed bolsa (obvious stop pool)] «Un segundo error, más silencioso: aparcar tu propio stop justo dentro de una bolsa obvia.»
  - S058 [repisa [seed]] «Si tú ves la repisa, la ve todo el mundo, incluido quien se beneficia de barrerla.»
  - S066 [flujo forzado [seed]] «Menos liquidez en reposo significa que el mismo flujo forzado mueve el precio mucho más.»
  - S069 [seed bolsa (obvious stop pool)] «Y mantén tus stops fuera de la bolsa obvia: más allá del nivel, no un tick dentro de él.»
  - S071 [combustible [seed]] «Combínalo con la lección 1: un funding unilateral más un clúster gordo en el lado concurrido es combustible cargado.»
  - S072 [non-seed "arder" (mercado preparado para arder)] «Los datos siguen sin predecir la chispa: te muestran un mercado preparado para arder.»
  - S074 [seed bolsa (stop pool)] «Los stops y los precios de liquidación se agrupan justo pasados el máximo y el mínimo obvios porque todos razonan igual, y un jugador grande que necesita ejecutar tamaño barre esa bolsa y recupera el nivel en una o dos velas.»
  - S075 [combustible [seed]] «Un barrido se convierte en un squeeze cuando la bolsa está concurrida y apalancada —acumulación, disparo, cascada, agotamiento—, así que la ventaja honesta es operar el agotamiento y nunca perseguir una cascada cuyo combustible es una bolsa finita de posiciones atrapadas.»
- **10 Metaphor then gloss** (1)
  - S013 [metaphor "repisa de stop-loss" glossed by colon: "la orden de venta protectora ... se coloca justo debajo del mínimo"] «Debajo de un mínimo reciente se sitúa una repisa de stop-loss de largos: la orden de venta protectora de un largo se coloca *justo debajo* del mínimo que "debería aguantar".»
- **11 Synonym rotation** (1)
  - S013 [stop/liquidation cluster: repisa (S013), zona (S014), banda (S023), bolsa de liquidez (S023), clúster (S032)] 
- **A absolutes** (5)
  - S013 [debería] «Debajo de un mínimo reciente se sitúa una repisa de stop-loss de largos: la orden de venta protectora de un largo se coloca *justo debajo* del mínimo que "debería aguantar".»
  - S038 [deben, deben] «Una liquidación es una orden *forzada* en la dirección que daña a la masa: los cortos cerrados por la fuerza deben comprar, los largos cerrados por la fuerza deben vender.»
  - S041 [nunca] «Sin más órdenes forzadas detrás, el movimiento que era pura mecánica simplemente se detiene, y normalmente rebota, porque nunca hubo nada duradero impulsándolo.»
  - S070 [nunca] «Cuando un squeeze está corriendo de verdad, la verdadera ventaja está en operar el agotamiento —contra la cascada—, nunca en perseguirla; y si no distingues en qué fase estás, la operación correcta es ninguna.»
  - S075 [nunca, summary] «Un barrido se convierte en un squeeze cuando la bolsa está concurrida y apalancada —acumulación, disparo, cascada, agotamiento—, así que la ventaja honesta es operar el agotamiento y nunca perseguir una cascada cuyo combustible es una bolsa finita de posiciones atrapadas.»

**EN** — 49 hits, 75 sentences, density 65.3

- **1 Filler** (7)
  - S002 [all the way (not in cand): "zooms all the way in", intensifier] «This lesson zooms all the way in to the order book: *where* the exits and protective orders are stacked, why price is so often drawn to run through them, and how, when the crowded side is leveraged, that run turns into a self-feeding cascade — a squeeze.»
  - S006 [crucially: emphasis tag] «Liquidity is resting orders waiting to be filled — limit orders and, crucially, *stop orders* parked at prices where they will trigger.»
  - S026 [exactly: emphatic, no quantity] «A shelf of stops is exactly that pool.»
  - S041 [simply: intensifier] «With no more forced orders behind it, the move that was pure mechanics simply stops — and usually snaps back, because nothing durable was ever driving it.»
  - S070 [actually: emphatic] «When a squeeze is actually running, the honest edge is fading exhaustion, never chasing the cascade — and if you cannot tell which phase you are in, the correct trade is none.»
  - S070 [honest: "the honest edge"] «When a squeeze is actually running, the honest edge is fading exhaustion, never chasing the cascade — and if you cannot tell which phase you are in, the correct trade is none.»
  - S075 [honest: "the honest edge"] «A sweep becomes a squeeze when the pool is crowded and leveraged — build, trigger, cascade, exhaustion — so the honest edge is fading the exhaustion, never chasing a cascade whose fuel is a finite pool of trapped positions.»
- **2 Rhythmic triad** (1)
  - S019 [the obvious swing low / the round number / the level that held twice; first and third overlap; drop "the obvious swing low"] «The obvious swing low, the round number, the level that held twice — that is where "put your stop just beyond it" sends thousands of orders to the same handful of ticks.»
- **4 Summary/uplift closer** (5)
  - S004 [editorial: framing line after "None of this predicts direction" (fuel/burn metaphor)] «It maps the fuel and shows you where the market tends to burn it.»
  - S011 [restate: repeats "keep these strictly apart" (S005) and the two definitions] «They pile up together, which is why the words get tangled — but they are not the same thing, and this lesson uses each one literally.»
  - S020 [restate: restates S018 "everyone is looking at the same chart"] «The map is not random; it is built by shared, predictable reasoning.»
  - S044 [editorial: "The same machine, mirrored"] «The same machine, mirrored.»
  - S072 [restate: repeats S003/S004 (does not predict; market primed to burn)] «The data still does not predict the spark; it shows you a market primed to burn.»
- **5 Sentence over 30 words** (11)
  - S002 [46w] «This lesson zooms all the way in to the order book: *where* the exits and protective orders are stacked, why price is so often drawn to run through them, and how, when the crowded side is leveraged, that run turns into a self-feeding cascade — a squeeze.»
  - S016 [31w **aside-only** (21w without asides)] «Above a recent high sits a shelf of short stop-losses — a short's protective buy order goes *just above* the high — plus the liquidation prices of leveraged shorts, which sit above entry.»
  - S019 [31w] «The obvious swing low, the round number, the level that held twice — that is where "put your stop just beyond it" sends thousands of orders to the same handful of ticks.»
  - S029 [55w] «Instead, in a single candle, price drops from the 26,200 it was trading at all the way to 25,350, cutting through the entire shelf: the long stop-losses trigger as market sells, the leveraged longs down there are liquidated (more forced selling), and all of that selling is absorbed by the large player's resting buy orders.»
  - S031 [32w **aside-only** (26w without asides)] «That is a sweep (a "stop run" or "liquidity grab"): the people who were stopped out and liquidated sold the exact low, and their orders were the liquidity someone else filled into.»
  - S032 [40w] «A sweep becomes a squeeze when the pool that fires is a *crowded, leveraged* one, so the orders that trigger are not just voluntary stops but liquidations — and each forced close pushes price into the next cluster of forced closes.»
  - S068 [31w] «Read the map as zones of volatility and likely sweeps, not as targets to trade toward: a cluster tells you where it may get violent, not which way the day ends.»
  - S070 [31w] «When a squeeze is actually running, the honest edge is fading exhaustion, never chasing the cascade — and if you cannot tell which phase you are in, the correct trade is none.»
  - S073 [31w] «Liquidity is resting orders waiting to be filled; liquidation is the exchange force-closing a leveraged position — they pile up in the same places, which is why the two words get tangled.»
  - S074 [39w] «Stops and liquidation prices cluster just beyond a recent high and a recent low because everyone reasons alike, and a large player who needs to fill size sweeps that pool and reclaims the level within a candle or two.»
  - S075 [37w] «A sweep becomes a squeeze when the pool is crowded and leveraged — build, trigger, cascade, exhaustion — so the honest edge is fading the exhaustion, never chasing a cascade whose fuel is a finite pool of trapped positions.»
- **7 No solo / not only** (1)
  - S032 «A sweep becomes a squeeze when the pool that fires is a *crowded, leveraged* one, so the orders that trigger are not just voluntary stops but liquidations — and each forced close pushes price into the next cluster of forced closes.»
- **9 Course-coined term** (22)
  - S004 [fuel [seed]] «It maps the fuel and shows you where the market tends to burn it.»
  - S013 [shelf [seed]] «Below a recent low sits a shelf of long stop-losses — a long's protective sell order goes *just under* the low that "should hold.»
  - S016 [shelf [seed]] «Above a recent high sits a shelf of short stop-losses — a short's protective buy order goes *just above* the high — plus the liquidation prices of leveraged shorts, which sit above entry.»
  - S023 [shelf [seed]] «That whole band is a dense shelf of resting sell orders — a pool of liquidity sitting right below price.»
  - S023 [liquidity pool [seed]] «That whole band is a dense shelf of resting sell orders — a pool of liquidity sitting right below price.»
  - S025 [seed pool (of opposite orders) — stop-cluster sense] «They need a pool of opposite orders to fill into quietly.»
  - S026 [shelf [seed]] «A shelf of stops is exactly that pool.»
  - S029 [shelf [seed]] «Instead, in a single candle, price drops from the 26,200 it was trading at all the way to 25,350, cutting through the entire shelf: the long stop-losses trigger as market sells, the leveraged longs down there are liquidated (more forced selling), and all of that selling is absorbed by the large player's resting buy orders.»
  - S032 [seed pool (stop/liquidation cluster)] «A sweep becomes a squeeze when the pool that fires is a *crowded, leveraged* one, so the orders that trigger are not just voluntary stops but liquidations — and each forced close pushes price into the next cluster of forced closes.»
  - S036 [fuel [seed]] «The fuel is loaded.»
  - S039 [shelf [seed]] «That forced flow moves price into the next shelf, which fires, which moves price again — self-feeding.»
  - S039 [forced flow [seed]] «That forced flow moves price into the next shelf, which fires, which moves price again — self-feeding.»
  - S047 [shelf [seed]] «The recent high is 3,000; short liquidation prices stack in shelves above it: around 3,050, 3,150, and 3,300.»
  - S050 [shelf [seed]] «That buying lifts price to 3,150, hitting the next shelf; those forced buys carry it to 3,300, hitting the next.»
  - S057 [seed pool (obvious stop pool)] «A second, quieter mistake: parking your own stop just inside an obvious pool.»
  - S058 [shelf [seed]] «If you can see the shelf, so can everyone — including whoever benefits from sweeping it.»
  - S066 [forced flow [seed]] «Less resting liquidity means the same forced flow moves price much further.»
  - S069 [seed pool (obvious stop pool)] «And keep your stops outside the obvious pool — beyond the level, not one tick inside it.»
  - S071 [fuel [seed]] «Combine that with lesson 1: one-sided funding plus a fat cluster on the crowded side is loaded fuel.»
  - S072 [non-seed "burn" (market primed to burn)] «The data still does not predict the spark; it shows you a market primed to burn.»
  - S074 [seed pool (stop pool)] «Stops and liquidation prices cluster just beyond a recent high and a recent low because everyone reasons alike, and a large player who needs to fill size sweeps that pool and reclaims the level within a candle or two.»
  - S075 [fuel [seed]] «A sweep becomes a squeeze when the pool is crowded and leveraged — build, trigger, cascade, exhaustion — so the honest edge is fading the exhaustion, never chasing a cascade whose fuel is a finite pool of trapped positions.»
- **10 Metaphor then gloss** (1)
  - S013 [metaphor "shelf of long stop-losses" glossed after dash: "a long's protective sell order goes just under the low"] «Below a recent low sits a shelf of long stop-losses — a long's protective sell order goes *just under* the low that "should hold.»
- **11 Synonym rotation** (1)
  - S013 [stop/liquidation cluster: shelf (S013), zone (S014), band (S023), pool of liquidity (S023), cluster (S032)] 
- **A absolutes** (3)
  - S038 [must, must] «A liquidation is a *forced* order in the direction that hurts the crowd: shorts force-closed must buy, longs force-closed must sell.»
  - S070 [never] «When a squeeze is actually running, the honest edge is fading exhaustion, never chasing the cascade — and if you cannot tell which phase you are in, the correct trade is none.»
  - S075 [never, summary] «A sweep becomes a squeeze when the pool is crowded and leveraged — build, trigger, cascade, exhaustion — so the honest edge is fading the exhaustion, never chasing a cascade whose fuel is a finite pool of trapped positions.»

### m20-l1

**ES** — 34 hits, 79 sentences, density 43.0

- **1 Filler** (8)
  - S002 [realmente: "cuántos son negociables hoy" already carries it] «La tokenómica es la cara de la oferta de esa historia: cuántos tokens existen, cuántos son realmente negociables hoy y cuántos más están programados para llegar.»
  - S008 [de verdad: emphatic] «Es la oferta circulante que de verdad fija el precio, porque es todo lo que el mercado puede negociar hoy.»
  - S022 [sencillamente: intensifier] «Si no entra dinero nuevo —el market cap se queda en 500 millones—, el precio pasa a ser sencillamente 500 / 650 = $0,77, una caída del 23%, y ni un solo poseedor tuvo que cambiar de opinión.»
  - S024 [Dicho al revés (not in cand): announcer of a restatement; also "para no moverse del sitio" repeats "mantener el precio plano"] «Dicho al revés: solo para mantener el precio plano en $1,00, el mercado tiene que absorber un 30% más de tokens, lo que significa 150 millones de dólares de compra nueva para no moverse del sitio.»
  - S038 [announcer sentence (not in cand): "Este es el montaje que pilla a los principiantes."] «Este es el montaje que pilla a los principiantes.»
  - S046 [simplemente: deletable ("para que el precio se mantenga")] «Para que el precio simplemente *se mantenga* en $3, el mercado tiene que absorber 920.000.000 × $3 = 2.760 millones de dólares de oferta nueva: más de once veces los 240 millones de oferta circulante que hoy sostienen el precio.»
  - S063 [de verdad: deletable ("antes de que los tokens se muevan")] «El movimiento puede estar medio hecho antes de que los tokens se muevan de verdad.»
  - S070 [announcer (not in cand): "La idea única que llevarte de aquí:"] «La idea única que llevarte de aquí: un desbloqueo programado es un shock de oferta que el gráfico no puede mostrar.»
- **2 Rhythmic triad** (2)
  - S034 [el mismo token / el mismo precio / el mismo instante; drop "el mismo instante"] «El mismo token, el mismo precio, el mismo instante, y dos valoraciones que se diferencian en 10×.»
  - S058 [una ruptura limpia / una tendencia de apoyo / un setup de manual; third covers the other two; drop "un setup de manual"] «Una ruptura limpia, una tendencia de apoyo, un setup de manual: todo eso puede quedar invalidado por un desbloqueo programado que el gráfico no tenía forma de mostrar.»
- **4 Summary/uplift closer** (5)
  - S026 [restate: repeats S025 (invisible en la vela = nunca aparece como patrón)] «Un token que infla en silencio un 30% al año pelea contra un lastre anual del 30% que nunca aparece como un patrón.»
  - S037 [editorial: "la distancia entre ambos es una etiqueta de advertencia"] «No son el mismo número, y la distancia entre ambos es una etiqueta de advertencia.»
  - S049 [editorial: "no es una ganga: es una factura que aún no ha llegado"] «Un market cap modesto bajo una FDV gigantesca no es una ganga: es una factura que aún no ha llegado.»
  - S056 [editorial: "no por nada que el patrón hiciera mal"] «El precio cae por la aritmética de la oferta, no por nada que el patrón hiciera mal.»
  - S059 [restate: repeats S057/S058 (la oferta anula el patrón)] «La llegada de oferta nueva para venderse es una fuerza fundamental que anula el patrón.»
- **5 Sentence over 30 words** (15)
  - S001 [34w] «Dos tokens pueden cotizar al mismo precio y valer cantidades muy distintas, y uno de ellos puede estar preparado en silencio para caer por razones que no tienen nada que ver con el gráfico.»
  - S009 [31w **aside-only** (28w without asides)] «La oferta total es todo lo emitido hasta la fecha, incluidos los tokens bloqueados, en vesting o reservados (equipo, tesorería, inversores) y que, por tanto, aún no están en el mercado.»
  - S022 [36w **aside-only** (28w without asides)] «Si no entra dinero nuevo —el market cap se queda en 500 millones—, el precio pasa a ser sencillamente 500 / 650 = $0,77, una caída del 23%, y ni un solo poseedor tuvo que cambiar de opinión.»
  - S024 [36w] «Dicho al revés: solo para mantener el precio plano en $1,00, el mercado tiene que absorber un 30% más de tokens, lo que significa 150 millones de dólares de compra nueva para no moverse del sitio.»
  - S046 [38w] «Para que el precio simplemente *se mantenga* en $3, el mercado tiene que absorber 920.000.000 × $3 = 2.760 millones de dólares de oferta nueva: más de once veces los 240 millones de oferta circulante que hoy sostienen el precio.»
  - S052 [34w **aside-only** (20w without asides)] «Pero un desbloqueo grande —un "cliff", en el que un tramo grande se libera en una sola fecha— puede volcar al mercado más oferta en un día de la que absorbe el trading normal.»
  - S054 [45w] «Un cliff desbloquea ahora un tramo de 20 millones de tokens de inversores en una sola fecha: un salto del 20% en la oferta circulante de la noche a la mañana, y dos días y medio de volumen normal volcados sobre el libro de golpe.»
  - S055 [39w] «Aunque solo se venda un tercio de ese tramo, son unos 6,7 millones de tokens buscando compradores contra un libro que normalmente despacha 8 millones en un *día*: casi un día entero extra de ventas comprimido en unas horas.»
  - S060 [33w **aside-only** (19w without asides)] «Los mercados tradicionales también tienen vencimientos de bloqueo —los de dentro no pueden vender el primer día de una salida a bolsa—, pero el cripto vuelve el mecanismo mucho más nítido, y público.»
  - S062 [37w] «Como el shock es *conocido*, tiende a anticiparse (front-run): el precio suele debilitarse en los días *previos* a un desbloqueo grande a medida que los operadores informados se posicionan por delante, no solo el día en sí.»
  - S065 [33w] «No hay sesión nocturna que digiera la oferta nueva ni pausa que frene una caída: las mismas condiciones que vuelven feroces a las cascadas de liquidación vuelven feroces a los volcados de desbloqueo.»
  - S076 [32w] «Revisa el calendario de desbloqueo en busca de liberaciones grandes cerca de tu horizonte de operación, y trata un cliff cercano como un motivo de cautela que el gráfico no puede darte.»
  - S077 [50w] «La tokenómica es la cara de la oferta que un gráfico no puede mostrar: la oferta circulante es lo que se negocia hoy, la total es todo lo emitido, la máxima es el techo, y el hueco entre circulante y máxima es oferta futura que ya hace cola para llegar.»
  - S078 [45w] «El market cap es precio × circulante y la FDV es precio × máxima, así que un mismo token a un mismo precio lleva dos valoraciones que pueden diferir en diez veces: un cap modesto bajo una FDV gigantesca es una factura que todavía no ha llegado.»
  - S079 [41w] «La emisión diluye a los poseedores de forma mecánica cambie o no alguien de opinión, y un unlock grande y programado es un shock de oferta que invalida un setup limpio, así que lee el calendario antes de fiarte del patrón.»
- **10 Metaphor then gloss** (2)
  - S011 [metaphor "el techo" glossed after colon: "la mayor cantidad de tokens que existirá jamás"] «La oferta máxima es el techo: la mayor cantidad de tokens que existirá *jamás*, una vez ocurridas todas las emisiones programadas.»
  - S036 [metaphor "el techo hipotético" glossed: "una cifra de 'y si estuviera todo fuera'"] «La FDV es el techo hipotético, una cifra de "y si estuviera todo fuera".»
- **11 Synonym rotation** (2)
  - S023 [inflation drag: dilución (S023), viento en contra (S025), lastre anual (S026)] 
  - S050 [token release event: desbloqueo (S050), liberaciones (S076), unlock (S079, English word in ES text)] 
- **A absolutes** (1)
  - S026 [nunca] «Un token que infla en silencio un 30% al año pelea contra un lastre anual del 30% que nunca aparece como un patrón.»

**EN** — 28 hits, 79 sentences, density 35.4

- **1 Filler** (9)
  - S002 [actually: "how many are tradable today" already carries it] «Tokenomics is the supply side of that story: how many tokens exist, how many are actually tradable today, and how many more are scheduled to arrive.»
  - S008 [actually: emphatic] «This is the float that actually sets the price, because it is all the market can currently trade.»
  - S022 [simply: intensifier] «If no fresh money arrives — the market cap stays $500 million — the price is simply 500 / 650 = $0.77, a 23% fall, and not one holder had to change their mind.»
  - S024 [Put the other way round (not in cand): announcer of a restatement; also "to stand still" repeats "hold the price flat"] «Put the other way round: just to hold the price flat at $1.00, the market has to absorb 30% more tokens, which means $150 million of new buying to stand still.»
  - S038 [announcer sentence (not in cand): "Here is the setup that catches beginners."] «Here is the setup that catches beginners.»
  - S046 [merely (not in cand): deletable, mirrors ES simplemente] «For the price to merely *hold* at $3, the market has to absorb 920,000,000 × $3 = $2.76 billion of new supply — more than eleven times the $240 million float that is holding the price up today.»
  - S055 [actually: deletable ("only a third of that tranche sells")] «Even if only a third of that tranche actually sells, that is ~6.7 million tokens hunting for bids against a book that normally clears 8 million in a *day* — almost a full extra day of selling compressed into hours.»
  - S063 [actually: deletable ("before the tokens move")] «The move can be half over before the tokens actually move.»
  - S070 [announcer (not in cand): "The single idea to carry out of this:"] «The single idea to carry out of this: a scheduled unlock is a supply shock the chart cannot show.»
- **2 Rhythmic triad** (2)
  - S034 [same token / same price / same instant; drop "same instant"] «Same token, same price, same instant — and two valuations that differ by 10×.»
  - S058 [a clean breakout / a supportive trend / a textbook setup; third covers the other two; drop "a textbook setup"] «A clean breakout, a supportive trend, a textbook setup — all of it can be invalidated by a scheduled unlock the chart had no way of showing.»
- **4 Summary/uplift closer** (5)
  - S026 [restate: repeats S025 (invisible on a candle = never shows up as a pattern)] «A token quietly inflating 30% a year is fighting a 30% annual drag that never shows up as a pattern.»
  - S037 [editorial: "the distance between them is a warning label"] «They are not the same number, and the distance between them is a warning label.»
  - S049 [editorial: "not a bargain — it is a bill that has not arrived yet"] «A modest market cap sitting under a gigantic FDV is not a bargain — it is a bill that has not arrived yet.»
  - S056 [editorial: "not by anything the pattern did wrong"] «Price gets pushed down by the arithmetic of supply, not by anything the pattern did wrong.»
  - S059 [restate: repeats S057/S058 (supply overrides the pattern)] «New supply arriving to be sold is a fundamental force that overrides the pattern.»
- **5 Sentence over 30 words** (9)
  - S001 [35w] «Two tokens can trade at the same price and be worth wildly different amounts — and one of them can be quietly set up to fall for reasons that have nothing to do with the chart.»
  - S024 [31w] «Put the other way round: just to hold the price flat at $1.00, the market has to absorb 30% more tokens, which means $150 million of new buying to stand still.»
  - S046 [35w] «For the price to merely *hold* at $3, the market has to absorb 920,000,000 × $3 = $2.76 billion of new supply — more than eleven times the $240 million float that is holding the price up today.»
  - S054 [33w] «A cliff now unlocks a 20-million-token investor tranche on one date — a 20% jump in the float overnight, and two and a half days of normal volume dropped onto the book at once.»
  - S055 [39w] «Even if only a third of that tranche actually sells, that is ~6.7 million tokens hunting for bids against a book that normally clears 8 million in a *day* — almost a full extra day of selling compressed into hours.»
  - S062 [33w] «Because the shock is *known*, it tends to be front-run: price frequently weakens in the days *before* a big unlock as informed players position ahead of it, not just on the day itself.»
  - S077 [39w] «Tokenomics is the supply side a chart cannot show: circulating supply is what trades today, total supply is everything minted, max supply is the ceiling, and the gap between circulating and max is future supply already queued to arrive.»
  - S078 [41w] «Market cap is price × circulating and FDV is price × max, so one token at one price carries two valuations that can differ by ten times — a modest cap sitting under a gigantic FDV is a bill that has not arrived yet.»
  - S079 [34w] «Emission dilutes holders mechanically whether or not anyone changes their mind, and a large scheduled unlock is a supply shock that overrides a clean setup, so read the calendar before you trust the pattern.»
- **10 Metaphor then gloss** (2)
  - S011 [metaphor "the ceiling" glossed after colon: "the most tokens that will ever exist"] «Max supply is the ceiling: the most tokens that will *ever* exist, once every scheduled emission has happened.»
  - S036 [metaphor "the hypothetical ceiling" glossed: "a 'what if everything were out' figure"] «FDV is the hypothetical ceiling, a "what if everything were out" figure.»
- **11 Synonym rotation** (1)
  - S023 [inflation drag: dilution (S023), headwind (S025), annual drag (S026)] 
- **A absolutes** (1)
  - S026 [never] «A token quietly inflating 30% a year is fighting a 30% annual drag that never shows up as a pattern.»

### m21-l1

**ES** — 36 hits, 72 sentences, density 50.0

- **1 Filler** (9)
  - S010 [exactamente: emphatic, no quantity] «Tu posición no tiene ninguna opinión sobre el precio, que es exactamente de lo que se trata.»
  - S019 [honesta: "su forma honesta"] «Esa es su forma honesta: un rendimiento anual de en torno al 5%, delta neutral, sobre una cantidad grande de capital, a cambio de llevar dos posiciones en un exchange.»
  - S021 [Fíjate: announcer] «Fíjate también en lo que *no* es: no es un 5% de tu cuenta al año a menos que tengas la cuenta entera metida, y no es gratis: el capital queda inmovilizado, y no hacer nada con 120.000 USDT no te habría dado nada pero tampoco habría necesitado ningún exchange.»
  - S023 [justo (not in cand): "que es justo por lo que", emphatic] «En parte no lo han dejado: hay mesas haciéndolo con tamaño, que es justo por lo que la prima de las monedas grandes suele quedarse bastante por debajo de una décima de punto porcentual.»
  - S030 [justo (not in cand): "se ensancha justo cuando", emphatic] «Y el corolario que sí puedes usar: el hueco se ensancha justo cuando la masa está más loca.»
  - S032 ["que es otra forma de decir que" (not in cand): reformulation announcer] «Ahí es cuando el carry paga de forma espectacular, que es otra forma de decir que el rendimiento del carry es un termómetro de la manía del apalancamiento, la misma lectura que hace m19-l1 desde el otro lado de la mesa.»
  - S033 [announcer sentence (not in cand): "Aquí está la mitad que no cuenta ningún vendedor de cursos."] «Aquí está la mitad que no cuenta ningún vendedor de cursos.»
  - S042 [justo (not in cand): "justo en el momento en el que", emphatic] «Dos patas en dos exchanges son dos riesgos de contraparte, más la transferencia entre ellos justo en el momento en el que menos te apetece que una transferencia vaya lenta.»
  - S045 [announcer sentence (not in cand): "Esta es la que hay que grabarse a fuego"] «**Esta es la que hay que grabarse a fuego, y es donde vuelve m06, la liquidación.**»
- **2 Rhythmic triad** (2)
  - S003 [existe / es enorme / se le vende ... como dinero gratis; drop "existe"] «Esta lección se mete a vivir dentro de esa frase, porque la operación que describe existe, es enorme y se le vende a los principiantes como dinero gratis.»
  - S068 [modesto / hambriento de capital / márgenes exigentes / riesgo de cola (4 items for rhythm); "modesto" overlaps with the margin item; drop "modesto"] «La convierte en un negocio: modesto, hambriento de capital, con márgenes exigentes en lo operativo y con un riesgo de cola que hay que gestionar activamente en vez de cubrir.»
- **3 Rhetorical question** (2)
  - S011 «¿Y para qué mantenerla?»
  - S022 «Si esto es un retorno esperado positivo sin riesgo direccional, ¿por qué lo ha dejado alguien ahí tirado?»
- **4 Summary/uplift closer** (7)
  - S005 [editorial: "la diferencia entre esas dos descripciones es la lección entera"] «Es un negocio de margen fino con colas gordas, y la diferencia entre esas dos descripciones es la lección entera.»
  - S010 [restate: delta neutral already explained in S009] «Tu posición no tiene ninguna opinión sobre el precio, que es exactamente de lo que se trata.»
  - S032 [restate: "que es otra forma de decir que..." plus cross-reference to m19-l1] «Ahí es cuando el carry paga de forma espectacular, que es otra forma de decir que el rendimiento del carry es un termómetro de la manía del apalancamiento, la misma lectura que hace m19-l1 desde el otro lado de la mesa.»
  - S037 [editorial: "Nada cambió en tu posición: cambió de lado el mercado"] «Nada cambió en tu posición: cambió de lado el mercado.»
  - S041 [editorial: "Ahí está la forma «margen fino, cola gorda» en una línea"] «Ahí está la forma «margen fino, cola gorda» en una línea: cobras cantidades pequeñas de forma fiable y pagas cantidades grandes de vez en cuando.»
  - S044 [editorial: "el «not your keys» de m02 disfrazado de estrategia"] «Las dos cosas son el «not your keys» de m02 disfrazado de estrategia: tu posición delta neutral es un derecho frente a un intermediario, y la neutralidad vale lo que valga el intermediario.»
  - S069 [editorial: compares to m23-l1 "descripción tramposa" (last prose unit)] «Vendida como «rendimiento sin riesgo», es la misma descripción tramposa que «más operaciones es más beneficio» en m23-l1: el número que se cita es real, y no es el número que decide el resultado.»
- **5 Sentence over 30 words** (14)
  - S009 [33w] «Ahora eres delta neutral: si el BTC se va a 70.000 ganas 10.000 en el spot y pierdes 10.000 en el corto; si se va a 50.000, los dos se cambian el papel.»
  - S021 [50w] «Fíjate también en lo que *no* es: no es un 5% de tu cuenta al año a menos que tengas la cuenta entera metida, y no es gratis: el capital queda inmovilizado, y no hacer nada con 120.000 USDT no te habría dado nada pero tampoco habría necesitado ningún exchange.»
  - S023 [34w] «En parte no lo han dejado: hay mesas haciéndolo con tamaño, que es justo por lo que la prima de las monedas grandes suele quedarse bastante por debajo de una décima de punto porcentual.»
  - S025 [36w] «Cada dólar metido aquí es un dólar que no está haciendo otra cosa, y ese 5% tiene que ganarle a lo que sea que ese dinero pudiera rendir en otro sitio, incluido, a veces, simplemente prestarlo.»
  - S032 [41w] «Ahí es cuando el carry paga de forma espectacular, que es otra forma de decir que el rendimiento del carry es un termómetro de la manía del apalancamiento, la misma lectura que hace m19-l1 desde el otro lado de la mesa.»
  - S044 [33w] «Las dos cosas son el «not your keys» de m02 disfrazado de estrategia: tu posición delta neutral es un derecho frente a un intermediario, y la neutralidad vale lo que valga el intermediario.»
  - S051 [42w] «Tu pata corta pierde 18.000 USDT contra el colateral que le pusieras y, si ese colateral eran 60.000, no pasa nada; pero si fuiste eficiente con el capital y pusiste 15.000, el corto se liquida mucho antes de que el rally termine.»
  - S053 [40w] «**Te quedas con la pata ganadora de una cobertura cuya pata perdedora ha sido cerrada al peor precio posible**, es decir, con un largo desnudo, en un mercado que acaba de subir un 30%, al que has entrado por accidente.»
  - S058 [31w] «La forma de sobrevivir a ello no tiene ningún glamur: pon detrás del corto bastante más colateral del que exige la aritmética y acepta el rendimiento menor que sale de ahí.»
  - S063 [49w] «La pérdida no está acotada por el mismo diseño, y no porque los precios puedan escaparse (no pueden hacerle daño a una posición cubierta), sino porque los fallos *operativos* no tienen techo: una pata liquidada, un exchange del que no puedes retirar, un funding que se queda en negativo.»
  - S066 [45w] «Un carry concurrido es un carry que paga menos, que es la prima de m19-l1 leída desde el otro lado de la mesa y la razón de que los rendimientos que se anuncian sean siempre los del periodo *anterior* a que llegara todo el mundo.»
  - S069 [34w] «Vendida como «rendimiento sin riesgo», es la misma descripción tramposa que «más operaciones es más beneficio» en m23-l1: el número que se cita es real, y no es el número que decide el resultado.»
  - S070 [46w] «El cash-and-carry es delta neutral por construcción —compra el spot, ponte corto en el perpetuo— y gana porque un funding positivo significa que los largos pagan a los cortos, lo que a una tasa normal son alrededor de un 5% anual sobre el capital que inmoviliza.»
  - S071 [61w] «No es dinero gratis sino un negocio de margen fino con colas gordas: el funding cambia de signo y te cobra con el mismo reloj, las dos patas son derechos frente a una plataforma y, sobre todo, delta neutral no es margen neutral: el exchange liquida una posición contra su propio colateral y no sabe que tu pata de spot existe.»
- **10 Metaphor then gloss** (1)
  - S044 [metaphor "«not your keys» disfrazado de estrategia" glossed after colon: "tu posición delta neutral es un derecho frente a un intermediario"] «Las dos cosas son el «not your keys» de m02 disfrazado de estrategia: tu posición delta neutral es un derecho frente a un intermediario, y la neutralidad vale lo que valga el intermediario.»
- **11 Synonym rotation** (1)
  - S001 [the funding trade: arbitraje (S001), la operación (S003), carry (S032), cash-and-carry (S070)] 
- **A absolutes** (2)
  - S052 [nunca] «El spot no lo rescata nunca.»
  - S066 [siempre] «Un carry concurrido es un carry que paga menos, que es la prima de m19-l1 leída desde el otro lado de la mesa y la razón de que los rendimientos que se anuncian sean siempre los del periodo *anterior* a que llegara todo el mundo.»

**EN** — 33 hits, 72 sentences, density 45.8

- **1 Filler** (11)
  - S010 [exactly: emphatic, no quantity] «Your position has no opinion about price at all, which is exactly the point.»
  - S019 [honest: "the honest shape of it"] «That is the honest shape of it: a 5%-ish annual yield, delta-neutral, on a large amount of capital, in exchange for running two positions on an exchange.»
  - S021 [Notice (not in cand): announcer] «Notice also what it is *not*: it is not 5% of your account per year unless your whole account is in it, and it is not free — the capital is locked, and doing nothing with 120,000 USDT would have earned you nothing but would also have needed no exchange.»
  - S023 [precisely: emphatic] «Partly they have not: desks run this at size, which is precisely why the premium on major coins normally sits well inside a tenth of a percent.»
  - S030 [actually: "the corollary you can actually use", deletable] «And the corollary you can actually use: the gap widens exactly when the crowd is maddest.»
  - S030 [exactly: "widens exactly when", emphatic] «And the corollary you can actually use: the gap widens exactly when the crowd is maddest.»
  - S032 ["which is another way of saying" (not in cand): reformulation announcer] «That is when the carry pays spectacularly, which is another way of saying the carry's yield is a leverage-mania thermometer, the same reading m19-l1 takes from the other side of the table.»
  - S033 [announcer sentence (not in cand): "Here is the half no course-seller mentions."] «Here is the half no course-seller mentions.»
  - S042 [exactly: "at exactly the moment", emphatic] «Two legs on two exchanges is two sets of counterparty risk, plus the transfer between them at exactly the moment you least want a transfer to be slow.»
  - S045 [announcer sentence (not in cand): "This is the one to burn into memory"] «**This is the one to burn into memory, and it is where m06, liquidation, comes back.**»
  - S058 [strictly (not in cand): "than the arithmetic strictly requires", intensifier] «The way to survive it is unglamorous: post far more collateral against the short than the arithmetic strictly requires, and accept the lower yield that follows.»
- **2 Rhythmic triad** (2)
  - S003 [it is real / it is enormous / it is sold to beginners as free money; drop "it is real"] «This lesson goes and lives inside that sentence, because the trade it describes is real, it is enormous, and it is sold to beginners as free money.»
  - S068 [modest / capital-hungry / operationally demanding margins / tail risk (4 items for rhythm); drop "modest"] «It makes it a business: modest, capital-hungry, operationally demanding margins, with a tail risk that has to be actively managed rather than hedged away.»
- **3 Rhetorical question** (2)
  - S011 «So why hold it?»
  - S022 «If this is a positive expected return with no directional risk, why has anyone left it lying there?»
- **4 Summary/uplift closer** (7)
  - S005 [editorial: "the difference between those two descriptions is the whole lesson"] «It is a thin-margin business with fat tails, and the difference between those two descriptions is the whole lesson.»
  - S010 [restate: delta-neutral already explained in S009] «Your position has no opinion about price at all, which is exactly the point.»
  - S032 [restate: "which is another way of saying..." plus cross-reference to m19-l1] «That is when the carry pays spectacularly, which is another way of saying the carry's yield is a leverage-mania thermometer, the same reading m19-l1 takes from the other side of the table.»
  - S037 [editorial: "Nothing about your position changed; the market changed sides"] «Nothing about your position changed; the market changed sides.»
  - S041 [editorial: "That is the thin-margin, fat-tail shape in one line"] «That is the thin-margin, fat-tail shape in one line: you collect small amounts, reliably, and pay large amounts occasionally.»
  - S044 [editorial: "m02's 'not your keys' wearing a strategy"] «Both are m02's "not your keys" wearing a strategy: your delta-neutral position is a claim on an intermediary, and the neutrality is only as good as the intermediary.»
  - S069 [editorial: compares to m23-l1 "misdescription" (last prose unit)] «Sold as "risk-free yield", it is the same misdescription as "more trades means more profit" in m23-l1 — the number quoted is real, and it is not the number that decides the outcome.»
- **5 Sentence over 30 words** (9)
  - S021 [49w] «Notice also what it is *not*: it is not 5% of your account per year unless your whole account is in it, and it is not free — the capital is locked, and doing nothing with 120,000 USDT would have earned you nothing but would also have needed no exchange.»
  - S032 [32w] «That is when the carry pays spectacularly, which is another way of saying the carry's yield is a leverage-mania thermometer, the same reading m19-l1 takes from the other side of the table.»
  - S051 [42w] «Your short leg is down 18,000 USDT against whatever collateral you posted for it, and if that collateral was 60,000 you are fine, but if you were efficient with capital and posted 15,000 the short is liquidated long before the rally ends.»
  - S053 [40w] «**You are left holding the winning leg of a hedge whose losing leg has been closed at the worst possible price** — which is to say, a naked long, in a market that has just gone up 30%, entered by accident.»
  - S063 [43w] «The downside is not bounded by the same design — not because prices can run away (they cannot hurt a hedged position) but because the *operational* failures are open-ended: a liquidated leg, an exchange you cannot withdraw from, a funding rate that stays negative.»
  - S066 [33w] «A crowded carry is a carry paying less — which is m19-l1's premium read from the other side of the table, and the reason the advertised yields belong to the period *before* everybody arrived.»
  - S069 [32w] «Sold as "risk-free yield", it is the same misdescription as "more trades means more profit" in m23-l1 — the number quoted is real, and it is not the number that decides the outcome.»
  - S070 [38w] «The cash-and-carry is delta-neutral by construction — buy the spot, short the perpetual — and it earns because positive funding means longs pay shorts, which at an ordinary rate is about 5% a year on the capital it ties up.»
  - S071 [53w] «It is not free money but a thin-margin business with fat tails: funding flips sign and bills you on the same clock, both legs are claims on a venue, and above all delta-neutral is not margin-neutral — the exchange liquidates a position against its own collateral and does not know your spot leg exists.»
- **10 Metaphor then gloss** (1)
  - S044 [metaphor "'not your keys' wearing a strategy" glossed after colon: "your delta-neutral position is a claim on an intermediary"] «Both are m02's "not your keys" wearing a strategy: your delta-neutral position is a claim on an intermediary, and the neutrality is only as good as the intermediary.»
- **11 Synonym rotation** (1)
  - S001 [the funding trade: arbitrage (S001), the trade (S003), carry (S032), cash-and-carry (S070)] 
- **A absolutes** (1)
  - S052 [never] «The spot never rescues it.»

### m21-l2

**ES** — 38 hits, 61 sentences, density 62.3

- **1 Filler** (16)
  - S003 [announcer sentence (not in cand): "esta vez se dice en voz alta:"] «Esta lección es la tercera aparición de un molde que ya conoces, y esta vez se dice en voz alta:»
  - S007 [absolutamente (not in cand): "no te dice absolutamente nada", intensifier] «Un evento programado te dice *en qué clase de mercado* estás a punto de estar —cuánta liquidez, cuánta volatilidad, quién es probable que se vea obligado a operar— y no te dice absolutamente nada sobre hacia dónde irá el precio.»
  - S010 [announcer sentence (not in cand): "Aquí lo tienes como evento."] «Aquí lo tienes como evento.»
  - S012 [announcer (not in cand): "Ese es todo el mecanismo, y ya tienes en la mano todas las herramientas para leerlo:"] «Ese es todo el mecanismo, y ya tienes en la mano todas las herramientas para leerlo:»
  - S023 [Simplemente: intensifier] «Simplemente llegó cuando todo el que tenía interés ya había actuado, y lo único que quedaba por pasar era el desposicionamiento.»
  - S024 [simplemente: "como si los mercados fueran simplemente veleidosos", deletable] ««Compra el rumor, vende la noticia» es el refrán más viejo de este negocio y suele soltarse sin ningún mecanismo detrás, como si los mercados fueran simplemente veleidosos.»
  - S032 [exactamente: emphatic, no quantity] «A la gente que llega *por* la noticia, que es exactamente cuando la noticia suena más fuerte y el flujo de compradores nuevos es mayor.»
  - S033 [announcer (not in cand): "Ese es todo el truco:"] «Ese es todo el truco: el evento confirmado es el momento de máxima demanda entrante, así que es el mejor momento para estar vendiendo.»
  - S035 [de verdad: "la lectura que de verdad sirve"] «Y de ahí sale la lectura que de verdad sirve: un evento que lleva semanas siendo público está en gran parte ya en el precio; uno que llega sin aviso no lo está.»
  - S036 [en realidad: deletable ("El refrán es una afirmación sobre...")] «El refrán es en realidad una afirmación sobre *cuánto tiempo ha tenido el mercado para prepararse*.»
  - S046 [justo (not in cand): "caen justo a la peor hora", emphatic] «Se publican con antelación, casi siempre son inofensivos y de vez en cuando caen justo a la peor hora.»
  - S048 [precisamente: emphatic] «Esta es la seria, y no es aleatoria: los exchanges se degradan cuando se dispara el volumen, que es precisamente cuando tienes una posición que necesita atención.»
  - S050 [emphatic tag sentence (not in cand): "No es una hipótesis."] «No es una hipótesis.»
  - S052 [tag (not in cand): "y se cierran fuerte"] «Aquí se cierran dos costuras, y se cierran fuerte:»
  - S058 [announcer (not in cand): "dicho una vez más"] «Y es el argumento del tercer riesgo del carry de m21-l1, dicho una vez más: una posición delta neutral cuyas patas están en una plataforma a la que no puedes llegar no es neutral, son dos posiciones gestionadas por el software de otro.»
  - S061 [justo (not in cand): "llegan justo cuando se dispara el volumen", emphatic] «Los vencimientos trimestrales y de opciones vuelcan flujo mecánico sobre el perpetuo, y el último punto del calendario es la propia plataforma: las caídas llegan justo cuando se dispara el volumen, y el motor de liquidación no se cae cuando se cae la app.»
- **2 Rhythmic triad** (1)
  - S040 [operaciones de carry / spreads de calendario / toda m21-l1; m21-l1 is the carry trade, overlaps item 1; drop "toda m21-l1"] «Un contrato con fecha converge al spot cuando vence, y todo lo construido sobre la diferencia entre él y el perpetuo —operaciones de carry, spreads de calendario, toda m21-l1— hay que cerrarlo o rolarlo en ese momento.»
- **3 Rhetorical question** (1)
  - S038 «¿Por qué mueven entonces el perpetuo los contratos con fecha y los vencimientos de opciones?»
- **4 Summary/uplift closer** (7)
  - S008 [editorial: "Con los calendarios se pierde dinero casi siempre por confundir lo primero con lo segundo"] «Con los calendarios se pierde dinero casi siempre por confundir lo primero con lo segundo.»
  - S010 [ahead: "Aquí lo tienes como evento."] «Aquí lo tienes como evento.»
  - S012 [editorial: "Ese es todo el mecanismo, y ya tienes en la mano todas las herramientas"] «Ese es todo el mecanismo, y ya tienes en la mano todas las herramientas para leerlo:»
  - S023 [restate: repeats S020 (lo conocido se anticipa; ya habían actuado)] «Simplemente llegó cuando todo el que tenía interés ya había actuado, y lo único que quedaba por pasar era el desposicionamiento.»
  - S025 [editorial/ahead: "El mecanismo es sencillo y va de quién tiene qué."] «El mecanismo es sencillo y va de quién tiene qué.»
  - S036 [restate: reformulates S035 (tiempo público = ya en el precio)] «El refrán es en realidad una afirmación sobre *cuánto tiempo ha tenido el mercado para prepararse*.»
  - S058 [restate: "dicho una vez más", repeats m21-l1 third risk (last prose unit)] «Y es el argumento del tercer riesgo del carry de m21-l1, dicho una vez más: una posición delta neutral cuyas patas están en una plataforma a la que no puedes llegar no es neutral, son dos posiciones gestionadas por el software de otro.»
- **5 Sentence over 30 words** (10)
  - S007 [40w **aside-only** (27w without asides)] «Un evento programado te dice *en qué clase de mercado* estás a punto de estar —cuánta liquidez, cuánta volatilidad, quién es probable que se vea obligado a operar— y no te dice absolutamente nada sobre hacia dónde irá el precio.»
  - S017 [46w] «Un fondo que lleva dieciocho meses esperando puede aguantar, puede vender en fuerza semanas después o puede haber cubierto la exposición con un corto mucho antes de la fecha, en cuyo caso la venta ya ocurrió, en el perpetuo, y el día del unlock está tranquilo.»
  - S021 [38w] «Es el mismo mecanismo que el «vender la noticia» de más abajo, y por eso los unlocks producen tantas veces una deriva a la baja durante semanas *antes* de la fecha y un rebote el día en cuestión.»
  - S035 [33w] «Y de ahí sale la lectura que de verdad sirve: un evento que lleva semanas siendo público está en gran parte ya en el precio; uno que llega sin aviso no lo está.»
  - S040 [37w **aside-only** (29w without asides)] «Un contrato con fecha converge al spot cuando vence, y todo lo construido sobre la diferencia entre él y el perpetuo —operaciones de carry, spreads de calendario, toda m21-l1— hay que cerrarlo o rolarlo en ese momento.»
  - S047 [31w] «Se pueden saber, así que se pueden esquivar: no abras una posición que necesitarías gestionar durante una ventana en la que la plataforma ya te ha avisado de que estará caída.»
  - S057 [43w] «Ese es el argumento entero a favor de que el stop de protección esté *puesto en el exchange* en vez de vivir en tu cabeza, y a favor de un tamaño de posición que sobreviva a un movimiento al que no puedas reaccionar.»
  - S058 [43w] «Y es el argumento del tercer riesgo del carry de m21-l1, dicho una vez más: una posición delta neutral cuyas patas están en una plataforma a la que no puedes llegar no es neutral, son dos posiciones gestionadas por el software de otro.»
  - S060 [57w] «Un unlock de tokens es oferta pública llegando a un libro, así que mídelo contra la profundidad y no contra la capitalización, y cuenta con que se anticipe: lo conocido se posiciona de antemano, que es el mecanismo del «vender la noticia», donde el evento confirmado es el momento de máxima demanda entrante a la que vender.»
  - S061 [44w] «Los vencimientos trimestrales y de opciones vuelcan flujo mecánico sobre el perpetuo, y el último punto del calendario es la propia plataforma: las caídas llegan justo cuando se dispara el volumen, y el motor de liquidación no se cae cuando se cae la app.»
- **9 Course-coined term** (2)
  - S023 [non-seed "desposicionamiento" (standard: deshacer posiciones / unwind; S039 uses "deshacer")] «Simplemente llegó cuando todo el que tenía interés ya había actuado, y lo único que quedaba por pasar era el desposicionamiento.»
  - S052 [non-seed "costuras" (module cross-links as seams)] «Aquí se cierran dos costuras, y se cierran fuerte:»
- **11 Synonym rotation** (1)
  - S045 [the trading venue: exchange (S045), plataforma (S047), la app (S049), empresa (S053)] 
- **A absolutes** (5)
  - S001 [nunca] «Parte de lo que mueve un mercado no está en el gráfico ni va a estarlo nunca.»
  - S008 [siempre] «Con los calendarios se pierde dinero casi siempre por confundir lo primero con lo segundo.»
  - S037 [nunca] «Los perpetuos no vencen nunca: para eso están (m04-l1).»
  - S046 [siempre] «Se publican con antelación, casi siempre son inofensivos y de vez en cuando caen justo a la peor hora.»
  - S059 [nunca, summary] «Un evento programado predice condiciones y nunca dirección: cuánta liquidez y cuánta volatilidad va a haber, y a quién pueden obligar a operar.»

**EN** — 39 hits, 61 sentences, density 63.9

- **1 Filler** (16)
  - S003 [announcer sentence (not in cand): "this time it gets said out loud:"] «This lesson is the third appearance of a mould you already know, and this time it gets said out loud:»
  - S007 [at all (not in cand): "tells you nothing at all", intensifier] «A scheduled event tells you *what kind of market* you are about to be in — how liquid, how volatile, who is likely to be forced to trade — and it tells you nothing at all about which way price will go.»
  - S010 [announcer sentence (not in cand): "Here it is as an event."] «Here it is as an event.»
  - S012 [announcer (not in cand): "That is the whole mechanism, and every tool you need to read it is already in your hands:"] «That is the whole mechanism, and every tool you need to read it is already in your hands:»
  - S023 [simply: intensifier] «It simply arrived after everybody who cared had already acted, and the last thing left to happen was the un-positioning.»
  - S024 [merely (not in cand): "as though markets were merely fickle", deletable] «"Buy the rumour, sell the news" is the oldest adage in this business, and it is usually offered with no mechanism at all — as though markets were merely fickle.»
  - S032 [exactly: emphatic, no quantity] «To the people who arrive *because* of the news, which is exactly when the news is loudest and the new-buyer flow is at its largest.»
  - S033 [announcer (not in cand): "That is the whole trick:"] «That is the whole trick: the confirmed event is the moment of maximum incoming demand, so it is the best moment to be selling into.»
  - S035 [actually: "the reading that is actually usable"] «And it gives you the reading that is actually usable: an event that has been public for weeks is largely in the price already; an event that arrives with no warning is not.»
  - S036 [really: deletable] «The adage is really a statement about *how long the market has had to prepare*.»
  - S046 [exactly: "at exactly the wrong hour", emphatic] «Published in advance, usually harmless, occasionally landing at exactly the wrong hour.»
  - S048 [precisely: emphatic] «This is the serious one, and it is not random: exchanges degrade when volume spikes, which is precisely when you have a position that needs attention.»
  - S050 [emphatic tag sentence (not in cand): "Not a hypothetical."] «Not a hypothetical.»
  - S052 [tag (not in cand): "and they close hard"] «Two seams close here, and they close hard:»
  - S058 [announcer (not in cand): "stated once more"] «And it is the argument for the carry's third risk in m21-l1 stated once more: a delta-neutral position whose legs sit on a venue you cannot reach is not neutral, it is two positions being managed by somebody else's software.»
  - S061 [exactly: "arrive exactly when volume spikes", emphatic] «Quarterly and options expiries drop mechanical flow onto the perpetual, and the last item on the calendar is the venue itself: outages arrive exactly when volume spikes, and the liquidation engine does not go down when the app does.»
- **2 Rhythmic triad** (1)
  - S040 [carry trades / calendar spreads / the whole of m21-l1; m21-l1 is the carry trade, overlaps item 1; drop "the whole of m21-l1"] «A dated contract converges to spot at settlement, and everything built on the difference between it and the perp — carry trades, calendar spreads, the whole of m21-l1 — has to be closed or rolled at that moment.»
- **3 Rhetorical question** (1)
  - S038 «So why do dated contracts and options expiries move the perp?»
- **4 Summary/uplift closer** (7)
  - S008 [editorial: "Traders lose money on calendars almost entirely by mistaking the first thing for the second"] «Traders lose money on calendars almost entirely by mistaking the first thing for the second.»
  - S010 [ahead: "Here it is as an event."] «Here it is as an event.»
  - S012 [editorial: "That is the whole mechanism, and every tool you need ... is already in your hands"] «That is the whole mechanism, and every tool you need to read it is already in your hands:»
  - S023 [restate: repeats S020 (known gets anticipated; already acted)] «It simply arrived after everybody who cared had already acted, and the last thing left to happen was the un-positioning.»
  - S025 [editorial/ahead: "The mechanism is simple and it is about who holds what."] «The mechanism is simple and it is about who holds what.»
  - S036 [restate: reformulates S035 (public for weeks = already in price)] «The adage is really a statement about *how long the market has had to prepare*.»
  - S058 [restate: "stated once more", repeats m21-l1 third risk (last prose unit)] «And it is the argument for the carry's third risk in m21-l1 stated once more: a delta-neutral position whose legs sit on a venue you cannot reach is not neutral, it is two positions being managed by somebody else's software.»
- **5 Sentence over 30 words** (9)
  - S007 [40w **aside-only** (28w without asides)] «A scheduled event tells you *what kind of market* you are about to be in — how liquid, how volatile, who is likely to be forced to trade — and it tells you nothing at all about which way price will go.»
  - S017 [45w] «A fund that has waited eighteen months may hold, may sell into strength weeks later, or may have hedged the exposure with a short long before the date — in which case the selling already happened, on the perp, and the unlock day itself is quiet.»
  - S021 [33w] «This is the same mechanism as "sell the news" below, and it is why unlocks so often produce a drift down for weeks *before* the date and a bounce on the day itself.»
  - S035 [33w] «And it gives you the reading that is actually usable: an event that has been public for weeks is largely in the price already; an event that arrives with no warning is not.»
  - S040 [36w **aside-only** (28w without asides)] «A dated contract converges to spot at settlement, and everything built on the difference between it and the perp — carry trades, calendar spreads, the whole of m21-l1 — has to be closed or rolled at that moment.»
  - S057 [33w] «This is the whole argument for the protective stop being *resting on the exchange* rather than living in your head, and for the position size that survives a move you cannot react to.»
  - S058 [40w] «And it is the argument for the carry's third risk in m21-l1 stated once more: a delta-neutral position whose legs sit on a venue you cannot reach is not neutral, it is two positions being managed by somebody else's software.»
  - S060 [55w] «A token unlock is public supply arriving in a book, so size it against the depth rather than the market cap and expect it to be anticipated — what is known gets positioned for, which is the mechanism behind "sell the news", where the confirmed event is the moment of maximum incoming demand to sell into.»
  - S061 [39w] «Quarterly and options expiries drop mechanical flow onto the perpetual, and the last item on the calendar is the venue itself: outages arrive exactly when volume spikes, and the liquidation engine does not go down when the app does.»
- **7 No solo / not only** (1)
  - S054 «Custody risk is not just about theft; it is about access at the moment access matters.»
- **9 Course-coined term** (3)
  - S023 [non-seed "un-positioning" (standard: unwinding; S039 uses "unwound")] «It simply arrived after everybody who cared had already acted, and the last thing left to happen was the un-positioning.»
  - S044 [forced flow [seed]] «Large expiries therefore concentrate real, forced flow into a narrow window — again in the perp — and the hours around them are unusually noisy.»
  - S052 [non-seed "seams" (module cross-links as seams)] «Two seams close here, and they close hard:»
- **11 Synonym rotation** (1)
  - S045 [the trading venue: exchange (S045), venue (S047), the app (S049), company (S053)] 
- **A absolutes** (3)
  - S001 [never] «Some of what moves a market is not on the chart and never will be.»
  - S037 [never] «Perpetuals never expire — that is the whole point of them (m04-l1).»
  - S059 [never, summary] «A scheduled event predicts conditions and never direction: how liquid and how volatile the market is about to be, and who may be forced to trade.»

### m22-l1

**ES** — 53 hits, 125 sentences, density 42.4

- **1 Filler** (14)
  - S011 [justo (not in cand): "justo cuando lo necesitas", emphatic] «La regla te reduce el tamaño automáticamente en un drawdown, justo cuando lo necesitas.»
  - S014 [totalmente (not in cand): "totalmente recuperable", intensifier] «Como el 1% se toma del saldo *actual* cada vez, las pérdidas se acumulan con suavidad: diez perdedoras seguidas te dejan con alrededor del 90,4% de la cuenta (0,99 elevado a diez), es decir, un 9,6% abajo aproximadamente: doloroso pero totalmente recuperable.»
  - S019 [perfectamente (not in cand): "perfectamente corriente", intensifier] «Un 1% por operación con 3 operaciones a la semana y un 1% por operación con 15 al día son exposiciones muy distintas por unidad de *tiempo*: el trader rápido puede encontrarse una racha de ocho perdedoras perfectamente corriente en una sola tarde —alrededor del 8% de la cuenta antes de cenar— mientras que el lento se encuentra la misma racha repartida en un mes, con margen de sobra para darse cuenta y frenar.»
  - S021 [honesta: "la elección honesta de la fracción"] «La fórmula no cambia en nada; lo que cambia es la elección honesta de la fracción.»
  - S037 [realmente: "donde la idea queda realmente invalidada", deletable] «El stop estructural sigue siendo el principal: va donde la idea queda realmente invalidada, nunca en "1,5 ATR" porque lo diga un múltiplo.»
  - S040 [honestas: "las dos respuestas honestas"] «La aritmética de arriba te entrega las dos respuestas honestas: ensancha el stop más allá del ruido y acepta el tamaño menor que eso impone, o deja pasar la operación.»
  - S044 [announcer (not in cand): "el asunto merece demostrarse de frente, porque la verdad es más útil que el eslogan"] «La fórmula de arriba ya lo refuta, pero el asunto merece demostrarse de frente, porque la verdad es más útil que el eslogan: el tamaño salió del stop, así que el apalancamiento no puede cambiarlo.»
  - S055 [de verdad: "Qué cambia de verdad", deletable] «**Qué cambia de verdad:**»
  - S057 [honesto: "el uso honesto del apalancamiento"] «Ese es el uso honesto del apalancamiento: la *misma* posición inmoviliza menos de tu saldo y deja capital libre para otras cosas.»
  - S062 [simplemente: intensifier] «Es simplemente irrelevante para esta operación.»
  - S069 [Fíjate: announcer ("Fíjate bien")] «Fíjate bien en qué cambió y qué no: la pérdida en sí no es mayor (`0,05 × 1.700 ≈ 85 USDT`, más comisiones).»
  - S081 [de verdad: "el ratio que de verdad decide"] «Pensar en R te libera de la cifra en dólares y te apunta al ratio que de verdad decide si ganas dinero: el tamaño de tus ganadoras *en relación con* tus perdedoras.»
  - S088 [exactamente: "Cómo se combinan exactamente", deletable] «(Cómo se combinan exactamente la tasa de acierto y el payoff en un valor esperado tiene su propia lección más adelante en el curso.)»
  - S089 [announcer sentence (not in cand): "Aquí está la aritmética que arruina a los traders sobreapalancados."] «Aquí está la aritmética que arruina a los traders sobreapalancados.»
- **4 Summary/uplift closer** (9)
  - S004 [ahead: points to the next lesson after the content ended] «Mantener varias a la vez, donde esos límites dejan de ser independientes, es la siguiente lección.»
  - S017 [motivate: "lo que te compra el derecho a equivocarte una y otra vez sin quedar fuera del juego"] «Un riesgo fijo y pequeño es lo que te compra el derecho a equivocarte una y otra vez sin quedar fuera del juego.»
  - S036 [restate: repeats S035 (el stop fija las unidades)] «Es el único dato que fija todo lo demás.»
  - S042 [restate: sums up S037-S041 (stop from structure, ATR veto)] «El stop sale de la estructura; el ATR solo veta un stop que el ruido se comería.»
  - S044 [editorial: "merece demostrarse de frente, porque la verdad es más útil que el eslogan"] «La fórmula de arriba ya lo refuta, pero el asunto merece demostrarse de frente, porque la verdad es más útil que el eslogan: el tamaño salió del stop, así que el apalancamiento no puede cambiarlo.»
  - S049 [restate: repeats S048 (los números salieron del presupuesto y del gráfico)] «El selector de apalancamiento no fue nunca un dato de entrada.»
  - S072 [editorial: "Tu stop dejó de ser tu stop."] «Tu stop dejó de ser tu stop.»
  - S075 [editorial/ahead: "problema de disciplina ... te espera en los fallos de más abajo"] «Eso es un problema de disciplina más que de aritmética, y te espera en los fallos de más abajo.»
  - S088 [ahead: "(... tiene su propia lección más adelante en el curso.)"] «(Cómo se combinan exactamente la tasa de acierto y el payoff en un valor esperado tiene su propia lección más adelante en el curso.)»
- **5 Sentence over 30 words** (26)
  - S001 [32w] «El hábito que separa a los traders que duran de los que se arruinan no es acertar con los ganadores: es decidir, *antes* de cada operación, exactamente cuánto están dispuestos a perder.»
  - S014 [42w] «Como el 1% se toma del saldo *actual* cada vez, las pérdidas se acumulan con suavidad: diez perdedoras seguidas te dejan con alrededor del 90,4% de la cuenta (0,99 elevado a diez), es decir, un 9,6% abajo aproximadamente: doloroso pero totalmente recuperable.»
  - S016 [32w **aside-only** (29w without asides)] «Compáralo ahora con un trader que arriesga el 20% por operación: dos malas decisiones (0,8 × 0,8 = 0,64) y la cuenta ya está un 36% abajo; tres y queda casi a la mitad.»
  - S019 [74w] «Un 1% por operación con 3 operaciones a la semana y un 1% por operación con 15 al día son exposiciones muy distintas por unidad de *tiempo*: el trader rápido puede encontrarse una racha de ocho perdedoras perfectamente corriente en una sola tarde —alrededor del 8% de la cuenta antes de cenar— mientras que el lento se encuentra la misma racha repartida en un mes, con margen de sobra para darse cuenta y frenar.»
  - S022 [46w] «Cuanto más rápido el estilo, más razones para quedarte en la parte baja —un 0,5% en vez de un 1%— y para limitar también el día además de la operación, que es para lo que sirve el freno diario del módulo del plan de trading (m27-l1).»
  - S028 [44w **aside-only** (23w without asides)] «Decide dónde va tu stop —el precio al que admites que la operación está equivocada— y mide la distancia de la entrada a ese stop. → digamos que el stop está a 250 puntos (un "punto" aquí es una unidad de precio en el gráfico).»
  - S039 [81w] «Compáralo con el ATR de la temporalidad en la que entraste —la regla de m16-l1 para cuánto recorre una barra típica— y, si la distancia de la entrada al stop queda bastante por debajo de un ATR, la operación está apostando a que no ocurrirá una barra corriente. m06-l1 ya enseñó lo que el ruido normal le hace a un precio que importa; la única diferencia aquí es que llega a tu stop en vez de a tu precio de liquidación.»
  - S041 [31w **aside-only** (19w without asides)] «Lo que esto *no* es: dimensionar desde la volatilidad —recortar a la mitad cada posición porque la semana se puso violenta—, que es otra disciplina y queda fuera de este curso.»
  - S043 [31w] «La confusión de principiante más habitual de todo el curso es creer que el selector de apalancamiento *es* el mando del riesgo, que 20× es cuatro veces más peligroso que 5×.»
  - S044 [35w] «La fórmula de arriba ya lo refuta, pero el asunto merece demostrarse de frente, porque la verdad es más útil que el eslogan: el tamaño salió del stop, así que el apalancamiento no puede cambiarlo.»
  - S071 [33w] «Estás fuera de una operación cuya tesis seguía viva, a un precio que no elegiste, y una posición que cerró el exchange no se puede reabrir al precio desde el que pretendías aguantar.»
  - S074 [40w] «A 20× el mismo saldo puede sostener posiciones cuyo tamaño conjunto no aprobó ningún presupuesto de riesgo, así que el apalancamiento alto no añade riesgo a una operación *dimensionada*: quita la fricción que antes te impedía tomar una sin dimensionar.»
  - S081 [32w] «Pensar en R te libera de la cifra en dólares y te apunta al ratio que de verdad decide si ganas dinero: el tamaño de tus ganadoras *en relación con* tus perdedoras.»
  - S099 [52w] «Cada punto porcentual más de drawdown retira capital *y* sube el listón de la recuperación a la vez, así que la curva se vuelve en tu contra más rápido cuanto más profundo caes: esa es toda la razón para limitar el riesgo por operación antes de acercarte siquiera a un pozo profundo.»
  - S100 [35w] «Dos de las trampas anteriores son tan habituales que merecen nombrarse aparte: dimensionar por la recompensa en vez de por el stop, y creer que "una pérdida del 50% solo necesita una ganancia del 50%".»
  - S110 [45w] «Puedes estar temerariamente sobredimensionado a 2× y perfectamente dimensionado a 20×: es la demostración de los dos escenarios de más arriba, y lo único que decide el número de apalancamiento en una operación bien dimensionada es si la liquidación puede alcanzarte antes que tu stop.»
  - S112 [32w] «Un movimiento del 10–15% en un día es corriente en una altcoin y sería una sacudida de las que se ven una vez cada diez años en una acción de primera línea.»
  - S113 [38w] «Dimensiona una posición de cripto como si un movimiento del 2% fuera el peor caso y un martes cualquiera tocará tu stop; sobredimensiónala con apalancamiento encima y ese mismo martes puede llevarse una gran parte de la cuenta.»
  - S114 [31w **aside-only** (24w without asides)] «El apalancamiento por sí solo no añade riesgo *si* dimensionas desde el stop —esa es la demostración de más arriba—, pero el cripto es lo que hace que importe el *colchón*.»
  - S115 [36w] «El caso de 20× dejaba solo 700 puntos entre el stop y la liquidación, alrededor del 1,2% del precio, y en un mercado rápido el precio puede saltar por encima de un stop más de eso.»
  - S116 [37w] «Un margen que parece seguro en un gráfico tranquilo no es automáticamente seguro en una cascada, y esa es la razón práctica para quedarse bastante por debajo del punto de cruce en lugar de justo por debajo.»
  - S119 [46w **aside-only** (21w without asides)] «En un movimiento violento —una cascada de liquidaciones, una caída del exchange, la liquidez escasa de un fin de semana, una noticia repentina a las 3 de la madrugada— el precio puede saltar de golpe por encima de tu stop y te ejecutan bastante más allá.»
  - S121 [34w] «Trata el 1% como un techo que aguanta en condiciones tranquilas, no como un suelo que el exchange garantiza, y dimensiona dejando algo de margen para que la ejecución salga peor de lo previsto.»
  - S122 [35w] «Arriesga una fracción fija y pequeña de la cuenta en cada operación —normalmente el 1%—, porque las rachas de pérdidas son normales y una fracción de un saldo que encoge te reduce el tamaño automáticamente.»
  - S123 [34w] «Dimensiona la posición desde el stop y no al revés: presupuesto de riesgo ÷ distancia del stop da las unidades, así que un stop más ancho fuerza una posición más pequeña para el mismo dinero.»
  - S124 [31w] «El apalancamiento no es el mando del riesgo, porque el tamaño ya salió del stop; el único criterio para elegirlo es que la liquidación nunca llegue a ser tu stop efectivo.»
- **9 Course-coined term** (1)
  - S022 [non-seed "freno diario" (standard: límite de pérdida diaria; EN uses "daily stop")] «Cuanto más rápido el estilo, más razones para quedarte en la parte baja —un 0,5% en vez de un 1%— y para limitar también el día además de la operación, que es para lo que sirve el freno diario del módulo del plan de trading (m27-l1).»
- **10 Metaphor then gloss** (1)
  - S043 [metaphor "el mando del riesgo" glossed: "que 20× es cuatro veces más peligroso que 5×"] «La confusión de principiante más habitual de todo el curso es creer que el selector de apalancamiento *es* el mando del riesgo, que 20× es cuatro veces más peligroso que 5×.»
- **11 Synonym rotation** (2)
  - S043 [leverage setting: selector de apalancamiento (S043), ajuste de apalancamiento (S045), mando (S066)] 
  - S064 [gap between stop and liquidation: colchón (S064), margen de seguridad (S065), margen (S116)] 
- **A absolutes** (5)
  - S037 [nunca] «El stop estructural sigue siendo el principal: va donde la idea queda realmente invalidada, nunca en "1,5 ATR" porque lo diga un múltiplo.»
  - S049 [nunca] «El selector de apalancamiento no fue nunca un dato de entrada.»
  - S098 [debes] «Ir de 100 → 50 es una pérdida del 50%, pero subir de 50 → 100 es una ganancia del +100%, porque el 50 que debes duplicar es ahora toda tu cuenta.»
  - S117 [nunca] «Cripto no cierra nunca, lo que suena más seguro que un mercado que abre un hueco (gap) el fin de semana; no lo es.»
  - S124 [nunca, summary] «El apalancamiento no es el mando del riesgo, porque el tamaño ya salió del stop; el único criterio para elegirlo es que la liquidación nunca llegue a ser tu stop efectivo.»

**EN** — 43 hits, 126 sentences, density 34.1

- **1 Filler** (13)
  - S011 [exactly: "exactly when you need it to", emphatic] «The rule sizes you down automatically in a drawdown — exactly when you need it to.»
  - S014 [fully (not in cand): "fully recoverable", intensifier] «Since 1% is taken from the *current* balance each time, losses compound gently: ten losers in a row leave you with about 90.4% of the account (0.99 to the power of ten), i.e. down roughly 9.6% — painful but fully recoverable.»
  - S019 [perfectly (not in cand): "perfectly ordinary", intensifier] «1% per trade at 3 trades a week and 1% per trade at 15 trades a day are very different exposures per unit of *time*: the fast trader can meet a perfectly ordinary run of eight losers in a single afternoon — roughly 8% of the account gone before dinner — while the slow one meets the identical streak spread over a month, with plenty of room to notice and slow down.»
  - S021 [honest: "the honest choice of fraction"] «None of the formula changes; what changes is the honest choice of fraction.»
  - S040 [honest: "both honest answers"] «The arithmetic above hands you both honest answers: widen the stop past the noise and take the smaller size it forces, or leave the trade alone.»
  - S044 [announcer (not in cand): "the point deserves to be shown head-on, because the truth is more useful than the slogan"] «The formula above already refutes it, but the point deserves to be shown head-on, because the truth is more useful than the slogan: the size came from the stop, so the leverage cannot change it.»
  - S055 [actually: "What actually changes", deletable] «**What actually changes:**»
  - S057 [honest: "the honest use of leverage"] «That is the honest use of leverage: the *same* position ties up less of your balance, leaving capital free for other things.»
  - S062 [simply: intensifier] «It is simply irrelevant to this trade.»
  - S069 [Note (not in cand): announcer ("Note carefully what did and did not change")] «Note carefully what did and did not change: the loss itself is no bigger (`0.05 × 1,700 ≈ 85 USDT`, plus fees).»
  - S081 [actually: "the ratio that actually decides"] «Thinking in R frees you from the dollar amount and points you at the ratio that actually decides whether you make money: the size of your winners *relative to* your losers.»
  - S088 [Exactly: "Exactly how win rate and payoff combine", deletable] «(Exactly how win rate and payoff combine into an expected value has its own lesson later in the course.)»
  - S089 [announcer sentence (not in cand): "Here is the arithmetic that ruins over-leveraged traders."] «Here is the arithmetic that ruins over-leveraged traders.»
- **4 Summary/uplift closer** (9)
  - S004 [ahead: points to the next lesson after the content ended] «Holding several at once, where those caps stop being independent, is the next lesson.»
  - S017 [motivate: "what buys you the right to be wrong repeatedly without being removed from the game"] «A small fixed risk is what buys you the right to be wrong repeatedly without being removed from the game.»
  - S036 [restate: repeats S035 (the stop sets the units)] «It is the single input that fixes everything else.»
  - S042 [restate: sums up S037-S041 (stop from structure, ATR veto)] «The stop comes from structure; the ATR only vetoes a stop the noise would eat.»
  - S044 [editorial: "deserves to be shown head-on, because the truth is more useful than the slogan"] «The formula above already refutes it, but the point deserves to be shown head-on, because the truth is more useful than the slogan: the size came from the stop, so the leverage cannot change it.»
  - S049 [restate: repeats S048 (numbers came from the budget and the chart)] «The leverage selector was never an input.»
  - S072 [editorial: "Your stop stopped being your stop."] «Your stop stopped being your stop.»
  - S075 [editorial/ahead: "a discipline problem ... waiting for you in the failure modes below"] «That is a discipline problem rather than an arithmetic one, and it is waiting for you in the failure modes below.»
  - S088 [ahead: "(... has its own lesson later in the course.)"] «(Exactly how win rate and payoff combine into an expected value has its own lesson later in the course.)»
- **5 Sentence over 30 words** (18)
  - S014 [40w] «Since 1% is taken from the *current* balance each time, losses compound gently: ten losers in a row leave you with about 90.4% of the account (0.99 to the power of ten), i.e. down roughly 9.6% — painful but fully recoverable.»
  - S019 [70w] «1% per trade at 3 trades a week and 1% per trade at 15 trades a day are very different exposures per unit of *time*: the fast trader can meet a perfectly ordinary run of eight losers in a single afternoon — roughly 8% of the account gone before dinner — while the slow one meets the identical streak spread over a month, with plenty of room to notice and slow down.»
  - S022 [41w] «The faster the style, the stronger the case for sitting at the low end — 0.5% rather than 1% — and for capping the day as well as the trade, which is what the daily stop in the trading-plan module (m27-l1) is for.»
  - S028 [42w **aside-only** (21w without asides)] «Decide where your stop goes — the price at which you admit the trade is wrong — and measure the distance from entry to that stop. → say the stop sits 250 points away (a "point" here is one unit of price on the chart).»
  - S039 [68w] «Measure it against the ATR of the timeframe you entered on — m16-l1's ruler for how far a typical bar travels — and if the entry-to-stop distance sits much under one ATR, the trade is betting that an ordinary bar will not happen. m06-l1 already showed what ordinary noise does to a price that matters; the only difference here is that it reaches your stop instead of your liquidation price.»
  - S044 [35w] «The formula above already refutes it, but the point deserves to be shown head-on, because the truth is more useful than the slogan: the size came from the stop, so the leverage cannot change it.»
  - S071 [34w] «You are out of a trade whose thesis was still alive, at a price you never chose, and a position the exchange closed cannot be re-opened at the price you meant to hold from.»
  - S074 [41w] «At 20× the same balance can carry positions whose combined size no risk budget ever approved — so high leverage does not add risk to a *sized* trade, it removes the friction that used to stop you from taking an unsized one.»
  - S081 [31w] «Thinking in R frees you from the dollar amount and points you at the ratio that actually decides whether you make money: the size of your winners *relative to* your losers.»
  - S099 [47w] «Every further percent of drawdown removes capital *and* raises the bar for the recovery at the same time, so the curve turns against you faster the deeper you fall — which is the whole reason to cap risk per trade before you are ever near a deep hole.»
  - S100 [34w] «Two of the traps above are so common they deserve to be named on their own: sizing for the reward instead of the stop, and believing "a 50% loss just needs a 50% gain.»
  - S111 [41w] «You can be recklessly oversized at 2× and perfectly sized at 20× — that is the two-scenario demonstration above, and the only thing the leverage number decides on a properly sized trade is whether liquidation can reach you before your stop does.»
  - S114 [39w] «Size a crypto position as if a 2% move were the worst case and an unremarkable Tuesday will hit your stop; oversize it with leverage on top and that same Tuesday can take a large slice of the account.»
  - S116 [32w] «The 20× case left only 700 points between the stop and liquidation, about 1.2% of price, and in a fast market price can jump straight through a stop by more than that.»
  - S117 [33w] «A margin that looks safe on a calm chart is not automatically safe in a cascade, which is the practical reason to sit well under the crossing point rather than just beneath it.»
  - S120 [33w **aside-only** (18w without asides)] «In a violent move — a liquidation cascade, an exchange outage, thin weekend liquidity, a news shock at 3 a.m. — price can jump straight past your stop and you are filled well beyond it.»
  - S122 [32w] «Treat the 1% as a ceiling that holds in calm conditions, not a floor the exchange guarantees, and size with a little room for the fill to come out worse than planned.»
  - S124 [31w] «Size the position from the stop rather than the other way round: risk budget ÷ stop distance gives the units, so a wider stop forces a smaller position for the same money.»
- **10 Metaphor then gloss** (1)
  - S043 [metaphor "the risk dial" glossed: "that 20× is four times as dangerous as 5×"] «The most common beginner confusion in this whole course is that the leverage selector *is* the risk dial — that 20× is four times as dangerous as 5×.»
- **11 Synonym rotation** (2)
  - S043 [leverage setting: leverage selector (S043), leverage setting (S045), dial (S066)] 
  - S064 [gap between stop and liquidation: cushion (S064), safety margin (S065), margin (S117)] 
- **A absolutes** (6)
  - S037 [never] «The structural stop stays primary: it goes where the idea is invalidated, never at "1.5 ATR" because a multiple said so.»
  - S049 [never] «The leverage selector was never an input.»
  - S071 [never] «You are out of a trade whose thesis was still alive, at a price you never chose, and a position the exchange closed cannot be re-opened at the price you meant to hold from.»
  - S098 [must] «Going 100 → 50 is a 50% loss, but climbing 50 → 100 is a +100% gain, because the 50 you must double is now your entire account.»
  - S118 [never] «Crypto never closes, which sounds safer than a market that gaps over a weekend — it is not.»
  - S125 [must, never, summary] «Leverage is not the risk dial, since the size already came from the stop; the one criterion for choosing it is that liquidation must never become your effective stop.»

### m22-l2

**ES** — 25 hits, 52 sentences, density 48.1

- **1 Filler** (7)
  - S009 [announcer (not in cand): "Por qué esto lo decide todo:"] «Por qué esto lo decide todo: el riesgo solo se diversifica cuando la correlación está por debajo de +1.»
  - S020 [announcer sentence (not in cand): "Aquí está la aritmética que pilla a la gente."] «Aquí está la aritmética que pilla a la gente.»
  - S022 [honesta: "en la jerga honesta del trader"] «Abres tres posiciones largas en tres altcoins distintas —monedas basura, en la jerga honesta del trader— y dimensionas cada una correctamente con la regla de la lección anterior: 1% de riesgo, 100 USDT, cada una con su stop colocado un 10% por debajo de la entrada.»
  - S035 [de verdad: "hubieran sido de verdad independientes", deletable] «Si las monedas hubieran sido de verdad independientes, la probabilidad de que las tres saltaran en la misma ventana sería baja, y las pérdidas habrían llegado repartidas en el tiempo, dándote margen para reaccionar entre una y otra.»
  - S038 [justo (not in cand): "Eso es justo lo que adormece", emphatic] «Eso es justo lo que adormece a los traders y les hace tratarlas como apuestas separadas.»
  - S041 [justo (not in cand): "justo cuando la necesitas", emphatic] «La diversificación que creías haber medido con el mercado tranquilo se evapora justo cuando la necesitas.»
  - S047 [de verdad: "si es de verdad una idea nueva"] «Antes de añadir una posición, pregúntate si es de verdad una idea nueva o la misma apuesta con un traje distinto.»
- **2 Rhythmic triad** (2)
  - S026 [tres monedas / tres tickets / tres apuestas "pequeñas"; first two overlap; drop "tres tickets"] «Te sientes diversificado: tres monedas, tres tickets, tres apuestas "pequeñas" del 1% por separado.»
  - S037 [su propia narrativa / su propio listado / su propio influencer; rhythm list of examples; drop "su propio listado"] «En mercados tranquilos, las alts *parecen* independientes: cada una sube o baja por su propia narrativa, su propio listado, su propio influencer.»
- **4 Summary/uplift closer** (3)
  - S012 [restate: repeats S010 (misma apuesta mantenida dos veces) as "una sola apuesta con diez trajes"] «Diez largos en diez monedas que se mueven todas juntas son una sola apuesta con diez trajes.»
  - S036 [restate: repeats the contrast in S035 (correlacionadas llegan juntas)] «Correlacionadas, llegan juntas, dentro de una sola vela.»
  - S041 [restate: repeats S040 (correlations jump to +1 in a drawdown)] «La diversificación que creías haber medido con el mercado tranquilo se evapora justo cuando la necesitas.»
- **5 Sentence over 30 words** (8)
  - S022 [46w] «Abres tres posiciones largas en tres altcoins distintas —monedas basura, en la jerga honesta del trader— y dimensionas cada una correctamente con la regla de la lección anterior: 1% de riesgo, 100 USDT, cada una con su stop colocado un 10% por debajo de la entrada.»
  - S035 [38w] «Si las monedas hubieran sido de verdad independientes, la probabilidad de que las tres saltaran en la misma ventana sería baja, y las pérdidas habrían llegado repartidas en el tiempo, dándote margen para reaccionar entre una y otra.»
  - S044 [32w] «Así que los stops del 10% del ejemplo anterior se los saltan de largo: en un libro de alts fino no te ejecutan a −10%, te ejecutan más abajo, tras el deslizamiento.»
  - S045 [46w] «Cada posición pierde entonces *más* que su presupuesto de 100 USDT, y la "apuesta del 3%" se convierte calladamente en un 4% o peor, y todo cae en un solo movimiento, 24/7, incluido un fin de semana fino en el que apenas hay nadie para ejecutarte.»
  - S046 [37w **aside-only** (21w without asides)] «Decide un riesgo máximo para cada *grupo* correlacionado (por ejemplo, "no más del 2% en riesgo en el conjunto de mis largos en alts") y luego dimensiona las operaciones individuales para que quepan dentro de ese techo.»
  - S050 [35w] «Dimensionar cada operación por separado da por hecho que son independientes, y la correlación es lo que rompe esa suposición: dos posiciones en +1 no son dos apuestas, son la misma apuesta mantenida dos veces.»
  - S051 [36w] «Tres largos correlacionados en alts dimensionados al 1% cada uno son una sola apuesta del 3% con tres trajes, y saltan sus stops dentro de una misma vela en lugar de llegar repartidos en el tiempo.»
  - S052 [53w] «En un drawdown las correlaciones del cripto saltan hacia +1 y la mayoría de las alts tienen una beta superior a 1 frente a BTC, así que limita el grupo correlacionado y no la línea, cuenta apuestas independientes y no tickers, y pregúntate cuánto te costaría ahora mismo un mercado un 10% abajo.»
- **9 Course-coined term** (4)
  - S012 [non-seed "apuesta con N trajes" (same bet in different costumes)] «Diez largos en diez monedas que se mueven todas juntas son una sola apuesta con diez trajes.»
  - S034 [non-seed "apuesta ... con tres trajes"] «Correlacionados, son una sola apuesta de ~3% con tres trajes.»
  - S047 [non-seed "la misma apuesta con un traje distinto"] «Antes de añadir una posición, pregúntate si es de verdad una idea nueva o la misma apuesta con un traje distinto.»
  - S051 [non-seed "una sola apuesta del 3% con tres trajes"] «Tres largos correlacionados en alts dimensionados al 1% cada uno son una sola apuesta del 3% con tres trajes, y saltan sus stops dentro de una misma vela en lugar de llegar repartidos en el tiempo.»
- **11 Synonym rotation** (1)
  - S004 [individual open positions: posiciones (S004), tickets (S011), tickers (S016), líneas (S017)] 
- **A absolutes** (1)
  - S033 [nunca] «Nunca fueron tres riesgos del 1% independientes.»

**EN** — 24 hits, 52 sentences, density 46.2

- **1 Filler** (7)
  - S009 [announcer (not in cand): "Why this decides everything:"] «Why this decides everything: risk only diversifies away when correlation is below +1.»
  - S020 [announcer sentence (not in cand): "Here is the arithmetic that catches people."] «Here is the arithmetic that catches people.»
  - S022 [honest: "in the trader's honest vernacular"] «You open three long positions on three different alts — junk coins, in the trader's honest vernacular — and you size each one correctly by the last lesson's rule: 1% risk, 100 USDT, each with its stop placed 10% below entry.»
  - S035 [truly: "Had the coins truly been independent", deletable] «Had the coins truly been independent, the odds of all three stopping out in the same window would be low, and the losses would have arrived spread out over time — giving you room to react between them.»
  - S038 [exactly: emphatic] «That is exactly what lulls traders into treating them as separate bets.»
  - S041 [precisely: emphatic] «The diversification you thought you measured in calm weather evaporates precisely when you need it.»
  - S047 [genuinely: "whether it is genuinely a new idea"] «Before adding a position, ask whether it is genuinely a new idea or the same bet in a fresh costume.»
- **2 Rhythmic triad** (2)
  - S026 [three coins / three tickets / three separate "small" 1% bets; first two overlap; drop "three tickets"] «You feel diversified: three coins, three tickets, three separate "small" 1% bets.»
  - S037 [its own narrative / its own listing / its own influencer; rhythm list of examples; drop "its own listing"] «In calm markets, alts *look* independent — each one pumps or dumps on its own narrative, its own listing, its own influencer.»
- **4 Summary/uplift closer** (3)
  - S012 [restate: repeats S010 (same bet held twice) as "one bet wearing ten costumes"] «Ten longs on ten coins that all move together is one bet wearing ten costumes.»
  - S036 [restate: repeats the contrast in S035 (correlated, they arrive together)] «Correlated, they arrive together, inside a single candle.»
  - S041 [restate: repeats S040 (correlations snap to +1 in a drawdown)] «The diversification you thought you measured in calm weather evaporates precisely when you need it.»
- **5 Sentence over 30 words** (7)
  - S022 [39w] «You open three long positions on three different alts — junk coins, in the trader's honest vernacular — and you size each one correctly by the last lesson's rule: 1% risk, 100 USDT, each with its stop placed 10% below entry.»
  - S035 [37w] «Had the coins truly been independent, the odds of all three stopping out in the same window would be low, and the losses would have arrived spread out over time — giving you room to react between them.»
  - S045 [40w] «Each position then loses *more* than its 100 USDT budget, and the "3% bet" quietly becomes 4% or worse — all of it landing in one move, 24/7, including on a thin weekend when there is barely anyone to fill you.»
  - S046 [32w **aside-only** (18w without asides)] «Decide a maximum risk for each correlated *group* (for example, "no more than 2% at risk across all my alt longs combined"), then size the individual trades to fit inside that ceiling.»
  - S050 [33w] «Sizing each trade on its own assumes the trades are independent, and correlation is what breaks that assumption: two positions at +1 are not two bets, they are the same bet held twice.»
  - S051 [32w] «Three correlated alt longs sized at 1% each are one 3% bet in three costumes, and they all hit their stops inside a single candle instead of arriving spread out over time.»
  - S052 [44w] «In a drawdown crypto correlations snap toward +1 and most alts have a beta above 1 to BTC, so cap the correlated cluster rather than the line, count independent bets rather than tickers, and ask what a −10% market would cost you right now.»
- **9 Course-coined term** (4)
  - S012 [non-seed "bet wearing N costumes"] «Ten longs on ten coins that all move together is one bet wearing ten costumes.»
  - S034 [non-seed "one ~3% bet in three costumes"] «Correlated, they are one ~3% bet in three costumes.»
  - S047 [non-seed "the same bet in a fresh costume"] «Before adding a position, ask whether it is genuinely a new idea or the same bet in a fresh costume.»
  - S051 [non-seed "one 3% bet in three costumes"] «Three correlated alt longs sized at 1% each are one 3% bet in three costumes, and they all hit their stops inside a single candle instead of arriving spread out over time.»
- **11 Synonym rotation** (1)
  - S004 [individual open positions: positions (S004), tickets (S011), tickers (S016), lines (S017)] 
- **A absolutes** (1)
  - S033 [never] «Those were never three independent 1% risks.»

### m23-l1

**ES** — 58 hits, 105 sentences, density 55.2

- **1 Filler** (11)
  - S001 [completamente (not in cand): "vidas completamente distintas", intensifier] «Tres traders pueden llevar la misma cuenta en el mismo exchange y tener vidas completamente distintas.»
  - S020 [honesta: "la forma honesta de distinguir los estilos"] «Pero el periodo de tenencia es la forma honesta de distinguir los estilos, no lo ingenioso que parezca el setup ni la moneda que te toque operar.»
  - S021 [Fíjate en que: announcer] «Fíjate en que cada estilo nombra *dos* gráficos, no uno —una temporalidad lenta y otra rápida— y hacen trabajos distintos: la temporalidad superior dicta el sesgo, la inferior dicta la entrada.»
  - S032 [genuinamente (not in cand): "un win rate genuinamente más alto", intensifier] «Por eso un estilo de alta frecuencia necesita un win rate genuinamente más alto solo para no perder: antes de que un scalper conserve un solo céntimo, su edge tiene que superar toda la pila de comisiones y spreads.»
  - S044 [announcer sentence (not in cand): "Pongámosle números."] «Pongámosle números.»
  - S075 [announcer sentence (not in cand): "De ahí sale una consecuencia concreta y repetida."] «De ahí sale una consecuencia concreta y repetida.»
  - S085 [announcer sentence (not in cand): "De aquí salen dos reglas."] «De aquí salen dos reglas.»
  - S088 [announcer sentence (not in cand): "Esta es la mitad horaria de la elección de estilo."] «Esta es la mitad horaria de la elección de estilo.»
  - S093 [enormemente (not in cand): "importan enormemente", intensifier] «El scalping exige concentración intensa y continua durante toda la sesión, reflejos rápidos y una ejecución limpia; los costes y el slippage importan enormemente, y el desgaste emocional es alto.»
  - S098 [Fíjate en que: announcer] «Fíjate en que no son grados de lo mismo: la parte difícil del scalping es la *atención*, la del swing trading es la *paciencia*, y ambas rara vez conviven cómodamente en la misma persona.»
  - S105 [de verdad: "puedan sostener de verdad"] «La frecuencia es un coste, no una estrategia, y el reloj 24/7 sigue teniendo forma: pondera una señal por la sesión en que se imprimió y elige el estilo que tu horario y tu temperamento puedan sostener de verdad.»
- **2 Rhythmic triad** (4)
  - S004 [tu temporalidad / tu factura de comisiones / incluso tu sueño; third is there for rhythm; drop "incluso tu sueño"] «Conviene acertar pronto, porque casi todo lo demás —tu temporalidad, tu factura de comisiones, incluso tu sueño— se deriva de ella.»
  - S017 [comes / trabajas / duermes; "duermes" carries the overnight point; drop "comes"] «La posición sigue abierta mientras comes, trabajas y duermes.»
  - S058 [campana de cierre / fin de semana / sesión que el exchange te imponga; first and third overlap; drop "ni sesión que el exchange te imponga"] «No hay campana de cierre, ni fin de semana, ni sesión que el exchange te imponga, a diferencia de una bolsa de valores, que cierra de noche y los fines de semana y te da un punto de corte natural.»
  - S093 [concentración intensa y continua / reflejos rápidos / ejecución limpia; second and third overlap; drop "reflejos rápidos"] «El scalping exige concentración intensa y continua durante toda la sesión, reflejos rápidos y una ejecución limpia; los costes y el slippage importan enormemente, y el desgaste emocional es alto.»
- **4 Summary/uplift closer** (7)
  - S004 [motivate: "Conviene acertar pronto, porque casi todo lo demás ... se deriva de ella"] «Conviene acertar pronto, porque casi todo lo demás —tu temporalidad, tu factura de comisiones, incluso tu sueño— se deriva de ella.»
  - S020 [restate: holding period as the separator already said in S002] «Pero el periodo de tenencia es la forma honesta de distinguir los estilos, no lo ingenioso que parezca el setup ni la moneda que te toque operar.»
  - S026 [editorial: "Tener esto claro es el núcleo de elegir un estilo"] «Tener esto claro es el núcleo de elegir un estilo, porque a cada estilo lo castiga uno diferente.»
  - S056 [restate: re-explains the three net results just given] «Las comisiones castigaron las muchas idas y vueltas del scalper; el funding gravó el mantenimiento nocturno del swing trader; el day trader, que entra y sale una vez sin mantener nada, es quien más conservó de este movimiento concreto.»
  - S059 [restate: "En cripto no tienes nada de eso gratis" repeats S058] «En cripto no tienes nada de eso gratis.»
  - S079 [editorial: "No es un fenómeno nuevo: es la bolsa de liquidez de m19-l2 programada por el reloj"] «No es un fenómeno nuevo: es la bolsa de liquidez de m19-l2 programada por el reloj, donde el fin de semana construye la bolsa y la reapertura es la hora previsible a la que aparece algo lo bastante grande para tomarla.»
  - S084 [editorial: "La información era la hora."] «La información era la hora.»
- **5 Sentence over 30 words** (26)
  - S006 [32w **aside-only** (21w without asides)] «Tres cosas se mueven juntas a lo largo de él: el periodo de tenencia (cuánto tiempo permanece abierta una posición), el número de operaciones (cuántas haces) y la temporalidad (qué gráfico lees).»
  - S011 [34w] «*En la práctica:* un scalper trabaja BTC en el gráfico de 1 minuto durante una hora movida, recortando unas décimas de punto porcentual cada vez y cerrando cada operación en menos de noventa segundos.»
  - S014 [38w] «*En la práctica:* un day trader toma una ruptura matinal a las 09:00, la gestiona un par de horas y vuelve a estar plano bastante antes de la noche: el "día" es una única sesión, no varios días.»
  - S021 [31w **aside-only** (25w without asides)] «Fíjate en que cada estilo nombra *dos* gráficos, no uno —una temporalidad lenta y otra rápida— y hacen trabajos distintos: la temporalidad superior dicta el sesgo, la inferior dicta la entrada.»
  - S023 [44w] «Y como la temporalidad decide en qué periodos merece la pena leer tus indicadores, el estilo elige de paso también esos parámetros: las convenciones de medias móviles que acompañan a cada temporalidad —9/21 intradía, 20/50 en swing, 50/200 en el diario— están en m10-l1.»
  - S027 [39w **aside-only** (13w without asides)] «Cada vez que abres o cierras cruzas el spread (la diferencia entre la mejor compra y la mejor venta, que cedes cuando tomas liquidez) y pagas una comisión (la parte que se lleva el exchange por emparejar tu orden).»
  - S032 [39w] «Por eso un estilo de alta frecuencia necesita un win rate genuinamente más alto solo para no perder: antes de que un scalper conserve un solo céntimo, su edge tiene que superar toda la pila de comisiones y spreads.»
  - S045 [31w **aside-only** (21w without asides)] «Toma una posición de 10.000 USDT que captura un movimiento bruto del 3 % —300 USDT de beneficio en bruto antes de cualquier coste— y entrégale el mismo movimiento a cada estilo.»
  - S056 [39w] «Las comisiones castigaron las muchas idas y vueltas del scalper; el funding gravó el mantenimiento nocturno del swing trader; el day trader, que entra y sale una vez sin mantener nada, es quien más conservó de este movimiento concreto.»
  - S058 [40w] «No hay campana de cierre, ni fin de semana, ni sesión que el exchange te imponga, a diferencia de una bolsa de valores, que cierra de noche y los fines de semana y te da un punto de corte natural.»
  - S060 [38w] «Para un day trader, esto significa que no hay un "día" natural: tienes que *inventarte* tu propia sesión y, sobre todo, parar cuando termina en vez de derivar en un maratón de 14 horas frente a la pantalla.»
  - S067 [39w] «El exchange nunca cierra, pero la mayoría de las personas y los grandes participantes que aportan su liquidez tienen horario de oficina, así que la semana sigue teniendo una forma, y esa forma entra en tu elección de estilo.»
  - S071 [41w] «La sesión asiática, aproximadamente de 00:00 a 08:00 UTC, opera sobre un libro más fino, y los fines de semana son aún más finos: el flujo institucional se retira desde el viernes por la tarde hasta el lunes por la mañana.»
  - S073 [32w] «La misma compra de 50 BTC que un libro profundo de Londres/Nueva York absorbe sin pestañear empuja el precio mucho más lejos en un libro poco profundo de domingo por la mañana.»
  - S074 [40w] «Así que el *mismo* acontecimiento en el gráfico pesa distinto según la hora: un nivel roto contra volumen real es información sobre oferta y demanda; un nivel roto porque no había nadie es en buena medida un accidente del reloj.»
  - S076 [51w] «Los fines de semana tienden a derivar en rangos de poco volumen —sin flujo institucional que empuje una tendencia, el precio se enrosca— y los traders colocan sus órdenes en los bordes de ese rango, así que los stops se acumulan justo más allá de su máximo y de su mínimo.»
  - S078 [40w] «La reapertura del lunes es el momento en que el volumen real regresa a un libro cuyos extremos obvios están repletos de órdenes en reposo, y muy a menudo recorre uno o los dos antes de hacer cualquier otra cosa.»
  - S079 [41w] «No es un fenómeno nuevo: es la bolsa de liquidez de m19-l2 programada por el reloj, donde el fin de semana construye la bolsa y la reapertura es la hora previsible a la que aparece algo lo bastante grande para tomarla.»
  - S082 [33w **aside-only** (22w without asides)] «El lunes por la mañana llega volumen real, el precio hace una mecha hasta 59.100 —por debajo del mínimo del rango, barriendo los stops aparcados ahí— y cierra de vuelta dentro del rango.»
  - S087 [53w] «Generalízalo a todas las señales que uses: una ruptura, un pico de volumen o la recuperación de un nivel en la sesión asiática o en fin de semana pesan menos que el mismo acontecimiento durante el solapamiento Londres/Nueva York, y a menudo merecen la confirmación de una sesión activa antes de que actúes.»
  - S089 [37w] «Un scalper necesita horas en las que el libro sea profundo y los movimientos reales; cazar ticks en un libro muerto a las 03:00 es pagar el peaje completo de comisiones por la peor liquidez del día.»
  - S094 [66w] «Es también el estilo en el que toda la disciplina de este curso tiene menos holgura: lo que en m27-l1 es escribir el plan por adelantado, aquí es el plan previo a la sesión —reglas, tamaños y el bracket adjunto de m24-l1 decididos antes de sentarte, de modo que cada entrada ejecuta un plan que ya está en papel en vez de redactarlo a toda velocidad—.»
  - S098 [34w] «Fíjate en que no son grados de lo mismo: la parte difícil del scalping es la *atención*, la del swing trading es la *paciencia*, y ambas rara vez conviven cómodamente en la misma persona.»
  - S103 [40w] «Lo que separa a un scalper, un day trader y un swing trader es cuánto mantienen y con qué frecuencia operan, y esa única elección decide la temporalidad, el coste y los errores a los que cada uno se expone.»
  - S104 [54w] «Los dos costes responden a relojes distintos: las comisiones se cobran por ejecución y escalan con el número de operaciones, mientras que el funding se cobra por reloj y escala con el tiempo mantenido, así que el mismo movimiento de 300 USDT deja 180, 292 y 274 según solo el estilo que lo tomó.»
  - S105 [39w] «La frecuencia es un coste, no una estrategia, y el reloj 24/7 sigue teniendo forma: pondera una señal por la sesión en que se imprimió y elige el estilo que tu horario y tu temperamento puedan sostener de verdad.»
- **9 Course-coined term** (5)
  - S028 [non-seed "peaje" (fees as a toll)] «Ambas se cobran por ejecución —una al entrar, otra al salir—, así que una sola ida y vuelta paga el peaje dos veces.»
  - S029 [non-seed "peaje"] «En una operación el peaje es pequeño; multiplicado por el número de operaciones, es el coste mayor y más predecible que tienes.»
  - S031 [non-seed "peaje"] «Un scalper que hace 100 idas y vueltas al día paga el peaje 200 veces al día, se haya movido el mercado o no.»
  - S079 [bolsa de liquidez [seed]] «No es un fenómeno nuevo: es la bolsa de liquidez de m19-l2 programada por el reloj, donde el fin de semana construye la bolsa y la reapertura es la hora previsible a la que aparece algo lo bastante grande para tomarla.»
  - S089 [non-seed "peaje" ("el peaje completo de comisiones")] «Un scalper necesita horas en las que el libro sea profundo y los movimientos reales; cazar ticks en un libro muerto a las 03:00 es pagar el peaje completo de comisiones por la peor liquidez del día.»
- **10 Metaphor then gloss** (3)
  - S036 [metaphor "otra correa ... el funding es esa correa" glossed in S037-S038 (who pays whom, pushes the perp back toward spot)] «Un perpetuo nunca vence, así que necesita otra correa, y el funding es esa correa.»
  - S065 [metaphor "libertad y trampa a la vez" glossed after colon: "siempre puedes operar, lo que significa que siempre puedes sobreoperar"] «El reloj 24/7 es libertad y trampa a la vez: siempre puedes operar, lo que significa que siempre puedes sobreoperar.»
  - S079 [metaphor "la bolsa de liquidez ... programada por el reloj" glossed: "donde el fin de semana construye la bolsa y la reapertura es la hora previsible..."] «No es un fenómeno nuevo: es la bolsa de liquidez de m19-l2 programada por el reloj, donde el fin de semana construye la bolsa y la reapertura es la hora previsible a la que aparece algo lo bastante grande para tomarla.»
- **11 Synonym rotation** (2)
  - S004 [per-trade trading costs: factura de comisiones (S004), comisión (S027), peaje (S028), pila de comisiones y spreads (S032)] 
  - S071 [thin order book: libro más fino (S071), libro poco profundo (S073), libro tranquilo (S086), libro muerto (S089)] 
- **A absolutes** (6)
  - S036 [nunca] «Un perpetuo nunca vence, así que necesita otra correa, y el funding es esa correa.»
  - S040 [nunca] «Un scalper casi nunca está en posición cuando salta el reloj del funding, así que el funding apenas le afecta.»
  - S047 [debe] «El funding corre al 0,03 % por intervalo, así que en cada intervalo una posición mantenida debe `10.000 × 0,0003 = 3 USDT`.»
  - S065 [siempre, siempre] «El reloj 24/7 es libertad y trampa a la vez: siempre puedes operar, lo que significa que siempre puedes sobreoperar.»
  - S066 [siempre, siempre] «"Siempre abierto" no es lo mismo que "siempre igual".»
  - S067 [nunca] «El exchange nunca cierra, pero la mayoría de las personas y los grandes participantes que aportan su liquidez tienen horario de oficina, así que la semana sigue teniendo una forma, y esa forma entra en tu elección de estilo.»

**EN** — 52 hits, 105 sentences, density 49.5

- **1 Filler** (12)
  - S001 [completely (not in cand): "completely different lives", intensifier] «Three traders can run the same account on the same exchange and lead completely different lives.»
  - S020 [honest: "the honest way to tell the styles apart"] «But the holding period is the honest way to tell the styles apart — not how clever the setup looks, and not which coin you happen to be trading.»
  - S021 [Note that: announcer] «Note that each style names *two* charts, not one — a slower frame and a faster frame — and they do different jobs: the higher timeframe dictates the bias, the lower one dictates the entry.»
  - S032 [genuinely: "a genuinely higher win rate", intensifier] «That is why a high-frequency style needs a genuinely higher win rate just to break even: before a scalper keeps a single cent, their edge has to beat the entire stack of fees and spreads.»
  - S044 [announcer sentence (not in cand): "Put numbers on it."] «Put numbers on it.»
  - S060 [crucially: emphasis tag] «For a day trader, this means there is no natural "day" — you have to *invent* your own session and, crucially, stop when it ends instead of drifting into a 14-hour screen marathon.»
  - S075 [announcer sentence (not in cand): "That has one concrete, repeating consequence."] «That has one concrete, repeating consequence.»
  - S085 [announcer sentence (not in cand): "Two rules come out of this."] «Two rules come out of this.»
  - S088 [announcer sentence (not in cand): "This is the scheduling half of the style choice."] «This is the scheduling half of the style choice.»
  - S093 [enormously (not in cand): "matter enormously", intensifier] «Scalping demands continuous, intense focus for the whole session, fast reflexes and clean execution; costs and slippage matter enormously, and the emotional churn is high.»
  - S098 [Notice (not in cand): announcer] «Notice these are not degrees of the same thing: scalping's hard part is *attention*, swing trading's hard part is *patience*, and the two rarely live comfortably in the same person.»
  - S105 [actually: "can actually run"] «Frequency is a cost, not a strategy, and the 24/7 clock still has a shape: weight a signal by the session it printed in, and pick the style your schedule and temperament can actually run.»
- **2 Rhythmic triad** (4)
  - S004 [your timeframe / your fee bill / even your sleep; third is there for rhythm; drop "even your sleep"] «It is worth getting right early, because almost everything else — your timeframe, your fee bill, even your sleep — falls out of it.»
  - S017 [eat / work / sleep; "sleep" carries the overnight point; drop "eat"] «The position stays open while you eat, work and sleep.»
  - S058 [no closing bell / no weekend / no session the exchange imposes; first and third overlap; drop "no session the exchange imposes on you"] «There is no closing bell, no weekend, no session the exchange imposes on you — unlike a stock market, which shuts overnight and on weekends and hands you a natural stopping point.»
  - S093 [continuous, intense focus / fast reflexes / clean execution; second and third overlap; drop "fast reflexes"] «Scalping demands continuous, intense focus for the whole session, fast reflexes and clean execution; costs and slippage matter enormously, and the emotional churn is high.»
- **4 Summary/uplift closer** (7)
  - S004 [motivate: "It is worth getting right early, because almost everything else ... falls out of it"] «It is worth getting right early, because almost everything else — your timeframe, your fee bill, even your sleep — falls out of it.»
  - S020 [restate: holding period as the separator already said in S002] «But the holding period is the honest way to tell the styles apart — not how clever the setup looks, and not which coin you happen to be trading.»
  - S026 [editorial: "Getting this straight is the heart of choosing a style"] «Getting this straight is the heart of choosing a style, because each style is punished by a different one.»
  - S056 [restate: re-explains the three net results just given] «Fees punished the scalper's many round-trips; funding taxed the swing trader's overnight hold; the day trader, in and out once with nothing held over, kept the most of this particular move.»
  - S059 [restate: "In crypto you get none of that for free" repeats S058] «In crypto you get none of that for free.»
  - S079 [editorial: "This is not a new phenomenon: it is m19-l2's liquidity pocket, scheduled by the clock"] «This is not a new phenomenon: it is m19-l2's liquidity pocket, scheduled by the clock — the weekend builds the pocket, and the reopen is the predictable hour at which something large enough to take it shows up.»
  - S084 [editorial: "The hour was the information."] «The hour was the information.»
- **5 Sentence over 30 words** (19)
  - S014 [35w] «*In practice:* a day trader takes a morning breakout at 09:00, manages it for a couple of hours, and is flat again well before the evening — the "day" is a single session, not several days.»
  - S021 [33w **aside-only** (26w without asides)] «Note that each style names *two* charts, not one — a slower frame and a faster frame — and they do different jobs: the higher timeframe dictates the bias, the lower one dictates the entry.»
  - S023 [40w] «And because the timeframe decides which periods your indicators are worth reading on, the style quietly picks those parameters too: the moving-average conventions that go with each frame — 9/21 intraday, 20/50 for swing, 50/200 on the daily — are in m10-l1.»
  - S027 [39w **aside-only** (14w without asides)] «Every time you open or close you cross the spread (the gap between the best bid and the best ask, which you give up when you take liquidity) and pay a fee (the exchange's cut for matching your order).»
  - S032 [35w] «That is why a high-frequency style needs a genuinely higher win rate just to break even: before a scalper keeps a single cent, their edge has to beat the entire stack of fees and spreads.»
  - S056 [31w] «Fees punished the scalper's many round-trips; funding taxed the swing trader's overnight hold; the day trader, in and out once with nothing held over, kept the most of this particular move.»
  - S058 [31w] «There is no closing bell, no weekend, no session the exchange imposes on you — unlike a stock market, which shuts overnight and on weekends and hands you a natural stopping point.»
  - S060 [32w] «For a day trader, this means there is no natural "day" — you have to *invent* your own session and, crucially, stop when it ends instead of drifting into a 14-hour screen marathon.»
  - S067 [34w] «The exchange never closes, but most of the people and desks that provide its liquidity keep office hours — so the week still has a shape, and that shape belongs in your choice of style.»
  - S074 [38w] «So the *identical* chart event carries different weight at different hours: a level broken against real size is evidence about supply and demand, while a level broken because nobody was home is largely an accident of the clock.»
  - S076 [38w **aside-only** (28w without asides)] «Weekends tend to drift into low-volume ranges — no institutional flow to drive a trend, so price coils — and traders put their orders around the edges of that range, so stops accumulate just beyond its high and its low.»
  - S078 [34w] «The Monday reopen is the moment real size returns to a book whose obvious extremes are stuffed with resting orders, and it very often runs one or both of them before doing anything else.»
  - S079 [37w] «This is not a new phenomenon: it is m19-l2's liquidity pocket, scheduled by the clock — the weekend builds the pocket, and the reopen is the predictable hour at which something large enough to take it shows up.»
  - S087 [48w] «Generalise it to every signal you use — a breakout, a volume spike, a level reclaim in the Asian session or over a weekend earns less weight than the same event during the London/New York overlap, and often deserves confirmation from an active session before you act on it.»
  - S089 [34w] «A scalper needs hours where the book is deep and the moves are real; hunting ticks in a dead 03:00 book means paying the full fee toll for the worst liquidity of the day.»
  - S094 [53w] «It is also the style where every discipline in this course has the least room: the scalper's version of m27-l1's written-in-advance plan is a pre-session one — rules, sizes and m24-l1's attached bracket settled before you sit down, so that each entry executes a plan already on paper instead of drafting one at speed.»
  - S103 [37w] «What separates a scalper, a day trader and a swing trader is how long they hold and how often they trade, and that one choice decides the timeframe, the cost and the mistakes each is exposed to.»
  - S104 [50w] «The two costs answer to different clocks: fees are charged per fill and scale with the number of trades, while funding is charged on a clock and scales with time held — so the same 300 USDT move nets 180, 292 and 274 depending only on the style that took it.»
  - S105 [35w] «Frequency is a cost, not a strategy, and the 24/7 clock still has a shape: weight a signal by the session it printed in, and pick the style your schedule and temperament can actually run.»
- **9 Course-coined term** (5)
  - S028 [non-seed "toll" (fees as a toll)] «Both are charged per fill — once going in, once coming out — so a single round-trip pays the toll twice.»
  - S029 [non-seed "toll"] «On one trade the toll is small; multiplied by the number of trades, it is the biggest and most predictable cost you have.»
  - S031 [non-seed "toll"] «A scalper doing 100 round-trips a day pays the toll 200 times a day, whether the market went anywhere or not.»
  - S079 [seed liquidity pool variant "liquidity pocket" (stop-cluster sense, weekend range extremes)] «This is not a new phenomenon: it is m19-l2's liquidity pocket, scheduled by the clock — the weekend builds the pocket, and the reopen is the predictable hour at which something large enough to take it shows up.»
  - S089 [non-seed "toll" ("the full fee toll")] «A scalper needs hours where the book is deep and the moves are real; hunting ticks in a dead 03:00 book means paying the full fee toll for the worst liquidity of the day.»
- **10 Metaphor then gloss** (3)
  - S036 [metaphor "another leash — funding is that leash" glossed in S037-S038 (who pays whom, nudges the perp back toward spot)] «A perpetual never expires, so it needs another leash — funding is that leash.»
  - S065 [metaphor "freedom and trap in one" glossed after colon: "you can always trade, which means you can always over-trade"] «The 24/7 clock is freedom and trap in one: you can always trade, which means you can always over-trade.»
  - S079 [metaphor "liquidity pocket, scheduled by the clock" glossed: "the weekend builds the pocket, and the reopen is the predictable hour..."] «This is not a new phenomenon: it is m19-l2's liquidity pocket, scheduled by the clock — the weekend builds the pocket, and the reopen is the predictable hour at which something large enough to take it shows up.»
- **11 Synonym rotation** (2)
  - S004 [per-trade trading costs: fee bill (S004), fee (S027), toll (S028), stack of fees and spreads (S032)] 
  - S071 [thin order book: thinner book (S071), thin Sunday-morning book (S073), quiet book (S086), dead book (S089)] 
- **A absolutes** (5)
  - S036 [never] «A perpetual never expires, so it needs another leash — funding is that leash.»
  - S040 [never] «A scalper is almost never in a position when the funding clock ticks, so funding barely touches them.»
  - S065 [always, always] «The 24/7 clock is freedom and trap in one: you can always trade, which means you can always over-trade.»
  - S066 [always, always] «"Always open" is not the same as "always the same".»
  - S067 [never] «The exchange never closes, but most of the people and desks that provide its liquidity keep office hours — so the week still has a shape, and that shape belongs in your choice of style.»

### m23-l2

**ES** — 55 hits, 91 sentences, density 60.4

- **1 Filler** (17)
  - S003 [not in cand: «Arranca por la frase de la que cuelga toda la lección» announcer] «Arranca por la frase de la que cuelga toda la lección:»
  - S007 [honestidad: «contestan con honestidad» applied to an answer] «Todas las temporalidades contestan con honestidad; lo que pasa es que contestan a preguntas distintas, y una pregunta que no querías hacer te la contestan igual.»
  - S017 [not in cand: «Y ya está.» tag sentence] «Y ya está.»
  - S019 [exactamente: intensifier on a cross-reference] «Es exactamente lo que dice m29 de una sola vela, un piso más arriba.»
  - S033 [honesta: «la razón honesta» applied to a reason] «Esa es la razón honesta para mirar una temporalidad superior.»
  - S035 [not in cand: «El reparto de tareas es viejo y es sencillo:» announcer] «El reparto de tareas es viejo y es sencillo:»
  - S041 [not in cand: «Y aquí viene la parte que conviene decir con cuidado» announcer] «Y aquí viene la parte que conviene decir con cuidado, porque suele enseñarse como misticismo.»
  - S050 [not in cand: «Y dicho así te llevas el límite de regalo» announcer] «Y dicho así te llevas el límite de regalo: una temporalidad superior manda en su trabajo.»
  - S052 [not in cand: «Aquí está la trampa» announcer] «Aquí está la trampa, y cuesta más dinero que cualquier indicador.»
  - S060 [exactamente: intensifier] «Solo en ese panel es un rally: varios cientos de puntos, mínimos crecientes de principio a fin, exactamente lo que un gráfico rápido convierte en tendencia recién nacida.»
  - S064 [not in cand: «La forma general del error:» announcer] «La forma general del error:»
  - S066 [Fíjate en que: announcer] «Fíjate en que la temporalidad menor no mentía.»
  - S067 [de verdad: emphatic «existió de verdad»] «El rally existió de verdad; podrías haber ganado dinero con él si hubieras salido una hora después.»
  - S069 [not in cand: «Toda la lección se reduce a» announcer] «Toda la lección se reduce a un orden de operaciones:»
  - S081 [de verdad: emphatic «suavice de verdad»] «Una pareja útil está separada más o menos por un factor de cuatro a seis: lo bastante como para que la superior suavice de verdad a la inferior, y lo bastante cerca como para que las dos hablen del mismo suceso.»
  - S085 [exactamente: intensifier on a cross-reference] «Va al otro lado de la estructura que invalidaría *esta entrada* —el mínimo relevante que acaba de hacer la temporalidad menor— y la posición se dimensiona desde esa distancia, exactamente como lo hace m22.»
  - S090 [honesta: «la razón honesta» applied to a reason] «Los niveles no se mueven al cambiar el desplegable; solo cambia el ruido que los rodea, y esa es la razón honesta para mirar más arriba.»
- **2 Rhythmic triad** (5)
  - S032 [mismo nivel / misma acción del precio / relación señal/ruido distinta; drop «la misma acción del precio»] «El mismo nivel, la misma acción del precio, una relación señal/ruido radicalmente distinta.»
  - S047 [mucha menos gente / órdenes más pequeñas / la mayoría ya está en otra cosa; drop the third] «Un nivel de 15m de hace dos horas lo ha visto quien estuviera mirando un gráfico de 15m en las últimas dos horas: mucha menos gente, con órdenes mucho más pequeñas, y la mayoría ya está en otra cosa.»
  - S048 [más órdenes en reposo / de más gente / con más convicción; drop «con más convicción»] «Así que un nivel del diario pesa más que uno de 15m por la misma razón por la que una salida concurrida pesa más que una vacía: hay más órdenes en reposo, de más gente y con más convicción.»
  - S063 [el pullback se acaba / la tendencia bajista sigue / la ventana cierra en 8.360; first two are the same event, drop «el pullback se acaba»] «Y la figura enseña la resolución que la versión de ejercicio te esconde: el pullback se acaba, la tendencia bajista sigue y la ventana cierra cerca de 8.360, por debajo de donde arrancó todo el rebote.»
  - S074 [dirección / estructura / niveles que importan; drop «estructura» (overlaps dirección)] «Dirección, estructura y los niveles que importan.»
- **4 Summary/uplift closer** (6)
  - S018 [restate: «Es agregación, no información nueva» sums up the bullets] «Es agregación, no información nueva.»
  - S025 [restate: repeats S024 lossy compression] «Si subes de temporalidad pierdes detalle; no ganas sabiduría.»
  - S028 [restate: repeats S027 (same number on every chart)] «No se desplaza porque cambies el desplegable.»
  - S032 [restate: sums up S030–S031] «El mismo nivel, la misma acción del precio, una relación señal/ruido radicalmente distinta.»
  - S040 [restate: recasts the context/execution definitions of S038–S039] «La temporalidad superior te dice *si* hay que buscar un largo siquiera; la inferior te dice *dónde* empieza ese largo.»
  - S071 [restate: «Nunca al revés.» repeats S070] «Nunca al revés.**»
- **5 Sentence over 30 words** (16)
  - S002 [35w] «Esta lección va de qué son el uno para el otro, porque esa relación no es cuestión de gustos y confundir el orden es una de las costumbres más caras que puede coger un principiante.»
  - S030 [36w] «En 15m, la aproximación a 25.900 son cuarenta velas de vaivén, tres de las cuales lo pinchan y vuelven, y cada una de ellas parece, en el momento en que se imprime, que está pasando algo.»
  - S047 [39w] «Un nivel de 15m de hace dos horas lo ha visto quien estuviera mirando un gráfico de 15m en las últimas dos horas: mucha menos gente, con órdenes mucho más pequeñas, y la mayoría ya está en otra cosa.»
  - S048 [39w] «Así que un nivel del diario pesa más que uno de 15m por la misma razón por la que una salida concurrida pesa más que una vacía: hay más órdenes en reposo, de más gente y con más convicción.»
  - S051 [31w] «Pregúntale al diario dónde poner el stop y te dará algo a un 6% de distancia, que tampoco es sabiduría: es un gráfico al que le preguntan algo que no responde.»
  - S056 [48w] «Lo que no has mirado es el de 4h, donde esas mismas velas son una sola vela de pullback dentro de una tendencia bajista: un rebote dentro de una estructura que sigue haciendo máximos decrecientes y en la que los vendedores que la mandan están esperando para vender.»
  - S058 [36w] «La ventana abre cerca de 10.400 y el gráfico de 4h se cae hasta unos 8.760: un tramo de un 16% largo, hecho de máximos y mínimos decrecientes, que es lo que es una tendencia bajista.»
  - S062 [32w] «El precio sigue miles de puntos por debajo de donde empezó el tramo; la caída ha recuperado alrededor de un 40% de sí misma y no ha hecho ni un máximo creciente.»
  - S063 [36w] «Y la figura enseña la resolución que la versión de ejercicio te esconde: el pullback se acaba, la tendencia bajista sigue y la ventana cierra cerca de 8.360, por debajo de donde arrancó todo el rebote.»
  - S068 [42w] «Lo que salió mal es que la operación se *dimensionó y se mantuvo* como si fuera una tendencia cuando era una interrupción dentro de la tendencia de otro, y lo que termina una interrupción es la tendencia volviendo, deprisa, contra tu posición.»
  - S081 [41w] «Una pareja útil está separada más o menos por un factor de cuatro a seis: lo bastante como para que la superior suavice de verdad a la inferior, y lo bastante cerca como para que las dos hablen del mismo suceso.»
  - S083 [38w] «Cada una que añades es otro gráfico que puede llevarte la contraria, y quien mira cinco no está mejor informado: tiene garantizado encontrar una que diga lo que le apetece oír, que es volver al aviso de arriba.»
  - S085 [34w **aside-only** (24w without asides)] «Va al otro lado de la estructura que invalidaría *esta entrada* —el mínimo relevante que acaba de hacer la temporalidad menor— y la posición se dimensiona desde esa distancia, exactamente como lo hace m22.»
  - S087 [48w] «Es una operación de 15 minutos cargando con un riesgo de 4 horas y, como el tamaño sale de la distancia al stop, es además una posición varias veces más pequeña de la que creías estar tomando, o una pérdida varias veces mayor que la que habías planeado.»
  - S089 [40w] «Un gráfico no tiene opinión, tiene la opinión de su temporalidad: una vela de 4h son dieciséis velas de 15m agregadas, así que una temporalidad mayor es compresión con pérdidas y no información nueva —tira a la basura el camino—.»
  - S091 [56w] «La temporalidad superior pone el contexto y la inferior la ejecución, nunca al revés, porque el error caro es operar en la menor una tendencia que en la mayor es un pullback; y abrir gráfico tras gráfico hasta que alguno te dé la razón sobre la posición que ya tienes es ir de compras, no analizar.»
- **9 Course-coined term** (4)
  - S027 [repisa [seed]] «Una repisa en 25.900 (m03-l2, m08-l1) está en 25.900 en el diario, en el de 1h y en el de 1 minuto.»
  - S054 [escalera [seed]] «El gráfico de 15m enseña un avance de manual: mínimos crecientes, máximos crecientes, una secuencia que cualquiera llamaría tendencia alcista (la escalera de m08-l1, dibujada en un gráfico rápido).»
  - S078 [«ir de compras (con pasos intermedios)»: calque of «timeframe shopping», used as a term] «Mirar la temporalidad superior *después* de haber encontrado un setup que te gusta es ir de compras con pasos intermedios.»
  - S091 [«es ir de compras, no analizar»: same coined term] «La temporalidad superior pone el contexto y la inferior la ejecución, nunca al revés, porque el error caro es operar en la menor una tendencia que en la mayor es un pullback; y abrir gráfico tras gráfico hasta que alguno te dé la razón sobre la posición que ya tienes es ir de compras, no analizar.»
- **10 Metaphor then gloss** (4)
  - S005 [«Un gráfico no tiene opinión» glossed in S007 as answering different questions] «Tiene la opinión de su temporalidad.**»
  - S019 [«un piso más arriba» glossed in S020–S021] «Es exactamente lo que dice m29 de una sola vela, un piso más arriba.»
  - S024 [«compresión con pérdidas» glossed in S025 («pierdes detalle»)] «Cambiar de temporalidad es, por tanto, una compresión con pérdidas cuya intensidad eliges tú.»
  - S048 [«una salida concurrida pesa más que una vacía: hay más órdenes en reposo…» simile glossed after the colon] «Así que un nivel del diario pesa más que uno de 15m por la misma razón por la que una salida concurrida pesa más que una vacía: hay más órdenes en reposo, de más gente y con más convicción.»
- **11 Synonym rotation** (3)
  - S001 [lower timeframe: temporalidad rápida (S001), temporalidad inferior/la inferior (S037), temporalidad menor (S053), gráfico rápido (S054)] 
  - S021 [higher timeframe: temporalidad mayor (S021), temporalidad superior (S033), temporalidades altas (S042), gráfico grande (S043)] 
  - S053 [the counter-trend bounce: pullback (S053), rebote (S056), rally (S060), interrupción (S068)] 
- **A absolutes** (4)
  - S031 [nunca] «En 4h ese mismo tramo son dos o tres velas con una mecha metida en el nivel y un cuerpo que nunca cerró al otro lado.»
  - S042 [siempre] ««Las temporalidades altas siempre mandan» no es una ley del mercado.»
  - S071 [nunca] «Nunca al revés.**»
  - S091 [nunca, summary] «La temporalidad superior pone el contexto y la inferior la ejecución, nunca al revés, porque el error caro es operar en la menor una tendencia que en la mayor es un pullback; y abrir gráfico tras gráfico hasta que alguno te dé la razón sobre la posición que ya tienes es ir de compras, no analizar.»

**EN** — 56 hits, 92 sentences, density 60.9

- **1 Filler** (20)
  - S003 [not in cand: «Start from the sentence the whole lesson hangs on» announcer] «Start from the sentence the whole lesson hangs on:»
  - S007 [honestly: «answers honestly» applied to an answer] «Every frame answers honestly; they are simply answering different questions, and a question you did not mean to ask gets answered anyway.»
  - S007 [simply: intensifier] «Every frame answers honestly; they are simply answering different questions, and a question you did not mean to ask gets answered anyway.»
  - S017 [not in cand: «That is the entire operation.» tag sentence] «That is the entire operation.»
  - S019 [exactly: intensifier on a cross-reference] «This is exactly the point m29 makes about a single candle, one level up.»
  - S033 [honest: «the honest reason» applied to a reason] «That is the honest reason to look at a higher frame at all.»
  - S033 [not in cand: «at all» intensifier («to look at a higher frame at all»)] «That is the honest reason to look at a higher frame at all.»
  - S036 [not in cand: «The working division of labour is old and it is simple:» announcer] «The working division of labour is old and it is simple:»
  - S042 [not in cand: «And here is the part worth saying carefully» announcer] «And here is the part worth saying carefully, because it usually gets taught as mysticism.»
  - S051 [not in cand: «State it that way and you also get the limit for free» announcer] «State it that way and you also get the limit for free: a higher frame rules for its job.»
  - S053 [not in cand: «Here is the trap» announcer] «Here is the trap, and it costs more money than any indicator ever will.»
  - S061 [exactly: intensifier] «On that panel alone it is a rally: several hundred points, higher lows the whole way, exactly the thing a fast chart makes look like a fresh trend.»
  - S065 [not in cand: «The general form of the mistake:» announcer] «The general form of the mistake:»
  - S067 [Notice that: announcer] «Notice that the lower frame was not lying.»
  - S068 [genuinely: emphatic («There genuinely was a rally»)] «There genuinely was a rally; you could genuinely have made money in it if you had been out again in an hour.»
  - S068 [genuinely: emphatic («could genuinely have made money»)] «There genuinely was a rally; you could genuinely have made money in it if you had been out again in an hour.»
  - S070 [not in cand: «The whole lesson reduces to» announcer] «The whole lesson reduces to an order of operations:»
  - S082 [genuinely: emphatic] «A useful pair sits roughly four to six times apart — enough that the higher frame genuinely smooths the lower one, close enough that the two are talking about the same event.»
  - S086 [exactly: intensifier on a cross-reference] «It goes beyond the structure that would invalidate *this entry* — the swing low the lower frame just made — and the position is then sized from that distance, exactly as m22 does it.»
  - S091 [honest: «the honest reason» applied to a reason] «Levels do not move when you change the dropdown; only the noise around them does, which is the honest reason to look higher.»
- **2 Rhythmic triad** (5)
  - S032 [same level / same price action / different signal-to-noise; drop «same price action»] «Same level, same price action, radically different signal-to-noise.»
  - S048 [far smaller crowd / far smaller orders / most have moved on; drop the third] «A 15-minute level from two hours ago has been seen by whoever was watching a 15-minute chart in the last two hours — a far smaller crowd, with far smaller orders, most of whom have already moved on.»
  - S049 [more resting orders / from more people / held with more conviction; drop «held with more conviction»] «So a daily level outweighs a 15m level for the same reason a crowded exit outweighs an empty one: more resting orders, from more people, held with more conviction.»
  - S064 [the pullback ends / the downtrend resumes / the window closes near 8,360; first two are the same event, drop «the pullback ends»] «And the figure shows the resolution the exercise version withholds: the pullback ends, the downtrend resumes, and the window closes near 8,360 — below where the whole bounce started.»
  - S075 [direction / structure / the levels that matter; drop «structure»] «Direction, structure, the levels that matter.»
- **4 Summary/uplift closer** (6)
  - S018 [restate: «Aggregation, not new information.» sums up the bullets] «Aggregation, not new information.»
  - S025 [restate: repeats S024 lossy compression] «Go coarser and you lose detail; you do not gain wisdom.»
  - S028 [restate: repeats S027] «It does not shift when you change the dropdown.»
  - S032 [restate: sums up S030–S031] «Same level, same price action, radically different signal-to-noise.»
  - S041 [restate: recasts the context/execution definitions of S039–S040] «The higher frame tells you *whether* to look for a long at all; the lower frame tells you *where* the long begins.»
  - S072 [restate: «Never the reverse.» repeats S071] «Never the reverse.**»
- **5 Sentence over 30 words** (13)
  - S002 [36w] «This lesson is about what those two charts are to each other — because the relationship is not a matter of taste, and getting it backwards is one of the most expensive habits a beginner can build.»
  - S030 [34w] «On the 15m chart, the approach to 25,900 is forty candles of wobble, three of which poke through and come back — and each of those looks, at the moment it prints, like something happening.»
  - S048 [37w] «A 15-minute level from two hours ago has been seen by whoever was watching a 15-minute chart in the last two hours — a far smaller crowd, with far smaller orders, most of whom have already moved on.»
  - S052 [34w] «Ask the daily chart where to put your stop and it will hand you something 6% away, which is not wisdom either — it is a chart being asked a question it does not answer.»
  - S057 [45w] «What you did not look at is the 4-hour chart, where those same candles are one pullback candle inside a downtrend — a bounce inside a structure that is still making lower highs, and which the sellers who own that structure are waiting to sell into.»
  - S059 [32w] «The window opens near 10,400 and the 4-hour chart falls away to about 8,760 — a leg of some 16%, made of lower highs and lower lows, which is what a downtrend is.»
  - S069 [42w] «What went wrong is that the trade was *sized and held* as though it were a trend, when it was an interruption inside somebody else's trend — and the thing that ends an interruption is the trend resuming, at speed, into your position.»
  - S082 [31w] «A useful pair sits roughly four to six times apart — enough that the higher frame genuinely smooths the lower one, close enough that the two are talking about the same event.»
  - S084 [40w] «Every frame you add is another chart that can disagree, and the reader who watches five of them is not better informed — they are guaranteed to find one that says whatever they want, which returns you to the warning above.»
  - S086 [32w **aside-only** (24w without asides)] «It goes beyond the structure that would invalidate *this entry* — the swing low the lower frame just made — and the position is then sized from that distance, exactly as m22 does it.»
  - S088 [44w] «It is a 15-minute trade carrying a 4-hour risk, and since size comes from stop distance, it is also a position several times smaller than the one you thought you were taking, or a loss several times bigger than the one you planned for.»
  - S090 [34w] «A chart has no opinion, it has its frame's opinion: one 4-hour candle is sixteen 15-minute candles aggregated, so a higher frame is lossy compression rather than new information — it throws away the path.»
  - S092 [51w] «The higher frame sets the context and the lower one the execution, never the reverse, because the expensive error is trading a lower-frame trend that is a pullback on the frame above it — and opening chart after chart until one agrees with the position you already hold is shopping, not analysis.»
- **8 Repeated paragraph opener** (1)
  - S017 ["That is" ×3 (S017, S033, S073)] 
- **9 Course-coined term** (4)
  - S027 [shelf [seed]] «A shelf at 25,900 (m03-l2, m08-l1) is at 25,900 on the daily, on the 1-hour and on the 1-minute.»
  - S055 [staircase/ladder [seed]] «The 15-minute chart shows a textbook advance: higher lows, higher highs, a clean sequence anyone would call an uptrend (m08-l1's ladder, drawn on a fast chart).»
  - S079 [«timeframe shopping (with extra steps)»: used as a term] «Looking at the higher frame *after* you have found a setup you like is timeframe shopping with extra steps.»
  - S092 [«is shopping, not analysis»: same term] «The higher frame sets the context and the lower one the execution, never the reverse, because the expensive error is trading a lower-frame trend that is a pullback on the frame above it — and opening chart after chart until one agrees with the position you already hold is shopping, not analysis.»
- **10 Metaphor then gloss** (4)
  - S005 [«A chart has no opinion» glossed in S007 as answering different questions] «It has its frame's opinion.**»
  - S019 [«one level up» glossed in S020–S021] «This is exactly the point m29 makes about a single candle, one level up.»
  - S024 [«lossy compression» glossed in S025 («you lose detail»)] «So changing frame is a lossy compression you choose the strength of.»
  - S049 [«a crowded exit outweighs an empty one: more resting orders…» simile glossed after the colon] «So a daily level outweighs a 15m level for the same reason a crowded exit outweighs an empty one: more resting orders, from more people, held with more conviction.»
- **11 Synonym rotation** (3)
  - S001 [higher timeframe: slower frame (S001), higher frame (S021), higher timeframes (S043), big chart (S044)] 
  - S001 [lower timeframe: faster one (S001), lower frame (S037), fast chart (S055)] 
  - S054 [the counter-trend bounce: pullback (S054), bounce (S057), rally (S061), interruption (S069)] 
- **A absolutes** (4)
  - S031 [never] «On the 4h chart the same stretch is two or three candles with a wick into the level and a body that never closed beyond it.»
  - S043 [always] «"Higher timeframes always win" is not a law of markets.»
  - S072 [never] «Never the reverse.**»
  - S092 [never, summary] «The higher frame sets the context and the lower one the execution, never the reverse, because the expensive error is trading a lower-frame trend that is a pullback on the frame above it — and opening chart after chart until one agrees with the position you already hold is shopping, not analysis.»

### m24-l1

**ES** — 41 hits, 77 sentences, density 53.2

- **1 Filler** (12)
  - S002 [not in cand: «justo cuando más importa» intensifier] «La misma idea, introducida con el tipo de orden equivocado, puede ejecutarse a un precio que nunca aceptaste, o no ejecutarse en absoluto justo cuando más importa.»
  - S004 [not in cand: «no es más que» minimiser] «Un libro de órdenes no es más que la lista viva de las órdenes puestas por los demás: bids (órdenes de compra) apiladas por debajo del precio actual y asks (órdenes de venta) apiladas por encima.»
  - S016 [sencillamente: intensifier] «Una orden de límite fija tu precio, pero el mercado puede sencillamente no volver a él, y te quedas sin ejecutar mientras el movimiento ocurre sin ti.»
  - S026 [not in cand: «Aquí está la trampa» announcer] «Aquí está la trampa, y *por qué* salta.»
  - S032 [not in cand: «justo en el momento» intensifier] «Un stop-limit protege tu precio y, justo en el momento en que más necesitas salir, puede no protegerte en absoluto.»
  - S032 [not in cand: «en absoluto» intensifier] «Un stop-limit protege tu precio y, justo en el momento en que más necesitas salir, puede no protegerte en absoluto.»
  - S034 [justamente: intensifier] «Y está deliberadamente exagerada en una cosa —separa el trigger del límite lo suficiente para que se distingan a simple vista—; en la práctica los pondrías a un tick el uno del otro, que es justamente lo que hace que la trampa pase desapercibida.»
  - S054 [nada más: tag; «descarte el exceso» already says it] «Marcar esa salida como reduce-only hace que el exchange la limite al tamaño de tu posición y descarte el exceso, de modo que el peor caso es una salida limpia y completa, y nada más.»
  - S068 [precisamente: intensifier] «Los perpetuos no cierran nunca: un libro poco profundo de un domingo por la noche puede abrir un hueco de varios puntos porcentuales en segundos y sin nadie alrededor, que es *precisamente* la condición que se salta un stop-limit y deja una orden de protección abandonada.»
  - S071 [de verdad: emphatic «puede de verdad hacer caminar»] «En una altcoin poco profunda, el ejemplo de slippage de arriba no es una curiosidad: una orden de mercado de tamaño normal puede de verdad hacer caminar el precio varios puntos porcentuales, y un stop-limit saltado puede de verdad dejarte tirado, porque para empezar nunca hubo mucho volumen puesto contra el que ejecutar.»
  - S071 [de verdad: emphatic «puede de verdad dejarte tirado»] «En una altcoin poco profunda, el ejemplo de slippage de arriba no es una curiosidad: una orden de mercado de tamaño normal puede de verdad hacer caminar el precio varios puntos porcentuales, y un stop-limit saltado puede de verdad dejarte tirado, porque para empezar nunca hubo mucho volumen puesto contra el que ejecutar.»
  - S072 [simplemente: intensifier] «En spot solo puedes vender lo que tienes, así que una venta sobredimensionada simplemente lo vende todo y para.»
- **4 Summary/uplift closer** (7)
  - S003 [editorial: «La ejecución no es un detalle…» comments on what the paragraph said] «La ejecución no es un detalle; es donde tu plan se encuentra con el libro de órdenes.»
  - S006 [ahead: points to the order types below once the content has ended] «Cuál de las dos cosas hace es toda la distinción entre los tipos de orden de más abajo.»
  - S021 [restate: «La misma idea, dos resultados…» sums up S019–S020] «La misma idea, dos resultados elegidos por completo por el tipo de orden: más barato-o-nada frente a ya-a-mercado.»
  - S023 [motivate: «la diferencia es donde se hacen daño los principiantes»] «Tiene dos formas, y la diferencia es donde se hacen daño los principiantes.»
  - S032 [restate: repeats the failure just walked through] «Un stop-limit protege tu precio y, justo en el momento en que más necesitas salir, puede no protegerte en absoluto.»
  - S042 [restate: S041 already said the trade is fully defined] «Colocarlos juntos define la operación antes de que llegue la emoción: el SL dice cuánto perderás si te equivocas, el TP dice dónde te llevarás la ganancia.»
  - S077 [editorial: summary ends on «te conviertes en él» flourish] «Etiqueta como reduce-only cada salida en un perpetuo para que un cierre mal dimensionado no te dé la vuelta a corto, y recuerda que el slippage es lo que cuesta una orden de mercado en un libro poco profundo: allí no consigues el precio de mercado, te conviertes en él.»
- **5 Sentence over 30 words** (21)
  - S004 [36w **aside-only** (30w without asides)] «Un libro de órdenes no es más que la lista viva de las órdenes puestas por los demás: bids (órdenes de compra) apiladas por debajo del precio actual y asks (órdenes de venta) apiladas por encima.»
  - S019 [32w] «Una orden de mercado se ejecuta al instante en 60.000, y un poco peor si 1 BTC es más de lo que hay en esa mejor oferta, porque sube hasta la siguiente.»
  - S020 [40w] «Una orden de límite de compra en 59.850, en cambio, espera: si el precio baja un poco se ejecuta y te ahorras 150; si el precio se dispara sin bajar, nunca se ejecuta y ves el movimiento desde la barrera.»
  - S030 [36w] «Pero una venta con límite solo se ejecuta a 99,9 o más, y el precio ahora está en 97 y cayendo: nadie te va a comprar a 99,9 cuando el mercado le permite comprar a 97.»
  - S034 [44w **aside-only** (30w without asides)] «Y está deliberadamente exagerada en una cosa —separa el trigger del límite lo suficiente para que se distingan a simple vista—; en la práctica los pondrías a un tick el uno del otro, que es justamente lo que hace que la trampa pase desapercibida.»
  - S041 [34w **aside-only** (29w without asides)] «En el momento en que ambas están puestas la operación queda del todo definida —arriesgas 1.200 para ganar 3.000— y se cerrará sola por un extremo o por el otro, estés mirando o durmiendo.»
  - S044 [54w] «Casi cualquier exchange de perpetuos te deja adjuntar el TP y el SL a la propia orden de entrada: va una sola instrucción al mercado, la entrada se ejecuta y sus dos salidas ya están puestas detrás —dimensionadas a la posición y enlazadas de modo que la que se ejecute cancele a la otra—.»
  - S046 [49w] «Es la única forma de que el plan entre al mercado *contigo*: teclear tres órdenes a mano mientras se imprime una vela de 1 minuto no es ejecución, es la psicología de m26 ocurriendo en tiempo real, y la orden que se olvida bajo presión es siempre el stop.»
  - S047 [31w] «Es una salida *voluntaria* que tú controlas, que no debe confundirse con la liquidación, que es el exchange cerrando a la fuerza una posición apalancada cuando se te agota el margen.»
  - S053 [64w] «Si el precio ya se ha movido y parte de la orden se comporta de forma inesperada, o la orden se duplica, una venta simple por más de lo que tienes puede cerrar tu largo y abrir un corto: querías salir y en su lugar te has dado la vuelta al lado opuesto, ahora posicionado en contra del mismo movimiento que acabas de asegurar.»
  - S054 [35w] «Marcar esa salida como reduce-only hace que el exchange la limite al tamaño de tu posición y descarte el exceso, de modo que el peor caso es una salida limpia y completa, y nada más.»
  - S056 [31w] «Las órdenes de mercado lo provocan: tu orden se come las órdenes puestas en el libro y, si no hay suficientes arriba, se ejecuta cada vez más abajo, a peores precios.»
  - S059 [40w] «Un libro fino, habitual en altcoins pequeñas o a las 3 de la madrugada, tiene poco volumen puesto, así que hasta una orden de mercado modesta hace caminar el precio varios ticks y consigues un promedio de ejecución visiblemente peor.»
  - S064 [33w] «Esos 0,65 de diferencia son el slippage; y en un libro profundo, donde 100,0 podría contener 500 contratos, la misma orden se habría ejecutado por completo a 100,0, sin nada a peor precio.»
  - S065 [50w] «La defensa práctica: en mercados poco profundos, prefiere órdenes de límite para fijar tu precio, reduce el tamaño para no verte obligado a comerte el libro entero, y nunca asumas que una orden de mercado se ejecuta cerca del último precio impreso cuando el libro que hay detrás está vacío.»
  - S068 [46w] «Los perpetuos no cierran nunca: un libro poco profundo de un domingo por la noche puede abrir un hueco de varios puntos porcentuales en segundos y sin nadie alrededor, que es *precisamente* la condición que se salta un stop-limit y deja una orden de protección abandonada.»
  - S071 [53w] «En una altcoin poco profunda, el ejemplo de slippage de arriba no es una curiosidad: una orden de mercado de tamaño normal puede de verdad hacer caminar el precio varios puntos porcentuales, y un stop-limit saltado puede de verdad dejarte tirado, porque para empezar nunca hubo mucho volumen puesto contra el que ejecutar.»
  - S074 [35w] «Por eso existe reduce-only y por eso debe ir en cada salida que pongas en un perpetuo: restaura la garantía, propia del spot, de que cerrar una posición nunca puede abrir por accidente la contraria.»
  - S075 [35w] «Toda orden o toma una orden en reposo o se convierte en una, y eso lo decide todo: una orden de mercado compra inmediatez y renuncia al control del precio, una limitada hace lo contrario.»
  - S076 [45w] «La trampa es el stop-limit de protección: en una caída rápida el precio se salta tu límite, la orden se queda sin ejecutar por encima del mercado y sigues dentro de la posición sin salida automática, así que los stops de protección van a stop-market.»
  - S077 [50w] «Etiqueta como reduce-only cada salida en un perpetuo para que un cierre mal dimensionado no te dé la vuelta a corto, y recuerda que el slippage es lo que cuesta una orden de mercado en un libro poco profundo: allí no consigues el precio de mercado, te conviertes en él.»
- **11 Synonym rotation** (1)
  - S059 [thin order book: libro fino (S059), libro poco profundo (S060), libro que hay detrás está vacío (S065)] 
- **A absolutes** (10)
  - S002 [nunca] «La misma idea, introducida con el tipo de orden equivocado, puede ejecutarse a un precio que nunca aceptaste, o no ejecutarse en absoluto justo cuando más importa.»
  - S020 [nunca] «Una orden de límite de compra en 59.850, en cambio, espera: si el precio baja un poco se ejecuta y te ahorras 150; si el precio se dispara sin bajar, nunca se ejecuta y ves el movimiento desde la barrera.»
  - S046 [siempre] «Es la única forma de que el plan entre al mercado *contigo*: teclear tres órdenes a mano mientras se imprime una vela de 1 minuto no es ejecución, es la psicología de m26 ocurriendo en tiempo real, y la orden que se olvida bajo presión es siempre el stop.»
  - S047 [debe] «Es una salida *voluntaria* que tú controlas, que no debe confundirse con la liquidación, que es el exchange cerrando a la fuerza una posición apalancada cuando se te agota el margen.»
  - S049 [debería] «Un stop-loss bien colocado debería dispararse mucho antes de que la liquidación entre siquiera en juego: eso es buena parte de su trabajo.»
  - S051 [nunca] «Una orden reduce-only es una que el exchange garantiza que *solo podrá reducir* tu posición actual, nunca abrir ni agrandar una.»
  - S065 [nunca] «La defensa práctica: en mercados poco profundos, prefiere órdenes de límite para fijar tu precio, reduce el tamaño para no verte obligado a comerte el libro entero, y nunca asumas que una orden de mercado se ejecuta cerca del último precio impreso cuando el libro que hay detrás está vacío.»
  - S068 [nunca] «Los perpetuos no cierran nunca: un libro poco profundo de un domingo por la noche puede abrir un hueco de varios puntos porcentuales en segundos y sin nadie alrededor, que es *precisamente* la condición que se salta un stop-limit y deja una orden de protección abandonada.»
  - S071 [nunca] «En una altcoin poco profunda, el ejemplo de slippage de arriba no es una curiosidad: una orden de mercado de tamaño normal puede de verdad hacer caminar el precio varios puntos porcentuales, y un stop-limit saltado puede de verdad dejarte tirado, porque para empezar nunca hubo mucho volumen puesto contra el que ejecutar.»
  - S074 [debe, nunca] «Por eso existe reduce-only y por eso debe ir en cada salida que pongas en un perpetuo: restaura la garantía, propia del spot, de que cerrar una posición nunca puede abrir por accidente la contraria.»

**EN** — 32 hits, 77 sentences, density 41.6

- **1 Filler** (11)
  - S004 [not in cand: «is just the live list» minimiser] «An order book is just the live list of everyone else's resting orders: bids (offers to buy) stacked below the current price, asks (offers to sell) stacked above it.»
  - S016 [simply: intensifier] «A limit order names your price, but the market may simply never come back to it, and you sit unfilled while the move happens without you.»
  - S026 [not in cand: «Here is the trap» announcer] «Here is the trap, and *why* it springs.»
  - S032 [exactly: intensifier on «the moment»] «A stop-limit protects your price and, in exactly the moment you most need out, can fail to protect you at all.»
  - S032 [not in cand: «at all» intensifier] «A stop-limit protects your price and, in exactly the moment you most need out, can fail to protect you at all.»
  - S034 [exactly: intensifier] «It is also deliberately exaggerated in one respect: it separates the trigger from the limit far enough to tell them apart by eye, where in practice you would set them a tick from each other, which is exactly what lets the trap go unnoticed.»
  - S054 [nothing more: tag; «discard the excess» already says it] «Marking that exit reduce-only makes the exchange cap it at your position size and discard the excess, so the worst case is a clean, complete exit and nothing more.»
  - S068 [precisely: intensifier] «Perpetuals never close: a thin Sunday-night book can gap several percent in seconds with nobody around, which is *precisely* the condition that skips a stop-limit and leaves a protective order stranded.»
  - S071 [really: emphatic «really can walk the price»] «On a thin alt the slippage example above is not a curiosity — a normal-sized market order really can walk the price several percent, and a skipped stop-limit really can leave you stranded, because there was never much resting size to fill against in the first place.»
  - S071 [really: emphatic «really can leave you stranded»] «On a thin alt the slippage example above is not a curiosity — a normal-sized market order really can walk the price several percent, and a skipped stop-limit really can leave you stranded, because there was never much resting size to fill against in the first place.»
  - S072 [simply: intensifier] «On spot you can only sell what you hold, so an oversized sell simply sells everything and stops.»
- **4 Summary/uplift closer** (7)
  - S003 [editorial: «Execution is not a detail…» comments on what the paragraph said] «Execution is not a detail; it is where your plan meets the order book.»
  - S006 [ahead: points to the order types below once the content has ended] «Which of the two it does is the whole distinction between the order types below.»
  - S021 [restate: «Same idea, two outcomes…» sums up S019–S020] «Same idea, two outcomes chosen entirely by the order type — cheaper-or-nothing versus now-at-market.»
  - S023 [motivate: «the difference is where beginners get hurt»] «It comes in two forms, and the difference is where beginners get hurt.»
  - S032 [restate: repeats the failure just walked through] «A stop-limit protects your price and, in exactly the moment you most need out, can fail to protect you at all.»
  - S042 [restate: S041 already said the trade is fully defined] «Placing them together defines the trade before emotion arrives: the SL says how much you will lose if wrong, the TP says where you will take the win.»
  - S077 [editorial: summary ends on «you become it» flourish] «Tag every exit reduce-only on a perp so a mis-sized close cannot flip you short, and remember slippage is what a market order costs in a thin book — you do not get the market price there, you become it.»
- **5 Sentence over 30 words** (14)
  - S020 [35w] «A limit buy at 59,850 instead waits: if price dips a touch it fills and you save 150; if price runs up without dipping, it never fills and you watch the move from the sidelines.»
  - S030 [32w] «But a sell limit only fills at 99.9 or higher, and price is now 97 and falling: nobody will buy from you at 99.9 when the market lets them buy at 97.»
  - S034 [44w] «It is also deliberately exaggerated in one respect: it separates the trigger from the limit far enough to tell them apart by eye, where in practice you would set them a tick from each other, which is exactly what lets the trap go unnoticed.»
  - S041 [33w **aside-only** (27w without asides)] «The moment both are placed the trade is fully defined — you risk 1,200 to make 3,000 — and it will close itself at one end or the other whether you are watching or asleep.»
  - S044 [49w] «Almost every perpetuals venue lets you attach the TP and the SL to the entry order itself: one instruction goes to the market, the entry fills, and its two exits are already resting behind it — sized to the position, and wired so that whichever one fills cancels the other.»
  - S046 [45w] «It is the only way the plan enters the market *with* you: typing three orders by hand while a 1-minute candle prints is not execution, it is m26's psychology happening in real time, and the order that gets forgotten under pressure is always the stop.»
  - S053 [55w] «If price has already moved and part of the order behaves unexpectedly, or the order is duplicated, a plain sell for more than you hold can close your long and open a short — you meant to exit and instead you have flipped to the opposite side, now positioned against the very move you just banked.»
  - S059 [34w] «A thin book, common in small altcoins or at 3 a.m., has little resting size, so even a modest market order walks the price several ticks and you get a visibly worse average fill.»
  - S065 [45w] «The practical defence: on thin markets, prefer limit orders so you name your price, size down so you are not forced to eat the whole book, and never assume a market order fills near the last printed price when the book behind it is empty.»
  - S068 [31w] «Perpetuals never close: a thin Sunday-night book can gap several percent in seconds with nobody around, which is *precisely* the condition that skips a stop-limit and leaves a protective order stranded.»
  - S071 [46w] «On a thin alt the slippage example above is not a curiosity — a normal-sized market order really can walk the price several percent, and a skipped stop-limit really can leave you stranded, because there was never much resting size to fill against in the first place.»
  - S074 [33w] «That is why reduce-only exists and why it belongs on every exit you place on a perp: it restores the spot-like guarantee that closing a position can never accidentally open the opposite one.»
  - S076 [38w] «The trap is the protective stop-limit — in a fast drop price gaps past your limit, the order rests above the market unfilled, and you are still in a position with no automatic exit, so protective stops are stop-market.»
  - S077 [39w] «Tag every exit reduce-only on a perp so a mis-sized close cannot flip you short, and remember slippage is what a market order costs in a thin book — you do not get the market price there, you become it.»
- **A absolutes** (9)
  - S002 [never] «The same idea, entered with the wrong order type, can fill at a price you never agreed to, or fail to fill at all when it matters most.»
  - S016 [never] «A limit order names your price, but the market may simply never come back to it, and you sit unfilled while the move happens without you.»
  - S020 [never] «A limit buy at 59,850 instead waits: if price dips a touch it fills and you save 150; if price runs up without dipping, it never fills and you watch the move from the sidelines.»
  - S046 [always] «It is the only way the plan enters the market *with* you: typing three orders by hand while a 1-minute candle prints is not execution, it is m26's psychology happening in real time, and the order that gets forgotten under pressure is always the stop.»
  - S051 [never] «A reduce-only order is one the exchange promises will *only ever reduce* your current position, never open or enlarge one.»
  - S065 [never] «The practical defence: on thin markets, prefer limit orders so you name your price, size down so you are not forced to eat the whole book, and never assume a market order fills near the last printed price when the book behind it is empty.»
  - S068 [never] «Perpetuals never close: a thin Sunday-night book can gap several percent in seconds with nobody around, which is *precisely* the condition that skips a stop-limit and leaves a protective order stranded.»
  - S071 [never] «On a thin alt the slippage example above is not a curiosity — a normal-sized market order really can walk the price several percent, and a skipped stop-limit really can leave you stranded, because there was never much resting size to fill against in the first place.»
  - S074 [never] «That is why reduce-only exists and why it belongs on every exit you place on a perp: it restores the spot-like guarantee that closing a position can never accidentally open the opposite one.»

### m25-l1

**ES** — 27 hits, 81 sentences, density 33.3

- **1 Filler** (7)
  - S006 [not in cand: «Esta lección es un único argumento encadenado:» announcer] «Esta lección es un único argumento encadenado: dos números en bruto, la única cifra que los combina, las rachas de pérdidas que esa cifra garantiza y por qué nada de esto se puede juzgar con un puñado de operaciones.»
  - S040 [not in cand: «Esto cierra el círculo con los dos ejemplos de arriba» announcer] «Esto cierra el círculo con los dos ejemplos de arriba.»
  - S061 [not in cand: «Cada uno tiene una frase que el trader se dice…» announcer] «Cada uno tiene una frase que el trader se dice a sí mismo primero.»
  - S062 [not in cand: «La trampa más seductora.» editorial tag] «La trampa más seductora.»
  - S069 [honesta: «la postura honesta» applied to a stance/reading] «La postura honesta que hay debajo de los tres: casi nunca tendrás datos suficientes para estar seguro, y tus sensaciones durante un drawdown son la prueba menos fiable que posees.»
  - S072 [precisamente: intensifier] «Eso es precisamente lo que lo hace peligroso para la esperanza.»
  - S077 [not in cand: «justo el que» intensifier] «Primero, las comisiones y el funding: cada operación de más paga la comisión de ida y vuelta, y un edge ajustado por operación es justo el que un flujo de operaciones de baja calidad y alta frecuencia se come vivo — el win rate de equilibrio sube en silencio con cada posición que abres.»
- **2 Rhythmic triad** (1)
  - S071 [sin campana de cierre / sin fin de semana / siempre otra vela; all restate 24/7, drop «sin fin de semana»] «El cripto funciona 24/7: sin campana de cierre, sin fin de semana, siempre otra vela.»
- **4 Summary/uplift closer** (6)
  - S006 [ahead: lesson roadmap closes the intro paragraph] «Esta lección es un único argumento encadenado: dos números en bruto, la única cifra que los combina, las rachas de pérdidas que esa cifra garantiza y por qué nada de esto se puede juzgar con un puñado de operaciones.»
  - S026 [restate: takeaway of the two worked examples] «La esperanza es lo que separa a los dos; el win rate por sí solo los habría ordenado al revés.»
  - S043 [editorial: «La misma lección, ahora como umbral…»] «La misma lección, ahora como umbral en lugar de como cálculo completo.»
  - S061 [ahead: announces the three sentences that follow] «Cada uno tiene una frase que el trader se dice a sí mismo primero.»
  - S064 [editorial: «Win rate sin payoff es medio número.»] «Win rate sin payoff es medio número.»
  - S075 [restate: repeats S073–S074 (diluting the edge)] «No estás sumando a tu edge: estás diluyendo tu media con operaciones que nunca lo tuvieron.»
- **5 Sentence over 30 words** (12)
  - S006 [39w] «Esta lección es un único argumento encadenado: dos números en bruto, la única cifra que los combina, las rachas de pérdidas que esa cifra garantiza y por qué nada de esto se puede juzgar con un puñado de operaciones.»
  - S015 [41w] «Un win rate bajo con un payoff grande gana dinero: acierta solo el 35% de las veces, pero deja correr las operaciones ganadoras hasta varias veces el tamaño de las perdedoras, y las ganancias pagan de sobra las frecuentes pérdidas pequeñas.»
  - S049 [36w] «A lo largo de unos cientos de operaciones se espera que una racha de cinco pérdidas ocurra más de una vez, y una racha de ocho, en algún punto de una carrera larga, es casi segura.»
  - S051 [41w] «Y cuanto más operas, más profunda es la peor racha que deberías esperar encontrar: una muestra mayor no suaviza las rachas, sino que *garantiza* que tarde o temprano topes con una lo bastante larga como para poner a prueba tus nervios.»
  - S056 [39w] «con un win rate del 40%, una tanda de diez operaciones puede salir con 7 ganadas o con 2 ganadas por puro azar, y esas dos tandas cuentan historias opuestas sobre un sistema que no ha cambiado en nada.»
  - S059 [37w] «Quien te enseña una captura de ocho operaciones en verde te está enseñando varianza, no un edge probado; y tu propia buena semana no demuestra nada hasta que se repite a lo largo de una muestra real.»
  - S070 [32w **aside-only** (28w without asides)] «Decide las reglas —esperanza, payoff, racha tolerable— *antes* de que llegue la emoción, y luego deja que lo que te haga cambiar de opinión sea una muestra real, no una mala tarde.»
  - S074 [35w] «Pero un mercado que nunca cierra te tienta a seguir haciendo clic, y cada operación marginal tomada por aburrimiento o por FOMO es una operación de esperanza más baja o negativa mezclada en la muestra.»
  - S077 [53w] «Primero, las comisiones y el funding: cada operación de más paga la comisión de ida y vuelta, y un edge ajustado por operación es justo el que un flujo de operaciones de baja calidad y alta frecuencia se come vivo — el win rate de equilibrio sube en silencio con cada posición que abres.»
  - S078 [71w] «Segundo, el tiempo comprimido: como puedes tomar las operaciones de una semana en una sola noche en vela, una racha de pérdidas normal que un trader de swing diario encontraría a lo largo de meses puede golpearte en unas horas, lo que se siente mucho más como un "sistema roto" de lo que es, y alimenta directamente la trampa de abandonar en mitad de una racha de la que hablábamos arriba.»
  - S079 [31w] «El win rate cuenta tus ganadoras e ignora su tamaño; el payoff mide su tamaño e ignora con qué frecuencia llegan: solo la esperanza, `win% × ganancia media − loss% × pérdida media`, dice si un sistema gana dinero.»
  - S081 [57w] «Las rachas de pérdidas son aritmética y no averías —con un win rate del 40%, cinco seguidas son alrededor de una de cada trece— y un puñado de operaciones es varianza, así que decide las reglas antes de que llegue la emoción y deja que te haga cambiar de opinión una muestra real, nunca una mala tarde.»
- **11 Synonym rotation** (1)
  - S027 [break-even: equilibrio / solo para no perder (S027), quedar en tablas (S033), no hundirte (S039)] 
- **A absolutes** (8)
  - S027 [debes] «Iguala la esperanza a cero exactamente y obtienes el win rate de equilibrio (break-even): la frecuencia que debes superar, para un payoff dado, solo para no perder.»
  - S050 [debe] «las operaciones son (a efectos prácticos) independientes, así que una mala racha no tiene memoria ni se autocorrige — el mercado no te "debe" una ganancia tras cuatro pérdidas.»
  - S051 [deberías] «Y cuanto más operas, más profunda es la peor racha que deberías esperar encontrar: una muestra mayor no suaviza las rachas, sino que *garantiza* que tarde o temprano topes con una lo bastante larga como para poner a prueba tus nervios.»
  - S069 [nunca] «La postura honesta que hay debajo de los tres: casi nunca tendrás datos suficientes para estar seguro, y tus sensaciones durante un drawdown son la prueba menos fiable que posees.»
  - S071 [siempre] «El cripto funciona 24/7: sin campana de cierre, sin fin de semana, siempre otra vela.»
  - S074 [nunca] «Pero un mercado que nunca cierra te tienta a seguir haciendo clic, y cada operación marginal tomada por aburrimiento o por FOMO es una operación de esperanza más baja o negativa mezclada en la muestra.»
  - S075 [nunca] «No estás sumando a tu edge: estás diluyendo tu media con operaciones que nunca lo tuvieron.»
  - S081 [nunca, summary] «Las rachas de pérdidas son aritmética y no averías —con un win rate del 40%, cinco seguidas son alrededor de una de cada trece— y un puñado de operaciones es varianza, así que decide las reglas antes de que llegue la emoción y deja que te haga cambiar de opinión una muestra real, nunca una mala tarde.»

**EN** — 24 hits, 84 sentences, density 28.6

- **1 Filler** (7)
  - S006 [not in cand: «This lesson is one connected argument:» announcer] «This lesson is one connected argument: two raw numbers, the single figure that combines them, the losing streaks that figure guarantees, and why none of it can be judged from a handful of trades.»
  - S040 [not in cand: «This closes the loop on the two examples above» announcer] «This closes the loop on the two examples above.»
  - S061 [not in cand: «Each of them has a sentence the trader says…» announcer] «Each of them has a sentence the trader says to themselves first.»
  - S063 [not in cand: «The most seductive trap.» editorial tag] «The most seductive trap.»
  - S072 [honest: «the honest stance» applied to a stance/reading] «The honest stance underneath all three: you will almost never have enough data to be certain, and your feelings during a drawdown are the least reliable evidence you own.»
  - S075 [precisely: intensifier] «That is precisely what makes it dangerous for expectancy.»
  - S080 [exactly: intensifier] «First, fees and funding: every extra trade pays the round-trip fee, and a thin per-trade edge is exactly the kind that a stream of low-quality, high-frequency trades eats alive — the break-even win rate quietly rises with every position you open.»
- **2 Rhythmic triad** (1)
  - S074 [no closing bell / no weekend / always another candle; all restate 24/7, drop «no weekend»] «Crypto runs 24/7 — no closing bell, no weekend, always another candle.»
- **4 Summary/uplift closer** (6)
  - S006 [ahead: lesson roadmap closes the intro paragraph] «This lesson is one connected argument: two raw numbers, the single figure that combines them, the losing streaks that figure guarantees, and why none of it can be judged from a handful of trades.»
  - S026 [restate: takeaway of the two worked examples] «Expectancy is what separates the two; win rate on its own would have ranked them backwards.»
  - S043 [editorial: «Same lesson, now as a threshold…»] «Same lesson, now as a threshold instead of a full calculation.»
  - S061 [ahead: announces the three sentences that follow] «Each of them has a sentence the trader says to themselves first.»
  - S065 [editorial: «Win rate without payoff is half a number.»] «Win rate without payoff is half a number.»
  - S078 [restate: repeats S076–S077 (diluting the edge)] «You are not adding to your edge — you are diluting your average with trades that never had one.»
- **5 Sentence over 30 words** (9)
  - S006 [34w] «This lesson is one connected argument: two raw numbers, the single figure that combines them, the losing streaks that figure guarantees, and why none of it can be judged from a handful of trades.»
  - S015 [40w] «A low win rate with a big payoff makes money: win just 35% of the time, but let the winners run to several times the size of the losers, and the wins more than pay for the frequent small losses.»
  - S051 [38w] «And the more trades you take, the deeper the worst streak you should expect to meet: a larger sample does not smooth the streaks away, it *guarantees* you eventually hit a run long enough to test your nerve.»
  - S056 [38w] «with a 40% win rate, a run of ten trades can easily come out 7 wins or 2 wins purely by chance — and those two runs tell opposite stories about a system that has not changed at all.»
  - S059 [31w] «Someone showing you a screenshot of eight green trades is showing you variance, not a proven edge — and your own good week proves nothing until it repeats across a real sample.»
  - S077 [31w] «But a market that never closes tempts you to keep clicking, and every marginal trade taken out of boredom or FOMO is a lower- or negative-expectancy trade mixed into the sample.»
  - S080 [40w] «First, fees and funding: every extra trade pays the round-trip fee, and a thin per-trade edge is exactly the kind that a stream of low-quality, high-frequency trades eats alive — the break-even win rate quietly rises with every position you open.»
  - S081 [55w] «Second, compressed time: because you can take a week's worth of trades in a single all-night session, a normal losing streak that a daily-swing trader would meet over months can hit you in a few hours — which feels far more like a "broken system" than it is, and feeds straight into the abandon-during-a-streak trap above.»
  - S084 [48w] «Losing streaks are arithmetic, not malfunctions — at a 40% win rate, five losses in a row is about one in thirteen — and a handful of trades is variance, so decide the rules before the emotion arrives and let a real sample, never a bad afternoon, change your mind.»
- **11 Synonym rotation** (1)
  - S027 [break-even: break-even / just to avoid losing (S027), break even (S033), just to tread water (S039)] 
- **A absolutes** (7)
  - S027 [must] «Set expectancy to exactly zero and you learn the break-even win rate — the frequency you must clear, for a given payoff, just to avoid losing.»
  - S039 [must] «Winners half the size of losers: you must win two out of three *just to tread water*.»
  - S072 [never] «The honest stance underneath all three: you will almost never have enough data to be certain, and your feelings during a drawdown are the least reliable evidence you own.»
  - S074 [always] «Crypto runs 24/7 — no closing bell, no weekend, always another candle.»
  - S077 [never] «But a market that never closes tempts you to keep clicking, and every marginal trade taken out of boredom or FOMO is a lower- or negative-expectancy trade mixed into the sample.»
  - S078 [never] «You are not adding to your edge — you are diluting your average with trades that never had one.»
  - S084 [never, summary] «Losing streaks are arithmetic, not malfunctions — at a 40% win rate, five losses in a row is about one in thirteen — and a handful of trades is variance, so decide the rules before the emotion arrives and let a real sample, never a bad afternoon, change your mind.»

### m26-l1

**ES** — 57 hits, 95 sentences, density 60.0

- **1 Filler** (16)
  - S004 [not in cand: «calladamente» tic (4 uses in lesson)] «En todos ellos, un plan tranquilo y sensato que hiciste por adelantado queda calladamente anulado por una versión de ti del momento que funciona con miedo, codicia u orgullo herido, y esa versión siempre tiene una razón preparada.»
  - S005 [not in cand: «justo cuando» intensifier] «Esto no se arregla intentando estar más tranquilo o más disciplinado en el momento, porque el momento es justo cuando tu criterio falla.»
  - S007 [not in cand: «El resto de la lección son cuatro patrones.» announcer] «El resto de la lección son cuatro patrones.»
  - S014 [not in cand: «calladamente» tic] «Además, has anclado calladamente en "recuperar lo perdido" —tu saldo de partida— como el estado natural del mundo, de modo que estar por debajo no se registra como un hecho neutro, sino como una amenaza continua que debes acabar.»
  - S030 [not in cand: «calladamente» tic] «Para esquivar ese pequeño golpe al ego, la mente reescribe calladamente el plan.»
  - S031 [de verdad: emphatic «parece de verdad la jugada inteligente»] «Debajo está la trampa del coste hundido: cambias una pérdida pequeña *segura* ahora por una grande *incierta* después, y como una pérdida segura escuece tanto, apostar para evitarla parece de verdad la jugada inteligente.»
  - S032 [honesta: «la única decisión honesta» applied to a decision] «La presión de tener una operación abierta es justo el sesgo que el stop se diseñó para anular; ensancharlo en caliente es tirar la única decisión honesta y sin presión que tomaste.»
  - S032 [not in cand: «es justo el sesgo» intensifier] «La presión de tener una operación abierta es justo el sesgo que el stop se diseñó para anular; ensancharlo en caliente es tirar la única decisión honesta y sin presión que tomaste.»
  - S038 [not in cand: «jamás» emphatic doubling of «nunca»] «nunca mueves un stop más lejos, jamás.»
  - S057 [en realidad: reframing tic; «El FOMO es miedo al arrepentimiento futuro» loses nothing] «El FOMO es en realidad miedo al *arrepentimiento futuro*: el dolor anticipado de verlo seguir sin ti se siente ahora mismo mayor que el riesgo real que tienes delante.»
  - S059 [not in cand: «justo donde» intensifier] «Acabas comprando una sensación, no un setup, y llegando justo donde los compradores anteriores se preparan para vendértelo.»
  - S066 [not in cand: «Mira los cuatro juntos y el mismo esqueleto asoma en todos.» announcer] «Mira los cuatro juntos y el mismo esqueleto asoma en todos.»
  - S068 [precisamente: intensifier on «porque»] «Cada uno llega con una frase razonable puesta —"recuperar lo perdido", "darle margen", "lo estoy leyendo perfecto", "me lo estoy perdiendo"— que te crees a medias precisamente porque está hecha a medida de lo que ya quieres hacer.»
  - S073 [not in cand: «es justo lo que falla» intensifier] «La fuerza de voluntad es justo lo que falla bajo el miedo y la codicia; un precompromiso funciona *porque* no depende de que seas fuerte en tu momento más débil.»
  - S080 [not in cand: «calladamente» tic] «Un stop se corre más lejos a lo largo de *días* mientras una tesis se endurece calladamente en esperanza, y un mes fuerte te tienta a sobredimensionar el siguiente swing.»
  - S086 [exactamente: intensifier] «A las 3 de la madrugada de un domingo el mercado sigue abierto y tu tilt aún tiene adónde ir, así que la única campana de cierre que tienes es la que te construyes tú, que es exactamente para lo que sirve el límite de pérdida diaria.»
- **2 Rhythmic triad** (4)
  - S027 [darle margen / el nivel está básicamente bien / va a rebotar; drop «el nivel está básicamente bien»] «Entonces: "voy a darle margen, el nivel está básicamente bien, va a rebotar".»
  - S056 [tarde / al peor precio del movimiento / sin lógica de entrada ni invalidación; first two overlap, drop «tarde»] «Compras tarde, al peor precio del movimiento, sin lógica de entrada ni invalidación.»
  - S061 [en el techo / sin stop / sin plan; drop «sin plan» (overlaps «sin stop»)] «A las tres velas verdes no lo aguantas y compras en el techo, sin stop, sin plan.»
  - S064 [tu entrada / tu stop / tu invalidación; stop and invalidation overlap, drop «tu invalidación»] «si no puedes decir tu entrada, tu stop y tu invalidación *antes* de hacer clic, no es una operación, es una persecución, y la dejas pasar.»
- **4 Summary/uplift closer** (7)
  - S008 [ahead: roadmap of how each pattern will be presented] «En cada uno miramos las mismas tres cosas —qué es, por qué ocurre (la maquinaria emocional que hay debajo) y qué aspecto tiene con números reales— y luego la regla de precompromiso que lo desactiva.»
  - S022 [restate: «Ese es el bucle…» sums up S020–S021] «Ese es el bucle: cada intento de borrar la pérdida la agranda y aprieta más el nudo.»
  - S040 [restate: repeats S039] «Un stop solo se mueve en la dirección en que la operación va bien.»
  - S051 [restate: sums up S050] «Una operación anodina, tomada con el tamaño equivocado, devuelve la racha entera.»
  - S053 [restate: recasts the rule in S052] «A los buenos resultados se les permite cambiar tu confianza; no se les permite cambiar tu tamaño.»
  - S065 [motivate: «Siempre hay otra oportunidad.»] «Siempre hay otra oportunidad.»
  - S092 [editorial: last prose unit ends on a comment about the feed, not on content] «Un timeline que solo muestra ganadores no es una prueba sobre la operación que tienes delante.»
- **5 Sentence over 30 words** (20)
  - S001 [36w] «A la mayoría de las cuentas no las destruye un análisis malo, sino una lista corta de patrones emocionales corrientes que se repiten en casi todo el mundo y que parecen del todo razonables mientras ocurren.»
  - S004 [38w] «En todos ellos, un plan tranquilo y sensato que hiciste por adelantado queda calladamente anulado por una versión de ti del momento que funciona con miedo, codicia u orgullo herido, y esa versión siempre tiene una razón preparada.»
  - S008 [35w **aside-only** (17w without asides)] «En cada uno miramos las mismas tres cosas —qué es, por qué ocurre (la maquinaria emocional que hay debajo) y qué aspecto tiene con números reales— y luego la regla de precompromiso que lo desactiva.»
  - S013 [33w] «Una pérdida duele más o menos el doble de lo que agrada una ganancia del mismo tamaño, así que tu cerebro archiva una cifra roja como una herida y exige cerrarla de inmediato.»
  - S014 [39w] «Además, has anclado calladamente en "recuperar lo perdido" —tu saldo de partida— como el estado natural del mundo, de modo que estar por debajo no se registra como un hecho neutro, sino como una amenaza continua que debes acabar.»
  - S031 [34w] «Debajo está la trampa del coste hundido: cambias una pérdida pequeña *segura* ahora por una grande *incierta* después, y como una pérdida segura escuece tanto, apostar para evitarla parece de verdad la jugada inteligente.»
  - S032 [32w] «La presión de tener una operación abierta es justo el sesgo que el stop se diseñó para anular; ensancharlo en caliente es tirar la única decisión honesta y sin presión que tomaste.»
  - S033 [31w **aside-only** (23w without asides)] «Promediar a la baja —añadir a la posición para "defender el nivel"— es la misma trampa con cara de ayuda: apila más riesgo sobre algo que ya va en tu contra.»
  - S045 [33w] «Atribuye las ganancias a tu habilidad y habría culpado a la mala suerte de las pérdidas, así que una serie de ruido se lee como prueba de que por fin "lo has pillado".»
  - S050 [56w] «La sexta operación no tiene nada de especial —una perdedora corriente—, pero con el triple de tamaño te cuesta 3R de golpe, y el mayor apalancamiento hace que el precio de liquidación quede ahora dentro del ruido rutinario, así que un movimiento que antes era una pequeña pérdida planificada puede sacarte del todo a la fuerza.»
  - S058 [36w] «La manada lo amplifica: cuando el precio y todos a tu alrededor se mueven y tú no, el propio movimiento empieza a parecer una prueba, cuando lo único que demuestra es que el precio ya subió.»
  - S062 [35w] «Minutos después revierte a la media un 15%: estás al instante en pérdida al peor precio de todo el movimiento, y como nunca definiste una invalidación no tienes ni idea de si aguantar o soltar.»
  - S068 [38w **aside-only** (25w without asides)] «Cada uno llega con una frase razonable puesta —"recuperar lo perdido", "darle margen", "lo estoy leyendo perfecto", "me lo estoy perdiendo"— que te crees a medias precisamente porque está hecha a medida de lo que ya quieres hacer.»
  - S069 [35w] «Cada uno se **decide peor en el momento y mejor por adelantado**, y por eso toda solución es una regla escrita cuando no había nada en juego, no más entereza invocada cuando lo hay todo.»
  - S070 [32w] «Cada uno tiene una señal que puedes notar antes de que te cueste: urgencia que sube, el picor de "arreglarlo" ya mismo, un subidón de sentirte imparable, el escozor de quedarte fuera.»
  - S078 [31w] «Day trading está en medio: la venganza aparece como saltarse el límite de pérdida diaria "para salvar el día", y el stop se ensancha sobre un nivel intradía que "siempre aguanta".»
  - S086 [47w] «A las 3 de la madrugada de un domingo el mercado sigue abierto y tu tilt aún tiene adónde ir, así que la única campana de cierre que tienes es la que te construyes tú, que es exactamente para lo que sirve el límite de pérdida diaria.»
  - S088 [38w] «A 100×, tu colchón de margen es de en torno al 1%, así que una sola decisión en tilt puede alcanzar el precio de liquidación y acabar con la cuenta antes de que hayas tenido tiempo de calmarte.»
  - S093 [50w] «La mayoría de las cuentas las destruyen cuatro patrones emocionales corrientes y no un mal análisis, y cada uno llega con una frase razonable puesta: «solo necesito una buena operación para volver a estar en paz», «voy a darle margen», «ahora mismo lo estoy leyendo perfecto», «me lo estoy perdiendo».»
  - S094 [70w] «Comparten una forma —al plan tranquilo que hiciste estando plano lo anula un yo del momento movido por el miedo, la codicia o el orgullo herido—, y por eso el remedio nunca es más fuerza de voluntad sino el compromiso previo: un límite de pérdida diaria, un stop que solo se mueve hacia el beneficio, un tamaño que no cambia con una racha y ninguna entrada sin una invalidación declarada.»
- **9 Course-coined term** (3)
  - S004 [«una versión de ti del momento»: coined label for the hot-state self] «En todos ellos, un plan tranquilo y sensato que hiciste por adelantado queda calladamente anulado por una versión de ti del momento que funciona con miedo, codicia u orgullo herido, y esa versión siempre tiene una razón preparada.»
  - S067 [«un yo del momento»: same coined label] «Cada uno es tu yo tranquilo y fuera del mercado siendo anulado por un yo del momento que funciona con un conjunto de incentivos distinto y peor.»
  - S094 [«un yo del momento»: same coined label] «Comparten una forma —al plan tranquilo que hiciste estando plano lo anula un yo del momento movido por el miedo, la codicia o el orgullo herido—, y por eso el remedio nunca es más fuerza de voluntad sino el compromiso previo: un límite de pérdida diaria, un stop que solo se mueve hacia el beneficio, un tamaño que no cambia con una racha y ninguna entrada sin una invalidación declarada.»
- **10 Metaphor then gloss** (6)
  - S033 [«la misma trampa con cara de ayuda: apila más riesgo…» glossed after the colon] «Promediar a la baja —añadir a la posición para "defender el nivel"— es la misma trampa con cara de ayuda: apila más riesgo sobre algo que ya va en tu contra.»
  - S063 [«la misma persecución pagada a plazos; solo significa que…» glossed after the semicolon] «Comprar "un poco" e ir *promediando al alza* según sigue subiendo es la misma persecución pagada a plazos; solo significa que tu mayor tamaño está al peor precio.»
  - S071 [«Esa sensación es la alarma: la señal para apoyarte en la regla» glossed after the colon] «Esa sensación es la alarma: la señal para apoyarte en la regla, no para saltártela.»
  - S084 [«interruptor automático externo que termina una espiral de venganza» glossed in the relative clause] «Un mercado de acciones cierra; la campana de cierre es un interruptor automático externo que termina una espiral de venganza, quieras o no.»
  - S086 [«la única campana de cierre… es la que te construyes tú, que es exactamente para lo que sirve el límite de pérdida diaria»] «A las 3 de la madrugada de un domingo el mercado sigue abierto y tu tilt aún tiene adónde ir, así que la única campana de cierre que tienes es la que te construyes tú, que es exactamente para lo que sirve el límite de pérdida diaria.»
  - S095 [«La propia sensación es la alarma: es la señal para apoyarte en la regla»] «La propia sensación es la alarma: es la señal para apoyarte en la regla, no para saltártela.»
- **11 Synonym rotation** (1)
  - S028 [widening the stop: deslizas el stop más lejos (S028), ensancharlo (S032), mover un stop más lejos (S038), ensanchar el stop (S079), se corre más lejos (S080)] 
- **A absolutes** (15)
  - S004 [siempre] «En todos ellos, un plan tranquilo y sensato que hiciste por adelantado queda calladamente anulado por una versión de ti del momento que funciona con miedo, codicia u orgullo herido, y esa versión siempre tiene una razón preparada.»
  - S012 [siempre] «La racionalización es siempre alguna versión de "solo necesito una buena operación para recuperar lo perdido".»
  - S014 [debes] «Además, has anclado calladamente en "recuperar lo perdido" —tu saldo de partida— como el estado natural del mundo, de modo que estar por debajo no se registra como un hecho neutro, sino como una amenaza continua que debes acabar.»
  - S015 [nunca] «La urgencia es la señal: una buena operación nunca es algo que *necesites* que pase ahora mismo.»
  - S016 [debe] «Con ella viaja un pariente cercano —"toca un rebote"—, pero el mercado no recuerda tus dos pérdidas ni te debe una tercera ganancia.»
  - S021 [nunca] «Pierde —las operaciones normales pierden constantemente— y ahora vas 140 USDT abajo, un agujero del 7%, y el impulso de hacerlo *otra vez*, más grande, es más fuerte que nunca.»
  - S024 [nunca, nunca] «Tu siguiente posición nunca es mayor que tu tamaño normal: una pérdida es motivo para *reducir o parar*, nunca para subir.»
  - S038 [nunca] «nunca mueves un stop más lejos, jamás.»
  - S046 [nunca] «Peor aún, el exceso de confianza se siente *idéntico* a la competencia desde dentro, de modo que nunca salta ninguna alarma interna que te avise.»
  - S062 [nunca] «Minutos después revierte a la media un 15%: estás al instante en pérdida al peor precio de todo el movimiento, y como nunca definiste una invalidación no tienes ni idea de si aguantar o soltar.»
  - S065 [siempre] «Siempre hay otra oportunidad.»
  - S078 [siempre] «Day trading está en medio: la venganza aparece como saltarse el límite de pérdida diaria "para salvar el día", y el stop se ensancha sobre un nivel intradía que "siempre aguanta".»
  - S085 [nunca] «Los perpetuos no cierran nunca.»
  - S090 [nunca] «El cripto vive en Twitter, Telegram y Discord, donde el feed es un goteo de las ganancias que otros capturan en pantalla y casi nunca de sus pérdidas.»
  - S094 [nunca, summary] «Comparten una forma —al plan tranquilo que hiciste estando plano lo anula un yo del momento movido por el miedo, la codicia o el orgullo herido—, y por eso el remedio nunca es más fuerza de voluntad sino el compromiso previo: un límite de pérdida diaria, un stop que solo se mueve hacia el beneficio, un tamaño que no cambia con una racha y ninguna entrada sin una invalidación declarada.»

**EN** — 53 hits, 96 sentences, density 55.2

- **1 Filler** (16)
  - S005 [not in cand: «quietly» tic (3 uses plus «silently»)] «In every one, a calm, sensible plan you made in advance gets quietly overruled by an in-the-moment version of you that is running on fear, greed, or wounded pride — and that version always has a reason ready.»
  - S006 [exactly: intensifier] «You do not fix this by trying to be calmer or more disciplined in the moment, because the moment is exactly when your judgment fails.»
  - S008 [not in cand: «The rest of this lesson is four patterns.» announcer] «The rest of this lesson is four patterns.»
  - S015 [not in cand: «silently» tic] «You have also silently anchored on "even" — your starting balance — as the natural state of the world, so sitting below it registers not as a neutral fact but as an ongoing threat you must end.»
  - S031 [not in cand: «quietly» tic] «To dodge that small hit to the ego, the mind quietly rewrites the plan.»
  - S032 [actually: emphatic «actually feels like the smart move»] «Underneath sits the sunk-cost trap: you swap a *certain* small loss now for an *uncertain* large one later — and because a sure loss stings so badly, taking a gamble to avoid it actually feels like the smart move.»
  - S033 [precisely: intensifier] «The pressure of holding an open trade is precisely the bias the stop was built to overrule; widening it in the heat throws away the one honest, pressure-free decision you made.»
  - S033 [honest: «the one honest… decision» applied to a decision] «The pressure of holding an open trade is precisely the bias the stop was built to overrule; widening it in the heat throws away the one honest, pressure-free decision you made.»
  - S039 [not in cand: «ever» emphatic tag] «you never move a stop wider, ever.»
  - S058 [really: reframing tic; «FOMO is fear of future regret» loses nothing] «FOMO is really fear of *future regret*: the anticipated pain of watching it run on without you feels larger, right now, than the real risk sitting in front of you.»
  - S060 [exactly: intensifier] «You end up buying a feeling, not a setup, and arriving exactly where the earlier buyers are getting ready to sell to you.»
  - S067 [not in cand: «Look at the four together and the same skeleton shows through» announcer] «Look at the four together and the same skeleton shows through every one.»
  - S069 [precisely: intensifier on «because»] «Each arrives wearing a reasonable sentence — "get back to even," "give it room," "I'm reading it perfectly," "I'm missing it" — that you half-believe precisely because it is tailored to what you already want to do.»
  - S074 [not in cand: «the very thing» intensifier] «Willpower is the very thing that fails under fear and greed; a pre-commitment works *because* it does not rely on you being strong at your weakest moment.»
  - S081 [not in cand: «quietly» tic] «A stop gets nudged wider over *days* as a thesis quietly hardens into hope, and a strong month tempts you to oversize the next swing.»
  - S087 [exactly: intensifier] «At 3 a.m. on a Sunday the market is still open and your tilt still has somewhere to go, so the only closing bell you get is the one you build yourself — which is exactly what the daily loss limit is for.»
- **2 Rhythmic triad** (4)
  - S028 [give it room / the level is basically fine / it'll bounce; drop «the level is basically fine»] «Then: "let me give it room — the level is basically fine, it'll bounce.»
  - S057 [late / at the worst price of the move / no entry logic and no invalidation; first two overlap, drop «late»] «You buy late, at the worst price of the move, with no entry logic and no invalidation.»
  - S062 [at the top / no stop / no plan; drop «no plan» (overlaps «no stop»)] «Three green candles in, you cannot stand it and you buy at the top, no stop, no plan.»
  - S065 [your entry / your stop / your invalidation; stop and invalidation overlap, drop «your invalidation»] «if you cannot state your entry, your stop, and your invalidation *before* you click, it is not a trade, it is a chase — and you skip it.»
- **4 Summary/uplift closer** (7)
  - S009 [ahead: roadmap of how each pattern will be presented] «For each one we look at the same three things — what it is, why it happens (the emotional machinery underneath), and what it looks like with real numbers — and then the pre-commitment rule that defuses it.»
  - S023 [restate: «That is the loop…» sums up S021–S022] «That is the loop: each attempt to erase the loss deepens it and tightens the grip.»
  - S041 [restate: repeats S040] «A stop only ever moves in the direction of the trade going right.»
  - S052 [restate: sums up S051] «One unremarkable trade, taken at the wrong size, gives back the whole streak.»
  - S054 [restate: recasts the rule in S053] «Good results are allowed to change your confidence; they are not allowed to change your size.»
  - S066 [motivate: «There is always another setup.»] «There is always another setup.»
  - S093 [editorial: last prose unit ends on a comment about the feed, not on content] «A timeline showing only winners is not evidence about the trade in front of you.»
- **5 Sentence over 30 words** (16)
  - S005 [37w] «In every one, a calm, sensible plan you made in advance gets quietly overruled by an in-the-moment version of you that is running on fear, greed, or wounded pride — and that version always has a reason ready.»
  - S007 [31w] «You fix it with pre-commitment: a rule written down while you are flat and calm, that removes the decision at the point where you are least able to make it well.»
  - S009 [36w **aside-only** (18w without asides)] «For each one we look at the same three things — what it is, why it happens (the emotional machinery underneath), and what it looks like with real numbers — and then the pre-commitment rule that defuses it.»
  - S015 [35w] «You have also silently anchored on "even" — your starting balance — as the natural state of the world, so sitting below it registers not as a neutral fact but as an ongoing threat you must end.»
  - S032 [38w] «Underneath sits the sunk-cost trap: you swap a *certain* small loss now for an *uncertain* large one later — and because a sure loss stings so badly, taking a gamble to avoid it actually feels like the smart move.»
  - S033 [31w] «The pressure of holding an open trade is precisely the bias the stop was built to overrule; widening it in the heat throws away the one honest, pressure-free decision you made.»
  - S051 [49w] «The sixth trade is nothing special — an ordinary loser — but at triple size it costs you 3R in one go, and the higher leverage means the liquidation price now sits inside routine noise, so a move that used to be a small planned loss can force you out entirely.»
  - S059 [35w] «The herd amplifies it — when price and everyone around you are moving and you are not, the move itself starts to feel like evidence, when all it actually proves is that price already went up.»
  - S063 [33w] «Minutes later it mean-reverts 15% — you are instantly underwater at the single worst price of the move, and because you never defined an invalidation you have no idea whether to hold or fold.»
  - S069 [35w **aside-only** (21w without asides)] «Each arrives wearing a reasonable sentence — "get back to even," "give it room," "I'm reading it perfectly," "I'm missing it" — that you half-believe precisely because it is tailored to what you already want to do.»
  - S070 [32w] «Each is **decided worst in the moment and best in advance**, which is why every fix is a rule written when nothing was at stake, not more resolve summoned when everything is.»
  - S071 [31w] «Each has a tell you can feel before it costs you: rising urgency, the itch to "fix" it right now, a flush of feeling unstoppable, the ache of being left out.»
  - S079 [32w] «Day trading sits in the middle: revenge shows up as blowing through the daily loss limit "to save the day," and the stop gets widened on an intraday level that "always holds."»
  - S087 [42w] «At 3 a.m. on a Sunday the market is still open and your tilt still has somewhere to go, so the only closing bell you get is the one you build yourself — which is exactly what the daily loss limit is for.»
  - S094 [46w] «Most accounts are destroyed by four ordinary emotional patterns rather than by bad analysis, and each arrives wearing a reasonable sentence: "I just need one good trade to get back to even", "let me give it room", "I'm reading it perfectly right now", "I'm missing it".»
  - S095 [63w] «They share a shape — the calm plan you made while flat is overruled by an in-the-moment self running on fear, greed or wounded pride — which is why the fix is never more willpower but pre-commitment: a daily loss limit, a stop that only ever moves toward profit, a size that does not change with a streak, and no entry without a stated invalidation.»
- **9 Course-coined term** (3)
  - S005 [«an in-the-moment version of you»: coined label for the hot-state self] «In every one, a calm, sensible plan you made in advance gets quietly overruled by an in-the-moment version of you that is running on fear, greed, or wounded pride — and that version always has a reason ready.»
  - S068 [«an in-the-moment self»: same coined label] «Each is your calm, flat self being overruled by an in-the-moment self running on a different, worse set of incentives.»
  - S095 [«an in-the-moment self»: same coined label] «They share a shape — the calm plan you made while flat is overruled by an in-the-moment self running on fear, greed or wounded pride — which is why the fix is never more willpower but pre-commitment: a daily loss limit, a stop that only ever moves toward profit, a size that does not change with a streak, and no entry without a stated invalidation.»
- **10 Metaphor then gloss** (6)
  - S034 [«the same trap wearing a helpful face: it piles more risk…» glossed after the colon] «Averaging down — adding to the position to "defend the level" — is the same trap wearing a helpful face: it piles more risk onto something already going against you.»
  - S064 [«the same chase paid in installments; it just means…» glossed after the semicolon] «Buying "a little" and *averaging up* as it keeps running is the same chase paid in installments; it just means your worst-priced size is your largest.»
  - S072 [«That feeling is the alarm — the signal to fall back on the rule»] «That feeling is the alarm — the signal to fall back on the rule, not to override it.»
  - S085 [«an external circuit breaker that ends a revenge spiral» glossed in the relative clause] «A stock market closes; the closing bell is an external circuit breaker that ends a revenge spiral whether you like it or not.»
  - S087 [«the only closing bell you get is the one you build yourself — which is exactly what the daily loss limit is for»] «At 3 a.m. on a Sunday the market is still open and your tilt still has somewhere to go, so the only closing bell you get is the one you build yourself — which is exactly what the daily loss limit is for.»
  - S096 [«The feeling itself is the alarm: it is the signal to fall back on the rule»] «The feeling itself is the alarm: it is the signal to fall back on the rule, not to override it.»
- **11 Synonym rotation** (1)
  - S029 [widening the stop: slide the stop further away (S029), widening it (S033), move a stop wider (S039), stop-widening (S080), nudged wider (S081)] 
- **A absolutes** (12)
  - S005 [always] «In every one, a calm, sensible plan you made in advance gets quietly overruled by an in-the-moment version of you that is running on fear, greed, or wounded pride — and that version always has a reason ready.»
  - S013 [always] «The rationalization is always some version of "I just need one good trade to get back to even."»
  - S015 [must] «You have also silently anchored on "even" — your starting balance — as the natural state of the world, so sitting below it registers not as a neutral fact but as an ongoing threat you must end.»
  - S016 [never] «The urgency is the tell: a sound trade is never something you *need* to happen right now.»
  - S025 [never, never] «Your next position is never larger than your normal size — a loss is a reason to size *down or stop*, never up.»
  - S039 [never] «you never move a stop wider, ever.»
  - S063 [never] «Minutes later it mean-reverts 15% — you are instantly underwater at the single worst price of the move, and because you never defined an invalidation you have no idea whether to hold or fold.»
  - S066 [always] «There is always another setup.»
  - S079 [always] «Day trading sits in the middle: revenge shows up as blowing through the daily loss limit "to save the day," and the stop gets widened on an intraday level that "always holds."»
  - S086 [never] «Perpetuals never close.»
  - S091 [never] «Crypto lives on Twitter, Telegram, and Discord, where the feed is a stream of other people's screenshotted wins and almost never their losses.»
  - S095 [never, summary] «They share a shape — the calm plan you made while flat is overruled by an in-the-moment self running on fear, greed or wounded pride — which is why the fix is never more willpower but pre-commitment: a daily loss limit, a stop that only ever moves toward profit, a size that does not change with a streak, and no entry without a stated invalidation.»

### m27-l1

**ES** — 59 hits, 102 sentences, density 57.8

- **1 Filler** (13)
  - S002 [simplemente: intensifier («decidida de antemano y luego ejecutada» says it)] «Una operación es esas piezas ensambladas en una sola cadena ininterrumpida, decidida de antemano y luego simplemente ejecutada.»
  - S003 [not in cand: «Esta lección recorre una única operación…» announcer] «Esta lección recorre una única operación de principio a fin, con números, para que veas el proceso entero de golpe, y para que veas que, cuando el dinero está en riesgo, casi todas las decisiones ya están tomadas.»
  - S005 [nada más: tag after «exactamente eso»] «Ten presente ese número: todo lo que viene después está construido para que equivocarse cueste exactamente eso y nada más.»
  - S008 [not in cand: «es justo lo que queremos» intensifier] «Un retroceso dentro de una tendencia alcista es justo lo que queremos: una oportunidad de unirnos a la tendencia a mejor precio, con la propia tendencia de nuestro lado.»
  - S011 [honesta: «la respuesta honesta» applied to an answer] «La mayor parte del tiempo la respuesta honesta a «¿qué se ofrece?» es *nada limpio*, y la mejor operación es ninguna.»
  - S022 [not in cand: «es justo la operación» intensifier] «Así que una señal del marco micro que contradice el sesgo macro es una operación descartada, no una oportunidad de operar en contra: un largo limpio en 1 hora dentro de una tendencia bajista diaria es justo la operación que este protocolo existe para rechazar.»
  - S036 [de verdad: emphatic «aparecieron de verdad»] «comprar el nivel a ciegas da por hecho que aguantará; esperar la reacción obliga al mercado a demostrar que los compradores aparecieron de verdad antes de comprometerte.»
  - S040 [sencillamente: intensifier] «Si el precio cierra bien por debajo de la mecha de rechazo —digamos por debajo de 59.300— esa tesis es sencillamente falsa: el nivel no aguantó.»
  - S053 [de verdad: emphatic «dibuja de verdad»] «Esos cuatro precios —el nivel, la entrada, el stop y el objetivo— son la operación entera, y son lo que un trader dibuja de verdad en el gráfico.»
  - S066 [honesta: «la única respuesta honesta» applied to an answer] «Si la única respuesta honesta es «está en verde», el stop se queda donde lo puso el plan.»
  - S069 [honestidad: «tiene que entrar la honestidad» applied to a reading of the phrase] «Es una forma legítima de asegurar avance y quitarle carga emocional al resto, pero la frase que lo vende —un «runner sin riesgo»— es donde tiene que entrar la honestidad, porque ese runner no es gratis y puedes ponerle precio exacto.»
  - S093 [precisamente: intensifier on «porque»] «Funciona precisamente porque no te consulta en el momento en que menos capaz eres de responder.»
  - S099 [simplemente: intensifier] «Sin ella, una tarde de −2% simplemente se prolonga en la misma sesión a las 3 de la madrugada, que es la hora en la que el tilt está menos vigilado.»
- **2 Rhythmic triad** (2)
  - S033 [empujaron por debajo / fueron absorbidos / perdieron; drop «y perdieron» (same as absorbed)] «Los vendedores empujaron por debajo del nivel, fueron absorbidos y perdieron.»
  - S091 [anclada en volver a cero / con sensación de urgencia / la persona menos cualificada del mundo; third is rhetorical, drop it] «La persona que decide si sigue operando tras un −3% es la versión de ti de la que habla todo m26: anclada en volver a estar en cero, con sensación de urgencia y la persona menos cualificada del mundo para juzgar su propio estado.»
- **4 Summary/uplift closer** (6)
  - S003 [ahead: lesson roadmap closes the intro paragraph] «Esta lección recorre una única operación de principio a fin, con números, para que veas el proceso entero de golpe, y para que veas que, cuando el dinero está en riesgo, casi todas las decisiones ya están tomadas.»
  - S005 [ahead: «todo lo que viene después…»] «Ten presente ese número: todo lo que viene después está construido para que equivocarse cueste exactamente eso y nada más.»
  - S012 [ahead: «así que miramos más de cerca»] «Hoy hay un retroceso en una tendencia alcista, así que miramos más de cerca.»
  - S029 [restate: S028 already said confluence improves the odds] «La confluencia es como conviertes un nivel a cara o cruz en un lugar donde vale la pena arriesgar dinero.»
  - S081 [editorial: «una operación planificada y ejecutada» after the result] «Resultado: +3,7R ≈ +370 USDT, o +3,0R ≈ +300 USDT si ejecutamos la versión con parciales de arriba: una operación planificada y ejecutada.»
  - S093 [restate: S092 already said pre-commitment decides it before the moment] «Funciona precisamente porque no te consulta en el momento en que menos capaz eres de responder.»
- **5 Sentence over 30 words** (22)
  - S003 [38w] «Esta lección recorre una única operación de principio a fin, con números, para que veas el proceso entero de golpe, y para que veas que, cuando el dinero está en riesgo, casi todas las decisiones ya están tomadas.»
  - S014 [48w] «Las temporalidades anidadas (m03-l2) y la elección de temporalidad según el estilo (m23) implican un paso del proceso que ninguna de las dos deja escrito, así que aquí queda nombrado: la temporalidad superior dicta el sesgo, la temporalidad inferior dicta la entrada, y el orden no es reversible.»
  - S021 [33w] «Déjale elegir la dirección y siempre encontrarás una que apunte donde ya querías ir: es el aviso de m03-l2 sobre saltar entre niveles de zoom para justificar una posición, llegando un paso antes.»
  - S022 [45w] «Así que una señal del marco micro que contradice el sesgo macro es una operación descartada, no una oportunidad de operar en contra: un largo limpio en 1 hora dentro de una tendencia bajista diaria es justo la operación que este protocolo existe para rechazar.»
  - S024 [45w] «El precio cae hacia 60.000, y allí coinciden tres cosas independientes: es el máximo previo que se rompió al subir (la vieja resistencia pasa a soporte), es el retroceso 0,618 del último tramo, y la EMA de 50 al alza trepa hacia la misma zona.»
  - S032 [36w] «Esperamos la reacción en el marco micro (véase m08-l2): el precio se hunde hasta 59.700, se forma una mecha inferior larga y la vela de 1 hora cierra de vuelta en 60.300, una vela de rechazo.»
  - S043 [31w **aside-only** (26w without asides)] «Colocado en la estructura, que te salte significa algo real —te equivocaste con el nivel— en vez de ser una distancia aleatoria que el mercado atraviesa con una mecha por ruido.»
  - S056 [34w **aside-only** (24w without asides)] «Hazlo en ese orden y el riesgo es constante en cada operación sin importar el precio ni el apalancamiento; invíertelo —elige un tamaño y luego busca un stop que «encaje»— y vuelves a apostar.»
  - S061 [69w] «El stop se mueve a break-even solo cuando la operación ha producido una confirmación nueva a su favor en la temporalidad de ejecución: una ruptura de estructura en la dirección de la operación, que en este largo significa un nuevo máximo más alto y después el mínimo más alto que le sigue, ambos por encima de la entrada, en el gráfico de 1 hora del que salió la entrada.»
  - S064 [37w **aside-only** (20w without asides)] «El verde es donde vive el ruido —una sola vela hasta 60.600 es un número que el mercado marca y borra todo el día— mientras que la estructura es algo que el precio ha tenido que *construir*.»
  - S068 [31w] «En esta operación el primer nivel contrario es el máximo menor en 62.300, exactamente +2R: vendes ahí el 40%, mueves el stop a 60.300 y dejas el 60% apuntando a 64.000.»
  - S069 [41w] «Es una forma legítima de asegurar avance y quitarle carga emocional al resto, pero la frase que lo vende —un «runner sin riesgo»— es donde tiene que entrar la honestidad, porque ese runner no es gratis y puedes ponerle precio exacto.»
  - S072 [32w] «Lo que compras a cambio es una proporción mayor de ganancias pequeñas: la operación que se atasca en 62.300 y se da la vuelta ahora sale en +0,8R en vez de 0.»
  - S073 [31w **aside-only** (30w without asides)] «Si esa operación merece la pena no te lo puede decir nadie en abstracto: son dos versiones de *tu* sistema, y el diario (m27-l2) es el único instrumento que puede compararlas.»
  - S089 [39w **aside-only** (25w without asides)] «La X la eliges tú, típicamente entre el 1 y el 3% (los estilos rápidos que hacen más operaciones al día pertenecen a la parte baja), y se fija en el plan, antes del día malo, nunca durante él.»
  - S091 [44w] «La persona que decide si sigue operando tras un −3% es la versión de ti de la que habla todo m26: anclada en volver a estar en cero, con sensación de urgencia y la persona menos cualificada del mundo para juzgar su propio estado.»
  - S096 [51w] «El mercado está abierto 24/7, así que una operación que colocas el viernes está viva y sin vigilancia todo el fin de semana, en libros poco profundos donde 60.000 puede recibir una mecha violenta con poco volumen: una razón más para que protejan el stop y el tamaño, no tu atención.»
  - S097 [34w] «Y como el apalancamiento está a un clic, la disciplina de *dimensionar desde el stop* es lo que evita que «0,1 BTC» se convierta en silencio en una posición cuyo stop es una liquidación.»
  - S098 [45w] «El 24/7 también significa que no hay campana de cierre que te dé por terminado un mal día, así que el «día» del *freno diario* tienes que definirlo tú: elige una hora de reinicio, escríbela (00:00 UTC, por ejemplo) y que esa sea la campana.»
  - S099 [31w] «Sin ella, una tarde de −2% simplemente se prolonga en la misma sesión a las 3 de la madrugada, que es la hora en la que el tilt está menos vigilado.»
  - S100 [52w] «Una operación de principio a fin, con las decisiones tomadas antes de arriesgar dinero: el gráfico diario da el contexto, tres razones independientes hacen de 60.000 una confluencia, la reacción en el nivel es el trigger, y el stop va donde la idea está muerta y no donde la pérdida resulta tolerable.»
  - S101 [45w] «El tamaño llega el último, desde el stop —presupuesto de riesgo ÷ distancia del stop—, y con la posición viva la habilidad más difícil es no hacer casi nada, moviendo el stop a break-even solo con un test estructural y nunca en contra de la operación.»
- **9 Course-coined term** (9)
  - S006 [lente [seed]] «Empieza por la lente más amplia, la pregunta del bloque D: ¿qué está *haciendo* el mercado y ofrece algo?»
  - S020 [«el marco micro»: coined label for the lower/execution timeframe] «el marco micro imprime señales constantemente, en las dos direcciones.»
  - S022 [«una señal del marco micro… el sesgo macro»: same coined pair] «Así que una señal del marco micro que contradice el sesgo macro es una operación descartada, no una oportunidad de operar en contra: un largo limpio en 1 hora dentro de una tendencia bajista diaria es justo la operación que este protocolo existe para rechazar.»
  - S023 [«todavía en el marco macro»: coined label for the higher timeframe] «Acércate al retroceso, todavía en el marco macro.»
  - S032 [«en el marco micro»: same coined label] «Esperamos la reacción en el marco micro (véase m08-l2): el precio se hunde hasta 59.700, se forma una mecha inferior larga y la vela de 1 hora cierra de vuelta en 60.300, una vela de rechazo.»
  - S084 [«un freno diario»: coined name for the daily loss limit / daily stop] «Así que el plan lleva un segundo límite, separado: un freno diario, que es el límite de pérdida diaria de m26 hecho mecánico.»
  - S092 [«el freno diario»: same coined term] «La respuesta de m26 era el compromiso previo —decidirlo cuando no hay nada en juego— y el freno diario es esa doctrina convertida en un número y un corte duro.»
  - S098 [«el «día» del *freno diario*»: same coined term] «El 24/7 también significa que no hay campana de cierre que te dé por terminado un mal día, así que el «día» del *freno diario* tienes que definirlo tú: elige una hora de reinicio, escríbela (00:00 UTC, por ejemplo) y que esa sea la campana.»
  - S102 [«un freno diario fijado en el plan»: same coined term] «Un segundo límite, separado, cierra el día: un freno diario fijado en el plan antes del día malo, que no te consulta cuando menos capaz eres de responder.»
- **10 Metaphor then gloss** (3)
  - S006 [«la lente más amplia» glossed as «la pregunta del bloque D: ¿qué está haciendo el mercado…?»] «Empieza por la lente más amplia, la pregunta del bloque D: ¿qué está *haciendo* el mercado y ofrece algo?»
  - S064 [«El verde es donde vive el ruido —una sola vela hasta 60.600 es un número que el mercado marca y borra…»] «El verde es donde vive el ruido —una sola vela hasta 60.600 es un número que el mercado marca y borra todo el día— mientras que la estructura es algo que el precio ha tenido que *construir*.»
  - S084 [«un freno diario, que es el límite de pérdida diaria de m26 hecho mecánico»] «Así que el plan lleva un segundo límite, separado: un freno diario, que es el límite de pérdida diaria de m26 hecho mecánico.»
- **11 Synonym rotation** (4)
  - S014 [higher timeframe: temporalidad superior (S014), gráfico lento (S015), marco macro (S023), gráfico diario (S013)] 
  - S014 [lower timeframe: temporalidad inferior (S014), gráfico rápido (S018), marco micro (S020), temporalidad de ejecución (S061)] 
  - S018 [invalidation: dónde está muerta la idea (S018), esa tesis es sencillamente falsa (S040), el precio que invalida el setup (S042)] 
  - S084 [daily loss limit: freno diario (S084), límite de pérdida diaria (S084), segundo límite (S084), corte duro (S092)] 
- **A absolutes** (8)
  - S021 [siempre] «Déjale elegir la dirección y siempre encontrarás una que apunte donde ya querías ir: es el aviso de m03-l2 sobre saltar entre niveles de zoom para justificar una posición, llegando un paso antes.»
  - S030 [nunca] «Un nivel es un *lugar que vigilar*, nunca una razón para comprar por sí solo.»
  - S037 [nunca] «Cuesta un poco de precio (compras a 60.300, no a 60.000) a cambio de pruebas: una operación que puedes rechazar si la reacción nunca llega.»
  - S074 [siempre] «Decídelo en el plan, ejecútalo igual siempre y deja que el registro diga qué versión gana.»
  - S077 [nunca] «Arriba en un largo, abajo en un corto; nunca en contra.»
  - S083 [nunca] «Nada limita todavía la pérdida de un día, y un mal día casi nunca es una sola operación.»
  - S089 [nunca] «La X la eliges tú, típicamente entre el 1 y el 3% (los estilos rápidos que hacen más operaciones al día pertenecen a la parte baja), y se fija en el plan, antes del día malo, nunca durante él.»
  - S101 [nunca, summary] «El tamaño llega el último, desde el stop —presupuesto de riesgo ÷ distancia del stop—, y con la posición viva la habilidad más difícil es no hacer casi nada, moviendo el stop a break-even solo con un test estructural y nunca en contra de la operación.»

**EN** — 47 hits, 102 sentences, density 46.1

- **1 Filler** (12)
  - S002 [simply: intensifier («decided in advance and then executed» says it)] «A trade is those pieces assembled into one unbroken chain, decided in advance and then simply executed.»
  - S003 [not in cand: «This lesson walks a single trade end to end…» announcer] «This lesson walks a single trade end to end, with numbers, so you can see the whole process at once — and see that by the time money is at risk, almost every decision has already been made.»
  - S005 [not in cand: «and no more» tag after «exactly that»] «Hold that number in mind: everything downstream is built to make being wrong cost exactly that and no more.»
  - S011 [honest: «the honest answer» applied to an answer] «Most of the time the honest answer to "what is on offer?" is *nothing clean* — and the best trade is no trade.»
  - S022 [precisely: intensifier] «So a micro-frame signal that contradicts the macro bias is a skipped trade, not a counter-trade opportunity: a clean 1-hour long inside a daily downtrend is precisely the trade this protocol exists to refuse.»
  - S036 [actually: emphatic «actually showed up»] «buying the level blind assumes it will hold; waiting for the reaction makes the market prove buyers actually showed up before you commit.»
  - S040 [simply: intensifier] «If price closes well below the rejection wick — say below 59,300 — that thesis is simply false: the level did not hold.»
  - S053 [actually: emphatic «actually draws»] «Those four prices — the level, the entry, the stop and the target — are the whole trade, and they are what a trader actually draws on the chart.»
  - S066 [honest: «the only honest answer» applied to an answer] «If the only honest answer is "it is up", the stop stays where the plan put it.»
  - S069 [honesty: «where the honesty has to come in» applied to a reading of the phrase] «It is a legitimate way to bank progress and take the emotional weight off the remainder — but the phrase that sells it, a *risk-free runner*, is where the honesty has to come in, because the runner is not free and you can price it exactly.»
  - S093 [precisely: intensifier on «because»] «It works precisely because it does not consult you at the moment you are least able to answer.»
  - S099 [simply: intensifier] «Without it, a −2% evening simply rolls into the same session at 3 a.m., which is the hour tilt is least supervised.»
- **2 Rhythmic triad** (2)
  - S033 [pushed below the level / were absorbed / lost; drop «and lost» (same as absorbed)] «Sellers pushed below the level, were absorbed, and lost.»
  - S092 [anchored on getting back to even / feeling urgency / the least qualified person in the world; third is rhetorical, drop it] «The person deciding whether to keep trading after −3% is the version of you all of m26 is about: anchored on getting back to even, feeling urgency, and the least qualified person in the world to assess their own state. m26's answer was pre-commitment — decide it when nothing is at stake — and the daily stop is that doctrine turned into a number and a hard cutoff.»
- **4 Summary/uplift closer** (6)
  - S003 [ahead: lesson roadmap closes the intro paragraph] «This lesson walks a single trade end to end, with numbers, so you can see the whole process at once — and see that by the time money is at risk, almost every decision has already been made.»
  - S005 [ahead: «everything downstream…»] «Hold that number in mind: everything downstream is built to make being wrong cost exactly that and no more.»
  - S012 [ahead: «so we look closer»] «Today there is a pullback in an uptrend, so we look closer.»
  - S029 [restate: S028 already said confluence improves the odds] «Confluence is how you turn a coin-flip level into a location worth risking money at.»
  - S082 [editorial: «a planned trade, executed» after the result] «Result: +3.7R ≈ +370 USDT — or +3.0R ≈ +300 USDT if we ran the partials version above — a planned trade, executed.»
  - S093 [restate: S092 already said pre-commitment decides it before the moment] «It works precisely because it does not consult you at the moment you are least able to answer.»
- **5 Sentence over 30 words** (16)
  - S003 [37w] «This lesson walks a single trade end to end, with numbers, so you can see the whole process at once — and see that by the time money is at risk, almost every decision has already been made.»
  - S014 [40w] «Nested timeframes (m03-l2) and the timeframe-per-style choice (m23) both imply a process step neither one spells out, so here it is, named: the higher timeframe dictates the bias, the lower timeframe dictates the entry — and the order is not reversible.»
  - S021 [35w] «Let it choose the direction and you will always find one pointing where you already wanted to go — that is m03-l2's warning about flipping between zoom levels to justify a position, arriving one step earlier.»
  - S022 [34w] «So a micro-frame signal that contradicts the macro bias is a skipped trade, not a counter-trade opportunity: a clean 1-hour long inside a daily downtrend is precisely the trade this protocol exists to refuse.»
  - S024 [47w] «Price is falling toward 60,000, and three independent things line up there: it is the prior swing high that broke on the way up (old resistance becomes support), it is the 0,618 retracement of the last leg, and the rising 50-EMA is climbing into the same zone.»
  - S032 [31w **aside-only** (29w without asides)] «We wait for the reaction on the micro frame (see m08-l2): price dips to 59,700, a long lower wick forms and the 1-hour candle closes back at 60,300 — a rejection candle.»
  - S056 [35w **aside-only** (25w without asides)] «Do it in that order and risk is constant across every trade regardless of price or leverage; reverse it — pick a size, then find a stop that "feels" right — and you are back to gambling.»
  - S061 [56w] «The stop moves to break-even only once the trade has produced new confirmation in its favour on the execution timeframe — a break of structure in the trade's direction, which for this long means a fresh higher high and then the higher low that follows it, both above entry, on the 1-hour chart the entry came from.»
  - S069 [45w] «It is a legitimate way to bank progress and take the emotional weight off the remainder — but the phrase that sells it, a *risk-free runner*, is where the honesty has to come in, because the runner is not free and you can price it exactly.»
  - S074 [35w] «Whether that exchange is worth making is not something anyone can tell you in the abstract: it is two versions of *your* system, and the journal (m27-l2) is the only instrument that can compare them.»
  - S090 [35w **aside-only** (23w without asides)] «The X is yours to pick, typically 1–3% (faster styles taking more trades a day belong at the low end), and it is set in the plan, before the losing day — never adjusted during one.»
  - S092 [66w] «The person deciding whether to keep trading after −3% is the version of you all of m26 is about: anchored on getting back to even, feeling urgency, and the least qualified person in the world to assess their own state. m26's answer was pre-commitment — decide it when nothing is at stake — and the daily stop is that doctrine turned into a number and a hard cutoff.»
  - S096 [44w] «The market is open 24/7, so a trade you place on Friday is live and unwatched all weekend, on thin books where 60,000 can be wicked hard on low volume — another reason the stop and the size, not your attention, must do the protecting.»
  - S098 [44w] «24/7 also means there is no closing bell to end a bad day for you, so the "day" in *daily stop* is one you have to define yourself: pick a reset hour, write it down (00:00 UTC, say), and let that be the bell.»
  - S100 [50w] «One trade end to end, with the decisions made before money is at risk: the daily chart gives the context, three independent reasons make 60,000 confluence, the reaction at the level is the trigger, and the stop goes where the idea is dead rather than where the loss feels tolerable.»
  - S101 [40w] «Size comes last, from the stop — risk budget ÷ stop distance — and once the position is live the hardest skill is doing almost nothing, with the stop moving to break-even only against a structural test and never away from the trade.»
- **9 Course-coined term** (5)
  - S006 [lens [seed]] «Start with the widest lens, the block-D question: what is the market *doing*, and does it offer anything?»
  - S020 [«the micro frame»: coined label for the lower/execution timeframe] «the micro frame prints signals constantly, in both directions.»
  - S022 [«a micro-frame signal… the macro bias»: same coined pair] «So a micro-frame signal that contradicts the macro bias is a skipped trade, not a counter-trade opportunity: a clean 1-hour long inside a daily downtrend is precisely the trade this protocol exists to refuse.»
  - S023 [«still on the macro frame»: coined label for the higher timeframe] «Zoom in on the pullback, still on the macro frame.»
  - S032 [«on the micro frame»: same coined label] «We wait for the reaction on the micro frame (see m08-l2): price dips to 59,700, a long lower wick forms and the 1-hour candle closes back at 60,300 — a rejection candle.»
- **10 Metaphor then gloss** (2)
  - S006 [«the widest lens» glossed as «the block-D question: what is the market doing…?»] «Start with the widest lens, the block-D question: what is the market *doing*, and does it offer anything?»
  - S064 [«Green is where noise lives — a single candle to 60,600 is a number the market prints and unprints…»] «Green is where noise lives — a single candle to 60,600 is a number the market prints and unprints all day — while structure is something price had to *build*.»
- **11 Synonym rotation** (4)
  - S014 [higher timeframe: higher timeframe (S014), slower chart (S015), macro frame (S023), daily chart (S013)] 
  - S014 [lower timeframe: lower timeframe (S014), faster chart (S018), micro frame (S020), execution timeframe (S061)] 
  - S018 [invalidation: where is the idea dead (S018), that thesis is simply false (S040), the price that invalidates the setup (S042)] 
  - S085 [daily loss limit: daily stop (S085), daily loss limit (S085), second, separate limit (S085), hard cutoff (S092)] 
- **A absolutes** (7)
  - S021 [always] «Let it choose the direction and you will always find one pointing where you already wanted to go — that is m03-l2's warning about flipping between zoom levels to justify a position, arriving one step earlier.»
  - S030 [never] «A level is a *place to watch*, never a reason to buy on its own.»
  - S037 [never] «It costs a little price (you buy at 60,300, not 60,000) in exchange for evidence — a trade you can refuse if the reaction never comes.»
  - S078 [never] «Up for a long, down for a short — never away.»
  - S090 [never] «The X is yours to pick, typically 1–3% (faster styles taking more trades a day belong at the low end), and it is set in the plan, before the losing day — never adjusted during one.»
  - S096 [must] «The market is open 24/7, so a trade you place on Friday is live and unwatched all weekend, on thin books where 60,000 can be wicked hard on low volume — another reason the stop and the size, not your attention, must do the protecting.»
  - S101 [never, summary] «Size comes last, from the stop — risk budget ÷ stop distance — and once the position is live the hardest skill is doing almost nothing, with the stop moving to break-even only against a structural test and never away from the trade.»

### m27-l2

**ES** — 33 hits, 62 sentences, density 53.2

- **1 Filler** (10)
  - S001 [de verdad: emphatic «¿mi proceso funciona de verdad…?»] «Un plan de trading es una hipótesis: «este proceso gana dinero». m27-l1 construyó una operación completa; esta lección trata de la maquinaria que convierte un montón de operaciones en una respuesta a la única pregunta que importa: *¿mi proceso funciona de verdad y cómo lo sé?»
  - S014 [honesto: «hace el registro honesto» applied to a record] «Una captura de pantalla rápida del gráfico en la entrada y la salida hace el registro honesto y fácil de revisar después.»
  - S024 [de verdad: emphatic «nunca siguieron de verdad»] «sin el diario estos dos parecen lo mismo —un número rojo— y los principiantes los confunden una y otra vez: abandonan un buen sistema tras pérdidas autoinfligidas o se aferran a uno malo que nunca siguieron de verdad.»
  - S027 [de verdad: emphatic «buena de verdad»] «La idea es buena de verdad, *y* trae una condición previa que la propuesta siempre se deja fuera.»
  - S034 [simplemente: intensifier] «Si tras un centenar de operaciones tus operaciones A promedian, digamos, +0,6R y tus B +0,05R, tu calificación está haciendo un trabajo real y escalonar el riesgo es simplemente actuar sobre información medida.»
  - S037 [not in cand: «justo con la racha de suerte» intensifier] «Doce operaciones A no demuestran nada, y la tentación es declarar la escala probada justo con la racha de suerte que te hizo sentirte capaz de calificar.»
  - S051 [de verdad: emphatic «de verdad trivial»] «Elige un tamaño en el que un −1R completo te sea de verdad trivial.»
  - S055 [not in cand: «la inversión exacta de la regla» intensifier] «Subir el tamaño tras una pérdida para «recuperar más rápido» es la inversión exacta de la regla: es el reflejo del trader perdedor y convierte una racha adversa en una cuenta reventada.»
  - S059 [fíjate: announcer «Y fíjate otra vez en…»] «Y fíjate otra vez en el límite honesto: como el slippage real, los costes de funding y los gaps nocturnos de cripto (unlocks de m20, liquidez de m19-l2) no están en la demo, trata los resultados en papel como un techo optimista, no como el número que ganarás de verdad.»
  - S059 [honesto: «el límite honesto» applied to a limit] «Y fíjate otra vez en el límite honesto: como el slippage real, los costes de funding y los gaps nocturnos de cripto (unlocks de m20, liquidez de m19-l2) no están en la demo, trata los resultados en papel como un techo optimista, no como el número que ganarás de verdad.»
- **4 Summary/uplift closer** (4)
  - S002 [ahead: lesson roadmap («Tres partes:…») closes the intro paragraph] «Tres partes: el diario que registra las pruebas, la validación que reúne suficientes antes de arriesgar dinero real, y el paso disciplinado al dinero real cuando lo hace.»
  - S025 [restate: «Solo el registro los distingue.» repeats S024] «Solo el registro los distingue.»
  - S029 [editorial: «Por eso esta sección va después de él y no antes.»] «Por eso esta sección va después de él y no antes.»
  - S049 [restate: repeats S048 (learn where mistakes are cheap)] «La validación traslada el aprendizaje a donde los errores son baratos.»
- **5 Sentence over 30 words** (15)
  - S001 [46w] «Un plan de trading es una hipótesis: «este proceso gana dinero». m27-l1 construyó una operación completa; esta lección trata de la maquinaria que convierte un montón de operaciones en una respuesta a la única pregunta que importa: *¿mi proceso funciona de verdad y cómo lo sé?»
  - S015 [33w **aside-only** (27w without asides)] «medir en R elimina el tamaño de posición y el tamaño de la cuenta, así que cien operaciones se vuelven una distribución limpia que sí puedes juzgar (esta es la muestra de m25).»
  - S024 [38w] «sin el diario estos dos parecen lo mismo —un número rojo— y los principiantes los confunden una y otra vez: abandonan un buen sistema tras pérdidas autoinfligidas o se aferran a uno malo que nunca siguieron de verdad.»
  - S026 [35w] «Tarde o temprano alguien te dirá que dimensiones según la calidad del setup: arriesgar el 0,5–1% en los setups normales y hasta el 2% en los mejores, para que el dinero siga a la convicción.»
  - S030 [34w **aside-only** (20w without asides)] «El riesgo fraccionario fijo (m22) —el mismo 1% en cada operación, sin importar cómo se sienta el setup— es la disciplina para todo el mundo y para la mayor parte de una vida operando.»
  - S034 [33w] «Si tras un centenar de operaciones tus operaciones A promedian, digamos, +0,6R y tus B +0,05R, tu calificación está haciendo un trabajo real y escalonar el riesgo es simplemente actuar sobre información medida.»
  - S038 [35w] «Sin las pruebas, «arriesgar más en los mejores setups» se derrumba en *arriesgar más cuando me siento más convencido*, que es el momento en el que m26 dice que eres más peligroso para ti mismo.»
  - S039 [38w] «Dos barandillas se mantienen en cualquier caso: nunca por encima del 2%, y la calificación se asigna antes de entrar, nunca se revisa al alza a mitad de operación ni después de una pérdida para agrandar la siguiente.»
  - S043 [32w] «Un puñado de operaciones es ruido (m25): un sistema del 60% de acierto puede mostrar fácilmente 3 perdedoras en sus primeras 5, y un mal sistema puede colar 4 ganadoras por suerte.»
  - S055 [32w] «Subir el tamaño tras una pérdida para «recuperar más rápido» es la inversión exacta de la regla: es el reflejo del trader perdedor y convierte una racha adversa en una cuenta reventada.»
  - S058 [53w] «Las cuentas demo y los tamaños diminutos están disponibles 24/7 sin esfuerzo, así que no hay excusa para no validar; pero ese mismo acceso 24/7, el apalancamiento alto y el feed lleno de las ganancias de otros empujan con fuerza en sentido contrario, hacia subir el tamaño rápido sobre una ventaja sin probar.»
  - S059 [50w] «Y fíjate otra vez en el límite honesto: como el slippage real, los costes de funding y los gaps nocturnos de cripto (unlocks de m20, liquidez de m19-l2) no están en la demo, trata los resultados en papel como un techo optimista, no como el número que ganarás de verdad.»
  - S060 [44w] «La memoria miente, así que el diario es el único instrumento que puede decirte la verdad: setup, plan, ejecución frente a ese plan y el resultado en R y no en dólares, para que cien operaciones se conviertan en una distribución que puedas juzgar.»
  - S061 [39w] «La revisión semanal ordena cada operación en seguí el plan o no lo seguí, lo que separa dos fallos que como número rojo parecen idénticos y piden respuestas opuestas: un sistema roto pide estudio, una ejecución rota pide disciplina.»
  - S062 [48w] «Valida donde equivocarse es gratis, recuerda que la demo prueba el proceso y nunca el miedo, y da el paso al dinero real con un tamaño en el que un −1R completo sea trivial, escalando solo con lo que demuestre el registro y nunca para recuperar una pérdida.»
- **10 Metaphor then gloss** (3)
  - S003 [«La memoria miente.» glossed in S004] «La memoria miente.»
  - S031 [«una muleta de principiante» glossed as «la versión que tu estado de ánimo no puede corromper»] «No es una muleta de principiante de la que te gradúas; es la versión que tu estado de ánimo no puede corromper, porque no tiene ninguna rueda que girar.»
  - S048 [«pagando la matrícula a la tarifa más cara posible» glossed in S049] «la alternativa es descubrir si tu sistema funciona usando dinero que no puedes permitirte perder, pagando la matrícula a la tarifa más cara posible.»
- **11 Synonym rotation** (1)
  - S041 [paper trading: cuenta demo (S041), papel (S045), dinero de mentira (S046), resultados en papel (S059)] 
- **A absolutes** (6)
  - S022 [nunca] «El sistema nunca se probó; la variable fuiste *tú*.»
  - S024 [nunca] «sin el diario estos dos parecen lo mismo —un número rojo— y los principiantes los confunden una y otra vez: abandonan un buen sistema tras pérdidas autoinfligidas o se aferran a uno malo que nunca siguieron de verdad.»
  - S027 [siempre] «La idea es buena de verdad, *y* trae una condición previa que la propuesta siempre se deja fuera.»
  - S039 [nunca, nunca] «Dos barandillas se mantienen en cualquier caso: nunca por encima del 2%, y la calificación se asigna antes de entrar, nunca se revisa al alza a mitad de operación ni después de una pérdida para agrandar la siguiente.»
  - S056 [nunca] «El tamaño sigue a la ventaja demostrada, nunca a la necesidad de recuperar.»
  - S062 [nunca, nunca, summary] «Valida donde equivocarse es gratis, recuerda que la demo prueba el proceso y nunca el miedo, y da el paso al dinero real con un tamaño en el que un −1R completo sea trivial, escalando solo con lo que demuestre el registro y nunca para recuperar una pérdida.»

**EN** — 28 hits, 64 sentences, density 43.8

- **1 Filler** (10)
  - S001 [actually: emphatic «does my process actually work»] «A trading plan is a hypothesis: "this process makes money." m27-l1 built one complete trade; this lesson is about the machinery that turns a pile of trades into an answer to the only question that matters — *does my process actually work, and how do I know?»
  - S014 [honest: «makes the record honest» applied to a record] «A quick screenshot of the chart at entry and exit makes the record honest and fast to review later.»
  - S026 [actually: emphatic «never actually followed»] «without the journal these two look the same — a red number — and beginners consistently misread them, abandoning a good system after self-inflicted losses or clinging to a bad one they never actually followed.»
  - S029 [genuinely: emphatic «genuinely sound»] «The idea is genuinely sound — *and* it carries a precondition the pitch always leaves out.»
  - S036 [simply: intensifier] «If after a hundred-odd trades your A trades average, say, +0.6R and your B trades +0.05R, your grading is doing real work and tiering the risk is simply acting on measured information.»
  - S039 [exactly: intensifier] «Twelve A trades prove nothing, and the temptation is to declare the ladder proven on exactly the lucky run that made you feel like a grader in the first place.»
  - S053 [genuinely: emphatic «genuinely trivial»] «Pick a size where a full −1R is genuinely trivial to you.»
  - S057 [not in cand: «the exact inversion of the rule» intensifier] «Raising size after a loss to "make it back faster" is the exact inversion of the rule: it is the losing trader's reflex, and it turns a drawdown into a blown account.»
  - S061 [honest: «the honest limit» applied to a limit] «And note the honest limit again: because crypto's real slippage and funding costs and overnight gaps (m20 unlocks, m19-l2 liquidity) are absent on demo, treat paper results as an optimistic ceiling, not the number you will actually earn.»
  - S061 [not in cand: «And note… again» announcer] «And note the honest limit again: because crypto's real slippage and funding costs and overnight gaps (m20 unlocks, m19-l2 liquidity) are absent on demo, treat paper results as an optimistic ceiling, not the number you will actually earn.»
- **4 Summary/uplift closer** (4)
  - S002 [ahead: lesson roadmap («Three parts:…») closes the intro paragraph] «Three parts: the journal that records the evidence, the validation that gathers enough of it before you risk real money, and the disciplined step to real money once it does.»
  - S027 [restate: «Only the record tells them apart.» repeats S026] «Only the record tells them apart.»
  - S031 [editorial: «That is why this section sits after it and not before.»] «That is why this section sits after it and not before.»
  - S051 [restate: repeats S050 (learn where mistakes are cheap)] «Validation moves the learning to where mistakes are cheap.»
- **5 Sentence over 30 words** (10)
  - S001 [46w] «A trading plan is a hypothesis: "this process makes money." m27-l1 built one complete trade; this lesson is about the machinery that turns a pile of trades into an answer to the only question that matters — *does my process actually work, and how do I know?»
  - S026 [33w **aside-only** (30w without asides)] «without the journal these two look the same — a red number — and beginners consistently misread them, abandoning a good system after self-inflicted losses or clinging to a bad one they never actually followed.»
  - S028 [31w] «Sooner or later someone will tell you to size by setup quality: risk 0.5–1% on ordinary setups and up to 2% on your best ones, so the money follows the conviction.»
  - S036 [32w] «If after a hundred-odd trades your A trades average, say, +0.6R and your B trades +0.05R, your grading is doing real work and tiering the risk is simply acting on measured information.»
  - S057 [32w] «Raising size after a loss to "make it back faster" is the exact inversion of the rule: it is the losing trader's reflex, and it turns a drawdown into a blown account.»
  - S060 [45w] «Demo accounts and tiny position sizes are trivially available 24/7, so there is no excuse not to validate — but the same 24/7 access, high leverage, and feed full of other people's wins push hard the other way, toward sizing up fast on an untested edge.»
  - S061 [38w] «And note the honest limit again: because crypto's real slippage and funding costs and overnight gaps (m20 unlocks, m19-l2 liquidity) are absent on demo, treat paper results as an optimistic ceiling, not the number you will actually earn.»
  - S062 [39w] «Memory lies, so the journal is the only instrument that can tell you the truth: setup, plan, execution against that plan, and the result in R rather than dollars, so a hundred trades become one distribution you can judge.»
  - S063 [38w] «The weekly review sorts every trade into followed the plan or did not, which separates two failures that look identical as a red number and need opposite responses — a broken system needs study, a broken execution needs discipline.»
  - S064 [43w] «Validate where being wrong is free, remember demo tests the process and never the fear, and step to real money at a size where a full −1R is trivial, scaling only on what the record proves and never to win a loss back.»
- **10 Metaphor then gloss** (3)
  - S003 [«Memory lies.» glossed in S004] «Memory lies.»
  - S033 [«a beginner's crutch» glossed as «the version that cannot be corrupted by your mood»] «It is not a beginner's crutch you graduate out of; it is the version that cannot be corrupted by your mood, because it has no dial to turn.»
  - S050 [«paying tuition at the most expensive possible rate» glossed in S051] «the alternative is discovering whether your system works using money you cannot afford to lose — paying tuition at the most expensive possible rate.»
- **11 Synonym rotation** (1)
  - S043 [paper trading: demo account (S043), paper trading (S047), play money (S048), paper results (S061)] 
- **A absolutes** (6)
  - S024 [never] «The system was never tested; *you* were the variable.»
  - S026 [never] «without the journal these two look the same — a red number — and beginners consistently misread them, abandoning a good system after self-inflicted losses or clinging to a bad one they never actually followed.»
  - S029 [always] «The idea is genuinely sound — *and* it carries a precondition the pitch always leaves out.»
  - S041 [never, never, never] «Two guard-rails hold either way: never above 2%, and the grade is assigned before entry — never revised upward mid-trade, and never after a loss to make the next trade bigger.»
  - S058 [never] «Size follows proven edge, never the need to recover.»
  - S064 [never, never, summary] «Validate where being wrong is free, remember demo tests the process and never the fear, and step to real money at a size where a full −1R is trivial, scaling only on what the record proves and never to win a loss back.»

### m28-l1

**ES** — 37 hits, 81 sentences, density 45.7

- **1 Filler** (18)
  - S003 [not in cand: «Y ahora la parte incómoda.» announcer] «Y ahora la parte incómoda.»
  - S005 [de verdad: emphatic «produzcan de verdad»] «Apuntaste un win rate y un payoff medio, los multiplicaste y salió una respuesta, pero nadie ha comprobado que tus reglas produzcan de verdad ese win rate en este mercado.»
  - S006 [not in cand: «absolutamente» intensifier («no vale absolutamente nada»)] «La esperanza es una *afirmación*, y hasta que se pone a prueba no vale absolutamente nada.»
  - S011 [honesto: «lo hacen honesto» applied to a test/reading] «Tres condiciones lo hacen honesto, y cada una está ahí por una forma concreta de engañarse a uno mismo.»
  - S013 [not in cand: «calladamente» tic] «Si no puedes escribirlas, no tienes un sistema: tienes un conjunto de preferencias que se irán recolocando calladamente alrededor de lo que hizo el gráfico.»
  - S014 [not in cand: «Ese fallo ya tiene nombre en este curso.» announcer] «Ese fallo ya tiene nombre en este curso.»
  - S018 [not in cand: «Esta es la parte que todo el mundo se salta y es la que importa» announcer] «Esta es la parte que todo el mundo se salta y es la que importa, porque un ojo que ha visto el desenlace no puede dejar de verlo.»
  - S027 [not in cand: «en absoluto» intensifier] «Así que quien hace veinte operaciones, ve un 60% de aciertos y concluye «el sistema funciona» no ha aprendido nada en absoluto sobre su sistema, y quien ve un 35% y tira el sistema a la basura ha hecho lo mismo en la otra dirección.»
  - S033 [honesta: «La regla honesta» applied to a rule] «**La regla honesta: las decenas no dicen nada, los cientos empiezan a hablar.**»
  - S034 [fíjate en: announcer] «Y fíjate en lo que esto le hace a la aritmética de m25.»
  - S046 [not in cand: «La pista es fácil de decir y difícil de aceptar:» announcer] «La pista es fácil de decir y difícil de aceptar: cuanto más fino sea el ajuste de un sistema a los datos con los que se construyó, menos suele sobrevivir al contacto con datos que no ha visto.»
  - S047 [not in cand: «La defensa es una de las ideas más simples de la estadística y no necesita vocabulario:» announcer] «La defensa es una de las ideas más simples de la estadística y no necesita vocabulario:»
  - S061 [not in cand: «Esta es la que se subestima.» announcer] «Esta es la que se subestima.»
  - S064 [de verdad: emphatic «si de verdad lo ejecutas»] «La esperanza del sistema solo es la esperanza del sistema si de verdad lo ejecutas.»
  - S065 [honesta: «limitación honesta» applied to a limit] «La demo tiene su propia limitación honesta: no te cuesta nada, así que no pone a prueba la psicología.»
  - S066 [justamente: intensifier] «Por eso justamente m27-l2 pasa a *tamaño real mínimo* en lugar de quedarse en demo: la cantidad más pequeña que aun así escuece es la forma más barata de averiguar qué haces bajo presión.»
  - S067 [not in cand: «Es el juicio más difícil del trading, y es difícil por una razón concreta y estructural:» announcer] «Es el juicio más difícil del trading, y es difícil por una razón concreta y estructural:»
  - S079 [honesto: «un backtest solo es honesto» applied to a test/reading] «La esperanza matemática era una suposición hasta que algo la puso a prueba, y un backtest solo es honesto bajo tres condiciones: las reglas escritas antes de mirar, barra a barra y sin retroceder —porque un ojo que ha visto el desenlace no puede dejar de verlo— y cada operación registrada en R.»
- **4 Summary/uplift closer** (5)
  - S006 [restate: S004 already said the number was an assumption] «La esperanza es una *afirmación*, y hasta que se pone a prueba no vale absolutamente nada.»
  - S009 [editorial: «Cobra por operación.» witty tag on S008] «Cobra por operación.»
  - S011 [ahead: announces the three conditions that follow] «Tres condiciones lo hacen honesto, y cada una está ahí por una forma concreta de engañarse a uno mismo.»
  - S016 [restate: «Con una regla pasa igual.» repeats S015] «Con una regla pasa igual.»
  - S022 [editorial: «una muestra que no anotaste no es una muestra»] «Un backtest es un diario de operaciones que no costaron nada, y se lee igual: estás construyendo la *muestra* de la que va la sección siguiente, y una muestra que no anotaste no es una muestra.»
- **5 Sentence over 30 words** (12)
  - S019 [31w] «Mirar un movimiento ya terminado y preguntarse «¿yo habría entrado aquí?» no es una prueba: la respuesta es siempre que sí, y en la dirección a la que fue el movimiento.»
  - S022 [36w] «Un backtest es un diario de operaciones que no costaron nada, y se lee igual: estás construyendo la *muestra* de la que va la sección siguiente, y una muestra que no anotaste no es una muestra.»
  - S027 [45w] «Así que quien hace veinte operaciones, ve un 60% de aciertos y concluye «el sistema funciona» no ha aprendido nada en absoluto sobre su sistema, y quien ve un 35% y tira el sistema a la basura ha hecho lo mismo en la otra dirección.»
  - S035 [52w] «La esperanza es win rate por ganancia media menos tasa de fallo por pérdida media, así que una banda de error de ±11 puntos en el win rate es también una banda de error en la esperanza; con veinte operaciones, lo bastante ancha como para contener a la vez «rentable» y «desangrándose».»
  - S046 [38w] «La pista es fácil de decir y difícil de aceptar: cuanto más fino sea el ajuste de un sistema a los datos con los que se construyó, menos suele sobrevivir al contacto con datos que no ha visto.»
  - S055 [37w] «Si solo funciona en la mitad a la que se ajustó, no es un sistema, es una descripción, y la disciplina consiste en decirlo y volver a empezar, no en ir a ajustar también la segunda mitad.»
  - S059 [37w] «Tu stop-limit no se ejecuta (m24); cruzas un spread más ancho del que suponía el backtest; el slippage de la entrada se come un quinto de la ventaja; el funding se acumula en las tenencias de swing.»
  - S066 [34w] «Por eso justamente m27-l2 pasa a *tamaño real mínimo* en lugar de quedarse en demo: la cantidad más pequeña que aun así escuece es la forma más barata de averiguar qué haces bajo presión.»
  - S073 [56w] «Decide, por escrito y por adelantado, qué contaría como prueba de que el sistema está roto: un drawdown más profundo que el peor que produjo el backtest, una esperanza observada que lleva por debajo de la declarada durante una muestra suficientemente grande, una racha perdedora más larga de lo que dice la aritmética que debería ocurrir.»
  - S079 [53w] «La esperanza matemática era una suposición hasta que algo la puso a prueba, y un backtest solo es honesto bajo tres condiciones: las reglas escritas antes de mirar, barra a barra y sin retroceder —porque un ojo que ha visto el desenlace no puede dejar de verlo— y cada operación registrada en R.»
  - S080 [47w] «El tamaño de la muestra es lo difícil: una moneda justa da doce aciertos de veinte una de cada cuatro veces, así que las decenas no dicen nada y los cientos empiezan a hablar, y la banda solo se cierra con la raíz cuadrada de la muestra.»
  - S081 [43w] «El sobreajuste es el pecado capital, porque cada parámetro que añades es un grado de libertad más para que el pasado te dé la razón, y la defensa es ajustar en una mitad del histórico y probar en la mitad que no tocaste.»
- **10 Metaphor then gloss** (1)
  - S015 [«la línea de tendencia redibujada de m15-l1: una línea que se va ajustando hasta encajar encajará siempre…» analogy glossed after the colon] «Un backtest sin reglas escritas de antemano es la línea de tendencia redibujada de m15-l1: una línea que se va ajustando hasta encajar encajará siempre, y nunca te dirá nada.»
- **11 Synonym rotation** (1)
  - S010 [out-of-sample data: histórico que no usaste para inventarlas (S010), datos que no ha visto (S046), la segunda mitad, que no has mirado nunca (S051), la mitad que nunca se le dejó ver (S054), la mitad que no tocaste (S081)] 
- **A absolutes** (6)
  - S015 [siempre, nunca] «Un backtest sin reglas escritas de antemano es la línea de tendencia redibujada de m15-l1: una línea que se va ajustando hasta encajar encajará siempre, y nunca te dirá nada.»
  - S019 [siempre] «Mirar un movimiento ya terminado y preguntarse «¿yo habría entrado aquí?» no es una prueba: la respuesta es siempre que sí, y en la dirección a la que fue el movimiento.»
  - S051 [nunca] «Luego pasa las reglas terminadas y congeladas por la segunda mitad, que no has mirado nunca.»
  - S054 [nunca] «Si el sistema rinde en la mitad que nunca se le dejó ver, tienes algo de evidencia.»
  - S073 [debería] «Decide, por escrito y por adelantado, qué contaría como prueba de que el sistema está roto: un drawdown más profundo que el peor que produjo el backtest, una esperanza observada que lleva por debajo de la declarada durante una muestra suficientemente grande, una racha perdedora más larga de lo que dice la aritmética que debería ocurrir.»
  - S074 [nunca] «Que sea una desviación medida respecto a la esperanza, nunca una sensación.»

**EN** — 41 hits, 81 sentences, density 50.6

- **1 Filler** (21)
  - S003 [not in cand: «Here is the uncomfortable part.» announcer] «Here is the uncomfortable part.»
  - S005 [actually: emphatic «actually produce»] «You wrote down a win rate and an average payoff, multiplied them out and got an answer, but nobody has checked that your rules actually produce that win rate on this market.»
  - S006 [exactly: intensifier («worth exactly nothing»)] «Expectancy is a *claim*, and until it is tested it is worth exactly nothing.»
  - S011 [honest: «make it honest» applied to a test/reading] «Three conditions make it honest, and each one is there because of a specific way people fool themselves.»
  - S013 [not in cand: «quietly» tic] «If you cannot write them down, you do not have a system; you have a set of preferences that will quietly reshape themselves around whatever the chart did.»
  - S014 [not in cand: «That failure has a name in this course already.» announcer] «That failure has a name in this course already.»
  - S018 [not in cand: «This is the part everyone skips and it is the part that matters» announcer] «This is the part everyone skips and it is the part that matters, because an eye that has seen the outcome cannot unsee it.»
  - S023 [not in cand: «at all» intensifier («no edge at all»)] «Suppose your system is exactly a coin flip: 50% win rate, no edge at all.»
  - S027 [not in cand: «whatsoever» intensifier] «So a trader who runs twenty trades, sees 60% winners and concludes "the system works" has learned nothing whatsoever about their system, and a trader who sees 35% and throws the system away has done the same thing in the other direction.»
  - S031 [not in cand: «at all» intensifier («no edge at all»)] «At twenty trades the answer is "anything between 28% and 72%", which means an observed 65% is completely compatible with having no edge at all.»
  - S033 [honest: «The honest rule of thumb» applied to a rule] «**The honest rule of thumb: dozens say nothing, hundreds begin to speak.**»
  - S034 [not in cand: «And note what this does…» announcer] «And note what this does to m25's arithmetic.»
  - S045 [not in cand: «at all» intensifier («no predictive content at all»)] «A rule with enough knobs can describe *any* history perfectly, including one generated by dice — and a description of the past has no predictive content at all.»
  - S046 [not in cand: «The tell is easy to state and hard to accept:» announcer] «The tell is easy to state and hard to accept: the more finely a system fits the data it was built on, the less it usually survives contact with data it has not seen.»
  - S047 [not in cand: «The defence is one of the simplest ideas in statistics, and it needs no vocabulary:» announcer] «The defence is one of the simplest ideas in statistics, and it needs no vocabulary:»
  - S061 [not in cand: «This is the one people underestimate.» announcer] «This is the one people underestimate.»
  - S064 [actually: emphatic «if you actually run it»] «The system's expectancy is only the system's if you actually run it.»
  - S065 [honest: «honest limitation» applied to a limit] «Demo has its own honest limitation: it costs you nothing, so it does not test the psychology.»
  - S066 [precisely: intensifier] «That is precisely why m27-l2 goes to *minimum real size* rather than staying on demo — the smallest sum that still stings is the cheapest way to find out what you do under pressure.»
  - S067 [not in cand: «This is the hardest judgement in trading, and it is hard for a specific, structural reason:» announcer] «This is the hardest judgement in trading, and it is hard for a specific, structural reason:»
  - S079 [honest: «a backtest is honest» applied to a test/reading] «Expectancy was an assumption until something tested it, and a backtest is honest only under three conditions: the rules written down before you look, bar by bar with no scrolling back — because an eye that has seen the outcome cannot unsee it — and every trade logged in R.»
- **4 Summary/uplift closer** (5)
  - S006 [restate: S004 already said the number was an assumption] «Expectancy is a *claim*, and until it is tested it is worth exactly nothing.»
  - S009 [editorial: «It charges by the trade.» witty tag on S008] «It charges by the trade.»
  - S011 [ahead: announces the three conditions that follow] «Three conditions make it honest, and each one is there because of a specific way people fool themselves.»
  - S016 [restate: «So will a rule.» repeats S015] «So will a rule.»
  - S022 [editorial: «a sample you did not record is not a sample»] «A backtest is a journal of trades that did not cost anything, and it is read the same way — you are building the *sample* the next section is about, and a sample you did not record is not a sample.»
- **5 Sentence over 30 words** (13)
  - S005 [32w] «You wrote down a win rate and an average payoff, multiplied them out and got an answer, but nobody has checked that your rules actually produce that win rate on this market.»
  - S022 [40w] «A backtest is a journal of trades that did not cost anything, and it is read the same way — you are building the *sample* the next section is about, and a sample you did not record is not a sample.»
  - S027 [42w] «So a trader who runs twenty trades, sees 60% winners and concludes "the system works" has learned nothing whatsoever about their system, and a trader who sees 35% and throws the system away has done the same thing in the other direction.»
  - S035 [44w] «Expectancy is win rate times average win minus loss rate times average loss, so an error band of ±11 points on the win rate is an error band on the expectancy too — one wide enough, at twenty trades, to contain both "profitable" and "bleeding".»
  - S046 [34w] «The tell is easy to state and hard to accept: the more finely a system fits the data it was built on, the less it usually survives contact with data it has not seen.»
  - S055 [40w] «If it only works on the half it was fitted to, it is not a system, it is a description — and the discipline is to say so and start again, not to go back and tune the second half too.»
  - S059 [31w **aside-only** (30w without asides)] «Your stop-limit does not fill (m24); you cross a wider spread than the backtest assumed; slippage on the entry eats a fifth of the edge; funding accumulates on the swing holds.»
  - S066 [33w] «That is precisely why m27-l2 goes to *minimum real size* rather than staying on demo — the smallest sum that still stings is the cheapest way to find out what you do under pressure.»
  - S073 [50w] «Decide, in writing and in advance, what would count as evidence that the system is broken — a drawdown deeper than the worst the backtest produced, an observed expectancy that has sat below its claimed value for a large enough sample, a losing streak longer than the arithmetic says should happen.»
  - S076 [34w] «"I cannot take this any more" is a state of mind, and the whole point of writing the rule down beforehand is that it is decided by someone who is not in that state.»
  - S079 [48w] «Expectancy was an assumption until something tested it, and a backtest is honest only under three conditions: the rules written down before you look, bar by bar with no scrolling back — because an eye that has seen the outcome cannot unsee it — and every trade logged in R.»
  - S080 [38w] «Sample size is the hard part: a fair coin gives twelve wins in twenty one time in four, so dozens say nothing and hundreds begin to speak, the band closing only with the square root of the sample.»
  - S081 [43w] «Overfitting is the cardinal sin, because every parameter you add is one more degree of freedom for the past to agree with you, and the defence is to fit on one half of the history and test on the half you never touched.»
- **10 Metaphor then gloss** (1)
  - S015 [«m15-l1's redrawn trendline: a line that gets adjusted until it fits will fit forever…» analogy glossed after the colon] «A backtest without pre-written rules is m15-l1's redrawn trendline: a line that gets adjusted until it fits will fit forever, and it will never tell you anything.»
- **11 Synonym rotation** (1)
  - S010 [out-of-sample data: price history that you did not use to invent them (S010), data it has not seen (S046), the second half, which you never looked at (S051), the half it was never allowed to see (S054), the half you never touched (S081)] 
- **A absolutes** (6)
  - S015 [never] «A backtest without pre-written rules is m15-l1's redrawn trendline: a line that gets adjusted until it fits will fit forever, and it will never tell you anything.»
  - S019 [always] «Looking at a completed move and asking "would I have taken this?" is not a test — the answer is always yes, in the direction the move went.»
  - S051 [never] «Then run the finished, frozen rules over the second half, which you never looked at.»
  - S054 [never] «If the system performs on the half it was never allowed to see, you have some evidence.»
  - S074 [never] «Make it a measured deviation from expectancy, never a feeling.»
  - S081 [never, summary] «Overfitting is the cardinal sin, because every parameter you add is one more degree of freedom for the past to agree with you, and the defence is to fit on one half of the history and test on the half you never touched.»

### m29-l1

**ES** — 28 hits, 78 sentences, density 35.9

- **1 Filler** (9)
  - S011 [extra: justo (emphatic, = exactly)] «Esa compresión es lo que hace legibles los gráficos, pero parte de lo que tira es justo lo que querías.»
  - S019 [precisamente: emphatic, no identity pinned] «Cuando una vela se lee de forma ambigua —volumen alto con un rango minúsculo, un mínimo nuevo que se niega a tener continuidad— la ambigüedad está muy a menudo precisamente donde estaba el detalle descartado.»
  - S031 [extra: "Una nota de terminología, porque hace tropezar a mucha gente" announcer] «Una nota de terminología, porque hace tropezar a mucha gente: "volumen de compra taker" significa que el taker era el comprador, que alguien barrió la oferta.»
  - S046 [Fíjate: announcer] «Fíjate ahora en lo que puedes decir y no podías decir solo con la barra de volumen: no únicamente que la hora fue movida, sino que la impaciencia que hubo en ella se inclinaba hacia un lado.»
  - S047 [de verdad: emphatic; the contrast is carried by "no un indicador derivado"] «El delta son datos reportados de verdad, no un indicador derivado, pero es *específico de cada exchange* y su calidad varía.»
  - S063 [claramente: "merece decirse claramente" announcer] «Ese reparto es deliberado y merece decirse claramente: un ejercicio honesto necesita datos que este curso pueda generar de forma creíble.»
  - S063 [honesto: applied to an exercise] «Ese reparto es deliberado y merece decirse claramente: un ejercicio honesto necesita datos que este curso pueda generar de forma creíble.»
  - S065 [extra: "como es debido"] «Donde ocurre eso, la lección explica el concepto como es debido y nombra las herramientas reales en lugar de fingir.»
  - S071 [de verdad: "si lo fue" says it already] «El flujo de órdenes es donde compruebas si lo fue de verdad.»
- **2 Rhythmic triad** (1)
  - S025 [agresor / lado impaciente / el que eligió operar ahora — same idea three times; drop "el lado impaciente"] «El taker es el agresor: el lado impaciente, el que eligió operar *ahora* en vez de esperar un precio mejor.»
- **4 Summary/uplift closer** (5)
  - S017 [restate: S016 already says they print the same candle] «Ninguna aritmética sobre el OHLCV puede separarlas, porque la diferencia nunca estuvo en los cinco números.»
  - S042 [restate: S041-S042 pair restates S038 after the examples] «El delta responde *qué lado estaba presionando, y cuánto*.»
  - S046 [editorial: comments on what the worked example showed] «Fíjate ahora en lo que puedes decir y no podías decir solo con la barra de volumen: no únicamente que la hora fue movida, sino que la impaciencia que hubo en ella se inclinaba hacia un lado.»
  - S065 [editorial: course policy restating S063] «Donde ocurre eso, la lección explica el concepto como es debido y nombra las herramientas reales en lugar de fingir.»
  - S075 [editorial: last prose sentence, lens-wordplay closer] «No es una lente que deje de equivocarse.»
- **5 Sentence over 30 words** (8)
  - S019 [35w **aside-only** (20w without asides)] «Cuando una vela se lee de forma ambigua —volumen alto con un rango minúsculo, un mínimo nuevo que se niega a tener continuidad— la ambigüedad está muy a menudo precisamente donde estaba el detalle descartado.»
  - S027 [37w] «El volumen cuenta por igual los dos lados de cada operación: eso era lo de m14, que una operación siempre tiene comprador y vendedor, así que el volumen nunca puede ser alcista ni bajista por sí solo.»
  - S046 [37w] «Fíjate ahora en lo que puedes decir y no podías decir solo con la barra de volumen: no únicamente que la hora fue movida, sino que la impaciencia que hubo en ella se inclinaba hacia un lado.»
  - S049 [31w] «En otros exchanges se *estima*, clásicamente con la "regla del tick": suponer que una operación impresa al precio de venta fue compra taker y una al de compra fue venta taker.»
  - S064 [50w] «Una escalera de profundidad y un gráfico de footprint son una *forma* de datos distinta de cualquier serie temporal de aquí —una instantánea de un libro, una distribución dentro de una sola barra— y falsificarlas te enseñaría a leer una imagen que no es la que muestran las herramientas reales.»
  - S076 [32w] «Todo lo anterior salía de los cinco números que guarda una vela y de las cuarenta mil operaciones que descarta: dos horas opuestas, una distribuyendo y otra absorbiendo, dibujan la misma vela.»
  - S077 [52w] «El flujo de órdenes es el dato que las separa: un maker ofrece un precio y espera, un taker lo acepta y es el agresor, y el delta es el volumen de compra taker menos el de venta taker, así que el volumen responde cuántos aparecieron y el delta qué lado presionaba.»
  - S078 [39w] «Lee el delta como presión y nunca como dirección: el agresor es a menudo la orden minorista, los stops que saltan o las liquidaciones, mientras que el maker paciente que absorbe es el tamaño que sabe lo que hace.»
- **9 Course-coined term** (4)
  - S070 [non-seed estocada (bajo el soporte) for a spring's break below support] «El spring de m09 y su test —una estocada bajo el soporte que se recupera— es la historia de una venta que fue absorbida.»
  - S072 [non-seed "una capa más cerca de las operaciones"] «La divergencia de m12 —el precio hace un extremo nuevo, el momentum se niega a confirmarlo— es un patrón en un oscilador calculado a partir del precio. m30 aplica la lógica idéntica una capa más cerca de las operaciones.»
  - S074 [lente [seed]] «El flujo de órdenes es otra lente, y buena.»
  - S075 [lente [seed]] «No es una lente que deje de equivocarse.»
- **11 Synonym rotation** (1)
  - S007 [aggressive side: bando impaciente (S007), lado impaciente (S014), agresor (S025), taker (S023)] 
- **A absolutes** (3)
  - S017 [nunca] «Ninguna aritmética sobre el OHLCV puede separarlas, porque la diferencia nunca estuvo en los cinco números.»
  - S027 [siempre, nunca] «El volumen cuenta por igual los dos lados de cada operación: eso era lo de m14, que una operación siempre tiene comprador y vendedor, así que el volumen nunca puede ser alcista ni bajista por sí solo.»
  - S078 [nunca, summary] «Lee el delta como presión y nunca como dirección: el agresor es a menudo la orden minorista, los stops que saltan o las liquidaciones, mientras que el maker paciente que absorbe es el tamaño que sabe lo que hace.»

**EN** — 26 hits, 78 sentences, density 33.3

- **1 Filler** (10)
  - S011 [exactly: emphatic] «That compression is what makes charts readable — but some of what it throws away is exactly what you wanted.»
  - S019 [precisely: emphatic] «When a candle reads ambiguously — heavy volume with a tiny range, a new low that refuses to follow through — the ambiguity is very often precisely where the discarded detail was.»
  - S031 [extra: "One terminology note, because it trips people up" announcer] «One terminology note, because it trips people up: "taker buy volume" means the taker was the buyer — someone lifted the offer.»
  - S046 [extra: "Now notice" announcer] «Now notice what you can say that you could not say from the volume bar alone: not just that the hour was busy, but that the impatience in it leaned one way.»
  - S047 [extra: "real" emphatic; contrast carried by "not a derived indicator"] «Delta is real reported data, not a derived indicator — but it is *venue-specific*, and its quality varies.»
  - S063 [honest: applied to an exercise] «That split is deliberate and worth stating plainly: an honest exercise needs data this course can actually generate credibly.»
  - S063 [actually: emphatic] «That split is deliberate and worth stating plainly: an honest exercise needs data this course can actually generate credibly.»
  - S063 [extra: "worth stating plainly" announcer] «That split is deliberate and worth stating plainly: an honest exercise needs data this course can actually generate credibly.»
  - S065 [extra: "properly"] «Where that is the case, the lesson explains the concept properly and names the real tools instead of pretending.»
  - S071 [actually: "whether it was" says it] «Order flow is where you check whether it actually was.»
- **2 Rhythmic triad** (1)
  - S025 [aggressor / the impatient side / the one who chose to trade now — drop "the impatient side"] «The taker is the aggressor: the impatient side, the one who chose to trade *now* instead of waiting for a better price.»
- **4 Summary/uplift closer** (5)
  - S017 [restate] «No arithmetic on OHLCV can separate them, because the difference was never in the five numbers.»
  - S042 [restate] «Delta answers *which side was pressing, and by how much*.»
  - S046 [editorial] «Now notice what you can say that you could not say from the volume bar alone: not just that the hour was busy, but that the impatience in it leaned one way.»
  - S065 [editorial] «Where that is the case, the lesson explains the concept properly and names the real tools instead of pretending.»
  - S075 [editorial: last prose sentence] «It is not a lens that stops being wrong.»
- **5 Sentence over 30 words** (4)
  - S046 [32w] «Now notice what you can say that you could not say from the volume bar alone: not just that the hour was busy, but that the impatience in it leaned one way.»
  - S064 [47w] «A depth ladder and a footprint chart are a different *shape* of data from every time series here — an instant snapshot of a book, a distribution inside a single bar — and faking them would teach you to read a picture that isn't the one real tools show.»
  - S077 [47w] «Order flow is the data that separates them: a maker offers a price and rests, a taker accepts it and is the aggressor, and delta is taker buy volume minus taker sell volume, so volume answers how many showed up while delta answers which side was pressing.»
  - S078 [36w] «Read delta as pressure and never as direction — the aggressor is often the retail order, the stop firing or the liquidation, while the patient maker absorbing it is the size that knows what it is doing.»
- **7 No solo / not only** (1)
  - S046 «Now notice what you can say that you could not say from the volume bar alone: not just that the hour was busy, but that the impatience in it leaned one way.»
- **9 Course-coined term** (4)
  - S070 [non-seed "stab below support"] «m09's spring and its test — a stab below support that recovers — is the story of selling being absorbed.»
  - S072 [non-seed "one layer closer to the trades"] «m12's divergence — price makes a new extreme, momentum refuses to confirm — is a pattern in an oscillator computed from price. m30 runs the identical logic one layer closer to the trades.»
  - S074 [lens [seed]] «Order flow is another lens, and a good one.»
  - S075 [lens [seed]] «It is not a lens that stops being wrong.»
- **11 Synonym rotation** (1)
  - S007 [aggressive side: impatient one (S007), impatient side (S014), aggressor (S025), taker (S023)] 
- **A absolutes** (3)
  - S017 [never] «No arithmetic on OHLCV can separate them, because the difference was never in the five numbers.»
  - S027 [always, never] «Volume counts both sides of every trade equally — m14's point that a trade always has a buyer and a seller, so volume can never be bullish or bearish by itself.»
  - S078 [never, summary] «Read delta as pressure and never as direction — the aggressor is often the retail order, the stop firing or the liquidation, while the patient maker absorbing it is the size that knows what it is doing.»

### m30-l1

**ES** — 36 hits, 74 sentences, density 48.6

- **1 Filler** (10)
  - S016 [Fíjate en: announcer] «Fíjate en las horas 2 y 4: el delta se puso claramente negativo y el CVD no se volvió negativo; retrocedió hacia donde había empezado.»
  - S016 [claramente: degree adverb adds nothing] «Fíjate en las horas 2 y 4: el delta se puso claramente negativo y el CVD no se volvió negativo; retrocedió hacia donde había empezado.»
  - S036 [de verdad: emphatic] «Con el CVD puedes mirar: si el precio está plano o cayendo mientras el CVD sube de forma sostenida, es que los compradores agresivos están presionando de verdad, y que el precio no se mueva significa que hay algo ahí tomando el otro lado de todo eso.»
  - S051 [exactamente: emphatic] «La figura muestra exactamente esa forma y, después, lo que vino detrás.»
  - S053 [fíjate en: announcer] «La resolución de la derecha es lo que suele seguir a una divergencia así, y fíjate en la palabra honesta: *suele*.»
  - S053 [honesta: applied to a word] «La resolución de la derecha es lo que suele seguir a una divergencia así, y fíjate en la palabra honesta: *suele*.»
  - S061 [extra: justo (emphatic)] «Es el más común de los tres casos, y llamarlo divergencia porque querías una es justo el error que los ejercicios de esta lección están construidos para quitarte.»
  - S062 [honesto: applied to a problem] «m09 te dejó un problema concreto y honesto.»
  - S073 [de verdad: emphatic] «Mejora la absorción de m14 de inferencia a lectura: un precio plano o cayendo mientras el CVD sube significa que los compradores agresivos presionan de verdad y que algo está tomando el otro lado de todo eso.»
  - S074 [simplemente] «Una divergencia de CVD es la lógica de m12 una capa más cerca de las operaciones —el precio hace un mínimo más bajo y el CVD uno más alto— y se adelanta porque la agresión se gasta antes de que el precio se mueva; el tercer caso, en el que el CVD simplemente coincide, es el más común, y llamarlo divergencia porque querías una es el error que hay que quitarse.»
- **2 Rhythmic triad** (2)
  - S022 [tiene tendencia / hace máximos más altos y mínimos más bajos / se consolida — first two overlap; drop "tiene tendencia"] «La línea se parece a una serie de precio y se comporta como ella: tiene tendencia, hace máximos más altos y mínimos más bajos, se consolida.»
  - S060 [presionaron / nadie se puso en medio / fue donde lo mandó la presión — third restates first; drop it] «Es una caída directa y respaldada por el flujo: los vendedores presionaron, nadie relevante se puso en medio y el precio fue donde lo mandó la presión.»
- **4 Summary/uplift closer** (8)
  - S005 [ahead: announces the lesson's destination] «Es el instrumento de flujo de órdenes más útil para quien lee gráficos, y esta lección tiene un único destino: usarlo para ver la absorción directamente, en lugar de deducirla de una barra de volumen gorda y confiar.»
  - S017 [restate: aphorism summing up the hour table] «El delta es el flujo de la hora; el CVD es la posición de la sesión.»
  - S021 [editorial: "es toda la técnica"] «Comparar dónde está ahora con dónde estaba en el último swing es toda la técnica.»
  - S037 [restate] «El mismo suceso, con la suposición de m14 convertida en lectura.»
  - S050 [restate: S048-S049 already say it] «Alguien estaba comprando todo lo que vendían.»
  - S053 [editorial: comments on the word "suele"] «La resolución de la derecha es lo que suele seguir a una divergencia así, y fíjate en la palabra honesta: *suele*.»
  - S069 [restate: punchline after S066-S068] «El flujo no.»
  - S071 [editorial: last prose sentence] «Pero es una respuesta bastante mejor que "espera a ver si aguanta".»
- **5 Sentence over 30 words** (10)
  - S005 [38w] «Es el instrumento de flujo de órdenes más útil para quien lee gráficos, y esta lección tiene un único destino: usarlo para ver la absorción directamente, en lugar de deducirla de una barra de volumen gorda y confiar.»
  - S006 [39w **aside-only** (30w without asides)] «Coge el delta de cada periodo —volumen de compra taker menos volumen de venta taker— y ve manteniendo una suma corriente desde algún punto de partida, normalmente el principio de una sesión o de la ventana que estás mirando.»
  - S034 [31w] «En m14, la absorción era una inferencia fuerte: una barra de volumen enorme casi sin rango de precio, así que *presumiblemente* alguien grande se estaba tragando todo lo que le lanzaban.»
  - S036 [47w] «Con el CVD puedes mirar: si el precio está plano o cayendo mientras el CVD sube de forma sostenida, es que los compradores agresivos están presionando de verdad, y que el precio no se mueva significa que hay algo ahí tomando el otro lado de todo eso.»
  - S048 [38w] «Pero el CVD en ese segundo mínimo marca −4.800: a lo largo de todo ese segundo tramo, la compra agresiva fue lo bastante positiva en neto para levantar el total corriente en 14.000 mientras el precio caía 900.»
  - S057 [33w] «Es la misma razón por la que se adelanta la divergencia de momentum de m12, pero una capa más cerca de las operaciones y medida en vez de calculada a partir del precio.»
  - S063 [39w] «Un spring es una estocada bajo el soporte que se recupera, y solo puedes etiquetarla como spring *después* de que el precio vuelva adentro: en vivo, esa misma mecha es indistinguible del comienzo de una ruptura bajista de verdad.»
  - S066 [47w] «En un spring real, la estocada bajo el soporte es venta siendo absorbida, así que el CVD debería mostrarlo: el precio se lleva el mínimo, el CVD se niega a hacer un mínimo nuevo correspondiente y, en el test, el precio aguanta mientras el flujo sigue sostenido.»
  - S073 [37w] «Mejora la absorción de m14 de inferencia a lectura: un precio plano o cayendo mientras el CVD sube significa que los compradores agresivos presionan de verdad y que algo está tomando el otro lado de todo eso.»
  - S074 [71w] «Una divergencia de CVD es la lógica de m12 una capa más cerca de las operaciones —el precio hace un mínimo más bajo y el CVD uno más alto— y se adelanta porque la agresión se gasta antes de que el precio se mueva; el tercer caso, en el que el CVD simplemente coincide, es el más común, y llamarlo divergencia porque querías una es el error que hay que quitarse.»
- **9 Course-coined term** (5)
  - S057 [non-seed "una capa más cerca de las operaciones"] «Es la misma razón por la que se adelanta la divergencia de momentum de m12, pero una capa más cerca de las operaciones y medida en vez de calculada a partir del precio.»
  - S063 [non-seed estocada] «Un spring es una estocada bajo el soporte que se recupera, y solo puedes etiquetarla como spring *después* de que el precio vuelva adentro: en vivo, esa misma mecha es indistinguible del comienzo de una ruptura bajista de verdad.»
  - S066 [non-seed estocada] «En un spring real, la estocada bajo el soporte es venta siendo absorbida, así que el CVD debería mostrarlo: el precio se lleva el mínimo, el CVD se niega a hacer un mínimo nuevo correspondiente y, en el test, el precio aguanta mientras el flujo sigue sostenido.»
  - S070 [lente [seed]] «Esto no vuelve seguro el spring: es confluencia (m14), una lente independiente más que coincide.»
  - S074 [non-seed "una capa más cerca de las operaciones"] «Una divergencia de CVD es la lógica de m12 una capa más cerca de las operaciones —el precio hace un mínimo más bajo y el CVD uno más alto— y se adelanta porque la agresión se gasta antes de que el precio se mueva; el tercer caso, en el que el CVD simplemente coincide, es el más común, y llamarlo divergencia porque querías una es el error que hay que quitarse.»
- **11 Synonym rotation** (1)
  - S033 [absorption: absorción (S033), tragándose (S034), se la comieron (S040), tomando el otro lado (S036)] 
- **A absolutes** (1)
  - S066 [debería] «En un spring real, la estocada bajo el soporte es venta siendo absorbida, así que el CVD debería mostrarlo: el precio se lleva el mínimo, el CVD se niega a hacer un mínimo nuevo correspondiente y, en el test, el precio aguanta mientras el flujo sigue sostenido.»

**EN** — 35 hits, 74 sentences, density 47.3

- **1 Filler** (10)
  - S003 [exactly: emphatic] «What makes delta a tool you can read is accumulating it, exactly as a running bank balance tells you more than any single transaction.»
  - S005 [extra: "single most useful" intensifier] «It is the single most useful order-flow instrument for a chart reader, and this lesson has one destination: using it to see absorption directly, instead of inferring absorption from a fat volume bar and hoping.»
  - S016 [extra: "Notice" announcer] «Notice hours 2 and 4: the delta went sharply negative, and the CVD did not become negative — it fell back toward where it had started.»
  - S036 [really: emphatic] «With CVD you can look: if price is flat or falling while CVD climbs steadily, aggressive buyers really are pressing, and the fact that price is not moving means something is standing there taking the other side of all of it.»
  - S051 [exactly: emphatic] «The figure shows exactly that shape, and then what followed it.»
  - S053 [honest: applied to a word] «The resolution on the right is what a divergence like this often precedes, and note the honest word: *often*.»
  - S053 [extra: "note the honest word" announcer] «The resolution on the right is what a divergence like this often precedes, and note the honest word: *often*.»
  - S062 [honest: applied to a problem] «m09 left you with a specific, honest problem.»
  - S073 [really: emphatic] «It upgrades m14's absorption from an inference to a reading: price flat or falling while CVD climbs means aggressive buyers really are pressing and something is taking the other side of all of it.»
  - S074 [simply] «A CVD divergence is m12's logic one layer closer to the trades — price makes a lower low while CVD makes a higher low — and it leads because aggression is spent before price moves; the third case, where CVD simply agrees, is the most common and calling it a divergence because you wanted one is the error to train out.»
- **2 Rhythmic triad** (2)
  - S022 [it trends / higher highs and lower lows / it consolidates — drop "it trends"] «The line looks and behaves like a price series — it trends, it makes higher highs and lower lows, it consolidates.»
  - S060 [sellers pressed / nobody stood in the way / price went where the pressure sent it — drop third] «That is a straightforward, flow-backed move down: sellers pressed, nobody meaningful stood in the way, and price went where the pressure sent it.»
- **4 Summary/uplift closer** (8)
  - S005 [ahead] «It is the single most useful order-flow instrument for a chart reader, and this lesson has one destination: using it to see absorption directly, instead of inferring absorption from a fat volume bar and hoping.»
  - S017 [restate] «The delta is the hour's flow; the CVD is the position of the session.»
  - S021 [editorial: "is the whole technique"] «Comparing where it is now against where it was at the last swing is the whole technique.»
  - S037 [restate] «Same event, m14's guess turned into a reading.»
  - S050 [restate] «Someone was buying everything they sold.»
  - S053 [editorial] «The resolution on the right is what a divergence like this often precedes, and note the honest word: *often*.»
  - S069 [restate] «The flow does not.»
  - S071 [editorial: last prose sentence] «But it is a considerably better answer than "wait and see whether it holds."»
- **5 Sentence over 30 words** (9)
  - S005 [35w] «It is the single most useful order-flow instrument for a chart reader, and this lesson has one destination: using it to see absorption directly, instead of inferring absorption from a fat volume bar and hoping.»
  - S006 [33w **aside-only** (26w without asides)] «Take each period's delta — taker buy volume minus taker sell volume — and keep a running sum from some starting point, usually the beginning of a session or of the window you're looking at.»
  - S036 [41w] «With CVD you can look: if price is flat or falling while CVD climbs steadily, aggressive buyers really are pressing, and the fact that price is not moving means something is standing there taking the other side of all of it.»
  - S048 [31w] «But the CVD at that second low reads −4,800: over that whole second leg, aggressive buying was net *positive* enough to lift the running total by 14,000 while price fell 900.»
  - S061 [33w] «It is the most common of the three cases, and calling it a divergence because you wanted one is the error the exercises in this lesson are built to train out of you.»
  - S063 [35w] «A spring is a stab below support that recovers, and you can only label it a spring *after* price comes back inside — live, that same wick is indistinguishable from the start of a genuine breakdown.»
  - S066 [44w] «On a real spring the stab below support is selling being absorbed, so the CVD should show it: price takes out the low, the CVD refuses to make a corresponding new low, and on the test the price holds while the flow stays supported.»
  - S073 [34w] «It upgrades m14's absorption from an inference to a reading: price flat or falling while CVD climbs means aggressive buyers really are pressing and something is taking the other side of all of it.»
  - S074 [59w] «A CVD divergence is m12's logic one layer closer to the trades — price makes a lower low while CVD makes a higher low — and it leads because aggression is spent before price moves; the third case, where CVD simply agrees, is the most common and calling it a divergence because you wanted one is the error to train out.»
- **9 Course-coined term** (5)
  - S057 [non-seed "one layer closer to the trades"] «That is the same reason m12's momentum divergence leads — but one layer closer to the trades, and measured rather than computed from price.»
  - S063 [non-seed stab] «A spring is a stab below support that recovers, and you can only label it a spring *after* price comes back inside — live, that same wick is indistinguishable from the start of a genuine breakdown.»
  - S066 [non-seed stab] «On a real spring the stab below support is selling being absorbed, so the CVD should show it: price takes out the low, the CVD refuses to make a corresponding new low, and on the test the price holds while the flow stays supported.»
  - S070 [lens [seed]] «This does not make the spring certain — it is confluence (m14), one more independent lens agreeing.»
  - S074 [non-seed "one layer closer to the trades"] «A CVD divergence is m12's logic one layer closer to the trades — price makes a lower low while CVD makes a higher low — and it leads because aggression is spent before price moves; the third case, where CVD simply agrees, is the most common and calling it a divergence because you wanted one is the error to train out.»
- **11 Synonym rotation** (1)
  - S033 [absorption: absorption (S033), soaking up (S034), eaten (S040), taking the other side (S036)] 
- **A absolutes** (1)
  - S055 [must] «To make a new low, sellers must overcome resting bids; if the bids keep absorbing, the sellers exhaust themselves at a price that barely improves.»

### m31-l1

**ES** — 41 hits, 70 sentences, density 58.6

- **1 Filler** (11)
  - S003 [extra: "en serio"] «Ahora merece leerse en serio, porque el libro es donde vive físicamente la absorción del módulo anterior.»
  - S004 [extra: "Una cosa que conviene dejar clara antes de nada" announcer] «Una cosa que conviene dejar clara antes de nada: esta lección es conceptual.»
  - S013 [extra: "absolutamente" intensifier] «Un libro es una fotografía de la intención en el presente, y no tiene absolutamente nada de historia dentro.»
  - S023 [realmente: emphatic] «La misma orden, el mismo precio nominal en pantalla, un resultado muy distinto; y por esto la liquidez, y no solo el precio, decide lo que realmente te cuesta una operación.»
  - S026 [extra: justo] «Los traders vigilan los muros justo por eso, y a menudo el precio sí se atasca en uno.»
  - S032 [honesta: applied to a reading] «La lectura honesta es más cuidadosa.»
  - S050 [honestamente] «Este curso no puede mostrarte un libro en vivo, así que esto es honestamente lo que sí:»
  - S062 [extra: justo] «Los muros se retiran, y se retiran justo cuando iban a ser testeados.»
  - S066 [extra: "en absoluto" intensifier] «Todo lo que está ahí en reposo es revocable, y buena parte de lo que importa (icebergs, órdenes que los algoritmos mantienen fuera de pantalla) no está en el libro en absoluto.»
  - S069 [de verdad: emphatic] «La profundidad decide lo que de verdad te cuesta una operación por el slippage, un muro es una orden en reposo llamativamente grande que actúa como suelo solo mientras está ahí —se cancela en un milisegundo, y el spoofing es exactamente eso— y el desequilibrio es una lectura de saturación, la menos sólida del bloque.»
  - S069 [exactamente: emphatic] «La profundidad decide lo que de verdad te cuesta una operación por el slippage, un muro es una orden en reposo llamativamente grande que actúa como suelo solo mientras está ahí —se cancela en un milisegundo, y el spoofing es exactamente eso— y el desequilibrio es una lectura de saturación, la menos sólida del bloque.»
- **2 Rhythmic triad** (2)
  - S038 [spread se ensancha / liquidez se evapora / primer movimiento violento — first two overlap; drop "la liquidez se evapora"] «m17 te contó lo que pasa alrededor de una publicación programada —un dato de IPC, una decisión de la Fed—: el spread se ensancha, la liquidez se evapora y el primer movimiento suele ser violento y luego se retrae por completo.»
  - S061 [suelo garantizado / apoyarse en él / mover un stop — first two overlap; drop "apoyarse en él"] «Alguna versión de esa frase es el error de libro de órdenes más común con diferencia: ver un tamaño grande en reposo por debajo y tratarlo como un suelo garantizado, apoyarse en él o, peor, mover un stop por debajo.»
- **4 Summary/uplift closer** (8)
  - S005 [ahead: "la razón se explica cerca del final"] «No hay ejercicio de gráfico al final, y eso es deliberado, no un olvido; la razón se explica cerca del final, junto con las herramientas que sí te muestran un libro de verdad.»
  - S013 [restate: S011 already says snapshot with no history] «Un libro es una fotografía de la intención en el presente, y no tiene absolutamente nada de historia dentro.»
  - S017 [restate: aphorism] «El volumen es el registro de ese consumo; el libro es el combustible que consumió.»
  - S023 [restate] «La misma orden, el mismo precio nominal en pantalla, un resultado muy distinto; y por esto la liquidez, y no solo el precio, decide lo que realmente te cuesta una operación.»
  - S035 [editorial] «Eso es una afirmación sobre la resistencia al movimiento, no una predicción.»
  - S039 [ahead] «Este módulo explica el *mecanismo* detrás de ese síntoma.»
  - S049 [restate] «El primer movimiento con frecuencia no es la opinión del mercado sobre la noticia: es un libro poco profundo siendo cruzado.»
  - S067 [ahead + motivate: last prose sentence] «Queda la publicación, donde entender el mecanismo se paga sobre todo como la disciplina de no hacer nada:»
- **5 Sentence over 30 words** (17)
  - S005 [33w] «No hay ejercicio de gráfico al final, y eso es deliberado, no un olvido; la razón se explica cerca del final, junto con las herramientas que sí te muestran un libro de verdad.»
  - S006 [37w **aside-only** (24w without asides)] «El libro de órdenes es la lista de órdenes limitadas sin ejecutar a cada precio, en los dos lados: bids (ofertas de compra, por debajo del precio actual) y asks u ofertas (ofertas de venta, por encima).»
  - S008 [31w] «El hueco entre el bid más alto y el ask más bajo es el spread, y el precio actual no es más que donde ocurrió la última operación entre los dos.»
  - S014 [31w] «Las operaciones y las órdenes en reposo se relacionan directamente: la orden a mercado de un taker se come el libro en reposo, nivel a nivel de precio, hasta quedar llena.»
  - S023 [31w] «La misma orden, el mismo precio nominal en pantalla, un resultado muy distinto; y por esto la liquidez, y no solo el precio, decide lo que realmente te cuesta una operación.»
  - S033 [48w] «Dice que ahora mismo hay más *disposición pasiva a comprar* que a vender en las cercanías, lo que significa que hará falta mucha más venta agresiva para empujar el precio hacia abajo a costa de ese bid que compra agresiva para levantarlo a costa del ask, más fino.»
  - S037 [49w] «Es además la lectura menos sólida de este bloque, por tres razones: las órdenes se pueden cancelar, los participantes más grandes deliberadamente no muestran su tamaño, y el desequilibrio que estás mirando bien puede ser una consecuencia del movimiento que ya ocurrió en lugar de una causa del siguiente.»
  - S038 [41w] «m17 te contó lo que pasa alrededor de una publicación programada —un dato de IPC, una decisión de la Fed—: el spread se ensancha, la liquidez se evapora y el primer movimiento suele ser violento y luego se retrae por completo.»
  - S044 [36w] «Así que en los segundos anteriores a la publicación el libro *se adelgaza drásticamente* y el spread se ensancha, no porque nadie se haya vuelto bajista, sino porque quienes normalmente aportan profundidad se han echado atrás.»
  - S052 [32w] «Un heatmap del libro de órdenes, que dibuja la profundidad en reposo a lo largo del *tiempo* como intensidad de color, así que puedes ver los muros aparecer, persistir y ser retirados.»
  - S056 [32w] «Por qué aquí no hay ejercicio: una escalera de profundidad es esa instantánea inmediata indexada por precio que se describía arriba, y todos los gráficos que genera este curso son series temporales.»
  - S061 [40w] «Alguna versión de esa frase es el error de libro de órdenes más común con diferencia: ver un tamaño grande en reposo por debajo y tratarlo como un suelo garantizado, apoyarse en él o, peor, mover un stop por debajo.»
  - S065 [32w] «La profundidad te dice lo que cuesta ahora mover el precio, no hacia dónde va: un lado ask fino significa que subir es barato *hoy*, no que la subida vaya a venir.»
  - S066 [32w **aside-only** (23w without asides)] «Todo lo que está ahí en reposo es revocable, y buena parte de lo que importa (icebergs, órdenes que los algoritmos mantienen fuera de pantalla) no está en el libro en absoluto.»
  - S068 [39w] «El libro de órdenes es la otra mitad del mercado: no operaciones que ocurrieron sino órdenes limitadas en reposo esperando y, a diferencia de todo lo demás en este curso, es una instantánea inmediata sin nada de historia dentro.»
  - S069 [55w] «La profundidad decide lo que de verdad te cuesta una operación por el slippage, un muro es una orden en reposo llamativamente grande que actúa como suelo solo mientras está ahí —se cancela en un milisegundo, y el spoofing es exactamente eso— y el desequilibrio es una lectura de saturación, la menos sólida del bloque.»
  - S070 [40w] «También explica la publicación programada de m17: los creadores de mercado retiran sus cotizaciones ante un evento con hora fijada, así que la primera vela violenta es un libro poco profundo siendo cruzado y no una opinión sobre la noticia.»
- **9 Course-coined term** (1)
  - S017 [combustible [seed]] «El volumen es el registro de ese consumo; el libro es el combustible que consumió.»
- **10 Metaphor then gloss** (1)
  - S025 ["actúa como un suelo" then glossed: los vendedores tienen que masticar 400 BTC] «Mientras está ahí actúa como un suelo: los vendedores tienen que masticar 400 BTC antes de que el precio pueda bajar.»
- **11 Synonym rotation** (1)
  - S019 [thin book: poco profundo (S019), fino (S033), se adelgaza (S044)] 
- **A absolutes** (1)
  - S063 [nunca] «Nunca dejes que una orden en reposo que alguien puede cancelar gratis sea la razón de que tu riesgo esté donde está.»

**EN** — 36 hits, 70 sentences, density 51.4

- **1 Filler** (14)
  - S003 [extra: "properly"] «Now it is worth reading properly, because the book is where the absorption of the last module physically lives.»
  - S004 [extra: "One thing to settle before anything else" announcer] «One thing to settle before anything else: this lesson is conceptual.»
  - S008 [really] «The gap between the highest bid and the lowest ask is the spread, and the current price is really just wherever the last trade happened between them.»
  - S013 [extra: "at all"] «A book is a photograph of intention in the present, and it has no history in it at all.»
  - S023 [actually] «Same order, same nominal price on screen, very different outcome — and this is why liquidity, not just price, decides what a trade actually costs you.»
  - S026 [exactly] «Traders watch walls for exactly that reason, and often price does stall at one.»
  - S032 [honest: applied to a reading] «The honest read is more careful.»
  - S049 [extra: "at all"] «The first move frequently is not the market's opinion of the news at all — it is a thin book being crossed.»
  - S050 [honestly] «This course cannot show you a live book, so here is honestly what does:»
  - S061 [extra: "single most common"] «Some version of that sentence is the single most common order-book mistake: seeing large size resting below and treating it as a guaranteed floor, leaning on it, or worse, moving a stop under it.»
  - S062 [precisely] «Walls get pulled, and they get pulled precisely when they would have been tested.»
  - S066 [extra: "at all"] «Everything resting there is revocable, and a good deal of what matters (icebergs, orders held off-screen by algorithms) is not in the book at all.»
  - S069 [actually] «Depth decides what a trade actually costs you through slippage, a wall is a conspicuously large resting order that acts as a floor only while it is there — it can be cancelled in a millisecond, and spoofing is exactly that — and imbalance is a crowding read, the flimsiest in the block.»
  - S069 [exactly] «Depth decides what a trade actually costs you through slippage, a wall is a conspicuously large resting order that acts as a floor only while it is there — it can be cancelled in a millisecond, and spoofing is exactly that — and imbalance is a crowding read, the flimsiest in the block.»
- **2 Rhythmic triad** (2)
  - S038 [spread widens / liquidity evaporates / first move violent — drop "liquidity evaporates"] «m17 told you what happens around a scheduled release — a CPI print, an FOMC decision: the spread widens, liquidity evaporates, and the first move is often violent and then fully retraced.»
  - S061 [guaranteed floor / leaning on it / moving a stop — drop "leaning on it"] «Some version of that sentence is the single most common order-book mistake: seeing large size resting below and treating it as a guaranteed floor, leaning on it, or worse, moving a stop under it.»
- **4 Summary/uplift closer** (8)
  - S005 [ahead] «There is no chart exercise at the end of it, and that is deliberate rather than an omission — the reason is explained near the end, along with the tools that do show you a book for real.»
  - S013 [restate] «A book is a photograph of intention in the present, and it has no history in it at all.»
  - S017 [restate] «Volume is the record of that consumption; the book is the fuel it consumed.»
  - S023 [restate] «Same order, same nominal price on screen, very different outcome — and this is why liquidity, not just price, decides what a trade actually costs you.»
  - S035 [editorial] «That is a statement about resistance to movement, not a prediction.»
  - S039 [ahead] «This module explains the *mechanism* behind that symptom.»
  - S049 [restate] «The first move frequently is not the market's opinion of the news at all — it is a thin book being crossed.»
  - S067 [ahead + motivate] «Which leaves the release, where understanding the mechanism pays off mostly as the discipline to do nothing:»
- **5 Sentence over 30 words** (10)
  - S005 [37w] «There is no chart exercise at the end of it, and that is deliberate rather than an omission — the reason is explained near the end, along with the tools that do show you a book for real.»
  - S006 [33w **aside-only** (21w without asides)] «The order book is the list of unexecuted limit orders at every price, on both sides: bids (offers to buy, below the current price) and asks or offers (offers to sell, above it).»
  - S033 [40w] «It says there is currently more *passive willingness to buy* than to sell nearby — which means it will take much more aggressive selling to push price down through that bid than aggressive buying to lift it through the thinner ask.»
  - S037 [52w] «It is also the flimsiest reading in this block, for three reasons — the orders can be cancelled, the largest players deliberately do not display their size, and the imbalance you are looking at may well be a consequence of the move that already happened rather than a cause of the next one.»
  - S038 [31w] «m17 told you what happens around a scheduled release — a CPI print, an FOMC decision: the spread widens, liquidity evaporates, and the first move is often violent and then fully retraced.»
  - S057 [31w **aside-only** (12w without asides)] «Building a credible interactive book — with orders appearing, refilling, and being cancelled in real time, which is the *only* version that teaches anything true — is a different project from this one.»
  - S061 [34w] «Some version of that sentence is the single most common order-book mistake: seeing large size resting below and treating it as a guaranteed floor, leaning on it, or worse, moving a stop under it.»
  - S068 [36w] «The order book is the other half of the market: not trades that happened but resting limit orders waiting, and unlike everything else in this course it is an instantaneous snapshot with no history in it.»
  - S069 [51w] «Depth decides what a trade actually costs you through slippage, a wall is a conspicuously large resting order that acts as a floor only while it is there — it can be cancelled in a millisecond, and spoofing is exactly that — and imbalance is a crowding read, the flimsiest in the block.»
  - S070 [34w] «It also explains m17's scheduled release: market makers pull their quotes ahead of a timed event, so the first violent candle is a thin book being crossed rather than an opinion about the news.»
- **9 Course-coined term** (1)
  - S017 [fuel [seed]] «Volume is the record of that consumption; the book is the fuel it consumed.»
- **10 Metaphor then gloss** (1)
  - S025 ["acts as a floor" then glossed: sellers must chew through 400 BTC] «While it sits there it acts as a floor: sellers must chew through 400 BTC before price can go lower.»
- **A absolutes** (2)
  - S025 [must] «While it sits there it acts as a floor: sellers must chew through 400 BTC before price can go lower.»
  - S063 [never] «Never let a resting order that someone can cancel for free be the reason your risk sits where it does.»

### m32-l1

**ES** — 22 hits, 53 sentences, density 41.5

- **1 Filler** (5)
  - S031 [extra: "Y ojo:" announcer] «Y ojo: el mismo exchange puede mostrar las dos a la vez —una prima estructural de fricción con picos de demanda encima—, y por eso lo que importa es el *cambio* de la prima, no su nivel.»
  - S033 [extra: genuinamente] «Si ese exchange representa una bolsa de capital distinta, eso es información genuinamente temprana: el flujo tiene que aparecer en algún lado antes de aparecer en todos.»
  - S043 [simplemente] «Eso pone un suelo: por debajo del coste aproximado de la ida y vuelta, ninguna prima merece arbitrarse, así que las primas pequeñas simplemente persisten.»
  - S047 [honesto: applied to a picture/reading] «Así que el cuadro honesto no es "el arbitraje elimina las primas", sino "el arbitraje las topa en el coste de hacerlo"; y donde ese coste es alto, el tope es alto.»
  - S050 [exactamente] «Puedes calcularla tú mismo con dos fuentes de precio, que es exactamente lo que hace el cálculo de abajo.»
- **2 Rhythmic triad** (1)
  - S044 [restringido / lento / topado — restricted and capped overlap; drop "restringido"] «En algunas jurisdicciones mover el tramo *fiat* está restringido, es lento o está topado.»
- **4 Summary/uplift closer** (4)
  - S018 [restate of S017] «Comparar el 1,5 % de hoy con un 1,5 % de hace dos años tiene sentido; comparar 900 con 900 no.»
  - S024 [restate] «Esta prima es *información*: te dice de dónde nace la presión compradora.»
  - S038 [editorial] «Lo saturado es frágil, aquí como en todo el resto de este curso.»
  - S050 [ahead: last prose sentence points at the calculation below] «Puedes calcularla tú mismo con dos fuentes de precio, que es exactamente lo que hace el cálculo de abajo.»
- **5 Sentence over 30 words** (12)
  - S001 [32w] «m19 te enseñó la base: el hueco entre un perpetuo y su propio precio spot, y cómo una prima sostenida se lee como un posicionamiento apalancado saturado y no como un pronóstico.»
  - S023 [37w] «Esto es lo que quiere decir la gente cuando dice que el capital está "entrando por" un exchange concreto, algo habitual cuando el flujo institucional o minorista de un país llega antes que el de los demás.»
  - S031 [37w **aside-only** (27w without asides)] «Y ojo: el mismo exchange puede mostrar las dos a la vez —una prima estructural de fricción con picos de demanda encima—, y por eso lo que importa es el *cambio* de la prima, no su nivel.»
  - S035 [31w] «Una prima que pasó semanas al 3 % y cae al 0,2 % te está diciendo que el comprador local ansioso ha terminado, o que la barrera que la sostenía acaba de abrirse.»
  - S045 [36w] «Esta es la grande: es la razón de que las primas sostenidas más famosas hayan aparecido históricamente en exchanges de países con controles de capital estrictos, y de que puedan durar meses en lugar de minutos.»
  - S046 [38w] «La versión eficiente de la operación necesita inventario en los dos exchanges a la vez, lo que significa inmovilizar capital por adelantado y aceptar el riesgo de contraparte de los dos exchanges (el "not your keys" de m02).»
  - S047 [32w] «Así que el cuadro honesto no es "el arbitraje elimina las primas", sino "el arbitraje las topa en el coste de hacerlo"; y donde ese coste es alto, el tope es alto.»
  - S048 [61w] «Varias plataformas de datos publican índices de prima entre exchanges de forma continua; el más conocido es la prima de Coinbase (BTC spot en Coinbase contra una referencia global, muy vigilada como aproximación del flujo institucional estadounidense), y la veterana prima del mercado coreano, a la que suele llamarse "prima kimchi", es el caso de manual del tipo impulsado por fricción.»
  - S049 [35w] «Esos son ejemplos de dónde se mide el concepto, no el concepto en sí, y por eso este módulo se llama *prima entre exchanges* y no lleva el nombre del índice de ningún exchange concreto.»
  - S051 [46w] «No hay un único precio de Bitcoin, solo un precio en cada exchange, y el hueco entre dos de ellos es la prima entre exchanges, que se cita como porcentaje del exchange de referencia porque 900 no significa nada hasta que sabes de qué son 900.»
  - S052 [51w] «Tiene dos causas muy distintas que conviene separar: la demanda regional que llega antes a un sitio, que sí es informativa, y la fricción para mover valor —controles de capital, vías bancarias lentas, una cola de retiros parada—, que es el precio de una barrera y no una señal de demanda.»
  - S053 [33w] «El arbitraje no elimina una prima, la topa al coste de hacerlo, así que lee el cambio y no el nivel, y trátala como lectura de flujo y nunca como señal de compra.»
- **A absolutes** (2)
  - S039 [debería] «El arbitraje que debería borrar una prima es real y está trabajando constantemente, y es lento por razones concretas que merece conocer:»
  - S053 [nunca, summary] «El arbitraje no elimina una prima, la topa al coste de hacerlo, así que lee el cambio y no el nivel, y trátala como lectura de flujo y nunca como señal de compra.»

**EN** — 19 hits, 53 sentences, density 35.8

- **1 Filler** (6)
  - S031 [extra: "Notably," announcer] «Notably, the same venue can show both at once — a structural friction premium with demand-driven spikes on top of it, which is why what matters is the premium's *change*, not its level.»
  - S033 [genuinely] «If the venue represents a distinct pool of capital, that is genuinely early information — the flow has to show up somewhere before it shows up everywhere.»
  - S043 [simply] «These set a floor: below roughly the round-trip cost, no premium is worth arbitraging, so small premiums simply persist.»
  - S047 [honest: applied to a picture/reading] «So the honest picture is not "arbitrage eliminates premiums" but "arbitrage caps them at the cost of doing it" — and where that cost is high, the cap is high.»
  - S050 [exactly] «You can compute it yourself from two price feeds, which is exactly what the calculation below does.»
  - S052 [genuinely] «It has two very different causes worth telling apart: regional demand arriving somewhere first, which is genuinely informative, and transfer friction — capital controls, slow banking, a paused withdrawal queue — which is the price of a barrier rather than a demand signal.»
- **2 Rhythmic triad** (1)
  - S044 [restricted / slow / capped — drop "restricted"] «In some jurisdictions moving the *fiat* leg is restricted, slow, or capped.»
- **4 Summary/uplift closer** (4)
  - S018 [restate] «Comparing 1.5% today with 1.5% two years ago is meaningful; comparing 900 with 900 is not.»
  - S024 [restate] «This premium is *information*: it tells you where the buying pressure originates.»
  - S038 [editorial] «Crowded is fragile, here as everywhere else in this course.»
  - S050 [ahead] «You can compute it yourself from two price feeds, which is exactly what the calculation below does.»
- **5 Sentence over 30 words** (8)
  - S031 [32w] «Notably, the same venue can show both at once — a structural friction premium with demand-driven spikes on top of it, which is why what matters is the premium's *change*, not its level.»
  - S045 [33w] «This is the big one — it is why the most famous sustained premiums have historically appeared on venues in countries with tight capital controls, and why they can last months rather than minutes.»
  - S046 [31w **aside-only** (27w without asides)] «The efficient version of the trade needs inventory on both venues simultaneously, which means tying up capital in advance and accepting the counterparty risk of both exchanges (m02's "not your keys").»
  - S048 [52w] «Several data sites publish cross-venue premium indices continuously; the best known is the Coinbase premium (spot BTC on Coinbase against a global reference, widely watched as a proxy for US institutional flow), and the long-running Korean-market premium usually referred to as the "Kimchi premium" is the textbook case of the friction-driven kind.»
  - S049 [31w] «Those are examples of where the concept is measured, not the concept itself — which is why this module is called *premium between venues* rather than named after any one exchange's index.»
  - S051 [45w] «There is no single price for Bitcoin, only a price on each venue, and the gap between two of them is the premium between venues — quoted as a percentage of the reference venue, because 900 means nothing until you know what it is 900 of.»
  - S052 [41w] «It has two very different causes worth telling apart: regional demand arriving somewhere first, which is genuinely informative, and transfer friction — capital controls, slow banking, a paused withdrawal queue — which is the price of a barrier rather than a demand signal.»
  - S053 [34w] «Arbitrage does not eliminate a premium, it caps it at the cost of doing it, so read the change rather than the level and treat it as a flow reading, never a buy signal.»
- **A absolutes** (1)
  - S053 [never, summary] «Arbitrage does not eliminate a premium, it caps it at the cost of doing it, so read the change rather than the level and treat it as a flow reading, never a buy signal.»

### m33-l1

**ES** — 33 hits, 55 sentences, density 60.0

- **1 Filler** (9)
  - S015 [Fíjate en que: announcer] «Fíjate en que esto es el delta de m29, pero resuelto por nivel de precio en vez de sumado a lo largo del periodo: la resolución más fina de todo el bloque.»
  - S018 [honesta: applied to a reason] «Esa es la razón honesta de que aquí no haya ejercicio para él: nada más en este curso produce datos de distribución-dentro-de-una-barra, y la visualización no es en absoluto una serie temporal.»
  - S018 [extra: "en absoluto" intensifier] «Esa es la razón honesta de que aquí no haya ejercicio para él: nada más en este curso produce datos de distribución-dentro-de-una-barra, y la visualización no es en absoluto una serie temporal.»
  - S026 [honestos: applied to levels] «m03 y m08 enseñaban los niveles como sitios donde el precio ha reaccionado, trazados a partir de máximos y mínimos: honestos pero a ojo, y vulnerables a la crítica de que siempre puedes encontrar una línea que encaje.»
  - S030 [exactamente: emphatic] «Te da una razón para un nivel más allá de "parece un nivel", que es exactamente lo que pedía la advertencia de m08 sobre trazar líneas que encajen con tu sesgo.»
  - S042 [extra: genuinamente] «El POC de la sesión de ayer, dibujado en el gráfico de hoy, es un nivel genuinamente útil y probarlo no te cuesta nada.»
  - S044 [extra: genuina] «El flujo de órdenes, el libro, los footprints: cada uno es una mejora genuina de resolución, y ninguno convierte una probabilidad en una garantía.»
  - S047 [extra: "Merece nombrar dos versiones concretas" announcer] «Merece nombrar dos versiones concretas, porque las dos son las herramientas de este módulo vueltas contra su dueño.»
  - S055 [de verdad: emphatic; contrast carried by "y no una línea que elegiste"] «Es una mejora sobre unos soportes y resistencias puestos a ojo, porque un nodo de volumen alto es un precio en el que muchos participantes se pusieron de acuerdo de verdad y no una línea que elegiste; la trampa es creer que un dato más fino es más certeza, y tratar el POC como un imán al que hay que llegar.»
- **2 Rhythmic triad** (1)
  - S001 [una vela por periodo / una barra de volumen por periodo / un valor de CVD por periodo — repeated frame; drop the CVD item] «Todos los gráficos de este curso ponen el tiempo en el eje horizontal: una vela por periodo, una barra de volumen por periodo, un valor de CVD por periodo.»
- **4 Summary/uplift closer** (6)
  - S004 [ahead: "La razón se explica más abajo"] «La razón se explica más abajo en lugar de dejarse como un hueco.»
  - S015 [editorial: "la resolución más fina de todo el bloque"] «Fíjate en que esto es el delta de m29, pero resuelto por nivel de precio en vez de sumado a lo largo del periodo: la resolución más fina de todo el bloque.»
  - S030 [editorial: ties back to m08's warning] «Te da una razón para un nivel más allá de "parece un nivel", que es exactamente lo que pedía la advertencia de m08 sobre trazar líneas que encajen con tu sesgo.»
  - S046 [restate: aphorism restating S043] «Resolución no es certeza.»
  - S049 [ahead: "es material de m26" pointer after content ended] «Operar hacia un POC sin ninguna otra razón, y sin stop porque "tiene que llegar", es material de m26.»
  - S052 [editorial: last prose sentence, restates S051 noise point] «Leer footprint es una habilidad profesional construida encima de todo lo de este curso, no un atajo que se lo salte; y cuanto más granular es el dato, mayor es la proporción de ruido frente a señal.»
- **5 Sentence over 30 words** (17)
  - S002 [42w] «Este último módulo del bloque va de las dos herramientas que giran esa idea —organizan el volumen por precio en lugar de por tiempo— y de ser claros contigo sobre lo que este curso puede y no puede generar para que practiques.»
  - S006 [45w] «En lugar de un cuerpo y dos mechas, cada nivel de precio *dentro* del rango de esa vela recibe una fila, y cada fila muestra cuánto se negoció ahí, normalmente separado en volumen de compra taker y volumen de venta taker a ese precio exacto.»
  - S014 [34w] «Eso se lee como una historia concreta y no como una forma: los compradores empujaron hacia arriba y, en 60.100, se toparon con una venta fuerte que se comió la mayor parte del esfuerzo.»
  - S015 [32w] «Fíjate en que esto es el delta de m29, pero resuelto por nivel de precio en vez de sumado a lo largo del periodo: la resolución más fina de todo el bloque.»
  - S018 [32w] «Esa es la razón honesta de que aquí no haya ejercicio para él: nada más en este curso produce datos de distribución-dentro-de-una-barra, y la visualización no es en absoluto una serie temporal.»
  - S020 [37w **aside-only** (30w without asides)] «Un perfil de volumen aplica el mismo giro a un tramo más largo —una sesión, una semana, un rango entero— y dibuja el volumen total negociado a cada precio como un histograma horizontal al lado del gráfico.»
  - S026 [38w] «m03 y m08 enseñaban los niveles como sitios donde el precio ha reaccionado, trazados a partir de máximos y mínimos: honestos pero a ojo, y vulnerables a la crítica de que siempre puedes encontrar una línea que encaje.»
  - S028 [53w] «Un nodo de volumen alto es un precio en el que coincidieron muchos participantes y, por tanto, uno que probablemente defiendan o vuelvan a trabajar; un nodo de volumen bajo es un precio que el mercado rechazó rápido, y el precio suele atravesar esos huecos deprisa porque ahí hay poco historial de interés.»
  - S030 [31w] «Te da una razón para un nivel más allá de "parece un nivel", que es exactamente lo que pedía la advertencia de m08 sobre trazar líneas que encajen con tu sesgo.»
  - S036 [35w] «Un nivel con volumen detrás sigue siendo solo un nivel: te dice dónde una reacción es *más probable*, no que vaya a ocurrir, y no elimina la necesidad de confirmación, de stop ni de dimensionamiento.»
  - S037 [46w] «El perfil de volumen es el más accesible de los dos y está ampliamente disponible: TradingView incluye perfil de volumen de rango fijo y de sesión (las variantes más avanzadas están en los planes de pago), y casi cualquier plataforma de gráficos serios trae alguna versión.»
  - S045 [38w] «Los traders que se arruinan con un gráfico de footprint abierto lo hacen igual que todos los demás: posición demasiado grande, stop demasiado ajustado o inexistente, y la convicción de que un dato mejor les daba la razón.»
  - S048 [57w] «Tratar el POC como un imán que hay que tocar es la primera: "el precio siempre vuelve al POC" es folclore, y un nodo de volumen alto no es más que un precio con un historial de acuerdo, lo que hace una reacción ahí más probable que en un precio al azar: una probabilidad, no una cita.»
  - S051 [39w] «En la resolución más fina, la mayor parte de lo que ves es ruido: un único nivel de precio marcando 310 vendidos contra 120 comprados es un momento de una vela, e incontables desequilibrios así se resuelven en nada.»
  - S052 [37w] «Leer footprint es una habilidad profesional construida encima de todo lo de este curso, no un atajo que se lo salte; y cuanto más granular es el dato, mayor es la proporción de ruido frente a señal.»
  - S054 [65w] «El footprint abre una vela y muestra lo que se negoció en cada nivel dentro de ella —el delta de m29 resuelto por precio en vez de sumado en el periodo— mientras que el perfil de volumen hace lo mismo a lo largo de una sesión y te da el POC, el precio con más volumen, y el área de valor que contiene el grueso.»
  - S055 [61w] «Es una mejora sobre unos soportes y resistencias puestos a ojo, porque un nodo de volumen alto es un precio en el que muchos participantes se pusieron de acuerdo de verdad y no una línea que elegiste; la trampa es creer que un dato más fino es más certeza, y tratar el POC como un imán al que hay que llegar.»
- **A absolutes** (3)
  - S026 [siempre] «m03 y m08 enseñaban los niveles como sitios donde el precio ha reaccionado, trazados a partir de máximos y mínimos: honestos pero a ojo, y vulnerables a la crítica de que siempre puedes encontrar una línea que encaje.»
  - S043 [debería] «La trampa contra la que todo este bloque debería vacunarte es la creencia de que un dato más fino significa más certeza.»
  - S048 [siempre] «Tratar el POC como un imán que hay que tocar es la primera: "el precio siempre vuelve al POC" es folclore, y un nodo de volumen alto no es más que un precio con un historial de acuerdo, lo que hace una reacción ahí más probable que en un precio al azar: una probabilidad, no una cita.»

**EN** — 29 hits, 55 sentences, density 52.7

- **1 Filler** (9)
  - S015 [extra: "Notice" announcer] «Notice this is the delta of m29, but resolved by price level rather than summed over the period — the finest resolution in this block.»
  - S018 [honest: applied to a reason] «That is the honest reason there is no exercise for it here: nothing else in this course produces distribution-within-a-bar data, and the visualisation is not a time series at all.»
  - S018 [extra: "at all"] «That is the honest reason there is no exercise for it here: nothing else in this course produces distribution-within-a-bar data, and the visualisation is not a time series at all.»
  - S026 [honest: applied to levels] «m03 and m08 taught levels as places price has reacted to — drawn from highs and lows, honest but eyeballed, and vulnerable to the criticism that you can always find a line that fits.»
  - S030 [precisely: emphatic] «It gives you a reason for a level beyond "it looks like one" — which is precisely what m08's warning about drawing lines to fit your bias was asking for.»
  - S042 [genuinely] «The POC of yesterday's session, drawn on today's chart, is a genuinely useful level and costs you nothing to try.»
  - S044 [genuine: emphatic] «Order flow, the book, footprints: each is a genuine upgrade in resolution, and none of them converts a probability into a guarantee.»
  - S047 [extra: "Two specific versions are worth naming" announcer] «Two specific versions are worth naming, because both are this module's tools turned against their owner.»
  - S055 [actually: emphatic] «That is an upgrade on eyeballed support and resistance, because a high-volume node is a price many participants actually agreed on rather than a line you chose; the trap is believing finer data is more certainty, and treating the POC as a magnet that must be hit.»
- **2 Rhythmic triad** (1)
  - S001 [one candle / one volume bar / one CVD value per period — drop the CVD item] «Every chart in this course puts time on the horizontal axis: one candle per period, one volume bar per period, one CVD value per period.»
- **4 Summary/uplift closer** (6)
  - S004 [ahead] «The reason is explained below rather than left as a gap.»
  - S015 [editorial] «Notice this is the delta of m29, but resolved by price level rather than summed over the period — the finest resolution in this block.»
  - S030 [editorial] «It gives you a reason for a level beyond "it looks like one" — which is precisely what m08's warning about drawing lines to fit your bias was asking for.»
  - S046 [restate] «Resolution is not certainty.»
  - S049 [ahead: "is m26's material"] «Trading toward a POC with no other reason, and with no stop because "it has to get there", is m26's material.»
  - S052 [editorial: last prose sentence] «Footprint reading is a professional skill built on top of everything in this course, not a shortcut around it — and the more granular the data, the higher the ratio of noise to signal.»
- **5 Sentence over 30 words** (13)
  - S002 [43w] «This last module of the block is about the two tools that rotate that idea — they organise volume by price instead of by time — and about being straight with you regarding what this course can and cannot generate for you to practise on.»
  - S006 [39w] «Instead of one body and two wicks, each price level *within* that candle's range gets a row, and each row shows how much traded there — usually split into taker buy volume and taker sell volume at that exact price.»
  - S020 [33w **aside-only** (26w without asides)] «A volume profile applies the same rotation to a longer stretch — a session, a week, an entire range — and plots total volume traded at each price as a horizontal histogram beside the chart.»
  - S026 [33w] «m03 and m08 taught levels as places price has reacted to — drawn from highs and lows, honest but eyeballed, and vulnerable to the criticism that you can always find a line that fits.»
  - S028 [46w] «A high-volume node is a price many participants agreed on and therefore one they are likely to defend or re-engage with; a low-volume node is a price the market rejected quickly, and price often traverses such gaps fast because there is little history of interest there.»
  - S036 [38w] «A level with volume behind it is still only a level: it tells you where a reaction is *more likely*, not that one will happen, and it does not remove the need for confirmation, a stop, or sizing.»
  - S037 [36w **aside-only** (28w without asides)] «Volume profile is the more accessible of the two and is widely available: TradingView includes fixed-range and session volume profile (the more advanced variants sit behind paid tiers), and most serious charting platforms ship some version.»
  - S045 [35w] «The traders who blow up with a footprint chart open do it the same way as everyone else — position too large, stop too tight or absent, and a conviction that better data made them right.»
  - S048 [51w] «Treating the POC as a magnet that must be hit is the first: "price always returns to the POC" is folklore, and a high-volume node is only a price with a history of agreement, which makes a reaction there more likely than at a random price — a probability, not an appointment.»
  - S051 [34w] «At the finest resolution most of what you see is noise: a single price level printing 310 sold against 120 bought is one moment of one candle, and countless such imbalances resolve into nothing.»
  - S052 [33w] «Footprint reading is a professional skill built on top of everything in this course, not a shortcut around it — and the more granular the data, the higher the ratio of noise to signal.»
  - S054 [56w] «A footprint breaks one candle open into what traded at each level inside it — m29's delta resolved by price rather than summed over the period — while a volume profile does the same across a session and gives you the POC, the price with the most volume, and the value area that holds the bulk of it.»
  - S055 [47w] «That is an upgrade on eyeballed support and resistance, because a high-volume node is a price many participants actually agreed on rather than a line you chose; the trap is believing finer data is more certainty, and treating the POC as a magnet that must be hit.»
- **A absolutes** (3)
  - S026 [always] «m03 and m08 taught levels as places price has reacted to — drawn from highs and lows, honest but eyeballed, and vulnerable to the criticism that you can always find a line that fits.»
  - S048 [must, always] «Treating the POC as a magnet that must be hit is the first: "price always returns to the POC" is folklore, and a high-volume node is only a price with a history of agreement, which makes a reaction there more likely than at a random price — a probability, not an appointment.»
  - S055 [must, summary] «That is an upgrade on eyeballed support and resistance, because a high-volume node is a price many participants actually agreed on rather than a line you chose; the trap is believing finer data is more certainty, and treating the POC as a magnet that must be hit.»

### m34-l1

**ES** — 65 hits, 103 sentences, density 63.1

- **1 Filler** (9)
  - S007 [exactamente: emphatic] «Así que esta lección hace con el léxico SMC exactamente lo que m08-l2 hizo con los patrones de vela japoneses: mapea cada nombre sobre una mecánica más una ubicación, nunca como señal por sí sola.»
  - S013 [extra: "palabra por palabra" intensifier] «Eso es, palabra por palabra, el comprador que absorbe dentro del rango de m09.»
  - S019 [Fíjate en: announcer] «Fíjate en dos cosas que hacen honesta esa frase.»
  - S019 [honesta: applied to a sentence] «Fíjate en dos cosas que hacen honesta esa frase.»
  - S044 [extra: "Ojo con la palabra:" announcer] «Ojo con la palabra: a menudo, no siempre.»
  - S047 [claramente: degree adverb adds nothing] «Durante el resto de la ventana el precio se queda claramente por encima y el hueco sigue abierto; el tramo final es la vuelta a por él, con la mecha entrando hasta 27.320.»
  - S071 [exactamente: emphatic] «Aquí es donde este dialecto se separa de lo que este curso está dispuesto a afirmar, y conviene ver exactamente en qué punto.»
  - S097 [extra: "perfectamente" intensifier] «Un stop más allá del extremo lejano de una zona es un stop estructural perfectamente razonable; un stop ampliado para que la zona "tenga margen" es m26.»
  - S098 [honesta: applied to a reason] «Y quédate con la razón honesta por la que merecía la pena leer esto: la mitad de lo que se escribe sobre gráficos está escrito en este dialecto, y no poder leerlo es una desventaja sin ninguna ventaja.»
- **2 Rhythmic triad** (1)
  - S076 [discutirlo / comprobarlo / equivocarte con él — argue and check overlap; drop "discutirlo"] «Puedes discutirlo, comprobarlo y equivocarte con él.»
- **4 Summary/uplift closer** (8)
  - S003 [ahead: "la afirmación que esta lección acaba desmontando"] «El smart money del nombre es la afirmación misma: que existe una clase identificable de participantes institucionales que mueve el precio deliberadamente contra todos los demás, y que estos patrones son las huellas que deja; es la afirmación que esta lección acaba desmontando.»
  - S006 [editorial: "Lo que falta no es mecánica: es el diccionario"] «Lo que falta no es mecánica: es el diccionario.»
  - S009 [ahead: "es el tema de la última sección"] «Esas dos cosas no son lo mismo, y la diferencia es el tema de la última sección.»
  - S044 [editorial: comments on the word "a menudo"] «Ojo con la palabra: a menudo, no siempre.»
  - S057 [editorial] «El segundo acrónimo añade una palabra, no una idea; ahora m08-l1 también lo nombra, donde vive la escalera.»
  - S076 [editorial] «Puedes discutirlo, comprobarlo y equivocarte con él.»
  - S081 [editorial: course-boundary framing] «Es la misma frontera que dibujan m29 con el flujo de órdenes y m33 con el footprint: decir qué hace la herramienta, decir dónde se para, y no dejar que un relato ocupe el sitio de un mecanismo.»
  - S100 [editorial: last prose sentence, "Eso es todo el efecto que hay"] «Eso es todo el efecto que hay, y también su fecha de caducidad.»
- **5 Sentence over 30 words** (26)
  - S003 [43w] «El smart money del nombre es la afirmación misma: que existe una clase identificable de participantes institucionales que mueve el precio deliberadamente contra todos los demás, y que estos patrones son las huellas que deja; es la afirmación que esta lección acaba desmontando.»
  - S005 [50w] «Casi toda la sustancia ya está enseñada, con otros nombres: las bolsas de liquidez y los barridos en m19-l2, el spring y la absorción en m09, el cambio de carácter en m08-l1, la inversión de roles y los soportes como *zonas* también en m08-l1, el vacío de liquidez en m08-l2.»
  - S007 [35w] «Así que esta lección hace con el léxico SMC exactamente lo que m08-l2 hizo con los patrones de vela japoneses: mapea cada nombre sobre una mecánica más una ubicación, nunca como señal por sí sola.»
  - S021 [31w] «Nadie anuncia nada y el libro de órdenes no muestra nada; lo que se razona es que un tamaño capaz de mover el precio así difícilmente cupo en un solo precio.»
  - S022 [33w] «La segunda: es una zona, como todo soporte en este curso (m08-l1), porque está definida por los extremos de unas velas y porque la reacción se espera *en algún punto dentro de ella*.»
  - S024 [35w] «Sin un cierre limpio más allá del máximo que el mercado venía respetando, no hay impulso que haya roto nada, y las velas anteriores son un retroceso corriente de los que toda tendencia está llena.»
  - S025 [32w] «Este es el error que más caro sale del dialecto entero: dibujar la zona primero y no comprobar nunca la estructura, con lo que se puede encontrar una zona en cualquier gráfico.»
  - S030 [31w **aside-only** (25w without asides)] «Y no es una mecha asomando —decide el cuerpo, como en m08-l1—: el impulso continúa y deja cierres hasta 2.045, más de un 4 % por encima del máximo que ha roto.»
  - S032 [44w] «m08-l2 ya te avisó de este fenómeno desde el otro extremo: una mecha muy larga impresa en un libro fino de fin de semana es un vacío de liquidez, un trecho por el que casi nada se negoció, y hay que desconfiar de ella.»
  - S034 [35w] «Lo que m08-l2 dejó fuera es que el mismo vacío, cuando un movimiento rápido lo deja *detrás*, es una zona, y que el precio vuelve a ella lo bastante a menudo para merecer un nombre.»
  - S042 [32w] «Al otro lado de ese tramo quedaron órdenes que querían operar y no pudieron, y quien se subió al movimiento lo hizo sin la referencia de precio que da un rango negociado.»
  - S046 [35w] «El máximo de la vela anterior está en 27.100 y el mínimo de la siguiente en 28.000, así que ese tramo de unos 900 puntos —la banda sombreada— se cruzó dentro de esa única barra.»
  - S047 [33w] «Durante el resto de la ventana el precio se queda claramente por encima y el hueco sigue abierto; el tramo final es la vuelta a por él, con la mecha entrando hasta 27.320.»
  - S049 [32w] «No es un hueco de sesión: los mercados tradicionales cierran y abren con salto, y el cripto funciona 24/7 (m10-l1), así que esto es siempre un desequilibrio *dentro* de una serie continua.»
  - S052 [34w **aside-only** (29w without asides)] «m08-l1 te enseñó la escalera —máximos y mínimos más altos— y le puso nombre a la ruptura que la termina: el cambio de carácter, CHoCH, el primer mínimo más bajo en una tendencia alcista.»
  - S064 [31w] «Sobre la última, porque es la que más se estira: premium y discount significan *estás en la mitad alta o en la mitad baja de un rango que has dibujado tú*.»
  - S067 [51w] «Donde esto se convierte en numerología es en las bandas con decimales, del tipo "la entrada óptima está en el 0,705–0,79": m13 ya zanjó que ningún mecanismo obliga a un mercado a respetar una proporción, y que lo único que tienen esos niveles a favor es que mucha gente los vigila.»
  - S073 [34w] «*"Los stops y los precios de liquidación se agrupan justo debajo de un mínimo obvio, así que un movimiento hasta esa banda dispara una ráfaga de ventas que alguien absorbe desde el otro lado."*»
  - S075 [34w] «El primero nombra un mecanismo con piezas que puedes señalar: dónde están las órdenes de protección y por qué se agrupan (m19-l2), y qué le hace la venta forzada a un libro fino (m06-l1).»
  - S081 [38w] «Es la misma frontera que dibujan m29 con el flujo de órdenes y m33 con el footprint: decir qué hace la herramienta, decir dónde se para, y no dejar que un relato ocupe el sitio de un mecanismo.»
  - S084 [34w] «El dialecto está especialmente expuesto: las zonas son bandas, las bandas se pueden mover un poco, y todo impulso tiene velas antes, así que a posteriori siempre se encuentra una cerca de una reacción.»
  - S098 [38w] «Y quédate con la razón honesta por la que merecía la pena leer esto: la mitad de lo que se escribe sobre gráficos está escrito en este dialecto, y no poder leerlo es una desventaja sin ninguna ventaja.»
  - S099 [44w] «Que mucha gente vigile las mismas zonas hace que se acumulen órdenes a su alrededor, y ese efecto es real —igual que el del 0,618 y el de la media de 200—, pero funciona mientras la zona esté concurrida, no porque el nombre acierte.»
  - S101 [54w] «El dialecto SMC es un diccionario más que un sistema: un order block es la zona de origen del impulso, un fair value gap es un tramo cruzado dentro de una sola vela, un liquidity grab es el barrido de m19-l2, y BOS y CHoCH son las dos rupturas de la escalera de m08-l1.»
  - S102 [40w] «Cada uno es una mecánica que ya tienes, y el orden importa sobre todo en la zona de origen: la ruptura va primero, o las velas anteriores son un pullback corriente y entonces puede encontrarse una zona en cualquier gráfico.»
  - S103 [37w] «Apréndelo porque la masa lo habla, no porque prediga: una afirmación que nombra un actor y un motivo en lugar de un mecanismo explica igual de bien todos los desenlaces, lo que significa que no predice ninguno.»
- **9 Course-coined term** (18)
  - S005 [bolsa de liquidez [seed]] «Casi toda la sustancia ya está enseñada, con otros nombres: las bolsas de liquidez y los barridos en m19-l2, el spring y la absorción en m09, el cambio de carácter en m08-l1, la inversión de roles y los soportes como *zonas* también en m08-l1, el vacío de liquidez en m08-l2.»
  - S008 [non-seed "dialecto" as the name for SMC vocabulary] «Y adopta la misma postura que m13 con Fibonacci y m10-l1 con la media de 200: merece la pena entender este dialecto porque la masa lo habla, no porque prediga.»
  - S018 [non-seed "zona de origen del impulso" (course's own name for order block)] «A esa zona el dialecto la llama order block; aquí la llamamos la zona de origen del impulso, que es lo que es.»
  - S018 [non-seed "dialecto"] «A esa zona el dialecto la llama order block; aquí la llamamos la zona de origen del impulso, que es lo que es.»
  - S025 [non-seed "dialecto"] «Este es el error que más caro sale del dialecto entero: dibujar la zona primero y no comprobar nunca la estructura, con lo que se puede encontrar una zona en cualquier gráfico.»
  - S028 [non-seed "zona de origen"] «Las últimas velas bajistas antes del impulso van de 1.810 a 1.855: esa banda sombreada es la zona de origen.»
  - S052 [escalera [seed]] «m08-l1 te enseñó la escalera —máximos y mínimos más altos— y le puso nombre a la ruptura que la termina: el cambio de carácter, CHoCH, el primer mínimo más bajo en una tendencia alcista.»
  - S056 [escalera [seed]] «Una escalera, dos clases de ruptura: la que continúa la secuencia y la que la rompe.»
  - S057 [escalera [seed]] «El segundo acrónimo añade una palabra, no una idea; ahora m08-l1 también lo nombra, donde vive la escalera.»
  - S059 [non-seed "zona de origen de un impulso"] «la zona de origen de un impulso: las últimas velas contrarias antes del movimiento que rompió la estructura. *m08-l1* (inversión de roles, zonas en vez de líneas) y *m09* (absorción).»
  - S061 [seed variant: "bolsa de stops en reposo"] «un barrido de una bolsa de stops en reposo, con recuperación inmediata del nivel. *m19-l2*, y las mechas de caza de stops de *m08-l1*.»
  - S062 [escalera [seed]] «las dos rupturas de la escalera: la que continúa la secuencia y la que la termina. *m08-l1*.»
  - S071 [non-seed "dialecto"] «Aquí es donde este dialecto se separa de lo que este curso está dispuesto a afirmar, y conviene ver exactamente en qué punto.»
  - S084 [non-seed "dialecto"] «El dialecto está especialmente expuesto: las zonas son bandas, las bandas se pueden mover un poco, y todo impulso tiene velas antes, así que a posteriori siempre se encuentra una cerca de una reacción.»
  - S095 [non-seed "dialecto"] «El dialecto no se gana una excepción; se gana la misma prueba.»
  - S098 [non-seed "dialecto"] «Y quédate con la razón honesta por la que merecía la pena leer esto: la mitad de lo que se escribe sobre gráficos está escrito en este dialecto, y no poder leerlo es una desventaja sin ninguna ventaja.»
  - S101 [escalera [seed]] «El dialecto SMC es un diccionario más que un sistema: un order block es la zona de origen del impulso, un fair value gap es un tramo cruzado dentro de una sola vela, un liquidity grab es el barrido de m19-l2, y BOS y CHoCH son las dos rupturas de la escalera de m08-l1.»
  - S102 [non-seed "zona de origen"] «Cada uno es una mecánica que ya tienes, y el orden importa sobre todo en la zona de origen: la ruptura va primero, o las velas anteriores son un pullback corriente y entonces puede encontrarse una zona en cualquier gráfico.»
- **10 Metaphor then gloss** (1)
  - S052 ["la escalera" glossed in the same sentence: máximos y mínimos más altos] «m08-l1 te enseñó la escalera —máximos y mínimos más altos— y le puso nombre a la ruptura que la termina: el cambio de carácter, CHoCH, el primer mínimo más bajo en una tendencia alcista.»
- **11 Synonym rotation** (2)
  - S006 [SMC vocabulary: diccionario (S006), léxico SMC (S007), dialecto (S008)] 
  - S034 [FVG span: vacío (S034), tramo (S037), hueco (S047), desequilibrio (S048)] 
- **A absolutes** (7)
  - S007 [nunca] «Así que esta lección hace con el léxico SMC exactamente lo que m08-l2 hizo con los patrones de vela japoneses: mapea cada nombre sobre una mecánica más una ubicación, nunca como señal por sí sola.»
  - S025 [nunca] «Este es el error que más caro sale del dialecto entero: dibujar la zona primero y no comprobar nunca la estructura, con lo que se puede encontrar una zona en cualquier gráfico.»
  - S044 [siempre] «Ojo con la palabra: a menudo, no siempre.»
  - S049 [siempre] «No es un hueco de sesión: los mercados tradicionales cierran y abren con salto, y el cripto funciona 24/7 (m10-l1), así que esto es siempre un desequilibrio *dentro* de una serie continua.»
  - S084 [siempre] «El dialecto está especialmente expuesto: las zonas son bandas, las bandas se pueden mover un poco, y todo impulso tiene velas antes, así que a posteriori siempre se encuentra una cerca de una reacción.»
  - S088 [nunca] «Los huecos se revisitan a menudo y algunos no se revisitan nunca, sobre todo los que una tendencia dejó atrás.»
  - S093 [nunca] «Reacción *dentro* de la banda, con la holgura que m08-l1 y m13 exigen a cualquier nivel, y con el cierre —nunca el extremo— decidiendo si se perdió.»

**EN** — 62 hits, 104 sentences, density 59.6

- **1 Filler** (12)
  - S008 [exactly: emphatic] «So this lesson does to the SMC lexicon exactly what m08-l2 did to the named Japanese candle patterns: it maps each name onto a mechanic plus a location, never as a standalone signal.»
  - S014 [extra: "word for word" intensifier] «That is, word for word, m09's buyer absorbing inside the range.»
  - S020 [honest: applied to a sentence] «Notice two things that keep that sentence honest.»
  - S020 [extra: "Notice" announcer] «Notice two things that keep that sentence honest.»
  - S026 [extra: "at all"] «This is the costliest error in the whole dialect: the zone gets drawn first and the structure is never checked, which means a zone can be found on any chart at all.»
  - S045 [extra: "Mind the word:" announcer] «Mind the word: often, not always.»
  - S070 [genuinely: emphatic] «And in crypto the word collides with two genuinely different things that do have mechanisms: the inter-venue premium (m32) and the perp-versus-spot basis (m19).»
  - S072 [exactly: emphatic] «This is where the dialect parts company with what this course is willing to assert, and it is worth seeing exactly at which point.»
  - S089 [extra: "at all"] «Gaps are revisited often and some are never revisited at all, especially the ones a trend ran away from.»
  - S091 [exactly: emphatic] «Nothing you have read here changes how a trade is built, and that is exactly why this module sits at the end of the course:»
  - S098 [extra: "perfectly" intensifier] «A stop beyond a zone's far edge is a perfectly sensible structural stop; a stop widened so the zone has "room to work" is m26.»
  - S099 [honest: applied to a reason] «And keep the honest reason this was worth reading: half of what is written about charts is written in this dialect, and being unable to read it is a handicap with no upside.»
- **2 Rhythmic triad** (1)
  - S077 [argue with it / check it / be wrong about it — drop "argue with it"] «You can argue with it, check it, and be wrong about it.»
- **4 Summary/uplift closer** (8)
  - S003 [ahead] «The smart money in that name is itself the claim: that an identifiable class of institutional participants moves price deliberately against everyone else, and that these patterns are the footprints it leaves — the claim this lesson ends up dismantling.»
  - S007 [editorial: "It is the dictionary."] «It is the dictionary.»
  - S010 [ahead] «Those are not the same claim, and the difference is what the last section is about.»
  - S045 [editorial] «Mind the word: often, not always.»
  - S058 [editorial] «The second acronym adds a word, not an idea — and m08-l1 now names it too, where the ladder lives.»
  - S077 [editorial] «You can argue with it, check it, and be wrong about it.»
  - S082 [editorial] «It is the same boundary m29 draws around order flow and m33 around the footprint: say what the tool does, say where it stops, and never let a story stand in for a mechanism.»
  - S101 [editorial: last prose sentence] «That is the whole of the effect, and also its expiry date.»
- **5 Sentence over 30 words** (20)
  - S003 [39w] «The smart money in that name is itself the claim: that an identifiable class of institutional participants moves price deliberately against everyone else, and that these patterns are the footprints it leaves — the claim this lesson ends up dismantling.»
  - S005 [42w] «Almost all of the substance is already taught, under other names: liquidity pools and sweeps in m19-l2, the spring and absorption in m09, the change of character in m08-l1, role reversal and support-as-a-*zone* also in m08-l1, the liquidity void in m08-l2.»
  - S008 [33w] «So this lesson does to the SMC lexicon exactly what m08-l2 did to the named Japanese candle patterns: it maps each name onto a mechanic plus a location, never as a standalone signal.»
  - S023 [33w] «Second, it is a zone, like every support in this course (m08-l1), because it is defined by the extremes of a handful of candles and because the reaction is expected *somewhere inside it*.»
  - S025 [36w] «Without a clean close beyond the high the market had been respecting, there is no impulse that broke anything, and the candles before it are an ordinary pullback of the kind every trend is full of.»
  - S026 [32w] «This is the costliest error in the whole dialect: the zone gets drawn first and the structure is never checked, which means a zone can be found on any chart at all.»
  - S031 [36w] «And it is not a wick poking through: what decides is the body, as in m08-l1, and the impulse goes on to close as high as 2,045, more than 4% clear of the high it broke.»
  - S033 [36w] «m08-l2 already warned you about this phenomenon from the other end: a very long wick printed in a thin weekend book is a liquidity void, a stretch almost nothing traded through, and it should be distrusted.»
  - S035 [32w] «What m08-l2 left out is that the same emptiness, when a fast move leaves it *behind*, is a zone, and that price returns to it often enough to be worth a name.»
  - S043 [31w] «On the far side of that span sat orders that wanted to trade and could not, and whoever joined the move did so without the price reference a traded range provides.»
  - S048 [31w] «For the rest of the window price stays clearly above it and the gap stays open; the closing stretch is it coming back for it, the wick reaching down to 27,320.»
  - S065 [31w] «On that last one, because it is the one that gets stretched furthest: premium and discount mean *you are in the upper or the lower half of a range you drew*.»
  - S068 [50w] «Where this tips into numerology is the bands with decimal places, the "optimal trade entry is the 0.705–0.79 retracement" kind: m13 already settled that no mechanism forces a market to respect a ratio, and that all such a level has going for it is that plenty of people watch it.»
  - S082 [34w] «It is the same boundary m29 draws around order flow and m33 around the footprint: say what the tool does, say where it stops, and never let a story stand in for a mechanism.»
  - S085 [32w] «The dialect is unusually exposed to this: zones are bands, bands can be nudged, and every impulse has candles before it, so a hindsight reader will always find one near a reaction.»
  - S099 [33w] «And keep the honest reason this was worth reading: half of what is written about charts is written in this dialect, and being unable to read it is a handicap with no upside.»
  - S100 [42w] «Plenty of people watching the same zones does make orders pile up around them, and that effect is real — as real as the 0.618 and the 200-day average — but it works while the zone is crowded, not because the name is right.»
  - S102 [47w] «The SMC dialect is a dictionary rather than a system: an order block is the impulse's origin zone, a fair value gap is a span crossed inside a single candle, a liquidity grab is m19-l2's sweep, and BOS and CHoCH are the two breaks of m08-l1's ladder.»
  - S103 [41w] «Every one of them is a mechanic you already have, and the order matters most for the origin zone — the break comes first, or the candles before it are an ordinary pullback and a zone can be found on any chart.»
  - S104 [36w] «Learn it because the crowd speaks it, not because it predicts: a claim that names an actor and a motive rather than a mechanism explains every outcome equally well, which means it predicts none of them.»
- **9 Course-coined term** (18)
  - S005 [liquidity pool [seed]] «Almost all of the substance is already taught, under other names: liquidity pools and sweeps in m19-l2, the spring and absorption in m09, the change of character in m08-l1, role reversal and support-as-a-*zone* also in m08-l1, the liquidity void in m08-l2.»
  - S009 [non-seed "dialect"] «And it takes the same stance m13 takes towards Fibonacci and m10-l1 towards the 200-day average: this dialect is worth understanding because the crowd speaks it, not because it predicts.»
  - S019 [non-seed "impulse's origin zone"] «The dialect calls that area an order block; here we call it the impulse's origin zone, which is what it is.»
  - S019 [non-seed "dialect"] «The dialect calls that area an order block; here we call it the impulse's origin zone, which is what it is.»
  - S026 [non-seed "dialect"] «This is the costliest error in the whole dialect: the zone gets drawn first and the structure is never checked, which means a zone can be found on any chart at all.»
  - S029 [non-seed "origin zone"] «The last down candles before the impulse run from 1,810 to 1,855: that shaded band is the origin zone.»
  - S053 [staircase/ladder [seed]] «m08-l1 taught you the ladder — higher highs and higher lows — and named the break that ends it: the change of character, CHoCH, the first lower low in an uptrend.»
  - S057 [staircase/ladder [seed]] «One ladder, two kinds of break: the one that continues the sequence and the one that ends it.»
  - S058 [staircase/ladder [seed]] «The second acronym adds a word, not an idea — and m08-l1 now names it too, where the ladder lives.»
  - S060 [non-seed "impulse's origin zone"] «the impulse's origin zone: the last opposing candles before the move that broke structure. *m08-l1* (role reversal, zones rather than lines) and *m09* (absorption).»
  - S062 [seed variant: "pocket of resting stops"] «a sweep of a pocket of resting stops, with the level reclaimed immediately. *m19-l2*, and *m08-l1*'s stop-hunting wicks.»
  - S063 [staircase/ladder [seed]] «the two breaks of the ladder: the one that continues the sequence and the one that ends it. *m08-l1*.»
  - S072 [non-seed "dialect"] «This is where the dialect parts company with what this course is willing to assert, and it is worth seeing exactly at which point.»
  - S085 [non-seed "dialect"] «The dialect is unusually exposed to this: zones are bands, bands can be nudged, and every impulse has candles before it, so a hindsight reader will always find one near a reaction.»
  - S096 [non-seed "dialect"] «The dialect gets no exception; it gets the same test.»
  - S099 [non-seed "dialect"] «And keep the honest reason this was worth reading: half of what is written about charts is written in this dialect, and being unable to read it is a handicap with no upside.»
  - S102 [staircase/ladder [seed]] «The SMC dialect is a dictionary rather than a system: an order block is the impulse's origin zone, a fair value gap is a span crossed inside a single candle, a liquidity grab is m19-l2's sweep, and BOS and CHoCH are the two breaks of m08-l1's ladder.»
  - S103 [non-seed "origin zone"] «Every one of them is a mechanic you already have, and the order matters most for the origin zone — the break comes first, or the candles before it are an ordinary pullback and a zone can be found on any chart.»
- **10 Metaphor then gloss** (1)
  - S053 ["the ladder" glossed in the same sentence: higher highs and higher lows] «m08-l1 taught you the ladder — higher highs and higher lows — and named the break that ends it: the change of character, CHoCH, the first lower low in an uptrend.»
- **11 Synonym rotation** (2)
  - S007 [SMC vocabulary: dictionary (S007), lexicon (S008), dialect (S009)] 
  - S035 [FVG span: emptiness/void (S035), span (S038), gap (S048), imbalance (S049)] 
- **A absolutes** (9)
  - S008 [never] «So this lesson does to the SMC lexicon exactly what m08-l2 did to the named Japanese candle patterns: it maps each name onto a mechanic plus a location, never as a standalone signal.»
  - S017 [never] «If the size that caused the rally was working there and never got fully filled, what is left is still there.»
  - S026 [never] «This is the costliest error in the whole dialect: the zone gets drawn first and the structure is never checked, which means a zone can be found on any chart at all.»
  - S045 [always] «Mind the word: often, not always.»
  - S050 [always] «It is not a session gap: traditional markets close and reopen with a jump, and crypto runs 24/7 (m10-l1), so this is always an imbalance *inside* a continuous series.»
  - S082 [never] «It is the same boundary m29 draws around order flow and m33 around the footprint: say what the tool does, say where it stops, and never let a story stand in for a mechanism.»
  - S085 [always] «The dialect is unusually exposed to this: zones are bands, bands can be nudged, and every impulse has candles before it, so a hindsight reader will always find one near a reaction.»
  - S089 [never] «Gaps are revisited often and some are never revisited at all, especially the ones a trend ran away from.»
  - S094 [never] «A reaction *inside* the band, with the tolerance m08-l1 and m13 demand of any level, and with the close — never the extreme — deciding whether it was lost.»

### m35-l1

**ES** — 44 hits, 57 sentences, density 77.2

- **1 Filler** (10)
  - S011 [extra: "Y ahora el límite, con la misma franqueza" announcer] «Y ahora el límite, con la misma franqueza.»
  - S013 [extra: justo] «Lo que sí te ha dado este curso es el criterio para acumular esa experiencia sin arruinarte mientras la acumulas —el tamaño que sobrevive a una racha mala, el stop decidido antes de la entrada, el diario que convierte una operación en un dato en vez de en un recuerdo—, y eso es justo lo que separa a quien llegará a mil operaciones de quien se queda en veinte.»
  - S017 [exactamente: emphatic] «El diario que m27-l2 te hizo empezar es lo único que convierte horas de pantalla en muestra, y la muestra es exactamente lo que m28 exigía para poder decir algo de tu sistema.»
  - S021 [extra: justo] «La app te deja desmarcar una lección ya completada justo para esto, sin perder nada de lo que llevas hecho.»
  - S022 [extra: "Y ahora el aviso que protege todo lo anterior" announcer] «Y ahora el aviso que protege todo lo anterior, porque es el error clásico del día después de terminar un curso: la tentación es buscar más tácticas.»
  - S024 [Fíjate en: announcer] «Fíjate en lo que eso es en realidad: añadir mandos a un sistema cuya muestra no ha crecido.»
  - S024 [en realidad: emphatic] «Fíjate en lo que eso es en realidad: añadir mandos a un sistema cuya muestra no ha crecido.»
  - S027 [de verdad: emphatic ("un escalón de verdad")] «Si en algún momento quieres subir un escalón de verdad, hay dos escaleras, y este curso no es el primer peldaño de ninguna: son edificios distintos.»
  - S036 [honestidad: announcer ("La honestidad que importa aquí")] «La honestidad que importa aquí: es otra profesión.»
  - S043 [extra: "Queda una cosa por decir" announcer] «Queda una cosa por decir, y hace falta el mismo día que termines el curso.»
- **2 Rhythmic triad** (4)
  - S004 [frame: Sabes… (S004) / Sabes… (S005) / Sabes… (S006) / Y sabes… (S007) — repeated opener; merge two] «Sabes leer un gráfico por mecanismos en lugar de por formas: qué órdenes hay en reposo en un nivel y por qué se acumulan ahí, qué le hace la venta forzada a un libro fino, qué esconde una vela cuando la miras como el agregado que es.»
  - S023 [otro patrón / otro indicador / otro setup con nombre propio — drop "otro setup con nombre propio"] «Otro patrón, otro indicador, otro setup con nombre propio.»
  - S037 [código / estadística / datos — statistics and data overlap; drop "datos"] «Donde este curso puso ojos y proceso, esa escalera pone código, estadística y datos, y los tres se aprenden aparte.»
  - S052 [la prisa / el FOMO / la racha ajena… — hurry and FOMO overlap; drop "la prisa"] «Y todo ese ecosistema está construido sobre la psicología que describe m26: la prisa, el FOMO, la racha ajena vista de cerca y la propia vista de lejos.»
- **4 Summary/uplift closer** (7)
  - S003 [editorial] «Sin inflar nada: un curso que exagera lo que ha enseñado deja mal preparado para lo primero que pasa después de terminarlo.»
  - S010 [restate] «Las técnicas caducan cuando cambia el mercado que las produjo; el criterio no.»
  - S013 [motivate: "lo que separa a quien llegará a mil operaciones de quien se queda en veinte"] «Lo que sí te ha dado este curso es el criterio para acumular esa experiencia sin arruinarte mientras la acumulas —el tamaño que sobrevive a una racha mala, el stop decidido antes de la entrada, el diario que convierte una operación en un dato en vez de en un recuerdo—, y eso es justo lo que separa a quien llegará a mil operaciones de quien se queda en veinte.»
  - S026 [restate] «Más tácticas sobre la misma muestra no es más sistema; es menos.»
  - S028 [editorial] «Nombrarlas es más útil que fingir que no están ahí.»
  - S039 [editorial] «Lo que sigue valiendo dentro de él es lo de siempre —una ventaja medida, un tamaño que sobrevive a la racha, un criterio de abandono escrito antes de necesitarlo—, y por eso este curso va primero aunque no lleve allí.»
  - S054 [motivate: last prose sentence ("la única campana de cierre…")] «Elige tu temporalidad, dimensiona desde el stop, escribe antes de mirar, y que la única campana de cierre que tengas siga siendo la que te construyes tú.»
- **5 Sentence over 30 words** (19)
  - S004 [47w] «Sabes leer un gráfico por mecanismos en lugar de por formas: qué órdenes hay en reposo en un nivel y por qué se acumulan ahí, qué le hace la venta forzada a un libro fino, qué esconde una vela cuando la miras como el agregado que es.»
  - S005 [33w] «Sabes dimensionar una posición desde la distancia al stop y no desde el apalancamiento (m22), lo que significa que sabes cuánto puedes perder antes de abrirla y que ese número lo eliges tú.»
  - S009 [46w] «Es la pregunta que este curso ha repetido en cada módulo —qué órdenes hay ahí, quién las puso, qué las obliga a ejecutarse— y es la única que seguirá sirviendo con material que este curso no cubre, incluido el que se escriba el año que viene.»
  - S012 [40w] «El curso no te ha dado experiencia, y no puede dártela: saber cómo se comporta un libro fino a las 3 de la madrugada de un domingo no es lo mismo que haber tenido una posición abierta a esa hora.»
  - S013 [69w] «Lo que sí te ha dado este curso es el criterio para acumular esa experiencia sin arruinarte mientras la acumulas —el tamaño que sobrevive a una racha mala, el stop decidido antes de la entrada, el diario que convierte una operación en un dato en vez de en un recuerdo—, y eso es justo lo que separa a quien llegará a mil operaciones de quien se queda en veinte.»
  - S017 [33w] «El diario que m27-l2 te hizo empezar es lo único que convierte horas de pantalla en muestra, y la muestra es exactamente lo que m28 exigía para poder decir algo de tu sistema.»
  - S025 [57w] «Es el sobreajuste de m28 en versión humana —la misma operación de ajustar el ruido, hecha con la carrera de uno en lugar de con una hoja de cálculo— y tiene el mismo síntoma: cada racha mala produce una regla nueva, y así ninguna regla llega a acumular las operaciones que harían falta para saber si servía.»
  - S030 [40w] «la comisión, el slippage y el impacto que tu propia orden tiene en el precio, cada uno como una función del tamaño de la orden y no como una constante—, que es lo que m24 te hizo estimar a mano.»
  - S031 [31w] «qué fracción del capital arriesgar por operación, derivada de la ventaja medida en lugar de fijada por regla, del tipo de la fórmula de Kelly—, sobre el porcentaje fijo de m22.»
  - S035 [31w] «un modelo que decide en qué estado está el mercado antes de aplicar la regla que corresponde a ese estado—, los ciclos de volatilidad de m16 medidos en vez de vistos.»
  - S039 [40w **aside-only** (22w without asides)] «Lo que sigue valiendo dentro de él es lo de siempre —una ventaja medida, un tamaño que sobrevive a la racha, un criterio de abandono escrito antes de necesitarlo—, y por eso este curso va primero aunque no lleve allí.»
  - S040 [55w] «El vecino natural son las opciones. m21-l2 ya las nombró —los vencimientos grandes concentran flujo forzado en el perpetuo— y allí mismo declaró la frontera: la mecánica de una opción, cómo se dimensiona una cobertura y por qué cambia al moverse el precio, es un segundo curso y no una nota al pie de este.»
  - S042 [41w] «Lo que cambia al pasar de un instrumento a otro es la forma en que se gana y se pierde dinero; lo que no cambia es que hay que saber, antes de abrir, cuánto puedes perder y qué te haría cerrar.»
  - S044 [43w] «Ahí fuera hay un ecosistema entero esperándote: grupos de señales, canales VIP, gente que se ofrece a operar tu cuenta y el curso que sí promete, el que pone el win rate que este curso se ha negado a poner en ninguna lección.»
  - S048 [37w] «Una señal que no puede contestar eso es la misma afirmación sin mecanismo que m34 desmontó en el dialecto de la masa, con otro disfraz, y se responde igual: si ninguna observación la contradice, no predice nada.»
  - S051 [47w] «Eso no convierte a nadie en un estafador —un negocio puede ser honesto y tener sus incentivos igual—, pero es un dato, y es un dato que ya sabes leer, porque es la misma pregunta de siempre aplicada a una persona en vez de a un nivel.»
  - S055 [51w] «Lo que te llevas del curso es leer un gráfico por su mecanismo y no por su forma, dimensionar desde el stop y validar un proceso antes de pagarlo, pero lo más valioso es lo que menos se parece a una técnica: distinguir una afirmación con mecanismo de una sin él.»
  - S056 [32w] «El curso no te ha dado experiencia, así que el camino por defecto es quedarte donde estás y hacerlo más veces, dejando crecer el diario hasta que la muestra pueda decir algo.»
  - S057 [42w] «Resiste la tentación del día siguiente de coleccionar más tácticas, que es el sobreajuste en forma humana, y lee cada señal que te vendan —y los incentivos de quien te la vende— con la misma pregunta que le harías a un nivel.»
- **9 Course-coined term** (2)
  - S040 [flujo forzado [seed]] «El vecino natural son las opciones. m21-l2 ya las nombró —los vencimientos grandes concentran flujo forzado en el perpetuo— y allí mismo declaró la frontera: la mecánica de una opción, cómo se dimensiona una cobertura y por qué cambia al moverse el precio, es un segundo curso y no una nota al pie de este.»
  - S048 [non-seed "dialecto de la masa"] «Una señal que no puede contestar eso es la misma afirmación sin mecanismo que m34 desmontó en el dialecto de la masa, con otro disfraz, y se responde igual: si ninguna observación la contradice, no predice nada.»
- **10 Metaphor then gloss** (1)
  - S024 ["añadir mandos a un sistema" glossed by S025 (el sobreajuste de m28 en versión humana)] «Fíjate en lo que eso es en realidad: añadir mandos a un sistema cuya muestra no ha crecido.»
- **11 Synonym rotation** (1)
  - S027 [the next discipline: escaleras (S027), edificios distintos (S027), otra profesión (S036), nivel dos / planta baja (S038)] 
- **A absolutes** (3)
  - S039 [siempre] «Lo que sigue valiendo dentro de él es lo de siempre —una ventaja medida, un tamaño que sobrevive a la racha, un criterio de abandono escrito antes de necesitarlo—, y por eso este curso va primero aunque no lleve allí.»
  - S049 [siempre] «Y hay un mecanismo que puedes leer siempre, incluso cuando te esconden el de la estrategia: el de quien te la vende.»
  - S051 [siempre] «Eso no convierte a nadie en un estafador —un negocio puede ser honesto y tener sus incentivos igual—, pero es un dato, y es un dato que ya sabes leer, porque es la misma pregunta de siempre aplicada a una persona en vez de a un nivel.»

**EN** — 44 hits, 57 sentences, density 77.2

- **1 Filler** (10)
  - S011 [extra: "And now the limit, with the same frankness" announcer] «And now the limit, with the same frankness.»
  - S013 [exactly: emphatic] «What this course has given you is the criteria to accumulate that experience without ruining yourself while you accumulate it — a size that survives a bad streak, a stop decided before the entry, a journal that turns a trade into a data point instead of a memory — and that is exactly what separates someone who will reach a thousand trades from someone who stops at twenty.»
  - S017 [exactly: emphatic] «The journal m27-l2 made you start is the only thing that turns screen time into sample, and sample is exactly what m28 demanded before anything could be said about your system.»
  - S021 [exactly: emphatic] «The app lets you un-mark a completed lesson for exactly this, without losing anything else you have done.»
  - S022 [extra: "And now the warning that protects everything above" announcer] «And now the warning that protects everything above, because it is the classic mistake of the day after finishing a course: the temptation is to look for more tactics.»
  - S024 [actually: emphatic] «Notice what that actually is: adding knobs to a system whose sample has not grown.»
  - S024 [extra: "Notice" announcer] «Notice what that actually is: adding knobs to a system whose sample has not grown.»
  - S027 [genuine: emphatic] «If at some point you want to climb a genuine step up, there are two ladders, and this course is the first rung of neither: they are different buildings.»
  - S036 [honesty: announcer] «The honesty that matters here: it is another profession.»
  - S043 [extra: "One thing is left to say" announcer] «One thing is left to say, and it is needed the same day you finish the course.»
- **2 Rhythmic triad** (4)
  - S004 [frame: You can… (S004) / You can… (S005) / You know… (S006) / And you can… (S007) — repeated opener] «You can read a chart by mechanism rather than by shape: which orders are resting at a level and why they pile up there, what forced selling does to a thin book, what a candle hides when you look at it as the aggregate it is.»
  - S023 [another pattern / another indicator / another setup — drop "another setup with a name of its own"] «Another pattern, another indicator, another setup with a name of its own.»
  - S037 [code / statistics / data — drop "data"] «Where this course put eyes and process, that ladder puts code, statistics and data, and all three are learned elsewhere.»
  - S052 [the hurry / the FOMO / someone else's streak… — drop "the hurry"] «And the whole of that ecosystem is built on the psychology m26 describes: the hurry, the FOMO, someone else's streak seen up close and your own seen from far away.»
- **4 Summary/uplift closer** (7)
  - S003 [editorial] «Without inflating any of it: a course that overstates what it taught leaves you badly prepared for the first thing that happens after you finish it.»
  - S010 [restate] «Techniques expire when the market that produced them changes; the criterion does not.»
  - S013 [motivate] «What this course has given you is the criteria to accumulate that experience without ruining yourself while you accumulate it — a size that survives a bad streak, a stop decided before the entry, a journal that turns a trade into a data point instead of a memory — and that is exactly what separates someone who will reach a thousand trades from someone who stops at twenty.»
  - S026 [restate] «More tactics over the same sample is not more system; it is less.»
  - S028 [editorial] «Naming them is more use than pretending they are not there.»
  - S039 [editorial] «What still holds inside it is what always held — a measured edge, a size that survives the streak, an abandonment criterion written before you need it — which is why this course comes first even though it does not lead there.»
  - S054 [motivate: last prose sentence] «Choose your timeframe, size from the stop, write before you look, and may the only closing bell you get remain the one you build yourself.»
- **5 Sentence over 30 words** (19)
  - S004 [46w] «You can read a chart by mechanism rather than by shape: which orders are resting at a level and why they pile up there, what forced selling does to a thin book, what a candle hides when you look at it as the aggregate it is.»
  - S005 [37w] «You can size a position from the distance to the stop rather than from the leverage (m22), which means you know what you can lose before you open it, and that the number is one you choose.»
  - S009 [45w] «It is the question this course has repeated in every module — which orders are there, who put them there, what forces them to fill — and it is the only one that keeps working on material this course does not cover, including material written next year.»
  - S012 [35w] «The course has not given you experience, and it cannot: knowing how a thin book behaves at 3 a.m. on a Sunday is not the same as having had a position open at that hour.»
  - S013 [66w] «What this course has given you is the criteria to accumulate that experience without ruining yourself while you accumulate it — a size that survives a bad streak, a stop decided before the entry, a journal that turns a trade into a data point instead of a memory — and that is exactly what separates someone who will reach a thousand trades from someone who stops at twenty.»
  - S017 [31w] «The journal m27-l2 made you start is the only thing that turns screen time into sample, and sample is exactly what m28 demanded before anything could be said about your system.»
  - S025 [50w] «It is m28's overfitting in human form — the same act of fitting the noise, performed with a career instead of a spreadsheet — and it has the same symptom: every bad streak produces a new rule, so no rule ever accumulates the trades it would take to know whether it helped.»
  - S030 [35w] «the fee, the slippage and the impact your own order has on the price, each as a function of order size rather than as a constant — which is what m24 had you estimate by hand.»
  - S031 [31w] «what fraction of capital to risk per trade, derived from the measured edge instead of fixed by rule, of the kind the Kelly formula gives — over the fixed percentage of m22.»
  - S039 [40w **aside-only** (23w without asides)] «What still holds inside it is what always held — a measured edge, a size that survives the streak, an abandonment criterion written before you need it — which is why this course comes first even though it does not lead there.»
  - S040 [53w] «The natural neighbour is options. m21-l2 already named them — large expiries concentrate forced flow into the perpetual — and declared the frontier in the same breath: the mechanics of an option, how a hedge is sized and why it changes as price moves, are a second course and not a footnote in this one.»
  - S042 [40w] «What changes from one instrument to another is the shape of how money is made and lost; what does not change is that you have to know, before you open, what you can lose and what would make you close.»
  - S044 [44w] «Out there is an entire ecosystem waiting for you: signal groups, VIP channels, people offering to trade your account, and the course that does promise — the one that puts a number on the win rate this course has refused to put in any lesson.»
  - S048 [41w] «A signal that cannot answer that is the same claim without a mechanism that m34 took apart in the crowd's dialect, wearing a different costume, and it is answered the same way: if no observation would contradict it, it predicts nothing.»
  - S050 [35w] «Someone who lives off selling you the signal is paid when you subscribe, not when you win; someone paid a share of the volume you move is paid by your activity, not by your result.»
  - S051 [47w] «That makes nobody a fraud — a business can be honest and still have its incentives — but it is a fact, and it is a fact you already know how to read, because it is the same old question applied to a person instead of to a level.»
  - S055 [56w] «What you take from the course is the ability to read a chart by mechanism rather than by shape, to size from the stop, and to validate a process before paying for it — but the most valuable possession is the one that looks least like a technique: telling a claim with a mechanism from one without.»
  - S056 [31w] «The course has not given you experience, so the default path is to stay where you are and do it more times, growing the journal until the sample can say something.»
  - S057 [39w] «Resist the day-after temptation to collect more tactics, which is overfitting in human form, and read every signal sold to you — and the incentives of whoever is selling it — with the same question you would ask of a level.»
- **9 Course-coined term** (2)
  - S040 [forced flow [seed]] «The natural neighbour is options. m21-l2 already named them — large expiries concentrate forced flow into the perpetual — and declared the frontier in the same breath: the mechanics of an option, how a hedge is sized and why it changes as price moves, are a second course and not a footnote in this one.»
  - S048 [non-seed "the crowd's dialect"] «A signal that cannot answer that is the same claim without a mechanism that m34 took apart in the crowd's dialect, wearing a different costume, and it is answered the same way: if no observation would contradict it, it predicts nothing.»
- **10 Metaphor then gloss** (1)
  - S024 ["adding knobs to a system" glossed by S025 (m28's overfitting in human form)] «Notice what that actually is: adding knobs to a system whose sample has not grown.»
- **11 Synonym rotation** (1)
  - S027 [the next discipline: ladders (S027), different buildings (S027), another profession (S036), level two / ground floor (S038)] 
- **A absolutes** (2)
  - S039 [always] «What still holds inside it is what always held — a measured edge, a size that survives the streak, an abandonment criterion written before you need it — which is why this course comes first even though it does not lead there.»
  - S049 [always] «And there is one mechanism you can always read, even when the strategy's own is kept from you: the mechanism of whoever is selling it to you.»

## Pilot proposal

I propose two modules: **m08-l1** (slot 1, from the 10 worst) and **m27-l1** (slot 2, m20 or later, with risk
rules). Hit counts below are ES · EN, pattern by pattern, from the table above. "Sentences that would change"
counts the distinct sentences carrying a pattern 1–7, 9 or 10 hit (8 and 11 are lesson-level and change
through those). "Risky" means sentences among them that state a rule, a quantity or a direction. The rewrites
are proposals to judge the voice by. None of them is applied.

### Slot 1: m08-l1 (Estructura de precio)

**Why this one.** It ranks 3rd by density with every pattern counted and **1st without pattern 5**
(52.9). So it is the lesson most shaped by voice tics rather than by long sentences. It is also where the
two biggest coined terms live: «escalera» (11 of the course's 20 ES uses) and «estante» (4). It adds
«asomo» and three rhetorical questions. A pilot here tests the hardest thing in pass 1.2, which is
replacing a term the lesson is built around, in the lesson later modules point back to (m23-l2 and m34-l1 cite «la escalera de m08-l1»).

| Pattern | 1 | 2 | 3 | 4 | 5 [aside-only] | 6 | 7 | 8 | 9 | 10 | 11 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| m08-l1 | 13·13 | 3·3 | 3·3 | 11·11 | 27·22 [8·7] | 0·0 | 0·0 | 0·0 | 19·19 | 2·2 | 3·4 | 81·77 |

**Sentences that would change:** 51 of 103 (ES), 49 of 103 (EN). That includes 8 · 7 aside-only splits,
which change no words.

**Risky to rewrite** (ES ids; EN in brackets where they differ). These carry levels, the trend definition or
the close-vs-wick rule:
- **Figure-anchored numbers.** S037, S039 (2.130, 2.166, 2.035). `fig-m08-breakout-vs-fakeout` checks
  these against the generated panels within 1%, and S037's «literalmente el mismo gráfico … hasta el momento
  de la decisión» is the claim behind its `identical_through` test. Keep the numbers and the
  «mismo gráfico» claim; drop only «literalmente».
- **The ladder numbers.** S052, S066 (100 / 110 / 104 / 118 / 109 / 126, then 106). The coupling file says
  these round numbers ARE the teaching. S073 carries the guard phrase «instancia generada», which must
  survive.
- **Definitions with direction.** S044 (HH/HL), S045–S046 (LH/LL), S053, S059 («una tendencia sigue intacta
  mientras…»), S066 (CHoCH = the first lower low).
- **Levels.** S018 (58.050 / 58.600 / 58.300 / 58.150), S020 (58.000–58.400).
- **Rules.** S092 («el cierre, nunca el extremo»), S080 («la primera vela pasada un nivel es la vela más
  cara de operar»), S084 (wait for the second break), S089–S090 (where stops cluster), S088 (the 4 a.m.
  Sunday break).
- EN only: S033, S073, S090, S103 carry the same content and also need care.

**The three I would rewrite first.**

1. **Rhetorical question + coined term + editorial closer** (S047–S051, pattern 3, 9, 4). Before:

   > ¿Para qué molestarse en nombrar la escalera? Porque la secuencia te dice quién va ganando sin
   > preguntarle a ningún indicador. […] En cuanto la escalera se detiene, se detiene también la
   > suposición.

   After:

   > La secuencia de máximos y mínimos te dice quién va ganando sin preguntarle a ningún indicador. […]
   > Cuando la secuencia se interrumpe, esa suposición deja de valer.

   EN: «The sequence of highs and lows tells you who is winning without asking any indicator. […] When the
   sequence breaks off, that assumption stops holding.»

   *Risk:* low. «Se interrumpe» stays as general as «se detiene». It does not turn the sentence into «the
   first lower low», which S066 teaches separately as the CHoCH.

2. **Coined term + metaphor gloss** (S012–S013, pattern 9, 10). Before:

   > Un soporte no es magia en el número: es un estante de órdenes de compra en reposo que las últimas
   > visitas enseñaron a la gente a dejar. La resistencia es el mismo estante, hecho de órdenes de venta.

   After:

   > Un soporte no es magia en el número: es una zona con órdenes de compra en reposo, que las últimas
   > visitas enseñaron a la gente a dejar ahí. La resistencia es lo mismo con órdenes de venta.

   EN: «A support is not magic in the number: it is a zone of resting buy orders that the last few visits
   taught people to leave there. Resistance is the same thing with sell orders.»

   *Risk:* low. «Zona» is the word the lesson tells the reader to keep (S006), so this also removes one
   name from the S/R rotation (zona / estante / banda / nivel).

3. **Fillers + closer + long sentence on a rule** (S092, pattern 1 ×2, 4, 5). Before:

   > Por eso la mecha que asoma por tu nivel suele ser más larga y más traicionera en cripto que la versión
   > de manual, y por eso el cierre, nunca el extremo, es la única lectura honesta de si un nivel rompió de
   > verdad.

   After:

   > Por eso, en cripto, la mecha que perfora tu nivel suele ser más larga que en los manuales. Para saber
   > si un nivel ha roto, mira el cierre, nunca el extremo.

   EN: «That is why, in crypto, the wick through your level is often longer than in the textbooks. To
   judge whether a level broke, read the close, never the extreme.»

   *Risk:* **medium**. This is a rule. The words «el cierre, nunca el extremo» stay verbatim, the single
   hedge «suele / often» stays, and «traicionera / nastier» goes because the length is the fact. Check this
   one closely.

**Alternative for slot 1: m19-l2** (Mapas de liquidez y squeezes). It ranks 4th, and 2nd without
pattern 5. It is the densest lesson for seed terms (repisa ×9, bolsa ×6, combustible ×4, flujo forzado
×2, plus «arder»), and almost all of its other hits are fillers and closers. Choose it if you would rather
pilot the term sweep on mechanics than on the foundational trend lesson. Its risk is the liquidation
arithmetic in S047–S050 (3.000 / 3.050 / 3.150 / 3.300).

### Slot 2: m27-l1 (Anatomía de una operación completa)

**Why this one.** It is the course's worked plan, and every risk rule in it is concrete: 1% of 10.000 = 100
USDT, size from the stop, break-even only on a structural test, partials at +2R, a daily limit of X = 2%
(1–3%), and a reset hour. It mixes all three kinds of rewrite the pass will meet on rules: coined terms
(«freno diario», «marco macro / micro», «lente»), fillers wrapped around quantities («exactamente +2R»,
«justo la operación»), and long sentences that are long only because of asides. Its density (52.0, rank 18 of 44)
is mid-course, so it also tests whether the voice holds on a lesson that is not obviously bad.

| Pattern | 1 | 2 | 3 | 4 | 5 [aside-only] | 6 | 7 | 8 | 9 | 10 | 11 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| m27-l1 | 13·12 | 2·2 | 0·0 | 6·6 | 22·16 [5·3] | 0·0 | 0·0 | 0·0 | 9·5 | 3·2 | 4·4 | 59·47 |

**Sentences that would change:** 41 of 102 (ES), 33 of 102 (EN). The ES/EN gap is the four ES-only «freno
diario» hits plus six more long ES sentences.

**Risky to rewrite** (ES ids). These hold the rule, the number or the direction. 30 of the 41 changed ES
sentences touch one:
- **Sizing and risk budget.** S004–S005 (10.000 USDT, 1% = 100), S056 (size from the stop, never the
  reverse), S101 (risk budget ÷ stop distance), S097.
- **Direction and timeframe order.** S014 (the higher timeframe sets the bias and the lower the entry; not
  reversible), S021–S022 (a 1-hour long inside a daily downtrend is rejected), S032 (59.700 / 60.300).
- **Stop management.** S040 (below 59.300 the thesis is false), S061 (break-even only after a new HH and
  then an HL), S064 (60.600), S066 («el stop se queda donde lo puso el plan»).
- **Targets and partials.** S068 (62.300 = +2R, 40% / 60%, stop to 60.300, 64.000), S072 (+0,8R), S081
  (+3,7R ≈ +370 USDT / +3,0R ≈ +300 USDT).
- **The daily limit.** S084–S089 (X = 2%, 200 USDT, two −1R losses, 1–3%, «nunca durante él»), S091
  (−3%), S098 (00:00 UTC), S099 (−2%, 3 a.m.).
- Summary S100–S102. The guard phrase «setup generado / generated setup» (`fig-m27-trade-anatomy`) must
  survive.

**Coupling to settle before the pilot.** «Freno diario» is the ES term of the glossary entry
`g-daily-stop` (origin m27-l1), and it is also in g-overtrading's definition, in m22-l1, in the m27-l1
heading and in its summary. Replacing it in m27-l1 alone would leave the glossary term absent from its
own origin lesson, which the never-coins guard refuses. So either the pilot takes the rename end to end
(glossary + m22-l1 + heading + summary), or the pilot leaves «freno diario» for the course-wide term sweep.
I would take it in the pilot: it is one entry and two lessons, and it shows how the sweep will go.

**The three I would rewrite first.**

1. **Coined term + metaphor gloss** (S084, pattern 9, 10). Before:

   > Así que el plan lleva un segundo límite, separado: un freno diario, que es el límite de pérdida diaria
   > de m26 hecho mecánico.

   After:

   > Así que el plan lleva un segundo límite, separado: un límite de pérdida diaria. Es la regla de m26,
   > fijada como un número.

   EN (keeps the standard «daily stop»): «So the plan carries a second, separate limit: a daily stop. It is
   m26's daily loss limit, fixed as a number.»

   *Risk:* low on content. The coupling above is the real cost.

2. **Coined labels + filler + long sentence on a direction rule** (S022, pattern 9, 1, 5). Before:

   > Así que una señal del marco micro que contradice el sesgo macro es una operación descartada, no una
   > oportunidad de operar en contra: un largo limpio en 1 hora dentro de una tendencia bajista diaria es
   > justo la operación que este protocolo existe para rechazar.

   After:

   > Así que una señal en la temporalidad inferior que contradice el sesgo de la superior es una operación
   > descartada, no una oportunidad de operar en contra. Un largo limpio en 1 hora dentro de una tendencia
   > bajista diaria es la operación que este paso rechaza.

   EN: «So a lower-timeframe signal that contradicts the higher-timeframe bias is a skipped trade, not a
   chance to trade against it. A clean 1-hour long inside a daily downtrend is the trade this step
   rejects.»

   *Risk:* **medium**. This is a direction rule. «Largo», «1 hora» and «bajista diaria» stay untouched.
   «Temporalidad superior / inferior» is the pair S014 already uses, so the lesson goes from four names per
   timeframe to one.

3. **Aside-only split on a quantity rule** (S089, pattern 5, aside-only). Before:

   > La X la eliges tú, típicamente entre el 1 y el 3% (los estilos rápidos que hacen más operaciones al día
   > pertenecen a la parte baja), y se fija en el plan, antes del día malo, nunca durante él.

   After:

   > La X la eliges tú, normalmente entre el 1 y el 3%. Los estilos rápidos, que hacen más operaciones al
   > día, van en la parte baja. Se fija en el plan, antes del día malo, nunca durante él.

   EN: «You pick the X, typically 1–3%. Faster styles, which take more trades a day, belong at the low end.
   It is set in the plan, before the losing day, never adjusted during one.»

   *Risk:* low. This is a split with no new words. «1 y el 3%», «parte baja» and «nunca durante él» stay
   verbatim. It shows what pattern 5's aside-only class looks like when done.

**Alternative for slot 2: m22-l1** (Gestionar el riesgo). It is the core risk-rule lesson
(sizing from the stop, the drawdown asymmetry, the risk dial), with 125 sentences and almost no coined
terms (1 ES). Its hits are mostly fillers (14 · 13), closers (9 · 9) and long sentences (26 · 18), so it
tests the voice on pure rules without the term sweep mixed in. 30 of its 43 changed ES sentences touch a
number or a rule, the same share as m27-l1.

### What happens after you pick

Next session: rewrite the two modules, ES and EN together, on the voice page. Keep every risky sentence's
numbers, directions and «nunca / siempre» words byte-identical unless you approve a change. Then
regenerate `glossary-links.*.txt` and `lesson-refs.*.txt`, run the figure-coupling, glossary and bundle
checks and the backend and frontend suites, and log any phrasing the editor itself introduced to the voice
page's blacklist.
