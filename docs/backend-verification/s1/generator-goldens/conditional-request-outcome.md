# If-None-Match outcomes (`conditional-request-outcome`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 625447138837461318, level 2

A client sends `PUT /files/3` with `If-None-Match: "a1","c3"`. The current entity tag of the resource is `"a1"`. What does the origin server do?

a) The origin server performs the method and then answers with a `2xx` status code
b) It performs the method first, then answers `412 Precondition Failed`
c) The origin server answers `304 Not Modified` and does not perform the method
d) It answers `412 Precondition Failed` and does not perform the method

**Key: d**

Explanation: Inputs: `PUT /files/3`, `If-None-Match: "a1","c3"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"a1"` matches the current entity tag, so the condition is false. Step 2: the method is `PUT`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `PUT`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 2. seed 270297231958076051, level 2

A client sends `GET /books/41` with `If-None-Match: *`. The resource has a current representation. What does the origin server do?

a) The server performs the method and then answers with a `2xx` status code
b) The origin server performs the method first, then answers `304 Not Modified`
c) The server answers `304 Not Modified` and does not perform the method
d) The origin server answers `412 Precondition Failed` and does not perform the method

**Key: c**

Explanation: Inputs: `GET /books/41`, `If-None-Match: *`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the resource has a current representation, so the condition `*` is false. Step 2: the method is `GET`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `GET`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 3. seed 4408690559796987458, level 2

A client sends `PUT /orders/9` with `If-None-Match: *`. The resource has a current representation. What does the origin server do?

a) It answers `412 Precondition Failed` and does not perform the method
b) The server answers `304 Not Modified` and does not perform the method
c) It performs the method first, then answers `412 Precondition Failed`
d) The server performs the method and then answers with a `2xx` status code

**Key: a**

Explanation: Inputs: `PUT /orders/9`, `If-None-Match: *`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the resource has a current representation, so the condition `*` is false. Step 2: the method is `PUT`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `PUT`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 4. seed 818295045488721211, level 1

A client sends `PUT /files/3` with `If-None-Match: "c3","d4"`. The current entity tag of the resource is `"c3"`. What does the origin server do?

a) The server performs the method first, then answers `412 Precondition Failed`
b) The server answers `304 Not Modified` and does not perform the method
c) The server performs the method and then answers with a `2xx` status code
d) The server answers `412 Precondition Failed` and does not perform the method

**Key: d**

Explanation: Inputs: `PUT /files/3`, `If-None-Match: "c3","d4"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"c3"` matches the current entity tag, so the condition is false. Step 2: the method is `PUT`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `PUT`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 5. seed 852834015205849452, level 1

A client sends `GET /items/7` with `If-None-Match: "a1","c3"`. The current entity tag of the resource is `"a1"`. What does the origin server do?

a) It performs the method and then answers with a `2xx` status code
b) It answers `412 Precondition Failed` and does not perform the method
c) The origin server performs the method first, then answers `304 Not Modified`
d) The server answers `304 Not Modified` and does not perform the method

**Key: d**

Explanation: Inputs: `GET /items/7`, `If-None-Match: "a1","c3"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"a1"` matches the current entity tag, so the condition is false. Step 2: the method is `GET`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `GET`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 6. seed 2591976606957999631, level 2

A client sends `DELETE /books/41` with `If-None-Match: *`. The resource has a current representation. What does the origin server do?

a) The origin server performs the method first, then answers `412 Precondition Failed`
b) The server answers `304 Not Modified` and does not perform the method
c) The server answers `412 Precondition Failed` and does not perform the method
d) It performs the method and then answers with a `2xx` status code

**Key: c**

Explanation: Inputs: `DELETE /books/41`, `If-None-Match: *`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the resource has a current representation, so the condition `*` is false. Step 2: the method is `DELETE`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `DELETE`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 7. seed 4155902829660561296, level 2

A client sends `GET /books/41` with `If-None-Match: "c3","e5"`. The current entity tag of the resource is `"e5"`. What does the origin server do?

