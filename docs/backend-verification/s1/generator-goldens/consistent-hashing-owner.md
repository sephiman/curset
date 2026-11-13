# Consistent hashing (`consistent-hashing-owner`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 2826621112684604894, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 45, `B` at 62, `C` at 78. Then node `D` joins at position 14. Of the keys at positions 1, 12, 14, 15, 17, 78, how many change owner?

a) 2
b) 1
c) 6
d) 3

**Key: d**

Explanation: Compute the clockwise owner of each key before and after. 1: `A` to `D`; 12: `A` to `D`; 14: `A` to `D`; 15: `A` to `A`; 17: `A` to `A`; 78: `C` to `C`. 3 of them end up with a different owner; only the keys in the arc next to the new node move.

## 2. seed 205579899297895588, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 16, `E` at 38, `B` at 49, `C` at 55, `D` at 99. Then node `E` leaves. Of the keys at positions 8, 9, 19, 38, 46, 63, 86, 93, how many change owner?

a) 1
b) 2
c) 8
d) 3

**Key: b**

Explanation: Compute the clockwise owner of each key before and after. 8: `A` to `A`; 9: `A` to `A`; 19: `E` to `B`; 38: `E` to `B`; 46: `B` to `B`; 63: `D` to `D`; 86: `D` to `D`; 93: `D` to `D`. 2 of them end up with a different owner; only the keys in the arc next to the departed node move.

## 3. seed 2404408618222546783, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `C` at 38, `A` at 73, `B` at 94. Then node `D` joins at position 11. Of the keys at positions 1, 25, 40, 64, 78, 88, 97, how many change owner?

a) 2
b) 3
c) 1
d) 7

**Key: a**

Explanation: Compute the clockwise owner of each key before and after. 1: `C` to `D`; 25: `C` to `C`; 40: `A` to `A`; 64: `A` to `A`; 78: `B` to `B`; 88: `B` to `B`; 97: `C` to `D`. 2 of them end up with a different owner; only the keys in the arc next to the new node move.

## 4. seed 4336962999521843541, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `D` at 7, `B` at 29, `E` at 38, `A` at 40, `C` at 70. Then node `C` leaves. Which node owns the key at position 57 afterwards?

a) Node `B`
b) Node `A`
c) Node `C`
d) Node `D`

**Key: d**

Explanation: Before the change the first node clockwise from 57 was `C`. The ring then holds `D` at 7, `B` at 29, `E` at 38, `A` at 40; going clockwise from 57 the first node is `D`, so it owns the key. Counterclockwise would give `A`, which is not the rule.

## 5. seed 65327873958547667, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `D` at 0, `B` at 9, `A` at 25, `C` at 40. Then node `D` leaves. Which node owns the key at position 95 afterwards?

a) Node `C`
b) Node `D`
c) Node `A`
d) Node `B`

**Key: d**

Explanation: Before the change the first node clockwise from 95 was `D`. The ring then holds `B` at 9, `A` at 25, `C` at 40; going clockwise from 95 the first node is `B`, so it owns the key. Counterclockwise would give `C`, which is not the rule.

## 6. seed 4192410850797803199, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `C` at 2, `B` at 6, `A` at 42. Then node `D` joins at position 75. Of the keys at positions 28, 53, 56, 67, 72, 80, 92, 97, how many change owner?

a) 8
b) 4
c) 5
d) 3

**Key: b**

Explanation: Compute the clockwise owner of each key before and after. 28: `A` to `A`; 53: `C` to `D`; 56: `C` to `D`; 67: `C` to `D`; 72: `C` to `D`; 80: `C` to `C`; 92: `C` to `C`; 97: `C` to `C`. 4 of them end up with a different owner; only the keys in the arc next to the new node move.

## 7. seed 332184997771077315, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 55, `B` at 75, `C` at 84. Then node `D` joins at position 50. Of the keys at positions 15, 39, 47, 50, 64, 78, how many change owner?

a) 4
b) 3
c) 6
d) 1

**Key: a**

