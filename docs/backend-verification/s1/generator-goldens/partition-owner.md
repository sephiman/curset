# Which partition receives a row (`partition-owner`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 1573767102060760604, level 1

A range-partitioned table has `p0` `FROM (0) TO (150)`, `p1` `FROM (150) TO (300)`, `p2` `FROM (300) TO (350)`, `p3` `FROM (350) TO (450)`. Which partition gets `id = 300`?

a) `p0`
b) `p2`
c) `p3`
d) `p1`

**Key: b**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 300. 2. `p2` covers 300 up to but not including 350, and 300 <= 300 < 350. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 2. seed 2052177292893171613, level 2

A table is hash partitioned with modulus 4: `p0` to `p3` take remainders 0 to 3. The hash value of a new row's partition key is `88`. Which partition receives the row?

a) `p0`
b) `p1`
c) `p3`
d) `p2`

**Key: a**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 88 by 4: 22 with remainder 0. 2. The partition with remainder 0 is `p0`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 3. seed 95722210000776501, level 1

A range-partitioned table has `p0` `FROM (0) TO (100)`, `p1` `FROM (100) TO (150)`, `p2` `FROM (150) TO (250)`, `p3` `FROM (250) TO (350)`, `p4` `FROM (350) TO (400)`. Which partition gets `id = 250`?

a) `p0`
b) `p4`
c) `p3`
d) `p2`

**Key: c**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 250. 2. `p3` covers 250 up to but not including 350, and 250 <= 250 < 350. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 4. seed 2674049407023758599, level 2

A table is hash partitioned with modulus 6: `p0` to `p5` take remainders 0 to 5. The hash value of a new row's partition key is `73`. Which partition receives the row?

a) `p1`
b) `p3`
c) `p4`
d) `p0`

**Key: a**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 73 by 6: 12 with remainder 1. 2. The partition with remainder 1 is `p1`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 5. seed 2527683940034467397, level 2

A table is hash partitioned with modulus 7: `p0` to `p6` take remainders 0 to 6. The hash value of a new row's partition key is `95`. Which partition receives the row?

a) `p6`
b) `p4`
c) `p2`
d) `p5`

**Key: b**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 95 by 7: 13 with remainder 4. 2. The partition with remainder 4 is `p4`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 6. seed 3745724300848940670, level 2

A table is hash partitioned with modulus 7: `p0` to `p6` take remainders 0 to 6. The hash value of a new row's partition key is `90`. Which partition receives the row?

a) `p2`
b) `p5`
c) `p0`
d) `p6`

**Key: d**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 90 by 7: 12 with remainder 6. 2. The partition with remainder 6 is `p6`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 7. seed 652377106218063717, level 2

A table is hash partitioned with modulus 7: `p0` to `p6` take remainders 0 to 6. The hash value of a new row's partition key is `41`. Which partition receives the row?

a) `p1`
b) `p6`
c) `p5`
d) `p0`

**Key: b**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 41 by 7: 5 with remainder 6. 2. The partition with remainder 6 is `p6`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 8. seed 1268693069988892280, level 1

A range-partitioned table has `p0` `FROM (100) TO (250)`, `p1` `FROM (250) TO (300)`, `p2` `FROM (300) TO (450)`, `p3` `FROM (450) TO (550)`. Which partition gets `id = 300`?

a) `p3`
b) `p2`
c) `p0`
d) `p1`

**Key: b**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 300. 2. `p2` covers 300 up to but not including 450, and 300 <= 300 < 450. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 9. seed 4135012410341955582, level 2

A table is hash partitioned with modulus 7: `p0` to `p6` take remainders 0 to 6. The hash value of a new row's partition key is `86`. Which partition receives the row?

a) `p2`
b) `p4`
c) `p5`
d) `p6`

**Key: a**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 86 by 7: 12 with remainder 2. 2. The partition with remainder 2 is `p2`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 10. seed 2980179177805562586, level 2

A table is hash partitioned with modulus 6: `p0` to `p5` take remainders 0 to 5. The hash value of a new row's partition key is `67`. Which partition receives the row?

a) `p5`
b) `p2`
c) `p1`
d) `p4`

**Key: c**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 67 by 6: 11 with remainder 1. 2. The partition with remainder 1 is `p1`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 11. seed 2566319082698948317, level 1

