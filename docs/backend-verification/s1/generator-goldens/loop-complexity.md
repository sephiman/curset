# Loop complexity (`loop-complexity`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 1395712313809192518, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int a = 1; a * a <= n; a++) {
        total += a;
    }
}
```

a) Time `O(n log n)`, space `O(1)`
b) Time `O(sqrt n)`, space `O(1)`
c) Time `O(log n)`, space `O(1)`
d) Time `O(n)`, space `O(1)`

**Key: b**

Explanation: Step by step: the loop stops when a * a exceeds n, after about sqrt n iterations. Time is `O(sqrt n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 2. seed 3713444870858108740, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < 8; col++) {
            total += row + col;
        }
    }
}
```

a) Time `O(n)`, space `O(n)`
b) Time `O(n)`, space `O(1)`
c) Time `O(log n)`, space `O(1)`
d) Time `O(1)`, space `O(1)`

**Key: b**

Explanation: Step by step: the inner loop always runs 8 times, a constant, so the cost is 8 * n. Time is `O(n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n^2)` time overcounts: the work does not grow that fast.

## 3. seed 2414972534408054577, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int row = n; row > 0; row /= 3) {
        total += row;
    }
}
```

a) Time `O(n log n)`, space `O(1)`
b) Time `O(log n)`, space `O(1)`
c) Time `O(n)`, space `O(n)`
d) Time `O(n)`, space `O(1)`

**Key: b**

Explanation: Step by step: the counter is divided by 3 each time, so it reaches 0 after about log n steps. Time is `O(log n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 4. seed 62955162742682025, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    List<Integer> out = new ArrayList<>();
    for (int row = 0; row < n; row++) {
        out.add(row * row);
    }
}
```

a) Time `O(log n)`, space `O(n)`
b) Time `O(1)`, space `O(n)`
c) Time `O(n^2)`, space `O(1)`
d) Time `O(n)`, space `O(n)`

**Key: d**

Explanation: Step by step: n iterations, and the list keeps n elements, so space grows with n too. Time is `O(n)`. Space: the structure built keeps a number of elements proportional to n, so the space is linear, which is `O(n)`. Reading it as `O(n^2)` time overcounts: the work does not grow that fast.

## 5. seed 589266046415303656, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int row = n; row > 0; row /= 3) {
        total += row;
    }
}
```

a) Time `O(n)`, space `O(n)`
b) Time `O(log n)`, space `O(1)`
c) Time `O(n log n)`, space `O(1)`
d) Time `O(n)`, space `O(1)`

**Key: b**

Explanation: Step by step: the counter is divided by 3 each time, so it reaches 0 after about log n steps. Time is `O(log n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 6. seed 1941820245854922602, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int p = 0; p < n; p++) {
        total += p;
    }
}
```

a) Time `O(n^2)`, space `O(n)`
b) Time `O(log n)`, space `O(1)`
c) Time `O(n)`, space `O(1)`
d) Time `O(n)`, space `O(n)`

**Key: c**

Explanation: Step by step: one pass of n iterations doing constant work, with a single accumulator. Time is `O(n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n^2)` time overcounts: the work does not grow that fast.

## 7. seed 1276999757354008478, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int i = 1; i * i <= n; i++) {
        total += i;
    }
}
```

a) Time `O(1)`, space `O(1)`
b) Time `O(n)`, space `O(n)`
c) Time `O(sqrt n)`, space `O(1)`
d) Time `O(sqrt n)`, space `O(n)`

**Key: c**

Explanation: Step by step: the loop stops when i * i exceeds n, after about sqrt n iterations. Time is `O(sqrt n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 8. seed 3171472908847757465, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < n; col++) {
            total += row * col;
        }
    }
}
```

a) Time `O(n^2)`, space `O(1)`
b) Time `O(log n)`, space `O(1)`
c) Time `O(1)`, space `O(1)`
d) Time `O(n^2)`, space `O(n)`

**Key: a**

Explanation: Step by step: n outer iterations each run n inner iterations: n * n. Time is `O(n^2)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n log n)` time overcounts: the work does not grow that fast.

