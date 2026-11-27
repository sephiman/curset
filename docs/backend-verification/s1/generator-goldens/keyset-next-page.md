# Keyset pagination (`keyset-next-page`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 767503796135934995, level 2

Rows `(score, id)`: `(50, 15)`, `(50, 55)`, `(50, 85)`, `(70, 26)`, `(90, 68)`, `(90, 91)`. The page before ended at `(50, 55)`. Which ids does `WHERE (score, id) > (50, 55) ORDER BY score, id LIMIT 2` return?

a) `55, 85`
b) `85, 26`
c) `15, 55`
d) `68, 91`

**Key: b**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 55)`: (50, 85), (70, 26), (90, 68), (90, 91). The first 2 in sort order have ids `85, 26`. Wrong options: `15, 55` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `68, 91` is what `WHERE score > 50 AND id > 55` returns under the same `ORDER BY` and `LIMIT`, since it tests the score and the id separately. `55, 85` is what `WHERE (score, id) >= (50, 55)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 2. seed 3039119132660363826, level 2

Rows `(score, id)`: `(70, 39)`, `(70, 67)`, `(70, 76)`, `(90, 34)`, `(90, 38)`, `(90, 79)`. The page before ended at `(70, 67)`. Which ids does `WHERE (score, id) > (70, 67) ORDER BY score, id LIMIT 3` return?

a) `67, 76, 34`
b) `34, 38, 79`
c) `76, 34, 38`
d) `39, 67, 76`

**Key: c**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(70, 67)`: (70, 76), (90, 34), (90, 38), (90, 79). The first 3 in sort order have ids `76, 34, 38`. Wrong options: `34, 38, 79` is what `WHERE score > 70` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `39, 67, 76` is what `WHERE score >= 70` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `67, 76, 34` is what `WHERE (score, id) >= (70, 67)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 3. seed 205726351363170158, level 2

Rows `(score, id)`: `(50, 75)`, `(70, 29)`, `(70, 45)`, `(70, 51)`, `(90, 41)`, `(90, 98)`. The page before ended at `(70, 45)`. Which ids does `WHERE (score, id) > (70, 45) ORDER BY score, id LIMIT 3` return?

a) `29, 45, 51`
b) `75, 51, 98`
c) `51, 41, 98`
d) `45, 51, 41`

**Key: c**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(70, 45)`: (70, 51), (90, 41), (90, 98). The first 3 in sort order have ids `51, 41, 98`. Wrong options: `29, 45, 51` is what `WHERE score >= 70` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `45, 51, 41` is what `WHERE (score, id) >= (70, 45)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. `75, 51, 98` is what `WHERE id > 45` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 4. seed 2694501809816132763, level 2

Rows `(score, id)`: `(50, 40)`, `(50, 69)`, `(70, 16)`, `(70, 72)`, `(90, 49)`, `(90, 61)`. The page before ended at `(50, 40)`. Which ids does `WHERE (score, id) > (50, 40) ORDER BY score, id LIMIT 3` return?

a) `69, 16, 72`
b) `69, 72, 49`
c) `72, 49, 61`
d) `16, 72, 49`

**Key: a**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 40)`: (50, 69), (70, 16), (70, 72), (90, 49), (90, 61). The first 3 in sort order have ids `69, 16, 72`. Wrong options: `16, 72, 49` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `72, 49, 61` is what `WHERE score > 50 AND id > 40` returns under the same `ORDER BY` and `LIMIT`, since it tests the score and the id separately. `69, 72, 49` is what `WHERE id > 40` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 5. seed 54258552136928142, level 2

Rows `(score, id)`: `(50, 59)`, `(50, 85)`, `(50, 93)`, `(70, 26)`, `(70, 97)`, `(90, 96)`. The page before ended at `(50, 85)`. Which ids does `WHERE (score, id) > (50, 85) ORDER BY score, id LIMIT 3` return?

a) `93, 26, 97`
b) `26, 97, 96`
c) `85, 93, 26`
d) `59, 85, 93`

**Key: a**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 85)`: (50, 93), (70, 26), (70, 97), (90, 96). The first 3 in sort order have ids `93, 26, 97`. Wrong options: `26, 97, 96` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `59, 85, 93` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `85, 93, 26` is what `WHERE (score, id) >= (50, 85)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 6. seed 3567601416985765540, level 2

Rows `(score, id)`: `(50, 19)`, `(50, 69)`, `(50, 74)`, `(50, 98)`, `(70, 47)`, `(90, 90)`. The page before ended at `(50, 69)`. Which ids does `WHERE (score, id) > (50, 69) ORDER BY score, id LIMIT 3` return?

a) `74, 98, 47`
b) `19, 69, 74`
c) `74, 98, 90`
d) `69, 74, 98`

**Key: a**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 69)`: (50, 74), (50, 98), (70, 47), (90, 90). The first 3 in sort order have ids `74, 98, 47`. Wrong options: `19, 69, 74` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `69, 74, 98` is what `WHERE (score, id) >= (50, 69)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. `74, 98, 90` is what `WHERE id > 69` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 7. seed 766571584725280944, level 2

Rows `(score, id)`: `(50, 32)`, `(50, 96)`, `(70, 55)`, `(90, 29)`, `(90, 33)`, `(90, 69)`. The page before ended at `(50, 32)`. Which ids does `WHERE (score, id) > (50, 32) ORDER BY score, id LIMIT 3` return?

a) `55, 29, 33`
b) `96, 55, 33`
c) `96, 55, 29`
d) `55, 33, 69`

**Key: c**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 32)`: (50, 96), (70, 55), (90, 29), (90, 33), (90, 69). The first 3 in sort order have ids `96, 55, 29`. Wrong options: `55, 29, 33` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `55, 33, 69` is what `WHERE score > 50 AND id > 32` returns under the same `ORDER BY` and `LIMIT`, since it tests the score and the id separately. `96, 55, 33` is what `WHERE id > 32` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 8. seed 4445091745595046516, level 2

