<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# Programme — Backend Engineering in Depth

Locked in session S0 (2026-11-13) from section 9 of `docs/backend-in-depth-course-requirements.md` v1.1,
copied literally. Each bullet carries a stable id `<subsection>.<letter>` and its class mark: `[J]` for an
entry the programme marks (J) (and every bullet of module 12, which section 9 declares all J), `[F]` otherwise.
`[F]` is the programme's mark, not the final class: the source coverage report
(`docs/backend-verification/s0/source-coverage.md`) may turn an `[F]` bullet into X, J or dropped.
Ids are permanent; a later programme change appends ids and never renumbers.


This is the programme the scope and coverage audits use. S0 copies it literally to `content/backend-in-depth/programme.md`. Entries marked (J) are judgement by nature.

### Module 01 — Pragmatic software design and patterns

- **1.1 Design principles, pragmatism and data-oriented programming**
  - `1.1.a` [F] SOLID applied with judgement: cohesion, coupling and the limits of abstraction.
  - `1.1.b` [J] DRY, YAGNI and KISS: when to tolerate duplication instead of abstracting early. (J)
  - `1.1.c` [F] Law of Demeter, composition over inheritance, immutability in the domain.
  - `1.1.d` [F] Data-oriented programming in modern Java: algebraic domain modelling with records, sealed classes, pattern matching for switch and record patterns.
- **1.2 GoF patterns in modern backend code**
  - `1.2.a` [F] Creational: Factory Method, Abstract Factory, Builder (invariants validated at construction).
  - `1.2.b` [F] Structural: Adapter, Decorator, Facade, Proxy, applied to HTTP clients, caches and persistence layers.
  - `1.2.c` [F] Behavioural: Strategy, Observer, Template Method, Command, Chain of Responsibility, State.
- **1.3 Application architecture and modular evolution**
  - `1.3.a` [F] Hexagonal architecture (ports and adapters) and pragmatic Clean Architecture in Spring Boot.
  - `1.3.b` [J] Modular monolith versus microservices: context boundaries (Spring Modulith) and when to avoid the cost of distribution. (J)
  - `1.3.c` [F] Architectural fitness functions: automated architecture tests with ArchUnit against layer violations and dependency cycles.
  - `1.3.d` [F] Tactical domain modelling: aggregates, value objects, domain events.
- **1.4 Auditing and defending AI-assisted code**
  - `1.4.a` [J] Review checklist for assistant-generated code: unnecessary dependencies, broken encapsulation, leaky abstractions, hidden debt. (J)
  - `1.4.b` [F] Subtle failures typical of generated Java/Spring code: `@Transactional` on self-invocation, blocking `ForkJoinPool.commonPool()` from `CompletableFuture`, broken interrupt handling.
  - `1.4.c` [J] Explaining and defending each design decision in a take-home review. (J)

### Module 02 — Algorithms and data structures

- **2.1 Complexity and Java collections internals**
  - `2.1.a` [F] Asymptotic notation, amortised analysis, space complexity.
  - `2.1.b` [F] Internals of `ArrayList`, `LinkedList`, `ArrayDeque`, `HashMap` (collisions, treeification, resizing), `LinkedHashMap`, `TreeMap`, `PriorityQueue`.
  - `2.1.c` [F] The `equals` / `hashCode` / `compareTo` contracts and their effect on collections.
- **2.2 Arrays, strings and hashing**
  - `2.2.a` [F] Two pointers, sliding window, prefix sums, counting with maps.
  - `2.2.b` [F] Binary search over arrays and over the answer space.
  - `2.2.c` [F] Sorting: classic algorithms, stability, and what Java uses in each case.
  - `2.2.d` [F] Interval problems: merging, overlaps, sweep line.
- **2.3 Linear structures and trees**
  - `2.3.a` [F] Linked lists (fast and slow pointers, reversal), stacks, queues, monotonic stack.
  - `2.3.b` [F] Binary trees and BSTs: recursive and iterative traversals, lowest common ancestor, validation.
  - `2.3.c` [F] Heaps and top-K problems; tries for prefixes.