Explanation: Compute the clockwise owner of each key before and after. 15: `A` to `D`; 39: `A` to `D`; 47: `A` to `D`; 50: `A` to `D`; 64: `B` to `B`; 78: `C` to `C`. 4 of them end up with a different owner; only the keys in the arc next to the new node move.

## 8. seed 3145480983183313567, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 18, `C` at 32, `D` at 54, `E` at 86, `B` at 96. Then node `D` leaves. Of the keys at positions 16, 21, 22, 46, 47, 79, 91, how many change owner?

a) 2
b) 3
c) 1
d) 7

**Key: a**

Explanation: Compute the clockwise owner of each key before and after. 16: `A` to `A`; 21: `C` to `C`; 22: `C` to `C`; 46: `D` to `E`; 47: `D` to `E`; 79: `E` to `E`; 91: `B` to `B`. 2 of them end up with a different owner; only the keys in the arc next to the departed node move.

## 9. seed 4202536965759009034, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `C` at 17, `A` at 25, `D` at 46, `B` at 51. Then node `C` leaves. Which node owns the key at position 88 afterwards?

a) Node `C`
b) Node `A`
c) Node `B`
d) Node `D`

**Key: b**

Explanation: Before the change the first node clockwise from 88 was `C`. The ring then holds `A` at 25, `D` at 46, `B` at 51; going clockwise from 88 the first node is `A`, so it owns the key. Counterclockwise would give `B`, which is not the rule.

## 10. seed 3839612320203162019, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `C` at 11, `D` at 45, `A` at 47, `B` at 50, `E` at 78. Then node `C` leaves. Which node owns the key at position 89 afterwards?

a) Node `D`
b) Node `A`
c) Node `C`
d) Node `E`

**Key: a**

Explanation: Before the change the first node clockwise from 89 was `C`. The ring then holds `D` at 45, `A` at 47, `B` at 50, `E` at 78; going clockwise from 89 the first node is `D`, so it owns the key. Counterclockwise would give `E`, which is not the rule.

## 11. seed 2117989040594523433, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `D` at 8, `C` at 12, `E` at 31, `B` at 96, `A` at 99. Then node `A` leaves. Which node owns the key at position 97 afterwards?

a) Node `D`
b) Node `B`
c) Node `A`
d) Node `C`

**Key: a**

Explanation: Before the change the first node clockwise from 97 was `A`. The ring then holds `D` at 8, `C` at 12, `E` at 31, `B` at 96; going clockwise from 97 the first node is `D`, so it owns the key. Counterclockwise would give `B`, which is not the rule.

## 12. seed 3120754460458832562, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `E` at 10, `A` at 13, `C` at 18, `B` at 46, `D` at 78. Then node `B` leaves. Of the keys at positions 16, 22, 45, 76, 94, 97, how many change owner?

a) 2
b) 3
c) 6
d) 1

**Key: a**

Explanation: Compute the clockwise owner of each key before and after. 16: `C` to `C`; 22: `B` to `D`; 45: `B` to `D`; 76: `D` to `D`; 94: `E` to `E`; 97: `E` to `E`. 2 of them end up with a different owner; only the keys in the arc next to the departed node move.

## 13. seed 4331601529056384014, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 5, `E` at 33, `C` at 61, `B` at 68, `D` at 99. Then node `E` leaves. Which node owns the key at position 10 afterwards?

a) Node `B`
b) Node `C`
c) Node `E`
d) Node `A`

**Key: b**

Explanation: Before the change the first node clockwise from 10 was `E`. The ring then holds `A` at 5, `C` at 61, `B` at 68, `D` at 99; going clockwise from 10 the first node is `C`, so it owns the key. Counterclockwise would give `A`, which is not the rule.

## 14. seed 2378367190314136319, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 41, `B` at 43, `D` at 74, `C` at 78. Then node `A` leaves. Which node owns the key at position 91 afterwards?

a) Node `C`
b) Node `D`
c) Node `B`
d) Node `A`

**Key: c**

Explanation: Before the change the first node clockwise from 91 was `A`. The ring then holds `B` at 43, `D` at 74, `C` at 78; going clockwise from 91 the first node is `B`, so it owns the key. Counterclockwise would give `C`, which is not the rule.

