# The Frontier Leaderboard — 2D Ranking

> **Filed:** 2026-06-22 · **Refresh cadence:** rolling, whenever a new benchmark score lands on any tracked source · **Axes:** [frontier reasoning](concepts/frontier-reasoning.md) (vertical), [long-horizon agentic coherence](concepts/long-horizon-agentic-coherence.md) (horizontal)

This is the single page most readers come to the wiki for. It
places every tracked frontier Large Language Model (LLM) on the
two axes the wiki defends as load-bearing — *frontier reasoning*
(intellectual ceiling on research-grade problems) and
*long-horizon agentic coherence* (the user's "long-term execution"
intuition, named more precisely).

For the longer-form story behind the two-axis structure see
[overview.md](overview.md); for the benchmark numbers that
support every placement see the
[benchmark leaves](benchmarks/benchmarks.md) and the per-model
score tables on the [model leaves](models/models.md).

## TL;DR ranking

| Axis | Rank 1 | Rank 2 | Rank 3 | Rank 4 | Rank 5 |
|------|--------|--------|--------|--------|--------|
| **Frontier reasoning** (FrontierMath Tier 4 v2 primary) | [Claude Fable 5](models/claude-fable-5.md) — 87.8% ±5.2 | [GPT-5.5 Pro](models/gpt-5-5.md) — 78.0% ±6.5 | [GPT-5.5](models/gpt-5-5.md) — 72.5% ±7.1 | [Claude Opus 4.8](models/claude-opus-4-8.md) — 56.1% ±7.8 | — |
| **Long-horizon agentic coherence** (Vending-Bench 2 primary) | [Claude Opus 4.6](models/claude-opus-4-7.md) — $8,017.59 (5-run avg) | [GLM-5.1](models/glm-5-1.md) — $5,634.41 | [Gemini 3 Pro](models/gemini-3-pro.md) — $5,478.16 | [Claude Fable 5](models/claude-fable-5.md) — ~$5,680 (single best, partial) | [Claude Opus 4.8](models/claude-opus-4-8.md) — below Opus 4.6 (vendor-acknowledged regression) |

