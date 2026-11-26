import { useEffect, useRef } from "react";
import { useSearchParams } from "react-router";
import { DataView, EmptyState, Skeleton, Status, TextLink } from "strata-react";
import type { Load } from "strata-react";
import { renderInline, renderMarkdown, type LinkContext } from "./markdown";

/** Rendered Markdown from the repo. Scrolls to `?a=<anchor>` once drawn. */
export function Prose({ md, ctx, inline = false, className = "" }: { md: string; ctx: LinkContext; inline?: boolean; className?: string }) {
  const ref = useRef<HTMLDivElement>(null);
  const [params] = useSearchParams();
  const anchor = params.get("a");
  const html = inline ? renderInline(md, ctx) : renderMarkdown(md, ctx);
  useEffect(() => {
    if (!anchor || !ref.current) return;
    const el = ref.current.querySelector(`[id="${CSS.escape(anchor)}"]`);
    el?.scrollIntoView({ block: "start" });
  }, [anchor, html]);
  if (inline) return <span className={`prose prose-inline ${className}`} dangerouslySetInnerHTML={{ __html: html }} />;
  return <div ref={ref} className={`prose ${className}`} dangerouslySetInnerHTML={{ __html: html }} />;
}

export function PageSkeleton() {
  return (
    <div className="flex flex-col gap-4" aria-hidden="true">
      <Skeleton className="h-9 w-2/3" />
      <Skeleton className="h-5 w-full" />
      <Skeleton className="h-5 w-5/6" />
      <div className="grid gap-4 sm:grid-cols-3">
        <Skeleton className="h-24" />
        <Skeleton className="h-24" />
        <Skeleton className="h-24" />
      </div>
      <Skeleton className="h-64" />
    </div>
  );
}

/** A loaded value, or the skeleton, or the failed read with Try again. */
export function Loaded<T>({ state, children }: { state: Load<T>; children: (data: T) => React.ReactNode }) {
  return (
    <DataView state={state} isEmpty={() => false} skeleton={<PageSkeleton />} empty={<EmptyState title="Nothing here" />}>
      {children}
    </DataView>
  );
}

export function Section({ title, id, children, intro }: { title: string; id?: string; children: React.ReactNode; intro?: React.ReactNode }) {
  return (
    <section aria-labelledby={id ? `${id}-h` : undefined} className="flex flex-col gap-3">
      <h2 id={id ? `${id}-h` : undefined} className="type-heading">
        {title}
      </h2>
      {intro ? <div className="type-body-sm text-muted-foreground max-w-prose">{intro}</div> : null}
      {children}
    </section>
  );
}

const STATUS_TONE: Record<string, "success" | "info" | "neutral" | "warning"> = {
  approved: "success",
  candidate: "info",
  deprecated: "neutral",
  "in use": "success",
  draft: "info",
  retired: "neutral",
};

/** A term's or domain's status as its word. */
export function StatusWord({ status }: { status: string }) {
  const word = status || "unknown";
  return <Status tone={STATUS_TONE[word] ?? "neutral"}>{word[0].toUpperCase() + word.slice(1)}</Status>;
}

/** Kappa against the method's target (κ ≥ 0.6, spec T8). */
export function KappaWord({ kappa, raters }: { kappa: number | null | undefined; raters: number }) {
  if (raters < 2 || kappa == null) return <Status tone="neutral">Not scored</Status>;
  return kappa >= 0.6 ? <Status tone="success">Passes</Status> : <Status tone="warning">Below 0.6</Status>;
}

export function TermLink({ domain, id, label }: { domain: string; id: string; label?: string }) {
  return <TextLink to={`/d/${domain}/term/${id}`}>{label ?? id}</TextLink>;
}

export function Facts({ items }: { items: { label: string; value: React.ReactNode }[] }) {
  return (
    <dl className="grid gap-x-6 gap-y-2 sm:grid-cols-[max-content_1fr]">
      {items.map((it) => (
        <div key={it.label} className="contents">
          <dt className="type-label text-muted-foreground">{it.label}</dt>
          <dd className="type-body-sm min-w-0">{it.value}</dd>
        </div>
      ))}
    </dl>
  );
}
