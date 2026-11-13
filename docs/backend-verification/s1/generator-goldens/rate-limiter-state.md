# Rate limiter state (`rate-limiter-state`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 3512214502419407771, level 1

A token bucket holds at most 2 tokens, starts full and gains 2 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 0, 2, 3, 3, 3, 3, 4. Which requests are rejected?

a) none
b) requests #5, #6
c) request #1
d) request #6

**Key: b**

Explanation: Tokens before each request, capped at the capacity: #1 at 0: 2 tokens, accepted; #2 at 2: 2 tokens, accepted; #3 at 3: 2 tokens, accepted; #4 at 3: 1 token, accepted; #5 at 3: 0 tokens, rejected; #6 at 3: 0 tokens, rejected; #7 at 4: 2 tokens, accepted.

## 2. seed 978331897767095530, level 1

A token bucket holds at most 3 tokens, starts full and gains 1 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 2, 2, 2, 2, 5, 7, 10, 10. Which requests are rejected?

a) none
b) requests #4, #5
c) requests #3, #4
d) request #4

**Key: d**

Explanation: Tokens before each request, capped at the capacity: #1 at 2: 3 tokens, accepted; #2 at 2: 2 tokens, accepted; #3 at 2: 1 token, accepted; #4 at 2: 0 tokens, rejected; #5 at 5: 3 tokens, accepted; #6 at 7: 3 tokens, accepted; #7 at 10: 3 tokens, accepted; #8 at 10: 2 tokens, accepted.

## 3. seed 1113633367339631561, level 2

A sliding-window limiter allows 2 accepted requests per 4 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 4, t]`; rejected requests are not counted. Requests arrive at seconds 0, 2, 3, 3, 3, 4, 4, 6, 8. Which requests are rejected?

a) requests #4, #5, #7
b) requests #3, #4, #5, #7
c) requests #2, #3, #4, #5, #7, #8
d) requests #3, #4, #5, #8

**Key: b**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 0: 0 in the window, accepted; #2 at 2: 1 in the window, accepted; #3 at 3: 2 in the window, rejected; #4 at 3: 2 in the window, rejected; #5 at 3: 2 in the window, rejected; #6 at 4: 1 in the window, accepted; #7 at 4: 2 in the window, rejected; #8 at 6: 1 in the window, accepted; #9 at 8: 1 in the window, accepted.

## 4. seed 2062210441628362098, level 2

A sliding-window limiter allows 3 accepted requests per 4 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 4, t]`; rejected requests are not counted. Requests arrive at seconds 0, 1, 2, 3, 4, 6, 6, 6. Which requests are rejected?

a) request #8
b) requests #3, #4, #7, #8
c) requests #4, #5, #8
d) requests #4, #8

**Key: d**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 0: 0 in the window, accepted; #2 at 1: 1 in the window, accepted; #3 at 2: 2 in the window, accepted; #4 at 3: 3 in the window, rejected; #5 at 4: 2 in the window, accepted; #6 at 6: 1 in the window, accepted; #7 at 6: 2 in the window, accepted; #8 at 6: 3 in the window, rejected.

## 5. seed 4379027967668037132, level 2

A sliding-window limiter allows 3 accepted requests per 5 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 5, t]`; rejected requests are not counted. Requests arrive at seconds 1, 3, 5, 6, 7, 8, 9, 9, 9. Which requests are rejected?

a) requests #5, #7, #8, #9
b) requests #6, #7, #8, #9
c) requests #7, #8, #9
d) requests #4, #6, #8, #9

**Key: a**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 1: 0 in the window, accepted; #2 at 3: 1 in the window, accepted; #3 at 5: 2 in the window, accepted; #4 at 6: 2 in the window, accepted; #5 at 7: 3 in the window, rejected; #6 at 8: 2 in the window, accepted; #7 at 9: 3 in the window, rejected; #8 at 9: 3 in the window, rejected; #9 at 9: 3 in the window, rejected.

## 6. seed 2083203590779911018, level 2

A sliding-window limiter allows 2 accepted requests per 3 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 3, t]`; rejected requests are not counted. Requests arrive at seconds 1, 2, 3, 5, 5, 5, 6, 9, 9. Which requests are rejected?

a) requests #3, #5, #6, #9
b) request #6
c) requests #2, #3, #5, #6, #7, #9
d) requests #3, #6, #7

**Key: d**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 1: 0 in the window, accepted; #2 at 2: 1 in the window, accepted; #3 at 3: 2 in the window, rejected; #4 at 5: 0 in the window, accepted; #5 at 5: 1 in the window, accepted; #6 at 5: 2 in the window, rejected; #7 at 6: 2 in the window, rejected; #8 at 9: 0 in the window, accepted; #9 at 9: 1 in the window, accepted.

## 7. seed 1928311144240751965, level 1

A token bucket holds at most 4 tokens, starts full and gains 1 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 2, 3, 3, 3, 3, 3, 6, 6, 6, 8. Which requests are rejected?

