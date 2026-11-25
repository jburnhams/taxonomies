#!/usr/bin/env python3
"""Build the rater prompts for one agreement-test round (process step 8, spec T8).

Reads a domain's samples.md (one "## <set title>" section of `| `id` | item | [from](url) |`
rows), facets.md and glossary.md, and writes, in domains/<name>/rounds/<round>/:
  items.csv        id,item,from
  prompt-<x>.md    one prompt per rater, values shuffled with a different seed each
                   (Wan et al. 2024 §5.2.2: LLM raters showed position bias)

The facet questions, values and rater rules are set in FACETS below for the ux domain;
the value definitions are copied from glossary.md, without Warrant, History, Status or
Example, so raters see only definitions, scope notes and near misses.

Usage: python3 tools/rater_kit.py domains/ux "Round-1 test" rounds/round-1 a b
"""
import csv, random, re, sys
from pathlib import Path

FACETS = {
    "aspect": ("Which part of the interface is it about?",
               ["colour", "typography", "layout", "component", "imagery", "motion", "copy", "interaction"]),
    "brief_override": ("Can the brief allow it?", ["slop", "defect"]),
    "detection": ("What is the least you need to find it?", ["code", "render", "judgement"]),
    "mode": ("On which screens does it count?", ["any-mode", "persuade", "operate"]),
}

RULES = """Rules:
- Aspect: the part of the interface that has to change to remove the problem.
- Brief override: `slop` if a brief could ask for it with a reason, `defect` if it fails some user whatever the brief says.
- Detection: the least evidence that finds the item as written. `code` if reading the source is enough, `render` if the page has to be running, `judgement` if you need to know the brief or the subject. Whether the brief allows it is the other question.
- Mode: the narrowest set of screens the item applies to, as written. `any-mode` unless the item or its section ties it to Persuade (landing, marketing, pricing) or Operate (app screens, dashboards, tables, settings) screens.
- If an item bundles several checks, classify the first one named."""


def main(domain, set_title, out, *raters):
    d = Path(domain)
    out = d / out
    out.mkdir(parents=True, exist_ok=True)
    s = (d / "samples.md").read_text()
    sec = s.split(f"## {set_title}")[1].split("\n## ")[0]
    rows = []
    for line in sec.splitlines():
        m = re.match(r"\| `(\w+)` \| (.*) \| \[([^\]]+)\]\(", line)
        if m:
            rows.append((m.group(1), m.group(2).replace("\\|", "|"), m.group(3)))
    with open(out / "items.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "item", "from"])
        w.writerows(rows)
    g = (d / "glossary.md").read_text()
    ents = {m.group(1): m.group(0) for m in
            re.finditer(r"### [^\n]+ \(`([\w-]+)`\)\n.*?(?=\n### |\Z)", g, re.S)}
    items_csv = (out / "items.csv").read_text().strip()
    for i, name in enumerate(raters):
        rnd = random.Random(i + 1)
        p = [f"# Rater prompt: {d.name} taxonomy, {out.name}", "",
             f"You are classifying {len(rows)} items for a taxonomy agreement test. Use only the "
             "definitions below; do not look anything up and do not use other knowledge of the "
             "repos they come from.", "",
             "Each item is one entry from a research repo about generated React + Tailwind "
             "interfaces: a tell (a design habit that shows up whatever the product is) or a "
             "quality check. The `from` column says which file and section it came from, which "
             "is part of the item.", "",
             "For every item, answer all four questions with exactly one value each, chosen from "
             "the list for that question. If no value fits, still pick the closest one and write "
             "`unsure` plus a few words in the note column.", "", RULES, "",
             "Answer as CSV only, with this header and one row per item, in the items' order:", "",
             "```", "id,aspect,brief_override,detection,mode,note", "```", "",
             "## The questions and their values", ""]
        for k, (q, vals) in FACETS.items():
            v = vals[:]
            rnd.shuffle(v)
            p.append(f"- **{k}**: {q} Values: " + ", ".join(f"`{x}`" for x in v))
        p += ["", "## Definitions of the values", ""]
        allv = [x for k in FACETS for x in FACETS[k][1]]
        rnd.shuffle(allv)
        for x in allv:
            e = "\n".join(l for l in ents[x].splitlines()
                          if not re.match(r"- \*\*(Warrant|History|Status|Example)\*\*", l))
            p.append(e.strip() + "\n")
        p += ["## Items", "", "```csv", items_csv, "```", ""]
        (out / f"prompt-{name}.md").write_text("\n".join(p))
    print(f"{len(rows)} items, prompts: {', '.join(raters)}")


if __name__ == "__main__":
    main(*sys.argv[1:])
