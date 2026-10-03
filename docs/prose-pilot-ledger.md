# Prose pass 1.2, P1 pilot ledger: m08-l1 and m27-l1

2026-10-03. Nothing is committed. Sentence ids (`S###`) are the inventory's (`docs/prose-inventory.md`,
taken at `f0d0e68`). For new sentences produced by a split, `S018a/b` etc.

## What changed, in one place

| File | Change |
| --- | --- |
| `content/es/lessons/m08-l1.md`, `content/en/lessons/m08-l1.md` | full voice rewrite |
| `content/es/lessons/m27-l1.md`, `content/en/lessons/m27-l1.md` | full voice rewrite; ES heading «El freno diario: …» → «El límite de pérdida diaria: …» |
| `content/es/lessons/m22-l1.md` | «freno diario» → «límite de pérdida diaria» (one sentence, term only) |
| `content/glossary.yaml` | `g-daily-stop` ES term → «límite de pérdida diaria» (EN «daily stop» kept, no `match` added); the ES definition of **`g-revenge-trading`** (see note 4) |
| `content/course.yaml` | m27-l1 ES summary: «un freno diario fijado» → «un límite de pérdida diaria fijado». Nothing else |
| `content/figure-coupling.yaml` | `fig-m08-market-structure.why`: «ladder» ×3 and «staircase» → «sequence (of higher highs and higher lows)» / «structure» |
| `content/glossary-links.{es,en}.txt` | regenerated (below) |
| `content/lesson-refs.{es,en}.txt` | regenerated; **context text only** (below) |
| `docs/prose-pilot-ledger.md` | this file |

### Verification

| Check | Result |
| --- | --- |
| `export_bundle.py` (format 2) | exit 0; text diff 0; block inventory OK (88 ASTs); exercise refs OK (242 marks). Fingerprint `9e7facd5…` → **`47ad8a49…`** |
| Bundle files that moved | `ast/{es,en}/m08-l1.json`, `ast/{es,en}/m27-l1.json`, `ast/es/m22-l1.json`, **`ast/es/m26-l1.json`** (new glossary mark, note 6), `ast/index.json` (mark/emphasis counts), `figure-coupling.yaml` (the bundle ships a copy of the coupling YAML, so the note edit shows here), `glossary/glossary.es.json`, `manifest.json` (fingerprint, file hashes, the m27-l1 ES summary), `reading-seconds.json`. Everything else byte-identical |
| `reading-seconds.json` | m08-l1 ES 799 → 773, EN 728 → 710; m27-l1 ES 806 → 790, EN 745 → 731; m22-l1 ES 883 → 884 |
| `export_generation_goldens.py` | `exercise-mode.tsv`, `figures.tsv`, `formatter-cases.tsv`, `configs/`: **zero diff** |
| `glossary-links.*.txt` | every (lesson, term) pair the same as at HEAD except **one added**: ES `m23-l1 g-daily-stop` (m26-l1). Header counts: ES 1053 → 1054 marks, EN 1117 unchanged |
| `lesson-refs.*.txt` | every (lesson, target, kind, key) row the same as at HEAD; only the quoted context changed (m08-l1 → m15-l1, m22-l1 → m27-l1, m27-l1 → m03-l2 / m08-l2 / m26 ×3 / m27-l2). This file was not on your list of expected changes, but it cannot stay byte-identical when a sentence next to a module reference changes |
| figure/prose coupling | `test_figure_prose_coupling.py` passes. All anchored numbers (2.130, 2.225, 2.166, 2.035) are still printed. Guard phrases «instancia generada» / «generated instance» and «setup generado» / «generated setup» survive on one line each (the test does a raw substring match, so a hard wrap inside them would fail it) |
| Numbers / absolutes per file | Every number token in all four lesson files is the same multiset as before; «nunca / siempre / debe…» and «never / always / must» counts are unchanged (ES m08 3, ES m27 7, EN m08 4, EN m27 6) |
| `::` blocks | directives byte-identical in all four files; `:::note` blocks byte-identical except the two «freno diario» in ES m27-l1 (note 3) |
| backend `pytest` / frontend `vitest` | **1300 passed, 20 skipped** / **458 passed, 1 skipped** (same as round 7), run on the final text; this includes `test_figure_prose_coupling.py`, `test_glossary.py` (never-coins guard) and both report tests |

## Notes and judgement calls (read these first)

1. **«asomo» in m08 S039 is not «la primera vela que cruza el nivel».** «el mismo asomo llega a 2.166» refers to the
   fakeout's *highest* point (the coupling anchor is `high:122`, «the fakeout's furthest poke»), several candles after
   the first break. «la primera vela que cruza el nivel llega a 2.166» would be false. I wrote «la misma ruptura llega a
   2.166» / «the same break reaches 2.166». The other two «asomo» (S035, S077, S078) use the decided form.
2. **«combustible» (m08 S035) replaced although it was not on your rename list.** The inventory's proposal for m08-l1
   is «stops y órdenes de ruptura». The antecedent is the orders of S034, so I wrote «Cuando esas órdenes se agotan» /
   «Once those orders are spent». Revert if you want «combustible» left for the course-wide sweep.
3. **«freno diario» appeared twice inside the m27-l1 `:::note{type=warning}`.** I renamed the term there and changed
   nothing else in the note. Leaving it would have put the old term next to the new heading.
4. **The brief says «g-overtrading ES definition»; the sentence is in `g-revenge-trading`.** `g-overtrading` does not
   mention the term. The definition that said «El freno diario existe para cerrar la sesión…» is `g-revenge-trading`
   (ES «venganza»). I changed that one.
5. **No old-form `match` was added.** The only lesson link to `g-daily-stop` was in m22-l1 and it moves with the
   rename. Exercises are not linked.
6. **New ES-only glossary mark in m26-l1.** ES m26-l1 already said «límite de pérdida diaria» (×3), so it now links to
   `g-daily-stop` (first occurrence: «**La regla:** un límite de pérdida diaria fijo…»). EN m26-l1 says «daily loss
   limit», which does not match EN «daily stop», so this mark exists in ES only. I think this is right (it is the same
   concept), but it is a locale asymmetry.
7. **«freno diario» still exists outside the files you allowed me to touch.** `content/exercises/m27-ex-1.yaml` (stem,
   one option, two explanations), `content/exercises/m27-ex-3.yaml` (one stem), and the **m27 module** summary in
   `course.yaml` (line 1412, «el freno diario que termina un día perdedor»; that is the module, not the lesson). So
   m27-l1's own exercises now use a term the lesson no longer teaches. This needs a decision before or during the full
   pass.
8. **«la escalera de m08-l1» is now a dangling pointer** in m23-l2 (S054, EN S055 «m08-l1's ladder»), m34-l1 (S057
   «donde vive la escalera») and the m34 summary in `course.yaml` (lines 1801, 1809). m08-l1 no longer says
   «escalera». The m08-l1 **summary** still says «estantes / shelves» because `course.yaml` was frozen except for m27.
9. **S089: the approved sample's relative clause was reverted (session 2, at your request).** The sample turned
   the restrictive «los estilos rápidos que hacen más operaciones al día» into an explanatory one («…, que
   hacen…,»), which widened the claim to all fast styles. Now: «Los estilos rápidos que hacen más operaciones al
   día van en la parte baja.» / «Fast styles that take more trades a day belong at the low end.» The rest of the
   approved split («normalmente», «van en», three sentences) stands. Regenerated: text diff 0, goldens identical,
   link and ref pairs unchanged.
10. **EN S084 mirrors your ES change.** ES «convertida en un número» → EN «turned into a number» (the approved EN said
    «fixed as a number»). With that, «convertida en un número» / «turned into a number» appears twice in that section
    (S084 and the old S092 «convertida en un número y un corte duro»).
11. **m27 S069 «es donde tiene que entrar la honestidad» → «es engañosa» / «is misleading».** This is the nearest any
    change comes to adding nuance: the original implies that the phrase misleads, and the new text says it outright.
12. **Two regressions caught by regenerating:** (a) splitting m27 S096 had turned «libros poco profundos» / «thin
    books» into «los libros son poco profundos» / «books are thin», and the `g-thin-book` mark disappeared from m27-l1
    in both locales. Fixed by keeping the exact term («Ese fin de semana transcurre en libros poco profundos…»).
    (b) My first re-wrap also re-flowed eight untouched paragraphs (five inside a `:::note`). All eight were restored
    byte for byte.
13. **Italics:** `*que aguanta*` / `*that holds*` went with the deleted S040, and `*¿ha cambiado de verdad el
    control?*` became `*¿ha cambiado el control?*`. Bold is unchanged apart from the two m27 lead-ins you asked for.

## Hit counts, before → after

Counted the way the inventory counts. Pattern 5 was recounted mechanically with the same splitter, which reproduces
the inventory's before-figures exactly (lesson body 25·20 and 20·14, plus 2 summary sentences each). Summaries were
not edited (frozen), so their hits are included in "after".

**m08-l1** (ES·EN)

| # | Pattern | Before | After | What is left |
|---:|---|---|---|---|
| 1 | Filler | 13·13 | 0·0 | |
| 2 | Rhythmic triad | 3·3 | 1·1 | S009–S011 (three groups; left, see below) |
| 3 | Rhetorical question | 3·3 | 0·0 | |
| 4 | Closer | 11·11 | 4·4 (+3·3 borderline) | left: S006, S053, S069, S080. Borderline: S051, S092, S100 now close their paragraph with the rule in plain words (S051 and S092 are your approved samples) |
| 5 | Over 30 words [aside-only] | 27·22 [8·7] | 4·3 [1·1] | ES S018b (35w, the second half of an aside-only split), S052 (numeric sequence), summary S102, S103; EN S052, S102, S103 |
| 9 | Coined term | 19·19 | 1·1 | summary S101 «estantes / shelves» (course.yaml frozen) |
| 10 | Metaphor then gloss | 2·2 | 0·0 | |
| 11 | Synonym rotation | 3·4 | 3·3 | S/R area (zona / banda / nivel / vecindario), fakeout (fakeout / falsa ruptura / trampas), CHoCH (primera grieta / cambio de carácter / indicio / patrón roto). EN staircase/ladder/sequence is fixed |
| | **Total** | **81·77** | **13·12 (+3·3)** | |

**m27-l1** (ES·EN)

| # | Pattern | Before | After | What is left |
|---:|---|---|---|---|
| 1 | Filler | 13·12 | 0·0 | (the lead-in label «con su precio honesto» / «honestly priced» stays: labels are structure) |
| 2 | Rhythmic triad | 2·2 | 0·0 | |
| 4 | Closer | 6·6 | 1·1 (+2·2 borderline) | left: S093. Borderline: S005 («Todo lo que viene después…» still looks ahead), S012 («Hoy hay un retroceso en una tendencia alcista.» restates S007 but carries the "today, unlike most days" contrast) |
| 5 | Over 30 words [aside-only] | 22·16 [5·3] | 3·3 [1·0] | S024b (list of the three confluence facts, 35w / 29w without the parenthesis), summary S100, S101 |
| 9 | Coined term | 9·5 | 0·0 | |
| 10 | Metaphor then gloss | 3·2 | 0·0 | |
| 11 | Synonym rotation | 4·4 | 2·2 | invalidation (idea muerta / tesis falsa / invalida el setup), daily limit (límite de pérdida diaria / segundo límite / corte duro) |
| | **Total** | **59·47** | **6·6 (+2·2)** | |

## Sentences left alone despite a hit

| Lesson | Sentence | Hit | Why left |
|---|---|---|---|
| m08 | S006 «La palabra que hay que retener es *zona*.» | closer (editorial) | It is an instruction that names the lesson's key word, and S012's approved rewrite leans on it. Deleting it removes the instruction. |
| m08 | S009–S011 (three groups of traders) | triad | Each group is a separate fact: bought the bounce, missed it, underwater. The reviewer's "drop the second" removes a fact. |
| m08 | S014 «—una banda de unas cuantas velas de ancho—», S018 «vecindario», S058 «la primera grieta» | rotation | No other hit in the sentence, or the sentence is aside-only (split, not reworded). «Primera grieta» comes before the term CHoCH is introduced, so swapping in the term would teach it early. |
| m08 | S052 (100 / 110 / 104 / 118 / 109 / 126) | over 30, aside-only | One numeric sequence and a risky sentence. Splitting it would break the sequence the coupling note says IS the teaching. |
| m08 | S053 «…una secuencia que podrías describirle a alguien por teléfono» | closer (editorial) | Only the coined term changed. The tail is why the numbers are round, and the coupling note quotes it. |
| m08 | S069 «Ese vocabulario —y el resto del dialecto…— se mapea… en m34-l1» | closer (ahead) | It carries the cross-reference to m34-l1 (a fact). «Dialecto» is the m34 coined term and belongs to the m34 decision. |
| m08 | S080 «La primera vela pasada un nivel es la vela más cara de operar.» | closer (restate) | Risky rule sentence. The fix for a restate is deletion, which removes the rule. |
| m08 | summary S101–S103 | coined term (estantes), 2 long | `course.yaml` frozen except for m27. |
| m27 | S024b (three confluence facts) | over 30 | A list of three required facts, which the inventory does not count as a triad. One idea. |
| m27 | S061 «temporalidad de ejecución» | rotation | Risky rule sentence. The rule's words stay verbatim. Two names for the lower timeframe is below the 3-name threshold. |
| m27 | S093 «Funciona porque no te consulta…» | closer (restate) | Only «precisamente» was removed. It is the reason the rule works, and the m27-ex-1 explanation echoes it. |
| m27 | invalidation rotation (S018 / S040 / S042) | rotation | No other hit in those sentences. |
| m27 | summary S100–S101 | 2 long | `course.yaml`: only the term rename was allowed. |
| m27 | «lo que hiciste de verdad» (El registro) | — | Not counted by the inventory: it contrasts what you did with what you planned. |

## Phrasings I reused 3+ times (blacklist candidates)

These are shapes I introduced, mostly as the second half of a split:

- **«Es + noun phrase» / "It is… / That is…" as a sentence opener after a split.** ES: «Es el primer mínimo más bajo…»,
  «Es la ruptura que *confirma*…», «Es la regla de m26…», «Es la persona menos cualificada…», «Es una razón más…»,
  «Es este:» (6). EN: «It is the first lower low…», «It is the break that…», «It is m26's daily loss limit…», «That
  is another reason…», «That is m03-l2's warning…», «That is why…» ×2 (7). This is the strongest candidate: it is
  what splitting at a colon or semicolon produces, and the cure is to vary where the split falls, not to rotate words.
- **«Son los… / They are the…»** as a split opener. ES «Son los stops…», «Son los fines de semana…» (2). EN «They are
  the stop-losses…», «They are the weekends…», «They are the least qualified…» (3).
- **«Por eso» / "That is why"** starting a new sentence: ES S087, S092 (approved), S097 (3). EN S087, S092 (2) + «So
  the discipline…».

None of these is a filler by itself. They become a tic at density. Every word I used for a replacement is standard
outside the course; I did not coin anything. «Fiable» (S100) and «directa» (S002) replace «honesta / honesto» where
the original meant *reliable* and *unmediated*.

---

## Reviewer pass: how it was run

After each lesson I re-read every changed sentence against its "before" with five questions. **R**: did a rule,
quantity or direction change? **F+**: was a fact added? **F−**: was a fact removed? **G**: did a glossary term change
form or leave the lesson? **C**: is a coined term left? A row is **PASS** when all five are "no". A note after
"PASS —" records the closest call. Pattern codes follow the inventory: 1 filler, 2 triad, 3 rhetorical question,
4 closer, 5 over 30 words (5a = aside-only), 9 coined term, 10 metaphor then gloss, 11 rotation.

**Rows that failed review and were fixed before this ledger:**

| Where | What the review found | Fix |
|---|---|---|
| m08 S039 (both) | The decided «la primera vela que cruza el nivel» for «asomo» would say the *first* candle reached 2.166. That is false: 2.166 is the fakeout's furthest high. (R) | «la misma ruptura» / «the same break» |
| m27 S096 (both) | My split rewrote «libros poco profundos» / «thin books», and `g-thin-book` left m27-l1. (G) | the exact term restored |
| m08 S035, S067; m27 S091 (both) | My renames and splits had left three sentences at 31–33 words, so they still hit pattern 5 | split once more at the existing clause boundary |

### m08-l1 — ES

