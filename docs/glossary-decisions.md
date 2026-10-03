# Decisiones sobre glossary-candidates.md — 3 de octubre de 2026

Revisión de la tabla curada (125 filas) de `docs/glossary-candidates.md`. Esto decide; el agente de la ronda corta ejecuta.

## Reglas

1. **Nada inventado.** Ningún término del glosario ni de la prosa que no exista fuera del curso. El lector debe poder buscar la palabra en cualquier fuente de trading y encontrarla con el mismo sentido. Los términos acuñados por el curso (lente, escalera, repisa, flujo forzado, bolsa de liquidez en el sentido de cúmulo de stops) se sustituyen por el término estándar en el pase de prosa 1.2, no se glosan.
2. **Sentido técnico distinto del cotidiano**, o jerga.
3. **2+ lecciones en ambos idiomas.** Excepción única: nombres propios de patrón de vela y de sesgo de backtest entran con 1 lección.
4. **Never-coins:** 0 lecciones en un idioma → fuera, salvo que la prosa de ese idioma lo use antes.
5. Los alias y acepciones no crean entrada: añaden `match` o acepción a la entrada existente.

## Tareas del agente, no decisiones

- Comprobar si "cierre forzoso" (7 lecciones ES) es forma no capturada de liquidación → añadir como match.
- Comprobar si "medias móviles" (4) es plural no capturado de media móvil → añadir como match.
- Comprobar cómo expresa EN "pérdida acotada" (3/0): si existe con otra palabra, unificar y evaluar; si no, fuera.
- Glosario de la app vs glosario del oficio: si "instancia generada" entra, marcar que es vocabulario de la app.

## Tabla

