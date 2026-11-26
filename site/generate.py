#!/usr/bin/env python3
"""Read the repo's taxonomy files and write the data the explorer site shows.

Nothing here is hand-kept: every domain folder under `domains/` with a `glossary.md` is
picked up, and every round folder under it with an `items.csv` and `answers/*.csv`. The
parsers follow the field grammar of `design/spec.md` §1 (records start `### <label>
(`<id>`)`, fields are `- **<Field>**: <value>`), the same grammar `tools/check_domain.py`
checks, so a file that passes T1 is a file this can read.

Writes, under site/public/ (git-ignored, rebuilt on every deploy):
  data/index.json        the overview: domains with counts, docs, sources
  data/domain/<id>.json  one domain: terms, facets, items, rounds with answers and kappa
  raw/<path>             copies of every markdown doc and every CSV under domains/,
                         fetched as text by the doc and file pages. Stored source copies
                         (PDFs, saved pages) are NOT copied: the site is public and the
                         repo is private (see site/README.md).

Usage: python3 site/generate.py [--check]   (--check: parse only, print problems, write nothing)
"""
import csv, io, json, re, shutil, subprocess, sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site" / "public"
REPO = "jburnhams/taxonomies"
ITEM_ID = re.compile(r"`([a-z]\d{2,3})`")
ID_IN = re.compile(r"`([\w-]+)`")
problems = []


def warn(msg):
    problems.append(msg)


def git(*args):
    try:
        return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return ""


# ---------- markdown helpers ----------

def title_of(md, fallback):
    m = re.search(r"^# (.+)$", md, re.M)
    return m.group(1).strip() if m else fallback


def lead(md, name):
    """The paragraph after `**<name>**:` (the repo's 'In one line' / 'In plain words' / 'Status')."""
    m = re.search(rf"^\*\*{re.escape(name)}\*\*:?\s*(.*?)(?=\n\s*\n|\Z)", md, re.M | re.S | re.I)
    return re.sub(r"\s*\n\s*", " ", m.group(1)).strip() if m else ""


def records(md):
    """Every `### label (`id`)` record: label, id, the h2 it sits under, its fields, and the prose after them.

    A field is a top-level bullet `- **Name**: value`; indented lines continue it (so a
    multi-line Values field or nested Value notes stay with their field)."""
    out = []
    h2 = ""
    lines = md.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            h2 = line[3:].strip()
        m = re.match(r"^### (.+?) \(`([\w-]+)`\)\s*$", line)
        if not m:
            i += 1
            continue
        label, rid = m.groups()
        i += 1
        body = []
        while i < len(lines) and not re.match(r"^#{1,3} ", lines[i]):
            body.append(lines[i])
            i += 1
        fields, order, prose, cur = {}, [], [], None
        for b in body:
            fm = re.match(r"^- \*\*([^*]+)\*\*:\s?(.*)$", b)
            if fm:
                cur = fm.group(1).strip()
                fields[cur] = fm.group(2)
                order.append(cur)
            elif cur and b.startswith("  ") and b.strip():
                fields[cur] += "\n" + b
            elif b.strip() == "" and not prose:
                cur = None
            else:
                cur = None
                prose.append(b)
        out.append({"label": label.strip(), "id": rid, "section": h2,
                    "fields": {k: v.strip() for k, v in fields.items()}, "order": order,
                    "prose": "\n".join(prose).strip()})
    return out


def preamble(md):
    """The doc before its first record or `## Entries` heading."""
    m = re.search(r"^(## Entries|### .+\(`[\w-]+`\))", md, re.M)
    return md[: m.start()].strip() if m else md.strip()


def ids_in(v):
    return ID_IN.findall(v or "")


def dated_bullets(md):
    """Changelog bullets with the `## YYYY-MM-DD` they sit under."""
    out, day, cur = [], "", None
    for line in md.split("\n"):
        d = re.match(r"^## (\d{4}-\d{2}-\d{2})", line)
        if d:
            day, cur = d.group(1), None
            continue
        if line.startswith("- "):
            cur = {"date": day, "text": line[2:].strip()}
            out.append(cur)
        elif cur is not None and line.startswith("  ") and line.strip():
            cur["text"] += " " + line.strip()
        else:
            cur = None
    return out