## 9. seed 4251725508426834972, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int row = n; row > 0; row /= 3) {
        total += row;
    }
}
```

a) Time `O(log n)`, space `O(n)`
b) Time `O(sqrt n)`, space `O(1)`
c) Time `O(n log n)`, space `O(1)`
d) Time `O(log n)`, space `O(1)`

**Key: d**

Explanation: Step by step: the counter is divided by 3 each time, so it reaches 0 after about log n steps. Time is `O(log n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 10. seed 4132243557074608477, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int a = 0; a < n; a++) {
        total += a;
    }
}
```

a) Time `O(sqrt n)`, space `O(1)`
b) Time `O(n)`, space `O(n)`
c) Time `O(log n)`, space `O(1)`
d) Time `O(n)`, space `O(1)`

**Key: d**

Explanation: Step by step: one pass of n iterations doing constant work, with a single accumulator. Time is `O(n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n^2)` time overcounts: the work does not grow that fast.

## 11. seed 2480185887151543538, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            total += j;
        }
    }
}
```

a) Time `O(n log n)`, space `O(n)`
b) Time `O(sqrt n)`, space `O(1)`
c) Time `O(n^2)`, space `O(1)`
d) Time `O(log n)`, space `O(1)`

**Key: c**

Explanation: Step by step: the inner loop runs 0 + 1 + ... + (n - 1) = n(n - 1)/2 times, which is quadratic. Time is `O(n^2)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n log n)` time overcounts: the work does not grow that fast.

## 12. seed 3399767491943316033, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    List<Integer> out = new ArrayList<>();
    for (int p = 0; p < n; p++) {
        out.add(p * p);
    }
}
```

a) Time `O(n)`, space `O(n)`
b) Time `O(n^2)`, space `O(n)`
c) Time `O(n)`, space `O(1)`
d) Time `O(n^2)`, space `O(1)`

**Key: a**

Explanation: Step by step: n iterations, and the list keeps n elements, so space grows with n too. Time is `O(n)`. Space: the structure built keeps a number of elements proportional to n, so the space is linear, which is `O(n)`. Reading it as `O(n^2)` time overcounts: the work does not grow that fast.

## 13. seed 4421602035734905744, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int a = 1; a < n; a *= 3) {
        for (int b = 0; b < a; b++) {
            total += b;
        }
    }
}
```

a) Time `O(log n)`, space `O(1)`
b) Time `O(1)`, space `O(1)`
c) Time `O(sqrt n)`, space `O(1)`
d) Time `O(n)`, space `O(1)`

**Key: d**

Explanation: Step by step: the inner loop runs 1 + 3 + 3^2 + ... up to n times in total, a geometric sum dominated by its last term, about n. Time is `O(n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n log n)` time overcounts: the work does not grow that fast.

## 14. seed 3526443755928574058, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 8; j++) {
            total += i + j;
        }
    }
}
```

a) Time `O(log n)`, space `O(1)`
b) Time `O(n)`, space `O(1)`
c) Time `O(n)`, space `O(n)`
d) Time `O(sqrt n)`, space `O(1)`

**Key: b**

Explanation: Step by step: the inner loop always runs 8 times, a constant, so the cost is 8 * n. Time is `O(n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n^2)` time overcounts: the work does not grow that fast.

## 15. seed 3554689259081459188, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int i = 0; i < n; i++) {
        total += i;
    }
}
```

a) Time `O(n)`, space `O(1)`
b) Time `O(n^2)`, space `O(n)`
c) Time `O(sqrt n)`, space `O(1)`
d) Time `O(n^2)`, space `O(1)`

**Key: a**

Explanation: Step by step: one pass of n iterations doing constant work, with a single accumulator. Time is `O(n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n^2)` time overcounts: the work does not grow that fast.

## 16. seed 1509456182309423293, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int p = 1; p < n; p *= 2) {
        total += p;
    }
}
```

a) Time `O(log n)`, space `O(1)`
b) Time `O(n)`, space `O(1)`
c) Time `O(1)`, space `O(1)`
d) Time `O(n)`, space `O(n)`

**Key: a**

Explanation: Step by step: the counter is multiplied by 2 each time, so it reaches n after about log n steps. Time is `O(log n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 17. seed 1987729518201366636, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < n; col++) {
            total += row * col;
        }
    }
}
```

a) Time `O(log n)`, space `O(1)`
b) Time `O(n log n)`, space `O(n)`
c) Time `O(n^2)`, space `O(1)`
d) Time `O(n^2)`, space `O(n)`

**Key: c**

Explanation: Step by step: n outer iterations each run n inner iterations: n * n. Time is `O(n^2)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n log n)` time overcounts: the work does not grow that fast.

## 18. seed 4161632303403148436, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int i = 1; i * i <= n; i++) {
        total += i;
    }
}
```

