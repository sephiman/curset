# Binary heap contents (`binary-heap-contents`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 421694015513883938, level 1

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(22)`, `add(19)`, `add(59)`, `add(15)`, `add(43)`, `add(44)`, `add(54)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the whole array `[19, 15, 59, 54, 43, 44]`
b) `[19, 22, 44, 54, 43, 59]`
c) the array `[54, 19, 44, 22, 43, 59]`
d) `[19, 22, 43, 44, 54, 59]`

**Key: b**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(22)` gives `[22]`; `add(19)` gives `[19, 22]`; `add(59)` gives `[19, 22, 59]`; `add(15)` gives `[15, 19, 59, 22]`; `add(43)` gives `[15, 19, 59, 22, 43]`; `add(44)` gives `[15, 19, 44, 22, 43, 59]`; `add(54)` gives `[15, 19, 44, 22, 43, 59, 54]`; `removeRoot()` gives `[19, 22, 44, 54, 43, 59]`.

## 2. seed 3863595851256644977, level 1

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(36)`, `add(41)`, `add(17)`, `add(29)`, `add(6)`, `add(46)`, `add(54)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the array `[17, 41, 46, 29, 6, 54]`
b) the array `[17, 29, 36, 41, 46, 54]`
c) the array `[46, 36, 41, 29, 6, 17]`
d) `[17, 29, 36, 41, 54, 46]`

**Key: d**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(36)` gives `[36]`; `add(41)` gives `[36, 41]`; `add(17)` gives `[17, 41, 36]`; `add(29)` gives `[17, 29, 36, 41]`; `add(6)` gives `[6, 17, 36, 41, 29]`; `add(46)` gives `[6, 17, 36, 41, 29, 46]`; `add(54)` gives `[6, 17, 36, 41, 29, 46, 54]`; `removeRoot()` gives `[17, 29, 36, 41, 54, 46]`.

## 3. seed 2496545396774914841, level 2

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(33)`, `add(6)`, `add(38)`, `add(46)`, `add(58)`, `add(29)`, `removeRoot()`, `add(25)`, `removeRoot()`, `add(26)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the array `[26, 29, 38, 46, 58]`
b) `[29, 33, 38, 46, 58]`
c) the whole array `[38, 33, 29, 46, 58]`
d) `[33, 29, 26, 6, 25]`

**Key: b**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(33)` gives `[33]`; `add(6)` gives `[6, 33]`; `add(38)` gives `[6, 33, 38]`; `add(46)` gives `[6, 33, 38, 46]`; `add(58)` gives `[6, 33, 38, 46, 58]`; `add(29)` gives `[6, 33, 29, 46, 58, 38]`; `removeRoot()` gives `[29, 33, 38, 46, 58]`; `add(25)` gives `[25, 33, 29, 46, 58, 38]`; `removeRoot()` gives `[29, 33, 38, 46, 58]`; `add(26)` gives `[26, 33, 29, 46, 58, 38]`; `removeRoot()` gives `[29, 33, 38, 46, 58]`.

## 4. seed 3762060783275444972, level 1

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(18)`, `add(20)`, `add(53)`, `add(35)`, `add(19)`, `add(24)`, `add(6)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the whole array `[35, 19, 24, 18, 6, 20]`
b) `[6, 20, 53, 35, 19, 24]`
c) the whole array `[18, 19, 24, 35, 20, 53]`
d) the whole array `[18, 19, 20, 24, 35, 53]`

**Key: c**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(18)` gives `[18]`; `add(20)` gives `[18, 20]`; `add(53)` gives `[18, 20, 53]`; `add(35)` gives `[18, 20, 53, 35]`; `add(19)` gives `[18, 19, 53, 35, 20]`; `add(24)` gives `[18, 19, 24, 35, 20, 53]`; `add(6)` gives `[6, 19, 18, 35, 20, 53, 24]`; `removeRoot()` gives `[18, 19, 24, 35, 20, 53]`.

## 5. seed 1138181408728651634, level 1

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(25)`, `add(31)`, `add(6)`, `add(37)`, `add(10)`, `add(39)`, `add(5)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the array `[5, 31, 37, 25, 10, 6]`
b) the array `[37, 31, 6, 25, 10, 5]`
c) the array `[37, 31, 25, 10, 6, 5]`
d) the array `[31, 37, 6, 5, 10, 39]`

**Key: b**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(25)` gives `[25]`; `add(31)` gives `[31, 25]`; `add(6)` gives `[31, 25, 6]`; `add(37)` gives `[37, 31, 6, 25]`; `add(10)` gives `[37, 31, 6, 25, 10]`; `add(39)` gives `[39, 31, 37, 25, 10, 6]`; `add(5)` gives `[39, 31, 37, 25, 10, 6, 5]`; `removeRoot()` gives `[37, 31, 6, 25, 10, 5]`.

## 6. seed 4206831602262586192, level 2

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(33)`, `add(30)`, `add(31)`, `add(15)`, `add(39)`, `add(14)`, `removeRoot()`, `add(22)`, `removeRoot()`, `add(38)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the whole array `[30, 33, 31, 38, 39]`
b) the array `[38, 30, 15, 33, 39]`
c) the whole array `[31, 30, 22, 15, 14]`
d) the whole array `[30, 31, 33, 38, 39]`

**Key: a**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(33)` gives `[33]`; `add(30)` gives `[30, 33]`; `add(31)` gives `[30, 33, 31]`; `add(15)` gives `[15, 30, 31, 33]`; `add(39)` gives `[15, 30, 31, 33, 39]`; `add(14)` gives `[14, 30, 15, 33, 39, 31]`; `removeRoot()` gives `[15, 30, 31, 33, 39]`; `add(22)` gives `[15, 30, 22, 33, 39, 31]`; `removeRoot()` gives `[22, 30, 31, 33, 39]`; `add(38)` gives `[22, 30, 31, 33, 39, 38]`; `removeRoot()` gives `[30, 33, 31, 38, 39]`.

## 7. seed 2554422707334427489, level 2

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(28)`, `add(59)`, `add(41)`, `add(26)`, `add(14)`, `add(46)`, `removeRoot()`, `add(50)`, `removeRoot()`, `add(21)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the array `[41, 28, 21, 26, 14]`
b) the array `[46, 26, 41, 21, 14]`
c) the array `[21, 28, 41, 26, 14]`
d) the array `[41, 28, 26, 21, 14]`

