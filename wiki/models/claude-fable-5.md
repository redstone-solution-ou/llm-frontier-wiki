# Claude Fable 5

> **Short name:** `claude-fable-5` · **Vendor:** Anthropic · **Released:** 2026 (first half) · **Effort tiers tracked:** `[max]`

## What it is

A 2026-generation Claude model from Anthropic, positioned as the
top-of-stack reasoning-leaning frontier model. The model is the
current leader on the wiki's
[frontier reasoning](../concepts/frontier-reasoning.md) axis and a
mid-pack entry on the
[long-horizon agentic coherence](../concepts/long-horizon-agentic-coherence.md)
axis. It is the cleanest current example of the wiki's two-axis
thesis: leading the reasoning ceiling does not imply leading
agentic suitability.

## Scores on tracked benchmarks

| Benchmark | Score | Effort tier | Filed | Source |
|-----------|-------|-------------|-------|--------|
| [FrontierMath Tier 4 (v2)](../benchmarks/frontiermath.md) | 87.8% ±5.2 | `[max]` | 2026-06 | [LM Council mirror](https://lmcouncil.ai/benchmarks) |
| [FrontierMath Tiers 1–3 (v2)](../benchmarks/frontiermath.md) | 87.0% ±2.0 | `[max]` | 2026-06 | [LM Council mirror](https://lmcouncil.ai/benchmarks) |
| [Vending-Bench 2](../benchmarks/vending-bench-2.md) | $5,680.26 (rank 10, 5-run avg, `- High`) | High | 2026-06 | [Andon Labs](https://andonlabs.com/evals/vending-bench-2) (accessed 2026-06-23) |
| [DeepSWE](../benchmarks/deepswe.md) | not on the public leaderboard | — | — | — |
| [SWE-PRBench](../benchmarks/swe-prbench.md) | not in paper baseline | — | — | — |

## Where this model sits on the axes

- **Frontier reasoning:** **Rank 1.** 87.8% ±5.2 on FrontierMath
  Tier 4 v2 is ~10 percentage points clear of the second-place
  base model (GPT-5.5 Pro at 78.0% ±6.5). Fable 5 narrowly trails
  GPT-5.5 Pro on Tiers 1–3 (87.0% vs 87.7%) but opens the gap on
  the harder tier — the signature of a model whose ceiling sits
  above the rest of the frontier.
- **Long-horizon agentic coherence:** **Mid-pack.** The
  $5,680.26 five-run-average figure on Vending-Bench 2 (rank 10,
  `- High`) puts Fable 5 in roughly the same band as Claude Opus
  4.8 ($5,787.43, rank 9) and well below the leader Claude Opus 4.7
  ($10,936.76). The vendor / secondary commentary describes Fable 5
  as a reasoning-leaning rather than agent-leaning generation.

## When to pick this model

Pick Fable 5 when the job is dominated by hard intellectual
problems and the inference loop is short — graduate-level
mathematics assistance, research-grade proof outlining, or any
single-shot evaluation where the question is well-specified and
the model has the time it needs to think. Do not pick Fable 5
as the unsupervised agent in a multi-hour business loop; pick a
model that leads the
[long-horizon agentic coherence](../concepts/long-horizon-agentic-coherence.md)
axis (Opus 4.7) for that job.

## Known caveats

- The Vending-Bench 2 figure is the official five-run average
  (rank 10, `- High` effort tier); earlier wiki snapshots labeled
  it a single best-run estimate, which the current board corrects.
- Tier 4 confidence interval is ±5.2 percentage points. The 10-
  point gap to the second-place base model is robust to that
  interval, but the absolute number could move within it on
  re-evaluation.
- The "AI co-mathematician" entry (third on Tier 4 v2 at 75.6%) is
  a *system*, not a base-model comparison. Fable 5's lead is
  against base models; system-level ensembles sit between Fable 5
  and the rest.
- `[max]` effort is expensive. Default-effort deployment scores
  would be lower; the leaderboard number is the
  upper-bound configuration.

## Related wiki pages

- [../frontier-leaderboard.md](../frontier-leaderboard.md)
- [../benchmarks/frontiermath.md](../benchmarks/frontiermath.md)
- [../benchmarks/vending-bench-2.md](../benchmarks/vending-bench-2.md)
- [../concepts/frontier-reasoning.md](../concepts/frontier-reasoning.md)
- [../concepts/reasoning-effort.md](../concepts/reasoning-effort.md)
