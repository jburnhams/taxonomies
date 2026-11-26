# Round 3: results

**In one line**: all three raters answered all 60 items and every facet passes, for all three (Fleiss' κ area 0.80, decider 0.77, moment 0.86) and for the non-Claude pair (0.76, 0.76, 0.83).

- **Files tested**: `facets.md` and `glossary.md` at commit `5d0ad9e` (2026-11-26), the kit commit too.
- **Rater claude**: Claude Opus 5.5 (`claude-opus-5-5`), Claude Code `claude -p`, effort high, no tools. [`answers/claude.csv`](./answers/claude.csv), [raw](./answers/claude-raw.md). 14 notes marked `unsure`.
- **Rater openai**: GPT-6.2-Astra (`gpt-6.2-astra`), `codex exec`, read-only sandbox, reasoning effort high, web search off. [`answers/openai.csv`](./answers/openai.csv), [raw](./answers/openai-raw.md). 11 notes marked `unsure`.
- **Rater gemini**: Gemini 4 Carbon High (`gemini-4-carbon-high`), Antigravity `agy -p`, sandboxed. [`answers/gemini.csv`](./answers/gemini.csv), [raw](./answers/gemini-raw.md). 21 notes marked `unsure`.
- All three ran on omarchy on 2026-11-26 from fresh empty directories holding only their own prompt file, on Jonathan's plans (no API keys), same models and flags as rounds 1 and 2. Every answer has 60 rows with the ids in `items.csv`, and only listed values.

Target (J5, M4): Fleiss' κ ≥ 0.6 on each facet, and the non-Claude pair κ ≥ 0.6.

| Facet | Fleiss' κ (3 raters) | openai-gemini κ | Pass? |
|---|---|---|---|
| area | 0.80 | 0.76 | yes |
| decider | 0.77 | 0.76 | yes |
| moment | 0.86 | 0.83 | yes |

## All three raters

`python3 tools/kappa.py domains/prompts/rounds/round-3/answers/{claude,openai,gemini}.csv`

```
raters: claude, openai, gemini; items compared: 60

| Facet | Unanimous | Fleiss' kappa | claude-openai | claude-gemini | openai-gemini |
|---|---|---|---|---|---|
| area | 75% | 0.80 | 0.74 | 0.90 | 0.76 |
| decider | 87% | 0.77 | 0.79 | 0.76 | 0.76 |
| moment | 83% | 0.86 | 0.87 | 0.87 | 0.83 |

Not unanimous (claude / openai / gemini); majority value, or SPLIT when none (M5):
- `g01` area: tool / tool / context -> tool
- `g02` area: context / control / control -> control
- `g03` area: model / tool / model -> model
- `g09` area: control / control / coordination -> control
- `g12` area: operations / control / operations -> operations
- `g22` area: verification / control / control -> control
- `g24` area: tool / operations / tool -> tool
- `g26` area: control / operations / control -> control
- `g31` area: coordination / control / coordination -> coordination
- `g39` area: model / tool / tool -> tool
- `g45` area: output / tool / output -> output
- `g48` area: model / tool / model -> model
- `g57` area: control / tool / control -> control
- `g61` area: tool / verification / tool -> tool
- `g62` area: operations / tool / operations -> operations
- `g01` decider: rule / rule / working-model -> rule
- `g04` decider: working-model / rule / rule -> rule
- `g05` decider: working-model / rule / working-model -> working-model
- `g10` decider: working-model / working-model / rule -> working-model
- `g45` decider: person / person / rule -> person
- `g52` decider: working-model / rule / working-model -> working-model
- `g59` decider: person / rule / rule -> rule
- `g65` decider: second-model / rule / rule -> rule
- `g11` moment: tool-call / tool-call / turn -> tool-call
- `g12` moment: setup / tool-call / setup -> setup
- `g22` moment: ending / turn / turn -> turn
- `g29` moment: setup / setup / tool-call -> setup
- `g45` moment: ending / tool-call / tool-call -> tool-call
- `g48` moment: setup / setup / turn -> setup
- `g53` moment: ending / after-run / ending -> ending
- `g57` moment: tool-call / setup / tool-call -> tool-call
- `g61` moment: tool-call / after-run / tool-call -> tool-call
- `g66` moment: ending / ending / setup -> ending
```

## The non-Claude pair (M4)

`python3 tools/kappa.py domains/prompts/rounds/round-3/answers/{openai,gemini}.csv`

```
raters: openai, gemini; items compared: 60

| Facet | Agreement | Cohen's kappa |
|---|---|---|
| area | 80% | 0.76 |
| decider | 92% | 0.76 |
| moment | 87% | 0.83 |

Disagreements (openai / gemini):
- `g01` area: tool / context
- `g03` area: tool / model
- `g09` area: control / coordination
- `g12` area: control / operations
- `g24` area: operations / tool
- `g26` area: operations / control
- `g31` area: control / coordination
- `g45` area: tool / output
- `g48` area: tool / model
- `g57` area: tool / control
- `g61` area: verification / tool
- `g62` area: tool / operations
- `g01` decider: rule / working-model
- `g05` decider: rule / working-model
- `g10` decider: working-model / rule
- `g45` decider: person / rule
- `g52` decider: rule / working-model
- `g11` moment: tool-call / turn
- `g12` moment: tool-call / setup
- `g29` moment: setup / tool-call
- `g48` moment: setup / turn
- `g53` moment: after-run / ending
- `g57` moment: setup / tool-call
- `g61` moment: after-run / tool-call
- `g66` moment: ending / setup
```
