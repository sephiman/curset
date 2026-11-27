# Topological orderings (`topological-order-valid`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 3032124957098265275, level 2

A directed graph on vertices 0 to 5 has edges `0->1`, `0->3`, `2->3`, `2->5`, `3->1`, `3->5`, `4->3`, `4->5`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `1, 5, 3, 0, 2, 4`
b) `0, 1, 2, 3, 4, 5`
c) `0, 2, 3, 4, 1, 5`
d) `4, 2, 0, 3, 5, 1`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `4, 2, 0, 3, 5, 1`. Checking each edge: 1. `0->1` has 0 at place 3 and 1 at place 6; 2. `0->3` has 0 at place 3 and 3 at place 4; 3. `2->3` has 2 at place 2 and 3 at place 4; 4. `2->5` has 2 at place 2 and 5 at place 5; 5. `3->1` has 3 at place 4 and 1 at place 6; 6. `3->5` has 3 at place 4 and 5 at place 5; 7. `4->3` has 4 at place 1 and 3 at place 4; 8. `4->5` has 4 at place 1 and 5 at place 5. Every tail is left of its head. The postorder itself, `1, 5, 3, 0, 2, 4`, fails on `0->1`. Source: `erickson-dfs#p8`.

## 2. seed 1157543864891684706, level 2

A directed graph on vertices 0 to 5 has edges `0->1`, `0->5`, `1->2`, `3->2`, `3->4`, `3->5`, `4->2`, `5->2`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `4, 0, 5, 1, 2, 3`
b) `3, 4, 0, 5, 1, 2`
c) `0, 1, 2, 3, 4, 5`
d) `3, 4, 1, 5, 0, 2`

**Key: b**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `3, 4, 0, 5, 1, 2`. Checking each edge: 1. `0->1` has 0 at place 3 and 1 at place 5; 2. `0->5` has 0 at place 3 and 5 at place 4; 3. `1->2` has 1 at place 5 and 2 at place 6; 4. `3->2` has 3 at place 1 and 2 at place 6; 5. `3->4` has 3 at place 1 and 4 at place 2; 6. `3->5` has 3 at place 1 and 5 at place 4; 7. `4->2` has 4 at place 2 and 2 at place 6; 8. `5->2` has 5 at place 4 and 2 at place 6. Every tail is left of its head. The postorder itself, `2, 1, 5, 0, 4, 3`, fails on `0->1`. Source: `erickson-dfs#p8`.

## 3. seed 964218836290855497, level 2

A directed graph on vertices 0 to 5 has edges `1->3`, `4->0`, `4->3`, `5->0`, `5->2`, `5->4`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `5, 4, 2, 1, 3, 0`
b) `0, 1, 2, 3, 4, 5`
c) `0, 3, 1, 2, 4, 5`
d) `4, 2, 1, 3, 0, 5`

**Key: a**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `5, 4, 2, 1, 3, 0`. Checking each edge: 1. `1->3` has 1 at place 4 and 3 at place 5; 2. `4->0` has 4 at place 2 and 0 at place 6; 3. `4->3` has 4 at place 2 and 3 at place 5; 4. `5->0` has 5 at place 1 and 0 at place 6; 5. `5->2` has 5 at place 1 and 2 at place 3; 6. `5->4` has 5 at place 1 and 4 at place 2. Every tail is left of its head. The postorder itself, `0, 3, 1, 2, 4, 5`, fails on `1->3`. Source: `erickson-dfs#p8`.

## 4. seed 76983462444890050, level 1

A directed graph on vertices 0 to 4 has edges `1->0`, `1->2`, `2->3`, `3->0`, `4->0`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `0, 3, 2, 1, 4`
b) `4, 0, 2, 3, 1`
c) `1, 2, 3, 0, 4`
d) `4, 1, 2, 3, 0`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `4, 1, 2, 3, 0`. Checking each edge: 1. `1->0` has 1 at place 2 and 0 at place 5; 2. `1->2` has 1 at place 2 and 2 at place 3; 3. `2->3` has 2 at place 3 and 3 at place 4; 4. `3->0` has 3 at place 4 and 0 at place 5; 5. `4->0` has 4 at place 1 and 0 at place 5. Every tail is left of its head. The postorder itself, `0, 3, 2, 1, 4`, fails on `1->0`. Source: `erickson-dfs#p8`.

## 5. seed 1596840395725148393, level 2

A directed graph on vertices 0 to 5 has edges `0->3`, `1->0`, `1->3`, `1->4`, `1->5`, `2->1`, `2->4`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `1, 5, 4, 0, 3, 2`
b) `2, 1, 5, 4, 3, 0`
c) `1, 2, 0, 3, 4, 5`
d) `2, 1, 5, 4, 0, 3`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `2, 1, 5, 4, 0, 3`. Checking each edge: 1. `0->3` has 0 at place 5 and 3 at place 6; 2. `1->0` has 1 at place 2 and 0 at place 5; 3. `1->3` has 1 at place 2 and 3 at place 6; 4. `1->4` has 1 at place 2 and 4 at place 4; 5. `1->5` has 1 at place 2 and 5 at place 3; 6. `2->1` has 2 at place 1 and 1 at place 2; 7. `2->4` has 2 at place 1 and 4 at place 4. Every tail is left of its head. The postorder itself, `3, 0, 4, 5, 1, 2`, fails on `0->3`. Source: `erickson-dfs#p8`.

## 6. seed 4540223754209578338, level 1

A directed graph on vertices 0 to 4 has edges `0->3`, `1->2`, `1->3`, `1->4`, `2->3`, `2->4`, `3->4`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `4, 3, 0, 2, 1`
b) `2, 0, 3, 4, 1`
c) `1, 2, 0, 3, 4`
d) `1, 2, 3, 0, 4`

**Key: c**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `1, 2, 0, 3, 4`. Checking each edge: 1. `0->3` has 0 at place 3 and 3 at place 4; 2. `1->2` has 1 at place 1 and 2 at place 2; 3. `1->3` has 1 at place 1 and 3 at place 4; 4. `1->4` has 1 at place 1 and 4 at place 5; 5. `2->3` has 2 at place 2 and 3 at place 4; 6. `2->4` has 2 at place 2 and 4 at place 5; 7. `3->4` has 3 at place 4 and 4 at place 5. Every tail is left of its head. The postorder itself, `4, 3, 0, 2, 1`, fails on `0->3`. Source: `erickson-dfs#p8`.

