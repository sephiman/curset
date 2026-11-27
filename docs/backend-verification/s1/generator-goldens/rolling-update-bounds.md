# Rolling update bounds (`rolling-update-bounds`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 3319370743217300717, level 2

A Deployment with `replicas: 22` rolls out with `maxSurge: 30%` and `maxUnavailable: 30%`. At most how many Pods of the Deployment exist at any moment during the update?

a) 52 Pods
b) 15 Pods
c) 29 Pods
d) 35 Pods

**Key: c**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 22 replicas, surge 30%. Step 1: `maxSurge` 30% of 22 Pods, rounded up, is 7 Pods. Step 2: 22 + 7 = 29. Result: 29 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 2. seed 3257003582455185117, level 1

A Deployment with `replicas: 15` rolls out with `maxSurge: 2` and `maxUnavailable: 1`. At least how many Pods are available at all times during the update?

a) 12 Pods
b) 13 Pods
c) 16 Pods
d) 14 Pods

**Key: d**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 15 replicas, unavailable 1. Step 1: `maxUnavailable` is 1 Pod. Step 2: 15 - 1 = 14. Result: 14 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 3. seed 538308496260827631, level 1

A Deployment with `replicas: 14` rolls out with `maxSurge: 2` and `maxUnavailable: 1`. At least how many Pods are available at all times during the update?

a) 12 Pods
b) 15 Pods
c) 11 Pods
d) 13 Pods

**Key: d**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 14 replicas, unavailable 1. Step 1: `maxUnavailable` is 1 Pod. Step 2: 14 - 1 = 13. Result: 13 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 4. seed 1632131994789651824, level 1

A Deployment with `replicas: 15` rolls out with `maxSurge: 1` and `maxUnavailable: 2`. At most how many Pods of the Deployment exist at any moment during the update?

a) 17 Pods
b) 18 Pods
c) 14 Pods
d) 16 Pods

**Key: d**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 15 replicas, surge 1. Step 1: `maxSurge` is 1 Pod. Step 2: 15 + 1 = 16. Result: 16 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 5. seed 3186112300759397173, level 2

A Deployment with `replicas: 23` rolls out with `maxSurge: 10%` and `maxUnavailable: 10%`. At least how many Pods are available at all times during the update?

a) 13 Pods
b) 18 Pods
c) 25 Pods
d) 21 Pods

**Key: d**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 23 replicas, unavailable 10%. Step 1: `maxUnavailable` 10% of 23 Pods, rounded down, is 2 Pods. Step 2: 23 - 2 = 21. Result: 21 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 6. seed 3761479761041917660, level 2

A Deployment with `replicas: 29` rolls out with `maxSurge: 25%` and `maxUnavailable: 10%`. At least how many Pods are available at all times during the update?

a) 31 Pods
b) 26 Pods
c) 21 Pods
d) 27 Pods

**Key: d**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 29 replicas, unavailable 10%. Step 1: `maxUnavailable` 10% of 29 Pods, rounded down, is 2 Pods. Step 2: 29 - 2 = 27. Result: 27 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 7. seed 848819325191779070, level 1

A Deployment with `replicas: 12` rolls out with `maxSurge: 2` and `maxUnavailable: 1`. At most how many Pods of the Deployment exist at any moment during the update?

a) 15 Pods
b) 10 Pods
c) 14 Pods
d) 13 Pods

**Key: c**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 12 replicas, surge 2. Step 1: `maxSurge` is 2 Pods. Step 2: 12 + 2 = 14. Result: 14 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 8. seed 1468885580426710958, level 1

A Deployment with `replicas: 15` rolls out with `maxSurge: 3` and `maxUnavailable: 1`. At least how many Pods are available at all times during the update?

a) 11 Pods
b) 12 Pods
c) 14 Pods
d) 16 Pods

**Key: c**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 15 replicas, unavailable 1. Step 1: `maxUnavailable` is 1 Pod. Step 2: 15 - 1 = 14. Result: 14 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 9. seed 1412658093904248977, level 1

