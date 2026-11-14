# SPDX-License-Identifier: AGPL-3.0-only
"""`capacity-estimation`: back-of-envelope QPS, storage, bandwidth and cache size from stated assumptions."""

from __future__ import annotations

import random
from dataclasses import dataclass
from fractions import Fraction
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, grouped

SECONDS_PER_DAY = 86_400
Kind = Literal["qps", "storage", "bandwidth", "cache"]


@dataclass(frozen=True)
class Capacity:
    kind: Kind
    #: Millions of users, writes or items, depending on the kind.
    millions: int
    per_unit: int
    peak: int
    size_kb: int
    years: int
    replicas: int
    percent: int


def _qps(s: Capacity) -> Fraction:
    return Fraction(s.millions * 1_000_000 * s.per_unit * s.peak, SECONDS_PER_DAY)


def _storage_tb(
    s: Capacity, kb_per_tb: int = 10**9, replicas: int | None = None, years: int | None = None
) -> Fraction:
    written_kb = s.millions * 1_000_000 * s.size_kb * 365 * (s.years if years is None else years)
    return Fraction(written_kb * (s.replicas if replicas is None else replicas), kb_per_tb)


def _mbit(qps: Fraction, size_kb: int, bits: int = 8, divisor: int = 1000) -> Fraction:
    return qps * size_kb * bits / divisor


def _cache_gb(s: Capacity, fraction: bool = True, divisor: int = 10**6) -> Fraction:
    share = Fraction(s.percent, 100) if fraction else Fraction(1)
    return s.millions * 1_000_000 * s.size_kb * share / divisor


