# Composite index usage (`composite-index-usage`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 2952394530915424205, level 1

A PostgreSQL 18 table has a B-tree index on `(created_at, user_id, region, category)`. A query runs `WHERE created_at = ? AND user_id = ? AND region = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `created_at`, `user_id` and `region`
b) `created_at`, `user_id`, `region` and `category`
c) `region`
d) `created_at`

**Key: a**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `created_at` has an equality, so it bounds the scan and the next column counts too; `user_id` has an equality, so it bounds the scan and the next column counts too; `region` has an equality, so it bounds the scan and the next column counts too; `category` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 2. seed 3813000580339241313, level 2

A PostgreSQL 18 table has a B-tree index on `(region, tenant_id, user_id, created_at)`. A query runs `WHERE region = ? AND tenant_id = ? AND user_id = ? AND created_at = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `created_at`
b) `region`
c) `region`, `tenant_id`, `user_id` and `created_at`
d) `region`, `tenant_id` and `user_id`

**Key: c**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `region` has an equality, so it bounds the scan and the next column counts too; `tenant_id` has an equality, so it bounds the scan and the next column counts too; `user_id` has an equality, so it bounds the scan and the next column counts too; `created_at` has an equality, so it bounds the scan and the next column counts too. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 3. seed 1996323035403701948, level 2

A PostgreSQL 18 table has a B-tree index on `(category, tenant_id, created_at)`. A query runs `WHERE tenant_id = ? AND created_at > ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `category`
b) `category`, `tenant_id` and `created_at`
c) `tenant_id`
d) None of them

**Key: d**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `category` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 4. seed 3690956296012121087, level 2

A PostgreSQL 18 table has a B-tree index on `(status, created_at, user_id, tenant_id)`. A query runs `WHERE status = ? AND created_at > ? AND tenant_id = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `status`, `created_at` and `tenant_id`
b) `status` and `created_at`
c) `status`, `created_at`, `user_id` and `tenant_id`
d) `tenant_id`

**Key: b**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `status` has an equality, so it bounds the scan and the next column counts too; `created_at` has an inequality, which still bounds the scan but ends the prefix. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 5. seed 4258703409435475465, level 2

A PostgreSQL 18 table has a B-tree index on `(user_id, status, created_at, region)`. A query runs `WHERE user_id = ? AND created_at = ? AND region = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `user_id`
b) `user_id`, `status`, `created_at` and `region`
c) None of them
d) `user_id`, `created_at` and `region`

**Key: a**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `user_id` has an equality, so it bounds the scan and the next column counts too; `status` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 6. seed 1419015741279042908, level 2

A PostgreSQL 18 table has a B-tree index on `(created_at, user_id, status, category)`. A query runs `WHERE created_at = ? AND user_id > ? AND category > ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `created_at`, `user_id`, `status` and `category`
b) `category`
c) `created_at` and `user_id`
d) `created_at`

**Key: c**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `created_at` has an equality, so it bounds the scan and the next column counts too; `user_id` has an inequality, which still bounds the scan but ends the prefix. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 7. seed 3560162482155239132, level 2

A PostgreSQL 18 table has a B-tree index on `(created_at, status, region)`. A query runs `WHERE created_at > ? AND region > ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `created_at`, `status` and `region`
b) `created_at`
c) None of them
d) `region`

**Key: b**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `created_at` has an inequality, which still bounds the scan but ends the prefix. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 8. seed 552530805051293483, level 1

A PostgreSQL 18 table has a B-tree index on `(region, category, tenant_id)`. A query runs `WHERE region = ? AND category = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `category`
b) `region`, `category` and `tenant_id`
c) `region`
d) `region` and `category`

**Key: d**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `region` has an equality, so it bounds the scan and the next column counts too; `category` has an equality, so it bounds the scan and the next column counts too; `tenant_id` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 9. seed 3480505339811097560, level 1

A PostgreSQL 18 table has a B-tree index on `(region, category, user_id, tenant_id)`. A query runs `WHERE region = ? AND category = ? AND user_id = ? AND tenant_id = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `tenant_id`
b) `region`, `category` and `user_id`
c) `region`
d) `region`, `category`, `user_id` and `tenant_id`

**Key: d**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `region` has an equality, so it bounds the scan and the next column counts too; `category` has an equality, so it bounds the scan and the next column counts too; `user_id` has an equality, so it bounds the scan and the next column counts too; `tenant_id` has an equality, so it bounds the scan and the next column counts too. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 10. seed 145649618579519102, level 1

A PostgreSQL 18 table has a B-tree index on `(status, tenant_id, category, user_id)`. A query runs `WHERE status = ? AND tenant_id = ? AND user_id = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `status` and `tenant_id`
b) `user_id`
c) `status`, `tenant_id` and `user_id`
d) `status`, `tenant_id`, `category` and `user_id`

