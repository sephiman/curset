<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# Glossary candidates

A proposal, not a change. Content round 5 added nothing to `glossary.yaml` from this list; the only
glossary edit in that round is `g-narrative` becoming two senses. New entries go in a later round,
after review, and each one has to pass the never-coins rule in both locales first.

**How it was built** (from `content/{es,en}/lessons/*.md` as they stood before the round-5 bold
cleanup, so "bold" means bold at that point):

1. Every `**…**` span in both locales, with the lessons it appears in (appendix A).
2. Every ES word, and every ES two-word phrase with no stopword in it, that appears in 3 or more of
   the 44 lessons, minus the terms already in the glossary (their ES term and `match` forms, with a
   naive plural). That gives 1818 words and 160 phrases (appendices B and C).
3. A curated main table: the entries from 1 and 2 that are plausibly trading vocabulary, plus a few
   bold-only terms (candle names, ecosystem words) that fall under the 3-lesson threshold. Lesson
   counts are recomputed per term with its plural and variant forms, in each locale separately.

Columns: **ES / EN lessons** is how many lessons use the term in that locale. A 0 in either column
means the term would coin in that locale today and the prose has to use it first. **Bold** means the
term sat inside a `**` span somewhere before the cleanup. Rows marked *alias* or *sense* in the
definition belong to an existing entry rather than a new one.

## Curated candidates (125)

| ES term | EN term | ES lessons | EN lessons | Bold | Proposed definition |
| --- | --- | ---: | ---: | --- | --- |
| tendencia alcista | uptrend | 12 | 12 | yes | A sequence of higher highs and higher lows; it stands until a lower low breaks it. |
| tendencia bajista | downtrend | 11 | 11 | yes | Lower highs and lower lows; the mirror of an uptrend. |
| mercado lateral | sideways market | 3 | 7 | no | Price held between two bounds with no sequence of higher or lower swings; a range by another name. |
| suelo | floor | 18 | 16 | yes | Plain word for support: the area where buying has stopped falls before. |
| techo | ceiling | 18 | 12 | yes | Plain word for resistance: the area where selling has capped rises before. |
| escalera | staircase | 9 | 3 | yes | The run of higher highs and higher lows (or the reverse) that defines a trend. |
| repisa | shelf | 4 | 7 | no | A flat area where price paused before; resting orders make it a level. |
| impulso | impulse | 4 | 3 | yes | A fast, one-directional leg that a pullback or retracement is measured against. |
| rebote | bounce | 11 | 11 | yes | A move back up from a level; not a reversal until structure confirms it. |
| extremo | extreme | 21 | 16 | yes | The high or low tip of a move or a candle, as opposed to its close. |
| cierre (de vela) | close | 32 | 37 | yes | The last price of a candle; the course's rule is to judge a break by the close, not the wick. |
| apertura | open | 8 | 31 | yes | The first price of a candle or session. |
| barra | bar | 13 | 14 | yes | One period on a chart; the same thing as a candle, drawn or named differently. |
| hueco | gap | 21 | 26 | yes | A jump between one close and the next open with no trading in between. |
| número redondo | round number | 3 | 3 | yes | A price like 60,000 where many people place orders, which makes it a level by itself. |
| zona de interés | area of interest | 1 | 0 | yes | A price area marked in advance where you expect to watch for a reaction. |
| área de valor | value area | 1 | 1 | yes | In a volume profile, the price band where most of the volume traded. |
| valor justo | fair value | 1 | 2 | yes | The price a market treats as fair for now; in the SMC dialect, a gap it expects to refill. |
| cuña ascendente / descendente | rising / falling wedge | 1 | 1 | yes | A wedge whose two lines both slope up or both slope down; proposed as senses of g-wedge. |
| triángulo ascendente / descendente / simétrico | ascending / descending / symmetrical triangle | 1 | 1 | yes | Triangle variants by which line is flat; proposed as senses of the triangle entry. |
| diagonal | diagonal | 2 | 2 | yes | A sloping line drawn through swing points: a trendline or a channel edge. |
| compresión | compression | 6 | 6 | yes | A stretch where the range of each bar shrinks; it tends to come before expansion. |
| expansión | expansion | 3 | 3 | yes | A stretch where the range of each bar grows, usually after compression. |
| volatilidad | volatility | 10 | 10 | yes | How far price typically moves per bar; it sets stop distance and therefore size. |
| squeeze de volatilidad | volatility squeeze | 3 | 3 | yes | Bands pressed unusually tight; a sense distinct from a short squeeze, to add to g-squeeze. |
| régimen | regime | 7 | 7 | yes | The state a market is in (trending, ranging, quiet, wild), which decides which tools work. |
| momentum | momentum | 7 | 8 | yes | How fast price is moving in one direction; what oscillators measure. |
| sesgo | bias | 10 | 9 | yes | The direction you lean on before entering, taken from the higher timeframe. |
| temporalidad superior | higher timeframe | 4 | 5 | yes | The slower chart that sets the bias; the lower one times the entry. |
| de arriba abajo | top-down | 4 | 4 | no | Reading from the higher timeframe down to the entry timeframe, in that order. |
| intradía | intraday | 4 | 4 | yes | Within a single day; positions opened and closed before the day ends. |
| periodo de tenencia | holding period | 2 | 2 | yes | How long a style keeps a position open; it decides the timeframe you trade. |
| sesión | session | 21 | 21 | yes | The hours a region's traders are active (Asia, London, New York); depth changes with them. |
| campana de cierre | closing bell | 15 | 15 | yes | The daily close of traditional markets, which crypto does not have. |
| mercados tradicionales | traditional markets | 8 | 8 | no | Stocks, bonds and futures on venues that close; the contrast for crypto's 24/7 trading. |
| fin de semana (liquidez) | weekend | 27 | 27 | yes | Hours when professional flow steps back and books thin, so the same order moves price further. |
| doji | doji | 1 | 1 | yes | A candle whose open and close are almost equal: indecision, read only at a level. |
| martillo | hammer | 1 | 1 | yes | A small body with a long lower wick: buyers rejected lower prices during the candle. |
| estrella fugaz | shooting star | 1 | 1 | yes | A small body with a long upper wick: sellers rejected higher prices during the candle. |
| harami | harami | 1 | 1 | yes | A candle whose body sits inside the previous body; a pause, not a signal by itself. |
| vela verde / roja | green / red candle | 5 | 5 | yes | A candle that closed above / below its open. |
| agregado | aggregate | 6 | 6 | no | What a candle is: four prices summarising every trade in a period, hiding who traded. |
| orden stop | stop order | 3 | 4 | no | An order that waits until price touches a trigger and then becomes a market or limit order. |
| bracket | bracket | 2 | 2 | yes | An entry with its stop and target attached, so both exits exist from the first fill. |
| ejecución | fill / execution | 8 | 17 | yes | The price and size your order actually traded at, which can differ from the price you saw. |
| cotización | quote | 4 | 8 | yes | The bid and ask a market maker is offering at a given moment. |
| creadores de mercado | market makers | 6 | 6 | no | Firms that keep resting bids and asks and earn the spread; they pull quotes before big releases. |
| arbitraje | arbitrage | 5 | 5 | yes | Buying in one place and selling the same thing in another to capture a price difference. |
| arbitrajista | arbitrageur | 2 | 2 | no | Someone who closes price gaps between venues or between perpetual and spot for profit. |
| iceberg | iceberg | 2 | 2 | yes | A large order shown in small slices so the book never displays its true size. |
| spoofing | spoofing | 1 | 1 | yes | Placing large orders meant to be cancelled, to fake depth and move other traders. |
| wash trading | wash trading | 2 | 1 | yes | Trading with yourself to inflate volume; why reported volume on some venues is not real. |
| compra / venta agresiva | aggressive buy / sell | 3 | 3 | no | A market order that takes resting liquidity; proposed as an alias of g-aggressor. |
| tick | tick | 9 | 9 | no | The smallest price step a market allows; also one trade print. |
| deslizamiento | slippage (ES synonym) | 5 | 9 | yes | Spanish synonym the course uses for slippage; proposed as an ES match form of g-slippage. |
| liquidez | liquidity | 27 | 25 | yes | How much size can trade near the current price without moving it much. |
| libro fino / profundo | thin / deep book | 25 | 18 | yes | A book with little / a lot resting near price; how far one order moves price. |
| volumen | volume | 23 | 22 | yes | How much traded in a period; the participation behind a move. |
| participación | participation | 8 | 8 | yes | Real volume behind a move; a break without it is suspect. |
| confirmación | confirmation | 14 | 12 | yes | Evidence after the signal (a close, volume) that the read was right before you act on it. |
| bolsa de liquidez | liquidity pool | 3 | 1 | no | A cluster of stops and liquidation orders at a known price that a move can trigger. |
| caza de stops | stop hunt | 7 | 6 | yes | A move into a stop cluster that triggers it and reverses; the crowd's name for a sweep. |
| flujo forzado | forced flow | 14 | 13 | no | Orders nobody chose to send (liquidations, stop-outs) that hit the book regardless of price. |
| colateral | collateral | 8 | 8 | yes | What you post to back a leveraged position; its value can fall with the market. |
| exposición | exposure | 5 | 5 | yes | How much of your account moves with a given market, counting every correlated position. |
| cobertura | hedge | 5 | 6 | yes | A second position that offsets the risk of the first. |
| contraparte | counterparty | 3 | 3 | no | The other side of your trade, or the platform holding your funds and its failure risk. |
| sobreapalancado | over-leveraged | 4 | 4 | no | Using so much leverage that a normal move liquidates the position. |
| posicionamiento | positioning | 4 | 4 | yes | Who holds what, long or short, and how crowded each side is. |
| unilateral | one-sided | 5 | 7 | no | Positioning or funding stacked on one side, which is the fuel for a squeeze. |
| futuros trimestrales | quarterly / dated futures | 2 | 2 | yes | Futures that expire on a set date; the contrast to perpetuals. |
| opciones | options | 3 | 2 | yes | Contracts giving the right, not the obligation, to buy or sell at a price; a second course. |
| derivados | derivatives | 6 | 3 | no | Contracts whose value comes from another asset: futures, perpetuals, options. |
| perpetuo | perp / perpetual | 18 | 18 | yes | Short form for a perpetual future; proposed as a match form of g-perpetual. |
| stop | stop | 29 | 34 | yes | Short form for stop-loss; proposed as a match form of g-stop-loss. |
| objetivo | target | 13 | 10 | no | Where you plan to take profit; proposed as a match form of g-take-profit. |
| entrada | entry | 25 | 23 | yes | The price where a position opens, decided before the order is sent. |
| salida | exit | 14 | 15 | yes | The price or rule that closes a position, decided before entry. |
| ventaja | edge | 9 | 18 | no | A measured positive expectancy over enough trades; what a system has to prove it has. |
| racha perdedora | losing streak | 4 | 3 | yes | Several losses in a row; normal and predictable for any win rate below 100%. |
| muestra | sample | 22 | 4 | yes | The number of trades behind a statistic; too few and the number means nothing. |
| pérdida acotada | capped loss | 3 | 0 | yes | A loss with a known maximum, set by the stop and the size before entry. |
| asimetría | asymmetry | 3 | 3 | no | A 50% loss needs a 100% gain to recover; why drawdowns must stay small. |
| ganancia / pérdida media | average win / loss | 3 | 3 | yes | The two halves of payoff, measured over a sample. |
| break-even | break-even | 3 | 4 | yes | The point where a trade or system neither wins nor loses after costs. |
| sistema | system | 7 | 7 | yes | A written set of rules for entry, exit and size that can be tested. |
| plan de trading | trading plan | 5 | 4 | no | The written rules you follow before and during every trade. |
| revisión semanal | weekly review | 1 | 1 | yes | A fixed time to read the journal and separate system errors from execution errors. |
| precompromiso | precommitment | 2 | 2 | yes | Deciding the rule while calm, so the decision does not depend on how you feel later. |
| sesgo de retrospectiva | hindsight bias | 1 | 1 | yes | Seeing a pattern clearly only because you already know the outcome. |
| sesgo de supervivencia | survivorship bias | 1 | 0 | yes | Judging by the winners you can see while the losers dropped out of view. |
| look-ahead | look-ahead bias | 1 | 1 | yes | Using information in a backtest that was not available at the time of the trade. |
| walk-forward | walk-forward | 1 | 1 | yes | Fit on one window, test on the next, move forward and repeat. |
| dinero real | real money | 3 | 5 | yes | Trading with funds you can lose, which tests psychology as well as the system. |
| demo | demo | 2 | 2 | yes | Simulated trading with no money at risk; it tests the rules but not your nerve. |
| horas de pantalla | screen time | 1 | 1 | yes | Time spent watching live markets, which is how reads become recognisable. |
| criterio de abandono | abandonment criterion | 1 | 1 | no | A rule written in advance for when to stop trading a system. |
| sobreoperar | overtrading | 2 | 1 | no | Taking trades outside the plan, usually after losses or out of boredom. |
| exchange | exchange | 28 | 29 | yes | A platform where you trade; centralised (CEX) or decentralised (DEX). |
| token | token | 6 | 6 | yes | A crypto asset issued on a blockchain. |
| baja capitalización | small cap / low cap | 4 | 7 | yes | A token with a small market cap and usually a thin book. |
| alt | alt | 15 | 17 | yes | Short for altcoin; proposed as a match form of g-altcoin. |
| alt season | alt season | 1 | 1 | yes | A phase where capital rotates into altcoins and they outperform Bitcoin; never guaranteed. |
| ETH/BTC | ETH/BTC | 1 | 1 | yes | Ether priced in Bitcoin; a gauge of risk appetite moving down the curve. |
| refugio / oro digital | safe haven / digital gold | 1 | 1 | yes | The claim that Bitcoin rises when other markets fall; the course treats it as a narrative that often fails. |
| publicación macro | macro release | 1 | 1 | yes | A scheduled economic number (CPI, rates) that thins books before it and moves all markets after. |
| IPC | CPI | 2 | 2 | no | The consumer price index; the main inflation release markets trade around. |
| vesting | vesting | 2 | 2 | yes | The schedule that releases locked tokens to insiders over time. |
| oferta total | total supply | 2 | 2 | yes | All tokens that exist now, locked or not. |
| dilución | dilution | 1 | 1 | no | New supply reducing what each existing token represents. |
| autocustodia | self-custody | 2 | 2 | yes | Holding your own keys rather than leaving coins on an exchange. |
| clave privada | private key | 2 | 2 | yes | The secret that controls a wallet; whoever holds it owns the coins. |
| not your keys | not your keys | 4 | 4 | yes | Short for 'not your keys, not your coins': coins on an exchange are a claim on the exchange. |
| listado | listing | 3 | 3 | no | A token being added to an exchange, which often moves its price on the day. |
| sentimiento | sentiment | 3 | 4 | yes | The mood of the crowd, read from indexes, social data and funding. |
| pánico | panic | 7 | 4 | no | Selling driven by fear rather than plan; the opposite extreme of euphoria. |
| masa / multitud | crowd | 13 | 14 | yes | The majority of traders, whose positioning the course reads as fuel. |
| prima de Coinbase | Coinbase premium | 1 | 1 | yes | BTC priced higher on Coinbase than elsewhere; read as US demand. A case of the inter-venue premium. |
| indicador | indicator | 13 | 12 | no | A value computed from price or volume; it summarises the chart, it does not add information. |
| línea de cero | zero line | 2 | 2 | yes | The centre line of an oscillator such as MACD; crossing it means the averages swapped order. |
| serie temporal | time series | 3 | 3 | yes | Values in time order; every chart this course generates is one. |
| microestructura | microstructure | 1 | 1 | yes | How orders meet and fill: the book, the spread, the flow. |
| heatmap | heatmap | 1 | 2 | yes | A chart of resting book depth over time, coloured by size. |
| instancia generada | generated instance | 5 | 5 | yes | A specific chart or question produced by the course from a seed; the app's own vocabulary. |
| confluencia (lente) | lens | 6 | 6 | yes | An independent way of reading the chart; confluence is several lenses agreeing. |

## Appendix A — every bold span, with its lessons

Display ids. Spans are whitespace-normalised and otherwise verbatim, so case and punctuation variants
are separate rows.

### ES — 1735 spans, 1360 distinct