- **2.4 Graphs**
  - `2.4.a` [F] Representations, BFS and DFS, connected components, cycle detection.
  - `2.4.b` [F] Topological sort, union-find, shortest paths (Dijkstra).
  - `2.4.c` [F] Grids as implicit graphs.
- **2.5 Algorithm design techniques**
  - `2.5.a` [F] Recursion and backtracking: subsets, permutations, pruning.
  - `2.5.b` [F] Dynamic programming: state definition, memoisation versus tabulation, common patterns (knapsack, subsequences, grids).
  - `2.5.c` [F] Greedy algorithms and when they are correct.
  - `2.5.d` [F] Basic bit manipulation.
- **2.6 Design structures common in interviews**
  - `2.6.a` [F] LRU and LFU caches, in-memory rate limiter, iterator over nested structures, running median.
- **2.7 Pattern recognition**
  - `2.7.a` [F] Given a problem statement: identify the pattern, the data structure and the complexity of the naive and the optimal solution.

### Module 03 — Modern JVM, concurrency and performance

- **3.1 JVM internals, memory management and cloud efficiency**
  - `3.1.a` [F] Memory areas: stack, heap, metaspace; escape analysis and TLABs.
  - `3.1.b` [F] Modern collectors: how G1 and generational ZGC work and are tuned (latency versus throughput).
  - `3.1.c` [F] Diagnosing memory leaks; reading heap dumps and thread dumps.
  - `3.1.d` [F] Start-up time and footprint on Kubernetes: AppCDS and Project Leyden, Spring Boot AOT, GraalVM Native Image and their trade-offs.
- **3.2 Classic concurrency and the Java Memory Model**
  - `3.2.a` [F] Visibility, atomicity and ordering: `volatile`, happens-before, `Atomic*` classes.
  - `3.2.b` [F] `CompletableFuture` (composition with a dedicated executor, exception handling), `ExecutorService`, `ReentrantLock`, `StampedLock`, `Semaphore`.
  - `3.2.c` [F] Concurrent collections (`ConcurrentHashMap`, `CopyOnWriteArrayList`, blocking queues); deadlocks, livelocks and race conditions.
- **3.3 Project Loom: virtual threads, structured concurrency and scoped values**
  - `3.3.a` [F] Virtual threads (JEP 444): carrier and virtual threads, scheduling, and differences from reactive programming.
  - `3.3.b` [F] Pinning and its evolution (JEP 491): `synchronized` and native calls in Java 21 versus Java 24 and later; sizing connection pools; limiting concurrency with semaphores.
  - `3.3.c` [F] Structured concurrency (JEP 505 and its state in the pinned version): `StructuredTaskScope.open()` and `Joiner` policies, cancellation, prevention of thread leaks; how the API changed between previews.
  - `3.3.d` [F] Scoped values (JEP 506) as a replacement for `ThreadLocal` in context propagation.
- **3.4 Profiling, benchmarking and measuring performance**
  - `3.4.a` [F] Java Flight Recorder and JDK Mission Control: events, continuous recording, overhead.
  - `3.4.b` [F] CPU and allocation profiling with async-profiler; reading flame graphs; safepoint bias.
  - `3.4.c` [F] Microbenchmarks with JMH: warm-up, dead-code elimination, constant folding, `Blackhole`, forks.
  - `3.4.d` [F] Measuring latency: percentiles versus means, histograms, coordinated omission.
  - `3.4.e` [J] Method: hypothesis, measurement, single change, verification; when not to optimise. (J)

### Module 04 — Kotlin for Java developers

- **4.1 Type system and null safety**
  - `4.1.a` [F] Nullable types, safe calls, the Elvis operator, smart casts, `lateinit`.
  - `4.1.b` [F] Platform types in Java interoperability and nullability annotations.
  - `4.1.c` [F] Generics: declaration-site variance (`in` / `out`) and reified type parameters.