a) requests #4, #5, #6
b) requests #5, #6, #7, #8, #9
c) none
d) request #6

**Key: d**

Explanation: Tokens before each request, capped at the capacity: #1 at 2: 4 tokens, accepted; #2 at 3: 4 tokens, accepted; #3 at 3: 3 tokens, accepted; #4 at 3: 2 tokens, accepted; #5 at 3: 1 token, accepted; #6 at 3: 0 tokens, rejected; #7 at 6: 3 tokens, accepted; #8 at 6: 2 tokens, accepted; #9 at 6: 1 token, accepted; #10 at 8: 2 tokens, accepted.

## 8. seed 2704216001775078860, level 2

A sliding-window limiter allows 4 accepted requests per 4 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 4, t]`; rejected requests are not counted. Requests arrive at seconds 2, 5, 7, 8, 9, 9, 9, 10, 11, 11. Which requests are rejected?

a) requests #6, #7, #9, #10
b) requests #6, #7, #8, #10
c) requests #8, #9, #10
d) requests #7, #8, #10

**Key: d**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 2: 0 in the window, accepted; #2 at 5: 1 in the window, accepted; #3 at 7: 1 in the window, accepted; #4 at 8: 2 in the window, accepted; #5 at 9: 2 in the window, accepted; #6 at 9: 3 in the window, accepted; #7 at 9: 4 in the window, rejected; #8 at 10: 4 in the window, rejected; #9 at 11: 3 in the window, accepted; #10 at 11: 4 in the window, rejected.

## 9. seed 2633117676241410816, level 1

A token bucket holds at most 2 tokens, starts full and gains 1 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 0, 2, 3, 5, 8, 11, 11, 11. Which requests are rejected?

a) request #8
b) request #1
c) none
d) requests #1, #8

**Key: a**

Explanation: Tokens before each request, capped at the capacity: #1 at 0: 2 tokens, accepted; #2 at 2: 2 tokens, accepted; #3 at 3: 2 tokens, accepted; #4 at 5: 2 tokens, accepted; #5 at 8: 2 tokens, accepted; #6 at 11: 2 tokens, accepted; #7 at 11: 1 token, accepted; #8 at 11: 0 tokens, rejected.

## 10. seed 1874894138192170191, level 2

A sliding-window limiter allows 2 accepted requests per 3 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 3, t]`; rejected requests are not counted. Requests arrive at seconds 1, 1, 1, 2, 3, 4, 4. Which requests are rejected?

a) requests #4, #5
b) requests #3, #4, #5, #6, #7
c) requests #3, #4, #5
d) requests #3, #4, #7

**Key: c**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 1: 0 in the window, accepted; #2 at 1: 1 in the window, accepted; #3 at 1: 2 in the window, rejected; #4 at 2: 2 in the window, rejected; #5 at 3: 2 in the window, rejected; #6 at 4: 0 in the window, accepted; #7 at 4: 1 in the window, accepted.

## 11. seed 1873343275279489871, level 1

A token bucket holds at most 3 tokens, starts full and gains 1 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 2, 4, 5, 5, 5, 5, 5, 6, 9, 10. Which requests are rejected?

a) none
b) requests #4, #5, #6, #7
c) request #7
d) requests #6, #7

**Key: d**

Explanation: Tokens before each request, capped at the capacity: #1 at 2: 3 tokens, accepted; #2 at 4: 3 tokens, accepted; #3 at 5: 3 tokens, accepted; #4 at 5: 2 tokens, accepted; #5 at 5: 1 token, accepted; #6 at 5: 0 tokens, rejected; #7 at 5: 0 tokens, rejected; #8 at 6: 1 token, accepted; #9 at 9: 3 tokens, accepted; #10 at 10: 3 tokens, accepted.

## 12. seed 3949548451227115653, level 2

A sliding-window limiter allows 4 accepted requests per 5 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 5, t]`; rejected requests are not counted. Requests arrive at seconds 3, 3, 5, 8, 8, 10, 11, 11, 13, 13. Which requests are rejected?

a) requests #5, #9, #10
b) request #10
c) request #8
d) requests #7, #8

**Key: c**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 3: 0 in the window, accepted; #2 at 3: 1 in the window, accepted; #3 at 5: 2 in the window, accepted; #4 at 8: 1 in the window, accepted; #5 at 8: 2 in the window, accepted; #6 at 10: 2 in the window, accepted; #7 at 11: 3 in the window, accepted; #8 at 11: 4 in the window, rejected; #9 at 13: 2 in the window, accepted; #10 at 13: 3 in the window, accepted.

## 13. seed 3095176794953675629, level 2

A sliding-window limiter allows 3 accepted requests per 4 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 4, t]`; rejected requests are not counted. Requests arrive at seconds 0, 3, 5, 5, 5, 8, 9. Which requests are rejected?

a) requests #5, #7
b) none
c) request #5
d) requests #4, #5

