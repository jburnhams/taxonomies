# Prompts taxonomy: samples

**In one line**: 192 section headings from `jburnhams/prompts`, drawn by a seeded shuffle
across 67 files and split into build (64), bare-facet test (12), round-1 test (60) and
held (56); four round-1 items moved to build after the facet work drew on them.

**In plain words**: an *item* is one section of the repo's own analysis: a heading such as
"Deterministic, non-LLM completion gates" plus the first lines under it. Each one
describes one mechanism, approach or design choice. We sort the build items to find the
sorting questions, then sort items nobody has looked at to see whether the questions work.

## How the items were drawn

Taken from `jburnhams/prompts` at commit `a531474` (2026-11-26).

- **Population** (proposal M2 in [`design/method-v1.1.md`](../../design/method-v1.1.md)):
  every `##` and `###` section of the repo's own analysis docs: the 30 cross-source docs
  at the root (not `README.md`, `changelog.md`, `sources.md`), `agent-design/*.md` (not
  the `proposals-*` files), `agent-design/keel/*.md`, `telemetry/*.md`,
  `code-mode/README.md` and `mcp-apps/README.md`: 1,070 sections. Stored prompts
  (`leaked/`, `skills/`, per-source folders) are the repo's sources, not its analysis,
  and are left out of stage 1.
- **Kept**: headings of at least four words, not a meta heading (sources covered, design
  takeaways, status, "what this pass ...", "answers to the questions asked" and the like),
  with at least 60 characters of text under them: 584 sections.
