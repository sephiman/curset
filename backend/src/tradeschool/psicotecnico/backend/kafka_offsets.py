# SPDX-License-Identifier: AGPL-3.0-only
"""`kafka-consumer-lag`: committed offset (the next record to read) and lag after consumer events."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code

Kind = Literal["lag", "restart"]
Step = tuple[str, int]


@dataclass(frozen=True)
class Partition:
    kind: Kind
    steps: tuple[Step, ...]


@dataclass(frozen=True)
class Reading:
    end: int
    position: int
    committed: int
    #: Position at the moment of the last crash, with the committed offset it fell back to.
    crashed_at: int
    resumed_at: int


def replay(s: Partition) -> Reading:
    end = position = committed = crashed_at = resumed_at = 0
    for name, amount in s.steps:
        if name == "produce":
            end += amount
        elif name == "poll":
            position += min(amount, end - position)
        elif name == "commit":
            committed = position
        else:
            crashed_at, resumed_at = position, committed
            position = committed
    return Reading(end, position, committed, crashed_at, resumed_at)


NARRATION = {
    "produce": "{n} records are produced",
    "poll": "the consumer polls and processes up to {n} records",
    "commit": "the consumer commits its position",
    "crash": "the consumer crashes and restarts",
}


def _narrate(steps: tuple[Step, ...]) -> str:
    return "; ".join(NARRATION[name].format(n=amount) for name, amount in steps)


class KafkaOffsetsGenerator(BackendGenerator[Partition]):
    id: ClassVar[str] = "kafka-consumer-lag"
    citation: ClassVar[Citation] = Citation(
        "m08-l02",
        "kafka-javadoc-kafkaconsumer#offsets-and-consumer-position-heading; "
        "kafka-javadoc-kafkaconsumer#commitSync(java.util.Map)",
    )

    def scenario(self, rng: random.Random, level: int) -> Partition | None:
        steps: list[Step] = [("produce", rng.randint(8, 20))]
        for _ in range(rng.randint(3, 5)):
            steps.append(
                rng.choice(
                    [
                        ("poll", rng.randint(2, 8)),
                        ("poll", rng.randint(2, 8)),
                        ("commit", 0),
                        ("produce", rng.randint(2, 9)),
                    ]
                )
            )
        if level == 1:
            steps.append(("poll", rng.randint(2, 6)))
            steps.insert(rng.randint(2, len(steps) - 1), ("commit", 0))
            scenario = Partition("lag", tuple(steps))
            return scenario if replay(scenario).position > replay(scenario).committed else None
        steps.append(("poll", rng.randint(2, 6)))
        steps.append(("crash", 0))
        scenario = Partition("restart", tuple(steps))
        reading = replay(scenario)
        return scenario if reading.crashed_at - reading.resumed_at > 0 and reading.committed > 0 else None

    def stem(self, s: Partition) -> str:
        setup = (
            "A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. "
            f"In order: {_narrate(s.steps)}."
        )
        if s.kind == "lag":
            return (
                f"{setup} The lag is the log-end offset minus the committed offset. What are the committed "
                f"offset and the lag at the end?"
            )
        return (
            f"{setup} After the restart the consumer resumes from its committed offset. "
            f"Which offset does the first fetch after the restart start from, and how many already processed "
            f"records will it read again?"
        )

    def correct(self, s: Partition) -> str:
        r = replay(s)
        if s.kind == "lag":
            return self._lag(r.committed, r.end - r.committed)
        return self._restart(r.resumed_at, r.crashed_at - r.resumed_at)

    @staticmethod
    def _lag(committed: int, lag: int) -> str:
        return f"committed {code(committed)}, lag {code(lag)}"

    @staticmethod
    def _restart(offset: int, reread: int) -> str:
        return f"offset {code(offset)}, {reread} {'record' if reread == 1 else 'records'} read again"

    def mistakes(self, s: Partition) -> list[str]:
        r = replay(s)
        if s.kind == "lag":
            return [
                self._lag(max(0, r.committed - 1), r.end - max(0, r.committed - 1)),
                self._lag(r.committed, r.end - r.position),
                self._lag(r.position, r.end - r.position),
                self._lag(r.committed + 1, r.end - r.committed - 1),
                self._lag(r.position - 1, r.end - r.position + 1),
                self._lag(r.committed, r.end - r.committed + r.position - r.committed),
            ]
        reread = r.crashed_at - r.resumed_at
        return [
            self._restart(r.crashed_at, 0),
            self._restart(r.resumed_at + 1, max(0, reread - 1)),
            self._restart(r.resumed_at - 1, reread + 1),
            self._restart(r.resumed_at, reread + 1),
            self._restart(r.resumed_at, max(0, reread - 1)),
            self._restart(r.crashed_at - 1, 1),
        ]

    def explanation(self, s: Partition) -> str:
        r = replay(s)
        if s.kind == "lag":
            return (
                f"Replaying the events gives log-end offset {r.end} and position {r.position}. A commit "
                f"stores "
                f"the "
                f"position, which is the offset of the next record to read, not the last one processed. The "
                f"last commit "
                f"left {r.committed}, so lag = {r.end} - {r.committed} = {r.end - r.committed}. Records "
                f"polled "
                f"after "
                f"that commit are not committed yet."
            )
        return (
            f"Before the crash the position was {r.crashed_at} but the last commit stored {r.resumed_at}, "
            f"the offset of "
            f"the next record to read at that time. A restarted consumer fetches from the committed offset, "
            f"so it "
            f"starts at {r.resumed_at} and reads {r.crashed_at} - {r.resumed_at} = "
            f"{r.crashed_at - r.resumed_at} "
            f"records again."
        )
