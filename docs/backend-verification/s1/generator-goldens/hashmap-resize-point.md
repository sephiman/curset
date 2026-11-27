# Hash table resizing (`hashmap-resize-point`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 981326540181914396, level 1

A table follows the `HashMap` rule: 32 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the first time?

a) insert number 32
b) insert 16
c) 33
d) insert number 17

**Key: d**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 32 buckets that limit is 32 x 0.5 = 16. Entry 16 still fits, so entry 17 is the first to exceed it. Answer: 17. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 2. seed 1417657673873137765, level 2

A table follows the `HashMap` rule: 8 buckets, load factor `0.75`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) insert 16
b) insert 7
c) insert number 17
d) insert 13

**Key: d**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 8 buckets that limit is 8 x 0.75 = 6. The first doubling gives 16 buckets, so the limit becomes 16 x 0.75 = 12. Entry 12 still fits, so entry 13 doubles the table again. Answer: 13. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 3. seed 3644675880063450126, level 2

A table follows the `HashMap` rule: 16 buckets, load factor `0.75`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) 33
b) insert 13
c) insert 25
d) 24

**Key: c**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.75 = 12. The first doubling gives 32 buckets, so the limit becomes 32 x 0.75 = 24. Entry 24 still fits, so entry 25 doubles the table again. Answer: 25. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 4. seed 3357714568073677863, level 2

A table follows the `HashMap` rule: 32 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) 65
b) insert 33
c) 32
d) insert number 64

**Key: b**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 32 buckets that limit is 32 x 0.5 = 16. The first doubling gives 64 buckets, so the limit becomes 64 x 0.5 = 32. Entry 32 still fits, so entry 33 doubles the table again. Answer: 33. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 5. seed 2868384519405584173, level 1

A table follows the `HashMap` rule: 32 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the first time?

a) 16
b) insert 17
c) insert 32
d) insert number 33

**Key: b**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 32 buckets that limit is 32 x 0.5 = 16. Entry 16 still fits, so entry 17 is the first to exceed it. Answer: 17. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 6. seed 36127895823011743, level 1

A table follows the `HashMap` rule: 8 buckets, load factor `0.75`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the first time?

a) insert number 6
b) insert number 9
c) 7
d) 13

**Key: c**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 8 buckets that limit is 8 x 0.75 = 6. Entry 6 still fits, so entry 7 is the first to exceed it. Answer: 7. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 7. seed 2726459654230741004, level 2

A table follows the `HashMap` rule: 32 buckets, load factor `0.75`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) insert 49
b) insert 64
c) insert 25
d) insert number 65

**Key: a**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 32 buckets that limit is 32 x 0.75 = 24. The first doubling gives 64 buckets, so the limit becomes 64 x 0.75 = 48. Entry 48 still fits, so entry 49 doubles the table again. Answer: 49. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 8. seed 184815819299545661, level 1

A table follows the `HashMap` rule: 16 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the first time?

a) insert number 17
b) 9
c) insert 16
d) insert number 8

**Key: b**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.5 = 8. Entry 8 still fits, so entry 9 is the first to exceed it. Answer: 9. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 9. seed 3231336861149409583, level 2

A table follows the `HashMap` rule: 16 buckets, load factor `0.75`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) insert 32
b) 25
c) insert number 24
d) insert number 33

**Key: b**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.75 = 12. The first doubling gives 32 buckets, so the limit becomes 32 x 0.75 = 24. Entry 24 still fits, so entry 25 doubles the table again. Answer: 25. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 10. seed 518361843547806878, level 2

A table follows the `HashMap` rule: 16 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) insert number 9
b) insert number 33
c) 16
d) insert 17

**Key: d**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.5 = 8. The first doubling gives 32 buckets, so the limit becomes 32 x 0.5 = 16. Entry 16 still fits, so entry 17 doubles the table again. Answer: 17. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 11. seed 3468013027322992070, level 2

A table follows the `HashMap` rule: 8 buckets, load factor `0.75`, buckets double once entries exceed load factor times buckets. The bucket is `key mod buckets`. After 15 distinct keys, in which bucket does key `90` sit?

a) bucket 2
b) bucket 26
c) bucket number 0
d) bucket number 18

