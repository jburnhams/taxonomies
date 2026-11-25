# Taxonomy from zero

Start here. Each level assumes only the one before it. Stop at any level; each ends with
where to go deeper.

---

## Level 0: like you're five

You have a big pile of toys. You put them into boxes and write a word on each box. That
is a **taxonomy**: a way of sorting things into groups, and names for the groups.

Three things always go wrong:

1. **Some toys fit two boxes.** The red fire engine is a vehicle *and* a red thing.
2. **People call things different names.** You say "fire engine", your friend says "fire
   truck", and now nobody can find it.
3. **New toys arrive** that don't fit any box.

Everything below is about those three problems.

---

## Level 1: the words people use

| Word | Means | Toy example |
|---|---|---|
| **classification** | sorting things into groups | putting toys in boxes |
| **taxonomy** | a classification of *kinds* of things, often in levels | toys > vehicles > fire engines |
| **nomenclature** | the rules for the *names* | "box labels are one word, lower case" |
| **controlled vocabulary** | the agreed list of names | the printed list of box labels |
| **synonym / alias** | another name for the same thing | "fire truck" for "fire engine" |
| **thesaurus** | vocabulary plus links: broader, narrower, related, "use X instead" | "fire engine: a kind of truck; see also ambulance" |
| **facet** | one independent question you can ask about anything | "What colour?" "Does it make noise?" |
| **ontology** | a vocabulary written precisely enough for a computer to reason with | "every vehicle has wheels; a fire engine is a vehicle" |
| **pattern language** | named good solutions to recurring problems, linked together | "musical chairs: when to play it, why it works, what to play next" |

---

## Level 2: the six big findings

This is the "science of naming things", boiled down. Each links to the topic doc that
goes deeper.

**1. People almost never pick the same name.** In experiments, two people chose the
same word for the same thing less than 20% of the time; two programmers named the same
variable the same way about 7% of the time. So names have to be **agreed and written
down**, and the other names people use kept as aliases.
→ [3. Naming](./03-naming.md)

**2. Minds sort by best examples, not definitions.** "Robin" is a better bird than
"penguin". People also have a just-right level of detail: they say "chair", not
"furniture" or "kitchen chair". So **name things at that level** and give every name a
**clear example** as well as a definition.
→ [2. How minds categorise](./02-how-minds-categorise.md)

**3. One tree rarely fits.** Real things overlap (the fire engine problem). The fix,
from libraries in the 1930s and independently from Christopher Alexander's "A City is
Not a Tree", is **facets**: several short independent lists instead of one deep tree.
→ [1. Structures](./01-structures.md)

**4. Keep the name separate from the sorting.** Biologists rename nothing when they
reshuffle the tree of life: each name is pinned to a **type specimen**, and the oldest
name wins. If you bake the sorting into the names, every reshuffle breaks every name.
→ [3. Naming](./03-naming.md), [4. Vocabularies](./04-vocabularies-and-ontologies.md)

**5. Words are local.** "Remote" means one thing at home and another at work. Software
design calls this **bounded contexts**: one agreed vocabulary per context, plus a small
map between contexts, instead of one vocabulary for everything.
→ [6. Shared language in software](./06-shared-language-in-software.md)

**6. There are tested ways to build one.** Write down what it is for, sort real
examples, test the boxes on new examples, repeat, and stop when two people sort a
fresh batch the same way.
→ [5. Building and testing](./05-building-and-testing.md)

---

## Level 3: is this a solved problem?

Half. The **method** is solved: librarians, biologists, ontology engineers, information
architects and software designers have converged on the same handful of practices. The
**content** is not and never will be: in 1668 John Wilkins tried to classify everything
in the universe and build a language from it, and it failed for the reasons above. Every
good taxonomy is good *for a purpose*, and you still have to agree it for each domain.
→ [7. Limits and politics](./07-limits-and-politics.md)

Alexander's *A Pattern Language* is a cousin: a taxonomy names the *things* in a domain;
a pattern language names the *good moves* and links them. You need the first to write the
second.
→ [8. Pattern languages](./08-pattern-languages.md)

---

## Level 4: what we would do

Per domain (prompts, UX research, ...): write the purpose and the questions the taxonomy
must answer; collect the words already in use; make a few facets; write a glossary entry
per concept (one preferred name, aliases, a one-line definition, a real example, a near
miss); test it by having two raters (Jonathan and a model, or two models) classify the
same sample; fix and repeat until they agree. Keep each repo's vocabulary separate, with
a small shared core and a map. Add patterns on top for design domains.
→ [design/](./design/README.md)

---

## Level 5: the sources

65 books, papers and standards, one folder each, in [`sources/`](./sources); the list is
[`sources.md`](./sources.md); the ones to fetch are in [`to-fetch.md`](./to-fetch.md).
