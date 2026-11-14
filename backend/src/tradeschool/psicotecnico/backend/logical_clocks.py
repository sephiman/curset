# SPDX-License-Identifier: AGPL-3.0-only
"""`logical-clocks`: Lamport timestamps, vector timestamps and which events are concurrent."""

from __future__ import annotations

import random
from dataclasses import dataclass
from itertools import combinations
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code

Kind = Literal["lamport", "vector", "concurrent"]
LABELS = "abcdefghijkl"


@dataclass(frozen=True)
class Event:
    label: str
    process: int
    #: The event it receives from, None for a local or send event.
    receives: int | None
    sends: bool


@dataclass(frozen=True)
class Trace:
    kind: Kind
    processes: int
    events: tuple[Event, ...]
    asked: int
    pair: tuple[int, int] = (0, 0)


def lamport(
    s: Trace, *, receive_max: bool = True, receive_plus: bool = True, send_ticks: bool = True
) -> list[int]:
    clock = [0] * s.processes
    stamps: list[int] = []
    for event in s.events:
        p = event.process
        if event.receives is not None:
            heard = stamps[event.receives]
            base = max(clock[p], heard) if receive_max else heard
            clock[p] = base + (1 if receive_plus else 0)
        elif event.sends and not send_ticks:
            pass
        else:
            clock[p] += 1
        stamps.append(clock[p])
    return stamps


def vector(s: Trace, *, merge: str = "max", tick_on_receive: bool = True) -> list[tuple[int, ...]]:
    clocks = [[0] * s.processes for _ in range(s.processes)]
    stamps: list[tuple[int, ...]] = []
    for event in s.events:
        mine = clocks[event.process]
        if event.receives is not None:
            heard = stamps[event.receives]
            if merge == "max":
                mine[:] = [max(a, b) for a, b in zip(mine, heard, strict=True)]
            elif merge == "overwrite":
                mine[:] = list(heard)
            else:
                mine[:] = [a + b for a, b in zip(mine, heard, strict=True)]
        if event.receives is None or tick_on_receive:
            mine[event.process] += 1
        stamps.append(tuple(mine))
    return stamps


def _before(a: tuple[int, ...], b: tuple[int, ...]) -> bool:
    return a != b and all(x <= y for x, y in zip(a, b, strict=True))


def concurrent_pairs(s: Trace) -> list[tuple[int, int]]:
    stamps = vector(s)
    return [
        (i, j)
        for i, j in combinations(range(len(stamps)), 2)
        if not _before(stamps[i], stamps[j]) and not _before(stamps[j], stamps[i])
    ]


def ordered_pairs(s: Trace) -> list[tuple[int, int]]:
    concurrent = set(concurrent_pairs(s))
    return [p for p in combinations(range(len(s.events)), 2) if p not in concurrent]


def _vec(v: tuple[int, ...]) -> str:
    return code("[" + ", ".join(map(str, v)) + "]")


def _pair(s: Trace, pair: tuple[int, int]) -> str:
    return f"{code(s.events[pair[0]].label)} and {code(s.events[pair[1]].label)}"


def _describe(event: Event, s: Trace) -> str:
    where = f"P{event.process + 1}"
    if event.receives is not None:
        return f"{code(event.label)}: {where} receives the message of {code(s.events[event.receives].label)}"
    return f"{code(event.label)}: {where} " + ("sends a message" if event.sends else "has a local step")


def _trace(rng: random.Random, kind: Kind, processes: int, length: int) -> Trace | None:
    events: list[Event] = []
    pending: list[int] = []
    for index in range(length):
        process = rng.randrange(processes)
        candidates = [e for e in pending if events[e].process != process]
        if candidates and rng.random() < 0.55:
            sent = rng.choice(candidates)
            pending.remove(sent)
            events.append(Event(LABELS[index], process, sent, False))
        elif rng.random() < 0.5:
            pending.append(index)
            events.append(Event(LABELS[index], process, None, True))
        else:
            events.append(Event(LABELS[index], process, None, False))
    return Trace(kind, processes, tuple(events), len(events) - 1)


