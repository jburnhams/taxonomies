# Rater prompt: voice taxonomy, stage 1, round 1

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

- **area**: Which part of the work is it about? Values: `elicitation`, `representation`, `governance`, `operations`, `evaluation`, `preparation`, `generation`
- **modality**: Which voice is it about? Values: `both`, `spoken`, `written`
- **trait**: Which part of the voice is it about? Values: `whole-voice`, `identity`, `expression`, `content`, `naturalness`

## Definitions of the values

### evaluation (`evaluation`)

- **Definition**: Evaluation is an area of the work that covers judging how close the output is to the real voice.
- **Scope**: Includes listening tests, pairwise judgements, automatic metrics and their calibration, LLM judges, held-out sets, splits and leakage, baselines and benchmarks. Excludes checks on Jonathan's own takes before training (`preparation`).
- **Aliases**: assessment, testing
- **Near miss**: A watermark on every generated clip: it is listed beside the diagnostics, but it protects against misuse, so it is `governance`.
- **Kind**: thing
- **Facet**: `area`

### operations (`operations`)

- **Definition**: Operations is an area of the work that covers running, rebuilding and paying for the voice models.
- **Scope**: Includes model and package size, speed and real-time factor, the runtime (CPU, browser, ONNX), quantisation, GPU hours and cost, manifests, versions and reproducibility. Excludes the choice of architecture for quality (`generation`).
- **Aliases**: deployment, cost, reproducibility
- **Near miss**: A student's parameter count quoted to compare quality: it is `generation` when the point is what the model can learn, `operations` when the point is whether it fits.
- **Kind**: thing
- **Facet**: `area`

### naturalness (`naturalness`)

- **Definition**: Naturalness is a trait of a voice that is whether it sounds or reads as made by a person, apart from which person.
- **Scope**: Includes artefacts, noise and clipping, over-smoothing, fluency, MOS for naturalness or quality, and AI-text detection. Excludes whether it is his (`identity`).
- **Aliases**: quality, audio quality, fluency
- **Near miss**: A listening test asking "which sounds more like you?": a person judges, but the question is whose voice, so `identity`.
- **Kind**: property
- **Facet**: `trait`

### written (`written`)

- **Definition**: Written is a modality value for items about Jonathan's voice as writing.
- **Scope**: Includes his messages and emails, writing style, authorship, text generation with language models and text metrics.
- **Aliases**: text, writing, written voice
- **Near miss**: A paper on LLM judges of writing style: it is about text, so `written`, unless the item says the same bias holds for audio.
- **Kind**: thing
- **Facet**: `modality`

### identity (`identity`)

- **Definition**: Identity is a trait of a voice that makes it sound or read as one particular person.
- **Scope**: Includes timbre, accent, overall pitch range, idiolect and habits that stay when he changes style, speaker similarity, speaker verification and authorship. Excludes what changes with the style or the audience (`expression`).
- **Aliases**: speaker identity, authorship, sounds like me, timbre
- **Near miss**: His pitch when sarcastic: pitch is his, but the value that changes with the style is `expression`; his pitch range across all takes is `identity`.
- **Kind**: property
- **Facet**: `trait`

### content (`content`)

- **Definition**: Content is a trait of a voice that is what is said: the words and their meaning.
- **Scope**: Includes the words spoken or written, pronunciation and lexicons, intelligibility and WER, phonetic coverage, and whether a draft keeps the facts of its brief. Excludes accent, which is how he pronounces (`identity`).
- **Aliases**: content fidelity, intelligibility, pronunciation
- **Near miss**: A British word list (BATH/TRAP, T-glottalling): it tests words, but the point is how he says them, so `identity`.
- **Kind**: property
- **Facet**: `trait`

### whole voice (`whole-voice`)

- **Definition**: Whole voice is a trait value for items about the voice as a whole, with no one part of it named.
- **Scope**: Includes licences and rights for a cloning model, runtime size and speed, privacy rules for the whole archive, and surveys that cover every part. Use it only when the item names no part; a bundle takes the first part it names.
- **Aliases**: overall, all traits
- **Near miss**: Voice cloning in general: if the item says the clone keeps his timbre, it names a part, so `identity`.
- **Kind**: property
- **Facet**: `trait`

