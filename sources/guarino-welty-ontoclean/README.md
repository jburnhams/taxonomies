# An Overview of OntoClean

- **Source**: Nicola Guarino and Christopher Welty, "An Overview of OntoClean", in Staab and Studer (eds.), *Handbook on Ontologies* (Springer, 2004; 2nd ed. 2009). Also "Evaluating ontological decisions with OntoClean", *CACM* 45(2), 2002.
- **Type**: Book chapter
- **Access**: free author copy
- **URL**: https://www.loa.istc.cnr.it/wp-content/uploads/2020/03/OverviewOntoClean-compresso.pdf
- **Read**: Read in full 2026-11-25 (first half in the first pass, second half from the stored PDF).
- **Stored** (private, in [`taxonomies-sources/guarino-welty-ontoclean/`](https://github.com/jburnhams/taxonomies-sources/tree/main/guarino-welty-ontoclean)): `guarino-welty-2004-overview-of-ontoclean.pdf` (+ `.md`): the *Handbook on Ontologies* chapter, author copy from ISTC-CNR. The 2002 CACM article is not stored. Downloaded 2026-11-25; notes checked against it the same day. `.md` beside a file is its text, extracted for searching.
- **To fetch**: Nothing needed: what the notes rely on was readable online.
- **Used in**: [`04-vocabularies-and-ontologies.md`](../../04-vocabularies-and-ontologies.md)

## What is distinctive

A test for whether an is-a link is valid, using properties of the concepts themselves.

## Notes

First pass read the first half; the rest (the pitfalls and the worked example) checked against the stored chapter 2026-11-25.

- **Rigidity**: a property is rigid (+R) if "essential to all its possible instances" (Person); anti-rigid (~R) if every instance can stop having it (Student); semi-rigid otherwise. "Every property in an ontology should be labeled as rigid, non-rigid, or anti-rigid."
- **Identity** (+I, +O): whether the property carries (or supplies) a criterion for telling instances apart ("is that my dog?"), at one time or over time.
- **Unity** (+U, -U, ~U): whether instances are wholes, and by what criterion.
- **Dependence** (+D): whether an instance needs something else to exist.
- **Constraints on is-a**: "antirigid properties cannot subsume rigid properties" (Student cannot subsume Human); a ~U property cannot subsume a +U one; properties with incompatible identity criteria cannot subsume each other.
- **The pitfalls the worked example exposes** (second half):
  - **Constitution mistaken for is-a**: living beings are *constituted of* matter, not kinds of matter ("one of the most common modeling problems we have seen"); a club is constituted of people.
  - **"Can be" mistaken for "is a"**: their own example has **Agent** subsuming Animal and Social Entity. Agent is anti-rigid (a role), so the links are wrong: "The modeler intends to mean, not that all animals are agents, but that animals can be agents. This is a very common misuse".
  - **Phases** (Caterpillar, Butterfly) are anti-rigid states of one kind (Lepidopteran), not kinds.
- **Backbone taxonomy**: once checked, the rigid properties form a backbone that every instance falls under; roles and phases hang off it.
- For us: a cheap check on every broader/narrower link: is the parent a role, a phase or a "can be"? Note the direct hit on our domain: in OntoClean "agent" is a **role** (anything that acts). If Jonathan's vocabulary uses "agent" as a kind (a configured LLM program), the glossary must say so explicitly, and "acting as reviewer" stays a role either way.