Rows `(score, id)`: `(50, 17)`, `(50, 26)`, `(50, 30)`, `(70, 95)`, `(90, 23)`, `(90, 32)`. The page before ended at `(50, 26)`. Which ids does `WHERE (score, id) > (50, 26) ORDER BY score, id LIMIT 2` return?

a) `95, 23`
b) `95, 32`
c) `26, 30`
d) `30, 95`

**Key: d**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 26)`: (50, 30), (70, 95), (90, 23), (90, 32). The first 2 in sort order have ids `30, 95`. Wrong options: `95, 23` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `95, 32` is what `WHERE score > 50 AND id > 26` returns under the same `ORDER BY` and `LIMIT`, since it tests the score and the id separately. `26, 30` is what `WHERE (score, id) >= (50, 26)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 9. seed 838199404553206374, level 2

Rows `(score, id)`: `(50, 47)`, `(50, 97)`, `(70, 18)`, `(70, 76)`, `(90, 52)`, `(90, 54)`. The page before ended at `(50, 47)`. Which ids does `WHERE (score, id) > (50, 47) ORDER BY score, id LIMIT 2` return?

a) `76, 52`
b) `97, 76`
c) `97, 18`
d) `18, 76`

**Key: c**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 47)`: (50, 97), (70, 18), (70, 76), (90, 52), (90, 54). The first 2 in sort order have ids `97, 18`. Wrong options: `18, 76` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `76, 52` is what `WHERE score > 50 AND id > 47` returns under the same `ORDER BY` and `LIMIT`, since it tests the score and the id separately. `97, 76` is what `WHERE id > 47` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 10. seed 2891277460219569988, level 2

Rows `(score, id)`: `(50, 29)`, `(50, 35)`, `(50, 88)`, `(70, 15)`, `(90, 43)`, `(90, 47)`. The page before ended at `(50, 35)`. Which ids does `WHERE (score, id) > (50, 35) ORDER BY score, id LIMIT 3` return?

a) `15, 43, 47`
b) `35, 88, 15`
c) `88, 43, 47`
d) `88, 15, 43`

**Key: d**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 35)`: (50, 88), (70, 15), (90, 43), (90, 47). The first 3 in sort order have ids `88, 15, 43`. Wrong options: `15, 43, 47` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `35, 88, 15` is what `WHERE (score, id) >= (50, 35)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. `88, 43, 47` is what `WHERE id > 35` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 11. seed 274400345197373611, level 2

Rows `(score, id)`: `(70, 26)`, `(70, 42)`, `(70, 43)`, `(70, 59)`, `(90, 25)`, `(90, 66)`. The page before ended at `(70, 42)`. Which ids does `WHERE (score, id) > (70, 42) ORDER BY score, id LIMIT 2` return?

a) `25, 66`
b) `26, 42`
c) `43, 59`
d) `42, 43`

**Key: c**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(70, 42)`: (70, 43), (70, 59), (90, 25), (90, 66). The first 2 in sort order have ids `43, 59`. Wrong options: `25, 66` is what `WHERE score > 70` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `26, 42` is what `WHERE score >= 70` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `42, 43` is what `WHERE (score, id) >= (70, 42)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 12. seed 2675840265124143235, level 2

Rows `(score, id)`: `(50, 37)`, `(50, 47)`, `(70, 74)`, `(90, 15)`, `(90, 66)`, `(90, 68)`. The page before ended at `(50, 37)`. Which ids does `WHERE (score, id) > (50, 37) ORDER BY score, id LIMIT 3` return?

a) `47, 74, 15`
b) `47, 74, 66`
c) `74, 66, 68`
d) `74, 15, 66`

**Key: a**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 37)`: (50, 47), (70, 74), (90, 15), (90, 66), (90, 68). The first 3 in sort order have ids `47, 74, 15`. Wrong options: `74, 15, 66` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `74, 66, 68` is what `WHERE score > 50 AND id > 37` returns under the same `ORDER BY` and `LIMIT`, since it tests the score and the id separately. `47, 74, 66` is what `WHERE id > 37` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 13. seed 4147848350443822232, level 2