**Key: b**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 8 buckets that limit is 8 x 0.75 = 6. 1. entry 7 exceeds 6, so the table has 16 buckets; 2. entry 13 exceeds 12, so the table has 32 buckets. The table has 32 buckets, so the key 90 goes to bucket 90 mod 32 = 26. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 12. seed 3573796881794273722, level 1

A table follows the `HashMap` rule: 8 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. After 10 distinct keys are inserted, how many buckets does it have?

a) 8 buckets in total
b) 24
c) 32 buckets in total
d) 64 buckets

**Key: c**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 8 buckets that limit is 8 x 0.5 = 4. 1. entry 5 exceeds 4, so the table has 16 buckets; 2. entry 9 exceeds 8, so the table has 32 buckets. After 10 entries the table has 32 buckets. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 13. seed 4440437166324755491, level 1

A table follows the `HashMap` rule: 16 buckets, load factor `0.75`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the first time?

a) insert 13
b) insert number 17
c) insert 25
d) insert 16

**Key: a**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.75 = 12. Entry 12 still fits, so entry 13 is the first to exceed it. Answer: 13. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 14. seed 724932577736185713, level 1

A table follows the `HashMap` rule: 8 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. After 9 distinct keys are inserted, how many buckets does it have?

a) 8
b) 32
c) 64 buckets in total
d) 24 buckets

**Key: b**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 8 buckets that limit is 8 x 0.5 = 4. 1. entry 5 exceeds 4, so the table has 16 buckets; 2. entry 9 exceeds 8, so the table has 32 buckets. After 9 entries the table has 32 buckets. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 15. seed 341370882140052431, level 1

A table follows the `HashMap` rule: 16 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the first time?

a) insert number 8
b) insert number 17
c) insert 16
d) 9

**Key: d**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.5 = 8. Entry 8 still fits, so entry 9 is the first to exceed it. Answer: 9. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 16. seed 3209394443248988467, level 1

A table follows the `HashMap` rule: 16 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. After 17 distinct keys are inserted, how many buckets does it have?

a) 64 buckets in total
b) 48 buckets
c) 128
d) 16 buckets in total

**Key: a**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.5 = 8. 1. entry 9 exceeds 8, so the table has 32 buckets; 2. entry 17 exceeds 16, so the table has 64 buckets. After 17 entries the table has 64 buckets. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 17. seed 1373008386850570265, level 1

A table follows the `HashMap` rule: 16 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. After 18 distinct keys are inserted, how many buckets does it have?

a) 16
b) 64
c) 48 buckets in total
d) 128 buckets

**Key: b**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.5 = 8. 1. entry 9 exceeds 8, so the table has 32 buckets; 2. entry 17 exceeds 16, so the table has 64 buckets. After 18 entries the table has 64 buckets. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 18. seed 2817531644829445672, level 2

A table follows the `HashMap` rule: 16 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) 32
b) 17
c) insert 33
d) insert 9

**Key: b**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.5 = 8. The first doubling gives 32 buckets, so the limit becomes 32 x 0.5 = 16. Entry 16 still fits, so entry 17 doubles the table again. Answer: 17. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 19. seed 750928941954492764, level 2

A table follows the `HashMap` rule: 16 buckets, load factor `0.75`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) insert number 13
b) insert 33
c) insert number 25
d) insert 24

**Key: c**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.75 = 12. The first doubling gives 32 buckets, so the limit becomes 32 x 0.75 = 24. Entry 24 still fits, so entry 25 doubles the table again. Answer: 25. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 20. seed 2363819300670879033, level 1

A table follows the `HashMap` rule: 8 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the first time?

a) insert number 9
b) insert 8
c) 4
d) insert 5

**Key: d**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 8 buckets that limit is 8 x 0.5 = 4. Entry 4 still fits, so entry 5 is the first to exceed it. Answer: 5. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 21. seed 3166921426111086064, level 1

A table follows the `HashMap` rule: 16 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. After 18 distinct keys are inserted, how many buckets does it have?

a) 64 buckets in total
b) 128
c) 16 buckets in total
d) 48 buckets