A Deployment with `replicas: 14` rolls out with `maxSurge: 3` and `maxUnavailable: 1`. At least how many Pods are available at all times during the update?

a) 15 Pods
b) 10 Pods
c) 11 Pods
d) 13 Pods

**Key: d**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 14 replicas, unavailable 1. Step 1: `maxUnavailable` is 1 Pod. Step 2: 14 - 1 = 13. Result: 13 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 10. seed 4335188164764748879, level 1

A Deployment with `replicas: 12` rolls out with `maxSurge: 1` and `maxUnavailable: 2`. At most how many Pods of the Deployment exist at any moment during the update?

a) 14 Pods
b) 13 Pods
c) 11 Pods
d) 15 Pods

**Key: b**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 12 replicas, surge 1. Step 1: `maxSurge` is 1 Pod. Step 2: 12 + 1 = 13. Result: 13 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 11. seed 2304638151055693218, level 1

A Deployment with `replicas: 14` rolls out with `maxSurge: 3` and `maxUnavailable: 1`. At least how many Pods are available at all times during the update?

a) 15 Pods
b) 13 Pods
c) 10 Pods
d) 11 Pods

**Key: b**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 14 replicas, unavailable 1. Step 1: `maxUnavailable` is 1 Pod. Step 2: 14 - 1 = 13. Result: 13 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 12. seed 3287195417583477527, level 2

A Deployment with `replicas: 22` rolls out with `maxSurge: 50%` and `maxUnavailable: 10%`. At least how many Pods are available at all times during the update?

a) 19 Pods
b) 11 Pods
c) 12 Pods
d) 20 Pods

**Key: d**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 22 replicas, unavailable 10%. Step 1: `maxUnavailable` 10% of 22 Pods, rounded down, is 2 Pods. Step 2: 22 - 2 = 20. Result: 20 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 13. seed 1080983084336234798, level 1

A Deployment with `replicas: 14` rolls out with `maxSurge: 2` and `maxUnavailable: 1`. At least how many Pods are available at all times during the update?

a) 15 Pods
b) 13 Pods
c) 12 Pods
d) 11 Pods

**Key: b**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 14 replicas, unavailable 1. Step 1: `maxUnavailable` is 1 Pod. Step 2: 14 - 1 = 13. Result: 13 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 14. seed 4551276807213126811, level 2

A Deployment with `replicas: 22` rolls out with `maxSurge: 10%` and `maxUnavailable: 10%`. At least how many Pods are available at all times during the update?

a) 17 Pods
b) 12 Pods
c) 20 Pods
d) 24 Pods

**Key: c**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 22 replicas, unavailable 10%. Step 1: `maxUnavailable` 10% of 22 Pods, rounded down, is 2 Pods. Step 2: 22 - 2 = 20. Result: 20 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 15. seed 4457791155418105841, level 2

A Deployment with `replicas: 21` rolls out with `maxSurge: 25%` and `maxUnavailable: 25%`. At most how many Pods of the Deployment exist at any moment during the update?

a) 26 Pods
b) 15 Pods
c) 27 Pods
d) 32 Pods

**Key: c**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 21 replicas, surge 25%. Step 1: `maxSurge` 25% of 21 Pods, rounded up, is 6 Pods. Step 2: 21 + 6 = 27. Result: 27 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 16. seed 3515790937811715174, level 1

A Deployment with `replicas: 15` rolls out with `maxSurge: 1` and `maxUnavailable: 2`. At most how many Pods of the Deployment exist at any moment during the update?

a) 14 Pods
b) 17 Pods
c) 16 Pods
d) 18 Pods

**Key: c**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 15 replicas, surge 1. Step 1: `maxSurge` is 1 Pod. Step 2: 15 + 1 = 16. Result: 16 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 17. seed 1677083517139601991, level 2

A Deployment with `replicas: 21` rolls out with `maxSurge: 50%` and `maxUnavailable: 30%`. At least how many Pods are available at all times during the update?

a) 10 Pods
b) 27 Pods
c) 15 Pods
d) 14 Pods

