# Currency check C1a — normativa (age-administrativo-c1)

Date: 2026-10-17. Source list: `content/age-administrativo-c1/sources/normativa.yaml` (93 entries: 89 with `boe_id`,
4 EU norms with `celex`). Method: for every `boe_id`, the «Última actualización publicada el …» line of
`https://www.boe.es/buscar/act.php?id=<ID>` and the `posteriores` of
`https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/<ID>/analisis` (JSON), fetched by a script; every
`posterior` with a 2025 or 2026 id was dated from `diario_boe/xml.php` and compared with the stored date. BOE section I
sumarios of 14, 15, 16 and 17-10-2026 were read by hand for norms too new to appear in the análisis. EU norms: the
EUR-Lex «Current consolidated version» line and the Publications Office (Cellar) notices of each consolidation.

## Summary

- **No BOE norm is newer.** For all 89 `boe_id` entries the latest «Última actualización publicada» on boe.es equals
  the stored `consolidated_as_of`. No modification published after a stored date is missing from the stored file,
  except the annex changes to Ley 38/1988 that boe.es itself does not consolidate (already recorded in
  `amended_2025_2026`).
- **Three EU entries are newer on EUR-Lex**: TUE and TFUE (consolidated 15-03-2025; changes only to Protocols No 3
  and No 5) and the Council's Rules of Procedure (consolidated 01-01-2026; annex III every year, arts. 11 and 12).
  No article the lessons cite changes.
- Not textual modifications, recorded for awareness: RDL 13/2026 (BOE-A-2026-11848) and RDL 30/2026
  (BOE-A-2026-21318, published 14-10-2026) are «se dicta en relación» with arts. 21, 23, 25 and 32 LO 2/2012. No lesson
  cites those articles. Corrección de errores del RD 707/2026 (BOE-A-2026-21525, 16-10-2026) corrects only the
  preamble («oído el Consejo de Estado» → «de acuerdo con el Consejo de Estado»); RD 707/2026 is the modifying norm
  of the RD 366/2007 cambio pendiente, and no cited article changes.
- Entries without a consolidated text (Acuerdo CM 15-07-2005 BOE-A-2005-13337, Orden HAC/1517/2025, RDL 14/2025
  [`unverified: true`], Resolución 02-12-2005): boe.es still has none (análisis 404, no «Texto consolidado» on
  act.php). RDL 14/2025 has no later modification (only its convalidación and an application resolution).
- No cambio pendiente has entered into force, and no «(desde …)» date has passed on 2026-10-17.

## Norms

