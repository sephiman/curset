# Visit order of breadth-first and depth-first search (`graph-traversal-order`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 1226667521660359350, level 2

An undirected graph on vertices 0 to 6 has edges `0-6`, `1-5`, `1-6`, `2-5`, `4-5`, `4-6`, `5-6`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 1, 2, 4, 5, 6`
b) `2, 4, 5, 1, 6, 0`
c) `0, 6, 1, 5, 2, 4`
d) `0, 6, 1, 4, 5, 2`

**Key: c**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 6 at depth 1; 3. enter 1 at depth 2; 4. enter 5 at depth 3; 5. enter 2 at depth 4; 6. enter 4 at depth 4. Visit order: `0, 6, 1, 5, 2, 4`. Not reachable from 0, so never visited: 3. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 2. seed 565741401341220598, level 2

An undirected graph on vertices 0 to 6 has edges `0-4`, `2-6`, `3-4`, `3-6`, `4-5`, `4-6`, `5-6`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 4, 3, 5, 6, 2`
b) `0, 2, 3, 4, 5, 6`
c) `2, 5, 6, 3, 4, 0`
d) `0, 4, 3, 6, 2, 5`

**Key: d**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 4 at depth 1; 3. enter 3 at depth 2; 4. enter 6 at depth 3; 5. enter 2 at depth 4; 6. enter 5 at depth 4. Visit order: `0, 4, 3, 6, 2, 5`. Not reachable from 0, so never visited: 1. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 3. seed 4135261864004265620, level 1

An undirected graph on vertices 0 to 5 has edges `0-2`, `0-3`, `1-2`, `1-3`, `2-3`, `3-4`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 2, 3, 1, 4`
b) `0, 2, 1, 3, 4`
c) `4, 3, 1, 2, 0`
d) `0, 3, 4, 2, 1`

**Key: b**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 2 at depth 1; 3. enter 1 at depth 2; 4. enter 3 at depth 3; 5. enter 4 at depth 4. Visit order: `0, 2, 1, 3, 4`. Not reachable from 0, so never visited: 5. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 4. seed 4203112821357859921, level 2

An undirected graph on vertices 0 to 6 has edges `0-2`, `1-2`, `1-4`, `1-5`, `2-4`, `2-5`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `4, 5, 1, 2, 0`
b) `0, 2, 1, 4, 5`
c) `0, 2, 5, 1, 4`
d) `0, 1, 2, 4, 5`

**Key: b**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 2 at depth 1; 3. enter 1 at depth 2; 4. enter 4 at depth 3; 5. enter 5 at depth 3. Visit order: `0, 2, 1, 4, 5`. Not reachable from 0, so never visited: 3, 6. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 5. seed 4297056550111252657, level 2

An undirected graph on vertices 0 to 6 has edges `0-1`, `0-4`, `0-6`, `1-2`, `1-3`, `2-6`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 1, 2, 6, 3, 4`
b) `0, 6, 2, 1, 3, 4`
c) `0, 1, 4, 6, 2, 3`
d) `0, 1, 2, 3, 4, 6`

**Key: a**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 1 at depth 1; 3. enter 2 at depth 2; 4. enter 6 at depth 3; 5. enter 3 at depth 2; 6. enter 4 at depth 1. Visit order: `0, 1, 2, 6, 3, 4`. Not reachable from 0, so never visited: 5. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 6. seed 2659253974202666934, level 1

An undirected graph on vertices 0 to 5 has edges `0-2`, `1-3`, `2-3`, `2-4`, `3-4`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 1, 2, 3, 4`
b) `0, 2, 4, 3, 1`
c) `0, 2, 3, 1, 4`
d) `0, 2, 3, 4, 1`

**Key: d**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 2; 2. take 2 from the queue, then add 3 and 4; 3. take 3 from the queue, then add 1; 4. take 4 from the queue, then add nothing; 5. take 1 from the queue, then add nothing. Visit order: `0, 2, 3, 4, 1`. Not reachable from 0, so never visited: 5. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.

## 7. seed 2225862767974562471, level 1

An undirected graph on vertices 0 to 5 has edges `0-2`, `1-2`, `1-4`, `2-3`, `2-4`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 1, 2, 3, 4`
b) `0, 2, 1, 4, 3`
c) `0, 2, 4, 1, 3`
d) `0, 2, 1, 3, 4`

