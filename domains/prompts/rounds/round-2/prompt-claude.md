# Rater prompt: prompts taxonomy, stage 1, round 2

You are classifying 56 items for a taxonomy agreement test. Use only the definitions below; do not look anything up, do not read any files, and do not use other knowledge of the repo they come from.

Each item is one section of a research repo about how AI agent products and harnesses are built (Claude Code, Codex, Gemini CLI, MCP, agent SDKs) and of the designs of the repo owner's own agent platform (Keel, with configurations Forge and Lens). An item is the section's heading, the first lines under it (`gist`), and the file it is in (`from`).

For every item, answer all three questions with exactly one value each, chosen from the list for that question. If no value fits, still pick the closest one and write `unsure` plus a few words in the note column.

Rules:
- Classify the mechanism, approach or design choice the section describes, not the document it is in. The `from` column is part of the item.
- area: the part of an agent system that would have to change to change the mechanism. Whatever decides *whether* something may happen is `control`; whatever decides *where work goes next* is `coordination`; checking whether finished work is right is `verification`.
- decider: the party whose decision has the final say when it applies. Test: if the model ignored its instructions, would the outcome still hold? Yes: `rule` (or `second-model` / `person` if one of those decides). No: `working-model`. A store or format with nothing decided at run time, and a setting a person chose before the run, are `rule`.
- moment: the first point in a run's life at which it takes effect. `setup` is only what happens before the first model request (configuration, loading context, choosing tools, provisioning). A format, store or rule fixed in advance takes the moment at which it is used: a result format at `tool-call`, a tier computed when a run finishes at `ending`, a memory store at `after-run`.
- If an item describes several mechanisms, classify the first one named.

Answer as CSV only, with this header and one row per item, in the items' order. Quote any note that contains a comma.

```
id,area,decider,moment,note
```

## The questions and their values

- **area**: Which part of an agent system is it about? Values: `tool`, `model`, `context`, `output`, `control`, `coordination`, `verification`, `operations`
- **decider**: Who makes the call when it applies? Values: `working-model`, `person`, `rule`, `second-model`
- **moment**: When does it act? Values: `tool-call`, `failure`, `setup`, `turn`, `ending`, `after-run`

## Definitions of the values

### output (`output`)

- **Definition**: Output is an area of an agent system that covers what a run produces for people to read or use.
- **Scope**: Includes turn text and its style, narration, titles, generated files and artefacts, interactive views, tables and charts, and how they are delivered. Excludes records kept for operators (`operations`).
- **Aliases**: deliverable, response, artefact
- **Near miss**: A transcript of the run: it is produced, but for operators and analysis, so it is `operations`.
- **Kind**: thing
- **Facet**: `area`

### failure (`failure`)

- **Definition**: A failure is a moment that comes when something goes wrong or a limit is reached during a run.
- **Scope**: Includes errors, timeouts, budget and context limits, loops, broken model responses, lost or restarted sessions, and what recovers from them.
- **Aliases**: error, recovery, limit
- **Near miss**: A planned stop because the work is done: `ending`.
- **Kind**: happening
- **Facet**: `moment`

### turn (`turn`)

- **Definition**: A turn is a moment that comes with each model request and its reply.
- **Scope**: Includes building each request, cache placement, reminders added per request, reasoning budgets, text and titles produced per reply.
- **Aliases**: step, request, model call
- **Near miss**: A check on each shell command: it acts per action, so `tool-call`.
- **Kind**: happening
- **Facet**: `moment`

### model access (`model`)

- **Definition**: Model access is an area of an agent system that covers how models are called and chosen.
- **Scope**: Includes providers and their wire formats (dialects), routing between models, reasoning effort and thinking budgets, prompt caching, and what happens when a model's response is broken. Excludes what the model is told (`context`) and which tools it is offered (`tool`).
- **Aliases**: LLM access, inference
- **Near miss**: Deferring tool definitions so the cache survives: the change is to how the request is assembled, so it is `model` when the point is the cache and `tool` when the point is which tools are loaded.
- **Kind**: thing
- **Facet**: `area`

### ending (`ending`)

- **Definition**: An ending is a moment that comes when a run or a sub-run finishes and hands back its result.
- **Scope**: Includes completion tools and gates, the shape of a sub-agent's answer, hand-offs, escalation after a review, what a run's outcome records.
- **Aliases**: completion, finish
- **Near miss**: A review of a merged PR the next day: it is after the run, so `after-run`.
- **Kind**: happening
- **Facet**: `moment`