### representation (`representation`)

- **Definition**: Representation is an area of the work that covers how a voice or a style is written down or encoded.
- **Scope**: Includes markup (SSML, EmotionML), emotion and stance vocabularies, style labels and tags, pronunciation lexicons, style and speaker embeddings, reference clips used as model inputs, and written style profiles. Excludes the model that reads them (`generation`).
- **Aliases**: style representation, style control
- **Near miss**: A teacher that takes a separate emotion reference: the model is `generation`; the separate input is `representation` when the item is about the input.
- **Kind**: thing
- **Facet**: `area`

### spoken (`spoken`)

- **Definition**: Spoken is a modality value for items about Jonathan's voice as speech.
- **Scope**: Includes recordings, text-to-speech, voice cloning, markup for speech, listening tests and speech metrics.
- **Aliases**: speech, spoken voice, audio
- **Near miss**: An LLM writing the recording prompts: the LLM writes text, but the item is about what he reads aloud, so it is `spoken`.
- **Kind**: thing
- **Facet**: `modality`

### elicitation (`elicitation`)

- **Definition**: Elicitation is an area of the work that covers what Jonathan is asked to record or write, and how he is asked.
- **Scope**: Includes recording prompts and scripts, coverage of sounds and styles, coaching and demonstrations, recording sessions and their order, and choosing what to record next (active learning). Excludes what is done with a take once recorded (`preparation`).
- **Aliases**: recording design, script design, data collection
- **Near miss**: A held-out intelligibility list such as the Harvard sentences: he reads it, but it is chosen to test the output, so it is `evaluation` when the point is the test.
- **Kind**: thing
- **Facet**: `area`

### expression (`expression`)

- **Definition**: Expression is a trait of a voice that is how something is said or written in one situation.
- **Scope**: Includes emotion, style, stance, vocal events, prosody that varies by style, register and tone towards an audience, and style transfer. Excludes what stays the same across styles (`identity`).
- **Aliases**: delivery, register, tone, expressiveness
- **Near miss**: A style embedding used to verify authorship: it is called "style", but the question it answers is who wrote it, so `identity`.
- **Kind**: property
- **Facet**: `trait`

### governance (`governance`)

- **Definition**: Governance is an area of the work that covers the rights to the voice data and models and their protection from misuse.
- **Scope**: Includes privacy of the archive, memorisation and leakage of personal details by a trained model, consent, licences of teachers, corpora and providers, watermarks and provenance. Excludes leakage of test data into training (`evaluation`).
- **Aliases**: privacy, safety, data governance
- **Near miss**: A licence that forbids training on a teacher's outputs: it decides which teacher is usable, but it is a right, so it is `governance` even inside a teacher comparison.
- **Kind**: thing
- **Facet**: `area`

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

### generation (`generation`)

- **Definition**: Generation is an area of the work that covers the models and methods that produce speech or text in the voice.
- **Scope**: Includes teachers and students, voice cloning, fine-tuning and adapters, synthetic data and voice conversion, vocoders, and for the written voice prompting with examples, retrieval, refinement and preference training. Excludes how inputs are encoded (`representation`) and judging the result (`evaluation`).
- **Aliases**: synthesis, training, modelling
- **Near miss**: A rule never to put teacher audio in the held-out set: it is about synthetic data, but its job is to protect the test, so it is `evaluation`.
- **Kind**: thing
- **Facet**: `area`

## Items

