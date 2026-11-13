# Isolation levels and anomalies (`isolation-anomaly`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 3649581409398187884, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL REPEATABLE READ`. Two doctors are on call. T1 and T2 each run `SELECT count(*) FROM on_call`, see 2, and then T1 deletes its own row while T2 deletes the other doctor's row. Both then commit. What is the outcome?

a) Both commit; 0 doctors stay on call in this interleaving
b) Both commit; 1 doctor stays on call
c) The second delete fails with `could not serialize access due to concurrent update`; 1 doctor stays on call
d) One transaction fails with `could not serialize access due to read/write dependencies among transactions`; 1 doctor stays on call, which is what PostgreSQL 18 does at this isolation level

**Key: a**

Explanation: REPEATABLE READ is snapshot isolation: each transaction keeps its snapshot, and the two deletes touch different rows, so neither conflicts. Both commit and no doctor is left; REPEATABLE READ does not prevent this serialization anomaly.

## 2. seed 299756882677063784, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL READ COMMITTED`. T1 runs `SELECT count(*) FROM orders WHERE status = 'open'` and gets 5. T2 inserts one more open order and commits. T1 repeats the same query. What happens?

a) It waits for T2 to commit or roll back before returning anything
b) It returns `6` without waiting for T2
c) It returns `5` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
d) It fails with `could not serialize access due to concurrent update` in this interleaving

**Key: b**

Explanation: At READ COMMITTED each statement takes a new snapshot, so T1's second statement sees T2's committed change and returns 6.

## 3. seed 3369631191795561894, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL REPEATABLE READ`. Two doctors are on call. T1 and T2 each run `SELECT count(*) FROM on_call`, see 2, and then T1 deletes its own row while T2 deletes the other doctor's row. Both then commit. What is the outcome?

a) Both commit; 1 doctor stays on call, which is what PostgreSQL 18 does at this isolation level
b) The second delete fails with `could not serialize access due to concurrent update`; 1 doctor stays on call in this interleaving
c) Both commit; 0 doctors stay on call
d) One transaction fails with `could not serialize access due to read/write dependencies among transactions`; 1 doctor stays on call

**Key: c**

Explanation: REPEATABLE READ is snapshot isolation: each transaction keeps its snapshot, and the two deletes touch different rows, so neither conflicts. Both commit and no doctor is left; REPEATABLE READ does not prevent this serialization anomaly.

## 4. seed 361335532740786851, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL SERIALIZABLE`. Two doctors are on call. T1 and T2 each run `SELECT count(*) FROM on_call`, see 2, and then T1 deletes its own row while T2 deletes the other doctor's row. Both then commit. What is the outcome?

a) Both commit; 0 doctors stay on call
b) The second delete fails with `could not serialize access due to concurrent update`; 1 doctor stays on call, which is what PostgreSQL 18 does at this isolation level
c) One transaction fails with `could not serialize access due to read/write dependencies among transactions`; 1 doctor stays on call
d) The second delete waits for the first to commit, then both commit; 0 doctors stay on call

**Key: c**

Explanation: Each transaction read the rows the other one changed, a read/write dependency cycle that no serial order explains. SERIALIZABLE detects it and rolls one transaction back, leaving 1 doctor on call.

## 5. seed 2392716766376099748, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL REPEATABLE READ`. Two doctors are on call. T1 and T2 each run `SELECT count(*) FROM on_call`, see 2, and then T1 deletes its own row while T2 deletes the other doctor's row. Both then commit. What is the outcome?

a) Both commit; 0 doctors stay on call in this interleaving
b) Both commit; 1 doctor stays on call in this interleaving
c) One transaction fails with `could not serialize access due to read/write dependencies among transactions`; 1 doctor stays on call
d) The second delete waits for the first to commit, then both commit; 0 doctors stay on call, which is what PostgreSQL 18 does at this isolation level

**Key: a**

Explanation: REPEATABLE READ is snapshot isolation: each transaction keeps its snapshot, and the two deletes touch different rows, so neither conflicts. Both commit and no doctor is left; REPEATABLE READ does not prevent this serialization anomaly.

