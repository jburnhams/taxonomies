#!/usr/bin/env python3
"""Draw the prompts-taxonomy samples (samples.md) from a checkout of jburnhams/prompts.

Usage: python3 sample.py /path/to/prompts > items-all.csv
Reproduces commit a531474's draw: population, filters, seeded file-by-file order, and the
hand-dropped meta sections (EXCLUDE, positions in the drawn order).
"""
import csv, collections, glob, os, random, re, sys

SEED = 20261126
EXCLUDE = {9, 16, 19, 27, 30, 41, 52, 69, 85, 95, 114, 125, 127, 148, 182, 184, 188, 189}
SETS = [("b", 60), ("t", 12), ("r", 60), ("h", 60)]
SKIP_FILES = {"README.md", "changelog.md", "sources.md"}
SKIP_HEAD = re.compile(r"^(sources covered|design takeaways|absences|see also|sources cited|what follows|summary|contents|status|open questions|where each source sits)", re.I)
META = re.compile(r"(open points|reading order|what it measures|layers|running|^tier \d|proposal|what this changes|for the design|takeaway|where .* stands|status|summary|overview|conclusion|recommendation|what we|next steps|changelog|references|glossary|words we)", re.I)
META2 = re.compile(r"^(what (this|the) (repo|pass|field|sources?|extension)|why the split|patterns across|what was read|design decisions|.*decisions still|mechanisms that recur|what the sources agree|the numbers|supersessions|the one sentence|what it is, in one|how .* sits|what .* has that|where .* today|.*in one table|what .* carries|what gets analysed)", re.I)


def files(root):
    os.chdir(root)
    fs = [f for f in sorted(glob.glob("*.md")) if f not in SKIP_FILES]
    fs += sorted(glob.glob("agent-design/*.md")) + sorted(glob.glob("agent-design/keel/*.md"))
    fs += sorted(glob.glob("telemetry/*.md")) + ["code-mode/README.md", "mcp-apps/README.md"]
    return fs


def gist(lines, i):
    buf = []
    for t in lines[i + 1:i + 40]:
        if re.match(r"^#{1,3} ", t):
            break
        t = t.strip()
        if not t or t.startswith(("```", "|", "<!--", "---")):
            if buf and t.startswith("|"):
                break
            continue
        buf.append(re.sub(r"^[-*>]\s*", "", t))
        if len(" ".join(buf)) > 420:
            break
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", " ".join(buf)).replace("**", "")
    s = re.sub(r"\s+", " ", s)
    out = ""
    for x in re.split(r"(?<=[.!?:])\s", s):
        if len(out) + len(x) > 300 and out:
            break
        out += (" " if out else "") + x
    return out[:340]


def population(root):
    pop = []
    for f in files(root):
        if f.startswith("agent-design/proposals"):
            continue
        lines = open(f).read().split("\n")
        for i, l in enumerate(lines):
            m = re.match(r"^(##|###) (.+)", l)
            if not m:
                continue
            raw = m.group(2).strip()
            if SKIP_HEAD.match(re.sub(r"^[\d\w]{1,3}\. ", "", raw)):
                continue
            h = re.sub(r"^\d+[a-z]?\.\s*", "", raw).strip()
            if len(h.split()) < 4 or META.search(h) or h.endswith(":") or META2.match(h):
                continue
            g = gist(lines, i)
            if len(g) >= 60:
                pop.append(dict(file=f, h=h, g=g))
    return pop


def main(root):
    pop = population(root)
    rnd = random.Random(SEED)
    by = collections.defaultdict(list)
    for it in pop:
        by[it["file"]].append(it)
    for f in by:
        rnd.shuffle(by[f])
    fs = sorted(by)
    rnd.shuffle(fs)
    order, k = [], 0
    while len(order) < len(pop):
        order += [by[f][k] for f in fs if k < len(by[f])]
        k += 1
    rest = [it for n, it in enumerate(order) if n not in EXCLUDE]
    w = csv.writer(sys.stdout)
    w.writerow(["id", "item", "gist", "from"])
    p = 0
    for pre, n in SETS:
        for i in range(n):
            it = rest[p]; p += 1
            w.writerow([f"{pre}{i + 1:02d}", it["h"].replace("**", ""), it["g"], it["file"]])


if __name__ == "__main__":
    main(sys.argv[1])
