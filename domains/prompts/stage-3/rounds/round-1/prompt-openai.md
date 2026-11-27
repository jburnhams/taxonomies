# Rater prompt: prompts taxonomy, stage 3 (control area), round 1

You are classifying 30 items for a taxonomy agreement test. Use only the definitions below; do not look anything up, do not read any files, and do not use other knowledge of the repo they come from.

Each item is one section of a research repo about how AI agent products and harnesses are built (Claude Code, Codex, Gemini CLI, Goose, MCP, agent SDKs) and of the designs of the repo owner's own agent platform (Keel, with configurations Forge and Lens). An item is the section's heading, the first lines under it (`gist`), and the file it is in (`from`).

For every item, answer all three questions with exactly one value each. If no value fits, still pick the closest one and write `unsure` plus a few words in the note column.

Rules:
- Classify the mechanism, approach or design choice the section describes, not the document it is in. The `from` column is part of the item.
- in_area: `yes` if the mechanism is about the `control` area as defined below (whether an action may happen, and what stops, redirects or restarts a run); `no` if another area's definition fits it better (for example how a tool matches or parses its input is `tool`, what is loaded into the prompt or how it is cut down is `context`, where work goes next between sub-agents is `coordination`, checking whether finished work is right is `verification`, a design roadmap or cost report is `operations`). If `no`, still answer the other two with the closest values.
- target: what the control decides about. One action a tool would take, or a limit set once on what a run or sub-agent's tools may do (a permission mode, a sandbox, a tool scope, authority), or a step a framework runs again: `tool-action`. Whether the whole run goes on, where it is pointed, its budget, and how it may end: `run-course`. Text arriving from outside the people running the agent (tool results, web pages, untrusted files, emails, other sessions) and how far it may direct the agent: `incoming-text`. A change or output the run has finished, before it merges or is acted on (a pull request's risk tier, a merge gate): `work-product`.
- response: what the control does when it acts. Settles it itself, letting it through or refusing it: `gate` (also use `gate` when the item is about a control's whole allow/ask/refuse choice). Passes the decision to a person and waits: `ask-person`. Sets a level (a risk tier, a trust level, an authority posture) that other rules then read: `grade`. Adds text that changes what the agent does next while the run goes on: `redirect`. Runs something again or carries it on after a failure or stop: `recover`. Stops or suspends the run, or fixes the ways it may end: `halt`.
- If an item describes several mechanisms, classify the first one named; if it surveys several approaches without naming one first, classify the one it recommends, or pick the closest and mark `unsure`.

Answer as CSV only, with this header and one row per item, in the items' order. Quote any note that contains a comma.

```
id,in_area,target,response,note
```

## The questions and their values

- **in_area**: Is it about the `control` area? Values: `yes`, `no`
- **target**: What does it govern? Values: `work-product`, `run-course`, `tool-action`, `incoming-text`
- **response**: What does it do when it acts? Values: `ask-person`, `halt`, `recover`, `gate`, `redirect`, `grade`

## The areas (for `in_area`)

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

### coordination (`coordination`)

- **Definition**: Coordination is an area of an agent system that covers how agents and runs are arranged and where work goes next.
- **Scope**: Includes sub-agents and orchestrators, triggers, pipelines and their edges, hand-offs between runs, entrypoints and the kinds of run a system offers. Excludes deciding whether an action is allowed (`control`).
- **Aliases**: orchestration, multi-agent
- **Near miss**: A tool that ends a run: choosing which ending applies is `control`; the follow-up run it dispatches is `coordination`.
- **Kind**: thing
- **Facet**: `area`

### output (`output`)

- **Definition**: Output is an area of an agent system that covers what a run produces for people to read or use.
- **Scope**: Includes turn text and its style, narration, titles, generated files and artefacts, interactive views, tables and charts, and how they are delivered. Excludes records kept for operators (`operations`).
- **Aliases**: deliverable, response, artefact
- **Near miss**: A transcript of the run: it is produced, but for operators and analysis, so it is `operations`.
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

### model calling (`model`)

- **Definition**: Model calling is an area of an agent system that covers how models are called and chosen.
- **Scope**: Includes providers and their wire formats (dialects), routing between models, reasoning effort and thinking budgets, prompt caching, and what happens when a model's response is broken. Excludes what the model is told (`context`) and which tools it is offered (`tool`).
- **Aliases**: model access, LLM access, inference
- **Near miss**: Deferring tool definitions so the cache survives: the change is to how the request is assembled, so it is `model` when the point is the cache and `tool` when the point is which tools are loaded.
- **Kind**: thing
- **Facet**: `area`

### operations (`operations`)

- **Definition**: Operations is an area of an agent system that covers running agents and keeping their records.
- **Scope**: Includes telemetry, traces and transcripts, storage and dashboards, version control and commits, local compute, provenance of content, deployment. Excludes checking the quality of the work (`verification`).
- **Aliases**: ops, observability
- **Near miss**: A loop detector that stops a run: it reads telemetry, but stopping decides, so it is `control`.
- **Kind**: thing
- **Facet**: `area`

## Definitions of the values

### grade (`grade`)

- **Definition**: Grade is a control response: the control sets a level, such as a risk tier or a trust level, that other rules then read.
- **Scope**: Includes risk tiers and their drivers, a predictor's score, a context file's authority posture, and what a risk output should contain.
- **Aliases**: tiering, scoring
- **Near miss**: An eval's score: grades the quality of work, `verification`.
- **Kind**: happening
- **Facet**: `response`

### run course (`run-course`)

- **Definition**: A run course is a control target: whether a run goes on, where it is pointed and how it ends.
- **Scope**: Includes budgets, loop detection, steers, recovery after a crash or a limit, suspension and the allowed endings.
- **Aliases**: the run
- **Near miss**: A run's sub-agent spawning: where work goes next is `coordination`, unless the item is about what the sub-agent may do (`tool-action`).
- **Kind**: thing
- **Facet**: `target`

### redirect (`redirect`)

- **Definition**: Redirect is a control response: the control adds text that changes what the agent does next, and the run goes on.
- **Scope**: Includes steers, nudges, loop warnings and a reminder of a rule.
- **Aliases**: course correction
- **Near miss**: A `system-reminder` that only reports a fact: `supply` in the context area, not a control response.
- **Kind**: happening
- **Facet**: `response`

### ask a person (`ask-person`)

- **Definition**: Ask a person is a control response: the control passes the decision to a person and waits for the answer.
- **Scope**: Includes permission prompts, a command escalated to the user, a pull request held for a required human reviewer, and what counts as the person's answer.
- **Aliases**: prompt the user
- **Near miss**: A `handoff`: gives the person the work, not one decision.
- **Kind**: happening
- **Facet**: `response`

### work product (`work-product`)

- **Definition**: A work product is a control target: a change or other output a run has finished, before it is merged, published or acted on.
- **Scope**: Includes a pull request's risk tier, merge gates, protected labels and required reviewers.
- **Aliases**: the change
- **Near miss**: Checking whether the change is right (tests, review findings): `verification`. How much scrutiny it gets, and whether it may merge without a person, is control.
- **Kind**: thing
- **Facet**: `target`

### gate (`gate`)

- **Definition**: Gate is a control response: the control settles the case itself, letting it through or refusing it.
- **Scope**: Includes an allow list match, a blocking monitor's verdict, a sandbox refusal, a trust gate and a merge gate. Use it for an item about the whole choice of a control that can allow, ask or refuse.
- **Aliases**: allow or refuse, allow/deny
- **Near miss**: `ask-person`: the control does not settle it.
- **Kind**: happening
- **Facet**: `response`

### incoming text (`incoming-text`)

- **Definition**: Incoming text is a control target: text that reaches the model from outside the people running it, and how much it may direct the agent.
- **Scope**: Includes tool results, web pages, files from an untrusted workspace, emails and messages from other sessions; trust gating and defences against prompt injection.
- **Aliases**: untrusted input, external content
- **Near miss**: A context file's precedence over another one: which instruction text wins, area `context` (`precedence`), unless the item is about refusing text that is not trusted.
- **Kind**: thing
- **Facet**: `target`

### halt (`halt`)

- **Definition**: Halt is a control response: the control stops or suspends a run, or fixes the ways it is allowed to end.
- **Scope**: Includes run budgets that stop a run, suspension until something resolves, interrupts and aborts, and completion tools that are a run's only endings.
- **Aliases**: stop
- **Near miss**: Refusing one action while the run goes on: `gate`.
- **Kind**: happening
- **Facet**: `response`

### tool action (`tool-action`)

- **Definition**: A tool action is a control target: one action a run's tools would take, or the set of actions a run or sub-agent may take at all.
- **Scope**: Includes a command or file write waiting for approval, a sandbox's limits, a sub-agent's tool scope and authority, and a step a framework replays. Excludes whether the run as a whole goes on (`run-course`).
- **Aliases**: command
- **Near miss**: A tool's own matching or parsing rules (a whitespace-tolerant edit): how the tool works, area `tool`, not whether it may run.
- **Kind**: thing
- **Facet**: `target`

### recover (`recover`)

- **Definition**: Recover is a control response: the control runs something again or carries it on after it failed or stopped.
- **Scope**: Includes retries, replays, resuming a run or a delegate, and requeueing lost tool calls.
- **Aliases**: re-run
- **Near miss**: `halt` with a later resume: when the item is about the stop and its wake condition, `halt`; when it is about how the work picks up, `recover`.
- **Kind**: happening
- **Facet**: `response`

## Items

```csv
id,item,gist,from
kr01,"Guardian, in two tiers","The original Permissions section describes one LLM reviewer. There are now two models in the loop, with different jobs. *Tier 1 — the async classifier (`guardian_v2.classifier_instructions`, captured in `guardian-v2-classifier.md`).",codex/README.md
kr02,Where the enforcement actually lives: harness vs. prompt,"A cross-cutting structural finding, not tied to any one axis above: for most sources with a real mechanism, the model's own system prompt says nothing about it. Claude Code (leaked):",agent-permissions-approval.md
kr03,Recursion and tool-scope limits,"Can a sub-agent spawn its own sub-agents? Can it use every tool the orchestrator can, or a deliberately narrower set?",agent-subagent-architectures.md
kr04,"Redundant, model-authored parameters that exist to steer, not to compute","A recurring trick worth naming: parameters whose value the tool barely uses, included because *writing them changes the model's behaviour* or gives the human something to read. Gemini CLI's `replace` requires an `instruction` field alongside `old_string`/`new_string`:",agent-tool-implementations.md
kr05,The authority chain: a risk analysis aimed at the exact thing that goes wrong,The security pass adds a section that runs only when the diff materially changes authority:,clawsweeper/README.md
kr06,"Budgets, truncation, and staleness","*Only Codex has a byte budget on the context-file hierarchy: `project_doc_max_bytes`, default 32 KiB, shared across all files.",agent-context-file-loading.md
kr07,"Completion tools: separate tools, or a flag on a tool?","*Neither. The spec declares a contract, and the harness generates the tool. Authors don't write `Complete`, and they can't mark an arbitrary tool as run-ending.",agent-design/keel/endings.md
kr08,Hosted products: what is shown and what is hidden,"*CodeRabbit Triage cards (`docs.coderabbit.ai/triage/your-triage-view`) show separate signals, each tied to the reviewed commit:",agent-risk-assessment.md
kr09,Proof is its own axis,"ClawSweeper treats real-behaviour proof as separate from correctness: ""Tests … and CI support proof and never replace it"". Forge reviews without running anything, so it can't produce proof. It can *report* whether proof exists: `proof.path` is set from what the PR shows:",agent-design/risk.md
kr10,What the grader may conclude,"Deep Agents is the careful one (`agentic-sdks/deepagents.md` §4): per-criterion verdicts, a frozen criterion list that cannot shrink, a coverage retry, and a `satisfied` verdict downgraded to `unverified` when coverage stays short.",agent-run-steering.md
kr11,"Compaction needs a second budget, and a degradation says what it did not damage","*Amends `generative.md` §2b's refusal vocabulary; the compaction half lands in `future.md`. Two small things, both from failure modes this design has not written down.",agent-design/cloudflare.md
kr12,"Stopped, not dead: a resource limit inside a live run","Added 2026-11-02 in the weekly pass, from `leaked/claude-code/piebald-2.1.316/`.* §1 covers a runner that died. Claude Code 2.1.314 adds the case just short of that: the sandbox enforces a limit itself, kills the work, and the run carries on.",agent-run-recovery.md
kr13,The four-tier confirmation taxonomy,"`confirmation_policies` (captured in `gpt-6-astra_confirmation-policy.md`) is an 11 KB policy document covering computer and browser use only — ""It does not apply to terminal or shell commands, and any other tools such as MCP connectors."" Four modes: 1.",codex/README.md
kr14,"Claude Code's auto-mode classifier, read from the shipped prompt","Added 2026-10-19.* The classifier is a 14k-token prompt, `agent-prompt-security-monitor-for-autonomous-agent-actions-first-part.md`, plus pieces appended by context.",agent-permissions-approval.md
kr15,October 2026: delegation never widens authority,"Added 2026-10-19.* In one week (2026-10-07 to 2026-10-16) four harnesses closed the same class of hole: a sub-agent running with more authority than the agent that delegated to it, or with authority taken from somewhere other than its parent. Each fix is in code, with tests. *Goose:",agent-subagent-architectures.md
kr16,"Stance: ""abundant intelligence, scarce trust""","`VISION.md` states the design rule more plainly than any other source here: Whenever behavior can be a model judgment with a clear prompt and an auditable output, prefer that over deterministic machinery. Code exists for the trust boundary only:",clawsweeper/README.md
kr17,Three postures on authority,"The same class of file — a Markdown document any contributor can commit — is introduced to the model three incompatible ways: *Supreme. Claude Code: *""These instructions OVERRIDE any default behavior and you MUST follow them exactly as written.""* *Subordinate on safety, superior on everything else.",agent-context-file-loading.md
kr18,Predicting change risk from history: Meta's DRS and RADAR,"Added 2026-10-17 (third pass).* Every source above judges a change by reading it. Meta has run the other approach for over two years: predict the risk of a diff from what similar diffs did in production, and gate on the prediction.",agent-risk-assessment.md
kr19,"How the tier is computed: a floor, then escalation only","Three contributors, combined with `max`. None of them can lower the tier another one set.",agent-design/risk.md
kr20,Whether it blocks the run,"Reminders, nudges and notices: no extra call, nothing to block on. The trajectory judge runs concurrently: the agent keeps going and the steer lands on a later request. A tick that finds the last evaluation still running is skipped.",agent-run-steering.md
kr21,Claude Code: two reminders and a requeue tool,"`system-reminder-tool-calls-lost-to-session-restart.md` lists, by label, every call the previous turn issued that has no result, and says they ""may not have run, or not completely. Check before issuing them again, and decide whether they are still needed."" Two variants:",agent-run-recovery.md
kr22,The 2026-10-17 re-read: Guardian learns to look things up (targeted),"A targeted pass over `ee6814b..ce0323f2f2` (2026-09-12 → 2026-10-17), limited to review, Guardian and context assembly. The `ReviewTask` rubric and `codex-rs/prompts/templates/review/` are unchanged. `/review` gained only lifecycle fixes (#50804, #51217). Guardian changed the most:",codex/README.md
kr23,Risk classification: static rules vs. LLM-based judgment,"The central axis this doc set out to investigate, and the one with the widest spread of sophistication found anywhere in this collection.",agent-permissions-approval.md
kr24,Concurrency and write-safety across sub-agents,"Once an orchestrator can fire off more than one sub-agent, a new failure mode appears that ordinary single-tool parallelism doesn't have: two sub-agents editing the same file at once. Only a few sources address this directly.",agent-subagent-architectures.md
kr25,"Two granularities, one problem","They are the same problem at different time scales. The action-risk systems are older and much more mechanised, and a PR-level design should borrow from them most. The clearest example is Guardian's rule that a `low` is valid only under the exact authorization snapshot it was computed in (§4).",agent-risk-assessment.md
kr26,"Effort is not risk, and residual risk is not inherent risk","Effort (estimated human review minutes, gitStream-style, from additions and deletions by change type) is reported separately in `attention.effort_minutes`. It never feeds the tier.",agent-design/risk.md
kr27,Where it goes relative to the cache,"At the tail, and never edited once sent. See `agent-prompt-cache-health.md` §3: a reminder at the front of the request busts the prefix on every firing, and deleting an old one invalidates later thinking blocks.",agent-run-steering.md
kr28,"Loops inside a run: when is a retry ""the same"" retry?","Added 2026-11-02, from OpenHands SDK #6278 (`c3985a4`, `openhands-sdk/openhands/sdk/conversation/stuck_detector.py` and the PR's `.pr/validation-loops.md` evidence file).* Every harness here that detects in-run loops counts repeats of ""the same call"", and the definition of ""same"" decides what it catches.",agent-run-recovery.md
kr29,"Email turns: whose words count, and what a bare ""yes"" approves","Added 2026-10-26.* Claude Code 2.1.305 added rules to the auto-mode classifier for a session whose user can write to it by email (`agent-prompt-security-monitor-email-sender-turns.md`). Only ""the sender's own new words"" establish intent.",agent-permissions-approval.md
kr30,Who sets the level,"Five patterns, from least to most robust: 1. Model self-report. One pass returns a level (PR-Agent's `risk_level`, Bugbot's `riskScore`). Cheap and explainable, but it can go down as easily as up, and it inherits the reviewer's blind spots. 2. Deterministic rules on what was touched.",agent-risk-assessment.md
```
