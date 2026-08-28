# State-Machine Invariants and Test Obligations

## Global invariants
1. Only an accepted, current, tenant/environment-bound authority decision may progress a privileged flow.
2. Every invalid transition returns a typed denial and creates no privileged external effect or accounting post.
3. Posted accounting events are immutable, balanced and corrected only by linked compensating events.
4. Evidence/delivery/reconciliation states do not imply accounting/settlement state.
5. A withdrawal’s availability lock appears at most once for its logical intent; broadcast ambiguity prevents automatic second mutation.

## Required machines
- Proposal: `DRAFT → VALIDATED → POLICY_EVALUATED → DENIED|REQUIRES_LEGAL_REVIEW|AWAITING_AUTHORIZATION → AUTHORIZED → CONSUMED|EXPIRED|REVOKED`.
- Payment: `RECEIVED → VALIDATED → AUTHORIZED → CAPTURE_REQUESTED → CAPTURE_EVIDENCED → SETTLEMENT_OBSERVED → RECONCILED` plus fee/reversal/refund/correction/malformed/conflict branches.
- Withdrawal: `INTENT_CREATED → LOCK_POSTED → AUTHORIZED → BROADCAST_REQUESTED → BROADCAST_EVIDENCED|BROADCAST_AMBIGUOUS|BROADCAST_REJECTED → CONFIRMED|FAILED|REORGED`.
- Order: `PROPOSED → RISK_ALLOWED → SUBMITTED → ACKNOWLEDGED → PARTIALLY_FILLED* → FILLED|CANCELLED|REJECTED|UNKNOWN`.
- LP: `PROPOSED → RISK_ALLOWED → MINT_REQUESTED → ACTIVE → REBALANCE_REQUESTED|EXIT_REQUESTED → CLOSED|UNKNOWN`.
- Reconciliation: `OPEN → EVIDENCE_COLLECTING → MATCHED|MISSING_EVIDENCE|CONFLICT|STALE|REORGED → CORRECTION_PROPOSED? → CLOSED`.

Model tests enumerate or generate legal/illegal transitions, duplicate/replay permutations and failure interruptions. They explicitly cover payment fee/reversal/refund/settlement/correction/malformed/conflict; withdrawal ambiguity; venue reorg/finality and partial fills; DEX/LP drift; and tenant/auth/policy/environment revocation.
