# Apex-Artifacts — Design Token Sets

Six substitutable design token sets, each as CSS custom properties.
Pick deliberately per artifact. See `references/design-tokens.md`
in the core references bundle for the platter principle.

## Sets in this bundle

- `tokens/sets/tokens-default-cool.css`
- `tokens/sets/tokens-ft-salmon.css`
- `tokens/sets/tokens-penguin-classic.css`
- `tokens/sets/tokens-quanta-cobalt.css`
- `tokens/sets/tokens-scandi-fog.css`
- `tokens/sets/tokens-ukiyo-e.css`

Plus the DTCG-format JSON source (`tokens/tokens.json`).

---


## `tokens/sets/tokens-default-cool.css`

```css
/* ============================================================
 * Token set: default-cool
 *
 * The original cool-slate baseline. Renamed from tokens/tokens.css
 * during Wave 1 (Item 2.1) so the 5 substitutable sets can sit
 * alongside it under tokens/sets/. The historical file
 * tokens/tokens.css remains in place (it scopes the same values to
 * a bare :root, for artifacts that don't yet opt into the
 * data-token-set selector). This file is the *registered* form,
 * scoped so an artifact can switch sets purely by toggling an
 * attribute.
 *
 * Activate on any artifact root with:
 *   <html data-token-set="default-cool">
 * or apply to a subtree:
 *   <div data-token-set="default-cool"> … </div>
 * ============================================================ */

:root[data-token-set="default-cool"] {
  color-scheme: light dark;

  /* ---- font families ---- */
  --font-sans:  "Inter Tight", "Inter", -apple-system, system-ui, sans-serif;
  --font-serif: "Fraunces", "Source Serif Pro", Georgia, serif;
  --font-mono:  "JetBrains Mono", "IBM Plex Mono", ui-monospace, monospace;

  /* ---- font sizes ---- */
  --fs-caption: 0.64rem;
  --fs-body-sm: 0.8rem;
  --fs-body:    1rem;
  --fs-body-lg: 1.25rem;
  --fs-h4:      1.563rem;
  --fs-h3:      1.953rem;
  --fs-h2:      2.441rem;
  --fs-h1:      3.052rem;
  --fs-display: 3.815rem;

  /* ---- font weights ---- */
  --fw-regular:  400;
  --fw-medium:   500;
  --fw-semibold: 600;
  --fw-bold:     700;

  /* ---- neutrals (cool slate) ---- */
  --n-50:  oklch(98% 0.004 240);
  --n-100: oklch(95% 0.008 240);
  --n-200: oklch(90% 0.012 240);
  --n-300: oklch(80% 0.018 240);
  --n-400: oklch(65% 0.022 240);
  --n-500: oklch(50% 0.025 240);
  --n-600: oklch(38% 0.024 240);
  --n-700: oklch(28% 0.020 240);
  --n-800: oklch(20% 0.016 240);
  --n-900: oklch(13% 0.012 240);

  /* ---- accent (default: ink) ---- */
  --accent:      oklch(45% 0.18 250);
  --accent-soft: oklch(92% 0.04 250);

  /* ---- semantic ---- */
  --success: oklch(55% 0.14 150);
  --warning: oklch(75% 0.17 75);
  --danger:  oklch(55% 0.20 25);
  --info:    oklch(60% 0.14 230);

  /* ---- chart palette ---- */
  --chart-1: oklch(55% 0.18 250);
  --chart-2: oklch(60% 0.18 30);
  --chart-3: oklch(65% 0.15 130);
  --chart-4: oklch(55% 0.15 300);
  --chart-5: oklch(70% 0.15 75);
  --chart-6: oklch(50% 0.10 200);
  --chart-7: oklch(45% 0.14 340);
  --chart-8: oklch(35% 0.02 240);

  /* ---- spacing (4-px base) ---- */
  --s-0:  0;
  --s-1:  0.25rem;
  --s-2:  0.5rem;
  --s-3:  0.75rem;
  --s-4:  1rem;
  --s-6:  1.5rem;
  --s-8:  2rem;
  --s-12: 3rem;
  --s-16: 4rem;
  --s-24: 6rem;

  /* ---- radius ---- */
  --r-none: 0;
  --r-sm:   4px;
  --r-md:   8px;
  --r-lg:   16px;
  --r-pill: 9999px;

  /* ---- shadow ---- */
  --sh-sm: 0 1px 2px rgb(15 23 42 / 0.04), 0 1px 3px rgb(15 23 42 / 0.06);
  --sh-md: 0 4px 8px rgb(15 23 42 / 0.04), 0 2px 4px rgb(15 23 42 / 0.06);
  --sh-lg: 0 12px 24px rgb(15 23 42 / 0.06), 0 4px 8px rgb(15 23 42 / 0.08);
  --sh-xl: 0 24px 48px rgb(15 23 42 / 0.08), 0 8px 16px rgb(15 23 42 / 0.10);

  /* ---- motion ---- */
  --dur-micro:      120ms;
  --dur-transition: 240ms;
  --dur-emphasis:   480ms;
  --dur-narrative:  960ms;

  --ease-standard: cubic-bezier(0.2, 0, 0, 1);
  --ease-enter:    cubic-bezier(0.05, 0.7, 0.1, 1);
  --ease-exit:     cubic-bezier(0.3, 0, 0.8, 0.15);

  /* ---- breakpoints ---- */
  --bp-sm: 640px;
  --bp-md: 768px;
  --bp-lg: 1024px;
  --bp-xl: 1280px;
}

/* ---- dark scheme ---- */
@media (prefers-color-scheme: dark) {
  :root[data-token-set="default-cool"] {
    --n-50:  oklch(13% 0.012 240);
    --n-100: oklch(17% 0.014 240);
    --n-200: oklch(22% 0.016 240);
    --n-300: oklch(30% 0.020 240);
    --n-400: oklch(45% 0.022 240);
    --n-500: oklch(60% 0.024 240);
    --n-600: oklch(72% 0.022 240);
    --n-700: oklch(82% 0.016 240);
    --n-800: oklch(90% 0.010 240);
    --n-900: oklch(97% 0.006 240);

    --accent:      oklch(75% 0.15 250);
    --accent-soft: oklch(28% 0.08 250);

    --success: oklch(70% 0.14 150);
    --warning: oklch(82% 0.15 75);
    --danger:  oklch(68% 0.18 25);
    --info:    oklch(72% 0.13 230);

    --sh-sm: 0 1px 2px rgb(0 0 0 / 0.3);
    --sh-md: 0 4px 8px rgb(0 0 0 / 0.4);
    --sh-lg: 0 12px 24px rgb(0 0 0 / 0.45);
    --sh-xl: 0 24px 48px rgb(0 0 0 / 0.5);
  }
}

/* ---- reduced motion ---- */
@media (prefers-reduced-motion: reduce) {
  :root[data-token-set="default-cool"] {
    --dur-micro:      0.01ms;
    --dur-transition: 0.01ms;
    --dur-emphasis:   0.01ms;
    --dur-narrative:  0.01ms;
  }
}
```