- **4.2 Idiomatic Kotlin**
  - `4.2.a` [F] `data class`, `sealed class` and `sealed interface`, `object`, `value class`, exhaustive `when`.
  - `4.2.b` [F] Extension functions and scope functions (`let`, `run`, `apply`, `also`, `with`).
  - `4.2.c` [F] Read-only collection interfaces, sequences versus collections, delegation with `by`.
  - `4.2.d` [F] Comparison with modern Java records, sealed classes and pattern matching (see 1.1).
- **4.3 Coroutines**
  - `4.3.a` [F] `suspend` functions, continuations, and what the compiler generates.
  - `4.3.b` [F] Structured concurrency: `CoroutineScope`, `launch` and `async`, `Job` versus `SupervisorJob`, cooperative cancellation, exception propagation.
  - `4.3.c` [F] Dispatchers, context switching, blocking calls inside coroutines.
  - `4.3.d` [F] `Flow`: cold flows, operators, `StateFlow` and `SharedFlow`, backpressure.
  - `4.3.e` [F] Coroutines versus virtual threads (see 3.3).
- **4.4 Kotlin in Spring Boot**
  - `4.4.a` [F] Compiler plugins (`all-open`, `no-arg`) and why Spring and JPA need them.
  - `4.4.b` [F] JPA entities in Kotlin: risks of `data class`, equality, lazy loading.
  - `4.4.c` [F] Controllers and repositories with `suspend` functions; configuration DSLs.
  - `4.4.d` [F] Testing: MockK and coroutine tests with virtual time.
- **4.5 Interoperability and migration from Java**
  - `4.5.a` [F] Calls in both directions: `@JvmStatic`, `@JvmOverloads`, `@Throws`, unchecked exceptions.
  - `4.5.b` [J] Incremental migration of a Java code base and common mistakes. (J)

### Module 05 — Spring Framework and Spring Boot internals

- **5.1 IoC container and bean lifecycle**
  - `5.1.a` [F] `BeanDefinition`, `BeanFactory` versus `ApplicationContext`, scopes, initialisation order.
  - `5.1.b` [F] Lifecycle: instantiation, injection, `BeanPostProcessor`, initialisation and destruction callbacks.
  - `5.1.c` [F] Constructor versus field injection, circular dependencies, `@Lazy`, `@Primary`, `@Qualifier`.
  - `5.1.d` [F] `@Configuration` (full versus lite mode), `@Conditional`, profiles.
- **5.2 Spring Boot auto-configuration**
  - `5.2.a` [F] How auto-configurations are discovered and ordered; `@ConditionalOn…`; the condition evaluation report.
  - `5.2.b` [F] Starters, `@ConfigurationProperties`, precedence of externalised configuration.
  - `5.2.c` [F] Writing an auto-configuration and an internal starter.
- **5.3 AOP and proxies**
  - `5.3.a` [F] JDK dynamic proxies versus CGLIB; why self-invocation bypasses the proxy.
  - `5.3.b` [F] Limits: `final` and private methods, calls from constructors.
  - `5.3.c` [F] Proxy-based annotations: `@Transactional`, `@Async`, `@Cacheable`, `@Retryable`, and their ordering.
- **5.4 Transaction management**
  - `5.4.a` [F] `PlatformTransactionManager`, resource synchronisation, thread binding.
  - `5.4.b` [F] Propagation, isolation, `readOnly`, timeouts.
  - `5.4.c` [F] Rollback rules: checked versus unchecked exceptions, `rollbackFor`.
  - `5.4.d` [F] `@TransactionalEventListener` phases; transactions with virtual threads, `@Async` and reactive code.
