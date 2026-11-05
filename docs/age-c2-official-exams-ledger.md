# Ledger de exámenes oficiales — Auxiliar Administrativo del Estado (C2), ingreso libre

Round R0a, 2026-11-05. Input for the «Exámenes oficiales» practice set (requirements v1.1, R5.2, which takes C1's R5.5). The set is not built here.

Columns: **Nº** as numbered by position in the questionnaire. **Tema / tipo**: for bloque I and bloque II questions, the tema of the 2025 programme (`content/age-auxiliar-c2/sources/programa.md`) as `bloque.tema`, a second tema in brackets when the choice is debatable; for psicotécnico questions, `psico:` and the type of `docs/age-c2-psicotecnico-index.md`. **Estado**: see below. **Clave**: as printed on the definitive answer sheet. **Nota de clave**: «Clave oficial discutida» and the reason. **Nota**: why a question is excluded or doubtful, the current name or label the practice set shows, errata in the official text, the modelo B number (in modelo A tables) or the modelo A question it repeats (in modelo B tables), and the transcription mark of the image table.

Estado (same rules as `docs/age-official-exams-ledger.md`, C1):

- `vigente`: enters the practice set with the official key, no note.
- `vigente-con-nota`: enters with the official key and a visible note: «Clave oficial discutida» (the key is not supported by the text in force, or not unique), «Denominación actual» (an organ renamed since), «Etiqueta actual» (a Windows 11 / Microsoft 365 label that changed; «sin confirmar en la interfaz española» when not checked on a Spanish-locale install).
- `norma modificada: …`, `función retirada`, `fuera de temario`: excluded from the set, with the reason. «(cambio-pendiente, desde DD-MM-YYYY)» marks a change already published that takes effect later.
- `dudosa`: could not be settled; excluded from the set.
- `anulada`: voided on the definitive answer sheet; not in the set.

Status was checked against the consolidated texts in `content/age-auxiliar-c2/sources/normativa/` (version in force on 2026-11-05), ofimática against Windows 11 and Microsoft 365 desktop (Anexo I 2.2), and every psicotécnico item was recomputed (arithmetic and tables in Python, verbal items against the DLE). Official keys are never a source of facts for authored questions.

**Software versions.** The 2025 convocatoria fixes Windows 11 and Microsoft 365 desktop. The 2022 and OEP 2020 questionnaires name Windows 10 and Office/Excel 2019: their questions are kept when the feature still exists, with an «Etiqueta actual» note when a label changed, and excluded as `función retirada` when it does not.

**Naming.** The files `conv2020_*` are the OEP 2020 exams (cover «CUESTIONARIO 19 / AUX–LI», answer sheets «Oferta de Empleo Público de 2020»), the same pattern as in C1. The 2020 sets are «programa anterior», as in C1 (R3.4; Juanjo, 2026-11-05): their questions are classified against the 2025 programme and go into the practice set, filtered as above, but never into tema counts or programme structure.

**Not published.** The INAP page publishes no Auxiliar extraordinario for 2025 or 2022.

## Summary

| Questionnaire | Questions | vigente | vigente-con-nota | anulada | norma modificada | función retirada | dudosa | fuera de temario |
|---|---|---|---|---|---|---|---|---|
| conv2025_A | 120 | 118 | 0 | 1 | 1 | 0 | 0 | 0 |
| conv2025_B | 120 | 118 | 0 | 1 | 1 | 0 | 0 | 0 |
| conv2024_A | 120 | 116 | 2 | 1 | 0 | 0 | 1 | 0 |
| conv2024_B | 120 | 116 | 2 | 1 | 0 | 0 | 1 | 0 |
| conv2024_X | 120 | 110 | 7 | 1 | 0 | 1 | 1 | 0 |
| conv2022 | 120 | 112 | 3 | 3 | 1 | 0 | 1 | 0 |
| conv2020 | 120 | 113 | 3 | 2 | 0 | 2 | 0 | 0 |
| conv2020_X | 120 | 112 | 2 | 2 | 1 | 3 | 0 | 0 |
| **Total** | 960 | 915 | 19 | 12 | 4 | 6 | 4 | 0 |

Distinct questions (modelo B not counted): 720. vigente 681, vigente-con-nota 17, anulada 10, norma modificada 3, función retirada 6, dudosa 3, fuera de temario 0.

Modelo B repeats modelo A in a different order; its rows duplicate modelo A's classification and only the number and key letter change.

## Excluded and noted questions (distinct)

- 2025-P2-6: norma modificada: RDL 1/2013 (TR derechos personas con discapacidad) art. 2.j). La Ley 4/2026 (en vigor 23-10-2026) sustituyó la definición de «inclusión social» que copia el enunciado por «Inclusión: proceso o estado irrenunciable…»; la definición del enunciado ya no está en el texto vigente.
- 2025-P2-13: Anulada en la plantilla definitiva: un insider es una persona de la organización y el incidente puede ser intencionado o accidental, por lo que c y d son defendibles.
- 2024-P1-18: dudosa. Dudosa: la Resolución no está en sources/ ni en normativa.yaml; no se pudo comprobar el plazo de toma de posesión ni si sigue vigente o fue sustituida.
- 2024-P1-23: Anulada. Art. 9: el Gobierno determina el nivel mínimo y su financiación «correrá a cuenta de la Administración General del Estado»; ninguna opción lo dice así.
- 2024-P2-18: vigente-con-nota. Clave oficial discutida: con iPhone, Vínculo móvil permite mensajes y llamadas pero no ver las fotos; la clave solo es exacta para Android. Etiqueta actual: Vínculo móvil (antes «Tu Teléfono»).
- 2024-P2-23: vigente-con-nota. Etiqueta actual: en Windows 11 el Explorador abre en «Inicio», con las secciones Acceso rápido (carpetas ancladas y frecuentes) y Recientes; sin confirmar en la interfaz española.
- 2024X-R1-1: dudosa. Dudosa: la orden que regula el Consejo de Desarrollo Sostenible no está en sources/ ni en normativa.yaml; no se pudo comprobar la composición vigente de su Comisión Permanente.
- 2024X-P2-2: vigente-con-nota. Clave oficial discutida: la c contradice el art. 13.1 («sin que se utilicen siglas o abreviaturas»); la correcta es la d (art. 13.2). Revisado frente al cambio-pendiente (RD 707/2026, desde 02-01-2027): el nuevo art. 13.2 mantiene «se evitará la utilización de fondos con dibujos y tintas que presenten poco contraste»; la d sigue siendo la correcta.
- 2024X-P2-9: vigente-con-nota. Clave oficial discutida: la norma no define el PAG como punto único de acceso a todas las Administraciones y a la UE; el art. 2.1 lo ciñe a la AGE y el 2.3 a información de otras Administraciones mediante convenio. La clave parece seguir la presentación del portal administracion.gob.es, no el texto normativo.
- 2024X-P2-29: vigente-con-nota. Clave oficial discutida: firma y etiqueta no son obligatorias; lo imprescindible es remitente y destinatario, por lo que la d no puede ser la correcta (la c es la más próxima). La plantilla definitiva imprime d en la 29 y a en la 30; las claves de 31 a 33 son correctas, así que no es un desplazamiento de columna. La plantilla podría corresponder a otro modelo del extraordinario. Decisión del coordinador (Juanjo, 2026-11-05): clave oficial discutida en ambas.
- 2024X-P2-30: vigente-con-nota. Clave oficial discutida: la agrupación de direcciones para enviar a todas a la vez es el «Grupo de contactos» (d); «Tabla de envío» no existe. La plantilla definitiva imprime d en la 29 y a en la 30; las claves de 31 a 33 son correctas, así que no es un desplazamiento de columna. La plantilla podría corresponder a otro modelo del extraordinario. Decisión del coordinador (Juanjo, 2026-11-05): clave oficial discutida en ambas.
- 2024X-P2-38: vigente-con-nota. Etiqueta actual: en Windows 11, «Centro de notificaciones» (Windows + N o la fecha y hora de la barra de tareas); «Centro de actividades» es el nombre de Windows 10.
- 2024X-P2-39: función retirada. Visor 3D ya no viene instalado en Windows 11 y Microsoft lo retiró; la pregunta solo tiene una respuesta para Windows 10.
- 2024X-P2-40: vigente-con-nota. Etiqueta actual: en Windows 11 no hay botón «Agregar columnas»; las columnas se añaden con clic derecho en el encabezado, en vista Detalles; sin confirmar en la interfaz española.
- 2024X-P2-42: vigente-con-nota. Etiqueta actual: «Herramientas de Windows» (en Windows 10, «Herramientas administrativas»).
- 2024X-P2-48: Anulada en la plantilla definitiva. La misma pregunta (Apache) sale en 2024-P2-49 con clave válida.
- 2022-P1-12: norma modificada: V Plan de Gobierno Abierto 2025-2029 (suprime los ejes). El «vigente Plan» del examen era el IV Plan (2020-2024), cuyo tercer eje es la integridad. Hoy rige el V Plan 2025-2029, que no tiene ejes: «Con respecto al IV Plan, se suprimen los ejes, que quedan integrados en los compromisos» (content/age-administrativo-c1/sources/otros/transparencia-v-plan.pdf; este curso aún no tiene copia). Resuelto por el coordinador; el clasificador la dejó dudosa.
- 2022-P1-39: vigente-con-nota. Clave oficial discutida: «b» solo da 52 operando de izquierda a derecha; con la prioridad habitual de la multiplicación ninguna opción da 52 (b = −118)
- 2022-R1-5: vigente-con-nota. Clave oficial discutida: 1.105/85 = 13 contrataciones, pero con una contratación cada dos días se llega el día 24 o 26; ninguna opción lo recoge y la clave «el día 13» confunde contrataciones con días
- 2022-P2-13: dudosa. Pregunta de actualidad caducada: Android 14 (octubre de 2023) era la última versión al celebrarse el examen; hoy lo son Android 16 (junio de 2025) o Android 17, según la fecha en que se publique, y ambas figuran entre las opciones. Ninguna norma fija la respuesta; excluida del set.
- 2022-P2-16: vigente-con-nota. Etiqueta actual: en Windows 11 el icono de red de la barra de tareas abre la Configuración rápida; la flecha junto a Wi-Fi muestra las redes disponibles y el botón Conectar. Sin confirmar en la interfaz española.
- 2022-P2-42: Anulada en la plantilla definitiva (motivo no publicado; probablemente porque «Campo de búsqueda» no es un tipo de datos: se crea con el Asistente para búsquedas).
- 2022-P2-43: Anulada en la plantilla definitiva (motivo no publicado; probablemente porque en Access concatenan tanto & como +).
- 2022-R2-3: Anulada en la plantilla definitiva (motivo no publicado; probablemente porque la opción esperada escribe «ICPM» por ICMP).
- 2020-P1-12: Anulada. La opción d reproduce el art. 63.1.e) (Subsecretarios); a) es del Secretario de Estado (art. 62.2.i), b) del Director general (art. 66) y c) del Ministro (art. 61.q).
- 2020-P1-29: vigente-con-nota. Denominación actual: Ministerio de Hacienda (RD 829/2023, art. 1); «Ministerio de Hacienda y Función Pública» era su nombre en la fecha del examen.
- 2020-P1-53: Anulada en la plantilla definitiva (motivo no publicado). La serie 4, 1, 5, 2, 7, _ admite dos lecturas: término par siguiente de 1, 2, … → 3; o la suma siguiente → 10.
- 2020-P1-55: vigente-con-nota. Clave oficial discutida: «Gafa y Ojo» tampoco mantiene la relación continente–contenido (y «Mar y Arena» es dudosa); la respuesta no es única
- 2020-P2-12: vigente-con-nota. Etiqueta actual: en Windows 11 la pestaña «Inicio» del Administrador de tareas es la página «Aplicaciones de arranque» del menú lateral. La pestaña «Planificación» (c) sigue sin existir.
- 2020-P2-17: función retirada. El Reconocimiento de voz de Windows quedó en desuso en 2023 y se retiró a partir de Windows 11 24H2 (lo sustituye Acceso por voz), así que la opción d tampoco es hoy una herramienta de Windows. Igual que C1 conv2020 P1 50.
- 2020-P2-19: función retirada. El Explorador de Windows 11 sustituyó la cinta (Inicio > Organizar > Mover a / Copiar a) por la barra de comandos, que no tiene «Mover a»; se mueve con Cortar y Pegar o arrastrando. Mismo criterio que C1 conv2024_X P1 53.
- 2020X-P1-18: norma modificada: RGPD art. 4.7. La pregunta cita el RD 1720/2007, que desarrolla la LO 15/1999, derogada por la LOPDGDD (disposición derogatoria única.1). En el RGPD la figura es el «responsable del tratamiento» (art. 4.7), que ninguna opción nombra; «responsable del fichero» ya no es la denominación vigente.
- 2020X-P1-39: vigente-con-nota. Clave oficial discutida: «Bandera y Asta» tampoco es continente–contenido (y «Calle y Semáforo» es dudosa); la respuesta no es única Errata: «LIQUIDO» sin tilde
- 2020X-P1-54: Anulada en la plantilla definitiva (motivo no publicado). 45x − 60 = −x da x = 60/46 ≈ 1,304, y ninguna opción coincide.
- 2020X-P2-3: función retirada. En Windows 11 22H2 el Asistente de concentración se sustituyó por «No molestar» (notificaciones) y «Concentración» (sesiones); la pregunta solo se responde para Windows 10. Igual que C1 conv2020_X P1 46.
- 2020X-P2-8: función retirada. Microsoft indica que «Presentar en línea» (Office Presentation Service) ya no está disponible en la mayoría de versiones de Word para Windows; no figura en Word de Microsoft 365. Igual que C1 conv2020_X P1 54.
- 2020X-P2-28: Anulada en la plantilla definitiva (motivo no publicado).
- 2020X-P2-31: función retirada. WordPad se eliminó de Windows 11 a partir de la versión 24H2 (2024); la comparación con el Bloc de notas ya no es posible. Igual que C1 conv2020_X P1 45.
- 2020X-P2-32: vigente-con-nota. Etiqueta actual: el Explorador de Windows 11 no tiene pestaña «Buscar»; al iniciar una búsqueda aparece en la barra de comandos el botón «Opciones de búsqueda». Sin confirmar en la interfaz española.