| Span | Lessons |
| --- | --- |
| Qué es. | m04-l1, m07-l1, m08-l2, m14-l1, m18-l1, m22-l1, m26-l1, m29-l1, m30-l1, m31-l1, m32-l1, m33-l1 |
| En la práctica. | m04-l1, m07-l1, m08-l2, m14-l1, m18-l1, m23-l1, m26-l1, m27-l1, m29-l1, m30-l1, m31-l1 |
| 24/7 | m03-l2, m04-l1, m08-l2, m09-l2, m12-l1, m25-l1 |
| liquidación | m04-l1, m19-l2, m22-l2, m24-l1, m26-l1, m27-l1 |
| base | m16-l1, m19-l1, m21-l1, m32-l1, m34-l1 |
| funding | m07-l1, m11-l1, m12-l1, m18-l1, m23-l1 |
| m08-l1 | m15-l1, m15-l2, m16-l1, m23-l2, m34-l1 |
| m26 | m16-l1, m23-l2, m28-l1, m34-l1, m35-l1 |
| soporte | m03-l2, m08-l1, m09-l1, m09-l2, m13-l1 |
| volumen | m03-l1, m03-l2, m14-l1, m23-l2, m30-l1 |
| 10.000 USDT | m22-l1, m22-l2, m23-l1, m27-l1 |
| 60.000 | m19-l1, m22-l1, m24-l1, m27-l1 |
| instancia generada | m08-l1, m08-l2, m09-l2, m24-l1 |
| m08-l2 | m15-l2, m16-l1, m27-l1, m34-l1 |
| m19-l2 | m15-l1, m16-l1, m21-l1, m34-l1 |
| m22 | m16-l1, m23-l2, m34-l1, m35-l1 |
| m23-l1 | m10-l1, m17-l1, m21-l1, m23-l2 |
| m27-l1 | m03-l2, m22-l1, m23-l1, m23-l2 |
| Por qué importa. | m04-l1, m08-l2, m22-l1, m29-l1 |
| rango | m03-l1, m03-l2, m09-l1, m10-l1 |
| resistencia | m03-l2, m08-l1, m09-l1, m09-l2 |
| spring | m09-l1, m09-l2, m29-l1, m30-l1 |
| +500 | m11-l1, m29-l1, m30-l1 |
| 0 | m11-l1, m22-l2, m30-l1 |
| 1% | m22-l1, m26-l1, m27-l1 |
| 100 | m03-l2, m11-l1, m28-l1 |
| cierre | m03-l1, m08-l1, m23-l2 |
| Ejemplo trabajado. | m29-l1, m31-l1, m32-l1 |
| estructura | m03-l2, m08-l1, m12-l1 |
| m10-l1 | m15-l2, m23-l1, m34-l1 |
| m14 | m15-l1, m15-l2, m16-l1 |
| m15-l1 | m08-l1, m15-l2, m28-l1 |
| m16-l1 | m08-l2, m19-l2, m22-l1 |
| m27-l2 | m27-l1, m28-l1, m35-l1 |
| maker | m07-l1, m24-l1, m29-l1 |
| máximo | m03-l1, m23-l2, m34-l1 |
| máximo más alto | m08-l1, m12-l1, m30-l1 |
| mínimo | m03-l1, m23-l2, m34-l1 |
| mínimo más bajo | m08-l1, m12-l1, m30-l1 |
| precio | m12-l1, m19-l1, m33-l1 |
| slippage | m02-l1, m24-l1, m31-l1 |
| spread | m02-l1, m23-l1, m31-l1 |
| taker | m07-l1, m24-l1, m29-l1 |
| 0 a 100 | m11-l1, m18-l1 |
| 0,5 | m13-l1, m25-l1 |
| 1.745 | m09-l1, m09-l2 |
| 1.800 | m09-l1, m09-l2 |
| 1.810 | m09-l2, m34-l1 |
| 100 USDT | m22-l1, m27-l1 |
| 15% | m19-l1, m19-l2 |
| 1R | m26-l1, m27-l1 |
| 2.000 | m19-l1, m22-l1 |
| 24/7, sin campana de cierre. | m19-l2, m20-l1 |
| 25.400 | m09-l2, m19-l2 |
| 50 | m11-l1, m28-l1 |
| 5× | m07-l1, m22-l1 |
| 60.300 | m19-l1, m27-l1 |
| alcista | m03-l1, m10-l1 |
| ATR | m16-l1, m22-l1 |
| bajista | m03-l1, m10-l1 |
| banda | m03-l2, m13-l1 |
| barrido | m19-l2, m34-l1 |
| Con números. | m19-l1, m21-l1 |
| conceptual | m31-l1, m33-l1 |
| confluencia | m14-l1, m27-l1 |
| contexto | m11-l1, m18-l1 |
| diario | m27-l1, m27-l2 |
| distribución | m09-l1, m09-l2 |
| divergencia | m12-l1, m29-l1 |
| día | m22-l1, m27-l1 |
| Dónde falla esto. | m12-l1, m18-l1 |
| freno diario | m22-l1, m27-l1 |
| libro de órdenes | m02-l1, m24-l1 |
| liquidaciones | m18-l1, m19-l2 |
| liquidez | m19-l2, m24-l1 |
| m03-l2 | m15-l1, m23-l2 |
| m04-l1 | m21-l1, m21-l2 |
| m06-l1 | m22-l1, m34-l1 |
| m13 | m15-l2, m34-l1 |
| m15-l2 | m08-l2, m16-l1 |
| m16 | m15-l2, m35-l1 |
| m19 | m16-l1, m34-l1 |
| m19-l1 | m21-l1, m21-l2 |
| m21-l1 | m19-l1, m21-l2 |
| m24 | m28-l1, m35-l1 |
| m29 | m23-l2, m34-l1 |
| m31 | m21-l2, m35-l1 |
| m32 | m34-l1, m35-l1 |
| margen | m05-l1, m06-l1 |
| margen de mantenimiento | m05-l1, m06-l1 |
| markdown | m09-l1, m09-l2 |
| markup | m09-l1, m09-l2 |
| más bajo | m03-l1, m30-l1 |
| máximo más bajo | m12-l1, m30-l1 |
| mínimo más alto | m12-l1, m30-l1 |
| nada | m08-l2, m18-l1 |
| no | m05-l1, m34-l1 |
| No | m18-l1, m20-l1 |
| nocional | m04-l1, m07-l1 |
| Por qué existe. | m04-l1, m07-l1 |
| Por qué ocurre. | m14-l1, m26-l1 |
| Por qué se agrupan: | m19-l2, m25-l1 |
| porqué | m03-l1, m03-l2 |
| prima entre exchanges | m32-l1, m34-l1 |
| profundidad | m02-l1, m31-l1 |
| Qué. | m06-l1, m20-l1 |
| spot | m02-l1, m23-l1 |
| stop | m22-l1, m24-l1 |
| stop-hunt | m08-l2, m09-l1 |
| temporalidad | m03-l1, m23-l1 |
| tendencia | m03-l1, m03-l2 |
| tendencia alcista | m03-l2, m08-l1 |
| tendencia bajista | m03-l2, m08-l1 |
| tiempo | m23-l2, m33-l1 |
| upthrust | m09-l1, m09-l2 |
| UTAD | m09-l1, m09-l2 |
| zona | m08-l1, m34-l1 |
| "ahora mismo lo estás leyendo perfecto". | m26-l1 |
| "El precio se movió +2 %, así que mi PnL es +2 %." | m07-l1 |
| "me lo estoy perdiendo, tengo que entrar". | m26-l1 |
| "Más operaciones significa más beneficio". | m23-l1 |
| "Si el mercado cayera un 10% ahora mismo, ¿cuánto perdería?" | m22-l2 |
| "Small cap = barato" y "precio bajo = barato". | m20-l1 |
| "solo necesito una buena operación para recuperar lo perdido". | m26-l1 |
| "toca un rebote" | m26-l1 |
| "una pérdida del 50% solo necesita una ganancia del 50%". | m22-l1 |
| "voy a darle margen, el nivel está básicamente bien, va a rebotar". | m26-l1 |
| "¿tendencia o rango, en mi temporalidad?" | m03-l2 |
| $0,001 | m20-l1 |
| $0,50 | m20-l1 |
| $0,77 | m20-l1 |
| $3,00 | m20-l1 |
| $50 | m20-l1 |
| (un tercio) → necesitas | m22-l1 |
| +0,01% | m04-l1 |
| +0,05R | m27-l2 |
| +0,1% | m04-l1 |
| +0,15 % | m07-l1 |
| +0,6R | m27-l2 |
| +0,8R | m27-l1 |
| +1 | m22-l2 |
| +1,80 % sobre el nocional | m07-l1 |
| +100% | m22-l1 |
| +150 | m11-l1 |
| +17 | m11-l1 |
| +2 % | m07-l1 |
| +20 | m11-l1 |
| +200 | m29-l1 |
| +2R | m22-l1 |
| +3,0R ≈ +300 USDT | m27-l1 |
| +3,7R ≈ +370 USDT | m27-l1 |
| +300 | m30-l1 |
| +360 | m11-l1 |
| +392 | m11-l1 |
| +393 | m11-l1 |
| +3R | m22-l1 |
| +400 USDT | m07-l1 |
| +410 | m11-l1 |
| +420 | m11-l1 |
| +50 | m11-l1 |
| +60 USDT por operación | m25-l1 |
| +650 | m29-l1 |
| +80 | m11-l1 |
| +800 | m30-l1 |
| +9,0 % | m07-l1 |
| , porque la ganancia de recuperación se calcula sobre la base más pequeña que dejó la pérdida: - Pierde un | m22-l1 |
| , y la cuenta es puramente mecánica: - la | m23-l2 |
| . | m22-l1 |
| . - Pierde un | m22-l1 |
| 0,01% cada 8h | m21-l1 |
| 0,03 % por intervalo | m23-l1 |
| 0,04 % por ejecución | m23-l1 |
| 0,1 BTC | m27-l1 |
| 0,11 % del nocional solo para cubrir costes | m07-l1 |
| 0,2 unidades | m22-l1 |
| 0,3 % | m11-l1 |
| 0,3% de tu nocional cada día | m04-l1 |
| 0,382 | m13-l1 |
| 0,4 unidades | m22-l1 |
| 0,5–1% | m27-l2 |
| 0,618 | m13-l1 |
| 0,8% | m08-l2 |
| 0,9 % | m11-l1 |
| 00:00 a 00:00 UTC | m03-l1 |
| 1 | m25-l1 |
| 1 de cada 13 | m25-l1 |
| 1 de cada 60 | m25-l1 |
| 1 hora | m27-l1 |
| 1 y el 3% | m27-l1 |
| 1% de riesgo, 100 USDT, cada una con su stop colocado un 10% por debajo de la entrada. | m22-l2 |
| 1,0 unidad | m22-l1 |
| 1,00 | m11-l1 |
| 1,20 | m11-l1 |
| 1,3% de slippage | m02-l1 |
| 1,35 | m11-l1 |
| 1,5% | m06-l1 |
| 1,50 | m11-l1 |
| 1,60 | m11-l1 |
| 1,9% | m08-l2 |
| 1. Demanda regional: la informativa. | m32-l1 |
| 1. Dos toques proponen, el tercero valida. | m15-l1 |
| 1. Las reglas se escriben ANTES de mirar. | m28-l1 |
| 1.000 | m27-l1 |
| 1.000 millones de dólares | m20-l1 |
| 1.589 | m16-l1 |
| 1.834 | m34-l1 |
| 1.855 | m34-l1 |
| 1.870 | m09-l2 |
| 1.902 | m16-l1 |
| 1.930 | m09-l2 |
| 1.960 | m34-l1 |
| 1.965 | m34-l1 |
| 10 | m20-l1 |
| 10 contratos | m24-l1 |
| 10% al mismo tiempo | m22-l2 |
| 10.000 | m19-l1 |
| 10.300 | m15-l1 |
| 10.361 | m16-l1 |
| 10.400 | m23-l2 |
| 10.551 | m16-l1 |
| 10.570 | m15-l1 |
| 10.575 | m15-l1 |
| 10.740 | m15-l1 |
| 100 millones de dólares | m20-l1 |
| 100 puntos | m22-l1 |
| 1000 | m28-l1 |
| 100× | m26-l1 |
| 100–200 cada vez | m09-l1 |
| 101,8 en la primera vela | m10-l1 |
| 106,3 en la quinta | m10-l1 |
| 108 | m03-l2 |
| 10× | m06-l1 |
| 11.270 | m15-l1 |
| 12.272 | m16-l1 |
| 120.000 USDT | m21-l1 |
| 13.000 | m19-l1 |
| 14 | m11-l1 |
| 150 | m09-l1 |
| 18 | m12-l1 |
| 180, 292 y 274 USDT | m23-l1 |
| 2 | m25-l1 |
| 2 a 100,0 | m24-l1 |
| 2% | m27-l2 |
| 2,026 | m02-l1 |
| 2. Declara tu anclaje y mantenlo. | m15-l1 |
| 2. Fricción de transferencia: la aburrida. | m32-l1 |
| 2. Vela a vela, sin volver hacia atrás. | m28-l1 |
| 2.000 millones | m20-l1 |
| 2.014 | m16-l1 |
| 2.017 a 2.499 | m13-l1 |
| 2.020 | m19-l1 |
| 2.035 | m08-l1 |
| 2.045 | m34-l1 |
| 2.050 a 1.800 | m09-l2 |
| 2.100 | m34-l1 |
| 2.125 | m14-l1 |
| 2.130 | m08-l1 |
| 2.166 | m08-l1 |
| 2.195 | m14-l1 |
| 2.201 | m13-l1 |
| 2.210 | m09-l2 |
| 2.225 | m08-l1 |
| 2.258 | m13-l1 |
| 2.258 a 2.201 | m13-l1 |
| 2.300 | m19-l1 |
| 2.315 | m13-l1 |
| 2.670 | m19-l1 |
| 2.760 millones de dólares | m20-l1 |
| 20 | m28-l1 |
| 20 y 50, para swing trading | m10-l1 |
| 20.400 | m07-l1 |
| 200 millones | m20-l1 |
| 200 USDT | m27-l1 |
| 2000 contratos | m09-l1 |
| 20× | m22-l1 |
| 23.500 | m30-l1 |
| 23.900 | m09-l2 |
| 24 horas al día, 7 días a la semana | m23-l1 |
| 24.400 | m30-l1 |
| 24/7 significa que no hay enfriamiento forzoso. | m26-l1 |
| 24/7, sin campana de cierre ni interruptores automáticos. | m06-l1 |
| 24/7, sin cierre. | m09-l1 |
| 240 millones de dólares | m20-l1 |
| 25% | m25-l1 |
| 25.350 | m19-l2 |
| 25.850 | m19-l2 |
| 25.900 | m19-l2 |
| 250 puntos | m22-l1 |
| 26.220 | m19-l2 |
| 26.780 | m34-l1 |
| 27.100 | m34-l1 |
| 27.320 | m34-l1 |
| 28 | m12-l1 |
| 28.000 | m34-l1 |
| 28.250 | m12-l1 |
| 28.320 | m34-l1 |
| 29.000 | m09-l2 |
| 2FA por SMS y el SIM-swap. | m02-l1 |
| 3 | m25-l1 |
| 3 a 100,5 | m24-l1 |
| 3 USDT/día | m04-l1 |
| 3,7R | m27-l1 |
| 3. Cada operación registrada con la disciplina de m27. | m28-l1 |
| 3. Una línea que redibujas cada semana nunca fue una línea. | m15-l1 |
| 3.000 | m19-l2 |
| 3.000 millones de dólares | m20-l1 |
| 3.000 USDT de exposición larga | m22-l2 |
| 3.450 | m19-l2 |
| 3.700 | m27-l1 |
| 30 USDT/día | m04-l1 |
| 30% de inflación | m20-l1 |
| 30.590 | m09-l2 |
| 300 | m28-l1 |
| 30× | m22-l1 |
| 30–50% | m27-l1 |
| 310 | m33-l1 |
| 32.600 | m12-l1 |
| 33,3% | m25-l1 |
| 38 | m12-l1 |
| 3R | m22-l1 |
| 5 a 101,0 | m24-l1 |
| 50 y 200, en el diario: | m10-l1 |
| 50% | m25-l1 |
| 50.000 | m08-l2 |
| 50.050 | m08-l2 |
| 500 puntos | m22-l1 |
| 500 USDT | m04-l1 |
| 50× | m06-l1 |
| 58.000 | m22-l1 |
| 58.800 | m24-l1 |
| 59.000 | m03-l2 |
| 59.300 | m27-l1 |
| 59.850 | m24-l1 |
| 5R | m26-l1 |
| 60% | m22-l1 |
| 60.400 | m08-l2 |
| 61.000 | m08-l2 |
| 61.200 | m08-l2 |
| 62.000 | m03-l2 |
| 62.300 | m27-l1 |
| 63.000 | m24-l1 |
| 64.000 | m27-l1 |
| 66,7% | m25-l1 |
| 7.750 | m19-l1 |
| 70% | m28-l1 |
| 700 | m22-l1 |
| 75 | m11-l1 |
| 8 USDT | m23-l1 |
| 8% en circulación | m20-l1 |
| 8.360 | m23-l2 |
| 8.760 | m23-l2 |
| 85 | m12-l1 |
| 88: codicia extrema | m18-l1 |
| 89 | m03-l2 |
| 9 | m12-l1 |
| 9 y 21, en gráficos intradía. | m10-l1 |
| 9,5% | m06-l1 |
| 9.290 | m15-l1 |
| 9.314 | m06-l1 |
| 9.460 | m23-l2 |
| 9.500 | m06-l1 |
| 9.510 | m15-l1 |
| 9.550 | m15-l1 |
| 9.700 por debajo de él | m22-l1 |
| 9.935 | m15-l1 |
| 90 | m12-l1 |
| 90,4% | m22-l1 |
| 92 | m03-l2 |
| 920 millones de tokens restantes (el 92%) | m20-l1 |
| : tienes que duplicar lo que queda. - Pierde un | m22-l1 |
| A corto plazo, un sistema válido en mala racha no se distingue de un sistema roto. | m28-l1 |
| a cámara lenta | m26-l1 |
| a menudo | m34-l1 |
| abre en 100, sube hasta 108, cae hasta 96 y cierra en 101 | m03-l1 |
| abre en 108 y cierra en 101 sin mecha inferior | m03-l1 |
| Abre primero la temporalidad superior. | m23-l2 |
| absorbiendo | m14-l1 |
| absorción | m29-l1 |
| acelerar y salir por la línea a la que iba | m15-l1 |
| acreedores sin garantía | m02-l1 |
| activo risk-on | m17-l1 |
| Acumulación | m09-l1 |
| acumulación | m09-l1 |
| Acumulación. | m19-l2 |
| acumularlo | m30-l1 |
| adjuntar | m24-l1 |
| agotamiento local | m19-l1 |
| Agotamiento. | m19-l2 |
| agregar promedia el ruido y deja el nivel en pie | m23-l2 |
| agresor | m29-l1 |
| aguanta | m08-l1 |
| Ajusta sobre la primera mitad. | m28-l1 |
| alcista regular | m12-l1 |
| algo más de la mitad | m14-l1 |
| alrededor de un 5,5% anual | m21-l1 |
| alt | m18-l1 |
| Altcoins | m01-l1 |
| altura de la base proyectada desde la ruptura | m15-l2 |
| antes | m34-l1 |
| anti-venganza | m27-l1 |
| anticiparse | m20-l1 |
| Apalancamiento extremo. | m19-l2 |
| apertura | m03-l1 |
| API keys con permisos de más. | m02-l1 |
| API keys con permisos limitados. | m02-l1 |
| Aportan confluencia. | m13-l1 |
| Apostar a que la "alt season" está garantizada. | m17-l1 |
| app de autenticación | m02-l1 |
| Arbitraje estadístico | m35-l1 |
| Asfixiar la operación ganadora. | m27-l1 |
| asks | m31-l1 |
| Asks (ventas) | m02-l1 |
| Autenticación de dos factores (2FA). | m02-l1 |
| Autocustodia: | m02-l1 |
| aviso de que la participación se está adelgazando | m14-l1 |
| bajista regular | m12-l1 |
| bajo esos mismos dos puntos | m12-l1 |
| banda de Bollinger | m16-l1 |
| bandas | m03-l2 |
| beta superior a 1 | m22-l2 |
| bids | m31-l1 |
| Bids (compras) | m02-l1 |
| Bitcoin (BTC) | m01-l1 |
| Bitcoin y al mercado amplio | m18-l1 |
| blockchain | m01-l1 |
| bloques | m01-l1 |
| Bollinger | m16-l1 |
| bolsa de órdenes contrarias | m19-l2 |
| BOS | m34-l1 |
| BOS / CHoCH | m34-l1 |
| bracket | m24-l1 |
| BTC → ETH → alts de gran capitalización → alts de pequeña capitalización. | m17-l1 |
| C | m03-l1 |
| cada ocho horas | m04-l1 |
| Cada parámetro que añades es un grado de libertad más para que el pasado te dé la razón. | m28-l1 |
| calendario | m21-l2 |
| calendario de desbloqueo | m20-l1 |
| calendario de emisión | m20-l1 |
| calendario de vesting | m21-l2 |
| Calificar setups presupone que sabes calificar | m27-l2 |
| cambio de carácter (CHoCH) | m08-l1 |
| canal | m15-l1 |
| canal de Keltner | m16-l1 |
| Cantar un giro con un solo cambio de carácter. | m08-l1 |
| capitulación | m18-l1 |
| captura de pantalla | m27-l2 |
| cascada de liquidaciones | m06-l1 |
| Cascada. | m19-l2 |
| Cascadas de liquidación. | m05-l1 |
| Caídas bajo carga. | m21-l2 |
| CHoCH | m34-l1 |
| cientos de velas | m03-l1 |
| cierra a la fuerza | m05-l1 |
| cierran antes de que acabe el día | m23-l1 |
| cinco días pagando se llevan cinco sextos de un mes de cobros | m21-l1 |
| cinco veces | m14-l1 |
| Clasificación de régimen | m35-l1 |
| clave privada | m01-l1 |
| cobertura de cortos | m19-l1 |
| codicia extrema | m18-l1 |
| Comisiones (taker en ambos lados): | m07-l1 |
| Comisiones en cada paso. | m32-l1 |
| comisión | m23-l1 |
| comisión taker | m07-l1 |
| componente de efectivo | m01-l1 |
| compra | m19-l1 |
| compra a mercado de 2.000 unidades | m02-l1 |
| Compra el spot. | m21-l1 |
| compra limitada a 2,00 | m02-l1 |
| comprar | m19-l2 |
| Comprar justo antes de un cliff. | m20-l1 |
| compresión | m08-l2 |
| con poca profundidad | m02-l1 |
| con qué frecuencia operan | m23-l1 |
| confirma | m34-l1 |
| confirma un cambio que ya está en marcha | m10-l1 |
| Confundir apalancamiento con tamaño de posición. | m22-l1 |
| Confundir el "market cap" con dinero real. | m01-l1 |
| Confundir el market cap con la FDV. | m20-l1 |
| contar dos veces lo mismo | m18-l1 |
| contrato | m04-l1 |
| contrato inverso | m05-l1 |
| control de la salida | m22-l1 |
| control del precio | m24-l1 |
| Controles de capital y límites bancarios. | m32-l1 |
| convenciones, no como resultados. | m10-l1 |
| convención, no como una promesa | m15-l2 |
| correlación | m22-l2 |
| corto | m04-l1 |
| Corto (short): | m04-l1 |
| corto concurrido | m19-l2 |
| coste, no una estrategia | m23-l1 |
| Costes de transacción modelados | m35-l1 |
| cotiza 24 horas al día, 7 días a la semana | m17-l1 |
| Creer que "stablecoin" significa "garantizado". | m01-l1 |
| Creer que el apalancamiento aumenta el rendimiento esperado. | m05-l1 |
| cripto funciona 24/7 | m18-l1 |
| Cruce de cero: | m11-l1 |
| cruce de la línea de cero | m11-l1 |
| cruce de la línea de señal | m11-l1 |
| cruce de la muerte | m10-l1 |
| Cruce de señal: | m11-l1 |
| cruce dorado | m10-l1 |
| Cuando la banda de Bollinger queda enteramente dentro del canal de Keltner, el mercado está en > squeeze. | m16-l1 |
| Cuando la base se rompe: una señal de agotamiento. | m19-l1 |
| Cuando la tesis llegó primero. | m15-l1 |
| cuando se dispara el volumen | m21-l2 |
| cuatro a seis | m23-l2 |
| Cuenta apuestas independientes, no tickers. | m22-l2 |
| cuerpo | m03-l1 |
| cuerpos y mechas de los swings que de verdad giraron | m08-l1 |
| Custodia del exchange (custodial): | m02-l1 |
| cuánto ruido lo rodea | m23-l2 |
| cuánto tiempo mantienen | m23-l1 |
| Cuña ascendente | m15-l2 |
| Cuña descendente | m15-l2 |
| CVD | m30-l1 |
| cómo reacciona el precio ahí | m27-l1 |
| Cómo se ganan los niveles. | m27-l2 |
| cómo se reparte la convergencia | m15-l2 |
| Dar por hecho que el agresor es el lado informado. | m29-l1 |
| day trader | m23-l1 |
| Day trader | m23-l2 |
| Day trader — 1 ida y vuelta, sin funding. | m23-l1 |
| day trading | m23-l1 |
| Day trading | m26-l1 |
| Day trading. | m23-l1 |
| de días a semanas | m23-l1 |
| de forma aislada | m19-l1 |
| de minutos a horas | m23-l1 |
| de protección | m24-l1 |
| de segundos a unos pocos minutos | m23-l1 |
| de vuelta dentro | m08-l1 |
| Debajo de un mínimo reciente | m19-l2 |
| decenas o cientos de operaciones al día | m23-l1 |
| Decide el cuerpo, no la mecha | m15-l1 |
| decide peor en el momento y mejor por adelantado | m26-l1 |
| Dejarlo todo en el exchange. | m02-l1 |
| delta | m29-l1 |
| delta neutral | m21-l1 |
| Delta neutral no es margen neutral. | m21-l1 |
| demanda por un uso real | m01-l1 |
| dentro de una sola barra | m34-l1 |
| desbloqueo grande | m20-l1 |
| desde | m22-l1 |
| desequilibrado al bid | m31-l1 |
| deslizamiento (slippage) | m24-l1 |
| desmarcar | m35-l1 |
| Después baja a la temporalidad menor | m23-l2 |
| desviaciones típicas | m16-l1 |
| desviación medida respecto a la esperanza | m28-l1 |
| Diagonal: | m15-l1 |
| diferencia | m04-l1 |
| diluyendo tu media | m25-l1 |
| Dimensionamiento fraccional | m35-l1 |
| dimensionar por la recompensa en vez de por el stop | m22-l1 |
| directamente entre largos y cortos | m04-l1 |
| discount | m34-l1 |
| Disparo. | m19-l2 |
| dispersan los cierres | m16-l1 |
| distancia | m22-l1 |
| Distribución | m09-l1 |
| Divergencia alcista de CVD. | m30-l1 |
| Divergencia bajista de CVD. | m30-l1 |
| divergencia del histograma del MACD | m11-l1 |
| divergencia oculta | m12-l1 |
| divergencia regular | m12-l1 |
| DOM | m31-l1 |
| Dominancia a la baja | m17-l1 |
| Dominancia al alza | m17-l1 |
| dominancia de Bitcoin | m17-l1 |
| Dominancia de Bitcoin | m18-l1 |
| dos días y medio de volumen normal | m20-l1 |
| dos exchanges diferentes | m32-l1 |
| dos rupturas de la escalera | m34-l1 |
| dos swings claros del mismo tipo | m30-l1 |
| Dos temporalidades, tres como mucho. | m23-l2 |
| dos veces | m07-l1 |
| Dónde queda la liquidación respecto a tu stop. | m22-l1 |
| Dónde se rompe de verdad. | m22-l1 |
| efectos de red | m01-l1 |
| Ejecución frente a plan | m27-l2 |
| Ejemplo resuelto, un solo token. | m20-l1 |
| Ejemplo resuelto. | m20-l1 |
| Ejemplo trabajado (alcista) | m30-l1 |
| Ejemplo: | m09-l2 |
| El 0,5 no | m13-l1 |
| El apalancamiento absurdo está en el menú. | m05-l1 |
| El apalancamiento alto hace fatal un solo tilt. | m26-l1 |
| El apalancamiento amontonado añade combustible. | m03-l2 |
| El calendario es exacto y lo tiene todo el mundo. | m20-l1 |
| El canal describe una regularidad que se ha cumplido. Operarlo supone que la regularidad continúa, y esa suposición es la apuesta. | m15-l1 |
| El capital no es gratis. | m21-l1 |
| El capital ya tiene que estar colocado. | m32-l1 |
| El colateral que depositas. | m22-l1 |
| El contexto arriba, el trigger abajo. Nunca al revés. | m23-l2 |
| El cruzado poniendo en juego, sin avisar, toda la cuenta. | m05-l1 |
| El curso no te ha dado experiencia | m35-l1 |
| el de quien te la vende. | m35-l1 |
| El diario, creciendo. | m35-l1 |
| El dinero perdido en el stop: | m22-l1 |
| El doji. | m08-l2 |
| El exceso de apalancamiento mete tu precio de liquidación dentro del ruido normal. | m06-l1 |
| El FOMO social está fabricado. | m26-l1 |
| El funding es la pista de agotamiento más honesta. | m11-l1 |
| el funding es positivo, y funding positivo significa que los largos pagan a los cortos | m21-l1 |
| El funding es un mecanismo nativo del cripto. | m19-l1 |
| El funding es un medidor de posicionamiento, no una señal de entrada. | m19-l1 |
| El funding negativo te cobra | m21-l1 |
| El funding sigue el tiempo que mantienes. | m23-l1 |
| El funding solo existe en los perpetuos. | m23-l1 |
| El funding y el apalancamiento agrupan los stops. | m09-l1 |
| El giro, cuando llega, es violento. | m11-l1 |
| el hueco se ensancha justo cuando la masa está más loca. | m21-l1 |
| El margen cruzado convierte un solo error en un acontecimiento devastador que liquida toda la cuenta. | m06-l1 |
| El mercado funciona 24/7. | m02-l1 |
| El mismo cruce alcista de la línea de señal dentro de un rango | m11-l1 |
| El mismo cruce alcista de la línea de señal dentro de una tendencia alcista establecida | m11-l1 |
| El nocional: | m22-l1 |
| el OI te dice si un movimiento está respaldado por posiciones nuevas o solo por gente que deshace las viejas. | m19-l1 |
| El orden | m10-l1 |
| El plan | m27-l2 |
| el precio del perpetuo menos el precio del spot | m19-l1 |
| el propio exchange. | m21-l2 |
| El rango del fin de semana y el barrido del lunes. | m23-l1 |
| El reloj: normalmente cada 8 horas. | m19-l1 |
| el rendimiento del carry es un termómetro de la manía del apalancamiento | m21-l1 |
| El resultado en R | m27-l2 |
| El riesgo de cartera es tu exposición total a un mismo movimiento del mercado, sin importar en cuántas posiciones separadas lo hayas repartido. | m22-l2 |
| El riesgo no se entera de nada de esto. | m34-l1 |
| el riesgo solo se diversifica cuando la correlación está por debajo de +1. | m22-l2 |
| El setup | m27-l2 |
| el significado de una vela viene, sobre todo, de dónde ocurre. | m08-l2 |
| El stop define el riesgo; el riesgo define el tamaño. | m22-l1 |
| El stop se mueve a break-even solo cuando la operación ha producido una confirmación nueva a su favor en la temporalidad de ejecución | m27-l1 |
| el suelo del rango deja de tocarse. | m09-l2 |
| El tamaño de posición: | m22-l1 |
| el tamaño salió del stop, así que el apalancamiento no puede cambiarlo. | m22-l1 |
| el terreno está saturado: reduce tamaño, aprieta el riesgo y deja de perseguir el precio. | m18-l1 |
| el tiempo comprimido | m25-l1 |
| el tono del pasado reciente | m18-l1 |
| El trader. | m28-l1 |
| el triple | m03-l1 |
| El volumen de fin de semana es fino. | m03-l1 |
| El índice del dólar (DXY). | m17-l1 |
| Elegir un estilo que pelea con tu horario. | m23-l1 |
| EMA de 12 ha cruzado a la de 26 sin más | m11-l1 |
| EMA de 50 al alza | m27-l1 |
| Empieza donde perder no se sienta nada. | m27-l2 |
| en el plan, antes del día malo | m27-l1 |
| En la práctica: | m06-l1 |
| en R | m27-l1 |
| en su trabajo | m23-l2 |
| En un drawdown, las correlaciones de cripto saltan hacia +1: | m22-l2 |
| En un mercado sin ritmo. | m15-l1 |
| En una tendencia alcista: | m13-l1 |
| En una tendencia bajista: | m13-l1 |
| En una tendencia fuerte, un oscilador puede quedarse clavado en su extremo mucho tiempo. | m11-l1 |
| Encima de un máximo reciente | m19-l2 |
| Encontrar una divergencia en cada gráfico. | m30-l1 |
| Encuentras en la temporalidad menor una tendencia que en la mayor es un pullback. | m23-l2 |
| Ensanchar el stop. | m27-l1 |
| Envolvente | m08-l2 |
| Es agregación, no información nueva. | m23-l2 |
| Es aún menos información de lo habitual. | m15-l1 |
| es otra profesión. | m35-l1 |
| Es por exchange. | m30-l1 |
| escala con el número de operaciones, no con el tamaño del movimiento | m23-l1 |
| escala con el tiempo mantenido | m23-l1 |
| Escala solo cuando el diario lo demuestre. | m27-l2 |
| Escalar para recuperar. | m27-l2 |
| Escalonar el riesgo sobre confianza sin calificar. | m27-l2 |
| escasez creíble | m01-l1 |
| Ese número era una suposición. | m28-l1 |
| espera al cierre y comprueba si vino alguien detrás | m15-l1 |
| espera al cierre, y a que ese cierre aguante. | m08-l1 |
| esperando | m31-l1 |
| esperanza | m25-l1 |
| esperanza = win% × ganancia media − loss% × pérdida media | m25-l1 |
| Esta es la desambiguación que hay que hacer bien, porque la colisión es total y los dos mecanismos no tienen nada que ver el uno con el otro. | m16-l1 |
| Esta es la que hay que grabarse a fuego, y es donde vuelve m06, la liquidación. | m21-l1 |
| estadística sin mecanismo | m15-l2 |
| Este curso se ancla en los cierres | m15-l1 |
| Estrella de la mañana / del atardecer | m08-l2 |
| Estrella fugaz | m08-l2 |
| etapas | m09-l1 |
| ETH/BTC a la baja | m17-l1 |
| ETH/BTC al alza | m17-l1 |
| Etiquetar en retrospectiva. | m09-l1 |
| euforia | m18-l1 |
| eventos propios de cripto | m17-l1 |
| exchange centralizado (CEX) | m02-l1 |
| exchange descentralizado (DEX) | m02-l1 |
| expansión | m16-l1 |
| exposición de crédito a un emisor | m01-l1 |
| exposición direccional | m22-l2 |
| extensiones | m13-l1 |
| extremo | m19-l1 |
| Fair value gap / imbalance | m34-l1 |
| fakeout | m08-l1 |
| Fakeouts de fin de semana y de libro poco profundo. | m08-l1 |
| falsa ruptura | m09-l1 |
| Fase A | m09-l1 |
| fase A | m09-l2 |
| Fase B | m09-l1 |
| fase B | m09-l2 |
| Fase C | m09-l1 |
| fase C | m09-l2 |
| Fase D | m09-l1 |
| fase D | m09-l2 |
| Fase E | m09-l1 |
| fase E | m09-l2 |
| fases A–E | m09-l1 |
| Fiarte de una cifra agregada entre exchanges como si fuera exacta. | m29-l1 |
| Fiarte de una ruptura con volumen bajo. | m14-l1 |
| fija el criterio antes de empezar. | m28-l1 |
| fines de semana son aún más finos | m23-l1 |
| fino | m24-l1 |
| finos | m17-l1 |
| Flujo de órdenes | m29-l1 |
| FOMO | m26-l1 |
| footprint | m33-l1 |
| forma | m30-l1 |
| Forzar la historia. | m09-l1 |
| forzoso | m19-l2 |
| fracción pequeña y fija de tu cuenta | m22-l1 |
| fuera | m19-l2 |
| Funding negativo: | m19-l1 |
| Funding positivo: | m19-l1 |
| funding rate | m19-l1 |
| Funding: | m07-l1 |
| futuro con vencimiento | m23-l1 |
| futuro perpetuo | m04-l1 |
| futuros perpetuos | m23-l1 |
| Futuros trimestrales. | m21-l2 |
| ganancia está acotada | m21-l1 |
| gastado | m34-l1 |
| H | m03-l1 |
| hacia delante | m28-l1 |
| Harami | m08-l2 |
| has dejado de seguirlo | m28-l1 |
| hay más órdenes en reposo | m23-l2 |
| heatmap del libro de órdenes | m31-l1 |
| herramientas con mecánica conocida | m01-l1 |
| histograma | m11-l1 |
| histograma con signo | m16-l1 |
| histograma del MACD en busca de cambios de momentum | m11-l1 |
| Horas de pantalla. | m35-l1 |
| Horizontal (m03-l2): | m15-l1 |
| hueco | m17-l1 |
| hueco entre ambos es tu margen de maniobra | m05-l1 |
| huella del flujo de órdenes | m08-l2 |
| iceberg | m31-l1 |
| Ignorar el tramo de la divisa. | m32-l1 |
| Ignorar la ida y vuelta. | m07-l1 |
| iguales | m11-l1 |
| improvisar a mitad de operación | m27-l1 |
| Improvisar una salida. | m27-l1 |
| impulsada por lo social | m18-l1 |
| impulsivo o te aburres con facilidad | m23-l1 |
| independientes | m22-l2 |
| inferencia | m34-l1 |
| inflación | m20-l1 |
| inmediatez | m24-l1 |
| inmediatez vs precio | m24-l1 |
| instantánea inmediata | m31-l1 |
| Intentar arbitrarla siendo principiante. | m32-l1 |
| invalidado por un desbloqueo programado | m20-l1 |
| Inversión de roles (el giro). | m03-l2 |
| Ir de compras por las temporalidades. | m23-l2 |
| Juzgar el sistema por un puñado de operaciones. | m27-l2 |
| Keltner | m16-l1 |
| L | m03-l1 |
| La anchura es una lectura de la volatilidad realizada | m16-l1 |
| La base se reancla | m21-l2 |
| La compresión dice que viene una expansión. No dice hacia dónde. | m16-l1 |
| La confirmación on-chain es definitiva. | m02-l1 |
| La deriva del fin de semana. | m17-l1 |
| la diagonal es el instrumento más débil de este curso. | m15-l1 |
| La dimensión de la frecuencia. | m22-l1 |
| la distribución es la misma historia del revés | m09-l2 |
| la divergencia regular compara los extremos y espera un giro; la oculta aparece en el retroceso y espera que la tendencia se reanude. | m12-l1 |
| La dominancia subió del 50% al 56% mientras el propio precio de Bitcoin caía un 10%. | m17-l1 |
| la EMA reacciona más rápido (menos retardo), pero esa velocidad también la hace más ruidosa | m10-l1 |
| la liberación de los posicionados | m21-l2 |
| la liquidación nunca debe ser tu stop efectivo. | m22-l1 |
| la línea MACD cruzó por encima de su señal precisamente porque la línea MACD giró al alza | m11-l1 |
| la misma serie de precio, vela por vela, hasta el final del tramo común | m19-l1 |
| la misma vela | m29-l1 |
| la mitad | m03-l1 |
| La parte con mecanismo. | m15-l2 |
| La parte sin mecanismo. | m15-l2 |
| La pendiente. | m10-l1 |
| La posición del precio. | m10-l1 |
| La regla honesta: las decenas no dicen nada, los cientos empiezan a hablar. | m28-l1 |
| La regla: | m26-l1 |
| La ruptura sigue la misma disciplina que todo lo demás en este bloque: | m15-l2 |
| la ruptura va primero | m34-l1 |
| La sesión asiática, aproximadamente de 00:00 a 08:00 UTC | m23-l1 |
| La temporalidad cambia la lectura. | m30-l1 |
| la temporalidad superior dicta el sesgo, la temporalidad inferior dicta la entrada | m27-l1 |
| La temporalidad superior pone el contexto. La inferior pone la ejecución. | m23-l2 |
| La tendencia ascendida a ley. | m34-l1 |
| La vela de rango pequeño. | m08-l2 |
| La volatilidad más el apalancamiento vuelven letal el sobredimensionar. | m22-l1 |
| la volatilidad se agrupa | m16-l1 |
| La volatilidad y el momentum se derivan ambos del propio precio | m18-l1 |
| La zona dibujada a posteriori. | m34-l1 |
| La única regla inviolable: el stop solo se mueve a favor de la operación. | m27-l1 |
| largo | m04-l1 |
| Largo (long): | m04-l1 |
| Las comisiones siguen el número de operaciones. | m23-l1 |
| las comisiones y el funding | m25-l1 |
| las dos ejecuciones | m07-l1 |
| Las dos patas tienen que estar en algún sitio. | m21-l1 |
| Las emisiones son una venta de fondo constante. | m20-l1 |
| las fechas de vencimiento son ráfagas programadas de flujo mecánico en el perpetuo | m21-l2 |
| Las transacciones son irreversibles. | m01-l1 |
| las últimas velas contrarias antes de él | m34-l1 |
| Lee la secuencia hacia delante, nunca hacia atrás. | m34-l1 |
| Leer el volumen de forma aislada. | m14-l1 |
| Leer un CVD que sube como "el precio va a subir". | m30-l1 |
| Leer una prima como señal de compra. | m32-l1 |
| lenta | m10-l1 |
| lente para leer esa forma | m09-l1 |
| libro de órdenes fino de una altcoin | m09-l2 |
| libros de alts poco profundos | m12-l1 |
| Libros finos, sobre todo fines de semana y alts. | m19-l2 |
| Limita el grupo, no solo la línea. | m22-l2 |
| lineal | m05-l1 |
| Liquidación | m05-l1 |
| Liquidity grab / sweep | m34-l1 |
| Lista blanca de direcciones de retiro. | m02-l1 |
| llega con una frase razonable puesta | m26-l1 |
| Lo cerca que queda tu liquidación. | m05-l1 |
| Lo conocido se anticipa | m21-l2 |
| Lo predeterminado sigue siendo lo predeterminado. | m27-l2 |
| Lo que cuesta operar de verdad. | m28-l1 |
| Lo que sí hay es un mecanismo: | m23-l2 |
| Londres, aproximadamente de 07:00 a 16:00 UTC | m23-l1 |
| long | m06-l1 |
| long con 1 BTC a 20.000 | m07-l1 |
| Long squeeze (squeeze de largos): | m19-l2 |
| Long: | m06-l1 |
| Look-ahead | m28-l1 |
| los cortos pagan a los largos | m19-l1 |
| Los extremos pueden persistir durante semanas o meses. | m18-l1 |
| los largos pagan a los cortos. | m19-l1 |
| Los libros de las alts son peores. | m03-l2 |
| Los libros poco profundos de las alts abaratan los springs. | m09-l1 |
| Los libros poco profundos de las alts amplifican cada cascada. | m06-l1 |
| Los libros poco profundos de las alts convierten órdenes corrientes en su peor enemigo. | m24-l1 |
| Los libros poco profundos de las alts tragan mal. | m20-l1 |
| Los libros poco profundos de los alts clavan el extremo más tiempo. | m11-l1 |
| Los libros poco profundos producen falsas rupturas. | m03-l2 |
| Los límites de temporalidad son arbitrarios. | m03-l1 |
| Los límites honestos de la demo. | m27-l2 |
| Los mercados 24/7 no se reinician. | m11-l1 |
| Los mercados 24/7, sin campana de cierre, hacen que el riesgo de no ejecución del stop-limit sea real, no teórico. | m24-l1 |
| Los números redondos y los fibs se agrupan. | m13-l1 |
| Los perpetuos de alts llegan a extremos mayores. | m19-l1 |
| Los rangos persisten y los niveles se arrastran entre "días". | m03-l2 |
| Los rangos se rompen de verdad en ambas direcciones. | m09-l2 |
| Los testeos cortan por los dos lados. | m03-l2 |
| Los tipos de interés. | m17-l1 |
| límite | m24-l1 |
| límite de pérdida diaria | m26-l1 |
| línea de cero | m11-l1 |
| línea de señal | m11-l1 |
| línea de tendencia | m15-l1 |
| línea MACD | m11-l1 |
| m02. | m21-l2 |
| m06. | m21-l2 |
| m09 | m34-l1 |
| m11 | m16-l1 |
| m20 | m21-l2 |
| m21-l2 | m35-l1 |
| m25 | m28-l1 |
| m25-l1 | m22-l1 |
| m28 | m35-l1 |
| m30 — CVD. | m29-l1 |
| m31 — el libro de órdenes. | m29-l1 |
| m32 — la prima entre exchanges. | m29-l1 |
| m33 | m34-l1 |
| m33 — gráficos de footprint y perfil de volumen. | m29-l1 |
| m34 | m35-l1 |
| m34-l1 | m08-l1 |
| MACD | m11-l1 |
| Mantenimientos programados. | m21-l2 |
| mapa | m09-l1 |
| marca | m04-l1 |
| Marco macro → sesgo y niveles. | m27-l1 |
| Marco micro → trigger y stop. | m27-l1 |
| margen aislado | m05-l1 |
| Margen aislado (isolated) | m06-l1 |
| margen cruzado | m05-l1 |
| Margen cruzado (cross) | m06-l1 |
| margen inicial | m05-l1 |
| mark | m04-l1 |
| Markdown | m09-l1 |
| market cap | m01-l1 |
| Market cap = precio × oferta circulante. | m20-l1 |
| market cap y la FDV | m20-l1 |
| Markup | m09-l1 |
| Martillo / pin bar | m08-l2 |
| Matiz cripto: | m07-l1 |
| mecha de caza de stops | m09-l2 |
| mecha larga | m03-l1 |
| mechas | m03-l1 |
| Mechas de caza de stops. | m08-l1 |
| Mechas de fin de semana. | m06-l1 |
| media móvil (MM) | m10-l1 |
| media móvil exponencial (EMA) | m10-l1 |
| media móvil simple (SMA) | m10-l1 |
| memoria | m03-l2 |
| mercado | m24-l1 |
| merece la pena entender este dialecto porque la masa lo habla | m34-l1 |
| Microestructura medida | m35-l1 |
| miedo extremo | m18-l1 |
| mientras la zona esté concurrida | m34-l1 |
| mientras tus monedas estén en un exchange, es el exchange quien las guarda por ti. | m02-l1 |
| Mira qué hace el interés abierto alrededor. | m21-l2 |
| misma | m08-l2 |
| Momentum y volumen de mercado (~25%) | m18-l1 |
| Mover el stop a break-even: con un test, no con una sensación. | m27-l1 |
| Mover o ensanchar el stop una vez dentro. | m22-l1 |
| movimiento bruto del 3 % | m23-l1 |
| muerta | m27-l1 |
| muestra | m25-l1 |
| muro | m31-l1 |
| más allá | m08-l1 |
| más alto | m03-l1 |
| más gente durante más tiempo | m23-l2 |
| más tácticas | m35-l1 |
| más volumen | m08-l1 |
| máximo de giro | m03-l2 |
| máximo del swing | m13-l1 |
| máximo previo | m27-l1 |
| máximos más altos (HH) | m08-l1 |
| máximos más altos y mínimos más altos | m03-l2 |
| máximos más bajos (LH) | m08-l1 |
| máximos más bajos y mínimos más bajos | m03-l2 |
| Mídelo contra el libro, no contra la capitalización. | m21-l2 |
| mínimo de giro | m03-l2 |
| mínimo del swing | m13-l1 |
| mínimo nuevo con él | m30-l1 |
| mínimos crecientes | m09-l2 |
| mínimos más altos (HL) | m08-l1 |
| mínimos más bajos (LL) | m08-l1 |
| múltiplos R | m25-l1 |
| Nada de esto predice la dirección. Todo esto predice las condiciones. | m21-l2 |
| nada que el panel de precio de arriba no contenga ya | m16-l1 |
| nadie está obligado a mantenerla | m15-l1 |
| Nadie puede arbitrar una cantidad infinita. | m21-l1 |
| narrativa | m01-l1 |
| nativos de cripto | m04-l1 |
| negativo | m19-l2 |
| negocio | m21-l1 |
| negocio de margen fino con colas gordas | m21-l1 |
| Neto = +2R | m22-l1 |
| Neto: `300 − 120 = 180 USDT`. | m23-l1 |
| Neto: `300 − 8 = 292 USDT`. | m23-l1 |
| Neto: `300 − 8 − 18 = 274 USDT`. | m23-l1 |
| ningún mecanismo | m13-l1 |
| no es un sistema, es una descripción | m28-l1 |
| no hacer casi nada | m27-l1 |
| No hacer nada, la mayor parte del tiempo. | m27-l1 |
| no hay 60 patrones, hay dos mecánicas con 60 nombres. | m08-l2 |
| No hay ritual de apertura ni de cierre. | m03-l1 |
| no hay un sistema nuevo, hay tres mecánicas con más nombres. | m34-l1 |
| no realizada | m07-l1 |
| no tiene fecha de vencimiento | m04-l1 |
| No todo token desbloqueado se vende. | m21-l2 |
| No todos los perpetuos usan una stablecoin. | m05-l1 |
| No vuelvas a subir para justificar la operación. | m23-l2 |
| nocional = 100 ÷ 0,10 = 1.000 USDT por posición. | m22-l2 |
| nocional × la tasa de funding | m04-l1 |
| nodo de volumen bajo | m33-l1 |
| none | m09-l1 |
| Nueva York, aproximadamente de 13:00 a 21:00 UTC. | m23-l1 |
| nunca | m27-l1 |
| nunca cierra | m04-l1 |
| Nunca escales para recuperar. | m27-l2 |
| nunca leas el OI sin el precio | m19-l1 |
| número de operaciones | m23-l1 |
| número redondo | m13-l1 |
| O | m03-l1 |
| o más | m24-l1 |
| observado | m28-l1 |
| oferta circulante | m20-l1 |
| oferta circulante, total y máximo | m20-l1 |
| oferta máxima | m20-l1 |
| oferta programada y pública que llega a un libro | m21-l2 |
| oferta total | m20-l1 |
| once veces | m20-l1 |
| opciones | m35-l1 |
| open interest (OI) | m19-l1 |
| operación aislada | m22-l1 |
| operación descartada | m27-l1 |
| operar el agotamiento | m19-l2 |
| Operar la dominancia como si fuera dirección. | m17-l1 |
| Operar la temporalidad menor contra la mayor es operar el ruido contra la señal que lo contiene. | m23-l2 |
| Operar tamaño real con un sistema sin validar. | m27-l2 |
| operar una divergencia en espacio abierto | m12-l1 |
| Operarla sin un nivel y sin un stop. | m30-l1 |
| orden | m24-l1 |
| Orden de mercado (market) | m02-l1 |
| Orden limitada (limit) | m02-l1 |
| order block | m34-l1 |
| Order block | m34-l1 |
| oscilador | m11-l1 |
| overrun | m08-l2 |
| paciencia | m23-l1 |
| pagas | m04-l1 |
| Papel o tamaño mínimo primero. | m27-l2 |
| parabólicos | m12-l1 |
| paralela | m15-l1 |
| participación | m03-l1 |
| Participación detrás | m15-l2 |
| pasivo en los libros del exchange | m02-l1 |
| patrón | m15-l2 |
| Payoff | m25-l1 |
| pequeña porción de su oferta en circulación | m20-l1 |
| perfil de volumen | m33-l1 |
| periodo de tenencia | m23-l1 |
| Pero mucha más volatilidad, así que las MM rápidas son más ruidosas. | m10-l1 |
| Perpetuo por debajo del spot: un descuento. | m19-l1 |
| Perpetuo por encima del spot: una prima. | m19-l1 |
| Perpetuos y spot cuentan historias distintas. | m30-l1 |
| perseguir el squeeze cuando ya está gastado. | m19-l2 |
| Perseguir la primera vela pasada un nivel. | m08-l1 |
| Pide el mecanismo. | m35-l1 |
| Pinzas | m08-l2 |
| PnL bruto: | m07-l1 |
| PnL neto realizado | m07-l1 |
| POC | m33-l1 |
| pon a prueba la afirmación antes de pagar por saberla. | m28-l1 |
| Pondera un cruce del MACD según qué línea se cruzó y según el régimen en que ocurrió. | m11-l1 |
| Pondera una señal por la sesión en la que se imprimió. | m23-l1 |
| ponerse corto contra una tendencia fuerte porque "tiene que estar agotada" | m12-l1 |
| Ponte corto en el perpetuo. | m21-l1 |
| por debajo de 30 = sobreventa | m11-l1 |
| por ejecución | m23-l1 |
| por encima | m22-l1 |
| por encima de 70 = sobrecompra | m11-l1 |
| por encima o por debajo del punto medio | m34-l1 |
| por nivel de precio | m33-l1 |
| Por qué ahí y en ningún otro sitio: | m27-l1 |
| Por qué aquí: | m09-l1 |
| Por qué confluencia y no una sola línea: | m27-l1 |
| Por qué el orden no se puede invertir: | m27-l1 |
| Por qué el punto de partida no importa. | m30-l1 |
| Por qué el tamaño al final: | m27-l1 |
| Por qué empezar aquí: | m27-l1 |
| Por qué en R y no en dinero: | m27-l2 |
| Por qué es el número correcto: | m25-l1 |
| Por qué es frágil. | m31-l1 |
| Por qué es un shock, con números. | m20-l1 |
| Por qué es un tipo de dato distinto. | m31-l1 |
| Por qué es un viento en contra. | m20-l1 |
| Por qué es una forma de datos distinta. | m33-l1 |
| Por qué esperar el trigger: | m27-l1 |
| Por qué este orden. | m22-l1 |
| Por qué esto mejora los "soportes y resistencias". | m33-l1 |
| Por qué existe la distinción. | m07-l1 |
| Por qué existen dos precios. | m04-l1 |
| Por qué hay dos tarifas. | m07-l1 |
| Por qué importa el reloj. | m23-l1 |
| Por qué importa la distancia. | m20-l1 |
| Por qué importa más que la puntuación: | m27-l2 |
| Por qué importa: | m03-l1 |
| Por qué importa: la mitad que en realidad es solo precio. | m18-l1 |
| Por qué las pruebas no son opcionales: | m27-l2 |
| Por qué marca oportunidad. | m18-l1 |
| Por qué merece una mirada propia. | m19-l1 |
| Por qué mienten las muestras pequeñas: | m25-l1 |
| Por qué ninguno sirve solo: | m25-l1 |
| Por qué no es volumen. | m29-l1 |
| por qué ocurre | m26-l1 |
| Por qué puede existir. | m32-l1 |
| Por qué se adelanta al precio. | m14-l1 |
| Por qué se adelanta. | m30-l1 |
| Por qué se retroalimenta. | m06-l1 |
| Por qué se sitúa justo ahí. | m06-l1 |
| Por qué siempre se lee en relativo. | m14-l1 |
| Por qué significa "continuación": | m12-l1 |
| Por qué significa "giro": | m12-l1 |
| Por qué tan pequeña. | m22-l1 |
| Por qué te avisa. | m18-l1 |
| Por qué una regla mecánica y no criterio: | m27-l1 |
| Por qué validar siquiera: | m27-l2 |
| Por qué: | m09-l2 |
| posicionamiento y flujo | m32-l1 |
| posiciones, contra el margen de su propia cuenta | m21-l1 |
| Precio abajo, OI abajo: | m19-l1 |
| Precio abajo, OI arriba: | m19-l1 |
| Precio arriba, OI abajo: | m19-l1 |
| Precio arriba, OI arriba: | m19-l1 |
| precio de marca | m04-l1 |
| Precio por encima de una MM rápida que sube, y la rápida por encima de la lenta = tendencia alcista; la imagen espejo = tendencia bajista. | m10-l1 |
| precios de liquidación de los cortos apalancados | m19-l2 |
| precios de liquidación de los largos apalancados | m19-l2 |
| precompromiso | m26-l1 |
| premium | m34-l1 |
| Premium / discount | m34-l1 |
| presupuesto de riesgo | m22-l1 |
| previo a la sesión | m23-l1 |
| prima de Coinbase | m32-l1 |
| prima del 1,5 % | m32-l1 |
| programada | m17-l1 |
| programada por el reloj | m23-l1 |
| prueba | m09-l2 |
| publicaciones macro | m17-l1 |
| pullback | m08-l1 |
| pérdida acotada | m02-l1 |
| pérdida no está acotada por el mismo diseño | m21-l1 |
| que el histograma llegue a cero y que el cruce ocurra son el mismo evento. | m11-l1 |
| quedarte donde estás y hacerlo más veces. | m35-l1 |
| quién tiene qué | m21-l2 |
| qué aspecto tiene con números reales | m26-l1 |
| Qué aspecto tiene. | m14-l1 |
| Qué cambia de verdad: | m22-l1 |
| qué es | m26-l1 |
| Qué es idéntico a 5× y a 20×: | m22-l1 |
| Qué son. | m07-l1 |
| Qué ves que una vela esconde. | m33-l1 |
| Qué: | m09-l2 |
| R | m22-l1 |
| racha perdedora | m28-l1 |
| rangos | m09-l1 |
| ratio ETH/BTC | m17-l1 |
| raíz cuadrada | m28-l1 |
| Reacciona a los datos macro en tiempo real, incluso cuando nada más puede. | m17-l1 |
| rechazo | m08-l2 |
| recorre una barra | m16-l1 |
| Redes sociales (~15%) | m18-l1 |
| reduce-only | m24-l1 |
| Reduce-only es una salvaguarda propia de los perpetuos. | m24-l1 |
| Releer. | m35-l1 |
| relojes distintos | m23-l1 |
| rendimiento anual de en torno al 5%, delta neutral | m21-l1 |
| repartidas por una banda de precios | m03-l2 |
| resistencia en torno a 29.640 | m09-l2 |
| resistencias | m03-l1 |
| resultado neto | m07-l1 |
| resumen | m29-l1 |
| retestear y aguantar | m08-l1 |
| retirar sus cotizaciones | m31-l1 |
| retiros desactivados | m02-l1 |
| retroceso 0,618 | m27-l1 |
| retrocesos de Fibonacci | m13-l1 |
| revisión semanal | m27-l2 |
| Riesgo de cartera | m22-l1 |
| Riesgo de gap, 24/7. | m22-l1 |
| riesgo nocturno te destroza el sueño | m23-l1 |
| risk-off | m17-l1 |
| Risk-off: | m17-l1 |
| Risk-on: | m17-l1 |
| ritmo de cambio | m12-l1 |
| ritmo de emisión/inflación | m20-l1 |
| ritmo puede agotarse y ceder por la línea sobre la que estaba construido | m15-l1 |
| RS | m11-l1 |
| RS = ganancia media ÷ pérdida media | m11-l1 |
| RSI | m11-l1 |
| ruido | m03-l1 |
| ruido de temporalidad baja | m03-l1 |
| Ruido de wash trading. | m14-l1 |
| ruptura de estructura (BOS) | m08-l1 |
| ruptura genuina | m08-l1 |
| rápida | m10-l1 |
| sabes distinguir una afirmación con mecanismo de una que no lo tiene. | m35-l1 |
| salto del 20% en la oferta circulante de la noche a la mañana | m20-l1 |
| Sangrado por funding en un long mantenido. | m07-l1 |
| saturación | m31-l1 |
| Scalper | m23-l2 |
| Scalper — 15 idas y vueltas, sin funding. | m23-l1 |
| scalping | m23-l1 |
| Scalping | m26-l1 |
| Scalping. | m23-l1 |
| Se calcula por completo a partir de la serie de precios. | m18-l1 |
| se comprime a sí misma | m21-l1 |
| se derrumba | m32-l1 |
| se ensancha | m32-l1 |
| segunda mitad, que no has mirado nunca | m28-l1 |
| sentimiento de masas | m18-l1 |
| serie temporal | m33-l1 |
| Sesgo de retrospectiva. | m09-l2 |
| Sesgo de supervivencia | m28-l1 |
| señal que puedes notar | m26-l1 |
| shock de oferta que el gráfico no puede mostrar | m20-l1 |
| short squeeze | m09-l1 |
| Short squeeze (squeeze de cortos): | m19-l2 |
| Short: | m06-l1 |
| Si no puedes nombrar la mecánica, no hay operación. | m34-l1 |
| Sin cierre, fines de semana finos. | m05-l1 |
| Sin diario, cada pérdida es ambigua. | m27-l2 |
| Sin fronteras de sesión. | m14-l1 |
| Sin huecos, una serie continua. | m10-l1 |
| sin límite | m24-l1 |
| Sin operador central. | m01-l1 |
| SMA50 informa en la práctica de un precio de hace unas 25 velas | m10-l1 |
| smart money | m34-l1 |
| sobreajuste | m28-l1 |
| Sobredimensionar "solo por esta vez". | m22-l1 |
| solapamiento, más o menos de 13:00 a 16:00 UTC | m23-l1 |
| solo lectura | m02-l1 |
| solo para volver a estar en tablas. - Pierde un | m22-l1 |
| Somete la cartera a estrés. | m22-l2 |
| Son autocumplidos. | m13-l1 |
| son el mismo gráfico | m14-l1 |
| soporte en torno a 28.140 | m09-l2 |
| soportes | m03-l1 |
| spoofing | m31-l1 |
| squeeze | m19-l2 |
| Squeeze de liquidez / short squeeze | m16-l1 |
| Squeeze de volatilidad | m16-l1 |
| squeeze de volatilidad | m19-l2 |
| Stablecoins | m01-l1 |
| stop ajustado permite una más grande, para el mismo riesgo | m22-l1 |
| stop ancho fuerza una posición más pequeña | m22-l1 |
| stop es de la temporalidad por la que entraste | m23-l2 |
| stop y tu tamaño de posición tienen que vigilar por ti | m23-l1 |
| stop-limit | m24-l1 |
| stop-loss (SL) | m24-l1 |
| stop-loss de cortos | m19-l2 |
| stop-loss de largos | m19-l2 |
| stop-market | m24-l1 |
| suelo móvil en una tendencia alcista o un techo en una bajista | m10-l1 |
| Suficientes operaciones antes de juzgar. | m27-l2 |
| swing trader | m23-l1 |
| Swing trader | m23-l2 |
| Swing trader — 1 ida y vuelta, 6 intervalos de funding. | m23-l1 |
| swing trading | m23-l1 |
| Swing trading | m26-l1 |
| Swing trading. | m23-l1 |
| sí | m35-l1 |
| take-profit (TP) | m24-l1 |
| taker era el comprador | m29-l1 |
| Tamaño de posición = presupuesto de riesgo ÷ distancia del stop. | m22-l1 |
| También se calcula directamente del precio y el volumen. | m18-l1 |
| tasa de funding | m04-l1 |
| Tasa de funding negativa → los cortos pagan a los largos. | m04-l1 |
| Tasa de funding positiva → los largos pagan a los cortos. | m04-l1 |
| tasa de margen de mantenimiento | m06-l1 |
| tasa de margen inicial | m06-l1 |
| Te quedas con la pata ganadora de una cobertura cuya pata perdedora ha sido cerrada al peor precio posible | m21-l1 |
| Ten claro en qué sesión operas de verdad. | m23-l1 |
| tendencia fuerte | m12-l1 |
| tendencia previa | m09-l1 |
| tendencia, no un calendario | m17-l1 |
| Tendencias de búsqueda | m18-l1 |
| termina | m34-l1 |
| termómetro de la manía del apalancamiento | m19-l1 |
| test | m30-l1 |
| Tiempo de transferencia. | m32-l1 |
| Tiene que haber participación detrás | m15-l1 |
| Tienes claves, no cuentas. | m01-l1 |
| tokenómica | m20-l1 |
| Tomas de beneficio parciales: una elección de estilo, con su precio honesto. | m27-l1 |
| Total: −300 USDT = 3% de la cuenta, de un solo movimiento. | m22-l2 |
| trabajo a tiempo completo | m23-l1 |
| tramo cruzado dentro de una sola vela | m34-l1 |
| tramo de impulso | m13-l1 |
| trampa del coste hundido | m26-l1 |
| Trata la zona como zona. | m34-l1 |
| Tratar a cripto como un refugio seguro. | m17-l1 |
| Tratar el delta como una señal de dirección. | m29-l1 |
| tres | m22-l2 |
| tres veces | m14-l1 |
| trigger (trigger) | m24-l1 |
| Triángulo ascendente | m15-l2 |
| Triángulo descendente | m15-l2 |
| Triángulo simétrico | m15-l2 |
| tu orden no se ejecuta | m24-l1 |
| tu propio | m19-l2 |
| Tus ganancias y tus pérdidas, de forma simétrica. | m05-l1 |
| Un cuerpo que cierra al otro lado de la línea | m15-l2 |
| Un gráfico no tiene opinión. Tiene la opinión de su temporalidad. | m23-l2 |
| Un mercado 24/7 pone a prueba los niveles una y otra vez. | m13-l1 |
| un mercado tranquilo no es un mercado seguro. Es un mercado que todavía no se ha movido. | m16-l1 |
| un nivel es un precio, y un precio es el mismo número en todos los gráficos. | m23-l2 |
| un OI que sube significa que se abren posiciones nuevas; un OI que baja significa que se cierran posiciones existentes. | m19-l1 |
| un ojo que ha visto el desenlace no puede dejar de verlo. | m28-l1 |
| un ritmo constante de avance | m15-l1 |
| Un stop-limit de protección que atraviesa el hueco y nunca se ejecuta. | m24-l1 |
| Un suelo para lo estrecho que puede ser el stop. | m22-l1 |
| un único rango de acumulación de principio a fin | m09-l2 |
| una | m22-l1 |
| Una advertencia que conviene tener ya. | m29-l1 |
| una compresión que aún no se ha resuelto no es una señal. | m15-l2 |
| Una de cada cuatro veces, una moneda sin trucar te da doce aciertos o más: un 60% de win rate. | m28-l1 |
| Una orden de mercado arrojada a un libro poco profundo. | m24-l1 |
| Una palabra, dos mecanismos. | m19-l2 |
| Una prima no es una dirección | m19-l1 |
| Una reacción trabajada. | m10-l1 |
| Una ruptura con volumen débil | m14-l1 |
| Una ruptura con volumen fuerte | m14-l1 |
| una sola apuesta de ~3% con tres trajes. | m22-l2 |
| una sola vela | m19-l2 |
| una sola vela de pullback dentro de una tendencia bajista | m23-l2 |
| una vela | m03-l1 |
| una vela verde | m23-l2 |
| unlock | m17-l1 |
| USDC | m01-l1 |
| UST | m01-l1 |
| vacío de liquidez | m34-l1 |
| Validación walk-forward | m35-l1 |
| valor justo | m04-l1 |
| valor nocional | m05-l1 |
| Valoración totalmente diluida (FDV) = precio × oferta máxima. | m20-l1 |
| varianza | m25-l1 |
| vecinas | m34-l1 |
| velas | m03-l1 |
| Vencimientos de opciones. | m21-l2 |
| vender | m19-l2 |
| venganza | m26-l1 |
| ver | m30-l1 |
| Volatilidad (~25%) | m18-l1 |
| volatilidad y barridos probables | m19-l2 |
| volumen de compra taker | m29-l1 |
| Volumen fino de fin de semana. | m14-l1 |
| wash trading | m14-l1 |
| whipsaw | m10-l1 |
| Win rate | m25-l1 |
| win rate de equilibrio | m25-l1 |
| win rate genuinamente más alto solo para no perder | m23-l1 |
| win% de equilibrio = 1 ÷ (1 + payoff) | m25-l1 |
| Wyckoff | m09-l1 |
| y abrir un corto | m24-l1 |
| yo tranquilo y fuera del mercado siendo anulado | m26-l1 |
| zona a vigilar, no una línea que tenga que aguantar | m10-l1 |
| zona contraria | m18-l1 |
| zona de interés | m18-l1 |
| zona de origen | m34-l1 |
| zona dorada 0,5–0,618 | m13-l1 |
| «El sistema falló». | m27-l2 |
| «las cuñas ascendentes rompen a la baja, las descendentes al alza» | m15-l2 |
| «No puedo cerrar» como riesgo real. | m21-l2 |
| «No seguí el sistema». | m27-l2 |
| «not your keys, not your coins» | m02-l1 |
| «¿quién está absorbiendo, y en qué lado?» | m09-l1 |
| ¿A quién le vende? | m21-l2 |
| ¿Quién compró antes? | m21-l2 |
| ¿Qué pasa el día de la fecha? | m21-l2 |
| área de valor | m33-l1 |
| índice de miedo y codicia | m18-l1 |
| último precio | m04-l1 |
| → necesitas | m22-l1 |
| −1 | m22-l2 |
| −100 USDT | m22-l2 |
| −18,00 USDT | m07-l1 |
| −18.800 | m30-l1 |
| −1R | m22-l1 |
| −20 USDT por operación | m25-l1 |
| −22,22 USDT | m07-l1 |
| −300 | m30-l1 |
| −32 | m11-l1 |
| −4.800 | m30-l1 |
| −500 | m11-l1 |
| −800 | m30-l1 |

