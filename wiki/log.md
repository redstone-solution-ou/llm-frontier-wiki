# Wiki Log

Append-only chronological record of work on this wiki. Newest at
the bottom. Each entry uses a consistent prefix so the log is
parseable with simple tools (`grep "^## \[" log.md | tail -10`).

## [2026-06-22] scaffold | Initial repo created

Created the repository skeleton following the
[llm-wiki.md](../llm-wiki.md) pattern adapted to the LLM frontier
domain. Three layers in place: `papers/` (reserved for cached
benchmark methodology snapshots — empty at this filing, the
benchmarks tracked are live web sources), `wiki/` (LLM-owned
markdown), and [`CLAUDE.md`](../CLAUDE.md) (schema). Sections
instantiated: `concepts/`, `benchmarks/`, `models/`. The wiki is
organized around two axes
([frontier-reasoning.md](concepts/frontier-reasoning.md) and
[long-horizon-agentic-coherence.md](concepts/long-horizon-agentic-coherence.md))
and culminates in the 2D ranking page
[`frontier-leaderboard.md`](frontier-leaderboard.md).

## [2026-06-22] ingest | Vending-Bench 2 (Andon Labs)

Added [Vending-Bench 2](benchmarks/vending-bench-2.md). Primary
signal for the
[long-horizon agentic coherence](concepts/long-horizon-agentic-coherence.md)
axis. Public leaderboard mirrored from
[llm-stats.com/benchmarks/vending-bench-2](https://llm-stats.com/benchmarks/vending-bench-2)
(refresh date 2026-06-22): Claude Opus 4.6 $8,017.59, GLM-5.1
$5,634.41, Gemini 3 Pro $5,478.16, Gemini 3 Flash $3,635.00.
Methodology and known failure modes synthesized from the
operator's own page, the maxpool report, and Andon Labs blog
posts cited inline. Noted explicitly that the leaderboard is
self-reported and that newer Anthropic models (Opus 4.7, 4.8,
Fable 5) have side-channel data but no canonical leaderboard
entry. Touched [models/claude-opus-4-7.md](models/claude-opus-4-7.md),
[models/claude-opus-4-8.md](models/claude-opus-4-8.md),
[models/glm-5-2.md](models/glm-5-2.md) (then filed as glm-5-1), and
[models/gemini-3-pro.md](models/gemini-3-pro.md) with the relevant
rows.

## [2026-06-22] ingest | DeepSWE

Added [DeepSWE](benchmarks/deepswe.md). Long-horizon coding
companion benchmark on the
[long-horizon agentic coherence](concepts/long-horizon-agentic-coherence.md)
axis. 113 original tasks across 91 open-source repositories in five
languages, behavioral verifiers, median 668-line / 7-file
reference solutions from median 2,158-character prompts. Public
leaderboard mirrored from [deepswe.net](https://deepswe.net/)
(refresh 2026-05-30): GPT-5.5 [xhigh] 70% ±4% with 47k median
output tokens and 20-min median wall-clock; Opus 4.8 [max]
58% ±5%; GPT-5.4 [xhigh] 56% ±5%; Opus 4.7 [max] 54% ±5%; Sonnet
4.6 [high] 32% ±4%. Touched [models/gpt-5-5.md](models/gpt-5-5.md),
[models/claude-opus-4-8.md](models/claude-opus-4-8.md), and
[models/claude-opus-4-7.md](models/claude-opus-4-7.md).

## [2026-06-22] ingest | FrontierMath (Tiers 1–3 v2 and Tier 4 v2)

Added [FrontierMath](benchmarks/frontiermath.md). Primary signal
for the [frontier reasoning](concepts/frontier-reasoning.md) axis.
v2 released 2026-06-12 with corrections to 42% of v1 problems.
338 unpublished problems split into Tiers 1–3 (295 base set) and
Tier 4 (43 research-grade expansion). Verified via Python
`answer()` function with hard 1,000,000-token budget per problem.
Top-5 ranking mirrored from
[lmcouncil.ai/benchmarks](https://lmcouncil.ai/benchmarks)
(refresh 2026-06): Tier 4 v2 led by Claude Fable 5 [max] at
87.8% ±5.2 with GPT-5.5 Pro [xhigh] second at 78.0% ±6.5; Tiers
1–3 v2 led by GPT-5.5 Pro [xhigh] at 87.7% ±1.9 with Fable 5
second at 87.0% ±2.0. Order flips between tiers — Fable 5 is
deeper, GPT-5.5 Pro broader. Touched
[models/claude-fable-5.md](models/claude-fable-5.md),
[models/gpt-5-5.md](models/gpt-5-5.md), and
[models/claude-opus-4-8.md](models/claude-opus-4-8.md).

## [2026-06-22] ingest | SWE-PRBench

Added [SWE-PRBench](benchmarks/swe-prbench.md). Long-context
attention-degradation companion benchmark on the
[long-horizon agentic coherence](concepts/long-horizon-agentic-coherence.md)
axis. 350 pull requests with human-annotated review ground truth
across three context configurations (diff-only, diff+files, full
repository). Paper baseline leaderboard (judge: GPT-5.2; pipeline
v0.4.1; eval_100 split) led by Claude Haiku 4.5 at 0.153
weighted score; no model detects more than 31% of human-flagged
issues on any configuration. Headline finding: every model
degrades monotonically as context expands; a structured
2,000-token diff-with-summary prompt outperforms a 2,500-token
full-context prompt across all models. The user's local fork at
`~/Desktop/workspace/swe-prbench` extends the harness with a
Claude Code CLI provider for evaluating Opus 4.7/4.8 effort
tiers; those results are not in the paper baseline.

## [2026-06-22] feature | Two-axis structure adopted

Renamed the user's "long-term execution / planning" intuition to
[long-horizon agentic coherence](concepts/long-horizon-agentic-coherence.md)
after considering and rejecting alternatives (*sustained agentic
performance*, *operational endurance*, *long-horizon planning*).
The new name captures three facets that the alternatives under-
cover: identity drift (the Vending-Bench 2 "paid the invoice
twice" failure mode), attention-allocation under summarization
(the SWE-PRBench `config_A → config_C` degradation), and
tool-use consistency across thousands of steps. Retained the
user's "intellectual capability" intuition as
[frontier reasoning](concepts/frontier-reasoning.md).

## [2026-06-22] feature | Frontier leaderboard 2D chart generated

Built [frontier-leaderboard.md](frontier-leaderboard.md) — the
single page the wiki is centered on. ASCII chart places every
tracked model on (Vending-Bench 2 $, FrontierMath Tier 4 v2 %).
Three findings the chart surfaces that aggregate leaderboards
hide: (a) the two axes are independent, (b) same-vendor models
can disagree across axes (Opus 4.8 reasoning rank-5 with
documented Vending-Bench 2 regression vs Opus 4.6), (c) the
upper-right quadrant is empty — no current model leads both
axes. Working picks by job shape filed at the bottom of the
chart page.

## [2026-06-22] ingest | Harness-Bench (Yao et al., Peking University + Qiyuan Tech, arXiv:2605.27922)

Added [Harness-Bench](benchmarks/harness-bench.md). PDF cached at
[`papers/harness-bench_2605.27922.pdf`](../papers/harness-bench_2605.27922.pdf).
Primary axis: [agentic scaffolding](concepts/agentic-scaffolding.md);
secondary signal on
[long-horizon agentic coherence](concepts/long-horizon-agentic-coherence.md).
The paper is a diagnostic benchmark for the harness contribution:
106 sandboxed tasks evaluated factorially across 6 configurable
harnesses (OpenClaw, ZeroClaw, Hermes, Moltis, NullClaw, NanoBot)
× 8 API model backends (claude-opus-4.6, claude-sonnet-4.6,
gemini-3.1-pro-preview, qwen3.6-plus, glm-5.1, kimi-k2.5, gpt-5.4,
deepseek-v4-flash), 5,194 trajectories total. Score formula
`Security · Completion · Process`. Judge: claude-sonnet-4.6 (fixed
external). Headline finding: a 23.8-point aggregate score gap
between NanoBot (76.2) and OpenClaw (52.4) on the same
task-and-backend pool; Codex (specialized stack with gpt-5.4)
reported separately at 80.4 as a practical reference point.
Introduces "execution alignment" / "execution drift" as a precise
framing for what the wiki had previously called identity drift.
Top failure modes: contract/format violations (36.4%), tool/
recovery (24.6%), evidence/grounding (14.6%), artifact commitment
(11.1%), state/continuation (9.3%). Notable cross-benchmark
observation filed in the leaf: claude-opus-4.6 is the
[Vending-Bench 2](benchmarks/vending-bench-2.md) public-leaderboard
leader *and* one of the two highest cross-harness variance
backends on Harness-Bench — both true, both meaningful. Touched
[benchmarks/benchmarks.md](benchmarks/benchmarks.md) (hub +
"Why these together" section now distinguishes Harness-Bench as a
meta-benchmark), [concepts/agentic-scaffolding.md](concepts/agentic-scaffolding.md)
(new sections "Execution alignment — the failure-mode lens" and
"A revealing cross-benchmark observation"),
[concepts/long-horizon-agentic-coherence.md](concepts/long-horizon-agentic-coherence.md)
(triangulating-benchmarks list extended), and
[index.md](index.md).

## [2026-06-22] refactor | 2D chart upgraded from ASCII to matplotlib

Replaced the ASCII chart on
[frontier-leaderboard.md](frontier-leaderboard.md) with a
matplotlib scatter plot at
[`wiki/assets/frontier-leaderboard.png`](assets/frontier-leaderboard.png).
The generator script
[`scripts/generate_frontier_chart.py`](../scripts/generate_frontier_chart.py)
is the single source of truth for placements: the `MODELS` table
at the top of the file is the editable list. Models are colored
by vendor (Anthropic, OpenAI, Google, Zhipu AI). Marker shape
signals placement confidence: filled circle = both axes measured;
hollow square = proxy or inferred placement; down-arrow caret =
absent from the FrontierMath Tier 4 v2 top-5, y plotted as a
conservative ceiling. FrontierMath ±% confidence intervals appear
as vertical error bars on measured points. The empty upper-right
"frontier" quadrant is shaded to highlight the wiki's headline
observation that no current model leads both axes. Schema in
[CLAUDE.md](../CLAUDE.md) extended with a "Generated assets"
convention (one script under `scripts/` per asset under
`wiki/assets/`; edit-script-then-regen-PNG flow).

## [2026-06-22] scope | Models and benchmarks tracked at v0

Six models tracked: [Claude Fable 5](models/claude-fable-5.md),
[Claude Opus 4.7](models/claude-opus-4-7.md),
[Claude Opus 4.8](models/claude-opus-4-8.md),
[GPT-5.5](models/gpt-5-5.md) (with GPT-5.5 Pro variant),
[GLM-5.1](models/glm-5-2.md), [Gemini 3 Pro](models/gemini-3-pro.md).
Four benchmarks tracked:
[Vending-Bench 2](benchmarks/vending-bench-2.md),
[DeepSWE](benchmarks/deepswe.md),
[FrontierMath](benchmarks/frontiermath.md),
[SWE-PRBench](benchmarks/swe-prbench.md). Selection criterion: every
model is on the top-5 of at least one tracked benchmark's primary
ranking, except Opus 4.7 which is tracked because Anthropic and
secondary coverage identify it as the current Vending-Bench Arena
vendor pick despite no canonical 5-run-average filing.

## [2026-06-23] refresh | Vending-Bench 2 official leaderboard — Opus 4.7 now rank 1

Re-checked [Vending-Bench 2](benchmarks/vending-bench-2.md) against
the official Andon Labs page
([andonlabs.com/evals/vending-bench-2](https://andonlabs.com/evals/vending-bench-2),
accessed 2026-06-23) after a user flagged the score as stale. The
2026-06-22 snapshot had been built from a lagging llm-stats mirror and
was wrong at the top. The official board now lists 49 models, led by
**Claude Opus 4.7 at $10,936.76** (first model past $10k), then
**GLM-5.2 $8,313.78**, **Claude Opus 4.6 $8,017.59**, **GPT-5.5
$7,523.84**, **Claude Sonnet 4.6 $7,204.14**; Opus 4.8 (`- High`) is
rank 9 ($5,787.43) and Fable 5 (`- High`) rank 10 ($5,680.26).
Corrections: Opus 4.7 promoted from "no canonical filing / Arena vendor
pick" to outright leader; the open-weights leaf renamed
[models/glm-5-1.md → models/glm-5-2.md](models/glm-5-2.md) ($5,634.41 →
$8,313.78, now above Opus 4.6); Opus 4.8 and Fable 5 reclassified from
side-channel / single-best estimates to on-board five-run averages;
Gemini 3 Pro ($5,478.16) marked below the current top ten. Folded in
the official trend analysis (+$799/month Western, +$1,047/month Chinese,
~131-day lag, projected crossover Aug 2027) and methodology levers
($100 per 1M output tokens billed weekly, ~69k context window). Touched
[benchmarks/vending-bench-2.md](benchmarks/vending-bench-2.md),
[frontier-leaderboard.md](frontier-leaderboard.md),
[models/claude-opus-4-7.md](models/claude-opus-4-7.md),
[models/glm-5-2.md](models/glm-5-2.md),
[models/gpt-5-5.md](models/gpt-5-5.md),
[models/claude-opus-4-8.md](models/claude-opus-4-8.md),
[models/claude-fable-5.md](models/claude-fable-5.md),
[models/gemini-3-pro.md](models/gemini-3-pro.md),
[models/models.md](models/models.md), [overview.md](overview.md),
[index.md](index.md),
[concepts/long-horizon-agentic-coherence.md](concepts/long-horizon-agentic-coherence.md),
[benchmarks/harness-bench.md](benchmarks/harness-bench.md), and
[scripts/generate_frontier_chart.py](../scripts/generate_frontier_chart.py)
(chart regenerated).
