# Voice stage 1, round 1: results

**In one line**: all three facets pass J23. Fleiss' κ is 0.96 on `area`, 1.00 on
`modality` and 0.81 on `trait`, and the non-Claude pair scores 0.97, 1.00 and 0.77. One
item (`r20`) had no majority on `trait` and goes to **Unsorted**.

Run on omarchy on 2026-11-27 (kit `9762bc8`, answers `f05f2e0`). The three raters were
Claude Opus 5.5 (`claude -p`), GPT-6.2-Astra (`codex exec`, effort high) and Gemini 4
Carbon High (`agy -p`). Each ran in a new empty folder with only its prompt (method v1.1
M6). Run details are at the top of each `answers/<rater>-raw.md`. The CLIs' own system
prompts could not be removed, nor could the user's global `~/.claude/CLAUDE.md` and
`~/.codex/AGENTS.md`. Those are about the machine's repos and say nothing about taxonomies.

## Scores (`tools/kappa.py`, 40 items)

| Facet | Unanimous | Fleiss κ | claude-openai | claude-gemini | openai-gemini |
|---|---|---|---|---|---|
| area | 95% | 0.96 | 0.97 | 0.94 | 0.97 |
| modality | 100% | 1.00 | 1.00 | 1.00 | 1.00 |
| trait | 80% | 0.81 | 0.90 | 0.77 | 0.77 |

Pass (J23): every Fleiss' κ is ≥ 0.6, and every openai-gemini κ is ≥ 0.6.

## Disagreements (claude / openai / gemini → majority, M5)

- `r16` area: evaluation / representation / representation → representation (eGeMAPS: a
  feature set whose use the item does not state).
- `r17` area: preparation / preparation / generation → preparation (filters on synthetic
  clips).
- `r03` trait: whole-voice / naturalness / naturalness → naturalness
- `r05` trait: identity / identity / naturalness → identity
- `r08` trait: identity / identity / whole-voice → identity
- `r14` trait: identity / content / identity → identity (a pronunciation lexicon whose
  point is accent)
- `r20` trait: whole-voice / expression / naturalness → **SPLIT**, to Unsorted
- `r23` trait: content / content / whole-voice → content
- `r39` trait: identity / identity / whole-voice → identity
- `r40` trait: naturalness / naturalness / expression → naturalness

**Pattern**: 6 of the 8 `trait` disagreements involve `whole-voice`. Gemini used it for
items that name a part of the voice only through a metric or a model (`r08`, `r23`,
`r39`). Claude used it for items about stored features or a model release that name no
quality (`r03`, `r20`). The fix tightens `whole-voice` and adds a near miss for each case
(see `changelog.md`). `modality` at 1.00 shows the doc-name rule is clear. It may also
mean the round held few `both` items: the majority put 2 of 40 there.
