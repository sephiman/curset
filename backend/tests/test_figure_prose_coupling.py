# SPDX-License-Identifier: AGPL-3.0-only
"""The lessons' worked numbers are approximations of their figures' generated values.

The FIGURE is the source of truth and the prose rounds it, which couples prose to generator output: a
reseed silently strands every number beside the chart, and nothing crashes.
Each course's `figure-coupling.yaml` declares the coupling; this checks it both ways — the figure moved,
and the prose moved (per-locale number formatting, every content tree the course has). `identical_through`
holds same-seed panels equal bar by bar, and guarded exceptions must keep their generated-instance
lead-in. Every pipeline course is covered; one without figures is recorded as "no figures".
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pytest
import yaml

from pipeline_courses import NO_FIGURES, course_dir, figure_step_line, pipeline_courses
from tradeschool.content.registry import CourseRegistry
from tradeschool.exercises.figures import FigureSpec, build_figure

_DEFAULT_TOL = 0.01  # a human rounding lands well inside 1%; a moved figure lands well outside it

_SERIES_KEYS = ("open", "high", "low", "close", "volume")
_PANE_KEYS = ("rsi", "oi", "cvd")


@dataclass(frozen=True)
class Coupling:
    """One course's coupling manifest, with what it needs to check it."""

    slug: str
    content: Path
    locales: tuple[str, ...]
    figures: dict[str, FigureSpec]
    coupled: dict[str, Any]
    exceptions: dict[str, Any]

    def built(self, figure_id: str) -> dict[str, Any]:
        return build_figure(self.figures[figure_id], self.locales[0])

    def panel(self, figure_id: str, index: int) -> dict[str, Any]:
        panels = self.built(figure_id)["panels"]
        assert isinstance(panels, list)
        panel = panels[index]
        assert isinstance(panel, dict)
        return panel

    def lesson_text(self, lesson_id: str, locale: str) -> str:
        return (self.content / locale / "lessons" / f"{lesson_id}.md").read_text(encoding="utf-8")


def _coupling(course: CourseRegistry) -> Coupling:
    content = course_dir(course)
    with (content / "figure-coupling.yaml").open(encoding="utf-8") as fh:
        raw = yaml.safe_load(fh)
    assert isinstance(raw, dict)
    return Coupling(
        course.slug, content, tuple(course.languages), course.figures, raw["figures"], raw["exceptions"]
    )


_WITH_FIGURES = [_coupling(course) for course in pipeline_courses() if course.has_figures]
_WITHOUT_FIGURES = [course for course in pipeline_courses() if not course.has_figures]


def _resolve(panel: dict[str, Any], what: str, spec: dict[str, Any]) -> float:
    """Turn an anchor's `what` expression into the figure's actual number."""
    kind, _, arg = what.partition(":")
    series = panel["series"]

    if kind == "level":
        for level in panel["levels"]:
            if level["label"] == arg:
                return float(level["price"])
        raise AssertionError(f"no level labelled {arg!r} (has: {[x['label'] for x in panel['levels']]})")
    if kind in ("diagonal_start", "diagonal_end", "diagonal_at"):
        # A sloped line has no single price, so a lesson quoting one has to say WHERE. `diagonal_start`
        # and `diagonal_end` are its two drawn anchors; `diagonal_at:<label>@<bar>` is the PROJECTION at
        # a bar, which is what a break is actually judged against and therefore what m15-l1 prints.
        label, _, at = arg.partition("@")
        for line in panel["diagonals"]:
            if line["label"] == label:
                if kind == "diagonal_start":
                    return float(line["start_price"])
                if kind == "diagonal_end":
                    return float(line["end_price"])
                span = line["end"] - line["start"]
                ratio = (int(at) - line["start"]) / span
                return float(line["start_price"] + (line["end_price"] - line["start_price"]) * ratio)
        raise AssertionError(
            f"no diagonal labelled {label!r} (has: {[x['label'] for x in panel['diagonals']]})"
        )
    if kind in ("band_low", "band_high"):
        # A zone has two prices and a lesson quotes both, so each edge is its own anchor (m34's origin
        # zone and imbalance). The edges are derived from the CANDLES the injector planted — a down-leg's
        # range, a pair of wicks either side of a one-bar move — so they move if the generator moves,
        # which is exactly what this manifest exists to catch.
        for band in panel["bands"]:
            if band["label"] == arg:
                return float(band["low" if kind == "band_low" else "high"])
        raise AssertionError(f"no band labelled {arg!r} (has: {[x['label'] for x in panel['bands']]})")
    if kind in _SERIES_KEYS:
        return float(series[kind][int(arg)])
    if kind in _PANE_KEYS:
        assert kind in panel, f"figure has no {kind} pane"
        return float(panel[kind][int(arg)])
    if kind == "volume_ratio":
        lo, hi = (int(x) for x in arg.split("-"))
        b_lo, b_hi = spec["volume_baseline"]
        return _median(series["volume"][lo:hi]) / _median(series["volume"][b_lo:b_hi])
    if kind in ("fib_impulse_low", "fib_impulse_high"):
        levels = {level["label"]: float(level["price"]) for level in panel["levels"]}
        span = (levels["500"] - levels["618"]) / (0.618 - 0.5)
        high = levels["500"] + span / 2
        return high if kind == "fib_impulse_high" else high - span
    raise AssertionError(f"unknown anchor expression {what!r}")


