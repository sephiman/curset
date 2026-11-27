# Snowflake id capacity (`snowflake-layout`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 682924790938175705, level 1

5 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 4,096 distinct ids per millisecond
b) 60
c) 20,480 ids
d) 5,120 distinct ids

**Key: c**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `5 × 4,096`. The result is 20,480. Wrong options: 4,096 counts one machine only. 5,120 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 60 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 2. seed 2717443758380483099, level 1

3 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 4,096 distinct ids
b) 3,072
c) 36 ids
d) 12,288 ids in total

**Key: d**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `3 × 4,096`. The result is 12,288. Wrong options: 4,096 counts one machine only. 3,072 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 36 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 3. seed 1465849068792594610, level 1

3 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 36 distinct ids per millisecond
b) 4,096
c) 3,072 ids in one millisecond
d) 12,288

**Key: d**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `3 × 4,096`. The result is 12,288. Wrong options: 4,096 counts one machine only. 3,072 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 36 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 4. seed 2635238217052625525, level 1

3 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 4,096 distinct ids per millisecond
b) 3,072 ids in total
c) 36 ids in one millisecond
d) 12,288 ids in one millisecond

**Key: d**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `3 × 4,096`. The result is 12,288. Wrong options: 4,096 counts one machine only. 3,072 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 36 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 5. seed 837001851055559168, level 1

3 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 12,288 distinct ids
b) 36 ids in total
c) 4,096 distinct ids per millisecond
d) 12,288,000 distinct ids per millisecond

**Key: a**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `3 × 4,096`. The result is 12,288. Wrong options: 4,096 counts one machine only. 36 multiplies by the 12 bits instead of the `2^12` values. 12,288,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 6. seed 1927775344912246260, level 1

6 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 4,096 distinct ids
b) 6,144
c) 24,576 distinct ids per millisecond
d) 24,576,000 ids

**Key: c**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `6 × 4,096`. The result is 24,576. Wrong options: 4,096 counts one machine only. 6,144 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 24,576,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 7. seed 3802749657564170384, level 1

3 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 3,072
b) 12,288 ids in total
c) 36 distinct ids
d) 4,096

**Key: b**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `3 × 4,096`. The result is 12,288. Wrong options: 4,096 counts one machine only. 3,072 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 36 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 8. seed 925627697305630840, level 1

3 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 36 ids in one millisecond
b) 4,096
c) 3,072 ids
d) 12,288 distinct ids per millisecond

**Key: d**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `3 × 4,096`. The result is 12,288. Wrong options: 4,096 counts one machine only. 3,072 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 36 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 9. seed 3831839811043263355, level 1

7 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 28,672,000 ids in one millisecond
b) 84 ids
c) 28,672
d) 4,096 ids

**Key: c**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `7 × 4,096`. The result is 28,672. Wrong options: 4,096 counts one machine only. 84 multiplies by the 12 bits instead of the `2^12` values. 28,672,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 10. seed 3312175715483672802, level 1

7 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 28,672 ids in total
b) 84 distinct ids per millisecond
c) 7,168 distinct ids per millisecond
d) 4,096 ids in one millisecond

**Key: a**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `7 × 4,096`. The result is 28,672. Wrong options: 4,096 counts one machine only. 7,168 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 84 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 11. seed 789291761783585583, level 1

3 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 12,288 distinct ids
b) 3,072 ids in total
c) 4,096 distinct ids
d) 36 ids in one millisecond

**Key: a**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `3 × 4,096`. The result is 12,288. Wrong options: 4,096 counts one machine only. 3,072 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 36 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 12. seed 2243805443266033685, level 1

6 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 24,576 distinct ids per millisecond
b) 24,576,000 ids in total
c) 6,144 distinct ids
d) 72 ids

**Key: a**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `6 × 4,096`. The result is 24,576. Wrong options: 6,144 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 72 multiplies by the 12 bits instead of the `2^12` values. 24,576,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 13. seed 1586296126059724461, level 1

7 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 4,096 ids in one millisecond
b) 28,672
c) 84
d) 7,168 distinct ids

**Key: b**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `7 × 4,096`. The result is 28,672. Wrong options: 4,096 counts one machine only. 7,168 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 84 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 14. seed 2538190274277482908, level 1