| Norm | ID | Stored date | Latest on boe.es | Newer? | Modifying norms | Articles changed |
|---|---|---|---|---|---|---|
| CE | BOE-A-1978-31229 | 2026-05-20 | 2026-05-20 | No | None | — |
| LO 2/1979 (LOTC) | BOE-A-1979-23709 | 2024-08-02 | 2024-08-02 | No | None | — |
| LO 3/1981 (Defensor del Pueblo) | BOE-A-1981-10325 | 2009-11-04 | 2009-11-04 | No | None | — |
| Reglamento del Congreso | BOE-A-1982-5196 | 2026-07-28 | 2026-07-28 | No | None | — |
| Reglamento del Senado | BOE-A-1994-10830 | 2025-11-14 | 2025-11-14 | No | None | — |
| LOPJ (LO 6/1985) | BOE-A-1985-12666 | 2025-02-17 | 2025-02-17 | No | None | — |
| Ley 38/1988 (Demarcación y Planta) | BOE-A-1988-29622 | 2025-01-03 | 2025-01-03 | No | No consolidated update; RD 388/2025, 422/2025, 930/2025 and 559/2026 change annexes II–VIII and XIII, boe.es does not consolidate them (already listed in amended_2025_2026) | — |
| LO 1/2025 (eficiencia de la Justicia) | BOE-A-2025-76 | 2025-06-04 | 2025-06-04 | No | None | — |
| Ley 50/1997 (Gobierno) | BOE-A-1997-25336 | 2025-01-03 | 2025-01-03 | No | None | — |
| Ley 19/2013 (transparencia) | BOE-A-2013-12887 | 2022-07-09 | 2022-07-09 | No | None | — |
| RD 615/2024 (Estatuto del CTBG) | BOE-A-2024-15944 | 2026-09-18 | 2026-09-18 | No | None | — |
| Ley 40/2015 (LRJSP) | BOE-A-2015-10566 | 2024-08-02 | 2024-08-02 | No | None | — |
| Ley 2/2014 (Acción y Servicio Exterior) | BOE-A-2014-3248 | 2018-06-12 | 2018-06-12 | No | None | — |
| Ley 3/2015 (alto cargo) | BOE-A-2015-3444 | 2026-09-18 | 2026-09-18 | No | None | — |
| RD 829/2023 (departamentos ministeriales) | BOE-A-2023-23537 | 2023-12-29 | 2023-12-29 | No | None | — |
| RD 1009/2023 (estructura orgánica básica) | BOE-A-2023-24842 | 2026-07-29 | 2026-07-29 | No | None | — |
| LBRL (Ley 7/1985) | BOE-A-1985-5392 | 2026-10-03 | 2026-10-03 | No | None | — |
| RD 208/1996 (información administrativa) | BOE-A-1996-4997 | 2011-06-04 | 2011-06-04 | No | None | — |
| RD 951/2005 (calidad; quejas y sugerencias) | BOE-A-2005-14836 | 2009-06-30 | 2009-06-30 | No | None | — |
| RD 366/2007 (accesibilidad ante la AGE) | BOE-A-2007-6239 | 2026-09-03 | 2026-09-03 | No | None | — |
| LO 4/2001 (derecho de petición) | BOE-A-2001-21090 | 2011-07-28 | 2011-07-28 | No | None | — |
| RDL 1/2013 (TR derechos personas con discapacidad) | BOE-A-2013-12632 | 2026-10-03 | 2026-10-03 | No | None | — |
| RD 1708/2011 (Sistema Español de Archivos) | BOE-A-2011-18541 | 2024-03-27 | 2024-03-27 | No | None | — |
| Ley 16/1985 (Patrimonio Histórico) | BOE-A-1985-12534 | 2026-10-03 | 2026-10-03 | No | None | — |
| Ley 39/2015 (LPAC) | BOE-A-2015-10565 | 2024-11-06 | 2024-11-06 | No | None | — |
| RD 203/2021 (Reglamento de actuación por medios electrónicos) | BOE-A-2021-5032 | 2025-04-02 | 2025-04-02 | No | None | — |
| Orden HAP/1949/2014 (PAG) | BOE-A-2014-10908 | 2015-11-26 | 2015-11-26 | No | None | — |
| RD 127/2015 (ventanilla única empresarial) | BOE-A-2015-2671 | 2015-03-13 | no «Última actualización» line (never modified; consolidated text present) | No | None | — |
| RD 1112/2018 (accesibilidad web) | BOE-A-2018-12699 | 2019-08-12 | 2019-08-12 | No | None | — |
| RD 776/2011 (supresión de órganos colegiados) | BOE-A-2011-9736 | 2011-06-04 | no «Última actualización» line (never modified; consolidated text present) | No | None | — |
| Decreto 914/1969 (Archivo General de la Administración Civil) | BOE-A-1969-643 | 1969-05-26 | no «Última actualización» line (never modified; consolidated text present) | No | None | — |
| RD 1401/2007 (Comisión Superior Calificadora de Documentos Administrativos) | BOE-A-2007-19248 | 2017-05-23 | 2017-05-23 | No | None | — |
| RD 1164/2002 (eliminación de documentos) | BOE-A-2002-22192 | 2007-11-07 | 2007-11-07 | No | None | — |
| Acuerdo del Consejo de Ministros de 15-07-2005 (Red de Oficinas Integradas) | BOE-A-2005-13337 | 2005-08-03 | no consolidated text (análisis 404) | No | None | — |
| Ley 14/2013 (apoyo a los emprendedores) | BOE-A-2013-10074 | 2025-04-09 | 2025-04-09 | No | None | — |
| LOPDGDD (LO 3/2018) | BOE-A-2018-16673 | 2025-12-27 | 2025-12-27 | No | None | — |
| Código Civil | BOE-A-1889-4763 | 2025-01-03 | 2025-01-03 | No | None | — |
| LJCA (Ley 29/1998) | BOE-A-1998-16718 | 2025-01-03 | 2025-01-03 | No | None | — |
| LCSP (Ley 9/2017) | BOE-A-2017-12902 | 2026-04-09 | 2026-04-09 | No | None | — |
| Orden HAC/1517/2025 (umbrales de contratación) | BOE-A-2025-26605 | 2025-12-26 | no consolidated text (análisis 404) | No | None | — |
| Ley 60/2003 (Arbitraje) | BOE-A-2003-23646 | 2015-10-06 | 2015-10-06 | No | None | — |
| Ley 38/2003 (General de Subvenciones) | BOE-A-2003-20977 | 2026-10-03 | 2026-10-03 | No | None | — |
| LO 3/1980 (Consejo de Estado) | BOE-A-1980-8648 | 2024-08-02 | 2024-08-02 | No | None | — |
| LO 3/2007 (igualdad) | BOE-A-2007-6115 | 2024-08-02 | 2024-08-02 | No | None | — |
| LO 1/2004 (violencia de género) | BOE-A-2004-21760 | 2022-09-07 | 2022-09-07 | No | None | — |
| Ley 4/2023 (trans y LGTBI) | BOE-A-2023-5366 | 2023-03-01 | no «Última actualización» line (never modified; consolidated text present) | No | None | — |
| Ley 15/2022 (igualdad de trato) | BOE-A-2022-11589 | 2022-07-13 | no «Última actualización» line (never modified; consolidated text present) | No | None | — |
| Ley 39/2006 (dependencia) | BOE-A-2006-21990 | 2026-10-03 | 2026-10-03 | No | None | — |
| RD 803/2022 (Estatuto del INE) | BOE-A-2022-16198 | 2025-10-31 | 2025-10-31 | No | None | — |
| TREBEP (RDL 5/2015) | BOE-A-2015-11719 | 2026-10-03 | 2026-10-03 | No | None | — |
| Ley 30/1984 (reforma de la Función Pública) | BOE-A-1984-17387 | 2015-10-31 | 2015-10-31 | No | None | — |
| RD 1405/1986 (Registro Central de Personal) | BOE-A-1986-18101 | 2000-01-18 | 2000-01-18 | No | None | — |
| RD 2073/1999 (Reglamento del Registro Central de Personal) | BOE-A-2000-1007 | 2000-01-18 | no «Última actualización» line (never modified; consolidated text present) | No | None | — |
| RD 364/1995 (Reglamento General de Ingreso y Provisión) | BOE-A-1995-8729 | 2006-03-04 | 2006-03-04 | No | None | — |
| Resolución de 14-04-2026 (jornada y horarios en la AGE) | BOE-A-2026-8287 | 2026-04-15 | no «Última actualización» line (never modified; consolidated text present) | No | None | — |
| RD 2271/2004 (empleo público y discapacidad) | BOE-A-2004-21221 | 2004-12-17 | no «Última actualización» line (never modified; consolidated text present) | No | None | — |
| RDL 6/2023 (medidas urgentes; función pública) | BOE-A-2023-25758 | 2025-01-03 | 2025-01-03 | No | None | — |
| RD 365/1995 (situaciones administrativas) | BOE-A-1995-8730 | 2006-03-04 | 2006-03-04 | No | None | — |
| Ley 53/1984 (incompatibilidades) | BOE-A-1985-151 | 2024-06-08 | 2024-06-08 | No | None | — |
| RD 598/1985 (incompatibilidades, desarrollo) | BOE-A-1985-7820 | 1985-05-04 | no «Última actualización» line (never modified; consolidated text present) | No | None | — |
| RD 33/1986 (Reglamento de Régimen Disciplinario) | BOE-A-1986-1216 | 1991-12-31 | 1991-12-31 | No | None | — |
| RDL 4/2000 (TR Seguridad Social Funcionarios Civiles) | BOE-A-2000-12140 | 2024-12-21 | 2024-12-21 | No | None | — |
| RD 375/2003 (Reglamento General del Mutualismo Administrativo) | BOE-A-2003-7527 | 2024-12-21 | 2024-12-21 | No | None | — |
| RD 577/1997 (Estatuto de MUFACE) | BOE-A-1997-9874 | 2026-06-12 | 2026-06-12 | No | None | — |
| RDL 670/1987 (TR Clases Pasivas) | BOE-A-1987-12636 | 2025-01-29 | 2025-01-29 | No | None | — |
| ET (RDL 2/2015) | BOE-A-2015-11430 | 2026-10-03 | 2026-10-03 | No | None | — |
| IV Convenio único AGE | BOE-A-2019-7414 | 2025-04-11 | 2025-04-11 | No | None | — |
| LGSS (RDL 8/2015) | BOE-A-2015-11724 | 2026-10-03 | 2026-10-03 | No | None | — |
| LGP (Ley 47/2003) | BOE-A-2003-21614 | 2022-12-24 | 2022-12-24 | No | None | — |
| LO 2/2012 (Estabilidad Presupuestaria) | BOE-A-2012-5730 | 2025-12-03 | 2025-12-03 | No | None (RDL 13/2026, BOE-A-2026-11848, 03-06-2026, and RDL 30/2026, BOE-A-2026-21318, 14-10-2026, are «se dicta en relación» with arts. 21, 23, 25 and 32, not textual changes) | — |
| Ley 31/2022 (PGE 2023, prorrogados) | BOE-A-2022-22128 | 2026-09-30 | 2026-09-30 | No | None | — |
| LO 2/1982 (Tribunal de Cuentas) | BOE-A-1982-11584 | 2024-08-02 | 2024-08-02 | No | None | — |
| Ley 7/1988 (Funcionamiento del Tribunal de Cuentas) | BOE-A-1988-8678 | 2014-09-17 | 2014-09-17 | No | None | — |
| RD 2188/1995 (control interno IGAE) | BOE-A-1996-1578 | 2015-02-26 | 2015-02-26 | No | None | — |
| Orden de 1 de febrero de 1996 (documentos contables) | BOE-A-1996-2749 | 2024-09-17 | 2024-09-17 | No | None | — |
| Orden PRE/1576/2002 (pago de obligaciones) | BOE-A-2002-12506 | 2026-06-26 | 2026-06-26 | No | None | — |
| RD 462/2002 (indemnizaciones por razón del servicio) | BOE-A-2002-10337 | 2022-12-24 | 2022-12-24 | No | None | — |
| Orden de 30 de julio de 1992 (confección de nóminas) | BOE-A-1992-19493 | 1992-08-13 | no «Última actualización» line (never modified; consolidated text present) | No | None | — |
| RDL 14/2025 (retribuciones sector público) | BOE-A-2025-24445 | null (original 2025-12-03) | no consolidated text (análisis 404) | No | None | — |
| RD 725/1989 (anticipos de caja fija) | BOE-A-1989-14441 | 2026-10-08 | 2026-10-08 | No | None | — |
| RD 640/1987 (pagos a justificar) | BOE-A-1987-12158 | 2026-10-08 | 2026-10-08 | No | None | — |
| RD 887/2006 (Reglamento de Subvenciones) | BOE-A-2006-13371 | 2023-06-29 | 2023-06-29 | No | None | — |
| Orden de 1 de febrero de 1996 (Instrucción de operatoria contable) | BOE-A-1996-2627 | 2024-09-17 | 2024-09-17 | No | None | — |
| Ley 33/1987 (PGE 1988) | BOE-A-1987-28404 | 2013-12-26 | 2013-12-26 | No | None | — |
| Resolución de 20 de enero de 2014 (códigos de la clasificación económica) | BOE-A-2014-879 | 2014-01-29 | no «Última actualización» line (never modified; consolidated text present) | No | None | — |
| Resolución de 2 de diciembre de 2005 (dietas, anexo II RD 462/2002) | BOE-A-2005-19988 | 2005-12-03 | no consolidated text (análisis 404) | No | None | — |
| Orden HFP/793/2023 (indemnización por uso de vehículo particular) | BOE-A-2023-16462 | 2023-07-17 | no «Última actualización» line (never modified; consolidated text present) | No | None | — |
| Orden HAC/557/2026 (elaboración de los PGE para 2027) | BOE-A-2026-12037 | 2026-06-05 | no «Última actualización» line (never modified; consolidated text present) | No | None | — |
| ENS (RD 311/2022) | BOE-A-2022-7191 | 2024-11-06 | 2024-11-06 | No | None | — |
| TUE | CELEX 12016M/TXT | 2016-06-07 (DO C 202) | 2025-03-15 (EUR-Lex consolidated 02016M/TXT-20250315) | **Yes** (protocols only) | 2016/1192 (DO L 200, 26-07-2016), 2019/654 and 2019/655 (DO L 110, 25-04-2019), 2019/629 (DO L 111, 25-04-2019), 2019/1255 (DO L 196, 24-07-2019), 2024/2019 (DO L, 12-08-2024), 2025/504 (DO L, 14-03-2025) | Protocol No 3 (Statute of the CJEU) arts. 23, 49, 49 bis, 50, 50 bis, 50 ter, 51, 54, 58, 62, 62 ter, 64; Protocol No 5 (EIB Statute) arts. 4, 7, 9, 16. No article of the TUE or TFUE body |
| TFUE | CELEX 12016E/TXT | 2016-06-07 (DO C 202) | 2025-03-15 (02016E/TXT-20250315) | **Yes** (protocols only) | same as TUE (one consolidation of both treaties and their protocols) | same as TUE |
| Reglamento interno del Consejo | CELEX 32009D0937 | null; file is the original act (DO L 325, 11-12-2009) | 2026-01-01 (02009D0937-20260101) | **Yes** | 20 acts, M1–M20: 2010/594, 2010/795, 2011/900, 2013/37, 2013/345, 2013/746, 2014/692, 2014/900, 2015/2393, 2016/2353, 2017/2461, 2018/2076, 2019/2209, 2020/2030, 2021/2320, 2022/1242, 2022/2518, 2023/2827, 2024/3231, 2025/2427 (DO L, 27-11-2025) | Annex III (population figures, replaced every year; latest from 01-01-2026), art. 11.5 and new 11.6 of the annex (2014/692, from 01-11-2014), art. 12.1 first subparagraph of the annex (2022/1242, from 18-07-2022), annex I list of configurations (2010/594). Arts. 1.3 and 1.4 of the annex unchanged |
| RGPD (Reglamento (UE) 2016/679) | CELEX 32016R0679 | null; file is the original act (DO L 119, 04-05-2016) | 2016-05-04 (only consolidated version, 02016R0679-20160504) | No | None in force (corrigenda R(01)–R(03); amendment proposals 52025PC0501 and 52025PC0837 not adopted) | — |

