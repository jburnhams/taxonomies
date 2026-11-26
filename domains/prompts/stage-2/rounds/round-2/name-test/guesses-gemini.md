# Name test: gemini guesses

- **CLI**: Antigravity `agy` 1.5.18, `agy -p "<prompt>" --output-format json --print-timeout 1800s --disable-slash-commands --sandbox --model gemini-4-carbon-high`.
- **Model**: `gemini-4-carbon-high` (Gemini 4 Carbon, High).
- **Run**: 2026-11-26T13:28:06Z to 2026-11-26T13:30:42Z (UTC), 153 s. Tokens: 10957 in, 10840 out (9845 thinking).
- Prompt: the whole of `prompt.md` (commit `9ced6b7`), copied alone into a fresh empty temp directory and run from there, as the only input. API keys removed from the environment (billed to the plan).

## Reply (verbatim)

- built-in scope: Context and default instructions shipped inside the agent harness itself that apply across all users, organizations, and projects out of the box.
- compaction summary: A condensed, model-generated summary of earlier conversation and tool activity that replaces older turns when the context window fills up.
- conditional loading: Injecting a piece of context or set of rules only when specific trigger criteria—such as matching file paths, directories, or active tools—are met.
- consolidation: Merging, deduplicating, pruning, and reorganizing accumulated notes or memories into a cleaner and more coherent persistent state.
- context file: A dedicated file in a repository or configuration directory (such as `CLAUDE.md`, `AGENTS.md`, or `GEMINI.md`) read by the harness to give the agent instructions and background context.
- context-file import: A directive or reference inside a context file (such as an `@path` include) that pulls another file's contents into context alongside the parent file.
- conversation scope: Context and state that persist across turns within a single chat thread or interactive session without carrying over to other conversations.
- envelope: The structural wrapper—such as delimiter tags, metadata headers, and message-role containers—used to package a piece of context or payload for delivery to the model.
- framing: The surrounding meta-text or cues that tell the model what an injected piece of context is, where it came from, how authoritative or reliable it is, and how to use it.
- index file: A compact catalog or entrypoint file (such as `MEMORY.md`) loaded upfront to summarize available deeper files so the agent knows what exists and can read details on demand.
- instruction text: Prescriptive rules, directives, and workflow guidance written to tell the agent how to behave and operate, as opposed to factual knowledge or execution logs.
- kept knowledge: Durable facts, project conventions, domain details, and user preferences retained across sessions so the agent does not have to rediscover them each run.
- learning: Extracting reusable lessons, preferences, or behavioral adjustments from actual runs and user corrections so future executions improve.
- memory: The subsystem or persistent store through which an agent saves and recalls learned knowledge across separate sessions.
- note: A discrete, self-contained written entry or topic file capturing a specific observation, fact, or piece of saved context.
- organization scope: Shared policies, instructions, and context configured at the company or team level that apply across all users and projects within that organization.
- precedence: The priority rules determining which instruction or context source overrides another when multiple scopes or files conflict.
- progressive disclosure: Giving the model only lightweight summaries, names, or pointers upfront and revealing full file, skill, or tool details in stages only when needed.
- project scope: Context, instructions, and saved knowledge tied to a specific repository or workspace and shared across runs within that project.
- promotion: Elevating temporary or narrowly scoped information—such as a scratchpad item, session finding, or local note—into a more durable form or broader scope like project rules or user memory.
- recording: Capturing events, observations, decisions, or raw notes from a live or completed run into storage.
- reduction: Paring down active context in the model's window—through techniques like truncation, pruning, or compaction—to stay within token budgets and preserve model focus.
- request scope: Ephemeral context supplied only for a single user turn or model call rather than persisting across the rest of the conversation.
- retrospective: A post-run or periodic review pass over completed execution history to extract lessons, spot recurring mistakes, and update persisted knowledge or instructions.
- run history: The chronological transcript of user prompts, model responses, reasoning steps, tool calls, and tool outputs accumulated over an agent's execution.
- scratchpad: Mutable working space used by an agent during a task or session to track plans, checklists, and intermediate findings without committing them to long-term storage.
- staleness: The condition in which saved context, summaries, or memories drift out of date because the underlying codebase, environment, or user intent has changed since they were written.
- supply: The process and mechanisms by which the harness gathers, selects, assembles, and feeds context into the model's window.
- truncation: Cutting off oversized text—such as large tool outputs, file reads, or oldest turns—at a hard size or token limit without summarizing what was dropped.
- user scope: Personal instructions, preferences, and memories stored for a single individual that apply across all of their projects and conversations.
- write gate: A filter, validation check, or approval step that controls whether candidate information is allowed to be written into persistent memory or context files.
