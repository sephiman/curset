# Kafka offsets and consumer lag (`kafka-consumer-lag`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 879322278347662220, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 13 records are produced; the consumer commits its position; the consumer polls and processes up to 7 records; the consumer polls and processes up to 2 records; the consumer polls and processes up to 7 records; 4 records are produced; the consumer commits its position; the consumer polls and processes up to 6 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `13`, lag `4`
b) committed `14`, lag `3`
c) committed `16`, lag `1`
d) committed `13`, lag `0`

**Key: a**

Explanation: Replaying the events gives log-end offset 17 and position 17. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 13, so lag = 17 - 13 = 4. Records polled after that commit are not committed yet.

## 2. seed 990985166434970943, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 16 records are produced; the consumer polls and processes up to 3 records; the consumer commits its position; the consumer polls and processes up to 3 records; the consumer polls and processes up to 3 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `9`, 0 records read again
b) offset `3`, 6 records read again
c) offset `2`, 7 records read again
d) offset `4`, 5 records read again

**Key: b**

Explanation: Before the crash the position was 9 but the last commit stored 3, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 3 and reads 9 - 3 = 6 records again.

## 3. seed 631533027981635051, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 10 records are produced; 7 records are produced; the consumer polls and processes up to 5 records; the consumer commits its position; the consumer polls and processes up to 2 records; 7 records are produced; the consumer polls and processes up to 5 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `11`, 1 record read again
b) offset `5`, 7 records read again
c) offset `6`, 6 records read again
d) offset `4`, 8 records read again

**Key: b**

Explanation: Before the crash the position was 12 but the last commit stored 5, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 5 and reads 12 - 5 = 7 records again.

## 4. seed 632023490480434112, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 14 records are produced; 3 records are produced; 3 records are produced; the consumer commits its position; 9 records are produced; the consumer commits its position; the consumer polls and processes up to 4 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `1`, lag `28`
b) committed `0`, lag `29`
c) committed `4`, lag `25`
d) committed `0`, lag `33`

**Key: b**

Explanation: Replaying the events gives log-end offset 29 and position 4. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 0, so lag = 29 - 0 = 29. Records polled after that commit are not committed yet.

## 5. seed 536218421506714132, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 20 records are produced; the consumer commits its position; the consumer polls and processes up to 3 records; 8 records are produced; the consumer commits its position; the consumer commits its position; the consumer polls and processes up to 4 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `3`, lag `21`
b) committed `2`, lag `26`
c) committed `4`, lag `24`
d) committed `3`, lag `25`

**Key: d**

Explanation: Replaying the events gives log-end offset 28 and position 7. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 3, so lag = 28 - 3 = 25. Records polled after that commit are not committed yet.

## 6. seed 4526135894085087477, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 13 records are produced; the consumer polls and processes up to 5 records; the consumer polls and processes up to 6 records; the consumer polls and processes up to 6 records; the consumer commits its position; 8 records are produced; the consumer polls and processes up to 2 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `13`, 3 records read again
b) offset `12`, 3 records read again
c) offset `13`, 2 records read again
d) offset `15`, 0 records read again

**Key: c**

Explanation: Before the crash the position was 15 but the last commit stored 13, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 13 and reads 15 - 13 = 2 records again.

## 7. seed 4177962794041798066, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 10 records are produced; the consumer commits its position; the consumer polls and processes up to 2 records; 4 records are produced; the consumer commits its position; the consumer polls and processes up to 7 records; the consumer polls and processes up to 2 records; the consumer polls and processes up to 5 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `1`, lag `13`
b) committed `14`, lag `0`
c) committed `3`, lag `11`
d) committed `2`, lag `12`

**Key: d**

Explanation: Replaying the events gives log-end offset 14 and position 14. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 2, so lag = 14 - 2 = 12. Records polled after that commit are not committed yet.

## 8. seed 3147582557326544582, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 20 records are produced; the consumer polls and processes up to 7 records; the consumer commits its position; 4 records are produced; the consumer polls and processes up to 5 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `7`, 4 records read again
b) offset `6`, 6 records read again
c) offset `7`, 5 records read again
d) offset `8`, 4 records read again

**Key: c**

Explanation: Before the crash the position was 12 but the last commit stored 7, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 7 and reads 12 - 7 = 5 records again.

## 9. seed 855296173183952481, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 19 records are produced; the consumer commits its position; the consumer polls and processes up to 4 records; the consumer commits its position; the consumer polls and processes up to 6 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `4`, 7 records read again
b) offset `3`, 7 records read again
c) offset `5`, 5 records read again
d) offset `4`, 6 records read again

