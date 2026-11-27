# Autoscaler desired replicas (`hpa-desired-replicas`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 1046738507122775195, level 1

A HorizontalPodAutoscaler targets an average of `50m` CPU per Pod. 2 Pods currently average `150m`. How many replicas does it ask for?

a) 2
b) 6
c) 4
d) 8

**Key: b**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 150m, desired 50m. Step 1: the ratio is 150 / 50 = 3. Step 2: 2 x 3 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 2. seed 159371177366311548, level 1

A HorizontalPodAutoscaler targets an average of `100m` CPU per Pod. 4 Pods currently average `300m`. How many replicas does it ask for?

a) 16
b) 12
c) 8
d) 4

**Key: b**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 4 replicas, current 300m, desired 100m. Step 1: the ratio is 300 / 100 = 3. Step 2: 4 x 3 = 12. Result: 12 replicas. Source: `k8s-hpa#algorithm-details`.

## 3. seed 940981896495173322, level 1

A HorizontalPodAutoscaler targets an average of `200m` CPU per Pod. 6 Pods currently average `400m`. How many replicas does it ask for?

a) 12
b) 6
c) 2400
d) 18

**Key: a**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 6 replicas, current 400m, desired 200m. Step 1: the ratio is 400 / 200 = 2. Step 2: 6 x 2 = 12. Result: 12 replicas. Source: `k8s-hpa#algorithm-details`.

## 4. seed 1860083390716929339, level 1

A HorizontalPodAutoscaler targets an average of `50m` CPU per Pod. 5 Pods currently average `100m`. How many replicas does it ask for?

a) 10
b) 500
c) 15
d) 2

**Key: a**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 5 replicas, current 100m, desired 50m. Step 1: the ratio is 100 / 50 = 2. Step 2: 5 x 2 = 10. Result: 10 replicas. Source: `k8s-hpa#algorithm-details`.

## 5. seed 1750960137701760461, level 1

A HorizontalPodAutoscaler targets an average of `100m` CPU per Pod. 2 Pods currently average `300m`. How many replicas does it ask for?

a) 4
b) 8
c) 6
d) 2

**Key: c**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 300m, desired 100m. Step 1: the ratio is 300 / 100 = 3. Step 2: 2 x 3 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 6. seed 4297488324564738941, level 1

A HorizontalPodAutoscaler targets an average of `50m` CPU per Pod. 3 Pods currently average `150m`. How many replicas does it ask for?

a) 9
b) 3
c) 1
d) 6

**Key: a**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 3 replicas, current 150m, desired 50m. Step 1: the ratio is 150 / 50 = 3. Step 2: 3 x 3 = 9. Result: 9 replicas. Source: `k8s-hpa#algorithm-details`.

## 7. seed 3605620973647749245, level 1

A HorizontalPodAutoscaler targets an average of `50m` CPU per Pod. 2 Pods currently average `100m`. How many replicas does it ask for?

a) 2
b) 6
c) 4
d) 1

**Key: c**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 100m, desired 50m. Step 1: the ratio is 100 / 50 = 2. Step 2: 2 x 2 = 4. Result: 4 replicas. Source: `k8s-hpa#algorithm-details`.

## 8. seed 3797385006417905270, level 1

A HorizontalPodAutoscaler targets an average of `200m` CPU per Pod. 2 Pods currently average `600m`. How many replicas does it ask for?

a) 8
b) 3
c) 4
d) 6

**Key: d**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 600m, desired 200m. Step 1: the ratio is 600 / 200 = 3. Step 2: 2 x 3 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 9. seed 3518416543851480853, level 1

A HorizontalPodAutoscaler targets an average of `200m` CPU per Pod. 3 Pods currently average `600m`. How many replicas does it ask for?

a) 6
b) 3
c) 9
d) 1

**Key: c**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 3 replicas, current 600m, desired 200m. Step 1: the ratio is 600 / 200 = 3. Step 2: 3 x 3 = 9. Result: 9 replicas. Source: `k8s-hpa#algorithm-details`.

## 10. seed 4338737848828262900, level 1

A HorizontalPodAutoscaler targets an average of `100m` CPU per Pod. 2 Pods currently average `200m`. How many replicas does it ask for?

a) 6
b) 4
c) 2
d) 1

**Key: b**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 200m, desired 100m. Step 1: the ratio is 200 / 100 = 2. Step 2: 2 x 2 = 4. Result: 4 replicas. Source: `k8s-hpa#algorithm-details`.

