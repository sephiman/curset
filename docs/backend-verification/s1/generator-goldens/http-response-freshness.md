# HTTP response freshness (`http-response-freshness`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 446930794742729348, level 1

A cache holds a response with `Cache-Control: max-age=300`. The age of the response is 105 seconds. In how many seconds does the response become stale?

a) 195 seconds
b) 105 seconds
c) 300 seconds
d) 405 seconds

**Key: a**

Explanation: Inputs: `max-age=300`, age 105 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 300 seconds, from `max-age=300`. Step 2: the response turns stale when its age reaches 300: 300 - 105 = 195 seconds from now. Result: 195 seconds. The other options answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 2. seed 3702885578843718751, level 1

A cache holds a response with `Cache-Control: max-age=60`. The age of the response is 15 seconds. In how many seconds does the response become stale?

a) 45 seconds
b) 60 seconds
c) 15 seconds
d) 75 seconds

**Key: a**

Explanation: Inputs: `max-age=60`, age 15 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 60 seconds, from `max-age=60`. Step 2: the response turns stale when its age reaches 60: 60 - 15 = 45 seconds from now. Result: 45 seconds. The other options answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 3. seed 3347585348436395757, level 2

A shared cache holds a response with `Cache-Control: max-age=120, s-maxage=90`. The age of the response is 360 seconds. How many seconds ago did the response become stale?

a) 360 seconds
b) 450 seconds
c) 270 seconds
d) 120 seconds

**Key: c**

Explanation: Inputs: `max-age=120`, `s-maxage=90`, age 360 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 90 seconds, from `s-maxage=90`, which a shared cache lets override `max-age=120`. Step 2: the response turned stale when its age reached 90: 360 - 90 = 270 seconds ago. Result: 270 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 4. seed 4052650949624178639, level 2

A shared cache holds a response with `Cache-Control: max-age=600, s-maxage=300`. The age of the response is 135 seconds. In how many seconds does the response become stale?

a) 465 seconds
b) 165 seconds
c) 600 seconds
d) 300 seconds

**Key: b**

Explanation: Inputs: `max-age=600`, `s-maxage=300`, age 135 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 300 seconds, from `s-maxage=300`, which a shared cache lets override `max-age=600`. Step 2: the response turns stale when its age reaches 300: 300 - 135 = 165 seconds from now. Result: 165 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 5. seed 267455362047664218, level 2

A shared cache holds a response with `Cache-Control: max-age=600, s-maxage=120`. The age of the response is 225 seconds. How many seconds ago did the response become stale?

a) 225 seconds
b) 105 seconds
c) 600 seconds
d) 345 seconds

**Key: b**

Explanation: Inputs: `max-age=600`, `s-maxage=120`, age 225 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 120 seconds, from `s-maxage=120`, which a shared cache lets override `max-age=600`. Step 2: the response turned stale when its age reached 120: 225 - 120 = 105 seconds ago. Result: 105 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 6. seed 2688214854971762205, level 2

A shared cache holds a response with `Cache-Control: max-age=180, s-maxage=300`. The age of the response is 45 seconds. In how many seconds does the response become stale?

a) 135 seconds
b) 180 seconds
c) 345 seconds
d) 255 seconds

**Key: d**

Explanation: Inputs: `max-age=180`, `s-maxage=300`, age 45 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 300 seconds, from `s-maxage=300`, which a shared cache lets override `max-age=180`. Step 2: the response turns stale when its age reaches 300: 300 - 45 = 255 seconds from now. Result: 255 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 7. seed 2623392054640259003, level 1

A cache holds a response with `Cache-Control: max-age=600`. The age of the response is 180 seconds. In how many seconds does the response become stale?

a) 600 seconds
b) 180 seconds
c) 420 seconds
d) 780 seconds

**Key: c**

Explanation: Inputs: `max-age=600`, age 180 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 600 seconds, from `max-age=600`. Step 2: the response turns stale when its age reaches 600: 600 - 180 = 420 seconds from now. Result: 420 seconds. The other options answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 8. seed 131849392424606167, level 2

