# LRU cache contents (`lru-cache-contents`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 4185430573847231229, level 2

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(A)`, `get(B)`, `put(B)`, `put(A)`, `put(A)`, `get(D)`, `get(B)`, `get(A)`, `put(C)`, `put(E)`, which keys does it hold, from least to most recently used?

a) `[A, C, E]`
b) `[E, C, A]`
c) `[B, C, E]`
d) `[B, A, E]`

**Key: a**

Explanation: Keep the keys ordered by last use, oldest first: `put(A)` gives `[A]`; `get(B)` gives `[A]`; `put(B)` gives `[A, B]`; `put(A)` gives `[B, A]`; `put(A)` gives `[B, A]`; `get(D)` gives `[B, A]`; `get(B)` gives `[A, B]`; `get(A)` gives `[B, A]`; `put(C)` gives `[B, A, C]`; `put(E)` gives `[A, C, E]`.

## 2. seed 754741199252818838, level 1

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(D)`, `put(B)`, `put(C)`, `put(E)`, `get(B)`, `put(A)`, `put(E)`, `get(A)`, which keys does it hold, from least to most recently used?

a) `[A, E, B]`
b) `[B, E, A]`
c) `[C, A, E]`
d) `[D, E, A]`

**Key: b**

Explanation: Keep the keys ordered by last use, oldest first: `put(D)` gives `[D]`; `put(B)` gives `[D, B]`; `put(C)` gives `[D, B, C]`; `put(E)` gives `[B, C, E]`; `get(B)` gives `[C, E, B]`; `put(A)` gives `[E, B, A]`; `put(E)` gives `[B, A, E]`; `get(A)` gives `[B, E, A]`.

## 3. seed 1286210826307322020, level 1

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(A)`, `put(D)`, `put(D)`, `put(B)`, `put(C)`, `get(B)`, `put(B)`, `put(C)`, `get(D)`, which keys does it hold, from least to most recently used?

a) `[C, B, D]`
b) `[D, B, C]`
c) `[B, C, D]`
d) `[D, C, B]`

**Key: c**

Explanation: Keep the keys ordered by last use, oldest first: `put(A)` gives `[A]`; `put(D)` gives `[A, D]`; `put(D)` gives `[A, D]`; `put(B)` gives `[A, D, B]`; `put(C)` gives `[D, B, C]`; `get(B)` gives `[D, C, B]`; `put(B)` gives `[D, C, B]`; `put(C)` gives `[D, B, C]`; `get(D)` gives `[B, C, D]`.

## 4. seed 1498614041188636153, level 1

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(C)`, `put(D)`, `put(A)`, `get(A)`, `put(A)`, `put(E)`, `get(E)`, `put(D)`, which keys does it hold, from least to most recently used?

a) `[A, E, D]`
b) `[D, A, E]`
c) `[D, E, A]`
d) `[C, E, D]`

**Key: a**

Explanation: Keep the keys ordered by last use, oldest first: `put(C)` gives `[C]`; `put(D)` gives `[C, D]`; `put(A)` gives `[C, D, A]`; `get(A)` gives `[C, D, A]`; `put(A)` gives `[C, D, A]`; `put(E)` gives `[D, A, E]`; `get(E)` gives `[D, A, E]`; `put(D)` gives `[A, E, D]`.

## 5. seed 2138956946763850026, level 2

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(D)`, `put(B)`, `get(F)`, `put(E)`, `put(B)`, `get(F)`, `put(B)`, `put(F)`, `put(B)`, `put(D)`, which keys does it hold, from least to most recently used?

a) `[D, B, F]`
b) `[E, F, D]`
c) `[F, B, D]`
d) `[E, B, D]`

**Key: c**

Explanation: Keep the keys ordered by last use, oldest first: `put(D)` gives `[D]`; `put(B)` gives `[D, B]`; `get(F)` gives `[D, B]`; `put(E)` gives `[D, B, E]`; `put(B)` gives `[D, E, B]`; `get(F)` gives `[D, E, B]`; `put(B)` gives `[D, E, B]`; `put(F)` gives `[E, B, F]`; `put(B)` gives `[E, F, B]`; `put(D)` gives `[F, B, D]`.

## 6. seed 3736398155006468503, level 1

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(B)`, `put(D)`, `get(E)`, `put(B)`, `put(A)`, `put(C)`, `put(B)`, `put(C)`, `put(E)`, which keys does it hold, from least to most recently used?

a) `[B, C, E]`
b) `[D, B, E]`
c) `[E, C, B]`
d) `[C, B, E]`

**Key: a**

Explanation: Keep the keys ordered by last use, oldest first: `put(B)` gives `[B]`; `put(D)` gives `[B, D]`; `get(E)` gives `[B, D]`; `put(B)` gives `[D, B]`; `put(A)` gives `[D, B, A]`; `put(C)` gives `[B, A, C]`; `put(B)` gives `[A, C, B]`; `put(C)` gives `[A, B, C]`; `put(E)` gives `[B, C, E]`.

