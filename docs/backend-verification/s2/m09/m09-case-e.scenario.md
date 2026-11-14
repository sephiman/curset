# URL shortener and distributed ID generation

A company runs a public URL shortener. A short link such as `sho.rt/Xk3pQ9` maps to a long URL, and the service creates about 5,000 new links per second while serving 50 times as many redirects. Links must never collide, and the identifier of a new link must be created on any of 20 stateless nodes without asking a central allocator.

The team is comparing how to generate the identifiers and how to store the mapping:

- A central auto-increment sequence is easy to reason about, but every node would have to coordinate with it for each new link.
- UUIDs avoid coordination. Some are random, some embed a timestamp, and the team has to choose a version that suits an indexed link table.
- The mapping is held in Redis Cluster, which splits the key space into hash slots. Related keys, such as the click counters of one link, should land in the same slot.
- Other designs in the team's reading list place keys on a consistent hashing ring with virtual nodes, as Dynamo does, so the effect of adding or removing a node is limited.
