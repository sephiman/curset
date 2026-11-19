# Normativa block check, batch 2

Blind check of the `## Normativa` block of m02-l02, m02-l03, m02-l04, m02-l05, m03-l01, m03-l02, m03-l03
and m03-l04 (`content/aeat-agentes-hacienda/es/lessons/`) against the citations in each lesson's prose, esquema
tables (last column and any citation inside a cell), notes and «Lo que más cae». Labels checked against `short`
in `content/aeat-agentes-hacienda/sources/normativa.yaml`.

Method: a regex pass over each file collected every «art./arts. … NORMA», «disposición …» and «apartado …»
citation. Every lesson was then read in full to confirm the attributions, the sub-article forms (`2.Uno`,
`3.Dos.1.º.a)`, `66 bis.2`, `52.1–2`) and the series that inherit the norm of the previous item.

Scope rule applied: a citation is a parenthetical reference that names the norm («(art. 62.2 LGT)»). Mentions of
articles inside the body of a sentence or a quoted provision («el artículo 47.1», «artículo 20 de la LIVA») are
not counted as citations. They are listed under «Observaciones» for each lesson, for information.

## Summary

| Lesson | Lines | PASS | FAIL | Missing lines |
|---|---|---|---|---|
| m02-l02 | 3 | 3 | 0 | 0 |
| m02-l03 | 2 | 2 | 0 | 1 |
| m02-l04 | 1 | 1 | 0 | 0 |
| m02-l05 | 3 | 3 | 0 | 0 |
| m03-l01 | 26 | 26 | 0 | 0 |
| m03-l02 | 6 | 6 | 0 | 0 |
| m03-l03 | 3 | 3 | 0 | 0 |
| m03-l04 | 8 | 8 | 0 | 0 |
| **Total** | **52** | **52** | **0** | **1** |

One block fails: m02-l03 cites RD 829/2023 and has no line for it.

## m02-l02

- `Ley 39/2015 (LPAC): arts. 24, 30, 34–52, 98 y 106–114.` PASS. Cited: 24, 30, 34–52 (the range «arts. 34–52
  LPAC» plus 34–45, 47–52 one by one), 98, 106, 107, 108, 109, 110, 111, 112, 113, 114.
- `LJCA (Ley 29/1998): art. 70.` PASS (art. 70.2 LJCA).
- `LO 3/1980 (Consejo de Estado): art. 22.` PASS (art. 22.10 LO 3/1980).

Observaciones: the prose also mentions LPAC arts. 56 and 125.1 inside sentences or quoted text, with no
parenthetical citation.

## m02-l03

- `Ley 39/2015 (LPAC): arts. 1–7, 9–11, 13, 15, 21–25, 28, 30–33, 53, 68, 91 y 122.` PASS. Cited: 1, 2, 3, 4, 5,
  6, 7, 9, 10, 11, 13, 15, 21, 22, 23, 24, 25, 28, 30, 31, 32, 33, 53, 68 (arts. 30.2–3 y 68.1), 91 (91.3) and 122
  (arts. 30.4–5 y 122.1).
- `RD 203/2021 (Reglamento de actuación por medios electrónicos): art. 26.` PASS (art. 26.2.c) RD 203/2021).
- **FAIL (missing line).** The table «Sistemas de identificación electrónica», row c), cites «(art. 22.1 del Real
  Decreto 829/2023, de 20 de noviembre, por el que se reestructuran los departamentos ministeriales,
  RD 829/2023)». The norm is in normativa.yaml as `RD 829/2023 (departamentos ministeriales)`
  (BOE-A-2023-23537), and the block has no line for it. Line to add:
  `- RD 829/2023 (departamentos ministeriales): art. 22.`

Observaciones: Ley 19/2013 is named inside the row d) of art. 13 LPAC, with no article cited. «artículo 29 de la
Constitución» appears inside the quoted text of art. 24.1 LPAC. LPAC arts. 3, 21, 39, 53, 68, 86, 87, 95 and 98.2
are also mentioned in running or quoted text.

## m02-l04

- `Ley 39/2015 (LPAC): arts. 38, 54, 56–58, 60–64, 66, 68–71, 73–77, 80–88 y 94–104.` PASS. Cited: 38, 54, 56,
  57, 58, 60, 61, 62, 63, 64, 66, 68, 69, 70, 71, 73, 74, 75, 76, 77, 80 (80.1–2), 81, 82, 83, 84, 85, 86, 87,
  88, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104. Every article inside each range is cited.

