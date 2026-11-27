# Sets after a sequence of unions (`union-find-sets`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 2605412371187508524, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(6,5)`, `union(2,3)`, `union(6,0)`, `union(3,2)`. How many sets remain?

a) 5
b) 7
c) 4
d) 3

**Key: c**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(6,5)` leaves 6 sets, largest 2; 2. `union(2,3)` leaves 5 sets, largest 2; 3. `union(6,0)` leaves 4 sets, largest 3; 4. `union(3,2)` (already in one set, nothing changes) leaves 4 sets, largest 3. Result: 4. Source: `erickson-union-find#p1`.

## 2. seed 4288896232929532495, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(5,6)`, `union(7,1)`, `union(7,1)`, `union(5,4)`, `union(0,6)`. What size is the largest set?

a) 6
b) 4
c) 2
d) 3

**Key: b**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(5,6)` leaves 7 sets, largest 2; 2. `union(7,1)` leaves 6 sets, largest 2; 3. `union(7,1)` (already in one set, nothing changes) leaves 6 sets, largest 2; 4. `union(5,4)` leaves 5 sets, largest 3; 5. `union(0,6)` leaves 4 sets, largest 4. Result: 4. Source: `erickson-union-find#p1`.

## 3. seed 409273977250556998, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(2,6)`, `union(5,1)`, `union(2,1)`, `union(7,2)`, `union(5,1)`, `union(1,0)`, `union(4,1)`. What size is the largest set?

a) 7
b) 3
c) 8
d) 6

**Key: a**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(2,6)` leaves 7 sets, largest 2; 2. `union(5,1)` leaves 6 sets, largest 2; 3. `union(2,1)` leaves 5 sets, largest 4; 4. `union(7,2)` leaves 4 sets, largest 5; 5. `union(5,1)` (already in one set, nothing changes) leaves 4 sets, largest 5; 6. `union(1,0)` leaves 3 sets, largest 6; 7. `union(4,1)` leaves 2 sets, largest 7. Result: 7. Source: `erickson-union-find#p1`.

## 4. seed 4450133611011382218, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(2,4)`, `union(1,6)`, `union(4,6)`, `union(4,6)`. How many sets remain?

a) 4
b) 3
c) 7
d) 5

**Key: a**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(2,4)` leaves 6 sets, largest 2; 2. `union(1,6)` leaves 5 sets, largest 2; 3. `union(4,6)` leaves 4 sets, largest 4; 4. `union(4,6)` (already in one set, nothing changes) leaves 4 sets, largest 4. Result: 4. Source: `erickson-union-find#p1`.

## 5. seed 1873158486034364262, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(3,5)`, `union(0,3)`, `union(2,3)`, `union(5,1)`, `union(1,0)`. How many sets remain?

a) 5
b) 3
c) 4
d) 7

**Key: b**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(3,5)` leaves 6 sets, largest 2; 2. `union(0,3)` leaves 5 sets, largest 3; 3. `union(2,3)` leaves 4 sets, largest 4; 4. `union(5,1)` leaves 3 sets, largest 5; 5. `union(1,0)` (already in one set, nothing changes) leaves 3 sets, largest 5. Result: 3. Source: `erickson-union-find#p1`.

## 6. seed 1248778207739632355, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(6,5)`, `union(2,1)`, `union(2,1)`, `union(3,1)`, `union(5,1)`. How many sets remain?

a) 4
b) 5
c) 3
d) 2

**Key: c**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(6,5)` leaves 6 sets, largest 2; 2. `union(2,1)` leaves 5 sets, largest 2; 3. `union(2,1)` (already in one set, nothing changes) leaves 5 sets, largest 2; 4. `union(3,1)` leaves 4 sets, largest 3; 5. `union(5,1)` leaves 3 sets, largest 5. Result: 3. Source: `erickson-union-find#p1`.

## 7. seed 97522676817364345, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(5,3)`, `union(2,6)`, `union(6,2)`, `union(1,2)`, `union(0,2)`, `union(4,0)`. How many sets remain?

a) 5
b) 3
c) 7
d) 2

