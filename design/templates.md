# Templates

*Superseded by [`spec.md`](./spec.md) §§2-7 (2026-11-25), which fixes the field names,
adds `Kind`, `Status` and `Warrant`, and replaces confidence with status. Kept for
history.*

Plain markdown, so people and agents read them without tools. Field names follow SKOS
([`skos-2009`](../sources/skos-2009/)) so a script could convert them to RDF later.

## `scope.md`

```markdown
# <Domain> taxonomy: scope

- **Context**: <repo or area this vocabulary governs>
- **Purpose** (meta-characteristic): <the one thing every facet must help with>
- **Readers**: <who uses these names: Jonathan, agents, end users>
- **Neighbouring contexts**: <other domains, and the map file>

## Competency questions
1. <a question the taxonomy must let you answer, e.g. "Which agents run unattended?">
2. ...

## Out of scope
- ...

## Ending conditions
- Kappa per facet >= 0.7 on a sample of <n> items
- No term added, merged or split in the last round
- <others>
```

## `facets.md`, one block per facet

```markdown
## <Facet name> (`<facet-id>`)

- **Question**: <the question this facet answers about an item>
- **Principle of division**: <the single characteristic used>
- **Kind of term**: thing | property | role | happening
- **Values**: `<term-id>` <Preferred label>, `<term-id>` <Preferred label>, ...
- **Unsorted**: <items currently waiting, with links>
- **Kappa**: <latest value, date, sample>
```

## `glossary.md`, one block per concept

```markdown
### <Preferred label> (`<term-id>`)

- **Definition**: A <preferred label> is a <genus> that <differentia>.
- **Scope**: Includes <...>. Excludes <...> (use `<other-id>`).
- **Aliases**: <alt label>, <alt label>  (hidden: <misspellings, old names>)
- **Type example**: <link to the clearest real case in the repo>
- **Near miss**: <link or description>, because <...>
- **Broader**: `<term-id>` · **Related**: `<term-id>`
- **Facet**: `<facet-id>`
- **Confidence**: settled | working | tentative
- **Matches**: exactMatch `<context>:<term-id>` (see map.md)
- **History**: 2026-11-25 added (<reason>)
```

Rules for the ID: lower-case, hyphenated, never reused, never changed even when the label is.

## `changelog.md`

Illustrative entries, not decisions:

```markdown
## 2026-11-25
- **rename** `sub-agent`: "Subagent" -> "Sub-agent" (873 vs 821 uses; hyphenated form kept
  as preferred, other as alias)
- **split** `tool-surface` into `tool-set` and `tool-schema` (round 2 hesitations on 6 items)
- **deprecate** `playbook` -> use `skill`
```

Operations: add, rename, split, merge, promote, demote, deprecate (from Kundisch et al.).

## A pattern

```markdown
# <NAME IN CAPITALS> (`<pattern-id>`) **

**Context**: serves <LARGER PATTERN>, <LARGER PATTERN>.

**Problem**: <one or two sentences, in bold in the original form>

<Forces and evidence, with links to sources and to examples in the repo.>

**Therefore**: <the solution, stated as an instruction>

**Smaller patterns**: <SMALLER PATTERN>, ...
**Facets**: <facet-id>: <value>, ...
```

The asterisks after the name are the confidence (none, one, two), as in Alexander.