**Key: a**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(28)` gives `[28]`; `add(59)` gives `[59, 28]`; `add(41)` gives `[59, 28, 41]`; `add(26)` gives `[59, 28, 41, 26]`; `add(14)` gives `[59, 28, 41, 26, 14]`; `add(46)` gives `[59, 28, 46, 26, 14, 41]`; `removeRoot()` gives `[46, 28, 41, 26, 14]`; `add(50)` gives `[50, 28, 46, 26, 14, 41]`; `removeRoot()` gives `[46, 28, 41, 26, 14]`; `add(21)` gives `[46, 28, 41, 26, 14, 21]`; `removeRoot()` gives `[41, 28, 21, 26, 14]`.

## 8. seed 53662379115302219, level 2

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(11)`, `add(50)`, `add(45)`, `add(58)`, `add(13)`, `add(20)`, `removeRoot()`, `add(21)`, `removeRoot()`, `add(8)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[21, 20, 8, 11, 13]`
b) `[20, 45, 21, 58, 50]`
c) the whole array `[8, 50, 45, 58, 13]`
d) the whole array `[20, 21, 45, 50, 58]`

**Key: b**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(11)` gives `[11]`; `add(50)` gives `[11, 50]`; `add(45)` gives `[11, 50, 45]`; `add(58)` gives `[11, 50, 45, 58]`; `add(13)` gives `[11, 13, 45, 58, 50]`; `add(20)` gives `[11, 13, 20, 58, 50, 45]`; `removeRoot()` gives `[13, 45, 20, 58, 50]`; `add(21)` gives `[13, 45, 20, 58, 50, 21]`; `removeRoot()` gives `[20, 45, 21, 58, 50]`; `add(8)` gives `[8, 45, 20, 58, 50, 21]`; `removeRoot()` gives `[20, 45, 21, 58, 50]`.

## 9. seed 1796934651471248977, level 2

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(21)`, `add(50)`, `add(3)`, `add(45)`, `add(58)`, `add(30)`, `removeRoot()`, `add(57)`, `removeRoot()`, `add(19)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the array `[45, 30, 21, 19, 3]`
b) the array `[57, 45, 3, 19, 30]`
c) `[3, 50, 19, 21, 45]`
d) `[45, 21, 30, 19, 3]`

**Key: d**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(21)` gives `[21]`; `add(50)` gives `[50, 21]`; `add(3)` gives `[50, 21, 3]`; `add(45)` gives `[50, 45, 3, 21]`; `add(58)` gives `[58, 50, 3, 21, 45]`; `add(30)` gives `[58, 50, 30, 21, 45, 3]`; `removeRoot()` gives `[50, 45, 30, 21, 3]`; `add(57)` gives `[57, 45, 50, 21, 3, 30]`; `removeRoot()` gives `[50, 45, 30, 21, 3]`; `add(19)` gives `[50, 45, 30, 21, 3, 19]`; `removeRoot()` gives `[45, 21, 30, 19, 3]`.

## 10. seed 360954171343335604, level 2

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(37)`, `add(6)`, `add(36)`, `add(42)`, `add(56)`, `add(34)`, `removeRoot()`, `add(50)`, `removeRoot()`, `add(55)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the array `[42, 37, 36, 34, 6]`
b) the array `[55, 6, 34, 42, 56]`
c) the array `[42, 37, 36, 6, 34]`
d) the array `[34, 42, 36, 6, 37]`

**Key: c**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(37)` gives `[37]`; `add(6)` gives `[37, 6]`; `add(36)` gives `[37, 6, 36]`; `add(42)` gives `[42, 37, 36, 6]`; `add(56)` gives `[56, 42, 36, 6, 37]`; `add(34)` gives `[56, 42, 36, 6, 37, 34]`; `removeRoot()` gives `[42, 37, 36, 6, 34]`; `add(50)` gives `[50, 37, 42, 6, 34, 36]`; `removeRoot()` gives `[42, 37, 36, 6, 34]`; `add(55)` gives `[55, 37, 42, 6, 34, 36]`; `removeRoot()` gives `[42, 37, 36, 6, 34]`.

## 11. seed 886424338669682945, level 2

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(51)`, `add(29)`, `add(34)`, `add(23)`, `add(12)`, `add(42)`, `removeRoot()`, `add(41)`, `removeRoot()`, `add(8)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the array `[8, 29, 42, 23, 12]`
b) the whole array `[29, 41, 34, 51, 42]`
c) the array `[34, 29, 23, 12, 8]`
d) the whole array `[34, 29, 8, 23, 12]`

**Key: d**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(51)` gives `[51]`; `add(29)` gives `[51, 29]`; `add(34)` gives `[51, 29, 34]`; `add(23)` gives `[51, 29, 34, 23]`; `add(12)` gives `[51, 29, 34, 23, 12]`; `add(42)` gives `[51, 29, 42, 23, 12, 34]`; `removeRoot()` gives `[42, 29, 34, 23, 12]`; `add(41)` gives `[42, 29, 41, 23, 12, 34]`; `removeRoot()` gives `[41, 29, 34, 23, 12]`; `add(8)` gives `[41, 29, 34, 23, 12, 8]`; `removeRoot()` gives `[34, 29, 8, 23, 12]`.

## 12. seed 3755278037685203534, level 2

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(13)`, `add(53)`, `add(35)`, `add(58)`, `add(38)`, `add(33)`, `removeRoot()`, `add(7)`, `removeRoot()`, `add(46)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[35, 53, 46, 58, 38]`
b) `[46, 38, 35, 58, 53]`
c) `[35, 38, 46, 58, 53]`
d) the array `[35, 38, 46, 53, 58]`

**Key: c**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(13)` gives `[13]`; `add(53)` gives `[13, 53]`; `add(35)` gives `[13, 53, 35]`; `add(58)` gives `[13, 53, 35, 58]`; `add(38)` gives `[13, 38, 35, 58, 53]`; `add(33)` gives `[13, 38, 33, 58, 53, 35]`; `removeRoot()` gives `[33, 38, 35, 58, 53]`; `add(7)` gives `[7, 38, 33, 58, 53, 35]`; `removeRoot()` gives `[33, 38, 35, 58, 53]`; `add(46)` gives `[33, 38, 35, 58, 53, 46]`; `removeRoot()` gives `[35, 38, 46, 58, 53]`.

