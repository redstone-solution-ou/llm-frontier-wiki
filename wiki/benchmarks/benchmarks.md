# Benchmarks

The leaf layer of the wiki — one short page per primary benchmark
that the wiki uses to position Large Language Models (LLMs) on its
two organizing axes. Every claim on a leaf cites the benchmark's
own methodology page, its published paper, or a documented
secondary mirror; for cross-benchmark synthesis see the
[concepts](../concepts/concepts.md) pages, and for the live
ranking see [`frontier-leaderboard.md`](../frontier-leaderboard.md).

The four benchmarks below were chosen because each one *isolates*
something the others miss. Tile them together and the result is a
2-dimensional map of frontier capability. Use any single benchmark
in isolation and the picture is wrong in known ways.

## Long-horizon agentic coherence — agent-loop probes

The wiki's primary axis on this side measures whether a model can
*hold its situation together* across long agentic trajectories.
Different benchmarks probe different facets:

- [Vending-Bench 2](vending-bench-2.md) — Andon Labs, 2026. Operate
  a simulated vending-machine business for a full year (365 days,
  3,000–6,000 messages, 60–100M tokens per run). Final bank balance
  is the only metric. The canonical reference for **long-horizon
  agentic coherence**: identity drift, looping, hallucinated
  supplier emails, and silent failure modes are exactly what this
  benchmark catches that single-step reasoning cannot.
- [DeepSWE](deepswe.md) — DeepSWE.net, 2026. 113 original software-
  engineering tasks across 91 open-source repositories in five
  languages, with short prompts and median 668-line / 7-file
  reference solutions. Behavioral verifiers grade outcomes, not
  reference-implementation match. The **long-horizon coding**
  companion to Vending-Bench 2 — same coherence question, narrower
  task domain.
- [SWE-PRBench](swe-prbench.md) — Foundry AI, 2026
  (arXiv:2603.26130). 350 pull requests with human-annotated review
  ground truth across three context configurations
  (diff-only / diff+files / full repository). The headline finding
  is that **every model degrades monotonically as context expands**
  — long-context attention degradation, isolated. This is the
  attention-allocation sub-axis of long-horizon coherence: even
  when the model is given all the information it needs, can it
  actually attend to it?
- [Harness-Bench](harness-bench.md) — Peking University + Qiyuan
  Tech, 2026 (arXiv:2605.27922). 106 sandboxed offline tasks
  evaluated factorially across 6 configurable harnesses × 8 model
  backends (5,194 trajectories). Fixes external task conditions
  and lets each harness run with its native execution behavior.
  Headline number: a **23.8-point aggregate gap between the best
  and worst harness on the same model-backend pool** (NanoBot 76.2
  vs OpenClaw 52.4). The canonical empirical anchor for the
  [agentic-scaffolding](../concepts/agentic-scaffolding.md)
  concept — "Agent = Model + Harness", measured directly.

## Frontier reasoning — research-grade reasoning probe

The wiki's primary axis on this side measures *intellectual
ceiling*: the hardest problems a model can solve when given
unlimited time per question but constrained by a hard inference-
token budget.

- [FrontierMath](frontiermath.md) — Epoch AI, v2 released
  2026-06-12. 338 unpublished mathematics problems written and
  vetted by expert mathematicians, split into a 295-problem base
  set (Tiers 1–3) and a 43-problem research-grade expansion
  (Tier 4). Verified via Python `answer()` functions with a hard
  1,000,000-token-per-problem budget. The canonical reference for
  **frontier reasoning**: contamination-resistant, judge-free,
  budget-gated.

## Index by slug

| Slug | Primary axis | Operator | Latest leaderboard | Sample size |
|------|--------------|----------|--------------------|-------------|
| [deepswe](deepswe.md) | long-horizon agentic coherence (coding) | DeepSWE benchmark team | 2026-05-30 | 113 tasks |
| [frontiermath](frontiermath.md) | frontier reasoning | Epoch AI | 2026-06 (v2) | 338 problems (43 in Tier 4) |
| [harness-bench](harness-bench.md) | agentic scaffolding (with long-horizon-coherence secondary) | Peking University + Qiyuan Tech | 2026-05 (arXiv v1) | 106 tasks × 6 harnesses × 8 backends = 5,194 trajectories |
| [swe-prbench](swe-prbench.md) | long-horizon agentic coherence (review / attention) | Foundry AI | 2026-03 (paper baseline) | 350 PRs (100-PR eval split) |
| [vending-bench-2](vending-bench-2.md) | long-horizon agentic coherence (business sim) | Andon Labs | 2026-06-22 | 365-day simulated year per run |

## Why these four together

The four-benchmark set is deliberately small. A 2D capability map
that tries to mirror every leaderboard becomes a leaderboard itself
and stops being informative. The argument the wiki makes is that:

- One benchmark per axis is the minimum for a 2D claim
  (FrontierMath Tier 4 ↔ frontier reasoning; Vending-Bench 2 ↔
  long-horizon agentic coherence).
- Two extra benchmarks are needed to triangulate the coherence axis,
  because a single number on a single eval cannot distinguish
  "model holds together for 5 minutes" from "model holds together
  for 365 simulated days" — DeepSWE adds the multi-file coding
  facet, SWE-PRBench adds the attention-allocation facet.
- Harness-Bench is a *meta-benchmark*: it does not add a third axis
  of capability, it isolates the *scaffolding contribution* that
  the other four benchmarks score jointly with the model. Adding
  it makes the wiki's existing scaffolding caveats empirically
  grounded rather than anecdotal.

## Related wiki pages

- [../concepts/concepts.md](../concepts/concepts.md) — the two
  organizing axes and supporting concepts.
- [../frontier-leaderboard.md](../frontier-leaderboard.md) — the
  live 2D ranking page.
- [../overview.md](../overview.md) — the wiki entry point and the
  longer story behind the two-axis structure.