## 11. seed 2338543487085518126, level 1

A HorizontalPodAutoscaler targets an average of `200m` CPU per Pod. 2 Pods currently average `600m`. How many replicas does it ask for?

a) 4
b) 6
c) 2
d) 8

**Key: b**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 600m, desired 200m. Step 1: the ratio is 600 / 200 = 3. Step 2: 2 x 3 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 12. seed 4011142873034531077, level 1

A HorizontalPodAutoscaler targets an average of `50m` CPU per Pod. 2 Pods currently average `100m`. How many replicas does it ask for?

a) 6
b) 1
c) 2
d) 4

**Key: d**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 100m, desired 50m. Step 1: the ratio is 100 / 50 = 2. Step 2: 2 x 2 = 4. Result: 4 replicas. Source: `k8s-hpa#algorithm-details`.

## 13. seed 1638249785993372871, level 1

A HorizontalPodAutoscaler targets an average of `200m` CPU per Pod. 3 Pods currently average `600m`. How many replicas does it ask for?

a) 9
b) 3
c) 1
d) 6

**Key: a**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 3 replicas, current 600m, desired 200m. Step 1: the ratio is 600 / 200 = 3. Step 2: 3 x 3 = 9. Result: 9 replicas. Source: `k8s-hpa#algorithm-details`.

## 14. seed 375719668902715942, level 1

A HorizontalPodAutoscaler targets an average of `50m` CPU per Pod. 3 Pods currently average `100m`. How many replicas does it ask for?

a) 6
b) 2
c) 3
d) 9

**Key: a**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 3 replicas, current 100m, desired 50m. Step 1: the ratio is 100 / 50 = 2. Step 2: 3 x 2 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 15. seed 1238415112479047332, level 1

A HorizontalPodAutoscaler targets an average of `100m` CPU per Pod. 3 Pods currently average `200m`. How many replicas does it ask for?

a) 2
b) 3
c) 9
d) 6

**Key: d**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 3 replicas, current 200m, desired 100m. Step 1: the ratio is 200 / 100 = 2. Step 2: 3 x 2 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 16. seed 220676068228930428, level 1

A HorizontalPodAutoscaler targets an average of `100m` CPU per Pod. 3 Pods currently average `200m`. How many replicas does it ask for?

a) 2
b) 3
c) 6
d) 9

**Key: c**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 3 replicas, current 200m, desired 100m. Step 1: the ratio is 200 / 100 = 2. Step 2: 3 x 2 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 17. seed 2628685684255368881, level 1

A HorizontalPodAutoscaler targets an average of `50m` CPU per Pod. 3 Pods currently average `100m`. How many replicas does it ask for?

a) 3
b) 2
c) 6
d) 9

**Key: c**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 3 replicas, current 100m, desired 50m. Step 1: the ratio is 100 / 50 = 2. Step 2: 3 x 2 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 18. seed 1394484633511571405, level 1

A HorizontalPodAutoscaler targets an average of `200m` CPU per Pod. 3 Pods currently average `600m`. How many replicas does it ask for?

a) 3
b) 1
c) 9
d) 6

**Key: c**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 3 replicas, current 600m, desired 200m. Step 1: the ratio is 600 / 200 = 3. Step 2: 3 x 3 = 9. Result: 9 replicas. Source: `k8s-hpa#algorithm-details`.

## 19. seed 4562747505693459670, level 1

A HorizontalPodAutoscaler targets an average of `50m` CPU per Pod. 3 Pods currently average `100m`. How many replicas does it ask for?

a) 3
b) 2
c) 9
d) 6

**Key: d**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 3 replicas, current 100m, desired 50m. Step 1: the ratio is 100 / 50 = 2. Step 2: 3 x 2 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 20. seed 4277677172416705049, level 1

A HorizontalPodAutoscaler targets an average of `100m` CPU per Pod. 2 Pods currently average `200m`. How many replicas does it ask for?

a) 2
b) 1
c) 4
d) 6

**Key: c**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 200m, desired 100m. Step 1: the ratio is 200 / 100 = 2. Step 2: 2 x 2 = 4. Result: 4 replicas. Source: `k8s-hpa#algorithm-details`.

## 21. seed 2598677765512259679, level 1

