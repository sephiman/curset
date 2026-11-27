# Tumbling windows and grace periods (`stream-window-grace`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 114797670421468702, level 1

Kafka Streams aggregates a topic in tumbling windows of 10 minutes, aligned to the epoch. A record carries the timestamp 10:29. Which window does it belong to?

a) 10:10 to 10:20
b) 10:29 to 10:39
c) 10:20 to 10:30
d) 10:30 to 10:40

**Key: c**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 10 minutes, timestamp 10:29. Step 1: the start is the timestamp rounded down to a multiple of 10 minutes, which is 10:20. Step 2: the end is 10:20 + 10 minutes = 10:30. Result: 10:20 to 10:30. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 2. seed 1181659767179255957, level 2

A Kafka Streams aggregation uses tumbling windows of 15 minutes with a grace period of 15 minutes. Stream time, the largest timestamp seen so far, is 10:40. A record arrives with the timestamp 10:27. What happens to it?

a) Rejected: the 10:00 to 10:15 window closes at 10:30
b) Accepted: the 10:15 to 10:30 window closes at 10:45
c) Rejected: the 10:15 to 10:30 window closes at 10:30
d) Accepted: the 10:30 to 10:45 window closes at 11:00

**Key: b**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 15 minutes, grace 15 minutes, timestamp 10:27, stream time 10:40. Step 1: the record belongs to the 10:15 to 10:30 window. Step 2: the window closes at 10:30 + 15 minutes = 10:45. Step 3: stream time 10:40 is before 10:45. Result: the record is accepted. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 3. seed 1709241085975640876, level 2

A Kafka Streams aggregation uses tumbling windows of 5 minutes with a grace period of 15 minutes. Stream time, the largest timestamp seen so far, is 15:01. A record arrives with the timestamp 14:37. What happens to it?

a) Rejected: the 14:30 to 14:35 window closes at 14:50
b) Rejected: the 14:37 to 14:42 window closes at 14:57
c) Rejected: the 14:35 to 14:40 window closes at 14:55
d) Rejected: the 14:40 to 14:45 window closes at 15:00

**Key: c**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 5 minutes, grace 15 minutes, timestamp 14:37, stream time 15:01. Step 1: the record belongs to the 14:35 to 14:40 window. Step 2: the window closes at 14:40 + 15 minutes = 14:55. Step 3: stream time 15:01 is after 14:55. Result: the record is rejected. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 4. seed 4323989966484647951, level 2

A Kafka Streams aggregation uses tumbling windows of 5 minutes with a grace period of 10 minutes. Stream time, the largest timestamp seen so far, is 09:32. A record arrives with the timestamp 09:06. What happens to it?

a) Rejected: the 09:00 to 09:05 window closes at 09:15
b) Rejected: the 09:05 to 09:10 window closes at 09:20
c) Rejected: the 09:06 to 09:11 window closes at 09:21
d) Rejected: the 09:10 to 09:15 window closes at 09:25

**Key: b**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 5 minutes, grace 10 minutes, timestamp 09:06, stream time 09:32. Step 1: the record belongs to the 09:05 to 09:10 window. Step 2: the window closes at 09:10 + 10 minutes = 09:20. Step 3: stream time 09:32 is after 09:20. Result: the record is rejected. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 5. seed 918020575091681469, level 2

A Kafka Streams aggregation uses tumbling windows of 15 minutes with a grace period of 15 minutes. Stream time, the largest timestamp seen so far, is 09:41. A record arrives with the timestamp 09:28. What happens to it?

a) Rejected: the 09:15 to 09:30 window closes at 09:30
b) Accepted: the 09:30 to 09:45 window closes at 10:00
c) Accepted: the 09:15 to 09:30 window closes at 09:45
d) Rejected: the 09:00 to 09:15 window closes at 09:30

**Key: c**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 15 minutes, grace 15 minutes, timestamp 09:28, stream time 09:41. Step 1: the record belongs to the 09:15 to 09:30 window. Step 2: the window closes at 09:30 + 15 minutes = 09:45. Step 3: stream time 09:41 is before 09:45. Result: the record is accepted. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 6. seed 301631894187761399, level 1

Kafka Streams aggregates a topic in tumbling windows of 30 minutes, aligned to the epoch. A record carries the timestamp 14:48. Which window does it belong to?

a) 14:00 to 14:30
b) 14:48 to 15:18
c) 14:30 to 15:00
d) 15:00 to 15:30

