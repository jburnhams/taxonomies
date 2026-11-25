# 8. Pattern languages, and how they relate to taxonomy

**In one line**: a taxonomy names the *kinds of things* in a domain; a pattern language
names the *recurring good solutions* and links them so they combine. They come from the
same place (Alexander started by clustering design requirements, and argued that real
structure is a network, not a tree), and they need each other: patterns are written in
the domain's vocabulary, and a pattern collection is itself classified.

## The simple version

A taxonomy is the labels on the toy boxes. A pattern language is a book of good
games: each game has a short name ("musical chairs"), says when to play it and why it
works, and says which other games go well before or after it. To write the games
down clearly, you need the box labels; and once you have a lot of games, you need to
sort them too.

## What Alexander did

*A Pattern Language* (1977, [`alexander-1977`](./sources/alexander-1977-a-pattern-language/))
has 253 patterns, ordered from regions and towns down to construction details. Each
pattern "describes a problem which occurs over and over again in our environment, and
then describes the core of the solution to that problem, in such a way that you can use
this solution a million times over, without ever doing it the same way twice."

Every pattern has the same form:

1. A number and a **name** (a short noun phrase you can say aloud:
   LIGHT ON TWO SIDES OF EVERY ROOM).
2. **Asterisks** (none, one or two) for how confident the authors are that it is a
   true invariant.
3. A picture.
4. The **context**: which larger patterns it helps complete.
5. The **problem**, in bold, then the evidence.
6. "**Therefore:**" and the **solution**, in bold.
7. The smaller patterns that complete it.

It is a *language* because the names are a vocabulary and the links are a grammar: a
design is a sentence made from patterns. *The Timeless Way of Building* (1979,
[`alexander-1979`](./sources/alexander-1979-timeless-way/)) gives the theory: a shared
language lets ordinary people generate good places; when the language belongs only to
specialists, places get worse.

## Where it comes from: the same place as taxonomy

- *Notes on the Synthesis of Form* (1964,
  [`alexander-1964`](./sources/alexander-1964-synthesis-of-form/)) treats design as
  removing **misfits**: list the requirements, link the ones that interact, and
  decompose the graph into nearly independent clusters, each solved by a "diagram".
  That is a classification method (clustering requirements), and the diagrams became
  patterns.
- "A City is Not a Tree" (1965,
  [`alexander-1965`](./sources/alexander-1965-city-is-not-a-tree/)) argues that real
  structures are **semilattices** (overlapping sets), not trees, and that designers
  impose trees because "the mind has an overwhelming predisposition to see trees". This
  is the facet argument of [1](./01-structures.md), reached independently. A pattern
  language is a semilattice: a pattern can help complete several larger ones.

## How it reached software

Beck and Cunningham tried it on user interfaces in 1987; the "Gang of Four" book
(1994, [`gamma-1994`](./sources/gamma-1994-design-patterns/)) made 23 patterns standard
vocabulary (Factory, Observer, Adapter). Two things to note:

- GoF **classified** its patterns on two facets, **purpose** (creational, structural,
  behavioural) and **scope** (class, object). A pattern catalogue needs a taxonomy.
- Software patterns mostly kept the names and lost the *language*: the links that let
  patterns compose. Gabriel and Salingaros both make this point
  ([`gabriel-1996`](./sources/gabriel-1996-patterns-of-software/),
  [`salingaros-2000`](./sources/salingaros-2000-structure-of-pattern-languages/):
  a set of patterns is a language only if it is connected).

Pattern writing has its own patterns: mandatory elements (name, problem, context,
forces, solution) and naming advice such as an evocative noun-phrase name
([`meszaros-doble-1997`](./sources/meszaros-doble-1997-pattern-writing/), not read
this pass). UI design has pattern languages too
([`tidwell-designing-interfaces`](./sources/tidwell-designing-interfaces/)), which is
the bridge to the UX research repo.

## Taxonomy vs pattern language

| | Taxonomy / vocabulary | Pattern language |
|---|---|---|
| Names | kinds of things, properties, roles, processes | recurring problem-solution pairs |
| Question answered | "what is this?" | "what should I do here, and why?" |
| Unit | a term with a definition | a pattern with context, forces, solution |
| Structure | facets, hierarchy, related links | a network from large to small |
| Truth claim | "this is how we divide the domain" | "this solution works; confidence: \*\*" |
| Fails by | wrong boxes, synonyms, catch-alls | vague names, unlinked catalogue, dogma |

How they fit together:

1. **Patterns are written in the vocabulary.** A pattern's context and problem use the
   domain's terms; if "agent", "tool" and "skill" are loose, every pattern that uses
   them is loose.
2. **A pattern's name is a term** and follows the naming rules
   ([3](./03-naming.md)), with the extra wish that it be evocative and sayable.
3. **A pattern collection is classified** by facets (GoF's purpose x scope;
   Alexander's scale), which come from the vocabulary.
4. **Both are languages for a community** (Alexander's shared language, Evans's
   ubiquitous language). The point is shared use, not correctness.
5. **Confidence marks** (Alexander's asterisks) are worth copying into the vocabulary:
   mark how settled each term is.

## For Jonathan's domains

Both repos are already partly pattern languages. The prompts repo's agent-design
proposals and the ux-research tell registry and rules are collections of named
problem-solution pairs. The design in [`design/`](./design/README.md) therefore has two
layers: a **vocabulary** (the taxonomy, agreed first) and an optional **pattern layer**
on top, written in Alexander's form and using only vocabulary terms.

Back to the start: [`eli5.md`](./eli5.md). The design: [`design/`](./design/README.md).
