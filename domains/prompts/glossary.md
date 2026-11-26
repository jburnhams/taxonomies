# Prompts taxonomy: glossary

**In one line**: one entry per concept in the prompts repo, with the word to use, the other
words people use for it, a definition, an example and a near miss.

**In plain words**: when you write in the prompts repo, use the heading word of the entry.
If you reach for one of its aliases, it points you here. Everything here is `candidate`
until stage 1 passes its rounds (spec G3).

**Status**: draft, 2026-11-26. Holds the values of facet set A (recommended, awaiting
Jonathan's choice in [`facets.md`](./facets.md)) so the round-1 kit can be built. The
kernel terms (agent, harness, run, turn, tool, ...) follow J14, the decision on what
"agent" means. Field rules: [`design/spec.md` §4](../../design/spec.md#4-glossarymd).
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
4. **`operations`** is flagged by T3 as a possible plural; it is a mass noun here
   (as in "IT operations"), kept.

## Area values (`area`)

### model (`model`)

- **Definition**: Model is an area of an agent system that covers how models are called and chosen.
- **Scope**: Includes providers and their wire formats (dialects), routing between models, reasoning effort and thinking budgets, prompt caching, and what happens when a model's response is broken. Excludes what the model is told (`context`) and which tools it is offered (`tool`).
- **Aliases**: LLM, model access, inference
- **Example**: [agent-prompt-cache-health.md](https://github.com/jburnhams/prompts/blob/a531474/agent-prompt-cache-health.md), what moves a cached prefix.
- **Near miss**: Deferring tool definitions so the cache survives: the change is to how the request is assembled, so it is `model` when the point is the cache and `tool` when the point is which tools are loaded.
- **Kind**: thing
- **Facet**: `area`
- **Status**: candidate
- **Warrant**: model 3,759 uses in 210 files; LLM 308 (Jonathan's words: "llm")
- **History**: 2026-11-26 added.

### tool (`tool`)

- **Definition**: Tool is an area of an agent system that covers what the model can do and how its calls and their results move.
- **Scope**: Includes the tool surface, tool implementations, call and result formats, large results and refs, deferred tool loading, code mode, MCP servers and their protocol. Excludes whether a call is allowed (`control`).
- **Aliases**: tools, tool use, MCP
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
- **Aliases**: context window, memory, prompt
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
- **Aliases**: evaluation, eval, evals, review, testing
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
- **Aliases**: ops, observability, telemetry
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
- **Aliases**: harness, code, deterministic check, static rule, policy
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
- **Aliases**: completion, finish, handoff
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