**Key: d**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(5,3)` leaves 6 sets, largest 2; 2. `union(2,6)` leaves 5 sets, largest 2; 3. `union(6,2)` (already in one set, nothing changes) leaves 5 sets, largest 2; 4. `union(1,2)` leaves 4 sets, largest 3; 5. `union(0,2)` leaves 3 sets, largest 4; 6. `union(4,0)` leaves 2 sets, largest 5. Result: 2. Source: `erickson-union-find#p1`.

## 8. seed 1480111059076743654, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(2,1)`, `union(3,2)`, `union(3,6)`, `union(4,1)`, `union(5,0)`, `union(7,1)`, `union(6,1)`. What size is the largest set?

a) 4
b) 8
c) 6
d) 2

**Key: c**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(2,1)` leaves 7 sets, largest 2; 2. `union(3,2)` leaves 6 sets, largest 3; 3. `union(3,6)` leaves 5 sets, largest 4; 4. `union(4,1)` leaves 4 sets, largest 5; 5. `union(5,0)` leaves 3 sets, largest 5; 6. `union(7,1)` leaves 2 sets, largest 6; 7. `union(6,1)` (already in one set, nothing changes) leaves 2 sets, largest 6. Result: 6. Source: `erickson-union-find#p1`.

## 9. seed 4443129612918256344, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(6,1)`, `union(3,6)`, `union(5,2)`, `union(2,0)`, `union(6,0)`. How many sets remain?

a) 3
b) 4
c) 2
d) 6

**Key: c**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(6,1)` leaves 6 sets, largest 2; 2. `union(3,6)` leaves 5 sets, largest 3; 3. `union(5,2)` leaves 4 sets, largest 3; 4. `union(2,0)` leaves 3 sets, largest 3; 5. `union(6,0)` leaves 2 sets, largest 6. Result: 2. Source: `erickson-union-find#p1`.

## 10. seed 3024709873896757077, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(6,1)`, `union(3,6)`, `union(6,4)`, `union(1,4)`. How many sets remain?

a) 4
b) 7
c) 5
d) 3

**Key: a**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(6,1)` leaves 6 sets, largest 2; 2. `union(3,6)` leaves 5 sets, largest 3; 3. `union(6,4)` leaves 4 sets, largest 4; 4. `union(1,4)` (already in one set, nothing changes) leaves 4 sets, largest 4. Result: 4. Source: `erickson-union-find#p1`.

## 11. seed 595371514309979246, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(0,3)`, `union(7,6)`, `union(4,5)`, `union(3,7)`, `union(2,0)`, `union(2,5)`. What size is the largest set?

a) 7
b) 3
c) 5
d) 4

**Key: a**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(0,3)` leaves 7 sets, largest 2; 2. `union(7,6)` leaves 6 sets, largest 2; 3. `union(4,5)` leaves 5 sets, largest 2; 4. `union(3,7)` leaves 4 sets, largest 4; 5. `union(2,0)` leaves 3 sets, largest 5; 6. `union(2,5)` leaves 2 sets, largest 7. Result: 7. Source: `erickson-union-find#p1`.

## 12. seed 4429470442611207849, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(0,3)`, `union(3,5)`, `union(5,0)`, `union(5,6)`, `union(4,5)`, `union(5,2)`. How many sets remain?

a) 3
b) 1
c) 6
d) 2

**Key: d**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(0,3)` leaves 6 sets, largest 2; 2. `union(3,5)` leaves 5 sets, largest 3; 3. `union(5,0)` (already in one set, nothing changes) leaves 5 sets, largest 3; 4. `union(5,6)` leaves 4 sets, largest 4; 5. `union(4,5)` leaves 3 sets, largest 5; 6. `union(5,2)` leaves 2 sets, largest 6. Result: 2. Source: `erickson-union-find#p1`.

## 13. seed 1837865429534899691, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(6,1)`, `union(7,4)`, `union(2,3)`, `union(0,6)`, `union(2,3)`, `union(6,3)`. What size is the largest set?

a) 3
b) 4
c) 5
d) 7

