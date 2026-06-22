# Concepts

The cross-cutting ideas the wiki uses to interpret benchmark
numbers and rank Large Language Models (LLMs). Two of the four
pages are *organizing axes* — the wiki's claim is that frontier
capability is best read on two axes rather than one aggregate
score. The remaining two pages are supporting concepts that the
axis pages depend on.

## The two organizing axes

- [long-horizon-agentic-coherence.md](long-horizon-agentic-coherence.md) —
  the wiki's term for the user's "long-term execution / planning"
  intuition. Measures whether a model holds its identity, tool
  use, and decision-making together across thousands of agentic
  steps without drifting, looping, or hallucinating prior
  context. Primary benchmark:
  [Vending-Bench 2](../benchmarks/vending-bench-2.md).
- [frontier-reasoning.md](frontier-reasoning.md) — the wiki's
  term for the user's "intellectual capability" intuition.
  Measures the ceiling on research-grade reasoning problems
  under a hard inference-token budget but without time-per-step
  pressure. Primary benchmark:
  [FrontierMath](../benchmarks/frontiermath.md) Tier 4 (v2).

The two axes are *orthogonal* — the same model can lead one and
lag on the other. The wiki's
[frontier leaderboard](../frontier-leaderboard.md) defends that
claim with the current data.

## Supporting concepts

- [reasoning-effort.md](reasoning-effort.md) — vendor-exposed
  effort tiers (`xhigh`, `max`, etc.) are part of every benchmark
  row; ignoring them produces apparent contradictions between
  leaderboards that are actually agreements once effort is
  matched.
- [agentic-scaffolding.md](agentic-scaffolding.md) — every
  benchmark on the long-horizon coherence axis scores model +
  scaffold jointly. Apparent leaderboard contradictions usually
  trace to vendor-scaffold vs standardized-scaffold differences.

## Related wiki pages

- [../benchmarks/benchmarks.md](../benchmarks/benchmarks.md) — the
  four benchmarks the wiki tracks, each placed on one axis.
- [../frontier-leaderboard.md](../frontier-leaderboard.md) — the
  2D ranking page.
- [../overview.md](../overview.md) — the longer-form story behind
  the two-axis structure.
