# Currency audit, C2 R2b part C — norms (2026-11-06)

Every BOE entry of `content/age-auxiliar-c2/sources/normativa.yaml` (78) against the «Última actualización publicada
el …» line of `https://www.boe.es/buscar/act.php?id=<ID>`, read on 2026-11-06 by `../tools/check_norms.py` (raw result:
`norms-boe.json`). EU entries against the Publications Office (Cellar) SPARQL list of consolidated versions
(`cdm:act_consolidated_date`), the same query as C1's run of 2026-11-05.

**Result.** No norm has a newer consolidation than the stored file. Five entries are texts boe.es does not consolidate
(the two CE reforms, the Resolución de 2-12-2005, Ley 29/1975, the Acuerdo de 15-07-2005): no «Última actualización»
line, unchanged. **Ley 34/2002 (LSSI):** the stored date 2025-12-18 was the open-data API's `fecha_actualizacion`
(a metadata date); act.php gives 23-01-2025 and the live consolidated PDF is byte-identical (sha256) to the stored
file: the text is current, `consolidated_as_of` corrected to 2025-01-23 (the file name keeps the old date).

**EU.** TUE and TFUE (with the Statute of the Court, protocol 3) 2025-03-15, Council Rules of Procedure 2026-01-01,
RGPD 2016-05-04 (never consolidated since): all equal to the stored versions. The Resolución de la SEFP de 7-05-2024
has no BOE consolidation (not checked).

**RDL 31/2026** (BOE-A-2026-21872): not convalidated on boe.es on 2026-11-06. Its análisis (open-data API) has no
later reference («posteriores») and no «convalidación»; a BOE title search for its convalidación finds nothing. Art.
86.2 CE: 30 working days from 21-10-2026 (plazo about 04-12-2026). C2 places resting on it: the RDL 4/2000 and LGSS
entries' `cambios_pendientes` (01-12-2026, 01-01-2027) and the m01-l14 «Cambio pendiente» Normativa note (art. 19.1
RDL 4/2000, first paragraph unchanged by the RDL). If derogated, those revert (theory ledger, open item 4).

**Pending changes and «desde» marks.** None passed on 2026-11-06. Still pending: Reglamento del Congreso (XVI
legislatura, constitutive session 23-12-2026), RDL 31/2026 (01-12-2026, 01-01-2027), RD 707/2026 (02-01-2027;
m02-l01 «desde 02-01-2027» twice and its Normativa note). The other dated phrases in lessons are facts (effects
dates of 2023 and 2026, an Access example date), not marks.