A shared cache holds a response with `Cache-Control: max-age=240, s-maxage=180`. The age of the response is 345 seconds. How many seconds ago did the response become stale?

a) 165 seconds
b) 240 seconds
c) 525 seconds
d) 105 seconds

**Key: a**

Explanation: Inputs: `max-age=240`, `s-maxage=180`, age 345 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 180 seconds, from `s-maxage=180`, which a shared cache lets override `max-age=240`. Step 2: the response turned stale when its age reached 180: 345 - 180 = 165 seconds ago. Result: 165 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 9. seed 3788108285293076337, level 2

A shared cache holds a response with `Cache-Control: max-age=180, s-maxage=300`. The age of the response is 525 seconds. How many seconds ago did the response become stale?

a) 225 seconds
b) 345 seconds
c) 825 seconds
d) 525 seconds

**Key: a**

Explanation: Inputs: `max-age=180`, `s-maxage=300`, age 525 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 300 seconds, from `s-maxage=300`, which a shared cache lets override `max-age=180`. Step 2: the response turned stale when its age reached 300: 525 - 300 = 225 seconds ago. Result: 225 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 10. seed 451315686952923283, level 2

A shared cache holds a response with `Cache-Control: max-age=600, s-maxage=180`. The age of the response is 420 seconds. How many seconds ago did the response become stale?

a) 240 seconds
b) 600 seconds
c) 420 seconds
d) 180 seconds

**Key: a**

Explanation: Inputs: `max-age=600`, `s-maxage=180`, age 420 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 180 seconds, from `s-maxage=180`, which a shared cache lets override `max-age=600`. Step 2: the response turned stale when its age reached 180: 420 - 180 = 240 seconds ago. Result: 240 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 11. seed 647502150211439616, level 1

A cache holds a response with `Cache-Control: max-age=240`. The age of the response is 105 seconds. In how many seconds does the response become stale?

a) 135 seconds
b) 345 seconds
c) 240 seconds
d) 105 seconds

**Key: a**

Explanation: Inputs: `max-age=240`, age 105 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 240 seconds, from `max-age=240`. Step 2: the response turns stale when its age reaches 240: 240 - 105 = 135 seconds from now. Result: 135 seconds. The other options answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 12. seed 808207741334118620, level 2

A shared cache holds a response with `Cache-Control: max-age=600, s-maxage=60`. The age of the response is 195 seconds. How many seconds ago did the response become stale?

a) 135 seconds
b) 405 seconds
c) 195 seconds
d) 255 seconds

**Key: a**

Explanation: Inputs: `max-age=600`, `s-maxage=60`, age 195 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 60 seconds, from `s-maxage=60`, which a shared cache lets override `max-age=600`. Step 2: the response turned stale when its age reached 60: 195 - 60 = 135 seconds ago. Result: 135 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 13. seed 1613385426883272414, level 2

A shared cache holds a response with `Cache-Control: max-age=180, s-maxage=240`. The age of the response is 525 seconds. How many seconds ago did the response become stale?

a) 765 seconds
b) 525 seconds
c) 180 seconds
d) 285 seconds

**Key: d**

Explanation: Inputs: `max-age=180`, `s-maxage=240`, age 525 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 240 seconds, from `s-maxage=240`, which a shared cache lets override `max-age=180`. Step 2: the response turned stale when its age reached 240: 525 - 240 = 285 seconds ago. Result: 285 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 14. seed 4323224354133914140, level 2

A shared cache holds a response with `Cache-Control: max-age=300, s-maxage=180`. The age of the response is 450 seconds. How many seconds ago did the response become stale?

a) 450 seconds
b) 630 seconds
c) 150 seconds
d) 270 seconds

**Key: d**

Explanation: Inputs: `max-age=300`, `s-maxage=180`, age 450 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 180 seconds, from `s-maxage=180`, which a shared cache lets override `max-age=300`. Step 2: the response turned stale when its age reached 180: 450 - 180 = 270 seconds ago. Result: 270 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 15. seed 1695233371807448876, level 2

A shared cache holds a response with `Cache-Control: max-age=600, s-maxage=90`. The age of the response is 210 seconds. How many seconds ago did the response become stale?

