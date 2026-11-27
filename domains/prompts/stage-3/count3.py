#!/usr/bin/env python3
"""Count control-area words in a checkout of jburnhams/prompts (stage-3 harvest).

Usage: python3 count3.py /path/to/prompts
"ctl" is the eight control docs (sample3.py CTX); "all" is every .md outside leaked/ and
skills/. Case-insensitive; each pattern is a regex over the text.
"""
import glob, os, re, sys

CTL = ["agent-permissions-approval.md", "agent-risk-assessment.md", "agent-run-recovery.md",
       "agent-run-steering.md", "agent-design/risk.md", "agent-design/keel/authority.md",
       "agent-design/keel/endings.md", "agent-design/keel/rules.md"]
TERMS = [
    ("approv-", r"\bapprov\w*"), ("permission", r"\bpermissions?\b"), ("risk", r"\brisks?\b"),
    ("tier", r"\btiers?\b"), ("policy", r"\bpolic(y|ies)\b"), ("blocking", r"\bblocking\b"),
    ("sandbox", r"\bsandbox\w*"), ("guardian", r"\bguardian\b"), ("retr(y|ies)", r"\bretr(y|ies|ied)\b"),
    ("classifier", r"\bclassifiers?\b"), ("escalat-", r"\bescalat\w*"), ("reminder", r"\breminders?\b"),
    ("system-reminder", r"\bsystem[- ]reminders?\b"), ("monitor", r"\bmonitors?\b"),
    ("resume", r"\bresum\w*"), ("authority", r"\bauthorit(y|ies)\b"), ("steer", r"\bsteer\w*"),
    ("nudge", r"\bnudg\w*"), ("guard", r"\bguard(s|rails?)?\b"), ("blast radius", r"\bblast radius\b"),
    ("completion gate", r"\bcompletion gates?\b"), ("allowlist / allow list", r"\ballow[- ]?lists?\b"),
    ("deny list / denylist", r"\bden(y|ied)[- ]?lists?\b"), ("prompt injection", r"\bprompt[- ]injections?\b"),
    ("idempot-", r"\bidempot\w*"), ("replay", r"\breplay\w*"), ("suspend-", r"\bsuspen(d|ds|ded|sion)\b"),
    ("budget", r"\bbudgets?\b"), ("stuck", r"\bstuck\b"), ("loop detect-", r"\bloop detect\w*"),
    ("trust", r"\btrust(ed|s)?\b"), ("driver", r"\bdrivers?\b"), ("confirm-", r"\bconfirm\w*"),
    ("confirmation polic-", r"\bconfirmation[ _]polic\w*"), ("auto mode", r"\bauto[- ]mode\b"),
    ("plan mode", r"\bplan mode\b"), ("yolo", r"\byolo\b"), ("interrupt", r"\binterrupt\w*"),
    ("abort", r"\babort\w*"), ("refus-", r"\brefus\w*"), ("deny", r"\bden(y|ies|ied)\b"),
    ("gate", r"\bgat(e|es|ed|ing)\b"), ("handoff", r"\bhand[- ]?offs?\b"), ("verdict", r"\bverdicts?\b"),
    ("checkpoint", r"\bcheckpoints?\b"), ("rollback / undo", r"\b(roll ?back|undo)\b"),
    ("destructive", r"\bdestructive\b"), ("irreversible", r"\birreversible\b"),
]

def main(root):
    os.chdir(root)
    allf = [f for f in glob.glob("**/*.md", recursive=True) if not f.startswith(("leaked/", "skills/"))]
    text = {f: open(f, encoding="utf-8", errors="replace").read() for f in allf}
    print("| Term (stem) | ctl | all | files |\n|---|---|---|---|")
    rows = []
    for name, pat in TERMS:
        rx = re.compile(pat, re.I)
        c = sum(len(rx.findall(text[f])) for f in CTL)
        a = [len(rx.findall(text[f])) for f in allf]
        rows.append((c, sum(a), sum(1 for n in a if n), name))
    for c, a, n, name in sorted(rows, reverse=True):
        print(f"| {name} | {c:,} | {a:,} | {n} |")

if __name__ == "__main__":
    main(sys.argv[1])