Rows `(score, id)`: `(50, 56)`, `(50, 79)`, `(50, 85)`, `(70, 44)`, `(70, 87)`, `(90, 50)`. The page before ended at `(50, 79)`. Which ids does `WHERE (score, id) > (50, 79) ORDER BY score, id LIMIT 2` return?

a) `85, 87`
b) `85, 44`
c) `44, 87`
d) `56, 79`

**Key: b**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 79)`: (50, 85), (70, 44), (70, 87), (90, 50). The first 2 in sort order have ids `85, 44`. Wrong options: `44, 87` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `56, 79` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `85, 87` is what `WHERE id > 79` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 14. seed 2300612740892450644, level 2

Rows `(score, id)`: `(50, 16)`, `(70, 50)`, `(70, 73)`, `(70, 79)`, `(90, 33)`, `(90, 67)`. The page before ended at `(70, 73)`. Which ids does `WHERE (score, id) > (70, 73) ORDER BY score, id LIMIT 2` return?

a) `50, 73`
b) `79, 33`
c) `73, 79`
d) `33, 67`

**Key: b**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(70, 73)`: (70, 79), (90, 33), (90, 67). The first 2 in sort order have ids `79, 33`. Wrong options: `33, 67` is what `WHERE score > 70` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `50, 73` is what `WHERE score >= 70` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `73, 79` is what `WHERE (score, id) >= (70, 73)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 15. seed 1100153995255893637, level 2

Rows `(score, id)`: `(50, 55)`, `(50, 92)`, `(70, 53)`, `(70, 91)`, `(90, 76)`, `(90, 82)`. The page before ended at `(50, 55)`. Which ids does `WHERE (score, id) > (50, 55) ORDER BY score, id LIMIT 3` return?

a) `53, 91, 76`
b) `91, 76, 82`
c) `92, 53, 91`
d) `92, 91, 76`

**Key: c**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 55)`: (50, 92), (70, 53), (70, 91), (90, 76), (90, 82). The first 3 in sort order have ids `92, 53, 91`. Wrong options: `53, 91, 76` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `91, 76, 82` is what `WHERE score > 50 AND id > 55` returns under the same `ORDER BY` and `LIMIT`, since it tests the score and the id separately. `92, 91, 76` is what `WHERE id > 55` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 16. seed 153079319258547104, level 2

Rows `(score, id)`: `(50, 85)`, `(70, 41)`, `(70, 45)`, `(70, 60)`, `(70, 89)`, `(90, 83)`. The page before ended at `(70, 45)`. Which ids does `WHERE (score, id) > (70, 45) ORDER BY score, id LIMIT 2` return?

a) `45, 60`
b) `41, 45`
c) `60, 89`
d) `85, 60`

**Key: c**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(70, 45)`: (70, 60), (70, 89), (90, 83). The first 2 in sort order have ids `60, 89`. Wrong options: `41, 45` is what `WHERE score >= 70` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `45, 60` is what `WHERE (score, id) >= (70, 45)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. `85, 60` is what `WHERE id > 45` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 17. seed 34114213199020911, level 2

Rows `(score, id)`: `(50, 16)`, `(50, 42)`, `(50, 54)`, `(70, 41)`, `(70, 72)`, `(70, 86)`. The page before ended at `(50, 42)`. Which ids does `WHERE (score, id) > (50, 42) ORDER BY score, id LIMIT 3` return?

a) `42, 54, 41`
b) `54, 72, 86`
c) `16, 42, 54`
d) `54, 41, 72`

**Key: d**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 42)`: (50, 54), (70, 41), (70, 72), (70, 86). The first 3 in sort order have ids `54, 41, 72`. Wrong options: `16, 42, 54` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `42, 54, 41` is what `WHERE (score, id) >= (50, 42)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. `54, 72, 86` is what `WHERE id > 42` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 18. seed 3512871460403089533, level 2

Rows `(score, id)`: `(50, 53)`, `(50, 60)`, `(50, 73)`, `(50, 74)`, `(70, 49)`, `(90, 67)`. The page before ended at `(50, 60)`. Which ids does `WHERE (score, id) > (50, 60) ORDER BY score, id LIMIT 3` return?

a) `73, 74, 49`
b) `53, 60, 73`
c) `60, 73, 74`
d) `73, 74, 67`

**Key: a**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 60)`: (50, 73), (50, 74), (70, 49), (90, 67). The first 3 in sort order have ids `73, 74, 49`. Wrong options: `53, 60, 73` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `60, 73, 74` is what `WHERE (score, id) >= (50, 60)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. `73, 74, 67` is what `WHERE id > 60` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 19. seed 4052032163622832014, level 2

Rows `(score, id)`: `(50, 41)`, `(50, 62)`, `(70, 40)`, `(70, 55)`, `(70, 81)`, `(90, 22)`. The page before ended at `(50, 41)`. Which ids does `WHERE (score, id) > (50, 41) ORDER BY score, id LIMIT 2` return?

a) `55, 81`
b) `40, 55`
c) `62, 55`
d) `62, 40`

