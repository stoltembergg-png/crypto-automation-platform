# Chains

**Status:** Proposed

## Context
Financial automation needs a decision that is explicit about evidence limits, authority and rollback.

## Decision
EVM-family adapter contract is initial candidate; each chain requires per-network claim/finality/token/RPC evidence. Solana is a separate future adapter family.

## Consequences
Future implementation cards must bind this ADR version, add negative tests, record owner/revalidation trigger and preserve deny-by-default. A contradiction requires a superseding ADR and adversarial review.

## Evidence status
Planning decision only; it is not provider, legal, runtime or production proof.
