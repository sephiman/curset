# Lamport and vector clocks (`logical-clocks`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 1533500503003568843, level 1

Each of 2 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P1 sends a message; `b`: P1 has a local step; `c`: P1 has a local step; `d`: P2 receives the message of `a`; `e`: P1 has a local step; `f`: P1 sends a message; `g`: P2 receives the message of `f`. A message carries its sender's clock after the send. What is the timestamp of event `g`?

a) 7
b) 5
c) 6
d) 4

**Key: c**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 1 + 1 = 2; `c` = 2 + 1 = 3; `d` = max(0, 1) + 1 = 2; `e` = 3 + 1 = 4; `f` = 4 + 1 = 5; `g` = max(2, 5) + 1 = 6.

## 2. seed 2737046291740163461, level 1

Each of 2 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P1 sends a message; `b`: P1 sends a message; `c`: P2 receives the message of `b`; `d`: P1 has a local step; `e`: P2 has a local step; `f`: P2 receives the message of `a`; `g`: P1 sends a message; `h`: P2 sends a message. A message carries its sender's clock after the send. What is the timestamp of event `f`?

a) 6
b) 5
c) 2
d) 4

**Key: b**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 1 + 1 = 2; `c` = max(0, 2) + 1 = 3; `d` = 2 + 1 = 3; `e` = 3 + 1 = 4; `f` = max(4, 1) + 1 = 5.

## 3. seed 3154130382935878217, level 1

Each of 2 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P2 sends a message; `b`: P2 has a local step; `c`: P2 has a local step; `d`: P1 sends a message; `e`: P1 sends a message; `f`: P2 has a local step; `g`: P2 receives the message of `d`. A message carries its sender's clock after the send. What is the timestamp of event `g`?

a) 6
b) 5
c) 4
d) 2

**Key: b**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 1 + 1 = 2; `c` = 2 + 1 = 3; `d` = 0 + 1 = 1; `e` = 1 + 1 = 2; `f` = 3 + 1 = 4; `g` = max(4, 1) + 1 = 5.

## 4. seed 1369951084803007927, level 2

Processes P1 to P2 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P1 sends a message; `b`: P1 has a local step; `c`: P1 has a local step; `d`: P1 sends a message; `e`: P1 has a local step; `f`: P1 has a local step; `g`: P2 receives the message of `d`. Which pair of events is concurrent?

a) `e` and `g`
b) `a` and `c`
c) `c` and `f`
d) `c` and `e`

**Key: a**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[1, 0]`; `b` = `[2, 0]`; `c` = `[3, 0]`; `d` = `[4, 0]`; `e` = `[5, 0]`; `f` = `[6, 0]`; `g` = `[4, 1]`. Neither `[5, 0]` nor `[4, 1]` is at most the other, so `e` and `g` are concurrent.

## 5. seed 2562782893485639203, level 2

Processes P1 to P3 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P2 has a local step; `b`: P2 has a local step; `c`: P2 has a local step; `d`: P3 sends a message; `e`: P1 receives the message of `d`; `f`: P1 sends a message; `g`: P2 sends a message. Which pair of events is concurrent?

a) `b` and `c`
b) `a` and `g`
c) `f` and `g`
d) `d` and `f`

**Key: c**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[0, 1, 0]`; `b` = `[0, 2, 0]`; `c` = `[0, 3, 0]`; `d` = `[0, 0, 1]`; `e` = `[1, 0, 1]`; `f` = `[2, 0, 1]`; `g` = `[0, 4, 0]`. Neither `[2, 0, 1]` nor `[0, 4, 0]` is at most the other, so `f` and `g` are concurrent.

## 6. seed 228813545711031285, level 1

Each of 2 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P2 sends a message; `b`: P2 sends a message; `c`: P1 receives the message of `b`; `d`: P2 has a local step; `e`: P2 has a local step; `f`: P1 sends a message; `g`: P1 receives the message of `a`. A message carries its sender's clock after the send. What is the timestamp of event `c`?

a) 4
b) 1
c) 3
d) 2

**Key: c**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 1 + 1 = 2; `c` = max(0, 2) + 1 = 3.

## 7. seed 1437124835097448752, level 2

Processes P1 to P3 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P1 sends a message; `b`: P3 receives the message of `a`; `c`: P2 sends a message; `d`: P1 receives the message of `c`; `e`: P3 has a local step; `f`: P2 sends a message; `g`: P1 sends a message; `h`: P1 receives the message of `f`. Which pair of events is concurrent?

a) `a` and `f`
b) `f` and `h`
c) `c` and `f`
d) `a` and `b`

