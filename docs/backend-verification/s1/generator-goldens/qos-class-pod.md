# Pod QoS class (`qos-class-pod`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 231092101682521560, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 500m/500m, memory 1Gi/1Gi`
b) `cpu none/none, memory none/none`
c) `cpu 250m/none, memory 128Mi/none`
d) `cpu none/none, memory 128Mi/128Mi`

**Key: a**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 500m/500m, memory 1Gi/1Gi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 250m/none, memory 128Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 3: `cpu none/none, memory 128Mi/128Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 4: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Result: `cpu 500m/500m, memory 1Gi/1Gi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 2. seed 884765548072347348, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 50m/250m, memory 512Mi/1Gi`
b) `cpu none/none, memory none/none`
c) `cpu 50m/none, memory 256Mi/none`
d) `cpu 50m/50m, memory 1Gi/1Gi`

**Key: d**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 1Gi/1Gi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 50m/none, memory 256Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 3: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 4: `cpu 50m/250m, memory 512Mi/1Gi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Result: `cpu 50m/50m, memory 1Gi/1Gi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 3. seed 4559862848431153188, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 500m/500m, memory 512Mi/512Mi`
b) `cpu none/none, memory none/none`
c) `cpu 50m/250m, memory 256Mi/512Mi`
d) `cpu 1000m/none, memory 256Mi/none`

**Key: a**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 500m/500m, memory 512Mi/512Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 1000m/none, memory 256Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 3: `cpu 50m/250m, memory 256Mi/512Mi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 4: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Result: `cpu 500m/500m, memory 512Mi/512Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 4. seed 997727515371032107, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu none/none, memory 512Mi/512Mi`
b) `cpu none/none, memory none/none`
c) `cpu 50m/50m, memory 256Mi/256Mi`
d) `cpu 1000m/none, memory 128Mi/none`

**Key: c**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 256Mi/256Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 3: `cpu 1000m/none, memory 128Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 4: `cpu none/none, memory 512Mi/512Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Result: `cpu 50m/50m, memory 256Mi/256Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 5. seed 2056198074910506013, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu none/none, memory 128Mi/128Mi`
b) `cpu none/none, memory none/none`
c) `cpu 250m/250m, memory 128Mi/128Mi`
d) `cpu 250m/none, memory 512Mi/none`

**Key: c**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 250m/250m, memory 128Mi/128Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 250m/none, memory 512Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 3: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 4: `cpu none/none, memory 128Mi/128Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Result: `cpu 250m/250m, memory 128Mi/128Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 6. seed 728370809716097875, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu none/none, memory 256Mi/256Mi`
b) `cpu 50m/50m, memory 512Mi/512Mi`
c) `cpu none/none, memory none/none`
d) `cpu 500m/1000m, memory 512Mi/1Gi`

**Key: b**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 512Mi/512Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 3: `cpu 500m/1000m, memory 512Mi/1Gi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 4: `cpu none/none, memory 256Mi/256Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Result: `cpu 50m/50m, memory 512Mi/512Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 7. seed 407712386991553520, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu none/none, memory none/none`
b) `cpu 1000m/none, memory 256Mi/none`
c) `cpu 50m/50m, memory 512Mi/512Mi`
d) `cpu none/none, memory 512Mi/512Mi`

**Key: c**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 512Mi/512Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory 512Mi/512Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 3: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 4: `cpu 1000m/none, memory 256Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Result: `cpu 50m/50m, memory 512Mi/512Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 8. seed 2674511634960596949, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 500m/500m, memory 1Gi/1Gi`
b) `cpu none/none, memory none/none`
c) `cpu none/none, memory 128Mi/128Mi`
d) `cpu 50m/250m, memory 512Mi/1Gi`

**Key: a**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 500m/500m, memory 1Gi/1Gi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory 128Mi/128Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 3: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 4: `cpu 50m/250m, memory 512Mi/1Gi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Result: `cpu 500m/500m, memory 1Gi/1Gi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 9. seed 2454692707276208931, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 1000m/none, memory 128Mi/none`
b) `cpu none/none, memory 1Gi/1Gi`
c) `cpu 50m/50m, memory 256Mi/256Mi`
d) `cpu 500m/1000m, memory 128Mi/256Mi`

