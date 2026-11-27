# Stage-3 name test (T9): results

**In one line**: both fresh readers are well above the 80% target (openai 31 of 33, 94%;
gemini 32 of 33, 97%), and all seven entries changed by the revision pass were guessed
right by both. The misses were "grade" (both readers) and "replay" (openai only).
"grade" is relabelled "set a level".

Graded by Claude, 2026-11-27, against the definitions at commit `9d2b864`, the commit the
prompt was built from. A guess counts as right when a reader holding it would use the
label where the glossary means it. Both readers saw only [`prompt.md`](./prompt.md),
which lists the labels with no definitions. Run details are at the top of
[`guesses-openai.md`](./guesses-openai.md) and [`guesses-gemini.md`](./guesses-gemini.md)
(commit `cc4b0e8`).

| Reader | Right | Of | Share | Target |
|---|---|---|---|---|
| openai (`gpt-6.2-astra`) | 31 | 33 | 94% | ≥ 80% |
| gemini (`gemini-4-carbon-high`) | 32 | 33 | 97% | ≥ 80% |

## Misses and what changed

| Label | Glossary meaning | openai guess | gemini guess | Fix |
|---|---|---|---|---|
| grade | the control sets a level (a risk tier, a trust level) that other rules read | how well a result meets criteria | an evaluation or score of quality | label is now **set a level**, ID `grade` kept so round-1 answers still read; "grade" is an alias. Both readers took the eval sense, which the entry's near miss already excluded. |
| replay | a framework re-runs a step to rebuild state, so its tool calls must be safe to repeat | using a record to reconstruct how a run unfolded | re-running recorded events to reconstruct state, audit or test: right on rebuilding state | near miss added for replaying a recorded trace to audit or test. |

## Close calls, counted right

- **steer** (openai): "a person or controller gives an active agent guidance". The
  person sense is the stage-1 near miss; "controller" fits, so it counts, but the near
  miss stays.
- **redirect** (gemini): "stopping or rejecting the agent's current action and sending
  the run down a different path". Rejecting is `gate`; sending the run another way is
  this. Counted right; the value entry already says the run goes on.
- **blocking monitor** (openai): "a component that watches a run and can prevent it from
  advancing". Ours is a second model checking actions; the reader did not say model, but
  would use the label in the right place.

## The revision pass (M8 retest)

`compaction`, `steer`, `handoff`, `approval`, `permission-mode`, `sandbox` and
`precedence` were all guessed right by both readers. Both read `handoff` as passing the
task with its context (not a decision), and both read `escalation` as routing a decision
up, which is the split R3 made.

## Outcome

T9 holds for stage 3. One relabel and one near miss, both in
[`../../../glossary.md`](../../../glossary.md).