**Key: a**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.5 = 8. 1. entry 9 exceeds 8, so the table has 32 buckets; 2. entry 17 exceeds 16, so the table has 64 buckets. After 18 entries the table has 64 buckets. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 22. seed 1132432714697666028, level 1

A table follows the `HashMap` rule: 8 buckets, load factor `0.75`, buckets double once entries exceed load factor times buckets. After 13 distinct keys are inserted, how many buckets does it have?

a) 24 buckets
b) 64 buckets in total
c) 8
d) 32

**Key: d**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 8 buckets that limit is 8 x 0.75 = 6. 1. entry 7 exceeds 6, so the table has 16 buckets; 2. entry 13 exceeds 12, so the table has 32 buckets. After 13 entries the table has 32 buckets. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 23. seed 4550742542144400239, level 2

A table follows the `HashMap` rule: 16 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) insert 33
b) insert 9
c) 17
d) insert number 16

**Key: c**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.5 = 8. The first doubling gives 32 buckets, so the limit becomes 32 x 0.5 = 16. Entry 16 still fits, so entry 17 doubles the table again. Answer: 17. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 24. seed 2991931795863402795, level 1

A table follows the `HashMap` rule: 16 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the first time?

a) 9
b) insert 16
c) insert number 8
d) insert number 17

**Key: a**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.5 = 8. Entry 8 still fits, so entry 9 is the first to exceed it. Answer: 9. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 25. seed 695431508633756337, level 2

A table follows the `HashMap` rule: 16 buckets, load factor `0.75`, buckets double once entries exceed load factor times buckets. The bucket is `key mod buckets`. After 25 distinct keys, in which bucket does key `121` sit?

a) 21
b) bucket 121
c) 57
d) bucket 25

**Key: c**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.75 = 12. 1. entry 13 exceeds 12, so the table has 32 buckets; 2. entry 25 exceeds 24, so the table has 64 buckets. The table has 64 buckets, so the key 121 goes to bucket 121 mod 64 = 57. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 26. seed 3753413582746956090, level 2

A table follows the `HashMap` rule: 16 buckets, load factor `0.75`, buckets double once entries exceed load factor times buckets. The bucket is `key mod buckets`. After 25 distinct keys, in which bucket does key `95` sit?

a) 47
b) bucket 15
c) 11
d) bucket number 31

**Key: d**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.75 = 12. 1. entry 13 exceeds 12, so the table has 32 buckets; 2. entry 25 exceeds 24, so the table has 64 buckets. The table has 64 buckets, so the key 95 goes to bucket 95 mod 64 = 31. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 27. seed 1086801237044278942, level 2

A table follows the `HashMap` rule: 16 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) insert 9
b) insert 33
c) 17
d) insert number 16

**Key: c**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.5 = 8. The first doubling gives 32 buckets, so the limit becomes 32 x 0.5 = 16. Entry 16 still fits, so entry 17 doubles the table again. Answer: 17. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 28. seed 4335545123366273685, level 2

A table follows the `HashMap` rule: 16 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) insert 32
b) insert number 9
c) insert number 33
d) insert 17

**Key: d**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.5 = 8. The first doubling gives 32 buckets, so the limit becomes 32 x 0.5 = 16. Entry 16 still fits, so entry 17 doubles the table again. Answer: 17. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 29. seed 4076561455645463396, level 2

A table follows the `HashMap` rule: 16 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) insert 32
b) insert 17
c) insert number 33
d) insert number 9

**Key: b**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.5 = 8. The first doubling gives 32 buckets, so the limit becomes 32 x 0.5 = 16. Entry 16 still fits, so entry 17 doubles the table again. Answer: 17. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 30. seed 4434805470679859588, level 2

A table follows the `HashMap` rule: 32 buckets, load factor `0.75`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) 48
b) insert 25
c) insert 49
d) insert 64

**Key: c**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 32 buckets that limit is 32 x 0.75 = 24. The first doubling gives 64 buckets, so the limit becomes 64 x 0.75 = 48. Entry 48 still fits, so entry 49 doubles the table again. Answer: 49. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 31. seed 3175443247710448014, level 2

A table follows the `HashMap` rule: 16 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. The bucket is `key mod buckets`. After 10 distinct keys, in which bucket does key `56` sit?