def _median(values: list[float]) -> float:
    ordered = sorted(values)
    mid = len(ordered) // 2
    return ordered[mid] if len(ordered) % 2 else (ordered[mid - 1] + ordered[mid]) / 2


def _localized(number: float, locale: str) -> str:
    """How each tree writes a coupled number: 1.800 in Spanish, 1,800 in English."""
    grouped = f"{abs(int(number)):,}"
    return grouped.replace(",", ".") if locale == "es" else grouped


def _anchors() -> list[tuple[Coupling, str, dict[str, Any], dict[str, Any]]]:
    return [
        (course, fid, spec, anchor)
        for course in _WITH_FIGURES
        for fid, spec in course.coupled.items()
        for anchor in spec["anchors"]
    ]


def _figures(which: str, keep: Any = lambda spec: True) -> list[tuple[Coupling, str]]:
    return [
        (course, fid)
        for course in _WITH_FIGURES
        for fid in sorted(getattr(course, which))
        if keep(getattr(course, which)[fid])
    ]


def _param_id(value: object) -> str:
    if isinstance(value, Coupling):
        return value.slug
    return value if isinstance(value, str) else ""


def _ident(figure_id: str, anchor: dict[str, Any]) -> str:
    return f"{figure_id}[panel {anchor.get('panel', 0)}] {anchor['what']}"


# --- a course without figures is named, never failed and never an empty pass ----------------------


@pytest.mark.parametrize("course", _WITHOUT_FIGURES, ids=lambda course: course.slug)
def test_a_course_without_figures_is_recorded_as_no_figures(course: CourseRegistry) -> None:
    assert not (course_dir(course) / "figure-coupling.yaml").exists()
    assert figure_step_line(course) == f"{course.slug}: {NO_FIGURES}"


def test_the_pipeline_covers_a_course_with_figures_and_one_without() -> None:
    """Both branches run in this suite, or the "no figures" line is only ever a claim."""
    assert _WITH_FIGURES and _WITHOUT_FIGURES


# --- the manifest describes reality ---------------------------------------------------------------


@pytest.mark.parametrize(("course", "figure_id"), _figures("coupled") + _figures("exceptions"), ids=_param_id)
def test_every_declared_figure_exists_and_its_lessons_embed_it(course: Coupling, figure_id: str) -> None:
    assert figure_id in course.figures, f"figure-coupling.yaml names an unknown figure {figure_id!r}"
    spec = course.coupled.get(figure_id) or course.exceptions[figure_id]
    directive = f"::figure{{id={figure_id}}}"
    for lesson_id in spec["lessons"]:
        for locale in course.locales:
            body = course.lesson_text(lesson_id, locale)
            assert directive in body, f"{locale}/{lesson_id} does not embed {figure_id}"


# --- 1. the figure has not moved out from under the prose -----------------------------------------


@pytest.mark.parametrize(("course", "figure_id", "spec", "anchor"), _anchors(), ids=_param_id)
def test_prose_number_still_approximates_the_generated_value(
    course: Coupling, figure_id: str, spec: dict[str, Any], anchor: dict[str, Any]
) -> None:
    panel = course.panel(figure_id, anchor.get("panel", 0))
    actual = _resolve(panel, anchor["what"], spec)
    stale = (
        f"{_ident(figure_id, anchor)} is now {actual:.2f}. The figure moved out from under the prose "
        f"— re-run the worked-number pass for: {', '.join(spec['lessons'])} (es + en), then update "
        f"content/figure-coupling.yaml."
    )

    if "min" in anchor or "max" in anchor:
        assert anchor["min"] <= actual <= anchor["max"], (
            f"{stale} It left the band [{anchor['min']}, {anchor['max']}] the prose's qualitative "
            f"claim depends on."
        )
        return

    prose = float(anchor["prose"])
    if "abstol" in anchor:
        assert abs(actual - prose) <= anchor["abstol"], f"{stale} The prose says {anchor['prose']}."
    else:
        tol = float(anchor.get("tol", _DEFAULT_TOL))
        assert abs(actual - prose) <= tol * abs(actual), (
            f"{stale} The prose says {anchor['prose']}, which is "
            f"{abs(actual - prose) / abs(actual):.2%} off (tolerance {tol:.0%})."
        )


