# CLAUDE.md — Schema for the LLM Frontier Wiki

This file is the working contract for a Claude Code (or equivalent) session
operating on this repository. Read it before touching anything. The generic
LLM-wiki pattern this schema instantiates is in
[llm-wiki.md](llm-wiki.md); that file describes the idea in the abstract.
This file is the project-specific conventions, templates, and workflows.

## Project identity

A research wiki on the **Large Language Model (LLM) frontier**: which
models currently sit at the top of the capability curve, how that
position is measured, and which axes of capability the benchmarks
actually probe. The wiki is built around two organizing axes that
the user finds most load-bearing for frontier model selection:

1. **Frontier reasoning** — the model's ceiling on long-form,
   research-level intellectual problems. The primary signal is
   *FrontierMath Tier 4 (v2)*; secondary signals are
   FrontierMath Tiers 1-3 and other "expert-only" reasoning evals.
2. **Long-horizon agentic coherence** — the model's ability to
   maintain coherent tool use, planning, and decision-making across
   thousands of agentic steps without identity drift, looping, or
   silent failure. The primary signal is *Vending-Bench 2* (1-year
   vending-machine business simulation, 60–100M tokens per run);
   secondary signals are *DeepSWE* (long-horizon coding, 7-file
   solutions from short prompts) and *SWE-PRBench* (long-context
   code review).

The reader is an engineer or researcher choosing a frontier model for
a specific job and wanting to know: "which model leads on the axis
that matters for this job, and what is the evidence?" The wiki names
the axes, points at the benchmarks that probe each one, and keeps a
running 2D leaderboard at [`wiki/frontier-leaderboard.md`](wiki/frontier-leaderboard.md).

## Architecture

Three layers. Each has a distinct lifetime and ownership discipline.

- **`papers/`** — raw source layer. Cached benchmark pages, papers,
  system cards, and result dumps. Treated as immutable references.
  Named descriptively (`vending-bench-2_andonlabs_2026-06.html`,
  `frontiermath_tier-4-v2_epoch_2026-06.html`, ...). New ingests
  go here first. If a source is a live web leaderboard with no stable
  PDF, cite the URL and access date in the leaf instead and skip the
  local snapshot.
- **`wiki/`** — the wiki proper. LLM-owned markdown. Every numeric
  claim cites a benchmark page, paper section, or system card; every
  cross-cutting claim links to another wiki page. This layer is where
  all the work happens.
- **`CLAUDE.md`** (this file) — schema / conventions / workflows.
  Co-evolves with the wiki; update it whenever a convention changes.

## Top-level layout

```
llm-frontier-wiki/
├── CLAUDE.md                   (this file — schema)
├── llm-wiki.md                 (reference copy of the generic pattern)
├── README.md                   (repo landing page)
├── papers/                     (immutable source snapshots)
└── wiki/
    ├── overview.md             (orientation and reading paths)
    ├── index.md                (flat catalog of every wiki page)
    ├── log.md                  (chronological append-only log)
    ├── frontier-leaderboard.md (the 2D ranking page — live root chart)
    ├── concepts/
    │   ├── concepts.md         (section hub)
    │   ├── frontier-reasoning.md
    │   ├── long-horizon-agentic-coherence.md
    │   ├── reasoning-effort.md
    │   └── agentic-scaffolding.md
    ├── benchmarks/
    │   ├── benchmarks.md       (section hub)
    │   ├── vending-bench-2.md
    │   ├── deepswe.md
    │   ├── frontiermath.md
    │   └── swe-prbench.md
    └── models/
        ├── models.md           (section hub)
        └── <slug>.md           (one per frontier model tracked)
```

**Naming convention (folder-note pattern):** there is exactly ONE
`README.md` in the entire repo, at the root. Every wiki section uses
a folder-note named after the section itself (`concepts.md`,
`benchmarks.md`, `models.md`) as its hub. The wiki's own hub is
`overview.md`. The 2D leaderboard lives at the wiki root because it
is the single artifact most readers come here to see; everything
else is supporting structure.

