#!/usr/bin/env python3
"""Look up the term to use, see what changed, and gather term requests (design/growth.md).

A domain repo (prompts, ux-research, ...) uses this to ask "which word do I use for this
concept?" before it writes one, and to see what changed in its glossary since its last
pass. The taxonomies repo uses `intake` to collect the requests domain repos have written.
Standard library only, one file, so it runs without a checkout of this repo:

  curl -fsSL https://raw.githubusercontent.com/jburnhams/taxonomies/main/tools/term.py \\
    | python3 - lookup prompts "approval timeout"

Commands:
  lookup DOMAIN WORDS...       the term for these words: an exact label match, else the
                               closest terms, plus any request already made for them
  changes DOMAIN --since DATE  operations logged on or after DATE (YYYY-MM-DD), breaking ones
                               marked, and requests answered since then
  intake [--repos DIR] [--write]
                               (taxonomies repo) new requests in each domain repo's
                               term-requests.md, each with its lookup; --write adds them to
                               domains/<name>/requests.md as `open`

Where the files come from: --root DIR, else $TAXONOMIES_ROOT, else this script's own repo
when it sits in a checkout, else raw.githubusercontent.com (main branch).
Exit codes for lookup: 0 an exact label matched, 1 only near terms, 2 nothing found.
"""
import argparse, json, os, re, sys, urllib.request
from pathlib import Path

RAW = "https://raw.githubusercontent.com/jburnhams/taxonomies/main/"
BREAKING = {"rename", "split", "merge", "move", "deprecate"}
OPS = BREAKING | {"add", "redefine", "alias", "adopt", "record", "review", "score", "decide"}
STOP = set("a an the of to for in on and or is it its by with as at be that this from".split())


# ---------- reading the files ----------

def find_root(arg):
    for r in (arg, os.environ.get("TAXONOMIES_ROOT")):
        if r:
            return Path(r)
    here = Path(__file__).resolve().parent.parent if "__file__" in globals() else None
    if here and (here / "domains").is_dir():
        return here
    return None


def read(root, rel):
    """Text of rel under root, or from GitHub; '' if it does not exist."""
    if root:
        p = root / rel
        return p.read_text() if p.exists() else ""
    try:
        with urllib.request.urlopen(RAW + rel, timeout=20) as r:
            return r.read().decode()
    except Exception as e:  # 404 for a file not created yet
        if getattr(e, "code", None) == 404:
            return ""
        sys.exit(f"term.py: cannot fetch {RAW + rel}: {e}")


def records(md):
    """`### label (`id`)` records with their `- **Field**: value` bullets (spec §1 grammar)."""
    out = []
    md = re.sub(r"^```.*?^```[ \t]*$", "", md, flags=re.M | re.S)  # templates in code fences are not records
    for m in re.finditer(r"^### (.+?) \(`([\w-]+)`\)[ \t]*\n(.*?)(?=^#{1,3} |\Z)", md, re.M | re.S):
        label, rid, body = m.groups()
        fields, cur = {}, None
        for line in body.split("\n"):
            fm = re.match(r"^- \*\*([^*]+)\*\*:\s?(.*)$", line)
            if fm:
                cur = fm.group(1).strip()
                fields[cur] = fm.group(2).strip()
            elif cur and line.startswith("  ") and line.strip():
                fields[cur] += " " + line.strip()
            else:
                cur = None
        out.append({"label": label.strip(), "id": rid, **fields})
    return out


def fold(s):
    return re.sub(r"[-_\s]+", " ", s.strip().lower().strip("`\"'"))


def words(s):
    return {w.rstrip("s") if len(w) > 3 else w for w in re.findall(r"[a-z0-9]+", s.lower())} - STOP


def ids_in(v):
    return re.findall(r"`([\w-]+)`", v or "")


def labels(t):
    return [t["label"]] + [a for f in ("Aliases", "Hidden") for a in (t.get(f) or "").split(",") if a.strip()]


# ---------- lookup ----------

