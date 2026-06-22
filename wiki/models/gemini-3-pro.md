# Gemini 3 Pro

> **Short name:** `gemini-3-pro` · **Vendor:** Google DeepMind · **Released:** late 2025 / early 2026 · **Effort tiers tracked:** not annotated on the tracked leaderboards

## What it is

Google DeepMind's late-2025 / early-2026 flagship frontier model.
The wiki tracks Gemini 3 Pro because it holds rank 3 on the public
[Vending-Bench 2](../benchmarks/vending-bench-2.md) leaderboard
and is one of the only non-Anthropic models with a documented
five-run-average position on that benchmark. The wiki does not
track Gemini 3 Flash separately because its position is on the
same leaderboard at rank 4 and the qualitative wiki claim is
about Pro.

## Scores on tracked benchmarks

| Benchmark | Score | Effort tier | Filed | Source |
|-----------|-------|-------------|-------|--------|
| [Vending-Bench 2](../benchmarks/vending-bench-2.md) | **$5,478.16** (rank 3, 5-run avg) | not disclosed | 2025-12 | [llm-stats mirror](https://llm-stats.com/benchmarks/vending-bench-2) |
| [FrontierMath Tier 4 (v2)](../benchmarks/frontiermath.md) | not in top-5 | — | — | — |
| [DeepSWE](../benchmarks/deepswe.md) | not on the public leaderboard | — | — | — |
| [SWE-PRBench](../benchmarks/swe-prbench.md) | not in paper baseline | — | — | — |

A separate [Gemini 3.1 Pro variant has been reported at 54.2% on
SWE-Bench Pro](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained)
in independent reviews, but SWE-Bench Pro is not one of the four
benchmarks the wiki tracks; the figure is logged here only as
secondary context.

## Where this model sits on the axes

- **Long-horizon agentic coherence:** **Top-3 public placement.**
  Gemini 3 Pro's $5,478.16 on Vending-Bench 2 sits in a narrow
  band with GLM-5.1 ($5,634.41) and ~$2,500 below Opus 4.6's
  leaderboard lead. The Google line therefore sits in the
  "competitive but not leading" band on this axis.
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
  Opus 4.6 / 4.7 lead the Vending-Bench 2 axis.
- The job demands the absolute reasoning ceiling — Fable 5 leads
  the FrontierMath axis and Gemini is not on the top-5 board.

## Known caveats

- **Filed 2025-12.** The public Vending-Bench 2 row is from late
  2025; newer Gemini generations (3.1, Flash variants) have
  partial coverage elsewhere but not on the canonical
  leaderboards the wiki tracks.
- **Self-reported.** Same caveat as every Vending-Bench 2 row.
- **No FrontierMath top-5 placement.** A model that does not file
  a competitive number on the wiki's primary reasoning benchmark
  cannot be ranked on that axis except by inference; the wiki
  marks Gemini 3 Pro as a long-horizon-only entry until a
  reasoning-axis score lands.

## Related wiki pages

- [../frontier-leaderboard.md](../frontier-leaderboard.md)
- [../benchmarks/vending-bench-2.md](../benchmarks/vending-bench-2.md)
- [../concepts/long-horizon-agentic-coherence.md](../concepts/long-horizon-agentic-coherence.md)
- [glm-5-1.md](glm-5-1.md) — the open-weights sibling at similar
  Vending-Bench 2 position.
