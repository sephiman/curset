# Circuit breaker state (`circuit-breaker-state`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 1548464030997012810, level 2

A circuit breaker uses a count-based window of the last `4` calls, `minimumNumberOfCalls = 2` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F F S S S F S. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 3`. Those calls have outcomes F F F. What is the state once they complete, and how many of the first calls were rejected?

a) OPEN; 5 calls rejected over the whole sequence
b) OPEN; 6 calls rejected
c) OPEN; 4 calls rejected in total
d) HALF_OPEN; 5 calls rejected over the whole sequence

**Key: a**

Explanation: After call 2 the window holds F F: 2 failures out of 2 is 100%, which is at least 50% with at least 2 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 5 later calls are rejected. In HALF_OPEN the 3 permitted calls are evaluated together: 3 failures out of 3 is 100%, at least 50%, so the breaker goes back to OPEN.

## 2. seed 202419126742271943, level 1

A circuit breaker uses a count-based window of the last `8` calls, `minimumNumberOfCalls = 7` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F F S F S F S F F F S. What is the state after the last call, and how many calls were rejected?

a) OPEN; 10 calls rejected over the whole sequence
b) OPEN; 4 calls rejected over the whole sequence
c) OPEN; 5 calls rejected over the whole sequence
d) HALF_OPEN; 4 calls rejected over the whole sequence

**Key: b**

Explanation: After call 7 the window holds F F S F S F S: 4 failures out of 7 is 57%, which is at least 50% with at least 7 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 4 later calls are rejected.

## 3. seed 2080749574312881978, level 1

A circuit breaker uses a count-based window of the last `5` calls, `minimumNumberOfCalls = 4` and `failureRateThreshold = 40`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F S F S S S F S S. What is the state after the last call, and how many calls were rejected?

a) OPEN; 4 calls rejected in total
b) OPEN; 6 calls rejected in total
c) OPEN; 8 calls rejected in total
d) OPEN; 5 calls rejected in total

**Key: d**

Explanation: After call 4 the window holds F S F S: 2 failures out of 4 is 50%, which is at least 40% with at least 4 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 5 later calls are rejected.

## 4. seed 3120809401405707997, level 1

A circuit breaker uses a count-based window of the last `6` calls, `minimumNumberOfCalls = 4` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F F F S F F S F S F. What is the state after the last call, and how many calls were rejected?

a) OPEN; 5 calls rejected in total
b) OPEN; 6 calls rejected over the whole sequence
c) OPEN; 9 calls rejected
d) OPEN; 7 calls rejected

**Key: b**

Explanation: After call 4 the window holds F F F S: 3 failures out of 4 is 75%, which is at least 50% with at least 4 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 6 later calls are rejected.

## 5. seed 3936617210434639087, level 2

A circuit breaker uses a count-based window of the last `8` calls, `minimumNumberOfCalls = 6` and `failureRateThreshold = 60`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S S F F F S S F S F S F. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 4`. Those calls have outcomes S S S F. What is the state once they complete, and how many of the first calls were rejected?

a) CLOSED; 3 calls rejected in total
b) OPEN; 2 calls rejected over the whole sequence
c) CLOSED; 1 call rejected in total
d) CLOSED; 2 calls rejected over the whole sequence

**Key: d**

Explanation: After call 10 the window holds F F F S S F S F: 5 failures out of 8 is 62%, which is at least 60% with at least 6 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 2 later calls are rejected. In HALF_OPEN the 4 permitted calls are evaluated together: 1 failure out of 4 is 25%, below 60%, so the breaker goes back to CLOSED.

## 6. seed 2267942426072891133, level 1

A circuit breaker uses a count-based window of the last `5` calls, `minimumNumberOfCalls = 5` and `failureRateThreshold = 60`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S S F F F F S F S. What is the state after the last call, and how many calls were rejected?

a) HALF_OPEN; 4 calls rejected
b) OPEN; 5 calls rejected over the whole sequence
c) OPEN; 4 calls rejected in total
d) OPEN; 3 calls rejected over the whole sequence

**Key: c**

Explanation: After call 5 the window holds S S F F F: 3 failures out of 5 is 60%, which is at least 60% with at least 5 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 4 later calls are rejected.

## 7. seed 3288673656020992554, level 2