**Key: d**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 41)`: (50, 62), (70, 40), (70, 55), (70, 81), (90, 22). The first 2 in sort order have ids `62, 40`. Wrong options: `40, 55` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `55, 81` is what `WHERE score > 50 AND id > 41` returns under the same `ORDER BY` and `LIMIT`, since it tests the score and the id separately. `62, 55` is what `WHERE id > 41` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 20. seed 1172300476223392449, level 2

Rows `(score, id)`: `(50, 32)`, `(50, 52)`, `(50, 94)`, `(70, 22)`, `(70, 97)`, `(90, 34)`. The page before ended at `(50, 52)`. Which ids does `WHERE (score, id) > (50, 52) ORDER BY score, id LIMIT 3` return?

a) `94, 22, 97`
b) `52, 94, 22`
c) `22, 97, 34`
d) `32, 52, 94`

**Key: a**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 52)`: (50, 94), (70, 22), (70, 97), (90, 34). The first 3 in sort order have ids `94, 22, 97`. Wrong options: `22, 97, 34` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `32, 52, 94` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `52, 94, 22` is what `WHERE (score, id) >= (50, 52)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 21. seed 706689996534653104, level 2

Rows `(score, id)`: `(50, 54)`, `(70, 38)`, `(70, 41)`, `(90, 46)`, `(90, 61)`, `(90, 86)`. The page before ended at `(70, 41)`. Which ids does `WHERE (score, id) > (70, 41) ORDER BY score, id LIMIT 3` return?

a) `46, 61, 86`
b) `54, 46, 61`
c) `38, 41, 46`
d) `41, 46, 61`

**Key: a**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(70, 41)`: (90, 46), (90, 61), (90, 86). The first 3 in sort order have ids `46, 61, 86`. Wrong options: `38, 41, 46` is what `WHERE score >= 70` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `41, 46, 61` is what `WHERE (score, id) >= (70, 41)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. `54, 46, 61` is what `WHERE id > 41` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 22. seed 4180344603199591441, level 2

Rows `(score, id)`: `(50, 42)`, `(50, 76)`, `(70, 30)`, `(70, 80)`, `(90, 43)`, `(90, 88)`. The page before ended at `(50, 42)`. Which ids does `WHERE (score, id) > (50, 42) ORDER BY score, id LIMIT 3` return?

a) `76, 80, 43`
b) `30, 80, 43`
c) `76, 30, 80`
d) `80, 43, 88`

**Key: c**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 42)`: (50, 76), (70, 30), (70, 80), (90, 43), (90, 88). The first 3 in sort order have ids `76, 30, 80`. Wrong options: `30, 80, 43` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `80, 43, 88` is what `WHERE score > 50 AND id > 42` returns under the same `ORDER BY` and `LIMIT`, since it tests the score and the id separately. `76, 80, 43` is what `WHERE id > 42` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 23. seed 714826760472642825, level 2

Rows `(score, id)`: `(50, 17)`, `(50, 61)`, `(90, 12)`, `(90, 29)`, `(90, 50)`, `(90, 59)`. The page before ended at `(50, 17)`. Which ids does `WHERE (score, id) > (50, 17) ORDER BY score, id LIMIT 2` return?

a) `29, 50`
b) `61, 12`
c) `12, 29`
d) `61, 29`