## 6. seed 2950959638632062720, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL REPEATABLE READ`. Two doctors are on call. T1 and T2 each run `SELECT count(*) FROM on_call`, see 2, and then T1 deletes its own row while T2 deletes the other doctor's row. Both then commit. What is the outcome?

a) Both commit; 1 doctor stays on call
b) One transaction fails with `could not serialize access due to read/write dependencies among transactions`; 1 doctor stays on call in this interleaving
c) The second delete waits for the first to commit, then both commit; 0 doctors stay on call, which is what PostgreSQL 18 does at this isolation level
d) Both commit; 0 doctors stay on call

**Key: d**

Explanation: REPEATABLE READ is snapshot isolation: each transaction keeps its snapshot, and the two deletes touch different rows, so neither conflicts. Both commit and no doctor is left; REPEATABLE READ does not prevent this serialization anomaly.

## 7. seed 1561901728123100889, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL READ COMMITTED`. T2 runs `UPDATE accounts SET balance = 350 WHERE id = 1` (balance was 250) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It returns `250` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
b) It fails with `could not serialize access due to concurrent update` in this interleaving
c) It returns `350` without waiting for T2
d) It waits for T2 to commit or roll back before returning anything

**Key: a**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 250.

## 8. seed 4159456951775630142, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL SERIALIZABLE`. T1 runs `SELECT count(*) FROM orders WHERE status = 'open'` and gets 3. T2 inserts one more open order and commits. T1 repeats the same query. What happens?

a) It returns `3` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
b) It fails with `could not serialize access due to concurrent update` in this interleaving
c) It waits for T2 to commit or roll back before returning anything
d) It returns `4` without waiting for T2, which is what PostgreSQL 18 does at this isolation level

**Key: a**

Explanation: At SERIALIZABLE the snapshot is taken at the first statement and kept, so T1 still sees 3. A plain read raises no serialization error; only a transaction that updates a row changed meanwhile does. PostgreSQL's REPEATABLE READ also prevents phantoms.

## 9. seed 40909112816933482, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL REPEATABLE READ`. T2 runs `UPDATE accounts SET balance = 250 WHERE id = 1` (balance was 200) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It waits for T2 to commit or roll back before returning anything, which is what PostgreSQL 18 does at this isolation level
b) It fails with `could not serialize access due to concurrent update` in this interleaving
c) It returns `250` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
d) It returns `200` without waiting for T2, which is what PostgreSQL 18 does at this isolation level

**Key: d**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 200.

## 10. seed 2359536114700481376, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL REPEATABLE READ`. Two doctors are on call. T1 and T2 each run `SELECT count(*) FROM on_call`, see 2, and then T1 deletes its own row while T2 deletes the other doctor's row. Both then commit. What is the outcome?

a) One transaction fails with `could not serialize access due to read/write dependencies among transactions`; 1 doctor stays on call
b) Both commit; 1 doctor stays on call
c) The second delete fails with `could not serialize access due to concurrent update`; 1 doctor stays on call in this interleaving
d) Both commit; 0 doctors stay on call, which is what PostgreSQL 18 does at this isolation level

**Key: d**

Explanation: REPEATABLE READ is snapshot isolation: each transaction keeps its snapshot, and the two deletes touch different rows, so neither conflicts. Both commit and no doctor is left; REPEATABLE READ does not prevent this serialization anomaly.

## 11. seed 1036416336677094025, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL REPEATABLE READ`. T2 runs `UPDATE accounts SET balance = 350 WHERE id = 1` (balance was 250) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It returns `250` without waiting for T2
b) It waits for T2 to commit or roll back before returning anything
c) It fails with `could not serialize access due to concurrent update`, which is what PostgreSQL 18 does at this isolation level
d) It returns `350` without waiting for T2

**Key: a**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 250.

## 12. seed 2659173078427267701, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL SERIALIZABLE`. T1 runs `SELECT count(*) FROM orders WHERE status = 'open'` and gets 3. T2 inserts one more open order and commits. T1 repeats the same query. What happens?

