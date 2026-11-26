import { useParams } from "react-router";
import { Breadcrumb, DataTable, LinkCard, LinkCardList, Metric, MetricStrip, PageHeader, Status, Tabs, TextLink, format } from "strata-react";
import type { Column } from "strata-react";
import { useDomain, useLinks, kap, cap, plainText, type Domain, type Item, type Term } from "../data";
import { KappaWord, Loaded, Prose, Section, StatusWord, TermLink } from "../parts";

export function DomainPage() {
  const { domain = "" } = useParams();
  const load = useDomain(domain);
  return <Loaded state={load}>{(d) => <DomainView d={d} />}</Loaded>;
}

function finding(d: Domain): string {
  const cand = d.counts.status.candidate ?? 0;
  const latest = d.rounds.at(-1);
  if (!d.rounds.length) return `No test round yet: all ${format.integer(d.counts.terms)} terms are drafts until a round scores them.`;
  if (latest && latest.raters.length < 2) return `${latest.title} is waiting for its raters' answers.`;
  if (cand) return `${format.integer(cand)} of ${format.integer(d.counts.terms)} terms are still candidates, waiting for the next round.`;
  return `Every term is approved; the lowest kappa in ${d.counts.latestRound} is ${kap(d.counts.minKappa)}.`;
}

function DomainView({ d }: { d: Domain }) {
  const ctx = useLinks(`${d.path}/scope.md`, d);
  const facets = d.facets.filter((f) => f.inUse);
  const latest = [...d.rounds].reverse().find((r) => r.raters.length >= 2);
  return (
    <div className="flex flex-col gap-8">
      <Breadcrumb items={[{ label: "Taxonomies", to: "/" }, { label: d.title }]} />
      <PageHeader title={d.title} scope={<Prose md={d.status} ctx={ctx} inline />} finding={{ text: finding(d) }} />
      {d.plain ? (
        <div className="max-w-prose">
          <Prose md={cap(d.plain)} ctx={ctx} />
        </div>
      ) : null}
      <MetricStrip label={`${d.title} in figures`}>
        <Metric label="Terms" value={format.integer(d.counts.terms)} note={`${format.integer(d.counts.status.approved ?? 0)} approved, ${format.integer(d.counts.status.candidate ?? 0)} candidate`} />
        <Metric label="Facets" value={format.integer(facets.length)} />
        <Metric label="Items" value={format.integer(d.counts.items)} note="named in samples and rounds" />
        <Metric label="Lowest kappa" value={kap(d.counts.minKappa)} note={latest ? `${latest.title}, target 0.6` : "no round scored yet"} />
      </MetricStrip>
      <Tabs
        param="tab"
        label={`${d.title} views`}
        items={[
          { value: "facets", label: "Facets" },
          { value: "glossary", label: "Glossary" },
          { value: "rounds", label: "Rounds" },
          { value: "items", label: "Items" },
          { value: "files", label: "Files" },
          { value: "changes", label: "Changes" },
        ]}
      >
        {(tab) =>
          tab === "glossary" ? <Glossary d={d} /> : tab === "rounds" ? <Rounds d={d} /> : tab === "items" ? <Items d={d} /> : tab === "files" ? <Files d={d} /> : tab === "changes" ? <Changes d={d} /> : <Facets d={d} />
        }
      </Tabs>
    </div>
  );
}