a) 390 seconds
b) 120 seconds
c) 600 seconds
d) 210 seconds

**Key: b**

Explanation: Inputs: `max-age=600`, `s-maxage=90`, age 210 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 90 seconds, from `s-maxage=90`, which a shared cache lets override `max-age=600`. Step 2: the response turned stale when its age reached 90: 210 - 90 = 120 seconds ago. Result: 120 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 16. seed 4239934451425390280, level 2

A shared cache holds a response with `Cache-Control: max-age=600, s-maxage=240`. The age of the response is 480 seconds. How many seconds ago did the response become stale?

a) 240 seconds
b) 480 seconds
c) 720 seconds
d) 120 seconds

**Key: a**

Explanation: Inputs: `max-age=600`, `s-maxage=240`, age 480 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 240 seconds, from `s-maxage=240`, which a shared cache lets override `max-age=600`. Step 2: the response turned stale when its age reached 240: 480 - 240 = 240 seconds ago. Result: 240 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 17. seed 1941861767875066477, level 1

A cache holds a response with `Cache-Control: max-age=60`. The age of the response is 15 seconds. In how many seconds does the response become stale?

a) 60 seconds
b) 15 seconds
c) 45 seconds
d) 75 seconds

**Key: c**

Explanation: Inputs: `max-age=60`, age 15 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 60 seconds, from `max-age=60`. Step 2: the response turns stale when its age reaches 60: 60 - 15 = 45 seconds from now. Result: 45 seconds. The other options answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 18. seed 1484015803793539395, level 2

A shared cache holds a response with `Cache-Control: max-age=120, s-maxage=240`. The age of the response is 60 seconds. In how many seconds does the response become stale?

a) 240 seconds
b) 120 seconds
c) 300 seconds
d) 180 seconds

**Key: d**

Explanation: Inputs: `max-age=120`, `s-maxage=240`, age 60 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 240 seconds, from `s-maxage=240`, which a shared cache lets override `max-age=120`. Step 2: the response turns stale when its age reaches 240: 240 - 60 = 180 seconds from now. Result: 180 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 19. seed 596124557119029452, level 1

A cache holds a response with `Cache-Control: max-age=60`. The age of the response is 15 seconds. In how many seconds does the response become stale?

a) 60 seconds
b) 75 seconds
c) 15 seconds
d) 45 seconds

**Key: d**

Explanation: Inputs: `max-age=60`, age 15 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 60 seconds, from `max-age=60`. Step 2: the response turns stale when its age reaches 60: 60 - 15 = 45 seconds from now. Result: 45 seconds. The other options answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 20. seed 4219880888570818890, level 2

A shared cache holds a response with `Cache-Control: max-age=120, s-maxage=60`. The age of the response is 330 seconds. How many seconds ago did the response become stale?

a) 120 seconds
b) 210 seconds
c) 270 seconds
d) 390 seconds

**Key: c**

Explanation: Inputs: `max-age=120`, `s-maxage=60`, age 330 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 60 seconds, from `s-maxage=60`, which a shared cache lets override `max-age=120`. Step 2: the response turned stale when its age reached 60: 330 - 60 = 270 seconds ago. Result: 270 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 21. seed 1891610817564657378, level 2

A shared cache holds a response with `Cache-Control: max-age=240, s-maxage=180`. The age of the response is 330 seconds. How many seconds ago did the response become stale?

a) 240 seconds
b) 330 seconds
c) 510 seconds
d) 150 seconds

**Key: d**

Explanation: Inputs: `max-age=240`, `s-maxage=180`, age 330 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 180 seconds, from `s-maxage=180`, which a shared cache lets override `max-age=240`. Step 2: the response turned stale when its age reached 180: 330 - 180 = 150 seconds ago. Result: 150 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 22. seed 4245533484161240441, level 2

A shared cache holds a response with `Cache-Control: max-age=120, s-maxage=180`. The age of the response is 450 seconds. How many seconds ago did the response become stale?

a) 270 seconds
b) 180 seconds
c) 630 seconds
d) 450 seconds

