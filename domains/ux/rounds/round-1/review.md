# Round 1: competency questions (T10) and heuristic review (T11)

**In one line**: all twelve competency questions are answered from `facets.md` and
`glossary.md`; the Z39.19 review found one misplaced alias and no missing facet.

Checked 2026-11-26 by Claude against the files as committed with this page.

## T10: competency questions from [`../../scope.md`](../../scope.md)

| # | Question (short) | Answered by | Answer, with round-1 examples |
|---|---|---|---|
| 1 | Which tells can slop-lint find in the code, which need the render or the brief? | facet `detection` | `code` items (most: `r01`, `r10`, `h14`), `render` (`r16`, `r20`, `r21`), `judgement` (`r11`, `r12`, `r24`, `r29`) |
| 2 | Which count only on Operate, which only on Persuade? | facet `mode` | `operate`: `r01`-`r05`, `r12`; `persuade`: `r28`; the rest `any-mode` |
| 3 | Slop or defect? | facet `brief-override`, entries `slop`, `defect` | e.g. `r22` (inverted dark mode) is a defect, after the round-1 scope note |
| 4 | Which part of the interface? | facet `aspect` | eight values; `r20` (blank page) is the one item in **Unsorted** |
| 5 | What does "surface" mean, and the other sense? | `surface`, `screen` | a tonal layer; the page being built is a `screen` |
| 6 | Tell, slop, defect? | `tell`, `slop`, `defect` | a tell is one pattern; slop the property of a look built from them; a defect fails a user whatever the brief says |
| 7 | Mood, vibe, direction, reference sentence? | `mood-word` (aliases mood, vibe), `direction`, `reference-sentence` | a mood word is input, a reference sentence fixes a point, the direction is the chosen idea |
| 8 | What do mode and treatment each decide? | `mode`, `treatment` | mode: what the person is there to do; treatment: how much decoration |
| 9 | Which wave, and what is a wave? | `wave`, `tell-registry` | the registry dates each tell by wave; a wave is a period of spread |
| 10 | Token contract, and where it lives? | `token-contract` | DESIGN.md and the theme; a literal value at a call site breaks it |
| 11 | "The one question" and "the one finding"? | `screen-question`, `screen-finding` (ids `one-question`, `one-finding`) | the question an Operate screen answers; today's fact that most needs attention |
| 12 | Signature move against a model's signature? | `signature-move`, `model-signature` | chosen from the subject, against habits that identify the generator |

Question 1 is answered per item, so the taxonomy answers it for an item once that item is classified;
the full list of tells by detection needs every registry row classified, which is
maintenance work (step 12), not a gap in the facets.

## T11: Z39.19 §11.2.2 evaluation questions

- **Unmarked synonyms**: one found. "fingerprint" was an alias of `tell`, but the repo uses
  it only for generator fingerprints (§3g), so it moved to `model-signature`. "generic"
  and "median" are adjectives or descriptions of slop, not labels; left out.
- **Missing facets**: none. One item in Unsorted (`r20`); whole-page failures may need an
  aspect value if more arrive (S6).
- **Out-of-date terms**: none; the glossary is one day old. The registry's own dating
  (waves) is the repo's currency mechanism.
- **Consistent term form**: singular, lower case, except the four mode names, which the
  repo always capitalises (Persuade, Operate, Read, Experience), kept as proper names.
  T3 and T4 clean (`tools/check_domain.py`).
- **Definitions and scope notes**: all genus-differentia (T4); nine scope notes widened
  after round 1 where raters split or hesitated.