## 13. seed 1362108168507749669, level 2

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(9)`, `add(38)`, `add(29)`, `add(36)`, `add(41)`, `add(2)`, `removeRoot()`, `add(55)`, `removeRoot()`, `add(28)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the array `[41, 36, 29, 28, 2]`
b) the whole array `[36, 28, 29, 9, 2]`
c) `[36, 29, 28, 9, 2]`
d) the array `[2, 38, 28, 9, 36]`

**Key: b**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(9)` gives `[9]`; `add(38)` gives `[38, 9]`; `add(29)` gives `[38, 9, 29]`; `add(36)` gives `[38, 36, 29, 9]`; `add(41)` gives `[41, 38, 29, 9, 36]`; `add(2)` gives `[41, 38, 29, 9, 36, 2]`; `removeRoot()` gives `[38, 36, 29, 9, 2]`; `add(55)` gives `[55, 36, 38, 9, 2, 29]`; `removeRoot()` gives `[38, 36, 29, 9, 2]`; `add(28)` gives `[38, 36, 29, 9, 2, 28]`; `removeRoot()` gives `[36, 28, 29, 9, 2]`.

## 14. seed 2987664566493944716, level 1

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(37)`, `add(15)`, `add(38)`, `add(2)`, `add(3)`, `add(26)`, `add(36)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the whole array `[37, 36, 26, 15, 3, 2]`
b) `[38, 15, 36, 2, 3, 26]`
c) `[36, 15, 37, 2, 3, 26]`
d) the array `[37, 15, 36, 2, 3, 26]`

**Key: d**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(37)` gives `[37]`; `add(15)` gives `[37, 15]`; `add(38)` gives `[38, 15, 37]`; `add(2)` gives `[38, 15, 37, 2]`; `add(3)` gives `[38, 15, 37, 2, 3]`; `add(26)` gives `[38, 15, 37, 2, 3, 26]`; `add(36)` gives `[38, 15, 37, 2, 3, 26, 36]`; `removeRoot()` gives `[37, 15, 36, 2, 3, 26]`.

## 15. seed 4017416454919915162, level 1

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(17)`, `add(1)`, `add(45)`, `add(11)`, `add(59)`, `add(35)`, `add(16)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[16, 45, 35, 1, 11, 17]`
b) `[45, 16, 35, 1, 11, 17]`
c) the whole array `[45, 1, 35, 11, 59, 16]`
d) the whole array `[45, 35, 17, 16, 11, 1]`

**Key: b**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(17)` gives `[17]`; `add(1)` gives `[17, 1]`; `add(45)` gives `[45, 1, 17]`; `add(11)` gives `[45, 11, 17, 1]`; `add(59)` gives `[59, 45, 17, 1, 11]`; `add(35)` gives `[59, 45, 35, 1, 11, 17]`; `add(16)` gives `[59, 45, 35, 1, 11, 17, 16]`; `removeRoot()` gives `[45, 16, 35, 1, 11, 17]`.

## 16. seed 2765595265003310325, level 2

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(56)`, `add(55)`, `add(15)`, `add(58)`, `add(14)`, `add(45)`, `removeRoot()`, `add(5)`, `removeRoot()`, `add(28)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[28, 55, 45, 58, 56]`
b) `[55, 15, 45, 58, 56]`
c) `[28, 45, 55, 56, 58]`
d) the whole array `[28, 55, 45, 58, 14]`

**Key: a**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(56)` gives `[56]`; `add(55)` gives `[55, 56]`; `add(15)` gives `[15, 56, 55]`; `add(58)` gives `[15, 56, 55, 58]`; `add(14)` gives `[14, 15, 55, 58, 56]`; `add(45)` gives `[14, 15, 45, 58, 56, 55]`; `removeRoot()` gives `[15, 55, 45, 58, 56]`; `add(5)` gives `[5, 55, 15, 58, 56, 45]`; `removeRoot()` gives `[15, 55, 45, 58, 56]`; `add(28)` gives `[15, 55, 28, 58, 56, 45]`; `removeRoot()` gives `[28, 55, 45, 58, 56]`.

## 17. seed 1796782145356838709, level 1

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(4)`, `add(53)`, `add(23)`, `add(7)`, `add(55)`, `add(40)`, `add(19)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the whole array `[19, 53, 23, 7, 55, 40]`
b) the array `[7, 19, 23, 40, 53, 55]`
c) the array `[23, 7, 19, 53, 55, 40]`
d) the whole array `[7, 23, 19, 53, 55, 40]`

**Key: d**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(4)` gives `[4]`; `add(53)` gives `[4, 53]`; `add(23)` gives `[4, 53, 23]`; `add(7)` gives `[4, 7, 23, 53]`; `add(55)` gives `[4, 7, 23, 53, 55]`; `add(40)` gives `[4, 7, 23, 53, 55, 40]`; `add(19)` gives `[4, 7, 19, 53, 55, 40, 23]`; `removeRoot()` gives `[7, 23, 19, 53, 55, 40]`.

## 18. seed 325936454258167939, level 2

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(43)`, `add(7)`, `add(25)`, `add(49)`, `add(9)`, `add(17)`, `removeRoot()`, `add(11)`, `removeRoot()`, `add(16)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[16, 7, 11, 49, 9]`
b) `[17, 11, 16, 7, 9]`
c) `[16, 43, 25, 7, 9]`
d) `[17, 16, 11, 9, 7]`

**Key: b**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(43)` gives `[43]`; `add(7)` gives `[43, 7]`; `add(25)` gives `[43, 7, 25]`; `add(49)` gives `[49, 43, 25, 7]`; `add(9)` gives `[49, 43, 25, 7, 9]`; `add(17)` gives `[49, 43, 25, 7, 9, 17]`; `removeRoot()` gives `[43, 17, 25, 7, 9]`; `add(11)` gives `[43, 17, 25, 7, 9, 11]`; `removeRoot()` gives `[25, 17, 11, 7, 9]`; `add(16)` gives `[25, 17, 16, 7, 9, 11]`; `removeRoot()` gives `[17, 11, 16, 7, 9]`.

## 19. seed 1764153237771134938, level 1

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(36)`, `add(44)`, `add(32)`, `add(12)`, `add(24)`, `add(56)`, `add(59)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the whole array `[24, 32, 36, 44, 59, 56]`
b) the array `[24, 32, 36, 44, 56, 59]`
c) the array `[32, 44, 56, 12, 24, 59]`
d) the whole array `[56, 36, 44, 12, 24, 32]`

**Key: a**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(36)` gives `[36]`; `add(44)` gives `[36, 44]`; `add(32)` gives `[32, 44, 36]`; `add(12)` gives `[12, 32, 36, 44]`; `add(24)` gives `[12, 24, 36, 44, 32]`; `add(56)` gives `[12, 24, 36, 44, 32, 56]`; `add(59)` gives `[12, 24, 36, 44, 32, 56, 59]`; `removeRoot()` gives `[24, 32, 36, 44, 59, 56]`.

