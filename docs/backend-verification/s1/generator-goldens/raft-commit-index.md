# Raft commit index (`raft-commit-index`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 1813378012646337334, level 1

A Raft cluster has 5 servers; the leader's log ends at index 9. The followers' match indexes are 7, 4, 9, 8. All entries come from the leader's current term. What is the highest committed index?

a) 8
b) 9
c) 7
d) 4

**Key: a**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 9, 7, 4, 9, 8 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 9, 9, 8, 7, 4. Step 3: the index 8 in position 3 is reached by 3 servers, and no higher index is. Result: 8. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 2. seed 2298969832352979512, level 2

A Raft cluster has 5 servers; the leader's log ends at index 8. The followers' match indexes are 5, 6, 3, 8. All entries come from the leader's current term. What is the highest committed index?

a) 8
b) 5
c) 3
d) 6

**Key: d**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 8, 5, 6, 3, 8 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 8, 8, 6, 5, 3. Step 3: the index 6 in position 3 is reached by 3 servers, and no higher index is. Result: 6. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 3. seed 3676960082496153800, level 1

A Raft cluster has 5 servers; the leader's log ends at index 6. The followers' match indexes are 2, 2, 3, 1. All entries come from the leader's current term. What is the highest committed index?

a) 6
b) 3
c) 2
d) 1

**Key: c**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 6, 2, 2, 3, 1 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 6, 3, 2, 2, 1. Step 3: the index 2 in position 3 is reached by 3 servers, and no higher index is. Result: 2. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 4. seed 2227855375396882707, level 1

A Raft cluster has 5 servers; the leader's log ends at index 7. The followers' match indexes are 4, 4, 3, 2. All entries come from the leader's current term. What is the highest committed index?

a) 7
b) 2
c) 3
d) 4

**Key: d**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 7, 4, 4, 3, 2 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 7, 4, 4, 3, 2. Step 3: the index 4 in position 3 is reached by 3 servers, and no higher index is. Result: 4. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 5. seed 414943919651242933, level 1

A Raft cluster has 5 servers; the leader's log ends at index 6. The followers' match indexes are 6, 1, 5, 2. All entries come from the leader's current term. What is the highest committed index?

a) 5
b) 2
c) 1
d) 6

**Key: a**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 6, 6, 1, 5, 2 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 6, 6, 5, 2, 1. Step 3: the index 5 in position 3 is reached by 3 servers, and no higher index is. Result: 5. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 6. seed 1841613716394117745, level 1

A Raft cluster has 5 servers; the leader's log ends at index 9. The followers' match indexes are 7, 9, 6, 2. All entries come from the leader's current term. What is the highest committed index?

a) 9
b) 7
c) 2
d) 6

**Key: b**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 9, 7, 9, 6, 2 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 9, 9, 7, 6, 2. Step 3: the index 7 in position 3 is reached by 3 servers, and no higher index is. Result: 7. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 7. seed 1842987721344266981, level 2

A Raft cluster has 7 servers; the leader's log ends at index 6. The followers' match indexes are 3, 6, 0, 4, 4, 5. All entries come from the leader's current term. What is the highest committed index?

a) 6
b) 4
c) 5
d) 0

**Key: b**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 6, 3, 6, 0, 4, 4, 5 with the leader's own index first. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: sorted from the highest, the indexes are 6, 6, 5, 4, 4, 3, 0. Step 3: the index 4 in position 4 is reached by 4 servers, and no higher index is. Result: 4. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 8. seed 3211329330997810218, level 2

A Raft cluster has 7 servers; the leader's log ends at index 7. The followers' match indexes are 7, 6, 6, 0, 1, 4. All entries come from the leader's current term. What is the highest committed index?

a) 7
b) 4
c) 6
d) 0

**Key: c**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 7, 7, 6, 6, 0, 1, 4 with the leader's own index first. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: sorted from the highest, the indexes are 7, 7, 6, 6, 4, 1, 0. Step 3: the index 6 in position 4 is reached by 4 servers, and no higher index is. Result: 6. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 9. seed 3368917494515018671, level 2

A Raft cluster has 5 servers; the leader's log ends at index 8. The followers' match indexes are 7, 1, 3, 4. All entries come from the leader's current term. What is the highest committed index?

