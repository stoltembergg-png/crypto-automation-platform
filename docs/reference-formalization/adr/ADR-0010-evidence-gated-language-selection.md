# ADR-0010: Evidence-Gated Language Selection

**Status:** Proposed — Q-009 required.

## Decision
Record Next.js + TypeScript frontend and Rust critical-backend as user preferences, not selected implementation technologies. Select only after a documented evaluation of threat fit, determinism/performance, ecosystem maturity, toolchain/reproducibility, testability, operability, interoperability and team constraints.

## Consequences
No architecture or workload claim is fabricated to favor a language. Selection must be revisited upon materially changed requirement/toolchain evidence.