**Key: c**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 0: 0 in the window, accepted; #2 at 3: 1 in the window, accepted; #3 at 5: 1 in the window, accepted; #4 at 5: 2 in the window, accepted; #5 at 5: 3 in the window, rejected; #6 at 8: 2 in the window, accepted; #7 at 9: 1 in the window, accepted.

## 14. seed 1023033896872537326, level 1

A token bucket holds at most 2 tokens, starts full and gains 2 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 1, 1, 1, 1, 2, 2, 4, 4. Which requests are rejected?

a) request #4
b) none
c) requests #3, #4
d) requests #3, #4, #5, #6

**Key: c**

Explanation: Tokens before each request, capped at the capacity: #1 at 1: 2 tokens, accepted; #2 at 1: 1 token, accepted; #3 at 1: 0 tokens, rejected; #4 at 1: 0 tokens, rejected; #5 at 2: 2 tokens, accepted; #6 at 2: 1 token, accepted; #7 at 4: 2 tokens, accepted; #8 at 4: 1 token, accepted.

## 15. seed 3241059604646926336, level 1

A token bucket holds at most 2 tokens, starts full and gains 2 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 0, 3, 4, 5, 6, 9, 9, 9. Which requests are rejected?

a) request #1
b) none
c) request #8
d) requests #1, #8

**Key: c**

Explanation: Tokens before each request, capped at the capacity: #1 at 0: 2 tokens, accepted; #2 at 3: 2 tokens, accepted; #3 at 4: 2 tokens, accepted; #4 at 5: 2 tokens, accepted; #5 at 6: 2 tokens, accepted; #6 at 9: 2 tokens, accepted; #7 at 9: 1 token, accepted; #8 at 9: 0 tokens, rejected.

## 16. seed 2472454843973175823, level 1

A token bucket holds at most 2 tokens, starts full and gains 2 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 0, 0, 2, 4, 4, 4, 7, 8, 8. Which requests are rejected?

a) request #6
b) requests #1, #2, #6
c) requests #6, #9
d) requests #1, #2

**Key: a**

Explanation: Tokens before each request, capped at the capacity: #1 at 0: 2 tokens, accepted; #2 at 0: 1 token, accepted; #3 at 2: 2 tokens, accepted; #4 at 4: 2 tokens, accepted; #5 at 4: 1 token, accepted; #6 at 4: 0 tokens, rejected; #7 at 7: 2 tokens, accepted; #8 at 8: 2 tokens, accepted; #9 at 8: 1 token, accepted.

## 17. seed 2384555009948452733, level 2

A sliding-window limiter allows 3 accepted requests per 5 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 5, t]`; rejected requests are not counted. Requests arrive at seconds 1, 1, 1, 2, 2, 2, 5, 6, 6, 6. Which requests are rejected?

a) requests #4, #5, #6, #7
b) requests #4, #5, #6, #7, #8, #9, #10
c) requests #3, #4, #5, #6, #7, #10
d) requests #4, #5, #6, #10

**Key: a**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 1: 0 in the window, accepted; #2 at 1: 1 in the window, accepted; #3 at 1: 2 in the window, accepted; #4 at 2: 3 in the window, rejected; #5 at 2: 3 in the window, rejected; #6 at 2: 3 in the window, rejected; #7 at 5: 3 in the window, rejected; #8 at 6: 0 in the window, accepted; #9 at 6: 1 in the window, accepted; #10 at 6: 2 in the window, accepted.

## 18. seed 3703496478437029346, level 1

A token bucket holds at most 4 tokens, starts full and gains 2 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 0, 1, 4, 5, 5, 5, 5, 5. Which requests are rejected?

a) request #8
b) request #1
c) requests #7, #8
d) requests #1, #8

**Key: a**

Explanation: Tokens before each request, capped at the capacity: #1 at 0: 4 tokens, accepted; #2 at 1: 4 tokens, accepted; #3 at 4: 4 tokens, accepted; #4 at 5: 4 tokens, accepted; #5 at 5: 3 tokens, accepted; #6 at 5: 2 tokens, accepted; #7 at 5: 1 token, accepted; #8 at 5: 0 tokens, rejected.

## 19. seed 2452809781808576350, level 1

A token bucket holds at most 2 tokens, starts full and gains 2 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 0, 2, 2, 2, 2, 4, 4, 7, 8. Which requests are rejected?

a) requests #4, #5
b) request #5
c) request #1
d) none

**Key: a**

Explanation: Tokens before each request, capped at the capacity: #1 at 0: 2 tokens, accepted; #2 at 2: 2 tokens, accepted; #3 at 2: 1 token, accepted; #4 at 2: 0 tokens, rejected; #5 at 2: 0 tokens, rejected; #6 at 4: 2 tokens, accepted; #7 at 4: 1 token, accepted; #8 at 7: 2 tokens, accepted; #9 at 8: 2 tokens, accepted.

## 20. seed 3458739901720432635, level 2

A sliding-window limiter allows 3 accepted requests per 3 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 3, t]`; rejected requests are not counted. Requests arrive at seconds 0, 3, 5, 5, 5, 7, 8. Which requests are rejected?

