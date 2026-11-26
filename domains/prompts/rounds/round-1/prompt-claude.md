# Rater prompt: prompts taxonomy, stage 1, round 1

You are classifying 60 items for a taxonomy agreement test. Use only the definitions below; do not look anything up, do not read any files, and do not use other knowledge of the repo they come from.

Each item is one section of a research repo about how AI agent products and harnesses are built (Claude Code, Codex, Gemini CLI, MCP, agent SDKs) and of the designs of the repo owner's own agent platform (Keel, with configurations Forge and Lens). An item is the section's heading, the first lines under it (`gist`), and the file it is in (`from`).

For every item, answer all three questions with exactly one value each, chosen from the list for that question. If no value fits, still pick the closest one and write `unsure` plus a few words in the note column.

Rules:
- Classify the mechanism, approach or design choice the section describes, not the document it is in. The `from` column is part of the item.
- area: the part of an agent system that would have to change to change the mechanism. Whatever decides *whether* something may happen is `control`; whatever decides *where work goes next* is `coordination`; checking whether finished work is right is `verification`.
- decider: the party whose decision has the final say when it applies. If nothing is decided at run time (a store, a format, a protocol rule), answer `rule`. A setting a person chose before the run is `rule`.
- moment: the first point in a run's life at which it takes effect. Anything fixed for the whole run, including protocol and format rules, is `setup`.
- If an item describes several mechanisms, classify the first one named.

Answer as CSV only, with this header and one row per item, in the items' order. Quote any note that contains a comma.

```
id,area,decider,moment,note
```

## The questions and their values

- **area**: Which part of an agent system is it about? Values: `control`, `verification`, `tool`, `output`, `operations`, `model`, `coordination`, `context`
- **decider**: Who makes the call when it applies? Values: `working-model`, `second-model`, `rule`, `person`
- **moment**: When does it act? Values: `tool-call`, `after-run`, `ending`, `failure`, `setup`, `turn`

## Definitions of the values

### tool use (`tool`)

- **Definition**: Tool use is an area of an agent system that covers what the model can do and how its calls and their results move.
- **Scope**: Includes the tool surface, tool implementations, call and result formats, large results and refs, deferred tool loading, code mode, MCP servers and their protocol. Excludes whether a call is allowed (`control`).
- **Aliases**: tooling
- **Near miss**: An approval prompt before a shell command: the command is a tool, but asking whether it may run is `control`.
- **Kind**: thing
- **Facet**: `area`

### turn (`turn`)

- **Definition**: A turn is a moment that comes with each model request and its reply.
- **Scope**: Includes building each request, cache placement, reminders added per request, reasoning budgets, text and titles produced per reply.
- **Aliases**: step, request, model call
- **Near miss**: A check on each shell command: it acts per action, so `tool-call`.
- **Kind**: happening
- **Facet**: `moment`

### rule (`rule`)

- **Definition**: A rule is a decider that is fixed logic applied without a model's judgment.
- **Scope**: Includes harness code, schema and format checks, caps and budgets, a setting chosen beforehand and applied by code, and the default for stores and formats where nothing is chosen at run time.
- **Aliases**: code, deterministic check, static rule
- **Near miss**: A person choosing a permission mode before the run: the choice is the person's, but at run time the mode is applied by code, so `rule`.
- **Kind**: role
- **Facet**: `decider`

### working model (`working-model`)

- **Definition**: A working model is a decider that is the model doing the task, acting on its own judgment and instructions.
- **Scope**: Includes instructions in a prompt that the model follows or not, a model choosing which tool or ending to call, a model rating its own risk. Excludes a separate model call made to check it (`second-model`).
- **Aliases**: the model, agent judgment, model self-report
- **Near miss**: Rules written in the prompt as a table that the harness then checks: the check has the final say, so `rule`.
- **Kind**: role
- **Facet**: `decider`

### failure (`failure`)

