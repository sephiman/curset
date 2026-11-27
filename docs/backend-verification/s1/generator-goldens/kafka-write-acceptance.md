# Kafka write acceptance (`kafka-write-acceptance`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 1953782383180791199, level 2

A topic has replication factor 4 and `min.insync.replicas=3`. A producer sends with `acks=all`; 4 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 2
b) 0
c) 3
d) 1

**Key: d**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 4 in sync, minimum 3. Step 1: with `acks=all` writes pass while the in-sync count is at least 3. Step 2: the spare replicas are 4 - 3 = 1. Result: 1, and one more loss leaves 2, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 2. seed 2141769598417489951, level 1

A topic has replication factor 5 and `min.insync.replicas=3`. A producer sends with `acks=all`; 2 replicas, leader included, are in sync. Which statement about this write is true?

a) The write is accepted without `NotEnoughReplicas`: the leader holds the record, so the producer can be acknowledged
b) The write is accepted without `NotEnoughReplicas`: `acks=all` waits only for the replicas that are in sync
c) The write is accepted without `NotEnoughReplicas`: `min.insync.replicas` is only a target, not a limit on writes
d) The write is rejected with `NotEnoughReplicas`: only 2 replicas in sync, fewer than 3 that `acks=all` needs

**Key: d**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=all`, 2 in sync, minimum 3. Step 1: with `acks=all` the minimum is checked. Step 2: 2 in sync is below 3. Result: the write is rejected with `NotEnoughReplicas`. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 3. seed 887870061429060346, level 1

A topic has replication factor 5 and `min.insync.replicas=4`. A producer sends with `acks=all`; 3 replicas, leader included, are in sync. Which statement about this write is true?

a) The write is accepted without `NotEnoughReplicas`: `min.insync.replicas` is only a target, not a limit on writes
b) The write is rejected with `NotEnoughReplicas`: 3 replicas in sync are fewer than the 4 in `min.insync.replicas`
c) The write is accepted without `NotEnoughReplicas`: a majority of the 5 replicas must be in sync
d) The write is accepted without `NotEnoughReplicas`: `acks=all` waits only for the replicas that are in sync

**Key: b**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=all`, 3 in sync, minimum 4. Step 1: with `acks=all` the minimum is checked. Step 2: 3 in sync is below 4. Result: the write is rejected with `NotEnoughReplicas`. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 4. seed 1408440876259014814, level 2

A topic has replication factor 4 and `min.insync.replicas=3`. A producer sends with `acks=all`; 4 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 1
b) 2
c) 3
d) 0

**Key: a**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 4 in sync, minimum 3. Step 1: with `acks=all` writes pass while the in-sync count is at least 3. Step 2: the spare replicas are 4 - 3 = 1. Result: 1, and one more loss leaves 2, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 5. seed 467517854747729854, level 1

A topic has replication factor 5 and `min.insync.replicas=3`. A producer sends with `acks=all`; 2 replicas, leader included, are in sync. Which statement about this write is true?

a) The write is accepted without `NotEnoughReplicas`: the leader holds the record, so the producer can be acknowledged
b) The write is accepted without `NotEnoughReplicas`: `acks=all` waits only for the replicas that are in sync
c) The write is accepted without `NotEnoughReplicas`: `min.insync.replicas` is only a target, not a limit on writes
d) The write is rejected with `NotEnoughReplicas`: 2 replicas in sync are fewer than the 3 in `min.insync.replicas`

