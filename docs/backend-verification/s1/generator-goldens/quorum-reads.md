# Quorums and stale reads (`quorum-reads`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 527965990681310867, level 2

A key is replicated on `n = 5` nodes. A write succeeds once `w = 1` replicas acknowledge it. The other replicas have not received the write yet. A read queries `r = 1` replicas, chosen as unluckily as possible. At most how many of the replicas it queries can return the old value?

a) 3
b) 1
c) 0
d) 5

**Key: b**

Explanation: 4 replicas still hold the old value. The unluckiest read queries as many of them as it can: the smaller of `r = 1` and 4, that is 1.

## 2. seed 813759751475122570, level 2

A key is replicated on `n = 4` nodes. A write succeeds once `w = 1` replicas acknowledge it. The other replicas have not received the write yet. A read queries `r = 3` replicas, chosen as unluckily as possible. At most how many of the replicas it queries can return the old value?

a) 3
b) 0
c) 2
d) 1

**Key: a**

Explanation: 3 replicas still hold the old value. The unluckiest read queries as many of them as it can: the smaller of `r = 3` and 3, that is 3.

## 3. seed 527060546583561360, level 1

A key is replicated on `n = 4` nodes. A write succeeds once `w = 2` replicas acknowledge it. A later read queries `r = 2` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) A read can return stale data when it picks replicas that missed the write: `w + r = 4` does not exceed `n = 4`, so a read set can avoid every replica that took the write
b) No stale read is possible, whichever replicas the read picks: reads always pick the replica with the latest timestamp
c) No stale read is possible, whichever replicas the read picks: `w + r = 4` equals `n = 4`, which is enough
d) No stale read is possible, whichever replicas the read picks: the `r = 2` replicas are queried in parallel, so one of them is current

**Key: a**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `2 + 2 = 4` against `n = 4`: 4 does not exceed 4, so the 2 replicas read can all lie among the 2 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 4. seed 3858026415065172012, level 1

A key is replicated on `n = 7` nodes. A write succeeds once `w = 4` replicas acknowledge it. A later read queries `r = 3` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) No stale read is possible, whichever replicas the read picks: `w + r = 7` reaches `n = 7`
b) A read can return stale data when it picks replicas that missed the write: `w + r = 7` does not exceed `n = 7`, so a read set can avoid every replica that took the write
c) No stale read is possible: `w + r = 7` reaches `n = 7`
d) No stale read is possible, whichever replicas the read picks: reads always pick the replica with the latest timestamp

**Key: b**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `4 + 3 = 7` against `n = 7`: 7 does not exceed 7, so the 3 replicas read can all lie among the 3 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 5. seed 2266273069307326981, level 2

A key is replicated on `n = 4` nodes. A write succeeds once `w = 3` replicas acknowledge it. The remaining replicas have not received the write yet. What is the smallest `r` for which every read is guaranteed to include at least one replica holding the acknowledged write?

a) 1
b) 4
c) 2
d) 3

**Key: c**

Explanation: 1 replicas missed the write. A read must not fit among them, so it needs one more than that: 4 - 3 + 1 = 2, which is the smallest `r` with `w + r > n`.

## 6. seed 301117554378979303, level 1

A key is replicated on `n = 7` nodes. A write succeeds once `w = 4` replicas acknowledge it. A later read queries `r = 3` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) No stale read is possible: `w + r = 7` reaches `n = 7`
b) No stale read is possible: `w + r = 7` equals `n = 7`, which is enough
c) A read can return stale data: `w + r = 7` does not exceed `n = 7`
d) No stale read is possible: reads always pick the replica with the latest timestamp

**Key: c**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `4 + 3 = 7` against `n = 7`: 7 does not exceed 7, so the 3 replicas read can all lie among the 3 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 7. seed 2253609860421789747, level 1

A key is replicated on `n = 7` nodes. A write succeeds once `w = 5` replicas acknowledge it. A later read queries `r = 2` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) No stale read is possible, whichever replicas the read picks: the `r = 2` replicas are queried in parallel, so one of them is current
b) No stale read is possible, whichever replicas the read picks: the read returns the newest version among its `r = 2` replicas
c) No stale read is possible: the `r = 2` replicas are queried in parallel, so one of them is current
d) A read can return stale data: `w + r = 7` does not exceed `n = 7`

