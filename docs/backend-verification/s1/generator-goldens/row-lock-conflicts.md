# Row lock conflicts (`row-lock-conflicts`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 248106135792511938, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) plain `SELECT`
b) `DELETE`
c) `UPDATE`
d) `SELECT ... FOR NO KEY UPDATE`

**Key: a**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: plain `SELECT` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 2. seed 2433433225594487893, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does have to wait?

a) `SELECT ... FOR KEY SHARE`
b) `SELECT ... FOR SHARE`
c) plain `SELECT`
d) `SELECT ... FOR NO KEY UPDATE`

**Key: d**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that waits. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR NO KEY UPDATE` is the only offered statement on the waiting side. The other options come from one misreading: a reader assumes a shared lock stops other shared locks and plain reads. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 3. seed 4479175905430794812, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR UPDATE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR NO KEY UPDATE`
b) `SELECT ... FOR KEY SHARE`
c) `SELECT ... FOR SHARE`
d) plain `SELECT`

**Key: d**

Explanation: Inputs: transaction 1 holds `FOR UPDATE` on the row; the question asks for a statement that does not wait. Rule: a `FOR UPDATE` lock stops every other lock, update and delete on the row, and row-level locks never affect plain reads. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are plain `SELECT`. Result: plain `SELECT` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes weaker lock modes, such as a shared lock, can coexist with it. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 4. seed 3856243483925886774, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR KEY SHARE`
b) `SELECT ... FOR NO KEY UPDATE`
c) `SELECT ... FOR UPDATE`
d) `DELETE`

**Key: a**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR KEY SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 5. seed 2813290990898966615, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does have to wait?

a) `SELECT ... FOR SHARE`
b) `SELECT ... FOR NO KEY UPDATE`
c) `SELECT ... FOR KEY SHARE`
d) plain `SELECT`

**Key: b**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that waits. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR NO KEY UPDATE` is the only offered statement on the waiting side. The other options come from one misreading: a reader assumes a shared lock stops other shared locks and plain reads. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 6. seed 640716177437472707, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `UPDATE`
b) `DELETE`
c) plain `SELECT`
d) `SELECT ... FOR UPDATE`

**Key: c**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: plain `SELECT` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 7. seed 2284809905892830470, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR UPDATE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR SHARE`
b) `SELECT ... FOR NO KEY UPDATE`
c) plain `SELECT`
d) `SELECT ... FOR KEY SHARE`

**Key: c**

Explanation: Inputs: transaction 1 holds `FOR UPDATE` on the row; the question asks for a statement that does not wait. Rule: a `FOR UPDATE` lock stops every other lock, update and delete on the row, and row-level locks never affect plain reads. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are plain `SELECT`. Result: plain `SELECT` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes weaker lock modes, such as a shared lock, can coexist with it. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 8. seed 1570845006040633667, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR NO KEY UPDATE`
b) `DELETE`
c) `SELECT ... FOR SHARE`
d) `SELECT ... FOR UPDATE`

**Key: c**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 9. seed 877531167280005973, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR UPDATE`
b) `SELECT ... FOR NO KEY UPDATE`
c) `UPDATE`
d) `SELECT ... FOR SHARE`

**Key: d**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 10. seed 2836030774171908256, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR UPDATE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR SHARE`
b) plain `SELECT`
c) `SELECT ... FOR NO KEY UPDATE`
d) `SELECT ... FOR KEY SHARE`

**Key: b**

Explanation: Inputs: transaction 1 holds `FOR UPDATE` on the row; the question asks for a statement that does not wait. Rule: a `FOR UPDATE` lock stops every other lock, update and delete on the row, and row-level locks never affect plain reads. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are plain `SELECT`. Result: plain `SELECT` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes weaker lock modes, such as a shared lock, can coexist with it. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 11. seed 25525385164179964, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR NO KEY UPDATE`
b) `SELECT ... FOR SHARE`
c) `SELECT ... FOR UPDATE`
d) `UPDATE`

**Key: b**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 12. seed 1842937880158932692, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `DELETE`
b) `SELECT ... FOR UPDATE`
c) `SELECT ... FOR KEY SHARE`
d) `UPDATE`

**Key: c**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR KEY SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 13. seed 2794511267157383689, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR NO KEY UPDATE`
b) `SELECT ... FOR SHARE`
c) `SELECT ... FOR UPDATE`
d) `UPDATE`

