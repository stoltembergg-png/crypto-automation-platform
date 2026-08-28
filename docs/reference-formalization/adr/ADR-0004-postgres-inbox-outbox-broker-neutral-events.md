# ADR-0004: Postgres Inbox/Outbox and Broker-Neutral Events First

**Status:** Proposed.

## Decision
Use a capability-scoped local transaction kernel with Postgres inbox/outbox as the first integration mechanism. Domain event contracts are broker-neutral.

## Consequences
Local persistence/event recording can be atomic; external provider delivery cannot. Do not introduce a broker or distributed services without documented throughput, durability, ordering, isolation and operating evidence.
