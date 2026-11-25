# 5. Building and testing a taxonomy

**In one line**: there are published, tested methods. State the purpose, alternate
between "group what you see" and "test what you think", stop when written ending
conditions hold, and check that two people (or a person and a model) classify the same
things the same way.

## The simple version

Tip all the toys on the floor. Make piles that seem right and name them. Then take
your pile names and try to sort a fresh bag of toys into them. Wherever you hesitate,
fix the piles or the names. Stop when a new bag sorts without trouble and a friend sorts
it the same way you did.

## The methods

### Nickerson, Varshney and Muntermann (2013)

The most used method in information systems
([`nickerson-2013`](./sources/nickerson-2013-taxonomy-method/); paywalled, details via
[`kundisch-2022`](./sources/kundisch-2022-taxonomy-update/) and prior knowledge):

1. Choose a **meta-characteristic**, "derived from the purpose and target users of the
   taxonomy": the one thing every dimension must relate to.
2. Write the **ending conditions** (below).
3. Loop. Each round is either
   - **empirical-to-conceptual**: take a set of real objects, find their characteristics,
     group them into dimensions; or
   - **conceptual-to-empirical**: propose dimensions from what you know, then test them
     on objects.
4. Stop when the ending conditions hold.

**Subjective ending conditions**: "concise, robust, comprehensive, extendible, and
explanatory". **Objective** ones (from prior knowledge; check against the paper): every
object in the sample classified; no object merged or split in the last round; at least
one object in every characteristic; no dimension or characteristic added in the last
round; every dimension unique; no duplicate characteristics within a dimension.

### Kundisch et al. (2022): the update

Reviewing 164 IS taxonomy papers, they found only **34% evaluated** the result
([`kundisch-2022`](./sources/kundisch-2022-taxonomy-update/), CC BY). Their extended
process wraps Nickerson's loop with objectives, demonstration, evaluation and
communication, and adds:

- Do at least one round of **each** kind of iteration.
- **Evaluate twice**: *ex ante* by the designers ("Is it a taxonomy? Is it applicable?")
  and *ex post* with users ("Is it useful?"), each with a method, criteria and a
  target value.
- **Taxonomy operations** for maintenance: add; update (rename, swap, split, merge,
  promote, demote); delete. Our change log uses these words.

### Software engineering's version

Usman et al. (2017) found most software engineering taxonomies were hierarchies built
without a stated method and rarely validated, and proposed a 13-step method that makes
**choosing the structure** (hierarchy, tree, paradigm, facets) an explicit step
([`usman-2017`](./sources/usman-2017-se-taxonomies/)).

### Building facets: Denton's seven steps

The practical recipe ([`denton-2003`](./sources/denton-2003-faceted-howto/)):
1 domain collection, 2 entity listing (break descriptions into concepts),
3 facet creation, 4 facet arrangement (order the values; test-classify),
5 citation order, 6 classification, 7 revision, testing and maintenance.

### Ontology building

Noy and McGuinness's seven steps start with scope and **competency questions** and
"consider reusing existing" vocabularies
([`noy-mcguinness-2001`](./sources/noy-mcguinness-2001-ontology-101/)).

These four agree on the shape: **purpose first, a sample of real things, alternating
bottom-up and top-down rounds, explicit stopping rules, then test with users.**

## Finding categories from data

- **Card sorting** ([`spencer-2009`](./sources/spencer-2009-card-sorting/)): open sorts
  find people's own groups and words; closed sorts test yours. About 15 participants
  gives stable results (Tullis and Wood,
  [`tullis-wood-2004`](./sources/tullis-wood-2004-card-sort-sample-size/), figures to
  check). Follow with **tree testing**.
- **Clustering**: numerical taxonomy's descendants
  ([`sokal-sneath-1963`](./sources/sokal-sneath-1963-numerical-taxonomy/)). With LLMs:
  TnT-LLM has a model propose and refine a label taxonomy from batches of text, then
  label at scale ([`wan-2024-tnt-llm`](./sources/wan-2024-tnt-llm/)); Clio clusters
  conversations and has a model name the clusters
  ([`tamkin-2024-clio`](./sources/tamkin-2024-clio/)). Good for the
  empirical-to-conceptual round on a pile of files. Clusters show what looks alike, not
  what the groups mean; the names still go through [3](./03-naming.md). Details checked
  2026-11-25: TnT-LLM's loop is generate, then per batch *evaluate, list issues,
  modify*, then a final review, all by the model and all carrying a **use-case
  instruction** (the purpose and the label format), with no person in the loop; Clio
  extracts "facets" per item, clusters one facet with embeddings and k-means, and
  recovered known topics with 94% accuracy on synthetic data. Neither shows the
  categories are the right ones for a purpose, so a person still decides.
- **Workshops**: EventStorming harvests a domain's words fast and shows where one word
  means two things ([`brandolini-event-storming`](./sources/brandolini-event-storming/)).
- **Grounded theory**: build categories from cases and keep revising (Star,
  [`star-1998`](./sources/star-1998-grounded-classification/)). Its core move is
  **constant comparison**: compare unlike cases to find the dimensions they share
  ("why is a priest like a prostitute?"), which is a concrete way to find facets.

## Testing agreement

The objective test that a taxonomy's terms are clear: give two raters the vocabulary
only, have them classify the same sample independently, and measure agreement beyond
chance with **Cohen's kappa** ([`cohen-1960-kappa`](./sources/cohen-1960-kappa/)). Rough
benchmarks: above 0.6 substantial, above 0.8 almost perfect. Low agreement on one facet
means its definitions or boundaries are unclear; the items people disagree on show where.

For a one-person project, the raters can be Jonathan and a model, or two fresh model
sessions given only the vocabulary. A model that cannot apply the vocabulary from its
definitions is a useful warning that a new contributor could not either.

## What this means for our design

The procedure in [`design/`](./design/README.md) is Nickerson's loop with Denton's
facet steps inside it, Kundisch's evaluation and operations around it, competency
questions as the purpose test, and a kappa check as the main objective ending condition.

Next: [6. Shared language in software](./06-shared-language-in-software.md).
