# Claude Opus 4.8

> **Short name:** `claude-opus-4-8` · **Vendor:** Anthropic · **Released:** 2026 (mid-year) · **Effort tiers tracked:** `[max]`

## What it is

The most recent Anthropic Opus generation as of 2026-06. Positioned
by Anthropic as a step forward in alignment relative to
[Opus 4.7](claude-opus-4-7.md) and Opus 4.6, with documented
trade-offs on the
[long-horizon agentic coherence](../concepts/long-horizon-agentic-coherence.md)
axis: the [Andon Labs blog post on Opus 4.8 and Vending-Bench](https://andonlabs.com/blog/opus-4-8-vending-bench)
characterizes the model as "better alignment, worse performance" on
Vending-Bench 2 and Vending-Bench Arena. This makes Opus 4.8 the
single cleanest worked example of the wiki's two-axis thesis:
alignment tuning can be measured as a regression on one axis even
when it is an improvement on others.

## Scores on tracked benchmarks

| Benchmark | Score | Effort tier | Filed | Source |
|-----------|-------|-------------|-------|--------|
| [DeepSWE](../benchmarks/deepswe.md) | 58% ±5% | `[max]` | 2026-05 | [deepswe.net](https://deepswe.net/) |
| [FrontierMath Tier 4 (v2)](../benchmarks/frontiermath.md) | 56.1% ±7.8 | `[max]` | 2026-06 | [LM Council mirror](https://lmcouncil.ai/benchmarks) |
| [FrontierMath Tiers 1–3 (v2)](../benchmarks/frontiermath.md) | 80.0% ±2.4 | `[max]` | 2026-06 | [LM Council mirror](https://lmcouncil.ai/benchmarks) |
| [Vending-Bench 2](../benchmarks/vending-bench-2.md) | not on public leaderboard; vendor-reported as **below Opus 4.6's $8,017.59** | not disclosed | 2026-06 | [Andon Labs blog](https://andonlabs.com/blog/opus-4-8-vending-bench) |
| [SWE-PRBench](../benchmarks/swe-prbench.md) | not in paper baseline | — | — | — |

## Where this model sits on the axes

- **Frontier reasoning:** **Top-5, mid-frontier.** 56.1% ±7.8 on
  FrontierMath Tier 4 v2 (rank 5) and 80.0% ±2.4 on Tiers 1–3
  (rank 4). Clearly a frontier-tier reasoner, but ~30 percentage
  points behind [Fable 5](claude-fable-5.md) on Tier 4 and ~7
  points behind on Tiers 1–3. The model is competitive on
  medium-difficulty reasoning and not the right pick at the
  ceiling.
- **Long-horizon agentic coherence:** **Top tier on coding,
  regressed on business sim.** Opus 4.8 leads its Anthropic
  siblings on [DeepSWE](../benchmarks/deepswe.md) (58% ±5% vs Opus
  4.7's 54% ±5%) — i.e. on long-horizon coding specifically, Opus
  4.8 is the strongest Anthropic option. On the broader
  Vending-Bench 2 / Vending-Bench Arena business-simulation
  variants, Anthropic's own commentary documents a regression vs
  Opus 4.6 / 4.7. This is one of the rare model leafs where
  intra-axis position is *not* a single number.

## When to pick this model

Pick Opus 4.8 when you want:

- The strongest Claude-line model on **long-horizon coding** as
  measured by DeepSWE (58% ±5%).
- A frontier-reasoning model that is materially cheaper / better-
  aligned than Fable 5 and is acceptable at ~56% on Tier 4 — i.e.
  graduate-level mathematics support but not research-level
  problem solving.

Do not pick Opus 4.8 when:

- The job is a multi-hour autonomous business agent — Opus 4.6 /
  4.7 are the documented stronger picks on Vending-Bench 2 /
  Arena. Anthropic's own blog acknowledges this.
- The job requires the absolute reasoning ceiling — Fable 5 is
  ~30 points stronger on Tier 4.

## Known caveats

- **Documented alignment-vs-coherence trade-off.** Anthropic's own
  blog and Andon Labs' coverage describe Opus 4.8 as a Vending-Bench
  / Vending-Bench Arena / Blueprint-Bench 2 *regression* vs Opus
  4.6 while being a step forward in alignment. The trade-off is
  unusually well-documented and is the canonical example for the
  wiki's [agentic-scaffolding](../concepts/agentic-scaffolding.md)
  and [reasoning-effort](../concepts/reasoning-effort.md) concepts.
- DeepSWE position depends on the `[max]` effort tier; default-
  effort deployment will score below 58%.
- The FrontierMath Tier 4 ±7.8 confidence interval is large; rank
  is robust to the interval but the gap to GPT-5.5 `[xhigh]`
  (72.5% ±7.1) is not statistically clean.

## Related wiki pages

- [../frontier-leaderboard.md](../frontier-leaderboard.md)
- [../benchmarks/deepswe.md](../benchmarks/deepswe.md)
- [../benchmarks/frontiermath.md](../benchmarks/frontiermath.md)
- [../concepts/long-horizon-agentic-coherence.md](../concepts/long-horizon-agentic-coherence.md)
- [claude-opus-4-7.md](claude-opus-4-7.md) — the prior-generation
  Anthropic sibling.
- [claude-fable-5.md](claude-fable-5.md) — the reasoning-axis
  sibling.
