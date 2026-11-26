# Building Ontologies with Basic Formal Ontology

- **Source**: Robert Arp, Barry Smith, Andrew D. Spear, *Building Ontologies with Basic Formal Ontology* (MIT Press, 2015); and Smith et al., "The OBO Foundry", *Nature Biotechnology* 25(11), 2007.
- **Type**: Book + article
- **Access**: book paywalled; MIT Press may have an open edition (not checked)
- **URL**: none found
- **Read**: Book not read; the 2007 OBO Foundry paper read in full 2026-11-25 from the stored copy.
- **Stored** (private, in [`taxonomies-sources/arp-smith-spear-2015-bfo/`](https://github.com/jburnhams/taxonomies-sources/tree/main/arp-smith-spear-2015-bfo)): `smith-2007-obo-foundry.html` (+ `.md`): Smith et al. 2007, "The OBO Foundry", author manuscript from PMC (PMC2814061). The book is not stored. Downloaded 2026-11-25; notes checked against it the same day. `.md` beside a file is its text, extracted for searching.
- **To fetch**: The book (the OBO Foundry paper is stored).
- **Used in**: [`04-vocabularies-and-ontologies.md`](../../04-vocabularies-and-ontologies.md)

## What is distinctive

The realist school of ontology building, with a top-level split every domain can sit under.

## Notes

The book is not stored. Checked 2026-11-25 against the stored OBO Foundry paper (Smith et al. 2007, author manuscript); points only the book makes are marked.

- **Top split, confirmed in the paper's Table 1**: **continuants** (things that persist: organisms, cells, molecules, and dependent ones such as qualities and functions) vs **occurrents** (processes at each scale). The Foundry's ontologies are laid out as a grid of granularity (organ/organism, cell, molecule) by continuant/occurrent, itself a paradigm in Kwasnik's sense.
- **Principles inherited from the Gene Ontology** (paper): ontologies should be **open** (usable without licence, open to change by community debate), **orthogonal** (scope "clearly bounded" and "no term should appear in more than one ontology"), in a well-specified syntax, and sharing one space of **identifiers** so old annotations survive change.
- **Definitions** (paper): genus-differentia form, from the FMA: "an A = def. a B that C's where B is the 'is_a' parent of A". Anchoring definitions in the is-a hierarchy "diminishes the role of opinion in determining where terms should be placed".
- **Cross-products** (paper): build compound terms by composing terms from several ontologies (PATO "increased concentration" + FMA "blood" + ChEBI "glucose") instead of pre-listing each one; this avoids an approval bottleneck for every new term. It is faceted, post-coordinated classification under another name.
- **Convergence** (paper): members commit "that, for any particular domain, there is convergence on a single ontology"; several rival cell-type ontologies were merged into one.
- Single inheritance in the asserted hierarchy, univocal terms and "reuse before you invent" are the book's rules (from prior knowledge; book not read).
- For us: the continuant/occurrent split is a good first facet check (is this term a thing, a property, a role, or a happening?); orthogonality is the rule that each term has one home context; composing terms from facets beats enumerating compounds.
