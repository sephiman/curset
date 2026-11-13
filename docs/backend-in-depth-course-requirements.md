# Backend Engineering in Depth — course requirements

Version 1.1 · 2026-11-12 · slug `backend-in-depth` · language: English only

This document is a **delta**. The base is `docs/age-administrativo-course-requirements.md`; the provenance and generator rules come from `docs/age-auxiliar-course-requirements.md`; the staged build comes from `docs/aeat-agentes-course-requirements.md`. Where this document is silent, the base applies. Where it conflicts, this document wins. `CLAUDE.md` and `docs/prose-voice.md` apply unchanged.

## 1. Purpose and scope

A self-paced course for a senior backend engineer who wants to get better at the job and reach Staff level. Interview preparation is one use of it, not its driver. There is no exam date, no call, and no official exam.

In scope: theory lessons, schemas, a multiple-choice bank, code-reading questions, runtime question generators, and system-design cases built from keyed questions.

Out of scope, by decision:

- Any exercise where the learner writes code. No in-platform editor, no companion kata repository.
- Free-text answers and any grading by a live model.
- Angular and frontend in general. Salary negotiation.
- Personal interview stories and any employer-internal system.
- The Android app. Courses `crypto-futures`, `age-administrativo-c1`, `age-auxiliar-c2`, `aeat-agentes-hacienda` and the Android bundle stay byte-identical in every round unless the round says otherwise.

## 2. What changes from an oposiciones course

| Oposiciones course | This course |
|---|---|
| Programme copied literally from the BOE | Programme is section 9 of this document, locked in S0 |
| Sources: consolidated legal texts | Sources: primary technical documentation (section 3) |
| Cite the version in force on exam day | Cite the **pinned version** in `versions.yaml` |
| Exam-style guide derived from official exams | Question style guide written in S0 from the rules in section 6 |
| Official-exam ledger and official-exam sets | None |
| «Lo que más cae» derived from official exams | «Key points»: a recap of the lesson's own verified facts; no claim about how often anything is asked |
| Presets with BOE scoring rules | Practice presets only (section 6.6) |
| Supuestos (`case`) | System-design cases (`case`), section 6.4 |
| Psychometric generators | Engineering generators, section 6.3 |
| Monthly legal-currency audit | Version audit, section 8 |
| Every sentence is a literal fact | Three content classes, section 4 |

## 3. Sources (session S0)

Claude Code finds and downloads every source. Plain fetch first; if the site refuses, Playwright. Each stored source records URL, retrieval date and sha256.

### 3.1 Tiers

**Tier A — primary, normative.** The only tier that can support a tested fact.

- Language and VM specifications, JEPs, official API documentation.
- Official reference documentation of each product, for the pinned version: PostgreSQL, Apache Kafka, Spring Framework, Spring Boot, Spring Security, Spring Data, Kotlin and kotlinx.coroutines, Kubernetes, Redis, Elasticsearch, Resilience4j, Axon Framework, Debezium, gRPC and Protocol Buffers, OpenTelemetry, Micrometer, Testcontainers, JUnit, Flyway, Liquibase, PgBouncer, HikariCP.
- IETF RFCs and equivalent standards (HTTP, TLS, QUIC, OAuth 2.0, JWT, Problem Details, OpenID Connect, OpenAPI, AsyncAPI).
- OWASP projects, SLSA, DORA publications from their own sites.
- Original papers when the authors or the publisher make them freely available (for example Raft, Lamport clocks, Dynamo).

**Tier B — books** (for example *Designing Data-Intensive Applications*, the GoF book). Cited by chapter for orientation only. Never stored in the repo, never extracted, never the only support of a tested fact.

**Tier C — public reference material.** Used for module 12 and for judgement content elsewhere: engineering career ladders and handbooks published by companies, books with an open online edition, and articles by identifiable authors on their own or their employer's site. Stored like Tier A when the licence allows. Everything taken from Tier C is class J (section 4).

Not sources: forums, Q&A sites, aggregators, anonymous blogs, tutorials, and any model output.

### 3.2 Files

- `versions.yaml` — the pinned version of each product: the latest stable release on the day S0 runs (for Java, the latest LTS). A fact that differs between versions names the version in the sentence ("since Java 24").
- `sources.yaml` — replaces `normativa.yaml`. Per source: id, tier, product, version, URL, retrieval date, sha256, local path, licence, and `extract_allowed: true | false`.
- Licence rule: when `extract_allowed` is false the "View solution" panel shows "no extract" with the reason and a link to the source. Nothing is quoted from it.
- **Anchors.** Each stored source is split into anchored sections (`source_id#anchor`) with their own sha256. Citations point at an anchor, and writers and verifiers load anchors, never whole sources.

### 3.3 Source coverage report

S0 ends with a table mapping every programme bullet in section 9 to at least one Tier A source, or marking it as class J with its Tier B/C source, or flagging it as "no primary source found". Nothing waits for a decision. Default rules, each use logged in the ledger:

- No Tier A source but an acceptable Tier B or C source: the bullet becomes class J.
- No acceptable source at all: the bullet is left out of the course and listed as dropped.
- The programme's wording disagrees with the documentation of the pinned version: the documentation wins and the lesson states the pinned behaviour.

## 4. Content classes

Every sentence of theory, every schema row and every question belongs to exactly one class.

**F — fact.** Verifiable against a stored Tier A source for the pinned version. Inline citation. Blind verification sentence by sentence by an agent that did not write it. Only F and X feed the bank and the generators.

**X — executable fact.** A claim about what a Java or Kotlin snippet prints, returns or throws. Verified by running the snippet on the pinned JDK at build time. The evidence is the snippet, the command and the sha256 of its output, stored with the question. X is limited to code that runs with the JDK and the Kotlin compiler alone. A claim that needs a database, a broker or any external service is not X: it must be F from documentation, or it is dropped.

**J — judgement.** Trade-offs, criteria, practices, career and communication advice. Rendered visibly different from facts and attributed to a named source in the text ("According to …"). Verification checks that the attribution is faithful, not that the judgement is true. J is never the key of a multiple-choice question.

All code shown in a lesson compiles and was run; a snippet that is deliberately broken says so and records the compiler or runtime error as its evidence.

## 5. Theory

One lesson per numbered subsection of the programme (68 lessons). Base rules apply: no length caps, glossary with terms that exist outside the course in the same sense, schemas (`::esquema`: table, decision tree, steps), blind verification, provenance.

Deltas:

- Schema rows are F facts with a citation. Literal wording of the source is not required.
- Each lesson ends with «Key points», restating F and X facts already in the lesson.
- Glossary terms use the wording of the cited source.
- Every lesson section declares the programme bullet ids it covers in its metadata. The **scope** audit (every section maps to a bullet), the **coverage** audit (every bullet has a section) and the **version** audit (every citation resolves to an anchor of the pinned version) are scripts, not model passes.

## 6. Questions

### 6.1 Static bank

Four options, one correct, explanation, citation, and extract when the licence allows. A question that fails verification is discarded, not repaired.

Question types:

- Concept and scenario questions keyed to an F fact.
- Code-reading questions keyed to an X fact: what this prints, which line holds the bug, what the complexity is, which refactoring preserves behaviour.

Target: about 1,500 at publication. The quota per lesson is computed by script from its count of F and X facts (roughly 15 to 30, minimum 10). Extracts are checked by script: an extract must be a literal substring of the cited anchor.

Style guide (`docs/backend-question-style.md`, written in S0): explanations never refer to options by letter; the key is not systematically the longest option; each distractor is a real misconception that a cited fact contradicts; code in questions and options is formatted as code.

### 6.2 Build-time variant families

A template plus parameters produces many code-reading questions. A script instantiates each variant, runs it on the pinned JDK and records the output as the key. Distractors are computed by script from typical mistakes (off-by-one, wrong evaluation order, integer overflow ignored). Derivation by script comes before derivation by model.

### 6.3 Runtime generators

Same mechanism as the C2 psychometric generators: seeded, deterministic, the key computed by code, unit tests with golden seeds. Each generator cites the F fact its rule comes from and produces an explanation that shows the computation.

Initial families:

1. Capacity estimation: QPS, storage, bandwidth, cache size.
2. Quorums: `w + r > n` and which reads can be stale.
3. Token bucket and sliding-window rate limiter state after a sequence of requests.
4. Circuit breaker state after a sequence of calls.
5. Retry delay bounds with exponential backoff and full jitter.
6. Lamport and vector clocks: timestamps and which events are concurrent.
7. Kafka consumer lag and committed offsets after a sequence of events.
8. Isolation level against anomaly for an interleaving of two transactions.
9. Whether a query can use a given composite index.
10. Consistent hashing: which node owns a key before and after a node joins or leaves.
11. LRU cache contents after a sequence of operations.
12. Binary heap contents after a sequence of insertions and removals.
13. Time and space complexity of a generated loop structure.

### 6.4 System-design cases

One `case` per blueprint in programme section 9.4 (seven cases). Each has a scenario and 10 to 20 keyed questions whose answers follow from F facts. No free text.

### 6.5 Scheduler

Unseen questions first. Options shuffled. A failed question returns at increasing intervals. No streaks, no points, no reminders.

### 6.6 Presets

By lesson, by module, mixed review (driven by the scheduler), code reading only, generators only. The existing clock stays optional. There is no official mock exam.

## 7. Platform deltas

The platform session reads the repo first and builds only what is missing.

- **N1** Code blocks with syntax highlighting in lessons, question stems, options and explanations; horizontal scroll on mobile.
- **N2** Judgement rendering: a callout or equivalent that marks class J and shows its attribution.
- **N3** `extract_allowed` honoured by the "View solution" panel.
- **N4** The scheduler of section 6.5.
- **N5** Registration of the generator families of section 6.3 in the existing generator framework.

