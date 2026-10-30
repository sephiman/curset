# Case plan — round R4 (supuestos prácticos), 2026-10-28

Requirements R6.1–R6.2; style guide § 11 and checklist § 12; bank plan § 3. Twenty cases `sp-01` … `sp-20`, each a
scenario plus 20 questions. The slots per case are in `slots.tsv`; the briefs below fix the body, the place and the
threads, so the twenty cases do not ask the same four things.

## Proportions

Part 2 of the six exams of 2022–2025 (300 questions, reserves included), scaled to 20 questions: bloque III 8.1,
IV 6.1, V 5.1, II 0.5 (I 0.2). The slots give, per case on average: III 8.3, IV 5.7, V 5.5, II 0.6. By tema over the
20 cases: III.3 79, III.4 70, III.6 12, III.2 5; IV.5 46, IV.4 25, IV.6 19, IV.8 8, IV.3 6, IV.7 6, IV.9 3; V.2 48,
V.3 30, V.4 15, V.5 13, V.6 3; II.1 3, II.2 1, II.3 4, II.4 4. A writer may move one slot between temas of the same
bloque when a thread needs it, and says so in the notes.

## Shared rules for the briefs

- Bodies are real AGE bodies with their current names; every person is fictional (first name + two surnames, no
  name of a known public figure). A person keeps one name through the case.
- Dates: 2027 unless the brief says otherwise (the course cites the law in force in 2027, so no `cambio-pendiente`
  doubt). 2027 national festivos: 1 Jan (Fri), 6 Jan (Wed), 25 Mar Jueves Santo (regional in most CCAA), 26 Mar
  Viernes Santo, 1 May (Sat), 15 Aug (Sun), 12 Oct (Tue), 1 Nov (Mon), 6 Dec (Mon), 8 Dec (Wed), 25 Dec (Sat).
  The scenario says where the office is; each computation either avoids every festivo of that place or names it.
