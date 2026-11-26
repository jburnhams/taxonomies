# Prompts taxonomy, stage 2 (context area): term harvest

**In one line**: the words the prompts repo uses for the context area, counted at
`e7d4fb2`, with seven groups of synonyms, seven words that mean two things, the repo's
own classifications that became facets, and the terms stage 2 should define.

**In plain words**: before naming anything we count which words the repo already uses
and where it uses several words for one idea, or one word for several. Most of the
choices below follow the commonest word unless it is ambiguous.

Counted by script over the eight context docs ("ctx") and over every analysis doc and
per-source README ("all"; `leaked/` and `skills/` excluded), case-insensitive, word
stems as shown. Process step 3 ([`design/process.md`](../../../design/process.md)).

## Counts

| Term (stem) | ctx | all | files |
|---|---|---|---|
| memory | 734 | 1,567 | 66 |
| summar- (summary, summarise) | 194 | 772 | 89 |
| section | 187 | 711 | 89 |
| scope | 142 | 679 | 83 |
| tier | 139 | 678 | 71 |
| compaction | 129 | 551 | 55 |
| learning(s) | 121 | 344 | 35 |
| note(s) | 119 | 597 | 91 |
| consolidat- | 113 | 190 | 20 |
| inject- | 87 | 374 | 75 |
| level | 84 | 466 | 84 |
| index | 80 | 212 | 37 |
| retriev- | 78 | 194 | 69 |
| budget | 75 | 521 | 68 |
| envelope | 67 | 366 | 50 |
| context file | 62 | 209 | 49 |
| prefix | 58 | 265 | 61 |
| stale- | 53 | 196 | 46 |
| gate | 53 | 636 | 84 |
| knowledge | 50 | 88 | 26 |
| system prompt | 49 | 467 | 84 |
| resolution | 47 | 158 | 42 |
| promot- | 46 | 155 | 40 |
| truncat- | 36 | 294 | 55 |
| provenance | 31 | 260 | 59 |
| reminder | 30 | 125 | 29 |
| dream- | 26 | 42 | 6 |
| precedence | 25 | 65 | 23 |
| forget- | 24 | 49 | 19 |
| catalog(ue) | 23 | 192 | 48 |
| condens- | 22 | 58 | 7 |
| recall | 21 | 61 | 15 |
| import | 20 | 115 | 45 |
| just-in-time / JIT | 18 | 35 | 14 |
| on demand | 15 | 36 | 20 |
| hints | 15 | 48 | 15 |
| handoff | 15 | 272 | 45 |
| digest | 14 | 80 | 24 |
| prun- | 13 | 20 | 8 |
| distill- | 12 | 21 | 11 |
| retrospective | 11 | 39 | 17 |
| transclu- | 9 | 36 | 9 |
| scratchpad | 6 | 35 | 16 |
| evict- | 6 | 82 | 18 |
| authority | 6 | 171 | 42 |
| progressive disclosure | 4 | 14 | 12 |
| rules file | 3 | 21 | 12 |
| instruction file | 4 | 19 | 12 |

## Synonym sets

1. **Shrinking this run's context**: compaction 129, summarisation (summar- 194),
   condensation 22, context compression. Stage 1 chose `compaction` for the happening;
   "summary" is its product. Truncation 36, pruning 13 and eviction 6 also shrink, by
   cutting rather than rewriting. Facet value `reduction` covers all of them.
2. **What is kept across runs**: memory 734, learning 121, knowledge 50, note 119.
   Stage 1's `memory` has "learnings" as an alias. Keel's own docs separate notes,
   memory and consolidation as "three things" (`keel/memory.md` §16c), and
   `agent-design/memory.md` makes a learning one kind of section. Proposal: `learning`
   becomes a narrower term of `memory` (the alias moves), `note` its own entry.
3. **Repo instruction files**: context file 62, hints 15 (Goose), rules file 3,
   instruction file 4, steering file 2 (Kiro). Settled in stage 1 (`context-file`).
4. **Loading later, when needed**: just-in-time 18, on demand 15, progressive disclosure
   4 (Codex's own phrase), lazy 2. Two ideas: the model reads more when it decides to
   (progressive disclosure, index then detail), or the harness adds more when a path or
   keyword matches (conditional or just-in-time loading). Two entries.
5. **Shortening a store between runs**: consolidation 113, dreaming 26, distillation 12,
   promotion 46. "Dreaming" is one product's name for consolidation; promotion is moving a
   candidate into a store, a different act. Two entries: `consolidation`, `promotion`.
6. **How widely content applies**: level 84, scope 142, tier 139. Memory §1 says
   "level", the context service says "tier". The facet takes `reach` because "scope" is
   a field name in every glossary entry and "tier" also names model sizes.
7. **Text placed around loaded content**: envelope 67, wrapper, tag. `envelope` is
   commonest; a homonym (below).

## Homonyms

1. **injection**: loading text into the prompt (context) and a prompt-injection attack
   (control). The attack keeps "prompt injection"; the loading sense is `supply`.
2. **envelope**: the wrapper around loaded content (context-file loading §9) and Keel's
   run input ("in the envelope alongside the existing blocks", `agent-design/memory.md`
   §3c). Both in Keel's design; the first is the context sense.
3. **tier**: a context-service source tier (repo, user, org), a model size tier, and a
   memory tier (index, detail).
4. **index**: a memory index file in the prompt (memory §4, "index-plus-detail"), and a
   search index.
5. **section**: a heading in a doc, and the context service's "atomic unit"
   (`agent-design/context-files.md` §1b).
6. **scope**: memory level, a task's scope ("work outside your scope"), and a glossary
   field. Avoided as a label.
7. **note**: a Keel note (one pipeline run's memory), DeepSeek's "Agent Notes"
   (decision records), and the everyday sense.

## The repo's own classifications

- **Memory levels** (`agent-memory-learning.md` §1): task/turn, session, repo shared,
  repo private, user, org. Became facet `reach` (five values; repo shared and private
  merged into `project-scope`, task/turn into `request-scope` where it lasts one request
  and `conversation-scope` otherwise).
- **Who writes memory** (§2: working model, background agent, human) and **six trigger
  points** (§3): stage 1's `decider` and `moment`.
- **Retrieval modes** (§5: unconditionally injected, index then on-demand read, tool
  search, trigger-matched injection): Set C's `arrival`, kept as glossary terms.
- **Three postures on authority** (context-file loading §13: supreme, subordinate on
  safety, untrusted data): values of a possible stage-3 facet inside `framing`.
- **Compaction triggers** (compaction §1: proactive, reactive, manual): stage 1's
  `moment` and `decider`.
- **Four channels** for loaded context (context-file loading §12a: files, MCP
  instructions, skills, hooks and plugins): covered by `content` = `instruction-text`
  and the kernel entries.

## Terms for the stage-2 glossary

Drafted after Jonathan chooses the facet set; listed here so the choice can be judged.

`learning`, `note`, `retrospective`, `consolidation`, `promotion`, `compaction summary`,
`truncation`, `progressive disclosure`, `conditional loading`, `context-file import`,
`envelope`, `precedence`, `staleness`, `write gate` (Keel's digest gate is one),
`scratchpad`, `index file`.

## Stage-1 entries this touches

- `memory`: alias "learnings" moves to a new `learning` entry.
- `context-file`: "a file in a repo" leaves out a user's global file (`~/.claude/CLAUDE.md`)
  and org policy files, which the repo calls context files too (context service tiers).
  Widen to "a file that tells agents how to work and that a harness loads".
- `compaction`: unchanged; `reduction` is the operation, compaction one kind.
