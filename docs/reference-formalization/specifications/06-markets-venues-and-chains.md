# SDD-06 — Markets, Exchanges, Venues and Chains

**Status:** generic contract specification. It identifies no supported provider, exchange, asset, network or chain.

## Provider claim register
Before a venue/chain/wallet adapter is selected or described as supported, create an owned claim record with: claim ID; provider/product/region/version; exact operation/resource boundary; source URL or contract plus configuration snapshot digest; accountable owner; security and legal disposition; expiry; revocation process; boundary-test requirement/result; and contradiction/incident link. Claims are capability facts, not a global vendor label. Expired, untested, revoked, unsupported or legally unresolved claims deny use.

## Market and venue contract
Market data is an observation carrying source/sequence/timestamp/latency, instrument definition, quantity/price units, confidence/freshness and correlation. An order intent carries tenant, instrument, side, quantity/limit/risk constraints, policy/risk/authorization hashes and idempotency. A venue order workflow separates `SUBMITTED`, `ACKNOWLEDGED`, `PARTIALLY_FILLED`, `FILLED`, `CANCELLED`, `REJECTED`, `UNKNOWN` and reconciliation facts. Partial fill is a quantity-specific fact, not a boolean success.

## Chain observations
Chain data includes network/chain identifier, block/slot reference, transaction/log reference, confirmation/finality policy version, observed time, parser version and reorg lineage. It is untrusted until chain-specific validation. Reorg/finality thresholds are venue/asset/network-scoped and must be supplied by Q-005; no universal confirmation rule is assumed.

## Integration failure containment
Adapters expose normalized broker-neutral events through local outbox/inbox contracts while preserving raw evidence safely. Timeouts, rate limits, malformed payloads, duplicate events, gaps and conflicts quarantine/correlate rather than mutating Ledger state. No broker/service is required until workload evidence proves it.

## Tests
Contract/property tests cover stale data, non-monotonic sequence, wrong units, partial-fill/cancel race, duplicate order reference, provider error, timeout, unknown acknowledgement, reorg and finality transition. Every test asserts tenant isolation and no direct ledger mutation.
