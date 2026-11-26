#!/usr/bin/env python3
"""Draw the taxonomies-taxonomy samples from the method's own documents (process step 2).

An item is one unit of the method that a reader or agent looks up: a rule of design/spec.md
(S1 ... T14), a step of design/process.md, a field of a domain file (spec §§2-4), or a
decision of design/decisions.md (J1 ... J19). The source-check proposals are left out: each
became a decision (J9-J15) and would be a duplicate.

Items of each kind are shuffled with a fixed seed and spread evenly through one order,
which is cut into the sets, so every set has rules, steps, fields and decisions in about the same mix (chosen for variety,
Denton §2.3 step 1, not at random as a whole).

Usage: python3 domains/taxonomies/sample.py > domains/taxonomies/items-all.csv
"""
import csv, random, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SEED = 20261126
SETS = [("b", 48), ("t", 10), ("r", 30), ("h", 20)]


def clean(s):
    s = re.sub(r"\[([^\]]+)\]\[[^\]]*\]", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"\(\s*\)|\(\s*;\s*\)", "", s)
    s = s.replace("**", "").replace("◆ ", "").replace("⚠ ", "")
    return re.sub(r"\s+", " ", s).strip()


def first_sentences(s, limit=260):
    out = ""
    for x in re.split(r"(?<=[.!?])\s", clean(s)):
        if len(out) + len(x) > limit and out:
            break
        out += (" " if out else "") + x
    return out


def rules():
    spec = (ROOT / "design/spec.md").read_text()
    for m in re.finditer(r"^- \*\*([SNDCGT]\d+)\. ([^*]+?)\*\*(.*?)(?=^- \*\*|^#|\Z)", spec, re.M | re.S):
        rid, title, body = m.groups()
        yield ("rule", f"spec {rid}", f"{title.strip().rstrip('.')}. {first_sentences(body)}", f"design/spec.md ({rid})")


def steps():
    pr = (ROOT / "design/process.md").read_text()
    # who does each step, from "The steps at a glance", so a rater sees it as a reader does
    who = dict(re.findall(r"^\| (\d+) \|[^|]+\|[^|]+\| ([^|]+?) \|$", pr, re.M))
    for m in re.finditer(r"^## Step (\d+)\. (.+?)\n(.*?)(?=^## |\Z)", pr, re.M | re.S):
        n, title, body = m.groups()
        body = re.sub(r"^\s*(\d+\.|-)\s*", "", body.strip(), flags=re.M)
        yield ("step", f"process step {n}", f"{title.strip()} (who: {who[n]}). {first_sentences(body)}", f"design/process.md (step {n})")


def fields():
    spec = (ROOT / "design/spec.md").read_text()
    for sec, fname in (("## 2. `scope.md`", "scope.md"), ("## 3. `facets.md`", "facets.md"), ("## 4. `glossary.md`", "glossary.md")):
        part = spec.split(sec)[1].split("\n## ")[0]
        for line in part.splitlines():
            m = re.match(r"^\| \*\*([^*]+)\*\* \|(.*)\|\s*$", line)
            if not m:
                continue
            cells = [c.strip() for c in m.group(2).split("|")]
            text = cells[-1] if fname == "glossary.md" else cells[0]
            yield ("field", f"{fname} field", f"{m.group(1)}: {clean(text)}", f"design/spec.md ({fname})")


def decisions():
    d = (ROOT / "design/decisions.md").read_text()
    for line in d.splitlines():
        m = re.match(r"^\| (J\d+) \| ([^|]+) \| ([^|]+) \|", line)
        if m:
            jid, what, answer = (x.strip() for x in m.groups())
            yield ("decision", f"decision {jid}", f"{what}: {clean(answer)}", f"design/decisions.md ({jid})")


def main():
    rnd = random.Random(SEED)
    pools = [list(g()) for g in (rules, steps, fields, decisions)]
    for p in pools:
        rnd.shuffle(p)
    # spread each kind evenly through the order: item i of n sits at (i + 0.5) / n
    dealt = [x for _, _, x in sorted(((i + 0.5) / len(p), k, x) for k, p in enumerate(pools) for i, x in enumerate(p))]
    w = csv.writer(sys.stdout)
    w.writerow(["id", "item", "kind", "from"])
    i = 0
    for prefix, n in SETS:
        for k in range(n):
            if i >= len(dealt):
                break
            kind, ref, text, src = dealt[i]
            w.writerow([f"{prefix}{k + 1:02d}", f"{ref}. {text}", kind, src])
            i += 1
    print(f"{i} of {len(dealt)} items drawn", file=sys.stderr)


if __name__ == "__main__":
    main()
