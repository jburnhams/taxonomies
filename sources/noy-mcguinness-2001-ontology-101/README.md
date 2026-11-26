# Ontology Development 101: A Guide to Creating Your First Ontology

- **Source**: Natalya F. Noy and Deborah L. McGuinness, "Ontology Development 101: A Guide to Creating Your First Ontology" (Stanford KSL-01-05, 2001).
- **Type**: Tech report / web guide
- **Access**: free to read
- **URL**: https://protege.stanford.edu/publications/ontology_development/ontology101-noy-mcguinness.html
- **Read**: Read in part 2026-11-25: the first half or so verbatim; the rest only as a summary, so claims from it are marked.
- **Stored** (private, in [`taxonomies-sources/noy-mcguinness-2001-ontology-101/`](https://github.com/jburnhams/taxonomies-sources/tree/main/noy-mcguinness-2001-ontology-101)): `noy-mcguinness-2001-ontology-101.html` (+ `.md`), with its figures in `img/`: the guide from protege.stanford.edu. Downloaded 2026-11-25; the parts of the notes marked as from a summary were checked against it the same day. `.md` beside a file is its text, extracted for searching.
- **To fetch**: Nothing needed: the guide is stored in `taxonomies-sources`.
- **Used in**: [`04-vocabularies-and-ontologies.md`](../../04-vocabularies-and-ontologies.md), [`05-building-and-testing.md`](../../05-building-and-testing.md)

## What is distinctive

The friendliest step-by-step guide to modelling a domain; most of it applies to taxonomies too.

## Notes

- Three rules: "There is no one correct way to model a domain"; development "is necessarily an iterative process"; concepts "should be close to objects (physical or logical) and relationships in your domain of interest".
- Seven steps: determine domain and scope; consider reuse; enumerate important terms; define classes and hierarchy; define properties (slots); define facets of slots; create instances.
- **Competency questions**: "a sketch of questions that a knowledge base based on the ontology should be able to answer", the "litmus test" for scope.
- Naming: "Synonyms for the same concept do not represent different classes"; pick singular or plural and stick to it. 
- Siblings (§4.2, checked against the stored text 2026-11-25): "many well structured ontologies have between two and a dozen direct subclasses"; one direct subclass suggests "a modeling problem or the ontology is not complete"; more than a dozen suggests missing intermediate categories.
- When to add a class (§4.4, checked): "we introduce a new class in the hierarchy usually only when there is something that we can say about this class that we cannot say about the superclass".
