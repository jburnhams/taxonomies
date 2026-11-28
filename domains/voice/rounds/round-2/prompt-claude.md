# Rater prompt: voice taxonomy, stage 1, round 2

You are classifying 40 items for a taxonomy agreement test. Use only the definitions below; do not look anything up, do not read any files, and do not use other knowledge of the repo they come from.

Each item comes from a research repo about cloning one person's voice (Jonathan's), spoken and written: making a small local text-to-speech model that sounds like him, and a writing assistant that writes like him. An item is either one source the repo has read (its title and one-line summary) or one finding or conclusion from a topic or design doc. Columns: `id`, `item`, `from` (the source folder or doc).

For every item, answer all three questions with exactly one value each. If no value fits, still pick the closest one and write `unsure` plus a few words in the note column.

Rules:
- Classify what the item itself says (the source's finding, or the doc's point), not the whole document it comes from. The `from` column is part of the item: `papers/`, `specs/` and `repos/` are sources; `spoken-*.md` and `written-*.md` are topic docs; `voice-design/` is the design. The text in [brackets] at the start of a finding names its doc and heading.
- area: the step of the work that would have to change to change the item. A tool, model or metric takes the area of what the item says it is used for: a quality score used to check Jonathan's own takes before training is `preparation`; used to judge a model's output is `evaluation`. Held-out sets, splits and leakage of test data are `evaluation`. Licences, privacy, memorisation, consent and watermarks are `governance`, even inside a teacher or evaluation doc. Model size, speed, runtime, cost and reproducibility are `operations`.
- modality: `spoken` for speech, `written` for text. A finding in a `spoken-*.md` or `written-*.md` doc takes that doc's voice unless it says it holds for both. Use `both` only when the item itself applies to the spoken and the written voice alike.
- trait: what part of the voice the item would change or measure. Who it sounds or reads like (timbre, accent, overall pitch range, authorship, speaker similarity): `identity`. How something is said or written in one situation (emotion, style, stance, per-style prosody, register, tone to an audience): `expression`. What is said (words, pronunciation errors, intelligibility, WER, meaning kept, phonetic coverage): `content`. Whether it sounds or reads as made by a person at all (artefacts, noise, fluency, naturalness MOS, AI detection): `naturalness`. Only if the item names no part of the voice at all (a licence, a runtime size, a privacy rule): `whole-voice`. A "style" embedding or score used to tell authors apart is `identity`.
- If an item names several things, classify the first one named.

Answer as CSV only, with this header and one row per item, in the items' order. Quote any note that contains a comma.

```
id,area,modality,trait,note
```

## The questions and their values

- **area**: Which part of the work is it about? Values: `governance`, `generation`, `preparation`, `elicitation`, `operations`, `evaluation`, `representation`
- **modality**: Which voice is it about? Values: `both`, `written`, `spoken`
- **trait**: Which part of the voice is it about? Values: `naturalness`, `whole-voice`, `content`, `expression`, `identity`

## Definitions of the values

### representation (`representation`)

- **Definition**: Representation is an area of the work that covers how a voice or a style is written down or encoded.
- **Scope**: Includes markup (SSML, EmotionML), emotion and stance vocabularies, style labels and tags, pronunciation lexicons, style and speaker embeddings, reference clips used as model inputs, and written style profiles. Excludes the model that reads them (`generation`).
- **Aliases**: style representation, style control
- **Near miss**: A teacher that takes a separate emotion reference: the model is `generation`; the separate input is `representation` when the item is about the input.
- **Kind**: thing
- **Facet**: `area`

### expression (`expression`)

- **Definition**: Expression is a trait of a voice that is how something is said or written in one situation.
- **Scope**: Includes emotion, style, stance, vocal events, prosody that varies by style, register and tone towards an audience, and style transfer. Excludes what stays the same across styles (`identity`).
- **Aliases**: delivery, register, tone, expressiveness
- **Near miss**: A style embedding used to verify authorship: it is called "style", but the question it answers is who wrote it, so `identity`.
- **Kind**: property
- **Facet**: `trait`

