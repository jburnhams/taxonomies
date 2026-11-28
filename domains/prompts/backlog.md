# Prompts taxonomy: term backlog

**In one line**: concepts that a settled term opens but no stage has defined yet, so each
stage starts from a list instead of from memory (method v1.1 M8, proposed as J33).

**In plain words**: defining one word shows you the words next to it. "Approval" brings
up who approves, what an allow list is, and what happens when the answer is no. Those
go here, with the term that opened them and how often the repo uses them, until a stage
takes them. A stage takes the rows for its area at its start and adds the rows it opened
at its end.

Warrant counts are over the control docs ("ctl", the eight in
[`stage-3/samples.md`](./stage-3/samples.md)) and over every analysis doc and per-source
README ("all"), at prompts `e7d4fb2`, from [`stage-3/harvest.md`](./stage-3/harvest.md)
unless marked. **Taken** names the stage and the entry; **open** rows wait for a stage.

## Taken by stage 3 (control)

| Concept | Opened by | Warrant | Taken as |
|---|---|---|---|
| raising a risk tier or a case to more scrutiny | `handoff` (alias "escalation" was a homonym) | escalat- 36 ctl / 182 all | `escalation` (new) |
| a level that sets how much scrutiny a change or action gets | `control` scope ("risk levels") | tier 102 / 678 | `risk-tier` (new) |
| the reason a tier was set (path, size, authority, ...) | `risk-tier` | driver 28 / 59 | `risk-driver` (new) |
| a list of commands or paths that are allowed or refused without asking | `approval` scope ("allow lists") | allowlist or allow list 6 / 147 | `allow-list` (new) |
| what a run may do on its own: the permissions it carries | `sub-agent`, `permission-mode` | authority 26 / 196 | `authority` (new) |
| a monitor that holds an action until it says yes | `verification` near miss ("blocking monitor") | blocking 16 / 136; guardian 54 / 182; monitor 26 / 95 | `blocking-monitor` (new) |
| a limit on tokens, turns, money or time for one run | `failure` alias "limit" | budget 12 / 464 | `run-budget` (new) |
| spotting that a run repeats itself | `steer` scope ("loop warnings") | stuck 2 / 22; loop detect- 1 / 12 | `loop-detection` (new) |
| running a step or a tool call again after it failed | `failure` | retr(y\|ies) 40 / 460 | `retry` (new) |
| a framework running a step again on its own, which a tool must survive | `retry` | replay 14 / 132; idempot- 2 / 79 | `replay` (new) |
| carrying on a stopped run from its saved state | `failure` | resume- 26 / 366 | `resume` (new) |
| a run waiting, not ended, until something resolves | `ending` | suspend- 3 / 132 | `suspension` (new) |
| a check that refuses to end a run until its work passes | `self-verification` scope | completion gate 1 / 43 | `completion-gate` (new) |
| text in a tool result or file that tries to take over the agent | `tool-result` | prompt injection 7 / 41 | `prompt-injection` (new) |
| refusing to load project content from a workspace not marked as trusted | `context-file` | trust 18 / 324 | `trust-gate` (new) |
| the harness channel for adding text to a turn | `steer` (aliases covered notices that are not steers) | system-reminder 17 / 51; reminder 35 / 128 | `system-reminder` (new, split from `steer`) |

## Open

| Concept | Opened by | Warrant | Expected stage |
|---|---|---|---|
| fork: a copy of a run or session that goes on separately | `session` (stage 1) | fork ⚠ not counted | coordination |
| artifact: a file or page a run produces for a person | `output` area (stage 1) | artifact ⚠ not counted | output |
| three postures on a context file's authority (supreme, advisory, data) | `framing` (stage 2), `kr17` here | ⚠ one doc | context, revisit (could be finer `framing` values) |
| a reviewer's verdict on a PR (approve, request changes) | `approval` near miss, `code-review` | ⚠ not counted | verification |
| blast radius: how much a change or action can affect | `risk-driver` | blast radius 10 / 23 | verification or a later control pass |
| proof: evidence that a change works in real use, apart from tests | `kr09` | ⚠ not counted | verification |
| deny list, as its own entry rather than an alias of `allow-list` | `allow-list` | deny list or denylist 5 / 14 | control retest, if raters split it |
| confirmation policy: a document listing which actions need a person | `permission-mode` alias "approval policy" | confirmation polic- 1 / 9 | control retest |
| swarm: a set of agents working on one task at once, results combined | [#23](https://github.com/jburnhams/taxonomies/issues/23), from `coordination` | swarm 39 all at prompts `16aef6a`; 77 in `agent-swarms.md` + proposals at `1a3c84b` | coordination |
| topology: who talks to whom and who combines (independent, centralized, hierarchical, decentralized, board) | [#24](https://github.com/jburnhams/taxonomies/issues/24), from `orchestrator` | topolog- 13 all; 10 swarms | coordination (maybe a facet) |
| fan-out: starting several sub-agents at once and joining their results | [#25](https://github.com/jburnhams/taxonomies/issues/25), from `sub-agent` | fan out or fan-out 130 all; fan-in 4 | coordination |
| join: the end of a fan-out, with its deadline and rule for a missing part | `fan-out` (#25) | ⚠ not counted; proposal 3 in `proposals-swarms-2026-11.md` | coordination |
| board: a shared append-only record agents post to instead of messaging | [#26](https://github.com/jburnhams/taxonomies/issues/26), from `scratchpad`, `memory` near misses | message board 3 all; board 40 swarms | coordination |
| vote: choosing the answer most independent agents give | [#27](https://github.com/jburnhams/taxonomies/issues/27), from `self-verification` | vote or voting 18 all; ensemble 25; best-of-N 9 | coordination or verification |
| debate: agents reading each other's answers and revising over rounds | [#28](https://github.com/jburnhams/taxonomies/issues/28), from `vote` | debate 2 all; 18 swarms | coordination or verification |
| one agent passing control to another inside a run (OpenAI, LangGraph, MS "handoff") | [#29](https://github.com/jburnhams/taxonomies/issues/29) (`clarify` on `handoff`) | handoff or transfer_to 18 swarms | intake first (R4), else coordination |
