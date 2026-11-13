# Capacity estimation (`capacity-estimation`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 3676559342045155953, level 1

A service stores 100 million new records per day of 8 KB each, kept for 3 years with 3 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) approximately 3,504.0 TB
b) about 2.6 TB
c) 876.0 TB
d) 2,628.0 TB

**Key: d**

Explanation: Per day: 100,000,000 x 8 KB = 800,000,000 KB. Over 3 years: 800,000,000 x 365 x 3 KB. With 3 replicas that is 2,628,000,000,000 KB, which is 2,628.0 TB.

## 2. seed 1255606160535111415, level 1

A service has 20 million daily active users, each making 30 requests per day. Peak traffic is 3 times the daily average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). What peak request rate must it handle?

a) approximately 20,833 QPS
b) approximately 20,833,333 QPS
c) 6,944 QPS
d) approximately 500,000 QPS

**Key: a**

Explanation: Requests per day: 20,000,000 x 30 = 600,000,000. Average rate: 600,000,000 / 86,400 s = 6,944.4 QPS. Peak rate: 6,944.4 x 3 = 20,833 QPS.

## 3. seed 830093710776734633, level 1

A service has 150 million daily active users, each making 10 requests per day. Peak traffic is 2 times the daily average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). What peak request rate must it handle?

a) approximately 34,722,222 QPS
b) 833,333 QPS
c) approximately 34.7 QPS
d) approximately 34,722 QPS

**Key: d**

Explanation: Requests per day: 150,000,000 x 10 = 1,500,000,000. Average rate: 1,500,000,000 / 86,400 s = 17,361.1 QPS. Peak rate: 17,361.1 x 2 = 34,722 QPS.

## 4. seed 1163736455022069361, level 2

A service has 40 million daily active users, each making 30 requests per day. Peak traffic is 2 times the daily average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). What peak request rate must it handle?

a) approximately 666,667 QPS
b) about 27.8 QPS
c) about 13,889 QPS
d) 27,778 QPS

**Key: d**

Explanation: Requests per day: 40,000,000 x 30 = 1,200,000,000. Average rate: 1,200,000,000 / 86,400 s = 13,888.9 QPS. Peak rate: 13,888.9 x 2 = 27,778 QPS.

## 5. seed 1106755023876964686, level 1

A service has 8 million daily active users, each making 30 requests per day. Peak traffic is 4 times the daily average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). What peak request rate must it handle?

a) about 44,444 QPS
b) 11.1 QPS
c) about 11,111 QPS
d) 2,778 QPS

**Key: c**

Explanation: Requests per day: 8,000,000 x 30 = 240,000,000. Average rate: 240,000,000 / 86,400 s = 2,777.8 QPS. Peak rate: 2,777.8 x 4 = 11,111 QPS.

## 6. seed 3709080574508712640, level 2

A service stores 25 million new records per day of 4 KB each, kept for 5 years with 2 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) about 0.4 TB
b) 365,000.0 TB
c) 365.0 TB
d) about 73.0 TB

**Key: c**

Explanation: Per day: 25,000,000 x 4 KB = 100,000,000 KB. Over 5 years: 100,000,000 x 365 x 5 KB. With 2 replicas that is 365,000,000,000 KB, which is 365.0 TB.

## 7. seed 4463893653556744721, level 1

A service stores 5 million new records per day of 4 KB each, kept for 2 years with 2 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) approximately 43.8 TB
b) approximately 0.0 TB
c) 29.2 TB
d) 29,200.0 TB

**Key: c**

Explanation: Per day: 5,000,000 x 4 KB = 20,000,000 KB. Over 2 years: 20,000,000 x 365 x 2 KB. With 2 replicas that is 29,200,000,000 KB, which is 29.2 TB.

## 8. seed 4031913657131048924, level 1

A service stores 20 million new records per day of 8 KB each, kept for 2 years with 3 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) approximately 116.8 TB
b) approximately 350.4 TB
c) about 175.2 TB
d) about 467.2 TB

