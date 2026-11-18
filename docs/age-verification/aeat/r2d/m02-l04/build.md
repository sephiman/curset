# Build — `m02-l04` (II.4), 2026-11-17

## Size
Words HEAD → built, esquema rows excluded: 2372 → 8700 (ratio 3.67; 2.29 of the 1.6 target, i.e. over target). Esquema-row words: 480 → 2117.
Over target because the range holds 54 articles, 24 of them not treated at HEAD, and each got its rule/conditions/exceptions sentences; every enumeration is a complete esquema. Nothing was cut for size.

## Sentences added by category
(a) none (no R2b removal in this tema). (b) review items 2, 3, 4, 5, 6: art. 56.1–56.3 (principios, quién, plazo, a)–i)), art. 66.1 a)–f) (the «entre otros datos» sentence is gone), 66.2, 66.4, 68.3–68.4, art. 69.1–69.4 and 69.6, 77.1–77.7 with 77.3 bis, 78.1 and 78.3, 86.1–86.5, 98.1 a)–d), 98.2 a)–d), 101–105. (c) arts. 54, 55, 59, 60.2, 61.1, 62.4, 63.1–63.3, 64.1–64.3, 65, 67, 70.2–70.3, 71, 72.1, 73, 75.1–75.4, 76.1–76.2, 79.1, 80.2–80.4, 81.1–81.2, 82.1–82.5, 83.1–83.4, 84.2, 87, 88.2, 88.3, 88.5–88.7, 89.1–89.2, 90.1–90.4, 91.1, 91.3, 92, 93, 94.1, 94.3, 94.5, 95.1–95.4, 96.4, 96.6 a)–h) and the dictamen paragraph, 96.7, 97, 100.3. (d) three «No confundir» blocks. (e) none usable: the pool's art. 74 version («incluso las que se refieran a la nulidad de actuaciones») is not PASS, so HEAD's art. 74 sentence stays in both places; the 56.1 principios sentence from the pool is added beside HEAD's 56.1. Added byte-identical 156, esquema rows from items 53 (HEAD sentences 93).
«Lo que más cae»: HEAD's ten lines, unchanged. «Normativa»: rebuilt from what the lesson cites.

## Enumerations as esquemas
56.3 (9), 64.2 (6), 66.1 (6), 89.1 (5), 90.3 a)–b) 1.º–2.º (3), 96.6 (8), 98.1 (4), 98.2 (4, verbatim parts of the inline sentence), 103.1 (3, same), arts. 101–104 (10 rows, verbatim parts of the four bullets). Kept as in HEAD/pool: 100.1 (bullet list a)–d), already whole), 58 and 84.1–2 (whole, in prose), the «Algunos plazos» esquema (pool version, with the 77.2 extraordinario, 73.1 and 73.2 rows added).

## build_check
`m02-l04: HEAD 93 · added byte-identical 156 · esquema rows from items 53 · not in pool 7`. cites.py: 280 citations, 0 unresolved.

## «Not in pool» lines (7)
- Two new «Normativa» lines: the LPAC line (rebuilt for the sentences kept) and the LRJSP line (art. 34 named only in 86.5 now).
- Five esquema rows, art. 89.1 a)–e): the pool's list items have no PASS verdict (the lead-in sentence does). Kept because dropping them breaks a complete enumeration (89.1 a)–e)).

## Pool sentences left out, with reason
- art. 55.2 second sentence (organs that carry out the actuaciones previas), 61.3 and 61.4 (content of the petición razonada), 66.1 last párrafo (oficinas facilitan el código), 66.3 (recibo), 66.5 (comprobaciones automáticas), 69.5 (published models), 72.2 (plazo in the communication), 78.2 (place, date, hour, técnicos), 79.2 (concretar extremos), 88.4 (electronic resolution), 89.3 (contents of the propuesta), 91.2 (contents of the resolución, repeats 81.2): procedure or development, no rule, condition or exception.
- Pool art. 74 sentence with «incluso las que se refieran a la nulidad de actuaciones», pool «Lo que más cae» lines for 56.1, 56.4, 77.2 and the pool's «Lo que más cae» art. 74 line: not PASS or not category (e); HEAD's lines kept.
- The pool's own «Medios de ejecución forzosa» esquema (cells paraphrased, not verbatim) is replaced by rows whose cells are verbatim parts of the bullets.

## Pool gaps
No article of the range lacks a PASS sentence. Art. 89.1 a)–e) items are not PASS as items (see above); art. 74's «incluso las que se refieran a la nulidad de actuaciones» clause is in the pool but not PASS, so it is missing from the lesson (map flag from the audit stays open).

## Sentences that do not stand alone where they now sit
- Bullets under art. 69: «La resolución que declare tales circunstancias…» (refers to the 69.4 sentence before), «Las declaraciones responsables y las comunicaciones…» (needs the two definitions above).
- Bullets under art. 86: «Esos instrumentos deben establecer…», «Requieren en todo caso…» and «Los acuerdos que se suscriban…» refer to the 86.1 paragraph.
- «En todo caso, esas medidas quedan sin efecto…» (56.2) and «Esa suspensión cautelar…» (the 90.3 lead-in) refer to the sentence before.
- «En ambos casos es necesario que el denunciante cese…» (62.4) refers to the two preceding 62.4 sentences.
- Esquema rows with lower-case starts («hay lugar a ella cuando…», «puede liquidarse de forma provisional…», «los actos administrativos que impongan…») are verbatim parts of the bullets and read as continuations of their Medio cell.
- «Estos, en un plazo no inferior a diez días…» (HEAD, 82.2) refers to the sentence before.
