# SPDX-License-Identifier: AGPL-3.0-only
"""`stream-window-grace`: the tumbling window a record falls into and whether its grace period has run out."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation
from tradeschool.psicotecnico.backend.source_line import source_line

Kind = Literal["window", "late"]

RULE = (
    "Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, "
    "and accepts records until stream time passes its end plus the grace period."
)


@dataclass(frozen=True)
class Record:
    kind: Kind
    size: int
    grace: int
    timestamp: int
    #: The largest timestamp seen so far; unused by the `window` kind.
    stream_time: int = 0


def clock(minutes: int) -> str:
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def start_of(s: Record, timestamp: int | None = None) -> int:
    t = s.timestamp if timestamp is None else timestamp
    return t // s.size * s.size


def window(s: Record, start: int) -> str:
    return f"{clock(start)} to {clock(start + s.size)}"


def closes_at(s: Record) -> int:
    return start_of(s) + s.size + s.grace


def is_accepted(s: Record) -> bool:
    return s.stream_time < closes_at(s)


def _outcome(s: Record, start: int, closed: int) -> str:
    verdict = "Accepted" if s.stream_time < closed else "Rejected"
    return f"{verdict}: the {window(s, start)} window closes at {clock(closed)}"


class WindowGraceGenerator(BackendGenerator[Record]):
    id: ClassVar[str] = "stream-window-grace"
    citation: ClassVar[Citation] = Citation(
        "m08-l07",
        "kafka-streams-dsl-api#tumbling-time-windows",
        confirmed="kafka-streams-dsl-api#tumbling-time-windows; kafka-streams-dsl-api#window-final-results",
    )

    def scenario(self, rng: random.Random, level: int) -> Record | None:
        size = rng.choice((5, 10, 15, 30))
        base = rng.choice((9, 10, 14)) * 60 + rng.randrange(0, 60, 5)
        timestamp = base if level == 1 and rng.random() < 0.4 else base + rng.randint(1, size - 1)
        if level == 1:
            return Record("window", size, 0, timestamp)
        grace = rng.choice((5, 10, 15))
        probe = Record("late", size, grace, timestamp)
        # inside the grace period but past the window end, or clearly after the close
        stream_time = (
            closes_at(probe) - rng.randint(1, grace - 1)
            if rng.random() < 0.5
            else closes_at(probe) + rng.randint(1, 15)
        )
        return Record("late", size, grace, timestamp, stream_time)

    def stem(self, s: Record) -> str:
        if s.kind == "window":
            return (
                f"Kafka Streams aggregates a topic in tumbling windows of {s.size} minutes, aligned "
                f"to the epoch. "
                f"A record carries the timestamp {clock(s.timestamp)}. Which window does it belong to?"
            )
        return (
            f"A Kafka Streams aggregation uses tumbling windows of {s.size} minutes with a grace "
            f"period of {s.grace} minutes. "
            f"Stream time, the largest timestamp seen so far, is {clock(s.stream_time)}. "
            f"A record arrives with the timestamp {clock(s.timestamp)}. What happens to it?"
        )

    def correct(self, s: Record) -> str:
        start = start_of(s)
        if s.kind == "window":
            return window(s, start)
        return _outcome(s, start, closes_at(s))

    def mistakes(self, s: Record) -> list[str]:
        start = start_of(s)
        if s.kind == "window":
            others = (start - s.size, start + s.size, s.timestamp, round(s.timestamp / s.size) * s.size)
            return [window(s, other) for other in others]
        elsewhere = [start - s.size, start + s.size, s.timestamp]
        listed = [_outcome(s, other, other + s.size + s.grace) for other in elsewhere]
        no_grace = _outcome(s, start, start + s.size)
        # without the grace period the same window gets the same verdict only by coincidence
        return [*listed, no_grace] if no_grace[:3] != self.correct(s)[:3] else listed

    def explanation(self, s: Record) -> str:
        return f"{self._steps(s)} {source_line(self.citation)}"

    def _steps(self, s: Record) -> str:
        start = start_of(s)
        if s.kind == "window":
            return (
                f"{RULE} Inputs: size {s.size} minutes, timestamp {clock(s.timestamp)}. "
                f"Step 1: the start is the timestamp rounded down to a multiple of {s.size} minutes, "
                f"which is {clock(start)}. "
                f"Step 2: the end is {clock(start)} + {s.size} minutes = {clock(start + s.size)}. "
                f"Result: {window(s, start)}."
            )
        verdict = "before" if is_accepted(s) else "after"
        result = "accepted" if is_accepted(s) else "rejected"
        return (
            f"{RULE} Inputs: size {s.size} minutes, grace {s.grace} minutes, timestamp {clock(s.timestamp)}, "
            f"stream time {clock(s.stream_time)}. "
            f"Step 1: the record belongs to the {window(s, start)} window. "
            f"Step 2: the window closes at {clock(start + s.size)} + {s.grace} minutes = "
            f"{clock(closes_at(s))}. "
            f"Step 3: stream time {clock(s.stream_time)} is {verdict} {clock(closes_at(s))}. "
            f"Result: the record is {result}."
        )