a) 3
b) 1
c) 7
d) 4

**Key: d**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 8, 7, 1, 3, 4 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 8, 7, 4, 3, 1. Step 3: the index 4 in position 3 is reached by 3 servers, and no higher index is. Result: 4. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 10. seed 1324150135982236696, level 1

A Raft cluster has 5 servers; the leader's log ends at index 6. The followers' match indexes are 4, 3, 2, 5. All entries come from the leader's current term. What is the highest committed index?

a) 6
b) 2
c) 3
d) 4

**Key: d**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 6, 4, 3, 2, 5 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 6, 5, 4, 3, 2. Step 3: the index 4 in position 3 is reached by 3 servers, and no higher index is. Result: 4. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 11. seed 3140274578628408910, level 1

A Raft cluster has 5 servers; the leader's log ends at index 8. The followers' match indexes are 7, 5, 4, 6. All entries come from the leader's current term. What is the highest committed index?

a) 7
b) 5
c) 4
d) 6

**Key: d**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 8, 7, 5, 4, 6 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 8, 7, 6, 5, 4. Step 3: the index 6 in position 3 is reached by 3 servers, and no higher index is. Result: 6. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 12. seed 806412626011571779, level 2

A Raft cluster has 5 servers; the leader's log ends at index 8. The followers' match indexes are 3, 1, 3, 2. All entries come from the leader's current term. What is the highest committed index?

a) 3
b) 1
c) 8
d) 2

**Key: a**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 8, 3, 1, 3, 2 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 8, 3, 3, 2, 1. Step 3: the index 3 in position 3 is reached by 3 servers, and no higher index is. Result: 3. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 13. seed 4496202195882320467, level 2

A Raft cluster has 5 servers; the leader's log ends at index 8. The followers' match indexes are 4, 2, 1, 4. All entries come from the leader's current term. What is the highest committed index?

a) 2
b) 4
c) 8
d) 1

**Key: b**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 8, 4, 2, 1, 4 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 8, 4, 4, 2, 1. Step 3: the index 4 in position 3 is reached by 3 servers, and no higher index is. Result: 4. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 14. seed 3321525364792765407, level 2

A Raft cluster has 5 servers; the leader's log ends at index 6. The followers' match indexes are 0, 2, 5, 0. All entries come from the leader's current term. What is the highest committed index?

a) 5
b) 2
c) 6
d) 0

**Key: b**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 6, 0, 2, 5, 0 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 6, 5, 2, 0, 0. Step 3: the index 2 in position 3 is reached by 3 servers, and no higher index is. Result: 2. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 15. seed 615552123264851217, level 2

A Raft cluster has 7 servers; the leader's log ends at index 8. The followers' match indexes are 1, 1, 7, 4, 6, 6. All entries come from the leader's current term. What is the highest committed index?

a) 1
b) 4
c) 8
d) 6

**Key: d**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 8, 1, 1, 7, 4, 6, 6 with the leader's own index first. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: sorted from the highest, the indexes are 8, 7, 6, 6, 4, 1, 1. Step 3: the index 6 in position 4 is reached by 4 servers, and no higher index is. Result: 6. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 16. seed 1394391152806992016, level 2

A Raft cluster has 7 servers; the leader's log ends at index 9. The followers' match indexes are 8, 7, 8, 2, 2, 2. All entries come from the leader's current term. What is the highest committed index?

a) 9
b) 2
c) 8
d) 7

**Key: d**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 9, 8, 7, 8, 2, 2, 2 with the leader's own index first. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: sorted from the highest, the indexes are 9, 8, 8, 7, 2, 2, 2. Step 3: the index 7 in position 4 is reached by 4 servers, and no higher index is. Result: 7. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 17. seed 515813594353213153, level 2

A Raft cluster has 7 servers; the leader's log ends at index 8. The followers' match indexes are 6, 3, 3, 0, 6, 4. All entries come from the leader's current term. What is the highest committed index?

a) 6
b) 4
c) 8
d) 3

**Key: b**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 8, 6, 3, 3, 0, 6, 4 with the leader's own index first. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: sorted from the highest, the indexes are 8, 6, 6, 4, 3, 3, 0. Step 3: the index 4 in position 4 is reached by 4 servers, and no higher index is. Result: 4. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 18. seed 2945844420326236444, level 2