**Key: b**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 14. seed 4321904156487919756, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR UPDATE`
b) `UPDATE`
c) `SELECT ... FOR KEY SHARE`
d) `DELETE`

**Key: c**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR KEY SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 15. seed 1028747736770026808, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR UPDATE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR KEY SHARE`
b) plain `SELECT`
c) `SELECT ... FOR SHARE`
d) `SELECT ... FOR NO KEY UPDATE`

**Key: b**

Explanation: Inputs: transaction 1 holds `FOR UPDATE` on the row; the question asks for a statement that does not wait. Rule: a `FOR UPDATE` lock stops every other lock, update and delete on the row, and row-level locks never affect plain reads. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are plain `SELECT`. Result: plain `SELECT` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes weaker lock modes, such as a shared lock, can coexist with it. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 16. seed 331381528431674784, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `DELETE`
b) plain `SELECT`
c) `SELECT ... FOR NO KEY UPDATE`
d) `UPDATE`

**Key: b**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: plain `SELECT` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 17. seed 1765126553589038840, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `DELETE`
b) plain `SELECT`
c) `UPDATE`
d) `SELECT ... FOR NO KEY UPDATE`

**Key: b**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: plain `SELECT` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 18. seed 1815236088659842509, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `DELETE`
b) `SELECT ... FOR SHARE`
c) `SELECT ... FOR UPDATE`
d) `SELECT ... FOR NO KEY UPDATE`

**Key: b**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 19. seed 3306116803966974101, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `UPDATE`
b) `SELECT ... FOR KEY SHARE`
c) `SELECT ... FOR NO KEY UPDATE`
d) `SELECT ... FOR UPDATE`

**Key: b**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR KEY SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 20. seed 4542359470652335365, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `DELETE`
b) `UPDATE`
c) `SELECT ... FOR NO KEY UPDATE`
d) `SELECT ... FOR SHARE`

**Key: d**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 21. seed 1921522054673450553, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `DELETE`
b) `UPDATE`
c) `SELECT ... FOR SHARE`
d) `SELECT ... FOR UPDATE`

**Key: c**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 22. seed 2913074618693901679, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR NO KEY UPDATE`
b) `UPDATE`
c) `SELECT ... FOR UPDATE`
d) `SELECT ... FOR SHARE`

**Key: d**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 23. seed 2566102787409012673, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR KEY SHARE`
b) `DELETE`
c) `SELECT ... FOR UPDATE`
d) `SELECT ... FOR NO KEY UPDATE`

**Key: a**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR KEY SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 24. seed 3781155229692025539, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does have to wait?

a) `SELECT ... FOR SHARE`
b) plain `SELECT`
c) `SELECT ... FOR KEY SHARE`
d) `SELECT ... FOR NO KEY UPDATE`

**Key: d**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that waits. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR NO KEY UPDATE` is the only offered statement on the waiting side. The other options come from one misreading: a reader assumes a shared lock stops other shared locks and plain reads. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 25. seed 46918429965054017, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does have to wait?

a) plain `SELECT`
b) `SELECT ... FOR KEY SHARE`
c) `SELECT ... FOR NO KEY UPDATE`
d) `SELECT ... FOR SHARE`

**Key: c**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that waits. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR NO KEY UPDATE` is the only offered statement on the waiting side. The other options come from one misreading: a reader assumes a shared lock stops other shared locks and plain reads. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 26. seed 4483093091931690882, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) plain `SELECT`
b) `DELETE`
c) `UPDATE`
d) `SELECT ... FOR NO KEY UPDATE`

**Key: a**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: plain `SELECT` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 27. seed 1637291300464038267, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR UPDATE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR SHARE`
b) plain `SELECT`
c) `SELECT ... FOR NO KEY UPDATE`
d) `SELECT ... FOR KEY SHARE`

**Key: b**

Explanation: Inputs: transaction 1 holds `FOR UPDATE` on the row; the question asks for a statement that does not wait. Rule: a `FOR UPDATE` lock stops every other lock, update and delete on the row, and row-level locks never affect plain reads. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are plain `SELECT`. Result: plain `SELECT` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes weaker lock modes, such as a shared lock, can coexist with it. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 28. seed 1370143096011947688, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR SHARE`
b) `DELETE`
c) `UPDATE`
d) `SELECT ... FOR UPDATE`

