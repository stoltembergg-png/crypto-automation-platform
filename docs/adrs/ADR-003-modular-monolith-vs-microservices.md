# Modular monolith vs microservices

**Status:** Accepted for planning

## Context
Financial automation needs a decision that is explicit about evidence limits, authority and rollback.

## Decision
Use a modular monolith with owned persistence, dependency checks, transaction kernel and broker-neutral contracts. Extract only with workload/isolation/ownership evidence.

## Consequences
Future implementation cards must bind this ADR version, add negative tests, record owner/revalidation trigger and preserve deny-by-default. A contradiction requires a superseding ADR and adversarial review.

## Evidence status
Planning decision only; it is not provider, legal, runtime or production proof.