function Facets({ d }: { d: Domain }) {
  const latest = [...d.rounds].reverse().find((r) => r.raters.length >= 2);
  const facets = d.facets.filter((f) => f.inUse);
  if (!facets.length) return <p className="type-body text-muted-foreground pt-4">No facet is in use yet: no glossary entry names a facet in its Facet field.</p>;
  return (
    <div className="flex flex-col gap-6 pt-4">
      <p className="type-body-sm text-muted-foreground max-w-prose">
        A facet is a question you can ask of any item, with a short list of answers. Each answer is a glossary term. Open a facet for its values and how the raters used them.
      </p>
      <LinkCardList label="Facets">
        {facets.map((f) => {
          const k = latest?.kappa.find((x) => x.facet === f.id);
          return (
            <LinkCard
              key={f.id}
              to={`/d/${d.id}/facet/${f.id}`}
              title={f.label}
              description={`${f.fields.Question ?? ""} ${f.values.map((v) => d.terms[v]?.label ?? v).join(", ")}.`}
              marks={
                <>
                  <Status tone="neutral">{`${f.values.length} values`}</Status>
                  {k ? <Status tone={k.kappa != null && k.kappa >= 0.6 ? "success" : "warning"}>{`κ ${kap(k.kappa)}`}</Status> : <Status tone="neutral">Not scored</Status>}
                  {f.unsorted.length ? <Status tone="warning">{`${f.unsorted.length} unsorted`}</Status> : null}
                </>
              }
            />
          );
        })}
      </LinkCardList>
    </div>
  );
}

function tree(d: Domain) {
  const roots = Object.values(d.terms).filter((t) => !t.broader.some((b) => d.terms[b]));
  const Node = ({ t, depth }: { t: Term; depth: number }) => (
    <li>
      <TermLink domain={d.id} id={t.id} label={t.label} />
      {t.narrower.length ? (
        <ul className="pl-5 border-l border-border ml-1 flex flex-col gap-1 pt-1">
          {t.narrower.map((n) => (d.terms[n] && depth < 8 ? <Node key={n} t={d.terms[n]} depth={depth + 1} /> : null))}
        </ul>
      ) : null}
    </li>
  );
  const withKids = roots.filter((t) => t.narrower.length);
  return { withKids, Node };
}

function Glossary({ d }: { d: Domain }) {
  const ctx = useLinks(`${d.path}/glossary.md`, d);
  const rows = Object.values(d.terms);
  const columns: Column<Term>[] = [
    { key: "label", header: "Term", value: (t) => t.label, cell: (t) => <TermLink domain={d.id} id={t.id} label={t.label} /> },
    { key: "definition", header: "Definition", value: (t) => t.fields.Definition ?? "", cell: (t) => <Prose md={t.fields.Definition ?? ""} ctx={ctx} inline />, hideBelow: "md" },
    { key: "kind", header: "Kind", value: (t) => t.kind, hideBelow: "sm" },
    { key: "facet", header: "Facet", value: (t) => t.facets.join(", ") || null, missing: "Not a value", hideBelow: "lg" },
    { key: "status", header: "Status", value: (t) => t.status, cell: (t) => <StatusWord status={t.status} /> },
  ];
  const { withKids, Node } = tree(d);
  return (
    <div className="flex flex-col gap-8 pt-4">
      <DataTable caption={`${d.title} glossary`} columns={columns} rows={rows} rowKey={(t) => `term:${t.id}`} sortParam="sort" virtualizeFrom={400} />
      {withKids.length ? (
        <Section title="Broader and narrower" id="tree" intro="Terms with a Broader field, drawn as the is-a tree they make. Narrower links are derived, never written by hand (spec §4).">
          <ul className="flex flex-col gap-2 type-body">
            {withKids.map((t) => (
              <Node key={t.id} t={t} depth={0} />
            ))}
          </ul>
        </Section>
      ) : null}
      <details className="max-w-prose">
        <summary className="type-label cursor-pointer">The glossary's own introduction and label choices</summary>
        <div className="pt-3">
          <Prose md={d.glossaryIntro} ctx={ctx} />
        </div>
      </details>
    </div>
  );
}