Notes on the table. «Latest on boe.es» for the EU rows is the latest consolidated version on EUR-Lex. «No
«Última actualización» line» means boe.es shows the consolidated text of a norm never modified, so the stored
publication date stands. For the TUE/TFUE, EUR-Lex also lists M1–M4 and Croatia's Accession Treaty as modifications
of the DO C 202 text; they predate 07-06-2016 and are already in it (checked: Statute art. 48, from Regulation
2015/2422, reads the same in both files). Entry into force of the post-2016 treaty changes, as the EUR-Lex
consolidation dates: 2016/1192 from 01-09-2016; 2019/629 from 01-05-2019; 2019/654 and 2019/655 from 01-02-2020;
2019/1255 from 01-03-2020; 2024/2019 from 01-09-2024; 2025/504 from 15-03-2025.

## Citations of changed articles

### TUE/TFUE — Protocol No 3 (Statute of the CJEU) and Protocol No 5 (EIB Statute)

No lesson, glossary entry or course.yaml summary cites Protocol No 5, the EIB, or any article of Protocol No 3. The
lessons cite only the treaty body (`es/lessons/m01-l11.md` «Normativa»: TUE arts. 1–2, 4–5, 7, 13–19, 49, 50,
Protocol No 6; TFUE arts. 2–4, 6, 229, 231, 234–236, 238, 244, 247, 250, 252–254, 258–260, 263–264, 267, 288), and no
treaty article changed. Three sentences rest on the Statute without citing an article of it:

1. `es/lessons/m01-l11.md:287-291` — «El número exacto lo fija el Estatuto del Tribunal de Justicia de la Unión
   Europea (art. 254 TFUE). […] A fecha de 16-10-2026, el Tribunal General tiene 54 jueces, dos por cada Estado
   miembro». Statute art. 48, old and new: «c) dos Jueces por Estado miembro a partir del 1 de septiembre de 2019».
   Unchanged. **Fact changes: no.**
2. `es/lessons/m01-l11.md:294-297` — «El Tribunal se pronuncia sobre los recursos […] y con carácter prejudicial, a
   petición de los órganos jurisdiccionales nacionales (art. 19.3 TUE).» and `es/lessons/m01-l11.md:421-424` — «ese
   órgano está obligado a someterla al Tribunal (art. 267 TFUE).» Old Statute: no transfer of preliminary rulings. New
   Statute art. 50 ter (Regulation 2024/2019): «El Tribunal General será competente para conocer de las peticiones de
   decisión prejudicial planteadas sobre la base del artículo 267 […] que estén comprendidas exclusivamente en una o
   varias de las siguientes materias específicas: a) el sistema común del impuesto sobre el valor añadido; b) los
   impuestos especiales; c) el código aduanero; d) la clasificación arancelaria […]; e) la compensación y asistencia a
   los pasajeros […]». «El Tribunal» here is the institution (TJUE), which includes the General Court.
   **Fact changes: no.**