A range-partitioned table has `p0` `FROM (0) TO (150)`, `p1` `FROM (150) TO (200)`, `p2` `FROM (200) TO (350)`, `p3` `FROM (350) TO (500)`, `p4` `FROM (500) TO (650)`. Which partition gets `id = 200`?

a) `p1`
b) `p3`
c) `p0`
d) `p2`

**Key: d**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 200. 2. `p2` covers 200 up to but not including 350, and 200 <= 200 < 350. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 12. seed 3509943500091700548, level 1

A range-partitioned table has `p0` `FROM (100) TO (200)`, `p1` `FROM (200) TO (300)`, `p2` `FROM (300) TO (400)`, `p3` `FROM (400) TO (500)`, `p4` `FROM (500) TO (650)`. Which partition gets `id = 400`?

a) `p2`
b) `p0`
c) `p3`
d) `p4`

**Key: c**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 400. 2. `p3` covers 400 up to but not including 500, and 400 <= 400 < 500. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 13. seed 3422773350840114358, level 2

A table is hash partitioned with modulus 6: `p0` to `p5` take remainders 0 to 5. The hash value of a new row's partition key is `60`. Which partition receives the row?

a) `p0`
b) `p1`
c) `p4`
d) `p5`

**Key: a**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 60 by 6: 10 with remainder 0. 2. The partition with remainder 0 is `p0`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 14. seed 2263505825505000645, level 1

A range-partitioned table has `p0` `FROM (0) TO (100)`, `p1` `FROM (100) TO (200)`, `p2` `FROM (200) TO (300)`, `p3` `FROM (300) TO (350)`. Which partition gets `id = 200`?

a) `p1`
b) `p2`
c) `p3`
d) `p0`

**Key: b**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 200. 2. `p2` covers 200 up to but not including 300, and 200 <= 200 < 300. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 15. seed 172795131495644182, level 2

A table is hash partitioned with modulus 4: `p0` to `p3` take remainders 0 to 3. The hash value of a new row's partition key is `30`. Which partition receives the row?

a) `p0`
b) `p1`
c) `p3`
d) `p2`

**Key: d**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 30 by 4: 7 with remainder 2. 2. The partition with remainder 2 is `p2`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 16. seed 2112656910683044519, level 2

A table is hash partitioned with modulus 7: `p0` to `p6` take remainders 0 to 6. The hash value of a new row's partition key is `46`. Which partition receives the row?

a) `p4`
b) `p6`
c) `p2`
d) `p5`

**Key: a**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 46 by 7: 6 with remainder 4. 2. The partition with remainder 4 is `p4`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 17. seed 1283020075752076865, level 2

A table is hash partitioned with modulus 5: `p0` to `p4` take remainders 0 to 4. The hash value of a new row's partition key is `40`. Which partition receives the row?

a) `p1`
b) `p0`
c) `p3`
d) `p4`

**Key: b**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 40 by 5: 8 with remainder 0. 2. The partition with remainder 0 is `p0`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 18. seed 624021931309493198, level 2

A table is hash partitioned with modulus 4: `p0` to `p3` take remainders 0 to 3. The hash value of a new row's partition key is `90`. Which partition receives the row?

a) `p2`
b) `p3`
c) `p1`
d) `p0`

**Key: a**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 90 by 4: 22 with remainder 2. 2. The partition with remainder 2 is `p2`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 19. seed 4462333138515441600, level 2

A table is hash partitioned with modulus 7: `p0` to `p6` take remainders 0 to 6. The hash value of a new row's partition key is `92`. Which partition receives the row?

a) `p5`
b) `p4`
c) `p1`
d) `p6`

**Key: c**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 92 by 7: 13 with remainder 1. 2. The partition with remainder 1 is `p1`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 20. seed 3613027116922657535, level 2

A table is hash partitioned with modulus 6: `p0` to `p5` take remainders 0 to 5. The hash value of a new row's partition key is `75`. Which partition receives the row?

a) `p5`
b) `p3`
c) `p4`
d) `p2`

**Key: b**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 75 by 6: 12 with remainder 3. 2. The partition with remainder 3 is `p3`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 21. seed 2887943775120426648, level 2

A table is hash partitioned with modulus 7: `p0` to `p6` take remainders 0 to 6. The hash value of a new row's partition key is `53`. Which partition receives the row?

a) `p4`
b) `p2`
c) `p5`
d) `p0`