## 7. seed 2128103712836318309, level 1

A directed graph on vertices 0 to 4 has edges `1->0`, `3->0`, `3->2`, `4->0`, `4->2`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `0, 1, 2, 3, 4`
b) `3, 2, 1, 0, 4`
c) `4, 3, 2, 0, 1`
d) `4, 3, 2, 1, 0`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `4, 3, 2, 1, 0`. Checking each edge: 1. `1->0` has 1 at place 4 and 0 at place 5; 2. `3->0` has 3 at place 2 and 0 at place 5; 3. `3->2` has 3 at place 2 and 2 at place 3; 4. `4->0` has 4 at place 1 and 0 at place 5; 5. `4->2` has 4 at place 1 and 2 at place 3. Every tail is left of its head. The postorder itself, `0, 1, 2, 3, 4`, fails on `1->0`. Source: `erickson-dfs#p8`.

## 8. seed 3708783956114574160, level 2

A directed graph on vertices 0 to 5 has edges `2->1`, `3->1`, `3->2`, `5->0`, `5->1`, `5->2`, `5->3`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `4, 3, 2, 1, 0, 5`
b) `5, 4, 3, 1, 2, 0`
c) `0, 1, 2, 3, 4, 5`
d) `5, 4, 3, 2, 1, 0`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `5, 4, 3, 2, 1, 0`. Checking each edge: 1. `2->1` has 2 at place 4 and 1 at place 5; 2. `3->1` has 3 at place 3 and 1 at place 5; 3. `3->2` has 3 at place 3 and 2 at place 4; 4. `5->0` has 5 at place 1 and 0 at place 6; 5. `5->1` has 5 at place 1 and 1 at place 5; 6. `5->2` has 5 at place 1 and 2 at place 4; 7. `5->3` has 5 at place 1 and 3 at place 3. Every tail is left of its head. The postorder itself, `0, 1, 2, 3, 4, 5`, fails on `2->1`. Source: `erickson-dfs#p8`.

## 9. seed 218307583450387548, level 1

A directed graph on vertices 0 to 4 has edges `0->2`, `0->4`, `1->2`, `2->4`, `3->1`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `3, 1, 2, 0, 4`
b) `3, 1, 0, 2, 4`
c) `0, 1, 2, 3, 4`
d) `1, 0, 2, 4, 3`

**Key: b**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `3, 1, 0, 2, 4`. Checking each edge: 1. `0->2` has 0 at place 3 and 2 at place 4; 2. `0->4` has 0 at place 3 and 4 at place 5; 3. `1->2` has 1 at place 2 and 2 at place 4; 4. `2->4` has 2 at place 4 and 4 at place 5; 5. `3->1` has 3 at place 1 and 1 at place 2. Every tail is left of its head. The postorder itself, `4, 2, 0, 1, 3`, fails on `0->2`. Source: `erickson-dfs#p8`.

## 10. seed 11585634603700827, level 2

A directed graph on vertices 0 to 5 has edges `0->5`, `1->2`, `1->5`, `2->3`, `3->0`, `3->5`, `4->5`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `4, 1, 2, 3, 5, 0`
b) `4, 1, 2, 3, 0, 5`
c) `1, 2, 3, 0, 5, 4`
d) `5, 0, 3, 2, 1, 4`

**Key: b**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `4, 1, 2, 3, 0, 5`. Checking each edge: 1. `0->5` has 0 at place 5 and 5 at place 6; 2. `1->2` has 1 at place 2 and 2 at place 3; 3. `1->5` has 1 at place 2 and 5 at place 6; 4. `2->3` has 2 at place 3 and 3 at place 4; 5. `3->0` has 3 at place 4 and 0 at place 5; 6. `3->5` has 3 at place 4 and 5 at place 6; 7. `4->5` has 4 at place 1 and 5 at place 6. Every tail is left of its head. The postorder itself, `5, 0, 3, 2, 1, 4`, fails on `0->5`. Source: `erickson-dfs#p8`.

## 11. seed 4312151220533055886, level 1

A directed graph on vertices 0 to 4 has edges `1->2`, `1->3`, `2->3`, `3->0`, `4->2`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `1, 2, 3, 0, 4`
b) `1, 2, 3, 4, 0`
c) `0, 1, 2, 3, 4`
d) `4, 1, 2, 3, 0`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `4, 1, 2, 3, 0`. Checking each edge: 1. `1->2` has 1 at place 2 and 2 at place 3; 2. `1->3` has 1 at place 2 and 3 at place 4; 3. `2->3` has 2 at place 3 and 3 at place 4; 4. `3->0` has 3 at place 4 and 0 at place 5; 5. `4->2` has 4 at place 1 and 2 at place 3. Every tail is left of its head. The postorder itself, `0, 3, 2, 1, 4`, fails on `1->2`. Source: `erickson-dfs#p8`.

## 12. seed 4132562426769525755, level 2

A directed graph on vertices 0 to 5 has edges `0->1`, `0->3`, `1->5`, `2->5`, `3->4`, `3->5`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `2, 1, 3, 4, 0, 5`
b) `2, 0, 3, 4, 1, 5`
c) `5, 1, 4, 3, 0, 2`
d) `0, 3, 4, 1, 5, 2`

**Key: b**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `2, 0, 3, 4, 1, 5`. Checking each edge: 1. `0->1` has 0 at place 2 and 1 at place 5; 2. `0->3` has 0 at place 2 and 3 at place 3; 3. `1->5` has 1 at place 5 and 5 at place 6; 4. `2->5` has 2 at place 1 and 5 at place 6; 5. `3->4` has 3 at place 3 and 4 at place 4; 6. `3->5` has 3 at place 3 and 5 at place 6. Every tail is left of its head. The postorder itself, `5, 1, 4, 3, 0, 2`, fails on `0->1`. Source: `erickson-dfs#p8`.

## 13. seed 3911955523238897958, level 2

