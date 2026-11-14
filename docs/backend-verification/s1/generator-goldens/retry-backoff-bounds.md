# Retry backoff bounds (`retry-backoff-bounds`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 1418252426046215390, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(3200, 100 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 7?

a) 1,600 ms
b) about 6,400 ms
c) 700 ms
d) about 3,200 ms

**Key: d**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 7 is bounded by min(3200, 100 x 2^6) = min(3200, 6400) = 3200 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 2. seed 3663769149868219308, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(400, 100 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 6?

a) approximately 800 ms
b) about 400 ms
c) about 600 ms
d) about 200 ms

**Key: b**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 6 is bounded by min(400, 100 x 2^5) = min(400, 3200) = 400 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 3. seed 202866727293709324, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(1600, 200 * 2^(n-1))]` ms. What is the largest total wait the client can accumulate over its first 7 retries?

a) 7,800 ms
b) about 12,700 ms
c) about 25,400 ms
d) approximately 3,900 ms

**Key: a**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(1600, 200) = 200, retry 2: min(1600, 400) = 400, retry 3: min(1600, 800) = 800, retry 4: min(1600, 1600) = 1600, retry 5: min(1600, 3200) = 1600, retry 6: min(1600, 6400) = 1600, retry 7: min(1600, 12800) = 1600. The worst case draws every bound: 200 + 400 + 800 + 1600 + 1600 + 1600 + 1600 = 7800 ms.

## 4. seed 2438426822505244164, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(2000, 500 * 2^(n-1))]` ms. What is the expected total wait over the first 6 retries?

a) 4,750 ms
b) about 2,000 ms
c) 11,000 ms
d) approximately 15,750 ms

**Key: a**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(2000, 500) = 500, retry 2: min(2000, 1000) = 1000, retry 3: min(2000, 2000) = 2000, retry 4: min(2000, 4000) = 2000, retry 5: min(2000, 8000) = 2000, retry 6: min(2000, 16000) = 2000. A uniform draw from 0 to a bound averages half of it, so the expected total is half of 500 + 1000 + 2000 + 2000 + 2000 + 2000 = 9500 ms, that is 4,750 ms.

## 5. seed 3908396930074060279, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(100, 50 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 5?

a) approximately 200 ms
b) approximately 250 ms
c) 800 ms
d) approximately 100 ms

**Key: d**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 5 is bounded by min(100, 50 x 2^4) = min(100, 800) = 100 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 6. seed 442584982756009158, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(100, 50 * 2^(n-1))]` ms. What is the expected total wait over the first 4 retries?

a) approximately 100 ms
b) 175 ms
c) approximately 400 ms
d) 750 ms

**Key: b**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(100, 50) = 50, retry 2: min(100, 100) = 100, retry 3: min(100, 200) = 100, retry 4: min(100, 400) = 100. A uniform draw from 0 to a bound averages half of it, so the expected total is half of 50 + 100 + 100 + 100 = 350 ms, that is 175 ms.

## 7. seed 4171038782601562652, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(500, 250 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 6?

a) 500 ms
b) 1,500 ms
c) 8,000 ms
d) approximately 250 ms

**Key: a**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 6 is bounded by min(500, 250 x 2^5) = min(500, 8000) = 500 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 8. seed 2991986083349088283, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(800, 200 * 2^(n-1))]` ms. What is the expected total wait over the first 5 retries?

a) about 1,500 ms
b) approximately 6,200 ms
c) approximately 3,600 ms
d) 800 ms

**Key: a**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(800, 200) = 200, retry 2: min(800, 400) = 400, retry 3: min(800, 800) = 800, retry 4: min(800, 1600) = 800, retry 5: min(800, 3200) = 800. A uniform draw from 0 to a bound averages half of it, so the expected total is half of 200 + 400 + 800 + 800 + 800 = 3000 ms, that is 1,500 ms.

## 9. seed 3867663592586203059, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(4000, 500 * 2^(n-1))]` ms. What is the expected total wait over the first 5 retries?

a) 5,750 ms
b) about 4,000 ms
c) approximately 7,750 ms
d) approximately 20,000 ms

**Key: a**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(4000, 500) = 500, retry 2: min(4000, 1000) = 1000, retry 3: min(4000, 2000) = 2000, retry 4: min(4000, 4000) = 4000, retry 5: min(4000, 8000) = 4000. A uniform draw from 0 to a bound averages half of it, so the expected total is half of 500 + 1000 + 2000 + 4000 + 4000 = 11500 ms, that is 5,750 ms.