A circuit breaker uses a count-based window of the last `6` calls, `minimumNumberOfCalls = 4` and `failureRateThreshold = 40`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F F S F S S F S F. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 3`. Those calls have outcomes F F S. What is the state once they complete, and how many of the first calls were rejected?

a) OPEN; 6 calls rejected in total
b) HALF_OPEN; 5 calls rejected in total
c) OPEN; 5 calls rejected over the whole sequence
d) OPEN; 4 calls rejected in total

**Key: c**

Explanation: After call 4 the window holds F F S F: 3 failures out of 4 is 75%, which is at least 40% with at least 4 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 5 later calls are rejected. In HALF_OPEN the 3 permitted calls are evaluated together: 2 failures out of 3 is 67%, at least 40%, so the breaker goes back to OPEN.

## 8. seed 3677351288946220813, level 2

A circuit breaker uses a count-based window of the last `5` calls, `minimumNumberOfCalls = 5` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F F S F S F F. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 3`. Those calls have outcomes S S S. What is the state once they complete, and how many of the first calls were rejected?

a) CLOSED; 3 calls rejected
b) HALF_OPEN; 2 calls rejected over the whole sequence
c) CLOSED; 2 calls rejected over the whole sequence
d) CLOSED; 1 call rejected in total

**Key: c**

Explanation: After call 5 the window holds F F S F S: 3 failures out of 5 is 60%, which is at least 50% with at least 5 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 2 later calls are rejected. In HALF_OPEN the 3 permitted calls are evaluated together: 0 failures out of 3 is 0%, below 50%, so the breaker goes back to CLOSED.

## 9. seed 3737197398773088158, level 2

A circuit breaker uses a count-based window of the last `8` calls, `minimumNumberOfCalls = 8` and `failureRateThreshold = 40`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F S S F F S F F S F S S S. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 2`. Those calls have outcomes F F. What is the state once they complete, and how many of the first calls were rejected?

a) OPEN; 5 calls rejected over the whole sequence
b) OPEN; 6 calls rejected in total
c) HALF_OPEN; 5 calls rejected
d) OPEN; 4 calls rejected in total

**Key: a**

Explanation: After call 8 the window holds F S S F F S F F: 5 failures out of 8 is 62%, which is at least 40% with at least 8 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 5 later calls are rejected. In HALF_OPEN the 2 permitted calls are evaluated together: 2 failures out of 2 is 100%, at least 40%, so the breaker goes back to OPEN.

## 10. seed 3461498422774047428, level 1

A circuit breaker uses a count-based window of the last `4` calls, `minimumNumberOfCalls = 4` and `failureRateThreshold = 60`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F S S S F S S S S. What is the state after the last call, and how many calls were rejected?

a) OPEN; 8 calls rejected
b) HALF_OPEN; 0 calls rejected
c) CLOSED; 0 calls rejected
d) OPEN; 1 call rejected

**Key: c**

Explanation: Window of the last 4 calls, rate = failures / calls recorded, evaluated only once 4 calls are recorded. After the last call the failure rate never reaches 60%, so the breaker stays CLOSED and rejects nothing.

## 11. seed 4301137622297578708, level 1

A circuit breaker uses a count-based window of the last `6` calls, `minimumNumberOfCalls = 5` and `failureRateThreshold = 60`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F F S S S F S F F S S S. What is the state after the last call, and how many calls were rejected?

a) OPEN; 11 calls rejected
b) OPEN; 1 call rejected over the whole sequence
c) CLOSED; 0 calls rejected over the whole sequence
d) HALF_OPEN; 0 calls rejected

**Key: c**

Explanation: Window of the last 6 calls, rate = failures / calls recorded, evaluated only once 5 calls are recorded. After the last call the failure rate never reaches 60%, so the breaker stays CLOSED and rejects nothing.

## 12. seed 2509398772125528443, level 1

A circuit breaker uses a count-based window of the last `8` calls, `minimumNumberOfCalls = 6` and `failureRateThreshold = 40`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S S F F S S F F S S F. What is the state after the last call, and how many calls were rejected?

a) OPEN; 4 calls rejected
b) OPEN; 7 calls rejected
c) OPEN; 3 calls rejected
d) OPEN; 5 calls rejected

**Key: a**

Explanation: After call 7 the window holds S S F F S S F: 3 failures out of 7 is 43%, which is at least 40% with at least 6 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 4 later calls are rejected.

## 13. seed 3262222859117565345, level 2

A circuit breaker uses a count-based window of the last `8` calls, `minimumNumberOfCalls = 6` and `failureRateThreshold = 60`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S F F S F S F F S S S F. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 3`. Those calls have outcomes S F F. What is the state once they complete, and how many of the first calls were rejected?

a) HALF_OPEN; 4 calls rejected in total
b) OPEN; 5 calls rejected over the whole sequence
c) OPEN; 3 calls rejected
d) OPEN; 4 calls rejected over the whole sequence

**Key: d**

