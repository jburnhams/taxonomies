# UX taxonomy: changelog

Every change as a named operation (spec G4), newest day first. The approving agent is
named on each line (G1); Jonathan can reverse any of them.

## 2026-11-25

- **add** set A, chosen by Jonathan: facets `aspect`, `brief-override`, `detection`, `mode`
  are no longer a proposal (process step 4).
- **add** 12 candidate terms for the facet values (`colour`, `typography`, `layout`,
  `component`, `imagery`, `motion`, `copy`, `interaction`, `code`, `render`, `judgement`,
  `any-mode`), and **Facet** fields on `slop`, `defect`, `persuade` and `operate`.
  Scope notes and near misses were written from build items only; three draft phrases that
  echoed round-1 or held items (a staged delay, a modal as the first thought, the Lucide
  icon names, sound) were reworded before the raters saw the files. Approved by: Claude.
- **add** `rounds/round-1/`: items, two rater prompts with values shuffled differently,
  and how to run and score the second rater.
- **move** sample items `r06`, `r07`, `r09`, `r26` (round-1 test) and `h16` (held) into the
  build sample, and `h01`, `h12`, `h14`, `h15` into the round-1 test: the draft facets and
  glossary had drawn on the first five, so they were no longer fresh (process step 2;
  raised in review on PR #5).
- **add** 41 candidate terms to `glossary.md` (general terms and the four modes), with seven
  label choices listed at its top for Jonathan's veto: `surface` is the tonal layer and
  `screen` the thing being built; "layer" goes to `stack-layer`; `defect`; `mood-word`;
  `signature-move` against `model-signature`; `one-question` and `one-finding`. Approved
  by: Claude (thread "Build the ux-research taxonomy"), as candidates only.
- **add** `scope.md`, `samples.md`, `harvest.md`, draft `facets.md`: round 1 started
  (process steps 1-5). Approved by: Claude (thread "Build the ux-research taxonomy").
- **redefine** facet value `render` (proposal, set A): "needs the running page" instead of
  "needs pixels", because a keyboard check (`t04`) needs the page but not a screenshot.
- **add** facet value `imagery` to `aspect` (proposal, set A): `t02` (image `alt` and size)
  fitted no other value.
- **add** rater rule for `detection` (proposal, set A): take the least evidence that finds
  the item as written, after `t03` and `t05`.