a) It returns `3` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
b) It fails with `could not serialize access due to concurrent update`
c) It waits for T2 to commit or roll back before returning anything
d) It returns `4` without waiting for T2 in this interleaving

**Key: a**

Explanation: At SERIALIZABLE the snapshot is taken at the first statement and kept, so T1 still sees 3. A plain read raises no serialization error; only a transaction that updates a row changed meanwhile does. PostgreSQL's REPEATABLE READ also prevents phantoms.

## 13. seed 2572848780364632590, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL REPEATABLE READ`. T2 runs `UPDATE accounts SET balance = 200 WHERE id = 1` (balance was 100) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It returns `200` without waiting for T2 in this interleaving
b) It fails with `could not serialize access due to concurrent update`
c) It waits for T2 to commit or roll back before returning anything
d) It returns `100` without waiting for T2, which is what PostgreSQL 18 does at this isolation level

**Key: d**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 100.

## 14. seed 1892251862701775226, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL READ UNCOMMITTED`. T2 runs `UPDATE accounts SET balance = 600 WHERE id = 1` (balance was 500) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It returns `600` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
b) It fails with `could not serialize access due to concurrent update`
c) It returns `500` without waiting for T2 in this interleaving
d) It waits for T2 to commit or roll back before returning anything in this interleaving

**Key: c**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 500.

## 15. seed 1897743251986736615, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL REPEATABLE READ`. T2 runs `UPDATE accounts SET balance = 300 WHERE id = 1` (balance was 200) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It returns `300` without waiting for T2
b) It fails with `could not serialize access due to concurrent update` in this interleaving
c) It returns `200` without waiting for T2 in this interleaving
d) It waits for T2 to commit or roll back before returning anything, which is what PostgreSQL 18 does at this isolation level

**Key: c**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 200.

## 16. seed 2668146140696776645, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL REPEATABLE READ`. T2 runs `UPDATE accounts SET balance = 300 WHERE id = 1` (balance was 200) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It returns `200` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
b) It returns `300` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
c) It fails with `could not serialize access due to concurrent update`, which is what PostgreSQL 18 does at this isolation level
d) It waits for T2 to commit or roll back before returning anything in this interleaving

**Key: a**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 200.

## 17. seed 607494865232420759, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL READ UNCOMMITTED`. T2 runs `UPDATE accounts SET balance = 550 WHERE id = 1` (balance was 500) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It returns `500` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
b) It returns `550` without waiting for T2
c) It fails with `could not serialize access due to concurrent update`
d) It waits for T2 to commit or roll back before returning anything in this interleaving

**Key: a**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 500.

## 18. seed 2706858101907150897, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL READ COMMITTED`. T2 runs `UPDATE accounts SET balance = 300 WHERE id = 1` (balance was 250) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It returns `250` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
b) It fails with `could not serialize access due to concurrent update` in this interleaving
c) It returns `300` without waiting for T2
d) It waits for T2 to commit or roll back before returning anything

**Key: a**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 250.

## 19. seed 3524160448737612383, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL READ UNCOMMITTED`. T1 runs `SELECT count(*) FROM orders WHERE status = 'open'` and gets 3. T2 inserts one more open order and commits. T1 repeats the same query. What happens?

a) It returns `3` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
b) It fails with `could not serialize access due to concurrent update`, which is what PostgreSQL 18 does at this isolation level
c) It returns `4` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
d) It waits for T2 to commit or roll back before returning anything

**Key: c**

Explanation: At READ UNCOMMITTED each statement takes a new snapshot, so T1's second statement sees T2's committed change and returns 4 (READ UNCOMMITTED is treated as READ COMMITTED).

## 20. seed 1679384834677527238, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL READ COMMITTED`. T1 runs `SELECT count(*) FROM orders WHERE status = 'open'` and gets 5. T2 inserts one more open order and commits. T1 repeats the same query. What happens?