a) The origin server answers `304 Not Modified` and does not perform the method
b) The origin server answers `412 Precondition Failed` and does not perform the method
c) The server performs the method and then answers with a `2xx` status code
d) The origin server performs the method first, then answers `304 Not Modified`

**Key: a**

Explanation: Inputs: `GET /books/41`, `If-None-Match: "c3","e5"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"e5"` matches the current entity tag, so the condition is false. Step 2: the method is `GET`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `GET`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 8. seed 959894882906109420, level 1

A client sends `GET /files/3` with `If-None-Match: "d4","e5"`. The current entity tag of the resource is `"d4"`. What does the origin server do?

a) The server performs the method and then answers with a `2xx` status code
b) The origin server answers `304 Not Modified` and does not perform the method
c) It performs the method first, then answers `304 Not Modified`
d) The server answers `412 Precondition Failed` and does not perform the method

**Key: b**

Explanation: Inputs: `GET /files/3`, `If-None-Match: "d4","e5"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"d4"` matches the current entity tag, so the condition is false. Step 2: the method is `GET`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `GET`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 9. seed 279135511345803198, level 2

A client sends `DELETE /orders/9` with `If-None-Match: "e5","c3"`. The current entity tag of the resource is `"e5"`. What does the origin server do?

a) The origin server performs the method first, then answers `412 Precondition Failed`
b) The origin server performs the method and then answers with a `2xx` status code
c) It answers `304 Not Modified` and does not perform the method
d) The server answers `412 Precondition Failed` and does not perform the method

**Key: d**

Explanation: Inputs: `DELETE /orders/9`, `If-None-Match: "e5","c3"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"e5"` matches the current entity tag, so the condition is false. Step 2: the method is `DELETE`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `DELETE`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 10. seed 1042540877962164315, level 1

A client sends `GET /orders/9` with `If-None-Match: "d4","a1"`. The current entity tag of the resource is `"d4"`. What does the origin server do?

a) The origin server performs the method first, then answers `304 Not Modified`
b) It answers `412 Precondition Failed` and does not perform the method
c) The origin server answers `304 Not Modified` and does not perform the method
d) It performs the method and then answers with a `2xx` status code

**Key: c**

Explanation: Inputs: `GET /orders/9`, `If-None-Match: "d4","a1"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"d4"` matches the current entity tag, so the condition is false. Step 2: the method is `GET`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `GET`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 11. seed 1300325161301335678, level 2

A client sends `PUT /files/3` with `If-None-Match: "b2","d4"`. The current entity tag of the resource is `"d4"`. What does the origin server do?

a) The server performs the method and then answers with a `2xx` status code
b) The server answers `304 Not Modified` and does not perform the method
c) It answers `412 Precondition Failed` and does not perform the method
d) The origin server performs the method first, then answers `412 Precondition Failed`

**Key: c**

Explanation: Inputs: `PUT /files/3`, `If-None-Match: "b2","d4"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"d4"` matches the current entity tag, so the condition is false. Step 2: the method is `PUT`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `PUT`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 12. seed 3661912729993250312, level 1

A client sends `GET /books/41` with `If-None-Match: "d4","c3"`. The current entity tag of the resource is `"d4"`. What does the origin server do?

a) The origin server performs the method first, then answers `304 Not Modified`
b) It answers `304 Not Modified` and does not perform the method
c) It answers `412 Precondition Failed` and does not perform the method
d) It performs the method and then answers with a `2xx` status code

**Key: b**

Explanation: Inputs: `GET /books/41`, `If-None-Match: "d4","c3"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"d4"` matches the current entity tag, so the condition is false. Step 2: the method is `GET`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `GET`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 13. seed 3621176665212979962, level 2

A client sends `HEAD /items/7` with `If-None-Match: *`. The resource has a current representation. What does the origin server do?

a) The origin server answers `304 Not Modified` and does not perform the method
b) The origin server performs the method first, then answers `304 Not Modified`
c) It answers `412 Precondition Failed` and does not perform the method
d) The origin server performs the method and then answers with a `2xx` status code

**Key: a**

Explanation: Inputs: `HEAD /items/7`, `If-None-Match: *`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the resource has a current representation, so the condition `*` is false. Step 2: the method is `HEAD`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `HEAD`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 14. seed 1856358302904590823, level 2