a) bucket 6
b) bucket 0
c) bucket 24
d) 56

**Key: c**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.5 = 8. 1. entry 9 exceeds 8, so the table has 32 buckets. The table has 32 buckets, so the key 56 goes to bucket 56 mod 32 = 24. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 32. seed 2732952475088446401, level 1

A table follows the `HashMap` rule: 16 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the first time?

a) insert 17
b) 16
c) insert number 9
d) insert 8

**Key: c**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.5 = 8. Entry 8 still fits, so entry 9 is the first to exceed it. Answer: 9. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 33. seed 819353720618120275, level 2

A table follows the `HashMap` rule: 8 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. The bucket is `key mod buckets`. After 6 distinct keys, in which bucket does key `54` sit?

a) bucket 2
b) bucket number 0
c) 22
d) bucket number 6

**Key: d**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 8 buckets that limit is 8 x 0.5 = 4. 1. entry 5 exceeds 4, so the table has 16 buckets. The table has 16 buckets, so the key 54 goes to bucket 54 mod 16 = 6. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 34. seed 4534970432238300864, level 2

A table follows the `HashMap` rule: 32 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) insert number 33
b) insert 17
c) insert 32
d) insert 65

**Key: a**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 32 buckets that limit is 32 x 0.5 = 16. The first doubling gives 64 buckets, so the limit becomes 64 x 0.5 = 32. Entry 32 still fits, so entry 33 doubles the table again. Answer: 33. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 35. seed 3539081055900909375, level 2

A table follows the `HashMap` rule: 32 buckets, load factor `0.75`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) insert 65
b) 49
c) 25
d) 64

**Key: b**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 32 buckets that limit is 32 x 0.75 = 24. The first doubling gives 64 buckets, so the limit becomes 64 x 0.75 = 48. Entry 48 still fits, so entry 49 doubles the table again. Answer: 49. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 36. seed 799671226090603737, level 2

A table follows the `HashMap` rule: 16 buckets, load factor `0.75`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) 25
b) insert number 33
c) insert number 24
d) 13

**Key: a**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.75 = 12. The first doubling gives 32 buckets, so the limit becomes 32 x 0.75 = 24. Entry 24 still fits, so entry 25 doubles the table again. Answer: 25. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 37. seed 2983642205723350144, level 2

A table follows the `HashMap` rule: 32 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. The bucket is `key mod buckets`. After 18 distinct keys, in which bucket does key `224` sit?

a) bucket 96
b) bucket 0
c) 32
d) 8

**Key: c**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 32 buckets that limit is 32 x 0.5 = 16. 1. entry 17 exceeds 16, so the table has 64 buckets. The table has 64 buckets, so the key 224 goes to bucket 224 mod 64 = 32. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 38. seed 1617464753679261298, level 2

A table follows the `HashMap` rule: 32 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. The bucket is `key mod buckets`. After 18 distinct keys, in which bucket does key `176` sit?

a) bucket number 16
b) bucket 48
c) 14
d) bucket 0

**Key: b**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 32 buckets that limit is 32 x 0.5 = 16. 1. entry 17 exceeds 16, so the table has 64 buckets. The table has 64 buckets, so the key 176 goes to bucket 176 mod 64 = 48. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 39. seed 4524685521169896266, level 2

A table follows the `HashMap` rule: 32 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. The bucket is `key mod buckets`. After 34 distinct keys, in which bucket does key `153` sit?

a) bucket number 17
b) 153
c) 57
d) bucket 25

**Key: d**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 32 buckets that limit is 32 x 0.5 = 16. 1. entry 17 exceeds 16, so the table has 64 buckets; 2. entry 33 exceeds 32, so the table has 128 buckets. The table has 128 buckets, so the key 153 goes to bucket 153 mod 128 = 25. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 40. seed 2409887611287665162, level 2

A table follows the `HashMap` rule: 16 buckets, load factor `0.75`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) 13
b) insert number 24
c) insert number 33
d) 25

**Key: d**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.75 = 12. The first doubling gives 32 buckets, so the limit becomes 32 x 0.75 = 24. Entry 24 still fits, so entry 25 doubles the table again. Answer: 25. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 41. seed 1466781680322744893, level 2

