# X-fast trie search levels (`xfast-level-probes`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 2989249904065103095, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 12`. Nodes match `x` at levels 0 to 7 only. Which levels `i` are probed, in order?

a) exactly the levels `6, 9, 7, 8`
b) levels `8, 7, 9, 6`, in order
c) the levels `7, 10, 9, 8`
d) levels `1, 2, 3, 4, 5, 6, 7, 8`, in order

**Key: a**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 12`: `i = (0 + 13) / 2 = 6`, a node matches, so `l = 6`; `i = (6 + 13) / 2 = 9`, no node matches, so `h = 9`; `i = (6 + 9) / 2 = 7`, a node matches, so `l = 7`; `i = (7 + 9) / 2 = 8`, no node matches, so `h = 8`. The loop ends with `l = 7` and `h = 8`, so `u` is at level 7. Wrong options: `7, 10, 9, 8` comes from rounding the middle up. `1, 2, 3, 4, 5, 6, 7, 8` comes from scanning the levels one by one. `8, 7, 9, 6` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 2. seed 2089903980018673370, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 15`. Nodes match `x` at levels 0 to 3 only. Which levels `i` are probed, in order?

a) the levels `8, 4, 2, 3`
b) levels `7, 3, 5, 4`, in order
c) `3, 2, 4, 8`
d) `1, 2, 3, 4`

**Key: a**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 15`: `i = (0 + 16) / 2 = 8`, no node matches, so `h = 8`; `i = (0 + 8) / 2 = 4`, no node matches, so `h = 4`; `i = (0 + 4) / 2 = 2`, a node matches, so `l = 2`; `i = (2 + 4) / 2 = 3`, a node matches, so `l = 3`. The loop ends with `l = 3` and `h = 4`, so `u` is at level 3. Wrong options: `7, 3, 5, 4` comes from starting with `h = w` instead of `h = w + 1`. `1, 2, 3, 4` comes from scanning the levels one by one. `3, 2, 4, 8` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 3. seed 1482798220490821298, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 7`. Nodes match `x` at levels 0 to 1 only. Which levels `i` are probed, in order?

a) levels `4, 6, 7`, in order
b) the levels `4, 2, 1`
c) exactly the levels `1, 2, 4`
d) `3, 1, 2`

**Key: b**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 7`: `i = (0 + 8) / 2 = 4`, no node matches, so `h = 4`; `i = (0 + 4) / 2 = 2`, no node matches, so `h = 2`; `i = (0 + 2) / 2 = 1`, a node matches, so `l = 1`. The loop ends with `l = 1` and `h = 2`, so `u` is at level 1. Wrong options: `3, 1, 2` comes from starting with `h = w` instead of `h = w + 1`. `4, 6, 7` comes from swapping the two updates. `1, 2, 4` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 4. seed 4214159596531239439, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 15`. Nodes match `x` at levels 0 to 2 only. Which levels `i` are probed, in order?

a) the levels `8, 4, 2, 3`
b) exactly the levels `8, 12, 14, 15`
c) `3, 2, 4, 8`
d) the levels `7, 3, 1, 2`

**Key: a**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 15`: `i = (0 + 16) / 2 = 8`, no node matches, so `h = 8`; `i = (0 + 8) / 2 = 4`, no node matches, so `h = 4`; `i = (0 + 4) / 2 = 2`, a node matches, so `l = 2`; `i = (2 + 4) / 2 = 3`, no node matches, so `h = 3`. The loop ends with `l = 2` and `h = 3`, so `u` is at level 2. Wrong options: `7, 3, 1, 2` comes from starting with `h = w` instead of `h = w + 1`. `8, 12, 14, 15` comes from swapping the two updates. `3, 2, 4, 8` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 5. seed 1307208811053241090, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 15`. Nodes match `x` at levels 0 to 12 only. Which levels `i` are probed, in order?

a) exactly the levels `1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13`
b) `8, 12, 14, 13`
c) levels `13, 14, 12, 8`, in order
d) `8, 4, 2, 1`

**Key: b**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 15`: `i = (0 + 16) / 2 = 8`, a node matches, so `l = 8`; `i = (8 + 16) / 2 = 12`, a node matches, so `l = 12`; `i = (12 + 16) / 2 = 14`, no node matches, so `h = 14`; `i = (12 + 14) / 2 = 13`, no node matches, so `h = 13`. The loop ends with `l = 12` and `h = 13`, so `u` is at level 12. Wrong options: `8, 4, 2, 1` comes from swapping the two updates. `1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13` comes from scanning the levels one by one. `13, 14, 12, 8` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 6. seed 3402300915534916747, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 7`. Nodes match `x` at levels 0 to 1 only. Which levels `i` are probed, in order?

a) the levels `3, 1, 2`
b) the levels `4, 2, 1`
c) the levels `4, 6, 7`
d) the levels `1, 2, 4`

**Key: b**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 7`: `i = (0 + 8) / 2 = 4`, no node matches, so `h = 4`; `i = (0 + 4) / 2 = 2`, no node matches, so `h = 2`; `i = (0 + 2) / 2 = 1`, a node matches, so `l = 1`. The loop ends with `l = 1` and `h = 2`, so `u` is at level 1. Wrong options: `3, 1, 2` comes from starting with `h = w` instead of `h = w + 1`. `4, 6, 7` comes from swapping the two updates. `1, 2, 4` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 7. seed 522071060213833496, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 8`. Nodes match `x` at levels 0 to 3 only. Which levels `i` are probed, in order?

