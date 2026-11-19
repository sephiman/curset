# Blind verify (edition) — `m01-l05`

2026-11-19. Opus verifier. Input: `r2d/m01-l05/pending.md` (9 rows, all «Normativa» lines). Each line compared with
every citation in the lesson as it stands (parentheticals, esquema «Cita» cells, «art. N» citations, wrapped lines
joined), above the «Normativa» heading.

Normativa additions (no pending row; prose names these norms and no line lists them): CE (art. 105.b), nombrada en el
art. 12 Ley 19/2013, l. 476–477); Real Decreto 1083/2009 (art. 7 Ley 19/2013, l. 422); Reglamento (UE) n.º 651/2014
and LBRL (Ley 7/1985) (art. 8.1 Ley 19/2013, l. 441, 451); Ley 16/1985 (art. 15.3 Ley 19/2013, l. 521); LGP
(Ley 47/2003), Ley Orgánica 2/2012, LOFCA (LO 8/1980) and TRLRHL (RDL 2/2004) (art. 28 Ley 19/2013, l. 667–681).

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `4e87530309` | PASS | Normativa vs. lesson citations (LRJSP) | every listed unit cited (arts. 3.1.c … 46.3 LRJSP), none missing, no duplicates | — |
| `1f741619b3` | PASS | Normativa vs. lesson citations (RD 203/2021) | listed units match the citations exactly | — |
| `5e71ffebee` | FAIL | Normativa vs. lesson citations (LPAC) | lists arts. 1 and 40, which the lesson never cites for the LPAC: «art. 1» (l. 329, 361) and «art. 40» (l. 840) are citations of the Ley 19/2013 | - Ley 39/2015 (LPAC): arts. 12.2, 14.1, 14.2, 14.3, 16.1, 16.4, 17.1, 17.2, 31.2, 133, 133.1, 133.2, 133.3 y 133.4. |
| `b539918b35` | FAIL | Normativa vs. lesson citations (Ley 19/2013) | missing units the lesson cites: 1 (l. 329, 361), 7 (l. 410–423), 16 (l. 531), 27 (l. 657), 31.3 (l. 760–761), 40 (l. 840); duplicate unit «29.2.d» / «29.2.d)» (l. 730, 1229), kept once. Ends in a bare article number, so no final period | - Ley 19/2013 (transparencia): arts. 1, 2.1, 3, 5.1, 5.3, 5.4, 6.1, 6.2, 7, 8.1, 8.1.a), 8.2, 9.1, 9.3, 10.1, 11, 12, 13, 14.1, 14.2, 15.1, 15.3, 16, 17.1, 17.2, 17.3, 17.4, 18.1, 19.1, 19.2, 19.3, 20.1, 20.2, 20.3, 20.4, 20.5, 20.6, 22.2, 23.1, 23.2, 24.1, 24.2, 24.3, 24.4, 24.5, 24.6, 25.1, 25.2, 25.3, 26.1, 26.2.a), 26.2.b), 27, 28, 29, 29.1, 29.1.d), 29.2, 29.2.d), 29.3, 30.1, 30.2, 30.3, 30.4, 30.5, 31.1, 31.2.a), 31.2.b), 31.3, 31.4.a), 31.4.b), 32.1, 32.2, 33.2, 34, 35, 36.2, 36.3, 37.1, 37.2, 38.1, 39.2 y 40 |
| `a48d9f6ae1` | PASS | Normativa vs. lesson citations (Estatuto RD 615/2024) | cited as «Estatuto RD 615/2024»: arts. 1.1, 1.4, 12.1, 12.2, 17.1.f), all listed, none missing | — |
| `7f42617e82` | PASS | Normativa vs. lesson citations (RGPD) | listed units match the citations exactly | — |
| `96bde646fd` | PASS | Normativa vs. lesson citations (LOPDGDD) | listed units match the citations exactly | — |
| `d1544a404d` | FAIL | Normativa vs. lesson citations (Ley 30/1992) | the lesson cites no article of the Ley 30/1992; «art. 31.3» is the Ley 19/2013's (l. 760–761, Oficina de Conflictos de Intereses). The Ley 30/1992 is only named inside the text of art. 2.1.i) Ley 19/2013 (l. 381, «artículo 5 de la Ley 30/1992») | - Ley 30/1992 (LRJAP-PAC, derogada), nombrada en el art. 2.1 Ley 19/2013. |
| `e22779fb88` | FAIL | Normativa vs. lesson citations (Esquema Nacional de Seguridad) | misparsed line: the label swallowed a stale «nombrado en» note and the article list is the union of the LRJSP, RD 203/2021 and LPAC units; the lesson cites no article of RD 3/2010 and no longer cites art. 5.3 RD 203/2021, arts. 17.3 or 27.3 LPAC, or any «55.2». The lesson only names the Esquema Nacional de Seguridad inside art. 46.3 LRJSP (l. 95–97); it does not name RD 3/2010 (not in `normativa.yaml`; the ENS is now RD 311/2022, outside the snapshots) | - Esquema Nacional de Seguridad, nombrado en el art. 46.3 LRJSP; no figura en `normativa.yaml`. |

PASS 5 · FAIL 4
