#!/usr/bin/env python3
"""Mechanical checks T1-T6 on one domain's glossary.md and facets.md (spec §10, J19).

T1 integrity, T2 labels, T3 name form, T4 definition form, T5 kinds, T6 facets.
Prints one line per problem and exits 1 if any. Heuristic where the spec asks for
judgement (T3's evaluative-word list, plural endings): it flags, a person decides.

Usage: python3 tools/check_domain.py domains/ux
"""
import re, sys
from pathlib import Path

REQ = ["Definition", "Scope", "Example", "Near miss", "Kind", "Status", "Warrant", "History"]
KINDS = {"thing", "property", "role", "happening"}
CLAIM = {"type", "class", "kind", "category", "sort"}
CATCH = {"other", "misc", "miscellaneous", "unknown", "general"}
EVAL = {"legacy", "hacky", "minor", "bad", "good", "proper", "best", "nice", "ugly", "modern", "clean"}
STATUSW = {"new", "old", "deprecated", "draft", "final", "v1", "v2"}


def parse_glossary(text):
    recs = {}
    for m in re.finditer(r"^### (.+?) \(`([\w-]+)`\)\n(.*?)(?=^### |\Z)", text, re.M | re.S):
        label, rid, body = m.groups()
        f = dict(re.findall(r"^- \*\*([^*]+)\*\*: (.*)$", body, re.M))
        dup = rid in recs
        recs[rid] = {"label": label, **f, "_dup": dup or recs.get(rid, {}).get("_dup", False)}
    return recs


def ids_in(v):
    return re.findall(r"`([\w-]+)`", v or "")


def main(domain):
    d = Path(domain)
    G = parse_glossary((d / "glossary.md").read_text())
    F = (d / "facets.md").read_text()
    err = []
    fold = lambda s: re.sub(r"[-\s]+", " ", s.strip().lower())
    # T1
    for rid, r in G.items():
        if r.get("_dup"): err.append(f"T1 {rid}: duplicate id")
        for k in REQ:
            if not r.get(k): err.append(f"T1 {rid}: missing {k}")
        b = ids_in(r.get("Broader")); rel = ids_in(r.get("Related"))
        for x in b + rel + ids_in(r.get("Replaced by")):
            if x not in G: err.append(f"T1 {rid}: refers to missing `{x}`")
        if rid in b + rel: err.append(f"T1 {rid}: related to itself")
        if set(b) & set(rel): err.append(f"T1 {rid}: both broader and related to {set(b) & set(rel)}")
    for rid in G:
        seen, cur = set(), rid
        while True:
            b = ids_in(G[cur].get("Broader")) if cur in G else []
            if not b: break
            cur = b[0]
            if cur in seen or cur == rid: err.append(f"T1 {rid}: cycle in broader"); break
            seen.add(cur)
    # T2
    labels = {}
    for rid, r in G.items():
        ls = [r["label"]] + [a for a in (r.get("Aliases") or "").split(",") if a.strip()] \
             + [a for a in (r.get("Hidden") or "").split(",") if a.strip()]
        for l in ls:
            k = fold(l)
            if k in labels and labels[k] != rid: err.append(f"T2 label '{l.strip()}' on `{rid}` and `{labels[k]}`")
            labels[k] = rid
        if r.get("Status", "").startswith("deprecated") and not ids_in(r.get("Replaced by")):
            err.append(f"T2 {rid}: deprecated without Replaced by")
    # T3
    for rid, r in G.items():
        words = re.findall(r"[a-z0-9]+", r["label"].lower())
        if {"and", "or"} & set(words): err.append(f"T3 {rid}: 'and'/'or' in label")
        if any(w.startswith("non") or w == "not" for w in words): err.append(f"T3 {rid}: negation in label")
        for s, name in [(CLAIM, "claim word"), (CATCH, "catch-all"), (EVAL, "evaluative word"), (STATUSW, "status word")]:
            if set(words) & s: err.append(f"T3 {rid}: {name} {set(words) & s}")
        if re.search(r"\d{4}", r["label"]): err.append(f"T3 {rid}: date in label")
        if words and words[-1].endswith("s") and not words[-1].endswith(("ss", "us", "is")):
            err.append(f"T3 {rid}: possible plural '{words[-1]}' (check)")
    # T4
    for rid, r in G.items():
        dfn = r.get("Definition", ""); lab = r["label"]
        b0 = ids_in(r.get("Broader"))
        mass = re.escape(G[b0[0]]["label"]) + " " if b0 and b0[0] in G else "(?!)"
        pat = rf"^(A |An |The )?{re.escape(lab)} is (a |an |{mass})"
        proper = r.get("Kind") == "thing" and re.match(rf"^{re.escape(lab)} is the ", dfn) and lab[0].islower() and "-" in lab
        if not re.match(pat, dfn, re.I) and not proper: err.append(f"T4 {rid}: does not start '<label> is a'")
        after = re.split(r" is an? ", dfn, maxsplit=1)
        if len(after) == 2 and re.search(rf"\b{re.escape(lab.lower())}\b", after[1].lower()):
            err.append(f"T4 {rid}: label repeated after 'is a' (circular?)")
        if re.search(r"\b(usually|generally|e\.g\.|for example)\b", dfn, re.I): err.append(f"T4 {rid}: hedge or example in definition")
        b = ids_in(r.get("Broader"))
        if b and b[0] in G and len(after) == 2:
            gl = G[b[0]]["label"].lower()
            if not after[1].lower().startswith(gl): err.append(f"T4 {rid}: genus is not broader term '{gl}'")
    # T5
    for rid, r in G.items():
        if r.get("Kind") not in KINDS: err.append(f"T5 {rid}: kind '{r.get('Kind')}'")
        for b in ids_in(r.get("Broader")):
            if b in G and G[b].get("Kind") in ("role", "happening") and r.get("Kind") == "thing":
                err.append(f"T5 {rid}: thing under {G[b].get('Kind')} `{b}`")
    # T6
    for fm in re.finditer(r"^### (.+?) \(`([\w-]+)`\)\n(.*?)(?=^##|\Z)", F, re.M | re.S):
        fid, body = fm.group(2), fm.group(3)
        vm = re.search(r"^- \*\*Values\*\*: (.*?)(?=^- \*\*|\Z)", body, re.M | re.S)
        if not vm: continue
        top = re.sub(r"\([^)]*\)", "", vm.group(1))
        vals = re.findall(r"(?:^|,\s*)`([\w-]+)`", top.strip())
        if len(vals) < 2: err.append(f"T6 facet {fid}: fewer than two values")
        if len(vals) > 12: err.append(f"T6 facet {fid}: more than a dozen values")
        for v in vals:
            if v not in G: err.append(f"T6 facet {fid}: value `{v}` has no glossary entry")
            elif fid not in ids_in(G[v].get("Facet")): err.append(f"T6 `{v}`: Facet field does not name `{fid}`")
    for e in err: print(e)
    print(f"{len(G)} terms checked; {len(err)} problem(s)")
    return 1 if err else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