Explanation: After call 8 the window holds S F F S F S F F: 5 failures out of 8 is 62%, which is at least 60% with at least 6 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 4 later calls are rejected. In HALF_OPEN the 3 permitted calls are evaluated together: 2 failures out of 3 is 67%, at least 60%, so the breaker goes back to OPEN.

## 14. seed 3083030789817849835, level 1

A circuit breaker uses a count-based window of the last `4` calls, `minimumNumberOfCalls = 2` and `failureRateThreshold = 60`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F S S F S S S S. What is the state after the last call, and how many calls were rejected?

a) HALF_OPEN; 0 calls rejected in total
b) OPEN; 7 calls rejected in total
c) CLOSED; 0 calls rejected
d) OPEN; 1 call rejected in total

**Key: c**

Explanation: Window of the last 4 calls, rate = failures / calls recorded, evaluated only once 2 calls are recorded. After the last call the failure rate never reaches 60%, so the breaker stays CLOSED and rejects nothing.

## 15. seed 578995422403329792, level 1

A circuit breaker uses a count-based window of the last `6` calls, `minimumNumberOfCalls = 4` and `failureRateThreshold = 60`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F F F S F S F S F S S S. What is the state after the last call, and how many calls were rejected?

a) OPEN; 7 calls rejected
b) OPEN; 8 calls rejected over the whole sequence
c) HALF_OPEN; 8 calls rejected
d) OPEN; 9 calls rejected

**Key: b**

Explanation: After call 4 the window holds F F F S: 3 failures out of 4 is 75%, which is at least 60% with at least 4 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 8 later calls are rejected.

## 16. seed 3949444949455400525, level 1

A circuit breaker uses a count-based window of the last `6` calls, `minimumNumberOfCalls = 4` and `failureRateThreshold = 60`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F S F S F S F F S. What is the state after the last call, and how many calls were rejected?

a) OPEN; 5 calls rejected over the whole sequence
b) OPEN; 8 calls rejected over the whole sequence
c) OPEN; 4 calls rejected in total
d) OPEN; 3 calls rejected

**Key: c**

Explanation: After call 5 the window holds F S F S F: 3 failures out of 5 is 60%, which is at least 60% with at least 4 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 4 later calls are rejected.

## 17. seed 4268349545781686810, level 1

A circuit breaker uses a count-based window of the last `4` calls, `minimumNumberOfCalls = 2` and `failureRateThreshold = 40`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F F S S F F. What is the state after the last call, and how many calls were rejected?

a) OPEN; 4 calls rejected
b) HALF_OPEN; 4 calls rejected
c) OPEN; 5 calls rejected in total
d) OPEN; 3 calls rejected

**Key: a**

Explanation: After call 2 the window holds F F: 2 failures out of 2 is 100%, which is at least 40% with at least 2 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 4 later calls are rejected.

## 18. seed 741405456574276352, level 1

A circuit breaker uses a count-based window of the last `4` calls, `minimumNumberOfCalls = 3` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S S F F S F S F S F. What is the state after the last call, and how many calls were rejected?

a) OPEN; 5 calls rejected over the whole sequence
b) OPEN; 6 calls rejected over the whole sequence
c) OPEN; 4 calls rejected in total
d) OPEN; 7 calls rejected

**Key: b**

Explanation: After call 4 the window holds S S F F: 2 failures out of 4 is 50%, which is at least 50% with at least 3 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 6 later calls are rejected.

## 19. seed 619112724810118579, level 2

A circuit breaker uses a count-based window of the last `6` calls, `minimumNumberOfCalls = 4` and `failureRateThreshold = 40`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S S F F F F S F. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 4`. Those calls have outcomes S F F F. What is the state once they complete, and how many of the first calls were rejected?

a) OPEN; 3 calls rejected in total
b) HALF_OPEN; 4 calls rejected in total
c) CLOSED; 4 calls rejected
d) OPEN; 4 calls rejected in total

**Key: d**

Explanation: After call 4 the window holds S S F F: 2 failures out of 4 is 50%, which is at least 40% with at least 4 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 4 later calls are rejected. In HALF_OPEN the 4 permitted calls are evaluated together: 3 failures out of 4 is 75%, at least 40%, so the breaker goes back to OPEN.

## 20. seed 3216507674488610169, level 2

A circuit breaker uses a count-based window of the last `5` calls, `minimumNumberOfCalls = 4` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F S F F F S S S S F F. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 2`. Those calls have outcomes S S. What is the state once they complete, and how many of the first calls were rejected?

a) HALF_OPEN; 7 calls rejected over the whole sequence
b) CLOSED; 7 calls rejected
c) CLOSED; 8 calls rejected in total
d) CLOSED; 6 calls rejected over the whole sequence