**Key: c**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 30 minutes, timestamp 14:48. Step 1: the start is the timestamp rounded down to a multiple of 30 minutes, which is 14:30. Step 2: the end is 14:30 + 30 minutes = 15:00. Result: 14:30 to 15:00. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 7. seed 432280470411791534, level 2

A Kafka Streams aggregation uses tumbling windows of 30 minutes with a grace period of 15 minutes. Stream time, the largest timestamp seen so far, is 11:28. A record arrives with the timestamp 10:34. What happens to it?

a) Rejected: the 10:30 to 11:00 window closes at 11:15
b) Rejected: the 10:00 to 10:30 window closes at 10:45
c) Accepted: the 11:00 to 11:30 window closes at 11:45
d) Rejected: the 10:34 to 11:04 window closes at 11:19

**Key: a**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 30 minutes, grace 15 minutes, timestamp 10:34, stream time 11:28. Step 1: the record belongs to the 10:30 to 11:00 window. Step 2: the window closes at 11:00 + 15 minutes = 11:15. Step 3: stream time 11:28 is after 11:15. Result: the record is rejected. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 8. seed 1225291041398127068, level 1

Kafka Streams aggregates a topic in tumbling windows of 15 minutes, aligned to the epoch. A record carries the timestamp 11:02. Which window does it belong to?

a) 11:02 to 11:17
b) 10:45 to 11:00
c) 11:15 to 11:30
d) 11:00 to 11:15

**Key: d**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 15 minutes, timestamp 11:02. Step 1: the start is the timestamp rounded down to a multiple of 15 minutes, which is 11:00. Step 2: the end is 11:00 + 15 minutes = 11:15. Result: 11:00 to 11:15. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 9. seed 2893181477739294353, level 2

A Kafka Streams aggregation uses tumbling windows of 15 minutes with a grace period of 10 minutes. Stream time, the largest timestamp seen so far, is 14:56. A record arrives with the timestamp 14:38. What happens to it?

a) Accepted: the 14:45 to 15:00 window closes at 15:10
b) Accepted: the 14:38 to 14:53 window closes at 15:03
c) Rejected: the 14:30 to 14:45 window closes at 14:55
d) Rejected: the 14:15 to 14:30 window closes at 14:40

**Key: c**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 15 minutes, grace 10 minutes, timestamp 14:38, stream time 14:56. Step 1: the record belongs to the 14:30 to 14:45 window. Step 2: the window closes at 14:45 + 10 minutes = 14:55. Step 3: stream time 14:56 is after 14:55. Result: the record is rejected. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 10. seed 4179596566067244310, level 2

A Kafka Streams aggregation uses tumbling windows of 5 minutes with a grace period of 5 minutes. Stream time, the largest timestamp seen so far, is 14:58. A record arrives with the timestamp 14:52. What happens to it?

a) Rejected: the 14:45 to 14:50 window closes at 14:55
b) Accepted: the 14:52 to 14:57 window closes at 15:02
c) Accepted: the 14:50 to 14:55 window closes at 15:00
d) Rejected: the 14:50 to 14:55 window closes at 14:55

**Key: c**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 5 minutes, grace 5 minutes, timestamp 14:52, stream time 14:58. Step 1: the record belongs to the 14:50 to 14:55 window. Step 2: the window closes at 14:55 + 5 minutes = 15:00. Step 3: stream time 14:58 is before 15:00. Result: the record is accepted. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 11. seed 2712951434583675938, level 1

Kafka Streams aggregates a topic in tumbling windows of 15 minutes, aligned to the epoch. A record carries the timestamp 09:24. Which window does it belong to?

a) 09:30 to 09:45
b) 09:00 to 09:15
c) 09:15 to 09:30
d) 09:24 to 09:39

**Key: c**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 15 minutes, timestamp 09:24. Step 1: the start is the timestamp rounded down to a multiple of 15 minutes, which is 09:15. Step 2: the end is 09:15 + 15 minutes = 09:30. Result: 09:15 to 09:30. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 12. seed 2689951047224333461, level 1

Kafka Streams aggregates a topic in tumbling windows of 10 minutes, aligned to the epoch. A record carries the timestamp 14:21. Which window does it belong to?

a) 14:30 to 14:40
b) 14:10 to 14:20
c) 14:20 to 14:30
d) 14:21 to 14:31