- **5.5 Web layer**
  - `5.5.a` [F] Request path: filters, `DispatcherServlet`, handler mappings, interceptors, argument resolution, message converters.
  - `5.5.b` [F] Validation, `@ControllerAdvice`, error model.
  - `5.5.c` [F] Spring MVC versus WebFlux; MVC on virtual threads.
  - `5.5.d` [F] HTTP clients: `RestClient`, `WebClient`, declarative interfaces; timeouts and connection pools.
- **5.6 Spring Security**
  - `5.6.a` [F] Architecture: `DelegatingFilterProxy`, `FilterChainProxy`, `SecurityFilterChain`; filter order.
  - `5.6.b` [F] Authentication (`AuthenticationManager`, `AuthenticationProvider`) and `SecurityContext`; propagation across threads.
  - `5.6.c` [F] Request-level and method-level authorisation (`@PreAuthorize`).
  - `5.6.d` [F] Resource server with JWT: validation, mapping claims to authorities, several issuers for multi-tenancy.
- **5.7 Spring Data and JPA**
  - `5.7.a` [F] Repositories: derived queries, `@Query`, projections, specifications.
  - `5.7.b` [F] Persistence context, entity states, dirty checking, flush, `open-in-view`.
  - `5.7.c` [F] Auditing, optimistic locking, batching (see 6.3).
- **5.8 Operating and testing Spring Boot applications**
  - `5.8.a` [F] Actuator: health groups, metrics, management endpoints.
  - `5.8.b` [F] Start-up and shutdown events; graceful shutdown.
  - `5.8.c` [F] Test slices (`@WebMvcTest`, `@DataJpaTest`), `@SpringBootTest`, test-context caching, `@ServiceConnection` with Testcontainers.

### Module 06 — Relational persistence, transactions and SQL optimisation

- **6.1 ACID, MVCC and PostgreSQL internals**
  - `6.1.a` [F] MVCC and write-ahead logging in PostgreSQL.
  - `6.1.b` [F] Operating cost of MVCC: dead tuples, autovacuum tuning, table and index bloat, transaction ID wraparound.
  - `6.1.c` [F] Isolation levels of the SQL standard and their real behaviour in PostgreSQL: Read Uncommitted, Read Committed, Repeatable Read (snapshot isolation), Serializable (SSI).
- **6.2 Concurrency anomalies, locking and connection pooling**
  - `6.2.a` [F] Dirty reads, non-repeatable reads, phantom reads, lost updates, write skew.
  - `6.2.b` [F] Optimistic locking (`@Version`) versus pessimistic locking (`SELECT … FOR UPDATE`, `FOR SHARE`, queues with `SKIP LOCKED`).
  - `6.2.c` [F] Connections at scale: sizing HikariCP; PgBouncer transaction pooling versus session pooling.
- **6.3 Advanced indexing, partitioning and SQL optimisation**
  - `6.3.a` [F] B-tree, hash, GIN, GiST; partial, composite and covering indexes (`INCLUDE`).
  - `6.3.b` [F] Reading plans with `EXPLAIN (ANALYZE, BUFFERS)`.
  - `6.3.c` [F] Offset versus keyset pagination; declarative partitioning by range and hash.
  - `6.3.d` [F] ORM anti-patterns: N+1, fetch joins, DTO projections, session management, write batching.
- **6.4 Zero-downtime schema evolution**
  - `6.4.a` [F] Expand and contract with Flyway or Liquibase, `CREATE INDEX CONCURRENTLY`, batched backfill, backward compatibility.

### Module 07 — Networking and API design

- **7.1 Networking fundamentals for backend engineers**
  - `7.1.a` [F] TCP: connection set-up and teardown, flow and congestion control, keep-alive, head-of-line blocking, `TIME_WAIT`.
  - `7.1.b` [F] DNS: resolution, TTL, caches including the JVM's, service discovery in Kubernetes.
  - `7.1.c` [F] TLS 1.3: handshake, certificates and chain of trust, SNI, ALPN, mTLS.
  - `7.1.d` [F] Connect, read and total timeouts; HTTP connection pools and stale connections.
