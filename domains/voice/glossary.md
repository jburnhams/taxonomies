# Voice taxonomy: glossary

**In one line**: one entry per concept in the voice-research repo, with the word to use,
the other words people use for it, a definition, an example and a near miss.

**In plain words**: when you write in voice-research, use the heading word of the entry.
If you reach for one of its aliases, it points you here. Everything here is `candidate`
until stage 1 passes its rounds (spec G3).

**Status**: stage 1 in use from 2026-11-27, after round 1 and the name test passed
([`scope.md`](./scope.md)). 15 values of facet set A (chosen by Jonathan 2026-11-27,
[`facets.md`](./facets.md)) and 47 kernel terms. 59 are `approved` (`style` after round 2). Three are `candidate`
(`coaching`, `demonstration` "coaching demo", `whole-voice`): each failed or changed in round 2
and waits for the next round. Field rules:
[`design/spec.md` §4](../../design/spec.md#4-glossarymd). Counts:
[`harvest.md`](./harvest.md). Examples link to voice-research (private) at `d02cddc`.
Links to `prompts` terms are in [`map.md`](./map.md).

## Label choices for Jonathan's veto (J8)

1. **"prompt" gets no entry**: it names three concepts here (harvest homonym 1). The text
   he reads is a **`recording-prompt`**, the audio a cloning model copies is a
   **`reference-clip`**, and the text sent to a language model uses the `prompts`
   context's word (see `map.md`; a clarify request is filed there, because `prompts` has
   "prompt" only as an alias of `context-window`, which is defined as a limit).