- **Madrid 2027 inhábiles (verified by the sp-08 and sp-09 verifiers against Decreto 82/2026 of the Comunidad and the city's local festivos):** Fri 1 Jan, Wed 6 Jan, Fri 19 Mar (San José), Thu 25 Mar, Fri 26 Mar, Sat 1 May, Mon 16 Aug (Asunción moved), Tue 12 Oct, Mon 1 Nov, Tue 9 Nov (Almudena, city), Mon 6 Dec, Wed 8 Dec, Sat 25 Dec; San Isidro (15 May) falls on a Saturday. Other places: establish the 2027 regional and local calendar and say what you relied on. `case_check.py` flags any of the Madrid dates written in a case.
- At least 10 questions per case compute a date or an amount (so 9 survive a drop). The brief lists candidate
  computations; the writer picks those the lesson supports.
- Computation codes. Dates: subsanación (art. 68 LPAC), audiencia (art. 82), información pública (art. 83), plazo
  máximo and silencio (arts. 21, 24), caducidad (art. 25), notificación electrónica rechazada (art. 43.2), plazo
  ampliado (art. 32), urgencia (art. 33), alzada/reposición (arts. 122, 124), revisión (art. 125), lesividad
  (art. 107), responsabilidad patrimonial (art. 67), contencioso (art. 46 LJCA, August), plazos de licitación,
  formalización, recurso especial, pago (LCSP), toma de posesión and cese (RD 364/1995 or the rule the lesson gives),
  permisos and vacaciones (TREBEP), excedencias and reingreso, prescripción de faltas y sanciones, quejas (RD
  951/2005), derechos RGPD, justificación de pagos a justificar. Amounts: valor estimado, umbrales SARA and contrato
  menor, garantías, penalidades por demora, modificación, suplemento/crédito extraordinario, transferencia,
  anticipo de tesorería, compromisos plurianuales, anticipos de caja fija, dietas and kilometraje (RD 462/2002),
  asistencias, subsidio de IT, compatibilidad, reintegro de subvenciones.

## Briefs

| Case | Body (place) | Threads | Candidate computations |
|---|---|---|---|
| sp-01 | Confederación Hidrográfica del Tajo (Madrid) | a vertido authorization request missing a document; resolution and alzada; an obras contract to repair a riverside structure; a Jefa de Sección who wins a concurso in another city; a funcionario who asks excedencia to care for a child; a gasto with no credit in the chapter | subsanación, plazo máximo/silencio, alzada, valor estimado, garantía definitiva, toma de posesión with change of residence, excedencia end date, suplemento amount |
| sp-02 | Subdelegación del Gobierno en Valladolid | a citizen's complaint about the oficina de asistencia en materia de registros; a fall in the building and a claim for damages; a cleaning services contract late in performance; a funcionaria's leave on a relative's death; a minor disciplinary matter; travel on official business | queja answer, responsabilidad patrimonial plazo, penalidades por demora, permiso days, prescripción, dietas and kilometraje, transferencia amount |
| sp-03 | Instituto Nacional de Administración Pública (Madrid) | an online training services contract; an agreement (convenio) with a university; a funcionaria interina; a comisión de servicios; course fees that generate credit; anticipos de caja fija; a student's right of access to personal data | SARA threshold, abierto simplificado plazos, garantía, convenio duration, comisión de servicios end, RGPD answer date, generación amount, caja fija limit |
| sp-04 | Instituto Nacional de Estadística (Madrid) | a company fined for not answering a survey (sancionador) and its reposición; a supply contract for tablets; personal laboral interviewers under the convenio único; a laboral employee on incapacidad temporal; an incorporación de crédito; pagos a justificar | caducidad, reposición, recurso deadline, entrega/recepción, IT subsidy amount, incorporación, justificación deadline |
| sp-05 | Biblioteca Nacional de España (Madrid) | a researcher's reproduction request refused and appealed; a digitisation services contract later modified; a funcionario appointed to a post that puts him in servicios especiales; a request for compatibility with private teaching; an inversión in shelving; a crédito extraordinario | alzada, modificación limit, revisión de precios, compatibility amount, reingreso, crédito extraordinario amount, fases |
| sp-06 | Confederación Hidrográfica del Guadalquivir (Sevilla) | an illegal water extraction file (sancionador); a resolution later found void; a contrato menor; a funcionaria victim of violencia de género (excedencia, traslado); a retiring funcionario (clases pasivas); an ampliación de crédito; transferencias corrientes | caducidad, prescripción, revisión de oficio, contrato menor limit, excedencia rights, jubilación date, ampliación amount |
| sp-07 | Mutualidad General de Funcionarios Civiles del Estado (Madrid; servicio provincial in Zaragoza) | a mutualista's benefit request and electronic notification; a maintenance contract for the IT system; IT of a mutualista; a funcionario moving to servicio en otras Administraciones; vacaciones; transferencias | notificación 10 días naturales, plazo máximo/silencio, IT subsidy, vacaciones days, valor estimado, contract duration/prórroga, transferencia amount |
| sp-08 | Servicio Público de Empleo Estatal (Madrid) | a grant scheme under concurrencia competitiva and a reintegro; a recurso extraordinario de revisión; a call-centre services contract under SARA and a recurso especial; a Jefe de Servicio dismissed from a libre designación post; birth leave; a minor fault | reintegro + interés de demora, revisión deadline, recurso especial deadline, formalización, cese/reassignment dates, nacimiento leave weeks/dates |
| sp-09 | Organismo Autónomo Parques Nacionales (Madrid; centre in Valsaín, Segovia) | a use authorization in a park and silence; a claim for damages after a fallen tree; an obras contract for a visitor centre (clasificación, recepción, garantía); fijo discontinuo laboral staff; travel by own car; a plurianual commitment | silencio date, responsabilidad patrimonial, clasificación threshold, recepción/plazo de garantía, kilometraje, plurianual limits, anticipo de tesorería |
| sp-10 | Fondo Español de Garantía Agraria O.A. (Madrid) | an aid recovery file notified by publication; a contencioso against it (August); an auditing services contract; a funcionario en prácticas acquiring the condition; reingreso from excedencia; a reparo of the Intervención | notificación edictal, contencioso with August, toma de posesión, reingreso, fiscalización plazo, documentos, transferencia |
| sp-11 | Instituto de la Juventud (Madrid) | grants to youth associations; a contract for organising a meeting, divided into lots; a complaint about a youth information office; data of minors; a funcionaria's reduced working day; a minor-fault procedure; dietas of a group | queja answer, lots and contrato menor, garantía, reducción de jornada, prescripción, dietas amounts, subvención justification, suplemento |
| sp-12 | Instituto de Turismo de España (Madrid) | an advertising services contract under SARA, an abnormally low offer and a recurso especial; a funcionario en servicios especiales; an interim funcionario's end; a selection board's assistance payments; a generación de crédito | ofertas anormalmente bajas plazo, recurso especial, formalización, asistencias amount, interino end, generación |
| sp-13 | Centro de Investigaciones Sociológicas (Madrid) | a fieldwork services contract; a convenio with a university; laboral staff selection; a funcionario on IT (MUFACE); anticipos de caja fija and their reposición; ADOK documents; electronic office and registry | plazos de licitación, garantía, convenio, MUFACE IT dates, caja fija limit, fases/documentos, transferencia |
| sp-14 | Instituto de Salud Carlos III (Madrid) | a reagent supply contract under urgency; a procedure whose plazos are extended; a funcionaria on excedencia por interés particular and her reingreso; a very serious fault and its prescripción; vinculación and plurianual expenditure; pagos a justificar | urgencia halving, ampliación, excedencia dates, prescripción, plurianual limits, justificación, garantía |
| sp-15 | Jefatura Central de Tráfico (Jefatura Provincial in Toledo) | a citizen helped at the counter and through the sede; a registry submission; a security services contract late in performance; a funcionaria's leave to care for a seriously ill child; servicio activo; travel; transferencias corrientes | subsanación, alzada, penalidades, permiso dates, dietas, kilometraje, transferencia |
| sp-16 | Instituto Nacional de las Artes Escénicas y de la Música (Madrid) | a spectator injured in a theatre and a claim for damages; a supply contract for instruments; laboral staff under the convenio único; a laboral employee's birth subsidy; an ampliación de crédito; an inversión | responsabilidad patrimonial, Consejo de Estado threshold, garantía, subsidio amount, ampliación amount, fases |
| sp-17 | Delegación de Economía y Hacienda en Murcia | a company obliged to deal electronically that files on paper; a reposición; a small works contract (abierto simplificado sumario); a new funcionario's toma de posesión; a disciplinary file with suspensión provisional; caja fija; dietas (Murcia festivos: 19 Mar, 9 Jun) | subsanación (art. 68.4), reposición, plazos de licitación, toma de posesión, suspensión provisional limit, caja fija, dietas |
| sp-18 | Centro de Estudios Políticos y Constitucionales (Madrid) | a co-publishing convenio; archive and registry of documents; a claim needing the Consejo de Estado; a funcionaria in comisión de servicios; jubilación; transfers with LGP limits; payments phases | convenio, responsabilidad patrimonial, comisión end, jubilación date, transferencia limits, fases, pago |
| sp-19 | Mutualidad General Judicial (Madrid) | a mutualista's benefit refused; alzada; a software maintenance contract (duration, prórroga, preaviso); an incompatibility request; IT; an incorporación; pagos a justificar; an access-to-data request | alzada, prórroga preaviso, compatibility amount, IT dates, incorporación, justificación, RGPD answer date |
| sp-20 | Dirección General del Instituto Geográfico Nacional (Ministerio de Transportes y Movilidad Sostenible, Madrid) | a GNSS equipment supply contract under SARA; a data breach of a survey's personal data; new funcionarios after a selection process; permisos; a trip abroad (dietas en el extranjero); a transfer between programmes of the department | SARA, garantía, plazo de entrega, brecha 72 horas, toma de posesión, permiso dates, dietas en el extranjero, transferencia |

## Pairs

The «choose one of two» rule: after verification the cases are paired for the simulation preset (R5) into ten
pairs of similar difficulty and tema mix. The pairing is computed from the kept questions (mean difficulty, count of
computations, bloque mix, engine mix) and recorded in `docs/age-cases-ledger.md`.