**Key: b**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 17)`: (50, 61), (90, 12), (90, 29), (90, 50), (90, 59). The first 2 in sort order have ids `61, 12`. Wrong options: `12, 29` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `29, 50` is what `WHERE score > 50 AND id > 17` returns under the same `ORDER BY` and `LIMIT`, since it tests the score and the id separately. `61, 29` is what `WHERE id > 17` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 24. seed 2806600725258861147, level 2

Rows `(score, id)`: `(50, 41)`, `(50, 73)`, `(50, 87)`, `(70, 17)`, `(90, 36)`, `(90, 37)`. The page before ended at `(50, 73)`. Which ids does `WHERE (score, id) > (50, 73) ORDER BY score, id LIMIT 3` return?

a) `17, 36, 37`
b) `87, 17, 36`
c) `41, 73, 87`
d) `73, 87, 17`

**Key: b**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 73)`: (50, 87), (70, 17), (90, 36), (90, 37). The first 3 in sort order have ids `87, 17, 36`. Wrong options: `17, 36, 37` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `41, 73, 87` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `73, 87, 17` is what `WHERE (score, id) >= (50, 73)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 25. seed 2037508511246701693, level 2

Rows `(score, id)`: `(50, 77)`, `(50, 82)`, `(50, 97)`, `(70, 28)`, `(90, 13)`, `(90, 50)`. The page before ended at `(50, 82)`. Which ids does `WHERE (score, id) > (50, 82) ORDER BY score, id LIMIT 2` return?

a) `28, 13`
b) `82, 97`
c) `77, 82`
d) `97, 28`

**Key: d**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 82)`: (50, 97), (70, 28), (90, 13), (90, 50). The first 2 in sort order have ids `97, 28`. Wrong options: `28, 13` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `77, 82` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `82, 97` is what `WHERE (score, id) >= (50, 82)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 26. seed 97878530644380713, level 2

Rows `(score, id)`: `(50, 52)`, `(70, 15)`, `(70, 24)`, `(90, 29)`, `(90, 41)`, `(90, 70)`. The page before ended at `(70, 24)`. Which ids does `WHERE (score, id) > (70, 24) ORDER BY score, id LIMIT 2` return?

a) `15, 24`
b) `29, 41`
c) `24, 29`
d) `52, 29`

**Key: b**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(70, 24)`: (90, 29), (90, 41), (90, 70). The first 2 in sort order have ids `29, 41`. Wrong options: `15, 24` is what `WHERE score >= 70` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `24, 29` is what `WHERE (score, id) >= (70, 24)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. `52, 29` is what `WHERE id > 24` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 27. seed 3683116241883359834, level 2

Rows `(score, id)`: `(50, 24)`, `(50, 43)`, `(50, 90)`, `(70, 61)`, `(90, 38)`, `(90, 96)`. The page before ended at `(50, 43)`. Which ids does `WHERE (score, id) > (50, 43) ORDER BY score, id LIMIT 2` return?

a) `24, 43`
b) `61, 38`
c) `90, 61`
d) `43, 90`

**Key: c**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 43)`: (50, 90), (70, 61), (90, 38), (90, 96). The first 2 in sort order have ids `90, 61`. Wrong options: `61, 38` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `24, 43` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `43, 90` is what `WHERE (score, id) >= (50, 43)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 28. seed 4505835860217710569, level 2

Rows `(score, id)`: `(50, 51)`, `(50, 71)`, `(70, 32)`, `(70, 64)`, `(90, 66)`, `(90, 87)`. The page before ended at `(50, 51)`. Which ids does `WHERE (score, id) > (50, 51) ORDER BY score, id LIMIT 2` return?

a) `64, 66`
b) `32, 64`
c) `71, 32`
d) `71, 64`

**Key: c**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 51)`: (50, 71), (70, 32), (70, 64), (90, 66), (90, 87). The first 2 in sort order have ids `71, 32`. Wrong options: `32, 64` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `64, 66` is what `WHERE score > 50 AND id > 51` returns under the same `ORDER BY` and `LIMIT`, since it tests the score and the id separately. `71, 64` is what `WHERE id > 51` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 29. seed 1649284889460455233, level 2

Rows `(score, id)`: `(50, 62)`, `(70, 13)`, `(70, 35)`, `(70, 38)`, `(70, 83)`, `(90, 55)`. The page before ended at `(70, 35)`. Which ids does `WHERE (score, id) > (70, 35) ORDER BY score, id LIMIT 3` return?

a) `35, 38, 83`
b) `38, 83, 55`
c) `13, 35, 38`
d) `62, 38, 83`

**Key: b**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(70, 35)`: (70, 38), (70, 83), (90, 55). The first 3 in sort order have ids `38, 83, 55`. Wrong options: `13, 35, 38` is what `WHERE score >= 70` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `35, 38, 83` is what `WHERE (score, id) >= (70, 35)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. `62, 38, 83` is what `WHERE id > 35` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 30. seed 1434271792780466270, level 2

Rows `(score, id)`: `(50, 25)`, `(50, 67)`, `(50, 92)`, `(70, 68)`, `(90, 15)`, `(90, 37)`. The page before ended at `(50, 67)`. Which ids does `WHERE (score, id) > (50, 67) ORDER BY score, id LIMIT 3` return?

a) `25, 67, 92`
b) `68, 15, 37`
c) `67, 92, 68`
d) `92, 68, 15`

**Key: d**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 67)`: (50, 92), (70, 68), (90, 15), (90, 37). The first 3 in sort order have ids `92, 68, 15`. Wrong options: `68, 15, 37` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `25, 67, 92` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `67, 92, 68` is what `WHERE (score, id) >= (50, 67)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 31. seed 915763275340496653, level 2

Rows `(score, id)`: `(50, 11)`, `(50, 28)`, `(50, 92)`, `(70, 25)`, `(90, 16)`, `(90, 60)`. The page before ended at `(50, 28)`. Which ids does `WHERE (score, id) > (50, 28) ORDER BY score, id LIMIT 3` return?

a) `11, 28, 92`
b) `25, 16, 60`
c) `28, 92, 25`
d) `92, 25, 16`

**Key: d**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 28)`: (50, 92), (70, 25), (90, 16), (90, 60). The first 3 in sort order have ids `92, 25, 16`. Wrong options: `25, 16, 60` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `11, 28, 92` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `28, 92, 25` is what `WHERE (score, id) >= (50, 28)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 32. seed 417582034340523383, level 2

Rows `(score, id)`: `(50, 83)`, `(70, 47)`, `(70, 92)`, `(90, 46)`, `(90, 54)`, `(90, 63)`. The page before ended at `(70, 47)`. Which ids does `WHERE (score, id) > (70, 47) ORDER BY score, id LIMIT 2` return?

a) `46, 54`
b) `83, 92`
c) `92, 46`
d) `54, 63`

