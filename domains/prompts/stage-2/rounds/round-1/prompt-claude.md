# Rater prompt: prompts taxonomy, stage 2 (context area), round 1

You are classifying 30 items for a taxonomy agreement test. Use only the definitions below; do not look anything up, do not read any files, and do not use other knowledge of the repo they come from.

Each item is one section of a research repo about how AI agent products and harnesses are built (Claude Code, Codex, Gemini CLI, Goose, MCP, agent SDKs) and of the designs of the repo owner's own agent platform (Keel, with configurations Forge and Lens). An item is the section's heading, the first lines under it (`gist`), and the file it is in (`from`).

For every item, answer all four questions with exactly one value each. If no value fits, still pick the closest one and write `unsure` plus a few words in the note column.

Rules:
- Classify the mechanism, approach or design choice the section describes, not the document it is in. The `from` column is part of the item.
- in_area: `yes` if the mechanism is about the `context` area as defined below (what the model is given to read and what is kept for later); `no` if another area's definition fits it better (for example prompt caching is `model`, a tool's definition or schema is `tool`, a mid-run text whose job is to redirect the model is `control`, reporting what was loaded is `operations`). If `no`, still answer the other three with the closest values.
- operation: the change the mechanism makes to what the model reads. Choosing and loading content, and writing what a fixed prompt says, is `supply`; where chosen text sits and how much it counts is `framing`; making content already there shorter or removing it is `reduction`; keeping content so a later request or run can use it is `recording`.
- content: where the text the mechanism handles came from. Written in advance to tell the model how to act: `instruction-text`. Kept from earlier work: `kept-knowledge` (a fact a run learned stays `kept-knowledge` even when a person writes it into a context file). This conversation's own record, including its summaries: `run-history`.
- reach: the widest set of requests and runs that read the same text. If a section describes stores with several reaches, take the widest it describes; if it states none, take where that kind of text usually lives (a context file in a repo: `project-scope`).
- If an item describes several mechanisms, classify the first one named; if it surveys several approaches without naming one first, classify the one it recommends, or pick the closest and mark `unsure`.

Answer as CSV only, with this header and one row per item, in the items' order. Quote any note that contains a comma.

```
id,in_area,operation,content,reach,note
```

## The questions and their values

- **in_area**: Is it about the `context` area? Values: `yes`, `no`
- **operation**: What does it do to the context? Values: `reduction`, `recording`, `framing`, `supply`
- **content**: What kind of text is it about? Values: `run-history`, `instruction-text`, `kept-knowledge`
- **reach**: How far does that text reach? Values: `user-scope`, `project-scope`, `organization-scope`, `conversation-scope`, `request-scope`

## The areas (for `in_area`)

### operations (`operations`)

- **Definition**: Operations is an area of an agent system that covers running agents and keeping their records.
- **Scope**: Includes telemetry, traces and transcripts, storage and dashboards, version control and commits, local compute, provenance of content, deployment. Excludes checking the quality of the work (`verification`).
- **Aliases**: ops, observability
- **Near miss**: A loop detector that stops a run: it reads telemetry, but stopping decides, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

### context (`context`)

- **Definition**: Context is an area of an agent system that covers what the model is given to read and what is kept for later.
- **Scope**: Includes system prompts, context files (AGENTS.md, CLAUDE.md), injected environment text, compaction and summaries, memory across runs. Excludes mid-run text that steers the model (`control`).
- **Aliases**: context engineering
- **Near miss**: A reminder the harness injects when the model loops: it is text in the context, but its job is to redirect, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

### tool use (`tool`)

- **Definition**: Tool use is an area of an agent system that covers what the model can do and how its calls and their results move.
- **Scope**: Includes the tool surface, tool implementations, call and result formats, large results and refs, deferred tool loading, code mode, MCP servers and their protocol. Excludes whether a call is allowed (`control`).
- **Aliases**: tooling
- **Near miss**: An approval prompt before a shell command: the command is a tool, but asking whether it may run is `control`.
- **Kind**: thing
- **Facet**: `area`

### verification (`verification`)