A directed graph on vertices 0 to 5 has edges `0->1`, `0->3`, `1->3`, `3->2`, `4->2`, `4->3`, `5->1`, `5->2`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `4, 0, 1, 3, 2, 5`
b) `5, 4, 1, 0, 3, 2`
c) `2, 3, 1, 0, 4, 5`
d) `5, 4, 0, 1, 3, 2`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `5, 4, 0, 1, 3, 2`. Checking each edge: 1. `0->1` has 0 at place 3 and 1 at place 4; 2. `0->3` has 0 at place 3 and 3 at place 5; 3. `1->3` has 1 at place 4 and 3 at place 5; 4. `3->2` has 3 at place 5 and 2 at place 6; 5. `4->2` has 4 at place 2 and 2 at place 6; 6. `4->3` has 4 at place 2 and 3 at place 5; 7. `5->1` has 5 at place 1 and 1 at place 4; 8. `5->2` has 5 at place 1 and 2 at place 6. Every tail is left of its head. The postorder itself, `2, 3, 1, 0, 4, 5`, fails on `0->1`. Source: `erickson-dfs#p8`.

## 14. seed 3186177591359639783, level 2

A directed graph on vertices 0 to 5 has edges `0->2`, `0->3`, `1->2`, `1->3`, `1->5`, `2->5`, `3->2`, `3->5`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `0, 1, 2, 3, 4, 5`
b) `4, 1, 0, 3, 2, 5`
c) `4, 1, 2, 3, 0, 5`
d) `5, 2, 3, 0, 1, 4`

**Key: b**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `4, 1, 0, 3, 2, 5`. Checking each edge: 1. `0->2` has 0 at place 3 and 2 at place 5; 2. `0->3` has 0 at place 3 and 3 at place 4; 3. `1->2` has 1 at place 2 and 2 at place 5; 4. `1->3` has 1 at place 2 and 3 at place 4; 5. `1->5` has 1 at place 2 and 5 at place 6; 6. `2->5` has 2 at place 5 and 5 at place 6; 7. `3->2` has 3 at place 4 and 2 at place 5; 8. `3->5` has 3 at place 4 and 5 at place 6. Every tail is left of its head. The postorder itself, `5, 2, 3, 0, 1, 4`, fails on `0->2`. Source: `erickson-dfs#p8`.

## 15. seed 231838992183745921, level 1

A directed graph on vertices 0 to 4 has edges `0->1`, `0->2`, `0->4`, `1->4`, `3->0`, `3->1`, `3->2`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `3, 1, 2, 0, 4`
b) `4, 1, 2, 0, 3`
c) `0, 3, 1, 2, 4`
d) `3, 0, 2, 1, 4`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `3, 0, 2, 1, 4`. Checking each edge: 1. `0->1` has 0 at place 2 and 1 at place 4; 2. `0->2` has 0 at place 2 and 2 at place 3; 3. `0->4` has 0 at place 2 and 4 at place 5; 4. `1->4` has 1 at place 4 and 4 at place 5; 5. `3->0` has 3 at place 1 and 0 at place 2; 6. `3->1` has 3 at place 1 and 1 at place 4; 7. `3->2` has 3 at place 1 and 2 at place 3. Every tail is left of its head. The postorder itself, `4, 1, 2, 0, 3`, fails on `0->1`. Source: `erickson-dfs#p8`.

## 16. seed 3642900565420157897, level 1

A directed graph on vertices 0 to 4 has edges `0->1`, `0->2`, `0->4`, `1->4`, `3->2`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `0, 2, 1, 4, 3`
b) `3, 0, 2, 1, 4`
c) `4, 1, 2, 0, 3`
d) `0, 1, 2, 3, 4`

**Key: b**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `3, 0, 2, 1, 4`. Checking each edge: 1. `0->1` has 0 at place 2 and 1 at place 4; 2. `0->2` has 0 at place 2 and 2 at place 3; 3. `0->4` has 0 at place 2 and 4 at place 5; 4. `1->4` has 1 at place 4 and 4 at place 5; 5. `3->2` has 3 at place 1 and 2 at place 3. Every tail is left of its head. The postorder itself, `4, 1, 2, 0, 3`, fails on `0->1`. Source: `erickson-dfs#p8`.

## 17. seed 3928931275442881470, level 1

A directed graph on vertices 0 to 4 has edges `0->1`, `0->2`, `0->3`, `2->1`, `4->3`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `0, 1, 2, 3, 4`
b) `1, 2, 3, 0, 4`
c) `4, 0, 3, 2, 1`
d) `0, 3, 2, 1, 4`

**Key: c**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `4, 0, 3, 2, 1`. Checking each edge: 1. `0->1` has 0 at place 2 and 1 at place 5; 2. `0->2` has 0 at place 2 and 2 at place 4; 3. `0->3` has 0 at place 2 and 3 at place 3; 4. `2->1` has 2 at place 4 and 1 at place 5; 5. `4->3` has 4 at place 1 and 3 at place 3. Every tail is left of its head. The postorder itself, `1, 2, 3, 0, 4`, fails on `0->1`. Source: `erickson-dfs#p8`.

## 18. seed 2055510156031616866, level 2

A directed graph on vertices 0 to 5 has edges `2->1`, `2->3`, `4->1`, `4->2`, `5->0`, `5->1`, `5->2`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `0, 1, 3, 2, 4, 5`
b) `4, 2, 3, 1, 0, 5`
c) `5, 4, 2, 3, 1, 0`
d) `0, 1, 2, 3, 4, 5`

**Key: c**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `5, 4, 2, 3, 1, 0`. Checking each edge: 1. `2->1` has 2 at place 3 and 1 at place 5; 2. `2->3` has 2 at place 3 and 3 at place 4; 3. `4->1` has 4 at place 2 and 1 at place 5; 4. `4->2` has 4 at place 2 and 2 at place 3; 5. `5->0` has 5 at place 1 and 0 at place 6; 6. `5->1` has 5 at place 1 and 1 at place 5; 7. `5->2` has 5 at place 1 and 2 at place 3. Every tail is left of its head. The postorder itself, `0, 1, 3, 2, 4, 5`, fails on `2->1`. Source: `erickson-dfs#p8`.

## 19. seed 3444653010545353209, level 1

A directed graph on vertices 0 to 4 has edges `0->2`, `1->0`, `1->2`, `1->4`, `3->2`, `4->2`, `4->3`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `2, 0, 3, 4, 1`
b) `0, 1, 2, 3, 4`
c) `1, 4, 3, 2, 0`
d) `1, 4, 3, 0, 2`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `1, 4, 3, 0, 2`. Checking each edge: 1. `0->2` has 0 at place 4 and 2 at place 5; 2. `1->0` has 1 at place 1 and 0 at place 4; 3. `1->2` has 1 at place 1 and 2 at place 5; 4. `1->4` has 1 at place 1 and 4 at place 2; 5. `3->2` has 3 at place 3 and 2 at place 5; 6. `4->2` has 4 at place 2 and 2 at place 5; 7. `4->3` has 4 at place 2 and 3 at place 3. Every tail is left of its head. The postorder itself, `2, 0, 3, 4, 1`, fails on `0->2`. Source: `erickson-dfs#p8`.