## 10. seed 3728251942695197410, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(4000, 250 * 2^(n-1))]` ms. What is the largest total wait the client can accumulate over its first 7 retries?

a) 7,875 ms
b) approximately 15,750 ms
c) approximately 31,750 ms
d) about 4,000 ms

**Key: b**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(4000, 250) = 250, retry 2: min(4000, 500) = 500, retry 3: min(4000, 1000) = 1000, retry 4: min(4000, 2000) = 2000, retry 5: min(4000, 4000) = 4000, retry 6: min(4000, 8000) = 4000, retry 7: min(4000, 16000) = 4000. The worst case draws every bound: 250 + 500 + 1000 + 2000 + 4000 + 4000 + 4000 = 15750 ms.

## 11. seed 4322366904261697838, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(400, 100 * 2^(n-1))]` ms. What is the expected total wait over the first 7 retries?

a) approximately 400 ms
b) about 1,150 ms
c) 12,700 ms
d) 6,350 ms

**Key: b**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(400, 100) = 100, retry 2: min(400, 200) = 200, retry 3: min(400, 400) = 400, retry 4: min(400, 800) = 400, retry 5: min(400, 1600) = 400, retry 6: min(400, 3200) = 400, retry 7: min(400, 6400) = 400. A uniform draw from 0 to a bound averages half of it, so the expected total is half of 100 + 200 + 400 + 400 + 400 + 400 + 400 = 2300 ms, that is 1,150 ms.

## 12. seed 4229572457982111798, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(800, 100 * 2^(n-1))]` ms. What is the expected total wait over the first 6 retries?

a) approximately 1,550 ms
b) approximately 6,300 ms
c) about 4,800 ms
d) approximately 3,800 ms

**Key: a**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(800, 100) = 100, retry 2: min(800, 200) = 200, retry 3: min(800, 400) = 400, retry 4: min(800, 800) = 800, retry 5: min(800, 1600) = 800, retry 6: min(800, 3200) = 800. A uniform draw from 0 to a bound averages half of it, so the expected total is half of 100 + 200 + 400 + 800 + 800 + 800 = 3100 ms, that is 1,550 ms.

## 13. seed 4548875273807515812, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(500, 250 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 4?

a) about 1,000 ms
b) approximately 250 ms
c) about 2,000 ms
d) about 500 ms

**Key: d**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 4 is bounded by min(500, 250 x 2^3) = min(500, 2000) = 500 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 14. seed 4333209302098577737, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(100, 50 * 2^(n-1))]` ms. What is the expected total wait over the first 5 retries?

a) approximately 500 ms
b) approximately 100 ms
c) approximately 775 ms
d) approximately 225 ms

**Key: d**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(100, 50) = 50, retry 2: min(100, 100) = 100, retry 3: min(100, 200) = 100, retry 4: min(100, 400) = 100, retry 5: min(100, 800) = 100. A uniform draw from 0 to a bound averages half of it, so the expected total is half of 50 + 100 + 100 + 100 + 100 = 450 ms, that is 225 ms.

## 15. seed 1252635660231606994, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(400, 200 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 4?

a) 1,600 ms
b) approximately 200 ms
c) about 400 ms
d) about 800 ms

**Key: c**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 4 is bounded by min(400, 200 x 2^3) = min(400, 1600) = 400 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 16. seed 4222926251235536943, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(400, 100 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 6?

a) approximately 800 ms
b) approximately 200 ms
c) approximately 600 ms
d) about 400 ms

**Key: d**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 6 is bounded by min(400, 100 x 2^5) = min(400, 3200) = 400 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 17. seed 3043541559519716429, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(400, 100 * 2^(n-1))]` ms. What is the expected total wait over the first 5 retries?

a) 1,800 ms
b) about 400 ms
c) about 750 ms
d) about 3,100 ms

**Key: c**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(400, 100) = 100, retry 2: min(400, 200) = 200, retry 3: min(400, 400) = 400, retry 4: min(400, 800) = 400, retry 5: min(400, 1600) = 400. A uniform draw from 0 to a bound averages half of it, so the expected total is half of 100 + 200 + 400 + 400 + 400 = 1500 ms, that is 750 ms.

## 18. seed 4147359084458410610, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(1000, 250 * 2^(n-1))]` ms. What is the largest total wait the client can accumulate over its first 7 retries?

a) about 15,875 ms
b) 1,000 ms
c) 2,875 ms
d) 5,750 ms

