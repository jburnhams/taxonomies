# Clio: Privacy-Preserving Insights into Real-World AI Use

- **Source**: Alex Tamkin et al., "Clio: Privacy-Preserving Insights into Real-World AI Use" (Anthropic; arXiv 2412.13678, 2024).
- **Type**: Preprint
- **Access**: open
- **URL**: https://arxiv.org/abs/2412.13678v1
- **Read**: Not read this pass. The notes are from prior knowledge of a well-known work and need checking against the text.
- **Stored here**: Nothing yet. This cloud container's network policy blocks the publisher's site, so no copy could be downloaded. Drop a PDF here (for example `tamkin-2024-clio.pdf`) and note it in this line.
- **To fetch**: Nothing needed: what the notes rely on was readable online.
- **Used in**: [`05-building-and-testing.md`](../../05-building-and-testing.md)

## What is distinctive

Bottom-up hierarchical clustering of conversations with LLM-written cluster names.

## Notes

- Extract facets per conversation, embed, cluster, have a model name each cluster, then build a hierarchy of clusters.
- Shows the numerical-taxonomy approach (Sokal and Sneath) done with LLMs. Good for discovering categories; the names it produces still need the naming rules applied.