### operations (`operations`)

- **Definition**: Operations is an area of the work that covers running, rebuilding and paying for the voice models.
- **Scope**: Includes model and package size, speed and real-time factor, the runtime (CPU, browser, ONNX), quantisation, GPU hours and cost, manifests, versions and reproducibility. Excludes the choice of architecture for quality (`generation`).
- **Aliases**: deployment, cost, reproducibility
- **Near miss**: A student's parameter count quoted to compare quality: it is `generation` when the point is what the model can learn, `operations` when the point is whether it fits.
- **Kind**: thing
- **Facet**: `area`

### whole voice (`whole-voice`)

- **Definition**: Whole voice is a trait value for items about the voice as a whole, with no one part of it named.
- **Scope**: Includes licences and rights for a cloning model, runtime size and speed, privacy rules for the whole archive, and surveys that cover every part. Use it only when the item names no part and measures, changes or stores no quality of the output. An item that names a part only through a metric or a model still names it: WER and ROUGE are `content`, speaker similarity and a cloning model's voice input are `identity`, a judge recognising whose text it is is `identity`. Stored features (pitch, energy, durations) take the trait they are kept for, `expression` when the item does not say.
- **Aliases**: overall, all traits
- **Near miss**: A model release that clones from reference audio: it names no trait in words, but cloning a voice is `identity`. A small model's speed and size: `whole-voice`, since no quality of the output is named.
- **Kind**: property
- **Facet**: `trait`

### generation (`generation`)

- **Definition**: Generation is an area of the work that covers the models and methods that produce speech or text in the voice.
- **Scope**: Includes teachers and students, voice cloning, fine-tuning and adapters, synthetic data and voice conversion, vocoders, and for the written voice prompting with examples, retrieval, refinement and preference training. Excludes how inputs are encoded (`representation`) and judging the result (`evaluation`).
- **Aliases**: synthesis, training, modelling
- **Near miss**: A rule never to put teacher audio in the held-out set: it is about synthetic data, but its job is to protect the test, so it is `evaluation`.
- **Kind**: thing
- **Facet**: `area`

### identity (`identity`)

- **Definition**: Identity is a trait of a voice that makes it sound or read as one particular person.
- **Scope**: Includes timbre, accent, overall pitch range, idiolect and habits that stay when he changes style, speaker similarity, speaker verification and authorship. Excludes what changes with the style or the audience (`expression`).
- **Aliases**: speaker identity, authorship, sounds like me, timbre
- **Near miss**: His pitch when sarcastic: pitch is his, but the value that changes with the style is `expression`; his pitch range across all takes is `identity`.
- **Kind**: property
- **Facet**: `trait`

### naturalness (`naturalness`)

- **Definition**: Naturalness is a trait of a voice that is whether it sounds or reads as made by a person, apart from which person.
- **Scope**: Includes artefacts, noise and clipping, over-smoothing, fluency, MOS for naturalness or quality, and AI-text detection. Excludes whether it is his (`identity`).
- **Aliases**: quality, audio quality, fluency
- **Near miss**: A listening test asking "which sounds more like you?": a person judges, but the question is whose voice, so `identity`.
- **Kind**: property
- **Facet**: `trait`

### preparation (`preparation`)

- **Definition**: Preparation is an area of the work that covers turning raw takes and messages into training data.
- **Scope**: Includes transcripts, forced alignment, checks on each take (noise, clipping, wrong words), observed-style labels, cleaning and deduplication of messages, and what is kept out of the training pool. Excludes splitting off a held-out set (`evaluation`) and how a style is encoded as model input (`representation`).
- **Aliases**: dataset QA, data processing, annotation
- **Near miss**: A quality score such as DNSMOS: it is `preparation` when it filters takes before training, and `evaluation` when it scores a model's output.
- **Kind**: thing
- **Facet**: `area`

