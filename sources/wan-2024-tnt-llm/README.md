# TnT-LLM: Text Mining at Scale with Large Language Models

- **Source**: Mengting Wan et al., "TnT-LLM: Text Mining at Scale with Large Language Models" (Microsoft; arXiv 2403.12173, 2024).
- **Type**: Preprint
- **Access**: open (CC BY-NC-ND 4.0)
- **URL**: https://arxiv.org/abs/2403.12173v1
- **Read**: Read in part 2026-11-25 from the stored PDF: abstract, introduction and the method section; experiments skimmed.
- **Stored here**: `wan-2024-tnt-llm.pdf` (+ `.md`): arXiv 2403.12173v1 (CC BY-NC-ND 4.0). Downloaded 2026-11-25; notes checked against it the same day. `.md` beside a file is its text, extracted for searching.
- **To fetch**: Nothing needed: the paper is stored here.
- **Used in**: [`05-building-and-testing.md`](../../05-building-and-testing.md)

## What is distinctive

Using an LLM to propose a label taxonomy from a corpus, then to label at scale.

## Notes

Checked against the stored paper 2026-11-25 (abstract and §3).

- **Phase 1, taxonomy generation**: Stage 1 has the LLM **summarise** each text, to normalise them. Stage 2 splits the summaries into minibatches ("Similar to SGD") and runs three zero-shot prompts: an **initial generation** prompt on the first batch; an **update** prompt on each later batch that (1) evaluates the taxonomy on the new data, (2) identifies issues and suggestions, (3) modifies the taxonomy; and a final **review** prompt that checks format and quality. Every prompt carries a **use-case instruction** giving the goal and format (number of labels, words per label). Rerunning Stage 2 inside each category adds levels.
- **Phase 2, classification**: the LLM labels a sample, which trains lightweight classifiers to label at scale; these perform comparably to or better than using the LLM as the classifier, at far lower cost.
- **Evaluation**: on Bing Copilot conversations (user intent and conversational domain), with human and automatic metrics, against baselines.
- **Correction**: the first pass said phase 1 runs "with human review". The review step is an LLM prompt; humans appear in the evaluation, not in the loop.
- For us: a way to run Nickerson's empirical-to-conceptual step on a pile of files (prompts, UI tells). The use-case instruction is the meta-characteristic written as a prompt. Since the loop has no human in it by design, our method has to add one: a person decides the names.
