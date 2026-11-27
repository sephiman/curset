# Raft election votes (`raft-election-votes`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 367085866493377524, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 1, 2 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate C need to become leader?

a) 3
b) 6
c) 4
d) 2

**Key: a**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 1, 2 and 1. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate C holds 1. Step 3: 4 - 1 = 3. Result: 3 more votes. Source: `paper-raft-dissertation#p34`.

## 2. seed 1379092589435277823, level 1

A Raft cluster has 5 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate C need to become leader?

a) 3
b) 4
c) 2
d) 1

**Key: c**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 5 servers, votes 1, 1 and 1. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: candidate C holds 1. Step 3: 3 - 1 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 3. seed 4499321737922515861, level 1

A Raft cluster has 5 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate B need to become leader?

a) 3
b) 4
c) 2
d) 1

**Key: c**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 5 servers, votes 1, 1 and 1. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: candidate B holds 1. Step 3: 3 - 1 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 4. seed 4610188838628644261, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate C need to become leader?

a) 6
b) 1
c) 3
d) 2

**Key: c**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 1, 1 and 1. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate C holds 1. Step 3: 4 - 1 = 3. Result: 3 more votes. Source: `paper-raft-dissertation#p34`.

## 5. seed 1015715482356270046, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 2, 2 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 3
b) 1
c) 2
d) 5

**Key: c**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 2, 2 and 1. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate A holds 2. Step 3: 4 - 2 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 6. seed 3243865402583091861, level 1

A Raft cluster has 9 servers. Candidates A, B and C hold 3, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 6
b) 2
c) 5
d) 1

**Key: b**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 9 servers, votes 3, 1 and 1. Step 1: the majority of 9 servers is 9 // 2 + 1 = 5. Step 2: candidate A holds 3. Step 3: 5 - 3 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 7. seed 2229461854146173495, level 1

A Raft cluster has 5 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate C need to become leader?

a) 2
b) 1
c) 4
d) 3

**Key: a**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 5 servers, votes 1, 1 and 1. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: candidate C holds 1. Step 3: 3 - 1 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 8. seed 3032524065088390906, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 2, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate B need to become leader?

a) 3
b) 4
c) 6
d) 2

**Key: a**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 2, 1 and 1. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate B holds 1. Step 3: 4 - 1 = 3. Result: 3 more votes. Source: `paper-raft-dissertation#p34`.

## 9. seed 3491542532052755334, level 1

A Raft cluster has 9 servers. Candidates A, B and C hold 1, 1 and 2 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 2
b) 8
c) 4
d) 3

**Key: c**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 9 servers, votes 1, 1 and 2. Step 1: the majority of 9 servers is 9 // 2 + 1 = 5. Step 2: candidate A holds 1. Step 3: 5 - 1 = 4. Result: 4 more votes. Source: `paper-raft-dissertation#p34`.

## 10. seed 1408841144558288331, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate B need to become leader?

a) 3
b) 2
c) 6
d) 1

**Key: a**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 1, 1 and 1. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate B holds 1. Step 3: 4 - 1 = 3. Result: 3 more votes. Source: `paper-raft-dissertation#p34`.

## 11. seed 3527790163820219884, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 1, 1 and 2 votes in one term, their own included; the other servers have not voted. How many more votes does candidate C need to become leader?

a) 3
b) 2
c) 4
d) 1

**Key: b**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 1, 1 and 2. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate C holds 2. Step 3: 4 - 2 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 12. seed 4453575944233024255, level 1

A Raft cluster has 9 servers. Candidates A, B and C hold 1, 1 and 2 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 3
b) 4
c) 5
d) 8

**Key: b**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 9 servers, votes 1, 1 and 2. Step 1: the majority of 9 servers is 9 // 2 + 1 = 5. Step 2: candidate A holds 1. Step 3: 5 - 1 = 4. Result: 4 more votes. Source: `paper-raft-dissertation#p34`.

## 13. seed 1434662661715567586, level 1

A Raft cluster has 5 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 4
b) 1
c) 3
d) 2

**Key: d**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 5 servers, votes 1, 1 and 1. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: candidate A holds 1. Step 3: 3 - 1 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 14. seed 466267441753371918, level 1

A Raft cluster has 9 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 8
b) 1
c) 4
d) 3

