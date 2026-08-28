# DEX abstraction

**Status:** Accepted for planning

## Context
Financial automation needs a decision that is explicit about evidence limits, authority and rollback.

## Decision
Use protocol registry, decoded finite action templates, simulation and transaction guard. No arbitrary router/calldata or implicit protocol admission.

## Consequences
Future implementation cards must bind this ADR version, add negative tests, record owner/revalidation trigger and preserve deny-by-default. A contradiction requires a superseding ADR and adversarial review.

## Evidence status
Planning decision only; it is not provider, legal, runtime or production proof.