### EN — 1735 spans, 1356 distinct

| Span | Lessons |
| --- | --- |
| What it is. | m04-l1, m07-l1, m08-l2, m14-l1, m18-l1, m22-l1, m26-l1, m29-l1, m30-l1, m31-l1, m32-l1, m33-l1 |
| In practice. | m04-l1, m07-l1, m08-l2, m14-l1, m18-l1, m23-l1, m26-l1, m27-l1, m29-l1, m30-l1, m31-l1 |
| 24/7 | m03-l2, m04-l1, m08-l2, m09-l2, m12-l1, m25-l1 |
| support | m03-l1, m03-l2, m08-l1, m09-l1, m09-l2, m13-l1 |
| basis | m16-l1, m19-l1, m21-l1, m32-l1, m34-l1 |
| funding | m07-l1, m11-l1, m12-l1, m18-l1, m23-l1 |
| liquidation | m04-l1, m22-l2, m24-l1, m26-l1, m27-l1 |
| m08-l1 | m15-l1, m15-l2, m16-l1, m23-l2, m34-l1 |
| m26 | m16-l1, m23-l2, m28-l1, m34-l1, m35-l1 |
| resistance | m03-l1, m03-l2, m08-l1, m09-l1, m09-l2 |
| 10,000 USDT | m22-l1, m22-l2, m23-l1, m27-l1 |
| 60,000 | m19-l1, m22-l1, m24-l1, m27-l1 |
| generated instance | m08-l1, m08-l2, m09-l2, m24-l1 |
| m08-l2 | m15-l2, m16-l1, m27-l1, m34-l1 |
| m19-l2 | m15-l1, m16-l1, m21-l1, m34-l1 |
| m22 | m16-l1, m23-l2, m34-l1, m35-l1 |
| m23-l1 | m10-l1, m17-l1, m21-l1, m23-l2 |
| m27-l1 | m03-l2, m22-l1, m23-l1, m23-l2 |
| not | m05-l1, m18-l1, m20-l1, m34-l1 |
| spring | m09-l1, m09-l2, m29-l1, m30-l1 |
| Why it matters. | m04-l1, m08-l2, m22-l1, m29-l1 |
| Worked example. | m20-l1, m29-l1, m31-l1, m32-l1 |
| +500 | m11-l1, m29-l1, m30-l1 |
| 0 | m11-l1, m22-l2, m30-l1 |
| 1% | m22-l1, m26-l1, m27-l1 |
| 100 | m03-l2, m11-l1, m28-l1 |
| close | m03-l1, m08-l1, m23-l2 |
| downtrend | m03-l2, m08-l1, m10-l1 |
| high | m03-l1, m23-l2, m34-l1 |
| higher high | m08-l1, m12-l1, m30-l1 |
| low | m03-l1, m23-l2, m34-l1 |
| lower low | m08-l1, m12-l1, m30-l1 |
| m10-l1 | m15-l2, m23-l1, m34-l1 |
| m14 | m15-l1, m15-l2, m16-l1 |
| m15-l1 | m08-l1, m15-l2, m28-l1 |
| m16-l1 | m08-l2, m19-l2, m22-l1 |
| m27-l2 | m27-l1, m28-l1, m35-l1 |
| maker | m07-l1, m24-l1, m29-l1 |
| price | m12-l1, m19-l1, m33-l1 |
| range | m03-l2, m09-l1, m10-l1 |
| spread | m02-l1, m23-l1, m31-l1 |
| structure | m03-l2, m08-l1, m12-l1 |
| taker | m07-l1, m24-l1, m29-l1 |
| thin | m02-l1, m17-l1, m24-l1 |
| uptrend | m03-l2, m08-l1, m10-l1 |
| volume | m03-l1, m03-l2, m23-l2 |
| Volume | m03-l1, m14-l1, m30-l1 |
| 0.5 | m13-l1, m25-l1 |
| 1,745 | m09-l1, m09-l2 |
| 1,800 | m09-l1, m09-l2 |
| 1,810 | m09-l2, m34-l1 |
| 100 USDT | m22-l1, m27-l1 |
| 15% | m19-l1, m19-l2 |
| 1R | m26-l1, m27-l1 |
| 2,000 | m19-l1, m22-l1 |
| 24/7, no closing bell. | m19-l2, m20-l1 |
| 25,400 | m09-l2, m19-l2 |
| 50 | m11-l1, m28-l1 |
| 5× | m07-l1, m22-l1 |
| 60,300 | m19-l1, m27-l1 |
| ATR | m16-l1, m22-l1 |
| band | m03-l2, m13-l1 |
| Bitcoin dominance | m17-l1, m18-l1 |
| conceptual | m31-l1, m33-l1 |
| confluence | m14-l1, m27-l1 |
| context | m11-l1, m18-l1 |
| Cross margin | m05-l1, m06-l1 |
| daily stop | m22-l1, m27-l1 |
| day | m22-l1, m27-l1 |
| Day trading | m23-l1, m26-l1 |
| Distribution | m09-l1, m09-l2 |
| divergence | m12-l1, m29-l1 |
| funding rate | m04-l1, m19-l1 |
| higher low | m12-l1, m30-l1 |
| How this burns people. | m12-l1, m18-l1 |
| Isolated margin | m05-l1, m06-l1 |
| Liquidation | m05-l1, m19-l2 |
| liquidations | m18-l1, m19-l2 |
| Liquidity | m19-l2, m24-l1 |
| long | m04-l1, m06-l1 |
| lower | m03-l1, m30-l1 |
| lower high | m12-l1, m30-l1 |
| m03-l2 | m15-l1, m23-l2 |
| m04-l1 | m21-l1, m21-l2 |
| m06-l1 | m22-l1, m34-l1 |
| m13 | m15-l2, m34-l1 |
| m15-l2 | m08-l2, m16-l1 |
| m16 | m15-l2, m35-l1 |
| m19 | m16-l1, m34-l1 |
| m19-l1 | m21-l1, m21-l2 |
| m21-l1 | m19-l1, m21-l2 |
| m24 | m28-l1, m35-l1 |
| m29 | m23-l2, m34-l1 |
| m31 | m21-l2, m35-l1 |
| m32 | m34-l1, m35-l1 |
| margin | m05-l1, m06-l1 |
| markdown | m09-l1, m09-l2 |
| markup | m09-l1, m09-l2 |
| nothing | m08-l2, m18-l1 |
| notional | m04-l1, m07-l1 |
| order book | m02-l1, m24-l1 |
| Phase A | m09-l1, m09-l2 |
| Phase B | m09-l1, m09-l2 |
| Phase C | m09-l1, m09-l2 |
| Scalping | m23-l1, m26-l1 |
| slippage | m02-l1, m31-l1 |
| stop | m22-l1, m24-l1 |
| stop-hunt | m08-l2, m09-l1 |
| sweep | m19-l2, m34-l1 |
| swing high | m03-l2, m13-l1 |
| swing low | m03-l2, m13-l1 |
| Swing trading | m23-l1, m26-l1 |
| test | m09-l2, m30-l1 |
| three times | m03-l1, m14-l1 |
| time | m23-l2, m33-l1 |
| timeframe | m03-l1, m23-l1 |
| upthrust | m09-l1, m09-l2 |
| UTAD | m09-l1, m09-l2 |
| What. | m06-l1, m20-l1 |
| why | m03-l1, m03-l2 |
| Why it exists. | m04-l1, m07-l1 |
| Why it happens. | m14-l1, m26-l1 |
| Why they cluster: | m19-l2, m25-l1 |
| zone | m08-l1, m34-l1 |
| "a 50% loss just needs a 50% gain." | m22-l1 |
| "a bounce is due" | m26-l1 |
| "I cannot close" as a real risk. | m21-l2 |
| "I didn't follow the system." | m27-l2 |
| "I just need one good trade to get back to even." | m26-l1 |
| "I'm missing it, I have to get in." | m26-l1 |
| "If the market dropped 10% right this second, what would I lose?" | m22-l2 |
| "let me give it room — the level is basically fine, it'll bounce." | m26-l1 |
| "More trades means more profit." | m23-l1 |
| "not your keys, not your coins." | m02-l1 |
| "reading it perfectly right now." | m26-l1 |
| "rising wedges break down, falling wedges break up." | m15-l2 |
| "sell the news" | m21-l2 |
| "Small cap = cheap" and "low price = cheap". | m20-l1 |
| "The price moved +2%, so my PnL is +2%." | m07-l1 |
| "The system failed." | m27-l2 |
| "trending or ranging, on my timeframe?" | m03-l2 |
| "who is doing the absorbing, and on which side?" | m09-l1 |
| $0.001 | m20-l1 |
| $0.50 | m20-l1 |
| $0.77 | m20-l1 |
| $1 billion | m20-l1 |
| $100 million | m20-l1 |
| $2.76 billion | m20-l1 |
| $240 million | m20-l1 |
| $3 billion | m20-l1 |
| $3.00 | m20-l1 |
| $50 | m20-l1 |
| (a third) → you need | m22-l1 |
| +0.01% | m04-l1 |
| +0.05R | m27-l2 |
| +0.1% | m04-l1 |
| +0.15% | m07-l1 |
| +0.6R | m27-l2 |
| +0.8R | m27-l1 |
| +1 | m22-l2 |
| +1.80% on notional | m07-l1 |
| +100% | m22-l1 |
| +150 | m11-l1 |
| +17 | m11-l1 |
| +2% | m07-l1 |
| +20 | m11-l1 |
| +200 | m29-l1 |
| +2R | m22-l1 |
| +3.0R ≈ +300 USDT | m27-l1 |
| +3.7R ≈ +370 USDT | m27-l1 |
| +300 | m30-l1 |
| +360 | m11-l1 |
| +392 | m11-l1 |
| +393 | m11-l1 |
| +3R | m22-l1 |
| +400 USDT | m07-l1 |
| +410 | m11-l1 |
| +420 | m11-l1 |
| +50 | m11-l1 |
| +60 USDT per trade | m25-l1 |
| +650 | m29-l1 |
| +80 | m11-l1 |
| +800 | m30-l1 |
| +9.0% | m07-l1 |
| , and the arithmetic is completely mechanical: - the 4h | m23-l2 |
| , because the recovery gain is calculated on the smaller base that the loss left behind: - Lose | m22-l1 |
| . | m22-l1 |
| . - Lose | m22-l1 |
| 0 to 100 | m18-l1 |
| 0,618 retracement | m27-l1 |
| 0.01% per 8h | m21-l1 |
| 0.03% per interval | m23-l1 |
| 0.04% per fill | m23-l1 |
| 0.1 BTC | m27-l1 |
| 0.11% of notional just to break even | m07-l1 |
| 0.2 units | m22-l1 |
| 0.3% | m11-l1 |
| 0.3% of your notional every day | m04-l1 |
| 0.382 | m13-l1 |
| 0.4 units | m22-l1 |
| 0.5 does not | m13-l1 |
| 0.5–0.618 golden zone | m13-l1 |
| 0.5–1% | m27-l2 |
| 0.618 | m13-l1 |
| 0.8% | m08-l2 |
| 0.9% | m11-l1 |
| 00:00 to 00:00 UTC | m03-l1 |
| 0–100 | m11-l1 |
| 1 | m25-l1 |
| 1 in 13 | m25-l1 |
| 1 in 60 | m25-l1 |
| 1% risk, 100 USDT, each with its stop placed 10% below entry. | m22-l2 |
| 1,000 | m27-l1 |
| 1,589 | m16-l1 |
| 1,834 | m34-l1 |
| 1,855 | m34-l1 |
| 1,870 | m09-l2 |
| 1,902 | m16-l1 |
| 1,930 | m09-l2 |
| 1,960 | m34-l1 |
| 1,965 | m34-l1 |
| 1-hour | m27-l1 |
| 1. Regional demand — the informative one. | m32-l1 |
| 1. The rules are written down BEFORE you look. | m28-l1 |
| 1. Two touches propose, the third validates. | m15-l1 |
| 1.0 unit | m22-l1 |
| 1.00 | m11-l1 |
| 1.20 | m11-l1 |
| 1.3% slippage | m02-l1 |
| 1.35 | m11-l1 |
| 1.5% | m06-l1 |
| 1.5% premium | m32-l1 |
| 1.50 | m11-l1 |
| 1.60 | m11-l1 |
| 1.9% | m08-l2 |
| 10 | m20-l1 |
| 10 contracts | m24-l1 |
| 10% at the same time | m22-l2 |
| 10,000 | m19-l1 |
| 10,300 | m15-l1 |
| 10,361 | m16-l1 |
| 10,400 | m23-l2 |
| 10,551 | m16-l1 |
| 10,570 | m15-l1 |
| 10,575 | m15-l1 |
| 10,740 | m15-l1 |
| 100 points | m22-l1 |
| 1000 | m28-l1 |
| 100× | m26-l1 |
| 100–200 at a time | m09-l1 |
| 101.8 on the very first bar | m10-l1 |
| 106.3 by bar five | m10-l1 |
| 108 | m03-l2 |
| 10× | m06-l1 |
| 11,270 | m15-l1 |
| 12,272 | m16-l1 |
| 12-EMA has crossed the 26-EMA outright | m11-l1 |
| 120,000 USDT | m21-l1 |
| 13,000 | m19-l1 |
| 14 | m11-l1 |
| 150 | m09-l1 |
| 18 | m12-l1 |
| 180, 292 and 274 USDT | m23-l1 |
| 1–3% | m27-l1 |
| 2 | m25-l1 |
| 2 at 100.0 | m24-l1 |
| 2 billion | m20-l1 |
| 2% | m27-l2 |
| 2,000 contracts | m09-l1 |
| 2,014 | m16-l1 |
| 2,017 to 2,499 | m13-l1 |
| 2,020 | m19-l1 |
| 2,035 | m08-l1 |
| 2,045 | m34-l1 |
| 2,050 down to 1,800 | m09-l2 |
| 2,100 | m34-l1 |
| 2,125 | m14-l1 |
| 2,130 | m08-l1 |
| 2,166 | m08-l1 |
| 2,195 | m14-l1 |
| 2,201 | m13-l1 |
| 2,210 | m09-l2 |
| 2,225 | m08-l1 |
| 2,258 | m13-l1 |
| 2,258 down to 2,201 | m13-l1 |
| 2,300 | m19-l1 |
| 2,315 | m13-l1 |
| 2,670 | m19-l1 |
| 2. Bar by bar, with no scrolling back. | m28-l1 |
| 2. Declare your anchor and keep it. | m15-l1 |
| 2. Transfer friction — the boring one. | m32-l1 |
| 2.026 | m02-l1 |
| 20 | m28-l1 |
| 20 and 50, for swing trading | m10-l1 |
| 20% jump in the float overnight | m20-l1 |
| 20,400 | m07-l1 |
| 200 million | m20-l1 |
| 200 USDT | m27-l1 |
| 20× | m22-l1 |
| 23,500 | m30-l1 |
| 23,900 | m09-l2 |
| 24 hours a day, 7 days a week | m23-l1 |
| 24,400 | m30-l1 |
| 24/7 markets don't reset. | m11-l1 |
| 24/7 markets with no closing bell make the stop-limit fill risk real, not theoretical. | m24-l1 |
| 24/7 means no forced cool-off. | m26-l1 |
| 24/7, no close. | m09-l1 |
| 24/7, no closing bell, no circuit breakers. | m06-l1 |
| 25% | m25-l1 |
| 25,350 | m19-l2 |
| 25,850 | m19-l2 |
| 25,900 | m19-l2 |
| 250 points | m22-l1 |
| 26,220 | m19-l2 |
| 26,780 | m34-l1 |
| 27,100 | m34-l1 |
| 27,320 | m34-l1 |
| 28 | m12-l1 |
| 28,000 | m34-l1 |
| 28,250 | m12-l1 |
| 28,320 | m34-l1 |
| 29,000 | m09-l2 |
| 3 | m25-l1 |
| 3 at 100.5 | m24-l1 |
| 3 USDT/day | m04-l1 |
| 3% gross move | m23-l1 |
| 3,000 | m19-l2 |
| 3,000 USDT of long exposure | m22-l2 |
| 3,450 | m19-l2 |
| 3,700 | m27-l1 |
| 3. A line you redraw every week was never a line. | m15-l1 |
| 3. Every trade logged with m27's discipline. | m28-l1 |
| 3.7R | m27-l1 |
| 30 USDT/day | m04-l1 |
| 30% inflation | m20-l1 |
| 30,590 | m09-l2 |
| 300 | m28-l1 |
| 30× | m22-l1 |
| 30–50% | m27-l1 |
| 310 | m33-l1 |
| 32,600 | m12-l1 |
| 33.3% | m25-l1 |
| 38 | m12-l1 |
| 3R trade | m22-l1 |
| 5 at 101.0 | m24-l1 |
| 5%-ish annual yield, delta-neutral | m21-l1 |
| 50 and 200, on the daily | m10-l1 |
| 50% | m25-l1 |
| 50,000 | m08-l2 |
| 50,050 | m08-l2 |
| 500 points | m22-l1 |
| 500 USDT | m04-l1 |
| 50× | m06-l1 |
| 58,000 | m22-l1 |
| 58,800 | m24-l1 |
| 59,000 | m03-l2 |
| 59,300 | m27-l1 |
| 59,850 | m24-l1 |
| 5R | m26-l1 |
| 60% | m22-l1 |
| 60,400 | m08-l2 |
| 61,000 | m08-l2 |
| 61,200 | m08-l2 |
| 62,000 | m03-l2 |
| 62,300 | m27-l1 |
| 63,000 | m24-l1 |
| 64,000 | m27-l1 |
| 66.7% | m25-l1 |
| 7,750 | m19-l1 |
| 70% | m28-l1 |
| 700 | m22-l1 |
| 75 | m11-l1 |
| 8 USDT | m23-l1 |
| 8% circulating | m20-l1 |
| 8,360 | m23-l2 |
| 8,760 | m23-l2 |
| 85 | m12-l1 |
| 88 — extreme greed | m18-l1 |
| 89 | m03-l2 |
| 9 | m12-l1 |
| 9 and 21, on intraday charts. | m10-l1 |
| 9,290 | m15-l1 |
| 9,314 | m06-l1 |
| 9,460 | m23-l2 |
| 9,500 | m06-l1 |
| 9,510 | m15-l1 |
| 9,550 | m15-l1 |
| 9,700 below it | m22-l1 |
| 9,935 | m15-l1 |
| 9.5% | m06-l1 |
| 90 | m12-l1 |
| 90.4% | m22-l1 |
| 92 | m03-l2 |
| 920 million tokens (92%) | m20-l1 |
| A 24/7 market tests levels repeatedly. | m13-l1 |
| A body closing beyond the line | m15-l2 |
| A break on strong volume | m14-l1 |
| A break on weak volume | m14-l1 |
| a candle's meaning comes overwhelmingly from where it happens. | m08-l2 |
| A caveat worth having now. | m29-l1 |
| A chart has no opinion. It has its frame's opinion. | m23-l2 |
| a coil that has not resolved yet is not a signal. | m15-l2 |
| a constant rate of advance | m15-l1 |
| A floor under the stop's width. | m22-l1 |
| a level is a price, and a price is the same number on every chart. | m23-l2 |
| a little over half | m14-l1 |
| A market order dumped into a thin book. | m24-l1 |
| A premium is not a direction | m19-l1 |
| A protective stop-limit that gaps through, and never fills. | m24-l1 |
| a quiet market is not a safe market. It is a market that has not moved yet. | m16-l1 |
| a single candle | m19-l2 |
| A worked reaction. | m10-l1 |
| about 5.5% a year | m21-l1 |
| above | m22-l1 |
| above 70 = overbought | m11-l1 |
| Above a recent high | m19-l2 |
| above or below the midpoint | m34-l1 |
| absorbing | m14-l1 |
| absorption | m29-l1 |
| Absurd leverage is on the menu. | m05-l1 |
| accelerate out through the line it was heading for | m15-l1 |
| accumulating | m30-l1 |
| Accumulation | m09-l1 |
| accumulation | m09-l1 |
| aggregation averages the noise out and leaves the level standing | m23-l2 |
| Aggregation, not new information. | m23-l2 |
| aggressor | m29-l1 |
| Also computed straight from price and volume. | m18-l1 |
| alt | m18-l1 |
| Alt perps go to bigger extremes. | m19-l1 |
| Alt-books are worse. | m03-l2 |
| Altcoins | m01-l1 |
| an eye that has seen the outcome cannot unsee it. | m28-l1 |
| and open a short | m24-l1 |
| anti-revenge-trading | m27-l1 |
| arrives wearing a reasonable sentence | m26-l1 |
| Ascending triangle | m15-l2 |
| ask for the mechanism. | m35-l1 |
| Asks | m02-l1 |
| asks | m31-l1 |
| Assuming the aggressor is the informed side. | m29-l1 |
| attach | m24-l1 |
| authenticator app | m02-l1 |
| back inside | m08-l1 |
| bands | m03-l2 |
| bar travels | m16-l1 |
| base height projected from the break | m15-l2 |
| bearish | m03-l1 |
| Bearish CVD divergence. | m30-l1 |
| bearish regular | m12-l1 |
| beforehand | m34-l1 |
| Believing "stablecoin" means "guaranteed." | m01-l1 |
| Believing leverage raises expected return. | m05-l1 |
| below 30 = oversold | m11-l1 |
| Below a recent low | m19-l2 |
| beta above 1 | m22-l2 |
| Betting the "alt season" is guaranteed. | m17-l1 |
| beyond | m08-l1 |
| bid-imbalanced | m31-l1 |
| Bids | m02-l1 |
| bids | m31-l1 |
| Bitcoin (BTC) | m01-l1 |
| Bitcoin and the broad market | m18-l1 |
| blockchain | m01-l1 |
| blocks | m01-l1 |
| bodies and wicks of the swings that actually turned | m08-l1 |
| body | m03-l1 |
| Bollinger | m16-l1 |
| Bollinger band | m16-l1 |
| BOS | m34-l1 |
| BOS / CHoCH | m34-l1 |
| both fills | m07-l1 |
| bought | m19-l1 |
| bounded loss | m02-l1 |
| bracket | m24-l1 |
| break of structure (BOS) | m08-l1 |
| break-even win rate | m25-l1 |
| break-even win% = 1 ÷ (1 + payoff) | m25-l1 |
| BTC → ETH → large-cap alts → small-cap alts. | m17-l1 |
| Build. | m19-l2 |
| bullish | m03-l1 |
| Bullish CVD divergence. | m30-l1 |
| bullish regular | m12-l1 |
| business | m21-l1 |
| But far more volatility, so fast MAs are noisier. | m10-l1 |
| buy | m19-l2 |
| Buy the spot. | m21-l1 |
| Buying right before a cliff. | m20-l1 |
| by price level | m33-l1 |
| C | m03-l1 |
| calendar | m21-l2 |
| Calling a reversal on one change of character. | m08-l1 |
| calm, flat self being overruled | m26-l1 |
| candlesticks | m03-l1 |
| Cap the cluster, not just the line. | m22-l2 |
| Capital already has to be in place. | m32-l1 |
| Capital controls and banking limits. | m32-l1 |
| Capital is not free. | m21-l1 |
| capitulation | m18-l1 |
| Cascade. | m19-l2 |
| cash leg | m01-l1 |
| centralised exchange (CEX) | m02-l1 |
| change of character (CHoCH) | m08-l1 |
| channel | m15-l1 |
| Chasing the first candle past a level. | m08-l1 |
| chasing the squeeze after it is spent. | m19-l2 |
| CHoCH | m34-l1 |
| Choking the winner. | m27-l1 |
| Circulating supply | m20-l1 |
| circulating, total and max supply | m20-l1 |
| closed before the day is out | m23-l1 |
| closes scatter | m16-l1 |
| Coinbase premium | m32-l1 |
| collapsing | m32-l1 |
| compressed time | m25-l1 |
| compresses itself | m21-l1 |
| compression | m08-l2 |
| Compression says an expansion is coming. It does not say which way. | m16-l1 |
| Computed entirely from the price series. | m18-l1 |
| confirms | m34-l1 |
| confirms a change that is already underway | m10-l1 |
| Confusing leverage with position size. | m22-l1 |
| Context above, trigger below. Never the reverse. | m23-l2 |
| contract | m04-l1 |
| contrarian zone | m18-l1 |
| control of the exit | m22-l1 |
| convention, not a promise. | m15-l2 |
| conventions, not results. | m10-l1 |
| Correlation | m22-l2 |
| cost, not a strategy | m23-l1 |
| Count independent bets, not tickers. | m22-l2 |
| credible scarcity | m01-l1 |
| credit exposure to an issuer | m01-l1 |
| Cross margin quietly staking the whole account. | m05-l1 |
| Cross margin turns one mistake into an account-wide event. | m06-l1 |
| Crowded leverage adds fuel. | m03-l2 |
| crowded short | m19-l2 |
| crowding | m31-l1 |
| Crypto nuance: | m07-l1 |
| crypto runs 24/7 | m18-l1 |
| crypto-native | m04-l1 |
| Crypto-native events | m17-l1 |
| CVD | m30-l1 |
| daily | m27-l1 |
| daily loss limit | m26-l1 |
| dated future | m23-l1 |
| day trader | m23-l1 |
| Day trader | m23-l2 |
| Day trader — 1 round-trip, no funding. | m23-l1 |
| Day trading. | m23-l1 |
| days to weeks | m23-l1 |
| dead | m27-l1 |
| death cross | m10-l1 |
| decentralised exchange (DEX) | m02-l1 |
| decided worst in the moment and best in advance | m26-l1 |
| delta | m29-l1 |
| delta-neutral | m21-l1 |
| Delta-neutral is not margin-neutral. | m21-l1 |
| demand for a real use | m01-l1 |
| depth | m02-l1 |
| Depth | m31-l1 |
| Descending triangle | m15-l2 |
| Diagonal: | m15-l1 |
| difference | m04-l1 |
| different clocks | m23-l1 |
| diluting your average | m25-l1 |
| directional exposure | m22-l2 |
| directly between longs and shorts | m04-l1 |
| discount | m34-l1 |
| distance | m22-l1 |
| distribution | m09-l1 |
| distribution is the same story upside down | m09-l2 |
| Do nothing — most of the time. | m27-l1 |
| does | m35-l1 |
| doing almost nothing | m27-l1 |
| DOM | m31-l1 |
| Dominance rose from 50% to 56% while Bitcoin's own price fell 10%. | m17-l1 |
| double-counting | m18-l1 |
| downside is not bounded by the same design | m21-l1 |
| dozens or hundreds of trades a day | m23-l1 |
| eleven times | m20-l1 |
| emission schedule | m20-l1 |
| emission/inflation rate | m20-l1 |
| Emissions are a constant background sell. | m20-l1 |
| ends | m34-l1 |
| Engulfing | m08-l2 |
| Enough trades before judging. | m27-l2 |
| equal | m11-l1 |
| ETH/BTC ratio | m17-l1 |
| Euphoria | m18-l1 |
| every eight hours | m04-l1 |
| Every parameter you add is one more degree of freedom for the past to agree with you. | m28-l1 |
| Example: | m09-l2 |
| Exchange (custodial) custody: | m02-l1 |
| Execution vs plan | m27-l2 |
| Exhaustion. | m19-l2 |
| expansion | m16-l1 |
| expectancy | m25-l1 |
| expectancy = win% × average win − loss% × average loss | m25-l1 |
| expiry dates are scheduled bursts of mechanical flow in the perpetual | m21-l2 |
| exponential moving average (EMA) | m10-l1 |
| extensions | m13-l1 |
| extreme | m19-l1 |
| extreme fear | m18-l1 |
| extreme greed | m18-l1 |
| Extreme leverage. | m19-l2 |
| Extremes can persist for weeks or months. | m18-l1 |
| fading exhaustion | m19-l2 |
| fair value | m04-l1 |
| Fair value gap / imbalance | m34-l1 |
| fakeout | m08-l1 |
| Falling dominance | m17-l1 |
| falling ETH/BTC | m17-l1 |
| Falling wedge | m15-l2 |
| false break | m09-l1 |
| fast | m10-l1 |
| Fear & Greed index | m18-l1 |
| fee | m23-l1 |
| Fees (taker on both sides): | m07-l1 |
| fees and funding | m25-l1 |
| Fees at every step. | m32-l1 |
| Fees track the number of trades. | m23-l1 |
| Fibonacci retracements | m13-l1 |
| Finding a divergence on every chart. | m30-l1 |
| Fit on the first half. | m28-l1 |
| five days of paying wipes out five sixths of a month of collecting | m21-l1 |
| five times | m14-l1 |
| fix the criterion before you start. | m28-l1 |
| fixed small fraction of your account | m22-l1 |
| FOMO | m26-l1 |
| footprint | m33-l1 |
| Footprint | m33-l1 |
| footprint of order flow | m08-l2 |
| for as long as your coins sit on an exchange, the exchange is holding them for you. | m02-l1 |
| for its job | m23-l2 |
| force-closing | m05-l1 |
| forcibly closing | m19-l2 |
| Forcing the story. | m09-l1 |
| forward | m28-l1 |
| four to six times apart | m23-l2 |
| Fractional sizing | m35-l1 |
| from | m22-l1 |
| front-run | m20-l1 |
| full-time job | m23-l1 |
| Fully-diluted valuation (FDV) = price × max supply. | m20-l1 |
| Funding and leverage cluster the stops. | m09-l1 |
| Funding bleed on a long hold. | m07-l1 |
| Funding is a crypto-native mechanism. | m19-l1 |
| Funding is a positioning gauge, not an entry signal. | m19-l1 |
| funding is positive, and positive funding means longs pay shorts | m21-l1 |
| Funding is the more honest exhaustion clue. | m11-l1 |
| Funding only exists on perpetuals. | m23-l1 |
| Funding tracks the time you hold. | m23-l1 |
| Funding: | m07-l1 |
| gap | m17-l1 |
| gap between them is your breathing room | m05-l1 |
| Gap risk, 24/7. | m22-l1 |
| genuine breakout | m08-l1 |
| golden cross | m10-l1 |
| Grading setups presupposes that you can grade | m27-l2 |
| Gross PnL: | m07-l1 |
| H | m03-l1 |
| half | m03-l1 |
| half the score | m18-l1 |
| Hammer / pin bar | m08-l2 |
| Harami | m08-l2 |
| hidden divergence | m12-l1 |
| High leverage makes a single tilt fatal. | m26-l1 |
| higher | m03-l1 |
| higher highs (HH) | m08-l1 |
| higher highs and higher lows | m03-l2 |
| higher lows | m09-l2 |
| higher lows (HL) | m08-l1 |
| higher volume | m08-l1 |
| higher win rate just to break even | m23-l1 |
| Hindsight bias. | m09-l2 |
| Hindsight labeling. | m09-l1 |
| histogram | m11-l1 |
| histogram for shifts in momentum | m11-l1 |
| holding period | m23-l1 |
| holds | m08-l1 |
| Horizontal (m03-l2): | m15-l1 |
| How close your liquidation sits. | m05-l1 |
| how long they hold | m23-l1 |
| how much noise surrounds it | m23-l2 |
| how often they trade | m23-l1 |
| how price reacts there | m27-l1 |
| how the convergence is shared | m15-l2 |
| hundreds of candles | m03-l1 |
| iceberg | m31-l1 |
| identical | m08-l2 |
| If you cannot name the mechanic, there is no trade. | m34-l1 |
| Ignoring the currency leg. | m32-l1 |
| Ignoring the round trip. | m07-l1 |
| immediacy | m24-l1 |
| immediacy vs price | m24-l1 |
| Improvising an exit. | m27-l1 |
| impulse leg | m13-l1 |
| impulsive or easily bored | m23-l1 |
| In a downtrend: | m13-l1 |
| In a drawdown, crypto correlations snap toward +1: | m22-l2 |
| In a market with no rhythm. | m15-l1 |
| In a strong trend, an oscillator can stay pinned at its extreme for a very long time. | m11-l1 |
| In an uptrend: | m13-l1 |
| in isolation | m19-l1 |
| In practice: | m06-l1 |
| in R | m27-l1 |
| in the plan, before the losing day | m27-l1 |
| In the short run, a valid system having a bad run is indistinguishable from a broken system. | m28-l1 |
| independent | m22-l2 |
| inference | m34-l1 |
| inflation | m20-l1 |
| Initial margin | m05-l1 |
| initial margin rate | m06-l1 |
| inside a single bar | m34-l1 |
| instantaneous snapshot | m31-l1 |
| inter-venue premium | m34-l1 |
| Interest rates. | m17-l1 |
| invalidated by a scheduled unlock | m20-l1 |
| inverse contract | m05-l1 |
| it is another profession. | m35-l1 |
| It is even less information than usual. | m15-l1 |
| it is not a system, it is a description | m28-l1 |
| It is per-venue. | m30-l1 |
| It reacts to macro prints in real time — including when nothing else can. | m17-l1 |
| it trades 24 hours a day, 7 days a week | m17-l1 |
| journal | m27-l2 |
| Judging the system from a handful of trades. | m27-l2 |
| just to get back to even. - Lose | m22-l1 |
| Keltner | m16-l1 |
| Keltner channel | m16-l1 |
| Know which session you actually trade. | m23-l1 |
| L | m03-l1 |
| large unlock | m20-l1 |
| Last price | m04-l1 |
| Leaving everything on the exchange. | m02-l1 |
| lens for reading that shape | m09-l1 |
| leverage-mania thermometer | m19-l1 |
| liability on the exchange's books | m02-l1 |
| limit | m24-l1 |
| limit buy at 2.00 | m02-l1 |
| Limit order | m02-l1 |
| limit order | m24-l1 |
| linear | m05-l1 |
| liquidation cascade | m06-l1 |
| Liquidation cascades. | m05-l1 |
| liquidation must never be your effective stop. | m22-l1 |
| liquidation prices of leveraged longs | m19-l2 |
| liquidation prices of leveraged shorts | m19-l2 |
| liquidity | m24-l1 |
| Liquidity grab / sweep | m34-l1 |
| Liquidity squeeze / short squeeze | m16-l1 |
| liquidity void | m34-l1 |
| local exhaustion | m19-l1 |
| London, roughly 07:00–16:00 UTC | m23-l1 |
| Long | m04-l1 |
| long 1 BTC at 20,000 | m07-l1 |
| Long squeeze: | m19-l2 |
| long stop-losses | m19-l2 |
| long wick | m03-l1 |
| Long: | m06-l1 |
| longs pay shorts. | m19-l1 |
| Look-ahead | m28-l1 |
| losing streak | m28-l1 |
| low-volume node | m33-l1 |
| lower highs (LH) | m08-l1 |
| lower highs and lower lows | m03-l2 |
| lower lows (LL) | m08-l1 |
| lower-timeframe noise | m03-l1 |
| m02. | m21-l2 |
| m06. | m21-l2 |
| m09 | m34-l1 |
| m11 | m16-l1 |
| m20 | m21-l2 |
| m21-l2 | m35-l1 |
| m25 | m28-l1 |
| m25-l1 | m22-l1 |
| m28 | m35-l1 |
| m30 — CVD. | m29-l1 |
| m31 — the order book. | m29-l1 |
| m32 — premium between venues. | m29-l1 |
| m33 | m34-l1 |
| m33 — footprint charts and volume profile. | m29-l1 |
| m34 | m35-l1 |
| m34-l1 | m08-l1 |
| MACD | m11-l1 |
| MACD line | m11-l1 |
| MACD-histogram divergence | m11-l1 |
| Macro frame → bias and levels. | m27-l1 |
| Macro releases | m17-l1 |
| Maintenance margin | m05-l1 |
| maintenance margin | m06-l1 |
| maintenance margin rate | m06-l1 |
| map | m09-l1 |
| mark | m04-l1 |
| Mark price | m04-l1 |
| mark price | m04-l1 |
| Markdown | m09-l1 |
| market | m24-l1 |
| market buy for 2,000 units | m02-l1 |
| market cap | m01-l1 |
| Market cap = price × circulating supply. | m20-l1 |
| market cap and FDV | m20-l1 |
| Market momentum and volume (~25%) | m18-l1 |
| Market order | m02-l1 |
| market order | m24-l1 |
| Markup | m09-l1 |
| Mass sentiment | m18-l1 |
| Max supply | m20-l1 |
| measured deviation from expectancy | m28-l1 |
| Measured microstructure | m35-l1 |
| memory | m03-l2 |
| Micro frame → trigger and stop. | m27-l1 |
| mid-trade improvisation | m27-l1 |
| minutes to hours | m23-l1 |
| Mistaking "market cap" for real money. | m01-l1 |
| Mistaking market cap for FDV. | m20-l1 |
| Modelled transaction costs | m35-l1 |
| Money lost at the stop | m22-l1 |
| more participants for longer | m23-l2 |
| more resting orders | m23-l2 |
| more tactics | m35-l1 |
| Morning star / evening star | m08-l2 |
| Move the stop to break-even — against a test, not a feeling. | m27-l1 |
| moving average (MA) | m10-l1 |
| moving floor in an uptrend or a ceiling in a downtrend | m10-l1 |
| Moving or widening the stop once you are in. | m22-l1 |
| narrative | m01-l1 |
| negative | m19-l2 |
| Negative funding bills you | m21-l1 |
| Negative funding rate → shorts pay longs. | m04-l1 |
| Negative funding: | m19-l1 |
| neighbouring | m34-l1 |
| Net = +2R | m22-l1 |
| net realized PnL | m07-l1 |
| net result | m07-l1 |
| Net: `300 − 120 = 180 USDT`. | m23-l1 |
| Net: `300 − 8 = 292 USDT`. | m23-l1 |
| Net: `300 − 8 − 18 = 274 USDT`. | m23-l1 |
| network effects | m01-l1 |
| never | m27-l1 |
| never closes | m04-l1 |
| Never go back up to justify the trade. | m23-l2 |
| never read OI without price | m19-l1 |
| Never scale to win it back. | m27-l2 |
| new low with it | m30-l1 |
| New York, roughly 13:00–21:00 UTC. | m23-l1 |
| No central operator. | m01-l1 |
| No close, thin weekends. | m05-l1 |
| no expiry date | m04-l1 |
| No gaps, one continuous series. | m10-l1 |
| No journal, so every loss is ambiguous. | m27-l2 |
| no mechanism | m13-l1 |
| No session boundaries. | m14-l1 |
| Nobody can arbitrage an infinite amount. | m21-l1 |
| nobody is obliged to maintain it | m15-l1 |
| noise | m03-l1 |
| none | m09-l1 |
| None of this predicts direction. All of it predicts conditions. | m21-l2 |
| Not every perpetual is settled in a stablecoin. | m05-l1 |
| Not every unlocked token is sold. | m21-l2 |
| nothing the price panel above it does not already contain. | m16-l1 |
| Notional | m22-l1 |
| notional = 100 ÷ 0.10 = 1,000 USDT per position. | m22-l2 |
| notional value | m05-l1 |
| notional × the funding rate | m04-l1 |
| O | m03-l1 |
| observed | m28-l1 |
| often | m34-l1 |
| OI tells you whether a move is backed by new positions or just by people unwinding old ones. | m19-l1 |
| On-chain settlement is final. | m02-l1 |
| one | m22-l1 |
| one candle | m03-l1 |
| one green candle | m23-l2 |
| one pullback candle inside a downtrend | m23-l2 |
| One time in four, a fair coin gives you twelve wins or more — a 60% win rate. | m28-l1 |
| One word, two mechanisms. | m19-l2 |
| one ~3% bet in three costumes. | m22-l2 |
| open | m03-l1 |
| Open interest (OI) | m19-l1 |
| Open the higher frame first. | m23-l2 |
| opens at 100, runs up to 108, falls to 96, and closes at 101 | m03-l1 |
| opens at 108 and closes at 101 with no lower wick | m03-l1 |
| options | m35-l1 |
| Options expiries. | m21-l2 |
| or higher | m24-l1 |
| Order | m10-l1 |
| order | m24-l1 |
| order block | m34-l1 |
| Order block | m34-l1 |
| order book heatmap | m31-l1 |
| Order flow | m29-l1 |
| origin zone | m34-l1 |
| oscillator | m11-l1 |
| Outages under load. | m21-l2 |
| outside | m19-l2 |
| Over-leverage puts your liquidation price inside normal noise. | m06-l1 |
| Over-scoped API keys. | m02-l1 |
| overfitting | m28-l1 |
| overlap, about 13:00–16:00 UTC | m23-l1 |
| overnight risk wrecks your sleep | m23-l1 |
| overrun | m08-l2 |
| Oversizing "just this once." | m22-l1 |
| Paper or minimum size first. | m27-l2 |
| parabolic | m12-l1 |
| parallel | m15-l1 |
| Partial take-profits — a style choice, honestly priced. | m27-l1 |
| participation | m03-l1 |
| Participation behind it | m15-l2 |
| Participation has to be behind it | m15-l1 |
| patience | m23-l1 |
| pattern | m15-l2 |
| pay | m04-l1 |
| Payoff | m25-l1 |
| per fill | m23-l1 |
| Perp above spot: a premium. | m19-l1 |
| Perp below spot: a discount. | m19-l1 |
| perpetual future | m04-l1 |
| perpetual futures | m23-l1 |
| Perps and spot tell different stories. | m30-l1 |
| Phase D | m09-l1 |
| phase D | m09-l2 |
| Phase E | m09-l1 |
| phase E | m09-l2 |
| phases A–E | m09-l1 |
| Picking a style that fights your schedule. | m23-l1 |
| POC | m33-l1 |
| pool of opposite orders | m19-l2 |
| Portfolio risk | m22-l1 |
| Portfolio risk is your total exposure to a single market move, no matter how many separate positions you have split it across. | m22-l2 |
| Position size | m22-l1 |
| Position size = risk budget ÷ stop distance. | m22-l1 |
| positioning and flow | m32-l1 |
| positions, against the margin in their own account | m21-l1 |
| Positive funding rate → longs pay shorts. | m04-l1 |
| Positive funding: | m19-l1 |
| pre-commitment | m26-l1 |
| pre-session | m23-l1 |
| premium | m34-l1 |
| Premium / discount | m34-l1 |
| premium between venues | m32-l1 |
| Price above a rising fast MA, fast above slow = uptrend; the mirror = downtrend. | m10-l1 |
| price control | m24-l1 |
| Price down, OI down | m19-l1 |
| Price down, OI up | m19-l1 |
| Price position. | m10-l1 |
| Price up, OI down | m19-l1 |
| Price up, OI up | m19-l1 |
| prior swing high | m27-l1 |
| prior trend | m09-l1 |
| private key | m01-l1 |
| protective | m24-l1 |
| pull their quotes | m31-l1 |
| pullback | m08-l1 |
| Quarterly futures. | m21-l2 |
| R | m22-l1 |
| R-multiples | m25-l1 |
| ranges | m09-l1 |
| Ranges break both ways for real. | m09-l2 |
| Ranges persist and levels carry across "days." | m03-l2 |
| ranging | m03-l1 |
| rate-of-change | m12-l1 |
| Re-reading. | m35-l1 |
| Read the sequence forwards, never backwards. | m34-l1 |
| read-only | m02-l1 |
| Reading a premium as a buy signal. | m32-l1 |
| Reading rising CVD as "price will rise." | m30-l1 |
| Reading volume in isolation. | m14-l1 |
| reduce-only | m24-l1 |
| Reduce-only is a perpetuals-specific safeguard. | m24-l1 |
| Regime classification | m35-l1 |
| regular divergence | m12-l1 |
| regular divergence compares the extremes and expects a turn; hidden divergence appears on the retracement and expects the trend to resume. | m12-l1 |
| rejection | m08-l2 |
| resistance around 29,640 | m09-l2 |
| retest and hold | m08-l1 |
| revenge | m26-l1 |
| rhythm can give out through the line it was built on | m15-l1 |
| rising 50-EMA | m27-l1 |
| Rising dominance | m17-l1 |
| rising ETH/BTC | m17-l1 |
| rising OI means fresh positions are being opened; falling OI means existing positions are being closed. | m19-l1 |
| Rising wedge | m15-l2 |
| risk budget | m22-l1 |
| Risk hears none of this. | m34-l1 |
| risk only diversifies away when correlation is below +1. | m22-l2 |
| risk-off | m17-l1 |
| Risk-off: | m17-l1 |
| risk-on asset | m17-l1 |
| Risk-on: | m17-l1 |
| Role reversal (the flip). | m03-l2 |
| round number | m13-l1 |
| Round numbers and fibs cluster. | m13-l1 |
| RS | m11-l1 |
| RS = average gain ÷ average loss | m11-l1 |
| RSI | m11-l1 |
| same candle | m29-l1 |
| sample | m25-l1 |
| Scale only after the journal proves it. | m27-l2 |
| scales with the number of trades, not with the size of the move | m23-l1 |
| scales with time held | m23-l1 |
| Scaling to recover. | m27-l2 |
| Scalper | m23-l2 |
| Scalper — 15 round-trips, no funding. | m23-l1 |
| Scalping. | m23-l1 |
| scheduled | m17-l1 |
| scheduled by the clock | m23-l1 |
| Scheduled maintenance. | m21-l2 |
| scheduled, public supply arriving in a book | m21-l2 |
| Scoped API keys. | m02-l1 |
| Screen time. | m35-l1 |
| screenshot | m27-l2 |
| Search trends | m18-l1 |
| second half, which you never looked at. | m28-l1 |
| seconds to a few minutes | m23-l1 |
| Self-custody: | m02-l1 |
| sell | m19-l2 |
| Settlement is final. | m01-l1 |
| shape | m30-l1 |
| Shooting star | m08-l2 |
| Short | m04-l1 |
| short | m04-l1 |
| short covering | m19-l1 |
| short squeeze | m09-l1 |
| Short squeeze: | m19-l2 |
| short stop-losses | m19-l2 |
| Short the perpetual. | m21-l1 |
| Short: | m06-l1 |
| shorting a strong trend because it "has to be exhausted." | m12-l1 |
| shorts pay longs | m19-l1 |
| Signal cross: | m11-l1 |
| signal line | m11-l1 |
| signal-line cross | m11-l1 |
| signed histogram | m16-l1 |
| simple moving average (SMA) | m10-l1 |
| single accumulation range from start to finish | m09-l2 |
| single trade on its own | m22-l1 |
| Size it against the book, not against the market cap. | m21-l2 |
| sizing for the reward instead of the stop | m22-l1 |
| skipped trade | m27-l1 |
| Slippage | m24-l1 |
| Slope. | m10-l1 |
| slow | m10-l1 |
| slow-motion | m26-l1 |
| SMA50 effectively reports a price about 25 bars old | m10-l1 |
| small slice of its supply circulating | m20-l1 |
| smart money | m34-l1 |
| SMS 2FA and the SIM-swap. | m02-l1 |
| Social FOMO is engineered. | m26-l1 |
| Social media (~15%) | m18-l1 |
| socially driven | m18-l1 |
| span crossed inside a single candle | m34-l1 |
| spent | m34-l1 |
| Spoofing | m31-l1 |
| Spot | m02-l1 |
| spot | m23-l1 |
| spread across a band of prices | m03-l2 |
| square root | m28-l1 |
| squeeze | m19-l2 |
| Stablecoins | m01-l1 |
| stages | m09-l1 |
| standard deviations | m16-l1 |
| Start where losing feels like nothing. | m27-l2 |
| Statistical arbitrage | m35-l1 |
| statistics without a mechanism | m15-l2 |
| stay where you are and do it more times. | m35-l1 |
| stop and your position size have to do the watching for you | m23-l1 |
| stop belongs to the frame you entered on | m23-l2 |
| stop-hunt wick | m09-l2 |
| Stop-hunt wicks. | m08-l1 |
| stop-limit | m24-l1 |
| stop-loss (SL) | m24-l1 |
| stop-market | m24-l1 |
| Stress-test the book. | m22-l2 |
| strong trend | m12-l1 |
| summary | m29-l1 |
| sunk-cost trap | m26-l1 |
| supply shock the chart cannot show | m20-l1 |
| support around 28,140 | m09-l2 |
| Survivorship | m28-l1 |
| swing trader | m23-l1 |
| Swing trader | m23-l2 |
| Swing trader — 1 round-trip, 6 funding intervals. | m23-l1 |
| Swing trading. | m23-l1 |
| Symmetric triangle | m15-l2 |
| take-profit (TP) | m24-l1 |
| taker buy volume | m29-l1 |
| taker fee | m07-l1 |
| taker was the buyer | m29-l1 |
| tell you can feel | m26-l1 |
| tendency, not a timetable | m17-l1 |
| test the claim before you pay to find out. | m28-l1 |
| Testing cuts both ways. | m03-l2 |
| That number was an assumption. | m28-l1 |
| The Asian session, roughly 00:00–08:00 UTC | m23-l1 |
| The basis re-anchors | m21-l2 |
| The body decides, not the wick | m15-l1 |
| the break comes first. | m34-l1 |
| The break follows the same discipline as everything else in this block: | m15-l2 |
| The calendar is exact and everyone has it. | m20-l1 |
| the carry's yield is a leverage-mania thermometer | m21-l1 |
| The channel describes a regularity that has held. Trading it assumes the regularity persists, and that assumption is the bet. | m15-l1 |
| The clock: usually every 8 hours. | m19-l1 |
| The collateral you post. | m22-l1 |
| The costs of actually trading. | m28-l1 |
| The course has not given you experience | m35-l1 |
| The default stays the default. | m27-l2 |
| the diagonal is the weakest instrument in this course. | m15-l1 |
| The doji. | m08-l2 |
| the EMA reacts faster (less lag), but that speed also makes it noisier | m10-l1 |
| the exchange itself. | m21-l2 |
| the floor of the range stops being touched. | m09-l2 |
| The frequency dimension. | m22-l1 |
| the gap widens exactly when the crowd is maddest. | m21-l1 |
| the ground is crowded: size down, tighten risk, stop chasing. | m18-l1 |
| The higher frame sets the context. The lower frame sets the execution. | m23-l2 |
| the higher timeframe dictates the bias, the lower timeframe dictates the entry | m27-l1 |
| the histogram reaching zero and the cross happening are the same event. | m11-l1 |
| The honest limits of demo. | m27-l2 |
| The honest rule of thumb: dozens say nothing, hundreds begin to speak. | m28-l1 |
| The journal, growing. | m35-l1 |
| the last opposing candles before it | m34-l1 |
| the MACD line crossed above its signal precisely because the MACD line turned up | m11-l1 |
| The market runs 24/7. | m02-l1 |
| the mechanism of whoever is selling it to you. | m35-l1 |
| The numbers. | m21-l1 |
| The one inviolable rule: the stop only ever moves in the trade's favour. | m27-l1 |
| The part with a mechanism. | m15-l2 |
| The part without one. | m15-l2 |
| the perpetual's price minus the spot price | m19-l1 |
| The plan | m27-l2 |
| the release of the positioned | m21-l2 |
| The result in R | m27-l2 |
| The reversal, when it comes, is violent. | m11-l1 |
| The rule: | m26-l1 |
| The same bullish signal-line cross inside a range | m11-l1 |
| The same bullish signal-line cross inside an established uptrend | m11-l1 |
| the same price series, candle for candle, to the end of the shared leg | m19-l1 |
| The setup | m27-l2 |
| the size came from the stop, so the leverage cannot change it. | m22-l1 |
| The small-range candle. | m08-l2 |
| The stop defines the risk; the risk defines the size. | m22-l1 |
| The stop moves to break-even only once the trade has produced new confirmation in its favour on the execution timeframe | m27-l1 |
| The tendency promoted to a law. | m34-l1 |
| the tone of the recent past | m18-l1 |
| The trader. | m28-l1 |
| The two legs need to sit somewhere. | m21-l1 |
| The US dollar index (DXY). | m17-l1 |
| The weekend range and the Monday sweep. | m23-l1 |
| The width is a read of realized volatility | m16-l1 |
| The zone drawn in hindsight. | m34-l1 |
| Then drop to the lower frame | m23-l2 |
| there aren't 60 patterns, there are two mechanics wearing 60 names. | m08-l2 |
| there is no new system, there are three mechanics with more names. | m34-l1 |
| There is no open or close ritual. | m03-l1 |
| They add confluence. | m13-l1 |
| They are self-fulfilling. | m13-l1 |
| they are the same chart | m14-l1 |
| thin alt books | m12-l1 |
| Thin alt books make springs cheap. | m09-l1 |
| Thin alt books pin the extreme longer. | m11-l1 |
| Thin alt books swallow badly. | m20-l1 |
| Thin alt books turn ordinary orders into their own worst enemy. | m24-l1 |
| Thin alt-books amplify every cascade. | m06-l1 |
| thin alt-coin book | m09-l2 |
| Thin books produce false breaks. | m03-l2 |
| Thin books, especially weekends and alts. | m19-l2 |
| Thin weekend volume. | m14-l1 |
| thin-margin business with fat tails | m21-l1 |
| This course anchors on closes | m15-l1 |
| this dialect is worth understanding because the crowd speaks it | m34-l1 |
| This is the disambiguation to get right, because the collision is total and the two mechanisms have nothing to do with each other. | m16-l1 |
| This is the one to burn into memory, and it is where m06, liquidation, comes back. | m21-l1 |
| three | m22-l2 |
| Tiering risk on ungraded confidence. | m27-l2 |
| tight stop allows a larger one — for the same risk | m22-l1 |
| time series | m33-l1 |
| Timeframe boundaries are arbitrary. | m03-l1 |
| Timeframe changes the reading. | m30-l1 |
| Timeframe shopping. | m23-l2 |
| Tokenomics | m20-l1 |
| tools with known mechanics | m01-l1 |
| Total supply | m20-l1 |
| Total: −300 USDT = 3% of the account, from a single move. | m22-l2 |
| trade count | m23-l1 |
| trading a divergence in open space | m12-l1 |
| Trading dominance as if it were direction. | m17-l1 |
| Trading it without a level or a stop. | m30-l1 |
| Trading real size on an unvalidated system. | m27-l2 |
| Trading the lower frame against the higher one is trading the noise against the signal that > contains it. | m23-l2 |
| Transfer time. | m32-l1 |
| Treat the zone as a zone. | m34-l1 |
| Treating crypto as a safe haven. | m17-l1 |
| Treating delta as a direction signal. | m29-l1 |
| trend | m03-l2 |
| trending | m03-l1 |
| trendline | m15-l1 |
| trigger | m24-l1 |
| Trigger. | m19-l2 |
| Trusting a cross-venue number as if it were exact. | m29-l1 |
| Trusting a low-volume breakout. | m14-l1 |
| Trying to arbitrage it as a beginner. | m32-l1 |
| Tweezers | m08-l2 |
| twice | m07-l1 |
| two and a half days of normal volume | m20-l1 |
| two breaks of the ladder | m34-l1 |
| two clear swings of the same kind | m30-l1 |
| two different exchanges | m32-l1 |
| Two frames, three at the outside. | m23-l2 |
| Two-factor authentication (2FA). | m02-l1 |
| un-mark | m35-l1 |
| unbounded | m24-l1 |
| under those same two points | m12-l1 |
| unlock | m17-l1 |
| unlock calendar | m20-l1 |
| unrealized | m07-l1 |
| unsecured creditors | m02-l1 |
| upside is bounded | m21-l1 |
| USDC | m01-l1 |
| UST | m01-l1 |
| value area | m33-l1 |
| variance | m25-l1 |
| vesting schedule | m21-l2 |
| Volatility (~25%) | m18-l1 |
| volatility and likely sweeps | m19-l2 |
| Volatility and momentum are both derived from price itself | m18-l1 |
| volatility clusters. | m16-l1 |
| Volatility plus leverage makes oversizing lethal. | m22-l1 |
| Volatility squeeze | m16-l1 |
| volatility squeeze | m19-l2 |
| volume profile | m33-l1 |
| Volume profile | m33-l1 |
| wait for the close, and check whether anyone came with it. | m15-l1 |
| wait for the close, and for that close to hold. | m08-l1 |
| waiting | m31-l1 |
| Walk-forward validation | m35-l1 |
| wall | m31-l1 |
| warning that participation is thinning | m14-l1 |
| wash trading | m14-l1 |
| Wash-trading noise. | m14-l1 |
| Watch what open interest does around it. | m21-l2 |
| Weekend and thin-book fakeouts. | m08-l1 |
| Weekend drift. | m17-l1 |
| Weekend volume is thin. | m03-l1 |
| Weekend wicks. | m06-l1 |
| weekends are thinner still | m23-l1 |
| weekly review | m27-l2 |
| Weigh a MACD cross by which line was crossed and by the regime it happened in. | m11-l1 |
| Weight a signal by the session it printed in. | m23-l1 |
| What actually changes: | m22-l1 |
| What earning the tiers looks like. | m27-l2 |
| What happens on the day? | m21-l2 |
| What is identical at 5× and at 20×: | m22-l1 |
| What is known gets anticipated | m21-l2 |
| what it is | m26-l1 |
| what it looks like with real numbers | m26-l1 |
| What it looks like. | m14-l1 |
| What there is, is a mechanism: | m23-l2 |
| What they are. | m07-l1 |
| What you see that a candle hides. | m33-l1 |
| What: | m09-l2 |
| When the basis snaps: an exhaustion tell. | m19-l1 |
| When the Bollinger band sits entirely inside the Keltner channel, the market is in a squeeze. | m16-l1 |
| When the thesis came first. | m15-l1 |
| when volume spikes | m21-l2 |
| Where it actually breaks. | m22-l1 |
| Where liquidation sits relative to your stop. | m22-l1 |
| while the zone is crowded | m34-l1 |
| whipsaw | m10-l1 |
| Who bought before? | m21-l2 |
| Who do they sell to? | m21-l2 |
| who holds what | m21-l2 |
| Why a mechanical rule instead of judgement: | m27-l1 |
| Why confluence and not a single line: | m27-l1 |
| Why here: | m09-l1 |
| Why it can exist at all. | m32-l1 |
| Why it earns a look of its own. | m19-l1 |
| Why it feeds on itself. | m06-l1 |
| why it happens | m26-l1 |
| Why it is a different kind of data. | m31-l1 |
| Why it is a different shape of data. | m33-l1 |
| Why it is a headwind. | m20-l1 |
| Why it is a shock, with numbers. | m20-l1 |
| Why it is fragile. | m31-l1 |
| Why it is not volume. | m29-l1 |
| Why it leads price. | m14-l1 |
| Why it leads. | m30-l1 |
| Why it marks opportunity. | m18-l1 |
| Why it matters: | m03-l1 |
| Why it means "continuation": | m12-l1 |
| Why it means "reversal": | m12-l1 |
| Why it sits exactly there. | m06-l1 |
| Why it warns you. | m18-l1 |
| Why neither works alone: | m25-l1 |
| Why R and not dollars: | m27-l2 |
| Why size last: | m27-l1 |
| Why small samples lie: | m25-l1 |
| Why so small. | m22-l1 |
| Why start here: | m27-l1 |
| Why the clock matters at all. | m23-l1 |
| Why the distinction exists. | m07-l1 |
| Why the evidence is not optional: | m27-l2 |
| Why the gap matters. | m20-l1 |
| Why the order cannot flip: | m27-l1 |
| Why the starting point does not matter. | m30-l1 |
| Why there and nowhere else: | m27-l1 |
| Why there are two rates. | m07-l1 |
| Why this is an upgrade on "support and resistance". | m33-l1 |
| Why this is the right number: | m25-l1 |
| Why this matters more than the score: | m27-l2 |
| Why this matters — the half that is really just price. | m18-l1 |
| Why this order. | m22-l1 |
| Why two prices exist. | m04-l1 |
| Why validate at all: | m27-l2 |
| Why wait for the trigger: | m27-l1 |
| Why you always read it relative. | m14-l1 |
| Why: | m09-l2 |
| wicks | m03-l1 |
| wide stop forces a smaller position | m22-l1 |
| widening | m32-l1 |
| Widening the stop. | m27-l1 |
| Win rate | m25-l1 |
| Withdrawal address whitelist. | m02-l1 |
| withdrawals disabled | m02-l1 |
| Worked example (bullish) | m30-l1 |
| Worked example, one token. | m20-l1 |
| Worked numbers. | m19-l1 |
| worse | m05-l1 |
| Wyckoff | m09-l1 |
| You are left holding the winning leg of a hedge whose losing leg has been closed at the worst possible price | m21-l1 |
| you can tell a claim with a mechanism from one without. | m35-l1 |
| you do not fill | m24-l1 |
| You find a trend on the lower frame that is a pullback on the higher one. | m23-l2 |
| You hold keys, not accounts. | m01-l1 |
| you stopped following it | m28-l1 |
| Your gains and your losses, symmetrically. | m05-l1 |
| your own | m19-l2 |
| Zero cross: | m11-l1 |
| zero line | m11-l1 |
| zero-line cross | m11-l1 |
| zone of interest | m18-l1 |
| zone to watch, not a line that must hold | m10-l1 |
| — you have to double what is left. - Lose | m22-l1 |
| → you need | m22-l1 |
| −1 | m22-l2 |
| −100 USDT | m22-l2 |
| −18,800 | m30-l1 |
| −18.00 USDT | m07-l1 |
| −1R | m22-l1 |
| −20 USDT per trade | m25-l1 |
| −22.22 USDT | m07-l1 |
| −300 | m30-l1 |
| −32 | m11-l1 |
| −4,800 | m30-l1 |
| −500 | m11-l1 |
| −800 | m30-l1 |