**Key: c**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(6,1)` leaves 7 sets, largest 2; 2. `union(7,4)` leaves 6 sets, largest 2; 3. `union(2,3)` leaves 5 sets, largest 2; 4. `union(0,6)` leaves 4 sets, largest 3; 5. `union(2,3)` (already in one set, nothing changes) leaves 4 sets, largest 3; 6. `union(6,3)` leaves 3 sets, largest 5. Result: 5. Source: `erickson-union-find#p1`.

## 14. seed 1024881300647171671, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(5,3)`, `union(0,4)`, `union(4,6)`, `union(0,6)`. How many sets remain?

a) 7
b) 3
c) 5
d) 4

**Key: d**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(5,3)` leaves 6 sets, largest 2; 2. `union(0,4)` leaves 5 sets, largest 2; 3. `union(4,6)` leaves 4 sets, largest 3; 4. `union(0,6)` (already in one set, nothing changes) leaves 4 sets, largest 3. Result: 4. Source: `erickson-union-find#p1`.

## 15. seed 3716809073527242754, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(5,3)`, `union(7,4)`, `union(3,5)`, `union(3,4)`, `union(5,2)`. What size is the largest set?

a) 3
b) 5
c) 6
d) 4

**Key: b**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(5,3)` leaves 7 sets, largest 2; 2. `union(7,4)` leaves 6 sets, largest 2; 3. `union(3,5)` (already in one set, nothing changes) leaves 6 sets, largest 2; 4. `union(3,4)` leaves 5 sets, largest 4; 5. `union(5,2)` leaves 4 sets, largest 5. Result: 5. Source: `erickson-union-find#p1`.

## 16. seed 1331212707446298189, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(0,6)`, `union(1,2)`, `union(6,0)`, `union(2,7)`, `union(5,6)`, `union(5,1)`, `union(6,0)`. What size is the largest set?

a) 8
b) 3
c) 4
d) 6

**Key: d**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(0,6)` leaves 7 sets, largest 2; 2. `union(1,2)` leaves 6 sets, largest 2; 3. `union(6,0)` (already in one set, nothing changes) leaves 6 sets, largest 2; 4. `union(2,7)` leaves 5 sets, largest 3; 5. `union(5,6)` leaves 4 sets, largest 3; 6. `union(5,1)` leaves 3 sets, largest 6; 7. `union(6,0)` (already in one set, nothing changes) leaves 3 sets, largest 6. Result: 6. Source: `erickson-union-find#p1`.

## 17. seed 3860342126299859465, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(1,5)`, `union(3,4)`, `union(0,2)`, `union(1,0)`, `union(4,0)`. How many sets remain?

a) 6
b) 3
c) 2
d) 4

**Key: c**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(1,5)` leaves 6 sets, largest 2; 2. `union(3,4)` leaves 5 sets, largest 2; 3. `union(0,2)` leaves 4 sets, largest 2; 4. `union(1,0)` leaves 3 sets, largest 4; 5. `union(4,0)` leaves 2 sets, largest 6. Result: 2. Source: `erickson-union-find#p1`.

## 18. seed 3595148438992950758, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(1,3)`, `union(7,4)`, `union(3,4)`, `union(5,4)`, `union(3,6)`, `union(7,4)`. What size is the largest set?

a) 5
b) 3
c) 6
d) 7

**Key: c**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(1,3)` leaves 7 sets, largest 2; 2. `union(7,4)` leaves 6 sets, largest 2; 3. `union(3,4)` leaves 5 sets, largest 4; 4. `union(5,4)` leaves 4 sets, largest 5; 5. `union(3,6)` leaves 3 sets, largest 6; 6. `union(7,4)` (already in one set, nothing changes) leaves 3 sets, largest 6. Result: 6. Source: `erickson-union-find#p1`.

## 19. seed 3519349308931087461, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(1,2)`, `union(5,3)`, `union(2,0)`, `union(1,5)`, `union(7,3)`. What size is the largest set?

a) 4
b) 5
c) 6
d) 3

**Key: c**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(1,2)` leaves 7 sets, largest 2; 2. `union(5,3)` leaves 6 sets, largest 2; 3. `union(2,0)` leaves 5 sets, largest 3; 4. `union(1,5)` leaves 4 sets, largest 5; 5. `union(7,3)` leaves 3 sets, largest 6. Result: 6. Source: `erickson-union-find#p1`.