a) Time `O(log n)`, space `O(1)`
b) Time `O(sqrt n)`, space `O(1)`
c) Time `O(n)`, space `O(1)`
d) Time `O(n)`, space `O(n)`

**Key: b**

Explanation: Step by step: the loop stops when i * i exceeds n, after about sqrt n iterations. Time is `O(sqrt n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 19. seed 2048426408115202425, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int row = 1; row * row <= n; row++) {
        total += row;
    }
}
```

a) Time `O(sqrt n)`, space `O(1)`
b) Time `O(sqrt n)`, space `O(n)`
c) Time `O(log n)`, space `O(1)`
d) Time `O(n)`, space `O(1)`

**Key: a**

Explanation: Step by step: the loop stops when row * row exceeds n, after about sqrt n iterations. Time is `O(sqrt n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 20. seed 1105892116975660206, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    List<Integer> out = new ArrayList<>();
    for (int a = 0; a < n; a++) {
        out.add(a * a);
    }
}
```

a) Time `O(n)`, space `O(1)`
b) Time `O(n)`, space `O(n)`
c) Time `O(sqrt n)`, space `O(n)`
d) Time `O(1)`, space `O(n)`

**Key: b**

Explanation: Step by step: n iterations, and the list keeps n elements, so space grows with n too. Time is `O(n)`. Space: the structure built keeps a number of elements proportional to n, so the space is linear, which is `O(n)`. Reading it as `O(n^2)` time overcounts: the work does not grow that fast.

## 21. seed 845057237999039931, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int i = 1; i < n; i *= 3) {
        total += i;
    }
}
```

a) Time `O(log n)`, space `O(n)`
b) Time `O(n log n)`, space `O(1)`
c) Time `O(log n)`, space `O(1)`
d) Time `O(sqrt n)`, space `O(1)`

**Key: c**

Explanation: Step by step: the counter is multiplied by 3 each time, so it reaches n after about log n steps. Time is `O(log n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 22. seed 4282212837736509240, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 8; j++) {
            total += i + j;
        }
    }
}
```

a) Time `O(n)`, space `O(n)`
b) Time `O(n)`, space `O(1)`
c) Time `O(1)`, space `O(1)`
d) Time `O(n^2)`, space `O(1)`

**Key: b**

Explanation: Step by step: the inner loop always runs 8 times, a constant, so the cost is 8 * n. Time is `O(n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n^2)` time overcounts: the work does not grow that fast.

## 23. seed 3834595037151901985, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int a = 1; a < n; a *= 2) {
        for (int b = 0; b < a; b++) {
            total += b;
        }
    }
}
```

a) Time `O(log n)`, space `O(1)`
b) Time `O(n)`, space `O(1)`
c) Time `O(n log n)`, space `O(n)`
d) Time `O(1)`, space `O(1)`

**Key: b**

Explanation: Step by step: the inner loop runs 1 + 2 + 2^2 + ... up to n times in total, a geometric sum dominated by its last term, about n. Time is `O(n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n log n)` time overcounts: the work does not grow that fast.

## 24. seed 4397036287841848489, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int p = 0; p < n; p++) {
        for (int q = 0; q < n; q++) {
            total += p * q;
        }
    }
}
```

a) Time `O(n log n)`, space `O(n)`
b) Time `O(sqrt n)`, space `O(1)`
c) Time `O(n log n)`, space `O(1)`
d) Time `O(n^2)`, space `O(1)`

**Key: d**

Explanation: Step by step: n outer iterations each run n inner iterations: n * n. Time is `O(n^2)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n log n)` time overcounts: the work does not grow that fast.

## 25. seed 3681627347680468585, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int a = 1; a < n; a *= 3) {
        total += a;
    }
}
```

a) Time `O(1)`, space `O(1)`
b) Time `O(n)`, space `O(n)`
c) Time `O(log n)`, space `O(1)`
d) Time `O(n)`, space `O(1)`

**Key: c**

Explanation: Step by step: the counter is multiplied by 3 each time, so it reaches n after about log n steps. Time is `O(log n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 26. seed 4587021565200508706, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int row = 1; row < n; row *= 3) {
        total += row;
    }
}
```