**Key: c**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 21 replicas, unavailable 30%. Step 1: `maxUnavailable` 30% of 21 Pods, rounded down, is 6 Pods. Step 2: 21 - 6 = 15. Result: 15 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 18. seed 3720715674784395567, level 1

A Deployment with `replicas: 14` rolls out with `maxSurge: 2` and `maxUnavailable: 1`. At least how many Pods are available at all times during the update?

a) 15 Pods
b) 13 Pods
c) 12 Pods
d) 11 Pods

**Key: b**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 14 replicas, unavailable 1. Step 1: `maxUnavailable` is 1 Pod. Step 2: 14 - 1 = 13. Result: 13 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 19. seed 4596485021321074537, level 1

A Deployment with `replicas: 13` rolls out with `maxSurge: 2` and `maxUnavailable: 1`. At least how many Pods are available at all times during the update?

a) 12 Pods
b) 10 Pods
c) 11 Pods
d) 14 Pods

**Key: a**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 13 replicas, unavailable 1. Step 1: `maxUnavailable` is 1 Pod. Step 2: 13 - 1 = 12. Result: 12 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 20. seed 2444650910281090214, level 2

A Deployment with `replicas: 21` rolls out with `maxSurge: 30%` and `maxUnavailable: 25%`. At most how many Pods of the Deployment exist at any moment during the update?

a) 14 Pods
b) 27 Pods
c) 51 Pods
d) 28 Pods

**Key: d**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 21 replicas, surge 30%. Step 1: `maxSurge` 30% of 21 Pods, rounded up, is 7 Pods. Step 2: 21 + 7 = 28. Result: 28 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 21. seed 1831860914145754450, level 1

A Deployment with `replicas: 16` rolls out with `maxSurge: 3` and `maxUnavailable: 2`. At most how many Pods of the Deployment exist at any moment during the update?

a) 13 Pods
b) 21 Pods
c) 18 Pods
d) 19 Pods

**Key: d**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 16 replicas, surge 3. Step 1: `maxSurge` is 3 Pods. Step 2: 16 + 3 = 19. Result: 19 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 22. seed 1161773584866507204, level 1

A Deployment with `replicas: 14` rolls out with `maxSurge: 1` and `maxUnavailable: 2`. At least how many Pods are available at all times during the update?

a) 11 Pods
b) 16 Pods
c) 12 Pods
d) 13 Pods

**Key: c**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 14 replicas, unavailable 2. Step 1: `maxUnavailable` is 2 Pods. Step 2: 14 - 2 = 12. Result: 12 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 23. seed 1124461352151839917, level 2

A Deployment with `replicas: 22` rolls out with `maxSurge: 25%` and `maxUnavailable: 50%`. At most how many Pods of the Deployment exist at any moment during the update?

a) 16 Pods
b) 47 Pods
c) 33 Pods
d) 28 Pods

**Key: d**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 22 replicas, surge 25%. Step 1: `maxSurge` 25% of 22 Pods, rounded up, is 6 Pods. Step 2: 22 + 6 = 28. Result: 28 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 24. seed 2265595830689960830, level 1

A Deployment with `replicas: 15` rolls out with `maxSurge: 2` and `maxUnavailable: 1`. At least how many Pods are available at all times during the update?

a) 13 Pods
b) 16 Pods
c) 14 Pods
d) 12 Pods

**Key: c**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 15 replicas, unavailable 1. Step 1: `maxUnavailable` is 1 Pod. Step 2: 15 - 1 = 14. Result: 14 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 25. seed 3160801671108654832, level 1

A Deployment with `replicas: 15` rolls out with `maxSurge: 1` and `maxUnavailable: 2`. At most how many Pods of the Deployment exist at any moment during the update?

a) 14 Pods
b) 17 Pods
c) 18 Pods
d) 16 Pods

**Key: d**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 15 replicas, surge 1. Step 1: `maxSurge` is 1 Pod. Step 2: 15 + 1 = 16. Result: 16 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 26. seed 796498679607459051, level 2

A Deployment with `replicas: 29` rolls out with `maxSurge: 30%` and `maxUnavailable: 10%`. At least how many Pods are available at all times during the update?