| Id | Before | After | Patterns | Review |
|---|---|---|---|---|
| S002 | Deja un registro visible de dónde pelearon compradores y vendedores, y ese registro —la estructura— es la lectura de gráfico más honesta que puedes hacer, porque es el precio en sí, no un indicador derivado de él. | Deja un registro visible de dónde pelearon compradores y vendedores. Ese registro es la estructura, y es la lectura de gráfico más directa que puedes hacer: es el precio en sí, no un indicador derivado de él. | 1, 5 | PASS — «honesta» → «directa»: the reason clause («es el precio en sí») already says what "honest" meant |
| S003 | Todo lo de esta lección es una forma de leer ese registro: dónde se frenó el precio, dónde rompió y si las rupturas significaron algo. | Leer ese registro es ver dónde se frenó el precio, dónde rompió y si las rupturas significaron algo. | 4 (ahead) | PASS — the three questions stay; only the scope frame goes |
| S007–S008 | ¿Por qué la compra reaparece de forma fiable en el mismo sitio? Porque el sitio se recuerda, y el recuerdo se convierte en órdenes. | La compra reaparece de forma fiable en el mismo sitio porque el sitio se recuerda, y el recuerdo se convierte en órdenes. | 3 | PASS |
| S012–S013 | Un soporte no es magia en el número: es un estante de órdenes de compra en reposo que las últimas visitas enseñaron a la gente a dejar. La resistencia es el mismo estante, hecho de órdenes de venta. | Un soporte no es magia en el número: es una zona con órdenes de compra en reposo, que las últimas visitas enseñaron a la gente a dejar ahí. La resistencia es lo mismo con órdenes de venta. | 9, 10 | PASS (approved sample) |
| S018 | Caso concreto: supón que BTC ha girado al alza tres veces en el mismo vecindario —una vez pinchó con la mecha hasta 58.050 y cerró de vuelta en 58.600, otra vez hizo base en torno a 58.300 durante varias velas, otra cayó a 58.150 en el intradía y se recuperó—. | Caso concreto: supón que BTC ha girado al alza tres veces en el mismo vecindario. Una vez pinchó con la mecha hasta 58.050 y cerró de vuelta en 58.600, otra vez hizo base en torno a 58.300 durante varias velas, otra cayó a 58.150 en el intradía y se recuperó. | 5a | PASS — split only; risky (levels) |
| S020 | Hay un estante de unos 58.000–58.400 de ancho. | Hay una zona de unos 58.000–58.400 de ancho. | 9 | PASS — risky (levels) |
| S021 | Traza la zona a partir de los cuerpos y mechas de los swings que de verdad giraron, y espera que el precio reaccione *en algún punto dentro de ella*, no en un número exacto. | Traza la zona a partir de los cuerpos y mechas de los swings que giraron. Espera que el precio reaccione *en algún punto dentro de ella*, no en un número exacto. | 1, 5 | PASS |
| S024 | Una ruptura genuina cierra con decisión más allá del nivel —un cuerpo de vela entero al otro lado— y luego aguanta ahí, idealmente volviendo a *retestear* el antiguo nivel como nuevo soporte (o resistencia) y rebotando. | Una ruptura genuina cierra con decisión más allá del nivel —un cuerpo de vela entero al otro lado— y luego aguanta ahí. Idealmente, vuelve a *retestear* el antiguo nivel como nuevo soporte (o resistencia) y rebota. | 5a | PASS — split; the gerunds became finite verbs, which is the least a split needs |
| S029 | Ambos tienen un mecanismo, y conviene entenderlo en vez de memorizarlo. | *(deleted)* | 1 (announcer) | PASS — an exhortation, not a fact; the mechanisms follow |
| S030 | Una ruptura genuina suele retestear y aguantar por *inversión de roles*: los vendedores que defendían la antigua resistencia han sido arrollados y muchos cierran sus cortos en el retroceso hacia el nivel, convirtiendo a los antiguos vendedores en compradores; mientras tanto, los compradores que se negaron a perseguir el precio consiguen por fin su entrada en la antigua línea. | Una ruptura genuina suele retestear y aguantar por *inversión de roles*. Los vendedores que defendían la antigua resistencia han sido arrollados, y muchos cierran sus cortos en el retroceso hacia el nivel: los antiguos vendedores pasan a ser compradores. Mientras tanto, los compradores que se negaron a perseguir el precio consiguen por fin su entrada en la antigua línea. | 5 | PASS |
| S032 | El retest es el mercado votando por segunda vez. | *(deleted)* | 4 (editorial) | PASS — a metaphor closer; S031 states the fact |
| S033 | Un fakeout ocurre porque el nivel obvio es exactamente donde se apilan las órdenes en reposo justo más allá de él: los stops de los traders posicionados contra el nivel, y las órdenes de compra de los traders de ruptura que dejan instrucciones de "compra si rompe". | Un fakeout ocurre porque las órdenes en reposo se apilan justo más allá del nivel obvio. Son los stops de los traders posicionados contra el nivel y las órdenes de compra de los traders de ruptura, que dejan instrucciones de "compra si rompe". | 1, 5 | PASS |
| S035 | Cuando ese combustible se agota, el precio cae de vuelta dentro, y quienes compraron el asomo quedan ahora atrapados por encima del nivel y motivados para vender. | Cuando esas órdenes se agotan, el precio cae de vuelta dentro. Quienes compraron la primera vela que cruza el nivel quedan ahora atrapados por encima del nivel y motivados para vender. | 9 ×2 | PASS — «combustible» was not on the decided list (note 2) |
| S036 | La falsa ruptura no falló por accidente: se quedó sin las mismas órdenes que la provocaron. | *(deleted)* | 4 (restate) | PASS — S033–S035 carry the mechanism |
| S037 | En concreto, con los números de la figura de abajo: la resistencia está en torno a 2.130, y los dos paneles son literalmente el mismo gráfico —el mismo rango, las mismas velas— hasta el momento de la decisión. | En concreto, con los números de la figura de abajo: la resistencia está en torno a 2.130. Los dos paneles son el mismo gráfico —el mismo rango, las mismas velas— hasta el momento de la decisión. | 1, 5 | PASS — risky (`identical_through` claim intact) |
| S039 | A la derecha, un fakeout: el mismo asomo llega a 2.166, aguanta media docena de velas por encima y luego las pierde —cierra de vuelta bajo 2.130, pierde 2.035 en pocas velas y sigue cayendo desde ahí—. | A la derecha, un fakeout: la misma ruptura llega a 2.166, aguanta media docena de velas por encima y luego las pierde. Cierra de vuelta bajo 2.130, pierde 2.035 en pocas velas y sigue cayendo desde ahí. | 9, 5a | FAIL → fixed (note 1); risky |
| S040 | Mismo nivel, mismas primeras velas: solo el cierre *que aguanta* y lo que viene después los distinguen. | *(deleted)* | 4 (restate) | PASS — S041 states the close-and-hold rule; S038–S039 show what follows |
| S042 | Una mecha que atraviesa un nivel es un rumor; unas pocas velas cerrando al otro lado son un titular sin confirmar —el panel de la derecha las tiene y aun así fracasa—; un cuerpo que cierra más allá y *se queda* es la noticia. | Una mecha que atraviesa un nivel no basta, y unas pocas velas cerrando al otro lado tampoco: el panel de la derecha las tiene y aun así fracasa. Lo que cuenta es un cuerpo que cierra más allá y *se queda*. | 2, 5 | PASS — all three steps and the figure fact kept; the rumour/news metaphor went |
| S044 | Una tendencia alcista es una escalera de máximos más altos (HH) y mínimos más altos (HL): cada subida supera el pico anterior y cada retroceso hace suelo por encima del anterior. | Una tendencia alcista es una secuencia de máximos más altos (HH) y mínimos más altos (HL). Cada subida supera el pico anterior y cada retroceso hace suelo por encima del anterior. | 9, 10, 5a | PASS — risky (definition) |
| S047–S048 | ¿Para qué molestarse en nombrar la escalera? Porque la secuencia te dice quién va ganando sin preguntarle a ningún indicador. | La secuencia de máximos y mínimos te dice quién va ganando sin preguntarle a ningún indicador. | 3, 9 | PASS (approved sample) |
| S051 | En cuanto la escalera se detiene, se detiene también la suposición. | Cuando la secuencia se interrumpe, esa suposición deja de valer. | 9, 4 | PASS (approved sample) |
| S053 | Cada mínimo por encima del mínimo anterior, cada máximo por encima del máximo anterior: una escalera que podrías describirle a alguien por teléfono. | Cada mínimo por encima del mínimo anterior, cada máximo por encima del máximo anterior: una secuencia que podrías describirle a alguien por teléfono. | 9 (4 left) | PASS — risky (definition) |
| S055 | Existe porque no todos actúan a la vez: algunos compradores toman ganancias durante la subida, algunos vendedores tardíos prueban suerte, y el precio devuelve parte del último tramo antes de que la tendencia se reanude. | Existe porque no todos actúan a la vez. Algunos compradores toman ganancias durante la subida, algunos vendedores tardíos prueban suerte, y el precio devuelve parte del último tramo antes de que la tendencia se reanude. | 5 | PASS |
| S059 | Una tendencia sigue intacta mientras la escalera continúa. | Una tendencia sigue intacta mientras la secuencia de máximos y mínimos continúa. | 9 | PASS — risky («sigue intacta mientras» verbatim) |
| S063–S064 | ¿Por qué pesa tanto esa primera ruptura? Porque toda la tendencia alcista se apoyaba en un mecanismo: que cada retroceso se compraba por encima del retroceso anterior. | Esa primera ruptura pesa tanto porque toda la tendencia alcista se apoyaba en un mecanismo: que cada retroceso se compraba por encima del retroceso anterior. | 3 | PASS |
| S066 | En la escalera de arriba, el precio cayendo desde 126, pasando por 109, hasta un mínimo de 106 es un cambio de carácter: el primer mínimo más bajo en una serie que solo había hecho mínimos más altos. | En la secuencia de arriba, el precio cayendo desde 126, pasando por 109, hasta un mínimo de 106 es un cambio de carácter. Es el primer mínimo más bajo en una serie que solo había hecho mínimos más altos. | 9, 5 | PASS — risky |
| S067 | Al gemelo de ese giro también le han puesto nombre, aunque este curso no lo necesite para explicar la escalera: cada máximo más alto que se lleva por delante el máximo anterior es una ruptura de estructura (BOS), la ruptura que *confirma* el patrón, frente al CHoCH, que lo rompe. | Al gemelo de ese giro también le han puesto nombre, aunque este curso no lo necesite para explicar la estructura. Cada máximo más alto que se lleva por delante el máximo anterior es una ruptura de estructura (BOS). Es la ruptura que *confirma* el patrón, frente al CHoCH, que lo rompe. | 9, 5 | PASS |
| S068 | Una escalera, dos clases de ruptura. | Una estructura, dos clases de ruptura. | 9 | PASS |
| S071 | La misma estructura también puede describirse con líneas *inclinadas* —líneas de tendencia y canales— y m15-l1 lo retoma, incluida la explicación honesta de cuánto más débil es la afirmación de la versión inclinada. | La misma estructura también puede describirse con líneas *inclinadas* —líneas de tendencia y canales—. Lo retoma m15-l1, incluida la explicación de cuánto más débil es la afirmación de la versión inclinada. | 1, 5a | PASS |
| S072 | La figura pone esa comparación lado a lado, con cada swing etiquetado: a la izquierda una escalera que sigue subiendo, a la derecha la misma escalera cuyo último swing falla. | La figura pone esa comparación lado a lado, con cada swing etiquetado: a la izquierda una secuencia que sigue subiendo, a la derecha la misma secuencia cuyo último swing falla. | 9 ×2 | PASS |
| S073 | Cada panel es una instancia generada con sus propios precios —los números de la escalera de arriba son proporciones para que la secuencia se pueda seguir de memoria, no una cotización que buscar—; lo que hay que leer es la forma y las etiquetas. | Cada panel es una instancia generada con sus propios precios. Los números del ejemplo de arriba son proporciones para que la secuencia se pueda seguir de memoria, no una cotización que buscar. Lo que hay que leer es la forma y las etiquetas. | 9, 5a | PASS — guard phrase intact; «escalera» → «ejemplo» rather than «secuencia», so «la secuencia» later in the sentence keeps its words |
| S074 | El cambio de carácter no es una promesa de que la tendencia se haya girado; es el primer *indicio* de que la regla de la vieja tendencia ha dejado de funcionar. | El cambio de carácter no es una promesa de que la tendencia se haya girado. Es el primer *indicio* de que la regla de la vieja tendencia ha dejado de funcionar. | 5 | PASS |
| S077 | La ruptura parece obvia, la vela es verde y rápida, y el miedo a perdérsela ahoga el plan, así que compras el asomo. | La ruptura parece obvia y la vela es verde y rápida. El miedo a perdérsela ahoga el plan, así que compras la primera vela que cruza el nivel. | 2, 9 | PASS — nothing dropped; the triad became two sentences |
| S078 | Pero el asomo es precisamente de lo que está hecho un fakeout: has comprado el estallido de stops disparados y órdenes de ruptura al peor precio posible, instantes antes de que se gire de vuelta dentro. | Pero un fakeout está hecho de esa vela. Has comprado el estallido de stops disparados y órdenes de ruptura al peor precio posible, instantes antes de que se gire de vuelta dentro. | 1, 9, 5 | PASS |
| S084 | Trata el CHoCH como una pregunta —*¿ha cambiado de verdad el control?*— y espera la respuesta: un máximo más bajo tras el mínimo más bajo, un intento fallido de recuperar el nivel, una segunda ruptura que confirme. | Trata el CHoCH como una pregunta: *¿ha cambiado el control?* Espera la respuesta: un máximo más bajo tras el mínimo más bajo, un intento fallido de recuperar el nivel, una segunda ruptura que confirme. | 1, 5 | PASS — risky; the three answers verbatim, no «o»/«y» added |
| S086 | Sin campana de cierre, las horas muertas —los fines de semana y el tramo en que todas las zonas horarias importantes duermen a la vez— funcionan con un libro de órdenes fino. | Sin campana de cierre, las horas muertas funcionan con un libro de órdenes fino. Son los fines de semana y el tramo en que todas las zonas horarias importantes duermen a la vez. | 5a | PASS — split; the aside moved after the clause |
| S087 | Menos órdenes en reposo significa que hace falta mucho menos tamaño para empujar el precio más allá de un nivel obvio, así que las falsas rupturas se concentran justo en estas ventanas. | Menos órdenes en reposo significa que hace falta mucho menos tamaño para empujar el precio más allá de un nivel obvio. Por eso las falsas rupturas se concentran en estas ventanas. | 1, 5 | PASS |
| S088 | Una "ruptura" impresa a las 4 de la madrugada de un domingo merece más recelo que la misma ruptura en una sesión concurrida de un día laborable; puede que el nivel simplemente se haya atravesado empujando aire vacío y vuelva de golpe cuando regrese el volumen real. | Una "ruptura" impresa a las 4 de la madrugada de un domingo merece más recelo que la misma ruptura en una sesión concurrida de un día laborable. Puede que el nivel se haya atravesado empujando aire vacío y vuelva de golpe cuando regrese el volumen real. | 1, 5 | PASS — risky; «concurrida» (busy session, not the crowded-positioning sense) untouched |
| S089 | El apalancamiento concentra los stops y los precios de liquidación justo más allá de los máximos y mínimos de swing obvios: todos miran los mismos niveles, así que las órdenes de protección de todos acaban en la misma banda estrecha. | El apalancamiento concentra los stops y los precios de liquidación justo más allá de los máximos y mínimos de swing obvios. Todos miran los mismos niveles, así que las órdenes de protección de todos acaban en la misma banda estrecha. | 5 | PASS — risky |
| S090 | En un libro poco profundo, un participante grande puede empujar el precio hasta esa banda, disparar los stops apilados y forzar la liquidación de los traders sobreapalancados, absorber la avalancha de órdenes resultante y dejar que el precio vuelva de golpe, dejando una mecha larga que perforó el nivel y cerró muy lejos de él. | En un libro poco profundo, un participante grande puede empujar el precio hasta esa banda, disparar los stops apilados y forzar la liquidación de los traders sobreapalancados. Después puede absorber la avalancha de órdenes resultante y dejar que el precio vuelva de golpe. Queda una mecha larga que perforó el nivel y cerró muy lejos de él. | 5 | PASS — risky; «puede» carried into the second sentence |
| S092 | Por eso la mecha que asoma por tu nivel suele ser más larga y más traicionera en cripto que la versión de manual, y por eso el cierre, nunca el extremo, es la única lectura honesta de si un nivel rompió de verdad. | Por eso, en cripto, la mecha que perfora tu nivel suele ser más larga que en los manuales. Para saber si un nivel ha roto, mira el cierre, nunca el extremo. | 1 ×2, 4, 5 | PASS (approved sample) — risky; «el cierre, nunca el extremo» verbatim |
| S100 | El cambio de carácter es el aviso honesto más temprano; ni uno antes. | El cambio de carácter es el aviso fiable más temprano; antes no hay ninguno. | 1, 4 | PASS — «honesto» meant *reliable*; dropping it outright would claim there are no earlier warnings of any kind |