**Key: a**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[1, 0, 0]`; `b` = `[1, 0, 1]`; `c` = `[0, 1, 0]`; `d` = `[2, 1, 0]`; `e` = `[1, 0, 2]`; `f` = `[0, 2, 0]`; `g` = `[3, 1, 0]`; `h` = `[4, 2, 0]`. Neither `[1, 0, 0]` nor `[0, 2, 0]` is at most the other, so `a` and `f` are concurrent.

## 8. seed 1620637714986146925, level 2

Processes P1 to P2 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P1 sends a message; `b`: P1 has a local step; `c`: P1 sends a message; `d`: P1 sends a message; `e`: P2 receives the message of `c`; `f`: P1 sends a message; `g`: P1 sends a message. Which pair of events is concurrent?

a) `e` and `g`
b) `a` and `d`
c) `c` and `g`
d) `c` and `d`

**Key: a**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[1, 0]`; `b` = `[2, 0]`; `c` = `[3, 0]`; `d` = `[4, 0]`; `e` = `[3, 1]`; `f` = `[5, 0]`; `g` = `[6, 0]`. Neither `[3, 1]` nor `[6, 0]` is at most the other, so `e` and `g` are concurrent.

## 9. seed 2992865735222333956, level 2

Processes P1 to P3 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P3 has a local step; `b`: P1 has a local step; `c`: P1 sends a message; `d`: P3 has a local step; `e`: P1 has a local step; `f`: P3 receives the message of `c`. Which pair of events is concurrent?

a) `b` and `e`
b) `a` and `f`
c) `c` and `e`
d) `a` and `c`

**Key: d**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[0, 0, 1]`; `b` = `[1, 0, 0]`; `c` = `[2, 0, 0]`; `d` = `[0, 0, 2]`; `e` = `[3, 0, 0]`; `f` = `[2, 0, 3]`. Neither `[0, 0, 1]` nor `[2, 0, 0]` is at most the other, so `a` and `c` are concurrent.

## 10. seed 2367025713182835022, level 2

Processes P1 to P2 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P2 sends a message; `b`: P1 receives the message of `a`; `c`: P2 sends a message; `d`: P2 sends a message; `e`: P1 sends a message; `f`: P2 receives the message of `e`; `g`: P1 receives the message of `d`; `h`: P2 has a local step. Which pair of events is concurrent?

a) `d` and `h`
b) `b` and `h`
c) `c` and `d`
d) `g` and `h`

**Key: d**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[0, 1]`; `b` = `[1, 1]`; `c` = `[0, 2]`; `d` = `[0, 3]`; `e` = `[2, 1]`; `f` = `[2, 4]`; `g` = `[3, 3]`; `h` = `[2, 5]`. Neither `[3, 3]` nor `[2, 5]` is at most the other, so `g` and `h` are concurrent.

## 11. seed 2258122072193123831, level 2

Each of 2 processes keeps a vector clock, all starting at `[0, 0]`. Every local step, send and receive is an event, delivered in this global order: `a`: P1 sends a message; `b`: P1 sends a message; `c`: P2 receives the message of `a`; `d`: P1 sends a message; `e`: P1 sends a message; `f`: P1 has a local step; `g`: P2 receives the message of `d`; `h`: P2 receives the message of `e`. A message carries its sender's vector after the send. What is the vector of event `g`?

a) `[4, 2]`
b) `[3, 0]`
c) `[3, 1]`
d) `[3, 2]`

**Key: d**

Explanation: A receive takes the component-wise maximum of its own vector and the message's, then adds 1 to its own component; any other event only adds 1. `a` = `[1, 0]`; `b` = `[2, 0]`; `c` = `[1, 1]`; `d` = `[3, 0]`; `e` = `[4, 0]`; `f` = `[5, 0]`; `g` = `[3, 2]`.

## 12. seed 2229136935548895461, level 1

Each of 2 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P1 has a local step; `b`: P1 sends a message; `c`: P2 has a local step; `d`: P1 sends a message; `e`: P2 receives the message of `d`; `f`: P1 sends a message. A message carries its sender's clock after the send. What is the timestamp of event `e`?

a) 2
b) 5
c) 3
d) 4

**Key: d**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 1 + 1 = 2; `c` = 0 + 1 = 1; `d` = 2 + 1 = 3; `e` = max(1, 3) + 1 = 4.

## 13. seed 4159916488133572768, level 2

Processes P1 to P3 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P3 has a local step; `b`: P3 has a local step; `c`: P3 sends a message; `d`: P3 has a local step; `e`: P2 receives the message of `c`; `f`: P2 has a local step; `g`: P3 has a local step. Which pair of events is concurrent?

