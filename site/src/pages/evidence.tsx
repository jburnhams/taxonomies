// The drill-down pages: a facet, a term, a round, an item. Each shows the record as the
// repo writes it and then the evidence under it, down to each rater's raw answer.
import { useParams } from "react-router";
import { Breadcrumb, CompositionBar, DataTable, EmptyState, PageHeader, Status, TextLink, format } from "strata-react";
import type { Column } from "strata-react";
import { useDomain, useIndexData, useLinks, githubBlob, kap, pct, cap, type Domain, type Round, type Term } from "../data";
import { Facts, KappaWord, Loaded, Prose, Section, StatusWord, TermLink } from "../parts";

function useDomainPage<T>(render: (d: Domain) => React.ReactNode) {
  const { domain = "" } = useParams();
  const load = useDomain(domain);
  return <Loaded state={load}>{render}</Loaded>;
}

const crumbs = (d: Domain, ...rest: { label: string; to?: string }[]) => [{ label: "Taxonomies", to: "/" }, { label: d.title, to: `/d/${d.id}` }, ...rest];

function Missing({ what, d }: { what: string; d: Domain }) {
  return <EmptyState title={`No ${what} by that name in ${d.title}`} action={<TextLink to={`/d/${d.id}`}>Back to {d.title}</TextLink>} />;
}

// ---------- facet ----------

export function FacetPage() {
  const { facet = "" } = useParams();
  return useDomainPage((d) => {
    const f = d.facets.find((x) => x.id === facet);
    return f ? <FacetView d={d} fid={facet} /> : <Missing what="facet" d={d} />;
  });
}

function FacetView({ d, fid }: { d: Domain; fid: string }) {
  const f = d.facets.find((x) => x.id === fid)!;
  const ctx = useLinks(`${d.path}/facets.md`, d);
  const rounds = d.rounds.filter((r) => r.facets.includes(fid) && r.raters.length);
  const FIELDS = ["Principle", "Kind", "Order", "Agreement", "Unsorted"];
  return (
    <div className="flex flex-col gap-8">
      <Breadcrumb items={crumbs(d, { label: "Facets", to: `/d/${d.id}?tab=facets` }, { label: f.label })} />
      <PageHeader title={f.label} scope={f.fields.Question} />
      {!f.inUse ? <Status tone="neutral">Not in use: an alternative that was weighed</Status> : null}
      <Facts items={FIELDS.filter((k) => f.fields[k]).map((k) => ({ label: k, value: <Prose md={f.fields[k]} ctx={ctx} inline /> }))} />
      <Section title="Values" id="values" intro="Each value is a glossary term. The counts are how many round items each rater put under it.">
        <DataTable
          caption={`Values of ${f.label}`}
          rowKey={(v: string) => `value:${v}`}
          rows={f.values}
          columns={[
            { key: "value", header: "Value", value: (v: string) => f.values.indexOf(v), cell: (v: string) => <TermLink domain={d.id} id={v} label={d.terms[v]?.label ?? v} /> },
            { key: "def", header: "Definition", value: (v: string) => d.terms[v]?.fields.Definition ?? null, cell: (v: string) => <Prose md={d.terms[v]?.fields.Definition ?? "No glossary entry"} ctx={ctx} inline />, hideBelow: "md" },
            ...rounds.flatMap((r) =>
              r.raters.map(
                (rt): Column<string> => ({
                  key: `${r.id}-${rt.name}`,
                  header: `${rt.name}, ${r.id}`,
                  numeric: true,
                  value: (v: string) => Object.values(r.answers).filter((a) => a[rt.name]?.[fid] === v).length,
                  hideBelow: "sm",
                }),
              ),
            ),
            { key: "status", header: "Status", value: (v: string) => d.terms[v]?.status ?? null, cell: (v: string) => <StatusWord status={d.terms[v]?.status ?? ""} /> },
          ]}
        />
      </Section>
      {rounds.map((r) => (
        <RoundShare key={r.id} r={r} fid={fid} d={d} />
      ))}
      {f.prose ? (
        <Section title="Notes" id="notes">
          <div className="max-w-prose">
            <Prose md={f.prose} ctx={ctx} />
          </div>
        </Section>
      ) : null}
      <p className="type-body-sm text-muted-foreground">
        As written in <TextLink to={`/doc/${d.path}/facets.md`}>facets.md</TextLink>, under “{f.set}”.
      </p>
    </div>
  );
}

