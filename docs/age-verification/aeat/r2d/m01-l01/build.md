# Build — I.1 (`m01-l01`), R2d, 2026-11-17

Script: `…/scratchpad/b-m01-l01/build.py` (pool walk: the pool text minus the dropped sentences, HEAD forms restored where the pool form has no PASS, lists turned into esquemas; the only new text is one «Normativa» line edit).

## Size

| | words |
|---|---|
| HEAD, excluding esquema rows | 5,198 (wc -w 5,843 with the HEAD rows, 616 in directive/rows) |
| Built, excluding esquema rows | 11,992 (esquema rows 2,635) |

Ratio to HEAD (excl. rows): 2.31. Ratio to the 1.6 target (8,317): 1.44. Above target: about 110 articles of the range (títulos preliminar, I, IX, X; LOTC arts. 16–26, 33, 41–44, 56–79) now give their rule, conditions and exceptions, the 128–136 and 39–52 CE articles one apartado each, and 11 enumerations became esquemas.

## Sentences added (not in HEAD): 243 prose + 69 esquema rows (rows from items / sub-items)

- (a) R2b removals: none in the map.
- (b) Review items: none confirmed as content (item 4 and 10 are glossary, step 4).
- (c) Articles HEAD did not treat or treated in part: all added sentences below except (d)/(e): CE 2 (patria común), 3.2–3.3, 4.1–4.2, 6–7, 8.2, 9.2, 10.1, 11.1, 11.3, 13.1, 13.3, 13.4, DA 2.ª, 15–16, 17.1/17.3, 18, 19, 20.1/20.3–4, 22, 23, 24–26, 27–29, 30–38, 39–48, 50–52, 128–132, 135–136, 55.2 párr. 2, 116.1–6, 159.4 párr. 2, 161.1.a, 162.2, 164, 165; derogatoria 1 (laws), 2; LOTC 2.1–2.2, 16–17, 19–26, 27.2, 32–33, 41–44, 46, 49–50, 56–58, 59–79 and the título list.
- (d) «No confundir»: 2 blocks (55.1 / 55.2 CE; 33.1 / 76 LOTC), 4 sentences, as in the pool.
- (e) HEAD sentences replaced by the pool form: derogatoria 1 sentence (HEAD «entre otras» removed; now the lead-in and an esquema), «Sección 1.ª» heading label, capítulo III paragraph (HEAD «entre otros» removed; materias esquema), «Lo que más cae» art. 159.4 line (complete list).
- Normativa: pool lines copied; the CE line edited (disposición derogatoria 1–2 instead of 1–3) and the LO 4/1981 line removed.

## Enumerations as esquemas (11)

Derogatoria 1 (6 rows), 20.1 CE (a–d), 24.2 CE (8), materias arts. 39–52 CE (14), 2.1 LOTC (10 incl. d) bis, e) bis), 19.1 LOTC (7), 23.1 LOTC (7), 33.2 LOTC (a–c, b with two rows), 44.1 LOTC (a–c), 59.1 LOTC (a–c), 75 ter.1 LOTC (a–c); 20.1 and 24.2 keep their whole bullet (rows are verbatim sub-items). Already in the pool as esquemas: 53 CE, Regencia, 167–168 CE, 27.2, 46.1, 50.1 LOTC. HEAD flat lists (62, 63, 64.1, 159, 161.1, 162.1 CE, estados table) stay.

## Pool sentences left out (each states no rule, condition or exception, or has no PASS)

Left out although verified: 25.2 LOTC (haber pasivo computation: development of 25.1), 75 quinquies.2 LOTC (traslado and personación periods: procedure).
Left out because no PASS (restored to HEAD form where HEAD had the sentence): preámbulo content paragraph; disposición derogatoria 3 CE; 17.2 CE clause «para la realización de las averiguaciones tendentes…» (HEAD form kept); 37.1 CE «así como la fuerza vinculante de los convenios» (HEAD form kept); 49.1 second sentence and 49.2 CE (4 sentences); the LO 4/1981 block (11 sentences, not an article of the range); 18 LOTC «Los más de quince años…»; 9.1, 9.2, 9.4 LOTC expanded sentences (HEAD paragraph restored); 27.1 LOTC; 50.2 LOTC.

## Pool gaps (articles of the range with no PASS sentence)

preámbulo content; disposición derogatoria 3 CE; 17.2 clause, 37.1 clause, art. 49.1 second sentence and 49.2 CE; 9.1/9.2/9.4 LOTC details; 18 LOTC clause; 27.1, 50.2 LOTC; LOTC arts. 3, 4, 6.2, 7.2–7.3, 8, 10, 11–15, 28–31, 34–40, 47, 48, 51–55, 80–95 (chapter level only, via the título line).

## «not in pool» (build_check, 15 lines)

- 27.2 LOTC: lead-in «Son susceptibles de declaración de inconstitucionalidad…» and rows a)–f) (7 lines); 46.1 LOTC: lead-in, 4-column header, rows a), b) (4 lines); 50.1 LOTC: lead-in and rows a), b) (3 lines). Kept only because dropping them leaves a legal enumeration incomplete.
- l.910 «Normativa» CE line (edited: derogatoria 1–2).

## Checks

- build_check: `m01-l01: HEAD 285 · added byte-identical 243 · esquema rows from items 69 · not in pool 15`.
- cites.py: 450 citations, 0 unresolved.
- split_paragraphs: 2 paragraphs split.
- Esquema row citations checked against the prose before writing (scratch check, 0 problems). index_sources: see final message.

## Sentences that do not stand on their own where they now sit

- «Estas libertades tienen su límite…» (20.4 CE, bullet «Medios de comunicación y límites»): «estas libertades» refers to 20.1, which is in the previous bullets.
- «Lo anterior se entiende sin perjuicio…» (33.3 LOTC): follows the 33.2 esquema.
- «…la Sala, o la Sección en el supuesto del artículo 52.2…» (56.2 LOTC): art. 52.2 LOTC is not in the lesson.
- «Los capítulos»/other LO 4/1981 references: removed with the block.
