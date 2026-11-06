# Currency audit 2026-11 — norms (step 1)

2026-11-05. Every entry of `content/age-administrativo-c1/sources/normativa.yaml` (98) checked: BOE entries against
the «Última actualización publicada el …» line of `https://www.boe.es/buscar/act.php?id=<ID>` and the modifying norms
in the open-data `…/legislacion-consolidada/id/<ID>/analisis`; EU entries against the Publications Office (Cellar)
SPARQL list of consolidated versions (`cdm:act_consolidated_date`). Entries without a consolidated text redirect to
`doc.php` (no «Última actualización» line): still unconsolidated, as in October.

**Result.** Four BOE norms have a newer consolidation, all from one modifying norm, **Real Decreto-ley 31/2026, de 20
de octubre** (BOE-A-2026-21872), «de mejora de la acción protectora de la Seguridad Social»: LGSS, RDL 4/2000, TRLCPE
and ET. Every other entry is at its latest version. RDL 31/2026 is not convalidated on boe.es on 2026-11-05 (no
«convalidación» reference in its análisis); art. 86.2 CE gives the Congreso 30 working days from 21-10-2026. The
Ley 4/2026 changes (in force 23-10-2026) and the RD 813/2026 changes (28-10-2026) were already in the stored files
(October's cambios_pendientes): not newer, their marks are dropped (step 2).

Saved (old files stay), sha256 identical to the copies C2's R0a downloaded the same day:
`BOE-A-2015-11724_lgss_2026-10-21.pdf`, `BOE-A-2000-12140_trlssfce_2026-10-21.pdf`,
`BOE-A-1987-12636_trlcpe_2026-10-21.pdf`, `BOE-A-2015-11430_et_2026-10-21.pdf` (C2 lacks this one) and the modifying
norm `BOE-A-2026-21872_rdl-31-2026_2026-10-21.pdf`. In the new consolidated texts, precepts with a future effect
(LGSS 144.4, 169.1.a), 171, 172, 173.1 and 309.1; RDL 4/2000 19.1) print the future wording with «Téngase en cuenta…»
and the «Redacción anterior»; LGSS 190–192 and ET 37.6 are integrated without notice.