# --- 2. the prose still prints the number it is pinned to -----------------------------------------


@pytest.mark.parametrize(("course", "figure_id", "spec", "anchor"), _anchors(), ids=_param_id)
def test_every_coupled_number_appears_in_every_lesson_that_quotes_it(
    course: Coupling, figure_id: str, spec: dict[str, Any], anchor: dict[str, Any]
) -> None:
    if not anchor.get("in_prose", True) or "prose" not in anchor:
        # One reason per skipped anchor: the three shapes that are checked by VALUE and deliberately
        # not searched for in the prose. A shared message here would hide which of the three applied.
        if "prose" not in anchor:
            pytest.skip(f"{anchor['what']}: a min/max band, not a printed number — nothing to search for")
        if anchor.get("panel"):
            pytest.skip(
                f"{anchor['what']} panel {anchor['panel']}: the shared-seed twin of a value the prose "
                f"asserts once, on panel 0"
            )
        pytest.skip(f"{anchor['what']}: value-checked only — too small an integer to search for meaningfully")
    # An anchor may narrow the figure's lesson list: two lessons can embed one figure and quote
    # different amounts of it (m09-l1 is the map and prints the support and the spring; m09-l2 walks
    # every phase), and demanding the whole chart from the lesson that needs two numbers would push
    # the other five into it just to satisfy a test.
    for lesson_id in anchor.get("lessons", spec["lessons"]):
        for locale in course.locales:
            wanted = _localized(float(anchor["prose"]), locale)
            body = course.lesson_text(lesson_id, locale)
            # Bounded so 2.125 does not match inside 2.1250 or 2.125,50 — but a number ending a
            # sentence ("...se queda en 29.350.") still counts, so the trailing separator is only
            # rejected when a digit follows it.
            assert re.search(rf"(?<![\d.,]){re.escape(wanted)}(?!\d)(?![.,]\d)", body), (
                f"{locale}/{lesson_id} no longer prints {wanted}, the rounded value of "
                f"{_ident(figure_id, anchor)}. Either the prose drifted from the figure or the "
                f"coupling in content/figure-coupling.yaml is out of date."
            )


# --- 3. panels the prose calls "the same chart" are the same chart --------------------------------


@pytest.mark.parametrize(
    ("course", "figure_id"), _figures("coupled", lambda spec: "identical_through" in spec), ids=_param_id
)
def test_panels_that_share_a_seed_render_the_same_candles(course: Coupling, figure_id: str) -> None:
    spec = course.coupled[figure_id]
    through = spec["identical_through"]
    first = course.panel(figure_id, 0)["series"]
    for index in range(1, len(course.built(figure_id)["panels"])):
        other = course.panel(figure_id, index)["series"]
        for key in ("open", "high", "low", "close"):
            assert first[key][: through + 1] == other[key][: through + 1], (
                f"{figure_id}: panels 0 and {index} diverge in {key} before bar {through}, but "
                f"{', '.join(spec['lessons'])} tell the reader they are the same chart. Either the "
                f"panels stopped sharing a seed or the claim has to come out of the prose."
            )


# --- 4. figures the prose does NOT adapt to keep their lead-in ------------------------------------


@pytest.mark.parametrize(("course", "figure_id"), _figures("exceptions"), ids=_param_id)
def test_exception_figures_keep_their_generated_instance_lead_in(course: Coupling, figure_id: str) -> None:
    spec = course.exceptions[figure_id]
    for lesson_id in spec["lessons"]:
        for locale in course.locales:
            phrase = spec["guard_phrase"][locale]
            body = course.lesson_text(lesson_id, locale)
            assert phrase.lower() in body.lower(), (
                f"{locale}/{lesson_id} lost the '{phrase}' lead-in for {figure_id}. That figure is a "
                f"declared exception — its prose keeps its own numbers — so the reader has to be told "
                f"the chart carries different ones. Reason on file: {spec['why'].strip()}"
            )