a) requests #5, #7
b) request #5
c) requests #4, #5
d) none

**Key: b**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 0: 0 in the window, accepted; #2 at 3: 0 in the window, accepted; #3 at 5: 1 in the window, accepted; #4 at 5: 2 in the window, accepted; #5 at 5: 3 in the window, rejected; #6 at 7: 2 in the window, accepted; #7 at 8: 1 in the window, accepted.

## 21. seed 3441009716897816792, level 1

A token bucket holds at most 2 tokens, starts full and gains 1 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 1, 1, 3, 4, 7, 7, 7, 10. Which requests are rejected?

a) requests #2, #7
b) request #7
c) request #2
d) requests #3, #7

**Key: b**

Explanation: Tokens before each request, capped at the capacity: #1 at 1: 2 tokens, accepted; #2 at 1: 1 token, accepted; #3 at 3: 2 tokens, accepted; #4 at 4: 2 tokens, accepted; #5 at 7: 2 tokens, accepted; #6 at 7: 1 token, accepted; #7 at 7: 0 tokens, rejected; #8 at 10: 2 tokens, accepted.

## 22. seed 1566660887704299817, level 2

A sliding-window limiter allows 4 accepted requests per 5 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 5, t]`; rejected requests are not counted. Requests arrive at seconds 2, 2, 2, 2, 3, 6, 7, 8. Which requests are rejected?

a) request #5
b) requests #5, #6
c) requests #4, #5, #6
d) requests #5, #6, #7

**Key: b**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 2: 0 in the window, accepted; #2 at 2: 1 in the window, accepted; #3 at 2: 2 in the window, accepted; #4 at 2: 3 in the window, accepted; #5 at 3: 4 in the window, rejected; #6 at 6: 4 in the window, rejected; #7 at 7: 0 in the window, accepted; #8 at 8: 1 in the window, accepted.

## 23. seed 3551184810353942629, level 1

A token bucket holds at most 3 tokens, starts full and gains 1 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 0, 1, 1, 1, 1, 1, 2, 2, 5. Which requests are rejected?

a) requests #5, #6, #8
b) requests #4, #5, #6, #7, #8
c) requests #1, #3, #4, #5, #6, #8
d) requests #6, #8

**Key: a**

Explanation: Tokens before each request, capped at the capacity: #1 at 0: 3 tokens, accepted; #2 at 1: 3 tokens, accepted; #3 at 1: 2 tokens, accepted; #4 at 1: 1 token, accepted; #5 at 1: 0 tokens, rejected; #6 at 1: 0 tokens, rejected; #7 at 2: 1 token, accepted; #8 at 2: 0 tokens, rejected; #9 at 5: 3 tokens, accepted.

## 24. seed 742249331793513658, level 2

A sliding-window limiter allows 2 accepted requests per 3 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 3, t]`; rejected requests are not counted. Requests arrive at seconds 2, 2, 2, 5, 8, 9, 11, 12. Which requests are rejected?

a) request #3
b) none
c) requests #3, #4, #7
d) requests #2, #3, #6, #8

**Key: a**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 2: 0 in the window, accepted; #2 at 2: 1 in the window, accepted; #3 at 2: 2 in the window, rejected; #4 at 5: 0 in the window, accepted; #5 at 8: 0 in the window, accepted; #6 at 9: 1 in the window, accepted; #7 at 11: 1 in the window, accepted; #8 at 12: 1 in the window, accepted.

## 25. seed 3692176668993146103, level 2

A sliding-window limiter allows 3 accepted requests per 4 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 4, t]`; rejected requests are not counted. Requests arrive at seconds 2, 3, 4, 4, 5, 5, 6, 7, 7, 7. Which requests are rejected?

a) requests #4, #5, #6, #9, #10
b) requests #4, #5, #6, #7, #9, #10
c) requests #3, #4, #5, #6, #9, #10
d) requests #6, #7, #8, #9, #10

**Key: a**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 2: 0 in the window, accepted; #2 at 3: 1 in the window, accepted; #3 at 4: 2 in the window, accepted; #4 at 4: 3 in the window, rejected; #5 at 5: 3 in the window, rejected; #6 at 5: 3 in the window, rejected; #7 at 6: 2 in the window, accepted; #8 at 7: 2 in the window, accepted; #9 at 7: 3 in the window, rejected; #10 at 7: 3 in the window, rejected.

## 26. seed 4579202048532855462, level 2

A sliding-window limiter allows 3 accepted requests per 3 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 3, t]`; rejected requests are not counted. Requests arrive at seconds 1, 1, 2, 2, 3, 4, 5, 6, 7, 9. Which requests are rejected?

a) requests #3, #4, #5, #8
b) requests #4, #5, #6
c) request #4
d) requests #4, #5

**Key: d**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 1: 0 in the window, accepted; #2 at 1: 1 in the window, accepted; #3 at 2: 2 in the window, accepted; #4 at 2: 3 in the window, rejected; #5 at 3: 3 in the window, rejected; #6 at 4: 1 in the window, accepted; #7 at 5: 1 in the window, accepted; #8 at 6: 2 in the window, accepted; #9 at 7: 2 in the window, accepted; #10 at 9: 1 in the window, accepted.

