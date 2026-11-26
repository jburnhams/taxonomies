#!/usr/bin/env python3
"""Write the stage-2 round-2 rater prompts from facets.md, glossary.md and items.csv.

One prompt per rater, each with the values and definitions in a different seeded order
(spec T8: shuffle values for model raters). Usage, from this folder:
python3 make_prompts.py
"""
import csv, random, re
from pathlib import Path

HERE = Path(__file__).parent
DOMAIN = HERE.parent.parent.parent
RATERS = {"claude": 41, "openai": 42, "gemini": 43}
AREAS = ["model", "tool", "context", "control", "coordination", "output", "verification", "operations"]
FACETS = [("operation", "What does it do to the context?"),
          ("content", "What kind of text is it about?"),
          ("reach", "How far does that text reach?")]

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
                     if not re.match(r"- \*\*(Status|Warrant|History|Example)\*\*", l)).strip()


items = list(csv.DictReader(open(HERE / "items.csv")))
RULES = """Rules:
- Classify the mechanism, approach or design choice the section describes, not the document it is in. The `from` column is part of the item.
- in_area: `yes` if the mechanism is about the `context` area as defined below (what the model is given to read and what is kept for later); `no` if another area's definition fits it better (for example prompt caching is `model`, a tool's definition or schema is `tool`, a mid-run text whose job is to redirect the model is `control`, reporting what was loaded is `operations`). If `no`, still answer the other three with the closest values.
- operation: the change the mechanism makes to what the model reads. Choosing and loading content, and writing what a fixed prompt says, is `supply`; where chosen text sits and how much it counts is `framing`; making content already there shorter or removing it is `reduction`; keeping content so a later request or run can use it is `recording`.
- content: where the text the mechanism handles came from. Written in advance to tell the model how to act: `instruction-text`. Kept from earlier work: `kept-knowledge` (a fact a run learned stays `kept-knowledge` even when a person writes it into a context file). This conversation's own record, including its summaries: `run-history`.
- reach: the widest set of requests and runs that read the same text. For a recording (a memory write, a digest, a promotion), the runs that will read what it keeps, not the run it came from. Text shipped with the harness or an agent configuration (a product's own system prompt, its reviewer or delegate prompt, a built-in reminder) is `built-in-scope`. If a section describes stores with several reaches, take the widest it describes. If it does not say how widely a store, file or server is shared, take `project-scope` unless the text says it follows a person (`user-scope`) or a team (`organization-scope`).
- If an item describes several mechanisms, classify the first one named; if it surveys several approaches without naming one first, classify the one it recommends, or pick the closest and mark `unsure`."""

for name, seed in RATERS.items():
    rnd = random.Random(seed)
    qs, defs = [], []
    for fid, q in FACETS:
        vs = values[fid][:]
        rnd.shuffle(vs)
        qs.append(f"- **{fid}**: {q} Values: " + ", ".join(f"`{v}`" for v in vs))
        defs += vs
    rnd.shuffle(defs)
    areas = AREAS[:]
    rnd.shuffle(areas)
    body = f"""# Rater prompt: prompts taxonomy, stage 2 (context area), round 2

You are classifying {len(items)} items for a taxonomy agreement test. Use only the definitions below; do not look anything up, do not read any files, and do not use other knowledge of the repo they come from.

Each item is one section of a research repo about how AI agent products and harnesses are built (Claude Code, Codex, Gemini CLI, Goose, MCP, agent SDKs) and of the designs of the repo owner's own agent platform (Keel, with configurations Forge and Lens). An item is the section's heading, the first lines under it (`gist`), and the file it is in (`from`).

For every item, answer all four questions with exactly one value each. If no value fits, still pick the closest one and write `unsure` plus a few words in the note column.

{RULES}

Answer as CSV only, with this header and one row per item, in the items' order. Quote any note that contains a comma.

```
id,in_area,operation,content,reach,note
```

## The questions and their values

- **in_area**: Is it about the `context` area? Values: `yes`, `no`
{chr(10).join(qs)}

## The areas (for `in_area`)

""" + "\n\n".join(clean(entries[a]) for a in areas) + """

## Definitions of the values

""" + "\n\n".join(clean(entries[v]) for v in defs) + "\n\n## Items\n\n```csv\n" + \
        (HERE / "items.csv").read_text().strip() + "\n```\n"
    (HERE / f"prompt-{name}.md").write_text(body)
    print(name, len(body.split()), "words")