- **Definition**: Verification is an area of an agent system that covers checking whether the work is right.
- **Scope**: Includes self-verification and completion gates, code review of a change, evals, benchmarks and their graders. Excludes checks on whether an action may happen (`control`).
- **Aliases**: checking, quality checks
- **Near miss**: A blocking monitor that refuses a risky command: it checks an action before it happens, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

### output (`output`)

- **Definition**: Output is an area of an agent system that covers what a run produces for people to read or use.
- **Scope**: Includes turn text and its style, narration, titles, generated files and artefacts, interactive views, tables and charts, and how they are delivered. Excludes records kept for operators (`operations`).
- **Aliases**: deliverable, response, artefact
- **Near miss**: A transcript of the run: it is produced, but for operators and analysis, so it is `operations`.
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

### control (`control`)

- **Definition**: Control is an area of an agent system that covers whether an action may happen and what stops or redirects a run.
- **Scope**: Includes approval and permission modes, risk levels, sandboxing, blocking monitors, steering and nudges, recovery after errors and limits, and how a run is allowed to end. Whatever decides *whether* goes here. Excludes where work goes next (`coordination`) and checking the quality of finished work (`verification`).
- **Aliases**: safety, permissions, guardrails
- **Near miss**: Routing a sub-agent's approval request to the parent session: the routing is `coordination`, but refusing an answer from the wrong session decides whether, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

## Definitions of the values

### user scope (`user-scope`)

- **Definition**: A user scope is a reach of content that follows one person into every project.
- **Scope**: Includes a user's global context file, preferences, and a memory store kept per person rather than per repo.
- **Aliases**: user level, global, personal
- **Near miss**: A team or org policy every member's runs read (`organization-scope`).
- **Kind**: property
- **Facet**: `reach`

### instruction text (`instruction-text`)

- **Definition**: Instruction text is a part of the context window that was written in advance to tell the model how to act.
- **Scope**: Includes system prompts and their generated blocks, context files, skill bodies and catalogs, MCP server instructions, format notes, and reminders the harness injects. Excludes facts a run learned, even when stored in a context file (`kept-knowledge`).
- **Aliases**: guidance, prompt text
- **Near miss**: A learning: written by or for a run from what happened, not in advance.
- **Kind**: thing
- **Facet**: `content`

### organization scope (`organization-scope`)

- **Definition**: An organization scope is a reach of content that applies to the runs of many people in a team or organization.
- **Scope**: Includes org policy files, team memory, a vendor-side knowledge library keyed to an org, and a platform-wide memory resource.
- **Aliases**: org level, team level, organisation scope
- **Near miss**: Content shared by several of one person's projects (`user-scope`).
- **Kind**: property
- **Facet**: `reach`

### supply (`supply`)

- **Definition**: A supply is an operation on the context window that decides what content goes in front of the model and puts it there.
- **Scope**: Includes what a system prompt says, finding and loading context files, choosing which memories to retrieve, conditional and just-in-time loading, and text the harness injects mid-run to inform the model. Excludes where and how the text is presented once chosen (`framing`).
- **Aliases**: loading, injection, context assembly
- **Near miss**: A memory write: it stores content for a later run (`recording`); only the later read is a supply.
- **Kind**: happening
- **Facet**: `operation`

### run history (`run-history`)

- **Definition**: Run history is a part of the context window that records what has happened so far in the current conversation.
- **Scope**: Includes messages, tool calls and results, images and screenshots, todo lists and plans, compaction summaries, and a prior attempt handed to the next run of the same task.
- **Aliases**: conversation history, history
- **Near miss**: A transcript kept after the run for analysis (`operations` area).
- **Kind**: thing
- **Facet**: `content`

### kept knowledge (`kept-knowledge`)

- **Definition**: Kept knowledge is a part of the context window that comes from earlier work and was kept for later use.
- **Scope**: Includes memories, learnings, notes, decision records, consolidated summaries of past sessions, and a fact a run learned that a person then wrote into a context file.
- **Aliases**: learned content, prior knowledge
- **Near miss**: A compaction summary of the current run: it is this run's own record (`run-history`).
- **Kind**: thing
- **Facet**: `content`