**Key: b**

Explanation: Per day: 20,000,000 x 8 KB = 160,000,000 KB. Over 2 years: 160,000,000 x 365 x 2 KB. With 3 replicas that is 350,400,000,000 KB, which is 350.4 TB.

## 9. seed 461379132480604968, level 1

A service stores 50 million new records per day of 4 KB each, kept for 5 years with 2 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) 730,000.0 TB
b) about 1,095.0 TB
c) 365.0 TB
d) 730.0 TB

**Key: d**

Explanation: Per day: 50,000,000 x 4 KB = 200,000,000 KB. Over 5 years: 200,000,000 x 365 x 5 KB. With 2 replicas that is 730,000,000,000 KB, which is 730.0 TB.

## 10. seed 1003971071087531149, level 2

A cache keeps the hottest 10% of 40 million objects of 2 KB each. Use decimal units (1 GB = 10^6 KB). How much memory does the cache need for one copy of the data?

a) about 80.0 GB
b) about 16.0 GB
c) approximately 8.0 GB
d) about 0.0 GB

**Key: c**

Explanation: Hot objects: 40,000,000 x 10% = 4,000,000. Memory: 4,000,000 x 2 KB = 8,000,000 KB, which is 8.0 GB.

## 11. seed 460254627713054246, level 2

A cache keeps the hottest 20% of 40 million objects of 50 KB each. Use decimal units (1 GB = 10^6 KB). How much memory does the cache need for one copy of the data?

a) 400.0 GB
b) approximately 40.0 GB
c) 2,000.0 GB
d) about 0.4 GB

**Key: a**

Explanation: Hot objects: 40,000,000 x 20% = 8,000,000. Memory: 8,000,000 x 50 KB = 400,000,000 KB, which is 400.0 GB.

## 12. seed 2388289650016688595, level 1

A service has 40 million daily active users, each making 6 requests per day. Peak traffic is 2 times the daily average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). What peak request rate must it handle?

a) approximately 5,556 QPS
b) about 2,778 QPS
c) 11,111 QPS
d) 133,333 QPS

**Key: a**

Explanation: Requests per day: 40,000,000 x 6 = 240,000,000. Average rate: 240,000,000 / 86,400 s = 2,777.8 QPS. Peak rate: 2,777.8 x 2 = 5,556 QPS.

## 13. seed 1224199382634728276, level 1

A service stores 50 million new records per day of 20 KB each, kept for 3 years with 2 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) approximately 2,190.0 TB
b) approximately 1,095.0 TB
c) approximately 3,285.0 TB
d) approximately 2,190,000.0 TB

**Key: a**

Explanation: Per day: 50,000,000 x 20 KB = 1,000,000,000 KB. Over 3 years: 1,000,000,000 x 365 x 3 KB. With 2 replicas that is 2,190,000,000,000 KB, which is 2,190.0 TB.

## 14. seed 2613087828170811392, level 2

A service has 25 million daily active users, each making 4 requests per day, with a 5 KB response and a peak of 3 times the average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). Use 1 Mbit = 1,000 kbit. What peak outbound bandwidth does it need?

a) about 17.4 Mbit/s
b) about 46.3 Mbit/s
c) 0.1 Mbit/s
d) 138.9 Mbit/s

**Key: d**

Explanation: Peak rate: 25,000,000 x 4 x 3 / 86,400 s = 3,472.2 QPS. Each response is 5 KB = 40 kbit, so 3,472.2 x 40 kbit / 1,000 = 138.9 Mbit/s.

## 15. seed 240322266933000385, level 2

A service has 50 million daily active users, each making 20 requests per day, with a 8 KB response and a peak of 3 times the average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). Use 1 Mbit = 1,000 kbit. What peak outbound bandwidth does it need?