**Key: a**

Explanation: Inputs: `max-age=120`, `s-maxage=180`, age 450 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 180 seconds, from `s-maxage=180`, which a shared cache lets override `max-age=120`. Step 2: the response turned stale when its age reached 180: 450 - 180 = 270 seconds ago. Result: 270 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 23. seed 2534409020668048566, level 1

A cache holds a response with `Cache-Control: max-age=60`. The age of the response is 15 seconds. In how many seconds does the response become stale?

a) 75 seconds
b) 60 seconds
c) 15 seconds
d) 45 seconds

**Key: d**

Explanation: Inputs: `max-age=60`, age 15 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 60 seconds, from `max-age=60`. Step 2: the response turns stale when its age reaches 60: 60 - 15 = 45 seconds from now. Result: 45 seconds. The other options answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 24. seed 1499638506768381735, level 2

A shared cache holds a response with `Cache-Control: max-age=90, s-maxage=180`. The age of the response is 405 seconds. How many seconds ago did the response become stale?

a) 405 seconds
b) 225 seconds
c) 585 seconds
d) 180 seconds

**Key: b**

Explanation: Inputs: `max-age=90`, `s-maxage=180`, age 405 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 180 seconds, from `s-maxage=180`, which a shared cache lets override `max-age=90`. Step 2: the response turned stale when its age reached 180: 405 - 180 = 225 seconds ago. Result: 225 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 25. seed 896185572328210675, level 1

A cache holds a response with `Cache-Control: max-age=60`. The age of the response is 15 seconds. In how many seconds does the response become stale?

a) 15 seconds
b) 45 seconds
c) 75 seconds
d) 60 seconds

**Key: b**

Explanation: Inputs: `max-age=60`, age 15 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 60 seconds, from `max-age=60`. Step 2: the response turns stale when its age reaches 60: 60 - 15 = 45 seconds from now. Result: 45 seconds. The other options answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 26. seed 2594361584511079893, level 2

A shared cache holds a response with `Cache-Control: max-age=90, s-maxage=240`. The age of the response is 375 seconds. How many seconds ago did the response become stale?

a) 135 seconds
b) 375 seconds
c) 615 seconds
d) 285 seconds

**Key: a**

Explanation: Inputs: `max-age=90`, `s-maxage=240`, age 375 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 240 seconds, from `s-maxage=240`, which a shared cache lets override `max-age=90`. Step 2: the response turned stale when its age reached 240: 375 - 240 = 135 seconds ago. Result: 135 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 27. seed 2800397747109933355, level 1

A cache holds a response with `Cache-Control: max-age=60`. The age of the response is 15 seconds. In how many seconds does the response become stale?

a) 15 seconds
b) 60 seconds
c) 45 seconds
d) 75 seconds

**Key: c**

Explanation: Inputs: `max-age=60`, age 15 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 60 seconds, from `max-age=60`. Step 2: the response turns stale when its age reaches 60: 60 - 15 = 45 seconds from now. Result: 45 seconds. The other options answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 28. seed 1834150554611397465, level 2

A shared cache holds a response with `Cache-Control: max-age=600, s-maxage=120`. The age of the response is 330 seconds. How many seconds ago did the response become stale?

a) 210 seconds
b) 120 seconds
c) 330 seconds
d) 600 seconds

**Key: a**

Explanation: Inputs: `max-age=600`, `s-maxage=120`, age 330 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 120 seconds, from `s-maxage=120`, which a shared cache lets override `max-age=600`. Step 2: the response turned stale when its age reached 120: 330 - 120 = 210 seconds ago. Result: 210 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 29. seed 1042915983000038927, level 2

A shared cache holds a response with `Cache-Control: max-age=120, s-maxage=60`. The age of the response is 345 seconds. How many seconds ago did the response become stale?

a) 405 seconds
b) 120 seconds
c) 225 seconds
d) 285 seconds

**Key: d**

