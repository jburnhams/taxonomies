# Voice taxonomy: scope

**In one line**: the vocabulary for `jburnhams/voice-research` (cloning one person's
spoken and written voice for the strata-voice app), built in stages: first the core words
and the questions that sort every source and finding, then one area at a time.

**In plain words**: the voice-research repo reads papers, standards and model repos about
making a small model that sounds like Jonathan, and an assistant that writes like him. It
uses one word for several things ("prompt" is the text he reads aloud, the clip a
voice-cloning model copies, and the text sent to a language model; "reference" is a clip,
a held-out take and a citation), and several words for one thing (take, recording,
utterance, clip). This folder fixes one word per idea, and a few questions that sort every
source and finding, so research passes, designs and the agents that write them say the same
thing the same way. Where a concept is also an agent-design concept (a language model, an
eval, a model that judges another's output), it uses the `prompts` word or maps to it
([`map.md`](./map.md)).

Built with the method in [`design/process.md`](../../design/process.md) (version 1) and
[`design/spec.md`](../../design/spec.md), with the large-domain changes of
[`design/method-v1.1.md`](../../design/method-v1.1.md) (M1-M8, proposed), as the
`prompts` domain is.

- **Context**: [`jburnhams/voice-research`](https://github.com/jburnhams/voice-research)
  (private): the topic docs at the root (`spoken-*.md`, `written-*.md`), the two
  research agendas, the designs in `voice-design/`, and the READMEs of the source folders
  (`papers/`, `specs/`, `repos/`). Short context name: `voice`.
- **Purpose**: to name the concepts of personal voice cloning once, and sort every source
  and finding the repo holds by the questions a research pass or a design asks of it:
  which part of the work it belongs to, whether it is about the spoken or the written
  voice, and which part of the voice it is about.
- **Readers**, in priority order (◆ J9, recommendation followed): Jonathan first; then the
  agents that write the research passes and designs in voice-research and the strata-voice
  app. Where they conflict, Jonathan's reading wins.
- **Owner**: Jonathan. Agents approve changes that pass T1-T6 with a logged reason;
  Jonathan reviews [`changelog.md`](./changelog.md) and can veto (J8, spec G1).
- **Status**: `draft`, stage 1 started 2026-11-27. Item excerpts are public in this repo
  by Jonathan's choice (2026-11-27), though voice-research is private.

## Stages (proposal M1)

The population is 329 items (133 sources, 196 findings; [`samples.md`](./samples.md)),
over M1's threshold of about 300, and the repo's own docs split the work into at least
seven parts (the agendas' areas A-K). So it is built in stages inside one context.

| Stage | Covers | Facets | Status |
|---|---|---|---|
| 1. Kernel | the words every part uses (voice, take, teacher, student, reference clip, style, synthetic data, held-out set, listening test, LLM judge, ...) and the split into areas | proposed set A: `area`, `modality`, `trait` ([`facets.md`](./facets.md)) | draft 2026-11-27 |
| 2+. Areas | one at a time, in the order the repo's work reaches them (J10). Likely first: `evaluation` (most warrant: MOS 189, WER 247, judge 264, metric 151 uses) or `generation` (teacher 223, student 206, fine-tun- 329) | per area | not started |

## Competency questions (stage 1)

Answered from `facets.md` and `glossary.md` alone (T10).

1. Which sources and findings are about what Jonathan is asked to record or write, and which about what is done with it afterwards?
2. Which findings apply to both voices, spoken and written?
3. Which sources are about sounding like him (identity), and which about how he says or writes something (expression)?
4. Which findings concern privacy, consent, licences or provenance?
5. What is the difference between a take, a recording, an utterance and a clip?
6. What is the difference between a teacher and a student, and where does synthetic data come in?
7. What is the difference between a recording prompt, a reference clip and a model prompt?
8. What is the difference between a requested style and an observed style, and between a style, an emotion and a stance?
9. What is the difference between a listening test, an automatic metric and an LLM judge?
10. What is a held-out set, and what counts as leakage into it?
11. What is the difference between zero-shot cloning, fine-tuning and an adapter?
12. What is the difference between retrieval, few-shot examples and a style profile for the written voice?
13. Which words here mean the same as a `prompts` term, and which only look the same?

## Out of scope

- **Stored copies and quotes**: each source folder's stored files, and quotes in its
  README, keep their authors' words (for example "speaker prompt", "SIM", "persona").
  The glossary records them as aliases where they name one of our concepts.
- **Standard identifiers**: SSML and EmotionML element and attribute names (`prosody`,
  `express-as`, `category`), metric acronyms (WER, MOS, EER) and model names
  (Qwen3-TTS, tiny-voca) are governed by their owners; an entry links to them, it does
  not rename them. The repo's CLAUDE.md already says to use the W3C words for markup.
- **Agent design**: how an agent harness, its tools and its context work is the `prompts`
  context. Where voice-research uses one of those concepts (a language model, an eval, a
  model that judges output), it maps to the `prompts` term ([`map.md`](./map.md)).
- **Interface design** of the recording studio: the `ux` context.

## Neighbours

- **prompts** (`domains/prompts/`, stages 1-3 in use): shared concepts `language-model`,
  `eval`, `benchmark`, `second-model` (the LLM judge here is narrower); words that look
  the same but name different things here: `session`, `transcript`, `prompt`. Links
  are in [`map.md`](./map.md), `closeMatch` by default (spec C3).
- **ux** (`domains/ux/`): the recording studio's screens; no shared terms yet.

## Ending conditions (each stage)

As `prompts` (J23 and method v1.1), on the same round:

- T1-T6 clean.
- T7: every item in a fresh sample of 40 gets a value in every facet, or goes to
  **Unsorted** with a note, and **Unsorted** holds at most 3 items (about 7%).
  40 is M3's floor for the largest facet (`area`, 7 values: 35) rounded up.
- T8 (proposal M4): Fleiss' κ ≥ 0.6 on every facet across three raters from three model
  families, and Cohen's κ ≥ 0.6 on every facet between the two non-Claude raters.
- T9: a fresh reader guesses at least 80% of the stage's preferred labels right.
- T10: every competency question above is answered, with the answer in `changelog.md`.
- T11: the Z39.19 §11.2.2 review finds no unmarked synonym and no missing facet.
- No facet added, split or merged in the last round.

## Samples

[`samples.md`](./samples.md): build (60), bare-facet test (12), round-1 test (40), held
for round 2 (40), drawn at voice-research `d02cddc`. Term harvest: [`harvest.md`](./harvest.md).