a) 740.7 Mbit/s
b) approximately 2,222,222.2 Mbit/s
c) 2,777.8 Mbit/s
d) about 2,222.2 Mbit/s

**Key: d**

Explanation: Peak rate: 50,000,000 x 20 x 3 / 86,400 s = 34,722.2 QPS. Each response is 8 KB = 64 kbit, so 34,722.2 x 64 kbit / 1,000 = 2,222.2 Mbit/s.

## 16. seed 4196864790757382296, level 2

A service stores 150 million new records per day of 4 KB each, kept for 2 years with 3 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) approximately 1,314.0 TB
b) 438.0 TB
c) 1,314,000.0 TB
d) approximately 657.0 TB

**Key: a**

Explanation: Per day: 150,000,000 x 4 KB = 600,000,000 KB. Over 2 years: 600,000,000 x 365 x 2 KB. With 3 replicas that is 1,314,000,000,000 KB, which is 1,314.0 TB.

## 17. seed 2592294357855500955, level 1

A service stores 20 million new records per day of 8 KB each, kept for 2 years with 2 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) 233.6 TB
b) about 233,600.0 TB
c) about 0.2 TB
d) 116.8 TB

**Key: a**

Explanation: Per day: 20,000,000 x 8 KB = 160,000,000 KB. Over 2 years: 160,000,000 x 365 x 2 KB. With 2 replicas that is 233,600,000,000 KB, which is 233.6 TB.

## 18. seed 492218148704922774, level 1

A service stores 50 million new records per day of 2 KB each, kept for 5 years with 3 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) 109.5 TB
b) 182.5 TB
c) about 730.0 TB
d) 547.5 TB

**Key: d**

Explanation: Per day: 50,000,000 x 2 KB = 100,000,000 KB. Over 5 years: 100,000,000 x 365 x 5 KB. With 3 replicas that is 547,500,000,000 KB, which is 547.5 TB.

## 19. seed 3109250054884910549, level 2

A service has 25 million daily active users, each making 10 requests per day, with a 100 KB response and a peak of 3 times the average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). Use 1 Mbit = 1,000 kbit. What peak outbound bandwidth does it need?

a) 6,944.4 Mbit/s
b) approximately 6,944,444.4 Mbit/s
c) about 2,314.8 Mbit/s
d) 868.1 Mbit/s

**Key: a**

Explanation: Peak rate: 25,000,000 x 10 x 3 / 86,400 s = 8,680.6 QPS. Each response is 100 KB = 800 kbit, so 8,680.6 x 800 kbit / 1,000 = 6,944.4 Mbit/s.

## 20. seed 2689408112019322478, level 1

A service stores 100 million new records per day of 5 KB each, kept for 2 years with 3 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) approximately 1,095.0 TB
b) approximately 547.5 TB
c) approximately 365.0 TB
d) about 1.1 TB

**Key: a**

Explanation: Per day: 100,000,000 x 5 KB = 500,000,000 KB. Over 2 years: 500,000,000 x 365 x 2 KB. With 3 replicas that is 1,095,000,000,000 KB, which is 1,095.0 TB.

## 21. seed 4016250599766519086, level 2

A service stores 25 million new records per day of 100 KB each, kept for 5 years with 3 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) approximately 4,562.5 TB
b) approximately 13,687.5 TB
c) about 2,737.5 TB
d) 18,250.0 TB

**Key: b**

Explanation: Per day: 25,000,000 x 100 KB = 2,500,000,000 KB. Over 5 years: 2,500,000,000 x 365 x 5 KB. With 3 replicas that is 13,687,500,000,000 KB, which is 13,687.5 TB.

## 22. seed 3130743711464907364, level 1

A service has 10 million daily active users, each making 10 requests per day. Peak traffic is 3 times the daily average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). What peak request rate must it handle?

a) 3.5 QPS
b) 3,472 QPS
c) about 83,333 QPS
d) about 3,472,222 QPS

**Key: b**

