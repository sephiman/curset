# Thread pool queuing and rejection (`thread-pool-state`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 1672758273640814970, level 2

A `ThreadPoolExecutor` has `corePoolSize` 2, `maximumPoolSize` 4 and an `ArrayBlockingQueue` of capacity 4. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) 9
b) call number 5
c) call 7
d) call number 8

**Key: a**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 2. 2. Queue slots: 4. 3. Extra thread slots: 4 - 2 = 2. 4. The first call after all are used is call 4 + 4 + 1 = 9, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 2. seed 1739676660263254873, level 2

A `ThreadPoolExecutor` has `corePoolSize` 3, `maximumPoolSize` 6 and an `ArrayBlockingQueue` of capacity 2. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) 9
b) 12
c) call number 8
d) 6

**Key: a**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 3. 2. Queue slots: 2. 3. Extra thread slots: 6 - 3 = 3. 4. The first call after all are used is call 6 + 2 + 1 = 9, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 3. seed 1047775708881866375, level 2

A `ThreadPoolExecutor` has `corePoolSize` 3, `maximumPoolSize` 5 and an `ArrayBlockingQueue` of capacity 2. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) 6
b) call number 11
c) call number 8
d) call 7

**Key: c**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 3. 2. Queue slots: 2. 3. Extra thread slots: 5 - 3 = 2. 4. The first call after all are used is call 5 + 2 + 1 = 8, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 4. seed 2211364530590598440, level 1

A `ThreadPoolExecutor` has `corePoolSize` 3, `maximumPoolSize` 4 and an `ArrayBlockingQueue` of capacity 4. Tasks that never finish are passed to `execute`. After 8 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 4, queued 0, rejected 4
b) threads 3, queued 4, rejected 1
c) threads 4, queued 4, rejected 0
d) threads 3, queued 5, rejected 0

**Key: c**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(8, 3) = 3. 2. Tasks queued: at most 4, here 4. 3. Extra threads started: 1. 4. Rejected: 8 - 4 - 4 = 0. Result: threads 4, queued 4, rejected 0. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 5. seed 278098048239620377, level 2

A `ThreadPoolExecutor` has `corePoolSize` 1, `maximumPoolSize` 3 and an `ArrayBlockingQueue` of capacity 3. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) call number 8
b) call 7
c) call 4
d) call number 5

**Key: b**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 1. 2. Queue slots: 3. 3. Extra thread slots: 3 - 1 = 2. 4. The first call after all are used is call 3 + 3 + 1 = 7, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 6. seed 1321225256420754896, level 2

A `ThreadPoolExecutor` has `corePoolSize` 3, `maximumPoolSize` 6 and an `ArrayBlockingQueue` of capacity 5. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) call number 11
b) 9
c) 12
d) call 7

**Key: c**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 3. 2. Queue slots: 5. 3. Extra thread slots: 6 - 3 = 3. 4. The first call after all are used is call 6 + 5 + 1 = 12, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 7. seed 3371200904477379610, level 2

A `ThreadPoolExecutor` has `corePoolSize` 1, `maximumPoolSize` 2 and an `ArrayBlockingQueue` of capacity 3. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) call 7
b) 6
c) 3
d) call number 5

**Key: b**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 1. 2. Queue slots: 3. 3. Extra thread slots: 2 - 1 = 1. 4. The first call after all are used is call 2 + 3 + 1 = 6, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 8. seed 795032264766881247, level 2

A `ThreadPoolExecutor` has `corePoolSize` 2, `maximumPoolSize` 5 and an `ArrayBlockingQueue` of capacity 3. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) call number 8
b) 9
c) 6
d) call number 11

**Key: b**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 2. 2. Queue slots: 3. 3. Extra thread slots: 5 - 2 = 3. 4. The first call after all are used is call 5 + 3 + 1 = 9, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 9. seed 4195221537948175466, level 1

