# Normativa block check — batch 1

Blind check of the «## Normativa» block of m01-l01 … m01-l07 and m02-l01 (`content/aeat-agentes-hacienda/es/lessons/`),
against `sources/normativa.yaml`. No lesson file was edited.

Method: every «art./arts./artículo(s)», «disposición …», «preámbulo», «anexo» and «apartado» reference in the lesson
body (prose, esquema tables including the Cita column, notes, «Lo que más cae») was extracted by script, assigned to the
norm named after it (or, in a series, to the preceding one), reduced to article level, and compared with the block. Every
mismatch was then read in context. A singular «art. 168.1 y 3» or «art. 1.1–2» is one article (apartados), not two.
References inside transcribed or paraphrased legal text («en el artículo 81», «del artículo 18.2 y 3 de la Constitución»)
are treated as *named*, not cited, which is how the existing blocks treat them; the borderline ones are listed as notes.

## Totals

- Cited-norm lines checked: 65 — PASS 63, FAIL 2.
- Named-only lines («nombrado/nombrada en…», «no figura en normativa.yaml»): 7 — none contradicts the text.
- Cited norms with no line: 2 (both m02-l01).
- Labels: every label is the `short` of the right norm in `normativa.yaml`.

## m01-l01

- `CE: arts. 1, 2, 6–60, 62–65, 81, 91, 92, 99, 100, 114–116, 159–164 y 167–169, preámbulo y disposición final.` — PASS.
  (Art. 82 appears only inside the transcribed text of art. 27.2 LOTC, line 527: named, not cited.)
- `LO 2/1979 (LOTC): arts. 1, 4, 6, 7, 9, 10, 16–18, 23, 24, 27, 29, 30, 33, 35, 39, 41–59, 62, 63 y 76.` — PASS.
- Reforma de 15 de febrero de 2024 (named) — consistent with line 150.

## m01-l02

All 11 lines PASS: CE; Reforma de 19 de mayo de 2026 (disposición final única and disposición transitoria única, line 79);
LOREG (LO 5/1985); LO 3/1984; Ley 50/1981; LO 3/1981; LOPJ (LO 6/1985); Ley 38/1988; Reglamento del Congreso;
Reglamento del Senado; LO 1/2025 (disposición transitoria segunda, line 922).

Notes (no change proposed):
- CE art. 116 is not listed. It appears in the transcribed art. 78.2 CE (line 199) and in the course sentence «Los
  artículos 86 y 116 son los decretos-leyes y los estados de alarma, excepción y sitio (art. 57 Reglamento del Congreso)»
  (line 203). Borderline: if a course-voice gloss counts as a citation, the CE line needs 116.
- CE 103, 131 and 18 appear only inside transcribed text (lines 489, 107, 765): named.

## m01-l03

All 4 lines PASS: CE; Ley 50/1997 (Gobierno); Ley 40/2015 (LRJSP); RD 829/2023 (art. 1).
CE 82, 86, 94, 96 and LRJSP 15.2 appear only inside transcribed text (lines 213, 826, 374): named.

## m01-l04

All 9 cited lines PASS: CE (with disposición transitoria quinta); LO 1/1995 and LO 2/1995 (with preámbulo); LBRL;
TUE; TFUE; Estatuto del Tribunal de Justicia de la Unión Europea (art. 50 ter); Protocolo n.º 6 (art. único);
Reglamento interno del Consejo (art. 1).

Notes:
- TFUE art. 255 is named in the course paraphrase «tras consultar al comité del artículo 255 del TFUE … (art. 253 TFUE)»
  (line 993). Borderline, like m01-l02 CE 116.
- Named-only line: every claim checks out. It is incomplete in one place, not contradictory: the Estatuto de Baleares is
  also named in art. 40 LBRL (line 792), not only in art. 41.3.

## m01-l05

All 7 cited lines PASS: Ley 40/2015 (LRJSP); RD 203/2021 (with anexo); Ley 39/2015 (LPAC); Ley 19/2013; RD 615/2024
(cited as «Estatuto RD 615/2024», arts. 1, 12, 17); RGPD; LOPDGDD.
Named-only lines (Ley 30/1992 in arts. 2.1, 24.3, 30.5 Ley 19/2013; Esquema Nacional de Seguridad in art. 46.3 LRJSP)
match the text.

