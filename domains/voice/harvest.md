# Voice taxonomy: harvest

**In one line**: the words voice-research uses for its concepts, with counts, grouped
into synonym sets and homonyms, and the existing vocabularies it already leans on
(process step 3).

**In plain words**: before choosing any word we counted how often each candidate is used,
which words name the same idea, and which word names more than one. The counts are the
"warrant" each glossary entry cites.

**How counted**: `grep -oiE` over the repo's own prose at `d02cddc`: the 24 root and
`voice-design/` docs and the 133 source READMEs (about 155,000 words; stored copies such
as `paper.txt` left out). A count is uses / files. Counts are of the word, all senses:
"take" counts the noun only by its usual neighbours (his take, real takes, each take);
"prompt" counts every sense, which is the point of homonym 1. Build-sample items
(`b01`-`b60`) were read for the senses.

## Counts (candidate words)

| Word | Uses / files | Note |
|---|---|---|
| style | 1,231 / 137 | the commonest concept word; several senses (homonym 3) |
| speaker | 822 / 90 | the person whose voice it is, and any person in a corpus |
| TTS | 649 / 92 | text-to-speech model or system |
| author | 535 / 142 | written-voice counterpart of speaker; also the paper's authors |
| emotion | 447 / 62 | EmotionML sense; overlaps style |
| prompt | 426 / 96 | three senses (homonym 1) |
| eval- | 340 / 122 | evaluation, eval set |
| fine-tun- | 329 / 78 | |
| LLM | 296 / 66 | "language model" 85 / 33 |
| reference | 293 / 82 | four senses (homonym 2); "reference clip/audio" 30 / 18 |
| take (noun) | 266 / 87 | one recording of one prompt by Jonathan |
| F0, pitch | 267 / 50 | |
| licence | 265 / 140 | every source README has a Licence line |
| judge | 264 / 34 | LLM judge; also Jonathan judging |
| WER | 247 / 58 | |
| expressi- | 228 / 63 | expression, expressive |
| teacher | 223 / 74 | the large cloning model that makes synthetic data |
| label | 216 / 75 | style label; data label |
| student | 206 / 80 | the small local model |
| embedding | 204 / 76 | speaker, style and authorship embeddings |
| align- | 191 / 55 | forced alignment |
| speaker similarity (SIM, SECS, SS) | 190 / 45 | |
| MOS | 189 / 46 | CMOS 44, MUSHRA 39 |
| example | 189 / 69 | few-shot examples, and the plain sense |
| dataset | 183 / 80 | corpus 164 / 65 |
| synthetic | 178 / 62 | augment- 85 / 31 |
| listener | 178 / 63 | rater 59 / 36 |
| accent | 177 / 56 | |
| recording | 175 / 73 | |
| naturalness | 162 / 65 | |
| retriev-, RAG | 160 / 25 | written voice |
| clip | 158 / 58 | |
| baseline | 156 / 82 | |
| utterance | 152 / 55 | |
| metric | 151 / 62 | |
| prosod- | 144 / 55 | |
| zero-shot | 137 / 45 | voice clon- 127 / 57 |
| preference | 134 / 36 | DPO 40 |
| message | 130 / 41 | written voice: one email or chat message |
| A/B, pairwise, forced-choice | 124 / 54 | |
| markup, SSML | 123 / 28 | EmotionML 97 / 29 |
| authorship | 117 / 32 | stylometr- 14 |
| tag | 118 / 23 | free-text style tag |
| session | 111 / 39 | recording session |
| profile | 111 / 32 | style profile |
| stance | 110 / 57 | project vocabulary: sarcastic, sympathetic, ... |
| verifier, verification | 107 / 38 | speaker and authorship verification |
| held-out | 105 / 70 | |
| split | 96 / 42 | |
| coverage | 96 / 36 | diphone 63 / 14 |
| benchmark | 94 / 42 | |
| privacy, private | 87 / 28 | memoris- 43 / 9 |
| vocal event (laugh, sigh, filler) | 85 / 29 | |
| leak- | 79 / 36 | |
| identity | 77 / 34 | timbre 36 / 17 |
| medium | 77 / 37 | audience 46, recipient 54, register 31 |
| transcript | 75 / 35 | |
| demonstration, demo | 71 / 34 | coach- 39 / 16 |
| lexicon | 70 / 16 | |
| vocoder | 68 / 34 | codec 28 |
| adaptation | 65 / 26 | adapter 78 / 18, LoRA 124 / 21 |
| few-shot, in-context | 68 / 24 | |
| active learning, acquisition | 58 / 16 | |
| voice conversion | 56 / 22 | |
| vocabular- | 56 / 23 | |
| script | 50 / 21 | |
| elicit- | 45 / 22 | |
| watermark | 42 / 9 | provenance 15 / 10, consent 10 / 8 |
| requested, observed | 30 / 13 | requested vs observed style |

