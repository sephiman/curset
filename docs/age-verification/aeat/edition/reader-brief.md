# Standing-alone readers — brief (edition step 1, check 4)

Per lesson you get the assembled lesson `content/aeat-agentes-hacienda/es/lessons/<lesson>.md` (sentences cut whole from
the pool lesson `docs/age-verification/aeat/pool/<lesson>.md`) and the reserve `docs/age-verification/aeat/reserve/<lesson>.md`
(everything left out, each line `` `id` · origin · report — text ``, under its section path). You change no file but your
output JSON. You write no prose for the course.

Read the assembled lesson as a student would, top to bottom. Flag every kept sentence, list item or table that no longer
stands alone because something it leans on was left out:
- a dangling anaphor: «dicho plazo», «el apartado anterior», «dicha resolución», «en este caso», «la misma», «los
  mencionados», «estos importes», «la citada ley» whose referent is not in the lesson;
- a list item or esquema whose lead-in is gone, or a lead-in whose list is gone («los siguientes:» with nothing after);
- an exception, «salvo», «sin embargo», «además», «por el contrario» whose rule is not kept;
- a reference to a section, tema, table, example or article of this lesson that is not in it («véase», «como se vio»);
- a paragraph that now starts mid-argument.
Do not flag style, length, missing topics or facts you think should be added. Do not flag a sentence merely because it is
short or because its neighbour is gone, if it still reads whole.

For each flag find, in the reserve file, the neighbouring sentence that solves it (usually the one just before or after
it in the pool lesson). Give its id. If no single reserve sentence solves it, say `"restore": null` and suggest nothing.

Output `docs/age-verification/aeat/edition/reader/<lesson>.json`:

```json
{"flags": [{"line": 123, "starts": "first 8 words of the flagged sentence", "problem": "dangling «dicho plazo»",
            "restore": ["<reserve sentence id>"]}], "checked_lines": N}
```

`restore` is a list of reserve ids (may be several, in pool order) or null. Process your lessons in order and write each
file when done. Final reply: per lesson, number of flags and how many have a restore id. English output only.