Notes:
- LPAC arts. 21 and 68 are named in the paraphrase of art. 14.1 RD 203/2021 (lines 238, 242): named, not cited.
- CE (in art. 12 Ley 19/2013, line 476; art. 1.a LOPDGDD, line 844), Ley 16/1985, Ley 47/2003 (LGP) and LO 2/2012 are
  named in transcribed text but have no «nombrada en» line. m01-l06 does write such lines, so this is a consistency
  point, not a rule breach.

## m01-l06

All 8 cited lines PASS: LO 3/2007 (with disposición adicional primera); LO 1/2004; LOPJ (art. 89); Ley 15/2022;
Ley 4/2023; RDL 1/2013; Ley 39/2006 (with disposición final primera); Ley 4/2026 (disposición final vigesimoctava).
The named-only line matches the text (Código Penal art. 468 at line 183 is inside art. 89.5 LOPJ; CE in 1.1 Ley 15/2022
and 1 RDL 1/2013; LPAC art. 112 in art. 40 Ley 15/2022; LRJSP 109 and 22.3 in 41.1 Ley 15/2022 and 9.2 Ley 4/2023).

## m01-l07

15 of 17 cited lines PASS: Ley 30/1984 (21, 29, 29 bis; arts. 1, 20, 25 appear only in paraphrased text, lines 54,
765, 918, 1072); RD 364/1995; RD 365/1995; RDL 6/2023; Ley 53/1984; RD 598/1985; RDL 4/2000; RD 375/2003 (90 and 91
appear only inside the transcribed art. 92.4); RD 577/1997; LGSS; RDL 1/2013; Ley 40/2015; RD 829/2023 (art. 22);
Resolución de 14-04-2026 (apartados 9.1, 9.7, 14.2–14.3); RDL 670/1987 (cited as TRLCPE).
Named-only lines (Ley 29/1975; Ley 29/2011 art. 5 in arts. 49.f and 89.6 TREBEP) match the text.

FAIL 1 — TREBEP line omits art. 97. The prescription table at line 1045 has the heading «TREBEP (art. 97)», which is
the only citation of art. 97 in the lesson. Corrected line:

```
- TREBEP (RDL 5/2015): arts. 1, 2, 4, 7–12, 14–16, 18, 20, 22–24, 30, 31, 33, 34, 36–39, 41, 42, 46–50, 47 bis, 52–56, 59–64, 67, 75, 76, 78–82, 84–91 y 93–98, disposición derogatoria única, disposición final cuarta, disposición adicional decimoséptima, disposición adicional decimotercera y disposición adicional decimocuarta.
```

FAIL 2 — RD 33/1986 line lists art. 97, which the lesson never cites for RD 33/1986. The 97 is the TREBEP heading in the
same table row (line 1045, «TREBEP (art. 97) | RD 33/1986 (arts. 20–21)»), attributed to the wrong norm. Corrected line:

```
- RD 33/1986 (Reglamento de Régimen Disciplinario): arts. 1, 6–8, 14–21, 29, 30, 33, 35–37, 41–43, 45 y 47.
```

Note: line 890 says in the course's own voice that «La disposición final tercera del TREBEP da nueva redacción al
artículo 16.1 de la Ley 53/1984» (citation: art. 16.1 Ley 53/1984). Borderline. If it counts, the TREBEP line also needs
«disposición final tercera».

## m02-l01

All 7 lines PASS: CE (with disposición derogatoria 3); Ley 50/1997 (arts. 23–26); Ley 39/2015 (LPAC); LO 3/1980
(art. 22); TUE (arts. 1, 4, 5; arts. 24 and 26 TUE appear only inside the paraphrase of art. 291.2 TFUE, line 255);
TFUE (288–291, 297); Código Civil (arts. 1, 2).

Missing line 1 — RD 829/2023 is cited and has no line. The esquema row e) at line 133 adds the course note «(hoy:
Ministro de la Presidencia, Justicia y Relaciones con las Cortes; art. 3.1 del Real Decreto 829/2023, de 20 de
noviembre, …)». That is the course's own citation; it is not text of art. 24.1 Ley 50/1997. Line to add:

```
- RD 829/2023 (departamentos ministeriales): art. 3.
```

Missing line 2 — line 231 cites «(Declaración 17 relativa a la primacía, aneja al Acta Final de la Conferencia
Intergubernamental)». It has no line and is not in `normativa.yaml`. Line to add, following the m01-l05 convention:

```
- Declaración 17 relativa a la primacía, aneja al Acta Final de la Conferencia Intergubernamental; no figura en `normativa.yaml`.
```