## 7. seed 2814281946570347148, level 1

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(B)`, `put(B)`, `get(B)`, `put(C)`, `put(E)`, `put(D)`, `put(E)`, `get(D)`, which keys does it hold, from least to most recently used?

a) `[C, D, E]`
b) `[D, E, C]`
c) `[C, E, D]`
d) `[B, C, E]`

**Key: c**

Explanation: Keep the keys ordered by last use, oldest first: `put(B)` gives `[B]`; `put(B)` gives `[B]`; `get(B)` gives `[B]`; `put(C)` gives `[B, C]`; `put(E)` gives `[B, C, E]`; `put(D)` gives `[C, E, D]`; `put(E)` gives `[C, D, E]`; `get(D)` gives `[C, E, D]`.

## 8. seed 2414309487676626670, level 1

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(B)`, `get(C)`, `get(B)`, `put(E)`, `put(D)`, `put(E)`, `put(A)`, which keys does it hold, from least to most recently used?

a) `[E, D, A]`
b) `[A, E, D]`
c) `[B, D, A]`
d) `[D, E, A]`

**Key: d**

Explanation: Keep the keys ordered by last use, oldest first: `put(B)` gives `[B]`; `get(C)` gives `[B]`; `get(B)` gives `[B]`; `put(E)` gives `[B, E]`; `put(D)` gives `[B, E, D]`; `put(E)` gives `[B, D, E]`; `put(A)` gives `[D, E, A]`.

## 9. seed 1775199101388007378, level 1

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(F)`, `get(D)`, `put(A)`, `put(C)`, `put(D)`, `get(F)`, `put(D)`, which keys does it hold, from least to most recently used?

a) `[A, C, D, F]`
b) `[F, A, C, D]`
c) `[D, F, C, A]`
d) `[A, C, F, D]`

**Key: d**

Explanation: Keep the keys ordered by last use, oldest first: `put(F)` gives `[F]`; `get(D)` gives `[F]`; `put(A)` gives `[F, A]`; `put(C)` gives `[F, A, C]`; `put(D)` gives `[F, A, C, D]`; `get(F)` gives `[A, C, D, F]`; `put(D)` gives `[A, C, F, D]`.

## 10. seed 3548963076235759306, level 2

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `get(A)`, `put(A)`, `put(F)`, `get(E)`, `put(C)`, `put(A)`, `get(D)`, `put(A)`, `put(E)`, `put(E)`, `put(F)`, which keys does it hold, from least to most recently used?

a) `[F, E, A]`
b) `[C, E, F]`
c) `[F, C, E]`
d) `[A, E, F]`

**Key: d**

Explanation: Keep the keys ordered by last use, oldest first: `get(A)` gives `[]`; `put(A)` gives `[A]`; `put(F)` gives `[A, F]`; `get(E)` gives `[A, F]`; `put(C)` gives `[A, F, C]`; `put(A)` gives `[F, C, A]`; `get(D)` gives `[F, C, A]`; `put(A)` gives `[F, C, A]`; `put(E)` gives `[C, A, E]`; `put(E)` gives `[C, A, E]`; `put(F)` gives `[A, E, F]`.

## 11. seed 4066327859357230861, level 2

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(F)`, `get(C)`, `put(A)`, `get(A)`, `get(F)`, `put(D)`, `get(F)`, `get(A)`, `put(G)`, `put(F)`, `put(B)`, which keys does it hold, from least to most recently used?

a) `[A, G, F, B]`
b) `[F, A, G, B]`
c) `[B, F, G, A]`
d) `[A, D, G, B]`

**Key: a**

Explanation: Keep the keys ordered by last use, oldest first: `put(F)` gives `[F]`; `get(C)` gives `[F]`; `put(A)` gives `[F, A]`; `get(A)` gives `[F, A]`; `get(F)` gives `[A, F]`; `put(D)` gives `[A, F, D]`; `get(F)` gives `[A, D, F]`; `get(A)` gives `[D, F, A]`; `put(G)` gives `[D, F, A, G]`; `put(F)` gives `[D, A, G, F]`; `put(B)` gives `[A, G, F, B]`.

## 12. seed 4565996755554108709, level 2

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `get(F)`, `put(C)`, `put(A)`, `get(G)`, `put(B)`, `get(G)`, `get(A)`, `put(G)`, `put(B)`, `put(C)`, which keys does it hold, from least to most recently used?

a) `[C, B, A, G]`
b) `[A, G, B, C]`
c) `[C, B, G, A]`
d) `[C, A, B, G]`

**Key: b**

Explanation: Keep the keys ordered by last use, oldest first: `get(F)` gives `[]`; `put(C)` gives `[C]`; `put(A)` gives `[C, A]`; `get(G)` gives `[C, A]`; `put(B)` gives `[C, A, B]`; `get(G)` gives `[C, A, B]`; `get(A)` gives `[C, B, A]`; `put(G)` gives `[C, B, A, G]`; `put(B)` gives `[C, A, G, B]`; `put(C)` gives `[A, G, B, C]`.

## 13. seed 315217183229194652, level 1

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `get(F)`, `put(C)`, `put(E)`, `put(B)`, `put(E)`, `get(C)`, `get(A)`, `put(F)`, which keys does it hold, from least to most recently used?

a) `[C, B, E, F]`
b) `[C, E, B, F]`
c) `[F, C, E, B]`
d) `[B, E, C, F]`

**Key: d**

Explanation: Keep the keys ordered by last use, oldest first: `get(F)` gives `[]`; `put(C)` gives `[C]`; `put(E)` gives `[C, E]`; `put(B)` gives `[C, E, B]`; `put(E)` gives `[C, B, E]`; `get(C)` gives `[B, E, C]`; `get(A)` gives `[B, E, C]`; `put(F)` gives `[B, E, C, F]`.