a) Time `O(sqrt n)`, space `O(1)`
b) Time `O(n log n)`, space `O(1)`
c) Time `O(log n)`, space `O(1)`
d) Time `O(log n)`, space `O(n)`

**Key: c**

Explanation: Step by step: the counter is multiplied by 3 each time, so it reaches n after about log n steps. Time is `O(log n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 27. seed 2531893837813297254, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int p = 1; p * p <= n; p++) {
        total += p;
    }
}
```

a) Time `O(1)`, space `O(1)`
b) Time `O(sqrt n)`, space `O(1)`
c) Time `O(log n)`, space `O(1)`
d) Time `O(n)`, space `O(1)`

**Key: b**

Explanation: Step by step: the loop stops when p * p exceeds n, after about sqrt n iterations. Time is `O(sqrt n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 28. seed 3621272371145596929, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int i = 1; i < n; i *= 3) {
        total += i;
    }
}
```

a) Time `O(n)`, space `O(n)`
b) Time `O(n)`, space `O(1)`
c) Time `O(1)`, space `O(1)`
d) Time `O(log n)`, space `O(1)`

**Key: d**

Explanation: Step by step: the counter is multiplied by 3 each time, so it reaches n after about log n steps. Time is `O(log n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 29. seed 4387050895447907613, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            total += j;
        }
    }
}
```

a) Time `O(n log n)`, space `O(1)`
b) Time `O(n^2)`, space `O(1)`
c) Time `O(log n)`, space `O(1)`
d) Time `O(n log n)`, space `O(n)`

**Key: b**

Explanation: Step by step: the inner loop runs 0 + 1 + ... + (n - 1) = n(n - 1)/2 times, which is quadratic. Time is `O(n^2)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n log n)` time overcounts: the work does not grow that fast.

## 30. seed 2490669715179720873, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int a = n; a > 0; a /= 2) {
        total += a;
    }
}
```

a) Time `O(n)`, space `O(n)`
b) Time `O(1)`, space `O(1)`
c) Time `O(n)`, space `O(1)`
d) Time `O(log n)`, space `O(1)`

**Key: d**

Explanation: Step by step: the counter is divided by 2 each time, so it reaches 0 after about log n steps. Time is `O(log n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 31. seed 249935774292454898, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int i = n; i > 0; i /= 2) {
        total += i;
    }
}
```

a) Time `O(n)`, space `O(1)`
b) Time `O(log n)`, space `O(1)`
c) Time `O(1)`, space `O(1)`
d) Time `O(n)`, space `O(n)`

**Key: b**

Explanation: Step by step: the counter is divided by 2 each time, so it reaches 0 after about log n steps. Time is `O(log n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 32. seed 328109300600966861, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    List<Integer> out = new ArrayList<>();
    for (int i = 0; i < n; i++) {
        out.add(i * i);
    }
}
```

a) Time `O(sqrt n)`, space `O(n)`
b) Time `O(1)`, space `O(n)`
c) Time `O(log n)`, space `O(n)`
d) Time `O(n)`, space `O(n)`

**Key: d**

Explanation: Step by step: n iterations, and the list keeps n elements, so space grows with n too. Time is `O(n)`. Space: the structure built keeps a number of elements proportional to n, so the space is linear, which is `O(n)`. Reading it as `O(n^2)` time overcounts: the work does not grow that fast.

## 33. seed 3016168887112671455, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    List<Integer> out = new ArrayList<>();
    for (int row = 0; row < n; row++) {
        out.add(row * row);
    }
}
```

a) Time `O(sqrt n)`, space `O(n)`
b) Time `O(log n)`, space `O(n)`
c) Time `O(1)`, space `O(n)`
d) Time `O(n)`, space `O(n)`

**Key: d**

Explanation: Step by step: n iterations, and the list keeps n elements, so space grows with n too. Time is `O(n)`. Space: the structure built keeps a number of elements proportional to n, so the space is linear, which is `O(n)`. Reading it as `O(n^2)` time overcounts: the work does not grow that fast.