function RoundShare({ r, fid, d }: { r: Round; fid: string; d: Domain }) {
  const f = d.facets.find((x) => x.id === fid)!;
  const consensus = new Map<string, number>();
  let split = 0;
  for (const by of Object.values(r.answers)) {
    const vals = new Set(Object.values(by).map((a) => a[fid]));
    if (vals.size === 1) {
      const v = [...vals][0];
      consensus.set(v, (consensus.get(v) ?? 0) + 1);
    } else split++;
  }
  const k = r.kappa.find((x) => x.facet === fid);
  const parts = [
    ...f.values.filter((v) => consensus.get(v)).map((v) => ({ key: v, label: d.terms[v]?.label ?? v, value: consensus.get(v)! })),
    ...[...consensus.keys()].filter((v) => !f.values.includes(v)).map((v) => ({ key: v, label: `${v} (not a value)`, value: consensus.get(v)! })),
    ...(split ? [{ key: "_split", label: "Raters split", value: split, colour: "var(--muted-foreground)" }] : []),
  ];
  if (r.raters.length < 2) return null;
  return (
    <Section
      title={`How ${r.title.toLowerCase()} sorted it`}
      id={`share-${r.id}`}
      intro={
        <>
          Items the raters agreed on, by value, and items they split on. Agreement {pct(k?.agreement)}, {k?.measure ?? "Cohen"}'s κ {kap(k?.kappa)} on {k?.n} items.{" "}
          <TextLink to={`/d/${d.id}/round/${r.id}?facet=${fid}`}>See each item</TextLink>
        </>
      }
    >
      <div className="max-w-2xl">
        <CompositionBar label={`${f.label}, ${r.id}`} parts={parts} formatValue={(n) => format.count(n, "item", "items")} partHeader="Value" valueHeader="Items" />
      </div>
    </Section>
  );
}

// ---------- term ----------

export function TermPage() {
  const { term = "" } = useParams();
  return useDomainPage((d) => (d.terms[term] ? <TermView d={d} t={d.terms[term]} /> : <Missing what="term" d={d} />));
}

const SHOWN = ["Scope", "Aliases", "Hidden", "Example", "Near miss", "Kind", "Warrant"];

function TermView({ d, t }: { d: Domain; t: Term }) {
  const ctx = useLinks(`${d.path}/glossary.md`, d);
  const index = useIndexData();
  const chain: Term[] = [];
  for (let cur = t.broader[0]; cur && d.terms[cur] && chain.length < 10; cur = d.terms[cur].broader[0]) chain.unshift(d.terms[cur]);
  const facet = t.facets[0] ? d.facets.find((f) => f.id === t.facets[0]) : undefined;
  const path = facet
    ? [{ label: facet.label, to: `/d/${d.id}/facet/${facet.id}` }]
    : [{ label: "Glossary", to: `/d/${d.id}?tab=glossary` }, ...chain.map((c) => ({ label: c.label, to: `/d/${d.id}/term/${c.id}` }))];
  const history = (t.fields.History ?? "").split(/;\s*(?=\d{4}-\d{2}-\d{2})/).filter(Boolean);
  const other = t.order.filter((k) => !SHOWN.includes(k) && !["Definition", "Status", "History", "Broader", "Related", "Facet", "Replaced by"].includes(k));
  const placed = t.placed;
  const rel = (ids: string[]) =>
    ids.length ? (
      <span className="flex flex-wrap gap-x-3 gap-y-1">
        {ids.map((x) => (
          <TermLink key={x} domain={d.id} id={x} label={d.terms[x]?.label ?? x} />
        ))}
      </span>
    ) : null;
  const relations = [
    { label: "Broader", value: rel(t.broader) },
    { label: "Narrower", value: rel(t.narrower) },
    { label: "Related", value: rel(t.related) },
    { label: "Replaced by", value: rel(t.replacedBy) },
    { label: "Value of", value: facet ? <TextLink to={`/d/${d.id}/facet/${facet.id}`}>{`${facet.label}: ${facet.fields.Question ?? ""}`}</TextLink> : null },
    { label: "Beside it", value: facet ? rel(facet.values.filter((v) => v !== t.id)) : null },
  ].filter((r) => r.value);
  return (
    <div className="flex flex-col gap-8">
      <Breadcrumb items={crumbs(d, ...path, { label: t.label })} />
      <PageHeader title={t.label} scope={<span className="flex flex-wrap items-center gap-2"><StatusWord status={t.status} /><code className="type-caption">{`${d.id}:${t.id}`}</code></span>} />
      <div className="max-w-prose type-body">
        <Prose md={t.fields.Definition ?? "No definition."} ctx={ctx} />
      </div>
      <Facts items={SHOWN.concat(other).filter((k) => t.fields[k]).map((k) => ({ label: k, value: <Prose md={t.fields[k]} ctx={ctx} inline /> }))} />
      {relations.length ? (
        <Section title="Where it sits" id="relations">
          <Facts items={relations} />
        </Section>
      ) : null}
      <Section title="How it was decided" id="evidence" intro="The term's history, the changes logged against it, and every round item a rater sorted under it, with each rater's answer.">
        <ol className="flex flex-col gap-1 type-body-sm list-disc pl-5">
          {history.map((h, i) => (
            <li key={i}>
              <Prose md={h} ctx={ctx} inline />
            </li>
          ))}
        </ol>
        {t.changelog.length ? (
          <div className="flex flex-col gap-2">
            <h3 className="type-label">In the changelog</h3>
            <ul className="flex flex-col gap-2 type-body-sm list-disc pl-5">
              {t.changelog.map((i) => (
                <li key={i}>
                  <span className="text-muted-foreground">{d.changelog[i].date}: </span>
                  <Prose md={d.changelog[i].text} ctx={ctx} inline />
                </li>
              ))}
            </ul>
          </div>
        ) : null}
        {t.items.length ? (
          <p className="type-body-sm">
            Items its notes name:{" "}
            {t.items.map((i, n) => (
              <span key={i}>
                {n ? ", " : ""}
                <TextLink to={`/d/${d.id}/item/${i}`}>{i}</TextLink>
              </span>
            ))}
          </p>
        ) : null}
      </Section>
      {placed.length ? <Placed d={d} t={t} /> : facet ? <p className="type-body-sm text-muted-foreground">No rater has put an item under this value yet.</p> : null}
      <p className="type-body-sm text-muted-foreground">
        As written in <TextLink to={`/doc/${d.path}/glossary.md`}>glossary.md</TextLink>
        {t.section ? `, under “${t.section}”` : ""}. <TextLink href={githubBlob(index, `${d.path}/glossary.md`)}>Source on GitHub</TextLink>
      </p>
    </div>
  );
}