## conv2025_A — Convocatoria 2025 — ejercicio único, modelo A

- Fecha del examen: 23-05-2026 (del nombre del fichero; el cuestionario no imprime fecha).
- Cuestionario: `sources/examenes-oficiales/2026-05-23_conv2025_modeloA_cuestionario.pdf`. Plantilla definitiva: `sources/examenes-oficiales/2026-05-23_conv2025_modeloA_plantilla-definitiva.pdf`.

### Primera parte

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | I.1 | vigente | a |  | Modelo B: P1 4. |
| 2 | I.1 | vigente | a |  | Modelo B: P1 1. |
| 3 | I.2 | vigente | d |  | Modelo B: P1 2. |
| 4 | I.2 | vigente | d |  | Modelo B: P1 3. |
| 5 | I.3 | vigente | a |  | Modelo B: P1 6. |
| 6 | I.2 | vigente | d |  | Modelo B: P1 5. |
| 7 | I.4 | vigente | a |  | Modelo B: P1 9. |
| 8 | I.5 | vigente | c |  | Modelo B: P1 10. |
| 9 | I.5 (o I.4) | vigente | d |  | Modelo B: P1 7. |
| 10 | I.6 | vigente | c |  | Modelo B: P1 8. La norma que crea la Comisión Delegada del Gobierno para la Agenda 2030 y le atribuye esa función no está en sources/ ni en normativa.yaml: clave no comprobada en texto. |
| 11 | I.7 | vigente | c |  | Modelo B: P1 12. |
| 12 | I.8 | vigente | a |  | Modelo B: P1 14. |
| 13 | I.8 | vigente | c |  | Modelo B: P1 11. |
| 14 | I.9 | vigente | b |  | Modelo B: P1 13. |
| 15 | I.9 | vigente | a |  | Modelo B: P1 16. |
| 16 | I.10 | vigente | a |  | Modelo B: P1 15. |
| 17 | I.10 | vigente | c |  | Modelo B: P1 19. |
| 18 | I.11 | vigente | a |  | Modelo B: P1 17. |
| 19 | I.11 | vigente | c |  | Modelo B: P1 20. |
| 20 | I.11 | vigente | d |  | Modelo B: P1 18. |
| 21 | I.7 | vigente | a |  | Modelo B: P1 23. |
| 22 | I.14 | vigente | b |  | Modelo B: P1 21. |
| 23 | I.13 | vigente | d |  | Modelo B: P1 24. |
| 24 | I.13 | vigente | d |  | Modelo B: P1 22. |
| 25 | I.14 | vigente | c |  | Modelo B: P1 27. |
| 26 | I.14 | vigente | c |  | Modelo B: P1 25. |
| 27 | I.14 | vigente | d |  | Modelo B: P1 26. |
| 28 | I.15 | vigente | b |  | Modelo B: P1 30. |
| 29 | I.15 | vigente | d |  | Modelo B: P1 28. |
| 30 | I.16 | vigente | d |  | Modelo B: P1 29. |
| 31 | psico: verbal-ortografia | vigente | a |  | Modelo B: P1 32. |
| 32 | psico: verbal-ortografia | vigente | c |  | Modelo B: P1 33. |
| 33 | psico: verbal-ortografia | vigente | d |  | Modelo B: P1 31. |
| 34 | psico: verbal-antonimos | vigente | d |  | Modelo B: P1 35. |
| 35 | psico: verbal-antonimos | vigente | b |  | Modelo B: P1 36. |
| 36 | psico: verbal-antonimos | vigente | a |  | Modelo B: P1 34. |
| 37 | psico: verbal-sinonimos | vigente | b |  | Modelo B: P1 39. |
| 38 | psico: verbal-sinonimos | vigente | d |  | Modelo B: P1 37. |
| 39 | psico: verbal-sinonimos | vigente | c |  | Modelo B: P1 38. |
| 40 | psico: calculo-porcentajes | vigente | b |  | Modelo B: P1 41. |
| 41 | psico: calculo-porcentajes | vigente | d |  | Modelo B: P1 42. |
| 42 | psico: calculo-porcentajes | vigente | a |  | Modelo B: P1 40. |
| 43 | psico: calculo-fracciones-proporciones | vigente | b |  | Modelo B: P1 45. |
| 44 | psico: serie-numerica | vigente | a |  | Modelo B: P1 43. |
| 45 | psico: serie-numerica | vigente | d |  | Modelo B: P1 44. |
| 46 | psico: calculo-ecuaciones | vigente | d |  | Modelo B: P1 47. |
| 47 | psico: calculo-ecuaciones | vigente | a |  | Modelo B: P1 48. |
| 48 | psico: calculo-ecuaciones | vigente | b |  | Modelo B: P1 46. |
| 49 | psico: tablas-lectura | vigente | d |  | Modelo B: P1 51. |
| 50 | psico: tablas-lectura | vigente | b |  | Modelo B: P1 49. |
| 51 | psico: tablas-lectura | vigente | c |  | Modelo B: P1 50. |
| 52 | psico: tablas-lectura | vigente | a |  | Modelo B: P1 53. |
| 53 | psico: tablas-lectura | vigente | b |  | Modelo B: P1 52. |
| 54 | psico: tablas-lectura | vigente | a |  | Modelo B: P1 54. |
| 55 | psico: tablas-lectura | vigente | d |  | Modelo B: P1 57. |
| 56 | psico: tablas-lectura | vigente | a |  | Modelo B: P1 58. |
| 57 | psico: tablas-lectura | vigente | d |  | Modelo B: P1 55. |
| 58 | psico: tablas-lectura | vigente | c |  | Modelo B: P1 56. |
| 59 | psico: tablas-lectura | vigente | b |  | Modelo B: P1 60. |
| 60 | psico: tablas-lectura | vigente | c |  | Modelo B: P1 59. |

### Primera parte — preguntas de reserva

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | I.16 | vigente | c |  | Modelo B: R1 1. Revisado frente a la Ley 4/2026 (en vigor 23-10-2026): el art. 95 del texto consolidado de 03-10-2026 mantiene la clave; a), b) y d) son infracciones graves (art. 95.3). |
| 2 | I.10 | vigente | d |  | Modelo B: R1 2. |
| 3 | psico: verbal-ortografia | vigente | b |  | Modelo B: R1 3. |
| 4 | psico: verbal-antonimos | vigente | a |  | Modelo B: R1 4. |
| 5 | psico: calculo-problemas | vigente | b |  | Modelo B: R1 5. |

### Segunda parte

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | II.1 | vigente | d |  | Modelo B: P2 3. |
| 2 | II.1 (o I.2) | vigente | b |  | Modelo B: P2 1. |
| 3 | II.1 (o I.1) | vigente | c |  | Modelo B: P2 2. |
| 4 | II.2 | vigente | a |  | Modelo B: P2 5. |
| 5 | II.2 | vigente | a |  | Modelo B: P2 6. Errata: «Orden Ministeral» en la opción c. |
| 6 | II.1 (o I.16) | norma modificada: RDL 1/2013 (TR derechos personas con discapacidad) art. 2.j) | a |  | Modelo B: P2 4. La Ley 4/2026 (en vigor 23-10-2026) sustituyó la definición de «inclusión social» que copia el enunciado por «Inclusión: proceso o estado irrenunciable…»; la definición del enunciado ya no está en el texto vigente. |
| 7 | II.3 (o I.11) | vigente | d |  | Modelo B: P2 9. |
| 8 | II.4 | vigente | d |  | Modelo B: P2 7. |
| 9 | II.4 | vigente | c |  | Modelo B: P2 8. |
| 10 | II.4 | vigente | d |  | Modelo B: P2 10. |
| 11 | II.5 | vigente | c |  | Modelo B: P2 13. |
| 12 | II.5 | vigente | b |  | Modelo B: P2 11. Norma técnica ISO/IEC 27000 (vocabulario), no normativa del programa. |
| 13 | II.5 | anulada | Anulada |  | Modelo B: P2 12. Anulada en la plantilla definitiva: un insider es una persona de la organización y el incidente puede ser intencionado o accidental, por lo que c y d son defendibles. |
| 14 | II.5 (o II.6) | vigente | c |  | Modelo B: P2 16. |
| 15 | II.5 | vigente | a |  | Modelo B: P2 14. |
| 16 | II.5 | vigente | b |  | Modelo B: P2 15. |
| 17 | II.6 | vigente | c |  | Modelo B: P2 18. |
| 18 | II.7 | vigente | a |  | Modelo B: P2 19. |
| 19 | II.6 | vigente | b |  | Modelo B: P2 17. |
| 20 | II.6 | vigente | a |  | Modelo B: P2 21. |
| 21 | II.6 | vigente | c |  | Modelo B: P2 20. |
| 22 | II.6 | vigente | c |  | Modelo B: P2 22. |
| 23 | II.6 (o II.5) | vigente | d |  | Modelo B: P2 25. |
| 24 | II.7 (o II.5) | vigente | b |  | Modelo B: P2 24. |
| 25 | II.10 | vigente | a |  | Modelo B: P2 23. |
| 26 | II.7 | vigente | b |  | Modelo B: P2 28. |
| 27 | II.7 | vigente | d |  | Modelo B: P2 27. |
| 28 | II.8 | vigente | b |  | Modelo B: P2 26. |
| 29 | II.8 | vigente | b |  | Modelo B: P2 31. |
| 30 | II.8 | vigente | c |  | Modelo B: P2 30. |
| 31 | II.8 | vigente | a |  | Modelo B: P2 29. |
| 32 | II.9 | vigente | d |  | Modelo B: P2 33. |
| 33 | II.9 | vigente | b |  | Modelo B: P2 34. |
| 34 | II.9 | vigente | a |  | Modelo B: P2 32. |
| 35 | II.9 | vigente | c |  | Modelo B: P2 37. |
| 36 | II.9 | vigente | c |  | Modelo B: P2 36. |
| 37 | II.9 | vigente | a |  | Modelo B: P2 35. |
| 38 | II.10 | vigente | a |  | Modelo B: P2 40. |
| 39 | II.10 | vigente | c |  | Modelo B: P2 39. |
| 40 | II.10 | vigente | c |  | Modelo B: P2 38. |
| 41 | II.10 | vigente | a |  | Modelo B: P2 42. |
| 42 | II.10 | vigente | d |  | Modelo B: P2 43. |
| 43 | II.11 | vigente | c |  | Modelo B: P2 41. Clave válida en Outlook clásico. |
| 44 | II.11 | vigente | a |  | Modelo B: P2 45. |
| 45 | II.11 | vigente | b |  | Modelo B: P2 46. |
| 46 | II.11 | vigente | b |  | Modelo B: P2 44. |
| 47 | II.11 | vigente | a |  | Modelo B: P2 49. |
| 48 | II.12 (o II.5) | vigente | b |  | Modelo B: P2 50. |
| 49 | II.12 | vigente | a |  | Modelo B: P2 48. Errata del parse: el ctx «2025 - AUX-L- MODELO A Página 13 de 14» es la cabecera de página, no texto de la pregunta. |
| 50 | II.12 | vigente | d |  | Modelo B: P2 47. |

### Segunda parte — preguntas de reserva

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | II.7 | vigente | d |  | Modelo B: R2 1. |
| 2 | II.9 | vigente | b |  | Modelo B: R2 2. |
| 3 | II.5 (o II.11) | vigente | b |  | Modelo B: R2 3. Microsoft To Do no figura por su nombre en el programa; se asigna a software (II.5), con las tareas de Outlook como alternativa. |
| 4 | II.2 (o I.8) | vigente | b |  | Modelo B: R2 4. |
| 5 | II.2 | vigente | b |  | Modelo B: R2 5. |

## conv2025_B — Convocatoria 2025 — ejercicio único, modelo B

- Fecha del examen: 23-05-2026 (ídem). Repite el modelo A en otro orden; la columna «Nota» da el número del modelo A.
- Cuestionario: `sources/examenes-oficiales/2026-05-23_conv2025_modeloB_cuestionario.pdf`. Plantilla definitiva: `sources/examenes-oficiales/2026-05-23_conv2025_modeloB_plantilla-definitiva.pdf`.

