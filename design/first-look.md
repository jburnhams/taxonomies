# First look: what applying this to the two repos would start from

Not the application (that comes after the design is agreed). These are observations
from a quick read on 2026-11-25, to show the method has something to bite on.

## prompts (agent design)

**Synonyms already in use** (case-insensitive counts across `*.md`, 2026-11-25):

| Concept (guessed) | Forms found |
|---|---|
| a helper agent started by another | "sub-agent" 873, "subagent" 821, "sub agent" 2 |
| the code around the model | "harness" 1,770, "scaffold" 131 |
| the tools an agent has | "tool surface" 170, "tool set" 67, "toolset" 49 |
| the file an agent reads on start | "memory file" 60, "context file" 32 (and `CLAUDE.md`/`AGENTS.md` by name) |

Whether each row is one concept or several is exactly what Round 1 decides (N2, N3).
"Harness" and "scaffold" may be the same thing or a real distinction (the
`inside-the-scaffold` paper uses "scaffold" for the code architecture); the glossary
would say which.

**Facets already latent**: [`agent-archetypes.md`](https://github.com/jburnhams/prompts/blob/main/agent-archetypes.md)
explains its six archetypes with two axes, *deployment context* (human-in-the-loop vs
run-to-completion) and *scaffold richness* (minimal vs maximal). Those are two facets;
the archetypes are cells in their grid (a paradigm, in Kwasnik's terms), plus extra
features. It also has a "Not an archetype" section, which is a residual category doing
its proper job: showing where the scheme stops.

**Concept files as a facet**: the `agent-*.md` docs (memory, permissions, telemetry,
tool surfaces, ...) are a flat list of concerns. A facet such as "which part of an agent
is this about" would give them one principle of division.

**Proper names** (Keel, Forge, Lens) are names for specific designs, like species names
anchored to a type. They need no definition beyond their type (the design doc), but they
should be in the glossary so agents know they are names, not concepts.

## ux-research

**A taxonomy already exists**: [`ux-slop-taxonomy.md`](https://github.com/jburnhams/ux-research/blob/main/ux-slop-taxonomy.md)
catalogues tells "by layer" (colour and surface, typography, layout, components, motion,
copy, signatures and drift). Layer is one facet. Its §4, "The quality floor is a different
axis", already says a second facet exists. Detectability and severity are named as further
dimensions. So it is faceted in practice; the method would make the facets explicit and
test them with kappa.

**Pattern language candidates**: the rules in `ui-library/` and the dated tell registry
are problem-solution pairs. Written in the pattern form, with "wave" dates as the
history, they would be a UI pattern language linked to the glossary.

**Terms worth defining early**: "tell", "slop", "surface", "mood", "token", "Operate"
(as in the README's "Operate-surface rules"). "Surface" in particular is used in both
repos ("tool surface" in prompts, "surface" in ux-research), probably with different
meanings: a first entry for the context map.

## Suggested order

1. Agree the design (or its changes).
2. ux-research first: it already has a faceted catalogue, so it is a quick test of the method.
3. prompts second: bigger, more synonyms, more to gain.
4. Then the shared kernel and the map between them.