def table_rows(md):
    """Rows of every pipe table, as lists of cell strings, with the heading they sit under."""
    out, head = [], ""
    for line in md.split("\n"):
        if line.startswith("#"):
            head = line.lstrip("#").strip()
        if line.startswith("|") and not re.match(r"^\|[\s:|-]+\|\s*$", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            out.append((head, cells))
    return out


def read_csv(p):
    with open(p, newline="") as f:
        return list(csv.DictReader(f))


# ---------- kappa (same formula as tools/kappa.py) ----------

def cohen(a, b):
    n = len(a)
    if not n:
        return None, None
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    return po, (1.0 if pe == 1 else (po - pe) / (1 - pe))


def fleiss(rows):
    """rows: one list of labels per item, one label per rater (all items rated by all)."""
    n = len(rows)
    if not n:
        return None
    m = len(rows[0])
    cats = sorted({x for r in rows for x in r})
    pj = {c: sum(r.count(c) for r in rows) / (n * m) for c in cats}
    Pi = [(sum(r.count(c) ** 2 for c in cats) - m) / (m * (m - 1)) for r in rows]
    P, Pe = sum(Pi) / n, sum(v * v for v in pj.values())
    return 1.0 if Pe == 1 else (P - Pe) / (1 - Pe)


# ---------- one domain ----------

def norm(v):
    return (v or "").strip().strip("`").lower()


def parse_round(d, rdir, facet_ids):
    rel = rdir.relative_to(ROOT).as_posix()
    rnd = {"id": rdir.name, "path": rel, "docs": [], "files": [], "items": [], "raters": [],
           "facets": [], "answers": {}, "notes": {}, "kappa": [], "pairs": [], "disagreements": []}
    for p in sorted(rdir.rglob("*")):
        if p.is_file():
            r = p.relative_to(ROOT).as_posix()
            (rnd["docs"] if p.suffix == ".md" else rnd["files"]).append(r)
    rd = rdir / "README.md"
    rnd["title"] = rdir.name.replace("-", " ").capitalize()
    res = rdir / "results.md"
    rnd["oneLine"] = lead(res.read_text(), "In one line") if res.exists() else (lead(rd.read_text(), "In one line") if rd.exists() else "")
    if (rdir / "items.csv").exists():
        rnd["items"] = [{"id": r["id"].strip(), "item": (r.get("item") or "").strip(), "from": (r.get("from") or "").strip()}
                        for r in read_csv(rdir / "items.csv")]
    adir = rdir / "answers"
    if not adir.is_dir():
        return rnd
    for p in sorted(adir.glob("*.csv")):
        rows = read_csv(p)
        if not rows:
            continue
        name = p.stem
        rnd["raters"].append({"name": name, "file": p.relative_to(ROOT).as_posix(), "rows": len(rows)})
        cols = [c for c in rows[0].keys() if c and c.strip() not in ("id", "note")]
        for c in cols:
            fid = c.strip().replace("_", "-")
            if fid not in rnd["facets"]:
                rnd["facets"].append(fid)
                if facet_ids and fid not in facet_ids:
                    warn(f"{rel}: answer column {c} is not a facet of the domain")
        for r in rows:
            iid = r["id"].strip()
            rnd["answers"].setdefault(iid, {})[name] = {c.strip().replace("_", "-"): norm(r[c]) for c in cols}
            if (r.get("note") or "").strip():
                rnd["notes"].setdefault(iid, {})[name] = r["note"].strip()
    raters = [r["name"] for r in rnd["raters"]]
    ids = [i["id"] for i in rnd["items"]] or sorted(rnd["answers"])
    full = [i for i in ids if all(n in rnd["answers"].get(i, {}) for n in raters)]
    for f in rnd["facets"]:
        k = {"facet": f, "n": len(full)}
        if len(raters) >= 2:
            labs = [[rnd["answers"][i][n].get(f, "") for n in raters] for i in full]
            k["agreement"] = sum(len(set(l)) == 1 for l in labs) / len(labs) if labs else None
            if len(raters) == 2:
                k["kappa"] = cohen([l[0] for l in labs], [l[1] for l in labs])[1]
                k["measure"] = "Cohen"
            else:
                k["kappa"] = fleiss(labs)
                k["measure"] = "Fleiss"
            for i, l in zip(full, labs):
                if len(set(l)) > 1:
                    rnd["disagreements"].append({"item": i, "facet": f, "answers": dict(zip(raters, l))})
        rnd["kappa"].append(k)
    for a, b in combinations(raters, 2):
        for f in rnd["facets"]:
            po, kv = cohen([rnd["answers"][i][a].get(f, "") for i in full], [rnd["answers"][i][b].get(f, "") for i in full])
            rnd["pairs"].append({"a": a, "b": b, "facet": f, "agreement": po, "kappa": kv})
    return rnd


def parse_items(d):
    """Every item the domain names: from items CSVs and from the tables in samples.md."""
    items = {}
    sm = d / "samples.md"
    if sm.exists():
        for head, cells in table_rows(sm.read_text()):
            m = re.fullmatch(r"`([a-z]\d{2,3})`", cells[0]) if cells else None
            if m and len(cells) >= 2:
                items[m.group(1)] = {"id": m.group(1), "item": cells[1], "from": cells[2] if len(cells) > 2 else "", "set": head}
    for p in sorted(d.rglob("*.csv")):
        if "answers" in p.parts:
            continue
        try:
            rows = read_csv(p)
        except Exception:
            continue
        if not rows or "id" not in rows[0]:
            continue
        textcol = next((c for c in ("item", "text", "heading") if c in rows[0]), None)
        if not textcol:
            continue
        for r in rows:
            iid = r["id"].strip()
            it = items.setdefault(iid, {"id": iid, "item": r[textcol].strip(), "from": (r.get("from") or "").strip(), "set": ""})
            if not it.get("item"):
                it["item"] = r[textcol].strip()
    return items


def parse_domain(d):
    rel = d.relative_to(ROOT).as_posix()
    gl = (d / "glossary.md").read_text()
    fa = (d / "facets.md").read_text() if (d / "facets.md").exists() else ""
    sc = (d / "scope.md").read_text() if (d / "scope.md").exists() else ""
    ch = (d / "changelog.md").read_text() if (d / "changelog.md").exists() else ""
    dom = {"id": d.name, "path": rel}
    dom["title"] = title_of(sc or gl, d.name).split(":")[0].strip()
    dom["oneLine"] = lead(sc, "In one line") or lead(gl, "In one line")
    dom["plain"] = lead(sc, "In plain words")
    st = re.search(r"^- \*\*Status\*\*:\s*(.*?)(?=\n- \*\*|\n\s*\n|\Z)", sc, re.M | re.S)
    dom["status"] = re.sub(r"\s+", " ", st.group(1)).strip() if st else lead(gl, "Status")
    sw = re.search(r"\b(in use|draft|retired)\b", dom["status"].lower())
    dom["statusWord"] = sw.group(1) if sw else "draft"
    dom["glossaryIntro"] = preamble(gl)
    dom["docs"] = sorted(p.relative_to(ROOT).as_posix() for p in d.rglob("*.md"))
    dom["files"] = sorted(p.relative_to(ROOT).as_posix() for p in d.rglob("*") if p.is_file() and p.suffix != ".md")

    # terms
    terms = {}
    for r in records(gl):
        f = r["fields"]
        if r["id"] in terms:
            warn(f"{rel}/glossary.md: duplicate id {r['id']}")
        t = {"id": r["id"], "label": r["label"], "section": r["section"], "fields": f, "order": r["order"],
             "prose": r["prose"],
             "status": (re.match(r"\w+", f.get("Status", "")) or [""])[0].lower(),
             "kind": f.get("Kind", "").strip().strip("`"),
             "broader": ids_in(f.get("Broader")), "related": ids_in(f.get("Related")),
             "facets": ids_in(f.get("Facet")), "replacedBy": ids_in(f.get("Replaced by")),
             "aliases": [a.strip() for a in f.get("Aliases", "").split(",") if a.strip()],
             "narrower": [], "items": sorted(set(ITEM_ID.findall(" ".join(f.values())))), "changelog": []}
        terms[r["id"]] = t
    for t in terms.values():
        for b in t["broader"]:
            if b in terms:
                terms[b]["narrower"].append(t["id"])
            else:
                warn(f"{rel}: `{t['id']}` broader `{b}` has no entry")
        for x in t["related"] + t["replacedBy"]:
            if x not in terms:
                warn(f"{rel}: `{t['id']}` refers to missing `{x}`")
    dom["terms"] = terms

    # facets: a facet is in use when glossary terms name it in their Facet field
    used = {f for t in terms.values() for f in t["facets"]}
    facets = []
    for r in records(fa):
        f = r["fields"]
        if "Question" not in f and "Values" not in f:
            continue
        top = re.sub(r"\([^)]*\)", "", f.get("Values", ""), flags=re.S).split("\n  -")[0]
        vals = re.findall(r"(?:^|,\s*)`([\w-]+)`", top.strip()) or re.findall(r"`([\w-]+)`", f.get("Values", ""))
        facets.append({"id": r["id"], "label": r["label"], "set": r["section"], "fields": f, "order": r["order"],
                       "prose": r["prose"], "values": vals, "inUse": r["id"] in used,
                       "unsorted": sorted(set(ITEM_ID.findall(f.get("Unsorted", ""))))})
    for f in facets:
        if f["inUse"]:
            for v in f["values"]:
                if v not in terms:
                    warn(f"{rel}: facet `{f['id']}` value `{v}` has no glossary entry")
    dom["facets"] = facets
    dom["facetsIntro"] = preamble(fa)
    facet_ids = {f["id"] for f in facets if f["inUse"]}

    # changelog lines per term
    dom["changelog"] = dated_bullets(ch)
    for i, line in enumerate(dom["changelog"]):
        for x in set(ids_in(line["text"])):
            if x in terms:
                terms[x]["changelog"].append(i)

    # items and rounds
    items = parse_items(d)
    rounds = []
    rroot = d / "rounds"
    if rroot.is_dir():
        for rdir in sorted(p for p in rroot.iterdir() if p.is_dir()):
            rnd = parse_round(d, rdir, facet_ids)
            for it in rnd["items"]:
                items.setdefault(it["id"], {"id": it["id"], "item": it["item"], "from": it["from"], "set": ""})
            rounds.append(rnd)
    dom["rounds"] = rounds
    # where each item is mentioned: docs, terms, facets
    mentions = defaultdict(list)
    for p in d.rglob("*.md"):
        for iid in set(ITEM_ID.findall(p.read_text())):
            mentions[iid].append(p.relative_to(ROOT).as_posix())
    for iid, it in items.items():
        it["docs"] = sorted(mentions.get(iid, []))
        it["terms"] = sorted(t for t, v in terms.items() if iid in v["items"])
        it["rounds"] = [r["id"] for r in rounds if iid in r["answers"] or any(x["id"] == iid for x in r["items"])]
        it["unsortedIn"] = [f["id"] for f in facets if iid in f["unsorted"]]
    dom["items"] = items

    # value usage: how often each rater put an item under each facet value
    for t in terms.values():
        t["placed"] = []
    for rnd in rounds:
        for iid, by in rnd["answers"].items():
            for f in rnd["facets"]:
                vals = {a.get(f) for a in by.values() if a.get(f)}
                for v in vals:
                    if v in terms:
                        terms[v]["placed"].append({"round": rnd["id"], "item": iid, "facet": f,
                                                   "unanimous": len({a.get(f) for a in by.values()}) == 1})
    # counts
    sc_ = Counter(t["status"] for t in terms.values())
    latest = next((r for r in reversed(rounds) if r["kappa"] and len(r["raters"]) >= 2), None)
    dom["counts"] = {"terms": len(terms), "status": dict(sc_), "facets": len(facet_ids), "rounds": len(rounds),
                     "items": len(items),
                     "minKappa": min((k["kappa"] for k in latest["kappa"] if k.get("kappa") is not None), default=None) if latest else None,
                     "latestRound": latest["id"] if latest else None}
    return dom


# ---------- the repo ----------

def doc_entry(p):
    md = p.read_text()
    rel = p.relative_to(ROOT).as_posix()
    return {"path": rel, "title": title_of(md, rel), "oneLine": lead(md, "In one line")}


def main(check=False):
    domains = []
    for d in sorted((ROOT / "domains").iterdir()):
        if d.is_dir() and (d / "glossary.md").exists():
            domains.append(parse_domain(d))
    # the method's own vocabulary first, then by size
    domains.sort(key=lambda x: (x["id"] != "taxonomies", -x["counts"]["terms"]))

    top = [doc_entry(p) for p in sorted(ROOT.glob("*.md")) if p.name not in ("CLAUDE.md",)]
    design = [doc_entry(p) for p in sorted((ROOT / "design").glob("*.md"))]
    sources = []
    for s in sorted((ROOT / "sources").iterdir()):
        rd = s / "README.md"
        if not rd.exists():
            continue
        md = rd.read_text()
        fld = lambda k: (re.search(rf"^- \*\*{k}\*\*:\s*(.*)$", md, re.M) or [None, ""])[1].strip()
        stored = sorted(p.name for p in s.iterdir() if p.is_file() and p.name != "README.md")
        sources.append({"slug": s.name, "title": title_of(md, s.name), "source": fld("Source"), "type": fld("Type"),
                        "access": fld("Access"), "read": fld("Read"), "stored": stored})

    index = {
        "repo": REPO, "commit": git("rev-parse", "HEAD"), "short": git("rev-parse", "--short", "HEAD"),
        "date": git("log", "-1", "--format=%cs"),
        "readme": {"oneLine": lead((ROOT / "README.md").read_text(), "In one line"),
                   "intro": (ROOT / "README.md").read_text().split("\n## ")[0].split("\n", 1)[-1].strip()},
        "domains": [{k: d[k] for k in ("id", "title", "oneLine", "plain", "status", "statusWord", "counts", "path")}
                    | {"facets": [{"id": f["id"], "label": f["label"], "values": f["values"],
                                   "question": f["fields"].get("Question", "")} for f in d["facets"] if f["inUse"]]}
                    for d in domains],
        "topDocs": top, "designDocs": design, "sources": sources,
        "problems": problems,
        "docs": sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*.md")
                       if p.relative_to(ROOT).parts[0] not in (".git", "site", "node_modules", ".github")
                       and (p.relative_to(ROOT).parts[0] != "sources" or p.name == "README.md")),
    }
    for p in problems:
        print("generate:", p, file=sys.stderr)
    if check:
        print(f"{len(domains)} domains, {sum(len(d['terms']) for d in domains)} terms, {len(sources)} sources; {len(problems)} problem(s)")
        return 0
    if OUT.exists():
        for sub in ("data", "raw"):
            shutil.rmtree(OUT / sub, ignore_errors=True)
    (OUT / "data" / "domain").mkdir(parents=True, exist_ok=True)
    (OUT / "data" / "index.json").write_text(json.dumps(index, ensure_ascii=False))
    for d in domains:
        (OUT / "data" / "domain" / f"{d['id']}.json").write_text(json.dumps(d, ensure_ascii=False))
    # raw text: every markdown doc (sources: README only) and every CSV under domains/
    n = 0
    for p in ROOT.rglob("*"):
        r = p.relative_to(ROOT)
        if not p.is_file() or r.parts[0] in (".git", "site", "node_modules", ".github"):
            continue
        if r.parts[0] == "sources" and p.name != "README.md":
            continue
        if p.suffix == ".md" or (p.suffix == ".csv" and r.parts[0] == "domains"):
            dst = OUT / "raw" / r
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(p, dst)
            n += 1
    print(f"wrote {len(domains)} domains, {n} raw files to {OUT.relative_to(ROOT)}; {len(problems)} problem(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
