# Excerpt verification — report, part 7 (items 238–287, bloque VI, fresh sample after the sample-6 fixes)

Blind opus verifier, `sample-7.jsonl`: 50 at random (seed 20261031) from bloque VI, none in samples 1–6. Saved by the
coordinator from the verifier's returned text.

Counts: **yes 44 · full-only 0 · no 6** (240, 260, 263, 265, 271, 280): miss rate 12 %. Extractor flags: 255 (serious),
243; minor run-ins 251, 274, 287; source garbles 244, 262, 277, 283.

| n | key | verdict | note |
|---|---|---|---|
| 238 | m06-l03-ex-8/m06-l03-q302 | yes | |
| 239 | m06-l03-ex-2/m06-l03-q045 | yes | |
| 240 | m06-l08-ex-2/m06-l08-q036 | no | Right section, wrong paragraph: the first paragraph of «Proving the Ideas» (DARPA contracts); the Mockapetris/DNS sentence is a later paragraph. |
| 241 | m06-l07-ex-8/m06-l07-q251 | yes | |
| 242 | m06-l04-ex-6/m06-l04-q219 | yes | |
| 243 | m06-l01-ex-6/m06-l01-q174 | yes | Flag: excerpt repeats the heading «Seis componentes clave de VDI»; none of the section body taken. |
| 244 | m06-l06-ex-1/m06-l06-q009 | yes | Garble from the source. |
| 245 | m06-l01-ex-3/m06-l01-q066 | yes | |
| 246 | m06-l03-ex-1/m06-l03-q003 | yes | |
| 247 | m06-l03-ex-3/m06-l03-q057 | yes | |
| 248 | m06-l05-ex-6/m06-l05-q222 | yes | |
| 249 | m06-l03-ex-10/m06-l03-q373 | yes | |
| 250 | m06-l06-ex-9/m06-l06-q349 | yes | |
| 251 | m06-l02-ex-5/m06-l02-q153 | yes | Minor: two list items joined with no separator. |
| 252 | m06-l01-ex-9/m06-l01-q311 | yes | |
| 253 | m06-l08-ex-3/m06-l08-q065 | yes | |
| 254 | m06-l06-ex-4/m06-l06-q124 | yes | |
| 255 | m06-l08-ex-1/m06-l08-q025 | yes | Flag, serious: the splitter broke at «S.» (S. Crocker) and glued «In 1969 a key step was taken by S.» onto the Postel sentence: reads as a false statement. |
| 256 | m06-l06-ex-5/m06-l06-q157 | yes | |
| 257 | m06-l01-ex-2/m06-l01-q048 | yes | |
| 258 | m06-l03-ex-5/m06-l03-q145 | yes | |
| 259 | m06-l03-ex-11/m06-l03-q392 | yes | |
| 260 | m06-l01-ex-7/m06-l01-q205 | no | Page intro sentence plus a stray table-of-contents word; the fact is a table row under h2 «Funcionalidad». |
| 261 | m06-l06-ex-3/m06-l06-q057 | yes | Cosmetic: starts with the table label. |
| 262 | m06-l05-ex-6/m06-l05-q220 | yes | Source wording. |
| 263 | m06-l02-ex-7/m06-l02-q247 | no | The cited section is only link titles; the fact is in the page's lead sentence. |
| 264 | m06-l08-ex-3/m06-l08-q055 | yes | |
| 265 | m06-l04-ex-6/m06-l04-q225 | no | Stops at «Seleccione una imagen.»; the step naming the checkbox («active la casilla Permitir solapamientos») comes three lines later. |
| 266 | m06-l07-ex-2/m06-l07-q040 | yes | |
| 267 | m06-l04-ex-4/m06-l04-q142 | yes | |
| 268 | m06-l08-ex-6/m06-l08-q155 | yes | |
| 269 | m06-l06-ex-8/m06-l06-q306 | yes | |
| 270 | m06-l03-ex-2/m06-l03-q040 | yes | |
| 271 | m06-l01-ex-9/m06-l01-q307 | no | Wrong paragraph; the fact is in the page's lead («Puede usar la aplicación Seguridad de Windows para ver y administrar el estado de Firewall de Windows»). |
| 272 | m06-l01-ex-3/m06-l01-q068 | yes | |
| 273 | m06-l05-ex-2/m06-l05-q021 | yes | |
| 274 | m06-l02-ex-5/m06-l02-q155 | yes | Minor: two paragraphs joined with no separator. |
| 275 | m06-l06-ex-9/m06-l06-q352 | yes | |
| 276 | m06-l05-ex-1/m06-l05-q009 | yes | |
| 277 | m06-l05-ex-8/m06-l05-q256 | yes | Source garble. |
| 278 | m06-l06-ex-12/m06-l06-q430 | yes | |
| 279 | m06-l04-ex-2/m06-l04-q032 | yes | |
| 280 | m06-l05-ex-5/m06-l05-q130 | no | Only the first two sentences of a ~110-word paragraph; the fact needs the next ones («fila absoluta toma la forma A$1», «la relativa cambia y la absoluta no»). |
| 281 | m06-l04-ex-4/m06-l04-q151 | yes | |
| 282 | m06-l04-ex-7/m06-l04-q248 | yes | |
| 283 | m06-l04-ex-5/m06-l04-q211 | yes | Source wording. |
| 284 | m06-l07-ex-10/m06-l07-q328 | yes | |
| 285 | m06-l04-ex-8/m06-l04-q313 | yes | |
| 286 | m06-l04-ex-5/m06-l04-q163 | yes | |
| 287 | m06-l02-ex-1/m06-l02-q021 | yes | Minor: adjacent `<strong>` elements joined without a space (no whitespace in the source HTML). |

## Misses and flags by cause (verifier's grouping)

- Wrong paragraph inside the right unit: 240, 271.
- Cut before the fact, the two-sentence window too short: 265, 280.
- Citation unit holds no prose (page title / links-only section), no fallback: 260, 263.
- Garbled by the extractor: 255 (splitter on «S.»), 243 (heading only), 251, 274, 287 (run-ins).
- Garbled in the source: 244, 262, 277, 283.