**Key: b**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 2 at depth 1; 3. enter 1 at depth 2; 4. enter 4 at depth 3; 5. enter 3 at depth 2. Visit order: `0, 2, 1, 4, 3`. Not reachable from 0, so never visited: 5. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 8. seed 1307350775546313414, level 1

An undirected graph on vertices 0 to 5 has edges `0-3`, `0-5`, `1-4`, `3-4`, `3-5`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 3, 5, 4, 1`
b) `0, 3, 4, 1, 5`
c) `0, 1, 3, 4, 5`
d) `1, 4, 5, 3, 0`

**Key: b**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 3 at depth 1; 3. enter 4 at depth 2; 4. enter 1 at depth 3; 5. enter 5 at depth 2. Visit order: `0, 3, 4, 1, 5`. Not reachable from 0, so never visited: 2. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 9. seed 2547577025920708243, level 2

An undirected graph on vertices 0 to 6 has edges `0-4`, `1-3`, `1-4`, `2-4`, `2-6`, `3-6`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 4, 2, 6, 3, 1`
b) `2, 6, 3, 1, 4, 0`
c) `0, 4, 1, 3, 6, 2`
d) `0, 4, 1, 2, 3, 6`

**Key: c**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 4 at depth 1; 3. enter 1 at depth 2; 4. enter 3 at depth 3; 5. enter 6 at depth 4; 6. enter 2 at depth 5. Visit order: `0, 4, 1, 3, 6, 2`. Not reachable from 0, so never visited: 5. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 10. seed 2904186326326909983, level 2

An undirected graph on vertices 0 to 6 has edges `0-1`, `0-2`, `0-4`, `0-6`, `2-3`, `3-4`, `4-6`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `1, 6, 4, 3, 2, 0`
b) `0, 6, 4, 3, 2, 1`
c) `0, 1, 2, 3, 4, 6`
d) `0, 1, 2, 4, 6, 3`

**Key: c**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 1 at depth 1; 3. enter 2 at depth 1; 4. enter 3 at depth 2; 5. enter 4 at depth 3; 6. enter 6 at depth 4. Visit order: `0, 1, 2, 3, 4, 6`. Not reachable from 0, so never visited: 5. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 11. seed 606963052777633126, level 2

An undirected graph on vertices 0 to 6 has edges `0-4`, `0-5`, `1-2`, `1-4`, `1-5`, `4-6`, `5-6`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 5, 6, 4, 1, 2`
b) `0, 4, 5, 1, 6, 2`
c) `0, 1, 2, 4, 5, 6`
d) `0, 4, 1, 2, 5, 6`

**Key: b**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 4 and 5; 2. take 4 from the queue, then add 1 and 6; 3. take 5 from the queue, then add nothing; 4. take 1 from the queue, then add 2; 5. take 6 from the queue, then add nothing; 6. take 2 from the queue, then add nothing. Visit order: `0, 4, 5, 1, 6, 2`. Not reachable from 0, so never visited: 3. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.

## 12. seed 2711152120517698321, level 2

An undirected graph on vertices 0 to 6 has edges `0-2`, `1-5`, `2-3`, `2-5`, `3-4`, `4-5`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 2, 5, 4, 3, 1`
b) `1, 5, 4, 3, 2, 0`
c) `0, 2, 3, 4, 5, 1`
d) `0, 1, 2, 3, 4, 5`

**Key: c**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 2 at depth 1; 3. enter 3 at depth 2; 4. enter 4 at depth 3; 5. enter 5 at depth 4; 6. enter 1 at depth 5. Visit order: `0, 2, 3, 4, 5, 1`. Not reachable from 0, so never visited: 6. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 13. seed 3934676284829537093, level 2

