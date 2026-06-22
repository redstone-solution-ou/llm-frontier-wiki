# Frontier Reasoning

The ceiling of a Large Language Model (LLM)'s ability to solve
research-grade intellectual problems — original mathematics, novel
proofs, problems whose framing the model has never seen — when
given enough inference budget to think but no opportunity to copy
a memorized answer.

## Intuition

The user's original phrasing for this axis was "intellectual
capability". That phrasing is correct but imprecise; "intelligence"
in colloquial use mixes broad-band linguistic competence (which
every frontier LLM has) with the much narrower property the wiki
actually cares about: how *deep* can the model go before it stops
producing correct work.

"Frontier reasoning" is the wiki's term for that depth. The word
*frontier* points at the operating regime: problems at the edge of
human research capability, not problems an undergraduate would
solve in a tutorial. The word *reasoning* points at the
multi-step inferential structure required: rephrasing the problem,
choosing the right machinery, executing a multi-page proof,
arriving at a verifiable concrete answer.

This axis is *orthogonal* to the
[long-horizon agentic coherence](long-horizon-agentic-coherence.md)
axis. A model that scores 88% on FrontierMath Tier 4 may still loop
inside a vending-machine simulation; a model that holds its
identity across 365 simulated days may still miss a research
mathematics problem an undergraduate would solve. The wiki's
[2D leaderboard](../frontier-leaderboard.md) defends exactly that
orthogonality.

## How it is measured