## 27. seed 3644490302724017937, level 2

A sliding-window limiter allows 2 accepted requests per 5 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 5, t]`; rejected requests are not counted. Requests arrive at seconds 3, 5, 5, 8, 11, 12, 15, 16, 18, 18. Which requests are rejected?

a) requests #4, #9, #10
b) requests #3, #4, #7, #8
c) request #10
d) requests #3, #6, #9, #10

**Key: d**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 3: 0 in the window, accepted; #2 at 5: 1 in the window, accepted; #3 at 5: 2 in the window, rejected; #4 at 8: 1 in the window, accepted; #5 at 11: 1 in the window, accepted; #6 at 12: 2 in the window, rejected; #7 at 15: 1 in the window, accepted; #8 at 16: 1 in the window, accepted; #9 at 18: 2 in the window, rejected; #10 at 18: 2 in the window, rejected.

## 28. seed 4420778814768874009, level 2

A sliding-window limiter allows 2 accepted requests per 3 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 3, t]`; rejected requests are not counted. Requests arrive at seconds 3, 6, 7, 9, 9, 11, 12, 15. Which requests are rejected?

a) request #6
b) requests #3, #5, #6
c) requests #4, #5
d) request #5

**Key: d**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 3: 0 in the window, accepted; #2 at 6: 0 in the window, accepted; #3 at 7: 1 in the window, accepted; #4 at 9: 1 in the window, accepted; #5 at 9: 2 in the window, rejected; #6 at 11: 1 in the window, accepted; #7 at 12: 1 in the window, accepted; #8 at 15: 0 in the window, accepted.

## 29. seed 1807907220113682721, level 2

A sliding-window limiter allows 2 accepted requests per 4 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 4, t]`; rejected requests are not counted. Requests arrive at seconds 1, 4, 5, 7, 8, 8, 8, 9, 11, 12. Which requests are rejected?

a) requests #4, #7, #8, #9
b) requests #3, #5, #6, #7, #9
c) requests #2, #4, #5, #6, #7, #9, #10
d) requests #4, #6, #7, #9

**Key: d**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 1: 0 in the window, accepted; #2 at 4: 1 in the window, accepted; #3 at 5: 1 in the window, accepted; #4 at 7: 2 in the window, rejected; #5 at 8: 1 in the window, accepted; #6 at 8: 2 in the window, rejected; #7 at 8: 2 in the window, rejected; #8 at 9: 1 in the window, accepted; #9 at 11: 2 in the window, rejected; #10 at 12: 1 in the window, accepted.

## 30. seed 2566050308072490042, level 1

A token bucket holds at most 2 tokens, starts full and gains 1 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 1, 1, 1, 4, 4, 5, 6, 6, 6, 9. Which requests are rejected?

a) requests #3, #8, #9
b) request #9
c) requests #3, #6, #7, #8, #9
d) requests #2, #3, #9

**Key: a**

Explanation: Tokens before each request, capped at the capacity: #1 at 1: 2 tokens, accepted; #2 at 1: 1 token, accepted; #3 at 1: 0 tokens, rejected; #4 at 4: 2 tokens, accepted; #5 at 4: 1 token, accepted; #6 at 5: 1 token, accepted; #7 at 6: 1 token, accepted; #8 at 6: 0 tokens, rejected; #9 at 6: 0 tokens, rejected; #10 at 9: 2 tokens, accepted.

## 31. seed 3798451012305610275, level 1

A token bucket holds at most 2 tokens, starts full and gains 1 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 3, 4, 4, 5, 6, 6, 6, 6. Which requests are rejected?

a) requests #3, #4, #6, #7, #8
b) requests #7, #8
c) requests #6, #7, #8
d) none

**Key: c**

Explanation: Tokens before each request, capped at the capacity: #1 at 3: 2 tokens, accepted; #2 at 4: 2 tokens, accepted; #3 at 4: 1 token, accepted; #4 at 5: 1 token, accepted; #5 at 6: 1 token, accepted; #6 at 6: 0 tokens, rejected; #7 at 6: 0 tokens, rejected; #8 at 6: 0 tokens, rejected.

## 32. seed 4401994440001166525, level 1

A token bucket holds at most 2 tokens, starts full and gains 2 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 0, 3, 6, 6, 6, 6, 7, 10, 10. Which requests are rejected?

a) requests #5, #6
b) request #1
c) request #6
d) none

**Key: a**

Explanation: Tokens before each request, capped at the capacity: #1 at 0: 2 tokens, accepted; #2 at 3: 2 tokens, accepted; #3 at 6: 2 tokens, accepted; #4 at 6: 1 token, accepted; #5 at 6: 0 tokens, rejected; #6 at 6: 0 tokens, rejected; #7 at 7: 2 tokens, accepted; #8 at 10: 2 tokens, accepted; #9 at 10: 1 token, accepted.

## 33. seed 988869596868422735, level 1

A token bucket holds at most 3 tokens, starts full and gains 1 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 1, 4, 6, 9, 11, 11, 11, 11, 11, 12. Which requests are rejected?

a) none
b) requests #8, #9
c) request #9
d) requests #7, #8, #9, #10

**Key: b**

Explanation: Tokens before each request, capped at the capacity: #1 at 1: 3 tokens, accepted; #2 at 4: 3 tokens, accepted; #3 at 6: 3 tokens, accepted; #4 at 9: 3 tokens, accepted; #5 at 11: 3 tokens, accepted; #6 at 11: 2 tokens, accepted; #7 at 11: 1 token, accepted; #8 at 11: 0 tokens, rejected; #9 at 11: 0 tokens, rejected; #10 at 12: 1 token, accepted.

## 34. seed 2713739807267392838, level 2

A sliding-window limiter allows 3 accepted requests per 3 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 3, t]`; rejected requests are not counted. Requests arrive at seconds 1, 3, 5, 7, 7, 7, 8. Which requests are rejected?