Observaciones: «el artículo 34 de la Ley de Régimen Jurídico del Sector Público» appears inside the paraphrase of
art. 86.5 LPAC, and the Ley 1/2000, de Enjuiciamiento Civil, is named in arts. 56.3 and 77.1. Neither is a
parenthetical citation.

## m02-l05

- `Ley 39/2015 (LPAC): arts. 112–118 y 121–126.` PASS. Cited: 112, 113, 114, 115, 116, 117, 118, 121, 122, 123,
  124, 125, 126.
- `LJCA (Ley 29/1998): arts. 1–3, 6, 12, 25–30, 44, 46, 115 y 128.` PASS. Cited: 1, 2, 3, 6, 12 (12.1.a),
  12.1.b)–c), 12.2.a)), 25, 26, 27, 28, 29, 30, 44 (44.1, 44.2–3), 46, 115, 128.
- `LO 1/2025 (eficiencia de la Justicia): disposición adicional primera.` PASS.

Observaciones: «los artículos 47 y 48 LPAC», «artículo 47.1 LPAC», «artículo 21.4, segundo párrafo, LPAC»,
«artículo 24.1, tercer párrafo» and «artículo 90.4» appear inside paraphrased or quoted text, not as parenthetical
citations. LJCA arts. 29, 30, 44 and 78 are mentioned the same way. 29, 30 and 44 are cited elsewhere anyway.

## m03-l01

All 26 lines PASS:

- `CE: arts. 31, 133, 134, 142 y 156–158.` Cited: 31, 133, 134, 142, 156, 157, 158.
- `LGT (Ley 58/2003): arts. 2–4.` Cited: 2, 3, 4.
- `LGP (Ley 47/2003): arts. 5 y 6.` Cited: 5, 6.
- `LOFCA (LO 8/1980): arts. 2–4, 6, 9–11, 19 y 23.` Cited: 2.Uno, 3, 4.Uno/4.Dos, 6.Uno/Dos/Tres, 9, 10, 11,
  19.Dos, 23.
- `Ley 22/2009 (financiación de las Comunidades Autónomas): art. 25.`
- `Concierto Económico con el País Vasco (Ley 12/2002): art. 1.` Cited as 1.Uno and 1.Dos «Concierto Económico».
- `Convenio Económico con Navarra (Ley 28/1990): art. 1.`
- `TRLRHL (RDL 2/2004): arts. 2, 6, 8, 9, 15, 16, 20, 26, 28–32, 41, 44, 56–60, 78, 92, 100, 104, 131–134, 136 y
  148.` Every article and every range member is cited.
- `LIRPF (Ley 35/2006): arts. 1–3.`, `LIS (Ley 27/2014): art. 1.`, `LIVA (Ley 37/1992): arts. 1 y 3.`
  (1, 1.a)–c), 3.Dos.1.º.a) and b)), `TRLIRNR (RDL 5/2004): art. 1.`, `Ley 19/1991 (Impuesto sobre el
  Patrimonio): art. 1.`, `TRLITPAJD (RDL 1/1993): art. 1.`, `Ley 38/2022 (gravámenes temporales e ITSGF): art. 3.`
  (3.Uno, 3.Dos.2, 3.Tres), `Ley 13/1996 (…): art. 12.` (12.Uno), `Ley 16/2012 (…): art. 19.` (19.Uno),
  `Ley 16/2013 (…): art. 5.` (5.Uno), `Ley 7/2022 (…): arts. 67 y 84.`, `Ley 29/1987 (ISD): art. 1.`,
  `Ley 38/1992 (Impuestos Especiales): arts. 1 y 2.`, `Ley 15/2012 (sostenibilidad energética): arts. 1 y 12.`,
  `Ley 8/2015 (…): art. 9.`, `Ley 4/2020 (…): art. 1.`, `Ley 5/2020 (…): art. 1.`.
- `Ley 7/2024 (Impuesto Complementario; margen de intereses y comisiones): art. 1 y disposición final novena.`
  Cited: 1.1 and «disposición final novena.Uno Ley 7/2024».

Observaciones: running or quoted text also mentions Ley 15/2012 art. 4, Ley 5/2020 art. 2, Ley 7/2024 art. 6,
Ley 16/2012 art. 19 («en la forma y condiciones previstas en el artículo 19»), CE arts. 2, 138 and 158 (inside the
row b) of art. 4.Dos LOFCA), LOFCA arts. 2.Uno.a) and 6, TRLRHL arts. 2, 15, 20.1.B), 30 and 59.1, and
LO 18/2001. None is a parenthetical citation.

## m03-l02