### Primera parte

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | I.1 | vigente | a |  | = modelo A P1 2. |
| 2 | I.2 | vigente | d |  | = modelo A P1 3. |
| 3 | I.2 | vigente | d |  | = modelo A P1 4. |
| 4 | I.1 | vigente | a |  | = modelo A P1 1. |
| 5 | I.2 | vigente | d |  | = modelo A P1 6. |
| 6 | I.3 | vigente | a |  | = modelo A P1 5. |
| 7 | I.5 (o I.4) | vigente | d |  | = modelo A P1 9. |
| 8 | I.6 | vigente | c |  | = modelo A P1 10. La norma que crea la Comisión Delegada del Gobierno para la Agenda 2030 y le atribuye esa función no está en sources/ ni en normativa.yaml: clave no comprobada en texto. |
| 9 | I.4 | vigente | a |  | = modelo A P1 7. |
| 10 | I.5 | vigente | c |  | = modelo A P1 8. |
| 11 | I.8 | vigente | c |  | = modelo A P1 13. |
| 12 | I.7 | vigente | c |  | = modelo A P1 11. |
| 13 | I.9 | vigente | b |  | = modelo A P1 14. |
| 14 | I.8 | vigente | a |  | = modelo A P1 12. |
| 15 | I.10 | vigente | a |  | = modelo A P1 16. |
| 16 | I.9 | vigente | a |  | = modelo A P1 15. |
| 17 | I.11 | vigente | a |  | = modelo A P1 18. |
| 18 | I.11 | vigente | d |  | = modelo A P1 20. |
| 19 | I.10 | vigente | c |  | = modelo A P1 17. |
| 20 | I.11 | vigente | c |  | = modelo A P1 19. |
| 21 | I.14 | vigente | b |  | = modelo A P1 22. |
| 22 | I.13 | vigente | d |  | = modelo A P1 24. |
| 23 | I.7 | vigente | a |  | = modelo A P1 21. |
| 24 | I.13 | vigente | d |  | = modelo A P1 23. |
| 25 | I.14 | vigente | c |  | = modelo A P1 26. |
| 26 | I.14 | vigente | d |  | = modelo A P1 27. |
| 27 | I.14 | vigente | c |  | = modelo A P1 25. |
| 28 | I.15 | vigente | d |  | = modelo A P1 29. |
| 29 | I.16 | vigente | d |  | = modelo A P1 30. |
| 30 | I.15 | vigente | b |  | = modelo A P1 28. |
| 31 | psico: verbal-ortografia | vigente | d |  | = modelo A P1 33. |
| 32 | psico: verbal-ortografia | vigente | a |  | = modelo A P1 31. |
| 33 | psico: verbal-ortografia | vigente | c |  | = modelo A P1 32. |
| 34 | psico: verbal-antonimos | vigente | a |  | = modelo A P1 36. |
| 35 | psico: verbal-antonimos | vigente | d |  | = modelo A P1 34. |
| 36 | psico: verbal-antonimos | vigente | b |  | = modelo A P1 35. |
| 37 | psico: verbal-sinonimos | vigente | d |  | = modelo A P1 38. |
| 38 | psico: verbal-sinonimos | vigente | c |  | = modelo A P1 39. |
| 39 | psico: verbal-sinonimos | vigente | b |  | = modelo A P1 37. |
| 40 | psico: calculo-porcentajes | vigente | a |  | = modelo A P1 42. |
| 41 | psico: calculo-porcentajes | vigente | b |  | = modelo A P1 40. |
| 42 | psico: calculo-porcentajes | vigente | d |  | = modelo A P1 41. |
| 43 | psico: serie-numerica | vigente | a |  | = modelo A P1 44. |
| 44 | psico: serie-numerica | vigente | d |  | = modelo A P1 45. |
| 45 | psico: calculo-fracciones-proporciones | vigente | b |  | = modelo A P1 43. |
| 46 | psico: calculo-ecuaciones | vigente | b |  | = modelo A P1 48. |
| 47 | psico: calculo-ecuaciones | vigente | d |  | = modelo A P1 46. |
| 48 | psico: calculo-ecuaciones | vigente | a |  | = modelo A P1 47. |
| 49 | psico: tablas-lectura | vigente | b |  | = modelo A P1 50. |
| 50 | psico: tablas-lectura | vigente | c |  | = modelo A P1 51. |
| 51 | psico: tablas-lectura | vigente | d |  | = modelo A P1 49. |
| 52 | psico: tablas-lectura | vigente | b |  | = modelo A P1 53. |
| 53 | psico: tablas-lectura | vigente | a |  | = modelo A P1 52. |
| 54 | psico: tablas-lectura | vigente | a |  | = modelo A P1 54. |
| 55 | psico: tablas-lectura | vigente | d |  | = modelo A P1 57. |
| 56 | psico: tablas-lectura | vigente | c |  | = modelo A P1 58. |
| 57 | psico: tablas-lectura | vigente | d |  | = modelo A P1 55. |
| 58 | psico: tablas-lectura | vigente | a |  | = modelo A P1 56. |
| 59 | psico: tablas-lectura | vigente | c |  | = modelo A P1 60. |
| 60 | psico: tablas-lectura | vigente | b |  | = modelo A P1 59. |

### Primera parte — preguntas de reserva

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | I.16 | vigente | c |  | = modelo A R1 1. Revisado frente a la Ley 4/2026 (en vigor 23-10-2026): el art. 95 del texto consolidado de 03-10-2026 mantiene la clave; a), b) y d) son infracciones graves (art. 95.3). |
| 2 | I.10 | vigente | d |  | = modelo A R1 2. |
| 3 | psico: verbal-ortografia | vigente | b |  | = modelo A R1 3. |
| 4 | psico: verbal-antonimos | vigente | a |  | = modelo A R1 4. |
| 5 | psico: calculo-problemas | vigente | b |  | = modelo A R1 5. |

### Segunda parte

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | II.1 (o I.2) | vigente | b |  | = modelo A P2 2. |
| 2 | II.1 (o I.1) | vigente | c |  | = modelo A P2 3. |
| 3 | II.1 | vigente | d |  | = modelo A P2 1. |
| 4 | II.1 (o I.16) | norma modificada: RDL 1/2013 (TR derechos personas con discapacidad) art. 2.j) | a |  | = modelo A P2 6. La Ley 4/2026 (en vigor 23-10-2026) sustituyó la definición de «inclusión social» que copia el enunciado por «Inclusión: proceso o estado irrenunciable…»; la definición del enunciado ya no está en el texto vigente. |
| 5 | II.2 | vigente | a |  | = modelo A P2 4. |
| 6 | II.2 | vigente | a |  | = modelo A P2 5. Errata: «Orden Ministeral» en la opción c. |
| 7 | II.4 | vigente | d |  | = modelo A P2 8. |
| 8 | II.4 | vigente | c |  | = modelo A P2 9. |
| 9 | II.3 (o I.11) | vigente | d |  | = modelo A P2 7. |
| 10 | II.4 | vigente | d |  | = modelo A P2 10. |
| 11 | II.5 | vigente | b |  | = modelo A P2 12. Norma técnica ISO/IEC 27000 (vocabulario), no normativa del programa. |
| 12 | II.5 | anulada | Anulada |  | = modelo A P2 13. Anulada en la plantilla definitiva: un insider es una persona de la organización y el incidente puede ser intencionado o accidental, por lo que c y d son defendibles. |
| 13 | II.5 | vigente | c |  | = modelo A P2 11. |
| 14 | II.5 | vigente | a |  | = modelo A P2 15. |
| 15 | II.5 | vigente | b |  | = modelo A P2 16. |
| 16 | II.5 (o II.6) | vigente | c |  | = modelo A P2 14. |
| 17 | II.6 | vigente | b |  | = modelo A P2 19. |
| 18 | II.6 | vigente | c |  | = modelo A P2 17. |
| 19 | II.7 | vigente | a |  | = modelo A P2 18. |
| 20 | II.6 | vigente | c |  | = modelo A P2 21. |
| 21 | II.6 | vigente | a |  | = modelo A P2 20. |
| 22 | II.6 | vigente | c |  | = modelo A P2 22. |
| 23 | II.10 | vigente | a |  | = modelo A P2 25. |
| 24 | II.7 (o II.5) | vigente | b |  | = modelo A P2 24. |
| 25 | II.6 (o II.5) | vigente | d |  | = modelo A P2 23. |
| 26 | II.8 | vigente | b |  | = modelo A P2 28. |
| 27 | II.7 | vigente | d |  | = modelo A P2 27. |
| 28 | II.7 | vigente | b |  | = modelo A P2 26. |
| 29 | II.8 | vigente | a |  | = modelo A P2 31. |
| 30 | II.8 | vigente | c |  | = modelo A P2 30. |
| 31 | II.8 | vigente | b |  | = modelo A P2 29. |
| 32 | II.9 | vigente | a |  | = modelo A P2 34. |
| 33 | II.9 | vigente | d |  | = modelo A P2 32. |
| 34 | II.9 | vigente | b |  | = modelo A P2 33. |
| 35 | II.9 | vigente | a |  | = modelo A P2 37. |
| 36 | II.9 | vigente | c |  | = modelo A P2 36. |
| 37 | II.9 | vigente | c |  | = modelo A P2 35. |
| 38 | II.10 | vigente | c |  | = modelo A P2 40. |
| 39 | II.10 | vigente | c |  | = modelo A P2 39. |
| 40 | II.10 | vigente | a |  | = modelo A P2 38. |
| 41 | II.11 | vigente | c |  | = modelo A P2 43. Clave válida en Outlook clásico. |
| 42 | II.10 | vigente | a |  | = modelo A P2 41. |
| 43 | II.10 | vigente | d |  | = modelo A P2 42. |
| 44 | II.11 | vigente | b |  | = modelo A P2 46. |
| 45 | II.11 | vigente | a |  | = modelo A P2 44. |
| 46 | II.11 | vigente | b |  | = modelo A P2 45. |
| 47 | II.12 | vigente | d |  | = modelo A P2 50. |
| 48 | II.12 | vigente | a |  | = modelo A P2 49. Errata del parse: el ctx «2025 - AUX-L- MODELO A Página 13 de 14» es la cabecera de página, no texto de la pregunta. |
| 49 | II.11 | vigente | a |  | = modelo A P2 47. |
| 50 | II.12 (o II.5) | vigente | b |  | = modelo A P2 48. |

### Segunda parte — preguntas de reserva

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | II.7 | vigente | d |  | = modelo A R2 1. |
| 2 | II.9 | vigente | b |  | = modelo A R2 2. |
| 3 | II.5 (o II.11) | vigente | b |  | = modelo A R2 3. Microsoft To Do no figura por su nombre en el programa; se asigna a software (II.5), con las tareas de Outlook como alternativa. |
| 4 | II.2 (o I.8) | vigente | b |  | = modelo A R2 4. |
| 5 | II.2 | vigente | b |  | = modelo A R2 5. |

## conv2024_A — Convocatoria 2024 (OEP 2023-2024) — ejercicio único, modelo A

- Fecha del examen: no impresa; PDF creado el 07-11-2024.
- Cuestionario: `sources/examenes-oficiales/conv2024_modeloA_cuestionario.pdf`. Plantilla definitiva: `sources/examenes-oficiales/conv2024_modeloA_plantilla-definitiva.pdf`.

### Primera parte

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | I.1 | vigente | a |  | Modelo B: P1 1. |
| 2 | I.2 | vigente | b |  | Modelo B: P1 3. |
| 3 | I.3 | vigente | d |  | Modelo B: P1 6. |
| 4 | I.1 | vigente | c |  | Modelo B: P1 4. |
| 5 | I.5 | vigente | d |  | Modelo B: P1 2. |
| 6 | I.2 | vigente | c |  | Modelo B: P1 5. |
| 7 | I.5 | vigente | d |  | Modelo B: P1 7. |
| 8 | I.7 | vigente | a |  | Modelo B: P1 8. |
| 9 | I.6 | vigente | c |  | Modelo B: P1 10. Revisado: el enunciado fija el IV Plan (2020-2024), ya terminado; el V Plan de Gobierno Abierto 2025-2029 se aprobó el 6-10-2025. La clave vale para el IV Plan. El plan no está en sources/. |
| 10 | I.4 | vigente | b |  | Modelo B: P1 9. |
| 11 | I.8 (o I.11) | vigente | d |  | Modelo B: P1 11. |
| 12 | I.8 | vigente | a |  | Modelo B: P1 12. |
| 13 | I.9 | vigente | a |  | Modelo B: P1 13. |
| 14 | I.10 | vigente | d |  | Modelo B: P1 14. |
| 15 | I.8 | vigente | c |  | Modelo B: P1 16. |
| 16 | I.8 | vigente | c |  | Modelo B: P1 18. |
| 17 | I.11 | vigente | a |  | Modelo B: P1 17. |
| 18 | I.13 | dudosa | a |  | Modelo B: P1 15. Dudosa: la Resolución no está en sources/ ni en normativa.yaml; no se pudo comprobar el plazo de toma de posesión ni si sigue vigente o fue sustituida. |
| 19 | I.11 | vigente | b |  | Modelo B: P1 19. |
| 20 | I.14 | vigente | a |  | Modelo B: P1 21. |
| 21 | I.8 | vigente | a |  | Modelo B: P1 22. |
| 22 | I.11 | vigente | d |  | Modelo B: P1 20. |
| 23 | I.16 | anulada | Anulada |  | Modelo B: P1 24. Anulada. Art. 9: el Gobierno determina el nivel mínimo y su financiación «correrá a cuenta de la Administración General del Estado»; ninguna opción lo dice así. |
| 24 | I.15 (o I.8) | vigente | d |  | Modelo B: P1 23. |
| 25 | I.15 | vigente | d |  | Modelo B: P1 25. |
| 26 | I.16 | vigente | d |  | Modelo B: P1 28. |
| 27 | I.16 | vigente | b |  | Modelo B: P1 26. |
| 28 | I.14 | vigente | c |  | Modelo B: P1 27. |
| 29 | I.13 | vigente | d |  | Modelo B: P1 30. |
| 30 | I.14 (o I.13) | vigente | a |  | Modelo B: P1 29. La Resolución citada no está en sources/ (no localizada en boe.es): clave no comprobada en su texto. La disposición transitoria sexta del RDL 6/2023, a la que la Resolución se adecua, da el mismo intervalo. |
| 31 | psico: verbal-sinonimos | vigente | b |  | Modelo B: P1 32. |
| 32 | psico: verbal-antonimos | vigente | a |  | Modelo B: P1 33. |
| 33 | psico: verbal-antonimos | vigente | d |  | Modelo B: P1 31. |
| 34 | psico: verbal-sinonimos | vigente | a |  | Modelo B: P1 34. |
| 35 | psico: verbal-antonimos | vigente | c |  | Modelo B: P1 35. |
| 36 | psico: verbal-ortografia | vigente | a |  | Modelo B: P1 37. |
| 37 | psico: verbal-sinonimos | vigente | b |  | Modelo B: P1 36. |
| 38 | psico: atencion-codificacion | vigente | b |  | Modelo B: P1 39. |
| 39 | psico: verbal-ortografia | vigente | a |  | Modelo B: P1 40. |
| 40 | psico: calculo-porcentajes | vigente | d |  | Modelo B: P1 38. |
| 41 | psico: verbal-ortografia | vigente | c |  | Modelo B: P1 42. |
| 42 | psico: atencion-codificacion | vigente | a |  | Modelo B: P1 44. |
| 43 | psico: atencion-codificacion | vigente | c |  | Modelo B: P1 41. |
| 44 | psico: calculo-porcentajes | vigente | c |  | Modelo B: P1 43. |
| 45 | psico: serie-numerica | vigente | d |  | Modelo B: P1 46. |
| 46 | psico: serie-numerica | vigente | c |  | Modelo B: P1 45. |
| 47 | psico: calculo-porcentajes | vigente | c |  | Modelo B: P1 47. |
| 48 | psico: serie-numerica | vigente | d |  | Modelo B: P1 48. |
| 49 | psico: administrativo-clasificacion | vigente | d |  | Modelo B: P1 49. |
| 50 | psico: administrativo-clasificacion | vigente | b |  | Modelo B: P1 50. |
| 51 | psico: tablas-lectura | vigente | b |  | Modelo B: P1 51. |
| 52 | psico: tablas-lectura | vigente | c |  | Modelo B: P1 53. |
| 53 | psico: administrativo-clasificacion | vigente | c |  | Modelo B: P1 52. |
| 54 | psico: administrativo-clasificacion | vigente | a |  | Modelo B: P1 54. |
| 55 | psico: tablas-lectura | vigente | b |  | Modelo B: P1 55. Tabla «Cuadro Laboratorios» transcrita de la imagen (véase la transcripción al final). |
| 56 | psico: tablas-lectura | vigente | a |  | Modelo B: P1 58. Tabla «Cuadro Laboratorios» transcrita de la imagen (véase la transcripción al final). |
| 57 | psico: tablas-lectura | vigente | b |  | Modelo B: P1 56. Tabla «Cuadro Laboratorios» transcrita de la imagen (véase la transcripción al final). |
| 58 | psico: tablas-lectura | vigente | d |  | Modelo B: P1 60. Tabla «Cuadro Laboratorios» transcrita de la imagen (véase la transcripción al final). |
| 59 | psico: tablas-lectura | vigente | a |  | Modelo B: P1 57. Tabla «Cuadro Laboratorios» transcrita de la imagen (véase la transcripción al final). |
| 60 | psico: tablas-lectura | vigente | c |  | Modelo B: P1 59. Tabla «Cuadro Laboratorios» transcrita de la imagen (véase la transcripción al final). |