Explanation: Requests per day: 10,000,000 x 10 = 100,000,000. Average rate: 100,000,000 / 86,400 s = 1,157.4 QPS. Peak rate: 1,157.4 x 3 = 3,472 QPS.

## 23. seed 2638639042701890612, level 1

A service has 150 million daily active users, each making 30 requests per day. Peak traffic is 4 times the daily average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). What peak request rate must it handle?

a) approximately 833,333 QPS
b) 5,000,000 QPS
c) 208.3 QPS
d) about 208,333 QPS

**Key: d**

Explanation: Requests per day: 150,000,000 x 30 = 4,500,000,000. Average rate: 4,500,000,000 / 86,400 s = 52,083.3 QPS. Peak rate: 52,083.3 x 4 = 208,333 QPS.

## 24. seed 3079607152083965865, level 1

A service stores 20 million new records per day of 200 KB each, kept for 3 years with 3 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) about 13,140.0 TB
b) about 13.1 TB
c) approximately 17,520.0 TB
d) about 4,380.0 TB

**Key: a**

Explanation: Per day: 20,000,000 x 200 KB = 4,000,000,000 KB. Over 3 years: 4,000,000,000 x 365 x 3 KB. With 3 replicas that is 13,140,000,000,000 KB, which is 13,140.0 TB.

## 25. seed 597401895665550637, level 2

A cache keeps the hottest 20% of 20 million objects of 8 KB each. Use decimal units (1 GB = 10^6 KB). How much memory does the cache need for one copy of the data?

a) approximately 64.0 GB
b) about 32,000.0 GB
c) 32.0 GB
d) about 160.0 GB

**Key: c**

Explanation: Hot objects: 20,000,000 x 20% = 4,000,000. Memory: 4,000,000 x 8 KB = 32,000,000 KB, which is 32.0 GB.

## 26. seed 3853485526121013739, level 1

A service stores 20 million new records per day of 200 KB each, kept for 5 years with 2 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) 21,900.0 TB
b) approximately 14,600.0 TB
c) 14,600,000.0 TB
d) 14.6 TB

**Key: b**

Explanation: Per day: 20,000,000 x 200 KB = 4,000,000,000 KB. Over 5 years: 4,000,000,000 x 365 x 5 KB. With 2 replicas that is 14,600,000,000,000 KB, which is 14,600.0 TB.

## 27. seed 1879624540689202250, level 1

A service has 8 million daily active users, each making 20 requests per day. Peak traffic is 4 times the daily average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). What peak request rate must it handle?

a) 1,852 QPS
b) about 29,630 QPS
c) approximately 7,407 QPS
d) about 7.4 QPS

**Key: c**

Explanation: Requests per day: 8,000,000 x 20 = 160,000,000. Average rate: 160,000,000 / 86,400 s = 1,851.9 QPS. Peak rate: 1,851.9 x 4 = 7,407 QPS.

## 28. seed 4334185380342863784, level 2

A service has 150 million daily active users, each making 30 requests per day, with a 100 KB response and a peak of 3 times the average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). Use 1 Mbit = 1,000 kbit. What peak outbound bandwidth does it need?

a) approximately 156,250.0 Mbit/s
b) 41,666.7 Mbit/s
c) approximately 15,625.0 Mbit/s
d) about 125,000.0 Mbit/s

**Key: d**

Explanation: Peak rate: 150,000,000 x 30 x 3 / 86,400 s = 156,250.0 QPS. Each response is 100 KB = 800 kbit, so 156,250.0 x 800 kbit / 1,000 = 125,000.0 Mbit/s.

## 29. seed 1771327056233480927, level 1

A service has 25 million daily active users, each making 20 requests per day. Peak traffic is 2 times the daily average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). What peak request rate must it handle?

a) 11.6 QPS
b) approximately 11,574 QPS
c) approximately 5,787 QPS
d) about 277,778 QPS

**Key: b**