**Key: c**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 10 minutes, timestamp 14:21. Step 1: the start is the timestamp rounded down to a multiple of 10 minutes, which is 14:20. Step 2: the end is 14:20 + 10 minutes = 14:30. Result: 14:20 to 14:30. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 13. seed 3823887628635379771, level 1

Kafka Streams aggregates a topic in tumbling windows of 15 minutes, aligned to the epoch. A record carries the timestamp 09:37. Which window does it belong to?

a) 09:15 to 09:30
b) 09:45 to 10:00
c) 09:37 to 09:52
d) 09:30 to 09:45

**Key: d**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 15 minutes, timestamp 09:37. Step 1: the start is the timestamp rounded down to a multiple of 15 minutes, which is 09:30. Step 2: the end is 09:30 + 15 minutes = 09:45. Result: 09:30 to 09:45. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 14. seed 2724073702284232092, level 1

Kafka Streams aggregates a topic in tumbling windows of 10 minutes, aligned to the epoch. A record carries the timestamp 10:02. Which window does it belong to?

a) 10:02 to 10:12
b) 10:10 to 10:20
c) 09:50 to 10:00
d) 10:00 to 10:10

**Key: d**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 10 minutes, timestamp 10:02. Step 1: the start is the timestamp rounded down to a multiple of 10 minutes, which is 10:00. Step 2: the end is 10:00 + 10 minutes = 10:10. Result: 10:00 to 10:10. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 15. seed 2865191641698900645, level 1

Kafka Streams aggregates a topic in tumbling windows of 10 minutes, aligned to the epoch. A record carries the timestamp 14:09. Which window does it belong to?

a) 14:00 to 14:10
b) 14:10 to 14:20
c) 14:09 to 14:19
d) 13:50 to 14:00

**Key: a**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 10 minutes, timestamp 14:09. Step 1: the start is the timestamp rounded down to a multiple of 10 minutes, which is 14:00. Step 2: the end is 14:00 + 10 minutes = 14:10. Result: 14:00 to 14:10. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 16. seed 1434105873481173787, level 2

A Kafka Streams aggregation uses tumbling windows of 15 minutes with a grace period of 15 minutes. Stream time, the largest timestamp seen so far, is 10:56. A record arrives with the timestamp 10:38. What happens to it?

a) Accepted: the 10:30 to 10:45 window closes at 11:00
b) Rejected: the 10:15 to 10:30 window closes at 10:45
c) Rejected: the 10:30 to 10:45 window closes at 10:45
d) Accepted: the 10:38 to 10:53 window closes at 11:08

**Key: a**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 15 minutes, grace 15 minutes, timestamp 10:38, stream time 10:56. Step 1: the record belongs to the 10:30 to 10:45 window. Step 2: the window closes at 10:45 + 15 minutes = 11:00. Step 3: stream time 10:56 is before 11:00. Result: the record is accepted. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 17. seed 86017674429915095, level 1

Kafka Streams aggregates a topic in tumbling windows of 5 minutes, aligned to the epoch. A record carries the timestamp 14:17. Which window does it belong to?

a) 14:10 to 14:15
b) 14:17 to 14:22
c) 14:20 to 14:25
d) 14:15 to 14:20

**Key: d**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 5 minutes, timestamp 14:17. Step 1: the start is the timestamp rounded down to a multiple of 5 minutes, which is 14:15. Step 2: the end is 14:15 + 5 minutes = 14:20. Result: 14:15 to 14:20. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 18. seed 3128569096322552069, level 2

A Kafka Streams aggregation uses tumbling windows of 10 minutes with a grace period of 10 minutes. Stream time, the largest timestamp seen so far, is 11:09. A record arrives with the timestamp 10:51. What happens to it?

a) Accepted: the 10:50 to 11:00 window closes at 11:10
b) Accepted: the 11:00 to 11:10 window closes at 11:20
c) Accepted: the 10:51 to 11:01 window closes at 11:11
d) Rejected: the 10:50 to 11:00 window closes at 11:00

**Key: a**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 10 minutes, grace 10 minutes, timestamp 10:51, stream time 11:09. Step 1: the record belongs to the 10:50 to 11:00 window. Step 2: the window closes at 11:00 + 10 minutes = 11:10. Step 3: stream time 11:09 is before 11:10. Result: the record is accepted. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 19. seed 110471141514028623, level 1

Kafka Streams aggregates a topic in tumbling windows of 10 minutes, aligned to the epoch. A record carries the timestamp 10:15. Which window does it belong to?