## 8. Build plan

The whole course is built in one run of sessions, with no review gate, and published once at the end. Every decision follows a default rule and is logged; nothing waits for Juanjo. The agent never commits.

### 8.1 Sessions

| Session | Runs | Does |
|---|---|---|
| S0 Setup | once | `versions.yaml`, sources with anchors, programme lock, source coverage report, question style guide, skeleton (`course.yaml`, lesson "How this course works", 68 stubs), ledgers |
| S1 Platform and tooling | once | Deltas N1–N5, the 13 generators, and the build scripts of 8.3 |
| S2 Module | the same prompt, re-run until the ledger shows all 12 modules done | One module end to end: theory, schemas, glossary, questions, verification. Module 09 also builds the seven cases; module 12 uses Tier C |
| S3 Final | once | Whole-course script audits, glossary and cross-link pass, `status: published` |

Module order: 06 first, because it is the most documentation-verifiable and exercises the whole pipeline; then 01 to 05 and 07 to 12 in numeric order. A module that does not fit in one usage window resumes from the ledger with the same prompt.

Expected total: 16 to 20 sessions.

### 8.2 The unit of work is the lesson

Each lesson goes through one pipeline, once. Theory, schemas and questions are written together and verified together, so each source anchor is read once by a writer and once by a verifier.

1. **Write** (Sonnet subagent). Loads only the anchors for the lesson's programme bullets. Produces, in one pass: the lesson with bullet ids per section, its schemas, glossary entries, «Key points», the code snippets as files, and the question candidates with citation and extract.
2. **Script checks.** Run every snippet on the pinned JDK and record outputs as keys; build variant families; check that extracts are literal substrings; check that citations resolve; check scope metadata.
3. **Verify** (Opus subagent that did not write the lesson). Loads the lesson, the questions and only the cited anchors. Writes a verdict file: one line per sentence, row and question, `pass` or `fail` with a reason of at most fifteen words.
4. **Fix.** A failed theory sentence is rewritten once from the source and re-verified alone; a second failure deletes it. A failed question is discarded. Replacement questions are written only if the lesson falls under the minimum quota.
5. **Ledger.** One line per lesson: counts written, passed, discarded, and default rules used.

### 8.3 Build scripts (written in S1)

`run_snippets` (execute and record), `build_variants`, `check_extracts`, `check_citations`, `check_scope`, `check_coverage`, `lesson_quota`, and `close_round.sh` extended to call them.

### 8.4 Token rules

- Anything a script can check is not sent to a model.
- Sources are read by anchor, never whole.
- Subagents write their output to files and return a status of at most five lines.
- The orchestrating session never reads lesson bodies or sources; it reads the ledger and the status lines.
- One session per module. A new session reads only the "where to resume" section of the ledger.
- At most eight subagents: four writers and four verifiers, each chaining lessons to reuse its context within a module.
- Provenance first: an identical, already verified sentence or question with the same anchor hash is inherited, not re-verified.
- Handoffs of at most thirty lines; no prose reports beyond the ledger and the verdict files.

### 8.5 Maintenance

A version audit every three months and whenever a pinned product publishes a new major or LTS release. A script lists the anchors whose content changed; only the facts citing those anchors are re-verified.

Ledgers and reports: `docs/backend-theory-ledger.md`, `docs/backend-bank-ledger.md`, `docs/backend-verification/`.

## 9. Programme (official)

This is the programme the scope and coverage audits use. S0 copies it literally to `content/backend-in-depth/programme.md`. Entries marked (J) are judgement by nature.

### Module 01 — Pragmatic software design and patterns

- **1.1 Design principles, pragmatism and data-oriented programming**
  - SOLID applied with judgement: cohesion, coupling and the limits of abstraction.
  - DRY, YAGNI and KISS: when to tolerate duplication instead of abstracting early. (J)
  - Law of Demeter, composition over inheritance, immutability in the domain.
  - Data-oriented programming in modern Java: algebraic domain modelling with records, sealed classes, pattern matching for switch and record patterns.
- **1.2 GoF patterns in modern backend code**
  - Creational: Factory Method, Abstract Factory, Builder (invariants validated at construction).
  - Structural: Adapter, Decorator, Facade, Proxy, applied to HTTP clients, caches and persistence layers.
  - Behavioural: Strategy, Observer, Template Method, Command, Chain of Responsibility, State.
- **1.3 Application architecture and modular evolution**
  - Hexagonal architecture (ports and adapters) and pragmatic Clean Architecture in Spring Boot.
  - Modular monolith versus microservices: context boundaries (Spring Modulith) and when to avoid the cost of distribution. (J)
  - Architectural fitness functions: automated architecture tests with ArchUnit against layer violations and dependency cycles.
  - Tactical domain modelling: aggregates, value objects, domain events.
