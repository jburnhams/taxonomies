# Stage 3, round 1: agreement test kit (control area)

**In one line**: everything three raters need for round 1 of stage 3 (the control area)
of the prompts taxonomy, the name test for the new and revised labels, and how to score
both.

**In plain words**: three models from three families each sort the same 30 fresh
sections using only the definitions, without seeing each other's answers. They first say
whether a section is about the control area at all, then answer the two stage-3
questions. The stage-3 scores count only the sections most raters put in the area.
Separately, two readers guess what 33 labels mean from the label alone: the new control
words, and the seven earlier words this stage changed (the retest in method v1.1 M8).

Tests facet set A for stage 3 (`target`, `response`; [`../../../facets.md`](../../../facets.md),
"Stage 3"), while Jonathan's choice of set is open. Same three models as stage 2 (Claude
Opus 5.5, GPT-6.2-Astra, Gemini 4 Carbon High). 30 items: method v1.1 M3's floor is 30
(J7), and 5 × 6 `response` values = 30.

## Files

- [`items.csv`](./items.csv): the 30 round-1 items `kr01`-`kr30` from
  [`../../samples.md`](../../samples.md): heading, opening text (`gist`), file.
- `prompt-claude.md`, `prompt-openai.md`, `prompt-gemini.md`: the same prompt with values,
  areas and definitions in a different order for each rater (spec T8, seeds 51-53). Each
  is self-contained: send the whole file as the only input. Regenerate with
  `python3 make_prompts.py`.
- `answers/<rater>.csv`: each rater's answers, header `id,in_area,target,response,note`.
  `answers/<rater>-raw.md`: the full reply and the run details.
- [`name-test/prompt.md`](./name-test/prompt.md): the T9 name test, 33 labels in
  alphabetical order. Replies go in `name-test/guesses-openai.md` and
  `name-test/guesses-gemini.md` (two non-Claude readers, as in stage 2).

## Running the raters (on omarchy, through each vendor's CLI)

Exactly as stage 2 ([`../../../stage-2/rounds/round-1/README.md`](../../../stage-2/rounds/round-1/README.md),
method v1.1 M6): a new empty directory per rater holding only its prompt, read-only, tools
and web off where the CLI allows, the whole prompt as the only input, the strongest model
at high effort (`claude -p --model opus`; `codex exec --sandbox read-only` with
GPT-6.2-Astra, effort high; `agy -p --sandbox` with Gemini 4 Carbon High, not Flash).
Record CLI, version, model, effort, date and tokens at the top of each raw file. Check 30
rows with the ids in `items.csv` and only the listed values. The name test runs the same
way for openai and gemini. Never route sign-ins through a proxy.

## Scoring

From the repo root:

```
R=domains/prompts/stage-3/rounds/round-1/answers
# in_area across all items (re-tests stage 1's control boundary)
python3 tools/kappa.py $R/{claude,openai,gemini}.csv --facets in_area
# stage-3 facets on the items most raters put in the area
python3 tools/kappa.py $R/{claude,openai,gemini}.csv --where in_area=yes
python3 tools/kappa.py $R/{openai,gemini}.csv --where in_area=yes --ref $R/claude.csv
```

Pass (J23): Fleiss' κ ≥ 0.6 on `target` and `response`, and the openai-gemini pair
κ ≥ 0.6 on each. `in_area` is reported, not a pass condition. Name test: a label passes
when both readers' guesses fit its definition; a miss gets a relabel or a near miss, as
in stage 2.