**Key: d**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `5 + 2 = 7` against `n = 7`: 7 does not exceed 7, so the 2 replicas read can all lie among the 2 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 8. seed 4595766395120198344, level 2

A key is replicated on `n = 3` nodes. A write succeeds once `w = 1` replicas acknowledge it. The remaining replicas have not received the write yet. What is the smallest `r` for which every read is guaranteed to include at least one replica holding the acknowledged write?

a) 2
b) 3
c) 1
d) 4

**Key: b**

Explanation: 2 replicas missed the write. A read must not fit among them, so it needs one more than that: 3 - 1 + 1 = 3, which is the smallest `r` with `w + r > n`.

## 9. seed 4025136080661451281, level 2

A key is replicated on `n = 5` nodes. A write succeeds once `w = 2` replicas acknowledge it. The other replicas have not received the write yet. A read queries `r = 2` replicas, chosen as unluckily as possible. At most how many of the replicas it queries can return the old value?

a) 0
b) 2
c) 1
d) 4

**Key: b**

Explanation: 3 replicas still hold the old value. The unluckiest read queries as many of them as it can: the smaller of `r = 2` and 3, that is 2.

## 10. seed 3989605980743320045, level 2

A key is replicated on `n = 6` nodes. A write succeeds once `w = 1` replicas acknowledge it. The other replicas have not received the write yet. A read queries `r = 4` replicas, chosen as unluckily as possible. At most how many of the replicas it queries can return the old value?

a) 1
b) 3
c) 6
d) 4

**Key: d**

Explanation: 5 replicas still hold the old value. The unluckiest read queries as many of them as it can: the smaller of `r = 4` and 5, that is 4.

## 11. seed 3902992657521036900, level 2

A key is replicated on `n = 5` nodes. A write succeeds once `w = 3` replicas acknowledge it. The remaining replicas have not received the write yet. What is the smallest `r` for which every read is guaranteed to include at least one replica holding the acknowledged write?

a) 3
b) 2
c) 5
d) 4

**Key: a**

Explanation: 2 replicas missed the write. A read must not fit among them, so it needs one more than that: 5 - 3 + 1 = 3, which is the smallest `r` with `w + r > n`.

## 12. seed 1506680805953395178, level 1

A key is replicated on `n = 4` nodes. A write succeeds once `w = 3` replicas acknowledge it. A later read queries `r = 1` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) No stale read is possible: the read returns the newest version among its `r = 1` replicas
b) No stale read is possible: `w + r = 4` reaches `n = 4`
c) A read can return stale data when it picks replicas that missed the write: `w + r = 4` does not exceed `n = 4`, so a read set can avoid every replica that took the write
d) No stale read is possible: `w + r = 4` equals `n = 4`, which is enough

**Key: c**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `3 + 1 = 4` against `n = 4`: 4 does not exceed 4, so the 1 replicas read can all lie among the 1 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 13. seed 1590276496060924511, level 2

A key is replicated on `n = 3` nodes. A write succeeds once `w = 1` replicas acknowledge it. The other replicas have not received the write yet. A read queries `r = 2` replicas, chosen as unluckily as possible. At most how many of the replicas it queries can return the old value?

a) 0
b) 1
c) 3
d) 2

**Key: d**

Explanation: 2 replicas still hold the old value. The unluckiest read queries as many of them as it can: the smaller of `r = 2` and 2, that is 2.

## 14. seed 3864490030591455873, level 2

A key is replicated on `n = 4` nodes. A write succeeds once `w = 3` replicas acknowledge it. The remaining replicas have not received the write yet. What is the smallest `r` for which every read is guaranteed to include at least one replica holding the acknowledged write?

a) 1
b) 3
c) 4
d) 2

**Key: d**

Explanation: 1 replicas missed the write. A read must not fit among them, so it needs one more than that: 4 - 3 + 1 = 2, which is the smallest `r` with `w + r > n`.

## 15. seed 3638330773469671350, level 1

A key is replicated on `n = 4` nodes. A write succeeds once `w = 1` replicas acknowledge it. A later read queries `r = 2` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) No stale read is possible, whichever replicas the read picks: reads always pick the replica with the latest timestamp
b) No stale read is possible, whichever replicas the read picks: the `r = 2` replicas are queried in parallel, so one of them is current
c) No stale read is possible: reads always pick the replica with the latest timestamp
d) A read can return stale data: `w + r = 3` does not exceed `n = 4`

