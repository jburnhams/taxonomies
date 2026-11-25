# Working in taxonomies

Research into classification and naming, and a method for agreeing a taxonomy per
domain. Layout and reading order are in [`README.md`](./README.md).

- **Layers**: `sources/<slug>/` (one folder per source: README with citation, type,
  access, URL, what was read and when, stored files, notes; raw copies stored beside it,
  which Jonathan has said is fine for this private repo), then topic docs at the root
  (`NN-topic.md`, each opening with a one-line answer and a plain explanation), then
  `design/`.
- **Every source** read or cited gets a folder and a row in `sources.md`. Paywalled or
  unreachable ones go in `to-fetch.md`; move them out when read.
- **Evidence**: say whether a claim was read in the source or comes from prior
  knowledge; mark the latter for checking.
- **Changelog**: every change adds an entry to `changelog.md` in the same commit, grouped
  under `## YYYY-MM-DD`, newest first.
- **Design changes** are Jonathan's decisions: the design is a proposal until he adopts it.
