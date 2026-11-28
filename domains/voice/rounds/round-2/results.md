# Voice stage 1, round 2: results

**In one line**: all three facets pass J23 again, on 40 fresh items. Fleiss' κ is 0.87 on
`area`, 0.96 on `modality` and 0.89 on `trait`, and the non-Claude pair scores 0.91, 0.94
and 0.87. Two items had no majority on `trait`; both are LLM-judge biases.

Run on omarchy on 2026-11-28, from kit `dfebdbb` with answers in `9debcd7`. The raters,
commands and clean-run rules were the same as round 1; run details are at the top of each
`answers/<rater>-raw.md`. Gemini took 23 minutes; the other two took under a minute.

## Scores (`tools/kappa.py`, 40 items)

| Facet | Unanimous | Fleiss κ | claude-openai | claude-gemini | openai-gemini |
|---|---|---|---|---|---|
| area | 85% | 0.87 | 0.84 | 0.87 | 0.91 |
| modality | 98% | 0.96 | 0.94 | 1.00 | 0.94 |
| trait | 90% | 0.89 | 0.90 | 0.90 | 0.87 |

Compared with round 1, `area` fell from 0.96 to 0.87 and `trait` rose from 0.81 to 0.89.
The `whole-voice` redefinition worked: it now appears in only 2 of the 6 trait
disagreements, against 6 of 8 in round 1.

## Disagreements (claude / openai / gemini → majority, M5)

- `h06` area: generation / representation / representation → representation
- `h15` area: preparation / governance / preparation → preparation (redacting names when the text is kept)
- `h19` area: representation / generation / generation → generation
- `h27` area: generation / evaluation / generation → generation (topic-matched examples, in a leakage section)
- `h34` area: preparation / preparation / evaluation → preparation (speaker verifiers as a check on takes)
- `h35` area: elicitation / preparation / preparation → preparation
- `h13` modality: written / both / written → written
- `h07` trait: content / expression / naturalness → **SPLIT** (judges prefer longer text)
- `h09` trait: expression / expression / whole-voice → expression
- `h13` trait: whole-voice / identity / expression → **SPLIT** (self and other labels bias judges)
- `h31` trait: identity / content / identity → identity

The `area` disagreements follow the round-1 rule cases: what a check is used for, and an
item's own point against the section it sits in. Each one resolves to a majority. The two
splits are both about a judge's bias rather than a part of the voice. A new near miss on
`whole-voice` covers them (length and position bias: `whole-voice`; a judge recognising
its own text: `identity`).

**Kit fault**: `sample.py` broke the sentence after "e.g.", so `h36` (MARY TTS) was cut to
end at "(e.g.". All three raters still agreed on it. The draw is kept as rated, and
`sample.py` now skips such breaks for later draws.