**Key: d**

Explanation: Before the crash the position was 10 but the last commit stored 4, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 4 and reads 10 - 4 = 6 records again.

## 10. seed 3734948260640449452, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 19 records are produced; the consumer polls and processes up to 8 records; the consumer commits its position; 9 records are produced; the consumer polls and processes up to 4 records; the consumer polls and processes up to 5 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `9`, lag `19`
b) committed `8`, lag `20`
c) committed `7`, lag `21`
d) committed `8`, lag `29`

**Key: b**

Explanation: Replaying the events gives log-end offset 28 and position 17. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 8, so lag = 28 - 8 = 20. Records polled after that commit are not committed yet.

## 11. seed 2850732854285595357, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 13 records are produced; the consumer polls and processes up to 8 records; the consumer polls and processes up to 5 records; 8 records are produced; the consumer commits its position; 4 records are produced; the consumer polls and processes up to 6 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `13`, 7 records read again
b) offset `12`, 7 records read again
c) offset `13`, 6 records read again
d) offset `19`, 0 records read again

**Key: c**

Explanation: Before the crash the position was 19 but the last commit stored 13, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 13 and reads 19 - 13 = 6 records again.

## 12. seed 804724089273022141, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 17 records are produced; 6 records are produced; the consumer polls and processes up to 5 records; the consumer commits its position; the consumer commits its position; the consumer polls and processes up to 7 records; the consumer polls and processes up to 2 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `5`, 8 records read again
b) offset `5`, 9 records read again
c) offset `6`, 8 records read again
d) offset `13`, 1 record read again

**Key: b**

Explanation: Before the crash the position was 14 but the last commit stored 5, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 5 and reads 14 - 5 = 9 records again.

## 13. seed 1696822119112966896, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 15 records are produced; the consumer polls and processes up to 6 records; the consumer commits its position; 4 records are produced; the consumer polls and processes up to 3 records; the consumer polls and processes up to 3 records; the consumer polls and processes up to 2 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `6`, 8 records read again
b) offset `7`, 7 records read again
c) offset `6`, 9 records read again
d) offset `5`, 9 records read again

**Key: a**

Explanation: Before the crash the position was 14 but the last commit stored 6, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 6 and reads 14 - 6 = 8 records again.

## 14. seed 3965577613783918305, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 12 records are produced; the consumer commits its position; 3 records are produced; the consumer commits its position; 8 records are produced; 3 records are produced; the consumer polls and processes up to 2 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `0`, lag `26`
b) committed `0`, lag `28`
c) committed `0`, lag `24`
d) committed `2`, lag `24`

**Key: a**

Explanation: Replaying the events gives log-end offset 26 and position 2. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 0, so lag = 26 - 0 = 26. Records polled after that commit are not committed yet.

## 15. seed 4008018289309002005, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 20 records are produced; the consumer commits its position; 3 records are produced; 7 records are produced; the consumer commits its position; the consumer polls and processes up to 4 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `0`, lag `34`
b) committed `0`, lag `30`
c) committed `1`, lag `29`
d) committed `4`, lag `26`

**Key: b**

Explanation: Replaying the events gives log-end offset 30 and position 4. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 0, so lag = 30 - 0 = 30. Records polled after that commit are not committed yet.

## 16. seed 3299423600864097338, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 20 records are produced; the consumer commits its position; the consumer polls and processes up to 2 records; the consumer commits its position; the consumer polls and processes up to 3 records; the consumer polls and processes up to 6 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `2`, 8 records read again
b) offset `2`, 9 records read again
c) offset `10`, 1 record read again
d) offset `3`, 8 records read again

**Key: b**

Explanation: Before the crash the position was 11 but the last commit stored 2, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 2 and reads 11 - 2 = 9 records again.

## 17. seed 434050830047574689, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 15 records are produced; 3 records are produced; the consumer polls and processes up to 3 records; the consumer polls and processes up to 4 records; the consumer commits its position; the consumer polls and processes up to 3 records; the consumer polls and processes up to 6 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `7`, 9 records read again
b) offset `15`, 1 record read again
c) offset `7`, 8 records read again
d) offset `8`, 8 records read again

**Key: a**

Explanation: Before the crash the position was 16 but the last commit stored 7, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 7 and reads 16 - 7 = 9 records again.

