# Telemetry and event ingestion pipeline

A fleet-management company receives position and engine events from 400,000 vehicles. Each vehicle sends a small event every few seconds, and traffic peaks in bursts when many vehicles reconnect at once. The pipeline must accept the events without losing them, keep each vehicle's events together, and let analysts query metrics a few seconds later.

The design the team is discussing has four stages:

- Ingest. An edge service writes every event to Kafka. Producers batch and compress the events, and the topic is keyed by vehicle owner so that one owner's events stay together.
- Broker. Kafka stores events in a log on commodity disks and serves consumers from the page cache. Shared clusters give each client group a quota per broker.
- Stream processing. A Flink job aggregates the events into per-minute metrics and takes checkpoints. Some jobs need very low latency and some need strong guarantees.
- Storage. The aggregated metrics go to a replicated key-value store that replicates each item on several nodes and uses read and write quorums.
