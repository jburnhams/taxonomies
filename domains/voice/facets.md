# Voice taxonomy: facets

**In one line**: three sorting questions for every source and finding in
voice-research (which part of the work, which voice, which part of the voice), set A,
chosen by Jonathan 2026-11-27, with the two alternatives he did not take.

**In plain words**: a facet is a question you can ask of any item, with a short list of
answers. With these three you could find, for example, "every finding about evaluating
the expression of the spoken voice" without anyone having written that list. Stage 1 only
needs facets that work across the whole repo; each area gets its own finer questions in a
later stage (proposal M1 in [`design/method-v1.1.md`](../../design/method-v1.1.md)).

**Status**: set A chosen by Jonathan, 2026-11-27 (process step 4). In use from 2026-11-27,
after round 1 passed J23 on every facet ([results](./rounds/round-1/results.md)).

## How these were found

- **Compared unlike items** (step 4, constant comparison): the rule not to put Azure or
  teacher audio in the training pool (`b01`), ECAPA-TDNN as a speaker verifier (`b04`),
  LUAR similarity under prompting (`b26`) and "collect some unscripted speech" (`b11`).
  Each belongs to one part of the work (preparing data, evaluation, generation,
  elicitation); each is about the spoken or the written voice; and each is about one part
  of what makes a voice his: who it sounds like (`b04`, `b26`), how he says something
  (`b11`), or several at once (`b01`).
- **Reused the repo's own questions**: the agendas' areas A-K are the area question; the
  file names (`spoken-*`, `written-*`) are the modality question; the evaluation docs'
  split into identity, expression, accent and naturalness tests
  ([`spoken-evaluation.md`](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-evaluation.md)
  "What we conclude" 2-4; written: authenticity, style, content fidelity) is the trait
  question.
- **Checked against general categories** (OBO Foundry Table 1): `area` is a part of the
  work (a process, but sorted as the part that would change), `modality` is a thing (which
  voice), `trait` is a quality (dependent continuant). No role facet (who decides) held
  across all items: it applies to evaluation and data checks only, which is where a later
  stage can pick it up, reusing `prompts`' `decider` values (`person`, `second-model`,
  `rule`).
- **Structure (spec S2)**: three dimensions, so facets. In the build sample every `trait`
  value occurs in at least three areas, and both voices occur in five of the seven areas.

## Set A (chosen): area, modality, trait

### Area (`area`)

- **Question**: Which part of the work is it about?
- **Principle**: the step of building a personal voice that would have to change to change
  the item.
- **Kind**: thing
- **Values**: `elicitation`, `preparation`, `representation`, `generation`, `evaluation`, `operations`, `governance`
- **Value notes** (the one-line descriptions used in the bare test):
  - `elicitation`: what Jonathan is asked to record or write, and how: recording prompts,
    coverage, coaching, demonstrations, sessions, choosing what to record next.
  - `preparation`: turning raw takes and messages into training data: transcripts,
    alignment, checks on each take, labels, cleaning, what is kept out of the pool.
  - `representation`: how a voice or a style is written down or encoded: markup,
    vocabularies, style labels and tags, embeddings, reference clips as inputs, style
    profiles.
  - `generation`: the models and methods that produce the voice: teachers, students,
    voice cloning, fine-tuning, adapters, prompting with examples, retrieval, synthetic
    data.
  - `evaluation`: judging how close the output is: listening tests, automatic metrics,
    LLM judges, held-out sets, splits, leakage.
  - `operations`: running and rebuilding it: model size, speed, runtime, cost, manifests,
    reproducibility.
  - `governance`: rights and protection: privacy, memorisation, consent, licences,
    watermarks, provenance.
- **Order**: by sequence (the order the work happens), then the two cross-cutting areas.
- **Unsorted**: none.
- **Agreement**: Fleiss' κ 0.87, openai-gemini 0.91; 2026-11-28, 40 items (round 2), Claude Opus 5.5, GPT-6.2-Astra, Gemini 4 Carbon High. Round 1: 0.96, 0.97.

### Modality (`modality`)

- **Question**: Which voice is it about?
- **Principle**: the medium the voice is produced in.
- **Kind**: thing
- **Values**: `spoken`, `written`, `both`
- **Value notes**:
  - `spoken`: speech: recordings, TTS, voice cloning, listening tests.
  - `written`: text: messages, emails, writing style, text generation.
  - `both`: the item applies to both voices as written (a rule about held-out data, a
    privacy rule, a judge bias that holds for audio and text).
- **Order**: by size of the repo's share, then the shared value.
- **Unsorted**: none.
- **Agreement**: Fleiss' κ 0.96, openai-gemini 0.94; 2026-11-28, 40 items (round 2), same raters. Round 1: 1.00, 1.00 (only 2 items were `both`).

