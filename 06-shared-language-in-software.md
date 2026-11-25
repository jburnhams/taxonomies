# 6. Shared language in software

**In one line**: software's best answer to "naming things" is Domain-Driven Design's
*ubiquitous language*: one set of words used by everyone and in the code, valid inside
an explicitly **bounded context**, with explicit maps between contexts. It argues
against one global taxonomy for everything.

## The simple version

At home "the remote" means the TV remote. At work it means a git server. Both are fine,
as long as everyone knows which room they are in. So instead of forcing one meaning for
every word everywhere, draw the rooms, agree the words inside each room, and keep a
small dictionary for the words that travel between rooms.

## Ubiquitous language and bounded contexts

Eric Evans ([`evans-2003`](./sources/evans-2003-domain-driven-design/); the 2015
Reference is CC BY):

- **Ubiquitous Language**: "Use the model as the backbone of a language." The same
  words in conversation, docs, prompts and code. "Recognize that a change in the
  language is a change to the model": renaming is design work, not tidying.
- **Bounded Context**: "Explicitly define the context within which a model applies."
  Inside a context, one meaning per word. Across contexts, a word may differ, and that
  is allowed.
- **Context Map**: how contexts relate. The patterns: Partnership, **Shared Kernel** (a
  small shared subset changed only by agreement), Customer/Supplier, Conformist,
  **Anticorruption Layer** (translate the other context's words into yours),
  Open-host Service, **Published Language** (a documented shared vocabulary for
  exchange), Separate Ways, Big Ball of Mud.

Mapped onto Jonathan's repos: **each repo (prompts, ux-research, ...) is a bounded
context** with its own vocabulary. A **shared kernel** holds the few terms that truly
mean the same across them. SKOS mapping links (`exactMatch`, `closeMatch`, ...) are the
context map written down ([4](./04-vocabularies-and-ontologies.md)).

This is the same conclusion as Bowker and Star's **boundary objects**: shared
vocabularies work when they are loose enough to be used by different groups and tight
enough to mean something in each ([7](./07-limits-and-politics.md)).

## Naming inside code

- "There are only two hard things in Computer Science: cache invalidation and naming
  things" (Phil Karlton, via [Fowler](./sources/karlton-two-hard-things/)).
- Two developers pick the same name 6.9% of the time (median), and teaching a
  three-step procedure (concepts, then words, then the name) makes names better
  ([`feitelson-2021`](./sources/feitelson-2021-how-developers-choose-names/)).
- **Consistent and concise naming**: one name per concept and one concept per name,
  checked against an explicit identifier dictionary
  ([`deissenboeck-pizka-2006`](./sources/deissenboeck-pizka-2006-concise-consistent-naming/)).
  That dictionary is a controlled vocabulary.
- Full words beat abbreviations and single letters for comprehension
  ([`lawrie-2006`](./sources/lawrie-2006-whats-in-a-name/),
  [`hofmeister-2017`](./sources/hofmeister-2017-shorter-names/)).
- **Linguistic antipatterns**: names that promise what the thing does not do
  ([`arnaoudova-2016`](./sources/arnaoudova-2016-linguistic-antipatterns/)).

## Taxonomies in software engineering research

Software engineering builds many taxonomies (of defects, of agents, of architectures),
mostly hierarchies, mostly without a stated method, rarely validated
([`usman-2017`](./sources/usman-2017-se-taxonomies/)). The prompts repo's own
[`papers/inside-the-scaffold`](https://github.com/jburnhams/prompts/tree/main/papers/inside-the-scaffold)
taxonomy of coding agents is an example of the genre, and a useful one: it found that
control strategies form a spectrum rather than discrete categories, which is a reason to
use facets with ordered values rather than boxes.

## Why this matters more with agents

An agent reads the vocabulary every time it runs. Synonyms in a prompt or a CLAUDE.md
cost it the same as they cost a new developer: it has to guess whether "tool",
"function" and "action" are one thing or three. A glossary that the agent loads is a
ubiquitous language for humans and models together, and kappa between two model
sessions is a direct test of whether the language is clear
([5](./05-building-and-testing.md)).

Next: [7. Limits and politics](./07-limits-and-politics.md).