a) It fails with `could not serialize access due to concurrent update` in this interleaving
b) It waits for T2 to commit or roll back before returning anything in this interleaving
c) It returns `6` without waiting for T2
d) It returns `5` without waiting for T2, which is what PostgreSQL 18 does at this isolation level

**Key: c**

Explanation: At READ COMMITTED each statement takes a new snapshot, so T1's second statement sees T2's committed change and returns 6.

## 21. seed 171238002442308791, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL REPEATABLE READ`. Two doctors are on call. T1 and T2 each run `SELECT count(*) FROM on_call`, see 2, and then T1 deletes its own row while T2 deletes the other doctor's row. Both then commit. What is the outcome?

a) The second delete fails with `could not serialize access due to concurrent update`; 1 doctor stays on call
b) One transaction fails with `could not serialize access due to read/write dependencies among transactions`; 1 doctor stays on call, which is what PostgreSQL 18 does at this isolation level
c) Both commit; 1 doctor stays on call in this interleaving
d) Both commit; 0 doctors stay on call, which is what PostgreSQL 18 does at this isolation level

**Key: d**

Explanation: REPEATABLE READ is snapshot isolation: each transaction keeps its snapshot, and the two deletes touch different rows, so neither conflicts. Both commit and no doctor is left; REPEATABLE READ does not prevent this serialization anomaly.

## 22. seed 3086748574061531906, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL SERIALIZABLE`. Two doctors are on call. T1 and T2 each run `SELECT count(*) FROM on_call`, see 2, and then T1 deletes its own row while T2 deletes the other doctor's row. Both then commit. What is the outcome?

a) Both commit; 0 doctors stay on call
b) The second delete waits for the first to commit, then both commit; 0 doctors stay on call
c) One transaction fails with `could not serialize access due to read/write dependencies among transactions`; 1 doctor stays on call, which is what PostgreSQL 18 does at this isolation level
d) Both commit; 1 doctor stays on call

**Key: c**

Explanation: Each transaction read the rows the other one changed, a read/write dependency cycle that no serial order explains. SERIALIZABLE detects it and rolls one transaction back, leaving 1 doctor on call.

## 23. seed 85753905872588889, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL REPEATABLE READ`. Two doctors are on call. T1 and T2 each run `SELECT count(*) FROM on_call`, see 2, and then T1 deletes its own row while T2 deletes the other doctor's row. Both then commit. What is the outcome?

a) The second delete fails with `could not serialize access due to concurrent update`; 1 doctor stays on call, which is what PostgreSQL 18 does at this isolation level
b) The second delete waits for the first to commit, then both commit; 0 doctors stay on call
c) Both commit; 0 doctors stay on call, which is what PostgreSQL 18 does at this isolation level
d) One transaction fails with `could not serialize access due to read/write dependencies among transactions`; 1 doctor stays on call, which is what PostgreSQL 18 does at this isolation level

**Key: c**

Explanation: REPEATABLE READ is snapshot isolation: each transaction keeps its snapshot, and the two deletes touch different rows, so neither conflicts. Both commit and no doctor is left; REPEATABLE READ does not prevent this serialization anomaly.

## 24. seed 4193742650931012236, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL REPEATABLE READ`. T1 runs `SELECT count(*) FROM orders WHERE status = 'open'` and gets 5. T2 inserts one more open order and commits. T1 repeats the same query. What happens?

a) It fails with `could not serialize access due to concurrent update`, which is what PostgreSQL 18 does at this isolation level
b) It waits for T2 to commit or roll back before returning anything, which is what PostgreSQL 18 does at this isolation level
c) It returns `6` without waiting for T2 in this interleaving
d) It returns `5` without waiting for T2

**Key: d**

Explanation: At REPEATABLE READ the snapshot is taken at the first statement and kept, so T1 still sees 5. A plain read raises no serialization error; only a transaction that updates a row changed meanwhile does. PostgreSQL's REPEATABLE READ also prevents phantoms.