## 20. seed 1233879053296190202, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(5,0)`, `union(6,0)`, `union(2,4)`, `union(0,1)`, `union(3,1)`, `union(5,2)`. What size is the largest set?

a) 3
b) 5
c) 7
d) 4

**Key: c**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(5,0)` leaves 7 sets, largest 2; 2. `union(6,0)` leaves 6 sets, largest 3; 3. `union(2,4)` leaves 5 sets, largest 3; 4. `union(0,1)` leaves 4 sets, largest 4; 5. `union(3,1)` leaves 3 sets, largest 5; 6. `union(5,2)` leaves 2 sets, largest 7. Result: 7. Source: `erickson-union-find#p1`.

## 21. seed 4478579032434050298, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(0,4)`, `union(5,3)`, `union(1,4)`, `union(2,0)`, `union(1,4)`, `union(3,5)`. How many sets remain?

a) 4
b) 7
c) 6
d) 3

**Key: d**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(0,4)` leaves 6 sets, largest 2; 2. `union(5,3)` leaves 5 sets, largest 2; 3. `union(1,4)` leaves 4 sets, largest 3; 4. `union(2,0)` leaves 3 sets, largest 4; 5. `union(1,4)` (already in one set, nothing changes) leaves 3 sets, largest 4; 6. `union(3,5)` (already in one set, nothing changes) leaves 3 sets, largest 4. Result: 3. Source: `erickson-union-find#p1`.

## 22. seed 1431246409563566855, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(6,2)`, `union(6,2)`, `union(5,3)`, `union(0,4)`, `union(6,3)`. How many sets remain?

a) 3
b) 2
c) 4
d) 6

**Key: a**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(6,2)` leaves 6 sets, largest 2; 2. `union(6,2)` (already in one set, nothing changes) leaves 6 sets, largest 2; 3. `union(5,3)` leaves 5 sets, largest 2; 4. `union(0,4)` leaves 4 sets, largest 2; 5. `union(6,3)` leaves 3 sets, largest 4. Result: 3. Source: `erickson-union-find#p1`.

## 23. seed 1762718859500371441, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(0,6)`, `union(1,3)`, `union(0,5)`, `union(0,2)`. How many sets remain?

a) 3
b) 7
c) 5
d) 6

**Key: a**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(0,6)` leaves 6 sets, largest 2; 2. `union(1,3)` leaves 5 sets, largest 2; 3. `union(0,5)` leaves 4 sets, largest 3; 4. `union(0,2)` leaves 3 sets, largest 4. Result: 3. Source: `erickson-union-find#p1`.

## 24. seed 1172451388007111943, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(4,6)`, `union(2,3)`, `union(4,2)`, `union(4,5)`. How many sets remain?

a) 3
b) 5
c) 7
d) 4

**Key: a**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(4,6)` leaves 6 sets, largest 2; 2. `union(2,3)` leaves 5 sets, largest 2; 3. `union(4,2)` leaves 4 sets, largest 4; 4. `union(4,5)` leaves 3 sets, largest 5. Result: 3. Source: `erickson-union-find#p1`.

## 25. seed 1567996735041084861, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(2,3)`, `union(5,1)`, `union(3,7)`, `union(5,3)`, `union(0,6)`. What size is the largest set?

a) 4
b) 6
c) 5
d) 3

**Key: c**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(2,3)` leaves 7 sets, largest 2; 2. `union(5,1)` leaves 6 sets, largest 2; 3. `union(3,7)` leaves 5 sets, largest 3; 4. `union(5,3)` leaves 4 sets, largest 5; 5. `union(0,6)` leaves 3 sets, largest 5. Result: 5. Source: `erickson-union-find#p1`.

## 26. seed 1345467404184775646, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(2,3)`, `union(5,3)`, `union(7,4)`, `union(3,1)`, `union(1,7)`. What size is the largest set?

a) 5
b) 6
c) 3
d) 4

