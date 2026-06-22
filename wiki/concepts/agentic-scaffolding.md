# Agentic Scaffolding

The harness layer around a Large Language Model (LLM) — the tool
specifications, summarization chain, retry policy, memory layout,
and judge configuration — that turns a raw next-token predictor
into an agent. The wiki cares about scaffolding because every
benchmark on the
[long-horizon agentic coherence](long-horizon-agentic-coherence.md)
axis scores model + scaffold jointly, and the scaffold contribution
is often not separable from the model contribution in the public
data.

## Intuition

A frontier model's nominal capability — what it can do in a
single forward pass on a clean prompt — is only loosely connected
to its capability *inside an agent loop*. Inside the loop the
model interacts with:

- A **tool layer** that defines the action vocabulary.
- A **summarizer** that compresses past turns once they no longer
  fit in the context window.
- A **retry / verifier policy** that decides whether the model
  gets another attempt after an apparent failure.
- A **memory layout** that controls what the model sees and in
  what order on each tool turn.
- An **evaluator / judge** that scores the final outcome.

Three of the four benchmarks the wiki tracks
([Vending-Bench 2](../benchmarks/vending-bench-2.md),
[DeepSWE](../benchmarks/deepswe.md),
[SWE-PRBench](../benchmarks/swe-prbench.md)) jointly score model
and scaffold and do not isolate them. [FrontierMath](../benchmarks/frontiermath.md)
is the exception: it uses a thin scaffold (the model emits a
Python `answer()` function which is then executed), which is part
of why it functions cleanly as a *model-only* reasoning probe.

## Why the wiki tracks it

- **The Harness-Bench 23.8-point gap.** The single most direct
  empirical anchor for the concept is
  [Harness-Bench](../benchmarks/harness-bench.md) (Yao et al.,
  arXiv:2605.27922, 2026-05): on 106 sandboxed tasks evaluated
  factorially across 6 configurable harnesses × 8 model backends,
  the aggregate score gap between the best and worst harness is
  **23.8 percentage points** (NanoBot 76.2 vs OpenClaw 52.4) on
  the *same task set and model-backend pool*. The paper's
  recommendation is to report agent capability at the
  model-harness configuration level rather than attributing it to
  the base model alone — exactly the framing this wiki adopts.
  The paper's compact summary equation, "Agent = Model + Harness",
  matches the wiki's claim almost verbatim.
- **The "memory paradox" finding.** Vending-Bench 2's documentation
  notes that **60k-token context windows sometimes underperform
  ~30k windows** on the same task, attributable to signal dilution
  in the summarization layer. This is a scaffold property
  reflected in the model's score.
- **Configuration-A vs Configuration-C degradation.** SWE-PRBench
  shows every model degrading monotonically as context expands.
  This is partly a model property (attention allocation) and
  partly a scaffold property (which 2k tokens of the 50k-token
  repository did the harness surface to the model?). The paper
  reports that a structured 2,000-token diff-with-summary prompt
  outperforms a 2,500-token full-context prompt — i.e. *scaffold
  choice changes the score by more than the prompt size
  difference*.
- **Vendor scaffold vs standardized scaffold.** On
  SWE-Bench Pro, the same model (Claude Opus 4.8) has been
  reported at 69.2% under Anthropic's own scaffold and at lower
  numbers under standardized scaffolds. This kind of vendor /
  third-party gap is the single most common cause of apparent
  contradictions between LLM leaderboards.

## Execution alignment — the failure-mode lens

[Harness-Bench](../benchmarks/harness-bench.md) introduces a more
precise term for what the wiki has been calling "scaffold
contribution": **execution alignment** — "the degree to which a
harness preserves correspondence among the agent's reasoning, the
observed workspace state, the actions taken through tools, and the
conditions checked by the evaluator" (Harness-Bench §5.2). Failures
are framed as *execution drift*: model reasoning becomes "weakly
coupled to the files, tools, evidence, state, or output contracts
through which success is ultimately judged".

The Harness-Bench failure taxonomy (Table 3) names five recurring
symptoms across the 5,194 trajectories analyzed:

| Symptom | Rate among failures | Lens |
|---------|--------------------:|------|
| Contract / format | 36.4% | Output is locally plausible but violates the schema, manifest, or ledger the evaluator checks |
| Tool / recovery | 24.6% | Tool errors are observed but not followed by recovery or plan revision |
| Evidence / grounding | 14.6% | Claims are made without source coverage; verification is incomplete |
| Artifact commitment | 11.1% | Plausible reasoning is not converted into the workspace artifact the task requires |
| State / continuation | 9.3% | Multi-round or interrupted tasks lose durable progress between turns |

These are useful labels for the wiki's [long-horizon-agentic-coherence](long-horizon-agentic-coherence.md)
discussion: most of what the wiki has called "identity drift" or
"silent failure" is in fact execution drift in the Harness-Bench
sense.

## A revealing cross-benchmark observation

[Claude Opus 4.6](../models/claude-opus-4-7.md) is the
[Vending-Bench 2](../benchmarks/vending-bench-2.md) public-
leaderboard leader at $8,017.59 *and* one of the two highest-
variance backends on [Harness-Bench](../benchmarks/harness-bench.md)
(the other is `deepseek-v4-flash`). Both can be true: Opus 4.6 is
strong inside a dedicated, well-tuned long-horizon scaffold and
brittle across arbitrary scaffold swaps. This is the picture the
concept page predicts; Harness-Bench is the first benchmark to
make it visible in numbers.

## How scaffolding interacts with the wiki's axes

- On the
  [long-horizon agentic coherence](long-horizon-agentic-coherence.md)
  axis, scaffolding is a load-bearing co-determinant of every
  score. A claim like "model X is better than model Y on
  Vending-Bench 2" implicitly says "model X plus the scaffold
  submitter Z chose is better than model Y plus the scaffold
  submitter W chose". The wiki marks scores as self-reported
  whenever this caveat applies.
- On the
  [frontier reasoning](frontier-reasoning.md) axis, scaffolding
  effects are smaller because the FrontierMath Python-`answer()`
  protocol is thin. Reasoning-axis claims are therefore closer
  to clean model claims.

## How to think about scaffold contribution

A useful first-pass heuristic the wiki recommends:

- If two leaderboards disagree on rank order, **check whether
  one is under vendor scaffold and the other under a standardized
  scaffold**. Most apparent contradictions resolve to this.
- If the same model on the same benchmark has two different
  scores filed weeks apart, **check whether the scaffold version
  changed** (DeepSWE, Vending-Bench 2, and SWE-PRBench all
  version their harnesses; SWE-PRBench at v0.4.1 as of 2026-06).
- If a model claims a context-window-driven capability gain,
  **check it against
  [SWE-PRBench](../benchmarks/swe-prbench.md)'s `config_A → config_C`
  degradation curve**. Long-context capability claims that are
  not validated against actual long-context attention are
  unreliable.

## Related wiki pages

- [long-horizon-agentic-coherence.md](long-horizon-agentic-coherence.md)
  — every benchmark on this axis scores model + scaffold jointly.
- [reasoning-effort.md](reasoning-effort.md) — effort and scaffold
  are often controlled by different parties (vendor sets effort,
  submitter sets scaffold), which compounds the comparability
  problem.
- [../benchmarks/harness-bench.md](../benchmarks/harness-bench.md)
  — the canonical empirical anchor for this concept.
- [../benchmarks/vending-bench-2.md](../benchmarks/vending-bench-2.md)
- [../benchmarks/swe-prbench.md](../benchmarks/swe-prbench.md)
- [../frontier-leaderboard.md](../frontier-leaderboard.md)
