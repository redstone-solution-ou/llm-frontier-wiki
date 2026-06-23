# Gemini 3 Pro

> **Short name:** `gemini-3-pro` · **Vendor:** Google DeepMind · **Released:** late 2025 / early 2026 · **Effort tiers tracked:** not annotated on the tracked leaderboards

## What it is

Google DeepMind's late-2025 / early-2026 flagship frontier model.
The wiki tracks Gemini 3 Pro because it held rank 3 on the
[Vending-Bench 2](../benchmarks/vending-bench-2.md) leaderboard at the
2025-12 filing and was one of the only non-Anthropic models with a
documented five-run-average position on that benchmark. As of the
2026-06-23 refresh its $5,478.16 is unchanged but newer entrants
(Opus 4.7, GLM-5.2, GPT-5.5, Sonnet 4.6) have pushed it below the
current top ten.

## Scores on tracked benchmarks

| Benchmark | Score | Effort tier | Filed | Source |
|-----------|-------|-------------|-------|--------|
| [Vending-Bench 2](../benchmarks/vending-bench-2.md) | **$5,478.16** (was rank 3; below current top 10) | not disclosed | 2025-12 | [Andon Labs](https://andonlabs.com/evals/vending-bench-2) (accessed 2026-06-23) |
| [FrontierMath Tier 4 (v2)](../benchmarks/frontiermath.md) | not in top-5 | — | — | — |
| [DeepSWE](../benchmarks/deepswe.md) | not on the public leaderboard | — | — | — |
| [SWE-PRBench](../benchmarks/swe-prbench.md) | not in paper baseline | — | — | — |

A separate [Gemini 3.1 Pro variant has been reported at 54.2% on
SWE-Bench Pro](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained)
in independent reviews, but SWE-Bench Pro is not one of the four
benchmarks the wiki tracks; the figure is logged here only as
secondary context.

## Where this model sits on the axes

- **Long-horizon agentic coherence:** **Competitive but no longer
  top-tier.** Gemini 3 Pro's $5,478.16 on Vending-Bench 2 was a top-3
  placement in late 2025, but the 2026-06 board has it below the top
  ten — well behind the open-weights leader [GLM-5.2](glm-5-2.md)
  ($8,313.78) and ~$5,500 below the leader Opus 4.7 ($10,936.76). The
  Google line therefore sits in the "competitive but trailing the
  current frontier" band on this axis.
- **Frontier reasoning:** **Not in the top-5 public ranking** on
  FrontierMath Tier 4 v2. The model's most relevant reasoning
  comparisons live on benchmarks the wiki does not yet track
  (Gemini's own AI Olympiad-style evals); the absence from Tier 4
  top-5 is interpreted as a real reasoning-ceiling gap rather
  than a missing evaluation.

## When to pick this model

Pick Gemini 3 Pro when:

- The job is long-horizon agentic and the deployment is already
  inside Google Cloud / Vertex / Gemini infrastructure — pricing
  and tooling integration are weight-bearing in real deployment
  decisions even when raw benchmark numbers favor a competitor.
- Multimodal long-horizon work (vision + agentic) is part of the
  job — Gemini's multimodal coverage is the strongest of the
  tracked models, even though the wiki does not measure that
  axis directly.

Do not pick Gemini 3 Pro when:

- The job demands the absolute long-horizon agentic ceiling —
  Opus 4.7 leads the Vending-Bench 2 axis, with GLM-5.2 the
  open-weights alternative, both well above Gemini 3 Pro.
- The job demands the absolute reasoning ceiling — Fable 5 leads
  the FrontierMath axis and Gemini is not on the top-5 board.

## Known caveats

- **Score is from 2025-12.** The Vending-Bench 2 row predates the
  current board; the figure has not moved but the field has, so the
  rank is stale even though the dollar value is not.
- **Operator-run.** Same caveat as every Vending-Bench 2 row — run
  and reported by Andon Labs on its own harness.
- **No FrontierMath top-5 placement.** A model that does not file
  a competitive number on the wiki's primary reasoning benchmark
  cannot be ranked on that axis except by inference; the wiki
  marks Gemini 3 Pro as a long-horizon-only entry until a
  reasoning-axis score lands.

## Related wiki pages

- [../frontier-leaderboard.md](../frontier-leaderboard.md)
- [../benchmarks/vending-bench-2.md](../benchmarks/vending-bench-2.md)
- [../concepts/long-horizon-agentic-coherence.md](../concepts/long-horizon-agentic-coherence.md)
- [glm-5-2.md](glm-5-2.md) — the open-weights sibling, now well
  above Gemini 3 Pro on this benchmark.
