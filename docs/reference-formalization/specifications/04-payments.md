# SDD-04 — Payment Lifecycle and Accounting Correlation

**Status:** Proposed. Payment support requires Q-001, Q-002 and Q-004; this is not a provider capability claim.

## Lifecycle facts
A payment is a correlated workflow, never one mutable status. Required facts: `PAYMENT_RECEIVED`, `PAYMENT_VALIDATED`, `PAYMENT_AUTHORIZED`, `PAYMENT_CAPTURE_REQUESTED`, `PAYMENT_CAPTURE_EVIDENCED`, `PAYMENT_FEE_ASSESSED`, `PAYMENT_SETTLEMENT_OBSERVED`, `PAYMENT_REVERSAL_OBSERVED`, `PAYMENT_REFUND_REQUESTED`, `PAYMENT_REFUND_EVIDENCED`, `PAYMENT_CORRECTION_PROPOSED`, `PAYMENT_MALFORMED`, `PAYMENT_CONFLICT`, and `PAYMENT_RECONCILIATION_REQUIRED`.

## State machine
`RECEIVED → VALIDATED → AUTHORIZED → CAPTURE_REQUESTED → CAPTURE_EVIDENCED → SETTLEMENT_OBSERVED → RECONCILED`; each transition can enter `MALFORMED`, `CONFLICT`, `EXPIRED`, or `RECONCILIATION_REQUIRED`. Reversal/refund and correction are independent, versioned workflows; their external observation does not itself post a balance change.

## Controls
- Provider/webhook payloads are untrusted and tenant-bound before idempotency evaluation.
- Idempotency scope is tenant + provider + provider-object reference + event type + schema version; identical repeats return `DUPLICATE`, semantically divergent reuse returns `CONFLICT`.
- Fee, refund, reversal, settlement and correction accounting rules must be supplied by Q-004. Every accounting command references the associated evidence/correlation and authority decision.
- Missing, malformed, out-of-order, conflicting or late facts create an exception/reconciliation record; they never cause heuristic balance repair.

## Test matrix
Generate all lifecycle permutations including duplicate/out-of-order webhook, capture success with missing settlement, fee mismatch, partial refund, reversal after settlement, correction attempt, conflict, malformed input and cross-tenant reference. Assert exact typed disposition, no duplicate post and a complete audit/correlation trail.