a) levels `3, 2, 4`, in order
b) exactly the levels `4, 6, 7, 8`
c) the levels `4, 2, 3`
d) levels `5, 3, 4`, in order

**Key: c**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 8`: `i = (0 + 9) / 2 = 4`, no node matches, so `h = 4`; `i = (0 + 4) / 2 = 2`, a node matches, so `l = 2`; `i = (2 + 4) / 2 = 3`, a node matches, so `l = 3`. The loop ends with `l = 3` and `h = 4`, so `u` is at level 3. Wrong options: `5, 3, 4` comes from rounding the middle up. `4, 6, 7, 8` comes from swapping the two updates. `3, 2, 4` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 8. seed 1163056906309116494, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 7`. Nodes match `x` at levels 0 to 2 only. Which levels `i` are probed, in order?

a) exactly the levels `3, 1, 2`
b) `4, 6, 7`
c) `4, 2, 3`
d) exactly the levels `1, 2, 3`

**Key: c**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 7`: `i = (0 + 8) / 2 = 4`, no node matches, so `h = 4`; `i = (0 + 4) / 2 = 2`, a node matches, so `l = 2`; `i = (2 + 4) / 2 = 3`, no node matches, so `h = 3`. The loop ends with `l = 2` and `h = 3`, so `u` is at level 2. Wrong options: `3, 1, 2` comes from starting with `h = w` instead of `h = w + 1`. `4, 6, 7` comes from swapping the two updates. `1, 2, 3` comes from scanning the levels one by one. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 9. seed 3375275584501989805, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 12`. Nodes match `x` at levels 0 to 6 only. Which levels `i` are probed, in order?

a) levels `7, 9, 6`, in order
b) levels `7, 4, 6`, in order
c) the levels `6, 3, 1`
d) `6, 9, 7`

**Key: d**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 12`: `i = (0 + 13) / 2 = 6`, a node matches, so `l = 6`; `i = (6 + 13) / 2 = 9`, no node matches, so `h = 9`; `i = (6 + 9) / 2 = 7`, no node matches, so `h = 7`. The loop ends with `l = 6` and `h = 7`, so `u` is at level 6. Wrong options: `7, 4, 6` comes from rounding the middle up. `6, 3, 1` comes from swapping the two updates. `7, 9, 6` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 10. seed 984343057014706521, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 7`. Nodes match `x` at levels 0 to 1 only. Which levels `i` are probed, in order?

a) exactly the levels `3, 1, 2`
b) the levels `4, 2, 1`
c) `1, 2, 4`
d) the levels `4, 6, 7`

**Key: b**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 7`: `i = (0 + 8) / 2 = 4`, no node matches, so `h = 4`; `i = (0 + 4) / 2 = 2`, no node matches, so `h = 2`; `i = (0 + 2) / 2 = 1`, a node matches, so `l = 1`. The loop ends with `l = 1` and `h = 2`, so `u` is at level 1. Wrong options: `3, 1, 2` comes from starting with `h = w` instead of `h = w + 1`. `4, 6, 7` comes from swapping the two updates. `1, 2, 4` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 11. seed 2961743656407667993, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 11`. Nodes match `x` at levels 0 to 7 only. Which levels `i` are probed, in order?

a) the levels `8, 7, 9, 6`
b) exactly the levels `5, 8, 6, 7`
c) exactly the levels `6, 9, 8, 7`
d) levels `6, 9, 7, 8`, in order

**Key: d**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 11`: `i = (0 + 12) / 2 = 6`, a node matches, so `l = 6`; `i = (6 + 12) / 2 = 9`, no node matches, so `h = 9`; `i = (6 + 9) / 2 = 7`, a node matches, so `l = 7`; `i = (7 + 9) / 2 = 8`, no node matches, so `h = 8`. The loop ends with `l = 7` and `h = 8`, so `u` is at level 7. Wrong options: `6, 9, 8, 7` comes from rounding the middle up. `5, 8, 6, 7` comes from starting with `h = w` instead of `h = w + 1`. `8, 7, 9, 6` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 12. seed 3094774772346926058, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 15`. Nodes match `x` at levels 0 to 14 only. Which levels `i` are probed, in order?

a) `8, 12, 14, 15`
b) the levels `15, 14, 12, 8`
c) levels `1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15`, in order
d) the levels `8, 4, 2, 1`

**Key: a**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 15`: `i = (0 + 16) / 2 = 8`, a node matches, so `l = 8`; `i = (8 + 16) / 2 = 12`, a node matches, so `l = 12`; `i = (12 + 16) / 2 = 14`, a node matches, so `l = 14`; `i = (14 + 16) / 2 = 15`, no node matches, so `h = 15`. The loop ends with `l = 14` and `h = 15`, so `u` is at level 14. Wrong options: `8, 4, 2, 1` comes from swapping the two updates. `1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15` comes from scanning the levels one by one. `15, 14, 12, 8` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 13. seed 4089628360884770182, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 15`. Nodes match `x` at levels 0 to 5 only. Which levels `i` are probed, in order?

a) exactly the levels `8, 12, 14, 15`
b) exactly the levels `8, 4, 6, 5`
c) the levels `7, 3, 5, 6`
d) levels `5, 6, 4, 8`, in order