**Key: b**

Explanation: After call 4 the window holds F S F F: 3 failures out of 4 is 75%, which is at least 50% with at least 4 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 7 later calls are rejected. In HALF_OPEN the 2 permitted calls are evaluated together: 0 failures out of 2 is 0%, below 50%, so the breaker goes back to CLOSED.

## 21. seed 1948293877880348603, level 2

A circuit breaker uses a count-based window of the last `5` calls, `minimumNumberOfCalls = 5` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F F F S F F S. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 3`. Those calls have outcomes S S F. What is the state once they complete, and how many of the first calls were rejected?

a) CLOSED; 3 calls rejected
b) CLOSED; 2 calls rejected in total
c) CLOSED; 1 call rejected in total
d) HALF_OPEN; 2 calls rejected

**Key: b**

Explanation: After call 5 the window holds F F F S F: 4 failures out of 5 is 80%, which is at least 50% with at least 5 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 2 later calls are rejected. In HALF_OPEN the 3 permitted calls are evaluated together: 1 failure out of 3 is 33%, below 50%, so the breaker goes back to CLOSED.

## 22. seed 3022140968624503337, level 2

A circuit breaker uses a count-based window of the last `6` calls, `minimumNumberOfCalls = 4` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F F S F F S S F S F S. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 3`. Those calls have outcomes F S S. What is the state once they complete, and how many of the first calls were rejected?

a) HALF_OPEN; 7 calls rejected over the whole sequence
b) CLOSED; 8 calls rejected in total
c) CLOSED; 7 calls rejected over the whole sequence
d) CLOSED; 6 calls rejected in total

**Key: c**

Explanation: After call 4 the window holds F F S F: 3 failures out of 4 is 75%, which is at least 50% with at least 4 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 7 later calls are rejected. In HALF_OPEN the 3 permitted calls are evaluated together: 1 failure out of 3 is 33%, below 50%, so the breaker goes back to CLOSED.

## 23. seed 2727686684863340019, level 1

A circuit breaker uses a count-based window of the last `5` calls, `minimumNumberOfCalls = 4` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F F S S S F S S F S. What is the state after the last call, and how many calls were rejected?

a) OPEN; 9 calls rejected over the whole sequence
b) OPEN; 7 calls rejected over the whole sequence
c) OPEN; 6 calls rejected over the whole sequence
d) OPEN; 5 calls rejected over the whole sequence

**Key: c**

Explanation: After call 4 the window holds F F S S: 2 failures out of 4 is 50%, which is at least 50% with at least 4 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 6 later calls are rejected.

## 24. seed 3645287691017024451, level 2

A circuit breaker uses a count-based window of the last `6` calls, `minimumNumberOfCalls = 6` and `failureRateThreshold = 60`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F F F F F S S F S S. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 3`. Those calls have outcomes F S S. What is the state once they complete, and how many of the first calls were rejected?

a) CLOSED; 4 calls rejected
b) HALF_OPEN; 4 calls rejected in total
c) CLOSED; 3 calls rejected over the whole sequence
d) OPEN; 4 calls rejected over the whole sequence

**Key: a**

Explanation: After call 6 the window holds F F F F F S: 5 failures out of 6 is 83%, which is at least 60% with at least 6 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 4 later calls are rejected. In HALF_OPEN the 3 permitted calls are evaluated together: 1 failure out of 3 is 33%, below 60%, so the breaker goes back to CLOSED.

## 25. seed 822380313331369648, level 2

A circuit breaker uses a count-based window of the last `5` calls, `minimumNumberOfCalls = 5` and `failureRateThreshold = 40`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S S F S F S F S S S F. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 2`. Those calls have outcomes F S. What is the state once they complete, and how many of the first calls were rejected?

a) OPEN; 7 calls rejected
b) OPEN; 5 calls rejected over the whole sequence
c) HALF_OPEN; 6 calls rejected in total
d) OPEN; 6 calls rejected in total

**Key: d**

Explanation: After call 5 the window holds S S F S F: 2 failures out of 5 is 40%, which is at least 40% with at least 5 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 6 later calls are rejected. In HALF_OPEN the 2 permitted calls are evaluated together: 1 failure out of 2 is 50%, at least 40%, so the breaker goes back to OPEN.

## 26. seed 1749749526757351750, level 2