---


## `tokens/sets/tokens-ft-salmon.css`

```css
/* ============================================================
 * Token set: ft-salmon
 *
 * Generated from tokens/sets/tokens-ft-salmon.json by
 * tokens/build.mjs. Do not edit by hand — regenerate.
 *
 * Activate on any artifact root with:
     <html data-token-set="ft-salmon">
 * or apply to a subtree:
     <div data-token-set="ft-salmon"> … </div>
 * ============================================================ */

:root[data-token-set="ft-salmon"] {
  color-scheme: light;

  /* font families (recommended; substitutable) */
  --font-sans: "Inter Tight", "Inter", -apple-system, system-ui, sans-serif;
  --font-serif: "Fraunces", "Source Serif Pro", Georgia, serif;
  --font-mono: "JetBrains Mono", "IBM Plex Mono", ui-monospace, monospace;
  --font-display: "Fraunces", "Source Serif Pro", Georgia, serif;
  --font-body: "Inter", -apple-system, system-ui, sans-serif;

  /* font sizes */
  --fs-caption: 0.64rem;
  --fs-body-sm: 0.8rem;
  --fs-body: 1rem;
  --fs-body-lg: 1.25rem;
  --fs-h4: 1.563rem;
  --fs-h3: 1.953rem;
  --fs-h2: 2.441rem;
  --fs-h1: 3.052rem;
  --fs-display: 3.815rem;

  /* font weights */
  --fw-regular: 400;
  --fw-medium: 500;
  --fw-semibold: 600;
  --fw-bold: 700;

  /* line heights */
  --lh-tight: 1.1;
  --lh-snug: 1.3;
  --lh-normal: 1.6;
  --lh-relaxed: 1.75;

  /* neutral ramp (n-50 lightest → n-900 darkest) */
  --n-50: oklch(98% 0.012 50);
  --n-100: oklch(95% 0.015 50);
  --n-200: oklch(90% 0.018 45);
  --n-300: oklch(80% 0.022 40);
  --n-400: oklch(64% 0.020 35);
  --n-500: oklch(48% 0.018 280);
  --n-600: oklch(38% 0.016 260);
  --n-700: oklch(28% 0.014 250);
  --n-800: oklch(20% 0.012 250);
  --n-900: oklch(13% 0.010 250);

  /* accents */
  --accent-ink: oklch(45% 0.18 250);
  --accent-signal: oklch(55% 0.19 25);
  --accent-growth: oklch(55% 0.15 150);
  --accent-attention: oklch(72% 0.18 65);
  --accent-primary: oklch(35% 0.13 255);
  --accent-secondary: oklch(55% 0.20 25);

  /* semantic */
  --success: oklch(48% 0.13 145);
  --warning: oklch(60% 0.16 60);
  --danger: oklch(55% 0.20 25);
  --info: oklch(40% 0.14 250);
  --error: oklch(48% 0.20 25);

  /* chart categorical */
  --chart-1: oklch(35% 0.13 255);
  --chart-2: oklch(55% 0.20 25);
  --chart-3: oklch(60% 0.13 75);
  --chart-4: oklch(48% 0.13 145);
  --chart-5: oklch(45% 0.10 200);
  --chart-6: oklch(45% 0.14 320);

  /* spacing (4-px base) */
  --s-0: 0;
  --s-1: 0.25rem;
  --s-2: 0.5rem;
  --s-3: 0.75rem;
  --s-4: 1rem;
  --s-6: 1.5rem;
  --s-8: 2rem;
  --s-12: 3rem;
  --s-16: 4rem;
  --s-24: 6rem;

  /* radius */
  --r-none: 0;
  --r-sm: 4px;
  --r-md: 8px;
  --r-lg: 16px;
  --r-pill: 9999px;

  /* shadow */
  --sh-sm: 0 1px 2px rgb(15 23 42 / 0.04), 0 1px 3px rgb(15 23 42 / 0.06);
  --sh-md: 0 4px 8px rgb(15 23 42 / 0.04), 0 2px 4px rgb(15 23 42 / 0.06);
  --sh-lg: 0 12px 24px rgb(15 23 42 / 0.06), 0 4px 8px rgb(15 23 42 / 0.08);
  --sh-xl: 0 24px 48px rgb(15 23 42 / 0.08), 0 8px 16px rgb(15 23 42 / 0.10);

  /* motion */
  --dur-micro: 120ms;
  --dur-transition: 240ms;
  --dur-emphasis: 480ms;
  --dur-narrative: 960ms;
  --ease-standard: cubic-bezier(0.2, 0, 0, 1);
  --ease-enter: cubic-bezier(0.05, 0.7, 0.1, 1);
  --ease-exit: cubic-bezier(0.3, 0, 0.8, 0.15);

  /* breakpoints */
  --bp-sm: 640px;
  --bp-md: 768px;
  --bp-lg: 1024px;
  --bp-xl: 1280px;
}

@media (prefers-reduced-motion: reduce) {
  :root[data-token-set="ft-salmon"] {
    --dur-micro: 0.01ms;
    --dur-transition: 0.01ms;
    --dur-emphasis: 0.01ms;
    --dur-narrative: 0.01ms;
  }
}
```