**Key: a**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `status` has an equality, so it bounds the scan and the next column counts too; `tenant_id` has an equality, so it bounds the scan and the next column counts too; `category` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 11. seed 1351919544849116019, level 1

A PostgreSQL 18 table has a B-tree index on `(created_at, region, status, tenant_id)`. A query runs `WHERE created_at = ? AND status = ? AND tenant_id = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `tenant_id`
b) `created_at`
c) `created_at`, `region`, `status` and `tenant_id`
d) `created_at`, `status` and `tenant_id`

**Key: b**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `created_at` has an equality, so it bounds the scan and the next column counts too; `region` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 12. seed 1658229318027146976, level 1

A PostgreSQL 18 table has a B-tree index on `(region, user_id, created_at, tenant_id)`. A query runs `WHERE created_at = ? AND tenant_id = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) None of them
b) `region`
c) `created_at`
d) `tenant_id`

**Key: a**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `region` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 13. seed 833878248430944776, level 2

A PostgreSQL 18 table has a B-tree index on `(category, region, user_id, tenant_id)`. A query runs `WHERE region = ? AND user_id > ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `region` and `user_id`
b) None of them
c) `region`
d) `category`, `region`, `user_id` and `tenant_id`

**Key: b**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `category` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 14. seed 1648530210112668297, level 2

A PostgreSQL 18 table has a B-tree index on `(region, user_id, tenant_id, created_at)`. A query runs `WHERE region > ? AND user_id = ? AND tenant_id > ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `tenant_id`
b) `region`, `user_id` and `tenant_id`
c) None of them
d) `region`

**Key: d**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `region` has an inequality, which still bounds the scan but ends the prefix. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 15. seed 1260465692672629842, level 2

A PostgreSQL 18 table has a B-tree index on `(user_id, tenant_id, region)`. A query runs `WHERE user_id = ? AND tenant_id = ? AND region = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `user_id` and `tenant_id`
b) `user_id`
c) `region`
d) `user_id`, `tenant_id` and `region`

**Key: d**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `user_id` has an equality, so it bounds the scan and the next column counts too; `tenant_id` has an equality, so it bounds the scan and the next column counts too; `region` has an equality, so it bounds the scan and the next column counts too. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 16. seed 964964364031363173, level 1

A PostgreSQL 18 table has a B-tree index on `(user_id, tenant_id, region, category)`. A query runs `WHERE user_id = ? AND region = ? AND category = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `user_id`, `region` and `category`
b) `user_id`, `tenant_id`, `region` and `category`
c) `user_id`
d) None of them

**Key: c**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `user_id` has an equality, so it bounds the scan and the next column counts too; `tenant_id` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 17. seed 3900258275030778365, level 1

A PostgreSQL 18 table has a B-tree index on `(created_at, status, tenant_id, region)`. A query runs `WHERE status = ? AND tenant_id = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `status` and `tenant_id`
b) `created_at`
c) `created_at`, `status`, `tenant_id` and `region`
d) None of them

**Key: d**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `created_at` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 18. seed 3516246650236610890, level 2

A PostgreSQL 18 table has a B-tree index on `(user_id, created_at, category)`. A query runs `WHERE user_id > ? AND created_at = ? AND category = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `user_id`, `created_at` and `category`
b) `user_id`
c) `created_at` and `category`
d) None of them

**Key: b**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `user_id` has an inequality, which still bounds the scan but ends the prefix. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 19. seed 2204976265244364403, level 2

A PostgreSQL 18 table has a B-tree index on `(category, user_id, created_at, region)`. A query runs `WHERE category = ? AND user_id > ? AND created_at > ? AND region = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `category` and `user_id`
b) `category`
c) `region`
d) `category`, `user_id`, `created_at` and `region`

**Key: a**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `category` has an equality, so it bounds the scan and the next column counts too; `user_id` has an inequality, which still bounds the scan but ends the prefix. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 20. seed 957594439591378476, level 1

A PostgreSQL 18 table has a B-tree index on `(status, created_at, region, user_id)`. A query runs `WHERE created_at = ? AND region = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) None of them
b) `status`, `created_at`, `region` and `user_id`
c) `created_at` and `region`
d) `region`

