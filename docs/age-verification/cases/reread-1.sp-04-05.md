# Re-read 1 — dropped questions of sp-04 and sp-05 (R4, 2026-10-28)

Under «Rulings of 2026-10-28 (user)» in `verify-spec.md`: dependence fails only when no case fact is used (scenario or
own stem) or the question contradicts the scenario; copies are judged on stem and options, not on the kind of
computation. sp-04 judged against the current scenario (after «Replacements 1»); q21–q25 not judged here. sp-05's
scenario is unchanged since verify-1; its two SCENARIO faults stand. Checks other than the re-judged ones are taken from
`sp-04.verify-1.md` / `sp-05.verify-1.md`, where all were PASS for the restored rows.

## sp-04

| id | original check | new verdict | reason |
|---|---|---|---|
| q03 | 4 dependence | RESTORED | Stem names the INE's sanctioning procedure against Transportes Valdemaría, S.L. (case facts); consistent with «el INE acuerda iniciar el procedimiento sancionador»; checks 1–3, 5 PASS. |
| q05 | 5 copy | DROPPED | Current scenario no longer has the alta médica por curación (15 Jun 2027) the key counts from, nor «visitante»; the stem does not supply it, so the key rests on a missing fact (check 1/4). Copy not re-judged. |
| q06 | 4 dependence | RESTORED | Stem names the tabletas delivered by Tecnoterminales Alcor, S.L. (case facts); delivery 4 Nov 2027 still in the scenario; checks 1–3, 5 PASS. |
| q11 | 4 dependence | RESTORED | Stem uses the INE and its personal laboral vacancies; no contradiction with «El INE convoca 20 plazas de personal laboral del Convenio único» (the prior offer of art. 27.2 precedes any ingreso libre convocatoria); checks 1–3, 5 PASS. Note: `depends_on` still quotes the old «quiere cubrir 20 puestos vacantes». |
| q17 | 4 dependence (+ `follows: q16` unstated) | RESTORED | Stem uses the INE's remanentes and the 2027 budget (case facts), consistent with the scenario; it does not need q16's answer (the stem names the remanentes itself), so the unstated `follows` is metadata, not a dependence fault; checks 1–3, 5 PASS. |

## sp-05

| id | original check | new verdict | reason |
|---|---|---|---|
| q01 | 5 copy | DROPPED | Near-identical stem to 2025 extr. Supuesto I q17 («¿Debería abstenerse [pariente] de…?») with the official key «Sí… consanguinidad dentro del cuarto grado» and a «No… tercer grado de consanguinidad» distractor: the ruling's key-plus-distractor case. |
| q04 | 1 key (SCENARIO) | DROPPED | Rests on the alzada fault (reposición lies, Estatuto BNE art. 9.4); stands. |
| q06 | 4 dependence | RESTORED | Stem names Archivos Digitales Ibérica, S.A. and the digitalización contract (case facts); a key stating the deciding fact no longer fails; checks 1–3, 5 PASS. |
| q09 | 5 copy | RESTORED | Official 2022 extr. SII reserva 2 asks the percentage (10/20/30/50 % options); this stem asks the euro ceiling for the case's lote, options are amounts from the case's 54.000 euros: same kind of computation, not the same stem or options; checks 1–4 PASS. |
| q10 | 4 dependence | RESTORED | Stem names Don Ernesto Palomares Ruiz and his personal eventual post (case facts); key stating the deciding fact no longer fails; check 5 PASS in verify-1 (closeness to 2025 extr. SII q2 noted there, options differ). |
| q11 | 5 copy | RESTORED | Official 2022 extr. SI q14 asks which statement about Mir's situation is correct (rule options); this asks a date with the case's 30 Sep cese, options are dates: not the same stem or options; key Tue 2 Nov 2027 rechecked; checks 1–4 PASS. |
| q12 | 4 dependence | RESTORED | Stem carries the 28 Oct date and Don Julián Ibáñez Roldán (case facts); official 2024 ord. SII reserva 1 asks the plazo (10/15 días options), this asks the effect of silence: not a copy; checks 1–3, 5 PASS. |
| q13 | 4 item 16 | DROPPED | Stray periods in the explanation; not a dependence fault. |
| q17 | 5 copy | DROPPED | Near-identical stem to 2025 extr. Supuesto I q6 («¿A qué artículo del presupuesto se imputa(ría) la compra de…?») with the official key art. 63 and official distractors art. 62 and art. 21, same titles. |
| q18 | 4 key misworded | DROPPED | Key states the opposite of art. 2.3 RD 725/1989's reason; not a dependence fault. |
| q19 | 4 dependence | RESTORED | Stem uses the Intervención Delegada over the Biblioteca (case facts), consistent with the scenario; checks 1–3, 5 PASS. |
| q20 | 4 dependence | RESTORED | Stem uses the IGAE's revisión of the organismo (case facts), consistent with the scenario; checks 1–3, 5 PASS. |

## Summary

- sp-04: re-read 5; restored 4 (q03, q06, q11, q17); still dropped 1 (q05: missing fact in the current scenario).
- sp-05: re-read 12; restored 7 (q06, q09, q10, q11, q12, q19, q20); still dropped 5 (q04 key/SCENARIO; q13 and q18
  style other than dependence; q01 and q17 copy).
- Overlap note for the coordinator: restored sp-04 q03, q06, q11, q17 sit beside their replacements q21–q25 (same
  temas: q03/q21 III.3, q06/q23 III.4, q11/q24 IV.8, q17/q25 V.2).
