# SPDX-License-Identifier: AGPL-3.0-only
"""The backend-in-depth generators (requirements 6.3) and the citations their module sessions still owe."""

from __future__ import annotations

from tradeschool.psicotecnico.backend.base import Citation, CitedGenerator
from tradeschool.psicotecnico.backend.capacity import CapacityGenerator
from tradeschool.psicotecnico.backend.circuit_breaker import CircuitBreakerGenerator
from tradeschool.psicotecnico.backend.composite_index import CompositeIndexGenerator
from tradeschool.psicotecnico.backend.consistent_hashing import ConsistentHashingGenerator
from tradeschool.psicotecnico.backend.heap_contents import HeapContentsGenerator
from tradeschool.psicotecnico.backend.isolation_anomaly import IsolationAnomalyGenerator
from tradeschool.psicotecnico.backend.kafka_offsets import KafkaOffsetsGenerator
from tradeschool.psicotecnico.backend.logical_clocks import LogicalClocksGenerator
from tradeschool.psicotecnico.backend.loop_complexity import LoopComplexityGenerator
from tradeschool.psicotecnico.backend.lru_cache import LruCacheGenerator
from tradeschool.psicotecnico.backend.quorum import QuorumGenerator
from tradeschool.psicotecnico.backend.rate_limiter import RateLimiterGenerator
from tradeschool.psicotecnico.backend.retry_backoff import RetryBackoffGenerator

BACKEND_GENERATORS: dict[str, CitedGenerator] = {
    generator.id: generator
    for generator in (
        CapacityGenerator(),
        QuorumGenerator(),
        RateLimiterGenerator(),
        CircuitBreakerGenerator(),
        RetryBackoffGenerator(),
        LogicalClocksGenerator(),
        KafkaOffsetsGenerator(),
        IsolationAnomalyGenerator(),
        CompositeIndexGenerator(),
        ConsistentHashingGenerator(),
        LruCacheGenerator(),
        HeapContentsGenerator(),
        LoopComplexityGenerator(),
    )
}


def unfilled_citations() -> list[tuple[str, Citation]]:
    """The generators whose citation a module session has not confirmed yet."""
    return [(gid, g.citation) for gid, g in BACKEND_GENERATORS.items() if g.citation.unfilled]
