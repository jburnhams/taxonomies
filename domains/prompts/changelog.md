# Prompts taxonomy: changelog

Every change as a named operation (spec G4), newest day first. The approving agent is
named on each line (G1); Jonathan can reverse any of them.

## 2026-11-27

- **record** stage-3 round 1 (run on omarchy by the coordinator, `cc4b0e8`): Fleiss' κ
  target 0.83, response 0.80; non-Claude pair 0.75, 0.70; pass (J23). Name test 94% and
  97%, all seven revised entries right. **rename** value `grade` → "set a level" (ID
  kept); **redefine** `replay` (near miss for trace replay). `stage-3/rounds/round-1/review.md`:
  every ending condition holds apart from Jonathan's facet choice. Approved by: Claude (G1).
- **add** stage 3 (control area), `draft`: `stage-3/sample3.py`, `items.csv` (104 items
  at prompts `e7d4fb2`), `samples.md`, `count3.py`, `harvest.md`; facet set A (`target`,
  `response`) with sets B and C and a bare test in `facets.md`; 10 `candidate` value
  entries; the round-1 kit and name test in `stage-3/rounds/round-1/`; `scope.md` stage
  row and competency questions 21-27. Proposed by: Claude, after Jonathan said "Yes
  please" to stage 3.
- **add** `backlog.md` (method v1.1 M8, proposed as J27): 16 rows taken by stage 3, 8
  open. Proposed by: Claude, after Jonathan asked for new terms to be added as each
  decided concept opens more.
- **add** 16 `candidate` terms from the backlog: `escalation`, `risk-tier`,
  `risk-driver`, `allow-list`, `authority`, `blocking-monitor`, `run-budget`,
  `loop-detection`, `retry`, `replay`, `resume`, `suspension`, `completion-gate`,
  `prompt-injection`, `trust-gate`, `system-reminder`. T1-T6 clean apart from the listed
  `operations` flag. Approved by: Claude (G1).
- **redefine** `compaction` (R1: scope against `truncation`), `approval` (R4: a second
  model can approve), `permission-mode` (R5: near miss for approval policy files),
  `sandbox` (R6: near miss for worktree isolation). **split** `steer` (R2: aliases
  "system reminder", "reminder", "system-reminder" to the new `system-reminder`).
  **redefine** `handoff` (R3: alias "escalation" to the new `escalation`) and
  `precedence` (R7: alias "authority" to the new `authority`). All seven back to
  `candidate` for the stage-3 name test; [`stage-3/revision.md`](./stage-3/revision.md)
  has the reasons and the G6 list. Approved by: Claude (G1); Jonathan can veto.

## 2026-11-26

- **add** domain `prompts`: `scope.md` (draft, staged per method v1.1 M1), `harvest.md`,
  `samples.md` with `sample.py` and `items-all.csv` (192 items at prompts `a531474`),
  `facets.md` (sets A-C, bare-facet test). No glossary entries yet: they follow
  Jonathan's choice of facets (process step 4). Drafted by: Claude.
- **add** 18 `candidate` entries for set A's values to `glossary.md`; decider `model`
  renamed `working-model` before first use (label clash with area `model`). Drafted by:
  Claude; redone if Jonathan picks another set.
- **add** round-1 kit `rounds/round-1/` for three raters (Claude, OpenAI, Gemini Pro).
- **decide** facet set A (area, decider, moment): chosen by Jonathan on 2026-11-26.
- **decide** J14: `agent` = a model configured to act; Claude Code, Codex etc. are harnesses; sub-agent and reviewer are roles. Chosen by Jonathan on 2026-11-26.
- **add** 36 kernel `candidate` entries (agent, harness, agent SDK, model, model provider,
  run, session, transcript, trace, tool, tool surface, tool result, MCP, MCP server, MCP
  App, skill, plugin, hook, sub-agent, orchestrator, system prompt, context window,
  context file, compaction, memory, steer, approval, permission mode, sandbox, handoff,
  trigger, pipeline, eval, benchmark, self-verification, code review). Drafted and
  approved as candidates by: Claude; label choices 4-8 listed for Jonathan's veto.
- **rename** area values `model` "model" → "model access" and `tool` "tool" → "tool use";
  IDs unchanged. Area and decider aliases that named kernel concepts moved to them. The
  round-1 prompts were generated before this (commit `91d01cf`) and show the old labels;
  answers use IDs, so scoring is unaffected.