An undirected graph on vertices 0 to 6 has edges `0-5`, `1-3`, `1-5`, `4-5`, `4-6`, `5-6`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 5, 6, 4, 1, 3`
b) `3, 1, 6, 4, 5, 0`
c) `0, 5, 1, 3, 4, 6`
d) `0, 5, 1, 4, 6, 3`

**Key: c**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 5 at depth 1; 3. enter 1 at depth 2; 4. enter 3 at depth 3; 5. enter 4 at depth 2; 6. enter 6 at depth 3. Visit order: `0, 5, 1, 3, 4, 6`. Not reachable from 0, so never visited: 2. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 14. seed 353967426516586878, level 2

An undirected graph on vertices 0 to 6 has edges `0-2`, `0-3`, `0-6`, `2-6`, `3-6`, `4-5`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 6, 3, 2`
b) `0, 2, 3, 6`
c) `3, 6, 2, 0`
d) `0, 2, 6, 3`

**Key: d**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 2 at depth 1; 3. enter 6 at depth 2; 4. enter 3 at depth 3. Visit order: `0, 2, 6, 3`. Not reachable from 0, so never visited: 1, 4, 5. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 15. seed 4443124052750776457, level 1

An undirected graph on vertices 0 to 5 has edges `0-2`, `1-2`, `1-3`, `2-3`, `2-5`, `3-5`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 1, 2, 3, 5`
b) `5, 3, 1, 2, 0`
c) `0, 2, 1, 3, 5`
d) `0, 2, 5, 3, 1`

**Key: c**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 2 at depth 1; 3. enter 1 at depth 2; 4. enter 3 at depth 3; 5. enter 5 at depth 4. Visit order: `0, 2, 1, 3, 5`. Not reachable from 0, so never visited: 4. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 16. seed 4018487807505532220, level 2

An undirected graph on vertices 0 to 6 has edges `0-5`, `1-2`, `2-4`, `2-5`, `2-6`, `4-6`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 5, 2, 1, 4, 6`
b) `1, 6, 4, 2, 5, 0`
c) `0, 5, 2, 6, 4, 1`
d) `0, 1, 2, 4, 5, 6`

**Key: a**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 5 at depth 1; 3. enter 2 at depth 2; 4. enter 1 at depth 3; 5. enter 4 at depth 3; 6. enter 6 at depth 4. Visit order: `0, 5, 2, 1, 4, 6`. Not reachable from 0, so never visited: 3. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 17. seed 517980978299556589, level 2

An undirected graph on vertices 0 to 6 has edges `0-1`, `0-4`, `0-5`, `0-6`, `1-6`, `3-6`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 6, 5, 4, 1, 3`
b) `0, 6, 3, 1, 5, 4`
c) `0, 1, 4, 5, 6, 3`
d) `0, 1, 6, 3, 4, 5`

**Key: c**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 1, 4, 5 and 6; 2. take 1 from the queue, then add nothing; 3. take 4 from the queue, then add nothing; 4. take 5 from the queue, then add nothing; 5. take 6 from the queue, then add 3; 6. take 3 from the queue, then add nothing. Visit order: `0, 1, 4, 5, 6, 3`. Not reachable from 0, so never visited: 2. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.

## 18. seed 4309269512421543784, level 1

An undirected graph on vertices 0 to 5 has edges `0-3`, `0-4`, `1-3`, `3-5`, `4-5`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 4, 5, 3, 1`
b) `0, 1, 3, 4, 5`
c) `0, 3, 1, 5, 4`
d) `0, 3, 4, 1, 5`

**Key: c**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 3 at depth 1; 3. enter 1 at depth 2; 4. enter 5 at depth 2; 5. enter 4 at depth 3. Visit order: `0, 3, 1, 5, 4`. Not reachable from 0, so never visited: 2. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 19. seed 3191841735272820687, level 1

An undirected graph on vertices 0 to 5 has edges `0-1`, `0-3`, `0-4`, `2-4`, `3-4`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `1, 2, 4, 3, 0`
b) `0, 4, 3, 2, 1`
c) `0, 1, 2, 3, 4`
d) `0, 1, 3, 4, 2`

**Key: d**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 1 at depth 1; 3. enter 3 at depth 1; 4. enter 4 at depth 2; 5. enter 2 at depth 3. Visit order: `0, 1, 3, 4, 2`. Not reachable from 0, so never visited: 5. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 20. seed 829298490219062280, level 2

