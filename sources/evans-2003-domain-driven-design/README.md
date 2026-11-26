# Domain-Driven Design: Tackling Complexity in the Heart of Software

- **Source**: Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software* (Addison-Wesley, 2003); and *Domain-Driven Design Reference* (2015, CC BY 4.0).
- **Type**: Book + free reference
- **Access**: book paywalled; Reference open (CC BY 4.0)
- **URL**: https://domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf
- **Read**: Reference read in part 2026-11-25; book not read this pass.
- **Stored here**: `evans-2015-ddd-reference.pdf` (+ `.md`): *Domain-Driven Design Reference* (2015, CC BY 4.0) from domainlanguage.com. The 2003 book is not stored. Downloaded 2026-11-25; quoted lines checked against it the same day. `.md` beside a file is its text, extracted for searching.
- **To fetch**: The 2003 book (optional; the Reference covers the patterns).
- **Used in**: [`06-shared-language-in-software.md`](../../06-shared-language-in-software.md), [`07-limits-and-politics.md`](../../07-limits-and-politics.md)

## What is distinctive

Software's answer to naming: one language shared by experts and code, bounded to a context, with explicit maps between contexts.

## Notes

- **Ubiquitous Language**: "Use the model as the backbone of a language." The team uses the same words in talk, documents and code; "Recognize that a change in the language is a change to the model."
- **Bounded Context**: "Explicitly define the context within which a model applies." The same word may mean different things in different contexts; that is allowed, as long as the boundary is explicit. Inside a context, one meaning per word.
- **Context Map** relationships between contexts (names from the Reference's contents): Partnership, Shared Kernel, Customer/Supplier Development, Conformist, Anticorruption Layer, Open-host Service, Published Language, Separate Ways, Big Ball of Mud.
- For us: the strongest argument against one global taxonomy for all of Jonathan's projects. One vocabulary per domain (prompts, UX, ...), plus a small **shared kernel** of cross-domain terms and an explicit map.