Explanation: Inputs: `max-age=120`, `s-maxage=60`, age 345 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 60 seconds, from `s-maxage=60`, which a shared cache lets override `max-age=120`. Step 2: the response turned stale when its age reached 60: 345 - 60 = 285 seconds ago. Result: 285 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 30. seed 2205410160098637400, level 1

A cache holds a response with `Cache-Control: max-age=240`. The age of the response is 135 seconds. In how many seconds does the response become stale?

a) 240 seconds
b) 105 seconds
c) 375 seconds
d) 135 seconds

**Key: b**

Explanation: Inputs: `max-age=240`, age 135 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 240 seconds, from `max-age=240`. Step 2: the response turns stale when its age reaches 240: 240 - 135 = 105 seconds from now. Result: 105 seconds. The other options answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 31. seed 511100676043238427, level 2

A shared cache holds a response with `Cache-Control: max-age=180, s-maxage=300`. The age of the response is 165 seconds. In how many seconds does the response become stale?

a) 180 seconds
b) 465 seconds
c) 135 seconds
d) 300 seconds

**Key: c**

Explanation: Inputs: `max-age=180`, `s-maxage=300`, age 165 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 300 seconds, from `s-maxage=300`, which a shared cache lets override `max-age=180`. Step 2: the response turns stale when its age reaches 300: 300 - 165 = 135 seconds from now. Result: 135 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 32. seed 3265204233779377332, level 2

A shared cache holds a response with `Cache-Control: max-age=600, s-maxage=60`. The age of the response is 15 seconds. In how many seconds does the response become stale?

a) 15 seconds
b) 75 seconds
c) 45 seconds
d) 60 seconds

**Key: c**

Explanation: Inputs: `max-age=600`, `s-maxage=60`, age 15 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 60 seconds, from `s-maxage=60`, which a shared cache lets override `max-age=600`. Step 2: the response turns stale when its age reaches 60: 60 - 15 = 45 seconds from now. Result: 45 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 33. seed 4160750834072342081, level 2

A shared cache holds a response with `Cache-Control: max-age=120, s-maxage=300`. The age of the response is 180 seconds. In how many seconds does the response become stale?

a) 180 seconds
b) 480 seconds
c) 120 seconds
d) 300 seconds

**Key: c**

Explanation: Inputs: `max-age=120`, `s-maxage=300`, age 180 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 300 seconds, from `s-maxage=300`, which a shared cache lets override `max-age=120`. Step 2: the response turns stale when its age reaches 300: 300 - 180 = 120 seconds from now. Result: 120 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 34. seed 4186728001477423103, level 2

A shared cache holds a response with `Cache-Control: max-age=60, s-maxage=90`. The age of the response is 45 seconds. In how many seconds does the response become stale?

a) 90 seconds
b) 60 seconds
c) 45 seconds
d) 15 seconds

**Key: c**

Explanation: Inputs: `max-age=60`, `s-maxage=90`, age 45 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 90 seconds, from `s-maxage=90`, which a shared cache lets override `max-age=60`. Step 2: the response turns stale when its age reaches 90: 90 - 45 = 45 seconds from now. Result: 45 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 35. seed 1897398789510625297, level 2

A shared cache holds a response with `Cache-Control: max-age=300, s-maxage=180`. The age of the response is 420 seconds. How many seconds ago did the response become stale?

a) 120 seconds
b) 420 seconds
c) 300 seconds
d) 240 seconds

**Key: d**

Explanation: Inputs: `max-age=300`, `s-maxage=180`, age 420 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 180 seconds, from `s-maxage=180`, which a shared cache lets override `max-age=300`. Step 2: the response turned stale when its age reached 180: 420 - 180 = 240 seconds ago. Result: 240 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 36. seed 3496208466877734876, level 1

A cache holds a response with `Cache-Control: max-age=240`. The age of the response is 135 seconds. In how many seconds does the response become stale?

a) 240 seconds
b) 135 seconds
c) 105 seconds
d) 375 seconds

**Key: c**

Explanation: Inputs: `max-age=240`, age 135 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 240 seconds, from `max-age=240`. Step 2: the response turns stale when its age reaches 240: 240 - 135 = 105 seconds from now. Result: 105 seconds. The other options answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 37. seed 919419512970802236, level 1

