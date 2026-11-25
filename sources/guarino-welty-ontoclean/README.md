# An Overview of OntoClean

- **Source**: Nicola Guarino and Christopher Welty, "An Overview of OntoClean", in Staab and Studer (eds.), *Handbook on Ontologies* (Springer, 2004; 2nd ed. 2009). Also "Evaluating ontological decisions with OntoClean", *CACM* 45(2), 2002.
- **Type**: Book chapter
- **Access**: free author copy
- **URL**: https://www.loa.istc.cnr.it/wp-content/uploads/2020/03/OverviewOntoClean-compresso.pdf
- **Read**: Read in part 2026-11-25: the first half or so verbatim; the rest only as a summary, so claims from it are marked.
- **Stored here**: Nothing yet. This cloud container's network policy blocks the publisher's site, so no copy could be downloaded. Drop a PDF here (for example `guarino-welty-ontoclean.pdf`) and note it in this line.
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