## 15. seed 3748701315182972333, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 4, `B` at 31, `D` at 65, `C` at 93. Then node `E` joins at position 76. Of the keys at positions 33, 47, 60, 64, 68, 74, 77, 80, how many change owner?

a) 3
b) 8
c) 1
d) 2

**Key: d**

Explanation: Compute the clockwise owner of each key before and after. 33: `D` to `D`; 47: `D` to `D`; 60: `D` to `D`; 64: `D` to `D`; 68: `C` to `E`; 74: `C` to `E`; 77: `C` to `C`; 80: `C` to `C`. 2 of them end up with a different owner; only the keys in the arc next to the new node move.

## 16. seed 1884437597944223826, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 67, `C` at 92, `B` at 99. Then node `D` joins at position 10. Of the keys at positions 1, 2, 3, 42, 80, 81, 96, how many change owner?

a) 1
b) 7
c) 2
d) 3

**Key: d**

Explanation: Compute the clockwise owner of each key before and after. 1: `A` to `D`; 2: `A` to `D`; 3: `A` to `D`; 42: `A` to `A`; 80: `C` to `C`; 81: `C` to `C`; 96: `B` to `B`. 3 of them end up with a different owner; only the keys in the arc next to the new node move.

## 17. seed 4304558275050667772, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 2, `B` at 47, `D` at 90, `C` at 96. Then node `E` joins at position 34. Of the keys at positions 7, 9, 15, 28, 32, 58, 91, 93, how many change owner?

a) 5
b) 8
c) 1
d) 6

**Key: a**

Explanation: Compute the clockwise owner of each key before and after. 7: `B` to `E`; 9: `B` to `E`; 15: `B` to `E`; 28: `B` to `E`; 32: `B` to `E`; 58: `D` to `D`; 91: `C` to `C`; 93: `C` to `C`. 5 of them end up with a different owner; only the keys in the arc next to the new node move.

## 18. seed 1098289471732588425, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `C` at 19, `B` at 57, `D` at 60, `A` at 84. Then node `C` leaves. Which node owns the key at position 18 afterwards?

a) Node `B`
b) Node `A`
c) Node `C`
d) Node `D`

**Key: a**

Explanation: Before the change the first node clockwise from 18 was `C`. The ring then holds `B` at 57, `D` at 60, `A` at 84; going clockwise from 18 the first node is `B`, so it owns the key. Counterclockwise would give `A`, which is not the rule.

## 19. seed 2032630214280821918, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `C` at 20, `B` at 49, `D` at 51, `A` at 86. Then node `C` leaves. Which node owns the key at position 91 afterwards?

a) Node `C`
b) Node `B`
c) Node `A`
d) Node `D`

**Key: b**

Explanation: Before the change the first node clockwise from 91 was `C`. The ring then holds `B` at 49, `D` at 51, `A` at 86; going clockwise from 91 the first node is `B`, so it owns the key. Counterclockwise would give `A`, which is not the rule.

## 20. seed 406360410425784883, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `B` at 24, `A` at 35, `E` at 41, `D` at 52, `C` at 55. Then node `B` leaves. Which node owns the key at position 7 afterwards?

a) Node `A`
b) Node `B`
c) Node `C`
d) Node `E`

**Key: a**

Explanation: Before the change the first node clockwise from 7 was `B`. The ring then holds `A` at 35, `E` at 41, `D` at 52, `C` at 55; going clockwise from 7 the first node is `A`, so it owns the key. Counterclockwise would give `C`, which is not the rule.

## 21. seed 1303040175695028462, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 15, `D` at 27, `C` at 32, `B` at 85. Then node `B` leaves. Which node owns the key at position 69 afterwards?

a) Node `D`
b) Node `B`
c) Node `A`
d) Node `C`

**Key: c**

Explanation: Before the change the first node clockwise from 69 was `B`. The ring then holds `A` at 15, `D` at 27, `C` at 32; going clockwise from 69 the first node is `A`, so it owns the key. Counterclockwise would give `C`, which is not the rule.

## 22. seed 4594428198279712146, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `D` at 9, `A` at 15, `B` at 52, `C` at 63. Then node `E` joins at position 2. Of the keys at positions 31, 42, 43, 50, 95, 96, how many change owner?