A client sends `DELETE /items/7` with `If-None-Match: "c3","b2"`. The current entity tag of the resource is `"c3"`. What does the origin server do?

a) It performs the method first, then answers `412 Precondition Failed`
b) It performs the method and then answers with a `2xx` status code
c) It answers `304 Not Modified` and does not perform the method
d) The server answers `412 Precondition Failed` and does not perform the method

**Key: d**

Explanation: Inputs: `DELETE /items/7`, `If-None-Match: "c3","b2"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"c3"` matches the current entity tag, so the condition is false. Step 2: the method is `DELETE`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `DELETE`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 15. seed 581685685913046960, level 1

A client sends `GET /files/3` with `If-None-Match: "b2","e5"`. The current entity tag of the resource is `"b2"`. What does the origin server do?

a) The server performs the method and then answers with a `2xx` status code
b) The origin server answers `412 Precondition Failed` and does not perform the method
c) It answers `304 Not Modified` and does not perform the method
d) The server performs the method first, then answers `304 Not Modified`

**Key: c**

Explanation: Inputs: `GET /files/3`, `If-None-Match: "b2","e5"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"b2"` matches the current entity tag, so the condition is false. Step 2: the method is `GET`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `GET`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 16. seed 442262615761300158, level 1

A client sends `PUT /items/7` with `If-None-Match: "d4","a1"`. The current entity tag of the resource is `"d4"`. What does the origin server do?

a) It performs the method first, then answers `412 Precondition Failed`
b) The origin server answers `412 Precondition Failed` and does not perform the method
c) It performs the method and then answers with a `2xx` status code
d) It answers `304 Not Modified` and does not perform the method

**Key: b**

Explanation: Inputs: `PUT /items/7`, `If-None-Match: "d4","a1"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"d4"` matches the current entity tag, so the condition is false. Step 2: the method is `PUT`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `PUT`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 17. seed 2167626989849536194, level 2

A client sends `DELETE /books/41` with `If-None-Match: *`. The resource has a current representation. What does the origin server do?

a) The origin server answers `412 Precondition Failed` and does not perform the method
b) It answers `304 Not Modified` and does not perform the method
c) The server performs the method first, then answers `412 Precondition Failed`
d) It performs the method and then answers with a `2xx` status code

**Key: a**

Explanation: Inputs: `DELETE /books/41`, `If-None-Match: *`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the resource has a current representation, so the condition `*` is false. Step 2: the method is `DELETE`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `DELETE`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 18. seed 2142063145496682872, level 1

A client sends `PUT /items/7` with `If-None-Match: "b2","d4"`. The current entity tag of the resource is `"d4"`. What does the origin server do?

a) It answers `304 Not Modified` and does not perform the method
b) The origin server answers `412 Precondition Failed` and does not perform the method
c) The origin server performs the method and then answers with a `2xx` status code
d) The server performs the method first, then answers `412 Precondition Failed`

**Key: b**

Explanation: Inputs: `PUT /items/7`, `If-None-Match: "b2","d4"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"d4"` matches the current entity tag, so the condition is false. Step 2: the method is `PUT`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `PUT`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 19. seed 3929756835234277224, level 1

A client sends `GET /books/41` with `If-None-Match: "b2","e5"`. The current entity tag of the resource is `"e5"`. What does the origin server do?

a) The origin server performs the method and then answers with a `2xx` status code
b) It answers `412 Precondition Failed` and does not perform the method
c) The origin server performs the method first, then answers `304 Not Modified`
d) The origin server answers `304 Not Modified` and does not perform the method

**Key: d**

Explanation: Inputs: `GET /books/41`, `If-None-Match: "b2","e5"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"e5"` matches the current entity tag, so the condition is false. Step 2: the method is `GET`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `GET`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 20. seed 1763205209170531654, level 1

A client sends `GET /items/7` with `If-None-Match: "d4","a1"`. The current entity tag of the resource is `"a1"`. What does the origin server do?