### Primera parte — preguntas de reserva

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | I.5 | vigente | a |  | Modelo B: R1 1. |
| 2 | I.12 | vigente | a |  | Modelo B: R1 2. |
| 3 | psico: verbal-antonimos | vigente | d |  | Modelo B: R1 3. |
| 4 | psico: calculo-porcentajes | vigente | d |  | Modelo B: R1 4. |
| 5 | psico: calculo-ecuaciones | vigente | b |  | Modelo B: R1 5. Errata: enunciado «Halle el valor de 21(4x – 6) = x» sin «x en» |

### Segunda parte

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | II.1 | vigente | a |  | Modelo B: P2 1. |
| 2 | II.2 | vigente | b |  | Modelo B: P2 3. |
| 3 | II.1 | vigente | d |  | Modelo B: P2 2. La Ley 51/2003 que cita el enunciado (y el propio art. 2) está derogada por el RDL 1/2013; el art. 2 conserva la remisión. |
| 4 | II.4 | vigente | b |  | Modelo B: P2 5. El enunciado dice «creación y supresión»; el art. 6.1 exige el informe solo para la creación. |
| 5 | II.1 | vigente | d |  | Modelo B: P2 4. |
| 6 | II.2 | vigente | c |  | Modelo B: P2 6. El enunciado copia el art. 9.1, que aún nombra los «Gobiernos Civiles» (hoy Subdelegaciones del Gobierno). |
| 7 | II.3 | vigente | d |  | Modelo B: P2 8. |
| 8 | II.3 | vigente | d |  | Modelo B: P2 9. |
| 9 | II.3 | vigente | a |  | Modelo B: P2 7. |
| 10 | II.4 | vigente | b |  | Modelo B: P2 10. |
| 11 | II.4 (o II.5) | vigente | a |  | Modelo B: P2 13. |
| 12 | II.5 | vigente | a |  | Modelo B: P2 11. |
| 13 | II.6 | vigente | b |  | Modelo B: P2 12. |
| 14 | II.5 | vigente | d |  | Modelo B: P2 17. |
| 15 | II.5 | vigente | d |  | Modelo B: P2 16. |
| 16 | II.6 | vigente | a |  | Modelo B: P2 14. |
| 17 | II.5 | vigente | c |  | Modelo B: P2 15. |
| 18 | II.6 | vigente-con-nota | c | Clave oficial discutida: con iPhone, Vínculo móvil permite mensajes y llamadas pero no ver las fotos; la clave solo es exacta para Android. | Modelo B: P2 18. Etiqueta actual: Vínculo móvil (antes «Tu Teléfono»). |
| 19 | II.7 | vigente | b |  | Modelo B: P2 19. |
| 20 | II.7 | vigente | d |  | Modelo B: P2 22. |
| 21 | II.7 (o II.6) | vigente | d |  | Modelo B: P2 20. |
| 22 | II.7 (o II.6) | vigente | d |  | Modelo B: P2 21. |
| 23 | II.7 | vigente-con-nota | b |  | Modelo B: P2 23. Etiqueta actual: en Windows 11 el Explorador abre en «Inicio», con las secciones Acceso rápido (carpetas ancladas y frecuentes) y Recientes; sin confirmar en la interfaz española. |
| 24 | II.9 | vigente | a |  | Modelo B: P2 24. |
| 25 | II.7 | vigente | a |  | Modelo B: P2 26. La opción a abrevia «Historial de archivos». |
| 26 | II.7 | vigente | d |  | Modelo B: P2 25. |
| 27 | II.8 | vigente | c |  | Modelo B: P2 28. La página guardada ms-word-atajos.html da las teclas del teclado estadounidense; con teclado español, Ctrl+< reduce el tamaño de fuente. |
| 28 | II.8 | vigente | b |  | Modelo B: P2 30. |
| 29 | II.8 | vigente | d |  | Modelo B: P2 27. |
| 30 | II.8 | vigente | a |  | Modelo B: P2 32. |
| 31 | II.8 | vigente | b |  | Modelo B: P2 29. |
| 32 | II.9 | vigente | b |  | Modelo B: P2 31. |
| 33 | II.9 | vigente | c |  | Modelo B: P2 34. Excel ofrece además «Imprimir tabla seleccionada» cuando la celda activa está en una tabla; no es una de las opciones. |
| 34 | II.9 | vigente | d |  | Modelo B: P2 36. |
| 35 | II.9 | vigente | d |  | Modelo B: P2 33. |
| 36 | II.10 | vigente | b |  | Modelo B: P2 37. |
| 37 | II.11 | vigente | b |  | Modelo B: P2 35. |
| 38 | II.10 | vigente | b |  | Modelo B: P2 40. |
| 39 | II.10 | vigente | c |  | Modelo B: P2 39. |
| 40 | II.10 | vigente | d |  | Modelo B: P2 42. |
| 41 | II.11 | vigente | c |  | Modelo B: P2 38. Clave válida en Outlook clásico. |
| 42 | II.10 | vigente | a |  | Modelo B: P2 41. |
| 43 | II.12 | vigente | d |  | Modelo B: P2 45. |
| 44 | II.11 | vigente | c |  | Modelo B: P2 44. Clave válida en Outlook clásico (ámbito «Buzón actual»). |
| 45 | II.11 | vigente | c |  | Modelo B: P2 43. Clave válida en Outlook clásico. |
| 46 | II.12 (o II.5) | vigente | a |  | Modelo B: P2 46. |
| 47 | II.5 (o II.12) | vigente | c |  | Modelo B: P2 48. |
| 48 | II.6 | vigente | d |  | Modelo B: P2 50. |
| 49 | II.12 | vigente | a |  | Modelo B: P2 49. |
| 50 | II.12 (o II.4) | vigente | c |  | Modelo B: P2 47. |

### Segunda parte — preguntas de reserva

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | II.4 | vigente | a |  | Modelo B: R2 1. Enunciado impreciso: 2002 es el año de la Ley 34/2002 (LSSI), que impuso la accesibilidad a los sitios web públicos; la Directiva (UE) 2016/2102 y el RD 1112/2018 son posteriores. |
| 2 | II.9 | vigente | a |  | Modelo B: R2 2. |
| 3 | II.7 | vigente | d |  | Modelo B: R2 3. |
| 4 | II.9 | vigente | a |  | Modelo B: R2 4. |
| 5 | II.4 | vigente | a |  | Modelo B: R2 5. |

## conv2024_B — Convocatoria 2024 (OEP 2023-2024) — ejercicio único, modelo B

- Fecha del examen: la del modelo A. Repite el modelo A en otro orden.
- Cuestionario: `sources/examenes-oficiales/conv2024_modeloB_cuestionario.pdf`. Plantilla definitiva: `sources/examenes-oficiales/conv2024_modeloB_plantilla-definitiva.pdf`.

### Primera parte

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | I.1 | vigente | a |  | = modelo A P1 1. |
| 2 | I.5 | vigente | d |  | = modelo A P1 5. |
| 3 | I.2 | vigente | b |  | = modelo A P1 2. |
| 4 | I.1 | vigente | c |  | = modelo A P1 4. |
| 5 | I.2 | vigente | c |  | = modelo A P1 6. |
| 6 | I.3 | vigente | d |  | = modelo A P1 3. |
| 7 | I.5 | vigente | d |  | = modelo A P1 7. |
| 8 | I.7 | vigente | a |  | = modelo A P1 8. |
| 9 | I.4 | vigente | b |  | = modelo A P1 10. |
| 10 | I.6 | vigente | c |  | = modelo A P1 9. Revisado: el enunciado fija el IV Plan (2020-2024), ya terminado; el V Plan de Gobierno Abierto 2025-2029 se aprobó el 6-10-2025. La clave vale para el IV Plan. El plan no está en sources/. |
| 11 | I.8 (o I.11) | vigente | d |  | = modelo A P1 11. |
| 12 | I.8 | vigente | a |  | = modelo A P1 12. |
| 13 | I.9 | vigente | a |  | = modelo A P1 13. |
| 14 | I.10 | vigente | d |  | = modelo A P1 14. |
| 15 | I.13 | dudosa | a |  | = modelo A P1 18. Dudosa: la Resolución no está en sources/ ni en normativa.yaml; no se pudo comprobar el plazo de toma de posesión ni si sigue vigente o fue sustituida. |
| 16 | I.8 | vigente | c |  | = modelo A P1 15. |
| 17 | I.11 | vigente | a |  | = modelo A P1 17. |
| 18 | I.8 | vigente | c |  | = modelo A P1 16. |
| 19 | I.11 | vigente | b |  | = modelo A P1 19. |
| 20 | I.11 | vigente | d |  | = modelo A P1 22. |
| 21 | I.14 | vigente | a |  | = modelo A P1 20. |
| 22 | I.8 | vigente | a |  | = modelo A P1 21. |
| 23 | I.15 (o I.8) | vigente | d |  | = modelo A P1 24. |
| 24 | I.16 | anulada | Anulada |  | = modelo A P1 23. Anulada. Art. 9: el Gobierno determina el nivel mínimo y su financiación «correrá a cuenta de la Administración General del Estado»; ninguna opción lo dice así. |
| 25 | I.15 | vigente | d |  | = modelo A P1 25. |
| 26 | I.16 | vigente | b |  | = modelo A P1 27. |
| 27 | I.14 | vigente | c |  | = modelo A P1 28. |
| 28 | I.16 | vigente | d |  | = modelo A P1 26. |
| 29 | I.14 (o I.13) | vigente | a |  | = modelo A P1 30. La Resolución citada no está en sources/ (no localizada en boe.es): clave no comprobada en su texto. La disposición transitoria sexta del RDL 6/2023, a la que la Resolución se adecua, da el mismo intervalo. |
| 30 | I.13 | vigente | d |  | = modelo A P1 29. |
| 31 | psico: verbal-antonimos | vigente | d |  | = modelo A P1 33. |
| 32 | psico: verbal-sinonimos | vigente | b |  | = modelo A P1 31. |
| 33 | psico: verbal-antonimos | vigente | a |  | = modelo A P1 32. |
| 34 | psico: verbal-sinonimos | vigente | a |  | = modelo A P1 34. |
| 35 | psico: verbal-antonimos | vigente | c |  | = modelo A P1 35. |
| 36 | psico: verbal-sinonimos | vigente | b |  | = modelo A P1 37. |
| 37 | psico: verbal-ortografia | vigente | a |  | = modelo A P1 36. |
| 38 | psico: calculo-porcentajes | vigente | d |  | = modelo A P1 40. |
| 39 | psico: atencion-codificacion | vigente | b |  | = modelo A P1 38. |
| 40 | psico: verbal-ortografia | vigente | a |  | = modelo A P1 39. |
| 41 | psico: atencion-codificacion | vigente | c |  | = modelo A P1 43. |
| 42 | psico: verbal-ortografia | vigente | c |  | = modelo A P1 41. |
| 43 | psico: calculo-porcentajes | vigente | c |  | = modelo A P1 44. |
| 44 | psico: atencion-codificacion | vigente | a |  | = modelo A P1 42. |
| 45 | psico: serie-numerica | vigente | c |  | = modelo A P1 46. |
| 46 | psico: serie-numerica | vigente | d |  | = modelo A P1 45. |
| 47 | psico: calculo-porcentajes | vigente | c |  | = modelo A P1 47. |
| 48 | psico: serie-numerica | vigente | d |  | = modelo A P1 48. |
| 49 | psico: administrativo-clasificacion | vigente | d |  | = modelo A P1 49. |
| 50 | psico: administrativo-clasificacion | vigente | b |  | = modelo A P1 50. |
| 51 | psico: tablas-lectura | vigente | b |  | = modelo A P1 51. |
| 52 | psico: administrativo-clasificacion | vigente | c |  | = modelo A P1 53. |
| 53 | psico: tablas-lectura | vigente | c |  | = modelo A P1 52. |
| 54 | psico: administrativo-clasificacion | vigente | a |  | = modelo A P1 54. |
| 55 | psico: tablas-lectura | vigente | b |  | = modelo A P1 55. Tabla «Cuadro Laboratorios» transcrita de la imagen (véase la transcripción al final). |
| 56 | psico: tablas-lectura | vigente | b |  | = modelo A P1 57. Tabla «Cuadro Laboratorios» transcrita de la imagen (véase la transcripción al final). |
| 57 | psico: tablas-lectura | vigente | a |  | = modelo A P1 59. Tabla «Cuadro Laboratorios» transcrita de la imagen (véase la transcripción al final). |
| 58 | psico: tablas-lectura | vigente | a |  | = modelo A P1 56. Tabla «Cuadro Laboratorios» transcrita de la imagen (véase la transcripción al final). |
| 59 | psico: tablas-lectura | vigente | c |  | = modelo A P1 60. Tabla «Cuadro Laboratorios» transcrita de la imagen (véase la transcripción al final). |
| 60 | psico: tablas-lectura | vigente | d |  | = modelo A P1 58. Tabla «Cuadro Laboratorios» transcrita de la imagen (véase la transcripción al final). |