Explanation: Requests per day: 25,000,000 x 20 = 500,000,000. Average rate: 500,000,000 / 86,400 s = 5,787.0 QPS. Peak rate: 5,787.0 x 2 = 11,574 QPS.

## 30. seed 1756060984025349262, level 1

A service stores 50 million new records per day of 4 KB each, kept for 2 years with 2 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) approximately 0.3 TB
b) about 146.0 TB
c) about 292,000.0 TB
d) approximately 292.0 TB

**Key: d**

Explanation: Per day: 50,000,000 x 4 KB = 200,000,000 KB. Over 2 years: 200,000,000 x 365 x 2 KB. With 2 replicas that is 292,000,000,000 KB, which is 292.0 TB.

## 31. seed 3286393184819423743, level 1

A service has 150 million daily active users, each making 30 requests per day. Peak traffic is 4 times the daily average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). What peak request rate must it handle?

a) about 208,333,333 QPS
b) 5,000,000 QPS
c) approximately 208,333 QPS
d) 52,083 QPS

**Key: c**

Explanation: Requests per day: 150,000,000 x 30 = 4,500,000,000. Average rate: 4,500,000,000 / 86,400 s = 52,083.3 QPS. Peak rate: 52,083.3 x 4 = 208,333 QPS.

## 32. seed 806899032175525550, level 1

A service has 8 million daily active users, each making 6 requests per day. Peak traffic is 4 times the daily average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). What peak request rate must it handle?

a) 8,889 QPS
b) 2,222 QPS
c) 53,333 QPS
d) approximately 2,222,222 QPS

**Key: b**

Explanation: Requests per day: 8,000,000 x 6 = 48,000,000. Average rate: 48,000,000 / 86,400 s = 555.6 QPS. Peak rate: 555.6 x 4 = 2,222 QPS.

## 33. seed 4363846324682418949, level 1

A service has 150 million daily active users, each making 30 requests per day. Peak traffic is 5 times the daily average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). What peak request rate must it handle?

a) about 260,417 QPS
b) about 1,302,083 QPS
c) about 6,250,000 QPS
d) about 260,416,667 QPS

**Key: a**

Explanation: Requests per day: 150,000,000 x 30 = 4,500,000,000. Average rate: 4,500,000,000 / 86,400 s = 52,083.3 QPS. Peak rate: 52,083.3 x 5 = 260,417 QPS.

## 34. seed 272226373357039541, level 2

A service stores 25 million new records per day of 8 KB each, kept for 3 years with 3 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) approximately 876.0 TB
b) approximately 657.0 TB
c) about 219.0 TB
d) about 657,000.0 TB

**Key: b**

Explanation: Per day: 25,000,000 x 8 KB = 200,000,000 KB. Over 3 years: 200,000,000 x 365 x 3 KB. With 3 replicas that is 657,000,000,000 KB, which is 657.0 TB.

## 35. seed 123073567884773833, level 2

A service stores 8 million new records per day of 200 KB each, kept for 2 years with 2 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) about 3,504.0 TB
b) approximately 2,336,000.0 TB
c) approximately 2,336.0 TB
d) about 1,168.0 TB

**Key: c**

Explanation: Per day: 8,000,000 x 200 KB = 1,600,000,000 KB. Over 2 years: 1,600,000,000 x 365 x 2 KB. With 2 replicas that is 2,336,000,000,000 KB, which is 2,336.0 TB.

## 36. seed 825765581773260106, level 1

A service stores 5 million new records per day of 5 KB each, kept for 5 years with 3 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) approximately 27.4 TB
b) approximately 0.1 TB
c) 136.9 TB
d) 45.6 TB

**Key: c**

Explanation: Per day: 5,000,000 x 5 KB = 25,000,000 KB. Over 5 years: 25,000,000 x 365 x 5 KB. With 3 replicas that is 136,875,000,000 KB, which is 136.9 TB.

