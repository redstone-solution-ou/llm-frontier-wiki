# Long-Horizon Agentic Coherence

The capacity of a Large Language Model (LLM) to maintain coherent
identity, tool use, and decision-making across a long sequence of
agentic steps — thousands of tool calls, tens of millions of
tokens, or hundreds of simulated decision rounds — without
drifting off task, looping, hallucinating prior context, or
silently degrading.

## Intuition

Frontier capability benchmarks before 2026 mostly measured what a
model can do in *one shot* or in *a few thousand tokens*. By 2026
the binding constraint on real-world deployment is not single-step
ability — even mid-tier models pass most short-horizon evals — it
is whether the model can be left running inside an agent harness
for a meaningful amount of work without spiraling.

"Long-horizon agentic coherence" is the name this wiki uses for that
capacity. The word *coherence* is deliberate: the failure modes the
axis exposes are not failures of individual reasoning steps but
failures of *consistency across steps*. A model that paid an
invoice on day 47 and then paid the same invoice again on day 64
because it forgot the first payment did not reason badly at either
step; it reasoned coherently within each step and incoherently
across them.

The phrase the user originally proposed for this axis — *long-term
execution* — is in the same family but understates what is being
measured. "Execution" suggests carrying out a known plan; the
benchmarks on this axis specifically test situations where the
plan must be *recovered* or *re-formed* under summarization,
adversarial counterparties, and silent feedback. *Coherence* is
the property that makes execution possible in those conditions.

Alternative names the wiki considered and rejected:

- *Sustained agentic performance* — flat; "performance" is the
  noun benchmarks themselves use, which makes the axis name
  circular.
- *Operational endurance* — emphasizes time, but the benchmarks
  measure *coherent* time, not raw time. A model that loops for
  365 simulated days is "enduring" and useless.
- *Long-horizon planning* — accurate for the planning subcomponent
  but under-covers the identity-drift and attention-allocation
  facets that Vending-Bench 2 and SWE-PRBench respectively expose.

**Long-horizon agentic coherence** is the wiki's settled term.

## How it is measured

The wiki tracks three benchmarks on this axis, each probing a
different facet:

- [Vending-Bench 2](../benchmarks/vending-bench-2.md) (primary
  signal). A one-year simulated vending-machine business, 60–100M
  tokens per rollout, final bank balance averaged across 5 runs.
  Probes coherence under: (a) hard summarization (no model has a
  365-day context window), (b) silent reward (only end-of-year
  score), and (c) adversarial counterparties (suppliers exploit
  over-trust). This is the wiki's canonical reference for the
  axis.
- [DeepSWE](../benchmarks/deepswe.md) (coding sub-axis). 113
  original Software Engineering (SWE) tasks with median 668-line
  reference solutions from median 2,158-character prompts.
  Probes whether the model can hold a multi-file mental model
  together through 20+ minutes of repository exploration and
  edits. Wall-clock and token medians (47k tokens / 20 minutes
  for the leader) are explicit; this is *bounded* long-horizon,
  unlike Vending-Bench's unbounded simulation.
- [SWE-PRBench](../benchmarks/swe-prbench.md) (attention-
  allocation sub-axis). 350 pull-request reviews across three
  context configurations. The headline result — every model
  degrades from `config_A` (diff only) to `config_C` (full
  repository) — isolates *whether the model can use the long
  context it has*. A 1M-token context window means little if
  detection rate halves across that window.
- [Harness-Bench](../benchmarks/harness-bench.md) (scaffold-
  dependence sub-axis). 106 sandboxed tasks factorially crossed
  with 6 harnesses × 8 model backends. Does not score the model
  in isolation; instead measures how much of a given agent's
  score belongs to the harness. The category "Long-running
  Autonomy & State Adaptation" (11 tasks) overlaps the coherence
  axis directly. The paper's "execution alignment" framing
  (§5.2) gives a more precise name to what this axis previously
  called identity drift: reasoning becomes weakly coupled to the
  files, tools, evidence, state, or output contracts the
  evaluator can see.

The axis is best read by triangulating these benchmarks: a model that
scores well only on Vending-Bench 2 but poorly on SWE-PRBench may
be relying on its harness's summarization rather than on its own
attention; a model that scores well on DeepSWE but poorly on
Vending-Bench 2 holds together for 20 minutes but not for a
simulated year. The 2D map at
[`frontier-leaderboard.md`](../frontier-leaderboard.md) collapses
these three signals into one axis position; the leaf for each
benchmark exposes the underlying detail.

## Why it is a useful axis

Three predictions about real deployments fall out of the
long-horizon coherence axis that an aggregate-score leaderboard
hides:

1. **Agent harness suitability.** A model with high reasoning but
   low coherence will write a brilliant first response and then
   drift off task by the fifteenth tool call. A model with the
   opposite profile is the right pick for any deployment longer
   than ~50 tool calls. Vending-Bench 2 makes this prediction
   directly.
2. **Alignment-vs-coherence trade-off visibility.** Anthropic's own
   blog acknowledges that Opus 4.8 underperforms Opus 4.6 on
   Vending-Bench 2 despite being "a step forward in alignment".
   That regression is invisible on aggregate leaderboards and visible
   on this axis. Picking a frontier model for an autonomous-business
   role without consulting this axis is therefore a known way to
   regress.
3. **Long-context window claims are not long-context attention
   claims.** SWE-PRBench's `config_A → config_C` curve makes the
   point starkly: even when a model accepts a 1M-token context,
   its effective attention budget is smaller, and tasks that
   require *using* the long context degrade. Real-world deployment
   choices that depend on "model claims a 1M context window"
   should be cross-checked against this axis.

## Trade-offs and failure modes

- The axis is *coupled with the harness*. Vending-Bench 2 scores
  the model + scaffold jointly; isolating the model contribution
  requires controlling the summarizer chain, which the benchmark
  documentation does not do consistently.
- The axis is *coupled with alignment tuning*. Helpfulness-trained
  models over-trust adversarial suppliers; sycophancy-trained models
  underprice. Alignment work that improves single-step behavior can
  regress multi-step behavior, and the axis exposes that.
- Benchmarks on this axis are *expensive*: a single Vending-Bench 2
  run is 60–100M tokens. Frontier-model evaluations on the axis are
  necessarily sparse and slow, which means the public leaderboard
  lags the actual frontier by months.
- The axis *does not* measure raw intellectual ceiling. A model that
  scores well here is not necessarily smart at hard mathematics —
  see the
  [frontier reasoning](frontier-reasoning.md) page.

## Models that exemplify high values on this axis

- [Claude Opus 4.6](../models/claude-opus-4-7.md) — $8,017.59 on
  Vending-Bench 2 (2026-02), the public-leaderboard leader and the
  reference point against which Opus 4.8's regression is read.
  Claude Opus 4.7 (covered on the same model leaf cluster) is
  reported as the current vendor pick for long-horizon agentic
  jobs, leading the Vending-Bench Arena variant per secondary
  sources.
- [GPT-5.5](../models/gpt-5-5.md) — 70% ±4% on DeepSWE with the
  smallest median output tokens (47k) and wall-clock time (20 min)
  of any top-five entry, indicating efficient long-horizon coding
  rather than brute-force token-burn.
- [GLM-5.1](../models/glm-5-1.md) — $5,634.41 on Vending-Bench 2,
  the strongest open-source result on the axis as of 2026-06.

## Open questions

- Is long-horizon agentic coherence a *capability* or a *training
  side effect*? Anthropic's Opus 4.8 regression vs Opus 4.6 suggests
  the latter is at least possible — i.e. that coherence can be
  *lost* during further alignment tuning. A clean answer requires
  intervention studies the public has not seen yet.
- What is the harness-vs-model decomposition of the score?
  Vending-Bench 2 documentation does not isolate this; the
  "memory paradox" finding (60k context windows underperforming
  30k) suggests scaffold choices are weight-bearing.
- Does coherence transfer across domains? A model that holds
  together on Vending-Bench 2 (business simulation) may or may
  not hold together on a long-horizon scientific research task.
  No public benchmark currently bridges these domains.
- Is there a measurable "coherence horizon" beyond which every
  model fails? Vending-Bench 2's theoretical optimum (~$63k) is
  ~8× higher than the best public result (~$8k); the gap suggests
  every current model is well below that horizon.
- Can short-horizon evaluations predict long-horizon coherence?
  If not, the axis cannot be cheaply screened; if yes, the
  benchmark cost story changes.

## Related wiki pages

- [frontier-reasoning.md](frontier-reasoning.md) — the other
  organizing axis.
- [agentic-scaffolding.md](agentic-scaffolding.md) — the
  harness layer that the model is jointly scored with;
  empirically grounded by
  [Harness-Bench](../benchmarks/harness-bench.md).
- [reasoning-effort.md](reasoning-effort.md) — effort tiers
  affect coherence-axis scores significantly.
- [../benchmarks/vending-bench-2.md](../benchmarks/vending-bench-2.md)
- [../benchmarks/deepswe.md](../benchmarks/deepswe.md)
- [../benchmarks/swe-prbench.md](../benchmarks/swe-prbench.md)
- [../benchmarks/harness-bench.md](../benchmarks/harness-bench.md)
- [../frontier-leaderboard.md](../frontier-leaderboard.md)
