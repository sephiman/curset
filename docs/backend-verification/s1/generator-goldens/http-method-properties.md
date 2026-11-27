# Safe and idempotent methods (`http-method-properties`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 1879695484657045374, level 2

A client may send any of the following requests. Which one is not safe in the sense of RFC 9110, because its defined semantics are not essentially read-only?

a) `GET /invoices/2`
b) `TRACE /orders/9`
c) `PUT /invoices/2`
d) `HEAD /users/124`

**Key: c**

Explanation: Inputs: the question asks for a request that is not safe. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `PUT` as idempotent but not safe. Step 2: find the method among the ones that are not safe. Result: `PUT /invoices/2`. The other options come from taking a read-only method for one that changes state: `GET` is safe, `HEAD` is safe, `OPTIONS` is safe, `TRACE` is safe. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 2. seed 4098128683445156951, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `PUT /reports/17`
b) `POST /books/405`
c) `TRACE /items/12`
d) `DELETE /files/7`

**Key: c**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `TRACE` as safe. Step 2: find the method among the safe ones. Result: `TRACE /items/12`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 3. seed 829206280208519114, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `POST /users/124`
b) `DELETE /carts/4`
c) `GET /invoices/2`
d) `PUT /invoices/2`

**Key: c**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `GET` as safe. Step 2: find the method among the safe ones. Result: `GET /invoices/2`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 4. seed 4464568583444125247, level 2

A proxy sits between a client and an origin server, and a connection fails before the response arrives. Which of these requests must the proxy not retry automatically?

a) `OPTIONS /jobs/3`
b) `POST /users/124`
c) `TRACE /orders/9`
d) `GET /invoices/2`

**Key: b**

Explanation: Inputs: the question asks for a request that is not idempotent. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `POST` as neither safe nor idempotent. Step 2: keep the methods that are not idempotent, which a proxy must not retry. Result: `POST /users/124`. The other options come from taking an idempotent method for one that must not be retried: `GET` is safe, `HEAD` is safe, `OPTIONS` is safe, `TRACE` is safe, `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 5. seed 1769722230422680925, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `POST /users/124`
b) `DELETE /carts/4`
c) `OPTIONS /jobs/3`
d) `PUT /invoices/2`

**Key: c**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `OPTIONS` as safe. Step 2: find the method among the safe ones. Result: `OPTIONS /jobs/3`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 6. seed 3608942312049112723, level 2

A client may send any of the following requests. Which one is idempotent but not safe, as RFC 9110 defines both properties for its methods?

a) `TRACE /orders/9`
b) `PUT /invoices/2`
c) `POST /users/124`
d) `OPTIONS /jobs/3`

**Key: b**

Explanation: Inputs: the question asks for an idempotent request that is not safe. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `PUT` as idempotent but not safe. Step 2: keep the idempotent methods and drop the safe ones. Result: `PUT /invoices/2`. The other options come from forgetting that safe methods are idempotent too, or taking `POST` for idempotent: `GET` is safe, `HEAD` is safe, `OPTIONS` is safe, `TRACE` is safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 7. seed 2214334774244633469, level 2

A client may send any of the following requests. Which one is idempotent but not safe, as RFC 9110 defines both properties for its methods?

a) `HEAD /books/405`
b) `OPTIONS /tags/8`
c) `DELETE /files/7`
d) `TRACE /items/12`

**Key: c**

Explanation: Inputs: the question asks for an idempotent request that is not safe. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `DELETE` as idempotent but not safe. Step 2: keep the idempotent methods and drop the safe ones. Result: `DELETE /files/7`. The other options come from forgetting that safe methods are idempotent too, or taking `POST` for idempotent: `GET` is safe, `HEAD` is safe, `OPTIONS` is safe, `TRACE` is safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 8. seed 4301623485649065633, level 2

A client may send any of the following requests. Which one is not safe in the sense of RFC 9110, because its defined semantics are not essentially read-only?

a) `GET /invoices/2`
b) `HEAD /users/124`
c) `DELETE /carts/4`
d) `OPTIONS /jobs/3`

**Key: c**

Explanation: Inputs: the question asks for a request that is not safe. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `DELETE` as idempotent but not safe. Step 2: find the method among the ones that are not safe. Result: `DELETE /carts/4`. The other options come from taking a read-only method for one that changes state: `GET` is safe, `HEAD` is safe, `OPTIONS` is safe, `TRACE` is safe. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 9. seed 988536917782634436, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `PUT /reports/17`
b) `DELETE /files/7`
c) `POST /books/405`
d) `GET /reports/17`

**Key: d**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `GET` as safe. Step 2: find the method among the safe ones. Result: `GET /reports/17`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 10. seed 3390199409718199460, level 2

A proxy sits between a client and an origin server, and a connection fails before the response arrives. Which of these requests must the proxy not retry automatically?

a) `POST /users/124`
b) `TRACE /orders/9`
c) `OPTIONS /jobs/3`
d) `DELETE /carts/4`

**Key: a**

Explanation: Inputs: the question asks for a request that is not idempotent. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `POST` as neither safe nor idempotent. Step 2: keep the methods that are not idempotent, which a proxy must not retry. Result: `POST /users/124`. The other options come from taking an idempotent method for one that must not be retried: `GET` is safe, `HEAD` is safe, `OPTIONS` is safe, `TRACE` is safe, `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 11. seed 1360828788876711443, level 2

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `POST /books/405`
b) `PUT /reports/17`
c) `DELETE /files/7`
d) `TRACE /items/12`

