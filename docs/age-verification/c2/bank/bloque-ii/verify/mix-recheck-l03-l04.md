# Mix re-check, m02-l03 and m02-l04 (round R3, 2026-11-07)

Blind re-judge of the «copies a kept question» failures in `m02-l03.authored-mix.draft.json` and
`m02-l04.authored-mix.draft.json` under the coordinator ruling of 2026-11-07: a variant copies a kept question of the
same lesson only when it tests the same fact, angle and key and carries over two or more of that question's
distractors, verbatim or reworded. Kept = `m02-l0N.kept-derived.json` + `m02-l0N.authored.draft.json`, minus
`drops.tsv`. For each question that passes the copy test, the other checks of `verify-spec.md` were run: key, unique,
citation (`check_draft.py`: 0 anchor misses on both drafts), the rest of style (§ 12 items 1–15) and official
(packs `c2/bloque-ii/questions/m02-l03.md`, `m02-l04.md`). Sources: `pdftotext -layout` of Ley 16/1985 (2026-10-03),
RD 1708/2011 (2024-03-27), LPAC (2024-11-06), LRJSP (2024-08-02), RD 203/2021 (2025-04-02).

A distractor counts as carried when it makes the same wrong claim as one of the kept question's distractors. A
distractor that only shares one word or the pattern, but makes another claim, does not count. Borderline calls are
given in the reason column.