**Key: a**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `status` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 21. seed 1395669197395388336, level 1

A PostgreSQL 18 table has a B-tree index on `(created_at, category, region)`. A query runs `WHERE created_at = ? AND region = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `created_at` and `region`
b) `created_at`, `category` and `region`
c) `created_at`
d) None of them

**Key: c**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `created_at` has an equality, so it bounds the scan and the next column counts too; `category` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 22. seed 1499685786961431291, level 2

A PostgreSQL 18 table has a B-tree index on `(tenant_id, region, status)`. A query runs `WHERE tenant_id > ? AND region = ? AND status = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `region` and `status`
b) `status`
c) `tenant_id`
d) None of them

**Key: c**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `tenant_id` has an inequality, which still bounds the scan but ends the prefix. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 23. seed 3267659481725990362, level 2

A PostgreSQL 18 table has a B-tree index on `(category, user_id, status)`. A query runs `WHERE user_id = ? AND status = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `status`
b) `user_id`
c) None of them
d) `category`

**Key: c**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `category` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 24. seed 3241722720332696005, level 2

A PostgreSQL 18 table has a B-tree index on `(created_at, region, category, tenant_id)`. A query runs `WHERE created_at > ? AND region > ? AND category > ? AND tenant_id = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `tenant_id`
b) `created_at`
c) None of them
d) `created_at`, `region`, `category` and `tenant_id`

**Key: b**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `created_at` has an inequality, which still bounds the scan but ends the prefix. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 25. seed 3975671202461322957, level 2

A PostgreSQL 18 table has a B-tree index on `(region, user_id, tenant_id)`. A query runs `WHERE region = ? AND user_id = ? AND tenant_id > ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `region` and `user_id`
b) `tenant_id`
c) `region`, `user_id` and `tenant_id`
d) `region`

**Key: c**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `region` has an equality, so it bounds the scan and the next column counts too; `user_id` has an equality, so it bounds the scan and the next column counts too; `tenant_id` has an inequality, which still bounds the scan but ends the prefix. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 26. seed 2957957725086410560, level 2

A PostgreSQL 18 table has a B-tree index on `(tenant_id, region, user_id)`. A query runs `WHERE tenant_id = ? AND region = ? AND user_id = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `tenant_id`
b) `tenant_id`, `region` and `user_id`
c) `tenant_id` and `region`
d) `user_id`

**Key: b**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `tenant_id` has an equality, so it bounds the scan and the next column counts too; `region` has an equality, so it bounds the scan and the next column counts too; `user_id` has an equality, so it bounds the scan and the next column counts too. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 27. seed 278312081321701738, level 2

A PostgreSQL 18 table has a B-tree index on `(tenant_id, region, category, user_id)`. A query runs `WHERE category > ? AND user_id = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `category`
b) `user_id`
c) `tenant_id`
d) None of them

**Key: d**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `tenant_id` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 28. seed 3848952458910606085, level 2

A PostgreSQL 18 table has a B-tree index on `(region, user_id, status, tenant_id)`. A query runs `WHERE user_id = ? AND status > ? AND tenant_id = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) None of them
b) `region`
c) `user_id` and `tenant_id`
d) `tenant_id`

**Key: a**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `region` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 29. seed 2179247597961716215, level 2

A PostgreSQL 18 table has a B-tree index on `(region, created_at, category)`. A query runs `WHERE region = ? AND created_at > ? AND category = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `region` and `category`
b) `region`, `created_at` and `category`
c) `region`
d) `region` and `created_at`

**Key: d**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `region` has an equality, so it bounds the scan and the next column counts too; `created_at` has an inequality, which still bounds the scan but ends the prefix. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 30. seed 2284203987092746055, level 2

A PostgreSQL 18 table has a B-tree index on `(status, user_id, category)`. A query runs `WHERE status = ? AND user_id > ? AND category > ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `status`
b) `status` and `user_id`
c) `status`, `user_id` and `category`
d) `category`

**Key: b**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `status` has an equality, so it bounds the scan and the next column counts too; `user_id` has an inequality, which still bounds the scan but ends the prefix. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 31. seed 710403330198200883, level 2