- **Definition**: A failure is a moment that comes when something goes wrong or a limit is reached during a run.
- **Scope**: Includes errors, timeouts, budget and context limits, loops, broken model responses, lost or restarted sessions, and what recovers from them.
- **Aliases**: error, recovery, limit
- **Near miss**: A planned stop because the work is done: `ending`.
- **Kind**: happening
- **Facet**: `moment`

### coordination (`coordination`)

- **Definition**: Coordination is an area of an agent system that covers how agents and runs are arranged and where work goes next.
- **Scope**: Includes sub-agents and orchestrators, triggers, pipelines and their edges, hand-offs between runs, entrypoints and the kinds of run a system offers. Excludes deciding whether an action is allowed (`control`).
- **Aliases**: orchestration, multi-agent
- **Near miss**: A tool that ends a run: choosing which ending applies is `control`; the follow-up run it dispatches is `coordination`.
- **Kind**: thing
- **Facet**: `area`

### context (`context`)

- **Definition**: Context is an area of an agent system that covers what the model is given to read and what is kept for later.
- **Scope**: Includes system prompts, context files (AGENTS.md, CLAUDE.md), injected environment text, compaction and summaries, memory across runs. Excludes mid-run text that steers the model (`control`).
- **Aliases**: context engineering
- **Near miss**: A reminder the harness injects when the model loops: it is text in the context, but its job is to redirect, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

### setup (`setup`)

- **Definition**: A setup is a moment that comes before a run's first model request.
- **Scope**: Includes configuration, choosing tools and models, loading context files, and anything fixed for the whole run, including protocol and format rules with no single moment.
- **Aliases**: start, startup, initialisation, configuration
- **Near miss**: Loading a deeper context file when the model first reads that folder: it happens mid-run, so `tool-call`.
- **Kind**: happening
- **Facet**: `moment`

### model access (`model`)

- **Definition**: Model access is an area of an agent system that covers how models are called and chosen.
- **Scope**: Includes providers and their wire formats (dialects), routing between models, reasoning effort and thinking budgets, prompt caching, and what happens when a model's response is broken. Excludes what the model is told (`context`) and which tools it is offered (`tool`).
- **Aliases**: LLM access, inference
- **Near miss**: Deferring tool definitions so the cache survives: the change is to how the request is assembled, so it is `model` when the point is the cache and `tool` when the point is which tools are loaded.
- **Kind**: thing
- **Facet**: `area`

### verification (`verification`)

- **Definition**: Verification is an area of an agent system that covers checking whether the work is right.
- **Scope**: Includes self-verification and completion gates, code review of a change, evals, benchmarks and their graders. Excludes checks on whether an action may happen (`control`).
- **Aliases**: checking, quality checks
- **Near miss**: A blocking monitor that refuses a risky command: it checks an action before it happens, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

### second model (`second-model`)

- **Definition**: A second model is a decider that is a separate model call, apart from the working model, whose answer has the final say.
- **Scope**: Includes classifiers, blocking monitors, judges, graders, validators and small helper models (title writers, summarisers) when their output stands. Excludes the working model reviewing itself (`working-model`).
- **Aliases**: judge, LLM judge, monitor, classifier, grader, verifier
- **Near miss**: A sub-agent that does part of the task: it is a separate model call, but it works rather than decides; its work is judged by whoever accepts it.
- **Kind**: role
- **Facet**: `decider`

### output (`output`)

- **Definition**: Output is an area of an agent system that covers what a run produces for people to read or use.
- **Scope**: Includes turn text and its style, narration, titles, generated files and artefacts, interactive views, tables and charts, and how they are delivered. Excludes records kept for operators (`operations`).
- **Aliases**: deliverable, response, artefact
- **Near miss**: A transcript of the run: it is produced, but for operators and analysis, so it is `operations`.
- **Kind**: thing
- **Facet**: `area`

### tool call (`tool-call`)

