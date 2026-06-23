# The LLM Frontier — Two Axes

This wiki is built around a single claim: the practical question
"which frontier Large Language Model (LLM) should I pick for this
job?" is best answered on **two axes**, not on a single aggregate
score. The two axes are:

1. **[Frontier reasoning](concepts/frontier-reasoning.md)** — the
   model's ceiling on research-grade intellectual problems when
   given enough inference budget to think but no memorized-answer
   shortcut. Primary benchmark:
   [FrontierMath](benchmarks/frontiermath.md) Tier 4 (v2), 43
   unpublished research-mathematics problems with hard token
   budgets and Python-`answer()` verification.
2. **[Long-horizon agentic coherence](concepts/long-horizon-agentic-coherence.md)** —
   the model's ability to hold identity, tool use, and decision-
   making together across thousands of agentic steps without
   drifting, looping, or hallucinating prior context. Primary
   benchmark: [Vending-Bench 2](benchmarks/vending-bench-2.md),
   a year-long vending-machine business simulation with 3,000–6,000
   tool messages and 60–100M tokens per rollout.

The hypothesis the wiki defends is that these two axes are
**orthogonal**: a model can lead one and lag the other. The
evidence for that claim is laid out in the
[frontier leaderboard](frontier-leaderboard.md); the short version
is that the FrontierMath Tier 4 v2 leader ([Claude Fable
5](models/claude-fable-5.md), 87.8% ±5.2) is *not* the
Vending-Bench 2 leader ([Claude Opus 4.7](models/claude-opus-4-7.md),
$10,936.76 five-run average), and the Vending-Bench 2 leader is
*not* on the FrontierMath Tier 4 v2 top-5 at all.

The rest of this page walks through that thesis end to end. The
wiki is organized to support it: a small set of
[concepts](concepts/concepts.md) defines the axes and the
supporting ideas, four
[benchmark leaves](benchmarks/benchmarks.md) record the methodology
and leaderboard for each tracked benchmark, and one
[model leaf](models/models.md) per tracked frontier model carries
the score table and the axis-position summary. You can read this
page top to bottom without following any link and come away with
the shape of the field; clicking a link takes you to a denser
treatment of the same idea, and clicking a benchmark takes you to
the underlying methodology.

## Why one axis is not enough

Most public LLM leaderboards rank models on a single aggregate
score — an average over a basket of evals. This approach has two
defects the wiki tries to repair:

1. **It mixes capabilities the user does not want mixed.** A
   model that scores 88% on hard mathematics and 50% on
   long-horizon agent tasks has a different deployment fit than
   a model that scores 60% on both. The aggregate can be the same
   while the picks differ. The two-axis structure makes the
   relevant difference visible.
