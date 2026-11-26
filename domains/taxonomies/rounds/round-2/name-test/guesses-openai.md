# Name test: openai guesses

- **CLI**: codex-cli 0.172.0, `codex exec --skip-git-repo-check --sandbox read-only --ephemeral --ignore-user-config --ignore-rules -m gpt-6.2-astra -c model_reasoning_effort=high -c web_search=disabled --json -o answer -`, prompt on stdin.
- **Model**: `gpt-6.2-astra`, reasoning effort high. Read-only sandbox, user config and MCP servers not loaded, web search off; the event log shows no tool calls.
- **Run**: 2026-11-26T07:49:53Z to 2026-11-26T07:50:13Z (UTC). Tokens: 18707 in, 347 out (0 reasoning), on the ChatGPT plan.
- **Not removable**: Codex's own system prompt, and the user's global `~/.codex/AGENTS.md` (about this machine's repos, nothing about taxonomies).
- Prompt: the whole of `name-test/prompt.md` (commit `7004a36`), copied alone into a fresh empty temp directory and run from there, as the only input. API keys removed from the environment (billed to the plan).

## Reply (verbatim)

- part / purpose: I’d expect this to say who the taxonomy is for and what they need to do with it.
- part / boundary: I’d expect this to say which things belong in the taxonomy and which fall outside its scope.
- part / structure: I’d expect this to cover how the sorting questions and their allowed answers fit together.
- part / naming: I’d expect this to cover the words people see for each sorting question and answer.
- part / meaning: I’d expect this to define what each answer covers so people can distinguish it from similar answers.
- part / evidence: I’d expect this to say what examples or observations support a rule or a choice of terms.
- part / change: I’d expect this to cover how people add, revise, or retire terms and rules.
- stage / framing: I’d expect this to be when people agree on the problem the taxonomy should solve and the scope of the work.
- stage / building: I’d expect this to be when people draft the sorting questions, labels, and definitions.
- stage / testing: I’d expect this to be when people try the taxonomy on real examples to see where it works and where they disagree.
- stage / governing: I’d expect this to be when people oversee the taxonomy in use and resolve requests to change it.
- check / script: I’d expect a program to apply a stated test and report whether the rule is met.
- check / judgement: I’d expect a person to weigh the evidence against the rule and decide whether it is met.
- check / owner decision: I’d expect the person accountable for the taxonomy to have the final say on whether the rule is met.