## 18. seed 2350757850227706879, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 9 records are produced; 7 records are produced; the consumer polls and processes up to 2 records; the consumer commits its position; the consumer commits its position; 5 records are produced; 9 records are produced; the consumer polls and processes up to 4 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `3`, lag `27`
b) committed `2`, lag `24`
c) committed `2`, lag `28`
d) committed `2`, lag `32`

**Key: c**

Explanation: Replaying the events gives log-end offset 30 and position 6. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 2, so lag = 30 - 2 = 28. Records polled after that commit are not committed yet.

## 19. seed 925718232430891447, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 19 records are produced; 6 records are produced; 7 records are produced; the consumer polls and processes up to 2 records; the consumer commits its position; the consumer polls and processes up to 6 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `1`, lag `31`
b) committed `2`, lag `24`
c) committed `3`, lag `29`
d) committed `2`, lag `30`

**Key: d**

Explanation: Replaying the events gives log-end offset 32 and position 8. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 2, so lag = 32 - 2 = 30. Records polled after that commit are not committed yet.

## 20. seed 2322768844212408677, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 14 records are produced; the consumer polls and processes up to 7 records; the consumer polls and processes up to 4 records; the consumer commits its position; the consumer polls and processes up to 4 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `11`, 4 records read again
b) offset `14`, 0 records read again
c) offset `11`, 3 records read again
d) offset `12`, 2 records read again

**Key: c**

Explanation: Before the crash the position was 14 but the last commit stored 11, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 11 and reads 14 - 11 = 3 records again.

## 21. seed 2841421567539534216, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 19 records are produced; the consumer commits its position; the consumer commits its position; the consumer polls and processes up to 7 records; the consumer commits its position; the consumer polls and processes up to 6 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `7`, lag `12`
b) committed `12`, lag `7`
c) committed `13`, lag `6`
d) committed `6`, lag `13`

**Key: a**

Explanation: Replaying the events gives log-end offset 19 and position 13. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 7, so lag = 19 - 7 = 12. Records polled after that commit are not committed yet.

## 22. seed 933095712360970572, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 16 records are produced; the consumer commits its position; the consumer commits its position; the consumer polls and processes up to 5 records; the consumer commits its position; the consumer polls and processes up to 7 records; the consumer polls and processes up to 6 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `15`, lag `1`
b) committed `5`, lag `11`
c) committed `4`, lag `12`
d) committed `5`, lag `22`

**Key: b**

Explanation: Replaying the events gives log-end offset 16 and position 16. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 5, so lag = 16 - 5 = 11. Records polled after that commit are not committed yet.

## 23. seed 3374423741013225055, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 16 records are produced; 8 records are produced; 2 records are produced; the consumer polls and processes up to 7 records; the consumer polls and processes up to 2 records; the consumer commits its position; the consumer polls and processes up to 4 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `9`, 3 records read again
b) offset `9`, 5 records read again
c) offset `9`, 4 records read again
d) offset `12`, 1 record read again

**Key: c**

Explanation: Before the crash the position was 13 but the last commit stored 9, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 9 and reads 13 - 9 = 4 records again.

## 24. seed 3001756311753729856, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 8 records are produced; 3 records are produced; 7 records are produced; the consumer commits its position; the consumer polls and processes up to 6 records; 3 records are produced; the consumer polls and processes up to 6 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `0`, lag `33`
b) committed `12`, lag `9`
c) committed `1`, lag `20`
d) committed `0`, lag `21`

**Key: d**

Explanation: Replaying the events gives log-end offset 21 and position 12. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 0, so lag = 21 - 0 = 21. Records polled after that commit are not committed yet.

## 25. seed 4302421364043196641, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 18 records are produced; the consumer commits its position; 8 records are produced; 7 records are produced; the consumer commits its position; 6 records are produced; the consumer polls and processes up to 6 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `1`, lag `38`
b) committed `5`, lag `34`
c) committed `0`, lag `39`
d) committed `6`, lag `33`

**Key: c**

Explanation: Replaying the events gives log-end offset 39 and position 6. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 0, so lag = 39 - 0 = 39. Records polled after that commit are not committed yet.

## 26. seed 2627501336502260258, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 10 records are produced; the consumer commits its position; 9 records are produced; the consumer polls and processes up to 3 records; the consumer commits its position; the consumer polls and processes up to 6 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `9`, 0 records read again
b) offset `3`, 7 records read again
c) offset `3`, 6 records read again
d) offset `3`, 5 records read again