**Key: d**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=all`, 2 in sync, minimum 3. Step 1: with `acks=all` the minimum is checked. Step 2: 2 in sync is below 3. Result: the write is rejected with `NotEnoughReplicas`. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 6. seed 3793591482493460513, level 2

A topic has replication factor 5 and `min.insync.replicas=3`. A producer sends with `acks=all`; 4 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 2
b) 0
c) 1
d) 3

**Key: c**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 4 in sync, minimum 3. Step 1: with `acks=all` writes pass while the in-sync count is at least 3. Step 2: the spare replicas are 4 - 3 = 1. Result: 1, and one more loss leaves 2, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 7. seed 2437633708855045570, level 1

A topic has replication factor 4 and `min.insync.replicas=2`. A producer sends with `acks=0`; 1 replica, leader included, is in sync. Which statement about this write is true?

a) The write is rejected with `NotEnoughReplicas`: every one of the 4 replicas must be in sync
b) The write is accepted without `NotEnoughReplicas`: only `acks=all` checks the in-sync replica count
c) The write is rejected with `NotEnoughReplicas`: `min.insync.replicas` also applies to `acks=0`
d) The write is rejected with `NotEnoughReplicas`: a majority of the 4 replicas must be in sync

**Key: b**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=0`, 1 in sync, minimum 2. Step 1: the minimum is checked only when `acks=all`. Step 2: here it is `acks=0`, so the in-sync count does not matter. Result: the write is accepted. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 8. seed 1315333967736171963, level 1

A topic has replication factor 5 and `min.insync.replicas=4`. A producer sends with `acks=1`; 1 replica, leader included, is in sync. Which statement about this write is true?

a) The write is rejected with `NotEnoughReplicas`: every one of the 5 replicas must be in sync
b) The write is rejected with `NotEnoughReplicas`: a majority of the 5 replicas must be in sync
c) The write is accepted without `NotEnoughReplicas`: only `acks=all` checks the in-sync replica count
d) The write is rejected with `NotEnoughReplicas`: `min.insync.replicas` also applies to `acks=1`

**Key: c**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=1`, 1 in sync, minimum 4. Step 1: the minimum is checked only when `acks=all`. Step 2: here it is `acks=1`, so the in-sync count does not matter. Result: the write is accepted. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 9. seed 1164247664609693680, level 2

A topic has replication factor 4 and `min.insync.replicas=3`. A producer sends with `acks=all`; 4 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 3
b) 1
c) 2
d) 0

**Key: b**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 4 in sync, minimum 3. Step 1: with `acks=all` writes pass while the in-sync count is at least 3. Step 2: the spare replicas are 4 - 3 = 1. Result: 1, and one more loss leaves 2, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 10. seed 1525047147557847465, level 1

A topic has replication factor 5 and `min.insync.replicas=2`. A producer sends with `acks=all`; 1 replica, leader included, is in sync. Which statement about this write is true?

a) The write is accepted without `NotEnoughReplicas`: the leader holds the record, so the producer can be acknowledged
b) The write is rejected with `NotEnoughReplicas`: 1 replica in sync is fewer than the 2 in `min.insync.replicas`
c) The write is accepted without `NotEnoughReplicas`: `acks=all` waits only for the replicas that are in sync
d) The write is accepted without `NotEnoughReplicas`: `min.insync.replicas` is only a target, not a limit on writes

**Key: b**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=all`, 1 in sync, minimum 2. Step 1: with `acks=all` the minimum is checked. Step 2: 1 in sync is below 2. Result: the write is rejected with `NotEnoughReplicas`. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 11. seed 2288018358357167207, level 1

A topic has replication factor 5 and `min.insync.replicas=4`. A producer sends with `acks=all`; 3 replicas, leader included, are in sync. Which statement about this write is true?

a) The write is rejected with `NotEnoughReplicas`: only 3 replicas in sync, fewer than 4 that `acks=all` needs
b) The write is accepted without `NotEnoughReplicas`: a majority of the 5 replicas must be in sync
c) The write is accepted without `NotEnoughReplicas`: `acks=all` waits only for the replicas that are in sync
d) The write is accepted without `NotEnoughReplicas`: the leader holds the record, so the producer can be acknowledged

**Key: a**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=all`, 3 in sync, minimum 4. Step 1: with `acks=all` the minimum is checked. Step 2: 3 in sync is below 4. Result: the write is rejected with `NotEnoughReplicas`. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 12. seed 3234260886662676726, level 1

A topic has replication factor 5 and `min.insync.replicas=4`. A producer sends with `acks=0`; 1 replica, leader included, is in sync. Which statement about this write is true?

a) The write is rejected with `NotEnoughReplicas`: every one of the 5 replicas must be in sync
b) The write is rejected with `NotEnoughReplicas`: a majority of the 5 replicas must be in sync
c) The write is rejected with `NotEnoughReplicas`: `min.insync.replicas` also applies to `acks=0`
d) The write is accepted without `NotEnoughReplicas`: only `acks=all` checks the in-sync replica count

**Key: d**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=0`, 1 in sync, minimum 4. Step 1: the minimum is checked only when `acks=all`. Step 2: here it is `acks=0`, so the in-sync count does not matter. Result: the write is accepted. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 13. seed 738601067879962092, level 2

