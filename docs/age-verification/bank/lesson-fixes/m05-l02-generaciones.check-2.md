# m05-l02 «Generaciones de crédito»: blind check, round 2

Verifier run of 2026-10-30. Texts read: arts. 53, 62 and 63 LGP (`BOE-A-2003-21614_lgp_2022-12-24.pdf`,
`pdftotext -layout`); arts. 1.a) and 9 Ley 31/2022 (`BOE-A-2022-22128_pge-2023_2026-09-30.html`). Lesson read at its
working-tree state (diff against HEAD covers lines 205, 286, 288 and 393). `docs/prose-voice.md` read.

Norm text that decides:

- Art. 63.1.b) LGP: titulares de los ministerios, «previo informe favorable de la Intervención Delegada», authorise
  «Generaciones de crédito en los supuestos contemplados en los párrafos a), d) y f) del apartado 2 del artículo 53».
- Art. 62.1.b) LGP: the Ministro de Hacienda, «Las generaciones previstas en el párrafo c) … y las que corresponda
  realizar en el Presupuesto del Estado en los supuestos definidos en los párrafos b) y e)».
- Art. 63.2 LGP: presidentes y directores of the organismos autónomos exercise, «referidas a sus respectivos
  presupuestos, las relativas a las generaciones contenidas en los párrafos b) y e) … así como las establecidas en este
  artículo a favor de los ministros, quienes podrán avocarlas en todo o en parte».
- Art. 9.Dos.8 Ley 31/2022: the titular of Hacienda authorises «las variaciones o modificaciones presupuestarias que se
  realicen en el presupuesto de las entidades referidas en los apartados 1.º, 2.º y 4.º de la letra a) del artículo 1
  …, cuando las mismas afecten a créditos del Capítulo 4 …, del Capítulo 7 … o del Capítulo 8 …, excepto que la
  normativa presupuestaria atribuya su competencia al Consejo de Ministros o requiera la remisión de un proyecto de ley
  a las Cortes Generales, a excepción de lo previsto en el apartado Cinco del presente artículo». Art. 1.a): 1.º Estado,
  2.º organismos autónomos, 3.º Seguridad Social (not covered), 4.º agencias y resto con presupuesto limitativo.
- Art. 9.Cinco: titulares or presidentes authorise in their budgets «las transferencias de crédito o las variaciones
  presupuestarias que afecten a las transferencias corrientes y de capital» when the perceptor's legal nature differs
  from the convocatoria.
- Art. 53.4 LGP: «Los ingresos procedentes de reembolso de préstamos únicamente podrán dar lugar a generaciones en
  aquellos créditos destinados a la concesión de nuevos préstamos» (chapter 8).

## Part 1 — lesson

| Lesson text | Verdict | Reason |
|---|---|---|
| Table row 1 (l. 286): «a), d) y f) \| Titular del ministerio, previo informe favorable de la Intervención Delegada, salvo las que afecten a los capítulos 4, 7 u 8, que autoriza el Ministro de Hacienda (salvo el art. 9.Cinco) \| art. 63.1.b) LGP; art. 9.Dos.8 Ley 31/2022» | PASS | Letters and informe are 63.1.b). The «salvo las que» is plural feminine, so it attaches to the generaciones (the competence), not to the singular «informe». Chapters 4/7/8 and the Cinco carve-out are Dos.8; the Consejo de Ministros / proyecto de ley carve-out is left out, which is harmless because no generación goes to either. Both citations hold. Spanish correct; the nested «salvo … (salvo …)» is dense but unambiguous. |
| Table row 2 (l. 287, unchanged): «c), y b) y e) en el presupuesto del Estado \| Ministro de Hacienda, salvo las que la Ley 31/2022 atribuye a otros órganos \| art. 62.1.b) LGP; art. 9.Tres, Cuatro y Ocho Ley 31/2022» | PASS | Verbatim scope of 62.1.b). Dos.8 gives these to the same Ministro de Hacienda, so it does not need to appear here. |
| Table row 3 (l. 288): «b) y e), y las de los párrafos a), d) y f) que el art. 63.1.b) da a los ministros, en su presupuesto \| Presidente o Director del organismo autónomo, salvo las que afecten a los capítulos 4, 7 u 8, que autoriza el Ministro de Hacienda (salvo el art. 9.Cinco); el ministro puede avocar las demás en todo o en parte \| art. 63.2 LGP; art. 9.Dos.8 Ley 31/2022» | PASS | Letters, budget and avocation are 63.2 («quienes podrán avocarlas en todo o en parte»). The chapter exception comes right after «Presidente o Director», so it limits the presidente's competence. «avocar las demás» then limits the avocation to what is left, which is right: what Dos.8 gives Hacienda is not the presidente's, so the ministro cannot avocate it. Organismos autónomos are art. 1.a).2.º, inside Dos.8. Both citations hold. |
| Summary row (l. 205): «Generación \| Titular del ministerio, Ministro de Hacienda o Presidente o Director del organismo, según el ingreso y el capítulo del crédito (arts. 62.1.b), 63.1.b) y 63.2 LGP; art. 9.Dos.8 Ley 31/2022) \| …» | PASS | The three organs are the full set (Tres and Cuatro give the titular de Defensa / Sanidad, Ocho the titular or presidente: same organs). «según el ingreso y el capítulo del crédito» now names both criteria; Dos.8 cited. |
| «Lo que más cae» (l. 393): «La generación por aportación del Estado a un organismo autónomo la autoriza su Presidente o Director; el ministro puede avocarla, salvo que afecte a créditos de los capítulos 4, 7 u 8, que autoriza el Ministro de Hacienda (arts. 53.2.a), 63.1.b) y 63.2 LGP; art. 9.Dos.8 Ley 31/2022).» | FAIL | The exception sits in the avocation clause. A learner reads «el ministro puede avocarla, salvo que afecte a créditos de los capítulos 4, 7 u 8» as a limit on the avocation, while the first clause still says flatly that the presidente authorises. Dos.8 removes the competence itself: the titular de Hacienda authorises «las variaciones o modificaciones presupuestarias que se realicen en el presupuesto de las entidades referidas en los apartados 1.º, 2.º y 4.º … cuando las mismas afecten a créditos del Capítulo 4 …, del Capítulo 7 … o del Capítulo 8». The citations hold; the attachment does not. Same order as row 3 would fix it, e.g. «… la autoriza su Presidente o Director, salvo que afecte a créditos de los capítulos 4, 7 u 8, que la autoriza el Ministro de Hacienda; en los demás casos el ministro puede avocarla (…)». |