**Key: b**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(2,3)` leaves 7 sets, largest 2; 2. `union(5,3)` leaves 6 sets, largest 3; 3. `union(7,4)` leaves 5 sets, largest 3; 4. `union(3,1)` leaves 4 sets, largest 4; 5. `union(1,7)` leaves 3 sets, largest 6. Result: 6. Source: `erickson-union-find#p1`.

## 27. seed 3707500171611238096, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(3,5)`, `union(0,1)`, `union(6,1)`, `union(4,1)`, `union(3,0)`. How many sets remain?

a) 7
b) 6
c) 3
d) 2

**Key: d**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(3,5)` leaves 6 sets, largest 2; 2. `union(0,1)` leaves 5 sets, largest 2; 3. `union(6,1)` leaves 4 sets, largest 3; 4. `union(4,1)` leaves 3 sets, largest 4; 5. `union(3,0)` leaves 2 sets, largest 6. Result: 2. Source: `erickson-union-find#p1`.

## 28. seed 436477801771242544, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(3,5)`, `union(4,6)`, `union(5,3)`, `union(5,0)`, `union(4,5)`, `union(5,3)`. How many sets remain?

a) 3
b) 5
c) 4
d) 7

**Key: a**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(3,5)` leaves 6 sets, largest 2; 2. `union(4,6)` leaves 5 sets, largest 2; 3. `union(5,3)` (already in one set, nothing changes) leaves 5 sets, largest 2; 4. `union(5,0)` leaves 4 sets, largest 3; 5. `union(4,5)` leaves 3 sets, largest 5; 6. `union(5,3)` (already in one set, nothing changes) leaves 3 sets, largest 5. Result: 3. Source: `erickson-union-find#p1`.

## 29. seed 1552548601871867877, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(2,0)`, `union(0,3)`, `union(1,6)`, `union(1,5)`, `union(6,5)`, `union(6,0)`. How many sets remain?

a) 6
b) 3
c) 7
d) 2

**Key: d**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(2,0)` leaves 6 sets, largest 2; 2. `union(0,3)` leaves 5 sets, largest 3; 3. `union(1,6)` leaves 4 sets, largest 3; 4. `union(1,5)` leaves 3 sets, largest 3; 5. `union(6,5)` (already in one set, nothing changes) leaves 3 sets, largest 3; 6. `union(6,0)` leaves 2 sets, largest 6. Result: 2. Source: `erickson-union-find#p1`.

## 30. seed 3304397592875850257, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(1,5)`, `union(3,0)`, `union(3,1)`, `union(1,0)`, `union(4,0)`. How many sets remain?

a) 4
b) 5
c) 7
d) 3

**Key: d**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(1,5)` leaves 6 sets, largest 2; 2. `union(3,0)` leaves 5 sets, largest 2; 3. `union(3,1)` leaves 4 sets, largest 4; 4. `union(1,0)` (already in one set, nothing changes) leaves 4 sets, largest 4; 5. `union(4,0)` leaves 3 sets, largest 5. Result: 3. Source: `erickson-union-find#p1`.

## 31. seed 4285297664272672244, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(5,0)`, `union(0,7)`, `union(0,5)`, `union(7,0)`, `union(5,4)`, `union(2,7)`, `union(7,3)`. What size is the largest set?

a) 8
b) 5
c) 3
d) 6

**Key: d**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(5,0)` leaves 7 sets, largest 2; 2. `union(0,7)` leaves 6 sets, largest 3; 3. `union(0,5)` (already in one set, nothing changes) leaves 6 sets, largest 3; 4. `union(7,0)` (already in one set, nothing changes) leaves 6 sets, largest 3; 5. `union(5,4)` leaves 5 sets, largest 4; 6. `union(2,7)` leaves 4 sets, largest 5; 7. `union(7,3)` leaves 3 sets, largest 6. Result: 6. Source: `erickson-union-find#p1`.

## 32. seed 2669942485435568500, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(0,2)`, `union(3,2)`, `union(4,7)`, `union(5,0)`, `union(1,5)`, `union(6,3)`, `union(3,7)`. What size is the largest set?

a) 3
b) 6
c) 8
d) 5

