# Plan — round R2, tax part (III.1–III.20, `m03-l01` … `m03-l20`)

2026-11-11. Course `aeat-agentes-hacienda`, part III «Organización de la Hacienda Pública y Derecho Tributario». Theory
only; nothing committed. Requirements v1.1 (R3.5, R4.2–R4.5). Writer and verifier spec:
`docs/age-verification/aeat/r2-tax/spec.md`. Working files and reports: `docs/age-verification/aeat/r2-tax/<lesson>/`.
Ledger: `docs/aeat-theory-ledger.md` (section «Tax part»).

## Inputs

- Question packs: `docs/age-verification/aeat/r2/questions/m03-lNN.md` (`r2/tools/question_packs.py III.n`): 315
  coverage questions (vigente or vigente-con-nota, OEP 2022–2025 with the 2022 extraordinario, first tema), 62 more as
  reference (second tema, OEP 2020–2021, excluded).
- Facts asked, one line per coverage question with the article and the R0a evidence:
  `docs/age-verification/aeat/r2-tax/asked-digest.md`. The per-tema lists below are its article column.
- Norms: `content/aeat-agentes-hacienda/sources/normativa.yaml` (snapshots on boe.es as of 2026-11-11; annual figures
  under `cifras_anuales`; RDL 29/2026 and the other unconvalidated RDLs in the header and in the entries).
- Exam style: `docs/aeat-exam-style.md` §§ 2, 8–9 (what the first exercise asks of the tax temas).

## Depth

The measure is the first exercise (R4.3). Three levels, by coverage questions in OEP 2022–2025:

- **Full** (≥ 20): every article of the governing range in the norm's order, each plazo, percentage, amount, organ,
  exception and list complete; worked examples where the norm's own rule is applied step by step.
- **Standard** (10–19): every article of the range that states a rule, plazo, amount, organ or list; definitional and
  procedural detail of the regulation where the questions reached it.
- **Focused** (< 10): the programme's phrases, each at the depth of its own article, plus every fact asked.

No word ceiling at any level. A fact an official question asked is never cut. A fact the programme does not name and no
first-exercise question of OEP 2022–2025 asked stays out.

## New sources this round

Questions in the packs cite norms the course lacked: TRLITPAJD art. 1.1 (2022X-29), Ley 38/2022 art. 3 (ITSGF, 2023-87),
Código de Comercio art. 30.1 (2022X-45), RD 1676/2009 art. 4.1.b) (III.4), Orden EHA/586/2011 (III.6). III.1 «los
impuestos de titularidad estatal y sus características» adds the art. 1 of each state tax (IP, ISD, IIEE, IRNR). All
downloaded from boe.es and entered in `normativa.yaml`; whatever cannot be obtained is listed in the ledger and its
fact stays out. After the last group: the order of models that RIRPF art. 67 and RGAT art. 49 depend on (RD 117/2024).

## Groups, in dependency order

A later tema leans on an earlier one: the LGT's general part (concepts, obligados, prescripción) comes before the
procedures; gestión and inspección before recaudación; recaudación before sanciones and revisión, which cite all of
them; the taxes come last, IRPF before Sociedades (shared rules on rendimientos de actividades) and IVA after both.

| Group | Temas | Governing norm |
|---|---|---|
| G1 Sistema fiscal y AEAT | III.1, III.2 | CE; LOFCA, Ley 22/2009, TRLRHL; each tax's art. 1; art. 103 Ley 31/1990 and the AEAT structure orders |
| G2 LGT, parte general | III.3, III.4 | LGT títulos I–II; RGAT títulos I–II (censos, NIF, libros, representación) |
| G3 Aplicación de los tributos: normas comunes | III.5, III.6 | LGT título III, capítulos I–II and arts. 119–122; RGAT |
| G4 Gestión e inspección | III.7, III.8 | LGT título III, capítulos III–IV; RGAT títulos IV–V |
| G5 Recaudación | III.9, III.10, III.11, III.12 | LGT arts. 59–82, 160–177; RGR |
| G6 Sanciones y revisión | III.13, III.14 | LGT títulos IV–V; RGRST; RGRVA |
| G7 IRPF | III.15, III.16 | LIRPF; RIRPF; módulos orders |
| G8 Sociedades | III.17 | LIS; RIS |
| G9 IVA | III.18, III.19 | LIVA; RIVA; RD 1619/2012 |
| G10 Aduanas | III.20 | CAU (Reglamento (UE) 952/2013); Reglamentos 2015/2446 and 2015/2447 |