a) The server answers `412 Precondition Failed` and does not perform the method
b) The origin server performs the method and then answers with a `2xx` status code
c) The server answers `304 Not Modified` and does not perform the method
d) The server performs the method first, then answers `304 Not Modified`

**Key: c**

Explanation: Inputs: `GET /items/7`, `If-None-Match: "d4","a1"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"a1"` matches the current entity tag, so the condition is false. Step 2: the method is `GET`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `GET`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 21. seed 2813886196506672298, level 2

A client sends `GET /files/3` with `If-None-Match: "b2","c3"`. The current entity tag of the resource is `"c3"`. What does the origin server do?

a) The origin server answers `304 Not Modified` and does not perform the method
b) The server performs the method and then answers with a `2xx` status code
c) It performs the method first, then answers `304 Not Modified`
d) The origin server answers `412 Precondition Failed` and does not perform the method

**Key: a**

Explanation: Inputs: `GET /files/3`, `If-None-Match: "b2","c3"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"c3"` matches the current entity tag, so the condition is false. Step 2: the method is `GET`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `GET`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 22. seed 3736043982602148712, level 2

A client sends `PUT /items/7` with `If-None-Match: *`. The resource has a current representation. What does the origin server do?

a) The origin server performs the method first, then answers `412 Precondition Failed`
b) The server answers `304 Not Modified` and does not perform the method
c) The server performs the method and then answers with a `2xx` status code
d) The server answers `412 Precondition Failed` and does not perform the method

**Key: d**

Explanation: Inputs: `PUT /items/7`, `If-None-Match: *`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the resource has a current representation, so the condition `*` is false. Step 2: the method is `PUT`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `PUT`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 23. seed 1220470278513493579, level 1

A client sends `GET /users/12` with `If-None-Match: "a1","c3"`. The current entity tag of the resource is `"c3"`. What does the origin server do?

a) It answers `304 Not Modified` and does not perform the method
b) It performs the method and then answers with a `2xx` status code
c) The origin server performs the method first, then answers `304 Not Modified`
d) The server answers `412 Precondition Failed` and does not perform the method

**Key: a**

Explanation: Inputs: `GET /users/12`, `If-None-Match: "a1","c3"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"c3"` matches the current entity tag, so the condition is false. Step 2: the method is `GET`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `GET`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 24. seed 89020275298075474, level 2

A client sends `PUT /items/7` with `If-None-Match: *`. The resource has a current representation. What does the origin server do?

a) It performs the method and then answers with a `2xx` status code
b) It answers `412 Precondition Failed` and does not perform the method
c) The origin server answers `304 Not Modified` and does not perform the method
d) The origin server performs the method first, then answers `412 Precondition Failed`

**Key: b**

Explanation: Inputs: `PUT /items/7`, `If-None-Match: *`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the resource has a current representation, so the condition `*` is false. Step 2: the method is `PUT`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `PUT`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 25. seed 2309663167800984202, level 1

A client sends `PUT /items/7` with `If-None-Match: "a1","e5"`. The current entity tag of the resource is `"a1"`. What does the origin server do?

a) The server performs the method first, then answers `412 Precondition Failed`
b) The server answers `304 Not Modified` and does not perform the method
c) The server answers `412 Precondition Failed` and does not perform the method
d) It performs the method and then answers with a `2xx` status code

**Key: c**

Explanation: Inputs: `PUT /items/7`, `If-None-Match: "a1","e5"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"a1"` matches the current entity tag, so the condition is false. Step 2: the method is `PUT`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `PUT`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 26. seed 705551281436736067, level 1

A client sends `PUT /orders/9` with `If-None-Match: "d4","a1"`. The current entity tag of the resource is `"d4"`. What does the origin server do?

a) The origin server answers `412 Precondition Failed` and does not perform the method
b) The origin server answers `304 Not Modified` and does not perform the method
c) It performs the method first, then answers `412 Precondition Failed`
d) It performs the method and then answers with a `2xx` status code

**Key: a**

Explanation: Inputs: `PUT /orders/9`, `If-None-Match: "d4","a1"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"d4"` matches the current entity tag, so the condition is false. Step 2: the method is `PUT`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `PUT`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 27. seed 2795694389233015017, level 2

