# Custody

**Status:** Proposed

## Context
Financial automation needs a decision that is explicit about evidence limits, authority and rollback.

## Decision
No custody model is legally selected. Evaluate hybrid/MPC/HSM/multisig/custodian under Q-001..Q-004; direct private-key storage is prohibited.

## Consequences
Future implementation cards must bind this ADR version, add negative tests, record owner/revalidation trigger and preserve deny-by-default. A contradiction requires a superseding ADR and adversarial review.

## Evidence status
Planning decision only; it is not provider, legal, runtime or production proof.