## 14. seed 3349576493491500999, level 2

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(E)`, `get(C)`, `put(E)`, `put(F)`, `get(C)`, `put(F)`, `get(E)`, `put(C)`, `put(D)`, which keys does it hold, from least to most recently used?

a) `[F, C, D]`
b) `[F, E, D]`
c) `[E, C, D]`
d) `[D, C, E]`

**Key: c**

Explanation: Keep the keys ordered by last use, oldest first: `put(E)` gives `[E]`; `get(C)` gives `[E]`; `put(E)` gives `[E]`; `put(F)` gives `[E, F]`; `get(C)` gives `[E, F]`; `put(F)` gives `[E, F]`; `get(E)` gives `[F, E]`; `put(C)` gives `[F, E, C]`; `put(D)` gives `[E, C, D]`.

## 15. seed 501958830257674129, level 2

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(A)`, `put(E)`, `get(C)`, `get(A)`, `put(F)`, `put(B)`, `get(C)`, `get(G)`, `put(F)`, `put(A)`, `put(D)`, which keys does it hold, from least to most recently used?

a) `[E, B, F, D]`
b) `[B, F, A, D]`
c) `[D, A, F, B]`
d) `[E, F, B, D]`

**Key: b**

Explanation: Keep the keys ordered by last use, oldest first: `put(A)` gives `[A]`; `put(E)` gives `[A, E]`; `get(C)` gives `[A, E]`; `get(A)` gives `[E, A]`; `put(F)` gives `[E, A, F]`; `put(B)` gives `[E, A, F, B]`; `get(C)` gives `[E, A, F, B]`; `get(G)` gives `[E, A, F, B]`; `put(F)` gives `[E, A, B, F]`; `put(A)` gives `[E, B, F, A]`; `put(D)` gives `[B, F, A, D]`.

## 16. seed 2820873367741946594, level 2

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `get(F)`, `put(E)`, `put(C)`, `put(D)`, `put(A)`, `put(B)`, `put(B)`, `get(C)`, `get(E)`, `put(D)`, `put(E)`, which keys does it hold, from least to most recently used?

a) `[B, D, E]`
b) `[E, D, B]`
c) `[B, C, E]`
d) `[A, B, E]`

**Key: a**

Explanation: Keep the keys ordered by last use, oldest first: `get(F)` gives `[]`; `put(E)` gives `[E]`; `put(C)` gives `[E, C]`; `put(D)` gives `[E, C, D]`; `put(A)` gives `[C, D, A]`; `put(B)` gives `[D, A, B]`; `put(B)` gives `[D, A, B]`; `get(C)` gives `[D, A, B]`; `get(E)` gives `[D, A, B]`; `put(D)` gives `[A, B, D]`; `put(E)` gives `[B, D, E]`.

## 17. seed 3744004482735692481, level 1

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(B)`, `get(A)`, `put(E)`, `put(E)`, `put(B)`, `put(A)`, `put(D)`, `put(D)`, `get(D)`, which keys does it hold, from least to most recently used?

a) `[E, B, D]`
b) `[D, A, B]`
c) `[E, A, D]`
d) `[B, A, D]`

**Key: d**

Explanation: Keep the keys ordered by last use, oldest first: `put(B)` gives `[B]`; `get(A)` gives `[B]`; `put(E)` gives `[B, E]`; `put(E)` gives `[B, E]`; `put(B)` gives `[E, B]`; `put(A)` gives `[E, B, A]`; `put(D)` gives `[B, A, D]`; `put(D)` gives `[B, A, D]`; `get(D)` gives `[B, A, D]`.

## 18. seed 2942210611190207656, level 2

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `get(C)`, `put(D)`, `put(A)`, `get(E)`, `get(B)`, `put(C)`, `put(F)`, `put(E)`, `put(C)`, `put(E)`, `put(A)`, which keys does it hold, from least to most recently used?

a) `[A, E, C]`
b) `[F, E, A]`
c) `[D, E, A]`
d) `[C, E, A]`

**Key: d**

Explanation: Keep the keys ordered by last use, oldest first: `get(C)` gives `[]`; `put(D)` gives `[D]`; `put(A)` gives `[D, A]`; `get(E)` gives `[D, A]`; `get(B)` gives `[D, A]`; `put(C)` gives `[D, A, C]`; `put(F)` gives `[A, C, F]`; `put(E)` gives `[C, F, E]`; `put(C)` gives `[F, E, C]`; `put(E)` gives `[F, C, E]`; `put(A)` gives `[C, E, A]`.

## 19. seed 2498211414702168166, level 2

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `get(E)`, `put(F)`, `put(C)`, `put(E)`, `put(E)`, `put(F)`, `get(B)`, `get(B)`, `put(D)`, `put(B)`, `put(B)`, which keys does it hold, from least to most recently used?

a) `[B, D, F]`
b) `[F, D, B]`
c) `[C, E, B]`
d) `[E, D, B]`

**Key: b**

Explanation: Keep the keys ordered by last use, oldest first: `get(E)` gives `[]`; `put(F)` gives `[F]`; `put(C)` gives `[F, C]`; `put(E)` gives `[F, C, E]`; `put(E)` gives `[F, C, E]`; `put(F)` gives `[C, E, F]`; `get(B)` gives `[C, E, F]`; `get(B)` gives `[C, E, F]`; `put(D)` gives `[E, F, D]`; `put(B)` gives `[F, D, B]`; `put(B)` gives `[F, D, B]`.

## 20. seed 877434806255538195, level 2

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `get(F)`, `get(C)`, `put(C)`, `put(D)`, `put(D)`, `put(F)`, `get(D)`, `put(E)`, `put(D)`, `put(D)`, `put(E)`, which keys does it hold, from least to most recently used?

a) `[C, F, E]`
b) `[D, F, E]`
c) `[E, D, F]`
d) `[F, D, E]`

**Key: d**

Explanation: Keep the keys ordered by last use, oldest first: `get(F)` gives `[]`; `get(C)` gives `[]`; `put(C)` gives `[C]`; `put(D)` gives `[C, D]`; `put(D)` gives `[C, D]`; `put(F)` gives `[C, D, F]`; `get(D)` gives `[C, F, D]`; `put(E)` gives `[F, D, E]`; `put(D)` gives `[F, E, D]`; `put(D)` gives `[F, E, D]`; `put(E)` gives `[F, D, E]`.

## 21. seed 3150422216191307235, level 2

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(E)`, `put(A)`, `get(D)`, `get(C)`, `put(C)`, `put(F)`, `put(F)`, `put(C)`, `get(B)`, `get(E)`, `get(E)`, which keys does it hold, from least to most recently used?

