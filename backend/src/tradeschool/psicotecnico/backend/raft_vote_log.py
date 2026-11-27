# SPDX-License-Identifier: AGPL-3.0-only
"""`raft-vote-log`: which candidate log a Raft voter does not deny its vote for."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code
from tradeschool.psicotecnico.backend.source_line import source_line
from tradeschool.psicotecnico.item import Params

Log = tuple[int, ...]

RULE = (
    "Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. "
    "Raft compares the last entries of the two logs: the later last term is more up-to-date, "
    "and with the same last term the longer log is."
)
OLDER_LONGER = "longer log, older last term"
SAME_SHORTER = "same last term, shorter"
OLDER_SAME_LENGTH = "older last term, same length"


@dataclass(frozen=True)
class VoteScenario:
    voter: Log
    ahead: Log
    behind: tuple[tuple[str, Log], ...]


def more_up_to_date(first: Log, second: Log) -> bool:
    return (first[-1], len(first)) > (second[-1], len(second))


def mistake_logs(s: VoteScenario) -> dict[str, Log]:
    return dict(s.behind)


def _run(prefix: Log, term: int, length: int) -> Log:
    return (*prefix, *([term] * (length - len(prefix))))


def _render(log: Log) -> str:
    return code(f"[{', '.join(map(str, log))}]")


def _terms(log: Log) -> str:
    return f"last term {log[-1]}, length {len(log)}"


class RaftVoteLogGenerator(BackendGenerator[VoteScenario]):
    id: ClassVar[str] = "raft-vote-log"
    forms: ClassVar[tuple[str, ...]] = ("{}", "log {}", "the candidate log {}")
    citation: ClassVar[Citation] = Citation(
        "m08-l05",
        "paper-raft-dissertation#p40; paper-raft-dissertation#p42",
        confirmed="paper-raft-dissertation#p40; paper-raft-dissertation#p42",
    )

    def scenario_for(self, seed: int, level: int) -> VoteScenario:
        scenario = self.build(seed, Params(level)).facts["scenario"]
        assert isinstance(scenario, VoteScenario)
        return scenario

    def scenario(self, rng: random.Random, level: int) -> VoteScenario | None:
        term = rng.randint(3, 5)
        length = rng.randint(4, 6)
        prefix = tuple(sorted(rng.randint(1, term - 1) for _ in range(rng.randint(1, length - 3))))
        # Every log is the shared prefix plus a run of one term, so logs agreeing at an index agree before it.
        voter = _run(prefix, term, length)
        if level == 1:
            ahead = _run(prefix, term, length + rng.randint(1, 2))
            behind = (
                (SAME_SHORTER, _run(prefix, term, length - 1)),
                (OLDER_LONGER, _run(prefix, term - 1, length + 2)),
                (OLDER_SAME_LENGTH, _run(prefix, term - 1, length)),
            )
        else:
            ahead = _run(prefix, term + 1, length - rng.randint(1, 2))
            behind = (
                (SAME_SHORTER, _run(prefix, term, length - 1)),
                (OLDER_LONGER, _run(prefix, term - 1, length + 1)),
                (OLDER_SAME_LENGTH, _run(prefix, term - 1, length)),
            )
        return VoteScenario(voter, ahead, behind)

    def stem(self, s: VoteScenario) -> str:
        return (
            f"A Raft voter has not voted yet; its log has entry terms {_render(s.voter)}. "
            f"Candidates ask for its vote with these logs. "
            f"For which log does it NOT deny the vote because of the log?"
        )

    def correct(self, s: VoteScenario) -> str:
        return _render(s.ahead)

    def mistakes(self, s: VoteScenario) -> list[str]:
        return [_render(log) for _, log in s.behind]

    def explanation(self, s: VoteScenario) -> str:
        refuted = " ".join(
            f"Step {n}: {_render(log)} has {_terms(log)}: {name}, so the voter's log is more up-to-date "
            f"and it denies."
            for n, (name, log) in enumerate(s.behind, start=3)
        )
        return (
            f"{RULE} Inputs: voter log {_render(s.voter)}. "
            f"Step 1: the voter has {_terms(s.voter)}. "
            f"Step 2: candidate {_render(s.ahead)} has {_terms(s.ahead)}, so the voter's log is not more "
            f"up-to-date and it does not deny. "
            f"{refuted} Result: {_render(s.ahead)}. {source_line(self.citation)}"
        )