a) `c` and `e`
b) `a` and `f`
c) `c` and `f`
d) `d` and `f`

**Key: d**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[0, 0, 1]`; `b` = `[0, 0, 2]`; `c` = `[0, 0, 3]`; `d` = `[0, 0, 4]`; `e` = `[0, 1, 3]`; `f` = `[0, 2, 3]`; `g` = `[0, 0, 5]`. Neither `[0, 0, 4]` nor `[0, 2, 3]` is at most the other, so `d` and `f` are concurrent.

## 14. seed 2457105682908410930, level 1

Each of 2 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P1 sends a message; `b`: P2 sends a message; `c`: P2 sends a message; `d`: P1 receives the message of `c`; `e`: P1 sends a message; `f`: P2 sends a message; `g`: P2 receives the message of `e`. A message carries its sender's clock after the send. What is the timestamp of event `d`?

a) 2
b) 3
c) 4
d) 1

**Key: b**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 0 + 1 = 1; `c` = 1 + 1 = 2; `d` = max(1, 2) + 1 = 3.

## 15. seed 1199934559140114874, level 2

Processes P1 to P3 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P1 sends a message; `b`: P3 receives the message of `a`; `c`: P2 sends a message; `d`: P2 sends a message; `e`: P1 sends a message; `f`: P1 receives the message of `d`; `g`: P3 sends a message. Which pair of events is concurrent?

a) `b` and `g`
b) `b` and `e`
c) `c` and `f`
d) `d` and `f`

**Key: b**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[1, 0, 0]`; `b` = `[1, 0, 1]`; `c` = `[0, 1, 0]`; `d` = `[0, 2, 0]`; `e` = `[2, 0, 0]`; `f` = `[3, 2, 0]`; `g` = `[1, 0, 2]`. Neither `[1, 0, 1]` nor `[2, 0, 0]` is at most the other, so `b` and `e` are concurrent.

## 16. seed 925683804492920300, level 1

Each of 2 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P1 sends a message; `b`: P1 sends a message; `c`: P2 receives the message of `a`; `d`: P2 has a local step; `e`: P1 sends a message; `f`: P2 receives the message of `b`; `g`: P2 receives the message of `e`. A message carries its sender's clock after the send. What is the timestamp of event `f`?

a) 4
b) 3
c) 5
d) 2

**Key: a**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 1 + 1 = 2; `c` = max(0, 1) + 1 = 2; `d` = 2 + 1 = 3; `e` = 2 + 1 = 3; `f` = max(3, 2) + 1 = 4.

## 17. seed 4442188438329156652, level 2

Processes P1 to P2 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P2 sends a message; `b`: P2 sends a message; `c`: P1 has a local step; `d`: P2 sends a message; `e`: P1 has a local step; `f`: P1 sends a message; `g`: P1 has a local step; `h`: P2 receives the message of `f`. Which pair of events is concurrent?

a) `a` and `g`
b) `e` and `f`
c) `e` and `h`
d) `b` and `d`

**Key: a**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[0, 1]`; `b` = `[0, 2]`; `c` = `[1, 0]`; `d` = `[0, 3]`; `e` = `[2, 0]`; `f` = `[3, 0]`; `g` = `[4, 0]`; `h` = `[3, 4]`. Neither `[0, 1]` nor `[4, 0]` is at most the other, so `a` and `g` are concurrent.

## 18. seed 1988483710660842072, level 2

Processes P1 to P3 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P1 sends a message; `b`: P2 has a local step; `c`: P2 has a local step; `d`: P2 receives the message of `a`; `e`: P3 has a local step; `f`: P3 has a local step; `g`: P1 sends a message. Which pair of events is concurrent?

a) `a` and `g`
b) `a` and `f`
c) `b` and `c`
d) `a` and `d`

**Key: b**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[1, 0, 0]`; `b` = `[0, 1, 0]`; `c` = `[0, 2, 0]`; `d` = `[1, 3, 0]`; `e` = `[0, 0, 1]`; `f` = `[0, 0, 2]`; `g` = `[2, 0, 0]`. Neither `[1, 0, 0]` nor `[0, 0, 2]` is at most the other, so `a` and `f` are concurrent.

## 19. seed 1542031567187795292, level 2

Each of 2 processes keeps a vector clock, all starting at `[0, 0]`. Every local step, send and receive is an event, delivered in this global order: `a`: P2 sends a message; `b`: P2 sends a message; `c`: P1 receives the message of `a`; `d`: P2 has a local step; `e`: P1 receives the message of `b`; `f`: P1 has a local step; `g`: P1 sends a message; `h`: P2 receives the message of `g`. A message carries its sender's vector after the send. What is the vector of event `e`?