## 25. seed 3456525433345464886, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL READ COMMITTED`. T2 runs `UPDATE accounts SET balance = 600 WHERE id = 1` (balance was 500) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It returns `500` without waiting for T2 in this interleaving
b) It returns `600` without waiting for T2
c) It waits for T2 to commit or roll back before returning anything, which is what PostgreSQL 18 does at this isolation level
d) It fails with `could not serialize access due to concurrent update`, which is what PostgreSQL 18 does at this isolation level

**Key: a**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 500.

## 26. seed 1675615845603683789, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL READ UNCOMMITTED`. T2 runs `UPDATE accounts SET balance = 250 WHERE id = 1` (balance was 200) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It fails with `could not serialize access due to concurrent update` in this interleaving
b) It returns `200` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
c) It waits for T2 to commit or roll back before returning anything
d) It returns `250` without waiting for T2, which is what PostgreSQL 18 does at this isolation level

**Key: b**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 200.

## 27. seed 2816384663681953961, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL READ UNCOMMITTED`. T1 runs `SELECT count(*) FROM orders WHERE status = 'open'` and gets 2. T2 inserts one more open order and commits. T1 repeats the same query. What happens?

a) It returns `2` without waiting for T2 in this interleaving
b) It waits for T2 to commit or roll back before returning anything, which is what PostgreSQL 18 does at this isolation level
c) It fails with `could not serialize access due to concurrent update`
d) It returns `3` without waiting for T2 in this interleaving

**Key: d**

Explanation: At READ UNCOMMITTED each statement takes a new snapshot, so T1's second statement sees T2's committed change and returns 3 (READ UNCOMMITTED is treated as READ COMMITTED).

## 28. seed 505903349479211008, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL SERIALIZABLE`. Two doctors are on call. T1 and T2 each run `SELECT count(*) FROM on_call`, see 2, and then T1 deletes its own row while T2 deletes the other doctor's row. Both then commit. What is the outcome?

a) Both commit; 1 doctor stays on call
b) The second delete waits for the first to commit, then both commit; 0 doctors stay on call, which is what PostgreSQL 18 does at this isolation level
c) One transaction fails with `could not serialize access due to read/write dependencies among transactions`; 1 doctor stays on call
d) Both commit; 0 doctors stay on call, which is what PostgreSQL 18 does at this isolation level

**Key: c**

Explanation: Each transaction read the rows the other one changed, a read/write dependency cycle that no serial order explains. SERIALIZABLE detects it and rolls one transaction back, leaving 1 doctor on call.

## 29. seed 4300111150165049407, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL SERIALIZABLE`. T2 runs `UPDATE accounts SET balance = 300 WHERE id = 1` (balance was 250) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It fails with `could not serialize access due to concurrent update` in this interleaving
b) It waits for T2 to commit or roll back before returning anything
c) It returns `300` without waiting for T2
d) It returns `250` without waiting for T2, which is what PostgreSQL 18 does at this isolation level

**Key: d**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 250.

## 30. seed 1582587342899170656, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL REPEATABLE READ`. Two doctors are on call. T1 and T2 each run `SELECT count(*) FROM on_call`, see 2, and then T1 deletes its own row while T2 deletes the other doctor's row. Both then commit. What is the outcome?

a) The second delete waits for the first to commit, then both commit; 0 doctors stay on call in this interleaving
b) Both commit; 0 doctors stay on call, which is what PostgreSQL 18 does at this isolation level
c) One transaction fails with `could not serialize access due to read/write dependencies among transactions`; 1 doctor stays on call, which is what PostgreSQL 18 does at this isolation level
d) Both commit; 1 doctor stays on call

**Key: b**

Explanation: REPEATABLE READ is snapshot isolation: each transaction keeps its snapshot, and the two deletes touch different rows, so neither conflicts. Both commit and no doctor is left; REPEATABLE READ does not prevent this serialization anomaly.

## 31. seed 4197290010952897020, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL REPEATABLE READ`. T1 reads `SELECT balance FROM accounts WHERE id = 1` and gets 200. T2 runs `UPDATE accounts SET balance = 250 WHERE id = 1` and commits. T1 repeats the same `SELECT`. What happens?