- **1.4 Auditing and defending AI-assisted code**
  - Review checklist for assistant-generated code: unnecessary dependencies, broken encapsulation, leaky abstractions, hidden debt. (J)
  - Subtle failures typical of generated Java/Spring code: `@Transactional` on self-invocation, blocking `ForkJoinPool.commonPool()` from `CompletableFuture`, broken interrupt handling.
  - Explaining and defending each design decision in a take-home review. (J)

### Module 02 — Algorithms and data structures

- **2.1 Complexity and Java collections internals**
  - Asymptotic notation, amortised analysis, space complexity.
  - Internals of `ArrayList`, `LinkedList`, `ArrayDeque`, `HashMap` (collisions, treeification, resizing), `LinkedHashMap`, `TreeMap`, `PriorityQueue`.
  - The `equals` / `hashCode` / `compareTo` contracts and their effect on collections.
- **2.2 Arrays, strings and hashing**
  - Two pointers, sliding window, prefix sums, counting with maps.
  - Binary search over arrays and over the answer space.
  - Sorting: classic algorithms, stability, and what Java uses in each case.
  - Interval problems: merging, overlaps, sweep line.
- **2.3 Linear structures and trees**
  - Linked lists (fast and slow pointers, reversal), stacks, queues, monotonic stack.
  - Binary trees and BSTs: recursive and iterative traversals, lowest common ancestor, validation.
  - Heaps and top-K problems; tries for prefixes.
- **2.4 Graphs**
  - Representations, BFS and DFS, connected components, cycle detection.
  - Topological sort, union-find, shortest paths (Dijkstra).
  - Grids as implicit graphs.
- **2.5 Algorithm design techniques**
  - Recursion and backtracking: subsets, permutations, pruning.
  - Dynamic programming: state definition, memoisation versus tabulation, common patterns (knapsack, subsequences, grids).
  - Greedy algorithms and when they are correct.
  - Basic bit manipulation.
- **2.6 Design structures common in interviews**
  - LRU and LFU caches, in-memory rate limiter, iterator over nested structures, running median.
- **2.7 Pattern recognition**
  - Given a problem statement: identify the pattern, the data structure and the complexity of the naive and the optimal solution.

### Module 03 — Modern JVM, concurrency and performance

- **3.1 JVM internals, memory management and cloud efficiency**
  - Memory areas: stack, heap, metaspace; escape analysis and TLABs.
  - Modern collectors: how G1 and generational ZGC work and are tuned (latency versus throughput).
  - Diagnosing memory leaks; reading heap dumps and thread dumps.
  - Start-up time and footprint on Kubernetes: AppCDS and Project Leyden, Spring Boot AOT, GraalVM Native Image and their trade-offs.
- **3.2 Classic concurrency and the Java Memory Model**
  - Visibility, atomicity and ordering: `volatile`, happens-before, `Atomic*` classes.
  - `CompletableFuture` (composition with a dedicated executor, exception handling), `ExecutorService`, `ReentrantLock`, `StampedLock`, `Semaphore`.
  - Concurrent collections (`ConcurrentHashMap`, `CopyOnWriteArrayList`, blocking queues); deadlocks, livelocks and race conditions.
- **3.3 Project Loom: virtual threads, structured concurrency and scoped values**
  - Virtual threads (JEP 444): carrier and virtual threads, scheduling, and differences from reactive programming.
  - Pinning and its evolution (JEP 491): `synchronized` and native calls in Java 21 versus Java 24 and later; sizing connection pools; limiting concurrency with semaphores.
  - Structured concurrency (JEP 505 and its state in the pinned version): `StructuredTaskScope.open()` and `Joiner` policies, cancellation, prevention of thread leaks; how the API changed between previews.
  - Scoped values (JEP 506) as a replacement for `ThreadLocal` in context propagation.
- **3.4 Profiling, benchmarking and measuring performance**
  - Java Flight Recorder and JDK Mission Control: events, continuous recording, overhead.
  - CPU and allocation profiling with async-profiler; reading flame graphs; safepoint bias.
  - Microbenchmarks with JMH: warm-up, dead-code elimination, constant folding, `Blackhole`, forks.
  - Measuring latency: percentiles versus means, histograms, coordinated omission.
  - Method: hypothesis, measurement, single change, verification; when not to optimise. (J)

### Module 04 — Kotlin for Java developers

- **4.1 Type system and null safety**
  - Nullable types, safe calls, the Elvis operator, smart casts, `lateinit`.
  - Platform types in Java interoperability and nullability annotations.
  - Generics: declaration-site variance (`in` / `out`) and reified type parameters.
- **4.2 Idiomatic Kotlin**
  - `data class`, `sealed class` and `sealed interface`, `object`, `value class`, exhaustive `when`.
  - Extension functions and scope functions (`let`, `run`, `apply`, `also`, `with`).
  - Read-only collection interfaces, sequences versus collections, delegation with `by`.
  - Comparison with modern Java records, sealed classes and pattern matching (see 1.1).