**Key: c**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 9 servers, votes 1, 1 and 1. Step 1: the majority of 9 servers is 9 // 2 + 1 = 5. Step 2: candidate A holds 1. Step 3: 5 - 1 = 4. Result: 4 more votes. Source: `paper-raft-dissertation#p34`.

## 15. seed 1464274689864674708, level 1

A Raft cluster has 9 servers. Candidates A, B and C hold 2, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 7
b) 1
c) 3
d) 5

**Key: c**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 9 servers, votes 2, 1 and 1. Step 1: the majority of 9 servers is 9 // 2 + 1 = 5. Step 2: candidate A holds 2. Step 3: 5 - 2 = 3. Result: 3 more votes. Source: `paper-raft-dissertation#p34`.

## 16. seed 2945151716044606637, level 1

A Raft cluster has 5 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 4
b) 2
c) 3
d) 1

**Key: b**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 5 servers, votes 1, 1 and 1. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: candidate A holds 1. Step 3: 3 - 1 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 17. seed 1619753438093843459, level 1

A Raft cluster has 9 servers. Candidates A, B and C hold 1, 3 and 3 votes in one term, their own included; the other servers have not voted. How many more votes does candidate C need to become leader?

a) 1
b) 2
c) 5
d) 3

**Key: b**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 9 servers, votes 1, 3 and 3. Step 1: the majority of 9 servers is 9 // 2 + 1 = 5. Step 2: candidate C holds 3. Step 3: 5 - 3 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 18. seed 3606612937359446680, level 1

A Raft cluster has 9 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate B need to become leader?

a) 3
b) 1
c) 8
d) 4

**Key: d**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 9 servers, votes 1, 1 and 1. Step 1: the majority of 9 servers is 9 // 2 + 1 = 5. Step 2: candidate B holds 1. Step 3: 5 - 1 = 4. Result: 4 more votes. Source: `paper-raft-dissertation#p34`.

## 19. seed 823683690389108890, level 1

A Raft cluster has 5 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate C need to become leader?

a) 2
b) 3
c) 4
d) 1

**Key: a**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 5 servers, votes 1, 1 and 1. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: candidate C holds 1. Step 3: 3 - 1 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 20. seed 1435523962784574983, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 1, 2 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate C need to become leader?

a) 4
b) 3
c) 2
d) 6

**Key: b**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 1, 2 and 1. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate C holds 1. Step 3: 4 - 1 = 3. Result: 3 more votes. Source: `paper-raft-dissertation#p34`.

## 21. seed 4160885875688719563, level 1

A Raft cluster has 9 servers. Candidates A, B and C hold 1, 2 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 5
b) 2
c) 4
d) 8

**Key: c**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 9 servers, votes 1, 2 and 1. Step 1: the majority of 9 servers is 9 // 2 + 1 = 5. Step 2: candidate A holds 1. Step 3: 5 - 1 = 4. Result: 4 more votes. Source: `paper-raft-dissertation#p34`.

## 22. seed 1446262407627222053, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 2, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 5
b) 1
c) 3
d) 2

**Key: d**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 2, 1 and 1. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate A holds 2. Step 3: 4 - 2 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 23. seed 2181335996204827929, level 1

A Raft cluster has 9 servers. Candidates A, B and C hold 1, 1 and 3 votes in one term, their own included; the other servers have not voted. How many more votes does candidate B need to become leader?

a) 5
b) 4
c) 8
d) 3

**Key: b**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 9 servers, votes 1, 1 and 3. Step 1: the majority of 9 servers is 9 // 2 + 1 = 5. Step 2: candidate B holds 1. Step 3: 5 - 1 = 4. Result: 4 more votes. Source: `paper-raft-dissertation#p34`.

## 24. seed 254834407386739030, level 1

A Raft cluster has 9 servers. Candidates A, B and C hold 1, 1 and 2 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 3
b) 4
c) 2
d) 8

**Key: b**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 9 servers, votes 1, 1 and 2. Step 1: the majority of 9 servers is 9 // 2 + 1 = 5. Step 2: candidate A holds 1. Step 3: 5 - 1 = 4. Result: 4 more votes. Source: `paper-raft-dissertation#p34`.

## 25. seed 2743777283313821288, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 2, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 3
b) 2
c) 1
d) 4

**Key: b**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 2, 1 and 1. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate A holds 2. Step 3: 4 - 2 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 26. seed 2362901841642756724, level 1

A Raft cluster has 9 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 4
b) 1
c) 8
d) 5