a) It returns `200` without waiting for T2
b) It waits for T2 to commit or roll back before returning anything, which is what PostgreSQL 18 does at this isolation level
c) It fails with `could not serialize access due to concurrent update`
d) It returns `250` without waiting for T2, which is what PostgreSQL 18 does at this isolation level

**Key: a**

Explanation: At REPEATABLE READ the snapshot is taken at the first statement and kept, so T1 still sees 200. A plain read raises no serialization error; only a transaction that updates a row changed meanwhile does.

## 32. seed 1836212547263310725, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL REPEATABLE READ`. T1 runs `SELECT count(*) FROM orders WHERE status = 'open'` and gets 2. T2 inserts one more open order and commits. T1 repeats the same query. What happens?

a) It returns `2` without waiting for T2
b) It fails with `could not serialize access due to concurrent update`, which is what PostgreSQL 18 does at this isolation level
c) It returns `3` without waiting for T2 in this interleaving
d) It waits for T2 to commit or roll back before returning anything

**Key: a**

Explanation: At REPEATABLE READ the snapshot is taken at the first statement and kept, so T1 still sees 2. A plain read raises no serialization error; only a transaction that updates a row changed meanwhile does. PostgreSQL's REPEATABLE READ also prevents phantoms.

## 33. seed 1875499122964313142, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL SERIALIZABLE`. T2 runs `UPDATE accounts SET balance = 350 WHERE id = 1` (balance was 250) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It returns `350` without waiting for T2 in this interleaving
b) It fails with `could not serialize access due to concurrent update`
c) It waits for T2 to commit or roll back before returning anything
d) It returns `250` without waiting for T2 in this interleaving

**Key: d**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 250.

## 34. seed 4550707893795386691, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL SERIALIZABLE`. T2 runs `UPDATE accounts SET balance = 600 WHERE id = 1` (balance was 500) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It returns `600` without waiting for T2 in this interleaving
b) It fails with `could not serialize access due to concurrent update` in this interleaving
c) It returns `500` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
d) It waits for T2 to commit or roll back before returning anything, which is what PostgreSQL 18 does at this isolation level

**Key: c**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 500.

## 35. seed 3527614068491989129, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL READ COMMITTED`. T2 runs `UPDATE accounts SET balance = 550 WHERE id = 1` (balance was 500) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It returns `500` without waiting for T2
b) It fails with `could not serialize access due to concurrent update`
c) It waits for T2 to commit or roll back before returning anything, which is what PostgreSQL 18 does at this isolation level
d) It returns `550` without waiting for T2 in this interleaving

**Key: a**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 500.

## 36. seed 1888584014023163678, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL READ COMMITTED`. T2 runs `UPDATE accounts SET balance = 250 WHERE id = 1` (balance was 200) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It returns `250` without waiting for T2 in this interleaving
b) It fails with `could not serialize access due to concurrent update`, which is what PostgreSQL 18 does at this isolation level
c) It waits for T2 to commit or roll back before returning anything in this interleaving
d) It returns `200` without waiting for T2, which is what PostgreSQL 18 does at this isolation level

**Key: d**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 200.

## 37. seed 165794036477845379, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL REPEATABLE READ`. T2 runs `UPDATE accounts SET balance = 350 WHERE id = 1` (balance was 250) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It fails with `could not serialize access due to concurrent update`, which is what PostgreSQL 18 does at this isolation level
b) It waits for T2 to commit or roll back before returning anything
c) It returns `250` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
d) It returns `350` without waiting for T2, which is what PostgreSQL 18 does at this isolation level

**Key: c**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 250.

## 38. seed 1119569025606099607, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL READ COMMITTED`. T1 reads `SELECT balance FROM accounts WHERE id = 1` and gets 200. T2 runs `UPDATE accounts SET balance = 300 WHERE id = 1` and commits. T1 repeats the same `SELECT`. What happens?

a) It fails with `could not serialize access due to concurrent update`
b) It returns `200` without waiting for T2
c) It returns `300` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
d) It waits for T2 to commit or roll back before returning anything in this interleaving

