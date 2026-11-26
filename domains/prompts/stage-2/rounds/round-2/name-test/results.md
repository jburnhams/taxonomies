# Stage-2 name test (T9): results

**In one line**: both fresh readers are well above the 80% target (openai 29 of 31, 94%;
gemini 30 of 31, 97%). The misses were "note" (both readers) and "framing" (openai only).
"note" is relabelled "work note".

Graded by Claude, 2026-11-26, against the definitions at commit `9ced6b7`, the commit the
prompt was built from. A guess counts as right when a reader holding it would use the
label where the glossary means it. Both readers saw only [`prompt.md`](./prompt.md),
which lists the labels with no definitions. Run details are at the top of
[`guesses-openai.md`](./guesses-openai.md) and [`guesses-gemini.md`](./guesses-gemini.md)
(commit `427c5fd`).

| Reader | Right | Of | Share | Target |
|---|---|---|---|---|
| openai (`gpt-6.2-astra`) | 29 | 31 | 94% | ≥ 80% |
| gemini (`gemini-4-carbon-high`) | 30 | 31 | 97% | ≥ 80% |

## Misses and what changed

| Label | Glossary meaning | openai guess | gemini guess | Fix |
|---|---|---|---|---|
| note | a memory one run or pipeline writes for its own later runs, about the work in hand | any saved piece of text | any saved entry or topic file | label is now **work note**, with "note" and "agent note" as aliases. Both readers took the everyday sense, which harvest homonym 7 predicted |
| framing | where chosen text sits and how much it counts | the wording that tells the model what role a text plays | right: cues on where the text came from and how authoritative it is | no change. The definition holds, and gemini read it right. openai missed position, so a near miss on placement is added |

All six `reach` labels, all four `operation` labels other than `framing`, and all three
`content` labels were guessed right by both readers. Of the 16 context terms, only
"note" was missed.

## Outcome

T9 passes. `work-note` and `framing` stay `candidate`, like every stage-2 entry, until
stage 2 is adopted.