### both (`both`)

- **Definition**: Both is a modality value for items that apply to the spoken and the written voice alike, as written.
- **Scope**: Includes rules on held-out data and leakage, privacy and consent rules, judge biases and preference methods that the item applies to both, and the agendas' shared protocol. An item from a spoken or written doc is that doc's voice unless it says it holds for both.
- **Aliases**: shared, cross-modal
- **Near miss**: A finding about LLM judges in a written-voice doc: judges exist for audio too, but the item is about text, so it is `written`.
- **Kind**: thing
- **Facet**: `modality`

### evaluation (`evaluation`)

- **Definition**: Evaluation is an area of the work that covers judging how close the output is to the real voice.
- **Scope**: Includes listening tests, pairwise judgements, automatic metrics and their calibration, LLM judges, held-out sets, splits and leakage, baselines and benchmarks. Excludes checks on Jonathan's own takes before training (`preparation`).
- **Aliases**: assessment, testing
- **Near miss**: A watermark on every generated clip: it is listed beside the diagnostics, but it protects against misuse, so it is `governance`.
- **Kind**: thing
- **Facet**: `area`

### content (`content`)

- **Definition**: Content is a trait of a voice that is what is said: the words and their meaning.
- **Scope**: Includes the words spoken or written, pronunciation and lexicons, intelligibility and WER, phonetic coverage, and whether a draft keeps the facts of its brief. Excludes accent, which is how he pronounces (`identity`).
- **Aliases**: content fidelity, intelligibility, pronunciation
- **Near miss**: A British word list (BATH/TRAP, T-glottalling): it tests words, but the point is how he says them, so `identity`.
- **Kind**: property
- **Facet**: `trait`

### governance (`governance`)

- **Definition**: Governance is an area of the work that covers the rights to the voice data and models and their protection from misuse.
- **Scope**: Includes privacy of the archive, memorisation and leakage of personal details by a trained model, consent, licences of teachers, corpora and providers, watermarks and provenance. Excludes leakage of test data into training (`evaluation`).
- **Aliases**: privacy, safety, data governance
- **Near miss**: A licence that forbids training on a teacher's outputs: it decides which teacher is usable, but it is a right, so it is `governance` even inside a teacher comparison.
- **Kind**: thing
- **Facet**: `area`

### written (`written`)

- **Definition**: Written is a modality value for items about Jonathan's voice as writing.
- **Scope**: Includes his messages and emails, writing style, authorship, text generation with language models and text metrics.
- **Aliases**: text, writing, written voice
- **Near miss**: A paper on LLM judges of writing style: it is about text, so `written`, unless the item says the same bias holds for audio.
- **Kind**: thing
- **Facet**: `modality`

### elicitation (`elicitation`)

- **Definition**: Elicitation is an area of the work that covers what Jonathan is asked to record or write, and how he is asked.
- **Scope**: Includes recording prompts and scripts, coverage of sounds and styles, coaching and demonstrations, recording sessions and their order, and choosing what to record next (active learning). Excludes what is done with a take once recorded (`preparation`).
- **Aliases**: recording design, script design, data collection
- **Near miss**: A held-out intelligibility list such as the Harvard sentences: he reads it, but it is chosen to test the output, so it is `evaluation` when the point is the test.
- **Kind**: thing
- **Facet**: `area`

### spoken (`spoken`)

- **Definition**: Spoken is a modality value for items about Jonathan's voice as speech.
- **Scope**: Includes recordings, text-to-speech, voice cloning, markup for speech, listening tests and speech metrics.
- **Aliases**: speech, spoken voice, audio
- **Near miss**: An LLM writing the recording prompts: the LLM writes text, but the item is about what he reads aloud, so it is `spoken`.
- **Kind**: thing
- **Facet**: `modality`

## Items