a) 18 Pods
b) 27 Pods
c) 19 Pods
d) 31 Pods

**Key: b**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 29 replicas, unavailable 10%. Step 1: `maxUnavailable` 10% of 29 Pods, rounded down, is 2 Pods. Step 2: 29 - 2 = 27. Result: 27 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 27. seed 1911697056327801004, level 1

A Deployment with `replicas: 13` rolls out with `maxSurge: 3` and `maxUnavailable: 2`. At most how many Pods of the Deployment exist at any moment during the update?

a) 16 Pods
b) 15 Pods
c) 18 Pods
d) 10 Pods

**Key: a**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 13 replicas, surge 3. Step 1: `maxSurge` is 3 Pods. Step 2: 13 + 3 = 16. Result: 16 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 28. seed 870872237324500976, level 2

A Deployment with `replicas: 21` rolls out with `maxSurge: 25%` and `maxUnavailable: 30%`. At most how many Pods of the Deployment exist at any moment during the update?

a) 46 Pods
b) 27 Pods
c) 15 Pods
d) 26 Pods

**Key: b**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 21 replicas, surge 25%. Step 1: `maxSurge` 25% of 21 Pods, rounded up, is 6 Pods. Step 2: 21 + 6 = 27. Result: 27 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 29. seed 3729795660770974850, level 1

A Deployment with `replicas: 15` rolls out with `maxSurge: 1` and `maxUnavailable: 2`. At most how many Pods of the Deployment exist at any moment during the update?

a) 14 Pods
b) 18 Pods
c) 17 Pods
d) 16 Pods

**Key: d**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 15 replicas, surge 1. Step 1: `maxSurge` is 1 Pod. Step 2: 15 + 1 = 16. Result: 16 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 30. seed 21416619737121703, level 2

A Deployment with `replicas: 23` rolls out with `maxSurge: 10%` and `maxUnavailable: 10%`. At least how many Pods are available at all times during the update?

a) 18 Pods
b) 25 Pods
c) 20 Pods
d) 21 Pods

**Key: d**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 23 replicas, unavailable 10%. Step 1: `maxUnavailable` 10% of 23 Pods, rounded down, is 2 Pods. Step 2: 23 - 2 = 21. Result: 21 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 31. seed 2822399187119364023, level 2

A Deployment with `replicas: 27` rolls out with `maxSurge: 50%` and `maxUnavailable: 30%`. At most how many Pods of the Deployment exist at any moment during the update?

a) 13 Pods
b) 35 Pods
c) 77 Pods
d) 41 Pods

**Key: d**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 27 replicas, surge 50%. Step 1: `maxSurge` 50% of 27 Pods, rounded up, is 14 Pods. Step 2: 27 + 14 = 41. Result: 41 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 32. seed 1527895457497167116, level 2

A Deployment with `replicas: 21` rolls out with `maxSurge: 25%` and `maxUnavailable: 10%`. At least how many Pods are available at all times during the update?

a) 15 Pods
b) 11 Pods
c) 13 Pods
d) 19 Pods

**Key: d**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 21 replicas, unavailable 10%. Step 1: `maxUnavailable` 10% of 21 Pods, rounded down, is 2 Pods. Step 2: 21 - 2 = 19. Result: 19 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 33. seed 4598484294007960062, level 2

A Deployment with `replicas: 29` rolls out with `maxSurge: 25%` and `maxUnavailable: 30%`. At most how many Pods of the Deployment exist at any moment during the update?

a) 21 Pods
b) 54 Pods
c) 36 Pods
d) 37 Pods

**Key: d**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 29 replicas, surge 25%. Step 1: `maxSurge` 25% of 29 Pods, rounded up, is 8 Pods. Step 2: 29 + 8 = 37. Result: 37 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 34. seed 4119859604536197745, level 2

A Deployment with `replicas: 22` rolls out with `maxSurge: 10%` and `maxUnavailable: 30%`. At least how many Pods are available at all times during the update?

a) 16 Pods
b) 19 Pods
c) 13 Pods
d) 28 Pods