class CapacityGenerator(BackendGenerator[Capacity]):
    id: ClassVar[str] = "capacity-estimation"
    forms: ClassVar[tuple[str, ...]] = ("{}", "about {}", "approximately {}")
    min_separation: ClassVar[Fraction | None] = Fraction(1, 5)
    citation: ClassVar[Citation] = Citation(
        "m09-l01",
        "no stored anchor states the arithmetic: script from assumptions (amendment 1)",
        confirmed="paper-oneil-lsm-tree#p3",
    )

    def scenario(self, rng: random.Random, level: int) -> Capacity:
        kinds: tuple[Kind, ...] = (
            ("qps", "storage") if level == 1 else ("qps", "bandwidth", "cache", "storage")
        )
        return Capacity(
            kind=rng.choice(kinds),
            millions=rng.choice((5, 8, 10, 20, 25, 40, 50, 100, 150)),
            per_unit=rng.choice((4, 6, 10, 12, 20, 30)),
            peak=rng.choice((2, 3, 4, 5)),
            size_kb=rng.choice((2, 4, 5, 8, 20, 50, 100, 200)),
            years=rng.choice((2, 3, 5)),
            replicas=rng.choice((2, 3)),
            percent=rng.choice((10, 20, 25)),
        )

    def stem(self, s: Capacity) -> str:
        day = (
            f"Use {SECONDS_PER_DAY:,} seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB)."
        )
        if s.kind == "qps":
            return (
                f"A service has {s.millions} million daily active users, each making {s.per_unit} requests "
                f"per day. "
                f"Peak traffic is {s.peak} times the daily average. {day} What peak request rate must "
                f"it handle?"
            )
        if s.kind == "storage":
            return (
                f"A service stores {s.millions} million new records per day of {s.size_kb} KB each, kept for "
                f"{s.years} years with {s.replicas} replicas of every record. {day} How much raw storage "
                f"does "
                f"it need?"
            )
        if s.kind == "bandwidth":
            return (
                f"A service has {s.millions} million daily active users, each making {s.per_unit} requests "
                f"per "
                f"day, with a {s.size_kb} KB response and a peak of {s.peak} times the average. {day} "
                f"Use 1 Mbit = 1,000 kbit. What peak outbound bandwidth does it need?"
            )
        return (
            f"A cache keeps the hottest {s.percent}% of {s.millions} million objects of {s.size_kb} KB each. "
            f"Use decimal units (1 GB = 10^6 KB). How much memory does the cache need for one copy of the "
            f"data?"
        )

    def correct(self, s: Capacity) -> str:
        if s.kind == "qps":
            return f"{grouped(_qps(s))} QPS"
        if s.kind == "storage":
            return f"{grouped(_storage_tb(s), 1)} TB"
        if s.kind == "bandwidth":
            return f"{grouped(_mbit(_qps(s), s.size_kb), 1)} Mbit/s"
        return f"{grouped(_cache_gb(s), 1)} GB"

    def mistakes(self, s: Capacity) -> list[str]:
        if s.kind == "qps":
            average = Fraction(s.millions * 1_000_000 * s.per_unit, SECONDS_PER_DAY)
            per_hour = Fraction(s.millions * 1_000_000 * s.per_unit * s.peak, 3600)
            return [
                f"{grouped(average)} QPS",
                f"{grouped(_qps(s) * s.peak)} QPS",
                f"{grouped(_qps(s) / s.peak)} QPS",
                f"{grouped(per_hour)} QPS",
                f"{grouped(_qps(s) * 1000)} QPS",
                f"{grouped(_qps(s) / 1000, 1)} QPS",
            ]
        if s.kind == "storage":
            return [
                f"{grouped(_storage_tb(s, replicas=1), 1)} TB",
                f"{grouped(_storage_tb(s, years=1), 1)} TB",
                f"{grouped(_storage_tb(s, kb_per_tb=1024**3), 1)} TB",
                f"{grouped(_storage_tb(s, replicas=s.replicas + 1), 1)} TB",
                f"{grouped(_storage_tb(s, kb_per_tb=10**6), 1)} TB",
                f"{grouped(_storage_tb(s, kb_per_tb=10**12), 1)} TB",
            ]
        if s.kind == "bandwidth":
            qps = _qps(s)
            return [
                f"{grouped(_mbit(qps, s.size_kb, bits=1), 1)} Mbit/s",
                f"{grouped(_mbit(qps, s.size_kb, divisor=1024), 1)} Mbit/s",
                f"{grouped(_mbit(qps / s.peak, s.size_kb), 1)} Mbit/s",
                f"{grouped(_mbit(qps, s.size_kb, bits=10), 1)} Mbit/s",
                f"{grouped(_mbit(qps, s.size_kb, divisor=1), 1)} Mbit/s",
                f"{grouped(_mbit(qps, s.size_kb, divisor=10**6), 1)} Mbit/s",
            ]
        return [
            f"{grouped(_cache_gb(s, fraction=False), 1)} GB",
            f"{grouped(_cache_gb(s, divisor=1024**2), 1)} GB",
            f"{grouped(_cache_gb(s) * 2, 1)} GB",
            f"{grouped(_cache_gb(s) / 10, 1)} GB",
            f"{grouped(_cache_gb(s, divisor=10**3), 1)} GB",
            f"{grouped(_cache_gb(s, divisor=10**9), 1)} GB",
        ]

    def explanation(self, s: Capacity) -> str:
        users = s.millions * 1_000_000
        if s.kind == "qps":
            return (
                f"Requests per day: {users:,} x {s.per_unit} = {users * s.per_unit:,}. "
                f"Average rate: {users * s.per_unit:,} / {SECONDS_PER_DAY:,} s = "
                f"{grouped(_qps(s) / s.peak, 1)} "
                f"QPS. "
                f"Peak rate: {grouped(_qps(s) / s.peak, 1)} x {s.peak} = {grouped(_qps(s))} QPS."
            )
        if s.kind == "storage":
            return (
                f"Per day: {users:,} x {s.size_kb} KB = {users * s.size_kb:,} KB. Over {s.years} years: "
                f"{users * s.size_kb:,} x 365 x {s.years} KB. With {s.replicas} replicas that is "
                f"{grouped(_storage_tb(s) * 10**9)} KB, which is {grouped(_storage_tb(s), 1)} TB."
            )
        if s.kind == "bandwidth":
            return (
                f"Peak rate: {users:,} x {s.per_unit} x {s.peak} / {SECONDS_PER_DAY:,} s = "
                f"{grouped(_qps(s), 1)} "
                f"QPS. "
                f"Each response is {s.size_kb} KB = {s.size_kb * 8} kbit, so {grouped(_qps(s), 1)} "
                f"x {s.size_kb * 8} "
                f"kbit "
                f"/ 1,000 = {grouped(_mbit(_qps(s), s.size_kb), 1)} Mbit/s."
            )
        return (
            f"Hot objects: {users:,} x {s.percent}% = {grouped(users * Fraction(s.percent, 100))}. "
            f"Memory: {grouped(users * Fraction(s.percent, 100))} x {s.size_kb} KB = "
            f"{grouped(_cache_gb(s) * 10**6)} KB, which is {grouped(_cache_gb(s), 1)} GB."
        )
