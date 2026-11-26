# Round 1: results

**In one line**: both raters are in and every facet clears κ ≥ 0.6 (lowest: detection at 0.78); six disagreements to review.

- **Files tested**: `facets.md` and `glossary.md` at commit `a128b62` (2026-11-25).
- **Rater A**: Claude, a fresh session that read only [`prompt-claude.md`](./prompt-claude.md),
  2026-11-25. Answers: [`answers/claude.csv`](./answers/claude.csv). 30 rows, every value
  from the lists; 6 notes marked `unsure`.
- **Rater B**: Gemini 3.8 Flash (`gemini-3.8-flash`, Google AI Studio free-tier key), called
  through strata-models on omarchy (job 90221, model key `gemini-3.8-flash-api`), 2026-11-25.
  The whole of [`prompt-second.md`](./prompt-second.md) as the only prompt, effort `medium`;
  temperature cannot be set on this runtime (it ignores it). 3,349 tokens in, 15,878 out
  (mostly thinking), $0.00. Answers: [`answers/gemini.csv`](./answers/gemini.csv), the full
  reply in [`answers/gemini-raw.md`](./answers/gemini-raw.md). 30 rows, every id from
  `items.csv`, every value from the lists; 4 notes marked `unsure`.

## Kappa per facet

`python3 tools/kappa.py domains/ux/rounds/round-1/answers/claude.csv domains/ux/rounds/round-1/answers/gemini.csv` (Claude vs Gemini), 30 items.
Target κ ≥ 0.6 on every facet (J5).

| Facet | Agreement | Cohen's kappa |
|---|---|---|
| aspect | 93% | 0.92 |
| brief_override | 97% | 0.92 |
| detection | 90% | 0.78 |
| mode | 100% | 1.00 |

Disagreements (Claude / Gemini):

- `r02` aspect: colour / component
- `r11` aspect: colour / imagery
- `r22` brief_override: defect / slop
- `r13` detection: code / judgement
- `r19` detection: code / judgement
- `r30` detection: code / judgement

Gemini's own `unsure` notes: `r04` (typography or layout), `r08` (sound as interaction),
`r18` (interaction or copy), `r20` (component for a blank render). Two of these match rater
A's Unsorted candidates (`r08`, `r20`): both raters agreed on a value but neither was happy.

## What rater A flagged on its own

Recorded now and not acted on, so the files stay as rater B sees them:

- `r08` (sound with no off switch) and `r20` (blank render) fitted no aspect value. These
  are T7 **Unsorted** candidates: sound has no home, and a whole-page failure is not one
  part of the interface.
- `r02`, `r25`: colour against component (chart styling, glass).
- `r17` (`transition: all`): defect or slop is unclear for a performance check.
- `r22` (dark mode inverted): defect or slop.
