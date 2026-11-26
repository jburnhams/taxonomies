# Stage 2, round 1: agreement test kit (context area)

**In one line**: everything three raters need for round 1 of stage 2 (the context area)
of the prompts taxonomy, and how to score it.

**In plain words**: three models from three families each sort the same 30 fresh
sections using only the definitions, without seeing each other's answers. They first say
whether a section is about the context area at all, then answer the three stage-2
questions. The stage-2 scores count only the sections most raters put in the area.

Tests facet set A for stage 2 (`operation`, `content`, `reach`; [`../../../facets.md`](../../../facets.md),
"Stage 2"), while Jonathan's choice of set is open. It uses the same three models as
stage 1 (Claude Opus 5.5, GPT-6.2-Astra, Gemini 4 Carbon High). 30 items: method v1.1
M3's floor is 30 (J7) and 5 × 5 `reach` values = 25.

## Files

- [`items.csv`](./items.csv): the 30 round-1 items `cr01`-`cr30` from
  [`../../samples.md`](../../samples.md): heading, opening text (`gist`), file.
- `prompt-claude.md`, `prompt-openai.md`, `prompt-gemini.md`: the same prompt with values,
  areas and definitions in a different order for each rater (spec T8). Each is
  self-contained: send the whole file as the only input. Regenerate with
  `python3 make_prompts.py`.
- `answers/<rater>.csv`: each rater's answers, header
  `id,in_area,operation,content,reach,note`. `answers/<rater>-raw.md`: the full reply and
  the run details.

## Running the raters (on omarchy, through each vendor's CLI)

Exactly as stage 1 round 3 ([`../../../rounds/round-3/README.md`](../../../rounds/round-3/README.md),
method v1.1 M6): a new empty directory per rater holding only its prompt, read-only, tools
and web off where the CLI allows, the whole prompt as the only input, the strongest model
at high effort (`claude -p --model opus`; `codex exec --sandbox read-only` with
GPT-6.2-Astra, effort high; `agy -p --sandbox` with Gemini 4 Carbon High, not Flash).
Record CLI, version, model, effort, date and tokens at the top of each raw file. Check 30
rows with the ids in `items.csv` and only the listed values. Never route sign-ins
through a proxy.

## Scoring

From the repo root:

```
R=domains/prompts/stage-2/rounds/round-1/answers
# in_area across all items (re-tests stage 1's context boundary)
python3 tools/kappa.py $R/{claude,openai,gemini}.csv --facets in_area
# stage-2 facets on the items most raters put in the area
python3 tools/kappa.py $R/{claude,openai,gemini}.csv --where in_area=yes
python3 tools/kappa.py $R/{openai,gemini}.csv --where in_area=yes --ref $R/claude.csv
```

Pass (J23): Fleiss' κ ≥ 0.6 on `operation`, `content` and `reach`, and the openai-gemini
pair κ ≥ 0.6 on each. `in_area` is reported, not a pass condition: items most raters put
outside the area are listed and left to stage 1.
