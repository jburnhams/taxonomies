# A translation approach to portable ontology specifications

- **Source**: Thomas R. Gruber, "A translation approach to portable ontology specifications", *Knowledge Acquisition* 5(2), 1993, 199-220.
- **Type**: Journal article
- **Access**: paywalled (preprints circulate)
- **URL**: none found
- **Read**: Read 2026-11-25 from the stored preprint: sections 1-2 closely; the Ontolingua sections skimmed.
- **Stored here**: [`gruber-1993-ksl-92-71.pdf`](https://github.com/jburnhams/taxonomies-sources/blob/main/gruber-1993-ontology-definition/gruber-1993-ksl-92-71.pdf) (+ `.md`): Stanford KSL technical report 92-71 (revised April 1993), the preprint of the *Knowledge Acquisition* article, from a University of Utah course page. Downloaded 2026-11-25; notes checked against it the same day. `.md` beside a file is its text, extracted for searching.
- **To fetch**: Nothing needed: the preprint is stored here.
- **Used in**: [`04-vocabularies-and-ontologies.md`](../../04-vocabularies-and-ontologies.md)

## What is distinctive

The standard definition of an ontology in computing.

## Notes

Checked against the stored KSL 92-71 preprint 2026-11-25.

- **Definition** (§1): "An ontology is an explicit specification of a conceptualization." A conceptualization is "an abstract, simplified view of the world that we wish to represent **for some purpose**", the things presumed to exist and their relationships. Studer et al. (1998) later added "formal" and "shared" (from prior knowledge; not stored).
- **What an ontology contains** (§1): definitions that associate names "with human-readable text describing what the names are meant to denote, and formal axioms that constrain the interpretation and well-formed use of these terms". So even Gruber's ontologies are names plus prose definitions first; the axioms are the extra.
- **Commitment** (§2): agents sharing an ontology commit to its terms' meanings, not to each other's internals. "A commitment to a common ontology is a guarantee of consistency, but not completeness." A shared vocabulary does not need to describe everything to be useful.
- **Not in this paper**: the design criteria often attributed to Gruber (clarity, coherence, extendibility, minimal encoding bias, minimal ontological commitment) are from his 1995 paper "Toward principles for the design of ontologies used for knowledge sharing", not stored. The first pass did not cite them; noted here to avoid the mix-up.
- The difference from a taxonomy: an ontology adds typed relations, properties and axioms that a machine can reason over. Most of our need is met by names, prose definitions and a few relations; formal axioms are optional.
