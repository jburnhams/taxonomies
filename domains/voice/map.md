# Voice taxonomy: map to other contexts

**In one line**: which voice terms are the same as, or only look like, terms of the
`prompts` context, so a word keeps one meaning in each context (spec C1, C3).

**In plain words**: voice-research uses some agent-design ideas (a language model, an
eval, a model that judges). Where the idea is the same, the voice glossary uses the
`prompts` word and says so here; where the same word means something else, it says
that too. `closeMatch` is the default (C3); `exactMatch` only where the definitions are
the same concept.

## Links (spec §5)

- `eval` exactMatch `prompts:eval`: same definition, with "agent or model" cut to "model"
  because voice-research measures models only.
- `benchmark` exactMatch `prompts:benchmark`: as `eval`.
- `language-model` closeMatch `prompts:language-model`: same kind of model; `prompts`
  defines it as what "a harness calls to produce text and tool calls", narrower than the
  use here (writing recording prompts, drafting messages, judging). Labelled "model" in
  `prompts`, "language model" here, because "model" alone is ambiguous in voice-research.
- `llm-judge` broadMatch `prompts:second-model`: a `prompts` second model is any separate
  model call that has the final say (classifiers, monitors, judges); an LLM judge is the
  judging kind only. "LLM judge" is an alias of `second-model` in `prompts`, which is right
  for that context.
- `recording-session` relatedMatch `prompts:session`: different concepts that share the
  word "session"; voice uses "recording session" so the bare word is not needed.
- `style-instruction` relatedMatch `prompts:model-prompt`: both are text given to a
  model, but a style instruction goes to a text-to-speech model beside the text it
  speaks, and says only how to say it (added 2026-11-28).
- Assistant **memory** (KnowAct, voice-research `5af9937`): use `prompts:memory`. The
  voice glossary has no entry of its own, since the concept is the agent-design one.
- `retrieval` broadMatch `prompts:retrieval`: `prompts` counts every way kept items are
  brought into the prompt (pasted in, index read, search, trigger match); voice's
  `retrieval` is the search kind only, with long context as its near miss. Answered
  2026-11-28 ([#21](https://github.com/jburnhams/taxonomies/issues/21)).
- (no voice entry) "model prompt" closeMatch `prompts:model-prompt` (labelled "prompt"
  there): the text sent to a language model on one request. Voice keeps "model prompt",
  an alias in `prompts`, because "prompt" alone also means a recording prompt here.
  Answered 2026-11-28 ([#20](https://github.com/jburnhams/taxonomies/issues/20)).
- (no voice entry) "transcript": the words of a take here; a run's record of turns in
  `prompts` (`prompts:transcript`). Not mapped: different concepts. A later stage may
  add a voice entry labelled to avoid the collision.

## Asked of `prompts` (requests, design/growth.md)

- **clarify `prompts:context-window`** ("prompt"): `term.py lookup prompts "prompt"` gives
  `context-window`, defined as a limit on tokens, with "prompt" as an alias. Voice-research
  needs a word for *the text sent to a language model on one request* (a style profile,
  few-shot examples and retrieved messages go "in the prompt"). Is that `context-window`,
  or does `prompts` want a separate entry? Until answered, voice docs write "model prompt".
- **new `prompts: retrieval`**: no term in `prompts`, though the prompts repo uses
  "retriev-" about 400 times; voice has `retrieval` (stage 1 candidate) and would map to it.

Filed 2026-11-27 as [#20](https://github.com/jburnhams/taxonomies/issues/20) (clarify "prompt") and [#21](https://github.com/jburnhams/taxonomies/issues/21) (new `retrieval`); both answered 2026-11-28 (links above, and `domains/prompts/requests.md`).
