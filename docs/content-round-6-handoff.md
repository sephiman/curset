<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# Content round 6 — glossary additions, handoff

Glossary additions from `docs/glossary-decisions.md`, then one bundle regeneration. **Nothing is
committed. No lesson prose, `course.yaml` or exercise YAML was touched.** The only content files that
changed are `content/glossary.yaml` and the two generated `content/glossary-links.{es,en}.txt`.

| | ES | EN |
| --- | ---: | ---: |
| entries before | 178 | 178 |
| new entries added | **77** | **77** |
| entries after | 255 | 255 |
| web marks (glossary-links) | 580 → 1051 | 662 → 1114 |
| PDF links | 57 → 59 | 67 → 78 |

The decisions table has **80** rows marked "entra". Its totals line says 83, but only 80 rows carry
that mark. 77 were added, the three below were not, and one more term (`pérdida acotada`, a
"comprobar" row) was added by the check rule. 80 − 4 + 1 = 77.

## "entra" rows not added, and why

| Row | Why not |
| --- | --- |
| **volumen / volume** | It **already exists** as `g-volume` (origin m03-l1). My round-5 candidates table should not have listed it; that was a curation error in round 5, not a decision to make now. Nothing changed on `g-volume`. |
| **cotización / quote** | Below threshold in ES. In the quote sense it appears in one ES lesson ("retirar sus cotizaciones", m31-l1). m08-l1 and m08-l2 say "no una cotización que buscar", where it means a figure to look up, and m09-l1's "secuencia de cotizaciones" is a sequence of prices. EN has 2 lessons (m17-l1, m31-l1), but ES uses the verb "cotizan" in m17-l1, not the noun. |
| **sentimiento / sentiment** | Blocked by the **summary never-coins guard**, not by the lesson count (3 ES / 4 EN). The **m26-l1 ES summary** in `course.yaml` says "El propio sentimiento es la alarma", meaning "feeling", and m26-l1's prose never uses the word. The loader refuses a glossary term that a summary uses and its own lesson does not. Fixing it means changing that one word in `course.yaml` (for example "La propia sensación es la alarma"), which this round forbids. It can go in next round once the summary is changed. |
| **asimetría / asymmetry** | 0 lessons in the glossary's sense. Drawdown asymmetry is named only in m22-l1's **heading** ("…la asimetría del drawdown"), and the annotator and the course's own counts skip headings. The other two uses are other asymmetries: m07-l1 (unrealized PnL) and m29-l1 (buyer and seller both in every trade). A raw count said 2/2, and reading them showed otherwise. |

The rows marked "fuera" and "prosa-1.2" were not touched.

## The three checks ("Tareas del agente")

**cierre forzoso → yes, a form of liquidation.** ES uses it for the exchange's forced close in 11
lessons, and EN writes "forced close(s)" in the same places. Added to `g-liquidation` as match forms
in both locales: ES `cierre forzoso, cierres forzosos`, EN `forced close, forced closes`. The
existing ES `link_except: [m03-l1]` stays as it was.

**medias móviles → yes, a plural that was not captured.** The derived plural of "media móvil" is
"media móviles" (the naive rule pluralises the last word only), so "medias móviles" never matched in
four lessons. Added as an ES match form of `g-moving-average`. EN's derived "moving averages" was
already right, so EN is unchanged.

**pérdida acotada → added, as "bounded loss".** EN expresses it as "bounded loss" (m02-l1) and
"bounded, known loss" (m05-l1, m06-l1). Those are the same three lessons where ES says "pérdida
acotada", so EN already uses an equivalent term in 2+ lessons. Added as `g-bounded-loss`: ES
`pérdida acotada`, EN `bounded loss`, with EN match `bounded loss, bounded losses, bounded, known loss`.

**Glossary of the app vs glossary of the trade:** `instancia generada` is in, and its definition says
in both locales that it is app vocabulary, not trading vocabulary.

## Match forms added to existing entries (the "alias" rows, plus the checks)

A `match` list replaces the derived term-plus-plural entirely, so each list repeats the term itself.

