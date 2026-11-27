# SPDX-License-Identifier: AGPL-3.0-only
"""`row-lock-conflicts`: which statements wait on a PostgreSQL row held by a row-level lock."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code
from tradeschool.psicotecnico.backend.cited_source import source_line

Held = Literal["FOR UPDATE", "FOR SHARE"]
Kind = Literal["unblocked", "blocked"]

STATEMENTS: dict[str, str] = {
    "FOR UPDATE": code("SELECT ... FOR UPDATE"),
    "FOR NO KEY UPDATE": code("SELECT ... FOR NO KEY UPDATE"),
    "FOR SHARE": code("SELECT ... FOR SHARE"),
    "FOR KEY SHARE": code("SELECT ... FOR KEY SHARE"),
    "UPDATE": code("UPDATE"),
    "DELETE": code("DELETE"),
    "plain": f"plain {code('SELECT')}",
}
SHARE_ALLOWS = ("FOR SHARE", "FOR KEY SHARE", "plain")


@dataclass(frozen=True)
class LockHeld:
    held: Held
    kind: Kind
    answer: str


def waits(held: Held, statement: str) -> bool:
    if statement == "plain":
        return False
    return held == "FOR UPDATE" or statement not in SHARE_ALLOWS


def _statements(held: Held, *, blocked: bool) -> list[str]:
    return [name for name in STATEMENTS if waits(held, name) == blocked]


class RowLockConflictGenerator(BackendGenerator[LockHeld]):
    id: ClassVar[str] = "row-lock-conflicts"
    citation: ClassVar[Citation] = Citation(
        "m06-l02", "pg-explicit-locking#LOCKING-ROWS", confirmed="pg-explicit-locking#LOCKING-ROWS"
    )

    def scenario(self, rng: random.Random, level: int) -> LockHeld:
        held: Held = rng.choice(("FOR UPDATE", "FOR SHARE"))
        kind: Kind = "blocked" if level == 2 and held == "FOR SHARE" and rng.random() < 0.5 else "unblocked"
        answer = rng.choice(_statements(held, blocked=kind == "blocked"))
        return LockHeld(held, kind, answer)

    def stem(self, s: LockHeld) -> str:
        outcome = "have to wait" if s.kind == "blocked" else "not have to wait"
        return (
            f"In PostgreSQL, transaction 1 has run {code(f'SELECT ... {s.held}')} on one row and has not "
            f"finished. Which statement from transaction 2 on that same row does {outcome}?"
        )

    def correct(self, s: LockHeld) -> str:
        return STATEMENTS[s.answer]

    def mistakes(self, s: LockHeld) -> list[str]:
        if s.held == "FOR UPDATE":
            believed_free = [
                n for n in STATEMENTS if n in ("FOR SHARE", "FOR KEY SHARE", "FOR NO KEY UPDATE")
            ]
        else:
            believed_free = _statements(s.held, blocked=s.kind != "blocked")
        return [STATEMENTS[name] for name in believed_free]

    def explanation(self, s: LockHeld) -> str:
        blocked = ", ".join(STATEMENTS[n] for n in _statements(s.held, blocked=True))
        free = ", ".join(STATEMENTS[n] for n in _statements(s.held, blocked=False))
        rule = (
            "a `FOR UPDATE` lock stops every other lock, update and delete on the row, and row-level "
            "locks never affect plain reads"
            if s.held == "FOR UPDATE"
            else "a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets "
            "`FOR SHARE`, `FOR KEY SHARE` and plain reads through"
        )
        if s.held == "FOR UPDATE":
            misreading = "a reader assumes weaker lock modes, such as a shared lock, can coexist with it"
        elif s.kind == "blocked":
            misreading = "a reader assumes a shared lock stops other shared locks and plain reads"
        else:
            misreading = "a reader assumes a shared lock is a read lock that nothing has to wait on"
        return (
            f"Inputs: transaction 1 holds {code(s.held)} on the row; the question asks for a statement "
            f"that {'waits' if s.kind == 'blocked' else 'does not wait'}. "
            f"Rule: {rule}. "
            f"Step 1: the statements that wait are {blocked}. "
            f"Step 2: the statements that do not wait are {free}. "
            f"Result: {STATEMENTS[s.answer]} is the only offered statement on the "
            f"{'waiting' if s.kind == 'blocked' else 'non-waiting'} side. "
            f"The other options come from one misreading: {misreading}. {source_line(self.citation)}"
        )