## 20. seed 4442513298597063087, level 1

A directed graph on vertices 0 to 4 has edges `0->2`, `1->0`, `1->3`, `3->0`, `3->2`, `4->0`, `4->2`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `0, 1, 2, 3, 4`
b) `4, 1, 3, 0, 2`
c) `4, 1, 3, 2, 0`
d) `1, 3, 0, 2, 4`

**Key: b**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `4, 1, 3, 0, 2`. Checking each edge: 1. `0->2` has 0 at place 4 and 2 at place 5; 2. `1->0` has 1 at place 2 and 0 at place 4; 3. `1->3` has 1 at place 2 and 3 at place 3; 4. `3->0` has 3 at place 3 and 0 at place 4; 5. `3->2` has 3 at place 3 and 2 at place 5; 6. `4->0` has 4 at place 1 and 0 at place 4; 7. `4->2` has 4 at place 1 and 2 at place 5. Every tail is left of its head. The postorder itself, `2, 0, 3, 1, 4`, fails on `0->2`. Source: `erickson-dfs#p8`.

## 21. seed 2081484150180864230, level 2

A directed graph on vertices 0 to 5 has edges `0->1`, `0->4`, `1->2`, `1->3`, `4->1`, `4->2`, `5->4`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `2, 3, 1, 4, 0, 5`
b) `5, 1, 4, 0, 3, 2`
c) `5, 0, 4, 1, 3, 2`
d) `0, 1, 2, 3, 4, 5`

**Key: c**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `5, 0, 4, 1, 3, 2`. Checking each edge: 1. `0->1` has 0 at place 2 and 1 at place 4; 2. `0->4` has 0 at place 2 and 4 at place 3; 3. `1->2` has 1 at place 4 and 2 at place 6; 4. `1->3` has 1 at place 4 and 3 at place 5; 5. `4->1` has 4 at place 3 and 1 at place 4; 6. `4->2` has 4 at place 3 and 2 at place 6; 7. `5->4` has 5 at place 1 and 4 at place 3. Every tail is left of its head. The postorder itself, `2, 3, 1, 4, 0, 5`, fails on `0->1`. Source: `erickson-dfs#p8`.

## 22. seed 2246532140299588560, level 2

A directed graph on vertices 0 to 5 has edges `0->2`, `1->3`, `2->1`, `2->3`, `5->1`, `5->4`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `2, 5, 0, 1, 3, 4`
b) `0, 1, 2, 3, 4, 5`
c) `3, 1, 2, 0, 4, 5`
d) `5, 4, 0, 2, 1, 3`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `5, 4, 0, 2, 1, 3`. Checking each edge: 1. `0->2` has 0 at place 3 and 2 at place 4; 2. `1->3` has 1 at place 5 and 3 at place 6; 3. `2->1` has 2 at place 4 and 1 at place 5; 4. `2->3` has 2 at place 4 and 3 at place 6; 5. `5->1` has 5 at place 1 and 1 at place 5; 6. `5->4` has 5 at place 1 and 4 at place 2. Every tail is left of its head. The postorder itself, `3, 1, 2, 0, 4, 5`, fails on `0->2`. Source: `erickson-dfs#p8`.

## 23. seed 3063612750103595530, level 1

A directed graph on vertices 0 to 4 has edges `0->3`, `1->3`, `2->1`, `4->0`, `4->1`, `4->3`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `2, 1, 0, 3, 4`
b) `4, 2, 1, 0, 3`
c) `4, 0, 1, 2, 3`
d) `0, 1, 2, 3, 4`

**Key: b**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `4, 2, 1, 0, 3`. Checking each edge: 1. `0->3` has 0 at place 4 and 3 at place 5; 2. `1->3` has 1 at place 3 and 3 at place 5; 3. `2->1` has 2 at place 2 and 1 at place 3; 4. `4->0` has 4 at place 1 and 0 at place 4; 5. `4->1` has 4 at place 1 and 1 at place 3; 6. `4->3` has 4 at place 1 and 3 at place 5. Every tail is left of its head. The postorder itself, `3, 0, 1, 2, 4`, fails on `0->3`. Source: `erickson-dfs#p8`.

## 24. seed 4080818652619242917, level 2

A directed graph on vertices 0 to 5 has edges `1->0`, `1->5`, `2->1`, `2->5`, `3->1`, `3->4`, `3->5`, `4->5`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `0, 1, 2, 3, 4, 5`
b) `3, 4, 2, 1, 5, 0`
c) `3, 4, 2, 0, 5, 1`
d) `3, 1, 2, 4, 0, 5`

**Key: b**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `3, 4, 2, 1, 5, 0`. Checking each edge: 1. `1->0` has 1 at place 4 and 0 at place 6; 2. `1->5` has 1 at place 4 and 5 at place 5; 3. `2->1` has 2 at place 3 and 1 at place 4; 4. `2->5` has 2 at place 3 and 5 at place 5; 5. `3->1` has 3 at place 1 and 1 at place 4; 6. `3->4` has 3 at place 1 and 4 at place 2; 7. `3->5` has 3 at place 1 and 5 at place 5; 8. `4->5` has 4 at place 2 and 5 at place 5. Every tail is left of its head. The postorder itself, `0, 5, 1, 2, 4, 3`, fails on `1->0`. Source: `erickson-dfs#p8`.

## 25. seed 3501137521639015273, level 1

A directed graph on vertices 0 to 4 has edges `0->2`, `1->0`, `1->2`, `3->0`, `3->1`, `3->2`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `0, 1, 2, 3, 4`
b) `2, 0, 1, 3, 4`
c) `4, 3, 1, 0, 2`
d) `4, 3, 1, 2, 0`

**Key: c**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `4, 3, 1, 0, 2`. Checking each edge: 1. `0->2` has 0 at place 4 and 2 at place 5; 2. `1->0` has 1 at place 3 and 0 at place 4; 3. `1->2` has 1 at place 3 and 2 at place 5; 4. `3->0` has 3 at place 2 and 0 at place 4; 5. `3->1` has 3 at place 2 and 1 at place 3; 6. `3->2` has 3 at place 2 and 2 at place 5. Every tail is left of its head. The postorder itself, `2, 0, 1, 3, 4`, fails on `0->2`. Source: `erickson-dfs#p8`.