## 34. seed 1888718625970412539, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int row = 1; row < n; row *= 3) {
        total += row;
    }
}
```

a) Time `O(n)`, space `O(1)`
b) Time `O(log n)`, space `O(n)`
c) Time `O(log n)`, space `O(1)`
d) Time `O(sqrt n)`, space `O(1)`

**Key: c**

Explanation: Step by step: the counter is multiplied by 3 each time, so it reaches n after about log n steps. Time is `O(log n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 35. seed 4207321302183519453, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int i = 1; i * i <= n; i++) {
        total += i;
    }
}
```

a) Time `O(1)`, space `O(1)`
b) Time `O(log n)`, space `O(1)`
c) Time `O(sqrt n)`, space `O(1)`
d) Time `O(n)`, space `O(1)`

**Key: c**

Explanation: Step by step: the loop stops when i * i exceeds n, after about sqrt n iterations. Time is `O(sqrt n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 36. seed 537280426215308780, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 8; j++) {
            total += i + j;
        }
    }
}
```

a) Time `O(log n)`, space `O(1)`
b) Time `O(n^2)`, space `O(1)`
c) Time `O(n)`, space `O(1)`
d) Time `O(n)`, space `O(n)`

**Key: c**

Explanation: Step by step: the inner loop always runs 8 times, a constant, so the cost is 8 * n. Time is `O(n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n^2)` time overcounts: the work does not grow that fast.

## 37. seed 3076781379065948658, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < row; col++) {
            total += col;
        }
    }
}
```

a) Time `O(n^2)`, space `O(1)`
b) Time `O(n log n)`, space `O(n)`
c) Time `O(1)`, space `O(1)`
d) Time `O(n log n)`, space `O(1)`

**Key: a**

Explanation: Step by step: the inner loop runs 0 + 1 + ... + (n - 1) = n(n - 1)/2 times, which is quadratic. Time is `O(n^2)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n log n)` time overcounts: the work does not grow that fast.

## 38. seed 2100538611782461661, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int p = n; p > 0; p /= 2) {
        total += p;
    }
}
```

a) Time `O(1)`, space `O(1)`
b) Time `O(log n)`, space `O(1)`
c) Time `O(n)`, space `O(1)`
d) Time `O(n)`, space `O(n)`

**Key: b**

Explanation: Step by step: the counter is divided by 2 each time, so it reaches 0 after about log n steps. Time is `O(log n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 39. seed 1507211588862456606, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int row = n; row > 0; row /= 2) {
        total += row;
    }
}
```

a) Time `O(n)`, space `O(n)`
b) Time `O(log n)`, space `O(1)`
c) Time `O(n)`, space `O(1)`
d) Time `O(1)`, space `O(1)`

**Key: b**

Explanation: Step by step: the counter is divided by 2 each time, so it reaches 0 after about log n steps. Time is `O(log n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 40. seed 534670716310458971, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int p = 0; p < n; p++) {
        for (int q = 0; q < n; q++) {
            total += p * q;
        }
    }
}
```

a) Time `O(n log n)`, space `O(n)`
b) Time `O(n^2)`, space `O(1)`
c) Time `O(n log n)`, space `O(1)`
d) Time `O(log n)`, space `O(1)`

**Key: b**

Explanation: Step by step: n outer iterations each run n inner iterations: n * n. Time is `O(n^2)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n log n)` time overcounts: the work does not grow that fast.

## 41. seed 3421627659497287755, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int p = 0; p < n; p++) {
        for (int q = 0; q < n; q++) {
            total += p * q;
        }
    }
}
```

a) Time `O(n^2)`, space `O(1)`
b) Time `O(sqrt n)`, space `O(1)`
c) Time `O(log n)`, space `O(1)`
d) Time `O(n log n)`, space `O(n)`

**Key: a**

Explanation: Step by step: n outer iterations each run n inner iterations: n * n. Time is `O(n^2)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n log n)` time overcounts: the work does not grow that fast.

## 42. seed 2091335264733776331, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    List<Integer> out = new ArrayList<>();
    for (int i = 0; i < n; i++) {
        out.add(i * i);
    }
}
```

a) Time `O(n^2)`, space `O(1)`
b) Time `O(n)`, space `O(n)`
c) Time `O(sqrt n)`, space `O(n)`
d) Time `O(1)`, space `O(n)`

**Key: b**

Explanation: Step by step: n iterations, and the list keeps n elements, so space grows with n too. Time is `O(n)`. Space: the structure built keeps a number of elements proportional to n, so the space is linear, which is `O(n)`. Reading it as `O(n^2)` time overcounts: the work does not grow that fast.

## 43. seed 1921074550215571146, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            total += j;
        }
    }
}
```