### m08-l1 — EN

Mirrors ES row for row. Only EN-specific remarks are in the Review column.

| Id | Before | After | Patterns | Review |
|---|---|---|---|---|
| S002 | It leaves a visible record of where buyers and sellers fought, and that record — the structure — is the most honest chart-reading you can do, because it is the price itself, not an indicator derived from it. | It leaves a visible record of where buyers and sellers fought. That record is the structure, and it is the most direct chart-reading you can do: it is the price itself, not an indicator derived from it. | 1, 5 | PASS |
| S003 | Everything in this lesson is a way of reading that record: where price stalled, where it broke, and whether the breaks meant anything. | Reading that record means seeing where price stalled, where it broke, and whether the breaks meant anything. | 4 | PASS |
| S007–S008 | Why does buying reliably reappear at the same place? Because the place is remembered, and memory turns into orders. | Buying reliably reappears at the same place because the place is remembered, and memory turns into orders. | 3 | PASS |
| S012–S013 | A support is not magic in the number — it is a shelf of resting buy orders that the last few visits taught people to leave. Resistance is the same shelf built from sell orders. | A support is not magic in the number: it is a zone of resting buy orders that the last few visits taught people to leave there. Resistance is the same thing with sell orders. | 9, 10 | PASS (approved) |
| S018 | Concrete case: say BTC has turned up three times in the same neighbourhood — once it wicked down to 58,050 … and recovered. | Concrete case: say BTC has turned up three times in the same neighbourhood. Once it wicked down to 58,050 and closed back at 58,600, once it based around 58,300 for several candles, once it dipped to 58,150 intraday and recovered. | 5 | PASS — split only (EN was not marked aside-only, but the split mirrors ES) |
| S020 | There is a shelf roughly 58,000–58,400 wide. | There is a zone roughly 58,000–58,400 wide. | 9 | PASS — risky |
| S021 | Draw the zone from the bodies and wicks of the swings that actually turned, and expect price to react *somewhere inside it*, not at one exact number. | Draw the zone from the bodies and wicks of the swings that turned. Expect price to react *somewhere inside it*, not at one exact number. | 1 | PASS |
| S024 | A genuine breakout closes decisively beyond the level — a full candle body on the far side — and then holds there, ideally coming back to *retest* the old level as new support (or resistance) and bouncing away. | A genuine breakout closes decisively beyond the level — a full candle body on the far side — and then holds there. Ideally, it comes back to *retest* the old level as new support (or resistance) and bounces away. | 5a | PASS |
| S029 | Both have a mechanism, and it is worth understanding rather than memorising. | *(deleted)* | 1 | PASS |
| S030 | A genuine breakout tends to retest and hold because of *role reversal*: the sellers … turning former sellers into buyers; meanwhile the buyers who refused to chase finally get their entry at the old line. | A genuine breakout tends to retest and hold because of *role reversal*. The sellers who defended the old resistance have been overrun, and many cover their shorts on the pullback to the level: former sellers become buyers. Meanwhile the buyers who refused to chase finally get their entry at the old line. | 5 | PASS |
| S032 | The retest is the market voting a second time. | *(deleted)* | 4 | PASS |
| S033 | A fakeout happens because the obvious level is exactly where resting orders pile up just beyond it: the stop-losses of traders positioned into the level, and the buy orders of breakout traders who leave "buy if it breaks" instructions. | A fakeout happens because resting orders pile up just beyond the obvious level. They are the stop-losses of traders positioned into the level and the buy orders of breakout traders, who leave "buy if it breaks" instructions. | 1, 5 | PASS — risky in EN (inventory) |
| S035 | Once that fuel is spent, price falls back inside, and the ones who bought the poke are now trapped above the level and motivated to sell. | Once those orders are spent, price falls back inside. The ones who bought the first candle through the level are now trapped above the level and motivated to sell. | 9 ×2 | PASS |
| S036 | The false break didn't fail by accident; it ran out of the very orders that caused it. | *(deleted)* | 4 | PASS |
| S037 | Concretely, using the numbers in the figure below: resistance sits around 2,130, and the two panels are literally the same chart — the same range, the same candles — right up to the decision. | Concretely, using the numbers in the figure below: resistance sits around 2,130. The two panels are the same chart — the same range, the same candles — right up to the decision. | 1, 5a | PASS — risky |
| S039 | On the right, a fakeout: the same poke reaches 2,166, holds half a dozen candles above the line, then loses them — it closes back under 2,130, gives up 2,035 within a few candles, and keeps sliding from there. | On the right, a fakeout: the same break reaches 2,166, holds half a dozen candles above the line, then loses them. It closes back under 2,130, gives up 2,035 within a few candles, and keeps sliding from there. | 9, 5 | FAIL → fixed (note 1); risky |
| S040 | Same level, same first candles; only the close *that holds* and what follows tell them apart. | *(deleted)* | 4 | PASS |
| S042 | A wick through a level is a rumour; a few candles closing on the other side are an unconfirmed headline — the right-hand panel has them and still fails; a body that closes beyond and *stays* is the news. | A wick through a level is not enough, and neither are a few candles closing on the other side: the right-hand panel has them and still fails. What counts is a body that closes beyond and *stays*. | 2, 5 | PASS |
| S044 | An uptrend is a staircase of higher highs (HH) and higher lows (HL): each rally exceeds the last peak, and each dip bottoms above the last dip. | An uptrend is a sequence of higher highs (HH) and higher lows (HL). Each rally exceeds the last peak, and each dip bottoms above the last dip. | 9, 10 | PASS — risky |
| S047–S048 | Why bother naming the staircase? Because the sequence tells you who is winning without asking any indicator. | The sequence of highs and lows tells you who is winning without asking any indicator. | 3, 9 | PASS (approved) |
| S051 | The moment the staircase stops, so does the assumption. | When the sequence breaks off, that assumption stops holding. | 9, 4 | PASS (approved) |
| S053 | Each low above the previous low, each high above the previous high — a staircase you could describe to someone over the phone. | … — a sequence you could describe to someone over the phone. | 9 | PASS — risky |
| S055 | It exists because not everyone acts at once: some buyers take profit into strength, some late sellers try their luck, and price gives back part of the last leg before the trend resumes. | It exists because not everyone acts at once. Some buyers take profit into strength, some late sellers try their luck, and price gives back part of the last leg before the trend resumes. | 5 | PASS |
| S059 | A trend stays intact as long as the staircase continues. | A trend stays intact as long as the sequence of highs and lows continues. | 9 | PASS — risky |
| S063–S064 | Why does that first break carry so much weight? Because the whole uptrend rested on one mechanism — every dip being bought above the previous dip. | That first break carries so much weight because the whole uptrend rested on one mechanism — every dip being bought above the previous dip. | 3 | PASS |
| S066 | In the staircase above, price falling from 126 down through 109 to a low of 106 is a change of character — the first lower low in a run that had made only higher ones. | In the sequence above, price falling from 126 down through 109 to a low of 106 is a change of character. It is the first lower low in a run that had made only higher ones. | 9, 5 | PASS — risky |
| S067 | That break's twin has a name too, though this course does not need it to explain the ladder: every higher high … is a break of structure (BOS) — the break that *confirms* the pattern, as against the CHoCH, which breaks it. | That break's twin has a name too, though this course does not need it to explain the structure. Every higher high that takes out the previous high is a break of structure (BOS). It is the break that *confirms* the pattern, as against the CHoCH, which breaks it. | 9, 5 | PASS |
| S068 | One ladder, two kinds of break. | One structure, two kinds of break. | 9 | PASS |
| S071 | The same structure can also be described with *sloped* lines — trendlines and channels — and m15-l1 takes that up, including the honest account of how much weaker the sloped version's claim is. | The same structure can also be described with *sloped* lines — trendlines and channels. m15-l1 takes that up, including the account of how much weaker the sloped version's claim is. | 1, 5a | PASS — the second sentence starts with a module id, as the course already does elsewhere |
| S072 | … on the left a staircase that keeps climbing, on the right the same ladder whose final swing fails. | … on the left a sequence that keeps climbing, on the right the same sequence whose final swing fails. | 9 ×2 | PASS |
| S073 | Each panel is a generated instance carrying its own prices — the numbers in the ladder above are proportions, chosen so the sequence is one you can hold in your head, not a quote to go looking for — so what to read is the shape and the labels. | Each panel is a generated instance carrying its own prices. The numbers in the example above are proportions, chosen so the sequence is one you can hold in your head, not a quote to go looking for. What to read is the shape and the labels. | 9, 5a | PASS — guard phrase intact; risky in EN |
| S074 | The change of character is not a promise that the trend has reversed; it is the first *evidence* that the old trend's rule has stopped working. | The change of character is not a promise that the trend has reversed. It is the first *evidence* that the old trend's rule has stopped working. | — (mirror of ES S074) | PASS |
| S077 | The break looks obvious, the candle is green and fast, and the fear of missing it drowns out the plan — so you buy the poke. | The break looks obvious and the candle is green and fast. The fear of missing it drowns out the plan — so you buy the first candle through the level. | 2, 9 | PASS |
| S078 | But the poke is exactly what a fakeout is made of: you have bought the burst … moments before it reverses back inside. | But that candle is what a fakeout is made of. You have bought the burst of triggered stops and breakout orders at the worst possible price, moments before it reverses back inside. | 1, 9, 5 | PASS |
| S084 | Treat the CHoCH as a question — *has control actually changed?* — and wait for the answer: … | Treat the CHoCH as a question: *has control changed?* Wait for the answer: a lower high after the lower low, a failed attempt to reclaim, a second confirming break. | 1, 5a | PASS — risky |
| S086 | With no closing bell, the dead hours — weekends, and the stretch when every major timezone is asleep at once — run on a thin order book. | With no closing bell, the dead hours run on a thin order book. They are the weekends, and the stretch when every major timezone is asleep at once. | — (mirror) | PASS |
| S087 | Fewer resting orders means far less size is needed to shove price through an obvious level, so false breaks cluster in exactly these windows. | Fewer resting orders means far less size is needed to shove price through an obvious level. That is why false breaks cluster in these windows. | 1 | PASS |
| S088 | A "breakout" printed at 4 a.m. on a Sunday … session; the level may simply have been pushed through empty air and will snap back when real volume returns. | A "breakout" printed at 4 a.m. on a Sunday deserves more suspicion than the same break in a busy weekday session. The level may have been pushed through empty air and will snap back when real volume returns. | 1, 5 | PASS — risky |
| S089 | Leverage concentrates … the obvious swing highs and lows — everyone watches the same levels, so everyone's protective orders end up in the same narrow band. | Leverage concentrates stop-loss orders and liquidation prices just beyond the obvious swing highs and lows. Everyone watches the same levels, so everyone's protective orders end up in the same narrow band. | 5 | PASS — risky |
| S090 | In a thin book a large player can push price into that band, trip the clustered stops and force the liquidation of over-leveraged traders, absorb the resulting flood of orders, and let price snap back — leaving a long wick that pierced the level and closed far away from it. | In a thin book a large player can push price into that band, trip the clustered stops and force the liquidation of over-leveraged traders. Then it can absorb the resulting flood of orders and let price snap back. What is left is a long wick that pierced the level and closed far away from it. | 5 | PASS — risky |
| S092 | This is why the wick that pokes your level is often longer and nastier in crypto than the textbook version — and why the close, never the extreme, is the only honest reading of whether a level actually broke. | That is why, in crypto, the wick through your level is often longer than in the textbooks. To judge whether a level broke, read the close, never the extreme. | 1 ×2, 4, 5 | PASS (approved) — risky |
| S100 | The change of character is the earliest honest warning — no earlier. | The change of character is the earliest reliable warning; there is none before it. | 1, 4 | PASS |

### m27-l1 — ES