class LogicalClocksGenerator(BackendGenerator[Trace]):
    id: ClassVar[str] = "logical-clocks"
    citation: ClassVar[Citation] = Citation(
        "m08-l01",
        "paper-lamport-time-clocks-columns#p6 (IR1 verified; IR2 deleted on a second voice failure); "
        "paper-dynamo-columns#p12",
    )

    def scenario(self, rng: random.Random, level: int) -> Trace | None:
        kind: Kind = "lamport" if level == 1 else rng.choice(("vector", "concurrent"))
        trace = _trace(rng, kind, rng.choice((2, 3)), rng.randint(6, 8))
        if trace is None or not any(e.receives is not None for e in trace.events):
            return None
        if kind == "concurrent":
            ordered, concurrent = ordered_pairs(trace), concurrent_pairs(trace)
            if not concurrent or len(ordered) < 3:
                return None
            return Trace(kind, trace.processes, trace.events, 0, rng.choice(concurrent))
        receives = [i for i, e in enumerate(trace.events) if e.receives is not None]
        return Trace(kind, trace.processes, trace.events, rng.choice(receives))

    def stem(self, s: Trace) -> str:
        listing = "; ".join(_describe(e, s) for e in s.events)
        if s.kind == "lamport":
            return (
                f"Each of {s.processes} processes keeps a Lamport clock, all starting at 0. Every "
                f"local step, "
                f"send and "
                f"receive is an event, delivered in this global order: {listing}. A message carries "
                f"its sender's "
                f"clock "
                f"after the send. What is the timestamp of event {code(s.events[s.asked].label)}?"
            )
        if s.kind == "vector":
            zero = _vec((0,) * s.processes)
            return (
                f"Each of {s.processes} processes keeps a vector clock, all starting at {zero}. "
                f"Every local step, send and receive is an event, delivered in this global order: {listing}. "
                f"A message "
                f"carries its sender's vector after the send. "
                f"What is the vector of event {code(s.events[s.asked].label)}?"
            )
        return (
            f"Processes P1 to P{s.processes} keep vector clocks, and every local step, send and receive is "
            f"an event, "
            f"delivered in this global order: {listing}. Which pair of events is concurrent?"
        )

    def correct(self, s: Trace) -> str:
        if s.kind == "lamport":
            return str(lamport(s)[s.asked])
        if s.kind == "vector":
            return _vec(vector(s)[s.asked])
        return _pair(s, s.pair)

    def mistakes(self, s: Trace) -> list[str]:
        if s.kind == "lamport":
            clocks = [
                lamport(s, receive_max=False),
                lamport(s, receive_plus=False),
                lamport(s, send_ticks=False),
            ]
            right = lamport(s)[s.asked]
            return [str(v[s.asked]) for v in clocks] + [str(right + 1), str(max(1, right - 1))]
        if s.kind == "vector":
            vectors = [
                vector(s, merge="overwrite"),
                vector(s, merge="sum"),
                vector(s, tick_on_receive=False),
            ]
            return [_vec(v[s.asked]) for v in vectors]
        return [_pair(s, p) for p in ordered_pairs(s)]

    def explanation(self, s: Trace) -> str:
        if s.kind == "lamport":
            clocks = lamport(s)
            steps = []
            own = [0] * s.processes
            for i, event in enumerate(s.events[: s.asked + 1]):
                before = own[event.process]
                how = (
                    f"max({before}, {clocks[event.receives]}) + 1"
                    if event.receives is not None
                    else f"{before} + 1"
                )
                own[event.process] = clocks[i]
                steps.append(f"{code(event.label)} = {how} = {clocks[i]}")
            return (
                "A local step or a send adds 1; a receive takes the larger of its own clock and the "
                "message's, "
                "then adds 1. " + "; ".join(steps) + "."
            )
        stamps = vector(s)
        steps = [
            f"{code(e.label)} = {_vec(stamps[i])}"
            for i, e in enumerate(s.events[: s.asked + 1] if s.kind == "vector" else s.events)
        ]
        if s.kind == "vector":
            return (
                "A receive takes the component-wise maximum of its own vector and the message's, then adds "
                "1 to its "
                "own component; any other event only adds 1. " + "; ".join(steps) + "."
            )
        a, b = s.pair
        return (
            "Event x happened before y when x's vector is at most y's in every component and the vectors "
            "differ; "
            ""
            f"otherwise they are concurrent. Vectors: {'; '.join(steps)}. Neither {_vec(stamps[a])} nor "
            f"{_vec(stamps[b])} is at most the other, so {_pair(s, s.pair)} are concurrent."
        )