**Key: a**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 53 by 7: 7 with remainder 4. 2. The partition with remainder 4 is `p4`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 22. seed 722563800961784815, level 2

A table is hash partitioned with modulus 6: `p0` to `p5` take remainders 0 to 5. The hash value of a new row's partition key is `29`. Which partition receives the row?

a) `p1`
b) `p5`
c) `p4`
d) `p0`

**Key: b**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 29 by 6: 4 with remainder 5. 2. The partition with remainder 5 is `p5`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 23. seed 2496318950622248130, level 2

A table is hash partitioned with modulus 4: `p0` to `p3` take remainders 0 to 3. The hash value of a new row's partition key is `50`. Which partition receives the row?

a) `p2`
b) `p1`
c) `p3`
d) `p0`

**Key: a**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 50 by 4: 12 with remainder 2. 2. The partition with remainder 2 is `p2`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 24. seed 27147277209162252, level 1

A range-partitioned table has `p0` `FROM (0) TO (150)`, `p1` `FROM (150) TO (300)`, `p2` `FROM (300) TO (350)`, `p3` `FROM (350) TO (500)`. Which partition gets `id = 300`?

a) `p3`
b) `p2`
c) `p0`
d) `p1`

**Key: b**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 300. 2. `p2` covers 300 up to but not including 350, and 300 <= 300 < 350. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 25. seed 788161690286589315, level 2

A table is hash partitioned with modulus 5: `p0` to `p4` take remainders 0 to 4. The hash value of a new row's partition key is `66`. Which partition receives the row?

a) `p2`
b) `p0`
c) `p1`
d) `p3`

**Key: c**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 66 by 5: 13 with remainder 1. 2. The partition with remainder 1 is `p1`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 26. seed 2140103312597845824, level 1

A range-partitioned table has `p0` `FROM (100) TO (150)`, `p1` `FROM (150) TO (200)`, `p2` `FROM (200) TO (350)`, `p3` `FROM (350) TO (450)`. Which partition gets `id = 200`?

a) `p3`
b) `p1`
c) `p2`
d) `p0`

**Key: c**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 200. 2. `p2` covers 200 up to but not including 350, and 200 <= 200 < 350. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 27. seed 3075133477688060511, level 2

A table is hash partitioned with modulus 5: `p0` to `p4` take remainders 0 to 4. The hash value of a new row's partition key is `39`. Which partition receives the row?

a) `p2`
b) `p0`
c) `p3`
d) `p4`

**Key: d**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 39 by 5: 7 with remainder 4. 2. The partition with remainder 4 is `p4`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 28. seed 1945308972888116209, level 2

A table is hash partitioned with modulus 6: `p0` to `p5` take remainders 0 to 5. The hash value of a new row's partition key is `32`. Which partition receives the row?

a) `p4`
b) `p2`
c) `p3`
d) `p5`

**Key: b**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 32 by 6: 5 with remainder 2. 2. The partition with remainder 2 is `p2`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 29. seed 3821719049829450032, level 1

A range-partitioned table has `p0` `FROM (100) TO (200)`, `p1` `FROM (200) TO (300)`, `p2` `FROM (300) TO (450)`, `p3` `FROM (450) TO (600)`. Which partition gets `id = 300`?

a) `p3`
b) `p2`
c) `p1`
d) `p0`

**Key: b**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 300. 2. `p2` covers 300 up to but not including 450, and 300 <= 300 < 450. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 30. seed 3067899410436651809, level 1

A range-partitioned table has `p0` `FROM (100) TO (200)`, `p1` `FROM (200) TO (250)`, `p2` `FROM (250) TO (350)`, `p3` `FROM (350) TO (400)`, `p4` `FROM (400) TO (500)`. Which partition gets `id = 250`?

a) `p0`
b) `p2`
c) `p1`
d) `p3`

**Key: b**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 250. 2. `p2` covers 250 up to but not including 350, and 250 <= 250 < 350. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 31. seed 1823942022414289941, level 1

A range-partitioned table has `p0` `FROM (0) TO (50)`, `p1` `FROM (50) TO (150)`, `p2` `FROM (150) TO (250)`, `p3` `FROM (250) TO (300)`, `p4` `FROM (300) TO (450)`. Which partition gets `id = 250`?

a) `p4`
b) `p0`
c) `p3`
d) `p2`