A HorizontalPodAutoscaler targets an average of `50m` CPU per Pod. 5 Pods currently average `100m`. How many replicas does it ask for?

a) 5
b) 15
c) 2
d) 10

**Key: d**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 5 replicas, current 100m, desired 50m. Step 1: the ratio is 100 / 50 = 2. Step 2: 5 x 2 = 10. Result: 10 replicas. Source: `k8s-hpa#algorithm-details`.

## 22. seed 3389238129125685955, level 1

A HorizontalPodAutoscaler targets an average of `200m` CPU per Pod. 3 Pods currently average `600m`. How many replicas does it ask for?

a) 1
b) 9
c) 3
d) 6

**Key: b**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 3 replicas, current 600m, desired 200m. Step 1: the ratio is 600 / 200 = 3. Step 2: 3 x 3 = 9. Result: 9 replicas. Source: `k8s-hpa#algorithm-details`.

## 23. seed 222728276239687003, level 1

A HorizontalPodAutoscaler targets an average of `100m` CPU per Pod. 2 Pods currently average `200m`. How many replicas does it ask for?

a) 4
b) 2
c) 6
d) 1

**Key: a**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 200m, desired 100m. Step 1: the ratio is 200 / 100 = 2. Step 2: 2 x 2 = 4. Result: 4 replicas. Source: `k8s-hpa#algorithm-details`.

## 24. seed 3480307687884416721, level 1

A HorizontalPodAutoscaler targets an average of `50m` CPU per Pod. 2 Pods currently average `100m`. How many replicas does it ask for?

a) 6
b) 1
c) 4
d) 2

**Key: c**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 100m, desired 50m. Step 1: the ratio is 100 / 50 = 2. Step 2: 2 x 2 = 4. Result: 4 replicas. Source: `k8s-hpa#algorithm-details`.

## 25. seed 3911858107282017611, level 1

A HorizontalPodAutoscaler targets an average of `200m` CPU per Pod. 4 Pods currently average `400m`. How many replicas does it ask for?

a) 1600
b) 8
c) 2
d) 4

**Key: b**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 4 replicas, current 400m, desired 200m. Step 1: the ratio is 400 / 200 = 2. Step 2: 4 x 2 = 8. Result: 8 replicas. Source: `k8s-hpa#algorithm-details`.

## 26. seed 4387637473241506981, level 1

A HorizontalPodAutoscaler targets an average of `200m` CPU per Pod. 6 Pods currently average `400m`. How many replicas does it ask for?

a) 6
b) 12
c) 3
d) 2400

**Key: b**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 6 replicas, current 400m, desired 200m. Step 1: the ratio is 400 / 200 = 2. Step 2: 6 x 2 = 12. Result: 12 replicas. Source: `k8s-hpa#algorithm-details`.

## 27. seed 2949238462165725716, level 1

A HorizontalPodAutoscaler targets an average of `200m` CPU per Pod. 4 Pods currently average `400m`. How many replicas does it ask for?

a) 12
b) 4
c) 8
d) 1600

**Key: c**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 4 replicas, current 400m, desired 200m. Step 1: the ratio is 400 / 200 = 2. Step 2: 4 x 2 = 8. Result: 8 replicas. Source: `k8s-hpa#algorithm-details`.

## 28. seed 3084739584196972823, level 1

A HorizontalPodAutoscaler targets an average of `50m` CPU per Pod. 2 Pods currently average `150m`. How many replicas does it ask for?

a) 6
b) 2
c) 3
d) 4

**Key: a**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 150m, desired 50m. Step 1: the ratio is 150 / 50 = 3. Step 2: 2 x 3 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 29. seed 4485371367531129938, level 1

A HorizontalPodAutoscaler targets an average of `50m` CPU per Pod. 3 Pods currently average `100m`. How many replicas does it ask for?

a) 6
b) 3
c) 9
d) 2

**Key: a**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 3 replicas, current 100m, desired 50m. Step 1: the ratio is 100 / 50 = 2. Step 2: 3 x 2 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 30. seed 3863374422338166069, level 1

A HorizontalPodAutoscaler targets an average of `100m` CPU per Pod. 5 Pods currently average `200m`. How many replicas does it ask for?

a) 2
b) 10
c) 15
d) 5

**Key: b**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 5 replicas, current 200m, desired 100m. Step 1: the ratio is 200 / 100 = 2. Step 2: 5 x 2 = 10. Result: 10 replicas. Source: `k8s-hpa#algorithm-details`.

