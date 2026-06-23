# Claude Opus 4.7 (with 4.6 baseline context)

> **Short name:** `claude-opus-4-7` · **Vendor:** Anthropic · **Released:** 2026 (first half) · **Effort tiers tracked:** `[max]`

## What it is

The mid-2026 Anthropic Opus generation, sitting between Opus 4.6
(the prior [Vending-Bench 2](../benchmarks/vending-bench-2.md) leader)
and Opus 4.8 (the more recent, alignment-tuned variant that regressed
on the same benchmark). Opus 4.7 is now the **outright Vending-Bench 2
leader** at $10,936.76 — the first model to clear $10k on the eval —
which is why the wiki treats it as the reference model for the
long-horizon agentic coherence axis. The leaf keeps Opus 4.6 in close
context because there is no separate 4.6 leaf and 4.6 remains the rank-3
anchor against which both the 4.7 gain and the 4.8 regression are read.

## Scores on tracked benchmarks

| Benchmark | Score | Effort tier | Filed | Source |
|-----------|-------|-------------|-------|--------|
| [Vending-Bench 2](../benchmarks/vending-bench-2.md) | **$10,936.76** (rank 1, 5-run avg) | not disclosed | 2026-06 | [Andon Labs](https://andonlabs.com/evals/vending-bench-2) (accessed 2026-06-23) |
| [DeepSWE](../benchmarks/deepswe.md) | 54% ±5% | `[max]` | 2026-05 | [deepswe.net](https://deepswe.net/) |
| [FrontierMath Tier 4 (v2)](../benchmarks/frontiermath.md) | not on top-5 (Opus **4.8** sits 5th at 56.1% ±7.8) | — | 2026-06 | [LM Council mirror](https://lmcouncil.ai/benchmarks) |
| [SWE-PRBench](../benchmarks/swe-prbench.md) | not in paper baseline | — | — | — |

Opus 4.7 also leads the multi-agent *Vending-Bench Arena* variant
ahead of GPT-5.5 and Mythos 5 ([VentureBeat coverage,
2026-06](https://venturebeat.com/technology/surprise-upset-gpt-5-5-beats-claude-fable-5-on-brutal-new-agents-last-exam-benchmark)),
consistent with its rank-1 standing on the single-agent benchmark.

## Where this model sits on the axes

- **Long-horizon agentic coherence:** **The leader.** Opus 4.7's
  $10,936.76 five-run average is the Vending-Bench 2 high-water mark,
  ~$2,600 clear of the rank-2 entry ([GLM-5.2](glm-5-2.md) at
  $8,313.78) and ~$2,900 (+36%) above its own predecessor Opus 4.6
  ($8,017.59, rank 3). Opus 4.8's documented regression on this eval
  (rank 9 at $5,787.43, `- High`) confirms Opus 4.7 — not the newer
  4.8 — as the strongest Anthropic option on this axis.
- **Frontier reasoning:** **Mid-tier among frontier models.**
  Opus 4.7 is not on the FrontierMath Tier 4 top-5; the closest
  data point is Opus 4.8 at 56.1% ±7.8, ranking fifth on that
  leaderboard. Opus 4.7's reasoning ceiling is therefore plausibly
  in the same band — clearly frontier but ~30 points below Fable
  5 on the hardest tier.

## When to pick this model

Pick Opus 4.7 for unsupervised agentic deployments: anything that
involves more than a few dozen tool calls, an extended business
process, or a multi-hour planning task where identity drift, tool
mis-use, or silent hallucinated state is the primary risk. It is the
current top-scoring model on the wiki's primary long-horizon benchmark
and the model the wiki recommends for "let the agent run overnight"
jobs.

Do not pick Opus 4.7 for hardest-reasoning ceiling work; pick
[Claude Fable 5](claude-fable-5.md) for that. The orthogonality of
the two axes is the headline finding of the
[frontier leaderboard](../frontier-leaderboard.md).

## Known caveats

- **Opus 4.8 vs Opus 4.7 trade-off is real and load-bearing.**
  Anthropic's own blog characterizes Opus 4.8 as a step forward in
  alignment but a step backward on Vending-Bench 2 / Vending-Bench
  Arena / Blueprint-Bench 2, and the board now shows it directly:
  Opus 4.8 (`- High`) sits at rank 9 versus Opus 4.7 at rank 1.
  Picking Opus 4.8 for an autonomous deployment because it is "newer"
  is a documented regression risk.
- **The DeepSWE score (54% ±5%) is *below* the Opus 4.8 score
  (58% ±5%)** on the same benchmark — i.e. on long-horizon coding
  specifically, Opus 4.8 leads, even though Opus 4.7 leads on
  long-horizon business simulation. The axis is best thought of as
  multi-dimensional within itself.
- **Score is model + scaffold.** The Vending-Bench 2 figure reflects
  Andon Labs' harness and summarization strategy as well as the model;
  it is operator-run rather than a standardized multi-vendor re-run.

## Related wiki pages

- [../frontier-leaderboard.md](../frontier-leaderboard.md)
- [../benchmarks/vending-bench-2.md](../benchmarks/vending-bench-2.md)
- [../benchmarks/deepswe.md](../benchmarks/deepswe.md)
- [../concepts/long-horizon-agentic-coherence.md](../concepts/long-horizon-agentic-coherence.md)
- [claude-opus-4-8.md](claude-opus-4-8.md) — the alignment-tuned
  sibling.
- [claude-fable-5.md](claude-fable-5.md) — the reasoning-axis
  sibling.