### Primera parte — preguntas de reserva

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | I.5 | vigente | a |  | = modelo A R1 1. |
| 2 | I.12 | vigente | a |  | = modelo A R1 2. |
| 3 | psico: verbal-antonimos | vigente | d |  | = modelo A R1 3. |
| 4 | psico: calculo-porcentajes | vigente | d |  | = modelo A R1 4. |
| 5 | psico: calculo-ecuaciones | vigente | b |  | = modelo A R1 5. Errata: enunciado «Halle el valor de 21(4x – 6) = x» sin «x en» |

### Segunda parte

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | II.1 | vigente | a |  | = modelo A P2 1. |
| 2 | II.1 | vigente | d |  | = modelo A P2 3. La Ley 51/2003 que cita el enunciado (y el propio art. 2) está derogada por el RDL 1/2013; el art. 2 conserva la remisión. |
| 3 | II.2 | vigente | b |  | = modelo A P2 2. |
| 4 | II.1 | vigente | d |  | = modelo A P2 5. |
| 5 | II.4 | vigente | b |  | = modelo A P2 4. El enunciado dice «creación y supresión»; el art. 6.1 exige el informe solo para la creación. |
| 6 | II.2 | vigente | c |  | = modelo A P2 6. El enunciado copia el art. 9.1, que aún nombra los «Gobiernos Civiles» (hoy Subdelegaciones del Gobierno). |
| 7 | II.3 | vigente | a |  | = modelo A P2 9. |
| 8 | II.3 | vigente | d |  | = modelo A P2 7. |
| 9 | II.3 | vigente | d |  | = modelo A P2 8. |
| 10 | II.4 | vigente | b |  | = modelo A P2 10. |
| 11 | II.5 | vigente | a |  | = modelo A P2 12. |
| 12 | II.6 | vigente | b |  | = modelo A P2 13. |
| 13 | II.4 (o II.5) | vigente | a |  | = modelo A P2 11. |
| 14 | II.6 | vigente | a |  | = modelo A P2 16. |
| 15 | II.5 | vigente | c |  | = modelo A P2 17. |
| 16 | II.5 | vigente | d |  | = modelo A P2 15. |
| 17 | II.5 | vigente | d |  | = modelo A P2 14. |
| 18 | II.6 | vigente-con-nota | c | Clave oficial discutida: con iPhone, Vínculo móvil permite mensajes y llamadas pero no ver las fotos; la clave solo es exacta para Android. | = modelo A P2 18. Etiqueta actual: Vínculo móvil (antes «Tu Teléfono»). |
| 19 | II.7 | vigente | b |  | = modelo A P2 19. |
| 20 | II.7 (o II.6) | vigente | d |  | = modelo A P2 21. |
| 21 | II.7 (o II.6) | vigente | d |  | = modelo A P2 22. |
| 22 | II.7 | vigente | d |  | = modelo A P2 20. |
| 23 | II.7 | vigente-con-nota | b |  | = modelo A P2 23. Etiqueta actual: en Windows 11 el Explorador abre en «Inicio», con las secciones Acceso rápido (carpetas ancladas y frecuentes) y Recientes; sin confirmar en la interfaz española. |
| 24 | II.9 | vigente | a |  | = modelo A P2 24. |
| 25 | II.7 | vigente | d |  | = modelo A P2 26. |
| 26 | II.7 | vigente | a |  | = modelo A P2 25. La opción a abrevia «Historial de archivos». |
| 27 | II.8 | vigente | d |  | = modelo A P2 29. |
| 28 | II.8 | vigente | c |  | = modelo A P2 27. La página guardada ms-word-atajos.html da las teclas del teclado estadounidense; con teclado español, Ctrl+< reduce el tamaño de fuente. |
| 29 | II.8 | vigente | b |  | = modelo A P2 31. |
| 30 | II.8 | vigente | b |  | = modelo A P2 28. |
| 31 | II.9 | vigente | b |  | = modelo A P2 32. |
| 32 | II.8 | vigente | a |  | = modelo A P2 30. |
| 33 | II.9 | vigente | d |  | = modelo A P2 35. |
| 34 | II.9 | vigente | c |  | = modelo A P2 33. Excel ofrece además «Imprimir tabla seleccionada» cuando la celda activa está en una tabla; no es una de las opciones. |
| 35 | II.11 | vigente | b |  | = modelo A P2 37. |
| 36 | II.9 | vigente | d |  | = modelo A P2 34. |
| 37 | II.10 | vigente | b |  | = modelo A P2 36. |
| 38 | II.11 | vigente | c |  | = modelo A P2 41. Clave válida en Outlook clásico. |
| 39 | II.10 | vigente | c |  | = modelo A P2 39. |
| 40 | II.10 | vigente | b |  | = modelo A P2 38. |
| 41 | II.10 | vigente | a |  | = modelo A P2 42. |
| 42 | II.10 | vigente | d |  | = modelo A P2 40. |
| 43 | II.11 | vigente | c |  | = modelo A P2 45. Clave válida en Outlook clásico. |
| 44 | II.11 | vigente | c |  | = modelo A P2 44. Clave válida en Outlook clásico (ámbito «Buzón actual»). |
| 45 | II.12 | vigente | d |  | = modelo A P2 43. |
| 46 | II.12 (o II.5) | vigente | a |  | = modelo A P2 46. |
| 47 | II.12 (o II.4) | vigente | c |  | = modelo A P2 50. |
| 48 | II.5 (o II.12) | vigente | c |  | = modelo A P2 47. |
| 49 | II.12 | vigente | a |  | = modelo A P2 49. |
| 50 | II.6 | vigente | d |  | = modelo A P2 48. |

### Segunda parte — preguntas de reserva

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | II.4 | vigente | a |  | = modelo A R2 1. Enunciado impreciso: 2002 es el año de la Ley 34/2002 (LSSI), que impuso la accesibilidad a los sitios web públicos; la Directiva (UE) 2016/2102 y el RD 1112/2018 son posteriores. |
| 2 | II.9 | vigente | a |  | = modelo A R2 2. |
| 3 | II.7 | vigente | d |  | = modelo A R2 3. |
| 4 | II.9 | vigente | a |  | = modelo A R2 4. |
| 5 | II.4 | vigente | a |  | = modelo A R2 5. |

## conv2024_X — Convocatoria 2024 — llamamiento extraordinario

- Fecha del examen: no impresa; PDF creado el 10-02-2025. Misprint: segunda parte, «39.¿Cuál…» sin espacio.
- Cuestionario: `sources/examenes-oficiales/conv2024_extraordinario_cuestionario.pdf`. Plantilla definitiva: `sources/examenes-oficiales/conv2024_extraordinario_plantilla-definitiva.pdf`.

### Primera parte

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | I.2 | vigente | a |  |  |
| 2 | I.1 | vigente | c |  | Errata: la opción clave dice «lpublicidad» por «publicidad». |
| 3 | I.4 | vigente | d |  |  |
| 4 | I.4 | vigente | c |  |  |
| 5 | I.4 | vigente | b |  |  |
| 6 | I.2 | vigente | d |  |  |
| 7 | I.3 | vigente | c |  |  |
| 8 | I.3 | vigente | a |  |  |
| 9 | I.5 | vigente | b |  |  |
| 10 | I.5 | vigente | a |  |  |
| 11 | I.7 | vigente | c |  |  |
| 12 | I.7 | vigente | d |  |  |
| 13 | I.16 | vigente | a |  |  |
| 14 | I.6 | vigente | d |  |  |
| 15 | I.8 | vigente | c |  |  |
| 16 | I.8 | vigente | a |  |  |
| 17 | I.11 | vigente | c |  | Errata: el enunciado cita el art. 63; la definición de denuncia está en el art. 62.1. |
| 18 | I.10 | vigente | a |  | Pregunta fechada («a partir del 1 de enero de 2025»): la clave sigue siendo correcta para ese trío; la Decisión no está en sources/. |
| 19 | I.10 | vigente | b |  |  |
| 20 | I.11 | vigente | c |  |  |
| 21 | I.11 | vigente | d |  |  |
| 22 | I.11 | vigente | c |  |  |
| 23 | I.11 | vigente | c |  |  |
| 24 | I.9 | vigente | a |  |  |
| 25 | I.13 | vigente | a |  |  |
| 26 | I.13 | vigente | b |  |  |
| 27 | I.14 | vigente | c |  |  |
| 28 | I.16 | vigente | b |  |  |
| 29 | I.15 | vigente | c |  |  |
| 30 | I.13 | vigente | c |  |  |
| 31 | psico: calculo-ecuaciones | vigente | b |  |  |
| 32 | psico: calculo-porcentajes | vigente | c |  | Errata: «mayores de 4 años» por «de 4 años o más» (el complementario de «menores de 4»); no cambia la clave |
| 33 | psico: serie-numerica | vigente | d |  |  |
| 34 | psico: calculo-problemas | vigente | d |  |  |
| 35 | psico: calculo-problemas | vigente | d |  |  |
| 36 | psico: calculo-ecuaciones | vigente | b |  |  |
| 37 | psico: atencion-codificacion | vigente | c |  |  |
| 38 | psico: calculo-problemas | vigente | d |  |  |
| 39 | psico: calculo-problemas | vigente | b |  |  |
| 40 | psico: verbal-sinonimos | vigente | d |  |  |
| 41 | psico: verbal-antonimos | vigente | b |  |  |
| 42 | psico: verbal-definicion | vigente | a |  |  |
| 43 | psico: verbal-definicion | vigente | b |  |  |
| 44 | psico: verbal-sinonimos | vigente | d |  |  |
| 45 | psico: verbal-definicion | vigente | a |  |  |
| 46 | psico: administrativo-ordenacion | vigente | c |  |  |
| 47 | psico: verbal-intrusa | vigente | b |  |  |
| 48 | psico: verbal-definicion | vigente | c |  |  |
| 49 | psico: tablas-lectura | vigente | d |  |  |
| 50 | psico: tablas-lectura | vigente | b |  |  |
| 51 | psico: tablas-lectura | vigente | c |  |  |
| 52 | psico: tablas-lectura | vigente | d |  |  |
| 53 | psico: tablas-lectura | vigente | a |  | Errata: la clase «alumnos sin pelo» es todo alumno que no sea rubio, moreno ni pelirrojo (nota bajo la tabla) |
| 54 | psico: tablas-lectura | vigente | c |  |  |
| 55 | psico: atencion-codificacion | vigente | c |  |  |
| 56 | psico: atencion-codificacion | vigente | d |  | Errata: opción c «Puedan ser tener el mismo soporte» |
| 57 | psico: atencion-codificacion | vigente | a |  |  |
| 58 | psico: atencion-codificacion | vigente | a |  |  |
| 59 | psico: atencion-codificacion | vigente | d |  |  |
| 60 | psico: atencion-codificacion | vigente | d |  |  |

### Primera parte — preguntas de reserva

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | I.6 | dudosa | d |  | Dudosa: la orden que regula el Consejo de Desarrollo Sostenible no está en sources/ ni en normativa.yaml; no se pudo comprobar la composición vigente de su Comisión Permanente. |
| 2 | psico: verbal-antonimos | vigente | d |  |  |
| 3 | I.4 | vigente | a |  | Revisado frente a la LO 1/2025: el art. 65.1.º conserva la letra e), salvo lo que corresponda en primera instancia a la Sección de lo Penal del Tribunal Central de Instancia; la clave se mantiene. |
| 4 | psico: calculo-ecuaciones | vigente | b |  | Errata: reserva idéntica a 2024X-P1-36 (mismo enunciado, opciones y clave) |
| 5 | I.11 | vigente | b |  |  |