- **7.2 HTTP/1.1, HTTP/2 and HTTP/3**
  - `7.2.a` [F] Multiplexing, streams, header compression, and what each version solves.
  - `7.2.b` [F] QUIC and HTTP/3.
  - `7.2.c` [F] WebSockets and Server-Sent Events.
- **7.3 Load balancing and the edge**
  - `7.3.a` [F] L4 versus L7 balancers, algorithms, health checks, connection draining.
  - `7.3.b` [F] Reverse proxies, API gateways, Ingress and Gateway API in Kubernetes.
  - `7.3.c` [F] CDNs and edge caching.
- **7.4 HTTP semantics**
  - `7.4.a` [F] Safe and idempotent methods; status codes.
  - `7.4.b` [F] HTTP caching: `Cache-Control`, `ETag`, conditional requests, `Vary`.
  - `7.4.c` [F] Content negotiation and compression.
- **7.5 REST API design**
  - `7.5.a` [F] Resource modelling and naming.
  - `7.5.b` [F] Idempotency keys on `POST`, safe retries, server-side deduplication.
  - `7.5.c` [F] Optimistic concurrency with `ETag` and `If-Match`.
  - `7.5.d` [F] Pagination, filtering, sorting, partial responses.
  - `7.5.e` [F] Error model: Problem Details; validation errors.
  - `7.5.f` [F] Long-running operations, batch operations, webhooks (signing, retries, ordering).
  - `7.5.g` [F] Rate limiting as seen by the client: `429`, `Retry-After`, quota headers.
  - `7.5.h` [F] OpenAPI and contract-first design.
- **7.6 gRPC, GraphQL and asynchronous APIs**
  - `7.6.a` [F] gRPC and Protocol Buffers: call types, deadlines, cancellation, status codes, message evolution rules.
  - `7.6.b` [F] GraphQL: schema, resolvers, the N+1 problem.
  - `7.6.c` [F] AsyncAPI for event contracts (see 8.2).
  - `7.6.d` [J] Choosing between REST, gRPC, GraphQL and messaging. (J)
- **7.7 API evolution and governance**
  - `7.7.a` [F] Compatible and breaking changes; versioning strategies and their costs.
  - `7.7.b` [F] Tolerant reader, deprecation policy, deprecation and sunset headers.
  - `7.7.c` [J] API style guides and cross-team design review. (J)

### Module 08 — Distributed systems, messaging and resilience

- **8.1 Fundamentals of distributed systems**
  - `8.1.a` [F] CAP and PACELC applied to storage decisions.
  - `8.1.b` [F] Consistency models: linearizable, sequential, causal, eventual; read-your-writes and monotonic reads.
  - `8.1.c` [F] Time: physical clocks and NTP versus Lamport and vector clocks.
- **8.2 Event-driven architecture (Kafka and RabbitMQ)**
  - `8.2.a` [F] Kafka internals: partitions, replication factor, in-sync replicas, `acks`, consumer groups, offsets, cooperative rebalancing.
  - `8.2.b` [F] Contracts and ordering: Schema Registry compatibility modes, partition keys, hot partitions.
  - `8.2.c` [F] Error handling: dead-letter topics, poison pills, non-blocking retries, consumer lag.
  - `8.2.d` [F] Delivery semantics and idempotent consumers.
- **8.3 Distributed transactions without 2PC**
  - `8.3.a` [F] The dual-write problem.
  - `8.3.b` [F] Transactional outbox: polling with `SKIP LOCKED` versus change data capture with Debezium.
  - `8.3.c` [F] Sagas: orchestration versus choreography, compensating actions, semantic isolation.
- **8.4 Stability, resilience and traffic control**
  - `8.4.a` [F] Circuit breaker: states, sliding windows, slow-call thresholds, fallbacks with Resilience4j.
  - `8.4.b` [F] Retries with exponential backoff and full jitter.
  - `8.4.c` [F] Bulkheads, rate limiting (token bucket, leaky bucket, sliding window), load shedding, timeout propagation, backpressure.