**Key: c**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 256Mi/256Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 500m/1000m, memory 128Mi/256Mi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 3: `cpu none/none, memory 1Gi/1Gi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 4: `cpu 1000m/none, memory 128Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Result: `cpu 50m/50m, memory 256Mi/256Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 10. seed 4475651640295675207, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 500m/1000m, memory 128Mi/256Mi`
b) `cpu none/none, memory none/none`
c) `cpu none/none, memory 1Gi/1Gi`
d) `cpu 250m/250m, memory 1Gi/1Gi`

**Key: d**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 250m/250m, memory 1Gi/1Gi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 3: `cpu none/none, memory 1Gi/1Gi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 4: `cpu 500m/1000m, memory 128Mi/256Mi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Result: `cpu 250m/250m, memory 1Gi/1Gi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 11. seed 4321207597870768973, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 250m/250m, memory 1Gi/1Gi`
b) `cpu 250m/500m, memory 128Mi/256Mi`
c) `cpu none/none, memory 256Mi/256Mi`
d) `cpu none/none, memory none/none`

**Key: a**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 250m/250m, memory 1Gi/1Gi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 3: `cpu 250m/500m, memory 128Mi/256Mi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 4: `cpu none/none, memory 256Mi/256Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Result: `cpu 250m/250m, memory 1Gi/1Gi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 12. seed 1125930340257492970, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 250m/none, memory 512Mi/none`
b) `cpu none/none, memory none/none`
c) `cpu 500m/500m, memory 256Mi/256Mi`
d) `cpu none/none, memory 1Gi/1Gi`

**Key: c**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 500m/500m, memory 256Mi/256Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 3: `cpu none/none, memory 1Gi/1Gi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 4: `cpu 250m/none, memory 512Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Result: `cpu 500m/500m, memory 256Mi/256Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 13. seed 2642321861825637458, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu none/none, memory none/none`
b) `cpu 250m/250m, memory 1Gi/1Gi`
c) `cpu 50m/250m, memory 512Mi/1Gi`
d) `cpu 500m/none, memory 1Gi/none`

**Key: b**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 250m/250m, memory 1Gi/1Gi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 500m/none, memory 1Gi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 3: `cpu 50m/250m, memory 512Mi/1Gi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 4: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Result: `cpu 250m/250m, memory 1Gi/1Gi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 14. seed 449729676731531500, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu none/none, memory none/none`
b) `cpu none/none, memory 256Mi/256Mi`
c) `cpu 250m/500m, memory 512Mi/1Gi`
d) `cpu 500m/500m, memory 256Mi/256Mi`

**Key: d**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 500m/500m, memory 256Mi/256Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory 256Mi/256Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 3: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 4: `cpu 250m/500m, memory 512Mi/1Gi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Result: `cpu 500m/500m, memory 256Mi/256Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 15. seed 3922750434877710647, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 500m/none, memory 1Gi/none`
b) `cpu none/none, memory 512Mi/512Mi`
c) `cpu none/none, memory none/none`
d) `cpu 50m/50m, memory 1Gi/1Gi`

**Key: d**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 1Gi/1Gi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory 512Mi/512Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 3: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 4: `cpu 500m/none, memory 1Gi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Result: `cpu 50m/50m, memory 1Gi/1Gi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 16. seed 1673698188239056708, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 1000m/none, memory 256Mi/none`
b) `cpu 500m/500m, memory 256Mi/256Mi`
c) `cpu none/none, memory none/none`
d) `cpu 500m/1000m, memory 128Mi/256Mi`

**Key: b**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 500m/500m, memory 256Mi/256Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 500m/1000m, memory 128Mi/256Mi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 3: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 4: `cpu 1000m/none, memory 256Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Result: `cpu 500m/500m, memory 256Mi/256Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 17. seed 2989198602510774113, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu none/none, memory 128Mi/128Mi`
b) `cpu 250m/250m, memory 256Mi/256Mi`
c) `cpu none/none, memory none/none`
d) `cpu 1000m/none, memory 256Mi/none`

**Key: b**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 250m/250m, memory 256Mi/256Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 3: `cpu none/none, memory 128Mi/128Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 4: `cpu 1000m/none, memory 256Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Result: `cpu 250m/250m, memory 256Mi/256Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 18. seed 3548836214470993244, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 250m/500m, memory 128Mi/256Mi`
b) `cpu none/none, memory 256Mi/256Mi`
c) `cpu 50m/50m, memory 1Gi/1Gi`
d) `cpu 50m/none, memory 1Gi/none`

