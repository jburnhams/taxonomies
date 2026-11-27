#!/usr/bin/env python3
"""Draw the stage-3 (control area) samples from a checkout of jburnhams/prompts.

Usage: python3 sample3.py /path/to/prompts > items.csv
Same item unit, filters and draw as stage 2 (../stage-2/sample2.py, which reuses stage 1's
../sample.py); only the control docs, the heading words, the seed and the sets differ.
"""
import importlib.util, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("s2", os.path.join(HERE, "..", "stage-2", "sample2.py"))
s2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(s2)

s2.SEED = 20261128
s2.CTX = ["agent-permissions-approval.md", "agent-risk-assessment.md", "agent-run-recovery.md",
          "agent-run-steering.md", "agent-design/risk.md", "agent-design/keel/authority.md",
          "agent-design/keel/endings.md", "agent-design/keel/rules.md"]
s2.HEAD_KW = re.compile(
    r"\b(approv\w*|permissions?|sandbox\w*|risk\w*|guard\w*|monitors?|steer\w*|nudges?|recover\w*|"
    r"retr(y|ies)|stopped|stopping|blocking|blocked|blocker|trust\w*|polic(y|ies)|allow\w*|den(y|ies|ied)|escalat\w*|"
    r"interrupt\w*|abort\w*|confirm\w*|loop detection|budgets?|limits?|endings?|completion gate|authority|"
    r"authori[sz]\w*|safety|unsafe|destructive|prompt injection|yolo|auto mode|plan mode)\b", re.I)
s2.EXCLUDE = set()
s2.SETS = [("k", 30), ("kt", 10), ("kr", 30), ("kh", 400)]

if __name__ == "__main__":
    s2.main(sys.argv[1])
