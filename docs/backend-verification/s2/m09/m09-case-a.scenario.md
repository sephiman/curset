# Distributed rate limiter for a public API

A company exposes a public REST API through 12 gateway instances behind a load balancer. Each client is identified by an API key, and every key has a quota of 100 requests per 60-second window. Heavy clients must be slowed down, and a client that exceeds its quota must receive a `429` response.

The first version kept a counter per API key in the memory of each gateway instance. Clients quickly learned that spreading their calls over different instances let them exceed the quota, so the team moved the counters to a shared store that every instance queries before it forwards a request. That check runs on the request path of every call, so it has to stay fast.

The platform team is now deciding how the limiter works in detail:

- The limiter state lives in Redis, with atomic fixed-window counters, and an alternative based on the Resilience4j `RateLimiter` library is used for outbound calls to partner services.
- Responses advertise the quota with the `RateLimit-Policy` and `RateLimit` header fields of the IETF HTTP API draft, and may also carry `Retry-After`.
- The ingestion path into Kafka is protected with broker quotas, so a noisy producer cannot starve the others.