A client sends `HEAD /orders/9` with `If-None-Match: "d4","e5"`. The current entity tag of the resource is `"e5"`. What does the origin server do?

a) The server performs the method and then answers with a `2xx` status code
b) The origin server performs the method first, then answers `304 Not Modified`
c) It answers `412 Precondition Failed` and does not perform the method
d) The origin server answers `304 Not Modified` and does not perform the method

**Key: d**

Explanation: Inputs: `HEAD /orders/9`, `If-None-Match: "d4","e5"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"e5"` matches the current entity tag, so the condition is false. Step 2: the method is `HEAD`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `HEAD`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 28. seed 1181292618137978206, level 2

A client sends `DELETE /books/41` with `If-None-Match: *`. The resource has a current representation. What does the origin server do?

a) The server performs the method and then answers with a `2xx` status code
b) The server answers `412 Precondition Failed` and does not perform the method
c) It performs the method first, then answers `412 Precondition Failed`
d) It answers `304 Not Modified` and does not perform the method

**Key: b**

Explanation: Inputs: `DELETE /books/41`, `If-None-Match: *`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the resource has a current representation, so the condition `*` is false. Step 2: the method is `DELETE`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `DELETE`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 29. seed 3597161009641810130, level 2

A client sends `HEAD /files/3` with `If-None-Match: *`. The resource has a current representation. What does the origin server do?

a) The server answers `304 Not Modified` and does not perform the method
b) It performs the method and then answers with a `2xx` status code
c) The origin server answers `412 Precondition Failed` and does not perform the method
d) The server performs the method first, then answers `304 Not Modified`

**Key: a**

Explanation: Inputs: `HEAD /files/3`, `If-None-Match: *`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the resource has a current representation, so the condition `*` is false. Step 2: the method is `HEAD`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `HEAD`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 30. seed 3951886894350032306, level 2

A client sends `PUT /books/41` with `If-None-Match: "e5","c3"`. The current entity tag of the resource is `"c3"`. What does the origin server do?

a) The origin server answers `412 Precondition Failed` and does not perform the method
b) The origin server performs the method and then answers with a `2xx` status code
c) The origin server performs the method first, then answers `412 Precondition Failed`
d) It answers `304 Not Modified` and does not perform the method

**Key: a**

Explanation: Inputs: `PUT /books/41`, `If-None-Match: "e5","c3"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"c3"` matches the current entity tag, so the condition is false. Step 2: the method is `PUT`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `PUT`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 31. seed 3780667809435764665, level 2

A client sends `GET /orders/9` with `If-None-Match: "b2","d4"`. The current entity tag of the resource is `"b2"`. What does the origin server do?

a) The origin server performs the method first, then answers `304 Not Modified`
b) The origin server answers `412 Precondition Failed` and does not perform the method
c) The server performs the method and then answers with a `2xx` status code
d) The server answers `304 Not Modified` and does not perform the method

**Key: d**

Explanation: Inputs: `GET /orders/9`, `If-None-Match: "b2","d4"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"b2"` matches the current entity tag, so the condition is false. Step 2: the method is `GET`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `GET`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 32. seed 819944596339735128, level 2

A client sends `PUT /orders/9` with `If-None-Match: *`. The resource has a current representation. What does the origin server do?

a) The origin server performs the method and then answers with a `2xx` status code
b) The origin server answers `304 Not Modified` and does not perform the method
c) It performs the method first, then answers `412 Precondition Failed`
d) The server answers `412 Precondition Failed` and does not perform the method

**Key: d**

Explanation: Inputs: `PUT /orders/9`, `If-None-Match: *`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the resource has a current representation, so the condition `*` is false. Step 2: the method is `PUT`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `PUT`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 33. seed 2667811102284365749, level 2

A client sends `PUT /files/3` with `If-None-Match: "b2","a1"`. The current entity tag of the resource is `"a1"`. What does the origin server do?