a) 10:10 to 10:20
b) 10:15 to 10:25
c) 10:00 to 10:10
d) 10:20 to 10:30

**Key: a**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 10 minutes, timestamp 10:15. Step 1: the start is the timestamp rounded down to a multiple of 10 minutes, which is 10:10. Step 2: the end is 10:10 + 10 minutes = 10:20. Result: 10:10 to 10:20. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 20. seed 651559179360043035, level 2

A Kafka Streams aggregation uses tumbling windows of 10 minutes with a grace period of 5 minutes. Stream time, the largest timestamp seen so far, is 11:17. A record arrives with the timestamp 10:52. What happens to it?

a) Rejected: the 10:50 to 11:00 window closes at 11:05
b) Rejected: the 10:52 to 11:02 window closes at 11:07
c) Rejected: the 11:00 to 11:10 window closes at 11:15
d) Rejected: the 10:40 to 10:50 window closes at 10:55

**Key: a**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 10 minutes, grace 5 minutes, timestamp 10:52, stream time 11:17. Step 1: the record belongs to the 10:50 to 11:00 window. Step 2: the window closes at 11:00 + 5 minutes = 11:05. Step 3: stream time 11:17 is after 11:05. Result: the record is rejected. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 21. seed 3339559911923126949, level 2

A Kafka Streams aggregation uses tumbling windows of 30 minutes with a grace period of 10 minutes. Stream time, the largest timestamp seen so far, is 09:46. A record arrives with the timestamp 09:20. What happens to it?

a) Rejected: the 09:00 to 09:30 window closes at 09:40
b) Accepted: the 09:30 to 10:00 window closes at 10:10
c) Accepted: the 09:20 to 09:50 window closes at 10:00
d) Rejected: the 08:30 to 09:00 window closes at 09:10

**Key: a**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 30 minutes, grace 10 minutes, timestamp 09:20, stream time 09:46. Step 1: the record belongs to the 09:00 to 09:30 window. Step 2: the window closes at 09:30 + 10 minutes = 09:40. Step 3: stream time 09:46 is after 09:40. Result: the record is rejected. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 22. seed 4473575785307301502, level 1

Kafka Streams aggregates a topic in tumbling windows of 10 minutes, aligned to the epoch. A record carries the timestamp 10:14. Which window does it belong to?

a) 10:10 to 10:20
b) 10:00 to 10:10
c) 10:20 to 10:30
d) 10:14 to 10:24

**Key: a**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 10 minutes, timestamp 10:14. Step 1: the start is the timestamp rounded down to a multiple of 10 minutes, which is 10:10. Step 2: the end is 10:10 + 10 minutes = 10:20. Result: 10:10 to 10:20. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 23. seed 4234419502884410777, level 1

Kafka Streams aggregates a topic in tumbling windows of 15 minutes, aligned to the epoch. A record carries the timestamp 09:40. Which window does it belong to?

a) 09:15 to 09:30
b) 09:40 to 09:55
c) 09:45 to 10:00
d) 09:30 to 09:45

**Key: d**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 15 minutes, timestamp 09:40. Step 1: the start is the timestamp rounded down to a multiple of 15 minutes, which is 09:30. Step 2: the end is 09:30 + 15 minutes = 09:45. Result: 09:30 to 09:45. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 24. seed 1194281228484191711, level 1

Kafka Streams aggregates a topic in tumbling windows of 5 minutes, aligned to the epoch. A record carries the timestamp 09:48. Which window does it belong to?

a) 09:45 to 09:50
b) 09:50 to 09:55
c) 09:48 to 09:53
d) 09:40 to 09:45

**Key: a**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 5 minutes, timestamp 09:48. Step 1: the start is the timestamp rounded down to a multiple of 5 minutes, which is 09:45. Step 2: the end is 09:45 + 5 minutes = 09:50. Result: 09:45 to 09:50. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 25. seed 3931023993248023987, level 2

A Kafka Streams aggregation uses tumbling windows of 5 minutes with a grace period of 15 minutes. Stream time, the largest timestamp seen so far, is 14:33. A record arrives with the timestamp 14:18. What happens to it?

a) Accepted: the 14:15 to 14:20 window closes at 14:35
b) Rejected: the 14:15 to 14:20 window closes at 14:20
c) Rejected: the 14:10 to 14:15 window closes at 14:30
d) Accepted: the 14:20 to 14:25 window closes at 14:40