## Appendix B — ES words in 3+ lessons, not in the glossary (1818)

| Term | Lessons |
| --- | ---: |
| mercado | 42 |
| precio | 42 |
| verdad | 39 |
| exactamente | 38 |
| movimiento | 37 |
| justo | 36 |
| significa | 36 |
| real | 35 |
| tres | 35 |
| ahora | 34 |
| gráfico | 34 |
| sola | 34 |
| encima | 33 |
| nivel | 33 |
| abajo | 32 |
| grande | 32 |
| lado | 32 |
| número | 32 |
| posición | 32 |
| queda | 32 |
| sube | 32 |
| arriba | 31 |
| compra | 31 |
| cripto | 31 |
| debajo | 31 |
| dentro | 31 |
| lección | 31 |
| libro | 31 |
| ninguna | 31 |
| operación | 31 |
| semana | 31 |
| tamaño | 31 |
| vuelve | 31 |
| cierre | 30 |
| fin | 30 |
| leer | 30 |
| números | 30 |
| órdenes | 29 |
| alto | 28 |
| baja | 28 |
| cualquier | 28 |
| dirección | 28 |
| importa | 28 |
| orden | 28 |
| razón | 28 |
| btc | 27 |
| cerca | 27 |
| error | 27 |
| gente | 27 |
| liquidez | 27 |
| precios | 27 |
| señal | 27 |
| tiempo | 27 |
| anterior | 26 |
| día | 26 |
| lee | 26 |
| suele | 26 |
| venta | 26 |
| cuenta | 25 |
| deja | 25 |
| después | 25 |
| entrada | 25 |
| exchange | 25 |
| fuerza | 25 |
| nuevo | 25 |
| cambia | 24 |
| cierra | 24 |
| dinero | 24 |
| parece | 24 |
| peor | 24 |
| punto | 24 |
| rápido | 24 |
| stop | 24 |
| único | 24 |
| compradores | 23 |
| diferencia | 23 |
| fino | 23 |
| momento | 23 |
| operar | 23 |
| riesgo | 23 |
| ruido | 23 |
| trata | 23 |
| vuelta | 23 |
| alcista | 22 |
| convierte | 22 |
| mayor | 22 |
| mecánica | 22 |
| medida | 22 |
| muestra | 22 |
| mueve | 22 |
| ningún | 22 |
| operaciones | 22 |
| primera | 22 |
| profundo | 22 |
| siguiente | 22 |
| último | 22 |
| única | 22 |
| alrededor | 21 |
| detrás | 21 |
| funciona | 21 |
| horas | 21 |
| hueco | 21 |
| lectura | 21 |
| línea | 21 |
| menudo | 21 |
| máximo | 21 |
| niveles | 21 |
| propia | 21 |
| práctica | 21 |
| versión | 21 |
| ambos | 20 |
| cae | 20 |
| caída | 20 |
| frente | 20 |
| fuera | 20 |
| honesta | 20 |
| igual | 20 |
| lleva | 20 |
| mayoría | 20 |
| mitad | 20 |
| moneda | 20 |
| mínimo | 20 |
| pasa | 20 |
| primero | 20 |
| puntos | 20 |
| vale | 20 |
| demás | 19 |
| ejemplo | 19 |
| existe | 19 |
| final | 19 |
| flujo | 19 |
| idea | 19 |
| necesita | 19 |
| pequeña | 19 |
| propio | 19 |
| regla | 19 |
| sesión | 19 |
| trading | 19 |
| tramo | 19 |
| cuatro | 18 |
| errores | 18 |
| figura | 18 |
| honesto | 18 |
| llega | 18 |
| mercados | 18 |
| mundo | 18 |
| módulo | 18 |
| nombre | 18 |
| normal | 18 |
| ocurre | 18 |
| sale | 18 |
| suelo | 18 |
| techo | 18 |
| tranquilo | 18 |
| ver | 18 |
| acaba | 17 |
| bajista | 17 |
| buena | 17 |
| curso | 17 |
| datos | 17 |
| distintas | 17 |
| días | 17 |
| extremo | 17 |
| fuerte | 17 |
| grandes | 17 |
| gráficos | 17 |
| hora | 17 |
| información | 17 |
| medio | 17 |
| normalmente | 17 |
| nueva | 17 |
| posiciones | 17 |
| pérdida | 17 |
| pérdidas | 17 |
| simplemente | 17 |
| trampa | 17 |
| abierto | 16 |
| alta | 16 |
| cambio | 16 |
| campana | 16 |
| completo | 16 |
| comprar | 16 |
| cuesta | 16 |
| decide | 16 |
| entero | 16 |
| espera | 16 |
| merece | 16 |
| minutos | 16 |
| pregunta | 16 |
| principiante | 16 |
| reposo | 16 |
| segundo | 16 |
| stops | 16 |
| trabajo | 16 |
| traders | 16 |
| afirmación | 15 |
| allá | 15 |
| bastante | 15 |
| cerrar | 15 |
| cierran | 15 |
| disciplina | 15 |
| distinto | 15 |
| entrar | 15 |
| fíjate | 15 |
| libros | 15 |
| líneas | 15 |
| madrugada | 15 |
| mecanismo | 15 |
| media | 15 |
| mide | 15 |
| pierde | 15 |
| precisamente | 15 |
| salta | 15 |
| seguir | 15 |
| segunda | 15 |
| subir | 15 |
| swing | 15 |
| tipo | 15 |
| varios | 15 |
| vendedores | 15 |
| vender | 15 |
| útil | 15 |
| alguien | 14 |
| alts | 14 |
| común | 14 |
| conjunto | 14 |
| cualquiera | 14 |
| empuja | 14 |
| estaba | 14 |
| fines | 14 |
| lados | 14 |
| limpia | 14 |
| mal | 14 |
| mantener | 14 |
| mejor | 14 |
| máximos | 14 |
| oferta | 14 |
| pasado | 14 |
| pequeño | 14 |
| perder | 14 |
| principiantes | 14 |
| prueba | 14 |
| salir | 14 |
| siendo | 14 |
| silencio | 14 |
| sitio | 14 |
| tarde | 14 |
| usdt | 14 |
| aguantar | 13 |
| ambas | 13 |
| aritmética | 13 |
| bolsa | 13 |
| cero | 13 |
| comprando | 13 |
| compras | 13 |
| confirmación | 13 |
| contrario | 13 |
| debería | 13 |
| directamente | 13 |
| dispara | 13 |
| distinta | 13 |
| esperando | 13 |
| estructura | 13 |
| exchanges | 13 |
| formas | 13 |
| gana | 13 |
| golpe | 13 |
| herramienta | 13 |
| instante | 13 |
| lejos | 13 |
| límite | 13 |
| marca | 13 |
| moverse | 13 |
| ninguno | 13 |
| partir | 13 |
| patrón | 13 |
| pequeñas | 13 |
| perpetuo | 13 |
| profundos | 13 |
| razones | 13 |
| realidad | 13 |
| salida | 13 |
| semanas | 13 |
| siguen | 13 |
| siquiera | 13 |
| subida | 13 |
| supón | 13 |
| torno | 13 |
| total | 13 |
| trader | 13 |
| valor | 13 |
| varias | 13 |
| viene | 13 |
| abrir | 12 |
| alza | 12 |
| aparece | 12 |
| banda | 12 |
| cantidad | 12 |
| compara | 12 |
| concreto | 12 |
| construye | 12 |
| corta | 12 |
| esperar | 12 |
| estado | 12 |
| fija | 12 |
| fijo | 12 |
| ganancia | 12 |
| ganas | 12 |
| historia | 12 |
| indicador | 12 |
| llegar | 12 |
| mala | 12 |
| manual | 12 |
| motivo | 12 |
| mínimos | 12 |
| noche | 12 |
| pagan | 12 |
| perpetuos | 12 |
| pico | 12 |
| pone | 12 |
| primer | 12 |
| reales | 12 |
| respuesta | 12 |
| resultado | 12 |
| según | 12 |
| serie | 12 |
| toca | 12 |
| vende | 12 |
| ventana | 12 |
| aguanta | 11 |
| aspecto | 11 |
| atraviesa | 11 |
| buen | 11 |
| capital | 11 |
| cifra | 11 |
| cinco | 11 |
| daño | 11 |
| decisión | 11 |
| dejar | 11 |
| delante | 11 |
| demanda | 11 |
| describe | 11 |
| distancia | 11 |
| distintos | 11 |
| elige | 11 |
| empieza | 11 |
| enseña | 11 |
| enseñó | 11 |
| entera | 11 |
| esté | 11 |
| fallo | 11 |
| favor | 11 |
| fecha | 11 |
| futuros | 11 |
| ganancias | 11 |
| giro | 11 |
| larga | 11 |
| limpio | 11 |
| liquidaciones | 11 |
| manos | 11 |
| menor | 11 |
| mira | 11 |
| objetivo | 11 |
| pagando | 11 |
| paso | 11 |
| perdedora | 11 |
| periodo | 11 |
| quedarse | 11 |
| realmente | 11 |
| recorre | 11 |
| rompe | 11 |
| roto | 11 |
| saber | 11 |
| seguro | 11 |
| señales | 11 |
| termina | 11 |
| todavía | 11 |
| usa | 11 |
| volver | 11 |
| zona | 11 |
| acciones | 10 |
| actual | 10 |
| aviso | 10 |
| añade | 10 |
| barra | 10 |
| bloque | 10 |
| cara | 10 |
| cierres | 10 |
| comisiones | 10 |
| constantemente | 10 |
| convicción | 10 |
| conviene | 10 |
| cotiza | 10 |
| dibuja | 10 |
| diez | 10 |
| domingo | 10 |
| esconde | 10 |
| espejo | 10 |
| extremos | 10 |
| falta | 10 |
| frase | 10 |
| generan | 10 |
| gran | 10 |
| hacerlo | 10 |
| haciendo | 10 |
| hizo | 10 |
| hoy | 10 |
| imagen | 10 |
| importan | 10 |
| instrumento | 10 |
| límites | 10 |
| mirar | 10 |
| mover | 10 |
| mueven | 10 |
| negativo | 10 |
| pantalla | 10 |
| partes | 10 |
| participantes | 10 |
| plan | 10 |
| podría | 10 |
| principio | 10 |
| puñado | 10 |
| rebote | 10 |
| reglas | 10 |
| revés | 10 |
| separa | 10 |
| sesgo | 10 |
| tercera | 10 |
| terminado | 10 |
| toma | 10 |
| tratar | 10 |
| ventas | 10 |
| volatilidad | 10 |
| última | 10 |
| abre | 9 |
| alt | 9 |
| altos | 9 |
| barras | 9 |
| beneficio | 9 |
| cayendo | 9 |
| cientos | 9 |
| claramente | 9 |
| combustible | 9 |
| completa | 9 |
| comprador | 9 |
| concreta | 9 |
| confirma | 9 |
| conocida | 9 |
| constante | 9 |
| coste | 9 |
| cuentas | 9 |
| dejan | 9 |
| encontrar | 9 |
| escalera | 9 |
| fondo | 9 |
| fracción | 9 |
| frecuencia | 9 |
| habitual | 9 |
| habría | 9 |
| imprime | 9 |
| incluso | 9 |
| juntas | 9 |
| lógica | 9 |
| mantiene | 9 |
| meses | 9 |
| minuto | 9 |
| mirando | 9 |
| movimientos | 9 |
| necesitas | 9 |
| nuevos | 9 |
| paga | 9 |
| pagar | 9 |
| pena | 9 |
| pista | 9 |
| positivo | 9 |
| predice | 9 |
| puso | 9 |
| quedan | 9 |
| rara | 9 |
| reacción | 9 |
| reciente | 9 |
| respecto | 9 |
| resto | 9 |
| resultados | 9 |
| rápida | 9 |
| saldo | 9 |
| sentido | 9 |
| suceso | 9 |
| tick | 9 |
| tradicionales | 9 |
| ventaja | 9 |
| ves | 9 |
| vivo | 9 |
| últimas | 9 |
| abierta | 8 |
| activo | 8 |
| advertencia | 8 |
| algún | 8 |
| apalancada | 8 |
| apertura | 8 |
| arrastra | 8 |
| buscar | 8 |
| caer | 8 |
| cambiado | 8 |
| cambiar | 8 |
| camino | 8 |
| colateral | 8 |
| comparten | 8 |
| concurrida | 8 |
| condiciones | 8 |
| contexto | 8 |
| continua | 8 |
| corriente | 8 |
| dado | 8 |
| dato | 8 |
| depende | 8 |
| derecha | 8 |
| disponible | 8 |
| dispuestos | 8 |
| ejecución | 8 |
| empezar | 8 |
| empujar | 8 |
| empuje | 8 |
| encuentra | 8 |
| eres | 8 |
| escala | 8 |
| exige | 8 |
| existen | 8 |
| falla | 8 |
| falsa | 8 |
| fácil | 8 |
| gira | 8 |
| gratis | 8 |
| independientes | 8 |
| izquierda | 8 |
| lento | 8 |
| llegue | 8 |
| mañana | 8 |
| mecánico | 8 |
| mete | 8 |
| monedas | 8 |
| movido | 8 |
| noticia | 8 |
| ocurrió | 8 |
| opera | 8 |
| opinión | 8 |
| pago | 8 |
| participación | 8 |
| patrones | 8 |
| peligroso | 8 |
| permiso | 8 |
| peso | 8 |
| porcentaje | 8 |
| presión | 8 |
| probable | 8 |
| promesa | 8 |
| propios | 8 |
| pueda | 8 |
| quedar | 8 |
| quienes | 8 |
| recuperar | 8 |
| reduce | 8 |
| registro | 8 |
| secuencia | 8 |
| segundos | 8 |
| simple | 8 |
| subiendo | 8 |
| suelen | 8 |
| suficiente | 8 |
| suma | 8 |
| superior | 8 |
| tesis | 8 |
| trabajado | 8 |
| violenta | 8 |
| vive | 8 |
| vocabulario | 8 |
| vuelven | 8 |
| absoluto | 7 |
| acción | 7 |
| actuar | 7 |
| acuerdo | 7 |
| aguante | 7 |
| análisis | 7 |
| aparecer | 7 |
| aproximadamente | 7 |
| asoma | 7 |
| avance | 7 |
| bitcoin | 7 |
| bruto | 7 |
| capitalización | 7 |
| caro | 7 |
| caza | 7 |
| central | 7 |
| cerrando | 7 |
| clásico | 7 |
| cobra | 7 |
| come | 7 |
| completamente | 7 |
| comporta | 7 |
| conocido | 7 |
| construido | 7 |
| cubrir | 7 |
| debes | 7 |
| decenas | 7 |
| dejó | 7 |
| dibujan | 7 |
| dicen | 7 |
| difícil | 7 |
| dimensiona | 7 |
| direcciones | 7 |
| disparar | 7 |
| débil | 7 |
| ejecutar | 7 |
| ejercicio | 7 |
| elegir | 7 |
| elimina | 7 |
| ello | 7 |
| enorme | 7 |
| equivocada | 7 |
| equivocado | 7 |
| estructural | 7 |
| evento | 7 |
| fiable | 7 |
| finos | 7 |
| forzoso | 7 |
| futuro | 7 |
| ganadora | 7 |
| garantía | 7 |
| genuina | 7 |
| genuinamente | 7 |
| gestión | 7 |
| habilidad | 7 |
| haga | 7 |
| idéntica | 7 |
| intacta | 7 |
| lees | 7 |
| liquida | 7 |
| llegan | 7 |
| momentum | 7 |
| mostrar | 7 |
| natural | 7 |
| neto | 7 |
| operando | 7 |
| panel | 7 |
| papel | 7 |
| parecen | 7 |
| pasó | 7 |
| pausa | 7 |
| pequeños | 7 |
| pierdes | 7 |
| plano | 7 |
| plataformas | 7 |
| pon | 7 |
| pondera | 7 |
| problema | 7 |
| propias | 7 |
| proporción | 7 |
| propósito | 7 |
| protege | 7 |
| pánico | 7 |
| quedas | 7 |
| rally | 7 |
| recuerda | 7 |
| recupera | 7 |
| recuperación | 7 |
| relación | 7 |
| reloj | 7 |
| responde | 7 |
| ritmo | 7 |
| régimen | 7 |
| sería | 7 |
| significado | 7 |
| sistema | 7 |
| sostenida | 7 |
| suficientes | 7 |
| suposición | 7 |
| tema | 7 |
| tenga | 7 |
| tomar | 7 |
| transferencia | 7 |
| usar | 7 |
| verde | 7 |
| violento | 7 |
| visto | 7 |
| abres | 6 |
| absorbe | 6 |
| absorbiendo | 6 |
| acaban | 6 |
| acerca | 6 |
| acotada | 6 |
| adelgaza | 6 |
| agota | 6 |
| agregado | 6 |
| agrupan | 6 |
| aguantado | 6 |
| alcanza | 6 |
| anteriores | 6 |
| aplica | 6 |
| apuesta | 6 |
| apunta | 6 |
| atención | 6 |
| atrás | 6 |
| años | 6 |
| barato | 6 |
| calcula | 6 |
| cambió | 6 |
| casos | 6 |
| coge | 6 |
| coincide | 6 |
| compresión | 6 |
| compró | 6 |
| confundir | 6 |
| consecuencia | 6 |
| construcción | 6 |
| contar | 6 |
| continúa | 6 |
| control | 6 |
| costes | 6 |
| crece | 6 |
| cruzado | 6 |
| cuánta | 6 |
| cálculo | 6 |
| cómodamente | 6 |
| decisiones | 6 |
| deliberado | 6 |
| devuelve | 6 |
| digamos | 6 |
| dispararse | 6 |
| dispuesto | 6 |
| distinción | 6 |
| distinguir | 6 |
| ejecuta | 6 |
| empujaron | 6 |
| encoge | 6 |
| encontrarás | 6 |
| ensancha | 6 |
| entradas | 6 |
| escasa | 6 |
| espacio | 6 |
| estanca | 6 |
| estilo | 6 |
| estrategia | 6 |
| estuviera | 6 |
| exacto | 6 |
| facilidad | 6 |
| festivos | 6 |
| forman | 6 |
| forzado | 6 |
| funcionan | 6 |
| fórmula | 6 |
| garantizado | 6 |
| gestionar | 6 |
| girar | 6 |
| herramientas | 6 |
| historias | 6 |
| importante | 6 |
| inferior | 6 |
| intento | 6 |
| interés | 6 |
| juego | 6 |
| junto | 6 |
| juntos | 6 |
| lenta | 6 |
| lista | 6 |
| llegó | 6 |
| mantenimiento | 6 |
| mantienen | 6 |
| mantén | 6 |
| mapa | 6 |
| masa | 6 |
| medias | 6 |
| mes | 6 |
| miedo | 6 |
| miles | 6 |
| muestran | 6 |
| multitud | 6 |
| nocturno | 6 |
| nombrar | 6 |
| normales | 6 |
| ocurrir | 6 |
| ojo | 6 |
| operas | 6 |
| oportunidad | 6 |
| opuestas | 6 |
| opuesto | 6 |
| palabra | 6 |
| palabras | 6 |
| par | 6 |
| parezca | 6 |
| participante | 6 |
| perdiendo | 6 |
| perfectamente | 6 |
| persona | 6 |
| plataforma | 6 |
| plazo | 6 |
| pones | 6 |
| porción | 6 |
| positiva | 6 |
| protección | 6 |
| pruebas | 6 |
| psicología | 6 |
| puedas | 6 |
| quiere | 6 |
| racha | 6 |
| reacciona | 6 |
| referencia | 6 |
| resuelto | 6 |
| rompen | 6 |
| sabes | 6 |
| salen | 6 |
| seguridad | 6 |
| seis | 6 |
| sencillamente | 6 |
| sesiones | 6 |
| siente | 6 |
| siga | 6 |
| significan | 6 |
| signo | 6 |
| sirve | 6 |
| sobrevive | 6 |
| sostiene | 6 |
| supera | 6 |
| tasa | 6 |
| temporal | 6 |
| tenía | 6 |
| terminar | 6 |
| tokens | 6 |
| tomas | 6 |
| tranquila | 6 |
| unidades | 6 |
| vacío | 6 |
| vence | 6 |
| vendedor | 6 |
| venden | 6 |
| vigila | 6 |
| zonas | 6 |
| índice | 6 |
| acumula | 5 |
| acumulan | 5 |
| adelantado | 5 |
| agotado | 5 |
| aire | 5 |
| aislada | 5 |
| ajustar | 5 |
| ajuste | 5 |
| ancho | 5 |
| antemano | 5 |
| antiguo | 5 |
| apalancado | 5 |
| apilan | 5 |
| apostar | 5 |
| arbitraje | 5 |
| argumento | 5 |
| avisa | 5 |
| banco | 5 |
| brusco | 5 |
| bueno | 5 |
| busca | 5 |
| caen | 5 |
| calidad | 5 |
| cambios | 5 |
| cartera | 5 |
| cayó | 5 |
| cerró | 5 |
| ciclo | 5 |
| cifras | 5 |
| cita | 5 |
| clave | 5 |
| cobertura | 5 |
| coinciden | 5 |
| cola | 5 |
| coloca | 5 |
| colocado | 5 |
| compran | 5 |
| condición | 5 |
| confianza | 5 |
| confirmar | 5 |
| controlas | 5 |
| corre | 5 |
| correr | 5 |
| creadores | 5 |
| criterio | 5 |
| cruza | 5 |
| cubre | 5 |
| dar | 5 |
| day | 5 |
| decides | 5 |
| decía | 5 |
| defecto | 5 |
| definición | 5 |
| dejando | 5 |
| demasiado | 5 |
| demuestra | 5 |
| deriva | 5 |
| descripción | 5 |
| deslizamiento | 5 |
| detiene | 5 |
| diaria | 5 |
| dibujado | 5 |
| dimensionar | 5 |
| directo | 5 |
| disfrazado | 5 |
| dólar | 5 |
| dólares | 5 |
| ejecutan | 5 |
| ejecutarse | 5 |
| ejemplos | 5 |
| elección | 5 |
| eliges | 5 |
| empiezan | 5 |
| entender | 5 |
| entra | 5 |
| equivocarse | 5 |
| especialmente | 5 |
| esperabas | 5 |
| estrecha | 5 |
| estuvo | 5 |
| estén | 5 |
| exceso | 5 |
| explica | 5 |
| exposición | 5 |
| expuesto | 5 |
| extra | 5 |
| factura | 5 |
| fallos | 5 |
| fase | 5 |
| fiarte | 5 |
| fina | 5 |
| fondos | 5 |
| forzada | 5 |
| fuertes | 5 |
| ganando | 5 |
| ganar | 5 |
| genera | 5 |
| haces | 5 |
| hazte | 5 |
| honestidad | 5 |
| hábito | 5 |
| iguales | 5 |
| imagina | 5 |
| incluido | 5 |
| instancia | 5 |
| invisible | 5 |
| juzgar | 5 |
| largas | 5 |
| lateral | 5 |
| leerlo | 5 |
| lente | 5 |
| limita | 5 |
| limpiamente | 5 |
| llama | 5 |
| llevan | 5 |
| llevar | 5 |
| llevas | 5 |
| long | 5 |
| lunes | 5 |
| manda | 5 |
| mano | 5 |
| marcha | 5 |
| mayores | 5 |
| mejora | 5 |
| miente | 5 |
| modesta | 5 |
| muchísimo | 5 |
| muerto | 5 |
| niega | 5 |
| nombres | 5 |
| nota | 5 |
| obliga | 5 |
| ocho | 5 |
| ofertas | 5 |
| pagas | 5 |
| parar | 5 |
| pasando | 5 |
| pasar | 5 |
| pase | 5 |
| pie | 5 |
| piezas | 5 |
| poner | 5 |
| posible | 5 |
| postura | 5 |
| pregúntate | 5 |
| previa | 5 |
| primeras | 5 |
| proceso | 5 |
| quedarte | 5 |
| querías | 5 |
| rate | 5 |
| reaccionar | 5 |
| recorrido | 5 |
| registra | 5 |
| retira | 5 |
| riesgos | 5 |
| rompió | 5 |
| salió | 5 |
| saltar | 5 |
| salte | 5 |
| sana | 5 |
| sean | 5 |
| sentado | 5 |
| separado | 5 |
| short | 5 |
| solos | 5 |
| sostenido | 5 |
| subió | 5 |
| superar | 5 |
| tampoco | 5 |
| temprano | 5 |
| ten | 5 |
| tenido | 5 |
| test | 5 |
| tiende | 5 |
| tienta | 5 |
| tocar | 5 |
| tomando | 5 |
| trampas | 5 |
| truco | 5 |
| unidad | 5 |
| unilateral | 5 |
| vaivén | 5 |
| vaya | 5 |
| veinte | 5 |
| ven | 5 |
| vigilar | 5 |
| ánimo | 5 |
| últimos | 5 |
| abrió | 4 |
| absorber | 4 |
| acabas | 4 |
| accidente | 4 |
| acepta | 4 |
| acierto | 4 |
| actividad | 4 |
| adelante | 4 |
| afirmar | 4 |
| agotada | 4 |
| agotamiento | 4 |
| aislado | 4 |
| ajusta | 4 |
| ajustado | 4 |
| altas | 4 |
| amontona | 4 |
| amplifica | 4 |
| ancha | 4 |
| apagando | 4 |
| aparecieron | 4 |
| aparte | 4 |
| apetece | 4 |
| aplicada | 4 |
| aportas | 4 |
| aproximado | 4 |
| asegurar | 4 |
| atravesar | 4 |
| avanza | 4 |
| azar | 4 |
| bajar | 4 |
| bajos | 4 |
| bandas | 4 |
| bando | 4 |
| barata | 4 |
| basta | 4 |
| borra | 4 |
| calladamente | 4 |
| cambiando | 4 |
| caras | 4 |
| carga | 4 |
| caídas | 4 |
| caído | 4 |
| certeza | 4 |
| clara | 4 |
| clase | 4 |
| clásica | 4 |
| coincidir | 4 |
| colchón | 4 |
| comparar | 4 |
| comprime | 4 |
| comprobar | 4 |
| compromiso | 4 |
| comprueba | 4 |
| concentran | 4 |
| conclusión | 4 |
| confirmada | 4 |
| consiste | 4 |
| continuación | 4 |
| contraria | 4 |
| convertir | 4 |
| convierten | 4 |
| correcta | 4 |
| correcto | 4 |
| creer | 4 |
| creíble | 4 |
| cuentan | 4 |
| curva | 4 |
| cuántos | 4 |
| dale | 4 |
| darte | 4 |
| deberías | 4 |
| decidido | 4 |
| decirte | 4 |
| defensa | 4 |
| dejado | 4 |
| deliberadamente | 4 |
| derecho | 4 |
| desacuerdo | 4 |
| desconocido | 4 |
| describir | 4 |
| deshacer | 4 |
| dibujada | 4 |
| diciendo | 4 |
| direccional | 4 |
| discrepan | 4 |
| diseño | 4 |
| disparan | 4 |
| distingue | 4 |
| doble | 4 |
| duermes | 4 |
| efectivo | 4 |
| ejercicios | 4 |
| elegiste | 4 |
| emocional | 4 |
| empezado | 4 |
| empezó | 4 |
| empujan | 4 |
| empujando | 4 |
| encaja | 4 |
| encuentras | 4 |
| enteramente | 4 |
| entrado | 4 |
| entrega | 4 |
| equilibrio | 4 |
| escrita | 4 |
| escrito | 4 |
| esfuerzo | 4 |
| espectacular | 4 |
| esperado | 4 |
| estallido | 4 |
| estilos | 4 |
| estés | 4 |
| etiqueta | 4 |
| eventos | 4 |
| exacta | 4 |
| explican | 4 |
| falsas | 4 |
| fechas | 4 |
| fenómeno | 4 |
| fijada | 4 |
| fijas | 4 |
| forzadas | 4 |
| forzar | 4 |
| forzosos | 4 |
| frontera | 4 |
| frágil | 4 |
| ganadoras | 4 |
| ganan | 4 |
| garantiza | 4 |
| generada | 4 |
| general | 4 |
| giros | 4 |
| giró | 4 |
| golpea | 4 |
| golpean | 4 |
| goteo | 4 |
| habitualmente | 4 |
| habían | 4 |
| hayas | 4 |
| horario | 4 |
| hubo | 4 |
| hunde | 4 |
| ida | 4 |
| ideas | 4 |
| idéntico | 4 |
| importar | 4 |
| impulso | 4 |
| inicio | 4 |
| instrumentos | 4 |
| intención | 4 |
| intenta | 4 |
| intervalos | 4 |
| intradía | 4 |
| inversión | 4 |
| jamás | 4 |
| justamente | 4 |
| keys | 4 |
| lecturas | 4 |
| ley | 4 |
| leído | 4 |
| libre | 4 |
| llamado | 4 |
| llevaba | 4 |
| léelo | 4 |
| malo | 4 |
| market | 4 |
| matemática | 4 |
| material | 4 |
| matiz | 4 |
| medición | 4 |
| medir | 4 |
| memoria | 4 |
| miden | 4 |
| miras | 4 |
| modelo | 4 |
| movió | 4 |
| móviles | 4 |
| neutral | 4 |
| nombra | 4 |
| not | 4 |
| nueve | 4 |
| obvia | 4 |
| obvios | 4 |
| ocurra | 4 |
| ofrece | 4 |
| partida | 4 |
| pasada | 4 |
| pasos | 4 |
| pensar | 4 |
| perdedoras | 4 |
| perdieron | 4 |
| perdió | 4 |
| permite | 4 |
| perseguir | 4 |
| persistente | 4 |
| personas | 4 |
| pertenece | 4 |
| pesa | 4 |
| pide | 4 |
| pilla | 4 |
| planificada | 4 |
| poder | 4 |
| ponerse | 4 |
| ponerte | 4 |
| porcentual | 4 |
| porcentuales | 4 |
| posicionado | 4 |
| posicionamiento | 4 |
| preguntas | 4 |
| preparado | 4 |
| presente | 4 |
| previo | 4 |
| primeros | 4 |
| probabilidad | 4 |
| probabilidades | 4 |
| produce | 4 |
| profesional | 4 |
| profunda | 4 |
| programada | 4 |
| promedia | 4 |
| pronto | 4 |
| pronóstico | 4 |
| próximo | 4 |
| puedan | 4 |
| quedó | 4 |
| ratio | 4 |
| razonable | 4 |
| realizado | 4 |
| reanude | 4 |
| rebota | 4 |
| rechazado | 4 |
| recibe | 4 |
| recuperó | 4 |
| red | 4 |
| rendimiento | 4 |
| rentable | 4 |
| repisa | 4 |
| reserva | 4 |
| resolución | 4 |
| respeta | 4 |
| resuelve | 4 |
| retrocede | 4 |
| roja | 4 |
| saltan | 4 |
| saltarse | 4 |
| sangrando | 4 |
| saturado | 4 |
| scalper | 4 |
| sección | 4 |
| seguidas | 4 |
| sensación | 4 |
| separadas | 4 |
| señala | 4 |
| silenciosa | 4 |
| sitúa | 4 |
| sobrevivir | 4 |
| sostener | 4 |
| suben | 4 |
| subidas | 4 |
| suena | 4 |
| suerte | 4 |
| sustituye | 4 |
| síntoma | 4 |
| tablas | 4 |
| temprana | 4 |
| tercer | 4 |
| terminan | 4 |
| terreno | 4 |
| ticks | 4 |
| titular | 4 |
| token | 4 |
| tomada | 4 |
| toman | 4 |
| tope | 4 |
| toque | 4 |
| totalmente | 4 |
| traslada | 4 |
| través | 4 |
| traza | 4 |
| trazada | 4 |
| trivial | 4 |
| usarlo | 4 |
| utc | 4 |
| vacía | 4 |
| venir | 4 |
| verlo | 4 |
| versiones | 4 |
| vieja | 4 |
| viejo | 4 |
| vienen | 4 |
| vigilado | 4 |
| visible | 4 |
| viva | 4 |
| volvió | 4 |
| vuelto | 4 |
| vuelva | 4 |
| win | 4 |
| your | 4 |
| abandona | 3 |
| abandonar | 3 |
| abiertos | 3 |
| absolutamente | 3 |
| absorbida | 3 |
| absorbió | 3 |
| abstracto | 3 |
| acabar | 3 |
| acabó | 3 |
| acceso | 3 |
| aceptar | 3 |
| acertar | 3 |
| aciertos | 3 |
| acontecimiento | 3 |
| acorta | 3 |
| activa | 3 |
| activamente | 3 |
| actúa | 3 |
| actúan | 3 |
| acumulando | 3 |
| adelanta | 3 |
| afirmaciones | 3 |
| agresiva | 3 |
| agresivos | 3 |
| aguantó | 3 |
| agudiza | 3 |
| aleja | 3 |
| alimenta | 3 |
| altura | 3 |
| amontonan | 3 |
| amplia | 3 |
| amplio | 3 |
| ancla | 3 |
| anclaje | 3 |
| antigua | 3 |
| antiguos | 3 |
| apalancados | 3 |
| apiladas | 3 |
| apilados | 3 |
| aportan | 3 |
| apostando | 3 |
| apoyarse | 3 |
| app | 3 |
| aprendido | 3 |
| aproximación | 3 |
| apuntando | 3 |
| arranca | 3 |
| arriesgar | 3 |
| arrolle | 3 |
| artefacto | 3 |
| asimetría | 3 |
| atrae | 3 |
| atrapa | 3 |
| atrapado | 3 |
| atrapados | 3 |
| atrapan | 3 |
| añadir | 3 |
| año | 3 |
| bajada | 3 |
| barrer | 3 |
| basura | 3 |
| bola | 3 |
| bolsas | 3 |
| borde | 3 |
| borrar | 3 |
| break-even | 3 |
| bucle | 3 |
| cadena | 3 |
| calcular | 3 |
| calendario | 3 |
| caliente | 3 |
| calma | 3 |
| cambian | 3 |
| cantidades | 3 |
| capacidad | 3 |
| capaz | 3 |
| captura | 3 |
| carrera | 3 |
| causa | 3 |
| cautela | 3 |
| caía | 3 |
| cede | 3 |
| cercano | 3 |
| cerrada | 3 |
| cerrara | 3 |
| ciegas | 3 |
| cierras | 3 |
| circulante | 3 |
| claro | 3 |
| clic | 3 |
| clásicos | 3 |
| cobran | 3 |
| cobras | 3 |
| cociente | 3 |
| colocan | 3 |
| colocar | 3 |
| comienzo | 3 |
| comodidad | 3 |
| comparación | 3 |
| comprado | 3 |
| comprimido | 3 |
| concentra | 3 |
| concepto | 3 |
| conceptual | 3 |
| concluir | 3 |
| concretas | 3 |
| concurrido | 3 |
| confiar | 3 |
| confirme | 3 |
| conoce | 3 |
| conoces | 3 |
| construir | 3 |
| construyen | 3 |
| construyó | 3 |
| consume | 3 |
| contener | 3 |
| contiene | 3 |
| contienen | 3 |
| contigo | 3 |
| contraparte | 3 |
| controla | 3 |
| convención | 3 |
| convertida | 3 |
| cortas | 3 |
| corte | 3 |
| costa | 3 |
| costó | 3 |
| cotizado | 3 |
| crea | 3 |
| crecer | 3 |
| crecientes | 3 |
| creencia | 3 |
| creías | 3 |
| cristal | 3 |
| cross | 3 |
| cruce | 3 |
| cruces | 3 |
| cuestan | 3 |
| cueste | 3 |
| cuestión | 3 |
| cumpla | 3 |
| cuyas | 3 |
| cuántas | 3 |
| cúmulo | 3 |
| darse | 3 |
| debido | 3 |
| decidir | 3 |
| decisivo | 3 |
| dejas | 3 |
| deje | 3 |
| depositas | 3 |
| deprisa | 3 |
| derivado | 3 |
| derivados | 3 |
| desaparece | 3 |
| descansa | 3 |
| descansan | 3 |
| descarta | 3 |
| desconfiar | 3 |
| desconfía | 3 |
| describen | 3 |
| deshacerse | 3 |
| deslizas | 3 |
| despacio | 3 |
| detalle | 3 |
| dialecto | 3 |
| dibujar | 3 |
| diccionario | 3 |
| diciéndote | 3 |
| dicta | 3 |
| diferentes | 3 |
| diga | 3 |
| dijo | 3 |
| dimensionada | 3 |
| dimensionamiento | 3 |
| dimensionas | 3 |
| dio | 3 |
| disciplinado | 3 |
| divide | 3 |
| dorado | 3 |
| dueño | 3 |
| durar | 3 |
| duro | 3 |
| décima | 3 |
| efecto | 3 |
| ejecutado | 3 |
| eligió | 3 |
| emoción | 3 |
| empresa | 3 |
| empujado | 3 |
| empujón | 3 |
| ensanchar | 3 |
| entrando | 3 |
| entras | 3 |
| entraste | 3 |
| entrena | 3 |
| entusiastas | 3 |
| envía | 3 |
| equivocarte | 3 |
| específico | 3 |
| estaban | 3 |
| estadística | 3 |
| etapas | 3 |
| eth | 3 |
| evapora | 3 |
| excepciones | 3 |
| excepción | 3 |
| expansión | 3 |
| extrema | 3 |
| fabricado | 3 |
| falló | 3 |
| falso | 3 |
| fases | 3 |
| feed | 3 |
| figuras | 3 |
| fila | 3 |
| financiar | 3 |
| finas | 3 |
| fingir | 3 |
| firma | 3 |
| firmas | 3 |
| forzosa | 3 |
| fracasa | 3 |
| frecuente | 3 |
| frena | 3 |
| frenada | 3 |
| fricciones | 3 |
| fricción | 3 |
| fronteras | 3 |
| fuertemente | 3 |
| función | 3 |
| ganadores | 3 |
| gap | 3 |
| geometría | 3 |
| global | 3 |
| guardan | 3 |
| habituales | 3 |
| habla | 3 |
| habías | 3 |
| hecha | 3 |
| hechos | 3 |
| hiciera | 3 |
| hiciste | 3 |
| hipótesis | 3 |
| historial | 3 |
| holgura | 3 |
| honestamente | 3 |
| honestos | 3 |
| horaria | 3 |
| horizontal | 3 |
| hubiera | 3 |
| huecos | 3 |
| iban | 3 |
| ignora | 3 |
| igualmente | 3 |
| impresa | 3 |
| impreso | 3 |
| imprimiendo | 3 |
| incluida | 3 |
| incluidos | 3 |
| indicadores | 3 |
| inicial | 3 |
| inmediata | 3 |
| inmediatez | 3 |
| institucional | 3 |
| instrucción | 3 |
| intentando | 3 |
| intercambian | 3 |
| intercambio | 3 |
| intervalo | 3 |
| inverso | 3 |
| inversores | 3 |
| invertida | 3 |
| invierte | 3 |
| irrelevante | 3 |
| justificar | 3 |
| leen | 3 |
| leerse | 3 |
| levantar | 3 |
| leyendo | 3 |
| leída | 3 |
| libertad | 3 |
| liquidados | 3 |
| listado | 3 |
| literalmente | 3 |
| llegado | 3 |
| llegando | 3 |
| llegará | 3 |
| lleve | 3 |
| llevó | 3 |
| local | 3 |
| líquido | 3 |
| macro | 3 |
| malinterpretar | 3 |
| mando | 3 |
| mandos | 3 |
| mantenida | 3 |
| mantenido | 3 |
| mantienes | 3 |
| mantuvo | 3 |
| manía | 3 |
| maquinaria | 3 |
| marcar | 3 |
| mecanismos | 3 |
| medidas | 3 |
| medido | 3 |
| mesa | 3 |
| mesas | 3 |
| mil | 3 |
| misticismo | 3 |
| modesto | 3 |
| montón | 3 |
| moviéndose | 3 |
| mueva | 3 |
| mueves | 3 |
| máquina | 3 |
| método | 3 |
| móvil | 3 |
| nace | 3 |
| necesitan | 3 |
| negativa | 3 |
| negocia | 3 |
| negociado | 3 |
| negocio | 3 |
| negoció | 3 |
| nombró | 3 |
| nuestro | 3 |
| nuevas | 3 |
| obligado | 3 |
| obvio | 3 |
| oleada | 3 |
| olvida | 3 |
| olvidar | 3 |
| opciones | 3 |
| operan | 3 |
| operativa | 3 |
| operó | 3 |
| opuesta | 3 |
| oscila | 3 |
| paciencia | 3 |
| pagaste | 3 |
| paneles | 3 |
| parecían | 3 |
| pasados | 3 |
| pecado | 3 |
| pelea | 3 |
| peligro | 3 |
| pendiente | 3 |
| peores | 3 |
| perdedor | 3 |
| perdido | 3 |
| perfil | 3 |
| perfora | 3 |
| periodos | 3 |
| plana | 3 |
| ponen | 3 |
| porqué | 3 |
| posees | 3 |
| posterior | 3 |
| potente | 3 |
| precede | 3 |
| precisa | 3 |
| precisión | 3 |
| predecir | 3 |
| presupuesto | 3 |
| previos | 3 |
| privilegio | 3 |
| probar | 3 |
| producen | 3 |
| programado | 3 |
| programados | 3 |
| proporciones | 3 |
| publicado | 3 |
| publican | 3 |
| puesta | 3 |
| puesto | 3 |
| pura | 3 |
| puramente | 3 |
| pusiste | 3 |
| quiebra | 3 |
| quieras | 3 |
| quieres | 3 |
| quita | 3 |
| quizá | 3 |
| quédate | 3 |
| rachas | 3 |
| rato | 3 |
| raíz | 3 |
| reaccione | 3 |
| reacciones | 3 |
| realizada | 3 |
| reanuda | 3 |
| rebotando | 3 |
| recta | 3 |
| región | 3 |
| relativa | 3 |
| relativamente | 3 |
| relevante | 3 |
| repartido | 3 |
| repite | 3 |
| repiten | 3 |
| repunte | 3 |
| reservas | 3 |
| respalda | 3 |
| respaldada | 3 |
| respaldado | 3 |
| respetar | 3 |
| resumen | 3 |
| retirar | 3 |
| retraso | 3 |
| retrospectiva | 3 |
| rezagada | 3 |
| rinde | 3 |
| rinden | 3 |
| roles | 3 |
| rompa | 3 |
| ronda | 3 |
| sabe | 3 |
| saca | 3 |
| sacudir | 3 |
| salidas | 3 |
| salto | 3 |
| salvo | 3 |
| sangra | 3 |
| sangran | 3 |
| seductora | 3 |
| seguirá | 3 |
| segura | 3 |
| semanal | 3 |
| sencilla | 3 |
| sencillo | 3 |
| sentimiento | 3 |
| sepas | 3 |
| series | 3 |
| señalar | 3 |
| sientes | 3 |
| sigues | 3 |
| siguiendo | 3 |
| sitios | 3 |
| sobreapalancados | 3 |
| sobreviva | 3 |
| subes | 3 |
| subido | 3 |
| suelta | 3 |
| sueltan | 3 |
| sufres | 3 |
| sólida | 3 |
| tamaños | 3 |
| teniendo | 3 |
| tenías | 3 |
| termómetro | 3 |
| texto | 3 |
| tipos | 3 |
| tira | 3 |
| tomarla | 3 |
| topa | 3 |
| toques | 3 |
| trabaja | 3 |
| trabajando | 3 |
| trae | 3 |
| tramos | 3 |
| tranquilos | 3 |
| transacción | 3 |
| tratan | 3 |
| trates | 3 |
| trazar | 3 |
| trecho | 3 |
| triple | 3 |
| trátalo | 3 |
| tuvo | 3 |
| twitter | 3 |
| términos | 3 |
| típico | 3 |
| usan | 3 |
| vaivenes | 3 |
| valida | 3 |
| velocidad | 3 |
| vendido | 3 |
| vendiendo | 3 |
| ventanas | 3 |
| verdadero | 3 |
| verás | 3 |
| vida | 3 |
| vigilan | 3 |
| vino | 3 |
| violencia | 3 |
| vista | 3 |
| vistazo | 3 |
| vivir | 3 |
| voluntad | 3 |
| voy | 3 |
| voz | 3 |
| zoom | 3 |
| útiles | 3 |