A circuit breaker uses a count-based window of the last `8` calls, `minimumNumberOfCalls = 7` and `failureRateThreshold = 60`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F S F S F S F S F F. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 4`. Those calls have outcomes S S S S. What is the state once they complete, and how many of the first calls were rejected?

a) CLOSED; -1 calls rejected
b) HALF_OPEN; 0 calls rejected over the whole sequence
c) CLOSED; 1 call rejected in total
d) CLOSED; 0 calls rejected

**Key: d**

Explanation: After call 10 the window holds F S F S F S F F: 5 failures out of 8 is 62%, which is at least 60% with at least 7 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 0 later calls are rejected. In HALF_OPEN the 4 permitted calls are evaluated together: 0 failures out of 4 is 0%, below 60%, so the breaker goes back to CLOSED.

## 27. seed 3849264423752643693, level 1

A circuit breaker uses a count-based window of the last `5` calls, `minimumNumberOfCalls = 5` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F S F F S F S. What is the state after the last call, and how many calls were rejected?

a) HALF_OPEN; 2 calls rejected over the whole sequence
b) OPEN; 3 calls rejected over the whole sequence
c) OPEN; 6 calls rejected over the whole sequence
d) OPEN; 2 calls rejected in total

**Key: d**

Explanation: After call 5 the window holds F S F F S: 3 failures out of 5 is 60%, which is at least 50% with at least 5 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 2 later calls are rejected.

## 28. seed 3142180320362751306, level 2

A circuit breaker uses a count-based window of the last `4` calls, `minimumNumberOfCalls = 2` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S S F F S S. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 4`. Those calls have outcomes F S S F. What is the state once they complete, and how many of the first calls were rejected?

a) OPEN; 2 calls rejected in total
b) OPEN; 3 calls rejected over the whole sequence
c) CLOSED; 2 calls rejected over the whole sequence
d) HALF_OPEN; 2 calls rejected in total

**Key: a**

Explanation: After call 4 the window holds S S F F: 2 failures out of 4 is 50%, which is at least 50% with at least 2 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 2 later calls are rejected. In HALF_OPEN the 4 permitted calls are evaluated together: 2 failures out of 4 is 50%, at least 50%, so the breaker goes back to OPEN.

## 29. seed 552791220757601679, level 1

A circuit breaker uses a count-based window of the last `5` calls, `minimumNumberOfCalls = 4` and `failureRateThreshold = 40`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F S F F F S S F. What is the state after the last call, and how many calls were rejected?

a) OPEN; 7 calls rejected over the whole sequence
b) OPEN; 5 calls rejected over the whole sequence
c) OPEN; 4 calls rejected in total
d) OPEN; 3 calls rejected in total

**Key: c**

Explanation: After call 4 the window holds F S F F: 3 failures out of 4 is 75%, which is at least 40% with at least 4 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 4 later calls are rejected.

## 30. seed 3629731761127880274, level 1

A circuit breaker uses a count-based window of the last `4` calls, `minimumNumberOfCalls = 2` and `failureRateThreshold = 60`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S F S F F F F F S F. What is the state after the last call, and how many calls were rejected?

a) OPEN; 5 calls rejected
b) OPEN; 6 calls rejected over the whole sequence
c) OPEN; 4 calls rejected in total
d) HALF_OPEN; 5 calls rejected

**Key: a**

Explanation: After call 5 the window holds F S F F: 3 failures out of 4 is 75%, which is at least 60% with at least 2 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 5 later calls are rejected.

## 31. seed 1321564930830220473, level 1

A circuit breaker uses a count-based window of the last `4` calls, `minimumNumberOfCalls = 4` and `failureRateThreshold = 40`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S F F S F S S S F S. What is the state after the last call, and how many calls were rejected?

a) OPEN; 6 calls rejected over the whole sequence
b) OPEN; 7 calls rejected over the whole sequence
c) OPEN; 8 calls rejected over the whole sequence
d) OPEN; 5 calls rejected over the whole sequence

**Key: a**

Explanation: After call 4 the window holds S F F S: 2 failures out of 4 is 50%, which is at least 40% with at least 4 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 6 later calls are rejected.

## 32. seed 2745676872668114248, level 1

A circuit breaker uses a count-based window of the last `8` calls, `minimumNumberOfCalls = 6` and `failureRateThreshold = 40`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S S F F F S S S F F S. What is the state after the last call, and how many calls were rejected?

a) OPEN; 5 calls rejected
b) OPEN; 6 calls rejected in total
c) OPEN; 7 calls rejected
d) OPEN; 4 calls rejected

**Key: a**

Explanation: After call 6 the window holds S S F F F S: 3 failures out of 6 is 50%, which is at least 40% with at least 6 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 5 later calls are rejected.

## 33. seed 1197142298924158815, level 2

