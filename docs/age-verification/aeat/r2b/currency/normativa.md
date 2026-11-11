# Currency audit, AEAT R2b part C — norms and annual figures (2026-11-11)

Every BOE entry of `content/aeat-agentes-hacienda/sources/normativa.yaml` as it stood before this round (96) against the
«Última actualización publicada el …» line of `https://www.boe.es/buscar/act.php?id=<ID>`, read on 2026-11-11 by
`../tools/check_norms.py` (raw: `norms-boe.json`). EU entries against the Publications Office SPARQL list of consolidated
versions (`../tools/eu_versions.py`, `cdm:act_consolidated_date`).

**Result.** No norm has a newer consolidation than the stored file. Four entries have no «Última actualización» line,
as stored: the two CE reforms, Ley 29/1975 and Orden HAC/266/2024 (never consolidated; diario PDF).

**EU.** TUE and TFUE (with Protocols 3 and 6) 2025-03-15; Reglamento interno del Consejo 2026-01-01; CAU 2022-12-12;
Reglamento Delegado 2015/2446 2026-11-01; Reglamento de Ejecución 2015/2447 2026-07-01: all equal to the stored versions.
**RGPD:** the SPARQL lists a consolidated version of 25-05-2018 (the 2018 corrigendum applied); the stored file is the
DO original and its `version_vigente` note says the text in force is the original with the corrigenda of 2018 and 2021,
«guardadas en sources/otros/» — a note copied from C2 that named files this course did not hold. The m01-l05 sentence of
art. 9.1 follows the corrected wording («la orientación sexual»). The two corrigenda were copied from C1 with the same
sha256 (`doue-rgpd-correccion-2018.pdf`, `doue-rgpd-correccion-2021.pdf`, `fuentes.yaml` entries), so the note is now
true; no lesson sentence changed.

**Norms named only inside another norm (13 «nombrado/citado en…» lines naming a norm normativa.yaml lacked).** The tax
handoff counted 12; the citations golden lists 13 (six in m01-l07, one in m03-l05, six in m03-l17; the thirteenth is the
derogated Ley 30/1992, also entered so every name has a snapshot). Entered with `short` equal to the «Normativa» line
(m03-l05's line changed to start with the new short, decision 16 of the tax part) and snapshots:

| Norm | ID | Consolidated | Origin | Note |
|---|---|---|---|---|
| Ley 22/1993 | BOE-A-1993-31153 | 2014-10-01 | descarga nueva | DA 5.ª (art. 61.1 RD 364/1995) |
| Ley 29/2011 | BOE-A-2011-15039 | 2026-10-21 | descarga nueva | art. 5 (arts. 49.f) y 89.6 TREBEP) |
| Ley 7/1988 | BOE-A-1988-8678 | 2014-09-17 | copia de C1, mismo sha256 | art. 93.3 (art. 87.1.d) TREBEP) |
| Ley 30/1992 | BOE-A-1992-26318 | 2015-10-02 | descarga nueva | derogada; último texto consolidado |
| Código Penal (LO 10/1995) | BOE-A-1995-25444 | 2026-04-09 | descarga nueva | libro II, títulos II y VII |
| Estatuto de los Trabajadores | BOE-A-2015-11430 | 2026-10-21 | copia de C1, mismo sha256 | RDL 31/2026 sin convalidar; no toca lo citado |
| Ley 25/2003 | BOE-A-2003-14188 | 2003-07-16 | descarga nueva (diario PDF; no consolidada) | art. 51 |
| Ley 9/2012 | BOE-A-2012-14062 | 2022-01-19 | descarga nueva | derogada salvo, entre otras, la DA 10.ª, que es la citada |
| Ley 49/2002 | BOE-A-2002-25039 | 2023-12-20 | descarga nueva | título II |
| Ley 27/1984 | BOE-A-1984-17004 | 1996-06-08 | descarga nueva | art. 22 («Artículo veintidós») |
| LO 8/2007 | BOE-A-2007-13022 | 2024-05-30 | descarga nueva | sin precepto citado |
| Ley 34/1998 | BOE-A-1998-23284 | 2026-09-30 | descarga nueva | sin precepto citado |
| Ley 19/1994 | BOE-A-1994-15794 | 2025-07-29 | descarga nueva | art. 43 |

Each cited precept was found in its file (`pdftotext`).

**RDL 29/2026** (BOE-A-2026-20823): neither convalidated nor derogated on boe.es on 2026-11-11. BOE sumarios of
07-10 to 11-11-2026 (`r0a/scripts/norm/sumarios.py`): the only convalidation acuerdos published are those of RDL 24/2026
and 25/2026 (BOE 20-10-2026); the open-data análisis of the RDL lists one later reference, «SE DICTA EN RELACIÓN» (RDL
28/2026, prórroga de arrendamientos), not a convalidation. Deadline 19-11-2026 (count in `r1/rdl-29-2026-revert-list.md`)
not reached: the revert list is **not** applied; re-check the BOE from 18-11-2026 (with the Cortes dissolved, the
Diputación Permanente votes). RDL 31/2026: not convalidated (plazo about 04-12-2026). RDL 33, 35 and 36/2026 (BOE
11-11-2026): in force 12-11-2026; their marks stay as R0a set them.