**Key: c**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 250. 2. `p3` covers 250 up to but not including 300, and 250 <= 250 < 300. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 32. seed 4053533946673328751, level 1

A range-partitioned table has `p0` `FROM (100) TO (200)`, `p1` `FROM (200) TO (300)`, `p2` `FROM (300) TO (400)`, `p3` `FROM (400) TO (450)`, `p4` `FROM (450) TO (600)`. Which partition gets `id = 300`?

a) `p0`
b) `p2`
c) `p1`
d) `p3`

**Key: b**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 300. 2. `p2` covers 300 up to but not including 400, and 300 <= 300 < 400. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 33. seed 2558186971492378982, level 2

A table is hash partitioned with modulus 7: `p0` to `p6` take remainders 0 to 6. The hash value of a new row's partition key is `35`. Which partition receives the row?

a) `p5`
b) `p6`
c) `p1`
d) `p0`

**Key: d**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 35 by 7: 5 with remainder 0. 2. The partition with remainder 0 is `p0`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 34. seed 1802242903930031644, level 1

A range-partitioned table has `p0` `FROM (0) TO (150)`, `p1` `FROM (150) TO (250)`, `p2` `FROM (250) TO (350)`, `p3` `FROM (350) TO (500)`, `p4` `FROM (500) TO (550)`. Which partition gets `id = 250`?

a) `p3`
b) `p2`
c) `p0`
d) `p1`

**Key: b**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 250. 2. `p2` covers 250 up to but not including 350, and 250 <= 250 < 350. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 35. seed 1877414013603015471, level 2

A table is hash partitioned with modulus 7: `p0` to `p6` take remainders 0 to 6. The hash value of a new row's partition key is `30`. Which partition receives the row?

a) `p4`
b) `p2`
c) `p6`
d) `p3`

**Key: b**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 30 by 7: 4 with remainder 2. 2. The partition with remainder 2 is `p2`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 36. seed 2960254872356203514, level 2

A table is hash partitioned with modulus 5: `p0` to `p4` take remainders 0 to 4. The hash value of a new row's partition key is `85`. Which partition receives the row?

a) `p2`
b) `p1`
c) `p4`
d) `p0`

**Key: d**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 85 by 5: 17 with remainder 0. 2. The partition with remainder 0 is `p0`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 37. seed 198572819315074495, level 2

A table is hash partitioned with modulus 6: `p0` to `p5` take remainders 0 to 5. The hash value of a new row's partition key is `88`. Which partition receives the row?

a) `p5`
b) `p1`
c) `p2`
d) `p4`

**Key: d**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 88 by 6: 14 with remainder 4. 2. The partition with remainder 4 is `p4`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 38. seed 2787468012976552683, level 1

A range-partitioned table has `p0` `FROM (0) TO (100)`, `p1` `FROM (100) TO (200)`, `p2` `FROM (200) TO (350)`, `p3` `FROM (350) TO (500)`, `p4` `FROM (500) TO (550)`. Which partition gets `id = 350`?

a) `p4`
b) `p2`
c) `p0`
d) `p3`

**Key: d**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 350. 2. `p3` covers 350 up to but not including 500, and 350 <= 350 < 500. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 39. seed 3390305458687932057, level 2

A table is hash partitioned with modulus 5: `p0` to `p4` take remainders 0 to 4. The hash value of a new row's partition key is `50`. Which partition receives the row?

a) `p4`
b) `p1`
c) `p2`
d) `p0`

**Key: d**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 50 by 5: 10 with remainder 0. 2. The partition with remainder 0 is `p0`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 40. seed 3432765286116989529, level 2

A table is hash partitioned with modulus 7: `p0` to `p6` take remainders 0 to 6. The hash value of a new row's partition key is `75`. Which partition receives the row?

a) `p3`
b) `p1`
c) `p6`
d) `p5`

**Key: d**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 75 by 7: 10 with remainder 5. 2. The partition with remainder 5 is `p5`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 41. seed 4345142805849352783, level 2

A table is hash partitioned with modulus 6: `p0` to `p5` take remainders 0 to 5. The hash value of a new row's partition key is `28`. Which partition receives the row?

a) `p4`
b) `p5`
c) `p1`
d) `p0`

**Key: a**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 28 by 6: 4 with remainder 4. 2. The partition with remainder 4 is `p4`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 42. seed 3348539546293543800, level 1