def lookup(root, domain, query):
    terms = {t["id"]: t for t in records(read(root, f"domains/{domain}/glossary.md"))}
    if not terms:
        sys.exit(f"term.py: no glossary for domain '{domain}' (domains/{domain}/glossary.md)")
    reqs = records(read(root, f"domains/{domain}/requests.md"))
    q, qw = fold(query), words(query)
    # a label match wins; an identifier is a fallback only when no label matches (prompts IDs `model`, `tool` name areas)
    exact = [t for t in terms.values() if q in (fold(l) for l in labels(t))] \
        or [t for t in terms.values() if q == t["id"].replace("-", " ")]
    scored = []
    for t in terms.values():
        if t in exact:
            continue
        lw = set().union(*(words(l) for l in labels(t)))
        dw = words(" ".join(t.get(f, "") for f in ("Definition", "Scope", "Near miss")))
        s = 3 * len(qw & lw) + len(qw & dw) + (2 if q in fold(" ".join(labels(t))) else 0)
        if s:
            scored.append((s, t))
    scored.sort(key=lambda x: (-x[0], x[1]["id"]))
    near = [t for s, t in scored[:5] if s >= max(2, scored[0][0] // 2)] if scored else []
    asked = [r for r in reqs if q == fold(r["label"]) or (qw and len(qw & words(r["label"] + " " + r.get("Concept", ""))) >= max(1, len(qw) - 1))]
    return terms, exact, near, asked


def q_in_labels(t, query):
    return fold(query) in (fold(l) for l in labels(t))


def show_term(terms, t, why):
    st = t.get("Status", "?").split()[0]
    lines = [f"  {t['label']} (`{t['id']}`), {st}: {why}", f"    {t.get('Definition', '')}"]
    if t.get("Scope"):
        lines.append(f"    Scope: {t['Scope']}")
    if t.get("Near miss"):
        lines.append(f"    Near miss: {t['Near miss']}")
    if st == "deprecated":
        rep = [terms[i]["label"] + f" (`{i}`)" for i in ids_in(t.get("Replaced by")) if i in terms]
        lines.append(f"    Deprecated: use {', '.join(rep) or t.get('Replaced by')}")
    return "\n".join(lines)


def cmd_lookup(a):
    root = find_root(a.root)
    query = " ".join(a.words)
    terms, exact, near, asked = lookup(root, a.domain, query)
    if a.json:
        print(json.dumps({"query": query, "exact": exact, "near": near, "requests": asked}, ensure_ascii=False, indent=1))
    else:
        print(f"{a.domain}: \"{query}\"")
        if exact:
            print("Use:")
            for t in exact:
                why = ("preferred label" if fold(t["label"]) == fold(query)
                       else "you used an alias or old label; write the preferred label" if q_in_labels(t, query)
                       else "you used its identifier; write the preferred label")
                print(show_term(terms, t, why))
        elif near:
            print("No term has this label. Closest terms (check each one's scope and near miss):")
            for t in near:
                print(show_term(terms, t, "near"))
        else:
            print("No term found.")
        if asked:
            print("Already requested:")
            for r in asked:
                print(f"  {r['label']} (`{r['id']}`): {r.get('Outcome', 'open')}  [{r.get('Asked', '')}]")
        if not exact:
            print("If none fits, use your own word now and add a request to term-requests.md "
                  "in your repo (template: design/growth.md#the-request-record).")
    return 0 if exact else 1 if near or asked else 2


# ---------- changes ----------

def changelog_ops(md):
    """(day, text, ops) for each top-level bullet of a domain changelog."""
    out, day, cur = [], None, None
    for line in md.split("\n"):
        dm = re.match(r"^## (\d{4}-\d{2}-\d{2})", line)
        if dm:
            day, cur = dm.group(1), None
            continue
        if day and line.startswith("- "):
            cur = [day, line[2:].strip()]
            out.append(cur)
        elif cur and line.startswith("  ") and line.strip():
            cur[1] += " " + line.strip()
        else:
            cur = None
    return [(d, t, [o for o in re.findall(r"\*\*([a-z ]+?)\*\*", t) if o.split()[0] in OPS]) for d, t in out]


def cmd_changes(a):
    root = find_root(a.root)
    rows = [r for r in changelog_ops(read(root, f"domains/{a.domain}/changelog.md")) if r[0] >= a.since]
    tids = {t["id"] for t in records(read(root, f"domains/{a.domain}/glossary.md"))}
    # breaking: a rename, split, merge, move or deprecate that names a term, or a line marked "Breaking:"
    brk = lambda t, ops: "Breaking:" in t or bool({o.split()[0] for o in ops} & BREAKING and set(ids_in(t)) & tids)
    reqs = [r for r in records(read(root, f"domains/{a.domain}/requests.md"))
            if (r.get("Answered") or "")[:10] >= a.since]
    print(f"{a.domain}: changes on or after {a.since}, newest first (the day itself is included, so lines seen last time may repeat)")
    if not rows and not reqs:
        print("  none")
    for day, text, ops in rows:
        print(f"  {day} {'BREAKING ' if brk(text, ops) else ''}{text}")
    if reqs:
        print("Requests answered:")
        for r in reqs:
            print(f"  {r['label']} (`{r['id']}`): {r.get('Outcome', '')}  [{r.get('Answered', '')}]")
    if any(brk(t, ops) for _, t, ops in rows):
        print("Breaking changes: switch old labels to the new ones in docs you touch "
              "(`lookup` on an old label names its replacement).")
    return 0


# ---------- intake (run in the taxonomies repo) ----------

def domain_repo(scope):
    m = re.search(r"^- \*\*Context\*\*:.*?github\.com/([\w.-]+/[\w.-]+)", scope, re.M)
    return m.group(1) if m else None


def cmd_intake(a):
    root = find_root(a.root)
    if not root:
        sys.exit("term.py intake: run it in a checkout of jburnhams/taxonomies (or pass --root)")
    repos = Path(a.repos) if a.repos else root.parent
    found = 0
    for d in sorted(p for p in (root / "domains").iterdir() if (p / "glossary.md").exists()):
        repo = domain_repo((d / "scope.md").read_text()) if (d / "scope.md").exists() else None
        inbox = (repos / repo.split("/")[1] / "term-requests.md") if repo else root / "term-requests.md"
        if not inbox.exists():
            print(f"{d.name}: no inbox at {inbox}")
            continue
        logp = d / "requests.md"
        log = logp.read_text() if logp.exists() else ""
        done = {r["id"] for r in records(log)}
        new = [r for r in records(inbox.read_text()) if r["id"] not in done]
        print(f"{d.name}: {len(new)} new request(s) in {inbox}")
        for r in new:
            found += 1
            print(f"\n  {r['label']} (`{r['id']}`) ask: {r.get('Ask', 'new')}  term: {r.get('Term', '-')}")
            print(f"    Concept: {r.get('Concept', '')}")
            terms, exact, near, _ = lookup(root, d.name, r["label"])
            hits = exact or near
            print("    Lookup: " + (", ".join(f"`{t['id']}`" + (" (exact)" if t in exact else "") for t in hits) or "nothing"))
        if a.write and new:
            src = f"{repo}/term-requests.md" if repo else "term-requests.md"
            add = []
            for r in new:
                body = "".join(f"- **{k}**: {v}\n" for k, v in r.items() if k not in ("label", "id"))
                add.append(f"### {r['label']} (`{r['id']}`)\n\n{body}- **From**: `{src}`\n- **Outcome**: open\n")
            log = re.sub(r"^None yet\.\n?", "", log, flags=re.M)
            logp.write_text(log.rstrip("\n") + "\n\n" + "\n".join(add))
            print(f"  wrote {len(new)} to {logp.relative_to(root)}")
    return 0 if found else 1


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--root", help="a checkout of jburnhams/taxonomies")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("lookup"); s.add_argument("domain"); s.add_argument("words", nargs="+")
    s.add_argument("--json", action="store_true"); s.set_defaults(f=cmd_lookup)
    s = sub.add_parser("changes"); s.add_argument("domain"); s.add_argument("--since", required=True)
    s.set_defaults(f=cmd_changes)
    s = sub.add_parser("intake"); s.add_argument("--repos", help="folder holding the domain repos' checkouts")
    s.add_argument("--write", action="store_true"); s.set_defaults(f=cmd_intake)
    a = p.parse_args(argv)
    return a.f(a)


if __name__ == "__main__":
    sys.exit(main())