**Key: a**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 29. seed 1050590329367194846, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR UPDATE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR NO KEY UPDATE`
b) `SELECT ... FOR KEY SHARE`
c) `SELECT ... FOR SHARE`
d) plain `SELECT`

**Key: d**

Explanation: Inputs: transaction 1 holds `FOR UPDATE` on the row; the question asks for a statement that does not wait. Rule: a `FOR UPDATE` lock stops every other lock, update and delete on the row, and row-level locks never affect plain reads. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are plain `SELECT`. Result: plain `SELECT` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes weaker lock modes, such as a shared lock, can coexist with it. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 30. seed 4289689303270367824, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `DELETE`
b) plain `SELECT`
c) `SELECT ... FOR UPDATE`
d) `UPDATE`

**Key: b**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: plain `SELECT` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 31. seed 3036615236441241631, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does have to wait?

a) `SELECT ... FOR NO KEY UPDATE`
b) `SELECT ... FOR KEY SHARE`
c) `SELECT ... FOR SHARE`
d) plain `SELECT`

**Key: a**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that waits. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR NO KEY UPDATE` is the only offered statement on the waiting side. The other options come from one misreading: a reader assumes a shared lock stops other shared locks and plain reads. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 32. seed 284977703665266420, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) plain `SELECT`
b) `SELECT ... FOR NO KEY UPDATE`
c) `UPDATE`
d) `SELECT ... FOR UPDATE`

**Key: a**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: plain `SELECT` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 33. seed 2313890467657513671, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does have to wait?

a) plain `SELECT`
b) `SELECT ... FOR KEY SHARE`
c) `SELECT ... FOR NO KEY UPDATE`
d) `SELECT ... FOR SHARE`

**Key: c**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that waits. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR NO KEY UPDATE` is the only offered statement on the waiting side. The other options come from one misreading: a reader assumes a shared lock stops other shared locks and plain reads. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 34. seed 464060187034425384, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR NO KEY UPDATE`
b) `DELETE`
c) `SELECT ... FOR UPDATE`
d) `SELECT ... FOR SHARE`

**Key: d**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 35. seed 2224527879035986561, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `DELETE`
b) `UPDATE`
c) `SELECT ... FOR UPDATE`
d) `SELECT ... FOR KEY SHARE`

**Key: d**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR KEY SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 36. seed 3525130851679207706, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR UPDATE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR NO KEY UPDATE`
b) `SELECT ... FOR SHARE`
c) plain `SELECT`
d) `SELECT ... FOR KEY SHARE`

**Key: c**

Explanation: Inputs: transaction 1 holds `FOR UPDATE` on the row; the question asks for a statement that does not wait. Rule: a `FOR UPDATE` lock stops every other lock, update and delete on the row, and row-level locks never affect plain reads. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are plain `SELECT`. Result: plain `SELECT` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes weaker lock modes, such as a shared lock, can coexist with it. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 37. seed 3702741774626021239, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) plain `SELECT`
b) `SELECT ... FOR NO KEY UPDATE`
c) `SELECT ... FOR UPDATE`
d) `DELETE`

**Key: a**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: plain `SELECT` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 38. seed 3137719120317658926, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR NO KEY UPDATE`
b) `UPDATE`
c) `SELECT ... FOR UPDATE`
d) `SELECT ... FOR SHARE`

**Key: d**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 39. seed 2638064827589166906, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `DELETE`
b) `SELECT ... FOR UPDATE`
c) `SELECT ... FOR KEY SHARE`
d) `UPDATE`

**Key: c**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR KEY SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 40. seed 1374219056575704909, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR KEY SHARE`
b) `SELECT ... FOR NO KEY UPDATE`
c) `UPDATE`
d) `SELECT ... FOR UPDATE`

**Key: a**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR KEY SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 41. seed 1693240160876120868, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR KEY SHARE`
b) `DELETE`
c) `UPDATE`
d) `SELECT ... FOR UPDATE`