2. **It hides regressions.** Anthropic's own commentary on
   [Claude Opus 4.8](models/claude-opus-4-8.md) acknowledges
   "better alignment, worse performance" on
   [Vending-Bench 2](benchmarks/vending-bench-2.md) vs Opus 4.6
   ([Andon Labs blog](https://andonlabs.com/blog/opus-4-8-vending-bench)).
   On any aggregate score the regression is buried in a "newer
   model, similar overall number". On the long-horizon coherence
   axis it is a documented step backward.

The wiki argues that the two axes capture the two failure modes
that *actually matter* for frontier-model selection:
"the model is not smart enough for this problem" (reasoning axis)
and "the model is smart enough but cannot hold itself together
for this long" (coherence axis). One model can be the right
answer for the first, a different model the right answer for the
second.

## The reasoning axis — what FrontierMath measures

[FrontierMath](benchmarks/frontiermath.md) is, as of 2026-06, the
single most credible public probe of LLM reasoning ceiling. The
Epoch AI methodology page describes its 338 problems as crafted
and vetted by expert mathematicians, with "multiple hours" of
researcher effort required for typical problems and "multiple
days" for the upper-end ones. The benchmark resists the standard
shortcut paths to high scores: 326 of 338 problems are held out,
the answers are concrete computational objects verified by a
Python function (no LLM-as-judge in the loop), and a hard
1,000,000-token budget per problem penalizes "burn tokens until
you stumble on it" strategies.

Tier 4 (43 problems) is the research-grade subset; the v2 release
(2026-06-12) corrected 42% of v1 problems and is now the canonical
version. The top of the Tier 4 v2 leaderboard ([LM Council
mirror](https://lmcouncil.ai/benchmarks)) is:

| Rank | Model | Score |
|------|-------|-------|
| 1 | [Claude Fable 5 `[max]`](models/claude-fable-5.md) | 87.8% ±5.2 |
| 2 | [GPT-5.5 Pro `[xhigh]`](models/gpt-5-5.md) | 78.0% ±6.5 |
| 3 | "AI co-mathematician" (system, not base model) | 75.6% ±6.7 |
| 4 | [GPT-5.5 `[xhigh]`](models/gpt-5-5.md) | 72.5% ±7.1 |
| 5 | [Claude Opus 4.8](models/claude-opus-4-8.md) | 56.1% ±7.8 |

Fable 5's ~10-point lead over the second-place base model on the
hardest tier is the single sharpest reasoning-ceiling signal the
public has. On the easier Tiers 1–3 (295 problems) the order
flips — GPT-5.5 Pro tops the base set at 87.7% ±1.9 with Fable 5
second at 87.0% ±2.0 — which is informative: GPT-5.5 Pro is the
broader reasoner, Fable 5 the deeper one.

## The coherence axis — what Vending-Bench 2 measures

[Vending-Bench 2](benchmarks/vending-bench-2.md) is a year-long
simulated vending-machine business. The model gets $500 of
starting capital, pays $2 per simulated day in location fees,
purchases inventory from simulated suppliers (some of which
negotiate adversarially), sets prices, manages cash flow, and
responds to customer complaints. The only metric is the final
bank balance, averaged across 5 runs per model. A single run is
3,000–6,000 messages and 60–100M tokens — exceeding every frontier
model's working context window by 1–2 orders of magnitude, which
forces the harness to compress and summarize. The benchmark
therefore measures what happens to a model under sustained
operational pressure: identity drift, loops, hallucinated supplier
emails, payments made twice, over-trust of adversarial
counterparties.

The official leaderboard ([Andon Labs, accessed 2026-06-23](https://andonlabs.com/evals/vending-bench-2)), top of 49 listed models, is:

| Rank | Model | Final balance |
|------|-------|---------------|
| 1 | [Claude Opus 4.7](models/claude-opus-4-7.md) | $10,936.76 |
| 2 | [GLM-5.2 (Zhipu AI)](models/glm-5-2.md) | $8,313.78 |
| 3 | [Claude Opus 4.6](models/claude-opus-4-7.md) | $8,017.59 |
| 4 | [GPT-5.5](models/gpt-5-5.md) | $7,523.84 |
| 5 | Claude Sonnet 4.6 | $7,204.14 |

Opus 4.7's ~$2,600 lead over rank-2 GLM-5.2 — and its ~$2,900
(+36%) jump over its own predecessor Opus 4.6 — is the single
sharpest coherence signal the public has. Two things to note: (a)
Opus 4.8 (`- High`) lands at rank 9 ($5,787.43), *below* both Opus
4.6 and 4.7, matching Anthropic's own framing of 4.8 as a
*regression* on this benchmark, and (b) the leaderboard is
operator-run by Andon Labs on its own harness.

The wiki's pick for unsupervised agentic deployments is
[Claude Opus 4.7](models/claude-opus-4-7.md), the current
Vending-Bench 2 leader and also the top model on the multi-agent
*Vending-Bench Arena* variant. For an open-weights alternative
the wiki picks [GLM-5.2](models/glm-5-2.md), now rank 2 and above
Opus 4.6.

## Why the wiki adds DeepSWE and SWE-PRBench

A single benchmark per axis is the minimum for a 2D claim, not the
ideal. Two extra benchmarks triangulate the coherence axis:

- [DeepSWE](benchmarks/deepswe.md) — 113 original Software
  Engineering tasks, short prompts and multi-file long solutions,
  behavioral verifiers. Probes the **long-horizon coding**
  facet of coherence. [GPT-5.5 `[xhigh]`](models/gpt-5-5.md) leads
  at 70% ±4% with the best efficiency profile of any top-5
  entry; [Claude Opus 4.8](models/claude-opus-4-8.md) at 58% ±5%
  is the Claude-line alternative.
- [SWE-PRBench](benchmarks/swe-prbench.md) — 350 pull-request
  reviews across three context configurations. Probes the
  **attention-allocation** facet: every model degrades
  monotonically as the harness expands the context from a bare
  diff to the full repository. The benchmark's leaderboard is on
  older models (Haiku 4.5 leads at 0.153 weighted score) but its
  headline finding — that long-context windows are not
  long-context attention — is the cleanest available argument
  against treating nominal context window as a deployment
  parameter.

Together with Vending-Bench 2, these three benchmarks give the
coherence axis three facets: business-simulation coherence
(Vending-Bench 2), coding coherence (DeepSWE), and attention-
allocation coherence (SWE-PRBench). The 2D leaderboard collapses
these into one axis position; the leaf for each benchmark exposes
the underlying detail.

## What does *not* fit on the two axes

Several capabilities the wiki deliberately does *not* yet track:

- **Multimodal capability.** Frontier vision / audio / video
  capabilities are real and benchmarked separately; the wiki's
  axes are language + agent.
- **Latency / cost.** Effort tiers (`[max]`, `[xhigh]`) affect
  both, but the wiki does not currently rank models on dollars
  per benchmark dollar. See
  [reasoning-effort.md](concepts/reasoning-effort.md).
- **Alignment, safety, refusal calibration.** The Opus 4.8
  regression is what surfaced this — alignment is partly
  *measured by* the long-horizon coherence axis (refusal-rate
  changes show up as Vending-Bench 2 dollars left on the table)
  but the wiki does not yet have a dedicated alignment axis.
- **Multi-turn dialog quality.** The model's pleasantness or
  conversational fit on a 5-turn chat is not what the wiki
  measures.

These omissions are deliberate. Adding a third axis without a
third benchmark genuinely independent from the existing two would
add a column to the leaderboard without adding resolution; the
wiki's bet is that the two axes already named cover the most
load-bearing variation in frontier-model selection.

## Where to go next

If you came for the ranking, read
[frontier-leaderboard.md](frontier-leaderboard.md). That is the
single page the wiki is built around.

If you came for the methodology behind the ranking, read the
[benchmarks](benchmarks/benchmarks.md) hub and then the leaves of
the four tracked benchmarks.

If you came to understand the structure of the wiki and the
arguments behind the two axes, you are reading it.

If you came for a per-model summary with full score tables, read
the [models](models/models.md) hub and the individual model
leaves.

## Knowledge-graph sketch

```
llm-frontier-wiki
|
+-- concepts/
|   +-- frontier-reasoning              (axis 1)
|   +-- long-horizon-agentic-coherence  (axis 2)
|   +-- reasoning-effort                (supporting; every leaderboard row carries it)
|   +-- agentic-scaffolding             (supporting; harness vs model contribution)
|
+-- benchmarks/
|   +-- frontiermath                    (primary signal for axis 1)
|   +-- vending-bench-2                 (primary signal for axis 2)
|   +-- deepswe                         (axis 2, coding facet)
|   +-- swe-prbench                     (axis 2, attention-allocation facet)
|
+-- models/
|   +-- claude-fable-5                  (axis 1 leader)
|   +-- claude-opus-4-7                 (axis 2 leader; Vending-Bench 2 rank 1)
|   +-- claude-opus-4-8                 (axis 1 mid-tier; axis 2 regression vs predecessor)
|   +-- gpt-5-5                         (top-tier both axes; closest to upper-right quadrant)
|   +-- glm-5-2                         (axis 2 open-weights pick; rank 2)
|   +-- gemini-3-pro                    (axis 2; 2025-12 score, now below top 10)
|
+-- frontier-leaderboard.md             (the 2D chart and ranking)
```

## Related wiki pages

- [frontier-leaderboard.md](frontier-leaderboard.md) — the 2D
  ranking page.
- [concepts/concepts.md](concepts/concepts.md) — the two axes.
- [benchmarks/benchmarks.md](benchmarks/benchmarks.md) — the four
  benchmarks.
- [models/models.md](models/models.md) — the six tracked models.
- [index.md](index.md) — flat catalogue, first stop for a known
  topic.
- [log.md](log.md) — chronological record of ingests and
  rewrites.
