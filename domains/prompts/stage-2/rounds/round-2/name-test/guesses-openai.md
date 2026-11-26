# Name test: openai guesses

- **CLI**: codex-cli 0.172.0, `codex exec --skip-git-repo-check --sandbox read-only --ephemeral --ignore-user-config --ignore-rules -m gpt-6.2-astra -c model_reasoning_effort=high -c web_search=disabled --json -o answer -`, prompt on stdin. No tool calls in the event log.
- **Model**: `gpt-6.2-astra`, reasoning effort high.
- **Run**: 2026-11-26T13:28:06Z to 2026-11-26T13:28:33Z (UTC). Tokens: 18766 in, 642 out (0 reasoning).
- Prompt: the whole of `prompt.md` (commit `9ced6b7`), copied alone into a fresh empty temp directory and run from there, as the only input. API keys removed from the environment (billed to the plan).

## Reply (verbatim)

- built-in scope: The context comes from the agent product itself and applies wherever its defaults are in effect.
- compaction summary: A shorter account of earlier turns takes their place in the model’s context so the conversation can continue.
- conditional loading: The harness pulls text into context only when a condition matches, such as the agent working on a particular file.
- consolidation: Related or duplicate notes are combined into a single account worth keeping.
- context file: A file holds instructions or background information that the harness reads into the model’s context.
- context-file import: One context file references another so the harness includes the referenced text when it loads the first file.
- conversation scope: The text applies across turns in one conversation.
- envelope: The harness wraps a piece of text with information about where it came from or how the model should treat it.
- framing: The wording around supplied text tells the model what role that text plays, such as an instruction to follow or a passage to analyze.
- index file: A file lists available context with enough description for the agent to decide which entries to open.
- instruction text: This is text that tells the agent what to do or what rules to follow.
- kept knowledge: This is information selected for future use, such as a decision and the reason behind it.
- learning: The agent draws a lesson from experience that can change how it handles a later task.
- memory: This is the mechanism by which an agent retains information and recalls it when it becomes relevant.
- note: A note is an individual piece of saved text the agent can consult later.
- organization scope: The text applies across users and projects within one organization.
- precedence: This determines which instruction wins when two applicable instructions conflict.
- progressive disclosure: The agent sees a brief description first and can open the full material when it needs the detail.
- project scope: The text applies when the agent works in a particular project or repository.
- promotion: A piece of context moves into more durable or more widely applicable use, as when a task note becomes a project instruction.
- recording: The agent or harness captures what happened during work so it can be revisited later.
- reduction: The harness shrinks the amount of material the model receives to fit the available context budget.
- request scope: The text applies to a single request.
- retrospective: After a run, the agent reviews what happened and decides which lessons to carry forward.
- run history: This is the chronological record of what the agent did and what happened during its runs.
- scratchpad: This is temporary working space where the agent tracks intermediate results, plans, or open questions during a task.
- staleness: Saved context has become outdated because the facts or circumstances it describes have changed.
- supply: This is how the harness gets relevant material into the context the model receives.
- truncation: The harness cuts off part of a message, tool result, or history when it exceeds a limit.
- user scope: The text follows one user across their projects and conversations.
- write gate: A rule or check decides whether a proposed addition or change to persistent context gets saved.