## 26. seed 1425614490803405939, level 1

A directed graph on vertices 0 to 4 has edges `0->2`, `0->3`, `1->0`, `1->4`, `4->3`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `0, 1, 2, 3, 4`
b) `2, 3, 0, 4, 1`
c) `0, 1, 4, 2, 3`
d) `1, 4, 0, 3, 2`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `1, 4, 0, 3, 2`. Checking each edge: 1. `0->2` has 0 at place 3 and 2 at place 5; 2. `0->3` has 0 at place 3 and 3 at place 4; 3. `1->0` has 1 at place 1 and 0 at place 3; 4. `1->4` has 1 at place 1 and 4 at place 2; 5. `4->3` has 4 at place 2 and 3 at place 4. Every tail is left of its head. The postorder itself, `2, 3, 0, 4, 1`, fails on `0->2`. Source: `erickson-dfs#p8`.

## 27. seed 272929942937668509, level 2

A directed graph on vertices 0 to 5 has edges `1->0`, `2->0`, `2->3`, `2->5`, `3->0`, `3->5`, `4->0`, `4->3`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `4, 2, 3, 5, 1, 0`
b) `2, 3, 5, 1, 0, 4`
c) `2, 3, 4, 1, 0, 5`
d) `4, 2, 3, 5, 0, 1`

**Key: a**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `4, 2, 3, 5, 1, 0`. Checking each edge: 1. `1->0` has 1 at place 5 and 0 at place 6; 2. `2->0` has 2 at place 2 and 0 at place 6; 3. `2->3` has 2 at place 2 and 3 at place 3; 4. `2->5` has 2 at place 2 and 5 at place 4; 5. `3->0` has 3 at place 3 and 0 at place 6; 6. `3->5` has 3 at place 3 and 5 at place 4; 7. `4->0` has 4 at place 1 and 0 at place 6; 8. `4->3` has 4 at place 1 and 3 at place 3. Every tail is left of its head. The postorder itself, `0, 1, 5, 3, 2, 4`, fails on `1->0`. Source: `erickson-dfs#p8`.

## 28. seed 2545469148772738511, level 2

A directed graph on vertices 0 to 5 has edges `0->1`, `2->4`, `3->0`, `3->4`, `4->0`, `5->0`, `5->1`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `0, 1, 2, 3, 4, 5`
b) `3, 2, 4, 0, 1, 5`
c) `3, 5, 0, 2, 4, 1`
d) `5, 3, 2, 4, 0, 1`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `5, 3, 2, 4, 0, 1`. Checking each edge: 1. `0->1` has 0 at place 5 and 1 at place 6; 2. `2->4` has 2 at place 3 and 4 at place 4; 3. `3->0` has 3 at place 2 and 0 at place 5; 4. `3->4` has 3 at place 2 and 4 at place 4; 5. `4->0` has 4 at place 4 and 0 at place 5; 6. `5->0` has 5 at place 1 and 0 at place 5; 7. `5->1` has 5 at place 1 and 1 at place 6. Every tail is left of its head. The postorder itself, `1, 0, 4, 2, 3, 5`, fails on `0->1`. Source: `erickson-dfs#p8`.

## 29. seed 2448201843099971683, level 1

A directed graph on vertices 0 to 4 has edges `1->3`, `1->4`, `2->0`, `2->1`, `2->3`, `3->0`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `0, 1, 2, 3, 4`
b) `2, 1, 4, 3, 0`
c) `0, 3, 4, 1, 2`
d) `2, 3, 4, 1, 0`

**Key: b**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `2, 1, 4, 3, 0`. Checking each edge: 1. `1->3` has 1 at place 2 and 3 at place 4; 2. `1->4` has 1 at place 2 and 4 at place 3; 3. `2->0` has 2 at place 1 and 0 at place 5; 4. `2->1` has 2 at place 1 and 1 at place 2; 5. `2->3` has 2 at place 1 and 3 at place 4; 6. `3->0` has 3 at place 4 and 0 at place 5. Every tail is left of its head. The postorder itself, `0, 3, 4, 1, 2`, fails on `1->3`. Source: `erickson-dfs#p8`.

## 30. seed 10059000122963657, level 1

A directed graph on vertices 0 to 4 has edges `0->2`, `0->4`, `2->1`, `2->4`, `3->1`, `4->3`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `0, 1, 2, 3, 4`
b) `2, 0, 4, 3, 1`
c) `0, 2, 4, 3, 1`
d) `1, 3, 4, 2, 0`

**Key: c**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `0, 2, 4, 3, 1`. Checking each edge: 1. `0->2` has 0 at place 1 and 2 at place 2; 2. `0->4` has 0 at place 1 and 4 at place 3; 3. `2->1` has 2 at place 2 and 1 at place 5; 4. `2->4` has 2 at place 2 and 4 at place 3; 5. `3->1` has 3 at place 4 and 1 at place 5; 6. `4->3` has 4 at place 3 and 3 at place 4. Every tail is left of its head. The postorder itself, `1, 3, 4, 2, 0`, fails on `0->2`. Source: `erickson-dfs#p8`.

## 31. seed 2395060359064490757, level 1

A directed graph on vertices 0 to 4 has edges `0->1`, `0->3`, `3->1`, `4->0`, `4->1`, `4->3`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `0, 1, 2, 3, 4`
b) `2, 0, 3, 1, 4`
c) `1, 3, 0, 2, 4`
d) `4, 2, 0, 3, 1`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `4, 2, 0, 3, 1`. Checking each edge: 1. `0->1` has 0 at place 3 and 1 at place 5; 2. `0->3` has 0 at place 3 and 3 at place 4; 3. `3->1` has 3 at place 4 and 1 at place 5; 4. `4->0` has 4 at place 1 and 0 at place 3; 5. `4->1` has 4 at place 1 and 1 at place 5; 6. `4->3` has 4 at place 1 and 3 at place 4. Every tail is left of its head. The postorder itself, `1, 3, 0, 2, 4`, fails on `0->1`. Source: `erickson-dfs#p8`.

## 32. seed 1870676845012716630, level 1

A directed graph on vertices 0 to 4 has edges `0->4`, `1->4`, `2->0`, `2->3`, `2->4`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `2, 3, 1, 0, 4`
b) `2, 3, 1, 4, 0`
c) `4, 0, 1, 3, 2`
d) `3, 1, 0, 4, 2`