**Key: a**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 5 minutes, grace 15 minutes, timestamp 14:18, stream time 14:33. Step 1: the record belongs to the 14:15 to 14:20 window. Step 2: the window closes at 14:20 + 15 minutes = 14:35. Step 3: stream time 14:33 is before 14:35. Result: the record is accepted. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 26. seed 1290895305899877534, level 1

Kafka Streams aggregates a topic in tumbling windows of 30 minutes, aligned to the epoch. A record carries the timestamp 09:10. Which window does it belong to?

a) 09:30 to 10:00
b) 09:10 to 09:40
c) 08:30 to 09:00
d) 09:00 to 09:30

**Key: d**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 30 minutes, timestamp 09:10. Step 1: the start is the timestamp rounded down to a multiple of 30 minutes, which is 09:00. Step 2: the end is 09:00 + 30 minutes = 09:30. Result: 09:00 to 09:30. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 27. seed 1441297532272219034, level 2

A Kafka Streams aggregation uses tumbling windows of 10 minutes with a grace period of 10 minutes. Stream time, the largest timestamp seen so far, is 10:49. A record arrives with the timestamp 10:23. What happens to it?

a) Rejected: the 10:23 to 10:33 window closes at 10:43
b) Rejected: the 10:20 to 10:30 window closes at 10:40
c) Accepted: the 10:30 to 10:40 window closes at 10:50
d) Rejected: the 10:10 to 10:20 window closes at 10:30

**Key: b**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 10 minutes, grace 10 minutes, timestamp 10:23, stream time 10:49. Step 1: the record belongs to the 10:20 to 10:30 window. Step 2: the window closes at 10:30 + 10 minutes = 10:40. Step 3: stream time 10:49 is after 10:40. Result: the record is rejected. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 28. seed 1647723508388743285, level 1

Kafka Streams aggregates a topic in tumbling windows of 10 minutes, aligned to the epoch. A record carries the timestamp 09:23. Which window does it belong to?

a) 09:10 to 09:20
b) 09:30 to 09:40
c) 09:20 to 09:30
d) 09:23 to 09:33

**Key: c**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 10 minutes, timestamp 09:23. Step 1: the start is the timestamp rounded down to a multiple of 10 minutes, which is 09:20. Step 2: the end is 09:20 + 10 minutes = 09:30. Result: 09:20 to 09:30. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 29. seed 827105697718844277, level 2

A Kafka Streams aggregation uses tumbling windows of 10 minutes with a grace period of 5 minutes. Stream time, the largest timestamp seen so far, is 10:33. A record arrives with the timestamp 10:13. What happens to it?

a) Rejected: the 10:10 to 10:20 window closes at 10:25
b) Rejected: the 10:00 to 10:10 window closes at 10:15
c) Accepted: the 10:20 to 10:30 window closes at 10:35
d) Rejected: the 10:13 to 10:23 window closes at 10:28

**Key: a**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 10 minutes, grace 5 minutes, timestamp 10:13, stream time 10:33. Step 1: the record belongs to the 10:10 to 10:20 window. Step 2: the window closes at 10:20 + 5 minutes = 10:25. Step 3: stream time 10:33 is after 10:25. Result: the record is rejected. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 30. seed 3618576014416948019, level 1

Kafka Streams aggregates a topic in tumbling windows of 15 minutes, aligned to the epoch. A record carries the timestamp 09:21. Which window does it belong to?

a) 09:15 to 09:30
b) 09:00 to 09:15
c) 09:21 to 09:36
d) 09:30 to 09:45

**Key: a**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 15 minutes, timestamp 09:21. Step 1: the start is the timestamp rounded down to a multiple of 15 minutes, which is 09:15. Step 2: the end is 09:15 + 15 minutes = 09:30. Result: 09:15 to 09:30. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 31. seed 1623391521467063426, level 1

Kafka Streams aggregates a topic in tumbling windows of 30 minutes, aligned to the epoch. A record carries the timestamp 14:46. Which window does it belong to?

a) 15:00 to 15:30
b) 14:46 to 15:16
c) 14:00 to 14:30
d) 14:30 to 15:00

**Key: d**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 30 minutes, timestamp 14:46. Step 1: the start is the timestamp rounded down to a multiple of 30 minutes, which is 14:30. Step 2: the end is 14:30 + 30 minutes = 15:00. Result: 14:30 to 15:00. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 32. seed 486580609470007142, level 1

