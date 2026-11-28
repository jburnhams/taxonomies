# Voice stage 1, round 2: name test (T9) results

**In one line**: 2 of the 4 retested labels pass with both readers. "Coaching" fails with
both and "coaching demo" with one, so both stay `candidate`. Across the stage, 60 of 62
labels have now passed (97%, target 80%).

Corrected 2026-11-28 after review on taxonomies#31: `coaching` was first scored a pass,
but both guesses describe feedback during the session, which its scope excludes and round 1
scored a miss.

| Label | openai | gemini | Note |
|---|---|---|---|
| coaching | miss ("giving him feedback during a recording session so he can adjust how he reads a line") | miss ("guidance and feedback ... across takes") | Both read it as feedback on takes, the sense the scope excludes; one round-1 reader did too. The word itself pulls that way, so a relabel (for example "style cue", from the alias "cue") is a label choice for Jonathan, to test in the next name test. |
| coaching demo | pass ("a sample reading he can listen to, to hear what the coach is asking for") | miss ("a walkthrough … of how the coaching process works") | Near miss added: one clip of a style, not a demo of the process. |
| style | pass | pass | Gemini added "characteristic phrasing", which leans towards `identity`; the near miss covers it. |
| whole voice | pass | pass | Both read "his overall voice, all parts together", which is the definition's first line. The edge rule ("names no part") is a scope matter, tested by the raters. |
