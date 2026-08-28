# Database

**Status:** Accepted for planning

## Context
Financial automation needs a decision that is explicit about evidence limits, authority and rollback.

## Decision
PostgreSQL is initial authoritative relational store for ledger, inbox/outbox, audit projections and tenant policies; no external broker without workload evidence.

## Consequences
Future implementation cards must bind this ADR version, add negative tests, record owner/revalidation trigger and preserve deny-by-default. A contradiction requires a superseding ADR and adversarial review.

## Evidence status
Planning decision only; it is not provider, legal, runtime or production proof.
