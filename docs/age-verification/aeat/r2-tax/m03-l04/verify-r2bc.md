# Blind check of the R2b/R2c edits — m03-l04, 2026-11-11

Verifier spec `docs/age-verification/aeat/r2b/verify/spec.md`. One scope note and four esquemas (all tabla, each right
after the paragraphs it summarises): baja en el Censo (art. 11 RGAT), cambio de domicilio fiscal (art. 17 RGAT),
derechos que prescriben (arts. 66 and 66 bis LGT), cómputo (art. 67 LGT).

| id | verdict | reason | replacement |
|---|---|---|---|
| `0330d6d632` | PASS | Header; columns fit the rows. | |
| `a80a44d560` | PASS | Art. 11.1 RGAT («Quienes cesen en el desarrollo de todo tipo de actividades empresariales o profesionales o, no teniendo la condición de empresarios o profesionales, dejen de satisfacer rendimientos sujetos a retención o ingreso a cuenta…») and 11.2 («en el plazo de un mes desde que se cumplan las condiciones previstas en el apartado 1»). Faithful; in the prose with both citations. | |
| `71e60d84db` | PASS | Art. 11.3 RGAT: «Cuando una sociedad o entidad se disuelva, la declaración de baja deberá ser presentada en el plazo de un mes desde que se haya realizado, en su caso, la cancelación efectiva de los correspondientes asientos en el Registro Mercantil.» Verbatim; in the prose. | |
| `2f6af3d478` | PASS | Art. 11.4 RGAT: «los herederos deberán presentar la declaración de baja correspondiente en el plazo de seis meses desde el fallecimiento». Faithful, quotation as in the prose. | |
| `a23b46b1aa` | PASS | Note heads «Obligaciones y deberes de la Administración tributaria» (arts. 30–33 LGT); tema III.4 literal names the obligaciones formales, derechos y garantías of the obligados, obligados, capacidad, representación, domicilio and prescripción, not the Administración's obligations. 2025-43 exists (art. 31.2 LGT, intereses de demora on a devolución derivada de la normativa del tributo; key B), `vigente`; answering needs the section's art. 31.2 sentence (six months, interest «sin necesidad de que el obligado lo solicite»). | |
| `6b75d75488` | PASS | Header; columns fit the rows. | |
| `e27d3d40d3` | PASS | Art. 17.1 RGAT: «Las personas físicas que deban estar en el Censo de Empresarios, Profesionales y Retenedores, así como las personas jurídicas y demás entidades deberán cumplir la obligación de comunicar el cambio de domicilio fiscal… en el plazo de un mes a partir del momento en que produzca dicho cambio.» Faithful; in the prose. | |
| `2ee25e2671` | FAIL | Art. 17.2 RGAT: «…la comunicación del cambio de domicilio se deberá efectuar en el plazo de tres meses desde que se produzca…, salvo lo dispuesto en el párrafo siguiente», and that paragraph: in the State's competence, «si con anterioridad al vencimiento de dicho plazo finalizase el de presentación de la autoliquidación o comunicación de datos correspondiente a la imposición personal…, la comunicación deberá efectuarse en el correspondiente modelo de autoliquidación o comunicación de datos». The row gives the three months without that exception, which can bring the communication forward; the prose (art. 17.2 RGAT sentence) has the same gap. Drop until the prose has it (gap: m03-l04, art. 17.2 párrafo segundo RGAT). | drop |
| `313dbacaa0` | PASS | Header; columns fit the rows. | |
| `ac3e2e8143` | PASS | Art. 66.a) LGT verbatim, «cuatro años» from the opening; in the prose. | |
| `276f758a52` | PASS | Art. 66.b) LGT verbatim; in the prose. | |
| `cefb4967d3` | PASS | Art. 66.c) LGT verbatim; in the prose. | |
| `26b04c815c` | PASS | Art. 66.d) LGT verbatim; in the prose. | |
| `f8d136ca3a` | PASS | Art. 66 bis.2 LGT, first paragraph: «prescribirá a los diez años a contar desde el día siguiente a aquel en que finalice el plazo reglamentario establecido para presentar la declaración o autoliquidación correspondiente al ejercicio o periodo impositivo en que se generó el derecho a compensar dichas bases o cuotas o a aplicar dichas deducciones». Faithful, same wording as the prose. | |
| `120d3f1e63` | PASS | Header; the two responsables rows are the derecho b) of art. 66 applied to responsables (art. 67.2 starts «sin perjuicio» of b)), so «Derecho del art. 66» still fits. | |
| `bbe4ffd2f1` | PASS | Art. 67.1 LGT, caso a) and the cobro periódico por recibo rule. Faithful; in the prose. | |
| `38782df0bc` | PASS | Art. 67.1 LGT, caso b), including «sin perjuicio de lo dispuesto en el apartado 2». In the prose. | |
| `e341876f1d` | PASS | Art. 67.1 LGT, caso c), all three starting points and the incompatible-tributos rule; quotation as in the prose. | |
| `9a1c737886` | PASS | Art. 67.1 LGT, caso d), verbatim; in the prose. | |
| `d2fae7fb34` | PASS | Art. 67.2 LGT, first two paragraphs (solidarios and the later presupuesto de la responsabilidad). Faithful; in the prose. | |
| `e455382bf3` | PASS | Art. 67.2 LGT, third paragraph: «desde la notificación de la última actuación recaudatoria practicada al deudor principal o a cualquiera de los responsables solidarios». Verbatim; in the prose. | |
| title m03-l04 «Plazos de la declaración de baja en el Censo de Empresarios, Profesionales y Retenedores» | PASS | The three plazos of art. 11.2–4 RGAT; complete for the Censo. | |
| title m03-l04 «Plazos de la comunicación del cambio de domicilio fiscal» | PASS | Accurate for art. 17.1–2 RGAT (the row defect is reported under `2ee25e2671`). | |
| title m03-l04 «Derechos que prescriben y plazo» | PASS | Rows are the four rights of art. 66 («Prescribirán a los cuatro años los siguientes derechos») plus art. 66 bis.2, under «Plazos de prescripción». | |
| title m03-l04 «Desde cuándo se cuenta el plazo de prescripción» | PASS | Art. 67 heading «Cómputo de los plazos de prescripción»; every rule of 67.1–2 is a row. | |
