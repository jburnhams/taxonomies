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

**Status**: set A chosen by Jonathan, 2026-11-26 (process step 4). In use from 2026-11-26: round 3 passed J23 on every facet. Set A's values have draft glossary
entries (`candidate`) so the round-1 kit could be built while Jonathan chooses; they are
redone if he picks another set.

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

## Set A (chosen): area, decider, moment

### Area (`area`)

- **Question**: Which part of an agent system is it about?
- **Principle**: the part that would have to change to change the mechanism.
- **Kind**: thing
- **Values**: `model`, `tool`, `context`, `control`, `coordination`, `output`, `verification`, `operations`
- **Value notes** (the one-line descriptions used in the bare test):
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
- **Agreement**: Fleiss' κ = 0.80, non-Claude pair 0.76. Round 3, 2026-11-26, 60 items (round 2: 0.87 / 0.87; round 1: 0.93 / 0.92) ([results](./rounds/round-3/results.md)).

### Decider (`decider`)

- **Question**: Who makes the call when it applies?
- **Principle**: the party whose decision has the final say at that moment.
- **Kind**: role
- **Values**: `working-model`, `second-model`, `rule`, `person`
- **Value notes**:
  - `working-model`: the working model's own judgment, guided by its instructions.
  - `second-model`: a separate model call: a classifier, judge, monitor, grader or a
    small helper model (label to be chosen in the glossary; see harvest synonym set 3).
  - `rule`: fixed logic: harness code, a schema check, a configured setting applied by code.
    Test (added after round 1): if the model ignored its instructions, would the outcome
    still hold? Yes: `rule`. No: `working-model`.
  - `person`: a human answer at that moment (an approval, a reply, a typed command).
- **Order**: from least to most outside the run.
- **Unsorted**: none yet.
- **Agreement**: Fleiss' κ = 0.77, non-Claude pair 0.76. Round 3, 2026-11-26, 60 items (round 2: 0.66 / 0.54; round 1: 0.58 / 0.57).

### Moment (`moment`)

- **Question**: When does it act?
- **Principle**: the point in a run's life at which the mechanism takes effect.
- **Kind**: happening
- **Values**: `setup`, `turn`, `tool-call`, `failure`, `ending`, `after-run`
- **Value notes**:
  - `setup`: before the first model request: configuration, loading context, choosing tools.
    A format or store fixed in advance takes the moment it is used (added after round 1).
  - `turn`: on each model request or reply.
  - `tool-call`: on each tool call or its result.
  - `failure`: when something goes wrong or a limit is hit.
  - `ending`: when a run or sub-run finishes and hands back.
  - `after-run`: between or after runs: memory, evals, telemetry analysis, review of a PR.
- **Order**: the run's own order.
- **Unsorted**: none yet.
- **Agreement**: Fleiss' κ = 0.86, non-Claude pair 0.83. Round 3, 2026-11-26, 60 items (round 2: 0.72 / 0.67; round 1: 0.72 / 0.69).

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
`prompt`, `rule` with `code` or `schema`; the decider value was then called `model`) in seven of twelve, so it would add rater work
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
| `t04` | OpenHands' risk-assessment prompt is not self-review | control | working-model | tool-call | — |
| `t05` | `WarnOnCacheBusts` | model | rule | turn | model or operations: it only observes |
| `t06` | Tools marked as endings | control | working-model | ending | control or coordination |
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
5. **No facet added or dropped**; `second-model` replaces a first draft's `judge`, and
   the decider `model` became `working-model` so it does not share a label with the area.

## Stage 2: context area (proposed)

**Status**: proposed 2026-11-26, awaiting Jonathan's choice of set (process step 4). Set
A's values have `candidate` glossary entries so the round-1 kit could be built meanwhile;
they are redone if he picks another set. Samples: [`stage-2/samples.md`](./stage-2/samples.md);
terms: [`stage-2/harvest.md`](./stage-2/harvest.md).

These facets sort items whose `area` is `context`. Stage 1's `decider` and `moment`
still apply to them; the questions below are the ones only this area asks.

### How these were found

