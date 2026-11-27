# Voice stage 1, round 1: agreement test kit

**In one line**: everything three raters need for round 1 of the voice taxonomy's stage 1,
the name test for its 62 labels, and how to score both.

**In plain words**: three models from three families each sort the same 40 fresh items
(sources and findings from voice-research) using only the definitions, without seeing each
other's answers. Separately, two readers guess what each label means from the label alone.

Tests facet set A (`area`, `modality`, `trait`; [`../../facets.md`](../../facets.md)) while
Jonathan's choice of set is open. Same three models as `prompts` stage 3 (Claude Opus 5.5,
GPT-6.2-Astra, Gemini 4 Carbon High). 40 items: method v1.1 M3 asks at least 5 per value
of the largest facet (`area`, 7 values: 35).

## Files

- [`items.csv`](./items.csv): the 40 round-1 items `r01`-`r40` from
  [`../../samples.md`](../../samples.md): item text and `from`.
- `prompt-claude.md`, `prompt-openai.md`, `prompt-gemini.md`: the same prompt with values
  and definitions in a different order for each rater (spec T8, seeds 61-63). Each is
  self-contained: send the whole file as the only input. Regenerate with
  `python3 make_prompts.py`.
- `answers/<rater>.csv`: each rater's answers, header `id,area,modality,trait,note`.
  `answers/<rater>-raw.md`: the full reply and the run details.
- [`name-test/prompt.md`](./name-test/prompt.md): the T9 name test, 62 labels in
  alphabetical order. Replies go in `name-test/guesses-openai.md` and
  `name-test/guesses-gemini.md` (two non-Claude readers, as in `prompts`).

## Running the raters (on omarchy, through each vendor's CLI)

As `prompts` stage 3 ([`../../../prompts/stage-3/rounds/round-1/README.md`](../../../prompts/stage-3/rounds/round-1/README.md),
method v1.1 M6): a new empty directory per rater holding only its prompt, read-only, tools
and web off where the CLI allows, the whole prompt as the only input, the strongest model
at high effort (`claude -p --model opus`; `codex exec --sandbox read-only` with
GPT-6.2-Astra, effort high; `agy -p --sandbox` with Gemini 4 Carbon High, not Flash).
Record CLI, version, model, effort, date and tokens at the top of each raw file. Check 40
rows with the ids in `items.csv` and only the listed values. The name test runs the same
way for openai and gemini. Never route sign-ins through a proxy.

## Scoring

From the repo root:

```
R=domains/voice/rounds/round-1/answers
python3 tools/kappa.py $R/{claude,openai,gemini}.csv
python3 tools/kappa.py $R/{openai,gemini}.csv --ref $R/claude.csv
```

Pass (J23): Fleiss' κ ≥ 0.6 on `area`, `modality` and `trait`, and the openai-gemini
pair κ ≥ 0.6 on each. Name test: a label passes when both readers' guesses fit its
definition; at least 80% must pass (T9).
