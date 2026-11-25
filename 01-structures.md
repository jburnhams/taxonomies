# 1. The shapes a classification can take

**In one line**: a taxonomy does not have to be one big tree. Lists, trees, grids, facets
and networks are all classifications, and each one claims a different amount of
knowledge about the thing being sorted. Pick the shape your knowledge can support.

## The simple version

Sorting toys into boxes is a **list** of boxes. Putting boxes inside bigger boxes
("cars" inside "vehicles" inside "toys") is a **tree**. But a red toy fire engine
belongs with "vehicles" *and* with "red things" *and* with "things that make noise".
A tree makes you choose one box. **Facets** let you describe the toy on several
independent questions instead (What kind? What colour? Does it make noise?) and
find it by any of them. That one idea, from an Indian librarian in the 1930s, is the
biggest single lesson of this whole field.

## The forms, simplest first

Patrick Lambe's list of forms ([`lambe-2007`](./sources/lambe-2007-organising-knowledge/))
and Barbara Kwasnik's analysis of what each demands
([`kwasnik-1999`](./sources/kwasnik-1999-classification-structures/)):

| Form | What it is | Demands | Breaks when |
|---|---|---|---|
| **List** | flat set of names | agreement on the names | there are too many to scan |
| **Tree / hierarchy** | each thing in one place; is-a or part-of down the levels | one principle of division at each level, and enough theory to apply it | a thing belongs in two places; the principle changes |
| **Polyhierarchy** | a thing can have two parents | rules for when that is allowed | it turns into a tangle |
| **Paradigm / matrix** | two facets crossed in a grid | two independent dimensions | you need a third; but its **empty cells** point at things not yet named |
| **Facets** | several independent dimensions, each with its own short list | the facets to be truly independent | facets leak into each other; nobody can see the whole |
| **Network / system map** | things linked by typed relations | the relation types | it is not a classification any more, just a graph |

Kwasnik's point: each form encodes a different amount of **theory**. A strict
hierarchy says "we understand this domain well enough to divide it cleanly at every
level". Facets say less: "here are some independent questions you can ask of any
item". When a domain is young (agent design is), facets are the honest choice.

## Facets in detail

Ranganathan ([`ranganathan-prolegomena`](./sources/ranganathan-prolegomena/)) split a
subject into independent facets, each with its own list of values (foci), and built
compound subjects by combining values in a fixed **citation order**. His five
fundamental categories, **PMEST** (Personality, Matter, Energy, Space, Time), were
meant to apply to any subject. The British Classification Research Group made it
practical; Vickery's list of 13 categories (substance, organ, constituent, structure,
shape, property, object of action, action, operation, process, agent, space, time) is
a good checklist for finding the facets of a new domain
([`vickery-1960`](./sources/vickery-1960-faceted-classification/)).

Ranganathan's **three planes** separate three jobs that people usually mash together:

1. **Idea plane**: what the categories are.
2. **Verbal plane**: what words we use for them.
3. **Notational plane**: what codes or IDs we give them.

Agreeing on the idea plane first, then the words, then the IDs, avoids most naming
arguments: half of them are really arguments about what the category is.

Tests for a good facet, from Spiteri's simplification
([`spiteri-1998`](./sources/spiteri-1998-facet-model/)): it **differentiates**
(splits things into at least two groups), is **relevant** to the purpose, is
**ascertainable** (you can tell which value applies), is **permanent** (does not change
while the thing exists), is **homogeneous** (one characteristic of division only), and
its values are **mutually exclusive**.

Information systems research arrived at the same structure under another name:
Nickerson et al. define a taxonomy as a set of **dimensions**, each with
**characteristics** that are mutually exclusive and collectively exhaustive, so every
object has exactly one characteristic per dimension
([`nickerson-2013`](./sources/nickerson-2013-taxonomy-method/)). That is a faceted
classification.

## Why trees keep winning anyway, and why they shouldn't

Christopher Alexander made the same argument for cities in 1965
([`alexander-1965`](./sources/alexander-1965-city-is-not-a-tree/)). In a **tree**,
any two sets are either nested or disjoint. In a **semilattice**, sets can overlap, and
the overlap is itself a unit. Real cities are semilattices (the newsrack at a corner is
part of the drugstore and part of the crowd waiting at the traffic light); planned
cities are trees, because "the mind has an overwhelming predisposition to see trees
wherever it looks". On 20 elements a tree can hold at most 19 further subsets; a
semilattice can hold over a million. But he adds: "overlap alone does not give
structure. It can also give chaos."

So: use facets and allowed cross-links to keep the real overlaps, and rules to stop
the chaos.

## Typology vs taxonomy: two ways to build one

Kenneth Bailey ([`bailey-1994`](./sources/bailey-1994-typologies-taxonomies/))
separates a **typology** (built from concepts: choose dimensions, cross them) from a
**taxonomy** in the narrow sense (built from cases: group what you observe). Biology
fought this out as cladistics (a principle first: group by common descent,
[`hennig-1966`](./sources/hennig-1966-phylogenetic-systematics/)) versus phenetics
(measure overall similarity and cluster,
[`sokal-sneath-1963`](./sources/sokal-sneath-1963-numerical-taxonomy/)). The modern
methods alternate the two ([05](./05-building-and-testing.md)).

## What this means for our design

- Default to **facets**: a few independent questions, each with a short closed list.
- Allow a **tree inside a facet** only where is-a holds strictly.
- Separate idea, word and ID (Ranganathan's planes).
- Expect overlaps, and write rules for which ones are allowed.

Next: [2. How minds categorise](./02-how-minds-categorise.md).