A topic has replication factor 5 and `min.insync.replicas=3`. A producer sends with `acks=all`; 4 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 0
b) 2
c) 3
d) 1

**Key: d**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 4 in sync, minimum 3. Step 1: with `acks=all` writes pass while the in-sync count is at least 3. Step 2: the spare replicas are 4 - 3 = 1. Result: 1, and one more loss leaves 2, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 14. seed 756959695712593772, level 2

A topic has replication factor 4 and `min.insync.replicas=3`. A producer sends with `acks=all`; 4 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 3
b) 2
c) 0
d) 1

**Key: d**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 4 in sync, minimum 3. Step 1: with `acks=all` writes pass while the in-sync count is at least 3. Step 2: the spare replicas are 4 - 3 = 1. Result: 1, and one more loss leaves 2, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 15. seed 4506292383715125802, level 2

A topic has replication factor 4 and `min.insync.replicas=3`. A producer sends with `acks=all`; 4 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 1
b) 2
c) 0
d) 3

**Key: a**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 4 in sync, minimum 3. Step 1: with `acks=all` writes pass while the in-sync count is at least 3. Step 2: the spare replicas are 4 - 3 = 1. Result: 1, and one more loss leaves 2, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 16. seed 2597420838467387868, level 1

A topic has replication factor 5 and `min.insync.replicas=3`. A producer sends with `acks=all`; 2 replicas, leader included, are in sync. Which statement about this write is true?

a) The write is accepted without `NotEnoughReplicas`: `acks=all` waits only for the replicas that are in sync
b) The write is accepted without `NotEnoughReplicas`: the leader holds the record, so the producer can be acknowledged
c) The write is accepted without `NotEnoughReplicas`: `min.insync.replicas` is only a target, not a limit on writes
d) The write is rejected with `NotEnoughReplicas`: only 2 replicas in sync, fewer than 3 that `acks=all` needs

**Key: d**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=all`, 2 in sync, minimum 3. Step 1: with `acks=all` the minimum is checked. Step 2: 2 in sync is below 3. Result: the write is rejected with `NotEnoughReplicas`. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 17. seed 2377787942011410505, level 2

A topic has replication factor 4 and `min.insync.replicas=3`. A producer sends with `acks=all`; 4 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 2
b) 1
c) 0
d) 3

**Key: b**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 4 in sync, minimum 3. Step 1: with `acks=all` writes pass while the in-sync count is at least 3. Step 2: the spare replicas are 4 - 3 = 1. Result: 1, and one more loss leaves 2, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 18. seed 936443891881924880, level 2

A topic has replication factor 5 and `min.insync.replicas=3`. A producer sends with `acks=all`; 5 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 2
b) 1
c) 3
d) 4

**Key: a**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 5 in sync, minimum 3. Step 1: with `acks=all` writes pass while the in-sync count is at least 3. Step 2: the spare replicas are 5 - 3 = 2. Result: 2, and one more loss leaves 2, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 19. seed 669360281000562010, level 2

A topic has replication factor 4 and `min.insync.replicas=3`. A producer sends with `acks=all`; 4 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 2
b) 1
c) 0
d) 3

**Key: b**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 4 in sync, minimum 3. Step 1: with `acks=all` writes pass while the in-sync count is at least 3. Step 2: the spare replicas are 4 - 3 = 1. Result: 1, and one more loss leaves 2, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 20. seed 899777116558638902, level 2

A topic has replication factor 5 and `min.insync.replicas=4`. A producer sends with `acks=all`; 5 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 4
b) 1
c) 2
d) 0

**Key: b**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 5 in sync, minimum 4. Step 1: with `acks=all` writes pass while the in-sync count is at least 4. Step 2: the spare replicas are 5 - 4 = 1. Result: 1, and one more loss leaves 3, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 21. seed 1081544352143106941, level 1

A topic has replication factor 5 and `min.insync.replicas=3`. A producer sends with `acks=all`; 1 replica, leader included, is in sync. Which statement about this write is true?

a) The write is accepted without `NotEnoughReplicas`: `min.insync.replicas` is only a target, not a limit on writes
b) The write is accepted without `NotEnoughReplicas`: `acks=all` waits only for the replicas that are in sync
c) The write is rejected with `NotEnoughReplicas`: only 1 replica in sync, fewer than 3 that `acks=all` needs
d) The write is accepted without `NotEnoughReplicas`: the leader holds the record, so the producer can be acknowledged

**Key: c**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=all`, 1 in sync, minimum 3. Step 1: with `acks=all` the minimum is checked. Step 2: 1 in sync is below 3. Result: the write is rejected with `NotEnoughReplicas`. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 22. seed 2368115343326707311, level 2

