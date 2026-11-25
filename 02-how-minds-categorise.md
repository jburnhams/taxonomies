# 2. How minds categorise

**In one line**: people do not sort things by strict definitions. Categories have
good and bad examples, fuzzy edges, and one "natural" level of detail. A taxonomy
that ignores this is correct on paper and awkward in use.

## The simple version

Ask someone to name a bird and they say "robin", not "penguin", though both are birds.
Show them a picture of a kitchen chair and they say "chair", not "furniture" and not
"kitchen chair". Two things are happening. Categories have **best examples**
(prototypes), and there is a **just-right level** of detail (the basic level) that
people reach for first. Good names live at that level and good definitions come with a
best example.

## The classical view, and what broke it

The classical view (from Aristotle): a category is defined by necessary and
sufficient conditions; a thing is in or out. Most of logic, ontology engineering and
database design still assume it.

Three lines of work broke it as a description of how people think:

- **Family resemblance** (Wittgenstein, 1953,
  [`wittgenstein-1953`](./sources/wittgenstein-1953-family-resemblance/)): games share
  "a complicated network of similarities overlapping and criss-crossing", not one
  common feature.
- **Prototypes and the basic level** (Rosch, 1970s,
  [`rosch-1978`](./sources/rosch-1978-principles-of-categorization/),
  [`rosch-1976`](./sources/rosch-1976-basic-objects/)).
- **Radial categories and idealised cognitive models** (Lakoff, 1987,
  [`lakoff-1987`](./sources/lakoff-1987-women-fire-dangerous-things/)).

## Rosch: why some levels feel right

Two principles (Rosch 1978, p.2):

- **Cognitive economy**: "the task of category systems is to provide maximum
  information with the least cognitive effort."
- **Perceived world structure**: the world comes "as structured information rather than
  as arbitrary or unpredictable attributes" (features cluster: things with feathers
  tend to have wings).

A taxonomy has a **vertical** dimension (collie, dog, mammal, animal) and a
**horizontal** one (dog vs cat vs car at one level). The **basic level** is "the most
inclusive (abstract) level at which the categories can mirror the structure of
attributes perceived in the world". Above it (furniture) members share few features;
below it (kitchen chair) you add little. Evidence converges on the basic level from
many directions: it has the most listed attributes per unit of generality, its members
share motor movements (you sit on any chair the same way) and shapes, it is recognised
fastest, children learn it first, and adults name pictures with it.

The basic level moves with expertise: the 1976 study found students' basic level for
trees sat above the folk "generic" (tree, not oak), and experts name at finer levels.
So the right level depends on **who the names are for**.

**Prototypes** are "the clearest cases of" membership, measured by people's
goodness-of-example ratings. Rosch warned against over-reading this: the idea "has
tended to become reified as though it meant a specific category member or mental
structure", and "prototypes themselves do not constitute any particular model of
processes, representations, or learning" (p.15). They are a fact about judgments, not a
recipe for definitions.

## Lakoff: categories hang together by stories

Lakoff's title comes from the Dyirbal noun class *balan*, which includes women, fire
and dangerous things, linked by chains of association, not a shared feature.
**Radial categories** have a central case and extensions (mother: birth mother,
adoptive mother, stepmother), each linked by a different principle. **Idealised
cognitive models** are the background a category assumes: "bachelor" presumes a world
of marriageable adults, which is why the Pope is a poor example of one.

For a vocabulary, this means a term can be clear at its centre and contested at its
edges, and the edges are where to spend writing effort.

## Murphy: the three theories after the classical one

[`murphy-2002`](./sources/murphy-2002-big-book-of-concepts/) surveys them fairly:
**prototype** (a weighted summary of typical features), **exemplar** (the remembered
examples), **knowledge** (categories embedded in what we know about causes and
purposes). Each explains part of the data. Practical reading: store a definition **and**
examples **and** the purpose.

## Folk taxonomies: how deep people go

Across many cultures, folk biological classifications are shallow (rarely more than
five or six ranks), and the **generic** rank (oak, robin) is the busiest and best named,
with simple words; finer ranks get compound names (white oak)
([`berlin-1992`](./sources/berlin-1992-ethnobiological-classification/)).

## Essentialism: why renaming hurts

People act as if a category has a hidden essence that makes things what they are
([`medin-ortony-1989`](./sources/medin-ortony-1989-psychological-essentialism/)).
That is why a rename can feel like an attack on what something *is*, and why people
hunt for the one "true" taxonomy. Naming arguments get hot for this reason.

## What this means for our design

- Name at the **basic level for the intended readers** (Jonathan, and the agents that
  read the repos), not at the most abstract or most technical level.
- Every term gets a **definition** (for checking) and a **type example** (the
  prototype) and, where useful, a **near miss** (a thing that looks like it but is not).
- Keep it **shallow**: one busy level with short names; finer distinctions as compound
  names or as facet values.
- Write the edges down: where does the term stop applying?

Next: [3. Naming](./03-naming.md).
