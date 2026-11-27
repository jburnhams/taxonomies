#!/usr/bin/env python3
"""Draw the voice-taxonomy samples from jburnhams/voice-research (process step 2, method v1.1 M2).

An item is one of two kinds (M7: a heading plus its opening text, up to about 300 characters):
- `source`: one source folder (papers/, specs/, repos/): its title and its "In one line".
- `finding`: one bullet or numbered point of a topic doc (spoken-*.md, written-*.md) or a
  design doc (voice-design/*.md), with the doc's title and the heading it sits under.
Filters: bullets under 60 characters, link lists and "Sources:" lines are left out.

Each kind is shuffled with a fixed seed and spread evenly through one order (as in
domains/taxonomies/sample.py), which is cut into the sets, so every set has the same mix.

Usage: python3 domains/voice/sample.py ../voice-research > <private>/items-all.csv
The voice-research repo is private; where the item text is stored is J34 (scope.md).
"""
import csv, random, re, sys
from pathlib import Path

SEED = 20261127
SETS = [("b", 60), ("t", 12), ("r", 40), ("h", 40)]


def clean(s):
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = s.replace("**", "").replace("*", "").replace("`", "")
    return re.sub(r"\s+", " ", s).strip()


def cut(s, limit=300):
    s = clean(s)
    if len(s) <= limit:
        return s
    out = ""
    for x in re.split(r"(?<=[.!?])\s", s):
        if len(out) + len(x) > limit and out:
            break
        out += (" " if out else "") + x
    if len(out) > limit + 60 or out.endswith(":"):
        out = s[:limit].rsplit(" ", 1)[0] + " ..."
    return out


def sources(root):
    for kind in ("papers", "specs", "repos"):
        for d in sorted((root / kind).iterdir()):
            r = d / "README.md"
            if not r.exists():
                continue
            t = r.read_text()
            title = clean(t.splitlines()[0].lstrip("# "))
            m = re.search(r"^## In one line\n+(.*?)(?=\n##|\Z)", t, re.M | re.S)
            if m:
                yield ("source", f"{title}: {cut(m.group(1), 260)}", f"{kind}/{d.name}/")


def findings(root):
    files = sorted(root.glob("spoken-*.md")) + sorted(root.glob("written-*.md")) + sorted((root / "voice-design").glob("*.md"))
    for f in files:
        lines = f.read_text().splitlines()
        title = clean(lines[0].lstrip("# "))
        head = ""
        in_fence = False
        for ln in lines[1:]:
            if ln.startswith("```"):
                in_fence = not in_fence
            if in_fence:
                continue
            if ln.startswith("#"):
                head = clean(ln.lstrip("# "))
                continue
            m = re.match(r"^(?:- |\d+\. )(.*)", ln)
            if not m or len(m.group(1)) < 60 or m.group(1).startswith("Sources:"):
                continue
            ctx = f"{title} / {head}" if head else title
            yield ("finding", f"[{ctx}] {cut(m.group(1))}", str(f.relative_to(root)))


def main(src):
    root = Path(src)
    rnd = random.Random(SEED)
    pools = [list(sources(root)), list(findings(root))]
    for p in pools:
        rnd.shuffle(p)
    dealt = [x for _, _, x in sorted(((i + 0.5) / len(p), k, x) for k, p in enumerate(pools) for i, x in enumerate(p))]
    w = csv.writer(sys.stdout)
    w.writerow(["id", "item", "kind", "from"])
    i = 0
    for prefix, n in SETS:
        for k in range(n):
            if i >= len(dealt):
                break
            kind, text, frm = dealt[i]
            w.writerow([f"{prefix}{k + 1:02d}", text, kind, frm])
            i += 1
    print(f"{i} of {len(dealt)} items drawn ({len(pools[0])} sources, {len(pools[1])} findings)", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "../voice-research")