A topic has replication factor 5 and `min.insync.replicas=2`. A producer sends with `acks=all`; 3 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 0
b) 3
c) 2
d) 1

**Key: d**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 3 in sync, minimum 2. Step 1: with `acks=all` writes pass while the in-sync count is at least 2. Step 2: the spare replicas are 3 - 2 = 1. Result: 1, and one more loss leaves 1, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 23. seed 33386030373098365, level 1

A topic has replication factor 3 and `min.insync.replicas=2`. A producer sends with `acks=0`; 1 replica, leader included, is in sync. Which statement about this write is true?

a) The write is rejected with `NotEnoughReplicas`: `min.insync.replicas` also applies to `acks=0`
b) The write is accepted without `NotEnoughReplicas`: only `acks=all` checks the in-sync replica count
c) The write is rejected with `NotEnoughReplicas`: a majority of the 3 replicas must be in sync
d) The write is rejected with `NotEnoughReplicas`: every one of the 3 replicas must be in sync

**Key: b**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=0`, 1 in sync, minimum 2. Step 1: the minimum is checked only when `acks=all`. Step 2: here it is `acks=0`, so the in-sync count does not matter. Result: the write is accepted. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 24. seed 855820978563379747, level 2

A topic has replication factor 4 and `min.insync.replicas=3`. A producer sends with `acks=all`; 4 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 0
b) 2
c) 1
d) 3

**Key: c**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 4 in sync, minimum 3. Step 1: with `acks=all` writes pass while the in-sync count is at least 3. Step 2: the spare replicas are 4 - 3 = 1. Result: 1, and one more loss leaves 2, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 25. seed 2523916361103482136, level 2

A topic has replication factor 4 and `min.insync.replicas=3`. A producer sends with `acks=all`; 4 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 0
b) 1
c) 3
d) 2

**Key: b**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 4 in sync, minimum 3. Step 1: with `acks=all` writes pass while the in-sync count is at least 3. Step 2: the spare replicas are 4 - 3 = 1. Result: 1, and one more loss leaves 2, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 26. seed 1567789752940205345, level 1

A topic has replication factor 5 and `min.insync.replicas=3`. A producer sends with `acks=0`; 1 replica, leader included, is in sync. Which statement about this write is true?

a) The write is rejected with `NotEnoughReplicas`: a majority of the 5 replicas must be in sync
b) The write is rejected with `NotEnoughReplicas`: `min.insync.replicas` also applies to `acks=0`
c) The write is rejected with `NotEnoughReplicas`: every one of the 5 replicas must be in sync
d) The write is accepted without `NotEnoughReplicas`: only `acks=all` checks the in-sync replica count

**Key: d**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=0`, 1 in sync, minimum 3. Step 1: the minimum is checked only when `acks=all`. Step 2: here it is `acks=0`, so the in-sync count does not matter. Result: the write is accepted. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 27. seed 3279267831171898957, level 2