A circuit breaker uses a count-based window of the last `4` calls, `minimumNumberOfCalls = 2` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F F S F S F S. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 3`. Those calls have outcomes S F S. What is the state once they complete, and how many of the first calls were rejected?

a) OPEN; 5 calls rejected in total
b) CLOSED; 4 calls rejected in total
c) CLOSED; 6 calls rejected over the whole sequence
d) CLOSED; 5 calls rejected

**Key: d**

Explanation: After call 2 the window holds F F: 2 failures out of 2 is 100%, which is at least 50% with at least 2 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 5 later calls are rejected. In HALF_OPEN the 3 permitted calls are evaluated together: 1 failure out of 3 is 33%, below 50%, so the breaker goes back to CLOSED.

## 34. seed 1282706208996382829, level 2

A circuit breaker uses a count-based window of the last `8` calls, `minimumNumberOfCalls = 8` and `failureRateThreshold = 40`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F F S F F F S F F S F S F F. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 3`. Those calls have outcomes F F S. What is the state once they complete, and how many of the first calls were rejected?

a) OPEN; 6 calls rejected over the whole sequence
b) HALF_OPEN; 6 calls rejected in total
c) OPEN; 5 calls rejected in total
d) OPEN; 7 calls rejected in total

**Key: a**

Explanation: After call 8 the window holds F F S F F F S F: 6 failures out of 8 is 75%, which is at least 40% with at least 8 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 6 later calls are rejected. In HALF_OPEN the 3 permitted calls are evaluated together: 2 failures out of 3 is 67%, at least 40%, so the breaker goes back to OPEN.

## 35. seed 297427029291544875, level 2

A circuit breaker uses a count-based window of the last `8` calls, `minimumNumberOfCalls = 8` and `failureRateThreshold = 40`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S F F F F F F S S S S. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 2`. Those calls have outcomes S S. What is the state once they complete, and how many of the first calls were rejected?

a) CLOSED; 2 calls rejected in total
b) CLOSED; 3 calls rejected over the whole sequence
c) HALF_OPEN; 3 calls rejected over the whole sequence
d) CLOSED; 4 calls rejected over the whole sequence

**Key: b**

Explanation: After call 8 the window holds S F F F F F F S: 6 failures out of 8 is 75%, which is at least 40% with at least 8 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 3 later calls are rejected. In HALF_OPEN the 2 permitted calls are evaluated together: 0 failures out of 2 is 0%, below 40%, so the breaker goes back to CLOSED.

## 36. seed 2580994825935527610, level 2

A circuit breaker uses a count-based window of the last `4` calls, `minimumNumberOfCalls = 2` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F F S F F S S F S. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 2`. Those calls have outcomes F F. What is the state once they complete, and how many of the first calls were rejected?

a) OPEN; 8 calls rejected over the whole sequence
b) OPEN; 6 calls rejected
c) OPEN; 7 calls rejected in total
d) HALF_OPEN; 7 calls rejected

**Key: c**

Explanation: After call 2 the window holds F F: 2 failures out of 2 is 100%, which is at least 50% with at least 2 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 7 later calls are rejected. In HALF_OPEN the 2 permitted calls are evaluated together: 2 failures out of 2 is 100%, at least 50%, so the breaker goes back to OPEN.

## 37. seed 1684301001856835921, level 2

A circuit breaker uses a count-based window of the last `4` calls, `minimumNumberOfCalls = 3` and `failureRateThreshold = 40`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S F F F F F S S F. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 2`. Those calls have outcomes F F. What is the state once they complete, and how many of the first calls were rejected?

a) HALF_OPEN; 6 calls rejected
b) OPEN; 5 calls rejected in total
c) OPEN; 7 calls rejected over the whole sequence
d) OPEN; 6 calls rejected in total

**Key: d**

Explanation: After call 3 the window holds S F F: 2 failures out of 3 is 67%, which is at least 40% with at least 3 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 6 later calls are rejected. In HALF_OPEN the 2 permitted calls are evaluated together: 2 failures out of 2 is 100%, at least 40%, so the breaker goes back to OPEN.

## 38. seed 42242083361112002, level 1

A circuit breaker uses a count-based window of the last `5` calls, `minimumNumberOfCalls = 5` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S F S F S F S S S. What is the state after the last call, and how many calls were rejected?

a) OPEN; 3 calls rejected in total
b) OPEN; 7 calls rejected
c) OPEN; 2 calls rejected over the whole sequence
d) OPEN; 4 calls rejected over the whole sequence

**Key: a**

Explanation: After call 6 the window holds F S F S F: 3 failures out of 5 is 60%, which is at least 50% with at least 5 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 3 later calls are rejected.

## 39. seed 577433868758601861, level 1

A circuit breaker uses a count-based window of the last `8` calls, `minimumNumberOfCalls = 8` and `failureRateThreshold = 40`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F S S F S S S F S S S S F S. What is the state after the last call, and how many calls were rejected?

a) CLOSED; 0 calls rejected
b) OPEN; 13 calls rejected in total
c) OPEN; 1 call rejected
d) HALF_OPEN; 0 calls rejected over the whole sequence

**Key: a**

Explanation: Window of the last 8 calls, rate = failures / calls recorded, evaluated only once 8 calls are recorded. After the last call the failure rate never reaches 40%, so the breaker stays CLOSED and rejects nothing.

## 40. seed 275875222212308914, level 2

A circuit breaker uses a count-based window of the last `5` calls, `minimumNumberOfCalls = 5` and `failureRateThreshold = 40`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S S F F S F S S F. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 3`. Those calls have outcomes S S S. What is the state once they complete, and how many of the first calls were rejected?