**Key: a**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `2, 3, 1, 0, 4`. Checking each edge: 1. `0->4` has 0 at place 4 and 4 at place 5; 2. `1->4` has 1 at place 3 and 4 at place 5; 3. `2->0` has 2 at place 1 and 0 at place 4; 4. `2->3` has 2 at place 1 and 3 at place 2; 5. `2->4` has 2 at place 1 and 4 at place 5. Every tail is left of its head. The postorder itself, `4, 0, 1, 3, 2`, fails on `0->4`. Source: `erickson-dfs#p8`.

## 33. seed 1214192301619874611, level 1

A directed graph on vertices 0 to 4 has edges `1->0`, `2->0`, `2->1`, `2->3`, `2->4`, `3->0`, `4->3`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `4, 3, 1, 0, 2`
b) `0, 1, 2, 3, 4`
c) `2, 4, 3, 1, 0`
d) `2, 1, 3, 4, 0`

**Key: c**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `2, 4, 3, 1, 0`. Checking each edge: 1. `1->0` has 1 at place 4 and 0 at place 5; 2. `2->0` has 2 at place 1 and 0 at place 5; 3. `2->1` has 2 at place 1 and 1 at place 4; 4. `2->3` has 2 at place 1 and 3 at place 3; 5. `2->4` has 2 at place 1 and 4 at place 2; 6. `3->0` has 3 at place 3 and 0 at place 5; 7. `4->3` has 4 at place 2 and 3 at place 3. Every tail is left of its head. The postorder itself, `0, 1, 3, 4, 2`, fails on `1->0`. Source: `erickson-dfs#p8`.

## 34. seed 1693902510128355144, level 1

A directed graph on vertices 0 to 4 has edges `1->0`, `1->4`, `2->0`, `3->0`, `3->2`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `3, 2, 1, 4, 0`
b) `2, 1, 4, 0, 3`
c) `0, 1, 2, 3, 4`
d) `0, 4, 1, 2, 3`

**Key: a**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `3, 2, 1, 4, 0`. Checking each edge: 1. `1->0` has 1 at place 3 and 0 at place 5; 2. `1->4` has 1 at place 3 and 4 at place 4; 3. `2->0` has 2 at place 2 and 0 at place 5; 4. `3->0` has 3 at place 1 and 0 at place 5; 5. `3->2` has 3 at place 1 and 2 at place 2. Every tail is left of its head. The postorder itself, `0, 4, 1, 2, 3`, fails on `1->0`. Source: `erickson-dfs#p8`.

## 35. seed 1544189727325086524, level 1

A directed graph on vertices 0 to 4 has edges `1->0`, `1->3`, `2->0`, `2->1`, `2->3`, `3->0`, `4->1`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `4, 2, 0, 3, 1`
b) `4, 2, 1, 3, 0`
c) `2, 1, 3, 4, 0`
d) `2, 1, 3, 0, 4`

**Key: b**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `4, 2, 1, 3, 0`. Checking each edge: 1. `1->0` has 1 at place 3 and 0 at place 5; 2. `1->3` has 1 at place 3 and 3 at place 4; 3. `2->0` has 2 at place 2 and 0 at place 5; 4. `2->1` has 2 at place 2 and 1 at place 3; 5. `2->3` has 2 at place 2 and 3 at place 4; 6. `3->0` has 3 at place 4 and 0 at place 5; 7. `4->1` has 4 at place 1 and 1 at place 3. Every tail is left of its head. The postorder itself, `0, 3, 1, 2, 4`, fails on `1->0`. Source: `erickson-dfs#p8`.

## 36. seed 3441914404628960673, level 2

A directed graph on vertices 0 to 5 has edges `1->2`, `1->4`, `2->4`, `2->5`, `3->2`, `3->5`, `5->4`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `0, 1, 2, 3, 4, 5`
b) `3, 2, 1, 5, 4, 0`
c) `1, 2, 5, 4, 0, 3`
d) `3, 1, 2, 5, 4, 0`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `3, 1, 2, 5, 4, 0`. Checking each edge: 1. `1->2` has 1 at place 2 and 2 at place 3; 2. `1->4` has 1 at place 2 and 4 at place 5; 3. `2->4` has 2 at place 3 and 4 at place 5; 4. `2->5` has 2 at place 3 and 5 at place 4; 5. `3->2` has 3 at place 1 and 2 at place 3; 6. `3->5` has 3 at place 1 and 5 at place 4; 7. `5->4` has 5 at place 4 and 4 at place 5. Every tail is left of its head. The postorder itself, `0, 4, 5, 2, 1, 3`, fails on `1->2`. Source: `erickson-dfs#p8`.

## 37. seed 2070789101714092418, level 1

A directed graph on vertices 0 to 4 has edges `0->3`, `1->3`, `4->0`, `4->1`, `4->2`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `3, 0, 1, 2, 4`
b) `2, 1, 0, 3, 4`
c) `0, 1, 2, 3, 4`
d) `4, 2, 1, 0, 3`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `4, 2, 1, 0, 3`. Checking each edge: 1. `0->3` has 0 at place 4 and 3 at place 5; 2. `1->3` has 1 at place 3 and 3 at place 5; 3. `4->0` has 4 at place 1 and 0 at place 4; 4. `4->1` has 4 at place 1 and 1 at place 3; 5. `4->2` has 4 at place 1 and 2 at place 2. Every tail is left of its head. The postorder itself, `3, 0, 1, 2, 4`, fails on `0->3`. Source: `erickson-dfs#p8`.

## 38. seed 4050897886115792593, level 1

A directed graph on vertices 0 to 4 has edges `0->1`, `0->2`, `0->3`, `2->1`, `2->3`, `2->4`, `3->1`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `0, 1, 2, 3, 4`
b) `1, 3, 4, 2, 0`
c) `2, 4, 3, 1, 0`
d) `0, 2, 4, 3, 1`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `0, 2, 4, 3, 1`. Checking each edge: 1. `0->1` has 0 at place 1 and 1 at place 5; 2. `0->2` has 0 at place 1 and 2 at place 2; 3. `0->3` has 0 at place 1 and 3 at place 4; 4. `2->1` has 2 at place 2 and 1 at place 5; 5. `2->3` has 2 at place 2 and 3 at place 4; 6. `2->4` has 2 at place 2 and 4 at place 3; 7. `3->1` has 3 at place 4 and 1 at place 5. Every tail is left of its head. The postorder itself, `1, 3, 4, 2, 0`, fails on `0->1`. Source: `erickson-dfs#p8`.

