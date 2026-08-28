# Testing Strategy

## Evidence levels
Planning integrity is not product proof. Future proof is tiered: unit → contract → property/model → integration sandbox → paper replay → testnet → controlled mainnet gate. A skip, no-test run, mock-only path or stale SHA is `NO_PROOF`.

## Non-vacuous suites
- Ledger: balance/conservation/idempotency/compensation property tests.
- State machines: generated legal/illegal/retry/expiry/revocation transitions.
- Contracts: producer/consumer schema compatibility, unknown version/action and envelope replay.
- Security: tenant substitution, capability attenuation, secret redaction, forged webhook, malicious proposal/calldata.
- Chaos: provider/RPC/database/cache outage, timeout, duplicate/reordered event, gas spike, reorg, partial fill.
- Architecture: forbidden dependency/write and privileged bypass tests.
- Release: exact-SHA CI, SBOM/provenance, migration replay, rollback and environment isolation.

Every future acceptance test uses `@spec:AC-...` and a PR/requirement trace reference. No future task is complete until the test runner and ONP audit are green.