A Raft cluster has 5 servers; the leader's log ends at index 9. The followers' match indexes are 0, 8, 9, 7. All entries come from the leader's current term. What is the highest committed index?

a) 7
b) 9
c) 0
d) 8

**Key: d**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 9, 0, 8, 9, 7 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 9, 9, 8, 7, 0. Step 3: the index 8 in position 3 is reached by 3 servers, and no higher index is. Result: 8. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 19. seed 3902341124614788478, level 1

A Raft cluster has 5 servers; the leader's log ends at index 6. The followers' match indexes are 5, 2, 1, 2. All entries come from the leader's current term. What is the highest committed index?

a) 5
b) 1
c) 6
d) 2

**Key: d**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 6, 5, 2, 1, 2 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 6, 5, 2, 2, 1. Step 3: the index 2 in position 3 is reached by 3 servers, and no higher index is. Result: 2. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 20. seed 4323651099058069506, level 2

A Raft cluster has 7 servers; the leader's log ends at index 9. The followers' match indexes are 6, 0, 4, 7, 7, 6. All entries come from the leader's current term. What is the highest committed index?

a) 6
b) 7
c) 9
d) 0

**Key: a**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 9, 6, 0, 4, 7, 7, 6 with the leader's own index first. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: sorted from the highest, the indexes are 9, 7, 7, 6, 6, 4, 0. Step 3: the index 6 in position 4 is reached by 4 servers, and no higher index is. Result: 6. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 21. seed 3957278144446736466, level 2

A Raft cluster has 5 servers; the leader's log ends at index 9. The followers' match indexes are 6, 1, 9, 4. All entries come from the leader's current term. What is the highest committed index?

a) 4
b) 6
c) 9
d) 1

**Key: b**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 9, 6, 1, 9, 4 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 9, 9, 6, 4, 1. Step 3: the index 6 in position 3 is reached by 3 servers, and no higher index is. Result: 6. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 22. seed 1697506025488606765, level 1

A Raft cluster has 5 servers; the leader's log ends at index 6. The followers' match indexes are 5, 1, 3, 1. All entries come from the leader's current term. What is the highest committed index?

a) 3
b) 6
c) 5
d) 1

**Key: a**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 6, 5, 1, 3, 1 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 6, 5, 3, 1, 1. Step 3: the index 3 in position 3 is reached by 3 servers, and no higher index is. Result: 3. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 23. seed 997433994213169636, level 2

A Raft cluster has 5 servers; the leader's log ends at index 7. The followers' match indexes are 4, 3, 2, 6. All entries come from the leader's current term. What is the highest committed index?

a) 6
b) 7
c) 4
d) 2

**Key: c**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 7, 4, 3, 2, 6 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 7, 6, 4, 3, 2. Step 3: the index 4 in position 3 is reached by 3 servers, and no higher index is. Result: 4. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 24. seed 4165670021265106674, level 1

A Raft cluster has 5 servers; the leader's log ends at index 9. The followers' match indexes are 3, 5, 6, 3. All entries come from the leader's current term. What is the highest committed index?

a) 9
b) 3
c) 5
d) 6

**Key: c**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 9, 3, 5, 6, 3 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 9, 6, 5, 3, 3. Step 3: the index 5 in position 3 is reached by 3 servers, and no higher index is. Result: 5. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 25. seed 1214928083372393804, level 1

A Raft cluster has 5 servers; the leader's log ends at index 9. The followers' match indexes are 3, 1, 6, 2. All entries come from the leader's current term. What is the highest committed index?

a) 1
b) 3
c) 2
d) 9

**Key: b**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 9, 3, 1, 6, 2 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 9, 6, 3, 2, 1. Step 3: the index 3 in position 3 is reached by 3 servers, and no higher index is. Result: 3. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 26. seed 4211388568272920648, level 1

A Raft cluster has 5 servers; the leader's log ends at index 9. The followers' match indexes are 2, 7, 5, 9. All entries come from the leader's current term. What is the highest committed index?

a) 7
b) 5
c) 2
d) 9