- **4.3 Coroutines**
  - `suspend` functions, continuations, and what the compiler generates.
  - Structured concurrency: `CoroutineScope`, `launch` and `async`, `Job` versus `SupervisorJob`, cooperative cancellation, exception propagation.
  - Dispatchers, context switching, blocking calls inside coroutines.
  - `Flow`: cold flows, operators, `StateFlow` and `SharedFlow`, backpressure.
  - Coroutines versus virtual threads (see 3.3).
- **4.4 Kotlin in Spring Boot**
  - Compiler plugins (`all-open`, `no-arg`) and why Spring and JPA need them.
  - JPA entities in Kotlin: risks of `data class`, equality, lazy loading.
  - Controllers and repositories with `suspend` functions; configuration DSLs.
  - Testing: MockK and coroutine tests with virtual time.
- **4.5 Interoperability and migration from Java**
  - Calls in both directions: `@JvmStatic`, `@JvmOverloads`, `@Throws`, unchecked exceptions.
  - Incremental migration of a Java code base and common mistakes. (J)

### Module 05 — Spring Framework and Spring Boot internals

- **5.1 IoC container and bean lifecycle**
  - `BeanDefinition`, `BeanFactory` versus `ApplicationContext`, scopes, initialisation order.
  - Lifecycle: instantiation, injection, `BeanPostProcessor`, initialisation and destruction callbacks.
  - Constructor versus field injection, circular dependencies, `@Lazy`, `@Primary`, `@Qualifier`.
  - `@Configuration` (full versus lite mode), `@Conditional`, profiles.
- **5.2 Spring Boot auto-configuration**
  - How auto-configurations are discovered and ordered; `@ConditionalOn…`; the condition evaluation report.
  - Starters, `@ConfigurationProperties`, precedence of externalised configuration.
  - Writing an auto-configuration and an internal starter.
- **5.3 AOP and proxies**
  - JDK dynamic proxies versus CGLIB; why self-invocation bypasses the proxy.
  - Limits: `final` and private methods, calls from constructors.
  - Proxy-based annotations: `@Transactional`, `@Async`, `@Cacheable`, `@Retryable`, and their ordering.
- **5.4 Transaction management**
  - `PlatformTransactionManager`, resource synchronisation, thread binding.
  - Propagation, isolation, `readOnly`, timeouts.
  - Rollback rules: checked versus unchecked exceptions, `rollbackFor`.
  - `@TransactionalEventListener` phases; transactions with virtual threads, `@Async` and reactive code.
- **5.5 Web layer**
  - Request path: filters, `DispatcherServlet`, handler mappings, interceptors, argument resolution, message converters.
  - Validation, `@ControllerAdvice`, error model.
  - Spring MVC versus WebFlux; MVC on virtual threads.
  - HTTP clients: `RestClient`, `WebClient`, declarative interfaces; timeouts and connection pools.
- **5.6 Spring Security**
  - Architecture: `DelegatingFilterProxy`, `FilterChainProxy`, `SecurityFilterChain`; filter order.
  - Authentication (`AuthenticationManager`, `AuthenticationProvider`) and `SecurityContext`; propagation across threads.
  - Request-level and method-level authorisation (`@PreAuthorize`).
  - Resource server with JWT: validation, mapping claims to authorities, several issuers for multi-tenancy.
- **5.7 Spring Data and JPA**
  - Repositories: derived queries, `@Query`, projections, specifications.
  - Persistence context, entity states, dirty checking, flush, `open-in-view`.
  - Auditing, optimistic locking, batching (see 6.3).
- **5.8 Operating and testing Spring Boot applications**
  - Actuator: health groups, metrics, management endpoints.
  - Start-up and shutdown events; graceful shutdown.
  - Test slices (`@WebMvcTest`, `@DataJpaTest`), `@SpringBootTest`, test-context caching, `@ServiceConnection` with Testcontainers.

### Module 06 — Relational persistence, transactions and SQL optimisation

- **6.1 ACID, MVCC and PostgreSQL internals**
  - MVCC and write-ahead logging in PostgreSQL.
  - Operating cost of MVCC: dead tuples, autovacuum tuning, table and index bloat, transaction ID wraparound.
  - Isolation levels of the SQL standard and their real behaviour in PostgreSQL: Read Uncommitted, Read Committed, Repeatable Read (snapshot isolation), Serializable (SSI).
- **6.2 Concurrency anomalies, locking and connection pooling**
  - Dirty reads, non-repeatable reads, phantom reads, lost updates, write skew.
  - Optimistic locking (`@Version`) versus pessimistic locking (`SELECT … FOR UPDATE`, `FOR SHARE`, queues with `SKIP LOCKED`).
  - Connections at scale: sizing HikariCP; PgBouncer transaction pooling versus session pooling.