- **8.5 Consensus and coordination**
  - `8.5.a` [F] Partial failures, asynchronous networks, failure detectors, process pauses.
  - `8.5.b` [F] Raft: leader election, terms, log replication, commit index, membership changes, snapshots. Paxos as a reference.
  - `8.5.c` [F] Quorums, split brain and leader election in practice: ZooKeeper, etcd, KRaft.
  - `8.5.d` [F] Distributed locks and leases; fencing tokens.
  - `8.5.e` [F] Two-phase commit: how it works and why it blocks.
  - `8.5.f` [F] Gossip protocols and cluster membership.
- **8.6 Event sourcing and CQRS**
  - `8.6.a` [F] The event log as source of truth, aggregate rehydration, snapshots, optimistic concurrency on the event store.
  - `8.6.b` [F] CQRS: write and read models, projections, eventual consistency of read models.
  - `8.6.c` [F] Event evolution: versioning, upcasting, compensating events.
  - `8.6.d` [F] Projections in production: replay, rebuild without downtime, idempotency, tracking position.
  - `8.6.e` [F] Axon Framework: command bus, aggregates, event processors (subscribing versus streaming), sagas.
  - `8.6.f` [F] Personal data in an immutable log: crypto-shredding and erasure.
  - `8.6.g` [J] When not to use event sourcing. (J)
- **8.7 Stream processing**
  - `8.7.a` [F] Batch versus stream; event time versus processing time.
  - `8.7.b` [F] Tumbling, hopping, sliding and session windows; watermarks, late data, grace period.
  - `8.7.c` [F] Stateful processing: state stores, changelog topics, recovery.
  - `8.7.d` [F] Kafka Streams: KStream and KTable, joins, co-partitioning, repartition topics.
  - `8.7.e` [F] Exactly-once processing: idempotent producers and Kafka transactions.
  - `8.7.f` [F] Apache Flink as a reference: checkpoints, savepoints, backpressure.

### Module 09 — System design and data scalability

- **9.1 A step-by-step framework for system design**
  - `9.1.a` [F] Scope, functional and non-functional requirements (SLAs and SLOs, p95 and p99 latency, availability).
  - `9.1.b` [F] Back-of-the-envelope capacity estimation.
  - `9.1.c` [F] API contracts and choice of storage engine.
  - `9.1.d` [F] High-level architecture and end-to-end data flow.
- **9.2 Data scalability: replication, sharding and caching**
  - `9.2.a` [J] When to scale up, add replicas, partition locally, or shard. (J)
  - `9.2.b` [F] Replication: single-leader, multi-leader, leaderless with quorums; handling replication lag.
  - `9.2.c` [F] Sharding: range versus hash, consistent hashing with virtual nodes, hot keys, local versus global secondary indexes, cross-shard joins, rebalancing.
  - `9.2.d` [F] Distributed caching: cache-aside, read-through and write-through, write-behind, invalidation, cache stampede, hot keys.
- **9.3 Multi-tenant architecture and data isolation**
  - `9.3.a` [F] Database per tenant, schema per tenant, shared tables with row-level security.
  - `9.3.b` [F] Noisy neighbours: per-tenant quotas, fair queuing, bulkheads.
- **9.4 Blueprints**
  - `9.4.a` [F] Distributed rate limiter.
  - `9.4.b` [F] Booking and inventory engine under high contention.
  - `9.4.c` [F] Multi-channel notification platform.
  - `9.4.d` [F] Telemetry and event ingestion pipeline.
  - `9.4.e` [F] URL shortener and distributed ID generation.
  - `9.4.f` [F] Search and autocomplete.
  - `9.4.g` [F] Agentic diagnostics platform and enterprise AI gateway.