**Key: a**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 22 replicas, unavailable 30%. Step 1: `maxUnavailable` 30% of 22 Pods, rounded down, is 6 Pods. Step 2: 22 - 6 = 16. Result: 16 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 35. seed 4425469799070839414, level 2

A Deployment with `replicas: 26` rolls out with `maxSurge: 10%` and `maxUnavailable: 10%`. At most how many Pods of the Deployment exist at any moment during the update?

a) 28 Pods
b) 29 Pods
c) 36 Pods
d) 23 Pods

**Key: b**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 26 replicas, surge 10%. Step 1: `maxSurge` 10% of 26 Pods, rounded up, is 3 Pods. Step 2: 26 + 3 = 29. Result: 29 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 36. seed 837665357836746166, level 2

A Deployment with `replicas: 29` rolls out with `maxSurge: 10%` and `maxUnavailable: 50%`. At most how many Pods of the Deployment exist at any moment during the update?

a) 32 Pods
b) 39 Pods
c) 43 Pods
d) 26 Pods

**Key: a**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 29 replicas, surge 10%. Step 1: `maxSurge` 10% of 29 Pods, rounded up, is 3 Pods. Step 2: 29 + 3 = 32. Result: 32 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 37. seed 2995953592494299486, level 1

A Deployment with `replicas: 14` rolls out with `maxSurge: 2` and `maxUnavailable: 1`. At most how many Pods of the Deployment exist at any moment during the update?

a) 12 Pods
b) 16 Pods
c) 17 Pods
d) 15 Pods

**Key: b**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 14 replicas, surge 2. Step 1: `maxSurge` is 2 Pods. Step 2: 14 + 2 = 16. Result: 16 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 38. seed 41681845344817901, level 1

A Deployment with `replicas: 13` rolls out with `maxSurge: 3` and `maxUnavailable: 1`. At most how many Pods of the Deployment exist at any moment during the update?

a) 14 Pods
b) 16 Pods
c) 10 Pods
d) 17 Pods

**Key: b**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 13 replicas, surge 3. Step 1: `maxSurge` is 3 Pods. Step 2: 13 + 3 = 16. Result: 16 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 39. seed 1340227293010340995, level 1

A Deployment with `replicas: 13` rolls out with `maxSurge: 3` and `maxUnavailable: 1`. At most how many Pods of the Deployment exist at any moment during the update?

a) 10 Pods
b) 14 Pods
c) 17 Pods
d) 16 Pods

**Key: d**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 13 replicas, surge 3. Step 1: `maxSurge` is 3 Pods. Step 2: 13 + 3 = 16. Result: 16 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 40. seed 3653838823204663582, level 1

A Deployment with `replicas: 13` rolls out with `maxSurge: 2` and `maxUnavailable: 1`. At least how many Pods are available at all times during the update?

a) 14 Pods
b) 12 Pods
c) 10 Pods
d) 11 Pods

**Key: b**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 13 replicas, unavailable 1. Step 1: `maxUnavailable` is 1 Pod. Step 2: 13 - 1 = 12. Result: 12 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 41. seed 4248211764179484102, level 1

A Deployment with `replicas: 16` rolls out with `maxSurge: 3` and `maxUnavailable: 1`. At most how many Pods of the Deployment exist at any moment during the update?

a) 19 Pods
b) 17 Pods
c) 13 Pods
d) 20 Pods

**Key: a**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 16 replicas, surge 3. Step 1: `maxSurge` is 3 Pods. Step 2: 16 + 3 = 19. Result: 19 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 42. seed 3925794102303618342, level 2

A Deployment with `replicas: 27` rolls out with `maxSurge: 50%` and `maxUnavailable: 10%`. At least how many Pods are available at all times during the update?

a) 25 Pods
b) 17 Pods
c) 13 Pods
d) 24 Pods

**Key: a**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 27 replicas, unavailable 10%. Step 1: `maxUnavailable` 10% of 27 Pods, rounded down, is 2 Pods. Step 2: 27 - 2 = 25. Result: 25 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 43. seed 2362435174580878927, level 1