Kafka Streams aggregates a topic in tumbling windows of 30 minutes, aligned to the epoch. A record carries the timestamp 10:39. Which window does it belong to?

a) 10:30 to 11:00
b) 10:39 to 11:09
c) 10:00 to 10:30
d) 11:00 to 11:30

**Key: a**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 30 minutes, timestamp 10:39. Step 1: the start is the timestamp rounded down to a multiple of 30 minutes, which is 10:30. Step 2: the end is 10:30 + 30 minutes = 11:00. Result: 10:30 to 11:00. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 33. seed 2636556119516584472, level 1

Kafka Streams aggregates a topic in tumbling windows of 30 minutes, aligned to the epoch. A record carries the timestamp 14:50. Which window does it belong to?

a) 14:50 to 15:20
b) 15:00 to 15:30
c) 14:30 to 15:00
d) 14:00 to 14:30

**Key: c**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 30 minutes, timestamp 14:50. Step 1: the start is the timestamp rounded down to a multiple of 30 minutes, which is 14:30. Step 2: the end is 14:30 + 30 minutes = 15:00. Result: 14:30 to 15:00. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 34. seed 4501981102965968890, level 2

A Kafka Streams aggregation uses tumbling windows of 30 minutes with a grace period of 15 minutes. Stream time, the largest timestamp seen so far, is 10:41. A record arrives with the timestamp 10:03. What happens to it?

a) Accepted: the 10:30 to 11:00 window closes at 11:15
b) Accepted: the 10:00 to 10:30 window closes at 10:45
c) Rejected: the 10:00 to 10:30 window closes at 10:30
d) Accepted: the 10:03 to 10:33 window closes at 10:48

**Key: b**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 30 minutes, grace 15 minutes, timestamp 10:03, stream time 10:41. Step 1: the record belongs to the 10:00 to 10:30 window. Step 2: the window closes at 10:30 + 15 minutes = 10:45. Step 3: stream time 10:41 is before 10:45. Result: the record is accepted. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 35. seed 2768385981304396532, level 2

A Kafka Streams aggregation uses tumbling windows of 10 minutes with a grace period of 5 minutes. Stream time, the largest timestamp seen so far, is 09:57. A record arrives with the timestamp 09:38. What happens to it?

a) Rejected: the 09:40 to 09:50 window closes at 09:55
b) Rejected: the 09:30 to 09:40 window closes at 09:45
c) Rejected: the 09:38 to 09:48 window closes at 09:53
d) Rejected: the 09:20 to 09:30 window closes at 09:35

**Key: b**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 10 minutes, grace 5 minutes, timestamp 09:38, stream time 09:57. Step 1: the record belongs to the 09:30 to 09:40 window. Step 2: the window closes at 09:40 + 5 minutes = 09:45. Step 3: stream time 09:57 is after 09:45. Result: the record is rejected. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 36. seed 2824192957931356153, level 1

Kafka Streams aggregates a topic in tumbling windows of 5 minutes, aligned to the epoch. A record carries the timestamp 14:41. Which window does it belong to?

a) 14:41 to 14:46
b) 14:35 to 14:40
c) 14:45 to 14:50
d) 14:40 to 14:45

**Key: d**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 5 minutes, timestamp 14:41. Step 1: the start is the timestamp rounded down to a multiple of 5 minutes, which is 14:40. Step 2: the end is 14:40 + 5 minutes = 14:45. Result: 14:40 to 14:45. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 37. seed 2397360571979886757, level 2

A Kafka Streams aggregation uses tumbling windows of 5 minutes with a grace period of 15 minutes. Stream time, the largest timestamp seen so far, is 14:55. A record arrives with the timestamp 14:34. What happens to it?

a) Rejected: the 14:35 to 14:40 window closes at 14:55
b) Rejected: the 14:34 to 14:39 window closes at 14:54
c) Rejected: the 14:30 to 14:35 window closes at 14:50
d) Rejected: the 14:25 to 14:30 window closes at 14:45

**Key: c**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 5 minutes, grace 15 minutes, timestamp 14:34, stream time 14:55. Step 1: the record belongs to the 14:30 to 14:35 window. Step 2: the window closes at 14:35 + 15 minutes = 14:50. Step 3: stream time 14:55 is after 14:50. Result: the record is rejected. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 38. seed 3534641029877829548, level 2