a) `[0, 2]`
b) `[2, 3]`
c) `[2, 2]`
d) `[1, 2]`

**Key: c**

Explanation: A receive takes the component-wise maximum of its own vector and the message's, then adds 1 to its own component; any other event only adds 1. `a` = `[0, 1]`; `b` = `[0, 2]`; `c` = `[1, 1]`; `d` = `[0, 3]`; `e` = `[2, 2]`.

## 20. seed 3546772883232683625, level 1

Each of 2 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P1 sends a message; `b`: P2 sends a message; `c`: P2 sends a message; `d`: P2 sends a message; `e`: P2 sends a message; `f`: P2 receives the message of `a`. A message carries its sender's clock after the send. What is the timestamp of event `f`?

a) 5
b) 1
c) 6
d) 2

**Key: a**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 0 + 1 = 1; `c` = 1 + 1 = 2; `d` = 2 + 1 = 3; `e` = 3 + 1 = 4; `f` = max(4, 1) + 1 = 5.

## 21. seed 1221011233421693538, level 1

Each of 3 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P3 sends a message; `b`: P3 sends a message; `c`: P3 sends a message; `d`: P2 has a local step; `e`: P2 receives the message of `b`; `f`: P2 receives the message of `a`; `g`: P3 sends a message. A message carries its sender's clock after the send. What is the timestamp of event `f`?

a) 2
b) 4
c) 3
d) 5

**Key: b**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 1 + 1 = 2; `c` = 2 + 1 = 3; `d` = 0 + 1 = 1; `e` = max(1, 2) + 1 = 3; `f` = max(3, 1) + 1 = 4.

## 22. seed 4374258824397843227, level 1

Each of 2 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P1 sends a message; `b`: P1 sends a message; `c`: P1 sends a message; `d`: P1 has a local step; `e`: P2 receives the message of `c`; `f`: P1 has a local step; `g`: P1 has a local step; `h`: P2 receives the message of `a`. A message carries its sender's clock after the send. What is the timestamp of event `e`?

a) 5
b) 1
c) 3
d) 4

**Key: d**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 1 + 1 = 2; `c` = 2 + 1 = 3; `d` = 3 + 1 = 4; `e` = max(0, 3) + 1 = 4.

## 23. seed 1379695165940651543, level 2

Processes P1 to P3 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P1 sends a message; `b`: P2 receives the message of `a`; `c`: P1 has a local step; `d`: P1 sends a message; `e`: P1 sends a message; `f`: P1 has a local step; `g`: P2 receives the message of `e`. Which pair of events is concurrent?

a) `b` and `e`
b) `e` and `f`
c) `a` and `f`
d) `d` and `e`

**Key: a**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[1, 0, 0]`; `b` = `[1, 1, 0]`; `c` = `[2, 0, 0]`; `d` = `[3, 0, 0]`; `e` = `[4, 0, 0]`; `f` = `[5, 0, 0]`; `g` = `[4, 2, 0]`. Neither `[1, 1, 0]` nor `[4, 0, 0]` is at most the other, so `b` and `e` are concurrent.

## 24. seed 3701382724651389512, level 2

Processes P1 to P2 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P2 has a local step; `b`: P1 sends a message; `c`: P1 has a local step; `d`: P1 has a local step; `e`: P2 receives the message of `b`; `f`: P1 sends a message; `g`: P1 sends a message. Which pair of events is concurrent?

a) `d` and `f`
b) `b` and `d`
c) `a` and `e`
d) `d` and `e`

**Key: d**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[0, 1]`; `b` = `[1, 0]`; `c` = `[2, 0]`; `d` = `[3, 0]`; `e` = `[1, 2]`; `f` = `[4, 0]`; `g` = `[5, 0]`. Neither `[3, 0]` nor `[1, 2]` is at most the other, so `d` and `e` are concurrent.

## 25. seed 1580383192197333928, level 1

Each of 3 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P3 sends a message; `b`: P1 has a local step; `c`: P1 receives the message of `a`; `d`: P1 has a local step; `e`: P2 sends a message; `f`: P1 receives the message of `e`; `g`: P2 has a local step. A message carries its sender's clock after the send. What is the timestamp of event `f`?

a) 5
b) 4
c) 2
d) 3

**Key: b**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 0 + 1 = 1; `c` = max(1, 1) + 1 = 2; `d` = 2 + 1 = 3; `e` = 0 + 1 = 1; `f` = max(3, 1) + 1 = 4.

## 26. seed 3923657110712397036, level 2

