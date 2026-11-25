# SPDX-License-Identifier: AGPL-3.0-only
"""check_diagrams reads only the lesson file: red on an invalid block, silent on a lesson without one."""

from __future__ import annotations

import pytest
from scripts.tech_course import check_diagrams
from scripts.tech_course.lessons import Lesson

GOOD = (
    ':::diagram{kind="flow" caption="Two steps"}\n'
    "description: First a, then b.\na: Step a\nb: Step b\na -> b\n:::"
)


def test_a_lesson_without_diagrams_is_clean() -> None:
    assert check_diagrams.diagram_problems([Lesson("m06-l01", "# Title\n\nText.")]) == []


def test_a_valid_block_is_clean() -> None:
    assert check_diagrams.diagram_problems([Lesson("m06-l01", f"## S\n\n{GOOD}\n")]) == []


@pytest.mark.parametrize(
    ("block", "problem"),
    [
        (GOOD.replace(' caption="Two steps"', ""), "`caption` is required"),
        (GOOD.replace("description: First a, then b.\n", ""), "`description:` line is required"),
        (GOOD.replace("a -> b", "a -> c"), "undeclared node c"),
    ],
)
def test_an_invalid_block_names_lesson_and_block(block: str, problem: str) -> None:
    [found] = check_diagrams.diagram_problems([Lesson("m06-l02", f"ok\n\n{block}\n")])
    assert found.startswith("lesson m06-l02, diagram 1") and problem in found


def test_main_exits_one_on_a_problem_and_zero_on_the_course(capsys: pytest.CaptureFixture[str]) -> None:
    assert check_diagrams.main([]) == 0
    assert "problems" in capsys.readouterr().out