**Key: c**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 1Gi/1Gi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 250m/500m, memory 128Mi/256Mi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 3: `cpu none/none, memory 256Mi/256Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 4: `cpu 50m/none, memory 1Gi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Result: `cpu 50m/50m, memory 1Gi/1Gi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 19. seed 1464731210914342701, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 50m/250m, memory 256Mi/512Mi`
b) `cpu none/none, memory 128Mi/128Mi`
c) `cpu 1000m/none, memory 512Mi/none`
d) `cpu 1000m/1000m, memory 1Gi/1Gi`

**Key: d**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 1000m/1000m, memory 1Gi/1Gi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory 128Mi/128Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 3: `cpu 1000m/none, memory 512Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 4: `cpu 50m/250m, memory 256Mi/512Mi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Result: `cpu 1000m/1000m, memory 1Gi/1Gi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 20. seed 847465656438544925, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 500m/none, memory 512Mi/none`
b) `cpu none/none, memory 128Mi/128Mi`
c) `cpu 1000m/1000m, memory 512Mi/512Mi`
d) `cpu 250m/500m, memory 256Mi/512Mi`

**Key: c**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 1000m/1000m, memory 512Mi/512Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 500m/none, memory 512Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 3: `cpu none/none, memory 128Mi/128Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 4: `cpu 250m/500m, memory 256Mi/512Mi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Result: `cpu 1000m/1000m, memory 512Mi/512Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 21. seed 2581113514544713071, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 500m/1000m, memory 512Mi/1Gi`
b) `cpu 50m/50m, memory 256Mi/256Mi`
c) `cpu none/none, memory 128Mi/128Mi`
d) `cpu none/none, memory none/none`

**Key: b**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 256Mi/256Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 500m/1000m, memory 512Mi/1Gi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 3: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 4: `cpu none/none, memory 128Mi/128Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Result: `cpu 50m/50m, memory 256Mi/256Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 22. seed 4329163740412236244, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 500m/none, memory 256Mi/none`
b) `cpu none/none, memory 1Gi/1Gi`
c) `cpu 250m/500m, memory 256Mi/512Mi`
d) `cpu 50m/50m, memory 128Mi/128Mi`

**Key: d**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 128Mi/128Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 500m/none, memory 256Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 3: `cpu 250m/500m, memory 256Mi/512Mi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 4: `cpu none/none, memory 1Gi/1Gi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Result: `cpu 50m/50m, memory 128Mi/128Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 23. seed 1408978476151512308, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 50m/none, memory 1Gi/none`
b) `cpu none/none, memory none/none`
c) `cpu 500m/1000m, memory 128Mi/256Mi`
d) `cpu 250m/250m, memory 256Mi/256Mi`

**Key: d**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 250m/250m, memory 256Mi/256Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 50m/none, memory 1Gi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 3: `cpu 500m/1000m, memory 128Mi/256Mi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 4: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Result: `cpu 250m/250m, memory 256Mi/256Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 24. seed 3021301549458029435, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu none/none, memory 128Mi/128Mi`
b) `cpu none/none, memory none/none`
c) `cpu 1000m/1000m, memory 512Mi/512Mi`
d) `cpu 50m/none, memory 128Mi/none`

**Key: c**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 1000m/1000m, memory 512Mi/512Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory 128Mi/128Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 3: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 4: `cpu 50m/none, memory 128Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Result: `cpu 1000m/1000m, memory 512Mi/512Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 25. seed 1913634576980533549, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 50m/50m, memory 256Mi/256Mi`
b) `cpu none/none, memory none/none`
c) `cpu 250m/500m, memory 128Mi/256Mi`
d) `cpu 1000m/none, memory 128Mi/none`

**Key: a**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 256Mi/256Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 3: `cpu 1000m/none, memory 128Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 4: `cpu 250m/500m, memory 128Mi/256Mi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Result: `cpu 50m/50m, memory 256Mi/256Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 26. seed 267205078064686935, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu none/none, memory none/none`
b) `cpu 250m/500m, memory 128Mi/256Mi`
c) `cpu 50m/none, memory 128Mi/none`
d) `cpu 1000m/1000m, memory 1Gi/1Gi`

**Key: d**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 1000m/1000m, memory 1Gi/1Gi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 50m/none, memory 128Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 3: `cpu 250m/500m, memory 128Mi/256Mi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 4: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Result: `cpu 1000m/1000m, memory 1Gi/1Gi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 27. seed 1283483517294567883, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 250m/none, memory 256Mi/none`
b) `cpu none/none, memory none/none`
c) `cpu none/none, memory 1Gi/1Gi`
d) `cpu 1000m/1000m, memory 256Mi/256Mi`