An undirected graph on vertices 0 to 6 has edges `0-1`, `0-5`, `0-6`, `1-2`, `1-5`, `2-5`, `5-6`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 1, 2, 5, 6`
b) `6, 5, 2, 1, 0`
c) `0, 6, 5, 2, 1`
d) `0, 1, 5, 6, 2`

**Key: a**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 1 at depth 1; 3. enter 2 at depth 2; 4. enter 5 at depth 3; 5. enter 6 at depth 4. Visit order: `0, 1, 2, 5, 6`. Not reachable from 0, so never visited: 3, 4. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 21. seed 1101727340994445535, level 2

An undirected graph on vertices 0 to 6 has edges `0-2`, `0-3`, `0-6`, `3-4`, `3-6`, `4-5`, `4-6`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 2, 3, 4, 5, 6`
b) `0, 6, 4, 5, 3, 2`
c) `0, 6, 3, 2, 4, 5`
d) `0, 2, 3, 6, 4, 5`

**Key: d**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 2, 3 and 6; 2. take 2 from the queue, then add nothing; 3. take 3 from the queue, then add 4; 4. take 6 from the queue, then add nothing; 5. take 4 from the queue, then add 5; 6. take 5 from the queue, then add nothing. Visit order: `0, 2, 3, 6, 4, 5`. Not reachable from 0, so never visited: 1. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.

## 22. seed 681736094781612496, level 2

An undirected graph on vertices 0 to 6 has edges `0-3`, `1-4`, `1-5`, `3-4`, `3-6`, `5-6`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `6, 5, 1, 4, 3, 0`
b) `0, 1, 3, 4, 5, 6`
c) `0, 3, 4, 1, 5, 6`
d) `0, 3, 6, 5, 1, 4`

**Key: c**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 3 at depth 1; 3. enter 4 at depth 2; 4. enter 1 at depth 3; 5. enter 5 at depth 4; 6. enter 6 at depth 5. Visit order: `0, 3, 4, 1, 5, 6`. Not reachable from 0, so never visited: 2. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 23. seed 980287719817048140, level 2

An undirected graph on vertices 0 to 6 has edges `0-4`, `0-5`, `1-2`, `1-5`, `2-4`, `4-6`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 4, 5, 2, 6, 1`
b) `5, 1, 2, 6, 4, 0`
c) `0, 1, 2, 4, 5, 6`
d) `0, 4, 2, 1, 5, 6`

**Key: d**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 4 at depth 1; 3. enter 2 at depth 2; 4. enter 1 at depth 3; 5. enter 5 at depth 4; 6. enter 6 at depth 2. Visit order: `0, 4, 2, 1, 5, 6`. Not reachable from 0, so never visited: 3. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 24. seed 2997490779500431146, level 2

An undirected graph on vertices 0 to 6 has edges `0-1`, `0-5`, `0-6`, `1-5`, `2-4`, `3-6`, `5-6`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 1, 5, 6, 3`
b) `0, 1, 3, 5, 6`
c) `0, 6, 5, 1, 3`
d) `3, 6, 5, 1, 0`

**Key: a**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 1 at depth 1; 3. enter 5 at depth 2; 4. enter 6 at depth 3; 5. enter 3 at depth 4. Visit order: `0, 1, 5, 6, 3`. Not reachable from 0, so never visited: 2, 4. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 25. seed 1803596914577871503, level 2

An undirected graph on vertices 0 to 6 has edges `0-1`, `0-4`, `0-6`, `1-4`, `2-6`, `5-6`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 6, 5, 2, 4, 1`
b) `4, 1, 2, 5, 6, 0`
c) `0, 1, 4, 6, 2, 5`
d) `0, 1, 2, 4, 5, 6`

**Key: c**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 1 at depth 1; 3. enter 4 at depth 2; 4. enter 6 at depth 1; 5. enter 2 at depth 2; 6. enter 5 at depth 2. Visit order: `0, 1, 4, 6, 2, 5`. Not reachable from 0, so never visited: 3. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 26. seed 898641101888108795, level 2

An undirected graph on vertices 0 to 6 has edges `0-1`, `0-2`, `0-3`, `1-3`, `3-4`, `4-5`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 3, 4, 5, 1, 2`
b) `0, 3, 2, 1, 4, 5`
c) `0, 1, 3, 4, 5, 2`
d) `0, 1, 2, 3, 4, 5`

