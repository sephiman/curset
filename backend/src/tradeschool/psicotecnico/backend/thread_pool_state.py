# SPDX-License-Identifier: AGPL-3.0-only
"""`thread-pool-state`: threads, queued and rejected tasks of a `ThreadPoolExecutor` fed endless tasks."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code

Kind = Literal["state", "first-rejection"]
Tally = tuple[int, int, int]


@dataclass(frozen=True)
class Pool:
    kind: Kind
    core: int
    maximum: int
    capacity: int
    submissions: int


def pool_state(core: int, maximum: int, capacity: int, submissions: int) -> Tally:
    """Threads, queued and rejected after `execute` was called `submissions` times on tasks that never end."""
    threads = queued = rejected = 0
    for _ in range(submissions):
        if threads < core:
            threads += 1
        elif queued < capacity:
            queued += 1
        elif threads < maximum:
            threads += 1
        else:
            rejected += 1
    return threads, queued, rejected


def _text(tally: Tally) -> str:
    threads, queued, rejected = tally
    return f"threads {threads}, queued {queued}, rejected {rejected}"


def _threads_before_queue(s: Pool) -> Tally:
    threads = min(s.submissions, s.maximum)
    queued = min(s.submissions - threads, s.capacity)
    return threads, queued, s.submissions - threads - queued


def _maximum_ignored(s: Pool) -> Tally:
    return pool_state(s.core, s.core, s.capacity, s.submissions)


def _unbounded_queue(s: Pool) -> Tally:
    return min(s.submissions, s.core), max(0, s.submissions - s.core), 0


def _no_queue(s: Pool) -> Tally:
    return pool_state(s.core, s.maximum, 0, s.submissions)


def _core_taken_as_maximum(s: Pool) -> Tally:
    return pool_state(s.maximum, s.maximum, s.capacity, s.submissions)


def _call(number: int) -> str:
    """The wording follows the number, so an option's length carries no information about the key."""
    return ("{}", "call {}", "call number {}")[number % 3].format(number)


class ThreadPoolStateGenerator(BackendGenerator[Pool]):
    id: ClassVar[str] = "thread-pool-state"
    citation: ClassVar[Citation] = Citation(
        "m03-l02",
        "javadoc-threadpoolexecutor#class-threadpoolexecutor",
        confirmed="javadoc-threadpoolexecutor#class-threadpoolexecutor",
    )

    def scenario(self, rng: random.Random, level: int) -> Pool | None:
        core = rng.randint(1, 3)
        maximum = core + rng.randint(1, 3)
        capacity = rng.randint(2, 5)
        kind: Kind = "state" if level == 1 else "first-rejection"
        submissions = rng.randint(core + capacity + 1, maximum + capacity + 3)
        return Pool(kind, core, maximum, capacity, submissions)

    def stem(self, s: Pool) -> str:
        base = (
            f"A {code('ThreadPoolExecutor')} has {code('corePoolSize')} {s.core}, {code('maximumPoolSize')} "
            f"{s.maximum} and an {code('ArrayBlockingQueue')} of capacity {s.capacity}. Tasks that never "
            f"finish are passed to {code('execute')}."
        )
        if s.kind == "state":
            return (
                f"{base} After {s.submissions} calls, how many threads run, how many tasks wait in the "
                f"queue and how many are rejected?"
            )
        return f"{base} Which call is the first to be rejected?"

    def correct(self, s: Pool) -> str:
        if s.kind == "state":
            return _text(pool_state(s.core, s.maximum, s.capacity, s.submissions))
        return _call(s.maximum + s.capacity + 1)

    def mistakes(self, s: Pool) -> list[str]:
        if s.kind == "state":
            return [
                _text(f(s))
                for f in (
                    _threads_before_queue,
                    _maximum_ignored,
                    _unbounded_queue,
                    _no_queue,
                    _core_taken_as_maximum,
                )
            ]
        wrong = (
            s.core + s.capacity + 1,
            s.maximum + 1,
            s.maximum + s.capacity,
            s.core + s.maximum + s.capacity + 1,
        )
        return [_call(n) for n in wrong]

    def explanation(self, s: Pool) -> str:
        return f"{self._working(s)} Source: {code(self.citation.confirmed)}."

    def _working(self, s: Pool) -> str:
        rule = (
            f"Each call starts a thread while fewer than {code('corePoolSize')} run, otherwise "
            f"queues the task while the queue has room, otherwise starts a thread while fewer than "
            f"{code('maximumPoolSize')} run, otherwise rejects it."
        )
        core_started = min(s.submissions, s.core)
        base = f"1. Core threads started: min({s.submissions}, {s.core}) = {core_started}."
        if s.kind == "state":
            threads, queued, rejected = pool_state(s.core, s.maximum, s.capacity, s.submissions)
            return (
                f"{rule} {base} 2. Tasks queued: at most {s.capacity}, here {queued}. "
                f"3. Extra threads started: {threads - core_started}. "
                f"4. Rejected: {s.submissions} - {threads} - {queued} = {rejected}. "
                f"Result: {_text((threads, queued, rejected))}."
            )
        slots = f"1. Core threads: {s.core}. 2. Queue slots: {s.capacity}."
        return (
            f"{rule} {slots} 3. Extra thread slots: {s.maximum} - {s.core} = {s.maximum - s.core}. "
            f"4. The first call after all are used is call {s.maximum} + {s.capacity} + 1 = "
            f"{s.maximum + s.capacity + 1}, which is rejected."
        )