**Key: c**

Explanation: Before the crash the position was 9 but the last commit stored 3, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 3 and reads 9 - 3 = 6 records again.

## 27. seed 3416409272219162490, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 14 records are produced; the consumer polls and processes up to 3 records; the consumer polls and processes up to 3 records; the consumer commits its position; 5 records are produced; the consumer polls and processes up to 8 records; the consumer polls and processes up to 4 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `7`, lag `12`
b) committed `6`, lag `13`
c) committed `17`, lag `2`
d) committed `6`, lag `25`

**Key: b**

Explanation: Replaying the events gives log-end offset 19 and position 18. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 6, so lag = 19 - 6 = 13. Records polled after that commit are not committed yet.

## 28. seed 4507366758950289611, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 11 records are produced; 9 records are produced; 8 records are produced; the consumer polls and processes up to 2 records; the consumer commits its position; the consumer polls and processes up to 3 records; the consumer polls and processes up to 2 records; the consumer polls and processes up to 2 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `2`, lag `19`
b) committed `2`, lag `33`
c) committed `2`, lag `26`
d) committed `3`, lag `25`

**Key: c**

Explanation: Replaying the events gives log-end offset 28 and position 9. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 2, so lag = 28 - 2 = 26. Records polled after that commit are not committed yet.

## 29. seed 1005629014057276730, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 15 records are produced; the consumer polls and processes up to 7 records; the consumer commits its position; the consumer polls and processes up to 7 records; the consumer polls and processes up to 2 records; 9 records are produced; the consumer polls and processes up to 3 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `8`, 10 records read again
b) offset `7`, 10 records read again
c) offset `7`, 12 records read again
d) offset `7`, 11 records read again

**Key: d**

Explanation: Before the crash the position was 18 but the last commit stored 7, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 7 and reads 18 - 7 = 11 records again.

## 30. seed 2923976458623756137, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 15 records are produced; the consumer polls and processes up to 5 records; the consumer polls and processes up to 5 records; the consumer commits its position; the consumer polls and processes up to 4 records; the consumer commits its position; the consumer polls and processes up to 2 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `14`, lag `2`
b) committed `14`, lag `0`
c) committed `13`, lag `2`
d) committed `14`, lag `1`

**Key: d**

Explanation: Replaying the events gives log-end offset 15 and position 15. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 14, so lag = 15 - 14 = 1. Records polled after that commit are not committed yet.

## 31. seed 302484583140033168, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 14 records are produced; the consumer commits its position; the consumer commits its position; the consumer polls and processes up to 7 records; 9 records are produced; the consumer polls and processes up to 6 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `1`, lag `22`
b) committed `0`, lag `23`
c) committed `0`, lag `10`
d) committed `0`, lag `36`

**Key: b**

Explanation: Replaying the events gives log-end offset 23 and position 13. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 0, so lag = 23 - 0 = 23. Records polled after that commit are not committed yet.

## 32. seed 744531720093016858, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 11 records are produced; the consumer commits its position; the consumer polls and processes up to 2 records; the consumer polls and processes up to 5 records; 3 records are produced; the consumer commits its position; the consumer polls and processes up to 4 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `6`, 5 records read again
b) offset `8`, 3 records read again
c) offset `7`, 4 records read again
d) offset `10`, 1 record read again

**Key: c**

Explanation: Before the crash the position was 11 but the last commit stored 7, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 7 and reads 11 - 7 = 4 records again.

## 33. seed 2401926425934436481, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 9 records are produced; the consumer polls and processes up to 8 records; the consumer commits its position; the consumer commits its position; 3 records are produced; the consumer polls and processes up to 4 records; the consumer polls and processes up to 4 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `8`, lag `0`
b) committed `8`, lag `4`
c) committed `7`, lag `5`
d) committed `9`, lag `3`

**Key: b**

Explanation: Replaying the events gives log-end offset 12 and position 12. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 8, so lag = 12 - 8 = 4. Records polled after that commit are not committed yet.

## 34. seed 4347579623965042620, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 18 records are produced; 3 records are produced; the consumer polls and processes up to 5 records; the consumer polls and processes up to 5 records; the consumer commits its position; the consumer polls and processes up to 6 records; the consumer commits its position; the consumer polls and processes up to 5 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `15`, lag `6`
b) committed `20`, lag `1`
c) committed `16`, lag `5`
d) committed `16`, lag `0`

**Key: c**