**Key: d**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 1, 2 and 3; 2. take 1 from the queue, then add nothing; 3. take 2 from the queue, then add nothing; 4. take 3 from the queue, then add 4; 5. take 4 from the queue, then add 5; 6. take 5 from the queue, then add nothing. Visit order: `0, 1, 2, 3, 4, 5`. Not reachable from 0, so never visited: 6. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.

## 27. seed 3308899281055082042, level 2

An undirected graph on vertices 0 to 6 has edges `0-6`, `1-3`, `1-4`, `2-3`, `2-4`, `3-6`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 6, 3, 2, 4, 1`
b) `0, 6, 3, 1, 4, 2`
c) `2, 4, 1, 3, 6, 0`
d) `0, 1, 2, 3, 4, 6`

**Key: b**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 6 at depth 1; 3. enter 3 at depth 2; 4. enter 1 at depth 3; 5. enter 4 at depth 4; 6. enter 2 at depth 5. Visit order: `0, 6, 3, 1, 4, 2`. Not reachable from 0, so never visited: 5. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 28. seed 166730885213359529, level 2

An undirected graph on vertices 0 to 6 has edges `0-2`, `0-4`, `0-6`, `2-3`, `3-5`, `4-5`, `4-6`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 2, 4, 6, 3, 5`
b) `0, 2, 3, 5, 4, 6`
c) `0, 6, 4, 5, 3, 2`
d) `0, 6, 4, 2, 5, 3`

**Key: a**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 2, 4 and 6; 2. take 2 from the queue, then add 3; 3. take 4 from the queue, then add 5; 4. take 6 from the queue, then add nothing; 5. take 3 from the queue, then add nothing; 6. take 5 from the queue, then add nothing. Visit order: `0, 2, 4, 6, 3, 5`. Not reachable from 0, so never visited: 1. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.

## 29. seed 995007566717398208, level 2

An undirected graph on vertices 0 to 6 has edges `0-1`, `1-2`, `1-3`, `2-3`, `3-6`, `4-6`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 1, 2, 3, 6, 4`
b) `0, 1, 3, 2, 6, 4`
c) `0, 1, 2, 3, 4, 6`
d) `0, 1, 3, 6, 4, 2`

**Key: a**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 1; 2. take 1 from the queue, then add 2 and 3; 3. take 2 from the queue, then add nothing; 4. take 3 from the queue, then add 6; 5. take 6 from the queue, then add 4; 6. take 4 from the queue, then add nothing. Visit order: `0, 1, 2, 3, 6, 4`. Not reachable from 0, so never visited: 5. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.

## 30. seed 1623702483493450814, level 1

An undirected graph on vertices 0 to 5 has edges `0-4`, `1-4`, `1-5`, `2-4`, `2-5`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 4, 2, 5, 1`
b) `0, 1, 2, 4, 5`
c) `2, 5, 1, 4, 0`
d) `0, 4, 1, 5, 2`

**Key: d**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 4 at depth 1; 3. enter 1 at depth 2; 4. enter 5 at depth 3; 5. enter 2 at depth 4. Visit order: `0, 4, 1, 5, 2`. Not reachable from 0, so never visited: 3. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 31. seed 2722662842019861555, level 1

An undirected graph on vertices 0 to 5 has edges `0-1`, `0-2`, `0-5`, `1-4`, `1-5`, `2-4`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 5, 1, 4, 2`
b) `0, 1, 2, 5, 4`
c) `0, 1, 4, 2, 5`
d) `0, 1, 2, 4, 5`

**Key: c**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 1 at depth 1; 3. enter 4 at depth 2; 4. enter 2 at depth 3; 5. enter 5 at depth 2. Visit order: `0, 1, 4, 2, 5`. Not reachable from 0, so never visited: 3. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 32. seed 2424051307044254219, level 1

An undirected graph on vertices 0 to 5 has edges `0-3`, `0-4`, `2-3`, `2-4`, `3-5`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 2, 3, 4, 5`
b) `0, 4, 3, 5, 2`
c) `0, 3, 4, 2, 5`
d) `0, 4, 3, 2, 5`

**Key: c**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 3 and 4; 2. take 3 from the queue, then add 2 and 5; 3. take 4 from the queue, then add nothing; 4. take 2 from the queue, then add nothing; 5. take 5 from the queue, then add nothing. Visit order: `0, 3, 4, 2, 5`. Not reachable from 0, so never visited: 1. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.

