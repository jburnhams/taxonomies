# Prompts taxonomy: glossary

**In one line**: one entry per concept in the prompts repo, with the word to use, the other
words people use for it, a definition, an example and a near miss.

**In plain words**: when you write in the prompts repo, use the heading word of the entry.
If you reach for one of its aliases, it points you here. Everything here is `candidate`
until stage 1 passes its rounds (spec G3).

**Status**: draft, 2026-11-26, all `candidate`. 18 values of facet set A (chosen by
Jonathan, [`facets.md`](./facets.md)) and 36 kernel terms drafted after J14 ("agent" is a
model configured to act). The moment values `turn`, `tool-call` and `ending` are also the
kernel entries for those concepts. Field rules: [`design/spec.md` §4](../../design/spec.md#4-glossarymd).
Counts: [`harvest.md`](./harvest.md). Examples link to prompts at commit `a531474`.

## Label choices for Jonathan's veto (J8)

1. **`second-model`** for a separate model call that makes the call, rather than "judge",
   "monitor" or "classifier": each of those names one role of it (harvest synonym set 3),
   and the bare test had a title-writing helper model that is none of them (`t12`).
2. **`rule`** rather than "harness" or "code" for fixed logic, because the harness also
   runs the model and the other values, and a schema check or a setting applied by code is
   still a rule.
3. **`verification`** rather than "evaluation" for the checking area, because it covers
   self-verification and code review as well as evals; "eval" is an alias.
4. **Area labels "model access" and "tool use"** (IDs `model`, `tool` unchanged, as the
   round-1 raters use them): so that the plain words "model" and "tool" can be the
   kernel concepts (`language-model`, `agent-tool`). Area aliases that named kernel
   concepts (eval, memory, MCP, telemetry, harness, handoff) were moved to those entries.
5. **`context window`** for everything a model is given on one request, so the area keeps
   "context"; **`context file`** for AGENTS.md / CLAUDE.md and the like, which the repo
   has no single word for.
6. **`steer`** for mid-run redirecting text (nudge 108, steer 103, system-reminder 46):
   "nudge" is commoner but names only the gentle kind.
7. **`harness`** for the products (Claude Code, Codex), per J14; "coding agent" is an
   alias of `harness`.
8. **"mode"** gets no entry: it names at least four concepts (harvest homonym 2), and
   `permission-mode` takes the approval sense.
9. **`operations`** is flagged by T3 as a possible plural; it is a mass noun here
   (as in "IT operations"), kept.

## Area values (`area`)

### model access (`model`)

- **Definition**: Model access is an area of an agent system that covers how models are called and chosen.
- **Scope**: Includes providers and their wire formats (dialects), routing between models, reasoning effort and thinking budgets, prompt caching, and what happens when a model's response is broken. Excludes what the model is told (`context`) and which tools it is offered (`tool`).
- **Aliases**: LLM access, inference
- **Example**: [agent-prompt-cache-health.md](https://github.com/jburnhams/prompts/blob/a531474/agent-prompt-cache-health.md), what moves a cached prefix.
- **Near miss**: Deferring tool definitions so the cache survives: the change is to how the request is assembled, so it is `model` when the point is the cache and `tool` when the point is which tools are loaded.
- **Kind**: thing
- **Facet**: `area`
- **Status**: candidate
- **Warrant**: model 3,759 uses in 210 files; LLM 308 (Jonathan's words: "llm")
- **History**: 2026-11-26 added.

### tool use (`tool`)

- **Definition**: Tool use is an area of an agent system that covers what the model can do and how its calls and their results move.
- **Scope**: Includes the tool surface, tool implementations, call and result formats, large results and refs, deferred tool loading, code mode, MCP servers and their protocol. Excludes whether a call is allowed (`control`).
- **Aliases**: tooling
- **Example**: [agent-tool-surfaces.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-surfaces.md), the capability families.
- **Near miss**: An approval prompt before a shell command: the command is a tool, but asking whether it may run is `control`.
- **Kind**: thing
- **Facet**: `area`
- **Status**: candidate
- **Warrant**: "tool surface" 143, tool call 206, MCP server 132 (Jonathan's words: "mcps")
- **History**: 2026-11-26 added.

### context (`context`)

- **Definition**: Context is an area of an agent system that covers what the model is given to read and what is kept for later.
- **Scope**: Includes system prompts, context files (AGENTS.md, CLAUDE.md), injected environment text, compaction and summaries, memory across runs. Excludes mid-run text that steers the model (`control`).
- **Aliases**: context engineering
- **Example**: [agent-context-file-loading.md](https://github.com/jburnhams/prompts/blob/a531474/agent-context-file-loading.md).
- **Near miss**: A reminder the harness injects when the model loops: it is text in the context, but its job is to redirect, so it is `control`.
- **Kind**: thing
- **Facet**: `area`
- **Status**: candidate
- **Warrant**: compaction 501, memory 1,215, AGENTS.md 425, system prompt 258
- **History**: 2026-11-26 added.

### control (`control`)

- **Definition**: Control is an area of an agent system that covers whether an action may happen and what stops or redirects a run.
- **Scope**: Includes approval and permission modes, risk levels, sandboxing, blocking monitors, steering and nudges, recovery after errors and limits, and how a run is allowed to end. Whatever decides *whether* goes here. Excludes where work goes next (`coordination`) and checking the quality of finished work (`verification`).
- **Aliases**: safety, permissions, guardrails
- **Example**: [agent-permissions-approval.md](https://github.com/jburnhams/prompts/blob/a531474/agent-permissions-approval.md).
- **Near miss**: Routing a sub-agent's approval request to the parent session: the routing is `coordination`, but refusing an answer from the wrong session decides whether, so it is `control`.
- **Kind**: thing
- **Facet**: `area`
- **Status**: candidate
- **Warrant**: approval 759, sandbox 457, policy 614, permission 238
- **History**: 2026-11-26 added.

### coordination (`coordination`)

- **Definition**: Coordination is an area of an agent system that covers how agents and runs are arranged and where work goes next.
- **Scope**: Includes sub-agents and orchestrators, triggers, pipelines and their edges, hand-offs between runs, entrypoints and the kinds of run a system offers. Excludes deciding whether an action is allowed (`control`).
- **Aliases**: orchestration, multi-agent
- **Example**: [agent-subagent-architectures.md](https://github.com/jburnhams/prompts/blob/a531474/agent-subagent-architectures.md).
- **Near miss**: A tool that ends a run: choosing which ending applies is `control`; the follow-up run it dispatches is `coordination`.
- **Kind**: thing
- **Facet**: `area`
- **Status**: candidate
- **Warrant**: sub-agent 750 (both spellings), orchestrator 281, pipeline 390, trigger 306
- **History**: 2026-11-26 added.

### output (`output`)

- **Definition**: Output is an area of an agent system that covers what a run produces for people to read or use.
- **Scope**: Includes turn text and its style, narration, titles, generated files and artefacts, interactive views, tables and charts, and how they are delivered. Excludes records kept for operators (`operations`).
- **Aliases**: deliverable, response, artefact
- **Example**: [agent-generative-output.md](https://github.com/jburnhams/prompts/blob/a531474/agent-generative-output.md).
- **Near miss**: A transcript of the run: it is produced, but for operators and analysis, so it is `operations`.
- **Kind**: thing
- **Facet**: `area`
- **Status**: candidate
- **Warrant**: output 967, artifact 573, view 548
- **History**: 2026-11-26 added.

### verification (`verification`)

- **Definition**: Verification is an area of an agent system that covers checking whether the work is right.
- **Scope**: Includes self-verification and completion gates, code review of a change, evals, benchmarks and their graders. Excludes checks on whether an action may happen (`control`).
- **Aliases**: checking, quality checks
- **Example**: [agent-self-verification.md](https://github.com/jburnhams/prompts/blob/a531474/agent-self-verification.md).
- **Near miss**: A blocking monitor that refuses a risky command: it checks an action before it happens, so it is `control`.
- **Kind**: thing
- **Facet**: `area`
- **Status**: candidate
- **Warrant**: reviewer 445, eval 182, benchmark 129, self-verification 137 (Jonathan's words: "evals")
- **History**: 2026-11-26 added.

### operations (`operations`)

- **Definition**: Operations is an area of an agent system that covers running agents and keeping their records.
- **Scope**: Includes telemetry, traces and transcripts, storage and dashboards, version control and commits, local compute, provenance of content, deployment. Excludes checking the quality of the work (`verification`).
- **Aliases**: ops, observability
- **Example**: [agent-telemetry.md](https://github.com/jburnhams/prompts/blob/a531474/agent-telemetry.md).
- **Near miss**: A loop detector that stops a run: it reads telemetry, but stopping decides, so it is `control`.
- **Kind**: thing
- **Facet**: `area`
- **Status**: candidate
- **Warrant**: telemetry 158, trace 122, transcript 410
- **History**: 2026-11-26 added.

## Decider values (`decider`)

### working model (`working-model`)

- **Definition**: A working model is a decider that is the model doing the task, acting on its own judgment and instructions.
- **Scope**: Includes instructions in a prompt that the model follows or not, a model choosing which tool or ending to call, a model rating its own risk. Excludes a separate model call made to check it (`second-model`).
- **Aliases**: the model, agent judgment, model self-report
- **Example**: [agent-risk-assessment.md](https://github.com/jburnhams/prompts/blob/a531474/agent-risk-assessment.md), "Who sets the level": model self-report.
- **Near miss**: Rules written in the prompt as a table that the harness then checks: the check has the final say, so `rule`.
- **Kind**: role
- **Facet**: `decider`
- **Status**: candidate
- **Warrant**: "the agent" 629; "model self-report" in agent-risk-assessment.md
- **History**: 2026-11-26 added; renamed from the bare-test value "model" so the label differs from the area value.

### second model (`second-model`)

- **Definition**: A second model is a decider that is a separate model call, apart from the working model, whose answer has the final say.
- **Scope**: Includes classifiers, blocking monitors, judges, graders, validators and small helper models (title writers, summarisers) when their output stands. Excludes the working model reviewing itself (`working-model`).
- **Aliases**: judge, LLM judge, monitor, classifier, grader, verifier
- **Example**: [agent-permissions-approval.md](https://github.com/jburnhams/prompts/blob/a531474/agent-permissions-approval.md) §2c, Claude Code's auto-mode classifier.
- **Near miss**: A sub-agent that does part of the task: it is a separate model call, but it works rather than decides; its work is judged by whoever accepts it.
- **Kind**: role
- **Facet**: `decider`
- **Status**: candidate
- **Warrant**: judge 218, classifier 134, monitor 65, grader 39, verifier 30 (Jonathan's words: "llm judges")
- **History**: 2026-11-26 added.

### rule (`rule`)

- **Definition**: A rule is a decider that is fixed logic applied without a model's judgment.
- **Scope**: Includes harness code, schema and format checks, caps and budgets, a setting chosen beforehand and applied by code, and the default for stores and formats where nothing is chosen at run time.
- **Aliases**: code, deterministic check, static rule
- **Example**: [agent-self-verification.md](https://github.com/jburnhams/prompts/blob/a531474/agent-self-verification.md), "Deterministic, non-LLM completion gates".
- **Near miss**: A person choosing a permission mode before the run: the choice is the person's, but at run time the mode is applied by code, so `rule`.
- **Kind**: role
- **Facet**: `decider`
- **Status**: candidate
- **Warrant**: harness 1,544; "static rules" (agent-permissions-approval.md §2)
- **History**: 2026-11-26 added.

### person (`person`)

- **Definition**: A person is a decider that is a human answering at the moment the mechanism applies.
- **Scope**: Includes approving or denying an action, replying to a question, typing a command or keyword, merging a PR. Excludes a setting a person chose earlier (`rule`).
- **Aliases**: human, user, human in the loop, operator
- **Example**: [agent-permissions-approval.md](https://github.com/jburnhams/prompts/blob/a531474/agent-permissions-approval.md) §1, approval modes.
- **Near miss**: "ultrathink" typed by the user: the person decides, though code detects the word.
- **Kind**: role
- **Facet**: `decider`
- **Status**: candidate
- **Warrant**: approval 759; "human in the loop" in agent-design/vision.md
- **History**: 2026-11-26 added.

## Moment values (`moment`)

### setup (`setup`)

- **Definition**: A setup is a moment that comes before a run's first model request.
- **Scope**: Includes configuration, choosing tools and models, loading context files, and anything fixed for the whole run, including protocol and format rules with no single moment.
- **Aliases**: start, startup, initialisation, configuration
- **Example**: [agent-context-file-loading.md](https://github.com/jburnhams/prompts/blob/a531474/agent-context-file-loading.md).
- **Near miss**: Loading a deeper context file when the model first reads that folder: it happens mid-run, so `tool-call`.
- **Kind**: happening
- **Facet**: `moment`
- **Status**: candidate
- **Warrant**: Keel taxonomy §8 "Starting work"
- **History**: 2026-11-26 added.

### turn (`turn`)

- **Definition**: A turn is a moment that comes with each model request and its reply.
- **Scope**: Includes building each request, cache placement, reminders added per request, reasoning budgets, text and titles produced per reply.
- **Aliases**: step, request, model call
- **Example**: [agent-turn-output.md](https://github.com/jburnhams/prompts/blob/a531474/agent-turn-output.md).
- **Near miss**: A check on each shell command: it acts per action, so `tool-call`.
- **Kind**: happening
- **Facet**: `moment`
- **Status**: candidate
- **Warrant**: turn 887 uses in 143 files
- **History**: 2026-11-26 added.

### tool call (`tool-call`)

- **Definition**: A tool call is a moment that comes with each action the model takes through a tool, or with that action's result.
- **Scope**: Includes approval before an action, monitors on actions, result size limits and refs, MCP requests during a call.
- **Aliases**: action, tool invocation
- **Example**: [agent-tool-result-transport.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-result-transport.md).
- **Near miss**: A tool the model calls to finish: the call is the moment the run ends, so `ending`.
- **Kind**: happening
- **Facet**: `moment`
- **Status**: candidate
- **Warrant**: tool call 206 uses in 86 files
- **History**: 2026-11-26 added.

### failure (`failure`)

- **Definition**: A failure is a moment that comes when something goes wrong or a limit is reached during a run.
- **Scope**: Includes errors, timeouts, budget and context limits, loops, broken model responses, lost or restarted sessions, and what recovers from them.
- **Aliases**: error, recovery, limit
- **Example**: [agent-run-recovery.md](https://github.com/jburnhams/prompts/blob/a531474/agent-run-recovery.md).
- **Near miss**: A planned stop because the work is done: `ending`.
- **Kind**: happening
- **Facet**: `moment`
- **Status**: candidate
- **Warrant**: agent-run-recovery.md (whole doc)
- **History**: 2026-11-26 added.

### ending (`ending`)

- **Definition**: An ending is a moment that comes when a run or a sub-run finishes and hands back its result.
- **Scope**: Includes completion tools and gates, the shape of a sub-agent's answer, hand-offs, escalation after a review, what a run's outcome records.
- **Aliases**: completion, finish
- **Example**: [agent-design/keel/endings.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/endings.md).
- **Near miss**: A review of a merged PR the next day: it is after the run, so `after-run`.
- **Kind**: happening
- **Facet**: `moment`
- **Status**: candidate
- **Warrant**: Keel taxonomy §5 "How a run ends"; handoff 261
- **History**: 2026-11-26 added.

### after run (`after-run`)

- **Definition**: An after run is a moment that comes between runs or once a run is over.
- **Scope**: Includes writing and consolidating memory, evals and benchmarks, telemetry storage and analysis, retrospectives, a review triggered by a finished PR.
- **Aliases**: offline, between runs, post-run
- **Example**: [agent-memory-learning.md](https://github.com/jburnhams/prompts/blob/a531474/agent-memory-learning.md).
- **Near miss**: A loop detector inside the run: it reads the same signals, but acts during the run, so `failure`.
- **Kind**: happening
- **Facet**: `moment`
- **Status**: candidate
- **Warrant**: Keel taxonomy §7 "What a run leads to"
- **History**: 2026-11-26 added.

## Kernel terms (stage 1)

The words every area uses. Drafted 2026-11-26 after J14; all `candidate`. Not part of the
round-1 rater prompts (raters sort with the facet values only); tested by the name test (T9).

### agent (`agent`)

- **Definition**: An agent is a model configured to act, with a prompt and tools, in a loop that runs its tool calls and returns the results to it.
- **Scope**: Includes the orchestrator of a run and every sub-agent (Keel: one model context inside a run). Excludes the product or program that runs the loop, which is a `harness`; "coding agent" in the research docs usually names a harness and is an alias there only when it means the configured model.
- **Aliases**: agent loop, AI agent
- **Example**: [agent-design/keel/taxonomy.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/taxonomy.md)
- **Near miss**: Claude Code: it is a harness that runs agents; calling it "an agent" is the product sense.
- **Kind**: thing
- **Status**: candidate
- **Warrant**: agent 5,598 uses in 227 files; Keel taxonomy §1
- **History**: 2026-11-26 added; sense decided by Jonathan (J14).

### harness (`harness`)

- **Definition**: A harness is a program that runs one or more agents: it builds each model request, executes tool calls, enforces limits and keeps the transcript.
- **Scope**: Includes products and CLIs (Claude Code, Codex CLI, Gemini CLI, OpenCode, Goose), SWE-bench scaffolds and Keel itself. Excludes libraries for building one (`agent-sdk`) and the model provider's API.
- **Aliases**: scaffold, agent product, coding agent, agent runtime
- **Example**: [coding-agent-approaches.md](https://github.com/jburnhams/prompts/blob/a531474/coding-agent-approaches.md)
- **Near miss**: An agent SDK such as Pydantic AI: it supplies the parts a harness is built from but is not itself a running program.
- **Kind**: thing
- **Related**: `agent`
- **Status**: candidate
- **Warrant**: harness 1,544 in 170 files; scaffold 81 (Jonathan's words: "harnesses")
- **History**: 2026-11-26 added.

### agent SDK (`agent-sdk`)

- **Definition**: An agent SDK is a library for building harnesses and agents in code.
- **Scope**: Includes the Claude Agent SDK, OpenAI Agents SDK, LangGraph, Pydantic AI, Google ADK. Excludes the harness built with it.
- **Aliases**: SDK, agent framework, framework
- **Example**: [agentic-sdks/README.md](https://github.com/jburnhams/prompts/blob/a531474/agentic-sdks/README.md)
- **Near miss**: The Claude Agent SDK spawns the Claude Code CLI: the SDK is the library, the CLI is the harness.
- **Kind**: thing
- **Related**: `harness`
- **Status**: candidate
- **Warrant**: SDK 452 in 83 files; framework 143
- **History**: 2026-11-26 added.

### model (`language-model`)

- **Definition**: A model is a neural network that a harness calls to produce text and tool calls.
- **Scope**: Includes a model identified by its provider's id (`gpt-5.4`, `claude-opus-5-5`) and its reasoning settings. Excludes the configured agent built on it and the area value `model` (label "model access").
- **Aliases**: LLM, large language model
- **Example**: [agent-multi-model.md](https://github.com/jburnhams/prompts/blob/a531474/agent-multi-model.md)
- **Near miss**: A model provider: the company or service that serves the model.
- **Kind**: thing
- **Related**: `model-provider`
- **Status**: candidate
- **Warrant**: model 3,759 in 210 files; LLM 308 (Jonathan's words: "llm")
- **History**: 2026-11-26 added.

### model provider (`model-provider`)

- **Definition**: A model provider is a service that serves models through an API.
- **Scope**: Includes Anthropic, OpenAI, Google, NVIDIA NIM, OpenRouter, a local llama.cpp server.
- **Aliases**: provider, vendor, inference provider
- **Example**: [agent-tool-call-dialects.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-call-dialects.md)
- **Near miss**: A model family: Claude or Gemini names models, not the service.
- **Kind**: thing
- **Related**: `language-model`
- **Status**: candidate
- **Warrant**: provider 345; vendor 211
- **History**: 2026-11-26 added.

### run (`run`)

- **Definition**: A run is an execution of an agent configuration from its start to its ending.
- **Scope**: Includes a run's sub-agents (they are part of it). Excludes a person's longer interaction across many runs (`session`). The verb "run" is not this term.
- **Aliases**: execution, job, task run
- **Example**: [agent-design/keel/taxonomy.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/taxonomy.md)
- **Near miss**: A session in a chat UI, which may contain many runs.
- **Kind**: happening
- **Related**: `session`, `transcript`
- **Status**: candidate
- **Warrant**: run 3,287 in 219 files; Keel taxonomy §9
- **History**: 2026-11-26 added.

### session (`session`)

- **Definition**: A session is a continuing interaction between a person and a harness that can span several runs.
- **Scope**: Includes a Claude Code terminal session and a chat thread. Excludes the MCP protocol session removed in the `2026-07-28` MCP revision (a hidden label here, not a concept).
- **Aliases**: conversation, thread, chat
- **Example**: [agent-run-recovery.md](https://github.com/jburnhams/prompts/blob/a531474/agent-run-recovery.md)
- **Near miss**: A run: one execution, which a session may contain several of.
- **Kind**: happening
- **Related**: `run`
- **Status**: candidate
- **Warrant**: session 1,019; conversation 440; thread 457
- **History**: 2026-11-26 added.

### transcript (`transcript`)

- **Definition**: A transcript is a record of everything the model saw and did in a run, in order.
- **Scope**: Includes messages, tool calls and results as the model saw them. Excludes traces (timing and structure, `trace`).
- **Aliases**: trajectory, conversation log
- **Example**: [telemetry/standards.md](https://github.com/jburnhams/prompts/blob/a531474/telemetry/standards.md)
- **Near miss**: A trace: spans with timings, not the conversation.
- **Kind**: thing
- **Related**: `run`, `trace`
- **Status**: candidate
- **Warrant**: transcript 410; trajectory 49
- **History**: 2026-11-26 added.

### trace (`trace`)

- **Definition**: A trace is a record of a run as nested timed spans for monitoring.
- **Scope**: Includes OTel GenAI spans and their attributes. Excludes the model-visible conversation (`transcript`).
- **Aliases**: spans, telemetry trace
- **Example**: [telemetry/README.md](https://github.com/jburnhams/prompts/blob/a531474/telemetry/README.md)
- **Near miss**: A transcript: what the model saw, not how long each part took.
- **Kind**: thing
- **Related**: `transcript`
- **Status**: candidate
- **Warrant**: trace 122; span 119
- **History**: 2026-11-26 added.

### tool (`agent-tool`)

- **Definition**: A tool is a capability an agent can call by name with arguments, defined by a name, a description and an input schema.
- **Scope**: Includes built-in tools (Read, Edit, Bash), tools from MCP servers, and generated tools (Keel's Complete). Excludes the area value `tool` (label "tool use").
- **Aliases**: function, function tool
- **Example**: [agent-tool-implementations.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-implementations.md)
- **Near miss**: A skill: instructions and files the agent reads, not a callable function (though a skill may bring tools).
- **Kind**: thing
- **Related**: `tool-surface`, `tool-result`
- **Status**: candidate
- **Warrant**: tool call 206; Keel taxonomy §3
- **History**: 2026-11-26 added.

### tool surface (`tool-surface`)

- **Definition**: A tool surface is a set of tools an agent is offered in a run.
- **Scope**: Includes deferred tools that can be loaded on demand. Excludes a UI surface where output is shown.
- **Aliases**: toolset, tool list, tool set
- **Example**: [agent-tool-surfaces.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-surfaces.md)
- **Near miss**: Keel's tool group: a named, reusable set used to grant tools; a run's tool surface may combine several.
- **Kind**: thing
- **Related**: `agent-tool`
- **Status**: candidate
- **Warrant**: "tool surface" 143 in 67 files
- **History**: 2026-11-26 added.

### tool result (`tool-result`)

- **Definition**: A tool result is a message that a harness returns to the model after a tool call.
- **Scope**: Includes errors, truncated output and refs to large results stored elsewhere.
- **Aliases**: tool output, observation
- **Example**: [agent-tool-result-transport.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-result-transport.md)
- **Near miss**: The tool's side effect (a file written): the result is only what the model is told.
- **Kind**: thing
- **Related**: `agent-tool`
- **Status**: candidate
- **Warrant**: tool result 122 in 58 files
- **History**: 2026-11-26 added.

### MCP (`mcp`)

- **Definition**: MCP is a protocol by which a harness discovers and calls tools, resources and prompts offered by separate servers.
- **Scope**: Includes the base protocol and its extensions (Apps, Events, Tasks). The full name is an alias (spec N8: the abbreviation is far commoner).
- **Aliases**: Model Context Protocol
- **Example**: [agent-tool-result-transport.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-result-transport.md)
- **Near miss**: An agent SDK's own tool interface: in-process, not a protocol between programs.
- **Kind**: thing
- **Related**: `mcp-server`, `mcp-app`
- **Status**: candidate
- **Warrant**: MCP server 132; mcp-apps/, mcp-events.md (Jonathan's words: "mcps")
- **History**: 2026-11-26 added.

### MCP server (`mcp-server`)

- **Definition**: An MCP server is a program that offers tools, resources or prompts to harnesses over MCP.
- **Scope**: Includes local stdio servers and remote HTTP servers, and the connectors that claude.ai lists.
- **Aliases**: server, connector, MCP integration
- **Example**: [agent-design/keel/tools-and-agents.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/tools-and-agents.md)
- **Near miss**: A plugin: a package that may bundle MCP servers with skills and hooks.
- **Kind**: thing
- **Related**: `mcp`, `plugin`
- **Status**: candidate
- **Warrant**: MCP server 132 in 57 files; connector 47
- **History**: 2026-11-26 added.

### MCP App (`mcp-app`)

- **Definition**: An MCP App is an interactive view that an MCP server supplies as a `ui://` resource for the host to render.
- **Scope**: Includes views defined by SEP-1865. Excludes artefacts a model writes itself (generated HTML pages).
- **Aliases**: MCP Apps, ui:// view
- **Example**: [agent-interactive-views.md](https://github.com/jburnhams/prompts/blob/a531474/agent-interactive-views.md)
- **Near miss**: A Claude Artifact: written by the model, not served by an MCP server.
- **Kind**: thing
- **Related**: `mcp`
- **Status**: candidate
- **Warrant**: mcp-apps/README.md; MCP App 7
- **History**: 2026-11-26 added.

### skill (`skill`)

- **Definition**: A skill is a packaged folder of instructions and files that an agent loads when the description in its manifest matches the task.
- **Scope**: Includes Anthropic Agent Skills and the same format in other harnesses. Excludes the everyday sense of a capability.
- **Aliases**: Agent Skill, SKILL.md
- **Example**: [skills/](https://github.com/jburnhams/prompts/blob/a531474/skills/)
- **Near miss**: A slash command: run when a person types it, not chosen by the model from a description.
- **Kind**: thing
- **Related**: `plugin`
- **Status**: candidate
- **Warrant**: skill 685 in 115 files
- **History**: 2026-11-26 added.

### plugin (`plugin`)

- **Definition**: A plugin is a package that adds skills, commands, hooks, agents or MCP servers to a harness in one install.
- **Scope**: Includes Claude Code plugins and VS Code-style extensions that add agent features.
- **Aliases**: extension, bundle
- **Example**: [agent-tool-surfaces.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-surfaces.md)
- **Near miss**: An MCP server: one source of tools, which a plugin may contain.
- **Kind**: thing
- **Related**: `skill`, `mcp-server`, `hook`
- **Status**: candidate
- **Warrant**: plugin 169; extension 199
- **History**: 2026-11-26 added.

### hook (`hook`)

- **Definition**: A hook is a user-configured command that a harness runs at a named point in a run.
- **Scope**: Includes pre- and post-tool-use hooks and session-start hooks. Excludes the harness's own built-in checks (`rule`).
- **Aliases**: lifecycle hook, callback
- **Example**: [agent-permissions-approval.md](https://github.com/jburnhams/prompts/blob/a531474/agent-permissions-approval.md)
- **Near miss**: Middleware in an SDK: code in the same process, set by the developer rather than the user.
- **Kind**: thing
- **Related**: `plugin`
- **Status**: candidate
- **Warrant**: hook 120 in 44 files
- **History**: 2026-11-26 added.

### sub-agent (`sub-agent`)

- **Definition**: A sub-agent is an agent started by another agent to do part of its task and report back.
- **Scope**: Includes Claude Code's Task sub-agents, workers, forks and delegated runs that return a result to their spawner. Excludes a separate run started by a trigger.
- **Aliases**: subagent, worker, child agent, delegate
- **Example**: [agent-subagent-architectures.md](https://github.com/jburnhams/prompts/blob/a531474/agent-subagent-architectures.md)
- **Near miss**: A second model that checks an action: it decides rather than does work (`second-model`).
- **Kind**: role
- **Broader**: `agent`
- **Related**: `orchestrator`
- **Status**: candidate
- **Warrant**: sub-agent 481, subagent 269
- **History**: 2026-11-26 added; role, not kind (J14, OntoClean §8.3).

### orchestrator (`orchestrator`)

- **Definition**: An orchestrator is an agent that starts sub-agents and owns the run's ending.
- **Scope**: Includes Keel's top-level agent and Claude Code's coordinator mode.
- **Aliases**: coordinator, lead agent, parent agent, main agent
- **Example**: [agent-design/keel/taxonomy.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/taxonomy.md)
- **Near miss**: A dispatcher or pipeline: fixed code that routes work, not an agent.
- **Kind**: role
- **Broader**: `agent`
- **Related**: `sub-agent`
- **Status**: candidate
- **Warrant**: orchestrator 281; coordinator 26
- **History**: 2026-11-26 added.

### system prompt (`system-prompt`)

- **Definition**: A system prompt is a block of fixed text that a harness puts before the conversation to configure an agent.
- **Scope**: Includes generated blocks (environment, tool guidance). Excludes repo instructions loaded from files (`context-file`).
- **Aliases**: base prompt, system message, instructions
- **Example**: [agent-design/system-prompts.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/system-prompts.md)
- **Near miss**: A context file: written by a repo's owners and loaded per repo, not part of the harness.
- **Kind**: thing
- **Related**: `context-window`
- **Status**: candidate
- **Warrant**: system prompt 258 in 89 files
- **History**: 2026-11-26 added.

### context window (`context-window`)

- **Definition**: A context window is a body of input that a model is given on one request, up to its token limit.
- **Scope**: Includes the system prompt, tool definitions, conversation, tool results and injected text. Excludes the area value `context`, which is about how it is filled.
- **Aliases**: model context, prompt
- **Example**: [agent-context-compaction.md](https://github.com/jburnhams/prompts/blob/a531474/agent-context-compaction.md)
- **Near miss**: Memory: kept across runs and loaded into the context window only when retrieved.
- **Kind**: thing
- **Related**: `system-prompt`, `compaction`
- **Status**: candidate
- **Warrant**: context window 69 in 29 files
- **History**: 2026-11-26 added.

### context file (`context-file`)

- **Definition**: A context file is a file in a repo that tells agents how to work there and that a harness loads into the context window.
- **Scope**: Includes AGENTS.md, CLAUDE.md, GEMINI.md, .cursorrules and nested per-folder files.
- **Aliases**: AGENTS.md, CLAUDE.md, instruction file, rules file, conventions file
- **Example**: [agent-context-file-loading.md](https://github.com/jburnhams/prompts/blob/a531474/agent-context-file-loading.md)
- **Near miss**: A skill: loaded only when its description matches, not whenever the repo is open.
- **Kind**: thing
- **Related**: `system-prompt`
- **Status**: candidate
- **Warrant**: AGENTS.md 425; CLAUDE.md 102; "context file" 18
- **History**: 2026-11-26 added; label chosen because the repo has no single word (harvest synonym set 5).

### compaction (`compaction`)

- **Definition**: A compaction is a happening in which a harness replaces older parts of the context window with a shorter form to stay within its limit.
- **Scope**: Includes summarisation, truncation of old tool results, and anchored or incremental summaries.
- **Aliases**: summarisation, context compression, auto-compact
- **Example**: [agent-context-compaction.md](https://github.com/jburnhams/prompts/blob/a531474/agent-context-compaction.md)
- **Near miss**: Memory consolidation: between runs, for later runs, not to fit this one.
- **Kind**: happening
- **Related**: `context-window`
- **Status**: candidate
- **Warrant**: compaction 501 in 63 files
- **History**: 2026-11-26 added.

### memory (`memory`)

- **Definition**: A memory is a body of information that an agent system keeps across runs so that later runs can use it.
- **Scope**: Includes curated notes, learnings, episodic logs and their stores. Excludes the context window of one run.
- **Aliases**: long-term memory, learnings
- **Example**: [agent-memory-learning.md](https://github.com/jburnhams/prompts/blob/a531474/agent-memory-learning.md)
- **Near miss**: A transcript: a record of one run, which becomes memory only if something extracts from it.
- **Kind**: thing
- **Related**: `context-window`
- **Status**: candidate
- **Warrant**: memory 1,215 in 94 files
- **History**: 2026-11-26 added.

### steer (`steer`)

- **Definition**: A steer is a message that a harness or second model adds during a run to redirect the agent.
- **Scope**: Includes system reminders, nudges, loop warnings and a trajectory judge's feedback.
- **Aliases**: nudge, system reminder, reminder, system-reminder
- **Example**: [agent-run-steering.md](https://github.com/jburnhams/prompts/blob/a531474/agent-run-steering.md)
- **Near miss**: An approval prompt: asks a person, does not redirect the model.
- **Kind**: thing
- **Status**: candidate
- **Warrant**: steer 103; nudge 108; system-reminder 46
- **History**: 2026-11-26 added.

### approval (`approval`)

- **Definition**: An approval is a happening in which a person or a rule allows an action before it runs.
- **Scope**: Includes permission prompts, allow lists applied by code and an auto-mode classifier's allow.
- **Aliases**: permission prompt, confirmation, consent
- **Example**: [agent-permissions-approval.md](https://github.com/jburnhams/prompts/blob/a531474/agent-permissions-approval.md)
- **Near miss**: A review of finished work: after the fact, `code-review`.
- **Kind**: happening
- **Related**: `permission-mode`
- **Status**: candidate
- **Warrant**: approval 759 in 113 files
- **History**: 2026-11-26 added.

### permission mode (`permission-mode`)

- **Definition**: A permission mode is a setting that fixes which actions need an approval.
- **Scope**: Includes Claude Code's default, plan, accept-edits and auto modes, Codex's approval modes. Excludes other uses of "mode" (Forge's `mode: implement`, Roo Code's personas), which are not this term.
- **Aliases**: approval mode, approval policy
- **Example**: [agent-permissions-approval.md](https://github.com/jburnhams/prompts/blob/a531474/agent-permissions-approval.md)
- **Near miss**: Plan mode as a way of working: it also restricts tools, but its point is planning first.
- **Kind**: thing
- **Related**: `approval`
- **Status**: candidate
- **Warrant**: approval mode 17; permission mode 11; plan mode 81; auto mode 31
- **History**: 2026-11-26 added; "mode" alone is a homonym (harvest 2) and gets no entry.

### sandbox (`sandbox`)

- **Definition**: A sandbox is an isolated environment that limits what a run's tool calls can reach.
- **Scope**: Includes OS sandboxes, containers, micro-VMs and in-process interpreters for code mode.
- **Aliases**: isolation, container
- **Example**: [agent-local-compute.md](https://github.com/jburnhams/prompts/blob/a531474/agent-local-compute.md)
- **Near miss**: A permission mode: decides what is asked, not what can be reached.
- **Kind**: thing
- **Status**: candidate
- **Warrant**: sandbox 457 in 102 files
- **History**: 2026-11-26 added.

### handoff (`handoff`)

- **Definition**: A handoff is a happening in which a run passes its work to a person or another run instead of finishing it.
- **Scope**: Includes Keel's `HandOff` ending and escalation to a human.
- **Aliases**: hand-off, hand off, escalation
- **Example**: [agent-permissions-approval.md](https://github.com/jburnhams/prompts/blob/a531474/agent-permissions-approval.md)
- **Near miss**: A sub-agent's report: returned to its spawner, which carries on.
- **Kind**: happening
- **Status**: candidate
- **Warrant**: handoff 261; hand-off 17
- **History**: 2026-11-26 added.

### trigger (`trigger`)

- **Definition**: A trigger is a configured source of events that starts a run or a pipeline without a person starting it.
- **Scope**: Includes schedules, webhooks, MCP events and run outcomes.
- **Aliases**: automation, schedule
- **Example**: [agent-design/keel/triggers-and-runs.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/triggers-and-runs.md)
- **Near miss**: A hook: runs a command inside a run, does not start one.
- **Kind**: thing
- **Related**: `pipeline`
- **Status**: candidate
- **Warrant**: trigger 306 in 80 files
- **History**: 2026-11-26 added.

### pipeline (`pipeline`)

- **Definition**: A pipeline is a defined graph of runs joined by edges, so that one run's outcome starts the next.
- **Scope**: Includes Keel's pipelines and Forge's plan-to-implement chain.
- **Aliases**: workflow, chain
- **Example**: [agent-design/keel/pipelines.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/pipelines.md)
- **Near miss**: An orchestrator: an agent deciding at run time, not a defined graph.
- **Kind**: thing
- **Related**: `trigger`
- **Status**: candidate
- **Warrant**: pipeline 390; workflow 320
- **History**: 2026-11-26 added.

### eval (`eval`)

- **Definition**: An eval is a set of tasks with scoring that measures how well an agent or model does a kind of work.
- **Scope**: Includes a project's own eval suites. Excludes checks inside a run (`self-verification`).
- **Aliases**: evaluation, evals, eval suite, test suite
- **Example**: [agent-design/eval.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/eval.md)
- **Near miss**: Self-verification: the agent checking its own work during a run.
- **Kind**: thing
- **Related**: `benchmark`, `self-verification`
- **Status**: candidate
- **Warrant**: eval 182 in 57 files (Jonathan's words: "evals")
- **History**: 2026-11-26 added.

### benchmark (`benchmark`)

- **Definition**: A benchmark is an eval published for comparing agents or models across groups.
- **Scope**: Includes SWE-bench, Terminal-Bench, DAB.
- **Aliases**: leaderboard
- **Example**: [agent-data-analysis.md](https://github.com/jburnhams/prompts/blob/a531474/agent-data-analysis.md)
- **Near miss**: A project's own eval suite: not published for comparison.
- **Kind**: thing
- **Broader**: `eval`
- **Status**: candidate
- **Warrant**: benchmark 129; SWE-bench 90
- **History**: 2026-11-26 added.

### self-verification (`self-verification`)

- **Definition**: A self-verification is a happening in which an agent checks its own work before it ends.
- **Scope**: Includes running tests, completion gates the agent must pass, and re-reading its diff. Excludes another model reviewing it (`second-model`).
- **Aliases**: self-check, self-review
- **Example**: [agent-self-verification.md](https://github.com/jburnhams/prompts/blob/a531474/agent-self-verification.md)
- **Near miss**: A completion gate run by code: the check is a rule; self-verification is when the agent itself checks.
- **Kind**: happening
- **Related**: `eval`
- **Status**: candidate
- **Warrant**: self-verification 137 in 42 files
- **History**: 2026-11-26 added.

### code review (`code-review`)

- **Definition**: A code review is a happening in which a change is checked for faults before it is merged.
- **Scope**: Includes review by people, by review bots and by reviewer sub-agents. Excludes the agent checking its own work (`self-verification`).
- **Aliases**: PR review, review
- **Example**: [code-review-approaches.md](https://github.com/jburnhams/prompts/blob/a531474/code-review-approaches.md)
- **Near miss**: Self-review: the same agent, the same run.
- **Kind**: happening
- **Related**: `self-verification`
- **Status**: candidate
- **Warrant**: reviewer 445; code-review-approaches.md
- **History**: 2026-11-26 added.
