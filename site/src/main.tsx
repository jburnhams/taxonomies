import { createRoot } from "react-dom/client";
import { createHashRouter, Outlet, RouterProvider, ScrollRestoration } from "react-router";
import { AppShell, ColorSchemeChoice, StrataQueryProvider, ThemeProvider } from "strata-react";
import type { NavItem } from "strata-react";
import "./app.css";
import { IndexContext, useIndex } from "./data";
import { Loaded } from "./parts";
import { Overview } from "./pages/overview";
import { DomainPage } from "./pages/domain";
import { FacetPage, ItemPage, RoundPage, TermPage } from "./pages/evidence";
import { DocPage, FilePage, SourcesPage } from "./pages/docs";

// The question this site answers: "what words does each domain use, and what decided each one?"
function Root() {
  const load = useIndex();
  return (
    <Loaded state={load}>
      {(index) => {
        const nav: NavItem[] = [
          { to: "/", label: "Overview", end: true },
          ...index.domains.map((d) => ({ to: `/d/${d.id}`, label: d.title.replace(/ taxonomy$/i, "") })),
          { to: "/doc/design/process.md", label: "Method" },
          { to: "/sources", label: "Sources" },
        ];
        return (
          <IndexContext.Provider value={index}>
            <AppShell product="Taxonomies" nav={nav} navLabel="Sections" topBar={<ColorSchemeChoice compact />}>
              <Outlet />
            </AppShell>
            <ScrollRestoration />
          </IndexContext.Provider>
        );
      }}
    </Loaded>
  );
}

const router = createHashRouter([
  {
    path: "/",
    element: <Root />,
    children: [
      { index: true, element: <Overview /> },
      { path: "d/:domain", element: <DomainPage /> },
      { path: "d/:domain/facet/:facet", element: <FacetPage /> },
      { path: "d/:domain/term/:term", element: <TermPage /> },
      { path: "d/:domain/round/:round", element: <RoundPage /> },
      { path: "d/:domain/item/:item", element: <ItemPage /> },
      { path: "doc/*", element: <DocPage /> },
      { path: "file/*", element: <FilePage /> },
      { path: "sources", element: <SourcesPage /> },
    ],
  },
]);

createRoot(document.getElementById("root")!).render(
  <ThemeProvider>
    <StrataQueryProvider>
      <RouterProvider router={router} />
    </StrataQueryProvider>
  </ThemeProvider>,
);
