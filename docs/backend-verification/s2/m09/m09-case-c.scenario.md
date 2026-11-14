# Multi-channel notification platform

A retail company sends order confirmations, shipping updates and marketing messages by email, SMS and mobile push. Business services publish notification requests to Kafka, and one consumer group per channel reads them and calls the external provider for that channel. Providers are slow and fail often, and a duplicated order confirmation annoys customers while a lost one raises support tickets.

The team has to settle the following points:

- Delivery semantics. Each consumer reads a batch, calls the provider and saves its position in the log. The order of those steps decides whether a failure loses messages or repeats them.
- Retries. Failed sends are retried with a backoff, either in the client, with Resilience4j `Retry`, or as non-blocking retry and dead-letter topics in Spring for Apache Kafka.
- Dead letters. For the RabbitMQ queue that carries SMS requests, messages that cannot be delivered must end in a dead letter exchange for inspection.
- Idempotent requests. Business services call the notification API with an `Idempotency-Key` header, so a retried request never sends a second message.
