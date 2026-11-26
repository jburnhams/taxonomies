# Round 2: results

**In one line**: all three raters answered all 56 items; every facet passes on Fleiss' κ (area 0.87, decider 0.66, moment 0.72), but the non-Claude pair still misses on decider (0.54); area and moment pass for the pair (0.87, 0.67).

- **Files tested**: `facets.md` and `glossary.md` at commit `6145895` (2026-11-26), the kit commit too.
- **Rater claude**: Claude Opus 5.5 (`claude-opus-5-5`), Claude Code `claude -p`, effort high, no tools. [`answers/claude.csv`](./answers/claude.csv), [raw](./answers/claude-raw.md). 12 notes marked `unsure`.
- **Rater openai**: GPT-6.2-Astra (`gpt-6.2-astra`), `codex exec`, read-only sandbox, reasoning effort high, web search off. [`answers/openai.csv`](./answers/openai.csv), [raw](./answers/openai-raw.md). 11 notes marked `unsure`.
- **Rater gemini**: Gemini 4 Carbon High (`gemini-4-carbon-high`), Antigravity `agy -p`, sandboxed. [`answers/gemini.csv`](./answers/gemini.csv), [raw](./answers/gemini-raw.md). 1 note marked `unsure`.
- All three ran on omarchy on 2026-11-26 from fresh empty directories holding only their own prompt file, on Jonathan's plans (no API keys), same models and flags as round 1. Every answer has 56 rows, ids `h05`-`h60` as in `items.csv`, and only listed values.

Target (J5, M4): Fleiss' κ ≥ 0.6 on each facet, and the non-Claude pair κ ≥ 0.6.

| Facet | Fleiss' κ (3 raters) | openai-gemini κ | Pass? |
|---|---|---|---|
| area | 0.87 | 0.87 | yes |
| decider | 0.66 | 0.54 | **no** (pair) |
| moment | 0.72 | 0.67 | yes |

## All three raters

`python3 tools/kappa.py domains/prompts/rounds/round-2/answers/{claude,openai,gemini}.csv`

```
raters: claude, openai, gemini; items compared: 56

| Facet | Unanimous | Fleiss' kappa | claude-openai | claude-gemini | openai-gemini |
|---|---|---|---|---|---|
| area | 84% | 0.87 | 0.81 | 0.94 | 0.87 |
| decider | 79% | 0.66 | 0.71 | 0.71 | 0.54 |
| moment | 68% | 0.72 | 0.71 | 0.78 | 0.67 |

Not unanimous (claude / openai / gemini); majority value, or SPLIT when none (M5):
- `h07` area: model / control / model -> model
- `h17` area: model / tool / tool -> tool
- `h20` area: context / verification / context -> context
- `h21` area: context / control / context -> context
- `h28` area: control / tool / tool -> tool
- `h32` area: output / tool / output -> output
- `h43` area: coordination / operations / operations -> operations
- `h44` area: context / control / context -> context
- `h46` area: control / coordination / control -> control
- `h05` decider: rule / person / rule -> rule
- `h07` decider: rule / second-model / rule -> rule
- `h16` decider: working-model / rule / rule -> rule
- `h22` decider: second-model / rule / second-model -> second-model
- `h23` decider: working-model / rule / rule -> rule
- `h25` decider: person / person / rule -> person
- `h36` decider: working-model / working-model / rule -> working-model
- `h37` decider: second-model / second-model / rule -> second-model
- `h44` decider: second-model / rule / second-model -> second-model
- `h51` decider: rule / rule / second-model -> rule
- `h57` decider: second-model / rule / second-model -> second-model
- `h60` decider: rule / rule / working-model -> rule
- `h05` moment: after-run / setup / after-run -> after-run
- `h07` moment: turn / tool-call / turn -> turn
- `h08` moment: setup / setup / ending -> setup
- `h12` moment: after-run / setup / after-run -> after-run
- `h16` moment: tool-call / after-run / after-run -> after-run
- `h21` moment: setup / ending / turn -> SPLIT
- `h22` moment: tool-call / setup / tool-call -> tool-call
- `h23` moment: tool-call / setup / setup -> setup
- `h25` moment: setup / setup / turn -> setup
- `h32` moment: tool-call / setup / tool-call -> tool-call
- `h33` moment: after-run / turn / after-run -> after-run
- `h43` moment: setup / setup / after-run -> setup
- `h45` moment: tool-call / failure / tool-call -> tool-call
- `h46` moment: ending / ending / tool-call -> ending
- `h50` moment: tool-call / ending / ending -> ending
- `h56` moment: after-run / setup / after-run -> after-run
- `h58` moment: setup / failure / after-run -> SPLIT
- `h60` moment: setup / setup / tool-call -> setup
```