- **6.3 Advanced indexing, partitioning and SQL optimisation**
  - B-tree, hash, GIN, GiST; partial, composite and covering indexes (`INCLUDE`).
  - Reading plans with `EXPLAIN (ANALYZE, BUFFERS)`.
  - Offset versus keyset pagination; declarative partitioning by range and hash.
  - ORM anti-patterns: N+1, fetch joins, DTO projections, session management, write batching.
- **6.4 Zero-downtime schema evolution**
  - Expand and contract with Flyway or Liquibase, `CREATE INDEX CONCURRENTLY`, batched backfill, backward compatibility.

### Module 07 — Networking and API design

- **7.1 Networking fundamentals for backend engineers**
  - TCP: connection set-up and teardown, flow and congestion control, keep-alive, head-of-line blocking, `TIME_WAIT`.
  - DNS: resolution, TTL, caches including the JVM's, service discovery in Kubernetes.
  - TLS 1.3: handshake, certificates and chain of trust, SNI, ALPN, mTLS.
  - Connect, read and total timeouts; HTTP connection pools and stale connections.
- **7.2 HTTP/1.1, HTTP/2 and HTTP/3**
  - Multiplexing, streams, header compression, and what each version solves.
  - QUIC and HTTP/3.
  - WebSockets and Server-Sent Events.
- **7.3 Load balancing and the edge**
  - L4 versus L7 balancers, algorithms, health checks, connection draining.
  - Reverse proxies, API gateways, Ingress and Gateway API in Kubernetes.
  - CDNs and edge caching.
- **7.4 HTTP semantics**
  - Safe and idempotent methods; status codes.
  - HTTP caching: `Cache-Control`, `ETag`, conditional requests, `Vary`.
  - Content negotiation and compression.
- **7.5 REST API design**
  - Resource modelling and naming.
  - Idempotency keys on `POST`, safe retries, server-side deduplication.
  - Optimistic concurrency with `ETag` and `If-Match`.
  - Pagination, filtering, sorting, partial responses.
  - Error model: Problem Details; validation errors.
  - Long-running operations, batch operations, webhooks (signing, retries, ordering).
  - Rate limiting as seen by the client: `429`, `Retry-After`, quota headers.
  - OpenAPI and contract-first design.
- **7.6 gRPC, GraphQL and asynchronous APIs**
  - gRPC and Protocol Buffers: call types, deadlines, cancellation, status codes, message evolution rules.
  - GraphQL: schema, resolvers, the N+1 problem.
  - AsyncAPI for event contracts (see 8.2).
  - Choosing between REST, gRPC, GraphQL and messaging. (J)
- **7.7 API evolution and governance**
  - Compatible and breaking changes; versioning strategies and their costs.
  - Tolerant reader, deprecation policy, deprecation and sunset headers.
  - API style guides and cross-team design review. (J)

### Module 08 — Distributed systems, messaging and resilience

- **8.1 Fundamentals of distributed systems**
  - CAP and PACELC applied to storage decisions.
  - Consistency models: linearizable, sequential, causal, eventual; read-your-writes and monotonic reads.
  - Time: physical clocks and NTP versus Lamport and vector clocks.
- **8.2 Event-driven architecture (Kafka and RabbitMQ)**
  - Kafka internals: partitions, replication factor, in-sync replicas, `acks`, consumer groups, offsets, cooperative rebalancing.
  - Contracts and ordering: Schema Registry compatibility modes, partition keys, hot partitions.
  - Error handling: dead-letter topics, poison pills, non-blocking retries, consumer lag.
  - Delivery semantics and idempotent consumers.
- **8.3 Distributed transactions without 2PC**
  - The dual-write problem.
  - Transactional outbox: polling with `SKIP LOCKED` versus change data capture with Debezium.
  - Sagas: orchestration versus choreography, compensating actions, semantic isolation.
- **8.4 Stability, resilience and traffic control**
  - Circuit breaker: states, sliding windows, slow-call thresholds, fallbacks with Resilience4j.
  - Retries with exponential backoff and full jitter.
  - Bulkheads, rate limiting (token bucket, leaky bucket, sliding window), load shedding, timeout propagation, backpressure.
- **8.5 Consensus and coordination**
  - Partial failures, asynchronous networks, failure detectors, process pauses.
  - Raft: leader election, terms, log replication, commit index, membership changes, snapshots. Paxos as a reference.
  - Quorums, split brain and leader election in practice: ZooKeeper, etcd, KRaft.
  - Distributed locks and leases; fencing tokens.
  - Two-phase commit: how it works and why it blocks.
  - Gossip protocols and cluster membership.
- **8.6 Event sourcing and CQRS**
  - The event log as source of truth, aggregate rehydration, snapshots, optimistic concurrency on the event store.
  - CQRS: write and read models, projections, eventual consistency of read models.
  - Event evolution: versioning, upcasting, compensating events.
  - Projections in production: replay, rebuild without downtime, idempotency, tracking position.
  - Axon Framework: command bus, aggregates, event processors (subscribing versus streaming), sagas.
  - Personal data in an immutable log: crypto-shredding and erasure.
  - When not to use event sourcing. (J)