**Key: d**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `1 + 2 = 3` against `n = 4`: 3 does not exceed 4, so the 2 replicas read can all lie among the 3 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 16. seed 3384098202843389612, level 1

A key is replicated on `n = 3` nodes. A write succeeds once `w = 2` replicas acknowledge it. A later read queries `r = 2` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) A read can return stale data when it picks replicas that missed the write: the write is not on every replica, so the `r = 2` read replicas can all be stale
b) No stale read is possible, whichever replicas the read picks: `w + r = 4` exceeds `n = 3`, so every read set shares a replica with the write set
c) A read can return stale data: the write is not on every replica, so the `r = 2` read replicas can all be stale
d) A read can return stale data when it picks replicas that missed the write: `r = 2` is below `n = 3`

**Key: b**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `2 + 2 = 4` against `n = 3`: 4 is greater than 3, so every read set shares a replica with the write set. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 17. seed 1140265612951153235, level 1

A key is replicated on `n = 3` nodes. A write succeeds once `w = 1` replicas acknowledge it. A later read queries `r = 1` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) No stale read is possible: the read returns the newest version among its `r = 1` replicas
b) No stale read is possible, whichever replicas the read picks: reads always pick the replica with the latest timestamp
c) A read can return stale data when it picks replicas that missed the write: `w + r = 2` does not exceed `n = 3`, so a read set can avoid every replica that took the write
d) No stale read is possible, whichever replicas the read picks: the read returns the newest version among its `r = 1` replicas

**Key: c**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `1 + 1 = 2` against `n = 3`: 2 does not exceed 3, so the 1 replicas read can all lie among the 2 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 18. seed 1283155051615709274, level 2

A key is replicated on `n = 6` nodes. A write succeeds once `w = 1` replicas acknowledge it. The remaining replicas have not received the write yet. What is the smallest `r` for which every read is guaranteed to include at least one replica holding the acknowledged write?

a) 7
b) 4
c) 6
d) 5

**Key: c**

Explanation: 5 replicas missed the write. A read must not fit among them, so it needs one more than that: 6 - 1 + 1 = 6, which is the smallest `r` with `w + r > n`.

## 19. seed 2103098139555222580, level 1

A key is replicated on `n = 5` nodes. A write succeeds once `w = 4` replicas acknowledge it. A later read queries `r = 1` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) No stale read is possible: reads always pick the replica with the latest timestamp
b) A read can return stale data when it picks replicas that missed the write: `w + r = 5` does not exceed `n = 5`, so a read set can avoid every replica that took the write
c) No stale read is possible, whichever replicas the read picks: `w = 4` is a majority of `n = 5`
d) No stale read is possible: `w + r = 5` reaches `n = 5`

**Key: b**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `4 + 1 = 5` against `n = 5`: 5 does not exceed 5, so the 1 replicas read can all lie among the 1 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 20. seed 3211460051463190206, level 1

A key is replicated on `n = 6` nodes. A write succeeds once `w = 3` replicas acknowledge it. A later read queries `r = 3` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) A read can return stale data: `w + r = 6` does not exceed `n = 6`
b) No stale read is possible, whichever replicas the read picks: `w + r = 6` reaches `n = 6`
c) No stale read is possible, whichever replicas the read picks: reads always pick the replica with the latest timestamp
d) No stale read is possible, whichever replicas the read picks: the `r = 3` replicas are queried in parallel, so one of them is current

**Key: a**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `3 + 3 = 6` against `n = 6`: 6 does not exceed 6, so the 3 replicas read can all lie among the 3 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 21. seed 2797809490101666736, level 2

A key is replicated on `n = 6` nodes. A write succeeds once `w = 3` replicas acknowledge it. The other replicas have not received the write yet. A read queries `r = 2` replicas, chosen as unluckily as possible. At most how many of the replicas it queries can return the old value?

a) 2
b) 3
c) 0
d) 1

**Key: a**

Explanation: 3 replicas still hold the old value. The unluckiest read queries as many of them as it can: the smaller of `r = 2` and 3, that is 2.