**«(desde …)» marks.** No mark announces a future wording whose date has passed. Dated phrases with a past date are
facts («vigente desde el 01-01-2025», m03-l15; «en vigor desde el 23-10-2026», m01-l06) or the «Cambio pendiente por el
Real Decreto-ley 29/2026, … sin convalidar, con efectos desde el 01-01-2026 / 08-10-2026» notes in the «Normativa» of
m03-l15 and m03-l16, where what is pending is the convalidación, not the date (tax part, decisions 17 and 22). Future
marks: 01-12-2026 (m03-l04; RDL 31/2026 and RDL 29/2026 effects) and 01-01-2027 (m03-l15, three).

**Annual figures (R3.5), re-checked for 2026.** Every `cifras_anuales` value was found in the stored text of the norm
that sets it (`pdftotext`; the PGE 2023 file is boe.es HTML): interés legal 3,25 % and interés de demora 4,0625 % (DA 42.ª
Ley 31/2022), IPREM 20 / 600 / 7.200 / 8.400 euros (DA 90.ª), límite exento de garantías 50.000 euros (art. 2 Orden
HFP/311/2023), LIRPF and LIVA módulos limits, DA 55.ª LIRPF 1,1 % (RDL 29/2026), RDL 7/2026 deductions, TRLRHL art.
107.4 coefficients, Orden HAC/1425/2025 (2026) and HAC/1161/2026 (2027) figures. No Ley de Presupuestos for 2026 exists
(BOE API: only Orden HAC/974/2025, the elaboration order); the análisis of Ley 31/2022 lists no 2024–2026 change to DA
42.ª or 90.ª (the 2026 prórroga of RDL 16/2025, «sin efecto», and RDL 3/2026, convalidated, concern títulos IV and
VIII). The norms setting them are at their latest consolidation (table below). Status unchanged: «fuente legal; no
contrastado con la sede de la AEAT».

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
| Ley 40/2015 (LRJSP) | BOE-A-2015-10566 | 2024-08-02 | 2024-08-02 | No |
| RD 829/2023 (departamentos ministeriales) | BOE-A-2023-23537 | 2023-12-29 | 2023-12-29 | No |
| RD 1009/2023 (estructura orgánica básica) | BOE-A-2023-24842 | 2026-07-29 | 2026-07-29 | No |
| LBRL (Ley 7/1985) | BOE-A-1985-5392 | 2026-10-03 | 2026-10-03 | No |
| LO 1/1995 (Estatuto de Autonomía de Ceuta) | BOE-A-1995-6358 | 1995-03-14 | 1995-03-14 | No |
| LO 2/1995 (Estatuto de Autonomía de Melilla) | BOE-A-1995-6359 | 1995-03-14 | 1995-03-14 | No |
| Ley 39/2015 (LPAC) | BOE-A-2015-10565 | 2024-11-06 | 2024-11-06 | No |
| RD 203/2021 (Reglamento de actuación por medios electrónicos) | BOE-A-2021-5032 | 2025-04-02 | 2025-04-02 | No |
| Orden PCM/1382/2021 (REG-AGE) | BOE-A-2021-20477 | 2021-12-11 | 2021-12-11 | No |
| Ley 19/2013 (transparencia) | BOE-A-2013-12887 | 2022-07-09 | 2022-07-09 | No |
| RD 615/2024 (Estatuto del CTBG) | BOE-A-2024-15944 | 2026-09-18 | 2026-09-18 | No |
| LOPDGDD (LO 3/2018) | BOE-A-2018-16673 | 2025-12-27 | 2025-12-27 | No |
| LO 3/2007 (igualdad) | BOE-A-2007-6115 | 2024-08-02 | 2024-08-02 | No |
| LO 1/2004 (violencia de género) | BOE-A-2004-21760 | 2022-09-07 | 2022-09-07 | No |
| Ley 15/2022 (igualdad de trato) | BOE-A-2022-11589 | 2022-07-13 | 2022-07-13 | No |
| Ley 4/2023 (trans y LGTBI) | BOE-A-2023-5366 | 2023-03-01 | 2023-03-01 | No |
| RDL 1/2013 (TR derechos personas con discapacidad) | BOE-A-2013-12632 | 2026-10-03 | 2026-10-03 | No |
| Ley 39/2006 (dependencia) | BOE-A-2006-21990 | 2026-11-11 | 2026-11-11 | No |
| Ley 4/2026 (discapacidad y dependencia) | BOE-A-2026-20528 | 2026-10-03 | 2026-10-03 | No |
| TREBEP (RDL 5/2015) | BOE-A-2015-11719 | 2026-10-03 | 2026-10-03 | No |
| Ley 30/1984 (reforma de la Función Pública) | BOE-A-1984-17387 | 2015-10-31 | 2015-10-31 | No |
| RD 364/1995 (Reglamento General de Ingreso y Provisión) | BOE-A-1995-8729 | 2006-03-04 | 2006-03-04 | No |
| RD 365/1995 (situaciones administrativas) | BOE-A-1995-8730 | 2006-03-04 | 2006-03-04 | No |
| Ley 53/1984 (incompatibilidades) | BOE-A-1985-151 | 2024-06-08 | 2024-06-08 | No |
| RD 598/1985 (incompatibilidades, desarrollo) | BOE-A-1985-7820 | 1985-05-04 | 1985-05-04 | No |
| RD 33/1986 (Reglamento de Régimen Disciplinario) | BOE-A-1986-1216 | 1991-12-31 | 1991-12-31 | No |
| RDL 6/2023 (medidas urgentes; función pública) | BOE-A-2023-25758 | 2025-01-03 | 2025-01-03 | No |
| Ley 29/1975 (Seguridad Social de los Funcionarios Civiles del Estado) | BOE-A-1975-13887 | 1975-06-30 | sin línea (texto no consolidado) | No |
| RDL 4/2000 (TR Seguridad Social Funcionarios Civiles) | BOE-A-2000-12140 | 2026-10-21 | 2026-10-21 | No |
| RD 375/2003 (Reglamento General del Mutualismo Administrativo) | BOE-A-2003-7527 | 2024-12-21 | 2024-12-21 | No |
| RD 577/1997 (Estatuto de MUFACE) | BOE-A-1997-9874 | 2026-06-12 | 2026-06-12 | No |
| RDL 670/1987 (TR Clases Pasivas) | BOE-A-1987-12636 | 2026-10-21 | 2026-10-21 | No |
| LGSS (RDL 8/2015) | BOE-A-2015-11724 | 2026-11-11 | 2026-11-11 | No |
| LO 3/1980 (Consejo de Estado) | BOE-A-1980-8648 | 2024-08-02 | 2024-08-02 | No |
| Orden TDF/379/2024 (directivos públicos profesionales) | BOE-A-2024-8609 | 2024-04-30 | 2024-04-30 | No |
| Resolución de 14-04-2026 (jornada y horarios en la AGE) | BOE-A-2026-8287 | 2026-04-15 | 2026-04-15 | No |
| Código Civil | BOE-A-1889-4763 | 2025-01-03 | 2025-01-03 | No |
| LJCA (Ley 29/1998) | BOE-A-1998-16718 | 2025-01-03 | 2025-01-03 | No |
| LGP (Ley 47/2003) | BOE-A-2003-21614 | 2022-12-24 | 2022-12-24 | No |
| Ley 31/2022 (PGE 2023, prorrogados) | BOE-A-2022-22128 | 2026-09-30 | 2026-09-30 | No |
| LGT (Ley 58/2003) | BOE-A-2003-23186 | 2024-12-21 | 2024-12-21 | No |
| LIRPF (Ley 35/2006) | BOE-A-2006-20764 | 2026-11-11 | 2026-11-11 | No |
| LIVA (Ley 37/1992) | BOE-A-1992-28740 | 2026-10-07 | 2026-10-07 | No |
| LIS (Ley 27/2014) | BOE-A-2014-12328 | 2026-09-02 | 2026-09-02 | No |
| LOFCA (LO 8/1980) | BOE-A-1980-21166 | 2022-07-29 | 2022-07-29 | No |
| Ley 22/2009 (financiación de las Comunidades Autónomas) | BOE-A-2009-20375 | 2022-07-29 | 2022-07-29 | No |
| TRLRHL (RDL 2/2004) | BOE-A-2004-4214 | 2026-10-07 | 2026-10-07 | No |
| Concierto Económico con el País Vasco (Ley 12/2002) | BOE-A-2002-9969 | 2025-04-30 | 2025-04-30 | No |
| Convenio Económico con Navarra (Ley 28/1990) | BOE-A-1990-31117 | 2025-07-25 | 2025-07-25 | No |
| Ley 31/1990, art. 103 (creación de la AEAT) | BOE-A-1990-31180 | 2015-03-25 | 2015-03-25 | No |
| Orden PRE/3581/2007 (departamentos de la AEAT) | BOE-A-2007-21228 | 2025-09-13 | 2025-09-13 | No |
| Orden de 2 de junio de 1994 (estructura de la AEAT) | BOE-A-1994-12973 | 2024-02-07 | 2024-02-07 | No |
| Resolución de 13-01-2021 (estructura y organización territorial de la AEAT) | BOE-A-2021-519 | 2025-09-01 | 2025-09-01 | No |
| Resolución de 13-01-2021 (Departamento de Gestión Tributaria) | BOE-A-2021-590 | 2025-12-26 | 2025-12-26 | No |
| Resolución de 13-01-2021 (Área de Aduanas e Impuestos Especiales) | BOE-A-2021-591 | 2026-07-03 | 2026-07-03 | No |
| Resolución de 13-01-2021 (Área de Informática Tributaria) | BOE-A-2021-710 | 2024-02-08 | 2024-02-08 | No |
| Resolución de 13-01-2021 (Delegación Central de Grandes Contribuyentes) | BOE-A-2021-671 | 2021-01-16 | 2021-01-16 | No |
| Resolución de 27-05-2023 (área de recaudación de la AEAT) | BOE-A-2023-12914 | 2025-09-29 | 2025-09-29 | No |
| Resolución de 24-03-1992 (inspección de los tributos, Departamento de Inspección Financiera y Tributaria) | BOE-A-1992-7179 | 2026-07-03 | 2026-07-03 | No |
| RGAT (RD 1065/2007) | BOE-A-2007-15984 | 2026-10-07 | 2026-10-07 | No |
| RD 1619/2012 (Reglamento de facturación) | BOE-A-2012-14696 | 2026-03-31 | 2026-03-31 | No |
| RGR (RD 939/2005) | BOE-A-2005-14803 | 2024-01-31 | 2024-01-31 | No |
| Orden HFP/311/2023 (límite exento de garantías en aplazamientos) | BOE-A-2023-8119 | 2023-03-31 | 2023-03-31 | No |
| LEC (Ley 1/2000) | BOE-A-2000-323 | 2026-10-07 | 2026-10-07 | No |
| RGRST (RD 2063/2004) | BOE-A-2004-18398 | 2019-09-20 | 2019-09-20 | No |
| RGRVA (RD 520/2005) | BOE-A-2005-8662 | 2023-04-05 | 2023-04-05 | No |
| RIRPF (RD 439/2007) | BOE-A-2007-6820 | 2026-10-07 | 2026-10-07 | No |
| Orden HAC/1425/2025 (módulos 2026) | BOE-A-2025-25272 | 2025-12-11 | 2025-12-11 | No |
| Orden HAC/1161/2026 (módulos 2027) | BOE-A-2026-23174 | 2026-11-05 | 2026-11-05 | No |
| RIS (RD 634/2015) | BOE-A-2015-7771 | 2024-01-31 | 2024-01-31 | No |
| RIVA (RD 1624/1992) | BOE-A-1992-28925 | 2026-02-28 | 2026-02-28 | No |
| Ley 19/1991 (Impuesto sobre el Patrimonio) | BOE-A-1991-14392 | 2023-12-28 | 2023-12-28 | No |
| Ley 29/1987 (ISD) | BOE-A-1987-28141 | 2022-12-28 | 2022-12-28 | No |
| TRLITPAJD (RDL 1/1993) | BOE-A-1993-25359 | 2026-03-21 | 2026-03-21 | No |
| Ley 38/1992 (Impuestos Especiales) | BOE-A-1992-28741 | 2026-09-30 | 2026-09-30 | No |
| TRLIRNR (RDL 5/2004) | BOE-A-2004-4527 | 2023-05-25 | 2023-05-25 | No |
| Ley 38/2022 (gravámenes temporales e ITSGF) | BOE-A-2022-22684 | 2024-12-21 | 2024-12-21 | No |
| Código de Comercio | BOE-A-1885-6627 | 2023-05-09 | 2023-05-09 | No |
| RD 1676/2009 (Consejo para la Defensa del Contribuyente) | BOE-A-2009-19438 | 2017-12-30 | 2017-12-30 | No |
| Orden EHA/586/2011 (modelo 111) | BOE-A-2011-4948 | 2011-03-18 | 2011-03-18 | No |
| Orden HAC/1398/2003 (colaboración social) | BOE-A-2003-11044 | 2025-01-31 | 2025-01-31 | No |
| Orden HAC/342/2021 (modelos 234, 235 y 236) | BOE-A-2021-5780 | 2024-03-22 | 2024-03-22 | No |
| Orden HAC/266/2024 (modelo 239) | BOE-A-2024-5722 | 2024-03-22 | sin línea (texto no consolidado) | No |
| Orden HAC/277/2026 (modelos de IRPF y Patrimonio, ejercicio 2025) | BOE-A-2026-7041 | 2026-03-27 | 2026-03-27 | No |
| Ley 8/1989 (Tasas y Precios Públicos) | BOE-A-1989-8508 | 2017-11-09 | 2017-11-09 | No |
