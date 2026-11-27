# Name test: gemini guesses

- **CLI**: Antigravity `agy` 1.5.18, `agy -p "<prompt>" --output-format json --print-timeout 1800s --disable-slash-commands --sandbox --model gemini-4-carbon-high`.
- **Model**: `gemini-4-carbon-high` (Gemini 4 Carbon, High).
- **Run**: 2026-11-27T08:52:08Z to 2026-11-27T08:55:00Z (UTC), 169 s. Tokens: 10954 in, 9458 out (8274 thinking).
- Prompt: the whole of `prompt.md` (commit `9d2b864`), copied alone into a fresh empty temp directory and run from there, as the only input, in a session separate from the rating runs. API keys removed from the environment (billed to the plan).

## Reply (verbatim)

- allow list: A configured set of pre-approved tools, commands, paths, or network targets that an agent may use automatically without being blocked or requiring manual confirmation.
- approval: An explicit decision from a user or designated reviewer granting permission for a gated agent action to execute, either once or as a reusable rule.
- ask a person: A control or interaction step where the harness or agent pauses autonomous execution to request a decision, permission, or clarification from a human.
- authority: The scope of rights and power held by a principal, policy layer, or agent to perform, permit, or forbid specific actions.
- blocking monitor: A runtime watcher that inspects proposed actions or outputs inline and holds up or vetoes execution before an unsafe or policy-violating step can take effect.
- compaction: Summarizing, pruning, or condensing older conversation turns and tool outputs so the model's context stays within token limits and focused on relevant state.
- completion gate: A verification check—such as passing tests, linters, or stop hooks—that prevents an agent from declaring a task finished until required exit criteria are met.
- escalation: Routing an action or problem upward to a higher-privilege level—such as requesting unsandboxed execution, human review, or supervisor intervention—when current permissions or capabilities are insufficient.
- gate: A control checkpoint in the harness where execution cannot advance past a boundary until a policy rule, verification check, or human decision is satisfied.
- grade: An evaluation or score assessing how well an agent's output, step, or trajectory meets quality, correctness, or policy criteria.
- halt: Immediately terminating an active agent run—due to a user interrupt, hard policy violation, fatal error, or exhausted budget—so no further turns or actions occur.
- handoff: Transferring active control, responsibility, and working context of a task from one agent, specialized role, or human operator to another.
- incoming text: External text entering the model's context from users, files, tool outputs, or external sources that the harness assembles, frames, or screens before model consumption.
- loop detection: A harness safeguard that spots repetitive, non-progressing agent behavior—such as calling the same failing command repeatedly—so it can nudge, redirect, or stop the run.
- permission mode: A run-level operating posture—such as read-only plan mode, ask-before-edits, auto-edit, or full bypass—that sets baseline rules for which actions are allowed, gated, or denied.
- precedence: The priority order used to resolve conflicts when multiple rules or configuration layers apply to the same action, such as explicit deny rules or admin policies overriding project allow rules.
- prompt injection: Adversarial or untrusted instructions embedded inside data the model reads that attempt to hijack the agent's behavior or trigger unauthorized tool actions.
- recover: Restoring a disrupted run to a workable state after a crash, error, or context failure—through state repair, fallback, or rollback—so execution can continue instead of failing outright.
- redirect: Stopping or rejecting the agent's current action or line of pursuit and sending the run down a different path with new instructions or constraints.
- replay: Re-running a recorded sequence of messages, model turns, or tool events from a prior run to reconstruct state, audit behavior, or test harness changes.
- resume: Continuing a paused, interrupted, or saved run from its checkpointed state and conversation history rather than starting over from scratch.
- retry: Re-attempting a single failed step—such as a transient API error, malformed tool call, or failed check—from just before that step failed.
- risk driver: A concrete property of a proposed action or its context—such as network access, destructive flags, sensitive paths, or untrusted input—that increases the assessed risk of letting it happen.
- risk tier: A discrete severity bucket—such as read-only, reversible local write, or high-impact external/destructive—assigned to an action to determine what sandboxing, monitoring, or approval it requires.
- run budget: A quantitative limit placed on a run—such as maximum turns, tokens, wall-clock time, or cost—that stops or constrains execution once spent.
- run course: The unfolding trajectory, direction, and sequence of states an agent run follows from start toward completion as shaped by model choices and harness controls.
- sandbox: An isolated OS, container, filesystem, or network boundary that restricts the real-world reach and side effects of commands or code executed by the agent.
- steer: Feeding mid-run guidance or corrective cues into an active run to adjust how the agent approaches its current goal without aborting or restarting the run.
- suspension: Cleanly pausing an in-progress run—often persisting its state while awaiting approval, human input, or an external event—until it is ready to resume.
- system reminder: A harness-injected note inserted alongside user or tool messages mid-run to refresh instructions, surface environment state, or nudge model behavior without rewriting the system prompt.
- tool action: A concrete external operation requested by the model through a tool call, such as executing a shell command, modifying a file, or invoking an MCP server.
- trust gate: A checkpoint that withholds sensitive capabilities—such as loading repo hooks, MCP servers, or workspace configs, or acting on unfamiliar sources—until the user or policy explicitly marks that source as trusted.
- work product: The durable output artifact an agent run produces to fulfill its task—such as code diffs, new files, commits, or a report—as distinct from the intermediate conversation and tool trace.
