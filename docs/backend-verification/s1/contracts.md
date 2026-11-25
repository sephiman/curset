# S1 contracts — how backend-in-depth content is written, for the S1 code and the S2 writers

Decided in S1 (2026-11-13) under "nothing waits"; each is logged in `decisions.tsv`. Requirements v1.2 win.

## Citations

- A citation is `source_id#anchor`: `source_id` is an id in `content/backend-in-depth/sources/sources.yaml`,
  `anchor` an `anchor` of `sources/anchors/<source_id>.json`. Anchors may hold `(`, `)`, `,`, `<`, `[`, `%`
  and `~`, so a citation is always written as inline code: `` `pg-transaction-iso#XACT-SERIALIZABLE` ``.
- Several citations are separated by `; ` inside one parenthetical.
- Lesson prose (F sentences): the sentence ends with a parenthetical holding only citations:
  `… a serialization failure (`` `pg-transaction-iso#XACT-SERIALIZABLE` ``).`
- Esquema rows (amendment 3): the `tabla` citation column, or the trailing parenthetical of a list row,
  holds only such citations. The loader checks that each one resolves (source registered, anchor present);
  it does not demand that the prose cites the same anchor (that rule is for the norm grammar).
- Questions: `citation: "source_id#anchor"` (several: `"a#x; b#y"`, the first is the key's support).
- Tier B is never cited this way; a J callout names it in `source=`.

## Bullet metadata (scope and coverage audits)

- Right under each `## ` heading of a written lesson, one line `<!-- bullets: 6.2.a 6.2.b -->`.
  Never shown to the reader. `## Key points` and `## Sources` carry none and are not audited.
- A bullet belongs to the lesson's own subsection (`m06-l02` ↔ `6.2.*`). `m00-l01` is exempt (amendment 4).
- A lesson whose body still holds the stub note "Lesson not written yet." is `pending`: skipped by scope,
  counted (not failed) by coverage.

## Judgement (class J, N2)

    :::judgement{source="Google, Site Reliability Engineering, ch. 17" ref="sre-book-testing-reliability#…"}
    According to …, …
    :::

`source` is required (what the text attributes to); `ref` is optional and, when present, a citation as above.

## Code (N1, X facts)

- Fenced blocks with a language (`java`, `kotlin`, `sql`, `yaml`, `json`, `http`, `bash`, `text`).
- A run snippet lives in `content/backend-in-depth/snippets/<lesson-id>/<File>.java|.kt`; its run record next
  to it as `<File>.run.json` (command, exit code, stdout, stderr, sha256 of stdout, snippet sha256, JDK and
  Kotlin versions). A lesson block shows it as ```` ```java snippet=m06-l02/LostUpdate.java ````; the block
  body must equal the file. A question that rests on it carries `snippet: m06-l02/LostUpdate.java`.
- A deliberately broken snippet says so in the text; its record holds the non-zero exit and the error.

## Sources stored outside git (amendment 2)

`storage: local` copies resolve under `$CURSET_SOURCES_LOCAL`
(default `~/PycharmProjects/curset-saved-originals/backend-in-depth/local`). Absent folder: warn and skip
the content check; never fail.

## Diagrams (amendment 12, round D1)

    :::diagram{kind="sequence" caption="One line, under 100 characters"}
    description: Plain text listing the steps or elements in order, as one line.
    t1: Transaction T1
    t2: Transaction T2
    t1 -> t2: reads the row
    t2 --> t1: returns the new value
    :::

- `kind` is `sequence`, `state`, `flow`, `structure` or `timeline`; `caption` is one line; the `description:` line
  is required and is the alt text (`<desc>` of the SVG) and the fallback where no drawing is possible.
- Body lines: `id: label` declares a node (`id` is lower-case `[a-z][a-z0-9_]*`, ids unique); `a -> b: label`
  an edge or message (label optional), `a --> b: label` the dashed form (a return, in a sequence diagram).
  A timeline has only nodes, written `id: when | label`, in order. Every other kind needs at least one edge.
- At most 12 nodes. Orientation is vertical: time or flow runs downwards; a sequence diagram draws participants
  across the top in declaration order and messages in line order; a state or flow cycle closes on the right.
- Meaning: `state` nodes are states and edges transitions; `flow` nodes are steps; `structure` edges read
  "contains" or "points to" (drawn without arrowheads); `timeline` events are drawn along a vertical axis.
- A diagram introduces no fact. Every node, edge, label and `when` restates something the lesson's verified prose
  already says. The writer works from the lesson only and keeps a diagram map (element → the lesson sentence it
  restates) in the work folder; the blind check verifies the map against the sentences. A diagram with any
  fail-fact element is discarded, not repaired. A diagram is not a citation target and carries no citation.
- Place a block on its own, after the paragraph it illustrates, inside the section whose bullets it restates.
  The block is not prose: it is not counted for reading time of facts, glossary or the never-coin check, and
  `check_diagrams` (called by `close_round.sh`) reads only the lesson file: syntax, node limit, caption,
  description. Content-level checks never ask for the diagram map of an earlier round.
- Served form: the loader replaces each block by `::diagram{id="<lesson>-d<n>"}` (n counts blocks in the lesson,
  from 1) and sends `diagrams: [{id, kind, caption, description, svg, svgPrint}]` with the lesson and in the export.
  An invalid block stops the load: `lesson <id>, diagram <n>: <problem>`.
- Drawing: SVG produced by the backend at load time (`tradeschool/content/diagram.py`), no client library. The web
  `svg` paints with CSS variables `--diagram-ink|fill|line|accent` (defined per theme in `index.css`); `svgPrint`
  uses fixed light colours for the PDF, where pdfmake embeds it as vector graphics.