| Id | Before | After | Patterns | Review |
|---|---|---|---|---|
| S002 | …decidida de antemano y luego simplemente ejecutada. | …decidida de antemano y luego ejecutada. | 1 | PASS |
| S003 | Esta lección recorre una única operación de principio a fin, con números, para que veas el proceso entero de golpe, y para que veas que, cuando el dinero está en riesgo, casi todas las decisiones ya están tomadas. | Vamos a recorrer una única operación de principio a fin, con números, para ver el proceso entero de golpe. Cuando el dinero está en riesgo, casi todas las decisiones ya están tomadas. | 1, 4, 5 | PASS — the claim is now a flat sentence of its own |
| S005 | Ten presente ese número: todo lo que viene después está construido para que equivocarse cueste exactamente eso y nada más. | Todo lo que viene después está construido para que equivocarse cueste exactamente eso. | 1, 4 | PASS — risky; «exactamente eso» (pins 100 USDT) kept; «Ten presente ese número» was an exhortation |
| S006 | Empieza por la lente más amplia, la pregunta del bloque D: ¿qué está *haciendo* el mercado y ofrece algo? | Empieza por el contexto más amplio, la pregunta del bloque D: ¿qué está *haciendo* el mercado y ofrece algo? | 9, 10 | PASS — «contexto», as the section heading names it |
| S008 | Un retroceso dentro de una tendencia alcista es justo lo que queremos: … | Un retroceso dentro de una tendencia alcista es lo que queremos: … | 1 | PASS |
| S011 | La mayor parte del tiempo la respuesta honesta a «¿qué se ofrece?» es *nada limpio*, y la mejor operación es ninguna. | La mayor parte del tiempo la respuesta a «¿qué se ofrece?» es *nada limpio*, y la mejor operación es ninguna. | 1 | PASS |
| S012 | Hoy hay un retroceso en una tendencia alcista, así que miramos más de cerca. | Hoy hay un retroceso en una tendencia alcista. | 4 | PASS |
| S014 | Las temporalidades anidadas (m03-l2) y la elección de temporalidad según el estilo (m23) implican un paso del proceso que ninguna de las dos deja escrito, así que aquí queda nombrado: la temporalidad superior dicta el sesgo, la temporalidad inferior dicta la entrada, y el orden no es reversible. | Las temporalidades anidadas (m03-l2) y la elección de temporalidad según el estilo (m23) implican un paso del proceso que ninguna de las dos deja escrito. Es este: la temporalidad superior dicta el sesgo, la temporalidad inferior dicta la entrada, y el orden no es reversible. | 5 | PASS — risky; rule words verbatim |
| lead-in + S015 | **Marco macro → sesgo y niveles.** En el gráfico lento decides *en qué dirección…* | **Temporalidad superior → sesgo y niveles.** En la temporalidad superior decides *en qué dirección…* | 9 (label), 11 | PASS — label change as instructed |
| lead-in + S018 | **Marco micro → trigger y stop.** Solo entonces bajas al gráfico rápido, y solo para responder… | **Temporalidad inferior → trigger y stop.** Solo entonces bajas a la temporalidad inferior, y solo para responder… | 9 (label), 11 | PASS |
| S020 | el marco micro imprime señales constantemente, en las dos direcciones. | la temporalidad inferior imprime señales constantemente, en las dos direcciones. | 9 | PASS |
| S021 | Déjale elegir la dirección y siempre encontrarás una que apunte donde ya querías ir: es el aviso de m03-l2 … | Déjale elegir la dirección y siempre encontrarás una que apunte donde ya querías ir. Es el aviso de m03-l2 sobre saltar entre niveles de zoom para justificar una posición, llegando un paso antes. | 5 | PASS — risky («siempre» kept) |
| S022 | Así que una señal del marco micro que contradice el sesgo macro es una operación descartada, no una oportunidad de operar en contra: un largo limpio en 1 hora dentro de una tendencia bajista diaria es justo la operación que este protocolo existe para rechazar. | Así que una señal en la temporalidad inferior que contradice el sesgo de la superior es una operación descartada, no una oportunidad de operar en contra. Un largo limpio en 1 hora dentro de una tendencia bajista diaria es la operación que este paso rechaza. | 9, 1, 5 | PASS (approved sample) — risky |
| S023 | Acércate al retroceso, todavía en el marco macro. | Acércate al retroceso, todavía en la temporalidad superior. | 9 | PASS |
| S024 | El precio cae hacia 60.000, y allí coinciden tres cosas independientes: es el máximo previo … y la EMA de 50 al alza trepa hacia la misma zona. | El precio cae hacia 60.000, y allí coinciden tres cosas independientes. Es el máximo previo que se rompió al subir (la vieja resistencia pasa a soporte), es el retroceso 0,618 del último tramo, y la EMA de 50 al alza trepa hacia la misma zona. | 5 | PASS — the second half is still 35 words (a list of three facts) |
| S029 | La confluencia es como conviertes un nivel a cara o cruz en un lugar donde vale la pena arriesgar dinero. | *(deleted)* | 4 (restate) | PASS — S028 carries the odds claim |
| S032 | Esperamos la reacción en el marco micro (véase m08-l2): el precio se hunde hasta 59.700, se forma una mecha inferior larga y la vela de 1 hora cierra de vuelta en 60.300, una vela de rechazo. | Esperamos la reacción en la temporalidad inferior (véase m08-l2). El precio se hunde hasta 59.700, se forma una mecha inferior larga y la vela de 1 hora cierra de vuelta en 60.300: una vela de rechazo. | 9, 5 | PASS — risky |
| S033 | Los vendedores empujaron por debajo del nivel, fueron absorbidos y perdieron. | Los vendedores empujaron por debajo del nivel y fueron absorbidos. | 2 | PASS — «perdieron» restated «absorbidos» |
| S036 | …demostrar que los compradores aparecieron de verdad antes de comprometerte. | …demostrar que los compradores aparecieron antes de comprometerte. | 1 | PASS |
| S040 | …esa tesis es sencillamente falsa: el nivel no aguantó. | …esa tesis es falsa: el nivel no aguantó. | 1 | PASS — risky (59.300 kept) |
| S043 | Colocado en la estructura, que te salte significa algo real —te equivocaste con el nivel— en vez de ser una distancia aleatoria que el mercado atraviesa con una mecha por ruido. | Colocado en la estructura, que te salte significa algo real: te equivocaste con el nivel. No es una distancia aleatoria que el mercado atraviesa con una mecha por ruido. | 5a | PASS — split; «en vez de ser» → «No es», the least a split needs |
| S053 | …son lo que un trader dibuja de verdad en el gráfico. | …son lo que un trader dibuja en el gráfico. | 1 | PASS |
| S056 | Hazlo en ese orden y el riesgo es constante … apalancamiento; invíertelo —elige un tamaño y luego busca un stop que «encaje»— y vuelves a apostar. | Hazlo en ese orden y el riesgo es constante en cada operación sin importar el precio ni el apalancamiento. Invíertelo —elige un tamaño y luego busca un stop que «encaje»— y vuelves a apostar. | 5a | PASS — split only; risky |
| S061 | El stop se mueve a break-even solo cuando la operación ha producido una confirmación nueva a su favor en la temporalidad de ejecución: una ruptura de estructura en la dirección de la operación, que en este largo significa un nuevo máximo más alto y después el mínimo más alto que le sigue, ambos por encima de la entrada, en el gráfico de 1 hora del que salió la entrada. | El stop se mueve a break-even solo cuando la operación ha producido una confirmación nueva a su favor en la temporalidad de ejecución. Esa confirmación es una ruptura de estructura en la dirección de la operación, en el gráfico de 1 hora del que salió la entrada. En este largo significa un nuevo máximo más alto y después el mínimo más alto que le sigue, ambos por encima de la entrada. | 5 | PASS — risky; the 1-hour qualifier moved to the sentence that defines the confirmation, rule words verbatim |
| S064 | El verde es donde vive el ruido —una sola vela hasta 60.600 es un número que el mercado marca y borra todo el día— mientras que la estructura es algo que el precio ha tenido que *construir*. | El verde es ruido: una sola vela hasta 60.600 es un número que el mercado marca y borra todo el día. La estructura, en cambio, es algo que el precio ha tenido que *construir*. | 10, 5a | PASS — risky |
| S066 | Si la única respuesta honesta es «está en verde», el stop se queda donde lo puso el plan. | Si la única respuesta es «está en verde», el stop se queda donde lo puso el plan. | 1 | PASS — risky |
| S068 | …el máximo menor en 62.300, exactamente +2R: vendes ahí el 40%, mueves el stop a 60.300 y dejas el 60% apuntando a 64.000. | …el máximo menor en 62.300, exactamente +2R. Vendes ahí el 40%, mueves el stop a 60.300 y dejas el 60% apuntando a 64.000. | 5 | PASS — risky; «exactamente +2R» pins the quantity, so it stays |
| S069 | Es una forma legítima de asegurar avance y quitarle carga emocional al resto, pero la frase que lo vende —un «runner sin riesgo»— es donde tiene que entrar la honestidad, porque ese runner no es gratis y puedes ponerle precio exacto. | Es una forma legítima de asegurar avance y quitarle carga emocional al resto. Pero la frase que lo vende, un «runner sin riesgo», es engañosa: ese runner no es gratis y puedes ponerle precio exacto. | 1, 5 | PASS — closest call (note 11) |
| S072 | Lo que compras a cambio es una proporción mayor de ganancias pequeñas: la operación que se atasca en 62.300 … +0,8R en vez de 0. | Lo que compras a cambio es una proporción mayor de ganancias pequeñas. La operación que se atasca en 62.300 y se da la vuelta ahora sale en +0,8R en vez de 0. | 5 | PASS — risky |
| S073 | Si esa operación merece la pena no te lo puede decir nadie en abstracto: son dos versiones de *tu* sistema, y el diario (m27-l2) … | Si esa operación merece la pena no te lo puede decir nadie en abstracto. Son dos versiones de *tu* sistema, y el diario (m27-l2) es el único instrumento que puede compararlas. | 5a | PASS — split only |
| S081 | Resultado: +3,7R ≈ +370 USDT, o +3,0R ≈ +300 USDT si ejecutamos la versión con parciales de arriba: una operación planificada y ejecutada. | Resultado: +3,7R ≈ +370 USDT, o +3,0R ≈ +300 USDT si ejecutamos la versión con parciales de arriba. | 4 | PASS — risky |
| heading | ## El freno diario: la regla que cierra el día | ## El límite de pérdida diaria: la regla que cierra el día | 9 | PASS (decided) |
| S084 | Así que el plan lleva un segundo límite, separado: un freno diario, que es el límite de pérdida diaria de m26 hecho mecánico. | Así que el plan lleva un segundo límite, separado: un límite de pérdida diaria. Es la regla de m26, convertida en un número. | 9, 10 | PASS (approved sample with your change) — risky |
| S089 | La X la eliges tú, típicamente entre el 1 y el 3% (los estilos rápidos que hacen más operaciones al día pertenecen a la parte baja), y se fija en el plan, antes del día malo, nunca durante él. | La X la eliges tú, normalmente entre el 1 y el 3%. Los estilos rápidos que hacen más operaciones al día van en la parte baja. Se fija en el plan, antes del día malo, nunca durante él. | 5a | PASS (approved sample, relative clause reverted to restrictive in session 2) — risky; see note 9 |
| S091 | La persona que decide si sigue operando tras un −3% es la versión de ti de la que habla todo m26: anclada en volver a estar en cero, con sensación de urgencia y la persona menos cualificada del mundo para juzgar su propio estado. | La persona que decide si sigue operando tras un −3% es la versión de ti de la que habla todo m26. Está anclada en volver a estar en cero, con sensación de urgencia. Es la persona menos cualificada del mundo para juzgar su propio estado. | 2, 5 | PASS — risky; the reviewer's "drop the third" would remove the argument's point, so the triad was broken by splitting instead |
| S092 | La respuesta de m26 era el compromiso previo —decidirlo cuando no hay nada en juego— y el freno diario es esa doctrina convertida en un número y un corte duro. | La respuesta de m26 era el compromiso previo: decidirlo cuando no hay nada en juego. El límite de pérdida diaria es esa doctrina convertida en un número y un corte duro. | 9, 5a | PASS |
| S093 | Funciona precisamente porque no te consulta en el momento en que menos capaz eres de responder. | Funciona porque no te consulta en el momento en que menos capaz eres de responder. | 1 (4 left) | PASS |
| note (S094–S095 area) | El freno diario es la regla anti-venganza… Un freno diario que te saltas no es una regla… | El límite de pérdida diaria es la regla anti-venganza… Un límite de pérdida diaria que te saltas no es una regla… | 9 (term only) | PASS — note 3 |
| S096 | El mercado está abierto 24/7, así que una operación que colocas el viernes está viva y sin vigilancia todo el fin de semana, en libros poco profundos donde 60.000 puede recibir una mecha violenta con poco volumen: una razón más para que protejan el stop y el tamaño, no tu atención. | El mercado está abierto 24/7, así que una operación que colocas el viernes está viva y sin vigilancia todo el fin de semana. Ese fin de semana transcurre en libros poco profundos, donde 60.000 puede recibir una mecha violenta con poco volumen. Es una razón más para que protejan el stop y el tamaño, no tu atención. | 5 | FAIL → fixed (glossary term, see the fixes table) |
| S097 | Y como el apalancamiento está a un clic, la disciplina de *dimensionar desde el stop* es lo que evita que «0,1 BTC» se convierta en silencio en una posición cuyo stop es una liquidación. | El apalancamiento está a un clic. Por eso la disciplina de *dimensionar desde el stop* es lo que evita que «0,1 BTC» se convierta en silencio en una posición cuyo stop es una liquidación. | 5 | PASS — risky; the causal «como» is carried by «Por eso» |
| S098 | El 24/7 también significa que no hay campana de cierre que te dé por terminado un mal día, así que el «día» del *freno diario* tienes que definirlo tú: elige una hora de reinicio, escríbela (00:00 UTC, por ejemplo) y que esa sea la campana. | El 24/7 también significa que no hay campana de cierre que te dé por terminado un mal día. Así que el «día» del *límite de pérdida diaria* tienes que definirlo tú: elige una hora de reinicio, escríbela (00:00 UTC, por ejemplo) y que esa sea la campana. | 9, 5 | PASS — risky |
| S099 | Sin ella, una tarde de −2% simplemente se prolonga en la misma sesión a las 3 de la madrugada, … | Sin ella, una tarde de −2% se prolonga en la misma sesión a las 3 de la madrugada, que es la hora en la que el tilt está menos vigilado. | 1, 5 | PASS — risky |
| summary S102 (course.yaml) | …cierra el día: un freno diario fijado en el plan antes del día malo, … | …cierra el día: un límite de pérdida diaria fijado en el plan antes del día malo, … | 9 | PASS («fijado» still agrees with «límite») |

### m27-l1 — EN

| Id | Before | After | Patterns | Review |
|---|---|---|---|---|
| S002 | …decided in advance and then simply executed. | …decided in advance and then executed. | 1 | PASS |
| S003 | This lesson walks a single trade end to end, with numbers, so you can see the whole process at once — and see that by the time money is at risk, almost every decision has already been made. | We will walk a single trade end to end, with numbers, to see the whole process at once. By the time money is at risk, almost every decision has already been made. | 1, 4, 5 | PASS |
| S005 | Hold that number in mind: everything downstream is built to make being wrong cost exactly that and no more. | Everything downstream is built to make being wrong cost exactly that. | 1, 4 | PASS — risky |
| S006 | Start with the widest lens, the block-D question: … | Start with the broadest context, the block-D question: … | 9, 10 | PASS |
| S011 | Most of the time the honest answer to "what is on offer?" is … | Most of the time the answer to "what is on offer?" is … | 1 | PASS |
| S012 | Today there is a pullback in an uptrend, so we look closer. | Today there is a pullback in an uptrend. | 4 | PASS |
| S014 | …neither one spells out, so here it is, named: the higher timeframe dictates the bias, … | …neither one spells out. Here it is: the higher timeframe dictates the bias, the lower timeframe dictates the entry — and the order is not reversible. | 5 | PASS — risky |
| lead-ins + S015, S018 | **Macro frame → bias and levels.** On the slower chart you decide … / **Micro frame → trigger and stop.** Only then drop to the faster chart, … | **Higher timeframe → bias and levels.** On the higher timeframe you decide … / **Lower timeframe → trigger and stop.** Only then drop to the lower timeframe, … | 9, 11 | PASS |
| S020 | the micro frame prints signals constantly, in both directions. | the lower timeframe prints signals constantly, in both directions. | 9 | PASS |
| S021 | Let it choose the direction and you will always find one pointing where you already wanted to go — that is m03-l2's warning … | Let it choose the direction and you will always find one pointing where you already wanted to go. That is m03-l2's warning about flipping between zoom levels to justify a position, arriving one step earlier. | 5 | PASS — risky |
| S022 | So a micro-frame signal that contradicts the macro bias is a skipped trade, not a counter-trade opportunity: a clean 1-hour long inside a daily downtrend is precisely the trade this protocol exists to refuse. | So a lower-timeframe signal that contradicts the higher-timeframe bias is a skipped trade, not a chance to trade against it. A clean 1-hour long inside a daily downtrend is the trade this step rejects. | 9, 1, 5 | PASS (approved) — risky |
| S023 | Zoom in on the pullback, still on the macro frame. | Zoom in on the pullback, still on the higher timeframe. | 9 | PASS |
| S024 | Price is falling toward 60,000, and three independent things line up there: it is the prior swing high … | Price is falling toward 60,000, and three independent things line up there. It is the prior swing high that broke on the way up (old resistance becomes support), it is the 0,618 retracement of the last leg, and the rising 50-EMA is climbing into the same zone. | 5 | PASS — risky |
| S029 | Confluence is how you turn a coin-flip level into a location worth risking money at. | *(deleted)* | 4 | PASS |
| S032 | We wait for the reaction on the micro frame (see m08-l2): price dips to 59,700, … — a rejection candle. | We wait for the reaction on the lower timeframe (see m08-l2). Price dips to 59,700, a long lower wick forms and the 1-hour candle closes back at 60,300 — a rejection candle. | 9, 5a | PASS — risky |
| S033 | Sellers pushed below the level, were absorbed, and lost. | Sellers pushed below the level and were absorbed. | 2 | PASS |
| S036 | …prove buyers actually showed up before you commit. | …prove buyers showed up before you commit. | 1 | PASS |
| S040 | …that thesis is simply false: the level did not hold. | …that thesis is false: the level did not hold. | 1 | PASS — risky |
| S043 | Placed at the structure, being stopped out means something real — you were wrong about the level — instead of being a random distance the market wicks through by noise. | Placed at the structure, being stopped out means something real: you were wrong about the level. It is not a random distance the market wicks through by noise. | — (mirror) | PASS |
| S053 | …what a trader actually draws on the chart. | …what a trader draws on the chart. | 1 | PASS |
| S056 | …regardless of price or leverage; reverse it — pick a size, then find a stop that "feels" right — and you are back to gambling. | …regardless of price or leverage. Reverse it — pick a size, then find a stop that "feels" right — and you are back to gambling. | 5a | PASS — risky |
| S061 | The stop moves to break-even only once the trade has produced new confirmation in its favour on the execution timeframe — a break of structure in the trade's direction, which for this long means a fresh higher high and then the higher low that follows it, both above entry, on the 1-hour chart the entry came from. | The stop moves to break-even only once the trade has produced new confirmation in its favour on the execution timeframe. That confirmation is a break of structure in the trade's direction, on the 1-hour chart the entry came from. For this long it means a fresh higher high and then the higher low that follows it, both above entry. | 5 | PASS — risky |
| S064 | Green is where noise lives — a single candle to 60,600 is a number the market prints and unprints all day — while structure is something price had to *build*. | Green is noise: a single candle to 60,600 is a number the market prints and unprints all day. Structure, by contrast, is something price had to *build*. | 10 | PASS — risky |
| S066 | If the only honest answer is "it is up", the stop stays where the plan put it. | If the only answer is "it is up", the stop stays where the plan put it. | 1 | PASS — risky |
| S068 | …the minor swing high at 62,300, exactly +2R: sell 40% there, … | …the minor swing high at 62,300, exactly +2R. Sell 40% there, move the stop to 60,300, and leave 60% aiming at 64,000. | — (mirror) | PASS — risky |
| S069 | It is a legitimate way … — but the phrase that sells it, a *risk-free runner*, is where the honesty has to come in, because the runner is not free and you can price it exactly. | It is a legitimate way to bank progress and take the emotional weight off the remainder. But the phrase that sells it, a *risk-free runner*, is misleading: the runner is not free and you can price it exactly. | 1, 5 | PASS — note 11 |
| S072–S074 | What you buy with it is a higher share of small wins — the trade that stalls … +0.8R instead of 0. Whether that exchange is worth making … in the abstract: it is two versions … | What you buy with it is a higher share of small wins. The trade that stalls at 62,300 and comes back now scratches at +0.8R instead of 0. Whether that exchange is worth making is not something anyone can tell you in the abstract. It is two versions of *your* system, and the journal (m27-l2) is the only instrument that can compare them. | 5 | PASS — risky |
| S082 | Result: +3.7R ≈ +370 USDT — or +3.0R ≈ +300 USDT if we ran the partials version above — a planned trade, executed. | Result: +3.7R ≈ +370 USDT, or +3.0R ≈ +300 USDT if we ran the partials version above. | 4 | PASS — risky |
| S085 | So the plan carries a second, separate limit: a daily stop, which is m26's daily loss limit made mechanical. | So the plan carries a second, separate limit: a daily stop. It is m26's daily loss limit, turned into a number. | 10 | PASS — note 10 |
| S090 | The X is yours to pick, typically 1–3% (faster styles taking more trades a day belong at the low end), and it is set in the plan, before the losing day — never adjusted during one. | You pick the X, typically 1–3%. Fast styles that take more trades a day belong at the low end. It is set in the plan, before the losing day, never adjusted during one. | 5a | PASS (approved, relative clause reverted to restrictive in session 2) — risky; note 9 |
| S091–S092 | The person deciding … all of m26 is about: anchored on getting back to even, feeling urgency, and the least qualified person in the world to assess their own state. m26's answer was pre-commitment — decide it when nothing is at stake — and the daily stop is that doctrine turned into a number and a hard cutoff. | The person deciding whether to keep trading after −3% is the version of you all of m26 is about. That person is anchored on getting back to even, feeling urgency. They are the least qualified person in the world to assess their own state. m26's answer was pre-commitment: decide it when nothing is at stake. The daily stop is that doctrine turned into a number and a hard cutoff. | 2, 5 | PASS — risky |
| S093 | It works precisely because it does not consult you … | It works because it does not consult you at the moment you are least able to answer. | 1 | PASS |
| S096–S097 | The market is open 24/7, so a trade you place on Friday is live and unwatched all weekend, on thin books where 60,000 can be wicked hard on low volume — another reason the stop and the size, not your attention, must do the protecting. And because leverage sits one click away, the discipline of *sizing from the stop* is what stops "0.1 BTC" from quietly becoming a position whose stop is a liquidation. | The market is open 24/7, so a trade you place on Friday is live and unwatched all weekend. That weekend runs on thin books, where 60,000 can be wicked hard on low volume. That is another reason the stop and the size, not your attention, must do the protecting. Leverage sits one click away. So the discipline of *sizing from the stop* is what stops "0.1 BTC" from quietly becoming a position whose stop is a liquidation. | 5 | FAIL → fixed (thin books); risky («must» kept) |
| S098–S099 | 24/7 also means there is no closing bell to end a bad day for you, so the "day" in *daily stop* is one you have to define yourself: … Without it, a −2% evening simply rolls into the same session at 3 a.m., … | 24/7 also means there is no closing bell to end a bad day for you. So the "day" in *daily stop* is one you have to define yourself: pick a reset hour, write it down (00:00 UTC, say), and let that be the bell. Without it, a −2% evening rolls into the same session at 3 a.m., which is the hour tilt is least supervised. | 1, 5 | PASS — risky |

