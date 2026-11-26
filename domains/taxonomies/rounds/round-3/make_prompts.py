#!/usr/bin/env python3
"""Write the round-3 rater prompts (facet `check` only) from facets.md, glossary.md and items.csv.

One prompt per rater, each with the values and definitions in a different seeded order
(spec T8: shuffle values for model raters). Usage, from this folder:
python3 make_prompts.py
"""
import csv, random, re
from pathlib import Path

HERE = Path(__file__).parent
DOMAIN = HERE.parent.parent
RATERS = {"claude": 31, "openai": 32, "gemini": 33}
FACETS = [("check", "What settles whether it is met?")]

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
- check: who or what has the final word on whether the item holds. `script` only for what a script stored in the repo checks today; the definition of `script` lists them all. Anything else is `judgement`, even when a program could check it, unless the item's own text gives the final word to Jonathan or the owner (`owner-decision`); "can veto" or "checked by Jonathan" leaves it to whoever approves, so `judgement`.
- A decision is sorted by what it settles, not by the fact that the owner made it.
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
    body = f"""# Rater prompt: taxonomies taxonomy, round 3 (one question)

You are classifying {len(items)} items for a taxonomy agreement test. Use only the definitions below; do not look anything up, do not read any files, and do not use other knowledge of the repo they come from.

Each item is one unit of a written method for agreeing a taxonomy (a controlled vocabulary with facets) for one area of work: a rule, a process step, a file field or a recorded decision. The repo's owner is Jonathan.

For every item, answer the question with exactly one value, chosen from its list. If no value fits, still pick the closest one and write `unsure` plus a few words in the note column.

{RULES}

Answer as CSV only, with this header and one row per item, in the items' order. Quote any note that contains a comma.

```
id,check,note
```

## The questions and their values

{chr(10).join(qs)}

## Definitions of the values

""" + "\n\n".join(clean(entries[v]) for v in defs) + "\n\n## Items\n\n```csv\n" + \
        (HERE / "items.csv").read_text().strip() + "\n```\n"
    (HERE / f"prompt-{name}.md").write_text(body)
    print(name, len(body.split()), "words")
