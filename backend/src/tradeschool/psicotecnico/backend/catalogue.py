# SPDX-License-Identifier: AGPL-3.0-only
"""The backend-in-depth generators (requirements 6.3) and the citations their module sessions still owe."""

from __future__ import annotations

from tradeschool.psicotecnico.backend.base import Citation, CitedGenerator
from tradeschool.psicotecnico.backend.capacity import CapacityGenerator
from tradeschool.psicotecnico.backend.circuit_breaker import CircuitBreakerGenerator
from tradeschool.psicotecnico.backend.composite_index import CompositeIndexGenerator
from tradeschool.psicotecnico.backend.conditional_request_outcome import ConditionalRequestOutcomeGenerator
from tradeschool.psicotecnico.backend.consistent_hashing import ConsistentHashingGenerator
from tradeschool.psicotecnico.backend.error_budget import ErrorBudgetGenerator
from tradeschool.psicotecnico.backend.graph_traversal import GraphTraversalGenerator
from tradeschool.psicotecnico.backend.hashmap_resize import HashMapResizeGenerator
from tradeschool.psicotecnico.backend.heap_contents import HeapContentsGenerator
from tradeschool.psicotecnico.backend.hpa_replicas import HpaReplicasGenerator
from tradeschool.psicotecnico.backend.http_freshness import HttpFreshnessGenerator
from tradeschool.psicotecnico.backend.http_method_properties import HttpMethodPropertiesGenerator
from tradeschool.psicotecnico.backend.isolation_anomaly import IsolationAnomalyGenerator
from tradeschool.psicotecnico.backend.kafka_offsets import KafkaOffsetsGenerator
from tradeschool.psicotecnico.backend.kafka_write_acceptance import KafkaWriteAcceptanceGenerator
from tradeschool.psicotecnico.backend.keyset_next_page import KeysetNextPageGenerator
from tradeschool.psicotecnico.backend.logical_clocks import LogicalClocksGenerator
from tradeschool.psicotecnico.backend.loop_complexity import LoopComplexityGenerator
from tradeschool.psicotecnico.backend.lru_cache import LruCacheGenerator
from tradeschool.psicotecnico.backend.partition_owner import PartitionOwnerGenerator
from tradeschool.psicotecnico.backend.property_source import PropertySourceGenerator
from tradeschool.psicotecnico.backend.proxy_annotation import ProxyAnnotationGenerator
from tradeschool.psicotecnico.backend.qos_class import QosClassGenerator
from tradeschool.psicotecnico.backend.quorum import QuorumGenerator
from tradeschool.psicotecnico.backend.raft_commit import RaftCommitIndexGenerator
from tradeschool.psicotecnico.backend.raft_election import RaftElectionVotesGenerator
from tradeschool.psicotecnico.backend.raft_vote_log import RaftVoteLogGenerator
from tradeschool.psicotecnico.backend.rate_limiter import RateLimiterGenerator
from tradeschool.psicotecnico.backend.retry_backoff import RetryBackoffGenerator
from tradeschool.psicotecnico.backend.rolling_update import RollingUpdateBoundsGenerator
from tradeschool.psicotecnico.backend.row_lock_conflict import RowLockConflictGenerator
from tradeschool.psicotecnico.backend.snowflake_layout import SnowflakeLayoutGenerator
from tradeschool.psicotecnico.backend.thread_pool_state import ThreadPoolStateGenerator
from tradeschool.psicotecnico.backend.topological_order import TopologicalOrderGenerator
from tradeschool.psicotecnico.backend.union_find_sets import UnionFindGenerator
from tradeschool.psicotecnico.backend.window_grace import WindowGraceGenerator
from tradeschool.psicotecnico.backend.xfast_probe import XFastProbeGenerator

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
        GraphTraversalGenerator(),
        TopologicalOrderGenerator(),
        UnionFindGenerator(),
        HashMapResizeGenerator(),
        ThreadPoolStateGenerator(),
        PartitionOwnerGenerator(),
        PropertySourceGenerator(),
        ProxyAnnotationGenerator(),
        RowLockConflictGenerator(),
        HttpFreshnessGenerator(),
        HttpMethodPropertiesGenerator(),
        KafkaWriteAcceptanceGenerator(),
        RaftElectionVotesGenerator(),
        RaftCommitIndexGenerator(),
        WindowGraceGenerator(),
        HpaReplicasGenerator(),
        RollingUpdateBoundsGenerator(),
        ErrorBudgetGenerator(),
        ConditionalRequestOutcomeGenerator(),
        KeysetNextPageGenerator(),
        QosClassGenerator(),
        RaftVoteLogGenerator(),
        SnowflakeLayoutGenerator(),
        XFastProbeGenerator(),
    )
}


def unfilled_citations() -> list[tuple[str, Citation]]:
    """The generators whose citation a module session has not confirmed yet."""
    return [(gid, g.citation) for gid, g in BACKEND_GENERATORS.items() if g.citation.unfilled]