Processes P1 to P3 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P2 has a local step; `b`: P3 sends a message; `c`: P3 sends a message; `d`: P2 has a local step; `e`: P3 has a local step; `f`: P1 receives the message of `b`. Which pair of events is concurrent?

a) `a` and `c`
b) `b` and `f`
c) `a` and `d`
d) `c` and `e`

**Key: a**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[0, 1, 0]`; `b` = `[0, 0, 1]`; `c` = `[0, 0, 2]`; `d` = `[0, 2, 0]`; `e` = `[0, 0, 3]`; `f` = `[1, 0, 1]`. Neither `[0, 1, 0]` nor `[0, 0, 2]` is at most the other, so `a` and `c` are concurrent.

## 27. seed 3675950756161833450, level 2

Processes P1 to P2 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P2 has a local step; `b`: P1 sends a message; `c`: P1 has a local step; `d`: P2 receives the message of `b`; `e`: P1 has a local step; `f`: P2 has a local step; `g`: P2 sends a message. Which pair of events is concurrent?

a) `b` and `c`
b) `a` and `d`
c) `b` and `e`
d) `c` and `f`

**Key: d**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[0, 1]`; `b` = `[1, 0]`; `c` = `[2, 0]`; `d` = `[1, 2]`; `e` = `[3, 0]`; `f` = `[1, 3]`; `g` = `[1, 4]`. Neither `[2, 0]` nor `[1, 3]` is at most the other, so `c` and `f` are concurrent.

## 28. seed 308964515207237234, level 1

Each of 2 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P2 has a local step; `b`: P2 sends a message; `c`: P2 sends a message; `d`: P2 has a local step; `e`: P1 sends a message; `f`: P1 receives the message of `c`; `g`: P1 receives the message of `b`; `h`: P1 sends a message. A message carries its sender's clock after the send. What is the timestamp of event `g`?

a) 5
b) 3
c) 6
d) 4

**Key: a**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 1 + 1 = 2; `c` = 2 + 1 = 3; `d` = 3 + 1 = 4; `e` = 0 + 1 = 1; `f` = max(1, 3) + 1 = 4; `g` = max(4, 2) + 1 = 5.

## 29. seed 2849482568902294979, level 2

Processes P1 to P3 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P1 sends a message; `b`: P3 receives the message of `a`; `c`: P1 sends a message; `d`: P1 has a local step; `e`: P2 receives the message of `c`; `f`: P2 has a local step; `g`: P3 has a local step. Which pair of events is concurrent?

a) `c` and `f`
b) `e` and `g`
c) `c` and `e`
d) `e` and `f`

**Key: b**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[1, 0, 0]`; `b` = `[1, 0, 1]`; `c` = `[2, 0, 0]`; `d` = `[3, 0, 0]`; `e` = `[2, 1, 0]`; `f` = `[2, 2, 0]`; `g` = `[1, 0, 2]`. Neither `[2, 1, 0]` nor `[1, 0, 2]` is at most the other, so `e` and `g` are concurrent.

## 30. seed 3871178596463619919, level 2

Processes P1 to P3 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P3 sends a message; `b`: P1 sends a message; `c`: P1 receives the message of `a`; `d`: P3 has a local step; `e`: P2 receives the message of `b`; `f`: P1 sends a message; `g`: P2 receives the message of `f`. Which pair of events is concurrent?

a) `a` and `d`
b) `d` and `e`
c) `b` and `f`
d) `b` and `c`

**Key: b**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[0, 0, 1]`; `b` = `[1, 0, 0]`; `c` = `[2, 0, 1]`; `d` = `[0, 0, 2]`; `e` = `[1, 1, 0]`; `f` = `[3, 0, 1]`; `g` = `[3, 2, 1]`. Neither `[0, 0, 2]` nor `[1, 1, 0]` is at most the other, so `d` and `e` are concurrent.

## 31. seed 973081206218401077, level 2

Processes P1 to P3 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P3 sends a message; `b`: P2 receives the message of `a`; `c`: P3 has a local step; `d`: P1 sends a message; `e`: P3 sends a message; `f`: P2 receives the message of `d`. Which pair of events is concurrent?

a) `c` and `e`
b) `d` and `e`
c) `a` and `f`
d) `b` and `f`

