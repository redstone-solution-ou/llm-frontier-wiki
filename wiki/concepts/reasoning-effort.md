# Reasoning Effort

Vendor-exposed knobs that control how much internal reasoning a
Large Language Model (LLM) does before emitting a final answer.
The leaderboards this wiki tracks are not score tables of
"models"; they are score tables of **(model, effort)** pairs. The
effort tier is part of the row, and ignoring it produces
apparent contradictions between leaderboards that are actually
agreements once effort is matched.

## Intuition

Frontier vendors expose reasoning effort under different names:

- **OpenAI:** `low`, `medium`, `high`, `xhigh` (extra-high).
- **Anthropic Claude:** Reasoning effort levels including
  `low`, `medium`, `high`, `xhigh`, `max`, plus a "fast mode"
  toggle on top.
- **Zhipu AI / GLM:** Per-call thinking budget.
- **Google Gemini:** Pro / Flash split is partly a capability
  split and partly a budget split.

A model called at a higher effort spends more wall-clock and more
output tokens on internal chain-of-thought, self-consistency, or
search before answering. On hard problems (especially
[frontier reasoning](frontier-reasoning.md) problems on
FrontierMath Tier 4), the gap between effort tiers is often
larger than the gap between models at the same tier.

## How effort appears in the leaderboards

Three illustrative cases the wiki tracks:

- On [FrontierMath Tier 4 (v2)](../benchmarks/frontiermath.md),
  the top-five entries are annotated:
  Fable 5 `[max]`, GPT-5.5 Pro `[xhigh]`, GPT-5.5 `[xhigh]`. The
  effort tier is part of every row; a default-effort run of any
  of these models would score lower.
- On [DeepSWE](../benchmarks/deepswe.md), every leaderboard entry
  also carries an effort tier (`GPT-5.5 [xhigh]`, `Opus 4.8
  [max]`, `Sonnet 4.6 [high]`). DeepSWE additionally publishes
  median output tokens and wall-clock per model, which makes the
  effort dimension partially comparable across vendors.
- On [Vending-Bench 2](../benchmarks/vending-bench-2.md), effort
  tier is *not* directly disclosed on the public leaderboard —
  every run is a year-long simulation and the implied effort
  budget is "as much as the vendor / submitter chose to spend".
  This is one reason cross-leaderboard rankings on Vending-Bench
  appear inconsistent with rankings on DeepSWE: effort is
  controlled differently.

## Why it matters

- **A model can win a benchmark at a high effort tier and lose at
  a lower one**, sometimes by 20+ points. Aggregate scoreboards
  that report only the highest-effort number make every model
  look stronger than the deployment configuration the user
  actually picks.
- **Effort is the dominant cost driver.** A `[max]`-effort run of
  a frontier model can cost 5–20× more (wall-clock and dollars)
  than a default run. Production deployments rarely run at the
  effort tier shown on the leaderboard.
- **Effort tiers are not standardized across vendors.** OpenAI's
  `xhigh` and Anthropic's `max` are roughly comparable in
  *intent* but not necessarily in token budget. Comparing them
  row-by-row on a leaderboard requires noting that the
  comparison is approximate, not exact.

## Trade-offs and failure modes

- **Effort saturates.** Past a certain budget on most problems,
  additional effort does not improve accuracy; the curve is
  concave.
- **Effort interacts badly with long-horizon coherence.** Higher
  effort per step on Vending-Bench 2 means more tokens per
  decision means harder summarization, which can *reduce* the
  final balance via the "memory paradox" reported in the
  benchmark documentation. High effort is not always the right
  call on the coherence axis.
- **Effort is not a fungible substitute for capability.** GPT-5.4
  at `[xhigh]` does not match Fable 5 at `[max]` on Tier 4;
  effort is a multiplier on capability, not a replacement for
  it.

## Related wiki pages

- [frontier-reasoning.md](frontier-reasoning.md) — effort is the
  single largest visible knob on this axis.
- [long-horizon-agentic-coherence.md](long-horizon-agentic-coherence.md)
  — effort interacts non-monotonically here.
- [agentic-scaffolding.md](agentic-scaffolding.md) — both effort
  tiers and scaffolding are jointly controlled, often by different
  parties.
- [../frontier-leaderboard.md](../frontier-leaderboard.md)
