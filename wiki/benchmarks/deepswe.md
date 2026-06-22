# DeepSWE

> **Short name:** `deepswe` · **URL:** [deepswe.net](https://deepswe.net/) · **Operator:** DeepSWE benchmark team · **Latest leaderboard refresh:** 2026-05-30

## What it measures

DeepSWE measures **long-horizon software engineering** in the
realistic-developer-workflow regime: a model receives a compact natural
language brief (median prompt length 2,158 characters) and is expected
to produce a substantial multi-file change (median reference solution
**668 lines of code touching 7 files**) that passes behavioral
verifiers without breaking unrelated functionality. The benchmark sits
primarily on the
[long-horizon agentic coherence](../concepts/long-horizon-agentic-coherence.md)
axis — every task forces the model to do repository exploration,
multi-file edits, and regression checks across several minutes to
tens of minutes of agentic activity. Reasoning ceiling matters, but
holding it together across a long agentic trajectory matters more.

## Methodology

- **113 original tasks** written from scratch (not adapted from
  existing GitHub commits or pull requests), reducing the
  gold-commit-leakage risk that affects SWE-Bench-style benchmarks
  where models can recover known fixes from git history.
- **91 active open-source repositories** as the underlying corpus.
- **Five languages**: TypeScript, Go, Python, JavaScript, Rust —
  multi-language coverage is deliberate; many coding benchmarks
  measure Python proficiency only.
- **Behavioral verifiers, not unit-test-of-implementation.** Tasks
  are graded by whether the resulting code exhibits the requested
  behavior, allowing multiple valid implementations to pass; this
  reduces the rate of false negatives on tasks where the model's
  solution is correct but stylistically different from the
  reference.
- **Task domains:** runtime behavior (shutdown handling, async
  lifecycles, regression testing), data structures (sorting,
  pagination, maps, conflict detection), and developer tooling
  (Command-Line Interface (CLI) parsing, linting, caching, report
  generation).

All numbers above are from the
[DeepSWE benchmark page (deepswe.net, accessed 2026-06-22)](https://deepswe.net/).

## What makes it discriminative

DeepSWE deliberately engineers **short prompts with long implementations**
to defeat pattern-matching: the prompt does not enumerate the
sub-steps, so the model must plan multi-step without detailed
instructions. This is the property that separates strong long-horizon
coders from models that excel only when the task is already
decomposed. Comparison numbers from the DeepSWE page note that
SWE-Bench Pro tasks average 4,614-character prompts — more than twice
DeepSWE's 2,158 — and DeepSWE explicitly positions itself as a purer
test of "model plans multi-step in unfamiliar code" rather than "model
follows a specified plan".

The behavioral-verifier choice is also discriminative: SWE-Bench-style
strict-test-match scoring under-rewards correct alternative
implementations and over-rewards solutions that pattern-match the
exact reference variable names. DeepSWE's verifier explicitly looks
for the *requested behavior*, not the reference *code*, which the
benchmark page argues is the right discriminator for long-horizon
engineering ability.

## Leaderboard

Published leaderboard, last refreshed 2026-05-30
([deepswe.net](https://deepswe.net/)):

| Rank | Model | Score | Filed | Median output tokens | Median wall-clock |
|------|-------|-------|-------|----------------------|-------------------|
| 1 | GPT-5.5 [xhigh] | 70% ±4% | 2026-05 | 47k | 20 min |
| 2 | Claude Opus 4.8 [max] | 58% ±5% | 2026-05 | not disclosed | not disclosed |
| 3 | GPT-5.4 [xhigh] | 56% ±5% | 2026-05 | not disclosed | not disclosed |
| 4 | Claude Opus 4.7 [max] | 54% ±5% | 2026-05 | not disclosed | not disclosed |
| 5 | Claude Sonnet 4.6 [high] | 32% ±4% | 2026-05 | not disclosed | not disclosed |

GPT-5.5's pass rate is notable not just for being the highest but for
being achieved with a relatively modest 47k median output tokens and
20-minute median wall-clock — the DeepSWE page argues this rules out
"brute-force the search by emitting more tokens" as the explanation
for the top score.

## Known failure modes the benchmark exposes

- **Multi-file edit consistency.** A model that changes a function
  signature in one file but forgets to update the three call sites in
  other files fails the regression check. This is the single most
  common DeepSWE failure mode and is invisible to function-level
  benchmarks.
- **Premature termination.** Models that "decide they're done" partway
  through a multi-step task without running the verification step
  score zero even when the partial work is correct.
- **Stale-context bugs.** As a session extends, models begin reasoning
  off summaries of the codebase rather than the codebase itself,
  introducing changes that contradict files they no longer remember
  reading.
- **Brittle behavior on Rust / Go.** Score variance is higher on the
  static-typed-and-compiled languages; pattern matching from training
  data is less reliable when the type checker rejects an "almost
  right" solution.

## Limitations and open critiques

- **No standardized scaffold across vendors.** The leaderboard lists
  each model under a specific effort tier (`[xhigh]`, `[max]`,
  `[high]`) which is vendor-specific and not directly comparable
  across vendors. Two `[xhigh]` runs from GPT-5.5 and Claude Opus 4.8
  do not allocate the same wall-clock budget or the same number of
  internal reasoning tokens; the score table conflates this.
- **Sample size.** 113 tasks is small enough that confidence intervals
  are ±4–5 percentage points; rank order in the middle of the table
  is fragile.
- **Self-reported.** Submission and re-running policies are not fully
  documented on the public page; cross-vendor parity is best-effort.
- **One snapshot, no longitudinal data.** Unlike Vending-Bench 2 which
  tracks model regressions (Opus 4.8 < Opus 4.6 in absolute dollars),
  DeepSWE does not yet have a public history of how earlier Anthropic
  or OpenAI generations scored on the same 113 tasks, making it hard
  to read direction of travel for a model family.

## When to cite this benchmark

Cite DeepSWE as the canonical reference for **long-horizon
software-engineering ability under realistic developer prompts** —
short brief, long multi-file solution, behavioral verification.
It is the right benchmark for "would I let this model run unsupervised
on an unfamiliar repository for 20 minutes". For evaluations that
test code *review* rather than code *generation*, cite
[SWE-PRBench](./swe-prbench.md). For evaluations that test
business-process agentic coherence rather than coding, cite
[Vending-Bench 2](./vending-bench-2.md).

## In the knowledge graph

- **Primary axis:** [long-horizon agentic coherence](../concepts/long-horizon-agentic-coherence.md)
  (long-horizon coding sub-axis)
- **Related concepts:** [agentic scaffolding](../concepts/agentic-scaffolding.md),
  [reasoning effort](../concepts/reasoning-effort.md)
- **Models that lead here:** [GPT-5.5](../models/gpt-5-5.md),
  [Claude Opus 4.8](../models/claude-opus-4-8.md),
  [Claude Opus 4.7](../models/claude-opus-4-7.md)
- **See also:** [Vending-Bench 2](./vending-bench-2.md) (longer-horizon
  non-coding agentic companion), [SWE-PRBench](./swe-prbench.md)
  (review-not-generation companion)

## Related wiki pages

- [../frontier-leaderboard.md](../frontier-leaderboard.md)
- [../concepts/long-horizon-agentic-coherence.md](../concepts/long-horizon-agentic-coherence.md)
