# m06-l08 «InPrivate» item — blind check (2026-11-06)

Scope: `git diff HEAD -- content/age-administrativo-c1/es/lessons/m06-l08.md` (InPrivate list item, lines 86–89, and
the «Fuentes» line, 142–143) and the two `fuentes.yaml` entries. Sources opened directly:
`sources/otros/ms-edge-inprivate_2026-11-06.html` (text extracted, «Se aplica a»: Microsoft Edge, Windows 10, Windows 11)
and `sources/otros/ms-edge-atajos.html`.

| Item | Lines | Faithful | Cited | Placed/scoped | Voice | Verdict | Reason |
|---|---|---|---|---|---|---|---|
| How InPrivate opens: «desde el icono Configuración y más» | 86 | PASS | PASS | PASS | PASS | PASS | Page: «En Microsoft Edge, seleccione el icono Configuración y más y, después, la ventana Nuevo InPrivate.» The garbled item label is left out rather than decoded, as bloque VI spec § Labels requires («never decode a new one yourself (leave that fact out)»); what remains is what the page states. |
| Ctrl+Mayús+N | 86 | PASS | PASS | PASS | PASS | PASS | atajos: «Ctrl + Mayús + N — Abrir una nueva ventana de InPrivate»; key spelling matches the lesson's convention (Ctrl+Mayús+T etc.). |
| F10+Entrar opens the Configuración y más menu | 86–87 | PASS | PASS | PASS | PASS | PASS | atajos: «F10 + Entrar — Abrir el menú Configuración y más». |
| What InPrivate does not save | 87–89 | PASS | PASS | PASS | PASS | PASS | Page: «sin guardar el historial de exploración, las cookies, los datos del sitio o las entradas de formularios en su dispositivo»; second sentence uses «no se guardan en el equipo». Same four items, nothing added. |
| Downloads and favourites kept | 89 | PASS | PASS | PASS | PASS | PASS | Page: «permitir guardar descargas y favoritos». |
| Removed sentences not implied | 86–89 | PASS | — | PASS | — | PASS | No trace of passwords, «al cerrar todas las ventanas», ISP or workplace; «no guarda en el equipo» claims nothing about what others see. |
| «Fuentes» line | 142–143 | PASS | PASS | PASS | PASS | PASS | Title matches the page heading «Explorar InPrivate en Microsoft Edge»; consultado 06-11-2026 matches the yaml. |
| `fuentes.yaml` new entry | 1342–1347 | PASS | — | PASS | — | PASS | sha256 of file = `e60ecd30…0d2b` (matches); url same as old entry; consultado 2026-11-06; `lessons: [m06-l08]`. |
| `fuentes.yaml` old entry | 1335–1341 | PASS | — | PASS | — | PASS | sha256 unchanged and matches the file; `comprobacion` records the browser check and points to the new copy; `lessons: []` is consistent: the lesson no longer cites `ms-edge-inprivate.html` and no file under `exercises/` cites it. |
| Resolver | — | — | PASS (direct) / FAIL (gate) | — | — | see note | `_anchor('m06-l08', …)` resolves both lesson citations (`fuente-ms-edge-inprivate-2026-11-06-html`, `fuente-ms-edge-atajos-html`). `uv run pytest tests/test_citations.py -q -k "not frozen"` does not run: collection error, `excerpts.json is stale` for m04-l09-q078/q080/q082/q083/q084 and m06-l01-q378/q379. That comes from the m04-l09 and m06-l01 follow-ups, not from this change. |

Voice: no filler, no rhetorical device; Peninsular; no coined term. The list of four unsaved items mirrors the page's
enumeration and is not a rhythmic triad.

Notes (outside this change, for the coordinator):
- `excerpts.json` still holds m06-l08 entries citing `ms-edge-inprivate.html` (e.g. `m06-l08-q229`), and
  `citations.es.txt` lines 4272/4274 still list the old file for m06-l08 prose. Both are generated; regenerate
  (`scripts/extract_excerpts.py` and the frozen citation golden) before the gate test can pass.

Counts: 9 items PASS, 0 content FAIL. Resolver gate: blocked by stale `excerpts.json` (not caused by this change);
direct resolution PASS.