## 33. seed 519142501417208695, level 2

An undirected graph on vertices 0 to 6 has edges `0-4`, `1-4`, `1-5`, `1-6`, `3-5`, `4-6`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 4, 1, 6, 5, 3`
b) `0, 1, 3, 4, 5, 6`
c) `0, 4, 1, 5, 3, 6`
d) `0, 4, 6, 1, 5, 3`

**Key: a**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 4; 2. take 4 from the queue, then add 1 and 6; 3. take 1 from the queue, then add 5; 4. take 6 from the queue, then add nothing; 5. take 5 from the queue, then add 3; 6. take 3 from the queue, then add nothing. Visit order: `0, 4, 1, 6, 5, 3`. Not reachable from 0, so never visited: 2. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.

## 34. seed 885675929064082268, level 1

An undirected graph on vertices 0 to 5 has edges `0-3`, `0-4`, `1-3`, `2-4`, `3-4`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `1, 2, 4, 3, 0`
b) `0, 3, 1, 4, 2`
c) `0, 1, 2, 3, 4`
d) `0, 4, 3, 1, 2`

**Key: b**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 3 at depth 1; 3. enter 1 at depth 2; 4. enter 4 at depth 2; 5. enter 2 at depth 3. Visit order: `0, 3, 1, 4, 2`. Not reachable from 0, so never visited: 5. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 35. seed 629026423479796252, level 1

An undirected graph on vertices 0 to 5 has edges `0-1`, `0-4`, `1-3`, `1-5`, `3-5`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 1, 4, 3, 5`
b) `0, 1, 3, 4, 5`
c) `0, 4, 1, 5, 3`
d) `0, 1, 3, 5, 4`

**Key: a**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 1 and 4; 2. take 1 from the queue, then add 3 and 5; 3. take 4 from the queue, then add nothing; 4. take 3 from the queue, then add nothing; 5. take 5 from the queue, then add nothing. Visit order: `0, 1, 4, 3, 5`. Not reachable from 0, so never visited: 2. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.

## 36. seed 457461898715117302, level 1

An undirected graph on vertices 0 to 5 has edges `0-1`, `0-3`, `0-4`, `1-3`, `2-3`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 1, 3, 4, 2`
b) `0, 4, 3, 2, 1`
c) `0, 1, 3, 2, 4`
d) `0, 1, 2, 3, 4`

**Key: c**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 1 at depth 1; 3. enter 3 at depth 2; 4. enter 2 at depth 3; 5. enter 4 at depth 1. Visit order: `0, 1, 3, 2, 4`. Not reachable from 0, so never visited: 5. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 37. seed 242837566831233328, level 2

An undirected graph on vertices 0 to 6 has edges `0-1`, `0-2`, `0-5`, `1-2`, `2-6`, `3-5`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `6, 2, 1, 3, 5, 0`
b) `0, 1, 2, 3, 5, 6`
c) `0, 1, 2, 5, 6, 3`
d) `0, 1, 2, 6, 5, 3`

**Key: d**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 1 at depth 1; 3. enter 2 at depth 2; 4. enter 6 at depth 3; 5. enter 5 at depth 1; 6. enter 3 at depth 2. Visit order: `0, 1, 2, 6, 5, 3`. Not reachable from 0, so never visited: 4. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 38. seed 2006297606955156396, level 1

An undirected graph on vertices 0 to 5 has edges `0-1`, `0-3`, `1-2`, `1-3`, `2-3`, `2-4`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 1, 3, 2, 4`
b) `0, 1, 2, 3, 4`
c) `0, 3, 1, 2, 4`
d) `0, 3, 2, 4, 1`

**Key: a**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 1 and 3; 2. take 1 from the queue, then add 2; 3. take 3 from the queue, then add nothing; 4. take 2 from the queue, then add 4; 5. take 4 from the queue, then add nothing. Visit order: `0, 1, 3, 2, 4`. Not reachable from 0, so never visited: 5. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.

## 39. seed 238571280617887483, level 1