## 37. seed 2257534992862187418, level 1

A service stores 40 million new records per day of 4 KB each, kept for 3 years with 3 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) 525,600.0 TB
b) approximately 525.6 TB
c) approximately 175.2 TB
d) 700.8 TB

**Key: b**

Explanation: Per day: 40,000,000 x 4 KB = 160,000,000 KB. Over 3 years: 160,000,000 x 365 x 3 KB. With 3 replicas that is 525,600,000,000 KB, which is 525.6 TB.

## 38. seed 2783747654802139233, level 2

A service has 100 million daily active users, each making 6 requests per day. Peak traffic is 3 times the daily average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). What peak request rate must it handle?

a) 20,833 QPS
b) 500,000 QPS
c) 62,500 QPS
d) approximately 6,944 QPS

**Key: a**

Explanation: Requests per day: 100,000,000 x 6 = 600,000,000. Average rate: 600,000,000 / 86,400 s = 6,944.4 QPS. Peak rate: 6,944.4 x 3 = 20,833 QPS.

## 39. seed 3609033611328773896, level 1

A service has 100 million daily active users, each making 4 requests per day. Peak traffic is 5 times the daily average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). What peak request rate must it handle?

a) 23,148,148 QPS
b) 555,556 QPS
c) about 23,148 QPS
d) 115,741 QPS

**Key: c**

Explanation: Requests per day: 100,000,000 x 4 = 400,000,000. Average rate: 400,000,000 / 86,400 s = 4,629.6 QPS. Peak rate: 4,629.6 x 5 = 23,148 QPS.

## 40. seed 2749817318527846513, level 2

A service has 25 million daily active users, each making 12 requests per day, with a 50 KB response and a peak of 5 times the average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). Use 1 Mbit = 1,000 kbit. What peak outbound bandwidth does it need?

a) about 6,944.4 Mbit/s
b) 868.1 Mbit/s
c) approximately 8,680.6 Mbit/s
d) approximately 6,944,444.4 Mbit/s

**Key: a**

Explanation: Peak rate: 25,000,000 x 12 x 5 / 86,400 s = 17,361.1 QPS. Each response is 50 KB = 400 kbit, so 17,361.1 x 400 kbit / 1,000 = 6,944.4 Mbit/s.

## 41. seed 409239528978869258, level 1

A service stores 150 million new records per day of 5 KB each, kept for 5 years with 2 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) 2,737.5 TB
b) 1,368.8 TB
c) about 2,737,500.0 TB
d) 4,106.3 TB

**Key: a**

Explanation: Per day: 150,000,000 x 5 KB = 750,000,000 KB. Over 5 years: 750,000,000 x 365 x 5 KB. With 2 replicas that is 2,737,500,000,000 KB, which is 2,737.5 TB.

## 42. seed 2123129320324842125, level 2

A cache keeps the hottest 20% of 20 million objects of 4 KB each. Use decimal units (1 GB = 10^6 KB). How much memory does the cache need for one copy of the data?

a) 0.0 GB
b) approximately 1.6 GB
c) approximately 32.0 GB
d) about 16.0 GB

**Key: d**

Explanation: Hot objects: 20,000,000 x 20% = 4,000,000. Memory: 4,000,000 x 4 KB = 16,000,000 KB, which is 16.0 GB.

## 43. seed 1154206898604760988, level 1

A service stores 8 million new records per day of 2 KB each, kept for 3 years with 3 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) approximately 52,560.0 TB
b) 70.1 TB
c) about 17.5 TB
d) about 52.6 TB

**Key: d**

Explanation: Per day: 8,000,000 x 2 KB = 16,000,000 KB. Over 3 years: 16,000,000 x 365 x 3 KB. With 3 replicas that is 52,560,000,000 KB, which is 52.6 TB.

## 44. seed 1083887008217635351, level 2