a) 1
b) 3
c) 2
d) 6

**Key: c**

Explanation: Compute the clockwise owner of each key before and after. 31: `B` to `B`; 42: `B` to `B`; 43: `B` to `B`; 50: `B` to `B`; 95: `D` to `E`; 96: `D` to `E`. 2 of them end up with a different owner; only the keys in the arc next to the new node move.

## 23. seed 3633623481711420068, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `C` at 21, `D` at 24, `A` at 60, `B` at 80. Then node `C` leaves. Which node owns the key at position 96 afterwards?

a) Node `D`
b) Node `A`
c) Node `C`
d) Node `B`

**Key: a**

Explanation: Before the change the first node clockwise from 96 was `C`. The ring then holds `D` at 24, `A` at 60, `B` at 80; going clockwise from 96 the first node is `D`, so it owns the key. Counterclockwise would give `B`, which is not the rule.

## 24. seed 547103668387178490, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `E` at 34, `A` at 75, `B` at 77, `D` at 81, `C` at 91. Then node `A` leaves. Which node owns the key at position 40 afterwards?

a) Node `E`
b) Node `B`
c) Node `D`
d) Node `A`

**Key: b**

Explanation: Before the change the first node clockwise from 40 was `A`. The ring then holds `E` at 34, `B` at 77, `D` at 81, `C` at 91; going clockwise from 40 the first node is `B`, so it owns the key. Counterclockwise would give `E`, which is not the rule.

## 25. seed 4404053364715349646, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `B` at 7, `A` at 53, `C` at 55. Then node `D` joins at position 19. Of the keys at positions 0, 6, 11, 14, 47, 62, 83, 87, how many change owner?

a) 3
b) 2
c) 8
d) 1

**Key: b**

Explanation: Compute the clockwise owner of each key before and after. 0: `B` to `B`; 6: `B` to `B`; 11: `A` to `D`; 14: `A` to `D`; 47: `A` to `A`; 62: `B` to `B`; 83: `B` to `B`; 87: `B` to `B`. 2 of them end up with a different owner; only the keys in the arc next to the new node move.

## 26. seed 3915503766026497042, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `B` at 14, `A` at 60, `C` at 77, `D` at 87. Then node `B` leaves. Of the keys at positions 10, 12, 19, 62, 66, 82, 87, 88, how many change owner?

a) 3
b) 8
c) 2
d) 4

**Key: a**

Explanation: Compute the clockwise owner of each key before and after. 10: `B` to `A`; 12: `B` to `A`; 19: `A` to `A`; 62: `C` to `C`; 66: `C` to `C`; 82: `D` to `D`; 87: `D` to `D`; 88: `B` to `A`. 3 of them end up with a different owner; only the keys in the arc next to the departed node move.

## 27. seed 3004032391654724087, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `D` at 7, `B` at 8, `A` at 57, `C` at 62. Then node `A` leaves. Of the keys at positions 1, 2, 29, 43, 71, 77, how many change owner?

a) 0
b) 6
c) 2
d) 1

**Key: c**

Explanation: Compute the clockwise owner of each key before and after. 1: `D` to `D`; 2: `D` to `D`; 29: `A` to `C`; 43: `A` to `C`; 71: `D` to `D`; 77: `D` to `D`. 2 of them end up with a different owner; only the keys in the arc next to the departed node move.

## 28. seed 3765466580203951304, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `D` at 47, `B` at 58, `A` at 87, `C` at 94. Then node `B` leaves. Which node owns the key at position 52 afterwards?

a) Node `D`
b) Node `A`
c) Node `C`
d) Node `B`

**Key: b**

Explanation: Before the change the first node clockwise from 52 was `B`. The ring then holds `D` at 47, `A` at 87, `C` at 94; going clockwise from 52 the first node is `A`, so it owns the key. Counterclockwise would give `D`, which is not the rule.

## 29. seed 3844432714737124152, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `D` at 27, `B` at 66, `C` at 79, `A` at 96. Then node `D` leaves. Which node owns the key at position 99 afterwards?