**Key: b**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[0, 0, 1]`; `b` = `[0, 1, 1]`; `c` = `[0, 0, 2]`; `d` = `[1, 0, 0]`; `e` = `[0, 0, 3]`; `f` = `[1, 2, 1]`. Neither `[1, 0, 0]` nor `[0, 0, 3]` is at most the other, so `d` and `e` are concurrent.

## 32. seed 1074235662804545495, level 2

Processes P1 to P3 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P2 has a local step; `b`: P1 has a local step; `c`: P2 sends a message; `d`: P3 has a local step; `e`: P1 receives the message of `c`; `f`: P2 sends a message. Which pair of events is concurrent?

a) `b` and `e`
b) `a` and `e`
c) `c` and `f`
d) `b` and `f`

**Key: d**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[0, 1, 0]`; `b` = `[1, 0, 0]`; `c` = `[0, 2, 0]`; `d` = `[0, 0, 1]`; `e` = `[2, 2, 0]`; `f` = `[0, 3, 0]`. Neither `[1, 0, 0]` nor `[0, 3, 0]` is at most the other, so `b` and `f` are concurrent.

## 33. seed 2568215656304681260, level 2

Processes P1 to P2 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P2 sends a message; `b`: P1 has a local step; `c`: P2 sends a message; `d`: P2 has a local step; `e`: P1 has a local step; `f`: P1 receives the message of `a`; `g`: P2 has a local step; `h`: P1 receives the message of `c`. Which pair of events is concurrent?

a) `b` and `f`
b) `f` and `h`
c) `b` and `d`
d) `a` and `h`

**Key: c**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[0, 1]`; `b` = `[1, 0]`; `c` = `[0, 2]`; `d` = `[0, 3]`; `e` = `[2, 0]`; `f` = `[3, 1]`; `g` = `[0, 4]`; `h` = `[4, 2]`. Neither `[1, 0]` nor `[0, 3]` is at most the other, so `b` and `d` are concurrent.

## 34. seed 2391048658861733685, level 1

Each of 2 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P1 sends a message; `b`: P1 sends a message; `c`: P2 receives the message of `b`; `d`: P2 sends a message; `e`: P1 receives the message of `d`; `f`: P2 has a local step; `g`: P1 sends a message; `h`: P1 sends a message. A message carries its sender's clock after the send. What is the timestamp of event `e`?

a) 4
b) 5
c) 3
d) 2

**Key: b**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 1 + 1 = 2; `c` = max(0, 2) + 1 = 3; `d` = 3 + 1 = 4; `e` = max(2, 4) + 1 = 5.

## 35. seed 1837325540670997255, level 1

Each of 2 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P1 has a local step; `b`: P2 sends a message; `c`: P2 has a local step; `d`: P2 sends a message; `e`: P2 has a local step; `f`: P1 receives the message of `d`. A message carries its sender's clock after the send. What is the timestamp of event `f`?

a) 4
b) 2
c) 3
d) 5

**Key: a**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 0 + 1 = 1; `c` = 1 + 1 = 2; `d` = 2 + 1 = 3; `e` = 3 + 1 = 4; `f` = max(1, 3) + 1 = 4.

## 36. seed 2637251230752877397, level 2

Processes P1 to P2 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P1 has a local step; `b`: P1 sends a message; `c`: P1 has a local step; `d`: P2 sends a message; `e`: P1 receives the message of `d`; `f`: P1 sends a message. Which pair of events is concurrent?

a) `b` and `e`
b) `c` and `d`
c) `a` and `e`
d) `c` and `e`

**Key: b**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[1, 0]`; `b` = `[2, 0]`; `c` = `[3, 0]`; `d` = `[0, 1]`; `e` = `[4, 1]`; `f` = `[5, 1]`. Neither `[3, 0]` nor `[0, 1]` is at most the other, so `c` and `d` are concurrent.

## 37. seed 4106100947159252965, level 1

Each of 3 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P1 has a local step; `b`: P2 has a local step; `c`: P2 has a local step; `d`: P2 sends a message; `e`: P3 sends a message; `f`: P3 receives the message of `d`; `g`: P2 receives the message of `e`; `h`: P2 sends a message. A message carries its sender's clock after the send. What is the timestamp of event `g`?

a) 5
b) 4
c) 3
d) 2

**Key: b**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 0 + 1 = 1; `c` = 1 + 1 = 2; `d` = 2 + 1 = 3; `e` = 0 + 1 = 1; `f` = max(1, 3) + 1 = 4; `g` = max(3, 1) + 1 = 4.

## 38. seed 3820829004266953928, level 1

Each of 2 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P2 has a local step; `b`: P1 has a local step; `c`: P2 has a local step; `d`: P2 sends a message; `e`: P2 has a local step; `f`: P2 sends a message; `g`: P1 receives the message of `f`; `h`: P1 receives the message of `d`. A message carries its sender's clock after the send. What is the timestamp of event `h`?

a) 5
b) 7
c) 6
d) 8

**Key: b**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 0 + 1 = 1; `c` = 1 + 1 = 2; `d` = 2 + 1 = 3; `e` = 3 + 1 = 4; `f` = 4 + 1 = 5; `g` = max(1, 5) + 1 = 6; `h` = max(6, 3) + 1 = 7.