**Key: c**

Explanation: At READ COMMITTED each statement takes a new snapshot, so T1's second statement sees T2's committed change and returns 300.

## 39. seed 1042286021117061227, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL REPEATABLE READ`. T2 runs `UPDATE accounts SET balance = 600 WHERE id = 1` (balance was 500) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It fails with `could not serialize access due to concurrent update`
b) It waits for T2 to commit or roll back before returning anything, which is what PostgreSQL 18 does at this isolation level
c) It returns `500` without waiting for T2
d) It returns `600` without waiting for T2, which is what PostgreSQL 18 does at this isolation level

**Key: c**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 500.

## 40. seed 2190083854175841137, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL READ COMMITTED`. T2 runs `UPDATE accounts SET balance = 350 WHERE id = 1` (balance was 250) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It waits for T2 to commit or roll back before returning anything
b) It fails with `could not serialize access due to concurrent update`
c) It returns `250` without waiting for T2 in this interleaving
d) It returns `350` without waiting for T2 in this interleaving

**Key: c**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 250.

## 41. seed 3886130370606401987, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL REPEATABLE READ`. T2 runs `UPDATE accounts SET balance = 250 WHERE id = 1` (balance was 200) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It returns `200` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
b) It returns `250` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
c) It waits for T2 to commit or roll back before returning anything
d) It fails with `could not serialize access due to concurrent update`

**Key: a**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 200.

## 42. seed 2081220962175615439, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL READ UNCOMMITTED`. T1 reads `SELECT balance FROM accounts WHERE id = 1` and gets 200. T2 runs `UPDATE accounts SET balance = 250 WHERE id = 1` and commits. T1 repeats the same `SELECT`. What happens?

a) It waits for T2 to commit or roll back before returning anything, which is what PostgreSQL 18 does at this isolation level
b) It returns `200` without waiting for T2
c) It fails with `could not serialize access due to concurrent update` in this interleaving
d) It returns `250` without waiting for T2, which is what PostgreSQL 18 does at this isolation level

**Key: d**

Explanation: At READ UNCOMMITTED each statement takes a new snapshot, so T1's second statement sees T2's committed change and returns 250 (READ UNCOMMITTED is treated as READ COMMITTED).

## 43. seed 4610717141720255547, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL SERIALIZABLE`. T1 runs `SELECT count(*) FROM orders WHERE status = 'open'` and gets 6. T2 inserts one more open order and commits. T1 repeats the same query. What happens?

a) It fails with `could not serialize access due to concurrent update` in this interleaving
b) It waits for T2 to commit or roll back before returning anything in this interleaving
c) It returns `6` without waiting for T2
d) It returns `7` without waiting for T2 in this interleaving

**Key: c**

Explanation: At SERIALIZABLE the snapshot is taken at the first statement and kept, so T1 still sees 6. A plain read raises no serialization error; only a transaction that updates a row changed meanwhile does. PostgreSQL's REPEATABLE READ also prevents phantoms.

## 44. seed 2878249708352913239, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL SERIALIZABLE`. Two doctors are on call. T1 and T2 each run `SELECT count(*) FROM on_call`, see 2, and then T1 deletes its own row while T2 deletes the other doctor's row. Both then commit. What is the outcome?

a) Both commit; 0 doctors stay on call
b) Both commit; 1 doctor stays on call, which is what PostgreSQL 18 does at this isolation level
c) The second delete waits for the first to commit, then both commit; 0 doctors stay on call, which is what PostgreSQL 18 does at this isolation level
d) One transaction fails with `could not serialize access due to read/write dependencies among transactions`; 1 doctor stays on call

**Key: d**

Explanation: Each transaction read the rows the other one changed, a read/write dependency cycle that no serial order explains. SERIALIZABLE detects it and rolls one transaction back, leaving 1 doctor on call.