## 39. seed 2044487946034344461, level 1

A directed graph on vertices 0 to 4 has edges `1->0`, `1->2`, `1->4`, `2->0`, `3->0`, `3->2`, `3->4`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `3, 0, 4, 2, 1`
b) `0, 2, 4, 1, 3`
c) `1, 4, 2, 0, 3`
d) `3, 1, 4, 2, 0`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `3, 1, 4, 2, 0`. Checking each edge: 1. `1->0` has 1 at place 2 and 0 at place 5; 2. `1->2` has 1 at place 2 and 2 at place 4; 3. `1->4` has 1 at place 2 and 4 at place 3; 4. `2->0` has 2 at place 4 and 0 at place 5; 5. `3->0` has 3 at place 1 and 0 at place 5; 6. `3->2` has 3 at place 1 and 2 at place 4; 7. `3->4` has 3 at place 1 and 4 at place 3. Every tail is left of its head. The postorder itself, `0, 2, 4, 1, 3`, fails on `1->0`. Source: `erickson-dfs#p8`.

## 40. seed 3125763939495761345, level 2

A directed graph on vertices 0 to 5 has edges `0->2`, `3->1`, `3->5`, `4->0`, `4->1`, `4->2`, `5->1`, `5->2`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `3, 5, 1, 0, 2, 4`
b) `4, 3, 5, 1, 2, 0`
c) `2, 0, 1, 5, 3, 4`
d) `4, 3, 5, 1, 0, 2`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `4, 3, 5, 1, 0, 2`. Checking each edge: 1. `0->2` has 0 at place 5 and 2 at place 6; 2. `3->1` has 3 at place 2 and 1 at place 4; 3. `3->5` has 3 at place 2 and 5 at place 3; 4. `4->0` has 4 at place 1 and 0 at place 5; 5. `4->1` has 4 at place 1 and 1 at place 4; 6. `4->2` has 4 at place 1 and 2 at place 6; 7. `5->1` has 5 at place 3 and 1 at place 4; 8. `5->2` has 5 at place 3 and 2 at place 6. Every tail is left of its head. The postorder itself, `2, 0, 1, 5, 3, 4`, fails on `0->2`. Source: `erickson-dfs#p8`.

## 41. seed 2471398266392353516, level 1

A directed graph on vertices 0 to 4 has edges `1->0`, `1->3`, `1->4`, `3->2`, `4->3`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `0, 4, 3, 2, 1`
b) `1, 4, 3, 2, 0`
c) `0, 1, 2, 3, 4`
d) `0, 2, 3, 4, 1`

**Key: b**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `1, 4, 3, 2, 0`. Checking each edge: 1. `1->0` has 1 at place 1 and 0 at place 5; 2. `1->3` has 1 at place 1 and 3 at place 3; 3. `1->4` has 1 at place 1 and 4 at place 2; 4. `3->2` has 3 at place 3 and 2 at place 4; 5. `4->3` has 4 at place 2 and 3 at place 3. Every tail is left of its head. The postorder itself, `0, 2, 3, 4, 1`, fails on `1->0`. Source: `erickson-dfs#p8`.

## 42. seed 1910833661547540589, level 2

A directed graph on vertices 0 to 5 has edges `1->2`, `1->4`, `3->4`, `4->0`, `4->2`, `5->0`, `5->2`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `1, 4, 5, 3, 0, 2`
b) `0, 2, 4, 1, 3, 5`
c) `3, 1, 4, 2, 0, 5`
d) `5, 3, 1, 4, 2, 0`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `5, 3, 1, 4, 2, 0`. Checking each edge: 1. `1->2` has 1 at place 3 and 2 at place 5; 2. `1->4` has 1 at place 3 and 4 at place 4; 3. `3->4` has 3 at place 2 and 4 at place 4; 4. `4->0` has 4 at place 4 and 0 at place 6; 5. `4->2` has 4 at place 4 and 2 at place 5; 6. `5->0` has 5 at place 1 and 0 at place 6; 7. `5->2` has 5 at place 1 and 2 at place 5. Every tail is left of its head. The postorder itself, `0, 2, 4, 1, 3, 5`, fails on `1->2`. Source: `erickson-dfs#p8`.

## 43. seed 2020494110167606670, level 1

A directed graph on vertices 0 to 4 has edges `2->0`, `3->0`, `3->1`, `3->2`, `3->4`, `4->0`, `4->1`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `0, 1, 2, 4, 3`
b) `0, 1, 2, 3, 4`
c) `4, 2, 1, 0, 3`
d) `3, 4, 2, 1, 0`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `3, 4, 2, 1, 0`. Checking each edge: 1. `2->0` has 2 at place 3 and 0 at place 5; 2. `3->0` has 3 at place 1 and 0 at place 5; 3. `3->1` has 3 at place 1 and 1 at place 4; 4. `3->2` has 3 at place 1 and 2 at place 3; 5. `3->4` has 3 at place 1 and 4 at place 2; 6. `4->0` has 4 at place 2 and 0 at place 5; 7. `4->1` has 4 at place 2 and 1 at place 4. Every tail is left of its head. The postorder itself, `0, 1, 2, 4, 3`, fails on `2->0`. Source: `erickson-dfs#p8`.

## 44. seed 3732853832825343163, level 1

A directed graph on vertices 0 to 4 has edges `1->0`, `1->2`, `1->4`, `2->0`, `3->0`, `3->1`, `4->0`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `1, 3, 2, 4, 0`
b) `0, 1, 2, 3, 4`
c) `0, 2, 4, 1, 3`
d) `3, 1, 4, 2, 0`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `3, 1, 4, 2, 0`. Checking each edge: 1. `1->0` has 1 at place 2 and 0 at place 5; 2. `1->2` has 1 at place 2 and 2 at place 4; 3. `1->4` has 1 at place 2 and 4 at place 3; 4. `2->0` has 2 at place 4 and 0 at place 5; 5. `3->0` has 3 at place 1 and 0 at place 5; 6. `3->1` has 3 at place 1 and 1 at place 2; 7. `4->0` has 4 at place 3 and 0 at place 5. Every tail is left of its head. The postorder itself, `0, 2, 4, 1, 3`, fails on `1->0`. Source: `erickson-dfs#p8`.

## 45. seed 1310667686404625494, level 1

