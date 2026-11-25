# Changelog

All notable changes, grouped by day, newest first. See [`CLAUDE.md`](./CLAUDE.md).

## 2026-11-25

**First pass: literature review and a candidate system (branch `claude/project-thread-jyv2l9`)**.
Jonathan asked for the best research on taxonomy and naming, starting from an ELI5 and
going deep, laid out like `prompts` (sources, then topic docs, then our own design), with
a list of paywalled works to fetch, and a look at Alexander's *A Pattern Language*. The
container's network policy blocked downloads from every publisher and preprint host, so
no raw copies are stored yet; open sources were read through a web reader instead.

- `README.md`, `eli5.md`: **new**. Map of the repo; taxonomy from zero in six levels.
- `01-structures.md` to `08-pattern-languages.md`: **new** topic docs.
- `design/README.md`, `design/templates.md`, `design/first-look.md`: **new**. The candidate
  system (facets, SKOS-style glossary, bounded contexts, tested build method, pattern
  layer), its templates, and observations on the prompts and ux-research repos.
- `sources/` (65 folders), `sources.md`, `to-fetch.md`: **new**.
- Read online: Rosch 1978 (to p.15), Alexander 1965, Kundisch et al. 2022, Feitelson et al.
  2020 and the 2024 replication, Schober et al. 2009, Seppälä et al. 2017, Guarino and
  Welty (OntoClean), Noy and McGuinness, SKOS Reference, Evans's DDD Reference, Denton
  2003, ISKO "Facet analysis" (most in part).
- Not reached: Nickerson et al. 2013 (paywalled; its ending conditions are given from
  prior knowledge and marked), Furnas et al. 1987 full text (only the abstract, which is
  cut before its figure), Kwasnik 1999 (the IDEALS item has no fetchable PDF link),
  Meszaros and Doble (hillside.net refuses automated fetches). Everything else is in
  `to-fetch.md`.
