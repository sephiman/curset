# Normativa block check — batch 3 (m03-l05 … m03-l12)

Blind check of the «## Normativa» block of each lesson in `content/aeat-agentes-hacienda/es/lessons/`
against the citations in the lesson body (prose, esquema «Cita» column, «Lo que más cae»).

## Method

- A citation is an abbreviated `art.`/`arts.` reference (or an `apartado`/`disposición` reference to a
  norm) inside a parenthesis or in the last column of an esquema table. Every `art.`/`arts.` in the
  eight lessons sits in one of those two places (checked: none outside).
- Article level: `art. 62.2.a LGT` → 62; ranges expanded; `art. 152.1 y 2 LGT` read as apartados 1 and 2
  of art. 152, not as art. 2; an unnamed number in a series takes the next named norm, or the previous
  one when none follows.
- Spelled-out `artículo N …` inside paraphrased legal text (for example «en los términos del artículo 46
  LGT y el artículo 111 RGAT», «artículo 24 LOFCA», «artículo 29 CE») counts as a norm *named*, not
  cited. The blocks follow the same reading, and rule (5) leaves such norms out of scope. These mentions
  appear at the end of each lesson's section for the record. None of them contradicts a block line.
- Labels were checked against `short` in `sources/normativa.yaml`.
- Extraction done with a script, then each discrepancy and each unusual citation read in context.

## m03-l05

| Line | Result | Notes |
| --- | --- | --- |
| LGT (Ley 58/2003): arts. 85–95, 95 bis y 97–112. | PASS | Cited: 85–95, 95 bis, 97–112. Art. 96 is not cited and not listed. |
| RGAT (RD 1065/2007): arts. 62–64, 66, 69–75, 77–79, 91 y 102–104. | PASS | Exact match. |
| Ley 39/2015 (LPAC): arts. 14 y 43. | PASS | 14.2.a (l. 510), 43 (notificación electrónica). |
| Orden HAC/1398/2003 (colaboración social): apartado primero, apartado segundo, apartado tercero, apartado cuarto y disposición adicional única. | PASS | Apartados primero.1–5, segundo.1–4, tercero.1–3, cuarto.1–2 and DA única.1 cited (ll. 244–264). |

Named, not cited (no line needed): LGT arts. 27, 35, 46, 57, 128, 155, 250; RGAT arts. 36, 59, 111;
CE art. 29; LOFCA art. 24; Ley 12/2002 art. 66; Ley 25/2003 art. 51; Ley 10/2010; LO 15/1999;
Ley del Notariado; Código Civil and Ley 1/2000 (l. 518); «Código Aduanero Comunitario» (l. 55).

## m03-l06

| Line | Result | Notes |
| --- | --- | --- |
| LGT (Ley 58/2003): arts. 23, 98 y 119–122. | PASS | |
| RGAT (RD 1065/2007): arts. 118–120. | PASS | |
| LIRPF (Ley 35/2006): arts. 99 y 101. | PASS | |
| RIRPF (RD 439/2007): arts. 75, 76, 78, 80–82, 94, 95 y 108–112. | PASS | |
| LIS (Ley 27/2014): arts. 40, 41 y 128 y disposición adicional decimocuarta. | PASS | DA 14.ª.1.a and 1.b cited (ll. 360–364). |
| RIS (RD 634/2015): art. 62. | PASS | |
| LIVA (Ley 37/1992): art. 164. | PASS | 164.Uno.6.º (l. 35). |
| RIVA (RD 1624/1992): art. 71. | PASS | |
| Orden EHA/586/2011 (modelo 111): art. 1. | PASS | |

Named, not cited: LIRPF arts. 7, 37, 92, 94, 95, DA 26.ª, DA 33.ª, DT 18.ª; RIRPF arts. 83–88, 90, 93,
96–98, 104 (in reproduced text); LIS arts. 29, 34, 114; RIS art. 60; LIVA arts. 20, 26, 121; RIVA art. 30;
LGT art. 26; Ley 35/2003 and RD 1082/2012; Ley 19/1994 art. 76; Directiva 2003/41/CE; RD 304/2004.
«redacción del Real Decreto-ley 29/2026» appears inside citations of arts. 75.3.h, 75.4 RIRPF and similar
(ll. 192, 198, 226) as a version note, not as an article citation of the RDL; no line required by the
rules, but the caller may want a «nombrado en» line for RDL 29/2026.

## m03-l07

| Line | Result | Notes |
| --- | --- | --- |
| LGT (Ley 58/2003): arts. 31, 57, 117, 118, 120 y 123–140. | PASS | 126 cited at ll. 72 and 77; 132 at l. 237. |
| RGAT (RD 1065/2007): arts. 116, 122–131, 133, 135–137 y 153–165. | PASS | |
| LIRPF (Ley 35/2006): art. 103. | PASS | |
| Ley 39/2015 (LPAC): art. 30. | PASS | |