Explanation: Replaying the events gives log-end offset 21 and position 21. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 16, so lag = 21 - 16 = 5. Records polled after that commit are not committed yet.

## 35. seed 2673232298554717492, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 20 records are produced; the consumer commits its position; the consumer commits its position; 8 records are produced; the consumer polls and processes up to 5 records; the consumer polls and processes up to 5 records; the consumer commits its position; the consumer polls and processes up to 6 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `16`, lag `12`
b) committed `10`, lag `24`
c) committed `10`, lag `18`
d) committed `15`, lag `13`

**Key: c**

Explanation: Replaying the events gives log-end offset 28 and position 16. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 10, so lag = 28 - 10 = 18. Records polled after that commit are not committed yet.

## 36. seed 1219202202512691032, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 19 records are produced; the consumer commits its position; the consumer commits its position; the consumer commits its position; the consumer polls and processes up to 2 records; 5 records are produced; 6 records are produced; the consumer polls and processes up to 5 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `0`, lag `30`
b) committed `0`, lag `23`
c) committed `1`, lag `29`
d) committed `0`, lag `37`

**Key: a**

Explanation: Replaying the events gives log-end offset 30 and position 7. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 0, so lag = 30 - 0 = 30. Records polled after that commit are not committed yet.

## 37. seed 3703263081164650261, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 10 records are produced; the consumer polls and processes up to 3 records; the consumer polls and processes up to 3 records; the consumer commits its position; the consumer commits its position; the consumer polls and processes up to 2 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `7`, lag `3`
b) committed `6`, lag `2`
c) committed `6`, lag `4`
d) committed `8`, lag `2`

**Key: c**

Explanation: Replaying the events gives log-end offset 10 and position 8. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 6, so lag = 10 - 6 = 4. Records polled after that commit are not committed yet.

## 38. seed 2751518365806774533, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 9 records are produced; the consumer polls and processes up to 6 records; the consumer commits its position; 4 records are produced; 7 records are produced; the consumer polls and processes up to 2 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `8`, 0 records read again
b) offset `6`, 2 records read again
c) offset `5`, 3 records read again
d) offset `6`, 3 records read again

**Key: b**

Explanation: Before the crash the position was 8 but the last commit stored 6, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 6 and reads 8 - 6 = 2 records again.

## 39. seed 4253190061428135616, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 20 records are produced; 6 records are produced; the consumer commits its position; the consumer commits its position; the consumer commits its position; the consumer polls and processes up to 4 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `0`, lag `30`
b) committed `0`, lag `26`
c) committed `4`, lag `22`
d) committed `1`, lag `25`

**Key: b**

Explanation: Replaying the events gives log-end offset 26 and position 4. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 0, so lag = 26 - 0 = 26. Records polled after that commit are not committed yet.

## 40. seed 3831273313007382186, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 19 records are produced; 6 records are produced; the consumer commits its position; 4 records are produced; the consumer polls and processes up to 4 records; 7 records are produced; the consumer polls and processes up to 5 records; the consumer polls and processes up to 5 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `0`, lag `50`
b) committed `1`, lag `35`
c) committed `0`, lag `36`
d) committed `0`, lag `22`

**Key: c**

Explanation: Replaying the events gives log-end offset 36 and position 14. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 0, so lag = 36 - 0 = 36. Records polled after that commit are not committed yet.

## 41. seed 3842775129689129066, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 19 records are produced; the consumer polls and processes up to 4 records; the consumer commits its position; the consumer polls and processes up to 6 records; the consumer polls and processes up to 6 records; 2 records are produced; the consumer polls and processes up to 5 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `21`, 0 records read again
b) offset `4`, 17 records read again
c) offset `4`, 16 records read again
d) offset `4`, 18 records read again

**Key: b**

Explanation: Before the crash the position was 21 but the last commit stored 4, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 4 and reads 21 - 4 = 17 records again.

## 42. seed 3245328273569946642, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 20 records are produced; 8 records are produced; the consumer polls and processes up to 8 records; 7 records are produced; the consumer commits its position; the consumer polls and processes up to 6 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `8`, 7 records read again
b) offset `8`, 6 records read again
c) offset `9`, 5 records read again
d) offset `8`, 5 records read again

**Key: b**

Explanation: Before the crash the position was 14 but the last commit stored 8, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 8 and reads 14 - 8 = 6 records again.

