# Risk Policy Catalog

This catalog is a planning boundary for deterministic Risk Engine policies. It is not a live configuration.

## Initial policy namespaces

- Exposure: asset, protocol, chain, exchange, bridge, stablecoin, smart contract, user and strategy.
- Loss and capital: daily loss, drawdown, per-trade, daily volume, capital reserve and open positions.
- Market: staleness, depth, slippage, price impact, expected net profit, gas percentage and quote TTL.
- Operational: provider claim, environment attestation, reconciliation mismatch, audit health and kill-switch status.
- Authorization: legal disposition, automation mode, policy version, simulation result and transaction-guard verdict.

Every policy evaluation is tenant/environment scoped, versioned, correlated and expiry-bound. Unknown data, missing evidence, stale policy, a kill switch or an unresolved legal/provider/custody gate returns `DENY` or `REQUIRES_REVIEW`; it cannot be made permissive by AI output.

See `docs/specifications/RISK_ENGINE_SPEC.md` and `.planning/contracts/POLICY_DECISION.md` for the normative contract.
