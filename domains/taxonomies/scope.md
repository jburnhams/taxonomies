# Taxonomies taxonomy: scope

**In one line**: the vocabulary of the method itself (facet, rater, round, candidate,
warrant ...), written down as a taxonomy so the method's own words are agreed the way it
asks every other domain's to be.

**In plain words**: the spec and process use about fifty words with a special meaning:
a *facet* is a sorting question, a *round* is one test with fresh items, a *near miss* is
a note saying what a term is not. This domain gives each of them one entry, so anyone
reading the method, or a domain built with it, finds the word explained in one place.
It is also the first domain the explorer site shows, as a worked example of the files.

Built with the light version of [`design/process.md`](../../design/process.md#light-version-small-domains)
(version 1) and the file rules in [`design/spec.md`](../../design/spec.md). It is a
**draft**: steps 0, 1, 4 and 6 are done; there is no sample, harvest or round yet.

- **Context**: this repository's method: [`design/spec.md`](../../design/spec.md),
  [`design/process.md`](../../design/process.md), [`design/decisions.md`](../../design/decisions.md),
  and the files each domain folder holds. Short context name: `taxonomies`.
- **Purpose**: to name the method's concepts once, so that the spec, the process, every
  domain's files and the explorer site use the same words for them, and to sort each
  concept by what sort of thing it is and when in the method it comes up.
- **Readers**, in priority order: Jonathan first; then the agents that build and check
  domains with the method. Where they conflict, Jonathan's reading wins.
- **Owner**: Jonathan. Agents approve changes that pass T1-T6 with a logged reason; he
  can veto any change ([spec G1](../../design/spec.md#9-governance-how-a-taxonomy-changes)).
- **Status**: `draft`, 2026-11-26. Every term is `candidate`. Proposed, not adopted:
  whether the method's own words become a domain is Jonathan's decision.

## Competency questions

1. What does a domain folder hold, and what is each file for?
2. What is the difference between a term, a label and an identifier?
3. What is a facet, and how does a facet value differ from an alias?
4. What decides which word becomes the preferred label?
5. What is a round, who takes part, and what does it produce?
6. What does kappa measure, and what is the target?
7. Which changes may an agent make, and which only the owner?
8. When is a taxonomy adopted?
9. What is a near miss, and how does it differ from a scope note?
10. Which concepts belong to framing, building, testing and governing?

## Out of scope

The research vocabulary of the topic docs (prototype, basic level, family resemblance,
ontology as a field): those are words *about* classification, cited from sources, not
words the method uses to run. They can come in later through a shared kernel if a
domain needs them.

## Neighbours

Every other domain uses this vocabulary in its own files (`scope.md`, `facets.md`,
`glossary.md`). No `map.md` yet: no other domain defines these words.

## Ending conditions

As the light version: T1-T7, T10 and T11 pass. With under 30 spare concepts, a kappa
test (T8) would be indicative only.

## Next steps

1. Step 2: hold back a third of the method's concepts (for example those in
   `design/method-v1.1.md` and `design/source-check-2026-11-25.md`) as a test sample.
2. Step 3: a harvest over `design/` and the domain folders. The Warrant fields below
   were counted for this draft; a harvest would also find synonyms and homonyms.
3. A round: two model families sort the held-back concepts by `kind` and `stage`.
