import { useParams } from "react-router";
import { Breadcrumb, DataTable, PageHeader, Status, TextLink } from "strata-react";
import type { Column } from "strata-react";
import { useDomain, useIndexData, useLinks, useRaw, githubBlob, type Domain, type SourceEntry } from "../data";
import { Loaded, Prose } from "../parts";

function crumbsFor(path: string, title: string, domains: { id: string; title: string }[]) {
  const items: { label: string; to?: string }[] = [{ label: "Taxonomies", to: "/" }];
  const dm = path.match(/^domains\/([\w-]+)\//);
  if (dm) {
    const d = domains.find((x) => x.id === dm[1]);
    items.push({ label: d?.title ?? dm[1], to: `/d/${dm[1]}` });
    const rm = path.match(/^domains\/[\w-]+\/rounds\/([\w-]+)\//);
    if (rm) items.push({ label: rm[1], to: `/d/${dm[1]}/round/${rm[1]}` });
  } else if (path.startsWith("sources/")) items.push({ label: "Sources", to: "/sources" });
  else if (path.startsWith("design/")) items.push({ label: "Method", to: "/doc/design/README.md" });
  items.push({ label: title });
  return items;
}

/** Any Markdown file in the repo, fetched as text and rendered with its links resolved. */
export function DocPage() {
  const path = useParams()["*"] ?? "";
  const dm = path.match(/^domains\/([\w-]+)\//);
  return dm ? <DomainDoc path={path} domain={dm[1]} /> : <Doc path={path} />;
}

function DomainDoc({ path, domain }: { path: string; domain: string }) {
  const load = useDomain(domain);
  return <Loaded state={load}>{(d) => <Doc path={path} d={d} />}</Loaded>;
}

function Doc({ path, d }: { path: string; d?: Domain }) {
  const raw = useRaw(path);
  const index = useIndexData();
  const ctx = useLinks(path, d);
  return (
    <Loaded state={raw}>
      {(md) => {
        const title = (md.match(/^# (.+)$/m)?.[1] ?? path).replace(/`/g, "");
        const body = md.replace(/^# .+\n/m, "");
        return (
          <article className="flex flex-col gap-6">
            <Breadcrumb items={crumbsFor(path, title, index.domains)} />
            <PageHeader title={title} scope={<span><code className="type-caption">{path}</code> · <TextLink href={githubBlob(index, path)}>on GitHub</TextLink></span>} />
            <div className="max-w-3xl">
              <Prose md={body} ctx={ctx} />
            </div>
          </article>
        );
      }}
    </Loaded>
  );
}

/** A CSV from a domain folder, as a sortable table. */
export function FilePage() {
  const path = useParams()["*"] ?? "";
  const raw = useRaw(path);
  const index = useIndexData();
  return (
    <Loaded state={raw}>
      {(text) => {
        const rows = parseCsv(text);
        const head = rows.shift() ?? [];
        const objs = rows.map((r, i) => ({ key: String(i), cells: r }));
        const cols: Column<(typeof objs)[number]>[] = head.map((h, j) => ({ key: `c${j}`, header: h || `column ${j + 1}`, value: (r) => r.cells[j] ?? null }));
        return (
          <div className="flex flex-col gap-6">
            <Breadcrumb items={crumbsFor(path, path.split("/").pop() ?? path, index.domains)} />
            <PageHeader title={path.split("/").pop() ?? path} scope={<span><code className="type-caption">{path}</code> · {rows.length} rows · <TextLink href={githubBlob(index, path)}>on GitHub</TextLink></span>} />
            <DataTable caption={path} columns={cols} rows={objs} rowKey={(r) => `row:${r.key}`} sortParam="sort" />
          </div>
        );
      }}
    </Loaded>
  );
}

function parseCsv(text: string): string[][] {
  const rows: string[][] = [];
  let row: string[] = [], cell = "", q = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (q) {
      if (c === '"' && text[i + 1] === '"') { cell += '"'; i++; }
      else if (c === '"') q = false;
      else cell += c;
    } else if (c === '"') q = true;
    else if (c === ",") { row.push(cell); cell = ""; }
    else if (c === "\n" || c === "\r") {
      if (c === "\r" && text[i + 1] === "\n") i++;
      row.push(cell); cell = "";
      if (row.some((x) => x !== "")) rows.push(row);
      row = [];
    } else cell += c;
  }
  if (cell || row.length) { row.push(cell); rows.push(row); }
  return rows;
}

export function SourcesPage() {
  const index = useIndexData();
  const ctx = useLinks("sources.md");
  const cols: Column<SourceEntry>[] = [
    { key: "title", header: "Source", value: (s) => s.title, cell: (s) => <TextLink to={`/doc/sources/${s.slug}/README.md`}>{s.title}</TextLink> },
    { key: "type", header: "Type", value: (s) => s.type || null, hideBelow: "md" },
    { key: "read", header: "Read", value: (s) => s.read.replace(/\*\*/g, "").split(/[.;(]/)[0] || null, truncate: true, hideBelow: "sm" },
    {
      key: "stored",
      header: "Stored copy",
      value: (s) => s.stored.length,
      cell: (s) => (s.stored.length ? <Status tone="success">{`${s.stored.length} file${s.stored.length > 1 ? "s" : ""}`}</Status> : <Status tone="neutral">None</Status>),
    },
  ];
  return (
    <div className="flex flex-col gap-6">
      <Breadcrumb items={[{ label: "Taxonomies", to: "/" }, { label: "Sources" }]} />
      <PageHeader title="Sources" scope={`${index.sources.length} sources, one folder each`} />
      <p className="type-body-sm text-muted-foreground max-w-prose">
        Each source's notes are shown here. Stored copies (PDFs, saved pages) stay in the private repository and are not published on this site; their links go to GitHub. The full list by field, with read status, is{" "}
        <Prose md="[sources.md](sources.md)" ctx={ctx} inline />.
      </p>
      <DataTable caption="Sources" columns={cols} rows={index.sources} rowKey={(s) => `source:${s.slug}`} sortParam="sort" />
    </div>
  );
}