A `ThreadPoolExecutor` has `corePoolSize` 2, `maximumPoolSize` 4 and an `ArrayBlockingQueue` of capacity 4. Tasks that never finish are passed to `execute`. After 7 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 4, queued 0, rejected 3
b) threads 2, queued 4, rejected 1
c) threads 3, queued 4, rejected 0
d) threads 2, queued 5, rejected 0

**Key: c**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(7, 2) = 2. 2. Tasks queued: at most 4, here 4. 3. Extra threads started: 1. 4. Rejected: 7 - 3 - 4 = 0. Result: threads 3, queued 4, rejected 0. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 10. seed 3779159328185052928, level 2

A `ThreadPoolExecutor` has `corePoolSize` 2, `maximumPoolSize` 4 and an `ArrayBlockingQueue` of capacity 3. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) call 10
b) call number 5
c) call 7
d) call number 8

**Key: d**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 2. 2. Queue slots: 3. 3. Extra thread slots: 4 - 2 = 2. 4. The first call after all are used is call 4 + 3 + 1 = 8, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 11. seed 2645874532976905192, level 2

A `ThreadPoolExecutor` has `corePoolSize` 3, `maximumPoolSize` 5 and an `ArrayBlockingQueue` of capacity 2. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) call number 11
b) call number 8
c) 6
d) call 7

**Key: b**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 3. 2. Queue slots: 2. 3. Extra thread slots: 5 - 3 = 2. 4. The first call after all are used is call 5 + 2 + 1 = 8, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 12. seed 1524978473626315218, level 2

A `ThreadPoolExecutor` has `corePoolSize` 2, `maximumPoolSize` 3 and an `ArrayBlockingQueue` of capacity 4. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) call number 8
b) call 10
c) call 7
d) call 4

**Key: a**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 2. 2. Queue slots: 4. 3. Extra thread slots: 3 - 2 = 1. 4. The first call after all are used is call 3 + 4 + 1 = 8, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 13. seed 398407682170371317, level 1

A `ThreadPoolExecutor` has `corePoolSize` 3, `maximumPoolSize` 4 and an `ArrayBlockingQueue` of capacity 2. Tasks that never finish are passed to `execute`. After 8 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 4, queued 2, rejected 2
b) threads 4, queued 0, rejected 4
c) threads 3, queued 5, rejected 0
d) threads 3, queued 2, rejected 3

**Key: a**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(8, 3) = 3. 2. Tasks queued: at most 2, here 2. 3. Extra threads started: 1. 4. Rejected: 8 - 4 - 2 = 2. Result: threads 4, queued 2, rejected 2. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 14. seed 4327196930618753784, level 1

A `ThreadPoolExecutor` has `corePoolSize` 1, `maximumPoolSize` 2 and an `ArrayBlockingQueue` of capacity 4. Tasks that never finish are passed to `execute`. After 9 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 2, queued 0, rejected 7
b) threads 1, queued 4, rejected 4
c) threads 1, queued 8, rejected 0
d) threads 2, queued 4, rejected 3

**Key: d**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(9, 1) = 1. 2. Tasks queued: at most 4, here 4. 3. Extra threads started: 1. 4. Rejected: 9 - 2 - 4 = 3. Result: threads 2, queued 4, rejected 3. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 15. seed 2482705543249575860, level 2

A `ThreadPoolExecutor` has `corePoolSize` 2, `maximumPoolSize` 4 and an `ArrayBlockingQueue` of capacity 5. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) 9
b) call number 8
c) 12
d) call 10

**Key: d**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 2. 2. Queue slots: 5. 3. Extra thread slots: 4 - 2 = 2. 4. The first call after all are used is call 4 + 5 + 1 = 10, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 16. seed 4531719090149118489, level 1

A `ThreadPoolExecutor` has `corePoolSize` 2, `maximumPoolSize` 4 and an `ArrayBlockingQueue` of capacity 2. Tasks that never finish are passed to `execute`. After 7 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 2, queued 5, rejected 0
b) threads 4, queued 0, rejected 3
c) threads 4, queued 2, rejected 1
d) threads 2, queued 2, rejected 3

