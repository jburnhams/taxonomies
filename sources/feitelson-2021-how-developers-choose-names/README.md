# How Developers Choose Names

- **Source**: Dror G. Feitelson, Ayelet Mizrahi, Nofar Noy, Aviad Ben Shabat, Or Eliyahu, Roy Sheffer, "How Developers Choose Names", *IEEE Transactions on Software Engineering* (2020 online; doi 10.1109/TSE.2020.2976920). Follow-up: Alpern et al., "Reproducing, Extending, and Analyzing Naming Experiments" (arXiv 2402.10022, 2024).
- **Type**: Journal article + replication
- **Access**: open preprints on arXiv
- **URL**: https://arxiv.org/abs/2103.07487 ; https://arxiv.org/abs/2402.10022
- **Read**: Read 2026-11-25 (online copy, see URL). (PDF partly; key figures read verbatim)
- **Stored here**: `feitelson-2021-how-developers-choose-names.pdf` (+ `.md`): arXiv 2103.07487v1; `alpern-2024-reproducing-naming-experiments.pdf` (+ `.md`): arXiv 2402.10022v1. Downloaded 2026-11-25; the notes below were written before this copy was stored and have not yet been re-checked against it. `.md` beside a file is its text, extracted for searching.
- **To fetch**: Nothing needed: both preprints are stored here.
- **Used in**: [`03-naming.md`](../../03-naming.md), [`06-shared-language-in-software.md`](../../06-shared-language-in-software.md)

## What is distinctive

Furnas's finding, repeated for code: developers almost never pick the same name, but a simple naming procedure makes names better.

## Notes

- The median probability that two developers choose the same name for the same variable or function was **6.9%** (47 naming tasks; per-task range 2.5% to 64.6%).
- Names chosen by others were generally understood, but this "may hide different assumptions" that lead to bugs.
- **Three-step model of naming**: (1) choose the concepts to include, (2) choose a word for each concept, (3) build the name from the words. Developers taught the model produced names judged better "by a ratio of two-to-one".
- The 2024 replication confirms the low agreement and that using the model helps (asking for longer names does not). It classifies name concepts as universal (everyone includes it), alternative, or optional.
- Unresolved: the paper's abstract says 334 subjects, the body 234 respondents.
- For us: agreement on names has to be manufactured, not expected. The three steps are a good template for naming a term: decide the concepts first, then the words.