## 20. seed 2315345805931417220, level 2

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(36)`, `add(8)`, `add(55)`, `add(38)`, `add(44)`, `add(13)`, `removeRoot()`, `add(6)`, `removeRoot()`, `add(7)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the whole array `[36, 13, 7, 8, 6]`
b) `[13, 36, 55, 38, 44]`
c) the array `[8, 44, 6, 38, 7]`
d) the whole array `[36, 13, 8, 7, 6]`

**Key: a**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(36)` gives `[36]`; `add(8)` gives `[36, 8]`; `add(55)` gives `[55, 8, 36]`; `add(38)` gives `[55, 38, 36, 8]`; `add(44)` gives `[55, 44, 36, 8, 38]`; `add(13)` gives `[55, 44, 36, 8, 38, 13]`; `removeRoot()` gives `[44, 38, 36, 8, 13]`; `add(6)` gives `[44, 38, 36, 8, 13, 6]`; `removeRoot()` gives `[38, 13, 36, 8, 6]`; `add(7)` gives `[38, 13, 36, 8, 6, 7]`; `removeRoot()` gives `[36, 13, 7, 8, 6]`.

## 21. seed 1317715411142411567, level 1

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(30)`, `add(21)`, `add(23)`, `add(28)`, `add(37)`, `add(12)`, `add(42)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the array `[37, 30, 23, 21, 28, 12]`
b) `[42, 28, 21, 30, 37, 23]`
c) the array `[21, 28, 23, 30, 37, 42]`
d) `[21, 23, 28, 30, 37, 42]`

**Key: c**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(30)` gives `[30]`; `add(21)` gives `[21, 30]`; `add(23)` gives `[21, 30, 23]`; `add(28)` gives `[21, 28, 23, 30]`; `add(37)` gives `[21, 28, 23, 30, 37]`; `add(12)` gives `[12, 28, 21, 30, 37, 23]`; `add(42)` gives `[12, 28, 21, 30, 37, 23, 42]`; `removeRoot()` gives `[21, 28, 23, 30, 37, 42]`.

## 22. seed 3654118439491539878, level 1

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(26)`, `add(16)`, `add(48)`, `add(23)`, `add(35)`, `add(1)`, `add(52)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[16, 23, 48, 52, 35, 1]`
b) the whole array `[16, 23, 26, 35, 48, 52]`
c) the whole array `[52, 23, 16, 26, 35, 48]`
d) the whole array `[16, 23, 48, 26, 35, 52]`

**Key: d**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(26)` gives `[26]`; `add(16)` gives `[16, 26]`; `add(48)` gives `[16, 26, 48]`; `add(23)` gives `[16, 23, 48, 26]`; `add(35)` gives `[16, 23, 48, 26, 35]`; `add(1)` gives `[1, 23, 16, 26, 35, 48]`; `add(52)` gives `[1, 23, 16, 26, 35, 48, 52]`; `removeRoot()` gives `[16, 23, 48, 26, 35, 52]`.

## 23. seed 435672471208580033, level 2

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(26)`, `add(1)`, `add(7)`, `add(51)`, `add(10)`, `add(14)`, `removeRoot()`, `add(55)`, `removeRoot()`, `add(18)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the array `[7, 26, 14, 1, 10]`
b) the whole array `[18, 1, 7, 51, 10]`
c) the array `[18, 10, 14, 1, 7]`
d) the whole array `[18, 14, 10, 7, 1]`

**Key: c**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(26)` gives `[26]`; `add(1)` gives `[26, 1]`; `add(7)` gives `[26, 1, 7]`; `add(51)` gives `[51, 26, 7, 1]`; `add(10)` gives `[51, 26, 7, 1, 10]`; `add(14)` gives `[51, 26, 14, 1, 10, 7]`; `removeRoot()` gives `[26, 10, 14, 1, 7]`; `add(55)` gives `[55, 10, 26, 1, 7, 14]`; `removeRoot()` gives `[26, 10, 14, 1, 7]`; `add(18)` gives `[26, 10, 18, 1, 7, 14]`; `removeRoot()` gives `[18, 10, 14, 1, 7]`.

## 24. seed 1987709213252497401, level 1

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(41)`, `add(17)`, `add(55)`, `add(21)`, `add(46)`, `add(37)`, `add(33)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[46, 33, 41, 17, 21, 37]`
b) `[46, 41, 37, 33, 21, 17]`
c) `[55, 17, 37, 21, 46, 33]`
d) the array `[21, 37, 33, 41, 46, 55]`

**Key: a**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(41)` gives `[41]`; `add(17)` gives `[41, 17]`; `add(55)` gives `[55, 17, 41]`; `add(21)` gives `[55, 21, 41, 17]`; `add(46)` gives `[55, 46, 41, 17, 21]`; `add(37)` gives `[55, 46, 41, 17, 21, 37]`; `add(33)` gives `[55, 46, 41, 17, 21, 37, 33]`; `removeRoot()` gives `[46, 33, 41, 17, 21, 37]`.

## 25. seed 2679270364789228258, level 1

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(34)`, `add(10)`, `add(38)`, `add(2)`, `add(15)`, `add(29)`, `add(13)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[10, 2, 38, 13, 15, 29]`
b) `[10, 13, 15, 29, 34, 38]`
c) `[10, 15, 13, 34, 29, 38]`
d) the whole array `[29, 10, 13, 34, 15, 38]`

**Key: c**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(34)` gives `[34]`; `add(10)` gives `[10, 34]`; `add(38)` gives `[10, 34, 38]`; `add(2)` gives `[2, 10, 38, 34]`; `add(15)` gives `[2, 10, 38, 34, 15]`; `add(29)` gives `[2, 10, 29, 34, 15, 38]`; `add(13)` gives `[2, 10, 13, 34, 15, 38, 29]`; `removeRoot()` gives `[10, 15, 13, 34, 29, 38]`.

## 26. seed 2883292276591084804, level 2

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(38)`, `add(5)`, `add(35)`, `add(14)`, `add(7)`, `add(36)`, `removeRoot()`, `add(15)`, `removeRoot()`, `add(1)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[1, 14, 36, 5, 7]`
b) the array `[15, 14, 7, 5, 1]`
c) the array `[15, 5, 1, 14, 7]`
d) `[15, 14, 1, 5, 7]`