**Key: a**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 9 servers, votes 1, 1 and 1. Step 1: the majority of 9 servers is 9 // 2 + 1 = 5. Step 2: candidate A holds 1. Step 3: 5 - 1 = 4. Result: 4 more votes. Source: `paper-raft-dissertation#p34`.

## 27. seed 2028966706052808035, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 2, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 4
b) 2
c) 5
d) 1

**Key: b**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 2, 1 and 1. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate A holds 2. Step 3: 4 - 2 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 28. seed 1563024620747129881, level 1

A Raft cluster has 9 servers. Candidates A, B and C hold 2, 3 and 2 votes in one term, their own included; the other servers have not voted. How many more votes does candidate B need to become leader?

a) 6
b) 1
c) 2
d) 3

**Key: c**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 9 servers, votes 2, 3 and 2. Step 1: the majority of 9 servers is 9 // 2 + 1 = 5. Step 2: candidate B holds 3. Step 3: 5 - 3 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 29. seed 3512800951420959675, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 2, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate B need to become leader?

a) 3
b) 6
c) 4
d) 2

**Key: a**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 2, 1 and 1. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate B holds 1. Step 3: 4 - 1 = 3. Result: 3 more votes. Source: `paper-raft-dissertation#p34`.

## 30. seed 1425984243412556066, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate C need to become leader?

a) 4
b) 3
c) 2
d) 1

**Key: b**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 1, 1 and 1. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate C holds 1. Step 3: 4 - 1 = 3. Result: 3 more votes. Source: `paper-raft-dissertation#p34`.

## 31. seed 4076875103216751310, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate C need to become leader?

a) 3
b) 2
c) 4
d) 1

**Key: a**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 1, 1 and 1. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate C holds 1. Step 3: 4 - 1 = 3. Result: 3 more votes. Source: `paper-raft-dissertation#p34`.

## 32. seed 1361226649871216872, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 6
b) 1
c) 3
d) 2

**Key: c**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 1, 1 and 1. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate A holds 1. Step 3: 4 - 1 = 3. Result: 3 more votes. Source: `paper-raft-dissertation#p34`.

## 33. seed 4520308144875419189, level 1

A Raft cluster has 9 servers. Candidates A, B and C hold 1, 1 and 3 votes in one term, their own included; the other servers have not voted. How many more votes does candidate B need to become leader?

a) 4
b) 2
c) 3
d) 5

**Key: a**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 9 servers, votes 1, 1 and 3. Step 1: the majority of 9 servers is 9 // 2 + 1 = 5. Step 2: candidate B holds 1. Step 3: 5 - 1 = 4. Result: 4 more votes. Source: `paper-raft-dissertation#p34`.

## 34. seed 1857533054378051227, level 1

A Raft cluster has 9 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate C need to become leader?

a) 3
b) 1
c) 4
d) 5

**Key: c**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 9 servers, votes 1, 1 and 1. Step 1: the majority of 9 servers is 9 // 2 + 1 = 5. Step 2: candidate C holds 1. Step 3: 5 - 1 = 4. Result: 4 more votes. Source: `paper-raft-dissertation#p34`.

## 35. seed 779817915911971698, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 2
b) 6
c) 3
d) 4

**Key: c**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 1, 1 and 1. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate A holds 1. Step 3: 4 - 1 = 3. Result: 3 more votes. Source: `paper-raft-dissertation#p34`.

## 36. seed 3309943797565909905, level 1

A Raft cluster has 5 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 1
b) 2
c) 3
d) 4

**Key: b**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 5 servers, votes 1, 1 and 1. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: candidate A holds 1. Step 3: 3 - 1 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 37. seed 1110612740480265059, level 1

A Raft cluster has 5 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate C need to become leader?

a) 3
b) 1
c) 2
d) 4

**Key: c**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 5 servers, votes 1, 1 and 1. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: candidate C holds 1. Step 3: 3 - 1 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 38. seed 3874894670623653104, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 1, 1 and 2 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 4
b) 2
c) 3
d) 6

**Key: c**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 1, 1 and 2. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate A holds 1. Step 3: 4 - 1 = 3. Result: 3 more votes. Source: `paper-raft-dissertation#p34`.

## 39. seed 1435671842085139868, level 1

A Raft cluster has 9 servers. Candidates A, B and C hold 2, 2 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 2
b) 5
c) 3
d) 7