**Key: b**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 15`: `i = (0 + 16) / 2 = 8`, no node matches, so `h = 8`; `i = (0 + 8) / 2 = 4`, a node matches, so `l = 4`; `i = (4 + 8) / 2 = 6`, no node matches, so `h = 6`; `i = (4 + 6) / 2 = 5`, a node matches, so `l = 5`. The loop ends with `l = 5` and `h = 6`, so `u` is at level 5. Wrong options: `7, 3, 5, 6` comes from starting with `h = w` instead of `h = w + 1`. `8, 12, 14, 15` comes from swapping the two updates. `5, 6, 4, 8` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 14. seed 2109091277835392744, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 11`. Nodes match `x` at levels 0 to 8 only. Which levels `i` are probed, in order?

a) the levels `6, 9, 7, 8`
b) exactly the levels `8, 7, 9, 6`
c) levels `5, 8, 9`, in order
d) levels `1, 2, 3, 4, 5, 6, 7, 8, 9`, in order

**Key: a**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 11`: `i = (0 + 12) / 2 = 6`, a node matches, so `l = 6`; `i = (6 + 12) / 2 = 9`, no node matches, so `h = 9`; `i = (6 + 9) / 2 = 7`, a node matches, so `l = 7`; `i = (7 + 9) / 2 = 8`, a node matches, so `l = 8`. The loop ends with `l = 8` and `h = 9`, so `u` is at level 8. Wrong options: `5, 8, 9` comes from starting with `h = w` instead of `h = w + 1`. `1, 2, 3, 4, 5, 6, 7, 8, 9` comes from scanning the levels one by one. `8, 7, 9, 6` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 15. seed 316798522218093907, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 15`. Nodes match `x` at levels 0 to 12 only. Which levels `i` are probed, in order?

a) `13, 14, 12, 8`
b) levels `8, 12, 14, 13`, in order
c) levels `8, 4, 2, 1`, in order
d) exactly the levels `1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13`

**Key: b**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 15`: `i = (0 + 16) / 2 = 8`, a node matches, so `l = 8`; `i = (8 + 16) / 2 = 12`, a node matches, so `l = 12`; `i = (12 + 16) / 2 = 14`, no node matches, so `h = 14`; `i = (12 + 14) / 2 = 13`, no node matches, so `h = 13`. The loop ends with `l = 12` and `h = 13`, so `u` is at level 12. Wrong options: `8, 4, 2, 1` comes from swapping the two updates. `1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13` comes from scanning the levels one by one. `13, 14, 12, 8` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 16. seed 79158539621666491, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 8`. Nodes match `x` at levels 0 to 2 only. Which levels `i` are probed, in order?

a) the levels `1, 2, 3`
b) exactly the levels `3, 2, 4`
c) the levels `5, 3, 2`
d) levels `4, 2, 3`, in order

**Key: d**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 8`: `i = (0 + 9) / 2 = 4`, no node matches, so `h = 4`; `i = (0 + 4) / 2 = 2`, a node matches, so `l = 2`; `i = (2 + 4) / 2 = 3`, no node matches, so `h = 3`. The loop ends with `l = 2` and `h = 3`, so `u` is at level 2. Wrong options: `5, 3, 2` comes from rounding the middle up. `1, 2, 3` comes from scanning the levels one by one. `3, 2, 4` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 17. seed 4038827084382892580, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 11`. Nodes match `x` at levels 0 to 3 only. Which levels `i` are probed, in order?

a) levels `6, 3, 4`, in order
b) levels `4, 3, 6`, in order
c) `1, 2, 3, 4`
d) the levels `5, 2, 3, 4`

**Key: a**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 11`: `i = (0 + 12) / 2 = 6`, no node matches, so `h = 6`; `i = (0 + 6) / 2 = 3`, a node matches, so `l = 3`; `i = (3 + 6) / 2 = 4`, no node matches, so `h = 4`. The loop ends with `l = 3` and `h = 4`, so `u` is at level 3. Wrong options: `5, 2, 3, 4` comes from starting with `h = w` instead of `h = w + 1`. `1, 2, 3, 4` comes from scanning the levels one by one. `4, 3, 6` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 18. seed 1603983453644263607, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 12`. Nodes match `x` at levels 0 to 9 only. Which levels `i` are probed, in order?

a) exactly the levels `6, 9, 11, 10`
b) exactly the levels `1, 2, 3, 4, 5, 6, 7, 8, 9, 10`
c) levels `6, 3, 1`, in order
d) the levels `6, 9, 10`

**Key: a**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 12`: `i = (0 + 13) / 2 = 6`, a node matches, so `l = 6`; `i = (6 + 13) / 2 = 9`, a node matches, so `l = 9`; `i = (9 + 13) / 2 = 11`, no node matches, so `h = 11`; `i = (9 + 11) / 2 = 10`, no node matches, so `h = 10`. The loop ends with `l = 9` and `h = 10`, so `u` is at level 9. Wrong options: `6, 9, 10` comes from starting with `h = w` instead of `h = w + 1`. `6, 3, 1` comes from swapping the two updates. `1, 2, 3, 4, 5, 6, 7, 8, 9, 10` comes from scanning the levels one by one. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 19. seed 2770662978451205983, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 8`. Nodes match `x` at levels 0 to 5 only. Which levels `i` are probed, in order?

a) `5, 7, 6`
b) levels `5, 6, 4`, in order
c) `4, 2, 1`
d) `4, 6, 5`

