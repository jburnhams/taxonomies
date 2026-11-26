# Stage 2, round 1: results

**In one line**: all three raters answered all 30 items; `operation` (Fleiss' κ 0.82) and `content` (0.88) pass, `reach` passes for all three (0.68) but misses for the non-Claude pair (0.53).

- **Kit**: commit `258f560` (2026-11-26).
- **Raters**: Claude Opus 5.5 (`claude -p --model opus`, effort high, no tools); GPT-6.2-Astra (`codex exec`, read-only sandbox, effort high, web search off, no tool calls); Gemini 4 Carbon High (`agy -p --sandbox`). Same flags as stage 1 round 3; details at the top of each `answers/<rater>-raw.md`.
- All three ran on omarchy on 2026-11-26 from fresh empty directories holding only their own prompt, on Jonathan's plans (no API keys, no proxy). Each answer has 30 rows with the ids in `items.csv`, and only listed values. Notes marked `unsure`: claude 16, openai 16, gemini 10.

| Facet | Fleiss' κ (3 raters) | openai-gemini κ | Pass? |
|---|---|---|---|
| in_area (reported) | 0.75 | 0.63 | n/a |
| operation | 0.82 | 0.84 | yes |
| content | 0.88 | 0.82 | yes |
| reach | 0.68 | 0.53 | **no** (pair) |

Items most raters put outside the area (left to stage 1): `cr10`, `cr16`, `cr21`.

## Scores

```
raters: claude, openai, gemini; items compared: 30

| Facet | Unanimous | Fleiss' kappa | claude-openai | claude-gemini | openai-gemini |
|---|---|---|---|---|---|
| in_area | 93% | 0.75 | 0.84 | 0.78 | 0.63 |

Not unanimous (claude / openai / gemini); majority value, or SPLIT when none (M5):
- `cr16` in_area: no / no / yes -> no
- `cr24` in_area: yes / no / yes -> yes
=====
--where in_area=yes: kept 27 of 30 items (dropped: cr10, cr16, cr21)
raters: claude, openai, gemini; items compared: 27

| Facet | Unanimous | Fleiss' kappa | claude-openai | claude-gemini | openai-gemini |
|---|---|---|---|---|---|
| operation | 81% | 0.82 | 0.79 | 0.84 | 0.84 |
| content | 89% | 0.88 | 0.82 | 1.00 | 0.82 |
| reach | 67% | 0.68 | 0.68 | 0.84 | 0.53 |

Not unanimous (claude / openai / gemini); majority value, or SPLIT when none (M5):
- `cr12` operation: supply / framing / supply -> supply
- `cr13` operation: recording / supply / supply -> supply
- `cr14` operation: recording / recording / supply -> recording
- `cr19` operation: supply / framing / supply -> supply
- `cr26` operation: supply / framing / framing -> framing
- `cr05` content: kept-knowledge / run-history / kept-knowledge -> kept-knowledge
- `cr06` content: kept-knowledge / run-history / kept-knowledge -> kept-knowledge
- `cr12` content: instruction-text / run-history / instruction-text -> instruction-text
- `cr03` reach: user-scope / project-scope / user-scope -> user-scope
- `cr05` reach: project-scope / conversation-scope / project-scope -> project-scope
- `cr06` reach: project-scope / project-scope / user-scope -> project-scope
- `cr08` reach: user-scope / project-scope / user-scope -> user-scope
- `cr12` reach: organization-scope / conversation-scope / organization-scope -> organization-scope
- `cr13` reach: organization-scope / project-scope / organization-scope -> organization-scope
- `cr14` reach: project-scope / project-scope / user-scope -> project-scope
- `cr18` reach: user-scope / user-scope / project-scope -> user-scope
- `cr24` reach: project-scope / user-scope / project-scope -> project-scope
=====
--where in_area=yes: kept 27 of 30 items (dropped: cr10, cr16, cr21)
raters: openai, gemini; items compared: 27

| Facet | Agreement | Cohen's kappa |
|---|---|---|
| operation | 89% | 0.84 |
| content | 89% | 0.82 |
| reach | 67% | 0.53 |

Disagreements (openai / gemini):
- `cr12` operation: framing / supply
- `cr14` operation: recording / supply
- `cr19` operation: framing / supply
- `cr05` content: run-history / kept-knowledge
- `cr06` content: run-history / kept-knowledge
- `cr12` content: run-history / instruction-text
- `cr03` reach: project-scope / user-scope
- `cr05` reach: conversation-scope / project-scope
- `cr06` reach: project-scope / user-scope
- `cr08` reach: project-scope / user-scope
- `cr12` reach: conversation-scope / organization-scope
- `cr13` reach: project-scope / organization-scope
- `cr14` reach: project-scope / user-scope
- `cr18` reach: user-scope / project-scope
- `cr24` reach: user-scope / project-scope
```

## Fixes after scoring (2026-11-26)

`operation` and `content` pass on both conditions. `reach` fails the non-Claude pair
(0.53). Its nine pair splits have two causes, and the `unsure` notes name both.

| Cause | Items | Fix |
|---|---|---|
| Text shipped with the harness or a Keel configuration (a product's own system prompt, reviewer core, specialist wrapper, delegate prompt) had no value. All three raters forced `organization-scope` and noted it | `cr04`, `cr12`, `cr19`, `cr25` | new value **`built-in-scope`** |
| A store, catalog or MCP server whose sharing the section does not state: raters guessed user or project | `cr03`, `cr06`, `cr08`, `cr14`, `cr18`, `cr24` | rule: unstated means `project-scope`, unless the text says the store follows a person or a team |
| A recording judged by where its input came from (one session) rather than who reads its output | `cr05` | rule: a recording takes the reach of the runs that will read what it keeps |
| A prior attempt handed to the next run | `cr12` | named in `conversation-scope`'s scope |

`cr13` (a resolver by subject, project or org) is left as it is: the section names both.

Adding a value is a change to the facet, so round 2 has to show it holds (ending
condition "no facet added, split or merged in the last round").
`in_area`: `cr10`, `cr16` and `cr21` were put outside the area by most raters
(tool, tool, control), which agrees with stage 1's definitions. Not acted on.

Round 2: `ch01`-`ch30`, kit in [`../round-2/`](../round-2/README.md).