**Key: d**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `TRACE` as safe. Step 2: find the method among the safe ones. Result: `TRACE /items/12`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 12. seed 89055899815626801, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `POST /users/124`
b) `PUT /invoices/2`
c) `TRACE /orders/9`
d) `DELETE /carts/4`

**Key: c**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `TRACE` as safe. Step 2: find the method among the safe ones. Result: `TRACE /orders/9`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 13. seed 680410254383445501, level 2

A proxy sits between a client and an origin server, and a connection fails before the response arrives. Which of these requests must the proxy not retry automatically?

a) `POST /books/405`
b) `TRACE /items/12`
c) `PUT /reports/17`
d) `DELETE /files/7`

**Key: a**

Explanation: Inputs: the question asks for a request that is not idempotent. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `POST` as neither safe nor idempotent. Step 2: keep the methods that are not idempotent, which a proxy must not retry. Result: `POST /books/405`. The other options come from taking an idempotent method for one that must not be retried: `GET` is safe, `HEAD` is safe, `OPTIONS` is safe, `TRACE` is safe, `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 14. seed 3156021791817330597, level 2

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `DELETE /carts/4`
b) `PUT /invoices/2`
c) `POST /users/124`
d) `GET /invoices/2`

**Key: d**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `GET` as safe. Step 2: find the method among the safe ones. Result: `GET /invoices/2`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 15. seed 1214441022468359518, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `POST /books/405`
b) `PUT /reports/17`
c) `HEAD /books/405`
d) `DELETE /files/7`

**Key: c**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `HEAD` as safe. Step 2: find the method among the safe ones. Result: `HEAD /books/405`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 16. seed 1045071100125040669, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `PUT /reports/17`
b) `POST /books/405`
c) `DELETE /files/7`
d) `HEAD /books/405`

**Key: d**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `HEAD` as safe. Step 2: find the method among the safe ones. Result: `HEAD /books/405`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 17. seed 241031259342537590, level 2

A client may send any of the following requests. Which one is not safe in the sense of RFC 9110, because its defined semantics are not essentially read-only?

a) `OPTIONS /jobs/3`
b) `POST /users/124`
c) `TRACE /orders/9`
d) `GET /invoices/2`

**Key: b**

Explanation: Inputs: the question asks for a request that is not safe. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `POST` as neither safe nor idempotent. Step 2: find the method among the ones that are not safe. Result: `POST /users/124`. The other options come from taking a read-only method for one that changes state: `GET` is safe, `HEAD` is safe, `OPTIONS` is safe, `TRACE` is safe. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 18. seed 71300842459888068, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `DELETE /files/7`
b) `PUT /reports/17`
c) `POST /books/405`
d) `OPTIONS /tags/8`

**Key: d**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `OPTIONS` as safe. Step 2: find the method among the safe ones. Result: `OPTIONS /tags/8`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 19. seed 2881256701472429039, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `DELETE /carts/4`
b) `GET /invoices/2`
c) `POST /users/124`
d) `PUT /invoices/2`

**Key: b**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `GET` as safe. Step 2: find the method among the safe ones. Result: `GET /invoices/2`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 20. seed 2499538684191193730, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `POST /books/405`
b) `TRACE /items/12`
c) `DELETE /files/7`
d) `PUT /reports/17`

**Key: b**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `TRACE` as safe. Step 2: find the method among the safe ones. Result: `TRACE /items/12`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 21. seed 197483252793270785, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `PUT /reports/17`
b) `HEAD /books/405`
c) `DELETE /files/7`
d) `POST /books/405`

**Key: b**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `HEAD` as safe. Step 2: find the method among the safe ones. Result: `HEAD /books/405`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 22. seed 1533708880225492114, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `PUT /invoices/2`
b) `TRACE /orders/9`
c) `DELETE /carts/4`
d) `POST /users/124`

**Key: b**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `TRACE` as safe. Step 2: find the method among the safe ones. Result: `TRACE /orders/9`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 23. seed 1983796619541078671, level 2

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `DELETE /carts/4`
b) `GET /invoices/2`
c) `PUT /invoices/2`
d) `POST /users/124`

**Key: b**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `GET` as safe. Step 2: find the method among the safe ones. Result: `GET /invoices/2`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 24. seed 3742905816012965636, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `PUT /reports/17`
b) `OPTIONS /tags/8`
c) `DELETE /files/7`
d) `POST /books/405`

**Key: b**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `OPTIONS` as safe. Step 2: find the method among the safe ones. Result: `OPTIONS /tags/8`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 25. seed 3979834535613104098, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `GET /invoices/2`
b) `POST /users/124`
c) `DELETE /carts/4`
d) `PUT /invoices/2`

**Key: a**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `GET` as safe. Step 2: find the method among the safe ones. Result: `GET /invoices/2`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 26. seed 1468767416139152716, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `PUT /invoices/2`
b) `OPTIONS /jobs/3`
c) `POST /users/124`
d) `DELETE /carts/4`

**Key: b**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `OPTIONS` as safe. Step 2: find the method among the safe ones. Result: `OPTIONS /jobs/3`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 27. seed 4410594326638209124, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `POST /users/124`
b) `DELETE /carts/4`
c) `PUT /invoices/2`
d) `OPTIONS /jobs/3`

**Key: d**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `OPTIONS` as safe. Step 2: find the method among the safe ones. Result: `OPTIONS /jobs/3`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 28. seed 1177730729005240998, level 2

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `TRACE /orders/9`
b) `DELETE /carts/4`
c) `PUT /invoices/2`
d) `POST /users/124`

**Key: a**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `TRACE` as safe. Step 2: find the method among the safe ones. Result: `TRACE /orders/9`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 29. seed 1479749434956748330, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `POST /books/405`
b) `PUT /reports/17`
c) `GET /reports/17`
d) `DELETE /files/7`

**Key: c**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `GET` as safe. Step 2: find the method among the safe ones. Result: `GET /reports/17`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 30. seed 4163370510863294414, level 2

A client may send any of the following requests. Which one is not safe in the sense of RFC 9110, because its defined semantics are not essentially read-only?

a) `TRACE /orders/9`
b) `POST /users/124`
c) `HEAD /users/124`
d) `OPTIONS /jobs/3`

**Key: b**

Explanation: Inputs: the question asks for a request that is not safe. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `POST` as neither safe nor idempotent. Step 2: find the method among the ones that are not safe. Result: `POST /users/124`. The other options come from taking a read-only method for one that changes state: `GET` is safe, `HEAD` is safe, `OPTIONS` is safe, `TRACE` is safe. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 31. seed 2913283781190710368, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `POST /users/124`
b) `OPTIONS /jobs/3`
c) `DELETE /carts/4`
d) `PUT /invoices/2`

**Key: b**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `OPTIONS` as safe. Step 2: find the method among the safe ones. Result: `OPTIONS /jobs/3`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 32. seed 3451559115810523870, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `POST /users/124`
b) `OPTIONS /jobs/3`
c) `PUT /invoices/2`
d) `DELETE /carts/4`

**Key: b**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `OPTIONS` as safe. Step 2: find the method among the safe ones. Result: `OPTIONS /jobs/3`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 33. seed 231547402238992379, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `DELETE /files/7`
b) `OPTIONS /tags/8`
c) `POST /books/405`
d) `PUT /reports/17`

**Key: b**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `OPTIONS` as safe. Step 2: find the method among the safe ones. Result: `OPTIONS /tags/8`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 34. seed 1765448131299589971, level 2

A client may send any of the following requests. Which one is idempotent but not safe, as RFC 9110 defines both properties for its methods?

a) `HEAD /users/124`
b) `POST /users/124`
c) `PUT /invoices/2`
d) `GET /invoices/2`

**Key: c**

Explanation: Inputs: the question asks for an idempotent request that is not safe. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `PUT` as idempotent but not safe. Step 2: keep the idempotent methods and drop the safe ones. Result: `PUT /invoices/2`. The other options come from forgetting that safe methods are idempotent too, or taking `POST` for idempotent: `GET` is safe, `HEAD` is safe, `OPTIONS` is safe, `TRACE` is safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 35. seed 4167582539661203820, level 2

A client may send any of the following requests. Which one is idempotent but not safe, as RFC 9110 defines both properties for its methods?

a) `DELETE /carts/4`
b) `POST /users/124`
c) `GET /invoices/2`
d) `HEAD /users/124`

**Key: a**

Explanation: Inputs: the question asks for an idempotent request that is not safe. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `DELETE` as idempotent but not safe. Step 2: keep the idempotent methods and drop the safe ones. Result: `DELETE /carts/4`. The other options come from forgetting that safe methods are idempotent too, or taking `POST` for idempotent: `GET` is safe, `HEAD` is safe, `OPTIONS` is safe, `TRACE` is safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 36. seed 152212611513468505, level 2

A client may send any of the following requests. Which one is not safe in the sense of RFC 9110, because its defined semantics are not essentially read-only?

a) `GET /invoices/2`
b) `TRACE /orders/9`
c) `OPTIONS /jobs/3`
d) `DELETE /carts/4`

**Key: d**

Explanation: Inputs: the question asks for a request that is not safe. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `DELETE` as idempotent but not safe. Step 2: find the method among the ones that are not safe. Result: `DELETE /carts/4`. The other options come from taking a read-only method for one that changes state: `GET` is safe, `HEAD` is safe, `OPTIONS` is safe, `TRACE` is safe. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 37. seed 2250439045069608459, level 2

A proxy sits between a client and an origin server, and a connection fails before the response arrives. Which of these requests must the proxy not retry automatically?

a) `POST /users/124`
b) `HEAD /users/124`
c) `PUT /invoices/2`
d) `DELETE /carts/4`

**Key: a**

Explanation: Inputs: the question asks for a request that is not idempotent. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `POST` as neither safe nor idempotent. Step 2: keep the methods that are not idempotent, which a proxy must not retry. Result: `POST /users/124`. The other options come from taking an idempotent method for one that must not be retried: `GET` is safe, `HEAD` is safe, `OPTIONS` is safe, `TRACE` is safe, `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 38. seed 1955937728634911089, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `POST /users/124`
b) `HEAD /users/124`
c) `DELETE /carts/4`
d) `PUT /invoices/2`