type PlacedRow = { key: string; round: Round; item: string; facet: string };

function Placed({ d, t }: { d: Domain; t: Term }) {
  const ctx = useLinks(`${d.path}/rounds`, d);
  const rows: PlacedRow[] = t.placed.map((p) => ({ key: `${p.round}/${p.item}/${p.facet}`, round: d.rounds.find((r) => r.id === p.round)!, item: p.item, facet: p.facet }));
  const raters = [...new Set(rows.flatMap((r) => r.round.raters.map((x) => x.name)))];
  const agreed = rows.filter((r) => new Set(Object.values(r.round.answers[r.item] ?? {}).map((a) => a[r.facet])).size === 1).length;
  const columns: Column<PlacedRow>[] = [
    { key: "item", header: "Item", value: (r) => r.item, cell: (r) => <TextLink to={`/d/${d.id}/item/${r.item}`}>{r.item}</TextLink> },
    { key: "text", header: "What it says", value: (r) => d.items[r.item]?.item ?? "", cell: (r) => <Prose md={d.items[r.item]?.item ?? ""} ctx={ctx} inline /> },
    ...raters.map(
      (n): Column<PlacedRow> => ({
        key: n,
        header: n,
        value: (r) => r.round.answers[r.item]?.[n]?.[r.facet] ?? null,
        cell: (r) => {
          const v = r.round.answers[r.item]?.[n]?.[r.facet];
          return v === t.id ? <span>{d.terms[v]?.label ?? v}</span> : v ? <Status tone="warning">{d.terms[v]?.label ?? v}</Status> : null;
        },
      }),
    ),
    { key: "round", header: "Round", value: (r) => r.round.id, hideBelow: "sm" },
  ];
  return (
    <Section
      title="Items the raters put here"
      id="placed"
      intro={`${format.count(rows.length, "item", "items")}; the raters agreed on ${format.integer(agreed)}. A highlighted answer is a rater who chose another value.`}
    >
      <DataTable caption={`Round items sorted under ${t.label}`} columns={columns} rows={rows} rowKey={(r) => `placed:${r.key}`} />
      <p className="type-body-sm text-muted-foreground">
        Raw answers:{" "}
        {[...new Set(rows.map((r) => r.round))].flatMap((r) => r.raters).map((rt, i) => (
          <span key={rt.file}>
            {i ? ", " : ""}
            <TextLink to={`/file/${rt.file}`}>{rt.file.split("/").slice(-3).join("/")}</TextLink>
          </span>
        ))}
      </p>
    </Section>
  );
}

// ---------- round ----------

export function RoundPage() {
  const { round = "" } = useParams();
  return useDomainPage((d) => {
    const r = d.rounds.find((x) => x.id === round);
    return r ? <RoundView d={d} r={r} /> : <Missing what="round" d={d} />;
  });
}

