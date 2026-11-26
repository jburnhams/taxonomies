import { LinkCard, LinkCardList, Metric, MetricStrip, PageHeader, Status, TextLink, format } from "strata-react";
import { useIndexData, useLinks, kap, plainText } from "../data";
import { Prose, Section } from "../parts";

export function Overview() {
  const index = useIndexData();
  const ctx = useLinks("README.md");
  const terms = index.domains.reduce((n, d) => n + d.counts.terms, 0);
  const approved = index.domains.reduce((n, d) => n + (d.counts.status.approved ?? 0), 0);
  const method = index.designDocs.filter((d) => ["design/process.md", "design/spec.md", "design/decisions.md", "design/README.md"].includes(d.path));
  const topics = index.topDocs.filter((d) => /^\d\d-/.test(d.path));
  const eli5 = index.topDocs.find((d) => d.path === "eli5.md");
  return (
    <div className="flex flex-col gap-10">
      <PageHeader
        title="Taxonomies"
        scope={`Generated from ${index.repo} at ${index.short || "the working tree"}${index.date ? `, ${format.date(index.date)}` : ""}`}
      />
      <div className="max-w-prose flex flex-col gap-3">
        <Prose md={index.readme.intro} ctx={ctx} />
      </div>
      <MetricStrip label="The taxonomies so far">
        <Metric label="Domains" value={format.integer(index.domains.length)} />
        <Metric label="Terms" value={format.integer(terms)} note={`${format.integer(approved)} approved, the rest candidates`} />
        <Metric label="Sources" value={format.integer(index.sources.length)} note="each with a folder and notes" />
      </MetricStrip>

      <Section
        title="Explore a taxonomy"
        id="domains"
        intro="Each domain is one vocabulary: its sorting questions (facets), one entry per concept (the glossary), and the test rounds that decided them. Open one to drill from a facet to a term, to the items the raters sorted under it, to their raw answers."
      >
        <LinkCardList label="Domains">
          {index.domains.map((d) => (
            <LinkCard
              key={d.id}
              to={`/d/${d.id}`}
              title={d.title}
              description={plainText(d.oneLine)}
              marks={
                <>
                  <Status tone={d.statusWord === "in use" ? "success" : "info"}>
                    {d.statusWord === "in use" ? "In use" : d.statusWord === "retired" ? "Retired" : "Draft"}
                  </Status>
                  <Status tone="neutral">{`${format.integer(d.counts.terms)} terms`}</Status>
                  <Status tone="neutral">{`${format.integer(d.counts.facets)} facets`}</Status>
                  {d.counts.minKappa != null ? <Status tone="neutral">{`Lowest κ ${kap(d.counts.minKappa)}`}</Status> : <Status tone="neutral">Not tested yet</Status>}
                </>
              }
            />
          ))}
        </LinkCardList>
      </Section>

      <Section title="The method" id="method" intro="How every taxonomy here is built and checked. Every rule cites a stored source.">
        <LinkCardList label="Method documents">
          {eli5 ? <LinkCard to={`/doc/${eli5.path}`} title="Start here: taxonomy from zero" description={plainText(eli5.oneLine) || "Taxonomy explained in levels, from like-you're-five up."} /> : null}
          {method.map((d) => (
            <LinkCard key={d.path} to={`/doc/${d.path}`} title={d.title} description={plainText(d.oneLine)} />
          ))}
        </LinkCardList>
      </Section>

      <Section title="The research" id="research" intro="Topic docs that synthesise across the sources, then the sources themselves.">
        <ol className="flex flex-col gap-3 type-body">
          {topics.map((d) => (
            <li key={d.path}>
              <TextLink to={`/doc/${d.path}`}>{d.title}</TextLink>
              {d.oneLine ? <p className="text-muted-foreground type-body-sm max-w-prose">{plainText(d.oneLine)}</p> : null}
            </li>
          ))}
          <li>
            <TextLink to="/sources">{`All ${index.sources.length} sources`}</TextLink>
          </li>
        </ol>
      </Section>
      {index.problems.length ? (
        <Section title="What the generator could not read" id="problems">
          <ul className="type-body-sm list-disc pl-5">
            {index.problems.map((p) => (
              <li key={p}>{p}</li>
            ))}
          </ul>
        </Section>
      ) : null}
    </div>
  );
}