| ES | EN | Decisión | Nota |
| --- | --- | --- | --- |
| tendencia alcista | uptrend | entra | |
| tendencia bajista | downtrend | entra | |
| mercado lateral | sideways market | entra | |
| suelo | floor | alias | match de soporte |
| techo | ceiling | alias | match de resistencia |
| escalera | staircase | prosa-1.2 | acuñado; sustituir por "secuencia de máximos y mínimos crecientes/decrecientes" o "estructura" |
| repisa | shelf | prosa-1.2 | acuñado; sustituir por "nivel" / "zona de consolidación" |
| impulso | impulse | entra | |
| rebote | bounce | fuera | sentido cotidiano |
| extremo | extreme | fuera | sentido cotidiano |
| cierre (de vela) | close | entra | regla del curso: se juzga por el cierre |
| apertura | open | entra | |
| barra | bar | alias | match de vela |
| hueco | gap | entra | |
| número redondo | round number | entra | |
| zona de interés | area of interest | fuera | never-coins (EN 0) |
| área de valor | value area | fuera | 1/1 |
| valor justo | fair value | fuera | 1/2 |
| cuña ascendente / descendente | rising / falling wedge | acepción | de g-wedge |
| triángulo asc. / desc. / simétrico | asc. / desc. / symmetrical triangle | acepción | de triángulo |
| diagonal | diagonal | fuera | sentido cotidiano |
| compresión | compression | entra | |
| expansión | expansion | entra | |
| volatilidad | volatility | entra | |
| squeeze de volatilidad | volatility squeeze | acepción | de g-squeeze |
| régimen | regime | entra | |
| momentum | momentum | entra | |
| sesgo | bias | entra | |
| temporalidad superior | higher timeframe | entra | |
| de arriba abajo | top-down | entra | |
| intradía | intraday | entra | |
| periodo de tenencia | holding period | entra | |
| sesión | session | entra | |
| campana de cierre | closing bell | entra | |
| mercados tradicionales | traditional markets | fuera | concepto, no término |
| fin de semana (liquidez) | weekend | fuera | concepto, no término |
| doji | doji | entra | excepción 1 lección |
| martillo | hammer | entra | excepción 1 lección |
| estrella fugaz | shooting star | entra | excepción 1 lección |
| harami | harami | entra | excepción 1 lección |
| vela verde / roja | green / red candle | entra | |
| agregado | aggregate | fuera | explicación, no término |
| orden stop | stop order | entra | |
| bracket | bracket | entra | |
| ejecución | fill / execution | entra | |
| cotización | quote | entra | |
| creadores de mercado | market makers | entra | |
| arbitraje | arbitrage | entra | |
| arbitrajista | arbitrageur | fuera | redundante con arbitraje |
| iceberg | iceberg | entra | |
| spoofing | spoofing | fuera | 1/1 |
| wash trading | wash trading | entra | |
| compra / venta agresiva | aggressive buy / sell | alias | de g-aggressor |
| tick | tick | entra | |
| deslizamiento | slippage | alias | match ES de g-slippage |
| liquidez | liquidity | entra | |
| libro fino / profundo | thin / deep book | entra | |
| volumen | volume | entra | |
| participación | participation | entra | vigilar en 1.2: preferir "volumen que acompaña" donde encaje |
| confirmación | confirmation | entra | |
| bolsa de liquidez | liquidity pool | prosa-1.2 | colisión con pool de AMM; sustituir por "cúmulo de stops" |
| caza de stops | stop hunt | entra | |
| flujo forzado | forced flow | prosa-1.2 | acuñado; sustituir por "ventas forzadas" / "flujo de liquidaciones" |
| colateral | collateral | entra | |
| exposición | exposure | entra | |
| cobertura | hedge | entra | |
| contraparte | counterparty | entra | |
| sobreapalancado | over-leveraged | entra | |
| posicionamiento | positioning | entra | |
| unilateral | one-sided | entra | |
| futuros trimestrales | quarterly / dated futures | entra | |
| opciones | options | fuera | el curso no las enseña |
| derivados | derivatives | entra | |
| perpetuo | perp / perpetual | alias | match de g-perpetual |
| stop | stop | alias | match de g-stop-loss |
| objetivo | target | alias | match de g-take-profit |
| entrada | entry | entra | |
| salida | exit | entra | |
| ventaja | edge | entra | |
| racha perdedora | losing streak | entra | |
| muestra | sample | entra | |
| pérdida acotada | capped loss | comprobar | never-coins (EN 0); ver tarea |
| asimetría | asymmetry | entra | |
| ganancia / pérdida media | average win / loss | entra | |
| break-even | break-even | entra | |
| sistema | system | entra | |
| plan de trading | trading plan | entra | |
| revisión semanal | weekly review | fuera | 1/1 |
| precompromiso | precommitment | entra | |
| sesgo de retrospectiva | hindsight bias | entra | excepción 1 lección |
| sesgo de supervivencia | survivorship bias | fuera | never-coins (EN 0) |
| look-ahead | look-ahead bias | entra | excepción 1 lección |
| walk-forward | walk-forward | entra | excepción 1 lección |
| dinero real | real money | fuera | sentido cotidiano |
| demo | demo | fuera | sentido cotidiano |
| horas de pantalla | screen time | fuera | 1/1 |
| criterio de abandono | abandonment criterion | fuera | 1/1 |
| sobreoperar | overtrading | entra | |
| exchange | exchange | entra | |
| token | token | entra | |
| baja capitalización | small cap / low cap | entra | |
| alt | alt | alias | match de g-altcoin |
| alt season | alt season | fuera | 1/1 |
| ETH/BTC | ETH/BTC | fuera | 1/1 |
| refugio / oro digital | safe haven / digital gold | fuera | 1/1 |
| publicación macro | macro release | fuera | 1/1 |
| IPC | CPI | entra | |
| vesting | vesting | entra | |
| oferta total | total supply | entra | |
| dilución | dilution | fuera | 1/1 |
| autocustodia | self-custody | entra | |
| clave privada | private key | entra | |
| not your keys | not your keys | entra | |
| listado | listing | entra | |
| sentimiento | sentiment | entra | |
| pánico | panic | fuera | sentido cotidiano |
| masa / multitud | crowd | entra | |
| prima de Coinbase | Coinbase premium | fuera | 1/1 |
| indicador | indicator | entra | |
| línea de cero | zero line | entra | |
| serie temporal | time series | entra | |
| microestructura | microstructure | fuera | 1/1 |
| heatmap | heatmap | fuera | 1/1 |
| instancia generada | generated instance | entra | vocabulario de la app, no del oficio |
| confluencia (lente) | lens | prosa-1.2 | acuñado; sustituir "lente" por "lectura" / "forma de leer el gráfico"; confluencia ya existe |

## Totales

- entra: 83 (7 por la excepción de 1 lección)
- alias / acepción: 13
- prosa-1.2: 5 (escalera, repisa, flujo forzado, bolsa de liquidez, lente)
- comprobar: 1
- fuera: 23

## Para el inventario P0 del pase 1.2

Nuevo patrón: **términos acuñados por el curso**. Semilla: lente, escalera, repisa, flujo forzado, bolsa de liquidez (sentido stops), participación (vigilar). El agente debe buscar más del mismo tipo: palabras que el curso usa como término sin que existan fuera con ese sentido.
