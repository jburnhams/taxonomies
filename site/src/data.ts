// The shapes site/generate.py writes, and the hooks that read them.
import { createContext, useContext, useMemo } from "react";
import { fetchJson, useLoad } from "strata-react";
import type { LinkContext } from "./markdown";

export type FacetSummary = { id: string; label: string; values: string[]; question: string };
export type Counts = {
  terms: number;
  status: Record<string, number>;
  facets: number;
  rounds: number;
  items: number;
  minKappa: number | null;
  latestRound: string | null;
};
export type DomainSummary = {
  id: string;
  title: string;
  oneLine: string;
  plain: string;
  status: string;
  statusWord: string;
  counts: Counts;
  path: string;
  facets: FacetSummary[];
};
export type DocEntry = { path: string; title: string; oneLine: string };
export type SourceEntry = { slug: string; title: string; source: string; type: string; access: string; read: string; stored: string[] };
export type Index = {
  repo: string;
  commit: string;
  short: string;
  date: string;
  readme: { oneLine: string; intro: string };
  domains: DomainSummary[];
  topDocs: DocEntry[];
  designDocs: DocEntry[];
  sources: SourceEntry[];
  docs: string[];
  problems: string[];
};

export type Term = {
  id: string;
  label: string;
  section: string;
  fields: Record<string, string>;
  order: string[];
  prose: string;
  status: string;
  kind: string;
  broader: string[];
  related: string[];
  facets: string[];
  replacedBy: string[];
  aliases: string[];
  narrower: string[];
  items: string[];
  changelog: number[];
  placed: { round: string; item: string; facet: string; unanimous: boolean }[];
};
export type Facet = {
  id: string;
  label: string;
  set: string;
  fields: Record<string, string>;
  order: string[];
  prose: string;
  values: string[];
  inUse: boolean;
  unsorted: string[];
};
export type Item = {
  id: string;
  item: string;
  from: string;
  set: string;
  docs: string[];
  terms: string[];
  rounds: string[];
  unsortedIn: string[];
};
export type Kappa = { facet: string; n: number; agreement?: number | null; kappa?: number | null; measure?: string };
export type Round = {
  id: string;
  path: string;
  title: string;
  oneLine: string;
  docs: string[];
  files: string[];
  items: { id: string; item: string; from: string }[];
  raters: { name: string; file: string; rows: number }[];
  facets: string[];
  answers: Record<string, Record<string, Record<string, string>>>;
  notes: Record<string, Record<string, string>>;
  kappa: Kappa[];
  pairs: { a: string; b: string; facet: string; agreement: number | null; kappa: number | null }[];
  disagreements: { item: string; facet: string; answers: Record<string, string> }[];
};
export type Domain = Omit<DomainSummary, "facets"> & {
  glossaryIntro: string;
  facetsIntro: string;
  docs: string[];
  files: string[];
  terms: Record<string, Term>;
  facets: Facet[];
  changelog: { date: string; text: string }[];
  items: Record<string, Item>;
  rounds: Round[];
};

export const useIndex = () =>
  useLoad({ queryKey: ["index"], queryFn: () => fetchJson<Index>("data/index.json"), staleTime: Infinity });

export const useDomain = (id: string) =>
  useLoad({ queryKey: ["domain", id], queryFn: () => fetchJson<Domain>(`data/domain/${id}.json`), staleTime: Infinity });

export const useRaw = (path: string) =>
  useLoad({
    queryKey: ["raw", path],
    queryFn: async () => {
      const r = await fetch(`raw/${path}`);
      if (!r.ok) throw new Error(r.status === 404 ? `There is no page for ${path} on this site.` : `${path} could not be read (${r.status}).`);
      return r.text();
    },
    staleTime: Infinity,
  });

/** The index, once loaded, for pages that need the commit and the doc list to resolve links. */
export const IndexContext = createContext<Index | null>(null);
export const useIndexData = () => useContext(IndexContext)!;

/** Link context for Markdown from `base`, with term and item ids of `domain` turned into links. */
export function useLinks(base: string, domain?: Domain): LinkContext {
  const index = useIndexData();
  const docs = useMemo(() => new Set(index.docs), [index]);
  return useMemo(
    () => ({
      base,
      docs,
      commit: index.commit,
      repo: index.repo,
      code: domain
        ? (text: string) => {
            if (domain.terms[text]) return `#/d/${domain.id}/term/${text}`;
            if (domain.items[text]) return `#/d/${domain.id}/item/${text}`;
            if (domain.facets.some((f) => f.id === text && f.inUse)) return `#/d/${domain.id}/facet/${text}`;
            const x = text.match(/^([\w-]+):([\w-]+)$/);
            if (x && index.domains.some((d) => d.id === x[1])) return `#/d/${x[1]}/term/${x[2]}`;
            return null;
          }
        : undefined,
    }),
    [base, docs, index, domain],
  );
}

export const pct = (n: number | null | undefined) => (n == null ? "–" : `${Math.round(n * 100)}%`);
export const kap = (n: number | null | undefined) => (n == null ? "–" : n.toFixed(2));
export const githubBlob = (index: Index, path: string) => `https://github.com/${index.repo}/blob/${index.commit || "main"}/${path}`;

/** Markdown to plain text, for card descriptions: links keep their text, code and emphasis lose their marks. */
export const plainText = (md: string) =>
  cap(
    md
      .replace(/\[([^\]]+)\]\([^)]*\)/g, "$1")
      .replace(/\[([^\]]+)\]\[[^\]]*\]/g, "$1")
      .replace(/[`*]/g, "")
      .replace(/(^|\W)_([^_]+)_(?=\W|$)/g, "$1$2"),
  );
export const cap = (s: string) => (s ? s[0].toUpperCase() + s.slice(1) : s);
