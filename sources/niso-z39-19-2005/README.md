# Guidelines for the Construction, Format, and Management of Monolingual Controlled Vocabularies

- **Source**: ANSI/NISO Z39.19-2005 (R2010), *Guidelines for the Construction, Format, and Management of Monolingual Controlled Vocabularies* (NISO).
- **Type**: Standard
- **Access**: free download from NISO
- **URL**: https://niso.org/publications/ansiniso-z3919-2005-r2010
- **Read**: Read in part 2026-11-25 from the stored PDF: sections 5.3-6.6 and 8.1-8.4 (term choice, form and relationships); the display, interoperability and management sections not read.
- **Stored here**: `ansi-niso-z39-19-2005-r2010.pdf` (+ `.md`): the full standard, free download from NISO. Downloaded 2026-11-25; notes checked against it the same day. `.md` beside a file is its text, extracted for searching.
- **To fetch**: Nothing needed: the standard is stored here.
- **Used in**: [`04-vocabularies-and-ontologies.md`](../../04-vocabularies-and-ontologies.md), [`03-naming.md`](../../03-naming.md)

## What is distinctive

The US standard for lists, synonym rings, taxonomies and thesauri: how to choose terms and relate them.

## Notes

Checked against the stored text 2026-11-25; section numbers are the standard's.

- **Four types** in increasing structure (§5.4, Figure 5): **list** (ambiguity control), **synonym ring** (+ synonym control), **taxonomy** (+ hierarchical relationships), **thesaurus** (+ associative relationships). Each includes the simpler ones. A synonym ring is a special case: it groups equivalents for search expansion and "cannot be used during" indexing (§5.4.2).
- **Warrant** (§5.3.5): terms are chosen from "the natural language used to describe content objects (literary warrant), the language of users (user warrant), and the needs and priorities of the organization (organizational warrant)".
- **Single concept** (§6.3): "Each term included in a controlled vocabulary should represent a single concept (or unit of thought)."
- **Scope notes** (§6.2.2) restrict or expand a term, "distinguish between terms that have overlapping meanings in natural language", and should "state the chosen meaning of a term", optionally naming meanings deliberately excluded.
- **Grammar** (§6.4): nouns and noun phrases; activities as nouns or gerunds ("catalysis rather than catalyze"); adjectival (premodified) noun phrases preferred.
- **Singular and plural** (§6.5): count nouns "should normally be expressed as plurals"; mass nouns and abstract concepts singular. **But** §6.5.1.1 allows singular count nouns where literary or user warrant favours it (body parts in biomedicine, unique objects in a museum catalogue). So the singular convention of ontology practice is an allowed exception, not a clash.
- **Abbreviations** (§6.6.3): use the abbreviation only when "so well established that the full form ... is rarely used" (AIDS, DNA, lasers); otherwise the full form, with a cross-reference from the abbreviation ("automated teller machines rather than ATMs").
- **Relationships** (§8): equivalence (USE / UF), hierarchical with three kinds marked BTG/NTG generic ("[narrower term] is a [broader term]", with an all-and-some test), BTI/NTI instance, BTP/NTP whole-part, and associative (RT).
