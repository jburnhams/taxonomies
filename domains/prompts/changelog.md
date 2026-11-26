# Prompts taxonomy: changelog

Every change as a named operation (spec G4), newest day first. The approving agent is
named on each line (G1); Jonathan can reverse any of them.

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