a) HALF_OPEN; 4 calls rejected in total
b) CLOSED; 3 calls rejected in total
c) CLOSED; 4 calls rejected in total
d) CLOSED; 5 calls rejected

**Key: c**

Explanation: After call 5 the window holds S S F F S: 2 failures out of 5 is 40%, which is at least 40% with at least 5 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 4 later calls are rejected. In HALF_OPEN the 3 permitted calls are evaluated together: 0 failures out of 3 is 0%, below 40%, so the breaker goes back to CLOSED.

## 41. seed 536939817778992148, level 1

A circuit breaker uses a count-based window of the last `5` calls, `minimumNumberOfCalls = 4` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S S S F F S F. What is the state after the last call, and how many calls were rejected?

a) CLOSED; 0 calls rejected
b) OPEN; 1 call rejected in total
c) HALF_OPEN; 0 calls rejected in total
d) OPEN; 0 calls rejected

**Key: d**

Explanation: After call 7 the window holds S F F S F: 3 failures out of 5 is 60%, which is at least 50% with at least 4 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 0 later calls are rejected.

## 42. seed 2905397329512849660, level 1

A circuit breaker uses a count-based window of the last `4` calls, `minimumNumberOfCalls = 4` and `failureRateThreshold = 40`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S F F F F F F S F F. What is the state after the last call, and how many calls were rejected?

a) OPEN; 8 calls rejected
b) OPEN; 5 calls rejected in total
c) OPEN; 6 calls rejected over the whole sequence
d) OPEN; 7 calls rejected in total

**Key: c**

Explanation: After call 4 the window holds S F F F: 3 failures out of 4 is 75%, which is at least 40% with at least 4 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 6 later calls are rejected.

## 43. seed 669894091309479608, level 1

A circuit breaker uses a count-based window of the last `5` calls, `minimumNumberOfCalls = 5` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F F F S F F F. What is the state after the last call, and how many calls were rejected?

a) OPEN; 3 calls rejected in total
b) OPEN; 6 calls rejected over the whole sequence
c) HALF_OPEN; 2 calls rejected over the whole sequence
d) OPEN; 2 calls rejected

**Key: d**

Explanation: After call 5 the window holds F F F S F: 4 failures out of 5 is 80%, which is at least 50% with at least 5 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 2 later calls are rejected.

## 44. seed 3622699717337315083, level 2

A circuit breaker uses a count-based window of the last `5` calls, `minimumNumberOfCalls = 3` and `failureRateThreshold = 40`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S S S F F F S F F F. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 4`. Those calls have outcomes F S S F. What is the state once they complete, and how many of the first calls were rejected?

a) HALF_OPEN; 5 calls rejected
b) OPEN; 5 calls rejected in total
c) OPEN; 6 calls rejected
d) OPEN; 4 calls rejected

**Key: b**

Explanation: After call 5 the window holds S S S F F: 2 failures out of 5 is 40%, which is at least 40% with at least 3 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 5 later calls are rejected. In HALF_OPEN the 4 permitted calls are evaluated together: 2 failures out of 4 is 50%, at least 40%, so the breaker goes back to OPEN.

## 45. seed 1238425725611898293, level 2

A circuit breaker uses a count-based window of the last `4` calls, `minimumNumberOfCalls = 2` and `failureRateThreshold = 40`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S F F F S S S F. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 2`. Those calls have outcomes S S. What is the state once they complete, and how many of the first calls were rejected?

a) CLOSED; 5 calls rejected over the whole sequence
b) CLOSED; 6 calls rejected over the whole sequence
c) CLOSED; 7 calls rejected in total
d) HALF_OPEN; 6 calls rejected over the whole sequence