a) Node `C`
b) Node `D`
c) Node `A`
d) Node `B`

**Key: d**

Explanation: Before the change the first node clockwise from 99 was `D`. The ring then holds `B` at 66, `C` at 79, `A` at 96; going clockwise from 99 the first node is `B`, so it owns the key. Counterclockwise would give `A`, which is not the rule.

## 30. seed 2446343134863964611, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `C` at 3, `D` at 17, `A` at 20, `B` at 91. Then node `E` joins at position 86. Of the keys at positions 1, 8, 19, 27, 44, 59, 60, 74, how many change owner?

a) 8
b) 0
c) 5
d) 1

**Key: c**

Explanation: Compute the clockwise owner of each key before and after. 1: `C` to `C`; 8: `D` to `D`; 19: `A` to `A`; 27: `B` to `E`; 44: `B` to `E`; 59: `B` to `E`; 60: `B` to `E`; 74: `B` to `E`. 5 of them end up with a different owner; only the keys in the arc next to the new node move.

## 31. seed 1684221530035836088, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 28, `C` at 64, `D` at 66, `B` at 83. Then node `C` leaves. Which node owns the key at position 37 afterwards?

a) Node `D`
b) Node `B`
c) Node `A`
d) Node `C`

**Key: a**

Explanation: Before the change the first node clockwise from 37 was `C`. The ring then holds `A` at 28, `D` at 66, `B` at 83; going clockwise from 37 the first node is `D`, so it owns the key. Counterclockwise would give `A`, which is not the rule.

## 32. seed 892172804610904229, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 30, `B` at 35, `C` at 50, `D` at 60. Then node `E` joins at position 80. Of the keys at positions 30, 46, 53, 63, 67, 73, how many change owner?

a) 1
b) 0
c) 3
d) 6

**Key: c**

Explanation: Compute the clockwise owner of each key before and after. 30: `A` to `A`; 46: `C` to `C`; 53: `D` to `D`; 63: `A` to `E`; 67: `A` to `E`; 73: `A` to `E`. 3 of them end up with a different owner; only the keys in the arc next to the new node move.

## 33. seed 458116452024902833, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 12, `C` at 21, `B` at 61, `D` at 64. Then node `C` leaves. Which node owns the key at position 14 afterwards?

a) Node `B`
b) Node `C`
c) Node `D`
d) Node `A`

**Key: a**

Explanation: Before the change the first node clockwise from 14 was `C`. The ring then holds `A` at 12, `B` at 61, `D` at 64; going clockwise from 14 the first node is `B`, so it owns the key. Counterclockwise would give `A`, which is not the rule.

## 34. seed 1696472872140247947, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `C` at 41, `A` at 61, `D` at 66, `B` at 70. Then node `A` leaves. Of the keys at positions 13, 30, 48, 53, 83, 89, how many change owner?

a) 1
b) 3
c) 0
d) 2

**Key: d**

Explanation: Compute the clockwise owner of each key before and after. 13: `C` to `C`; 30: `C` to `C`; 48: `A` to `D`; 53: `A` to `D`; 83: `C` to `C`; 89: `C` to `C`. 2 of them end up with a different owner; only the keys in the arc next to the departed node move.

## 35. seed 1951250295120247529, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `C` at 61, `B` at 71, `D` at 96, `A` at 97. Then node `C` leaves. Which node owns the key at position 49 afterwards?

a) Node `A`
b) Node `C`
c) Node `D`
d) Node `B`

**Key: d**

Explanation: Before the change the first node clockwise from 49 was `C`. The ring then holds `B` at 71, `D` at 96, `A` at 97; going clockwise from 49 the first node is `B`, so it owns the key. Counterclockwise would give `A`, which is not the rule.

## 36. seed 1147443123283889638, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `D` at 5, `A` at 19, `B` at 25, `C` at 46. Then node `D` leaves. Which node owns the key at position 61 afterwards?

a) Node `A`
b) Node `C`
c) Node `B`
d) Node `D`

**Key: a**

Explanation: Before the change the first node clockwise from 61 was `D`. The ring then holds `A` at 19, `B` at 25, `C` at 46; going clockwise from 61 the first node is `A`, so it owns the key. Counterclockwise would give `C`, which is not the rule.