## 45. seed 2577878500722211297, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL READ UNCOMMITTED`. T2 runs `UPDATE accounts SET balance = 150 WHERE id = 1` (balance was 100) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It waits for T2 to commit or roll back before returning anything, which is what PostgreSQL 18 does at this isolation level
b) It returns `150` without waiting for T2 in this interleaving
c) It returns `100` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
d) It fails with `could not serialize access due to concurrent update`

**Key: c**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 100.

## 46. seed 2428974475598002509, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL READ COMMITTED`. T1 reads `SELECT balance FROM accounts WHERE id = 1` and gets 500. T2 runs `UPDATE accounts SET balance = 550 WHERE id = 1` and commits. T1 repeats the same `SELECT`. What happens?

a) It waits for T2 to commit or roll back before returning anything, which is what PostgreSQL 18 does at this isolation level
b) It returns `550` without waiting for T2
c) It returns `500` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
d) It fails with `could not serialize access due to concurrent update` in this interleaving

**Key: b**

Explanation: At READ COMMITTED each statement takes a new snapshot, so T1's second statement sees T2's committed change and returns 550.

## 47. seed 4224639852173285356, level 1

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL READ UNCOMMITTED`. T2 runs `UPDATE accounts SET balance = 600 WHERE id = 1` (balance was 500) and has not committed. T1 now runs `SELECT balance FROM accounts WHERE id = 1`. What happens?

a) It returns `600` without waiting for T2
b) It waits for T2 to commit or roll back before returning anything
c) It returns `500` without waiting for T2 in this interleaving
d) It fails with `could not serialize access due to concurrent update` in this interleaving

**Key: c**

Explanation: PostgreSQL never shows uncommitted data at any level, and READ UNCOMMITTED behaves like READ COMMITTED. A plain read does not wait for a writer, so T1 sees the committed value 500.

## 48. seed 2477805657907227883, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL SERIALIZABLE`. T1 runs `SELECT count(*) FROM orders WHERE status = 'open'` and gets 6. T2 inserts one more open order and commits. T1 repeats the same query. What happens?

a) It returns `6` without waiting for T2 in this interleaving
b) It returns `7` without waiting for T2
c) It waits for T2 to commit or roll back before returning anything
d) It fails with `could not serialize access due to concurrent update` in this interleaving

**Key: a**

Explanation: At SERIALIZABLE the snapshot is taken at the first statement and kept, so T1 still sees 6. A plain read raises no serialization error; only a transaction that updates a row changed meanwhile does. PostgreSQL's REPEATABLE READ also prevents phantoms.

## 49. seed 459677037479193672, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL SERIALIZABLE`. Two doctors are on call. T1 and T2 each run `SELECT count(*) FROM on_call`, see 2, and then T1 deletes its own row while T2 deletes the other doctor's row. Both then commit. What is the outcome?

a) Both commit; 0 doctors stay on call
b) Both commit; 1 doctor stays on call
c) One transaction fails with `could not serialize access due to read/write dependencies among transactions`; 1 doctor stays on call
d) The second delete waits for the first to commit, then both commit; 0 doctors stay on call, which is what PostgreSQL 18 does at this isolation level

**Key: c**

Explanation: Each transaction read the rows the other one changed, a read/write dependency cycle that no serial order explains. SERIALIZABLE detects it and rolls one transaction back, leaving 1 doctor on call.

## 50. seed 1868078958862515271, level 2

In PostgreSQL 18 both transactions run at `ISOLATION LEVEL READ UNCOMMITTED`. T1 runs `SELECT count(*) FROM orders WHERE status = 'open'` and gets 4. T2 inserts one more open order and commits. T1 repeats the same query. What happens?

a) It returns `5` without waiting for T2, which is what PostgreSQL 18 does at this isolation level
b) It returns `4` without waiting for T2 in this interleaving
c) It fails with `could not serialize access due to concurrent update`, which is what PostgreSQL 18 does at this isolation level
d) It waits for T2 to commit or roll back before returning anything in this interleaving

**Key: a**

Explanation: At READ UNCOMMITTED each statement takes a new snapshot, so T1's second statement sees T2's committed change and returns 5 (READ UNCOMMITTED is treated as READ COMMITTED).
