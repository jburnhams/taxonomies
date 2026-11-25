# Ontology Development 101: A Guide to Creating Your First Ontology

- **Source**: Natalya F. Noy and Deborah L. McGuinness, "Ontology Development 101: A Guide to Creating Your First Ontology" (Stanford KSL-01-05, 2001).
- **Type**: Tech report / web guide
- **Access**: free to read
- **URL**: https://protege.stanford.edu/publications/ontology_development/ontology101-noy-mcguinness.html
- **Read**: Read in part 2026-11-25: the first half or so verbatim; the rest only as a summary, so claims from it are marked.
- **Stored here**: `noy-mcguinness-2001-ontology-101.html` (+ `.md`), with its figures in `img/`: the guide from protege.stanford.edu. Downloaded 2026-11-25; the notes below were written before this copy was stored and have not yet been re-checked against it. `.md` beside a file is its text, extracted for searching.
- **To fetch**: Nothing needed: the guide is stored here.
- **Used in**: [`04-vocabularies-and-ontologies.md`](../../04-vocabularies-and-ontologies.md), [`05-building-and-testing.md`](../../05-building-and-testing.md)

## What is distinctive

The friendliest step-by-step guide to modelling a domain; most of it applies to taxonomies too.

## Notes

- Three rules: "There is no one correct way to model a domain"; development "is necessarily an iterative process"; concepts "should be close to objects (physical or logical) and relationships in your domain of interest".
- Seven steps: determine domain and scope; consider reuse; enumerate important terms; define classes and hierarchy; define properties (slots); define facets of slots; create instances.
- **Competency questions**: "a sketch of questions that a knowledge base based on the ontology should be able to answer", the "litmus test" for scope.
- Naming: "Synonyms for the same concept do not represent different classes"; pick singular or plural and stick to it. *(From the summary part: a new subclass is justified when there is something to say about it that is not true of its parent; "between two and a dozen direct subclasses" is typical; a class with one subclass may signal a problem.)*