**Key: c**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(7, 2) = 2. 2. Tasks queued: at most 2, here 2. 3. Extra threads started: 2. 4. Rejected: 7 - 4 - 2 = 1. Result: threads 4, queued 2, rejected 1. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 17. seed 3502018188098399971, level 2

A `ThreadPoolExecutor` has `corePoolSize` 3, `maximumPoolSize` 6 and an `ArrayBlockingQueue` of capacity 5. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) 15
b) 12
c) call 7
d) call number 11

**Key: b**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 3. 2. Queue slots: 5. 3. Extra thread slots: 6 - 3 = 3. 4. The first call after all are used is call 6 + 5 + 1 = 12, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 18. seed 2261432512426637841, level 1

A `ThreadPoolExecutor` has `corePoolSize` 1, `maximumPoolSize` 4 and an `ArrayBlockingQueue` of capacity 3. Tasks that never finish are passed to `execute`. After 6 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 1, queued 3, rejected 2
b) threads 3, queued 3, rejected 0
c) threads 4, queued 0, rejected 2
d) threads 4, queued 2, rejected 0

**Key: b**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(6, 1) = 1. 2. Tasks queued: at most 3, here 3. 3. Extra threads started: 2. 4. Rejected: 6 - 3 - 3 = 0. Result: threads 3, queued 3, rejected 0. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 19. seed 3684786129248455506, level 2

A `ThreadPoolExecutor` has `corePoolSize` 3, `maximumPoolSize` 5 and an `ArrayBlockingQueue` of capacity 5. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) call number 14
b) 9
c) call number 11
d) call 10

**Key: c**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 3. 2. Queue slots: 5. 3. Extra thread slots: 5 - 3 = 2. 4. The first call after all are used is call 5 + 5 + 1 = 11, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 20. seed 2928186349431781274, level 1

A `ThreadPoolExecutor` has `corePoolSize` 3, `maximumPoolSize` 4 and an `ArrayBlockingQueue` of capacity 3. Tasks that never finish are passed to `execute`. After 9 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 3, queued 3, rejected 3
b) threads 4, queued 0, rejected 5
c) threads 3, queued 6, rejected 0
d) threads 4, queued 3, rejected 2

**Key: d**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(9, 3) = 3. 2. Tasks queued: at most 3, here 3. 3. Extra threads started: 1. 4. Rejected: 9 - 4 - 3 = 2. Result: threads 4, queued 3, rejected 2. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 21. seed 1331861238766353218, level 1

A `ThreadPoolExecutor` has `corePoolSize` 1, `maximumPoolSize` 4 and an `ArrayBlockingQueue` of capacity 5. Tasks that never finish are passed to `execute`. After 10 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 1, queued 5, rejected 4
b) threads 4, queued 0, rejected 6
c) threads 1, queued 9, rejected 0
d) threads 4, queued 5, rejected 1

**Key: d**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(10, 1) = 1. 2. Tasks queued: at most 5, here 5. 3. Extra threads started: 3. 4. Rejected: 10 - 4 - 5 = 1. Result: threads 4, queued 5, rejected 1. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 22. seed 2507016562594829982, level 1

A `ThreadPoolExecutor` has `corePoolSize` 2, `maximumPoolSize` 5 and an `ArrayBlockingQueue` of capacity 4. Tasks that never finish are passed to `execute`. After 9 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 2, queued 4, rejected 3
b) threads 5, queued 4, rejected 0
c) threads 2, queued 7, rejected 0
d) threads 5, queued 0, rejected 4

**Key: b**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(9, 2) = 2. 2. Tasks queued: at most 4, here 4. 3. Extra threads started: 3. 4. Rejected: 9 - 5 - 4 = 0. Result: threads 5, queued 4, rejected 0. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 23. seed 3199662654529428601, level 2

A `ThreadPoolExecutor` has `corePoolSize` 2, `maximumPoolSize` 5 and an `ArrayBlockingQueue` of capacity 5. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) call number 11
b) 6
c) call number 8
d) call 10