**Key: a**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR KEY SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 42. seed 2500395662594399156, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR UPDATE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) plain `SELECT`
b) `SELECT ... FOR SHARE`
c) `SELECT ... FOR NO KEY UPDATE`
d) `SELECT ... FOR KEY SHARE`

**Key: a**

Explanation: Inputs: transaction 1 holds `FOR UPDATE` on the row; the question asks for a statement that does not wait. Rule: a `FOR UPDATE` lock stops every other lock, update and delete on the row, and row-level locks never affect plain reads. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are plain `SELECT`. Result: plain `SELECT` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes weaker lock modes, such as a shared lock, can coexist with it. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 43. seed 3162787143662119740, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `UPDATE`
b) `SELECT ... FOR NO KEY UPDATE`
c) `SELECT ... FOR SHARE`
d) `SELECT ... FOR UPDATE`

**Key: c**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 44. seed 3010807895002753838, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR UPDATE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) plain `SELECT`
b) `SELECT ... FOR SHARE`
c) `SELECT ... FOR KEY SHARE`
d) `SELECT ... FOR NO KEY UPDATE`

**Key: a**

Explanation: Inputs: transaction 1 holds `FOR UPDATE` on the row; the question asks for a statement that does not wait. Rule: a `FOR UPDATE` lock stops every other lock, update and delete on the row, and row-level locks never affect plain reads. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are plain `SELECT`. Result: plain `SELECT` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes weaker lock modes, such as a shared lock, can coexist with it. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 45. seed 4509706350417630504, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `UPDATE`
b) `SELECT ... FOR KEY SHARE`
c) `DELETE`
d) `SELECT ... FOR UPDATE`

**Key: b**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR KEY SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 46. seed 3676617051789998104, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `UPDATE`
b) `SELECT ... FOR NO KEY UPDATE`
c) `SELECT ... FOR SHARE`
d) `DELETE`

**Key: c**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 47. seed 1752263593759683021, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR UPDATE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) plain `SELECT`
b) `SELECT ... FOR SHARE`
c) `SELECT ... FOR NO KEY UPDATE`
d) `SELECT ... FOR KEY SHARE`

**Key: a**

Explanation: Inputs: transaction 1 holds `FOR UPDATE` on the row; the question asks for a statement that does not wait. Rule: a `FOR UPDATE` lock stops every other lock, update and delete on the row, and row-level locks never affect plain reads. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are plain `SELECT`. Result: plain `SELECT` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes weaker lock modes, such as a shared lock, can coexist with it. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 48. seed 1275497124016504667, level 1

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR UPDATE`
b) plain `SELECT`
c) `SELECT ... FOR NO KEY UPDATE`
d) `UPDATE`

**Key: b**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: plain `SELECT` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 49. seed 2738892287717520939, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR UPDATE`
b) `SELECT ... FOR NO KEY UPDATE`
c) `SELECT ... FOR SHARE`
d) `DELETE`

**Key: c**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.

## 50. seed 1901889866703940779, level 2

In PostgreSQL, transaction 1 has run `SELECT ... FOR SHARE` on one row and has not finished. Which statement from transaction 2 on that same row does not have to wait?

a) `SELECT ... FOR UPDATE`
b) `SELECT ... FOR NO KEY UPDATE`
c) `UPDATE`
d) `SELECT ... FOR SHARE`

**Key: d**

Explanation: Inputs: transaction 1 holds `FOR SHARE` on the row; the question asks for a statement that does not wait. Rule: a shared lock blocks `UPDATE`, `DELETE`, `FOR UPDATE` and `FOR NO KEY UPDATE`, and lets `FOR SHARE`, `FOR KEY SHARE` and plain reads through. Step 1: the statements that wait are `SELECT ... FOR UPDATE`, `SELECT ... FOR NO KEY UPDATE`, `UPDATE`, `DELETE`. Step 2: the statements that do not wait are `SELECT ... FOR SHARE`, `SELECT ... FOR KEY SHARE`, plain `SELECT`. Result: `SELECT ... FOR SHARE` is the only offered statement on the non-waiting side. The other options come from one misreading: a reader assumes a shared lock is a read lock that nothing has to wait on. Source: `pg-explicit-locking#LOCKING-ROWS`.