**Key: d**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(38)` gives `[38]`; `add(5)` gives `[38, 5]`; `add(35)` gives `[38, 5, 35]`; `add(14)` gives `[38, 14, 35, 5]`; `add(7)` gives `[38, 14, 35, 5, 7]`; `add(36)` gives `[38, 14, 36, 5, 7, 35]`; `removeRoot()` gives `[36, 14, 35, 5, 7]`; `add(15)` gives `[36, 14, 35, 5, 7, 15]`; `removeRoot()` gives `[35, 14, 15, 5, 7]`; `add(1)` gives `[35, 14, 15, 5, 7, 1]`; `removeRoot()` gives `[15, 14, 1, 5, 7]`.

## 27. seed 3825791419184273803, level 1

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(13)`, `add(48)`, `add(16)`, `add(37)`, `add(24)`, `add(26)`, `add(25)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[16, 24, 25, 26, 37, 48]`
b) the whole array `[37, 25, 26, 13, 24, 16]`
c) `[16, 24, 25, 48, 37, 26]`
d) the whole array `[25, 24, 16, 48, 37, 26]`

**Key: c**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(13)` gives `[13]`; `add(48)` gives `[13, 48]`; `add(16)` gives `[13, 48, 16]`; `add(37)` gives `[13, 37, 16, 48]`; `add(24)` gives `[13, 24, 16, 48, 37]`; `add(26)` gives `[13, 24, 16, 48, 37, 26]`; `add(25)` gives `[13, 24, 16, 48, 37, 26, 25]`; `removeRoot()` gives `[16, 24, 25, 48, 37, 26]`.

## 28. seed 811789439471880921, level 2

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(16)`, `add(55)`, `add(52)`, `add(42)`, `add(14)`, `add(58)`, `removeRoot()`, `add(41)`, `removeRoot()`, `add(49)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[49, 55, 58, 42, 14]`
b) the array `[42, 49, 52, 55, 58]`
c) `[49, 42, 41, 16, 14]`
d) `[42, 52, 49, 55, 58]`

**Key: d**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(16)` gives `[16]`; `add(55)` gives `[16, 55]`; `add(52)` gives `[16, 55, 52]`; `add(42)` gives `[16, 42, 52, 55]`; `add(14)` gives `[14, 16, 52, 55, 42]`; `add(58)` gives `[14, 16, 52, 55, 42, 58]`; `removeRoot()` gives `[16, 42, 52, 55, 58]`; `add(41)` gives `[16, 42, 41, 55, 58, 52]`; `removeRoot()` gives `[41, 42, 52, 55, 58]`; `add(49)` gives `[41, 42, 49, 55, 58, 52]`; `removeRoot()` gives `[42, 52, 49, 55, 58]`.

## 29. seed 3494641334820077467, level 1

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(19)`, `add(42)`, `add(57)`, `add(30)`, `add(48)`, `add(16)`, `add(3)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[48, 30, 42, 19, 3, 16]`
b) `[3, 48, 42, 19, 30, 16]`
c) the whole array `[57, 42, 16, 30, 48, 3]`
d) `[48, 42, 30, 19, 16, 3]`

**Key: a**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(19)` gives `[19]`; `add(42)` gives `[42, 19]`; `add(57)` gives `[57, 19, 42]`; `add(30)` gives `[57, 30, 42, 19]`; `add(48)` gives `[57, 48, 42, 19, 30]`; `add(16)` gives `[57, 48, 42, 19, 30, 16]`; `add(3)` gives `[57, 48, 42, 19, 30, 16, 3]`; `removeRoot()` gives `[48, 30, 42, 19, 3, 16]`.

## 30. seed 407686443783360107, level 2

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(23)`, `add(9)`, `add(11)`, `add(49)`, `add(24)`, `add(25)`, `removeRoot()`, `add(59)`, `removeRoot()`, `add(13)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[13, 24, 59, 49, 25]`
b) the whole array `[13, 23, 11, 49, 24]`
c) the array `[24, 23, 13, 9, 11]`
d) the array `[23, 24, 25, 49, 59]`

**Key: d**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(23)` gives `[23]`; `add(9)` gives `[9, 23]`; `add(11)` gives `[9, 23, 11]`; `add(49)` gives `[9, 23, 11, 49]`; `add(24)` gives `[9, 23, 11, 49, 24]`; `add(25)` gives `[9, 23, 11, 49, 24, 25]`; `removeRoot()` gives `[11, 23, 25, 49, 24]`; `add(59)` gives `[11, 23, 25, 49, 24, 59]`; `removeRoot()` gives `[23, 24, 25, 49, 59]`; `add(13)` gives `[13, 24, 23, 49, 59, 25]`; `removeRoot()` gives `[23, 24, 25, 49, 59]`.

## 31. seed 4456812637080699199, level 2

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(6)`, `add(5)`, `add(20)`, `add(32)`, `add(7)`, `add(39)`, `removeRoot()`, `add(52)`, `removeRoot()`, `add(51)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the array `[32, 20, 6, 5, 7]`
b) the whole array `[32, 20, 7, 6, 5]`
c) the whole array `[6, 20, 32, 5, 7]`
d) `[51, 5, 20, 32, 7]`

**Key: a**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(6)` gives `[6]`; `add(5)` gives `[6, 5]`; `add(20)` gives `[20, 5, 6]`; `add(32)` gives `[32, 20, 6, 5]`; `add(7)` gives `[32, 20, 6, 5, 7]`; `add(39)` gives `[39, 20, 32, 5, 7, 6]`; `removeRoot()` gives `[32, 20, 6, 5, 7]`; `add(52)` gives `[52, 20, 32, 5, 7, 6]`; `removeRoot()` gives `[32, 20, 6, 5, 7]`; `add(51)` gives `[51, 20, 32, 5, 7, 6]`; `removeRoot()` gives `[32, 20, 6, 5, 7]`.

## 32. seed 2709474420717102829, level 1

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(56)`, `add(32)`, `add(4)`, `add(1)`, `add(57)`, `add(46)`, `add(6)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the whole array `[4, 32, 6, 56, 57, 46]`
b) `[4, 32, 6, 1, 57, 46]`
c) the whole array `[4, 6, 32, 46, 56, 57]`
d) the whole array `[32, 4, 6, 56, 57, 46]`