a) Time `O(n log n)`, space `O(1)`
b) Time `O(n^2)`, space `O(n)`
c) Time `O(sqrt n)`, space `O(1)`
d) Time `O(n^2)`, space `O(1)`

**Key: d**

Explanation: Step by step: the inner loop runs 0 + 1 + ... + (n - 1) = n(n - 1)/2 times, which is quadratic. Time is `O(n^2)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n log n)` time overcounts: the work does not grow that fast.

## 44. seed 1659938801877739373, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int row = n; row > 0; row /= 3) {
        total += row;
    }
}
```

a) Time `O(n)`, space `O(n)`
b) Time `O(1)`, space `O(1)`
c) Time `O(n)`, space `O(1)`
d) Time `O(log n)`, space `O(1)`

**Key: d**

Explanation: Step by step: the counter is divided by 3 each time, so it reaches 0 after about log n steps. Time is `O(log n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 45. seed 2521002255987226038, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int a = 0; a < n; a++) {
        for (int b = 1; b < n; b *= 3) {
            total += b;
        }
    }
}
```

a) Time `O(1)`, space `O(1)`
b) Time `O(n^2)`, space `O(n)`
c) Time `O(n log n)`, space `O(1)`
d) Time `O(sqrt n)`, space `O(1)`

**Key: c**

Explanation: Step by step: n outer iterations each run about log n inner ones. Time is `O(n log n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n^2)` time overcounts: the work does not grow that fast.

## 46. seed 3497108359326174972, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int a = 1; a < n; a *= 2) {
        total += a;
    }
}
```

a) Time `O(log n)`, space `O(1)`
b) Time `O(n log n)`, space `O(1)`
c) Time `O(sqrt n)`, space `O(1)`
d) Time `O(log n)`, space `O(n)`

**Key: a**

Explanation: Step by step: the counter is multiplied by 2 each time, so it reaches n after about log n steps. Time is `O(log n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 47. seed 4295181579374669372, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int p = 1; p < n; p *= 2) {
        total += p;
    }
}
```

a) Time `O(log n)`, space `O(1)`
b) Time `O(log n)`, space `O(n)`
c) Time `O(n)`, space `O(n)`
d) Time `O(sqrt n)`, space `O(1)`

**Key: a**

Explanation: Step by step: the counter is multiplied by 2 each time, so it reaches n after about log n steps. Time is `O(log n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n)` time overcounts: the work does not grow that fast.

## 48. seed 1459002348171840141, level 1

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            total += i * j;
        }
    }
}
```

a) Time `O(log n)`, space `O(1)`
b) Time `O(n^2)`, space `O(1)`
c) Time `O(n log n)`, space `O(1)`
d) Time `O(n^2)`, space `O(n)`

**Key: b**

Explanation: Step by step: n outer iterations each run n inner iterations: n * n. Time is `O(n^2)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n log n)` time overcounts: the work does not grow that fast.

## 49. seed 848183075441883322, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < 8; col++) {
            total += row + col;
        }
    }
}
```

a) Time `O(log n)`, space `O(1)`
b) Time `O(n)`, space `O(1)`
c) Time `O(n)`, space `O(n)`
d) Time `O(sqrt n)`, space `O(1)`

**Key: b**

Explanation: Step by step: the inner loop always runs 8 times, a constant, so the cost is 8 * n. Time is `O(n)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n^2)` time overcounts: the work does not grow that fast.

## 50. seed 212063860872448003, level 2

In this Java method, `n` is the input value and every statement in a loop body takes constant time. Counting the memory that stays reachable beyond a few local variables, what are its worst-case time and space complexity?

```java
void run(int n) {
    long total = 0;
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < n; col++) {
            total += row * col;
        }
    }
}
```

a) Time `O(n^2)`, space `O(1)`
b) Time `O(1)`, space `O(1)`
c) Time `O(sqrt n)`, space `O(1)`
d) Time `O(n^2)`, space `O(n)`

**Key: a**

Explanation: Step by step: n outer iterations each run n inner iterations: n * n. Time is `O(n^2)`. Space: no structure grows with n, so the extra space is constant, which is `O(1)`. Reading it as `O(n log n)` time overcounts: the work does not grow that fast.
