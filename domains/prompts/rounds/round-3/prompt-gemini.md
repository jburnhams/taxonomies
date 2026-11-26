# Rater prompt: prompts taxonomy, stage 1, round 3

You are classifying 60 items for a taxonomy agreement test. Use only the definitions below; do not look anything up, do not read any files, and do not use other knowledge of the repo they come from.

Each item is one section of a research repo about how AI agent products and harnesses are built (Claude Code, Codex, Gemini CLI, MCP, agent SDKs) and of the designs of the repo owner's own agent platform (Keel, with configurations Forge and Lens). An item is the section's heading, the first lines under it (`gist`), and the file it is in (`from`).

For every item, answer all three questions with exactly one value each, chosen from the list for that question. If no value fits, still pick the closest one and write `unsure` plus a few words in the note column.

Rules:
- Classify the mechanism, approach or design choice the section describes, not the document it is in. The `from` column is part of the item.
- area: the part of an agent system that would have to change to change the mechanism. Whatever decides *whether* something may happen is `control`; whatever decides *where work goes next* is `coordination`; checking whether finished work is right is `verification`.
- decider: the party whose decision has the final say when it applies. Test: if the model ignored its instructions, would the outcome still hold? Yes: `rule` (or `second-model` / `person` if one of those decides). No: `working-model`. A store or format with nothing decided at run time, and a setting a person chose before the run, are `rule`. A separate model call (a validator, a summariser, a classifier, a trained predictor) is `second-model` even when the harness builds its prompt or picks which prompt to send. A person who only starts a run or a watch is not its decider.
- moment: the first point in a run's life at which it takes effect. `setup` is only what happens before the first model request (configuration, loading context, choosing tools, provisioning). A format, store or rule fixed in advance takes the moment at which it is used: a result format at `tool-call`, a tier computed when a run finishes at `ending`, a memory store at `after-run`.
- If an item describes several mechanisms, classify the first one named; if it surveys several approaches without naming one first, classify the one it recommends, or pick the closest and mark `unsure`.

Answer as CSV only, with this header and one row per item, in the items' order. Quote any note that contains a comma.

```
id,area,decider,moment,note
```

## The questions and their values

- **area**: Which part of an agent system is it about? Values: `operations`, `control`, `tool`, `context`, `output`, `model`, `verification`, `coordination`
- **decider**: Who makes the call when it applies? Values: `second-model`, `person`, `working-model`, `rule`
- **moment**: When does it act? Values: `after-run`, `turn`, `ending`, `setup`, `failure`, `tool-call`

## Definitions of the values

### person (`person`)

- **Definition**: A person is a decider that is a human answering at the moment the mechanism applies.
- **Scope**: Includes approving or denying an action, replying to a question, typing a command or keyword, handing an image or file to the agent, merging a PR. Excludes a setting a person chose earlier, and a person starting a run or a watch that then proceeds without them: the decider is whatever decides while it runs.
- **Aliases**: human, user, human in the loop, operator
- **Near miss**: "ultrathink" typed by the user: the person decides, though code detects the word.
- **Kind**: role
- **Facet**: `decider`

### working model (`working-model`)

- **Definition**: A working model is a decider that is the model doing the task, acting on its own judgment and instructions.
- **Scope**: Includes instructions in a prompt or a tool description that the model follows or not, a model choosing which tool or ending to call, which lost calls to retry, or how to combine calls into a program, and a model rating its own risk. The test: if the model ignored its instructions, would the outcome still hold? If not, the decider is the working model. Excludes a separate model call made to check it (`second-model`).
- **Aliases**: the model, agent judgment, model self-report
- **Near miss**: Rules written in the prompt as a table that the harness then checks: the check has the final say, so `rule`. A reminder the harness inserts listing lost calls: the harness writes it, but the model decides what to do, so `working-model`.
- **Kind**: role
- **Facet**: `decider`

### failure (`failure`)

