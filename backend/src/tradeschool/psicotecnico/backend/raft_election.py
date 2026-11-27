# SPDX-License-Identifier: AGPL-3.0-only
"""`raft-election-votes`: the votes a Raft candidate needs, counted over the full cluster."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation
from tradeschool.psicotecnico.backend.source_line import source_line

RULE = (
    "Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, "
    "and each server votes for at most one candidate per term."
)
LABELS = ("A", "B", "C")


@dataclass(frozen=True)
class Election:
    cluster: int
    votes: tuple[int, int, int]
    asked: int = 0

    @property
    def needed(self) -> int:
        return self.cluster // 2 + 1


def _missing(s: Election) -> int:
    return s.needed - s.votes[s.asked]


class RaftElectionVotesGenerator(BackendGenerator[Election]):
    id: ClassVar[str] = "raft-election-votes"
    levels: ClassVar[tuple[int, ...]] = (1,)
    citation: ClassVar[Citation] = Citation(
        "m08-l05", "paper-raft-dissertation#p34", confirmed="paper-raft-dissertation#p34"
    )

    def scenario(self, rng: random.Random, level: int) -> Election | None:
        cluster = rng.choice((5, 7, 9))
        cast = rng.randint(3, cluster - 1)
        first = rng.randint(1, cast - 2)
        second = rng.randint(1, cast - first - 1)
        votes = rng.sample([first, second, cast - first - second], 3)
        scenario = Election(cluster, (votes[0], votes[1], votes[2]), asked=rng.randrange(3))
        return scenario if 1 <= _missing(scenario) <= cluster - cast else None

    def stem(self, s: Election) -> str:
        a, b, c = s.votes
        return (
            f"A Raft cluster has {s.cluster} servers. Candidates A, B and C hold {a}, {b} and {c} votes "
            f"in one term, their own included; the other servers have not voted. "
            f"How many more votes does candidate {LABELS[s.asked]} need to become leader?"
        )

    def correct(self, s: Election) -> str:
        return str(_missing(s))

    def mistakes(self, s: Election) -> list[str]:
        own, cast = s.votes[s.asked], sum(s.votes)
        listed = [
            cast // 2 + 1 - own,
            s.needed,
            s.cluster - own,
            _missing(s) + 1,
            max(s.votes) - own + 1,
            s.cluster // 2 - own,
        ]
        return [str(m) for m in listed if m > 0]

    def explanation(self, s: Election) -> str:
        return f"{self._steps(s)} {source_line(self.citation)}"

    def _steps(self, s: Election) -> str:
        a, b, c = s.votes
        return (
            f"{RULE} Inputs: {s.cluster} servers, votes {a}, {b} and {c}. "
            f"Step 1: the majority of {s.cluster} servers is {s.cluster} // 2 + 1 = {s.needed}. "
            f"Step 2: candidate {LABELS[s.asked]} holds {s.votes[s.asked]}. "
            f"Step 3: {s.needed} - {s.votes[s.asked]} = {_missing(s)}. "
            f"Result: {_missing(s)} more vote{'' if _missing(s) == 1 else 's'}."
        )
