# Round 3: agreement test kit (stage 1)

**In one line**: everything three raters need for round 3 of the prompts taxonomy's
agreement test (process step 8, spec T8, method v1.1 M4-M6), and how to score it.

**In plain words**: three models from three families each sort the same 60 fresh items
using only the definitions, without seeing each other's answers. If they agree often
enough (Fleiss' κ ≥ 0.6 on each question, and the two non-Claude raters κ ≥ 0.6 with each
other), the definitions are clear; where they disagree, the disagreements show what to fix.

Tests facet set A after the round-2 fixes (a separate model call is `second-model` however its prompt is built; starting is not deciding;
[`../round-2/results.md`](../round-2/results.md#fixes-after-scoring-2026-11-26)). Use the same three
models as round 1 (Claude Opus 5.5, GPT-6.2-Astra, Gemini 4 Carbon High) so the change
shows the files, not the raters. 60 items, above method
v1.1 M3's floor of 40 (5 × 8 area values).

## Files

- [`items.csv`](./items.csv): the 60 round-3 items (`g01`-`g67` less eight meta sections, newly drawn) from
  [`../../samples.md`](../../samples.md): heading, opening text (`gist`), file.
- `prompt-claude.md`, `prompt-openai.md`, `prompt-gemini.md`: the same prompt with values
  and definitions in a different order for each rater (spec T8). Each is self-contained:
  send the whole file as the only input. Regenerate with `python3 make_prompts.py`.
- `answers/<rater>.csv`: each rater's answers, header `id,area,decider,moment,note`.
  `answers/<rater>-raw.md`: the full reply, and the run details (below).

## Running the raters (on omarchy, through each vendor's CLI)

Jonathan's ChatGPT and Google AI plans have no API credit, so the OpenAI and Gemini
raters run through their own CLIs, headless, as `strata-models/scripts/evals/record_cloud.py`
already does (`codex exec`, `agy -p`). Claude runs the same way through `claude -p`.

For each rater (method v1.1 M6):

1. Make a new empty directory outside any repo (`mktemp -d`), copy only its
   `prompt-<rater>.md` there, and run from it. No repo checkout, no other files.
2. Read-only, tools and web search off where the CLI allows it; no MCP servers.
3. Model: the strongest the plan offers, at high reasoning effort:
   - `claude`: Claude Code, Opus (`claude -p --model opus`, no tools allowed).
   - `openai`: `codex exec` with the strongest GPT model on the ChatGPT plan,
     `--sandbox read-only`, reasoning effort high.
   - `gemini`: Antigravity `agy -p` with the strongest Gemini **Pro** model the plan
     offers (not Flash).
4. The whole prompt file as the only user input. Save the reply as
   `answers/<rater>-raw.md`, with at the top: CLI and version, model id, effort, date
   and time, tokens if shown. The CLI's own system prompt cannot be removed; note that.
5. Save the CSV block as `answers/<rater>.csv`. Check: 60 rows, the ids in `items.csv`, only the
   listed values. A value outside a list is kept in the raw file and left blank in the CSV.
6. Never route the CLIs' sign-ins through a proxy (Google disables accounts for it).
   Stop if a plan's usage limit is near (record_cloud.py's 10% rule).

## Scoring

From the repo root:

```
python3 tools/kappa.py domains/prompts/rounds/round-3/answers/{claude,openai,gemini}.csv
python3 tools/kappa.py domains/prompts/rounds/round-3/answers/{openai,gemini}.csv
```

The first prints Fleiss' κ, each pair's Cohen's κ, and the majority value or SPLIT per
disagreement; the second is the non-author pair (M4). Paste both into `results.md` with
the three model names. Do not edit `facets.md` or `glossary.md` until all three have
answered and been scored.