**Key: c**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 9 servers, votes 2, 2 and 1. Step 1: the majority of 9 servers is 9 // 2 + 1 = 5. Step 2: candidate A holds 2. Step 3: 5 - 2 = 3. Result: 3 more votes. Source: `paper-raft-dissertation#p34`.

## 40. seed 4146606900292872692, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 1, 2 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate B need to become leader?

a) 2
b) 4
c) 5
d) 3

**Key: a**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 1, 2 and 1. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate B holds 2. Step 3: 4 - 2 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 41. seed 1583177681534122697, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate B need to become leader?

a) 1
b) 4
c) 2
d) 3

**Key: d**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 1, 1 and 1. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate B holds 1. Step 3: 4 - 1 = 3. Result: 3 more votes. Source: `paper-raft-dissertation#p34`.

## 42. seed 3788503881254978063, level 1

A Raft cluster has 9 servers. Candidates A, B and C hold 1, 1 and 2 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 8
b) 3
c) 5
d) 4

**Key: d**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 9 servers, votes 1, 1 and 2. Step 1: the majority of 9 servers is 9 // 2 + 1 = 5. Step 2: candidate A holds 1. Step 3: 5 - 1 = 4. Result: 4 more votes. Source: `paper-raft-dissertation#p34`.

## 43. seed 3090021777120725590, level 1

A Raft cluster has 5 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 3
b) 1
c) 4
d) 2

**Key: d**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 5 servers, votes 1, 1 and 1. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: candidate A holds 1. Step 3: 3 - 1 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 44. seed 1725452827882433970, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate B need to become leader?

a) 3
b) 2
c) 1
d) 6

**Key: a**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 1, 1 and 1. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate B holds 1. Step 3: 4 - 1 = 3. Result: 3 more votes. Source: `paper-raft-dissertation#p34`.

## 45. seed 3455670161351330759, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate B need to become leader?

a) 2
b) 3
c) 6
d) 1

**Key: b**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 1, 1 and 1. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate B holds 1. Step 3: 4 - 1 = 3. Result: 3 more votes. Source: `paper-raft-dissertation#p34`.

## 46. seed 3700108684578671935, level 1

A Raft cluster has 5 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 1
b) 3
c) 4
d) 2

**Key: d**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 5 servers, votes 1, 1 and 1. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: candidate A holds 1. Step 3: 3 - 1 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 47. seed 942909380472676749, level 1

A Raft cluster has 7 servers. Candidates A, B and C hold 1, 2 and 2 votes in one term, their own included; the other servers have not voted. How many more votes does candidate B need to become leader?

a) 2
b) 5
c) 1
d) 4

**Key: a**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 7 servers, votes 1, 2 and 2. Step 1: the majority of 7 servers is 7 // 2 + 1 = 4. Step 2: candidate B holds 2. Step 3: 4 - 2 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 48. seed 4181302728499262274, level 1

A Raft cluster has 5 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate C need to become leader?

a) 3
b) 4
c) 1
d) 2

**Key: d**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 5 servers, votes 1, 1 and 1. Step 1: the majority of 5 servers is 5 // 2 + 1 = 3. Step 2: candidate C holds 1. Step 3: 3 - 1 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.

## 49. seed 200128227580636275, level 1

A Raft cluster has 9 servers. Candidates A, B and C hold 1, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 4
b) 1
c) 8
d) 5

**Key: a**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 9 servers, votes 1, 1 and 1. Step 1: the majority of 9 servers is 9 // 2 + 1 = 5. Step 2: candidate A holds 1. Step 3: 5 - 1 = 4. Result: 4 more votes. Source: `paper-raft-dissertation#p34`.

## 50. seed 1751184059208308049, level 1

A Raft cluster has 9 servers. Candidates A, B and C hold 3, 1 and 1 votes in one term, their own included; the other servers have not voted. How many more votes does candidate A need to become leader?

a) 2
b) 6
c) 5
d) 1

**Key: a**

Explanation: Rule: a candidate wins a term only with votes from a majority of the servers in the full cluster, and each server votes for at most one candidate per term. Inputs: 9 servers, votes 3, 1 and 1. Step 1: the majority of 9 servers is 9 // 2 + 1 = 5. Step 2: candidate A holds 3. Step 3: 5 - 3 = 2. Result: 2 more votes. Source: `paper-raft-dissertation#p34`.
