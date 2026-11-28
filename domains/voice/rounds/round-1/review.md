# Voice stage 1, round 1: competency questions (T10) and heuristic review (T11)

**In one line**: round 1 passed J23 on all three facets, and the name test passed at 95%.
All 13 competency questions can be answered from `facets.md` and `glossary.md`. The
review found no unmarked synonym and no missing facet, so stage 1 is adopted (G1;
Jonathan can veto).

Checked by Claude on 2026-11-27, against the files as changed after the name test.

## T10: competency questions

| # | Question | Answered by |
|---|---|---|
| 1 | Asked to record or write, or what is done afterwards? | `area` = `elicitation`, against the later areas in sequence order |
| 2 | Which findings apply to both voices? | `modality` = `both`, with its rule (a doc's voice unless the item says both) |
| 3 | Sounding like him, or how he says it? | `trait` = `identity` against `expression`, with the rule: what stays across styles against what changes |
| 4 | Privacy, consent, licences, provenance? | `area` = `governance`; terms `memorisation`, `watermark` |
| 5 | Take, recording, utterance, clip? | `take` (one of his readings of one prompt), with the others as aliases; utterance as the corpora's word in its near miss |
| 6 | Teacher, student, synthetic data? | `teacher` and `student` (roles), `synthetic-data` (what the teacher makes, kept labelled apart from `real-data`) |
| 7 | Recording prompt, reference clip, model prompt? | `recording-prompt` (text he reads) against `reference-clip` (audio a model copies); the model prompt is the `prompts` concept (`map.md`, request #20) |
| 8 | Requested and observed style; style, emotion, stance? | `requested-style` against `observed-style`; `style` (named delivery), `emotion` (W3C vocabulary), `stance` (project vocabulary) |
| 9 | Listening test, automatic metric, LLM judge? | the three entries, with near misses between them (DNSMOS, critics) |
| 10 | Held-out set and leakage? | `held-out-set` and `leakage`, with `memorisation` as the near miss |
| 11 | Zero-shot cloning, fine-tuning, adapter? | `zero-shot-cloning` (no weight change), `fine-tuning` (weights change), `adapter` (small added weights) |
| 12 | Retrieval, few-shot examples, style profile? | `retrieval` (chosen by search), `few-shot-example` (his real messages in the prompt), `style-profile` (a description of them) |
| 13 | Which words match `prompts` terms, and which only look alike? | `map.md`: exactMatch `eval` and `benchmark`, closeMatch `language-model`, broadMatch `llm-judge`; homonyms `session` and `transcript` |

All 13 are answered.

## T11: Z39.19 §11.2.2 review

- **Unmarked synonyms**: none. Every word in the harvest's 11 synonym sets is a preferred
  label or an alias of one entry, which T2 confirms. "prompt" is deliberately left with
  no entry (label choice 1).
- **Missing facets**: none. One three-way split (`r20`, stored prosodic features), which
  the `whole-voice` redefinition addresses. The `unsure` notes choose between existing
  values. No rater asked for a value outside set A.
- **Facet changes**: none in round 1. One value was relabelled (`demonstration` →
  "coaching demo") and three were redefined, which are not facet changes.
- **T7**: every item got a value in every facet. Unsorted holds 1 item (`r20`), within
  the limit of 3.
- **Out-of-date terms**: none. Harvested at voice-research `d02cddc` (2026-11-27).
- **Term form**: T3 flags only `operations`, which is kept, as in `prompts`.
- **Weakness to watch**: `modality` scored 1.00 with only 2 `both` items. Round 2 (the 40
  held items `h01`-`h40`) should check it on more items that apply to both voices, and
  retest the four `candidate` entries.