## Page types and templates

Every page belongs to one of the types below. Use the template literally
when creating or rewriting. Do not invent new page types without updating
this file first.

### 1. Benchmark leaf — `wiki/benchmarks/<slug>.md`

One per benchmark. Slug is the lowercase hyphen-separated short name
(`vending-bench-2`, `deepswe`, `frontiermath`, `swe-prbench`).
Target length 600–1200 words. **A leaf is a faithful technical mirror
of the benchmark's substantive content** — every methodology choice
the benchmark documents (task construction, judge model, scoring
function, harness configuration, what specifically makes the eval
distinguish strong from weak models on the intended axis) belongs on
the leaf, not just the score table.

```markdown
# <Full Benchmark Name>

> **Short name:** `<slug>` · **URL:** <canonical URL> · **Operator:** <org> · **Latest version:** <date or version>

## What it measures
(One paragraph — the underlying capability the benchmark targets, and
which of the two wiki axes (frontier reasoning vs long-horizon agentic
coherence) it primarily probes. If it probes both, say so and explain
the split.)

## Methodology
(Task construction, sample size, harness, evaluator/judge, scoring
function. If the benchmark uses an LLM-as-judge, name the judge and
its agreement rate with humans where reported.)

## What makes it discriminative
(Why does this benchmark separate strong from weak models, and how is
it engineered to resist contamination / memorization / shortcut
exploitation? This is the "design rationale" section — quote the
methodology page or paper where it explains its own choices.)

## Leaderboard
(Markdown table with every model and its score, confidence interval
where reported, and the *date* the score was filed. Cite the URL.)

## Known failure modes the benchmark exposes
(What does the benchmark catch that lower-tier benchmarks miss? E.g.
identity drift in long-horizon, code-review false-positive rate,
research-math arithmetic mistakes, etc.)

## Limitations and open critiques
- at least 3 bullets — sample size, judge bias, contamination risk,
  selection bias in which models submitted, etc.

## When to cite this benchmark
(2-3 sentences: what specific capability claim is this the canonical
reference for, so a reader knows when to pick this vs a successor or
companion benchmark.)

## In the knowledge graph
- **Primary axis:** [<axis-page>](../concepts/<axis>.md)
- **Related concepts:** [<page>](../concepts/<page>.md), ...
- **Models that lead here:** [<model>](../models/<slug>.md), ...
- **See also:** [<other benchmark>](./<other>.md)
```

### 2. Concept page — `wiki/concepts/<slug>.md`

A cross-cutting idea that connects benchmarks and models — most
critically the two organizing axes (`frontier-reasoning`,
`long-horizon-agentic-coherence`), plus supporting concepts
(`reasoning-effort`, `agentic-scaffolding`). Target length 600–1000
words.

```markdown
# <Concept Name>

<1-2 sentence definition.>

## Intuition
(What this concept is and why the wiki is organized around it.)

## How it is measured
(Concrete benchmarks that probe it, and *what specifically about the
benchmark design* makes it a measure of this concept rather than of
something else.)

## Why it is a useful axis
(What does separating along this axis let you predict that
aggregate-score leaderboards do not?)

## Trade-offs and failure modes
(Where the concept is fuzzy, where benchmarks under-measure it,
known confounds with reasoning effort, scaffolding, or harness
quality.)

## Models that exemplify high / low values on this axis
- [<model>](../models/<slug>.md) — 1-line note on its score on the
  primary benchmark for this axis.

## Open questions
- 3-5 real open questions about how to measure or define this axis.

## Related wiki pages
- [<page>](../concepts/<other>.md)
- [<benchmark>](../benchmarks/<slug>.md)
```

### 3. Model leaf — `wiki/models/<slug>.md`

One per frontier model the wiki tracks. Slug is the lowercase
hyphenated model identifier (`claude-fable-5`, `claude-opus-4-7`,
`gpt-5-5`, `glm-5-1`, `gemini-3-pro`). Target length 400–800 words.

