# GPT-5.5 (with GPT-5.5 Pro variant)

> **Short name:** `gpt-5-5` · **Vendor:** OpenAI · **Released:** 2026 (first half) · **Effort tiers tracked:** `[xhigh]`

## What it is

OpenAI's mid-2026 frontier model. The wiki tracks two variants
under this leaf because they appear on different leaderboards:

- **GPT-5.5** — the base frontier model, used in the
  [DeepSWE](../benchmarks/deepswe.md) and
  [FrontierMath](../benchmarks/frontiermath.md) leaderboards.
- **GPT-5.5 Pro** — the higher-tier variant used specifically on
  the FrontierMath leaderboards. Distinguished by additional
  inference budget and an extended chain-of-thought scaffold.

The pair is the strongest OpenAI offering on both wiki axes as of
2026-06 and is the canonical alternative to the Anthropic Claude
line on the frontier-model market.

## Scores on tracked benchmarks

| Benchmark | Variant | Score | Effort tier | Filed | Source |
|-----------|---------|-------|-------------|-------|--------|
| [DeepSWE](../benchmarks/deepswe.md) | GPT-5.5 | **70% ±4%** (rank 1) | `[xhigh]` | 2026-05 | [deepswe.net](https://deepswe.net/) |
| [FrontierMath Tier 4 (v2)](../benchmarks/frontiermath.md) | GPT-5.5 Pro | 78.0% ±6.5 (rank 2) | `[xhigh]` | 2026-06 | [LM Council mirror](https://lmcouncil.ai/benchmarks) |
| [FrontierMath Tier 4 (v2)](../benchmarks/frontiermath.md) | GPT-5.5 | 72.5% ±7.1 (rank 4) | `[xhigh]` | 2026-06 | [LM Council mirror](https://lmcouncil.ai/benchmarks) |
| [FrontierMath Tiers 1–3 (v2)](../benchmarks/frontiermath.md) | GPT-5.5 Pro | **87.7% ±1.9** (rank 1) | `[xhigh]` | 2026-06 | [LM Council mirror](https://lmcouncil.ai/benchmarks) |
| [FrontierMath Tiers 1–3 (v2)](../benchmarks/frontiermath.md) | GPT-5.5 | 85.3% ±2.1 (rank 3) | `[xhigh]` | 2026-06 | [LM Council mirror](https://lmcouncil.ai/benchmarks) |
| [Vending-Bench 2](../benchmarks/vending-bench-2.md) | GPT-5.5 | **$7,523.84** (rank 4, 5-run avg) | not disclosed | 2026-06 | [Andon Labs](https://andonlabs.com/evals/vending-bench-2) (accessed 2026-06-23) |
| [SWE-PRBench](../benchmarks/swe-prbench.md) | — | not in paper baseline | — | — | — |

## Where this model sits on the axes

- **Frontier reasoning:** **Tier 1 (Pro variant) / tier 2 (base
  variant).** GPT-5.5 Pro tops Tiers 1–3 (87.7% ±1.9) and is second
  on Tier 4 (78.0% ±6.5). The base GPT-5.5 sits one rung lower on
  both tables. Together with [Fable 5](claude-fable-5.md), these
  are the two reasoning leaders of the 2026 frontier.
- **Long-horizon agentic coherence:** **Tier 1 on coding, tier 2
  on business sim.** GPT-5.5 [xhigh] tops the
  [DeepSWE](../benchmarks/deepswe.md) leaderboard at 70% ±4%, **with
  the smallest median output (47k tokens) and median wall-clock (20
  minutes)** of the top five — a meaningful efficiency lead, not
  just a raw pass-rate lead. On the broader Vending-Bench 2
  business simulation it now files a direct rank-4 score of
  $7,523.84 — behind Opus 4.7, GLM-5.2, and Opus 4.6, but ahead of
  Claude Sonnet 4.6 and the rest of the board.

## When to pick this model

Pick GPT-5.5 (or Pro) when:

- The job is **long-horizon coding** under a realistic developer
  workflow — DeepSWE-shaped tasks where short briefs require
  multi-file solutions. GPT-5.5 leads here with the best
  efficiency / pass-rate ratio published.
- The job is **research-grade mathematics with breadth coverage**
  rather than absolute ceiling — GPT-5.5 Pro tops Tiers 1–3 even
  though Fable 5 leads Tier 4.

Do not pick GPT-5.5 when:

- The job is a multi-hour unsupervised business agent — Opus 4.7
  leads the Vending-Bench 2 axis ($10,936.76), with GPT-5.5 a more
  distant rank 4 ($7,523.84).
- The job specifically requires the absolute reasoning ceiling on
  the hardest mathematics problems — Fable 5 leads Tier 4 by ~10
  points.

## Known caveats

- **Pro vs base separation.** GPT-5.5 Pro is the variant that
  delivers the FrontierMath top spots; default GPT-5.5 deployment
  will not match. Pro is an inference-budget multiplier and is
  treated as a different `[xhigh]+` row on the leaderboard.
- **Funding disclosure.** Epoch AI (the FrontierMath operator)
  discloses "this project is supported by OpenAI". No contamination
  evidence has surfaced and the held-out problem design is
  contamination-resistant, but the disclosure is relevant when
  interpreting OpenAI's strong position on this benchmark.
- DeepSWE's 70% ±4% is at `[xhigh]` effort; lower-effort
  deployment will score below this.

## Related wiki pages

- [../frontier-leaderboard.md](../frontier-leaderboard.md)
- [../benchmarks/deepswe.md](../benchmarks/deepswe.md)
- [../benchmarks/frontiermath.md](../benchmarks/frontiermath.md)
- [../concepts/frontier-reasoning.md](../concepts/frontier-reasoning.md)
- [../concepts/long-horizon-agentic-coherence.md](../concepts/long-horizon-agentic-coherence.md)
- [claude-fable-5.md](claude-fable-5.md) — the reasoning-axis
  rival.
- [claude-opus-4-7.md](claude-opus-4-7.md) — the long-horizon-axis
  rival.
