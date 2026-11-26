# Round 1: results

**In one line**: both raters are in and every facet clears κ ≥ 0.6 (lowest: detection at 0.78); the six disagreements were fixed in the scope notes, and round 1 met the ending conditions.

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

## Fixes after scoring (2026-11-26)

Each is a **redefine** in [`../../changelog.md`](../../changelog.md), made after both raters had
answered, so round 1 tested the files at `a128b62`:

| Item | Split | Fix |
|---|---|---|
| `r02` | aspect colour / component | `colour` scope: a chart's fill is colour; how it is drawn is `component` |
| `r11` | aspect colour / imagery | `imagery` scope: decorative shapes drawn as pictures (blobs) |
| `r22` | slop / defect | `defect` scope: a dark mode made by inverting the light theme; performance faults (`r17`) |
| `r13`, `r19`, `r30` | detection code / judgement | `code` and `judgement` scope: for copy, matching a word list is code, reading for meaning is judgement |
| `r04`, `r08`, `r18` | both or one unsure | `typography` covers figures; `interaction` covers form behaviour and sound; `copy` excludes label presence |
| `r20` | both unsure | to **Unsorted** under `aspect` (a whole-page failure) |

## Ending conditions ([`../../scope.md`](../../scope.md))

| Condition | Result |
|---|---|
| T1-T6 clean | yes, `python3 tools/check_domain.py domains/ux`: 0 problems |
| T7: every item placed or Unsorted, at most 2 Unsorted | yes: 1 (`r20`) |
| T8: κ ≥ 0.6 per facet, two families, 30 fresh items | yes: 0.92, 0.92, 0.78, 1.00 |
| T10: competency questions answered | yes, [`review.md`](./review.md) |
| T11: no unmarked synonym, no missing facet | yes after one alias move, [`review.md`](./review.md) |
| No facet added, split or merged in the last round | yes |

Also run: the name test (T9), [`name-test/results.md`](./name-test/results.md).

Round 2 (16 held items plus 14 from `ux-product-ui.md` and `ux-character.md`) tests the
13 terms changed above, which stay `candidate` until then.