Voice: none of the changed lines uses a filler, triad, rhetorical question, «no solo… sino», closer or stacked hedge.
«salvo» repeated within a cell is repetition, not a fault. Normativa list (l. 401) already carries Dos.8 and Cinco.

Notes that do not change a verdict:

- «(salvo el art. 9.Cinco)» copies Dos.8's carve-out; Cinco speaks of «variaciones presupuestarias que afecten a las
  transferencias corrientes y de capital» when the perceptor's nature changes, which a generación by ingresos rarely is.
  Faithful to the norm, opaque to a learner; acceptable in a table.
- Seguridad Social (art. 1.a).3.º) is outside Dos.8 and art. 63.3.a) gives it its own rule; still not in the table, as
  in round 1.
- Art. 9.Ocho (gastos comunes, titular or presidente) is cited in row 2 but not in rows 1 and 3; where such a
  generación lands in chapter 4, Ocho and Dos.8 overlap. Edge case, not a fault in a summary table.

## Part 2 — round 1 FAILs

| Round 1 FAIL | Round 2 change | Resolved |
|---|---|---|
| Table row 1: no Dos.8 exception | Exception and citation added | Yes |
| Table row 3: no Dos.8 exception | Exception added to the presidente's competence, avocation narrowed to «las demás», citation added | Yes |
| «Lo que más cae» line: stated flatly despite Dos.8 | Exception and citation added, but placed after «el ministro puede avocarla» | No: the exception attaches to the avocation, not to the competence |

The round 1 note on the summary row («según el ingreso» not the whole criterion; no Ley 31/2022 citation) is also
resolved. Change log `m05-l02-generaciones.md` round 2 entries 1–4 match the working tree.

Summary: 5 checked, 4 PASS, 1 FAIL (l. 393).

## Check 3

Line (l. 393): «La generación por aportación del Estado a un organismo autónomo la autoriza su Presidente o Director, salvo que afecte a créditos de los capítulos 4, 7 u 8, en cuyo caso la autoriza el Ministro de Hacienda; en los demás casos el ministro puede avocarla (arts. 53.2.a), 63.1.b) y 63.2 LGP; art. 9.Dos.8 Ley 31/2022).»

Verdict: PASS.

- The exception now follows «Presidente o Director», so it limits the competence, as art. 9.Dos.8 does («variaciones o modificaciones presupuestarias … en el presupuesto de las entidades referidas en los apartados 1.º, 2.º y 4.º … cuando las mismas afecten a créditos del Capítulo 4 …, 7 … u 8»).
- «en los demás casos el ministro puede avocarla» confines the avocation of art. 63.2 («quienes podrán avocarlas en todo o en parte») to what stays with the presidente, matching table row 3.
- Citations hold: 53.2.a) is the aportación del Estado to organismos autónomos; 63.1.b) gives the ministers a), d), f); 63.2 passes them to presidentes/directores with avocation; Dos.8 covers organismos autónomos (art. 1.a).2.º).
- Spanish correct and Peninsular; «en cuyo caso» / «en los demás casos» are clear. Voice: no filler, triad, rhetorical question, closer or stacked hedge.
- Note, not a fault: Dos.8's Cinco and Consejo de Ministros carve-outs are left out, as in check 2 accepted for a summary bullet; «el ministro» means the departmental minister by context.
