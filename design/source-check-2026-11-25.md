# What the stored sources change in the design (proposal)

**In one line**: reading the stored copies confirmed the design's rules and suggests
nine small additions. None is adopted; each is Jonathan's call.

On 2026-11-25, 32 sources were downloaded and the notes for most of them were checked
against the text (see [`changelog.md`](../changelog.md)). Most first-pass claims held.
The corrections that matter are in the source notes and topic docs. This page lists only
what would change [`README.md`](./README.md), by rule number.

## Confirmed as written

- **S2, S3, facets** (Kwasnik pp. 39-42; Denton §1): facets are for three or more
  independent dimensions, and they do not need a complete theory of the domain.
- **S4, roles never parents of kinds** (OntoClean, read in full): "antirigid properties
  cannot subsume rigid properties".
- **S6, no permanent "other"**: Kwasnik gives the same test for a hierarchy built too
  early ("The sure sign of a 'premature' hierarchical structure is the need for a
  'miscellaneous' or 'other' category", p. 29). Denton and Vickery say that when too
  many items land in "Other", you need a new facet. Add both as citations.
- **N1, one concept one name** (Deissenboeck and Pizka, read): consistency means
  names map to concepts one-to-one, with no homonyms and no synonyms.
- **N4, singular**: no conflict with Z39.19 after all. §6.5.1.1 allows singular where a
  field's own usage is singular. Open question 2 can be closed as "singular".
- **D1, genus-differentia** (Seppälä et al., OBO Foundry and WordNet all use it).

## Suggested additions

1. **Test the facet list before building on it** (Round 1, after step 5). Kwasnik: "it
   is not a simple matter to add fundamental facets once the general classification is
   established" (p. 41). Proposal: before writing any term entries, classify 10 items
   with the bare facet list, and add or drop facets then, while it is cheap.
2. **Find facets by constant comparison** (Round 1, step 5). Star 1998: compare unlike
   items to find the dimensions they share. For example: "how is a review prompt like a
   UI tell?" This gives step 5 a concrete method alongside Vickery's checklist.
3. **N7. Reticence**: no evaluative words in names ("legacy", "hacky", "minor", "bad").
   This is Ranganathan's 1937 Canon of Reticence: terms should be "purely descriptive
   and not opinionative".
4. **N4 amendment, abbreviations as aliases**: full words stay preferred, and every
   well-known abbreviation becomes an alias. Hofmeister: full words 19% faster.
   Lawrie: abbreviations often as good, and easier to remember. Z39.19 §6.6.3: prefer
   the abbreviation only when the full form is rarely used.
5. **D6. Owner** (or C-rule): each glossary, or each facet, names the person whose
   definition settles disputes; for now that is Jonathan. Two sources point this way.
   Medin and Ortony: people defer to "experts, who really know what makes the thing
   the thing that it is". Ranganathan's Canon of Currency asks for "some arrangement
   by which the terms can be changed over to current ones".
6. **Define "agent" first.** OntoClean's own worked example treats *Agent* as a role
   (anything that acts) and shows the error of placing it above kinds. The prompts
   repo uses "agent" as a kind of program. The first glossary should define which
   sense it means, and treat "acting as reviewer" and similar as roles either way.
7. **C3 amendment, prefer `closeMatch`.** SKOS makes `exactMatch` transitive (the
   only transitive mapping). A chain of `exactMatch` links across three repos would
   assert that the first and last terms are interchangeable. Use `exactMatch` only for
   real identity.
8. **S1 amendment, say whose purpose.** Hjørland: a classification "can never be
   neutral". The scope file names the readers it serves, and so whose interests win
   when the readers disagree (Jonathan's first, then the agents').
9. **Keep the procedure light and inside real work.** Two warnings from Alexander
   point the same way. In the 1971 preface to *Notes on the Synthesis of Form*, he
   disowned his own formal method because readers "made a cult of following" it.
   Gabriel reports that Alexander judged *A Pattern Language* had failed to change
   what got built, because the process mattered more than the catalogue. Proposal:
   run the build rounds only when a domain is being worked in, and judge the result
   by the "after" check (new synonyms, `unsorted` items in use), not by the glossary
   itself.

## Not changed by this pass

- The kappa target (0.7) and the card-sort figures still rest on sources that are not
  stored: Cohen 1960, Landis and Koch 1977, and Tullis and Wood 2004. Nickerson's
  ending conditions also still come from prior knowledge, because the Augsburg
  postprint could not be downloaded here. See [`to-fetch.md`](../to-fetch.md).
