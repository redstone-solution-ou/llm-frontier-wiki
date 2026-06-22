# Claude Opus 4.7 (with 4.6 baseline context)

> **Short name:** `claude-opus-4-7` · **Vendor:** Anthropic · **Released:** 2026 (first half) · **Effort tiers tracked:** `[max]`

## What it is

The mid-2026 Anthropic Opus generation, sitting between Opus 4.6
(the current public-leaderboard leader on
[Vending-Bench 2](../benchmarks/vending-bench-2.md)) and Opus 4.8
(the more recent, alignment-tuned variant that regressed on the
same benchmark). The wiki keeps the Opus 4.7 leaf in close contact
with Opus 4.6 because much of the public benchmark data on Opus 4.7
is reported only relative to its neighbors, and because the user
identifies Opus 4.7 as the current vendor pick for
long-horizon agentic deployments.

## Scores on tracked benchmarks

| Benchmark | Score | Effort tier | Filed | Source |
|-----------|-------|-------------|-------|--------|
| [Vending-Bench 2](../benchmarks/vending-bench-2.md) | not on public leaderboard; Opus **4.6** baseline is **$8,017.59** (5-run avg, leaderboard leader) | not disclosed | 2026-02 | [llm-stats mirror](https://llm-stats.com/benchmarks/vending-bench-2) |
| [DeepSWE](../benchmarks/deepswe.md) | 54% ±5% | `[max]` | 2026-05 | [deepswe.net](https://deepswe.net/) |
| [FrontierMath Tier 4 (v2)](../benchmarks/frontiermath.md) | not on top-5 (Opus **4.8** sits 5th at 56.1% ±7.8) | — | 2026-06 | [LM Council mirror](https://lmcouncil.ai/benchmarks) |
| [SWE-PRBench](../benchmarks/swe-prbench.md) | not in paper baseline | — | — | — |

Vendor-side reporting puts Opus 4.7 ahead of GPT-5.5 and Mythos 5
on the *Vending-Bench Arena* variant ([VentureBeat coverage,
2026-06](https://venturebeat.com/technology/surprise-upset-gpt-5-5-beats-claude-fable-5-on-brutal-new-agents-last-exam-benchmark));
this is partial side-channel data, not the canonical Vending-Bench 2
five-run average.

## Where this model sits on the axes

- **Long-horizon agentic coherence:** **Top tier**, possibly the
  vendor-side leader as of 2026-06. Opus 4.6's $8,017.59
  five-run average is the public-leaderboard high-water mark by a
  ~$2,400 gap over the next entry (GLM-5.1 at $5,634.41); Opus 4.7
  is positioned by Anthropic and by secondary coverage as the
  current vendor pick for autonomous agent deployments, and Opus
  4.8's documented regression on Vending-Bench 2 ([Andon Labs blog](https://andonlabs.com/blog/opus-4-8-vending-bench))
  implicitly leaves Opus 4.7 as the strongest current Anthropic
  option on this axis.
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
mis-use, or silent hallucinated state is the primary risk. This is
the model the wiki currently recommends for "let the agent run
overnight" jobs.

Do not pick Opus 4.7 for hardest-reasoning ceiling work; pick
[Claude Fable 5](claude-fable-5.md) for that. The orthogonality of
the two axes is the headline finding of the
[frontier leaderboard](../frontier-leaderboard.md).

## Known caveats

- **Public-leaderboard absence is itself information.** Opus 4.7
  does not yet have a published Vending-Bench 2 five-run-average
  figure; the wiki's placement is based on secondary coverage and
  on the documented Opus 4.6 baseline + Opus 4.8 regression. A
  canonical filing could move the position.
- **Opus 4.8 vs Opus 4.7 trade-off is real and load-bearing.**
  Anthropic's own blog characterizes Opus 4.8 as a step forward in
  alignment but a step backward on Vending-Bench 2 / Vending-Bench
  Arena / Blueprint-Bench 2. Picking Opus 4.8 for an autonomous
  deployment because it is "newer" is a known regression risk.
- The DeepSWE score (54% ±5%) is *below* the Opus 4.8 score
  (58% ±5%) on the same benchmark — i.e. on long-horizon coding
  specifically, Opus 4.8 leads, even though Opus 4.6 / 4.7 lead on
  long-horizon business simulation. The axis is best thought of as
  multi-dimensional within itself.

## Related wiki pages

- [../frontier-leaderboard.md](../frontier-leaderboard.md)
- [../benchmarks/vending-bench-2.md](../benchmarks/vending-bench-2.md)
- [../benchmarks/deepswe.md](../benchmarks/deepswe.md)
- [../concepts/long-horizon-agentic-coherence.md](../concepts/long-horizon-agentic-coherence.md)
- [claude-opus-4-8.md](claude-opus-4-8.md) — the alignment-tuned
  sibling.
- [claude-fable-5.md](claude-fable-5.md) — the reasoning-axis
  sibling.