**Key: a**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 9, 2, 7, 5, 9 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 9, 9, 7, 5, 2. Step 3: the index 7 in position 3 is reached by 3 servers, and no higher index is. Result: 7. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 27. seed 1749242026326979249, level 2

A Raft cluster has 7 servers; the leader's log ends at index 8. The followers' match indexes are 2, 7, 1, 7, 4, 5. All entries come from the leader's current term. What is the highest committed index?

a) 8
b) 1
c) 5
d) 7

**Key: c**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 8, 2, 7, 1, 7, 4, 5 with the leader's own index first. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: sorted from the highest, the indexes are 8, 7, 7, 5, 4, 2, 1. Step 3: the index 5 in position 4 is reached by 4 servers, and no higher index is. Result: 5. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 28. seed 2220449244610228706, level 1

A Raft cluster has 5 servers; the leader's log ends at index 6. The followers' match indexes are 1, 4, 2, 6. All entries come from the leader's current term. What is the highest committed index?

a) 1
b) 2
c) 4
d) 6

**Key: c**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 6, 1, 4, 2, 6 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 6, 6, 4, 2, 1. Step 3: the index 4 in position 3 is reached by 3 servers, and no higher index is. Result: 4. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 29. seed 3989999915794450501, level 2

A Raft cluster has 5 servers; the leader's log ends at index 8. The followers' match indexes are 3, 2, 0, 8. All entries come from the leader's current term. What is the highest committed index?

a) 0
b) 2
c) 3
d) 8

**Key: c**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 8, 3, 2, 0, 8 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 8, 8, 3, 2, 0. Step 3: the index 3 in position 3 is reached by 3 servers, and no higher index is. Result: 3. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 30. seed 2413416365945659073, level 1

A Raft cluster has 5 servers; the leader's log ends at index 7. The followers' match indexes are 6, 6, 1, 3. All entries come from the leader's current term. What is the highest committed index?

a) 3
b) 1
c) 6
d) 7

**Key: c**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 7, 6, 6, 1, 3 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 7, 6, 6, 3, 1. Step 3: the index 6 in position 3 is reached by 3 servers, and no higher index is. Result: 6. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 31. seed 188650843413221852, level 2

A Raft cluster has 7 servers; the leader's log ends at index 6. The followers' match indexes are 1, 3, 6, 0, 5, 0. All entries come from the leader's current term. What is the highest committed index?

a) 0
b) 5
c) 6
d) 3

**Key: d**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 6, 1, 3, 6, 0, 5, 0 with the leader's own index first. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: sorted from the highest, the indexes are 6, 6, 5, 3, 1, 0, 0. Step 3: the index 3 in position 4 is reached by 4 servers, and no higher index is. Result: 3. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 32. seed 2919356138518476330, level 1

A Raft cluster has 5 servers; the leader's log ends at index 9. The followers' match indexes are 7, 8, 3, 7. All entries come from the leader's current term. What is the highest committed index?

a) 8
b) 7
c) 9
d) 3

**Key: b**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 9, 7, 8, 3, 7 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 9, 8, 7, 7, 3. Step 3: the index 7 in position 3 is reached by 3 servers, and no higher index is. Result: 7. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 33. seed 349079909176526712, level 1

A Raft cluster has 5 servers; the leader's log ends at index 7. The followers' match indexes are 6, 1, 4, 7. All entries come from the leader's current term. What is the highest committed index?

a) 7
b) 6
c) 1
d) 4

**Key: b**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 7, 6, 1, 4, 7 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 7, 7, 6, 4, 1. Step 3: the index 6 in position 3 is reached by 3 servers, and no higher index is. Result: 6. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 34. seed 2416368592570135025, level 2

A Raft cluster has 7 servers; the leader's log ends at index 6. The followers' match indexes are 1, 2, 0, 1, 5, 4. All entries come from the leader's current term. What is the highest committed index?

a) 0
b) 2
c) 5
d) 1

**Key: b**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 6, 1, 2, 0, 1, 5, 4 with the leader's own index first. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: sorted from the highest, the indexes are 6, 5, 4, 2, 1, 1, 0. Step 3: the index 2 in position 4 is reached by 4 servers, and no higher index is. Result: 2. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 35. seed 3727288886280751902, level 2

