# Round 2: agreement test kit, and the name test

**In one line**: everything three raters need for round 2 of the taxonomies taxonomy's
agreement test, with the items' own ids removed, plus the name test (T9).

**In plain words**: round 1 passed, but `part` and `stage` were unanimous, which may mean
the items were easy rather than the definitions sharp: each item began with its rule id
(`spec N6`), and the definitions name the id ranges (`naming` covers N1-N8). Round 2
removes each item's own id, so raters have to read the text. It also meets method v1.1
M3, which round 1 did not: at least 5 items per value of the largest facet (`part`, 7
values), so at least 35.

Tests the files after the round-1 fixes to `script`, `judgement` and `owner-decision`
([`../round-1/results.md`](../round-1/results.md#fixes-after-scoring-2026-11-26)). Same three
models as round 1.

## Files

- [`items.csv`](./items.csv): 43 items, the 18 held items `h01`-`h18` and the 25 top-up
  items `s01`-`s25` ([`../../samples.md`](../../samples.md)), with the item's own id taken
  out and a `kind` column added. `from` is the file only.
- `prompt-claude.md`, `prompt-openai.md`, `prompt-gemini.md`: as in round 1, values and
  definitions shuffled per rater. Regenerate with `python3 make_prompts.py`.
- `answers/<rater>.csv` (header `id,part,stage,check,note`, 43 rows) and
  `answers/<rater>-raw.md`.
- [`name-test/prompt.md`](./name-test/prompt.md): the 14 value labels with no
  definitions (T9). Send it to each of the three CLIs in a fresh session, the same way,
  and save each reply as `name-test/guesses-<rater>.md`. Run it **before or apart from**
  the rating prompts, never in the same session.

## Running and scoring

As [`../round-1/README.md`](../round-1/README.md): empty temp dir per rater with only its
prompt, read-only, no tools, strongest model at high effort, no proxy. Then:

```
python3 tools/kappa.py domains/taxonomies/rounds/round-2/answers/{claude,openai,gemini}.csv
python3 tools/kappa.py domains/taxonomies/rounds/round-2/answers/{openai,gemini}.csv
```

into `results.md`. Do not edit `facets.md` or `glossary.md` until all three are scored.
