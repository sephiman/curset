# m05-l02 «Generaciones de crédito»: blind check of who authorises a generación

Verifier run of 2026-10-30. Texts read with `pdftotext -layout`: arts. 43, 52, 53, 56, 61, 62 and 63 LGP
(`BOE-A-2003-21614_lgp_2022-12-24.pdf`) and arts. 1 and 9 Ley 31/2022 (`BOE-A-2022-22128_pge-2023_2026-09-30.html`).
`sources/normativa.yaml`: the LGP has `cambios_pendientes: []` and no 2025-2026 amendment; the Ley 31/2022 entry and
the Orden HAC/557/2026 note record no later Ley de PGE, so the 2023 law rules by extension. None of the recorded
amendments of the Ley 31/2022 touches art. 9.

The norm text that decides part 1:

- Art. 63.1.b) LGP: the titulares de los ministerios authorise, «previo informe favorable de la Intervención
  Delegada», «Generaciones de crédito en los supuestos contemplados en los párrafos a), d) y f) del apartado 2 del
  artículo 53».
- Art. 62.1.b) LGP: the Ministro de Hacienda authorises «Las generaciones previstas en el párrafo c) del apartado 2 del
  artículo 53 y las que corresponda realizar en el Presupuesto del Estado en los supuestos definidos en los párrafos
  b) y e)».
- Art. 63.2 LGP: presidentes y directores de los organismos autónomos (and the other art. 3.1 entities) exercise, «referidas
  a sus respectivos presupuestos, las relativas a las generaciones contenidas en los párrafos b) y e) del apartado 2
  del artículo 53, así como las establecidas en este artículo a favor de los ministros, quienes podrán avocarlas en
  todo o en parte».
- Art. 63.3.a) LGP: in the Seguridad Social, its presidentes y directores authorise «Las generaciones de crédito a que
  se refiere el artículo 53, excepto en el supuesto del apartado 2.c)».
- Art. 9 Ley 31/2022: Tres (Defensa, 53.2.b) for the listed ingresos), Cuatro (Sanidad, 53.2.b) for the DA 10.ª TRLGSS
  ingresos), Ocho (titulares de los departamentos and presidentes o directores, «las generaciones de crédito que
  tengan por objeto financiar gastos comunes de edificios compartidos y servicios horizontales…»), and **Dos.8**:
  the persona titular del Ministerio de Hacienda authorises «las variaciones o modificaciones presupuestarias que se
  realicen en el presupuesto de las entidades referidas en los apartados 1.º, 2.º y 4.º de la letra a) del artículo 1
  [Estado, organismos autónomos, agencias y resto con presupuesto limitativo] …, cuando las mismas afecten a créditos
  del Capítulo 4 «Transferencias corrientes», del Capítulo 7 «Transferencias de capital» o del Capítulo 8 «Activos
  financieros», excepto que la normativa presupuestaria atribuya su competencia al Consejo de Ministros o requiera la
  remisión de un proyecto de ley a las Cortes Generales».

Dos.8 is not in the lesson and not in the fix note. It takes away from the ministro and from the presidente o director
every generación whose credit is in chapter 4, 7 or 8. Every 53.2.d) generation falls there: «Los ingresos procedentes
de reembolso de préstamos únicamente podrán dar lugar a generaciones en aquellos créditos destinados a la concesión de
nuevos préstamos» (art. 53.4 LGP), which are chapter 8.

## Part 1 — lesson

| Lesson text | Verdict | Reason |
|---|---|---|
| Table row 1: «a), d) y f) \| Titular del ministerio, previo informe favorable de la Intervención Delegada \| art. 63.1.b) LGP» | FAIL | Exact for the LGP, but stated with no exception while the Ley 31/2022 is in force: art. 9.Dos.8 gives the Ministro de Hacienda the modificaciones of the Estado and the organismos «cuando las mismas afecten a créditos del Capítulo 4 …, del Capítulo 7 … o del Capítulo 8», so a d) generation (always chapter 8, art. 53.4) and any a) or f) one in those chapters is not the ministro's. Row 2 carries a «salvo» for the Ley 31/2022; this row needs one too. |
| Table row 2: «c), y b) y e) en el presupuesto del Estado \| Ministro de Hacienda, salvo las que la Ley 31/2022 atribuye a otros órganos \| art. 62.1.b) LGP; art. 9.Tres, Cuatro y Ocho Ley 31/2022» | PASS | First cell is art. 62.1.b) word for word. Tres (Defensa), Cuatro (Sanidad) and Ocho (gastos comunes) are the exceptions that move these generaciones to other organs; Dos.8 gives the Ministro de Hacienda anyway, so it does not change this row. |
| Table row 3: «b) y e), y las de los párrafos a), d) y f) que el art. 63.1.b) da a los ministros, en su presupuesto \| Presidente o Director del organismo autónomo; el ministro puede avocarlas en todo o en parte \| art. 63.2 LGP» | FAIL | Letters, budget and avocation match art. 63.2 («quienes podrán avocarlas en todo o en parte»). It is again stated with no Ley 31/2022 exception: art. 9.Dos.8 gives the Ministro de Hacienda the modificaciones of the organismos autónomos (art. 1.a).2.º) affecting chapters 4, 7 and 8, so these generaciones are not the presidente's there. |
| Summary row near line 205: «Generación \| Titular del ministerio, Ministro de Hacienda o Presidente o Director del organismo, según el ingreso (arts. 62.1.b), 63.1.b) y 63.2 LGP) \| …» | PASS | The three organs are the full set (Tres, Cuatro, Ocho and Dos.8 only move generaciones between these same organs), each held by a cited article. Note: «según el ingreso» is not the whole criterion under Dos.8 (the chapter also decides), and the transferencia row below cites «art. 9 Ley 31/2022» while this one does not. |
| «Lo que más cae»: «La generación por aportación del Estado a un organismo autónomo la autoriza su Presidente o Director; el ministro puede avocarla (arts. 53.2.a), 63.1.b) y 63.2 LGP).» | FAIL | Right by the LGP (63.1.b) a) to the ministro, 63.2 passes it to the presidente, avocable; the official conv2025_A sup. II 12 keys the same for the INAP). Stated flatly while art. 9.Dos.8 Ley 31/2022 gives the Ministro de Hacienda the generación when the credit generated is in chapter 4, 7 or 8. |