- **Definition**: A tool call is a moment that comes with each action the model takes through a tool, or with that action's result.
- **Scope**: Includes approval before an action, monitors on actions, result size limits and refs, MCP requests during a call.
- **Aliases**: action, tool invocation
- **Near miss**: A tool the model calls to finish: the call is the moment the run ends, so `ending`.
- **Kind**: happening
- **Facet**: `moment`

### person (`person`)

- **Definition**: A person is a decider that is a human answering at the moment the mechanism applies.
- **Scope**: Includes approving or denying an action, replying to a question, typing a command or keyword, merging a PR. Excludes a setting a person chose earlier (`rule`).
- **Aliases**: human, user, human in the loop, operator
- **Near miss**: "ultrathink" typed by the user: the person decides, though code detects the word.
- **Kind**: role
- **Facet**: `decider`

### operations (`operations`)

- **Definition**: Operations is an area of an agent system that covers running agents and keeping their records.
- **Scope**: Includes telemetry, traces and transcripts, storage and dashboards, version control and commits, local compute, provenance of content, deployment. Excludes checking the quality of the work (`verification`).
- **Aliases**: ops, observability
- **Near miss**: A loop detector that stops a run: it reads telemetry, but stopping decides, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

### ending (`ending`)

- **Definition**: An ending is a moment that comes when a run or a sub-run finishes and hands back its result.
- **Scope**: Includes completion tools and gates, the shape of a sub-agent's answer, hand-offs, escalation after a review, what a run's outcome records.
- **Aliases**: completion, finish
- **Near miss**: A review of a merged PR the next day: it is after the run, so `after-run`.
- **Kind**: happening
- **Facet**: `moment`

### control (`control`)

- **Definition**: Control is an area of an agent system that covers whether an action may happen and what stops or redirects a run.
- **Scope**: Includes approval and permission modes, risk levels, sandboxing, blocking monitors, steering and nudges, recovery after errors and limits, and how a run is allowed to end. Whatever decides *whether* goes here. Excludes where work goes next (`coordination`) and checking the quality of finished work (`verification`).
- **Aliases**: safety, permissions, guardrails
- **Near miss**: Routing a sub-agent's approval request to the parent session: the routing is `coordination`, but refusing an answer from the wrong session decides whether, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

### after run (`after-run`)

- **Definition**: An after run is a moment that comes between runs or once a run is over.
- **Scope**: Includes writing and consolidating memory, evals and benchmarks, telemetry storage and analysis, retrospectives, a review triggered by a finished PR.
- **Aliases**: offline, between runs, post-run
- **Near miss**: A loop detector inside the run: it reads the same signals, but acts during the run, so `failure`.
- **Kind**: happening
- **Facet**: `moment`

## Items

