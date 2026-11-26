# Design Patterns: Elements of Reusable Object-Oriented Software

- **Source**: Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software* (Addison-Wesley, 1994); and Kent Beck and Ward Cunningham, "Using Pattern Languages for Object-Oriented Programs", OOPSLA 1987 workshop.
- **Type**: Book + workshop paper
- **Access**: book paywalled; Beck and Cunningham's paper free online
- **URL**: none found
- **Read**: Not read this pass. The notes are from prior knowledge of a well-known work and need checking against the text.
- **Stored** (private, in [`taxonomies-sources/gamma-1994-design-patterns/`](https://github.com/jburnhams/taxonomies-sources/tree/main/gamma-1994-design-patterns)): `beck-cunningham-1987-oopsla.html` (+ `.md`): Beck and Cunningham's OOPSLA-87 paper from c2.com. The Gamma et al. book is not stored. Downloaded 2026-11-25; the Beck and Cunningham point was checked against it the same day. `.md` beside a file is its text, extracted for searching.
- **To fetch**: The book (optional; Beck and Cunningham is stored).
- **Used in**: [`08-pattern-languages.md`](../../08-pattern-languages.md)

## What is distinctive

How Alexander's idea reached software: 23 named patterns, and a catalogue sorted by two facets.

## Notes

- Beck and Cunningham (1987) tried Alexander's approach on user-interface design; the GoF book (1994) made patterns mainstream. Checked against the stored OOPSLA-87 paper 2026-11-25: their reason was Alexander's, that occupants should design their own buildings, so "Computer users should write their own programs". Their five-pattern language for Smalltalk windows was Window Per Task, Few Panes Per Window, Standard Panes, Short Menus, Nouns and Verbs, and it was given to application specialists (not programmers) to write a specification. They also note that patterns "connect to other patterns where decisions made in one influence the others" and that Alexander showed such a language can be ordered "without cycles", so design proceeds without reversing earlier decisions. The GoF points below are from prior knowledge (book not stored).
- The 23 patterns are classified on two axes: **purpose** (creational, structural, behavioural) and **scope** (class, object). A paradigm/facet grid, not a tree.
- The book's real legacy is the names (Factory, Observer, Adapter) as shared vocabulary. Its form (intent, motivation, applicability, structure, consequences, related patterns) is more rigid than Alexander's.
- Software patterns mostly lost Alexander's *language* (the links that let patterns compose); they became catalogues.