function Rounds({ d }: { d: Domain }) {
  if (!d.rounds.length)
    return <p className="type-body text-muted-foreground pt-4 max-w-prose">No round yet. A round is two or more raters from different model families sorting fresh items with only the facets and glossary; its answers and kappa will show here once a `rounds/round-N/` folder exists.</p>;
  return (
    <div className="flex flex-col gap-6 pt-4">
      <LinkCardList label="Rounds">
        {d.rounds.map((r) => {
          const low = r.kappa.reduce<number | null>((m, k) => (k.kappa == null ? m : m == null ? k.kappa : Math.min(m, k.kappa)), null);
          return (
            <LinkCard
              key={r.id}
              to={`/d/${d.id}/round/${r.id}`}
              title={r.title}
              description={plainText(r.oneLine)}
              marks={
                <>
                  <Status tone="neutral">{`${r.items.length || Object.keys(r.answers).length} items`}</Status>
                  <Status tone="neutral">{`${r.raters.length} raters`}</Status>
                  <KappaWord kappa={low} raters={r.raters.length} />
                </>
              }
            />
          );
        })}
      </LinkCardList>
    </div>
  );
}

function Items({ d }: { d: Domain }) {
  const ctx = useLinks(`${d.path}/samples.md`, d);
  const rows = Object.values(d.items);
  const columns: Column<Item>[] = [
    { key: "id", header: "Item", value: (i) => i.id, cell: (i) => <TextLink to={`/d/${d.id}/item/${i.id}`}>{i.id}</TextLink> },
    { key: "item", header: "What it says", value: (i) => i.item, cell: (i) => <Prose md={i.item} ctx={ctx} inline /> },
    { key: "set", header: "Set", value: (i) => i.set || null, hideBelow: "md", missing: "Round only" },
    { key: "rounds", header: "Rated in", value: (i) => i.rounds.join(", ") || null, missing: "Not rated", hideBelow: "sm" },
  ];
  return (
    <div className="flex flex-col gap-4 pt-4">
      <p className="type-body-sm text-muted-foreground max-w-prose">
        Items are the domain's own material that the facets must sort: build items (used to find the facets), bare test items, and fresh items held back for the rounds.
      </p>
      <DataTable caption={`${d.title} items`} columns={columns} rows={rows} rowKey={(i) => `item:${i.id}`} sortParam="isort" />
    </div>
  );
}

function Files({ d }: { d: Domain }) {
  return (
    <div className="grid gap-8 pt-4 md:grid-cols-2">
      <Section title="Documents" id="docs">
        <ul className="flex flex-col gap-1 type-body-sm">
          {d.docs.map((p) => (
            <li key={p}>
              <TextLink to={`/doc/${p}`}>{p.slice(d.path.length + 1)}</TextLink>
            </li>
          ))}
        </ul>
      </Section>
      <Section title="Data files" id="data" intro="CSV files open as tables; anything else links to the repo.">
        <ul className="flex flex-col gap-1 type-body-sm">
          {d.files.map((p) => (
            <li key={p}>{p.endsWith(".csv") ? <TextLink to={`/file/${p}`}>{p.slice(d.path.length + 1)}</TextLink> : <FileOnGithub path={p} base={d.path} />}</li>
          ))}
        </ul>
      </Section>
    </div>
  );
}

function FileOnGithub({ path, base }: { path: string; base: string }) {
  const ctx = useLinks(path);
  return <Prose md={`[${path.slice(base.length + 1)}](${path.split("/").pop()})`} ctx={ctx} inline />;
}

function Changes({ d }: { d: Domain }) {
  const ctx = useLinks(`${d.path}/changelog.md`, d);
  if (!d.changelog.length) return <p className="pt-4 type-body text-muted-foreground">No changelog entries yet.</p>;
  const days = [...new Set(d.changelog.map((c) => c.date))];
  return (
    <div className="flex flex-col gap-6 pt-4 max-w-prose">
      {days.map((day) => (
        <Section key={day} title={day ? format.date(day) : "Undated"}>
          <ul className="flex flex-col gap-2 list-disc pl-5 type-body-sm">
            {d.changelog
              .filter((c) => c.date === day)
              .map((c, i) => (
                <li key={i}>
                  <Prose md={c.text} ctx={ctx} inline />
                </li>
              ))}
          </ul>
        </Section>
      ))}
    </div>
  );
}