**Key: d**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 1000m/1000m, memory 256Mi/256Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory 1Gi/1Gi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 3: `cpu 250m/none, memory 256Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 4: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Result: `cpu 1000m/1000m, memory 256Mi/256Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 28. seed 4537465088650549773, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 250m/500m, memory 256Mi/512Mi`
b) `cpu none/none, memory none/none`
c) `cpu 250m/none, memory 256Mi/none`
d) `cpu 500m/500m, memory 128Mi/128Mi`

**Key: d**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 500m/500m, memory 128Mi/128Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 3: `cpu 250m/500m, memory 256Mi/512Mi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 4: `cpu 250m/none, memory 256Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Result: `cpu 500m/500m, memory 128Mi/128Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 29. seed 2478087108097432560, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu none/none, memory 512Mi/512Mi`
b) `cpu 500m/500m, memory 1Gi/1Gi`
c) `cpu 500m/1000m, memory 512Mi/1Gi`
d) `cpu none/none, memory none/none`

**Key: b**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 500m/500m, memory 1Gi/1Gi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory 512Mi/512Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 3: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 4: `cpu 500m/1000m, memory 512Mi/1Gi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Result: `cpu 500m/500m, memory 1Gi/1Gi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 30. seed 563418246502017284, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 500m/1000m, memory 512Mi/1Gi`
b) `cpu none/none, memory none/none`
c) `cpu none/none, memory 512Mi/512Mi`
d) `cpu 250m/250m, memory 128Mi/128Mi`

**Key: d**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 250m/250m, memory 128Mi/128Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 500m/1000m, memory 512Mi/1Gi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 3: `cpu none/none, memory 512Mi/512Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 4: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Result: `cpu 250m/250m, memory 128Mi/128Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 31. seed 2617700052084049304, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu none/none, memory 256Mi/256Mi`
b) `cpu 1000m/1000m, memory 1Gi/1Gi`
c) `cpu none/none, memory none/none`
d) `cpu 500m/none, memory 256Mi/none`

**Key: b**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 1000m/1000m, memory 1Gi/1Gi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory 256Mi/256Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 3: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 4: `cpu 500m/none, memory 256Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Result: `cpu 1000m/1000m, memory 1Gi/1Gi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 32. seed 980236857798706264, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 500m/1000m, memory 512Mi/1Gi`
b) `cpu none/none, memory none/none`
c) `cpu none/none, memory 128Mi/128Mi`
d) `cpu 50m/50m, memory 128Mi/128Mi`

**Key: d**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 128Mi/128Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory 128Mi/128Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 3: `cpu 500m/1000m, memory 512Mi/1Gi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 4: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Result: `cpu 50m/50m, memory 128Mi/128Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 33. seed 3043837744794065335, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu none/none, memory 1Gi/1Gi`
b) `cpu 250m/250m, memory 1Gi/1Gi`
c) `cpu 50m/none, memory 256Mi/none`
d) `cpu none/none, memory none/none`

**Key: b**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 250m/250m, memory 1Gi/1Gi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 3: `cpu 50m/none, memory 256Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 4: `cpu none/none, memory 1Gi/1Gi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Result: `cpu 250m/250m, memory 1Gi/1Gi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 34. seed 3033699677204213931, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 250m/250m, memory 1Gi/1Gi`
b) `cpu 250m/500m, memory 256Mi/512Mi`
c) `cpu 1000m/none, memory 1Gi/none`
d) `cpu none/none, memory 128Mi/128Mi`

**Key: a**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 250m/250m, memory 1Gi/1Gi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 250m/500m, memory 256Mi/512Mi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 3: `cpu none/none, memory 128Mi/128Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 4: `cpu 1000m/none, memory 1Gi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Result: `cpu 250m/250m, memory 1Gi/1Gi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 35. seed 4117314475623181325, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 50m/none, memory 128Mi/none`
b) `cpu 1000m/1000m, memory 1Gi/1Gi`
c) `cpu 250m/500m, memory 512Mi/1Gi`
d) `cpu none/none, memory none/none`

**Key: b**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 1000m/1000m, memory 1Gi/1Gi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 50m/none, memory 128Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 3: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 4: `cpu 250m/500m, memory 512Mi/1Gi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Result: `cpu 1000m/1000m, memory 1Gi/1Gi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 36. seed 2875047015109942039, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu none/none, memory 512Mi/512Mi`
b) `cpu 50m/50m, memory 1Gi/1Gi`
c) `cpu 250m/500m, memory 512Mi/1Gi`
d) `cpu none/none, memory none/none`

