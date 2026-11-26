# Prompts taxonomy: scope

**In one line**: the vocabulary for `jburnhams/prompts` (agents, harnesses, models, tools
and MCP, context, control, evals), built in stages because the domain is too large for
one pass: first the core words and one question that splits the repo into areas, then
one area at a time.

**In plain words**: the prompts repo compares how dozens of AI agent products work and
designs Jonathan's own (Keel, Forge, Lens). It uses the same word for different things:
"agent" is a product in one doc and one model context inside a run in another; "mode"
means at least four things. This folder fixes one word per idea, starting with the
thirty or forty words every doc uses, and a few questions that sort every mechanism the
repo describes, so research passes, design docs and the agents that write them say the
same thing the same way.

Built with the method in [`design/process.md`](../../design/process.md) (version 1) and
[`design/spec.md`](../../design/spec.md), with the large-domain changes proposed in
[`design/method-v1.1.md`](../../design/method-v1.1.md) (M1-M6, not yet adopted).

- **Context**: [`jburnhams/prompts`](https://github.com/jburnhams/prompts): the research
  docs at the root, the per-source folders' READMEs, and the designs in `agent-design/`
  (Keel, Forge, Lens). Short context name: `prompts`.
- **Purpose**: to name the concepts of agent design once, and sort every mechanism the
  repo describes by the questions a research pass or a design doc asks of it: which
  part of an agent system it belongs to, who makes the call, and when it acts.
- **Readers**, in priority order (◆ J9, recommendation followed): Jonathan first; then
  the agents that run the weekly research passes and write the design docs. Where they
  conflict, Jonathan's reading wins.
- **Owner**: Jonathan. Agents approve changes that pass T1-T6 with a logged reason;
  Jonathan reviews [`changelog.md`](./changelog.md) and can veto (J8, spec G1).
- **Status**: `draft`, 2026-11-26. Stage 1 (kernel and areas) in progress.

## Stages (proposal M1)

The domain is about 815,000 words in 281 files. One pass over all of it would give a
glossary of hundreds of terms tested on 30 items, too few to show whether any one of
them works. So it is built in stages, each a full run of process steps 2-10 with its own
samples and rounds, inside this one context (one meaning per word across all stages).

| Stage | Covers | Facets | Status |
|---|---|---|---|
| 1. Kernel | the 30-40 words every area uses (agent, harness, model, run, turn, tool, MCP server, skill, sub-agent, context file, approval, eval, ...) and the split into areas | `area`, `decider`, `moment` (proposed) | samples drawn; facets await Jonathan |
| 2. First area | `context` or `control`, the two areas the repo's `changelog.md` mentions most (context and memory docs 79 times; permission, risk, recovery and steering docs 59; tool docs 45) | that area's own facets, such as channel or risk dimension | not started |
| 3+. Other areas | one at a time, in the order the repo's work reaches them (J10) | per area | not started |

A later stage may sort *sources* (harnesses, SDKs, products, protocols) as a second kind
of item, with `agent-archetypes.md` as its starting point. Stage 1 sorts mechanisms only.

## Competency questions (stage 1)

Answered from `facets.md` and `glossary.md` alone (T10).

1. Which mechanisms run with no person deciding, and which need a person's answer?
2. Which checks are made by a second model rather than by fixed rules?
3. Which area does a new research finding belong to, and so which doc should it go in?
4. Which mechanisms act on each tool call, and which only once per run?
5. What does "agent" mean in this repo, and which words are used for the other senses?
6. Which mechanisms act when something fails, and which at the end of a run?
7. What is the difference between a harness, an SDK and a model provider?
8. What is the difference between a run, a session, a turn and a transcript?
9. What is the difference between a sub-agent, a worker, a fork and a delegated run?
10. What do "mode", "surface" and "artifact" each mean, and which word is used for each other sense?
11. What is the difference between a judge, a monitor, a classifier, a grader and a reviewer?
12. What is the difference between an eval, a benchmark and self-verification?
13. What is an MCP server, an MCP App, a skill, a plugin and a connector, and how do they differ?

## Out of scope

- **Stored prompts and source code**: `leaked/`, `skills/` and each source folder's
  stored files keep their authors' words. The glossary records them as aliases where
  they name one of our concepts (Claude Code's `subagent_type`, Codex's "Guardian").
- **Tool and schema identifiers** in Keel's JSON schemas (`RunSpec`, `HandOff`,
  `Complete`): code names, governed by the schemas. Concepts they share are linked from
  the glossary entry, not renamed.
- **Interface design vocabulary**: the `ux` context (`domains/ux/`).
- **Vendor and product names** (Claude Code, Codex, Goose): proper names, given entries
  only where the repo uses one as a concept (for example "Code Mode").

## Neighbours

- **ux** (`domains/ux/`, in use): known overlap "surface" (`ux:surface` is a tonal layer;
  here "tool surface"), "skill" (`ux` means only the `ux-design` skill), "agent". A
  `map.md` is written in stage 1, `closeMatch` by default (spec C3).
- **Keel's own taxonomy** (`agent-design/keel/taxonomy.md`): not a separate context but
  the seed for this one (harvest, "Existing vocabularies"). Its entries are reused where
  they agree with the research docs' usage; where they differ (agent), J14 decides.

## Ending conditions (each stage)

Adopt a stage (process step 10) when all of these hold on the same round:

- T1-T6 clean.
- T7: every item in a fresh sample of 60 gets a value in every facet, or goes to
  **Unsorted** with a note, and **Unsorted** holds at most 4 items (about 7%, as in ux).
- T8 (proposal M4): Fleiss' κ ≥ 0.6 on every facet across three raters from three model
  families, and Cohen's κ ≥ 0.6 on every facet between the two non-Claude raters.
- T9: a fresh reader guesses at least 80% of the stage's preferred labels right.
- T10: every competency question above is answered, with the answer in `changelog.md`.
- T11: the Z39.19 §11.2.2 review finds no unmarked synonym and no missing facet.
- No facet added, split or merged in the last round.

## Samples

[`samples.md`](./samples.md): build (64), bare-facet test (12), round-1 test (60), held
for round 2 (56), all drawn at `a531474`. Term harvest: [`harvest.md`](./harvest.md).