EN keeps «daily stop» in its heading, the warning note and the summary, as decided.

## Risky sentences (rule / quantity / direction), separately

Every sentence the inventory marks risky for these two lessons. "Hit" = a pattern hit sat in the sentence, so it was
eligible. "Kept verbatim" lists the rule, quantity and direction words checked word by word against the before text.

| Lesson | Id | Hit | Changed? | Kept verbatim |
|---|---|---|---|---|
| m08 | S018 | 5a | split only | 58.050, 58.600, 58.300, 58.150 / 58,050 … |
| m08 | S020 | 9 | estante → zona | 58.000–58.400 |
| m08 | S033 (EN risky) | 1, 5 | yes | "just beyond", stops / buy orders of breakout traders |
| m08 | S037 | 1, 5 | split, «literalmente» out | 2.130; «el mismo gráfico — el mismo rango, las mismas velas — hasta el momento de la decisión» |
| m08 | S039 | 9, 5a | asomo → ruptura, split | 2.166, 2.130, 2.035, «media docena de velas» |
| m08 | S044 | 9, 10, 5a | escalera → secuencia, split | máximos más altos (HH), mínimos más altos (HL), «supera el pico anterior», «hace suelo por encima del anterior» |
| m08 | S045–S046 | — | no | — |
| m08 | S052 | 5a | **no** (left; see above) | 100 / 110 / 104 / 118 / 109 / 126 |
| m08 | S053 | 9 | escalera → secuencia | «cada mínimo por encima del mínimo anterior, cada máximo por encima del máximo anterior» |
| m08 | S059 | 9 | escalera → secuencia de máximos y mínimos | «sigue intacta mientras … continúa» |
| m08 | S066 | 9, 5 | escalera → secuencia, split | 126, 109, 106, «el primer mínimo más bajo», «solo había hecho mínimos más altos» |
| m08 | S073 | 9, 5a | split, escalera → ejemplo | «instancia generada», «proporciones», «no una cotización que buscar» |
| m08 | S080 | 4 | **no** (left; see above) | — |
| m08 | S084 | 1, 5 | «de verdad» out, split | the three answers: «un máximo más bajo tras el mínimo más bajo, un intento fallido de recuperar el nivel, una segunda ruptura que confirme» |
| m08 | S088 | 1, 5 | «simplemente» out, split | «4 de la madrugada de un domingo», «más recelo», «vuelva de golpe cuando regrese el volumen real» |
| m08 | S089 | 5 | split | «justo más allá de los máximos y mínimos de swing obvios», «la misma banda estrecha» |
| m08 | S090 | 5 | split ×2 | «empujar … disparar … forzar la liquidación … absorber … dejar que el precio vuelva de golpe», «perforó el nivel y cerró muy lejos de él» |
| m08 | S092 | 1, 4, 5 | approved sample | «el cierre, nunca el extremo», «suele ser más larga» |
| m08 | S103 (EN risky, summary) | 5 | **no** (course.yaml frozen) | — |
| m27 | S004 | — | no | 10.000 USDT, 1%, 100 USDT |
| m27 | S005 | 1, 4 | yes | «exactamente eso» |
| m27 | S014 | 5 | split | «la temporalidad superior dicta el sesgo, la temporalidad inferior dicta la entrada, y el orden no es reversible» |
| m27 | S021 | 5 | split | «siempre encontrarás una que apunte donde ya querías ir» |
| m27 | S022 | 9, 1, 5 | approved sample | «largo», «1 hora», «tendencia bajista diaria», «operación descartada, no una oportunidad de operar en contra» |
| m27 | S032 | 9, 5 | split | 59.700, 60.300, «vela de 1 hora», «mecha inferior larga» |
| m27 | S040 | 1 | «sencillamente» out | 59.300, «cierra bien por debajo de la mecha de rechazo» |
| m27 | S056 | 5a | split only | «en ese orden», «constante», «invíertelo» |
| m27 | S061 | 5 | split ×2 | «solo cuando», «temporalidad de ejecución», «nuevo máximo más alto y después el mínimo más alto que le sigue, ambos por encima de la entrada», «gráfico de 1 hora» |
| m27 | S064 | 10, 5a | yes | 60.600 |
| m27 | S066 | 1 | «honesta» out | «el stop se queda donde lo puso el plan» |
| m27 | S068 | 5 | split | 62.300, «exactamente +2R», 40%, 60.300, 60%, 64.000 |
| m27 | S072 | 5 | split | 62.300, +0,8R, 0 |
| m27 | S081 | 4 | tag out | +3,7R ≈ +370 USDT, +3,0R ≈ +300 USDT |
| m27 | S084 | 9, 10 | approved sample | «segundo límite, separado» |
| m27 | S085–S088 | — | no | X = 2%, 200 USDT, −1R, «dos stops» |
| m27 | S089 | 5a | approved sample | «1 y el 3%», «parte baja», «antes del día malo, nunca durante él» |
| m27 | S091 | 2, 5 | split ×2 | −3% |
| m27 | S097 | 5 | split | «0,1 BTC», «dimensionar desde el stop» |
| m27 | S098 | 9, 5 | split, term | 00:00 UTC |
| m27 | S099 | 1, 5 | «simplemente» out | −2%, «3 de la madrugada» |
| m27 | S100–S102 (summary) | 5, 9 | term rename in S102 only | everything else in the summary byte-identical |
| m27 | guard | — | — | «setup generado» / «generated setup» on one line |

## Full text, ES, before and after

Lesson body as it reads in `content/es/lessons/`. Exercises are omitted.

### m08-l1, before (`f0d0e68`)

````markdown
# Estructura de precio

El precio no vaga al azar. Deja un registro visible de dónde pelearon compradores y vendedores, y ese
registro —la estructura— es la lectura de gráfico más honesta que puedes hacer, porque es el
precio en sí, no un indicador derivado de él. Todo lo de esta lección es una forma de leer ese
registro: dónde se frenó el precio, dónde rompió y si las rupturas significaron algo.

## Soportes y resistencias son zonas, no líneas

Un soporte es una zona de precio donde la compra ha entrado repetidamente y ha frenado una caída.
Una resistencia es una zona donde la venta ha tapado repetidamente una subida. La palabra que hay
que retener es *zona*.

¿Por qué la compra reaparece de forma fiable en el mismo sitio? Porque el sitio se recuerda, y el
recuerdo se convierte en órdenes. Los traders que compraron el último rebote y lo vieron funcionar
dejan órdenes de compra para volver a hacerlo. Los que se perdieron el rebote esperan ahí una segunda
oportunidad. Los que compraron demasiado arriba y están en pérdidas colocan ahí su salida a break-even
(punto de equilibrio). Un soporte no es magia en el número: es un estante de órdenes de compra en
reposo que las últimas visitas enseñaron a la gente a dejar. La resistencia es el mismo estante, hecho
de órdenes de venta.

Por eso también es una zona, no una línea —una banda de unas cuantas velas de ancho— porque:

- Distintos traders colocaron sus órdenes a precios ligeramente distintos.
- Mechas y cierres cuentan historias diferentes; el "nivel" queda repartido entre ambos.
- Cuantas más veces se testea una zona, más ancha y más real se vuelve, no más precisa.

Caso concreto: supón que BTC ha girado al alza tres veces en el mismo vecindario —una vez pinchó con
la mecha hasta 58.050 y cerró de vuelta en 58.600, otra vez hizo base en torno a 58.300 durante varias
velas, otra cayó a 58.150 en el intradía y se recuperó—. No hay un único *precio* de soporte en esa
historia. Hay un estante de unos 58.000–58.400 de ancho. Traza la zona a partir de los cuerpos y
mechas de los swings que de verdad giraron, y espera que el precio reaccione *en algún punto dentro
de ella*, no en un número exacto.

:::note{type=warning}
La herida autoinfligida más común: trazar un nivel, ver que el precio lo falla por un 0,3% y concluir
"el soporte ha fallado". No falló: dibujaste una línea donde el mercado dibujó una banda. Una zona
que se toca y aguanta está haciendo su trabajo.
:::

## Ruptura vs fakeout

Tarde o temprano el precio sale del rango. La pregunta es si lo hizo *en serio*.

- Una ruptura genuina cierra con decisión más allá del nivel —un cuerpo de vela entero al
  otro lado— y luego aguanta ahí, idealmente volviendo a *retestear* el antiguo nivel como nuevo
  soporte (o resistencia) y rebotando. Punto extra si la ruptura ocurre con más volumen: hizo
  falta participación real para atravesarlo.
- Un fakeout (falsa ruptura) asoma más allá del nivel —a menudo con una mecha larga— y luego
  cierra de vuelta dentro del rango. La ruptura es rechazada. Estos atrapan a los traders que
  compraron la primera vela pasada la línea.

Ambos tienen un mecanismo, y conviene entenderlo en vez de memorizarlo. Una ruptura genuina suele
retestear y aguantar por *inversión de roles*: los vendedores que defendían la antigua resistencia
han sido arrollados y muchos cierran sus cortos en el retroceso hacia el nivel, convirtiendo a los
antiguos vendedores en compradores; mientras tanto, los compradores que se negaron a perseguir el
precio consiguen por fin su entrada en la antigua línea. El nivel que antes tapaba el precio ahora lo
sostiene: la resistencia se vuelve soporte. El retest es el mercado votando por segunda vez.

Un fakeout ocurre porque el nivel obvio es exactamente donde se apilan las órdenes en reposo justo
más allá de él: los stops de los traders posicionados contra el nivel, y las órdenes de compra de los
traders de ruptura que dejan instrucciones de "compra si rompe". Empuja el precio un pelo más allá del
nivel y las disparas todas a la vez: un estallido de compras sin nada real detrás. Cuando ese
combustible se agota, el precio cae de vuelta dentro, y quienes compraron el asomo quedan ahora
atrapados por encima del nivel y motivados para vender. La falsa ruptura no falló por accidente: se
quedó sin las mismas órdenes que la provocaron.

En concreto, con los números de la figura de abajo: la resistencia está en torno a 2.130, y los dos
paneles son literalmente el mismo gráfico —el mismo rango, las mismas velas— hasta el momento de la
decisión. A la izquierda, una ruptura genuina: el precio cierra por encima de la línea, sigue
empujando hasta 2.225 y ya no vuelve. A la derecha, un fakeout: el mismo asomo llega a 2.166,
aguanta media docena de velas por encima y luego las pierde —cierra de vuelta bajo 2.130, pierde
2.035 en pocas velas y sigue cayendo desde ahí—. Mismo nivel, mismas primeras velas: solo el cierre
*que aguanta* y lo que viene después los distinguen.

::figure{id=fig-m08-breakout-vs-fakeout}

El discriminador más útil: **espera al cierre, y a que ese cierre aguante.** Una mecha que atraviesa
un nivel es un rumor; unas pocas velas cerrando al otro lado son un titular sin confirmar —el panel
de la derecha las tiene y aun así fracasa—; un cuerpo que cierra más allá y *se queda* es la noticia.

:::note{type=info}
Nadie puede distinguir una ruptura de un fakeout en el instante en que el precio cruza la línea: ni
tú, ni nadie. Por eso los traders pacientes esperan el cierre más allá, y a menudo el retest,
aceptando que se perderán el primer tramo del movimiento a cambio de no quedar atrapados por la
mayoría de los fakeouts.
:::

## Estructura de mercado: HH/HL y LH/LL

Aléjate del nivel único y mira la secuencia de swings.

- Una tendencia alcista es una escalera de máximos más altos (HH) y mínimos más altos
  (HL): cada subida supera el pico anterior y cada retroceso hace suelo por encima del anterior.
- Una tendencia bajista es el espejo: máximos más bajos (LH) y mínimos más bajos (LL).
  Cada rebote falla más abajo, cada caída llega más lejos.

¿Para qué molestarse en nombrar la escalera? Porque la secuencia te dice quién va ganando sin
preguntarle a ningún indicador. Máximos más altos significan que los compradores siguen encontrando
otros compradores dispuestos a pagar más; mínimos más altos significan que cada retroceso se compra
antes de devolver la última ganancia. Mientras eso se cumpla, el camino de menor resistencia es hacia
arriba, y apostar en contra es apostar contra el equilibrio de fuerzas visible. En cuanto la escalera
se detiene, se detiene también la suposición.

Una tendencia alcista limpia podría leerse así: mínimo en 100, máximo en 110, retroceso a 104 (un
mínimo más alto), máximo en 118 (un máximo más alto), retroceso a 109 (mínimo más alto), máximo en
126. Cada mínimo por encima del mínimo anterior, cada máximo por encima del máximo anterior: una
escalera que podrías describirle a alguien por teléfono.

Un pullback es el movimiento en contra *dentro* de una tendencia: los retrocesos a 104 y 109 de
arriba. Existe porque no todos actúan a la vez: algunos compradores toman ganancias durante la subida,
algunos vendedores tardíos prueban suerte, y el precio devuelve parte del último tramo antes de que la
tendencia se reanude. Es la tendencia tomando aire, no girándose. La trampa es que en el momento en
que se forma no puedes distinguir un pullback del inicio de un giro: solo el siguiente swing lo
resuelve. Un retroceso a 109 que vuelve a girar al alza hacia un nuevo máximo *era* un pullback; el
mismo retroceso que sigue cayendo y rompe 104 era la primera grieta.

## Cambio de carácter

Una tendencia sigue intacta mientras la escalera continúa. Se rompe con un cambio de carácter
(CHoCH): el primer swing que viola el patrón.

En una tendencia alcista, eso es la primera vez que el precio hace un mínimo más bajo: no logra
mantenerse por encima del HL anterior. En una bajista, es el primer máximo más alto. ¿Por qué pesa
tanto esa primera ruptura? Porque toda la tendencia alcista se apoyaba en un mecanismo: que cada
retroceso se compraba por encima del retroceso anterior. Un mínimo más bajo es la primera vez que ese
mecanismo falla de forma visible: los compradores no aparecieron donde venían apareciendo. En la
escalera de arriba, el precio cayendo desde 126, pasando por 109, hasta un mínimo de 106 es un cambio de
carácter: el primer mínimo más bajo en una serie que solo había hecho mínimos más altos.