a) The server performs the method first, then answers `412 Precondition Failed`
b) The server answers `304 Not Modified` and does not perform the method
c) The origin server performs the method and then answers with a `2xx` status code
d) The origin server answers `412 Precondition Failed` and does not perform the method

**Key: d**

Explanation: Inputs: `PUT /files/3`, `If-None-Match: "b2","a1"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"a1"` matches the current entity tag, so the condition is false. Step 2: the method is `PUT`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `PUT`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 34. seed 4233115497800408507, level 1

A client sends `GET /items/7` with `If-None-Match: "a1","b2"`. The current entity tag of the resource is `"b2"`. What does the origin server do?

a) The origin server performs the method first, then answers `304 Not Modified`
b) The origin server performs the method and then answers with a `2xx` status code
c) The origin server answers `304 Not Modified` and does not perform the method
d) The server answers `412 Precondition Failed` and does not perform the method

**Key: c**

Explanation: Inputs: `GET /items/7`, `If-None-Match: "a1","b2"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"b2"` matches the current entity tag, so the condition is false. Step 2: the method is `GET`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `GET`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 35. seed 1870653887003634697, level 1

A client sends `GET /files/3` with `If-None-Match: "d4","b2"`. The current entity tag of the resource is `"b2"`. What does the origin server do?

a) The origin server answers `304 Not Modified` and does not perform the method
b) The origin server performs the method and then answers with a `2xx` status code
c) The server performs the method first, then answers `304 Not Modified`
d) The origin server answers `412 Precondition Failed` and does not perform the method

**Key: a**

Explanation: Inputs: `GET /files/3`, `If-None-Match: "d4","b2"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"b2"` matches the current entity tag, so the condition is false. Step 2: the method is `GET`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `GET`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 36. seed 1349255053016399801, level 1

A client sends `GET /users/12` with `If-None-Match: "d4","c3"`. The current entity tag of the resource is `"c3"`. What does the origin server do?

a) It answers `412 Precondition Failed` and does not perform the method
b) It answers `304 Not Modified` and does not perform the method
c) The origin server performs the method first, then answers `304 Not Modified`
d) The server performs the method and then answers with a `2xx` status code

**Key: b**

Explanation: Inputs: `GET /users/12`, `If-None-Match: "d4","c3"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"c3"` matches the current entity tag, so the condition is false. Step 2: the method is `GET`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `GET`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 37. seed 1850201771622758261, level 1

A client sends `PUT /users/12` with `If-None-Match: "d4","e5"`. The current entity tag of the resource is `"e5"`. What does the origin server do?

a) The origin server answers `304 Not Modified` and does not perform the method
b) It performs the method first, then answers `412 Precondition Failed`
c) The server answers `412 Precondition Failed` and does not perform the method
d) The server performs the method and then answers with a `2xx` status code

**Key: c**

Explanation: Inputs: `PUT /users/12`, `If-None-Match: "d4","e5"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"e5"` matches the current entity tag, so the condition is false. Step 2: the method is `PUT`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `PUT`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 38. seed 3872524877656074517, level 1

A client sends `PUT /files/3` with `If-None-Match: "d4","e5"`. The current entity tag of the resource is `"d4"`. What does the origin server do?

a) The server answers `304 Not Modified` and does not perform the method
b) The server answers `412 Precondition Failed` and does not perform the method
c) It performs the method first, then answers `412 Precondition Failed`
d) The origin server performs the method and then answers with a `2xx` status code

**Key: b**

Explanation: Inputs: `PUT /files/3`, `If-None-Match: "d4","e5"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"d4"` matches the current entity tag, so the condition is false. Step 2: the method is `PUT`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `PUT`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 39. seed 845794668762587081, level 1

A client sends `PUT /files/3` with `If-None-Match: "c3","e5"`. The current entity tag of the resource is `"e5"`. What does the origin server do?

a) The server performs the method and then answers with a `2xx` status code
b) The server answers `304 Not Modified` and does not perform the method
c) It answers `412 Precondition Failed` and does not perform the method
d) The origin server performs the method first, then answers `412 Precondition Failed`

**Key: c**

