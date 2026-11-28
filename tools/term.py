#!/usr/bin/env python3
"""Look up the term to use, see what changed, and gather term requests (design/growth.md).

A domain repo (prompts, ux-research, ...) uses this to ask "which word do I use for this
concept?" before it writes one, and to see what changed in its glossary since its last
pass. Requests are issues in jburnhams/taxonomies (form: .github/ISSUE_TEMPLATE/term-request.yml);
the taxonomies repo uses `intake` to log them. Issues are read from the public API (set
$GITHUB_TOKEN to raise the rate limit).
Standard library only, one file, so it runs without a checkout of this repo:

  curl -fsSL https://raw.githubusercontent.com/jburnhams/taxonomies/main/tools/term.py \\
    | python3 - lookup prompts "approval timeout"

Commands:
  lookup DOMAIN WORDS...       the term for these words: an exact label match, else the
                               closest terms, plus any request already made for them
  changes DOMAIN --since DATE  operations logged on or after DATE (YYYY-MM-DD), breaking ones
                               marked, and requests answered since then
  intake [--write]             (taxonomies repo) open term-request issues not yet logged,
                               each with its lookup; --write adds them to
                               domains/<name>/requests.md as `open` (ID issue-<number>)

Where the files come from: --root DIR, else $TAXONOMIES_ROOT, else this script's own repo
when it sits in a checkout, else raw.githubusercontent.com (main branch).
Exit codes for lookup: 0 an exact label matched, 1 only near terms, 2 nothing found.
"""
import argparse, json, os, re, sys, urllib.request
from pathlib import Path

RAW = "https://raw.githubusercontent.com/jburnhams/taxonomies/main/"
BREAKING = {"rename", "split", "merge", "move", "deprecate"}
OPS = BREAKING | {"add", "redefine", "alias", "adopt", "record", "review", "score", "decide"}
OUTCOMES = {"open", "use", "alias", "candidate", "clarified", "changed", "backlog", "declined"}  # growth R1
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

def lookup(root, domain, query, with_issues=False):
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
    # an open request matches on its label or concept; an answered one on its label only,
    # since its answer is in the glossary and a concept-word match is then mostly noise
    asked = [r for r in reqs if q == fold(r["label"]) or (qw and outcome(r) == "open" and len(qw & words(r["label"] + " " + r.get("Concept", ""))) >= max(1, len(qw) - 1))]
    if with_issues:  # open issues not yet logged, so both output modes report the same requests
        try:
            known = {r["id"] for r in asked}
            for i in request_issues("open"):
                if issue_domain(i) == domain and f"issue-{i['number']}" not in known and (
                        fold(issue_word(i)) == q or (qw and qw <= words(issue_word(i) + " " + i.get("Concept", "")))):
                    asked.append({"label": issue_word(i), "id": f"issue-{i['number']}", "Outcome": "open", "Asked": i["url"]})
        except Exception:
            pass
    return terms, exact, near, asked


def outcome(r):
    """The first word of a request record's Outcome (`use`, `backlog`, ...); 'open' if unset."""
    m = re.match(r"[`*\s]*([a-z]+)", r.get("Outcome") or "open")
    return m.group(1) if m else "?"


def short(v, n=160):
    """The first sentence of a long field, for one-line listings."""
    v = (v or "").split(". ")[0]
    return v if len(v) <= n else v[:n - 1] + "…"


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
    terms, exact, near, asked = lookup(root, a.domain, query, with_issues=True)
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
                print(f"  {r['label']} (`{r['id']}`): {short(r.get('Outcome', 'open'))}  [{r.get('Answered') or r.get('Asked', '')}]")
        if not exact:
            print("If none fits, use your own word now and file a term-request issue in "
                  "jburnhams/taxonomies (fields: design/growth.md#the-request-issue).")
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
            if max((r.get("Answered") or "")[:10], (r.get("Taken") or "")[:10]) >= a.since]
    print(f"{a.domain}: changes on or after {a.since}, newest first (the day itself is included, so lines seen last time may repeat)")
    if not rows and not reqs:
        print("  none")
    for day, text, ops in rows:
        print(f"  {day} {'BREAKING ' if brk(text, ops) else ''}{text}")
    if reqs:
        print("Requests answered:")
        for r in reqs:
            taken = f"; taken as {short(r['Taken'])}" if r.get("Taken") else ""
            print(f"  {r['label']} (`{r['id']}`): {short(r.get('Outcome', ''))}{taken}  [{r.get('Answered', '')}]")
    if any(brk(t, ops) for _, t, ops in rows):
        print("Breaking changes: switch old labels to the new ones in docs you touch "
              "(`lookup` on an old label names its replacement).")
    return 0


# ---------- intake (run in the taxonomies repo) ----------

API = "https://api.github.com/repos/jburnhams/taxonomies/issues"
FIELDS = {"domain": "Domain", "ask": "Ask", "word": "Word", "term": "Term", "concept": "Concept",
          "looked at": "Looked at", "example": "Example", "warrant": "Warrant", "asked": "Asked"}


def issue_fields(body):
    """The `### Field` sections of a term-request issue (the issue form's output, or an agent's body)."""
    out = {}
    for m in re.finditer(r"^### (.+?)\s*\n(.*?)(?=^### |\Z)", body or "", re.M | re.S):
        k = FIELDS.get(m.group(1).strip().lower())
        v = m.group(2).strip()
        if k and v and v != "_No response_":
            out[k] = " ".join(v.split())
    return out