Notes that do not change a verdict:

- No row covers the Seguridad Social. There art. 63.3.a) gives every 53.2 generación except c) to its presidentes y
  directores, avocable by the ministro. Row 1 («titular del ministerio» for a), d), f)) reads as if it held there too.
- Art. 63.1, third paragraph: the presidentes de los órganos del Estado con secciones diferenciadas hold the same
  competencias for their sección. Not in the table; acceptable as a reduction.
- Fix note (`m05-l02-generaciones.md`): its two changes are correct by art. 63.2 and 63.1.b); its «Left as is» reading
  of row 1 («exact») and of the summary row holds for the LGP only, since it does not consider art. 9.Dos.8.

## Part 2 — questions

Bank questions against `official/V.2.md`; case questions against their scenario and `official/V.2.md`. Word counts and
option lengths computed; all within limits (q176 option «El Ministro de Hacienda.» is an organ under five words, ruling).

| id | 1 key | 2 unique | 3 citation | 4 style | 5 not official | verdict | reason |
|---|---|---|---|---|---|---|---|
| m05-l02-q151 | PASS | PASS | PASS | PASS | PASS | PASS | Key is 63.1.b) «Intervención Delegada competente en el ministerio». |
| m05-l02-q152 | PASS | PASS | PASS | PASS | PASS | PASS | a), d), f) = aportaciones, reembolsos, reintegros; each distractor carries a c), b) or e) supuesto. |
| m05-l02-q154 | PASS | PASS | PASS | PASS | PASS | PASS | 62.1.b): c) plus b) and e) in the Estado. |
| m05-l02-q176 | PASS | PASS | PASS | PASS | PASS | PASS | 62.1.b) gives c) without limiting it to the Estado; 63.2 gives the presidente only b), e) and the ministerial a), d), f). Dos.8 Ley 31/2022 also points to Hacienda. |
| m05-l02-q242 | PASS | PASS | PASS | PASS | PASS | PASS | 63.2 «quienes podrán avocarlas en todo o en parte»; conv2025_A sup. II 12 asks who authorises, not who avocates, with other options. |
| m05-l02-q291 | PASS | PASS | PASS | PASS | PASS | PASS | Right «según el artículo 63.1.b)». Note: in force, a d) generation lands in chapter 8 (art. 53.4) and art. 9.Dos.8 Ley 31/2022 gives it to the Ministro de Hacienda; the stem's article scope keeps the key, no distractor becomes true. |
| m05-l02-q292 | PASS | PASS | PASS | PASS | PASS | PASS | 53.2.a) covers «otras personas naturales o jurídicas al Estado»; 63.1.b) gives a) to the ministro; 53.3 limits the compromiso firme to organismos and Seguridad Social. Note: no norm named; under art. 9.Dos.8 a chapter 4/7/8 credit would go to Hacienda, but distractor b) stays wrong by its own reason («porque el ingreso procede de una persona jurídica privada»). |
| m05-l02-q293 | PASS | PASS | PASS | PASS | PASS | PASS | 63.2 + 63.1.b) give the presidente the a) aportación del Estado; c) is Hacienda's; a loan received is no 53.2 ingreso; remanentes go by art. 58. Same Dos.8 note as q291, scoped by the article named. |
| m05-l02-q301 | PASS | PASS | PASS | PASS | PASS | PASS | 63.1.a) + 63.2; chapter 2 to 6 is not 52.1.a) or 9.Dos.6 (capital to corrientes) or Dos.8 (chapters 4/7/8); chapter 6 is not an art. 43.2 credit. |
| m05-l02-q308 | PASS | PASS | PASS | PASS | PASS | PASS | 9.Tres: «corresponde a la persona titular del Ministerio de Defensa autorizar las generaciones … 53.2.b) … ventas de productos farmacéuticos o de prestación de servicios hospitalarios». |
| sp-02/q19 | PASS | PASS | PASS | PASS | PASS | PASS | A January 2027 payroll overpayment returned in 2027 is 53.2.f); 63.1.b) gives it to the titular del ministerio with the ID report; payroll is chapter 1, so Dos.8 does not apply. Check 5: conv2020 sup. II 13 asks only which figure (generación vs incorporación/ampliación); here the stem adds the organ and two options share the key's figure, so the stem is not near-identical. |
| sp-10/q17 | PASS | PASS | PASS | PASS | PASS | PASS | Chapter 2, same programme, no personal, Ministry does not avocate: 63.1.a) + 63.2 give it to the Presidencia del FEGA; Dos.8 (chapters 4/7/8) and Dos.6 do not apply. Note: the scenario does not exclude an art. 43.2 credit (protocolo, arrendamientos) being increased; the ordinary reading is the one keyed. |

Summary: 12 checked, 12 PASS, 0 FAIL. No line appended to `bloque-v/drops.tsv` or `cases/drops.tsv`.