---


## `tokens/sets/tokens-penguin-classic.css`

```css
/* ============================================================
 * Token set: penguin-classic
 *
 * Generated from tokens/sets/tokens-penguin-classic.json by
 * tokens/build.mjs. Do not edit by hand — regenerate.
 *
 * Activate on any artifact root with:
     <html data-token-set="penguin-classic">
 * or apply to a subtree:
     <div data-token-set="penguin-classic"> … </div>
 * ============================================================ */

:root[data-token-set="penguin-classic"] {
  color-scheme: light;

  /* font families (recommended; substitutable) */
  --font-sans: "Inter Tight", "Inter", -apple-system, system-ui, sans-serif;
  --font-serif: "Fraunces", "Source Serif Pro", Georgia, serif;
  --font-mono: "JetBrains Mono", "IBM Plex Mono", ui-monospace, monospace;
  --font-display: "Futura", "Inter Tight", -apple-system, system-ui, sans-serif;
  --font-body: "Sabon", "Source Serif Pro", Georgia, serif;

  /* font sizes */
  --fs-caption: 0.64rem;
  --fs-body-sm: 0.8rem;
  --fs-body: 1rem;
  --fs-body-lg: 1.25rem;
  --fs-h4: 1.563rem;
  --fs-h3: 1.953rem;
  --fs-h2: 2.441rem;
  --fs-h1: 3.052rem;
  --fs-display: 3.815rem;

  /* font weights */
  --fw-regular: 400;
  --fw-medium: 500;
  --fw-semibold: 600;
  --fw-bold: 700;

  /* line heights */
  --lh-tight: 1.1;
  --lh-snug: 1.3;
  --lh-normal: 1.6;
  --lh-relaxed: 1.75;

  /* neutral ramp (n-50 lightest → n-900 darkest) */
  --n-50: oklch(96% 0.020 85);
  --n-100: oklch(93% 0.022 85);
  --n-200: oklch(88% 0.020 80);
  --n-300: oklch(78% 0.018 75);
  --n-400: oklch(60% 0.014 70);
  --n-500: oklch(45% 0.012 65);
  --n-600: oklch(32% 0.010 60);
  --n-700: oklch(20% 0.008 50);
  --n-800: oklch(14% 0.006 50);
  --n-900: oklch(8% 0.004 50);

  /* accents */
  --accent-ink: oklch(45% 0.18 250);
  --accent-signal: oklch(55% 0.19 25);
  --accent-growth: oklch(55% 0.15 150);
  --accent-attention: oklch(72% 0.18 65);
  --accent-primary: oklch(60% 0.21 40);
  --accent-primary-strong: oklch(48% 0.18 40);
  --accent-secondary: oklch(20% 0.008 50);

  /* semantic */
  --success: oklch(42% 0.13 145);
  --warning: oklch(55% 0.16 65);
  --danger: oklch(55% 0.20 25);
  --info: oklch(38% 0.15 255);
  --error: oklch(48% 0.18 25);

  /* chart categorical */
  --chart-1: oklch(48% 0.18 40);
  --chart-2: oklch(20% 0.008 50);
  --chart-3: oklch(42% 0.13 145);
  --chart-4: oklch(38% 0.15 255);
  --chart-5: oklch(50% 0.13 320);
  --chart-6: oklch(55% 0.10 80);

  /* spacing (4-px base) */
  --s-0: 0;
  --s-1: 0.25rem;
  --s-2: 0.5rem;
  --s-3: 0.75rem;
  --s-4: 1rem;
  --s-6: 1.5rem;
  --s-8: 2rem;
  --s-12: 3rem;
  --s-16: 4rem;
  --s-24: 6rem;

  /* radius */
  --r-none: 0;
  --r-sm: 4px;
  --r-md: 8px;
  --r-lg: 16px;
  --r-pill: 9999px;

  /* shadow */
  --sh-sm: 0 1px 2px rgb(15 23 42 / 0.04), 0 1px 3px rgb(15 23 42 / 0.06);
  --sh-md: 0 4px 8px rgb(15 23 42 / 0.04), 0 2px 4px rgb(15 23 42 / 0.06);
  --sh-lg: 0 12px 24px rgb(15 23 42 / 0.06), 0 4px 8px rgb(15 23 42 / 0.08);
  --sh-xl: 0 24px 48px rgb(15 23 42 / 0.08), 0 8px 16px rgb(15 23 42 / 0.10);

  /* motion */
  --dur-micro: 120ms;
  --dur-transition: 240ms;
  --dur-emphasis: 480ms;
  --dur-narrative: 960ms;
  --ease-standard: cubic-bezier(0.2, 0, 0, 1);
  --ease-enter: cubic-bezier(0.05, 0.7, 0.1, 1);
  --ease-exit: cubic-bezier(0.3, 0, 0.8, 0.15);

  /* breakpoints */
  --bp-sm: 640px;
  --bp-md: 768px;
  --bp-lg: 1024px;
  --bp-xl: 1280px;
}

@media (prefers-reduced-motion: reduce) {
  :root[data-token-set="penguin-classic"] {
    --dur-micro: 0.01ms;
    --dur-transition: 0.01ms;
    --dur-emphasis: 0.01ms;
    --dur-narrative: 0.01ms;
  }
}
```

