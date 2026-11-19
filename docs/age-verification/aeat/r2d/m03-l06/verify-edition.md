# Blind verify (edition) — `m03-l06`

2026-11-19. Opus verifier. Input: `r2d/m03-l06/pending.md` (7 rows, all «Normativa» lines). Each line compared with
every citation in the lesson as it stands (parentheticals, esquema «Cita» cells, «art. N» and «disposición …»
citations, wrapped lines joined).

Normativa additions (no pending row): the lesson cites the Orden EHA/586/2011 (art. 1.1, l. 293, 429) and has no line
for it: «- Orden EHA/586/2011 (modelo 111): art. 1.1.». Norms named without a line: RDL 29/2026 («redacción del
Real Decreto-ley 29/2026», l. 192, 198, 226), Ley 35/2003 and Real Decreto 1082/2012 (art. 75.3 RIRPF, l. 194; art. 76.2
RIRPF, l. 217), Directiva 2003/41/CE (art. 76.2 RIRPF, l. 220), Código de Comercio (disposición adicional
decimocuarta.1.a) LIS, l. 362), Ley 19/1994 (same, l. 364).

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `e0b1d5eda8` | PASS | Normativa vs. lesson citations (LGT) | listed units match the citations exactly | — |
| `edc8709ac9` | PASS | Normativa vs. lesson citations (RGAT) | arts. 118.1, 119.1, 120.2 cited, none missing | — |
| `e17a1caf52` | PASS | Normativa vs. lesson citations (LIRPF) | listed units match the citations exactly; the disposiciones adicionales vigésima sexta and trigésima tercera and the transitoria decimoctava appear only inside RIRPF/LIS text, so they need not be listed | — |
| `b57134fd8c` | PASS | Normativa vs. lesson citations (RIRPF) | listed units match the citations exactly; ends in a bare article number without final period, as intended | — |
| `53fc359f40` | FAIL | Normativa vs. lesson citations (LIS) | the lesson cites «disposición adicional decimocuarta.1.b) LIS» (l. 360) and «disposición adicional decimocuarta.1.a) LIS» (l. 362, 364); the line lists only «disposición adicional decimocuarta.1» (the form of the esquema cell, l. 372) and misses the two units as written | - LIS (Ley 27/2014): arts. 40.1, 40.2, 40.3, 40.5, 41, 128.1, 128.6, disposición adicional decimocuarta.1, disposición adicional decimocuarta.1.a) y disposición adicional decimocuarta.1.b). |
| `eac7a6d153` | PASS | Normativa vs. lesson citations (RIS) | only art. 62.1 cited | — |
| `2b961fb2e0` | PASS | Normativa vs. lesson citations (RIVA) | arts. 71.1, 71.3, 71.4 cited, none missing | — |

PASS 6 · FAIL 1