| id | carried distractors (kept id) | copy verdict | other checks | final verdict | reason |
|---|---|---|---|---|---|
| m02-l03-q138 | 1 (q001): soportes informáticos | PASS | key, unique, citation, style, official PASS | PASS | Art. 49.1: «Se excluyen los ejemplares no originales de ediciones», which is the only exclusion. The cien años distractor is explained by art. 49.4. Note: «anteriores a cien años» reads awkwardly but is not wrong. |
| m02-l03-q139 | 1 (q007): firma (de su autor → de un órgano) | PASS | all PASS | PASS | Key is the wording of art. 2.2.c). Soporte físico, expediente and firma are each explained. 2022-P2-5 asks the reverse (it gives the definition and asks the name), so check 5 passes. |
| m02-l03-q140 | 1 (q008): «reunidos por una persona…, cualquiera que sea el procedimiento» → «un mismo interesado, con independencia del procedimiento» | PASS | all PASS | PASS | Key is the wording of art. 2.2.d). q008's «finalizados de un mismo órgano, ordenados por fecha» and q140's «misma serie documental, firmados por el mismo órgano» make different claims and do not count (borderline). |
| m02-l03-q141 | 2 (q009): «presentados por los interesados en el registro» → «firmados por el interesado y registrados»; «obren en los archivos públicos» → «se conservan en el archivo electrónico único» | FAIL | not run | FAIL | Copies kept q009: same stem without the article, same key verbatim, two distractors carried reworded. |
| m02-l03-q143 | 1 (q069): ENS verbatim | PASS | all PASS | PASS | Art. 46.1 RD 203/2021: «admitido en el Esquema Nacional de Interoperabilidad y normativa correspondiente». The other distractors are new (Comisión de Archivos, calendario). |
| m02-l03-q144 | 1 (q016): «Solo para los órganos de la AGE» → «Solo para la AGE» | PASS | all PASS | PASS | Art. 38.2: «plena eficacia y validez para todas las Administraciones Públicas». q016's «AGE y su sector público institucional» and q144's «solo organismos públicos vinculados» make different claims (borderline). |
| m02-l03-q145 | 1 (q017): lectura pública / préstamo temporal (Bibliotecas) | PASS | all PASS | PASS | Art. 59.1: «la investigación, la cultura, la información y la gestión administrativa». Docencia and difusión comercial are new. Bibliotecas are explained by art. 59.2. |
| m02-l03-q146 | 1 (q018): Bibliotecas (conservan, catalogan… libros) | PASS | all PASS | PASS | Art. 59.1 lists a closed set of verbs: «reúnen, conservan, ordenan y difunden». «Tramitan y resuelven» does not count as q018's «digitalizan y anotan». Note: «procedimientos que los documentos documentan» is clumsy but grammatical. |
| m02-l03-q149 | 1 (q020): «mientras siguen en curso» → «mientras se tramitan» | PASS | all PASS | PASS | Art. 55.1: «una vez finalizados los procedimientos». q020's «conserva seis meses los documentos en papel» and q149's «documentos en papel digitalizados por las oficinas» make different claims (borderline). |
| m02-l03-q152 | 2 (q021): «fecha en que el documento llegue a la unidad» → «fecha en que el órgano destinatario reciba»; «fecha en que se resuelva el procedimiento» → «fecha de la resolución que ponga fin al trámite» | FAIL | not run | FAIL | Copies kept q021: same fact, angle and key, two distractors carried reworded. |
| m02-l03-q153 | 1 (q084): oficinas de asistencia (with «más próximas al domicilio» added) | PASS | all PASS | PASS | Art. 16.2 LPAC: «a sus destinatarios y a las unidades administrativas correspondientes desde el registro en que hubieran sido recibidas». q084's «archivos de gestión» and q153's «archivo central, desde el archivo de gestión» name different archives (borderline). Official 2024-P2-9 keys «sin dilación», a different angle. |
| m02-l03-q159 | 2 (q041): «hasta que finaliza el procedimiento» → «la finalización de su tramitación»; «hasta su transferencia al archivo histórico» → «su ingreso en el archivo histórico» | FAIL | not run | FAIL | Copies kept q041: same definition, angle and key, two distractors carried reworded. |
| m02-l03-q167 | 2 (q055): Ministerio de Hacienda verbatim; «Ministerio de la Presidencia, Justicia y Relaciones con las Cortes» → «Ministerio de la Presidencia» | FAIL | not run (also item 13) | FAIL | Copies kept q055. Also, «Ministerio de la Presidencia» is not a current department name (item 13). |
| m02-l03-q170 | 3 (q058): archivos centrales de los Ministerios, archivos de oficina o de gestión, Archivos Históricos Provinciales | FAIL | not run | FAIL | Copies kept q058: all three distractors carried, in a new order. |
| m02-l03-q171 | 1 (q012): «sin conexión alguna con el Registro Electrónico General» (vs q062 also 1: «independiente del REG») | PASS | all PASS | PASS | Art. 16.1: «plenamente interoperable e interconectado con el Registro Electrónico General de la Administración de la que depende». Check 5: 2025-P2-7 tests art. 16.4 (all registers interoperable), a different sentence and subject. «Autónomo, sin conexión alguna con el REG» echoes its «Autónomos», but the fact and key differ, so check 5 passes (flagged for the coordinator). |
| m02-l03-q173 | 1 (q078): copias auténticas | PASS | all PASS | PASS | Art. 16.1: «También se podrán anotar en el mismo, la salida de los documentos oficiales dirigidos a otros órganos o particulares». The only «also» item is the salida. q078's «resoluciones de eliminación» and q173's «resoluciones de los recursos» make different claims. |
| m02-l03-q174 | 1 (q014): horario de atención de las oficinas presenciales | PASS | all PASS | PASS | Art. 16.1 names órgano, fecha y hora oficial «y los días declarados como inhábiles». The trámites distractor is explained by the next sentence (the trámites list goes in the sede). |
| m02-l03-q175 | 1 (q133): calendario de conservación aprobado | PASS | all PASS | PASS | Art. 11.7.º: «acompañadas de los correspondientes instrumentos de descripción elaborados», a single accompaniment. q133's «informe previo de la Comisión de Archivos» and q175's «dictámenes de valoración de la Comisión Calificadora» name different bodies (borderline). Official 2022-P2-7 asks which archive has this function, a different angle and key. |
| m02-l03-q176 | 1 (q130): archivos históricos provinciales de las Delegaciones del Gobierno, verbatim | PASS | all PASS | PASS | Art. 10.1.1.º: «Coordinar y controlar el funcionamiento de los distintos archivos de gestión, así como proporcionar el asesoramiento técnico necesario a las unidades». The stem is identical to q130's, but two of the three distractors are new. Official 2024-P2-7 asks the reverse (which archive coordinates), so the key differs. |
| m02-l04-q173 | 1 (q002): «Solo al iniciar un nuevo procedimiento» → «Solo al inicio de cada procedimiento» | PASS | all PASS | PASS | Art. 14.1 LPAC: «podrá ser modificado por aquella en cualquier momento». Art. 3.2 RD 203/2021 also allows it at a later phase, so the «solo al inicio» distractor stays wrong. q002's «una vez en cada procedimiento» and q173's «una vez al año» set different limits (borderline). |
| m02-l04-q176 | 1 (q011): protección de datos | PASS | all PASS | PASS | Art. 40.1 LRJSP: «que reúna los requisitos exigidos por la legislación de firma electrónica». The ENI, the normas técnicas de la sede and the ENS are different distractors from q011's. |
| m02-l04-q178 | 1 (q099): Consejo de Ministros | PASS | all PASS | PASS | Art. 6.1 RD 203/2021: «La creación requerirá informe favorable de la Comisión Ministerial de Administración Digital respectiva». Check 5: same fact, angle and key as 2024-P2-4, but its distractors (titular del Departamento, Secretaría General Técnica, Comisión Superior Digital) are not carried. The Subsecretaría is a different organ from the SGT, so check 5 passes (flagged). The SGAD is a current organ. |
| m02-l04-q179 | 3 (q112): aviso al dispositivo, verbatim; puesta a disposición en la sede, verbatim; «firma de la resolución por el órgano competente» → «firma de la notificación por el órgano emisor» | FAIL | not run | FAIL | Copies kept q112: identical stem, same key, all three distractors carried. |
| m02-l04-q185 | 1 (q042): registro de notificaciones rechazadas | PASS | key, unique, citation PASS; style FAIL (item 13) | FAIL | The explanation names the non-current «Ministerio de Política Territorial y Función Pública». The key matches art. 43.4 LPAC («funcionará como un portal de acceso»). |

## Summary

Re-judged: 24. Copy test: 18 PASS, 6 FAIL (l03 q141, q152, q159, q167, q170; l04 q179).

Final: 17 PASS, 7 FAIL.

- PASS: m02-l03-q138, q139, q140, q143, q144, q145, q146, q149, q153, q171, q173, q174, q175, q176; m02-l04-q173,
  q176, q178.
- FAIL, copy (check 4): m02-l03-q141, q152, q159, q167 (also item 13), q170; m02-l04-q179.
- FAIL, item 13: m02-l04-q185.

Flags for the coordinator, not verdict-changing: m02-l03-q171 (official 2025-P2-7's «Autónomos» echoed on another
fact) and m02-l04-q178 (same fact, angle and key as 2024-P2-4, with all distractors new). `drops.tsv` was not touched.