- **Compared unlike build items**: a request-scoped reminder placed at the tail (`c02`), Goose's import expander (`c26`),
  Codex's ten-times-shorter memory prompts (`c24`) and Open Interpreter's tail truncation
  (`c37`). Each does a different thing to the context (sets where text goes, brings files
  in, keeps knowledge for later, cuts what is there), carries a different kind of text
  (instructions written in advance, knowledge from earlier runs, this run's own record),
  and its text lasts a different time and reaches a different set of runs (one request,
  every run in a repo, one person's runs, one conversation).
- **Reused the repo's own recurring questions**: memory "Levels: what scope does a memory
  belong to?" (`agent-memory-learning.md` §1, "the single most useful lens on this
  topic") is `reach`; the split into instruction files, memory and compaction that the
  repo's three context docs follow is `content`; the repo's verbs (load, place, compact,
  write) are `operation`. Memory §2 (who writes it) and §3 (six trigger points) are
  stage 1's `decider` and `moment`, so they are not repeated.
- **Checked against general categories** (OBO Foundry Table 1): `operation` is a
  happening, `content` a part (continuant), `reach` a quality of that part.

### Set A (recommended): operation, content, reach

### Operation (`operation`)

- **Question**: What does it do to the context?
- **Principle**: the change it makes to what the model reads.
- **Kind**: happening
- **Values**: `supply`, `framing`, `reduction`, `recording`
- **Order**: the life of content: chosen and put in, placed, cut down, kept for later.
- **Unsorted**: none yet.

### Content (`content`)

- **Question**: What kind of text is it about?
- **Principle**: where the text came from, as the model receives it.
- **Kind**: thing
- **Values**: `instruction-text`, `kept-knowledge`, `run-history`
- **Order**: written before the run, kept from earlier runs, made in this run.
- **Unsorted**: none yet.

### Reach (`reach`)

- **Question**: How far does that text reach?
- **Principle**: the widest set of requests and runs that read the same text.
- **Kind**: property
- **Values**: `request-scope`, `conversation-scope`, `project-scope`, `user-scope`, `organization-scope`
- **Order**: from one request outward.
- **Unsorted**: none yet.

### Set B: operation and content only

Drops `reach`, the facet with the most hesitations in the bare test below (four of nine).
Two facets is a grid (spec S2), and it loses the repo's own "most useful lens" (memory
levels) and competency question 16 in [`scope.md`](./scope.md).

### Set C: Set A plus arrival

Adds **Arrival** (`arrival`): *How does the text reach the model?* `always` (in every
request), `on-demand` (an index is in the prompt and the model reads or searches for the
rest: progressive disclosure, memory search tools), `on-match` (the harness adds it when
a path, keyword or feature matches). This is memory §5's "pasted in, pointed at,
searched, or triggered" and context-file loading §12. In the bare test it had no answer
for five of nine in-area items (every `recording` and `framing` item), so as a facet it
would need a `none` value. Its three ideas can be glossary terms instead (stage 2 term
list in [`stage-2/harvest.md`](./stage-2/harvest.md)).

### Bare-facet test (step 5), Set A

Twelve items `ct01`-`ct12` from [`stage-2/samples.md`](./stage-2/samples.md), classified
by Claude with the names and value entries above, 2026-11-26. Arrival is noted for Set C.

| ID | Item | In area | operation | content | reach | arrival | Hesitation |
|---|---|---|---|---|---|---|---|
| `ct01` | Codex: memory, learnings and retrospectives | yes | recording | kept-knowledge | user-scope | on-demand | a survey of a whole pipeline (write and read): took the first named |
| `ct02` | Conditional format notes | yes | supply | instruction-text | request-scope | on-match | — |
| `ct03` | Goose: memory, learnings and retrospectives | yes | supply | kept-knowledge | user-scope | always | survey; reach is user or project |
| `ct04` | Memory is where Codex uses output schemas | no (`tool`) | — | — | — | — | a tool definition, stage 1 sorts it |
| `ct05` | Conditional and just-in-time loading | yes | supply | instruction-text | project-scope | on-match | — |
| `ct06` | Analysis prompts: the quick run and its landings | yes | supply | instruction-text | conversation-scope | always | a prompt's text, not a mechanism |
| `ct07` | Detecting a collapse: `WarnOnCacheBusts` | no (`model`) | — | — | — | — | prompt caching is stage 1's `model` (`t05`) |
| `ct08` | Requests are not context | no (`operations`) | — | — | — | — | its point is that this channel is not context |
| `ct09` | Writing, validation and moderation | yes | recording | kept-knowledge | organization-scope | none | reach varies by store; took the widest |
| `ct10` | What a learning may and may not do | yes | framing | kept-knowledge | project-scope | none | — |
| `ct11` | Incremental vs. from-scratch summarization | yes | reduction | run-history | conversation-scope | always | — |
| `ct12` | The writer that may place but may not author | yes | recording | kept-knowledge | project-scope | none | reach not stated |

What it shows:

1. **Three of twelve are not in the area** (`tool`, `model`, `operations`), from sections
   in context docs and from the heading screen. Raters will answer `in_area` (yes/no,
   with stage 1's area definitions) and stage-2 facets are scored on items the majority
   puts in the area. That also re-tests stage 1's `context` boundary.
2. **`operation` works** on all nine; every value is used.
3. **`content` works**; `kept-knowledge` dominates (five of nine), as memory dominates the
   population (memory 734 against compaction 129 in the context docs). Round 1 checks
   whether that makes κ low, as `rule` did for stage 1's decider.
4. **`reach` is the weakest**: surveys and stores with several readerships (`ct01`,
   `ct03`, `ct09`, `ct12`). Proposed rule for raters: the widest reach the section
   describes; if none is stated, the store's usual home.
5. **Arrival does not apply** to five of nine, so it is Set C, not Set A.