- **Drawn**: shuffled within each file and across files with seed `20261126`, then taken
  file by file in turn, so each file gives two or three items before any gives more
  (variety, not chance: [Denton §2.3 step 1][den], "In a large domain, get enough to
  cover all foreseen possibilities"). Eighteen of the first 210 were dropped by hand as
  meta sections the filter missed (for example "What this does not change",
  "Corrections to this collection"); the next items filled their places.
- **Sizes** (proposal M3): 60 per test round, twice J7's 30, because the largest facet has
  eight values. [`sample.py`](./sample.py) reproduces the draw from a checkout;
  [`items-all.csv`](./items-all.csv) has all 192 with the text under each heading. IDs
  never change when an item moves.

## Build sample (64)

Used in steps 3-4 (harvest, finding facets). Not for testing. The last four rows were moved in from the round-1 set on 2026-11-26, because the facet comparison and the glossary drew on them; `h01`-`h04` replaced them in round 1 (IDs kept).

| ID | Item (section heading) | From |
|---|---|---|
| `b01` | Chat with a viewer | [agent-data-analysis.md](https://github.com/jburnhams/prompts/blob/a531474/agent-data-analysis.md) |
| `b02` | Showing a session: the views that recur | [telemetry/platforms-and-storage.md](https://github.com/jburnhams/prompts/blob/a531474/telemetry/platforms-and-storage.md) |
| `b03` | Other providers (added 2026-10-22) | [agent-deferred-tool-loading.md](https://github.com/jburnhams/prompts/blob/a531474/agent-deferred-tool-loading.md) |
| `b04` | Who sets the level | [agent-risk-assessment.md](https://github.com/jburnhams/prompts/blob/a531474/agent-risk-assessment.md) |
| `b05` | The tier chooses the run shape | [agent-design/risk.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/risk.md) |
| `b06` | Two more candidate patterns from Google Antigravity | [agent-self-verification.md](https://github.com/jburnhams/prompts/blob/a531474/agent-self-verification.md) |
| `b07` | What moves a prefix | [agent-prompt-cache-health.md](https://github.com/jburnhams/prompts/blob/a531474/agent-prompt-cache-health.md) |
| `b08` | Completion tools: separate tools, or a flag on a tool? | [agent-design/keel/endings.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/endings.md) |
| `b09` | Groups, grants and visibility | [agent-design/keel/tools-and-agents.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/tools-and-agents.md) |
| `b10` | `Read` is a converting reader | [agent-design/artifacts.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/artifacts.md) |
| `b11` | Claude Code at v2.1.303: provenance as a list of who is not the user | [agent-content-provenance.md](https://github.com/jburnhams/prompts/blob/a531474/agent-content-provenance.md) |
| `b12` | Marking something as *for the user* | [agent-tool-result-transport.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-result-transport.md) |
| `b13` | Narration: a genuinely separate mechanism from native reasoning display | [agent-turn-output.md](https://github.com/jburnhams/prompts/blob/a531474/agent-turn-output.md) |
| `b14` | v1 in one list | [agent-design/vision.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/vision.md) |
| `b15` | Three verbs, and the constraint that produces them | [agent-design/orchestration.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/orchestration.md) |
| `b16` | A learning is a section | [agent-design/memory.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/memory.md) |
| `b17` | General-purpose interactive pair-programmer ("kitchen sink") | [agent-archetypes.md](https://github.com/jburnhams/prompts/blob/a531474/agent-archetypes.md) |
| `b18` | Email turns: whose words count, and what a bare "yes" approves | [agent-permissions-approval.md](https://github.com/jburnhams/prompts/blob/a531474/agent-permissions-approval.md) |
| `b19` | A local cache tier, keyed on the ref | [agent-design/local.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/local.md) |
| `b20` | Finishing the job versus staying in scope (Claude Code 2.1.307) | [coding-agent-approaches.md](https://github.com/jburnhams/prompts/blob/a531474/coding-agent-approaches.md) |
| `b21` | OpenCode's automations: one client, read as code | [mcp-events.md](https://github.com/jburnhams/prompts/blob/a531474/mcp-events.md) |
| `b22` | Loop and anomaly detection, in the run and after it | [telemetry/analysis-and-alerts.md](https://github.com/jburnhams/prompts/blob/a531474/telemetry/analysis-and-alerts.md) |
| `b23` | Claude Code's REPL and Pi's codemode (read 2026-11-09) | [code-mode/README.md](https://github.com/jburnhams/prompts/blob/a531474/code-mode/README.md) |
| `b24` | Design as a separate artefact, produced before the pixels | [agent-generative-output.md](https://github.com/jburnhams/prompts/blob/a531474/agent-generative-output.md) |
| `b25` | Repository rules as a citation obligation, not a context blob | [code-review-approaches.md](https://github.com/jburnhams/prompts/blob/a531474/code-review-approaches.md) |
| `b26` | Five ways the field writes them | [agent-tool-implementations.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-implementations.md) |
| `b27` | How the harnesses compare | [agent-multi-model.md](https://github.com/jburnhams/prompts/blob/a531474/agent-multi-model.md) |
| `b28` | Choosing how the run ends: Complete, update Jira, open a PR, ask for help | [agent-design/keel/README.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/README.md) |
| `b29` | What the grader may conclude | [agent-run-steering.md](https://github.com/jburnhams/prompts/blob/a531474/agent-run-steering.md) |
| `b30` | Codex [source, 641e2e362c, `codex-rs/otel`] | [telemetry/harnesses-and-sdks.md](https://github.com/jburnhams/prompts/blob/a531474/telemetry/harnesses-and-sdks.md) |
| `b31` | Incremental/anchored summarization vs. from-scratch every time | [agent-context-compaction.md](https://github.com/jburnhams/prompts/blob/a531474/agent-context-compaction.md) |
| `b32` | Short waits inside a run: `Await` | [agent-design/medium.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/medium.md) |
| `b33` | The ref rule applies to writes, not only reads | [agent-design/generative.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/generative.md) |
| `b34` | Which revision? (and: from which repository?) | [agent-context-file-loading.md](https://github.com/jburnhams/prompts/blob/a531474/agent-context-file-loading.md) |
| `b35` | The constraint that decides the design | [agent-design/models.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/models.md) |
| `b36` | How Forge and Lens would use it | [agent-design/keel/memory.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/memory.md) |
| `b37` | Reasoning rides the same wire | [agent-tool-call-dialects.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-call-dialects.md) |
| `b38` | Codex: the surrounding plumbing | [agent-run-recovery.md](https://github.com/jburnhams/prompts/blob/a531474/agent-run-recovery.md) |
| `b39` | Async / background execution | [agent-tool-surfaces.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-surfaces.md) |
| `b40` | Who writes it: the working model, a background agent, or a human | [agent-memory-learning.md](https://github.com/jburnhams/prompts/blob/a531474/agent-memory-learning.md) |
| `b41` | Meaning: which attribute dialect | [telemetry/catalogue.md](https://github.com/jburnhams/prompts/blob/a531474/telemetry/catalogue.md) |
| `b42` | The specialist wrapper (multi-stage sub-agent) | [agent-design/system-prompts.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/system-prompts.md) |
| `b43` | Events from MCP servers *(proposed 2026-11-23, weekly pass)* | [agent-design/keel/triggers-and-runs.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/triggers-and-runs.md) |
| `b44` | What the fan-out is actually buying | [agent-design/review.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/review.md) |
| `b45` | October 2026: orchestration moves into code | [agent-subagent-architectures.md](https://github.com/jburnhams/prompts/blob/a531474/agent-subagent-architectures.md) |
| `b46` | Who may answer, and what an answer approves (added 2026-10-19) | [agent-design/formats.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/formats.md) |
| `b47` | Interrupted attempts *(added 2026-10-26)* | [agent-design/keel/pipelines.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/pipelines.md) |
| `b48` | Checklist for a design | [agent-vision-multimodal.md](https://github.com/jburnhams/prompts/blob/a531474/agent-vision-multimodal.md) |
| `b49` | Who renders, and what a non-rendering host does | [agent-interactive-views.md](https://github.com/jburnhams/prompts/blob/a531474/agent-interactive-views.md) |
| `b50` | What the model is given | [agent-design/keel/taxonomy.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/taxonomy.md) |
| `b51` | What is deliberately *not* configurable | [agent-design/tools.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/tools.md) |
| `b52` | Schema expressiveness: the conditional-requirement blocks | [agent-design/adk.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/adk.md) |
| `b53` | Discovery (a specification for the service, not the harness) | [agent-design/context-files.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/context-files.md) |
| `b54` | When (and whether) the agent commits | [agent-git-vcs.md](https://github.com/jburnhams/prompts/blob/a531474/agent-git-vcs.md) |
| `b55` | Suite 1 — Tool hardening (the hostile workspace) | [agent-design/eval.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/eval.md) |
| `b56` | Continuations and pipeline edges | [agent-design/keel/outputs.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/outputs.md) |
| `b57` | MCP: trace context in `_meta` (SEP-414) | [telemetry/standards.md](https://github.com/jburnhams/prompts/blob/a531474/telemetry/standards.md) |
| `b58` | The null literal costs more than the delimiter | [agent-tabular-results.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tabular-results.md) |
| `b59` | Code Mode has converged from four directions | [agent-local-compute.md](https://github.com/jburnhams/prompts/blob/a531474/agent-local-compute.md) |
| `b60` | Grounding: schema, semantics, verified queries | [agent-data-analysis.md](https://github.com/jburnhams/prompts/blob/a531474/agent-data-analysis.md) |
| `r06` | Blocking monitors against an agent that is trying to get past them | [agent-permissions-approval.md](https://github.com/jburnhams/prompts/blob/a531474/agent-permissions-approval.md) |
| `r36` | How a run ends | [agent-design/keel/taxonomy.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/taxonomy.md) |
| `r48` | Deterministic, non-LLM completion gates | [agent-self-verification.md](https://github.com/jburnhams/prompts/blob/a531474/agent-self-verification.md) |
| `r58` | The digest gate: most runs should produce nothing | [agent-design/memory.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/memory.md) |

## Bare-facet test (12)

Used in step 5 only: classified with the facet names and one line per value, before any glossary entry.

| ID | Item (section heading) | From |
|---|---|---|
| `t01` | Arize Phoenix [source, a9ce4b0f4d] | [telemetry/platforms-and-storage.md](https://github.com/jburnhams/prompts/blob/a531474/telemetry/platforms-and-storage.md) |
| `t02` | Why the cache survives | [agent-deferred-tool-loading.md](https://github.com/jburnhams/prompts/blob/a531474/agent-deferred-tool-loading.md) |
| `t03` | Escalation after validation (orchestrator, deterministic rules) | [agent-design/risk.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/risk.md) |
| `t04` | An adjacent-but-different mechanism worth distinguishing | [agent-self-verification.md](https://github.com/jburnhams/prompts/blob/a531474/agent-self-verification.md) |
| `t05` | Detecting a collapse: `WarnOnCacheBusts` | [agent-prompt-cache-health.md](https://github.com/jburnhams/prompts/blob/a531474/agent-prompt-cache-health.md) |
| `t06` | Tools marked as endings | [agent-design/keel/endings.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/endings.md) |
| `t07` | Server requests and deferred results in a hands-off run *(added 2026-11-09)* | [agent-design/keel/tools-and-agents.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/tools-and-agents.md) |
| `t08` | A third entrypoint: `analyse` | [agent-design/data.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/data.md) |
| `t09` | Non-trivial results come back as refs | [agent-design/artifacts.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/artifacts.md) |
| `t10` | Answers bound to the asker: Goose and Crush | [agent-content-provenance.md](https://github.com/jburnhams/prompts/blob/a531474/agent-content-provenance.md) |
| `t11` | The `2026-07-28` rewrite, and why it matters here | [agent-tool-result-transport.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-result-transport.md) |
| `t12` | Claude Code's three separate generators — worth detailing on its own | [agent-turn-output.md](https://github.com/jburnhams/prompts/blob/a531474/agent-turn-output.md) |

## Round-1 test (60)

Fresh items for the round-1 agreement test (step 8). Nobody classifies them before the raters do.

| ID | Item (section heading) | From |
|---|---|---|
| `r01` | Why an agent with no human in the loop needs eyes | [agent-design/vision.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/vision.md) |
| `r02` | When it runs: at transitions, not continuously | [agent-design/orchestration.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/orchestration.md) |
| `r03` | Why archetype 2, not archetype 1, and what that changes | [agent-design/README.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/README.md) |
| `r04` | Three channels, and why they are three | [agent-design/memory.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/memory.md) |
| `r05` | Not an archetype: orchestration patterns/backends | [agent-archetypes.md](https://github.com/jburnhams/prompts/blob/a531474/agent-archetypes.md) |
| `r07` | Sliding expiry, on the `persist` tier only | [agent-design/local.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/local.md) |
| `r08` | Communication style & verbosity | [coding-agent-approaches.md](https://github.com/jburnhams/prompts/blob/a531474/coding-agent-approaches.md) |
| `r09` | What runs the program: interpreters and their bounds (read 2026-11-09) | [code-mode/README.md](https://github.com/jburnhams/prompts/blob/a531474/code-mode/README.md) |
| `r10` | Four delivery channels, and why the choice is the design | [agent-generative-output.md](https://github.com/jburnhams/prompts/blob/a531474/agent-generative-output.md) |
| `r11` | AWS X-Ray and CloudWatch GenAI Observability | [telemetry/platform-comparison.md](https://github.com/jburnhams/prompts/blob/a531474/telemetry/platform-comparison.md) |
| `r12` | The rest of the loop that isn't the loop | [code-review-approaches.md](https://github.com/jburnhams/prompts/blob/a531474/code-review-approaches.md) |
| `r13` | The bug class this family invites | [agent-tool-implementations.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-implementations.md) |
| `r14` | Pattern A: sub-agents with a model pin | [agent-multi-model.md](https://github.com/jburnhams/prompts/blob/a531474/agent-multi-model.md) |
| `r15` | Whether it blocks the run | [agent-run-steering.md](https://github.com/jburnhams/prompts/blob/a531474/agent-run-steering.md) |
| `r16` | Claude Agent SDK [source, 32e96114c1] | [telemetry/harnesses-and-sdks.md](https://github.com/jburnhams/prompts/blob/a531474/telemetry/harnesses-and-sdks.md) |
| `r17` | Two things Codex's token-budget mode does that no summariser can | [agent-context-compaction.md](https://github.com/jburnhams/prompts/blob/a531474/agent-context-compaction.md) |
| `r18` | Review → implement handoff (`<findings>` envelope tag) | [agent-design/medium.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/medium.md) |
| `r19` | Skills, if they ever arrive, execute rather than read | [agent-design/generative.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/generative.md) |
| `r20` | The null case: Aider | [agent-context-file-loading.md](https://github.com/jburnhams/prompts/blob/a531474/agent-context-file-loading.md) |
| `r21` | `Expand`: look further, keep going | [agent-design/models.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/models.md) |
| `r22` | Substrate and retrieval: files for curated memory, search for episodic | [agent-design/keel/memory.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/memory.md) |
| `r23` | What implementing one actually costs | [agent-tool-call-dialects.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-call-dialects.md) |
| `r24` | Claude Code: two reminders and a requeue tool | [agent-run-recovery.md](https://github.com/jburnhams/prompts/blob/a531474/agent-run-recovery.md) |
| `r25` | Search & code navigation | [agent-tool-surfaces.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-surfaces.md) |
| `r26` | Hermes Agent's memory (read from source) | [agent-memory-learning.md](https://github.com/jburnhams/prompts/blob/a531474/agent-memory-learning.md) |
| `r27` | Signal shapes used for the agent itself | [telemetry/catalogue.md](https://github.com/jburnhams/prompts/blob/a531474/telemetry/catalogue.md) |
| `r28` | Review-mode system prompts (two shapes) | [agent-design/system-prompts.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/system-prompts.md) |
| `r29` | Draft runs on a sandbox | [agent-design/keel/triggers-and-runs.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/triggers-and-runs.md) |
| `r30` | Secret scan before the model sees the diff (amends §2) | [agent-design/review.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/review.md) |
| `r31` | Claude Code's coordinator, worker and workflow prompts (v2.1.303) | [agent-subagent-architectures.md](https://github.com/jburnhams/prompts/blob/a531474/agent-subagent-architectures.md) |
| `r32` | Rules common to every tool result | [agent-design/formats.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/formats.md) |
| `r33` | Pipeline runs are the durable record | [agent-design/keel/pipelines.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/pipelines.md) |
| `r34` | Browser surfaces: three postures | [agent-vision-multimodal.md](https://github.com/jburnhams/prompts/blob/a531474/agent-vision-multimodal.md) |
| `r35` | A run behind a view | [agent-interactive-views.md](https://github.com/jburnhams/prompts/blob/a531474/agent-interactive-views.md) |
| `r37` | The result envelope — the largest single mismatch | [agent-design/adk.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/adk.md) |
| `r38` | Budget, and saying when it bit | [agent-design/context-files.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/context-files.md) |
| `r39` | A sandbox-writable `.git` is a channel out of the sandbox | [agent-git-vcs.md](https://github.com/jburnhams/prompts/blob/a531474/agent-git-vcs.md) |
| `r40` | Suite 2 — Edit correctness under collateral-damage checking | [agent-design/eval.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/eval.md) |
| `r41` | Outputs: tools, chaining, or something else? | [agent-design/keel/outputs.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/outputs.md) |
| `r42` | Trajectory and transcript formats | [telemetry/standards.md](https://github.com/jburnhams/prompts/blob/a531474/telemetry/standards.md) |
| `r43` | Sandboxes, under a blast-radius threat model | [agent-local-compute.md](https://github.com/jburnhams/prompts/blob/a531474/agent-local-compute.md) |
| `r44` | Braintrust [secondary, Braintrust blog] | [telemetry/platforms-and-storage.md](https://github.com/jburnhams/prompts/blob/a531474/telemetry/platforms-and-storage.md) |
| `r45` | Discovery, deferral, selection, authorisation, and skill-scoped tools (added 2026-11-11) | [agent-deferred-tool-loading.md](https://github.com/jburnhams/prompts/blob/a531474/agent-deferred-tool-loading.md) |
| `r46` | What a risk output should contain | [agent-risk-assessment.md](https://github.com/jburnhams/prompts/blob/a531474/agent-risk-assessment.md) |
| `r47` | How the tier is computed: a floor, then escalation only | [agent-design/risk.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/risk.md) |
| `r49` | Placing injected text so it does not move the prefix | [agent-prompt-cache-health.md](https://github.com/jburnhams/prompts/blob/a531474/agent-prompt-cache-health.md) |
| `r50` | Deferred with a reason, not adopted | [agent-design/data.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/data.md) |
| `r51` | Immutability is a property of the ref, and it is visible | [agent-design/artifacts.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/artifacts.md) |
| `r52` | Provenance is not trust | [agent-content-provenance.md](https://github.com/jburnhams/prompts/blob/a531474/agent-content-provenance.md) |
| `r53` | Cline — the whole envelope, stringified | [agent-tool-result-transport.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-result-transport.md) |
| `r54` | Redaction is sometimes the model provider's choice, not the scaffold's | [agent-turn-output.md](https://github.com/jburnhams/prompts/blob/a531474/agent-turn-output.md) |
| `r55` | Evidence, verification, and what is deferred | [agent-design/vision.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/vision.md) |
| `r56` | What roles this design has, and the invariant they share | [agent-design/orchestration.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/orchestration.md) |
| `r57` | Two entrypoints, one core | [agent-design/README.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/README.md) |
| `r59` | Minimalist / self-sufficient scaffold | [agent-archetypes.md](https://github.com/jburnhams/prompts/blob/a531474/agent-archetypes.md) |
| `r60` | The capability paragraph is computed from the tool set | [agent-design/cloudflare.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/cloudflare.md) |
| `h01` | Sandbox and isolation as a complementary layer | [agent-permissions-approval.md](https://github.com/jburnhams/prompts/blob/a531474/agent-permissions-approval.md) |
| `h02` | A table's expiry error carries its shape | [agent-design/local.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/local.md) |
| `h03` | Identity & self-referential framing | [coding-agent-approaches.md](https://github.com/jburnhams/prompts/blob/a531474/coding-agent-approaches.md) |
| `h04` | The honesty rules that come with charting | [agent-generative-output.md](https://github.com/jburnhams/prompts/blob/a531474/agent-generative-output.md) |

## Held for round 2 (56)

Not looked at. Round 2 draws from here.

| ID | Item (section heading) | From |
|---|---|---|
| `h05` | `/steward`: one pass per wake-up | [code-review-approaches.md](https://github.com/jburnhams/prompts/blob/a531474/code-review-approaches.md) |
| `h06` | Four kinds of side channel | [agent-tool-implementations.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-implementations.md) |
| `h07` | Pattern D: routers and "auto" | [agent-multi-model.md](https://github.com/jburnhams/prompts/blob/a531474/agent-multi-model.md) |
| `h08` | A plan → implement pipeline, triggered by Jira, updating Jira at the end | [agent-design/keel/README.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/README.md) |
| `h09` | How a forged steer is told apart from a real one | [agent-run-steering.md](https://github.com/jburnhams/prompts/blob/a531474/agent-run-steering.md) |
| `h10` | Gemini CLI [source, 4ed06ed0dd; docs/cli/telemetry.md] | [telemetry/harnesses-and-sdks.md](https://github.com/jburnhams/prompts/blob/a531474/telemetry/harnesses-and-sdks.md) |
| `h11` | A summariser prompt the model refused, and summaries on an append-only thread (read 2026-11-09) | [agent-context-compaction.md](https://github.com/jburnhams/prompts/blob/a531474/agent-context-compaction.md) |
| `h12` | What a PR watch adds to 1a–1d *(proposed 2026-11-23, weekly pass)* | [agent-design/medium.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/medium.md) |
| `h13` | A closed refusal vocabulary on every validating write path | [agent-design/generative.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/generative.md) |
| `h14` | MCP instructions, and the cache problem that shaped them | [agent-context-file-loading.md](https://github.com/jburnhams/prompts/blob/a531474/agent-context-file-loading.md) |
| `h15` | `HandOff`: pass it on | [agent-design/models.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/models.md) |
| `h16` | Notes, memory and consolidation are three things | [agent-design/keel/memory.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/memory.md) |
| `h17` | Argument encoding is where reliability is won or lost | [agent-tool-call-dialects.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-call-dialects.md) |
| `h18` | The model's own response failed (read 2026-11-16) | [agent-run-recovery.md](https://github.com/jburnhams/prompts/blob/a531474/agent-run-recovery.md) |
| `h19` | Browser & web access | [agent-tool-surfaces.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-surfaces.md) |
| `h20` | Retrospectives: outcome triage and failure-to-prevention | [agent-memory-learning.md](https://github.com/jburnhams/prompts/blob/a531474/agent-memory-learning.md) |
| `h21` | Analysis prompts: the quick run and its landings | [agent-design/system-prompts.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/system-prompts.md) |
| `h22` | The validator brief — exact payload | [agent-design/review.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/review.md) |
| `h23` | October 2026: fewer sub-agents, or a thousand | [agent-subagent-architectures.md](https://github.com/jburnhams/prompts/blob/a531474/agent-subagent-architectures.md) |
| `h24` | Plan → implement handoff | [agent-design/formats.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/formats.md) |
| `h25` | Four entry points — and the fifth nobody built | [agent-vision-multimodal.md](https://github.com/jburnhams/prompts/blob/a531474/agent-vision-multimodal.md) |
| `h26` | How long a view lives | [agent-interactive-views.md](https://github.com/jburnhams/prompts/blob/a531474/agent-interactive-views.md) |
| `h27` | What a run leads to | [agent-design/keel/taxonomy.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/taxonomy.md) |
| `h28` | Retries make non-idempotent tools dangerous | [agent-design/adk.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/adk.md) |
| `h29` | Just-in-time loading for deeper files | [agent-design/context-files.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/context-files.md) |
| `h30` | Checkpoint and undo systems | [agent-git-vcs.md](https://github.com/jburnhams/prompts/blob/a531474/agent-git-vcs.md) |
| `h31` | Why this is not optional, and why public benchmarks don't substitute | [agent-design/eval.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/eval.md) |
| `h32` | Where a PR gets opened | [agent-design/keel/outputs.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/outputs.md) |
| `h33` | Content: off by default, three patterns | [telemetry/standards.md](https://github.com/jburnhams/prompts/blob/a531474/telemetry/standards.md) |
| `h34` | Measurement two — accuracy, and what it could not show | [agent-tabular-results.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tabular-results.md) |
| `h35` | The three-way split this pass is about | [agent-local-compute.md](https://github.com/jburnhams/prompts/blob/a531474/agent-local-compute.md) |
| `h36` | Who draws the chart | [agent-data-analysis.md](https://github.com/jburnhams/prompts/blob/a531474/agent-data-analysis.md) |
| `h37` | Predicting change risk from history: Meta's DRS and RADAR | [agent-risk-assessment.md](https://github.com/jburnhams/prompts/blob/a531474/agent-risk-assessment.md) |
| `h38` | Review-as-a-general-tool — the conflation trap | [agent-self-verification.md](https://github.com/jburnhams/prompts/blob/a531474/agent-self-verification.md) |
| `h39` | The completion gate gets a provenance half | [agent-design/data.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/data.md) |
| `h40` | 4 The operation set | [agent-design/artifacts.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/artifacts.md) |
| `h41` | A magic keyword to boost reasoning budget — one source, worth flagging for a meta-reason | [agent-turn-output.md](https://github.com/jburnhams/prompts/blob/a531474/agent-turn-output.md) |
| `h42` | Why these three and not others | [agent-design/vision.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/vision.md) |
| `h43` | Where the ledger lives | [agent-design/orchestration.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/orchestration.md) |
| `h44` | 4b-i. Claim strength: the gate decides whether, the wording decides how far | [agent-design/memory.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/memory.md) |
| `h45` | `Edit` gains a whitespace-normalised retry, and it flags itself | [agent-design/cloudflare.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/cloudflare.md) |
| `h46` | Hand-off: the outcome where permission is not available | [agent-permissions-approval.md](https://github.com/jburnhams/prompts/blob/a531474/agent-permissions-approval.md) |
| `h47` | Focused tools, with Code Mode named as the escape hatch | [agent-design/local.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/local.md) |
| `h48` | Environment & context injection | [coding-agent-approaches.md](https://github.com/jburnhams/prompts/blob/a531474/coding-agent-approaches.md) |
| `h49` | Why it is a category and not a footnote | [code-mode/README.md](https://github.com/jburnhams/prompts/blob/a531474/code-mode/README.md) |
| `h50` | Taste as a computable gate | [agent-generative-output.md](https://github.com/jburnhams/prompts/blob/a531474/agent-generative-output.md) |
| `h51` | The five decisions worth stealing | [code-review-approaches.md](https://github.com/jburnhams/prompts/blob/a531474/code-review-approaches.md) |
| `h52` | Memory scoped to a sub-agent, not just to a project | [agent-tool-implementations.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-implementations.md) |
| `h53` | Pattern B: two stages | [agent-multi-model.md](https://github.com/jburnhams/prompts/blob/a531474/agent-multi-model.md) |
| `h54` | The concept list, checked | [agent-design/keel/README.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/README.md) |
| `h55` | How long the text lasts | [agent-run-steering.md](https://github.com/jburnhams/prompts/blob/a531474/agent-run-steering.md) |
| `h56` | Claude Code [docs: code.claude.com/docs/en/monitoring-usage] | [telemetry/harnesses-and-sdks.md](https://github.com/jburnhams/prompts/blob/a531474/telemetry/harnesses-and-sdks.md) |
| `h57` | Claude Code at v2.1.303: four summariser prompts, and the user's words as a record | [agent-context-compaction.md](https://github.com/jburnhams/prompts/blob/a531474/agent-context-compaction.md) |
| `h58` | CI-failure fix runs (`source: ci_failure`) | [agent-design/medium.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/medium.md) |
| `h59` | What this document does not change | [agent-design/generative.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/generative.md) |
| `h60` | Skills: a catalog in the prompt, a body on demand | [agent-context-file-loading.md](https://github.com/jburnhams/prompts/blob/a531474/agent-context-file-loading.md) |

## Round-3 test (60)

Drawn 2026-11-26 after round 2 used up the held set: `sample.py` continues the same seeded order for 80 more (`g01`-`g80`); eight meta sections were dropped by hand (`g17`, `g19`, `g34`, `g36`, `g38`, `g47`, `g60`, `g78`) and the first 60 of the rest (`g01`-`g67`) are the round-3 items. `g68`-`g80` are held.

| ID | Item (section heading) | From |
|---|---|---|
| `g01` | How the quick agent is presented with them | [agent-design/models.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/models.md) |
| `g02` | Writing, validation and moderation | [agent-design/keel/memory.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/memory.md) |
| `g03` | Five ways to delimit a call, and the tokenizer decides which | [agent-tool-call-dialects.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-call-dialects.md) |
| `g04` | Goose: resume a delegate by id | [agent-run-recovery.md](https://github.com/jburnhams/prompts/blob/a531474/agent-run-recovery.md) |
| `g05` | Persistent memory & deployment as tools | [agent-tool-surfaces.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-surfaces.md) |
| `g06` | (b) A separate background agent reads finished transcripts | [agent-memory-learning.md](https://github.com/jburnhams/prompts/blob/a531474/agent-memory-learning.md) |
| `g07` | The `<prior_attempt>` paragraph (all landings) | [agent-design/system-prompts.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/system-prompts.md) |
| `g08` | Code changes in response to comments — the boundary | [agent-design/review.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/review.md) |
| `g09` | Turn/output bounding and the result-handling contract | [agent-subagent-architectures.md](https://github.com/jburnhams/prompts/blob/a531474/agent-subagent-architectures.md) |
| `g10` | Screenshots as verification evidence | [agent-vision-multimodal.md](https://github.com/jburnhams/prompts/blob/a531474/agent-vision-multimodal.md) |
| `g11` | What reaches the model, and as whose words | [agent-interactive-views.md](https://github.com/jburnhams/prompts/blob/a531474/agent-interactive-views.md) |
| `g12` | Where each harness-side rule actually lives | [agent-design/adk.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/adk.md) |
| `g13` | Kinds: one vocabulary, three resolutions | [agent-design/context-files.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/context-files.md) |
| `g14` | PR and push workflow | [agent-git-vcs.md](https://github.com/jburnhams/prompts/blob/a531474/agent-git-vcs.md) |
| `g15` | Suite 3 — Review mode | [agent-design/eval.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/eval.md) |
| `g16` | The dialects in practice | [telemetry/standards.md](https://github.com/jburnhams/prompts/blob/a531474/telemetry/standards.md) |
| `g18` | Pure JS vs WASM, and why the gap is architectural | [agent-local-compute.md](https://github.com/jburnhams/prompts/blob/a531474/agent-local-compute.md) |
| `g20` | LangSmith [source for the client, inference for the store] | [telemetry/platforms-and-storage.md](https://github.com/jburnhams/prompts/blob/a531474/telemetry/platforms-and-storage.md) |
| `g21` | Two granularities, one problem | [agent-risk-assessment.md](https://github.com/jburnhams/prompts/blob/a531474/agent-risk-assessment.md) |
| `g22` | Pipeline changes (multi- and single-stage alike) | [agent-design/risk.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/risk.md) |
| `g23` | Hook-based, user-configured verification gates | [agent-self-verification.md](https://github.com/jburnhams/prompts/blob/a531474/agent-self-verification.md) |
| `g24` | Promoted to `future.md` with a stated shape | [agent-design/data.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/data.md) |
| `g25` | MCP: central in the namespace, not in the block type | [agent-design/artifacts.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/artifacts.md) |
| `g26` | What it means for Forge | [agent-content-provenance.md](https://github.com/jburnhams/prompts/blob/a531474/agent-content-provenance.md) |
| `g27` | Roo Code — MCP-aware, and silently lossy | [agent-tool-result-transport.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-result-transport.md) |
| `g28` | A completed-reasoning-block micro-title — a second, smaller title-generation instance | [agent-turn-output.md](https://github.com/jburnhams/prompts/blob/a531474/agent-turn-output.md) |
| `g29` | Injection, and the one honest mitigation | [agent-design/vision.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/vision.md) |
| `g30` | Self-oversight inside a run | [agent-design/orchestration.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/orchestration.md) |
| `g31` | `blocker` suspends, and it reuses machinery that exists | [agent-design/memory.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/memory.md) |
| `g32` | Compaction needs a second budget, and a degradation says what it did not damage | [agent-design/cloudflare.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/cloudflare.md) |
| `g33` | Claude Code's auto-mode classifier, read from the shipped prompt | [agent-permissions-approval.md](https://github.com/jburnhams/prompts/blob/a531474/agent-permissions-approval.md) |
| `g35` | Per-model / per-provider prompt variants | [coding-agent-approaches.md](https://github.com/jburnhams/prompts/blob/a531474/coding-agent-approaches.md) |
| `g37` | The generated page is itself an injection surface | [agent-generative-output.md](https://github.com/jburnhams/prompts/blob/a531474/agent-generative-output.md) |
| `g39` | The repair catalogue, and why it must run *after* validation | [agent-tool-implementations.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-implementations.md) |
| `g40` | Pattern C: the advisor tool (cheap executor, strong consultant) | [agent-multi-model.md](https://github.com/jburnhams/prompts/blob/a531474/agent-multi-model.md) |
| `g41` | A saved tool group for Java agents, used against a repo | [agent-design/keel/README.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/keel/README.md) |
| `g42` | Who pays, and from which budget | [agent-run-steering.md](https://github.com/jburnhams/prompts/blob/a531474/agent-run-steering.md) |
| `g43` | One mechanism vs. a layered pipeline vs. a pluggable strategy | [agent-context-compaction.md](https://github.com/jburnhams/prompts/blob/a531474/agent-context-compaction.md) |
| `g44` | `SearchSource` / `ReadSource` (ref-pinned source beyond the working tree) | [agent-design/medium.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/medium.md) |
| `g45` | `AskUser` posts a decision record, not a prose question | [agent-design/generative.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/generative.md) |
| `g46` | Templating: there is none | [agent-context-file-loading.md](https://github.com/jburnhams/prompts/blob/a531474/agent-context-file-loading.md) |
| `g48` | How tools get advertised | [agent-tool-call-dialects.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-call-dialects.md) |
| `g49` | Stopped, not dead: a resource limit inside a live run | [agent-run-recovery.md](https://github.com/jburnhams/prompts/blob/a531474/agent-run-recovery.md) |
| `g50` | Code execution as a distinct capability from "the shell" | [agent-tool-surfaces.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tool-surfaces.md) |
| `g51` | OpenClaw's memory architecture (read from source) | [agent-memory-learning.md](https://github.com/jburnhams/prompts/blob/a531474/agent-memory-learning.md) |
| `g52` | General-purpose delegate prompt (coding mode) | [agent-design/system-prompts.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/system-prompts.md) |
| `g53` | Stable finding identity across sessions (amends §7) | [agent-design/review.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/review.md) |
| `g54` | Calling convention & protocol shape | [agent-subagent-architectures.md](https://github.com/jburnhams/prompts/blob/a531474/agent-subagent-architectures.md) |
| `g55` | Transport: getting the bytes to the model | [agent-vision-multimodal.md](https://github.com/jburnhams/prompts/blob/a531474/agent-vision-multimodal.md) |
| `g56` | Which tools a view may call | [agent-interactive-views.md](https://github.com/jburnhams/prompts/blob/a531474/agent-interactive-views.md) |
| `g57` | Advertising is not enforcement | [agent-design/adk.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/adk.md) |
| `g58` | Inlining, and when not to | [agent-design/context-files.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/context-files.md) |
| `g59` | Output: a ship/no-ship log | [agent-design/eval.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/eval.md) |
| `g61` | Measurement one — token cost | [agent-tabular-results.md](https://github.com/jburnhams/prompts/blob/a531474/agent-tabular-results.md) |
| `g62` | What breaks when you move compute into the tab | [agent-local-compute.md](https://github.com/jburnhams/prompts/blob/a531474/agent-local-compute.md) |
| `g63` | It already works, and jupyter-mcp is the proof | [agent-data-analysis.md](https://github.com/jburnhams/prompts/blob/a531474/agent-data-analysis.md) |
| `g64` | What the storage designs agree on [inference] | [telemetry/platforms-and-storage.md](https://github.com/jburnhams/prompts/blob/a531474/telemetry/platforms-and-storage.md) |
| `g65` | Hosted products: what is shown and what is hidden | [agent-risk-assessment.md](https://github.com/jburnhams/prompts/blob/a531474/agent-risk-assessment.md) |
| `g66` | The floor: path and kind rules (deterministic, harness) | [agent-design/risk.md](https://github.com/jburnhams/prompts/blob/a531474/agent-design/risk.md) |
| `g67` | Verification authority handed to the user, not the model | [agent-self-verification.md](https://github.com/jburnhams/prompts/blob/a531474/agent-self-verification.md) |

[den]: ../../sources/denton-2003-faceted-howto/denton-2003-faceted-howto.html