6 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 6,144 ids
b) 72 ids in total
c) 24,576 ids
d) 4,096 distinct ids

**Key: c**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `6 × 4,096`. The result is 24,576. Wrong options: 4,096 counts one machine only. 6,144 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 72 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 15. seed 3018491582099900321, level 1

3 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 3,072 distinct ids per millisecond
b) 36 ids
c) 4,096 distinct ids per millisecond
d) 12,288 distinct ids

**Key: d**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `3 × 4,096`. The result is 12,288. Wrong options: 4,096 counts one machine only. 3,072 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 36 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 16. seed 3226562927379995281, level 1

7 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 28,672 ids
b) 7,168 ids in one millisecond
c) 28,672,000 distinct ids per millisecond
d) 84

**Key: a**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `7 × 4,096`. The result is 28,672. Wrong options: 7,168 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 84 multiplies by the 12 bits instead of the `2^12` values. 28,672,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 17. seed 976547028923209572, level 1

6 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 24,576 ids
b) 6,144 distinct ids per millisecond
c) 72 ids
d) 4,096 ids

**Key: a**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `6 × 4,096`. The result is 24,576. Wrong options: 4,096 counts one machine only. 6,144 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 72 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 18. seed 4015291367513143170, level 1

3 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 4,096 ids in total
b) 12,288
c) 3,072 ids
d) 36

**Key: b**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `3 × 4,096`. The result is 12,288. Wrong options: 4,096 counts one machine only. 3,072 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 36 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 19. seed 940648118991253293, level 1

6 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 24,576,000 distinct ids
b) 72 distinct ids
c) 4,096 ids in one millisecond
d) 24,576 distinct ids

**Key: d**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `6 × 4,096`. The result is 24,576. Wrong options: 4,096 counts one machine only. 72 multiplies by the 12 bits instead of the `2^12` values. 24,576,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 20. seed 2557362079535345790, level 1

6 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 6,144 distinct ids
b) 4,096 ids
c) 72 ids
d) 24,576 ids in one millisecond

**Key: d**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `6 × 4,096`. The result is 24,576. Wrong options: 4,096 counts one machine only. 6,144 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 72 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 21. seed 731856034906521647, level 1

6 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 4,096 distinct ids
b) 72 distinct ids per millisecond
c) 24,576 ids in one millisecond
d) 6,144 distinct ids

**Key: c**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `6 × 4,096`. The result is 24,576. Wrong options: 4,096 counts one machine only. 6,144 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 72 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 22. seed 2914510128962355635, level 1

5 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 20,480,000 distinct ids per millisecond
b) 4,096 ids
c) 60 ids
d) 20,480 distinct ids

**Key: d**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `5 × 4,096`. The result is 20,480. Wrong options: 4,096 counts one machine only. 60 multiplies by the 12 bits instead of the `2^12` values. 20,480,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 23. seed 4556852717306796937, level 1

3 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 36 ids in total
b) 3,072 ids in total
c) 12,288 ids in total
d) 4,096 ids in one millisecond

**Key: c**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `3 × 4,096`. The result is 12,288. Wrong options: 4,096 counts one machine only. 3,072 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 36 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 24. seed 2749970542589956363, level 1

6 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 72 distinct ids
b) 4,096
c) 6,144 distinct ids
d) 24,576 ids in one millisecond

**Key: d**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `6 × 4,096`. The result is 24,576. Wrong options: 4,096 counts one machine only. 6,144 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 72 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 25. seed 2692964416358498773, level 1

3 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 36 ids in total
b) 12,288 ids in total
c) 4,096 distinct ids per millisecond
d) 3,072 ids in total

**Key: b**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `3 × 4,096`. The result is 12,288. Wrong options: 4,096 counts one machine only. 3,072 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 36 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 26. seed 3740842409964192585, level 1

5 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 20,480,000 distinct ids per millisecond
b) 4,096
c) 20,480 ids
d) 5,120

**Key: c**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `5 × 4,096`. The result is 20,480. Wrong options: 4,096 counts one machine only. 5,120 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 20,480,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 27. seed 2124658858494137415, level 1