2. **`take`** for one of Jonathan's recordings (the repo's own word, 266 uses), rather
   than "recording" (also the act and the archive) or "utterance" (the corpora's word for
   anyone's speech).
3. **`style`** for a named way of delivering (cheerful, whispering); its "whole manner of
   one author" sense goes to the trait value `identity` when the question is who wrote it.
   `emotion` and `stance` are narrower in use but kept as separate entries, not broader
   links, because the W3C vocabularies name emotions and not stances.
4. **`language model`** rather than "model" or "LLM": here "model" alone could be a TTS
   model, a verifier or an LLM. `closeMatch` to `prompts:language-model` (labelled "model"
   there), whose definition ("that a harness calls") is narrower than the use here.
5. **`LLM judge`** rather than `prompts`' "second model": in voice-research only a language
   model in this role is ever meant, and the repo says "judge" 264 times. Mapped
   `broadMatch prompts:second-model`.
6. **`eval`** and **`benchmark`** reuse the `prompts` labels and definitions (`exactMatch`),
   with "agent or model" cut to "model".
7. **`recording session`**, not "session", so as not to collide with `prompts:session`;
   "transcript" (the words of a take) gets no entry in stage 1 and is mapped as a
   different concept to `prompts:transcript`.
8. **`identity embedding`** for speaker and authorship embeddings together (the repo has
   no word for both), so the trait split (identity vs expression) is visible in the
   names: `style embedding` beside it.
9. **`whole voice`** as the fifth trait value, for items that name no one part (a licence,
   a runtime size). It is not a catch-all of the "other" kind: it is used only when no
   part is named.
10. **`operations`** is flagged by T3 as a possible plural; a mass noun, as in `prompts`.
11. **`coaching`** may need a new label: in both name tests, readers took it as feedback on a
   take, which its scope excludes. "Style cue" (from its alias "cue") is the option to test
   next round.

## Area values (`area`)

### elicitation (`elicitation`)

- **Definition**: Elicitation is an area of the work that covers what Jonathan is asked to record or write, and how he is asked.
- **Scope**: Includes recording prompts and scripts, coverage of sounds and styles, coaching and demonstrations, recording sessions and their order, and choosing what to record next (active learning). Excludes what is done with a take once recorded (`preparation`).
- **Aliases**: recording design, script design, data collection
- **Example**: [spoken-elicitation.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-elicitation.md), script design and emotion elicitation.
- **Near miss**: A held-out intelligibility list such as the Harvard sentences: he reads it, but it is chosen to test the output, so it is `evaluation` when the point is the test.
- **Kind**: thing
- **Facet**: `area`
- **Status**: approved
- **Warrant**: elicit- 45 / 22; script 50; coverage 96; coach- 39; agenda areas B, C, E
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### preparation (`preparation`)

- **Definition**: Preparation is an area of the work that covers turning raw takes and messages into training data.
- **Scope**: Includes transcripts, forced alignment, checks on each take (noise, clipping, wrong words), observed-style labels, cleaning and deduplication of messages, and what is kept out of the training pool. Excludes splitting off a held-out set (`evaluation`) and how a style is encoded as model input (`representation`).
- **Aliases**: dataset QA, data processing, annotation
- **Example**: [spoken-dataset-qa.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-dataset-qa.md), checking each take.
- **Near miss**: A quality score such as DNSMOS: it is `preparation` when it filters takes before training, and `evaluation` when it scores a model's output.
- **Kind**: thing
- **Facet**: `area`
- **Status**: approved
- **Warrant**: align- 191 / 55; transcript 75; dataset 183; agenda area H
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### representation (`representation`)

- **Definition**: Representation is an area of the work that covers how a voice or a style is written down or encoded.
- **Scope**: Includes markup (SSML, EmotionML), emotion and stance vocabularies, style labels and tags, pronunciation lexicons, style and speaker embeddings, reference clips used as model inputs, and written style profiles. Excludes the model that reads them (`generation`).
- **Aliases**: style representation, style control
- **Example**: [spoken-style-representation.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-style-representation.md), markup, vocabularies, labels and model inputs.
- **Near miss**: A teacher that takes a separate emotion reference: the model is `generation`; the separate input is `representation` when the item is about the input.
- **Kind**: thing
- **Facet**: `area`
- **Status**: approved
- **Warrant**: markup 123; EmotionML 97; embedding 204; label 216; agenda areas A, D
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### generation (`generation`)

- **Definition**: Generation is an area of the work that covers the models and methods that produce speech or text in the voice.
- **Scope**: Includes teachers and students, voice cloning, fine-tuning and adapters, synthetic data and voice conversion, vocoders, and for the written voice prompting with examples, retrieval, refinement and preference training. Excludes how inputs are encoded (`representation`) and judging the result (`evaluation`).
- **Aliases**: synthesis, training, modelling
- **Example**: [spoken-teachers.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-teachers.md), choosing a teacher.
- **Near miss**: A rule never to put teacher audio in the held-out set: it is about synthetic data, but its job is to protect the test, so it is `evaluation`.
- **Kind**: thing
- **Facet**: `area`
- **Status**: approved
- **Warrant**: teacher 223; student 206; fine-tun- 329; synthetic 178; TTS 649; agenda areas F, G
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### evaluation (`evaluation`)

- **Definition**: Evaluation is an area of the work that covers judging how close the output is to the real voice.
- **Scope**: Includes listening tests, pairwise judgements, automatic metrics and their calibration, LLM judges, held-out sets, splits and leakage, baselines and benchmarks. Excludes checks on Jonathan's own takes before training (`preparation`).
- **Aliases**: assessment, testing
- **Example**: [spoken-evaluation.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-evaluation.md), evaluating the spoken voice.
- **Near miss**: A watermark on every generated clip: it is listed beside the diagnostics, but it protects against misuse, so it is `governance`.
- **Kind**: thing
- **Facet**: `area`
- **Status**: approved
- **Warrant**: eval- 340 / 122; MOS 189; WER 247; metric 151; agenda area I
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### operations (`operations`)

- **Definition**: Operations is an area of the work that covers running, rebuilding and paying for the voice models.
- **Scope**: Includes model and package size, speed and real-time factor, the runtime (CPU, browser, ONNX), quantisation, GPU hours and cost, manifests, versions and reproducibility. Excludes the choice of architecture for quality (`generation`).
- **Aliases**: deployment, cost, reproducibility
- **Example**: [spoken-student.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-student.md), what model runs locally.
- **Near miss**: A student's parameter count quoted to compare quality: it is `generation` when the point is what the model can learn, `operations` when the point is whether it fits.
- **Kind**: thing
- **Facet**: `area`
- **Status**: approved
- **Warrant**: real-time 30 / 18; ONNX 25; quanti- 20; agenda areas G (deployment), K
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### governance (`governance`)

- **Definition**: Governance is an area of the work that covers the rights to the voice data and models and their protection from misuse.
- **Scope**: Includes privacy of the archive, memorisation and leakage of personal details by a trained model, consent, licences of teachers, corpora and providers, watermarks and provenance. Excludes leakage of test data into training (`evaluation`).
- **Aliases**: privacy, safety, data governance
- **Example**: [written-methods.md](https://github.com/jburnhams/voice-research/blob/d02cddc/written-methods.md), §5, privacy when training on a private archive.
- **Near miss**: A licence that forbids training on a teacher's outputs: it decides which teacher is usable, but it is a right, so it is `governance` even inside a teacher comparison.
- **Kind**: thing
- **Facet**: `area`
- **Status**: approved
- **Warrant**: licence 265 / 140; privacy 87; watermark 42; consent 10; agenda area J
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

## Modality values (`modality`)

### spoken (`spoken`)

- **Definition**: Spoken is a modality value for items about Jonathan's voice as speech.
- **Scope**: Includes recordings, text-to-speech, voice cloning, markup for speech, listening tests and speech metrics.
- **Aliases**: speech, spoken voice, audio
- **Example**: [spoken-teachers.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-teachers.md), teachers for the spoken voice.
- **Near miss**: An LLM writing the recording prompts: the LLM writes text, but the item is about what he reads aloud, so it is `spoken`.
- **Kind**: thing
- **Facet**: `modality`
- **Status**: approved
- **Warrant**: spoken-*.md (9 topic docs); speaker 822; TTS 649
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### written (`written`)

- **Definition**: Written is a modality value for items about Jonathan's voice as writing.
- **Scope**: Includes his messages and emails, writing style, authorship, text generation with language models and text metrics.
- **Aliases**: text, writing, written voice
- **Example**: [written-methods.md](https://github.com/jburnhams/voice-research/blob/d02cddc/written-methods.md), generating text in one person's voice.
- **Near miss**: A paper on LLM judges of writing style: it is about text, so `written`, unless the item says the same bias holds for audio.
- **Kind**: thing
- **Facet**: `modality`
- **Status**: approved
- **Warrant**: written-*.md (3 topic docs); author 535; message 130
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### both (`both`)

- **Definition**: Both is a modality value for items that apply to the spoken and the written voice alike, as written.
- **Scope**: Includes rules on held-out data and leakage, privacy and consent rules, judge biases and preference methods that the item applies to both, and the agendas' shared protocol. An item from a spoken or written doc is that doc's voice unless it says it holds for both.
- **Aliases**: shared, cross-modal
- **Example**: [voice-design/data-collection.md](https://github.com/jburnhams/voice-research/blob/d02cddc/voice-design/data-collection.md), what to record and keep now.
- **Near miss**: A finding about LLM judges in a written-voice doc: judges exist for audio too, but the item is about text, so it is `written`.
- **Kind**: thing
- **Facet**: `modality`
- **Status**: approved
- **Warrant**: voice-design/ docs and the agendas' shared sections
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

## Trait values (`trait`)

### identity (`identity`)

- **Definition**: Identity is a trait of a voice that makes it sound or read as one particular person.
- **Scope**: Includes timbre, accent, overall pitch range, idiolect and habits that stay when he changes style, speaker similarity, speaker verification and authorship. Excludes what changes with the style or the audience (`expression`).
- **Aliases**: speaker identity, authorship, sounds like me, timbre
- **Example**: [spoken-evaluation.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-evaluation.md), "sounds like me" as the outcome.
- **Near miss**: His pitch when sarcastic: pitch is his, but the value that changes with the style is `expression`; his pitch range across all takes is `identity`.
- **Kind**: property
- **Facet**: `trait`
- **Status**: approved
- **Warrant**: identity 77; speaker similarity 190; authorship 117; accent 177; timbre 36
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### expression (`expression`)

- **Definition**: Expression is a trait of a voice that is how something is said or written in one situation.
- **Scope**: Includes emotion, style, stance, vocal events, prosody that varies by style, register and tone towards an audience, and style transfer. Excludes what stays the same across styles (`identity`).
- **Aliases**: delivery, register, tone, expressiveness
- **Example**: [spoken-style-representation.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-style-representation.md), representing and controlling style.
- **Near miss**: A style embedding used to verify authorship: it is called "style", but the question it answers is who wrote it, so `identity`.
- **Kind**: property
- **Facet**: `trait`
- **Status**: approved
- **Warrant**: style 1,231; emotion 447; expressi- 228; prosod- 144; stance 110
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### content (`content`)

- **Definition**: Content is a trait of a voice that is what is said: the words and their meaning.
- **Scope**: Includes the words spoken or written, pronunciation and lexicons, intelligibility and WER, phonetic coverage, and whether a draft keeps the facts of its brief. Excludes accent, which is how he pronounces (`identity`).
- **Aliases**: content fidelity, intelligibility, pronunciation
- **Example**: [written-evaluation.md](https://github.com/jburnhams/voice-research/blob/d02cddc/written-evaluation.md), content fidelity.
- **Near miss**: A British word list (BATH/TRAP, T-glottalling): it tests words, but the point is how he says them, so `identity`.
- **Kind**: property
- **Facet**: `trait`
- **Status**: approved
- **Warrant**: WER 247; content fidelity / meaning 20; diphone 63; intelligib- 23
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### naturalness (`naturalness`)

- **Definition**: Naturalness is a trait of a voice that is whether it sounds or reads as made by a person, apart from which person.
- **Scope**: Includes artefacts, noise and clipping, over-smoothing, fluency, MOS for naturalness or quality, and AI-text detection. Excludes whether it is his (`identity`).
- **Aliases**: quality, audio quality, fluency
- **Example**: [spoken-dataset-qa.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-dataset-qa.md), quality checks.
- **Near miss**: A listening test asking "which sounds more like you?": a person judges, but the question is whose voice, so `identity`.
- **Kind**: property
- **Facet**: `trait`
- **Status**: approved
- **Warrant**: natural- 162 / 65; MOS 189
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### whole voice (`whole-voice`)

- **Definition**: Whole voice is a trait value for items about the voice as a whole, with no one part of it named.
- **Scope**: Includes licences and rights for a cloning model, runtime size and speed, privacy rules for the whole archive, and surveys that cover every part. Use it only when the item names no part and measures, changes or stores no quality of the output. An item that names a part only through a metric or a model still names it: WER and ROUGE are `content`, speaker similarity and a cloning model's voice input are `identity`, a judge recognising whose text it is is `identity`. Stored features (pitch, energy, durations) take the trait they are kept for, `expression` when the item does not say.
- **Aliases**: overall, all traits
- **Example**: [spoken-student.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-student.md), tiny-voca's size and runtime.
- **Near miss**: A judge's length or position bias: it skews whatever the judge scores and names no part, so `whole-voice`; a judge recognising its own text is about whose text it is, so `identity`. A model release that clones from reference audio: it names no trait in words, but cloning a voice is `identity`. A small model's speed and size: `whole-voice`, since no quality of the output is named.
- **Kind**: property
- **Facet**: `trait`
- **Status**: candidate
- **Warrant**: voice 1,000+ (every doc); voice clon- 127
- **History**: 2026-11-27 added. 2026-11-27 redefine: scope says a part named through a metric or model counts as named; 6 of 8 round-1 `trait` disagreements involved this value. 2026-11-28 redefine: near miss for judge biases (round-2 splits `h07`, `h13`); both name-test readers read the label right, stays candidate for one more round.

## Kernel terms (stage 1)

### voice (`voice`)

- **Definition**: A voice is a way of speaking or writing that marks one person, taken as something a model can reproduce.
- **Scope**: Includes the spoken voice and the written voice, each with identity, expression, content and naturalness. Excludes a voice as a TTS product's preset speaker ("an Azure voice"), which is a vendor's word for a model setting.
- **Aliases**: personal voice
- **Example**: [README.md](https://github.com/jburnhams/voice-research/blob/d02cddc/README.md), "cloning one person's voice, spoken and written".
- **Near miss**: An Azure voice such as Sonia: a vendor's preset speaker, used for demonstrations, not anyone's voice to clone.
- **Kind**: thing
- **Status**: approved
- **Warrant**: voice in every doc; Jonathan's words: "personal voice cloning"
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### take (`take`)

- **Definition**: A take is a recording of one recording prompt read once by Jonathan in one recording session.
- **Scope**: Includes retakes of the same prompt (each is a take), styled and neutral takes, and unscripted speech cut into units. Excludes other people's recordings in a corpus (utterances) and generated audio (`synthetic-data`).
- **Aliases**: recording, utterance, clip, sample
- **Example**: [voice-design/data-collection.md](https://github.com/jburnhams/voice-research/blob/d02cddc/voice-design/data-collection.md), what each take keeps.
- **Near miss**: An utterance in LibriTTS or ESD: one recorded unit of speech, but someone else's.
- **Kind**: thing
- **Related**: `recording-prompt`, `real-data`
- **Status**: approved
- **Warrant**: take (noun) 266 / 87; recording 175; utterance 152; clip 158
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### message (`message`)

- **Definition**: A message is a piece of Jonathan's real writing sent to someone: an email, a chat or a post.
- **Scope**: Includes sent messages with their thread, recipient and time, and his edits of a generated draft once sent. Excludes drafts a model generated (a draft, not a message) and other people's messages in the thread (kept as context).
- **Aliases**: email, sent message, post
- **Example**: [written-methods.md](https://github.com/jburnhams/voice-research/blob/d02cddc/written-methods.md), "100 or more sent messages per register".
- **Near miss**: A draft: text a model wrote for him to send; it becomes evidence only through his choice or edit.
- **Kind**: thing
- **Status**: approved
- **Warrant**: message 130 / 41; email in written docs
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### real data (`real-data`)

- **Definition**: Real data is a body of recordings or writing that Jonathan himself produced.
- **Scope**: Includes his takes, unscripted speech, found recordings and sent messages. Excludes anything a model made, even in his voice (`synthetic-data`), and other speakers' corpora.
- **Aliases**: own data, genuine data, human data
- **Example**: [voice-design/data-collection.md](https://github.com/jburnhams/voice-research/blob/d02cddc/voice-design/data-collection.md), what to record and keep now.
- **Near miss**: Voice-converted audio in his timbre: it sounds like him, but a model made it, so it is synthetic data.
- **Kind**: thing
- **Related**: `synthetic-data`
- **Status**: approved
- **Warrant**: real 393 / 97 ("real takes", "real data"); genuine
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### synthetic data (`synthetic-data`)

- **Definition**: Synthetic data is a body of speech or text that a model generated for training or testing, kept labelled apart from real data.
- **Scope**: Includes teacher audio in his voice, voice-converted audio, pseudo-labels (transcripts made by a model) and generated text. Excludes demonstrations, which are played to coach him and never trained on.
- **Aliases**: teacher data, generated data, augmentation data, pseudo-labels
- **Example**: [spoken-synthetic-augmentation.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-synthetic-augmentation.md), how much teacher audio.
- **Near miss**: A demonstration: generated audio too, but played to Jonathan as a cue, not used as data.
- **Kind**: thing
- **Related**: `real-data`, `teacher`
- **Status**: approved
- **Warrant**: synthetic 178 / 62; augment- 85 / 31; pseudo- 18
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### recording prompt (`recording-prompt`)

- **Definition**: A recording prompt is a text that Jonathan is shown to read aloud for a take.
- **Scope**: Includes a sentence from a script, a scenario he answers in his own words, and the style he is asked for with it. Excludes text sent to a language model (a model prompt, see `map.md`) and audio given to a cloning model (`reference-clip`).
- **Aliases**: script line, recording script, reading text
- **Example**: [spoken-elicitation.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-elicitation.md), §1, sound coverage.
- **Near miss**: A reference clip: also called a "prompt" in the teacher papers, but it is audio a model copies, not text he reads.
- **Kind**: thing
- **Related**: `take`, `coaching`
- **Status**: approved
- **Warrant**: prompt 426 / 96 (all senses); script 50; "prompt set"
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### recording session (`recording-session`)

- **Definition**: A recording session is a single sitting in which Jonathan records a run of takes under one set of conditions.
- **Scope**: Includes the room tone, microphone and browser settings recorded with it, and the order of prompts within it. Excludes a harness session (`prompts:session`).
- **Aliases**: session, sitting
- **Example**: [voice-design/data-collection.md](https://github.com/jburnhams/voice-research/blob/d02cddc/voice-design/data-collection.md), §1.3 recording conditions.
- **Near miss**: A harness session in the prompts context: same word, a different thing.
- **Kind**: happening
- **Status**: approved
- **Warrant**: session 111 / 39
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### coaching (`coaching`)

- **Definition**: Coaching is a cue shown or played with a recording prompt to ask for a style.
- **Scope**: Includes a style label, an emoji, a colour, a scenario card, and a demonstration before or after the first take. Excludes the recording prompt's text itself, and feedback on a take after it is recorded ("try that warmer"), which is a retake request.
- **Aliases**: cue, emotional cue, coaching mode
- **Example**: [spoken-elicitation.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-elicitation.md), §3, coaching.
- **Near miss**: A style label in the canonical record: the same word may be shown as coaching, but in the record it is the requested style.
- **Kind**: thing
- **Related**: `demonstration`, `requested-style`
- **Status**: candidate
- **Warrant**: coach- 39 / 16; cue
- **History**: 2026-11-27 added. 2026-11-27 redefine: scope excludes feedback after a take; a name-test reader read "coaching" as live direction. 2026-11-28 stays candidate: both round-2 name-test readers read it as feedback on takes; a relabel ("style cue") is for Jonathan.

### coaching demo (`demonstration`)

- **Definition**: A coaching demo is a generated clip played to Jonathan to show how a style might sound before or after he records it.
- **Scope**: Includes Azure and local TTS demos. Excludes any use as training data or as a speaker-similarity reference (data-collection §3).
- **Aliases**: demonstration, demo, demo audio
- **Example**: [voice-design/data-collection.md](https://github.com/jburnhams/voice-research/blob/d02cddc/voice-design/data-collection.md), §1.2, how each prompt is given.
- **Near miss**: Synthetic data: also generated audio, but trained on, not played to him. A few-shot example: shows a model what to write; a coaching demo is only ever played to Jonathan. A walkthrough of how coaching works: a coaching demo is one clip of a style, not a demonstration of the process.
- **Kind**: thing
- **Related**: `coaching`
- **Status**: candidate
- **Warrant**: demonstration, demo 71 / 34
- **History**: 2026-11-27 added. 2026-11-27 rename: "demonstration" → "coaching demo" (ID kept); both name-test readers read "demonstration" as an example shown to a model. 2026-11-28 redefine: near miss for "walkthrough of the process"; one of two round-2 name-test readers read it so. Stays candidate.

### coverage (`coverage`)

- **Definition**: Coverage is a property of a set of takes or messages: the share of the needed units it contains.
- **Scope**: Includes diphone and triphone coverage, coverage of stress and sentence types, of styles and intensities, and for writing of media and recipients. Excludes how many hours there are (amount).
- **Aliases**: phonetic coverage, style coverage
- **Example**: [spoken-acquisition.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-acquisition.md), coverage-only ranking.
- **Near miss**: Data amount: more minutes need not add coverage; CMU Arctic's first 593 prompts reach 78% of diphones.
- **Kind**: property
- **Status**: approved
- **Warrant**: coverage 96 / 36; diphone 63
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### teacher (`teacher`)

- **Definition**: A teacher is a role of a large model that generates synthetic data in Jonathan's voice to train a smaller model.
- **Scope**: Includes zero-shot cloning models and fine-tuned ones (Qwen3-TTS, IndexTTS2, CosyVoice) and, for writing, a large language model whose drafts train a smaller one. Excludes a TTS used only for demonstrations.
- **Aliases**: teacher model
- **Example**: [spoken-teachers.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-teachers.md), choosing a teacher.
- **Near miss**: Azure TTS in coaching: it generates speech, but never his and never for training.
- **Kind**: role
- **Related**: `student`, `synthetic-data`
- **Status**: approved
- **Warrant**: teacher 223 / 74
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### student (`student`)

- **Definition**: A student is a role of a small model trained on real and synthetic data to run locally in Jonathan's voice.
- **Scope**: Includes tiny-voca and its style-conditioned variants, Pocket TTS as a baseline, and a small fine-tuned language model for writing. Excludes the teacher it learns from.
- **Aliases**: student model, small model, local model
- **Example**: [spoken-student.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-student.md), what model runs locally.
- **Near miss**: A small teacher: Pocket TTS can clone zero-shot, but here it is the baseline a student must beat.
- **Kind**: role
- **Related**: `teacher`
- **Status**: approved
- **Warrant**: student 206 / 80
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### text-to-speech model (`tts-model`)

- **Definition**: A text-to-speech model is a model that turns text, and optional inputs such as markup or a reference clip, into speech.
- **Scope**: Includes teachers, students, vocoder-based pipelines and vendor services such as Azure TTS. Excludes speech recognition (ASR) and speaker verification models, which take speech in.
- **Aliases**: TTS, TTS model, speech synthesiser, synthesis model
- **Example**: [papers/fastspeech2/README.md](https://github.com/jburnhams/voice-research/blob/d02cddc/papers/fastspeech2/README.md), FastSpeech 2.
- **Near miss**: A speaker verifier: also a speech model, but it reads speech and outputs a score.
- **Kind**: thing
- **Status**: approved
- **Warrant**: TTS 649 / 92; TTS model 27
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### language model (`language-model`)

- **Definition**: A language model is a model that generates text from text, used here to write recording prompts, draft messages and judge output.
- **Scope**: Includes cloud and local LLMs, fine-tuned ones and their adapters. Excludes TTS models built on a language-model backbone (`tts-model`).
- **Aliases**: LLM, large language model
- **Example**: [written-methods.md](https://github.com/jburnhams/voice-research/blob/d02cddc/written-methods.md), prompting a strong cloud model.
- **Near miss**: CosyVoice's LM stage: a language model inside a TTS model, so the whole is a `tts-model`.
- **Kind**: thing
- **Matches**: closeMatch `prompts:language-model`
- **Status**: approved
- **Warrant**: LLM 296 / 66; language model 85 / 33
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### voice cloning (`voice-cloning`)

- **Definition**: Voice cloning is a process that makes a model produce speech or text in a given person's voice.
- **Scope**: Includes zero-shot cloning from a reference clip, fine-tuning on the person's data, and voice conversion of other speech into the voice. For writing, imitation of one author ("written voice cloning").
- **Aliases**: cloning, voice clone, author imitation
- **Example**: [spoken-teachers.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-teachers.md), no single teacher gives his voice, accent and style.
- **Near miss**: Style transfer: it changes how something is said, not whose voice it is.
- **Kind**: happening
- **Status**: approved
- **Warrant**: voice clon- 127 / 57; imitation (written)
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### zero-shot cloning (`zero-shot-cloning`)

- **Definition**: Zero-shot cloning is voice cloning from a reference clip or examples given at inference, with no change to the model's weights.
- **Scope**: Includes a few seconds of reference audio for a teacher, and few-shot examples for a language model. Excludes fine-tuning.
- **Aliases**: zero-shot TTS, in-context cloning
- **Example**: [papers/seed-tts/README.md](https://github.com/jburnhams/voice-research/blob/d02cddc/papers/seed-tts/README.md), Seed-TTS on accented speakers.
- **Near miss**: Fine-tuning on ten minutes of his speech: it also uses little data, but it changes the weights.
- **Kind**: happening
- **Broader**: `voice-cloning`
- **Related**: `reference-clip`
- **Status**: approved
- **Warrant**: zero-shot 137 / 45
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### fine-tuning (`fine-tuning`)

- **Definition**: Fine-tuning is a process that trains an existing model's weights further on a person's data so that it produces their voice.
- **Scope**: Includes full fine-tuning, speaker adaptation, SFT on one speaker, and training adapters. Excludes training a model from scratch and anything done only in the prompt (`zero-shot-cloning`).
- **Aliases**: SFT, speaker adaptation, adaptation
- **Example**: [papers/cosyvoice2/README.md](https://github.com/jburnhams/voice-research/blob/d02cddc/papers/cosyvoice2/README.md), single-speaker fine-tuning from 400 recordings.
- **Near miss**: Preference training (DPO): it also changes weights, but from pairs of choices rather than his data as targets; a later stage may give it an entry.
- **Kind**: happening
- **Related**: `adapter`, `voice-cloning`
- **Status**: approved
- **Warrant**: fine-tun- 329 / 78; adaptation 65 / 26
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### adapter (`adapter`)

- **Definition**: An adapter is a small set of added weights trained in place of a whole model's weights.
- **Scope**: Includes LoRA, QLoRA, RoSA and residual adapters in TTS. Excludes steering vectors added to activations without training.
- **Aliases**: LoRA, QLoRA, RoSA, PEFT
- **Example**: [written-methods.md](https://github.com/jburnhams/voice-research/blob/d02cddc/written-methods.md), §4, adapter mechanics.
- **Near miss**: A steering vector: a direction added at inference, not trained weights.
- **Kind**: thing
- **Status**: approved
- **Warrant**: adapter 78 / 18; LoRA 124 / 21
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### reference clip (`reference-clip`)

- **Definition**: A reference clip is a clip of speech given to a text-to-speech model at inference to set the voice or the style it copies.
- **Scope**: Includes speaker references, separate emotion references (IndexTTS2) and the choice among several candidate clips. Excludes a held-out take used as MUSHRA's hidden reference (evaluation), and other speakers' clips for style, which leak their voice.
- **Aliases**: speaker prompt, audio prompt, reference audio, voice prompt
- **Example**: [spoken-teachers.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-teachers.md), "the reference carries its conditions".
- **Near miss**: A recording prompt: what he reads to make a take; a take becomes a reference clip only when it is given to a model.
- **Kind**: thing
- **Related**: `zero-shot-cloning`
- **Status**: approved
- **Warrant**: reference (clip, audio) 30 / 18; reference 293 (all senses)
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### style (`style`)

- **Definition**: A style is a named way of delivering speech or text that Jonathan can be asked for, such as cheerful, whispering or formal.
- **Scope**: Includes emotions, stances and speaking modes (whisper, chat) when named as a target. Excludes a whole author's manner as in "style embedding" for authorship (`identity`).
- **Aliases**: speaking style, delivery style
- **Example**: [spoken-style-representation.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-style-representation.md), the project vocabulary.
- **Near miss**: Writing style in authorship verification, or "his style" meaning his habits in every situation: the word is the same, but the question is who, not how, so that is `identity`.
- **Kind**: thing
- **Related**: `emotion`, `stance`
- **Status**: approved
- **Warrant**: style 1,231 / 137 (all senses)
- **History**: 2026-11-27 added. 2026-11-27 redefine: near miss names the habit sense; a name-test reader read "style" as his characteristic manner. Label kept (N6, 1,231 uses). 2026-11-28 approved (round 2 and name test passed).

### emotion (`emotion`)

- **Definition**: An emotion is a feeling named from an EmotionML vocabulary that a take or output is asked to express or is heard to express.
- **Scope**: Includes categories (the W3C "everyday" set, Ekman's six), dimensions (PAD) and intensity. Excludes stances such as sarcasm, which the W3C vocabularies do not name.
- **Aliases**: emotion category, emotional style
- **Example**: [specs/w3c-emotion-voc/README.md](https://github.com/jburnhams/voice-research/blob/d02cddc/specs/w3c-emotion-voc/README.md), W3C emotion vocabularies.
- **Near miss**: Sarcasm: an attitude to what is said, not a feeling, so a `stance`.
- **Kind**: thing
- **Status**: approved
- **Warrant**: emotion 447 / 62; EmotionML 97
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### stance (`stance`)

- **Definition**: A stance is an attitude a speaker takes towards what they say or to whom, named in the project vocabulary.
- **Scope**: Includes sarcastic, sympathetic, reassuring, sincere and disbelieving. Excludes feelings in the W3C vocabularies (`emotion`).
- **Aliases**: attitude, pragmatic style
- **Example**: [spoken-style-representation.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-style-representation.md), "What we conclude" 2.
- **Near miss**: Sadness: a feeling the W3C vocabulary names, so `emotion`.
- **Kind**: thing
- **Status**: approved
- **Warrant**: stance 110 / 57
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### vocal event (`vocal-event`)

- **Definition**: A vocal event is a sound in speech that is not a word, such as a laugh, sigh, breath or filler.
- **Scope**: Includes events that are prompted and ones that occur unprompted in takes. Excludes pauses, which are prosody.
- **Aliases**: non-verbal sound, paralinguistic event
- **Example**: [spoken-style-representation.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-style-representation.md), project vocabulary for vocal events.
- **Near miss**: A pause: timing of the words, so `prosody`.
- **Kind**: thing
- **Status**: approved
- **Warrant**: vocal event, laugh, filler, sigh 85 / 29
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### prosody (`prosody`)

- **Definition**: Prosody is a property of speech: its pitch, timing, loudness and pauses over the words.
- **Scope**: Includes F0, duration, rate, energy, emphasis and pause distributions, measured or controlled. Excludes timbre, which is the sound of the voice itself (`identity`).
- **Aliases**: intonation, F0, pitch contour
- **Example**: [spoken-style-representation.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-style-representation.md), explicit prosody inputs.
- **Near miss**: Accent: also heard in the sounds of words, but a matter of pronunciation, not pitch and timing.
- **Kind**: property
- **Status**: approved
- **Warrant**: prosod- 144 / 55; F0, pitch 267 / 50
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### accent (`accent`)

- **Definition**: An accent is a property of a voice: the way its speaker pronounces words, shared with a region or group.
- **Scope**: Includes British vowel and consonant features (BATH/TRAP, non-rhotic r, T-glottalling) and his own pronunciations in the PLS lexicon. Excludes prosody.
- **Aliases**: pronunciation variety, British accent
- **Example**: [spoken-teachers.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-teachers.md), "accent is where zero-shot fails".
- **Near miss**: A pronunciation error by a model: wrong words, which is `content`, unless the item is about drift towards another accent.
- **Kind**: property
- **Status**: approved
- **Warrant**: accent 177 / 56
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### requested style (`requested-style`)

- **Definition**: A requested style is a style that a recording prompt, coaching or a model input asks for.
- **Scope**: Includes the EmotionML annotation of what was asked. Excludes what was actually heard (`observed-style`).
- **Aliases**: intended style, target style
- **Example**: [spoken-style-representation.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-style-representation.md), "requested vs observed".
- **Near miss**: An observed style: what a listener or Jonathan heard in the take, which may differ.
- **Kind**: role
- **Related**: `observed-style`, `style`
- **Status**: approved
- **Warrant**: requested 30 / 13 (with observed)
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### observed style (`observed-style`)

- **Definition**: An observed style is a style that a listener, Jonathan or a classifier hears in a take or output.
- **Scope**: Includes labels added after recording, and the unverified state until a person confirms it. Excludes the style that was asked for (`requested-style`).
- **Aliases**: perceived style, heard style
- **Example**: [papers/expresso/README.md](https://github.com/jburnhams/voice-research/blob/d02cddc/papers/expresso/README.md), a requested label is not the observed one.
- **Near miss**: A requested style: the label shown before the take.
- **Kind**: role
- **Related**: `requested-style`, `style`
- **Status**: approved
- **Warrant**: observed 30 / 13 (with requested)
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### style label (`style-label`)

- **Definition**: A style label is a word or short phrase that names a style, attached to a take or given to a model.
- **Scope**: Includes emotion labels, free-text tags in his own words and machine-written captions. Excludes markup that carries the label in a standard format (`markup`).
- **Aliases**: tag, style tag, caption, emotion label
- **Example**: [papers/style-tag-tts/README.md](https://github.com/jburnhams/voice-research/blob/d02cddc/papers/style-tag-tts/README.md), free-text tags regressed onto style embeddings.
- **Near miss**: A style embedding: a learned vector, not words.
- **Kind**: thing
- **Status**: approved
- **Warrant**: label 216 / 75; tag 118 / 23; caption 14
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### markup (`markup`)

- **Definition**: Markup is a text annotation in a standard format that tells a TTS model how to speak the text it surrounds.
- **Scope**: Includes SSML 1.1, EmotionML 1.0 embedded in it, PLS lexicons and vendor extensions such as Azure's express-as. Excludes free-text style labels.
- **Aliases**: SSML, EmotionML annotation, speech markup
- **Example**: [specs/w3c-ssml-1.1/README.md](https://github.com/jburnhams/voice-research/blob/d02cddc/specs/w3c-ssml-1.1/README.md), SSML 1.1.
- **Near miss**: A free-text tag ("a bit wry"): words about a style, but in no standard.
- **Kind**: thing
- **Status**: approved
- **Warrant**: markup, SSML 123 / 28; EmotionML 97 / 29
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### style embedding (`style-embedding`)

- **Definition**: A style embedding is a learned vector that encodes how something is said, used to control or compare style.
- **Scope**: Includes global style tokens, reference-encoder outputs, style vectors and emotion directions. Excludes vectors that encode who is speaking or writing (`identity-embedding`).
- **Aliases**: style vector, style token, GST, emotion direction
- **Example**: [papers/global-style-tokens/README.md](https://github.com/jburnhams/voice-research/blob/d02cddc/papers/global-style-tokens/README.md), global style tokens.
- **Near miss**: A LUAR authorship embedding: called a style representation, but trained to answer "same author?", so `identity-embedding`.
- **Kind**: thing
- **Related**: `identity-embedding`
- **Status**: approved
- **Warrant**: embedding 204 / 76; style vector 21; style token 26
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### identity embedding (`identity-embedding`)

- **Definition**: An identity embedding is a learned vector that encodes who is speaking or writing, used to compare a sample with a person.
- **Scope**: Includes speaker embeddings (ECAPA-TDNN, WavLM features) and authorship embeddings (LUAR). Excludes style embeddings.
- **Aliases**: speaker embedding, authorship embedding, speaker vector, LUAR
- **Example**: [papers/ecapa-tdnn/README.md](https://github.com/jburnhams/voice-research/blob/d02cddc/papers/ecapa-tdnn/README.md), ECAPA-TDNN speaker embeddings.
- **Near miss**: A style embedding: encodes how, not who; a reference embedding that leaks the speaker is a style embedding with a fault.
- **Kind**: thing
- **Related**: `speaker-similarity`
- **Status**: approved
- **Warrant**: speaker embedding 40 / 26; authorship embedding (LUAR) in written-evaluation
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### style profile (`style-profile`)

- **Definition**: A style profile is a written description of a person's writing habits put in a language model's prompt.
- **Scope**: Includes LLM-extracted trait lists and evidence-anchored short profiles. Excludes real messages given as few-shot examples.
- **Aliases**: profile, persona description, style description
- **Example**: [papers/personalbench/README.md](https://github.com/jburnhams/voice-research/blob/d02cddc/papers/personalbench/README.md), profiles barely repeat between runs.
- **Near miss**: Few-shot examples: his real messages, not a description of them.
- **Kind**: thing
- **Status**: approved
- **Warrant**: profile 111 / 32
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### few-shot example (`few-shot-example`)

- **Definition**: A few-shot example is a real message of the person placed in a language model's prompt to show their writing.
- **Scope**: Includes random, topic-matched and situation-matched examples, and negatives (his rejections with reasons). Excludes messages used to fine-tune.
- **Aliases**: in-context example, example message, shot
- **Example**: [written-methods.md](https://github.com/jburnhams/voice-research/blob/d02cddc/written-methods.md), §1, prompting.
- **Near miss**: A retrieved item: also placed in the prompt, but chosen by a search over the archive; an example chosen that way is both.
- **Kind**: thing
- **Related**: `retrieval`
- **Status**: approved
- **Warrant**: few-shot, in-context 68 / 24; example 189 (all senses)
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### retrieval (`retrieval`)

- **Definition**: Retrieval is a step that chooses items from a person's archive by a search and puts them in a language model's prompt.
- **Scope**: Includes BM25 and embedding search, RAG, and situation-matched retrieval (medium, relationship, intent). Excludes putting the whole archive in a long context.
- **Aliases**: RAG, retrieval-augmented generation
- **Example**: [written-methods.md](https://github.com/jburnhams/voice-research/blob/d02cddc/written-methods.md), §2, retrieval and long context.
- **Near miss**: Long context: every message goes in, nothing is chosen.
- **Kind**: happening
- **Related**: `few-shot-example`
- **Status**: approved
- **Warrant**: retriev-, RAG 160 / 25
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### held-out set (`held-out-set`)

- **Definition**: A held-out set is a body of real data set aside before any training or selection, used only to test.
- **Scope**: Includes held-out takes chosen by text and session, held-out messages on a chronological, thread-grouped split, and intelligibility lists. Excludes data used as a reference clip, prompt or training data.
- **Aliases**: test set, eval set, held-out takes
- **Example**: [spoken-acquisition.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-acquisition.md), "freeze the held-out set first".
- **Near miss**: A benchmark: a published test set for comparing models, not his own data.
- **Kind**: thing
- **Related**: `leakage`
- **Status**: approved
- **Warrant**: held-out 105 / 70; split 96; test set 47
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### leakage (`leakage`)

- **Definition**: Leakage is a fault in which test data, or information from it, reaches training, references or prompts.
- **Scope**: Includes random splits that put the same thread in both halves, prompts that contain the real message's first sentence, and active learning that selects from the held-out set. Excludes a model leaking personal details (`memorisation`).
- **Aliases**: data leakage, contamination, test leakage
- **Example**: [written-evaluation.md](https://github.com/jburnhams/voice-research/blob/d02cddc/written-evaluation.md), §2, leakage and splits.
- **Near miss**: Memorisation: training text coming out of the model, a privacy fault, not a test fault.
- **Kind**: happening
- **Related**: `held-out-set`
- **Status**: approved
- **Warrant**: leak- 79 / 36
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### listening test (`listening-test`)

- **Definition**: A listening test is a test in which people listen to clips and rate or compare them.
- **Scope**: Includes MOS, CMOS, SMOS, MUSHRA, ACR, DCR and CCR tests, and Jonathan's own blind tests. Excludes text read and judged by people (a pairwise judgement can be either).
- **Aliases**: MOS test, subjective test, human evaluation, MUSHRA
- **Example**: [spoken-evaluation.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-evaluation.md), wording and scale move MOS.
- **Near miss**: DNSMOS: predicts a listening-test score, but no one listens; it is an automatic metric.
- **Kind**: thing
- **Status**: approved
- **Warrant**: listener 178; MOS 189; CMOS 44; MUSHRA 39
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### pairwise judgement (`pairwise-judgement`)

- **Definition**: A pairwise judgement is a judgement in which a person or model chooses the better of two outputs rather than scoring one.
- **Scope**: Includes A/B tests with ties, forced choice, CCR, and Elo over pairwise votes, by Jonathan, listeners or an LLM judge. Excludes absolute ratings (ACR, MOS).
- **Aliases**: A/B test, forced choice, pairwise comparison
- **Example**: [written-evaluation.md](https://github.com/jburnhams/voice-research/blob/d02cddc/written-evaluation.md), pairwise beats independent scores.
- **Near miss**: A MUSHRA trial: all versions side by side, but each is rated on a scale.
- **Kind**: happening
- **Status**: approved
- **Warrant**: A/B, pairwise, forced-choice 124 / 54
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### automatic metric (`automatic-metric`)

- **Definition**: An automatic metric is a score computed by a program or model from outputs, without a person judging.
- **Scope**: Includes WER and CER, speaker similarity, UTMOS, DNSMOS, LUAR, BLEU, BERTScore, MAUVE and AI-text detectors. Excludes LLM judges, which are asked a question in words (`llm-judge`).
- **Aliases**: metric, objective metric, automatic score
- **Example**: [spoken-dataset-qa.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-dataset-qa.md), automatic checks and their limits.
- **Near miss**: An LLM judge: also a model, but it answers a question in words.
- **Kind**: thing
- **Status**: approved
- **Warrant**: metric 151 / 62; WER 247
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### speaker similarity (`speaker-similarity`)

- **Definition**: Speaker similarity is an automatic metric that scores how close two clips' identity embeddings are.
- **Scope**: Includes SIM, SIM-o, SECS and SS, which differ by verifier and cannot be compared across papers. Excludes SMOS, a listening test of similarity.
- **Aliases**: SIM, SECS, SS, cosine similarity
- **Example**: [spoken-teachers.md](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-teachers.md), "similarity scores disagree with listeners".
- **Near miss**: SMOS: listeners rate similarity; a person judges.
- **Kind**: thing
- **Broader**: `automatic-metric`
- **Related**: `identity-embedding`
- **Status**: approved
- **Warrant**: speaker similarity, SIM, SECS, SS 190 / 45
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### LLM judge (`llm-judge`)

- **Definition**: An LLM judge is a role of a language model that is asked to rate or compare outputs.
- **Scope**: Includes pairwise and absolute judges, judges given examples (TICL), and critics in refinement loops when their score is used. Excludes automatic metrics and the model that generated the output judging itself without a separate call.
- **Aliases**: LLM-as-a-judge, LLM rater, LLM evaluator, judge model
- **Example**: [written-evaluation.md](https://github.com/jburnhams/voice-research/blob/d02cddc/written-evaluation.md), LLM judges: position bias and self-preference.
- **Near miss**: A critic in refinement: also an LLM rating output, but its job is to improve the draft, so it is part of `generation` unless its score is reported.
- **Kind**: role
- **Matches**: broadMatch `prompts:second-model`
- **Status**: approved
- **Warrant**: judge 264 / 34; LLM-as-a-judge
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### calibration (`calibration`)

- **Definition**: Calibration is a check of an automatic metric on Jonathan's own data before it is trusted.
- **Scope**: Includes the same-author ceiling (his held-out data against his other data), the cross-author floor (his correspondents or other speakers) and positive and negative controls. Excludes the calibration of a confidence score inside a model.
- **Aliases**: metric calibration, ceiling and floor
- **Example**: [written-evaluation.md](https://github.com/jburnhams/voice-research/blob/d02cddc/written-evaluation.md), "What we conclude" 2.
- **Near miss**: A baseline: a system to beat, not a check that the measure works.
- **Kind**: happening
- **Related**: `automatic-metric`
- **Status**: approved
- **Warrant**: ceiling, floor 75 / 25; calibrat-
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### eval (`eval`)

- **Definition**: An eval is a set of tasks with scoring that measures how well a model does a kind of work.
- **Scope**: Includes the repo's own experiment protocols with a fixed test set and measures. Excludes one-off checks on takes (`preparation`).
- **Aliases**: evaluation suite, test protocol
- **Example**: [voice-design/experiments.md](https://github.com/jburnhams/voice-research/blob/d02cddc/voice-design/experiments.md), the experiment plan.
- **Near miss**: A benchmark: an eval published for comparing models.
- **Kind**: thing
- **Matches**: exactMatch `prompts:eval`
- **Status**: approved
- **Warrant**: eval- 340 / 122 (evaluation, eval set)
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### benchmark (`benchmark`)

- **Definition**: A benchmark is an eval published for comparing models across groups.
- **Scope**: Includes Seed-TTS-eval, CV3-eval, LaMP and TSTBench. Excludes the project's own held-out set.
- **Aliases**: benchmark suite
- **Example**: [papers/tstbench/README.md](https://github.com/jburnhams/voice-research/blob/d02cddc/papers/tstbench/README.md), TSTBench.
- **Near miss**: A held-out set: his own data, never published.
- **Kind**: thing
- **Broader**: `eval`
- **Matches**: exactMatch `prompts:benchmark`
- **Status**: approved
- **Warrant**: benchmark 94 / 42
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### baseline (`baseline`)

- **Definition**: A baseline is a role of a system or method that a new one must beat in a comparison.
- **Scope**: Includes a fixed phonetic script, random few-shot prompting, Pocket TTS with his reference clip, and a neutral-only student. Excludes the real take or message used as a reference.
- **Aliases**: control condition, comparison system
- **Example**: [written-methods.md](https://github.com/jburnhams/voice-research/blob/d02cddc/written-methods.md), "baselines that must be in the matrix".
- **Near miss**: His real take as MUSHRA's hidden reference: the target, not a competitor.
- **Kind**: role
- **Status**: approved
- **Warrant**: baseline 156 / 82
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### watermark (`watermark`)

- **Definition**: A watermark is a signal hidden in generated audio or text that a detector can later read to show it was generated.
- **Scope**: Includes AudioSeal and WavMark, and a codec round trip that strips them. Excludes provenance records kept outside the output (manifests).
- **Aliases**: audio watermark, provenance mark
- **Example**: [papers/audioseal/README.md](https://github.com/jburnhams/voice-research/blob/d02cddc/papers/audioseal/README.md), AudioSeal.
- **Near miss**: A dataset manifest: records where data came from, but outside the audio.
- **Kind**: thing
- **Status**: approved
- **Warrant**: watermark 42 / 9; provenance 15
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

### memorisation (`memorisation`)

- **Definition**: Memorisation is a fault in which a trained model stores parts of its training text and can reproduce them.
- **Scope**: Includes verbatim extraction, recovery of masked names and leakage of correspondents' personal details. Excludes test data reaching training (`leakage`).
- **Aliases**: memorization, training-data extraction, PII leakage
- **Example**: [written-methods.md](https://github.com/jburnhams/voice-research/blob/d02cddc/written-methods.md), §5, privacy when training on a private archive.
- **Near miss**: Leakage: a fault in the test design, not a privacy fault of the model.
- **Kind**: happening
- **Status**: approved
- **Warrant**: memori- 43 / 9; PII
- **History**: 2026-11-27 added. 2026-11-27 approved (stage 1 round 1 and name test passed).