## 39. seed 2325340973635646296, level 1

Each of 3 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P2 sends a message; `b`: P2 sends a message; `c`: P1 sends a message; `d`: P1 receives the message of `a`; `e`: P2 sends a message; `f`: P2 receives the message of `c`; `g`: P3 receives the message of `b`; `h`: P3 sends a message. A message carries its sender's clock after the send. What is the timestamp of event `f`?

a) 5
b) 1
c) 4
d) 3

**Key: c**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 1 + 1 = 2; `c` = 0 + 1 = 1; `d` = max(1, 1) + 1 = 2; `e` = 2 + 1 = 3; `f` = max(3, 1) + 1 = 4.

## 40. seed 4295587852021129890, level 2

Processes P1 to P2 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P2 sends a message; `b`: P2 has a local step; `c`: P2 has a local step; `d`: P2 sends a message; `e`: P1 sends a message; `f`: P1 sends a message; `g`: P1 receives the message of `d`; `h`: P2 receives the message of `e`. Which pair of events is concurrent?

a) `a` and `d`
b) `e` and `f`
c) `a` and `c`
d) `f` and `h`

**Key: d**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[0, 1]`; `b` = `[0, 2]`; `c` = `[0, 3]`; `d` = `[0, 4]`; `e` = `[1, 0]`; `f` = `[2, 0]`; `g` = `[3, 4]`; `h` = `[1, 5]`. Neither `[2, 0]` nor `[1, 5]` is at most the other, so `f` and `h` are concurrent.

## 41. seed 2073472949311653579, level 2

Processes P1 to P3 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P1 has a local step; `b`: P3 has a local step; `c`: P1 sends a message; `d`: P2 receives the message of `c`; `e`: P2 has a local step; `f`: P3 has a local step; `g`: P3 sends a message. Which pair of events is concurrent?

a) `a` and `e`
b) `b` and `g`
c) `a` and `d`
d) `b` and `e`

**Key: d**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[1, 0, 0]`; `b` = `[0, 0, 1]`; `c` = `[2, 0, 0]`; `d` = `[2, 1, 0]`; `e` = `[2, 2, 0]`; `f` = `[0, 0, 2]`; `g` = `[0, 0, 3]`. Neither `[0, 0, 1]` nor `[2, 2, 0]` is at most the other, so `b` and `e` are concurrent.

## 42. seed 3037426534747815092, level 1

Each of 3 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P3 sends a message; `b`: P3 sends a message; `c`: P2 receives the message of `b`; `d`: P2 receives the message of `a`; `e`: P2 has a local step; `f`: P2 sends a message; `g`: P3 sends a message; `h`: P1 sends a message. A message carries its sender's clock after the send. What is the timestamp of event `d`?

a) 5
b) 4
c) 2
d) 3

**Key: b**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 1 + 1 = 2; `c` = max(0, 2) + 1 = 3; `d` = max(3, 1) + 1 = 4.

## 43. seed 3490020452411977781, level 2

Processes P1 to P2 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P2 sends a message; `b`: P2 has a local step; `c`: P1 receives the message of `a`; `d`: P2 sends a message; `e`: P2 sends a message; `f`: P1 receives the message of `d`; `g`: P2 sends a message; `h`: P1 has a local step. Which pair of events is concurrent?

a) `c` and `e`
b) `b` and `h`
c) `f` and `h`
d) `b` and `g`

**Key: a**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[0, 1]`; `b` = `[0, 2]`; `c` = `[1, 1]`; `d` = `[0, 3]`; `e` = `[0, 4]`; `f` = `[2, 3]`; `g` = `[0, 5]`; `h` = `[3, 3]`. Neither `[1, 1]` nor `[0, 4]` is at most the other, so `c` and `e` are concurrent.

## 44. seed 4056773433720250421, level 1

Each of 3 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P2 sends a message; `b`: P1 receives the message of `a`; `c`: P3 sends a message; `d`: P3 has a local step; `e`: P1 sends a message; `f`: P1 has a local step; `g`: P1 receives the message of `c`; `h`: P2 has a local step. A message carries its sender's clock after the send. What is the timestamp of event `g`?

a) 2
b) 4
c) 5
d) 3

**Key: c**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = max(0, 1) + 1 = 2; `c` = 0 + 1 = 1; `d` = 1 + 1 = 2; `e` = 2 + 1 = 3; `f` = 3 + 1 = 4; `g` = max(4, 1) + 1 = 5.

## 45. seed 4020011312402961656, level 2

Processes P1 to P2 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P2 sends a message; `b`: P1 receives the message of `a`; `c`: P2 has a local step; `d`: P2 sends a message; `e`: P2 sends a message; `f`: P1 sends a message; `g`: P2 has a local step. Which pair of events is concurrent?

a) `a` and `b`
b) `f` and `g`
c) `a` and `d`
d) `d` and `g`

**Key: b**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[0, 1]`; `b` = `[1, 1]`; `c` = `[0, 2]`; `d` = `[0, 3]`; `e` = `[0, 4]`; `f` = `[2, 1]`; `g` = `[0, 5]`. Neither `[2, 1]` nor `[0, 5]` is at most the other, so `f` and `g` are concurrent.

