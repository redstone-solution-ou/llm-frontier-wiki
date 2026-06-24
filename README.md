# LLM Frontier — Research Wiki

This repository organizes the current state of the Large Language
Model (LLM) frontier as a navigable knowledge graph. It is built
around two organizing axes that the wiki argues are load-bearing
for choosing a frontier model:

1. **Frontier reasoning** — the model's ceiling on long-form,
   research-level intellectual problems. Probed primarily by
   [FrontierMath Tier 4 (v2)](wiki/benchmarks/frontiermath.md).
2. **Long-horizon agentic coherence** — the model's ability to
   maintain coherent tool use, planning, and decision-making across
   thousands of agentic steps without identity drift, looping, or
   silent failure. Probed primarily by
   [Vending-Bench 2](wiki/benchmarks/vending-bench-2.md), with
   [DeepSWE](wiki/benchmarks/deepswe.md) and
   [SWE-PRBench](wiki/benchmarks/swe-prbench.md) as the coding
   companions.

The hypothesis the wiki defends — and refines as new scores land —
is that aggregate-score leaderboards mix these two axes in ways
that hide useful structure. A model can lead the reasoning frontier
and still drift into a 30-message loop inside an agent harness; a
model can hold its identity across a one-year vending-machine
simulation and still miss an integration-of-distributions
question that a Mathematical Olympiad student would solve. The
right model for a job depends on which axis the job lives on.

## Start here

- [wiki/frontier-leaderboard.md](wiki/frontier-leaderboard.md) — the
  2D ranking page. The single artifact most readers come here for:
  every tracked model placed on (reasoning, long-horizon) with the
  benchmark numbers that justify the placement.
- [wiki/overview.md](wiki/overview.md) — the wiki entry point and
  the longer-form story behind the two axes.
- [wiki/index.md](wiki/index.md) — flat catalog of every wiki page
  with a one-line gloss; the first stop when you know a topic but
  not where it lives.
- [wiki/log.md](wiki/log.md) — chronological append-only record of
  ingests, queries-filed-back, lint passes, and refactors.

## Structure

- `papers/` — cached source material (benchmark methodology pages,
  papers, system cards). Treated as immutable references.
- `wiki/` — the markdown knowledge graph. Top-level folders are
  `concepts/` (the two axes and supporting cross-cutting ideas),
  `benchmarks/` (one leaf per benchmark), and `models/` (one leaf
  per tracked frontier model).

## Section hubs

- [wiki/concepts/concepts.md](wiki/concepts/concepts.md) — the two
  organizing axes (frontier reasoning, long-horizon agentic
  coherence) and the supporting concepts (reasoning effort, agentic
  scaffolding) that the wiki uses to interpret benchmark numbers.
- [wiki/benchmarks/benchmarks.md](wiki/benchmarks/benchmarks.md) —
  the four primary benchmarks that the wiki currently tracks:
  Vending-Bench 2, DeepSWE, FrontierMath, SWE-PRBench.
- [wiki/models/models.md](wiki/models/models.md) — one leaf per
  frontier model, with the model's scores on every tracked
  benchmark and its position on the two axes.

## Scope (as of 2026-06)

Version 0 covers four primary benchmarks, two organizing axes, and
six frontier models. The selection is deliberately small: the wiki's
goal is to be *correctly opinionated* about the axes that matter,
not to mirror every leaderboard on the web. Additions land via the
ingest workflow in [CLAUDE.md](CLAUDE.md); the two primary-axis boards
(FrontierMath Tier 4 v2 and Vending-Bench 2) are re-checked against
their official operator pages on a recurring cadence — see the
"Refresh: periodic leaderboard re-check" workflow in
[CLAUDE.md](CLAUDE.md) — so the rankings stay current.

Benchmarks tracked:

- [Vending-Bench 2](wiki/benchmarks/vending-bench-2.md) —
  Andon Labs, 2026. A simulated one-year vending-machine business;
  60–100M tokens per run; final bank balance is the only metric.
  The canonical *long-horizon agentic coherence* reference.
- [DeepSWE](wiki/benchmarks/deepswe.md) — DeepSWE.net, 2026.
  113 original, gold-commit-free Software Engineering (SWE) tasks
  across 91 active open-source repositories in five languages;
  short prompts, multi-file long solutions. The *long-horizon
  coding* companion to Vending-Bench 2.
- [FrontierMath](wiki/benchmarks/frontiermath.md) — Epoch AI,
  v2 released 2026-06. 338 unpublished research-grade mathematics
  problems split into Tiers 1–3 (295 problems) and Tier 4 (43
  problems, the hardest set). The canonical *frontier reasoning*
  reference.
- [SWE-PRBench](wiki/benchmarks/swe-prbench.md) — Foundry AI,
  2026-03 (arXiv:2603.26130). 350 pull requests with human-annotated
  ground truth for AI code review; the leaf focuses on the
  three-config attention-degradation curve and on why code
  *review* is a different evaluation regime from code generation.

Models tracked: Claude Fable 5, Claude Opus 4.7, Claude Opus 4.8,
GPT-5.5 (and GPT-5.5 Pro), GLM-5.2, Gemini 3 Pro. Each model has
a leaf with its scores on every tracked benchmark and a one-line
axis position summary.

## Credits and license

Cached source pages under `papers/` are reproduced under their
original licenses (operator pages, arXiv preprints, vendor system
cards); copyright remains with the respective authors and
operators. The wiki text (everything under `wiki/`, and this
README) is released under CC-BY-4.0.

## Related wiki pages

- [wiki/overview.md](wiki/overview.md)
- [wiki/frontier-leaderboard.md](wiki/frontier-leaderboard.md)