---


## `tokens/sets/tokens-quanta-cobalt.css`

```css
/* ============================================================
 * Token set: quanta-cobalt
 *
 * Generated from tokens/sets/tokens-quanta-cobalt.json by
 * tokens/build.mjs. Do not edit by hand — regenerate.
 *
 * Activate on any artifact root with:
     <html data-token-set="quanta-cobalt">
 * or apply to a subtree:
     <div data-token-set="quanta-cobalt"> … </div>
 * ============================================================ */

:root[data-token-set="quanta-cobalt"] {
  color-scheme: light;

  /* font families (recommended; substitutable) */
  --font-sans: "Inter Tight", "Inter", -apple-system, system-ui, sans-serif;
  --font-serif: "Source Serif Pro", "Charter", Georgia, serif;
  --font-mono: "JetBrains Mono", "IBM Plex Mono", ui-monospace, monospace;

  /* font sizes */
  --fs-caption: 0.64rem;
  --fs-body-sm: 0.8rem;
  --fs-body: 1rem;
  --fs-body-lg: 1.25rem;
  --fs-h4: 1.563rem;
  --fs-h3: 1.953rem;
  --fs-h2: 2.441rem;
  --fs-h1: 3.052rem;
  --fs-display: 3.815rem;

  /* font weights */
  --fw-regular: 400;
  --fw-medium: 500;
  --fw-semibold: 600;
  --fw-bold: 700;

  /* line heights */
  --lh-tight: 1.1;
  --lh-snug: 1.3;
  --lh-normal: 1.6;
  --lh-relaxed: 1.75;

  /* neutral ramp (n-50 lightest → n-900 darkest) */
  --n-50: oklch(99% 0.002 240);
  --n-100: oklch(97% 0.004 240);
  --n-200: oklch(92% 0.006 240);
  --n-300: oklch(84% 0.010 240);
  --n-400: oklch(66% 0.014 240);
  --n-500: oklch(48% 0.016 240);
  --n-600: oklch(36% 0.018 240);
  --n-700: oklch(25% 0.018 240);
  --n-800: oklch(17% 0.016 240);
  --n-900: oklch(10% 0.012 240);

  /* accents */
  --accent-ink: oklch(45% 0.18 250);
  --accent-signal: oklch(55% 0.19 25);
  --accent-growth: oklch(55% 0.15 150);
  --accent-attention: oklch(72% 0.18 65);
  --accent-primary: oklch(32% 0.18 265);
  --accent-secondary: oklch(60% 0.22 25);

  /* semantic */
  --success: oklch(45% 0.14 150);
  --warning: oklch(55% 0.16 70);
  --danger: oklch(55% 0.20 25);
  --info: oklch(32% 0.18 265);
  --error: oklch(48% 0.20 25);

  /* chart categorical */
  --chart-1: oklch(32% 0.18 265);
  --chart-2: oklch(55% 0.20 25);
  --chart-3: oklch(50% 0.15 145);
  --chart-4: oklch(45% 0.16 305);
  --chart-5: oklch(60% 0.13 75);
  --chart-6: oklch(42% 0.10 200);
  --chart-7: oklch(40% 0.14 340);
  --chart-8: oklch(28% 0.02 240);

  /* spacing (4-px base) */
  --s-0: 0;
  --s-1: 0.25rem;
  --s-2: 0.5rem;
  --s-3: 0.75rem;
  --s-4: 1rem;
  --s-6: 1.5rem;
  --s-8: 2rem;
  --s-12: 3rem;
  --s-16: 4rem;
  --s-24: 6rem;

  /* radius */
  --r-none: 0;
  --r-sm: 4px;
  --r-md: 8px;
  --r-lg: 16px;
  --r-pill: 9999px;

  /* shadow */
  --sh-sm: 0 1px 2px rgb(15 23 42 / 0.04), 0 1px 3px rgb(15 23 42 / 0.06);
  --sh-md: 0 4px 8px rgb(15 23 42 / 0.04), 0 2px 4px rgb(15 23 42 / 0.06);
  --sh-lg: 0 12px 24px rgb(15 23 42 / 0.06), 0 4px 8px rgb(15 23 42 / 0.08);
  --sh-xl: 0 24px 48px rgb(15 23 42 / 0.08), 0 8px 16px rgb(15 23 42 / 0.10);

  /* motion */
  --dur-micro: 120ms;
  --dur-transition: 240ms;
  --dur-emphasis: 480ms;
  --dur-narrative: 960ms;
  --ease-standard: cubic-bezier(0.2, 0, 0, 1);
  --ease-enter: cubic-bezier(0.05, 0.7, 0.1, 1);
  --ease-exit: cubic-bezier(0.3, 0, 0.8, 0.15);

  /* breakpoints */
  --bp-sm: 640px;
  --bp-md: 768px;
  --bp-lg: 1024px;
  --bp-xl: 1280px;
}

@media (prefers-reduced-motion: reduce) {
  :root[data-token-set="quanta-cobalt"] {
    --dur-micro: 0.01ms;
    --dur-transition: 0.01ms;
    --dur-emphasis: 0.01ms;
    --dur-narrative: 0.01ms;
  }
}
```

