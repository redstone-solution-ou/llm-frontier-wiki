# SWE-PRBench

> **Short name:** `swe-prbench` · **arXiv:** [2603.26130](https://arxiv.org/abs/2603.26130) · **Dataset:** [foundry-ai/swe-prbench](https://huggingface.co/datasets/foundry-ai/swe-prbench) · **Blog:** [foundryhq.ai/blog](https://foundryhq.ai/blog/swe-prbench-benchmarking-ai-code-review-quality) · **Operator:** Foundry AI · **Version:** v0.4.1 (pipeline)

## What it measures

SWE-PRBench evaluates **Artificial Intelligence (AI) code review
quality**: whether a Large Language Model (LLM) can identify the same
issues in a pull request that a real human reviewer flagged in
production code. The task is intentionally different from code
generation — there is no pass/fail test suite and no single correct
answer; success is operationalized as agreement with the union of
human reviewers' substantive review comments on the same diff.

The benchmark sits across both wiki axes: the
[frontier reasoning](../concepts/frontier-reasoning.md) axis is
implicated because identifying a real-but-subtle bug is a reasoning
problem, but the wiki's primary placement is on the
[long-horizon agentic coherence](../concepts/long-horizon-agentic-coherence.md)
axis because SWE-PRBench's signature finding is *attention
degradation with growing context length*: every model's detection
rate drops monotonically as the context expands from a bare diff to
diff-plus-file to full repository. That curve is the headline
contribution of the paper.

## Methodology

- **350 pull requests** with human-annotated ground truth, drawn from
  700 candidate repositories filtered by a Repository Quality Score
  ([SWE-PRBench arXiv:2603.26130, 2026-03](https://arxiv.org/abs/2603.26130)).
- **Three frozen context configurations** per task:
  - `config_A` (diff only)
  - `config_B` (diff + content of changed files)
  - `config_C` (diff + full repository context)
- **Three difficulty types** based on where the review-flagged issue
  lives:
  - **Type1_Direct** — the issue is on lines inside the diff hunk.
  - **Type2_Contextual** — the issue references unchanged code in
    the same file as the diff, or how the changed code interacts
    with existing code.
  - **Type3_Latent_Candidate** — the issue lives in a file *not* in
    the diff, requiring cross-file reasoning.
- **LLM-as-judge** with the agent–human-rubric agreement validated at
  Cohen's kappa = 0.75 ([SWE-PRBench paper](https://arxiv.org/abs/2603.26130)).
  Judge model in the published leaderboard is GPT-5.2 ([SWE-PRBench
  repository README](https://github.com/FoundryHQ-AI/swe-prbench)).
- **Three-bucket classification per agent comment:**
  - `CONFIRMED` — agent identifies the same underlying issue as a
    human reviewer.
  - `PLAUSIBLE` — comment is correct about the code but not raised by
    any human reviewer in the ground-truth set.
  - `FABRICATED` — comment references nonexistent code or makes
    factually wrong claims.
- The primary metric is a difficulty-weighted mean score `s̄` over
  the eval-100 split, combining the *detection rate of agent
  comments matching ground truth* (`DR_A`) and the *false-positive
  rate* of fabricated comments (`FPR`).

## What makes it discriminative

Three design choices make SWE-PRBench a sharper test of long-context
code understanding than a generation benchmark:

1. **It does not reward style or syntactic plausibility.** A
   well-formatted plausible-looking comment that names a nonexistent
   bug is graded `FABRICATED` and penalized. This is the opposite of
   code-generation benchmarks where syntactically valid pattern-
   matched output often scores well.
2. **The diff-only-versus-full-context comparison isolates
   attention.** The paper finds that "all 8 models degrade
   monotonically from config_A to config_C" — every model gets *worse*
   at finding the same bugs when given more context. The benchmark
   thereby separates "model genuinely uses long context" from "model
   nominally accepts long context but attends to it badly".
3. **Type3 (latent) issues require cross-file reasoning that no diff
   summarization can shortcut.** A model that scores well on
   Type3 is doing something the bare-diff benchmarks cannot
   measure.

## Leaderboard

Paper baseline leaderboard on the `eval_100` split, with judge model
**GPT-5.2** and pipeline version **v0.4.1** ([SWE-PRBench README](https://github.com/FoundryHQ-AI/swe-prbench)):

| Rank | Model | Overall (s̄) | DR_A | FPR | Filed |
|------|-------|-------------|------|-----|-------|
| 1 | Claude Haiku 4.5 | 0.153 | 0.306 | 0.346 | 2026-03 |
| 2 | Claude Sonnet 4.6 | 0.152 | 0.297 | 0.227 | 2026-03 |
| 3 | DeepSeek V3 | 0.150 | 0.312 | 0.315 | 2026-03 |
| 4 | Mistral Large 3 | 0.147 | 0.305 | 0.353 | 2026-03 |
| 5 | GPT-4o | 0.113 | 0.220 | 0.193 | 2026-03 |
| 6 | GPT-4o-mini | 0.108 | 0.210 | 0.353 | 2026-03 |
| 7 | Mistral Small | 0.106 | 0.257 | 0.251 | 2026-03 |
| 8 | Llama 3.3 70B | 0.079 | 0.223 | 0.417 | 2026-03 |

The headline result is sobering: **no model detects more than 31% of
human-flagged issues** on any configuration, and the **mean detection
rate across all 8 models is approximately 26%** ([SWE-PRBench arXiv
abstract](https://arxiv.org/abs/2603.26130)). The top four entries
(Haiku, Sonnet, DeepSeek, Mistral Large) are not statistically
distinguishable from each other; the rank-4 / rank-5 gap *is*
statistically significant.

A separate fork of the harness — the local Claude Code CLI
experiment, [present in `/Users/jeremycochoy/Desktop/workspace/swe-prbench`](https://github.com/<org>/swe-prbench-harness)
— evaluates four Opus 4.7/4.8 reasoning-effort tiers with Sonnet 4.6
as judge. Those results are not in the paper baseline and should be
quoted with the explicit caveat that the judge model is different.

## Known failure modes the benchmark exposes

- **Attention dilution with long context.** Every model degrades from
  `config_A` to `config_C`. A **structured 2,000-token diff-with-summary
  prompt outperforms a 2,500-token full-context prompt** across all
  models — i.e. the long-context degradation is not about content
  scarcity but about *attention allocation*.
- **Fabrication on irrelevant code.** Models with high `FPR` (Llama
  3.3 70B at 0.417) generate plausible-sounding comments on lines
  that have no defect.
- **False confidence on Type1.** Models pattern-match diff lines as
  obvious bug sites and over-flag them; Type2 (contextual) and Type3
  (latent) issues are systematically under-flagged.
- **Catastrophic ranking inversion vs generation benchmarks.**
  Claude Haiku 4.5, which is mid-tier on generation benchmarks, leads
  the SWE-PRBench leaderboard. This is the cleanest available
  demonstration that **code review is a different evaluation regime
  from code generation**.

## Limitations and open critiques

- **Older model selection.** The paper baseline evaluates GPT-4o and
  Llama 3.3 70B, which are by 2026-06 standards no longer frontier.
  Frontier models (Opus 4.7/4.8, Fable 5, GPT-5.5) are not in the
  published paper baseline; their numbers exist only in
  vendor / fork-specific runs and are not directly comparable.
- **LLM-as-judge.** Cohen's kappa with humans is 0.75, which is
  good for kappa but still admits non-trivial judge noise; the
  rank-1 vs rank-4 gap is within plausible judge-noise range.
- **350-PR sample, 100-PR eval split.** Confidence intervals on the
  point scores are not separately published; rank-order claims at
  the top of the table should be treated as approximate.
- **Domain coverage.** PRs are drawn from open-source repositories
  passing the Repository Quality Score filter; closed-source / large-
  internal-codebase review behavior may differ.
- **Detection rate is bounded above by ground-truth selection.** Any
  agent comment that a human reviewer *should* have flagged but did
  not is counted against the agent as `PLAUSIBLE` rather than
  `CONFIRMED`. This systematically under-credits agent
  comprehensiveness.

## When to cite this benchmark

Cite SWE-PRBench as the canonical reference for **AI code review
quality** and for the **long-context attention-degradation effect**.
The latter — the monotone degradation from `config_A` to `config_C`
across every model — is the single most useful result to cite when
arguing that nominal context windows misrepresent effective context
windows. For code *generation* under similar long-context conditions,
cite [DeepSWE](./deepswe.md) instead.

## In the knowledge graph

- **Primary axis:** [long-horizon agentic coherence](../concepts/long-horizon-agentic-coherence.md)
  (attention-allocation sub-axis); secondary signal on
  [frontier reasoning](../concepts/frontier-reasoning.md) for the
  defect-identification component
- **Related concepts:** [agentic scaffolding](../concepts/agentic-scaffolding.md)
  (context construction is half the score), [reasoning effort](../concepts/reasoning-effort.md)
- **Models that lead here:** [Claude Haiku 4.5 / Sonnet 4.6](../models/models.md)
  (paper baseline; frontier models have side-channel data only)
- **See also:** [DeepSWE](./deepswe.md) (long-context coding companion),
  [Vending-Bench 2](./vending-bench-2.md) (broader long-horizon
  agent-coherence companion)

## Related wiki pages

- [../frontier-leaderboard.md](../frontier-leaderboard.md)
- [../concepts/long-horizon-agentic-coherence.md](../concepts/long-horizon-agentic-coherence.md)
