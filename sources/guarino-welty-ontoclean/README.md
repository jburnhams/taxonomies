# An Overview of OntoClean

- **Source**: Nicola Guarino and Christopher Welty, "An Overview of OntoClean", in Staab and Studer (eds.), *Handbook on Ontologies* (Springer, 2004; 2nd ed. 2009). Also "Evaluating ontological decisions with OntoClean", *CACM* 45(2), 2002.
- **Type**: Book chapter
- **Access**: free author copy
- **URL**: https://www.loa.istc.cnr.it/wp-content/uploads/2020/03/OverviewOntoClean-compresso.pdf
- **Read**: Read in part 2026-11-25: the first half or so verbatim; the rest only as a summary, so claims from it are marked.
- **Stored here**: `guarino-welty-2004-overview-of-ontoclean.pdf` (+ `.md`): the *Handbook on Ontologies* chapter, author copy from ISTC-CNR. The 2002 CACM article is not stored. Downloaded 2026-11-25; the notes below were written before this copy was stored and have not yet been re-checked against it. `.md` beside a file is its text, extracted for searching.
- **To fetch**: Nothing needed: what the notes rely on was readable online.
- **Used in**: [`04-vocabularies-and-ontologies.md`](../../04-vocabularies-and-ontologies.md)

## What is distinctive

A test for whether an is-a link is valid, using properties of the concepts themselves.

## Notes

- **Rigidity**: a property is rigid (+R) if "essential to all its possible instances" (Person); anti-rigid (~R) if an instance can stop having it (Student); semi-rigid otherwise.
- **Identity** (+I, +O): whether the property carries (or supplies) a criterion for telling instances apart.
- **Unity** (+U, -U, ~U): whether instances are wholes, and by what criterion.
- **Dependence** (+D): whether an instance needs something else to exist.
- The key constraint: "If q is anti-rigid, then p must be anti-rigid" where q subsumes p. So **Student cannot be the parent of Person**. Role words (reviewer, orchestrator, owner) must not be parents of kind words (agent, model, file).
- For us: a cheap check on every broader/narrower link: is the parent a role and the child a kind?