A Kafka Streams aggregation uses tumbling windows of 30 minutes with a grace period of 10 minutes. Stream time, the largest timestamp seen so far, is 10:07. A record arrives with the timestamp 09:34. What happens to it?

a) Accepted: the 10:00 to 10:30 window closes at 10:40
b) Rejected: the 09:00 to 09:30 window closes at 09:40
c) Accepted: the 09:30 to 10:00 window closes at 10:10
d) Accepted: the 09:34 to 10:04 window closes at 10:14

**Key: c**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 30 minutes, grace 10 minutes, timestamp 09:34, stream time 10:07. Step 1: the record belongs to the 09:30 to 10:00 window. Step 2: the window closes at 10:00 + 10 minutes = 10:10. Step 3: stream time 10:07 is before 10:10. Result: the record is accepted. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 39. seed 1637963478771374405, level 2

A Kafka Streams aggregation uses tumbling windows of 10 minutes with a grace period of 15 minutes. Stream time, the largest timestamp seen so far, is 10:47. A record arrives with the timestamp 10:35. What happens to it?

a) Accepted: the 10:40 to 10:50 window closes at 11:05
b) Accepted: the 10:30 to 10:40 window closes at 10:55
c) Rejected: the 10:20 to 10:30 window closes at 10:45
d) Rejected: the 10:30 to 10:40 window closes at 10:40

**Key: b**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 10 minutes, grace 15 minutes, timestamp 10:35, stream time 10:47. Step 1: the record belongs to the 10:30 to 10:40 window. Step 2: the window closes at 10:40 + 15 minutes = 10:55. Step 3: stream time 10:47 is before 10:55. Result: the record is accepted. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 40. seed 1736503083138832182, level 1

Kafka Streams aggregates a topic in tumbling windows of 15 minutes, aligned to the epoch. A record carries the timestamp 14:42. Which window does it belong to?

a) 14:30 to 14:45
b) 14:42 to 14:57
c) 14:45 to 15:00
d) 14:15 to 14:30

**Key: a**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 15 minutes, timestamp 14:42. Step 1: the start is the timestamp rounded down to a multiple of 15 minutes, which is 14:30. Step 2: the end is 14:30 + 15 minutes = 14:45. Result: 14:30 to 14:45. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 41. seed 2989838261974786054, level 1

Kafka Streams aggregates a topic in tumbling windows of 30 minutes, aligned to the epoch. A record carries the timestamp 09:06. Which window does it belong to?

a) 09:06 to 09:36
b) 08:30 to 09:00
c) 09:00 to 09:30
d) 09:30 to 10:00

**Key: c**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 30 minutes, timestamp 09:06. Step 1: the start is the timestamp rounded down to a multiple of 30 minutes, which is 09:00. Step 2: the end is 09:00 + 30 minutes = 09:30. Result: 09:00 to 09:30. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 42. seed 1281759977975510434, level 1

Kafka Streams aggregates a topic in tumbling windows of 15 minutes, aligned to the epoch. A record carries the timestamp 14:28. Which window does it belong to?

a) 14:30 to 14:45
b) 14:00 to 14:15
c) 14:28 to 14:43
d) 14:15 to 14:30

**Key: d**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 15 minutes, timestamp 14:28. Step 1: the start is the timestamp rounded down to a multiple of 15 minutes, which is 14:15. Step 2: the end is 14:15 + 15 minutes = 14:30. Result: 14:15 to 14:30. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 43. seed 2227011881232667408, level 2

A Kafka Streams aggregation uses tumbling windows of 5 minutes with a grace period of 10 minutes. Stream time, the largest timestamp seen so far, is 11:10. A record arrives with the timestamp 10:42. What happens to it?

a) Rejected: the 10:35 to 10:40 window closes at 10:50
b) Rejected: the 10:42 to 10:47 window closes at 10:57
c) Rejected: the 10:40 to 10:45 window closes at 10:55
d) Rejected: the 10:45 to 10:50 window closes at 11:00

**Key: c**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 5 minutes, grace 10 minutes, timestamp 10:42, stream time 11:10. Step 1: the record belongs to the 10:40 to 10:45 window. Step 2: the window closes at 10:45 + 10 minutes = 10:55. Step 3: stream time 11:10 is after 10:55. Result: the record is rejected. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 44. seed 848490071779401489, level 1

Kafka Streams aggregates a topic in tumbling windows of 10 minutes, aligned to the epoch. A record carries the timestamp 14:35. Which window does it belong to?