a) request #6
b) requests #6, #7
c) requests #5, #6
d) request #7

**Key: a**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 1: 0 in the window, accepted; #2 at 3: 1 in the window, accepted; #3 at 5: 1 in the window, accepted; #4 at 7: 1 in the window, accepted; #5 at 7: 2 in the window, accepted; #6 at 7: 3 in the window, rejected; #7 at 8: 2 in the window, accepted.

## 35. seed 4046279421569570675, level 2

A sliding-window limiter allows 2 accepted requests per 5 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 5, t]`; rejected requests are not counted. Requests arrive at seconds 0, 2, 4, 4, 4, 7, 10, 11, 14, 15. Which requests are rejected?

a) requests #3, #4, #5, #9
b) requests #2, #3, #4, #5, #7, #8, #10
c) requests #3, #4, #5, #8
d) requests #3, #4, #5, #8, #10

**Key: c**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 0: 0 in the window, accepted; #2 at 2: 1 in the window, accepted; #3 at 4: 2 in the window, rejected; #4 at 4: 2 in the window, rejected; #5 at 4: 2 in the window, rejected; #6 at 7: 0 in the window, accepted; #7 at 10: 1 in the window, accepted; #8 at 11: 2 in the window, rejected; #9 at 14: 1 in the window, accepted; #10 at 15: 1 in the window, accepted.

## 36. seed 2788684025257509876, level 2

A sliding-window limiter allows 2 accepted requests per 3 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 3, t]`; rejected requests are not counted. Requests arrive at seconds 0, 3, 4, 4, 7, 8, 9, 9, 9. Which requests are rejected?

a) requests #4, #7, #8, #9
b) requests #3, #4, #6, #7, #8, #9
c) requests #4, #9
d) requests #8, #9

**Key: a**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 0: 0 in the window, accepted; #2 at 3: 0 in the window, accepted; #3 at 4: 1 in the window, accepted; #4 at 4: 2 in the window, rejected; #5 at 7: 0 in the window, accepted; #6 at 8: 1 in the window, accepted; #7 at 9: 2 in the window, rejected; #8 at 9: 2 in the window, rejected; #9 at 9: 2 in the window, rejected.

## 37. seed 3096362522107724198, level 2

A sliding-window limiter allows 2 accepted requests per 3 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 3, t]`; rejected requests are not counted. Requests arrive at seconds 1, 2, 4, 5, 6, 7, 9, 10, 11, 11. Which requests are rejected?

a) requests #3, #6, #9, #10
b) requests #5, #9, #10
c) requests #2, #4, #5, #7, #9, #10
d) requests #9, #10

**Key: b**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 1: 0 in the window, accepted; #2 at 2: 1 in the window, accepted; #3 at 4: 1 in the window, accepted; #4 at 5: 1 in the window, accepted; #5 at 6: 2 in the window, rejected; #6 at 7: 1 in the window, accepted; #7 at 9: 1 in the window, accepted; #8 at 10: 1 in the window, accepted; #9 at 11: 2 in the window, rejected; #10 at 11: 2 in the window, rejected.

## 38. seed 38331730833416261, level 2

A sliding-window limiter allows 2 accepted requests per 4 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 4, t]`; rejected requests are not counted. Requests arrive at seconds 0, 2, 2, 2, 4, 4, 5, 6, 7. Which requests are rejected?

a) requests #4, #6, #7
b) requests #3, #4, #7, #8, #9
c) requests #3, #4, #6, #7, #9
d) requests #3, #4, #5, #6, #8

**Key: c**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 0: 0 in the window, accepted; #2 at 2: 1 in the window, accepted; #3 at 2: 2 in the window, rejected; #4 at 2: 2 in the window, rejected; #5 at 4: 1 in the window, accepted; #6 at 4: 2 in the window, rejected; #7 at 5: 2 in the window, rejected; #8 at 6: 1 in the window, accepted; #9 at 7: 2 in the window, rejected.