## Synonym sets (several words, one concept)

1. **take**, recording, utterance, clip, sample: one recorded reading. "Utterance" and
   "clip" are the corpora's words (LibriTTS, ESD); "take" is the repo's own word for one
   of Jonathan's (`b11`, `b45`). "Recording" also means the act and the whole archive.
2. **reference clip**, reference audio, speaker prompt, audio prompt, prompt (audio),
   voice prompt: the clip a cloning model is given to copy (`b21`, `b59`).
3. **real data**, own data, genuine, human data: what Jonathan himself produced, as
   against synthetic data (`b01`, `b09`).
4. **synthetic data**, teacher data, generated audio, pseudo-labels, augmentation data
   (`b07`, `b37`).
5. **listening test**, MOS test, subjective test, human evaluation, CMOS, MUSHRA, A/B
   test (`b22`, `b25`, `b55`).
6. **LLM judge**, LLM-as-a-judge, LLM rater, LLM evaluator, judge (`b14`, `b34`, `b44`,
   `b60`).
7. **speaker similarity**, SIM, SIM-o, SECS, SS, cosine similarity (`b48`).
8. **fine-tuning**, SFT, speaker adaptation, adaptation, training on his data (`b49`).
9. **style profile**, profile, persona description, style description (`b26`).
10. **held-out set**, test set, eval set, held-out takes (`b18`, `b57`).
11. **coaching**, cue, emotional cue (label, emoji, colour, demo) (`b53`).

## Homonyms (one word, several concepts)

1. **prompt**: (a) the text Jonathan reads aloud (`b30`, `b42`, "prompt set"); (b) the
   reference clip given to a cloning model (`b21`, `b59`); (c) the text sent to a
   language model (`b26`, `b40`); (d) in the `prompts` context it is an alias of
   `context-window`. Fix: `recording prompt`, `reference clip`, and the `prompts` concept
   for (c) (see `map.md` and the clarify request there).
2. **reference**: a reference clip; a held-out real take used as the hidden reference in
   MUSHRA (`b22`); a "reference model" in DPO (`b51`); a citation. Fix: `reference clip`,
   `hidden reference`; the others are left to context.
3. **style**: (a) a named way of delivering (cheerful, whispering, sarcastic); (b) the
   whole written manner of one author, as in "style embedding", "style match" (`b02`,
   `b46`); (c) in "speaking style", everything that is not the words. Fix: `style` is (a);
   sense (b) is `identity` when it asks "who wrote this?" and `expression` when it asks
   "how is it said here?" (trait facet).
4. **session**: a recording session (voice); a harness session (`prompts:session`).
5. **transcript**: the words of a take (voice, `b54`); a run's record of turns
   (`prompts:transcript`).
6. **label**: a style label requested in coaching; a data label (transcript, phoneme,
   speaker); a value of a facet. Fix: `style label`.
7. **student / teacher**: also ordinary words in the elicitation papers ("acting
   students"); context settles it.

## Existing vocabularies (Z39.19 §11.1.1: reuse first)

- **W3C SSML 1.1, EmotionML 1.0 and the W3C emotion vocabularies**: element and category
  names are kept as identifiers (scope, out of scope). The "everyday" categories are the
  repo's emotion vocabulary ([`spoken-style-representation.md`](https://github.com/jburnhams/voice-research/blob/d02cddc/spoken-style-representation.md)).
- **The agendas' areas** (A markup, B elicitation, C active learning, D representation,
  E coaching, F teachers and augmentation, G student, H processing and QA, I evaluation,
  J governance, K cost and reproducibility) are the first draft of the `area` facet.
- **ITU-T P.800 / P.808 and ITU-R BS.1534**: the names of listening-test methods (ACR,
  DCR, CCR, MUSHRA) are kept as identifiers.
- **The `prompts` glossary**: looked up with `tools/term.py` on 2026-11-27. Found:
  `language-model` ("model"), `eval`, `benchmark`, `second-model` ("LLM judge" is an
  alias there), `session`, `transcript`. Not found: fine-tuning, few-shot examples,
  retrieval, dataset, adapter. "prompt" finds `context-window`, whose definition is a
  limit, not the text sent (homonym 1d).
