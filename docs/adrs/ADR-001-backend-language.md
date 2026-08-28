# Backend language selection

**Status:** Proposed

## Context
Financial automation needs a decision that is explicit about evidence limits, authority and rollback.

## Decision
Choose a language-neutral safety contract first. Rust is a user-preferred candidate; acceptance needs documented team/tooling, deterministic numeric, database, observability and benchmark spike evidence before runtime kernels are implemented.

## Consequences
Future implementation cards must bind this ADR version, add negative tests, record owner/revalidation trigger and preserve deny-by-default. A contradiction requires a superseding ADR and adversarial review.

## Evidence status
Planning decision only; it is not provider, legal, runtime or production proof.
