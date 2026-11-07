# SPDX-License-Identifier: AGPL-3.0-only
"""Splitting a count by weights, exactly, so the exam's type mix is the index's."""

from __future__ import annotations

from collections.abc import Sequence


def apportion(weights: Sequence[int], total: int) -> list[int]:
    """`total` split in proportion to `weights` by largest remainder; ties go to the earlier weight."""
    whole = sum(weights)
    shares = [total * w for w in weights]
    counts = [share // whole for share in shares]
    remainders = sorted(range(len(weights)), key=lambda i: (-(shares[i] % whole), i))
    for i in remainders[: total - sum(counts)]:
        counts[i] += 1
    return counts
