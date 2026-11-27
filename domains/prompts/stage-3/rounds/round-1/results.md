# Stage 3, round 1: results

**In one line**: all three raters answered all 30 items and both facets pass, for all three (Fleiss' κ target 0.83, response 0.80) and for the non-Claude pair (0.75, 0.70).

- **Kit**: commit `9d2b864` (2026-11-27).
- **Raters**: Claude Opus 5.5 (`claude -p --model opus`, effort high, no tools); GPT-6.2-Astra (`codex exec`, read-only sandbox, effort high, web search off, no tool calls); Gemini 4 Carbon High (`agy -p --sandbox`). Same flags as stage 2; details at the top of each `answers/<rater>-raw.md`.
- All three ran on omarchy on 2026-11-27 from fresh empty directories holding only their own prompt, on Jonathan's plans (no API keys, no proxy). Each answer has 30 rows with the ids in `items.csv`, and only listed values. Notes marked `unsure`: claude 9, openai 8, gemini 5.
- The name test ran in two other fresh sessions (codex and agy only): [`name-test/`](./name-test/).

| Facet | Fleiss' κ (3 raters) | openai-gemini κ | Pass? |
|---|---|---|---|
| in_area (reported) | 0.80 | 0.90 | n/a |
| target | 0.83 | 0.75 | yes |
| response | 0.80 | 0.70 | yes |

Items most raters put outside the area (left to stage 1): `kr04`, `kr05`, `kr06`, `kr10`, `kr11`, `kr27`.

## Scores

```
raters: claude, openai, gemini; items compared: 30

| Facet | Unanimous | Fleiss' kappa | claude-openai | claude-gemini | openai-gemini |
|---|---|---|---|---|---|
| in_area | 90% | 0.80 | 0.71 | 0.79 | 0.90 |

Not unanimous (claude / openai / gemini); majority value, or SPLIT when none (M5):
- `kr05` in_area: yes / no / no -> no
- `kr09` in_area: yes / no / yes -> yes
- `kr24` in_area: no / yes / yes -> yes
=====
--where in_area=yes: kept 24 of 30 items (dropped: kr04, kr05, kr06, kr10, kr11, kr27)
raters: claude, openai, gemini; items compared: 24

| Facet | Unanimous | Fleiss' kappa | claude-openai | claude-gemini | openai-gemini |
|---|---|---|---|---|---|
| target | 83% | 0.83 | 0.82 | 0.94 | 0.75 |
| response | 79% | 0.80 | 0.81 | 0.88 | 0.70 |

Not unanimous (claude / openai / gemini); majority value, or SPLIT when none (M5):
- `kr12` target: run-course / tool-action / run-course -> run-course
- `kr21` target: tool-action / run-course / tool-action -> tool-action
- `kr25` target: work-product / tool-action / work-product -> work-product
- `kr29` target: incoming-text / incoming-text / tool-action -> incoming-text
- `kr01` response: gate / grade / gate -> gate
- `kr12` response: recover / gate / recover -> recover
- `kr13` response: gate / gate / ask-person -> gate
- `kr21` response: recover / redirect / recover -> recover
- `kr29` response: gate / gate / ask-person -> gate
=====
--where in_area=yes: kept 24 of 30 items (dropped: kr04, kr05, kr06, kr10, kr11, kr27)
raters: openai, gemini; items compared: 24

| Facet | Agreement | Cohen's kappa |
|---|---|---|
| target | 83% | 0.75 |
| response | 79% | 0.70 |

Disagreements (openai / gemini):
- `kr12` target: tool-action / run-course
- `kr21` target: run-course / tool-action
- `kr25` target: tool-action / work-product
- `kr29` target: incoming-text / tool-action
- `kr01` response: grade / gate
- `kr12` response: gate / recover
- `kr13` response: gate / ask-person
- `kr21` response: redirect / recover
- `kr29` response: gate / ask-person
```