- **8.7 Stream processing**
  - Batch versus stream; event time versus processing time.
  - Tumbling, hopping, sliding and session windows; watermarks, late data, grace period.
  - Stateful processing: state stores, changelog topics, recovery.
  - Kafka Streams: KStream and KTable, joins, co-partitioning, repartition topics.
  - Exactly-once processing: idempotent producers and Kafka transactions.
  - Apache Flink as a reference: checkpoints, savepoints, backpressure.

### Module 09 — System design and data scalability

- **9.1 A step-by-step framework for system design**
  - Scope, functional and non-functional requirements (SLAs and SLOs, p95 and p99 latency, availability).
  - Back-of-the-envelope capacity estimation.
  - API contracts and choice of storage engine.
  - High-level architecture and end-to-end data flow.
- **9.2 Data scalability: replication, sharding and caching**
  - When to scale up, add replicas, partition locally, or shard. (J)
  - Replication: single-leader, multi-leader, leaderless with quorums; handling replication lag.
  - Sharding: range versus hash, consistent hashing with virtual nodes, hot keys, local versus global secondary indexes, cross-shard joins, rebalancing.
  - Distributed caching: cache-aside, read-through and write-through, write-behind, invalidation, cache stampede, hot keys.
- **9.3 Multi-tenant architecture and data isolation**
  - Database per tenant, schema per tenant, shared tables with row-level security.
  - Noisy neighbours: per-tenant quotas, fair queuing, bulkheads.
- **9.4 Blueprints**
  - Distributed rate limiter.
  - Booking and inventory engine under high contention.
  - Multi-channel notification platform.
  - Telemetry and event ingestion pipeline.
  - URL shortener and distributed ID generation.
  - Search and autocomplete.
  - Agentic diagnostics platform and enterprise AI gateway.
- **9.5 Storage engines and non-relational databases**
  - LSM-trees versus B-trees: memtable, SSTables, compaction, Bloom filters, write, read and space amplification.
  - Row-oriented versus columnar storage; OLTP versus OLAP.
  - Redis internals: data structures, single-threaded execution, RDB and AOF persistence, eviction policies, Sentinel and Cluster.
  - Elasticsearch internals: inverted index, segments and merges, refresh, shards and replicas, analysers, BM25, deep pagination.
  - Choosing between document, key-value, wide-column and time-series stores. (J)

### Module 10 — Platform, observability, security and AI integration

- **10.1 Observability of distributed systems**
  - Structured logs with correlation, metrics (Micrometer, Prometheus, RED and USE), distributed tracing with OpenTelemetry.
  - Actionable alerts based on SLOs and error budgets.
- **10.2 Security, identity and compliance**
  - Zero-trust between services: mTLS, default-deny NetworkPolicies, dynamic secrets.
  - OAuth 2.0 and OpenID Connect flows, JWT handling, key rotation, RBAC and ABAC.
  - Privacy by design, encryption in transit and at rest, immutable audit, regulated environments (NEN 7510, GDPR).
- **10.3 FinOps and infrastructure efficiency**
  - Kubernetes `requests` and `limits`, HPA and KEDA, inter-zone traffic cost, telemetry retention, storage selection.
- **10.4 Platform engineering and architecture of systems with AI**
  - Golden paths, global standards, threat-modelling templates. (J)
  - Deterministic state machines versus agentic loops. (J)
  - LLM integration: permission-aware RAG, Model Context Protocol with least privilege, cost control through AI gateways.
  - Security and reliability: indirect prompt injection, no leakage of production data, deterministic evals in CI.
- **10.5 Kubernetes in production and continuous delivery**
  - Pod lifecycle: liveness, readiness and start-up probes, and common mistakes.
  - Graceful shutdown: `SIGTERM`, `preStop`, `terminationGracePeriodSeconds`, connection draining, Spring Boot and Kafka consumers.
  - Availability during change: rolling updates, PodDisruptionBudgets, anti-affinity, zone spread.
  - Deployment strategies: rolling, blue/green, canary; progressive delivery and rollback.
  - Feature flags.
  - GitOps and CI/CD pipeline design: trunk-based development, immutable artefacts, promotion.
  - Database migrations inside a deployment (see 6.4).
  - DORA metrics.
- **10.6 Application security and supply chain**
  - OWASP Top 10 and OWASP API Security Top 10 applied to Java and Spring.
  - Broken access control: IDOR and BOLA, cross-tenant leaks, mass assignment.
  - Injection, SSRF, insecure deserialisation, path traversal.
  - HTTP surface: CORS, CSRF, security headers, input validation.
  - Secrets and sensitive data in logs, traces and dumps.
  - Supply chain: dependency analysis, SBOM, image signing, SLSA levels, reproducible builds.
  - Threat modelling with STRIDE.

