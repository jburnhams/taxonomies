# Changelog

All notable changes, grouped by day, newest first. See [`CLAUDE.md`](./CLAUDE.md).

## 2026-11-25

**Downloaded copies of the sources (branch `claude/project-thread-sn5nqu`)**.
The coordinator asked for full copies of every source from the first pass, now that the
project has a cloud environment that can reach publisher and preprint hosts; Jonathan had
said storing papers and books is fine as the repo is private. 32 of 65 sources now have a
stored copy, most with extracted text. Only legitimately free copies were taken (open
access, author or repository copies, course reading lists, public-domain and Digital
Library of India scans); Internet Archive loans and anonymous uploads of in-copyright
books were left alone.

- `sources/*/`: 38 files added across 32 folders (PDFs or saved HTML pages, plus OCR text
  for the Wilkins 1668 and Ranganathan scans). Beside each PDF or page, a `.md` holds its
  extracted text for searching; the original file is the authority. Medin and Ortony 1989
  and Star and Griesemer 1989 are image scans with no text layer, so they have no `.md`.
- `sources/*/README.md`: the **Stored here** and **To fetch** lines of those 32 folders
  now name the files and where each came from. The notes themselves were written before
  the copies were stored and have **not** been re-checked against them yet.
- Corrections: the Lawrie copy is the 2007 journal extension, not the ICPC 2006 paper;
  the Ranganathan copy is the 1937 first edition, not the 1967 third; the Hofmeister
  copy is the SANER 2017 paper (a longer EMSE 2019 version exists); `hjorland-2017-
  classification/`'s URL pointed to the IEKO *knowledge organization* article, and the
  stored copy is the IEKO *classification* article.
- `sources.md`: new **Stored** column (yes / part / blank).
- `to-fetch.md`: rewritten. 9 items obtained and removed; 24 remain. Free copies found
  for Nickerson et al. 2013 (Augsburg postprint) and Usman et al. 2017 (ScienceDirect)
  but those servers refused this container, so they are listed with links to open in a
  browser.
- Not reachable from this container (site-level bot blocks or resets, not the network
  policy): opus.bibliothek.uni-augsburg.de, link.springer.com PDFs, dl.acm.org and
  cacm.acm.org, sciencedirect.com, aisel.aisnet.org, econstor.eu, philarchive.org,
  ideals.illinois.edu item pages (bitstreams worked), wordnet.princeton.edu,
  researchgate.net, tandfonline.com, web.archive.org. The Rosch 1978 course copy used in
  the first pass now returns 404.

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