a) `[A, F, C]`
b) `[A, C, E]`
c) `[C, F, A]`
d) `[A, C, F]`

**Key: a**

Explanation: Keep the keys ordered by last use, oldest first: `put(E)` gives `[E]`; `put(A)` gives `[E, A]`; `get(D)` gives `[E, A]`; `get(C)` gives `[E, A]`; `put(C)` gives `[E, A, C]`; `put(F)` gives `[A, C, F]`; `put(F)` gives `[A, C, F]`; `put(C)` gives `[A, F, C]`; `get(B)` gives `[A, F, C]`; `get(E)` gives `[A, F, C]`; `get(E)` gives `[A, F, C]`.

## 22. seed 437233973761604004, level 2

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(A)`, `put(C)`, `get(F)`, `put(B)`, `put(G)`, `put(G)`, `put(F)`, `get(B)`, `put(E)`, `put(F)`, `put(F)`, which keys does it hold, from least to most recently used?

a) `[A, C, E, F]`
b) `[G, F, B, E]`
c) `[G, B, E, F]`
d) `[F, E, B, G]`

**Key: c**

Explanation: Keep the keys ordered by last use, oldest first: `put(A)` gives `[A]`; `put(C)` gives `[A, C]`; `get(F)` gives `[A, C]`; `put(B)` gives `[A, C, B]`; `put(G)` gives `[A, C, B, G]`; `put(G)` gives `[A, C, B, G]`; `put(F)` gives `[C, B, G, F]`; `get(B)` gives `[C, G, F, B]`; `put(E)` gives `[G, F, B, E]`; `put(F)` gives `[G, B, E, F]`; `put(F)` gives `[G, B, E, F]`.

## 23. seed 3114179063437603087, level 2

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `get(F)`, `put(A)`, `put(F)`, `put(B)`, `get(D)`, `get(C)`, `get(E)`, `put(C)`, `put(B)`, `get(D)`, `put(A)`, which keys does it hold, from least to most recently used?

a) `[F, B, A]`
b) `[A, B, C]`
c) `[B, C, A]`
d) `[C, B, A]`

**Key: d**

Explanation: Keep the keys ordered by last use, oldest first: `get(F)` gives `[]`; `put(A)` gives `[A]`; `put(F)` gives `[A, F]`; `put(B)` gives `[A, F, B]`; `get(D)` gives `[A, F, B]`; `get(C)` gives `[A, F, B]`; `get(E)` gives `[A, F, B]`; `put(C)` gives `[F, B, C]`; `put(B)` gives `[F, C, B]`; `get(D)` gives `[F, C, B]`; `put(A)` gives `[C, B, A]`.

## 24. seed 1673211241339679067, level 1

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(E)`, `put(A)`, `put(C)`, `put(B)`, `get(C)`, `put(E)`, `put(B)`, which keys does it hold, from least to most recently used?

a) `[B, E, C]`
b) `[B, C, E]`
c) `[C, E, B]`
d) `[C, B, E]`

**Key: c**

Explanation: Keep the keys ordered by last use, oldest first: `put(E)` gives `[E]`; `put(A)` gives `[E, A]`; `put(C)` gives `[E, A, C]`; `put(B)` gives `[A, C, B]`; `get(C)` gives `[A, B, C]`; `put(E)` gives `[B, C, E]`; `put(B)` gives `[C, E, B]`.

## 25. seed 1298538816616357902, level 1

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(D)`, `put(B)`, `put(B)`, `put(A)`, `put(B)`, `put(E)`, `put(C)`, which keys does it hold, from least to most recently used?

a) `[B, A, E, C]`
b) `[C, E, B, A]`
c) `[A, B, E, C]`
d) `[D, A, B, C]`

**Key: c**

Explanation: Keep the keys ordered by last use, oldest first: `put(D)` gives `[D]`; `put(B)` gives `[D, B]`; `put(B)` gives `[D, B]`; `put(A)` gives `[D, B, A]`; `put(B)` gives `[D, A, B]`; `put(E)` gives `[D, A, B, E]`; `put(C)` gives `[A, B, E, C]`.

## 26. seed 1664053512881368151, level 1

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(E)`, `put(C)`, `put(A)`, `put(B)`, `put(A)`, `put(D)`, `put(D)`, `put(C)`, `put(C)`, which keys does it hold, from least to most recently used?

