# Models

The leaf layer for the frontier Large Language Models (LLMs) that
this wiki currently tracks. Each leaf carries the model's scores
on every tracked benchmark and a one-line summary of where it sits
on the two axes the wiki is organized around.

Six models are tracked at the time of this filing. The selection
is the set that appears on at least one of the four tracked
benchmarks' top-5 positions and that is publicly available at
inference time.

## Anthropic line

- [Claude Fable 5](claude-fable-5.md) — the wiki's
  **frontier reasoning** leader. 87.8% ±5.2 on FrontierMath Tier 4
  v2, ~10 points clear of the next base-model entry.
- [Claude Opus 4.7](claude-opus-4-7.md) — the wiki's pick for
  **long-horizon agentic coherence** and the current Vending-Bench 2
  leader at $10,936.76 (rank 1, the first model past $10k).
- [Claude Opus 4.8](claude-opus-4-8.md) — alignment-tuned
  successor; tops Anthropic's DeepSWE row at 58% ±5% but is a
  documented *regression* on Vending-Bench 2 vs Opus 4.6 / 4.7,
  landing at rank 9 ($5,787.43, `- High`). The canonical example of
  the wiki's "two axes are independent" thesis.

## OpenAI line

- [GPT-5.5](gpt-5-5.md) (with GPT-5.5 Pro variant) — DeepSWE
  rank-1 at 70% ±4%, FrontierMath Tier 4 v2 rank-2 (Pro) at 78%
  ±6.5 and rank-4 (base) at 72.5% ±7.1, FrontierMath Tiers 1–3
  rank-1 (Pro) at 87.7% ±1.9, and now Vending-Bench 2 rank-4 at
  $7,523.84. The strongest single model that is simultaneously
  top-tier on both reasoning and long-horizon coding.

## Zhipu AI (open-weights)

- [GLM-5.2](glm-5-2.md) — the wiki's open-weights pick for
  long-horizon agentic deployments. Vending-Bench 2 rank-2 at
  $8,313.78, now *above* Opus 4.6 and behind only Opus 4.7.

## Google DeepMind

- [Gemini 3 Pro](gemini-3-pro.md) — Vending-Bench 2 $5,478.16;
  was rank 3 on the 2025-12 board but newer entrants have pushed it
  below the current top ten.

## Index

| Model | Vendor | Reasoning rank | Coherence rank |
|-------|--------|----------------|----------------|
| [Claude Fable 5](claude-fable-5.md) | Anthropic | **1** (FM Tier 4 v2: 87.8%) | mid-pack (Vending-Bench 2: $5,680, rank 10, `- High`) |
| [Claude Opus 4.7](claude-opus-4-7.md) | Anthropic | mid (FM not top-5) | **1 on Vending-Bench 2** ($10,936.76) |
| [Claude Opus 4.8](claude-opus-4-8.md) | Anthropic | 5 (FM Tier 4 v2: 56.1%) | mixed — DeepSWE rank-2 (58%); Vending-Bench 2 rank 9 ($5,787, regression) |
| [GPT-5.5 / GPT-5.5 Pro](gpt-5-5.md) | OpenAI | **2 (Pro)** (FM Tier 4 v2: 78.0%) | **1 on DeepSWE** (70%); Vending-Bench 2 rank 4 ($7,524) |
| [GLM-5.2](glm-5-2.md) | Zhipu AI | not top-5 | **2 on Vending-Bench 2** ($8,313.78) |
| [Gemini 3 Pro](gemini-3-pro.md) | Google DeepMind | not top-5 | Vending-Bench 2 $5,478.16 (below current top 10) |

## Related wiki pages

- [../frontier-leaderboard.md](../frontier-leaderboard.md) — the
  2D ranking page.
- [../benchmarks/benchmarks.md](../benchmarks/benchmarks.md) — the
  four benchmarks every model is scored on.
- [../concepts/concepts.md](../concepts/concepts.md) — the two
  axes the rankings are taken along.
