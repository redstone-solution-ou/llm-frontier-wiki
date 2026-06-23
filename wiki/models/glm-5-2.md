# GLM-5.2

> **Short name:** `glm-5-2` · **Vendor:** Zhipu AI (智谱 AI) · **Released:** 2026 · **Effort tiers tracked:** not disclosed per submission

## What it is

The current flagship reasoning-and-agent model from Zhipu AI's GLM
line, and the successor to GLM-5.1 (which this leaf previously
tracked). The wiki tracks GLM-5.2 specifically because it is the
**strongest open-weights model on the wiki's primary long-horizon
agentic coherence benchmark**, [Vending-Bench 2](../benchmarks/vending-bench-2.md),
where it now sits at **rank 2** — ahead of [Claude Opus 4.6](claude-opus-4-7.md)
and behind only [Claude Opus 4.7](claude-opus-4-7.md). That makes
GLM-5.2 the canonical answer to "what is the best long-horizon agentic
model available without a closed-vendor relationship", and the first
open-weights model to pass the strongest closed Western model of the
previous generation on this eval.

## Scores on tracked benchmarks

| Benchmark | Score | Effort tier | Filed | Source |
|-----------|-------|-------------|-------|--------|
| [Vending-Bench 2](../benchmarks/vending-bench-2.md) | **$8,313.78** (rank 2, 5-run avg) | not disclosed | 2026-06 | [Andon Labs](https://andonlabs.com/evals/vending-bench-2) (accessed 2026-06-23) |
| [FrontierMath Tier 4 (v2)](../benchmarks/frontiermath.md) | not in top-5 | — | — | — |
| [DeepSWE](../benchmarks/deepswe.md) | not on the public leaderboard | — | — | — |
| [SWE-PRBench](../benchmarks/swe-prbench.md) | not in paper baseline | — | — | — |

The GitHub repository [zai-org/GLM-5](https://github.com/zai-org/GLM-5)
positions the line as "from vibe coding to agentic engineering" —
i.e. it is explicitly tuned for long-horizon agent loops rather than
pure-reasoning benchmark optimization.

## Where this model sits on the axes

- **Long-horizon agentic coherence:** **Rank 2 on the public
  leaderboard, and the top non-Anthropic entry.** GLM-5.2's $8,313.78
  on Vending-Bench 2 edges *above* Claude Opus 4.6 ($8,017.59) and is
  the best open-weights result by a wide margin. The gap to the leader,
  Claude Opus 4.7 at $10,936.76, is ~$2,600. Andon Labs' frontier-lag
  analysis fits the Chinese SOTA trend at +$1,047/month (R² = 0.98)
  versus the Western +$799/month, lagging by ~131 days with a projected
  crossover around August 2027 — GLM-5.2 is the current data point
  anchoring that Chinese-frontier slope.
- **Frontier reasoning:** **Not on the top-5 public ranking.**
  GLM-5.2 has not filed a top-5 FrontierMath Tier 4 v2 score. The
  model's positioning is explicitly agent-leaning, and the wiki
  treats this as a real capability split rather than a missing
  measurement.

## When to pick this model

Pick GLM-5.2 when:

- The job is long-horizon agentic and an **open-weights model is
  required** — privacy constraints, on-premise deployment,
  fine-tuning, or vendor-independence requirements. It is now the
  best-scoring option in that constraint set, ahead of the previous
  Western closed leader (Opus 4.6).
- The job is in the same shape as Vending-Bench 2 (multi-day /
  multi-hour autonomous business agent) but the Anthropic Opus 4.7
  leader is out of reach (cost, access, or vendor policy).

Do not pick GLM-5.2 when:

- The job demands the absolute long-horizon ceiling — Claude Opus 4.7
  leads Vending-Bench 2 by ~$2,600.
- The job demands the absolute reasoning ceiling — GLM-5.2 is not
  on the top of any reasoning leaderboard.

## Known caveats

- **Operator-run leaderboard entry.** Andon Labs runs and reports the
  Vending-Bench 2 eval itself on its own harness; the figure is not a
  standardized multi-vendor re-run, and the score reflects model +
  scaffold jointly.
- **Reasoning-axis absence is informative.** The wiki interprets
  GLM-5.2's absence from FrontierMath Tier 4 v2 top-5 as a real
  capability gap on the reasoning axis, not as a missing evaluation;
  the leaderboard is open to submissions and the model is
  well-resourced.
- **Cost efficiency is a standout.** Andon Labs' score-vs-cost-per-run
  analysis plots GLM-5.2 toward the high-score / low-cost corner —
  materially cheaper per run than the Anthropic Opus or OpenAI GPT
  lines at a comparable score. "Long-horizon agentic dollars per
  benchmark dollar" is a metric the wiki does not yet track formally
  but on which GLM-5.2 is the leader.

## Related wiki pages

- [../frontier-leaderboard.md](../frontier-leaderboard.md)
- [../benchmarks/vending-bench-2.md](../benchmarks/vending-bench-2.md)
- [../concepts/long-horizon-agentic-coherence.md](../concepts/long-horizon-agentic-coherence.md)
- [gemini-3-pro.md](gemini-3-pro.md) — the Google sibling on the same
  benchmark.
- [claude-opus-4-7.md](claude-opus-4-7.md) — the long-horizon-axis
  leader (Opus 4.7) and the Opus 4.6 entry GLM-5.2 now sits above.
