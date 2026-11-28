# Rater claude: raw reply

- **CLI**: Claude Code 2.1.332 (Claude Code), `claude -p --model opus --effort high --tools "" --strict-mcp-config --mcp-config '{"mcpServers":{}}' --output-format json`, prompt on stdin.
- **Model**: `claude-opus-5-5`, effort high. No tools, no MCP servers, no web; 1 turn.
- **Run**: 2026-11-28T07:12:50Z to 2026-11-28T07:13:35Z (UTC), 45 s. Tokens: 12997 in, 4268 out (3365 thinking); list-price equivalent $0.18, on the Claude plan.
- **Not removable**: Claude Code's own system prompt, which also carries the user's global `~/.claude/CLAUDE.md` and memory index (about this machine's repos, nothing about taxonomies).
- Prompt: the whole of `prompt-claude.md` (kit commit `dfebdbb`), copied alone into a fresh empty temp directory and run from there, as the only input. API keys and proxy variables removed from the environment (billed to the plan), no proxy.
- CSV well formed on the first run (40 rows, listed values only); no re-run.

## Reply

```
id,area,modality,trait,note
h01,evaluation,spoken,content,
h02,generation,spoken,identity,"unsure: adaptation result, but the point is how much to record (elicitation)"
h03,operations,spoken,whole-voice,
h04,evaluation,written,identity,
h05,evaluation,written,identity,
h06,generation,written,expression,"unsure: conditioning on audience could be representation"
h07,evaluation,written,content,"unsure: length bias names no clear trait"
h08,representation,spoken,expression,"unsure: a survey of systems (generation) sorted by control strategy"
h09,evaluation,spoken,expression,"unsure: held-out set; style is the only part named"
h10,elicitation,spoken,expression,
h11,representation,spoken,expression,
h12,elicitation,spoken,expression,
h13,evaluation,written,whole-voice,"unsure: judge bias names no part of the voice"
h14,elicitation,spoken,content,"unsure: student_error names no part; coverage is the first part named"
h15,preparation,written,whole-voice,"unsure: redaction part would be governance; raw text keeps every trait"
h16,representation,spoken,expression,
h17,generation,spoken,content,
h18,evaluation,spoken,naturalness,
h19,representation,spoken,identity,"unsure: about the reference prompt length, could be generation"
h20,evaluation,spoken,whole-voice,"unsure: protocol names no part"
h21,elicitation,spoken,content,
h22,evaluation,spoken,naturalness,
h23,generation,spoken,identity,
h24,evaluation,written,content,
h25,preparation,spoken,expression,
h26,elicitation,spoken,naturalness,"unsure: synthesises badly is a vague quality"
h27,generation,written,identity,"unsure: under a leakage heading, but the finding is about prompt examples"
h28,elicitation,spoken,naturalness,"unsure: quality bar not specified"
h29,evaluation,written,identity,
h30,representation,spoken,expression,
h31,generation,written,identity,"unsure: personalisation names no part directly"
h32,representation,spoken,naturalness,"unsure: SNR is first named; captions mostly describe style"
h33,generation,spoken,expression,
h34,preparation,spoken,identity,
h35,elicitation,spoken,naturalness,
h36,representation,spoken,expression,
h37,generation,spoken,expression,
h38,operations,spoken,whole-voice,
h39,elicitation,spoken,expression,
h40,evaluation,written,identity,
```