## The non-Claude pair (M4)

`python3 tools/kappa.py domains/prompts/rounds/round-2/answers/{openai,gemini}.csv`

```
raters: openai, gemini; items compared: 56

| Facet | Agreement | Cohen's kappa |
|---|---|---|
| area | 89% | 0.87 |
| decider | 82% | 0.54 |
| moment | 73% | 0.67 |

Disagreements (openai / gemini):
- `h07` area: control / model
- `h20` area: verification / context
- `h21` area: control / context
- `h32` area: tool / output
- `h44` area: control / context
- `h46` area: coordination / control
- `h05` decider: person / rule
- `h07` decider: second-model / rule
- `h22` decider: rule / second-model
- `h25` decider: person / rule
- `h36` decider: working-model / rule
- `h37` decider: second-model / rule
- `h44` decider: rule / second-model
- `h51` decider: rule / second-model
- `h57` decider: rule / second-model
- `h60` decider: rule / working-model
- `h05` moment: setup / after-run
- `h07` moment: tool-call / turn
- `h08` moment: setup / ending
- `h12` moment: setup / after-run
- `h21` moment: ending / turn
- `h22` moment: setup / tool-call
- `h25` moment: setup / turn
- `h32` moment: setup / tool-call
- `h33` moment: turn / after-run
- `h43` moment: setup / after-run
- `h45` moment: failure / tool-call
- `h46` moment: ending / tool-call
- `h56` moment: setup / after-run
- `h58` moment: failure / after-run
- `h60` moment: setup / tool-call
```

## Reading the result

Under the adopted rules (J5, J6: two families, κ ≥ 0.6 per facet) round 2 passes: Fleiss'
κ clears 0.6 on every facet and so does every pair that includes Claude. It fails only
method v1.1 M4's extra rule, the non-Claude pair on decider (0.54). M4 is a proposal
(J23), not adopted; it is applied here because it is the stricter reading and the fix is
cheap. The pair's ten splits are three patterns, not noise.

## Fixes after scoring (2026-11-26)

Each is a **redefine** in [`../../changelog.md`](../../changelog.md), made after all three
raters had answered, so round 2 tested the files at `6145895`.

| Items | Split (openai / gemini) | Fix |
|---|---|---|
| `h07`, `h22`, `h44`, `h57` | `rule` against `second-model`: a separate model call whose prompt the harness builds or picks | `second-model` scope: a separate model call decides even when the harness builds or picks its prompt |
| `h37`, `h51` | `second-model` / `rule`: a trained risk predictor; a diff check | `second-model` scope names trained predictors; `h51` (a diff check) is `rule` as written |
| `h05`, `h25` | `person` / `rule`: a person starts a watch, a person hands over an image | `person` scope: starting is not deciding; handing over input is |
| `h36`, `h60` | `working-model` / `rule`: sections that survey a spectrum | `rule` scope and the prompt: classify what the section recommends, else mark `unsure` |

No facet added, split or merged. Round 3 uses 60 newly drawn items (`g01`-`g67`, see
[`../../samples.md`](../../samples.md#round-3-test-60)), the same three models, and the
new rules ([`../round-3/`](../round-3/README.md)).