| Entry | ES forms added | EN forms added |
| --- | --- | --- |
| `g-support` | suelo, suelos | floor, floors |
| `g-resistance` | techo, techos | ceiling, ceilings |
| `g-candle` | barra, barras | bar, bars |
| `g-aggressor` | compra(s) agresiva(s), venta(s) agresiva(s) | aggressive buy(s/ing), aggressive sell(s/ing) |
| `g-slippage` | deslizamiento, deslizamientos | — (EN is "slippage" already) |
| `g-perpetual-future` | perpetuo, perpetuos, and the correct plural **futuros perpetuos** | perpetual(s), perp(s) |
| `g-stop-loss` | stop, stops | the stop, a stop, your stop, the stops, your stops |
| `g-take-profit` | objetivo, objetivos | target, targets |
| `g-altcoin` | alt, alts | alt, alts |
| `g-liquidation` | cierre forzoso, cierres forzosos | forced close, forced closes |
| `g-moving-average` | medias móviles | — |
| `g-wedge` | cuña(s) ascendente(s), cuña(s) descendente(s) | rising wedge(s), falling wedge(s) |
| `g-triangle` | triángulo(s) ascendente(s) / descendente(s) / simétrico(s) | ascending / descending / symmetric(al) triangle(s) |

Two notes:

* **EN `stop` is narrowed to noun phrases.** Bare EN "stop" / "stops" is mostly a verb in this prose
  ("stop chasing", "stops being academic", "the app stops responding"). ES "stop" is always the noun,
  so ES takes the bare form.
* **`g-perpetual-future`'s derived ES plural was wrong** ("futuro perpetuos"). The new list writes
  "futuros perpetuos", so that plural links for the first time.

## Senses added (the "acepción" rows)

* **`g-wedge`**: two senses, rising and falling wedge, origin `m31-l2` (display m15-l2, the lesson
  that names them). The existing definition stays as the lead, so the entry is now the "lead
  definition + senses" shape.
* **`g-triangle`**: three senses, symmetric, ascending and descending, same origin, same shape.
* **`g-squeeze` / squeeze de volatilidad: nothing added.** The sense already exists: `g-squeeze`'s
  second sense (origin `m32-l1`) is the Bollinger-inside-Keltner volatility squeeze. Adding it again
  would duplicate it.

The variants all appear only in m15-l2, which is the entries' origin lesson, so they add no web marks.
They exist for the definition card.

## Origins

Each new entry's origin is its first lesson in **ES** reading order (the format holds one origin per
entry), stored as a lesson **key**. Four first ES hits were the wrong sense, and their origin is the
first lesson with the right one:

| Entry | First raw hit | Origin used (display) |
| --- | --- | --- |
| `g-close` | m02-l1, inside "campana de cierre" | m03-l1 |
| `g-confirmation` | m02-l1, "confirmación on-chain" | m09-l1 |
| `g-entry` | m01-l1, a ledger entry | m03-l2 |
| `g-hedge` | m19-l1, "cobertura de cortos" (short covering) | m21-l1 |

## False friends: `link_except`, per locale

Every new or changed web mark was read, in both locales. Where a lesson's first occurrence of the word
is another sense, that lesson is in the entry's `link_except` for that locale, so the next real
occurrence in a later lesson is still linked. Lesson **keys**:

| Entry | ES | EN |
| --- | --- | --- |
| `g-exchange` | — | m08-l1, m08-l2, m20-l2, m24-l1 |
| `g-indicator` | m15-l1 | — |
| `g-fill` | — | m16-l1 |
| `g-close` | m05-l1, m07-l1, m34-l2, m19-l2 | m23-l1 |
| `g-open` | m07-l1 | m07-l1 |
| `g-session` | m23-l1, m24-l1 | m22-l1, m23-l1, m24-l1 |
| `g-support` | m01-l1, m02-l1, m05-l1, m06-l1, m19-l1, m21-l1, m22-l1, m28-l1, m16-l1 | m01-l1, m02-l1, m05-l1, m06-l1, m19-l1, m21-l1, m22-l1, m28-l1, epilogue-l1 |
| `g-resistance` | m15-l1, m16-l1, m18-l1, m34-l1, m19-l1, m19-l2, m23-l1, m24-l2, m26-l1, m30-l1 | m18-l1, m19-l1, m19-l2, m24-l2 |
| `g-entry` | m01-l1, m15-l1, m18-l1 | m01-l1 |
| `g-edge` | m30-l1 | m03-l2, m04-l1, m31-l1, m21-l1, m29-l1, m30-l1 |
| `g-exit` | m09-l2, m10-l1, m32-l1, m18-l1, m20-l2 | m09-l2, m32-l1, m20-l2 |
| `g-compression` | m20-l2, m25-l1 | m20-l2, m25-l1 |
| `g-impulse` | m23-l1 | — |
| `g-confirmation` | m02-l1 | m28-l1 |
| `g-hedge` | m17-l1 | — |
| `g-slippage` | m03-l1 | — |
| `g-take-profit` | m01-l1, m09-l1, m09-l2, m22-l1 | m22-l1 |

What each exclusion is avoiding:

