# Clio: Privacy-Preserving Insights into Real-World AI Use

- **Source**: Alex Tamkin et al., "Clio: Privacy-Preserving Insights into Real-World AI Use" (Anthropic; arXiv 2412.13678, 2024).
- **Type**: Preprint
- **Access**: open
- **URL**: https://arxiv.org/abs/2412.13678v1
- **Read**: Not read this pass. The notes are from prior knowledge of a well-known work and need checking against the text.
- **Stored here**: `tamkin-2024-clio.pdf` (+ `.md`): arXiv 2412.13678v1. Downloaded 2026-11-25; the notes below were written before this copy was stored and have not yet been re-checked against it. `.md` beside a file is its text, extracted for searching.
- **To fetch**: Nothing needed: the paper is stored here.
- **Used in**: [`05-building-and-testing.md`](../../05-building-and-testing.md)

## What is distinctive

Bottom-up hierarchical clustering of conversations with LLM-written cluster names.

## Notes

- Extract facets per conversation, embed, cluster, have a model name each cluster, then build a hierarchy of clusters.
- Shows the numerical-taxonomy approach (Sokal and Sneath) done with LLMs. Good for discovering categories; the names it produces still need the naming rules applied.