A PostgreSQL 18 table has a B-tree index on `(region, status, category, user_id)`. A query runs `WHERE status > ? AND user_id = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `user_id`
b) `status`
c) `region`, `status`, `category` and `user_id`
d) None of them

**Key: d**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `region` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 32. seed 888564068406719858, level 2

A PostgreSQL 18 table has a B-tree index on `(status, created_at, category, user_id)`. A query runs `WHERE status = ? AND created_at = ? AND category > ? AND user_id > ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `status` and `created_at`
b) `status`, `created_at` and `category`
c) `user_id`
d) `status`

**Key: b**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `status` has an equality, so it bounds the scan and the next column counts too; `created_at` has an equality, so it bounds the scan and the next column counts too; `category` has an inequality, which still bounds the scan but ends the prefix. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 33. seed 3711006777098904953, level 2

A PostgreSQL 18 table has a B-tree index on `(created_at, category, tenant_id, status)`. A query runs `WHERE created_at > ? AND category = ? AND tenant_id > ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `created_at`, `category` and `tenant_id`
b) `category`
c) `created_at`
d) `tenant_id`

**Key: c**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `created_at` has an inequality, which still bounds the scan but ends the prefix. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 34. seed 23249749670102550, level 1

A PostgreSQL 18 table has a B-tree index on `(tenant_id, status, region, user_id)`. A query runs `WHERE tenant_id = ? AND status = ? AND region = ? AND user_id = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `tenant_id`, `status`, `region` and `user_id`
b) `tenant_id`, `status` and `region`
c) `user_id`
d) `tenant_id`

**Key: a**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `tenant_id` has an equality, so it bounds the scan and the next column counts too; `status` has an equality, so it bounds the scan and the next column counts too; `region` has an equality, so it bounds the scan and the next column counts too; `user_id` has an equality, so it bounds the scan and the next column counts too. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 35. seed 2816060573864238058, level 2

A PostgreSQL 18 table has a B-tree index on `(tenant_id, region, user_id, category)`. A query runs `WHERE region = ? AND user_id = ? AND category = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `region`
b) `region`, `user_id` and `category`
c) `tenant_id`, `region`, `user_id` and `category`
d) None of them

**Key: d**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `tenant_id` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 36. seed 1302240392148713987, level 2

A PostgreSQL 18 table has a B-tree index on `(tenant_id, user_id, region)`. A query runs `WHERE tenant_id > ? AND user_id = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `user_id`
b) `tenant_id`
c) `tenant_id` and `user_id`
d) `tenant_id`, `user_id` and `region`

**Key: b**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `tenant_id` has an inequality, which still bounds the scan but ends the prefix. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 37. seed 2932635073248771884, level 1

A PostgreSQL 18 table has a B-tree index on `(created_at, tenant_id, region)`. A query runs `WHERE created_at = ? AND region = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) None of them
b) `region`
c) `created_at`
d) `created_at` and `region`

**Key: c**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `created_at` has an equality, so it bounds the scan and the next column counts too; `tenant_id` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 38. seed 754068846100501347, level 1

A PostgreSQL 18 table has a B-tree index on `(created_at, tenant_id, region, status)`. A query runs `WHERE created_at = ? AND region = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `region`
b) `created_at`
c) `created_at`, `tenant_id`, `region` and `status`
d) `created_at` and `region`

**Key: b**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `created_at` has an equality, so it bounds the scan and the next column counts too; `tenant_id` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 39. seed 2639081228051782078, level 2

A PostgreSQL 18 table has a B-tree index on `(category, region, tenant_id)`. A query runs `WHERE category = ? AND region = ? AND tenant_id > ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `category`
b) `tenant_id`
c) `category`, `region` and `tenant_id`
d) `category` and `region`

**Key: c**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `category` has an equality, so it bounds the scan and the next column counts too; `region` has an equality, so it bounds the scan and the next column counts too; `tenant_id` has an inequality, which still bounds the scan but ends the prefix. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 40. seed 2411186282788660825, level 2

A PostgreSQL 18 table has a B-tree index on `(status, region, tenant_id, created_at)`. A query runs `WHERE tenant_id > ? AND created_at = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) None of them
b) `created_at`
c) `status`
d) `tenant_id` and `created_at`

**Key: a**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `status` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 41. seed 2108148173642631859, level 1