3. `glossary.yaml` g-cuestion-prejudicial — «Petición de un órgano jurisdiccional nacional al Tribunal de Justicia de
   la Unión Europea […] (art. 267 TFUE).» Same old/new text as item 2; «Tribunal de Justicia de la Unión Europea» is
   the institution. **Fact changes: no.** (A reader could take it as the Court of Justice alone; the definition stays
   true either way because it names the institution.)

### Reglamento interno del Consejo — arts. 11.5–11.6 and 12.1 of the annex, annex III

No place cites the changed provisions. Places citing the Rules of Procedure, all on arts. 1.3 and 1.4 of the annex:

1. `es/lessons/m01-l11.md:128-131` — «La Presidencia la ejercen grupos predeterminados de tres Estados miembros durante
   dieciocho meses. Cada miembro del grupo preside por rotación todas las formaciones, salvo la de Asuntos Exteriores,
   durante seis meses (art. 1.4 Reglamento interno del Consejo).»
2. `es/lessons/m01-l11.md:134-137` — «El Consejo tiene su sede en Bruselas. Durante los meses de abril, junio y octubre
   celebra sus sesiones en Luxemburgo (art. 1.3 …). En circunstancias excepcionales, el Consejo o el Coreper pueden
   decidir por unanimidad que una sesión se celebre en otro lugar (art. 1.3 …).»