**Key: c**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(70, 47)`: (70, 92), (90, 46), (90, 54), (90, 63). The first 2 in sort order have ids `92, 46`. Wrong options: `46, 54` is what `WHERE score > 70` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `54, 63` is what `WHERE score > 70 AND id > 47` returns under the same `ORDER BY` and `LIMIT`, since it tests the score and the id separately. `83, 92` is what `WHERE id > 47` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 33. seed 3441044180048725051, level 2

Rows `(score, id)`: `(50, 24)`, `(50, 28)`, `(50, 47)`, `(70, 18)`, `(90, 14)`, `(90, 56)`. The page before ended at `(50, 28)`. Which ids does `WHERE (score, id) > (50, 28) ORDER BY score, id LIMIT 3` return?

a) `47, 18, 14`
b) `24, 28, 47`
c) `18, 14, 56`
d) `28, 47, 18`

**Key: a**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 28)`: (50, 47), (70, 18), (90, 14), (90, 56). The first 3 in sort order have ids `47, 18, 14`. Wrong options: `18, 14, 56` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `24, 28, 47` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `28, 47, 18` is what `WHERE (score, id) >= (50, 28)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 34. seed 1326486921169616601, level 2

Rows `(score, id)`: `(50, 36)`, `(50, 49)`, `(50, 77)`, `(70, 21)`, `(70, 56)`, `(90, 46)`. The page before ended at `(50, 49)`. Which ids does `WHERE (score, id) > (50, 49) ORDER BY score, id LIMIT 3` return?

a) `77, 21, 56`
b) `49, 77, 21`
c) `21, 56, 46`
d) `36, 49, 77`

**Key: a**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 49)`: (50, 77), (70, 21), (70, 56), (90, 46). The first 3 in sort order have ids `77, 21, 56`. Wrong options: `21, 56, 46` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `36, 49, 77` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `49, 77, 21` is what `WHERE (score, id) >= (50, 49)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 35. seed 3037480023554421784, level 2

Rows `(score, id)`: `(50, 37)`, `(90, 18)`, `(90, 30)`, `(90, 44)`, `(90, 69)`, `(90, 90)`. The page before ended at `(90, 30)`. Which ids does `WHERE (score, id) > (90, 30) ORDER BY score, id LIMIT 3` return?

a) `37, 44, 69`
b) `30, 44, 69`
c) `44, 69, 90`
d) `18, 30, 44`

**Key: c**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(90, 30)`: (90, 44), (90, 69), (90, 90). The first 3 in sort order have ids `44, 69, 90`. Wrong options: `18, 30, 44` is what `WHERE score >= 90` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `30, 44, 69` is what `WHERE (score, id) >= (90, 30)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. `37, 44, 69` is what `WHERE id > 30` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 36. seed 3835737339989735120, level 2

Rows `(score, id)`: `(70, 28)`, `(70, 69)`, `(70, 71)`, `(90, 36)`, `(90, 55)`, `(90, 80)`. The page before ended at `(70, 69)`. Which ids does `WHERE (score, id) > (70, 69) ORDER BY score, id LIMIT 3` return?

a) `69, 71, 36`
b) `28, 69, 71`
c) `71, 36, 55`
d) `36, 55, 80`

**Key: c**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(70, 69)`: (70, 71), (90, 36), (90, 55), (90, 80). The first 3 in sort order have ids `71, 36, 55`. Wrong options: `36, 55, 80` is what `WHERE score > 70` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `28, 69, 71` is what `WHERE score >= 70` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `69, 71, 36` is what `WHERE (score, id) >= (70, 69)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 37. seed 936804144803513427, level 2

Rows `(score, id)`: `(50, 53)`, `(50, 57)`, `(70, 28)`, `(70, 71)`, `(70, 83)`, `(90, 73)`. The page before ended at `(50, 53)`. Which ids does `WHERE (score, id) > (50, 53) ORDER BY score, id LIMIT 3` return?

a) `28, 71, 83`
b) `57, 28, 71`
c) `71, 83, 73`
d) `57, 71, 83`

**Key: b**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 53)`: (50, 57), (70, 28), (70, 71), (70, 83), (90, 73). The first 3 in sort order have ids `57, 28, 71`. Wrong options: `28, 71, 83` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `71, 83, 73` is what `WHERE score > 50 AND id > 53` returns under the same `ORDER BY` and `LIMIT`, since it tests the score and the id separately. `57, 71, 83` is what `WHERE id > 53` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 38. seed 1776406525503446985, level 2

Rows `(score, id)`: `(50, 15)`, `(50, 72)`, `(50, 98)`, `(90, 22)`, `(90, 90)`, `(90, 99)`. The page before ended at `(50, 72)`. Which ids does `WHERE (score, id) > (50, 72) ORDER BY score, id LIMIT 2` return?

a) `98, 22`
b) `72, 98`
c) `22, 90`
d) `15, 72`

**Key: a**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 72)`: (50, 98), (90, 22), (90, 90), (90, 99). The first 2 in sort order have ids `98, 22`. Wrong options: `22, 90` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `15, 72` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `72, 98` is what `WHERE (score, id) >= (50, 72)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 39. seed 1759938508639852636, level 2