## 22. seed 3468334657960247648, level 2

A key is replicated on `n = 4` nodes. A write succeeds once `w = 2` replicas acknowledge it. The other replicas have not received the write yet. A read queries `r = 1` replicas, chosen as unluckily as possible. At most how many of the replicas it queries can return the old value?

a) 1
b) 3
c) 2
d) 0

**Key: a**

Explanation: 2 replicas still hold the old value. The unluckiest read queries as many of them as it can: the smaller of `r = 1` and 2, that is 1.

## 23. seed 1367274980937009730, level 2

A key is replicated on `n = 5` nodes. A write succeeds once `w = 4` replicas acknowledge it. The other replicas have not received the write yet. A read queries `r = 1` replicas, chosen as unluckily as possible. At most how many of the replicas it queries can return the old value?

a) 1
b) 0
c) 2
d) 4

**Key: a**

Explanation: 1 replicas still hold the old value. The unluckiest read queries as many of them as it can: the smaller of `r = 1` and 1, that is 1.

## 24. seed 4477616879083318462, level 1

A key is replicated on `n = 4` nodes. A write succeeds once `w = 2` replicas acknowledge it. A later read queries `r = 2` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) No stale read is possible: reads always pick the replica with the latest timestamp
b) A read can return stale data: `w + r = 4` does not exceed `n = 4`
c) No stale read is possible: the `r = 2` replicas are queried in parallel, so one of them is current
d) No stale read is possible: `w + r = 4` equals `n = 4`, which is enough

**Key: b**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `2 + 2 = 4` against `n = 4`: 4 does not exceed 4, so the 2 replicas read can all lie among the 2 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 25. seed 739452941555601323, level 2

A key is replicated on `n = 6` nodes. A write succeeds once `w = 5` replicas acknowledge it. The other replicas have not received the write yet. A read queries `r = 1` replicas, chosen as unluckily as possible. At most how many of the replicas it queries can return the old value?

a) 0
b) 2
c) 5
d) 1

**Key: d**

Explanation: 1 replicas still hold the old value. The unluckiest read queries as many of them as it can: the smaller of `r = 1` and 1, that is 1.

## 26. seed 4596146205013673645, level 2

A key is replicated on `n = 5` nodes. A write succeeds once `w = 2` replicas acknowledge it. The other replicas have not received the write yet. A read queries `r = 1` replicas, chosen as unluckily as possible. At most how many of the replicas it queries can return the old value?

a) 1
b) 2
c) 4
d) 0

**Key: a**

Explanation: 3 replicas still hold the old value. The unluckiest read queries as many of them as it can: the smaller of `r = 1` and 3, that is 1.

## 27. seed 699356200686023110, level 2

A key is replicated on `n = 5` nodes. A write succeeds once `w = 2` replicas acknowledge it. The other replicas have not received the write yet. A read queries `r = 3` replicas, chosen as unluckily as possible. At most how many of the replicas it queries can return the old value?

a) 3
b) 1
c) 2
d) 0

**Key: a**

Explanation: 3 replicas still hold the old value. The unluckiest read queries as many of them as it can: the smaller of `r = 3` and 3, that is 3.

## 28. seed 1326360724740424724, level 1

A key is replicated on `n = 4` nodes. A write succeeds once `w = 1` replicas acknowledge it. A later read queries `r = 1` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) No stale read is possible: the read returns the newest version among its `r = 1` replicas
b) No stale read is possible: reads always pick the replica with the latest timestamp
c) A read can return stale data: `w + r = 2` does not exceed `n = 4`
d) No stale read is possible, whichever replicas the read picks: the `r = 1` replicas are queried in parallel, so one of them is current

**Key: c**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `1 + 1 = 2` against `n = 4`: 2 does not exceed 4, so the 1 replicas read can all lie among the 3 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 29. seed 3522955171469149606, level 1

A key is replicated on `n = 7` nodes. A write succeeds once `w = 4` replicas acknowledge it. A later read queries `r = 2` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) No stale read is possible: the `r = 2` replicas are queried in parallel, so one of them is current
b) No stale read is possible: reads always pick the replica with the latest timestamp
c) A read can return stale data: `w + r = 6` does not exceed `n = 7`
d) No stale read is possible: `w = 4` is a majority of `n = 7`