type ItemRow = { id: string; item: string };

function RoundView({ d, r }: { d: Domain; r: Round }) {
  const ctx = useLinks(`${r.path}/README.md`, d);
  const rows: ItemRow[] = (r.items.length ? r.items : Object.keys(r.answers).map((id) => ({ id, item: d.items[id]?.item ?? "" }))).map((i) => ({ id: i.id, item: i.item }));
  const raters = r.raters.map((x) => x.name);
  const cols: Column<ItemRow>[] = [
    { key: "id", header: "Item", value: (i) => i.id, cell: (i) => <TextLink to={`/d/${d.id}/item/${i.id}`}>{i.id}</TextLink> },
    { key: "item", header: "What it says", value: (i) => i.item, cell: (i) => <Prose md={i.item} ctx={ctx} inline />, truncate: false },
    ...r.facets.map(
      (f): Column<ItemRow> => ({
        key: f,
        header: d.facets.find((x) => x.id === f)?.label ?? f,
        value: (i) => {
          const vals = raters.map((n) => r.answers[i.id]?.[n]?.[f] ?? "");
          return new Set(vals).size === 1 ? vals[0] || null : `~${vals.join(" / ")}`;
        },
        cell: (i) => {
          const vals = raters.map((n) => r.answers[i.id]?.[n]?.[f] ?? "");
          if (!vals.some(Boolean)) return null;
          if (new Set(vals).size === 1) return <TermLink domain={d.id} id={vals[0]} label={d.terms[vals[0]]?.label ?? vals[0]} />;
          return <Status tone="warning">{vals.map((v) => d.terms[v]?.label ?? (v || "none")).join(" / ")}</Status>;
        },
        hideBelow: "sm",
      }),
    ),
  ];
  return (
    <div className="flex flex-col gap-8">
      <Breadcrumb items={crumbs(d, { label: "Rounds", to: `/d/${d.id}?tab=rounds` }, { label: r.title })} />
      <PageHeader title={r.title} scope={`${format.count(rows.length, "item", "items")}, ${format.count(raters.length, "rater", "raters")}: ${raters.join(", ") || "none yet"}`} />
      {r.oneLine ? (
        <div className="max-w-prose">
          <Prose md={cap(r.oneLine)} ctx={ctx} />
        </div>
      ) : null}
      {raters.length >= 2 ? (
        <Section title="Agreement per facet" id="kappa" intro="Recomputed here from the answer files with the formula in tools/kappa.py (Cohen for two raters, Fleiss for three or more). Target κ ≥ 0.6 on every facet (spec T8, J5).">
          <DataTable
            caption="Kappa per facet"
            rowKey={(k) => `facet:${k.facet}`}
            rows={r.kappa}
            columns={[
              { key: "facet", header: "Facet", value: (k) => k.facet, cell: (k) => <TextLink to={`/d/${d.id}/facet/${k.facet}`}>{d.facets.find((f) => f.id === k.facet)?.label ?? k.facet}</TextLink> },
              { key: "agreement", header: "Agreement", numeric: true, value: (k) => k.agreement ?? null, cell: (k) => pct(k.agreement) },
              { key: "kappa", header: "Kappa", numeric: true, value: (k) => k.kappa ?? null, cell: (k) => kap(k.kappa) },
              { key: "measure", header: "Measure", value: (k) => k.measure ?? null, hideBelow: "sm" },
              { key: "n", header: "Items", numeric: true, value: (k) => k.n, hideBelow: "sm" },
              { key: "pass", header: "Result", value: (k) => (k.kappa != null && k.kappa >= 0.6 ? 1 : 0), cell: (k) => <KappaWord kappa={k.kappa} raters={raters.length} /> },
            ]}
          />
          {raters.length > 2 ? (
            <DataTable
              caption="Cohen's kappa for each pair of raters"
              rowKey={(p) => `pair:${p.a}-${p.b}-${p.facet}`}
              rows={r.pairs}
              columns={[
                { key: "pair", header: "Pair", value: (p) => `${p.a} / ${p.b}` },
                { key: "facet", header: "Facet", value: (p) => p.facet },
                { key: "agreement", header: "Agreement", numeric: true, value: (p) => p.agreement, cell: (p) => pct(p.agreement) },
                { key: "kappa", header: "Kappa", numeric: true, value: (p) => p.kappa, cell: (p) => kap(p.kappa) },
              ]}
            />
          ) : null}
        </Section>
      ) : (
        <p className="type-body text-muted-foreground max-w-prose">This round has {raters.length ? "one rater's answers" : "no answers"} yet, so nothing is scored. The items and prompts are below.</p>
      )}
      <Section title="Every item and every answer" id="items" intro={raters.length >= 2 ? "One link where the raters agreed; both answers, highlighted, where they split." : undefined}>
        <DataTable caption={`${r.title} items`} columns={cols} rows={rows} rowKey={(i) => `item:${i.id}`} sortParam="sort" />
      </Section>
      <Section title="Files" id="files">
        <ul className="flex flex-col gap-1 type-body-sm">
          {r.docs.map((p) => (
            <li key={p}>
              <TextLink to={`/doc/${p}`}>{p.slice(r.path.length + 1)}</TextLink>
            </li>
          ))}
          {r.files.map((p) => (
            <li key={p}>{p.endsWith(".csv") ? <TextLink to={`/file/${p}`}>{p.slice(r.path.length + 1)}</TextLink> : <Prose md={`[${p.slice(r.path.length + 1)}](${p.slice(r.path.length + 1)})`} ctx={ctx} inline />}</li>
          ))}
        </ul>
      </Section>
    </div>
  );
}