**Key: a**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 2. 2. Queue slots: 5. 3. Extra thread slots: 5 - 2 = 3. 4. The first call after all are used is call 5 + 5 + 1 = 11, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 24. seed 3146211947925954070, level 1

A `ThreadPoolExecutor` has `corePoolSize` 3, `maximumPoolSize` 6 and an `ArrayBlockingQueue` of capacity 4. Tasks that never finish are passed to `execute`. After 8 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 3, queued 5, rejected 0
b) threads 4, queued 4, rejected 0
c) threads 6, queued 2, rejected 0
d) threads 6, queued 0, rejected 2

**Key: b**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(8, 3) = 3. 2. Tasks queued: at most 4, here 4. 3. Extra threads started: 1. 4. Rejected: 8 - 4 - 4 = 0. Result: threads 4, queued 4, rejected 0. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 25. seed 2448392511465236177, level 1

A `ThreadPoolExecutor` has `corePoolSize` 2, `maximumPoolSize` 5 and an `ArrayBlockingQueue` of capacity 3. Tasks that never finish are passed to `execute`. After 8 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 5, queued 0, rejected 3
b) threads 5, queued 3, rejected 0
c) threads 2, queued 3, rejected 3
d) threads 2, queued 6, rejected 0

**Key: b**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(8, 2) = 2. 2. Tasks queued: at most 3, here 3. 3. Extra threads started: 3. 4. Rejected: 8 - 5 - 3 = 0. Result: threads 5, queued 3, rejected 0. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 26. seed 4150843870881132267, level 2

A `ThreadPoolExecutor` has `corePoolSize` 3, `maximumPoolSize` 4 and an `ArrayBlockingQueue` of capacity 4. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) call number 8
b) 9
c) call number 5
d) 12

**Key: b**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 3. 2. Queue slots: 4. 3. Extra thread slots: 4 - 3 = 1. 4. The first call after all are used is call 4 + 4 + 1 = 9, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 27. seed 2624311983844610396, level 2

A `ThreadPoolExecutor` has `corePoolSize` 3, `maximumPoolSize` 5 and an `ArrayBlockingQueue` of capacity 5. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) 9
b) 6
c) call number 11
d) call number 14

**Key: c**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 3. 2. Queue slots: 5. 3. Extra thread slots: 5 - 3 = 2. 4. The first call after all are used is call 5 + 5 + 1 = 11, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 28. seed 170100702570019459, level 1

A `ThreadPoolExecutor` has `corePoolSize` 2, `maximumPoolSize` 5 and an `ArrayBlockingQueue` of capacity 2. Tasks that never finish are passed to `execute`. After 8 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 2, queued 6, rejected 0
b) threads 5, queued 0, rejected 3
c) threads 5, queued 2, rejected 1
d) threads 2, queued 2, rejected 4

**Key: c**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(8, 2) = 2. 2. Tasks queued: at most 2, here 2. 3. Extra threads started: 3. 4. Rejected: 8 - 5 - 2 = 1. Result: threads 5, queued 2, rejected 1. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 29. seed 2123441709795015565, level 1

A `ThreadPoolExecutor` has `corePoolSize` 2, `maximumPoolSize` 5 and an `ArrayBlockingQueue` of capacity 5. Tasks that never finish are passed to `execute`. After 8 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 2, queued 6, rejected 0
b) threads 3, queued 5, rejected 0
c) threads 5, queued 3, rejected 0
d) threads 5, queued 0, rejected 3

**Key: b**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(8, 2) = 2. 2. Tasks queued: at most 5, here 5. 3. Extra threads started: 1. 4. Rejected: 8 - 3 - 5 = 0. Result: threads 3, queued 5, rejected 0. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 30. seed 722055895351642669, level 1

A `ThreadPoolExecutor` has `corePoolSize` 1, `maximumPoolSize` 2 and an `ArrayBlockingQueue` of capacity 2. Tasks that never finish are passed to `execute`. After 7 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 1, queued 6, rejected 0
b) threads 1, queued 2, rejected 4
c) threads 2, queued 2, rejected 3
d) threads 2, queued 0, rejected 5

