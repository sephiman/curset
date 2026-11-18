# Build — `m01-l05` (I.5), R2d, 2026-11-17

## Size
- Words (wc -w), HEAD 9880 (its three small esquemas included) → built 21116 excluding every table row; the 274 new esquema rows add about 7500 words of
  text (about 11500 with the Cita cells and the HEAD tables). Ratio to HEAD (excl. rows) 2.14; to the 1.6 target (15808) 1.34. Over the target on
  purpose: 46 legal enumerations are now esquemas (completeness wins) and about 60 articles that HEAD left out are added.
- 46 new esquemas, header `| Elemento | Contenido | Cita |`; a row per item; a second, third… sentence of an item is its own row
  labelled «x) (cont.)» (the checker only accepts one verified sentence per row).

## Sentences added by category
- (a) R2b removals: 0 (the map found none).
- (b) review item 3 (art. 33.1 adscripción): 1 sentence. The «(hoy: …)» link for arts. 33.1 and 37.1 is not in the pool: not written.
- (c) articles HEAD left out or treated in part: 379 prose sentences + 274 esquema rows (rule, conditions, exceptions; every enumeration whole).
- (d) «No confundir»: 3 blocks, 8 new sentences (the three HEAD sentences stay).
- (e) pool form replaces a HEAD sentence: 108→art. 12.2 LPAC sentence; 2.1 a)–g) paragraphs→esquema; 26.2 paragraphs→esquemas; art. 28, 29.1, 29.2,
  29.3, 38.1, 38.2 paragraphs→esquemas; art. 9.1 RGPD, 15.1, 17.1 RGPD lead-ins; 18.1 a); the «Supresión» row of the
  esquema «Algunos derechos del interesado»; Normativa lines (6 new lines, below).
- Esquema «Algunos derechos del interesado» keeps its title: it says «algunos» and every right is in the body (audit). Not edited otherwise.

## Pool sentences left out (they state no rule, condition or exception)
- Development/definition: +9, +10 (art. 2.a), +85 (11.1.i), +118, +119, +121 (21.2.c, d), +270, +272, +273 (54.3-54.5 how to preserve), +305
  (definición de digitalización), +308 (27.3.d publicity), +280 (26.1 definition, also no PASS), +728 (6.3 «entre otras» list), +775 (10.2 LOPDGDD registro).
- Organisational / AGE detail: +68, +72, +103 (7.5), +129 (60.3), +133, +141, +142, +144-+146 (61-62), +177, +225, +232, +236, +263, +264, +292, +297,
  +298, +328, +331, +807, and art. 48 RD +314-+320 (map: organisational).
- Kept although borderline because a neighbour sentence needs their citation: +136, +271, +327, +333, +771, +809.

## Enumerations as esquemas (46)
2, 4, 10.2, 11.1, 11.2, 21.2, 31.1, 8.1, 37.3, 38.1, 40.3, 50.1, 61.2 RD 203/2021; 16.4, 26.2, 27.3 LPAC; 2.1, 7, 8.1, 11, 15.3, 21.2,
26.2.a), 26.2.b), 28, 29.1, 29.2, 29.3, 30.5, 30.8, 38.1, 38.2 Ley 19/2013; 6.3, 6.4, 9.2, 13.1, 13.2, 14.1, 14.2, 14.3, 14.5, 15.1, 17.1, 23.1,
23.2 RGPD; 11.2, 11.3 LOPDGDD. Lists already in HEAD (14.2 LPAC, 3, 14.1, 18.1 Ley 19/2013 …) stay as HEAD lists; the 18.1 RGPD list stays a list
(three HEAD items + the pool's corrected a)). Two embedded citations (2.1.f, 2.1.g, 38.2.e) are cut from the row text (a verbatim part of the
verified sentence) so the esquema cites only units the prose cites.

## Checks
- build_check: `m01-l05: HEAD 319 · added byte-identical 387 · esquema rows from items 274 · not in pool 16`.
- cites.py: 745 citations, 0 unresolved. split_paragraphs: 0 split. index_sources: see the coordinator (no error naming the lesson when run).

## «not in pool» (16)
- 10 rows with no PASS verdict, kept because dropping them breaks a complete enumeration: art. 16.4 LPAC a)–e) and art. 26.2 LPAC a)–e). Need a blind check.
- 6 new Normativa lines: Ley 40/2015, RD 203/2021, Ley 39/2015, CE, LGP, and the closing «nombrados en …» line (art. 59.2 LRJSP, art. 48 RD, RD 1164/2002,
  art. 54.5 and 62.3 dropped because the built lesson no longer cites them).

## Pool gaps
None: every article of the ranges has pool sentences. Missing in the pool, not written: «(hoy: …)» for arts. 33.1 and 37.1 Ley 19/2013.

## Sentences that do not stand on their own where they now sit
- «(cont.)» rows: art. 2.1.i) «Se incluyen los órganos de cooperación…» and «En estos casos…»; art. 8.1.a) and b) continuations; art. 14.5.b) «En tales casos…»;
  art. 26.2.b).6.º «En el caso de obsequios…»; art. 38.1.d) «Para ello, elabora…»; art. 38.2.e) «El órgano competente debe motivar…»; art. 50.1.b) «Los sellos
  electrónicos de tiempo no cualificados…»; art. 11.2 LOPDGDD b) continuations.
- Prose: «Se incluyen…», «Esta obligación se extiende…» (art. 4 Ley 19/2013), «Este plazo es al menos de cinco años» (needs the previous sentence, kept).