**Key: d**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 8`: `i = (0 + 9) / 2 = 4`, a node matches, so `l = 4`; `i = (4 + 9) / 2 = 6`, no node matches, so `h = 6`; `i = (4 + 6) / 2 = 5`, a node matches, so `l = 5`. The loop ends with `l = 5` and `h = 6`, so `u` is at level 5. Wrong options: `5, 7, 6` comes from rounding the middle up. `4, 2, 1` comes from swapping the two updates. `5, 6, 4` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 20. seed 3101984600554739836, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 7`. Nodes match `x` at levels 0 to 6 only. Which levels `i` are probed, in order?

a) exactly the levels `4, 6, 7`
b) exactly the levels `7, 6, 4`
c) the levels `4, 2, 1`
d) `3, 5, 6`

**Key: a**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 7`: `i = (0 + 8) / 2 = 4`, a node matches, so `l = 4`; `i = (4 + 8) / 2 = 6`, a node matches, so `l = 6`; `i = (6 + 8) / 2 = 7`, no node matches, so `h = 7`. The loop ends with `l = 6` and `h = 7`, so `u` is at level 6. Wrong options: `3, 5, 6` comes from starting with `h = w` instead of `h = w + 1`. `4, 2, 1` comes from swapping the two updates. `7, 6, 4` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 21. seed 309709893927477181, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 7`. Nodes match `x` at levels 0 to 1 only. Which levels `i` are probed, in order?

a) exactly the levels `4, 2, 1`
b) `4, 6, 7`
c) `1, 2, 4`
d) levels `3, 1, 2`, in order

**Key: a**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 7`: `i = (0 + 8) / 2 = 4`, no node matches, so `h = 4`; `i = (0 + 4) / 2 = 2`, no node matches, so `h = 2`; `i = (0 + 2) / 2 = 1`, a node matches, so `l = 1`. The loop ends with `l = 1` and `h = 2`, so `u` is at level 1. Wrong options: `3, 1, 2` comes from starting with `h = w` instead of `h = w + 1`. `4, 6, 7` comes from swapping the two updates. `1, 2, 4` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 22. seed 3257245980626081163, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 8`. Nodes match `x` at levels 0 to 3 only. Which levels `i` are probed, in order?

a) levels `4, 2, 3`, in order
b) the levels `5, 3, 4`
c) exactly the levels `4, 6, 7, 8`
d) `3, 2, 4`

**Key: a**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 8`: `i = (0 + 9) / 2 = 4`, no node matches, so `h = 4`; `i = (0 + 4) / 2 = 2`, a node matches, so `l = 2`; `i = (2 + 4) / 2 = 3`, a node matches, so `l = 3`. The loop ends with `l = 3` and `h = 4`, so `u` is at level 3. Wrong options: `5, 3, 4` comes from rounding the middle up. `4, 6, 7, 8` comes from swapping the two updates. `3, 2, 4` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 23. seed 3049542464495065836, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 15`. Nodes match `x` at levels 0 to 5 only. Which levels `i` are probed, in order?

a) levels `8, 12, 14, 15`, in order
b) `5, 6, 4, 8`
c) levels `1, 2, 3, 4, 5, 6`, in order
d) exactly the levels `8, 4, 6, 5`

**Key: d**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 15`: `i = (0 + 16) / 2 = 8`, no node matches, so `h = 8`; `i = (0 + 8) / 2 = 4`, a node matches, so `l = 4`; `i = (4 + 8) / 2 = 6`, no node matches, so `h = 6`; `i = (4 + 6) / 2 = 5`, a node matches, so `l = 5`. The loop ends with `l = 5` and `h = 6`, so `u` is at level 5. Wrong options: `8, 12, 14, 15` comes from swapping the two updates. `1, 2, 3, 4, 5, 6` comes from scanning the levels one by one. `5, 6, 4, 8` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 24. seed 1997929814446948520, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 15`. Nodes match `x` at levels 0 to 2 only. Which levels `i` are probed, in order?

a) exactly the levels `8, 12, 14, 15`
b) `1, 2, 3`
c) exactly the levels `8, 4, 2, 3`
d) the levels `3, 2, 4, 8`

**Key: c**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 15`: `i = (0 + 16) / 2 = 8`, no node matches, so `h = 8`; `i = (0 + 8) / 2 = 4`, no node matches, so `h = 4`; `i = (0 + 4) / 2 = 2`, a node matches, so `l = 2`; `i = (2 + 4) / 2 = 3`, no node matches, so `h = 3`. The loop ends with `l = 2` and `h = 3`, so `u` is at level 2. Wrong options: `8, 12, 14, 15` comes from swapping the two updates. `1, 2, 3` comes from scanning the levels one by one. `3, 2, 4, 8` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 25. seed 340722867985529540, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 12`. Nodes match `x` at levels 0 to 7 only. Which levels `i` are probed, in order?

a) the levels `7, 10, 9, 8`
b) exactly the levels `6, 9, 7, 8`
c) exactly the levels `8, 7, 9, 6`
d) levels `1, 2, 3, 4, 5, 6, 7, 8`, in order

**Key: b**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 12`: `i = (0 + 13) / 2 = 6`, a node matches, so `l = 6`; `i = (6 + 13) / 2 = 9`, no node matches, so `h = 9`; `i = (6 + 9) / 2 = 7`, a node matches, so `l = 7`; `i = (7 + 9) / 2 = 8`, no node matches, so `h = 8`. The loop ends with `l = 7` and `h = 8`, so `u` is at level 7. Wrong options: `7, 10, 9, 8` comes from rounding the middle up. `1, 2, 3, 4, 5, 6, 7, 8` comes from scanning the levels one by one. `8, 7, 9, 6` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 26. seed 2391417175972104182, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 12`. Nodes match `x` at levels 0 to 7 only. Which levels `i` are probed, in order?

