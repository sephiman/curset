# Blind verify (edition) — `m03-l02`

2026-11-19. Opus verifier. Input: `r2d/m03-l02/pending.md` (5 rows: three esquema rows whose list marker was fixed,
two «Normativa» lines). Rows checked against `BOE-A-2007-21228_orden-pre-3581-2007-departamentos-aeat_2025-09-13.pdf`
(art. 6.2.e)); «Normativa» lines compared with every citation in the lesson as it stands.

Normativa additions (no pending row): the lesson cites the Orden PRE/3581/2007 (arts. 1.1, 2.1, 6.1.l), 6.2 and 10)
and has no line for it: «- Orden PRE/3581/2007 (departamentos de la AEAT): arts. 1.1, 2.1, 6.1.l), 6.2 y 10». Norms
named inside art. 103 Ley 31/1990 or art. 6.2 Orden PRE/3581/2007 without a line: Ley General Presupuestaria and its
Texto Refundido (l. 7, 21), Ley 22/2003 and Ley Concursal (l. 33–41), Código Civil (l. 51), Ley 39/1988 (l. 78), Ley de
Entidades Estatales Autónomas (l. 80), Ley General Tributaria and Real Decreto 2244/1979 (l. 82), Real Decreto-Ley
2/1989 (l. 217), Ley 53/1984 (l. 219).

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `281ad88214` | PASS | art. 6.2.e) Orden PRE/3581/2007 | first dash item of letter e), verbatim; only the stray marker went, no number or condition changed | — |
| `67aa2656ba` | PASS | art. 6.2.e) Orden PRE/3581/2007 | second dash item, verbatim, including «artículo 1.227 del Código Civil» and «con anterioridad al embargo» | — |
| `d603f350a0` | PASS | art. 6.2.e) Orden PRE/3581/2007 | third dash item, verbatim, including «en fecha anterior al embargo»; letter e) has exactly these three supuestos | — |
| `06d1b55e19` | PASS | Normativa vs. lesson citations (Ley 31/1990, art. 103) | every listed apartado cited, none missing; ordinals of the apartados (Uno … Once) kept as units, not split into articles; sorted as strings | — |
| `b431cb25d0` | PASS | Normativa vs. lesson citations (Ley 22/2009) | arts. 65.1–65.7 all cited, none missing | — |

PASS 5 · FAIL 0
