# Normativa block check — recheck 1

Blind recheck of nine «## Normativa» lines in `content/aeat-agentes-hacienda/es/lessons/`, under the rules in the
header of `batch-1.md`: label = `short` in `sources/normativa.yaml`; articles = exactly the articles of that norm the
lesson cites (parenthesised «art./arts.» citations and the Cita column of esquema tables), at article level; references
inside transcribed or paraphrased legal text, and norms only named, are not citations. No lesson file was edited.

## Totals

- Lines checked: 9 — PASS 9, FAIL 0.

## m01-l07

- `TREBEP (RDL 5/2015): arts. 1, 2, 4, 7–12, 14–16, 18, 20, 22–24, 30, 31, 33, 34, 36–39, 41, 42, 46–50, 47 bis, 52–56, 59–64, 67, 75, 76, 78–82, 84–91, 93–98, disposición derogatoria única, disposición final cuarta, disposición adicional decimoséptima, disposición adicional decimotercera y disposición adicional decimocuarta.` — PASS.
  - Art. 97: the prescription table at line 1045 has the header `| | TREBEP (art. 97) | RD 33/1986 (arts. 20–21) |`.
    The label before the parentheses makes art. 97 a TREBEP citation, and art. 97 TREBEP is the article on
    prescription of faults and sanctions. The range 93–98 includes it.
  - Every other article extracted from the body matches the list: 48.a)–m) (Cita column, lines 385–400), 49.a)–g)
    (lines 410–420), 46.1, 47.1, 47 bis.1–2 and 50.1. Nothing outside the list is cited.
  - Disposiciones: derogatoria única b) (lines 44, 46), final cuarta.1–2 (lines 50, 52), adicional decimoséptima.4
    (line 204), decimotercera (line 402) and decimocuarta (line 424) are all cited. «La disposición final tercera del
    TREBEP da nueva redacción…» (line 890) is prose, not in parentheses, so it only names the disposición and correctly
    has no entry. «excepto el artículo 25.2» (line 52) is inside the transcribed disposición final cuarta, so it is named,
    not cited.
- `RD 33/1986 (Reglamento de Régimen Disciplinario): arts. 1, 6–8, 14–21, 29, 30, 33, 35–37, 41–43, 45 y 47.` — PASS.
  The cited articles are 1, 6, 7.1, 8, 14, 15, 16, 17, 18.1, 19.1–2 and 20–21 (the table header at line 1045), plus
  29.1, 30, 33.1, 33.3, 35.1, 36, 37.1, 41, 42, 43, 45.1 and 47. Together they give exactly the listed set. Art. 97
  belongs to the TREBEP, not to this norm. The only other mention is the full title at line 6, which is not a citation.

## m02-l01

- `RD 829/2023 (departamentos ministeriales): art. 3.` — PASS. Line 133 (table row, parenthesised gloss «hoy: …;
  art. 3.1 del Real Decreto 829/2023, …»). This is the only reference to the norm.
- `Declaración 17 relativa a la primacía, aneja al Acta Final de la Conferencia Intergubernamental; no figura en
  \`normativa.yaml\`.` — PASS. The norm is not in `normativa.yaml`, so it has no `short`. Line 231 names it in
  parentheses with no article, so a not-in-yaml note line is the correct form.
- `Código Civil: arts. 1 y 2.` — PASS. Label matches the `short`. Arts. 1.1–1.6 are cited at lines 6, 19, 198–210, 214
  and in the esquema at lines 202–205. Arts. 2.1–2.3 are cited at lines 63, 66, 67 and 276. No other article is cited.

## m02-l03

- `RD 829/2023 (departamentos ministeriales): art. 22.` — PASS. Line 94 cites «(art. 22.1 del Real Decreto 829/2023,
  …, RD 829/2023)». This is the only reference.

## m03-l08

- `LGT (Ley 58/2003): arts. 7, 99, 101, 113, 114 y 141–158.` — PASS.
  - Art. 7 is cited once, at line 365: «(art. 30.4 LPAC, de aplicación supletoria, art. 7.2 LGT)». Adding it was correct.
  - The other cited articles are 99.7, 101.3.a and 101.4.a, 113, and 114.1–3. Every article from 141 to 158 is also
    cited, including 144 and 153. Nothing outside the list is cited.
  - «artículos 93 y 94 / 134 y 135 / 136 a 140 de la LGT» (lines 11, 12, 16, 246), «artículo 116» (line 69),
    «artículo 104.2» (line 303), «artículo 251» (line 307), «artículo 27» (line 355) and «artículo 188.1» (line 393)
    all sit inside transcribed or paraphrased legal text, without parentheses. They are named, not cited.
- `Resolución de 24-03-1992 (inspección de los tributos, Departamento de Inspección Financiera y Tributaria): apartado
  Cinco.` — PASS. Label matches the `short`. The single citation is at line 44: «(Resolución de 24-03-1992, apartado
  Cinco.2.c)». At article level this reduces to apartado Cinco.