```markdown
# <Full Model Name>

> **Short name:** `<slug>` · **Vendor:** <org> · **Released:** <YYYY-MM>

## What it is
(One paragraph — model class, distinguishing claim, scaffolds /
effort tiers the vendor exposes.)

## Scores on tracked benchmarks
(Markdown table with one row per benchmark in the wiki and the
model's score, with date and source link.)

## Where this model sits on the axes
- **Frontier reasoning:** <position vs others, with the benchmark
  number that supports it>
- **Long-horizon agentic coherence:** <position vs others, with the
  benchmark number that supports it>

## When to pick this model
(2-3 sentences: which kind of task this model is the right call for
based on the axes above.)

## Known caveats
- bullets on alignment-vs-performance trade-offs, scaffolding
  sensitivity, missing benchmark coverage, etc.

## Related wiki pages
- [frontier-leaderboard.md](../frontier-leaderboard.md)
- [<benchmark>](../benchmarks/<slug>.md), ...
```

### 4. Section hub (folder note) — `wiki/<section>/<section>.md`

Each wiki section has a hub page named after the section itself:
`concepts/concepts.md`, `benchmarks/benchmarks.md`,
`models/models.md`. One-paragraph orientation plus a bullet list with
a one-line gloss per sub-page. Target 120–180 words.

### 5. Wiki root files

- `wiki/overview.md` — entry point, the "story" of why the wiki is
  organized around the two axes, reading paths.
- `wiki/index.md` — flat catalog of every wiki page, one line each.
  First stop at query time. Must be kept in sync with every add /
  rename / delete.
- `wiki/log.md` — chronological append-only record.
- `wiki/frontier-leaderboard.md` — the 2D ranking artifact: a table
  and an ASCII chart positioning every tracked model on (reasoning
  axis, long-horizon axis). This is the page that gives the wiki its
  reason to exist; it must be regenerated whenever a new score lands.

## Style rules

- **Acronyms spelled out on first use per page**, with the short
  form in parentheses: "Large Language Model (LLM)", "Long-Horizon
  Agentic Coherence (LHAC)", "Frontier Math Tier 4 (FM4)". Established
  proper-name acronyms (GPT, GLM, Gemini, Claude, NEAT, RL, RLHF) are
  used as-is.
- **Cite benchmarks with their full name and operator on first use**:
  "*Vending-Bench 2* (Andon Labs, 2026-06)". The user finds opaque
  filenames or bare short names actively unhelpful.
- **No emojis.** Anywhere.
- **No fabricated numbers.** Every numeric claim cites a benchmark
  page, paper section, or model system card with an access date.
  Where a value is not disclosed, write "not disclosed" or "not on
  public leaderboard" and say so in a caveat.
- **No marketing language.** No "revolutionary", "game-changing",
  "state-of-the-art" without citation.
- **Relative links for internal navigation.** Never absolute URLs to
  other wiki pages.
- **First occurrence of a benchmark short name in prose is linked to
  its leaf** (`[Vending-Bench 2](../benchmarks/vending-bench-2.md)`).
  Subsequent occurrences are plain text. Same for model names and
  concept names.
- **Every page ends with a "Related wiki pages" section** with ≥2
  cross-links.
- **Score tables include score + confidence interval where reported
  + date filed + source link.** A bare number with no provenance is
  not enough.
- **Research tone.** Direct, qualified, willing to write "disputed",
  "not yet on the public leaderboard", "self-reported", "vendor
  scaffold vs standardized scaffold".
- **ATX headings** (`##`), not setext. Title case for H1, sentence
  case for H2+ by default.
- **American English spelling**, Oxford commas OK.

## Cross-link discipline

- Concept → concept: ≥1
- Concept → benchmark: ≥1
- Benchmark → concept (primary axis): exactly 1
- Benchmark → models that lead it: ≥1
- Model → benchmarks scored on: ≥1
- Model → concepts (axis positions): ≥1
- The 2D leaderboard links to every tracked model and every primary
  benchmark by relative path.
