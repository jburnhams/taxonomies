# Name test (T9), round 1

**In one line**: a fresh reader got 41 of 53 labels right, 8 partly and 4 wrong; two of the
wrong ones were renamed, two kept and flagged. WordNet gives 13 labels six or more noun senses.

**Guess the name.** A fresh Claude session read only [`prompt.md`](./prompt.md) (the 53
preferred labels and one line on what the repo is about) and guessed each meaning:
[`guesses-claude.md`](./guesses-claude.md), 2026-11-26. Graded against `glossary.md` by
the building agent (Claude), so the grading is one model's call:

| Result | Labels |
|---|---|
| **Wrong** (4) | `one question` (guessed "ask at most one clarifying question"), `one finding` (guessed "report one finding per review"), `treatment` (guessed "how one element is styled"; the repo means how much decoration a whole screen gets), `wave` (guessed "a batch of work") |
| **Partly** (8) | `any mode` (also read as light/dark), `code` (read as "the code layer"; it is a detection method), `Experience` (immersive or brand, rather than "inside the work"), `moment` (any memorable detail, not a rare earned one), `render` (screenshot only; the repo includes a keyboard pass), `silhouette test` (shape alone, not section order against competitors), `stack layer` (Tailwind / shadcn / React rather than the five decision levels), `surface` (gave both a panel layer, which is the chosen sense, and "product surface") |
| **Right** (41) | the rest |

What was done:

- **Renamed** `one question` → **`screen question`** and `one finding` → **`screen finding`**
  (IDs kept, old labels as aliases), because both guesses were wrong in a way that
  would mislead an agent, and "the one ..." is a phrase, not a name. Listed for
  Jonathan's veto in the glossary.
- **Kept** `treatment` and `wave`: both are the repo's established words (9 and 31 uses)
  and come from its sources (Claude `artifact-design`; taste-skill's dated waves). N6 keeps an
  established word unless it misleads; a reader of the docs meets them with their
  definition next to them. Flagged for Jonathan; T12 will show if they drift.
- Partly-right labels: no change. Facet values (`code`, `render`, `any mode`) are read
  beside their facet's question, which the bare-label test removes.

**WordNet** (Princeton WordNet 3.0, the copy in `nltk_data`, read 2026-11-26): senses per
part of speech for each label; multi-word labels are mostly absent. "Risk" is this
page's heuristic (high: 6 or more noun senses; medium: 4 or more senses in all), not
Miller's.

| Label | WordNet 3.0 senses (noun/verb/adj/adv) | Risk |
|---|---|---|
| any mode | not in WordNet | — |
| brief | noun 2, verb 1, adj 3 | medium |
| character | noun 9, verb 1 | high |
| code | noun 3, verb 2 | medium |
| colour | noun 8, verb 6, adj 1 | high |
| competitor test | not in WordNet | — |
| component | noun 3 | low |
| copy | noun 4, verb 4 | medium |
| dark mode | not in WordNet | — |
| defect | noun 4, verb 1 | medium |
| direction | noun 9 | high |
| drift | noun 7, verb 10 | high |
| editorial | noun 1, adj 2 | low |
| Experience | noun 3, verb 5 | medium |
| ground | noun 11, verb 12 | high |
| imagery | noun 1 | low |
| interaction | noun 2 | low |
| judgement | noun 7 | high |
| layout | noun 2 | low |
| mode | noun 6 | high |
| model signature | not in WordNet | — |
| moment | noun 6 | high |
| mood word | not in WordNet | — |
| motion | noun 7, verb 1 | high |
| one finding | not in WordNet | — |
| one question | not in WordNet | — |
| Operate | verb 7 | medium |
| palette role | not in WordNet | — |
| Persuade | verb 2 | low |
| quality floor | not in WordNet | — |
| Read | noun 1, verb 11 | medium |
| reference sentence | not in WordNet | — |
| render | noun 1, verb 13 | medium |
| screen | noun 9, verb 7 | high |
| signature move | not in WordNet | — |
| silhouette test | not in WordNet | — |
| slop | noun 5, verb 4 | medium |
| slop-lint | not in WordNet | — |
| stack layer | not in WordNet | — |
| stock whimsy | not in WordNet | — |
| subject | noun 8, verb 4, adj 3 | high |
| subject inventory | not in WordNet | — |
| surface | noun 6, verb 3, adj 1 | high |
| swap test | not in WordNet | — |
| tell | noun 1, verb 8 | medium |
| tell registry | not in WordNet | — |
| theme | noun 5, verb 1 | medium |
| token | noun 4, adj 1 | medium |
| token contract | not in WordNet | — |
| treatment | noun 4 | medium |
| typography | noun 2 | low |
| utilitarian | noun 1, adj 2 | low |
| wave | noun 9, verb 5 | high |

High-risk labels that are also everyday words in UI writing (`screen`, `surface`, `mode`,
`direction`, `ground`, `character`, `motion`, `colour`) are the ones whose scope notes
name the excluded sense; `surface` and `mode` already exclude theirs (screen sense,
dark mode).
