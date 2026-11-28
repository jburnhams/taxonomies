# taxonomies

Research into taxonomy, classification and naming: "the science of naming things", and
a method for agreeing a taxonomy up front that can then be applied to Jonathan's
domains, starting with agent design ([`jburnhams/prompts`](https://github.com/jburnhams/prompts))
and UX research ([`jburnhams/ux-research`](https://github.com/jburnhams/ux-research)).

Laid out like `prompts`: **sources** (one folder each), then **topic docs** that synthesise
across them, then **our own design**. First pass: 2026-11-25. Changes by day are in
[`changelog.md`](./changelog.md).

## Start here

**[→ `eli5.md`](./eli5.md)**: taxonomy from zero, in levels: like you're five, the
words, the six big findings, whether it is a solved problem, what we would do.

## Topic docs

Each opens with a one-line answer and a plain explanation, then goes deep.

1. [`01-structures.md`](./01-structures.md): lists, trees, grids, facets, networks;
   Ranganathan, Kwasnik, Alexander's "A City is Not a Tree".
2. [`02-how-minds-categorise.md`](./02-how-minds-categorise.md): prototypes, the basic
   level, radial categories; Rosch, Lakoff, Murphy, Berlin.
3. [`03-naming.md`](./03-naming.md): why people pick different names, biology's naming
   codes, rules for names and definitions.
4. [`04-vocabularies-and-ontologies.md`](./04-vocabularies-and-ontologies.md):
   thesauri, SKOS, ontologies, OntoClean.
5. [`05-building-and-testing.md`](./05-building-and-testing.md): Nickerson's method
   and its update, facet building, card sorting, LLM clustering, agreement tests.
6. [`06-shared-language-in-software.md`](./06-shared-language-in-software.md):
   Domain-Driven Design's ubiquitous language and bounded contexts, identifier research.
7. [`07-limits-and-politics.md`](./07-limits-and-politics.md): why there is no one
   right taxonomy; Bowker and Star, Borges and Wilkins.
8. [`08-pattern-languages.md`](./08-pattern-languages.md): Alexander, software
   patterns, and how pattern languages relate to taxonomies.

## Our design

**[→ `design/`](./design/README.md)**: the candidate system (proposal, not adopted):
facets plus a SKOS-style glossary per bounded context, built by an iterative tested
method, with an optional pattern layer. Templates in
[`design/templates.md`](./design/templates.md); a first look at the two repos in
[`design/first-look.md`](./design/first-look.md); what the stored sources suggest
changing in [`design/source-check-2026-11-25.md`](./design/source-check-2026-11-25.md).

**The method, in full**: [`design/process.md`](./design/process.md) (step by step) and
[`design/spec.md`](./design/spec.md) (what the files contain, the rules, governance and
tests), with every rule citing a stored source by path and page.
[`design/decisions.md`](./design/decisions.md) lists the choices only Jonathan can make.
`python3 tools/check_citations.py` checks that each rule and step cites a stored file
that exists (in `sources/stored-files.txt`, and on disk too if `taxonomies-sources` is
checked out beside this repo).
Changes for large domains are proposed in
[`design/method-v1.1.md`](./design/method-v1.1.md) (not adopted).

## Domains

- [`domains/ux/`](./domains/ux/scope.md): `jburnhams/ux-research`, in use since 2026-11-26.
- [`domains/prompts/`](./domains/prompts/scope.md): `jburnhams/prompts`, stage 1 (kernel
  and areas) started 2026-11-26.
- [`domains/taxonomies/`](./domains/taxonomies/scope.md): this repo's own method, in use
  since 2026-11-26.
- [`domains/voice/`](./domains/voice/scope.md): `jburnhams/voice-research` (spoken and
  written voice cloning), stage 1 (kernel and areas) in use since 2026-11-27, aligned with `prompts`.

## Domains and the explorer site

Each domain's taxonomy lives in `domains/<name>/` (spec §1):
[`ux`](./domains/ux/scope.md) (in use), `prompts` (in progress) and
[`taxonomies`](./domains/taxonomies/scope.md) (the method's own words, in use).
**[`site/`](./site/README.md)** builds a browsable site from them on every push to `main`:
an overview, then each domain's facets, terms, items and rounds, down to each rater's
answers. Published at <https://jburnhams.github.io/taxonomies/>.

**Asking for a term.** From any repo, with no checkout:
`curl -fsSL https://raw.githubusercontent.com/jburnhams/taxonomies/main/tools/term.py | python3 - lookup prompts "approval mode"`
gives the term to use, or the closest ones; `changes <domain> --since <date>` lists what
changed, breaking changes marked. When nothing fits, file a
[term request](https://github.com/jburnhams/taxonomies/issues/new?template=term-request.yml)
issue here; a weekly intake (Tuesdays) answers it on the issue and logs it in
`domains/<name>/requests.md`. Rules (adopted 2026-11-27): [`design/growth.md`](./design/growth.md).

## Sources

- [`sources/`](./sources): one folder per source with citation, access, what was read,
  and notes. Stored copies (PDFs, saved pages, extracted text) are kept out of this public
  repo, in the private [`jburnhams/taxonomies-sources`](https://github.com/jburnhams/taxonomies-sources)
  repo under the same folder names; [`sources/stored-files.txt`](./sources/stored-files.txt)
  lists them.
- [`sources.md`](./sources.md): the full list by field, with read status.
- [`to-fetch.md`](./to-fetch.md): paywalled or blocked items for Jonathan to fetch,
  most useful first.

**Evidence levels.** Each source folder says whether it was read (with date), read in
part, or not read this pass. Notes on unread works come from prior knowledge of
well-known texts and are marked for checking; topic docs say "from prior knowledge" where
a claim rests on one.