## 37. seed 103848967321453113, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 38, `D` at 47, `C` at 65, `B` at 90. Then node `A` leaves. Which node owns the key at position 5 afterwards?

a) Node `A`
b) Node `B`
c) Node `D`
d) Node `C`

**Key: c**

Explanation: Before the change the first node clockwise from 5 was `A`. The ring then holds `D` at 47, `C` at 65, `B` at 90; going clockwise from 5 the first node is `D`, so it owns the key. Counterclockwise would give `B`, which is not the rule.

## 38. seed 2700773354101907971, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 3, `E` at 19, `B` at 21, `D` at 34, `C` at 42. Then node `A` leaves. Which node owns the key at position 93 afterwards?

a) Node `B`
b) Node `E`
c) Node `A`
d) Node `C`

**Key: b**

Explanation: Before the change the first node clockwise from 93 was `A`. The ring then holds `E` at 19, `B` at 21, `D` at 34, `C` at 42; going clockwise from 93 the first node is `E`, so it owns the key. Counterclockwise would give `C`, which is not the rule.

## 39. seed 2932365758991061363, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 22, `B` at 38, `D` at 61, `E` at 63, `C` at 84. Then node `A` leaves. Which node owns the key at position 8 afterwards?

a) Node `A`
b) Node `D`
c) Node `C`
d) Node `B`

**Key: d**

Explanation: Before the change the first node clockwise from 8 was `A`. The ring then holds `B` at 38, `D` at 61, `E` at 63, `C` at 84; going clockwise from 8 the first node is `B`, so it owns the key. Counterclockwise would give `C`, which is not the rule.

## 40. seed 3128265431232305146, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 5, `B` at 44, `D` at 46, `C` at 71, `E` at 97. Then node `A` leaves. Which node owns the key at position 0 afterwards?

a) Node `D`
b) Node `A`
c) Node `E`
d) Node `B`

**Key: d**

Explanation: Before the change the first node clockwise from 0 was `A`. The ring then holds `B` at 44, `D` at 46, `C` at 71, `E` at 97; going clockwise from 0 the first node is `B`, so it owns the key. Counterclockwise would give `E`, which is not the rule.

## 41. seed 3850974427212980544, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `E` at 23, `B` at 52, `D` at 77, `C` at 86, `A` at 97. Then node `C` leaves. Of the keys at positions 14, 25, 29, 31, 44, 46, 80, 84, how many change owner?

a) 3
b) 1
c) 2
d) 0

**Key: c**

Explanation: Compute the clockwise owner of each key before and after. 14: `E` to `E`; 25: `B` to `B`; 29: `B` to `B`; 31: `B` to `B`; 44: `B` to `B`; 46: `B` to `B`; 80: `C` to `A`; 84: `C` to `A`. 2 of them end up with a different owner; only the keys in the arc next to the departed node move.

## 42. seed 616134271711846874, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `B` at 42, `C` at 72, `A` at 77. Then node `D` joins at position 70. Of the keys at positions 13, 31, 43, 46, 48, 51, 94, how many change owner?

a) 5
b) 0
c) 7
d) 4

**Key: d**

Explanation: Compute the clockwise owner of each key before and after. 13: `B` to `B`; 31: `B` to `B`; 43: `C` to `D`; 46: `C` to `D`; 48: `C` to `D`; 51: `C` to `D`; 94: `B` to `B`. 4 of them end up with a different owner; only the keys in the arc next to the new node move.

## 43. seed 4264542765202507490, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `D` at 21, `C` at 51, `B` at 86, `E` at 89, `A` at 93. Then node `D` leaves. Of the keys at positions 4, 15, 33, 45, 53, 61, 91, how many change owner?

a) 1
b) 2
c) 3
d) 7

**Key: b**

Explanation: Compute the clockwise owner of each key before and after. 4: `D` to `C`; 15: `D` to `C`; 33: `C` to `C`; 45: `C` to `C`; 53: `B` to `B`; 61: `B` to `B`; 91: `A` to `A`. 2 of them end up with a different owner; only the keys in the arc next to the departed node move.

