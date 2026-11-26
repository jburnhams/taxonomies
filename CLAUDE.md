# Working in taxonomies

Research into classification and naming, and a method for agreeing a taxonomy per
domain. Layout and reading order are in [`README.md`](./README.md).

- **Layers**: `sources/<slug>/` (one folder per source: README with citation, type,
  access, URL, what was read and when, stored files, notes), then topic docs at the root
  (`NN-topic.md`, each opening with a one-line answer and a plain explanation), then
  `design/`.
- **Stored copies never go in this repo**: it is public. PDFs, saved pages and extracted
  text go in the private [`jburnhams/taxonomies-sources`](https://github.com/jburnhams/taxonomies-sources)
  repo at `<slug>/<file>` (same folder names), with the path added to
  `sources/stored-files.txt` here and the README's **Stored** line linking to the folder.
  Link a stored file as `https://github.com/jburnhams/taxonomies-sources/blob/main/<slug>/<file>`.
  Notes and short quotes stay here.
- **Every source** read or cited gets a folder and a row in `sources.md`. Paywalled or
  unreachable ones go in `to-fetch.md`; move them out when read.
- **Evidence**: say whether a claim was read in the source or comes from prior
  knowledge; mark the latter for checking.
- **Changelog**: every change adds an entry to `changelog.md` in the same commit, grouped
  under `## YYYY-MM-DD`, newest first.
- **Design changes** are Jonathan's decisions: the design is a proposal until he adopts it.
- **Vocabulary**: the method's own words (facet, round, rater, warrant, near miss, ...)
  are defined once in [`domains/taxonomies/glossary.md`](./domains/taxonomies/glossary.md),
  in use since 2026-11-26. Use each entry's heading word, not its aliases, when writing
  `design/` and any domain's files; a concept with no entry gets a `candidate` entry
  there. Its facets ([`facets.md`](./domains/taxonomies/facets.md)) sort every rule:
  `check` says whether a script, a judgement or Jonathan settles it.