A table follows the `HashMap` rule: 32 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) insert 65
b) insert number 33
c) insert 17
d) insert 32

**Key: b**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 32 buckets that limit is 32 x 0.5 = 16. The first doubling gives 64 buckets, so the limit becomes 64 x 0.5 = 32. Entry 32 still fits, so entry 33 doubles the table again. Answer: 33. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 42. seed 4007714557736767634, level 2

A table follows the `HashMap` rule: 16 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) insert 17
b) 16
c) insert number 9
d) insert number 33

**Key: a**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.5 = 8. The first doubling gives 32 buckets, so the limit becomes 32 x 0.5 = 16. Entry 16 still fits, so entry 17 doubles the table again. Answer: 17. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 43. seed 2785145690346627602, level 2

A table follows the `HashMap` rule: 8 buckets, load factor `0.75`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) insert number 16
b) insert number 7
c) insert number 13
d) 17

**Key: c**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 8 buckets that limit is 8 x 0.75 = 6. The first doubling gives 16 buckets, so the limit becomes 16 x 0.75 = 12. Entry 12 still fits, so entry 13 doubles the table again. Answer: 13. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 44. seed 1243868386205774055, level 2

A table follows the `HashMap` rule: 32 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) insert number 32
b) insert number 17
c) 33
d) insert 64

**Key: c**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 32 buckets that limit is 32 x 0.5 = 16. The first doubling gives 64 buckets, so the limit becomes 64 x 0.5 = 32. Entry 32 still fits, so entry 33 doubles the table again. Answer: 33. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 45. seed 3757592638140321052, level 1

A table follows the `HashMap` rule: 32 buckets, load factor `0.75`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the first time?

a) insert number 24
b) insert number 33
c) insert 17
d) 25

**Key: d**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 32 buckets that limit is 32 x 0.75 = 24. Entry 24 still fits, so entry 25 is the first to exceed it. Answer: 25. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 46. seed 3951430258275385515, level 2

A table follows the `HashMap` rule: 16 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. The bucket is `key mod buckets`. After 11 distinct keys, in which bucket does key `54` sit?

a) bucket 22
b) 54
c) bucket 10
d) 6

**Key: a**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.5 = 8. 1. entry 9 exceeds 8, so the table has 32 buckets. The table has 32 buckets, so the key 54 goes to bucket 54 mod 32 = 22. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 47. seed 1812216067238107613, level 1

A table follows the `HashMap` rule: 32 buckets, load factor `0.75`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the first time?

a) 49
b) 25
c) insert 32
d) insert number 33

**Key: b**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 32 buckets that limit is 32 x 0.75 = 24. Entry 24 still fits, so entry 25 is the first to exceed it. Answer: 25. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 48. seed 3318272704636589367, level 1

A table follows the `HashMap` rule: 16 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the first time?

a) 9
b) insert 16
c) insert number 17
d) insert number 8

**Key: a**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.5 = 8. Entry 8 still fits, so entry 9 is the first to exceed it. Answer: 9. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 49. seed 2101810082905309729, level 2

A table follows the `HashMap` rule: 32 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. Which numbered insert, counting from 1, doubles it for the second time?

a) 64
b) insert 17
c) insert number 33
d) insert 32

**Key: c**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 32 buckets that limit is 32 x 0.5 = 16. The first doubling gives 64 buckets, so the limit becomes 64 x 0.5 = 32. Entry 32 still fits, so entry 33 doubles the table again. Answer: 33. Source: `javadoc-hashmap#class-hashmap-k-v`.

## 50. seed 4239843231063320430, level 1

A table follows the `HashMap` rule: 16 buckets, load factor `0.5`, buckets double once entries exceed load factor times buckets. After 18 distinct keys are inserted, how many buckets does it have?

a) 64
b) 16
c) 48 buckets in total
d) 128 buckets

**Key: a**

Explanation: The table doubles when its entries exceed `load factor x buckets`. With 16 buckets that limit is 16 x 0.5 = 8. 1. entry 9 exceeds 8, so the table has 32 buckets; 2. entry 17 exceeds 16, so the table has 64 buckets. After 18 entries the table has 64 buckets. Source: `javadoc-hashmap#class-hashmap-k-v`.