def request_issues(state="open"):
    """Term-request issues: label `term-request`, or a title starting "[term]". Public repo, no token needed."""
    out, page = [], 1
    while True:
        req = urllib.request.Request(f"{API}?state={state}&per_page=100&page={page}",
                                     headers={"Accept": "application/vnd.github+json"})
        tok = os.environ.get("GITHUB_TOKEN")
        if tok:
            req.add_header("Authorization", f"Bearer {tok}")
        with urllib.request.urlopen(req, timeout=20) as r:
            batch = json.load(r)
        for i in batch:
            if "pull_request" in i:
                continue
            if any(l["name"] == "term-request" for l in i.get("labels", [])) or i["title"].lower().startswith("[term]"):
                f = issue_fields(i.get("body"))
                out.append({"number": i["number"], "url": i["html_url"], "title": i["title"], "state": i["state"], **f})
        if len(batch) < 100:
            return out
        page += 1


def issue_domain(i):
    d = (i.get("Domain") or "").strip().lower()
    if not d:
        m = re.match(r"\[term\]\s*([\w-]+)\s*:", i["title"], re.I)
        d = m.group(1).lower() if m else ""
    return d


def issue_word(i):
    return i.get("Word") or re.sub(r"^\[term\]\s*[\w-]+\s*:\s*", "", i["title"], flags=re.I)


def cmd_intake(a):
    root = find_root(a.root)
    if not root:
        sys.exit("term.py intake: run it in a checkout of jburnhams/taxonomies (or pass --root)")
    try:
        every = request_issues("all")
    except Exception as e:
        sys.exit(f"term.py intake: cannot read issues from {API}: {e}")
    issues = [i for i in every if i["state"] == "open"]
    domains = {p.name: p for p in (root / "domains").iterdir() if (p / "glossary.md").exists()}
    found = 0
    for i in issues:
        d = issue_domain(i)
        if d not in domains:
            print(f"#{i['number']} {i['title']}: no domain '{d}' (set the Domain field)")
            continue
        rid = f"issue-{i['number']}"
        logp = domains[d] / "requests.md"
        log = logp.read_text() if logp.exists() else ""
        if rid in {r["id"] for r in records(log)}:
            continue
        found += 1
        word = issue_word(i)
        print(f"\n{d}: #{i['number']} {word} ask: {i.get('Ask', 'new')}  term: {i.get('Term', '-')}  {i['url']}")
        print(f"    Concept: {i.get('Concept', '')}")
        terms, exact, near, _ = lookup(root, d, word)
        print("    Lookup: " + (", ".join(f"`{t['id']}`" + (" (exact)" if t in exact else "") for t in exact or near) or "nothing"))
        if a.write:
            body = "".join(f"- **{k}**: {i[k]}\n" for k in FIELDS.values() if i.get(k) and k not in ("Domain", "Word"))
            rec = f"### {word} (`{rid}`)\n\n{body}- **From**: [#{i['number']}]({i['url']})\n- **Outcome**: open\n"
            log = re.sub(r"^None yet\.\n?", "", log, flags=re.M)
            logp.write_text(log.rstrip("\n") + "\n\n" + rec)
            print(f"    wrote `{rid}` to {logp.relative_to(root)}")
    print(f"\n{found} new request(s) of {len(issues)} open term-request issue(s)")
    drift = check_records(root, domains, {f"issue-{i['number']}": i for i in every})
    for line in drift:
        print(line)
    return 0 if found or drift else 1


def check_records(root, domains, by_id):
    """Records whose outcome is not one of R1's, or whose state disagrees with their issue (R7)."""
    out = []
    for d, path in sorted(domains.items()):
        for r in records((path / "requests.md").read_text() if (path / "requests.md").exists() else ""):
            o, i = outcome(r), by_id.get(r["id"])
            where = f"{d}: `{r['id']}` {r['label']}"
            if o not in OUTCOMES:
                out.append(f"{where}: outcome '{o}' is not one of {', '.join(sorted(OUTCOMES))} (growth R1)")
            if o != "open" and not r.get("Answered"):
                out.append(f"{where}: outcome set but no **Answered** (date, by)")
            if i and o == "open" and i["state"] == "closed":
                out.append(f"{where}: still `open` here but issue #{i['number']} is closed (answer it, or reopen the issue)")
            if i and o != "open" and i["state"] == "open":
                out.append(f"{where}: answered `{o}` here but issue #{i['number']} is open (comment the outcome and close it)")
    if out:
        out.insert(0, "\nRecords to fix:")
    return out


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--root", help="a checkout of jburnhams/taxonomies")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("lookup"); s.add_argument("domain"); s.add_argument("words", nargs="+")
    s.add_argument("--json", action="store_true"); s.set_defaults(f=cmd_lookup)
    s = sub.add_parser("changes"); s.add_argument("domain"); s.add_argument("--since", required=True)
    s.set_defaults(f=cmd_changes)
    s = sub.add_parser("intake")
    s.add_argument("--write", action="store_true"); s.set_defaults(f=cmd_intake)
    a = p.parse_args(argv)
    return a.f(a)


if __name__ == "__main__":
    sys.exit(main())