### setup (`setup`)

- **Definition**: A setup is a moment that comes before a run's first model request.
- **Scope**: Includes configuration, choosing tools and models, loading context files and the system prompt, provisioning a sandbox. Excludes a format, store or rule that is fixed in advance but takes effect later: it takes the moment at which it is used (a result format at `tool-call`, a risk tier computed at the end at `ending`, a memory store at `after-run`).
- **Aliases**: start, startup, initialisation, configuration
- **Near miss**: Loading a deeper context file when the model first reads that folder: it happens mid-run, so `tool-call`.
- **Kind**: happening
- **Facet**: `moment`

### coordination (`coordination`)

- **Definition**: Coordination is an area of an agent system that covers how agents and runs are arranged and where work goes next.
- **Scope**: Includes sub-agents and orchestrators, triggers, pipelines and their edges, hand-offs between runs, entrypoints and the kinds of run a system offers. Excludes deciding whether an action is allowed (`control`).
- **Aliases**: orchestration, multi-agent
- **Near miss**: A tool that ends a run: choosing which ending applies is `control`; the follow-up run it dispatches is `coordination`.
- **Kind**: thing
- **Facet**: `area`

### operations (`operations`)

- **Definition**: Operations is an area of an agent system that covers running agents and keeping their records.
- **Scope**: Includes telemetry, traces and transcripts, storage and dashboards, version control and commits, local compute, provenance of content, deployment. Excludes checking the quality of the work (`verification`).
- **Aliases**: ops, observability
- **Near miss**: A loop detector that stops a run: it reads telemetry, but stopping decides, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

### verification (`verification`)

- **Definition**: Verification is an area of an agent system that covers checking whether the work is right.
- **Scope**: Includes self-verification and completion gates, code review of a change, evals, benchmarks and their graders. Excludes checks on whether an action may happen (`control`).
- **Aliases**: checking, quality checks
- **Near miss**: A blocking monitor that refuses a risky command: it checks an action before it happens, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

### after run (`after-run`)

- **Definition**: An after run is a moment that comes between runs or once a run is over.
- **Scope**: Includes writing and consolidating memory, evals and benchmarks, telemetry storage and analysis, retrospectives, a review triggered by a finished PR.
- **Aliases**: offline, between runs, post-run
- **Near miss**: A loop detector inside the run: it reads the same signals, but acts during the run, so `failure`.
- **Kind**: happening
- **Facet**: `moment`

### tool use (`tool`)

- **Definition**: Tool use is an area of an agent system that covers what the model can do and how its calls and their results move.
- **Scope**: Includes the tool surface, tool implementations, call and result formats, large results and refs, deferred tool loading, code mode, MCP servers and their protocol. Excludes whether a call is allowed (`control`).
- **Aliases**: tooling
- **Near miss**: An approval prompt before a shell command: the command is a tool, but asking whether it may run is `control`.
- **Kind**: thing
- **Facet**: `area`

### rule (`rule`)

- **Definition**: A rule is a decider that is fixed logic applied without a model's judgment.
- **Scope**: Includes harness code, schema and format checks, caps and budgets, a setting chosen beforehand and applied by code, a model provider's service filtering content, and stores and formats where nothing is chosen at run time. The outcome holds even if the model ignores its instructions. Where a section names several mechanisms with different deciders, classify the first one named (reminders before a trajectory judge: `rule`).
- **Aliases**: code, deterministic check, static rule
- **Near miss**: A person choosing a permission mode before the run: the choice is the person's, but at run time the mode is applied by code, so `rule`.
- **Kind**: role
- **Facet**: `decider`

### second model (`second-model`)

- **Definition**: A second model is a decider that is a separate model call, apart from the working model, whose answer has the final say.
- **Scope**: Includes classifiers, blocking monitors, judges, graders, validators, trajectory judges, background agents that review or curate memory, and small helper models (title writers, summarisers) when their output stands. Excludes the working model reviewing itself (`working-model`), and a model provider's own service withholding or filtering content, which is `rule` unless the source says a model there decides.
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

### working model (`working-model`)