**Key: c**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(0,2)` leaves 7 sets, largest 2; 2. `union(3,2)` leaves 6 sets, largest 3; 3. `union(4,7)` leaves 5 sets, largest 3; 4. `union(5,0)` leaves 4 sets, largest 4; 5. `union(1,5)` leaves 3 sets, largest 5; 6. `union(6,3)` leaves 2 sets, largest 6; 7. `union(3,7)` leaves 1 set, largest 8. Result: 8. Source: `erickson-union-find#p1`.

## 33. seed 3687235497756449169, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(5,3)`, `union(2,6)`, `union(0,3)`, `union(7,2)`, `union(1,3)`, `union(0,2)`, `union(0,6)`. What size is the largest set?

a) 4
b) 8
c) 6
d) 7

**Key: d**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(5,3)` leaves 7 sets, largest 2; 2. `union(2,6)` leaves 6 sets, largest 2; 3. `union(0,3)` leaves 5 sets, largest 3; 4. `union(7,2)` leaves 4 sets, largest 3; 5. `union(1,3)` leaves 3 sets, largest 4; 6. `union(0,2)` leaves 2 sets, largest 7; 7. `union(0,6)` (already in one set, nothing changes) leaves 2 sets, largest 7. Result: 7. Source: `erickson-union-find#p1`.

## 34. seed 4167471493809179777, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(2,5)`, `union(0,4)`, `union(0,3)`, `union(1,3)`, `union(2,4)`, `union(4,5)`. How many sets remain?

a) 7
b) 6
c) 2
d) 4

**Key: c**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(2,5)` leaves 6 sets, largest 2; 2. `union(0,4)` leaves 5 sets, largest 2; 3. `union(0,3)` leaves 4 sets, largest 3; 4. `union(1,3)` leaves 3 sets, largest 4; 5. `union(2,4)` leaves 2 sets, largest 6; 6. `union(4,5)` (already in one set, nothing changes) leaves 2 sets, largest 6. Result: 2. Source: `erickson-union-find#p1`.

## 35. seed 3353219764469889938, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(2,6)`, `union(4,1)`, `union(3,0)`, `union(2,3)`. How many sets remain?

a) 4
b) 6
c) 7
d) 3

**Key: d**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(2,6)` leaves 6 sets, largest 2; 2. `union(4,1)` leaves 5 sets, largest 2; 3. `union(3,0)` leaves 4 sets, largest 2; 4. `union(2,3)` leaves 3 sets, largest 4. Result: 3. Source: `erickson-union-find#p1`.

## 36. seed 2469421326265102258, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(2,3)`, `union(0,2)`, `union(2,5)`, `union(3,6)`, `union(5,6)`, `union(6,4)`. How many sets remain?

a) 3
b) 6
c) 2
d) 5

**Key: c**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(2,3)` leaves 6 sets, largest 2; 2. `union(0,2)` leaves 5 sets, largest 3; 3. `union(2,5)` leaves 4 sets, largest 4; 4. `union(3,6)` leaves 3 sets, largest 5; 5. `union(5,6)` (already in one set, nothing changes) leaves 3 sets, largest 5; 6. `union(6,4)` leaves 2 sets, largest 6. Result: 2. Source: `erickson-union-find#p1`.

## 37. seed 138306632739451010, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(4,5)`, `union(0,5)`, `union(0,4)`, `union(6,0)`, `union(5,1)`. How many sets remain?

a) 5
b) 2
c) 3
d) 4

**Key: c**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(4,5)` leaves 6 sets, largest 2; 2. `union(0,5)` leaves 5 sets, largest 3; 3. `union(0,4)` (already in one set, nothing changes) leaves 5 sets, largest 3; 4. `union(6,0)` leaves 4 sets, largest 4; 5. `union(5,1)` leaves 3 sets, largest 5. Result: 3. Source: `erickson-union-find#p1`.

## 38. seed 3826921963813084362, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(3,7)`, `union(2,6)`, `union(3,7)`, `union(6,3)`, `union(6,7)`, `union(1,7)`, `union(7,4)`. What size is the largest set?

a) 5
b) 3
c) 6
d) 8

