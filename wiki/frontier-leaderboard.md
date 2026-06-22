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
proxy, with the relevant caveat in the legend below.

```
Frontier reasoning (FrontierMath Tier 4 v2, %)
 ^
 |
 100 |
     |
  90 |                              [Fable 5 — 87.8]
     |
  80 |                                [GPT-5.5 Pro — 78.0]   (x via DeepSWE proxy)
     |
  70 |                                [GPT-5.5 — 72.5]       (x via DeepSWE proxy)
     |
  60 |                               [Opus 4.8 — 56.1]
  50 |                                          [Opus 4.7 ~ 50-55, inferred]
     |
  40 |                              [Opus 4.6 — public-leaderboard leader on x]
     |                              (not on FM Tier 4 top-5; y placeholder)
  30 |                              [GLM-5.1 — not on FM top-5; y placeholder]
     |                             [Gemini 3 Pro — not on FM top-5; y placeholder]
  20 |
     |
  10 |
     |
   0 +-----+--------+--------+--------+--------+--------+----->
        $0       $2k      $4k      $6k      $8k      $10k
                   Long-horizon agentic coherence
                  (Vending-Bench 2, 5-run avg final balance, $)

  Approximate x-coordinates of placed models:
    Gemini 3 Pro : $5.48k   GLM-5.1     : $5.63k   Fable 5  : ~$5.68k
    Opus 4.8     : ~$5.79k  Opus 4.7    : ~$7-8k*  Opus 4.6 : $8.02k
    GPT-5.5 (Pro): not on VB2 — plotted via DeepSWE-rank-1 proxy (~$6k bucket)

  * Opus 4.7 has no public 5-run-average filing; placement is inferred
    from vendor + Vending-Bench Arena coverage, not from a canonical
    Vending-Bench 2 row.
```

Legend / placement notes:

- **[Fable 5]** at ~(reasoning 88, coherence ~$5.7k). Reasoning
  position is from FrontierMath Tier 4 v2 87.8% (filed 2026-06).
  Coherence position is from a single-best Vending-Bench rollout
  of $5,680.26 ([agentpedia mirror](https://agentpedia.codes/blog/claude-fable-5-benchmark-prompting-guide))
  — *not* a 5-run average; treat the x-coordinate as approximate.
- **[GPT-5.5 Pro]** at ~(reasoning 78, coherence not directly
  scored on Vending-Bench 2; positioned via DeepSWE rank-1 at 70%
  ±4% with 47k median tokens / 20 min wall-clock, which is the
  best evidence available for the variant).
- **[GPT-5.5]** at ~(reasoning 72.5, coherence positioned the same
  way — DeepSWE 70% ±4%). Note: base GPT-5.5 and Pro share the
  same DeepSWE row because the DeepSWE leaderboard lists "GPT-5.5
  [xhigh]" without a Pro/base split.
- **[Opus 4.8]** at ~(reasoning 56.1, coherence $5.5–$6k —
  *regression* zone). Anthropic's own commentary documents the
  regression on Vending-Bench 2 vs Opus 4.6.
- **[Opus 4.7]** at ~(reasoning ~50-55, inferred; not on FM top-5;
  coherence top-tier — the current vendor pick). Plotted with
  explicit "inferred" marker.
- **[Opus 4.6]** at ~(reasoning <50, not on FM top-5; coherence
  $8,017.59 — public-leaderboard leader). This is the
  canonical anchor on the horizontal axis.
- **[GLM-5.1]** at ~(reasoning <40, not on FM top-5; coherence
  $5,634.41). Strongest open-weights long-horizon model.
- **[Gemini 3 Pro]** at ~(reasoning <40, not on FM top-5;
  coherence $5,478.16).

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