## 43. seed 377089271763241253, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 19 records are produced; 9 records are produced; the consumer polls and processes up to 4 records; the consumer commits its position; the consumer polls and processes up to 5 records; 5 records are produced; the consumer polls and processes up to 6 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `15`, 0 records read again
b) offset `4`, 11 records read again
c) offset `3`, 12 records read again
d) offset `5`, 10 records read again

**Key: b**

Explanation: Before the crash the position was 15 but the last commit stored 4, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 4 and reads 15 - 4 = 11 records again.

## 44. seed 2111997287290558515, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 8 records are produced; the consumer polls and processes up to 3 records; the consumer commits its position; 6 records are produced; 2 records are produced; 9 records are produced; the consumer polls and processes up to 2 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `3`, 3 records read again
b) offset `3`, 2 records read again
c) offset `2`, 3 records read again
d) offset `5`, 0 records read again

**Key: b**

Explanation: Before the crash the position was 5 but the last commit stored 3, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 3 and reads 5 - 3 = 2 records again.

## 45. seed 4025109522459829032, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 15 records are produced; the consumer polls and processes up to 2 records; the consumer commits its position; 7 records are produced; the consumer polls and processes up to 4 records; the consumer polls and processes up to 4 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `2`, 9 records read again
b) offset `3`, 7 records read again
c) offset `2`, 7 records read again
d) offset `2`, 8 records read again

**Key: d**

Explanation: Before the crash the position was 10 but the last commit stored 2, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 2 and reads 10 - 2 = 8 records again.

## 46. seed 4564819266132514529, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 17 records are produced; the consumer commits its position; the consumer polls and processes up to 2 records; 2 records are produced; the consumer commits its position; the consumer commits its position; the consumer polls and processes up to 4 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `2`, lag `17`
b) committed `6`, lag `13`
c) committed `1`, lag `18`
d) committed `3`, lag `16`

**Key: a**

Explanation: Replaying the events gives log-end offset 19 and position 6. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 2, so lag = 19 - 2 = 17. Records polled after that commit are not committed yet.

## 47. seed 920593662971358420, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 10 records are produced; 9 records are produced; the consumer commits its position; 8 records are produced; the consumer commits its position; the consumer polls and processes up to 5 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `0`, lag `27`
b) committed `0`, lag `22`
c) committed `4`, lag `23`
d) committed `5`, lag `22`

**Key: a**

Explanation: Replaying the events gives log-end offset 27 and position 5. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 0, so lag = 27 - 0 = 27. Records polled after that commit are not committed yet.

## 48. seed 2328298999500247552, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 17 records are produced; the consumer polls and processes up to 2 records; 7 records are produced; the consumer commits its position; the consumer commits its position; the consumer polls and processes up to 5 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `2`, 6 records read again
b) offset `1`, 6 records read again
c) offset `2`, 5 records read again
d) offset `7`, 0 records read again

**Key: c**

Explanation: Before the crash the position was 7 but the last commit stored 2, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 2 and reads 7 - 2 = 5 records again.

## 49. seed 551061369174277081, level 2

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 17 records are produced; the consumer polls and processes up to 7 records; the consumer polls and processes up to 7 records; the consumer commits its position; the consumer polls and processes up to 2 records; the consumer polls and processes up to 4 records; the consumer crashes and restarts. After the restart the consumer resumes from its committed offset. Which offset does the first fetch after the restart start from, and how many already processed records will it read again?

a) offset `14`, 3 records read again
b) offset `14`, 4 records read again
c) offset `14`, 2 records read again
d) offset `15`, 2 records read again

**Key: a**

Explanation: Before the crash the position was 17 but the last commit stored 14, the offset of the next record to read at that time. A restarted consumer fetches from the committed offset, so it starts at 14 and reads 17 - 14 = 3 records again.

## 50. seed 4031145777548628643, level 1

A partition starts empty (offsets begin at 0) and its consumer group has committed offset 0. In order: 10 records are produced; 9 records are produced; the consumer commits its position; the consumer commits its position; 4 records are produced; the consumer polls and processes up to 3 records. The lag is the log-end offset minus the committed offset. What are the committed offset and the lag at the end?

a) committed `0`, lag `20`
b) committed `0`, lag `26`
c) committed `1`, lag `22`
d) committed `0`, lag `23`

**Key: d**

Explanation: Replaying the events gives log-end offset 23 and position 3. A commit stores the position, which is the offset of the next record to read, not the last one processed. The last commit left 0, so lag = 23 - 0 = 23. Records polled after that commit are not committed yet.