a) exactly the levels `6, 3, 1`
b) levels `1, 2, 3, 4, 5, 6, 7, 8`, in order
c) levels `6, 9, 7, 8`, in order
d) levels `7, 10, 9, 8`, in order

**Key: c**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 12`: `i = (0 + 13) / 2 = 6`, a node matches, so `l = 6`; `i = (6 + 13) / 2 = 9`, no node matches, so `h = 9`; `i = (6 + 9) / 2 = 7`, a node matches, so `l = 7`; `i = (7 + 9) / 2 = 8`, no node matches, so `h = 8`. The loop ends with `l = 7` and `h = 8`, so `u` is at level 7. Wrong options: `7, 10, 9, 8` comes from rounding the middle up. `6, 3, 1` comes from swapping the two updates. `1, 2, 3, 4, 5, 6, 7, 8` comes from scanning the levels one by one. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 27. seed 3099788110874722279, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 15`. Nodes match `x` at levels 0 to 5 only. Which levels `i` are probed, in order?

a) `7, 3, 5, 6`
b) the levels `5, 6, 4, 8`
c) `8, 12, 14, 15`
d) `8, 4, 6, 5`

**Key: d**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 15`: `i = (0 + 16) / 2 = 8`, no node matches, so `h = 8`; `i = (0 + 8) / 2 = 4`, a node matches, so `l = 4`; `i = (4 + 8) / 2 = 6`, no node matches, so `h = 6`; `i = (4 + 6) / 2 = 5`, a node matches, so `l = 5`. The loop ends with `l = 5` and `h = 6`, so `u` is at level 5. Wrong options: `7, 3, 5, 6` comes from starting with `h = w` instead of `h = w + 1`. `8, 12, 14, 15` comes from swapping the two updates. `5, 6, 4, 8` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 28. seed 840959717895098029, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 12`. Nodes match `x` at levels 0 to 1 only. Which levels `i` are probed, in order?

a) `1, 2`
b) exactly the levels `2, 1, 3, 6`
c) levels `7, 4, 2, 1`, in order
d) levels `6, 3, 1, 2`, in order

**Key: d**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 12`: `i = (0 + 13) / 2 = 6`, no node matches, so `h = 6`; `i = (0 + 6) / 2 = 3`, no node matches, so `h = 3`; `i = (0 + 3) / 2 = 1`, a node matches, so `l = 1`; `i = (1 + 3) / 2 = 2`, no node matches, so `h = 2`. The loop ends with `l = 1` and `h = 2`, so `u` is at level 1. Wrong options: `7, 4, 2, 1` comes from rounding the middle up. `1, 2` comes from scanning the levels one by one. `2, 1, 3, 6` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 29. seed 2033585496735404935, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 7`. Nodes match `x` at levels 0 to 2 only. Which levels `i` are probed, in order?

a) `1, 2, 3`
b) the levels `3, 2, 4`
c) exactly the levels `4, 2, 3`
d) the levels `3, 1, 2`

**Key: c**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 7`: `i = (0 + 8) / 2 = 4`, no node matches, so `h = 4`; `i = (0 + 4) / 2 = 2`, a node matches, so `l = 2`; `i = (2 + 4) / 2 = 3`, no node matches, so `h = 3`. The loop ends with `l = 2` and `h = 3`, so `u` is at level 2. Wrong options: `3, 1, 2` comes from starting with `h = w` instead of `h = w + 1`. `1, 2, 3` comes from scanning the levels one by one. `3, 2, 4` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 30. seed 4331953891865569700, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 7`. Nodes match `x` at levels 0 to 6 only. Which levels `i` are probed, in order?

a) levels `4, 6, 7`, in order
b) exactly the levels `7, 6, 4`
c) the levels `4, 2, 1`
d) levels `3, 5, 6`, in order

**Key: a**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 7`: `i = (0 + 8) / 2 = 4`, a node matches, so `l = 4`; `i = (4 + 8) / 2 = 6`, a node matches, so `l = 6`; `i = (6 + 8) / 2 = 7`, no node matches, so `h = 7`. The loop ends with `l = 6` and `h = 7`, so `u` is at level 6. Wrong options: `3, 5, 6` comes from starting with `h = w` instead of `h = w + 1`. `4, 2, 1` comes from swapping the two updates. `7, 6, 4` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 31. seed 3870450723973313249, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 12`. Nodes match `x` at levels 0 to 6 only. Which levels `i` are probed, in order?

a) the levels `7, 4, 6`
b) exactly the levels `7, 9, 6`
c) levels `6, 3, 1`, in order
d) the levels `6, 9, 7`

**Key: d**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 12`: `i = (0 + 13) / 2 = 6`, a node matches, so `l = 6`; `i = (6 + 13) / 2 = 9`, no node matches, so `h = 9`; `i = (6 + 9) / 2 = 7`, no node matches, so `h = 7`. The loop ends with `l = 6` and `h = 7`, so `u` is at level 6. Wrong options: `7, 4, 6` comes from rounding the middle up. `6, 3, 1` comes from swapping the two updates. `7, 9, 6` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 32. seed 1130115234086428779, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 11`. Nodes match `x` at levels 0 to 8 only. Which levels `i` are probed, in order?

a) levels `6, 9, 8`, in order
b) exactly the levels `8, 7, 9, 6`
c) levels `5, 8, 9`, in order
d) exactly the levels `6, 9, 7, 8`

