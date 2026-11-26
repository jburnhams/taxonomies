# What's in a name? A study of identifiers

- **Source**: Dawn Lawrie, Christopher Morrell, Henry Feild, David Binkley, "What's in a name? A study of identifiers", ICPC 2006.
- **Type**: Conference paper
- **Access**: paywalled
- **URL**: none found
- **Read**: Read 2026-11-25: abstract and results of the stored 2007 journal version (the extended ICPC 2006 study).
- **Stored here**: [`lawrie-2007-effective-identifier-names.pdf`](https://github.com/jburnhams/taxonomies-sources/blob/main/lawrie-2006-whats-in-a-name/lawrie-2007-effective-identifier-names.pdf) (+ `.md`): "Effective identifier names for comprehension and memory", *Innovations in Systems and Software Engineering* 3, 2007, the extended journal version of the ICPC 2006 paper by the same authors, from a Kent State course page. The ICPC 2006 paper itself is not stored. Downloaded 2026-11-25; notes checked against it the same day. `.md` beside a file is its text, extracted for searching.
- **To fetch**: The ICPC 2006 paper, only if the journal version's figures differ from what the notes cite.
- **Used in**: [`06-shared-language-in-software.md`](../../06-shared-language-in-software.md)

## What is distinctive

Experiment on identifier forms: full words vs abbreviations vs single letters.

## Notes

Checked 2026-11-25 against the stored 2007 journal version ("Effective identifier names for comprehension and memory", *ISSE* 3), which extends the ICPC 2006 study; the 2006 paper itself is not stored.

- **Design**: over 100 programmers described twelve functions (textbook algorithms and production code) and then recalled identifiers from each; identifiers came in three levels: single letters, abbreviations, full words.
- **Result** (abstract): "full-word identifiers lead to the best comprehension; however, in many cases, there is no statistical difference between using full words and abbreviations." And on memory: "well chosen abbreviations may be preferable in some situations since identifiers with fewer syllables are easier to remember."
- **Tension with Hofmeister et al. 2017**: Hofmeister found abbreviations no better than single letters and only full words faster; Lawrie found abbreviations often as good as words for comprehension, and better for recall. Different tasks (finding defects vs describing a function and recalling names) and populations. Both agree full words never lose on comprehension, and single letters are worst.
- For us: "full words" stays the default for preferred labels, but a well-known abbreviation is a reasonable *alias* and, where it is what everyone says, can be preferred (as Z39.19 §6.6.3 allows).
