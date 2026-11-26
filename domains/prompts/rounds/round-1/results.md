# Round 1: results

**In one line**: all three raters answered all 60 items; area passes easily (Fleiss' κ 0.93), moment passes (0.72), decider misses (0.58), and the non-Claude pair misses on decider (0.57) and just on moment (0.69).

- **Files tested**: `facets.md` and `glossary.md` at commit `962c408` (2026-11-26); prompts and items at kit commit `e923f21`.
- **Rater claude**: Claude Opus 5.5 (`claude-opus-5-5`), Claude Code `claude -p`, effort high, no tools. [`answers/claude.csv`](./answers/claude.csv), [raw](./answers/claude-raw.md). 9 notes marked `unsure`.
- **Rater openai**: GPT-6.2-Astra (`gpt-6.2-astra`), `codex exec`, read-only sandbox, reasoning effort high, web search off. [`answers/openai.csv`](./answers/openai.csv), [raw](./answers/openai-raw.md). 7 notes marked `unsure`.
- **Rater gemini**: Gemini 4 Carbon High (`gemini-4-carbon-high`), Antigravity `agy -p`, sandboxed. [`answers/gemini.csv`](./answers/gemini.csv), [raw](./answers/gemini-raw.md). 1 note marked `unsure`.
- All three ran on omarchy on 2026-11-26 from fresh empty directories holding only their own prompt file, on Jonathan's plans (no API keys). Every answer has 60 rows, ids `r01`-`r60` and `h01`-`h04` as in `items.csv`, and only listed values. A first run with the prompts before `e923f21` was discarded unscored.

Target (J5, M4): Fleiss' κ ≥ 0.6 on each facet, and the non-Claude pair κ ≥ 0.6.

| Facet | Fleiss' κ (3 raters) | openai-gemini κ | Pass? |
|---|---|---|---|
| area | 0.93 | 0.92 | yes |
| decider | 0.58 | 0.57 | **no** |
| moment | 0.72 | 0.69 | yes |

## All three raters

`python3 tools/kappa.py domains/prompts/rounds/round-1/answers/{claude,openai,gemini}.csv`

```
raters: claude, openai, gemini; items compared: 60

| Facet | Unanimous | Fleiss' kappa | claude-openai | claude-gemini | openai-gemini |
|---|---|---|---|---|---|
| area | 92% | 0.93 | 0.90 | 0.98 | 0.92 |
| decider | 83% | 0.58 | 0.64 | 0.53 | 0.57 |
| moment | 72% | 0.72 | 0.71 | 0.76 | 0.69 |

Not unanimous (claude / openai / gemini); majority value, or SPLIT when none (M5):
- `r19` area: context / tool / tool -> tool
- `r29` area: operations / control / operations -> operations
- `r33` area: coordination / operations / coordination -> coordination
- `r34` area: tool / control / tool -> tool
- `r41` area: output / tool / output -> output
- `r05` decider: rule / working-model / rule -> rule
- `r15` decider: rule / rule / second-model -> rule
- `r24` decider: rule / working-model / working-model -> working-model
- `r26` decider: rule / rule / second-model -> rule
- `r31` decider: working-model / working-model / rule -> working-model
- `r34` decider: rule / working-model / rule -> rule
- `r41` decider: working-model / working-model / rule -> working-model
- `r45` decider: working-model / rule / rule -> rule
- `r54` decider: second-model / rule / rule -> rule
- `r55` decider: rule / working-model / rule -> rule
- `r04` moment: after-run / setup / setup -> setup
- `r07` moment: after-run / tool-call / after-run -> after-run
- `r09` moment: tool-call / setup / tool-call -> tool-call
- `r14` moment: tool-call / setup / setup -> setup
- `r19` moment: setup / tool-call / setup -> setup
- `r22` moment: after-run / setup / setup -> setup
- `r23` moment: turn / setup / turn -> turn
- `r27` moment: after-run / setup / setup -> setup
- `r34` moment: setup / tool-call / setup -> setup
- `r39` moment: setup / setup / tool-call -> setup
- `r41` moment: tool-call / tool-call / setup -> tool-call
- `r43` moment: setup / setup / tool-call -> setup
- `r45` moment: tool-call / setup / setup -> setup
- `r46` moment: ending / setup / ending -> ending
- `r47` moment: ending / setup / ending -> ending
- `r55` moment: ending / ending / setup -> ending
- `h03` moment: setup / setup / turn -> setup
```

## The non-Claude pair (M4)

`python3 tools/kappa.py domains/prompts/rounds/round-1/answers/{openai,gemini}.csv`

```
raters: openai, gemini; items compared: 60

| Facet | Agreement | Cohen's kappa |
|---|---|---|
| area | 93% | 0.92 |
| decider | 88% | 0.57 |
| moment | 80% | 0.69 |

Disagreements (openai / gemini):
- `r29` area: control / operations
- `r33` area: operations / coordination
- `r34` area: control / tool
- `r41` area: tool / output
- `r05` decider: working-model / rule
- `r15` decider: rule / second-model
- `r26` decider: rule / second-model
- `r31` decider: working-model / rule
- `r34` decider: working-model / rule
- `r41` decider: working-model / rule
- `r55` decider: working-model / rule
- `r07` moment: tool-call / after-run
- `r09` moment: setup / tool-call
- `r19` moment: tool-call / setup
- `r23` moment: setup / turn
- `r34` moment: tool-call / setup
- `r39` moment: setup / tool-call
- `r41` moment: tool-call / setup
- `r43` moment: setup / tool-call
- `r46` moment: setup / ending
- `r47` moment: setup / ending
- `r55` moment: ending / setup
- `h03` moment: setup / turn
```
