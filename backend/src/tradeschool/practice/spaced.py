# SPDX-License-Identifier: AGPL-3.0-only
"""The `spaced` practice order: unseen questions, then failed ones as they fall due, then the rest."""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timedelta

from tradeschool.practice.order import Rand

#: Days until a failed question returns, by correct answers in a row since its last failure.
RETURN_AFTER_DAYS = (1, 3, 7, 15, 30)


@dataclass(frozen=True)
class Answer:
    at: datetime
    correct: bool


def due_at(answers: Sequence[Answer]) -> datetime | None:
    """When a failed question returns: its latest answer plus the step for the correct run that follows
    its last failure (a new failure resets the run); None when it never failed."""
    ordered = sorted(answers, key=lambda answer: answer.at)
    if all(answer.correct for answer in ordered):
        return None
    run = 0
    for answer in reversed(ordered):
        if not answer.correct:
            break
        run += 1
    step = RETURN_AFTER_DAYS[min(run, len(RETURN_AFTER_DAYS) - 1)]
    return ordered[-1].at + timedelta(days=step)


def spaced_order[Q: Hashable](
    question_ids: Sequence[Q],
    history: Mapping[Q, Sequence[Answer]],
    now: datetime,
    count: int | None,
    rand: Rand,
) -> list[Q]:
    """Unseen questions in random order; then the failed ones due by `now`, most overdue first; then
    every other seen question, the longest unanswered first."""
    unseen = [qid for qid in question_ids if not history.get(qid)]
    seen = [qid for qid in question_ids if history.get(qid)]
    due = {qid: when for qid in seen if (when := due_at(history[qid])) is not None and when <= now}
    rest = [qid for qid in seen if qid not in due]
    ordered = (
        sorted(unseen, key=lambda _: rand.random())
        + sorted(due, key=lambda qid: due[qid])
        + sorted(rest, key=lambda qid: max(answer.at for answer in history[qid]))
    )
    return ordered if count is None else ordered[:count]
