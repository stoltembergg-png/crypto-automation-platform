# Better Harness Execution Blocker

**Status:** BLOCKED — no Better Harness report generated.

The `/better-harness` skill was loaded and its canonical runner location was checked after the earlier stale-path attempt:

```text
C:\Users\Gabriel\AppData\Local\hermes\skills\better-harness\scripts\better-harness.mjs
```

The runner is absent (`RUNNER_MISSING`). Per the skill, no substitute report may be hand-written and no other cache/runtime may be searched by order. This is a harness-tooling blocker only; it is not planning, product-security, legal, provider, or mainnet evidence.

**Resumption condition:** the skill owner restores that exact runner path; then execute `harness evidence-bundle` and the three independent evidence passes specified by the skill.