| Norm | ID | Stored | boe.es latest | Newer? |
|---|---|---|---|---|
| CE | BOE-A-1978-31229 | 2026-05-20 | 2026-05-20 | No |
| Reforma de 15 de febrero de 2024 (reforma del art. 49 CE) | BOE-A-2024-3099 | 2024-02-17 | sin línea (texto no consolidado) | No |
| LO 2/1979 (LOTC) | BOE-A-1979-23709 | 2024-08-02 | 2024-08-02 | No |
| LO 3/1981 (Defensor del Pueblo) | BOE-A-1981-10325 | 2009-11-04 | 2009-11-04 | No |
| Reglamento del Congreso | BOE-A-1982-5196 | 2026-07-28 | 2026-07-28 | No |
| Reglamento del Senado | BOE-A-1994-10830 | 2025-11-14 | 2025-11-14 | No |
| Reforma de 19 de mayo de 2026 (reforma del art. 69.3 CE) | BOE-A-2026-10881 | 2026-05-20 | sin línea (texto no consolidado) | No |
| LOPJ (LO 6/1985) | BOE-A-1985-12666 | 2025-02-17 | 2025-02-17 | No |
| Ley 38/1988 (Demarcación y Planta) | BOE-A-1988-29622 | 2025-01-03 | 2025-01-03 | No |
| LO 1/2025 (eficiencia de la Justicia) | BOE-A-2025-76 | 2025-06-04 | 2025-06-04 | No |
| Ley 50/1997 (Gobierno) | BOE-A-1997-25336 | 2025-01-03 | 2025-01-03 | No |
| Ley 19/2013 (transparencia) | BOE-A-2013-12887 | 2022-07-09 | 2022-07-09 | No |
| RD 1/2024 (Comisiones Delegadas del Gobierno) | BOE-A-2024-519 | 2026-04-01 | 2026-04-01 | No |
| RD 615/2024 (Estatuto del CTBG) | BOE-A-2024-15944 | 2026-09-18 | 2026-09-18 | No |
| Ley 40/2015 (LRJSP) | BOE-A-2015-10566 | 2024-08-02 | 2024-08-02 | No |
| Ley 2/2014 (Acción y Servicio Exterior) | BOE-A-2014-3248 | 2018-06-12 | 2018-06-12 | No |
| Ley 3/2015 (alto cargo) | BOE-A-2015-3444 | 2026-09-18 | 2026-09-18 | No |
| RD 829/2023 (departamentos ministeriales) | BOE-A-2023-23537 | 2023-12-29 | 2023-12-29 | No |
| RD 1009/2023 (estructura orgánica básica) | BOE-A-2023-24842 | 2026-07-29 | 2026-07-29 | No |
| RD 210/2024 (estructura del MTDFP) | BOE-A-2024-3796 | 2026-06-12 | 2026-06-12 | No |
| LBRL (Ley 7/1985) | BOE-A-1985-5392 | 2026-10-03 | 2026-10-03 | No |
| Ley 39/2015 (LPAC) | BOE-A-2015-10565 | 2024-11-06 | 2024-11-06 | No |
| LJCA (Ley 29/1998) | BOE-A-1998-16718 | 2025-01-03 | 2025-01-03 | No |
| LO 3/1980 (Consejo de Estado) | BOE-A-1980-8648 | 2024-08-02 | 2024-08-02 | No |
| LOPDGDD (LO 3/2018) | BOE-A-2018-16673 | 2025-12-27 | 2025-12-27 | No |
| TREBEP (RDL 5/2015) | BOE-A-2015-11719 | 2026-10-03 | 2026-10-03 | No |
| Ley 30/1984 (reforma de la Función Pública) | BOE-A-1984-17387 | 2015-10-31 | 2015-10-31 | No |
| RD 1405/1986 (Registro Central de Personal) | BOE-A-1986-18101 | 2000-01-18 | 2000-01-18 | No |
| RD 2073/1999 (Reglamento del Registro Central de Personal) | BOE-A-2000-1007 | 2000-01-18 | 2000-01-18 | No |
| RD 364/1995 (Reglamento General de Ingreso y Provisión) | BOE-A-1995-8729 | 2006-03-04 | 2006-03-04 | No |
| RD 365/1995 (situaciones administrativas) | BOE-A-1995-8730 | 2006-03-04 | 2006-03-04 | No |
| RD 2271/2004 (empleo público y discapacidad) | BOE-A-2004-21221 | 2004-12-17 | 2004-12-17 | No |
| RDL 6/2023 (medidas urgentes; función pública) | BOE-A-2023-25758 | 2025-01-03 | 2025-01-03 | No |
| Orden TDF/379/2024 (directivos públicos profesionales) | BOE-A-2024-8609 | 2024-04-30 | 2024-04-30 | No |
| RD 33/1986 (Reglamento de Régimen Disciplinario) | BOE-A-1986-1216 | 1991-12-31 | 1991-12-31 | No |
| Resolución de 14-04-2026 (jornada y horarios en la AGE) | BOE-A-2026-8287 | 2026-04-15 | 2026-04-15 | No |
| RD 462/2002 (indemnizaciones por razón del servicio) | BOE-A-2002-10337 | 2022-12-24 | 2022-12-24 | No |
| Resolución de 2 de diciembre de 2005 (dietas, anexo II RD 462/2002) | BOE-A-2005-19988 | 2005-12-03 | sin línea (texto no consolidado) | No |
| Orden HFP/793/2023 (indemnización por uso de vehículo particular) | BOE-A-2023-16462 | 2023-07-17 | 2023-07-17 | No |
| RDL 14/2025 (retribuciones sector público) | BOE-A-2025-24445 | None | sin línea (texto no consolidado) | No |
| Ley 29/1975 (Seguridad Social de los Funcionarios Civiles del Estado) | BOE-A-1975-13887 | 1975-06-30 | sin línea (texto no consolidado) | No |
| RDL 4/2000 (TR Seguridad Social Funcionarios Civiles) | BOE-A-2000-12140 | 2026-10-21 | 2026-10-21 | No |
| RD 375/2003 (Reglamento General del Mutualismo Administrativo) | BOE-A-2003-7527 | 2024-12-21 | 2024-12-21 | No |
| RD 577/1997 (Estatuto de MUFACE) | BOE-A-1997-9874 | 2026-06-12 | 2026-06-12 | No |
| RDL 670/1987 (TR Clases Pasivas) | BOE-A-1987-12636 | 2026-10-21 | 2026-10-21 | No |
| LGSS (RDL 8/2015) | BOE-A-2015-11724 | 2026-10-21 | 2026-10-21 | No |
| Ley 31/2022 (PGE 2023, prorrogados) | BOE-A-2022-22128 | 2026-09-30 | 2026-09-30 | No |
| LGP (Ley 47/2003) | BOE-A-2003-21614 | 2022-12-24 | 2022-12-24 | No |
| LO 2/2012 (Estabilidad Presupuestaria) | BOE-A-2012-5730 | 2025-12-03 | 2025-12-03 | No |
| Orden HAC/557/2026 (elaboración de los PGE para 2027) | BOE-A-2026-12037 | 2026-06-05 | 2026-06-05 | No |
| Resolución de 20 de enero de 2014 (códigos de la clasificación económica) | BOE-A-2014-879 | 2014-01-29 | 2014-01-29 | No |
| LO 3/2007 (igualdad) | BOE-A-2007-6115 | 2024-08-02 | 2024-08-02 | No |
| LO 1/2004 (violencia de género) | BOE-A-2004-21760 | 2022-09-07 | 2022-09-07 | No |
| Ley 4/2023 (trans y LGTBI) | BOE-A-2023-5366 | 2023-03-01 | 2023-03-01 | No |
| Ley 15/2022 (igualdad de trato) | BOE-A-2022-11589 | 2022-07-13 | 2022-07-13 | No |
| RDL 1/2013 (TR derechos personas con discapacidad) | BOE-A-2013-12632 | 2026-10-03 | 2026-10-03 | No |
| Ley 39/2006 (dependencia) | BOE-A-2006-21990 | 2026-10-03 | 2026-10-03 | No |
| Ley 4/2026 (discapacidad y dependencia) | BOE-A-2026-20528 | 2026-10-03 | 2026-10-03 | No |
| RD 208/1996 (información administrativa) | BOE-A-1996-4997 | 2011-06-04 | 2011-06-04 | No |
| RD 366/2007 (accesibilidad ante la AGE) | BOE-A-2007-6239 | 2026-09-03 | 2026-09-03 | No |
| RD 707/2026 (accesibilidad cognitiva) | BOE-A-2026-18509 | 2026-09-03 | 2026-09-03 | No |
| RD 951/2005 (calidad; quejas y sugerencias) | BOE-A-2005-14836 | 2009-06-30 | 2009-06-30 | No |
| LO 4/2001 (derecho de petición) | BOE-A-2001-21090 | 2011-07-28 | 2011-07-28 | No |
| RD 776/2011 (supresión de órganos colegiados) | BOE-A-2011-9736 | 2011-06-04 | 2011-06-04 | No |
| RD 1708/2011 (Sistema Español de Archivos) | BOE-A-2011-18541 | 2024-03-27 | 2024-03-27 | No |
| Ley 16/1985 (Patrimonio Histórico) | BOE-A-1985-12534 | 2026-10-03 | 2026-10-03 | No |
| Decreto 914/1969 (Archivo General de la Administración Civil) | BOE-A-1969-643 | 1969-05-26 | 1969-05-26 | No |
| RD 1401/2007 (Comisión Superior Calificadora de Documentos Administrativos) | BOE-A-2007-19248 | 2017-05-23 | 2017-05-23 | No |
| RD 1164/2002 (eliminación de documentos) | BOE-A-2002-22192 | 2007-11-07 | 2007-11-07 | No |
| RD 203/2021 (Reglamento de actuación por medios electrónicos) | BOE-A-2021-5032 | 2025-04-02 | 2025-04-02 | No |
| Orden PCM/1382/2021 (REG-AGE) | BOE-A-2021-20477 | 2021-12-11 | 2021-12-11 | No |
| Orden HAP/1949/2014 (PAG) | BOE-A-2014-10908 | 2015-11-26 | 2015-11-26 | No |
| RD 127/2015 (ventanilla única empresarial) | BOE-A-2015-2671 | 2015-03-13 | 2015-03-13 | No |
| Acuerdo del Consejo de Ministros de 15-07-2005 (Red de Oficinas Integradas) | BOE-A-2005-13337 | 2005-08-03 | sin línea (texto no consolidado) | No |
| Ley 14/2013 (apoyo a los emprendedores) | BOE-A-2013-10074 | 2025-04-09 | 2025-04-09 | No |
| Ley 34/2002 (LSSI) | BOE-A-2002-13758 | 2025-12-18 | 2025-01-23 | No; fecha guardada corregida (era la de los metadatos) |
| RD 1112/2018 (accesibilidad web) | BOE-A-2018-12699 | 2019-08-12 | 2019-08-12 | No |
| ENS (RD 311/2022) | BOE-A-2022-7191 | 2024-11-06 | 2024-11-06 | No |
