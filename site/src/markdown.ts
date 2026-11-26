// A small Markdown renderer for the repo's own docs: headings with GitHub's anchor ids,
// paragraphs, nested lists, pipe tables, fenced code, block quotes, rules, and inline
// code, bold, italic, links (inline and reference-style). Written here rather than taken
// from a library so links can be resolved to the site's own pages (a doc, a term, a
// round, a source) and so the site adds no dependency beyond strata-react's stack.
// Everything is escaped first; no HTML in the source is passed through.

export type LinkContext = {
  /** Repo path of the file the Markdown came from, for resolving relative links. */
  base: string;
  /** Every Markdown path the site has a page for. */
  docs: ReadonlySet<string>;
  /** Commit the site was built from, for links to files the site does not show. */
  commit: string;
  repo: string;
  /** Turns an inline code span into a link when it names something the site has a page for (a term id, an item id). */
  code?: (text: string) => string | null;
};

const esc = (s: string) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

/** GitHub's heading anchor: lower case, punctuation dropped, spaces to hyphens. */
export function slug(text: string): string {
  return text
    .toLowerCase()
    .replace(/<[^>]+>/g, "")
    .replace(/[^\p{L}\p{N}\s_-]/gu, "")
    .trim()
    .replace(/\s/g, "-");
}

function joinPath(dir: string, rel: string): string {
  const parts = (dir ? dir.split("/") : []).concat(rel.split("/"));
  const out: string[] = [];
  for (const p of parts) {
    if (p === "" || p === ".") continue;
    if (p === "..") out.pop();
    else out.push(p);
  }
  return out.join("/");
}

export function dirOf(path: string): string {
  const i = path.lastIndexOf("/");
  return i < 0 ? "" : path.slice(0, i);
}

/** Where a link in the repo's Markdown should go on this site. External links stay as they are. */
export function resolveHref(href: string, ctx: LinkContext): { href: string; external: boolean } {
  if (/^[a-z]+:/i.test(href) || href.startsWith("//")) return { href, external: true };
  const [pathPart, anchor = ""] = href.split("#");
  const a = anchor ? `?a=${encodeURIComponent(anchor)}` : "";
  if (!pathPart) return { href: `#/doc/${ctx.base}${a}`, external: false };
  const isDir = pathPart.endsWith("/");
  const target = joinPath(dirOf(ctx.base), pathPart);
  const route = routeForPath(target, isDir, ctx.docs);
  if (route) return { href: `#${route}${a}`, external: false };
  const kind = isDir || !/\.[a-z0-9]+$/i.test(target) ? "tree" : "blob";
  return { href: `https://github.com/${ctx.repo}/${kind}/${ctx.commit || "main"}/${target}${anchor ? "#" + anchor : ""}`, external: true };
}

/** The site route for a repo path, or null when the site has no page for it. */
export function routeForPath(target: string, isDir: boolean, docs: ReadonlySet<string>): string | null {
  const clean = target.replace(/\/$/, "");
  const dm = clean.match(/^domains\/([\w-]+)(?:\/(.*))?$/);
  if (dm) {
    const [, d, rest = ""] = dm;
    if (rest === "" ) return `/d/${d}`;
    const rm = rest.match(/^rounds\/([\w-]+)(?:\/README\.md)?$/);
    if (rm) return `/d/${d}/round/${rm[1]}`;
    if (rest === "glossary.md") return `/d/${d}?tab=glossary`;
    if (rest === "facets.md") return `/d/${d}?tab=facets`;
    if (rest.endsWith(".csv")) return `/file/${clean}`;
  }
  if (docs.has(clean)) return `/doc/${clean}`;
  if ((isDir || !/\.[a-z0-9]+$/i.test(clean)) && docs.has(`${clean}/README.md`)) return `/doc/${clean}/README.md`;
  return null;
}

type Refs = Map<string, string>;

