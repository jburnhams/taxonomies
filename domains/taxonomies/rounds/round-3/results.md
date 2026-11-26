# Round 3: results

**In one line**: all three raters answered the check question on all 73 items and it now passes: Fleiss' κ 0.73, the non-Claude pair 0.75 (round 2: 0.55 and 0.45).

- **Files tested**: `facets.md` and `glossary.md` at commit `cac7f1f` (2026-11-26), the kit commit too, with `script` as a closed list.
- **Rater claude**: Claude Opus 5.5 (`claude-opus-5-5`), Claude Code `claude -p`, effort high, no tools. [`answers/claude.csv`](./answers/claude.csv), [raw](./answers/claude-raw.md). 8 notes marked `unsure`.
- **Rater openai**: GPT-6.2-Astra (`gpt-6.2-astra`), `codex exec`, read-only sandbox, reasoning effort high, web search off; no tool calls. [`answers/openai.csv`](./answers/openai.csv), [raw](./answers/openai-raw.md). 1 note marked `unsure`.
- **Rater gemini**: Gemini 4 Carbon High (`gemini-4-carbon-high`), Antigravity `agy -p`, sandboxed. [`answers/gemini.csv`](./answers/gemini.csv), [raw](./answers/gemini-raw.md). No notes marked `unsure`.
- All three ran on omarchy on 2026-11-26 from fresh empty directories holding only their own prompt file, on Jonathan's plans (no API keys, no proxy), same models and flags as rounds 1 and 2. Every answer has 73 rows with the ids in `items.csv`, and only listed values.

Target (J5, J23): Fleiss' κ ≥ 0.6, and the non-Claude pair κ ≥ 0.6.

| Facet | Fleiss' κ (3 raters) | openai-gemini κ | Pass? |
|---|---|---|---|
| check | 0.73 | 0.75 | yes |

The lowest pair is claude-gemini (0.61): four items (`h01`, `h04`, `h05`, `h07`) where Gemini alone said `judgement`.

## All three raters

`python3 tools/kappa.py domains/taxonomies/rounds/round-3/answers/{claude,openai,gemini}.csv`

```
raters: claude, openai, gemini; items compared: 73

| Facet | Unanimous | Fleiss' kappa | claude-openai | claude-gemini | openai-gemini |
|---|---|---|---|---|---|
| check | 89% | 0.73 | 0.82 | 0.61 | 0.75 |

Not unanimous (claude / openai / gemini); majority value, or SPLIT when none (M5):
- `h01` check: script / script / judgement -> script
- `h04` check: script / script / judgement -> script
- `h05` check: script / script / judgement -> script
- `h07` check: script / script / judgement -> script
- `h16` check: judgement / owner-decision / judgement -> judgement
- `s07` check: owner-decision / judgement / judgement -> judgement
- `s08` check: judgement / script / script -> script
- `s25` check: judgement / script / script -> script
```

## The non-Claude pair

`python3 tools/kappa.py domains/taxonomies/rounds/round-3/answers/{openai,gemini}.csv`

```
raters: openai, gemini; items compared: 73

| Facet | Agreement | Cohen's kappa |
|---|---|---|
| check | 93% | 0.75 |

Disagreements (openai / gemini):
- `h01` check: script / judgement
- `h04` check: script / judgement
- `h05` check: script / judgement
- `h07` check: script / judgement
- `h16` check: owner-decision / judgement
```
