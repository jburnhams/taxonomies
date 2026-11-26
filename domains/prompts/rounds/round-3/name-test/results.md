# Name test (T9): results

**In one line**: both fresh readers guessed well above the 80% target (openai 51 of 54,
94%; gemini 50 of 54, 93%). Four labels were missed, and each one has been renamed or
redefined in `glossary.md` and set back to `candidate`.

Graded by Claude, 2026-11-26. Each guess was compared with the entry's definition at
commit `a3261b3`, the commit the prompt was built from. A guess counts as right when a
reader holding it would use the label where the glossary means it. Both readers saw
only [`prompt.md`](./prompt.md), which lists the labels with no definitions. Run
details are at the top of [`guesses-openai.md`](./guesses-openai.md) and
[`guesses-gemini.md`](./guesses-gemini.md).

## Scores

| Reader | Right | Of | Share | Target |
|---|---|---|---|---|
| openai (`gpt-6.2-astra`) | 51 | 54 | 94% | ≥ 80% |
| gemini (`gemini-4-carbon-high`) | 50 | 54 | 93% | ≥ 80% |

## Missed labels and what changed

| Label (at `a3261b3`) | Glossary meaning | openai guess | gemini guess | Fix |
|---|---|---|---|---|
| rule (decider value) | fixed logic that decides: harness code, a schema check, a setting applied by code | an instruction or constraint the agent follows | a rules file (persistent instruction) | label is now **fixed logic**, with "rule" as an alias. Both readers took "rule" to mean prompt text, which is the opposite of the ignore test |
| model access (area value) | calling and choosing models: providers, dialects, routing, effort, caching | authentication and connection only | auth, billing and routing layer | label is now **model calling**, with "model access" as an alias. Both guesses were too narrow and missed routing, effort and caching |
| context window | the input a model is given on one request, up to its token limit | a token limit on one request, reply included | a token limit on one call | redefined as **a limit on how many tokens a model accepts on one request, its reply included**. The readers' sense is the common one, so the glossary now uses it, and "context" keeps the content sense |
| steer | a message the harness or a second model adds during a run to redirect the agent | close enough: new guidance while it works | a person's mid-run feedback | near miss added: a person's message typed while the agent works is the person's input (`person` deciding), not a steer. Missed by gemini only |

All other 50 labels were guessed right by both readers, including the three that were
changed after earlier rounds (`working model`, `second model`, `permission mode`).

## Outcome

T9 passes. The four changed entries are `candidate` until a later round retests them.
The other 50 are `approved`. Stage 1 is adopted on this round ([`../../../scope.md`](../../../scope.md)).