3 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 12,288 distinct ids
b) 3,072 distinct ids
c) 36 distinct ids per millisecond
d) 4,096 ids in one millisecond

**Key: a**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `3 × 4,096`. The result is 12,288. Wrong options: 4,096 counts one machine only. 3,072 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 36 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 28. seed 3304901378420540126, level 1

7 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 7,168 ids in one millisecond
b) 84 ids in one millisecond
c) 4,096 ids in one millisecond
d) 28,672 ids

**Key: d**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `7 × 4,096`. The result is 28,672. Wrong options: 4,096 counts one machine only. 7,168 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 84 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 29. seed 566833287527248539, level 1

6 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 24,576,000 ids in total
b) 24,576 distinct ids per millisecond
c) 4,096 ids in total
d) 6,144 ids in total

**Key: b**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `6 × 4,096`. The result is 24,576. Wrong options: 4,096 counts one machine only. 6,144 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 24,576,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 30. seed 2988355212353268531, level 1

3 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 12,288 distinct ids
b) 3,072 ids in one millisecond
c) 12,288,000 distinct ids per millisecond
d) 36

**Key: a**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `3 × 4,096`. The result is 12,288. Wrong options: 3,072 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 36 multiplies by the 12 bits instead of the `2^12` values. 12,288,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 31. seed 4361274710458372334, level 1

7 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 28,672,000
b) 7,168 distinct ids per millisecond
c) 28,672 ids
d) 84 distinct ids per millisecond

**Key: c**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `7 × 4,096`. The result is 28,672. Wrong options: 7,168 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 84 multiplies by the 12 bits instead of the `2^12` values. 28,672,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 32. seed 2822770028004639852, level 1

5 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 5,120 distinct ids per millisecond
b) 60 distinct ids per millisecond
c) 20,480,000 ids
d) 20,480

**Key: d**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `5 × 4,096`. The result is 20,480. Wrong options: 5,120 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 60 multiplies by the 12 bits instead of the `2^12` values. 20,480,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 33. seed 1327694512884263067, level 1

6 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 4,096 ids
b) 24,576
c) 6,144
d) 24,576,000

**Key: b**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `6 × 4,096`. The result is 24,576. Wrong options: 4,096 counts one machine only. 6,144 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 24,576,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 34. seed 2267922240601568635, level 1

6 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 4,096 distinct ids
b) 24,576
c) 6,144
d) 72 ids in total

**Key: b**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `6 × 4,096`. The result is 24,576. Wrong options: 4,096 counts one machine only. 6,144 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 72 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 35. seed 1017866514784692989, level 1

5 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 5,120 ids
b) 20,480 ids
c) 4,096
d) 60 ids

**Key: b**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `5 × 4,096`. The result is 20,480. Wrong options: 4,096 counts one machine only. 5,120 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 60 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 36. seed 1462700083517179227, level 1

6 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 6,144 distinct ids per millisecond
b) 72 distinct ids per millisecond
c) 24,576 distinct ids per millisecond
d) 24,576,000 ids in total

**Key: c**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `6 × 4,096`. The result is 24,576. Wrong options: 6,144 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 72 multiplies by the 12 bits instead of the `2^12` values. 24,576,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 37. seed 2648486553883214142, level 1

6 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 24,576 distinct ids per millisecond
b) 6,144 distinct ids per millisecond
c) 72 ids
d) 4,096 distinct ids per millisecond

**Key: a**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `6 × 4,096`. The result is 24,576. Wrong options: 4,096 counts one machine only. 6,144 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 72 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 38. seed 2960917444443687438, level 1

7 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 84 ids in one millisecond
b) 4,096 ids
c) 28,672 ids in one millisecond
d) 28,672,000 ids in one millisecond

**Key: c**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `7 × 4,096`. The result is 28,672. Wrong options: 4,096 counts one machine only. 84 multiplies by the 12 bits instead of the `2^12` values. 28,672,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 39. seed 265664538124945365, level 1

3 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 3,072 distinct ids per millisecond
b) 12,288 ids in total
c) 36 ids in one millisecond
d) 12,288,000 ids