A cache keeps the hottest 20% of 8 million objects of 8 KB each. Use decimal units (1 GB = 10^6 KB). How much memory does the cache need for one copy of the data?

a) approximately 64.0 GB
b) about 25.6 GB
c) about 12,800.0 GB
d) approximately 12.8 GB

**Key: d**

Explanation: Hot objects: 8,000,000 x 20% = 1,600,000. Memory: 1,600,000 x 8 KB = 12,800,000 KB, which is 12.8 GB.

## 45. seed 2447130542411011673, level 2

A service has 150 million daily active users, each making 10 requests per day, with a 8 KB response and a peak of 5 times the average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). Use 1 Mbit = 1,000 kbit. What peak outbound bandwidth does it need?

a) approximately 5,555.6 Mbit/s
b) about 5.6 Mbit/s
c) approximately 5,555,555.6 Mbit/s
d) 694.4 Mbit/s

**Key: a**

Explanation: Peak rate: 150,000,000 x 10 x 5 / 86,400 s = 86,805.6 QPS. Each response is 8 KB = 64 kbit, so 86,805.6 x 64 kbit / 1,000 = 5,555.6 Mbit/s.

## 46. seed 2832352175073404670, level 2

A service has 150 million daily active users, each making 6 requests per day. Peak traffic is 3 times the daily average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). What peak request rate must it handle?

a) about 31,250 QPS
b) about 31,250,000 QPS
c) about 10,417 QPS
d) 750,000 QPS

**Key: a**

Explanation: Requests per day: 150,000,000 x 6 = 900,000,000. Average rate: 900,000,000 / 86,400 s = 10,416.7 QPS. Peak rate: 10,416.7 x 3 = 31,250 QPS.

## 47. seed 3740278400848391722, level 1

A service stores 40 million new records per day of 5 KB each, kept for 3 years with 3 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) approximately 219.0 TB
b) 657,000.0 TB
c) 876.0 TB
d) approximately 657.0 TB

**Key: d**

Explanation: Per day: 40,000,000 x 5 KB = 200,000,000 KB. Over 3 years: 200,000,000 x 365 x 3 KB. With 3 replicas that is 657,000,000,000 KB, which is 657.0 TB.

## 48. seed 1196639790473644780, level 1

A service stores 150 million new records per day of 2 KB each, kept for 5 years with 2 replicas of every record. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). How much raw storage does it need?

a) approximately 1,095.0 TB
b) about 1.1 TB
c) 547.5 TB
d) about 1,095,000.0 TB

**Key: a**

Explanation: Per day: 150,000,000 x 2 KB = 300,000,000 KB. Over 5 years: 300,000,000 x 365 x 5 KB. With 2 replicas that is 1,095,000,000,000 KB, which is 1,095.0 TB.

## 49. seed 3307447169046434393, level 1

A service has 40 million daily active users, each making 10 requests per day. Peak traffic is 3 times the daily average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). What peak request rate must it handle?

a) about 13,888,889 QPS
b) 4,630 QPS
c) approximately 41,667 QPS
d) approximately 13,889 QPS

**Key: d**

Explanation: Requests per day: 40,000,000 x 10 = 400,000,000. Average rate: 400,000,000 / 86,400 s = 4,629.6 QPS. Peak rate: 4,629.6 x 3 = 13,889 QPS.

## 50. seed 3343517720747357811, level 2

A service has 100 million daily active users, each making 30 requests per day. Peak traffic is 2 times the daily average. Use 86,400 seconds per day, 365 days per year and decimal units (1 TB = 10^9 KB). What peak request rate must it handle?

a) 69,444,444 QPS
b) approximately 69.4 QPS
c) approximately 69,444 QPS
d) approximately 138,889 QPS

**Key: c**

Explanation: Requests per day: 100,000,000 x 30 = 3,000,000,000. Average rate: 3,000,000,000 / 86,400 s = 34,722.2 QPS. Peak rate: 34,722.2 x 2 = 69,444 QPS.