**Key: c**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(3,7)` leaves 7 sets, largest 2; 2. `union(2,6)` leaves 6 sets, largest 2; 3. `union(3,7)` (already in one set, nothing changes) leaves 6 sets, largest 2; 4. `union(6,3)` leaves 5 sets, largest 4; 5. `union(6,7)` (already in one set, nothing changes) leaves 5 sets, largest 4; 6. `union(1,7)` leaves 4 sets, largest 5; 7. `union(7,4)` leaves 3 sets, largest 6. Result: 6. Source: `erickson-union-find#p1`.

## 39. seed 974159161517094002, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(6,0)`, `union(5,1)`, `union(5,6)`, `union(5,4)`, `union(5,7)`, `union(6,0)`. What size is the largest set?

a) 2
b) 7
c) 6
d) 3

**Key: c**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(6,0)` leaves 7 sets, largest 2; 2. `union(5,1)` leaves 6 sets, largest 2; 3. `union(5,6)` leaves 5 sets, largest 4; 4. `union(5,4)` leaves 4 sets, largest 5; 5. `union(5,7)` leaves 3 sets, largest 6; 6. `union(6,0)` (already in one set, nothing changes) leaves 3 sets, largest 6. Result: 6. Source: `erickson-union-find#p1`.

## 40. seed 442688247433806097, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(3,1)`, `union(6,0)`, `union(0,4)`, `union(0,3)`. How many sets remain?

a) 5
b) 4
c) 3
d) 7

**Key: c**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(3,1)` leaves 6 sets, largest 2; 2. `union(6,0)` leaves 5 sets, largest 2; 3. `union(0,4)` leaves 4 sets, largest 3; 4. `union(0,3)` leaves 3 sets, largest 5. Result: 3. Source: `erickson-union-find#p1`.

## 41. seed 3377399489659123933, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(5,6)`, `union(2,0)`, `union(3,5)`, `union(1,0)`, `union(1,3)`, `union(1,6)`. How many sets remain?

a) 4
b) 6
c) 1
d) 2

**Key: d**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(5,6)` leaves 6 sets, largest 2; 2. `union(2,0)` leaves 5 sets, largest 2; 3. `union(3,5)` leaves 4 sets, largest 3; 4. `union(1,0)` leaves 3 sets, largest 3; 5. `union(1,3)` leaves 2 sets, largest 6; 6. `union(1,6)` (already in one set, nothing changes) leaves 2 sets, largest 6. Result: 2. Source: `erickson-union-find#p1`.

## 42. seed 848393087554344689, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(2,0)`, `union(5,2)`, `union(1,2)`, `union(2,6)`. How many sets remain?

a) 4
b) 7
c) 3
d) 5

**Key: c**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(2,0)` leaves 6 sets, largest 2; 2. `union(5,2)` leaves 5 sets, largest 3; 3. `union(1,2)` leaves 4 sets, largest 4; 4. `union(2,6)` leaves 3 sets, largest 5. Result: 3. Source: `erickson-union-find#p1`.

## 43. seed 4284857062153578225, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(5,2)`, `union(5,0)`, `union(5,3)`, `union(2,3)`. How many sets remain?

a) 4
b) 5
c) 3
d) 7

**Key: a**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(5,2)` leaves 6 sets, largest 2; 2. `union(5,0)` leaves 5 sets, largest 3; 3. `union(5,3)` leaves 4 sets, largest 4; 4. `union(2,3)` (already in one set, nothing changes) leaves 4 sets, largest 4. Result: 4. Source: `erickson-union-find#p1`.

## 44. seed 4522289280490568669, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(1,4)`, `union(4,1)`, `union(3,6)`, `union(7,1)`, `union(7,6)`. What size is the largest set?

a) 5
b) 3
c) 4
d) 6

**Key: a**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(1,4)` leaves 7 sets, largest 2; 2. `union(4,1)` (already in one set, nothing changes) leaves 7 sets, largest 2; 3. `union(3,6)` leaves 6 sets, largest 2; 4. `union(7,1)` leaves 5 sets, largest 3; 5. `union(7,6)` leaves 4 sets, largest 5. Result: 5. Source: `erickson-union-find#p1`.

## 45. seed 2728377485316319944, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(2,4)`, `union(3,0)`, `union(5,0)`, `union(4,6)`, `union(3,4)`. What size is the largest set?