**Key: b**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `HEAD` as safe. Step 2: find the method among the safe ones. Result: `HEAD /users/124`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 39. seed 4296223234402586236, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `POST /books/405`
b) `PUT /reports/17`
c) `GET /reports/17`
d) `DELETE /files/7`

**Key: c**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `GET` as safe. Step 2: find the method among the safe ones. Result: `GET /reports/17`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 40. seed 3408579418822681604, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `POST /users/124`
b) `PUT /invoices/2`
c) `OPTIONS /jobs/3`
d) `DELETE /carts/4`

**Key: c**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `OPTIONS` as safe. Step 2: find the method among the safe ones. Result: `OPTIONS /jobs/3`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 41. seed 2722682882656419382, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `DELETE /files/7`
b) `PUT /reports/17`
c) `OPTIONS /tags/8`
d) `POST /books/405`

**Key: c**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `OPTIONS` as safe. Step 2: find the method among the safe ones. Result: `OPTIONS /tags/8`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 42. seed 3829865676047839561, level 2

A client may send any of the following requests. Which one is not safe in the sense of RFC 9110, because its defined semantics are not essentially read-only?

a) `HEAD /books/405`
b) `DELETE /files/7`
c) `OPTIONS /tags/8`
d) `GET /reports/17`

**Key: b**

