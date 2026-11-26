# Round 1: results

**In one line**: all three raters answered all 30 items and every facet passes; part and stage were unanimous (Fleiss' κ 1.00), check 0.78, and the non-Claude pair 1.00, 1.00, 0.74.

- **Files tested**: `facets.md` and `glossary.md` at commit `dc3df29`; prompts and items at kit commit `0db889f` (2026-11-26).
- **Rater claude**: Claude Opus 5.5 (`claude-opus-5-5`), Claude Code `claude -p`, effort high, no tools. [`answers/claude.csv`](./answers/claude.csv), [raw](./answers/claude-raw.md). 4 notes marked `unsure`.
- **Rater openai**: GPT-6.2-Astra (`gpt-6.2-astra`), `codex exec`, read-only sandbox, reasoning effort high, web search off; no tool calls. [`answers/openai.csv`](./answers/openai.csv), [raw](./answers/openai-raw.md). 1 note marked `unsure`.
- **Rater gemini**: Gemini 4 Carbon High (`gemini-4-carbon-high`), Antigravity `agy -p`, sandboxed. [`answers/gemini.csv`](./answers/gemini.csv), [raw](./answers/gemini-raw.md). 1 note marked `unsure`.
- All three ran on omarchy on 2026-11-26 from fresh empty directories holding only their own prompt file, on Jonathan's plans (no API keys, no proxy), with the same models and flags as the prompts rounds. Every answer has 30 rows with the ids in `items.csv`, and only listed values.

Target (J5, J23): Fleiss' κ ≥ 0.6 on each facet, and the non-Claude pair κ ≥ 0.6.

| Facet | Fleiss' κ (3 raters) | openai-gemini κ | Pass? |
|---|---|---|---|
| part | 1.00 | 1.00 | yes |
| stage | 1.00 | 1.00 | yes |
| check | 0.78 | 0.74 | yes |

## All three raters

`python3 tools/kappa.py domains/taxonomies/rounds/round-1/answers/{claude,openai,gemini}.csv`

```
raters: claude, openai, gemini; items compared: 30

| Facet | Unanimous | Fleiss' kappa | claude-openai | claude-gemini | openai-gemini |
|---|---|---|---|---|---|
| part | 100% | 1.00 | 1.00 | 1.00 | 1.00 |
| stage | 100% | 1.00 | 1.00 | 1.00 | 1.00 |
| check | 87% | 0.78 | 0.84 | 0.74 | 0.74 |

Not unanimous (claude / openai / gemini); majority value, or SPLIT when none (M5):
- `r14` check: judgement / script / judgement -> judgement
- `r18` check: owner-decision / judgement / judgement -> judgement
- `r22` check: script / script / judgement -> script
- `r28` check: script / script / judgement -> script
```

## The non-Claude pair

`python3 tools/kappa.py domains/taxonomies/rounds/round-1/answers/{openai,gemini}.csv`

```
raters: openai, gemini; items compared: 30

| Facet | Agreement | Cohen's kappa |
|---|---|---|
| part | 100% | 1.00 |
| stage | 100% | 1.00 |
| check | 90% | 0.74 |

Disagreements (openai / gemini):
- `r14` check: script / judgement
- `r22` check: script / judgement
- `r28` check: script / judgement
```
