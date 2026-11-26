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
RATERS = {"claude": 11, "openai": 12, "gemini": 13}
FACETS = [("area", "Which part of an agent system is it about?"),
          ("decider", "Who makes the call when it applies?"),
          ("moment", "When does it act?")]

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
- Classify the mechanism, approach or design choice the section describes, not the document it is in. The `from` column is part of the item.
- area: the part of an agent system that would have to change to change the mechanism. Whatever decides *whether* something may happen is `control`; whatever decides *where work goes next* is `coordination`; checking whether finished work is right is `verification`.
- decider: the party whose decision has the final say when it applies. Test: if the model ignored its instructions, would the outcome still hold? Yes: `rule` (or `second-model` / `person` if one of those decides). No: `working-model`. A store or format with nothing decided at run time, and a setting a person chose before the run, are `rule`.
- moment: the first point in a run's life at which it takes effect. `setup` is only what happens before the first model request (configuration, loading context, choosing tools, provisioning). A format, store or rule fixed in advance takes the moment at which it is used: a result format at `tool-call`, a tier computed when a run finishes at `ending`, a memory store at `after-run`.
- If an item describes several mechanisms, classify the first one named."""

for name, seed in RATERS.items():
    rnd = random.Random(seed)
    qs, defs = [], []
    for fid, q in FACETS:
        vs = values[fid][:]
        rnd.shuffle(vs)
        qs.append(f"- **{fid}**: {q} Values: " + ", ".join(f"`{v}`" for v in vs))
        defs += vs
    rnd.shuffle(defs)
    body = f"""# Rater prompt: prompts taxonomy, stage 1, round 2

You are classifying {len(items)} items for a taxonomy agreement test. Use only the definitions below; do not look anything up, do not read any files, and do not use other knowledge of the repo they come from.

Each item is one section of a research repo about how AI agent products and harnesses are built (Claude Code, Codex, Gemini CLI, MCP, agent SDKs) and of the designs of the repo owner's own agent platform (Keel, with configurations Forge and Lens). An item is the section's heading, the first lines under it (`gist`), and the file it is in (`from`).

For every item, answer all three questions with exactly one value each, chosen from the list for that question. If no value fits, still pick the closest one and write `unsure` plus a few words in the note column.

{RULES}

Answer as CSV only, with this header and one row per item, in the items' order. Quote any note that contains a comma.

```
id,area,decider,moment,note
```

## The questions and their values

{chr(10).join(qs)}

## Definitions of the values

""" + "\n\n".join(clean(entries[v]) for v in defs) + "\n\n## Items\n\n```csv\n" + \
        (HERE / "items.csv").read_text().strip() + "\n```\n"
    (HERE / f"prompt-{name}.md").write_text(body)
    print(name, len(body.split()), "words")
