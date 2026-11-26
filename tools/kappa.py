#!/usr/bin/env python3
"""Agreement per facet between two or more raters' CSV answers (spec T8; method v1.1 M4, M5).

Each CSV has a header `id,<facet>,<facet>,...` (extra columns such as `note` are ignored
when not shared by all). Rows are matched by id; only ids every file has are compared.

- Two files: Cohen's kappa per facet, kappa = (p_o - p_e) / (1 - p_e) (prior knowledge;
  Cohen 1960 is not stored), and every disagreement.
- Three or more: Fleiss' kappa per facet across all raters (as TnT-LLM reports for
  multiple raters, Wan et al. 5.2.3), Cohen's kappa for every pair, the majority value
  per item (M5) and every item where the raters are not unanimous, marking three-way
  splits. Fleiss: P_bar = mean over items of (sum n_ij^2 - n) / (n(n-1)); P_e = sum p_j^2
  (prior knowledge; Fleiss 1971 is not stored).

Usage: python3 tools/kappa.py a.csv b.csv [c.csv ...] [--facets aspect,mode,...]
Rater names are the file names without `.csv`.
"""
import csv, sys
from collections import Counter
from itertools import combinations
from pathlib import Path


def load(p):
    with open(p, newline="") as f:
        return {r["id"].strip(): {k.strip(): (v or "").strip().strip("`").lower()
                                  for k, v in r.items() if k} for r in csv.DictReader(f)}


def cohen(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    return po, (1.0 if pe == 1 else (po - pe) / (1 - pe))


def fleiss(rows):
    """rows: one list of labels per item, all the same length (raters)."""
    N, n = len(rows), len(rows[0])
    counts = [Counter(r) for r in rows]
    cats = set().union(*counts)
    p_bar = sum((sum(v * v for v in c.values()) - n) / (n * (n - 1)) for c in counts) / N
    p_e = sum((sum(c[k] for c in counts) / (N * n)) ** 2 for k in cats)
    unanimous = sum(len(c) == 1 for c in counts) / N
    return unanimous, (1.0 if p_e == 1 else (p_bar - p_e) / (1 - p_e))


def main(argv):
    facets = None
    if "--facets" in argv:
        i = argv.index("--facets")
        facets = argv[i + 1].split(",")
        argv = argv[:i] + argv[i + 2:]
    if len(argv) < 2:
        sys.exit(__doc__)
    names = [Path(p).stem for p in argv]
    R = [load(p) for p in argv]
    ids = [i for i in R[0] if all(i in r for r in R[1:])]
    missing = sorted(set().union(*R) - set(ids))
    if not facets:
        first = next(iter(R[0].values()))
        facets = [k for k in first if k not in ("id", "note")]
    print(f"raters: {', '.join(names)}; items compared: {len(ids)}"
          + (f"; missing in some file: {missing}" if missing else ""))

    if len(R) == 2:
        print("\n| Facet | Agreement | Cohen's kappa |\n|---|---|---|")
        dis = []
        for f in facets:
            a = [R[0][i][f] for i in ids]; b = [R[1][i][f] for i in ids]
            po, k = cohen(a, b)
            print(f"| {f} | {po:.0%} | {k:.2f} |")
            dis += [(i, f, a[j], b[j]) for j, i in enumerate(ids) if a[j] != b[j]]
        print(f"\nDisagreements ({names[0]} / {names[1]}):")
        for d in dis:
            print(f"- `{d[0]}` {d[1]}: {d[2]} / {d[3]}")
        return

    pairs = list(combinations(range(len(R)), 2))
    head = " | ".join(f"{names[a]}-{names[b]}" for a, b in pairs)
    print(f"\n| Facet | Unanimous | Fleiss' kappa | {head} |")
    print("|---|---|---|" + "---|" * len(pairs))
    dis = []
    for f in facets:
        rows = [[r[i][f] for r in R] for i in ids]
        un, fk = fleiss(rows)
        cells = []
        for a, b in pairs:
            _, k = cohen([x[a] for x in rows], [x[b] for x in rows])
            cells.append(f"{k:.2f}")
        print(f"| {f} | {un:.0%} | {fk:.2f} | " + " | ".join(cells) + " |")
        for i, row in zip(ids, rows):
            c = Counter(row)
            if len(c) > 1:
                top, cnt = c.most_common(1)[0]
                maj = top if cnt * 2 > len(row) else None
                dis.append((i, f, row, maj))
    print(f"\nNot unanimous ({' / '.join(names)}); majority value, or SPLIT when none (M5):")
    for i, f, row, maj in dis:
        print(f"- `{i}` {f}: {' / '.join(row)} -> {maj or 'SPLIT'}")


if __name__ == "__main__":
    main(sys.argv[1:])