The programme has no Impuestos Especiales tema: the 2025 programme dropped it (`normativa.yaml` header). Ley 38/1992
enters only for III.1 (art. 1).

## Per tema

Norms: articles of the governing range (the R1 «Normativa» stubs, extended where the questions reach). «Asked»: the
articles of the coverage questions (count in brackets when repeated). Depth from the count.

### G1

**III.1 `m03-l01`** — El sistema fiscal español; principios impositivos en la CE; impuestos estatales; Haciendas
estatal, autonómica y local. 9 coverage questions. **Focused.**
- Norms: CE arts. 31, 133, 134.7, 142, 156–158; LGT art. 2.2 (clases de tributos) and 3 (principios); LGP arts. 1–5
  (Hacienda Pública estatal: concept); LOFCA arts. 1–4, 6, 10–11, 19; Ley 22/2009 arts. 25–34 (tributos cedidos);
  TRLRHL arts. 2, 56–59; Concierto (Ley 12/2002) and Convenio (Ley 28/1990) art. 1; art. 1 of LIRPF, LIS, LIVA, TRLIRNR,
  Ley 19/1991, Ley 29/1987, TRLITPAJD, Ley 38/1992; Ley 38/2022 art. 3 (ITSGF).
- Asked: CE 31.1, 31.3, 133; LIVA 1; TRLITPAJD 1.1; Ley 38/2022 art. 3; TRLRHL 59.2, 60; Ley 22/2009 25.1.

**III.2 `m03-l02`** — La AEAT: creación, naturaleza, objetivos, funciones y organización. 9. **Focused.**
- Norms: Ley 31/1990 art. 103 (Uno–Seis as the questions reach); Orden de 2 de junio de 1994 apartados primero–
  decimotercero; Orden PRE/3581/2007 arts. 1–9; Resolución de 13-01-2021 (organización territorial).
- Asked: art. 103.Tres (Presidente rank Secretario de Estado; Director General rank Subsecretario; jefatura del
  personal) ×3; Orden 1994 apdo. primero.2–3, cuarto.d), decimotercero.3; Orden PRE/3581/2007 art. 6.1.l);
  Resolución 13-01-2021 (Delegados Especiales: nombramiento).

### G2

**III.3 `m03-l03`** — Derecho tributario; fuentes; tributos; obligación tributaria; hecho imponible, devengo, bases,
cuota y deuda. 13. **Standard.**
- Norms: LGT arts. 1–16 (título I), 17–28 (título II, capítulo I, secciones 1.ª–2.ª: obligación principal, accesorias,
  intereses, recargos art. 27), 49–58 (cuantificación, deuda tributaria); Ley 31/2022 for the interest rates (annual).
- Asked: LGT 2.2.a), 8.a), 10.1, 20, 21.1, 25.2, 27.2 (×3, incl. a computation), 54, 56, 56.5, 56.6.
- Worked examples: recargo del art. 27.2 (fixed percentage by months; 15 % plus interest after 12 months).

**III.4 `m03-l04`** — Obligaciones formales; derechos y garantías; obligados; capacidad de obrar; representación;
domicilio; prescripción. 32. **Full.**
- Norms: LGT arts. 29–34, 35–48, 66–70, DA 6.ª; RGAT arts. 2–3, 9–17 (censos), 18–28 (NIF as asked), 29 (libros
  registro), 59 (domicilio), 110–113 (representación); RD 1619/2012 arts. 2–4, 6, 15; RIVA arts. 40, 62.6, 69 bis;
  RIRPF art. 68; Código de Comercio art. 30.1; RD 1676/2009 art. 4.