**Key: c**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(7, 1) = 1. 2. Tasks queued: at most 2, here 2. 3. Extra threads started: 1. 4. Rejected: 7 - 2 - 2 = 3. Result: threads 2, queued 2, rejected 3. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 31. seed 148541580333928838, level 1

A `ThreadPoolExecutor` has `corePoolSize` 2, `maximumPoolSize` 3 and an `ArrayBlockingQueue` of capacity 5. Tasks that never finish are passed to `execute`. After 11 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 3, queued 0, rejected 8
b) threads 3, queued 5, rejected 3
c) threads 2, queued 9, rejected 0
d) threads 2, queued 5, rejected 4

**Key: b**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(11, 2) = 2. 2. Tasks queued: at most 5, here 5. 3. Extra threads started: 1. 4. Rejected: 11 - 3 - 5 = 3. Result: threads 3, queued 5, rejected 3. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 32. seed 4176160540787290353, level 1

A `ThreadPoolExecutor` has `corePoolSize` 1, `maximumPoolSize` 4 and an `ArrayBlockingQueue` of capacity 4. Tasks that never finish are passed to `execute`. After 8 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 4, queued 4, rejected 0
b) threads 1, queued 7, rejected 0
c) threads 1, queued 4, rejected 3
d) threads 4, queued 0, rejected 4

**Key: a**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(8, 1) = 1. 2. Tasks queued: at most 4, here 4. 3. Extra threads started: 3. 4. Rejected: 8 - 4 - 4 = 0. Result: threads 4, queued 4, rejected 0. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 33. seed 4167400985073649575, level 1

A `ThreadPoolExecutor` has `corePoolSize` 1, `maximumPoolSize` 3 and an `ArrayBlockingQueue` of capacity 2. Tasks that never finish are passed to `execute`. After 4 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 1, queued 2, rejected 1
b) threads 1, queued 3, rejected 0
c) threads 3, queued 0, rejected 1
d) threads 2, queued 2, rejected 0

**Key: d**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(4, 1) = 1. 2. Tasks queued: at most 2, here 2. 3. Extra threads started: 1. 4. Rejected: 4 - 2 - 2 = 0. Result: threads 2, queued 2, rejected 0. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 34. seed 1007055162753262740, level 2

A `ThreadPoolExecutor` has `corePoolSize` 2, `maximumPoolSize` 4 and an `ArrayBlockingQueue` of capacity 2. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) 9
b) 6
c) call number 5
d) call 7

**Key: d**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 2. 2. Queue slots: 2. 3. Extra thread slots: 4 - 2 = 2. 4. The first call after all are used is call 4 + 2 + 1 = 7, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 35. seed 3594124642739142226, level 1

A `ThreadPoolExecutor` has `corePoolSize` 1, `maximumPoolSize` 4 and an `ArrayBlockingQueue` of capacity 5. Tasks that never finish are passed to `execute`. After 12 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 4, queued 0, rejected 8
b) threads 1, queued 5, rejected 6
c) threads 4, queued 5, rejected 3
d) threads 1, queued 11, rejected 0

**Key: c**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(12, 1) = 1. 2. Tasks queued: at most 5, here 5. 3. Extra threads started: 3. 4. Rejected: 12 - 4 - 5 = 3. Result: threads 4, queued 5, rejected 3. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 36. seed 2260071581046881832, level 1

A `ThreadPoolExecutor` has `corePoolSize` 3, `maximumPoolSize` 6 and an `ArrayBlockingQueue` of capacity 2. Tasks that never finish are passed to `execute`. After 9 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 6, queued 2, rejected 1
b) threads 3, queued 2, rejected 4
c) threads 3, queued 6, rejected 0
d) threads 6, queued 0, rejected 3

**Key: a**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(9, 3) = 3. 2. Tasks queued: at most 2, here 2. 3. Extra threads started: 3. 4. Rejected: 9 - 6 - 2 = 1. Result: threads 6, queued 2, rejected 1. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 37. seed 2118356044235691580, level 2

