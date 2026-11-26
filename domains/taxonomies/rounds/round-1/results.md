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

## Reading the numbers

Every facet passes both targets. The four splits are all on `check`, and all four are
about where `script` ends: whether a rule whose conditions look checkable (G4's list of
operations, G5's kept record, step 11's link) is settled by a program, and whether a
decision that adds a step Jonathan decides (J13) is his.

Two reasons not to read too much into part 1.00 and stage 1.00:

- **The items gave their ids.** Each began with its own id (`spec N6`, `decision J13`),
  and the definitions name id ranges (`naming` includes N1-N8; `testing` includes T1-T11).
  For most items, `part` and `stage` were a lookup, so this round tested the id ranges
  more than the definitions. The raters' own notes agree: every `unsure` was about an item
  the ranges did not cover (`r01`, J17 on sources; `r24`, J16 on status).
- **30 items is below method v1.1 M3** (◆ J22, merged with the prompts domain the same
  morning): at least 5 per value of the largest facet, so 35 for `part`'s 7 values.

So round 1 counts as passed under J5 and J23, and round 2 tests the same facets on 43
fresh items with the ids removed ([`../round-2/`](../round-2/README.md)).

## Fixes after scoring (2026-11-26)

| Item | Split | Fix |
|---|---|---|
| `r22` G5, `r28` step 11 | script / script / judgement | `script` scope: every condition the item sets must be one a program can test; a clause saying what the item is for ("so agents use it") is not a condition. Majority kept. |
| `r14` G4 | judgement / script / judgement | `script` near miss: G4's list looks checkable, but saying which operation a change is takes reading. `judgement` scope: any condition that needs reading makes the item `judgement`. |
| `r18` J13 | owner-decision / judgement / judgement | `owner-decision` near miss: a decision that adds a step in which Jonathan decides takes the check of the work it settles, not the step's Who. |

No facet or value was added, split or merged.