Explanation: Inputs: `PUT /files/3`, `If-None-Match: "c3","e5"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"e5"` matches the current entity tag, so the condition is false. Step 2: the method is `PUT`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `PUT`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 40. seed 3135608872539830399, level 2

A client sends `PUT /users/12` with `If-None-Match: *`. The resource has a current representation. What does the origin server do?

a) It answers `412 Precondition Failed` and does not perform the method
b) The origin server performs the method first, then answers `412 Precondition Failed`
c) It performs the method and then answers with a `2xx` status code
d) The origin server answers `304 Not Modified` and does not perform the method

**Key: a**

Explanation: Inputs: `PUT /users/12`, `If-None-Match: *`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the resource has a current representation, so the condition `*` is false. Step 2: the method is `PUT`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `PUT`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 41. seed 80402238614821684, level 2

A client sends `GET /items/7` with `If-None-Match: "a1","d4"`. The current entity tag of the resource is `"a1"`. What does the origin server do?

a) The server performs the method first, then answers `304 Not Modified`
b) It answers `304 Not Modified` and does not perform the method
c) The origin server performs the method and then answers with a `2xx` status code
d) The server answers `412 Precondition Failed` and does not perform the method

**Key: b**

Explanation: Inputs: `GET /items/7`, `If-None-Match: "a1","d4"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"a1"` matches the current entity tag, so the condition is false. Step 2: the method is `GET`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `GET`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 42. seed 2568503105275313481, level 2

A client sends `DELETE /orders/9` with `If-None-Match: "e5","c3"`. The current entity tag of the resource is `"c3"`. What does the origin server do?

a) The server answers `412 Precondition Failed` and does not perform the method
b) It answers `304 Not Modified` and does not perform the method
c) The server performs the method and then answers with a `2xx` status code
d) The server performs the method first, then answers `412 Precondition Failed`

**Key: a**

Explanation: Inputs: `DELETE /orders/9`, `If-None-Match: "e5","c3"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"c3"` matches the current entity tag, so the condition is false. Step 2: the method is `DELETE`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `DELETE`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 43. seed 428774421179256672, level 2

A client sends `HEAD /books/41` with `If-None-Match: "a1","e5"`. The current entity tag of the resource is `"a1"`. What does the origin server do?

a) The origin server answers `412 Precondition Failed` and does not perform the method
b) The server answers `304 Not Modified` and does not perform the method
c) The server performs the method first, then answers `304 Not Modified`
d) The origin server performs the method and then answers with a `2xx` status code

**Key: b**

Explanation: Inputs: `HEAD /books/41`, `If-None-Match: "a1","e5"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"a1"` matches the current entity tag, so the condition is false. Step 2: the method is `HEAD`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `HEAD`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 44. seed 481771617245781543, level 2

A client sends `HEAD /users/12` with `If-None-Match: "a1","b2"`. The current entity tag of the resource is `"b2"`. What does the origin server do?

a) The origin server answers `304 Not Modified` and does not perform the method
b) The server answers `412 Precondition Failed` and does not perform the method
c) The origin server performs the method first, then answers `304 Not Modified`
d) The origin server performs the method and then answers with a `2xx` status code

**Key: a**

Explanation: Inputs: `HEAD /users/12`, `If-None-Match: "a1","b2"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"b2"` matches the current entity tag, so the condition is false. Step 2: the method is `HEAD`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `HEAD`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 45. seed 2950092072493498827, level 2

A client sends `DELETE /orders/9` with `If-None-Match: *`. The resource has a current representation. What does the origin server do?

a) The origin server performs the method and then answers with a `2xx` status code
b) The origin server performs the method first, then answers `412 Precondition Failed`
c) It answers `412 Precondition Failed` and does not perform the method
d) The origin server answers `304 Not Modified` and does not perform the method

**Key: c**

Explanation: Inputs: `DELETE /orders/9`, `If-None-Match: *`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the resource has a current representation, so the condition `*` is false. Step 2: the method is `DELETE`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `DELETE`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 46. seed 2608676164057423698, level 1

A client sends `GET /users/12` with `If-None-Match: "c3","e5"`. The current entity tag of the resource is `"c3"`. What does the origin server do?