**Key: c**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `4 + 2 = 6` against `n = 7`: 6 does not exceed 7, so the 2 replicas read can all lie among the 3 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 30. seed 527443445149598114, level 1

A key is replicated on `n = 3` nodes. A write succeeds once `w = 1` replicas acknowledge it. A later read queries `r = 2` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) No stale read is possible: `r = 2` is a majority of `n = 3`
b) A read can return stale data when it picks replicas that missed the write: `w + r = 3` does not exceed `n = 3`, so a read set can avoid every replica that took the write
c) No stale read is possible, whichever replicas the read picks: the `r = 2` replicas are queried in parallel, so one of them is current
d) No stale read is possible: the read returns the newest version among its `r = 2` replicas

**Key: b**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `1 + 2 = 3` against `n = 3`: 3 does not exceed 3, so the 2 replicas read can all lie among the 2 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 31. seed 1096201558928120299, level 1

A key is replicated on `n = 6` nodes. A write succeeds once `w = 3` replicas acknowledge it. A later read queries `r = 3` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) No stale read is possible, whichever replicas the read picks: the `r = 3` replicas are queried in parallel, so one of them is current
b) No stale read is possible: `w + r = 6` reaches `n = 6`
c) A read can return stale data: `w + r = 6` does not exceed `n = 6`
d) No stale read is possible: reads always pick the replica with the latest timestamp

**Key: c**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `3 + 3 = 6` against `n = 6`: 6 does not exceed 6, so the 3 replicas read can all lie among the 3 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 32. seed 2979471578926859942, level 2

A key is replicated on `n = 7` nodes. A write succeeds once `w = 1` replicas acknowledge it. The other replicas have not received the write yet. A read queries `r = 1` replicas, chosen as unluckily as possible. At most how many of the replicas it queries can return the old value?

a) 0
b) 5
c) 7
d) 1

**Key: d**

Explanation: 6 replicas still hold the old value. The unluckiest read queries as many of them as it can: the smaller of `r = 1` and 6, that is 1.

## 33. seed 3984789972854251509, level 1

A key is replicated on `n = 7` nodes. A write succeeds once `w = 1` replicas acknowledge it. A later read queries `r = 6` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) No stale read is possible: `w + r = 7` equals `n = 7`, which is enough
b) No stale read is possible: `w + r = 7` reaches `n = 7`
c) A read can return stale data: `w + r = 7` does not exceed `n = 7`
d) No stale read is possible: the read returns the newest version among its `r = 6` replicas

**Key: c**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `1 + 6 = 7` against `n = 7`: 7 does not exceed 7, so the 6 replicas read can all lie among the 6 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 34. seed 4392649836245535050, level 2

A key is replicated on `n = 4` nodes. A write succeeds once `w = 1` replicas acknowledge it. The remaining replicas have not received the write yet. What is the smallest `r` for which every read is guaranteed to include at least one replica holding the acknowledged write?

a) 5
b) 4
c) 1
d) 3

**Key: b**

Explanation: 3 replicas missed the write. A read must not fit among them, so it needs one more than that: 4 - 1 + 1 = 4, which is the smallest `r` with `w + r > n`.

## 35. seed 716479519660126697, level 2

A key is replicated on `n = 3` nodes. A write succeeds once `w = 1` replicas acknowledge it. The remaining replicas have not received the write yet. What is the smallest `r` for which every read is guaranteed to include at least one replica holding the acknowledged write?

a) 1
b) 4
c) 2
d) 3

**Key: d**

Explanation: 2 replicas missed the write. A read must not fit among them, so it needs one more than that: 3 - 1 + 1 = 3, which is the smallest `r` with `w + r > n`.

## 36. seed 998825735166653981, level 1

A key is replicated on `n = 3` nodes. A write succeeds once `w = 2` replicas acknowledge it. A later read queries `r = 2` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) No stale read is possible: `w + r = 4` exceeds `n = 3`
b) A read can return stale data when it picks replicas that missed the write: `w = 2` is below `n = 3`
c) A read can return stale data when it picks replicas that missed the write: `r = 2` is below `n = 3`
d) A read can return stale data: replicas converge only eventually, so any read can lag

**Key: a**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `2 + 2 = 4` against `n = 3`: 4 is greater than 3, so every read set shares a replica with the write set. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 37. seed 3436537077358877014, level 2

