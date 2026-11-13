# SPDX-License-Identifier: AGPL-3.0-only
"""`isolation-anomaly`: what two interleaved transactions show under a PostgreSQL 18 isolation level."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code

Kind = Literal["dirty", "nonrepeatable", "phantom", "write-skew"]
LEVELS = ("READ UNCOMMITTED", "READ COMMITTED", "REPEATABLE READ", "SERIALIZABLE")
SERIALIZATION = "could not serialize access due to read/write dependencies among transactions"
OPEN_ORDERS = "SELECT count(*) FROM orders WHERE status = 'open'"
CONCURRENT_UPDATE = "could not serialize access due to concurrent update"


@dataclass(frozen=True)
class Interleaving:
    kind: Kind
    level: str
    old: int
    new: int


def sees_committed_changes(level: str) -> bool:
    """Below Repeatable Read a statement sees fresh commits; Read Uncommitted acts as Read Committed."""
    return level in ("READ UNCOMMITTED", "READ COMMITTED")


def _returns(value: int) -> str:
    return f"It returns {code(value)} without waiting for T2"


def _fails(message: str) -> str:
    return f"It fails with {code(message)}"


class IsolationAnomalyGenerator(BackendGenerator[Interleaving]):
    id: ClassVar[str] = "isolation-anomaly"
    # The long form only pads (it asserts nothing): without it the read-only keys are systematically short.
    forms: ClassVar[tuple[str, ...]] = (
        "{}",
        "{} in this interleaving",
        "{}, given the isolation level and the order of statements above",
    )
    citation: ClassVar[Citation] = Citation(
        "m06-l02",
        "pg-transaction-iso#TRANSACTION-ISO; pg-transaction-iso#XACT-SERIALIZABLE",
        confirmed="pg-transaction-iso#TRANSACTION-ISO; pg-transaction-iso#XACT-READ-COMMITTED; "
        "pg-transaction-iso#XACT-REPEATABLE-READ; pg-transaction-iso#XACT-SERIALIZABLE",
    )

    def scenario(self, rng: random.Random, level: int) -> Interleaving:
        kinds: tuple[Kind, ...] = ("dirty", "nonrepeatable") if level == 1 else ("phantom", "write-skew")
        kind = rng.choice(kinds)
        isolation = rng.choice(LEVELS if kind != "write-skew" else LEVELS[2:])
        old = rng.choice((100, 200, 250, 500)) if kind in ("dirty", "nonrepeatable") else rng.randint(2, 6)
        step = rng.choice((50, 100)) if kind in ("dirty", "nonrepeatable") else 1
        return Interleaving(kind, isolation, old, old + step)

    def stem(self, s: Interleaving) -> str:
        begin = f"In PostgreSQL 18 both transactions run at {code(f'ISOLATION LEVEL {s.level}')}."
        if s.kind == "dirty":
            return (
                f"{begin} T2 runs {code(f'UPDATE accounts SET balance = {s.new} WHERE id = 1')} (balance was "
                f"{s.old}) "
                f"and has not committed. T1 now runs {code('SELECT balance FROM accounts WHERE id = 1')}. "
                f"What happens?"
            )
        if s.kind == "nonrepeatable":
            return (
                f"{begin} T1 reads {code('SELECT balance FROM accounts WHERE id = 1')} and gets {s.old}. T2 "
                f"runs "
                f"{code(f'UPDATE accounts SET balance = {s.new} WHERE id = 1')} and commits. T1 repeats the "
                f"same "
                f"{code('SELECT')}. What happens?"
            )
        if s.kind == "phantom":
            return (
                f"{begin} T1 runs {code(OPEN_ORDERS)} "
                f"and gets "
                f"{s.old}. T2 inserts one more open order and commits. T1 repeats the same query. "
                f"What happens?"
            )
        return (
            f"{begin} Two doctors are on call. T1 and T2 each run {code('SELECT count(*) FROM on_call')}, "
            f"see 2, and "
            f"then T1 deletes its own row while T2 deletes the other doctor's row. Both then commit. What "
            f"is the "
            f"outcome?"
        )

    def correct(self, s: Interleaving) -> str:
        if s.kind == "dirty":
            return _returns(s.old)
        if s.kind in ("nonrepeatable", "phantom"):
            return _returns(s.new if sees_committed_changes(s.level) else s.old)
        if s.level == "SERIALIZABLE":
            return f"One transaction fails with {code(SERIALIZATION)}; 1 doctor stays on call"
        return "Both commit; 0 doctors stay on call"

    def mistakes(self, s: Interleaving) -> list[str]:
        if s.kind == "write-skew":
            return [
                "Both commit; 0 doctors stay on call",
                "Both commit; 1 doctor stays on call",
                f"The second delete fails with {code(CONCURRENT_UPDATE)}; 1 doctor stays on call",
                f"One transaction fails with {code(SERIALIZATION)}; 1 doctor stays on call",
                "The second delete waits for the first to commit, then both commit; 0 doctors stay on call",
            ]
        return [
            _returns(s.old),
            _returns(s.new),
            _fails(CONCURRENT_UPDATE),
            "It waits for T2 to commit or roll back before returning anything",
        ]

    def explanation(self, s: Interleaving) -> str:
        if s.kind == "dirty":
            return (
                f"PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like "
                f"READ "
                f"COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value {s.old}."
            )
        if s.kind in ("nonrepeatable", "phantom"):
            if sees_committed_changes(s.level):
                return (
                    f"At {s.level} each statement takes a new snapshot, so T1's second statement sees T2's "
                    f"committed "
                    f"change and returns {s.new}"
                    + (
                        " (READ UNCOMMITTED is treated as READ COMMITTED)."
                        if s.level == "READ UNCOMMITTED"
                        else "."
                    )
                )
            return (
                f"At {s.level} the snapshot is taken at the first statement and kept, so T1 still "
                f"sees {s.old}. "
                f"A plain read raises no serialization error; only a transaction that updates a row changed "
                f"meanwhile does."
                + (" PostgreSQL's REPEATABLE READ also prevents phantoms." if s.kind == "phantom" else "")
            )
        if s.level == "SERIALIZABLE":
            return (
                "Each transaction read the rows the other one changed, a read/write dependency cycle that "
                "no serial "
                "order explains. SERIALIZABLE detects it and rolls one transaction back, leaving 1 doctor "
                "on call."
            )
        return (
            "REPEATABLE READ is snapshot isolation: each transaction keeps its snapshot, and the two deletes "
            "touch "
            "different rows, so neither conflicts. Both commit and no doctor is left; REPEATABLE READ does "
            "not "
            "prevent this serialization anomaly."
        )
