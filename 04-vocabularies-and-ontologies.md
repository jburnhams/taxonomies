# 4. Controlled vocabularies, thesauri and ontologies

**In one line**: these are the standard, tested formats for writing a taxonomy down:
each concept gets one preferred name, its other names, a definition, and links to
broader, narrower and related concepts. An ontology adds rules a machine can reason
with; most of what we need stops before that.

## The simple version

A **controlled vocabulary** is the agreed list of box labels. A **thesaurus** adds
arrows: "fire engine, see also: ambulance", "fire engine is a kind of truck", and
"people also say fire truck: use fire engine". An **ontology** writes the same thing so
precisely that a computer can check it and draw conclusions ("every fire engine is a
vehicle, so it has wheels").

## The ladder of structure

NISO Z39.19 ([`niso-z39-19`](./sources/niso-z39-19-2005/)) names four rungs:

1. **List**: agreed terms.
2. **Synonym ring**: groups of terms treated as the same for search.
3. **Taxonomy**: terms in a hierarchy.
4. **Thesaurus**: terms with three relationships:
   - **Equivalence**: USE / UF ("use for"). The preferred term and its aliases.
   - **Hierarchy**: BT / NT (broader / narrower), of three kinds: *generic* (is-a),
     *whole-part*, *instance*.
   - **Association**: RT (related).

Plus **scope notes** saying what a term covers and does not. ISO 25964 is the
international version, with a data model and rules for mapping between vocabularies
([`iso-25964`](./sources/iso-25964/)).

## SKOS: the field list we will use

The W3C's SKOS ([`skos-2009`](./sources/skos-2009/)) turns the thesaurus into a small
data model. It is the right level of formality for us:

| SKOS | Meaning | Rule |
|---|---|---|
| `Concept` | a unit of thought, separate from its labels | |
| `prefLabel` | the preferred name | at most one per language |
| `altLabel` | other names people use | disjoint from prefLabel |
| `hiddenLabel` | misspellings, old names, for search only | disjoint from both |
| `definition`, `scopeNote`, `example` | what it means, where it stops, a case | |
| `historyNote`, `changeNote` | what changed and when | |
| `broader` / `narrower` | direct parent / child | **not** transitive; two parents allowed |
| `related` | associated, not hierarchical | cannot also be an ancestor |
| `ConceptScheme` | one vocabulary | |
| `exactMatch`, `closeMatch`, `broadMatch`, `narrowMatch`, `relatedMatch` | links to concepts in **other** schemes | |

The split between `Concept` and its labels is Ranganathan's idea plane vs verbal plane
again ([1](./01-structures.md)): the concept has a stable identity, the labels can
change. The mapping properties are how separate domain vocabularies point at each
other without merging ([6](./06-shared-language-in-software.md)).

## Ontologies: what they add

Gruber's definition: "an explicit specification of a conceptualization"
([`gruber-1993`](./sources/gruber-1993-ontology-definition/)). An ontology adds typed
relations, properties and axioms (for example in OWL) that a reasoner can check.

Useful ideas from ontology practice, even without the machinery:

- **Competency questions** (Noy and McGuinness,
  [`noy-mcguinness-2001`](./sources/noy-mcguinness-2001-ontology-101/)): write down the
  questions the vocabulary must let you answer. They set the scope and are the "litmus
  test" for whether it is done. Their first rule: "There is no one correct way to model
  a domain."
- **When to make a new class**: when there is something true of the subclass that is
  not true of the parent; otherwise it is a property value. Two to a dozen children per
  parent is typical; one child suggests a mistake.
- **OntoClean's rigidity test** ([`guarino-welty-ontoclean`](./sources/guarino-welty-ontoclean/)):
  a *rigid* property holds of a thing for as long as it exists (Person); an
  *anti-rigid* one can be gained or lost (Student). An anti-rigid concept cannot be the
  parent of a rigid one: Student cannot subsume Person. For us: **roles cannot be
  parents of kinds**. "Reviewer" is a role an agent plays; "agent" is a kind. A
  hierarchy that puts "agent" under "reviewer" is wrong.
- **Things vs happenings**: Basic Formal Ontology's top split into *continuants*
  (objects, qualities, roles) and *occurrents* (processes, events)
  ([`arp-smith-spear-2015`](./sources/arp-smith-spear-2015-bfo/)). A quick first check
  on any term: is it a thing, a property, a role, or something that happens? Mixing
  them in one facet is the most common error.
- **Definitions in genus-differentia form** and **naming conventions**
  ([3](./03-naming.md)).

## Why not a full ontology

A full OWL ontology needs tools (Protégé), a modelling discipline, and upkeep. Its pay-off
is machine reasoning. Our consumers are Jonathan and LLM agents reading markdown, so the
gain is small. SKOS-level structure in markdown, with the OntoClean and continuant
checks applied by hand, gets most of the benefit. If a domain later needs reasoning,
SKOS converts to RDF directly.

Next: [5. Building and testing a taxonomy](./05-building-and-testing.md).