Named, not cited: LGT arts. 32, 108, 142 and others mentioned as «artículo N»; RGAT arts. 31, 32.

## m03-l08

| Line | Result | Notes |
| --- | --- | --- |
| LGT (Ley 58/2003): arts. 99, 101, 113, 114 y 141–158. | **FAIL** | Omits art. 7: «(art. 30.4 LPAC, de aplicación supletoria, art. 7.2 LGT)» at l. 365 (worked example). |
| RGAT (RD 1065/2007): arts. 87, 88, 97, 98, 166–173 y 175–191. | PASS | Art. 174 not cited, not listed. |
| Ley 39/2015 (LPAC): art. 30. | PASS | |
| *(missing line)* | **FAIL** | l. 44 cites «(Resolución de 24-03-1992, apartado Cinco.2.c)». The norm is in `normativa.yaml` as `Resolución de 24-03-1992 (inspección de los tributos, Departamento de Inspección Financiera y Tributaria)` and the block has no line for it. |

Corrected lines:

- `- LGT (Ley 58/2003): arts. 7, 99, 101, 113, 114 y 141–158.`
- add `- Resolución de 24-03-1992 (inspección de los tributos, Departamento de Inspección Financiera y Tributaria): apartado Cinco.`

Named, not cited: LGT arts. 104, 172; RGAT art. 146; RDL 1/2004 (Catastro); Ley 21/2001 art. 46.3;
Ley 28/1990 and Ley 12/2002 (l. 309).

## m03-l09

| Line | Result | Notes |
| --- | --- | --- |
| LGT (Ley 58/2003): arts. 7, 26, 59–65 y 82. | PASS | |
| RGR (RD 939/2005): arts. 11, 12, 17, 28, 29, 32–54 y 68. | PASS | |
| Orden HFP/311/2023 (límite exento de garantías en aplazamientos): art. 2, disposición derogatoria única y disposición final única. | PASS | DDU and DFU cited at l. 350. |
| Ley 31/2022 (PGE 2023, prorrogados): disposición adicional cuadragésima segunda. | PASS | DA 42.ª.Uno and .Dos (l. 437). |
| Ley 39/2015 (LPAC): art. 30. | PASS | |

Named, not cited: LGT arts. 2, 3, 33, 81, 150, 161, 167, 168; RGR arts. 5, 9, 62, 74, 75–93, 113–115;
Orden HAP/2178/2015 (derogated, l. 350).

## m03-l10

| Line | Result | Notes |
| --- | --- | --- |
| LGT (Ley 58/2003): arts. 71–76 y 173. | PASS | |
| RGR (RD 939/2005): arts. 55–63 y 116. | PASS | |
| RGAT (RD 1065/2007): arts. 138–140, 142 y 143. | PASS | |
| Orden PRE/3581/2007 (departamentos de la AEAT): art. 6. | PASS | |

Named, not cited: LGT arts. 26, 62, 63, 161, 167, 169, 225, 239; RGR art. 109; Ley 47/2003 (l. 319).

## m03-l11

| Line | Result | Notes |
| --- | --- | --- |
| LGT (Ley 58/2003): arts. 28, 62, 77–82, 160, 161 y 163–168. | PASS | Art. 162 not cited, not listed. |
| RGR (RD 939/2005): arts. 3–8, 46, 64–67, 69–74 y 77. | PASS | |
| Ley 39/2015 (LPAC): art. 30. | PASS | |

Named, not cited: LGT arts. 26, 253.

## m03-l12

| Line | Result | Notes |
| --- | --- | --- |
| LGT (Ley 58/2003): arts. 162, 165, 167, 169–172 y 174–177. | PASS | |
| RGR (RD 939/2005): arts. 10, 75–85, 88 bis, 89–98, 100, 101, 103–109, 103 bis, 104 bis, 111, 113, 116, 117, 119, 120, 124 y 127. | PASS | The set matches exactly. Cosmetic: «103 bis» and «104 bis» come after the range «103–109». The other blocks put a bis next to its base number (compare «95, 95 bis» in m03-l05). Optional reorder: `arts. 10, 75–85, 88 bis, 89–98, 100, 101, 103, 103 bis, 104, 104 bis, 105–109, 111, 113, 116, 117, 119, 120, 124 y 127.` |
| LEC (Ley 1/2000): arts. 595 y 605–607. | PASS | |

Named, not cited: LGT arts. 28, 42, 62, 63, 77, 112, 142, 146; RGR art. 74; Código de Comercio art. 42;
Ley 47/2003 (l. 551).

## Totals

35 lines checked: 34 PASS, 1 FAIL (m03-l08 LGT), plus 1 missing line (m03-l08, Resolución de
24-03-1992). All labels match a `short` in `normativa.yaml`.