**Key: d**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(1000, 250) = 250, retry 2: min(1000, 500) = 500, retry 3: min(1000, 1000) = 1000, retry 4: min(1000, 2000) = 1000, retry 5: min(1000, 4000) = 1000, retry 6: min(1000, 8000) = 1000, retry 7: min(1000, 16000) = 1000. The worst case draws every bound: 250 + 500 + 1000 + 1000 + 1000 + 1000 + 1000 = 5750 ms.

## 19. seed 1820623702201231647, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(400, 200 * 2^(n-1))]` ms. What is the expected total wait over the first 3 retries?

a) 1,400 ms
b) about 1,000 ms
c) about 500 ms
d) about 700 ms

**Key: c**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(400, 200) = 200, retry 2: min(400, 400) = 400, retry 3: min(400, 800) = 400. A uniform draw from 0 to a bound averages half of it, so the expected total is half of 200 + 400 + 400 = 1000 ms, that is 500 ms.

## 20. seed 227591464359003464, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(800, 200 * 2^(n-1))]` ms. What is the largest total wait the client can accumulate over its first 4 retries?

a) 3,000 ms
b) approximately 1,100 ms
c) 2,200 ms
d) 1,500 ms

**Key: c**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(800, 200) = 200, retry 2: min(800, 400) = 400, retry 3: min(800, 800) = 800, retry 4: min(800, 1600) = 800. The worst case draws every bound: 200 + 400 + 800 + 800 = 2200 ms.

## 21. seed 4550244628081023494, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(400, 100 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 5?

a) about 500 ms
b) about 800 ms
c) 400 ms
d) 200 ms

**Key: c**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 5 is bounded by min(400, 100 x 2^4) = min(400, 1600) = 400 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 22. seed 1537059522560099784, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(800, 50 * 2^(n-1))]` ms. What is the largest total wait the client can accumulate over its first 7 retries?

a) 6,350 ms
b) about 800 ms
c) about 3,150 ms
d) approximately 1,575 ms

**Key: c**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(800, 50) = 50, retry 2: min(800, 100) = 100, retry 3: min(800, 200) = 200, retry 4: min(800, 400) = 400, retry 5: min(800, 800) = 800, retry 6: min(800, 1600) = 800, retry 7: min(800, 3200) = 800. The worst case draws every bound: 50 + 100 + 200 + 400 + 800 + 800 + 800 = 3150 ms.

## 23. seed 2184638627945359920, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(8000, 250 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 7?

a) 16,000 ms
b) about 8,000 ms
c) about 4,000 ms
d) about 1,750 ms

**Key: b**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 7 is bounded by min(8000, 250 x 2^6) = min(8000, 16000) = 8000 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 24. seed 1098506559830247751, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(400, 100 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 6?

a) 800 ms
b) 400 ms
c) 200 ms
d) about 600 ms

**Key: b**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 6 is bounded by min(400, 100 x 2^5) = min(400, 3200) = 400 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 25. seed 617226062708495594, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(400, 100 * 2^(n-1))]` ms. What is the expected total wait over the first 4 retries?

a) 400 ms
b) approximately 1,100 ms
c) about 550 ms
d) approximately 750 ms

**Key: c**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(400, 100) = 100, retry 2: min(400, 200) = 200, retry 3: min(400, 400) = 400, retry 4: min(400, 800) = 400. A uniform draw from 0 to a bound averages half of it, so the expected total is half of 100 + 200 + 400 + 400 = 1100 ms, that is 550 ms.

## 26. seed 1792293118001569024, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(1000, 500 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 3?

a) 500 ms
b) about 1,000 ms
c) approximately 2,000 ms
d) 1,500 ms

**Key: b**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 3 is bounded by min(1000, 500 x 2^2) = min(1000, 2000) = 1000 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 27. seed 293275521572068256, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(2000, 500 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 6?

a) approximately 1,000 ms
b) 4,000 ms
c) 3,000 ms
d) 2,000 ms

**Key: d**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 6 is bounded by min(2000, 500 x 2^5) = min(2000, 16000) = 2000 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 28. seed 3099953316958548899, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(400, 200 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 4?

a) 200 ms
b) approximately 800 ms
c) approximately 400 ms
d) about 1,600 ms

**Key: c**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 4 is bounded by min(400, 200 x 2^3) = min(400, 1600) = 400 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 29. seed 3216707265427932021, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(100, 50 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 3?

a) about 150 ms
b) about 200 ms
c) 50 ms
d) about 100 ms