A key is replicated on `n = 5` nodes. A write succeeds once `w = 2` replicas acknowledge it. The remaining replicas have not received the write yet. What is the smallest `r` for which every read is guaranteed to include at least one replica holding the acknowledged write?

a) 2
b) 4
c) 3
d) 5

**Key: b**

Explanation: 3 replicas missed the write. A read must not fit among them, so it needs one more than that: 5 - 2 + 1 = 4, which is the smallest `r` with `w + r > n`.

## 38. seed 91329810146434310, level 2

A key is replicated on `n = 3` nodes. A write succeeds once `w = 1` replicas acknowledge it. The remaining replicas have not received the write yet. What is the smallest `r` for which every read is guaranteed to include at least one replica holding the acknowledged write?

a) 1
b) 4
c) 2
d) 3

**Key: d**

Explanation: 2 replicas missed the write. A read must not fit among them, so it needs one more than that: 3 - 1 + 1 = 3, which is the smallest `r` with `w + r > n`.

## 39. seed 1749442189411096275, level 2

A key is replicated on `n = 7` nodes. A write succeeds once `w = 1` replicas acknowledge it. The remaining replicas have not received the write yet. What is the smallest `r` for which every read is guaranteed to include at least one replica holding the acknowledged write?

a) 6
b) 8
c) 7
d) 1

**Key: c**

Explanation: 6 replicas missed the write. A read must not fit among them, so it needs one more than that: 7 - 1 + 1 = 7, which is the smallest `r` with `w + r > n`.

## 40. seed 90375055984677965, level 2

A key is replicated on `n = 5` nodes. A write succeeds once `w = 2` replicas acknowledge it. The other replicas have not received the write yet. A read queries `r = 2` replicas, chosen as unluckily as possible. At most how many of the replicas it queries can return the old value?

a) 4
b) 2
c) 1
d) 0

**Key: b**

Explanation: 3 replicas still hold the old value. The unluckiest read queries as many of them as it can: the smaller of `r = 2` and 3, that is 2.

## 41. seed 4576183289809170036, level 2

A key is replicated on `n = 5` nodes. A write succeeds once `w = 2` replicas acknowledge it. The remaining replicas have not received the write yet. What is the smallest `r` for which every read is guaranteed to include at least one replica holding the acknowledged write?

a) 4
b) 5
c) 2
d) 3

**Key: a**

Explanation: 3 replicas missed the write. A read must not fit among them, so it needs one more than that: 5 - 2 + 1 = 4, which is the smallest `r` with `w + r > n`.

## 42. seed 103430359578862568, level 2

A key is replicated on `n = 6` nodes. A write succeeds once `w = 4` replicas acknowledge it. The remaining replicas have not received the write yet. What is the smallest `r` for which every read is guaranteed to include at least one replica holding the acknowledged write?

a) 6
b) 3
c) 4
d) 2

**Key: b**

Explanation: 2 replicas missed the write. A read must not fit among them, so it needs one more than that: 6 - 4 + 1 = 3, which is the smallest `r` with `w + r > n`.

## 43. seed 1938923600174845476, level 2

A key is replicated on `n = 7` nodes. A write succeeds once `w = 6` replicas acknowledge it. The other replicas have not received the write yet. A read queries `r = 1` replicas, chosen as unluckily as possible. At most how many of the replicas it queries can return the old value?

a) 2
b) 0
c) 6
d) 1

**Key: d**

Explanation: 1 replicas still hold the old value. The unluckiest read queries as many of them as it can: the smaller of `r = 1` and 1, that is 1.

## 44. seed 2532694958869188703, level 1

A key is replicated on `n = 7` nodes. A write succeeds once `w = 2` replicas acknowledge it. A later read queries `r = 5` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) No stale read is possible: reads always pick the replica with the latest timestamp
b) No stale read is possible, whichever replicas the read picks: the read returns the newest version among its `r = 5` replicas
c) A read can return stale data: `w + r = 7` does not exceed `n = 7`
d) No stale read is possible: the read returns the newest version among its `r = 5` replicas

**Key: c**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `2 + 5 = 7` against `n = 7`: 7 does not exceed 7, so the 5 replicas read can all lie among the 5 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 45. seed 3712260798652107483, level 1