- Asked: LGT 35, 37, 38, 43.1.h), 46.7, 48.2.c), 66, 66 bis.2, 67.1–2, 68 (×3), 68.8, 69, DA 6.ª; RGAT 3.5, 11.4,
  19, 20.3, 29.2, 59, 111.5, 112.1, 113; RD 1619/2012 4.2.a) and c), 15.3; RIVA 40, 62.6/69 bis; RIRPF 68.3–5;
  Código de Comercio 30.1; RD 1676/2009 4.1.b).
- Worked examples: cómputo of prescripción (art. 67.1) and its interrupción (art. 68).

### G3

**III.5 `m03-l05`** — Información y asistencia; colaboración social; carácter reservado; normas comunes; fases;
liquidaciones; obligación de resolver y plazos; prueba; notificaciones. 21. **Full.**
- Norms: LGT arts. 85–95 bis, 97–116; RGAT arts. 62–92 (información, asistencia, certificados, colaboración),
  93–116 (normas comunes) as the questions reach.
- Asked: LGT 86.1, 90 (×2), 91 (×2), 95 bis.1, 101.4.b), 104 (×4), 110.1 (×3); RGAT 70.4, 73.1 (×2), 75.2, 77.1,
  91.4, 103.c).
- Worked examples: cómputo of the plazo de resolución (art. 104.1–2) and of a notificación (art. 104.2, 109–112).

**III.6 `m03-l06`** — Declaraciones; autoliquidaciones; comunicaciones de datos; pagos a cuenta. 8. **Focused.**
- Norms: LGT arts. 23, 119–122; LIRPF arts. 99–101 (retenciones e ingresos a cuenta), 99.2; LIS arts. 40–41; RIRPF
  arts. 75–76, 108–112; Orden EHA/586/2011 (title).
- Asked: LGT 119.3; LIRPF 99.2, 101.8; LIS 40.1; RIRPF 75.3.c)–d), 112; Orden EHA/586/2011.

### G4

**III.7 `m03-l07`** — Actuaciones y procedimientos de gestión: iniciación, trámites, terminación; verificación de
datos; comprobación de valores; comprobación limitada; rectificación; devolución. 15. **Standard.**
- Norms: LGT arts. 117–140; RGAT arts. 117–163 as the questions reach (126–138 rectificación y devoluciones,
  153–159 comprobación de valores).
- Asked: LGT 31.2, 117.1.d) and l), 120.4, 129.1, 131, 133.2, 135.1, 136.3, 140.1–2; RGAT 128, 137, 153.6, 159.1.

**III.8 `m03-l08`** — Inspección: funciones y facultades; documentación; personación; procedimiento; medidas
cautelares. 22. **Full.**
- Norms: LGT arts. 99, 101, 113, 141–159; RGAT arts. 87, 166–197.
- Asked: LGT 99, 101.4.a), 113, 141.b), 143.1, 146.2, 149.3, 150 (×2), 155.1, 155.3 (×2), 157.2, 158.1, 158.3;
  RGAT 87.3.f), 171, 172.3, 181 (×4), 189.5.
- Worked example: duración de las actuaciones (art. 150.1–2) and its extensions.

### G5

**III.9 `m03-l09`** — Extinción (I): medios; pago (forma, momento, plazos, imputación, consignación, medios);
aplazamiento y fraccionamiento. 15. **Standard.**
- Norms: LGT arts. 59–65, 26 (intereses as aplazamiento applies them); RGR arts. 23–54; Orden HFP/311/2023; Ley
  31/2022 (interest, annual).
- Asked: LGT 62 (×2), 62.3, 62.4, 63.1, 65.1, 65.2.b), 65.4, 65.5; RGR 28.1, 33.1, 47.3, 48.2, 48.6, 52, 68.2.
- Worked examples: plazos de pago of art. 62.2 (liquidaciones notificadas in each half of the month, días hábiles);
  interest of an aplazamiento (art. 65 LGT, RGR art. 53).

