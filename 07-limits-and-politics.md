# 7. Limits and politics: why there is no one right taxonomy

**In one line**: the method is solved; the content is not and cannot be. Every
classification serves a purpose and a point of view, nothing real fits perfectly, and
the places it does not fit are where the useful information is.

## The simple version

There is no perfect way to sort toys, only a good way for a reason: tidying up, finding
things fast, or sharing with a sibling. Pick the reason first. And always keep a small
"not sure yet" box, look in it often, and change the other boxes when it fills up.

## The dream of one universal scheme

John Wilkins (1668) built a classification of everything and a language whose words
spelled out each thing's place in it. Borges mocked the dream with a fictional Chinese
encyclopaedia that divides animals into "those that belong to the Emperor, embalmed
ones, ... others", concluding "there is no classification of the universe that is not
arbitrary and conjectural"
([`wilkins-1668-and-borges`](./sources/wilkins-1668-real-character-and-borges/)). This
is the answer to "it feels like it should be a solved problem": the **procedure** is
solved (sections 1-6); a single **correct** taxonomy of anything interesting is not on
offer.

## Bowker and Star: what classifications do

*Sorting Things Out* ([`bowker-star-1999`](./sources/bowker-star-1999-sorting-things-out/);
quotes from prior knowledge, to check):

- The ideal classification has consistent, unique principles, mutually exclusive
  categories, and completeness. "No real-world working classification system that we
  have looked at meets these 'simple' requirements and we doubt that any ever could."
- Classifications become **invisible infrastructure**: once in use, nobody sees them, and
  they shape what can be said and counted.
- **Residual categories** ("other", "not elsewhere classified") are where the scheme
  fails, and so where to look.
- **Torque**: the strain when a thing's real path does not fit its category over time.
- **Boundary objects** (from Star and Griesemer,
  [`star-griesemer-1989`](./sources/star-griesemer-1989-boundary-objects/)): things
  "plastic enough to adapt to local needs ... yet robust enough to maintain a common
  identity across sites". A shared vocabulary across projects should be one.

## Pragmatism: judge by purpose

Hjørland's position ([`isko-encyclopedia`](./sources/isko-encyclopedia/),
[`hjorland-2017`](./sources/hjorland-2017-classification/)): a classification is good
relative to a purpose and a community, not "natural" or "true". He criticises facet
analysis itself as a priori, with a "lack of empirical basis" and a "speculative
ordering of knowledge". Noy and McGuinness agree from the engineering side: "There is
no one correct way to model a domain." Hence the first step of our method is writing
down the purpose.

## Taxonomies harden

Once names are in code, prompts and file paths, changing them costs real work, so the
first taxonomy tends to stick (the invisible-infrastructure point again). Two defences:

- **Stable IDs and aliases**, so a rename does not break references
  ([3](./03-naming.md), [4](./04-vocabularies-and-ontologies.md)).
- **Explicit operations and a change log** (add, rename, split, merge, promote, demote,
  deprecate), so change is routine rather than a crisis
  ([5](./05-building-and-testing.md)).

## Agreeing up front: how much?

Jonathan's question is whether projects go better with the taxonomy agreed first. The
literature supports agreeing **the purpose, the method, the naming rules and a first
draft** up front, and treating the content as a hypothesis that gets revised by
evidence:

- Nickerson's method assumes iteration; nobody gets it right in one pass.
- Evans: the language evolves with the model, but it is always explicit and shared.
- Biology: priority and types keep names stable while the classification moves.
- Alexander: patterns are marked with asterisks for how sure the authors are.

So "agreed up front" should mean "agreed and written down before work starts, with a
known way to change it", not "fixed".

Next: [8. Pattern languages](./08-pattern-languages.md).
