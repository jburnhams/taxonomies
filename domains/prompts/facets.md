# Prompts taxonomy: facets (stage 1)

**In one line**: three proposed sorting questions for every mechanism the prompts repo
describes (which part of an agent system, who makes the call, when it acts), plus two
alternatives, awaiting Jonathan's choice.

**In plain words**: a facet is a question you can ask of any item, with a short list of
answers. With these three you could find, for example, "every check in the tools area
that a second model makes on each tool call" without anyone having written that list.
Stage 1 only needs facets that work across the whole repo; each area gets its own
finer questions in a later stage (proposal M1 in
[`design/method-v1.1.md`](../../design/method-v1.1.md)).

**Status**: proposal, 2026-11-26 (process step 4). Values have no glossary entries yet;
they are written after Jonathan picks a set (step 6).

## How these were found

- **Compared unlike items** (step 4, constant comparison): a completion gate that refuses
  "done" until tests pass (`r48`), Claude Code's three title generators (`t12`), a
  blocking monitor (`r06`) and a memory digest gate (`r58`). Each is about one part of an
  agent system (verification, output, control, context); each has something that makes
  the call (fixed code, a small second model, a second model, fixed code); and each acts
  at a moment (the end, each turn, each tool call, after the run).
- **Reused the repo's own recurring questions**: "static rules vs. LLM-based judgment"
  (`agent-permissions-approval.md` §2) and "Who sets the level" (`agent-risk-assessment.md`,
  build item `b04`: model self-report up to fixed rules) are the decider question; Keel's
  taxonomy orders a run as starting (§8), running (§9), ending (§5) and what follows (§7),
  which is the moment question; *Inside the Scaffold*'s three layers and the repo's
  doc-per-topic layout are the area question (see [`harvest.md`](./harvest.md)).
- **Checked against general categories** (OBO Foundry Table 1): `area` is about a part
  (continuant), `decider` is a role, `moment` is a happening. Nothing about a quality of
  the mechanism (cost, risk) held across all items; risk has its own facets inside the
  control area (`agent-risk-assessment.md` §2), which is where stage 2 picks it up.
- **Structure (spec S2)**: three dimensions, so facets. In the bare test below `rule`
  occurs in four areas and `tool-call` in two; twelve items cannot show independence,
  so round 1 checks it on 60.

## Set A (recommended): area, decider, moment

### Area (`area`)

- **Question**: Which part of an agent system is it about?
- **Principle**: the part that would have to change to change the mechanism.
- **Kind**: thing
- **Values**, with one line each for the bare test:
  - `model`: calling and choosing models: providers, dialects, routing, reasoning
    effort, prompt caching.
  - `tool`: what the model can do and how calls and results move: tool surfaces,
    implementations, result transport, deferred loading, code mode, MCP.
  - `context`: what the model is given and keeps: system prompts, context files,
    compaction, memory.
  - `control`: what the agent may do and what stops or redirects it: approval,
    permission modes, risk, sandboxing, steering, recovery, endings.
  - `coordination`: how agents and runs are arranged: sub-agents, orchestration,
    triggers, pipelines, hand-offs between runs.
  - `output`: what a run produces for people: turn text, titles, generated files,
    interactive views, tables, charts.
  - `verification`: checking the work: self-verification, code review, evals,
    benchmarks.
  - `operations`: running and watching agents: telemetry, transcripts, version control,
    local compute, provenance.
- **Order**: from the model outward: what is called, what it can do, what it knows, what
  it may do, how runs fit together, what comes out, how it is checked, how it is run.
- **Unsorted**: none yet.

### Decider (`decider`)

- **Question**: Who makes the call when it applies?
- **Principle**: the party whose decision has the final say at that moment.
- **Kind**: role
- **Values**:
  - `model`: the working model's own judgment, guided by its instructions.
  - `second-model`: a separate model call: a classifier, judge, monitor, grader or a
    small helper model (label to be chosen in the glossary; see harvest synonym set 3).
  - `rule`: fixed logic: harness code, a schema check, a configured setting applied by code.
  - `person`: a human answer at that moment (an approval, a reply, a typed command).
