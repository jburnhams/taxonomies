#!/usr/bin/env python3
"""Draw the stage-2 (context area) samples from a checkout of jburnhams/prompts.

Usage: python3 sample2.py /path/to/prompts > items.csv
Reuses stage 1's item unit and filters (../sample.py). Population: every kept section of
the eight context docs, plus kept sections elsewhere (analysis docs and per-source
READMEs) whose heading names a context mechanism (HEAD_KW). Seeded file-by-file draw as
in stage 1. EXCLUDE lists hand removals by position in the drawn order.
"""
import collections, csv, glob, importlib.util, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("s1", os.path.join(HERE, "..", "sample.py"))
s1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(s1)

SEED = 20261127
CTX = ["agent-context-compaction.md", "agent-context-file-loading.md", "agent-memory-learning.md",
       "agent-prompt-cache-health.md", "agent-design/context-files.md", "agent-design/memory.md",
       "agent-design/system-prompts.md", "agent-design/keel/memory.md"]
HEAD_KW = re.compile(r"\b(memor(y|ies)|learnings?|compact\w*|context (files?|window|budget|management|engineering|service)|"
                     r"system prompts?|AGENTS\.md|CLAUDE\.md|GEMINI\.md|rules? files?|instructions?|summar\w*|"
                     r"prompt[- ]cach\w*|reminders?|retriev\w*|recall|scratchpad|notes?|truncat\w*|injected|preamble|skills? catalog)\b", re.I)
# Hand removals (meta sections and a stored prompt line the filters missed), by heading.
EXCLUDE = {"What changed from `medium.md` §6, and why", "What this implies for a new design",
           "What exists, and the gap",
           "Note: Use only relevant table for query and do aggregation, sorting, joins and grouby through sql query"}
POINTER = re.compile(r"^See `[^`]+` for the cross-source comparison this feeds into\.\s*")
SETS = [("c", 40), ("ct", 12), ("cr", 30), ("ch", 200)]


def src_readmes(root):
    os.chdir(root)
    return sorted(f for f in glob.glob("*/README.md") + glob.glob("*/*/README.md")
                  if not f.startswith(("leaked/", "skills/", "agent-design", "telemetry", "code-mode", "mcp-apps", "papers")))


def population(root):
    orig = s1.files
    s1.files = lambda r: (os.chdir(r), CTX)[1]
    a = s1.population(root)
    s1.files = orig
    others = [p for p in s1.population(root) if p["file"] not in CTX]
    srcs = src_readmes(root)
    s1.files = lambda r: (os.chdir(r), srcs)[1]
    for p in s1.population(root):
        p["g"] = POINTER.sub("", p["g"])  # a per-source section that only points elsewhere has no text
        if len(p["g"]) >= 60:
            others.append(p)
    s1.files = orig
    return a + [p for p in others if HEAD_KW.search(p["h"])]


def main(root):
    pop = population(root)
    rnd = random.Random(SEED)
    by = collections.defaultdict(list)
    for it in pop:
        by[it["file"]].append(it)
    for f in by:
        rnd.shuffle(by[f])
    fs = sorted(by); rnd.shuffle(fs)
    order, k = [], 0
    while len(order) < len(pop):
        order += [by[f][k] for f in fs if k < len(by[f])]
        k += 1
    rest = [it for it in order if it["h"] not in EXCLUDE]
    w = csv.writer(sys.stdout)
    w.writerow(["id", "item", "gist", "from"])
    p = 0
    for pre, n in SETS:
        for i in range(n):
            if p >= len(rest):
                return
            it = rest[p]; p += 1
            w.writerow([f"{pre}{i + 1:02d}", it["h"].replace("**", ""), it["g"], it["file"]])


if __name__ == "__main__":
    main(sys.argv[1])