- **Definition**: A working model is a decider that is the model doing the task, acting on its own judgment and instructions.
- **Scope**: Includes instructions in a prompt or a tool description that the model follows or not, a model choosing which tool or ending to call, which lost calls to retry, or how to combine calls into a program, and a model rating its own risk. The test: if the model ignored its instructions, would the outcome still hold? If not, the decider is the working model. Excludes a separate model call made to check it (`second-model`).
- **Aliases**: the model, agent judgment, model self-report
- **Near miss**: Rules written in the prompt as a table that the harness then checks: the check has the final say, so `rule`. A reminder the harness inserts listing lost calls: the harness writes it, but the model decides what to do, so `working-model`.
- **Kind**: role
- **Facet**: `decider`

### context (`context`)

- **Definition**: Context is an area of an agent system that covers what the model is given to read and what is kept for later.
- **Scope**: Includes system prompts, context files (AGENTS.md, CLAUDE.md), injected environment text, compaction and summaries, memory across runs. Excludes mid-run text that steers the model (`control`).
- **Aliases**: context engineering
- **Near miss**: A reminder the harness injects when the model loops: it is text in the context, but its job is to redirect, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

### control (`control`)

- **Definition**: Control is an area of an agent system that covers whether an action may happen and what stops or redirects a run.
- **Scope**: Includes approval and permission modes, risk levels, sandboxing, blocking monitors, steering and nudges, recovery after errors and limits, and how a run is allowed to end. Whatever decides *whether* goes here. Excludes where work goes next (`coordination`) and checking the quality of finished work (`verification`).
- **Aliases**: safety, permissions, guardrails
- **Near miss**: Routing a sub-agent's approval request to the parent session: the routing is `coordination`, but refusing an answer from the wrong session decides whether, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

### person (`person`)

- **Definition**: A person is a decider that is a human answering at the moment the mechanism applies.
- **Scope**: Includes approving or denying an action, replying to a question, typing a command or keyword, merging a PR. Excludes a setting a person chose earlier (`rule`).
- **Aliases**: human, user, human in the loop, operator
- **Near miss**: "ultrathink" typed by the user: the person decides, though code detects the word.
- **Kind**: role
- **Facet**: `decider`

## Items

