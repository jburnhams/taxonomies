# Round 3: competency questions (T10) and heuristic review (T11)

**In one line**: every stage-1 competency question in [`../../scope.md`](../../scope.md) can be
answered from `facets.md` and `glossary.md`. The review found no unmarked synonym and no
missing facet, and it lists two things for stage 2.

Checked by Claude, 2026-11-26, against the files at commit `5d0ad9e`. These are the files
round 3 tested.

## T10: competency questions

| # | Question | Answered by |
|---|---|---|
| 1 | Which mechanisms run with no person deciding? | facet `decider`: every value except `person`. The `person` scope says that starting a run is not deciding it |
| 2 | Which checks are made by a second model rather than by fixed rules? | `decider` = `second-model` against `rule`. The scopes give the ignore test and the rule about harness-built prompts |
| 3 | Which area does a new finding belong to, and so which doc? | facet `area`, eight values, each with an example doc |
| 4 | Which act on each tool call, and which only once per run? | `moment` = `tool-call` against `setup` / `ending` |
| 5 | What does "agent" mean, and which words are used for the other senses? | `agent` (J14). The product sense is `harness` (alias "coding agent"); a role sense is `sub-agent` or `orchestrator` |
| 6 | Which act when something fails, and which at the end? | `moment` = `failure` against `ending` |
| 7 | Harness, SDK, model provider? | `harness`, `agent-sdk`, `model-provider`, each with a near miss against the others |
| 8 | Run, session, turn, transcript? | `run`, `session`, `turn` (a moment value), `transcript` |
| 9 | Sub-agent, worker, fork, delegated run? | `sub-agent`, with worker, delegate and child agent as aliases. A fork has no entry yet (see T11) |
| 10 | "Mode", "surface", "artifact"? | "mode": no entry, by design; `permission-mode` takes the approval sense (label choice 8). "Surface": `tool-surface`. "Artifact": an alias of `output` only, so it is **partly answered** (see T11) |
| 11 | Judge, monitor, classifier, grader, reviewer? | all are aliases of `second-model`, a role. `code-review` covers the review sense |
| 12 | Eval, benchmark, self-verification? | `eval`, `benchmark` (narrower than eval), `self-verification`, with near misses between them |
| 13 | MCP server, MCP App, skill, plugin, connector? | `mcp-server` (alias connector), `mcp-app`, `skill`, `plugin` |

Twelve questions are answered and one is partly answered. Question 10's "artifact" sense
is left for stage 2 (output area).

## T11: Z39.19 §11.2.2 review

- **Unmarked synonyms**: none found. Every word in the harvest's seven synonym sets is
  either a preferred label or an alias of exactly one entry, which the checker's T2 test
  confirms.
- **Missing facets**: none. Round 3 had no three-way split and no rater asked for a
  dimension that does not exist. In the `unsure` notes (14, 11 and 21) the rater was
  choosing between existing values, mostly for survey sections.
- **Out-of-date terms**: none. All terms were harvested at prompts `a531474` (2026-11-26).
- **Term form**: consistent. T3 flags only `operations`, a mass noun that is kept.
- **Definitions and scope notes**: all pass T4. Five decider splits remain between the
  non-Claude pair (`g01`, `g05`, `g52`, `g10`, `g45`). They are recorded and not acted on,
  since the facet passes and a further change would need another round.
- **For stage 2**: (1) "fork" and "artifact" need entries in the coordination and output
  areas; (2) about a third of the `unsure` notes are on sections that survey several
  approaches, so a later stage could treat sources and surveys as a second kind of item
  (`scope.md`, "Stages").