function inline(src: string, ctx: LinkContext, refs: Refs): string {
  // Pull code spans out first so nothing inside them is formatted.
  const codes: string[] = [];
  let s = src.replace(/(`+)([\s\S]*?[^`])\1(?!`)/g, (_, _t, c: string) => {
    const text = c.trim();
    const to = ctx.code?.(text);
    const html = to ? `<a href="${esc(to)}"><code>${esc(text)}</code></a>` : `<code>${esc(text)}</code>`;
    codes.push(html);
    return `\u0000${codes.length - 1}\u0000`;
  });
  s = esc(s);
  const link = (text: string, url: string) => {
    const r = resolveHref(url.replace(/&amp;/g, "&"), ctx);
    const ext = r.external ? ` target="_blank" rel="noreferrer"` : "";
    return `<a href="${esc(r.href)}"${ext}>${text}</a>`;
  };
  // images become links: the site does not copy pictures
  s = s.replace(/!\[([^\]]*)\]\(([^)\s]+)(?:\s+&quot;[^&]*&quot;)?\)/g, (_, t, u) => link(t || u, u));
  s = s.replace(/\[([^\]]+)\]\(([^)\s]+)(?:\s+&quot;[^&]*&quot;)?\)/g, (_, t, u) => link(t, u));
  s = s.replace(/\[([^\]]+)\]\[([^\]]*)\]/g, (m, t, r) => {
    const u = refs.get((r || t).toLowerCase());
    return u ? link(t, u) : m;
  });
  s = s.replace(/&lt;(https?:\/\/[^\s&]+)&gt;/g, (_, u) => link(u, u));
  s = s.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  s = s.replace(/(^|[^\w*])\*([^*\s][^*]*?)\*(?!\w)/g, "$1<em>$2</em>");
  s = s.replace(/(^|[^\w])_([^_\s][^_]*?)_(?!\w)/g, "$1<em>$2</em>");
  s = s.replace(/\u0000(\d+)\u0000/g, (_, i) => codes[Number(i)]);
  return s;
}

function splitRow(line: string): string[] {
  const t = line.trim().replace(/^\|/, "").replace(/\|$/, "");
  const cells: string[] = [];
  let cur = "", inCode = false;
  for (let i = 0; i < t.length; i++) {
    const c = t[i];
    if (c === "`") inCode = !inCode;
    if (c === "\\" && t[i + 1] === "|") { cur += "|"; i++; continue; }
    if (c === "|" && !inCode) { cells.push(cur.trim()); cur = ""; continue; }
    cur += c;
  }
  cells.push(cur.trim());
  return cells;
}

const isTableSep = (l: string) => /^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$/.test(l);
const listRe = /^(\s*)([-*+]|\d+[.)])\s+(.*)$/;

export function renderMarkdown(md: string, ctx: LinkContext): string {
  const refs: Refs = new Map();
  const lines = md.replace(/\r\n?/g, "\n").split("\n").filter((l) => {
    const m = l.match(/^\s{0,3}\[([^\]]+)\]:\s*(\S+)/);
    if (m) { refs.set(m[1].toLowerCase(), m[2]); return false; }
    return true;
  });
  return blocks(lines, ctx, refs);
}