**Key: a**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(56)` gives `[56]`; `add(32)` gives `[32, 56]`; `add(4)` gives `[4, 56, 32]`; `add(1)` gives `[1, 4, 32, 56]`; `add(57)` gives `[1, 4, 32, 56, 57]`; `add(46)` gives `[1, 4, 32, 56, 57, 46]`; `add(6)` gives `[1, 4, 6, 56, 57, 46, 32]`; `removeRoot()` gives `[4, 32, 6, 56, 57, 46]`.

## 33. seed 3313537270812404352, level 1

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(5)`, `add(14)`, `add(57)`, `add(38)`, `add(43)`, `add(55)`, `add(25)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[25, 43, 55, 5, 38, 14]`
b) the array `[55, 43, 38, 25, 14, 5]`
c) `[14, 38, 25, 55, 43, 57]`
d) the whole array `[55, 43, 25, 5, 38, 14]`

**Key: d**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(5)` gives `[5]`; `add(14)` gives `[14, 5]`; `add(57)` gives `[57, 5, 14]`; `add(38)` gives `[57, 38, 14, 5]`; `add(43)` gives `[57, 43, 14, 5, 38]`; `add(55)` gives `[57, 43, 55, 5, 38, 14]`; `add(25)` gives `[57, 43, 55, 5, 38, 14, 25]`; `removeRoot()` gives `[55, 43, 25, 5, 38, 14]`.

## 34. seed 2219018185585206115, level 1

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(47)`, `add(52)`, `add(36)`, `add(51)`, `add(30)`, `add(21)`, `add(33)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the array `[52, 51, 36, 33, 30, 21]`
b) `[51, 47, 36, 33, 30, 21]`
c) the array `[30, 36, 33, 52, 51, 47]`
d) `[33, 51, 36, 47, 30, 21]`

**Key: b**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(47)` gives `[47]`; `add(52)` gives `[52, 47]`; `add(36)` gives `[52, 47, 36]`; `add(51)` gives `[52, 51, 36, 47]`; `add(30)` gives `[52, 51, 36, 47, 30]`; `add(21)` gives `[52, 51, 36, 47, 30, 21]`; `add(33)` gives `[52, 51, 36, 47, 30, 21, 33]`; `removeRoot()` gives `[51, 47, 36, 33, 30, 21]`.

## 35. seed 1248438669708943723, level 1

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(7)`, `add(14)`, `add(4)`, `add(6)`, `add(35)`, `add(16)`, `add(38)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[16, 14, 35, 6, 7, 4]`
b) the array `[6, 14, 7, 38, 35, 16]`
c) the array `[35, 14, 16, 6, 7, 4]`
d) the whole array `[38, 14, 4, 6, 35, 16]`

**Key: c**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(7)` gives `[7]`; `add(14)` gives `[14, 7]`; `add(4)` gives `[14, 7, 4]`; `add(6)` gives `[14, 7, 4, 6]`; `add(35)` gives `[35, 14, 4, 6, 7]`; `add(16)` gives `[35, 14, 16, 6, 7, 4]`; `add(38)` gives `[38, 14, 35, 6, 7, 4, 16]`; `removeRoot()` gives `[35, 14, 16, 6, 7, 4]`.

## 36. seed 3228617638343361221, level 1

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(25)`, `add(15)`, `add(22)`, `add(55)`, `add(53)`, `add(32)`, `add(26)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the whole array `[53, 26, 32, 15, 25, 22]`
b) the array `[26, 15, 22, 55, 53, 32]`
c) the whole array `[26, 53, 32, 15, 25, 22]`
d) `[53, 32, 26, 25, 22, 15]`

**Key: a**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(25)` gives `[25]`; `add(15)` gives `[25, 15]`; `add(22)` gives `[25, 15, 22]`; `add(55)` gives `[55, 25, 22, 15]`; `add(53)` gives `[55, 53, 22, 15, 25]`; `add(32)` gives `[55, 53, 32, 15, 25, 22]`; `add(26)` gives `[55, 53, 32, 15, 25, 22, 26]`; `removeRoot()` gives `[53, 26, 32, 15, 25, 22]`.

## 37. seed 610253684922878624, level 2

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(34)`, `add(7)`, `add(8)`, `add(10)`, `add(30)`, `add(56)`, `removeRoot()`, `add(12)`, `removeRoot()`, `add(42)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[10, 30, 12, 56, 42]`
b) `[12, 30, 34, 42, 56]`
c) the array `[12, 30, 42, 34, 56]`
d) the array `[30, 10, 12, 7, 8]`

**Key: c**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(34)` gives `[34]`; `add(7)` gives `[7, 34]`; `add(8)` gives `[7, 34, 8]`; `add(10)` gives `[7, 10, 8, 34]`; `add(30)` gives `[7, 10, 8, 34, 30]`; `add(56)` gives `[7, 10, 8, 34, 30, 56]`; `removeRoot()` gives `[8, 10, 56, 34, 30]`; `add(12)` gives `[8, 10, 12, 34, 30, 56]`; `removeRoot()` gives `[10, 30, 12, 34, 56]`; `add(42)` gives `[10, 30, 12, 34, 56, 42]`; `removeRoot()` gives `[12, 30, 42, 34, 56]`.

## 38. seed 1136688133683259985, level 2

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(21)`, `add(27)`, `add(29)`, `add(22)`, `add(41)`, `add(2)`, `removeRoot()`, `add(23)`, `removeRoot()`, `add(36)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[27, 22, 29, 36, 41]`
b) the whole array `[23, 27, 36, 29, 41]`
c) `[36, 22, 21, 27, 41]`
d) the array `[23, 27, 29, 36, 41]`

