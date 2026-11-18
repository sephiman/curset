# Build — I.6 (`m01-l06`), R2d, 2026-11-17

Script: `…/scratchpad/b-m01-l06/build.py` (pool walk: the pool text minus the sentences with no PASS; lists of legal enumerations turned into esquemas; the only new text is the «Normativa» edits).

## Size

| | words |
|---|---|
| HEAD, excluding esquema rows | 4,018 (wc -w 4,601 with the HEAD esquema rows, 583) |
| Built, excluding esquema rows | 21,267 (esquema rows 14,448; wc -w 35,715) |

Ratio to HEAD (excl. rows): 5.29. Ratio to the 1.6 target (6,429): 3.31. Far above target, by design of the brief: the range is six whole laws (about 440 articles); every article has its rule, conditions and exceptions sentences, every legal enumeration is complete as an esquema (42 esquemas, 14,448 words in rows), and nothing was left out for size. The prose itself is mostly the chapter-level bullet lists (one line per article) and the per-article sentences of the pool.

## Sentences added (not in HEAD): 593 prose + 405 esquema rows (a row counted even where its text is a HEAD item)

- (a) R2b removals: none in the map.
- (b) Review items (2 ayudas of art. 27 LO 1/2004; 3 tutela judicial, LOPJ art. 89 and LO 1/2004 arts. 61–69; 4 Consejo Nacional de la Discapacidad, art. 55 RDL 1/2013; 5 PIA, art. 29 Ley 39/2006; 6 revisión del grado, art. 30 Ley 39/2006; 7 Estrategia Estatal, art. 34 Ley 15/2022): 88 units (54 prose, 34 rows). Item 1 (the lesson is short) and the glossary items (9–11) are not content.
- (c) Articles HEAD did not treat or treated in part: 903 units (all the rest of the added prose and rows): LO 3/2007 arts. 1–2, 4–5, 6.3, 7.3–7.4, 8–9, 11.2, 12.1–12.3, 13–22, 23–44 (chapter level), 45.1–45.5, 46–48.1, 50.1, 51–52, 56–59, 60.2, 61–63, 64, 65–75, 77–78; LO 1/2004 arts. 1.2–1.4, 2–9, 11, 13–19, 20.2–20.7, 21–23, 25–26, 28, 28 bis, 28 ter, 29.1–29.3, 30.3, 31–32; Ley 15/2022 arts. 1, 2.2–2.4, 3–8 (5.1–5.2 only), 9.1–9.6, 10–33, 35–54 (gaps below); RDL 1/2013 arts. 1, 2 (a–t), 4.1–4.4, 5–41, 43–54, 57–94, 95.2–95.3, 96–105; Ley 39/2006 arts. 1.2, 2–4, 5.1.b) and i)–ii), 5.3–5.4, 6, 8–25, 26.2, 27, 28.3–28.7, 31–47, DF 1.ª.2–3.
- (d) «No confundir»: 3 blocks (7 sentences besides the labels), as in the pool: Delegación / Observatorio (arts. 29.1 and 30.1 LO 1/2004); persona con discapacidad / situación de dependencia (art. 4.1 RDL 1/2013, art. 2.2 Ley 39/2006); PIA / grado (arts. 29.3 and 30 Ley 39/2006).
- (e) HEAD sentences replaced by the pool form: the art. 54 LO 3/2007 sentence (l. 73 of HEAD, «…observan el principio…» → «…observarán… nombramientos que le corresponda efectuar…»); «Son infracciones graves, entre otras (art. 95.3 RDL 1/2013):» (now «Son infracciones graves (art. 95.3 RDL 1/2013):», items a)–i) complete); the «Lo que más cae» line «Entre los principios…» (art. 3 RDL 1/2013); five «Normativa» lines rebuilt (LO 3/2007, LO 1/2004, Ley 15/2022, RDL 1/2013, Ley 39/2006). The HEAD bullets of arts. 3 and 95.4 RDL 1/2013 and 95.3 a), b), h) became esquema rows with the same bytes (label «a)»…, marker out of the cell).

## Enumerations as esquemas (42, all with header `| Elemento | Contenido | Cita |`)

LO 3/2007: 14 (12), 20 (a–f), 46.2 (a–i), 51 (a–g), 62 (a–d), 77 (a–e). LO 1/2004: 2 (a–k), 19.2 (a–g), 28 ter (a–e). LOPJ: 89.5 (a–h), 89.6 (a–k), 89.7 (a–d). Ley 15/2022: 2.4 (a–f), 3.1 (a–o), 34.4 (a–d), 40 (a–r), 47.3 (a–d), 47.4 (a–d), 49.1 (a–j). RDL 1/2013: 1 (a–b), 3 (a–m, letters assigned by order), 2 (other definitions a–t, 18 rows), 95.2 (a–c), 95.3 (a–i), 95.4 (a–h), 105.3 (a–c). Ley 39/2006: 2 (1–17; item 15 split into 15, 15 a), 15 b)), 3 (a–t), 4.2 (a–q), 5.1 (i–ii), 8.2 (a–k), 11.1 (a–h), 13 (a–b), 15.1 (a–i), 29.3 (a–c), 30 (a–b), 33.3 (a–d), 43 (a–i), 44.3 (a–c), 44.4 (a–c), 45.2 (a–f), 47.3 (a–c). Items with several sentences give one row per sentence, same label (the splitter cuts them).
Already esquemas in the pool: «Órganos…» (widened to 13 organs), «Multas por clase…» (arts. 48 Ley 15/2022, 96 RDL 1/2013, 45.3 Ley 39/2006), «Discriminación y acoso por razón de sexo». HEAD/pool lists left as bullet lists: art. 6 Ley 15/2022 (definitions with their own citation per sentence: 6.1.a)…6.8), 26.1 Ley 39/2006 (HEAD list, whole), arts. 48.1 and 48.2 Ley 15/2022 (in the «Multas» esquema too), art. 45.3 Ley 39/2006 (idem), and every chapter-level list (one bullet per article, each with its own citation).