**Key: b**

Explanation: After call 2 the window holds S F: 1 failure out of 2 is 50%, which is at least 40% with at least 2 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 6 later calls are rejected. In HALF_OPEN the 2 permitted calls are evaluated together: 0 failures out of 2 is 0%, below 40%, so the breaker goes back to CLOSED.

## 46. seed 3552260770847684905, level 2

A circuit breaker uses a count-based window of the last `8` calls, `minimumNumberOfCalls = 6` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S F S S S S S F F F F F F. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 3`. Those calls have outcomes S F F. What is the state once they complete, and how many of the first calls were rejected?

a) HALF_OPEN; 2 calls rejected over the whole sequence
b) OPEN; 2 calls rejected over the whole sequence
c) OPEN; 3 calls rejected
d) OPEN; 1 call rejected

**Key: b**

Explanation: After call 11 the window holds S S S S F F F F: 4 failures out of 8 is 50%, which is at least 50% with at least 6 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 2 later calls are rejected. In HALF_OPEN the 3 permitted calls are evaluated together: 2 failures out of 3 is 67%, at least 50%, so the breaker goes back to OPEN.

## 47. seed 238100933315631579, level 2

A circuit breaker uses a count-based window of the last `5` calls, `minimumNumberOfCalls = 3` and `failureRateThreshold = 60`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F S F S S S S F F. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 3`. Those calls have outcomes F S F. What is the state once they complete, and how many of the first calls were rejected?

a) OPEN; 6 calls rejected
b) OPEN; 5 calls rejected
c) HALF_OPEN; 6 calls rejected
d) OPEN; 7 calls rejected in total

**Key: a**

Explanation: After call 3 the window holds F S F: 2 failures out of 3 is 67%, which is at least 60% with at least 3 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 6 later calls are rejected. In HALF_OPEN the 3 permitted calls are evaluated together: 2 failures out of 3 is 67%, at least 60%, so the breaker goes back to OPEN.

## 48. seed 578174360766343242, level 2

A circuit breaker uses a count-based window of the last `5` calls, `minimumNumberOfCalls = 3` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F F S S F F S S S. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 4`. Those calls have outcomes F S F S. What is the state once they complete, and how many of the first calls were rejected?

a) OPEN; 6 calls rejected
b) OPEN; 5 calls rejected
c) CLOSED; 6 calls rejected
d) OPEN; 7 calls rejected in total

**Key: a**

Explanation: After call 3 the window holds F F S: 2 failures out of 3 is 67%, which is at least 50% with at least 3 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 6 later calls are rejected. In HALF_OPEN the 4 permitted calls are evaluated together: 2 failures out of 4 is 50%, at least 50%, so the breaker goes back to OPEN.

## 49. seed 1723915791980801402, level 2

A circuit breaker uses a count-based window of the last `8` calls, `minimumNumberOfCalls = 7` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) S S S F S F F F S F F F F S. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 3`. Those calls have outcomes S S S. What is the state once they complete, and how many of the first calls were rejected?

a) HALF_OPEN; 6 calls rejected in total
b) CLOSED; 6 calls rejected in total
c) CLOSED; 7 calls rejected
d) CLOSED; 5 calls rejected over the whole sequence

**Key: b**

Explanation: After call 8 the window holds S S S F S F F F: 4 failures out of 8 is 50%, which is at least 50% with at least 7 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 6 later calls are rejected. In HALF_OPEN the 3 permitted calls are evaluated together: 0 failures out of 3 is 0%, below 50%, so the breaker goes back to CLOSED.

## 50. seed 4402180815786493289, level 2

A circuit breaker uses a count-based window of the last `4` calls, `minimumNumberOfCalls = 4` and `failureRateThreshold = 50`. It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes (S success, F failure) F F F F S S F F. Once it opens, `waitDurationInOpenState` elapses after the last call and it becomes HALF_OPEN with `permittedNumberOfCallsInHalfOpenState = 2`. Those calls have outcomes F S. What is the state once they complete, and how many of the first calls were rejected?

a) HALF_OPEN; 4 calls rejected in total
b) OPEN; 4 calls rejected in total
c) CLOSED; 4 calls rejected
d) OPEN; 3 calls rejected

**Key: b**

Explanation: After call 4 the window holds F F F F: 4 failures out of 4 is 100%, which is at least 50% with at least 4 calls recorded, so the breaker opens (the threshold is reached with `>=`, not exceeded). The 4 later calls are rejected. In HALF_OPEN the 2 permitted calls are evaluated together: 1 failure out of 2 is 50%, at least 50%, so the breaker goes back to OPEN.