A `ThreadPoolExecutor` has `corePoolSize` 3, `maximumPoolSize` 4 and an `ArrayBlockingQueue` of capacity 2. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) call 10
b) call 7
c) call number 5
d) 6

**Key: b**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 3. 2. Queue slots: 2. 3. Extra thread slots: 4 - 3 = 1. 4. The first call after all are used is call 4 + 2 + 1 = 7, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 38. seed 3370616458246439110, level 2

A `ThreadPoolExecutor` has `corePoolSize` 3, `maximumPoolSize` 6 and an `ArrayBlockingQueue` of capacity 5. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) 12
b) call 7
c) call number 11
d) 15

**Key: a**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 3. 2. Queue slots: 5. 3. Extra thread slots: 6 - 3 = 3. 4. The first call after all are used is call 6 + 5 + 1 = 12, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 39. seed 3317768781245486701, level 2

A `ThreadPoolExecutor` has `corePoolSize` 3, `maximumPoolSize` 5 and an `ArrayBlockingQueue` of capacity 2. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) call number 8
b) call number 11
c) 6
d) call 7

**Key: a**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 3. 2. Queue slots: 2. 3. Extra thread slots: 5 - 3 = 2. 4. The first call after all are used is call 5 + 2 + 1 = 8, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 40. seed 2913747859769291046, level 1

A `ThreadPoolExecutor` has `corePoolSize` 1, `maximumPoolSize` 4 and an `ArrayBlockingQueue` of capacity 2. Tasks that never finish are passed to `execute`. After 9 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 1, queued 2, rejected 6
b) threads 4, queued 0, rejected 5
c) threads 4, queued 2, rejected 3
d) threads 1, queued 8, rejected 0

**Key: c**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(9, 1) = 1. 2. Tasks queued: at most 2, here 2. 3. Extra threads started: 3. 4. Rejected: 9 - 4 - 2 = 3. Result: threads 4, queued 2, rejected 3. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 41. seed 1917061604620069300, level 1

A `ThreadPoolExecutor` has `corePoolSize` 1, `maximumPoolSize` 3 and an `ArrayBlockingQueue` of capacity 3. Tasks that never finish are passed to `execute`. After 6 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 3, queued 3, rejected 0
b) threads 1, queued 5, rejected 0
c) threads 1, queued 3, rejected 2
d) threads 3, queued 0, rejected 3

**Key: a**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(6, 1) = 1. 2. Tasks queued: at most 3, here 3. 3. Extra threads started: 2. 4. Rejected: 6 - 3 - 3 = 0. Result: threads 3, queued 3, rejected 0. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 42. seed 2165969630143998050, level 1

A `ThreadPoolExecutor` has `corePoolSize` 2, `maximumPoolSize` 5 and an `ArrayBlockingQueue` of capacity 2. Tasks that never finish are passed to `execute`. After 7 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 5, queued 2, rejected 0
b) threads 5, queued 0, rejected 2
c) threads 2, queued 2, rejected 3
d) threads 2, queued 5, rejected 0

**Key: a**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(7, 2) = 2. 2. Tasks queued: at most 2, here 2. 3. Extra threads started: 3. 4. Rejected: 7 - 5 - 2 = 0. Result: threads 5, queued 2, rejected 0. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 43. seed 4307976017618285231, level 1

A `ThreadPoolExecutor` has `corePoolSize` 3, `maximumPoolSize` 5 and an `ArrayBlockingQueue` of capacity 5. Tasks that never finish are passed to `execute`. After 11 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 3, queued 5, rejected 3
b) threads 5, queued 5, rejected 1
c) threads 3, queued 8, rejected 0
d) threads 5, queued 0, rejected 6

**Key: b**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(11, 3) = 3. 2. Tasks queued: at most 5, here 5. 3. Extra threads started: 2. 4. Rejected: 11 - 5 - 5 = 1. Result: threads 5, queued 5, rejected 1. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 44. seed 2179748464664780411, level 2

A `ThreadPoolExecutor` has `corePoolSize` 2, `maximumPoolSize` 3 and an `ArrayBlockingQueue` of capacity 2. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) call number 5
b) call 4
c) call number 8
d) 6