## Pool sentences left out

Left out because they have no PASS verdict (all listed as pool gaps below); no PASS sentence was left out. Nothing was dropped for size.

## Pool gaps (articles or apartados of the range with no PASS sentence, kept out)

- LO 3/2007 art. 50.2, 50.3, 50.5 (balance for the distintivo, reglamento, control and withdrawal; 50.1 treated), 50.4 not in the pool at all.
- LO 1/2004 arts. 10 and 12 (publicidad ilícita, acción de cesación), 21.2 first sentence (desempleo). Código Penal: arts. 148.4.º, 153.1, 171.4, 172.2, 468.2 (two pool sentences, no PASS).
- Ley 15/2022 arts. 5.3, 5.4, 5.5; 41.2 list of norms governing the Autoridad; 46.1 second sentence; 50.2; 52.3.
- Ley 4/2023: arts. 2, 4, 6–8, 44–45, 47–51 and the título/capítulo lines for arts. 10–42 and 52–82 (pool paragraphs with no PASS; coordinator note keeps the lesson's HEAD text for Ley 4/2023). Only HEAD's arts. 1, 3, 5, 9, 43, 46 stand.
- Articles with only a chapter-level bullet in the pool (no rule sentence): see the map «After build» (LO 3/2007 23–33, 35–40, 42–44, 65–72; Ley 15/2022 10–33, 35–39, 42–45, 53–54; RDL 1/2013 5–41, 43–54, 57–72, 74–77, 79–81, 84–93, 99–100, 102–104; Ley 39/2006 34–41).

## «not in pool» (build_check, 6 lines)

- l. 861 «Las demás definiciones del artículo 2 son (art. 2 RDL 1/2013):» — the lead-in of the art. 2 esquema; its verdict is FAIL in verify-recheck-1 (kept: dropping it breaks the complete enumeration of the 20 definitions).
- l. 881 row `| m) | Ajustes razonables: …` — verified neither as a sentence nor as a part; kept for the complete enumeration of art. 2 RDL 1/2013.
- «Normativa» lines (new text): LO 1/2004 (`arts. 1–9, 11, 13–28, 28 bis, 28 ter, 29–32 y 61–69`, arts. 10 and 12 out), Código Penal (`art. 468 y título VIII del libro II, nombrados en el art. 89.5 LOPJ`), the CE line, and the final «… no figuran en `normativa.yaml`» line. The Ley 4/2023 line is HEAD's.

## Checks

- build_check: `m01-l06: HEAD 104 · added byte-identical 647 · esquema rows from items 345 · not in pool 6`.
- cites.py: 1019 citations, 0 unresolved.
- split_paragraphs: 7 paragraphs split.
- index_sources (`--course aeat-agentes-hacienda`): exit 0, no validation error.

## Sentences that do not stand on their own where they now sit

- Bullet «El ente público al que corresponda velar para que los medios audiovisuales…» (art. 11 LO 1/2004): the ámbito introduction («En el ámbito de la publicidad…», art. 10) is out (no PASS).
- Esquema row 33.3.c) Ley 39/2006 («Las cantidades previstas en los apartados 1 y 2…»): art. 33.2 is not in the lesson.
- Row 89.7.b) LOPJ («…apartado 5. a)… apartado 5.h)») and 89.7.a) («apartado 6»): refer to the 89.5 and 89.6 esquemas.
- «Lo dispuesto en el párrafo anterior será también de aplicación durante el período de lactancia natural» (art. 58 LO 3/2007) and «Gozarán de este mismo derecho…» (art. 59): depend on the previous sentence of the paragraph.
- «Sólo excepcionalmente, y mediante informe motivado…» (art. 20 LO 3/2007): follows the art. 20 esquema.
- «Estas ayudas…» (art. 27.3 LO 1/2004) bullets: refer to the art. 27 bullets above.
- «Se considerarán también… Esta asimilación…» (art. 4.2 RDL 1/2013) bullets: continue the 4.2 párr. 1 sentence.
- «En estos casos, el expediente se tramitará de urgencia» (art. 28.7 Ley 39/2006) follows the previous bullet.
- Row 14.12 LO 3/2007 («Todos los puntos considerados en este artículo…») and 6.3.c)–d) Ley 15/2022: refer to the rest of their articles.
