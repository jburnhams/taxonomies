# Voice stage 1, round 2: name test (T9) results

**In one line**: 3 of the 4 retested labels pass with both readers. "Coaching demo" passes
with one reader only, so it gets a near miss and stays `candidate`. Across the stage, 61
of 62 labels have now passed (98%, target 80%).

| Label | openai | gemini | Note |
|---|---|---|---|
| coaching | pass | pass | Both read it as guidance on how he delivers a line. |
| coaching demo | pass ("a sample reading he can listen to, to hear what the coach is asking for") | miss ("a walkthrough … of how the coaching process works") | Near miss added: one clip of a style, not a demo of the process. |
| style | pass | pass | Gemini added "characteristic phrasing", which leans towards `identity`; the near miss covers it. |
| whole voice | pass | pass | Both read "his overall voice, all parts together", which is the definition's first line. The edge rule ("names no part") is a scope matter, tested by the raters. |