Al gemelo de ese giro también le han puesto nombre, aunque este curso no lo necesite para explicar la
escalera: cada máximo más alto que se lleva por delante el máximo anterior es una ruptura de
estructura (BOS), la ruptura que *confirma* el patrón, frente al CHoCH, que lo rompe. Una escalera,
dos clases de ruptura. Ese vocabulario —y el resto del dialecto que lo acompaña— se mapea sobre esta
misma mecánica en m34-l1.

Todo en esta lección traza sus niveles en horizontal, que es donde está el mecanismo. La misma estructura
también puede describirse con líneas *inclinadas* —líneas de tendencia y canales— y m15-l1 lo retoma,
incluida la explicación honesta de cuánto más débil es la afirmación de la versión inclinada.

La figura pone esa comparación lado a lado, con cada swing etiquetado: a la izquierda una escalera que
sigue subiendo, a la derecha la misma escalera cuyo último swing falla. Cada panel es una
instancia generada con sus propios precios —los números de la escalera de arriba son proporciones
para que la secuencia se pueda seguir de memoria, no una cotización que buscar—; lo que hay que leer es
la forma y las etiquetas.

::figure{id=fig-m08-market-structure}

El cambio de carácter no es una promesa de que la tendencia se haya girado; es el primer *indicio*
de que la regla de la vieja tendencia ha dejado de funcionar. A menudo precede a una transición más
larga o a un rango, no a un giro limpio.

:::note{type=warning}
El "cambio de carácter" se vende como una señal mágica de giro. No lo es. Es un patrón roto: un
motivo para dejar de dar por sentada la vieja tendencia y empezar a vigilar qué la sustituye. Un solo
mínimo más bajo en una tendencia alcista puede ser un pullback profundo que luego se reanuda; trata
el CHoCH como una pregunta, no como una respuesta.
:::

## La lectura errónea que sale cara

Dos errores causan casi todo el daño que este tema provoca.

**Perseguir la primera vela pasada un nivel.** La ruptura parece obvia, la vela es verde y rápida, y
el miedo a perdérsela ahoga el plan, así que compras el asomo. Pero el asomo es precisamente de lo que
está hecho un fakeout: has comprado el estallido de stops disparados y órdenes de ruptura al peor
precio posible, instantes antes de que se gire de vuelta dentro. Esperar al cierre, y a menudo al
retest, te cuesta los primeros puntos y te ahorra la mayoría de estas trampas. La primera vela pasada
un nivel es la vela más cara de operar.

**Cantar un giro con un solo cambio de carácter.** Un único mínimo más bajo parece un permiso para
ponerte corto y contrariar toda la tendencia previa. Pero un CHoCH es un patrón roto, no una tendencia
nueva, y las tendencias fuertes imprimen algún que otro mínimo más bajo dentro de un pullback profundo
continuamente. Cambia todo tu sesgo con el primero y la tendencia te arrollará en la reanudación.
Trata el CHoCH como una pregunta —*¿ha cambiado de verdad el control?*— y espera la respuesta: un
máximo más bajo tras el mínimo más bajo, un intento fallido de recuperar el nivel, una segunda
ruptura que confirme.

:::note{type=warning}
Ambos errores comparten una raíz: actuar con la *primera* señal en lugar de con la *confirmada*. El
mercado paga una prima a quien está dispuesto a llegar una o dos velas tarde a cambio de quedar
atrapado mucho menos a menudo.
:::

## El cripto abre 24/7, y eso tuerce estos patrones

Los mercados tradicionales cierran; el cripto nunca lo hace, y ese libro de órdenes siempre activo
cambia cómo se comporta la estructura.

**Fakeouts de fin de semana y de libro poco profundo.** Sin campana de cierre, las horas muertas —los fines de
semana y el tramo en que todas las zonas horarias importantes duermen a la vez— funcionan con un libro
de órdenes fino. Menos órdenes en reposo significa que hace falta mucho menos tamaño para empujar el
precio más allá de un nivel obvio, así que las falsas rupturas se concentran justo en estas ventanas.
Una "ruptura" impresa a las 4 de la madrugada de un domingo merece más recelo que la misma ruptura
en una sesión concurrida de un día laborable; puede que el nivel simplemente se haya atravesado
empujando aire vacío y vuelva de golpe cuando regrese el volumen real.

**Mechas de caza de stops.** El apalancamiento concentra los stops y los precios de liquidación justo
más allá de los máximos y mínimos de swing obvios: todos miran los mismos niveles, así que las órdenes
de protección de todos acaban en la misma banda estrecha. En un libro poco profundo, un participante grande
puede empujar el precio hasta esa banda, disparar los stops apilados y forzar la liquidación de los
traders sobreapalancados, absorber la avalancha de órdenes resultante y dejar que el precio vuelva de
golpe, dejando una mecha larga que perforó el nivel y cerró muy lejos de él. (Recuerda: una
*liquidación* aquí es el exchange cerrando a la fuerza esas posiciones sobreapalancadas, no una venta
ordinaria.) Por eso la mecha que asoma por tu nivel suele ser más larga y más traicionera en cripto
que la versión de manual, y por eso el cierre, nunca el extremo, es la única lectura honesta de si
un nivel rompió de verdad.

## Leer un gráfico en orden

1. Marca primero las zonas obvias, las que un desconocido rodearía con un círculo. Si tienes que
   entornar los ojos, no es un nivel.
2. Lee la secuencia de swings: ¿estás en HH/HL, en LH/LL, o en un rango desordenado sin ninguno de
   los dos?
3. En un nivel, espera al cierre. Más allá y aguantando = ruptura; más allá y luego de vuelta
   dentro = fakeout. Y pregúntate *cuándo* ocurrió la ruptura: una ruptura en la liquidez muerta del
   fin de semana es una señal más débil que la misma ruptura en una sesión concurrida.
4. Deja que el mercado confirme antes de rebautizar un pullback como giro. El cambio de carácter es
   el aviso honesto más temprano; ni uno antes.
````

### m08-l1, after

````markdown
# Estructura de precio

El precio no vaga al azar. Deja un registro visible de dónde pelearon compradores y vendedores. Ese
registro es la estructura, y es la lectura de gráfico más directa que puedes hacer: es el precio en
sí, no un indicador derivado de él. Leer ese registro es ver dónde se frenó el precio, dónde rompió y
si las rupturas significaron algo.

## Soportes y resistencias son zonas, no líneas

Un soporte es una zona de precio donde la compra ha entrado repetidamente y ha frenado una caída.
Una resistencia es una zona donde la venta ha tapado repetidamente una subida. La palabra que hay
que retener es *zona*.

La compra reaparece de forma fiable en el mismo sitio porque el sitio se recuerda, y el recuerdo se
convierte en órdenes. Los traders que compraron el último rebote y lo vieron funcionar dejan órdenes
de compra para volver a hacerlo. Los que se perdieron el rebote esperan ahí una segunda oportunidad.
Los que compraron demasiado arriba y están en pérdidas colocan ahí su salida a break-even (punto de
equilibrio). Un soporte no es magia en el número: es una zona con órdenes de compra en reposo, que
las últimas visitas enseñaron a la gente a dejar ahí. La resistencia es lo mismo con órdenes de
venta.

Por eso también es una zona, no una línea —una banda de unas cuantas velas de ancho— porque:

- Distintos traders colocaron sus órdenes a precios ligeramente distintos.
- Mechas y cierres cuentan historias diferentes; el "nivel" queda repartido entre ambos.
- Cuantas más veces se testea una zona, más ancha y más real se vuelve, no más precisa.

Caso concreto: supón que BTC ha girado al alza tres veces en el mismo vecindario. Una vez pinchó con
la mecha hasta 58.050 y cerró de vuelta en 58.600, otra vez hizo base en torno a 58.300 durante
varias velas, otra cayó a 58.150 en el intradía y se recuperó. No hay un único *precio* de soporte
en esa historia. Hay una zona de unos 58.000–58.400 de ancho. Traza la zona a partir de los cuerpos
y mechas de los swings que giraron. Espera que el precio reaccione *en algún punto dentro de ella*,
no en un número exacto.

:::note{type=warning}
La herida autoinfligida más común: trazar un nivel, ver que el precio lo falla por un 0,3% y concluir
"el soporte ha fallado". No falló: dibujaste una línea donde el mercado dibujó una banda. Una zona
que se toca y aguanta está haciendo su trabajo.
:::

## Ruptura vs fakeout

Tarde o temprano el precio sale del rango. La pregunta es si lo hizo *en serio*.

- Una ruptura genuina cierra con decisión más allá del nivel —un cuerpo de vela entero al
  otro lado— y luego aguanta ahí. Idealmente, vuelve a *retestear* el antiguo nivel como nuevo
  soporte (o resistencia) y rebota. Punto extra si la ruptura ocurre con más volumen: hizo
  falta participación real para atravesarlo.
- Un fakeout (falsa ruptura) asoma más allá del nivel —a menudo con una mecha larga— y luego
  cierra de vuelta dentro del rango. La ruptura es rechazada. Estos atrapan a los traders que
  compraron la primera vela pasada la línea.

Una ruptura genuina suele retestear y aguantar por *inversión de roles*. Los vendedores que
defendían la antigua resistencia han sido arrollados, y muchos cierran sus cortos en el retroceso
hacia el nivel: los antiguos vendedores pasan a ser compradores. Mientras tanto, los compradores que
se negaron a perseguir el precio consiguen por fin su entrada en la antigua línea. El nivel que
antes tapaba el precio ahora lo sostiene: la resistencia se vuelve soporte.

Un fakeout ocurre porque las órdenes en reposo se apilan justo más allá del nivel obvio. Son los
stops de los traders posicionados contra el nivel y las órdenes de compra de los traders de ruptura,
que dejan instrucciones de "compra si rompe". Empuja el precio un pelo más allá del nivel y las
disparas todas a la vez: un estallido de compras sin nada real detrás. Cuando esas órdenes se
agotan, el precio cae de vuelta dentro. Quienes compraron la primera vela que cruza el nivel quedan
ahora atrapados por encima del nivel y motivados para vender.

En concreto, con los números de la figura de abajo: la resistencia está en torno a 2.130. Los dos
paneles son el mismo gráfico —el mismo rango, las mismas velas— hasta el momento de la decisión. A
la izquierda, una ruptura genuina: el precio cierra por encima de la línea, sigue empujando hasta
2.225 y ya no vuelve. A la derecha, un fakeout: la misma ruptura llega a 2.166, aguanta media docena
de velas por encima y luego las pierde. Cierra de vuelta bajo 2.130, pierde 2.035 en pocas velas y
sigue cayendo desde ahí.

::figure{id=fig-m08-breakout-vs-fakeout}

El discriminador más útil: **espera al cierre, y a que ese cierre aguante.** Una mecha que atraviesa
un nivel no basta, y unas pocas velas cerrando al otro lado tampoco: el panel de la derecha las tiene
y aun así fracasa. Lo que cuenta es un cuerpo que cierra más allá y *se queda*.

:::note{type=info}
Nadie puede distinguir una ruptura de un fakeout en el instante en que el precio cruza la línea: ni
tú, ni nadie. Por eso los traders pacientes esperan el cierre más allá, y a menudo el retest,
aceptando que se perderán el primer tramo del movimiento a cambio de no quedar atrapados por la
mayoría de los fakeouts.
:::

## Estructura de mercado: HH/HL y LH/LL

Aléjate del nivel único y mira la secuencia de swings.

- Una tendencia alcista es una secuencia de máximos más altos (HH) y mínimos más altos
  (HL). Cada subida supera el pico anterior y cada retroceso hace suelo por encima del anterior.
- Una tendencia bajista es el espejo: máximos más bajos (LH) y mínimos más bajos (LL).
  Cada rebote falla más abajo, cada caída llega más lejos.

La secuencia de máximos y mínimos te dice quién va ganando sin preguntarle a ningún indicador.
Máximos más altos significan que los compradores siguen encontrando otros compradores dispuestos a
pagar más; mínimos más altos significan que cada retroceso se compra antes de devolver la última
ganancia. Mientras eso se cumpla, el camino de menor resistencia es hacia arriba, y apostar en
contra es apostar contra el equilibrio de fuerzas visible. Cuando la secuencia se interrumpe, esa
suposición deja de valer.

Una tendencia alcista limpia podría leerse así: mínimo en 100, máximo en 110, retroceso a 104 (un
mínimo más alto), máximo en 118 (un máximo más alto), retroceso a 109 (mínimo más alto), máximo en
126. Cada mínimo por encima del mínimo anterior, cada máximo por encima del máximo anterior: una
secuencia que podrías describirle a alguien por teléfono.

Un pullback es el movimiento en contra *dentro* de una tendencia: los retrocesos a 104 y 109 de
arriba. Existe porque no todos actúan a la vez. Algunos compradores toman ganancias durante la
subida, algunos vendedores tardíos prueban suerte, y el precio devuelve parte del último tramo antes
de que la tendencia se reanude. Es la tendencia tomando aire, no girándose. La trampa es que en el
momento en que se forma no puedes distinguir un pullback del inicio de un giro: solo el siguiente
swing lo resuelve. Un retroceso a 109 que vuelve a girar al alza hacia un nuevo máximo *era* un
pullback; el mismo retroceso que sigue cayendo y rompe 104 era la primera grieta.

## Cambio de carácter

Una tendencia sigue intacta mientras la secuencia de máximos y mínimos continúa. Se rompe con un
cambio de carácter (CHoCH): el primer swing que viola el patrón.

En una tendencia alcista, eso es la primera vez que el precio hace un mínimo más bajo: no logra
mantenerse por encima del HL anterior. En una bajista, es el primer máximo más alto. Esa primera
ruptura pesa tanto porque toda la tendencia alcista se apoyaba en un mecanismo: que cada retroceso
se compraba por encima del retroceso anterior. Un mínimo más bajo es la primera vez que ese
mecanismo falla de forma visible: los compradores no aparecieron donde venían apareciendo. En la
secuencia de arriba, el precio cayendo desde 126, pasando por 109, hasta un mínimo de 106 es un
cambio de carácter. Es el primer mínimo más bajo en una serie que solo había hecho mínimos más
altos.

Al gemelo de ese giro también le han puesto nombre, aunque este curso no lo necesite para explicar
la estructura. Cada máximo más alto que se lleva por delante el máximo anterior es una ruptura de
estructura (BOS). Es la ruptura que *confirma* el patrón, frente al CHoCH, que lo rompe. Una
estructura, dos clases de ruptura. Ese vocabulario —y el resto del dialecto que lo acompaña— se
mapea sobre esta misma mecánica en m34-l1.

Todo en esta lección traza sus niveles en horizontal, que es donde está el mecanismo. La misma
estructura también puede describirse con líneas *inclinadas* —líneas de tendencia y canales—. Lo
retoma m15-l1, incluida la explicación de cuánto más débil es la afirmación de la versión inclinada.

La figura pone esa comparación lado a lado, con cada swing etiquetado: a la izquierda una secuencia
que sigue subiendo, a la derecha la misma secuencia cuyo último swing falla. Cada panel es una
instancia generada con sus propios precios. Los números del ejemplo de arriba son proporciones para
que la secuencia se pueda seguir de memoria, no una cotización que buscar. Lo que hay que leer es la
forma y las etiquetas.

::figure{id=fig-m08-market-structure}

El cambio de carácter no es una promesa de que la tendencia se haya girado. Es el primer *indicio*
de que la regla de la vieja tendencia ha dejado de funcionar. A menudo precede a una transición más
larga o a un rango, no a un giro limpio.

:::note{type=warning}
El "cambio de carácter" se vende como una señal mágica de giro. No lo es. Es un patrón roto: un
motivo para dejar de dar por sentada la vieja tendencia y empezar a vigilar qué la sustituye. Un solo
mínimo más bajo en una tendencia alcista puede ser un pullback profundo que luego se reanuda; trata
el CHoCH como una pregunta, no como una respuesta.
:::

## La lectura errónea que sale cara

Dos errores causan casi todo el daño que este tema provoca.

**Perseguir la primera vela pasada un nivel.** La ruptura parece obvia y la vela es verde y rápida.
El miedo a perdérsela ahoga el plan, así que compras la primera vela que cruza el nivel. Pero un
fakeout está hecho de esa vela. Has comprado el estallido de stops disparados y órdenes de ruptura
al peor precio posible, instantes antes de que se gire de vuelta dentro. Esperar al cierre, y a
menudo al retest, te cuesta los primeros puntos y te ahorra la mayoría de estas trampas. La primera
vela pasada un nivel es la vela más cara de operar.

