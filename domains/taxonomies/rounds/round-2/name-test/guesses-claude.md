# Name test: claude guesses

- **CLI**: Claude Code 2.1.332 (Claude Code), `claude -p --model opus --effort high --tools "" --strict-mcp-config --mcp-config '{"mcpServers":{}}' --output-format json`, prompt on stdin.
- **Model**: `claude-opus-5-5`, effort high. No tools, no MCP servers, no web; 1 turn.
- **Run**: 2026-11-26T07:49:53Z to 2026-11-26T07:50:08Z (UTC). Tokens: 3984 in, 583 out (0 thinking); list-price equivalent $0.04, on the Claude plan.
- **Not removable**: Claude Code's own system prompt, which also carries the user's global `~/.claude/CLAUDE.md` and memory index (about this machine's repos, nothing about taxonomies).
- Prompt: the whole of `name-test/prompt.md` (commit `7004a36`), copied alone into a fresh empty temp directory and run from there, as the only input. API keys removed from the environment (billed to the plan).

## Reply (verbatim)

- part / purpose: Rules about why the taxonomy exists: what decisions or tasks it must support and for whom.
- part / boundary: Rules about scope, meaning which items and topics are in or out of the area the taxonomy covers.
- part / structure: Rules about how the terms and facets are arranged, such as hierarchy depth, number of facets, and whether categories are mutually exclusive and exhaustive.
- part / naming: Rules about the labels themselves: wording, length, consistency, and avoiding jargon or ambiguity.
- part / meaning: Rules about definitions, so that each term has a clear written scope note that tells it apart from its neighbours.
- part / evidence: Rules about what real material (sample items, usage data, test sorts) must back up the taxonomy's choices.
- part / change: Rules about how terms are added, merged, renamed or retired over time, and how that history is recorded.
- stage / framing: The first stage, where the purpose, scope, users and success criteria are agreed before any terms are drafted.
- stage / building: The stage where the facets and terms are drafted, defined and arranged.
- stage / testing: The stage where the draft is tried against real items or fresh people to see if it sorts reliably.
- stage / governing: The ongoing stage after adoption, where the taxonomy is owned, maintained and changed under agreed rules.
- check / script: A rule that an automated script can verify mechanically, such as unique labels, no orphan terms, or every term defined.
- check / judgement: A rule that needs a person to assess it qualitatively, such as whether a definition is clear or a label is natural.
- check / owner decision: A rule that is settled only when the taxonomy's named owner explicitly decides or signs off, rather than by a test or by review.