**Key: d**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 11`: `i = (0 + 12) / 2 = 6`, a node matches, so `l = 6`; `i = (6 + 12) / 2 = 9`, no node matches, so `h = 9`; `i = (6 + 9) / 2 = 7`, a node matches, so `l = 7`; `i = (7 + 9) / 2 = 8`, a node matches, so `l = 8`. The loop ends with `l = 8` and `h = 9`, so `u` is at level 8. Wrong options: `6, 9, 8` comes from rounding the middle up. `5, 8, 9` comes from starting with `h = w` instead of `h = w + 1`. `8, 7, 9, 6` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 33. seed 1884222661205297732, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 7`. Nodes match `x` at levels 0 to 6 only. Which levels `i` are probed, in order?

a) levels `4, 2, 1`, in order
b) `4, 6, 7`
c) `3, 5, 6`
d) the levels `7, 6, 4`

**Key: b**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 7`: `i = (0 + 8) / 2 = 4`, a node matches, so `l = 4`; `i = (4 + 8) / 2 = 6`, a node matches, so `l = 6`; `i = (6 + 8) / 2 = 7`, no node matches, so `h = 7`. The loop ends with `l = 6` and `h = 7`, so `u` is at level 6. Wrong options: `3, 5, 6` comes from starting with `h = w` instead of `h = w + 1`. `4, 2, 1` comes from swapping the two updates. `7, 6, 4` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 34. seed 4279394570373665624, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 11`. Nodes match `x` at levels 0 to 8 only. Which levels `i` are probed, in order?

a) levels `1, 2, 3, 4, 5, 6, 7, 8, 9`, in order
b) levels `8, 7, 9, 6`, in order
c) exactly the levels `6, 9, 7, 8`
d) the levels `5, 8, 9`

**Key: c**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 11`: `i = (0 + 12) / 2 = 6`, a node matches, so `l = 6`; `i = (6 + 12) / 2 = 9`, no node matches, so `h = 9`; `i = (6 + 9) / 2 = 7`, a node matches, so `l = 7`; `i = (7 + 9) / 2 = 8`, a node matches, so `l = 8`. The loop ends with `l = 8` and `h = 9`, so `u` is at level 8. Wrong options: `5, 8, 9` comes from starting with `h = w` instead of `h = w + 1`. `1, 2, 3, 4, 5, 6, 7, 8, 9` comes from scanning the levels one by one. `8, 7, 9, 6` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 35. seed 3216826693458825016, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 12`. Nodes match `x` at levels 0 to 2 only. Which levels `i` are probed, in order?

a) the levels `7, 4, 2, 3`
b) levels `1, 2, 3`, in order
c) exactly the levels `6, 3, 1, 2`
d) the levels `2, 1, 3, 6`

**Key: c**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 12`: `i = (0 + 13) / 2 = 6`, no node matches, so `h = 6`; `i = (0 + 6) / 2 = 3`, no node matches, so `h = 3`; `i = (0 + 3) / 2 = 1`, a node matches, so `l = 1`; `i = (1 + 3) / 2 = 2`, a node matches, so `l = 2`. The loop ends with `l = 2` and `h = 3`, so `u` is at level 2. Wrong options: `7, 4, 2, 3` comes from rounding the middle up. `1, 2, 3` comes from scanning the levels one by one. `2, 1, 3, 6` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 36. seed 4031281631744016877, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 8`. Nodes match `x` at levels 0 to 1 only. Which levels `i` are probed, in order?

a) exactly the levels `5, 3, 2, 1`
b) `4, 6, 7, 8`
c) `1, 2, 4`
d) levels `4, 2, 1`, in order

**Key: d**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 8`: `i = (0 + 9) / 2 = 4`, no node matches, so `h = 4`; `i = (0 + 4) / 2 = 2`, no node matches, so `h = 2`; `i = (0 + 2) / 2 = 1`, a node matches, so `l = 1`. The loop ends with `l = 1` and `h = 2`, so `u` is at level 1. Wrong options: `5, 3, 2, 1` comes from rounding the middle up. `4, 6, 7, 8` comes from swapping the two updates. `1, 2, 4` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 37. seed 4515377979804487155, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 15`. Nodes match `x` at levels 0 to 2 only. Which levels `i` are probed, in order?

a) the levels `3, 2, 4, 8`
b) exactly the levels `8, 4, 2, 3`
c) levels `7, 3, 1, 2`, in order
d) the levels `8, 12, 14, 15`

**Key: b**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 15`: `i = (0 + 16) / 2 = 8`, no node matches, so `h = 8`; `i = (0 + 8) / 2 = 4`, no node matches, so `h = 4`; `i = (0 + 4) / 2 = 2`, a node matches, so `l = 2`; `i = (2 + 4) / 2 = 3`, no node matches, so `h = 3`. The loop ends with `l = 2` and `h = 3`, so `u` is at level 2. Wrong options: `7, 3, 1, 2` comes from starting with `h = w` instead of `h = w + 1`. `8, 12, 14, 15` comes from swapping the two updates. `3, 2, 4, 8` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 38. seed 1200095746968456303, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 7`. Nodes match `x` at levels 0 to 3 only. Which levels `i` are probed, in order?

a) `3, 2, 4`
b) `3, 5, 4`
c) exactly the levels `4, 6, 7`
d) `4, 2, 3`