### Trait (`trait`)

- **Question**: Which part of the voice is it about?
- **Principle**: the quality of the output the item would change or measure.
- **Kind**: property
- **Values**: `identity`, `expression`, `content`, `naturalness`, `whole-voice`
- **Value notes**:
  - `identity`: who it sounds or reads like: timbre, accent, speaker similarity,
    authorship.
  - `expression`: how something is said or written in one situation: emotion, style,
    stance, prosody, register, tone to an audience.
  - `content`: what is said: the words, pronunciation, intelligibility, meaning kept.
  - `naturalness`: whether it sounds or reads as made by a person, apart from whose it is:
    artefacts, noise, fluency, AI-detectability.
  - `whole-voice`: the voice as a whole, with no one part named: a licence for a cloning
    model, a runtime size, a privacy rule about the archive.
- **Order**: from who, to how, to what, to how well; the whole last.
- **Unsorted**: [`r20`](./samples.md#round-1-test-40) (stored F0, energy and durations), 2026-11-27, answered by the `whole-voice` redefinition (`expression`). [`h07`](./samples.md#held-for-round-2-40) (judges prefer longer text) and [`h13`](./samples.md#held-for-round-2-40) (self and other labels bias judges), 2026-11-28, answered by the new `whole-voice` near miss (`whole-voice` and `identity`).
- **Agreement**: Fleiss' κ 0.89, openai-gemini 0.87; 2026-11-28, 40 items (round 2), same raters. Round 1: 0.81, 0.77, when 6 of 8 disagreements involved `whole-voice`; after its redefinition, 2 of 4.

## Set B (alternative): area, modality, origin

`origin`: whose data or evidence the item works from: `own` (Jonathan's real takes or
messages), `synthetic` (made by a model), `others` (other people's corpora, speakers or
raters). It names the repo's central worry (hypotheses H3, "separately labelled
synthetic"), but in the bare test 5 of 12 items (a markup standard, a verifier rule, a
vocabulary) work from no data at all, so it would need a fourth value that is a
catch-all. Better as a stage facet inside `preparation` and `generation`.

## Set C (alternative): area, trait

Drops `modality`, since the file name (`spoken-*`, `written-*`) gives it for findings. It
does not for the 133 sources (a judge-bias paper serves both voices), and the competency
question 2 ("which findings apply to both voices?") needs it, so set A keeps it.

## Bare-facet test (step 5)

The 12 items `t01`-`t12` ([`samples.md`](./samples.md#bare-facet-test-12)), classified by
Claude on 2026-11-27 with only the value notes above, before any glossary entry was
written.

| Item | area | modality | trait | origin (set B) | Hesitation |
|---|---|---|---|---|---|
| `t01` EmoKnob emotion direction | representation | spoken | expression | own | |
| `t02` name the verifier with every similarity number | evaluation | spoken | identity | — | origin: no data |
| `t03` reading context matters | elicitation | spoken | expression | others | |
| `t04` OpenVoice | generation | spoken | identity | others | |
| `t05` diagnostics beside the main test | evaluation | spoken | content | — | bundles WER, similarity, F0, size, watermark |
| `t06` TSTBench | evaluation | written | expression | others | |
| `t07` Arctic's flat-voice rules | elicitation | spoken | expression | others | |
| `t08` match his pitch in voice conversion | generation | spoken | expression | synthetic | trait: his pitch is identity, per style is expression |
| `t09` MaryTTS | generation | spoken | whole-voice | — | area: platform used for EmotionML synthesis |
| `t10` our emotion and stance vocabulary | representation | spoken | expression | — | origin: no data |
| `t11` DNSMOS | evaluation | spoken | naturalness | others | area: also a check on takes (`preparation`) |
| `t12` parallel text across styles | elicitation | spoken | expression | own | |

Changes made from it (all before the glossary was written):

1. **Bundles**: "if an item names several things, classify the first one named" (as in
   ux and prompts), for `t05`.
2. **Identity or expression**: a trait that stays when he changes style (timbre, overall
   pitch range, accent, idiolect) is `identity`; one that changes with the style or the
   audience (per-style pitch, register) is `expression`. Written into both scope notes,
   for `t08`.
3. **A tool, model or platform** takes the area of what the item says it is used for; a
   metric used to check takes before training is `preparation`, used to judge outputs is
   `evaluation`. For `t09`, `t11`.
4. **Set B's `origin`** failed on 4 of 12 items with no data; kept only as an alternative.
5. `both` and `operations`, `governance`, `preparation` did not occur in 12 items; the
   build sample has them (`b01` preparation, `b31` governance, `b45` operations, `b56`
   both), so they stay for round 1 to test.
