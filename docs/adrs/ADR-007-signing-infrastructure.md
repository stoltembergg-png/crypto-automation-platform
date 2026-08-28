# Signing infrastructure

**Status:** Proposed

## Context
Financial automation needs a decision that is explicit about evidence limits, authority and rollback.

## Decision
Per-operation signer request is guarded/decoded/allowlisted and binds authorization hash, scope and environment. Provider/key ceremony decision is evidence-gated.

## Consequences
Future implementation cards must bind this ADR version, add negative tests, record owner/revalidation trigger and preserve deny-by-default. A contradiction requires a superseding ADR and adversarial review.

## Evidence status
Planning decision only; it is not provider, legal, runtime or production proof.