**Key: d**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 7`: `i = (0 + 8) / 2 = 4`, no node matches, so `h = 4`; `i = (0 + 4) / 2 = 2`, a node matches, so `l = 2`; `i = (2 + 4) / 2 = 3`, a node matches, so `l = 3`. The loop ends with `l = 3` and `h = 4`, so `u` is at level 3. Wrong options: `3, 5, 4` comes from starting with `h = w` instead of `h = w + 1`. `4, 6, 7` comes from swapping the two updates. `3, 2, 4` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 39. seed 3397299822820033936, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 7`. Nodes match `x` at levels 0 to 1 only. Which levels `i` are probed, in order?

a) exactly the levels `3, 1, 2`
b) exactly the levels `4, 2, 1`
c) `4, 6, 7`
d) exactly the levels `1, 2, 4`

**Key: b**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 7`: `i = (0 + 8) / 2 = 4`, no node matches, so `h = 4`; `i = (0 + 4) / 2 = 2`, no node matches, so `h = 2`; `i = (0 + 2) / 2 = 1`, a node matches, so `l = 1`. The loop ends with `l = 1` and `h = 2`, so `u` is at level 1. Wrong options: `3, 1, 2` comes from starting with `h = w` instead of `h = w + 1`. `4, 6, 7` comes from swapping the two updates. `1, 2, 4` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 40. seed 4608153152776381370, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 8`. Nodes match `x` at levels 0 to 2 only. Which levels `i` are probed, in order?

a) `5, 3, 2`
b) `1, 2, 3`
c) `3, 2, 4`
d) `4, 2, 3`

**Key: d**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 8`: `i = (0 + 9) / 2 = 4`, no node matches, so `h = 4`; `i = (0 + 4) / 2 = 2`, a node matches, so `l = 2`; `i = (2 + 4) / 2 = 3`, no node matches, so `h = 3`. The loop ends with `l = 2` and `h = 3`, so `u` is at level 2. Wrong options: `5, 3, 2` comes from rounding the middle up. `1, 2, 3` comes from scanning the levels one by one. `3, 2, 4` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 41. seed 1616360194475250911, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 12`. Nodes match `x` at levels 0 to 7 only. Which levels `i` are probed, in order?

a) `1, 2, 3, 4, 5, 6, 7, 8`
b) the levels `6, 3, 1`
c) levels `6, 9, 7, 8`, in order
d) the levels `8, 7, 9, 6`

**Key: c**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 12`: `i = (0 + 13) / 2 = 6`, a node matches, so `l = 6`; `i = (6 + 13) / 2 = 9`, no node matches, so `h = 9`; `i = (6 + 9) / 2 = 7`, a node matches, so `l = 7`; `i = (7 + 9) / 2 = 8`, no node matches, so `h = 8`. The loop ends with `l = 7` and `h = 8`, so `u` is at level 7. Wrong options: `6, 3, 1` comes from swapping the two updates. `1, 2, 3, 4, 5, 6, 7, 8` comes from scanning the levels one by one. `8, 7, 9, 6` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 42. seed 3458674026923949838, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 7`. Nodes match `x` at levels 0 to 2 only. Which levels `i` are probed, in order?

a) levels `4, 2, 3`, in order
b) the levels `1, 2, 3`
c) `3, 1, 2`
d) the levels `4, 6, 7`

**Key: a**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 7`: `i = (0 + 8) / 2 = 4`, no node matches, so `h = 4`; `i = (0 + 4) / 2 = 2`, a node matches, so `l = 2`; `i = (2 + 4) / 2 = 3`, no node matches, so `h = 3`. The loop ends with `l = 2` and `h = 3`, so `u` is at level 2. Wrong options: `3, 1, 2` comes from starting with `h = w` instead of `h = w + 1`. `4, 6, 7` comes from swapping the two updates. `1, 2, 3` comes from scanning the levels one by one. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 43. seed 2990279318982096528, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 15`. Nodes match `x` at levels 0 to 8 only. Which levels `i` are probed, in order?

a) the levels `1, 2, 3, 4, 5, 6, 7, 8, 9`
b) levels `8, 4, 2, 1`, in order
c) the levels `7, 11, 9, 8`
d) levels `8, 12, 10, 9`, in order

**Key: d**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 15`: `i = (0 + 16) / 2 = 8`, a node matches, so `l = 8`; `i = (8 + 16) / 2 = 12`, no node matches, so `h = 12`; `i = (8 + 12) / 2 = 10`, no node matches, so `h = 10`; `i = (8 + 10) / 2 = 9`, no node matches, so `h = 9`. The loop ends with `l = 8` and `h = 9`, so `u` is at level 8. Wrong options: `7, 11, 9, 8` comes from starting with `h = w` instead of `h = w + 1`. `8, 4, 2, 1` comes from swapping the two updates. `1, 2, 3, 4, 5, 6, 7, 8, 9` comes from scanning the levels one by one. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 44. seed 3705569484121518684, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 12`. Nodes match `x` at levels 0 to 9 only. Which levels `i` are probed, in order?

a) the levels `7, 10, 9`
b) `6, 3, 1`
c) levels `6, 9, 11, 10`, in order
d) `6, 9, 10`

**Key: c**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 12`: `i = (0 + 13) / 2 = 6`, a node matches, so `l = 6`; `i = (6 + 13) / 2 = 9`, a node matches, so `l = 9`; `i = (9 + 13) / 2 = 11`, no node matches, so `h = 11`; `i = (9 + 11) / 2 = 10`, no node matches, so `h = 10`. The loop ends with `l = 9` and `h = 10`, so `u` is at level 9. Wrong options: `7, 10, 9` comes from rounding the middle up. `6, 9, 10` comes from starting with `h = w` instead of `h = w + 1`. `6, 3, 1` comes from swapping the two updates. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 45. seed 3366485280962244660, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 7`. Nodes match `x` at levels 0 to 2 only. Which levels `i` are probed, in order?

