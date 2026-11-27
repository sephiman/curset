# SPDX-License-Identifier: AGPL-3.0-only
"""`raft-commit-index`: the highest log entry replicated on a majority of the servers."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation
from tradeschool.psicotecnico.backend.source_line import source_line

RULE = (
    "Rule: an entry is committed once it is on a majority of the servers, and a server with match index k "
    "holds entries 1 to k."
)


@dataclass(frozen=True)
class Replication:
    #: The leader's own last index first, then each follower's match index.
    match: tuple[int, ...]

    @property
    def majority(self) -> int:
        return len(self.match) // 2 + 1

    @property
    def ranked(self) -> list[int]:
        return sorted(self.match, reverse=True)


def commit_index(s: Replication) -> int:
    return s.ranked[s.majority - 1]


class RaftCommitIndexGenerator(BackendGenerator[Replication]):
    id: ClassVar[str] = "raft-commit-index"
    citation: ClassVar[Citation] = Citation(
        "m08-l05",
        "paper-raft-dissertation#p36",
        confirmed="paper-raft-dissertation#p36; paper-raft-dissertation#p32",
    )

    def scenario(self, rng: random.Random, level: int) -> Replication | None:
        size = rng.choice((3, 5)) if level == 1 else rng.choice((5, 7))
        leader = rng.randint(6, 9)
        followers = [rng.randint(0 if level == 2 else 1, leader) for _ in range(size - 1)]
        return Replication((leader, *followers))

    def stem(self, s: Replication) -> str:
        followers = ", ".join(str(m) for m in s.match[1:])
        return (
            f"A Raft cluster has {len(s.match)} servers; the leader's log ends at index {s.match[0]}. "
            f"The followers' match indexes are {followers}. "
            f"All entries come from the leader's current term. What is the highest committed index?"
        )

    def correct(self, s: Replication) -> str:
        return str(commit_index(s))

    def mistakes(self, s: Replication) -> list[str]:
        ranked, majority = s.ranked, s.majority
        return [
            str(s.match[0]),
            str(ranked[-1]),
            str(ranked[majority - 2]),
            str(ranked[majority]) if majority < len(ranked) else str(ranked[-1]),
            str(max(s.match[1:])),
            str(ranked[1]),
        ]

    def explanation(self, s: Replication) -> str:
        return f"{self._steps(s)} {source_line(self.citation)}"

    def _steps(self, s: Replication) -> str:
        ranked = ", ".join(str(m) for m in s.ranked)
        key = commit_index(s)
        return (
            f"{RULE} Inputs: match indexes {', '.join(str(m) for m in s.match)} with the leader's "
            f"own index first. "
            f"Step 1: the majority of {len(s.match)} servers is {len(s.match)} // 2 + 1 = {s.majority}. "
            f"Step 2: sorted from the highest, the indexes are {ranked}. "
            f"Step 3: the index {key} in position {s.majority} is reached by {s.majority} servers, "
            f"and no higher index is. "
            f"Result: {key}."
        )