**Key: b**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(21)` gives `[21]`; `add(27)` gives `[21, 27]`; `add(29)` gives `[21, 27, 29]`; `add(22)` gives `[21, 22, 29, 27]`; `add(41)` gives `[21, 22, 29, 27, 41]`; `add(2)` gives `[2, 22, 21, 27, 41, 29]`; `removeRoot()` gives `[21, 22, 29, 27, 41]`; `add(23)` gives `[21, 22, 23, 27, 41, 29]`; `removeRoot()` gives `[22, 27, 23, 29, 41]`; `add(36)` gives `[22, 27, 23, 29, 41, 36]`; `removeRoot()` gives `[23, 27, 36, 29, 41]`.

## 39. seed 4335171649057122906, level 1

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(31)`, `add(48)`, `add(1)`, `add(20)`, `add(8)`, `add(12)`, `add(16)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the whole array `[31, 20, 16, 12, 8, 1]`
b) the array `[8, 16, 12, 48, 20, 31]`
c) the whole array `[12, 31, 16, 20, 8, 1]`
d) the whole array `[48, 20, 1, 16, 8, 12]`

**Key: a**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(31)` gives `[31]`; `add(48)` gives `[48, 31]`; `add(1)` gives `[48, 31, 1]`; `add(20)` gives `[48, 31, 1, 20]`; `add(8)` gives `[48, 31, 1, 20, 8]`; `add(12)` gives `[48, 31, 12, 20, 8, 1]`; `add(16)` gives `[48, 31, 16, 20, 8, 1, 12]`; `removeRoot()` gives `[31, 20, 16, 12, 8, 1]`.

## 40. seed 4504067517100360870, level 2

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(5)`, `add(19)`, `add(33)`, `add(20)`, `add(52)`, `add(16)`, `removeRoot()`, `add(21)`, `removeRoot()`, `add(54)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the whole array `[20, 21, 33, 54, 52]`
b) `[20, 21, 33, 52, 54]`
c) the array `[54, 19, 16, 20, 52]`
d) the whole array `[20, 33, 21, 54, 52]`

**Key: d**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(5)` gives `[5]`; `add(19)` gives `[5, 19]`; `add(33)` gives `[5, 19, 33]`; `add(20)` gives `[5, 19, 33, 20]`; `add(52)` gives `[5, 19, 33, 20, 52]`; `add(16)` gives `[5, 19, 16, 20, 52, 33]`; `removeRoot()` gives `[16, 19, 33, 20, 52]`; `add(21)` gives `[16, 19, 21, 20, 52, 33]`; `removeRoot()` gives `[19, 20, 21, 33, 52]`; `add(54)` gives `[19, 20, 21, 33, 52, 54]`; `removeRoot()` gives `[20, 33, 21, 54, 52]`.

## 41. seed 4280045583886067860, level 2

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(32)`, `add(38)`, `add(33)`, `add(44)`, `add(31)`, `add(3)`, `removeRoot()`, `add(52)`, `removeRoot()`, `add(47)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[33, 38, 47, 44, 52]`
b) `[38, 31, 52, 44, 47]`
c) `[47, 32, 31, 44, 38]`
d) `[33, 38, 44, 47, 52]`

**Key: a**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(32)` gives `[32]`; `add(38)` gives `[32, 38]`; `add(33)` gives `[32, 38, 33]`; `add(44)` gives `[32, 38, 33, 44]`; `add(31)` gives `[31, 32, 33, 44, 38]`; `add(3)` gives `[3, 32, 31, 44, 38, 33]`; `removeRoot()` gives `[31, 32, 33, 44, 38]`; `add(52)` gives `[31, 32, 33, 44, 38, 52]`; `removeRoot()` gives `[32, 38, 33, 44, 52]`; `add(47)` gives `[32, 38, 33, 44, 52, 47]`; `removeRoot()` gives `[33, 38, 47, 44, 52]`.

## 42. seed 611196600208188361, level 1

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(15)`, `add(20)`, `add(39)`, `add(9)`, `add(29)`, `add(21)`, `add(5)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[21, 15, 9, 20, 29, 39]`
b) the whole array `[5, 20, 39, 9, 29, 21]`
c) `[9, 15, 21, 20, 29, 39]`
d) the whole array `[9, 15, 20, 21, 29, 39]`

**Key: c**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(15)` gives `[15]`; `add(20)` gives `[15, 20]`; `add(39)` gives `[15, 20, 39]`; `add(9)` gives `[9, 15, 39, 20]`; `add(29)` gives `[9, 15, 39, 20, 29]`; `add(21)` gives `[9, 15, 21, 20, 29, 39]`; `add(5)` gives `[5, 15, 9, 20, 29, 39, 21]`; `removeRoot()` gives `[9, 15, 21, 20, 29, 39]`.

## 43. seed 1535458164780542346, level 1

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(28)`, `add(39)`, `add(42)`, `add(31)`, `add(19)`, `add(27)`, `add(38)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the array `[38, 39, 42, 31, 19, 27]`
b) `[39, 31, 38, 28, 19, 27]`
c) the whole array `[27, 28, 31, 38, 39, 42]`
d) the whole array `[27, 28, 38, 39, 31, 42]`

**Key: d**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(28)` gives `[28]`; `add(39)` gives `[28, 39]`; `add(42)` gives `[28, 39, 42]`; `add(31)` gives `[28, 31, 42, 39]`; `add(19)` gives `[19, 28, 42, 39, 31]`; `add(27)` gives `[19, 28, 27, 39, 31, 42]`; `add(38)` gives `[19, 28, 27, 39, 31, 42, 38]`; `removeRoot()` gives `[27, 28, 38, 39, 31, 42]`.

## 44. seed 3078706725446247509, level 1

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(8)`, `add(37)`, `add(11)`, `add(50)`, `add(24)`, `add(49)`, `add(35)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the whole array `[11, 37, 35, 50, 24, 49]`
b) `[11, 24, 35, 50, 37, 49]`
c) the array `[35, 24, 11, 50, 37, 49]`
d) the array `[11, 24, 35, 37, 49, 50]`

**Key: b**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(8)` gives `[8]`; `add(37)` gives `[8, 37]`; `add(11)` gives `[8, 37, 11]`; `add(50)` gives `[8, 37, 11, 50]`; `add(24)` gives `[8, 24, 11, 50, 37]`; `add(49)` gives `[8, 24, 11, 50, 37, 49]`; `add(35)` gives `[8, 24, 11, 50, 37, 49, 35]`; `removeRoot()` gives `[11, 24, 35, 50, 37, 49]`.

## 45. seed 2343832980666600457, level 1

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(30)`, `add(23)`, `add(3)`, `add(32)`, `add(38)`, `add(55)`, `add(27)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[27, 32, 38, 23, 30, 3]`
b) the array `[27, 23, 3, 32, 38, 55]`
c) the array `[38, 32, 27, 23, 30, 3]`
d) the array `[38, 32, 30, 27, 23, 3]`