### Segunda parte

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | II.2 | vigente | b |  | Errata: la opción d está cortada en el original («…se tramiten los procedimientos en cu») y dice «dentificación»; la a repite «las las». |
| 2 | II.1 | vigente-con-nota | c | Clave oficial discutida: la c contradice el art. 13.1 («sin que se utilicen siglas o abreviaturas»); la correcta es la d (art. 13.2). | Revisado frente al cambio-pendiente (RD 707/2026, desde 02-01-2027): el nuevo art. 13.2 mantiene «se evitará la utilización de fondos con dibujos y tintas que presenten poco contraste»; la d sigue siendo la correcta. |
| 3 | II.2 | vigente | b |  |  |
| 4 | II.3 | vigente | c |  |  |
| 5 | II.3 | vigente | a |  |  |
| 6 | II.4 (o I.11) | vigente | b |  |  |
| 7 | II.3 | vigente | c |  |  |
| 8 | II.4 (o I.11) | vigente | c |  |  |
| 9 | II.4 | vigente-con-nota | b | Clave oficial discutida: la norma no define el PAG como punto único de acceso a todas las Administraciones y a la UE; el art. 2.1 lo ciñe a la AGE y el 2.3 a información de otras Administraciones mediante convenio. | La clave parece seguir la presentación del portal administracion.gob.es, no el texto normativo. |
| 10 | II.4 | vigente | b |  |  |
| 11 | II.8 | vigente | a |  | Sin página guardada que lo confirme: las correcciones de color (saturación, tono) son de imágenes, no de modelos 3D; no se ha comprobado en la interfaz si el panel Formato de modelo 3D ofrece relleno. |
| 12 | II.8 | vigente | c |  |  |
| 13 | II.8 | vigente | b |  |  |
| 14 | II.8 | vigente | c |  |  |
| 15 | II.8 | vigente | a |  |  |
| 16 | II.9 | vigente | a |  |  |
| 17 | II.9 | vigente | b |  |  |
| 18 | II.9 | vigente | b |  |  |
| 19 | II.9 | vigente | d |  |  |
| 20 | II.9 | vigente | d |  | La a y la c incluyen VPN, que no es función de Excel en español (es VNA); la b incluye VENC, que no existe. |
| 21 | II.10 | vigente | b |  |  |
| 22 | II.10 | vigente | a |  |  |
| 23 | II.10 | vigente | c |  | Errata: «Asistente para consulta sencillas». |
| 24 | II.10 | vigente | a |  |  |
| 25 | II.11 | vigente | c |  | Si el integrante es un contacto guardado, puede editarse el contacto y usar «Actualizar ahora» en el grupo; dentro del grupo no se edita la dirección. |
| 26 | II.11 | vigente | b |  | Clave válida en Outlook clásico. |
| 27 | II.11 | vigente | c |  | Clave válida en Outlook clásico. |
| 28 | II.11 | vigente | b |  |  |
| 29 | II.11 (o II.12) | vigente-con-nota | d | Clave oficial discutida: firma y etiqueta no son obligatorias; lo imprescindible es remitente y destinatario, por lo que la d no puede ser la correcta (la c es la más próxima). | La plantilla definitiva imprime d en la 29 y a en la 30; las claves de 31 a 33 son correctas, así que no es un desplazamiento de columna. La plantilla podría corresponder a otro modelo del extraordinario. Decisión del coordinador (Juanjo, 2026-11-05): clave oficial discutida en ambas. |
| 30 | II.11 | vigente-con-nota | a | Clave oficial discutida: la agrupación de direcciones para enviar a todas a la vez es el «Grupo de contactos» (d); «Tabla de envío» no existe. | La plantilla definitiva imprime d en la 29 y a en la 30; las claves de 31 a 33 son correctas, así que no es un desplazamiento de columna. La plantilla podría corresponder a otro modelo del extraordinario. Decisión del coordinador (Juanjo, 2026-11-05): clave oficial discutida en ambas. |
| 31 | II.5 | vigente | b |  |  |
| 32 | II.5 | vigente | d |  |  |
| 33 | II.12 | vigente | c |  |  |
| 34 | II.5 | vigente | a |  | Errata: «Octogonal» por «Octal» en la opción c. |
| 35 | II.5 | vigente | d |  |  |
| 36 | II.5 (o II.6) | vigente | a |  | La clave describe PowerShell 7 (multiplataforma); Windows PowerShell 5.1, el preinstalado, solo funciona en Windows. |
| 37 | II.7 | vigente | b |  | Errata: «Windows 2010» por «Windows 10». |
| 38 | II.6 | vigente-con-nota | d |  | Etiqueta actual: en Windows 11, «Centro de notificaciones» (Windows + N o la fecha y hora de la barra de tareas); «Centro de actividades» es el nombre de Windows 10. |
| 39 | II.6 | función retirada | a |  | Visor 3D ya no viene instalado en Windows 11 y Microsoft lo retiró; la pregunta solo tiene una respuesta para Windows 10. |
| 40 | II.7 | vigente-con-nota | d |  | Etiqueta actual: en Windows 11 no hay botón «Agregar columnas»; las columnas se añaden con clic derecho en el encabezado, en vista Detalles; sin confirmar en la interfaz española. |
| 41 | II.12 (o II.6) | vigente | b |  | «Microsoft Explorer» de las opciones se refiere a Internet Explorer, retirado; no afecta a la clave. |
| 42 | II.7 | vigente-con-nota | a |  | Etiqueta actual: «Herramientas de Windows» (en Windows 10, «Herramientas administrativas»). |
| 43 | II.7 | vigente | d |  |  |
| 44 | II.12 | vigente | a |  |  |
| 45 | II.12 | vigente | c |  |  |
| 46 | II.12 | vigente | b |  |  |
| 47 | II.12 | vigente | b |  |  |
| 48 | II.12 | anulada | Anulada |  | Anulada en la plantilla definitiva. La misma pregunta (Apache) sale en 2024-P2-49 con clave válida. |
| 49 | II.12 | vigente | b |  |  |
| 50 | II.12 | vigente | c |  |  |

### Segunda parte — preguntas de reserva

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | II.8 | vigente | d |  |  |
| 2 | II.4 | vigente | a |  | El Catálogo de Servicios de Administración Digital no es norma; ninguna norma del programa lo regula. |
| 3 | II.9 | vigente | a |  |  |
| 4 | II.6 | vigente | d |  |  |
| 5 | II.5 (o II.6) | vigente | b |  |  |

## conv2022 — Convocatoria 2022 (OEP 2021-2022) — ejercicio único

- Fecha del examen: no impresa; PDF creado el 19-09-2023. Misprint: segunda parte, reserva 5 impresa «5    En Excel 2019…» sin punto. No hay llamamiento extraordinario publicado.
- Cuestionario: `sources/examenes-oficiales/conv2022_cuestionario.pdf`. Plantilla definitiva: `sources/examenes-oficiales/conv2022_plantilla-definitiva.pdf`.

### Primera parte

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | I.2 | vigente | c |  |  |
| 2 | I.2 | vigente | b |  |  |
| 3 | I.1 | vigente | d |  |  |
| 4 | I.1 | vigente | b |  |  |
| 5 | I.3 | vigente | a |  |  |
| 6 | I.4 | vigente | a |  |  |
| 7 | I.3 | vigente | b |  |  |
| 8 | I.5 | vigente | c |  |  |
| 9 | I.5 | vigente | a |  |  |
| 10 | I.7 | vigente | b |  |  |
| 11 | I.7 | vigente | b |  |  |
| 12 | I.6 | norma modificada: V Plan de Gobierno Abierto 2025-2029 (suprime los ejes) | c |  | El «vigente Plan» del examen era el IV Plan (2020-2024), cuyo tercer eje es la integridad. Hoy rige el V Plan 2025-2029, que no tiene ejes: «Con respecto al IV Plan, se suprimen los ejes, que quedan integrados en los compromisos» (content/age-administrativo-c1/sources/otros/transparencia-v-plan.pdf; este curso aún no tiene copia). Resuelto por el coordinador; el clasificador la dejó dudosa. |
| 13 | I.8 | vigente | b |  |  |
| 14 | I.8 | vigente | d |  | Errata: la opción clave dice «En cada una de las provincias pluriprovinciales»; el art. 74 dice «En cada provincia». |
| 15 | I.9 | vigente | d |  |  |
| 16 | I.9 | vigente | b |  |  |
| 17 | I.10 | vigente | c |  |  |
| 18 | I.10 | vigente | c |  |  |
| 19 | I.11 | vigente | c |  |  |
| 20 | I.12 | vigente | b |  | Errata: el enunciado da a la LO 3/2018 el título «de Protección de Datos de Carácter Personal» (el de la LO 15/1999). |
| 21 | I.11 | vigente | b |  |  |
| 22 | I.12 | vigente | c |  | Errata: el enunciado da a la LO 3/2018 el título «de Protección de Datos de Carácter Personal» (el de la LO 15/1999). |
| 23 | I.13 | vigente | b |  |  |
| 24 | I.13 | vigente | b |  |  |
| 25 | I.14 | vigente | c |  | Errata: la opción d dice «un tres» por «tres». |
| 26 | I.14 | vigente | a |  |  |
| 27 | I.15 | vigente | a |  |  |
| 28 | I.15 | vigente | b |  |  |
| 29 | I.16 | vigente | c |  |  |
| 30 | I.16 | vigente | a |  | Revisado frente a la Ley 4/2026 (en vigor 23-10-2026): el art. 26.1.a) ya dice «varias actividades de la vida diaria», sin «básicas»; la clave se mantiene. |
| 31 | psico: calculo-ecuaciones | vigente | c |  |  |
| 32 | psico: calculo-porcentajes | vigente | b |  |  |
| 33 | psico: calculo-fracciones-proporciones | vigente | b |  |  |
| 34 | psico: serie-numerica | vigente | d |  |  |
| 35 | psico: calculo-problemas | vigente | d |  |  |
| 36 | psico: calculo-porcentajes | vigente | b |  |  |
| 37 | psico: serie-numerica | vigente | a |  |  |
| 38 | psico: calculo-problemas | vigente | a |  |  |
| 39 | psico: calculo-problemas | vigente-con-nota | b | Clave oficial discutida: «b» solo da 52 operando de izquierda a derecha; con la prioridad habitual de la multiplicación ninguna opción da 52 (b = −118) |  |
| 40 | psico: verbal-sinonimos | vigente | d |  |  |
| 41 | psico: verbal-sinonimos | vigente | d |  |  |
| 42 | psico: verbal-antonimos | vigente | a |  |  |
| 43 | psico: verbal-intrusa | vigente | c |  |  |
| 44 | psico: verbal-definicion | vigente | b |  | Errata: opción d «Enjuciable» por «Enjuiciable» |
| 45 | psico: verbal-definicion | vigente | b |  |  |
| 46 | psico: verbal-ortografia | vigente | a |  |  |
| 47 | psico: administrativo-ordenacion | vigente | b |  |  |
| 48 | psico: administrativo-clasificacion | vigente | d |  | Errata: los rótulos D2 «Rota, Peter» y D3 «Rota, Marta» no están en orden alfabético; no afecta a la clave |
| 49 | psico: tablas-lectura | vigente | b |  |  |
| 50 | psico: tablas-lectura | vigente | a |  |  |
| 51 | psico: tablas-lectura | vigente | d |  |  |
| 52 | psico: tablas-lectura | vigente | b |  |  |
| 53 | psico: tablas-lectura | vigente | c |  |  |
| 54 | psico: tablas-lectura | vigente | b |  |  |
| 55 | psico: tablas-lectura | vigente | d |  |  |
| 56 | psico: tablas-lectura | vigente | a |  |  |
| 57 | psico: tablas-lectura | vigente | c |  |  |
| 58 | psico: tablas-lectura | vigente | a |  |  |
| 59 | psico: tablas-lectura | vigente | b |  |  |
| 60 | psico: tablas-lectura | vigente | d |  |  |

### Primera parte — preguntas de reserva

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | I.5 | vigente | d |  |  |
| 2 | I.11 | vigente | c |  |  |
| 3 | psico: verbal-sinonimos | vigente | b |  |  |
| 4 | I.15 | vigente | d |  |  |
| 5 | psico: calculo-problemas | vigente-con-nota | a | Clave oficial discutida: 1.105/85 = 13 contrataciones, pero con una contratación cada dos días se llega el día 24 o 26; ninguna opción lo recoge y la clave «el día 13» confunde contrataciones con días |  |

