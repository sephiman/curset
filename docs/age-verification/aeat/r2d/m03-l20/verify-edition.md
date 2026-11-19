# Blind verify (edition) — `m03-l20`

2026-11-19. Opus verifier. Input: `r2d/m03-l20/pending.md` (2 rows, both «Normativa» lines). Each line compared with
every citation in the lesson as it stands (parentheticals, esquema «Cita» cells, wrapped lines joined).

Normativa additions (no pending row): the lesson cites the CAU (122 citations «… CAU)») and has no line for it; the
list both pending lines carry is exactly the CAU's: «- Código Aduanero de la Unión (Reglamento (UE) 952/2013): arts.
4.1, 4.2, 5.12, 5.15, 5.16, 5.17, 5.18, 5.19, 5.26, 5.33, 5.5, 5.6, 5.9, 9.1, 9.2, 9.3, 9.4, 18.1, 18.2, 18.3, 18.4,
19.1, 19.2, 19.3, 20, 21, 39, 70.1, 70.2, 71.1.e), 71.3, 72, 72.a), 77.1, 77.2, 77.3, 78.1, 78.2, 78.3, 79.1, 79.2,
79.3, 79.4, 80.1, 80.2, 81.1, 81.2, 81.3, 82.1, 82.2, 82.3, 82.4, 83.1, 83.2, 84, 85.1, 85.2, 86.1, 86.2, 87.1, 87.2,
87.3, 87.4, 103.1, 103.2, 103.3, 124.1, 144, 149, 158.1, 158.2, 159.1, 159.2, 159.3, 160, 161, 162, 163.1, 163.2,
163.3, 233.4.a), 233.4.b)–e), 237.1, 240.1 y 240.2.». Norms named without a line: Directiva (UE) 2017/2455 and
Directiva (UE) 2019/883 (art. 138 Reglamento Delegado del CAU, l. 427, 430), Reglamento (UE) 2022/2399 (l. 471, art.
163.1 CAU).

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `2990a9bf1d` | FAIL | Normativa vs. lesson citations (Reglamento Delegado del CAU) | misattributed: the list is the CAU's (Reglamento (UE) 952/2013) units; the lesson cites the Reglamento Delegado as «Reglamento Delegado del CAU» only in arts. 5.1 (l. 68–81), 6.1 (l. 85), 7.1 (l. 94), 77 (l. 293), 80 (l. 302), 135.1 (l. 372), 136.1 (l. 383), 137.1 (l. 403), 138 (l. 417) and 140.1 (l. 436) | - Reglamento Delegado (UE) 2015/2446 (CAU, normas de desarrollo): arts. 5.1, 6.1, 7.1, 77, 80, 135.1, 136.1, 137.1, 138 y 140.1. |
| `7166263393` | FAIL | Normativa vs. lesson citations (Reglamento de Ejecución del CAU) | misattributed: the list is the CAU's units; the lesson cites the Reglamento de Ejecución only in art. 221.2 (l. 455–462) | - Reglamento de Ejecución (UE) 2015/2447 (CAU, normas de ejecución): art. 221.2. |

PASS 0 · FAIL 2
