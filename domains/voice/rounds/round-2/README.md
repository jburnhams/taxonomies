# Voice stage 1, round 2: agreement test kit

**In one line**: the three-rater test on the 40 held items `h01`-`h40`, the name test for
the four entries changed after round 1, and how to score both.

**In plain words**: the same three models sort 40 items no one has read yet, using the
definitions as they stand after round 1. Two readers guess the four changed labels. This
retests the four `candidate` entries (`coaching`, `demonstration` "coaching demo",
`style`, `whole-voice`) and checks `modality` on a fresh draw.

Same as [round 1](../round-1/README.md) in every other way. The models are Claude Opus
5.5, GPT-6.2-Astra and Gemini 4 Carbon High, with the same commands and the same rules
for a clean run (method v1.1 M6). The seeds are 71-73. The trait rule in the prompt now
carries the `whole-voice` redefinition.

## Files

- [`items.csv`](./items.csv): `h01`-`h40` from [`../../samples.md`](../../samples.md#held-for-round-2-40).
- `prompt-claude.md`, `prompt-openai.md`, `prompt-gemini.md`: regenerate with `python3 make_prompts.py`.
- `answers/<rater>.csv` (header `id,area,modality,trait,note`) and `answers/<rater>-raw.md`.
- [`name-test/prompt.md`](./name-test/prompt.md): 4 labels, replies in `name-test/guesses-openai.md` and `name-test/guesses-gemini.md`.

## Scoring

```
R=domains/voice/rounds/round-2/answers
python3 tools/kappa.py $R/{claude,openai,gemini}.csv
python3 tools/kappa.py $R/{openai,gemini}.csv --ref $R/claude.csv
```

Pass (J23): Fleiss' κ ≥ 0.6 on every facet, and the openai-gemini pair κ ≥ 0.6 on each.
