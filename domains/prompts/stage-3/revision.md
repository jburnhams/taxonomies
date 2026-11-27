# Prompts taxonomy, stage 3: revision pass

**In one line**: seven earlier entries that the control harvest showed were unclear or
wrong, each fixed by one named operation, and all seven back to `candidate` until the
stage-3 name test retests them (method v1.1 M8, proposed as J33).

**In plain words**: defining the control words showed that some words already agreed in
stages 1 and 2 overlap the new ones or mean two things. Small fixes add a near miss or
tighten a scope. Breaking fixes move an alias to a new entry; the old ID and label stay
where they were, so nothing that links to them breaks (spec G5).

Read 2026-11-27 against prompts `e7d4fb2`. Each row is one G4 operation
([`design/spec.md` §9](../../../design/spec.md)); the full text is in each entry's
**History** in [`../glossary.md`](../glossary.md).

| # | Entry | Operation | Breaking? | What was wrong | What changed |
|---|---|---|---|---|---|
| R1 | `compaction` | redefine | no | Its scope still said "truncation of old tool results" after stage 2 made `truncation` its own entry, so a tool result cut on arrival could be filed under either. | Scope says clearing or cutting old results to fit the window is part of a compaction, and cutting a result as it arrives is a `truncation`; near miss added. |
| R2 | `steer` | split | yes | Its aliases "system reminder", "reminder" and "system-reminder" named a channel that also carries notices that redirect nothing (lost tool calls, a session moved to a new runner: `agent-run-recovery.md` §1). | New `system-reminder` (the channel) takes those three aliases; `steer` keeps its ID, label and "nudge", and gets a near miss. |
| R3 | `handoff` | redefine | yes | Alias "escalation" is a homonym: the control docs use it for passing a decision up (a command sent to the user for approval, a tier raised after validation: `agent-permissions-approval.md` §5, `agent-design/risk.md` §3c), not for passing the work. | Alias removed and scope narrowed to giving a task to a person to finish; new `escalation` term; near misses both ways. |
| R4 | `approval` | redefine | no | Definition said "a person or a rule" while its scope included an auto-mode classifier, which is a `second-model`. | Definition says "a person, a rule or a second model"; near miss for a reviewer approving a pull request. |
| R5 | `permission-mode` | redefine | no | Alias "approval policy" also names review-policy files such as Cursor's `APPROVAL_POLICY.md` (`agent-design/risk.md` §12g), which say which pull requests need a person. | Alias kept (Codex's `approval_policy` setting is this sense); near miss added for the file. |
| R6 | `sandbox` | redefine | no | Alias "isolation" is also used for one git worktree per sub-agent, which keeps changes apart but limits nothing. | Near miss added. |
| R7 | `precedence` | redefine | yes | Alias "authority" (stage 2, from a context file's "authority" over the model) clashes with authority as what a run may do, the commoner sense in the control docs (authority 26, `agent-design/keel/authority.md`). T2 caught it when the new term was drafted. | Alias removed; the new `authority` takes the label; near miss added; the three authority postures stay in the backlog for the context area. |

Also checked and left alone: `failure` (aliases "error, recovery, limit" are loose but
name the moment, and the new `recover`, `retry` and `run-budget` are narrower terms with
their own labels); `control` (its scope already lists every new term's topic);
`verification` (keeps completion gates in its scope; the new `completion-gate` term is
used from either area); `second-model` (its alias "monitor" stays; the new
`blocking-monitor` is a role of it with its own label).

## Rename list (G6)

No ID or heading word changed, so no prompts doc needs renaming. Three uses change
which entry they point to:

- "system reminder" / "reminder" in `agent-run-steering.md` and `agent-run-recovery.md`
  now finds `system-reminder`; where those docs mean redirecting text, the heading word
  is still `steer`.
- "escalate" / "escalation" in `agent-permissions-approval.md` §5 and
  `agent-design/risk.md` §3 now finds `escalation`. Grep for "escalat" beside "human",
  "person" or "user" in the analysis docs found every use in the decision sense
  (asking a person to approve), none in the sense of handing over the work.
  `agent-design/medium.md` "Escalation triggers" is a third sense (upgrading a
  mechanism) and is a near miss on `escalation`; it keeps its wording.
- "authority" in `agent-context-file-loading.md` §"Three postures on authority" is the
  context sense; it keeps its wording and is listed in the backlog.

Stored prompts (`leaked/`, `skills/`, `codex/*.md` prompt copies) keep their authors'
wording.

## Retest

All seven entries are `candidate`. They go into the stage-3 name test
([`rounds/round-1/name-test/`](./rounds/round-1/name-test/)) with the new control terms,
and the stage is not adopted until they pass or are fixed again (M8 step 3).