---


## `tokens/sets/tokens-scandi-fog.css`

```css
/* ============================================================
 * Token set: scandi-fog
 *
 * Generated from tokens/sets/tokens-scandi-fog.json by
 * tokens/build.mjs. Do not edit by hand — regenerate.
 *
 * Activate on any artifact root with:
     <html data-token-set="scandi-fog">
 * or apply to a subtree:
     <div data-token-set="scandi-fog"> … </div>
 * ============================================================ */

:root[data-token-set="scandi-fog"] {
  color-scheme: light;

  /* font families (recommended; substitutable) */
  --font-sans: "Söhne", "Inter Tight", "Inter", -apple-system, system-ui, sans-serif;
  --font-serif: "Tiempos Text", "Source Serif Pro", Georgia, serif;
  --font-mono: "JetBrains Mono", "IBM Plex Mono", ui-monospace, monospace;

  /* font sizes */
  --fs-caption: 0.64rem;
  --fs-body-sm: 0.8rem;
  --fs-body: 1rem;
  --fs-body-lg: 1.25rem;
  --fs-h4: 1.563rem;
  --fs-h3: 1.953rem;
  --fs-h2: 2.441rem;
  --fs-h1: 3.052rem;
  --fs-display: 3.815rem;

  /* font weights */
  --fw-regular: 400;
  --fw-medium: 500;
  --fw-semibold: 600;
  --fw-bold: 700;

  /* line heights */
  --lh-tight: 1.1;
  --lh-snug: 1.3;
  --lh-normal: 1.6;
  --lh-relaxed: 1.75;

  /* neutral ramp (n-50 lightest → n-900 darkest) */
  --n-50: oklch(97% 0.008 230);
  --n-100: oklch(94% 0.010 230);
  --n-200: oklch(89% 0.012 232);
  --n-300: oklch(80% 0.014 235);
  --n-400: oklch(64% 0.014 238);
  --n-500: oklch(48% 0.013 240);
  --n-600: oklch(38% 0.013 240);
  --n-700: oklch(28% 0.012 240);
  --n-800: oklch(20% 0.010 240);
  --n-900: oklch(13% 0.008 240);

  /* accents */
  --accent-ink: oklch(45% 0.18 250);
  --accent-signal: oklch(55% 0.19 25);
  --accent-growth: oklch(55% 0.15 150);
  --accent-attention: oklch(72% 0.18 65);
  --accent-primary: oklch(42% 0.10 150);
  --accent-secondary: oklch(35% 0.14 340);

  /* semantic */
  --success: oklch(42% 0.10 150);
  --warning: oklch(58% 0.14 70);
  --danger: oklch(55% 0.20 25);
  --info: oklch(40% 0.12 240);
  --error: oklch(46% 0.17 28);

  /* chart categorical */
  --chart-1: oklch(42% 0.10 150);
  --chart-2: oklch(35% 0.14 340);
  --chart-3: oklch(40% 0.12 240);
  --chart-4: oklch(58% 0.13 70);
  --chart-5: oklch(46% 0.10 200);
  --chart-6: oklch(50% 0.12 30);
  --chart-7: oklch(28% 0.012 240);

  /* spacing (4-px base) */
  --s-0: 0;
  --s-1: 0.25rem;
  --s-2: 0.5rem;
  --s-3: 0.75rem;
  --s-4: 1rem;
  --s-6: 1.5rem;
  --s-8: 2rem;
  --s-12: 3rem;
  --s-16: 4rem;
  --s-24: 6rem;

  /* radius */
  --r-none: 0;
  --r-sm: 4px;
  --r-md: 8px;
  --r-lg: 16px;
  --r-pill: 9999px;

  /* shadow */
  --sh-sm: 0 1px 2px rgb(15 23 42 / 0.04), 0 1px 3px rgb(15 23 42 / 0.06);
  --sh-md: 0 4px 8px rgb(15 23 42 / 0.04), 0 2px 4px rgb(15 23 42 / 0.06);
  --sh-lg: 0 12px 24px rgb(15 23 42 / 0.06), 0 4px 8px rgb(15 23 42 / 0.08);
  --sh-xl: 0 24px 48px rgb(15 23 42 / 0.08), 0 8px 16px rgb(15 23 42 / 0.10);

  /* motion */
  --dur-micro: 120ms;
  --dur-transition: 240ms;
  --dur-emphasis: 480ms;
  --dur-narrative: 960ms;
  --ease-standard: cubic-bezier(0.2, 0, 0, 1);
  --ease-enter: cubic-bezier(0.05, 0.7, 0.1, 1);
  --ease-exit: cubic-bezier(0.3, 0, 0.8, 0.15);

  /* breakpoints */
  --bp-sm: 640px;
  --bp-md: 768px;
  --bp-lg: 1024px;
  --bp-xl: 1280px;
}

@media (prefers-reduced-motion: reduce) {
  :root[data-token-set="scandi-fog"] {
    --dur-micro: 0.01ms;
    --dur-transition: 0.01ms;
    --dur-emphasis: 0.01ms;
    --dur-narrative: 0.01ms;
  }
}
```

