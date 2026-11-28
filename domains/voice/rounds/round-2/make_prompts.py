#!/usr/bin/env python3
"""Write the voice stage-1 round-2 rater prompts from facets.md, glossary.md and items.csv.

One prompt per rater, each with the values and definitions in a different seeded order
(spec T8: shuffle values for model raters). Usage, from this folder: python3 make_prompts.py
"""
import re, random
from pathlib import Path

HERE = Path(__file__).parent
DOMAIN = HERE.parent.parent
RATERS = {"claude": 71, "openai": 72, "gemini": 73}
FACETS = [("area", "Which part of the work is it about?"),
          ("modality", "Which voice is it about?"),
          ("trait", "Which part of the voice is it about?")]

gl = (DOMAIN / "glossary.md").read_text()
entries = {m.group(2): m.group(0).strip() for m in
           re.finditer(r"^### (.+?) \(`([\w-]+)`\)\n.*?(?=^##|\Z)", gl, re.M | re.S)}
fa = (DOMAIN / "facets.md").read_text()
values = {}
for fid, _ in FACETS:
    m = re.search(rf"^### \w+ \(`{fid}`\)\n.*?^- \*\*Values\*\*: (.*?)$", fa, re.M | re.S)
    values[fid] = re.findall(r"`([\w-]+)`", m.group(1))


def clean(e):
    return "\n".join(l for l in e.split("\n")
                     if not re.match(r"- \*\*(Status|Warrant|History|Example|Matches)\*\*", l)).strip()


RULES = """Rules:
- Classify what the item itself says (the source's finding, or the doc's point), not the whole document it comes from. The `from` column is part of the item: `papers/`, `specs/` and `repos/` are sources; `spoken-*.md` and `written-*.md` are topic docs; `voice-design/` is the design. The text in [brackets] at the start of a finding names its doc and heading.
- area: the step of the work that would have to change to change the item. A tool, model or metric takes the area of what the item says it is used for: a quality score used to check Jonathan's own takes before training is `preparation`; used to judge a model's output is `evaluation`. Held-out sets, splits and leakage of test data are `evaluation`. Licences, privacy, memorisation, consent and watermarks are `governance`, even inside a teacher or evaluation doc. Model size, speed, runtime, cost and reproducibility are `operations`.
- modality: `spoken` for speech, `written` for text. A finding in a `spoken-*.md` or `written-*.md` doc takes that doc's voice unless it says it holds for both. Use `both` only when the item itself applies to the spoken and the written voice alike.
- trait: what part of the voice the item would change or measure. Who it sounds or reads like (timbre, accent, overall pitch range, authorship, speaker similarity): `identity`. How something is said or written in one situation (emotion, style, stance, per-style prosody, register, tone to an audience): `expression`. What is said (words, pronunciation errors, intelligibility, WER, meaning kept, phonetic coverage): `content`. Whether it sounds or reads as made by a person at all (artefacts, noise, fluency, naturalness MOS, AI detection): `naturalness`. Only if the item names no part of the voice at all (a licence, a runtime size, a privacy rule): `whole-voice`. A "style" embedding or score used to tell authors apart is `identity`.
- If an item names several things, classify the first one named."""

items = (HERE / "items.csv").read_text().strip()
n = items.count("\n")
for name, seed in RATERS.items():
    rnd = random.Random(seed)
    qs, defs = [], []
    for fid, q in FACETS:
        vs = values[fid][:]
        rnd.shuffle(vs)
        qs.append(f"- **{fid}**: {q} Values: " + ", ".join(f"`{v}`" for v in vs))
        defs += vs
    rnd.shuffle(defs)
    body = f"""# Rater prompt: voice taxonomy, stage 1, round 2

You are classifying {n} items for a taxonomy agreement test. Use only the definitions below; do not look anything up, do not read any files, and do not use other knowledge of the repo they come from.

Each item comes from a research repo about cloning one person's voice (Jonathan's), spoken and written: making a small local text-to-speech model that sounds like him, and a writing assistant that writes like him. An item is either one source the repo has read (its title and one-line summary) or one finding or conclusion from a topic or design doc. Columns: `id`, `item`, `from` (the source folder or doc).

For every item, answer all three questions with exactly one value each. If no value fits, still pick the closest one and write `unsure` plus a few words in the note column.

{RULES}

Answer as CSV only, with this header and one row per item, in the items' order. Quote any note that contains a comma.

```
id,area,modality,trait,note
```

## The questions and their values

{chr(10).join(qs)}

## Definitions of the values

""" + "\n\n".join(clean(entries[v]) for v in defs) + "\n\n## Items\n\n```csv\n" + items + "\n```\n"
    (HERE / f"prompt-{name}.md").write_text(body)
    print(name, len(body.split()))
