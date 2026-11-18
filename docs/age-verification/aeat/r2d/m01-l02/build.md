# Build — I.2 (`m01-l02`), R2d build pass, 2026-11-17

Builder: Sonnet. Base: `git show HEAD:…/m01-l02.md`; built from the verified pool `expansion/m01-l02.md` by dropping
unselected sentences (script, scratch `b-m01-l02/build.py`) and turning every verified list into an esquema.

## Size

| | words (excl. esquema rows) | esquema-row words |
|---|---|---|
| HEAD | 7299 | 1210 |
| Built | 14154 | 4842 |

Ratio to HEAD (excl. rows): 1.94. Target 1.6 × 7299 = 11678: built is 1.21 × the target. Over the target on purpose:
the chapter-level lists of the Reglamentos, LO 3/1981, LOPJ and Ley 38/1988 (about 3400 words) are the only
treatment the pool gives to hundreds of articles, the iniciativa legislativa popular (LO 3/1984) and the LOREG
composition rules are new sources of the pool, and arts. 88–89 / 93–96 CE and RC 108–123 are articles the map
lists as «not treated».

## Sentences added (pool PASS or N), by category

| Category | Sentences |
|---|---|
| (a) R2b removals in range | 0 (the map found none) |
| (b) confirmed review items (1 tramitación: arts. 88–89 CE, RC 108–123; 3 control del Gobierno arts. 108–111; 4 art. 134) | 45 |
| (c) articles of the range not treated or treated in part (CE 68.5, 70.2, 72.2, 76–78, 82–86, 92–96, 117–127; LO 3/1981 DF; LOPJ 560–561, 57, 65, 439 ter; LOREG 162–166, 6, 154–155; LO 3/1984 arts. 1–15; EOMF 2; chapter lists) | 239 |
| (d) «No confundir» blocks (71 CE; 90.2 CE / 74.2 CE; art. 2.4 LO 3/1981 / art. 567.2 LOPJ) | 14 |
| (e) pool versions replacing HEAD sentences (560.1 list, 561 lead-in, 630.1, 57.1, 65.1.º lead-in) | 65 |

Counts include esquema rows (93) and the 13 pool Normativa lines (all PASS; no new Normativa line written). HEAD
sentences replaced and removed: the six-item list of art. 560.1 and its lead-in, «El Consejo informa …» (561),
the two «El nombramiento …» sentences (630.1), «La Sala de lo Penal instruye … los demás cargos que enumera la ley»
(57.1), «La Sala de lo Penal de la Audiencia Nacional conoce … fuera del territorio nacional» (65.1.º), and the
old Normativa lines.

## Enumerations as esquemas (verified items, one row per item, citation of the lead-in)

LOREG 163.1 (a–e; items c and d split in two rows, as the splitter cuts them), LOREG 6.1 (a–p), LOREG 6.2 (a–b),
art. 83 CE, art. 94.1 CE (a–e), art. 2 LO 3/1984 (5), art. 5.2 LO 3/1984 (a–e), art. 108 RC (5), art. 560.1 LOPJ
(25), art. 561.1 LOPJ (9), art. 57.1 LOPJ (5), art. 65.1.º LOPJ (a–g); the pool's own esquemas kept: art. 82.1 RC,
art. 46.1 RC (23), art. 7.1, 10.1, 30.1 LO 3/1981. Their headers changed to `| Elemento | Contenido | Cita |` (a
header the pool holds). Every row's citation cell is the unit its lead-in sentence cites.

## build_check

`m01-l02: HEAD 345 · added byte-identical 229 · esquema rows from items 93 · not in pool 55`

`cites.py`: 723 citations, 0 unresolved. `index_sources.py --course aeat-agentes-hacienda`: see the final report.
`split_paragraphs`: 9 paragraphs split.

## «Not in pool» (55 lines, kept because dropping them breaks an article's rule or a complete enumeration)

| Lines | What | Why kept |
|---|---|---|
| lead-in + 4 rows | RC 82.1 clases de votación | enumeration RC 82 (map: incomplete); work item 6 |
| lead-in + 23 rows | RC 46.1 Comisiones Permanentes Legislativas | enumeration RC 46.1 (map: incomplete) |
| 2 sentences | art. 82.3 CE «No podrá entenderse concedida de modo implícito…», «Tampoco podrá permitir la subdelegación…» | the exceptions of 82.3 (map row) |
| lead-in + 2 rows | art. 83 CE a)–b) | map enumeration (not treated otherwise) |
| 1 | art. 86.3 CE (urgencia) | map row |
| 1 | art. 108 CE | only rule of the article |
| 2 | art. 134.1 and 134.4 CE | map review item 4 |
| lead-in + 6 rows | art. 7.1 LO 3/1981 | enumeration (map: incomplete) |
| lead-in + 3 rows (5–7) | art. 10.1 LO 3/1981 (rows 1–4 pass through HEAD or other pools) | enumeration (map: incomplete) |
| lead-in + 4 rows | art. 30.1 LO 3/1981 | enumeration (map: incomplete) |
| 1 | disposición final única LO 3/1981 | audit problem: no sentence |

