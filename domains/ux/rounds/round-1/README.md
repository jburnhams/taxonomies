# Round 1: agreement test kit

**In one line**: everything a second rater needs for round 1 of the ux taxonomy's
agreement test (process step 8, spec T8), and how to score it.

**In plain words**: two models from different families each sort the same 30 fresh
items using only the definitions, without seeing each other's answers. Where they agree
often enough (κ ≥ 0.6 on each question), the definitions are clear; where they disagree,
the disagreements show which definitions to fix.

Files:

- [`items.csv`](./items.csv): the 30 round-1 test items from [`../../samples.md`](../../samples.md), ids `r..` and `h..`.
- [`prompt-claude.md`](./prompt-claude.md): the prompt rater A (Claude) answered.
- [`prompt-second.md`](./prompt-second.md): the same prompt with values shuffled
  differently, for the second rater (an OpenAI or Gemini model). Self-contained: paste
  the whole file as the prompt.
- `answers/claude.csv`: rater A's answers (a fresh Claude session that read only its prompt).
- `answers/<family>.csv`: the second rater's answers, for example `answers/openai.csv`
  or `answers/gemini.csv`. Header: `id,aspect,brief_override,detection,mode,note`.

## Running the second rater

1. Send `prompt-second.md` as the whole prompt to one OpenAI or Gemini model, at low temperature if the API allows it,
   with nothing else in the context. Record the model name and date.
2. Save the CSV it returns as `answers/<family>.csv`. Check it has 30 rows and only the
   listed values. If a value is outside the list, record the raw value and pick nothing for it.
3. Score: `python3 tools/kappa.py domains/ux/rounds/round-1/answers/claude.csv domains/ux/rounds/round-1/answers/<family>.csv`
   from the repo root. Paste the table and the disagreement list into `results.md` here,
   with both model names.
4. Do not edit `facets.md` or `glossary.md` before scoring: the round must test the
   files as they were when rater A answered (commit noted in `results.md`).
