#!/usr/bin/env python3
"""Write the round-2 rater prompts from facets.md, glossary.md and items.csv.

One prompt per rater, each with the values and definitions in a different seeded order
(spec T8: shuffle values for model raters). Usage, from this folder:
python3 make_prompts.py
"""
import csv, random, re
from pathlib import Path

HERE = Path(__file__).parent
DOMAIN = HERE.parent.parent
RATERS = {"claude": 21, "openai": 22, "gemini": 23}
FACETS = [("part", "What part of a taxonomy is it about?"),
          ("stage", "In which stage of the work does it first apply?"),
          ("check", "What settles whether it is met?")]

gl = (DOMAIN / "glossary.md").read_text()
entries = {m.group(2): m.group(0).strip() for m in
           re.finditer(r"^### (.+?) \(`([\w-]+)`\)\n.*?(?=^##|\Z)", gl, re.M | re.S)}
fa = (DOMAIN / "facets.md").read_text()
values = {}
for fid, _ in FACETS:
    m = re.search(rf"\(`{fid}`\)\n.*?^- \*\*Values\*\*: (.*?)$", fa, re.M | re.S)
    values[fid] = re.findall(r"`([\w-]+)`", m.group(1))


def clean(e):
    keep = []
    for line in e.split("\n"):
        if re.match(r"- \*\*(Status|Warrant|History|Example)\*\*", line):
            continue
        keep.append(line)
    return "\n".join(keep).strip()


items = list(csv.DictReader(open(HERE / "items.csv")))
RULES = """Rules:
- Classify what the item itself says. The `kind` column says what it is: a rule of the method, a process step (some with who does it; "light version" steps are the short form of the process for small domains), a file field, a file of a domain folder, or a decision the owner recorded. The item's own id has been removed, so read its text; ids inside the text are references to other rules. The `from` column is part of the item.
- part: the part of a domain's files that would change if the item were changed or broken. Words and their counts (harvest, warrant) are `naming`; items, samples, rounds, raters and kappa are `evidence`; how contexts meet is `boundary`; what the domain is for and when it is finished is `purpose`.
- stage: the first group of process steps in which the item is applied or checked: `framing` steps 0-1, `building` steps 2-6, `testing` steps 7-9, `governing` steps 10-12. A validation test T1 to T11 is `testing`; T12 to T14 are `governing`. A field or a file takes the stage of the step that first fills or writes it; a light-version step takes the stage of the steps it runs. If an item applies in several stages, the first wins.
- check: who or what has the final word on whether the item holds. `script` only when a program can decide pass or fail on its own (a count, a format, a computed kappa); a script that only flags for a person is `judgement`. `owner-decision` only when the item's own text gives the final word to Jonathan or the owner; "can veto" or "checked by Jonathan" leaves it to whoever approves, so `judgement`.
- A decision is sorted by what it settles, on all three questions, not by the fact that the owner made it.
- If an item names several things, classify the first; if no value fits, pick the closest and mark `unsure`."""

for name, seed in RATERS.items():
    rnd = random.Random(seed)
    qs, defs = [], []
    for fid, q in FACETS:
        vs = values[fid][:]
        rnd.shuffle(vs)
        qs.append(f"- **{fid}**: {q} Values: " + ", ".join(f"`{v}`" for v in vs))
        defs += vs
    rnd.shuffle(defs)
    body = f"""# Rater prompt: taxonomies taxonomy, round 2

You are classifying {len(items)} items for a taxonomy agreement test. Use only the definitions below; do not look anything up, do not read any files, and do not use other knowledge of the repo they come from.

Each item is one unit of a written method for agreeing a taxonomy (a controlled vocabulary with facets) for one area of work: a rule, a process step, a file field or a recorded decision. The repo's owner is Jonathan.

For every item, answer all three questions with exactly one value each, chosen from the list for that question. If no value fits, still pick the closest one and write `unsure` plus a few words in the note column.

{RULES}

Answer as CSV only, with this header and one row per item, in the items' order. Quote any note that contains a comma.

```
id,part,stage,check,note
```

## The questions and their values

{chr(10).join(qs)}

## Definitions of the values

""" + "\n\n".join(clean(entries[v]) for v in defs) + "\n\n## Items\n\n```csv\n" + \
        (HERE / "items.csv").read_text().strip() + "\n```\n"
    (HERE / f"prompt-{name}.md").write_text(body)
    print(name, len(body.split()), "words")