**Key: b**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 1Gi/1Gi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 250m/500m, memory 512Mi/1Gi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 3: `cpu none/none, memory 512Mi/512Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 4: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Result: `cpu 50m/50m, memory 1Gi/1Gi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 37. seed 442425905305046010, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 500m/1000m, memory 512Mi/1Gi`
b) `cpu none/none, memory 1Gi/1Gi`
c) `cpu 50m/50m, memory 256Mi/256Mi`
d) `cpu none/none, memory none/none`

**Key: c**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 256Mi/256Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory 1Gi/1Gi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 3: `cpu 500m/1000m, memory 512Mi/1Gi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 4: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Result: `cpu 50m/50m, memory 256Mi/256Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 38. seed 895514386233432723, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu none/none, memory 512Mi/512Mi`
b) `cpu 50m/none, memory 1Gi/none`
c) `cpu 250m/500m, memory 512Mi/1Gi`
d) `cpu 250m/250m, memory 1Gi/1Gi`

**Key: d**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 250m/250m, memory 1Gi/1Gi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 50m/none, memory 1Gi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 3: `cpu none/none, memory 512Mi/512Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 4: `cpu 250m/500m, memory 512Mi/1Gi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Result: `cpu 250m/250m, memory 1Gi/1Gi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 39. seed 3139902577001924388, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu none/none, memory none/none`
b) `cpu 50m/50m, memory 512Mi/512Mi`
c) `cpu 50m/250m, memory 512Mi/1Gi`
d) `cpu none/none, memory 128Mi/128Mi`