**Key: d**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 3 is bounded by min(100, 50 x 2^2) = min(100, 200) = 100 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 30. seed 3107262463775776121, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(1000, 500 * 2^(n-1))]` ms. What is the largest total wait the client can accumulate over its first 3 retries?

a) about 2,500 ms
b) approximately 3,500 ms
c) about 1,000 ms
d) 1,250 ms

**Key: a**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(1000, 500) = 500, retry 2: min(1000, 1000) = 1000, retry 3: min(1000, 2000) = 1000. The worst case draws every bound: 500 + 1000 + 1000 = 2500 ms.

## 31. seed 3504024945669648087, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(8000, 500 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 7?

a) 32,000 ms
b) approximately 4,000 ms
c) approximately 16,000 ms
d) about 8,000 ms

**Key: d**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 7 is bounded by min(8000, 500 x 2^6) = min(8000, 32000) = 8000 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 32. seed 1340106325131316766, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(200, 50 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 7?

a) about 400 ms
b) about 3,200 ms
c) about 100 ms
d) 200 ms

**Key: d**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 7 is bounded by min(200, 50 x 2^6) = min(200, 3200) = 200 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 33. seed 3852294499876777342, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(1000, 500 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 3?

a) 1,500 ms
b) 1,000 ms
c) approximately 500 ms
d) 2,000 ms

**Key: b**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 3 is bounded by min(1000, 500 x 2^2) = min(1000, 2000) = 1000 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 34. seed 3595765489611193207, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(100, 50 * 2^(n-1))]` ms. What is the largest total wait the client can accumulate over its first 3 retries?

a) about 250 ms
b) 125 ms
c) 350 ms
d) 100 ms

**Key: a**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(100, 50) = 50, retry 2: min(100, 100) = 100, retry 3: min(100, 200) = 100. The worst case draws every bound: 50 + 100 + 100 = 250 ms.

## 35. seed 4458881911705540010, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(200, 100 * 2^(n-1))]` ms. What is the expected total wait over the first 3 retries?

a) approximately 250 ms
b) 350 ms
c) approximately 700 ms
d) about 200 ms

**Key: a**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(200, 100) = 100, retry 2: min(200, 200) = 200, retry 3: min(200, 400) = 200. A uniform draw from 0 to a bound averages half of it, so the expected total is half of 100 + 200 + 200 = 500 ms, that is 250 ms.

## 36. seed 4316589157792426960, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(4000, 500 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 5?

a) 4,000 ms
b) 2,500 ms
c) approximately 8,000 ms
d) about 2,000 ms

**Key: a**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 5 is bounded by min(4000, 500 x 2^4) = min(4000, 8000) = 4000 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 37. seed 412839686989836039, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(200, 100 * 2^(n-1))]` ms. What is the largest total wait the client can accumulate over its first 4 retries?

a) about 350 ms
b) approximately 700 ms
c) approximately 1,500 ms
d) approximately 200 ms

**Key: b**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(200, 100) = 100, retry 2: min(200, 200) = 200, retry 3: min(200, 400) = 200, retry 4: min(200, 800) = 200. The worst case draws every bound: 100 + 200 + 200 + 200 = 700 ms.

## 38. seed 1053557669737080345, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(800, 200 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 5?

a) approximately 3,200 ms
b) 800 ms
c) 400 ms
d) 1,600 ms

**Key: b**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 5 is bounded by min(800, 200 x 2^4) = min(800, 3200) = 800 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 39. seed 731482422525914925, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(4000, 250 * 2^(n-1))]` ms. What is the largest total wait the client can accumulate over its first 6 retries?

a) about 5,875 ms
b) approximately 24,000 ms
c) approximately 11,750 ms
d) approximately 4,000 ms

**Key: c**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(4000, 250) = 250, retry 2: min(4000, 500) = 500, retry 3: min(4000, 1000) = 1000, retry 4: min(4000, 2000) = 2000, retry 5: min(4000, 4000) = 4000, retry 6: min(4000, 8000) = 4000. The worst case draws every bound: 250 + 500 + 1000 + 2000 + 4000 + 4000 = 11750 ms.

## 40. seed 739028035678821737, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(100, 50 * 2^(n-1))]` ms. What is the expected total wait over the first 7 retries?

a) 3,175 ms
b) approximately 325 ms
c) 100 ms
d) 6,350 ms