A PostgreSQL 18 table has a B-tree index on `(status, tenant_id, user_id)`. A query runs `WHERE tenant_id = ? AND user_id = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `tenant_id` and `user_id`
b) `status`, `tenant_id` and `user_id`
c) None of them
d) `user_id`

**Key: c**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `status` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 42. seed 63569957405865024, level 2

A PostgreSQL 18 table has a B-tree index on `(category, user_id, tenant_id, status)`. A query runs `WHERE category = ? AND user_id = ? AND tenant_id > ? AND status = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `category`, `user_id` and `tenant_id`
b) `category` and `user_id`
c) `status`
d) `category`

**Key: a**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `category` has an equality, so it bounds the scan and the next column counts too; `user_id` has an equality, so it bounds the scan and the next column counts too; `tenant_id` has an inequality, which still bounds the scan but ends the prefix. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 43. seed 3446925463612640581, level 2

A PostgreSQL 18 table has a B-tree index on `(user_id, status, tenant_id)`. A query runs `WHERE user_id = ? AND status = ? AND tenant_id = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `user_id`
b) `user_id` and `status`
c) `user_id`, `status` and `tenant_id`
d) `tenant_id`

**Key: c**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `user_id` has an equality, so it bounds the scan and the next column counts too; `status` has an equality, so it bounds the scan and the next column counts too; `tenant_id` has an equality, so it bounds the scan and the next column counts too. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 44. seed 3837664639966922266, level 1

A PostgreSQL 18 table has a B-tree index on `(category, region, user_id)`. A query runs `WHERE category = ? AND region = ? AND user_id = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `category` and `region`
b) `user_id`
c) `category`
d) `category`, `region` and `user_id`

**Key: d**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `category` has an equality, so it bounds the scan and the next column counts too; `region` has an equality, so it bounds the scan and the next column counts too; `user_id` has an equality, so it bounds the scan and the next column counts too. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 45. seed 3336444398994764000, level 1

A PostgreSQL 18 table has a B-tree index on `(created_at, user_id, status)`. A query runs `WHERE created_at = ? AND user_id = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `created_at` and `user_id`
b) `created_at`
c) `created_at`, `user_id` and `status`
d) `user_id`

**Key: a**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `created_at` has an equality, so it bounds the scan and the next column counts too; `user_id` has an equality, so it bounds the scan and the next column counts too; `status` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 46. seed 1782889277488276725, level 1

A PostgreSQL 18 table has a B-tree index on `(created_at, tenant_id, status, category)`. A query runs `WHERE tenant_id = ? AND status = ? AND category = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `created_at`
b) `created_at`, `tenant_id`, `status` and `category`
c) None of them
d) `tenant_id`, `status` and `category`

**Key: c**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `created_at` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 47. seed 649205894746905369, level 2

A PostgreSQL 18 table has a B-tree index on `(created_at, category, user_id)`. A query runs `WHERE created_at = ? AND category > ? AND user_id > ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `created_at` and `category`
b) `created_at`, `category` and `user_id`
c) `user_id`
d) `created_at`

**Key: a**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `created_at` has an equality, so it bounds the scan and the next column counts too; `category` has an inequality, which still bounds the scan but ends the prefix. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 48. seed 400050115834150098, level 2

A PostgreSQL 18 table has a B-tree index on `(status, region, created_at)`. A query runs `WHERE status = ? AND created_at = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `status`
b) `created_at`
c) None of them
d) `status` and `created_at`

**Key: a**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `status` has an equality, so it bounds the scan and the next column counts too; `region` has no condition, so the leading prefix ends here. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 49. seed 1802257182332091365, level 2

A PostgreSQL 18 table has a B-tree index on `(category, created_at, status)`. A query runs `WHERE category > ? AND created_at > ? AND status = ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `category`
b) None of them
c) `status`
d) `category`, `created_at` and `status`

**Key: a**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `category` has an inequality, which still bounds the scan but ends the prefix. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.

## 50. seed 1295677240829227683, level 2

A PostgreSQL 18 table has a B-tree index on `(user_id, created_at, category)`. A query runs `WHERE user_id = ? AND created_at > ? AND category > ?`. Which columns' conditions are guaranteed to limit the portion of the index that is scanned, ignoring skip scan?

a) `category`
b) `user_id` and `created_at`
c) `user_id`, `created_at` and `category`
d) `user_id`

**Key: b**

Explanation: The rule: equality conditions on leading columns, plus an inequality on the first column without an equality, limit the scanned range. Going through the index in order: `user_id` has an equality, so it bounds the scan and the next column counts too; `created_at` has an inequality, which still bounds the scan but ends the prefix. Conditions on later columns are only checked inside the index: they save table visits but do not shrink the scanned range.