- **move** items `r06`, `r36`, `r48`, `r58` to the build sample and `h01`-`h04` into round 1
  (IDs kept): the facet comparison in `facets.md` and two glossary entries drew on the
  four, so they were no longer fresh (review on PR #9). Round-1 prompts regenerated; they
  now also show the relabelled area values.
- **score** round 1 (three raters, 60 items): area Fleiss' κ 0.93, decider 0.58 (fails),
  moment 0.72; non-Claude pair 0.92 / 0.57 / 0.69. Run on omarchy by the coordinator's
  session, commit `9778dc6`.
- **redefine** `working-model`, `rule`, `second-model`, `setup`: scope notes after round 1
  (table in `rounds/round-1/results.md`). Approved by: Claude.
- **add** round-2 kit `rounds/round-2/` (56 items `h05`-`h60`, prompts with the new rules).
- **score** round 2 (56 items `h05`-`h60`): Fleiss' κ area 0.87, decider 0.66, moment 0.72;
  non-Claude pair 0.87 / 0.54 (fails M4) / 0.67. Run on omarchy, commit `152c23d`.
- **redefine** `second-model`, `person`, `rule`: a separate model call decides however its
  prompt is built; starting is not deciding; surveys take what they recommend. Approved by:
  Claude.
- **add** 80 more items `g01`-`g80` by the same seeded draw (`sample.py`), eight dropped as
  meta; round-3 kit `rounds/round-3/` with `g01`-`g67` (60 items).
- **score** round 3 (60 items `g01`-`g67`): Fleiss' κ area 0.80, decider 0.77, moment 0.86;
  non-Claude pair 0.76 / 0.76 / 0.83. Every facet passes J23. No three-way split, so
  **Unsorted** is empty (T7). Run on omarchy, commit `bcdd92c`.
- **review** T10 (12 of 13 competency questions answered; "artifact" left for stage 2) and
  T11 (no unmarked synonym, no missing facet): `rounds/round-3/review.md`.
- **add** name-test prompt (T9) for the 54 labels: `rounds/round-3/name-test/prompt.md`.
- **review** name test (T9): openai 51/54 (94%), gemini 50/54 (93%), both above 80%:
  `rounds/round-3/name-test/results.md`. Graded by: Claude.
- **rename** `rule` label "rule" → "fixed logic" (alias "rule"); `model` label "model
  access" → "model calling" (alias "model access"). Ids kept. Both readers read "rule"
  as prompt text and "model access" as sign-in only. Approved by: Claude (G1).
- **redefine** `context-window` as a token limit on one request, reply included (the
  readers' sense); **add near miss** to `steer` for a person's mid-run message. Approved
  by: Claude (G1).
- **adopt** stage 1 (process step 10): every ending condition met on round 3. 50 terms
  `approved`, 4 `candidate` (the four above). Approved by: Claude under G1; Jonathan can veto.
- **add** stage 2 (context area), chosen over `control` for size and the repo's own
  memory-levels lens: `stage-2/sample2.py`, `samples.md`, `items.csv` (130 items from 32
  files at prompts `e7d4fb2`; build 40, bare test 12, round 1 30, held 48),
  `stage-2/harvest.md`. Drafted by: Claude.
- **add** stage-2 facet sets A-C to `facets.md` with a bare-facet test; set A
  (`operation`, `content`, `reach`) recommended, Jonathan to choose.
- **add** 12 `candidate` entries for set A's values to `glossary.md`.
- **add** competency questions 14-20 (stage 2) to `scope.md`.
- **add** stage-2 round-1 kit `stage-2/rounds/round-1/` (30 items, three prompts with an
  `in_area` question).
- **review** stage-2 round 1 (three raters on omarchy, commit `a52aea2`): Fleiss' κ on
  27 in-area items operation 0.82, content 0.88, reach 0.68; non-Claude pair 0.84 /
  0.82 / 0.53 (reach fails). `stage-2/rounds/round-1/results.md`.
- **add** `built-in-scope` to facet `reach` (text shipped with the harness or a
  configuration); **change** the `reach` principle (recordings take their readers'
  reach; unstated stores are `project-scope`) and `conversation-scope`'s scope (prior
  attempts). Approved by: Claude (G1), to be retested in round 2.
- **add** stage-2 round-2 kit `stage-2/rounds/round-2/` (`ch01`-`ch30`).
- **review** stage-2 round 2 (commit `733d917`, 28 in-area items): Fleiss' κ operation
  0.89, content 1.00, reach 0.84; non-Claude pair 0.83 / 1.00 / 0.83. Every facet passes
  J23; no three-way split.
- **add** 16 stage-2 `candidate` terms (learning, note, retrospective, consolidation,
  promotion, compaction summary, truncation, progressive disclosure, conditional
  loading, context-file import, envelope, precedence, staleness, write gate, scratchpad,
  index file). **change** `memory` (alias "learnings" moved to `learning`) and
  `context-file` (widened to user and org files); both back to `candidate`. `framing`
  aliases trimmed. Approved by: Claude (G1).
- **add** stage-2 name-test prompt (31 labels): `stage-2/rounds/round-2/name-test/prompt.md`.
- **review** stage-2 name test (T9): openai 29/31 (94%), gemini 30/31 (97%):
  `stage-2/rounds/round-2/name-test/results.md`. **rename** `note` label "note" → "work
  note" (alias kept); **add** near miss to `framing`. Approved by: Claude (G1).
- **review** stage-2 T10 (all seven questions answered) and T11 (nothing found):
  `stage-2/rounds/round-2/review.md`. Every ending condition holds except Jonathan's
  choice of facet set.
- **decide** stage-2 facet set A (`operation`, `content`, `reach`): chosen by Jonathan on
  2026-11-26.
- **adopt** stage 2 (process step 10): every ending condition met on round 2. Stage-2
  entries, `memory` and `context-file` set to `approved`; `work-note` stays `candidate`
  after its relabel. Approved by: Claude under G1; Jonathan can veto.
