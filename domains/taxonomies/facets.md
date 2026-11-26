# Taxonomies taxonomy: facets

**In one line**: two sorting questions for every concept the method uses: what sort of
thing it is, and in which stage of the method it comes up.

**In plain words**: the first question is the one the spec already asks of every term
(its Kind field), so the method's own four kinds become this domain's first facet. The
second follows the process's own order: frame, build, test, govern.

**Status**: draft, 2026-11-26, proposed with the domain; not chosen by Jonathan and not
tested. Every value has a `candidate` glossary entry.

## How these were found

- **Reused what exists** (step 0): spec rule S4 already sorts every term by kind
  (thing, property, role, happening), and process.md already groups its thirteen steps.
- **Checked against general categories** (OBO Foundry Table 1): `kind` is the
  continuant/occurrent split itself; `stage` is about a process (when).
- **Independence**: things occur in every stage (`scope` files in framing, `sample` in
  building, `round` folders in testing, `changelog` in governing), and so do happenings
  (harvest, agreement test, operation), so the two questions vary apart.

## Proposed: kind, stage

### Kind (`kind`)

- **Question**: What sort of thing is the concept?
- **Principle**: whether it exists on its own, is had by something, is played by something, or takes place.
- **Kind**: property
- **Values**: `thing`, `property`, `role`, `happening`
- **Order**: as spec S4 lists them.
- **Unsorted**: none yet.
- **Agreement**: not tested.

### Stage (`stage`)

- **Question**: In which stage of the method does the concept first come up?
- **Principle**: the first process step that produces or uses it.
- **Kind**: happening
- **Values**: `framing`, `building`, `testing`, `governing`
- **Order**: the order of the process steps.
- **Unsorted**: none yet.
- **Agreement**: not tested.
