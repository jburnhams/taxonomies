# TnT-LLM: Text Mining at Scale with Large Language Models

- **Source**: Mengting Wan et al., "TnT-LLM: Text Mining at Scale with Large Language Models" (Microsoft; arXiv 2403.12173, 2024).
- **Type**: Preprint
- **Access**: open (CC BY-NC-ND 4.0)
- **URL**: https://arxiv.org/abs/2403.12173v1
- **Read**: Not read this pass. The notes are from prior knowledge of a well-known work and need checking against the text.
- **Stored here**: `wan-2024-tnt-llm.pdf` (+ `.md`): arXiv 2403.12173v1 (CC BY-NC-ND 4.0). Downloaded 2026-11-25; the notes below were written before this copy was stored and have not yet been re-checked against it. `.md` beside a file is its text, extracted for searching.
- **To fetch**: Nothing needed: the paper is stored here.
- **Used in**: [`05-building-and-testing.md`](../../05-building-and-testing.md)

## What is distinctive

Using an LLM to propose a label taxonomy from a corpus, then to label at scale.

## Notes

- Phase 1: the LLM reads batches of texts and iteratively proposes, refines and summarises a label taxonomy (with human review). Phase 2: the LLM labels a sample, which trains a cheap classifier for scale.
- Evaluated against human raters on Bing chat logs.
- For us: a way to run Nickerson's empirical-to-conceptual step on a pile of files (prompts, UI tells), as long as a person decides the names.
