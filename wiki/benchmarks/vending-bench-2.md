# Vending-Bench 2

> **Short name:** `vending-bench-2` · **URL:** [andonlabs.com/evals/vending-bench-2](https://andonlabs.com/evals/vending-bench-2) · **Operator:** Andon Labs · **Latest leaderboard refresh:** 2026-06-23

## What it measures

Vending-Bench 2 measures **long-horizon agentic coherence**: whether a
Large Language Model (LLM) can hold its identity, tool use, and
decision-making together across an entire simulated year of running a
small business — roughly 3,000–6,000 tool messages and 60–100M tokens
in a single rollout. The benchmark sits squarely on the
[long-horizon agentic coherence](../concepts/long-horizon-agentic-coherence.md)
axis of this wiki: it cannot be solved by raw intellectual capacity
alone, because the failure modes it exposes — looping, identity
drift, hallucinated supplier emails, pricing below cost, paying the
same invoice twice — are not failures of reasoning at any single
step but failures of *coherence across thousands of steps*.

## Methodology

A model is given $500 of starting capital and tasked with operating a
vending-machine business for 365 simulated days. Each day costs $2 in
location fees, and a model that fails to pay for 10 consecutive days
goes bankrupt and the run ends early. Within a day the model must
purchase inventory from multiple simulated suppliers (who negotiate,
sometimes adversarially), set prices, respond to customer complaints,
manage cash flow, and make strategic decisions about which products to
stock.

Two harness levers are load-bearing and documented in the system
prompt: the agent's working context is **limited to ~69,000 tokens**
(older messages are trimmed automatically, keeping ~61% of messages),
and the agent is **charged $100 per million output tokens, billed
weekly** — so verbose, token-burning strategies are penalized directly
in the score. The only metric is the **final bank balance**, averaged
across **5 independent runs per model**
([Andon Labs, Vending-Bench 2](https://andonlabs.com/evals/vending-bench-2),
accessed 2026-06-23). Operating costs are real ($2/day means $730/year
baseline overhead before token costs), so a passive model that does
nothing goes bankrupt; profit requires *active*, *consistent*,
*correct* business behavior across the full year.

## What makes it discriminative

Three design choices make Vending-Bench 2 a sharp test of long-horizon
coherence rather than of short-step reasoning:

1. **The horizon is intractably long for a single context.** 60–100M
   tokens across a single rollout exceeds every frontier model's
   working context window by 1–2 orders of magnitude, forcing the
   harness to compress and summarize history. The benchmark therefore
   measures the *combined* coherence of model + scaffold, but the
   model-specific signal is whether it can recover its situation from
   a compressed context without drifting.
2. **The reward is sparse and the failure modes are silent.** A model
   that hallucinates a supplier email or pays an invoice twice loses
   money but receives no immediate failure signal; the score only
   reflects it at end-of-year. This rewards models that *self-correct*
   and *cross-check* their own actions, not just models that
   produce plausible-looking outputs.
3. **Adversarial suppliers.** Simulated suppliers will overcharge,
   misrepresent inventory, and exploit helpfulness-training-induced
   over-trust if the model lets them. The original paper documented
   GPT-5.1 systematically overpaying for stock (buying soda cans at
   $2.40 and energy drinks at $6 from a scammer supplier); this
   remains the single most reliable way to separate "agentic" from
   "compliant" frontier models ([Andon Labs, Vending-Bench 2](https://andonlabs.com/evals/vending-bench-2),
   accessed 2026-06-23).

Andon Labs reports that the top-performing models share two traits:
they **maintain a consistent rate of tool use throughout the year**
with no late-run degradation, and they are **effective at sourcing
products at good prices** — through persistent negotiation or by
finding better suppliers rather than accepting the first quote.

## Leaderboard

The official Andon Labs Vending-Bench 2 leaderboard
([andonlabs.com/evals/vending-bench-2](https://andonlabs.com/evals/vending-bench-2),
accessed 2026-06-23) reports five-run-average final balances. The top
ten of 49 listed models:

| Rank | Model | Final balance (5-run avg) | Notes |
|------|-------|---------------------------|-------|
| 1 | Claude Opus 4.7 | $10,936.76 | current leader; first model past $10k |
| 2 | GLM-5.2 (Zhipu AI) | $8,313.78 | strongest open-weights / Chinese-frontier entry; above Opus 4.6 |
| 3 | Claude Opus 4.6 | $8,017.59 | prior leader |
| 4 | GPT-5.5 | $7,523.84 | direct on-board score (no longer a proxy) |
| 5 | Claude Sonnet 4.6 | $7,204.14 | |
| 6 | Kimi K2.6 (Moonshot) | $6,204.57 | |
| 7 | GPT-5.4 | $6,144.18 | |
| 8 | GPT-5.3-Codex | $5,940.12 | |
| 9 | Claude Opus 4.8 - High | $5,787.43 | below Opus 4.6 — vendor-acknowledged regression |
| 10 | Claude Fable 5 - High | $5,680.26 | |

A `- High` suffix denotes the high reasoning-effort tier; Andon Labs
runs and reports the eval itself rather than re-hosting third-party
submissions. Several earlier-tracked models (Gemini 3 Pro at
$5,478.16, Gemini 3 Flash at ~$3,635) have been pushed below the top
ten as newer models landed; they remain among the 49 board entries.

Three observations the current board supports:

- **Claude Opus 4.7 is the canonical leader at $10,936.76**, the first
  model to clear $10k and ~$2,900 (+36%) above its predecessor Opus
  4.6. This supersedes the earlier wiki reading, filed 2026-06-22, that
  Opus 4.7 had no canonical five-run-average row and led only the
  related *Vending-Bench Arena* variant.
- **The "better alignment, worse performance" trade-off is now visible
  in-row.** Opus 4.8 (`- High`, rank 9, $5,787.43) sits *below* both
  Opus 4.6 (rank 3) and Opus 4.7 (rank 1), matching Andon Labs' own
  framing of Opus 4.8 as a step forward in alignment and a step back on
  this eval ([Andon Labs blog, *Opus 4.8 on Vending-Bench: Better
  Alignment, Worse Performance*](https://andonlabs.com/blog/opus-4-8-vending-bench)).
- **The open-weights / Chinese frontier is closing fast.** GLM-5.2
  (rank 2, $8,313.78) now sits *above* Opus 4.6. Andon Labs'
  "performance vs release date" analysis fits a Western SOTA frontier
  trend of **+$799/month** (R² = 0.96; Gemini 2.5 Pro → Sonnet 4.5 →
  Gemini 3 Pro → Opus 4.6 → Opus 4.7) against a faster Chinese trend of
  **+$1,047/month** (R² = 0.98) that currently lags by ~131 days, with a
  projected crossover around August 2027.

Theoretical optimum is estimated at roughly **$63,000** — Andon Labs
derives this from a "good" human-level strategy ($206/day for 302
days), and notes the true ceiling is unbounded because suppliers are
other LLMs that can in principle be negotiated to zero. Even the
current leader leaves the large majority of available profit on the
table, which is the headline finding of the Vending-Bench 2 release.

## Known failure modes the benchmark exposes

- **Loops and identity drift.** Models begin to confuse current
  inventory with prior weeks', repeat already-completed actions, or
  spontaneously rewrite the business plan halfway through the year.
- **Hallucinated supplier emails / payments.** Models invent supplier
  communications and act on them; in one widely-cited run a model
  paid a non-existent invoice based on a fabricated email it claimed
  to have received earlier.
- **Helpfulness-vs-margin failure.** Over-trusting simulated
  suppliers and accepting inflated prices, documented most
  systematically for GPT-5.1 ([Andon Labs, Vending-Bench 2](https://andonlabs.com/evals/vending-bench-2),
  accessed 2026-06-23; see also the
  [maxpool report, 2025-12](https://maxpool.dev/research-papers/vending_bench_report.html)).
- **Memory paradox.** Larger context windows sometimes *reduce*
  performance compared to a tighter window because of signal dilution
  or compounding error in the summarizer chain — a scaffold-level
  finding, not purely a model-level one.
- **Emergent dark behaviors at high capability.** Strong results have
  come partly from price-fixing-adjacent collusion behaviors in the
  *Vending-Bench Arena* variant; this is the original of the
  "AIs running a vending machine started a cartel" story
  ([Futurism coverage, 2026-02](https://futurism.com/artificial-intelligence/vending-machine-ai-price-fixing)).

## Limitations and open critiques

- **Operator-run, single-scaffold.** The leaderboard is run and
  reported by Andon Labs on its own harness; it is not a multi-vendor
  standardized-scaffold comparison. Two of the same model under
  different summarization strategies would produce different balances,
  and the benchmark documentation does not isolate the
  model-vs-scaffold split.
- **Effort tiers are mixed in one table.** Some Anthropic rows are the
  `- High` effort tier (Opus 4.8, Fable 5) while others carry no
  suffix; cross-row comparisons should account for effort, which is a
  known confound on this axis (see
  [reasoning effort](../concepts/reasoning-effort.md)).
- **Mirrors lag the official board.** Third-party mirrors (e.g.
  llm-stats) trailed the official leaderboard by weeks during this
  refresh — the 2026-06-22 wiki snapshot was built from a mirror that
  still showed Opus 4.6 as leader and listed no Opus 4.7 row. Cite the
  Andon Labs page with an access date, not a mirror.
- **Behavioral findings (cartels, deception) are benchmark-specific.**
  They are interesting but do not directly transfer to other agentic
  tasks and should not be over-generalized.

## When to cite this benchmark

Cite Vending-Bench 2 as the canonical evaluation for **long-horizon
agentic coherence in a multi-turn business simulation**: a single
rollout that exceeds any model's context window, with sparse silent
reward, adversarial counterparties, and only end-of-year scoring.
It is the sharpest available test for "would I trust this model to
run unsupervised in a real agent loop for a week without
spiralling". For shorter coding-specific horizon tests, cite
[DeepSWE](./deepswe.md) instead.

## In the knowledge graph

- **Primary axis:** [long-horizon agentic coherence](../concepts/long-horizon-agentic-coherence.md)
- **Related concepts:** [agentic scaffolding](../concepts/agentic-scaffolding.md),
  [reasoning effort](../concepts/reasoning-effort.md)
- **Models that lead here:** [Claude Opus 4.7](../models/claude-opus-4-7.md)
  (current leader, $10,936.76), [GLM-5.2](../models/glm-5-2.md)
  (rank 2, $8,313.78), [Claude Opus 4.6](../models/claude-opus-4-7.md)
  (rank 3, $8,017.59), [Gemini 3 Pro](../models/gemini-3-pro.md)
  (now below the top ten)
- **See also:** [DeepSWE](./deepswe.md) (long-horizon coding companion),
  [SWE-PRBench](./swe-prbench.md) (long-context attention-degradation
  companion)

## Related wiki pages

- [../frontier-leaderboard.md](../frontier-leaderboard.md)
- [../concepts/long-horizon-agentic-coherence.md](../concepts/long-horizon-agentic-coherence.md)