A Deployment with `replicas: 15` rolls out with `maxSurge: 2` and `maxUnavailable: 1`. At most how many Pods of the Deployment exist at any moment during the update?

a) 13 Pods
b) 17 Pods
c) 16 Pods
d) 18 Pods

**Key: b**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 15 replicas, surge 2. Step 1: `maxSurge` is 2 Pods. Step 2: 15 + 2 = 17. Result: 17 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 44. seed 2431167169175159492, level 2

A Deployment with `replicas: 26` rolls out with `maxSurge: 10%` and `maxUnavailable: 50%`. At most how many Pods of the Deployment exist at any moment during the update?

a) 36 Pods
b) 29 Pods
c) 28 Pods
d) 23 Pods

**Key: b**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 26 replicas, surge 10%. Step 1: `maxSurge` 10% of 26 Pods, rounded up, is 3 Pods. Step 2: 26 + 3 = 29. Result: 29 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 45. seed 1915865415001332778, level 1

A Deployment with `replicas: 16` rolls out with `maxSurge: 3` and `maxUnavailable: 1`. At least how many Pods are available at all times during the update?

a) 17 Pods
b) 12 Pods
c) 15 Pods
d) 13 Pods

**Key: c**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 16 replicas, unavailable 1. Step 1: `maxUnavailable` is 1 Pod. Step 2: 16 - 1 = 15. Result: 15 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 46. seed 671105323927324494, level 2

A Deployment with `replicas: 27` rolls out with `maxSurge: 30%` and `maxUnavailable: 30%`. At most how many Pods of the Deployment exist at any moment during the update?

a) 36 Pods
b) 57 Pods
c) 18 Pods
d) 35 Pods

**Key: a**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 27 replicas, surge 30%. Step 1: `maxSurge` 30% of 27 Pods, rounded up, is 9 Pods. Step 2: 27 + 9 = 36. Result: 36 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 47. seed 1047318337758484073, level 2

A Deployment with `replicas: 29` rolls out with `maxSurge: 25%` and `maxUnavailable: 10%`. At least how many Pods are available at all times during the update?

a) 31 Pods
b) 19 Pods
c) 27 Pods
d) 21 Pods

**Key: c**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 29 replicas, unavailable 10%. Step 1: `maxUnavailable` 10% of 29 Pods, rounded down, is 2 Pods. Step 2: 29 - 2 = 27. Result: 27 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 48. seed 1116353244309107702, level 2

A Deployment with `replicas: 21` rolls out with `maxSurge: 10%` and `maxUnavailable: 25%`. At most how many Pods of the Deployment exist at any moment during the update?

a) 23 Pods
b) 31 Pods
c) 24 Pods
d) 26 Pods

**Key: c**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 21 replicas, surge 10%. Step 1: `maxSurge` 10% of 21 Pods, rounded up, is 3 Pods. Step 2: 21 + 3 = 24. Result: 24 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 49. seed 4175207863710263706, level 1

A Deployment with `replicas: 15` rolls out with `maxSurge: 3` and `maxUnavailable: 1`. At most how many Pods of the Deployment exist at any moment during the update?

a) 16 Pods
b) 18 Pods
c) 19 Pods
d) 12 Pods

**Key: b**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 15 replicas, surge 3. Step 1: `maxSurge` is 3 Pods. Step 2: 15 + 3 = 18. Result: 18 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.

## 50. seed 2756168063258751084, level 2

A Deployment with `replicas: 23` rolls out with `maxSurge: 25%` and `maxUnavailable: 10%`. At least how many Pods are available at all times during the update?

a) 17 Pods
b) 13 Pods
c) 21 Pods
d) 20 Pods

**Key: c**

Explanation: Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down. Inputs: 23 replicas, unavailable 10%. Step 1: `maxUnavailable` 10% of 23 Pods, rounded down, is 2 Pods. Step 2: 23 - 2 = 21. Result: 21 Pods. Source: `k8s-deployment#max-surge`; `k8s-deployment#max-unavailable`.