## 44. seed 2915703591357777691, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 11, `B` at 22, `C` at 81, `D` at 98. Then node `C` leaves. Which node owns the key at position 43 afterwards?

a) Node `B`
b) Node `D`
c) Node `C`
d) Node `A`

**Key: b**

Explanation: Before the change the first node clockwise from 43 was `C`. The ring then holds `A` at 11, `B` at 22, `D` at 98; going clockwise from 43 the first node is `D`, so it owns the key. Counterclockwise would give `B`, which is not the rule.

## 45. seed 1045432192393801276, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `C` at 29, `A` at 38, `B` at 57, `D` at 85. Then node `B` leaves. Which node owns the key at position 40 afterwards?

a) Node `B`
b) Node `A`
c) Node `D`
d) Node `C`

**Key: c**

Explanation: Before the change the first node clockwise from 40 was `B`. The ring then holds `C` at 29, `A` at 38, `D` at 85; going clockwise from 40 the first node is `D`, so it owns the key. Counterclockwise would give `A`, which is not the rule.

## 46. seed 4595903558293728625, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `D` at 7, `C` at 8, `B` at 49, `A` at 58. Then node `E` joins at position 95. Of the keys at positions 1, 39, 44, 57, 60, 91, how many change owner?

a) 6
b) 1
c) 3
d) 2

**Key: d**

Explanation: Compute the clockwise owner of each key before and after. 1: `D` to `D`; 39: `B` to `B`; 44: `B` to `B`; 57: `A` to `A`; 60: `D` to `E`; 91: `D` to `E`. 2 of them end up with a different owner; only the keys in the arc next to the new node move.

## 47. seed 4577437600031791936, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 5, `D` at 15, `B` at 32, `C` at 61. Then node `C` leaves. Which node owns the key at position 51 afterwards?

a) Node `B`
b) Node `C`
c) Node `D`
d) Node `A`

**Key: d**

Explanation: Before the change the first node clockwise from 51 was `C`. The ring then holds `A` at 5, `D` at 15, `B` at 32; going clockwise from 51 the first node is `A`, so it owns the key. Counterclockwise would give `B`, which is not the rule.

## 48. seed 1064365703107342109, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `B` at 21, `A` at 85, `C` at 93. Then node `D` joins at position 8. Of the keys at positions 10, 14, 29, 66, 97, 98, how many change owner?

a) 6
b) 3
c) 2
d) 1

**Key: c**

Explanation: Compute the clockwise owner of each key before and after. 10: `B` to `B`; 14: `B` to `B`; 29: `A` to `A`; 66: `A` to `A`; 97: `B` to `D`; 98: `B` to `D`. 2 of them end up with a different owner; only the keys in the arc next to the new node move.

## 49. seed 3548808140826148728, level 2

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `A` at 34, `C` at 55, `B` at 88, `D` at 99. Then node `E` joins at position 85. Of the keys at positions 0, 11, 45, 48, 66, 79, how many change owner?

a) 1
b) 6
c) 2
d) 0

**Key: c**

Explanation: Compute the clockwise owner of each key before and after. 0: `A` to `A`; 11: `A` to `A`; 45: `C` to `C`; 48: `C` to `C`; 66: `B` to `E`; 79: `B` to `E`. 2 of them end up with a different owner; only the keys in the arc next to the new node move.

## 50. seed 3925074090248585767, level 1

A ring has positions 0 to 99. A key belongs to the first node found going clockwise (towards higher positions, wrapping from 99 to 0) from the key's position, a node at the key's own position included. Nodes: `E` at 21, `A` at 58, `D` at 61, `B` at 89, `C` at 90. Then node `E` leaves. Which node owns the key at position 92 afterwards?

a) Node `D`
b) Node `A`
c) Node `C`
d) Node `E`

**Key: b**

Explanation: Before the change the first node clockwise from 92 was `E`. The ring then holds `A` at 58, `D` at 61, `B` at 89, `C` at 90; going clockwise from 92 the first node is `A`, so it owns the key. Counterclockwise would give `C`, which is not the rule.