## 39. seed 3038343489815029164, level 2

A sliding-window limiter allows 2 accepted requests per 4 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 4, t]`; rejected requests are not counted. Requests arrive at seconds 0, 1, 2, 4, 4, 5, 6, 8, 9, 9. Which requests are rejected?

a) requests #2, #3, #5, #6, #7, #9, #10
b) requests #3, #6, #7, #10
c) requests #3, #4, #5, #8, #9, #10
d) requests #3, #5, #7, #10

**Key: d**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 0: 0 in the window, accepted; #2 at 1: 1 in the window, accepted; #3 at 2: 2 in the window, rejected; #4 at 4: 1 in the window, accepted; #5 at 4: 2 in the window, rejected; #6 at 5: 1 in the window, accepted; #7 at 6: 2 in the window, rejected; #8 at 8: 1 in the window, accepted; #9 at 9: 1 in the window, accepted; #10 at 9: 2 in the window, rejected.

## 40. seed 2354290158391715435, level 1

A token bucket holds at most 2 tokens, starts full and gains 1 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 3, 6, 9, 9, 9, 9, 11, 14, 16, 19. Which requests are rejected?

a) requests #5, #6
b) request #6
c) requests #5, #6, #7
d) none

**Key: a**

Explanation: Tokens before each request, capped at the capacity: #1 at 3: 2 tokens, accepted; #2 at 6: 2 tokens, accepted; #3 at 9: 2 tokens, accepted; #4 at 9: 1 token, accepted; #5 at 9: 0 tokens, rejected; #6 at 9: 0 tokens, rejected; #7 at 11: 2 tokens, accepted; #8 at 14: 2 tokens, accepted; #9 at 16: 2 tokens, accepted; #10 at 19: 2 tokens, accepted.

## 41. seed 2169889088607179132, level 2

A sliding-window limiter allows 2 accepted requests per 3 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 3, t]`; rejected requests are not counted. Requests arrive at seconds 1, 2, 4, 6, 8, 8, 10, 10, 10. Which requests are rejected?

a) requests #8, #9
b) requests #3, #6, #8, #9
c) requests #6, #8, #9
d) requests #2, #4, #6, #7, #8, #9

**Key: c**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 1: 0 in the window, accepted; #2 at 2: 1 in the window, accepted; #3 at 4: 1 in the window, accepted; #4 at 6: 1 in the window, accepted; #5 at 8: 1 in the window, accepted; #6 at 8: 2 in the window, rejected; #7 at 10: 1 in the window, accepted; #8 at 10: 2 in the window, rejected; #9 at 10: 2 in the window, rejected.

## 42. seed 845810395247151273, level 1

A token bucket holds at most 2 tokens, starts full and gains 1 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 0, 3, 3, 4, 5, 5, 5, 5, 6. Which requests are rejected?

a) requests #1, #7, #8
b) requests #6, #7, #8
c) requests #4, #5, #6, #7, #8
d) requests #1, #6, #7, #8

**Key: b**

Explanation: Tokens before each request, capped at the capacity: #1 at 0: 2 tokens, accepted; #2 at 3: 2 tokens, accepted; #3 at 3: 1 token, accepted; #4 at 4: 1 token, accepted; #5 at 5: 1 token, accepted; #6 at 5: 0 tokens, rejected; #7 at 5: 0 tokens, rejected; #8 at 5: 0 tokens, rejected; #9 at 6: 1 token, accepted.

## 43. seed 4516048740207053473, level 2

A sliding-window limiter allows 3 accepted requests per 3 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 3, t]`; rejected requests are not counted. Requests arrive at seconds 2, 2, 5, 7, 7, 8, 9, 9, 12, 15. Which requests are rejected?

a) requests #7, #8
b) none
c) requests #6, #8
d) request #8

**Key: a**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 2: 0 in the window, accepted; #2 at 2: 1 in the window, accepted; #3 at 5: 0 in the window, accepted; #4 at 7: 1 in the window, accepted; #5 at 7: 2 in the window, accepted; #6 at 8: 2 in the window, accepted; #7 at 9: 3 in the window, rejected; #8 at 9: 3 in the window, rejected; #9 at 12: 0 in the window, accepted; #10 at 15: 0 in the window, accepted.

## 44. seed 3751988296231940168, level 2

A sliding-window limiter allows 2 accepted requests per 4 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 4, t]`; rejected requests are not counted. Requests arrive at seconds 1, 2, 5, 6, 8, 8, 10, 11, 13. Which requests are rejected?

a) requests #7, #8
b) requests #3, #6, #7
c) requests #5, #6, #9
d) request #6

**Key: c**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 1: 0 in the window, accepted; #2 at 2: 1 in the window, accepted; #3 at 5: 1 in the window, accepted; #4 at 6: 1 in the window, accepted; #5 at 8: 2 in the window, rejected; #6 at 8: 2 in the window, rejected; #7 at 10: 0 in the window, accepted; #8 at 11: 1 in the window, accepted; #9 at 13: 2 in the window, rejected.

