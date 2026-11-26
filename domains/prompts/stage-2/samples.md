# Prompts taxonomy, stage 2 (context area): samples

**In one line**: 130 sections about the context area, drawn by a seeded rule from 32 files
of `jburnhams/prompts` and split into build (40), bare-facet test (12), round-1 test (30)
and held (48).

**In plain words**: stage 2 sorts only the mechanisms about what the model is given and
keeps (stage 1's `context` area). An item is still one section: its heading, the first
lines under it, and the file. Some sections in context docs turn out to be about another
area; raters say so, and those are left out of the stage-2 scores.

## How the items were drawn

Taken from `jburnhams/prompts` at commit `e7d4fb2` (2026-11-26) by
[`sample2.py`](./sample2.py), which reuses stage 1's item unit and filters
([`../sample.py`](../sample.py), method v1.1 M2 and M7).

- **Population**: every kept section of the eight context docs
  (`agent-context-compaction.md`, `agent-context-file-loading.md`,
  `agent-memory-learning.md`, `agent-prompt-cache-health.md`,
  `agent-design/context-files.md`, `agent-design/memory.md`,
  `agent-design/system-prompts.md`, `agent-design/keel/memory.md`): 97 sections. Plus
  every kept section elsewhere (stage 1's analysis docs, and this time the per-source
  folder READMEs) whose **heading** names a context mechanism (memory, learning,
  compaction, context file, system prompt, summary, truncation, reminder, retrieval,
  notes and similar; the list is `HEAD_KW` in the script). Matching the heading, not the
  text, keeps out sections that only mention memory in passing. A per-source section
  whose only text is "See `<doc>` for the cross-source comparison this feeds into" has
  no text of its own and is dropped.
- **Hand removals** (by heading, in `EXCLUDE`): "What changed from `medium.md` §6, and
  why", "What this implies for a new design", "What exists, and the gap" (meta), and a
  stored prompt line from PandasAI.
- **Drawn**: shuffled within each file and across files with seed `20261127`, then taken
  file by file in turn, as in stage 1.
- **Sizes** (method v1.1 M3): 30 per test round, which is J7's floor and five times the
  largest facet's values (`reach`, five values: 25). The population is small (130), so
  the held 48 cover one more full round and part of a third; if a third round is needed,
  the draw extends to `####` sections with the same seed.

Files: 32; most items from one file: 23 (`agent-memory-learning.md`).
[`items.csv`](./items.csv) has every item with its text.

## Build sample (40)

Used in harvest and finding facets. Not for testing.

| ID | Heading | From |
|---|---|---|
| `c01` | Scaffolding notes — what these actually do | `anthropic-skills/README.md` |
| `c02` | Placing injected text so it does not move the prefix | `agent-prompt-cache-health.md` |
| `c03` | Compaction needs a second budget, and a degradation says what it did not damage | `agent-design/cloudflare.md` |
| `c04` | Prompted-only instructions, no enforcement | `agent-self-verification.md` |
| `c05` | (d) Two instructions nobody else gives the reviewer | `code-review-approaches.md` |
| `c06` | Sub-agents & misc instructions | `copilot-chat/README.md` |
| `c07` | Which revision do the context files come from? | `github-pr-bots/README.md` |
| `c08` | How Forge and Lens would use it | `agent-design/keel/memory.md` |
| `c09` | The 2026-10-17 re-read: an attention axis, and memory of its own findings | `pr-agent/README.md` |
| `c10` | Agent Notes: decision memory with a lifecycle and a format gate | `deepseek-harness/README.md` |
| `c11` | Cross-run learning: a fourth entrypoint | `agent-design/medium.md` |
| `c12` | A summariser prompt the model refused, and summaries on an append-only thread (read 2026-11-09) | `agent-context-compaction.md` |
| `c13` | (c) Humans write it, and the agent is told to ask | `agent-memory-learning.md` |
| `c14` | Persistent memory & deployment as tools | `agent-tool-surfaces.md` |
| `c15` | Does the sub-agent get its own system prompt? | `agent-subagent-architectures.md` |
| `c16` | `btw.md`: a project context file with a tool manifest | `data-agents/btw/README.md` |
| `c17` | The scratchpad: a third position | `agent-data-analysis.md` |
| `c18` | Memory and learning — [`agent-memory-learning.md`](../agent-memory-learning.md) | `openclaw/README.md` |
| `c19` | Memory, learnings, and retrospectives | `cline/README.md` |
| `c20` | Memory, learnings, and retrospectives | `opencode/README.md` |
| `c21` | The response is a projection, and the cache entry is not | `agent-design/context-files.md` |
| `c22` | Memory, learnings, and retrospectives | `aider/README.md` |
| `c23` | SQL is an injected function, not a tool | `data-agents/pandasai/README.md` |
| `c24` | The memory prompts got ten times shorter | `codex/README.md` |
| `c25` | Guidance provenance in the report (amends §4a's closing note) | `agent-design/review.md` |
| `c26` | Context-file loading (`.goosehints` / `AGENTS.md`) | `goose/README.md` |
| `c27` | Retrieval as a second model call | `agent-tool-implementations.md` |
| `c28` | The shared reviewer core (`{{REVIEWER_CORE}}`) | `agent-design/system-prompts.md` |
| `c29` | Claude Code: two reminders and a requeue tool | `agent-run-recovery.md` |
| `c30` | Lifetime: images in the context window over time | `agent-vision-multimodal.md` |
| `c31` | What moves a prefix | `agent-prompt-cache-health.md` |
| `c32` | The learnings run promotes; the transcript pass is the fallback | `agent-design/memory.md` |
| `c33` | System prompt / preamble — what's sent before the diff | `code-review-approaches.md` |
| `c34` | How learnings reach a working run | `agent-design/medium.md` |
| `c35` | Sub-agent / multi-session isolation | `agent-context-compaction.md` |
| `c36` | Retrospectives: outcome triage and failure-to-prevention | `agent-memory-learning.md` |
| `c37` | Truncation, and what the notice should say | `agent-data-analysis.md` |
| `c38` | Context compaction — [`agent-context-compaction.md`](../agent-context-compaction.md) | `openclaw/README.md` |
| `c39` | What the run reports | `agent-design/context-files.md` |
| `c40` | Compaction and turn output | `aider/README.md` |

## Bare-facet test (12)

Classified in [`../facets.md`](../facets.md), "Stage 2". Not for testing.

| ID | Heading | From |
|---|---|---|
| `ct01` | Memory, learnings, and retrospectives | `codex/README.md` |
| `ct02` | Conditional format notes (`<format_notes>`) | `agent-design/review.md` |
| `ct03` | Memory, learnings, and retrospectives | `goose/README.md` |
| `ct04` | Memory is where Codex actually uses output schemas and namespaces | `agent-tool-implementations.md` |
| `ct05` | Conditional and just-in-time loading | `agent-context-file-loading.md` |
| `ct06` | Analysis prompts: the quick run and its landings | `agent-design/system-prompts.md` |
| `ct07` | Detecting a collapse: `WarnOnCacheBusts` | `agent-prompt-cache-health.md` |
| `ct08` | Requests are not context | `agent-design/memory.md` |
| `ct09` | Writing, validation and moderation | `agent-design/keel/memory.md` |
| `ct10` | What a learning may and may not do | `agent-design/medium.md` |
| `ct11` | Incremental/anchored summarization vs. from-scratch every time | `agent-context-compaction.md` |
| `ct12` | The writer that may place but may not author | `agent-memory-learning.md` |

## Round-1 test (30)

| ID | Heading | From |
|---|---|---|
| `cr01` | Kinds: one vocabulary, three resolutions | `agent-design/context-files.md` |
| `cr02` | Memory scoped to a sub-agent, not just to a project | `agent-tool-implementations.md` |
| `cr03` | MCP instructions, and the cache problem that shaped them | `agent-context-file-loading.md` |
| `cr04` | General-purpose delegate prompt (coding mode) | `agent-design/system-prompts.md` |
| `cr05` | The digest gate: most runs should produce nothing | `agent-design/memory.md` |
| `cr06` | Notes, memory and consolidation are three things | `agent-design/keel/memory.md` |
| `cr07` | Token budgeting — the numbers | `agent-context-compaction.md` |
| `cr08` | What is worth remembering: gates, taxonomies, and anti-rules | `agent-memory-learning.md` |
| `cr09` | Discovery (a specification for the service, not the harness) | `agent-design/context-files.md` |
| `cr10` | The truncation you cannot yet honestly claim | `agent-tool-implementations.md` |
| `cr11` | Budgets, truncation, and staleness | `agent-context-file-loading.md` |
| `cr12` | The `<prior_attempt>` paragraph (all landings) | `agent-design/system-prompts.md` |
| `cr13` | Subject: four kinds, one resolver | `agent-design/memory.md` |
| `cr14` | Substrate and retrieval: files for curated memory, search for episodic | `agent-design/keel/memory.md` |
| `cr15` | One mechanism vs. a layered pipeline vs. a pluggable strategy | `agent-context-compaction.md` |
| `cr16` | The tool surface: what the agent can actually do to its memory | `agent-memory-learning.md` |
| `cr17` | What the nonce does not cover | `agent-design/context-files.md` |
| `cr18` | Codex is building retrieval over the catalog — in shadow | `agent-context-file-loading.md` |
| `cr19` | The reviewer core, and the specialist wrapper | `agent-design/system-prompts.md` |
| `cr20` | Categories, with structure and per-category gates | `agent-design/memory.md` |
| `cr21` | Two things Codex's token-budget mode does that no summariser can | `agent-context-compaction.md` |
| `cr22` | OpenClaw's memory architecture (read from source) | `agent-memory-learning.md` |
| `cr23` | Narrowing, later: `paths` and `kinds` | `agent-design/context-files.md` |
| `cr24` | Trust gating, and why CI defeats it | `agent-context-file-loading.md` |
| `cr25` | The specialist wrapper (multi-stage sub-agent) | `agent-design/system-prompts.md` |
| `cr26` | A learning is a section | `agent-design/memory.md` |
| `cr27` | Claude Code at v2.1.303: four summariser prompts, and the user's words as a record | `agent-context-compaction.md` |
| `cr28` | What is actually injected, and where | `agent-memory-learning.md` |
| `cr29` | Injection point and the prompt cache | `agent-design/context-files.md` |
| `cr30` | The null case: Aider | `agent-context-file-loading.md` |

## Held for later rounds (48)

| ID | Heading | From |
|---|---|---|
| `ch01` | Review-mode system prompts (two shapes) | `agent-design/system-prompts.md` |
| `ch02` | What it is for | `agent-design/memory.md` |
| `ch03` | (b2) The working agent authors a *skill* on demand, with no distillation engine | `agent-memory-learning.md` |
| `ch04` | The envelope, and the nonce | `agent-design/context-files.md` |
| `ch05` | Which revision? (and: from which repository?) | `agent-context-file-loading.md` |
| `ch06` | The cost, stated plainly | `agent-design/memory.md` |
| `ch07` | When it runs: six trigger points | `agent-memory-learning.md` |
| `ch08` | Caching: every tier is a repo at a ref | `agent-design/context-files.md` |
| `ch09` | Hooks and plugins: assembled context, with weaker framing than files | `agent-context-file-loading.md` |
| `ch10` | `Retrospect` — in-session capture | `agent-design/memory.md` |
| `ch11` | (a) The working model writes, inline, as it works | `agent-memory-learning.md` |
| `ch12` | The atomic unit is a section, not a document | `agent-design/context-files.md` |
| `ch13` | Where the walk starts and stops | `agent-context-file-loading.md` |
| `ch14` | Three channels, and why they are three | `agent-design/memory.md` |
| `ch15` | Hermes Agent's memory (read from source) | `agent-memory-learning.md` |
| `ch16` | Three tiers, one source | `agent-design/context-files.md` |
| `ch17` | Beyond files: MCP, skills, hooks and plugins | `agent-context-file-loading.md` |
| `ch18` | Staleness, computed rather than declared | `agent-design/memory.md` |
| `ch19` | (b) A separate background agent reads finished transcripts | `agent-memory-learning.md` |
| `ch20` | Normalisation relocates an interpretation; it does not add one | `agent-design/context-files.md` |
| `ch21` | Templating: there is none | `agent-context-file-loading.md` |
| `ch22` | 4b-i. Claim strength: the gate decides whether, the wording decides how far | `agent-design/memory.md` |
| `ch23` | Nobody is doing RAG over agent memory | `agent-memory-learning.md` |
| `ch24` | What the file may instruct (and the review-mode reversal) | `agent-design/context-files.md` |
| `ch25` | Order, and the gap between claimed and structural precedence | `agent-context-file-loading.md` |
| `ch26` | Learnings arrive in the resolution | `agent-design/memory.md` |
| `ch27` | Levels: what scope does a memory belong to? | `agent-memory-learning.md` |
| `ch28` | Provenance: path and revision | `agent-design/context-files.md` |
| `ch29` | The negative sharpens: a harness with an escaper that doesn't point it here | `agent-context-file-loading.md` |
| `ch30` | `blocker` suspends, and it reuses machinery that exists | `agent-design/memory.md` |
| `ch31` | Memory as a platform resource (read 2026-11-02) | `agent-memory-learning.md` |
| `ch32` | Budget, and saying when it bit | `agent-design/context-files.md` |
| `ch33` | Escaping: nobody does it | `agent-context-file-loading.md` |
| `ch34` | The memory-first systems (secondhand, not re-read this pass) | `agent-memory-learning.md` |
| `ch35` | Every field, and what it is for | `agent-design/context-files.md` |
| `ch36` | Three postures on authority | `agent-context-file-loading.md` |
| `ch37` | Memory as an attack surface | `agent-memory-learning.md` |
| `ch38` | Just-in-time loading for deeper files | `agent-design/context-files.md` |
| `ch39` | Skills: a catalog in the prompt, a body on demand | `agent-context-file-loading.md` |
| `ch40` | Retrieval: pasted in, pointed at, searched, or triggered | `agent-memory-learning.md` |
| `ch41` | Inlining, and when not to | `agent-design/context-files.md` |
| `ch42` | Where it lands, and what that costs in cache | `agent-context-file-loading.md` |
| `ch43` | The channel that isn't memory: improvement requests | `agent-memory-learning.md` |
| `ch44` | Selection is the harness's job, and it is deterministic | `agent-design/context-files.md` |
| `ch45` | Claude Code's shipped memory prompts (v2.1.303) | `agent-memory-learning.md` |
| `ch46` | Retreats, absences, and capture gaps | `agent-memory-learning.md` |
| `ch47` | The review-tool loop: learning from humans instead of from yourself | `agent-memory-learning.md` |
| `ch48` | Who writes it: the working model, a background agent, or a human | `agent-memory-learning.md` |

## Sources cited

Denton's "In a large domain, get enough to cover all foreseen possibilities" and the
other reasons for the draw are cited in [`../samples.md`](../samples.md) and
[`design/method-v1.1.md`](../../../design/method-v1.1.md) M2-M3.
