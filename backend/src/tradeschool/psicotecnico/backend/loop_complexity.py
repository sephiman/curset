# SPDX-License-Identifier: AGPL-3.0-only
"""`loop-complexity`: time and space of a generated Java loop, with the classic miscount as a distractor."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code

CONSTANT, LOG, SQRT, LINEAR, LINEARITHMIC, QUADRATIC = (
    "O(1)",
    "O(log n)",
    "O(sqrt n)",
    "O(n)",
    "O(n log n)",
    "O(n^2)",
)
CLASSES = (CONSTANT, LOG, SQRT, LINEAR, LINEARITHMIC, QUADRATIC)


@dataclass(frozen=True)
class Shape:
    name: str
    level: int
    body: str
    time: str
    space: str
    #: The class a hurried reader gives it.
    trap: str
    why: str


def _lines(*lines: str) -> str:
    return "\n".join(lines)


SHAPES = (
    Shape(
        "single",
        1,
        _lines("for (int {i} = 0; {i} < n; {i}++) {{", "    total += {i};", "}}"),
        LINEAR,
        CONSTANT,
        QUADRATIC,
        "one pass of n iterations doing constant work, with a single accumulator",
    ),
    Shape(
        "doubling",
        1,
        _lines("for (int {i} = 1; {i} < n; {i} *= {k}) {{", "    total += {i};", "}}"),
        LOG,
        CONSTANT,
        LINEAR,
        "the counter is multiplied by {k} each time, so it reaches n after about log n steps",
    ),
    Shape(
        "halving",
        1,
        _lines("for (int {i} = n; {i} > 0; {i} /= {k}) {{", "    total += {i};", "}}"),
        LOG,
        CONSTANT,
        LINEAR,
        "the counter is divided by {k} each time, so it reaches 0 after about log n steps",
    ),
    Shape(
        "nested",
        1,
        _lines(
            "for (int {i} = 0; {i} < n; {i}++) {{",
            "    for (int {j} = 0; {j} < n; {j}++) {{",
            "        total += {i} * {j};",
            "    }}",
            "}}",
        ),
        QUADRATIC,
        CONSTANT,
        LINEARITHMIC,
        "n outer iterations each run n inner iterations: n * n",
    ),
    Shape(
        "fixed-inner",
        1,
        _lines(
            "for (int {i} = 0; {i} < n; {i}++) {{",
            "    for (int {j} = 0; {j} < 8; {j}++) {{",
            "        total += {i} + {j};",
            "    }}",
            "}}",
        ),
        LINEAR,
        CONSTANT,
        QUADRATIC,
        "the inner loop always runs 8 times, a constant, so the cost is 8 * n",
    ),
    Shape(
        "collect",
        1,
        _lines(
            "List<Integer> out = new ArrayList<>();",
            "for (int {i} = 0; {i} < n; {i}++) {{",
            "    out.add({i} * {i});",
            "}}",
        ),
        LINEAR,
        LINEAR,
        QUADRATIC,
        "n iterations, and the list keeps n elements, so space grows with n too",
    ),
    Shape(
        "triangle",
        2,
        _lines(
            "for (int {i} = 0; {i} < n; {i}++) {{",
            "    for (int {j} = 0; {j} < {i}; {j}++) {{",
            "        total += {j};",
            "    }}",
            "}}",
        ),
        QUADRATIC,
        CONSTANT,
        LINEARITHMIC,
        "the inner loop runs 0 + 1 + ... + (n - 1) = n(n - 1)/2 times, which is quadratic",
    ),
    Shape(
        "log-inner",
        2,
        _lines(
            "for (int {i} = 0; {i} < n; {i}++) {{",
            "    for (int {j} = 1; {j} < n; {j} *= {k}) {{",
            "        total += {j};",
            "    }}",
            "}}",
        ),
        LINEARITHMIC,
        CONSTANT,
        QUADRATIC,
        "n outer iterations each run about log n inner ones",
    ),
    Shape(
        "geometric",
        2,
        _lines(
            "for (int {i} = 1; {i} < n; {i} *= {k}) {{",
            "    for (int {j} = 0; {j} < {i}; {j}++) {{",
            "        total += {j};",
            "    }}",
            "}}",
        ),
        LINEAR,
        CONSTANT,
        LINEARITHMIC,
        "the inner loop runs 1 + {k} + {k}^2 + ... up to n times in total, a geometric sum dominated by its "
        "last term, about n",
    ),
    Shape(
        "sqrt",
        2,
        _lines("for (int {i} = 1; {i} * {i} <= n; {i}++) {{", "    total += {i};", "}}"),
        SQRT,
        CONSTANT,
        LINEAR,
        "the loop stops when {i} * {i} exceeds n, after about sqrt n iterations",
    ),
)


@dataclass(frozen=True)
class Loop:
    shape: int
    i: str
    j: str
    k: int


def _answer(time: str, space: str) -> str:
    return f"Time {code(time)}, space {code(space)}"


class LoopComplexityGenerator(BackendGenerator[Loop]):
    id: ClassVar[str] = "loop-complexity"
    citation: ClassVar[Citation] = Citation(
        "m02-l01",
        "no stored Tier A anchor states asymptotic analysis (coverage 2.1.a is J); amendment 1: stated model",
        confirmed="ods-1-3-mathematical-background#SECTION00433000000000000000",
    )

    def scenario(self, rng: random.Random, level: int) -> Loop:
        pool = [
            n
            for n, s in enumerate(SHAPES)
            if s.level <= level and (level == 1 or s.level == 2 or rng.random() < 0.3)
        ]
        i, j = rng.choice((("i", "j"), ("a", "b"), ("row", "col"), ("p", "q")))
        return Loop(rng.choice(pool), i, j, rng.choice((2, 3)))

    def _code(self, s: Loop) -> str:
        return SHAPES[s.shape].body.format(i=s.i, j=s.j, k=s.k)

    def stem(self, s: Loop) -> str:
        return (
            "In this Java method, `n` is the input value and every statement in a loop body takes constant "
            "time. "
            "Counting the memory that stays reachable beyond a few local variables, what are its "
            "worst-case time and space complexity?\n\n```java\nvoid run(int n) {\n    long total = 0;\n"
            + _indent(self._code(s))
            + "\n}\n```"
        )

    def correct(self, s: Loop) -> str:
        shape = SHAPES[s.shape]
        return _answer(shape.time, shape.space)

    def mistakes(self, s: Loop) -> list[str]:
        shape = SHAPES[s.shape]
        other_space = LINEAR if shape.space == CONSTANT else CONSTANT
        neighbours = [c for c in CLASSES if c not in (shape.time, shape.trap)][:3]
        pairs = [(shape.trap, shape.space), (shape.time, other_space), (shape.trap, other_space)]
        pairs += [(c, shape.space) for c in neighbours]
        return [_answer(t, sp) for t, sp in pairs]

    def explanation(self, s: Loop) -> str:
        shape = SHAPES[s.shape]
        why = shape.why.format(i=s.i, k=s.k)
        space = (
            "no structure grows with n, so the extra space is constant"
            if shape.space == CONSTANT
            else "the structure built keeps a number of elements proportional to n, so the space is linear"
        )
        return (
            f"Step by step: {why}. Time is {code(shape.time)}. Space: {space}, which is {code(shape.space)}. "
            f"Reading it as {code(shape.trap)} time overcounts: the work does not grow that fast."
        )


def _indent(block: str) -> str:
    return "\n".join("    " + line for line in block.splitlines())
