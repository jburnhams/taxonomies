import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";
import { colorSchemeScript } from "strata-react";

// base "./": the site is served from https://<user>.github.io/taxonomies/, and every route
// lives after the hash, so relative asset and data paths work at any depth.
export default defineConfig({
  base: "./",
  plugins: [
    tailwindcss(),
    {
      name: "color-scheme-script",
      transformIndexHtml: (html) => html.replace("%COLOR_SCHEME_SCRIPT%", colorSchemeScript()),
    },
  ],
  build: {
    outDir: "dist",
    emptyOutDir: true,
    chunkSizeWarningLimit: 1200,
    rollupOptions: {
      onwarn(warning, warn) {
        // lucide-react's "use client" lines mean nothing in a static bundle
        if (warning.code === "MODULE_LEVEL_DIRECTIVE") return;
        warn(warning);
      },
    },
  },
});
