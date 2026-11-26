# Shorter identifier names take longer to comprehend

- **Source**: Johannes Hofmeister, Janet Siegmund, Daniel V. Holt, "Shorter identifier names take longer to comprehend", SANER 2017.
- **Type**: Conference paper
- **Access**: paywalled (author copies may exist)
- **URL**: none found
- **Read**: Read 2026-11-25 from the stored PDF: abstract, design and results.
- **Stored** (private, in [`taxonomies-sources/hofmeister-2017-shorter-names/`](https://github.com/jburnhams/taxonomies-sources/tree/main/hofmeister-2017-shorter-names)): `hofmeister-2017-shorter-names.pdf` (+ `.md`): the SANER 2017 paper, author copy from Saarland University (se.cs.uni-saarland.de). An extended version appeared in *Empirical Software Engineering* 24, 2019 (doi 10.1007/s10664-018-9621-x), not stored. Downloaded 2026-11-25; notes checked against it the same day. `.md` beside a file is its text, extracted for searching.
- **To fetch**: Nothing needed: the paper is stored in `taxonomies-sources`.
- **Used in**: [`06-shared-language-in-software.md`](../../06-shared-language-in-software.md)

## What is distinctive

Measured cost of abbreviations: readers found defects faster with word names than with letters or abbreviations.

## Notes

Checked against the stored SANER 2017 paper 2026-11-25.

- **Design**: 72 professional C# developers each found and corrected defects in six code snippets (three semantic defects, three syntax errors), with identifiers shown as single **letters**, **abbreviations** or full **words**; time to find the defect was measured.
- **Result** (abstract): "words lead to, on average, 19% faster comprehension speed compared to letters and abbreviations, but we did not find a significant difference in speed between letters and abbreviations." The effect is on finding **semantic** defects; finding syntax errors was unaffected by naming style (§VI).
- So abbreviations bought nothing over single letters here: only full words helped. The first pass said "roughly a fifth faster"; the exact figure is 19%.
- An extended version is in *Empirical Software Engineering* 24, 2019 (not stored).
- Supports "full words, no abbreviations" in a vocabulary's preferred labels.
