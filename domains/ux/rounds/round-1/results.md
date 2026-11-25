# Round 1: results

**In one line**: waiting on the second rater; rater A's answers are in.

- **Files tested**: `facets.md` and `glossary.md` at commit `a128b62` (2026-11-25).
- **Rater A**: Claude, a fresh session that read only [`prompt-claude.md`](./prompt-claude.md),
  2026-11-25. Answers: [`answers/claude.csv`](./answers/claude.csv). 30 rows, every value
  from the lists; 6 notes marked `unsure`.
- **Rater B**: an OpenAI or Gemini model, run from omarchy with
  [`prompt-second.md`](./prompt-second.md). Not run yet.

## Kappa per facet

Not scored yet (needs rater B). Target κ ≥ 0.6 on every facet (J5).

## What rater A flagged on its own

Recorded now and not acted on, so the files stay as rater B sees them:

- `r08` (sound with no off switch) and `r20` (blank render) fitted no aspect value. These
  are T7 **Unsorted** candidates: sound has no home, and a whole-page failure is not one
  part of the interface.
- `r02`, `r25`: colour against component (chart styling, glass).
- `r17` (`transition: all`): defect or slop is unclear for a performance check.
- `r22` (dark mode inverted): defect or slop.