A directed graph on vertices 0 to 4 has edges `0->2`, `2->1`, `3->1`, `3->2`, `3->4`, `4->1`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `3, 4, 0, 2, 1`
b) `4, 0, 2, 1, 3`
c) `0, 1, 2, 3, 4`
d) `3, 4, 2, 0, 1`

**Key: a**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `3, 4, 0, 2, 1`. Checking each edge: 1. `0->2` has 0 at place 3 and 2 at place 4; 2. `2->1` has 2 at place 4 and 1 at place 5; 3. `3->1` has 3 at place 1 and 1 at place 5; 4. `3->2` has 3 at place 1 and 2 at place 4; 5. `3->4` has 3 at place 1 and 4 at place 2; 6. `4->1` has 4 at place 2 and 1 at place 5. Every tail is left of its head. The postorder itself, `1, 2, 0, 4, 3`, fails on `0->2`. Source: `erickson-dfs#p8`.

## 46. seed 1554410322730604053, level 1

A directed graph on vertices 0 to 4 has edges `0->1`, `2->0`, `2->1`, `2->3`, `3->0`, `3->1`, `3->4`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `3, 4, 0, 1, 2`
b) `2, 3, 4, 0, 1`
c) `1, 0, 4, 3, 2`
d) `0, 1, 2, 3, 4`

**Key: b**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `2, 3, 4, 0, 1`. Checking each edge: 1. `0->1` has 0 at place 4 and 1 at place 5; 2. `2->0` has 2 at place 1 and 0 at place 4; 3. `2->1` has 2 at place 1 and 1 at place 5; 4. `2->3` has 2 at place 1 and 3 at place 2; 5. `3->0` has 3 at place 2 and 0 at place 4; 6. `3->1` has 3 at place 2 and 1 at place 5; 7. `3->4` has 3 at place 2 and 4 at place 3. Every tail is left of its head. The postorder itself, `1, 0, 4, 3, 2`, fails on `0->1`. Source: `erickson-dfs#p8`.

## 47. seed 307223659931345996, level 1

A directed graph on vertices 0 to 4 has edges `0->1`, `2->1`, `3->1`, `3->2`, `3->4`, `4->1`, `4->2`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `0, 1, 2, 3, 4`
b) `3, 4, 2, 0, 1`
c) `3, 4, 2, 1, 0`
d) `4, 2, 0, 1, 3`

**Key: b**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `3, 4, 2, 0, 1`. Checking each edge: 1. `0->1` has 0 at place 4 and 1 at place 5; 2. `2->1` has 2 at place 3 and 1 at place 5; 3. `3->1` has 3 at place 1 and 1 at place 5; 4. `3->2` has 3 at place 1 and 2 at place 3; 5. `3->4` has 3 at place 1 and 4 at place 2; 6. `4->1` has 4 at place 2 and 1 at place 5; 7. `4->2` has 4 at place 2 and 2 at place 3. Every tail is left of its head. The postorder itself, `1, 0, 2, 4, 3`, fails on `0->1`. Source: `erickson-dfs#p8`.

## 48. seed 2328959132086887533, level 1

A directed graph on vertices 0 to 4 has edges `0->4`, `1->0`, `1->2`, `1->3`, `1->4`, `2->4`, `3->2`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `1, 3, 2, 0, 4`
b) `0, 1, 2, 3, 4`
c) `1, 3, 2, 4, 0`
d) `1, 0, 2, 3, 4`

**Key: a**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `1, 3, 2, 0, 4`. Checking each edge: 1. `0->4` has 0 at place 4 and 4 at place 5; 2. `1->0` has 1 at place 1 and 0 at place 4; 3. `1->2` has 1 at place 1 and 2 at place 3; 4. `1->3` has 1 at place 1 and 3 at place 2; 5. `1->4` has 1 at place 1 and 4 at place 5; 6. `2->4` has 2 at place 3 and 4 at place 5; 7. `3->2` has 3 at place 2 and 2 at place 3. Every tail is left of its head. The postorder itself, `4, 0, 2, 3, 1`, fails on `0->4`. Source: `erickson-dfs#p8`.

## 49. seed 1473492709819721102, level 2

A directed graph on vertices 0 to 5 has edges `0->2`, `0->4`, `1->4`, `4->2`, `5->0`, `5->2`, `5->4`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `5, 3, 1, 2, 4, 0`
b) `3, 1, 0, 4, 2, 5`
c) `2, 4, 0, 1, 3, 5`
d) `5, 3, 1, 0, 4, 2`

**Key: d**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `5, 3, 1, 0, 4, 2`. Checking each edge: 1. `0->2` has 0 at place 4 and 2 at place 6; 2. `0->4` has 0 at place 4 and 4 at place 5; 3. `1->4` has 1 at place 3 and 4 at place 5; 4. `4->2` has 4 at place 5 and 2 at place 6; 5. `5->0` has 5 at place 1 and 0 at place 4; 6. `5->2` has 5 at place 1 and 2 at place 6; 7. `5->4` has 5 at place 1 and 4 at place 5. Every tail is left of its head. The postorder itself, `2, 4, 0, 1, 3, 5`, fails on `0->2`. Source: `erickson-dfs#p8`.

## 50. seed 654749367069361476, level 1

A directed graph on vertices 0 to 4 has edges `0->1`, `0->3`, `0->4`, `2->0`, `2->1`, `2->3`, `2->4`. Which ordering of the vertices is a topological ordering, with every edge pointing from left to right?

a) `1, 3, 4, 0, 2`
b) `2, 0, 4, 3, 1`
c) `0, 4, 3, 1, 2`
d) `0, 1, 2, 3, 4`

**Key: b**

Explanation: An ordering is topological when every edge's tail comes before its head. The reversed postorder of a depth-first search is one: `2, 0, 4, 3, 1`. Checking each edge: 1. `0->1` has 0 at place 2 and 1 at place 5; 2. `0->3` has 0 at place 2 and 3 at place 4; 3. `0->4` has 0 at place 2 and 4 at place 3; 4. `2->0` has 2 at place 1 and 0 at place 2; 5. `2->1` has 2 at place 1 and 1 at place 5; 6. `2->3` has 2 at place 1 and 3 at place 4; 7. `2->4` has 2 at place 1 and 4 at place 3. Every tail is left of its head. The postorder itself, `1, 3, 4, 0, 2`, fails on `0->1`. Source: `erickson-dfs#p8`.