```csv
id,item,from
h01,"Harvard Sentences (IEEE 1969 Revised List of Phonetically Balanced Sentences): 720 short, simple declarative sentences (72 lists of 10) built for listening tests, not for coverage per second: useful to us as a fixed, public intelligibility test set and a standard-script baseline, not as the main reading material.",specs/harvard-sentences/
h02,"[How much of Jonathan's speech is needed? / Identity saturates early] Language adaptation: two speakers × 50 utterances beat 20 × 5 for similarity; about 20 samples overfit (arxiv-2406.08911). The survey reads the general pattern the same way: fast gains to about 20 sentences, then slow (neural-tts-survey).",spoken-data-amount.md
h03,"[Choosing what to record next: ranking and active learning / What we conclude] Log the acquisition system's own cost (writer calls, synthesis, GPU minutes) alongside human seconds; the spec asks for it and no source reports it.",spoken-acquisition.md
h04,"A Deep Metric Learning Approach to Account Linking: One short post does not identify its author; an embedding of up to 16 posts by the same account does (EER about 0.13), so authorship scores for Jonathan's drafts must be computed over groups of messages, not one.",papers/account-linking/
h05,"[Evaluating a written voice / Authorship embeddings (LUAR and relatives)] They can learn topic instead of style: without same-conversation negatives, verification AUC is 0.79 on random pairs but 0.58 on same-conversation pairs (style-embeddings). They read apostrophes, lower-case ""i"", missing final punctuation and line breaks, so text must be kept exactly as written.",written-evaluation.md
h06,"Computational Sociolinguistics: A Survey: A survey of computational work on language as social behaviour: speakers have agency and shift style by addressee, topic and setting (""there are no single-style speakers""), so per-person models must condition on audience and relationship, and accommodation, power and politeness effects are measurable from text.",papers/computational-sociolinguistics/
h07,[Evaluating a written voice / LLM judges] Length: GPT-4 judges prefer longer text (dpo); LLM rewrites run 17.75–23.1% longer than human text (tstbench).,written-evaluation.md
h08,"Towards Controllable Speech Synthesis in the Era of Large Language Models: A Systematic Survey: A map of about 100 controllable TTS systems sorted by control strategy (style tags → reference speech → natural-language descriptions → LLM instructions), whose one original experiment shows that UTMOS and NISQA do not track human ratings of expressive, ...",papers/controllable-tts-survey/
h09,"[Evaluating the spoken voice / What we conclude] Held-out real takes chosen by text and session before training, never used as teacher reference, synthetic prompt or training data; at least two sessions' worth, every style present.",spoken-evaluation.md
h10,"[What should Jonathan read? Script design and emotion elicitation / 2. Expression: read, acted or spontaneous] Stances come from scenarios.",spoken-elicitation.md
h11,"Style Tokens: Unsupervised Style Modeling, Control and Transfer in End-to-End Speech Synthesis: A small bank of learned ""style tokens"" (10 by default), trained with no labels from a reference encoder, picks up speed, pitch level, animation and even noise or speaker as separate soft factors; tokens can be selected, scaled (including negative values) and ...",papers/global-style-tokens/
h12,"[What should Jonathan read? Script design and emotion elicitation / 4. What we conclude] Record parallel sets: the same neutral-content sentence in neutral and in each target style, back to back, plus emotion-congruent sentences.",spoken-elicitation.md
h13,"Self- and Other-Labels Induce Bidirectional Bias in LLM Judges: When style is removed from what is judged, measured self-preference vanishes once quality and judge severity are controlled, but simply telling a judge ""this is your own"" or ""this is from another model"" moves scores on identical material by about 0.43 points on a 7-point scale.",papers/emnlp26-findings-1571/
h14,"[Spoken voice: the pipeline, reviewed against the evidence / Changes this asks of the spec] §7.1: the utility formula needs a calibrated student_error; until then rank on coverage and style gaps only, and keep a random arm.",voice-design/spoken.md
h15,"[Audience, medium and time: why one person has many written voices / What we conclude] Keep raw text exactly as sent; redaction replaces names with consistent placeholders and touches nothing else.",written-context.md
h16,"Voice and sound with Speech Synthesis Markup Language (SSML), Azure Speech: Azure's SSML extends W3C SSML with mstts:express-as (one style, an optional styledegree from 0.01 to 2 and an optional role, at sentence level, for a subset of voices) and, for HD voices, with inline [style] markers from a list of 62 styles that includes ...",specs/azure-ssml-voice/
h17,"[Synthetic augmentation: how much teacher audio, and how to keep it honest / Evidence] Splicing real speech is augmentation too. Joining real utterances at constituent boundaries, with a join tag, cut WER from 1.00 to 0.19 at 5 h; without the tag there was no gain (distribution-augmentation). This needs word and phone alignments.",spoken-synthetic-augmentation.md
h18,"ITU-T Recommendation P.800: Methods for subjective determination of transmission quality: P.800 is where ""MOS"" comes from: a five-point Absolute Category Rating (Excellent 5 to Bad 1) of short groups of unrelated 2–3 s sentences from several male and female talkers, with reference conditions in every test, sessions under 20 minutes, means with ...",specs/itu-p800/
h19,"[How much of Jonathan's speech is needed? / Identity saturates early] Zero-shot teachers need only seconds, and similarity rises with prompt length (VALL-E 0.38 / 0.42 / 0.48 for 3 / 5 / 10 s) (vall-e).",spoken-data-amount.md
h20,"[Evaluating the spoken voice / What we conclude] Fixed protocol: question wording, scale, number of clips and listeners written in the experiment before it runs; report confidence intervals per condition.",spoken-evaluation.md
h21,"The CMU Arctic speech databases: Counting diphones with stress and across word boundaries, even the 168K-sentence source pool misses 123 of 1,655 possible unstressed diphones, and the authors argue the last rare diphones are not worth recording: back off instead.",papers/cmu-arctic-ssw5/
h22,"[Evaluating the spoken voice / Evidence] Standards: P.800 ACR, DCR and CCR, sessions of 20 minutes or less (itu-p800); P.808 asks at least 8 ratings per stimulus, about 96 votes per condition, gold and trap questions, and recommends CCR for close systems (itu-p808); MUSHRA uses a hidden reference and anchors, at most 12 stimuli per trial, ...",spoken-evaluation.md
h23,"CosyVoice 2: Scalable Streaming Speech Synthesis with Large Language Models: CosyVoice 2 (Qwen2.5-0.5B LM plus a chunk-aware flow-matching decoder) merges zero-shot cloning and instructions (emotion, rate, dialect, role, [laughter], [breath], emphasis) in one model and shows speaker fine-tuning works from ""as few as 400 audio ...",papers/cosyvoice2/
h24,"[Written voice: the pipeline, reviewed against the evidence / Changes this asks of the design] §10: add the long-context baseline and the fact-perturbation set for content fidelity (mind-the-style-gap); never BLEU or AI detectors (stylobench-feature-inversion).",voice-design/written.md
h25,"[Checking each take: transcripts, alignment, speaker and quality / What we conclude] Emotion classifiers describe, never gate: the observed style comes from Jonathan or a listener.",spoken-dataset-qa.md
h26,"Toward Data-Efficient Speech Synthesis: Active Learning-Based Corpus Construction for Multi-Speaker Text-to-Speech Synthesis: Model-aware acquisition (add data only for speakers the current model synthesises badly) beat both quality-filtered random sampling and diversity-maximising core-set selection at the same data budget, on two architectures.",papers/seki-data-efficient-tts/
h27,[Evaluating a written voice / 2. Leakage and splits] Topic-matched examples hurt imitation (Enron top-5 attribution 69.3 → 36.0) (catch-me-if-you-can).,written-evaluation.md
h28,"Active Learning for Text-to-Speech Synthesis with Informative Sample Collection: ""Skip what the current model already synthesises well, keep what it fails on"" (train, try zero-shot on the candidate's speaker, drop it if the output already passes a quality bar) beat a same-sized quality-only selection: 71.0% vs 66.6% of speakers above the bar (Table I).",papers/active-learning-tts/
h29,"[Evaluating a written voice / Humans, and which question to ask] Pairwise judgements beat independent scores, for humans and LLMs: a TICL judge given five examples picked the real author 89.5% of the time against 55% for a 1–5 rating (ticl); Apple's study reached the same conclusion for LLM judges (evaluating-evaluators, abstract only).",written-evaluation.md
h30,"[The small student: what model runs locally / What we conclude] Add an utterance-level style input (a learned embedding per style plus intensity, and optionally a reference-clip embedding of his own) at the encoder and the duration/pitch/energy predictors; then test span-level control.",spoken-student.md
h31,"LaMP: When Large Language Models Meet Personalization: Retrieving a few of the user's own past items into the prompt helps every short personalised generation task, and which retriever wins depends on the task (BM25 for email subjects, dense Contriever for most others, recency sometimes), but LaMP's generation ...",papers/lamp/
h32,"[Representing and controlling style: markup, vocabularies, labels and model inputs / Labels and descriptions] Rich captions from machine-measured attributes (SNR, C50, pitch, rate, binned in 7) are what Parler-TTS trains on; generated accent matched 68% of the time (parler-tts-guidance).",spoken-style-representation.md
h33,"FastSpeech 2: Fast and High-Quality End-to-End Text to Speech: Feeding the model explicit phoneme duration (from Montreal Forced Aligner), frame pitch (as a wavelet spectrogram) and energy during training, and predicting them at inference, beats distillation-based FastSpeech and autoregressive models on LJ Speech with a ...",papers/fastspeech2/
h34,"[Checking each take: transcripts, alignment, speaker and quality / Evidence] Speaker. ECAPA-TDNN reaches EER 0.87–2.12% and WavLM-ECAPA 0.62–1.32%, both after score normalisation; neither paper gives a meaning for a raw cosine, and the two scales are not comparable (ecapa-tdnn, wavlm). Similarity measured against the training clip can reward channel copying (lorp-tts).",spoken-dataset-qa.md
h35,"[How much of Jonathan's speech is needed? / What we conclude] Record clean: one clean sample beats hours of mixed-quality found audio for adaptation, so found recordings are gated before they are used as training data (lorp-tts).",spoken-data-amount.md
h36,Expressive speech synthesis in MARY TTS using audiobook data and EmotionML: The one working implementation of EmotionML-driven synthesis we have found maps EmotionML categories onto a single arousal value (e.g.,papers/mary-emotionml-audiobooks/
h37,"[Synthetic augmentation: how much teacher audio, and how to keep it honest / Evidence] Model collapse. Training on generated data loses the tails first; keeping 10% real limits the loss; accumulate rather than replace (model-collapse). The tails are exactly his unusual prosody.",spoken-synthetic-augmentation.md
h38,"Piper (piper1-gpl GitHub README): ""A fast and local neural text-to-speech engine that embeds espeak-ng for phonemization"", used by Home Assistant and NVDA; the stored README is a link page and gives no architecture, size, speed or data figures, so nearly everything useful about Piper sits in docs we have not stored.",repos/piper/
h39,"[Data collection: what to record and keep now / 1.2 How each prompt is given] Parallel block: the same neutral-content sentence in neutral and then each style, back to back, so pairs exist (emoknob, esd-emotional-vc); plus emotion-congruent sentences.",voice-design/data-collection.md
h40,[Evaluating a written voice / 3. What we conclude] Aggregate authorship scores over five or more messages per condition.,written-evaluation.md
```