A topic has replication factor 4 and `min.insync.replicas=3`. A producer sends with `acks=all`; 4 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 1
b) 0
c) 2
d) 3

**Key: a**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 4 in sync, minimum 3. Step 1: with `acks=all` writes pass while the in-sync count is at least 3. Step 2: the spare replicas are 4 - 3 = 1. Result: 1, and one more loss leaves 2, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 28. seed 3312402720140600857, level 1

A topic has replication factor 5 and `min.insync.replicas=4`. A producer sends with `acks=0`; 1 replica, leader included, is in sync. Which statement about this write is true?

a) The write is rejected with `NotEnoughReplicas`: a majority of the 5 replicas must be in sync
b) The write is rejected with `NotEnoughReplicas`: every one of the 5 replicas must be in sync
c) The write is accepted without `NotEnoughReplicas`: only `acks=all` checks the in-sync replica count
d) The write is rejected with `NotEnoughReplicas`: `min.insync.replicas` also applies to `acks=0`

**Key: c**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=0`, 1 in sync, minimum 4. Step 1: the minimum is checked only when `acks=all`. Step 2: here it is `acks=0`, so the in-sync count does not matter. Result: the write is accepted. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 29. seed 377533038143325452, level 2

A topic has replication factor 5 and `min.insync.replicas=4`. A producer sends with `acks=all`; 5 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 4
b) 0
c) 1
d) 2

**Key: c**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 5 in sync, minimum 4. Step 1: with `acks=all` writes pass while the in-sync count is at least 4. Step 2: the spare replicas are 5 - 4 = 1. Result: 1, and one more loss leaves 3, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 30. seed 2160846596960982291, level 1

A topic has replication factor 4 and `min.insync.replicas=3`. A producer sends with `acks=all`; 2 replicas, leader included, are in sync. Which statement about this write is true?

a) The write is accepted without `NotEnoughReplicas`: `acks=all` waits only for the replicas that are in sync
b) The write is accepted without `NotEnoughReplicas`: the leader holds the record, so the producer can be acknowledged
c) The write is rejected with `NotEnoughReplicas`: 2 replicas in sync are fewer than the 3 in `min.insync.replicas`
d) The write is accepted without `NotEnoughReplicas`: `min.insync.replicas` is only a target, not a limit on writes

**Key: c**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=all`, 2 in sync, minimum 3. Step 1: with `acks=all` the minimum is checked. Step 2: 2 in sync is below 3. Result: the write is rejected with `NotEnoughReplicas`. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 31. seed 2734352221426493591, level 1

A topic has replication factor 4 and `min.insync.replicas=3`. A producer sends with `acks=all`; 1 replica, leader included, is in sync. Which statement about this write is true?

a) The write is rejected with `NotEnoughReplicas`: 1 replica in sync is fewer than the 3 in `min.insync.replicas`
b) The write is accepted without `NotEnoughReplicas`: the leader holds the record, so the producer can be acknowledged
c) The write is accepted without `NotEnoughReplicas`: `min.insync.replicas` is only a target, not a limit on writes
d) The write is accepted without `NotEnoughReplicas`: `acks=all` waits only for the replicas that are in sync

