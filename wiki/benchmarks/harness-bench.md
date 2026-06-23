# Harness-Bench

> **Short name:** `harness-bench` · **arXiv:** [2605.27922](https://arxiv.org/abs/2605.27922) · **PDF:** [local](../../papers/harness-bench_2605.27922.pdf) · **Code:** [github.com/Qihoo360/harness-bench](https://github.com/Qihoo360/harness-bench) · **Website:** [harness-bench.ai](https://harness-bench.ai) · **Operator:** Peking University + Qiyuan Tech · **Released:** 2026-05-27 (arXiv v1)

**Authors:** Yilun Yao, Xinyu Tan, Chao-Hsuan Liu, Yaoming Li, Zhengyang Wang, Wenhan Yu, Zhewen Tan, Yuxuan Tian (Peking University); Guangxiang Zhao, Lin Sun, Xiangzheng Zhang, Tong Yang (Qiyuan Tech). *"Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows"*, arXiv preprint 2605.27922, May 2026.

## What it measures

Harness-Bench measures **how much of a deployed agent's score belongs
to the harness rather than to the base model**. The benchmark fixes
the task environment, budget, timeout, and evaluator across all runs
and varies two factors: the configurable *harness* (the system layer
that wraps the Large Language Model (LLM) — prompts, action formats,
tool interfaces, state policies, retry/recovery, permissions) and the
model backend. The headline number is the gap between the best and
worst harness on the same model-backend pool: **23.8 percentage points**
(NanoBot 76.2 vs OpenClaw 52.4 aggregate score; Table 2, page 6).

The benchmark sits primarily on the
[agentic-scaffolding](../concepts/agentic-scaffolding.md) concept axis of
this wiki — it is the canonical empirical evidence for the claim
that aggregate-leaderboard scores conflate model and scaffold
contributions. Through its "Long-running Autonomy & State Adaptation"
task category (11 of 106 tasks) and the introduced concept of
*execution alignment* (see below), it also contributes signal to the
[long-horizon agentic coherence](../concepts/long-horizon-agentic-coherence.md)
axis.

## Methodology

- **106 sandboxed offline tasks** across 8 workflow categories
  (Software Engineering & Codebase Maintenance: 22, Workspace,
  Tool Use & Multimodal Operations: 15, Data, BI & Finance
  Analytics: 14, Knowledge, Evidence & Retrieval: 13, Office &
  Business Communication: 12, Vertical Professional Workflows:
  12, Long-running Autonomy & State Adaptation: 11, SRE, DevOps
  & Release Ops: 7; Figure 2, page 4).
- Each task is **manually reviewed for four properties**: realism,
  solvability, oracle-checkability, and integrity (§3.2, page 4-5).
- **6 configurable harnesses × 8 API model backends** =
  5,088 trajectories in the main factorial matrix, plus 106
  trajectories for Codex (a model-bound coding-agent stack reported
  separately because it does not expose a swappable backend
  interface) = **5,194 total trajectories analyzed** (§4.1, page 6).
- Each task is paired with **an oracle or rubric** that checks the
  final workspace state and, when needed, the execution trace.
  LLM-based process rubrics use **claude-sonnet-4.6 as a fixed
  external judge** (§4.1, page 6) — a meta-relevant choice given
  that claude-opus-4.6 is among the evaluated backends.
- **Scoring** is intentionally conservative and multiplicative:
  - `TaskScore_i = Security_i · Completion_i · Process_i`
  - `Process_i = (Robustness_i + ToolUse_i + Consistency_i) / 3`
  - `Security_i ∈ {0, 1}` — a single permission violation zeros the
    score for that task.
  - All non-binary scores are normalized to [0, 1].

The harnesses and model backends, from Appendix B (pages 12–13):

| Harness | Design category | Source |
|---------|----------------|--------|
| OpenClaw | Long-running runtime | [OpenClaw 2026](https://github.com/openclaw/openclaw) |
| ZeroClaw | Long-running runtime | [ZeroClaw Labs 2026](https://github.com/zeroclaw-labs/zeroclaw) |
| Hermes | Long-running runtime, research-oriented memory/skills agent | [Nous Research 2026](https://github.com/NousResearch/hermes-agent) |
| Moltis | Secure local runtime, persistent self-hosted agent server | [Moltis 2026](https://github.com/moltis-org/moltis) |
| NullClaw | Lightweight runtime | [NullClaw 2026](https://github.com/nullclaw/nullclaw) |
| NanoBot | Lightweight agent runtime, ultra-lightweight personal AI agent | [HKUDS 2026](https://github.com/HKUDS/nanobot) |

Model backends in the factorial matrix: `anthropic/claude-opus-4.6`,
`anthropic/claude-sonnet-4.6`, `google/gemini-3.1-pro-preview`,
`qwen/qwen3.6-plus`, `z-ai/glm-5.1`, `moonshot/kimi-k2.5`,
`openai/gpt-5.4`, `deepseek/deepseek-v4-flash`.

## What makes it discriminative

Three design choices make Harness-Bench a sharp probe of the
scaffolding contribution that other agent benchmarks abstract away:

1. **Native execution behavior preserved per harness.** Rather than
   forcing every system into a common internal policy or runtime,
   Harness-Bench fixes the *external* conditions (task, budget,
   timeout, evaluator) and lets each harness run with its own
   native prompting, tool interface, state management, and recovery
   behavior (§3, page 3-4). This is the discriminating choice: the
   benchmark measures *configurations* rather than isolating
   individual scaffold mechanisms.
2. **Multiplicative scoring concentrates the gap.** Because
   `TaskScore = Security · Completion · Process`, a configuration
   needs all three to be high. A harness that completes the task
   but emits malformed JSON (process robustness ≈ 0) loses the
   task. This is more conservative than additive scoring and
   prevents harnesses from compensating for one weakness with
   another strength.
3. **Sandboxed offline tasks for reproducibility.** Tasks avoid
   dependence on live services to "reduce benchmark drift and make
   runs reproducible and independently scorable" (§3, page 3). The
   trade-off — explicitly named as a limitation by the authors — is
   loss of coverage of live-service behavior, changing external
   state, and long-term production memory.

## Leaderboard

### Aggregate harness ranking (averaged over 106 tasks × 8 backends)

Table 2, page 6:

| Rank | Harness | Score (%) | Completion (%) | Security (%) | ToolUse (%) | Consistency (%) | Robustness (%) | Median tokens (K) | Median turns |
|------|---------|-----------|----------------|--------------|-------------|-----------------|----------------|-------------------|--------------|
| 1 | NanoBot | **76.2** | 81.6 | 100.0 | 93.8 | 93.7 | 91.7 | 68.7 | 7.3 |
| 2 | Hermes | 71.2 | 80.4 | 100.0 | 88.5 | 88.4 | 85.5 | 139.7 | 22.6 |
| 3 | Moltis | 68.8 | 78.4 | 100.0 | 86.3 | 87.3 | 84.1 | 134.9 | 8.0 |
| 4 | NullClaw | 64.4 | 75.9 | 100.0 | 85.3 | 81.4 | 78.3 | 175.1 | 12.1 |
| 5 | ZeroClaw | 61.4 | 69.9 | 100.0 | 84.1 | 83.2 | 79.0 | 133.2 | 8.6 |
| 6 | OpenClaw | 52.4 | 60.0 | 100.0 | 79.5 | 74.0 | 70.9 | 82.1 | 5.0 |
| — | Codex (model-bound, not in factorial matrix) | 80.4 | 86.5 | 100.0 | 92.4 | 93.9 | 91.6 | 86.1 | 5.0 |

NanoBot achieves the top configurable-harness score while using
**fewer tokens** than Hermes, ZeroClaw, NullClaw, and Moltis — i.e.
longer trajectories alone do not determine performance (§4.2, page
7). Codex (specialized coding stack with `gpt-5.4` underneath) tops
the entire table at 80.4 but is reported separately because it does
not expose the same configurable model-backend interface as the
other six harnesses; the authors interpret it as a *practical
reference point*, not a controlled harness ablation.

### Model-backend dependence (Figure 3, page 7)

Figure 3 (left panel) plots each backend's *mean score across
harnesses* against its *cross-harness variance over the fixed task
suite*. The qualitative finding (text, §4.3, page 7):

- **Stronger backends tend to have higher mean scores AND lower
  cross-harness variance.** Strong models are "more tolerant of
  differences in prompting, tool interfaces, state management, and
  recovery behavior".
- **Weaker or less robust backends show larger variance across
  harnesses**, meaning their performance depends more on the
  surrounding execution substrate. The paper highlights two
  high-variance backends (`claude-opus-4.6` and `deepseek-v4-flash`)
  whose Harness-Bench position is *not* a clean rank because the
  rank depends heavily on which harness wraps them.

The wiki extracts a specific cross-wiki-axis observation from this
finding: `claude-opus-4.6` posts a strong [Vending-Bench 2](vending-bench-2.md)
score of $8,017.59 — rank 3 on the current board, and the leader at
the time Harness-Bench was run — on a single dedicated scaffold, yet
is *also* the highest-variance backend on Harness-Bench (multi-harness
factorial). Both can be true: Opus 4.6
is strong inside a well-tuned long-horizon scaffold and brittle
across arbitrary scaffold swaps. This is exactly the picture the
[agentic-scaffolding](../concepts/agentic-scaffolding.md) concept
page predicts.

### Top recurring failure symptoms (Table 3, page 8)

| Failure mode | Rate among failed trajectories | Typical manifestation |
|--------------|--------------------------------|-----------------------|
| Contract / format | 36.4% | Schema or output-contract violations, malformed JSON, missing ledger rows, incomplete manifests |
| Tool / recovery | 24.6% | Tool errors or blocked commands not followed by effective recovery or plan revision |
| Evidence / grounding | 14.6% | Incomplete source coverage, often with unsupported claims or missing verification on evidence-heavy tasks |
| Artifact commitment | 11.1% | Plausible reasoning without committing required outputs or workspace artifacts |
| State / continuation | 9.3% | Failure to preserve durable progress or resume reliably in interrupted or multi-round tasks |

### Category-level harness dependence (Figure 4, page 13)

Cross-harness variance is **not uniform across task types**:

| Category | Approximate cross-harness variance |
|----------|-----------------------------------:|
| Data, BI & Finance Analytics | ~0.0155 |
| Workspace, Tool Use & Multimodal Operations | ~0.0130 |
| Software Engineering & Codebase Maintenance | ~0.0102 |
| Knowledge, Evidence & Retrieval | ~0.0094 |
| Long-running Autonomy & State Adaptation | ~0.0091 |
| Vertical Professional Workflows | ~0.0056 |
| SRE, DevOps & Release Ops | ~0.0049 |
| Office & Business Communication | ~0.0002 |

Harness effects are largest where success depends on "structured
data manipulation, tool sequencing, workspace edits, and
intermediate-state tracking"; smallest on language-centric tasks
where prompt-to-output mapping dominates.

## Execution alignment — the concept Harness-Bench introduces

The paper introduces *execution alignment* as "the degree to which a
harness preserves correspondence among the agent's reasoning, the
observed workspace state, the actions taken through tools, and the
conditions checked by the evaluator" (§5.2, page 9). Failures are
framed as *execution drift*: "points where model reasoning becomes
weakly coupled to the files, tools, evidence, state, or output
contracts through which success is ultimately judged" (§5, page 8).

This is a more precise version of the
[long-horizon agentic coherence](../concepts/long-horizon-agentic-coherence.md)
axis's "identity drift" failure mode: the model has not lost identity
in any psychological sense, but its reasoning has decoupled from the
substrate the evaluator can see. Five of the seven Harness-Bench
failure symptoms above are direct instances of this decoupling.

The compact summary equation the paper offers (§3, page 4):

> Agent = Model + Harness

…matches the wiki's prior claim almost verbatim and provides the
first dedicated empirical benchmark backing it.

## Limitations and open critiques

- **Sandboxed offline only.** The authors explicitly limit coverage
  of "live services, user feedback, changing external state, and
  long-term production memory" (§6, page 9). This is the right
  trade-off for reproducibility but means Harness-Bench cannot
  substitute for live-deployment evaluations such as
  [Vending-Bench 2](vending-bench-2.md) on its primary axis.
- **LLM-as-judge dependency.** Process scores rely on
  claude-sonnet-4.6 as the fixed judge. With claude-opus-4.6 and
  claude-sonnet-4.6 themselves among the evaluated backends, the
  same-vendor judge-vs-subject concern applies. The authors do not
  report inter-judge agreement.
- **Six harnesses is a sample of a much larger space.** The 23.8-
  point gap is across these six specific configurations; whether a
  hypothetical "optimal" harness exists outside the sample, or how
  the variance behaves as the harness pool grows, is not addressed.
- **Codex reported separately.** The strongest aggregate score
  (80.4) belongs to a stack that does not fit the factorial design.
  Including it as a "practical reference point" leaves an
  apples-to-oranges flavor on the headline ranking.
- **No standardized scaffold parameter.** Comparing Harness-Bench
  rankings to [DeepSWE](deepswe.md)'s `[xhigh]`/`[max]` effort
  tiers or to [Vending-Bench 2](vending-bench-2.md)'s vendor-side
  submissions is approximate at best. The benchmark complements
  these rather than reconciling them.
- **Process-rubric weights are equal.** Robustness / ToolUse /
  Consistency are averaged with equal weight; whether this is the
  right decomposition for downstream deployment decisions is an
  open question.

## When to cite this benchmark

Cite Harness-Bench as the **canonical empirical reference for "agent
score depends on the harness, not only on the model"**. It is the
right citation when:

- The user is comparing two leaderboards that disagree on the same
  model and the explanation involves harness configuration —
  Harness-Bench supplies the 23.8-point gap and the variance-vs-
  mean picture to back up the claim.
- The user is interpreting a deployment regression after a harness
  swap (e.g. moving from a vendor-built scaffold to an open-source
  one) and wants benchmark-grounded expectations for the size of
  the regression.
- The user is arguing that "agent capability" should be reported at
  the *configuration* level rather than the model level — the
  paper's central recommendation.

For the *long-horizon* business-simulation regime that Harness-Bench
explicitly does not cover, cite [Vending-Bench 2](vending-bench-2.md).
For the long-context coding regime, cite [DeepSWE](deepswe.md).
For raw reasoning ceiling, cite [FrontierMath](frontiermath.md).

## In the knowledge graph

- **Primary axis:** [agentic scaffolding](../concepts/agentic-scaffolding.md)
  — Harness-Bench is the canonical empirical anchor for this
  concept; the concept page previously cited only anecdotal
  evidence (the Vending-Bench 2 "memory paradox" and SWE-PRBench's
  `config_A → config_C` curve) and now has a head-on benchmark.
- **Secondary axis:** [long-horizon agentic coherence](../concepts/long-horizon-agentic-coherence.md)
  — via the "Long-running Autonomy & State Adaptation" category
  and the "execution alignment" concept.
- **Related concepts:** [reasoning effort](../concepts/reasoning-effort.md)
  — Harness-Bench fixes budget and timeout per task but the
  prompting/action format that drives effective effort is part of
  the harness, so the two concepts compose.
- **Models that appear in the backend pool:**
  [Claude Opus 4.6 / 4.7](../models/claude-opus-4-7.md) (4.6
  explicitly evaluated; 4.7 is the in-wiki follow-up),
  [Gemini 3 Pro](../models/gemini-3-pro.md) (3.1-pro-preview),
  [the GLM-5 line](../models/glm-5-2.md). [GPT-5.5](../models/gpt-5-5.md)
  is one generation newer than the GPT-5.4 backend Harness-Bench
  tests; [Fable 5](../models/claude-fable-5.md) and Opus 4.8
  post-date the paper.
- **See also:** [Vending-Bench 2](vending-bench-2.md) (single-
  scaffold long-horizon companion),
  [SWE-PRBench](swe-prbench.md) (long-context attention companion
  whose `config_A → config_C` finding is the SWE-PRBench analog of
  Harness-Bench's harness-gap finding).

## Related wiki pages

- [../concepts/agentic-scaffolding.md](../concepts/agentic-scaffolding.md)
- [../concepts/long-horizon-agentic-coherence.md](../concepts/long-horizon-agentic-coherence.md)
- [../frontier-leaderboard.md](../frontier-leaderboard.md)
- [./benchmarks.md](./benchmarks.md)