a) the levels `3, 1, 2`
b) the levels `4, 2, 3`
c) the levels `4, 6, 7`
d) exactly the levels `3, 2, 4`

**Key: b**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 7`: `i = (0 + 8) / 2 = 4`, no node matches, so `h = 4`; `i = (0 + 4) / 2 = 2`, a node matches, so `l = 2`; `i = (2 + 4) / 2 = 3`, no node matches, so `h = 3`. The loop ends with `l = 2` and `h = 3`, so `u` is at level 2. Wrong options: `3, 1, 2` comes from starting with `h = w` instead of `h = w + 1`. `4, 6, 7` comes from swapping the two updates. `3, 2, 4` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 46. seed 1674099570307621775, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 7`. Nodes match `x` at levels 0 to 6 only. Which levels `i` are probed, in order?

a) exactly the levels `3, 5, 6`
b) `4, 6, 7`
c) `7, 6, 4`
d) levels `4, 2, 1`, in order

**Key: b**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 7`: `i = (0 + 8) / 2 = 4`, a node matches, so `l = 4`; `i = (4 + 8) / 2 = 6`, a node matches, so `l = 6`; `i = (6 + 8) / 2 = 7`, no node matches, so `h = 7`. The loop ends with `l = 6` and `h = 7`, so `u` is at level 6. Wrong options: `3, 5, 6` comes from starting with `h = w` instead of `h = w + 1`. `4, 2, 1` comes from swapping the two updates. `7, 6, 4` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 47. seed 1947547319654724486, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 11`. Nodes match `x` at levels 0 to 7 only. Which levels `i` are probed, in order?

a) exactly the levels `8, 7, 9, 6`
b) exactly the levels `6, 9, 7, 8`
c) the levels `5, 8, 6, 7`
d) levels `6, 9, 8, 7`, in order

**Key: b**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 11`: `i = (0 + 12) / 2 = 6`, a node matches, so `l = 6`; `i = (6 + 12) / 2 = 9`, no node matches, so `h = 9`; `i = (6 + 9) / 2 = 7`, a node matches, so `l = 7`; `i = (7 + 9) / 2 = 8`, no node matches, so `h = 8`. The loop ends with `l = 7` and `h = 8`, so `u` is at level 7. Wrong options: `6, 9, 8, 7` comes from rounding the middle up. `5, 8, 6, 7` comes from starting with `h = w` instead of `h = w + 1`. `8, 7, 9, 6` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 48. seed 4086931141796254113, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 11`. Nodes match `x` at levels 0 to 3 only. Which levels `i` are probed, in order?

a) `4, 3, 6`
b) levels `6, 9, 10, 11`, in order
c) exactly the levels `1, 2, 3, 4`
d) levels `6, 3, 4`, in order

**Key: d**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 11`: `i = (0 + 12) / 2 = 6`, no node matches, so `h = 6`; `i = (0 + 6) / 2 = 3`, a node matches, so `l = 3`; `i = (3 + 6) / 2 = 4`, no node matches, so `h = 4`. The loop ends with `l = 3` and `h = 4`, so `u` is at level 3. Wrong options: `6, 9, 10, 11` comes from swapping the two updates. `1, 2, 3, 4` comes from scanning the levels one by one. `4, 3, 6` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 49. seed 3169851580044147327, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 11`. Nodes match `x` at levels 0 to 2 only. Which levels `i` are probed, in order?

a) the levels `6, 3, 2`
b) levels `6, 3, 1, 2`, in order
c) levels `1, 2, 3`, in order
d) exactly the levels `2, 1, 3, 6`

**Key: b**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 11`: `i = (0 + 12) / 2 = 6`, no node matches, so `h = 6`; `i = (0 + 6) / 2 = 3`, no node matches, so `h = 3`; `i = (0 + 3) / 2 = 1`, a node matches, so `l = 1`; `i = (1 + 3) / 2 = 2`, a node matches, so `l = 2`. The loop ends with `l = 2` and `h = 3`, so `u` is at level 2. Wrong options: `6, 3, 2` comes from rounding the middle up. `1, 2, 3` comes from scanning the levels one by one. `2, 1, 3, 6` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.

## 50. seed 1768241309018971469, level 2

In the Open Data Structures X-fast trie, the search starts at `l = 0`, `h = w + 1` with `w = 7`. Nodes match `x` at levels 0 to 6 only. Which levels `i` are probed, in order?

a) levels `3, 5, 6`, in order
b) `4, 2, 1`
c) exactly the levels `4, 6, 7`
d) the levels `7, 6, 4`

**Key: c**

Explanation: The search sets `l = i` when level i holds a matching node and `h = i` otherwise, and loops while `h - l > 1`. Here `w = 7`: `i = (0 + 8) / 2 = 4`, a node matches, so `l = 4`; `i = (4 + 8) / 2 = 6`, a node matches, so `l = 6`; `i = (6 + 8) / 2 = 7`, no node matches, so `h = 7`. The loop ends with `l = 6` and `h = 7`, so `u` is at level 6. Wrong options: `3, 5, 6` comes from starting with `h = w` instead of `h = w + 1`. `4, 2, 1` comes from swapping the two updates. `7, 6, 4` is the right probes in reverse order. Source: `ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000`.