a) The server answers `412 Precondition Failed` and does not perform the method
b) The server answers `304 Not Modified` and does not perform the method
c) It performs the method and then answers with a `2xx` status code
d) It performs the method first, then answers `304 Not Modified`

**Key: b**

Explanation: Inputs: `GET /users/12`, `If-None-Match: "c3","e5"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"c3"` matches the current entity tag, so the condition is false. Step 2: the method is `GET`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `GET`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 47. seed 1927393830143048340, level 1

A client sends `PUT /books/41` with `If-None-Match: "c3","d4"`. The current entity tag of the resource is `"d4"`. What does the origin server do?

a) The origin server answers `412 Precondition Failed` and does not perform the method
b) The server answers `304 Not Modified` and does not perform the method
c) The server performs the method first, then answers `412 Precondition Failed`
d) The server performs the method and then answers with a `2xx` status code

**Key: a**

Explanation: Inputs: `PUT /books/41`, `If-None-Match: "c3","d4"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"d4"` matches the current entity tag, so the condition is false. Step 2: the method is `PUT`, so the answer is `412 Precondition Failed`. Result: Answering `412 Precondition Failed` without performing the method. Answering `304 Not Modified` without performing the method comes from applying the rule for `GET` and `HEAD`, `304`, to a `PUT`, but a false `If-None-Match` condition gets `412 Precondition Failed` for every method but `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `412 Precondition Failed` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 48. seed 962146972855817156, level 2

A client sends `HEAD /books/41` with `If-None-Match: *`. The resource has a current representation. What does the origin server do?

a) The origin server answers `412 Precondition Failed` and does not perform the method
b) The origin server performs the method and then answers with a `2xx` status code
c) The server answers `304 Not Modified` and does not perform the method
d) The origin server performs the method first, then answers `304 Not Modified`

**Key: c**

Explanation: Inputs: `HEAD /books/41`, `If-None-Match: *`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the resource has a current representation, so the condition `*` is false. Step 2: the method is `HEAD`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `HEAD`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 49. seed 973576541943693740, level 1

A client sends `GET /items/7` with `If-None-Match: "b2","d4"`. The current entity tag of the resource is `"b2"`. What does the origin server do?

a) The origin server performs the method and then answers with a `2xx` status code
b) The origin server performs the method first, then answers `304 Not Modified`
c) The origin server answers `412 Precondition Failed` and does not perform the method
d) It answers `304 Not Modified` and does not perform the method

**Key: d**

Explanation: Inputs: `GET /items/7`, `If-None-Match: "b2","d4"`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the listed tag `"b2"` matches the current entity tag, so the condition is false. Step 2: the method is `GET`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `GET`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.

## 50. seed 882887261394990367, level 2

A client sends `GET /users/12` with `If-None-Match: *`. The resource has a current representation. What does the origin server do?

a) The server answers `412 Precondition Failed` and does not perform the method
b) The server performs the method first, then answers `304 Not Modified`
c) The origin server performs the method and then answers with a `2xx` status code
d) The origin server answers `304 Not Modified` and does not perform the method

**Key: d**

Explanation: Inputs: `GET /users/12`, `If-None-Match: *`. Rule: the `If-None-Match` condition is false when `*` meets a current representation or a listed tag matches the current one; then the server must not perform the method and answers `304 Not Modified` for `GET` or `HEAD` and `412 Precondition Failed` for all other methods. Step 1: the resource has a current representation, so the condition `*` is false. Step 2: the method is `GET`, so the answer is `304 Not Modified`. Result: Answering `304 Not Modified` without performing the method. Answering `412 Precondition Failed` without performing the method comes from applying the rule for the other methods, `412`, to a `GET`, but a false `If-None-Match` condition gets `304 Not Modified` for `GET` and `HEAD`. Performing the method and then answering with a `2xx` status code comes from ignoring the condition and performing the method, but the server must not perform the method when the condition evaluates to false. Performing the method first and then answering `304 Not Modified` comes from believing the condition is checked after the method has run, but the condition is a precondition, tested before the method is applied to the target resource. Source: `rfc9110#section-13.1.2`.