3. `es/lessons/m01-l11.md:438` — summary bullet «El Consejo tiene su sede en Bruselas y celebra sus sesiones en
   Luxemburgo en abril, junio y octubre (art. 1.3 Reglamento interno del Consejo).»
4. `es/lessons/m01-l11.md:450` — «Reglamento interno del Consejo: arts. 1.3 y 1.4 del anexo.»

Art. 1.3, old (2009) and new (01-01-2026), identical: «El Consejo tendrá su sede en Bruselas. Durante los meses de
abril, junio y octubre, el Consejo celebrará sus sesiones en Luxemburgo. Cuando concurran circunstancias
excepcionales y por causas debidamente justificadas, el Consejo o el Comité de Representantes Permanentes […]
(Coreper) podrán decidir, por unanimidad, que una sesión del Consejo se celebre en otro lugar.» Art. 1.4, identical:
«La Presidencia del Consejo, con excepción de la formación de Asuntos Exteriores, será desempeñada por grupos
predeterminados de tres Estados miembros durante un período de dieciocho meses. […] Cada miembro del grupo ejercerá
por rotación, durante un período de seis meses, la Presidencia de todas las formaciones del Consejo, con excepción de
la formación de Asuntos Exteriores.» **Fact changes: no** (all four).

### BOE norms

No BOE norm is newer, so no BOE article citation needs checking. Two related checks:

- Ley 38/1988: the unconsolidated annex changes (RD 388/2025, 422/2025, 930/2025, 559/2026) touch annexes II–VIII and
  XIII. The lessons cite arts. 1 and 2 only (`es/lessons/m01-l04.md:236`, `:252`, `:263`, `:328`). Fact changes: no.
- LO 2/2012: RDL 13/2026 and RDL 30/2026 relate to arts. 21, 23, 25 and 32. The course cites arts. 3.2, 3.3 and 5
  (`es/lessons/m05-l01.md:40-45`, `:189`; `glossary.yaml:1629`). Fact changes: no.

## Cambios pendientes in normativa.yaml

| Norm | Modifying norm | Published | `en_vigor` | Passed on 2026-10-17? |
|---|---|---|---|---|
| Reglamento del Congreso (BOE-A-1982-5196), art. 23 | Reforma de 23-07-2026 (BOE-A-2026-16353) | 2026-07-28 | XVI legislatura (elecciones 29-11-2026, sesión constitutiva 23-12-2026, RD 806/2026) | No |
| LBRL (BOE-A-1985-5392), arts. 25.2.q), 69.1 | Ley 4/2026, DF 3 (BOE-A-2026-20528) | 2026-10-03 | 2026-10-23 | No |
| RD 366/2007 (BOE-A-2007-6239), art. 13 | RD 707/2026, DF 1 (BOE-A-2026-18509) | 2026-09-03 | 2027-01-02 | No |
| RDL 1/2013 (BOE-A-2013-12632), arts. 2, 4.2 and others | Ley 4/2026, art. primero | 2026-10-03 | 2026-10-23 | No |
| Ley 16/1985 (BOE-A-1985-12534), DA 12 | Ley 4/2026, DF 4 | 2026-10-03 | 2026-10-23 | No |
| Ley 38/2003 (BOE-A-2003-20977), art. 2.4.j) | Ley 4/2026, DF 7 | 2026-10-03 | 2026-10-23 | No |
| Ley 39/2006 (BOE-A-2006-21990), arts. 2–37 and others | Ley 4/2026, art. segundo and DA 3 | 2026-10-03 | 2026-10-23 | No |
| TREBEP (BOE-A-2015-11719), art. 49.e) | Ley 4/2026, DF 11 | 2026-10-03 | 2026-10-23 | No |
| ET (BOE-A-2015-11430), art. 37.6 | Ley 4/2026, DF 10 | 2026-10-03 | 2026-10-23 | No |
| LGSS (BOE-A-2015-11724), arts. 190.5, 363.1.d) | Ley 4/2026, DF 12 | 2026-10-03 | 2026-10-23 | No |
| RD 725/1989 (BOE-A-1989-14441), art. 6.3 | RD 813/2026, art. segundo (BOE-A-2026-20915) | 2026-10-08 | 2026-10-28 | No |
| RD 640/1987 (BOE-A-1987-12158), art. 6 | RD 813/2026, art. primero | 2026-10-08 | 2026-10-28 | No |

The first date to watch is 2026-10-23 (Ley 4/2026), six days after this check.

## «(desde …)» marks

Searched with `grep -rn "desde [0-9]"`, `«(desde la …)»`, and a multi-line regex (marks split across a line break) over
`es/lessons/`, `glossary.yaml` and `course.yaml`.

