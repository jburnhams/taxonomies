# SKOS Simple Knowledge Organization System Reference

- **Source**: Alistair Miles and Sean Bechhofer (eds.), *SKOS Simple Knowledge Organization System Reference*, W3C Recommendation, 18 August 2009.
- **Type**: Web standard
- **Access**: open (W3C document licence: copying permitted with notice)
- **URL**: https://www.w3.org/TR/skos-reference/
- **Read**: Read 2026-11-25 (online copy, see URL). Later sections partly from a summary.
- **Stored here**: `skos-reference-2009.html` (+ `.md`): the W3C Recommendation. Downloaded 2026-11-25; the later sections were checked against it the same day. `.md` beside a file is its text, extracted for searching.
- **To fetch**: Nothing needed: the Recommendation is stored here.
- **Used in**: [`04-vocabularies-and-ontologies.md`](../../04-vocabularies-and-ontologies.md)

## What is distinctive

The lightweight, standard data model for a vocabulary: concepts, labels, notes, broader/narrower, and mappings to other schemes.

## Notes

- Classes: `Concept`, `ConceptScheme`, `Collection` (and `OrderedCollection`).
- Labels: `prefLabel`, `altLabel`, `hiddenLabel` (for misspellings). Integrity: "no more than one value of skos:prefLabel per language tag" (S14); the three labels are "pairwise disjoint" (S13).
- Notes: `definition`, `scopeNote`, `example`, `historyNote`, `changeNote`, `editorialNote`.
- Relations: `broader`/`narrower` (direct, **not** transitive), `broaderTransitive`, `related`. `related` is disjoint with `broaderTransitive` (S27). Polyhierarchy (two broaders) is allowed.
- Mappings between schemes: `exactMatch`, `closeMatch`, `broadMatch`, `narrowMatch`, `relatedMatch`. Checked against the stored text 2026-11-25: `exactMatch` ("a high degree of confidence that the concepts can be used interchangeably") is the only transitive mapping property and is a sub-property of `closeMatch`; `exactMatch` is disjoint with `broadMatch` and `relatedMatch` (S46). Because it is transitive, an `exactMatch` chain across three repos asserts that the first and last terms are interchangeable, so use `closeMatch` unless that is really meant.
- SKOS deliberately says nothing about cycles in `broader` or whether `related` is reflexive (§8.6.8 and the notes after S27): a scheme can be valid SKOS and still have a loop; checking for loops is our job.
- For us: SKOS is the field list for a term entry. We can write it in markdown and convert later if we ever need RDF.