**III.10 `m03-l10`** — Extinción (II): compensación; deducciones sobre transferencias; condonación; baja provisional;
terminación del apremio. 10. **Standard.**
- Norms: LGT arts. 71–76, 173; RGR arts. 55–63, 61–62 (baja provisional), 173; RGAT 139 (compensación of devoluciones)
  and 143 as asked; Orden PRE/3581/2007 art. 6.1.l).
- Asked: LGT 72.2, 72.3, 73.2, 173.3; RGAT 139.4.a), 143.1; RGR 56.2, 56.6, 61.1, 62.4.

**III.11 `m03-l11`** — Recaudación en período ejecutivo; iniciación; efectos; recargos; apremio (características,
concurrencia, suspensión); providencia y plazos; garantías. 11. **Standard.**
- Norms: LGT arts. 28, 62.5, 77–82, 160–168; RGR arts. 69–76; Ley 31/2022 (interest, annual).
- Asked: LGT 28 (×3 incl. 28.2 and 28.5), 62.2 and 62.5 (×3), 81, 161, 65.5, 163.2, 164.1, 168; RGR 46.1.
- Worked examples: recargos ejecutivo, de apremio reducido y ordinario (art. 28.2–4) with the plazos of art. 62.5.

**III.12 `m03-l12`** — Embargo; facultades; diligencias y oposición; práctica; depósito y enajenación; responsables;
sucesores. 24. **Full.**
- Norms: LGT arts. 162, 165, 169–177, 39–43 (responsables, as procedure cites them); RGR arts. 75–118, 124–127; LEC
  arts. 605–607.
- Asked: LGT 165.4, 169, 170.1, 170.3 (×3), 171.2, 177; RGR 76.5, 80.4, 85 (×2), 92.4, 97.6, 101.2, 101 and 104.4,
  103 bis.1, 104, 104 bis, 105.2, 107.1, 117.2, 127.1.d).

### G6

**III.13 `m03-l13`** — Potestad sancionadora; principios; sujetos; infracciones y sanciones; cuantificación;
extinción; procedimiento. 20. **Full.**
- Norms: LGT arts. 178–212; RGRST arts. 1–36 as asked.
- Asked: LGT 27, 179.2 (×2), 180.3 (×2), 184.3.a), 187.1 (×2), 188.1 and 3 (×2), 189.1, 191.2 (×2), 192, 194.1 (×3),
  208.1, 211.1, 211.2 and 4, 212.3.
- Worked examples: graduación (art. 187) and reducciones (art. 188.1 and 3) of a sanction.

**III.14 `m03-l14`** — Revisión en vía administrativa; reposición; reclamaciones económico-administrativas; tribunales.
18. **Standard.**
- Norms: LGT arts. 213–249; RGRVA arts. 1–9 (as procedures need), 21–25 (reposición), 28–34 (tribunales).
- Asked: LGT 212.3, 213.3 (×2), 216, 217.1, 217.2, 217.6, 219 (×2), 221.1, 222.2 (×2), 225, 225.1 and 4, 233.4–5,
  234.4, 235–236, 244.1.
- Worked example: plazos of the recurso de reposición and the reclamación (arts. 223.1, 235.1), from the
  notification date.

### G7

**III.15 `m03-l15`** — IRPF (I): naturaleza, objeto, ámbito; sujeción; rendimientos del trabajo, capital mobiliario e
inmobiliario, actividades económicas; imputación de rentas inmobiliarias; ganancias y pérdidas. 22. **Full.**
- Norms: LIRPF arts. 1–39, 85, DA 55.ª (RDL 29/2026); RIRPF arts. 1–43 as asked; módulos orders (annual).
- Asked: LIRPF 7 (×4 incl. f), h), j), x)), 12–13, 14.2.a), 16.2–3, 17.1.d), 19.2 (×3), 25.1, 25.3, 31.1.5.ª, 32.3,
  33.4–5 (×2), 42.2, 43.1.1.º, 85; RIRPF 2, 14.2.a).

