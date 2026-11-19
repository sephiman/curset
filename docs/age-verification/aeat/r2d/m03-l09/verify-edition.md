# Blind verify (edition) — `m03-l09`

2026-11-19. Opus verifier. Input: `r2d/m03-l09/pending.md` (4 rows, all «Normativa» lines). Each line compared with
every citation in the lesson as it stands (parentheticals, esquema «Cita» cells, «art. N» and «disposición …»
citations, wrapped lines joined).

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `48d8da6a67` | PASS | Normativa vs. lesson citations (LGT) | listed units match the citations exactly; no misparsed letters or ordinals | — |
| `44464790ac` | PASS | Normativa vs. lesson citations (RGR) | listed units match the citations exactly, no duplicates | — |
| `9ac09dc312` | FAIL | Normativa vs. lesson citations (Orden HFP/311/2023) | misses art. 2, cited at l. 346, 348 and in the esquema at l. 360; both disposiciones are cited at l. 350 | - Orden HFP/311/2023 (límite exento de garantías en aplazamientos): art. 2, disposición derogatoria única (que deroga la Orden HAP/2178/2015) y disposición final única. |
| `0211a1bb1f` | FAIL | Normativa vs. lesson citations (Ley 31/2022) | the lesson cites the units «disposición adicional cuadragésima segunda.Uno» and «…segunda.Dos» (l. 437); the line lists the whole disposición, a unit the lesson does not cite as written | - Ley 31/2022 (PGE 2023, prorrogados): disposición adicional cuadragésima segunda.Uno y disposición adicional cuadragésima segunda.Dos. |

PASS 2 · FAIL 2