[Claude Opus 4.7](models/claude-opus-4-7.md) is positioned by
Anthropic and by secondary coverage as the current vendor pick for
long-horizon agentic deployments, leading the Vending-Bench Arena
variant per [VentureBeat coverage](https://venturebeat.com/technology/surprise-upset-gpt-5-5-beats-claude-fable-5-on-brutal-new-agents-last-exam-benchmark);
it has no canonical Vending-Bench 2 five-run-average filing yet and
is treated here as a top-tier on the coherence axis on that basis.

## The 2D chart

Horizontal axis is **long-horizon agentic coherence** (Vending-Bench 2
$ as the primary signal; DeepSWE % and SWE-PRBench attention-curve
position as secondaries). Vertical axis is **frontier reasoning**
(FrontierMath Tier 4 v2 % as the primary signal). Models with
incomplete data on either axis are placed by their best available
proxy, with the marker shape signaling placement confidence (see
legend on the chart).

![2D capability map: every tracked frontier model placed on Vending-Bench 2 dollars (horizontal) vs FrontierMath Tier 4 v2 accuracy (vertical), colored by vendor, with the empty upper-right "frontier" quadrant shaded](assets/frontier-leaderboard.png)

> Regenerate with `python3 scripts/generate_frontier_chart.py`; the
> script is the single source of truth for the chart's placements,
> so update it whenever a score lands or moves and re-run before
> committing.

Placement coordinates that underlie the chart, expanded:

- **Fable 5** at (x ≈ $5,680, y = 87.8). x is a single-best
  Vending-Bench rollout ([agentpedia mirror](https://agentpedia.codes/blog/claude-fable-5-benchmark-prompting-guide)),
  *not* a 5-run average — treat as approximate. y is direct from
  FrontierMath Tier 4 v2 with ±5.2.
- **GPT-5.5 Pro** at (x ≈ $6,000 proxy, y = 78.0 ±6.5). x is not
  directly scored on Vending-Bench 2; placed via DeepSWE rank-1
  (70% ±4% at 47k median tokens / 20 min wall-clock).
- **GPT-5.5** at (x ≈ $6,000 proxy, y = 72.5 ±7.1). Same x-proxy
  as Pro because the DeepSWE leaderboard does not split Pro / base.
- **Opus 4.8** at (x ≈ $5,787, y = 56.1 ±7.8). x is the
  vendor-reported best Vending-Bench rollout; documented Anthropic-
  side regression vs Opus 4.6 means this is *below* the 4.6 anchor.
- **Opus 4.7** at (x ≈ $7,500 inferred, y ≈ 52 inferred). No
  canonical 5-run-average filing; placement is bracketed between
  Opus 4.6 (current leader) and Opus 4.8 (regression) per
  Anthropic + Vending-Bench Arena coverage.
- **Opus 4.6** at (x = $8,017.59, y = ceiling). Public-leaderboard
  leader on Vending-Bench 2 (5-run avg); not in FrontierMath Tier 4
  top-5, so y is plotted as a conservative ceiling marker (down-
  arrow caret).
- **GLM-5.1** at (x = $5,634.41, y = ceiling). Strongest open-
  weights long-horizon model; not in FM top-5.
- **Gemini 3 Pro** at (x = $5,478.16, y = ceiling). Not in FM top-5.

## Reading the chart

Three things the chart shows that an aggregate-score leaderboard
hides:

1. **The two axes are independent.** The reasoning leader
   ([Fable 5](models/claude-fable-5.md)) is *not* the long-horizon
   coherence leader (Opus 4.6 / 4.7). The long-horizon coherence
   leader is *not* the reasoning leader. This independence is the
   reason the wiki has two axes.
2. **Same-vendor models can disagree across axes.**
   [Opus 4.8](models/claude-opus-4-8.md) is a mid-frontier
   reasoner (rank 5 on Tier 4) and a documented *regression* on
   the long-horizon coherence axis vs its predecessor Opus 4.6.
   Picking the newer model because it is newer is a known way to
   regress on the coherence axis. This is the cleanest example of
   the wiki's thesis.
3. **The "smart and competent" upper-right quadrant is empty.**
   No single tracked model leads both axes. [GPT-5.5
   Pro](models/gpt-5-5.md) is the closest — top-2 reasoning, top-1
   coding-coherence — but it is not the Vending-Bench 2 leader.
   This is what "frontier" actually looks like in 2026-06:
   tradeoffs, not a single winner.

## Recommendations by job shape

- **Unsupervised long-running agent (e.g. business simulation,
  multi-hour autonomous loop):** pick
  [Claude Opus 4.7](models/claude-opus-4-7.md). Public-leaderboard
  baseline is Opus 4.6 at $8,017.59; vendor + secondary coverage
  point to Opus 4.7 as the current strongest variant.
  [GLM-5.1](models/glm-5-1.md) is the open-weights fallback.
- **Long-horizon coding (multi-file changes, 20+ minutes of
  agentic activity):** pick [GPT-5.5](models/gpt-5-5.md). DeepSWE
  rank-1 at 70% ±4%, with the best efficiency profile of any
  top-5 entry. [Claude Opus 4.8](models/claude-opus-4-8.md) at
  58% ±5% is the Claude-line alternative.
- **Hardest reasoning ceiling (research-grade math, novel proof
  outlines):** pick [Claude Fable 5](models/claude-fable-5.md).
  87.8% ±5.2 on FrontierMath Tier 4 v2, ~10 points clear of any
  other base model. [GPT-5.5 Pro](models/gpt-5-5.md) is the
  alternative for breadth across Tiers 1–3 (87.7% there).
- **Code review (long-context attention):** the published
  paper-baseline winner is Claude Haiku 4.5, but no frontier-tier
  model has filed on the v0.4.1 paper baseline yet — see
  [SWE-PRBench](benchmarks/swe-prbench.md) for the open question.

## Caveats applying to the whole chart

- Every Vending-Bench 2 row is **self-reported** per the operator's
  own disclosure. Cross-vendor comparisons should be read with
  that caveat.
- Every reasoning row is at **`[max]` or `[xhigh]` effort**.
  Default-effort deployment will score lower. See
  [reasoning-effort.md](concepts/reasoning-effort.md).
- Every long-horizon row scores **model + scaffold jointly**.
  See [agentic-scaffolding.md](concepts/agentic-scaffolding.md).
- Frontier models on the Anthropic side that are *newer than*
  Opus 4.6 do not yet have published 5-run-average
  Vending-Bench 2 entries. The chart's right edge reflects the
  data as published; the user's intuition that Opus 4.7 leads is
  consistent with the Vending-Bench Arena coverage but is not on
  the canonical leaderboard.

## Refresh policy

This page is regenerated whenever a new score lands on any tracked
benchmark. The schema for adding a new model is in
[../CLAUDE.md](../CLAUDE.md) under "Workflows → Ingest: adding a
new model"; the schema for adding a new benchmark is under
"Workflows → Ingest: adding a new benchmark". Each refresh should
also append a row to [log.md](log.md).

## Related wiki pages

- [overview.md](overview.md) — the longer-form story behind the
  two-axis structure and why the chart looks like it does.
- [concepts/concepts.md](concepts/concepts.md) — the two axes
  and the supporting concepts (reasoning effort, agentic
  scaffolding) that interpret the rows.
- [benchmarks/benchmarks.md](benchmarks/benchmarks.md) — the four
  benchmarks the placements draw from.
- [models/models.md](models/models.md) — one leaf per tracked
  model with full score tables and per-model caveats.
