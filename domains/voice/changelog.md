# Voice taxonomy: changelog

Every change as a named operation (spec G4), newest day first. The approving agent is
named on each line (G1); Jonathan can reverse any of them.

## 2026-11-28

- **add** `assisted-message`, `preference-data`, `reward` and `style-instruction` as `candidate`, after
  the research update at voice-research `5af9937` (39 new sources). **Redefine** (clarified, non-breaking)
  the near misses of `fine-tuning` (now points to `preference-data`) and `real-data` (assisted messages
  are real data, tagged). **Map** `style-instruction` relatedMatch `prompts:model-prompt`; assistant
  memory uses `prompts:memory`. **Record** the update check in `harvest.md`: counts before and after,
  homonym 8 ("verifier"), no alias drift in the new prose, and every new source sorted by the three
  facets with none Unsorted. Approved by: Claude (G1), after Jonathan said "See updated research".

- **map** `retrieval` broadMatch `prompts:retrieval` and "model prompt" closeMatch
  `prompts:model-prompt`, after `prompts` answered requests #20 and #21. Voice docs keep
  "model prompt". Approved by: Claude (G1).
- **record** round 2 (run on omarchy, `9debcd7`): Fleiss' κ area 0.87, modality 0.96,
  trait 0.89; openai-gemini 0.91, 0.94, 0.87; pass (J23). `h07` and `h13` (LLM-judge
  biases) to Unsorted, answered by a new `whole-voice` near miss. Name test: 2 of 4 retested
  labels pass with both readers. **approve** `style`; `coaching` stays `candidate` (both
  readers read it as feedback on takes; first scored a pass, corrected after review on #31). **redefine**
  `whole-voice` (judge-bias near miss) and `demonstration` (near miss: not a walkthrough of
  the process); both stay `candidate`. **fix** `sample.py`: no sentence break after "e.g."
  (it had cut `h36`); the stored draw is unchanged. Approved by: Claude (G1).
- **add** the round-2 kit in `rounds/round-2/`: the 40 held items `h01`-`h40`, three shuffled
  prompts (seeds 71-73) with the `whole-voice` rule as redefined, and a name test of the 4 changed labels.
  Proposed by: Claude, after Jonathan said "yes please" to round 2 and the rename pass.

## 2026-11-27

- **adopt** stage 1 (process step 10): `scope.md` status `in use`; 58 entries `approved`,
  4 left `candidate` (changed below) for round 2. T10: all 13 competency questions are
  answered (`rounds/round-1/review.md`). Approved by: Claude (G1). Jonathan can veto.
- **rename** `demonstration` → "coaching demo" (ID kept, "demonstration" kept as an
  alias): both name-test readers read it as an example shown to a model. **Redefine**
  `coaching` (excludes feedback after a take), `style` (near miss for the habit sense) and
  `whole-voice` (a part named through a metric or model counts as named; stored features
  default to `expression`). Approved by: Claude (G1).
- **record** round 1 (run on omarchy, `f05f2e0`): Fleiss' κ area 0.96, modality 1.00,
  trait 0.81; openai-gemini 0.97, 1.00, 0.77; pass (J23). `r20` goes to Unsorted (three
  different values). Name test: 59 of 62 labels (95%), each reader 60 of 62.
- **decide** facet set A (`area`, `modality`, `trait`), by Jonathan on the decision card,
  process step 4.
- **add** the round-1 kit in `rounds/round-1/` (40 items `r01`-`r40`, three shuffled
  prompts, name test of 62 labels). Proposed by: Claude.
- **add** `map.md` (requests filed as issues #20, #21): `eval`, `benchmark` exactMatch `prompts`; `language-model` closeMatch;
  `llm-judge` broadMatch `prompts:second-model`; `recording-session` relatedMatch
  `prompts:session`; two requests to `prompts` (clarify "prompt", new `retrieval`).
  Proposed by: Claude, after Jonathan asked that voice align with `prompts`.
- **add** 15 `candidate` values of proposed facet set A (`area`, `modality`, `trait`)
  and 47 `candidate` kernel terms; T1-T6 clean apart from the listed `operations` flag.
  Approved by: Claude (G1); label choices listed in `glossary.md` for Jonathan's veto.
- **add** `facets.md`: sets A, B, C and a bare-facet test on `t01`-`t12` (four
  hesitations, four rule changes before the glossary). Facet choice is Jonathan's
  (process step 4).
- **add** the domain, `draft`: `scope.md` (staged under M1: 329 items, over 300),
  `sample.py`, `items-all.csv` and `samples.md` (152 items drawn at voice-research
  `d02cddc`, seed 20261127), `harvest.md`. Item excerpts are public here by Jonathan's
  choice (2026-11-27), though voice-research is private. Proposed by: Claude, at
  Jonathan's request "create a new taxonomy for the voice-research repo".
