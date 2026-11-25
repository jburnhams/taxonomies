#!/usr/bin/env python3
"""Check that the design docs cite stored sources.

For each file given (default: design/spec.md and design/process.md):
  1. every relative link, inline or reference-style, points to a file that exists;
  2. every reference key used ([text][key]) is defined;
  3. every rule (a bullet starting "- **S1." style) and every "## Step" section cites
     at least one file under sources/, or carries a ⚠ marker saying its source is not
     stored.

Exit status 1 if anything fails. Usage: python3 tools/check_citations.py [files...]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT = ["design/spec.md", "design/process.md"]

REF_DEF = re.compile(r"^\[([^\]]+)\]:\s*(\S+)", re.M)
REF_USE = re.compile(r"\]\[([^\]]+)\]")
INLINE = re.compile(r"\]\(([^)\s]+)\)")
RULE = re.compile(r"^- \*\*([A-Z]\d+)\.", re.M)
STEP = re.compile(r"^## Step (\d+)", re.M)


def blocks(text, pattern, stop):
    """Yield (label, body) for each match of pattern, ending at the next stop match."""
    starts = [(m.start(), m.group(1)) for m in pattern.finditer(text)]
    for start, label in starts:
        nxt = stop.search(text, start + 1)
        end = nxt.start() if nxt else len(text)
        yield label, text[start:end]


def check(path):
    errors = []
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"^```.*?^```", "", text, flags=re.M | re.S)  # ignore code examples
    defs = dict(REF_DEF.findall(text))

    for key in set(REF_USE.findall(text)):
        if key not in defs:
            errors.append(f"reference [{key}] used but not defined")

    targets = list(defs.values()) + INLINE.findall(text)
    for target in targets:
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            continue
        file_part = target.split("#", 1)[0]
        if not (path.parent / file_part).exists():
            errors.append(f"link target missing: {target}")

    source_keys = {k for k, v in defs.items() if "sources/" in v}

    def cites_source(body):
        if "⚠" in body:
            return True
        if any(f"][{k}]" in body for k in source_keys):
            return True
        return "../sources/" in body

    rule_stop = re.compile(r"^(- \*\*[A-Z]\d+\.|#{2,3} )", re.M)
    for label, body in blocks(text, RULE, rule_stop):
        if not cites_source(body):
            errors.append(f"rule {label} cites no stored source")
    for label, body in blocks(text, STEP, re.compile(r"^## ", re.M)):
        if not cites_source(body):
            errors.append(f"step {label} cites no stored source")
    return errors


def main(argv):
    files = argv[1:] or DEFAULT
    failed = False
    for name in files:
        path = (ROOT / name) if not Path(name).is_absolute() else Path(name)
        errors = check(path)
        status = "ok" if not errors else f"{len(errors)} problem(s)"
        print(f"{name}: {status}")
        for e in errors:
            print(f"  - {e}")
        failed = failed or bool(errors)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
