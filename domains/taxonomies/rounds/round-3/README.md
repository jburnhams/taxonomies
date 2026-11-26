# Round 3: `check` only, on used items (indicative)

**In one line**: the three raters sort 73 items on one question, `check`, after it was
redefined as a closed list of what the repo's scripts check today.

**In plain words**: round 2 failed on `check` (Fleiss' κ 0.55) because "a program could
check it" was read two ways: Gemini read it as "a script does", the others as "one
could". `script` now means only what a stored script checks, and the definition lists
them. Every fresh item has been used, so this round reuses the 73 items of rounds 1 and 2
(ids removed). It is **indicative**, not a pass under T8: the raters have seen these
items before in other sessions, and the fix was written after reading round 2's
disagreements. Whether that is enough to adopt is Jonathan's decision.

## Files

- [`items.csv`](./items.csv): `r01`-`r30`, `h01`-`h18`, `s01`-`s25`, own ids removed.
- `prompt-<rater>.md`: one question, values and definitions shuffled per rater.
  Regenerate with `python3 make_prompts.py`.
- `answers/<rater>.csv` (header `id,check,note`, 73 rows) and `answers/<rater>-raw.md`.

## Running and scoring

As [`../round-1/README.md`](../round-1/README.md), then:

```
python3 tools/kappa.py domains/taxonomies/rounds/round-3/answers/{claude,openai,gemini}.csv
python3 tools/kappa.py domains/taxonomies/rounds/round-3/answers/{openai,gemini}.csv
```