### recording (`recording`)

- **Definition**: A recording is an operation on the context window that keeps content from it so that a later request or run can use it.
- **Scope**: Includes memory writes by the working model, a background agent or a person, notes and scratchpads, retrospectives, consolidation, promotion, write gates, staleness and forgetting rules for a store.
- **Aliases**: memory write, write-back, capture
- **Near miss**: Reading a memory back into a later run (`supply`). A transcript the harness saves of every run: `operations`, until something extracts from it.
- **Kind**: happening
- **Facet**: `operation`

### project scope (`project-scope`)

- **Definition**: A project scope is a reach of content that applies to every run in one repository or project.
- **Scope**: Includes committed context files, repo and path learnings, a project's private memory folder kept for one developer, and a team's notes kept in the repo.
- **Aliases**: repo scope, repo level, project level
- **Near miss**: A user's global CLAUDE.md, which follows the person into every project (`user-scope`).
- **Kind**: property
- **Facet**: `reach`

### reduction (`reduction`)

- **Definition**: A reduction is an operation on the context window that makes content already there shorter or removes it.
- **Scope**: Includes compaction and summaries, truncating tool results and files to a budget, dropping old images, pruning, and isolating a sub-agent's history from its parent's.
- **Aliases**: shrinking, context reduction
- **Near miss**: Memory consolidation: it shortens a store between runs, for later runs (`recording`), not the content of this one.
- **Kind**: happening
- **Facet**: `operation`

### conversation scope (`conversation-scope`)

- **Definition**: A conversation scope is a reach of content that lasts while one conversation continues.
- **Scope**: Includes a run's history, its plan and todos, compaction summaries, a session resumed after a restart, and a sub-agent's own context. Ends when nothing carries the content into a new conversation.
- **Aliases**: session level, run-scoped, session-scoped
- **Near miss**: A memory written for later sessions (`project-scope`, `user-scope` or `organization-scope`).
- **Kind**: property
- **Facet**: `reach`

### framing (`framing`)

- **Definition**: A framing is an operation on the context window that sets where chosen content sits and how much it counts.
- **Scope**: Includes position in the prompt (prefix, tail, first user message), envelopes and nonces, the authority a file is given (overrides, subordinate, untrusted data), precedence between sources, escaping, and whether a learning may only inform or may veto.
- **Aliases**: placement, envelope, precedence
- **Near miss**: Choosing which files to load at all (`supply`). Keeping the cached prefix stable for cost: `model` area, unless the change is to where the text goes.
- **Kind**: happening
- **Facet**: `operation`

### request scope (`request-scope`)

- **Definition**: A request scope is a reach of content that lasts for one model request.
- **Scope**: Includes request-scoped reminders, conditional format notes added only when a feature is present, and the one-off prompt of a helper call.
- **Aliases**: per-request, request-scoped
- **Near miss**: A reminder kept in the conversation once sent (`conversation-scope`).
- **Kind**: property
- **Facet**: `reach`

## Items

