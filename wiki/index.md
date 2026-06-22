# Wiki Index

Flat catalog of every page in this wiki. One line per page. First
stop at query time. Kept in sync with every add, rename, or delete.
Pages within a section are sorted alphabetically.

## Root

- [overview.md](overview.md) — entry point, the two-axis story,
  knowledge-graph sketch.
- [frontier-leaderboard.md](frontier-leaderboard.md) — the 2D
  ranking page; every tracked model placed on (frontier reasoning,
  long-horizon agentic coherence).
- [index.md](index.md) — this file.
- [log.md](log.md) — append-only chronological record.

## Concepts

- [concepts/concepts.md](concepts/concepts.md) — section hub for
  the two organizing axes and supporting concepts.
- [concepts/agentic-scaffolding.md](concepts/agentic-scaffolding.md)
  — the harness layer that benchmarks score jointly with the
  model; load-bearing for any long-horizon claim.
- [concepts/frontier-reasoning.md](concepts/frontier-reasoning.md)
  — axis 1; ceiling on research-grade intellectual problems.
  Primary signal: FrontierMath Tier 4 (v2).
- [concepts/long-horizon-agentic-coherence.md](concepts/long-horizon-agentic-coherence.md)
  — axis 2; coherent identity, tool use, decision-making across
  thousands of agentic steps. Primary signal: Vending-Bench 2.
- [concepts/reasoning-effort.md](concepts/reasoning-effort.md) —
  vendor effort tiers (`[xhigh]`, `[max]`, etc.) and how they
  appear on every leaderboard row.

## Benchmarks

- [benchmarks/benchmarks.md](benchmarks/benchmarks.md) — section
  hub for the four tracked benchmarks.
- [benchmarks/deepswe.md](benchmarks/deepswe.md) — DeepSWE.net,
  2026. 113 original SWE tasks, short briefs / multi-file long
  solutions, behavioral verifiers. Long-horizon coding sub-axis.
- [benchmarks/frontiermath.md](benchmarks/frontiermath.md) —
  Epoch AI, v2 released 2026-06-12. 338 unpublished mathematics
  problems split into Tiers 1–3 (295) and Tier 4 (43). Primary
  signal for the frontier reasoning axis.
- [benchmarks/harness-bench.md](benchmarks/harness-bench.md) —
  Peking University + Qiyuan Tech, 2026-05 (arXiv:2605.27922).
  106 tasks × 6 harnesses × 8 model backends = 5,194
  trajectories. Headline: 23.8-point harness gap on the same
  model-backend pool. Canonical empirical anchor for agentic
  scaffolding.
- [benchmarks/swe-prbench.md](benchmarks/swe-prbench.md) — Foundry
  AI, arXiv:2603.26130. 350 pull-request reviews across three
  context configurations; the canonical demonstration of
  long-context attention degradation.
- [benchmarks/vending-bench-2.md](benchmarks/vending-bench-2.md) —
  Andon Labs, 2026. 1-year simulated vending-machine business,
  $500 starting capital, $2/day fee, 60–100M tokens per run.
  Primary signal for the long-horizon agentic coherence axis.

## Models

- [models/models.md](models/models.md) — section hub for the six
  tracked frontier models.
- [models/claude-fable-5.md](models/claude-fable-5.md) — Anthropic,
  2026. Frontier reasoning leader at 87.8% ±5.2 on FrontierMath
  Tier 4 v2.
- [models/claude-opus-4-7.md](models/claude-opus-4-7.md) —
  Anthropic, 2026. Working pick for long-horizon agentic
  coherence; Opus 4.6 baseline is $8,017.59 on Vending-Bench 2.
- [models/claude-opus-4-8.md](models/claude-opus-4-8.md) —
  Anthropic, 2026. Alignment-tuned successor; DeepSWE rank-2 at
  58% ±5% but documented Vending-Bench 2 regression vs Opus 4.6.
- [models/gemini-3-pro.md](models/gemini-3-pro.md) — Google
  DeepMind, late 2025 / early 2026. Vending-Bench 2 rank-3 at
  $5,478.16.
- [models/glm-5-1.md](models/glm-5-1.md) — Zhipu AI, 2026. Open-
  weights pick; Vending-Bench 2 rank-2 at $5,634.41.
- [models/gpt-5-5.md](models/gpt-5-5.md) — OpenAI, 2026 (with
  GPT-5.5 Pro variant). DeepSWE rank-1 at 70% ±4%, FrontierMath
  Tier 4 v2 rank-2 (Pro) at 78.0% ±6.5.
