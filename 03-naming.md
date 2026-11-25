# 3. Naming

**In one line**: people almost never pick the same name for the same thing, so a
shared name has to be agreed and written down, with the other names people reach for
kept as aliases. Fields that have done this for centuries (biology above all) keep the
name separate from the classification and anchor it to an example.

## The simple version

If you and a friend each name a new toy, you will almost certainly choose different
names. That is not because one of you is bad at naming: it is normal. So the fix is not
"find the perfect name". It is: pick one name together, write it on the box, and also
write the other names people might use, so anyone looking for "the red truck" still
finds "the fire engine".

## The measurements

- **Furnas et al. (1987)**, across several domains (commands, recipes, classified
  ads): two people chose the same word for an object with probability **under 0.2**.
  One "obvious" name chosen by a designer (armchair naming) fails most users; many
  aliases per object fix most of it
  ([`furnas-1987`](./sources/furnas-1987-vocabulary-problem/); figures need checking
  against the full text).
- **Feitelson et al. (2020)**, for code: the median probability that two developers
  choose the same name for a variable or function was **6.9%**. Names by others were
  usually understood, but that "may hide different assumptions" that lead to bugs. A
  2024 replication confirms it
  ([`feitelson-2021`](./sources/feitelson-2021-how-developers-choose-names/)).

Feitelson's **three-step model** is a useful procedure: (1) choose which concepts the
name must carry, (2) choose a word for each, (3) put them together. People taught it
produced names judged better two to one. Most naming arguments are about step 1 (what
should the name say?), not step 2 (which word?), so settle step 1 explicitly.

## What biology learned (the strongest precedent)

The zoological and botanical codes ([`biological-nomenclature-codes`](./sources/biological-nomenclature-codes/))
run on five rules that carry straight over:

1. **Naming is separate from classifying.** Scientists may reclassify freely; the codes
   only decide what a group is called.
2. **Every name is anchored to a type** (a specimen, or a lower-ranked name). If a group
   is split, the name goes with the part that holds the type. The name points at a
   thing, not a description.
3. **Priority**: the first valid name wins; later ones become synonyms. Stability beats
   aptness.
4. **A name is a label, not a description**: an inapt name is not replaced for being inapt.
5. **No homonyms**: one name, one group.

The PhyloCode goes further and drops mandatory ranks, defining each name by explicit
anchors ([`phylocode-2020`](./sources/phylocode-2020/)): put the level in the name and
every reorganisation renames things.

The cautionary tale is Wilkins's 1668 universal language, where each word spelled out
its thing's place in a universal classification
([`wilkins-1668`](./sources/wilkins-1668-real-character-and-borges/)). Change the
classification and every word breaks. Do not encode the hierarchy in the names.

## Rules for writing a name (term)

From the OBO Foundry's survey-based conventions
([`schober-2009`](./sources/schober-2009-obo-naming-conventions/)), the NISO thesaurus
standard ([`niso-z39-19`](./sources/niso-z39-19-2005/)), and the identifier studies
([`deissenboeck-pizka-2006`](./sources/deissenboeck-pizka-2006-concise-consistent-naming/),
[`lawrie-2006`](./sources/lawrie-2006-whats-in-a-name/),
[`hofmeister-2017`](./sources/hofmeister-2017-shorter-names/),
[`arnaoudova-2016`](./sources/arnaoudova-2016-linguistic-antipatterns/)):

- **One concept, one name; one name, one concept** (within a context).
- **Nouns or noun phrases** for things; a noun for a process too ("compaction", not
  "compact"). Singular (OBO) for concepts; Z39.19 prefers plurals for countable
  things in thesauri, but allows singular where the field's own usage is singular
  (§6.5.1.1: body parts in medicine, objects in a museum catalogue). We pick one and
  stick to it.
- **Explicit and concise**; no articles.
- **No abbreviations** unless the short form is the one everyone uses (Z39.19 §6.6.3:
  "so well established that the full form ... is rarely used"; then alias the full
  form). Evidence, checked 2026-11-25: in Hofmeister et al. 2017, 72 professional
  developers found semantic defects 19% faster with full words than with letters or
  abbreviations, and abbreviations were no better than letters; Lawrie et al. found full
  words best for comprehension but often not significantly better than abbreviations,
  which were easier to remember. So full words as the preferred label, abbreviations
  as aliases.
- **No "and" / "or"** in a name: it is two concepts.
- **No negations** ("non-interactive agent"): name what it is.
- **No catch-alls** ("other", "misc", "unknown"): they hide the places the scheme fails.
- **No claims in the name** ("agent class", "type of review").
- **No admin data in the name** (dates, owners, status).
- **Names must not lie**: the scope the name implies must match the definition.

## Rules for writing a definition

Seppälä, Ruttenberg and Smith ([`seppala-2017`](./sources/seppala-2017-definitions/)):

- **Genus-differentia**: *an A is a B that C*, with exactly one genus, the nearest one.
  Example: "mammal: a vertebrate that has hair, gives live birth, and nurses its young".
- Necessary and, where possible, jointly sufficient conditions.
- No circularity; not too broad, not too narrow; one thing per definition.
- No "usually"; no examples inside the definition (they go in their own field); no
  negative definitions.

This is the classical view of [2](./02-how-minds-categorise.md), used on purpose: the
definition is for checking membership, while the **type example** carries the
prototype that people actually think with. Keep both.

## Choosing which word

- **Warrant** (Z39.19): take words from the material (literary warrant), from the
  people who will use them (user warrant), and from what the project needs
  (organisational warrant). In a repo, the first two are the existing docs and the
  words Jonathan uses when he talks about it.
- **Basic level** for the intended readers ([2](./02-how-minds-categorise.md)).
- **Check ambiguity** against plain English (WordNet,
  [`wordnet-1995`](./sources/wordnet-1995/)): a word with many senses ("agent",
  "model", "context") needs a tight scope note.
- **Evocative, short, sayable** for pattern names, named after the result, and tested by
  asking someone who has not read the definition to guess its meaning from the name
  ([8](./08-pattern-languages.md)).
- **Ranganathan's Canons of Terminology** (*Prolegomena*, 1937, pp. 62-72; read
  2026-11-25 from the stored scan), which anticipate most of the above:
  **Currency**: use the term current "among those who specialise in" the domain, and
  have "some arrangement by which the terms can be changed over to current ones";
  **Reticence**: terms "should not be critical", only "purely descriptive and not
  opinionative" (no "legacy", "hacky", "minor"); **Enumeration** and **Context**: a
  term's meaning is fixed by what is listed under it and by where it sits, because
  "one and the same term denotes several different entities". The last two are why a
  term entry needs its broader term and its scope note, not just a label.

Next: [4. Vocabularies and ontologies](./04-vocabularies-and-ontologies.md).
