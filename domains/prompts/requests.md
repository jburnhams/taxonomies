# Prompts taxonomy: requests

**In one line**: every request for a term, a clarification or a change that reached this
domain, with its outcome, so the asker can look the answer up.

**In plain words**: agents and people ask for a term, a clarification or a change by
filing a `term-request` issue in this repo ([form](https://github.com/jburnhams/taxonomies/issues/new?template=term-request.yml)).
`python3 tools/term.py intake --write` copies new issues in as `open` (ID `issue-<number>`);
whoever answers sets **Outcome** (`use`, `alias`, `candidate`, `clarified`, `changed`,
`backlog` or `declined`, with the term ID) and **Answered** (date, by), logs any operation
in [`changelog.md`](./changelog.md), comments the outcome on the issue with a link to the
PR and closes it. A `backlog` record gains **Taken** (date, term ID) when a stage defines
its term, and that stage comments the term on the issue. Rules:
[`design/growth.md`](../../design/growth.md). `term.py lookup` and `changes` show these
answers back to the asker. Nothing here is deleted.

## Requests

### handoff (`issue-29`)

- **Ask**: clarify
- **Term**: handoff
- **Concept**: OpenAI's Agents SDK (`transfer_to_<agent>` tools), LangGraph swarm (`active_agent`) and Microsoft Agent Framework's Handoff pattern use "handoff" for one agent passing control of the conversation to another agent inside the same run, which then answers in its place. The glossary's `handoff` is a run passing its work to a person or another run instead of finishing, and its near miss excludes a sub-agent report. Which does the in-run transfer fall under: `handoff` (widen the scope to "another agent"), a new term, or neither? The repo needs to say it in agent-swarms.md §4b and agent-subagent-architectures.md §7.
- **Looked at**: `lookup prompts "handoff"`: `handoff` (run to person or run), `escalation` (one decision up), `sub-agent` (reports back, the spawner carries on). None covers control moving between peer agents while the run goes on.
- **Example**: https://github.com/jburnhams/prompts/blob/1a3c84b/agent-swarms.md (§4b)
- **Warrant**: "handoff/transfer_to" 18 in agent-swarms.md and its proposals in this sense; agent-subagent-architectures.md §7 uses it the same way for Microsoft Agent Framework's Handoff pattern.
- **Asked**: jburnhams/prompts agent swarms deep dive, 2026-11-28, branch claude/project-thread-7iimfg
- **From**: [#29](https://github.com/jburnhams/taxonomies/issues/29)
- **Outcome**: clarified, `handoff`. The in-run transfer is a handoff: the definition now reads "a run or an agent passes its work to a person, another run or another agent instead of finishing it, and does not get it back", and the scope names the OpenAI, LangGraph and Microsoft cases. A sub-agent's report stays the near miss (the spawner gets the work back). Every earlier use still fits, so not breaking (R4); named in the PR for Jonathan's veto (R5).
- **Answered**: 2026-11-28, Claude (by-hand intake in the Taxonomies project, asked by Jonathan)

### debate (`issue-28`)

- **Ask**: new
- **Concept**: A debate is a happening in which several agents answer the same task, read each other's answers and revise their own over rounds before the answers are combined.
- **Looked at**: `lookup prompts "debate"`: no term. Near `vote` (requested separately: no agent reads another's answer) and `code-review` (one agent judges another's work product, with no rounds). Proposal 7 in the deep dive rules it out as a quality method, so the repo needs the word to say what is ruled out.
- **Example**: https://github.com/jburnhams/prompts/blob/1a3c84b/agent-swarms.md (§7)
- **Warrant**: "debate" 2 in the repo's docs at 16aef6a; 18 in agent-swarms.md and its proposals; the field's own word (multi-agent debate, Du et al. and the 2026 papers 2606.29270, 2609.35875).
- **Asked**: jburnhams/prompts agent swarms deep dive, 2026-11-28, branch claude/project-thread-7iimfg
- **From**: [#28](https://github.com/jburnhams/taxonomies/issues/28)
- **Outcome**: backlog (R3). The coordination area has no stage yet, so this is an open row in [`backlog.md`](./backlog.md) that the coordination stage starts from. Keep writing "debate" meanwhile (a usable word, growth loop step 2); `term.py changes prompts` will show the term when the stage defines it.
- **Answered**: 2026-11-28, Claude (by-hand intake in the Taxonomies project, asked by Jonathan)

### vote (`issue-27`)

- **Ask**: new
- **Concept**: A vote is a way of combining several independent answers to the same task by choosing the one most of them give, with no agent judging the evidence.
- **Looked at**: `lookup prompts "voting ensemble"`: no term. `self-verification` is one agent checking its own work; `second-model` decides about an action, not among answers; `eval` grades after the run. The field's words are self-consistency, majority voting, sampling-and-voting, best-of-N (best-of-N picks by a scorer, so it may be a near miss rather than an alias). Every 2026 debate paper read compares against it at matched budget.
- **Example**: https://github.com/jburnhams/prompts/blob/1a3c84b/agent-swarms.md (§7)
- **Warrant**: "vote/voting/majority vote" 18 in the repo's docs at 16aef6a; "ensemble" 25; "best-of-N" 9; 23 in agent-swarms.md and its proposals.
- **Asked**: jburnhams/prompts agent swarms deep dive, 2026-11-28, branch claude/project-thread-7iimfg
- **From**: [#27](https://github.com/jburnhams/taxonomies/issues/27)
- **Outcome**: backlog (R3). The coordination area has no stage yet, so this is an open row in [`backlog.md`](./backlog.md) that the coordination stage starts from. Keep writing "vote" meanwhile (a usable word, growth loop step 2); `term.py changes prompts` will show the term when the stage defines it.
- **Answered**: 2026-11-28, Claude (by-hand intake in the Taxonomies project, asked by Jonathan)

### board (`issue-26`)

- **Ask**: new
- **Concept**: A board is a shared append-only record that the agents of one run or swarm read and post to instead of messaging each other, so no agent routes and all coordination is observable.
- **Looked at**: `lookup prompts "blackboard shared state"`: no term. `memory` keeps information across runs, a board lives inside one; `scratchpad` (stage 2) is one agent's own working notes; `transcript` records one run for later, it is not read by peers during the run. Sources call it a blackboard (Salemi et al. 2510.01285), bulletin board (ArcticSwarm), message board (Codex, Antigravity), context board (Agensh).
- **Example**: https://github.com/jburnhams/prompts/blob/1a3c84b/agent-swarms.md (§4c)
- **Warrant**: "message board" 3 and "board" in this sense in agent-subagent-architectures.md §7b at 16aef6a; 40 in agent-swarms.md and its proposals; four independent systems in 2026 (Codex, ArcticSwarm, Antigravity, Agensh).
- **Asked**: jburnhams/prompts agent swarms deep dive, 2026-11-28, branch claude/project-thread-7iimfg
- **From**: [#26](https://github.com/jburnhams/taxonomies/issues/26)
- **Outcome**: backlog (R3). The coordination area has no stage yet, so this is an open row in [`backlog.md`](./backlog.md) that the coordination stage starts from. Keep writing "board" meanwhile (a usable word, growth loop step 2); `term.py changes prompts` will show the term when the stage defines it.
- **Answered**: 2026-11-28, Claude (by-hand intake in the Taxonomies project, asked by Jonathan)

### fan-out (`issue-25`)

- **Ask**: new
- **Concept**: A fan-out is a happening in which an agent or harness starts several sub-agents at once on parts or copies of a task and waits to combine their results (the join).
- **Looked at**: `lookup prompts "fan-out"`: no term. `sub-agent` is one member; `orchestrator` is the role that may do it; `pipeline` explicitly has no parallel branches in Keel. The repo uses fan-out as its own concept with reasons (review.md §6a: context coverage, role specialisation, sampling variance; agent-swarms.md adds alternative attempts) and needs a word for the join that ends it.
- **Example**: https://github.com/jburnhams/prompts/blob/16aef6a/agent-design/review.md (§6a "What the fan-out is actually buying")
- **Warrant**: "fan-out" / "fan out" 130 in the repo's docs at 16aef6a; "fan-in" 4.
- **Asked**: jburnhams/prompts agent swarms deep dive, 2026-11-28, branch claude/project-thread-7iimfg
- **From**: [#25](https://github.com/jburnhams/taxonomies/issues/25)
- **Outcome**: backlog (R3). The coordination area has no stage yet, so this is an open row in [`backlog.md`](./backlog.md) that the coordination stage starts from. Keep writing "fan-out" meanwhile (a usable word, growth loop step 2); `term.py changes prompts` will show the term when the stage defines it.
- **Answered**: 2026-11-28, Claude (by-hand intake in the Taxonomies project, asked by Jonathan)

### topology (`issue-24`)

- **Ask**: new
- **Concept**: A topology is the shape of a swarm or multi-agent run that says which agents talk to which and who combines results: independent, centralized, hierarchical, decentralized, or through a shared board. It could be a facet of the coordination area rather than a term.
- **Looked at**: `lookup prompts "topology"`: no term. `orchestrator` and `sub-agent` name roles inside one topology (centralized); `pipeline` is one fixed shape across runs; `coordination` is the area. The scaling study (arXiv 2512.08296) and the orchestration-trace survey (2605.02801) both sort systems by this axis.
- **Example**: https://github.com/jburnhams/prompts/blob/1a3c84b/agent-swarms.md (§1, the topology table)
- **Warrant**: "topolog-" 13 in the repo's docs at 16aef6a (agent-subagent-architectures.md §7 calls Microsoft Agent Framework's five patterns topologies), 10 more in agent-swarms.md and its proposals.
- **Asked**: jburnhams/prompts agent swarms deep dive, 2026-11-28, branch claude/project-thread-7iimfg
- **From**: [#24](https://github.com/jburnhams/taxonomies/issues/24)
- **Outcome**: backlog (R3). The coordination area has no stage yet, so this is an open row in [`backlog.md`](./backlog.md) that the coordination stage starts from. Keep writing "topology" meanwhile (a usable word, growth loop step 2); `term.py changes prompts` will show the term when the stage defines it.
- **Answered**: 2026-11-28, Claude (by-hand intake in the Taxonomies project, asked by Jonathan)

### swarm (`issue-23`)

- **Ask**: new
- **Concept**: A swarm is a set of agents (broader: `agent`, area `coordination`) working on one task at the same time, whose results are combined into one outcome.
- **Looked at**: `lookup prompts "swarm"`: no term. `sub-agent` (one agent started by another to do part of its task and report back) names a member, not the set; `orchestrator` names one role in some swarms, and several swarms read have none (Anthropic's C compiler, Agensh); `pipeline` is runs in sequence joined by edges, not agents at the same time; `coordination` is the whole area. "Multi-agent" is an alias of `coordination`, so the set itself has no word.
- **Example**: https://github.com/jburnhams/prompts/blob/1a3c84b/agent-swarms.md (§1)
- **Warrant**: "swarm" 39 in the repo's own docs (excluding leaked/ and skills/) at prompts 16aef6a, 77 in agent-swarms.md and its proposals at 1a3c84b; used as a product name by OpenAI Swarm, Kimi Agent Swarm, Antigravity /swarm, LangGraph swarm.
- **Asked**: jburnhams/prompts agent swarms deep dive, 2026-11-28, branch claude/project-thread-7iimfg
- **From**: [#23](https://github.com/jburnhams/taxonomies/issues/23)
- **Outcome**: backlog (R3). The coordination area has no stage yet, so this is an open row in [`backlog.md`](./backlog.md) that the coordination stage starts from. Keep writing "swarm" meanwhile (a usable word, growth loop step 2); `term.py changes prompts` will show the term when the stage defines it.
- **Answered**: 2026-11-28, Claude (by-hand intake in the Taxonomies project, asked by Jonathan)

### retrieval (`issue-21`)

- **Ask**: new
- **Concept**: Retrieval is a step that chooses items from a store by a search and puts them in the model's context (RAG, memory recall, code search results added to the prompt).
- **Looked at**: `term.py lookup prompts "retrieval"` finds no term. `memory` covers what is kept, not the search that brings it back. The stage-2 operation value `supply` is broader: it covers any content put in front of the model. The voice domain has `retrieval` as a stage-1 candidate and would map to it (`domains/voice/map.md`, PR #19).
- **Example**: https://github.com/jburnhams/prompts (repo-wide use, e.g. memory recall and RAG sections)
- **Warrant**: prompts: "retriev-" about 409 matching lines repo-wide, RAG 52 (grep, 2026-11-27); voice-research: retriev-/RAG 160 in 25 files.
- **Asked**: Voice taxonomy stage 1, `domains/voice/` on branch `claude/project-thread-h8atpn` (PR #19), aligning voice with prompts.
- **From**: [#21](https://github.com/jburnhams/taxonomies/issues/21)
- **Outcome**: candidate, `retrieval` (context area, a kind of `supply`). Defined from the prompts repo's own use, which is wider than the request: [agent-memory-learning.md §5](https://github.com/jburnhams/prompts/blob/4c30cd1/agent-memory-learning.md) counts pasting in, index reads, search and trigger matching as retrieval modes. Voice's search-only `retrieval` maps to it as broadMatch (`domains/voice/map.md`).
- **Answered**: 2026-11-28, Claude (by-hand intake in the Taxonomies project, asked by Jonathan)

### model prompt (`issue-20`)

- **Ask**: clarify
- **Term**: context-window
- **Concept**: A model prompt is a body of text that is sent to a language model on one request: the system prompt, examples, retrieved items and the request itself. `term.py lookup prompts "prompt"` gives `context-window`, but that entry is defined as a limit ("a limit on how many tokens a model accepts on one request"). Is "the prompt" meant as `context-window`, or should `prompts` have its own entry for the text that fills it?
- **Looked at**: `context-window` (candidate): "prompt" is an alias, but the definition is a limit, not the text. `system-prompt` is only one part of it. No other entry fits.
- **Example**: voice-research `written-methods.md` §1 (examples, a style profile and past failures go "in the prompt"); the voice domain's `domains/voice/map.md` in PR #19.
- **Warrant**: voice-research: "prompt" 426 uses in 96 files, about a quarter in this sense (2026-11-27).
- **Asked**: Voice taxonomy stage 1, `domains/voice/` on branch `claude/project-thread-h8atpn` (PR #19), aligning voice with prompts.
- **From**: [#20](https://github.com/jburnhams/taxonomies/issues/20)
- **Outcome**: changed, new candidate `model-prompt` (labelled "prompt") split from `context-window`. `context-window` keeps the limit; the text sent on one request is the prompt, and the alias "prompt" moved with it. Breaking (corrected 2026-11-28; first logged as not breaking): write "prompt" for the text sent on one request and "context window" only for its limit; uses such as "loaded into the context window" still read right. Voice-research keeps writing "model prompt" (an alias here), since "prompt" alone is ambiguous there; mapped in `domains/voice/map.md`. Split named in the PR for Jonathan's veto (R5).
- **Answered**: 2026-11-28, Claude (by-hand intake in the Taxonomies project, asked by Jonathan)
