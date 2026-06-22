# FrontierMath (Tiers 1–3 and Tier 4)

> **Short name:** `frontiermath` · **URL:** [epoch.ai/frontiermath](https://epoch.ai/frontiermath/tiers-1-4) · **Operator:** Epoch AI · **Latest version:** v2 released 2026-06-12

## What it measures

FrontierMath measures **frontier mathematical reasoning**: the
ceiling of a model's ability to solve original, unpublished
mathematics problems crafted and vetted by expert mathematicians.
The benchmark is the primary anchor of this wiki's
[frontier reasoning](../concepts/frontier-reasoning.md) axis.
Solving a typical problem "requires multiple hours of effort from a
researcher in the relevant branch of mathematics, and for the upper
end questions, multiple days" ([Epoch AI methodology page,
2026-06](https://epoch.ai/benchmarks/frontiermath-tier-4-v2)).

The benchmark deliberately targets capabilities that no other public
evaluation reliably probes: research-level problem framing,
multi-page proof structure, recognition of which area of mathematics
applies, and computational follow-through after the framing is
correct.

## Methodology

- **338 total problems** crafted by expert mathematicians and not
  published prior to the benchmark, spanning "most major branches of
  modern mathematics — from computationally intensive problems in
  number theory and real analysis to abstract questions in
  algebraic geometry and category theory" ([Epoch AI](https://epoch.ai/frontiermath/tiers-1-4)).
- **Two tiers:**
  - **Tiers 1–3 base set: 295 problems**, ranging from
    "undergraduate" through "exploratory problems suitable for an
    advanced graduate student".
  - **Tier 4 expansion set: 43 problems**, the *research-level*
    subset — the hardest set available to the public benchmark.
- **Twelve problems released publicly** (ten from Tiers 1–3, two
  from Tier 4); the remaining 326 are held out to prevent
  contamination.
- **Evaluation protocol:** the model must "submit a Python function
  `answer()` that returns the answer". Hard token limit per problem
  is 1,000,000 tokens with a forced-submission stage at 660,000
  tokens; the `answer()` function has a maximum runtime of 30
  seconds. Scoring is binary per problem: 1 for correct, 0 for
  incorrect or unsubmitted ([Tier 4 v2 methodology page](https://epoch.ai/benchmarks/frontiermath-tier-4-v2)).
- **v2 error correction.** On 2026-06-12 Epoch AI released v2, which
  "addressed errors in 42% of problems". The v2 numbers below are
  the canonical ones; v1 numbers should not be quoted alongside v2
  numbers without an explicit note.

## What makes it discriminative

FrontierMath is engineered to resist the four standard
benchmark-shortcut paths:

1. **Contamination resistance.** Problems are unpublished and held
   out; 12 sample problems are public for calibration, the other 326
   are not. Models cannot memorize their training data into a
   solution.
2. **Pattern-matching resistance.** Tier 4 problems are picked to
   require *original problem framing* — the model has to recognize
   which mathematical machinery applies, which is exactly the step
   that pattern matching against textbook problems fails on.
3. **Verification objectivity.** Answers are concrete computational
   objects (numbers, polynomials, sets) verified by running the
   model's submitted Python function. There is no LLM-as-judge in
   the loop, which removes a common source of inflated scores.
4. **Token-budget gating.** The 1,000,000-token cap per problem
   penalizes "burn tokens until you stumble on it" strategies; the
   forced 660k submission point makes silent loops cost the model a
   guaranteed zero on that problem.

This combination is why FrontierMath is currently the most credible
public separator of frontier reasoning ability: a model that scores
high cannot have done so via contamination, pattern matching, judge
sloppiness, or unlimited inference budget.

## Leaderboard

### Tier 4 (v2) — research-level subset, 43 problems

The single most discriminative public ranking on the
[frontier reasoning](../concepts/frontier-reasoning.md) axis.
Top five published as of 2026-06 ([LM Council benchmark mirror,
2026-06](https://lmcouncil.ai/benchmarks)):

| Rank | Model | Accuracy | Filed |
|------|-------|----------|-------|
| 1 | Claude Fable 5 [max] | 87.8% ±5.2 | 2026-06 |
| 2 | GPT-5.5 Pro [xhigh] | 78.0% ±6.5 | 2026-06 |
| 3 | "AI co-mathematician" (system not fully disclosed) | 75.6% ±6.7 | 2026-06 |
| 4 | GPT-5.5 [xhigh] | 72.5% ±7.1 | 2026-06 |
| 5 | Claude Opus 4.8 | 56.1% ±7.8 | 2026-06 |

Eighteen entries on the leaderboard in total; the top-five table is
the meaningful tier separator and the picture below rank 5 is a
long tail.

### Tiers 1–3 (v2) — base set, 295 problems

| Rank | Model | Accuracy | Filed |
|------|-------|----------|-------|
| 1 | GPT-5.5 Pro [xhigh] | 87.7% ±1.9 | 2026-06 |
| 2 | Claude Fable 5 [max] | 87.0% ±2.0 | 2026-06 |
| 3 | GPT-5.5 [xhigh] | 85.3% ±2.1 | 2026-06 |
| 4 | Claude Opus 4.8 | 80.0% ±2.4 | 2026-06 |
| 5 | GPT-5.4 [xhigh] | 78.6% ±2.4 | 2026-06 |

The order of the top two flips between tiers: GPT-5.5 Pro narrowly
edges out Fable 5 on the base set (1–3), while Fable 5 opens a
~10-point lead on Tier 4. This is the single most informative pair
of numbers in the wiki for diagnosing where each model's ceiling
actually sits — Fable 5 is harder to lose at the *upper* end of
mathematical difficulty, while GPT-5.5 Pro is slightly broader at
the medium-difficulty end.

## Known failure modes the benchmark exposes

- **Arithmetic and indexing errors at the end of correct framings.**
  Many model losses on Tier 4 are recorded as the model identifying
  the right approach in the chain-of-thought but producing the
  wrong final numerical answer.
- **Tool-use shortfalls.** The Python `answer()` function has 30
  seconds of execution time, so the model can do nontrivial
  computation; weak performers underuse this and try to do
  arithmetic in chain-of-thought instead.
- **Domain blind spots.** Pre-v2, several problems had errors in the
  problem statement (the 42% error rate v2 corrected). Even v2,
  problems in certain areas (algebraic geometry, category theory)
  appear to depress every model's score; the dataset is not
  uniformly hard across branches.

## Limitations and open critiques

- **Sample size.** 43 problems on Tier 4 gives ±5–8 point confidence
  intervals; ranks 2 through 4 are not cleanly separable.
- **"AI co-mathematician" opacity.** The third-ranked entry on
  Tier 4 v2 is reported as a system rather than a base model, with
  the underlying components not fully disclosed; treating it as a
  base-model comparison is inappropriate.
- **OpenAI funding disclosure.** The Epoch AI methodology page
  notes "This project is supported by OpenAI" — the operator and
  one of the leaderboard's top vendors have a financial relationship.
  No contamination evidence has surfaced, but the disclosure is
  load-bearing context.
- **Error-corrected v2 means historical claims need re-checking.**
  Any pre-2026-06-12 score is on v1 and should be flagged as such;
  the 42% v1 error rate means historical comparisons are not safe.
- **"Frontier" implies a ceiling that the benchmark itself may
  approach.** Fable 5's 87.8% on Tier 4 implies most current
  research-grade problems are now within reach for the top model —
  if true, the benchmark may saturate at the top within a generation
  or two, requiring Tier 5 or harder.

## When to cite this benchmark

Cite **FrontierMath Tier 4 (v2)** as the canonical reference for
*the upper bound of LLM reasoning ability on research-level
mathematics*; cite **Tiers 1–3 (v2)** for breadth across
undergraduate-through-graduate mathematics. The pair is the right
double-citation when arguing about a model's reasoning *ceiling*
vs its reasoning *floor*. For agentic-coherence claims, cite
[Vending-Bench 2](./vending-bench-2.md) or [DeepSWE](./deepswe.md)
instead — FrontierMath is a single-shot reasoning eval and does not
measure long-horizon planning.

## In the knowledge graph

- **Primary axis:** [frontier reasoning](../concepts/frontier-reasoning.md)
- **Related concepts:** [reasoning effort](../concepts/reasoning-effort.md)
  (every leaderboard entry is annotated by its effort tier:
  `[xhigh]`, `[max]`)
- **Models that lead here:** [Claude Fable 5](../models/claude-fable-5.md),
  [GPT-5.5](../models/gpt-5-5.md), [Claude Opus 4.8](../models/claude-opus-4-8.md)
- **See also:** [DeepSWE](./deepswe.md) (reasoning ceiling vs
  coding-execution ceiling),
  [Vending-Bench 2](./vending-bench-2.md) (reasoning vs coherence)

## Related wiki pages

- [../frontier-leaderboard.md](../frontier-leaderboard.md)
- [../concepts/frontier-reasoning.md](../concepts/frontier-reasoning.md)