### Segunda parte

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | II.2 | vigente | c |  | El Centro de Información Administrativa sigue existiendo: lo gestiona la Dirección General de Gobernanza Pública (RD 210/2024, art. 11.1.h). |
| 2 | II.1 | vigente | b |  |  |
| 3 | II.2 | vigente | b |  |  |
| 4 | II.2 | vigente | a |  |  |
| 5 | II.3 | vigente | b |  |  |
| 6 | II.3 | vigente | d |  |  |
| 7 | II.3 | vigente | a |  |  |
| 8 | II.4 (o I.11) | vigente | c |  |  |
| 9 | II.4 | vigente | b |  | Errata: el enunciado dice «Real Decreto 203/2023, de 30 de marzo»; es el Real Decreto 203/2021, de 30 de marzo. |
| 10 | II.4 (o I.11) | vigente | b |  |  |
| 11 | II.8 | vigente | a |  |  |
| 12 | II.5 | vigente | c |  |  |
| 13 | II.5 | dudosa | d |  | Pregunta de actualidad caducada: Android 14 (octubre de 2023) era la última versión al celebrarse el examen; hoy lo son Android 16 (junio de 2025) o Android 17, según la fecha en que se publique, y ambas figuran entre las opciones. Ninguna norma fija la respuesta; excluida del set. |
| 14 | II.5 | vigente | c |  |  |
| 15 | II.5 | vigente | a |  | Errata: las opciones escriben «ADM» por AMD y «Speadtrum» por Spreadtrum. |
| 16 | II.6 (o II.12) | vigente-con-nota | a |  | Etiqueta actual: en Windows 11 el icono de red de la barra de tareas abre la Configuración rápida; la flecha junto a Wi-Fi muestra las redes disponibles y el botón Conectar. Sin confirmar en la interfaz española. |
| 17 | II.12 (o II.6) | vigente | d |  | Internet Explorer se retiró el 15-06-2022; Microsoft Edge es el navegador integrado de Windows 11. La clave sigue siendo cierta. |
| 18 | II.7 | vigente | c |  | Posible: en Windows 11 «Restaurar versiones anteriores» solo aparece en «Mostrar más opciones» (menú contextual clásico); también está en Propiedades > Versiones anteriores. |
| 19 | II.7 | vigente | b |  |  |
| 20 | II.12 (o II.5) | vigente | a |  |  |
| 21 | II.7 (o II.6) | vigente | a |  |  |
| 22 | II.7 (o II.6) | vigente | d |  |  |
| 23 | II.7 | vigente | a |  |  |
| 24 | II.7 | vigente | a |  |  |
| 25 | II.7 | vigente | c |  | Posible: en Windows 11 la limpieza se hace también desde Configuración > Sistema > Almacenamiento (Archivos temporales, Sensor de almacenamiento); el Liberador de espacio en disco sigue incluido. |
| 26 | II.12 | vigente | a |  | La clave describe una dirección IPv4; una IPv6 tiene ocho grupos hexadecimales separados por dos puntos. |
| 27 | II.12 (o II.5) | vigente | b |  |  |
| 28 | II.12 (o II.11) | vigente | a |  | El enunciado es impreciso («servidores remotos de archivos»), pero IMAP es el único protocolo de correo entre las opciones. |
| 29 | II.12 | vigente | b |  |  |
| 30 | II.12 | vigente | d |  |  |
| 31 | II.8 | vigente | a |  |  |
| 32 | II.8 | vigente | b |  |  |
| 33 | II.8 | vigente | a |  | La opción d (Definir nueva lista multinivel) está en el mismo menú y también cambia el formato de la lista; la clave sigue el término «estilo de lista». |
| 34 | II.8 | vigente | c |  |  |
| 35 | II.8 | vigente | b |  | Revisado por el coordinador: el clasificador la marcó «Clave oficial discutida» porque ms-word-atajos.html da Ctrl+Alt+F; esa página da los atajos del teclado de EE. UU. (no coincide con Word en español en otros atajos), así que no basta para discutir la clave. Atajo sin confirmar en la interfaz española. |
| 36 | II.9 | vigente | b |  |  |
| 37 | II.9 | vigente | d |  |  |
| 38 | II.9 | vigente | d |  |  |
| 39 | II.9 | vigente | b |  |  |
| 40 | II.9 | vigente | c |  |  |
| 41 | II.10 (o II.5) | vigente | b |  |  |
| 42 | II.10 | anulada | Anulada |  | Anulada en la plantilla definitiva (motivo no publicado; probablemente porque «Campo de búsqueda» no es un tipo de datos: se crea con el Asistente para búsquedas). |
| 43 | II.10 | anulada | Anulada |  | Anulada en la plantilla definitiva (motivo no publicado; probablemente porque en Access concatenan tanto & como +). |
| 44 | II.10 | vigente | d |  |  |
| 45 | II.10 | vigente | c |  |  |
| 46 | II.11 | vigente | a |  |  |
| 47 | II.11 (o II.12) | vigente | d |  |  |
| 48 | II.11 | vigente | b |  | La cifra 320 suma 64 (parte local) + 1 (@) + 255 (dominio); el RFC 5321 limita en la práctica la dirección a 254 caracteres y ninguna página de Microsoft fija un límite propio de Outlook. |
| 49 | II.11 | vigente | d |  | Posible: pestañas de Outlook clásico; el nuevo Outlook para Windows tiene Inicio, Ver y Ayuda. |
| 50 | II.11 | vigente | c |  | Posible: en el nuevo Outlook «Marcar todos como leídos» está en el menú contextual de la carpeta. |

### Segunda parte — preguntas de reserva

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | II.3 | vigente | a |  |  |
| 2 | II.5 (o II.7) | vigente | d |  |  |
| 3 | II.12 | anulada | Anulada |  | Anulada en la plantilla definitiva (motivo no publicado; probablemente porque la opción esperada escribe «ICPM» por ICMP). |
| 4 | II.12 | vigente | d |  |  |
| 5 | II.9 | vigente | d |  |  |

## conv2020 — OEP 2020 — ejercicio único (programa anterior)

- Fecha del examen: no impresa; PDF creado el 27-01-2022. Portada «CUESTIONARIO 19 / AUX–LI», pie «2019 AUX-LI»; la plantilla dice «Oferta de Empleo Público de 2020».
- Cuestionario: `sources/examenes-oficiales/conv2020_cuestionario.pdf`. Plantilla definitiva: `sources/examenes-oficiales/conv2020_plantilla-definitiva.pdf`.

### Primera parte

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | I.1 (o I.5) | vigente | b |  |  |
| 2 | I.2 | vigente | a |  |  |
| 3 | I.2 | vigente | d |  |  |
| 4 | I.2 | vigente | d |  |  |
| 5 | I.1 | vigente | d |  |  |
| 6 | I.3 | vigente | a |  |  |
| 7 | I.4 | vigente | c |  |  |
| 8 | I.3 | vigente | c |  |  |
| 9 | I.4 | vigente | b |  |  |
| 10 | I.8 | vigente | c |  |  |
| 11 | I.6 | vigente | a |  |  |
| 12 | I.8 | anulada | Anulada |  | Anulada. La opción d reproduce el art. 63.1.e) (Subsecretarios); a) es del Secretario de Estado (art. 62.2.i), b) del Director general (art. 66) y c) del Ministro (art. 61.q). |
| 13 | I.10 | vigente | c |  |  |
| 14 | I.11 | vigente | c |  |  |
| 15 | I.7 | vigente | b |  |  |
| 16 | I.11 | vigente | a |  |  |
| 17 | I.12 | vigente | b |  | Errata: el enunciado cita el «Reglamento 2016/697» por el Reglamento (UE) 2016/679. |
| 18 | I.13 | vigente | b |  |  |
| 19 | I.14 | vigente | a |  |  |
| 20 | I.13 | vigente | a |  |  |
| 21 | I.11 | vigente | a |  |  |
| 22 | I.13 | vigente | c |  |  |
| 23 | I.14 | vigente | b |  |  |
| 24 | I.14 | vigente | c |  |  |
| 25 | I.14 | vigente | c |  |  |
| 26 | I.15 | vigente | a |  |  |
| 27 | I.16 | vigente | a |  |  |
| 28 | I.14 | vigente | b |  |  |
| 29 | I.15 | vigente-con-nota | c |  | Denominación actual: Ministerio de Hacienda (RD 829/2023, art. 1); «Ministerio de Hacienda y Función Pública» era su nombre en la fecha del examen. |
| 30 | I.15 | vigente | b |  |  |
| 31 | psico: tablas-lectura | vigente | b |  |  |
| 32 | psico: tablas-lectura | vigente | c |  |  |
| 33 | psico: tablas-lectura | vigente | d |  |  |
| 34 | psico: tablas-lectura | vigente | a |  |  |
| 35 | psico: tablas-lectura | vigente | b |  |  |
| 36 | psico: tablas-lectura | vigente | c |  |  |
| 37 | psico: verbal-sinonimos | vigente | c |  |  |
| 38 | psico: verbal-sinonimos | vigente | a |  |  |
| 39 | psico: atencion-codificacion | vigente | a |  |  |
| 40 | psico: administrativo-clasificacion | vigente | d |  |  |
| 41 | psico: calculo-ecuaciones | vigente | c |  | Redondeo: la opción oficial trunca el valor exacto en vez de redondearlo; sigue siendo la única cercana (−0,6757 → «−0,67») |
| 42 | psico: atencion-codificacion | vigente | b |  |  |
| 43 | psico: atencion-codificacion | vigente | b |  |  |
| 44 | psico: tablas-lectura | vigente | c |  |  |
| 45 | psico: tablas-lectura | vigente | b |  |  |
| 46 | psico: tablas-lectura | vigente | d |  |  |
| 47 | psico: tablas-lectura | vigente | b |  |  |
| 48 | psico: tablas-lectura | vigente | d |  |  |
| 49 | psico: tablas-lectura | vigente | c |  |  |
| 50 | psico: serie-alfanumerica | vigente | c |  |  |
| 51 | psico: calculo-problemas | vigente | a |  |  |
| 52 | psico: calculo-fracciones-proporciones | vigente | c |  |  |
| 53 | psico: serie-numerica | anulada | Anulada |  | Anulada en la plantilla definitiva (motivo no publicado). La serie 4, 1, 5, 2, 7, _ admite dos lecturas: término par siguiente de 1, 2, … → 3; o la suma siguiente → 10. |
| 54 | psico: verbal-antonimos | vigente | b |  |  |
| 55 | psico: verbal-analogia | vigente-con-nota | d | Clave oficial discutida: «Gafa y Ojo» tampoco mantiene la relación continente–contenido (y «Mar y Arena» es dudosa); la respuesta no es única |  |
| 56 | psico: verbal-definicion | vigente | b |  |  |
| 57 | psico: verbal-definicion | vigente | a |  |  |
| 58 | psico: verbal-ortografia | vigente | b |  |  |
| 59 | psico: administrativo-ordenacion | vigente | d |  |  |
| 60 | psico: administrativo-clasificacion | vigente | b |  |  |

### Primera parte — preguntas de reserva

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | psico: verbal-definicion | vigente | a |  |  |
| 2 | psico: calculo-ecuaciones | vigente | b |  | Redondeo: la opción oficial trunca el valor exacto en vez de redondearlo; sigue siendo la única cercana (−3,0476 → «−3,04») |
| 3 | I.3 | vigente | b |  |  |
| 4 | I.7 | vigente | b |  |  |
| 5 | I.13 | vigente | a |  |  |

### Segunda parte

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | II.1 | vigente | c |  |  |
| 2 | II.2 | vigente | a |  |  |
| 3 | II.2 | vigente | d |  |  |
| 4 | II.3 (o II.4) | vigente | d |  |  |
| 5 | II.3 | vigente | c |  |  |
| 6 | II.3 | vigente | a |  |  |
| 7 | II.3 (o II.4) | vigente | a |  | GEISER (Gestión Integrada de Servicios de Registro) sigue siendo la aplicación de registro en la nube de la Secretaría General de Administración Digital; Funciona, Notifica y Red SARA también siguen existiendo. Sin norma en normativa.yaml que la nombre. |
| 8 | II.5 | vigente | c |  |  |
| 9 | II.5 | vigente | d |  |  |
| 10 | II.5 | vigente | d |  |  |
| 11 | II.12 (o II.5) | vigente | b |  |  |
| 12 | II.7 (o II.6) | vigente-con-nota | c |  | Etiqueta actual: en Windows 11 la pestaña «Inicio» del Administrador de tareas es la página «Aplicaciones de arranque» del menú lateral. La pestaña «Planificación» (c) sigue sin existir. |
| 13 | II.7 (o II.6) | vigente | a |  |  |
| 14 | II.7 | vigente | c |  | Posible: en Windows 11 el Símbolo del sistema se abre por defecto dentro de Terminal Windows. |
| 15 | II.7 (o II.6) | vigente | c |  |  |
| 16 | II.7 | vigente | b |  | Posible: en Windows 11 «Expandir» del panel de navegación puede quedar en el menú contextual clásico («Mostrar más opciones»). |
| 17 | II.6 | función retirada | b |  | El Reconocimiento de voz de Windows quedó en desuso en 2023 y se retiró a partir de Windows 11 24H2 (lo sustituye Acceso por voz), así que la opción d tampoco es hoy una herramienta de Windows. Igual que C1 conv2020 P1 50. |
| 18 | II.7 | vigente | c |  |  |
| 19 | II.7 | función retirada | a |  | El Explorador de Windows 11 sustituyó la cinta (Inicio > Organizar > Mover a / Copiar a) por la barra de comandos, que no tiene «Mover a»; se mueve con Cortar y Pegar o arrastrando. Mismo criterio que C1 conv2024_X P1 53. |
| 20 | II.8 | vigente | d |  |  |
| 21 | II.8 | vigente | b |  |  |
| 22 | II.8 | vigente | c |  |  |
| 23 | II.8 | vigente | a |  |  |
| 24 | II.8 | vigente | b |  |  |
| 25 | II.9 | vigente | d |  |  |
| 26 | II.9 | vigente | d |  |  |
| 27 | II.9 | vigente | c |  |  |
| 28 | II.9 | vigente | c |  |  |
| 29 | II.9 | vigente | b |  |  |
| 30 | II.9 | vigente | c |  |  |
| 31 | II.10 | vigente | c |  |  |
| 32 | II.10 | vigente | a |  |  |
| 33 | II.10 | vigente | d |  |  |
| 34 | II.10 | vigente | a |  |  |
| 35 | II.10 | vigente | c |  |  |
| 36 | II.10 | vigente | b |  |  |
| 37 | II.10 | vigente | c |  |  |
| 38 | II.11 | vigente | d |  |  |
| 39 | II.11 | vigente | b |  | Posible: «Ignorar» es de Outlook clásico. |
| 40 | II.11 | vigente | b |  |  |
| 41 | II.11 | vigente | b |  |  |
| 42 | II.11 | vigente | b |  | Posible: solo Outlook clásico. |
| 43 | II.11 | vigente | a |  |  |
| 44 | II.12 | vigente | d |  |  |
| 45 | II.5 (o II.12) | vigente | a |  |  |
| 46 | II.12 | vigente | a |  |  |
| 47 | II.4 (o II.1) | vigente | d |  | La Directiva (UE) 2016/2102 no está en normativa.yaml; la transpone el RD 1112/2018, cuyo art. 1.2 recoge la misma definición. |
| 48 | II.12 | vigente | a |  |  |
| 49 | II.12 | vigente | a |  |  |
| 50 | II.4 (o I.11) | vigente | a |  |  |