- **Definition**: A failure is a moment that comes when something goes wrong or a limit is reached during a run.
- **Scope**: Includes errors, timeouts, budget and context limits, loops, broken model responses, lost or restarted sessions, and what recovers from them.
- **Aliases**: error, recovery, limit
- **Near miss**: A planned stop because the work is done: `ending`.
- **Kind**: happening
- **Facet**: `moment`

### setup (`setup`)

- **Definition**: A setup is a moment that comes before a run's first model request.
- **Scope**: Includes configuration, choosing tools and models, loading context files and the system prompt, provisioning a sandbox. Excludes a format, store or rule that is fixed in advance but takes effect later: it takes the moment at which it is used (a result format at `tool-call`, a risk tier computed at the end at `ending`, a memory store at `after-run`).
- **Aliases**: start, startup, initialisation, configuration
- **Near miss**: Loading a deeper context file when the model first reads that folder: it happens mid-run, so `tool-call`.
- **Kind**: happening
- **Facet**: `moment`

### output (`output`)

- **Definition**: Output is an area of an agent system that covers what a run produces for people to read or use.
- **Scope**: Includes turn text and its style, narration, titles, generated files and artefacts, interactive views, tables and charts, and how they are delivered. Excludes records kept for operators (`operations`).
- **Aliases**: deliverable, response, artefact
- **Near miss**: A transcript of the run: it is produced, but for operators and analysis, so it is `operations`.
- **Kind**: thing
- **Facet**: `area`

### turn (`turn`)

- **Definition**: A turn is a moment that comes with each model request and its reply.
- **Scope**: Includes building each request, cache placement, reminders added per request, reasoning budgets, text and titles produced per reply.
- **Aliases**: step, request, model call
- **Near miss**: A check on each shell command: it acts per action, so `tool-call`.
- **Kind**: happening
- **Facet**: `moment`

### control (`control`)

- **Definition**: Control is an area of an agent system that covers whether an action may happen and what stops or redirects a run.
- **Scope**: Includes approval and permission modes, risk levels, sandboxing, blocking monitors, steering and nudges, recovery after errors and limits, and how a run is allowed to end. Whatever decides *whether* goes here. Excludes where work goes next (`coordination`) and checking the quality of finished work (`verification`).
- **Aliases**: safety, permissions, guardrails
- **Near miss**: Routing a sub-agent's approval request to the parent session: the routing is `coordination`, but refusing an answer from the wrong session decides whether, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

### ending (`ending`)

- **Definition**: An ending is a moment that comes when a run or a sub-run finishes and hands back its result.
- **Scope**: Includes completion tools and gates, the shape of a sub-agent's answer, hand-offs, escalation after a review, what a run's outcome records.
- **Aliases**: completion, finish
- **Near miss**: A review of a merged PR the next day: it is after the run, so `after-run`.
- **Kind**: happening
- **Facet**: `moment`

### model access (`model`)

- **Definition**: Model access is an area of an agent system that covers how models are called and chosen.
- **Scope**: Includes providers and their wire formats (dialects), routing between models, reasoning effort and thinking budgets, prompt caching, and what happens when a model's response is broken. Excludes what the model is told (`context`) and which tools it is offered (`tool`).
- **Aliases**: LLM access, inference
- **Near miss**: Deferring tool definitions so the cache survives: the change is to how the request is assembled, so it is `model` when the point is the cache and `tool` when the point is which tools are loaded.
- **Kind**: thing
- **Facet**: `area`

### after run (`after-run`)

- **Definition**: An after run is a moment that comes between runs or once a run is over.
- **Scope**: Includes writing and consolidating memory, evals and benchmarks, telemetry storage and analysis, retrospectives, a review triggered by a finished PR.
- **Aliases**: offline, between runs, post-run
- **Near miss**: A loop detector inside the run: it reads the same signals, but acts during the run, so `failure`.
- **Kind**: happening
- **Facet**: `moment`

### second model (`second-model`)