```csv
id,item,gist,from
cr01,"Kinds: one vocabulary, three resolutions","*The vocabulary is v1 even though narrowing is not. `kinds` as a context-service narrowing parameter* is reserved (next subsection). The kind vocabulary itself is already load-bearing today, under two other names, and unifying them is worth doing before a third appears:",agent-design/context-files.md
cr02,"Memory scoped to a sub-agent, not just to a project","Claude Code stores memory per agent *type*: `~/.claude/agent-memory/<agentType>/`, `.claude/agent-memory/<agentType>/`, or `.claude/agent-memory-local/<agentType>/`, chosen by a per-agent `memory: 'user' | 'project' | 'local'` setting, each with its own `MEMORY.md`.",agent-tool-implementations.md
cr03,"MCP instructions, and the cache problem that shaped them","The MCP protocol lets a server return an `instructions` string at handshake, and harnesses splice it into the prompt. That is straightforward when every server is connected before the first request.",agent-context-file-loading.md
cr04,General-purpose delegate prompt (coding mode),"Short and role-scoped, per this file's intro — the delegate has no task envelope, no mode, and no Complete/AskUser, so it gets none of the orchestrator prompt's machinery. Closest precedent is Amp's generic `H_R` delegate prompt (`agent-subagent-architectures.md` §3). Tool scope:",agent-design/system-prompts.md
cr05,The digest gate: most runs should produce nothing,"Gemini CLI computes a model-free per-session digest — tool sequence, touched paths, and whether a validation command passed, in ≤160 characters — and routes on it, so ""which of 50 sessions is worth reading"" is answered with no model call (`../agent-memory-learning.md` §2b).",agent-design/memory.md
cr06,"Notes, memory and consolidation are three things","People use ""memory"" for all three. They have different lifetimes and want different machinery.",agent-design/keel/memory.md
cr07,Token budgeting — the numbers,"The specific ask this doc was written to cover in depth. Four sources had concrete, code-confirmed numeric thresholds available; the rest either don't expose fixed numbers in what's captured, or the relevant config lives outside the fetched files.",agent-context-compaction.md
cr08,"What is worth remembering: gates, taxonomies, and anti-rules","Every mature writer prompt is mostly a *filter*, not a format spec. *No-op is the encouraged default. Codex Phase 1:",agent-memory-learning.md
cr09,"Discovery (a specification for the service, not the harness)","Forge does not walk the filesystem for conventions. The context service resolves all three tiers, repo included (§1a), so what follows is the discovery contract *it* implements. It is specified here, in Forge's design, rather than left to the service's own documentation, for two reasons.",agent-design/context-files.md
cr10,The truncation you cannot yet honestly claim,"Two implementation details from the same source, both about reads that stream rather than load the file into memory (OpenCode, Kilo Code and Cline stream too; Claude Code is scored as not doing so): *Defer the decision at a chunk boundary.",agent-tool-implementations.md
cr11,"Budgets, truncation, and staleness","*Only Codex has a byte budget on the context-file hierarchy: `project_doc_max_bytes`, default 32 KiB, shared across all files.",agent-context-file-loading.md
cr12,The `<prior_attempt>` paragraph (all landings),"Added to the system prompt of every landing run: <prior_attempt> holds what an earlier, quicker run did before it asked for more. Treat it as notes from a colleague you have not checked. Reuse its queries and refs so you do not repeat its reads. Recompute any figure that will appear in your answer.",agent-design/system-prompts.md
cr13,"Subject: four kinds, one resolver","$defs.subject = { ""oneOf"": [ { ""kind"": ""repo"", ""repo"": ""<id>"" }, { ""kind"": ""path"", ""repo"": ""<id>"", ""path"": ""<prefix>"" }, { ""kind"": ""dependency"", ""coordinate"": ""<artifact coordinate>"", ""version"": ""<the version it was learned at>"" }, { ""kind"": ""tool"", ""tool"":",agent-design/memory.md
cr14,"Substrate and retrieval: files for curated memory, search for episodic","Revised 2026-11-02 after widening the survey to always-running agents (`../../agent-memory-learning.md` §15). The first draft said ""no embeddings"" outright. That was right for curated memory and wrong for the episodic layer.* *Every durable store has two layers.",agent-design/keel/memory.md
cr15,One mechanism vs. a layered pipeline vs. a pluggable strategy,"The biggest architectural fork in this survey: does the scaffold have one* way to compact, or does it treat compaction as a set of interchangeable/stackable strategies?",agent-context-compaction.md
cr16,The tool surface: what the agent can actually do to its memory,"Three findings fall out of the table: The read/write asymmetry is an exact inversion between two camps. Cursor and Augment can *write* a memory but have no read or search tool at all — because memories arrive pre-selected in the prompt, so there is nothing left to fetch. Codex is the mirror image:",agent-memory-learning.md
cr17,What the nonce does not cover,"Stated explicitly, because ""it is nonce-wrapped"" is easy to hear as ""it is handled"". *Covered, completely: forging either delimiter. Neither an early close nor a minted higher-binding open tag is representable without the run nonce. *Not covered:",agent-design/context-files.md
cr18,Codex is building retrieval over the catalog — in shadow,"`codex-rs/ext/skills/src/dynamic_skill_selector/` contains eleven competing selector implementations — fielded BM25, character n-grams, routing cards, LRU, LRU+lexical, LRU+character-routing, multi-query lexical, weighted lexical, and reciprocal-rank fusion over lexical and character signals — behind one trait whose doc comment sets the t",agent-context-file-loading.md
cr19,"The reviewer core, and the specialist wrapper","The finding rules are one shared text — `{{REVIEWER_CORE}}` — used by both finder shapes: wrapped in the sub-agent framing below for multi-stage specialists, and inlined as step 3 of the single-stage prompt (§2b).",agent-design/system-prompts.md
cr20,"Categories, with structure and per-category gates","§6c's four categories become five, each with a required shape and its own promotion gate:",agent-design/memory.md
cr21,Two things Codex's token-budget mode does that no summariser can,"Added 2026-09-12. Both follow from the §5 row above but are about the prompting* around the mechanism rather than the mechanism itself. *The exhaustion path narrows the tool surface to two calls. Codex's token-budget block carries three escalating prompts, not one.",agent-context-compaction.md
cr22,OpenClaw's memory architecture (read from source),"`openclaw/openclaw` `49f60db9` (2026-11-02), `docs/concepts/memory*.md`, `dreaming.md`, `active-memory/*.md`, `soul.md`. The earlier OpenClaw pass (2026-08-31) read its prompts and learning writers; this one read the memory architecture documents, which say why each piece exists.",agent-memory-learning.md
cr23,"Narrowing, later: `paths` and `kinds`","*Not v1. v1 appends the whole corpus. This subsection exists to record what narrowing will look like when it is needed, and — more usefully — what v1 has to avoid doing so that it stays available. The pressure that will force it is the review fan-out.",agent-design/context-files.md
cr24,"Trust gating, and why CI defeats it",Two harnesses refuse to load context files from a workspace the user hasn't trusted: Codex: `load_project_instructions` returns before any filesystem walk when `config.active_project.is_untrusted()`. User-level instructions still apply. Gemini CLI:,agent-context-file-loading.md
cr25,The specialist wrapper (multi-stage sub-agent),"Tool scope: `Read`, `Grep`, `List` only — no `Edit`, `Write`, or `Bash`. A specialist finds issues; it never touches code. You are a Forge review specialist. You were spawned by Forge's review orchestrator to look at one pull request for exactly one specialism.",agent-design/system-prompts.md
cr26,A learning is a section,"Learnings come back in `sections[]` (`context-files.md` §1b) like anything else: { ""id"": ""learned/8f21c0…"", ""tier"": ""learned"", ""binding"": ""default"", // always; see below ""title"": ""Integration tests need a live Postgres, not the mock"", ""body"": ""<Markdown, inert>"", ""bytes"": 410, ""scope"":",agent-design/memory.md
cr27,"Claude Code at v2.1.303: four summariser prompts, and the user's words as a record","Added 2026-10-19 from `leaked/claude-code/piebald-2.1.303/`.* The nine-section template in §2 is still shipped (with an ""additional instructions"" variant that now offers a 2,000-word cap), but it has three siblings, alternatives the client selects between (the extraction does not show the selection rule):",agent-context-compaction.md
cr28,"What is actually injected, and where","Four distinct injection sites, and the choice has consequences: Into the developer instructions — Codex.",agent-memory-learning.md
cr29,Injection point and the prompt cache,"Conventions blocks go in the task envelope (`formats.md` §1), not the system prompt. The system prompt is identical across every run of a given mode and is the cacheable prefix.",agent-design/context-files.md
cr30,The null case: Aider,"Aider has no loader, and its absence is instructive rather than a gap. Conventions are an ordinary read-only file the user names explicitly (`--read CONVENTIONS.md`, or a `read:` key in `.aider.conf.yml`), delivered through the same channel as any other read-only file:",agent-context-file-loading.md
```