---


## `tokens/sets/tokens-ukiyo-e.css`

```css
/* ============================================================
 * Token set: ukiyo-e
 *
 * Generated from tokens/sets/tokens-ukiyo-e.json by
 * tokens/build.mjs. Do not edit by hand — regenerate.
 *
 * Activate on any artifact root with:
     <html data-token-set="ukiyo-e">
 * or apply to a subtree:
     <div data-token-set="ukiyo-e"> … </div>
 * ============================================================ */

:root[data-token-set="ukiyo-e"] {
  color-scheme: light;

  /* font families (recommended; substitutable) */
  --font-sans: "Inter Tight", "Inter", -apple-system, system-ui, sans-serif;
  --font-serif: "Fraunces", "Noto Serif JP", Georgia, serif;
  --font-mono: "JetBrains Mono", "IBM Plex Mono", ui-monospace, monospace;
  --font-display: "Noto Serif JP", "Fraunces", "Source Serif Pro", Georgia, serif;
  --font-body: "Noto Sans JP", "Inter", -apple-system, system-ui, sans-serif;

  /* font sizes */
  --fs-caption: 0.64rem;
  --fs-body-sm: 0.8rem;
  --fs-body: 1rem;
  --fs-body-lg: 1.25rem;
  --fs-h4: 1.563rem;
  --fs-h3: 1.953rem;
  --fs-h2: 2.441rem;
  --fs-h1: 3.052rem;
  --fs-display: 3.815rem;

  /* font weights */
  --fw-regular: 400;
  --fw-medium: 500;
  --fw-semibold: 600;
  --fw-bold: 700;

  /* line heights */
  --lh-tight: 1.1;
  --lh-snug: 1.3;
  --lh-normal: 1.6;
  --lh-relaxed: 1.75;

  /* neutral ramp (n-50 lightest → n-900 darkest) */
  --n-50: oklch(96% 0.012 80);
  --n-100: oklch(93% 0.014 80);
  --n-200: oklch(88% 0.014 75);
  --n-300: oklch(78% 0.014 70);
  --n-400: oklch(60% 0.012 260);
  --n-500: oklch(45% 0.012 255);
  --n-600: oklch(32% 0.010 252);
  --n-700: oklch(22% 0.008 250);
  --n-800: oklch(15% 0.006 250);
  --n-900: oklch(9% 0.004 250);

  /* accents */
  --accent-ink: oklch(45% 0.18 250);
  --accent-signal: oklch(55% 0.19 25);
  --accent-growth: oklch(55% 0.15 150);
  --accent-attention: oklch(72% 0.18 65);
  --accent-primary: oklch(35% 0.16 255);
  --accent-secondary: oklch(55% 0.21 30);
  --accent-tertiary: oklch(72% 0.14 90);

  /* semantic */
  --success: oklch(45% 0.12 150);
  --warning: oklch(58% 0.16 65);
  --danger: oklch(55% 0.20 25);
  --info: oklch(35% 0.16 255);
  --error: oklch(50% 0.20 28);

  /* chart categorical */
  --chart-1: oklch(35% 0.16 255);
  --chart-2: oklch(55% 0.21 30);
  --chart-3: oklch(45% 0.12 150);
  --chart-4: oklch(40% 0.14 320);
  --chart-5: oklch(60% 0.12 85);
  --chart-6: oklch(38% 0.10 200);
  --chart-7: oklch(22% 0.008 250);

  /* spacing (4-px base) */
  --s-0: 0;
  --s-1: 0.25rem;
  --s-2: 0.5rem;
  --s-3: 0.75rem;
  --s-4: 1rem;
  --s-6: 1.5rem;
  --s-8: 2rem;
  --s-12: 3rem;
  --s-16: 4rem;
  --s-24: 6rem;

  /* radius */
  --r-none: 0;
  --r-sm: 4px;
  --r-md: 8px;
  --r-lg: 16px;
  --r-pill: 9999px;

  /* shadow */
  --sh-sm: 0 1px 2px rgb(15 23 42 / 0.04), 0 1px 3px rgb(15 23 42 / 0.06);
  --sh-md: 0 4px 8px rgb(15 23 42 / 0.04), 0 2px 4px rgb(15 23 42 / 0.06);
  --sh-lg: 0 12px 24px rgb(15 23 42 / 0.06), 0 4px 8px rgb(15 23 42 / 0.08);
  --sh-xl: 0 24px 48px rgb(15 23 42 / 0.08), 0 8px 16px rgb(15 23 42 / 0.10);

  /* motion */
  --dur-micro: 120ms;
  --dur-transition: 240ms;
  --dur-emphasis: 480ms;
  --dur-narrative: 960ms;
  --ease-standard: cubic-bezier(0.2, 0, 0, 1);
  --ease-enter: cubic-bezier(0.05, 0.7, 0.1, 1);
  --ease-exit: cubic-bezier(0.3, 0, 0.8, 0.15);

  /* breakpoints */
  --bp-sm: 640px;
  --bp-md: 768px;
  --bp-lg: 1024px;
  --bp-xl: 1280px;
}

@media (prefers-reduced-motion: reduce) {
  :root[data-token-set="ukiyo-e"] {
    --dur-micro: 0.01ms;
    --dur-transition: 0.01ms;
    --dur-emphasis: 0.01ms;
    --dur-narrative: 0.01ms;
  }
}
```