a) `[E, D, C]`
b) `[A, D, C]`
c) `[B, D, C]`
d) `[C, D, A]`

**Key: b**

Explanation: Keep the keys ordered by last use, oldest first: `put(E)` gives `[E]`; `put(C)` gives `[E, C]`; `put(A)` gives `[E, C, A]`; `put(B)` gives `[C, A, B]`; `put(A)` gives `[C, B, A]`; `put(D)` gives `[B, A, D]`; `put(D)` gives `[B, A, D]`; `put(C)` gives `[A, D, C]`; `put(C)` gives `[A, D, C]`.

## 27. seed 2146865810382987836, level 2

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(F)`, `put(C)`, `put(D)`, `put(E)`, `put(G)`, `put(D)`, `get(D)`, `get(E)`, `put(E)`, `put(G)`, which keys does it hold, from least to most recently used?

a) `[C, D, E, G]`
b) `[F, C, E, G]`
c) `[G, E, D, C]`
d) `[C, G, D, E]`

**Key: a**

Explanation: Keep the keys ordered by last use, oldest first: `put(F)` gives `[F]`; `put(C)` gives `[F, C]`; `put(D)` gives `[F, C, D]`; `put(E)` gives `[F, C, D, E]`; `put(G)` gives `[C, D, E, G]`; `put(D)` gives `[C, E, G, D]`; `get(D)` gives `[C, E, G, D]`; `get(E)` gives `[C, G, D, E]`; `put(E)` gives `[C, G, D, E]`; `put(G)` gives `[C, D, E, G]`.

## 28. seed 1864641723512560558, level 1

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `get(F)`, `get(B)`, `put(B)`, `put(E)`, `get(B)`, `put(F)`, `put(A)`, `put(E)`, `get(D)`, which keys does it hold, from least to most recently used?

a) `[E, B, F, A]`
b) `[B, F, A, E]`
c) `[B, E, F, A]`
d) `[E, A, F, B]`

**Key: b**

Explanation: Keep the keys ordered by last use, oldest first: `get(F)` gives `[]`; `get(B)` gives `[]`; `put(B)` gives `[B]`; `put(E)` gives `[B, E]`; `get(B)` gives `[E, B]`; `put(F)` gives `[E, B, F]`; `put(A)` gives `[E, B, F, A]`; `put(E)` gives `[B, F, A, E]`; `get(D)` gives `[B, F, A, E]`.

## 29. seed 2248628635371634443, level 1

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `get(C)`, `get(B)`, `put(C)`, `put(B)`, `put(E)`, `get(B)`, `get(D)`, `put(D)`, which keys does it hold, from least to most recently used?

a) `[D, B, E]`
b) `[E, B, D]`
c) `[B, E, D]`
d) `[C, E, D]`

**Key: b**

Explanation: Keep the keys ordered by last use, oldest first: `get(C)` gives `[]`; `get(B)` gives `[]`; `put(C)` gives `[C]`; `put(B)` gives `[C, B]`; `put(E)` gives `[C, B, E]`; `get(B)` gives `[C, E, B]`; `get(D)` gives `[C, E, B]`; `put(D)` gives `[E, B, D]`.

## 30. seed 3743159150940259824, level 1

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(A)`, `get(F)`, `get(D)`, `get(B)`, `put(D)`, `put(A)`, `put(B)`, `put(E)`, `put(F)`, which keys does it hold, from least to most recently used?

a) `[A, B, E, F]`
b) `[F, E, B, A]`
c) `[D, A, B, F]`
d) `[D, B, E, F]`

**Key: a**

Explanation: Keep the keys ordered by last use, oldest first: `put(A)` gives `[A]`; `get(F)` gives `[A]`; `get(D)` gives `[A]`; `get(B)` gives `[A]`; `put(D)` gives `[A, D]`; `put(A)` gives `[D, A]`; `put(B)` gives `[D, A, B]`; `put(E)` gives `[D, A, B, E]`; `put(F)` gives `[A, B, E, F]`.

## 31. seed 1812817898158764753, level 2

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `get(F)`, `put(E)`, `put(F)`, `get(E)`, `get(D)`, `put(E)`, `put(D)`, `put(D)`, `get(B)`, `put(B)`, `put(D)`, which keys does it hold, from least to most recently used?

a) `[E, F, D, B]`
b) `[F, E, D, B]`
c) `[D, B, E, F]`
d) `[F, E, B, D]`

**Key: d**

Explanation: Keep the keys ordered by last use, oldest first: `get(F)` gives `[]`; `put(E)` gives `[E]`; `put(F)` gives `[E, F]`; `get(E)` gives `[F, E]`; `get(D)` gives `[F, E]`; `put(E)` gives `[F, E]`; `put(D)` gives `[F, E, D]`; `put(D)` gives `[F, E, D]`; `get(B)` gives `[F, E, D]`; `put(B)` gives `[F, E, D, B]`; `put(D)` gives `[F, E, B, D]`.