**Key: c**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(30)` gives `[30]`; `add(23)` gives `[30, 23]`; `add(3)` gives `[30, 23, 3]`; `add(32)` gives `[32, 30, 3, 23]`; `add(38)` gives `[38, 32, 3, 23, 30]`; `add(55)` gives `[55, 32, 38, 23, 30, 3]`; `add(27)` gives `[55, 32, 38, 23, 30, 3, 27]`; `removeRoot()` gives `[38, 32, 27, 23, 30, 3]`.

## 46. seed 1398181603005885223, level 2

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(29)`, `add(13)`, `add(17)`, `add(40)`, `add(11)`, `add(20)`, `removeRoot()`, `add(25)`, `removeRoot()`, `add(28)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the array `[20, 28, 25, 40, 29]`
b) the whole array `[20, 25, 28, 29, 40]`
c) the array `[17, 20, 28, 40, 25]`
d) `[28, 13, 17, 40, 29]`

**Key: a**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(29)` gives `[29]`; `add(13)` gives `[13, 29]`; `add(17)` gives `[13, 29, 17]`; `add(40)` gives `[13, 29, 17, 40]`; `add(11)` gives `[11, 13, 17, 40, 29]`; `add(20)` gives `[11, 13, 17, 40, 29, 20]`; `removeRoot()` gives `[13, 20, 17, 40, 29]`; `add(25)` gives `[13, 20, 17, 40, 29, 25]`; `removeRoot()` gives `[17, 20, 25, 40, 29]`; `add(28)` gives `[17, 20, 25, 40, 29, 28]`; `removeRoot()` gives `[20, 28, 25, 40, 29]`.

## 47. seed 1387174414726910683, level 2

An empty array-backed binary min-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(38)`, `add(51)`, `add(5)`, `add(46)`, `add(13)`, `add(44)`, `removeRoot()`, `add(54)`, `removeRoot()`, `add(32)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the whole array `[38, 44, 46, 51, 54]`
b) `[38, 44, 54, 51, 46]`
c) the whole array `[32, 51, 54, 46, 13]`
d) the whole array `[38, 13, 54, 51, 46]`

**Key: b**

Explanation: An add appends at the end and sifts up while it is smaller than its parent; a removal puts the last element at the root and sifts it down towards the smaller child. `add(38)` gives `[38]`; `add(51)` gives `[38, 51]`; `add(5)` gives `[5, 51, 38]`; `add(46)` gives `[5, 46, 38, 51]`; `add(13)` gives `[5, 13, 38, 51, 46]`; `add(44)` gives `[5, 13, 38, 51, 46, 44]`; `removeRoot()` gives `[13, 44, 38, 51, 46]`; `add(54)` gives `[13, 44, 38, 51, 46, 54]`; `removeRoot()` gives `[38, 44, 54, 51, 46]`; `add(32)` gives `[32, 44, 38, 51, 46, 54]`; `removeRoot()` gives `[38, 44, 54, 51, 46]`.

## 48. seed 1220105010001733304, level 1

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(38)`, `add(30)`, `add(36)`, `add(29)`, `add(55)`, `add(7)`, `add(27)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) `[38, 30, 36, 29, 27, 7]`
b) the whole array `[27, 38, 36, 29, 30, 7]`
c) the array `[38, 36, 30, 29, 27, 7]`
d) `[36, 30, 27, 29, 55, 7]`

**Key: a**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(38)` gives `[38]`; `add(30)` gives `[38, 30]`; `add(36)` gives `[38, 30, 36]`; `add(29)` gives `[38, 30, 36, 29]`; `add(55)` gives `[55, 38, 36, 29, 30]`; `add(7)` gives `[55, 38, 36, 29, 30, 7]`; `add(27)` gives `[55, 38, 36, 29, 30, 7, 27]`; `removeRoot()` gives `[38, 30, 36, 29, 27, 7]`.

## 49. seed 3321510378407876977, level 2

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(17)`, `add(50)`, `add(57)`, `add(39)`, `add(38)`, `add(27)`, `removeRoot()`, `add(29)`, `removeRoot()`, `add(54)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the whole array `[38, 39, 54, 50, 57]`
b) `[54, 39, 27, 29, 38]`
c) `[39, 38, 29, 17, 27]`
d) the whole array `[50, 39, 29, 17, 38]`

**Key: c**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(17)` gives `[17]`; `add(50)` gives `[50, 17]`; `add(57)` gives `[57, 17, 50]`; `add(39)` gives `[57, 39, 50, 17]`; `add(38)` gives `[57, 39, 50, 17, 38]`; `add(27)` gives `[57, 39, 50, 17, 38, 27]`; `removeRoot()` gives `[50, 39, 27, 17, 38]`; `add(29)` gives `[50, 39, 29, 17, 38, 27]`; `removeRoot()` gives `[39, 38, 29, 17, 27]`; `add(54)` gives `[54, 38, 39, 17, 27, 29]`; `removeRoot()` gives `[39, 38, 29, 17, 27]`.

## 50. seed 2558348047455563360, level 2

An empty array-backed binary max-heap (children of index `i` at `2i + 1` and `2i + 2`) takes these operations in order: `add(34)`, `add(43)`, `add(2)`, `add(31)`, `add(4)`, `add(19)`, `removeRoot()`, `add(5)`, `removeRoot()`, `add(16)`, `removeRoot()`. `removeRoot()` moves the last element to the root and sifts it down. What does the array hold afterwards?

a) the whole array `[19, 16, 5, 4, 2]`
b) the array `[16, 34, 19, 31, 4]`
c) the array `[19, 5, 16, 2, 4]`
d) the whole array `[19, 16, 2, 5, 4]`

**Key: c**

Explanation: An add appends at the end and sifts up while it is larger than its parent; a removal puts the last element at the root and sifts it down towards the larger child. `add(34)` gives `[34]`; `add(43)` gives `[43, 34]`; `add(2)` gives `[43, 34, 2]`; `add(31)` gives `[43, 34, 2, 31]`; `add(4)` gives `[43, 34, 2, 31, 4]`; `add(19)` gives `[43, 34, 19, 31, 4, 2]`; `removeRoot()` gives `[34, 31, 19, 2, 4]`; `add(5)` gives `[34, 31, 19, 2, 4, 5]`; `removeRoot()` gives `[31, 5, 19, 2, 4]`; `add(16)` gives `[31, 5, 19, 2, 4, 16]`; `removeRoot()` gives `[19, 5, 16, 2, 4]`.
