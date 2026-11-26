# Stage 2, round 2: results

**In one line**: all three raters answered all 30 items and every facet passes, for all three (Fleiss' κ operation 0.89, content 1.00, reach 0.84) and for the non-Claude pair (0.83, 1.00, 0.83).

- **Kit**: commit `a73ecfd` (2026-11-26), after the round-1 reach fixes.
- **Raters**: Claude Opus 5.5 (`claude -p --model opus`, effort high, no tools); GPT-6.2-Astra (`codex exec`, read-only sandbox, effort high, web search off, no tool calls); Gemini 4 Carbon High (`agy -p --sandbox`). Same flags as round 1; details at the top of each `answers/<rater>-raw.md`.
- All three ran on omarchy on 2026-11-26 from fresh empty directories holding only their own prompt, on Jonathan's plans (no API keys, no proxy). Each answer has 30 rows with the ids in `items.csv`, and only listed values. Notes marked `unsure`: claude 12, openai 4, gemini 5.

| Facet | Fleiss' κ (3 raters) | openai-gemini κ | Pass? |
|---|---|---|---|
| in_area (reported) | 0.85 | 0.78 | n/a |
| operation | 0.89 | 0.83 | yes |
| content | 1.00 | 1.00 | yes |
| reach | 0.84 | 0.83 | yes |

Items most raters put outside the area (left to stage 1): `ch28`, `ch30`.

## Scores

```
raters: claude, openai, gemini; items compared: 30

| Facet | Unanimous | Fleiss' kappa | claude-openai | claude-gemini | openai-gemini |
|---|---|---|---|---|---|
| in_area | 97% | 0.85 | 1.00 | 0.78 | 0.78 |

Not unanimous (claude / openai / gemini); majority value, or SPLIT when none (M5):
- `ch08` in_area: yes / yes / no -> yes
=====
--where in_area=yes: kept 28 of 30 items (dropped: ch28, ch30)
raters: claude, openai, gemini; items compared: 28

| Facet | Unanimous | Fleiss' kappa | claude-openai | claude-gemini | openai-gemini |
|---|---|---|---|---|---|
| operation | 89% | 0.89 | 0.83 | 1.00 | 0.83 |
| content | 100% | 1.00 | 1.00 | 1.00 | 1.00 |
| reach | 89% | 0.84 | 0.84 | 0.84 | 0.83 |

Not unanimous (claude / openai / gemini); majority value, or SPLIT when none (M5):
- `ch06` operation: supply / recording / supply -> supply
- `ch09` operation: framing / supply / framing -> framing
- `ch18` operation: recording / framing / recording -> recording
- `ch06` reach: organization-scope / project-scope / project-scope -> project-scope
- `ch24` reach: built-in-scope / built-in-scope / organization-scope -> built-in-scope
- `ch27` reach: organization-scope / project-scope / organization-scope -> organization-scope
=====
--where in_area=yes: kept 28 of 30 items (dropped: ch28, ch30)
raters: openai, gemini; items compared: 28

| Facet | Agreement | Cohen's kappa |
|---|---|---|
| operation | 89% | 0.83 |
| content | 100% | 1.00 |
| reach | 93% | 0.83 |

Disagreements (openai / gemini):
- `ch06` operation: recording / supply
- `ch09` operation: supply / framing
- `ch18` operation: framing / recording
- `ch24` reach: built-in-scope / organization-scope
- `ch27` reach: project-scope / organization-scope
```