- **Order**: from least to most outside the run.
- **Unsorted**: none yet.

### Moment (`moment`)

- **Question**: When does it act?
- **Principle**: the point in a run's life at which the mechanism takes effect.
- **Kind**: happening
- **Values**:
  - `setup`: before the first model request: configuration, loading context, choosing tools.
  - `turn`: on each model request or reply.
  - `tool-call`: on each tool call or its result.
  - `failure`: when something goes wrong or a limit is hit.
  - `ending`: when a run or sub-run finishes and hands back.
  - `after-run`: between or after runs: memory, evals, telemetry analysis, review of a PR.
- **Order**: the run's own order.
- **Unsorted**: none yet.

## Set B: area and decider only

Drops `moment`, the weakest facet in the bare test (three of twelve items had no clear
moment). Two facets is a grid, not a faceted scheme (spec S2), and it loses competency
questions 4 and 6 in [`scope.md`](./scope.md).

## Set C: Set A plus channel

Adds **Channel** (`channel`): *Where is it written down?* `prompt` (text the model
reads), `schema` (a tool or protocol definition), `code` (harness logic), `config` (a
setting a person chooses). This is the repo's other recurring question ("Where the
enforcement actually lives: harness vs. prompt", `agent-permissions-approval.md` §7), but
classified for the bare-test items afterwards, it followed `decider` (`model` with
`prompt`, `rule` with `code` or `schema`) in seven of twelve, so it would add rater work
for little new sorting. Three of the five where it did not were in `control` (`t03`,
`t06`, `t10`), so stage 2 can add it there, where the two come apart.

## Bare-facet test (step 5), Set A

Twelve items `t01`-`t12` from [`samples.md`](./samples.md), classified by Claude with the
names and one-line values above, 2026-11-26. Hesitations are the point.

| ID | Item | area | decider | moment | Hesitation |
|---|---|---|---|---|---|
| `t01` | Arize Phoenix's store | operations | rule | after-run | nothing is decided: a store, not a choice |
| `t02` | Why the cache survives (deferred tools) | model | rule | turn | model or tool: the fix is in how the request is built |
| `t03` | Escalation after validation | control | rule | ending | the rules are in the prompt but the harness checks them; moment is a pipeline step |
| `t04` | OpenHands' risk-assessment prompt is not self-review | control | model | tool-call | — |
| `t05` | `WarnOnCacheBusts` | model | rule | turn | model or operations: it only observes |
| `t06` | Tools marked as endings | control | model | ending | control or coordination |
| `t07` | MCP elicitation and task handles in a hands-off run | tool | rule | tool-call | — |
| `t08` | A third entrypoint, `analyse` | coordination | person | setup | an entrypoint is a kind of run, not a mechanism |
| `t09` | Large results come back as refs | tool | rule | tool-call | — |
| `t10` | Answers bound to the asker (Goose, Crush) | control | person | tool-call | control or coordination |
| `t11` | The MCP `2026-07-28` rewrite | tool | rule | setup | a protocol revision has no moment |
| `t12` | Claude Code's three title generators | output | second-model | turn | "judge" does not fit a model that writes titles, hence `second-model` |

What it shows:

1. **`area` works** with two boundaries to settle in scope notes: `model` against
   `tool`/`operations` for caching (decided here by the principle: what would change),
   and `control` against `coordination` for endings and answers routed between
   sessions. Proposed rule: whatever decides *whether* goes to `control`; whatever
   decides *where work goes next* goes to `coordination`.
2. **`decider` works** for every item that describes a choice; for stores and formats
   (`t01`, `t11`) it defaults to `rule`. The rater prompt will say so.
3. **`moment` is the weakest**: `t08`, `t11` and `t03` had no clean answer. Proposed
   rule: the first moment at which it takes effect, `setup` for anything fixed before a
   run.
4. **Item quality**: two items (`t08`, `t11`) describe a design change or a revision
   rather than a mechanism. The round-1 prompt will tell raters to classify the
   mechanism the section describes.
5. **No facet added or dropped**; `second-model` replaces a first draft's `judge`.