A key is replicated on `n = 4` nodes. A write succeeds once `w = 3` replicas acknowledge it. A later read queries `r = 1` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) No stale read is possible: `w = 3` is a majority of `n = 4`
b) No stale read is possible: reads always pick the replica with the latest timestamp
c) No stale read is possible, whichever replicas the read picks: reads always pick the replica with the latest timestamp
d) A read can return stale data when it picks replicas that missed the write: `w + r = 4` does not exceed `n = 4`, so a read set can avoid every replica that took the write

**Key: d**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `3 + 1 = 4` against `n = 4`: 4 does not exceed 4, so the 1 replicas read can all lie among the 1 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 46. seed 1614339349441437611, level 1

A key is replicated on `n = 5` nodes. A write succeeds once `w = 1` replicas acknowledge it. A later read queries `r = 4` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) No stale read is possible, whichever replicas the read picks: the read returns the newest version among its `r = 4` replicas
b) No stale read is possible, whichever replicas the read picks: the `r = 4` replicas are queried in parallel, so one of them is current
c) A read can return stale data: `w + r = 5` does not exceed `n = 5`
d) No stale read is possible: `w + r = 5` reaches `n = 5`

**Key: c**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `1 + 4 = 5` against `n = 5`: 5 does not exceed 5, so the 4 replicas read can all lie among the 4 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 47. seed 1291160834945268412, level 1

A key is replicated on `n = 7` nodes. A write succeeds once `w = 4` replicas acknowledge it. A later read queries `r = 4` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) No stale read is possible, whichever replicas the read picks: `w + r = 8` exceeds `n = 7`, so every read set shares a replica with the write set
b) A read can return stale data when it picks replicas that missed the write: the write is not on every replica, so the `r = 4` read replicas can all be stale
c) A read can return stale data when it picks replicas that missed the write: replicas converge only eventually, so any read can lag
d) A read can return stale data when it picks replicas that missed the write: the write reached only `w = 4` of `n = 7` replicas

**Key: a**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `4 + 4 = 8` against `n = 7`: 8 is greater than 7, so every read set shares a replica with the write set. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 48. seed 4033603707236134189, level 2

A key is replicated on `n = 7` nodes. A write succeeds once `w = 5` replicas acknowledge it. The remaining replicas have not received the write yet. What is the smallest `r` for which every read is guaranteed to include at least one replica holding the acknowledged write?

a) 4
b) 2
c) 3
d) 5

**Key: c**

Explanation: 2 replicas missed the write. A read must not fit among them, so it needs one more than that: 7 - 5 + 1 = 3, which is the smallest `r` with `w + r > n`.

## 49. seed 44507423298798528, level 1

A key is replicated on `n = 4` nodes. A write succeeds once `w = 2` replicas acknowledge it. A later read queries `r = 2` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) A read can return stale data when it picks replicas that missed the write: `w + r = 4` does not exceed `n = 4`, so a read set can avoid every replica that took the write
b) No stale read is possible: `w + r = 4` equals `n = 4`, which is enough
c) No stale read is possible: the read returns the newest version among its `r = 2` replicas
d) No stale read is possible: the `r = 2` replicas are queried in parallel, so one of them is current

**Key: a**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `2 + 2 = 4` against `n = 4`: 4 does not exceed 4, so the 2 replicas read can all lie among the 2 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.

## 50. seed 4032722753844702934, level 1

A key is replicated on `n = 3` nodes. A write succeeds once `w = 1` replicas acknowledge it. A later read queries `r = 1` replicas, chosen as unluckily as possible, and returns the newest version among them. Which statement is true?

a) A read can return stale data: `w + r = 2` does not exceed `n = 3`
b) No stale read is possible: reads always pick the replica with the latest timestamp
c) No stale read is possible: the read returns the newest version among its `r = 1` replicas
d) No stale read is possible, whichever replicas the read picks: the read returns the newest version among its `r = 1` replicas

**Key: a**

Explanation: The read set and the write set must overlap in at least one replica, which needs `w + r > n`. Here `1 + 1 = 2` against `n = 3`: 2 does not exceed 3, so the 1 replicas read can all lie among the 2 that missed the write. Equality is not enough, because `w + r = n` still lets the two sets be disjoint.