A Raft cluster has 7 servers; the leader's log ends at index 8. The followers' match indexes are 8, 0, 4, 0, 2, 1. All entries come from the leader's current term. What is the highest committed index?

a) 2
b) 1
c) 0
d) 4

**Key: a**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 8, 8, 0, 4, 0, 2, 1 with the leader's own index first. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: sorted from the highest, the indexes are 8, 8, 4, 2, 1, 0, 0. Step 3: the index 2 in position 4 is reached by 4 servers, and no higher index is. Result: 2. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 36. seed 960140649684302745, level 2

A Raft cluster has 5 servers; the leader's log ends at index 8. The followers' match indexes are 0, 8, 3, 5. All entries come from the leader's current term. What is the highest committed index?

a) 3
b) 5
c) 0
d) 8

**Key: b**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 8, 0, 8, 3, 5 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 8, 8, 5, 3, 0. Step 3: the index 5 in position 3 is reached by 3 servers, and no higher index is. Result: 5. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 37. seed 1000591439270578787, level 2

A Raft cluster has 7 servers; the leader's log ends at index 6. The followers' match indexes are 3, 4, 2, 2, 6, 0. All entries come from the leader's current term. What is the highest committed index?

a) 6
b) 3
c) 0
d) 2

**Key: b**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 6, 3, 4, 2, 2, 6, 0 with the leader's own index first. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: sorted from the highest, the indexes are 6, 6, 4, 3, 2, 2, 0. Step 3: the index 3 in position 4 is reached by 4 servers, and no higher index is. Result: 3. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 38. seed 405818185598061419, level 2

A Raft cluster has 7 servers; the leader's log ends at index 6. The followers' match indexes are 1, 0, 0, 6, 4, 2. All entries come from the leader's current term. What is the highest committed index?

a) 1
b) 2
c) 4
d) 6

**Key: b**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 6, 1, 0, 0, 6, 4, 2 with the leader's own index first. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: sorted from the highest, the indexes are 6, 6, 4, 2, 1, 0, 0. Step 3: the index 2 in position 4 is reached by 4 servers, and no higher index is. Result: 2. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 39. seed 3682097401881445951, level 2

A Raft cluster has 5 servers; the leader's log ends at index 6. The followers' match indexes are 3, 3, 0, 1. All entries come from the leader's current term. What is the highest committed index?

a) 0
b) 6
c) 3
d) 1

**Key: c**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 6, 3, 3, 0, 1 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 6, 3, 3, 1, 0. Step 3: the index 3 in position 3 is reached by 3 servers, and no higher index is. Result: 3. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 40. seed 1323010796996617527, level 2

A Raft cluster has 7 servers; the leader's log ends at index 8. The followers' match indexes are 2, 5, 4, 1, 3, 6. All entries come from the leader's current term. What is the highest committed index?

a) 8
b) 5
c) 4
d) 1

**Key: c**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 8, 2, 5, 4, 1, 3, 6 with the leader's own index first. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: sorted from the highest, the indexes are 8, 6, 5, 4, 3, 2, 1. Step 3: the index 4 in position 4 is reached by 4 servers, and no higher index is. Result: 4. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 41. seed 3958775037892815793, level 1

A Raft cluster has 5 servers; the leader's log ends at index 9. The followers' match indexes are 2, 9, 8, 7. All entries come from the leader's current term. What is the highest committed index?

a) 2
b) 7
c) 9
d) 8

**Key: d**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 9, 2, 9, 8, 7 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 9, 9, 8, 7, 2. Step 3: the index 8 in position 3 is reached by 3 servers, and no higher index is. Result: 8. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 42. seed 3162118399843419611, level 1

A Raft cluster has 5 servers; the leader's log ends at index 8. The followers' match indexes are 3, 5, 8, 2. All entries come from the leader's current term. What is the highest committed index?

a) 5
b) 3
c) 2
d) 8

**Key: a**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 8, 3, 5, 8, 2 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 8, 8, 5, 3, 2. Step 3: the index 5 in position 3 is reached by 3 servers, and no higher index is. Result: 5. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 43. seed 3812814935020102031, level 2

