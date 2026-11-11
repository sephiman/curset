# Verification re-check 1 — `m03-l17` (blind)

Verifier: opus, 2026-11-11. Source: LIS snapshot (`BOE-A-2014-12328_lis_2026-09-02.pdf`: arts. 2, 3, 6, 7, 8, 9, 11, 29, 33, 34, 40 and DT 44.ª); `normativa.yaml` LIS entry (no `cifras_anuales`; the DT 44.ª rates are statutory and each sentence names the year and the disposición). For the «Normativa» block: every LIS article and every other norm in the prose above «## Normativa», parenthetical and running text («apartado 12 del artículo 15 bis de la LIS», «letra l) del artículo 15», «artículo 18 de la LIS», «artículo 101 de la LIS», «artículo 105 de la LIS», «apartado 11 del artículo 21», «capítulo XIV del título VII», «capítulo VII del título VII»). Pending line numbers match the current file.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `ad471260d7` | PASS | art. 11.3.2.º LIS | rule and its «No obstante» exception word for word; the following «Tampoco» rule is about the re-accounted gastos e ingresos, not about the reserve entries | — |
| `9994c452c8` | PASS | art. 29.1.a) and DT 44.ª.2.a).i) LIS | 17 %; 19 % for periods starting in 2026 | — |
| `2f585ec3ab` | PASS | art. 29.1.b) and DT 44.ª.2.a).ii) LIS | 20 %; 21 % for periods starting in 2026 | — |
| `9da133fba6` | PASS | art. 29.1 and DT 44.ª.2.a) LIS | 50.000 euros × días/365, or the base when lower; 19 % in 2026 | — |
| `17175ebb28` | PASS | art. 29.1 (third paragraph) and DT 44.ª.2.b), 3 and 4 LIS | 20 % «excepto si … deban tributar a un tipo diferente del general»; 23 % (2026), 22 % (2027), 21 % (2028) | — |
| `e561a0d0f4` | PASS | art. 33.2 LIS | definition and the «No se estimará» exclusion word for word; the arrendamiento rule follows in the next sentence | — |
| `61d7921f74` | PASS | art. 33.3 LIS | «esos importes» refers to the 60.000/1.200.000 and 120.000/2.400.000 limits of the two previous sentences; acreditación del cierre de un ciclo mercantil for the excess | — |
| `2b0f8e718f` | PASS | art. 40.1 LIS | first 20 días naturales of abril, octubre and diciembre; period in course on day 1; entities of art. 29.4–5 exempt from the payment and the declaración | — |
| `7097dc8f18` | PASS | arts. 2.1, 7.1.a) and 8.1 LIS | the tax applies «en todo el territorio español»; personas jurídicas residentes, «excluidas las sociedades civiles que no tengan objeto mercantil»; residence by constitution, domicilio social or sede de dirección efectiva | — |
| `e56123d5a9` | FAIL | arts. 6.1 and 6.2 LIS | drops the narrowing clause of art. 6.2: the entidades en régimen de atribución de rentas do not pay the tax «a excepción de lo dispuesto en el apartado 12 del artículo 15 bis» (the prose at l. 29 keeps it) | Las comunidades de bienes y demás entidades del artículo 35.4 LGT no tributan por el Impuesto sobre Sociedades, a excepción de lo dispuesto en el apartado 12 del artículo 15 bis LIS, y sus rentas se atribuyen a los comuneros o partícipes (arts. 6.1 y 6.2 LIS). |
| `c15f1517ce` | FAIL | LIS (Ley 27/2014) | every listed article is cited, but LIS units named in the prose are not listed: 15 bis.12 (l. 29), 15.l) (l. 108), 18 and 101 (l. 215), 105 (l. 228), 21.11 (l. 258), capítulo XIV del título VII (ll. 77, 88) and capítulo VII del título VII (l. 179) | LIS (Ley 27/2014): arts. 1, 2.1–2, 3, 4.1–2, 5.1–2, 6.1–2, 7.1–3, 8.1–2, 9.1–4, 10.1–4, 11.1–10, 11.12–13, 15.l), 15 bis.12, 17.1, 18, 20, 21.11, 23.1, 23.3, 23.5, 24.1–2, 25.1–2, 25.4, 26.1–5, 27.1–3, 28, 29.1–7, 30.1–2, 31.1–3, 31.6–7, 32.1, 32.3–5, 32.8, 33.1–3, 34, 40.1, 101, 105, 109, 110.1–2, 124.1–3, 125.1–3, 126, 127.1–5, capítulos VII y XIV del título VII y disposición transitoria cuadragésima cuarta.2–4. |
| `fa95de697c` | PASS | art. 34 LIS | art. 34 names «el apartado 2 del artículo 25 o en el apartado 1.a), b) y c) del artículo 36 de la Ley 7/1985»; prose l. 276 | — |
| `96fdfd6423` | PASS | art. 3 LIS | «de conformidad con el artículo 96 de la Constitución Española»; prose l. 11 | — |
| `bae2ae045c` | PASS | art. 7.1.k) LIS | «la Disposición adicional décima de la Ley 9/2012, de 14 de noviembre, de reestructuración y resolución de entidades de crédito»; prose l. 45 | — |
| `2fd96bbfbc` | FAIL | arts. 9.2 and 29.3 LIS | art. 9.2 names «el título II de la Ley 49/2002»; art. 29.3 names only «el régimen fiscal establecido en la Ley 49/2002», with no título (prose l. 220 the same) | Ley 49/2002 (régimen fiscal de las entidades sin fines lucrativos y de los incentivos fiscales al mecenazgo): título II, nombrado en el art. 9.2 LIS; nombrada también en el art. 29.3 LIS, sin precepto citado. |
| `ea4415f19e` | FAIL | art. 9.3.d) LIS | «sin precepto citado» is wrong: art. 9.3.d) reads «constituidos al amparo del artículo veintidós de la Ley 27/1984»; the list item at l. 82 also drops «del artículo 22», so it has to name it for the line to match the prose («- d) Los fondos de promoción de empleo constituidos al amparo del artículo 22 de la ley sobre reconversión y reindustrialización.») | Ley 27/1984 (reconversión y reindustrialización): art. 22, nombrado en el art. 9.3.d) LIS. |
| `675dc6492c` | PASS | art. 9.4 LIS | names the Ley Orgánica 8/2007 with no precepto; prose l. 86 | — |
| `9f614a1624` | PASS | art. 29.6 LIS | names the Ley 34/1998 with no precepto; prose l. 223 | — |
| `dfc97d9242` | PASS | art. 29.7 LIS | «el artículo 43 de la Ley 19/1994»; prose l. 224 | — |

The other lines of the block (LGT, LIRPF, Código de Comercio) match the prose; no line holds an editorial instruction or two norms.

PASS 15 · FAIL 4
