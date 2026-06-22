# GLM-5.1

> **Short name:** `glm-5-1` · **Vendor:** Zhipu AI (智谱 AI) · **Released:** 2026 (first half) · **Effort tiers tracked:** not disclosed per submission

## What it is

The 2026 flagship reasoning-and-agent model from Zhipu AI's GLM
line. The wiki tracks GLM-5.1 specifically because it is the
**strongest open-weights model on the wiki's primary long-horizon
agentic coherence benchmark**, [Vending-Bench 2](../benchmarks/vending-bench-2.md),
where it sits second only to [Claude Opus 4.6](claude-opus-4-7.md)
on the public leaderboard. That makes GLM-5.1 the canonical answer
to "what is the best long-horizon agentic model available without
a closed-vendor relationship".

## Scores on tracked benchmarks

| Benchmark | Score | Effort tier | Filed | Source |
|-----------|-------|-------------|-------|--------|
| [Vending-Bench 2](../benchmarks/vending-bench-2.md) | **$5,634.41** (rank 2, 5-run avg) | not disclosed | 2026-05 | [llm-stats mirror](https://llm-stats.com/benchmarks/vending-bench-2) |
| [FrontierMath Tier 4 (v2)](../benchmarks/frontiermath.md) | not in top-5 | — | — | — |
| [DeepSWE](../benchmarks/deepswe.md) | not on the public leaderboard | — | — | — |
| [SWE-PRBench](../benchmarks/swe-prbench.md) | not in paper baseline | — | — | — |

The GitHub repository [zai-org/GLM-5](https://github.com/zai-org/GLM-5)
positions the model as "from vibe coding to agentic engineering" —
i.e. the line is explicitly tuned for long-horizon agent loops
rather than pure-reasoning benchmark optimization.

## Where this model sits on the axes

- **Long-horizon agentic coherence:** **Top-tier on the public
  leaderboard.** GLM-5.1's $5,634.41 on Vending-Bench 2 is the
  best non-Anthropic public result and edges out
  [Gemini 3 Pro](gemini-3-pro.md) at $5,478.16. The gap to Claude
  Opus 4.6 at $8,017.59 is ~$2,400 — material but the only frontier
  model that has documented a larger Vending-Bench 2 lead is the
  Anthropic line, which is closed-weights.
- **Frontier reasoning:** **Not on the top-5 public ranking.**
  GLM-5.1 has not filed a top-5 FrontierMath Tier 4 v2 score. The
  model's positioning is explicitly agent-leaning, and the wiki
  treats this as a real capability split rather than a missing
  measurement.

## When to pick this model

Pick GLM-5.1 when:

- The job is long-horizon agentic and an **open-weights model is
  required** — privacy constraints, on-premise deployment,
  fine-tuning, or vendor-independence requirements.
- The job is in the same shape as Vending-Bench 2 (multi-day /
  multi-hour autonomous business agent) but the Anthropic Opus
  line is out of reach (cost, access, or vendor policy).

Do not pick GLM-5.1 when:

- The job demands the absolute reasoning ceiling — GLM-5.1 is not
  on the top of any reasoning leaderboard.
- The job is short-horizon and quality of single-shot answers
  dominates — frontier closed-weights models are likely better at
  that operating point per dollar.

## Known caveats

- **Self-reported leaderboard entry.** The llm-stats mirror flags
  the entire Vending-Bench 2 leaderboard as "unverified
  self-reported" results; the GLM-5.1 row was submitted by Zhipu
  AI / Andon Labs and has not been independently re-run on
  standardized infrastructure.
- **Reasoning-axis absence is informative.** The wiki interprets
  GLM-5.1's absence from FrontierMath Tier 4 v2 top-5 as a real
  capability gap on the reasoning axis, not as a missing
  evaluation; the leaderboard is open to submissions and the model
  is well-resourced.
- **Pricing is materially lower** than the Anthropic Opus or
  OpenAI GPT lines ($1.40 / $4.40 input / output per million
  tokens vs $5.00 / $25.00 for Opus 4.6 per the llm-stats mirror).
  Cost-adjusted "long-horizon agentic dollars per benchmark
  dollar" is a metric the wiki does not yet track but on which
  GLM-5.1 is the standout.

## Related wiki pages

- [../frontier-leaderboard.md](../frontier-leaderboard.md)
- [../benchmarks/vending-bench-2.md](../benchmarks/vending-bench-2.md)
- [../concepts/long-horizon-agentic-coherence.md](../concepts/long-horizon-agentic-coherence.md)
- [gemini-3-pro.md](gemini-3-pro.md) — the Google sibling at
  similar Vending-Bench 2 position.
- [claude-opus-4-7.md](claude-opus-4-7.md) — the long-horizon-axis
  leader.