Rows `(score, id)`: `(50, 95)`, `(70, 42)`, `(70, 47)`, `(90, 24)`, `(90, 67)`, `(90, 76)`. The page before ended at `(70, 47)`. Which ids does `WHERE (score, id) > (70, 47) ORDER BY score, id LIMIT 2` return?

a) `47, 24`
b) `95, 67`
c) `24, 67`
d) `67, 76`

**Key: c**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(70, 47)`: (90, 24), (90, 67), (90, 76). The first 2 in sort order have ids `24, 67`. Wrong options: `67, 76` is what `WHERE score > 70 AND id > 47` returns under the same `ORDER BY` and `LIMIT`, since it tests the score and the id separately. `47, 24` is what `WHERE (score, id) >= (70, 47)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. `95, 67` is what `WHERE id > 47` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 40. seed 726746379632690069, level 2

Rows `(score, id)`: `(50, 15)`, `(50, 52)`, `(50, 94)`, `(70, 78)`, `(90, 40)`, `(90, 58)`. The page before ended at `(50, 52)`. Which ids does `WHERE (score, id) > (50, 52) ORDER BY score, id LIMIT 3` return?

a) `52, 94, 78`
b) `15, 52, 94`
c) `94, 78, 58`
d) `94, 78, 40`

**Key: d**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 52)`: (50, 94), (70, 78), (90, 40), (90, 58). The first 3 in sort order have ids `94, 78, 40`. Wrong options: `15, 52, 94` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `52, 94, 78` is what `WHERE (score, id) >= (50, 52)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. `94, 78, 58` is what `WHERE id > 52` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 41. seed 3328188842231130053, level 2

Rows `(score, id)`: `(50, 86)`, `(70, 37)`, `(70, 48)`, `(70, 67)`, `(90, 64)`, `(90, 72)`. The page before ended at `(70, 48)`. Which ids does `WHERE (score, id) > (70, 48) ORDER BY score, id LIMIT 3` return?

a) `86, 67, 64`
b) `48, 67, 64`
c) `37, 48, 67`
d) `67, 64, 72`

**Key: d**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(70, 48)`: (70, 67), (90, 64), (90, 72). The first 3 in sort order have ids `67, 64, 72`. Wrong options: `37, 48, 67` is what `WHERE score >= 70` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `48, 67, 64` is what `WHERE (score, id) >= (70, 48)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. `86, 67, 64` is what `WHERE id > 48` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 42. seed 2548227061312428282, level 2

Rows `(score, id)`: `(50, 33)`, `(50, 40)`, `(50, 76)`, `(70, 37)`, `(70, 38)`, `(90, 91)`. The page before ended at `(50, 40)`. Which ids does `WHERE (score, id) > (50, 40) ORDER BY score, id LIMIT 2` return?

a) `37, 38`
b) `40, 76`
c) `76, 37`
d) `76, 91`

**Key: c**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 40)`: (50, 76), (70, 37), (70, 38), (90, 91). The first 2 in sort order have ids `76, 37`. Wrong options: `37, 38` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `40, 76` is what `WHERE (score, id) >= (50, 40)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. `76, 91` is what `WHERE id > 40` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 43. seed 3307750022424588903, level 2

Rows `(score, id)`: `(50, 44)`, `(50, 49)`, `(50, 86)`, `(70, 71)`, `(90, 45)`, `(90, 51)`. The page before ended at `(50, 49)`. Which ids does `WHERE (score, id) > (50, 49) ORDER BY score, id LIMIT 2` return?

a) `71, 45`
b) `71, 51`
c) `44, 49`
d) `86, 71`

**Key: d**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 49)`: (50, 86), (70, 71), (90, 45), (90, 51). The first 2 in sort order have ids `86, 71`. Wrong options: `71, 45` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `44, 49` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `71, 51` is what `WHERE score > 50 AND id > 49` returns under the same `ORDER BY` and `LIMIT`, since it tests the score and the id separately. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 44. seed 2320676742433311638, level 2

Rows `(score, id)`: `(50, 18)`, `(50, 89)`, `(90, 14)`, `(90, 40)`, `(90, 49)`, `(90, 70)`. The page before ended at `(50, 18)`. Which ids does `WHERE (score, id) > (50, 18) ORDER BY score, id LIMIT 2` return?

a) `89, 14`
b) `14, 40`
c) `89, 40`
d) `40, 49`

**Key: a**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 18)`: (50, 89), (90, 14), (90, 40), (90, 49), (90, 70). The first 2 in sort order have ids `89, 14`. Wrong options: `14, 40` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `40, 49` is what `WHERE score > 50 AND id > 18` returns under the same `ORDER BY` and `LIMIT`, since it tests the score and the id separately. `89, 40` is what `WHERE id > 18` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 45. seed 1697496878604403661, level 2

