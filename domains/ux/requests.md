# Ux taxonomy: requests

**In one line**: every request for a term, a clarification or a change that reached this
domain, with its outcome, so the asker can look the answer up.

**In plain words**: agents and people ask for a term, a clarification or a change by
filing a `term-request` issue in this repo ([form](https://github.com/jburnhams/taxonomies/issues/new?template=term-request.yml)).
`python3 tools/term.py intake --write` copies new issues in as `open` (ID `issue-<number>`);
whoever answers sets **Outcome** (`use`, `alias`, `candidate`, `clarified`, `changed`,
`backlog` or `declined`, with the term ID) and **Answered** (date, by), logs any operation
in [`changelog.md`](./changelog.md), comments the outcome on the issue with a link to the
PR and closes it. A `backlog` record gains **Taken** (date, term ID) when a stage defines
its term, and that stage comments the term on the issue. Rules:
[`design/growth.md`](../../design/growth.md). `term.py lookup` and `changes` show these
answers back to the asker. Nothing here is deleted.

## Requests

None yet.