**Key: a**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=all`, 1 in sync, minimum 3. Step 1: with `acks=all` the minimum is checked. Step 2: 1 in sync is below 3. Result: the write is rejected with `NotEnoughReplicas`. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 32. seed 4009312488085876963, level 2

A topic has replication factor 4 and `min.insync.replicas=3`. A producer sends with `acks=all`; 4 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 1
b) 3
c) 2
d) 0

**Key: a**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 4 in sync, minimum 3. Step 1: with `acks=all` writes pass while the in-sync count is at least 3. Step 2: the spare replicas are 4 - 3 = 1. Result: 1, and one more loss leaves 2, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 33. seed 3997901985687508440, level 2

A topic has replication factor 5 and `min.insync.replicas=4`. A producer sends with `acks=all`; 5 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 4
b) 2
c) 1
d) 0

**Key: c**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 5 in sync, minimum 4. Step 1: with `acks=all` writes pass while the in-sync count is at least 4. Step 2: the spare replicas are 5 - 4 = 1. Result: 1, and one more loss leaves 3, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 34. seed 1125001029651674951, level 2

A topic has replication factor 5 and `min.insync.replicas=4`. A producer sends with `acks=all`; 5 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 4
b) 2
c) 1
d) 0

**Key: c**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 5 in sync, minimum 4. Step 1: with `acks=all` writes pass while the in-sync count is at least 4. Step 2: the spare replicas are 5 - 4 = 1. Result: 1, and one more loss leaves 3, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 35. seed 1851648668768851808, level 1

A topic has replication factor 3 and `min.insync.replicas=2`. A producer sends with `acks=0`; 1 replica, leader included, is in sync. Which statement about this write is true?

a) The write is rejected with `NotEnoughReplicas`: `min.insync.replicas` also applies to `acks=0`
b) The write is rejected with `NotEnoughReplicas`: a majority of the 3 replicas must be in sync
c) The write is rejected with `NotEnoughReplicas`: every one of the 3 replicas must be in sync
d) The write is accepted without `NotEnoughReplicas`: only `acks=all` checks the in-sync replica count

**Key: d**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=0`, 1 in sync, minimum 2. Step 1: the minimum is checked only when `acks=all`. Step 2: here it is `acks=0`, so the in-sync count does not matter. Result: the write is accepted. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 36. seed 4383548154247031892, level 1

A topic has replication factor 4 and `min.insync.replicas=3`. A producer sends with `acks=1`; 2 replicas, leader included, are in sync. Which statement about this write is true?

a) The write is accepted without `NotEnoughReplicas`: only `acks=all` checks the in-sync replica count
b) The write is rejected with `NotEnoughReplicas`: every one of the 4 replicas must be in sync
c) The write is rejected with `NotEnoughReplicas`: a majority of the 4 replicas must be in sync
d) The write is rejected with `NotEnoughReplicas`: `min.insync.replicas` also applies to `acks=1`

**Key: a**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=1`, 2 in sync, minimum 3. Step 1: the minimum is checked only when `acks=all`. Step 2: here it is `acks=1`, so the in-sync count does not matter. Result: the write is accepted. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 37. seed 3936296095992799908, level 1

A topic has replication factor 3 and `min.insync.replicas=2`. A producer sends with `acks=all`; 1 replica, leader included, is in sync. Which statement about this write is true?

a) The write is accepted without `NotEnoughReplicas`: the leader holds the record, so the producer can be acknowledged
b) The write is accepted without `NotEnoughReplicas`: `acks=all` waits only for the replicas that are in sync
c) The write is accepted without `NotEnoughReplicas`: `min.insync.replicas` is only a target, not a limit on writes
d) The write is rejected with `NotEnoughReplicas`: 1 replica in sync is fewer than the 2 in `min.insync.replicas`

**Key: d**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=all`, 1 in sync, minimum 2. Step 1: with `acks=all` the minimum is checked. Step 2: 1 in sync is below 2. Result: the write is rejected with `NotEnoughReplicas`. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 38. seed 3821299864712156803, level 2

A topic has replication factor 5 and `min.insync.replicas=3`. A producer sends with `acks=all`; 5 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 1
b) 2
c) 3
d) 4

**Key: b**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 5 in sync, minimum 3. Step 1: with `acks=all` writes pass while the in-sync count is at least 3. Step 2: the spare replicas are 5 - 3 = 2. Result: 2, and one more loss leaves 2, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 39. seed 2824587153472602137, level 1

A topic has replication factor 4 and `min.insync.replicas=3`. A producer sends with `acks=1`; 1 replica, leader included, is in sync. Which statement about this write is true?

a) The write is rejected with `NotEnoughReplicas`: a majority of the 4 replicas must be in sync
b) The write is rejected with `NotEnoughReplicas`: `min.insync.replicas` also applies to `acks=1`
c) The write is accepted without `NotEnoughReplicas`: only `acks=all` checks the in-sync replica count
d) The write is rejected with `NotEnoughReplicas`: every one of the 4 replicas must be in sync