The wiki's primary signal for this axis is
[FrontierMath](../benchmarks/frontiermath.md), and specifically its
**Tier 4 (v2)** subset — 43 research-grade problems that "require
multiple hours of effort from a researcher in the relevant branch
of mathematics, and for the upper end questions, multiple days"
([Epoch AI Tier 4 v2 page](https://epoch.ai/benchmarks/frontiermath-tier-4-v2)).

Tier 4 is the right primary signal because of four design choices:

1. **Contamination resistance.** Problems are unpublished and held
   out (only 12 of 338 are public). Memorized-answer strategies
   fail.
2. **Original problem framing required.** The model must identify
   which mathematical machinery applies — exactly the step
   pattern-matching against training data cannot shortcut.
3. **Verification objectivity.** Answers are computational objects
   verified by running a model-submitted Python function. No
   LLM-as-judge in the loop; no judge-noise floor on the scores.
4. **Token-budget gating.** 1,000,000 tokens per problem with a
   forced submission at 660,000. "Burn tokens until you stumble
   on it" strategies cost a guaranteed zero on each unsolved
   problem.

The Tier 4 leaderboard is therefore as close to a clean "reasoning
ceiling" measurement as the public has. Tiers 1–3 (the 295-problem
base set) is a useful secondary signal: it has tighter confidence
intervals because of the larger sample size, but a top model now
saturates it (~87%), so it discriminates among the lower-tier
models more than among the top tier.

The wiki currently does not use coding benchmarks as primary
reasoning-axis signals — [DeepSWE](../benchmarks/deepswe.md) and
[SWE-PRBench](../benchmarks/swe-prbench.md) are both placed on the
[long-horizon agentic coherence](long-horizon-agentic-coherence.md)
axis. The argument is that coding ability is dominated by harness
quality and pattern matching against open-source code, not by the
multi-page reasoning that Tier 4 mathematics demands. This is a
deliberate axis choice and is open to revision if a coding
benchmark engineered for contamination resistance and reasoning
depth (rather than throughput) appears.

## Why it is a useful axis

Three predictions fall out of separating the reasoning-axis ranking
from the coherence-axis ranking:

1. **Hardest single-problem ceiling diverges from agentic
   suitability.** [Claude Fable 5](../models/claude-fable-5.md)
   leads FrontierMath Tier 4 at 87.8% but is not the public leader
   on Vending-Bench 2. The wiki's claim is that this is a real
   capability split, not a measurement artifact: hard mathematics
   and long-horizon agent loops require different things.
2. **Reasoning effort tier matters more on this axis than on the
   coherence axis.** The Tier 4 leaderboard explicitly annotates
   every top entry with its effort tier (`[max]`, `[xhigh]`); the
   gap between effort tiers is often larger than the gap between
   models at the same tier. See
   [reasoning-effort.md](reasoning-effort.md).
3. **The reasoning axis saturates within a generation or two.**
   Fable 5's 87.8% on Tier 4 with ±5.2% confidence implies the
   benchmark may approach saturation at the top within one model
   generation. If true, the axis will need Tier 5 or harder
   problems to remain discriminative. The
   [long-horizon agentic coherence](long-horizon-agentic-coherence.md)
   axis shows no such saturation: even the best model leaves ~7×
   the available profit on the table.

## Trade-offs and failure modes

- The axis *under-measures applied reasoning*. FrontierMath is
  pure mathematics. A model that scores high on Tier 4 is not
  necessarily strong at physics-style reasoning under partial
  observation, legal-style reasoning under contradictory precedent,
  or business-strategy reasoning under uncertainty.
- The axis is *strongly correlated with inference budget*. The
  `[max]` and `[xhigh]` annotations on the leaderboard are
  load-bearing; comparing a `[max]` Fable 5 to a `[default]`
  Opus is not a fair comparison.
- The axis can be *gamed by ensembling*. The "AI co-mathematician"
  third-place entry on Tier 4 v2 is a system, not a base model;
  including it on a model-vs-model leaderboard is misleading. The
  wiki marks it explicitly.
- Funding disclosure matters. Epoch AI's own page states "this
  project is supported by OpenAI" — no contamination evidence has
  surfaced and the held-out problem design resists obvious leakage,
  but the disclosure is load-bearing context.
- A high Tier 4 score does *not* mean the model can find or
  contribute original mathematics. It means the model can solve
  research-level problems that already have known answers. The two
  are different.

## Models that exemplify high values on this axis

- [Claude Fable 5](../models/claude-fable-5.md) — 87.8% ±5.2 on
  FrontierMath Tier 4 v2, ~10 points clear of the second-place base
  model. The current wiki pick for "raw reasoning ceiling".
- [GPT-5.5 Pro](../models/gpt-5-5.md) — 78.0% ±6.5 on Tier 4 and
  87.7% ±1.9 on Tiers 1–3; the top of the leaderboard on the base
  set, very close to Fable 5 on breadth but ~10 points behind on
  the hardest tier.
- [Claude Opus 4.8](../models/claude-opus-4-8.md) — 56.1% ±7.8 on
  Tier 4; clearly in the "frontier reasoning" tier but a generation
  behind Fable 5 on the upper end. Notable for being the
  alignment-tuned variant that regressed on
  [Vending-Bench 2](../benchmarks/vending-bench-2.md) — this is the
  cleanest demonstration that the two axes are independent.

## Open questions

- Does Tier 4 saturate this generation? Fable 5 at 87.8% implies
  yes within one to two generations; the wiki should plan for a
  Tier 5 or alternative ceiling benchmark.
- Does reasoning depth on mathematics predict reasoning depth on
  other research domains? Currently unmeasured at the public
  benchmark level.
- Are reasoning-axis gains coming from base model improvements or
  from training-time reasoning-effort scaffolds (chain-of-thought
  trace length, internal verification, self-consistency)? The
  effort-tier annotations on the leaderboard are suggestive but
  not separating.
- How does scaling continue to interact with this axis? The
  rate-of-improvement curve on Tier 4 is steep enough that the
  axis is currently capability-bound rather than evaluation-bound.

## Related wiki pages

- [long-horizon-agentic-coherence.md](long-horizon-agentic-coherence.md)
  — the orthogonal axis.
- [reasoning-effort.md](reasoning-effort.md) — effort-tier
  annotations on the leaderboards are load-bearing and discussed
  here.
- [../benchmarks/frontiermath.md](../benchmarks/frontiermath.md)
- [../frontier-leaderboard.md](../frontier-leaderboard.md)