## 45. seed 4365796487252414579, level 2

A sliding-window limiter allows 3 accepted requests per 3 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 3, t]`; rejected requests are not counted. Requests arrive at seconds 0, 1, 4, 6, 8, 10, 10, 10, 11, 12. Which requests are rejected?

a) request #10
b) request #9
c) requests #8, #9
d) requests #8, #10

**Key: d**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 0: 0 in the window, accepted; #2 at 1: 1 in the window, accepted; #3 at 4: 0 in the window, accepted; #4 at 6: 1 in the window, accepted; #5 at 8: 1 in the window, accepted; #6 at 10: 1 in the window, accepted; #7 at 10: 2 in the window, accepted; #8 at 10: 3 in the window, rejected; #9 at 11: 2 in the window, accepted; #10 at 12: 3 in the window, rejected.

## 46. seed 3469861651942835725, level 1

A token bucket holds at most 4 tokens, starts full and gains 1 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 1, 1, 4, 7, 7, 8, 8, 8, 8, 10. Which requests are rejected?

a) request #2
b) requests #7, #8, #9
c) request #9
d) requests #2, #9

**Key: c**

Explanation: Tokens before each request, capped at the capacity: #1 at 1: 4 tokens, accepted; #2 at 1: 3 tokens, accepted; #3 at 4: 4 tokens, accepted; #4 at 7: 4 tokens, accepted; #5 at 7: 3 tokens, accepted; #6 at 8: 3 tokens, accepted; #7 at 8: 2 tokens, accepted; #8 at 8: 1 token, accepted; #9 at 8: 0 tokens, rejected; #10 at 10: 2 tokens, accepted.

## 47. seed 3519250524388961657, level 1

A token bucket holds at most 3 tokens, starts full and gains 1 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 1, 1, 2, 2, 3, 4, 4, 5, 5, 8. Which requests are rejected?

a) request #9
b) requests #4, #5, #6, #7
c) requests #2, #4, #7, #9
d) requests #7, #9

**Key: d**

Explanation: Tokens before each request, capped at the capacity: #1 at 1: 3 tokens, accepted; #2 at 1: 2 tokens, accepted; #3 at 2: 2 tokens, accepted; #4 at 2: 1 token, accepted; #5 at 3: 1 token, accepted; #6 at 4: 1 token, accepted; #7 at 4: 0 tokens, rejected; #8 at 5: 1 token, accepted; #9 at 5: 0 tokens, rejected; #10 at 8: 3 tokens, accepted.

## 48. seed 1758118003710685678, level 2

A sliding-window limiter allows 3 accepted requests per 4 seconds. A request at second `t` counts the accepted ones with timestamps in `(t - 4, t]`; rejected requests are not counted. Requests arrive at seconds 0, 3, 3, 3, 4, 7, 7, 9. Which requests are rejected?

a) requests #3, #4, #7
b) none
c) request #4
d) requests #4, #5, #7

**Key: c**

Explanation: A timestamp exactly one window old has left the window. Request by request: #1 at 0: 0 in the window, accepted; #2 at 3: 1 in the window, accepted; #3 at 3: 2 in the window, accepted; #4 at 3: 3 in the window, rejected; #5 at 4: 2 in the window, accepted; #6 at 7: 1 in the window, accepted; #7 at 7: 2 in the window, accepted; #8 at 9: 2 in the window, accepted.

## 49. seed 4372786421514614427, level 1

A token bucket holds at most 4 tokens, starts full and gains 1 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 1, 1, 1, 2, 3, 3, 3. Which requests are rejected?

a) requests #2, #3, #6, #7
b) none
c) requests #5, #6, #7
d) request #7

**Key: d**

Explanation: Tokens before each request, capped at the capacity: #1 at 1: 4 tokens, accepted; #2 at 1: 3 tokens, accepted; #3 at 1: 2 tokens, accepted; #4 at 2: 2 tokens, accepted; #5 at 3: 2 tokens, accepted; #6 at 3: 1 token, accepted; #7 at 3: 0 tokens, rejected.

## 50. seed 1460829379392522035, level 1

A token bucket holds at most 2 tokens, starts full and gains 2 per second, credited whole at each request. Each accepted request costs one token. Requests arrive at seconds 0, 0, 1, 2, 5, 5, 5, 8, 8, 10. Which requests are rejected?

a) requests #1, #2, #7
b) request #7
c) requests #3, #7
d) requests #1, #2

**Key: b**

Explanation: Tokens before each request, capped at the capacity: #1 at 0: 2 tokens, accepted; #2 at 0: 1 token, accepted; #3 at 1: 2 tokens, accepted; #4 at 2: 2 tokens, accepted; #5 at 5: 2 tokens, accepted; #6 at 5: 1 token, accepted; #7 at 5: 0 tokens, rejected; #8 at 8: 2 tokens, accepted; #9 at 8: 1 token, accepted; #10 at 10: 2 tokens, accepted.
