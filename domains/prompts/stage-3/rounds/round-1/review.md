# Stage 3, round 1: competency questions (T10) and heuristic review (T11)

**In one line**: round 1 passed J23 on both facets, the name test passed, all seven
stage-3 competency questions can be answered from `facets.md` and `glossary.md`, and the
review found no unmarked synonym and no missing facet. Jonathan chose set A on 2026-11-27
and stage 3 was adopted.

Checked by Claude, 2026-11-27, against the files as changed after the name test.

## T10: competency questions

| # | Question | Answered by |
|---|---|---|
| 21 | Which controls govern one action, the run, incoming text, a finished change? | facet `target`: four values, with the rule for limits set once on a run's tools |
| 22 | Which settle a case themselves, which put it to a person? | `response` = `gate` against `ask-person`; terms `approval`, `escalation`, `blocking-monitor` |
| 23 | Which change course without stopping, which stop or suspend? | `response` = `redirect` against `halt`; terms `steer`, `loop-detection`, `suspension`, `run-budget` |
| 24 | Which run something again; retry, replay, resume? | `response` = `recover`; `retry` (failed, try again), `replay` (framework re-runs to rebuild state), `resume` (carry on from saved state), with near misses between them |
| 25 | Approval, escalation, handoff? | `approval` (an action allowed before it runs), `escalation` (a decision passed to a stricter check), `handoff` (the work passed on), near misses both ways since R3 |
| 26 | Steer or system reminder? | `steer` (the purpose: redirect) against `system-reminder` (the channel, which also carries plain notices), since R2 |
| 27 | What sets a change's risk tier, and what records why? | `risk-tier` and `risk-driver`; `response` = `grade` (label "set a level"); stage 1's `decider` for who sets it |

All seven are answered.

## T11: Z39.19 §11.2.2 review

- **Unmarked synonyms**: none. Every word in the stage-3 harvest's six synonym sets is a
  preferred label or an alias of one entry, which T2 confirms. T2 also caught the one
  clash the harvest missed (`precedence`'s alias "authority", R7).
- **Missing facets**: none. Round 1 had no three-way split. The `unsure` notes (9, 8 and
  5) choose between existing values. The disagreements fall in two patterns: a control
  whose whole allow/ask/refuse choice is the topic (`kr13`, `kr29`: `gate` or
  `ask-person`, settled by the stated rule), and recovery items that also refuse or
  steer (`kr12`, `kr21`). No rater asked for Set C's `enforcement`.
- **Facet changes**: none in round 1. Value `grade` relabelled "set a level" after the
  name test (ID kept), which is not a facet change.
- **Out-of-date terms**: none. Harvested at prompts `e7d4fb2` (2026-11-26).
- **Term form**: T3 flags only `operations` (stage 1, kept).
- **Area boundary**: six of 30 items were put outside `control` by most raters: tool
  (`kr04`, redundant parameters), context (`kr06` budgets and truncation, `kr11`
  compaction, `kr27` cache position), verification (`kr05` an authority-chain security
  review, `kr10` what a grader may conclude). Each agrees with stage 1's area
  definitions, so stage 1 needs no change.
- **Revision pass**: the seven changed entries passed the name test (M8 step 3).
- **For a later stage**: the backlog's eight open rows ([`../../../backlog.md`](../../../backlog.md)).

## Ending conditions (scope.md, each stage)

| Condition | Stage 3 |
|---|---|
| T1-T6 clean | yes (only the kept `operations` flag) |
| T7: every item sorted, Unsorted ≤ 7% | yes: 24 in-area items, no three-way split. The sample is 30, by method v1.1 M3 (5 × 6 values) |
| T8: J23 on every facet | yes: Fleiss 0.83 / 0.80, pair 0.75 / 0.70 ([results](./results.md)) |
| T9: ≥ 80% of labels guessed, revised entries included | yes: 94% and 97%, all seven revised entries right ([name test](./name-test/results.md)) |
| T10 | yes, all seven |
| T11 | yes |
| No facet change in the last round | yes |
| Facet set chosen by Jonathan (process step 4) | yes: set A, 2026-11-27 |