a) 2
b) 3
c) 5
d) 6

**Key: d**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(2,4)` leaves 7 sets, largest 2; 2. `union(3,0)` leaves 6 sets, largest 2; 3. `union(5,0)` leaves 5 sets, largest 3; 4. `union(4,6)` leaves 4 sets, largest 3; 5. `union(3,4)` leaves 3 sets, largest 6. Result: 6. Source: `erickson-union-find#p1`.

## 46. seed 3696568151477497381, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(6,4)`, `union(5,4)`, `union(0,3)`, `union(4,6)`, `union(3,2)`. How many sets remain?

a) 2
b) 7
c) 6
d) 3

**Key: d**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(6,4)` leaves 6 sets, largest 2; 2. `union(5,4)` leaves 5 sets, largest 3; 3. `union(0,3)` leaves 4 sets, largest 3; 4. `union(4,6)` (already in one set, nothing changes) leaves 4 sets, largest 3; 5. `union(3,2)` leaves 3 sets, largest 3. Result: 3. Source: `erickson-union-find#p1`.

## 47. seed 4024312150384158406, level 2

A union-find structure starts with 8 singleton sets, one per element 0 to 7. Each `union(a,b)` merges the whole sets of a and b. It runs `union(5,0)`, `union(6,3)`, `union(7,0)`, `union(3,7)`, `union(3,6)`, `union(6,2)`. What size is the largest set?

a) 5
b) 3
c) 6
d) 7

**Key: c**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 8 sets of one element. 1. `union(5,0)` leaves 7 sets, largest 2; 2. `union(6,3)` leaves 6 sets, largest 2; 3. `union(7,0)` leaves 5 sets, largest 3; 4. `union(3,7)` leaves 4 sets, largest 5; 5. `union(3,6)` (already in one set, nothing changes) leaves 4 sets, largest 5; 6. `union(6,2)` leaves 3 sets, largest 6. Result: 6. Source: `erickson-union-find#p1`.

## 48. seed 1915018140014620216, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(6,2)`, `union(5,3)`, `union(5,6)`, `union(6,5)`. How many sets remain?

a) 3
b) 5
c) 7
d) 4

**Key: d**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(6,2)` leaves 6 sets, largest 2; 2. `union(5,3)` leaves 5 sets, largest 2; 3. `union(5,6)` leaves 4 sets, largest 4; 4. `union(6,5)` (already in one set, nothing changes) leaves 4 sets, largest 4. Result: 4. Source: `erickson-union-find#p1`.

## 49. seed 1893210507221643635, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(2,0)`, `union(3,4)`, `union(0,2)`, `union(6,2)`, `union(6,1)`. How many sets remain?

a) 2
b) 4
c) 6
d) 3

**Key: d**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(2,0)` leaves 6 sets, largest 2; 2. `union(3,4)` leaves 5 sets, largest 2; 3. `union(0,2)` (already in one set, nothing changes) leaves 5 sets, largest 2; 4. `union(6,2)` leaves 4 sets, largest 3; 5. `union(6,1)` leaves 3 sets, largest 4. Result: 3. Source: `erickson-union-find#p1`.

## 50. seed 3587709921273287918, level 1

A union-find structure starts with 7 singleton sets, one per element 0 to 6. Each `union(a,b)` merges the whole sets of a and b. It runs `union(3,1)`, `union(4,6)`, `union(0,2)`, `union(6,4)`, `union(2,0)`. How many sets remain?

a) 6
b) 4
c) 5
d) 2

**Key: b**

Explanation: A union replaces the two sets of its arguments with their union, and a union of two elements already in one set changes nothing. Start with 7 sets of one element. 1. `union(3,1)` leaves 6 sets, largest 2; 2. `union(4,6)` leaves 5 sets, largest 2; 3. `union(0,2)` leaves 4 sets, largest 2; 4. `union(6,4)` (already in one set, nothing changes) leaves 4 sets, largest 2; 5. `union(2,0)` (already in one set, nothing changes) leaves 4 sets, largest 2. Result: 4. Source: `erickson-union-find#p1`.