## 32. seed 2497910123638601090, level 1

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(F)`, `put(F)`, `put(D)`, `put(E)`, `get(B)`, `put(A)`, `put(E)`, `put(D)`, `put(C)`, which keys does it hold, from least to most recently used?

a) `[D, E, A, C]`
b) `[A, E, D, C]`
c) `[C, D, E, A]`
d) `[F, A, E, C]`

**Key: b**

Explanation: Keep the keys ordered by last use, oldest first: `put(F)` gives `[F]`; `put(F)` gives `[F]`; `put(D)` gives `[F, D]`; `put(E)` gives `[F, D, E]`; `get(B)` gives `[F, D, E]`; `put(A)` gives `[F, D, E, A]`; `put(E)` gives `[F, D, A, E]`; `put(D)` gives `[F, A, E, D]`; `put(C)` gives `[A, E, D, C]`.

## 33. seed 642553006397632288, level 1

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(E)`, `put(C)`, `put(C)`, `put(B)`, `get(A)`, `put(B)`, `put(F)`, `get(C)`, `put(D)`, which keys does it hold, from least to most recently used?

a) `[C, B, F, D]`
b) `[D, C, F, B]`
c) `[B, F, C, D]`
d) `[E, B, F, D]`

**Key: c**

Explanation: Keep the keys ordered by last use, oldest first: `put(E)` gives `[E]`; `put(C)` gives `[E, C]`; `put(C)` gives `[E, C]`; `put(B)` gives `[E, C, B]`; `get(A)` gives `[E, C, B]`; `put(B)` gives `[E, C, B]`; `put(F)` gives `[E, C, B, F]`; `get(C)` gives `[E, B, F, C]`; `put(D)` gives `[B, F, C, D]`.

## 34. seed 1160407430209429221, level 1

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(B)`, `put(A)`, `get(A)`, `put(B)`, `put(E)`, `put(B)`, `get(B)`, `put(B)`, `put(A)`, which keys does it hold, from least to most recently used?

a) `[E, B, A]`
b) `[A, B, E]`
c) `[B, A, E]`
d) `[A, E, B]`

**Key: a**

Explanation: Keep the keys ordered by last use, oldest first: `put(B)` gives `[B]`; `put(A)` gives `[B, A]`; `get(A)` gives `[B, A]`; `put(B)` gives `[A, B]`; `put(E)` gives `[A, B, E]`; `put(B)` gives `[A, E, B]`; `get(B)` gives `[A, E, B]`; `put(B)` gives `[A, E, B]`; `put(A)` gives `[E, B, A]`.

## 35. seed 1678686547670317064, level 1

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(D)`, `put(C)`, `put(B)`, `get(D)`, `put(C)`, `get(C)`, `put(C)`, which keys does it hold, from least to most recently used?

a) `[B, D, C]`
b) `[C, D, B]`
c) `[D, B, C]`
d) `[D, C, B]`

**Key: a**

Explanation: Keep the keys ordered by last use, oldest first: `put(D)` gives `[D]`; `put(C)` gives `[D, C]`; `put(B)` gives `[D, C, B]`; `get(D)` gives `[C, B, D]`; `put(C)` gives `[B, D, C]`; `get(C)` gives `[B, D, C]`; `put(C)` gives `[B, D, C]`.

## 36. seed 2155072726611691364, level 2

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `get(C)`, `put(F)`, `put(B)`, `get(F)`, `put(C)`, `put(F)`, `put(F)`, `put(D)`, `put(B)`, which keys does it hold, from least to most recently used?

a) `[F, D, B]`
b) `[B, D, F]`
c) `[C, D, B]`
d) `[B, C, D]`

**Key: a**

Explanation: Keep the keys ordered by last use, oldest first: `get(C)` gives `[]`; `put(F)` gives `[F]`; `put(B)` gives `[F, B]`; `get(F)` gives `[B, F]`; `put(C)` gives `[B, F, C]`; `put(F)` gives `[B, C, F]`; `put(F)` gives `[B, C, F]`; `put(D)` gives `[C, F, D]`; `put(B)` gives `[F, D, B]`.

## 37. seed 3312215966886866536, level 1

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `get(C)`, `put(B)`, `put(A)`, `put(E)`, `put(D)`, `put(F)`, `put(B)`, `put(A)`, `get(B)`, which keys does it hold, from least to most recently used?

a) `[D, F, A, B]`
b) `[E, F, A, B]`
c) `[D, F, B, A]`
d) `[B, A, F, D]`

**Key: a**

Explanation: Keep the keys ordered by last use, oldest first: `get(C)` gives `[]`; `put(B)` gives `[B]`; `put(A)` gives `[B, A]`; `put(E)` gives `[B, A, E]`; `put(D)` gives `[B, A, E, D]`; `put(F)` gives `[A, E, D, F]`; `put(B)` gives `[E, D, F, B]`; `put(A)` gives `[D, F, B, A]`; `get(B)` gives `[D, F, A, B]`.