Rows `(score, id)`: `(50, 81)`, `(70, 66)`, `(70, 69)`, `(70, 93)`, `(90, 46)`, `(90, 73)`. The page before ended at `(70, 69)`. Which ids does `WHERE (score, id) > (70, 69) ORDER BY score, id LIMIT 3` return?

a) `93, 46, 73`
b) `69, 93, 46`
c) `81, 93, 73`
d) `66, 69, 93`

**Key: a**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(70, 69)`: (70, 93), (90, 46), (90, 73). The first 3 in sort order have ids `93, 46, 73`. Wrong options: `66, 69, 93` is what `WHERE score >= 70` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `69, 93, 46` is what `WHERE (score, id) >= (70, 69)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. `81, 93, 73` is what `WHERE id > 69` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 46. seed 1344099155663921793, level 2

Rows `(score, id)`: `(50, 29)`, `(50, 84)`, `(50, 91)`, `(70, 12)`, `(90, 35)`, `(90, 72)`. The page before ended at `(50, 84)`. Which ids does `WHERE (score, id) > (50, 84) ORDER BY score, id LIMIT 2` return?

a) `29, 84`
b) `84, 91`
c) `12, 35`
d) `91, 12`

**Key: d**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 84)`: (50, 91), (70, 12), (90, 35), (90, 72). The first 2 in sort order have ids `91, 12`. Wrong options: `12, 35` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `29, 84` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `84, 91` is what `WHERE (score, id) >= (50, 84)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 47. seed 4602751739977421320, level 2

Rows `(score, id)`: `(50, 45)`, `(50, 77)`, `(50, 79)`, `(50, 96)`, `(70, 73)`, `(70, 98)`. The page before ended at `(50, 77)`. Which ids does `WHERE (score, id) > (50, 77) ORDER BY score, id LIMIT 3` return?

a) `77, 79, 96`
b) `45, 77, 79`
c) `79, 96, 98`
d) `79, 96, 73`

**Key: d**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 77)`: (50, 79), (50, 96), (70, 73), (70, 98). The first 3 in sort order have ids `79, 96, 73`. Wrong options: `45, 77, 79` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `77, 79, 96` is what `WHERE (score, id) >= (50, 77)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. `79, 96, 98` is what `WHERE id > 77` returns under the same `ORDER BY` and `LIMIT`, since it compares only the id. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 48. seed 1544994634646749149, level 2

Rows `(score, id)`: `(50, 17)`, `(50, 79)`, `(50, 83)`, `(90, 42)`, `(90, 75)`, `(90, 98)`. The page before ended at `(50, 79)`. Which ids does `WHERE (score, id) > (50, 79) ORDER BY score, id LIMIT 3` return?

a) `42, 75, 98`
b) `79, 83, 42`
c) `83, 42, 75`
d) `17, 79, 83`

**Key: c**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 79)`: (50, 83), (90, 42), (90, 75), (90, 98). The first 3 in sort order have ids `83, 42, 75`. Wrong options: `42, 75, 98` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `17, 79, 83` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `79, 83, 42` is what `WHERE (score, id) >= (50, 79)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 49. seed 1032092131357325102, level 2

Rows `(score, id)`: `(70, 25)`, `(70, 39)`, `(70, 51)`, `(70, 82)`, `(90, 17)`, `(90, 45)`. The page before ended at `(70, 39)`. Which ids does `WHERE (score, id) > (70, 39) ORDER BY score, id LIMIT 2` return?

a) `51, 82`
b) `17, 45`
c) `39, 51`
d) `25, 39`

**Key: a**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(70, 39)`: (70, 51), (70, 82), (90, 17), (90, 45). The first 2 in sort order have ids `51, 82`. Wrong options: `17, 45` is what `WHERE score > 70` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `25, 39` is what `WHERE score >= 70` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `39, 51` is what `WHERE (score, id) >= (70, 39)` returns under the same `ORDER BY` and `LIMIT`, since it uses `>=` instead of `>`. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.

## 50. seed 2950776591947618116, level 2

Rows `(score, id)`: `(50, 36)`, `(50, 43)`, `(50, 44)`, `(70, 99)`, `(90, 34)`, `(90, 67)`. The page before ended at `(50, 43)`. Which ids does `WHERE (score, id) > (50, 43) ORDER BY score, id LIMIT 2` return?

a) `99, 67`
b) `44, 99`
c) `36, 43`
d) `99, 34`

**Key: b**

Explanation: A row constructor comparison compares its elements left to right and stops at the first unequal pair, so `(score, id) > (a, b)` keeps a row with a larger score, or with the same score and a larger id. Rows after `(50, 43)`: (50, 44), (70, 99), (90, 34), (90, 67). The first 2 in sort order have ids `44, 99`. Wrong options: `99, 34` is what `WHERE score > 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score. `36, 43` is what `WHERE score >= 50` returns under the same `ORDER BY` and `LIMIT`, since it compares only the score and keeps ties. `99, 67` is what `WHERE score > 50 AND id > 43` returns under the same `ORDER BY` and `LIMIT`, since it tests the score and the id separately. Source: `pg-functions-comparisons#ROW-WISE-COMPARISON`.