```csv
id,item,from
r01,"Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech (VITS): One end-to-end model (VAE + normalising flow + HiFi-GAN decoder + stochastic duration predictor) reaches MOS 4.43 against 4.46 for recordings on LJ Speech and equals recordings on VCTK (4.38 vs 4.38), with speaker identity as a single global embedding, and it is the architecture under Piper.",papers/vits/
r02,"[Representing and controlling style: markup, vocabularies, labels and model inputs / Model inputs] Emotion directions in speaker-embedding space (mean emotional minus neutral, α 0.4) give 86% emotion selection accuracy with similarity 0.705 vs 0.719; sarcasm only 61% (emoknob). That needs back-to-back neutral/styled pairs.",spoken-style-representation.md
r03,"[The small student: what model runs locally / Evidence] Pocket TTS: 100M and smaller 18.2M / 6.9M / 1.9M English variants, about 6× real time on 2 CPU cores, clones from a WAV prompt and reproduces its recording quality; no quality numbers; licence not stated (pocket-tts).",spoken-student.md
r04,"Panza: Design and Analysis of a Fully-Local Personalized Text Writing Assistant: Fine-tuning a 7–8B model on (LLM-written instruction, real sent email) pairs, ""reverse instructions"", makes its output match the user's email style (MAUVE about 0.9) where the same model with retrieval, and GPT-4o given the whole email history, do not (MAUVE ...",papers/panza-arxiv/
r05,[How much of Jonathan's speech is needed? / Identity saturates early] AdaSpeech: 20 sentences (about a minute) adapting the speaker embedding and conditional layer norm match full decoder fine-tuning (MOS 3.39 vs 3.35); quality drops below 10 sentences; a mismatch in recording conditions costs 0.30–0.35 MOS (adaspeech).,spoken-data-amount.md
r06,"The Mirror to Our Soul? Comparisons of Spontaneous and Posed Vocal Expression of Emotion: Even at matched intensity, listeners rate spontaneous vocal emotion as more genuine than posed (3.45 vs 2.66 on 0–4), yet the acoustic differences are few and subtle (posed happiness has wider pitch range, posed anger more jitter), and high-intensity ...",papers/spontaneous-vs-posed-vocal-emotion/
r07,"[Evaluating a written voice / LLM judges] Shared extractor bias: when a judge extracts traits the same way the method does, the method beats the real author on the judge's score (0.542 vs 0.427), and the judge's score has no correlation with LUAR (r 0.013) (personalbench).",written-evaluation.md
r08,"[Evaluating a written voice / LLM judges] Self-preference: a model recognises its own text 73.5% of the time and favours it (self-preference); content alone identifies the source model 50.7% of the time against 10% chance, so hiding the label is not enough (emnlp26-findings-1571).",written-evaluation.md
r09,"WavMark: Watermarking for Audio Generation: WavMark hides 32 bits in each 1 s of 16 kHz audio with an invertible network, repeating the mark across the file. Of the 32 bits, 10 are a pattern used to find each segment and 22 are payload.",papers/wavmark/
r10,"[Generating text in one person's voice: prompting, retrieval, refinement, training / 4. Training] Adapter mechanics: LoRA rank 1–4 suffices (lora); QLoRA matches 16-bit, needs adapters on all linear layers, loss on the response only, and data quality beats quantity (qlora); RoSA beats LoRA on maths and data-to-text but not instruction tuning, 1.9x slower (rosa).",written-methods.md
r11,"LongLaMP: A Benchmark for Personalized Long-form Text Generation: For email completion, retrieving four of the sender's own past emails into a 7B model's prompt nearly doubles ROUGE-1 (0.177 → 0.349), by far the largest gain of the four long-form tasks; but the input already contains 20–30% of the target email and scoring ...",papers/longlamp/
r12,[How much of Jonathan's speech is needed? / Expression does not saturate early] 15 minutes of expressive speech alone gave only neutral speech (style score 58.1 vs neutral 56.0); with 4–7 h of voice-converted expressive data from another speaker and a final fine-tune on the real data it reached 67.7.,spoken-data-amount.md
r13,[Evaluating a written voice / 2. Leakage and splits] A prompt that contains the first sentence of the real message raises the same-author rate from 22% to 50% (personalbench); llms-imitate-style is not evidence because its prompts reuse paragraphs of the reference.,written-evaluation.md
r14,"Unisyn Lexicon Release, version 1.3: Unisyn is an English pronunciation lexicon written once in accent-neutral ""keysymbols"" and turned into specific UK, US, Australian and New Zealand accents (down to town and speaker level) by perl rule scripts, with SAMPA or IPA output: the natural source for ...",specs/unisyn-lexicon/
r15,"[Evaluating the spoken voice / Evidence] Expression: the right test is forced-choice emotion identification plus ""real or acted?"" with unbiased hit rates (acting-experience-vocal-emotion); genuineness is a separate scale from intensity (spontaneous-vs-posed-vocal-emotion); a style can be recognised and still be the teacher's generic version (H3), so compare with his own take of the same style.",spoken-evaluation.md
r16,"The Geneva Minimalistic Acoustic Parameter Set (GeMAPS) for Voice Research and Affective Computing: eGeMAPS is a fixed, documented set of 88 interpretable voice parameters (pitch in semitones, loudness, jitter, shimmer, HNR, formants, spectral balance, MFCC 1–4, voiced and pause timing) that matches 6,000-feature sets on arousal (79.7% vs 78.0% UAR) but ...",papers/egemaps/
r17,"[Synthetic augmentation: how much teacher audio, and how to keep it honest / What we conclude] Filters: WER with an en-GB normaliser (looser for expressive), forced-alignment plausibility, duration and rate outliers, speaker similarity to held-out real takes on a calibrated verifier, pitch distribution per style against his, and too-high similarity to one reference (copying).",spoken-synthetic-augmentation.md
r18,"[Generating text in one person's voice: prompting, retrieval, refinement, training / 6. What we conclude] Privacy gates for any trained model: strip quotes and signatures, dedupe within threads, replace third-party names with consistent placeholders, audit with a fine-tuned/base perplexity ratio before use.",written-methods.md
r19,"EmoV-DB (repository README): The released corpus is four English speakers (Spk-No's French data is not listed), downloadable from OpenSLR 115, with a Montreal Forced Aligner recipe that trims nonverbal sounds before and after each sentence.",repos/emov-db/
r20,"[The small student: what model runs locally / What we conclude] Store what this family needs: forced-alignment durations, F0 with voicing, and energy for every take, from audio kept lossless at 24 kHz or above, without heavy denoising, with its gain recorded.",spoken-student.md
r21,"Matcha-TTS: A Fast TTS Architecture with Conditional Flow Matching: An 18.2M-parameter acoustic model trained with optimal-transport flow matching speaks well in 2 to 4 ODE steps (MOS 3.77 at 4 steps vs VITS 3.71 and FastSpeech 2 3.29, WER 2.15%) and needs only 4.8 GiB to train, the least of all systems compared; a ...",papers/matcha-tts/
r22,"[Choosing a teacher: which voice-cloning model makes the synthetic data / Findings that cut across teachers] Licences: Apache-2.0 for Qwen3-TTS (read) and CosyVoice (unchecked); the bilibili Model Use License for IndexTTS does not say whether outputs may train another model; F5-TTS and XTTS are non-commercial (unchecked). For a personal, local model this may not matter, but it decides what can be published.",spoken-teachers.md
r23,[Evaluating a written voice / 2. Leakage and splits] Random splits overstate: LaMP's best ROUGE-1 falls from 0.586 to 0.547 under a time split (lamp); Panza used a random 80/20 split (panza-arxiv).,written-evaluation.md
r24,"Residual Adapters for Few-Shot Text-to-Speech Speaker Adaptation: With a frozen 89M backbone trained on 243 h from 31 professional speakers, tiny residual adapters (0.1M parameters, 0.1%) in the decoder gave the same naturalness from 1, 5 or 30 minutes of a new neutral US speaker (MOS 4.42–4.46 female, 4.46–4.51 male, Table ...",papers/residual-adapters-tts/
r25,"[Checking each take: transcripts, alignment, speaker and quality / Evidence] Emotion. emotion2vec reaches about 72% on acted IEMOCAP and 82% on RAVDESS but 28% UA on natural MELD (emotion2vec); a style classifier fell from 92.5% (read) to 75.7% (improvised) and 27% on another corpus (expresso).",spoken-dataset-qa.md
r26,"What are neural text to speech HD voices? (Azure Speech): Azure's LLM-based HD voices come in three families (Dragon HD, Dragon HD Omni with 700+ voices and sampling knobs, and HD Flash), infer style from the text and take explicit style markers on English text, but drop most SSML control (no prosody, emphasis or break on Omni) and name no en-GB voice on this page.",specs/azure-hd-voices/
r27,"[Audience, medium and time: why one person has many written voices / Evidence] Power.",written-context.md
r28,[Choosing what to record next: ranking and active learning / Evidence] Active learning for TTS. Seki et al. keep the candidates the current model renders badly: 71.0% of speakers pass the quality bar vs 66.6% for quality-only and 42.6% for all data; UTMOS 2.60 vs 2.51 core-set vs 2.42 random.,spoken-acquisition.md
r29,"Towards End-to-End Prosody Transfer for Expressive Speech Synthesis with Tacotron: A 128-D reference embedding of the target audio makes Tacotron copy a reference's rhythm and pitch closely (""say it like this""), but it transfers pitch in absolute terms and leaks speaker identity: a speaker classifier heard the reference speaker in 61% of outputs and the intended target in only 21%.",papers/prosody-transfer-tacotron/
r30,"[Audience, medium and time: why one person has many written voices / What we conclude] Every sample keeps: medium, thread id, timestamp, the incoming message it answers, recipient id (an opaque id, not the name in the text), recipient count, and a relationship class (above / peer / below, close / distant), plus whether the message asks for something.",written-context.md
r31,"The Emotional Voices Database: Towards Controlling the Emotion Dimension in Voice Generation Systems: Actors read CMU Arctic sentences in five acted styles (neutral, amused, angry, sleepy, disgusted), one style per session, with speech-laughs, yawns and affect bursts encouraged: a few hundred sentences per style were enough for a small neutral-to-angry ...",papers/emov-db/
r32,"[Data collection: what to record and keep now / 1.2 How each prompt is given] Scenario card: two lines of situation, then the sentence; ""not your stage voice: imagine it and say it your way"" (acting-experience-vocal-emotion).",voice-design/data-collection.md
r33,"[How much of Jonathan's speech is needed? / What we conclude] Expressive speech: aim for 3–5 minutes per target style before synthesising it (the 15–30 min total in low-resource-expressive-da over 4–5 styles), split across sessions, and plan for augmentation and a real-only final fine-tune; never expect the style from real data alone at this size.",spoken-data-amount.md
r34,"Lina-Speech: Gated Linear Attention and Initial-State Tuning for Multi-Sample Prompting Text-To-Speech Synthesis: Instead of a few seconds of prompt audio, a recurrent (gated linear attention) TTS can absorb 45 s to 20 min of one speaker's or one style's recordings by tuning only a rank-1 initial state in under 20 s on an RTX 4090, and that raised listener-rated speaker ...",papers/arxiv-2410.23320/
r35,"[Data collection: what to record and keep now / 1.3 Recording conditions] Lossless, at least 24 kHz (48 kHz master is fine), no denoising or loudness normalisation applied to the master, gain recorded (libritts, vocos, hifigan).",voice-design/data-collection.md
r36,"ITU-T Recommendation P.808: Subjective evaluation of speech quality with a crowdsourcing approach: P.808 moves P.800's ACR, DCR and CCR tests online: workers pass a qualification job (hearing, language, device), a training job that expires, and short rating jobs of 5–15 stimuli with a headphone check, a fixed volume, and gold and trapping questions; it ...",specs/itu-p808/
r37,"[How much of Jonathan's speech is needed? / Identity saturates early] FastPitch + HiFi-GAN adaptation: MOS 2.81 at 1 min, 3.21 at 5 min, 3.40 at 30 min, 3.39 at 60 min, against real recordings at 3.94; speaking rate drifts at 1 min (16.3 vs 13.1 phones/s) and the vocoder needs fine-tuning too (arxiv-2110.05798).",spoken-data-amount.md
r38,[Choosing what to record next: ranking and active learning / Evidence] The same idea applied to LLM scripts.,spoken-acquisition.md
r39,"Qwen3-TTS (repository README): Only the five 12 Hz models are released (1.7B Base, CustomVoice, VoiceDesign; 0.6B Base, CustomVoice): Base clones from reference audio plus its transcript but takes no instruction, CustomVoice takes instructions but only for 9 preset voices, and fine-tuning instructions are in finetuning/.",repos/qwen3-tts/
r40,"[Evaluating the spoken voice / Evidence] Automatic metrics on expressive speech: UTMOS correlated −0.10 to −0.17 with humans, NISQA about 0, Gemini 0.12–0.17 (controllable-tts-survey); speaker similarity disagreed with SMOS (indextts2); see spoken-dataset-qa.md.",spoken-evaluation.md
```