function blocks(lines: string[], ctx: LinkContext, refs: Refs): string {
  const out: string[] = [];
  let i = 0;
  const seen = new Map<string, number>();
  while (i < lines.length) {
    const line = lines[i];
    if (!line.trim()) { i++; continue; }
    const fence = line.match(/^\s*(```+|~~~+)\s*([\w-]*)/);
    if (fence) {
      const body: string[] = [];
      i++;
      while (i < lines.length && !lines[i].trim().startsWith(fence[1])) body.push(lines[i++]);
      i++;
      out.push(`<pre><code>${esc(body.join("\n"))}</code></pre>`);
      continue;
    }
    const h = line.match(/^(#{1,6})\s+(.*?)\s*#*\s*$/);
    if (h) {
      const level = h[1].length;
      const html = inline(h[2], ctx, refs);
      let id = slug(h[2].replace(/`/g, "").replace(/\[([^\]]+)\]\([^)]*\)/g, "$1"));
      const n = seen.get(id) ?? 0;
      seen.set(id, n + 1);
      if (n) id = `${id}-${n}`;
      out.push(`<h${level} id="${esc(id)}">${html}</h${level}>`);
      i++;
      continue;
    }
    if (/^\s*([-*_])\s*(\1\s*){2,}$/.test(line)) { out.push("<hr>"); i++; continue; }
    if (line.trim().startsWith("|") && i + 1 < lines.length && isTableSep(lines[i + 1])) {
      const head = splitRow(line);
      const align = splitRow(lines[i + 1]).map((c) => (c.endsWith(":") ? (c.startsWith(":") ? "center" : "right") : ""));
      i += 2;
      const rows: string[][] = [];
      while (i < lines.length && lines[i].trim().startsWith("|")) rows.push(splitRow(lines[i++]));
      const cell = (tag: string, c: string, j: number) => `<${tag}${align[j] ? ` style="text-align:${align[j]}"` : ""}>${inline(c, ctx, refs)}</${tag}>`;
      out.push(
        `<div class="md-table"><table><thead><tr>${head.map((c, j) => cell("th", c, j)).join("")}</tr></thead><tbody>${rows
          .map((r) => `<tr>${r.map((c, j) => cell("td", c, j)).join("")}</tr>`)
          .join("")}</tbody></table></div>`,
      );
      continue;
    }
    if (/^\s*>/.test(line)) {
      const body: string[] = [];
      while (i < lines.length && /^\s*>/.test(lines[i])) body.push(lines[i++].replace(/^\s*>\s?/, ""));
      out.push(`<blockquote>${blocks(body, ctx, refs)}</blockquote>`);
      continue;
    }
    const lm = line.match(listRe);
    if (lm) {
      const indent = lm[1].length;
      const ordered = /\d/.test(lm[2]);
      const items: string[][] = [];
      while (i < lines.length) {
        const l = lines[i];
        const m = l.match(listRe);
        if (m && m[1].length === indent) { items.push([m[3]]); i++; continue; }
        if (!l.trim()) {
          // a blank line inside a list continues it only when the next line is indented or another item
          const next = lines[i + 1] ?? "";
          const nm = next.match(listRe);
          if ((nm && nm[1].length >= indent) || (next.trim() && /^\s+/.test(next) && next.search(/\S/) > indent)) { items[items.length - 1].push(""); i++; continue; }
          break;
        }
        if (l.search(/\S/) > indent && items.length) { items[items.length - 1].push(l.slice(Math.min(l.search(/\S/), indent + 2))); i++; continue; }
        if (!m && items.length && !/^\s*(#|\|)/.test(l)) { items[items.length - 1].push(l.trim()); i++; continue; }
        break;
      }
      const start = ordered ? Number(lm[2].replace(/\D/g, "")) : 1;
      const tag = ordered ? "ol" : "ul";
      out.push(
        `<${tag}${ordered && start !== 1 ? ` start="${start}"` : ""}>${items
          .map((it) => {
            const [first, ...rest] = it;
            const sub = rest.some((r) => r.trim()) ? blocks(rest, ctx, refs) : "";
            return `<li>${inline(first, ctx, refs)}${sub}</li>`;
          })
          .join("")}</${tag}>`,
      );
      continue;
    }
    const para: string[] = [];
    while (
      i < lines.length && lines[i].trim() && !/^(#{1,6})\s/.test(lines[i]) && !/^\s*(```|~~~)/.test(lines[i]) &&
      !(lines[i].trim().startsWith("|") && isTableSep(lines[i + 1] ?? "")) && !/^\s*>/.test(lines[i]) &&
      !(para.length && listRe.test(lines[i]))
    )
      para.push(lines[i++].trim());
    out.push(`<p>${inline(para.join(" "), ctx, refs)}</p>`);
  }
  return out.join("\n");
}

/** One line of Markdown (a field value) without a wrapping paragraph. */
export function renderInline(md: string, ctx: LinkContext): string {
  if (/\n/.test(md.trim())) return renderMarkdown(md, ctx);
  return inline(md, ctx, new Map());
}