## 31. seed 437753127324722179, level 1

A HorizontalPodAutoscaler targets an average of `200m` CPU per Pod. 3 Pods currently average `600m`. How many replicas does it ask for?

a) 9
b) 6
c) 3
d) 1

**Key: a**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 3 replicas, current 600m, desired 200m. Step 1: the ratio is 600 / 200 = 3. Step 2: 3 x 3 = 9. Result: 9 replicas. Source: `k8s-hpa#algorithm-details`.

## 32. seed 499247782866790198, level 1

A HorizontalPodAutoscaler targets an average of `50m` CPU per Pod. 3 Pods currently average `100m`. How many replicas does it ask for?

a) 2
b) 3
c) 9
d) 6

**Key: d**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 3 replicas, current 100m, desired 50m. Step 1: the ratio is 100 / 50 = 2. Step 2: 3 x 2 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 33. seed 3545167525635094521, level 1

A HorizontalPodAutoscaler targets an average of `100m` CPU per Pod. 2 Pods currently average `300m`. How many replicas does it ask for?

a) 8
b) 3
c) 6
d) 2

**Key: c**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 300m, desired 100m. Step 1: the ratio is 300 / 100 = 3. Step 2: 2 x 3 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 34. seed 3644006947666534414, level 1

A HorizontalPodAutoscaler targets an average of `50m` CPU per Pod. 3 Pods currently average `100m`. How many replicas does it ask for?

a) 6
b) 3
c) 2
d) 9

**Key: a**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 3 replicas, current 100m, desired 50m. Step 1: the ratio is 100 / 50 = 2. Step 2: 3 x 2 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 35. seed 169054990331095398, level 1

A HorizontalPodAutoscaler targets an average of `200m` CPU per Pod. 3 Pods currently average `400m`. How many replicas does it ask for?

a) 9
b) 6
c) 3
d) 2

**Key: b**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 3 replicas, current 400m, desired 200m. Step 1: the ratio is 400 / 200 = 2. Step 2: 3 x 2 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 36. seed 2455971656184904284, level 1

A HorizontalPodAutoscaler targets an average of `100m` CPU per Pod. 4 Pods currently average `200m`. How many replicas does it ask for?

a) 8
b) 12
c) 800
d) 2

**Key: a**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 4 replicas, current 200m, desired 100m. Step 1: the ratio is 200 / 100 = 2. Step 2: 4 x 2 = 8. Result: 8 replicas. Source: `k8s-hpa#algorithm-details`.

## 37. seed 3855605391637330540, level 1

A HorizontalPodAutoscaler targets an average of `50m` CPU per Pod. 2 Pods currently average `150m`. How many replicas does it ask for?

a) 8
b) 2
c) 6
d) 4

**Key: c**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 150m, desired 50m. Step 1: the ratio is 150 / 50 = 3. Step 2: 2 x 3 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 38. seed 3948846335602232955, level 1

A HorizontalPodAutoscaler targets an average of `100m` CPU per Pod. 5 Pods currently average `300m`. How many replicas does it ask for?

a) 15
b) 5
c) 10
d) 3

**Key: a**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 5 replicas, current 300m, desired 100m. Step 1: the ratio is 300 / 100 = 3. Step 2: 5 x 3 = 15. Result: 15 replicas. Source: `k8s-hpa#algorithm-details`.

## 39. seed 4286516449966665403, level 1

A HorizontalPodAutoscaler targets an average of `200m` CPU per Pod. 6 Pods currently average `600m`. How many replicas does it ask for?

a) 24
b) 2
c) 18
d) 12

**Key: c**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 6 replicas, current 600m, desired 200m. Step 1: the ratio is 600 / 200 = 3. Step 2: 6 x 3 = 18. Result: 18 replicas. Source: `k8s-hpa#algorithm-details`.

## 40. seed 4318663453587635521, level 1

A HorizontalPodAutoscaler targets an average of `200m` CPU per Pod. 5 Pods currently average `600m`. How many replicas does it ask for?

a) 15
b) 10
c) 3
d) 5

**Key: a**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 5 replicas, current 600m, desired 200m. Step 1: the ratio is 600 / 200 = 3. Step 2: 5 x 3 = 15. Result: 15 replicas. Source: `k8s-hpa#algorithm-details`.