| Place | Mark | Date | Passed on 2026-10-17? |
|---|---|---|---|
| `es/lessons/m01-l03.md:236` | (art. 23.1 Reglamento del Congreso, desde la XVI legislatura) | sesión constitutiva 23-12-2026 | No |
| `es/lessons/m01-l03.md:387` | (art. 23.1 Reglamento del Congreso, desde la XVI legislatura) | 23-12-2026 | No |
| `es/lessons/m01-l10.md:178` | (art. 25.2.q LBRL) (desde 23-10-2026) | 23-10-2026 | No |
| `es/lessons/m02-l01.md:65` | (art. 4.2 RDL 1/2013, desde 23-10-2026) | 23-10-2026 | No |
| `es/lessons/m02-l01.md:129` | (art. 13.1 RD 366/2007, desde 02-01-2027) | 02-01-2027 | No |
| `es/lessons/m02-l01.md:131` | (art. 10.2.a) Reglamento aprobado por RD 707/2026, desde 02-01-2027) | 02-01-2027 | No |
| `es/lessons/m03-l07.md:140` | (art. 2.m) RDL 1/2013, desde 23-10-2026) | 23-10-2026 | No |
| `es/lessons/m03-l07.md:156` | (art. 2.2 Ley 39/2006, desde 23-10-2026) | 23-10-2026 | No |
| `es/lessons/m03-l07.md:158` | (art. 26.1 Ley 39/2006, desde 23-10-2026) | 23-10-2026 | No |
| `es/lessons/m03-l07.md:177-178` | (art. 28.1 Ley 39/2006, desde 23-10-2026) | 23-10-2026 | No |
| `es/lessons/m03-l07.md:179` | (art. 28.2 Ley 39/2006, desde 23-10-2026) | 23-10-2026 | No |
| `es/lessons/m04-l02.md:131` | (art. 4.2 RDL 1/2013, desde 23-10-2026) | 23-10-2026 | No |
| `es/lessons/m04-l04.md:78` | (art. 67.4 TREBEP): desde 2027, sesenta y siete años (DT 7.ª LGSS schedule, not a cambio pendiente) | 2027 | No |
| `es/lessons/m04-l05.md:173` | (art. 49.e) TREBEP, desde 23-10-2026) | 23-10-2026 | No |
| `es/lessons/m04-l05.md:174` | (art. 49.e) TREBEP, desde 23-10-2026) | 23-10-2026 | No |
| `es/lessons/m04-l09.md:118-119` | (art. 190.5 LGSS, desde 23-10-2026) | 23-10-2026 | No |
| `es/lessons/m05-l03.md:174` | (art. 6 RD 640/1987, desde 28-10-2026) | 28-10-2026 | No |
| `es/lessons/m05-l03.md:203` | (art. 6.3 RD 725/1989, desde 28-10-2026) | 28-10-2026 | No |
| `glossary.yaml:706` | (art. 2.k) RDL 1/2013, desde 23-10-2026) | 23-10-2026 | No |
| `glossary.yaml:1256` | (art. 2.2 Ley 39/2006, desde 23-10-2026) | 23-10-2026 | No |
| `course.yaml:491` | «y desde 2027 la jubilación exige sesenta y siete años» (DT 7.ª LGSS schedule) | 2027 | No |

Every pending change with articles cited in the lessons carries a mark: LBRL 25.2.q), RDL 1/2013 2 and 4.2, Ley
39/2006 2.2, 26.1, 28.1, 28.2, TREBEP 49.e), LGSS 190.5, RD 366/2007 13.1, RD 640/1987 6, RD 725/1989 6.3, Reglamento
del Congreso 23.1.

## Downloads

In `SP/currency/normativa/` (SP = the session scratchpad,
`/tmp/claude-1000/-home-juanjo-PycharmProjects-curset/54c91df9-3820-4de4-9f77-b056024784fa/scratchpad`):

- `CELEX-02016M-TXT-20250315_tue_2025-03-15.pdf` — EUR-Lex consolidated TUE, 15-03-2025, 435 pages. It contains the
  TUE, the TFUE, the protocols (No 3 and No 5 with the ►M markers) and the declarations, like the stored DO C 202 file.
- `CELEX-02016E-TXT-20250315_tfue_2025-03-15.pdf` — the Cellar item for the consolidated TFUE, 15-03-2025. Only
  8 pages (cover, list of amending acts and the table of equivalences): not a usable full text. The full TFUE is in the
  TUE file above.
- `CELEX-02009D0937-20260101_reglamento-interno-consejo_2026-01-01.pdf` — consolidated Rules of Procedure of the
  Council, 01-01-2026, 54 pages.
- `BOE-A-2026-21525_correccion-rd-707-2026_2026-10-16.pdf` — corrección de errores del RD 707/2026 (preamble only).

No BOE consolidated PDF was downloaded: no BOE norm is newer. The amending EU acts were not downloaded separately;
the consolidated texts mark each change. EUR-Lex HTML/PDF endpoints returned 202 (anti-bot) on direct download; the
PDFs come from the Publications Office Cellar (`publications.europa.eu/resource/consolidation/<id>.SPA.pdfa2a`).