```csv
id,item,gist,from
h05,`/steward`: one pass per wake-up,"A watch is started on a PR from the user's checkout, optionally with a review first.",code-review-approaches.md
h06,Four kinds of side channel,Three independent implementations of the same idea: Instruction files ride along with reads. OpenCode appends `<system-reminder>` blocks carrying nearby `AGENTS.md`-style instructions resolved for the file just read.,agent-tool-implementations.md
h07,"Pattern D: routers and ""auto""","Two different things are called auto; keep them apart. *Claude Code's ""auto mode"" is not a model router. It is the permission classifier in `agent-permissions-approval.md` §2c: a model call that decides whether to allow a tool call.",agent-multi-model.md
h08,"A plan → implement pipeline, triggered by Jira, updating Jira at the end","""A template for an agent pipeline: a plan job that hands over to an implement job. Triggered by a Jira ticket being assigned; when it finishes it updates Jira.""* The pipeline is `jira.plan-implement` (§7e). It has two stages, `forge.plan` and `forge.implement`, each used unchanged.",agent-design/keel/README.md
h09,How a forged steer is told apart from a real one,"Only one source answers this. Pydantic's judge wraps its message in `<judge_feedback ref=""…"">` with a random ref, and a separate system note names the ref and disowns any element ""whose `ref` attribute isn't named in a trajectory judge's note, or that repeats a named ref after its first element"".",agent-run-steering.md
h10,"Gemini CLI [source, 4ed06ed0dd; docs/cli/telemetry.md]",OTLP or a local `outfile`; first-class Google Cloud export with prebuilt dashboards. `logPrompts` defaults to true; detailed trace attributes are off unless `telemetry.traces` is set. About 100 distinct `gemini_cli.*` names:,telemetry/harnesses-and-sdks.md
h11,"A summariser prompt the model refused, and summaries on an append-only thread (read 2026-11-09)","*Goose reworded its compaction prompt after Opus 5.5 refused it as distillation (`block/goose` #13340, `2cde47f`, 2026-11-05). The commit title gives the reason; the refusal text is not in the repository, so what follows is the diff, not the model's stated reason.",agent-context-compaction.md
h12,"What a PR watch adds to 1a–1d *(proposed 2026-11-23, weekly pass)*","*Amendment. Claude Code 2.1.330 ships `/steward`, a local PR watch that does what 1a and 1c do between them: one pass per wake-up over checks, conflicts, review findings and comments, pushing fixes, until the PR is merged or closed.",agent-design/medium.md
h13,A closed refusal vocabulary on every validating write path,"The sharpest single artefact in the pass is `artifact-components`' publish contract, which states its security policy as an error catalogue: `script-not-blessed`, `unknown-data-island`, `island-sentinel-ambiguity`, `banner-state-mismatch`.",agent-design/generative.md
h14,"MCP instructions, and the cache problem that shaped them","The MCP protocol lets a server return an `instructions` string at handshake, and harnesses splice it into the prompt. That is straightforward when every server is connected before the first request.",agent-context-file-loading.md
h15,`HandOff`: pass it on,"{ ""name"": ""HandOff"", ""input_schema"": { ""type"": ""object"", ""properties"": { ""reason"": { ""type"": ""string"", ""enum"": [""too_complex"", ""report_requested""] }, ""why"": { ""type"": ""string"", ""maxLength"": 300, ""description"": ""One sentence: what you could not do, or what the user asked for."" } }, ""required"":",agent-design/models.md
h16,"Notes, memory and consolidation are three things","People use ""memory"" for all three. They have different lifetimes and want different machinery.",agent-design/keel/memory.md
h17,Argument encoding is where reliability is won or lost,"The delimiter style is mostly cosmetic. How arguments are encoded is not, because it decides whether the model has to produce valid escaped JSON mid-generation or can emit raw text and stop. Ordered roughly from least to most demanding: *No JSON at all.",agent-tool-call-dialects.md
h18,The model's own response failed (read 2026-11-16),"§1–§6 are about tools and runners. This section is about the other half of every turn: the model's response itself arriving broken. Five harnesses changed how they handle it in one week, and between them they cover the four ways a response fails without an API error to say so. *1.",agent-run-recovery.md
h19,Browser & web access,"Three genuinely different capability tiers, not just ""has a browser tool or doesn't"": plain fetch, fetch-plus-search, and full interactive browser automation.",agent-tool-surfaces.md
h20,Retrospectives: outcome triage and failure-to-prevention,"""Memory"" and ""retrospective"" are separable. Most memory systems store facts*. A retrospective asks what happened, whether it worked, and what should be done differently. Only a handful of sources do the second thing, and Codex does it most explicitly.",agent-memory-learning.md
h21,Analysis prompts: the quick run and its landings,"Added 2026-10-22; draft, not adopted.* For the `analyse` entrypoint in `models.md`: a cheap, fast first run that either answers or calls `Expand` or `HandOff`, and two landing runs that receive a `<prior_attempt>`. The quick prompt is short on purpose.",agent-design/system-prompts.md
h22,The validator brief — exact payload,"One `Task(subagent_type: ""validator"")` call per surviving candidate (pipeline step 5), `prompt` assembled the same way — identically in both run shapes (§6): <candidate_finding> {{ the finding, as JSON per formats.md §4, exactly as the finder returned it (id assigned, verdict:",agent-design/review.md
h23,"October 2026: fewer sub-agents, or a thousand","Added 2026-10-26.* Two publications in the same fortnight pull in opposite directions, and are worth reading together because they agree on when each direction is right. *Anthropic, ""Building agents:",agent-subagent-architectures.md
h24,Plan → implement handoff,"How a `mode: plan` run's output becomes a `mode: implement` run's input. Deliberately underspecified in one place, on purpose — see the callout at the end. 1. A `mode: plan` run ends one of three ways:",agent-design/formats.md
h25,Four entry points — and the fifth nobody built,"Every image in every harness here arrives through one of four doors. All four presume one of two things: a human present to hand the image over, or a browser the agent itself drove. Neither holds for an agent whose input is a work item, which is why §2a below exists.",agent-vision-multimodal.md
h26,How long a view lives,"The pattern underneath is the one `agent-run-recovery.md` §5 found for work still running elsewhere: the transcript, not the client, is the source of truth, so anything that must survive (ordering, identity, long-running work) is minted by the server and written into the result.",agent-interactive-views.md
h27,What a run leads to,"*Outcome. The record of how a run ended: terminal, status, summary, report, the ending tool, handoff reason, integrity checks, refusal. Older word:* ""result"" (prose). *Effect. Something the model does to the world during a run, through a granted tool. The model decides. *Sink.",agent-design/keel/taxonomy.md
h28,Retries make non-idempotent tools dangerous,`McpTool.runAsync` wraps the call in `.retryWhen(errors -> errors.delay(100ms).take(3).doOnNext(reinitializeSession))` — up to three retries with a fresh session on any exception from `callTool`. For a read that is a convenience.,agent-design/adk.md
h29,Just-in-time loading for deeper files,"The harness already holds every repo section within the run's declared path scope — §1b's one call returns all of them, not just the root. So just-in-time loading is a reveal, not a read:",agent-design/context-files.md
h30,Checkpoint and undo systems,"The axis with the widest spread of sophistication in this whole doc — from nothing, through single-file undo stacks, to a fully automatic, git-based, session-integrated `/undo` feature.",agent-git-vcs.md
h31,"Why this is not optional, and why public benchmarks don't substitute",The research pass behind this design ended on an uncomfortable finding (`agent-tool-implementations.md` §4a2): *there is no public evidence base good enough to settle harness decisions.,agent-design/eval.md
h32,Where a PR gets opened,"Keel doesn't know what a pull request is. A configuration grants a tool that opens one, usually from an MCP server bound to the workspace (`tools-and-agents.md` §4a), and decides where it sits:",agent-design/keel/outputs.md
h33,"Content: off by default, three patterns","The conventions' content section [source, gen-ai-spans.md] is the most important text in this area for us: 1. Default: don't record instructions, inputs or outputs. 2. Record on the spans — for pre-production or where the telemetry store is already compliant. 3.",telemetry/standards.md
h34,"Measurement two — accuracy, and what it could not show","`bench/tabular-accuracy.py`. One synthetic table (120 rows × 8 columns, the same dirty-text shape as §3), rendered nine ways (`tsv` with `-` nulls, `tsv` with empty nulls, quoted CSV, pipe, Markdown table, minified JSON, columnar JSON, `key:",agent-tabular-results.md
h35,The three-way split this pass is about,Three decisions usually get made as one and are independent:,agent-local-compute.md
h36,Who draws the chart,"The most consequential design decision in the category, and the sources span the entire spectrum.",agent-data-analysis.md
h37,Predicting change risk from history: Meta's DRS and RADAR,"Added 2026-10-17 (third pass).* Every source above judges a change by reading it. Meta has run the other approach for over two years: predict the risk of a diff from what similar diffs did in production, and gate on the prediction.",agent-risk-assessment.md
h38,Review-as-a-general-tool — the conflation trap,"*Three sources have something literally named ""review"" that is *not* an autonomous self-check gate, and it's easy to mistake it for one from the name alone. Codex CLI's `ReviewTask`/`codex review`/`/review`:",agent-self-verification.md
h39,The completion gate gets a provenance half,"`generative.md` §2c added a computed half to the completion gate — checks the harness runs, rather than asks the model to attest. An analysis run gets one more: Every ref named in `Complete.evidence` must resolve, and every `table://` among them must have a `produced_by` that resolves.",agent-design/data.md
h40,4 The operation set,"A handle whose only operation is ""load it all back"" is a deferral — the tokens arrive one turn later. The operations must reduce, and after §2 and §3 they are simply the read tools: `Read` with a selector — ranges, pages, sheets, members.",agent-design/artifacts.md
h41,"A magic keyword to boost reasoning budget — one source, worth flagging for a meta-reason","Claude Code detects the literal word ""ultrathink"" typed anywhere in a user message and boosts the thinking budget for that turn, with dedicated UI highlighting as the user types it. (Note for anyone reading this doc after the fact:",agent-turn-output.md
h42,Why these three and not others,"Text extraction is deliberately not here. The single most common diagnosis image in a bug tracker is a screenshot of an error message, and it wants OCR, not vision: deterministic, no model call, no image in context, and a result that is ordinary text the rest of the agent already handles.",agent-design/vision.md
h43,Where the ledger lives,*Decided: the ledger owns execution state in its own store and holds `issue_key` as a reference; the tracker stays the human-facing record and receives projections. The question this settles is whether the table is just Jira with an agent-owned status field.,agent-design/orchestration.md
h44,"4b-i. Claim strength: the gate decides whether, the wording decides how far","Added 2026-09-12. The gates above are all *admission* tests — is this worth recording at all. They say nothing about how broadly the admitted record may be *worded*, and that is a separate leak with the same consequence.",agent-design/memory.md
h45,"`Edit` gains a whitespace-normalised retry, and it flags itself","*Amends `tools.md`'s `Edit`. `Edit` is exact-match-or-fail, which `../agent-tool-implementations.md` §4 shows is the near-universal choice and which this design adopted for the right reason.",agent-design/cloudflare.md
h46,Hand-off: the outcome where permission is not available,"Added 2026-09-12. §1's new Codex row needs unpacking, because one of its four tiers is a shape this collection has not seen. *Tier 1, hand-off required, is not an approval gate.",agent-permissions-approval.md
h47,"Focused tools, with Code Mode named as the escape hatch","The design had left this open, and the research settles it in the direction the existing surface already points. The data tool surface is specific tools — list, describe, fetch — not a general `execute(code)`. Code Mode is not in v1. The deciding argument is the UDF seam.",agent-design/local.md
h48,Environment & context injection,"What gets told to the model about *where* it's running, and how that data gets in — static text baked at build time vs. dynamically interpolated per session.",coding-agent-approaches.md
h49,Why it is a category and not a footnote,"The three claims the four implementations share, in their own words: *Models are better at code than at tool calls. Cloudflare states the mechanism as training-data asymmetry:",code-mode/README.md
h50,Taste as a computable gate,"`dataviz` ships `scripts/validate_palette.py` and a byte-equivalent `.js`, and they are the strongest instance in this entire collection of converting a judgement call into a deterministic check.",agent-generative-output.md
h51,The five decisions worth stealing,"Adoption is proven by diff, never by social signal. Merge status, a resolved thread, an author's ""fixed"" reply, and a same-file edit are each explicitly named as *context rather than adoption proof*.",code-review-approaches.md
h52,"Memory scoped to a sub-agent, not just to a project","Claude Code stores memory per agent *type*: `~/.claude/agent-memory/<agentType>/`, `.claude/agent-memory/<agentType>/`, or `.claude/agent-memory-local/<agentType>/`, chosen by a per-agent `memory: 'user' | 'project' | 'local'` setting, each with its own `MEMORY.md`.",agent-tool-implementations.md
h53,Pattern B: two stages,"Two independent runs, a typed handoff between them. Nothing in the second run depends on the first run's context window. Aider architect/editor is the oldest example: an architect model describes the change, a separate editor model produces edits.",agent-multi-model.md
h54,"The concept list, checked","The starting list was: MCP servers, tools, tool groups, tool visibility and deferral, completion tools, system prompts, starting query, model, sub-agents, user on-behalf-of. All of them are here. A run needs eleven more things, and each is something this folder already decided.",agent-design/keel/README.md
h55,How long the text lasts,"Pydantic separates request-scoped (seen on the request it fires on, gone after: ""adds recency; it doesn't keep a rule in force"") from *conversation-scoped (stays, for ""an obligation the model meets several tool calls later"").",agent-run-steering.md
h56,Claude Code [docs: code.claude.com/docs/en/monitoring-usage],"Not open source; read from the monitoring docs (first 100k of 176k characters). The richest harness telemetry found, and almost none of it uses `gen_ai.*` names. Switches: `CLAUDE_CODE_ENABLE_TELEMETRY=1`, then standard `OTEL_*_EXPORTER` and `OTEL_EXPORTER_OTLP_*`.",telemetry/harnesses-and-sdks.md
h57,"Claude Code at v2.1.303: four summariser prompts, and the user's words as a record","Added 2026-10-19 from `leaked/claude-code/piebald-2.1.303/`.* The nine-section template in §2 is still shipped (with an ""additional instructions"" variant that now offers a 2,000-word cap), but it has three siblings, alternatives the client selects between (the extraction does not show the selection rule):",agent-context-compaction.md
h58,CI-failure fix runs (`source: ci_failure`),"*What: a failed pipeline on a branch Forge owns (or is asked to babysit) dispatches a `mode: implement` run whose envelope carries a `<build_failure>` tag: pipeline/build id, the failed step's name, an excerpt of its log (truncated and sanitized), and the commit the run failed at.",agent-design/medium.md
h59,What this document does not change,"Stated explicitly so the absences read as decisions: No new tool. The v1 surface stays at 11. No new mode, no new run source, no new sub-agent type. No change to the completion gate's trigger, reset rule, or status semantics — only to what it returns (§2c). No change to `Complete.report`'s shape.",agent-design/generative.md
h60,"Skills: a catalog in the prompt, a body on demand","Skills are the field's answer to ""this instruction text is only relevant sometimes"". The shape is the same in every implementation: a catalog of names and one-line descriptions is always in the prompt, and the body of `SKILL.md` enters context only when the model asks for it.",agent-context-file-loading.md
```
