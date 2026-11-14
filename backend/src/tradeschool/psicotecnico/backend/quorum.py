# SPDX-License-Identifier: AGPL-3.0-only
"""`quorum-reads`: whether `w + r > n` makes a read see the last acknowledged write."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code

Kind = Literal["verdict", "min-read", "stale-count"]


@dataclass(frozen=True)
class Quorum:
    kind: Kind
    n: int
    w: int
    r: int
    #: Which wording of the verdict the key takes.
    style: int = 0


def _overlaps(s: Quorum) -> bool:
    return s.w + s.r > s.n


SAFE = ("No stale read is possible", "No stale read is possible, whichever replicas the read picks")
UNSAFE = (
    "A read can return stale data",
    "A read can return stale data when it picks replicas that missed the write",
)


def _verdict_correct(s: Quorum) -> str:
    total = s.w + s.r
    sums = code(f"w + r = {total}")
    if _overlaps(s):
        tail = ("", ", so every read set shares a replica with the write set")[s.style]
        return f"{SAFE[s.style]}: {sums} exceeds {code(f'n = {s.n}')}{tail}"
    tail = ("", ", so a read set can avoid every replica that took the write")[s.style]
    return f"{UNSAFE[s.style]}: {sums} does not exceed {code(f'n = {s.n}')}{tail}"


def _verdict_mistakes(s: Quorum) -> list[str]:
    total = s.w + s.r
    w, r, n = code(f"w = {s.w}"), code(f"r = {s.r}"), code(f"n = {s.n}")
    if _overlaps(s):
        reasons = [
            f"the write reached only {w} of {n} replicas",
            f"{r} is below {n}",
            f"{w} is below {n}",
            "replicas converge only eventually, so any read can lag",
            f"the write is not on every replica, so the {r} read replicas can all be stale",
        ]
        return [f"{form}: {reason}" for reason in reasons for form in UNSAFE]
    reasons = [
        f"the read returns the newest version among its {r} replicas",
        f"the {r} replicas are queried in parallel, so one of them is current",
        "reads always pick the replica with the latest timestamp",
    ]
    if total == s.n:
        reasons += [
            f"{code(f'w + r = {total}')} reaches {n}",
            f"{code(f'w + r = {total}')} equals {n}, which is enough",
        ]
    if s.w * 2 > s.n:
        reasons.append(f"{w} is a majority of {n}")
    if s.r * 2 > s.n:
        reasons.append(f"{r} is a majority of {n}")
    return [f"{form}: {reason}" for reason in reasons for form in SAFE]


class QuorumGenerator(BackendGenerator[Quorum]):
    id: ClassVar[str] = "quorum-reads"
    citation: ClassVar[Citation] = Citation("m09-l02", "paper-dynamo#p7", confirmed="paper-dynamo#p7")

    def scenario(self, rng: random.Random, level: int) -> Quorum:
        n = rng.choice((3, 4, 5, 6, 7))
        kind: Kind = "verdict" if level == 1 else rng.choice(("min-read", "stale-count"))
        w = rng.randint(1, n - 1)
        r = rng.randint(1, n - 1) if level == 1 else rng.randint(1, n - w)
        if kind == "verdict" and rng.random() < 0.5:
            r = max(1, n - w)
        return Quorum(kind, n, w, r, rng.randrange(2))

    def stem(self, s: Quorum) -> str:
        base = (
            f"A key is replicated on {code(f'n = {s.n}')} nodes. A write succeeds once {code(f'w = {s.w}')} "
            f"replicas "
            f"acknowledge it."
        )
        if s.kind == "verdict":
            return (
                f"{base} A later read queries {code(f'r = {s.r}')} replicas, chosen as unluckily as "
                f"possible, "
                f"and "
                f"returns the newest version among them. Which statement is true?"
            )
        if s.kind == "min-read":
            return (
                f"{base} The remaining replicas have not received the write yet. What is the smallest "
                f"{code('r')} "
                f"for which every read is guaranteed to include at least one replica holding the "
                f"acknowledged "
                f"write?"
            )
        return (
            f"{base} The other replicas have not received the write yet. A read queries {code(f'r = {s.r}')} "
            f"replicas, chosen as unluckily as possible. At most how many of the replicas it queries "
            f"can return "
            f"the old value?"
        )

    def correct(self, s: Quorum) -> str:
        if s.kind == "verdict":
            return _verdict_correct(s)
        if s.kind == "min-read":
            return str(s.n - s.w + 1)
        return str(min(s.r, s.n - s.w))

    def mistakes(self, s: Quorum) -> list[str]:
        if s.kind == "verdict":
            return _verdict_mistakes(s)
        if s.kind == "min-read":
            return [str(s.n - s.w), str(s.w), str(s.n // 2 + 1), str(s.n), str(s.n - s.w + 2)]
        return [str(s.r), str(max(0, s.n - s.w - s.r)), str(s.n - s.w + 1), str(max(0, s.r - s.w)), str(s.w)]

    def explanation(self, s: Quorum) -> str:
        total = s.w + s.r
        if s.kind == "verdict":
            outcome = (
                f"{total} is greater than {s.n}, so every read set shares a replica with the write set"
                if _overlaps(s)
                else f"{total} does not exceed {s.n}, so the {s.r} replicas read can all lie among the "
                f"{s.n - s.w} that missed the write"
            )
            return (
                f"The read set and the write set must overlap in at least one replica, which needs "
                f"{code('w + r > n')}. Here {code(f'{s.w} + {s.r} = {total}')} against {code(f'n = {s.n}')}: "
                f"{outcome}. "
                f"Equality is not enough, because {code('w + r = n')} still lets the two sets be disjoint."
            )
        if s.kind == "min-read":
            return (
                f"{s.n - s.w} replicas missed the write. A read must not fit among them, so it needs "
                f"one more "
                f"than "
                f"that: {s.n} - {s.w} + 1 = {s.n - s.w + 1}, which is the smallest {code('r')} with "
                f"{code('w + r > n')}."
            )
        return (
            f"{s.n - s.w} replicas still hold the old value. The unluckiest read queries as many of them as "
            f"it "
            f"can: the smaller of {code(f'r = {s.r}')} and {s.n - s.w}, that is {min(s.r, s.n - s.w)}."
        )