---


## `tokens/tokens.json` (DTCG source)

```json
{
  "$schema": "https://design-tokens.github.io/community-group/format/",
  "$description": "Apex-artifact design tokens. Style-Dictionary-compatible. See references/design-tokens.md for rationale and usage.",
  "$version": "1.0.0",

  "font": {
    "family": {
      "sans":  { "$value": "\"Inter Tight\", \"Inter\", -apple-system, system-ui, sans-serif", "$type": "fontFamily" },
      "serif": { "$value": "\"Fraunces\", \"Source Serif Pro\", Georgia, serif",               "$type": "fontFamily" },
      "mono":  { "$value": "\"JetBrains Mono\", \"IBM Plex Mono\", ui-monospace, monospace",   "$type": "fontFamily" }
    },
    "weight": {
      "regular":  { "$value": 400, "$type": "fontWeight" },
      "medium":   { "$value": 500, "$type": "fontWeight" },
      "semibold": { "$value": 600, "$type": "fontWeight" },
      "bold":     { "$value": 700, "$type": "fontWeight" }
    },
    "size": {
      "caption":  { "$value": "0.64rem", "$type": "dimension" },
      "bodySm":   { "$value": "0.8rem",  "$type": "dimension" },
      "body":     { "$value": "1rem",    "$type": "dimension" },
      "bodyLg":   { "$value": "1.25rem", "$type": "dimension" },
      "h4":       { "$value": "1.563rem","$type": "dimension" },
      "h3":       { "$value": "1.953rem","$type": "dimension" },
      "h2":       { "$value": "2.441rem","$type": "dimension" },
      "h1":       { "$value": "3.052rem","$type": "dimension" },
      "display":  { "$value": "3.815rem","$type": "dimension" }
    },
    "lineHeight": {
      "tight":   { "$value": 1.1,  "$type": "number" },
      "snug":    { "$value": 1.3,  "$type": "number" },
      "normal":  { "$value": 1.6,  "$type": "number" },
      "relaxed": { "$value": 1.75, "$type": "number" }
    }
  },

  "color": {
    "neutral": {
      "warm": {
        "50":  { "$value": "oklch(98% 0.004 80)", "$type": "color" },
        "100": { "$value": "oklch(96% 0.006 80)", "$type": "color" },
        "200": { "$value": "oklch(92% 0.009 80)", "$type": "color" },
        "300": { "$value": "oklch(85% 0.012 80)", "$type": "color" },
        "400": { "$value": "oklch(68% 0.015 80)", "$type": "color" },
        "500": { "$value": "oklch(52% 0.015 80)", "$type": "color" },
        "600": { "$value": "oklch(40% 0.014 80)", "$type": "color" },
        "700": { "$value": "oklch(30% 0.012 80)", "$type": "color" },
        "800": { "$value": "oklch(22% 0.010 80)", "$type": "color" },
        "900": { "$value": "oklch(15% 0.008 80)", "$type": "color" }
      },
      "cool": {
        "50":  { "$value": "oklch(98% 0.004 240)", "$type": "color" },
        "100": { "$value": "oklch(95% 0.008 240)", "$type": "color" },
        "200": { "$value": "oklch(90% 0.012 240)", "$type": "color" },
        "300": { "$value": "oklch(80% 0.018 240)", "$type": "color" },
        "400": { "$value": "oklch(65% 0.022 240)", "$type": "color" },
        "500": { "$value": "oklch(50% 0.025 240)", "$type": "color" },
        "600": { "$value": "oklch(38% 0.024 240)", "$type": "color" },
        "700": { "$value": "oklch(28% 0.020 240)", "$type": "color" },
        "800": { "$value": "oklch(20% 0.016 240)", "$type": "color" },
        "900": { "$value": "oklch(13% 0.012 240)", "$type": "color" }
      }
    },
    "accent": {
      "ink":       { "$value": "oklch(45% 0.18 250)", "$type": "color", "$description": "Confident blue" },
      "signal":    { "$value": "oklch(55% 0.19 25)",  "$type": "color", "$description": "Confident red" },
      "growth":    { "$value": "oklch(55% 0.15 150)", "$type": "color", "$description": "Confident green" },
      "attention": { "$value": "oklch(72% 0.18 65)",  "$type": "color", "$description": "Confident amber" }
    },
    "semantic": {
      "success": { "$value": "oklch(55% 0.14 150)", "$type": "color" },
      "warning": { "$value": "oklch(75% 0.17 75)",  "$type": "color" },
      "danger":  { "$value": "oklch(55% 0.20 25)",  "$type": "color" },
      "info":    { "$value": "oklch(60% 0.14 230)", "$type": "color" }
    },
    "chart": {
      "categorical": {
        "c1": { "$value": "oklch(55% 0.18 250)", "$type": "color", "$description": "blue" },
        "c2": { "$value": "oklch(60% 0.18 30)",  "$type": "color", "$description": "vermilion" },
        "c3": { "$value": "oklch(65% 0.15 130)", "$type": "color", "$description": "olive-green" },
        "c4": { "$value": "oklch(55% 0.15 300)", "$type": "color", "$description": "violet" },
        "c5": { "$value": "oklch(70% 0.15 75)",  "$type": "color", "$description": "amber" },
        "c6": { "$value": "oklch(50% 0.10 200)", "$type": "color", "$description": "teal" },
        "c7": { "$value": "oklch(45% 0.14 340)", "$type": "color", "$description": "magenta" },
        "c8": { "$value": "oklch(35% 0.02 240)", "$type": "color", "$description": "slate" }
      },
      "sequential": {
        "min": { "$value": "oklch(97% 0.02 250)", "$type": "color" },
        "max": { "$value": "oklch(35% 0.15 250)", "$type": "color" }
      },
      "diverging": {
        "low":  { "$value": "oklch(45% 0.18 25)",  "$type": "color" },
        "mid":  { "$value": "oklch(96% 0.003 80)", "$type": "color" },
        "high": { "$value": "oklch(45% 0.18 250)", "$type": "color" }
      }
    }
  },

  "space": {
    "0":  { "$value": "0",       "$type": "dimension" },
    "1":  { "$value": "0.25rem", "$type": "dimension" },
    "2":  { "$value": "0.5rem",  "$type": "dimension" },
    "3":  { "$value": "0.75rem", "$type": "dimension" },
    "4":  { "$value": "1rem",    "$type": "dimension" },
    "6":  { "$value": "1.5rem",  "$type": "dimension" },
    "8":  { "$value": "2rem",    "$type": "dimension" },
    "12": { "$value": "3rem",    "$type": "dimension" },
    "16": { "$value": "4rem",    "$type": "dimension" },
    "24": { "$value": "6rem",    "$type": "dimension" }
  },

  "radius": {
    "none": { "$value": "0",     "$type": "dimension" },
    "sm":   { "$value": "4px",   "$type": "dimension" },
    "md":   { "$value": "8px",   "$type": "dimension" },
    "lg":   { "$value": "16px",  "$type": "dimension" },
    "pill": { "$value": "9999px","$type": "dimension" }
  },

  "shadow": {
    "sm": {
      "$type": "shadow",
      "$value": [
        { "color": "rgb(15 23 42 / 0.04)", "offsetX": "0", "offsetY": "1px", "blur": "2px",  "spread": "0" },
        { "color": "rgb(15 23 42 / 0.06)", "offsetX": "0", "offsetY": "1px", "blur": "3px",  "spread": "0" }
      ]
    },
    "md": {
      "$type": "shadow",
      "$value": [
        { "color": "rgb(15 23 42 / 0.04)", "offsetX": "0", "offsetY": "4px", "blur": "8px",  "spread": "0" },
        { "color": "rgb(15 23 42 / 0.06)", "offsetX": "0", "offsetY": "2px", "blur": "4px",  "spread": "0" }
      ]
    },
    "lg": {
      "$type": "shadow",
      "$value": [
        { "color": "rgb(15 23 42 / 0.06)", "offsetX": "0", "offsetY": "12px","blur": "24px", "spread": "0" },
        { "color": "rgb(15 23 42 / 0.08)", "offsetX": "0", "offsetY": "4px", "blur": "8px",  "spread": "0" }
      ]
    },
    "xl": {
      "$type": "shadow",
      "$value": [
        { "color": "rgb(15 23 42 / 0.08)", "offsetX": "0", "offsetY": "24px","blur": "48px", "spread": "0" },
        { "color": "rgb(15 23 42 / 0.10)", "offsetX": "0", "offsetY": "8px", "blur": "16px", "spread": "0" }
      ]
    }
  },

  "motion": {
    "duration": {
      "micro":      { "$value": "120ms", "$type": "duration" },
      "transition": { "$value": "240ms", "$type": "duration" },
      "emphasis":   { "$value": "480ms", "$type": "duration" },
      "narrative":  { "$value": "960ms", "$type": "duration" }
    },
    "ease": {
      "standard": { "$value": "cubic-bezier(0.2, 0, 0, 1)",    "$type": "cubicBezier" },
      "enter":    { "$value": "cubic-bezier(0.05, 0.7, 0.1, 1)","$type": "cubicBezier" },
      "exit":     { "$value": "cubic-bezier(0.3, 0, 0.8, 0.15)","$type": "cubicBezier" }
    }
  },

  "breakpoint": {
    "sm": { "$value": "640px",  "$type": "dimension" },
    "md": { "$value": "768px",  "$type": "dimension" },
    "lg": { "$value": "1024px", "$type": "dimension" },
    "xl": { "$value": "1280px", "$type": "dimension" }
  }
}
```
