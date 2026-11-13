# S1 part B — loader and build scripts

Files: `backend/src/tradeschool/citations/course.py` (B1 loader: a course with `sources.yaml` resolves esquema rows `source_id#anchor`; norm rule unchanged elsewhere);
`backend/scripts/tech_sources.py` (`markdown_anchors`, `register-file`, `apply-licences` skips tier `course`);
`backend/scripts/tech_course/` (`lessons`, `programme`, `questions`, `anchor_text`, `toolchain`, `check_citations`, `check_extracts`, `check_scope`, `check_coverage`, `lesson_quota`, `run_snippets`, `build_variants`);
`docs/backend-verification/tools/close_round.sh`; `pyproject.toml` pythonpath adds `.` so tests import `scripts.*`; README paragraph; `content/backend-in-depth/en/lessons/m00-l01.md` (esquema restored, column "Source");
`content/backend-in-depth/sources/sources.yaml` + `anchors/course-requirements.json` (registered through `register-file`, under the registry lock).
Tests: `test_tech_course_citations.py` (red first: 4 of 5 failed before the loader change), `test_tech_sources_markdown.py`, `test_tech_course_scripts.py`, `test_tech_course_snippets.py` (JDK/Kotlin tests skip when absent); fixture family `tests/fixtures/variants/loop-sum.yaml`.
Decisions D20-D28 appended to `decisions.tsv` (course-tier source, loader scope, quota formula, Java pin match on dotted components, Kotlin provisioning, `unshare -rn` + 30 s timeout, record naming, variant mistakes, citation scan rule).
Run from `backend/`: `uv run python -m scripts.tech_course.<name> [--course C]`; Kotlin: `... toolchain provision` (done: 2.4.21 in `~/.cache/curset/toolchains/`, sha256 matched the release's).
Real-course results: `load_registry` loads (m00-l01 esquema row citations resolve); check_citations 1 distinct citation 0 problems; check_extracts 0/0; check_scope 0 written lessons audited, 68 pending... (m00-l01 exempt) 0 problems; check_coverage 249 bullets, 3 dropped, 246 pending, 0 uncovered; run_snippets and `--check` 0 snippets; build_variants no families; lesson_quota prints a 69-row TSV (m00-l01 F=3 quota 10, rest pending).
Verified: `unshare -rn` blocks a snippet's socket (test); Java 25.0.5.0.3 matches pin 25.0.5; a Kotlin snippet runs on 2.4.21; fenced `java snippet=...` info strings do not change `prose_word_count`.
Left: `close_round.sh` not run end to end (it compares other courses via git status, which other agents' work in progress would touch); a `snippet=` info string in the web renderer is the frontend agent's; esquema list rows whose anchors contain `)` may confuse `trailing_parenthetical` (tabla rows are safe; contracts favour tabla for citations); `course-requirements#4-content-classes` hash changes if section 4 of the requirements is edited (the version audit then flags m00-l01).
Suite status: see the status line returned with this report.
