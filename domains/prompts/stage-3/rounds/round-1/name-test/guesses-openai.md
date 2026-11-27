# Name test: openai guesses

- **CLI**: codex-cli 0.172.0, `codex exec --skip-git-repo-check --sandbox read-only --ephemeral --ignore-user-config --ignore-rules -m gpt-6.2-astra -c model_reasoning_effort=high -c web_search=disabled --json -o answer -`, prompt on stdin. No tool calls in the event log.
- **Model**: `gpt-6.2-astra`, reasoning effort high.
- **Run**: 2026-11-27T08:52:08Z to 2026-11-27T08:52:38Z (UTC). Tokens: 18769 in, 637 out (0 reasoning).
- Prompt: the whole of `prompt.md` (commit `9d2b864`), copied alone into a fresh empty temp directory and run from there, as the only input, in a session separate from the rating runs. API keys removed from the environment (billed to the plan).

## Reply (verbatim)

- allow list: A list of tools, actions, or targets that a policy explicitly permits.
- approval: A decision granting permission for a proposed action to proceed.
- ask a person: The agent requests an answer or decision from someone when it needs their input to continue.
- authority: The right of a person or system component to direct the agent or authorize an action.
- blocking monitor: A component that watches a run and can prevent it from advancing when it detects a specified condition.
- compaction: The harness condenses earlier conversation and tool results so the model has room for new context.
- completion gate: A check that must pass before the agent can declare its task finished.
- escalation: The agent refers a decision to someone or something with greater authority.
- gate: A check whose outcome determines whether a proposed step can proceed.
- grade: An assessment of how well a result meets specified criteria.
- halt: The current run stops taking further steps.
- handoff: Responsibility for continuing a task passes to another agent or person along with the context they need.
- incoming text: Text entering the run from a user, tool, or other source that may become part of the model’s context.
- loop detection: The harness looks for repeated actions or states that indicate the agent is making no progress.
- permission mode: A setting that determines which actions the agent can take automatically, which require approval, and which are blocked.
- precedence: The rule that determines which instruction or policy wins when several conflict.
- prompt injection: An attempt to redirect the agent by placing instructions in content it was asked to read or process.
- recover: The system restores a usable state after a failure so work can continue.
- redirect: The current run switches to a different objective or course of action.
- replay: The system uses a record of an earlier run to reconstruct how it unfolded.
- resume: A paused run continues from the state it preserved.
- retry: The agent attempts a step again after an earlier attempt failed.
- risk driver: A feature of an action or its circumstances that contributes to risk, such as how hard its effects would be to undo.
- risk tier: A category indicating how risky an action is and what safeguards it warrants.
- run budget: A limit on the time, tokens, money, or steps a run may consume.
- run course: The path a run takes as it continues, changes direction, pauses, or ends.
- sandbox: An execution environment that restricts which resources an agent’s tools can access or change.
- steer: A person or controller gives an active agent guidance that influences its next steps.
- suspension: A run is put on hold with enough state preserved to continue later.
- system reminder: A message the harness inserts into the model’s context to bring a constraint or current condition to its attention.
- tool action: A specific operation the agent requests through a tool, such as reading a file.
- trust gate: A check on whether a source is trusted enough for its input to guide a particular action.
- work product: The artifact or result the agent produces to fulfill the task.