An undirected graph on vertices 0 to 5 has edges `0-3`, `1-3`, `1-4`, `2-4`, `3-4`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 3, 4, 2, 1`
b) `2, 4, 1, 3, 0`
c) `0, 3, 1, 4, 2`
d) `0, 1, 2, 3, 4`

**Key: c**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 3 at depth 1; 3. enter 1 at depth 2; 4. enter 4 at depth 3; 5. enter 2 at depth 4. Visit order: `0, 3, 1, 4, 2`. Not reachable from 0, so never visited: 5. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 40. seed 1834881934996493291, level 2

An undirected graph on vertices 0 to 6 has edges `0-2`, `0-5`, `1-2`, `1-4`, `4-5`, `5-6`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 5, 6, 4, 1, 2`
b) `0, 5, 2, 6, 4, 1`
c) `0, 2, 5, 1, 4, 6`
d) `0, 2, 1, 4, 5, 6`

**Key: c**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 2 and 5; 2. take 2 from the queue, then add 1; 3. take 5 from the queue, then add 4 and 6; 4. take 1 from the queue, then add nothing; 5. take 4 from the queue, then add nothing; 6. take 6 from the queue, then add nothing. Visit order: `0, 2, 5, 1, 4, 6`. Not reachable from 0, so never visited: 3. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.

## 41. seed 3986661743875329405, level 2

An undirected graph on vertices 0 to 6 has edges `0-1`, `0-6`, `1-4`, `1-5`, `3-6`, `4-5`, `4-6`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 1, 6, 4, 5, 3`
b) `0, 1, 3, 4, 5, 6`
c) `0, 6, 1, 4, 3, 5`
d) `0, 6, 1, 3, 5, 4`

**Key: a**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 1 and 6; 2. take 1 from the queue, then add 4 and 5; 3. take 6 from the queue, then add 3; 4. take 4 from the queue, then add nothing; 5. take 5 from the queue, then add nothing; 6. take 3 from the queue, then add nothing. Visit order: `0, 1, 6, 4, 5, 3`. Not reachable from 0, so never visited: 2. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.

## 42. seed 3487582649914102955, level 1

An undirected graph on vertices 0 to 5 has edges `0-3`, `0-4`, `0-5`, `2-4`, `3-4`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 2, 3, 4, 5`
b) `0, 3, 4, 2, 5`
c) `0, 5, 4, 3, 2`
d) `0, 3, 4, 5, 2`

**Key: d**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 3, 4 and 5; 2. take 3 from the queue, then add nothing; 3. take 4 from the queue, then add 2; 4. take 5 from the queue, then add nothing; 5. take 2 from the queue, then add nothing. Visit order: `0, 3, 4, 5, 2`. Not reachable from 0, so never visited: 1. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.

## 43. seed 1183575387796351228, level 1

An undirected graph on vertices 0 to 5 has edges `0-1`, `0-3`, `1-2`, `2-3`, `2-5`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 1, 2, 3, 5`
b) `0, 3, 2, 5, 1`
c) `0, 1, 3, 2, 5`
d) `0, 3, 1, 2, 5`

**Key: c**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 1 and 3; 2. take 1 from the queue, then add 2; 3. take 3 from the queue, then add nothing; 4. take 2 from the queue, then add 5; 5. take 5 from the queue, then add nothing. Visit order: `0, 1, 3, 2, 5`. Not reachable from 0, so never visited: 4. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.

## 44. seed 4050890399592749485, level 1

An undirected graph on vertices 0 to 5 has edges `0-2`, `0-3`, `0-5`, `1-2`, `2-3`, `2-5`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 2, 3, 5, 1`
b) `0, 5, 2, 3, 1`
c) `0, 2, 1, 3, 5`
d) `0, 1, 2, 3, 5`

**Key: a**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 2, 3 and 5; 2. take 2 from the queue, then add 1; 3. take 3 from the queue, then add nothing; 4. take 5 from the queue, then add nothing; 5. take 1 from the queue, then add nothing. Visit order: `0, 2, 3, 5, 1`. Not reachable from 0, so never visited: 4. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.

## 45. seed 21863907172160064, level 1