### Segunda parte — preguntas de reserva

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | II.12 | vigente | c |  |  |
| 2 | II.9 | vigente | a |  |  |
| 3 | II.8 | vigente | d |  |  |
| 4 | II.5 | vigente | c |  |  |
| 5 | II.9 | vigente | d |  |  |

## conv2020_X — OEP 2020 — ejercicio extraordinario (programa anterior)

- Fecha del examen: no impresa; PDF creado el 28-03-2022. Mismo rótulo «CUESTIONARIO 19 / AUX–LI … EXTRAORDINARIO».
- Cuestionario: `sources/examenes-oficiales/conv2020_extraordinario_cuestionario.pdf`. Plantilla definitiva: `sources/examenes-oficiales/conv2020_extraordinario_plantilla-definitiva.pdf`.

### Primera parte

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | I.5 | vigente | a |  |  |
| 2 | I.1 | vigente | c |  |  |
| 3 | I.2 | vigente | c |  |  |
| 4 | I.3 | vigente | c |  |  |
| 5 | I.4 | vigente | d |  |  |
| 6 | I.5 | vigente | a |  |  |
| 7 | I.5 (o I.8) | vigente | a |  |  |
| 8 | I.8 | vigente | c |  |  |
| 9 | I.7 | vigente | d |  | Revisado: hoy el CTBG es autoridad administrativa independiente vinculada a la AGE a través del Ministerio para la Transformación Digital y de la Función Pública (art. 1 RD 615/2024); la opción d sigue siendo incorrecta. |
| 10 | I.10 | vigente | c |  | Errata: el enunciado atribuye la función al TFUE; está en el art. 17.1 TUE. |
| 11 | I.10 | vigente | c |  |  |
| 12 | I.10 | vigente | c |  |  |
| 13 | I.11 | vigente | d |  |  |
| 14 | I.11 | vigente | b |  |  |
| 15 | I.11 | vigente | a |  |  |
| 16 | I.8 | vigente | a |  |  |
| 17 | I.11 (o I.4) | vigente | d |  |  |
| 18 | I.12 | norma modificada: RGPD art. 4.7 | a |  | La pregunta cita el RD 1720/2007, que desarrolla la LO 15/1999, derogada por la LOPDGDD (disposición derogatoria única.1). En el RGPD la figura es el «responsable del tratamiento» (art. 4.7), que ninguna opción nombra; «responsable del fichero» ya no es la denominación vigente. |
| 19 | I.13 | vigente | c |  |  |
| 20 | I.14 | vigente | b |  |  |
| 21 | I.13 | vigente | a |  |  |
| 22 | I.14 | vigente | b |  |  |
| 23 | I.13 (o I.14) | vigente | b |  |  |
| 24 | I.15 | vigente | b |  |  |
| 25 | I.15 (o I.1) | vigente | a |  |  |
| 26 | I.15 | vigente | c |  |  |
| 27 | I.15 | vigente | d |  |  |
| 28 | I.15 | vigente | b |  |  |
| 29 | I.5 (o I.8) | vigente | b |  |  |
| 30 | I.16 | vigente | c |  |  |
| 31 | psico: atencion-codificacion | vigente | a |  |  |
| 32 | psico: administrativo-clasificacion | vigente | b |  |  |
| 33 | psico: calculo-ecuaciones | vigente | d |  |  |
| 34 | psico: calculo-fracciones-proporciones | vigente | b |  |  |
| 35 | psico: calculo-problemas | vigente | d |  |  |
| 36 | psico: verbal-sinonimos | vigente | b |  |  |
| 37 | psico: verbal-sinonimos | vigente | c |  |  |
| 38 | psico: verbal-antonimos | vigente | c |  |  |
| 39 | psico: verbal-analogia | vigente-con-nota | c | Clave oficial discutida: «Bandera y Asta» tampoco es continente–contenido (y «Calle y Semáforo» es dudosa); la respuesta no es única | Errata: «LIQUIDO» sin tilde |
| 40 | psico: verbal-definicion | vigente | b |  |  |
| 41 | psico: verbal-definicion | vigente | a |  |  |
| 42 | psico: verbal-definicion | vigente | c |  |  |
| 43 | psico: verbal-ortografia | vigente | a |  |  |
| 44 | psico: administrativo-ordenacion | vigente | b |  |  |
| 45 | psico: administrativo-clasificacion | vigente | b |  |  |
| 46 | psico: tablas-lectura | vigente | a |  |  |
| 47 | psico: tablas-lectura | vigente | c |  |  |
| 48 | psico: tablas-lectura | vigente | c |  |  |
| 49 | psico: tablas-lectura | vigente | d |  |  |
| 50 | psico: tablas-lectura | vigente | a |  |  |
| 51 | psico: tablas-lectura | vigente | b |  |  |
| 52 | psico: atencion-codificacion | vigente | d |  |  |
| 53 | psico: atencion-codificacion | vigente | c |  |  |
| 54 | psico: calculo-ecuaciones | anulada | Anulada |  | Anulada en la plantilla definitiva (motivo no publicado). 45x − 60 = −x da x = 60/46 ≈ 1,304, y ninguna opción coincide. |
| 55 | psico: tablas-lectura | vigente | d |  |  |
| 56 | psico: tablas-lectura | vigente | d |  |  |
| 57 | psico: tablas-lectura | vigente | d |  |  |
| 58 | psico: tablas-lectura | vigente | b |  |  |
| 59 | psico: tablas-lectura | vigente | b |  |  |
| 60 | psico: tablas-lectura | vigente | b |  |  |

### Primera parte — preguntas de reserva

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | I.14 | vigente | d |  |  |
| 2 | I.2 | vigente | a |  |  |
| 3 | psico: calculo-ecuaciones | vigente | a |  |  |
| 4 | psico: serie-alfanumerica | vigente | c |  |  |
| 5 | psico: verbal-ortografia | vigente | b |  |  |

### Segunda parte

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | II.1 | vigente | a |  | Revisado frente al cambio-pendiente del art. 13 (RD 707/2026, desde 02-01-2027): la clave descansa en el art. 12.2, que no cambia; b y d siguen siendo falsas con el nuevo art. 13 (requisitos de lectura fácil). |
| 2 | II.5 | vigente | b |  |  |
| 3 | II.6 | función retirada | a |  | En Windows 11 22H2 el Asistente de concentración se sustituyó por «No molestar» (notificaciones) y «Concentración» (sesiones); la pregunta solo se responde para Windows 10. Igual que C1 conv2020_X P1 46. |
| 4 | II.7 (o II.6) | vigente | b |  |  |
| 5 | II.7 | vigente | c |  |  |
| 6 | II.8 | vigente | c |  |  |
| 7 | II.8 | vigente | b |  |  |
| 8 | II.8 | función retirada | b |  | Microsoft indica que «Presentar en línea» (Office Presentation Service) ya no está disponible en la mayoría de versiones de Word para Windows; no figura en Word de Microsoft 365. Igual que C1 conv2020_X P1 54. |
| 9 | II.8 | vigente | c |  |  |
| 10 | II.9 | vigente | b |  |  |
| 11 | II.9 | vigente | d |  |  |
| 12 | II.9 | vigente | a |  | Posible: con algunas configuraciones regionales es-ES la abreviatura del mes aparece como «ene.». |
| 13 | II.9 | vigente | c |  |  |
| 14 | II.11 | vigente | d |  | Posible: válido en Outlook clásico; en el nuevo Outlook las firmas están en Configuración > Cuentas > Firmas. |
| 15 | II.11 | vigente | b |  | Posible: solo Outlook clásico; el nuevo Outlook no tiene grupos de envío/recepción. |
| 16 | II.11 | vigente | d |  | Posible: en Outlook clásico de Microsoft 365 los módulos se muestran en la barra de aplicaciones de la izquierda y el cuadro «Opciones de navegación» puede no estar disponible. |
| 17 | II.11 | vigente | a |  | Posible: Propiedades del mensaje solo en Outlook clásico. |
| 18 | II.11 | vigente | a |  |  |
| 19 | II.12 | vigente | b |  |  |
| 20 | II.2 | vigente | b |  |  |
| 21 | II.2 | vigente | a |  |  |
| 22 | II.2 | vigente | d |  |  |
| 23 | II.2 (o II.4) | vigente | b |  | El 060 sigue siendo el teléfono de información administrativa de la AGE: su gobernanza es de la Dirección General de Gobernanza Pública (RD 210/2024). |
| 24 | II.3 (o I.11) | vigente | c |  |  |
| 25 | II.5 | vigente | a |  |  |
| 26 | II.5 | vigente | c |  |  |
| 27 | II.5 | vigente | d |  |  |
| 28 | II.6 | anulada | Anulada |  | Anulada en la plantilla definitiva (motivo no publicado). |
| 29 | II.7 | vigente | b |  | Posible: el Bloc de notas de Windows 11 ha incorporado formato básico, pero sigue siendo el editor simple del sistema. |
| 30 | II.7 (o II.6) | vigente | b |  |  |
| 31 | II.7 | función retirada | a |  | WordPad se eliminó de Windows 11 a partir de la versión 24H2 (2024); la comparación con el Bloc de notas ya no es posible. Igual que C1 conv2020_X P1 45. |
| 32 | II.7 | vigente-con-nota | c |  | Etiqueta actual: el Explorador de Windows 11 no tiene pestaña «Buscar»; al iniciar una búsqueda aparece en la barra de comandos el botón «Opciones de búsqueda». Sin confirmar en la interfaz española. |
| 33 | II.8 | vigente | d |  |  |
| 34 | II.8 | vigente | c |  |  |
| 35 | II.8 | vigente | d |  | Posible: en Word de Microsoft 365 la barra de herramientas de acceso rápido puede estar oculta por defecto y mostrarse encima o debajo de la cinta; el nombre no cambia. |
| 36 | II.8 | vigente | a |  |  |
| 37 | II.8 | vigente | b |  |  |
| 38 | II.10 | vigente | d |  |  |
| 39 | II.10 | vigente | d |  |  |
| 40 | II.10 | vigente | a |  |  |
| 41 | II.10 | vigente | b |  |  |
| 42 | II.10 | vigente | c |  |  |
| 43 | II.10 | vigente | c |  |  |
| 44 | II.10 | vigente | d |  |  |
| 45 | II.11 | vigente | b |  | Posible: válido en Outlook clásico; en el nuevo Outlook va en Configuración > Correo > Correo no deseado. |
| 46 | II.11 | vigente | d |  | Posible: «Limpiar» solo existe en Outlook clásico. |
| 47 | II.11 | vigente | c |  |  |
| 48 | II.12 | vigente | b |  |  |
| 49 | II.12 | vigente | b |  |  |
| 50 | II.12 | vigente | c |  |  |

### Segunda parte — preguntas de reserva

| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |
|---|---|---|---|---|---|
| 1 | II.10 (o II.5) | vigente | d |  |  |
| 2 | II.7 | vigente | d |  |  |
| 3 | II.11 | vigente | c |  |  |
| 4 | II.9 | vigente | a |  |  |
| 5 | II.10 | vigente | c |  |  |

## Transcription of the image table «Cuadro Laboratorios» (conv2024, primera parte, 55–60)

The table is an embedded image in both modelos (the same image, byte for byte). Transcribed from the render `content/age-auxiliar-c2/sources/examenes-oficiales/renders/conv2024_modeloA_cuestionario_p07.png` (modelo B: `…modeloB_cuestionario_p07.png`). Check: the transcription reproduces the six official keys (55 b, 56 a, 57 b, 58 d, 59 a, 60 c in modelo A).

| Profesor | Materia | Día | Hora | Inscritos | Planta | Aula | Capacidad |
|---|---|---|---|---|---|---|---|
| Rubén Gómez | Química | Martes | 10:00 | 26 | 2 | 2 | 60 |
| Olivia Hidalgo | Biología | Lunes | 12:00 | 41 | 3 | 4 | 53 |
| Ignacio Benítez | Biotecnología | Miércoles | 11:00 | 28 | 2 | 6 | 45 |
| Elías Marín | Bioinformática | Jueves | 12:00 | 47 | 1 | 3 | 50 |
| Marta Torres | Genética | Miércoles | 13:00 | 39 | 2 | 5 | 47 |
| Sergio Parra | Inmunología | Jueves | 11:00 | 45 | 3 | 7 | 55 |
| Inés Herrera | Fisiología | Lunes | 10:00 | 26 | 4 | 1 | 35 |
| Vera Soler | Farmacología | Martes | 12:00 | 31 | 4 | 3 | 41 |
| Antonio Durán | Bioquímica | Viernes | 13:00 | 27 | 4 | 2 | 38 |
| Ángel Gutiérrez | Microbiología | Viernes | 12:00 | 40 | 1 | 2 | 55 |

