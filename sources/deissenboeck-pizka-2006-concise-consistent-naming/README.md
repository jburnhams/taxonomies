# Concise and consistent naming

- **Source**: Florian Deissenboeck and Markus Pizka, "Concise and consistent naming", *Software Quality Journal* 14(3), 2006, 261-282.
- **Type**: Journal article
- **Access**: paywalled
- **URL**: none found
- **Read**: Read 2026-11-25 from the stored journal PDF: sections 1-4 closely, sections 5-6 skimmed.
- **Stored** (private, in [`taxonomies-sources/deissenboeck-pizka-2006-concise-consistent-naming/`](https://github.com/jburnhams/taxonomies-sources/tree/main/deissenboeck-pizka-2006-concise-consistent-naming)): `deissenboeck-pizka-2006-sqj.pdf` (+ `.md`): the 2006 *Software Quality Journal* article, publisher layout, from itestra.com; `deissenboeck-pizka-2005-iwpc.pdf` (+ `.md`): the earlier IWPC 2005 conference version, from TU München. Downloaded 2026-11-25; notes checked against it the same day. `.md` beside a file is its text, extracted for searching.
- **To fetch**: Nothing needed: the journal article is stored in `taxonomies-sources`.
- **Used in**: [`03-naming.md`](../../03-naming.md), [`06-shared-language-in-software.md`](../../06-shared-language-in-software.md)

## What is distinctive

A formal model of good identifier naming: names and concepts should map one to one.

## Notes

Checked against the stored journal text 2026-11-25; page numbers are *Software Quality Journal* 14.

- **The model**: a set of concepts C, a set of names N, and the naming relation R ⊆ N × C.
- **Rule 1, consistency** (pp. 267-268): no **homonyms** (one name, several concepts: `file` for handles and filenames) and no **synonyms** (several names, one concept: `accountNumber` and `number`). Formally, R must be a bijection. Synonyms alone are a nuisance (more to learn, harder to search); mixed with homonyms "the mixture ... maximizes confusion".
- **Rule 2, correctness then conciseness** (pp. 268-269): an identifier is *correct* if it is the name of its concept or of a generalisation of it (`transformation` for a permutation); it is *concise* only if it is exactly the concept's name (`permutation`). So a vague-but-true name is correct and not concise.
- **The catch they name**: conciseness is defined relative to the concept set C. Put every conceivable concept in C and names grow absurd ("completePermutationByCascadedRecursion"); so C has to be chosen deliberately, i.e. naming quality depends on an agreed set of concepts.
- **Evidence**: about 70% of Eclipse's source characters are identifiers, with 142,275 distinct identifier names in Eclipse 3.1.1 (pp. 263, 274-275); the experiences section shows real synonym and homonym cases.
- **Tool**: an identifier dictionary (name, concept, type, description), built incrementally and used to propose names. This is a controlled vocabulary for code, and the same rule SKOS states as one preferred label per language.
- For us: their result strengthens the "glossary before names" order. A name can only be judged concise against an agreed concept list, which is the glossary.