**III.16 `m03-l16`** — IRPF (II): clases de renta; integración y compensación; bases liquidables; mínimos; cálculo del
impuesto estatal; cuota diferencial; tributación familiar; gestión. 14. **Standard.**
- Norms: LIRPF arts. 44–70, 79–84, 96–105; RIRPF arts. 61–68 and gestión as asked.
- Asked: LIRPF 46, 50.1, 52.1, 57, 60.1, 81, 81 bis (×2), 82.1 (×3), 96, 96.2–3, 97.6, 103.1.

### G8

**III.17 `m03-l17`** — Impuesto sobre Sociedades. 8. **Focused**, every programme phrase at its article's depth.
- Norms: LIS arts. 1–11, 17–20 (as asked), 26–34, 40–41, 124–127; RIS as asked.
- Asked: LIS 7.1, 7.2, 9.3 and 110.1, 17.1, 20, 26.1, 32.1, 40.1.

### G9

**III.18 `m03-l18`** — IVA (I): naturaleza, ámbito; hecho imponible; exenciones; lugar. 15. **Standard.**
- Norms: LIVA arts. 1–12, 13 (adquisiciones intracomunitarias, as asked), 20–25, 68–70; RIVA as asked.
- Asked: LIVA 7, 7.5.º, 7.6.º, 8.Dos (×3), 9.1.º and 9.1.º c), 12 (×2), 13.2.º, 20.Uno.5.º, 18.º a), 22.º, 20.Dos,
  21–22.

**III.19 `m03-l19`** — IVA (II): sujetos pasivos; repercusión; devengo; base; deducciones; sectores diferenciados;
prorrata; regularización de bienes de inversión; devoluciones. 18. **Standard.**
- Norms: LIVA arts. 75–118; RIVA as asked; RD 1619/2012 where repercusión needs the invoice.
- Asked: LIVA 75.Uno.1.º, 75.Uno.4.º, 75.Dos, 78, 78.Dos (×2), 78.Tres.3.º, 80.Uno, 80.Cuatro, 84.Uno.2.º e), 88.Cuatro,
  89.Uno, 93.Cuatro, 95.Tres.2.ª, 99.Tres (×2), 103.Dos.2.º, 104.Tres, 108.
- Worked examples: prorrata general (art. 104) and regularización of a bien de inversión (arts. 107–109).

### G10

**III.20 `m03-l20`** — La Aduana: representación aduanera; deuda aduanera de importación y exportación; inclusión en un
régimen aduanero: disposiciones generales. 11. **Standard.**
- Norms: CAU arts. 5, 18–21, 77–88, 139–149 (presentación y depósito temporal, as asked), 158–163, 210–211,
  233–240 (tránsito, as asked); Reglamentos 2015/2446 and 2015/2447 where the CAU defers to them (cited by article
  as written; the source indexer does not index their XHTML: list for section M).
- Asked: CAU 5.5, 5.26, 18.1, 70.1, 71.1.e), 72.a), 144, 149, 158.1, 233.4.a), 237 and 240.

## Per group, the same steps

1. Writer (sonnet) writes the group's temas in sequence (spec § Writer), notes in `r2-tax/<lesson>/writer.md`.
2. `tools/taxprov.py plan` → `r2-tax/<lesson>/pending.md`; C1/C2-identical sentences inherit.
3. Blind verifier (opus), batches of 60 → `r2-tax/<lesson>/verify.md`; worked examples recomputed.
4. FAILs applied (`taxprov.py apply`), re-checked by a different verifier → `verify-recheck-N.md`; after two failed
   re-checks the sentence is dropped and listed.
5. Coverage check (opus) of the group's coverage questions → `r2-tax/<lesson>/coverage.md`; misses fixed by the same
   rules.
6. Summaries in `course.yaml` (blind-checked), glossary entries (verified), records (`taxprov.py record`).
7. `close_round.sh`; goldens read; C1, C2, crypto-futures and Android unchanged; ledger and «where to resume» updated.