A range-partitioned table has `p0` `FROM (0) TO (150)`, `p1` `FROM (150) TO (200)`, `p2` `FROM (200) TO (350)`, `p3` `FROM (350) TO (400)`. Which partition gets `id = 200`?

a) `p0`
b) `p3`
c) `p1`
d) `p2`

**Key: d**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 200. 2. `p2` covers 200 up to but not including 350, and 200 <= 200 < 350. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 43. seed 1256760209802829216, level 1

A range-partitioned table has `p0` `FROM (100) TO (250)`, `p1` `FROM (250) TO (400)`, `p2` `FROM (400) TO (450)`, `p3` `FROM (450) TO (600)`, `p4` `FROM (600) TO (750)`. Which partition gets `id = 400`?

a) `p2`
b) `p3`
c) `p1`
d) `p0`

**Key: a**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 400. 2. `p2` covers 400 up to but not including 450, and 400 <= 400 < 450. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 44. seed 3215255037657118205, level 2

A table is hash partitioned with modulus 6: `p0` to `p5` take remainders 0 to 5. The hash value of a new row's partition key is `90`. Which partition receives the row?

a) `p1`
b) `p0`
c) `p5`
d) `p3`

**Key: b**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 90 by 6: 15 with remainder 0. 2. The partition with remainder 0 is `p0`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 45. seed 123487095123633444, level 1

A range-partitioned table has `p0` `FROM (100) TO (250)`, `p1` `FROM (250) TO (400)`, `p2` `FROM (400) TO (550)`, `p3` `FROM (550) TO (650)`, `p4` `FROM (650) TO (800)`. Which partition gets `id = 400`?

a) `p3`
b) `p0`
c) `p2`
d) `p1`

**Key: c**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 400. 2. `p2` covers 400 up to but not including 550, and 400 <= 400 < 550. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 46. seed 1033113853671244515, level 2

A table is hash partitioned with modulus 7: `p0` to `p6` take remainders 0 to 6. The hash value of a new row's partition key is `43`. Which partition receives the row?

a) `p5`
b) `p2`
c) `p1`
d) `p6`

**Key: c**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 43 by 7: 6 with remainder 1. 2. The partition with remainder 1 is `p1`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 47. seed 1613085367130624930, level 1

A range-partitioned table has `p0` `FROM (0) TO (150)`, `p1` `FROM (150) TO (300)`, `p2` `FROM (300) TO (450)`, `p3` `FROM (450) TO (500)`. Which partition gets `id = 300`?

a) `p1`
b) `p3`
c) `p0`
d) `p2`

**Key: d**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 300. 2. `p2` covers 300 up to but not including 450, and 300 <= 300 < 450. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 48. seed 2029817522674349104, level 2

A table is hash partitioned with modulus 7: `p0` to `p6` take remainders 0 to 6. The hash value of a new row's partition key is `90`. Which partition receives the row?

a) `p0`
b) `p5`
c) `p2`
d) `p6`

**Key: d**

Explanation: A hash partition holds the rows whose hash value divided by the modulus leaves its remainder. 1. Divide 90 by 7: 12 with remainder 6. 2. The partition with remainder 6 is `p6`. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 49. seed 2428946379055677099, level 1

A range-partitioned table has `p0` `FROM (0) TO (50)`, `p1` `FROM (50) TO (200)`, `p2` `FROM (200) TO (300)`, `p3` `FROM (300) TO (450)`, `p4` `FROM (450) TO (600)`. Which partition gets `id = 300`?

a) `p0`
b) `p4`
c) `p2`
d) `p3`

**Key: d**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 300. 2. `p3` covers 300 up to but not including 450, and 300 <= 300 < 450. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.

## 50. seed 3573171442302920672, level 1

A range-partitioned table has `p0` `FROM (0) TO (50)`, `p1` `FROM (50) TO (200)`, `p2` `FROM (200) TO (300)`, `p3` `FROM (300) TO (450)`. Which partition gets `id = 200`?

a) `p1`
b) `p2`
c) `p3`
d) `p0`

**Key: b**

Explanation: A range partition holds the keys from its lower bound, inclusive, up to its upper bound, exclusive, so `TO (n)` excludes n and the next partition starts at n. 1. The key is 200. 2. `p2` covers 200 up to but not including 300, and 200 <= 200 < 300. 3. A key equal to a bound belongs to the partition that starts there. Source: `pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW`.
