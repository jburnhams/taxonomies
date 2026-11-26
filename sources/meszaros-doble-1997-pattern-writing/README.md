# A Pattern Language for Pattern Writing

- **Source**: Gerard Meszaros and Jim Doble, "A Pattern Language for Pattern Writing", in *Pattern Languages of Program Design 3* (Addison-Wesley, 1997).
- **Type**: Book chapter (PLoP)
- **Access**: free on hillside.net (robots block automated fetching)
- **URL**: https://hillside.net/index.php/a-pattern-language-for-pattern-writing
- **Read**: Read 2026-11-25 from the stored PDF: the pattern list, Mandatory Elements Present, Optional Elements When Helpful and the naming patterns; other patterns skimmed.
- **Stored** (private, in [`taxonomies-sources/meszaros-doble-1997-pattern-writing/`](https://github.com/jburnhams/taxonomies-sources/tree/main/meszaros-doble-1997-pattern-writing)): `meszaros-doble-1997-pattern-writing.pdf` (+ `.md`): the full pattern language, from patternwritingpatterns.gerardmeszaros.com (the authors' copy). Downloaded 2026-11-25; notes checked against it the same day. `.md` beside a file is its text, extracted for searching.
- **To fetch**: Nothing needed: the paper is stored in `taxonomies-sources`.
- **Used in**: [`08-pattern-languages.md`](../../08-pattern-languages.md)

## What is distinctive

Patterns about how to write patterns, including how to name them.

## Notes

Checked against the stored text 2026-11-25 (the authors' 2005 web version of the PLoPD3 chapter).

- **Mandatory Elements Present**: **name, context, problem, forces, solution**. Names and order may vary by style; all five must be there. "There is no single correct style or template for patterns."
- **Optional Elements When Helpful**: indications (symptoms of the problem), resulting context, related patterns, examples, code samples, rationale, aliases, acknowledgments.
- **Naming patterns** (all three confirmed):
  - **Evocative Pattern Name**: "Choose a pattern name that is likely to conjure up images that convey the essence of the pattern solution to the target audience." Test it by having people who have not read the pattern guess what it is about from the name alone.
  - **Noun Phrase Name**: "Name the pattern after the result it creates." Names describing the problem are not unique (several solutions may share a problem); names with verbs or prepositions are awkward in conversation ("we have an example of Create Objects for States").
  - **Meaningful Metaphor Name**: a familiar metaphor, when one fits.
- The language also includes structure patterns (Visible Forces, Single-Pass Readable, Skippable Sections, Findable Sections), language-level ones (Pattern Thumbnail, Problem/Solution Summary, Glossary, Distinctive Headings Convey Structure, Running Example) and audience ones (Clear Target Audience, Terminology Tailored to Audience, Understood Notations).
- It describes "the desired result", not a recipe; experts can use it as a checklist.
- For us: the template our pattern layer would use, plus two naming rules that agree with the ontology guidance: name the *result* as a noun phrase, and test a name by asking someone who has not seen the definition to guess what it means (a cheap version of the Furnas test).