## 38. seed 1669531028749768352, level 2

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(A)`, `put(A)`, `get(C)`, `put(E)`, `put(B)`, `put(A)`, `put(E)`, `get(F)`, `get(E)`, `put(C)`, `get(E)`, which keys does it hold, from least to most recently used?

a) `[B, A, C]`
b) `[A, E, C]`
c) `[A, C, E]`
d) `[B, C, E]`

**Key: c**

Explanation: Keep the keys ordered by last use, oldest first: `put(A)` gives `[A]`; `put(A)` gives `[A]`; `get(C)` gives `[A]`; `put(E)` gives `[A, E]`; `put(B)` gives `[A, E, B]`; `put(A)` gives `[E, B, A]`; `put(E)` gives `[B, A, E]`; `get(F)` gives `[B, A, E]`; `get(E)` gives `[B, A, E]`; `put(C)` gives `[A, E, C]`; `get(E)` gives `[A, C, E]`.

## 39. seed 383829090651557243, level 1

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(B)`, `get(C)`, `get(C)`, `get(E)`, `put(E)`, `put(B)`, `put(A)`, `put(C)`, which keys does it hold, from least to most recently used?

a) `[E, B, C]`
b) `[B, A, C]`
c) `[E, A, C]`
d) `[C, A, B]`

**Key: b**

Explanation: Keep the keys ordered by last use, oldest first: `put(B)` gives `[B]`; `get(C)` gives `[B]`; `get(C)` gives `[B]`; `get(E)` gives `[B]`; `put(E)` gives `[B, E]`; `put(B)` gives `[E, B]`; `put(A)` gives `[E, B, A]`; `put(C)` gives `[B, A, C]`.

## 40. seed 2266326884818323810, level 2

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `get(C)`, `get(B)`, `put(A)`, `put(D)`, `put(B)`, `put(C)`, `get(A)`, `put(F)`, `get(C)`, `put(B)`, which keys does it hold, from least to most recently used?

a) `[B, C, F]`
b) `[B, F, C]`
c) `[D, F, B]`
d) `[F, C, B]`

**Key: d**

Explanation: Keep the keys ordered by last use, oldest first: `get(C)` gives `[]`; `get(B)` gives `[]`; `put(A)` gives `[A]`; `put(D)` gives `[A, D]`; `put(B)` gives `[A, D, B]`; `put(C)` gives `[D, B, C]`; `get(A)` gives `[D, B, C]`; `put(F)` gives `[B, C, F]`; `get(C)` gives `[B, F, C]`; `put(B)` gives `[F, C, B]`.

## 41. seed 2984408297701914603, level 1

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(E)`, `get(B)`, `put(F)`, `put(A)`, `put(E)`, `put(C)`, `get(E)`, `put(A)`, which keys does it hold, from least to most recently used?

a) `[E, F, A, C]`
b) `[F, A, C, E]`
c) `[F, C, E, A]`
d) `[F, E, C, A]`

**Key: c**

Explanation: Keep the keys ordered by last use, oldest first: `put(E)` gives `[E]`; `get(B)` gives `[E]`; `put(F)` gives `[E, F]`; `put(A)` gives `[E, F, A]`; `put(E)` gives `[F, A, E]`; `put(C)` gives `[F, A, E, C]`; `get(E)` gives `[F, A, C, E]`; `put(A)` gives `[F, C, E, A]`.

## 42. seed 2847655589441079914, level 1

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(D)`, `put(B)`, `put(A)`, `put(B)`, `get(D)`, `put(C)`, `put(E)`, `get(E)`, `put(C)`, which keys does it hold, from least to most recently used?

a) `[D, E, C]`
b) `[B, E, C]`
c) `[A, B, C]`
d) `[C, E, D]`

**Key: a**

Explanation: Keep the keys ordered by last use, oldest first: `put(D)` gives `[D]`; `put(B)` gives `[D, B]`; `put(A)` gives `[D, B, A]`; `put(B)` gives `[D, A, B]`; `get(D)` gives `[A, B, D]`; `put(C)` gives `[B, D, C]`; `put(E)` gives `[D, C, E]`; `get(E)` gives `[D, C, E]`; `put(C)` gives `[D, E, C]`.

## 43. seed 396724179920159068, level 1

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(D)`, `put(E)`, `put(F)`, `put(B)`, `put(C)`, `get(D)`, `get(E)`, which keys does it hold, from least to most recently used?

a) `[F, B, C, E]`
b) `[F, C, D, E]`
c) `[E, F, B, C]`
d) `[E, C, B, F]`

**Key: a**

Explanation: Keep the keys ordered by last use, oldest first: `put(D)` gives `[D]`; `put(E)` gives `[D, E]`; `put(F)` gives `[D, E, F]`; `put(B)` gives `[D, E, F, B]`; `put(C)` gives `[E, F, B, C]`; `get(D)` gives `[E, F, B, C]`; `get(E)` gives `[F, B, C, E]`.

## 44. seed 737349061854077292, level 1

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(B)`, `get(C)`, `put(E)`, `put(D)`, `put(B)`, `put(D)`, `get(B)`, `put(A)`, which keys does it hold, from least to most recently used?

a) `[E, D, A]`
b) `[A, B, D]`
c) `[B, D, A]`
d) `[D, B, A]`

**Key: d**

Explanation: Keep the keys ordered by last use, oldest first: `put(B)` gives `[B]`; `get(C)` gives `[B]`; `put(E)` gives `[B, E]`; `put(D)` gives `[B, E, D]`; `put(B)` gives `[E, D, B]`; `put(D)` gives `[E, B, D]`; `get(B)` gives `[E, D, B]`; `put(A)` gives `[D, B, A]`.