- **Definition**: A second model is a decider that is a separate model call, apart from the working model, whose answer has the final say.
- **Scope**: Includes classifiers, blocking monitors, judges, graders, validators, trajectory judges, background agents that review or curate memory, and small helper models (title writers, summarisers) when their output stands. A separate model call is the decider even when the harness assembles its prompt, chooses which of several prompts to send, or acts on its answer: a validator sub-agent's verdict, a summariser's summary, a trained risk predictor's score. Excludes the working model reviewing itself (`working-model`), and a model provider's own service withholding or filtering content, which is `rule` unless the source says a model there decides.
- **Aliases**: judge, LLM judge, monitor, classifier, grader, verifier
- **Near miss**: A sub-agent that does part of the task: it is a separate model call, but it works rather than decides; its work is judged by whoever accepts it.
- **Kind**: role
- **Facet**: `decider`

### tool call (`tool-call`)

- **Definition**: A tool call is a moment that comes with each action the model takes through a tool, or with that action's result.
- **Scope**: Includes approval before an action, monitors on actions, result size limits and refs, MCP requests during a call.
- **Aliases**: action, tool invocation
- **Near miss**: A tool the model calls to finish: the call is the moment the run ends, so `ending`.
- **Kind**: happening
- **Facet**: `moment`

### verification (`verification`)

- **Definition**: Verification is an area of an agent system that covers checking whether the work is right.
- **Scope**: Includes self-verification and completion gates, code review of a change, evals, benchmarks and their graders. Excludes checks on whether an action may happen (`control`).
- **Aliases**: checking, quality checks
- **Near miss**: A blocking monitor that refuses a risky command: it checks an action before it happens, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

### coordination (`coordination`)

- **Definition**: Coordination is an area of an agent system that covers how agents and runs are arranged and where work goes next.
- **Scope**: Includes sub-agents and orchestrators, triggers, pipelines and their edges, hand-offs between runs, entrypoints and the kinds of run a system offers. Excludes deciding whether an action is allowed (`control`).
- **Aliases**: orchestration, multi-agent
- **Near miss**: A tool that ends a run: choosing which ending applies is `control`; the follow-up run it dispatches is `coordination`.
- **Kind**: thing
- **Facet**: `area`

### rule (`rule`)

- **Definition**: A rule is a decider that is fixed logic applied without a model's judgment.
- **Scope**: Includes harness code, schema and format checks, caps and budgets, a setting chosen beforehand and applied by code, a model provider's service filtering content, and stores and formats where nothing is chosen at run time. The outcome holds even if the model ignores its instructions. Where a section names several mechanisms with different deciders, classify the first one named (reminders before a trajectory judge: `rule`); where it surveys a spectrum without naming one first, classify the one the section recommends or, failing that, mark `unsure`.
- **Aliases**: code, deterministic check, static rule
- **Near miss**: A person choosing a permission mode before the run: the choice is the person's, but at run time the mode is applied by code, so `rule`.
- **Kind**: role
- **Facet**: `decider`

### tool use (`tool`)

- **Definition**: Tool use is an area of an agent system that covers what the model can do and how its calls and their results move.
- **Scope**: Includes the tool surface, tool implementations, call and result formats, large results and refs, deferred tool loading, code mode, MCP servers and their protocol. Excludes whether a call is allowed (`control`).
- **Aliases**: tooling
- **Near miss**: An approval prompt before a shell command: the command is a tool, but asking whether it may run is `control`.
- **Kind**: thing
- **Facet**: `area`

### context (`context`)

- **Definition**: Context is an area of an agent system that covers what the model is given to read and what is kept for later.
- **Scope**: Includes system prompts, context files (AGENTS.md, CLAUDE.md), injected environment text, compaction and summaries, memory across runs. Excludes mid-run text that steers the model (`control`).
- **Aliases**: context engineering
- **Near miss**: A reminder the harness injects when the model loops: it is text in the context, but its job is to redirect, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

### operations (`operations`)