Explanation: Inputs: the question asks for a request that is not safe. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `DELETE` as idempotent but not safe. Step 2: find the method among the ones that are not safe. Result: `DELETE /files/7`. The other options come from taking a read-only method for one that changes state: `GET` is safe, `HEAD` is safe, `OPTIONS` is safe, `TRACE` is safe. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 43. seed 956918527020986837, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `POST /books/405`
b) `GET /reports/17`
c) `PUT /reports/17`
d) `DELETE /files/7`

**Key: b**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `GET` as safe. Step 2: find the method among the safe ones. Result: `GET /reports/17`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 44. seed 3457892848990412420, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `PUT /invoices/2`
b) `GET /invoices/2`
c) `DELETE /carts/4`
d) `POST /users/124`

**Key: b**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `GET` as safe. Step 2: find the method among the safe ones. Result: `GET /invoices/2`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 45. seed 2327355908642239128, level 2

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `PUT /invoices/2`
b) `GET /invoices/2`
c) `DELETE /carts/4`
d) `POST /users/124`

**Key: b**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `GET` as safe. Step 2: find the method among the safe ones. Result: `GET /invoices/2`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 46. seed 4561738158039160803, level 1

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `OPTIONS /tags/8`
b) `DELETE /files/7`
c) `PUT /reports/17`
d) `POST /books/405`