**Key: c**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=1`, 1 in sync, minimum 3. Step 1: the minimum is checked only when `acks=all`. Step 2: here it is `acks=1`, so the in-sync count does not matter. Result: the write is accepted. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 40. seed 4077638099536210854, level 1

A topic has replication factor 5 and `min.insync.replicas=4`. A producer sends with `acks=1`; 1 replica, leader included, is in sync. Which statement about this write is true?

a) The write is rejected with `NotEnoughReplicas`: `min.insync.replicas` also applies to `acks=1`
b) The write is rejected with `NotEnoughReplicas`: every one of the 5 replicas must be in sync
c) The write is rejected with `NotEnoughReplicas`: a majority of the 5 replicas must be in sync
d) The write is accepted without `NotEnoughReplicas`: `acks=1` skips the in-sync check

**Key: d**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=1`, 1 in sync, minimum 4. Step 1: the minimum is checked only when `acks=all`. Step 2: here it is `acks=1`, so the in-sync count does not matter. Result: the write is accepted. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 41. seed 2925323803563839383, level 2

A topic has replication factor 5 and `min.insync.replicas=3`. A producer sends with `acks=all`; 4 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 3
b) 1
c) 0
d) 2

**Key: b**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 4 in sync, minimum 3. Step 1: with `acks=all` writes pass while the in-sync count is at least 3. Step 2: the spare replicas are 4 - 3 = 1. Result: 1, and one more loss leaves 2, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 42. seed 4120352171946087441, level 1

A topic has replication factor 5 and `min.insync.replicas=3`. A producer sends with `acks=all`; 2 replicas, leader included, are in sync. Which statement about this write is true?

a) The write is accepted without `NotEnoughReplicas`: the leader holds the record, so the producer can be acknowledged
b) The write is accepted without `NotEnoughReplicas`: `min.insync.replicas` is only a target, not a limit on writes
c) The write is accepted without `NotEnoughReplicas`: `acks=all` waits only for the replicas that are in sync
d) The write is rejected with `NotEnoughReplicas`: 2 replicas in sync are fewer than the 3 in `min.insync.replicas`

**Key: d**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=all`, 2 in sync, minimum 3. Step 1: with `acks=all` the minimum is checked. Step 2: 2 in sync is below 3. Result: the write is rejected with `NotEnoughReplicas`. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 43. seed 1654182362845181379, level 1

A topic has replication factor 3 and `min.insync.replicas=2`. A producer sends with `acks=0`; 1 replica, leader included, is in sync. Which statement about this write is true?

a) The write is rejected with `NotEnoughReplicas`: a majority of the 3 replicas must be in sync
b) The write is rejected with `NotEnoughReplicas`: every one of the 3 replicas must be in sync
c) The write is accepted without `NotEnoughReplicas`: only `acks=all` checks the in-sync replica count
d) The write is rejected with `NotEnoughReplicas`: `min.insync.replicas` also applies to `acks=0`

**Key: c**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=0`, 1 in sync, minimum 2. Step 1: the minimum is checked only when `acks=all`. Step 2: here it is `acks=0`, so the in-sync count does not matter. Result: the write is accepted. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 44. seed 473125429779081378, level 1

A topic has replication factor 5 and `min.insync.replicas=3`. A producer sends with `acks=1`; 1 replica, leader included, is in sync. Which statement about this write is true?

a) The write is accepted without `NotEnoughReplicas`: `acks=1` skips the in-sync check
b) The write is rejected with `NotEnoughReplicas`: a majority of the 5 replicas must be in sync
c) The write is rejected with `NotEnoughReplicas`: every one of the 5 replicas must be in sync
d) The write is rejected with `NotEnoughReplicas`: `min.insync.replicas` also applies to `acks=1`