- **9.5 Storage engines and non-relational databases**
  - `9.5.a` [F] LSM-trees versus B-trees: memtable, SSTables, compaction, Bloom filters, write, read and space amplification.
  - `9.5.b` [F] Row-oriented versus columnar storage; OLTP versus OLAP.
  - `9.5.c` [F] Redis internals: data structures, single-threaded execution, RDB and AOF persistence, eviction policies, Sentinel and Cluster.
  - `9.5.d` [F] Elasticsearch internals: inverted index, segments and merges, refresh, shards and replicas, analysers, BM25, deep pagination.
  - `9.5.e` [J] Choosing between document, key-value, wide-column and time-series stores. (J)

### Module 10 — Platform, observability, security and AI integration

- **10.1 Observability of distributed systems**
  - `10.1.a` [F] Structured logs with correlation, metrics (Micrometer, Prometheus, RED and USE), distributed tracing with OpenTelemetry.
  - `10.1.b` [F] Actionable alerts based on SLOs and error budgets.
- **10.2 Security, identity and compliance**
  - `10.2.a` [F] Zero-trust between services: mTLS, default-deny NetworkPolicies, dynamic secrets.
  - `10.2.b` [F] OAuth 2.0 and OpenID Connect flows, JWT handling, key rotation, RBAC and ABAC.
  - `10.2.c` [F] Privacy by design, encryption in transit and at rest, immutable audit, regulated environments (NEN 7510, GDPR).
- **10.3 FinOps and infrastructure efficiency**
  - `10.3.a` [F] Kubernetes `requests` and `limits`, HPA and KEDA, inter-zone traffic cost, telemetry retention, storage selection.
- **10.4 Platform engineering and architecture of systems with AI**
  - `10.4.a` [J] Golden paths, global standards, threat-modelling templates. (J)
  - `10.4.b` [J] Deterministic state machines versus agentic loops. (J)
  - `10.4.c` [F] LLM integration: permission-aware RAG, Model Context Protocol with least privilege, cost control through AI gateways.
  - `10.4.d` [F] Security and reliability: indirect prompt injection, no leakage of production data, deterministic evals in CI.
- **10.5 Kubernetes in production and continuous delivery**
  - `10.5.a` [F] Pod lifecycle: liveness, readiness and start-up probes, and common mistakes.
  - `10.5.b` [F] Graceful shutdown: `SIGTERM`, `preStop`, `terminationGracePeriodSeconds`, connection draining, Spring Boot and Kafka consumers.
  - `10.5.c` [F] Availability during change: rolling updates, PodDisruptionBudgets, anti-affinity, zone spread.
  - `10.5.d` [F] Deployment strategies: rolling, blue/green, canary; progressive delivery and rollback.
  - `10.5.e` [F] Feature flags.
  - `10.5.f` [F] GitOps and CI/CD pipeline design: trunk-based development, immutable artefacts, promotion.
  - `10.5.g` [F] Database migrations inside a deployment (see 6.4).
  - `10.5.h` [F] DORA metrics.
- **10.6 Application security and supply chain**
  - `10.6.a` [F] OWASP Top 10 and OWASP API Security Top 10 applied to Java and Spring.
  - `10.6.b` [F] Broken access control: IDOR and BOLA, cross-tenant leaks, mass assignment.
  - `10.6.c` [F] Injection, SSRF, insecure deserialisation, path traversal.
  - `10.6.d` [F] HTTP surface: CORS, CSRF, security headers, input validation.
  - `10.6.e` [F] Secrets and sensitive data in logs, traces and dumps.
  - `10.6.f` [F] Supply chain: dependency analysis, SBOM, image signing, SLSA levels, reproducible builds.
  - `10.6.g` [F] Threat modelling with STRIDE.

### Module 11 — Code reading, debugging and testing