- **Definition**: Operations is an area of an agent system that covers running agents and keeping their records.
- **Scope**: Includes telemetry, traces and transcripts, storage and dashboards, version control and commits, local compute, provenance of content, deployment. Excludes checking the quality of the work (`verification`).
- **Aliases**: ops, observability
- **Near miss**: A loop detector that stops a run: it reads telemetry, but stopping decides, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

## Items

```csv
id,item,gist,from
g01,How the quick agent is presented with them,"The model meets the two tools in five places, and each carries one kind of information so that no two repeat each other.",agent-design/models.md
g02,"Writing, validation and moderation","The rule that decides everything here: the wider a store's readership, the less a run may write to it directly. A bad note costs one pipeline run. A bad team memory is read by every colleague's agent until someone notices. *Three write modes, set per store attachment:",agent-design/keel/memory.md
g03,"Five ways to delimit a call, and the tokenizer decides which",The families sort by *what kind of thing* the delimiters are. This is the distinction that predicts most parser behaviour.,agent-tool-call-dialects.md
g04,Goose: resume a delegate by id,"`summon.rs` gains a `resume` parameter taking the sub-agent id of a *failed or cancelled delegate. Only `instructions` may accompany it; every other field (`source`, `model`, `extensions`, `max_turns`, …) is rejected, so a resume cannot change what the delegate is.",agent-run-recovery.md
g05,Persistent memory & deployment as tools,Two capabilities that only a couple of sources in this collection expose as callable tools rather than passive conventions. Memory is the larger half and has moved a lot:,agent-tool-surfaces.md
g06,(b) A separate background agent reads finished transcripts,"Four independent implementations of the same idea, none of which existed in this collection's earlier passes. This is the strongest convergence in this doc:",agent-memory-learning.md
g07,The `<prior_attempt>` paragraph (all landings),"Added to the system prompt of every landing run: <prior_attempt> holds what an earlier, quicker run did before it asked for more. Treat it as notes from a colleague you have not checked. Reuse its queries and refs so you do not repeat its reads. Recompute any figure that will appear in your answer.",agent-design/system-prompts.md
g08,Code changes in response to comments — the boundary,"Review mode replies to threads; it never edits code (`system-prompts.md` §2's constraints). Making the change a reviewer asked for is the coding entrypoint's job, via the two roadmap run sources that already exist for it, and this section exists to pin the seam between them:",agent-design/review.md
g09,Turn/output bounding and the result-handling contract,"How does the sub-agent know when to stop, and in what shape does its answer arrive back at the orchestrator?",agent-subagent-architectures.md
g10,Screenshots as verification evidence,"The brief asked about using a browser ""to verify changes."" Four sources treat the screenshot not as an observation but as an artifact of proof, and they are the most directly relevant material in this collection. *Jules mandates it, with tools for the protocol.",agent-vision-multimodal.md
g11,"What reaches the model, and as whose words","A view can put text into the model's context in three ways, and each host decides how much of it to trust.",agent-interactive-views.md
g12,Where each harness-side rule actually lives,"The implementation contract assumes a harness. On this stack that harness is split across three places, and getting the split right is most of the integration work:",agent-design/adk.md
g13,"Kinds: one vocabulary, three resolutions","*The vocabulary is v1 even though narrowing is not. `kinds` as a context-service narrowing parameter* is reserved (next subsection). The kind vocabulary itself is already load-bearing today, under two other names, and unifying them is worth doing before a third appears:",agent-design/context-files.md
g14,PR and push workflow,"A literal, fully-specified PR template, with a parallel-gather- then-analyze research step first — Claude Code (leaked):",agent-git-vcs.md
g15,Suite 3 — Review mode,"Planted defects with known locations and severities, plus deliberately clean diffs. Measures precision as much as recall:",agent-design/eval.md
g16,The dialects in practice,"The clearest measure of how many dialects exist is what an ingester has to accept. Langfuse's OTLP ingestion processor [source, 48a31810e1] has, for input and output content alone, special cases for fifteen attribute families:",telemetry/standards.md
g18,"Pure JS vs WASM, and why the gap is architectural","The obvious way to get SQL into a browser is DuckDB-WASM, and it is a much more complete analytical engine than anything written in plain JavaScript: an optimizer, spill-to-disk, years of correctness work, and far more SQL surface. For heavy local analytics it is the right answer.",agent-local-compute.md
g20,"LangSmith [source for the client, inference for the store]",Runs are sent as a tree ordered by `dotted_order`. The store is not open source.,telemetry/platforms-and-storage.md
g21,"Two granularities, one problem","They are the same problem at different time scales. The action-risk systems are older and much more mechanised, and a PR-level design should borrow from them most. The clearest example is Guardian's rule that a `low` is valid only under the exact authorization snapshot it was computed in (§4).",agent-risk-assessment.md
g22,Pipeline changes (multi- and single-stage alike),"Against `system-prompts.md` §2a: 1. Step 1 (warranted?) is unchanged. A skip still produces no attention block. 2. Step 1½ (triage) is new (§3b). The harness has already put the floor and its drivers in the envelope as a `<review_policy>` block, harness-authored, so it carries no nonce. 3.",agent-design/risk.md
g23,"Hook-based, user-configured verification gates","One source has a genuinely general-purpose mechanism for this, not tied to any specific verification logic at all:",agent-self-verification.md
g24,Promoted to `future.md` with a stated shape,"*A kernel-backed session, for an interactive surface. Everything in v1 is stateless: scripts run under `Bash`, state lives in refs.",agent-design/data.md
g25,"MCP: central in the namespace, not in the block type","The artifact URI namespace is the addressing every Forge MCP tool speaks — refs go into tool calls and come back in results, uniformly, which is what makes the tool surface small. *What does not change is the wire shape.",agent-design/artifacts.md
g26,What it means for Forge,"The rules converge: the harness, not the content, decides who the principal is; an answer binds to the request it answers; approval covers exactly what was shown and lapses when that changes; summaries and relays never carry the user's authority.",agent-content-provenance.md
g27,"Roo Code — MCP-aware, and silently lossy","`src/core/tools/UseMcpToolTool.ts`, `processToolContent` (`b867ec9`). if (item.type === ""text"") return item.text if (item.type === ""resource"") { const { blob: _, ...rest } = item.resource; return JSON.stringify(rest, null, 2) } if (item.type === ""image"") { /* pushed to an images[] array as a data:",agent-tool-result-transport.md
g28,"A completed-reasoning-block micro-title — a second, smaller title-generation instance","Easy to miss, and distinct from session-title generation (§1):",agent-turn-output.md
g29,"Injection, and the one honest mitigation","*Deployment fact, 2026-08-30: only authenticated org members can attach to a Jira issue. That materially lowers this risk and the section is written accordingly — image-borne injection would require an insider, not a drive-by bug reporter.",agent-design/vision.md
g30,Self-oversight inside a run,One thing worth importing from OpenClaw at the run level rather than the ledger level. Its session goal injects a line into every turn:,agent-design/orchestration.md
g31,"`blocker` suspends, and it reuses machinery that exists","At `blocker`, `ReportProblem` is terminal, and the task suspends with a wake predicate on the report's resolution — one more predicate kind alongside `medium.md` §4c's `jira` / `build` / `pr` / `timer`. Suspension mechanics carry over from `formats.md` §5 unchanged:",agent-design/memory.md
g32,"Compaction needs a second budget, and a degradation says what it did not damage","*Amends `generative.md` §2b's refusal vocabulary; the compaction half lands in `future.md`. Two small things, both from failure modes this design has not written down.",agent-design/cloudflare.md
g33,"Claude Code's auto-mode classifier, read from the shipped prompt","Added 2026-10-19.* The classifier is a 14k-token prompt, `agent-prompt-security-monitor-for-autonomous-agent-actions-first-part.md`, plus pieces appended by context.",agent-permissions-approval.md
g35,Per-model / per-provider prompt variants,"Covered in more depth in each source's own README; summarized here for the ""leaders"":",coding-agent-approaches.md
g37,The generated page is itself an injection surface,"`artifact-components`, on a script writing reader-typed text into its own JSON island: A script in that lane that writes reader-typed text into its island must never splice the raw string: `</` inside a JSON string value ends the script element and executes what follows for every later viewer.",agent-generative-output.md
g39,"The repair catalogue, and why it must run *after* validation","§3e establishes that mature harnesses accept more than they advertise; §3f puts a floor under it; §3g explains mechanically why the sloppiness exists. What none of the code read here supplies is the *list* — which malformations actually occur, in what proportion, and in what order to fix them.",agent-tool-implementations.md
g40,"Pattern C: the advisor tool (cheap executor, strong consultant)","Anthropic's advisor tool (beta header `advisor-tool-2026-03-01`, launched April 2026) inverts pattern A. The cheap model runs the loop and may call `advisor`, which runs a separate Opus inference server-side within the same `/v1/messages` request. Mechanics from the docs:",agent-multi-model.md
g41,"A saved tool group for Java agents, used against a repo","""I define a tool group for Java coding agents from several MCP servers, control each tool's visibility, override its params and other settings to change how the agent sees it, and save it.",agent-design/keel/README.md
g42,"Who pays, and from which budget","Pydantic's judge claims one request from the run's own usage limit before each launch, and skips a tick the budget cannot fit, so judging cannot push a run over its limit. Deep Agents bounds the grader's input (30 messages, 4,000 characters each).",agent-run-steering.md
g43,One mechanism vs. a layered pipeline vs. a pluggable strategy,"The biggest architectural fork in this survey: does the scaffold have one* way to compact, or does it treat compaction as a set of interchangeable/stackable strategies?",agent-context-compaction.md
g44,`SearchSource` / `ReadSource` (ref-pinned source beyond the working tree),"Superseded as a *tool* design, 2026-08-30 — the capability is now v1. `artifacts.md` makes every read tool speak one address space, so these are not new tools:",agent-design/medium.md
g45,"`AskUser` posts a decision record, not a prose question","The `workshop` skill runs a decision loop through a published document: choices are rendered as option rows, a confirmed choice republishes the page, and the session reads the answer back through a named schema (`read_page_data`, schema `workshop-decisions`) rather than by parsing prose.",agent-design/generative.md
g46,Templating: there is none,"A clean negative result. No harness in this collection treats the repository's context file as a template. No `{{var}}` interpolation, no conditionals, no includes beyond the `@path` transclusion above, no environment-variable expansion inside the file body. The file is inert text.",agent-context-file-loading.md
g48,How tools get advertised,"Three shapes, and they are not interchangeable in cost: One compact JSON object per line inside `<tools>…</tools>`, placed in the system turn. Qwen3's template does this natively; OMP's owned dialects reuse the same shape. Cheapest to generate, and the closest thing to sending the schema verbatim.",agent-tool-call-dialects.md
g49,"Stopped, not dead: a resource limit inside a live run","Added 2026-11-02 in the weekly pass, from `leaked/claude-code/piebald-2.1.316/`.* §1 covers a runner that died. Claude Code 2.1.314 adds the case just short of that: the sandbox enforces a limit itself, kills the work, and the run carries on.",agent-run-recovery.md
g50,"Code execution as a distinct capability from ""the shell""","Most sources fold ""run code"" into ""run a shell command."" A few make code execution its own tool, or its own sandbox, distinct from the general shell.",agent-tool-surfaces.md
g51,OpenClaw's memory architecture (read from source),"`openclaw/openclaw` `49f60db9` (2026-11-02), `docs/concepts/memory*.md`, `dreaming.md`, `active-memory/*.md`, `soul.md`. The earlier OpenClaw pass (2026-08-31) read its prompts and learning writers; this one read the memory architecture documents, which say why each piece exists.",agent-memory-learning.md
g52,General-purpose delegate prompt (coding mode),"Short and role-scoped, per this file's intro — the delegate has no task envelope, no mode, and no Complete/AskUser, so it gets none of the orchestrator prompt's machinery. Closest precedent is Amp's generic `H_R` delegate prompt (`agent-subagent-architectures.md` §3). Tool scope:",agent-design/system-prompts.md
g53,Stable finding identity across sessions (amends §7),"From PR-Agent's `previous_findings` and Copilot's overview buckets (`../pr-agent/README.md`).* §7's reconciliation already joins findings to threads. Two additions: Identity is a key, not text.",agent-design/review.md
g54,Calling convention & protocol shape,"The biggest structural fork: is a ""sub-agent"" a tool call that returns a result, or a role in a shared conversation that hands control back and forth via convention?",agent-subagent-architectures.md
g55,Transport: getting the bytes to the model,"This is where the field is genuinely messy, and where the sharpest bug in the research lives.",agent-vision-multimodal.md
g56,Which tools a view may call,"The gap is the fourth row. App-only tools are designed to be invisible: to the model, which is the point, and in Claude to the user. So a view can run a write tool, or a costly query in a loop, with nobody approving each call.",agent-interactive-views.md
g57,Advertising is not enforcement,`toolFilter` controls which tools ADK exposes to the model. It does not stop the server executing a filtered-out tool if something calls it. The design's structural narrowing is therefore only half-implementable client-side:,agent-design/adk.md
g58,"Inlining, and when not to","`formats.md` §1's `<repo_context>` currently says: inline the root file ""if one exists and is short enough to inline; otherwise its path only, and the model reads it itself"". Made concrete: ≤ 32 KiB: inlined as a `<conventions>` block. > 32 KiB: the first 32 KiB inlined, truncation announced (§2).",agent-design/context-files.md
g59,Output: a ship/no-ship log,"Results are per-feature, not a leaderboard. Each entry records the change, the A/B table, a verdict, and the caveats — the same shape as `results/SUMMARY.md` in Hermes's eval. A tunable that cannot be shown to matter goes back to being a default, and is documented as such.",agent-design/eval.md
g61,Measurement one — token cost,"`bench/tabular-formats.py`. The same synthetic rows (8 columns: ids, a customer name with commas and quotes, categoricals, timestamps, a nullable float, a bool, a free-text note with commas, quotes, newlines and tabs; ~8% null revenue) rendered eleven ways. Tokenizers: `o200k_base` and `cl100k_base`.",agent-tabular-results.md
g62,What breaks when you move compute into the tab,"Not everything survives the move, and the failures are not where you expect. *The engine streams; the MCP boundary does not.",agent-local-compute.md
g63,"It already works, and jupyter-mcp is the proof","The user's idea — *an MCP tool creates the artifact directly (a binary, a database table, a parquet file) and returns the ref plus metadata* — is not speculative. jupyter-mcp ships it, inside plain MCP, with no extensions:",agent-data-analysis.md
g64,What the storage designs agree on [inference],"1. One row per span, wide, with maps for open-ended keys (usage, cost, metadata). Langfuse moved *to* this from normalised tables. 2. Content is stored separately or truncated in the hot table. The list view never needs more than a preview. 3.",telemetry/platforms-and-storage.md
g65,Hosted products: what is shown and what is hidden,"*CodeRabbit Triage cards (`docs.coderabbit.ai/triage/your-triage-view`) show separate signals, each tied to the reviewed commit:",agent-risk-assessment.md
g66,"The floor: path and kind rules (deterministic, harness)","The harness evaluates a review policy: an ordered list of rules, each matching changed paths or change kinds and naming a minimum tier. It is read from harness configuration, or the base SHA's copy of a repository file, never the head's (`context-files.md` §5).",agent-design/risk.md
g67,"Verification authority handed to the user, not the model","Two leaked sources place the actual accept/reject decision outside the model entirely — a third pole beyond ""self-report"" (§7) and ""separate LLM judge"" (§3), and structurally distinct from either.",agent-self-verification.md
```
