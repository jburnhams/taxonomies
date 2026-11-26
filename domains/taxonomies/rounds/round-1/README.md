# Round 1: agreement test kit

**In one line**: everything three raters need for round 1 of the taxonomies taxonomy's
agreement test (process steps 7 and 8, spec T8), and how to score it.

**In plain words**: three models from three families each sort the same 30 fresh items
(rules, steps, fields and decisions of the method) using only the definitions, without
seeing each other's answers. If they agree often enough (Fleiss' κ ≥ 0.6 on each
question, and the two non-Claude raters κ ≥ 0.6 with each other), the definitions are
clear; where they disagree, the disagreements show what to fix.

Tests facet set A (`part`, `stage`, `check`) as written after the bare-facet test
([`../../facets.md`](../../facets.md#bare-facet-test-step-5)). 30 items, the floor of
spec T8 and J7. Claude wrote the facets, so the non-Claude pair is the one that counts
against author bias.

## Files

- [`items.csv`](./items.csv): the 30 round-1 items `r01`-`r30` from
  [`../../samples.md`](../../samples.md#round-1-test-30), not read while building.
- `prompt-claude.md`, `prompt-openai.md`, `prompt-gemini.md`: the same prompt with values
  and definitions in a different order for each rater (spec T8). Each is self-contained:
  send the whole file as the only input. Regenerate with `python3 make_prompts.py`.
- `answers/<rater>.csv`: each rater's answers, header `id,part,stage,check,note`.
  `answers/<rater>-raw.md`: the full reply and the run details (below).

## Running the raters (on omarchy, through each vendor's CLI)

As for the prompts domain's rounds:

1. Make a new empty directory outside any repo (`mktemp -d`), copy only its
   `prompt-<rater>.md` there, and run from it. No repo checkout, no other files.
2. Read-only, tools and web search off where the CLI allows it; no MCP servers.
3. Model: the strongest the plan offers, at high reasoning effort:
   - `claude`: `claude -p --model opus`, no tools allowed.
   - `openai`: `codex exec` with the strongest GPT model on the ChatGPT plan,
     `--sandbox read-only`, reasoning effort high.
   - `gemini`: `agy -p` with the strongest Gemini **Pro** model the plan offers (not Flash).
4. The whole prompt file as the only user input. Save the reply as
   `answers/<rater>-raw.md`, with at the top: CLI and version, model id, effort, date
   and time, tokens if shown.
5. Save the CSV block as `answers/<rater>.csv`. Check: 30 rows, the ids in `items.csv`,
   only the listed values. A value outside a list is kept in the raw file and left blank.
6. Never route the CLIs' sign-ins through a proxy. Stop if a plan's usage limit is near.

## Scoring

From the repo root:

```
python3 tools/kappa.py domains/taxonomies/rounds/round-1/answers/{claude,openai,gemini}.csv
python3 tools/kappa.py domains/taxonomies/rounds/round-1/answers/{openai,gemini}.csv
```

Paste the results into `results.md` with the three model names. Do not edit `facets.md` or
`glossary.md` until all three have answered and been scored.