- **11.1 Java Streams, gatherers and collections in depth**
  - `11.1.a` [F] `flatMap`, composed comparators, `reduce`, `takeWhile` and `dropWhile`.
  - `11.1.b` [F] Collectors: multi-level `groupingBy`, `partitioningBy`, `toMap` with merge functions, `teeing`, custom collectors.
  - `11.1.c` [F] Stream gatherers (JEP 485): `windowFixed`, `windowSliding`, `fold`, `scan`.
  - `11.1.d` [F] Reading a pipeline: its result and its complexity.
- **11.2 Refactoring legacy code and reviewing AI-generated changes**
  - `11.2.a` [F] Code smells, hidden coupling, resource leaks, poor exception handling, concurrency errors.
  - `11.2.b` [F] Finding subtle production bugs in clean-looking code: races, money and time-zone precision, transaction leaks.
  - `11.2.c` [F] Safe extraction: extract method and class, introducing polymorphism, decoupling external dependencies.
- **11.3 Production debugging and incident triage**
  - `11.3.a` [F] Reading stack traces, correlating logs, p99 latency, connection-pool saturation, GC pauses and consumer lag to isolate a root cause.
- **11.4 Deterministic testing**
  - `11.4.a` [F] JUnit 5, Mockito and AssertJ: AAA, parameterised tests, injected `Clock`, edge cases.
  - `11.4.b` [F] Integration tests with Testcontainers.
- **11.5 Thinking aloud**
  - `11.5.a` [J] Clarifying edge cases first, stating complexity, justifying trade-offs as you go. (J)
- **11.6 Advanced testing and test strategy**
  - `11.6.a` [J] Shape of the suite and what to test at each level. (J)
  - `11.6.b` [F] Consumer-driven contract testing.
  - `11.6.c` [F] Property-based testing: properties, generators, shrinking.
  - `11.6.d` [F] Mutation testing.
  - `11.6.e` [F] Load testing: open and closed workload models, percentile targets, soak tests.
  - `11.6.f` [F] Flaky tests: causes and removal.
  - `11.6.g` [F] Chaos engineering: hypothesis, blast radius, fault injection.

### Module 12 — Staff-level technical leadership

Built only from public material (Tier C). Everything is class J and attributed.

- **12.1 Architecture documentation, decision making and governance**
  - `12.1.a` [J] ADRs and RFCs: context, options, trade-offs, consequences, mitigation.
  - `12.1.b` [J] Building consensus and influencing without authority.
  - `12.1.c` [J] Governing the development lifecycle when teams generate code with AI.
- **12.2 Remote work and asynchronous communication**
  - `12.2.a` [J] Clear written communication, asynchronous unblocking, living documentation, time-zone overlap.
- **12.3 Behavioural interviews: STAR and story archetypes**
  - `12.3.a` [J] The STAR method and its variants; quantifying results; separating your contribution from the team's.
  - `12.3.b` [J] What interviewers assess at Senior versus Staff level.
  - `12.3.c` [J] Six archetypes: critical migration, cross-team influence, incident response, technical conflict resolved with a simpler option, mentoring, failure and what changed afterwards.
  - `12.3.d` [J] A template for writing your own stories outside the course.
- **12.4 Cultural fit and product alignment**
  - `12.4.a` [J] Common questions from engineering managers, product managers and executives.
  - `12.4.b` [J] Questions to assess a company: technical maturity, autonomy, on-call, promotion, business stability.
- **12.5 Technical strategy and large migrations**
  - `12.5.a` [J] The Staff role: archetypes, scope versus Senior, low-visibility coordination work, choosing what to work on.
  - `12.5.b` [J] Published engineering career ladders and how to read them.
  - `12.5.c` [J] Technical strategy: diagnosis, policy, actions; vision and strategy documents.
  - `12.5.d` [J] Large migrations: strangler fig, branch by abstraction, parallel run, incremental data migration, completion criteria.
  - `12.5.e` [J] Build versus buy and technology evaluation.
  - `12.5.f` [J] Technical debt as a portfolio.
  - `12.5.g` [J] Estimation and risk in multi-quarter projects.
  - `12.5.h` [J] Deprecating and retiring systems and APIs.
