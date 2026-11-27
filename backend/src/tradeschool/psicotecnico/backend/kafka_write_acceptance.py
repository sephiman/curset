# SPDX-License-Identifier: AGPL-3.0-only
"""`kafka-write-acceptance`: whether a produce is accepted for given `acks`, minimum ISR and live ISR."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code
from tradeschool.psicotecnico.backend.source_line import source_line

Kind = Literal["verdict", "headroom"]
Acks = Literal["0", "1", "all"]

RULE = (
    "Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the "
    "leader included, "
    "and `min.insync.replicas` has no effect with `acks=0` or `acks=1`."
)


@dataclass(frozen=True)
class Write:
    kind: Kind
    acks: Acks
    replication_factor: int
    min_isr: int
    in_sync: int
    style: int = 0


def accepted(s: Write) -> bool:
    return s.acks != "all" or s.in_sync >= s.min_isr


def _setup(s: Write) -> str:
    return (
        f"A topic has replication factor {s.replication_factor} and "
        f"{code(f'min.insync.replicas={s.min_isr}')}. "
        f"A producer sends with {code(f'acks={s.acks}')}; {_replicas(s.in_sync)}, leader included, "
        f"{'is' if s.in_sync == 1 else 'are'} in sync."
    )


def _replicas(count: int) -> str:
    return f"{count} replica" + ("" if count == 1 else "s")


def _in_sync(count: int) -> str:
    return f"{_replicas(count)} in sync {'is' if count == 1 else 'are'}"


def _accept(reason: str) -> str:
    return f"The write is accepted without {code('NotEnoughReplicas')}: {reason}"


def _reject(reason: str) -> str:
    return f"The write is rejected with {code('NotEnoughReplicas')}: {reason}"


def _flawed_rules(s: Write) -> list[tuple[str, bool]]:
    """Each named misreading of the rule with the outcome it predicts for this write."""
    factor, in_sync = s.replication_factor, s.in_sync
    rules = [
        (f"every one of the {factor} replicas must be in sync", in_sync >= factor),
        (f"a majority of the {factor} replicas must be in sync", in_sync * 2 > factor),
        (f"{code('acks=all')} waits only for the replicas that are in sync", True),
        ("the leader holds the record, so the producer can be acknowledged", True),
        (f"{code('min.insync.replicas')} is only a target, not a limit on writes", True),
    ]
    if s.acks == "all":
        rules.append(("the leader does not count toward the minimum", in_sync - 1 >= s.min_isr))
    else:
        rules.append(
            (f"{code('min.insync.replicas')} also applies to {code(f'acks={s.acks}')}", in_sync >= s.min_isr)
        )
    return rules


class KafkaWriteAcceptanceGenerator(BackendGenerator[Write]):
    id: ClassVar[str] = "kafka-write-acceptance"
    citation: ClassVar[Citation] = Citation(
        "m08-l02",
        "kafka-topic-configs#min.insync.replicas",
        confirmed=(
            "kafka-topic-configs#min.insync.replicas; kafka-design#availability-and-durability-guarantees"
        ),
    )

    def scenario(self, rng: random.Random, level: int) -> Write | None:
        factor = rng.choice((3, 4, 5))
        min_isr = rng.randint(2, factor - 1)
        if level == 1:
            acks: Acks = rng.choice(("0", "1", "all", "all"))
            in_sync = rng.randint(1, factor)
            return Write("verdict", acks, factor, min_isr, in_sync, rng.randrange(2))
        return Write("headroom", "all", factor, min_isr, rng.randint(min_isr + 1, factor))

    def stem(self, s: Write) -> str:
        if s.kind == "verdict":
            return f"{_setup(s)} Which statement about this write is true?"
        return f"{_setup(s)} How many more replicas can fall out of sync before writes are rejected?"

    def correct(self, s: Write) -> str:
        if s.kind == "headroom":
            return str(s.in_sync - s.min_isr)
        count, minimum, acks = _replicas(s.in_sync), s.min_isr, code(f"acks={s.acks}")
        if not accepted(s):
            return _reject(
                (
                    f"only {count} in sync, fewer than {minimum} that {acks} needs",
                    f"{_in_sync(s.in_sync)} fewer than the {minimum} in {code('min.insync.replicas')}",
                )[s.style]
            )
        if s.acks == "all":
            reach = "meets" if s.in_sync == 1 else "meet"
            return _accept(
                (
                    f"{count} in sync {reach} the minimum {minimum}",
                    f"{_in_sync(s.in_sync)} at least the {minimum} required",
                )[s.style]
            )
        return _accept(
            (
                f"{acks} skips the in-sync check",
                f"only {code('acks=all')} checks the in-sync replica count",
            )[s.style]
        )

    def mistakes(self, s: Write) -> list[str]:
        if s.kind == "headroom":
            return [
                str(s.in_sync - s.min_isr + 1),
                str(s.in_sync - 1),
                str(s.replication_factor - s.min_isr),
                str(s.in_sync - s.min_isr - 1),
                str(s.min_isr),
            ]
        verdict = accepted(s)
        return [
            (_accept if outcome else _reject)(reason)
            for reason, outcome in _flawed_rules(s)
            if outcome != verdict
        ]

    def explanation(self, s: Write) -> str:
        return f"{self._steps(s)} {source_line(self.citation)}"

    def _steps(self, s: Write) -> str:
        if s.kind == "headroom":
            spare = s.in_sync - s.min_isr
            return (
                f"{RULE} Inputs: {s.in_sync} in sync, minimum {s.min_isr}. "
                f"Step 1: with {code('acks=all')} writes pass while the in-sync count is at least "
                f"{s.min_isr}. "
                f"Step 2: the spare replicas are {s.in_sync} - {s.min_isr} = {spare}. "
                f"Result: {spare}, and one more loss leaves {s.min_isr - 1}, below the minimum."
            )
        if s.acks != "all":
            return (
                f"{RULE} Inputs: {code(f'acks={s.acks}')}, {s.in_sync} in sync, minimum {s.min_isr}. "
                f"Step 1: the minimum is checked only when {code('acks=all')}. "
                f"Step 2: here it is {code(f'acks={s.acks}')}, so the in-sync count does not matter. "
                f"Result: the write is accepted."
            )
        verdict = "accepted" if accepted(s) else f"rejected with {code('NotEnoughReplicas')}"
        relation = "at least" if accepted(s) else "below"
        return (
            f"{RULE} Inputs: {code('acks=all')}, {s.in_sync} in sync, minimum {s.min_isr}. "
            f"Step 1: with {code('acks=all')} the minimum is checked. "
            f"Step 2: {s.in_sync} in sync is {relation} {s.min_isr}. "
            f"Result: the write is {verdict}."
        )
