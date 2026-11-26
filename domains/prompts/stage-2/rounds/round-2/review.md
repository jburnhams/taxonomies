# Stage 2, round 2: competency questions (T10) and heuristic review (T11)

**In one line**: all seven stage-2 competency questions in [`../../../scope.md`](../../../scope.md)
can be answered from `facets.md` and `glossary.md`. The review found no unmarked synonym
and no missing facet. Stage 2 is ready to adopt once Jonathan chooses the facet set.

Checked by Claude, 2026-11-26, against the files as changed after the name test.

## T10: competency questions

| # | Question | Answered by |
|---|---|---|
| 14 | What puts content in front of the model, and what keeps it for later? | `operation` = `supply` against `recording` |
| 15 | What cuts down what the model already has? | `operation` = `reduction`; terms `compaction`, `truncation`, `compaction-summary` |
| 16 | Which content reaches every run in a repo, and which only one person, one request or one conversation? | facet `reach`: six values, with the defaults for unstated stores |
| 17 | What decides where text sits or how much it counts? | `operation` = `framing`; terms `envelope`, `precedence` |
| 18 | Compaction, truncation, consolidation, summary? | `compaction` (fits this run), `truncation` (cuts without rewriting), `consolidation` (a store, between runs), `compaction-summary` (compaction's product), each with near misses against the others |
| 19 | Memory, learning, note, retrospective? | `memory` (broader), `learning` and `work-note` (narrower, near misses between them), `retrospective` (a happening that may produce learnings) |
| 20 | Progressive disclosure or conditional loading? | `progressive-disclosure` (the model chooses to read more) against `conditional-loading` (the harness adds text when a rule matches) |

All seven are answered.

## T11: Z39.19 §11.2.2 review

- **Unmarked synonyms**: none. Every word in the stage-2 harvest's seven synonym sets is
  a preferred label or an alias of one entry, which T2 confirms. "Learnings" moved from
  `memory` to `learning`; "dreaming" and "distillation" are aliases of `consolidation`.
- **Missing facets**: none. Round 2 had no three-way split. The `unsure` notes (12, 4
  and 5) choose between existing values, mostly for surveys and for stores whose sharing
  is unstated. Set C's `arrival` was not asked for by any rater. Its ideas are the
  entries `progressive-disclosure` and `conditional-loading`.
- **Facet changes**: `reach` gained `built-in-scope` after round 1, and round 2 tested it
  with no further change. The ending condition "no facet added, split or merged in the
  last round" holds for round 2.
- **Out-of-date terms**: none. Harvested at prompts `e7d4fb2` (2026-11-26).
- **Term form**: T3 flags only `operations` (stage 1, kept).
- **Area boundary**: five of 60 test items were put outside `context` by most raters:
  tool (`cr10`, `cr16`), control (`cr21`), and `ch28` and `ch30`. Each agrees with
  stage 1's area definitions, so stage 1 needs no change.
- **For a later stage**: (1) context-file loading §13's three postures on authority
  (supreme, subordinate on safety, untrusted data) could be values of a finer `framing`
  facet. (2) The population is small (130), and only 18 held items remain, so a third
  round would extend the draw to `####` sections.

## Ending conditions (scope.md, each stage)

| Condition | Stage 2 |
|---|---|
| T1-T6 clean | yes (only the kept `operations` flag) |
| T7: every item sorted, Unsorted ≤ 7% | yes: round 2, 28 in-area items, no three-way split. The sample is 30, by method v1.1 M3 (5 × 6 values), not 60 |
| T8: J23 on every facet | yes: Fleiss 0.89 / 1.00 / 0.84, pair 0.83 / 1.00 / 0.83 |
| T9: ≥ 80% of labels guessed | yes: 94% and 97% |
| T10 | yes, all seven |
| T11 | yes |
| No facet change in the last round | yes |
| Facet set chosen by Jonathan (process step 4) | **open**: decision card posted 2026-11-26, set A recommended |