**Key: b**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(100, 50) = 50, retry 2: min(100, 100) = 100, retry 3: min(100, 200) = 100, retry 4: min(100, 400) = 100, retry 5: min(100, 800) = 100, retry 6: min(100, 1600) = 100, retry 7: min(100, 3200) = 100. A uniform draw from 0 to a bound averages half of it, so the expected total is half of 50 + 100 + 100 + 100 + 100 + 100 + 100 = 650 ms, that is 325 ms.

## 41. seed 2904938924409017556, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(200, 100 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 3?

a) approximately 100 ms
b) 400 ms
c) 200 ms
d) approximately 300 ms

**Key: c**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 3 is bounded by min(200, 100 x 2^2) = min(200, 400) = 200 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 42. seed 1487588341274901025, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(200, 100 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 3?

a) approximately 200 ms
b) about 100 ms
c) 400 ms
d) 300 ms

**Key: a**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 3 is bounded by min(200, 100 x 2^2) = min(200, 400) = 200 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 43. seed 4386234445958243259, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(1000, 500 * 2^(n-1))]` ms. What is the largest total wait the client can accumulate over its first 4 retries?

a) 3,500 ms
b) about 7,500 ms
c) 1,000 ms
d) 1,750 ms

**Key: a**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(1000, 500) = 500, retry 2: min(1000, 1000) = 1000, retry 3: min(1000, 2000) = 1000, retry 4: min(1000, 4000) = 1000. The worst case draws every bound: 500 + 1000 + 1000 + 1000 = 3500 ms.

## 44. seed 902247633126600209, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(500, 250 * 2^(n-1))]` ms. What is the largest total wait the client can accumulate over its first 4 retries?

a) about 3,750 ms
b) approximately 500 ms
c) approximately 1,750 ms
d) approximately 875 ms

**Key: c**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(500, 250) = 250, retry 2: min(500, 500) = 500, retry 3: min(500, 1000) = 500, retry 4: min(500, 2000) = 500. The worst case draws every bound: 250 + 500 + 500 + 500 = 1750 ms.

## 45. seed 4372665367744569531, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(100, 50 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 5?

a) 250 ms
b) approximately 100 ms
c) about 200 ms
d) 800 ms

**Key: b**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 5 is bounded by min(100, 50 x 2^4) = min(100, 800) = 100 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 46. seed 3397384341206690059, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(1000, 250 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 5?

a) about 2,000 ms
b) about 1,000 ms
c) about 1,250 ms
d) approximately 4,000 ms

**Key: b**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 5 is bounded by min(1000, 250 x 2^4) = min(1000, 4000) = 1000 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 47. seed 1796179670436952482, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(400, 50 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 6?

a) approximately 800 ms
b) 200 ms
c) 300 ms
d) about 400 ms

**Key: d**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 6 is bounded by min(400, 50 x 2^5) = min(400, 1600) = 400 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 48. seed 1992990759292096021, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(3200, 200 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 6?

a) about 3,200 ms
b) 1,600 ms
c) 6,400 ms
d) about 1,200 ms

**Key: a**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 6 is bounded by min(3200, 200 x 2^5) = min(3200, 6400) = 3200 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 49. seed 40527688512682739, level 1

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(400, 200 * 2^(n-1))]` ms. What is the largest wait the client can draw before retry 4?

a) 1,600 ms
b) 200 ms
c) approximately 400 ms
d) approximately 800 ms

**Key: c**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. The draw before retry 4 is bounded by min(400, 200 x 2^3) = min(400, 1600) = 400 ms: the cap stops the doubling, and jitter only lowers the draw, never raises the bound.

## 50. seed 2021238193662643532, level 2

A client retries with exponential backoff and full jitter: the wait before retry `n` (first retry `n = 1`) is drawn uniformly from `[0, min(400, 200 * 2^(n-1))]` ms. What is the expected total wait over the first 3 retries?

a) approximately 1,400 ms
b) about 400 ms
c) about 1,000 ms
d) 500 ms

**Key: d**

Explanation: According to the simulator code AWS published for Marc Brooker's post "Exponential Backoff And Jitter", full jitter draws each wait uniformly between 0 and the capped exponential value; the stem fixes the exponent. Upper bounds in ms, retry 1: min(400, 200) = 200, retry 2: min(400, 400) = 400, retry 3: min(400, 800) = 400. A uniform draw from 0 to a bound averages half of it, so the expected total is half of 200 + 400 + 400 = 1000 ms, that is 500 ms.