## 46. seed 1354192302733914801, level 1

Each of 3 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P1 sends a message; `b`: P3 sends a message; `c`: P1 sends a message; `d`: P1 has a local step; `e`: P3 receives the message of `a`; `f`: P3 sends a message; `g`: P2 receives the message of `f`. A message carries its sender's clock after the send. What is the timestamp of event `g`?

a) 3
b) 5
c) 4
d) 2

**Key: c**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 0 + 1 = 1; `c` = 1 + 1 = 2; `d` = 2 + 1 = 3; `e` = max(1, 1) + 1 = 2; `f` = 2 + 1 = 3; `g` = max(0, 3) + 1 = 4.

## 47. seed 1117607002529906061, level 2

Processes P1 to P2 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P2 sends a message; `b`: P1 receives the message of `a`; `c`: P2 sends a message; `d`: P1 receives the message of `c`; `e`: P1 has a local step; `f`: P1 has a local step; `g`: P1 has a local step. Which pair of events is concurrent?

a) `e` and `f`
b) `c` and `f`
c) `a` and `c`
d) `b` and `c`

**Key: d**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[0, 1]`; `b` = `[1, 1]`; `c` = `[0, 2]`; `d` = `[2, 2]`; `e` = `[3, 2]`; `f` = `[4, 2]`; `g` = `[5, 2]`. Neither `[1, 1]` nor `[0, 2]` is at most the other, so `b` and `c` are concurrent.

## 48. seed 393338815364729653, level 2

Processes P1 to P3 keep vector clocks, and every local step, send and receive is an event, delivered in this global order: `a`: P1 has a local step; `b`: P1 sends a message; `c`: P2 sends a message; `d`: P1 receives the message of `c`; `e`: P1 sends a message; `f`: P1 has a local step; `g`: P3 receives the message of `b`; `h`: P3 has a local step. Which pair of events is concurrent?

a) `c` and `h`
b) `b` and `e`
c) `b` and `d`
d) `g` and `h`

**Key: a**

Explanation: Event x happened before y when x's vector is at most y's in every component and the vectors differ; otherwise they are concurrent. Vectors: `a` = `[1, 0, 0]`; `b` = `[2, 0, 0]`; `c` = `[0, 1, 0]`; `d` = `[3, 1, 0]`; `e` = `[4, 1, 0]`; `f` = `[5, 1, 0]`; `g` = `[2, 0, 1]`; `h` = `[2, 0, 2]`. Neither `[0, 1, 0]` nor `[2, 0, 2]` is at most the other, so `c` and `h` are concurrent.

## 49. seed 4595972732461157225, level 1

Each of 3 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P2 has a local step; `b`: P2 sends a message; `c`: P2 sends a message; `d`: P2 has a local step; `e`: P3 receives the message of `c`; `f`: P2 sends a message. A message carries its sender's clock after the send. What is the timestamp of event `e`?

a) 3
b) 4
c) 5
d) 2

**Key: b**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 1 + 1 = 2; `c` = 2 + 1 = 3; `d` = 3 + 1 = 4; `e` = max(0, 3) + 1 = 4.

## 50. seed 1157047090084894412, level 1

Each of 2 processes keeps a Lamport clock, all starting at 0. Every local step, send and receive is an event, delivered in this global order: `a`: P2 sends a message; `b`: P1 sends a message; `c`: P2 has a local step; `d`: P2 has a local step; `e`: P2 has a local step; `f`: P2 receives the message of `b`. A message carries its sender's clock after the send. What is the timestamp of event `f`?

a) 2
b) 5
c) 4
d) 6

**Key: b**

Explanation: A local step or a send adds 1; a receive takes the larger of its own clock and the message's, then adds 1. `a` = 0 + 1 = 1; `b` = 0 + 1 = 1; `c` = 1 + 1 = 2; `d` = 2 + 1 = 3; `e` = 3 + 1 = 4; `f` = max(4, 1) + 1 = 5.
