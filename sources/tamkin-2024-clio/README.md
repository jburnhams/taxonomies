# Clio: Privacy-Preserving Insights into Real-World AI Use

- **Source**: Alex Tamkin et al., "Clio: Privacy-Preserving Insights into Real-World AI Use" (Anthropic; arXiv 2412.13678, 2024).
- **Type**: Preprint
- **Access**: open
- **URL**: https://arxiv.org/abs/2412.13678v1
- **Read**: Read in part 2026-11-25 from the stored PDF: §1-2 (method and validation); the case studies and appendices not read.
- **Stored here**: `tamkin-2024-clio.pdf` (+ `.md`): arXiv 2412.13678v1. Downloaded 2026-11-25; notes checked against it the same day. `.md` beside a file is its text, extracted for searching.
- **To fetch**: Nothing needed: the paper is stored here.
- **Used in**: [`05-building-and-testing.md`](../../05-building-and-testing.md)

## What is distinctive

Bottom-up hierarchical clustering of conversations with LLM-written cluster names.

## Notes

Checked against the stored paper 2026-11-25 (§2).

- **Pipeline**: (1) **extract facets** per conversation, "specific attributes or characteristics such as the high-level conversation topic, number of conversational turns, or language used", some computed directly, some by a model; (2) **semantic clustering**: embed one natural-language facet (e.g. topic) and run k-means; (3) **describe clusters**: a model gives each cluster a title and summary from sample conversations; (4) **build a hierarchy** by recursively grouping base clusters into higher levels; plus a 2D map for exploration. Privacy layers sit between the steps.
- **Validation**: on 19,476 synthetic multilingual conversations with known topics, Clio "reconstructed the ground-truth distribution of topics ... with 94% accuracy".
- Note the word: Clio calls its extracted attributes "facets", in the same sense as Ranganathan's, and builds one hierarchy *per facet*.
- Shows the numerical-taxonomy approach (Sokal and Sneath) done with LLMs. Good for discovering categories at scale; the names it produces still need the naming rules applied, and the 94% is reconstruction of known categories, not a measure of whether the discovered ones are the right ones for a purpose.
