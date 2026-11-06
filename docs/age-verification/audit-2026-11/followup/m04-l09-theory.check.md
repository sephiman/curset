# m04-l09 — theory follow-up, blind check (2026-11-06)

Scope: the «### Incapacidad temporal» hunk of `git diff HEAD -- content/age-administrativo-c1/es/lessons/m04-l09.md`
(art. 169.1.a) 1.ª–5.ª, violencia de género documents and causalidad, art. 172 cotización). Norm:
`sources/normativa/BOE-A-2015-11724_lgss_2026-10-21.pdf`, new wording (RDL 31/2026, effect 01-12-2026), read with
`pdftotext -layout`. Anchors resolved with `CourseCitations.build(...)._anchor('m04-l09', c, 'es')`:
`art. 169.1.a) LGSS, desde 01-12-2026` → `boe-a-2015-11724-art-169`; `art. 172 LGSS, desde 01-12-2026` →
`boe-a-2015-11724-art-172`; `art. 171 LGSS` → `boe-a-2015-11724-art-171`. No misses.

Checks: F faithful, C cited, P placed/scoped, V voice.

| # | Item | Lines | F | C | P | V | Verdict | Reason |
|---|---|---|---|---|---|---|---|---|
| 1 | Lead-in «Desde el 1 de diciembre de 2026, tienen la consideración de situaciones especiales … las siguientes» | 68–69 | FAIL | P | FAIL | FAIL | FAIL | The date repeats the citation's `desde 01-12-2026` mark, which the spec makes the course's only signal for pending wording. It also reads as if all five situations start on 01-12-2026, though 1.ª–3.ª are in today's text too (the «Redacción anterior» lists menstruación/interrupción, gestación desde la semana 39 and donante). Norm: «Tendrán la consideración de situaciones especiales de incapacidad temporal por contingencias comunes las siguientes:». |
| 2 | 1.ª menstruación incapacitante secundaria o interrupción del embarazo, voluntaria o no, mientras reciba asistencia sanitaria por el Servicio Público de Salud y esté impedida para el trabajo | 71–72 | P | P | P | P | PASS | Keeps «mientras reciba asistencia sanitaria por el Servicio Público de Salud y esté impedida para el trabajo» and «voluntaria o no». |
| 3 | 1.ª exception: interrupción por accidente de trabajo o enfermedad profesional, incapacidad temporal por contingencias profesionales | 72–73 | P | P | P | P | PASS | «…sea debida a accidente de trabajo o enfermedad profesional, en cuyo caso tendrá la consideración de situación de incapacidad temporal por contingencias profesionales». Shortened, nothing dropped. |
| 4 | 2.ª gestación desde el día primero de la semana trigésima novena | 74 | P | P | P | P | PASS | «La de gestación de la mujer trabajadora desde el día primero de la semana trigésima novena». |
| 5 | 3.ª donante, sentence 1 | 76 | P | P | P | P | PASS | «Aquella en la que se encuentre la persona trabajadora donante de órganos o tejidos para su trasplante». |
| 6 | 3.ª donante, scope: días discontinuos e ininterrumpidos … hasta el alta por curación | 76–79 | P | P | P | P | PASS | «tanto los días discontinuos como ininterrumpidos … como los transcurridos desde el día del ingreso hospitalario para la realización de esta preparación o la realización del trasplante hasta que sea dado de alta por curación»; both branches and «de la Seguridad Social» kept. |
| 7 | 4.ª trastorno menopáusico secundario codificado a tal efecto | 81–83 | P | P | P | P | PASS | Verbatim, incl. «codificado a tal efecto», «por el Servicio Público de Salud» and «como consecuencia de dicha patología». |
| 8 | 5.ª lesiones causadas por el (ex)cónyuge o pareja, aun sin convivencia | 84–86 | P | P | P | P | PASS | Verbatim, incl. «aun sin convivencia»; correctly says only «asistencia sanitaria» (the norm does not add «por el Servicio Público de Salud» here). |
| 9 | 5.ª documents antes del alta médica por curación o mejoría, or sentencia condenatoria | 88–91 | P | P | P | P | PASS | «con anterioridad al alta médica por curación o mejoría hayan sido expedidos los documentos sanitarios oficiales de comunicación a la Fiscalía o al órgano judicial, orden de protección, resolución que acuerde una medida cautelar o informe del Ministerio Fiscal que recoja la existencia de indicios de violencia de género; o bien que se hubiera dictado sentencia condenatoria». Four documents and the alternative kept. Citation at the paragraph end covers it. |
| 10 | 5.ª causalidad expresa en los documentos | 91–93 | P | P | P | P | PASS | «En dichos documentos deberá figurar de forma expresa la relación de causalidad entre la lesión … y el acto de violencia que determina la condena, protección o inicio de la investigación». Note: the norm's sentence «El facultativo médico del Servicio Público de Salud identificará estas situaciones especiales mediante la correspondiente codificación» is not stated. It is a duty of the doctor, not a requisite of the worker, and its omission makes no lesson sentence false, so not a FAIL. |
| 11 | 172: 1.ª, 3.ª, 4.ª y 5.ª sin períodos mínimos | 95 | P | P | P | P | PASS | «En las situaciones especiales previstas en el artículo 169.1.a).1.ª, 3.ª, 4.ª y 5.ª no se exigirán periodos mínimos de cotización». |
| 12 | 172: 2.ª, períodos del art. 178.1 según la edad al inicio del descanso, referencia fecha de la baja médica | 95–97 | P | P | P | P | PASS | «se exigirá que la persona interesada acredite los periodos mínimos de cotización señalados en el artículo 178.1 según la edad que tenga cumplida en el momento de inicio del descanso, tomando como referencia la fecha de la baja médica». The new «tomando como referencia la fecha de la baja médica» is kept. |
| 13 | Subsidio a tanto por ciento; donación al 100 % (moved, unchanged) | 99–101 | P | P | P | P | PASS | Same text as HEAD, PASS in `audit-2026-11/theory.md` l.29. Note: art. 171.1 also has new wording from 01-12-2026 (RDL 31/2026 art. 1.4; donación now «prevista en el artículo 169.1.a).3.ª», plus a third paragraph for 1.ª, 2.ª, 4.ª y 5.ª). The sentences hold under both wordings; whether the citation should carry `, desde 01-12-2026` is for the coordinator, outside this hunk's brief. |

## FAIL replacement

- #1, lines 68–69: `Tienen la consideración de situaciones especiales de incapacidad temporal por contingencias comunes las siguientes (art. 169.1.a) LGSS, desde 01-12-2026):`

## Voice

No «never does» item in the hunk: no fillers, triads, rhetorical questions, «no solo… sino», closers or stacked
hedges; Peninsular Spanish; no coined terms (all wording is the norm's). The repeated citation on each list item is
course practice.

## Counts

13 items: 12 PASS, 1 FAIL (#1).