## 45. seed 3591149957269187210, level 2

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(A)`, `put(A)`, `get(F)`, `put(B)`, `put(D)`, `put(C)`, `get(D)`, `put(F)`, `get(D)`, `get(D)`, `get(D)`, which keys does it hold, from least to most recently used?

a) `[D, F, C]`
b) `[C, F, D]`
c) `[D, C, F]`
d) `[A, B, F]`

**Key: b**

Explanation: Keep the keys ordered by last use, oldest first: `put(A)` gives `[A]`; `put(A)` gives `[A]`; `get(F)` gives `[A]`; `put(B)` gives `[A, B]`; `put(D)` gives `[A, B, D]`; `put(C)` gives `[B, D, C]`; `get(D)` gives `[B, C, D]`; `put(F)` gives `[C, D, F]`; `get(D)` gives `[C, F, D]`; `get(D)` gives `[C, F, D]`; `get(D)` gives `[C, F, D]`.

## 46. seed 2956182154233607276, level 1

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(F)`, `put(A)`, `put(B)`, `get(F)`, `put(D)`, `get(F)`, `put(B)`, which keys does it hold, from least to most recently used?

a) `[A, D, F, B]`
b) `[F, A, D, B]`
c) `[B, F, D, A]`
d) `[F, A, B, D]`

**Key: a**

Explanation: Keep the keys ordered by last use, oldest first: `put(F)` gives `[F]`; `put(A)` gives `[F, A]`; `put(B)` gives `[F, A, B]`; `get(F)` gives `[A, B, F]`; `put(D)` gives `[A, B, F, D]`; `get(F)` gives `[A, B, D, F]`; `put(B)` gives `[A, D, F, B]`.

## 47. seed 3987017675493733351, level 2

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(A)`, `get(F)`, `get(D)`, `put(B)`, `put(D)`, `get(E)`, `put(E)`, `get(G)`, `put(F)`, `get(E)`, which keys does it hold, from least to most recently used?

a) `[E, F, D, B]`
b) `[B, D, F, E]`
c) `[B, D, E, F]`
d) `[A, B, D, F]`

**Key: b**

Explanation: Keep the keys ordered by last use, oldest first: `put(A)` gives `[A]`; `get(F)` gives `[A]`; `get(D)` gives `[A]`; `put(B)` gives `[A, B]`; `put(D)` gives `[A, B, D]`; `get(E)` gives `[A, B, D]`; `put(E)` gives `[A, B, D, E]`; `get(G)` gives `[A, B, D, E]`; `put(F)` gives `[B, D, E, F]`; `get(E)` gives `[B, D, F, E]`.

## 48. seed 2956833380833082609, level 2

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `get(A)`, `put(E)`, `put(D)`, `get(E)`, `put(G)`, `get(F)`, `put(B)`, `put(E)`, `put(E)`, `put(A)`, which keys does it hold, from least to most recently used?

a) `[D, G, B, A]`
b) `[E, G, B, A]`
c) `[G, B, E, A]`
d) `[A, E, B, G]`

**Key: c**

Explanation: Keep the keys ordered by last use, oldest first: `get(A)` gives `[]`; `put(E)` gives `[E]`; `put(D)` gives `[E, D]`; `get(E)` gives `[D, E]`; `put(G)` gives `[D, E, G]`; `get(F)` gives `[D, E, G]`; `put(B)` gives `[D, E, G, B]`; `put(E)` gives `[D, G, B, E]`; `put(E)` gives `[D, G, B, E]`; `put(A)` gives `[G, B, E, A]`.

## 49. seed 2416012660608302150, level 1

An LRU cache of capacity 4 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `put(C)`, `put(A)`, `put(E)`, `get(D)`, `get(A)`, `put(E)`, `put(C)`, `put(B)`, `put(D)`, which keys does it hold, from least to most recently used?

a) `[E, C, B, D]`
b) `[D, B, C, E]`
c) `[A, E, B, D]`
d) `[A, E, C, D]`

**Key: a**

Explanation: Keep the keys ordered by last use, oldest first: `put(C)` gives `[C]`; `put(A)` gives `[C, A]`; `put(E)` gives `[C, A, E]`; `get(D)` gives `[C, A, E]`; `get(A)` gives `[C, E, A]`; `put(E)` gives `[C, A, E]`; `put(C)` gives `[A, E, C]`; `put(B)` gives `[A, E, C, B]`; `put(D)` gives `[E, C, B, D]`.

## 50. seed 4005867901981252807, level 2

An LRU cache of capacity 3 starts empty. A `get` of a missing key changes nothing; a `put` of a new key evicts the least recently used entry when the cache is full. Both `get` and `put` of an existing key count as a use. After `get(F)`, `put(B)`, `put(D)`, `put(A)`, `get(D)`, `get(E)`, `put(C)`, `put(C)`, `put(F)`, `get(B)`, which keys does it hold, from least to most recently used?

a) `[F, C, D]`
b) `[A, F, B]`
c) `[D, C, F]`
d) `[A, C, F]`

**Key: c**

Explanation: Keep the keys ordered by last use, oldest first: `get(F)` gives `[]`; `put(B)` gives `[B]`; `put(D)` gives `[B, D]`; `put(A)` gives `[B, D, A]`; `get(D)` gives `[B, A, D]`; `get(E)` gives `[B, A, D]`; `put(C)` gives `[A, D, C]`; `put(C)` gives `[A, D, C]`; `put(F)` gives `[D, C, F]`; `get(B)` gives `[D, C, F]`.