**Key: b**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `3 × 4,096`. The result is 12,288. Wrong options: 3,072 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 36 multiplies by the 12 bits instead of the `2^12` values. 12,288,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 40. seed 3836943435537486380, level 1

7 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 28,672 ids in total
b) 7,168
c) 4,096 ids in total
d) 28,672,000 ids in total

**Key: a**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `7 × 4,096`. The result is 28,672. Wrong options: 4,096 counts one machine only. 7,168 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 28,672,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 41. seed 1755575588311881550, level 1

3 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 12,288 ids in one millisecond
b) 3,072 distinct ids per millisecond
c) 4,096 ids in total
d) 36 ids

**Key: a**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `3 × 4,096`. The result is 12,288. Wrong options: 4,096 counts one machine only. 3,072 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 36 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 42. seed 855589079168356381, level 1

7 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 28,672 ids in one millisecond
b) 84 distinct ids
c) 28,672,000 distinct ids per millisecond
d) 4,096

**Key: a**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `7 × 4,096`. The result is 28,672. Wrong options: 4,096 counts one machine only. 84 multiplies by the 12 bits instead of the `2^12` values. 28,672,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 43. seed 1426453049112934960, level 1

5 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 4,096 ids
b) 20,480,000 ids
c) 60 ids
d) 20,480 ids in total

**Key: d**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `5 × 4,096`. The result is 20,480. Wrong options: 4,096 counts one machine only. 60 multiplies by the 12 bits instead of the `2^12` values. 20,480,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 44. seed 3453413024828109989, level 1

6 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 24,576 distinct ids per millisecond
b) 72 distinct ids
c) 4,096 ids
d) 6,144

**Key: a**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `6 × 4,096`. The result is 24,576. Wrong options: 4,096 counts one machine only. 6,144 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 72 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 45. seed 2848025186114303312, level 1

5 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 20,480 ids
b) 4,096 distinct ids
c) 60 distinct ids per millisecond
d) 5,120 ids

**Key: a**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `5 × 4,096`. The result is 20,480. Wrong options: 4,096 counts one machine only. 5,120 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 60 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 46. seed 898473749819486192, level 1

5 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 20,480 distinct ids per millisecond
b) 5,120
c) 60 distinct ids per millisecond
d) 4,096 ids

**Key: a**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `5 × 4,096`. The result is 20,480. Wrong options: 4,096 counts one machine only. 5,120 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 60 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 47. seed 1736984972286719466, level 1

7 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 28,672 distinct ids
b) 84 ids in one millisecond
c) 28,672,000 ids in total
d) 7,168 distinct ids per millisecond

**Key: a**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `7 × 4,096`. The result is 28,672. Wrong options: 7,168 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 84 multiplies by the 12 bits instead of the `2^12` values. 28,672,000 counts a whole second of 1,000 milliseconds. Source: `snowflake-readme#top`.

## 48. seed 4086673436353450571, level 1

3 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 36
b) 12,288 ids in one millisecond
c) 4,096 ids in one millisecond
d) 3,072

**Key: b**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `3 × 4,096`. The result is 12,288. Wrong options: 4,096 counts one machine only. 3,072 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 36 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 49. seed 2898619244922583951, level 1

7 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 28,672 distinct ids
b) 4,096 distinct ids
c) 84 ids in total
d) 7,168 ids in total

**Key: a**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `7 × 4,096`. The result is 28,672. Wrong options: 4,096 counts one machine only. 7,168 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 84 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.

## 50. seed 2484432209050216284, level 1

5 machines run Twitter's 2010 Snowflake, each with its own configured machine id, and each generates as many ids as every millisecond allows. At most how many distinct ids do they produce in one millisecond?

a) 60 distinct ids per millisecond
b) 5,120 distinct ids
c) 4,096 ids
d) 20,480 distinct ids

**Key: d**

Explanation: The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number. Each machine produces at most `2^12` = 4,096 ids in a millisecond, and the machine id keeps the machines apart: `5 × 4,096`. The result is 20,480. Wrong options: 4,096 counts one machine only. 5,120 multiplies by the 10-bit machine field (1,024 values) instead of the sequence number. 60 multiplies by the 12 bits instead of the `2^12` values. Source: `snowflake-readme#top`.
