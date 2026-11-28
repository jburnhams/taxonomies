# Voice stage 1, round 1: name test (T9) results

**In one line**: 59 of 62 labels pass (95%, target 80%). Each reader got 60 right
(97%). The three misses lead to one relabel and two scope changes.

Readers: GPT-6.2-Astra (`codex exec`) and Gemini 4 Carbon High (`agy -p`), each given only
[`prompt.md`](./prompt.md) in an empty folder. Replies are in `guesses-openai.md` and
`guesses-gemini.md`. Claude scored them on 2026-11-27: a guess passes when it fits the
entry's definition and does not take the near miss.

| Label | openai | gemini | What went wrong, and the fix |
|---|---|---|---|
| demonstration | miss | miss | Both read it as an example shown to *a model* or to him, which takes the few-shot near miss. **Relabel** "coaching demo" (ID `demonstration` kept), with "demonstration" kept as an alias. |
| coaching | pass | miss | Gemini read it as live direction and feedback during recording. **Redefine** the scope: a cue given with the prompt, before the take; feedback on a take is a retake request, not coaching. |
| style | miss | pass | OpenAI read "his characteristic way of expressing", which is the identity sense (harvest homonym 3). **Kept**: style has 1,231 uses (N6). Its near miss already covers this, and a new near miss names the habit sense. |

Every other label passed with both readers, including the four mapped to `prompts`
(`eval`, `benchmark`, `language model`, `LLM judge`). Two readers added something to a
correct guess that the scope excludes: "drafted by the assistant" for `message`, and
"for comparison by a listener" for `reference clip`. Their near misses already cover
both, so they count as passes.