A cache holds a response with `Cache-Control: max-age=300`. The age of the response is 180 seconds. In how many seconds does the response become stale?

a) 300 seconds
b) 480 seconds
c) 180 seconds
d) 120 seconds

**Key: d**

Explanation: Inputs: `max-age=300`, age 180 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 300 seconds, from `max-age=300`. Step 2: the response turns stale when its age reaches 300: 300 - 180 = 120 seconds from now. Result: 120 seconds. The other options answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 38. seed 3217339560882461196, level 2

A shared cache holds a response with `Cache-Control: max-age=120, s-maxage=180`. The age of the response is 345 seconds. How many seconds ago did the response become stale?

a) 165 seconds
b) 525 seconds
c) 225 seconds
d) 120 seconds

**Key: a**

Explanation: Inputs: `max-age=120`, `s-maxage=180`, age 345 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 180 seconds, from `s-maxage=180`, which a shared cache lets override `max-age=120`. Step 2: the response turned stale when its age reached 180: 345 - 180 = 165 seconds ago. Result: 165 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 39. seed 4317667071429277345, level 2

A shared cache holds a response with `Cache-Control: max-age=180, s-maxage=300`. The age of the response is 60 seconds. In how many seconds does the response become stale?

a) 240 seconds
b) 180 seconds
c) 120 seconds
d) 300 seconds

**Key: a**

Explanation: Inputs: `max-age=180`, `s-maxage=300`, age 60 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 300 seconds, from `s-maxage=300`, which a shared cache lets override `max-age=180`. Step 2: the response turns stale when its age reaches 300: 300 - 60 = 240 seconds from now. Result: 240 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 40. seed 2826466456319936504, level 2

A shared cache holds a response with `Cache-Control: max-age=60, s-maxage=180`. The age of the response is 405 seconds. How many seconds ago did the response become stale?

a) 180 seconds
b) 345 seconds
c) 585 seconds
d) 225 seconds

**Key: d**

Explanation: Inputs: `max-age=60`, `s-maxage=180`, age 405 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 180 seconds, from `s-maxage=180`, which a shared cache lets override `max-age=60`. Step 2: the response turned stale when its age reached 180: 405 - 180 = 225 seconds ago. Result: 225 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 41. seed 4551938455260493083, level 2

A shared cache holds a response with `Cache-Control: max-age=240, s-maxage=300`. The age of the response is 75 seconds. In how many seconds does the response become stale?

a) 375 seconds
b) 165 seconds
c) 225 seconds
d) 300 seconds

**Key: c**

Explanation: Inputs: `max-age=240`, `s-maxage=300`, age 75 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 300 seconds, from `s-maxage=300`, which a shared cache lets override `max-age=240`. Step 2: the response turns stale when its age reaches 300: 300 - 75 = 225 seconds from now. Result: 225 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 42. seed 3079992516864054944, level 1

A cache holds a response with `Cache-Control: max-age=60`. The age of the response is 15 seconds. In how many seconds does the response become stale?

a) 60 seconds
b) 15 seconds
c) 75 seconds
d) 45 seconds

**Key: d**

Explanation: Inputs: `max-age=60`, age 15 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 60 seconds, from `max-age=60`. Step 2: the response turns stale when its age reaches 60: 60 - 15 = 45 seconds from now. Result: 45 seconds. The other options answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 43. seed 643601247282846421, level 2

A shared cache holds a response with `Cache-Control: max-age=90, s-maxage=120`. The age of the response is 375 seconds. How many seconds ago did the response become stale?

a) 255 seconds
b) 120 seconds
c) 375 seconds
d) 495 seconds

**Key: a**

Explanation: Inputs: `max-age=90`, `s-maxage=120`, age 375 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 120 seconds, from `s-maxage=120`, which a shared cache lets override `max-age=90`. Step 2: the response turned stale when its age reached 120: 375 - 120 = 255 seconds ago. Result: 255 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 44. seed 3400815373838407252, level 2

A shared cache holds a response with `Cache-Control: max-age=90, s-maxage=300`. The age of the response is 540 seconds. How many seconds ago did the response become stale?

