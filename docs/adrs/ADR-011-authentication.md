# Authentication

**Status:** Accepted for planning

## Context
Financial automation needs a decision that is explicit about evidence limits, authority and rollback.

## Decision
Passkey-first WebAuthn, session rotation, step-up for sensitive actions, tenant authorization and wallet proof as additional identity evidence only.

## Consequences
Future implementation cards must bind this ADR version, add negative tests, record owner/revalidation trigger and preserve deny-by-default. A contradiction requires a superseding ADR and adversarial review.

## Evidence status
Planning decision only; it is not provider, legal, runtime or production proof.
