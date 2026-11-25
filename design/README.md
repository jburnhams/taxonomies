# Our design: a candidate system for agreeing a taxonomy up front

**Status**: proposal, 2026-11-25. Not adopted. Built from the topic docs
[1](../01-structures.md) to [8](../08-pattern-languages.md); each rule names its source.
Working name: none yet (pick one; see [open questions](#open-questions)).

## In one paragraph

For each domain, write down **what the taxonomy is for** and the questions it must
answer. Describe the domain with a few **facets** (independent questions, each with a
short closed list of values) rather than one big tree. Keep a **glossary** in which every
concept has one preferred name, its aliases, a one-sentence genus-differentia
definition, a scope note, a **type example** from the repo and a near miss. Build it in
rounds, alternating "group real things" with "test our categories on new things", and
stop when written ending conditions hold, the main one being that two independent raters
classify a sample the same way. Each repo is its own **bounded context** with its own
glossary; a small shared kernel and explicit mappings link them. For design domains,
add a **pattern layer** on top, written in Alexander's form, using only glossary terms.

## Why this and not something else

| Option | Verdict | Why |
|---|---|---|
| One big hierarchy | no | Real domains overlap (Alexander's semilattice, Bowker and Star); a tree claims more knowledge than a young domain has (Kwasnik). |
| One global taxonomy for all projects | no | Words mean different things in different contexts (Evans); universal schemes fail (Wilkins, Borges). |
| Free tags | no | People pick the same word under 20% of the time (Furnas), developers 6.9% (Feitelson); tags multiply synonyms. |
| Full OWL ontology | not now | Reasoning is the pay-off and our readers are people and LLMs reading markdown; SKOS-level structure gets most of the benefit and converts later. |
| Pattern language alone | no | Patterns name solutions, not things; they need a vocabulary to be written in. |
| **Facets + SKOS-style glossary + bounded contexts + tested method (+ patterns)** | **yes** | Each part is the established answer from its field, and they fit together. |

## The artefacts (per domain)

Each domain (bounded context) keeps these, in a `taxonomy/` folder of its own repo or
here under `domains/<name>/`:

1. **`scope.md`**: purpose (Nickerson's meta-characteristic), intended readers
   (Jonathan, agents, users), **competency questions** (Noy and McGuinness), what is out
   of scope, and the neighbouring contexts.
2. **`facets.md`**: the facets. For each: the question it answers, its principle of
   division, its values (mutually exclusive, jointly exhaustive), and how "does not fit
   yet" is handled.
3. **`glossary.md`**: one entry per concept (template in [`templates.md`](./templates.md)),
   SKOS fields in markdown.
4. **`map.md`**: links to other contexts' terms (`exactMatch`, `closeMatch`,
   `broadMatch`, `narrowMatch`, `relatedMatch`) and to the shared kernel.
5. **`patterns/`** (design domains only): one file per pattern in Alexander's form.
6. **`changelog.md`**: every change as a named operation, newest first.

## The rules

**Structure**

- **S1. Purpose first.** No facet or term without a stated purpose and competency
  questions to test it against. *(Nickerson's meta-characteristic; competency questions;
  Hjørland's pragmatism.)*
- **S2. Facets, not one tree.** Three to seven facets. A hierarchy is allowed inside a
  facet only where is-a holds strictly. *(Ranganathan, Kwasnik, Alexander 1965.)*
- **S3. One principle per facet**; values mutually exclusive and jointly exhaustive; each
  facet passes Spiteri's tests (differentiates, relevant, ascertainable, permanent,
  homogeneous). *(Spiteri, Nickerson.)*
- **S4. Do not mix kinds of term in a facet**: things, properties, roles and happenings go
  in separate facets. **Roles are never parents of kinds.** *(BFO continuant/occurrent;
  OntoClean rigidity.)*
- **S5. Shallow.** At most three levels in any facet; the busiest level has the shortest
  names. *(Berlin; Rosch.)*
- **S6. No permanent "other".** Each facet has an `unsorted` inbox that is reviewed
  every round; a full inbox means the facet is wrong. *(Bowker and Star's residual
  categories; Schober 2.5.)*

**Names**

- **N1. One concept, one preferred name; one name, one concept** inside the context.
  *(Deissenboeck and Pizka; SKOS S14; ICZN no homonyms.)*
- **N2. Harvest, then choose.** Collect the words already used (in the repo and in
  Jonathan's own words) before choosing; record every other one as an alias.
  *(Z39.19 warrant; Furnas's aliasing.)*
- **N3. Concepts before words.** Agree what the name must carry, then the words, then the
  name. *(Feitelson's three steps; Ranganathan's idea/verbal planes.)*
- **N4. Form**: noun or noun phrase; singular; full words; no "and/or", no negation, no
  catch-alls, no claims ("type of"), no dates or status, no level encoded in the name.
  *(Schober; Seppälä; PhyloCode; Wilkins as the warning.)*
- **N5. Basic level for the readers**: the word Jonathan and an agent would reach for
  first, not the most abstract. *(Rosch.)*
- **N6. Stability beats aptness.** An established name is kept unless it misleads; IDs
  never change or get reused; old names become aliases. *(Priority and types in the
  biology codes; SKOS hiddenLabel.)*

**Definitions**

- **D1. Genus-differentia**: "An X is a Y that Z", one nearest genus, no circularity, no
  "usually". *(Seppälä et al.)*
- **D2. Scope note**: what it includes and excludes, especially at the edges.
  *(Z39.19; Lakoff's radial categories.)*
- **D3. Type example**: a real item in the repo (a file, a section) that is the clearest
  case, and the term's anchor if the definition is later revised. *(Biology's types;
  Rosch's prototypes.)*
- **D4. Near miss**: one thing that looks like it but is not, and why. *(Murphy;
  Lakoff.)*
- **D5. Confidence**: `settled`, `working` or `tentative`. *(Alexander's asterisks.)*

**Contexts**

- **C1. One glossary per bounded context** (per repo at first). *(Evans.)*
- **C2. Shared kernel**: only terms that are truly the same everywhere, kept small and
  changed only by agreement. *(Evans; boundary objects.)*
- **C3. Explicit mappings** between contexts using SKOS match types; a word may mean
  different things in two contexts if the map says so. *(SKOS; ISO 25964-2.)*

**Change**

- **M1. Named operations only**: add, rename, split, merge, promote, demote, deprecate,
  each logged with the reason. Deprecate, never delete. *(Kundisch et al.)*
- **M2. A rename is a model change**: update the glossary, the aliases and the uses in
  the same commit. *(Evans.)*

## The procedure

**Round 0: frame** (an hour)

1. Write `scope.md`: purpose, readers, 5-15 competency questions, out of scope.
2. Write the ending conditions (below) with target values.

**Round 1: harvest (empirical to conceptual)**

3. Take a sample of real items: 30 to 60 files or sections, chosen to be varied.
4. List every term used for the things in them; group synonyms; count uses. A model can
   do the first pass (TnT-LLM style); Jonathan decides.
5. Draft facets from the groupings, checking against Vickery's 13 categories and BFO's
   thing/property/role/happening split for anything missed.

**Round 2: propose (conceptual to empirical)**

6. Name each facet value and term (N1-N6) and write its entry (D1-D5).
7. Classify a **fresh** sample of 20-30 items with the draft. Note every hesitation and
   every item in `unsorted`.
8. Fix: split, merge, rename, move. Log the operations.

**Round 3: test agreement**

9. Two raters classify the same 20-30 items independently using only the glossary and
   facets: Jonathan and a model session, or two fresh model sessions.
10. Compute Cohen's kappa per facet. Below target: rewrite that facet's definitions and
    scope notes, repeat from 7.

**Stop** when the ending conditions hold:

- Objective: every sampled item classified; no facet value empty; no term added, merged
  or split in the last round; `unsorted` empty or reviewed; **kappa at least 0.7 on
  every facet** (proposed target; substantial agreement); each competency question can
  be answered with the glossary.
- Subjective (Nickerson): concise, robust, comprehensive, extendible, explanatory.

**After**: evaluate in use (Kundisch's ex post): after a month of work in the domain,
count new synonyms that crept in, terms added, and items that went to `unsorted`.

A light version for a small domain: Round 0, then one combined round of steps 3-8 on
20 items, then step 9-10 with two model sessions.

## Pattern layer (design domains)

Where the domain is about making things (agent design, UI), patterns sit on top of the
glossary:

- One file per pattern: **name** (noun phrase, evocative, follows N4), **confidence**
  (D5), **context** (larger patterns it serves), **problem**, **forces**, **therefore**
  (solution), **smaller patterns**, **examples** (links into the repo), **sources**.
- Every domain word in a pattern is a glossary term.
- Patterns are classified by the domain's facets (like GoF's purpose x scope).
- Patterns link up and down; an unlinked pattern is a catalogue entry, not yet part of the
  language (Salingaros).

## Where agents fit

- The glossary is loaded into agents' context (linked from CLAUDE.md / AGENTS.md) so they
  use the preferred names and recognise aliases.
- Agents are raters in the kappa test and do the harvesting pass.
- A lint step can flag aliases used in place of preferred names in new docs.

## Open questions

These change the goal, so they are Jonathan's to decide:

1. **Where glossaries live**: in each domain repo (closest to use; recommended) or
   centrally here.
2. **Singular or plural** term names: OBO says singular, Z39.19 says plural for countable
   things but allows singular where the field's usage is singular (§6.5.1.1, checked
   2026-11-25), so singular breaks neither. Recommended: singular, because the names
   double as identifiers in code and prompts.
3. **Kappa target**: 0.7 proposed. Higher is stricter and slower.
4. **A name for the system itself.**
5. **Machine-readable copy**: markdown only (recommended for now), or also SKOS/YAML
   generated from it.

Templates: [`templates.md`](./templates.md). What applying it to the two existing repos
would start from: [`first-look.md`](./first-look.md). What reading the stored sources
suggests changing (nine proposals, none adopted):
[`source-check-2026-11-25.md`](./source-check-2026-11-25.md).
