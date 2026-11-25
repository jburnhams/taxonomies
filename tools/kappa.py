#!/usr/bin/env python3
"""Cohen's kappa per facet between two raters' CSV answers (spec T8).

Each CSV has a header `id,<facet>,<facet>,...` (extra columns such as `note` are ignored
when not shared by both). Rows are matched by id. kappa = (p_o - p_e) / (1 - p_e)
(prior knowledge; Cohen 1960 is not stored). Also lists every disagreement, since those
are what the next round fixes (Z39.19 §11.2.2).

Usage: python3 tools/kappa.py answers/a.csv answers/b.csv [--facets aspect,mode,...]
"""
import csv, sys
from collections import Counter


def load(p):
    with open(p, newline="") as f:
        return {r["id"].strip(): {k.strip(): (v or "").strip().strip("`").lower()
                                  for k, v in r.items() if k} for r in csv.DictReader(f)}


def kappa(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    return po, (1.0 if pe == 1 else (po - pe) / (1 - pe))


def main(pa, pb, *rest):
    A, B = load(pa), load(pb)
    ids = [i for i in A if i in B]
    missing = sorted(set(A) ^ set(B))
    facets = None
    if rest and rest[0] == "--facets":
        facets = rest[1].split(",")
    if not facets:
        first = next(iter(A.values()))
        facets = [k for k in first if k not in ("id", "note")]
    print(f"items compared: {len(ids)}" + (f"; missing in one file: {missing}" if missing else ""))
    print("| Facet | Agreement | Cohen's kappa |\n|---|---|---|")
    dis = []
    for f in facets:
        a = [A[i][f] for i in ids]; b = [B[i][f] for i in ids]
        po, k = kappa(a, b)
        print(f"| {f} | {po:.0%} | {k:.2f} |")
        dis += [(i, f, A[i][f], B[i][f]) for i in ids if A[i][f] != B[i][f]]
    print("\nDisagreements:")
    for d in dis:
        print(f"- `{d[0]}` {d[1]}: {d[2]} / {d[3]}")


if __name__ == "__main__":
    main(*sys.argv[1:])