**Key: a**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `OPTIONS` as safe. Step 2: find the method among the safe ones. Result: `OPTIONS /tags/8`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 47. seed 3756596872831425191, level 2

A proxy sits between a client and an origin server, and a connection fails before the response arrives. Which of these requests must the proxy not retry automatically?

a) `POST /users/124`
b) `PUT /invoices/2`
c) `DELETE /carts/4`
d) `GET /invoices/2`

**Key: a**

Explanation: Inputs: the question asks for a request that is not idempotent. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `POST` as neither safe nor idempotent. Step 2: keep the methods that are not idempotent, which a proxy must not retry. Result: `POST /users/124`. The other options come from taking an idempotent method for one that must not be retried: `GET` is safe, `HEAD` is safe, `OPTIONS` is safe, `TRACE` is safe, `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 48. seed 1567524994391505933, level 2

A proxy sits between a client and an origin server, and a connection fails before the response arrives. Which of these requests must the proxy not retry automatically?

a) `HEAD /users/124`
b) `GET /invoices/2`
c) `POST /users/124`
d) `TRACE /orders/9`

**Key: c**

Explanation: Inputs: the question asks for a request that is not idempotent. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `POST` as neither safe nor idempotent. Step 2: keep the methods that are not idempotent, which a proxy must not retry. Result: `POST /users/124`. The other options come from taking an idempotent method for one that must not be retried: `GET` is safe, `HEAD` is safe, `OPTIONS` is safe, `TRACE` is safe, `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 49. seed 2421605318339710005, level 2

A proxy sits between a client and an origin server, and a connection fails before the response arrives. Which of these requests must the proxy not retry automatically?

a) `OPTIONS /tags/8`
b) `GET /reports/17`
c) `DELETE /files/7`
d) `POST /books/405`

**Key: d**

Explanation: Inputs: the question asks for a request that is not idempotent. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `POST` as neither safe nor idempotent. Step 2: keep the methods that are not idempotent, which a proxy must not retry. Result: `POST /books/405`. The other options come from taking an idempotent method for one that must not be retried: `GET` is safe, `HEAD` is safe, `OPTIONS` is safe, `TRACE` is safe, `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.

## 50. seed 318038703652897659, level 2

A client may send any of the following requests. Which one is safe in the sense of RFC 9110, meaning its defined semantics are essentially read-only?

a) `DELETE /carts/4`
b) `GET /invoices/2`
c) `POST /users/124`
d) `PUT /invoices/2`

**Key: b**

Explanation: Inputs: the question asks for a safe request. Rule: RFC 9110 defines `GET`, `HEAD`, `OPTIONS`, `TRACE` as safe; `PUT`, `DELETE` and the safe methods are idempotent; no other method it defines is idempotent. Step 1: classify `GET` as safe. Step 2: find the method among the safe ones. Result: `GET /invoices/2`. The other options come from taking a method that changes state for a read-only one: `PUT` is idempotent but not safe, `DELETE` is idempotent but not safe, `POST` is neither safe nor idempotent. Source: `rfc9110#section-9.2.1`; `rfc9110#section-9.2.2`.