A Raft cluster has 5 servers; the leader's log ends at index 7. The followers' match indexes are 7, 1, 0, 4. All entries come from the leader's current term. What is the highest committed index?

a) 7
b) 0
c) 1
d) 4

**Key: d**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 7, 7, 1, 0, 4 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 7, 7, 4, 1, 0. Step 3: the index 4 in position 3 is reached by 3 servers, and no higher index is. Result: 4. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 44. seed 1714188960155458461, level 2

A Raft cluster has 5 servers; the leader's log ends at index 7. The followers' match indexes are 3, 4, 0, 1. All entries come from the leader's current term. What is the highest committed index?

a) 4
b) 0
c) 3
d) 7

**Key: c**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 7, 3, 4, 0, 1 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 7, 4, 3, 1, 0. Step 3: the index 3 in position 3 is reached by 3 servers, and no higher index is. Result: 3. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 45. seed 1554967366029023131, level 2

A Raft cluster has 7 servers; the leader's log ends at index 7. The followers' match indexes are 5, 4, 0, 2, 1, 2. All entries come from the leader's current term. What is the highest committed index?

a) 0
b) 5
c) 4
d) 2

**Key: d**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 7, 5, 4, 0, 2, 1, 2 with the leader's own index first. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: sorted from the highest, the indexes are 7, 5, 4, 2, 2, 1, 0. Step 3: the index 2 in position 4 is reached by 4 servers, and no higher index is. Result: 2. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 46. seed 3432468065673599433, level 2

A Raft cluster has 7 servers; the leader's log ends at index 6. The followers' match indexes are 2, 6, 4, 2, 0, 6. All entries come from the leader's current term. What is the highest committed index?

a) 2
b) 6
c) 0
d) 4

**Key: d**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 6, 2, 6, 4, 2, 0, 6 with the leader's own index first. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: sorted from the highest, the indexes are 6, 6, 6, 4, 2, 2, 0. Step 3: the index 4 in position 4 is reached by 4 servers, and no higher index is. Result: 4. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 47. seed 1120433747250864517, level 1

A Raft cluster has 5 servers; the leader's log ends at index 9. The followers' match indexes are 3, 8, 3, 5. All entries come from the leader's current term. What is the highest committed index?

a) 9
b) 5
c) 3
d) 8

**Key: b**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 9, 3, 8, 3, 5 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 9, 8, 5, 3, 3. Step 3: the index 5 in position 3 is reached by 3 servers, and no higher index is. Result: 5. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 48. seed 3273350112377305750, level 1

A Raft cluster has 5 servers; the leader's log ends at index 9. The followers' match indexes are 1, 9, 8, 5. All entries come from the leader's current term. What is the highest committed index?

a) 8
b) 1
c) 5
d) 9

**Key: a**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 9, 1, 9, 8, 5 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 9, 9, 8, 5, 1. Step 3: the index 8 in position 3 is reached by 3 servers, and no higher index is. Result: 8. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 49. seed 2382277185016212032, level 2

A Raft cluster has 7 servers; the leader's log ends at index 7. The followers' match indexes are 4, 7, 0, 2, 5, 2. All entries come from the leader's current term. What is the highest committed index?

a) 2
b) 0
c) 4
d) 7

**Key: c**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 7, 4, 7, 0, 2, 5, 2 with the leader's own index first. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: sorted from the highest, the indexes are 7, 7, 5, 4, 2, 2, 0. Step 3: the index 4 in position 4 is reached by 4 servers, and no higher index is. Result: 4. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.

## 50. seed 442546823939931527, level 1

A Raft cluster has 5 servers; the leader's log ends at index 6. The followers' match indexes are 5, 3, 6, 4. All entries come from the leader's current term. What is the highest committed index?

a) 3
b) 6
c) 4
d) 5

**Key: d**

Explanation: Rule: an entry is committed once it is on a majority of the servers, and a server with match index k holds entries 1 to k. Inputs: match indexes 6, 5, 3, 6, 4 with the leader's own index first. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: sorted from the highest, the indexes are 6, 6, 5, 4, 3. Step 3: the index 5 in position 3 is reached by 3 servers, and no higher index is. Result: 5. Source: `paper-raft-dissertation#p36`; `paper-raft-dissertation#p32`.
