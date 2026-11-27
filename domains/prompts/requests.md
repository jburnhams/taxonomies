# Prompts taxonomy: requests

**In one line**: every request for a term, a clarification or a change that reached this
domain, with its outcome, so the asker can look the answer up.

**In plain words**: agents and people writing in the domain repo (`jburnhams/prompts`, file `term-requests.md`) ask
here when no term fits or a term is unclear or wrong. `python3 tools/term.py intake --write`
copies new requests in as `open`; whoever answers sets **Outcome** (`use`, `alias`,
`candidate`, `clarified`, `changed` or `declined`, with the term ID) and **Answered**
(date, by), and logs any operation in [`changelog.md`](./changelog.md). Rules:
[`design/growth.md`](../../design/growth.md) (proposed). `term.py lookup` and `changes`
show these answers back to the asker. Nothing here is deleted.

## Requests

None yet.