```csv
id,item,gist,from
r01,Why an agent with no human in the loop needs eyes,"The obvious answer — screenshots proving a UI change works — is the smaller half, and framing it that way gets the design wrong. Forge's inputs are a Jira ticket and a pull request, and both routinely carry images that are *not evidence but requirement or symptom: A UX ticket attaches a mockup.",agent-design/vision.md
r02,"When it runs: at transitions, not continuously","The ledger re-reads a ticket at exactly two moments, plus one sweep: 1. Before dispatch, as part of §4's pass — so a task never starts against intent that has already changed. 2.",agent-design/orchestration.md
r03,"Why archetype 2, not archetype 1, and what that changes","`agent-archetypes.md` draws the sharpest line in this collection between agents driven turn-by-turn by a human in a chat/IDE loop (archetype 1: Claude Code, Cursor, Cline, OpenCode, ...) and agents that run one task to completion with no one watching (archetype 2:",agent-design/README.md
r04,"Three channels, and why they are three","The single most common failure in the field's memory systems is putting things in a store that nothing will ever retrieve. Sorting by addressee separates them cleanly, and the three answers want different machinery:",agent-design/memory.md
r05,Not an archetype: orchestration patterns/backends,"CodeAct + Hyperlight isn't a competing approach to the six above — it's a tool-use strategy* (collapse several tool calls into one generated program, run it in an isolated micro-VM) that any archetype-1 or archetype-2 agent could adopt on top of whatever else it already does.",agent-archetypes.md
r07,"Sliding expiry, on the `persist` tier only","*Amends `artifacts.md` §5.5. `expires=""run""` is unchanged — a run is short and last-use expiry within it means nothing. The amendment applies one tier up: A `persist` artifact expires after a configurable period from last use, not from mint.",agent-design/local.md
r08,Communication style & verbosity,"The other major point of near-identical convergence in the Claude Code-descended family, and the clearest outlier from Cursor.",coding-agent-approaches.md
r09,What runs the program: interpreters and their bounds (read 2026-11-09),"None of these runs model code in a container. Each puts a JavaScript engine next to the agent loop, gives it nothing but the tool functions, and bounds it in-process or in a sidecar. The exception is DeepSeek, which moved the other way. Read from code or shipped binary unless marked.",code-mode/README.md
r10,"Four delivery channels, and why the choice is the design","Before anything about pixels, there is a plumbing question: how does the artefact get from the agent to the person? Four answers are in production, and almost every downstream constraint falls out of which one a harness picked.",agent-generative-output.md
r11,AWS X-Ray and CloudWatch GenAI Observability,"What it is. X-Ray is AWS's distributed tracing; spans now land in CloudWatch Logs and are searched with Transaction Search, which must be enabled. On top sits CloudWatch Generative AI Observability [docs]. Ingest. ADOT (AWS Distro for OpenTelemetry) or CloudWatch's native OTLP endpoints.",telemetry/platform-comparison.md
r12,The rest of the loop that isn't the loop,Two adjacent process documents in the same repo carry the review lessons that didn't fit in a skill: Regression guards must be proven to fail. From `docs/cookbook/responding-to-pr-review-on-a-stack.md`:,code-review-approaches.md
r13,The bug class this family invites,Goose's `retrieve` parses a category file by splitting on `\n\n` and keying the result map on the entry's tags:,agent-tool-implementations.md
r14,Pattern A: sub-agents with a model pin,"Every harness here that has sub-agents lets the model be set per sub-agent; the question is who sets it. Claude Code. The `model` field takes `sonnet`/`opus`/`haiku`/`fable`, a full ID, or `inherit`. Resolution order since v2.1.251:",agent-multi-model.md
r15,Whether it blocks the run,"Reminders, nudges and notices: no extra call, nothing to block on. The trajectory judge runs concurrently: the agent keeps going and the steer lands on a later request. A tick that finds the last evaluation still running is skipped.",agent-run-steering.md
r16,"Claude Agent SDK [source, 32e96114c1]","The SDK spawns the CLI, so its telemetry *is* Claude Code's. What the SDK adds is propagation:",telemetry/harnesses-and-sdks.md
r17,Two things Codex's token-budget mode does that no summariser can,"Added 2026-09-12. Both follow from the §5 row above but are about the prompting* around the mechanism rather than the mechanism itself. *The exhaustion path narrows the tool surface to two calls. Codex's token-budget block carries three escalating prompts, not one.",agent-context-compaction.md
r18,Review → implement handoff (`<findings>` envelope tag),"*What: a review run's confirmed findings can dispatch a follow-up `mode: implement` run on the PR's branch, whose envelope carries a `<findings>` tag holding the review run's posted findings verbatim (the review-finding schema, `formats.md` §4).",agent-design/medium.md
r19,"Skills, if they ever arrive, execute rather than read","`context-files.md` §12 covers the programmatic context channels v1 deliberately does without — MCP server `instructions`, skills, hooks, plugins — and states four rules for whichever of them is added later. The pass supplies a fifth, from `webapp-testing`:",agent-design/generative.md
r20,The null case: Aider,"Aider has no loader, and its absence is instructive rather than a gap. Conventions are an ordinary read-only file the user names explicitly (`--read CONVENTIONS.md`, or a `read:` key in `.aider.conf.yml`), delivered through the same channel as any other read-only file:",agent-context-file-loading.md
r21,"`Expand`: look further, keep going","{ ""name"": ""Expand"", ""input_schema"": { ""type"": ""object"", ""properties"": { ""keywords"": { ""type"": ""string"", ""maxLength"": 100, ""description"": ""Optional. Words to narrow what is shown."" } }, ""additionalProperties"": false } } Description (about 35 words):",agent-design/models.md
r22,"Substrate and retrieval: files for curated memory, search for episodic","Revised 2026-11-02 after widening the survey to always-running agents (`../../agent-memory-learning.md` §15). The first draft said ""no embeddings"" outright. That was right for curated memory and wrong for the episodic layer.* *Every durable store has two layers.",agent-design/keel/memory.md
r23,What implementing one actually costs,"Collected from OMP's converters, this is the checklist for driving a model in-band: 1. A renderer and a scanner, and the scanner must be wider.",agent-tool-call-dialects.md
r24,Claude Code: two reminders and a requeue tool,"`system-reminder-tool-calls-lost-to-session-restart.md` lists, by label, every call the previous turn issued that has no result, and says they ""may not have run, or not completely. Check before issuing them again, and decide whether they are still needed."" Two variants:",agent-run-recovery.md
r25,Search & code navigation,The clearest capability ladder in the whole comparison: plain filename/ text matching → dedicated fast-grep preference → semantic/AST-aware search → LSP-backed symbol search → a delegated search sub-agent.,agent-tool-surfaces.md
r26,Hermes Agent's memory (read from source),"`NousResearch/hermes-agent` `2b31d7b2` (2026-11-02), `website/docs/user-guide/features/{memory,memory-providers}.md`, `agent/{background_review,curator}.py`, `tools/memory_tool_store.py`. The earlier Hermes pass (2026-08-11) read its read-tool eval and `/learn`; this one read its memory.",agent-memory-learning.md
r27,Signal shapes used for the agent itself,*Most common combination: spans + metrics + a separate transcript.,telemetry/catalogue.md
r28,Review-mode system prompts (two shapes),"Review runs come in two harness-selected shapes sharing every wire format, the validator stage, and the reviewer core (`review.md` §6):",agent-design/system-prompts.md
r29,Draft runs on a sandbox,"A draft can't run on production; that's what publishing is for. It can run on a sandbox deployment, which is how a configuration is tried out and how `../eval.md`'s suites run against a change before it ships. A sandbox is a deployment with `kind: sandbox` (`examples/sandbox.deployment.json`).",agent-design/keel/triggers-and-runs.md
r30,Secret scan before the model sees the diff (amends §2),"From ClawSweeper's TruffleHog admission (`../clawsweeper/README.md` §6).* A new step 0 of diff construction: run a pinned secret scanner over the full introduced diff, the PR description and the comment bodies before any envelope is built. A verified live secret stops the review.",agent-design/review.md
r31,"Claude Code's coordinator, worker and workflow prompts (v2.1.303)",Added 2026-10-19 from `leaked/claude-code/piebald-2.1.303/`. This also supplies the Workflow authoring guide §7b had not read.* *Coordinator mode (`system-prompt-coordinator-mode-orchestration.md`) is a separate main prompt for a session that only orchestrates:,agent-subagent-architectures.md
r32,Rules common to every tool result,"*Payload lines must be distinguishable from structural lines, and the mechanism differs by payload — deliberately. Content is never escaped where escaping would break something; each block type instead carries an invariant that makes its payload lines unmistakable:",agent-design/formats.md
r33,Pipeline runs are the durable record,There is no ledger. Everything `../orchestration.md` designed a ledger for is a property of a pipeline run. Every run belongs to one: a template run on its own is a one-stage pipeline run named after the template.,agent-design/keel/pipelines.md
r34,Browser surfaces: three postures,"*Playwright MCP is the clearest statement of the text-first doctrine. Its screenshot tool's own description forbids acting on it: *""Take a screenshot of the current page.",agent-vision-multimodal.md
r35,A run behind a view,"Hex's connector renders another agent's progress and outputs inside Claude's conversation: thinking steps, then charts and tables with citations, while Claude's model reads a summary.",agent-interactive-views.md
r37,The result envelope — the largest single mismatch,"`AbstractMcpTool.wrapCallResult` converts an MCP `CallToolResult` into the `Map<String, Object>` the model receives. Its behaviour, read from source:",agent-design/adk.md
r38,"Budget, and saying when it bit","*Per-file cap: 32 KiB. Total cap: 64 KiB. Both are harness constants, not configuration. Codex's 32 KiB shared budget is the only budget in the field, and its failure mode is the one to avoid:",agent-design/context-files.md
r39,A sandbox-writable `.git` is a channel out of the sandbox,"Added 2026-10-26, from Claude Code 2.1.309 and 2.1.310 (`leaked/claude-code/piebald-2.1.310/`).* §4 treats worktrees as isolation for the *agent*. Two new Claude Code messages are about the reverse direction:",agent-git-vcs.md
r40,Suite 2 — Edit correctness under collateral-damage checking,"The audit's D4 as a hard rule: *every* task asserts on the whole working tree, not on the edited region. A task passes only if the intended change landed and nothing else moved.",agent-design/eval.md
r41,"Outputs: tools, chaining, or something else?","*All three, but they're different things, and the line between them is who decides.",agent-design/keel/outputs.md
r42,Trajectory and transcript formats,"Traces are not the only record of a run. The other record is the *transcript: the ordered messages, tool calls and results, as the model saw them. There is no OTel shape for it (content on spans is a per-call snapshot, not a conversation).",telemetry/standards.md
r43,"Sandboxes, under a blast-radius threat model",Most writing on sandboxing untrusted JS assumes an adversary. For an internal deployment the threat model is different and much more tractable:,agent-local-compute.md
r44,"Braintrust [secondary, Braintrust blog]","Built its own store, Brainstore: object storage as the source of truth, stateless nodes, a write-ahead log, background indexing with Tantivy full-text search, columnar analytics and vector indexes, with a run's spans co-located so a whole execution loads together.",telemetry/platforms-and-storage.md
r45,"Discovery, deferral, selection, authorisation, and skill-scoped tools (added 2026-11-11)","From the agentic-SDK deep dive (`agentic-sdks/`). Its most useful distinction is that four things get called ""tool search"":",agent-deferred-tool-loading.md
r46,What a risk output should contain,"Combining the above, a complete answer to ""how much attention"" has: 1. A level, valid for one exact snapshot (`tier` + `bound_to`). 2. Typed reasons: a dimension (§2) and a domain category for each (ClawSweeper's merge-risk domains, made repo-configurable). 3. Who must decide what:",agent-risk-assessment.md
r47,"How the tier is computed: a floor, then escalation only","Three contributors, combined with `max`. None of them can lower the tier another one set.",agent-design/risk.md
r49,Placing injected text so it does not move the prefix,"The general rule the sources converge on: anything the harness adds mid-run goes at the tail, and stays put once sent. Pydantic's reminders are request-scoped by default (seen on the request they fire on, not after) and conversation-scoped when an obligation must outlast that step.",agent-prompt-cache-health.md
r50,"Deferred with a reason, not adopted","*Shape assertions (`agent-data-analysis.md` §12, problem 1) — row counts across a join, null counts after a merge, groupby cardinality against expectation. These are the cheapest catch for the commonest silent failure in analysis, and no source does them.",agent-design/data.md
r51,"Immutability is a property of the ref, and it is visible","`git://acme/payments@a1b2c3d/...` is immutable; `git://acme/payments@main/...` is not. `artifact://`, `dep://` and `run://` always are. This matters twice:",agent-design/artifacts.md
r52,Provenance is not trust,"Codex's choice to keep provenance separate from trust (""independent of message role, visibility, and trust"") is the useful lesson. Trust is a policy over provenance, and the policy varies by consumer:",agent-content-provenance.md
r53,"Cline — the whole envelope, stringified","`sdk/packages/core/src/extensions/mcp/` (`fb60f9e`). export type McpToolCallResult = unknown; The SDK's MCP adapter (`tools.ts`) wraps each server tool with `createTool({ … execute: () => provider.callTool(…) })` and returns the `CallToolResult` as the tool's output, untyped.",agent-tool-result-transport.md
r54,"Redaction is sometimes the model provider's choice, not the scaffold's","Claude Code's `redacted_thinking` blocks (Anthropic's API-level safety-redacted/encrypted reasoning content) render only as an opaque placeholder — this is the model provider withholding content from the scaffold entirely, not a display decision Claude Code itself makes.",agent-turn-output.md
r55,"Evidence, verification, and what is deferred","Forge produces images only if something takes a screenshot, and v1 has no browser. So evidence is a direction, not a v1 feature. Recording the shape now because it decides two things in v1. *What v1 does commit to:",agent-design/vision.md
r56,"What roles this design has, and the invariant they share","We already have more role structure than OpenClaw, which has none in code: `subagent_type` (`general-purpose` / `reviewer` / `validator`) with the reviewer's specialist as a second key (`tools.md`; `context-files.md` §""Kinds""). The ledger adds no role. It adds a *dispatcher*, which is not an agent.",agent-design/orchestration.md
r57,"Two entrypoints, one core",┌─────────────────────────┐ │ Shared core tool set │ │ Read · Edit · Write │ │ Bash · Grep · List │ │ Task · AskUser │ │ FetchJira · AddComment │ │ InspectImage │ │ Complete │ └────────────┬─────────────┘ │ ┌──────────────────┴──────────────────┐ │ │ ┌────────▼─────────┐ ┌──────────▼──────────┐ │ Coding agent │ │ Review agent │,agent-design/README.md
r59,Minimalist / self-sufficient scaffold,"Not a deployment context — a philosophy that cuts across archetypes 1 and 2: strip the tool surface down as far as it'll go and either trust the model's judgment to fill the gap, or explicitly let it extend its own capabilities. *Defining traits:",agent-archetypes.md
r60,The capability paragraph is computed from the tool set,"*Amends `system-prompts.md`, and settles the open half of `README.md`'s *per-model prompt variation* row. That row adopts Codex's shape — one canonical prompt per mode, with *capability-conditional subtraction by heading as the upgrade path — and prices the cost honestly:",agent-design/cloudflare.md
h01,Sandbox and isolation as a complementary layer,"A fully platform-branching sandbox description, stated directly in the prompt text rather than left implicit — Zed (genuinely open source):",agent-permissions-approval.md
h02,A table's expiry error carries its shape,"*Extends `artifacts.md` §5.5. That section is already right that *expiry is a recoverable, self-describing error, never a null, and its worked example names the recovery through `origin`: <error tool=""Read"" ref=""artifact://img_7f3a2b9c""> !",agent-design/local.md
h03,Identity & self-referential framing,"How the prompt introduces the agent, and what happens when the user asks ""are you X"" or ""can you do Y"".",coding-agent-approaches.md
h04,The honesty rules that come with charting,"Worth quoting because nothing else in this collection puts truthfulness constraints in a layout skill. `artifact-dashboard`: *""Replace every placeholder number — and never invent one … The same goes for dates and metadata:",agent-generative-output.md
```