Left out from the pool: the N sentences «Las Cortes Generales controlan la acción del Gobierno (art. 66.2 CE).»
(repeats art. 66.2), art. 110.1 CE «Las Cámaras y sus Comisiones pueden reclamar la presencia…» (art. 110 is
stated by 110.2) and the «Voto telemático» lead-in plus a)–g) rows (art. 82.2 RC; a list of circumstances outside
the map's enumerations). Every PASS sentence of the pool is in the built lesson (as prose or as an esquema row).

## Pool gaps (no rule sentence in the pool)

1. Chapter level only (87 map rows, marked «chapter level» in the map): RC 1–9, 15–19, 54–55, 61–77, 90–94,
   99–107, 124–125 and 127–129, 130–169, 180–207; RS 20–26, 35–48, 96–159 (except 53.2, 55, 93.1), 160–196; LO 3/1981
   4, 9, 12–14, 16, 19–31 (except 30.1), 33; LOPJ 4 bis, 5–8, 10–20, 21–25, 27, 29, 35–36, 38–52, 55 bis, 56, 59–61,
   64 bis, 66–69, 71, 73–79, 82, 82 bis–83, 85–94, 96, 102–103, 104, 298–301, 378–388, 389–397, 398–401, 405–427,
   547–550, 292–297, 559, 562–565, 570 bis–578, 579–584 bis, 590–593, 596–598 bis, 601–610 ter, 638–642; Ley 38/1988
   2 bis–10.
2. Apartados the map names as missing that stay at chapter level: RC 11–13, 14.1, 20–21, 25.2–29, 31–32, 39.2–3, 40,
   42, 44–45, 51–53, 56–59, 78–79, 88; RS 1–19 (except 5.1), 28.2–3, 29–34, 49–68 (except 53.2, 55), 69–100 (except
   93.1); LO 3/1981 2.6, 5.4, 6.1–6.2, 6.4, 7.3, 8.3–8.4, 11.3, 17.1–17.2, 18.2; LOPJ 2.2, 3.2, 9.1, 31, 32.2, 63.1, 64.2,
   80.2–3, 81.2–3, 100.1, 101.3, 558.2, 567.2 párr. 2, 567.3, 567.6, 568.2, 569.1, 570.1, 589.1, 599.1 (2.ª–17.ª), 629,
   631–637; Ley 38/1988 2.1–2.4. (Read from the pool's citations; a grep per article would confirm.)

## Sentences that do not stand on their own where they now sit

Each depends on a neighbour that is present: art. 76.1 «Sin perjuicio de lo anterior…» and 76.2 (after the
comparecencia sentence); art. 77.2 «El Gobierno está obligado a explicarse sobre su contenido…» (after 77.2 first
sentence); 78.4 «Reunida la Cámara correspondiente…»; art. 82.3 «La delegación se agota…», «No podrá entenderse…»,
«Tampoco podrá…» (after the first sentence of 82.3); art. 86.2 «Los Decretos-leyes deberán ser inmediatamente…»,
«El Congreso habrá de pronunciarse … dicho plazo» and 86.3 «Durante ese plazo…»; art. 95.2 «esa contradicción»; 96.1
«Sus disposiciones…»; LO 3/1984 7.1 «Este plazo puede ser prorrogado…» and «Agotado el plazo…»; RC 110–123 sentences
that start «Si…», «Las enmiendas…», «Concluido el informe…»; art. 124.2 «Ejerce sus funciones…» and EOMF 2.2 «esta
denominación»; art. 561.2–4 «El Consejo emite su informe…», «Si en la orden de remisión…», «El Gobierno remite dicho
informe…»; art. 439 ter.2 «En ella el juez o jueza de paz…»; LOREG 162.3 «Los doscientos cuarenta y ocho Diputados
restantes…»; 166.1 «Son proclamados electos…»; «Sus capítulos regulan:» (after each «El Reglamento … se ordena en …»);
the first sentence under «El control del Gobierno» now opens with «estos medios de control» (its lead-in sentence on
art. 66.2 is left out).

## Normativa

Rebuilt from the pool's lines (all PASS): CE arts. 54, 66–96, 108–111, 117–127, 134, 145 y 158; the «nombrado en»
CE line (arts. 18, 131, 168); reforma de 19-05-2026; RC 1–207; RS 1–196; LOREG 6, 154–155, 162–163, 165–166; LO
3/1984 1–7, 9, 13–15; EOMF 1–11; LO 3/1981 1–37; LOPJ 1–434, 439 ter, 547–550, 558–642; Ley 38/1988 1–40, 53–64;
LO 1/2025; LOTC; RD 2917/1981 and Reglamento (UE) 2017/1939 (not in `normativa.yaml`). No new text.