**Key: b**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 512Mi/512Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 50m/250m, memory 512Mi/1Gi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 3: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 4: `cpu none/none, memory 128Mi/128Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Result: `cpu 50m/50m, memory 512Mi/512Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 40. seed 2925571940767810873, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 500m/500m, memory 128Mi/128Mi`
b) `cpu 500m/none, memory 512Mi/none`
c) `cpu none/none, memory 128Mi/128Mi`
d) `cpu 50m/250m, memory 512Mi/1Gi`

**Key: a**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 500m/500m, memory 128Mi/128Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 500m/none, memory 512Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 3: `cpu none/none, memory 128Mi/128Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 4: `cpu 50m/250m, memory 512Mi/1Gi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Result: `cpu 500m/500m, memory 128Mi/128Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 41. seed 2011814924839957283, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 250m/none, memory 1Gi/none`
b) `cpu none/none, memory none/none`
c) `cpu none/none, memory 512Mi/512Mi`
d) `cpu 50m/50m, memory 256Mi/256Mi`

**Key: d**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 256Mi/256Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 3: `cpu none/none, memory 512Mi/512Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 4: `cpu 250m/none, memory 1Gi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Result: `cpu 50m/50m, memory 256Mi/256Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 42. seed 629892266422990004, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 50m/50m, memory 256Mi/256Mi`
b) `cpu 500m/1000m, memory 256Mi/512Mi`
c) `cpu none/none, memory 512Mi/512Mi`
d) `cpu 250m/none, memory 512Mi/none`

**Key: a**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 256Mi/256Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 250m/none, memory 512Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 3: `cpu none/none, memory 512Mi/512Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 4: `cpu 500m/1000m, memory 256Mi/512Mi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Result: `cpu 50m/50m, memory 256Mi/256Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 43. seed 4475753339962562567, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 1000m/none, memory 512Mi/none`
b) `cpu 50m/250m, memory 256Mi/512Mi`
c) `cpu 500m/500m, memory 512Mi/512Mi`
d) `cpu none/none, memory 512Mi/512Mi`

**Key: c**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 500m/500m, memory 512Mi/512Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 50m/250m, memory 256Mi/512Mi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 3: `cpu 1000m/none, memory 512Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 4: `cpu none/none, memory 512Mi/512Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Result: `cpu 500m/500m, memory 512Mi/512Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 44. seed 4357037439822562636, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu none/none, memory 256Mi/256Mi`
b) `cpu none/none, memory none/none`
c) `cpu 1000m/none, memory 128Mi/none`
d) `cpu 50m/50m, memory 512Mi/512Mi`

**Key: d**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 512Mi/512Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 3: `cpu 1000m/none, memory 128Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 4: `cpu none/none, memory 256Mi/256Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Result: `cpu 50m/50m, memory 512Mi/512Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 45. seed 1924706066200330126, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 250m/250m, memory 256Mi/256Mi`
b) `cpu 500m/none, memory 256Mi/none`
c) `cpu none/none, memory none/none`
d) `cpu none/none, memory 1Gi/1Gi`

**Key: a**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 250m/250m, memory 256Mi/256Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 3: `cpu 500m/none, memory 256Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 4: `cpu none/none, memory 1Gi/1Gi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Result: `cpu 250m/250m, memory 256Mi/256Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 46. seed 2835995711980983391, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu none/none, memory none/none`
b) `cpu 250m/none, memory 512Mi/none`
c) `cpu 250m/500m, memory 128Mi/256Mi`
d) `cpu 50m/50m, memory 512Mi/512Mi`

**Key: d**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 512Mi/512Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 3: `cpu 250m/500m, memory 128Mi/256Mi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 4: `cpu 250m/none, memory 512Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Result: `cpu 50m/50m, memory 512Mi/512Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 47. seed 352951265533800470, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 500m/1000m, memory 512Mi/1Gi`
b) `cpu none/none, memory 128Mi/128Mi`
c) `cpu none/none, memory none/none`
d) `cpu 50m/50m, memory 128Mi/128Mi`

**Key: d**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 128Mi/128Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 500m/1000m, memory 512Mi/1Gi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 3: `cpu none/none, memory 128Mi/128Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Step 4: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Result: `cpu 50m/50m, memory 128Mi/128Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 48. seed 3811111540767487505, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 50m/250m, memory 128Mi/256Mi`
b) `cpu none/none, memory none/none`
c) `cpu 1000m/none, memory 128Mi/none`
d) `cpu 250m/250m, memory 1Gi/1Gi`

**Key: d**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 250m/250m, memory 1Gi/1Gi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 3: `cpu 50m/250m, memory 128Mi/256Mi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 4: `cpu 1000m/none, memory 128Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Result: `cpu 250m/250m, memory 1Gi/1Gi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 49. seed 1404759509233144731, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 1000m/1000m, memory 128Mi/128Mi`
b) `cpu 500m/none, memory 1Gi/none`
c) `cpu 250m/500m, memory 128Mi/256Mi`
d) `cpu none/none, memory none/none`

**Key: a**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 1000m/1000m, memory 128Mi/128Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu 500m/none, memory 1Gi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 3: `cpu 250m/500m, memory 128Mi/256Mi` is `Burstable`, because its requests are below the limits, but each limit must equal its request. Step 4: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Result: `cpu 1000m/1000m, memory 128Mi/128Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.

## 50. seed 404869114901842773, level 1

Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as request/limit, with `none` for unset. Which Pod gets the `Guaranteed` class?

a) `cpu 50m/50m, memory 256Mi/256Mi`
b) `cpu none/none, memory 512Mi/512Mi`
c) `cpu none/none, memory none/none`
d) `cpu 250m/none, memory 256Mi/none`

**Key: a**

Explanation: Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, all greater than zero and each limit equal to its request; `BestEffort` when no container sets any CPU or memory request or limit; `Burstable` otherwise. Step 1: `cpu 50m/50m, memory 256Mi/256Mi` is `Guaranteed`, because every container has equal non-zero CPU and memory requests and limits. Step 2: `cpu none/none, memory none/none` is `BestEffort`, because no container sets any request or limit. Step 3: `cpu 250m/none, memory 256Mi/none` is `Burstable`, because it has no limits, but a CPU and a memory limit must be set. Step 4: `cpu none/none, memory 512Mi/512Mi` is `Burstable`, because it has no CPU request or limit, but CPU and memory must both be set. Result: `cpu 50m/50m, memory 256Mi/256Mi`. Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.