| Norm | ID | Stored date | Latest | Newer? | Modifying norm | Precepts changed (effect) |
|---|---|---|---|---|---|---|
| CE | BOE-A-1978-31229 | 2026-05-20 | 2026-05-20 | No | — | — |
| LO 2/1979 (LOTC) | BOE-A-1979-23709 | 2024-08-02 | 2024-08-02 | No | — | — |
| LO 3/1981 (Defensor del Pueblo) | BOE-A-1981-10325 | 2009-11-04 | 2009-11-04 | No | — | — |
| Reglamento del Congreso | BOE-A-1982-5196 | 2026-07-28 | 2026-07-28 | No | — | — |
| Reglamento del Senado | BOE-A-1994-10830 | 2025-11-14 | 2025-11-14 | No | — | — |
| LOPJ (LO 6/1985) | BOE-A-1985-12666 | 2025-02-17 | 2025-02-17 | No | — | — |
| Ley 38/1988 (Demarcación y Planta) | BOE-A-1988-29622 | 2025-01-03 | 2025-01-03 | No | — | — |
| LO 1/2025 (eficiencia de la Justicia) | BOE-A-2025-76 | 2025-06-04 | 2025-06-04 | No | — | — |
| Ley 50/1997 (Gobierno) | BOE-A-1997-25336 | 2025-01-03 | 2025-01-03 | No | — | — |
| Ley 19/2013 (transparencia) | BOE-A-2013-12887 | 2022-07-09 | 2022-07-09 | No | — | — |
| RD 615/2024 (Estatuto del CTBG) | BOE-A-2024-15944 | 2026-09-18 | 2026-09-18 | No | — | — |
| Ley 40/2015 (LRJSP) | BOE-A-2015-10566 | 2024-08-02 | 2024-08-02 | No | — | — |
| Ley 2/2014 (Acción y Servicio Exterior) | BOE-A-2014-3248 | 2018-06-12 | 2018-06-12 | No | — | — |
| Ley 3/2015 (alto cargo) | BOE-A-2015-3444 | 2026-09-18 | 2026-09-18 | No | — | — |
| RD 829/2023 (departamentos ministeriales) | BOE-A-2023-23537 | 2023-12-29 | 2023-12-29 | No | — | — |
| RD 1009/2023 (estructura orgánica básica) | BOE-A-2023-24842 | 2026-07-29 | 2026-07-29 | No | — | — |
| LBRL (Ley 7/1985) | BOE-A-1985-5392 | 2026-10-03 | 2026-10-03 | No | — | — |
| TUE | CELEX 12016M/TXT | 2025-03-15 | 2025-03-15 (Cellar) | No | — | — |
| TFUE | CELEX 12016E/TXT | 2025-03-15 | 2025-03-15 (Cellar) | No | — | — |
| Reglamento interno del Consejo | CELEX 32009D0937 | 2026-01-01 | 2026-01-01 (Cellar) | No | — | — |
| RD 208/1996 (información administrativa) | BOE-A-1996-4997 | 2011-06-04 | 2011-06-04 | No | — | — |
| RD 951/2005 (calidad; quejas y sugerencias) | BOE-A-2005-14836 | 2009-06-30 | 2009-06-30 | No | — | — |
| RD 366/2007 (accesibilidad ante la AGE) | BOE-A-2007-6239 | 2026-09-03 | 2026-09-03 | No | — | — |
| LO 4/2001 (derecho de petición) | BOE-A-2001-21090 | 2011-07-28 | 2011-07-28 | No | — | — |
| RDL 1/2013 (TR derechos personas con discapacidad) | BOE-A-2013-12632 | 2026-10-03 | 2026-10-03 | No | — | — |
| RD 1708/2011 (Sistema Español de Archivos) | BOE-A-2011-18541 | 2024-03-27 | 2024-03-27 | No | — | — |
| Ley 16/1985 (Patrimonio Histórico) | BOE-A-1985-12534 | 2026-10-03 | 2026-10-03 | No | — | — |
| Ley 39/2015 (LPAC) | BOE-A-2015-10565 | 2024-11-06 | 2024-11-06 | No | — | — |
| RD 203/2021 (Reglamento de actuación por medios electrónicos) | BOE-A-2021-5032 | 2025-04-02 | 2025-04-02 | No | — | — |
| Orden HAP/1949/2014 (PAG) | BOE-A-2014-10908 | 2015-11-26 | 2015-11-26 | No | — | — |
| RD 127/2015 (ventanilla única empresarial) | BOE-A-2015-2671 | 2015-03-13 | never amended (no «Última actualización» line) | No | — | — |
| RD 1112/2018 (accesibilidad web) | BOE-A-2018-12699 | 2019-08-12 | 2019-08-12 | No | — | — |
| RD 776/2011 (supresión de órganos colegiados) | BOE-A-2011-9736 | 2011-06-04 | never amended (no «Última actualización» line) | No | — | — |
| Decreto 914/1969 (Archivo General de la Administración Civil) | BOE-A-1969-643 | 1969-05-26 | never amended (no «Última actualización» line) | No | — | — |
| RD 1401/2007 (Comisión Superior Calificadora de Documentos Administrativos) | BOE-A-2007-19248 | 2017-05-23 | 2017-05-23 | No | — | — |
| RD 1164/2002 (eliminación de documentos) | BOE-A-2002-22192 | 2007-11-07 | 2007-11-07 | No | — | — |
| Acuerdo del Consejo de Ministros de 15-07-2005 (Red de Oficinas Integradas) | BOE-A-2005-13337 | 2005-08-03 | no consolidated text (doc.php) | No | — | — |
| Ley 14/2013 (apoyo a los emprendedores) | BOE-A-2013-10074 | 2025-04-09 | 2025-04-09 | No | — | — |
| RGPD (Reglamento (UE) 2016/679) | CELEX 32016R0679 | None | 2016-05-04 (Cellar) | No | — | — |
| LOPDGDD (LO 3/2018) | BOE-A-2018-16673 | 2025-12-27 | 2025-12-27 | No | — | — |
| Código Civil | BOE-A-1889-4763 | 2025-01-03 | 2025-01-03 | No | — | — |
| LJCA (Ley 29/1998) | BOE-A-1998-16718 | 2025-01-03 | 2025-01-03 | No | — | — |
| LCSP (Ley 9/2017) | BOE-A-2017-12902 | 2026-04-09 | 2026-04-09 | No | — | — |
| Orden HAC/1517/2025 (umbrales de contratación) | BOE-A-2025-26605 | 2025-12-26 | no consolidated text (doc.php) | No | — | — |
| Ley 60/2003 (Arbitraje) | BOE-A-2003-23646 | 2015-10-06 | 2015-10-06 | No | — | — |
| Ley 38/2003 (General de Subvenciones) | BOE-A-2003-20977 | 2026-10-03 | 2026-10-03 | No | — | — |
| LO 3/1980 (Consejo de Estado) | BOE-A-1980-8648 | 2024-08-02 | 2024-08-02 | No | — | — |
| LO 3/2007 (igualdad) | BOE-A-2007-6115 | 2024-08-02 | 2024-08-02 | No | — | — |
| LO 1/2004 (violencia de género) | BOE-A-2004-21760 | 2022-09-07 | 2022-09-07 | No | — | — |
| Ley 4/2023 (trans y LGTBI) | BOE-A-2023-5366 | 2023-03-01 | never amended (no «Última actualización» line) | No | — | — |
| Ley 15/2022 (igualdad de trato) | BOE-A-2022-11589 | 2022-07-13 | never amended (no «Última actualización» line) | No | — | — |
| Ley 39/2006 (dependencia) | BOE-A-2006-21990 | 2026-10-03 | 2026-10-03 | No | — | — |
| RD 803/2022 (Estatuto del INE) | BOE-A-2022-16198 | 2025-10-31 | 2025-10-31 | No | — | — |
| TREBEP (RDL 5/2015) | BOE-A-2015-11719 | 2026-10-03 | 2026-10-03 | No | — | — |
| Ley 30/1984 (reforma de la Función Pública) | BOE-A-1984-17387 | 2015-10-31 | 2015-10-31 | No | — | — |
| RD 1405/1986 (Registro Central de Personal) | BOE-A-1986-18101 | 2000-01-18 | 2000-01-18 | No | — | — |
| RD 2073/1999 (Reglamento del Registro Central de Personal) | BOE-A-2000-1007 | 2000-01-18 | never amended (no «Última actualización» line) | No | — | — |
| RD 364/1995 (Reglamento General de Ingreso y Provisión) | BOE-A-1995-8729 | 2006-03-04 | 2006-03-04 | No | — | — |
| Resolución de 14-04-2026 (jornada y horarios en la AGE) | BOE-A-2026-8287 | 2026-04-15 | never amended (no «Última actualización» line) | No | — | — |
| RD 2271/2004 (empleo público y discapacidad) | BOE-A-2004-21221 | 2004-12-17 | never amended (no «Última actualización» line) | No | — | — |
| RDL 6/2023 (medidas urgentes; función pública) | BOE-A-2023-25758 | 2025-01-03 | 2025-01-03 | No | — | — |
| RD 365/1995 (situaciones administrativas) | BOE-A-1995-8730 | 2006-03-04 | 2006-03-04 | No | — | — |
| Ley 53/1984 (incompatibilidades) | BOE-A-1985-151 | 2024-06-08 | 2024-06-08 | No | — | — |
| RD 598/1985 (incompatibilidades, desarrollo) | BOE-A-1985-7820 | 1985-05-04 | never amended (no «Última actualización» line) | No | — | — |
| RD 33/1986 (Reglamento de Régimen Disciplinario) | BOE-A-1986-1216 | 1991-12-31 | 1991-12-31 | No | — | — |
| Ley 29/1975 (Seguridad Social de los Funcionarios Civiles del Estado) | BOE-A-1975-13887 | 1975-06-30 | no consolidated text (doc.php) | No | — | — |
| RDL 4/2000 (TR Seguridad Social Funcionarios Civiles) | BOE-A-2000-12140 | 2024-12-21 | 2026-10-21 | **Yes** | RDL 31/2026 | 19.1 (01-12-2026) |
| RD 375/2003 (Reglamento General del Mutualismo Administrativo) | BOE-A-2003-7527 | 2024-12-21 | 2024-12-21 | No | — | — |
| RD 577/1997 (Estatuto de MUFACE) | BOE-A-1997-9874 | 2026-06-12 | 2026-06-12 | No | — | — |
| RDL 670/1987 (TR Clases Pasivas) | BOE-A-1987-12636 | 2025-01-29 | 2026-10-21 | **Yes** | RDL 31/2026 | 27.2 (01-11-2026); 38.4, 41.1, 41.5, 42.9, 42.10 suprimido, DT 16.ª nueva, DA 20.ª suprimida (21-10-2026) |
| ET (RDL 2/2015) | BOE-A-2015-11430 | 2026-10-03 | 2026-10-21 | **Yes** | RDL 31/2026 | 37.6 (23-10-2026) |
| IV Convenio único AGE | BOE-A-2019-7414 | 2025-04-11 | 2025-04-11 | No | — | — |
| LGSS (RDL 8/2015) | BOE-A-2015-11724 | 2026-10-03 | 2026-10-21 | **Yes** | RDL 31/2026 (BOE-A-2026-21872, 21-10-2026) | 61.2 (01-11-2026); 144.4, 169.1.a), 171, 172, 173.1 (01-12-2026); 190.1–3, 191.2, 191.5 nuevo, 192.1–2 (23-10-2026); 309.1 (01-01-2027); 221.2, 224.1–2, 318.h) nuevo, DA 1.ª.1–2, DT 13.ª.2–3, DA 64.ª y DT 48.ª nuevas, DA 40.ª suprimida (21-10-2026) |
| LGP (Ley 47/2003) | BOE-A-2003-21614 | 2022-12-24 | 2022-12-24 | No | — | — |
| LO 2/2012 (Estabilidad Presupuestaria) | BOE-A-2012-5730 | 2025-12-03 | 2025-12-03 | No | — | — |
| Ley 31/2022 (PGE 2023, prorrogados) | BOE-A-2022-22128 | 2026-09-30 | 2026-09-30 | No | — | — |
| LO 2/1982 (Tribunal de Cuentas) | BOE-A-1982-11584 | 2024-08-02 | 2024-08-02 | No | — | — |
| Ley 7/1988 (Funcionamiento del Tribunal de Cuentas) | BOE-A-1988-8678 | 2014-09-17 | 2014-09-17 | No | — | — |
| RD 2188/1995 (control interno IGAE) | BOE-A-1996-1578 | 2015-02-26 | 2015-02-26 | No | — | — |
| Orden de 1 de febrero de 1996 (documentos contables) | BOE-A-1996-2749 | 2024-09-17 | 2024-09-17 | No | — | — |
| Orden PRE/1576/2002 (pago de obligaciones) | BOE-A-2002-12506 | 2026-06-26 | 2026-06-26 | No | — | — |
| RD 462/2002 (indemnizaciones por razón del servicio) | BOE-A-2002-10337 | 2022-12-24 | 2022-12-24 | No | — | — |
| Orden de 30 de julio de 1992 (confección de nóminas) | BOE-A-1992-19493 | 1992-08-13 | never amended (no «Última actualización» line) | No | — | — |
| RDL 14/2025 (retribuciones sector público) | BOE-A-2025-24445 | None | no consolidated text (doc.php) | No | — | — |
| RD 725/1989 (anticipos de caja fija) | BOE-A-1989-14441 | 2026-10-08 | 2026-10-08 | No | — | — |
| RD 640/1987 (pagos a justificar) | BOE-A-1987-12158 | 2026-10-08 | 2026-10-08 | No | — | — |
| RD 887/2006 (Reglamento de Subvenciones) | BOE-A-2006-13371 | 2023-06-29 | 2023-06-29 | No | — | — |
| Orden de 1 de febrero de 1996 (Instrucción de operatoria contable) | BOE-A-1996-2627 | 2024-09-17 | 2024-09-17 | No | — | — |
| Ley 33/1987 (PGE 1988) | BOE-A-1987-28404 | 2013-12-26 | 2013-12-26 | No | — | — |
| Resolución de 20 de enero de 2014 (códigos de la clasificación económica) | BOE-A-2014-879 | 2014-01-29 | never amended (no «Última actualización» line) | No | — | — |
| Resolución de 2 de diciembre de 2005 (dietas, anexo II RD 462/2002) | BOE-A-2005-19988 | 2005-12-03 | no consolidated text (doc.php) | No | — | — |
| Orden HFP/793/2023 (indemnización por uso de vehículo particular) | BOE-A-2023-16462 | 2023-07-17 | never amended (no «Última actualización» line) | No | — | — |
| Orden HAC/557/2026 (elaboración de los PGE para 2027) | BOE-A-2026-12037 | 2026-06-05 | never amended (no «Última actualización» line) | No | — | — |
| ENS (RD 311/2022) | BOE-A-2022-7191 | 2024-11-06 | 2024-11-06 | No | — | — |
| Reforma de 19 de mayo de 2026 (reforma del art. 69.3 CE) | BOE-A-2026-10881 | 2026-05-20 | no consolidated text (doc.php) | No | — | — |
| Estatuto del Tribunal de Justicia de la Unión Europea | CELEX 12016E/PRO/03 | 2025-03-15 | 2025-03-15 (Cellar) | No | — | — |
| RD 707/2026 (accesibilidad cognitiva) | BOE-A-2026-18509 | 2026-09-03 | never amended (no «Última actualización» line) | No | — | — |
| Ley 4/2026 (discapacidad y dependencia) | BOE-A-2026-20528 | 2026-10-03 | never amended (no «Última actualización» line) | No | — | — |
