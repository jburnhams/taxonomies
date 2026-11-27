# Prompts taxonomy, stage 3 (control area): samples

**In one line**: 104 sections about the control area, drawn by a seeded rule from 35 files
of `jburnhams/prompts` and split into build (30), bare-facet test (10), round-1 test (30)
and held (34).

**In plain words**: stage 3 sorts only the mechanisms that decide whether an action may
happen and what stops, redirects or restarts a run (stage 1's `control` area). An item
is still one section: its heading, the first lines under it, and the file. Some sections
turn out to be about another area; raters say so, and those are left out of the stage-3
scores.

## How the items were drawn

Taken from `jburnhams/prompts` at commit `e7d4fb2` (2026-11-26) by
[`sample3.py`](./sample3.py), which reuses stage 2's population rule and filters
([`../stage-2/sample2.py`](../stage-2/sample2.py), method v1.1 M2 and M7) with a new seed
(20261128), file list and heading words.

- **Population**: every kept section of the eight control docs
  (`agent-permissions-approval.md`, `agent-risk-assessment.md`, `agent-run-recovery.md`,
  `agent-run-steering.md`, `agent-design/risk.md`, `agent-design/keel/authority.md`,
  `agent-design/keel/endings.md`, `agent-design/keel/rules.md`), plus every kept section
  elsewhere (analysis docs and per-source READMEs) whose **heading** names a control
  mechanism (approval, permission, sandbox, risk, guard, monitor, steer, nudge, recover,
  retry, stopped or stopping, blocking or blocked, trust, policy, allow, deny, escalate, interrupt, abort, confirm,
  loop detection, budget, limit, ending, completion gate, authority, safety, destructive,
  prompt injection, yolo, auto mode, plan mode; the list is `HEAD_KW` in the script).
  61 of the 104 items come from the control docs.
- **Heading words narrowed by hand** before the draw: "block", "loop" and "stop" alone
  matched too many sections about other things (code blocks, the agent loop), so the
  list uses "blocking", "blocked", "blocker", "stopped", "stopping" and "loop detection".
- **Split**: the seeded draw orders the population, then takes 30 build items (`k01`-`k30`),
  10 bare-test items (`kt01`-`kt10`), 30 round-1 items (`kr01`-`kr30`) and the rest held
  (`kh01`-`kh34`) for later rounds. Fewer build and bare items than stage 2 (40 and 12)
  so that a held set is left; the population is smaller.

All items are in [`items.csv`](./items.csv) (`id,item,gist,from`); the round-1 items are
also in [`rounds/round-1/items.csv`](./rounds/round-1/items.csv).