## 41. seed 2305921015248339351, level 1

A HorizontalPodAutoscaler targets an average of `50m` CPU per Pod. 2 Pods currently average `100m`. How many replicas does it ask for?

a) 2
b) 6
c) 4
d) 1

**Key: c**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 100m, desired 50m. Step 1: the ratio is 100 / 50 = 2. Step 2: 2 x 2 = 4. Result: 4 replicas. Source: `k8s-hpa#algorithm-details`.

## 42. seed 1369134187969494017, level 1

A HorizontalPodAutoscaler targets an average of `200m` CPU per Pod. 2 Pods currently average `400m`. How many replicas does it ask for?

a) 2
b) 1
c) 6
d) 4

**Key: d**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 400m, desired 200m. Step 1: the ratio is 400 / 200 = 2. Step 2: 2 x 2 = 4. Result: 4 replicas. Source: `k8s-hpa#algorithm-details`.

## 43. seed 3284741439649439372, level 1

A HorizontalPodAutoscaler targets an average of `100m` CPU per Pod. 3 Pods currently average `200m`. How many replicas does it ask for?

a) 6
b) 9
c) 2
d) 3

**Key: a**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 3 replicas, current 200m, desired 100m. Step 1: the ratio is 200 / 100 = 2. Step 2: 3 x 2 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 44. seed 1309233928100504377, level 1

A HorizontalPodAutoscaler targets an average of `100m` CPU per Pod. 4 Pods currently average `200m`. How many replicas does it ask for?

a) 8
b) 12
c) 800
d) 2

**Key: a**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 4 replicas, current 200m, desired 100m. Step 1: the ratio is 200 / 100 = 2. Step 2: 4 x 2 = 8. Result: 8 replicas. Source: `k8s-hpa#algorithm-details`.

## 45. seed 1079501110871753119, level 1

A HorizontalPodAutoscaler targets an average of `100m` CPU per Pod. 2 Pods currently average `300m`. How many replicas does it ask for?

a) 3
b) 2
c) 6
d) 4

**Key: c**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 300m, desired 100m. Step 1: the ratio is 300 / 100 = 3. Step 2: 2 x 3 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 46. seed 3557960883329003588, level 1

A HorizontalPodAutoscaler targets an average of `50m` CPU per Pod. 2 Pods currently average `150m`. How many replicas does it ask for?

a) 8
b) 6
c) 4
d) 2

**Key: b**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 150m, desired 50m. Step 1: the ratio is 150 / 50 = 3. Step 2: 2 x 3 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 47. seed 3897038287819461732, level 1

A HorizontalPodAutoscaler targets an average of `100m` CPU per Pod. 5 Pods currently average `300m`. How many replicas does it ask for?

a) 5
b) 10
c) 3
d) 15

**Key: d**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 5 replicas, current 300m, desired 100m. Step 1: the ratio is 300 / 100 = 3. Step 2: 5 x 3 = 15. Result: 15 replicas. Source: `k8s-hpa#algorithm-details`.

## 48. seed 4290492023592630314, level 1

A HorizontalPodAutoscaler targets an average of `100m` CPU per Pod. 2 Pods currently average `200m`. How many replicas does it ask for?

a) 2
b) 1
c) 6
d) 4

**Key: d**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 200m, desired 100m. Step 1: the ratio is 200 / 100 = 2. Step 2: 2 x 2 = 4. Result: 4 replicas. Source: `k8s-hpa#algorithm-details`.

## 49. seed 1697950190124926202, level 1

A HorizontalPodAutoscaler targets an average of `200m` CPU per Pod. 2 Pods currently average `600m`. How many replicas does it ask for?

a) 2
b) 3
c) 6
d) 4

**Key: c**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 600m, desired 200m. Step 1: the ratio is 600 / 200 = 3. Step 2: 2 x 3 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.

## 50. seed 1202550005665428823, level 1

A HorizontalPodAutoscaler targets an average of `200m` CPU per Pod. 2 Pods currently average `600m`. How many replicas does it ask for?

a) 6
b) 4
c) 8
d) 3

**Key: a**

Explanation: Rule: the desired replicas are the current replicas times current metric / desired metric. Inputs: 2 replicas, current 600m, desired 200m. Step 1: the ratio is 600 / 200 = 3. Step 2: 2 x 3 = 6. Result: 6 replicas. Source: `k8s-hpa#algorithm-details`.