// ---------- item ----------

export function ItemPage() {
  const { item = "" } = useParams();
  return useDomainPage((d) => (d.items[item] ? <ItemView d={d} id={item} /> : <Missing what="item" d={d} />));
}

function ItemView({ d, id }: { d: Domain; id: string }) {
  const it = d.items[id];
  const ctx = useLinks(`${d.path}/samples.md`, d);
  const rounds = d.rounds.filter((r) => r.answers[id]);
  return (
    <div className="flex flex-col gap-8">
      <Breadcrumb items={crumbs(d, { label: "Items", to: `/d/${d.id}?tab=items` }, { label: id })} />
      <PageHeader title={`Item ${id}`} scope={it.set || (it.rounds.length ? `Test item, ${it.rounds.join(", ")}` : undefined)} />
      <div className="max-w-prose type-body">
        <Prose md={it.item} ctx={ctx} />
      </div>
      <Facts
        items={[
          { label: "From", value: it.from ? <Prose md={it.from} ctx={ctx} inline /> : null },
          { label: "Unsorted in", value: it.unsortedIn.length ? it.unsortedIn.map((f) => <TextLink key={f} to={`/d/${d.id}/facet/${f}`}>{f}</TextLink>) : null },
          { label: "Named by", value: it.terms.length ? <span className="flex flex-wrap gap-x-3">{it.terms.map((t) => <TermLink key={t} domain={d.id} id={t} label={d.terms[t]?.label} />)}</span> : null },
          { label: "Mentioned in", value: it.docs.length ? <span className="flex flex-wrap gap-x-3">{it.docs.map((p) => <TextLink key={p} to={`/doc/${p}`}>{p.slice(d.path.length + 1)}</TextLink>)}</span> : null },
        ].filter((x) => x.value)}
      />
      {rounds.map((r) => (
        <Section key={r.id} title={`Answers in ${r.title}`} id={r.id}>
          <DataTable
            caption={`Answers for ${id} in ${r.id}`}
            rowKey={(f: string) => `facet:${f}`}
            rows={r.facets}
            columns={[
              { key: "facet", header: "Facet", value: (f: string) => f, cell: (f: string) => <TextLink to={`/d/${d.id}/facet/${f}`}>{d.facets.find((x) => x.id === f)?.label ?? f}</TextLink> },
              ...r.raters.map(
                (rt): Column<string> => ({
                  key: rt.name,
                  header: rt.name,
                  value: (f: string) => r.answers[id]?.[rt.name]?.[f] ?? null,
                  cell: (f: string) => {
                    const v = r.answers[id]?.[rt.name]?.[f];
                    return v ? <TermLink domain={d.id} id={v} label={d.terms[v]?.label ?? v} /> : null;
                  },
                }),
              ),
              {
                key: "agree",
                header: "Raters",
                value: (f: string) => new Set(r.raters.map((rt) => r.answers[id]?.[rt.name]?.[f])).size,
                cell: (f: string) => (new Set(r.raters.map((rt) => r.answers[id]?.[rt.name]?.[f])).size === 1 ? <Status tone="success">Agree</Status> : <Status tone="warning">Split</Status>),
              },
            ]}
          />
          {r.notes[id] ? (
            <ul className="flex flex-col gap-1 type-body-sm">
              {Object.entries(r.notes[id]).map(([n, note]) => (
                <li key={n}>
                  <span className="type-label">{n}’s note: </span>
                  {note}
                </li>
              ))}
            </ul>
          ) : null}
        </Section>
      ))}
    </div>
  );
}