a) 300 seconds
b) 450 seconds
c) 240 seconds
d) 840 seconds

**Key: c**

Explanation: Inputs: `max-age=90`, `s-maxage=300`, age 540 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 300 seconds, from `s-maxage=300`, which a shared cache lets override `max-age=90`. Step 2: the response turned stale when its age reached 300: 540 - 300 = 240 seconds ago. Result: 240 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 45. seed 375836620681958600, level 1

A cache holds a response with `Cache-Control: max-age=240`. The age of the response is 105 seconds. In how many seconds does the response become stale?

a) 345 seconds
b) 240 seconds
c) 105 seconds
d) 135 seconds

**Key: d**

Explanation: Inputs: `max-age=240`, age 105 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 240 seconds, from `max-age=240`. Step 2: the response turns stale when its age reaches 240: 240 - 105 = 135 seconds from now. Result: 135 seconds. The other options answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 46. seed 4200675080516115840, level 2

A shared cache holds a response with `Cache-Control: max-age=300, s-maxage=240`. The age of the response is 480 seconds. How many seconds ago did the response become stale?

a) 480 seconds
b) 240 seconds
c) 720 seconds
d) 300 seconds

**Key: b**

Explanation: Inputs: `max-age=300`, `s-maxage=240`, age 480 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 240 seconds, from `s-maxage=240`, which a shared cache lets override `max-age=300`. Step 2: the response turned stale when its age reached 240: 480 - 240 = 240 seconds ago. Result: 240 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 47. seed 1356037654028494485, level 1

A cache holds a response with `Cache-Control: max-age=600`. The age of the response is 225 seconds. In how many seconds does the response become stale?

a) 600 seconds
b) 825 seconds
c) 225 seconds
d) 375 seconds

**Key: d**

Explanation: Inputs: `max-age=600`, age 225 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 600 seconds, from `max-age=600`. Step 2: the response turns stale when its age reaches 600: 600 - 225 = 375 seconds from now. Result: 375 seconds. The other options answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 48. seed 1731876821434471759, level 2

A shared cache holds a response with `Cache-Control: max-age=600, s-maxage=90`. The age of the response is 330 seconds. How many seconds ago did the response become stale?

a) 330 seconds
b) 600 seconds
c) 240 seconds
d) 420 seconds

**Key: c**

Explanation: Inputs: `max-age=600`, `s-maxage=90`, age 330 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 90 seconds, from `s-maxage=90`, which a shared cache lets override `max-age=600`. Step 2: the response turned stale when its age reached 90: 330 - 90 = 240 seconds ago. Result: 240 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 49. seed 527003501039720687, level 2

A shared cache holds a response with `Cache-Control: max-age=60, s-maxage=180`. The age of the response is 405 seconds. How many seconds ago did the response become stale?

a) 180 seconds
b) 345 seconds
c) 225 seconds
d) 585 seconds

**Key: c**

Explanation: Inputs: `max-age=60`, `s-maxage=180`, age 405 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 180 seconds, from `s-maxage=180`, which a shared cache lets override `max-age=60`. Step 2: the response turned stale when its age reached 180: 405 - 180 = 225 seconds ago. Result: 225 seconds. The other options use `max-age` where `s-maxage` applies, answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.

## 50. seed 3643496714420470649, level 1

A cache holds a response with `Cache-Control: max-age=300`. The age of the response is 180 seconds. In how many seconds does the response become stale?

a) 480 seconds
b) 120 seconds
c) 300 seconds
d) 180 seconds

**Key: b**

Explanation: Inputs: `max-age=300`, age 180 seconds. Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared cache takes the lifetime from `s-maxage` when present, ahead of `max-age`. Step 1: the freshness lifetime is 300 seconds, from `max-age=300`. Step 2: the response turns stale when its age reaches 300: 300 - 180 = 120 seconds from now. Result: 120 seconds. The other options answer with the lifetime or the age alone, or add where they should subtract. Source: `rfc9111#section-4.2`; `rfc9111#section-5.2.2.10`.