a) 14:35 to 14:45
b) 14:40 to 14:50
c) 14:20 to 14:30
d) 14:30 to 14:40

**Key: d**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 10 minutes, timestamp 14:35. Step 1: the start is the timestamp rounded down to a multiple of 10 minutes, which is 14:30. Step 2: the end is 14:30 + 10 minutes = 14:40. Result: 14:30 to 14:40. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 45. seed 111964236436270555, level 1

Kafka Streams aggregates a topic in tumbling windows of 15 minutes, aligned to the epoch. A record carries the timestamp 10:18. Which window does it belong to?

a) 10:00 to 10:15
b) 10:30 to 10:45
c) 10:18 to 10:33
d) 10:15 to 10:30

**Key: d**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 15 minutes, timestamp 10:18. Step 1: the start is the timestamp rounded down to a multiple of 15 minutes, which is 10:15. Step 2: the end is 10:15 + 15 minutes = 10:30. Result: 10:15 to 10:30. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 46. seed 1501427231665814530, level 2

A Kafka Streams aggregation uses tumbling windows of 30 minutes with a grace period of 15 minutes. Stream time, the largest timestamp seen so far, is 10:52. A record arrives with the timestamp 10:13. What happens to it?

a) Accepted: the 10:30 to 11:00 window closes at 11:15
b) Rejected: the 10:00 to 10:30 window closes at 10:45
c) Rejected: the 09:30 to 10:00 window closes at 10:15
d) Accepted: the 10:13 to 10:43 window closes at 10:58

**Key: b**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 30 minutes, grace 15 minutes, timestamp 10:13, stream time 10:52. Step 1: the record belongs to the 10:00 to 10:30 window. Step 2: the window closes at 10:30 + 15 minutes = 10:45. Step 3: stream time 10:52 is after 10:45. Result: the record is rejected. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 47. seed 4417733962308700344, level 1

Kafka Streams aggregates a topic in tumbling windows of 15 minutes, aligned to the epoch. A record carries the timestamp 09:28. Which window does it belong to?

a) 09:00 to 09:15
b) 09:15 to 09:30
c) 09:28 to 09:43
d) 09:30 to 09:45

**Key: b**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 15 minutes, timestamp 09:28. Step 1: the start is the timestamp rounded down to a multiple of 15 minutes, which is 09:15. Step 2: the end is 09:15 + 15 minutes = 09:30. Result: 09:15 to 09:30. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 48. seed 546378593668118691, level 1

Kafka Streams aggregates a topic in tumbling windows of 5 minutes, aligned to the epoch. A record carries the timestamp 09:16. Which window does it belong to?

a) 09:20 to 09:25
b) 09:16 to 09:21
c) 09:15 to 09:20
d) 09:10 to 09:15

**Key: c**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 5 minutes, timestamp 09:16. Step 1: the start is the timestamp rounded down to a multiple of 5 minutes, which is 09:15. Step 2: the end is 09:15 + 5 minutes = 09:20. Result: 09:15 to 09:20. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 49. seed 2412945588128550011, level 1

Kafka Streams aggregates a topic in tumbling windows of 10 minutes, aligned to the epoch. A record carries the timestamp 09:35. Which window does it belong to?

a) 09:40 to 09:50
b) 09:35 to 09:45
c) 09:30 to 09:40
d) 09:20 to 09:30

**Key: c**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 10 minutes, timestamp 09:35. Step 1: the start is the timestamp rounded down to a multiple of 10 minutes, which is 09:30. Step 2: the end is 09:30 + 10 minutes = 09:40. Result: 09:30 to 09:40. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.

## 50. seed 2616231778373478176, level 1

Kafka Streams aggregates a topic in tumbling windows of 30 minutes, aligned to the epoch. A record carries the timestamp 10:40. Which window does it belong to?

a) 10:00 to 10:30
b) 11:00 to 11:30
c) 10:30 to 11:00
d) 10:40 to 11:10

**Key: c**

Explanation: Rule: a tumbling window starts on a multiple of its size, includes its start and excludes its end, and accepts records until stream time passes its end plus the grace period. Inputs: size 30 minutes, timestamp 10:40. Step 1: the start is the timestamp rounded down to a multiple of 30 minutes, which is 10:30. Step 2: the end is 10:30 + 30 minutes = 11:00. Result: 10:30 to 11:00. Source: `kafka-streams-dsl-api#tumbling-time-windows`; `kafka-streams-dsl-api#window-final-results`.