**Cantar un giro con un solo cambio de carácter.** Un único mínimo más bajo parece un permiso para
ponerte corto y contrariar toda la tendencia previa. Pero un CHoCH es un patrón roto, no una
tendencia nueva, y las tendencias fuertes imprimen algún que otro mínimo más bajo dentro de un
pullback profundo continuamente. Cambia todo tu sesgo con el primero y la tendencia te arrollará en
la reanudación. Trata el CHoCH como una pregunta: *¿ha cambiado el control?* Espera la respuesta: un
máximo más bajo tras el mínimo más bajo, un intento fallido de recuperar el nivel, una segunda
ruptura que confirme.

:::note{type=warning}
Ambos errores comparten una raíz: actuar con la *primera* señal en lugar de con la *confirmada*. El
mercado paga una prima a quien está dispuesto a llegar una o dos velas tarde a cambio de quedar
atrapado mucho menos a menudo.
:::

## El cripto abre 24/7, y eso tuerce estos patrones

Los mercados tradicionales cierran; el cripto nunca lo hace, y ese libro de órdenes siempre activo
cambia cómo se comporta la estructura.

**Fakeouts de fin de semana y de libro poco profundo.** Sin campana de cierre, las horas muertas
funcionan con un libro de órdenes fino. Son los fines de semana y el tramo en que todas las zonas
horarias importantes duermen a la vez. Menos órdenes en reposo significa que hace falta mucho menos
tamaño para empujar el precio más allá de un nivel obvio. Por eso las falsas rupturas se concentran
en estas ventanas. Una "ruptura" impresa a las 4 de la madrugada de un domingo merece más recelo que
la misma ruptura en una sesión concurrida de un día laborable. Puede que el nivel se haya atravesado
empujando aire vacío y vuelva de golpe cuando regrese el volumen real.

**Mechas de caza de stops.** El apalancamiento concentra los stops y los precios de liquidación
justo más allá de los máximos y mínimos de swing obvios. Todos miran los mismos niveles, así que las
órdenes de protección de todos acaban en la misma banda estrecha. En un libro poco profundo, un
participante grande puede empujar el precio hasta esa banda, disparar los stops apilados y forzar la
liquidación de los traders sobreapalancados. Después puede absorber la avalancha de órdenes
resultante y dejar que el precio vuelva de golpe. Queda una mecha larga que perforó el nivel y cerró
muy lejos de él. (Recuerda: una *liquidación* aquí es el exchange cerrando a la fuerza esas
posiciones sobreapalancadas, no una venta ordinaria.) Por eso, en cripto, la mecha que perfora tu
nivel suele ser más larga que en los manuales. Para saber si un nivel ha roto, mira el cierre, nunca
el extremo.

## Leer un gráfico en orden

1. Marca primero las zonas obvias, las que un desconocido rodearía con un círculo. Si tienes que
   entornar los ojos, no es un nivel.
2. Lee la secuencia de swings: ¿estás en HH/HL, en LH/LL, o en un rango desordenado sin ninguno de
   los dos?
3. En un nivel, espera al cierre. Más allá y aguantando = ruptura; más allá y luego de vuelta
   dentro = fakeout. Y pregúntate *cuándo* ocurrió la ruptura: una ruptura en la liquidez muerta del
   fin de semana es una señal más débil que la misma ruptura en una sesión concurrida.
4. Deja que el mercado confirme antes de rebautizar un pullback como giro. El cambio de carácter es
   el aviso fiable más temprano; antes no hay ninguno.
````

### m27-l1, before (`f0d0e68`)

````markdown
# Anatomía de una operación completa

Has aprendido las piezas por separado: estructura, confluencia, la reacción en un nivel, dimensionar
desde el stop, esperanza matemática. Una operación es esas piezas ensambladas en una sola cadena
ininterrumpida, decidida de antemano y luego simplemente ejecutada. Esta lección recorre una única
operación de principio a fin, con números, para que veas el proceso entero de golpe, y para que veas
que, cuando el dinero está en riesgo, casi todas las decisiones ya están tomadas.

Operaremos una cuenta de 10.000 USDT y arriesgaremos el 1% —100 USDT— en esta única idea.
Ten presente ese número: todo lo que viene después está construido para que equivocarse cueste exactamente
eso y nada más.

## El contexto: qué ofrece el mercado

Empieza por la lente más amplia, la pregunta del bloque D: ¿qué está *haciendo* el mercado y ofrece
algo? En el gráfico diario, BTC está en una tendencia alcista limpia —una secuencia de máximos más
altos y mínimos más altos— y acaba de retroceder tras un empuje hasta 64.000. Un retroceso dentro
de una tendencia alcista es justo lo que queremos: una oportunidad de unirnos a la tendencia a mejor
precio, con la propia tendencia de nuestro lado.

**Por qué empezar aquí:** el contexto decide si hay operación siquiera. En un rango o una tendencia
bajista, este mismo setup sería una apuesta distinta y peor. La mayor parte del tiempo la respuesta
honesta a «¿qué se ofrece?» es *nada limpio*, y la mejor operación es ninguna. Hoy hay un retroceso en
una tendencia alcista, así que miramos más de cerca.

## De arriba abajo: qué decide cada gráfico

Esa lectura salió del gráfico diario, y de qué gráfico salió forma parte del método. Las
temporalidades anidadas (m03-l2) y la elección de temporalidad según el estilo (m23) implican un paso
del proceso que ninguna de las dos deja escrito, así que aquí queda nombrado: la temporalidad superior
dicta el sesgo, la temporalidad inferior dicta la entrada, y el orden no es reversible.

- **Marco macro → sesgo y niveles.** En el gráfico lento decides *en qué dirección tienes permiso para
  operar y a qué precios*. Aquí el diario da la tendencia alcista, el retroceso y las zonas de 60.000 y
  64.000. El emparejamiento cambia con tu estilo —un day trader lee el sesgo en 4H/1D, un scalper en
  1H— pero la jerarquía no.
- **Marco micro → trigger y stop.** Solo entonces bajas al gráfico rápido, y solo para responder
  *cuándo exactamente y dónde está muerta la idea*. En esta operación la vela de rechazo de más abajo es
  un cierre de 1 hora, y el stop se mide desde la mecha de esa vela.

**Por qué el orden no se puede invertir:** el marco micro imprime señales constantemente, en las dos
direcciones. Déjale elegir la dirección y siempre encontrarás una que apunte donde ya querías ir: es el
aviso de m03-l2 sobre saltar entre niveles de zoom para justificar una posición, llegando un paso antes.
Así que una señal del marco micro que contradice el sesgo macro es una operación descartada, no una
oportunidad de operar en contra: un largo limpio en 1 hora dentro de una tendencia bajista diaria es
justo la operación que este protocolo existe para rechazar.

## El setup: la estructura se encuentra con la confluencia

Acércate al retroceso, todavía en el marco macro. El precio cae hacia 60.000, y allí coinciden tres
cosas independientes: es el máximo previo que se rompió al subir (la vieja resistencia pasa a
soporte), es el retroceso 0,618 del último tramo, y la EMA de 50 al alza trepa hacia la misma
zona. Eso es confluencia: tres razones sin relación apuntando a un precio. Ninguna *crea* el nivel;
juntas hacen de 60.000 el lugar donde es más probable que la tendencia se reanude.

**Por qué confluencia y no una sola línea:** cualquier nivel aislado falla a menudo. Que fallen tres a
la vez es mucho menos probable, así que las probabilidades de que 60.000 aguante son mejores que las
que daría una sola herramienta. La confluencia es como conviertes un nivel a cara o cruz en un lugar
donde vale la pena arriesgar dinero.

## El trigger: la reacción en el nivel

Un nivel es un *lugar que vigilar*, nunca una razón para comprar por sí solo. Que el precio llegue a
60.000 no es la señal; la señal es cómo reacciona el precio ahí. Esperamos la reacción en el marco
micro (véase m08-l2): el precio se hunde hasta 59.700, se forma una mecha inferior larga y la vela de
1 hora cierra de vuelta en 60.300, una vela de rechazo. Los vendedores empujaron por debajo del
nivel, fueron absorbidos y perdieron. *Eso* es el trigger. Entramos en el cierre: 60.300.

**Por qué esperar el trigger:** comprar el nivel a ciegas da por hecho que aguantará; esperar la
reacción obliga al mercado a demostrar que los compradores aparecieron de verdad antes de
comprometerte. Cuesta un poco de precio (compras a 60.300, no a 60.000) a cambio de pruebas: una
operación que puedes rechazar si la reacción nunca llega.

## El stop: dónde la idea está equivocada

Antes de dimensionar, decide dónde la idea está muerta. Toda la tesis es «los compradores defienden
60.000». Si el precio cierra bien por debajo de la mecha de rechazo —digamos por debajo de 59.300—
esa tesis es sencillamente falsa: el nivel no aguantó. Así que el stop va en 59.300, un poco por
debajo del mínimo de la mecha.

**Por qué ahí y en ningún otro sitio:** el stop pertenece al precio que *invalida el setup*, no a la
cantidad de dinero que te apetece perder. Colocado en la estructura, que te salte significa algo real
—te equivocaste con el nivel— en vez de ser una distancia aleatoria que el mercado atraviesa con una
mecha por ruido. Entrada 60.300, stop 59.300, así que el riesgo por unidad es de 1.000 en precio.
Llama a esa distancia 1R.

## El tamaño: desde el stop, no desde la tripa

Ahora —y solo ahora— el tamaño. El presupuesto es 100 USDT; la pérdida por unidad en el stop es 1.000.
Entonces:

`tamaño = presupuesto de riesgo ÷ distancia del stop = 100 ÷ 1.000 = 0,1 unidades` (0,1 BTC).

Es la fórmula de m22 aplicada: mantén 0,1 BTC y que te salten en 59.300 pierde `0,1 × 1.000 = 100
USDT`, exactamente el 1%, por muy seguro que te sientas. El objetivo es la siguiente oferta obvia, el
máximo previo de 64.000: a 3.700 de distancia, unos 3,7R. Arriesgar 1R para ganar ~3,7R es
el tipo de apuesta desequilibrada sobre la que se construye la esperanza matemática (m25).

Esos cuatro precios —el nivel, la entrada, el stop y el objetivo— son la operación entera, y son lo que
un trader dibuja de verdad en el gráfico. La figura los dibuja sobre un setup generado con la misma
anatomía: lee la forma, no los números, que se quedan en el texto de arriba.

::figure{id=fig-m27-trade-anatomy}

**Por qué el tamaño al final:** el stop sale del gráfico, el tamaño sale del stop. Hazlo en ese orden y
el riesgo es constante en cada operación sin importar el precio ni el apalancamiento; invíertelo
—elige un tamaño y luego busca un stop que «encaje»— y vuelves a apostar.

## Gestionar la posición viva

La posición está abierta. La habilidad más difícil ahora es no hacer casi nada. El plan ya está
hecho; la gestión en vivo es una lista corta de acciones legítimas y una lista larga de tentaciones.

- **Mover el stop a break-even: con un test, no con una sensación.** «¿Legítimo o miedo?» no es
  una pregunta para resolver por estado de ánimo con dinero en juego, así que hazla comprobable. El
  stop se mueve a break-even solo cuando la operación ha producido una confirmación nueva a su favor en
  la temporalidad de ejecución: una ruptura de estructura en la dirección de la operación, que en este
  largo significa un nuevo máximo más alto y después el mínimo más alto que le sigue, ambos por encima de
  la entrada, en el gráfico de 1 hora del que salió la entrada. Aquí el precio empuja a 62.300 y
  retrocede a un mínimo más alto en 61.200: test superado, así que el stop va a 60.300 y estás siguiendo
  al gráfico. Estar en verde *no* es el test. El verde es donde vive el ruido —una sola vela hasta 60.600
  es un número que el mercado marca y borra todo el día— mientras que la estructura es algo que el
  precio ha tenido que *construir*. Así que hazte la pregunta en voz alta: ¿qué ha hecho esta operación a
  mi favor que no hubiera hecho antes? Si la única respuesta honesta es «está en verde», el stop se queda
  donde lo puso el plan.
- **Tomas de beneficio parciales: una elección de estilo, con su precio honesto.** El patrón habitual es
  cerrar un 30–50% en el primer nivel contrario y dejar correr el resto de la posición con el stop en break-even. En
  esta operación el primer nivel contrario es el máximo menor en 62.300, exactamente +2R: vendes ahí
  el 40%, mueves el stop a 60.300 y dejas el 60% apuntando a 64.000. Es una forma legítima de asegurar
  avance y quitarle carga emocional al resto, pero la frase que lo vende —un «runner sin riesgo»— es
  donde tiene que entrar la honestidad, porque ese runner no es gratis y puedes ponerle precio exacto.
  Esta ganadora devuelve `0,4 × 2R + 0,6 × 3,7R = 3,0R` en vez de 3,7R: el runner gratis costó 0,7R
  del payoff de esta operación. Recortar las ganadoras de forma sistemática baja tu payoff medio, y el
  payoff es la mitad de la esperanza matemática (m25). Lo que compras a cambio es una proporción mayor de
  ganancias pequeñas: la operación que se atasca en 62.300 y se da la vuelta ahora sale en +0,8R en
  vez de 0. Si esa operación merece la pena no te lo puede decir nadie en abstracto: son dos versiones
  de *tu* sistema, y el diario (m27-l2) es el único instrumento que puede compararlas. Decídelo en el
  plan, ejecútalo igual siempre y deja que el registro diga qué versión gana.
- **No hacer nada, la mayor parte del tiempo.** Si el precio deambula entre entrada y objetivo y nada
  de la estructura ha cambiado, la acción correcta es ninguna. La operación necesita espacio y tiempo
  para funcionar.
- **La única regla inviolable: el stop solo se mueve a favor de la operación.** Arriba en un largo,
  abajo en un corto; nunca en contra. En el momento en que ensanchas un stop para darle «más
  espacio» a una operación perdedora, has abandonado el plan y has quitado el tope a tu riesgo.

Nos toca el buen caso: el precio sube poco a poco, imprime un mínimo más alto en 61.200 (stop a
break-even) y toca 64.000. Salimos. Resultado: +3,7R ≈ +370 USDT, o +3,0R ≈ +300 USDT si
ejecutamos la versión con parciales de arriba: una operación planificada y ejecutada.

## El freno diario: la regla que cierra el día

Todo lo anterior limita la pérdida de *una* operación a 100 USDT. Nada limita todavía la pérdida de un
día, y un mal día casi nunca es una sola operación. Así que el plan lleva un segundo límite, separado:
un freno diario, que es el límite de pérdida diaria de m26 hecho mecánico. Escríbelo en una frase:
*si el PnL realizado del día llega a −X% de la cuenta, dejo de operar manualmente hasta mañana*. Sin
excepciones, sin «un setup más».

**En la práctica.** Pon X = 2% en esta cuenta de 10.000 USDT y el presupuesto del día son 200 USDT:
exactamente dos pérdidas completas de −1R. Encaja dos stops y la sesión se acabó: gráficos cerrados, sin
tercera idea, por buena que parezca la tercera idea. La X la eliges tú, típicamente entre el 1 y el 3%
(los estilos rápidos que hacen más operaciones al día pertenecen a la parte baja), y se fija en el plan,
antes del día malo, nunca durante él.

**Por qué una regla mecánica y no criterio:** por *quién* tendría que ejercer ese criterio. La persona que
decide si sigue operando tras un −3% es la versión de ti de la que habla todo m26: anclada en volver a
estar en cero, con sensación de urgencia y la persona menos cualificada del mundo para juzgar su propio estado. La
respuesta de m26 era el compromiso previo —decidirlo cuando no hay nada en juego— y el freno diario es esa
doctrina convertida en un número y un corte duro. Funciona precisamente porque no te consulta en el
momento en que menos capaz eres de responder.

:::note{type=warning}
El freno diario es la regla anti-venganza, así que la presión para romperlo llega exactamente cuando
está haciendo su trabajo. «Solo esta vez, el setup es demasiado bueno» es como un día de −2% se convierte
en una semana de −10%: reentras en tilt, subes el tamaño para recuperar, y la pérdida que te negaste a
aceptar en 200 USDT se acepta más tarde a varias veces ese precio. Un freno diario que te saltas no es una
regla, es una preferencia.
:::

## El registro

La operación no termina hasta que está escrita: el setup, el plan (entrada, stop, objetivo, tamaño), lo
que hiciste de verdad y el resultado en R. Ese registro es la materia prima de todo lo de
m27-l2: sin él no puedes distinguir una operación perdedora de un sistema roto.

## Dónde se rompe el plan en tiempo real

:::note{type=warning}
Casi ninguna cuenta muere por malos setups, sino por improvisar a mitad de operación: convertir una
operación planificada en una inventada después de estar en vivo.

