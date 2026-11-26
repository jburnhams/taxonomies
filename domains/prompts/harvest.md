# Prompts taxonomy: term harvest (stage 1)

**In one line**: the words the prompts repo uses for its core concepts, with counts, the
synonym sets and homonyms they form, and the existing vocabularies to reuse.

**In plain words**: before choosing names, we count what the repo already says. Where
several words mean one thing (sub-agent, subagent) we will pick one and keep the rest as
aliases. Where one word means several things ("agent", "mode") we will split it.

Process step 3 ([`design/process.md`](../../design/process.md#step-3-harvest-the-words)).
Counted 2026-11-26 at `jburnhams/prompts` commit `a531474`, over the repo's own writing:
281 markdown files, about 815,000 words, not counting `leaked/` and `skills/` (stored
prompts, which keep their authors' words). Counts are whole-word, case-folded matches
(`grep -o -i -w`), so they include quotes and code names; treat them as order of
magnitude. "Files" is the number of the 281 that use the word.

## Existing vocabularies to reuse (step 0)

- **`agent-design/keel/taxonomy.md`** (618 lines, proposal of 2026-10-23): "One meaning per
  word" for Keel, Forge and Lens, with *Not* (near miss) and *Where* fields, words not
  used as concepts (§10) and collisions settled (§11). It is a glossary for the repo's
  own design, and the closest thing to a seed. It defines **Agent** as "one model context
  inside a run, with its own prompt, tools and tier", which is not the sense most of the
  research docs use (homonym 1 below).
- **`agent-archetypes.md`**: six archetypes of agent product (pair-programmer,
  benchmark solver, minimalist scaffold, multi-role pipeline, PR-review specialist, app
  generator). A classification of whole harnesses, not of mechanisms; candidate values
  if a later stage sorts sources.
- **Rombaut 2026, *Inside the Scaffold*** (stored in `papers/inside-the-scaffold/`,
  CC-BY 4.0): a source-code taxonomy of 13 coding agents in three layers, "control
  architecture, tool/environment interfaces, and resource management" (folder README;
  the PDF is not yet read for this harvest, ⚠). Its layers line up with three of the
  proposed `area` values (`control`/`coordination`, `tool`, `context`).
- **Per-topic taxonomies inside docs**: approval modes (`agent-permissions-approval.md`
  §1), risk dimensions (`agent-risk-assessment.md` §2), memory types
  (`agent-memory-learning.md`), Codex's four-tier confirmation taxonomy
  (`codex/README.md`). These become area facets in later stages (M1).

## Counts for the kernel candidates

| Concept (draft) | Words used, with counts (files) |
|---|---|
| the program around the model | harness 1,544 (170), SDK 452 (83), runtime 361 (97), framework 143 (40), scaffold 81 (27), host 367 (75), client 407 (100) |
| a model configured to act | agent 5,598 (227), agents 1,665 (171); "coding agent" 160, "the agent" 629, "review agent" 26, "data agent" 24 |
| the model itself | model 3,759 (210), LLM 308 (82), provider 345 (80), vendor 211 (84) |
| one execution | run 3,287 (219, noun and verb), session 1,019 (147), thread 457 (88), conversation 440 (126) |
| one model request and reply | turn 887 (143), step 663 (139), loop 398 (115) |
| the record of a run | transcript 410 (107), trace 122 (38), trajectory 49 (22), span 119 (28) |
| an action the model can take | tool call 206 (86), tool result 122 (58), "tool surface" 143 (67), toolset 30, tool group 17 |
| tools from outside | MCP server 132 (57), plugin 169 (44), extension 199 (69), connector 47 (23), MCP App 7 |
| packaged instructions | skill 685 (115), command 597 (107), slash command 7 |
| an agent started by an agent | sub-agent 481 (77), subagent 269 (64), worker 133 (36), fork 97 (43), delegate 141 (42) |
| the agent that starts others | orchestrator 281 (55), coordinator 26 (13) |
| fixed instructions | system prompt 258 (89), prompt 2,467 (187), instruction 357 (100) |
| repo instructions | AGENTS.md 425 (84), CLAUDE.md 102 (25), conventions 412, "instruction file" 22, "context file" 18, "rules file" 9 |
| keeping context small | compaction 501 (63), context window 69 (29), prompt cache 19 |
| what persists across runs | memory 1,215 (94) |
| leave to a person or other run | handoff 261, hand-off 17, "hand off" 14 |
| may it happen | approval 759 (113), permission 238 (80), policy 614 (113), sandbox 457 (102) |
| a second model that checks | reviewer 445 (86), judge 218 (58), classifier 134 (39), guardian 182 (23, mostly Codex's Guardian), monitor 65 (29), grader 39 (11), verifier 30 (18) |
| mid-run text from the harness | system-reminder 46, nudge 108, steer 103 |
| measuring an agent | benchmark 129, eval 182 (57), SWE-bench 90, self-verification 137 (42) |
| starting work | trigger 306 (80), pipeline 390 (80), workflow 320 (96), template 521 (100), hook 120 (44) |
| what a run produces | output 967 (183), artifact 573 (94), view 548 (90), widget 57, canvas 52 |

## Synonym sets (one concept, several words)

1. **sub-agent / subagent** (481 / 269): spelling only. Keel's taxonomy uses "sub-agent".
2. **handoff / hand-off / hand off** (261 / 17 / 14): spelling; Keel uses `handoff` as a
   terminal and `HandOff` as a tool.
3. **judge / grader / verifier / monitor / classifier**: overlapping words for a second
   model call that checks the first. The repo distinguishes some of them (a *blocking
   monitor* gates actions in `agent-permissions-approval.md` §2d; a *trajectory judge*
   steers in `agent-run-steering.md`; a *grader* scores in evals), so this is a cluster
   to split by role, not to merge.
4. **transcript / trajectory** (410 / 49): the ordered record of messages and tool
   calls; "trajectory" is the benchmark word (`telemetry/standards.md`).
5. **AGENTS.md / CLAUDE.md / conventions / instruction file / context file / rules file**:
   files in a repo that tell an agent how to work. `agent-context-file-loading.md` covers
   them under one heading; the repo has no single word.
6. **plugin / extension / connector**: packaging for added tools and skills; the
   difference is per product.
7. **pipeline / workflow**: Keel's `pipeline` is a defined chain of runs; "workflow" is
   also Claude Code's `Workflow` tool and a general word.

## Homonyms (one word, several concepts)

1. **agent**: (a) a product or harness ("coding agent", Claude Code, Codex; most research
   docs); (b) one model context inside a run (Keel's taxonomy §1); (c) a sub-agent
   definition file (`.claude/agents/*.md`, `subagent_type`, 40 uses); (d) anything that
   acts (OntoClean's *Agent* role). Decision J14 settles which sense the glossary uses.
2. **mode** (1,261 uses in 152 files): approval or permission mode (28), plan mode (81),
   auto mode (31), Forge's `mode: implement` / `mode: plan` (a run kind), Roo Code's
   modes (a persona), output and render modes. At least four concepts.
3. **surface** (684): "tool surface" (143, the set of tools a model is given), UI surface
   and render surface in output docs, and `ux:surface` (a tonal layer) in the
   neighbouring context.
4. **artifact** (573): Claude's Artifacts (a published page), Keel's artifact store
   (`artifact://` refs, 47), and build artefacts in CI.
5. **session** (1,019): a user's chat session, a harness process lifetime, and the
   MCP protocol session that the `2026-07-28` revision removed.
6. **review**: code review of a PR (a use case), self-review by the agent
   (`agent-self-verification.md` §"Review-as-a-general-tool — the conflation trap" is
   about exactly this), and a reviewer sub-agent.
7. **template**: Keel's template (a run spec with a name and params) and a prompt
   template.
8. **run**: noun (one execution, Keel) and verb.
9. **skill**: Anthropic Agent Skills (a packaged folder with `SKILL.md`) and a general
   capability.

## Jonathan's words

From the request of 2026-11-26: "agents, mcps, llm, harnesses, evals, everything really".
So `mcp` (as the protocol and its servers), `llm` and `eval` are warrant for preferred
labels where the repo is split.
