# Rater prompt: prompts taxonomy, stage 2 (context area), round 2

You are classifying 30 items for a taxonomy agreement test. Use only the definitions below; do not look anything up, do not read any files, and do not use other knowledge of the repo they come from.

Each item is one section of a research repo about how AI agent products and harnesses are built (Claude Code, Codex, Gemini CLI, Goose, MCP, agent SDKs) and of the designs of the repo owner's own agent platform (Keel, with configurations Forge and Lens). An item is the section's heading, the first lines under it (`gist`), and the file it is in (`from`).

For every item, answer all four questions with exactly one value each. If no value fits, still pick the closest one and write `unsure` plus a few words in the note column.

Rules:
- Classify the mechanism, approach or design choice the section describes, not the document it is in. The `from` column is part of the item.
- in_area: `yes` if the mechanism is about the `context` area as defined below (what the model is given to read and what is kept for later); `no` if another area's definition fits it better (for example prompt caching is `model`, a tool's definition or schema is `tool`, a mid-run text whose job is to redirect the model is `control`, reporting what was loaded is `operations`). If `no`, still answer the other three with the closest values.
- operation: the change the mechanism makes to what the model reads. Choosing and loading content, and writing what a fixed prompt says, is `supply`; where chosen text sits and how much it counts is `framing`; making content already there shorter or removing it is `reduction`; keeping content so a later request or run can use it is `recording`.
- content: where the text the mechanism handles came from. Written in advance to tell the model how to act: `instruction-text`. Kept from earlier work: `kept-knowledge` (a fact a run learned stays `kept-knowledge` even when a person writes it into a context file). This conversation's own record, including its summaries: `run-history`.
- reach: the widest set of requests and runs that read the same text. For a recording (a memory write, a digest, a promotion), the runs that will read what it keeps, not the run it came from. Text shipped with the harness or an agent configuration (a product's own system prompt, its reviewer or delegate prompt, a built-in reminder) is `built-in-scope`. If a section describes stores with several reaches, take the widest it describes. If it does not say how widely a store, file or server is shared, take `project-scope` unless the text says it follows a person (`user-scope`) or a team (`organization-scope`).
- If an item describes several mechanisms, classify the first one named; if it surveys several approaches without naming one first, classify the one it recommends, or pick the closest and mark `unsure`.

Answer as CSV only, with this header and one row per item, in the items' order. Quote any note that contains a comma.

```
id,in_area,operation,content,reach,note
```

## The questions and their values

- **in_area**: Is it about the `context` area? Values: `yes`, `no`
- **operation**: What does it do to the context? Values: `reduction`, `supply`, `framing`, `recording`
- **content**: What kind of text is it about? Values: `run-history`, `kept-knowledge`, `instruction-text`
- **reach**: How far does that text reach? Values: `user-scope`, `request-scope`, `conversation-scope`, `built-in-scope`, `project-scope`, `organization-scope`

## The areas (for `in_area`)

### context (`context`)

- **Definition**: Context is an area of an agent system that covers what the model is given to read and what is kept for later.
- **Scope**: Includes system prompts, context files (AGENTS.md, CLAUDE.md), injected environment text, compaction and summaries, memory across runs. Excludes mid-run text that steers the model (`control`).
- **Aliases**: context engineering
- **Near miss**: A reminder the harness injects when the model loops: it is text in the context, but its job is to redirect, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

### output (`output`)

- **Definition**: Output is an area of an agent system that covers what a run produces for people to read or use.
- **Scope**: Includes turn text and its style, narration, titles, generated files and artefacts, interactive views, tables and charts, and how they are delivered. Excludes records kept for operators (`operations`).
- **Aliases**: deliverable, response, artefact
- **Near miss**: A transcript of the run: it is produced, but for operators and analysis, so it is `operations`.
- **Kind**: thing
- **Facet**: `area`

### operations (`operations`)

- **Definition**: Operations is an area of an agent system that covers running agents and keeping their records.
- **Scope**: Includes telemetry, traces and transcripts, storage and dashboards, version control and commits, local compute, provenance of content, deployment. Excludes checking the quality of the work (`verification`).
- **Aliases**: ops, observability
- **Near miss**: A loop detector that stops a run: it reads telemetry, but stopping decides, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

### control (`control`)

- **Definition**: Control is an area of an agent system that covers whether an action may happen and what stops or redirects a run.
- **Scope**: Includes approval and permission modes, risk levels, sandboxing, blocking monitors, steering and nudges, recovery after errors and limits, and how a run is allowed to end. Whatever decides *whether* goes here. Excludes where work goes next (`coordination`) and checking the quality of finished work (`verification`).
- **Aliases**: safety, permissions, guardrails
- **Near miss**: Routing a sub-agent's approval request to the parent session: the routing is `coordination`, but refusing an answer from the wrong session decides whether, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

### model calling (`model`)

- **Definition**: Model calling is an area of an agent system that covers how models are called and chosen.
- **Scope**: Includes providers and their wire formats (dialects), routing between models, reasoning effort and thinking budgets, prompt caching, and what happens when a model's response is broken. Excludes what the model is told (`context`) and which tools it is offered (`tool`).
- **Aliases**: model access, LLM access, inference
- **Near miss**: Deferring tool definitions so the cache survives: the change is to how the request is assembled, so it is `model` when the point is the cache and `tool` when the point is which tools are loaded.
- **Kind**: thing
- **Facet**: `area`

### coordination (`coordination`)

- **Definition**: Coordination is an area of an agent system that covers how agents and runs are arranged and where work goes next.
- **Scope**: Includes sub-agents and orchestrators, triggers, pipelines and their edges, hand-offs between runs, entrypoints and the kinds of run a system offers. Excludes deciding whether an action is allowed (`control`).
- **Aliases**: orchestration, multi-agent
- **Near miss**: A tool that ends a run: choosing which ending applies is `control`; the follow-up run it dispatches is `coordination`.
- **Kind**: thing
- **Facet**: `area`

### verification (`verification`)

- **Definition**: Verification is an area of an agent system that covers checking whether the work is right.
- **Scope**: Includes self-verification and completion gates, code review of a change, evals, benchmarks and their graders. Excludes checks on whether an action may happen (`control`).
- **Aliases**: checking, quality checks
- **Near miss**: A blocking monitor that refuses a risky command: it checks an action before it happens, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

### tool use (`tool`)

- **Definition**: Tool use is an area of an agent system that covers what the model can do and how its calls and their results move.
- **Scope**: Includes the tool surface, tool implementations, call and result formats, large results and refs, deferred tool loading, code mode, MCP servers and their protocol. Excludes whether a call is allowed (`control`).
- **Aliases**: tooling
- **Near miss**: An approval prompt before a shell command: the command is a tool, but asking whether it may run is `control`.
- **Kind**: thing
- **Facet**: `area`

## Definitions of the values

### run history (`run-history`)

- **Definition**: Run history is a part of the context window that records what has happened so far in the current conversation.
- **Scope**: Includes messages, tool calls and results, images and screenshots, todo lists and plans, compaction summaries, and a prior attempt handed to the next run of the same task.
- **Aliases**: conversation history, history
- **Near miss**: A transcript kept after the run for analysis (`operations` area).
- **Kind**: thing
- **Facet**: `content`

### conversation scope (`conversation-scope`)

- **Definition**: A conversation scope is a reach of content that lasts while one conversation continues.
- **Scope**: Includes a run's history, its plan and todos, compaction summaries, a session resumed after a restart, a sub-agent's own context, and a prior attempt handed to the next run of the same task. Ends when nothing carries the content into a new conversation.
- **Aliases**: session level, run-scoped, session-scoped
- **Near miss**: A memory written for later sessions, even when it is distilled from this one (`project-scope`, `user-scope` or `organization-scope`).
- **Kind**: property
- **Facet**: `reach`

### project scope (`project-scope`)

- **Definition**: A project scope is a reach of content that applies to every run in one repository or project.
- **Scope**: Includes committed context files, repo and path learnings, a project's private memory folder kept for one developer, and a team's notes kept in the repo. The default when a section does not say how widely a store or server is shared.
- **Aliases**: repo scope, repo level, project level
- **Near miss**: A user's global CLAUDE.md, which follows the person into every project (`user-scope`).
- **Kind**: property
- **Facet**: `reach`

### instruction text (`instruction-text`)

- **Definition**: Instruction text is a part of the context window that was written in advance to tell the model how to act.
- **Scope**: Includes system prompts and their generated blocks, context files, skill bodies and catalogs, MCP server instructions, format notes, and reminders the harness injects. Excludes facts a run learned, even when stored in a context file (`kept-knowledge`).
- **Aliases**: guidance, prompt text
- **Near miss**: A learning: written by or for a run from what happened, not in advance.
- **Kind**: thing
- **Facet**: `content`

### request scope (`request-scope`)

- **Definition**: A request scope is a reach of content that lasts for one model request.
- **Scope**: Includes request-scoped reminders, conditional format notes added only when a feature is present, and the one-off prompt of a helper call.
- **Aliases**: per-request, request-scoped
- **Near miss**: A reminder kept in the conversation once sent (`conversation-scope`).
- **Kind**: property
- **Facet**: `reach`

### kept knowledge (`kept-knowledge`)

- **Definition**: Kept knowledge is a part of the context window that comes from earlier work and was kept for later use.
- **Scope**: Includes memories, learnings, notes, decision records, consolidated summaries of past sessions, and a fact a run learned that a person then wrote into a context file.
- **Aliases**: learned content, prior knowledge
- **Near miss**: A compaction summary of the current run: it is this run's own record (`run-history`).
- **Kind**: thing
- **Facet**: `content`

### supply (`supply`)

- **Definition**: A supply is an operation on the context window that decides what content goes in front of the model and puts it there.
- **Scope**: Includes what a system prompt says, finding and loading context files, choosing which memories to retrieve, conditional and just-in-time loading, and text the harness injects mid-run to inform the model. Excludes where and how the text is presented once chosen (`framing`).
- **Aliases**: loading, injection, context assembly
- **Near miss**: A memory write: it stores content for a later run (`recording`); only the later read is a supply.
- **Kind**: happening
- **Facet**: `operation`

### framing (`framing`)

- **Definition**: A framing is an operation on the context window that sets where chosen content sits and how much it counts.
- **Scope**: Includes position in the prompt (prefix, tail, first user message), envelopes and nonces, the authority a file is given (overrides, subordinate, untrusted data), precedence between sources, escaping, and whether a learning may only inform or may veto.
- **Aliases**: placement, envelope, precedence
- **Near miss**: Choosing which files to load at all (`supply`). Keeping the cached prefix stable for cost: `model` area, unless the change is to where the text goes.
- **Kind**: happening
- **Facet**: `operation`

### user scope (`user-scope`)

- **Definition**: A user scope is a reach of content that follows one person into every project.
- **Scope**: Includes a user's global context file, preferences, and a memory store kept per person rather than per repo.
- **Aliases**: user level, global, personal
- **Near miss**: A team or org policy every member's runs read (`organization-scope`).
- **Kind**: property
- **Facet**: `reach`

### reduction (`reduction`)

- **Definition**: A reduction is an operation on the context window that makes content already there shorter or removes it.
- **Scope**: Includes compaction and summaries, truncating tool results and files to a budget, dropping old images, pruning, and isolating a sub-agent's history from its parent's.
- **Aliases**: shrinking, context reduction
- **Near miss**: Memory consolidation: it shortens a store between runs, for later runs (`recording`), not the content of this one.
- **Kind**: happening
- **Facet**: `operation`

### built-in scope (`built-in-scope`)

- **Definition**: A built-in scope is a reach of content that ships with a harness or an agent configuration and applies to every run of it.
- **Scope**: Includes a product's own system prompt, its reviewer and delegate prompts, built-in reminders and tool guidance, and a Keel configuration's fixed prompt blocks. Excludes files a user or team adds (`project-scope`, `user-scope`, `organization-scope`).
- **Aliases**: harness scope, shipped prompt, configuration scope
- **Near miss**: An org policy file every member's runs load (`organization-scope`): someone in the org wrote it, the product did not ship it.
- **Kind**: property
- **Facet**: `reach`

### recording (`recording`)

- **Definition**: A recording is an operation on the context window that keeps content from it so that a later request or run can use it.
- **Scope**: Includes memory writes by the working model, a background agent or a person, notes and scratchpads, retrospectives, consolidation, promotion, write gates, staleness and forgetting rules for a store.
- **Aliases**: memory write, write-back, capture
- **Near miss**: Reading a memory back into a later run (`supply`). A transcript the harness saves of every run: `operations`, until something extracts from it.
- **Kind**: happening
- **Facet**: `operation`

### organization scope (`organization-scope`)

- **Definition**: An organization scope is a reach of content that applies to the runs of many people in a team or organization.
- **Scope**: Includes org policy files, team memory, a vendor-side knowledge library keyed to an org, and a platform-wide memory resource.
- **Aliases**: org level, team level, organisation scope
- **Near miss**: Content shared by several of one person's projects (`user-scope`).
- **Kind**: property
- **Facet**: `reach`

## Items

```csv
id,item,gist,from
ch01,Review-mode system prompts (two shapes),"Review runs come in two harness-selected shapes sharing every wire format, the validator stage, and the reviewer core (`review.md` §6):",agent-design/system-prompts.md
ch02,What it is for,"A hands-off agent that hits a broken tool, a misleading tool description, a dependency whose documented behaviour is wrong, or a conventions section that contradicts the code has, in this design as it stands, exactly two options:",agent-design/memory.md
ch03,"(b2) The working agent authors a *skill* on demand, with no distillation engine",Hermes's `/learn` is a fourth shape that fits neither (a) nor (b):,agent-memory-learning.md
ch04,"The envelope, and the nonce","<conventions tier=""repo"" path=""{{path}}"" rev=""{{sha}}"" nonce=""{{nonce}}""> {{ file body, verbatim }} </conventions-{{nonce}}> <conventions tier=""org"" binding=""policy"" id=""{{id}}"" ref=""{{source.ref}}"" derived=""{{derivation.method}}"" nonce=""{{nonce}}""> {{ section body, verbatim }} </conventions-{{nonce}}> One tag for all three tiers, disting",agent-design/context-files.md
ch05,Which revision? (and: from which repository?),"A question with a uniform and slightly uncomfortable answer. *No loader in this collection is revision-aware. None takes a git ref, reads a blob from the index, or records the SHA a file came from. Every one of them walks the filesystem it is pointed at.",agent-context-file-loading.md
ch06,"The cost, stated plainly","Adding a machine-written tier breaks a property the service currently has: *a resolution is no longer a pure function of `(repo, ref, team)`. Two runs at the same ref, a day apart, can legitimately get different learned sections.",agent-design/memory.md
ch07,When it runs: six trigger points,"1. Mid-task, whenever the model notices something — Windsurf, Cursor, Augment, Goose, Qoder, Claude Code auto memory. The advantage is that the evidence is still in context; the cost is that the model is judging durability from a single moment. 2.",agent-memory-learning.md
ch08,Caching: every tier is a repo at a ref,"Org and team standards live in repositories too — located by convention or by configuration — which collapses a problem that looked awkward. Every tier is `(source repo, ref)`, and the service can see each source repo's latest ref cheaply, so:",agent-design/context-files.md
ch09,"Hooks and plugins: assembled context, with weaker framing than files","Codex's context module is the clearest case of prompt-as-assembly rather than prompt-as-document — 45 fragment types, each a `ContextualUserFragment` with its own role, content kind and marker pair. The ones relevant here:",agent-context-file-loading.md
ch10,`Retrospect` — in-session capture,"A tool available to coding and review runs after their work is done and before `Complete`, producing candidates, not learnings. { ""name"": ""Retrospect"", ""description"": ""Record one candidate learning from this run, before completing. Candidates are proposals, not memories:",agent-design/memory.md
ch11,"(a) The working model writes, inline, as it works","The model calls a tool mid-task. Variants differ mostly on how eager they're told to be: Maximally eager, no permission needed — Windsurf's `<memory_system>`: ""As soon as you encounter important information or context, proactively use the create_memory tool...",agent-memory-learning.md
ch12,"The atomic unit is a section, not a document","A single authored document mixes bindings: its security section is non-negotiable, its formatting section is a preference. Making the document* the unit would force organisations to split every document along a line nobody writes documents along.",agent-design/context-files.md
ch13,Where the walk starts and stops,Two details worth stealing. Codex documents an explicit opt-out: an empty `project_root_markers` list disables parent traversal without disabling the file.,agent-context-file-loading.md
ch14,"Three channels, and why they are three","The single most common failure in the field's memory systems is putting things in a store that nothing will ever retrieve. Sorting by addressee separates them cleanly, and the three answers want different machinery:",agent-design/memory.md
ch15,Hermes Agent's memory (read from source),"`NousResearch/hermes-agent` `2b31d7b2` (2026-11-02), `website/docs/user-guide/features/{memory,memory-providers}.md`, `agent/{background_review,curator}.py`, `tools/memory_tool_store.py`. The earlier Hermes pass (2026-08-11) read its read-tool eval and `/learn`; this one read its memory.",agent-memory-learning.md
ch16,"Three tiers, one source","*All three tiers arrive from the context service, resolved at task start. Forge reads no conventions off any filesystem — not the runner's, and not the checkout's. That is a separation of concerns rather than a distrust of the working tree:",agent-design/context-files.md
ch17,"Beyond files: MCP, skills, hooks and plugins","Everything above is about *files on disk, read at session start*. Four other channels put instruction text into the same prompts, and three of them can do it mid-session. They are worth separating out, because they answer a question the file loaders cannot:",agent-context-file-loading.md
ch18,"Staleness, computed rather than declared","Two mechanisms, both cheap, and the second is available to us and to nobody else in the field. *Age in words, not timestamps. Claude Code computes elapsed days from `mtime` and renders `""47 days ago""`, with the reasoning in the source:",agent-design/memory.md
ch19,(b) A separate background agent reads finished transcripts,"Four independent implementations of the same idea, none of which existed in this collection's earlier passes. This is the strongest convergence in this doc:",agent-memory-learning.md
ch20,Normalisation relocates an interpretation; it does not add one,"It is tempting to treat ""a model rewrote some of this policy"" as a new risk that needs a human gate. It is worth being precise about why that framing is wrong here, because it changes what the contract has to do. *The interpretation happens either way.",agent-design/context-files.md
ch21,Templating: there is none,"A clean negative result. No harness in this collection treats the repository's context file as a template. No `{{var}}` interpolation, no conditionals, no includes beyond the `@path` transclusion above, no environment-variable expansion inside the file body. The file is inert text.",agent-context-file-loading.md
ch22,"4b-i. Claim strength: the gate decides whether, the wording decides how far","Added 2026-09-12. The gates above are all *admission* tests — is this worth recording at all. They say nothing about how broadly the admitted record may be *worded*, and that is a separate leak with the same consequence.",agent-design/memory.md
ch23,Nobody is doing RAG over agent memory,"Qualified 2026-11-02: true of the coding and review harnesses and of curated memory everywhere, but not of always-running and memory-first agents, which search a large episodic layer with hybrid or vector retrieval.",agent-memory-learning.md
ch24,What the file may instruct (and the review-mode reversal),"Two paragraphs of harness-authored framing precede the blocks. They differ by mode, and the difference is the point. The framing below is written for the repo tier. Org and team documents get the same scope sentence and the same envelope, plus one line naming their binding:",agent-design/context-files.md
ch25,"Order, and the gap between claimed and structural precedence","*Everyone concatenates root-first, deeper-last. Codex reverses its ancestor list; Gemini CLI `unshift`s; Claude Code iterates `dirs.reverse()`; Goose reverses. Nobody puts the nearest file first.",agent-context-file-loading.md
ch26,Learnings arrive in the resolution,"No `<learnings>` envelope tag, no read tool, no detail tier. Learned sections arrive in `sections[]` with everything else, subject to the same budget (`context-files.md` §2), the same nonce envelope (§4), the same inlining rules (§8) and the same run record (§10).",agent-design/memory.md
ch27,Levels: what scope does a memory belong to?,"The single most useful lens on this topic, and the one most sources get to eventually: a fact learned in a session belongs at exactly one of several scopes, and picking the wrong one is what makes memory systems annoying.",agent-memory-learning.md
ch28,Provenance: path and revision,"Every block carries `path` and `rev`: <conventions path=""src/api/AGENTS.md"" rev=""a1b2c3d""> `rev` is the commit the *file content* was read at — `base_sha` in review mode (§5), the dispatched branch's head in coding mode. Not the file's last-modified commit:",agent-design/context-files.md
ch29,The negative sharpens: a harness with an escaper that doesn't point it here,"The clean negative above survives a twelfth reading, but OpenClaw (read from source 2026-08-31) changes what it *means*. It is the first harness in this set that ships a general-purpose escaping wrapper — and still injects its context files raw.",agent-context-file-loading.md
ch30,"`blocker` suspends, and it reuses machinery that exists","At `blocker`, `ReportProblem` is terminal, and the task suspends with a wake predicate on the report's resolution — one more predicate kind alongside `medium.md` §4c's `jira` / `build` / `pr` / `timer`. Suspension mechanics carry over from `formats.md` §5 unchanged:",agent-design/memory.md
```
