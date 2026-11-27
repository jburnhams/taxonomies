#!/usr/bin/env python3
"""Write the stage-3 round-1 rater prompts from facets.md, glossary.md and items.csv.

One prompt per rater, each with the values and definitions in a different seeded order
(spec T8: shuffle values for model raters). Usage, from this folder:
python3 make_prompts.py
"""
import csv, random, re
from pathlib import Path

HERE = Path(__file__).parent
DOMAIN = HERE.parent.parent.parent
RATERS = {"claude": 51, "openai": 52, "gemini": 53}
AREAS = ["model", "tool", "context", "control", "coordination", "output", "verification", "operations"]
FACETS = [("target", "What does it govern?"),
          ("response", "What does it do when it acts?")]

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
- in_area: `yes` if the mechanism is about the `control` area as defined below (whether an action may happen, and what stops, redirects or restarts a run); `no` if another area's definition fits it better (for example how a tool matches or parses its input is `tool`, what is loaded into the prompt or how it is cut down is `context`, where work goes next between sub-agents is `coordination`, checking whether finished work is right is `verification`, a design roadmap or cost report is `operations`). If `no`, still answer the other two with the closest values.
- target: what the control decides about. One action a tool would take, or a limit set once on what a run or sub-agent's tools may do (a permission mode, a sandbox, a tool scope, authority), or a step a framework runs again: `tool-action`. Whether the whole run goes on, where it is pointed, its budget, and how it may end: `run-course`. Text arriving from outside the people running the agent (tool results, web pages, untrusted files, emails, other sessions) and how far it may direct the agent: `incoming-text`. A change or output the run has finished, before it merges or is acted on (a pull request's risk tier, a merge gate): `work-product`.
- response: what the control does when it acts. Settles it itself, letting it through or refusing it: `gate` (also use `gate` when the item is about a control's whole allow/ask/refuse choice). Passes the decision to a person and waits: `ask-person`. Sets a level (a risk tier, a trust level, an authority posture) that other rules then read: `grade`. Adds text that changes what the agent does next while the run goes on: `redirect`. Runs something again or carries it on after a failure or stop: `recover`. Stops or suspends the run, or fixes the ways it may end: `halt`.
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
    body = f"""# Rater prompt: prompts taxonomy, stage 3 (control area), round 1

You are classifying {len(items)} items for a taxonomy agreement test. Use only the definitions below; do not look anything up, do not read any files, and do not use other knowledge of the repo they come from.

Each item is one section of a research repo about how AI agent products and harnesses are built (Claude Code, Codex, Gemini CLI, Goose, MCP, agent SDKs) and of the designs of the repo owner's own agent platform (Keel, with configurations Forge and Lens). An item is the section's heading, the first lines under it (`gist`), and the file it is in (`from`).

For every item, answer all three questions with exactly one value each. If no value fits, still pick the closest one and write `unsure` plus a few words in the note column.

{RULES}

Answer as CSV only, with this header and one row per item, in the items' order. Quote any note that contains a comma.

```
id,in_area,target,response,note
```

## The questions and their values

- **in_area**: Is it about the `control` area? Values: `yes`, `no`
{chr(10).join(qs)}

## The areas (for `in_area`)

""" + "\n\n".join(clean(entries[a]) for a in areas) + """

## Definitions of the values

""" + "\n\n".join(clean(entries[v]) for v in defs) + "\n\n## Items\n\n```csv\n" + \
        (HERE / "items.csv").read_text().strip() + "\n```\n"
    (HERE / f"prompt-{name}.md").write_text(body)
    print(name, len(body.split()), "words")
