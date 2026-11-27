# Prompts taxonomy, stage 3 (control area): term harvest

**In one line**: the words the prompts repo uses for the control area, counted at
`e7d4fb2`, with six groups of synonyms, six words that mean two or three things, the
repo's own classifications that became facets, and the terms stage 3 defines.

**In plain words**: before naming anything we count which words the repo already uses
and where it uses several words for one idea, or one word for several. This stage also
starts from the [term backlog](../backlog.md) and checks every earlier entry the counts
touch ([`revision.md`](./revision.md)).

Counted by [`count3.py`](./count3.py) over the eight control docs ("ctl", listed in
[`samples.md`](./samples.md)) and over every `.md` file outside `leaked/` and `skills/`
("all"), case-insensitive, word stems as shown. "all" here also counts design docs and
the changelog, so it is a little wider than stage 2's "all". Process step 3
([`design/process.md`](../../../design/process.md)).

## Counts

| Term (stem) | ctl | all | files |
|---|---|---|---|
| approv- | 189 | 1,313 | 146 |
| risk | 129 | 593 | 88 |
| tier | 102 | 678 | 83 |
| policy | 70 | 672 | 119 |
| gate | 65 | 1,046 | 141 |
| permission | 64 | 500 | 112 |
| confirm- | 58 | 655 | 124 |
| guardian | 54 | 182 | 23 |
| deny | 49 | 181 | 47 |
| sandbox | 48 | 626 | 114 |
| retr(y|ies) | 40 | 460 | 95 |
| escalat- | 36 | 182 | 59 |
| classifier | 36 | 143 | 41 |
| reminder | 35 | 128 | 34 |
| driver | 28 | 59 | 23 |
| resume | 26 | 366 | 89 |
| authority | 26 | 196 | 55 |
| monitor | 26 | 95 | 34 |
| refus- | 21 | 344 | 89 |
| auto mode | 20 | 54 | 14 |
| trust | 18 | 324 | 86 |
| handoff | 18 | 287 | 57 |
| system-reminder | 17 | 51 | 19 |
| blocking | 16 | 136 | 59 |
| interrupt | 15 | 119 | 40 |
| replay | 14 | 132 | 61 |
| plan mode | 14 | 80 | 25 |
| verdict | 13 | 151 | 50 |
| steer | 13 | 103 | 38 |
| budget | 12 | 464 | 98 |
| nudge | 12 | 109 | 39 |
| guard | 10 | 190 | 70 |
| blast radius | 10 | 23 | 13 |
| destructive | 9 | 116 | 52 |
| prompt injection | 7 | 41 | 25 |
| allowlist / allow list | 6 | 147 | 58 |
| yolo | 6 | 19 | 5 |
| deny list / denylist | 5 | 14 | 11 |
| irreversible | 4 | 25 | 15 |
| suspend- | 3 | 132 | 32 |
| checkpoint | 3 | 126 | 41 |
| idempot- | 2 | 79 | 43 |
| rollback / undo | 2 | 64 | 29 |
| stuck | 2 | 22 | 13 |
| abort | 1 | 55 | 35 |
| completion gate | 1 | 43 | 20 |
| loop detect- | 1 | 12 | 10 |
| confirmation polic- | 1 | 9 | 6 |

## Synonym sets

1. **Letting an action run**: approval 189, confirm- 58, permission 64, consent. Stage 1
   chose `approval` for the happening; `permission-mode` for the setting. Facet value
   `ask-person` and `gate` split who settles it.
2. **A second model that can stop an action**: guardian 54 (Codex's name), classifier 36
   (Claude Code's auto mode), monitor 26, security monitor. Stage 1's `second-model`
   covers every role; the role that holds an action is the new `blocking-monitor`.
3. **How much scrutiny**: risk tier, risk level, tier 102, attention level, score. "Tier"
   alone also names memory tiers and model sizes (stage 2 homonym 3), so the label is
   `risk-tier`; its reasons are `risk-driver` (driver 28).
4. **Running again**: retry 40, replay 14, resume 26, requeue, re-run. Three ideas: the
   harness or agent tries a failed step again (`retry`), a framework re-executes a step
   to rebuild state (`replay`, with idempotency 79 in all), a stopped run carries on from
   saved state (`resume`). Facet value `recover` covers all three.
5. **Mid-run text that changes course**: steer 13, nudge 12, reminder 35,
   system-reminder 17. Stage 1 put the channel and the purpose in one entry; the
   revision pass splits them (R2: `steer`, `system-reminder`).
6. **Stopping**: halt, stop, interrupt 15, abort 1, suspend 3, end. Suspension (waits to
   be woken) and an ending (over) are different; `suspension` gets an entry, stopping in
   general is facet value `halt`.

## Homonyms

1. **escalation**: passing a decision to a stricter check (approval §5, re-asking after a
   repeated call; risk §3c, raising a tier), handing work to a person (stage 1 alias of
   `handoff`, removed in R3), and upgrading a mechanism ("Escalation triggers" in
   `agent-design/medium.md`). The first is the new `escalation`.
2. **authority**: what a run may do (Keel authority, "delegation never widens
   authority") and how much a context file's text directs the model (the three postures,
   stage 2's alias on `precedence`, removed in R7).
3. **approval policy**: Codex's `approval_policy` setting (a `permission-mode`) and
   Cursor's `APPROVAL_POLICY.md` review-policy file (which pull requests need a person).
   R5 keeps the alias and adds a near miss.
4. **blocking**: a monitor that holds an action until it answers (control), and the
   everyday "blocking" of one task by another, or of a call by I/O. 136 uses in all;
   only the first is a term (`blocking-monitor`).
5. **gate**: 1,046 uses in all, in many kinds: completion gate, merge gate, write gate,
   trust gate. Each kind has its own entry; the bare word is facet value `gate`, the
   response all of them share (let through or refuse).
6. **isolation**: a sandbox that limits what can be reached, and a worktree per sub-agent
   that only keeps changes apart. R6 adds a near miss on `sandbox`.

## The repo's own classifications

- **Two granularities** (`agent-risk-assessment.md` §1: action-level and change-level
  risk): became facet `target` (`tool-action`, `work-product`), with `run-course` and
  `incoming-text` for the steering, recovery and trust items.
- **Who sets the level** (`agent-risk-assessment.md` §3, five patterns from model self-report to harness
  rules) and **static rules vs. LLM judgment** (approval §2): stage 1's `decider`.
- **Steering's decisions** (`agent-run-steering.md` §2: channel, forgery, how long,
  cache position, whether it blocks, who pays, what the grader may conclude): "how long"
  is stage 2's `reach`; "whether it blocks" separates `gate` from `redirect` in facet
  `response`.
- **Recovery's four positions** (`agent-run-recovery.md` §1): the terms `retry`,
  `resume`, `replay`.
- **Enforcement: harness vs. prompt** (approval §7): Set C's `enforcement`, not in Set A
  because nearly every item is harness-enforced (bare test).
- **Approval mode taxonomies** (approval §1) and the **four-tier confirmation taxonomy**
  (`codex/README.md`): values of `permission-mode` per product, not a facet.

## Terms for the stage-3 glossary

Drafted as `candidate` from the backlog rows this stage took
([`../backlog.md`](../backlog.md), "Taken by stage 3"): `escalation`, `risk-tier`,
`risk-driver`, `allow-list`, `authority`, `blocking-monitor`, `run-budget`,
`loop-detection`, `retry`, `replay`, `resume`, `suspension`, `completion-gate`,
`prompt-injection`, `trust-gate`, `system-reminder`. Rows opened and not taken are in the
backlog's "Open" table.