### Module 11 — Code reading, debugging and testing

- **11.1 Java Streams, gatherers and collections in depth**
  - `flatMap`, composed comparators, `reduce`, `takeWhile` and `dropWhile`.
  - Collectors: multi-level `groupingBy`, `partitioningBy`, `toMap` with merge functions, `teeing`, custom collectors.
  - Stream gatherers (JEP 485): `windowFixed`, `windowSliding`, `fold`, `scan`.
  - Reading a pipeline: its result and its complexity.
- **11.2 Refactoring legacy code and reviewing AI-generated changes**
  - Code smells, hidden coupling, resource leaks, poor exception handling, concurrency errors.
  - Finding subtle production bugs in clean-looking code: races, money and time-zone precision, transaction leaks.
  - Safe extraction: extract method and class, introducing polymorphism, decoupling external dependencies.
- **11.3 Production debugging and incident triage**
  - Reading stack traces, correlating logs, p99 latency, connection-pool saturation, GC pauses and consumer lag to isolate a root cause.
- **11.4 Deterministic testing**
  - JUnit 5, Mockito and AssertJ: AAA, parameterised tests, injected `Clock`, edge cases.
  - Integration tests with Testcontainers.
- **11.5 Thinking aloud**
  - Clarifying edge cases first, stating complexity, justifying trade-offs as you go. (J)
- **11.6 Advanced testing and test strategy**
  - Shape of the suite and what to test at each level. (J)
  - Consumer-driven contract testing.
  - Property-based testing: properties, generators, shrinking.
  - Mutation testing.
  - Load testing: open and closed workload models, percentile targets, soak tests.
  - Flaky tests: causes and removal.
  - Chaos engineering: hypothesis, blast radius, fault injection.

### Module 12 — Staff-level technical leadership

Built only from public material (Tier C). Everything is class J and attributed.

- **12.1 Architecture documentation, decision making and governance**
  - ADRs and RFCs: context, options, trade-offs, consequences, mitigation.
  - Building consensus and influencing without authority.
  - Governing the development lifecycle when teams generate code with AI.
- **12.2 Remote work and asynchronous communication**
  - Clear written communication, asynchronous unblocking, living documentation, time-zone overlap.
- **12.3 Behavioural interviews: STAR and story archetypes**
  - The STAR method and its variants; quantifying results; separating your contribution from the team's.
  - What interviewers assess at Senior versus Staff level.
  - Six archetypes: critical migration, cross-team influence, incident response, technical conflict resolved with a simpler option, mentoring, failure and what changed afterwards.
  - A template for writing your own stories outside the course.
- **12.4 Cultural fit and product alignment**
  - Common questions from engineering managers, product managers and executives.
  - Questions to assess a company: technical maturity, autonomy, on-call, promotion, business stability.
- **12.5 Technical strategy and large migrations**
  - The Staff role: archetypes, scope versus Senior, low-visibility coordination work, choosing what to work on.
  - Published engineering career ladders and how to read them.
  - Technical strategy: diagnosis, policy, actions; vision and strategy documents.
  - Large migrations: strangler fig, branch by abstraction, parallel run, incremental data migration, completion criteria.
  - Build versus buy and technology evaluation.
  - Technical debt as a portfolio.
  - Estimation and risk in multi-quarter projects.
  - Deprecating and retiring systems and APIs.

## 10. Rules that do not change

- A fact comes from the stored source or from an execution record, never from memory.
- Blind verification by an agent that did not write the text. Verifiers run on Opus, writers on Sonnet, never Haiku for a key. At most eight subagents.
- Provenance: a sentence, row or question identical to an already verified one, with the same citation and the same source hash, inherits its verification with a record.
- Nothing coined: every term exists outside the course with the same sense.
- No streaks, points or other engagement mechanics anywhere in the course.
- The agent never commits.

## Amendments (v1.2)

2026-11-13, session S1. Each amendment overrides the section it names.

1. Class X also covers arithmetic computed by a script from assumptions stated in the lesson or the question (capacity estimation, quorum arithmetic). The evidence is the script and its output.
2. Sources stored outside git are resolved through the environment variable `CURSET_SOURCES_LOCAL` (default `~/PycharmProjects/curset-saved-originals/backend-in-depth/local`). Scripts verify content when the folder is present and skip with a warning when it is absent; they never fail CI for that reason.
3. Schema rows in this course cite `source_id#anchor`.
4. Lesson `m00-l01` covers no programme bullet and is exempt from the scope audit.
5. 2026-11-13, session S2. Source rule, overriding the default rules of section 3.3: a programme item whose
   only stored source is Tier B or Tier C is written as class J, in a judgement block with attribution. It is
   omitted only when no stored source supports it. "Stored" means registered in `sources.yaml` (Tier A or C,
   with anchors) or in `docs/backend-verification/s0/tier-b.yaml` (Tier B, by chapter).