**Ensanchar el stop.** El precio se acerca a 59.300 y, en vez de aceptar la pérdida planificada de 100
USDT, deslizas el stop a 58.000 «solo para darle espacio». Has convertido una pérdida conocida y
presupuestada en una abierta. Este único movimiento —mover el stop *en contra*— es el pecado capital, y
con apalancamiento es como un riesgo del 1% se convierte en una liquidación.

**Asfixiar la operación ganadora.** El miedo opuesto: pegas el stop a break-even en la primera vela verde, antes de
cualquier estructura nueva, y te sacan por ruido normal a cambio de nada; luego ves la operación correr
al objetivo sin ti.

**Improvisar una salida.** Cerrar en un precio cualquiera porque «da miedo», o aguantar más allá del
objetivo porque «podría seguir», sustituye tu objetivo planificado por una sensación. El plan nombró la
salida por una razón; tu versión en vivo y emocional no puede renegociarla.
:::

## La operación que dejas abierta el viernes

El mercado está abierto 24/7, así que una operación que colocas el viernes está viva y sin vigilancia
todo el fin de semana, en libros poco profundos donde 60.000 puede recibir una mecha violenta con poco volumen:
una razón más para que protejan el stop y el tamaño, no tu atención. Y como el apalancamiento está a un
clic, la disciplina de *dimensionar desde el stop* es lo que evita que «0,1 BTC» se convierta en
silencio en una posición cuyo stop es una liquidación.

El 24/7 también significa que no hay campana de cierre que te dé por terminado un mal día, así que el
«día» del *freno diario* tienes que definirlo tú: elige una hora de reinicio, escríbela (00:00 UTC, por
ejemplo) y que esa sea la campana. Sin ella, una tarde de −2% simplemente se prolonga en la misma sesión
a las 3 de la madrugada, que es la hora en la que el tilt está menos vigilado.
````

### m27-l1, after

````markdown
# Anatomía de una operación completa

Has aprendido las piezas por separado: estructura, confluencia, la reacción en un nivel, dimensionar
desde el stop, esperanza matemática. Una operación es esas piezas ensambladas en una sola cadena
ininterrumpida, decidida de antemano y luego ejecutada. Vamos a recorrer una única operación de
principio a fin, con números, para ver el proceso entero de golpe. Cuando el dinero está en riesgo,
casi todas las decisiones ya están tomadas.

Operaremos una cuenta de 10.000 USDT y arriesgaremos el 1% —100 USDT— en esta única idea.
Todo lo que viene después está construido para que equivocarse cueste exactamente eso.

## El contexto: qué ofrece el mercado

Empieza por el contexto más amplio, la pregunta del bloque D: ¿qué está *haciendo* el mercado y
ofrece algo? En el gráfico diario, BTC está en una tendencia alcista limpia —una secuencia de
máximos más altos y mínimos más altos— y acaba de retroceder tras un empuje hasta 64.000. Un
retroceso dentro de una tendencia alcista es lo que queremos: una oportunidad de unirnos a la
tendencia a mejor precio, con la propia tendencia de nuestro lado.

**Por qué empezar aquí:** el contexto decide si hay operación siquiera. En un rango o una tendencia
bajista, este mismo setup sería una apuesta distinta y peor. La mayor parte del tiempo la respuesta
a «¿qué se ofrece?» es *nada limpio*, y la mejor operación es ninguna. Hoy hay un retroceso en una
tendencia alcista.

## De arriba abajo: qué decide cada gráfico

Esa lectura salió del gráfico diario, y de qué gráfico salió forma parte del método. Las
temporalidades anidadas (m03-l2) y la elección de temporalidad según el estilo (m23) implican un paso
del proceso que ninguna de las dos deja escrito. Es este: la temporalidad superior dicta el sesgo, la
temporalidad inferior dicta la entrada, y el orden no es reversible.

- **Temporalidad superior → sesgo y niveles.** En la temporalidad superior decides *en qué dirección
  tienes permiso para operar y a qué precios*. Aquí el diario da la tendencia alcista, el retroceso y
  las zonas de 60.000 y 64.000. El emparejamiento cambia con tu estilo —un day trader lee el sesgo en
  4H/1D, un scalper en 1H— pero la jerarquía no.
- **Temporalidad inferior → trigger y stop.** Solo entonces bajas a la temporalidad inferior, y solo
  para responder *cuándo exactamente y dónde está muerta la idea*. En esta operación la vela de
  rechazo de más abajo es un cierre de 1 hora, y el stop se mide desde la mecha de esa vela.

**Por qué el orden no se puede invertir:** la temporalidad inferior imprime señales constantemente,
en las dos direcciones. Déjale elegir la dirección y siempre encontrarás una que apunte donde ya
querías ir. Es el aviso de m03-l2 sobre saltar entre niveles de zoom para justificar una posición,
llegando un paso antes. Así que una señal en la temporalidad inferior que contradice el sesgo de la
superior es una operación descartada, no una oportunidad de operar en contra. Un largo limpio en 1
hora dentro de una tendencia bajista diaria es la operación que este paso rechaza.

## El setup: la estructura se encuentra con la confluencia

Acércate al retroceso, todavía en la temporalidad superior. El precio cae hacia 60.000, y allí
coinciden tres cosas independientes. Es el máximo previo que se rompió al subir (la vieja resistencia
pasa a soporte), es el retroceso 0,618 del último tramo, y la EMA de 50 al alza trepa hacia la misma
zona. Eso es confluencia: tres razones sin relación apuntando a un precio. Ninguna *crea* el nivel;
juntas hacen de 60.000 el lugar donde es más probable que la tendencia se reanude.

**Por qué confluencia y no una sola línea:** cualquier nivel aislado falla a menudo. Que fallen tres
a la vez es mucho menos probable, así que las probabilidades de que 60.000 aguante son mejores que
las que daría una sola herramienta.

## El trigger: la reacción en el nivel

Un nivel es un *lugar que vigilar*, nunca una razón para comprar por sí solo. Que el precio llegue a
60.000 no es la señal; la señal es cómo reacciona el precio ahí. Esperamos la reacción en la
temporalidad inferior (véase m08-l2). El precio se hunde hasta 59.700, se forma una mecha inferior
larga y la vela de 1 hora cierra de vuelta en 60.300: una vela de rechazo. Los vendedores empujaron
por debajo del nivel y fueron absorbidos. *Eso* es el trigger. Entramos en el cierre: 60.300.

**Por qué esperar el trigger:** comprar el nivel a ciegas da por hecho que aguantará; esperar la
reacción obliga al mercado a demostrar que los compradores aparecieron antes de comprometerte. Cuesta
un poco de precio (compras a 60.300, no a 60.000) a cambio de pruebas: una operación que puedes
rechazar si la reacción nunca llega.

## El stop: dónde la idea está equivocada

Antes de dimensionar, decide dónde la idea está muerta. Toda la tesis es «los compradores defienden
60.000». Si el precio cierra bien por debajo de la mecha de rechazo —digamos por debajo de 59.300—
esa tesis es falsa: el nivel no aguantó. Así que el stop va en 59.300, un poco por debajo del mínimo
de la mecha.

**Por qué ahí y en ningún otro sitio:** el stop pertenece al precio que *invalida el setup*, no a la
cantidad de dinero que te apetece perder. Colocado en la estructura, que te salte significa algo
real: te equivocaste con el nivel. No es una distancia aleatoria que el mercado atraviesa con una
mecha por ruido. Entrada 60.300, stop 59.300, así que el riesgo por unidad es de 1.000 en precio.
Llama a esa distancia 1R.

## El tamaño: desde el stop, no desde la tripa

Ahora —y solo ahora— el tamaño. El presupuesto es 100 USDT; la pérdida por unidad en el stop es 1.000.
Entonces:

`tamaño = presupuesto de riesgo ÷ distancia del stop = 100 ÷ 1.000 = 0,1 unidades` (0,1 BTC).

Es la fórmula de m22 aplicada: mantén 0,1 BTC y que te salten en 59.300 pierde `0,1 × 1.000 = 100
USDT`, exactamente el 1%, por muy seguro que te sientas. El objetivo es la siguiente oferta obvia, el
máximo previo de 64.000: a 3.700 de distancia, unos 3,7R. Arriesgar 1R para ganar ~3,7R es
el tipo de apuesta desequilibrada sobre la que se construye la esperanza matemática (m25).

Esos cuatro precios —el nivel, la entrada, el stop y el objetivo— son la operación entera, y son lo
que un trader dibuja en el gráfico. La figura los dibuja sobre un setup generado con la misma
anatomía: lee la forma, no los números, que se quedan en el texto de arriba.

::figure{id=fig-m27-trade-anatomy}

**Por qué el tamaño al final:** el stop sale del gráfico, el tamaño sale del stop. Hazlo en ese
orden y el riesgo es constante en cada operación sin importar el precio ni el apalancamiento.
Invíertelo —elige un tamaño y luego busca un stop que «encaje»— y vuelves a apostar.

## Gestionar la posición viva

La posición está abierta. La habilidad más difícil ahora es no hacer casi nada. El plan ya está
hecho; la gestión en vivo es una lista corta de acciones legítimas y una lista larga de tentaciones.

- **Mover el stop a break-even: con un test, no con una sensación.** «¿Legítimo o miedo?» no es una
  pregunta para resolver por estado de ánimo con dinero en juego, así que hazla comprobable. El stop
  se mueve a break-even solo cuando la operación ha producido una confirmación nueva a su favor en
  la temporalidad de ejecución. Esa confirmación es una ruptura de estructura en la dirección de la
  operación, en el gráfico de 1 hora del que salió la entrada. En este largo significa un nuevo
  máximo más alto y después el mínimo más alto que le sigue, ambos por encima de la entrada. Aquí el
  precio empuja a 62.300 y retrocede a un mínimo más alto en 61.200: test superado, así que el stop
  va a 60.300 y estás siguiendo al gráfico. Estar en verde *no* es el test. El verde es ruido: una
  sola vela hasta 60.600 es un número que el mercado marca y borra todo el día. La estructura, en
  cambio, es algo que el precio ha tenido que *construir*. Así que hazte la pregunta en voz alta:
  ¿qué ha hecho esta operación a mi favor que no hubiera hecho antes? Si la única respuesta es «está
  en verde», el stop se queda donde lo puso el plan.
- **Tomas de beneficio parciales: una elección de estilo, con su precio honesto.** El patrón
  habitual es cerrar un 30–50% en el primer nivel contrario y dejar correr el resto de la posición
  con el stop en break-even. En esta operación el primer nivel contrario es el máximo menor en
  62.300, exactamente +2R. Vendes ahí el 40%, mueves el stop a 60.300 y dejas el 60% apuntando a
  64.000. Es una forma legítima de asegurar avance y quitarle carga emocional al resto. Pero la
  frase que lo vende, un «runner sin riesgo», es engañosa: ese runner no es gratis y puedes ponerle
  precio exacto. Esta ganadora devuelve `0,4 × 2R + 0,6 × 3,7R = 3,0R` en vez de 3,7R: el runner
  gratis costó 0,7R del payoff de esta operación. Recortar las ganadoras de forma sistemática baja
  tu payoff medio, y el payoff es la mitad de la esperanza matemática (m25). Lo que compras a cambio
  es una proporción mayor de ganancias pequeñas. La operación que se atasca en 62.300 y se da la
  vuelta ahora sale en +0,8R en vez de 0. Si esa operación merece la pena no te lo puede decir nadie
  en abstracto. Son dos versiones de *tu* sistema, y el diario (m27-l2) es el único instrumento que
  puede compararlas. Decídelo en el plan, ejecútalo igual siempre y deja que el registro diga qué
  versión gana.
- **No hacer nada, la mayor parte del tiempo.** Si el precio deambula entre entrada y objetivo y nada
  de la estructura ha cambiado, la acción correcta es ninguna. La operación necesita espacio y tiempo
  para funcionar.
- **La única regla inviolable: el stop solo se mueve a favor de la operación.** Arriba en un largo,
  abajo en un corto; nunca en contra. En el momento en que ensanchas un stop para darle «más
  espacio» a una operación perdedora, has abandonado el plan y has quitado el tope a tu riesgo.

Nos toca el buen caso: el precio sube poco a poco, imprime un mínimo más alto en 61.200 (stop a
break-even) y toca 64.000. Salimos. Resultado: +3,7R ≈ +370 USDT, o +3,0R ≈ +300 USDT si
ejecutamos la versión con parciales de arriba.

## El límite de pérdida diaria: la regla que cierra el día

Todo lo anterior limita la pérdida de *una* operación a 100 USDT. Nada limita todavía la pérdida de
un día, y un mal día casi nunca es una sola operación. Así que el plan lleva un segundo límite,
separado: un límite de pérdida diaria. Es la regla de m26, convertida en un número. Escríbelo en una
frase: *si el PnL realizado del día llega a −X% de la cuenta, dejo de operar manualmente hasta
mañana*. Sin excepciones, sin «un setup más».

**En la práctica.** Pon X = 2% en esta cuenta de 10.000 USDT y el presupuesto del día son 200 USDT:
exactamente dos pérdidas completas de −1R. Encaja dos stops y la sesión se acabó: gráficos cerrados,
sin tercera idea, por buena que parezca la tercera idea. La X la eliges tú, normalmente entre el 1 y
el 3%. Los estilos rápidos que hacen más operaciones al día van en la parte baja. Se fija en el
plan, antes del día malo, nunca durante él.

**Por qué una regla mecánica y no criterio:** por *quién* tendría que ejercer ese criterio. La
persona que decide si sigue operando tras un −3% es la versión de ti de la que habla todo m26. Está
anclada en volver a estar en cero, con sensación de urgencia. Es la persona menos cualificada del
mundo para juzgar su propio estado. La respuesta de m26 era el compromiso previo: decidirlo cuando
no hay nada en juego. El límite de pérdida diaria es esa doctrina convertida en un número y un corte
duro. Funciona porque no te consulta en el momento en que menos capaz eres de responder.

:::note{type=warning}
El límite de pérdida diaria es la regla anti-venganza, así que la presión para romperlo llega exactamente cuando
está haciendo su trabajo. «Solo esta vez, el setup es demasiado bueno» es como un día de −2% se convierte
en una semana de −10%: reentras en tilt, subes el tamaño para recuperar, y la pérdida que te negaste a
aceptar en 200 USDT se acepta más tarde a varias veces ese precio. Un límite de pérdida diaria que te saltas no es una
regla, es una preferencia.
:::

## El registro

La operación no termina hasta que está escrita: el setup, el plan (entrada, stop, objetivo, tamaño), lo
que hiciste de verdad y el resultado en R. Ese registro es la materia prima de todo lo de
m27-l2: sin él no puedes distinguir una operación perdedora de un sistema roto.

## Dónde se rompe el plan en tiempo real

:::note{type=warning}
Casi ninguna cuenta muere por malos setups, sino por improvisar a mitad de operación: convertir una
operación planificada en una inventada después de estar en vivo.

**Ensanchar el stop.** El precio se acerca a 59.300 y, en vez de aceptar la pérdida planificada de 100
USDT, deslizas el stop a 58.000 «solo para darle espacio». Has convertido una pérdida conocida y
presupuestada en una abierta. Este único movimiento —mover el stop *en contra*— es el pecado capital, y
con apalancamiento es como un riesgo del 1% se convierte en una liquidación.

**Asfixiar la operación ganadora.** El miedo opuesto: pegas el stop a break-even en la primera vela verde, antes de
cualquier estructura nueva, y te sacan por ruido normal a cambio de nada; luego ves la operación correr
al objetivo sin ti.

**Improvisar una salida.** Cerrar en un precio cualquiera porque «da miedo», o aguantar más allá del
objetivo porque «podría seguir», sustituye tu objetivo planificado por una sensación. El plan nombró la
salida por una razón; tu versión en vivo y emocional no puede renegociarla.
:::

## La operación que dejas abierta el viernes

El mercado está abierto 24/7, así que una operación que colocas el viernes está viva y sin
vigilancia todo el fin de semana. Ese fin de semana transcurre en libros poco profundos, donde
60.000 puede recibir una mecha violenta con poco volumen. Es una razón más para que protejan el stop
y el tamaño, no tu atención. El apalancamiento está a un clic. Por eso la disciplina de *dimensionar
desde el stop* es lo que evita que «0,1 BTC» se convierta en silencio en una posición cuyo stop es
una liquidación.

El 24/7 también significa que no hay campana de cierre que te dé por terminado un mal día. Así que el
«día» del *límite de pérdida diaria* tienes que definirlo tú: elige una hora de reinicio, escríbela
(00:00 UTC, por ejemplo) y que esa sea la campana. Sin ella, una tarde de −2% se prolonga en la misma
sesión a las 3 de la madrugada, que es la hora en la que el tilt está menos vigilado.
````