* `techo` / `ceiling` and `suelo` / `floor`: usually a cap or a margin floor ("la oferta máxima es el
  techo", "ese suelo son apenas 100 USDT"), a market top or bottom, or "ground floor". `g-support`'s
  two existing exceptions (m01-l1, m02-l1, "support desk") carry over unchanged into the per-locale
  form.
* `objetivo` / `target`: "el objetivo de esta lección" (the goal), and "the break-even is the floor,
  not the target".
* `cierre` / `close`: closing a position, the verb, "a close cousin". EN takes noun phrases only
  ("the close", "a close", "daily close", "closing price"). Bare "close" / "closes" is a verb or
  "near" in most of the EN prose.
* `salida` / `exit`: "salida a bolsa" (an IPO), "la salida al alza" (a breakout), "una salida
  concurrida" (a crowded doorway).
* `entrada` / `entry`: a ledger entry, "entrada de dinero" (an inflow).
* `ventaja` / `edge`: "desventaja sin ninguna ventaja" (advantage); EN "the edge of the range",
  "right edge", "edge case".
* `exchange` (EN): "in exchange for", "exchange rate", "won that exchange".
* `sesión` / `session`: your own trading session, not a market session.
* `compresión` / `compression`: data compression ("lossy compression", the candle as a compression
  of trades).
* One-offs: `apertura` / `open` "orden de apertura" / "the open leg" (a position's opening order);
  `confirmación` on-chain / blockchain confirmations; `cobertura de cortos` (short covering);
  `impulso de hacerlo` (an urge); `indicador en vivo del apetito` (a gauge, not a technical
  indicator); `fill` "timelines fill with"; `deslizamiento hacia el cierre` (a drift).

One more fix of the same kind: EN "a stop hunt" was being claimed by `g-stop-loss`'s "a stop", because
the earlier match starts first. `g-stop-hunt` now lists "a stop hunt" / "a stop-hunt", so the longer
term wins at that position.

### What moved among the marks that already existed

* **EN `g-maker` lost 5 marks**: keys m06-l1, m15-l1, m17-l1, m34-l2, m20-l1. In each one, "maker"
  appeared only inside "market maker(s)", which the new `g-market-maker` now claims as the longer term.
  Those five were wrong links: a market maker is not a maker order.
* **Three marks changed policy (W ↔ WP)**: ES `g-liquidation` in key m04-l1, ES `g-stop-loss` in key
  m17-l2, EN `g-stop-loss` in key m08-l1. A new match form ("cierre forzoso", "stop") puts the term's
  first occurrence earlier in the course, and the first occurrence is what takes the term's one PDF
  link.
* No other existing mark was lost or changed policy, in either locale.

## Lesson count per new term

Counted on the current lesson text, after round 5, **from what the annotator actually marks**: the
lessons with a web mark, plus the origin lesson (never marked, by rule). False friends are already
out. Threshold 2 in each locale, 1 for the seven exceptions (doji, martillo, estrella fugaz, harami,
sesgo de retrospectiva, look-ahead, walk-forward). All 77 pass. Origin is the display id.

| Entry | ES | EN | Origin | ES lessons | EN lessons |
| --- | --- | --- | --- | ---: | ---: |
| `g-uptrend` | tendencia alcista | uptrend | m03-l1 | 12 | 12 |
| `g-downtrend` | tendencia bajista | downtrend | m03-l1 | 11 | 11 |
| `g-sideways-market` | mercado lateral | sideways market | m10-l1 | 3 | 3 |
| `g-impulse` | impulso | impulse | m08-l2 | 3 | 3 |
| `g-close` | cierre | close | m03-l1 | 17 | 13 |
| `g-open` | apertura | open | m03-l1 | 7 | 4 |
| `g-gap` | hueco | gap | m03-l1 | 10 | 9 |
| `g-round-number` | número redondo | round number | m03-l2 | 3 | 3 |
| `g-compression` | compresión | compression | m08-l2 | 4 | 4 |
| `g-expansion` | expansión | expansion | m15-l2 | 3 | 3 |
| `g-volatility` | volatilidad | volatility | m06-l1 | 10 | 10 |
| `g-regime` | régimen | regime | m03-l2 | 7 | 7 |
| `g-momentum` | momentum | momentum | m11-l1 | 7 | 8 |
| `g-bias` | sesgo | bias | m03-l2 | 8 | 7 |
| `g-higher-timeframe` | temporalidad superior | higher timeframe | m03-l2 | 4 | 5 |
| `g-top-down` | de arriba abajo | top-down | m03-l2 | 3 | 3 |
| `g-intraday` | intradía | intraday | m08-l1 | 4 | 4 |
| `g-holding-period` | periodo de tenencia | holding period | m10-l1 | 2 | 2 |
| `g-session` | sesión | session | m03-l1 | 17 | 17 |
| `g-closing-bell` | campana de cierre | closing bell | m02-l1 | 15 | 15 |
| `g-doji` | doji | doji | m08-l2 | 1 | 1 |
| `g-hammer` | martillo | hammer | m08-l2 | 1 | 1 |
| `g-shooting-star` | estrella fugaz | shooting star | m08-l2 | 1 | 1 |
| `g-harami` | harami | harami | m08-l2 | 1 | 1 |
| `g-green-candle` | vela verde | green candle | m03-l1 | 5 | 5 |
| `g-stop-order` | orden stop | stop order | m07-l1 | 2 | 3 |
| `g-bracket` | bracket | bracket | m23-l1 | 2 | 2 |
| `g-fill` | ejecución | fill | m02-l1 | 8 | 13 |
| `g-market-maker` | creador de mercado | market maker | m06-l1 | 6 | 6 |
| `g-arbitrage` | arbitraje | arbitrage | m04-l1 | 5 | 5 |
| `g-iceberg` | iceberg | iceberg | m14-l1 | 2 | 2 |
| `g-wash-trading` | wash trading | wash trading | m14-l1 | 2 | 2 |
| `g-tick` | tick | tick | m04-l1 | 9 | 9 |
| `g-liquidity` | liquidez | liquidity | m01-l1 | 26 | 24 |
| `g-thin-book` | libro fino | thin book | m01-l1 | 24 | 17 |
| `g-participation` | participación | participation | m03-l1 | 8 | 8 |
| `g-confirmation` | confirmación | confirmation | m09-l1 | 11 | 11 |
| `g-stop-hunt` | caza de stops | stop hunt | m03-l2 | 5 | 7 |
| `g-collateral` | colateral | collateral | m01-l1 | 8 | 8 |
| `g-exposure` | exposición | exposure | m01-l1 | 5 | 5 |
| `g-hedge` | cobertura | hedge | m21-l1 | 4 | 6 |
| `g-counterparty` | contraparte | counterparty | m09-l1 | 3 | 3 |
| `g-overleveraged` | sobreapalancado | over-leveraged | m08-l1 | 4 | 4 |
| `g-positioning` | posicionamiento | positioning | m03-l2 | 4 | 4 |
| `g-one-sided` | unilateral | one-sided | m11-l1 | 5 | 7 |
| `g-dated-future` | futuros trimestrales | quarterly futures | m21-l2 | 2 | 2 |
| `g-derivatives` | derivados | derivatives | m19-l1 | 3 | 3 |
| `g-entry` | entrada | entry | m03-l2 | 22 | 22 |
| `g-exit` | salida | exit | m07-l1 | 9 | 12 |
| `g-edge` | ventaja | edge | m05-l1 | 8 | 10 |
| `g-losing-streak` | racha perdedora | losing streak | m22-l1 | 4 | 4 |
| `g-sample` | muestra | sample | m25-l1 | 4 | 4 |
| `g-bounded-loss` | pérdida acotada | bounded loss | m02-l1 | 3 | 3 |
| `g-average-win` | ganancia media | average win | m11-l1 | 3 | 3 |
| `g-break-even` | break-even | break-even | m08-l1 | 3 | 4 |
| `g-system` | sistema | system | m22-l1 | 7 | 7 |
| `g-trading-plan` | plan de trading | trading plan | m03-l2 | 5 | 4 |
| `g-precommitment` | precompromiso | pre-commitment | m26-l1 | 2 | 2 |
| `g-hindsight-bias` | sesgo de retrospectiva | hindsight bias | m09-l2 | 1 | 1 |
| `g-look-ahead` | look-ahead | look-ahead | m28-l1 | 1 | 1 |
| `g-walk-forward` | walk-forward | walk-forward | m35-l1 | 1 | 1 |
| `g-overtrading` | sobreoperar | overtrading | m23-l1 | 2 | 2 |
| `g-exchange` | exchange | exchange | m01-l1 | 28 | 25 |
| `g-token` | token | token | m01-l1 | 4 | 6 |
| `g-small-cap` | baja capitalización | small cap | m03-l2 | 4 | 7 |
| `g-cpi` | IPC | CPI | m17-l1 | 2 | 2 |
| `g-vesting` | vesting | vesting | m20-l1 | 2 | 2 |
| `g-total-supply` | oferta total | total supply | m01-l1 | 2 | 2 |
| `g-self-custody` | autocustodia | self-custody | m01-l1 | 2 | 2 |
| `g-private-key` | clave privada | private key | m01-l1 | 2 | 2 |
| `g-not-your-keys` | not your keys | not your keys | m01-l1 | 4 | 4 |
| `g-listing` | listado | listing | m17-l1 | 3 | 4 |
| `g-crowd` | masa | crowd | m04-l1 | 13 | 14 |
| `g-indicator` | indicador | indicator | m01-l1 | 12 | 12 |
| `g-zero-line` | línea de cero | zero line | m11-l1 | 2 | 2 |
| `g-time-series` | serie temporal | time series | m29-l1 | 3 | 3 |
| `g-generated-instance` | instancia generada | generated instance | m08-l1 | 5 | 5 |

Term choices worth knowing about. Each follows from the decisions table (one row, one entry) or from
what the prose already says:

* **`g-fill`** is ES `ejecución`, EN `fill`. EN prose says "fill" far more than "execution".
* **`g-market-maker`** takes the singular "creador de mercado" / "market maker" as the term; the
  plural is a match form.
* **`g-green-candle`** ("vela verde") also matches "vela roja" / "red candle"; one row, one entry.
* **`g-thin-book`** ("libro fino") also matches "libro poco profundo" (the form ES prose uses most)
  and "libro profundo" / "deep book".
* **`g-average-win`** ("ganancia media") also matches "pérdida media" / "average loss".
* **`g-dated-future`** ("futuros trimestrales") also matches "futuro con vencimiento" / "dated
  future", which is what the prose actually writes in m23-l1.
* **`g-crowd`** is ES `masa` (with `multitud` as a match form), EN `crowd`.
* **`g-precommitment`**: the EN term is **"pre-commitment"**, hyphenated, because that is what the EN
  prose writes. "precommitment" failed the never-coins check.
* **`g-wash-trading`** EN also matches "wash-trading", and **`g-overtrading`** EN also matches
  "over-trade". Those forms take each of them to 2 EN lessons (m14-l1 + m29-l1; m23-l1 + m25-l1).

## Definitions

All 77 are written to the voice page (`docs/prose-voice.md`): short sentences, no filler, no closer,
Peninsular Spanish with "tú", EN mirroring ES. Most are the candidates file's proposal split into
shorter sentences. These were **rewritten substantially**; please review them:

| Entry | What changed against the proposal |
| --- | --- |
| `g-crowd` | "whose positioning the course reads as fuel" → what happens when the crowd sits on one side. "Fuel" is the course's own metaphor, not the trade's word. |
| `g-one-sided` | "the fuel for a squeeze" → "lo que alimenta un squeeze" / "what feeds a squeeze", for the same reason. |
| `g-positioning` | "who holds what, long or short, and how crowded each side is" (a triad) → "cuánto pesa el lado largo frente al corto". |
| `g-derivatives` | dropped "options" from the list (the course does not teach them; the decisions table keeps options out) and the triad with it. |
| `g-session` | "(Asia, London, New York)" → "como Londres o Nueva York", two examples and not three. |
| `g-gap` | added "En cripto no hay sesión que cierre, así que casi no los hay." |
| `g-arbitrage` | added "Es lo que cierra esas diferencias." |
| `g-compression` | "it tends to come before expansion" → "dice que la volatilidad cayó, no hacia dónde saldrá el precio", which is what m08-l2 teaches about it. |
| `g-green-candle` | written as one entry for both colours, plus "El color solo dice eso." |
| `g-thin-book` | written for thin and deep in one entry. |
| `g-average-win` | written for the average win, with the average loss named as the other half of the payoff. |
| `g-cpi` | "the main inflation release markets trade around" → "el dato de inflación que más mueve los mercados el día que se publica". |
| `g-vesting` | "to insiders" → "de fundadores e inversores". |
| `g-dated-future` | the contrast with perpetuals spelled out: "que no vencen". |
| `g-stop-hunt` | "the crowd's name for a sweep" → "el nombre popular de un barrido"; "cúmulo de stops" in place of the coined "bolsa de liquidez". |
| `g-market-maker` | no proposal existed for this exact row; written new. |
| `g-bounded-loss` | new (the check row). |

No definition uses lente, escalera, repisa, flujo forzado or bolsa de liquidez.

## Verification

All green. Nothing that is supposed to stay byte-identical moved.

| Check | Result |
| --- | --- |
| `export_bundle.py`, format **2**, to `dist/bundle/` | exit 0. Text diff 0 (prose and glossary multisets, every lesson block for block), block inventory OK (88 ASTs), exercise refs OK (242 marks). Fingerprint `8fa3834501ef93a0…` (round 5) → **`74d2afcaa702d766…`** |
| per-file diff against the round-5 bundle | **90 files moved, all expected:** `ast/{es,en}/*.json` for 43 lessons per locale (every lesson except m01-l1, which gains no mark because it is the origin of most of the terms it uses), `glossary/glossary.{es,en}.json`, the bundle README and `manifest.json` (term count 178 → 255; `files` hashes). **`reading-seconds.json` byte-identical.** No file added or removed |
| `export_generation_goldens.py` | `exercise-mode.tsv` (3915), `figures.tsv` (33), `formatter-cases.tsv`, `configs/` (107): **byte-identical** to round 5. Zero diff, no recapture |
| `verify_golden_stability.py` | exit 0, **90 committed fingerprints hold**. Generation digest `6999679392b682a2…`, unchanged |
| figure/prose coupling | `test_figure_prose_coupling.py` passes inside the backend suite (no prose changed) |
| `lesson-refs.{es,en}.txt` | byte-identical; the refs report test passes without regenerating |
| `glossary-links.{es,en}.txt` | regenerated and reviewed mark by mark, as described above |
| backend `pytest` (whole suite, incl. `test_glossary`, `test_content_manifest`, `test_export_bundle`) | **1300 passed, 20 skipped** |
| frontend `vitest` (whole suite, incl. both report tests) | **458 passed, 1 skipped** |

No guard, threshold, pin or golden was changed.

## Files

Modified: `content/glossary.yaml`, `content/glossary-links.es.txt`, `content/glossary-links.en.txt`.
New: `docs/content-round-6-handoff.md`. The bundle was re-exported to `dist/bundle/` (gitignored).
Not touched: lesson prose, `course.yaml`, exercise YAML, figure specs, `lesson-refs.*.txt`
(byte-identical, as no prose moved), the goldens.

## For next round

* `sentimiento` can be added once the m26-l1 ES summary stops using the word, which is a
  `course.yaml` change.
* `cotización` needs a second ES lesson that uses it in the quote sense, and that is a prose change
  (pass 1.2).
* The decisions file's totals line (83 "entra") does not match its table (80).

---

## 6b — `sentimiento` added

**The summary fix.** In `course.yaml`, the m26-l1 ES summary:

| before | after |
| --- | --- |
| El propio sentimiento es la alarma: es la señal para apoyarte en la regla, no para saltártela. | La propia sensación es la alarma: es la señal para apoyarte en la regla, no para saltártela. |

"Sensación" is the word m26-l1's own ES prose uses for the feeling (3 times), and it is not a
glossary term. The EN summary says "The feeling itself is the alarm". "Feeling" is not a glossary
term, so the EN side had no problem and is unchanged.

**The entry.** `g-sentiment`, ES `sentimiento`, EN `sentiment`, origin `m16-l1` (display m18-l1, the
sentiment lesson), placed after `g-listing` in origin order:

* ES: "El ánimo de la masa, leído en índices como el de miedo y codicia y en el funding."
* EN: "The mood of the crowd, read from indexes such as Fear & Greed and from funding."

**Lesson count:** ES **3** (m18-l1 origin, m20-l1, m32-l1), EN **4** (m18-l1 origin, m17-l1, m20-l1,
m32-l1). Every new mark was read, and all are market sentiment, so no `link_except` was needed. ES
m17-l1 phrases that sentence without the word.

| | ES | EN |
| --- | ---: | ---: |
| glossary entries | 255 → **256** | 255 → **256** |
| web marks | 1051 → 1053 | 1114 → 1117 |
| PDF links | 59 | 78 → 79 (EN m17-l1's mark is the term's first occurrence in the course) |

**Verification.** All green. Everything outside the expected set is byte-identical.

| Check | Result |
| --- | --- |
| bundle, format **2**, re-exported to `dist/bundle/` | text diff 0, block inventory OK, exercise refs OK. Fingerprint `74d2afcaa702d766…` → **`b752db33e7004dfa…`** |
| per-file diff against the round-6 bundle | moved: `ast/en/{m17-l1,m20-l1,m32-l1}.json`, `ast/es/{m20-l1,m32-l1}.json` (the lessons that gained the link), `ast/index.json`, `glossary/glossary.{es,en}.json`, `README.md` (term count) and `manifest.json` (the m26-l1 ES summary, the term count). `reading-seconds.json` and everything else byte-identical |
| generation goldens | `exercise-mode.tsv`, `figures.tsv`, `formatter-cases.tsv`, `configs/` byte-identical. Zero diff |
| `verify_golden_stability.py` | exit 0, 90 fingerprints hold, digest `6999679392b682a2…` unchanged |
| backend `pytest` | 1300 passed, 20 skipped (includes the summary never-coins guard and the figure/prose coupling test) |
| frontend `vitest` | 458 passed, 1 skipped |

Files changed in 6b: `content/course.yaml` (one word), `content/glossary.yaml`,
`content/glossary-links.{es,en}.txt`.