An undirected graph on vertices 0 to 5 has edges `0-1`, `0-3`, `0-4`, `0-5`, `1-5`, `4-5`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 5, 4, 1, 3`
b) `0, 1, 5, 4, 3`
c) `0, 5, 4, 3, 1`
d) `0, 1, 3, 4, 5`

**Key: d**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 1, 3, 4 and 5; 2. take 1 from the queue, then add nothing; 3. take 3 from the queue, then add nothing; 4. take 4 from the queue, then add nothing; 5. take 5 from the queue, then add nothing. Visit order: `0, 1, 3, 4, 5`. Not reachable from 0, so never visited: 2. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.

## 46. seed 1225590543510003062, level 2

An undirected graph on vertices 0 to 6 has edges `0-1`, `0-4`, `0-6`, `1-2`, `1-5`, `1-6`, `2-6`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 6, 4, 1, 2, 5`
b) `0, 1, 4, 6, 2, 5`
c) `0, 1, 2, 4, 5, 6`
d) `0, 1, 2, 6, 5, 4`

**Key: b**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 1, 4 and 6; 2. take 1 from the queue, then add 2 and 5; 3. take 4 from the queue, then add nothing; 4. take 6 from the queue, then add nothing; 5. take 2 from the queue, then add nothing; 6. take 5 from the queue, then add nothing. Visit order: `0, 1, 4, 6, 2, 5`. Not reachable from 0, so never visited: 3. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.

## 47. seed 519861820875416318, level 2

An undirected graph on vertices 0 to 6 has edges `0-4`, `0-6`, `1-6`, `2-4`, `2-5`, `2-6`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 6, 4, 1, 2, 5`
b) `0, 6, 4, 2, 1, 5`
c) `0, 4, 2, 5, 6, 1`
d) `0, 4, 6, 2, 1, 5`

**Key: d**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 4 and 6; 2. take 4 from the queue, then add 2; 3. take 6 from the queue, then add 1; 4. take 2 from the queue, then add 5; 5. take 1 from the queue, then add nothing; 6. take 5 from the queue, then add nothing. Visit order: `0, 4, 6, 2, 1, 5`. Not reachable from 0, so never visited: 3. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.

## 48. seed 1136755872645647932, level 2

An undirected graph on vertices 0 to 6 has edges `0-4`, `0-5`, `1-3`, `2-6`, `4-5`, `5-6`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 5, 6, 2, 4`
b) `2, 6, 5, 4, 0`
c) `0, 4, 5, 6, 2`
d) `0, 2, 4, 5, 6`

**Key: c**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 4 at depth 1; 3. enter 5 at depth 2; 4. enter 6 at depth 3; 5. enter 2 at depth 4. Visit order: `0, 4, 5, 6, 2`. Not reachable from 0, so never visited: 1, 3. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 49. seed 3450354606234927464, level 1

An undirected graph on vertices 0 to 5 has edges `0-3`, `1-2`, `1-4`, `2-3`, `2-4`. Neighbours are taken in increasing order. In what order does a recursive depth-first search from `0` visit the vertices?

a) `0, 3, 2, 1, 4`
b) `4, 1, 2, 3, 0`
c) `0, 1, 2, 3, 4`
d) `0, 3, 2, 4, 1`

**Key: a**

Explanation: A recursive depth-first search enters the first unseen neighbour before the next one. Steps: 1. enter 0 at depth 0; 2. enter 3 at depth 1; 3. enter 2 at depth 2; 4. enter 1 at depth 3; 5. enter 4 at depth 4. Visit order: `0, 3, 2, 1, 4`. Not reachable from 0, so never visited: 5. Source: `ods-12-3-graph-traversal#SECTION001532000000000000000`.

## 50. seed 4063597829198941178, level 1

An undirected graph on vertices 0 to 5 has edges `0-1`, `0-4`, `1-3`, `1-4`, `3-5`. Neighbours are taken in increasing order. In what order does a queue-based breadth-first search from `0` visit the vertices?

a) `0, 1, 3, 5, 4`
b) `0, 4, 1, 3, 5`
c) `0, 1, 4, 3, 5`
d) `0, 1, 3, 4, 5`

**Key: c**

Explanation: A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours. Steps: 1. take 0 from the queue, then add 1 and 4; 2. take 1 from the queue, then add 3; 3. take 4 from the queue, then add nothing; 4. take 3 from the queue, then add 5; 5. take 5 from the queue, then add nothing. Visit order: `0, 1, 4, 3, 5`. Not reachable from 0, so never visited: 2. Source: `ods-12-3-graph-traversal#SECTION001531000000000000000`.
