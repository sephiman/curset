# Booking and inventory under high contention

A ticketing company sells seats for a stadium concert. When sales open, tens of thousands of users compete for the same few thousand seats within minutes. The seats and bookings live in a PostgreSQL database, and the same seat must never be sold twice.

Users first hold a seat for a few minutes and then pay. The hold runs in a short transaction that selects the seat row and marks it taken. Several teams argue about how to write that transaction:

- Use explicit row-level locks with `SELECT … FOR UPDATE`, with or without `NOWAIT` or `SKIP LOCKED`, so competing holds do not wait for each other for long.
- Run the transactions at `REPEATABLE READ` or `SERIALIZABLE` and retry on failure, instead of locking by hand.
- Guard a room or a whole event with a Redis distributed lock where a database lock is not enough.

Mobile clients time out and retry, so the booking endpoints must be safe to repeat. The API accepts an `Idempotency-Key` header on `POST /bookings`, and the team needs to decide which HTTP status codes answer a repeated, a conflicting and an incomplete request.
