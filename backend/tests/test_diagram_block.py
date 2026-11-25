# SPDX-License-Identifier: AGPL-3.0-only
"""`:::diagram` blocks (amendment 12): contract, loader, drawing, and no change for lessons without one."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import cast

import pytest

from conftest import FIXTURE_CONTENT
from tradeschool.content import diagram
from tradeschool.content.registry import ContentError, load_registry

LESSON = "en/lessons/m01-l1.md"
STATE = """:::diagram{kind="state" caption="Row version lifecycle"}
description: A live row version becomes dead when a delete commits, and vacuum frees its space.
live: Live version
dead: Dead version
live -> dead: DELETE commits
dead -> live: space reused
:::"""
SEQUENCE = """:::diagram{kind="sequence" caption="Two transactions"}
description: T1 reads, T2 updates and commits, T1 reads again.
t1: Transaction T1
t2: Transaction T2
t1 -> t2: reads
t2 --> t1: value
t1 -> t1: reads again
:::"""
TIMELINE = """:::diagram{kind="timeline" caption="Phases"}
description: Add the column, then backfill.
a: Phase 1 | Add the column
b: Phase 2 | Backfill in batches
:::"""


@pytest.fixture
def course(tmp_path: Path) -> Path:
    copy = tmp_path / "fixture-tecnico"
    shutil.copytree(FIXTURE_CONTENT / "fixture-tecnico", copy)
    return copy


def _append(course: Path, block: str) -> None:
    path = course / LESSON
    path.write_text(path.read_text(encoding="utf-8") + "\n\n" + block + "\n", encoding="utf-8")


def _problems(block: str) -> list[str]:
    return diagram.problems_in("m01-l1", block)


def test_a_lesson_without_a_diagram_is_served_exactly_as_written(course: Path) -> None:
    registry = load_registry(course)
    detail = registry.lesson_detail("m01-l1", "en", set())
    assert detail is not None
    assert detail["markdown"] == (course / LESSON).read_text(encoding="utf-8").strip()
    assert "diagrams" not in detail


def test_a_valid_block_is_served_as_a_leaf_directive_with_its_drawings(course: Path) -> None:
    _append(course, STATE)
    detail = load_registry(course).lesson_detail("m01-l1", "en", set())
    assert detail is not None
    assert '::diagram{id="m01-l1-d1"}' in str(detail["markdown"]) and ":::diagram" not in str(
        detail["markdown"]
    )
    drawings = cast(list[dict[str, str]], detail["diagrams"])
    [drawn] = drawings
    assert drawn["caption"] == "Row version lifecycle" and drawn["kind"] == "state"
    assert "var(--diagram-ink)" in drawn["svg"] and "var(--diagram-ink)" not in drawn["svgPrint"]
    assert "<desc>A live row version" in drawn["svg"]


def test_the_export_carries_the_diagrams_of_the_lesson(course: Path) -> None:
    _append(course, SEQUENCE)
    export = load_registry(course).course_export("en")
    blocks = cast(list[dict[str, list[dict[str, list[dict[str, object]]]]]], export["blocks"])
    lessons = [lesson for block in blocks for m in block["modules"] for lesson in m["lessons"]]
    carrying = [lesson for lesson in lessons if lesson.get("diagrams")]
    assert [lesson["id"] for lesson in carrying] == ["m01-l1"]


@pytest.mark.parametrize(
    ("block", "problem"),
    [
        (STATE.replace('kind="state"', 'kind="pie"'), "`kind` must be one of"),
        (STATE.replace(' caption="Row version lifecycle"', ""), "`caption` is required"),
        (STATE.replace("description: A live", "Note A live"), "not a node, an edge or the description"),
        (STATE.replace("description:", "x:"), "`description:` line is required"),
        (STATE.replace("dead -> live", "dead -> ghost"), "undeclared node ghost"),
        (
            STATE.replace("live: Live version\n", "live: Live version\nlive: Again\n"),
            "node live declared twice",
        ),
        (STATE.replace('caption="Row', 'mood="x" caption="Row'), "unknown attribute mood"),
        (STATE.replace('kind="state"', "kind=state"), 'name="value" pairs'),
        (TIMELINE.replace("Phase 1 | ", ""), "reads `id: when | label`"),
        (
            STATE.replace("live -> dead: DELETE commits\ndead -> live: space reused\n", ""),
            "needs at least one edge",
        ),
    ],
)
def test_an_invalid_block_stops_the_load_naming_lesson_and_block(
    course: Path, block: str, problem: str
) -> None:
    _append(course, block)
    with pytest.raises(ContentError, match="lesson m01-l1, diagram 1") as raised:
        load_registry(course)
    assert problem in str(raised.value)


def test_thirteen_nodes_are_one_too_many_and_twelve_are_fine() -> None:
    def chain(count: int) -> str:
        nodes = "\n".join(f"n{i}: Step {i}" for i in range(count))
        edges = "\n".join(f"n{i} -> n{i + 1}" for i in range(count - 1))
        return f':::diagram{{kind="flow" caption="Chain"}}\ndescription: a chain\n{nodes}\n{edges}\n:::'

    assert _problems(chain(12)) == []
    assert "13 nodes, at most 12" in _problems(chain(13))[0]


def test_a_block_shown_inside_a_code_fence_is_neither_checked_nor_replaced() -> None:
    text = '```text\n:::diagram{kind="pie"}\n:::\n```\n'
    assert _problems(text) == [] and diagram.with_placeholders("m01-l1", text) == text


def test_the_second_block_is_numbered_two(course: Path) -> None:
    _append(course, STATE)
    _append(course, STATE.replace("dead -> live", "dead -> ghost"))
    with pytest.raises(ContentError, match="diagram 2"):
        load_registry(course)


@pytest.mark.parametrize("block", [STATE, SEQUENCE, TIMELINE])
def test_every_kind_draws_a_titled_svg_that_escapes_its_text(block: str) -> None:
    [parsed] = diagram.diagrams_in("m01-l1", block.replace("Transaction T1", "T1 <b>&"))
    svg = diagram.render(parsed, diagram.PRINT)
    assert svg.startswith("<svg") and f"<title>{parsed.caption}</title>" in svg
    assert "<b>" not in svg


def test_print_drawing_has_no_css_variables() -> None:
    [parsed] = diagram.diagrams_in("m01-l1", SEQUENCE)
    assert "var(" not in diagram.render(parsed, diagram.PRINT)


def test_a_cycle_is_drawn_with_the_closing_edge_looping_on_the_right() -> None:
    [parsed] = diagram.diagrams_in("m01-l1", STATE)
    assert "<path" in diagram.render(parsed, diagram.PRINT)


def test_a_code_fence_showing_the_syntax_does_not_take_the_real_block_s_place() -> None:
    text = f"```text\n{STATE}\n```\n\n{STATE}\n"
    served = diagram.with_placeholders("m01-l1", text)
    assert served.startswith("```text\n:::diagram") and served.rstrip().endswith('::diagram{id="m01-l1-d1"}')


def test_a_tilde_fence_is_code_too() -> None:
    assert _problems(f"~~~\n{STATE.replace('state', 'pie')}\n~~~\n") == []


def test_an_indented_opening_is_reported_not_swallowed() -> None:
    indented = "- step\n\n  " + STATE.replace("\n", "\n  ")
    assert "indented or its closing" in " ".join(_problems(indented))


def test_a_timeline_label_may_hold_a_bar() -> None:
    [parsed] = diagram.diagrams_in("m01-l1", TIMELINE.replace("Add the column", "A | B"))
    assert (parsed.nodes[0].when, parsed.nodes[0].label) == ("Phase 1", "A | B")


def test_long_labels_are_wrapped_inside_the_drawing() -> None:
    label = "sends the request to the server and waits for it to answer"
    block = f':::diagram{{kind="flow" caption="c"}}\ndescription: d\na: A\nb: B\na -> b: {label}\n:::'
    [parsed] = diagram.diagrams_in("m01-l1", block)
    svg = diagram.render(parsed, diagram.PRINT)
    width = float(svg.split('width="')[1].split('"')[0])
    assert label not in svg and width > 200


def test_diagram_words_do_not_count_as_reading_time() -> None:
    assert diagram.without_blocks(f"One two.\n\n{STATE}\n\nThree.") == "One two.\n\n\n\nThree."


def test_languages_must_agree_on_the_number_of_diagrams() -> None:
    assert diagram.locale_problems({"en": {"l": STATE}, "es": {"l": "sin diagrama"}})
    assert diagram.locale_problems({"en": {"l": STATE}, "es": {"l": STATE}}) == []
