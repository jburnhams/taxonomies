# Rounds 1-2: competency questions (T10) and heuristic review (T11)

**In one line**: all twelve competency questions are answered from `facets.md` and
`glossary.md`; the review found one unlinked near-synonym and one value no round item
took (`owner-decision`), and no missing facet.

Checked 2026-11-26 by Claude against the files as committed with this page, using the
majority labels of rounds 1 and 2 as examples. `check` examples will be re-read after
round 3.

## T10: competency questions from [`../../scope.md`](../../scope.md)

| # | Question (short) | Answered by | Answer, with round examples |
|---|---|---|---|
| 1 | Which rules can a script check, which need judgement? | facet `check` | `script`: what `check_domain.py`, `kappa.py` and `sample.py` check (`r03` T6, `r05` T8, `r08` T1, `h10` Kind); `judgement`: the rest (`r02`, `r09`, `h01`) |
| 2 | Which are Jonathan's to settle? | `owner-decision`, `owner`, `veto` | starting a domain (step 0), choosing facets (step 4), open questions such as J18 (`t05`, `t07`); none in the round items (see T11) |
| 3 | Which apply while writing a definition, which while choosing a label? | facet `part`: `meaning`, `naming` | `meaning`: `r02`, `r09`, `r15`, `h01`; `naming`: `r12`, `r17`, `r25`, `h09` |
| 4 | Which apply before any word is collected? | facet `stage`: `framing` | `r06`, `r13`, `r26`, `h03`, `s06` |
| 5 | Which govern changes after adoption? | `stage` `governing` with `part` `change` | `r14` G4, `r21` G1, `r22` G5, `h06` step 12 |
| 6 | What does a domain folder hold? | `taxonomy`, `glossary`, `changelog`, `round` | scope, facets, glossary, changelog, rounds; `map.md` once a neighbour exists (`neighbours` scope note) |
| 7 | Term, label, identifier? | `term`, `label`, `identifier` | a term is the concept's entry; a label names it and may change; the identifier never changes (N6) |
| 8 | Facet, facet value, alias? | `facet`, `facet-value`, `alias` | a facet is a sorting question; a value is a term that answers it; an alias is another word for one term |
| 9 | What is a round? | `round`, `rater`, `agreement-test` | raters sort a test sample using only the files; the files are fixed from the disagreements; kept in `rounds/round-N/` |
| 10 | What does kappa measure, and the target? | `kappa` | agreement beyond chance; Cohen's for two, Fleiss' for three; at least 0.6 per facet (J5, J23) |
| 11 | When is a taxonomy adopted? | `adoption`, `ending-condition` | when the ending conditions in `scope.md` hold; an agent approves, Jonathan can veto |
| 12 | Near miss against scope note? | `near-miss`, `scope-note` | a scope note says what the term includes and excludes; a near miss names one thing it is easily taken for, and why not |

## T11: Z39.19 §11.2.2 evaluation questions

- **Unmarked synonyms**: one near-synonym. `mechanical-check` (T1-T6 as a happening) and
  the value `script` overlap; they are different kinds (a test, and a check that a test
  is one of), so both stay, now linked by Related. "boundary" stays an alias of
  `neighbours`.
- **Missing facets**: none. No item went to Unsorted in either round.
- **Empty value**: `owner-decision` was the majority label of no round item (it was used
  in the bare-facet test, `t05` and `t07`). T6 asks whether a concept or axis is wrong.
  Read: the method reserves few things for the owner (step 0, step 4, open decisions,
  the shared kernel), and the draw happened to put them in the build and bare-test sets.
  Kept: it answers competency question 2, and an agent needs to know when to stop and
  ask. Re-check at the next review.
- **Out-of-date terms**: none; the glossary is one day old.
- **Consistent term form**: singular, lower case; `neighbours` is a mass noun (label
  choice 6). T3 and T4 clean apart from the two listed plural flags.
- **Definitions and scope notes**: the round-1 and round-2 fixes were all to `check`;
  every other value's scope note was used unchanged by three raters.
