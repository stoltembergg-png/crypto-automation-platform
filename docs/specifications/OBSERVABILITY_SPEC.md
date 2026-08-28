# Observability Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines OpenTelemetry traces, structured redacted logs, metrics, dashboards and alerts.

## Normative requirements

- Metrics: trade success/failure, expected/realized profit, slippage, latency, gas, RPC failures, exchange errors, strategy PnL, LP fees/IL, withdrawal failure and reconciliation mismatch.
- Correlation IDs span UI/API/ledger/provider/adapter/audit without secret/PII leakage.
- Alert rules map to an owner and kill-switch/reconciliation runbook.

## Component contracts

TraceContext, MetricSeries, AlertRule, RunbookRef, HealthSignal.

## Invariants and deny conditions

Telemetry is bounded and redacted; missing telemetry cannot authorize action. Alert acknowledgement is not issue resolution.

## State and failure semantics

EMITTED→CORRELATED→ALERTED→ACKNOWLEDGED→RESOLVED; disabled exporter creates health signal.

## Future verification

Trace propagation, redaction, cardinality, alert routing, exporter outage and runbook exercise tests.

## Queue ownership

Implementation is decomposed in `PR-117..PR-122`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/09-reconciliation-audit-observability.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