- `Ley 31/1990, art. 103 (creación de la AEAT): art. 103.` PASS. Every Ley 31/1990 citation is to art. 103 (Uno,
  Dos, Tres, Cuatro, Cinco, Seis, Siete, Ocho, Nueve, Diez, Once).
- `Ley 22/2009 (financiación de las Comunidades Autónomas): art. 65.` PASS (65.1–65.7).
- `Orden PRE/3581/2007 (departamentos de la AEAT): arts. 1, 2, 6 y 10.` PASS (1.1, 2.1, 6.1.l), 6.2, 10).
- `Orden de 2 de junio de 1994 (estructura de la AEAT): apartado segundo, apartado tercero, apartado quinto,
  apartado octavo, apartado primero, apartado decimotercero y apartado cuarto.` PASS. Cited: segundo, tercero,
  quinto.1–2, octavo, primero.2/.2.d)/.3/.6, decimotercero.1–2, cuarto.d). The apartados are listed in
  order of first appearance, not in numerical order. This is not a rule breach.
- `Resolución de 13-01-2021 (Delegación Central de Grandes Contribuyentes): apartado primero y apartado cuarto.`
  PASS (primero.1, cuarto.2).
- `Resolución de 13-01-2021 (estructura y organización territorial de la AEAT): apartado primero, apartado
  tercero, apartado cuarto, apartado quinto, apartado sexto, apartado séptimo, apartado octavo y apartado décimo.`
  PASS.

Observaciones: the quoted text of art. 103 Ley 31/1990 and of art. 6.2 of the Orden mentions «artículo 6.5 de la
Ley General Presupuestaria», «artículo 118 del Texto Refundido de la Ley General Presupuestaria», «artículos 22 a
47 de la Ley General Presupuestaria», «artículos 160 a 162», «155 y 156», «111» and «154 de la Ley General
Tributaria», «artículo 9 de la Ley 53/1984», «artículo 1.227 del Código Civil», Ley 22/2003 Concursal, Ley 39/1988
and RDL 2/1989. These are in-text mentions from the 1990–2007 originals. The LGT and LGP ones refer to the
earlier laws, not to Ley 58/2003 or Ley 47/2003, and must not be added to those lines.

## m03-l03

- `LGT (Ley 58/2003): arts. 1–4, 7, 8, 10–28, 49, 50, 53–56 y 58.` PASS. Cited: 1, 2, 3, 4, 7, 8, 10–28 (every
  article from 10 to 28 is cited individually), 49, 50, 53, 54, 55, 56, 58.
- `Ley 31/2022 (PGE 2023, prorrogados): disposición adicional cuadragésima segunda.` PASS (.Uno and .Dos).
- `Ley 8/1989 (Tasas y Precios Públicos): art. 24.` PASS.

Observaciones: the Código Civil art. 3.1 is mentioned in the text of art. 12.1 LGT, and LGT arts. 27, 28, 29, 35,
53, 62 and 88.5 are also mentioned in running or quoted text. None is a parenthetical citation.

## m03-l04

- `LGT (Ley 58/2003): arts. 29–48, 29 bis, 66–70, 66 bis y 104 y disposición adicional sexta.` PASS. Cited: 29,
  29 bis, 30–48 (every article cited), 66, 66 bis, 67, 68, 69, 70, 104 (104.5, in «arts. 68.1.a) y 104.5 LGT»),
  disposición adicional sexta (.1–.4).
- `RGAT (RD 1065/2007): arts. 2, 3, 11, 17–20, 29, 59 y 110–113.` PASS.
- `RD 1619/2012 (Reglamento de facturación): arts. 2–4 y 15.` PASS (2.1, 3.1, 3.3, 4.1–4.4, 15.1–2, 15.3).
- `RIVA (RD 1624/1992): arts. 40, 61, 62 y 69 bis.` PASS.
- `RIRPF (RD 439/2007): art. 68.` PASS.
- `Código de Comercio: art. 30.` PASS.
- `RD 1007/2023 (sistemas informáticos de facturación; VERI*FACTU): arts. 1 y 4.` PASS (1.1, 4, 4.1–4.3).
- `RD 1676/2009 (Consejo para la Defensa del Contribuyente): art. 4.` PASS (4.1, 4.1.a) y b)).

Observaciones: the LIVA (arts. 20, 25, 26, 68, 80, 121, 123, 129) and the LIRPF are named in quoted or running
text only, and neither has a line. That is consistent with the scope rule. LGT arts. 26, 79, 115, 175 and 176 are
mentioned in running text only.