**Key: a**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=1`, 1 in sync, minimum 3. Step 1: the minimum is checked only when `acks=all`. Step 2: here it is `acks=1`, so the in-sync count does not matter. Result: the write is accepted. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 45. seed 508596882398660312, level 2

A topic has replication factor 4 and `min.insync.replicas=3`. A producer sends with `acks=all`; 4 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 0
b) 1
c) 2
d) 3

**Key: b**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 4 in sync, minimum 3. Step 1: with `acks=all` writes pass while the in-sync count is at least 3. Step 2: the spare replicas are 4 - 3 = 1. Result: 1, and one more loss leaves 2, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 46. seed 1324300235821521343, level 1

A topic has replication factor 3 and `min.insync.replicas=2`. A producer sends with `acks=all`; 1 replica, leader included, is in sync. Which statement about this write is true?

a) The write is accepted without `NotEnoughReplicas`: `acks=all` waits only for the replicas that are in sync
b) The write is accepted without `NotEnoughReplicas`: the leader holds the record, so the producer can be acknowledged
c) The write is accepted without `NotEnoughReplicas`: `min.insync.replicas` is only a target, not a limit on writes
d) The write is rejected with `NotEnoughReplicas`: 1 replica in sync is fewer than the 2 in `min.insync.replicas`

**Key: d**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=all`, 1 in sync, minimum 2. Step 1: with `acks=all` the minimum is checked. Step 2: 1 in sync is below 2. Result: the write is rejected with `NotEnoughReplicas`. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 47. seed 1213468325779371234, level 2

A topic has replication factor 4 and `min.insync.replicas=3`. A producer sends with `acks=all`; 4 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 0
b) 1
c) 3
d) 2

**Key: b**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 4 in sync, minimum 3. Step 1: with `acks=all` writes pass while the in-sync count is at least 3. Step 2: the spare replicas are 4 - 3 = 1. Result: 1, and one more loss leaves 2, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 48. seed 725028255628305827, level 2

A topic has replication factor 5 and `min.insync.replicas=3`. A producer sends with `acks=all`; 5 replicas, leader included, are in sync. How many more replicas can fall out of sync before writes are rejected?

a) 2
b) 4
c) 1
d) 3

**Key: a**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: 5 in sync, minimum 3. Step 1: with `acks=all` writes pass while the in-sync count is at least 3. Step 2: the spare replicas are 5 - 3 = 2. Result: 2, and one more loss leaves 2, below the minimum. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 49. seed 3803939358332871311, level 1

A topic has replication factor 5 and `min.insync.replicas=3`. A producer sends with `acks=all`; 2 replicas, leader included, are in sync. Which statement about this write is true?

a) The write is accepted without `NotEnoughReplicas`: the leader holds the record, so the producer can be acknowledged
b) The write is rejected with `NotEnoughReplicas`: only 2 replicas in sync, fewer than 3 that `acks=all` needs
c) The write is accepted without `NotEnoughReplicas`: `min.insync.replicas` is only a target, not a limit on writes
d) The write is accepted without `NotEnoughReplicas`: `acks=all` waits only for the replicas that are in sync

**Key: b**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=all`, 2 in sync, minimum 3. Step 1: with `acks=all` the minimum is checked. Step 2: 2 in sync is below 3. Result: the write is rejected with `NotEnoughReplicas`. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.

## 50. seed 3387707173927650595, level 1

A topic has replication factor 5 and `min.insync.replicas=4`. A producer sends with `acks=all`; 3 replicas, leader included, are in sync. Which statement about this write is true?

a) The write is accepted without `NotEnoughReplicas`: `acks=all` waits only for the replicas that are in sync
b) The write is rejected with `NotEnoughReplicas`: only 3 replicas in sync, fewer than 4 that `acks=all` needs
c) The write is accepted without `NotEnoughReplicas`: `min.insync.replicas` is only a target, not a limit on writes
d) The write is accepted without `NotEnoughReplicas`: a majority of the 5 replicas must be in sync

**Key: b**

Explanation: Rule: with `acks=all` the write needs at least `min.insync.replicas` in-sync replicas, the leader included, and `min.insync.replicas` has no effect with `acks=0` or `acks=1`. Inputs: `acks=all`, 3 in sync, minimum 4. Step 1: with `acks=all` the minimum is checked. Step 2: 3 in sync is below 4. Result: the write is rejected with `NotEnoughReplicas`. Source: `kafka-topic-configs#min.insync.replicas`; `kafka-design#availability-and-durability-guarantees`.