## Appendix C — ES two-word phrases in 3+ lessons, not in the glossary (160)

| Term | Lessons |
| --- | ---: |
| tendencia alcista | 12 |
| tendencia bajista | 11 |
| precio sube | 10 |
| ejemplo trabajado | 8 |
| mercados tradicionales | 8 |
| sola vela | 8 |
| cierre forzoso | 7 |
| nuevo máximo | 7 |
| pierde dinero | 7 |
| ambos lados | 6 |
| apalancamiento alto | 6 |
| corto plazo | 6 |
| largos pagan | 6 |
| libro profundo | 6 |
| posición apalancada | 6 |
| precio cae | 6 |
| sola operación | 6 |
| cripto opera | 5 |
| error clásico | 5 |
| figura muestra | 5 |
| lección trata | 5 |
| lectura honesta | 5 |
| orden grande | 5 |
| propia media | 5 |
| ruido normal | 5 |
| tiempo real | 5 |
| tradicionales cierran | 5 |
| tres velas | 5 |
| varios días | 5 |
| algún punto | 4 |
| arriba abajo | 4 |
| baja capitalización | 4 |
| cortos pagan | 4 |
| cualquier mercado | 4 |
| day trader | 4 |
| futuros perpetuos | 4 |
| instancia generada | 4 |
| libro fino | 4 |
| media reciente | 4 |
| medias móviles | 4 |
| mercado entero | 4 |
| ningún mecanismo | 4 |
| not your | 4 |
| participación detrás | 4 |
| perpetuo cotiza | 4 |
| posición abierta | 4 |
| positivo significa | 4 |
| precio actual | 4 |
| precio cierra | 4 |
| precio suele | 4 |
| precio todavía | 4 |
| primera vela | 4 |
| propio precio | 4 |
| propios precios | 4 |
| punto porcentual | 4 |
| puntos porcentuales | 4 |
| temporalidad superior | 4 |
| tramo final | 4 |
| varios puntos | 4 |
| vela verde | 4 |
| venta forzada | 4 |
| volumen alto | 4 |
| volumen cuenta | 4 |
| your keys | 4 |
| única pregunta | 4 |
| alto significa | 3 |
| btc sube | 3 |
| buena operación | 3 |
| cierre diario | 3 |
| completamente distinto | 3 |
| compra agresiva | 3 |
| compra taker | 3 |
| compradores nuevos | 3 |
| cripto funciona | 3 |
| cuentan historias | 3 |
| dinero gratis | 3 |
| dinero nuevo | 3 |
| dinero real | 3 |
| ejemplo resuelto | 3 |
| espacio abierto | 3 |
| estaba comprando | 3 |
| exactamente igual | 3 |
| exchange cerrando | 3 |
| exchange cierra | 3 |
| flujo forzado | 3 |
| funding positivo | 3 |
| gana dinero | 3 |
| ganancia media | 3 |
| gran comprador | 3 |
| gráfico diario | 3 |
| hueco nocturno | 3 |
| imagen espejo | 3 |
| justo debajo | 3 |
| justo dentro | 3 |
| justo pasado | 3 |
| lado contrario | 3 |
| largos apalancados | 3 |
| liquidez escasa | 3 |
| mala operación | 3 |
| mecanismo detrás | 3 |
| mecha inferior | 3 |
| mecha larga | 3 |
| mercado alcista | 3 |
| mercado lateral | 3 |
| mercado tranquilo | 3 |
| mes pasado | 3 |
| movimiento brusco | 3 |
| mueven juntas | 3 |
| mínimo anterior | 3 |
| mínimo nuevo | 3 |
| mínimos crecientes | 3 |
| operación necesita | 3 |
| peor precio | 3 |
| ponerse corto | 3 |
| ponerte corto | 3 |
| precio baja | 3 |
| precio reaccione | 3 |
| precio rompe | 3 |
| precios distintos | 3 |
| primera lección | 3 |
| pérdida acotada | 3 |
| pérdida media | 3 |
| quedarse bastante | 3 |
| racha perdedora | 3 |
| razones propias | 3 |
| razón honesta | 3 |
| razón mecánica | 3 |
| riesgo real | 3 |
| ruptura bajista | 3 |
| ruptura genuina | 3 |
| semana tranquilo | 3 |
| serie temporal | 3 |
| sistema roto | 3 |
| sola barra | 3 |
| sola línea | 3 |
| sola posición | 3 |
| soporte antiguo | 3 |
| stop sale | 3 |
| sube significa | 3 |
| swing trader | 3 |
| tamaño real | 3 |
| tamaño sale | 3 |
| tendencia fuerte | 3 |
| tendencia previa | 3 |
| tendencias fuertes | 3 |
| tres días | 3 |
| valor nocional | 3 |
| veinte operaciones | 3 |
| vela anterior | 3 |
| vendedores empujaron | 3 |
| venta agresiva | 3 |
| venta taker | 3 |
| viene después | 3 |
| volumen enorme | 3 |
| volumen real | 3 |
| voz alta | 3 |
| órdenes fino | 3 |
| órdenes stop | 3 |
| última operación | 3 |
| último tramo | 3 |