- Broken relative links are a lint failure. Fix on sight.
- When you rename or delete a page, grep for inbound links and update
  them in the same commit.

## Workflows

### Ingest: adding a new benchmark

1. Cache the benchmark page or paper in `papers/` if a stable file
   exists. If the source is a live leaderboard with no PDF, skip the
   local snapshot and cite URL + access date instead.
2. Read the methodology page: what it measures, how the score is
   computed, judge model, sample size, harness.
3. Create leaf at `wiki/benchmarks/<slug>.md` using the benchmark-leaf
   template.
4. Update `wiki/benchmarks/benchmarks.md` index.
5. Update the relevant axis concept page to list this benchmark as a
   primary or secondary signal.
6. Update `wiki/frontier-leaderboard.md` with any new model scores
   the benchmark reveals.
7. Update `wiki/index.md` with the new leaf.
8. Append to `wiki/log.md`:
   `## [YYYY-MM-DD] ingest | <benchmark short name>` + 2-3 sentences.

### Ingest: adding a new model

1. Read the vendor's system card and any independent benchmark
   evaluations.
2. Create leaf at `wiki/models/<slug>.md` using the model-leaf
   template; fill the scores table from the benchmark leaves.
3. Update `wiki/models/models.md` index.
4. Update `wiki/frontier-leaderboard.md` with the new model's
   position on both axes.
5. Update `wiki/index.md`.
6. Append to `wiki/log.md`.

### Query: answering a user question

1. First stop: `wiki/frontier-leaderboard.md` for "which model
   leads on X". Otherwise `wiki/index.md`.
2. If the user asks for a recommendation, walk through the relevant
   axis concept page, then the benchmark leaf that supports the
   claim, then the model leaf.
3. **If the answer is non-trivial and generally useful**, file it
   back as a new concept page or update the leaderboard. Append to
   `wiki/log.md`.

### Lint: periodic health check

- **Stale leaderboard rows** — every row on
  `wiki/frontier-leaderboard.md` should have a "filed on YYYY-MM-DD"
  marker; flag anything more than 6 months old without a fresh
  re-check.
- **Orphan pages** — pages with zero inbound links.
- **Broken relative links** — every `../x.md` must resolve.
- **Template compliance** — benchmark leaves missing methodology or
  leaderboard sections, model leaves missing axis positions.
- **Unattributed numbers** — every `%`, `$`, or score value in prose
  must have a citation.
- **Vendor-scaffold confusion** — flag any leaderboard row that does
  not disclose whether it is the vendor's own scaffold or a
  standardized scaffold (this is the single most common source of
  apparent contradictions between leaderboards).
- Append `## [YYYY-MM-DD] lint | <summary>` to `wiki/log.md`.

## Anti-patterns (do NOT do these)

- Do not fabricate scores, model rankings, or URLs.
- Do not write a number on the leaderboard without a citation.
- Do not add emojis.
- Do not create marketing-tone prose.
- Do not mix vendor-reported scores with standardized-scaffold scores
  in the same row of the leaderboard; they are not comparable.
- Do not write to `papers/` — that layer is immutable.
- Do not use absolute URLs for internal wiki navigation.
- Do not leave a page without a "Related wiki pages" block.
- Do not edit `llm-wiki.md` as part of routine ingest, query-filed-back,
  or lint work; it is the reference copy of the generic pattern.
- Do not amend an already-pushed commit.
- Do not commit directly to `main`. Use feature branches and pull
  requests, one focused change per branch.

## Getting started in a new session

1. Read this file.
2. Read `wiki/frontier-leaderboard.md` to see the current 2D state.
3. Read `wiki/index.md` to see what exists.
4. Read `wiki/log.md` tail to see what was done recently.
5. Do the work.
6. Update `wiki/index.md`, the leaderboard, and `wiki/log.md` before
   committing.