**Key: d**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 2. 2. Queue slots: 2. 3. Extra thread slots: 3 - 2 = 1. 4. The first call after all are used is call 3 + 2 + 1 = 6, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 45. seed 456331042033710625, level 2

A `ThreadPoolExecutor` has `corePoolSize` 1, `maximumPoolSize` 4 and an `ArrayBlockingQueue` of capacity 2. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) 6
b) call number 8
c) call 4
d) call 7

**Key: d**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 1. 2. Queue slots: 2. 3. Extra thread slots: 4 - 1 = 3. 4. The first call after all are used is call 4 + 2 + 1 = 7, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 46. seed 3284033557419827098, level 1

A `ThreadPoolExecutor` has `corePoolSize` 3, `maximumPoolSize` 5 and an `ArrayBlockingQueue` of capacity 3. Tasks that never finish are passed to `execute`. After 7 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 4, queued 3, rejected 0
b) threads 5, queued 0, rejected 2
c) threads 3, queued 4, rejected 0
d) threads 3, queued 3, rejected 1

**Key: a**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(7, 3) = 3. 2. Tasks queued: at most 3, here 3. 3. Extra threads started: 1. 4. Rejected: 7 - 4 - 3 = 0. Result: threads 4, queued 3, rejected 0. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 47. seed 4590581867951500792, level 2

A `ThreadPoolExecutor` has `corePoolSize` 2, `maximumPoolSize` 5 and an `ArrayBlockingQueue` of capacity 2. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) call number 8
b) call 7
c) call 10
d) call number 5

**Key: a**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 2. 2. Queue slots: 2. 3. Extra thread slots: 5 - 2 = 3. 4. The first call after all are used is call 5 + 2 + 1 = 8, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 48. seed 3559274421763118161, level 1

A `ThreadPoolExecutor` has `corePoolSize` 2, `maximumPoolSize` 3 and an `ArrayBlockingQueue` of capacity 5. Tasks that never finish are passed to `execute`. After 10 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 3, queued 0, rejected 7
b) threads 2, queued 8, rejected 0
c) threads 2, queued 5, rejected 3
d) threads 3, queued 5, rejected 2

**Key: d**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(10, 2) = 2. 2. Tasks queued: at most 5, here 5. 3. Extra threads started: 1. 4. Rejected: 10 - 3 - 5 = 2. Result: threads 3, queued 5, rejected 2. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 49. seed 2498539387191912621, level 2

A `ThreadPoolExecutor` has `corePoolSize` 3, `maximumPoolSize` 6 and an `ArrayBlockingQueue` of capacity 5. Tasks that never finish are passed to `execute`. Which call is the first to be rejected?

a) 15
b) 9
c) call 7
d) 12

**Key: d**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads: 3. 2. Queue slots: 5. 3. Extra thread slots: 6 - 3 = 3. 4. The first call after all are used is call 6 + 5 + 1 = 12, which is rejected. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.

## 50. seed 4243934238371238205, level 1

A `ThreadPoolExecutor` has `corePoolSize` 1, `maximumPoolSize` 2 and an `ArrayBlockingQueue` of capacity 5. Tasks that never finish are passed to `execute`. After 10 calls, how many threads run, how many tasks wait in the queue and how many are rejected?

a) threads 2, queued 5, rejected 3
b) threads 1, queued 5, rejected 4
c) threads 1, queued 9, rejected 0
d) threads 2, queued 0, rejected 8

**Key: a**

Explanation: Each call starts a thread while fewer than `corePoolSize` run, otherwise queues the task while the queue has room, otherwise starts a thread while fewer than `maximumPoolSize` run, otherwise rejects it. 1. Core threads started: min(10, 1) = 1. 2. Tasks queued: at most 5, here 5. 3. Extra threads started: 1. 4. Rejected: 10 - 2 - 5 = 3. Result: threads 2, queued 5, rejected 3. Source: `javadoc-threadpoolexecutor#class-threadpoolexecutor`.
