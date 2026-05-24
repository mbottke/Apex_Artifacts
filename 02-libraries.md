# Apex-Artifacts — Libraries (platters, not recipes)

Bundled from the apex-artifacts source repository. Each source file
is enclosed by `<!-- BEGIN: path -->` ... `<!-- END: path -->`
anchors so semantic retrieval and humans can locate the original.

## Files in this bundle

- `references/libraries/color-library.md`
- `references/libraries/composition-library.md`
- `references/libraries/dataset-corpus.md`
- `references/libraries/iconography-library.md`
- `references/libraries/inspiration-atlas.md`
- `references/libraries/medical-artifacts.md`
- `references/libraries/motion-library.md`
- `references/libraries/pedagogy-library.md`
- `references/libraries/reader-models.md`
- `references/libraries/rhetorical-atlas.md`
- `references/libraries/romantic-artifacts.md`
- `references/libraries/scientific-artifacts.md`
- `references/libraries/snippet-cookbook.md`
- `references/libraries/type-library.md`
- `references/libraries/utilities.md`
- `references/libraries/visualization-grammar.md`

---


<!-- BEGIN: references/libraries/color-library.md -->

# Color Library

A platter, not a recipe. The palettes below are examples from a much larger space — a handful drawn from hundreds of possibilities across history, geography, and genre. None is "right"; each is one answer to a specific aesthetic problem. Combine them, invent from them, or reach outside them when this artifact calls for something unrepresented.

> See `references/how-to-use-this-system.md` for the platter principle.

---

## 1. Color theory, briefly

Enough theory to reason freshly rather than pick from a list.

### Perceptual foundations

- **Hue, chroma, lightness** — the three axes of color perception. OKLCH makes them independently manipulable, which HSL / HSV / RGB do not.
- **Perceptual uniformity** — equal numerical distances should produce equal perceived distances. OKLCH is perceptually uniform; HSL is not (yellow at 50% lightness reads brighter than blue at 50%).
- **Opponent processes** — human vision perceives red-green, blue-yellow, and light-dark as opposing pairs. This is why complementary pairs carry visual tension.
- **Simultaneous contrast** — a gray surrounded by red appears greenish; surrounded by blue appears yellowish. Color is relational.
- **Chromatic adaptation** — the eye adjusts to the dominant illuminant. A palette that looks warm in one context looks neutral in another.

### Harmony frameworks (none is "correct"; each produces a flavor)

- **Monochromatic** — one hue, varied lightness and chroma. Restrained, unified, can feel austere.
- **Analogous** — hues adjacent on the wheel (30–60° apart). Natural, calm, reminiscent of nature scenes.
- **Complementary** — hues opposite (180°). High tension, hard to balance, rewards discipline.
- **Split-complementary** — a hue plus the two adjacent to its complement. Softer than pure complementary; more movement than analogous.
- **Triadic** — three hues evenly spaced (120° apart). Vibrant, needs one dominant and two supporting.
- **Tetradic / square** — four hues in two complementary pairs. Rich but risks chaos.
- **Achromatic + single accent** — all grayscale with one saturated hue. The palette used by most serious editorial design for a reason.

### Temperature

- **Warm hues** (red, orange, yellow, warm browns): advance, energize, feel tactile
- **Cool hues** (blue, cyan, violet, cool greens): recede, calm, feel technological
- **Temperature-neutral neutrals** (pure gray) exist but are rare in apex work — most neutrals lean warm or cool and the lean is part of the identity

### Accessibility as design

- **Contrast** is a designable dimension, not an afterthought. 4.5:1 for body text, 3:1 for large text and UI elements — but apex work often uses 7:1 or higher for pure black-on-white editorial register
- **Colorblindness safety** — roughly 8% of men and 0.5% of women have some form of color vision deficiency. Most common: deuteranopia (red-green). Red and green should never be the sole distinguisher.
- **Non-color channels** — shape, pattern, position, label — pair with color to make information redundant-encoded

### Ways to generate a palette fresh

- **From a hue seed** — pick a primary hue, generate analogous / complementary / triadic via OKLCH rotation
- **From an inspiration image** — extract the dominant 5-8 colors; assess whether they balance; adjust chroma/lightness for UI use
- **From a mood** — "quiet engineering" → desaturated neutrals with one restrained accent; "archival scholarship" → warm off-whites with sepias and aged-ink darks
- **From a constraint** — "must be colorblind-safe, must work in dark mode, must support three categorical levels" → design backwards from constraints
- **From rebellion** — "what is everyone in this genre doing? do something else." Most SaaS is light-blue; use vermilion. Most data journalism uses viridis; use a single-hue ramp.

---

## 2. Palette atlas

A non-exhaustive walk through the space. Each entry is one option; the space is far larger.

### Editorial / serious / archival

**Financial Times Salmon** — the paper's iconic ground. Warm off-pink (#FFF1E5 / #FFF4E8) as surface; deep navy and black on top.

**The Economist Red** — pure editorial red (#E3120B) as accent, black body, warm off-white ground. Restrained.

**New York Review of Books** — cream, deep sepia ink, muted brick red for emphasis.

**Penguin Classics (classic)** — orange (#F1592A / #DE5032) and black on cream. Restrained mid-century.

**Quanta Magazine** — rich cobalt (#2E3E99), near-black, pure whites, saturated accent per issue.

**Kinfolk / Cereal** — muted neutrals, bone white, sage, ochre, muted clay. Contemporary editorial minimalism.

**MIT Press** — cool near-black, pure white, teal accent (#14B8A6-adjacent), occasional saffron.

### Scandinavian muted

**Finnish foggy** — pale gray-blues, off-whites, muted moss, deep plum accent.

**Copenhagen blue** — a soft-ink blue (#3B5167 or similar), warm white, muted coral.

**Aesop (brand)** — oat, warm off-black, botanical green, occasional terracotta.

### Mediterranean

**Amalfi citrus** — sun-bleached ochre, muted Mediterranean blue, coral, olive.

**Santorini blue-white** — near-pure white with cobalt and a touch of deep magenta.

**Tuscan sunset** — burnt sienna, olive, pale gold, deep wine.

### Japanese

**Ukiyo-e** — indigo (ai), vermilion (beni), gold, off-white, soft pinks. Woodblock print legacy.

**Wabi-sabi** — muted earth tones, aged bone, weathered gray, stone, moss.

**Contemporary Japanese editorial** (Muji register) — pure white, warm gray, muted accent. Monastic.

**Sumi ink** — deep charcoal black, rice-paper cream, single red seal accent.

### American mid-century

**Eames-era** — mustard, avocado, turquoise, burnt orange, creamy off-white. High-chroma optimism.

**Saul Bass** — flat primaries (vermilion, cobalt, gold), black, cream. Graphic design hero era.

**Charles & Ray** — warm woods, sage, cream, brick red, deep brown. Californian modernism.

### Bauhaus / De Stijl / constructivist

**Bauhaus primaries** — pure red, yellow, blue, black, white. No in-betweens.

**De Stijl** — pure primaries plus black plus white, nothing else. Mondrian palette.

**Russian constructivist** — vermilion red, black, cream, occasional gold. Propaganda-era.

### Memphis / 80s / post-modern

**Memphis group** — mint, hot pink, yellow, teal, black-and-white patterns. Deliberate chaos.

**Miami vice** — flamingo pink, turquoise, hot coral, palm green, sunset gold.

**Vaporwave** — lavender, mint, hot pink, deep purple. Digital nostalgia.

### 90s web / Y2K

**Chrome and optimism** — cyan, silver, pure black, glossy highlights.

**Dial-up era** — websafe hues; #0000FF, #FF0000, aggressive contrast.

**Frutiger Aero** — glossy blues, pure white, accent green, 2006-2013 era.

### Scientific / reference

**Nature-journal register** — cool gray, ink-black, restrained saturated accent per data series.

**Scientific American visual** — rich mid-grays, strong primary blue, one red flag color.

**Tufte print** — pure white ground, charcoal gray for body, black for the strongest ink marks, rare saturated accent.

### Data-dense / financial terminals

**Bloomberg terminal** — black ground, amber text (#F0A830-ish), green for positive, red for negative, orange for neutral alerts.

**Trading desk dark** — near-black, electric green, hot red, yellow highlights, cyan links.

### Gaming / entertainment

**Nintendo-era joy** — pure red (#E60012), pure white, pure black, canary yellow.

**Nordic noir** — deep blue-black, ice white, blood red, single electric accent.

**Cyberpunk neon** — magenta, cyan, black, yellow highlights, teal grime.

### Natural / botanical

**Audubon field guide** — cream pages, ink black, muted naturalist colors (sage, bark, robin's egg, goldfinch, cardinal red).

**Mineralogical** — ochre, malachite, azurite, iron oxide, bone.

**Oceanic** — deep trench, pelagic blue, kelp green, shell cream, vermilion (coral).

**Arctic / tundra** — bone white, slate, pale lichen, bruise purple, single ember orange.

**Desert / sonoran** — sand, sage, terra cotta, iron, bone.

### Historical / period

**Illuminated manuscript** — ultramarine (lapis), gold, madder red, oak-gall black, parchment.

**Victorian** — deep burgundy, mustard, forest, cream, sepia.

**Art Nouveau** — muted botanical palette — sage, rose, cream, gold accents.

**Art Deco** — deep teal, gold, black, cream, burgundy.

**Bauhaus Weimar** — mustard, cobalt, brick red, cream, black.

**Googie / atomic age** — turquoise, coral, cream, chrome-gray, sunrise orange.

### Propaganda-graphics register (for study, not imitation)

**Soviet poster** — vermilion, black, cream, occasional gold. Flat application.

**WPA poster** — flat color fields, muted saturated greens / blues / reds / yellows, restrained layout.

**Wartime British** — deep red, black, cream. "Keep Calm" register.

### Digital-native

**Material Design era** — Google's bold primaries. Teal + amber was a notable pairing.

**Brutalist web** — high contrast, pure white or pure black ground, saturated accents used as attack.

**Terminal revivalist** — dark charcoal, lime green or amber mono text, subtle color coding.

**Modern SaaS** — near-white ground, cool gray scale, indigo or blue-purple accent. The default Claude should be suspicious of — if the artifact ends up here by accident, it wasn't chosen; it was defaulted to.

### Monastic / contemplative

**Zen rock garden** — five tones of warm neutral, no accent.

**Quaker meeting hall** — cream, dark wood, one note of muted green.

**Shaker functional** — bone, oak, deep blue-gray, occasional brick.

---

## 3. Palette construction recipes

Ways to invent a palette when nothing in the atlas fits.

### The single-hue ramp
Pick one hue. Generate 10 lightness steps via OKLCH. Use the extremes for text and surface; the mids for accents and data. Monochrome, restrained, appropriate for reference-grade artifacts.

### The shifted-hue neutral
Rather than pure gray (`oklch(50% 0 h)`), shift the chroma to 0.01–0.03 with a specific hue. Gives neutrals a temperature without declaring a color.

### The inspiration-to-ui pipeline
1. Pick a reference image (painting, photograph, textile, natural scene).
2. Extract 5–8 dominant colors.
3. Evaluate: are they balanced in lightness? Is there enough contrast? Colorblind safe?
4. Adjust: lift some for text, darken some for body, select one as accent.
5. Add a pure or near-pure ground (typically lighter than anything in the original).
6. Test in both light and dark schemes.

### The constraint-driven build
- Must be WCAG AAA (7:1 for body)
- Must work colorblind
- Must have 3 categorical distinctions + 1 accent
- Must feel "institutional but not corporate"

Design backwards from the constraint list. Arrive somewhere specific.

### The rebellion
Survey 10 artifacts in the target genre. Note their palettes. Choose a palette that sits in none of those spaces. Justify the divergence by the artifact's actual argument.

### The emotional-target
Pick three adjectives — "quiet, warm, honest." Each word maps to a color space: *quiet* → low chroma, *warm* → hue rotation toward amber, *honest* → high ground / body contrast. The palette emerges from the intersection.

---

## 4. Dark-mode-native design

Dark mode is not inversion. It is a separate design.

- Accents lighten (saturated colors read as fluorescent on black)
- Shadows become luminous overlays, not drop shadows
- Body text is near-white (`oklch(95% ...)`) not pure white — pure white vibrates
- Ground is near-black (`oklch(13% ...)`) not pure black — pure black loses all dimension
- Test contrast independently; don't assume light-mode contrast transfers

When designing a palette, **design light and dark simultaneously** or commit to one and acknowledge the other will require a separate pass.

---

## 5. When to use which family

**No decision tree.** The artifact's tone, audience, subject, and context point at a family of palettes; the creator chooses within it or invents fresh. But a few compatibilities are worth noting (not rules — observations):

- **Financial / serious reference** pairs well with warm editorial neutrals or deep editorial blues
- **Scientific / dense data** pairs well with restrained palettes that reserve saturation for data
- **Consumer / warm product** pairs well with Scandinavian muted or Mediterranean warmth
- **Technical / developer audience** pairs well with terminal-revivalist or cool-slate registers
- **Editorial opinion / essay** can support almost anything; the palette becomes the voice
- **Teaching / pedagogical** benefits from restrained palettes — color becomes information, not decoration
- **Celebratory / launch / announcement** warrants more saturation than reference work

But the pairings above are defaults to *challenge*, not to follow. "This is a financial reference piece, so let's use a Japanese ukiyo-e palette" — if you can justify it, that divergence is exactly where the wow-factor lives.

---

## 6. Cross-references

- `references/design-tokens.md` — one canonical token set (cool slate + indigo), useful as a default but substitutable
- `references/libraries/type-library.md` — typography pairings that resonate with these palettes
- `references/libraries/inspiration-atlas.md` — artifacts across domains whose palettes you can extract from
- `references/medium-playbooks/data-visualization.md` — palette considerations specific to charts

---

## 7. How to extend this library

Add a palette when:
- It represents a tradition, era, region, or register not yet represented
- It is a documented historical palette (with provenance) or a coherent contemporary register
- You can name its character in a phrase — "austere Finnish monasticism," "California mid-century optimism"

Do not add:
- Personal favorites without broader provenance
- Palettes that duplicate something already present
- Palettes without a coherent register

The goal is breadth of traditions, not depth of any one.

<!-- END: references/libraries/color-library.md -->

---


<!-- BEGIN: references/libraries/composition-library.md -->

# Composition Library

A platter, not a layout recipe. Composition — the arrangement of elements on a surface — is where most craft is legible. This library surveys compositional traditions from across design history so that Claude can reason from a wider space than "hero + feature grid + footer."

> See `references/how-to-use-this-system.md` for the platter principle.

---

## 1. Compositional theory, briefly

### The fundamentals

- **Hierarchy** — what the eye reaches first, second, third. Achieved through size, weight, color, position, isolation, density.
- **Rhythm** — repeated and varied spacing; the pulse of the layout.
- **Scale** — relative size relationships. Apex work has meaningful scale jumps; mediocre work flattens everything to similar sizes.
- **Balance** — distribution of visual weight. Can be symmetric (formal) or asymmetric (dynamic).
- **Alignment** — invisible lines that elements share. The more strongly aligned, the more composed the result feels.
- **White space** — not absence, but presence. Silence shapes sound; white space shapes composition.
- **Figure-ground** — the foreground/background relationship. Apex work has deliberate figure-ground; amateur work often has neither.
- **Tension & release** — elements in opposition (scale, color, position) create visual interest; resolution of that tension creates satisfaction.

### Grid systems

A grid is one structural choice among many.

- **Single column** — long-form reading. 65-72ch measure.
- **2-column** — news, books, documents. Balance between density and readability.
- **3-column** — editorial, product comparison. Classic.
- **12-column** — product UI standard. Flexible but can become invisible as a constraint.
- **16-column** — denser, magazine-like.
- **Modular grid** — rows and columns both, allowing rectangular content blocks in various spans.
- **Baseline grid** — vertical rhythm based on line-height. All body text sits on consistent baselines; all elements snap to multiples of that unit.
- **Broken grid** — some elements obey the grid, one or two break it deliberately for emphasis.
- **Non-grid / asymmetric** — no underlying column structure. Requires more skill to avoid chaos.

Grids are tools; not using them is a choice, not an oversight. Apex work deploys them consciously, often violates them deliberately, and sometimes eschews them entirely.

---

## 2. Compositional traditions

### Swiss / International Typographic Style

Emerged in the 1950s from Zurich and Basel. Core figures: Josef Müller-Brockmann, Emil Ruder, Max Bill, Armin Hofmann.

**Characteristics:**
- Rigorous grid systems
- Asymmetric composition
- Sans-serif typefaces (often Akzidenz-Grotesk, later Helvetica)
- Left-aligned text
- Generous white space
- Photography treated graphically
- Grid visible through alignment, not lines

**Contemporary descendants:** Apple's product design (pre-2013 especially), Swiss tech/design firms, IDEO.

**When it fits:** reference material, product design, serious editorial, anything where information is the subject.

### Editorial / magazine composition

Shaped by 20th-century magazine design — Condé Nast, Time Inc., editorial photography traditions.

**Characteristics:**
- Strong typographic hierarchy
- Display type dramatically larger than body
- Pull quotes and oversized initials
- Photography as full-bleed or framed element
- Multiple columns with varying width
- Text wraps around images

**Contemporary descendants:** The New Yorker, Kinfolk, Monocle, It's Nice That, Dense Discovery.

**When it fits:** long-form, essay, narrative, persuasion, identity.

### Brutalist web (and print)

Emerged as a reaction to slick SaaS design, circa 2016-present. Key figures: Pascal Deville (brutalistwebsites.com), early Are.na aesthetic.

**Characteristics:**
- Raw, unstyled-looking type
- Stark grids or deliberate anti-grids
- High-contrast, often monochrome
- Unapologetic code-as-interface
- Documents rather than "experiences"
- Information density over polish

**Contemporary descendants:** Are.na, some GitHub pages, editorial sites like *Cabinet*, some newsletter platforms.

**When it fits:** independent publishing, aesthetic statement, document-as-artifact.

### Japanese editorial (contemporary)

Shaped by 20th-century Japanese graphic design — Ikko Tanaka, Kohei Sugiura, Kenya Hara, Jun Takahashi (Undercover print work).

**Characteristics:**
- Extreme restraint; pure white ground
- Small type set confidently
- Large empty regions as essential
- Asymmetric balance
- Mix of CJK and Latin with careful typographic pairing
- Photography as delicate element, not dominant

**Contemporary descendants:** Muji design language, some MoMA publications, editorial sites like *Paper* and *Toiletpaper*.

**When it fits:** contemplation, minimalism, luxury-adjacent register, calm.

### Bauhaus / De Stijl / constructivist

1919-1940 European avant-garde. Walter Gropius, László Moholy-Nagy, Piet Mondrian, El Lissitzky, Alexander Rodchenko.

**Characteristics:**
- Geometric primitives (circles, rectangles, primary colors)
- Asymmetric composition
- Typography as graphic element (angled, oversized, color-blocked)
- Photography + typography hybrids
- Structural grids often visible as lines
- Sans-serif type (Futura, Universal)

**Contemporary descendants:** posters (still!), brand identity for arts institutions, some propaganda-adjacent aesthetic choices.

**When it fits:** assertive, declarative, historical-aware, aesthetic statement.

### Polish poster school

1950s-1980s. Henryk Tomaszewski, Jan Lenica, Roman Cieślewicz, Waldemar Świerzy.

**Characteristics:**
- Hand-drawn elements
- Surreal juxtaposition
- Limited palette, often saturated
- Type and image as unified composition
- Symbolic rather than literal imagery

**When it fits:** cultural content, events, assertive aesthetic character.

### Memphis / postmodern

Mid-1980s Italian design collective. Ettore Sottsass, Michele De Lucchi.

**Characteristics:**
- Bold geometric patterns (squiggles, dots, grids)
- Clashing saturated colors
- Asymmetric, playful composition
- Mixed typefaces deliberately
- Decorative, anti-modernist

**Contemporary descendants:** some illustration-driven brands, 80s-revival design.

**When it fits:** rare; when the subject explicitly calls for playful, contrarian, deliberately non-serious.

### Information-dense / wonky

Exemplified by *The Economist*, the Federal Reserve publications, financial reports, sabermetrics visualizations.

**Characteristics:**
- Small type, dense layout
- Tables and charts as first-class citizens
- Minimal decoration
- Trust readers to read
- Deep information per inch

**Contemporary descendants:** *FT Alphaville*, *Marginal Revolution*, some academic journal articles, *Atomic* newsletter.

**When it fits:** reference, analysis, audience expects density.

### Scroll-driven narrative

Emerged from journalism (NYT "Snow Fall" 2012) and its explainer descendants.

**Characteristics:**
- Full-viewport sections
- Content revealed as user scrolls
- Sticky visuals with changing text
- Cinematic pacing
- Typography often large and display-scale

**Contemporary descendants:** The Pudding, Pudding Cuff, NYT interactives, the Ciechanowski essays.

**When it fits:** narrative explainers, story-driven journalism, product announcements.

### Dashboard / analytics layout

Emerged from business intelligence tools — Tableau, Mixpanel, Looker.

**Characteristics:**
- Grid of equal-sized panels
- KPIs in cards at top
- Primary chart prominent
- Secondary charts beneath
- Filters at edges

**Contemporary descendants:** every SaaS analytics tool.

**When it fits:** analytics, monitoring, operations. **Suspicion warranted** — the default dashboard layout is overused and often unargued. If your artifact is a dashboard, invent the composition instead of reaching for the default.

### Card-grid marketing

Emerged from Pinterest-like patterns, now ubiquitous in landing pages.

**Characteristics:**
- Equal-sized cards
- Image on top, title and short text below
- Hover animations
- "Features" or "benefits" grid

**Contemporary descendants:** most SaaS landing pages.

**When it fits:** rarely, if ever, for apex artifacts. It is the path of least resistance, and reads as template.

### Document-as-interface

Emerged from Notion, Roam, Craft, and long-form editorial docs.

**Characteristics:**
- Long-form vertical scroll
- Embedded interactive elements (toggles, callouts, code blocks, live computation)
- Typography-led
- Minimal chrome

**Contemporary descendants:** Notion pages, Observable notebooks, Substack, Ghost.

**When it fits:** reference, reading, knowledge work.

### Spatial / canvas

Emerged from Figma, Miro, tldraw, Arc Browser.

**Characteristics:**
- Free-form placement
- Zoom and pan as primary navigation
- Elements related spatially, not hierarchically
- Infinite canvas conceit

**When it fits:** exploratory, collaborative, concept-space artifacts.

### Print-first, even on screen

Some artifacts benefit from treating the screen as a page.

**Characteristics:**
- Fixed measure
- Headers, page numbers (conceptually)
- Body column, sidebar for marginalia
- Footnotes at bottom
- Serifed body, intentional
- Generous leading

**Contemporary descendants:** *The Browser* newsletter, *n+1*, long-form essay sites, academic paper renderings.

**When it fits:** long-form reading, serious essays, reference.

---

## 3. Layout patterns (as examples, not recipes)

Some common patterns. **Each is one option, not the option.**

### Hero + narrow reading column
Full-width hero (image, title, lede). Below, a narrow centered reading column for body text. Full-width figures can break out of the column.

### Sidebar + content
Left or right sidebar for navigation / metadata / filters. Main area for content. Classic documentation layout.

### Split-screen
Two panes, either equal or asymmetric. Comparison, before/after, code + result.

### Three-column docs
Left: navigation. Middle: prose. Right: code examples or references. Stripe's layout.

### Grid of cards
Equal cells. Product listings, link directories. Default often, apex rarely.

### Magazine spread
Multiple columns, varying widths, photography breaking into layout, pull quotes, dropcaps.

### Editorial long-read
Narrow column, generous leading, pull quotes mid-content, figures captioned precisely, chapter breaks visible.

### Infinite-scroll feed
Vertical stream of items. Social media default.

### Hub-and-spoke
Central overview page with links to detail pages. Documentation sites with "getting started" landing.

### Scroll-telling
Full-viewport sections, sticky visuals, narrative pacing.

### Atlas / reference
Index + browsable entries + deep detail. Wikipedia-like.

### Canvas / spatial
Free-form. No grid. Good for concept space, mind maps, creative work.

### Stacked dashboard
KPI strip → primary chart → secondary charts → detail table. (Suspicion warranted; default of defaults.)

### Split-reading with live panels
Prose left, interactive panels right that the prose references.

### Single page, vertical narrative
Entire artifact is one scroll; no navigation. Clarity through constraint.

### Timeline / chronology
Entities arranged temporally. Horizontal or vertical.

### Print-replica
Fixed-size artifact laid out as a page; possibly with page-flip affordance.

---

## 4. Negative space as design

One of the hardest disciplines. Most artifacts are too crowded; apex artifacts are often surprisingly empty.

- **White space around a hero** — isolates and amplifies
- **Space between sections** — gives reading a rhythm
- **Space inside components** — padding generous enough that content breathes
- **Margin around body text** — modern web tends to cramp; apex work breathes

Rule of thumb: after your first pass, increase all whitespace by 25%. See if the artifact improves. Often yes.

---

## 5. Hierarchy construction

How apex artifacts produce clear hierarchy:

- **Scale jumps** — body at 16px, H2 at 28px, H1 at 48px or more. Clear levels.
- **Weight contrast** — body at 400, headings at 600-700, display at 700-900. Use thin weights (200-300) for contrast moments only.
- **Isolation** — a lone element amid space reads as important regardless of its size.
- **Position** — top-left is the eye's starting point in LTR reading; top-center feels announced; center-center feels climactic.
- **Color saturation** — one saturated element among neutrals draws attention; everything saturated reads as noise.
- **Density contrast** — a dense block next to empty space: both become visible.

A common failure: every element uses a different weight, size, and color, trying to establish hierarchy through variety. The result is no hierarchy — everything shouts, nothing stands out.

---

## 6. Breaking the grid

Apex composition often uses a grid and then violates it, once, deliberately.

- A caption that extends into the margin
- A figure that breaks the column
- A pull quote that sits diagonally
- A footer aligned against the grid instead of with it

The violation is the focal point. The rest of the composition supports it by being disciplined.

---

## 7. Composing fresh

When no existing layout pattern fits:

1. **Start from the content's natural structure.** What are the elements? How do they relate hierarchically, temporally, or spatially?
2. **Draft a grid from the content's ratios.** If one element is ~3× another, try a 3:1 split.
3. **Establish the reading path** — where does the eye start? Where next? Where does it rest?
4. **Place the anchor** — the element the whole composition depends on.
5. **Distribute supporting elements** — fill in, respecting the grid you drafted.
6. **Introduce a break** — one element that violates the grid, earning focal attention.
7. **Edit down** — remove anything that doesn't contribute to the reading path.

---

## 8. Cross-references

- `references/libraries/type-library.md` — typography that fits these compositions
- `references/libraries/color-library.md` — palettes that support or contradict the composition
- `references/libraries/inspiration-atlas.md` — compositions from non-digital sources
- `references/medium-playbooks/long-form-document.md` — specific guidance for prose-heavy layouts
- `references/medium-playbooks/claude-react-artifact.md` — React-specific composition patterns

---

## 9. Extending this library

Add a tradition or pattern when:
- It has historical or contemporary provenance
- It is distinct from patterns already covered
- It solves a class of compositional problem

Avoid:
- Catalog of visual trends without deeper principle
- "The Best Layouts of 2024"-style lists
- Patterns that are minor variations on the Card Grid

The goal is breadth of design thinking, not a catalog of screens.

<!-- END: references/libraries/composition-library.md -->

---


<!-- BEGIN: references/libraries/dataset-corpus.md -->

# Dataset Corpus

A platter of dataset shapes and illustrative examples — not a prescribed set of datasets to reach for. Sample datasets should be *recombined, transformed, and generated fresh* to serve whatever the specific artifact needs. This library documents the space of data shapes, provides illustrative example datasets for each, and suggests generator patterns for producing fresh data.

> See `references/how-to-use-this-system.md` for the platter principle.

---

## 1. Data shapes (the space)

Data shape determines what visualizations and interactions are possible. Major shapes:

### Tabular (rectangular)

- **Flat table** — rows of observations, columns of attributes. The default shape for most datasets.
- **Pivot / wide-form** — one row per entity; columns for each time point or category. Good for humans; harder for many analyses.
- **Long-form / tidy** — one row per observation (Wickham's "tidy data"). Easier for grouped analyses.

### Time series

- **Regular** — observations at fixed intervals (daily, weekly, monthly)
- **Irregular** — observations at arbitrary times (user events, sensor readings)
- **Multi-series** — multiple parallel time series, possibly with different frequencies or scales
- **Cohort** — a fixed group tracked over time

### Categorical

- **Nominal** — unordered labels (country names, product categories, sentiment labels)
- **Ordinal** — ordered categories (Likert scales, ranks, tiers)
- **Binary** — two labels (yes/no, pass/fail, click/no-click)

### Hierarchical

- **Tree** — single root, branching structure (file systems, taxonomies, org charts)
- **DAG** — directed acyclic graph (dependencies, family trees)
- **Forest** — multiple disconnected trees

### Graph / network

- **Directed** — edges have direction (follower networks, web links)
- **Undirected** — symmetric edges (collaborations, friendships)
- **Weighted** — edges have numeric weights
- **Bipartite** — two node types, edges only between types (users↔products)
- **Temporal** — edges have timestamps

### Geographic / spatial

- **Point data** — locations with attributes (incidents, listings)
- **Region data** — polygons with attributes (countries, counties, neighborhoods)
- **Continuous fields** — elevation, temperature across space
- **Flow data** — movement between locations

### Text

- **Document collection** — many separate texts
- **Corpus with metadata** — texts annotated by date, author, topic
- **Sequence** — ordered text with positional structure

### Multimedia

- **Image sets** — classification datasets, object detection
- **Audio sequences** — waveforms with metadata
- **Video sequences** — frame-level metadata plus audio

### Matrix / grid

- **Correlation matrix** — pairwise values
- **Adjacency matrix** — network as matrix
- **Contingency table** — cross-tabulation of categorical variables
- **Heatmap data** — 2D grid of values

### Streaming / event

- **Event log** — sequence of typed events with attributes
- **Session data** — events grouped by session
- **Real-time streams** — continuously arriving observations

### Distributional

- **Univariate distribution** — counts of a single measure
- **Joint distribution** — counts across two or more measures
- **Empirical samples** — observed values of a process

---

## 2. Illustrative example datasets

Each is **one example** of its shape. Use as starting points for artifacts; freely swap values or generate fresh variants.

### Time series example: product KPIs Q1 2026

```json
[
  { "date": "2026-01-01", "dau": 42800, "signups": 312, "churn": 0.038 },
  { "date": "2026-01-08", "dau": 43900, "signups": 389, "churn": 0.035 },
  { "date": "2026-01-15", "dau": 45100, "signups": 401, "churn": 0.033 },
  { "date": "2026-01-22", "dau": 46800, "signups": 356, "churn": 0.036 },
  { "date": "2026-01-29", "dau": 47900, "signups": 412, "churn": 0.031 },
  { "date": "2026-02-05", "dau": 48600, "signups": 398, "churn": 0.029 },
  { "date": "2026-02-12", "dau": 52300, "signups": 534, "churn": 0.028, "event": "pricing change" },
  { "date": "2026-02-19", "dau": 58900, "signups": 612, "churn": 0.030 },
  { "date": "2026-02-26", "dau": 61200, "signups": 547, "churn": 0.029 },
  { "date": "2026-03-05", "dau": 63800, "signups": 498, "churn": 0.028 },
  { "date": "2026-03-12", "dau": 64100, "signups": 472, "churn": 0.027 },
  { "date": "2026-03-19", "dau": 65300, "signups": 451, "churn": 0.029 },
  { "date": "2026-03-26", "dau": 64800, "signups": 438, "churn": 0.030 }
]
```

### Categorical example: survey responses (Likert scale)

```json
[
  { "question": "Satisfaction with product", "strongly_disagree": 3, "disagree": 12, "neutral": 28, "agree": 82, "strongly_agree": 75 },
  { "question": "Would recommend to others", "strongly_disagree": 2, "disagree": 8, "neutral": 19, "agree": 96, "strongly_agree": 75 },
  { "question": "Value for money", "strongly_disagree": 8, "disagree": 21, "neutral": 44, "agree": 76, "strongly_agree": 51 },
  { "question": "Ease of onboarding", "strongly_disagree": 4, "disagree": 14, "neutral": 33, "agree": 89, "strongly_agree": 60 }
]
```

### Hierarchical example: taxonomy tree

```json
{
  "name": "Animals",
  "children": [
    {
      "name": "Mammals",
      "children": [
        { "name": "Primates", "count": 504 },
        { "name": "Carnivores", "count": 286 },
        { "name": "Rodents", "count": 2277 }
      ]
    },
    {
      "name": "Birds",
      "children": [
        { "name": "Passerines", "count": 6553 },
        { "name": "Raptors", "count": 533 }
      ]
    },
    {
      "name": "Fish",
      "children": [
        { "name": "Bony fish", "count": 32000 },
        { "name": "Cartilaginous fish", "count": 1200 }
      ]
    }
  ]
}
```

### Graph example: collaboration network (small)

```json
{
  "nodes": [
    { "id": "A", "group": "product", "label": "Alicia" },
    { "id": "B", "group": "design", "label": "Ben" },
    { "id": "C", "group": "engineering", "label": "Chen" },
    { "id": "D", "group": "engineering", "label": "Dana" },
    { "id": "E", "group": "marketing", "label": "Elena" },
    { "id": "F", "group": "product", "label": "Farrah" }
  ],
  "edges": [
    { "source": "A", "target": "B", "weight": 8 },
    { "source": "A", "target": "F", "weight": 12 },
    { "source": "B", "target": "C", "weight": 5 },
    { "source": "C", "target": "D", "weight": 15 },
    { "source": "D", "target": "A", "weight": 7 },
    { "source": "E", "target": "A", "weight": 6 },
    { "source": "E", "target": "F", "weight": 9 },
    { "source": "B", "target": "F", "weight": 11 }
  ]
}
```

### Geographic example: US state populations (abbreviated)

```json
[
  { "state": "California",  "code": "CA", "pop_2024": 38900000, "area_km2": 423970, "gdp_2024_trillion": 3.7 },
  { "state": "Texas",       "code": "TX", "pop_2024": 30500000, "area_km2": 696200, "gdp_2024_trillion": 2.5 },
  { "state": "Florida",     "code": "FL", "pop_2024": 22600000, "area_km2": 170312, "gdp_2024_trillion": 1.4 },
  { "state": "New York",    "code": "NY", "pop_2024": 19400000, "area_km2": 141297, "gdp_2024_trillion": 2.2 },
  { "state": "Pennsylvania","code": "PA", "pop_2024": 12900000, "area_km2": 119283, "gdp_2024_trillion": 0.9 }
]
```

### Cohort example: retention by cohort

```json
[
  { "cohort": "Jan 2026", "size": 1240, "w0": 100, "w1": 74, "w2": 58, "w4": 43, "w8": 32, "w12": 27 },
  { "cohort": "Feb 2026", "size": 1980, "w0": 100, "w1": 81, "w2": 72, "w4": 65, "w8": 59, "w12": 57 },
  { "cohort": "Mar 2026", "size": 2360, "w0": 100, "w1": 78, "w2": 64, "w4": 54, "w8": 45, "w12": 42 }
]
```

### Distribution example: response times

```json
{
  "p50": 145,
  "p75": 220,
  "p90": 380,
  "p95": 510,
  "p99": 1240,
  "p999": 3200,
  "samples": [120, 145, 160, 180, 210, 250, 310, 380, 450, 510, 720, 890, 1240]
}
```

### Network/flow example: Sankey (conversion funnel)

```json
{
  "nodes": [
    { "id": "landing" },
    { "id": "signup" },
    { "id": "onboarded" },
    { "id": "activated" },
    { "id": "paid" }
  ],
  "links": [
    { "source": "landing",   "target": "signup",    "value": 12000 },
    { "source": "signup",    "target": "onboarded", "value": 8400 },
    { "source": "onboarded", "target": "activated", "value": 5100 },
    { "source": "activated", "target": "paid",      "value": 1200 }
  ]
}
```

### Event log example: user session

```json
[
  { "t": 0,     "user": "u_17",  "event": "session_start", "path": "/" },
  { "t": 3400,  "user": "u_17",  "event": "page_view",     "path": "/pricing" },
  { "t": 8900,  "user": "u_17",  "event": "scroll",        "depth": 0.62 },
  { "t": 12100, "user": "u_17",  "event": "click",         "element": "cta_signup" },
  { "t": 12800, "user": "u_17",  "event": "page_view",     "path": "/signup" },
  { "t": 89400, "user": "u_17",  "event": "form_abandon",  "field": "password" }
]
```

### Text corpus example: labeled feedback

```json
[
  { "text": "This is the first analytics tool that felt built for engineers.", "sentiment": "positive", "length_chars": 58 },
  { "text": "I can't find the billing section anywhere.",                       "sentiment": "negative", "length_chars": 43 },
  { "text": "The dashboard loads fast but the mobile view is broken.",           "sentiment": "mixed",    "length_chars": 54 }
]
```

### Matrix example: correlation between metrics

```json
{
  "columns": ["speed", "price", "quality", "weight", "durability"],
  "rows": [
    [1.00, -0.32, 0.64, -0.55, 0.41],
    [-0.32, 1.00, 0.58, 0.22, 0.48],
    [0.64, 0.58, 1.00, -0.18, 0.77],
    [-0.55, 0.22, -0.18, 1.00, -0.62],
    [0.41, 0.48, 0.77, -0.62, 1.00]
  ]
}
```

### Survey example: question matrix

```json
{
  "questions": [
    { "id": "q1", "text": "I find the product valuable", "scale": "likert5" },
    { "id": "q2", "text": "I would recommend it",        "scale": "likert5" },
    { "id": "q3", "text": "It's well-designed",          "scale": "likert5" },
    { "id": "q4", "text": "It's worth the price",        "scale": "likert5" }
  ],
  "responses_by_segment": {
    "power_users":   { "q1": 4.3, "q2": 4.5, "q3": 4.1, "q4": 3.9, "n": 412 },
    "regular_users": { "q1": 3.7, "q2": 3.8, "q3": 3.6, "q4": 3.3, "n": 1840 },
    "new_users":     { "q1": 3.5, "q2": 3.4, "q3": 4.0, "q4": 3.1, "n": 623 }
  }
}
```

### Historical time series example: industrial production (synthetic)

```json
[
  { "year": 1980, "production_index": 78 },
  { "year": 1985, "production_index": 89 },
  { "year": 1990, "production_index": 102 },
  { "year": 1995, "production_index": 118 },
  { "year": 2000, "production_index": 132 },
  { "year": 2005, "production_index": 141 },
  { "year": 2010, "production_index": 134 },
  { "year": 2015, "production_index": 151 },
  { "year": 2020, "production_index": 147 },
  { "year": 2025, "production_index": 168 }
]
```

---

## 3. Generator patterns

For the specific artifact, synthetic data often beats copy-pasted examples. Patterns:

### Random walk (time series)

```js
function randomWalk(n, start = 100, volatility = 3, drift = 0.5) {
  const data = [{ t: 0, y: start }];
  for (let i = 1; i < n; i++) {
    const prev = data[i - 1].y;
    const step = (Math.random() - 0.5) * 2 * volatility + drift;
    data.push({ t: i, y: +(prev + step).toFixed(2) });
  }
  return data;
}
```

### Logistic growth (adoption curves)

```js
function logisticGrowth(n, K = 1000, r = 0.08, noise = 0.05) {
  const data = [];
  for (let t = 0; t < n; t++) {
    const base = K / (1 + Math.exp(-r * (t - n / 2)));
    const noisy = base * (1 + (Math.random() - 0.5) * noise);
    data.push({ t, y: +noisy.toFixed(1) });
  }
  return data;
}
```

### Event bursts (Poisson with event-triggered bursts)

```js
function eventBursts(durationMinutes, baseRate = 0.3, burstAt = [30, 90], burstMultiplier = 8) {
  const events = [];
  for (let m = 0; m < durationMinutes; m++) {
    let rate = baseRate;
    for (const burst of burstAt) {
      if (m >= burst && m < burst + 5) rate = baseRate * burstMultiplier;
    }
    if (Math.random() < rate) events.push({ minute: m });
  }
  return events;
}
```

### Cohort retention (declining curve)

```js
function cohortRetention(sizes, halfLives) {
  return sizes.map((size, i) => {
    const retention = {};
    for (const week of [0, 1, 2, 4, 8, 12]) {
      retention[`w${week}`] = +(Math.pow(0.5, week / halfLives[i]) * 100).toFixed(1);
    }
    return { cohort: `C${i + 1}`, size, ...retention };
  });
}
```

### Correlation matrix

```js
function symmetricCorrelationMatrix(n, seed = []) {
  const m = Array.from({ length: n }, () => Array(n).fill(0));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j <= i; j++) {
      if (i === j) m[i][j] = 1;
      else {
        const v = seed[i * n + j] ?? +(Math.random() * 2 - 1).toFixed(2);
        m[i][j] = m[j][i] = v;
      }
    }
  }
  return m;
}
```

### Network (preferential attachment)

```js
function preferentialAttachment(n, m = 2) {
  const nodes = [{ id: 0 }, { id: 1 }];
  const edges = [{ source: 0, target: 1 }];
  const deg = { 0: 1, 1: 1 };
  for (let i = 2; i < n; i++) {
    nodes.push({ id: i });
    deg[i] = 0;
    const chosen = new Set();
    while (chosen.size < Math.min(m, i)) {
      const total = Object.values(deg).reduce((a, b) => a + b, 0);
      const r = Math.random() * total;
      let cum = 0;
      for (const id of Object.keys(deg).map(Number)) {
        cum += deg[id];
        if (cum >= r && !chosen.has(id) && id !== i) { chosen.add(id); break; }
      }
    }
    for (const t of chosen) {
      edges.push({ source: i, target: t });
      deg[i]++; deg[t]++;
    }
  }
  return { nodes, edges };
}
```

---

## 4. Sources of real data (for when authenticity matters)

When an artifact genuinely needs real-world data, curated open sources include:

- **U.S. Bureau of Labor Statistics** — employment, wages, CPI
- **Federal Reserve (FRED)** — economic time series, 800,000+ series
- **World Bank Open Data** — development indicators by country
- **Our World in Data** — long historical time series across many topics
- **GADM / Natural Earth** — geographic boundary datasets
- **OpenStreetMap** — worldwide geographic data
- **UN Data** — population, economy, health
- **Kaggle datasets** — community-curated across thousands of topics
- **Hugging Face Datasets** — ML-focused, many domains
- **arXiv metadata** — scientific paper metadata
- **GitHub public data (via BigQuery)** — repositories, commits, contributors
- **Reddit, HackerNews archives** — social conversation data
- **US Census / American Community Survey** — demographic data
- **NOAA / NASA** — weather, climate, satellite
- **IMDb, TMDB** — film metadata
- **Project Gutenberg / HathiTrust** — historical text
- **Kaggle's built-in datasets** — curated starting points

When using real data:
- Cite the source in the artifact
- Note the snapshot date
- Respect licenses
- Don't fabricate "real-looking" stats — synthetic should be labeled synthetic

---

## 5. Anti-patterns with example data

- **Fabricating realistic-looking real data** — if your chart claims "Source: Bureau of Labor Statistics" but the data is invented, that's fraud. Label synthetic as synthetic.
- **Using the same example data everywhere** — every artifact using Apple stock prices or the iris dataset reads as template.
- **Ignoring the messy reality** — real data has gaps, outliers, and quirks. Synthetic data that's too clean produces unrealistic artifacts.
- **Overly simple data** — 5 rows don't stress-test a chart or a UI. Generate 100-1000 for real evaluation.
- **Ignoring scale realism** — a dashboard shouldn't claim to represent a company with 50M revenue if all numbers suggest a hobbyist project.

---

## 6. Cross-references

- `references/libraries/visualization-grammar.md` — what to do with these shapes
- `references/medium-playbooks/data-visualization.md` — operational chart guidance
- `assets/datasets/` — if the repo grows actual JSON files, store them here

---

## 7. Extending this corpus

Add shapes, examples, or generators when:
- The shape represents a distinct analysis space not covered
- The example is clearly illustrative
- The generator pattern produces realistic-feeling data

Avoid:
- Large real datasets (they belong elsewhere)
- Specific proprietary data
- Trivial variations

The goal: a creator can reach here, pick a shape and generator that fits, and not use the same data-shape every artifact.

<!-- END: references/libraries/dataset-corpus.md -->

---


<!-- BEGIN: references/libraries/iconography-library.md -->

# Iconography Library

A platter of visual languages, not a recommended set. Icons are a compressed visual vocabulary — which vocabulary the artifact speaks is a craft decision that deserves more deliberation than "import from lucide-react."

> See `references/how-to-use-this-system.md` for the platter principle.

---

## 1. Iconography theory

### What icons are for

- **Recognition before reading** — an icon read faster than its label
- **Categorical identity** — a small visual that means "this kind of thing"
- **Spatial compression** — fit more information in the same surface
- **Brand texture** — consistent icon style reinforces identity
- **Crossing language barriers** — some icons transcend (though fewer than designers often assume)

### What icons are not

- **Decoration** — if an icon earns no information, it costs attention
- **Universal symbols** — most "universal" icons are cultural (a floppy disk for "save" is opaque to anyone under 25)
- **Substitutes for labels** — most icons are clearer with a label; label-only is often clearer than icon-only
- **Aesthetic fillers** — dropping a sparkle icon next to every heading is noise

### Design dimensions

- **Line weight** — hairline, regular, bold, heavy. Must be consistent within a set.
- **Corner style** — sharp, rounded, varied
- **Level of abstraction** — realistic (iconic) vs. symbolic (abstract)
- **Fill vs. stroke** — outlined, filled, two-tone, duotone
- **Grid** — icons designed on a shared pixel grid (24×24 standard; some use 16, 20, 22, 32)
- **Optical adjustment** — visual sizes don't match geometric sizes; practitioners manually tune so a circle and a square "feel" the same visual weight

### The consistency imperative

Mixing icons from different sets is the single most common failure. A feather icon next to a lucide icon next to an emoji next to a custom SVG — each perfect on its own, together jarring. **Pick one set per artifact.** If you need an icon not in the set, draw one in the set's style.

---

## 2. Major icon systems

A spread of available options. Each has a distinct voice.

### Lucide (formerly Feather fork)
- **Voice:** clean, neutral, linear, approachable
- **Line weight:** 1.5px (consistent)
- **Grid:** 24×24
- **Style:** outlined, geometric; feels friendly without being cartoonish
- **Reach:** ~1,500 icons
- **Where:** most commonly the default in React/design-system contexts
- **Strengths:** wide coverage, open-source, MIT licensed, tree-shakable React package
- **Weaknesses:** ubiquitous → low differentiation

### Phosphor
- **Voice:** flexible, multi-weight (thin, light, regular, bold, fill, duotone)
- **Line weight:** varies by weight
- **Grid:** 256-based (designed for scaling)
- **Style:** geometric, friendly
- **Reach:** ~9,000 icons across weights
- **Strengths:** weight variety allows in-artifact tonal shift without changing set

### Heroicons
- **Voice:** companion to Tailwind CSS; three styles (outline, solid, mini, micro)
- **Line weight:** 1.5px outlined; filled for solid
- **Grid:** 24×24 (and 20×20 mini, 16×16 micro)
- **Strengths:** perfectly matched sizes for Tailwind utilities

### Radix Icons
- **Voice:** minimal, 15×15 grid (tiny)
- **Style:** precise, UI-tuned
- **Strengths:** pairs with Radix UI components; very small; good for dense interfaces

### Tabler Icons
- **Voice:** clean, neutral, well-executed
- **Line weight:** 2px
- **Grid:** 24×24
- **Reach:** ~5,000 icons
- **Strengths:** large set, consistent voice

### Remix Icons
- **Voice:** neutral, two styles (line and fill)
- **Style:** similar to Phosphor in neutrality
- **Strengths:** open source, large set

### Feather Icons (predecessor to Lucide)
- **Voice:** cleaner, lighter-weight feel than most
- **Line weight:** 2px stroke but visually lighter
- **Grid:** 24×24
- **Reach:** ~287 icons (small)
- **Strengths:** restraint; recognizability
- **Weaknesses:** small set; maintained by the community as Lucide now

### Font Awesome
- **Voice:** the biggest, densest; several styles (solid, regular, light, thin, duotone)
- **Reach:** ~30,000 icons (paid tiers)
- **Strengths:** comprehensiveness
- **Weaknesses:** visual over-saturation; can feel heavy

### Material Symbols / Material Icons
- **Voice:** Google's system; four style axes (fill, weight, grade, optical size)
- **Grid:** 24×24 or 20×20
- **Style:** geometric, clean
- **Strengths:** variable font format; scales cleanly
- **Weaknesses:** visually tied to Google's product aesthetic

### SF Symbols (Apple)
- **Voice:** Apple's native; thousands of icons
- **Grid:** varies
- **Style:** integrated with San Francisco typeface weights
- **Strengths:** immaculate pairing with Apple typography; automatic weight matching
- **Where:** Apple platforms natively

### Bootstrap Icons
- **Voice:** companion to Bootstrap; neutral
- **Style:** bold, filled, geometric
- **Reach:** ~2,000 icons

### Carbon Icons (IBM)
- **Voice:** IBM Design Language's companion
- **Style:** precise, geometric
- **Grid:** 16, 20, 24, 32
- **Strengths:** multiple sizes; well-executed at small sizes

### Iconoir
- **Voice:** neutral, outlined
- **Line weight:** 1.5px
- **Grid:** 24×24
- **Reach:** ~1,300 icons
- **Strengths:** free, MIT licensed; pleasant default

### Bootstrap's alternative, Akar Icons
- **Voice:** refined, slightly editorial
- **Line weight:** 1.5-2px
- **Style:** outlined, geometric

### Eva Icons
- **Voice:** clean, modern
- **Line weight:** 1.5-2px
- **Reach:** ~480 icons

### Atlassian (custom)
- **Voice:** crisp, corporate-friendly
- **Context:** tied to Atlassian's design language

---

## 3. Historic / cross-domain icon traditions

### Isotype (Otto Neurath, 1930s)

International System of Typographic Picture Education. Aimed at a universal pictorial language.

- Each icon represents **one unit** of something (a figure = 1,000 people)
- Quantities shown by repeating icons, not by resizing
- Rigorous visual vocabulary — not symbols, not abstractions, but stylized figures
- Designed by Gerd Arntz

**Lessons:**
- Repetition beats size for quantity
- Consistent style across an entire visual language
- Political intent: making information accessible to the non-literate

**Contemporary descendants:** Isotype revivals in data journalism; waffle charts; some infographic traditions.

### Susan Kare's original Mac icons (1983)

Designed for the original Macintosh at pixel-level resolution. Used pixel constraints as aesthetic.

- Bold, charming, memorable
- Constrained palette (bitmap only)
- Recognizable at 32×32

**Lessons:**
- Constraint as design
- Character possible within severe limits
- The trash can, the pointing hand — icons that shaped conventions for decades

### AIGA / DOT pictograms (1974)

American Institute of Graphic Arts designed a pictogram system for US transportation, later adopted internationally.

- Symbols for facilities (restroom, elevator, baggage, etc.)
- Highly abstracted human figures
- Designed for cross-language communication in airports and public spaces

**Lessons:**
- Icons work best when they are functionally unambiguous
- Public signage is a serious design domain; apex public-facing icons are rare but obvious when encountered

### Olympic pictograms

Each Olympics commissions a unique set of sports pictograms. Munich 1972 (Otl Aicher) set the template; subsequent Games have varied.

- Each set a coherent visual language
- Balance between recognition (cycling, running, swimming) and identity (games-specific style)

**Lessons:**
- Even constrained symbolic sets can have strong identity
- Coherent rules (all line weight, all grid, all color) make a set feel designed rather than assembled

### Historical manuscript marginalia

Medieval manuscripts feature an enormous vocabulary of marginal images: drôleries, floral ornaments, hand-drawn indicators (manicules — pointing hands). These inspired later typographic symbols.

**Lessons:**
- Secondary visual marks can carry meaning beyond the primary text
- Custom drawing for the specific context adds identity

### Road signs (Worboys, Fletcher, Kinneir & Calvert)

Modern road signage systems (1960s UK, etc.) are some of the most carefully designed public iconography.

**Lessons:**
- Meaning is often encoded in shape (circle = prohibition; triangle = warning; rectangle = information)
- Color coding is secondary; shape primary
- Contrast ratios carefully calibrated for distance reading

### Cartographic symbols

Map symbols have centuries of tradition — the symbol for a church, a well, contour lines, cliffs.

**Lessons:**
- Visual conventions can be deeply culturally embedded
- Legend-based systems can represent huge information surfaces

### Medical pictogram traditions

Medical communication has produced several specialised pictogram systems, each designed to bridge a specific literacy or language gap. The traditions matter because they are *evidence-based* — empirically validated for comprehension across reader populations.

**USP DI medication pictograms** — published by the United States Pharmacopeia in the 1980s; standardised under ISO 9186 (graphical-symbol comprehension testing). Each pictogram represents a specific medication-administration instruction: *take with food*, *take on empty stomach*, *do not crush*, *avoid alcohol*, *store in refrigerator*, *take at bedtime*, *for external use only*. The set is open-licensed and widely adopted.

**Lessons:**
- Empirically validated symbols outperform designer-novel symbols across reader populations
- A standardised set, even if individually unloved, has cumulative trust value
- ISO 9186 testing methodology (comprehension > 67% in target population) is the bar; rule-of-thumb design is not

**Hesperian Foundation low-literacy illustrations** — developed for *Where There Is No Doctor* (1970) and its sister volumes. Line drawings with intentional cultural neutrality (skin tones implied through line weight, not colour; clothing and setting deliberately generic); ultra-low line count (the illustration must read at degraded photocopy quality); body postures and gestures emphasising the *action* the reader should take, not the *anatomy*.

**Lessons:**
- The illustration is part of the reading; for low-literacy readers, it is often the dominant channel
- Design for the artifact's actual reproduction quality — photocopies, faxes, screen-readers
- Cultural neutrality is *more* work than cultural specificity, not less

**Vanderbilt pictographic prescription labels** — research-validated US-specific pictograms for prescription instructions. Developed at Vanderbilt University with comprehension testing across low-literacy and English-second-language populations. Each pictogram covers a specific instruction (*take once a day*, *take twice a day with food*, *take when needed*) and has been shown in randomised trials to improve adherence over text-only labels.

**Lessons:**
- The "validated by RCT" bar exists for icons too, and the bar matters
- Locale-specific validation matters — pictograms validated in one country may not transfer

**FIP pharmaceutical icons** — the International Pharmaceutical Federation's globally-developed icon set for medication instructions. Designed with input from pharmacists in dozens of countries; intended for cross-locale use. Open-access; updated periodically as comprehension testing surfaces failures.

**Lessons:**
- Cross-locale icons require ongoing testing; cultural drift is real
- Open-access institutional sets often outperform commercial ones in this domain because the testing budget is collective

**Where to deploy:** patient-facing artifacts whose readership includes low-literacy, low-numeracy, or English-second-language readers. Specifically: discharge instructions, medication labels, public-health materials, vaccine information statements, hospital-system patient portals serving diverse populations.

**Where not to deploy:** clinician-facing artifacts (the audience reads dense text efficiently; pictograms add noise without adding signal); investor-facing biotech materials (the audience expects technical density).

### Scientific diagramming

Chemistry structural formulas, electrical schematic symbols, music notation, dance notation (Laban), knitting charts, crochet charts.

**Lessons:**
- Domain-specific icon languages can be immensely expressive
- Adopting a traditional notation grounds your artifact in a field's craft

---

## 3b. Clinical algorithm glyphs

A small, stable vocabulary of glyphs has accumulated around clinical algorithms, pathway maps, triage views, and patient-safety artifacts. The glyphs are *operational* — each carries a specific clinical meaning that is read at a glance by a trained clinician. Using the wrong glyph for a clinical context is a category error that signals the artifact was assembled by someone outside the tradition. The glyphs below are the load-bearing ones; the corresponding visualization-grammar conventions live in `references/libraries/visualization-grammar.md` § Clinical algorithm and pathway forms.

### 3b.1 Pentagonal home-plate connector

A pentagon shape oriented with its point facing the direction of flow (right for left-to-right algorithms; down for top-to-bottom). The connector indicates that the algorithm continues in another document, on another page, or on another screen. The pentagon's directional shape encodes *"continue here in another diagram"* without consuming the local diagram's space. Apex deployment labels the pentagon with the target algorithm's name (*"Acute STEMI pathway — Figure 2"*); under-deployment leaves the pentagon unlabelled, forcing the reader to guess where the arrow leads. The convention originates in ANSI X3.5-1970 and ISO 5807; *UpToDate* and BMJ Best Practice are the canonical clinical-reference deployments.

### 3b.2 ⏱ clock glyph for time anchors

A clock glyph — either the Unicode `⏱` (U+23F1, stopwatch) or a custom SVG of a clock face — marks time-anchored steps in clinical algorithms. The glyph sits to the left of the step's rectangle; the time appears either inside the badge or in a paired label. Surviving Sepsis Hour-1 Bundle uses the convention with a prominent clock-badge at the top of the algorithm (*"⏱ Hour 1"*). The AHA/ASA stroke algorithm uses the clock at each interim time-target step (*"⏱ Door-to-CT ≤ 25 min"*, *"⏱ Door-to-needle ≤ 60 min"*). The glyph should not be deployed decoratively (a clock next to a step that has no time target); deployment must encode a real time-anchor that the post-event audit can measure against. See `references/libraries/visualization-grammar.md` § 7b.4.

### 3b.3 ACC / AHA Class + LoE bracket conventions

The Class-of-Recommendation + Level-of-Evidence bracket is a typographic glyph as much as a textual annotation. The bracket pattern `[Class, LoE]` — `[I, A]`, `[IIa, B-R]`, `[IIb, C-EO]`, `[III: Harm, B-NR]` — sits to the right of or below each recommendation in an algorithm. The colour-band on the rectangle's left edge encodes the class (Class I green; IIa pale green; IIb yellow; III: No Benefit hollow red; III: Harm filled red) and must achieve WCAG AA contrast against the rectangle's fill. The bracket-and-band pair is the unit; deploying only the bracket loses the at-a-glance scanning value; deploying only the colour-band fails colour-blind readers (the colour does not survive monochrome printing or screen-reader serialisation). See `references/libraries/visualization-grammar.md` § 7b.2 for the full Class-LoE specification.

### 3b.4 Vital-sign glyphs for triage views

A small set of stable glyphs encodes the core vital signs in clinical triage and ICU dashboard contexts:

- **BP cuff** (a sphygmomanometer pictogram, often simplified to a cuff-and-gauge) for blood pressure
- **Thermometer** (mercury-style or digital silhouette) for temperature
- **O₂ saturation badge** (often a circle with `O₂` or `SpO₂` label) for pulse oximetry
- **IV bag** (a hanging bag with drip chamber) for intravenous fluid status or active infusion
- **Heart rate icon** (an ECG complex or stylised pulse waveform) for HR
- **Respiratory rate icon** (paired arrows or a stylised lung) for RR

The glyphs pair with the numerical reading; the glyph is the *category cue* for at-a-glance scanning, the number is the *measurement*. Apex deployment uses one consistent glyph set across the artifact (most often a clinical-icon set such as Healthicons or a hand-drawn set in the artifact's visual register); under-deployment mixes glyphs from disparate sources (a Lucide stethoscope next to an SF Symbol thermometer next to a custom IV bag) and produces the consistency-failure named in § 1. The Wave 11 cross-cover triage template (`templates/react-cross-cover-triage.tsx`) demonstrates the convention with an oversized SBP lede paired with the BP-cuff glyph.

### 3b.5 SBAR baton (handoff transition marker)

A small labelled token — typically a rounded rectangle or a baton-shape — placed on every handoff arrow in a swim-lane pathway map. The token carries the handoff-framework label (*SBAR* or *I-PASS*) and a colour cue indicating handoff completeness: green for *full* (all framework elements documented), yellow for *partial* (some elements present), red for *minimal* (verbal only, undocumented). The convention originates in the Wave 11 `templates/svg-patient-pathway-map.svg` and surfaces in BPMN-derived clinical pathway maps more broadly. The baton's job is to make handoff content auditable at the diagram level — red batons are the QI-relevant transitions where Joint Commission Sentinel Event 58 (2017) communication-failure patterns concentrate. See `references/libraries/visualization-grammar.md` § 7b.7 and `references/medium-playbooks/clinical-handoff.md` for the per-persona handoff discipline.

### 3b.6 Red-flag glyph

A single, severity-elevated glyph marking the *can't-miss* finding in a clinical algorithm or pathway. The convention: a red triangle with a central exclamation (the ISO 7010 W001 *general warning* glyph) or a red flag icon, paired with a one-line label naming the finding. Apex deployment reserves the glyph for *true* red flags — findings whose presence changes management dramatically (sepsis criteria triggering the Hour-1 Bundle; ACC/AHA Class III: Harm contraindications; concussion red flags from the Concussion in Sport Group consensus 2017; stroke alert criteria triggering thrombolysis evaluation). Deploying the glyph for *every* warning produces the alarm-fatigue failure (`failure-modes.md` M6); the calibration discipline is one or two red-flag glyphs per algorithm. The Wave 11 return-to-play template uses the convention at the symptom-recurrence drop-back transition; the Surviving Sepsis algorithm uses it at the lactate ≥ 4 boundary.

### 3b.7 The teach-back hand

A small hand glyph (often a palm-out hand or a pointing-back hand) marking points in a patient-facing artifact where the *teach-back* discipline has been satisfied — the clinician has confirmed patient comprehension by asking the patient to paraphrase the instruction in their own words. The glyph functions as a documentation marker: a discharge instruction sheet with teach-back-hand glyphs at each major instruction signals that comprehension was checked, not assumed. The convention is emerging in the Ariadne Labs Serious Illness Care Programme materials (see `references/libraries/pedagogy-library.md` § Goals-of-care conversations) and in Choosing Wisely's patient-decision-aid artifacts. Apex deployment pairs the glyph with a brief text annotation (*"Comprehension confirmed via teach-back: 'Take one pill with breakfast'"*); under-deployment treats the glyph as decoration. Distinct from the standard *check* glyph because *check* means *task complete*; the teach-back hand means *patient understanding confirmed*.

### 3b.8 PHI-redaction shading

PHI (Protected Health Information) redaction in clinical-teaching artifacts and de-identified case displays follows a stable visual convention: a uniform light-grey or pale-yellow fill behind the redacted text, with the underlying text replaced by either a generic placeholder (*"[redacted: MRN]"*, *"[name]"*, *"[DOB]"*) or a representative stand-in (*"Patient A"*, *"01-Jan-1970"* for a date-shifted DOB). The shading is the visible witness to redaction; absence of shading on a de-identified case raises the question whether redaction occurred at all. Apex deployment uses one consistent shading colour across the artifact and a redaction legend in the colophon; under-deployment uses inconsistent black-bar redaction (which is the legal-document convention, not the teaching-artifact convention) or no shading at all. The Wave 11 handoff template (`templates/react-handoff-ipass.tsx`) ships a PHI-redact toggle that demonstrates the convention. HIPAA Safe Harbor (45 CFR 164.514(b)(2)) specifies the 18 identifiers requiring redaction; the visual convention is institutional rather than regulatory but stable across academic-medical-centre teaching materials.

---

## 4. Drawing your own

When the available sets don't fit:

- **Match the voice of the surrounding type.** Icons with hairline strokes paired with heavy-weight type fight.
- **Use the grid of your surrounding UI.** Usually 24×24 for 16px type; 20×20 for 14px type.
- **Constrain to the system's line weight** — if lucide is 1.5px, your custom additions are 1.5px.
- **Sketch on the optical grid.** A circle of diameter 20 on a 24 grid visually equals a square of side 16. Optical adjustment is tedious but essential.
- **Test at final size.** A symbol perfect at 96px may collapse at 16px.
- **Draw with the same tool conventions** (corner radius, stroke cap, stroke join) as the set.

---

## 5. Icon usage principles

### Sizing

Rule of thumb: icon size matches adjacent text size.
- Inline with 14-16px text: 14-16px icon
- Inline with 18-20px text: 18-20px icon
- Standalone button: text-size + 25-50%

### Pairing with text

- Icon + text together: **label the icon**. Don't rely on icon alone.
- Short labels (1-3 words) + icon: icon adds recognition
- Long labels + icon: icon often redundant; consider dropping

### Spacing

- Icon then text: 6-8px gap (smaller than word-space)
- Center-align icons with the x-height of adjacent text, not the full cap-height

### Accessibility

- `aria-hidden="true"` on icons that accompany visible text labels
- `aria-label="..."` on icon-only buttons
- Don't rely on color alone to distinguish meaning
- Make sure icon stroke width meets contrast ratios against surrounding surface

### Anti-patterns

- **An icon per heading** — pure noise
- **Mixing sets** — the #1 failure
- **Icon-only buttons without tooltip or aria-label** — accessibility failure
- **Emoji interspersed with icon set** — emoji has its own voice; it fights most icon sets
- **Using a generic "decorative" icon** when the subject would warrant a purpose-drawn mark

---

## 6. Cross-references

- `references/design-tokens.md` — typographic scale that icons size to
- `references/medium-playbooks/claude-react-artifact.md` — lucide-react usage in the Claude environment
- `references/libraries/composition-library.md` — where icons sit in layouts

---

## 7. Extending this library

Add an icon system or tradition when:
- It has a distinct visual voice
- It is actively maintained or historically significant
- It is accessible (available for use)

Avoid:
- Rounding up every minor icon pack
- Paid sets without noteworthy quality

<!-- END: references/libraries/iconography-library.md -->

---


<!-- BEGIN: references/libraries/inspiration-atlas.md -->

# Inspiration Atlas

A platter of **non-software** visual traditions, to widen what a software artifact can look like. Most AI-generated work looks like software because it has been fed software. Feeding it cartography, botanical illustration, manuscript marginalia, Swiss poster design, Japanese ukiyo-e, and mid-century advertising expands what gets imagined.

Every entry here is offered for *cross-pollination*: steal a principle, borrow a compositional move, recognize a voice — don't imitate wholesale.

> See `references/how-to-use-this-system.md` for the platter principle.

---

## 0. Rolling index — for the cross-pollination step in the operating loop

CLAUDE.md operating loop **Step 3 (Roll for cross-pollination)** asks you to sample one tradition from this atlas that is *not* native to the artifact's category, then declare whether it adopted, partially-adopted, or noted-but-rejected.

Use this numbered index as a mechanical handle when you can't think of a candidate. **Pick freely — the roll is for inspiration, not lottery.** If the digit-derived suggestion fights the artifact's job, pick a different one. The numbering exists so Claude has a way to choose *something* rather than nothing.

To roll: pick the number whose last digit matches the count of letters in the artifact's primary noun (e.g., "dashboard" has 9 letters → 9 = Blaeu atlas; "explainer" has 9 letters → 9 = Blaeu atlas; "form" has 4 letters → 4 = Japanese postwar poster). Or pick freely.

The point is to **consider** one tradition you wouldn't otherwise.

```
 1. Swiss poster                      31. Book of Kells
 2. Polish poster school              32. Lindisfarne Gospels
 3. Cuban ICAIC poster                33. Persian miniature
 4. Japanese postwar poster           34. Mughal miniature
 5. American mid-century advertising  35. Japanese emakimono
 6. Russian constructivist            36. Nuremberg Chronicle
 7. Mappae mundi                      37. Blake illuminated books
 8. Portolan chart                    38. Caldecott picture books
 9. Blaeu atlas                       39. WPA poster
10. Beck's Underground                40. Keep Calm wartime
11. Snow's cholera map                41. Atelier Populaire
12. Minard's Napoleon                 42. Cardew's Treatise (graphic notation)
13. Isochrone map                     43. Gregorian neumes
14. Cartogram                         44. Tablature (lute / guitar)
15. Penguin Classics                  45. DDB "Think Small"
16. Aldus Manutius                    46. Ogilvy long-copy
17. Massin's *Bald Soprano*           47. Saul Bass title sequence
18. Kelmscott Press                   48. Pablo Ferro typography
19. NYRB                              49. Criterion Collection covers
20. The New Yorker                    50. Myst (game)
21. Kinfolk                           51. Return of the Obra Dinn
22. Audubon                           52. Journey (game)
23. Peterson field guide              53. Disco Elysium
24. Sibley's bird guides              54. Riot Grrrl zine
25. Haeckel Kunstformen               55. Soviet samizdat
26. Da Vinci anatomy                  56. Eames *Powers of Ten*
27. Botanical plate                   57. Otl Aicher Munich '72
28. Netter's anatomy atlas            58. Vignelli MTA map
29. Geological cross-section          59. Isotype
30. Astronomical chart                60. Kenya Hara / Muji

61. BPMN 2.0 swim-lane                64. Surviving Sepsis Hour-1 Bundle
62. Lean Six Sigma VSM                65. Toyota Production System / Kaizen
63. WHO Surgical Safety Checklist     66. IHI improvement collaboratives
                                      67. VA QUERI program
```

Entries 61–67 (Process modeling and operations) are detailed in § 13b below; they belong on the cross-pollination roll for any artifact involving multi-actor sequential work, clinical pathways, operational runbooks, or process-improvement loops.

After the roll, declare in the pre-delivery YAML block:

```yaml
cross_pollination:
  tradition: "<entry from index above, or a tradition not on this list>"
  outcome: adopted | partially-adopted | noted-but-rejected
  reason: "<one specific sentence, >8 words; not 'doesn't fit' or 'felt right'>"
```

"Rejected" is a valid outcome when the tradition genuinely fights the artifact's job — but rejection without consideration is the failure mode this step exists to prevent. The 8-word reason floor exists to prevent autopilot.

### Scoping

The roll is **required** on every artifact above a complexity threshold: > 200 lines of code, > 600 words of prose, intended for any reader beyond the requester, or explicitly tagged as "apex" or "polished." Below the threshold (a 30-line tooltip widget, a 2-paragraph reply, a debugging probe), skip silently.

---

## 1. Posters

### Swiss poster (1950s-70s)

Josef Müller-Brockmann, Armin Hofmann, Emil Ruder, Max Bill. Zurich and Basel.

**What to study:** grid-driven composition; typography as graphic element; dramatic scale ratios between elements; photography used as abstraction, not narrative.

**Exemplary works:** Müller-Brockmann's Tonhalle concert posters (nested geometric forms with rigorous grid); Hofmann's Giselle ballet posters (contrast of hand-drawn element against Helvetica type).

**Transferable moves:** dramatic scale contrast, asymmetric balance, type-as-object, restrained palette.

### Polish poster school (1950s-80s)

Henryk Tomaszewski, Jan Lenica, Roman Cieślewicz, Waldemar Świerzy, Franciszek Starowieyski.

**What to study:** hand-drawn imagery; surreal juxtaposition; limited saturated palette; type integrated with illustration as unified whole; symbolic rather than literal imagery.

**Exemplary works:** Lenica's film posters (often hand-lettered, saturated color fields); Tomaszewski's collages.

**Transferable moves:** illustration as content, not decoration; symbolism; working within constrained palette.

### Cuban poster (ICAIC, 1960s-80s)

Alfredo Rostgaard, Raúl Martínez, Eduardo Muñoz Bachs.

**What to study:** flat color fields; photographic silk-screen aesthetic; psychedelic influence; socialist-optimistic register.

**Transferable moves:** saturated flat color, photographic halftones, bold type.

### Japanese poster (postwar)

Ikko Tanaka, Kohei Sugiura, Shigeo Fukuda, Tadanori Yokoo.

**What to study:** minimalism balanced with bold color; cultural motifs (ukiyo-e, calligraphy) integrated into modernist composition; playfulness with serious intent; extreme precision.

**Exemplary works:** Tanaka's Nihon Buyo (1981) — silhouette of a geisha from geometric primitives; Fukuda's Victory 1945 poster (bullet reversing toward cannon).

**Transferable moves:** visual pun; geometric abstraction of a figurative subject; extreme restraint.

### American mid-century advertising

Push Pin Studios (Milton Glaser, Seymour Chwast); Paul Rand; Saul Bass; Herb Lubalin.

**What to study:** conceptual cleverness paired with typographic craft; the "big idea" philosophy; integrated type + image; restraint in service of impact.

**Exemplary works:** Glaser's "I ❤ NY" logo; Rand's IBM, ABC, Westinghouse logos; Bass's AT&T logo; Lubalin's typographic experiments.

**Transferable moves:** conceptual compression; logotype as identity; typographic invention.

### Russian constructivist

El Lissitzky, Alexander Rodchenko, Varvara Stepanova, Gustav Klutsis (1920s-30s).

**What to study:** geometric abstraction; photomontage; angled typography; flat saturated palette; political urgency.

**Exemplary works:** Lissitzky's "Beat the Whites with the Red Wedge" (1919); Rodchenko's book covers and film posters.

**Transferable moves:** angled elements, block typography, photomontage, urgency through composition.

---

## 2. Maps and cartography

### Historical cartography

- **Ancient and medieval maps** — mappae mundi, portolan charts. Not geographically accurate — symbolic, narrative, religious. Illuminated and illustrated.
- **17th-18th-century European atlases** — Mercator, Ortelius, Blaeu. Decorative cartouches, elaborate scale bars, sea monsters.
- **Nautical charts** — precise, functional, overlaid with depth soundings, rhumb lines, navigational aids.
- **Pictorial maps** — 20th-century travel, WPA-era American state maps, children's book maps. Stylized, informative, friendly.

### Modern cartography

- **Arthur H. Robinson's projections** — Robinson projection; thoughtful compromise between accuracy and appearance
- **Jerry Brotton's historical survey** (*A History of the World in Twelve Maps*)
- **Alberto Cairo's writing** on cartographic visualization
- **Harry Beck's London Underground map (1933)** — radical abstraction; geography sacrificed for legibility. The exemplar of functional diagram over accurate representation.
- **Max Huber's Swiss maps and infographics**
- **Contemporary cartographic design** — Stamen's map tiles; Mapbox studio work.

**Transferable moves:**
- Legend design (how to document a visual language)
- Hierarchy of information in dense surfaces
- Abstraction when geography isn't the point (Beck's Tube map)
- The "inset" (zoomed detail within a larger context)
- Contour lines and isolines (encoding continuous fields with discrete lines)

### Data-as-map

- **Minard's Napoleon chart** (already a tear-down; study again here as cartography)
- **Snow's cholera map (1854)** — London Broad Street pump; classic dot-density geographic story
- **Hans Rosling's gapminder bubble maps** — time + geography + two variables in one animated view
- **Isochrone maps** — contours of travel time from a point (instead of distance)
- **Cartograms** — distort geography to encode a variable (Worldmapper)

---

## 3. Books and editorial traditions

### Classic publishers

- **Penguin Classics** — Jan Tschichold's mid-century redesign; orange and black; clear typographic grid; Romek Marber's covers
- **Pelican Books** — Penguin's educational line; distinctive blue
- **Aldus Manutius (15th-16th century)** — pocket editions; italic type; colophon pages; the origin of modern book design

### Editorial design

- **Robert Massin's *The Bald Soprano* (1964)** — Ionesco's play laid out typographically as stage direction; type becomes character
- **William Morris and the Kelmscott Press** — revival of medieval book design aesthetic
- **Beatrice Warde's "Crystal Goblet" (1932)** — essay on typographic restraint
- **Massimo Vignelli's *Graphic Design for Non-Profit Organizations***

### Contemporary editorial design

- **Kinfolk, Cereal, Apartamento** — minimal, editorial, sub-publishing
- **The New York Review of Books** — typographically austere, long-form serif
- **The New Yorker** — Irvin typeface, editorial illustration tradition, distinctive covers
- **Graphic Design USA annual**
- **Eye Magazine** (UK design publication)

**Transferable moves:**
- Display type as identity
- Caption-as-essay (the caption of a figure carrying significant information)
- Full-page openers with restraint
- Dropped capitals, pull quotes, sidebars
- The "reading room" aesthetic — serifs, generous leading, restrained color

---

## 4. Field guides and scientific illustration

### Classic field guides

- **John James Audubon's *Birds of America* (1827-1838)** — life-sized illustrations, scientific rigor, dramatic composition
- **Roger Tory Peterson's *A Field Guide to the Birds* (1934)** — the modern pocket field guide format; arrow-pointing identifying features; side-by-side comparison
- **David Sibley's guides** — highly refined illustrations; side-by-side comparisons; behavioral annotations

### Scientific illustration

- **Ernst Haeckel's *Kunstformen der Natur* (1904)** — radiolaria, jellyfish, algae as art; symmetry and pattern
- **Leonardo da Vinci's anatomical drawings**
- **Botanical plates** — traditional botanical illustration conventions: life-size or scale-noted; parts annotated; line-drawn habit; detailed flower cross-sections
- **Medical atlases** (Netter's, Gray's) — anatomical illustration traditions
- **Geological cross-sections** — encoding rock layers with pattern
- **Astronomical charts** — historical celestial atlases; modern survey projections

### Contemporary scientific illustration

- **Scientific American**'s illustration tradition
- **Quanta Magazine**'s commissioned figures
- **The Huntington Library's botanical art program**

**Transferable moves:**
- Annotated specimen (image + labeled parts + scale bar + context)
- Side-by-side comparison showing variation
- Stylization that increases identifiability over photographic realism
- Scale bars, orientation indicators, context panels

---

## 5. Manuscripts and marginalia

### Illuminated manuscripts (medieval European, Islamic, Armenian, Ethiopian, Persian, Indian)

- **Book of Kells (c. 800)** — Celtic illumination
- **Lindisfarne Gospels**
- **Persian miniatures** (14th-17th century)
- **Mughal miniature painting**
- **Japanese illustrated scrolls** (emakimono)

**What to study:** integration of text and illustration; the initial letter (dropcap) as art; marginal illustrations (drolleries); gold leaf and rich pigments; deliberate ornamental borders.

**Transferable moves:**
- The decorated opening
- Marginalia (side notes, hand-drawn indicators, asides in smaller type)
- Rich color as a signal of importance
- Integration of text-as-image

### Printed books' first centuries

- **Nuremberg Chronicle (1493)** — illustrated history with hundreds of woodcuts
- **William Blake's illuminated books** — text and image entirely integrated
- **Early children's books** (Randolph Caldecott, Kate Greenaway)

---

## 6. Propaganda graphics (study, not endorsement)

The craft of propaganda graphics is worth studying separately from the politics. The compression, urgency, and visual intelligence of mid-20th-century propaganda (from all political orientations) is instructive — they were designed by serious graphic designers working under severe constraints.

- **WPA posters (1935-43)** — New Deal public art; muted flat color; educational
- **British wartime posters** ("Keep Calm and Carry On") — austere, letterpress-feeling
- **Soviet posters** (Rodchenko, Lissitzky) — constructivist aesthetic
- **American wartime propaganda** (Norman Rockwell, Ben Shahn)
- **Mao-era Chinese posters** — saturated flat color, heroic realism
- **Atelier Populaire** (May 1968, Paris) — silkscreen posters; handmade urgency

**Lessons:** single message per poster; dramatic hierarchy; color as emotion; the relationship between restraint and urgency.

---

## 7. Music notation and graphic scores

- **Traditional Western notation** — five-line staves, notes, key signatures — an extraordinary condensed information language
- **Graphic scores** (John Cage, Karlheinz Stockhausen, Cornelius Cardew's *Treatise*) — scores as visual art; duration, pitch, and gesture encoded non-literally
- **Tablature** for guitar, lute, other instruments
- **Neumatic notation** (Gregorian chant) — the ancestor of modern notation

**Transferable moves:**
- Encoding sequence in space
- Multi-dimensional encoding along axes
- Conventional symbols learned once, applied thousands of times

---

## 8. Advertising history

- **Mid-century American (DDB, Bill Bernbach)** — "Think Small" (VW); "Lemon" (VW); wit + typography
- **Japanese mid-century** — Shinozaki, Tanaka; restraint + bold color
- **1960s UK (Alan Fletcher, Colin Forbes, Bob Gill)** — wit, restraint, typographic cleverness
- **Ogilvy's long-copy advertising** — "At 60 miles an hour the loudest noise in this new Rolls-Royce comes from the electric clock"
- **1990s-2000s British (AMV BBDO, Fallon London)** — brand films, conceptual craft

---

## 9. Film, television, and motion graphics

- **Saul Bass title sequences** — *Vertigo*, *Psycho*, *Anatomy of a Murder*; kinetic typography; abstraction
- **Kyle Cooper** — *Se7en*, *The Island of Dr. Moreau*; distressed aesthetic; typographic storytelling
- **Pablo Ferro** — *Dr. Strangelove*, *Bullitt*; hand-drawn kinetic typography
- **Bureau Oberhäuser, Golden Wolf, Psyop, Buck** — contemporary motion graphics studios
- **Criterion Collection** — film cover design; editorial tradition
- **The Zodiac Tapes** — title sequence work
- **Daniels (Swiss Army Man, Everything Everywhere)** — music videos; kinetic craft

---

## 10. Games and interactive

- **Myst** (1993) — environmental storytelling; minimal UI; puzzles embedded in beautiful scenes
- **Journey** (2012) — emotional arc; minimalism; wordless narrative
- **Return of the Obra Dinn** (2018) — 1-bit aesthetic; investigative gameplay; distinctive visual language
- **Katamari Damacy** series — aesthetic charm, UI playfulness
- **Celeste, Hades, Disco Elysium** — indie titles whose UI and visual language reward study
- **Braid** (2008) — time-mechanic as game + narrative
- **Board game design** — Reiner Knizia, Uwe Rosenberg; rule card design; component aesthetics

---

## 11. Zines, samizdat, vernacular

- **Riot Grrrl zines** (1990s) — punk aesthetic, photocopy texture, collage
- **Soviet samizdat** — typewritten, mimeographed, hand-bound; the aesthetic of necessity
- **Fanzines** — handmade production as aesthetic
- **Mimeo revolution (1960s-70s)** — cheap printing enabling grassroots publishing
- **Contemporary zines** — Brain Dead, It's Nice That, small press
- **Chapbook tradition** — poetry publishing; handmade covers

**Transferable moves:** embracing texture and imperfection; text as image; raw energy; low-resource polish.

---

## 12. Architectural drawing and industrial design

- **Plans, sections, elevations** — architectural drawing conventions: line weights; hatching conventions; annotation; scale bars
- **Axonometric and isometric views** — 3D without perspective
- **Technical drawings** (Eames office, Dieter Rams's Braun work) — exploded views, section drawings
- **Rendering traditions** (Frank Lloyd Wright's watercolors; contemporary architectural rendering)
- **Infographic-quality architectural diagrams** (Atlas of the Functional Organization of the Built Environment)

**Transferable moves:** exploded views; hatching as texture; precise annotation; crossed lines indicating scale or material.

---

## 13. Vernacular design

- **Roadside America** (diners, motels, gas stations of mid-century USA)
- **Folk lettering** (hand-painted signs; barn-side advertising; traveling circus posters)
- **Signage in cities around the world** (Japanese neon; Mexican hand-painted lettering; Indian film posters; African sign painting — Ghana's Nicholas Amonoo-Neizer; Frederick Ebony)
- **Ephemera** (bus tickets, matchbooks, tea labels, postage stamps, currency design)

---

## 13b. Process modeling and operations

The operations-and-improvement traditions — born in Toyota's Nagoya factories, refined in aviation and surgical safety, codified in BPMN and Lean Six Sigma — produced a visual vocabulary that travels well into clinical and complex-systems artifacts. The traditions share a discipline: *the diagram is the work*. A swim-lane map is not a description of a process; it is the artifact the process improvement is built against. A checklist is not a reminder; it is the cognitive prosthetic that prevents the failure. The transferable moves are operational; the traditions deserve more daylight in artifacts that involve any sequence-of-actors process.

### BPMN 2.0 swim-lane diagrams

Business Process Model and Notation, version 2.0 (Object Management Group standard ISO/IEC 19510:2013), is the contemporary standard for diagramming multi-stakeholder operational processes. The notation provides a structured vocabulary: pools (organisations), lanes (roles within an organisation), events (start / intermediate / end), tasks (work to be performed), gateways (decisions and parallel splits), data objects, and message flows. The vocabulary is large; the discipline is to use a small consistent subset for each diagram.

**What to study.** The lane-as-actor convention; the consistent left-to-right time flow; the explicit handoff arrows at every cross-lane transition; the gateway diamond as the *only* decision shape; the structured event vocabulary (timer events, message events, error events) that lets exception flows be diagrammed without cluttering the happy path.

**Transferable moves.** Multi-stakeholder pathway diagrams in healthcare (the Wave 11 SVG-patient-pathway-map template), incident-response runbooks in operations, customer-journey maps in product design, regulatory-submission workflows. The swim-lane visual itself is the analytical artifact — the gaps between handoffs are where waste, delay, and error concentrate.

**Reference.** OMG BPMN 2.0 specification (omg.org/spec/BPMN); Bruce Silver's *BPMN Method and Style* (2nd ed. 2011) for operational discipline; the NHS Improvement *Pathway Mapping* guide (2005) for clinical adaptation.

### Lean Six Sigma value-stream mapping

Value-stream mapping (VSM), originated at Toyota and codified for non-Japanese audiences by James Womack and Daniel Jones in *Lean Thinking* (1996; 2nd ed. 2003), is the discipline of diagramming a complete value-producing process — from raw material to finished delivery — with the explicit goal of distinguishing *value-added* time from *waste*. The visual: a horizontal flow of process boxes (each annotated with cycle time, changeover time, uptime, and operator count), with inventory triangles between boxes representing work-in-progress, push/pull arrows for material flow direction, and a *timeline ladder* at the bottom showing value-added time on the upper rung and waste time on the lower rung.

**What to study.** The ratio at the timeline ladder's right edge — typically *"450 min total lead time; 9 min value-added; 1.96% efficiency"* — is the diagnostic. The waste isn't hidden; it's the dominant element. The current-state map (CSM) and the future-state map (FSM) sit side-by-side; the gap between them is the improvement project's charter.

**Transferable moves.** Any analysis that asks *"where does the time go?"* — software-deployment pipelines, clinical-pathway latency analysis, customer-service workflows, scientific-publication pipelines (the *"submitted → published"* timeline at major journals). The discipline of explicitly *measuring* waste, not just acknowledging it.

**Reference.** Mike Rother & John Shook, *Learning to See* (1999; Lean Enterprise Institute) — the canonical VSM workbook with the standard visual conventions.

### The WHO Surgical Safety Checklist

Atul Gawande's collaboration with the World Health Organization produced the Surgical Safety Checklist (Haynes, Weiser *et al.*, *N Engl J Med* 2009;360:491) — a 19-item, three-pause-point checklist (sign-in before anaesthesia; time-out before incision; sign-out before patient leaves OR). The before-and-after observational data across eight hospitals in eight countries showed mortality reduction from 1.5% to 0.8% and inpatient-complication reduction from 11% to 7%. The checklist's lineage is explicit aviation: the cockpit pre-takeoff checklist culture, traceable to Boeing's response to the 1935 B-17 crash that killed test pilot Ployer Hill.

**What to study.** The visual: one page, large type, three columns for the three pause points, ticks for completion, a named *checklist captain* responsible for running it. The discipline: *"sign-in"* is verbal, not paper-only; every team member is named aloud; the checklist is read, not paraphrased. Gawande's *The Checklist Manifesto* (2009) articulates the underlying argument — checklists work because they offload cognitive load from working memory to a structured artifact, freeing the expert's attention for the non-routine.

**Transferable moves.** Any complex-procedural artifact whose failure mode is *omission*: software-deployment runbooks, scientific-experiment protocols, journalism fact-check workflows, accounting close-of-period checklists, post-incident review templates. The artifact is the cognitive prosthetic; the form is one page, ordered, ticked.

**Reference.** *Safe Surgery 2015* (Gawande, World Health Organization); the Argonne National Lab and NASA pre-launch checklist traditions for the aviation/aerospace lineage.

### The Surviving Sepsis Hour-1 Bundle

The Surviving Sepsis Campaign — a multinational guideline initiative co-sponsored by the Society of Critical Care Medicine and the European Society of Intensive Care Medicine — produced the Hour-1 Bundle (Evans, Rhodes *et al.*, *Crit Care Med* 2021;49:e1063) as a time-anchored care package: five actions to be completed within the first hour of sepsis recognition. The bundle's design is a deliberate tradition export — the aviation/Apollo *time-critical bundle* (the *"go-no-go"* poll at T-minus-9 minutes for a Saturn V launch) adapted to bedside resuscitation.

**What to study.** The visual convention (already documented in `references/libraries/visualization-grammar.md` § 7b.4): a prominent clock badge anchors the entire algorithm to the time-zero event; each sub-step carries a time-target annotation; post-event audit compares actual times against the targets. The before-and-after evidence is dramatic — implementation studies show mortality reductions of 20–30% — but the lesson for artifact design is the *visible time-anchor*: the diagram says *what to do by when*, not just *what to do*.

**Transferable moves.** Time-anchored algorithms beyond sepsis: stroke alert pathways (door-to-CT ≤ 25 min; door-to-needle ≤ 60 min), STEMI activation (door-to-balloon ≤ 90 min), trauma activation (golden hour), incident-response runbooks with time-bounded escalation, deployment-rollback procedures with mean-time-to-recovery targets.

**Reference.** Surviving Sepsis Campaign guidelines (current 2021 update); Levy *et al.*, *Crit Care Med* 2018;46:997 for the bundle-implementation evidence.

### Toyota Production System / Kaizen origins

The Toyota Production System (TPS), articulated by Taiichi Ohno in *Toyota Production System: Beyond Large-Scale Production* (Japanese 1978; English 1988), is the foundational text of Lean. The TPS rests on two pillars (*just-in-time* and *jidoka* — autonomation) and a third principle that became *kaizen* in the global translation: *continuous improvement* through worker-led, small, daily changes to the process. Kaizen is *not* the big improvement project; it is the *thousand small improvements* that compound over years.

**What to study.** The visual culture: the *andon* cord (any worker can stop the line; the cord's pull triggers a visible signal; the team converges to solve the problem before the line restarts); the *kanban* card (a physical token representing one unit of pull-signal demand; cards move; the visual *flow* of cards is the production schedule); the *5S* workstation discipline (sort, set in order, shine, standardise, sustain) producing visually uncluttered workspaces. The *5 Whys* root-cause discipline (ask *"why"* five times in sequence; the answer to the fifth *"why"* is usually a system flaw, not a person's mistake) is a Toyota invention now ubiquitous in incident-response retrospectives.

**Transferable moves.** Workplace-as-artifact thinking: the deployment dashboard whose visual state *is* the production schedule; the incident-response runbook whose *5 Whys* template is the post-mortem chassis; the QI A3 report (single A3-size sheet of paper holding the entire improvement project — problem, root cause, countermeasure, metrics, follow-up). The A3 in particular is a forgotten apex artifact form deserving revival.

**Reference.** Ohno 1978/1988; Jeffrey Liker, *The Toyota Way* (2004); John Shook, *Managing to Learn* (Lean Enterprise Institute 2008) for the A3 form.

### IHI improvement collaboratives

The Institute for Healthcare Improvement (IHI), founded by Don Berwick in 1991, developed the *Breakthrough Series Collaborative* model — a structured, time-bounded, multi-institution improvement project in which teams from 20–40 institutions work in parallel on a shared improvement aim, supported by a faculty of experts. Berwick's 2003 *JAMA* commentary (*"Disseminating innovations in health care"*, *JAMA* 2003;289:1969) articulated the diffusion-of-innovations theory underlying the model.

**What to study.** The visual artifacts: the *driver diagram* (primary drivers → secondary drivers → change ideas, laid out as a horizontal tree from the aim on the left to actionable changes on the right); the *run chart* (the dominant QI visualisation — time series with the median line, annotated with rules for distinguishing signal from noise: 8-point shift, 6-point trend, 14-point oscillation); the *Statistical Process Control (SPC) chart* (run chart with upper and lower control limits at ±3σ). These visualisations are the QI counterpart to the scientist's hypothesis test — they let the team distinguish real improvement from random variation.

**Transferable moves.** Improvement-collaborative thinking: the multi-team artifact (a dashboard tracking all participating teams against the shared aim); the driver-diagram visualisation (applicable to any *"what changes will produce the outcome we want"* analysis); the run-chart-as-default for any longitudinal-measurement artifact (replaces the bar chart's snapshot framing with a continuous narrative).

**Reference.** Provost & Murray, *The Health Care Data Guide* (2011) — the canonical run-chart and SPC-chart reference; IHI's *The Breakthrough Series* white paper (2003).

### VA QUERI program

The US Department of Veterans Affairs *Quality Enhancement Research Initiative* (QUERI), launched in 1998, operationalises an explicit *knowledge-to-implementation-to-measurement* loop. The QUERI six-step model: identify high-priority condition → identify best practices → identify clinical-practice variation → identify and implement interventions to promote best practices → document feasibility, efficiency, and effectiveness → measure impact on health-related quality of life. The model is the largest sustained implementation-science programme in US healthcare; its publication output runs to several thousand papers across two decades.

**What to study.** The conceptual artifact: the explicit *loop* between research, implementation, and measurement — research that does not feed back into implementation is treated as incomplete; implementation that does not feed back into research is treated as undisciplined. The visual artifacts: the *logic model* (inputs → activities → outputs → outcomes → impact, with arrows and feedback loops), the *RE-AIM framework* (*Reach × Efficacy × Adoption × Implementation × Maintenance*) as a five-axis radar plot for evaluating implementation projects, the *PARiHS framework* (*Promoting Action on Research Implementation in Health Services*) as a 2D evidence-context plot positioning implementation projects on axes of evidence quality and context readiness.

**Transferable moves.** Any artifact that must integrate research-and-practice: open-source-software development with research deployment; pharmaceutical post-market surveillance; education curricula with evidence-of-effect feedback. The discipline of *naming the loop* — what feeds back into what, on what cycle — is the transferable lesson.

**Reference.** Stetler *et al.*, *Implement Sci* 2008;3:8 — the canonical QUERI model paper; Damschroder *et al.*, *Implement Sci* 2009;4:50 for the related Consolidated Framework for Implementation Research (CFIR), which complements QUERI for non-VA contexts.

**Where this section transfers.** Process-modelling traditions belong on the cross-pollination roll (§ 0) for any artifact involving multi-actor sequential work — clinical pathways, operational runbooks, deployment workflows, customer journeys, scientific protocols. The discipline that *makes the process the artifact* is the unifying move; the specific visualisation (swim lane, value stream, run chart, driver diagram, A3) is the medium-specific implementation.

---

## 14. Other worth naming

- **Otl Aicher's Munich 1972 Olympic graphics** — entire visual system
- **Milton Glaser's *Dylan* poster (1966)** — silhouette + psychedelic hair
- **Jan Tschichold's *The New Typography*** — foundational modernist tract
- **Dieter Rams's 10 principles of good design**
- **Massimo Vignelli's MTA subway map**
- **FedEx logo** (the arrow hidden between E and x) — the logo whose reveal creates delight
- **International Style architecture** (Mies van der Rohe, Le Corbusier) — less-is-more philosophy
- **Japanese minimalism** (Kenya Hara, Muji)
- **Brutalist architecture** as architectural movement (influenced brutalist web)
- **Information design by Isotype and heirs** (Marie Neurath, Otl Aicher)
- **Charles and Ray Eames' film *Powers of Ten*** (1977) — scale as structure
- **Herb Lubalin's *U&lc* magazine**
- **Emigre magazine** (1984-2005) — postmodern type design platform
- **Benetton's controversial advertising** (Oliviero Toscani)
- **Stefan Sagmeister's design work**
- **Paula Scher's environmental typography**

---

## 15. Cross-pollination prompts

When approaching an artifact, ask:

- *What would this look like as a field guide entry?*
- *What would this look like as a Swiss poster?*
- *What would this look like as a map?*
- *What would this look like as an illuminated manuscript page?*
- *What would this look like as a zine?*
- *What would this look like as a Saul Bass title sequence?*

Most answers won't fit. One might. The one that does will be unexpected in a way that reads as craft.

---

## 16. Cross-references

- `references/libraries/composition-library.md` — many of these traditions contributed to composition thinking
- `references/libraries/color-library.md` — palettes from many of these traditions
- `references/libraries/type-library.md` — type traditions from these publishers and designers
- `references/apex-exemplars.md` — digital-era exemplars; this atlas complements those

---

## 17. Extending this atlas

Add entries when they:
- Represent a distinct tradition, period, or voice
- Have non-software provenance
- Suggest transferable moves for digital artifacts

Avoid:
- Digital-native references (those belong in `apex-exemplars.md`)
- Mere hall-of-fame lists without principles to extract
- Personal favorites without broader recognition

The goal: a rich, eclectic gallery that expands imagination. Not completeness.

<!-- END: references/libraries/inspiration-atlas.md -->

---


<!-- BEGIN: references/libraries/medical-artifacts.md -->

# Medical Artifacts Library

A platter for artifacts in medical, clinical, and health-facing domains — patient-facing communication, clinical tools, medical education, epidemiological visualization, anatomical illustration, public health. These domains carry unusual constraints (accuracy, clarity, trust, consequence) and unusual traditions (centuries of anatomical illustration, modern evidence-based medicine, epidemiological rigor).

The material here is meant to expand the creative space for medical artifacts, not narrow it into a default register.

> See `references/how-to-use-this-system.md` for the platter principle.

---

## 1. Core considerations in medical artifacts

Medical artifacts carry weight most artifacts don't:

- **Accuracy matters differently.** A misleading chart in a sales dashboard costs a conversation. A misleading chart in a clinical dashboard costs lives. Hold higher evidentiary standards.
- **Trust is foundational.** Readers often arrive anxious, uncertain, or grieving. The artifact's tone carries more than in other domains.
- **Cognitive load matters more.** Many medical readers (patients, families) are operating in stressful states. Design for the state they will actually be in, not the calm one.
- **Provenance is not optional.** Citations, methodology, limitations, conflicts of interest — all should be visible, not buried.
- **Regulation exists.** HIPAA, FDA guidance, medical-device rules, CE marking. Most artifact-making stays short of these thresholds, but know where the thresholds are.
- **Accessibility is higher-stakes.** Older readers, readers with low vision, readers with cognitive changes, readers with limited literacy — the medical audience skews toward these cases.

---

## 2. Medical artifact genres

### Reading-level targets by genre

Patient-facing medical artifacts have stable reading-level targets in the literature. Hitting them is part of the artifact's quality, not optional. The targets:

| Genre                              | Reading-level target (Flesch-Kincaid / SMOG) | Notes |
|------------------------------------|----------------------------------------------|-------|
| Discharge instructions             | Grade 5–7                                    | Often the floor; many patients are stressed and on medications affecting comprehension |
| Informed consent documents         | Grade 6–8                                    | AMA recommends grade 6; reality is often grade 12+ |
| Vaccine Information Statements (VIS) | Grade 6–8                                    | CDC publishes templates at this level |
| Patient-education leaflets         | Grade 6–8                                    | NHS leaflet standard; Mayo Clinic target |
| Medication labels (consumer)       | Grade 5–7                                    | FDA Drug Facts Label is at this register |
| Hospital website patient pages     | Grade 7–9                                    | Slightly higher; readers are usually pre-arrival |
| Cochrane plain-language summaries  | Grade 8                                      | Their stated target |
| Clinician-facing artifacts         | No target                                    | Jargon expected; tabular density is the constraint |
| Research papers                    | No target                                    | The peer-readership is the calibrator |

Tools to measure: Flesch-Kincaid Grade Level (most widely cited), SMOG (better for medical text — counts polysyllabic words and short sentences differently), Gunning-Fog. All have known limitations and disagree at the margins; treat the score as a *target zone*, not a precise threshold. The substantive test is whether the reader at the stated level can paraphrase the artifact's key claims.

When the artifact declares `medical_mode: true` in the pre-delivery YAML block, `medical.reading_level_target` and `medical.reading_level_measured` are required fields.

### Patient education materials

Artifacts that explain a condition, procedure, treatment, or regimen to a patient.

**Voice considerations:**
- Plain language over jargon. "High blood pressure" before "hypertension."
- Second person ("you") often appropriate — the reader is the subject.
- Honesty about uncertainty — "most people" rather than "always."
- No infantilization. Patients are adults with agency.
- Acknowledge emotional states. Not every explanation should be affect-neutral.

**Structure considerations:**
- **The 3-question answer.** What is it? What does it mean for me? What do I do next?
- **The teach-back loop.** After explaining, surface a "did this make sense?" moment.
- **Action orientation.** End on what the reader should do, concretely.

**Visual considerations:**
- Diagrams over text where possible, but captioned carefully.
- Avoid visual jargon (conventional anatomical positions, Latin terms) without explanation.
- Respect anxiety — avoid gratuitously graphic imagery when a cleaner diagram works.

**Exemplars to calibrate against:**
- NHS patient information leaflets (UK) — considered thoughtful, balanced, accessible
- Mayo Clinic patient-facing materials
- Cochrane plain-language summaries
- JAMA Patient Page

### Clinical decision tools (clinician-facing)

Artifacts used by clinicians at the point of care. Flowcharts, dosage calculators, risk scores, differential-diagnosis aids, treatment algorithms.

**Design considerations:**
- **Speed matters.** Clinicians often have seconds, not minutes. Form should not impose its own cognitive load on top of the clinical decision.
- **Evidence traceable.** Each recommendation links to the underlying study, guideline, or consensus statement. GRADE / CEBM tier shown.
- **Clearly bounded.** Scope of what the tool does and does not cover, prominently. *"This calculator estimates 10-year CVD risk in adults aged 40–79 without prior CVD. It does not apply to patients with diabetes, CKD, or familial hypercholesterolaemia."*
- **Graceful failure.** When inputs are missing or outliers, fail clearly rather than outputting misleading results. *"Total cholesterol > 320: out of validation range; clinical judgment required."*
- **Last-reviewed date visible.** Guidelines age; the artifact must declare its currency.

**Exemplars:**
- MDCalc (mdcalc.com) — clean calculator aesthetic
- NICE guidelines (UK) — structured evidence + recommendations
- UpToDate — encyclopedic clinical reference
- USPSTF preventive-care recommendations
- ACC/AHA risk calculators

### Patient decision aids

A distinct genre from clinician-facing tools. Patient decision aids support a patient (sometimes with their clinician) in making a *preference-sensitive* decision — one where the best choice depends on the patient's values, not on a unique correct answer (e.g., prostate-cancer screening, treatment options for early-stage breast cancer, anticoagulation choices for atrial fibrillation).

**The IPDAS framework (International Patient Decision Aid Standards) defines the quality criteria:**

- **Provides information about options** in sufficient detail for decision-making
- **Presents probabilities of outcomes** in unbiased and understandable ways (absolute risks, natural frequencies, icon arrays; not relative-risk-only)
- **Includes methods for clarifying and expressing patients' values** — values-clarification exercises, weight-the-trade-offs prompts
- **Includes structured guidance in steps of deliberation and communication** — what to discuss with the clinician, how to weigh the options
- **Is based on up-to-date evidence** with the evidence basis disclosed
- **Discloses conflicts of interest** of the developers
- **Uses plain language** appropriate to the patient population (reading-level targets above)
- **Provides a balanced presentation of options** — including the option of doing nothing

**Distinguishing patient decision aids from patient-education materials:** education materials inform; decision aids structure a deliberation. A decision aid presents the options, the trade-offs, and the values-clarification — and explicitly hands the decision to the patient. A pamphlet that says *"talk to your doctor"* is not a decision aid.

**Exemplars:**
- Ottawa Hospital Research Institute patient decision aids inventory (the canonical library)
- Healthwise decision points
- Mayo Clinic Shared Decision Making National Resource Center
- Option Grids (collaborative decision-aid format)

### Informed consent documents

A genre often treated as legal cover and rarely as a designed artifact. The IPDAS criteria for decision aids apply; the legal requirements add a separate layer.

**The four elements informed consent must cover** (in jurisdictions following the Belmont Report / Common Rule tradition):
1. The nature and purpose of the procedure or research
2. The reasonably foreseeable risks
3. The likely benefits
4. Reasonable alternatives, including the alternative of doing nothing

**Common failures:**
- *Consent theater* — see `failure-modes.md` M4. Legalese disguised as choice.
- Reading level above grade 12 when target is grade 6–8.
- Risks listed as comma-separated jargon at the end, in small type (see `failure-modes.md` M5).
- No teach-back — patient signs without a check on understanding.
- Coercive context — form presented in pre-op holding, with patient already gowned and on a stretcher.

**Apex pattern:**
- One page (or two, if the procedure is complex), grade 6–8.
- Four sections corresponding to the four elements, each under 100 words.
- Top three risks, by frequency or severity, in the main flow (not the footer); presented as natural frequencies.
- Teach-back prompt at the end: *"In your own words, what is being done and what could go wrong?"*
- Legal disclosures live in an appendix the patient is told exists; the appendix is signed if the institution requires it, but it is not the consent.
- Last-reviewed date and reviewer credentials on the artifact.

**Exemplars:**
- Macy Foundation conversation aids
- Plain-language consent templates from the Bioethics Research Library, Georgetown
- DECISIONS Project (NIH-funded plain-language consent research)

### Discharge instructions and clinical handoffs

Artifacts that summarise a patient's care plan at the moment of transition — from hospital to home, from one shift to the next, from one institution to another.

**Discharge instructions (patient-facing):**
- Reading level: grade 5–7. Patient may be on opioids, in pain, or fatigued.
- Front page is a single actionable summary: *"You can usually be back at a desk job in 1–3 days. Most people walk without crutches within a week."*
- Tabular *"if X, then Y"* triage logic for warning signs.
- Medication list with USP DI pictograms (when to take, with food, with water, with caution).
- Phone number for "concerns" in a coloured strip at the bottom of every page.
- No infantilization (see `failure-modes.md` M3); no jargon laundering (M7).

**Clinical handoffs (clinician-to-clinician):**
- Tabular structure (SBAR — Situation, Background, Assessment, Recommendation — is one common pattern; I-PASS — Illness severity, Patient summary, Action list, Situation awareness, Synthesis by receiver — is another).
- Active and contingency plans both present (*"if BP < 100, give 500 mL bolus and call me"*).
- Loose ends explicit (*"awaiting cardiology read on the echo"*).
- Receiver reads it back; the verbal handoff is part of the artifact.

**Exemplars:**
- I-PASS handoff curriculum (Boston Children's Hospital)
- Re-Engineered Discharge (RED) Toolkit (AHRQ)
- NHS hospital discharge summary templates

### Medical device user interfaces

UI for clinical devices — infusion pumps, ventilators, monitors, defibrillators, point-of-care diagnostics. Distinct from general clinical software because of regulatory constraints, alarm hierarchies, and use in time-critical scenarios.

**Regulatory baseline:**
- IEC 62366 (usability engineering for medical devices) — the standard the FDA references for human-factors evaluation
- IEC 60601-1-8 (alarm systems for medical electrical equipment) — alarm priority taxonomy, alarm sound conventions, alarm-fatigue mitigations
- FDA Guidance: "Applying Human Factors and Usability Engineering to Medical Devices" (2016)

**Design considerations:**
- **Alarm hierarchy: low / medium / high priority,** with distinct visual and auditory signatures. High-priority alarm must be unambiguous and silenceable only with deliberate action (not a single tap).
- **Alarm fatigue is the dominant failure mode.** Most alarms in clinical settings are false-positive; staff habituate; the true alarm is missed. The design discipline is *reducing* alarms, not adding them.
- **Single-purpose UI.** Unlike consumer software, clinical devices should *not* multitask. The infusion pump shows the infusion, full stop.
- **Read at distance.** A monitor at a bedside is read across 2–3 metres; the primary numbers must be legible at that distance.
- **Glove-friendly inputs.** Touch targets sized for gloved hands; haptic confirmation; no precise gestures.
- **Resilience under failure.** Network loss, sensor disconnect, power loss — the device must fail to a safe, known state.

**Exemplars:**
- Apple's UI guidance for clinical software on iPad / iPhone (Health and ResearchKit guidelines)
- IDEO / Smiths Medical infusion-pump redesign case study
- The OpenAPS / Loop diabetes-management community's interface conventions

### Public-health campaign materials and Vaccine Information Statements

Multi-surface artifacts deployed across posters, leaflets, social media, websites, and broadcast. One message, four surfaces.

**Genres:**
- **Vaccine Information Statements (VIS)** — CDC-mandated for each vaccine administered; standardised template; reading level grade 6–8; covers the disease, the vaccine, who should and should not receive it, side effects, what to do if a reaction occurs.
- **Public-health posters** — single-message, action-oriented, read at distance, behaviour-change voice. NHS "Be Clear on Cancer" campaign as the contemporary exemplar.
- **Social-media cards** — adapted from posters; reframed for thumb-scroll context; carry the action prompt.
- **Microsites and leaflets** — extended treatment; FAQ structure; tabular evidence presentation.

**Design considerations:**
- **Behaviour-change voice.** Imperative, specific, time-bound. *"If you've had a cough for three weeks, see your GP this week."* — not *"It is important to be aware of persistent symptoms."*
- **Institutional-trust colour signalling.** NHS blue, CDC navy, WHO blue — established trust signals; novel branding for a public-health message reads as commercial.
- **One action per artifact.** Multiple recommendations dilute compliance.
- **Cultural and linguistic adaptation.** Translation alone is insufficient; conventions, imagery, and metaphors must adapt.

**Exemplars:**
- NHS "Be Clear on Cancer"
- CDC COVID-era materials (with retrospective critique of consistency failures)
- WHO smoking-cessation campaigns
- Truth Initiative anti-smoking work
- "Drink Aware" UK alcohol-awareness campaign

### Biotech investor / FDA briefing materials

A genre at the intersection of medical and financial communication. Briefing books for FDA advisory committee meetings; investor decks for biotech companies presenting clinical results; analyst reports on trial readouts.

**Design considerations:**
- **The dual audience.** Investors and regulators may both read the same materials but bring different questions. The artifact must serve both without distortion.
- **Honest about endpoints.** Primary, secondary, exploratory endpoints clearly labelled. Statistical hierarchy preserved (no claiming a positive exploratory endpoint as if it were primary).
- **Forest plots and Kaplan-Meier curves with full at-risk tables.** The reader is sophisticated; the figures must withstand scrutiny.
- **CONSORT diagram included** for the trial.
- **Comparable historical context** where relevant — "competitor X showed Y in trial Z" — but acknowledged as cross-trial, not head-to-head.
- **Conflicts of interest disclosed prominently.**

**Failure modes specific to this genre:**
- Cherry-picked subgroup analyses presented as the headline.
- Per-protocol analysis foregrounded over intention-to-treat.
- Relative effect sizes without absolute (`failure-modes.md` M2).
- Confidence-inflation language (*"highly statistically significant"* for p = 0.04).
- "Trends toward" language for results that did not reach significance.

**Exemplars:**
- FDA Advisory Committee briefing documents (publicly available; variable quality)
- Genentech historical investor briefings
- New England Journal of Medicine's editorials on landmark approvals

### Epidemiological visualization

Data visualization for public-health contexts. COVID dashboards, vaccine-coverage maps, outbreak tracking, disease-burden comparisons.

**Principles:**
- **Truncated y-axes are a hazard.** In a clinical context, misleading a reader about scale can change behavior.
- **Rates over counts.** Normalize by population when comparing.
- **Uncertainty visible.** Confidence intervals, data lag, reporting completeness.
- **Actionable metadata.** Source, date of data, methodology, caveats.

**Exemplars:**
- John Snow's 1854 cholera map — foundational
- Our World in Data — reference standard for contemporary epi visualization
- John Burn-Murdoch's Financial Times charts (COVID era)
- CDC's surveillance reports (structured; dense; rigorous)
- Hans Rosling / Gapminder presentations

### Research papers and clinical publications

Journal-format scientific writing.

**Conventions:**
- IMRAD structure (Introduction, Methods, Results, Discussion) is standard
- CONSORT (clinical trials), STROBE (observational), PRISMA (systematic reviews), SPIRIT (protocols) — reporting frameworks for different study types
- Tables and figures numbered and captioned; source data available
- Conflict-of-interest disclosure
- Registered protocols and pre-registration increasingly expected
- Effect sizes, not just p-values. Clinical significance ≠ statistical significance

**Exemplars:**
- NEJM, JAMA, The Lancet, BMJ — varying house styles
- BMJ's infographics for studies — narrative summaries of published research

### Anatomical and medical illustration

Depicting human (or animal) anatomy for education or reference.

**Traditions:**

- **Andreas Vesalius — *De humani corporis fabrica* (1543)** — foundational anatomical atlas; shifted medicine from Galenic tradition to observation
- **Henry Gray & Henry Vandyke Carter — *Gray's Anatomy* (1858)** — the reference English-language atlas, still revised
- **Frank Netter — *Atlas of Human Anatomy* (1953)** — Netter's illustrations defined 20th-century medical education
- **Max Brödel** — pioneered the integration of anatomical illustration and medical education; Johns Hopkins department of art as applied to medicine (founded 1911)
- **Dorling Kindersley's anatomy atlases** — accessible, consumer-facing
- **Hokusai's anatomical sketches** — Japanese medical illustration
- **Leonardo da Vinci's anatomical drawings** — Renaissance; observational rigor

**Visual conventions:**
- Standard anatomical position (body facing viewer, arms at sides, palms forward)
- Specific planes (sagittal, coronal, transverse/axial)
- Directional terminology (superior/inferior, anterior/posterior, medial/lateral, proximal/distal)
- Layered illustration (skin removed to show muscle; muscle removed to show bone; etc.)
- Color conventions (red for arteries, blue for veins, yellow for nerves, green for lymphatics) — though these are conventions, not universal rules

### Medical imaging display

Radiology (X-ray, CT, MRI, ultrasound), pathology, endoscopy.

**Conventions for display:**
- Contrast and window-level (grayscale range mapped to Hounsfield units in CT)
- Orientation markers (L/R indicators; patient-anatomy orientation)
- Overlays (regions of interest, measurements, annotations)
- Comparison layouts (side-by-side for before/after or normal/abnormal)

**Considerations:**
- Never strip DICOM metadata when sharing for educational purposes — but scrub PHI
- Medical-grade monitors have calibrated grayscale; consumer monitors don't (may introduce artifacts in display)

### Pharmacology / drug information

Drug information sheets, prescribing references, interaction checkers.

**Genres:**
- Package inserts (FDA-regulated format; highly structured)
- BNF (British National Formulary) — clinical drug reference
- Micromedex, Lexicomp — commercial references
- MedlinePlus — patient-facing
- Clinical pharmacy apps (Epocrates, Sanford Guide)

**Key content elements:**
- Indication, dose, route, frequency
- Contraindications and cautions
- Drug-drug interactions
- Adverse effects by frequency
- Pregnancy/lactation categories
- Monitoring requirements

### Genetic and genomic

Pedigrees, karyotype displays, sequence alignment, variant visualization, GWAS results.

**Conventions:**
- **Pedigree symbols** — circle (female), square (male), diamond (unknown); filled = affected; lines for generations; / for deceased. Highly standardized.
- **Karyotype** — chromosomes arranged by size and banding pattern
- **Sequence alignment** — monospace font; conserved residues highlighted
- **Manhattan plot** — GWAS results with chromosomal position (x) and -log10(p-value) (y)

### Clinical informatics dashboards

Patient lists, census dashboards, quality-metric tracking, length-of-stay analyses.

**Considerations:**
- **Patient-level data** has different rules than aggregate data (PHI)
- Real-time vs. batched updates
- Alerting thresholds (avoid alert fatigue)
- Tie to action — dashboards for clinical use must connect to what to do next

---

## 3. Medical color registers (one palette family among many)

Medical artifacts often use restrained, neutral palettes — but the specific register varies by audience and context.

- **Institutional clinical** — deep blues, clinical whites, restrained teals. Mayo Clinic, Kaiser Permanente visual traditions.
- **Research-grade** — low-chroma neutrals, saturated accent only for data-series distinction. Nature, NEJM register.
- **Patient-facing consumer health** — warmer neutrals, greens and blues, more accessible. Healthline, WebMD register.
- **Biomedical scientific illustration** — Sepia-toned anatomical illustration (Gray's tradition); full-color realistic (Netter tradition); minimal line (educational diagram tradition).
- **Epidemiology emergency** — reserved reds for outbreak / severity; ordinal palettes for risk strata.
- **Pharmaceutical** — corporate, often trust-signaling blues; strict regulatory constraints on branding.

See `references/libraries/color-library.md` for the broader space.

---

## 4. Typography in medical artifacts

- **Highly readable body text.** Many readers have reduced vision. Minimum 16px body; 18px or 20px for patient materials.
- **Restrained display.** Medical artifacts are rarely the place for theatrical typography. Editorial or humanist sans generally appropriate.
- **Numerals matter.** Dosages, rates, percentages — use tabular figures. Align decimals.
- **Scientific notation** — variable-font support or proper math rendering for statistical expressions.
- **Units** — always. "0.5" is dangerous; "0.5 mg/kg" is safer; "0.5 mg/kg IV every 8h" is right.

---

## 5. Honest communication of uncertainty and risk

Medical artifacts often fail because risk is communicated poorly. Approaches:

- **Absolute risk, not just relative.** "Relative risk reduction of 50%" can mean 1 in 100 → 1 in 200 (small absolute change) or 50% → 25% (large). Always present both.
- **Natural frequencies over percentages.** "7 of 100 people" is understood more reliably than "7%."
- **Icon arrays / waffle charts.** 100-square grids with shaded squares representing affected. Isotype-tradition approach that works well for risk.
- **Time horizons explicit.** "5-year survival" ≠ "lifetime risk."
- **Visualization of uncertainty.** Shaded confidence bands; distributional views; scenarios.
- **Numeracy adaptation.** Low-numeracy readers benefit from frequencies and icons; high-numeracy readers can engage with probabilities and intervals.

### Seven risk-communication formats — when each succeeds and misleads

The same underlying risk can be communicated in many formats. Each has documented strengths and failure modes. The table below summarises the most-used seven; apex artifacts often present *two* formats side by side to triangulate reader understanding.

| Format                       | Example (treatment cuts heart-attack risk from 2% to 1% over 5 years) | Succeeds when                                                              | Misleads when                                                                 |
|------------------------------|-----------------------------------------------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| **1-in-X format**            | *"Without treatment, 1 in 50; with, 1 in 100."*                       | Reader is low-numeracy; the absolute frequency is small                    | The "X" values are large and hard to compare (1 in 137 vs. 1 in 142)          |
| **Natural frequency (out of 1,000 / 10,000)** | *"Of 1,000 people, 20 have a heart attack without; 10 with."* | Reader is low-numeracy; both arms shown on the same denominator            | Denominators differ between arms or between sources (cognitive load increases)|
| **Icon array / waffle chart**| 100-cell grid; 2 cells shaded vs. 1 cell shaded                       | The absolute risk is < 10%; the reader benefits from a visual              | The risk is < 1% (grids of 1,000 are unwieldy); the reader has low visual literacy |
| **Percent (absolute)**       | *"Risk drops from 2% to 1%."*                                         | Reader is numerate; precision matters                                      | Reader confuses absolute and relative; percent of small base looks negligible |
| **Number Needed to Treat (NNT)** | *"Treat 100 people for 5 years to prevent 1 heart attack."*        | Reader is a clinician; the decision is at the population level             | Reader is a patient (NNT is counterintuitive); time horizon implicit          |
| **Relative risk reduction (RR)** | *"Treatment cuts risk by 50%."*                                  | Almost never appropriate alone                                             | Used without absolute risk — the dominant failure mode (`failure-modes.md` M2)|
| **Absolute risk reduction (ARR)** | *"Treatment cuts risk by 1 percentage point."*                  | Reader is numerate; the comparison is with another ARR                     | Reader confuses with relative; the percentage-point distinction is invisible  |

**Apex pattern:** present *natural frequency + icon array + absolute risk* together. Three formats triangulating one risk. The Harding Center fact-boxes are the canonical implementation; Gigerenzer's body of work is the calibrating literature.

**Never:** present relative risk alone. *"Cuts your risk in half"* without the absolute baseline is the single most-documented misleading risk communication in the medical literature.

---

## 6. Ethical considerations

- **Informed consent model for visualization.** The reader of a medical artifact should leave with accurate understanding, not with persuasion toward a specific choice.
- **Conflicts of interest.** Pharma funding, device-maker influence, author COI — disclose.
- **Patient privacy.** PHI scrubbed. De-identified cases preferred. If using a patient image, consent.
- **Avoid stigma.** Mental-health, addiction, obesity, infectious-disease topics have long histories of stigmatizing representation. Specific language (person-first, identity-first — varies by community and condition) matters.
- **Cultural sensitivity.** What's clinically standard in one setting can be culturally inappropriate in another.

---

## 7. Medical literature references

Foundational work to reason from:

- **Cochrane Collaboration** — evidence synthesis; plain-language summaries
- **Cochrane Handbook for Systematic Reviews**
- **The BMJ's "Data" section** and its data-journalism work
- **STAT News** — contemporary medical journalism
- **Kaiser Health News / KFF Health News**
- **"How to Lie with Statistics" / "How Charts Lie"** (Cairo) — specifically relevant for medical visualization
- **Richard Doll's smoking/lung-cancer chart** — a canonical example of observational evidence visualized
- **Framingham Heart Study visualizations** — long-duration epidemiology
- **Gerd Gigerenzer's work on risk communication** — *Reckoning with Risk*; *Calculated Risks*

---

## 10. Regulatory and provenance vocabulary

Medical artifacts often need to declare the evidence basis, regulatory status, and provenance of their claims. The vocabulary below is the set of conventions to recognise and use correctly.

### Evidence tiers

- **GRADE** (Grading of Recommendations, Assessment, Development and Evaluation) — the dominant framework. Four tiers of certainty: *high*, *moderate*, *low*, *very low*. Strength of recommendation separately rated: *strong* or *conditional*. Cochrane and the WHO use GRADE.
- **CEBM Levels of Evidence** (Oxford Centre for Evidence-Based Medicine) — 5 levels, 1 (systematic reviews of RCTs) to 5 (expert opinion); pre-dates GRADE and still used in surgical and procedural specialties.
- **USPSTF grades** — A/B/C/D/I (Insufficient evidence). Used in US preventive care.
- **NICE evidence ratings** — UK; aligned with GRADE.

When the artifact declares `medical_mode: true`, `medical.evidence_basis` field should state the framework and the rating: *"GRADE: moderate"*, *"USPSTF: B"*, *"CEBM: 2a"*, or *"expert opinion"*.

### Last-reviewed dates

Medical artifacts age. A patient page from 2017 advising on COVID screening is wrong. Every medical artifact should display:
- **Last reviewed** — date of the most recent substantive review
- **Reviewer** — name and credential, or *"self-attested"* if the author is the reviewer
- **Next review due** — optional but recommended; usually 12–36 months from review

The dates appear in the artifact, not just in metadata. Patient leaflets typically place them in the footer; clinical tools in the metadata strip.

### Conflicts of interest

Disclosure conventions:
- **Financial** — direct payments, consulting, equity, grants from entities with a stake in the recommendation
- **Non-financial** — institutional affiliations, advocacy positions, prior public statements
- **None** — state explicitly; absence is not disclosure

ICMJE (International Committee of Medical Journal Editors) provides a standard disclosure form widely adopted. The artifact's reader should not have to hunt for COI; it appears at the top or in a clearly-labelled section.

### Regulatory marks and approval routes

- **FDA** (US Food and Drug Administration) — *FDA-approved*, *FDA-cleared* (different pathways; cleared is a lower bar, usually 510(k) substantial-equivalence), *Investigational* (in trials, not approved). *Boxed warning* (the "black box") for the most severe risks.
- **EMA** (European Medicines Agency) — *Centralised authorisation* (EU-wide), *National authorisation* (country-by-country)
- **MHRA** (UK Medicines and Healthcare products Regulatory Agency) — post-Brexit UK authorisation; *Yellow Card* scheme for adverse event reporting
- **CE marking** — required for medical devices in the European Economic Area; class I (low risk) through class III (high risk)
- **TGA** (Australia), **PMDA** (Japan), **Health Canada** — other major regulators with similar tier structures

### Clinical coding systems

When the artifact references conditions, procedures, drugs, or test results, the coding system matters:

- **ICD-10 / ICD-11** (International Classification of Diseases) — diagnoses; alphanumeric codes (J45.901 = "Unspecified asthma with status asthmaticus"). The standard for billing and epidemiology.
- **SNOMED CT** — clinical terminology, broader than ICD; concept-based; the standard for EHR documentation.
- **LOINC** (Logical Observation Identifiers Names and Codes) — laboratory and clinical observations; six-part code naming the analyte, property, time, system, scale, method.
- **RxNorm** — normalised drug naming for US clinical systems; links brand and generic names.
- **CPT** (Current Procedural Terminology) — US procedural billing codes; AMA-maintained.

Artifacts that link claims to coded data should cite the coding system used; *"asthma (ICD-10: J45)"* is more precise than *"asthma"* and is machine-readable.

### Pregnancy and lactation labeling

- **PLLR** (Pregnancy and Lactation Labeling Rule, FDA 2015) — replaced the old A/B/C/D/X letter categories with narrative summaries. The new format requires three sections: Pregnancy, Lactation, Females and Males of Reproductive Potential — each with a risk summary, clinical considerations, and data sections.
- The old letter categories (A/B/C/D/X) are still in older literature and some non-US contexts; recognise them but prefer PLLR-style narrative for new artifacts.

---

## 11. Drug-name and units discipline

Medication errors are a leading cause of preventable harm. The conventions below are *learned*, not intuitive, and apex medical artifacts honour them without exception.

### Tall-man lettering (ISMP)

The Institute for Safe Medication Practices maintains a list of look-alike drug names where mixed-case lettering should be used to make the distinction visible:

- **hydrALAzine** vs. **hydrOXYzine** (vasodilator vs. antihistamine — opposite indications)
- **predniSONE** vs. **prednisoLONE** (different potencies)
- **DOPamine** vs. **DOBUTamine** (different cardiovascular effects)
- **vinBLAStine** vs. **vinCRIStine** (chemotherapy; lethal if confused)
- **glipiZIDE** vs. **glyBURIDE** (sulfonylureas, different durations)
- **chlorproPAMIDE** vs. **chlorproMAZINE** (anti-diabetic vs. anti-psychotic)

When two such drugs appear in the same artifact, use tall-man lettering for both. The full ISMP list is at ismp.org/recommendations/confused-drug-names-list.

### Decimal and zero conventions

- **Leading zero before a decimal less than 1.** Always write *0.5 mg*, never *.5 mg*. A missed decimal point reads as 5 — a tenfold overdose.
- **No trailing zero after a whole number.** Write *5 mg*, never *5.0 mg*. The trailing zero, if the decimal point is missed, reads as 50 — also a tenfold overdose.
- **The decimal point itself is dangerous.** When possible, write doses in units that avoid decimals altogether (*500 mcg* rather than *0.5 mg*).

### Unit abbreviations

The ISMP error-prone abbreviation list identifies abbreviations that should be spelled out:

- **µg → mcg.** The Greek mu can be misread as *m* (giving *mg*, a thousandfold overdose). Write *mcg* always.
- **U → units.** *10U* of insulin has been misread as *100*. Write *10 units*.
- **IU → international units.** Same risk as *U*.
- **QD / QOD → daily / every other day.** The Latin abbreviations have been misread. Write the English.
- **HS → at bedtime.** *HS* has been misread as *half-strength*.
- **D/C → discharge / discontinue.** Ambiguous; spell out which.
- **cc → mL.** *cc* can be misread as *0*. Use *mL* always.
- **/ (slash) between drug names.** *Heparin/insulin* can be misread as *heparin one insulin* (heparin 1 insulin unit). Use the word *and* or list separately.

### Unit families and conversions

- **mEq, mmol, mg.** Different units measure different things and are not interchangeable. Potassium is dosed in mEq or mmol (charge / amount); the mg dose depends on the salt (potassium chloride vs. potassium phosphate vs. potassium citrate). Calcium: 1 g calcium gluconate = 4.65 mEq calcium; 1 g calcium chloride = 13.6 mEq calcium. The conversion is part of the prescription.
- **SI vs. conventional units in labs.** Glucose: 100 mg/dL (US conventional) = 5.6 mmol/L (SI). Creatinine: 1 mg/dL = 88 µmol/L. The conversion is field-specific and locale-specific.
- **Body-weight dosing.** *mg/kg* — the *kg* matters. State the patient's weight; state the calculated dose; do not let the multiplication be implicit.
- **Body-surface-area dosing.** *mg/m²* — common in oncology. State the BSA calculation method (Du Bois, Mosteller); the methods give slightly different results.

### Pharmaceutical pictograms

For low-literacy patient artifacts:
- **USP DI medication pictograms** (ISO 9186) — *"take with food"*, *"do not crush"*, *"avoid alcohol"*, *"store in refrigerator"*; standardised, widely-licensed
- **Hesperian Foundation low-literacy illustrations** — broader patient-education iconography
- **Vanderbilt pictographic prescription labels** — research-validated US-specific pictograms
- **FIP (International Pharmaceutical Federation)** — globally-developed pictogram set; available open-access

See `references/libraries/iconography-library.md` §3 for the iconography tradition; medical-mode artifacts should treat the choice of pictogram set as a design decision, not a default.

---

## 12. Inpatient note types

The resident's daily artifact catalogue. Each note type is a distinct genre with its own audience, length convention, legal status, and failure modes. Conflating them is the single most-common documentation failure on the wards.

- **Admission History & Physical (H&P).** ~1,200–1,800 words. Sections, in canonical order: Chief Complaint (CC, the patient's own words in quotes); History of Present Illness (HPI, narrative paragraph organised by OPQRST or the patient's own chronology); Review of Systems (ROS, by organ-system with pertinent positives and negatives); Past Medical History (PMH); Past Surgical History (PSH); Medications (with dose, route, frequency, indication); Allergies (with reaction, not just *NKDA*); Social History (substance use quantified — pack-years, AUDIT-C, last use); Family History (with age and cause of death for first-degree relatives); Physical Exam (vitals + by-system); Labs and Studies (with date and trend); Assessment and Plan (A&P, organised *by problem* in Weed POMR tradition — never by organ system on admission). The H&P is the legal record of the admission decision; ambiguity here surfaces months later in audit.

- **Daily progress note (SOAP).** 200–400 words *per active problem*. Subjective (overnight events, patient report); Objective (vitals trend, exam, new data); Assessment (one-line problem representation per problem); Plan (numbered actions). Weed's Problem-Oriented Medical Record (1968) is the source; CMS billing now requires problem-based organisation. Audit-grade legal record — the chart is read in malpractice review.

- **Event note.** Acute change-in-status documentation written contemporaneously with the event. Timestamped to the minute. Structure: time, event, assessment, action, response, family notification, attending notification. Distinct from a progress note because the audience includes future M&M review.

- **Procedure note.** Indication; informed consent obtained (with capacity assessment); pre-procedure time-out (universal protocol); site marking; sterile prep; technique (one paragraph); estimated blood loss (EBL); specimens sent; complications (or *"none"*); post-procedure plan. CMS requires every bedside procedure to have a note matching the procedure billing code.

- **Off-service note.** Written when transferring care to an oncoming team (e.g., rotation change, post-call sign-off of a long-stay patient). Summarises admission course, active problems, anticipated trajectory, contingencies. Bridges the H&P-to-discharge-summary gap.

- **Discharge summary.** Audit-grade. Required elements: admission/discharge dates; principal diagnosis and ICD-10 code; secondary diagnoses; procedures with CPT codes; hospital course (one paragraph per problem); discharge medications with reconciliation (started / continued / changed / stopped, each with reason); follow-up appointments with date/time/provider; pending studies the outpatient team must chase; condition at discharge; patient education provided. Medication reconciliation discipline is the dominant safety issue (Joint Commission NPSG.03.06.01).

**Exemplars.** UCSF Hospitalist Handbook; Pocket Medicine (Sabatine, "the Pocket Book") for the implicit conventions; Weed's *Medical Records, Medical Education, and Patient Care* (1969) for POMR origins; AMA E&M billing documentation guidelines for the audit-facing structure.

**Failure modes specific.** *Copy-forward decay* — yesterday's note pasted into today's with one number changed; the EHR's gift to malpractice plaintiffs. *Organ-system A&P on an admission* — disguises the diagnostic reasoning. *Bare-bones "stable, continue"* progress notes that fail audit. *Discharge summary written from memory three days later* — pending studies forgotten.

**Cross-references.** Distinct from the teaching-case form in `references/medium-playbooks/clinical-case.md` (which optimises for pedagogy, not legal record). For the bedside-handoff complement see §15.

---

## 13. Rounds-presentation conventions

The verbal artifact of inpatient medicine. Four distinct sub-forms, each with its own audience expectation. Misreading the form is how residents lose attendings' trust on day one.

- **The 30-second one-liner (problem representation).** Bowen's *NEJM* 2006 framework: *age + relevant PMH + acuity + presenting syndrome + key supporting data*. Example: *"56-year-old man with HTN, hyperlipidaemia, and 40-pack-year smoking history presenting with two hours of substernal chest pain radiating to the left jaw, with inferior ST elevation on ECG."* The one-liner is the unit of cognition that gets passed across services, into consults, and into the consultant's response. Apex one-liners commit to a syndrome, not a symptom — *"acute coronary syndrome"* beats *"chest pain"* when the data supports it.

- **The new-admit presentation.** 5–7 minutes. Full HPI as narrative; ROS by system (pertinent positives and negatives only); full PMH/SH/FH; physical exam (vitals + abnormalities + pertinent normals); labs and imaging (with comparison); Assessment-and-Plan *by problem*, with one-line problem representation per problem followed by differential, then plan. The senior expects you to commit to a leading diagnosis with the differential ranked, not to recite a list.

- **The daily-update presentation.** 60–90 seconds per patient. Interval since yesterday (events, new data); today's exam (focused); today's plan (numbered, by problem). The senior is tracking trajectory, not re-learning the patient. Lead with the *delta*, not the static history.

- **The rounding card.** The resident's personal pre-rounds artifact. Typically a folded letter-page with one patient per row: name, room, day-of-admission, one-line problem rep, vitals-overnight (with arrows or sparklines for trend), today's labs, planned interventions, scheduled studies, dispo. Format is personal but conventions are shared (Pocket Medicine ships with the canonical template). Apex rounding cards use sparklines for vital-sign trends — small inline trajectory replaces a column of numbers.

**Exemplars.** Bowen, *Educational Strategies to Promote Clinical Diagnostic Reasoning* (NEJM 2006) for the problem-representation framework. Stanford 25 (Abraham Verghese) for bedside-exam culture. Aquifer rounds-presentation rubric for the assessed form. Pocket Medicine (Sabatine) for the rounding-card convention.

**Failure modes specific.** *"Buried the lede"* — the syndrome arrives in minute four. *Symptom-as-diagnosis* — *"chest pain"* in the one-liner instead of *"ACS"*. *Reading the chart* — the presentation is a recital, not a synthesis. *No differential* — the assessment is a single diagnosis with no contenders considered. Cross-reference `references/medium-playbooks/clinical-case.md` for the written counterpart.

---

## 14. Consult notes (Goldman's 10 commandments)

The cross-service consultation note is its own genre, with etiquette distinct from the H&P. Lee Goldman's *Ten Commandments for Effective Consultations* (Arch Intern Med 1983; updated Salerno *Arch Intern Med* 2007) is the canonical reference; every internal-medicine residency teaches it explicitly. The commandments, abbreviated: (1) determine the question being asked; (2) establish urgency; (3) look for yourself (don't rely on the chart); (4) be as brief as appropriate; (5) be specific and concise (numbered recommendations); (6) provide contingency plans; (7) honour thy turf (don't take over the primary team's role); (8) teach with tact; (9) talk is cheap — and effective (verbal communication, not just chart); (10) follow up.

**Canonical structure.**
- *Reason for consult* — one sentence stating the question. *"Evaluate left-leg swelling in a post-op day-2 hip-arthroplasty patient with rising D-dimer."* The consult question is not *"please see and evaluate"* — that's a non-question and a documented dissatisfier on both sides.
- *Brief HPI* — three to five sentences. The primary team's H&P is in the chart; do not re-narrate.
- *Pertinent exam and data* — focused; *"the rest of the chart is unchanged"* is acceptable.
- *Impression* — committed; differential with leading diagnosis named.
- *Recommendations* — numbered, specific, actionable, with thresholds (*"if WBC > 15, repeat CT abdomen"*). Vague *"continue current management"* is a failure mode.
- *Contact* — pager, cell, attending name; availability for follow-up.

**Distinct from the H&P.** Different audience (a peer service, not the admitting team), different intent (answer a specific question, not document the admission), different length (one screen, not three pages). Signal-to-noise is the discipline; the consultant's reputation is built on saying useful things efficiently.

**Exemplars.** Goldman, *Arch Intern Med* 1983; Salerno *et al.* 2007 update; the *Annals of Internal Medicine In the Clinic* consult-note framework; Cleveland Clinic's published consult templates.

**Failure modes specific.** *Restating the chart* — re-narrating what the primary team already documented. *The non-recommendation* — *"continue current management; will follow"* without specifics. *The unbounded list* — twelve recommendations of equal weight, none prioritised. *No verbal handoff* — chart consult only, leaving the primary team to discover it on rounds. Cross-references §15 (handoffs) and §12 (H&P), each a distinct genre.

---

## 15. Sign-out, cross-cover, and handoff artifacts

The handoff is the most-studied artifact in patient safety. Joint Commission analyses attribute >60% of sentinel events to communication failures, the majority of which occur at handoffs. ACGME Common Program Requirement VI.E.3 requires every residency to have a structured handoff curriculum. The artifact is verbal, written, *and* read-back; all three components are required.

- **I-PASS (Starmer *et al.*, NEJM 2014).** The canonical structured handoff. *Illness severity* (stable / watcher / unstable) — a three-tier triage that lets the receiver prioritise. *Patient summary* — one-line problem representation plus brief course. *Action list* — numbered, time-anchored, owner-assigned tasks for the cross-cover shift. *Situation awareness with contingency planning* — *"if-then"* statements for anticipated trouble (*"if SBP < 90, give 500 mL bolus and call me; do not start vasopressors without discussion"*). *Synthesis by receiver* — read-back, not optional. The Starmer multicentre trial showed a 23% reduction in medical errors after I-PASS implementation; this is one of the largest documented effect sizes in patient-safety literature.

- **SBAR (Haig *et al.*, Jt Comm J Qual Patient Saf 2006).** For telephone consults and escalations. *Situation* (who you are, who the patient is, what is happening); *Background* (relevant context in one or two sentences); *Assessment* (your read); *Recommendation* (what you want from the listener). Originated in US Navy nuclear-submarine communication; adapted by Kaiser Permanente; now standard for nurse-to-physician communication.

- **The printed sign-out card.** One row per patient: room / name / age / one-line problem rep / code status / allergies (concise) / overnight to-dos / if-then contingencies / dispo. Conventions: code status (*Full Code* / *DNR-CC / DNR-CCA*) in a visually distinct cell; if-then contingencies in a column distinct from to-dos; the receiver writes time-of-event in the margin.

- **Read-back as part of the artifact.** The handoff is not complete when the speaker stops talking; it is complete when the receiver paraphrases back. The artifact's design must afford this — leave space, prompt for it explicitly, do not move on without it.

**Exemplars.** Starmer *et al.*, *Changes in Medical Errors after Implementation of a Handoff Program* (NEJM 2014); I-PASS Handoff Curriculum (Boston Children's Hospital); Haig *et al.* 2006; AHRQ TeamSTEPPS handoff modules.

**Failure modes specific.** *Verbal-only handoff* with no written backup — the receiver forgets the third patient by the fifth. *Written-only* — no read-back, no shared understanding. *Stable/unstable miscalibration* — labelling a watcher as stable, then being surprised at 3 a.m. *No contingencies* — only tasks, no anticipation. *Sign-out drift* — yesterday's sign-out copy-forwarded with the same to-dos still pending.

**Cross-references.** `references/medium-playbooks/cross-cluster/operating-manual.md` for the if-then-contingency discipline (handoffs are operating manuals for a single shift). §16 below for the time-critical retrospective documentation that handoff-failures feed into.

---

## 16. Code blue and Rapid Response Team documentation

Time-critical retrospective documentation. The code or RRT event is reconstructed minutes-to-hours later, usually for both clinical and medico-legal purposes, and the reconstruction quality depends entirely on what the recorder captured during the event itself.

**The code-blue runsheet.** Three columns minimum: *time* (to the second when possible, minute when not), *intervention* (drug + dose + route, or procedure, or rhythm note), *outcome / response* (rhythm change, ROSC, pulse return). The AHA ACLS megacode form is the canonical template — a pre-printed grid with rows for each minute of the code, columns for rhythm-check / drug / shock / CPR-quality (rate, depth, recoil, interruption). The form's design discipline: each line is a single fact, timestamped; no narrative until the post-event summary.

**The post-arrest checklist.** Triggered at ROSC (return of spontaneous circulation). Confirms airway (endotracheal tube position and capnography), breathing (ventilator settings and oxygen titration toward SpO₂ 92–98%, not 100%), circulation (post-ROSC blood pressure target MAP ≥ 65; vasopressor titration), neuro (pupils, GCS, decision on targeted temperature management 32–36°C per AHA 2020). 12-lead ECG within ten minutes (looking for STEMI as the precipitant). Cause identification using the Hs and Ts (Hypoxia, Hypovolaemia, H⁺ acidosis, Hypo/Hyperkalaemia, Hypothermia; Tension pneumothorax, Tamponade, Toxins, Thrombosis pulmonary, Thrombosis coronary). The checklist is its own designed artifact — a single-side card that lives on the code cart.

**The code summary printout.** Generated from the monitor / defibrillator after the event: ECG strips at each rhythm change, shock-delivery timestamps with energy, CPR-quality metrics (compression rate, depth, fraction of code spent compressing — the target is >80%). The printout is the objective ground truth against which the recorder's runsheet is reconciled.

**The family-notification timestamp.** Often missed. Required for medico-legal record: time family was reached, by whom, by what route, what was conveyed. Family-witnessed resuscitation (Critchell & Marik 2007) is a separate decision documented at the same point.

**The post-event debrief.** Hot debrief (within minutes; what worked / what didn't / one thing to change) is distinct from cold debrief (within 1–2 weeks; structured M&M-style review). Cheng *et al.* (Resuscitation 2014) systematic-review evidence: debriefing improves performance on next code. The artifact is a half-page structured prompt, not free narrative.

**Exemplars.** AHA ACLS Provider Manual megacode form; IHI Post-Arrest Debrief tool; Resuscitation Academy (Seattle) post-event review template; Pittsburgh post-cardiac-arrest care guidelines.

**Failure modes specific.** *Narrative-first recording* — the recorder writes prose during the code instead of grid entries, and the timeline collapses. *No timestamps on family notification.* *Drug names without doses* — *"gave epi"* without *"1 mg IV, third dose at 14:07"*. *Missing CPR-quality data* — the team thinks they were compressing well; the monitor printout disagrees. Cross-references §17 (these events feed M&M).

---

## 17. Morbidity and Mortality (M&M) artifacts

M&M is the oldest non-punitive systems-analysis register in medicine. Codman's *End Result System* (1914) is the historical root; the modern ACGME-mandated M&M conference is its institutional descendant. The artifact's purpose is system learning, not blame; the voice discipline this requires is the genre's defining feature.

**Canonical structure.**
1. *Chronology.* A UTC-or-local-time timeline at second-to-minute precision, reconstructed from chart, monitor printouts, and witness recollection. No interpretation in the chronology — events only.
2. *Decision points.* Specific moments where a different decision was available. Each named, each with the options that existed at that point and the option chosen.
3. *Contributing factors (Reason's Swiss-cheese model).* Active failures (the proximal slips, lapses, mistakes) *and* latent conditions (the system holes — staffing, equipment, protocol gaps, EHR misconfiguration — that lined up to let the active failure reach the patient). James Reason's *Human Error* (1990) is the framework.
4. *Cognitive errors (Croskerry's taxonomy).* Premature closure, anchoring, availability bias, base-rate neglect, search satisficing, confirmation bias, framing effect — each a named cognitive error with documented signature in diagnostic reasoning (Croskerry, *Acad Med* 2003).
5. *Counterfactual analysis.* Would a reasonable clinician with the information available at the time have made the same decision? Hindsight bias (Fischhoff 1975) is the disciplined enemy here.
6. *Corrective actions.* Just Culture algorithm (Marx 2001): was this a human error, at-risk behaviour, or reckless behaviour? Each calls for a different response — system fix, coaching, or accountability. Corrective actions are systems-level (protocol change, EHR redesign, staffing model) more often than individual.

**Forbidden moves.**
- *Blame.* Naming individuals as causal agents; the artifact's failure.
- *Hindsight bias.* *"They should have known"* with knowledge unavailable at the time.
- *Performative humility.* *"We could have done better"* as a substitute for specific analysis.
- *Narrative smoothing.* Filling gaps in the chronology with assumption.

**Exemplars.** AHRQ Patient Safety Network *WebM&M Cases and Commentaries* (the canonical contemporary corpus); *Annals of Internal Medicine* *Mortality Rounds*; IHI Open School *Root Cause Analysis* module; ACS NSQIP M&M conference structure; Aviation's NTSB accident reports as the cross-domain parent.

**Failure modes specific.** *The bad-apple frame* — single individual blamed, no system analysis. *Hindsight collapse* — the case reads as obvious in retrospect, no acknowledgement that it was not obvious at the time. *No corrective action* — analysis without commitment. *Corrective action that requires perfection* — *"the resident should remember to..."* — Just Culture explicitly rejects this as a non-fix.

**Cross-references.** `references/medium-playbooks/cross-cluster/operating-manual.md` for the corrective-action genre when it produces a protocol. §16 (code-blue events) and §15 (handoff failures) are the most-common M&M case sources. `references/medium-playbooks/clinical-case.md` for the teaching-case form (different audience, different intent — M&M is systems analysis, not pedagogy).

---

## 18. Quality-Improvement and PDSA artifacts

Quality improvement is the prospective complement to M&M's retrospective analysis. The Institute for Healthcare Improvement's Model for Improvement (Langley, Nolan *et al.*, *The Improvement Guide* 1996/2009) is the dominant framework, and ACGME requires every resident to lead or participate in a QI project before graduation.

**The Model for Improvement — three questions and a cycle.**
1. *What are we trying to accomplish?* — the *aim statement*, written in SMART form: specific, measurable, achievable, relevant, time-bound. *"Increase the proportion of eligible inpatients receiving VTE prophylaxis on hospital day 1 from 67% to 90% by end of Q3."* The aim is the contract; ambiguity here kills the project.
2. *How will we know that a change is an improvement?* — *measures*, of three kinds: outcome (the thing we ultimately care about — VTE rate), process (the thing we are changing — VTE prophylaxis ordered), balancing (the unintended consequence to watch — bleeding rate). All three are required; a project with only process measures cannot demonstrate improvement.
3. *What changes can we make that will result in improvement?* — *change ideas*, derived from process mapping, driver diagrams, or front-line interviews.

**The PDSA cycle.** Plan (predict; design the test; specify who-does-what-when); Do (run the test; record what actually happened including the unexpected); Study (compare prediction to result); Act (adopt, adapt, or abandon). One PDSA cycle is rarely sufficient; the discipline is *small, fast, iterated*.

**The run chart.** The canonical QI visualisation. Time on x-axis, measure on y-axis, median line, intervention markers as vertical annotations. Apparent improvement is tested against four non-random-signal rules (shift of ≥ 6 points on one side of median; trend of ≥ 5 increasing or decreasing points; runs of ≥ 8; astronomical data point). Provost & Murray, *The Health Care Data Guide* (2nd ed., 2022) is the canonical reference for run-chart and Shewhart-chart interpretation in healthcare.

**The driver diagram.** Aim → primary drivers (the leverage points) → secondary drivers (specific changes) → change ideas. Visual logic-model that links the aim to the interventions. A QI project without a driver diagram is hard to evaluate; the diagram is the project's theory of change.

**The SQUIRE 2.0 reporting framework.** Standards for Quality Improvement Reporting Excellence (Ogrinc *et al.* 2015) — the QI counterpart to CONSORT. Twenty-one items spanning context, intervention, study of intervention, measures, ethical considerations, results, lessons. Required for publication in journals like BMJ Quality and Safety.

**Exemplars.** IHI Open School curriculum; Provost & Murray *The Health Care Data Guide*; the BMJ Quality Improvement Reports archive; *Pediatrics*' QI feature; Cincinnati Children's' published improvement portfolio.

**Failure modes specific.** *No balancing measure* — the project documents process improvement but ignores the harm it caused. *Pre-post without statistical-process-control framing* — claiming improvement from random variation. *Aim drift* — the aim statement is revised mid-project to match the result. *Project graveyard* — single PDSA cycle, no iteration, no adoption.

**Cross-references.** §17 (M&M cases often surface the system gap that becomes a QI aim); `references/libraries/visualization-grammar.md` for run-chart and Shewhart-chart conventions; `references/medium-playbooks/cross-cluster/operating-manual.md` for the protocol artifacts QI projects often produce.

---

## 19. Surgical-specific genres

Surgery's artifact catalogue overlaps with internal medicine but adds genres specific to the operative discipline. The conventions below are visible across orthopaedics, general surgery, neurosurgery, urology, and otolaryngology, with subspecialty variation in the technical detail.

- **Operative note (op note).** Medico-legal *and* billing artifact. Standard sections, dictated within hours of the case: PRE-OP DIAGNOSIS / POST-OP DIAGNOSIS (often identical, sometimes diverged by intra-op findings); PROCEDURE (named in CPT-aligned terminology — *"Right total hip arthroplasty, cementless, posterior approach"*); SURGEON, ASSISTANTS, ANAESTHESIA TYPE; INDICATIONS (one paragraph linking the diagnosis to the procedural decision); FINDINGS (intra-op observations); TECHNIQUE (the narrative of the operation, step-by-step at a fidelity that would let a peer surgeon understand what was done); ESTIMATED BLOOD LOSS (EBL); SPECIMENS sent to pathology; IMPLANTS used (manufacturer, catalog number, size — required for recall and for revision surgeons years later); DRAINS placed; DISPOSITION. The TECHNIQUE section is the longest; ambiguity here surfaces in revision surgery a decade later.

- **Pre-operative planning note.** Subspecialty-specific. In arthroplasty: templating measurements on calibrated radiographs, implant size and offset selection, leg-length-discrepancy plan. In spine: level localisation, instrumentation selection. In trauma: fracture classification, reduction strategy, implant inventory. The pre-op plan is the surgeon's hypothesis; the op note records what was actually done. Discrepancies between plan and execution are themselves teaching material.

- **Surgical technique guide.** AO Surgery Reference is the canonical contemporary register: step-by-step layout, each step with anatomy figure + intra-operative photo or schematic + dictation-grade caption. Campbell's Operative Orthopaedics (now 14th ed.) and the *Journal of Bone and Joint Surgery Essential Surgical Techniques* (JBJS-EST) maintain the long-form printed tradition. The genre's design discipline: per step, the reader should be able to perform it without the surrounding pages.

- **Fracture-classification atlas.** Visual taxonomy as comparative-plate convention. AO/OTA (the universal long-bone scheme), Garden (femoral neck I–IV), Schatzker (tibial plateau I–VI), Salter-Harris (paediatric physeal I–V), Gustilo-Anderson (open-fracture I/II/IIIA/IIIB/IIIC), Neer (proximal humerus 2/3/4-part), Weber (ankle A/B/C). Each classification is visualised as a labelled grid of subtype illustrations on one page — the comparative-plate form is itself the teaching artifact.

- **Surgical informed consent.** Procedure-specific risks named by anatomical structure (*"injury to the sciatic nerve causing foot-drop, occurring in roughly 1 in 200 posterior-approach hip arthroplasties"*), not aggregated. Named alternatives including non-operative management. Implant-related disclosures (off-label use, manufacturer-recall history, expected revision interval).

- **Surgical M&M case.** Radiograph timeline (pre-op, immediate post-op, follow-up), intra-op decision points (each named with the option chosen), named complication using standardised vocabulary (Clavien-Dindo for general surgery; equivalent specialty taxonomies elsewhere). See §17 for the M&M discipline; surgical M&M's distinguishing feature is the imaging timeline as evidentiary spine.

- **Surgical illustration conventions.** Anatomic overlay on imaging (the surgical approach drawn over a CT or MRI slice, with structures-at-risk shaded); portal mapping (arthroscopic portal locations on a surface-anatomy diagram with depth and direction noted); surgical-approach diagrams with the interval between named muscles indicated and the neurovascular structures at risk labelled. Netter's surgical atlases and Hoppenfeld's *Surgical Exposures in Orthopaedics* are the calibration references.

- **Device documentation tradition.** Synthes (now DePuy Synthes), Stryker, Zimmer-Biomet, Smith & Nephew, Arthrex — surgical-implant manufacturers produce technique brochures that are themselves designed artifacts: high information density, exploded-view CAD renderings, step-by-step photography with surgical-hand pose, sizing tables. The genre's craft level is high; surgeons learn from these documents during residency and after.

- **Surgical coding.** CPT (procedural) and ICD-10-PCS (the seven-character grammar for hospital procedural coding: section / body-system / root operation / body part / approach / device / qualifier). Modifiers (-50 bilateral, -59 distinct procedural service, -22 increased complexity, -78 return to OR for related procedure). Billing-driven documentation patterns — the op note's TECHNIQUE section length is partly a coding artifact.

**Exemplars.** AO Surgery Reference; Campbell's Operative Orthopaedics; Hoppenfeld *Surgical Exposures*; Netter surgical atlases; JBJS-EST; the AAOS *OrthoInfo* patient-education library for the lay counterpart; Clavien-Dindo classification (Ann Surg 2004) for complication taxonomy.

**Failure modes specific.** *Op note from memory days later* — implant catalogue numbers wrong, sizes guessed. *TECHNIQUE that reads as boilerplate* — generic dictation indistinguishable across cases. *Classification without reference standard* — *"comminuted fracture"* instead of *"AO/OTA 32-B2.3"*. *Surgical illustration without structures-at-risk* — the approach diagram is decorative, not protective.

**Cross-references.** Surgical illustration conventions integrate with the new SVG register 16 (medical-imaging overlay) being added in Wave 10. `references/medium-playbooks/clinical-algorithm.md` for the pre-op decision-tree form. `references/medium-playbooks/cross-cluster/operating-manual.md` for the surgical-safety-checklist form (WHO Surgical Safety Checklist).

---

## 20. Sports-medicine-specific genres

Sports medicine's artifact catalogue spans clinic, training room, sideline, event venue, and rehab gym. The multi-stakeholder structure (athlete, athletic trainer, team physician, coach, parent, agent) drives much of the genre-specific design discipline.

- **Physical-exam maneuver reference.** Hoppenfeld's *Physical Examination of the Spine and Extremities* (1976) and Magee's *Orthopedic Physical Assessment* (now 7th ed.) are the canonical references. Standard layout per maneuver: surface-anatomy figure showing examiner and patient position, provocative test description, named eponym (Lachman, McMurray, Hawkins-Kennedy, Spurling), reported sensitivity and specificity with study citation, composite-test logic (no single maneuver is diagnostic; the cluster is).

- **Pre-Participation Evaluation (PPE).** The PPE Monograph (5th ed., AAP / AAFP / ACSM / AMSSM / AOSSM / AOASM consensus) defines the standard form. Cardiovascular screening section is the highest-stakes element: the 14-item AHA screening history (with explicit red-flag thresholds), the family-history items for hereditary cardiomyopathies and channelopathies, the murmur-with-dynamic-manoeuvres exam discipline. Sudden cardiac death prevention drives the form's structure.

- **Concussion assessment instruments.** SCAT6 (Concussion in Sport Group, Amsterdam 2023; *Br J Sports Med* 2023) for athletes ≥ 13y; Child-SCAT6 for 5–12y; CRT6 (Concussion Recognition Tool) for non-medical sideline use. Baseline-vs-current symptom inventory; cognitive testing (orientation, immediate memory, concentration, delayed recall); balance examination (modified BESS); cervical spine and neurological screen. Multi-stakeholder signoff (athlete, parent, AT, physician).

- **Graduated Return-To-Play (GRTP).** Six-stage protocol (Amsterdam 2023): symptom-limited activity → light aerobic → sport-specific exercise → non-contact training drills → full-contact practice (medical clearance required) → return to sport. Minimum 24h per stage; symptom return triggers reversion. Criterion-gated, time-bound, multi-stakeholder-signed. The artifact lives as a printed card or EHR template the athlete carries between team-physician, AT, and coach.

- **Rehab progression protocol.** ACL post-operative protocols (MOON, Shelbourne, Delaware-Oslo) as the canonical exemplars. Phased timeline (weeks 0–2 / 2–6 / 6–12 / 3–6 mo / 6–9 mo / 9–12 mo); entry criteria per phase (range of motion, swelling, gait, single-leg hop limb symmetry index ≥ 90%); milestone-gated rather than time-gated transitions. Return-to-sport criteria (MOON RTS battery; battery-passing rate at 9 months ~25%, indicating the discipline of the gate).

- **Sideline Emergency Action Plan (EAP).** NATA position-statement template. Venue diagram with AED location, ambulance route, communication tree, role assignments (who calls 911, who manages airway, who meets EMS, who notifies family). Rehearsed annually. Cervical-spine immobilisation algorithm. Heat-illness and lightning protocols by region. Distinct from a generic emergency plan because the venue-specific detail is the artifact's point.

- **Event-medicine medical action plan (MAP).** Mass-participation events (marathons, triathlons, large tournaments). ACSM Sideline Emergency Care tradition; *British Journal of Sports Medicine* mass-participation event guidelines. Per-mile aid-station layout; transport algorithm; collapse-triage flow; hyponatraemia-vs-dehydration decision pathway.

- **Athlete summary sheet.** One page per athlete on the team physician's desk: photo, position, season, relevant medical history, current injuries with phase and restriction, medication list with TUE (therapeutic use exemption) status, baseline cognitive and balance scores, allergies, emergency contact. Format is institutional but the conventions are stable across professional and collegiate sports medicine.

- **Athlete-as-stakeholder informed consent.** Return-to-play risk under uncertainty (the second-impact-syndrome conversation). Orthobiologic off-label use (PRP, BMAC, stem-cell preparations — most off-label; the consent must say so). Pediatric assent + parental permission for the under-18 athlete. Distinct from the surgical consent (§19) because the decision is preference-sensitive under genuine equipoise (continue this season vs. surgical management now), not procedural.

- **Athletic-trainer–physician collaboration artifacts.** Sideline-to-clinic handoff note (the AT's documentation that becomes the physician's intake); daily training-room treatment log (every athlete encounter, time-stamped); activity-restriction communication to coach (one-line: *"Cleared for full practice"* / *"Practice limited to non-contact drills through Friday"* / *"Held"*); return-to-sport clearance form signed by physician with AT acknowledgement.

- **MSK imaging-overlay clinical-correlation plate.** Diagnostic and procedural ultrasound is the dominant modality. Long-axis / short-axis / dynamic views; arrow-and-callout annotations identifying the lesion; clinical-correlation paragraph linking image finding to exam finding to plan. Static MRI correlation plates similarly: arrow-and-callout overlaying the MR slice with the named structure and the finding.

**Exemplars.** Hoppenfeld; Magee; PPE Monograph 5th ed.; Concussion in Sport Group SCAT6 (*Br J Sports Med* 2023); MOON ACL Return-to-Sport battery; NATA position statements on EAPs; AOSSM resources.

**Failure modes specific.** *Time-gated rehab without criterion gates* — the athlete progresses on the calendar regardless of recovery. *Sideline EAP that wasn't rehearsed* — exists on paper, fails in practice. *Concussion clearance under social pressure* — protocol bypassed for playoff games. *Activity-restriction communication via text* — informal, undocumented, deniable.

**Cross-references.** Physical-exam maneuver illustration integrates with the new SVG register 17 (physical-exam maneuver) being added in Wave 10. The athlete summary sheet shares conventions with `references/medium-playbooks/dashboard.md` (multi-panel decision tool). `references/medium-playbooks/cross-cluster/operating-manual.md` for the EAP and concussion protocol as if-then artifacts.

---

## 21. Clinical Practice Guideline as a designed artifact

Clinical practice guidelines (CPGs) are among the most-consequential designed artifacts in medicine — they shape practice, billing, malpractice standards-of-care, and quality measures across millions of encounters. The published guideline document is itself a designed artifact, distinct from the algorithm visualisations it contains (those live in `references/medium-playbooks/clinical-algorithm.md`).

**Canonical front-matter conventions.**
- *Writing-committee disclosure.* Members listed with affiliations and conflicts-of-interest declarations. ACC/AHA require the committee composition to include at least 50% members free of relevant industry relationships; the disclosure table is published with the guideline.
- *Methodology section.* Search strategy (databases, dates, MeSH terms); inclusion/exclusion criteria; evidence synthesis framework (GRADE, GRADE-ADOLOPMENT for adapted recommendations, Cochrane).
- *Funding source.* Disclosed at front; ACC/AHA explicitly fund their own writing committees to avoid industry sponsorship of the guideline itself (an institutional design decision visible in every published document).

**The recommendation-class / level-of-evidence banner.** ACC/AHA tradition since 2008, harmonised globally. Class of Recommendation (Class I = strong, IIa = moderate in favour, IIb = weak in favour, III = no benefit or harm). Level of Evidence (A = high-quality RCTs or meta-analyses; B-R = moderate-quality RCT data; B-NR = moderate-quality non-randomised; C-LD = limited data; C-EO = expert opinion). The 2×3 (or 2×5) grid is itself a designed convention — color-banded, abbreviation-disciplined, applied consistently to every recommendation. Misuse of the convention (writing a Class I rec with C-EO evidence without explicit justification) is itself a documentation failure.

**Evidence-summary tables.** Each recommendation backed by an Evidence Summary Table listing the supporting studies (study design, N, effect size with confidence interval, risk of bias). The table is the warrant for the rec; the rec without the table is opinion.

**The "Top 10 Take-Home Messages" register.** ACC/AHA convention since ~2018. The first page of the published guideline is a numbered list of the ten most-important clinical changes from the prior version. Designed for the clinician who will not read the full 100-page document — a deliberate concession to attention economics. The register's design discipline: each message ≤ 50 words, action-oriented, with rec-class banner.

**Recommendation-Specific Supportive Text (RSST).** ACC/AHA 2017+ convention. Each recommendation followed by a paragraph that summarises the supporting evidence, addresses minority opinions, and notes implementation considerations. The RSST is what makes the rec interpretable in cases the rec did not anticipate.

**The published-document design choices.** Typography (typically a serif body with clinical-mode discipline); two-column or single-column layout (varies by publisher); the algorithm figures as set-pieces with their own caption convention; internal cross-references using rec numbers (*"see Recommendation 4.2.1"*). NICE guidelines (UK) maintain a strikingly different visual register — denser tables, less typographic hierarchy, explicit "Why this recommendation matters" narrative paragraphs.

**Exemplars.** ACC/AHA *Guideline for the Management of Patients with Atrial Fibrillation* (2023) for the contemporary North-American register; ESC guidelines for the European register; NICE *NG-series* guidelines for the UK register; WHO Consolidated Guidelines for the global-health register; NCCN Clinical Practice Guidelines in Oncology for the oncology decision-tree-dominant register; IDSA infectious-disease guidelines for the focused-question register.

**Failure modes specific.** *Class I / Level C-EO* used reflexively without acknowledgement that the recommendation is expert opinion. *Rec without RSST* — the clinician cannot adapt to the case the rec did not anticipate. *Evidence-summary table not provided* — the warrant is invisible. *Industry-sponsored guideline with no disclosure* — the most-eroding failure of trust.

**Cross-references.** `references/medium-playbooks/clinical-algorithm.md` (Wave 10) for the algorithm figures *within* the guideline. `references/medium-playbooks/cross-cluster/operating-manual.md` for the implementation-pathway artifacts derived from guidelines. §22 below for the institutional artifacts that translate guidelines into local workflow.

---

## 22. Specialised clinical-decision artifacts

Five sub-genres often conflated, each with distinct design language and failure modes. The taxonomic discipline below matters because choosing the wrong genre for the job is the dominant failure mode.

- **Clinical pathway / care bundle.** Time-anchored, multi-step institutional translation of guideline recommendations into local workflow. Surviving Sepsis Campaign Hour-1 Bundle (lactate / blood cultures / broad-spectrum antibiotics / 30 mL/kg crystalloid for hypotension or lactate ≥ 4 / vasopressors for MAP < 65) — the bundle's clock-anchor is the design feature. Enhanced Recovery After Surgery (ERAS) protocols span pre-op-to-discharge with per-phase interventions (pre-op carbohydrate loading; intra-op opioid-sparing anaesthesia; post-op early ambulation and feeding; discharge criteria). ABCDEF ICU bundle (Awakening / Breathing / Coordination / Delirium / Early mobility / Family) — Vanderbilt-developed; published Society of Critical Care Medicine. Pathway artifacts are typically displayed as swim-lane diagrams or time-anchored grids (see swim-lane sub-genre below).

- **Choosing Wisely card.** Single-page negative-recommendation register. ABIM Foundation Choosing Wisely campaign (launched 2012; now > 80 specialty societies participating). Format: specialty society; headline-as-claim (*"Don't do X"*); supporting evidence paragraph; alternative action (*"do Y instead"*). The design language is intentionally distinct from positive guideline recommendations — typically a red banner or stop-sign register signalling the negative-recommendation grammar. Choosing the negative-rec format communicates that *not* ordering the test or treatment is the deliberate, evidence-based action.

- **FDA Boxed Warning (the "black box").** Regulatory-weight warning convention. The boxed-warning rectangle is itself the regulatory artifact: bordered with a heavy black rule, drug-name and risk in bold, monitoring requirements specified, REMS (Risk Evaluation and Mitigation Strategies) requirements noted where applicable. Examples: thiazolidinediones (heart failure); fluoroquinolones (tendinopathy and aortic dissection); SGLT2 inhibitors (Fournier's gangrene); SSRIs in adolescents (suicidality). The visual treatment carries regulatory force — the boxed-warning rectangle in the package insert and patient medication guide is required by 21 CFR 201.57(c)(1). Misuse of the convention (cosmetic boxed-warning-style boxes in non-regulatory artifacts) is itself a failure mode that erodes the convention's signal.

- **EHR Clinical Decision Support (CDS) artifact.** The Epic SmartSet, Cerner PowerPlan, MEDITECH order set, or Best Practice Advisory (BPA) is the designed artifact. Osheroff's *Five Rights of CDS* (the right information / to the right person / via the right channel / in the right format / at the right time) is the canonical design discipline. Order-set design discipline: pre-selected defaults reflect guideline recommendations; required fields prevent incomplete orders; warnings trigger only on actionable conditions. Alert-fatigue calibration is the dominant design challenge — Ancker *et al.* (J Am Med Inform Assoc 2017) documented BPA override rates above 90% in many implementations, making the alert worse than useless. Distinct from the printed algorithm (§21, clinical-algorithm.md) because the CDS lives *inside* the EHR workflow and inherits the workflow's affordances and constraints.

- **Patient-pathway swim-lane map.** Multi-department whole-encounter map. BPMN (Business Process Model and Notation) – derived; time-anchored along the x-axis; one swim-lane per department or role (ED, OR, ICU, ward, discharge planning, community provider); handoff markers at lane crossings; intervention markers within lanes. NHS Improvement *Pathway Mapping* (2005) is the canonical methodology reference; Mayo Clinic Diagnostic and Treatment Process Maps for the institutional implementation; *BMJ Quality and Safety* publishes pathway-mapping case studies. The swim-lane visual is itself the analytical artifact — the gaps and crossings are where waste, delay, and error live.

**Choosing among the five.** A pathway is a *workflow*; a Choosing Wisely card is a *negative recommendation*; a boxed warning is a *regulatory artifact*; a CDS is an *embedded computational nudge*; a swim-lane is an *analytical map*. Each has its own audience and lifecycle.

**Exemplars.** Surviving Sepsis Campaign Hour-1 Bundle; ERAS Society protocols; SCCM ICU Liberation ABCDEF bundle; ABIM Foundation Choosing Wisely lists; FDA package-insert structured-product-labeling specification; Osheroff *Improving Outcomes with Clinical Decision Support* (2nd ed., HIMSS); NHS Improvement *Improvement Leaders' Guide: Process Mapping*; Mayo Clinic Diagnostic and Treatment Process Maps.

**Failure modes specific.** *Cosmetic boxed-warning treatment* on non-regulatory content (erodes the regulatory signal). *Pathway as wall art* — published but not implemented in workflow. *Choosing Wisely card written as a positive recommendation* — buries the lede; loses the genre's distinctive force. *CDS without alert-fatigue calibration* — every order triggers a BPA; clinicians override reflexively; the one critical alert is missed. *Swim-lane without time anchor* — shows process but not the delay analysis the form exists to surface.

**Cross-references.** `references/medium-playbooks/clinical-algorithm.md` (Wave 10) for the algorithmic decision-tree form (a CDS often *implements* an algorithm). `references/medium-playbooks/cross-cluster/operating-manual.md` for the checklist register that pathways and bundles share. §21 (clinical practice guidelines, which these artifacts implement). §17 (M&M cases that surface the system gap a new pathway is designed to close).

---

## 8. Cross-references

- `references/libraries/color-library.md` — medical palettes in context of broader color space
- `references/libraries/visualization-grammar.md` — isotype/waffle for risk, choropleths for epidemiology
- `references/libraries/inspiration-atlas.md` — anatomical illustration tradition
- `references/libraries/iconography-library.md` — medical symbols (staff of Asclepius, prescription Rx, biohazard, etc.)
- `references/libraries/pedagogy-library.md` — medical education traditions (case method, OSCEs, problem-based learning, Osler apprenticeship model)
- `references/libraries/reader-models.md` — patient, clinician, researcher, family-member personas

---

## 9. Extending this library

Add to this library when:
- A medical sub-specialty has distinct visualization/communication traditions
- New risk-communication research surfaces useful patterns
- A notable medical illustrator / publication deserves referencing

Avoid:
- Prescribing specific clinical approaches (that's medicine's job)
- Generic "health dashboard" patterns without medical grounding
- Treating this as a substitute for clinical subject-matter expertise

The goal: expand the creative and communicative space for artifacts *about* medicine, not replace medical judgment.

<!-- END: references/libraries/medical-artifacts.md -->

---


<!-- BEGIN: references/libraries/motion-library.md -->

# Motion Library

A platter, not a spec. Motion design is a domain unto itself — Disney animation's 12 principles, UI motion language conventions, film editing rhythm, game feel, scientific visualization of dynamics, kinetic poster design. This library widens the space Claude draws from when asking "should this move, and how?"

> See `references/how-to-use-this-system.md` for the platter principle.

---

## 1. The fundamental question

Before *how*, ask **whether**. Motion has real costs: attention cost, performance cost, accessibility cost. Default to no motion; add it when it pays its rent.

### Motion earns its place when it:
- **Communicates causality** — "this caused that" via motion linking them
- **Preserves continuity** — maintains context across a state change
- **Signals affordance** — shows the reader what's interactive
- **Provides feedback** — confirms an action landed
- **Directs attention** — guides the eye to what's changing
- **Reveals structure** — animating a data transition shows the relationship
- **Creates emotional texture** — when the artifact's tone warrants it

### Motion fails when it:
- Is decorative without function
- Delays the reader from their goal
- Competes with other attention-requiring elements
- Makes users with vestibular disorders motion-sick
- Prevents users from reading at their own pace
- Feels performative ("look what I can do")

---

## 2. Animation principles across traditions

### Disney's 12 Principles (Thomas & Johnston, 1981)

Classical animation's foundational vocabulary. Apply sparingly to UI; applied liberally to character animation.

1. **Squash & stretch** — objects deform under force, snap back
2. **Anticipation** — winding up before the main action
3. **Staging** — arranging the frame to direct attention
4. **Straight-ahead vs. pose-to-pose** — animating linearly vs. keyframe-to-keyframe
5. **Follow-through & overlapping action** — parts trail the main action
6. **Slow-in & slow-out** — easing (not linear motion)
7. **Arcs** — natural motion follows curves, not straight lines
8. **Secondary action** — smaller motions supporting the main one
9. **Timing** — the *when* and *how fast*
10. **Exaggeration** — push beyond realism for readability
11. **Solid drawing** — character animation with dimensional conviction
12. **Appeal** — aesthetic charisma of the animated element

**For UI motion:** the relevant principles are anticipation (a tiny delay before reveal), slow-in/slow-out (cubic-bezier, never linear), follow-through (a child element trailing its parent), and timing (the difference between 120ms, 240ms, and 480ms is the difference between "snappy," "considered," and "deliberate").

### UI motion traditions

**Material Motion** (Google) — emphasized, slow-in-slow-out; elements emerge from and collapse into common ancestors. Documented extensively at `m3.material.io/foundations/motion`.

**Apple HIG motion** — subtle, fast, physics-based. Spring curves dominate. Motion should feel like physical properties of the elements.

**IBM motion** (product tradition) — more explicit timing; meaningful easing by category.

**Linear's motion language** — inertial, under 240ms, rarely more than 100ms for hover states. A masterclass in restraint.

**Framer / Rive motion** — rich spring physics; draggable, flingable interactions.

**Stripe's product motion** — subtle confirmation animations; careful transition in form flows.

**Vercel / Next.js marketing motion** — scroll-linked, crisp, gallery-like.

### Film / cinema timing

Film editors think of time differently than UI designers:
- **Cut** — instantaneous
- **Dissolve** — 15-45 frames (0.5-1.5s) of overlap
- **Fade** — 30-60 frames (1-2s) to black or from black
- **Match cut** — cut at a visual correspondence; no transition needed

UI borrows "cut" (instant) and "dissolve" (crossfade), but rarely "fade" (too slow for UI).

### Game feel (Steve Swink, *Game Feel*)

Game design has a vocabulary for what makes interaction *satisfying*:
- **Response time** — how fast the system responds (< 100ms feels instant)
- **Context** — what else is happening around the interaction
- **Polish** — particles, sound, screen shake, color flashes that amplify

For UI, game-feel thinking elevates moments: button presses, successful form submissions, state changes.

### Kinetic typography

Motion applied to type. Saul Bass's opening titles; contemporary kinetic type in film trailers and music videos. Text that moves with meaning — not just decoration.

### Scientific animation

Data-driven animation where motion encodes data:
- Evolving distributions
- State-space trajectories
- Simulation playback
- Temporal maps

Constraints differ from UI motion — here, motion IS the data. Speed, smoothness, and labels matter for interpretation, not ornament.

---

## 3. Timing vocabulary

Durations have meaning. The same animation at different speeds communicates different things.

| Duration | Feels like | Use for |
|----------|-----------|---------|
| 0ms (instant) | Sharp, decisive | Hard cuts, immediate feedback |
| 60–100ms | Snappy, responsive | Hover states, micro-interactions |
| 120–200ms | Quick transition | Tab switches, panel reveals, button states |
| 200–300ms | Considered, graceful | Modal entry, page transitions |
| 300–500ms | Deliberate, cinematic | Emphasis reveals, onboarding moments |
| 500–1000ms | Narrative | Scroll-driven reveals, story beats |
| 1000ms+ | Ambient | Background motion, breathing UI, loading states |

**For UI, most motion should live in the 120-300ms band.** Under 120ms is borderline perceptible (feels broken); over 300ms delays the reader.

---

## 4. Easing functions

Easing defines how duration is distributed across the animation. The shape matters more than the duration.

### Fundamental easings

- **Linear** — constant velocity. Feels robotic, mechanical. Use only for true constant-velocity motion (loading bars, clocks).
- **Ease-in** (slow start, fast end) — appropriate for elements *leaving* (building acceleration away).
- **Ease-out** (fast start, slow end) — appropriate for elements *arriving* (settling into place).
- **Ease-in-out** — both. Smooth both ways. General-purpose; often overused.

### Specific curves worth knowing

- **Standard** `cubic-bezier(0.4, 0, 0.2, 1)` — Material's default. Balanced.
- **Emphasized** `cubic-bezier(0.2, 0, 0, 1)` — stronger slow-in-slow-out.
- **Emphasized-decelerate** `cubic-bezier(0.05, 0.7, 0.1, 1)` — for entering elements.
- **Emphasized-accelerate** `cubic-bezier(0.3, 0, 0.8, 0.15)` — for exiting elements.
- **Bouncy** — overshoot then settle. For playful or celebratory moments.
- **Spring** — physics-based; no fixed duration, but stiffness and damping parameters. Apple default.
- **Out-back / in-back** — overshoots slightly; appropriate for landing with confidence.

### Spring physics

Spring animations are parameterized differently:
- **Stiffness** — how strong the pull back to target
- **Damping** — resistance; higher damping = faster settling
- **Mass** — how heavy the element feels

Framer Motion and Apple-native APIs use springs. They feel physical; they don't have a strict duration. Good for direct-manipulation interactions (drag, release, snap).

---

## 5. Motion patterns

Common recipes. Each is one option.

### Enter animations

- **Fade in** — `opacity: 0 → 1` over 200-300ms. The gentle default.
- **Slide in from direction** — `translateY(8px) → 0` or `translateX(-16px) → 0`. Provides directional context.
- **Scale in** — `scale(0.95) → 1` with fade. Slight presence.
- **Stagger** — child elements enter in sequence, offset by 30-80ms each. Choreography.

### Exit animations

- **Fade out** — `opacity: 1 → 0` over 120-200ms.
- **Slide out** — opposite of slide in.
- **Scale down + fade** — `scale(1 → 0.95)` with fade.
- **Fold up** — `height: auto → 0` for accordion-style close.

### Transitions between states

- **Cross-fade** — overlap old and new, 200-300ms.
- **Morph** — shape interpolation between source and destination.
- **Shared element transition** — an element that persists across a route change, animating its position/size.
- **Layout transition** — the `FLIP` technique (First, Last, Invert, Play) — record before/after positions, animate the difference.

### Feedback / confirmation

- **Pulse** — scale from 1 to 1.05 and back. Attention without distraction.
- **Glow** — box-shadow animation. For moment of focus.
- **Flash** — brief color change. Very brief (100ms).
- **Check animation** — icon draws from nothing (strokeDashoffset animation).
- **Toast** — slide in from edge, rest, slide out. 2.5-5s total.

### Attention / wayfinding

- **Bounce** — vertical translateY back and forth. Draws attention without demanding it.
- **Shake** — horizontal translateX back and forth, few cycles. Signals error (traditional).
- **Highlight** — background-color flash (subtle).
- **Arrow hint** — arrow animated toward a target with gentle bounce.

### Loading / waiting

- **Spinner** — continuous rotation. Linear motion is correct here.
- **Skeleton** — shimmering background on placeholder shapes. Implies progress.
- **Progress bar** — linear fill. Real progress or indeterminate cycling.
- **Ellipsis** — cycling dots. Low-effort, low-information.

### Playback

- **Scrubbable timeline** — reader drags to any point.
- **Play/pause/speed controls** — standard affordances.
- **Playback with animation ease** — slight anticipation before a step for readability.

### Scroll-linked

- **Parallax** — foreground and background move at different rates. Can feel premium; can feel gimmicky.
- **Sticky + content change** — element stays pinned while other content scrolls past and around it.
- **Scroll-trigger reveals** — elements fade/slide in as they enter viewport.
- **Pinned with progress** — element pinned, progresses through states based on scroll distance.

---

## 6. Motion for communication

Every motion should ask: *what is this communicating?*

### Direct mapping

Motion directly encodes meaning:
- A dot tracing the gradient-descent path
- A particle moving through a simulated flow
- A chart transition where the eye follows the morphing bars

Here motion IS the data. Apex work treats it with the same rigor as static visualization — labeled, slow enough to read, paced to reveal.

### Metaphorical

Motion signals meaning by convention:
- A tab's indicator sliding to the active tab
- A dropdown panel unfolding downward
- A dialog entering from center with a slight scale-up

The convention tells the reader "this is how this UI works." Consistency within an artifact matters more than novelty.

### Emotional texture

Motion sets emotional tone:
- Slow, heavy easing → serious, considered, luxurious
- Fast, snappy → efficient, technical, alert
- Bouncy, overshooting → playful, consumer, optimistic
- Rigid, linear → mechanical, formal, data-driven

Choose the easing and duration family that matches the artifact's tone. They should not fight.

---

## 7. Reduced motion

Respect `prefers-reduced-motion: reduce`. The Web Content Accessibility Guidelines specify this; so does macOS and Windows settings.

### What to do with reduced motion

- **Decorative motion:** disable entirely, or reduce to crossfade.
- **Motion that communicates continuity:** keep, but shorten and simplify (fade in 80ms instead of slide + fade 300ms).
- **Motion that carries meaning:** keep, but reduce parallax, large translations, and rotation.
- **Auto-playing animations:** pause by default.

Implementation pattern:
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
  /* Preserve specific animations that communicate meaning: */
  .semantic-animation { animation-duration: revert !important; }
}
```

In framer-motion: `<MotionConfig reducedMotion="user">` at root.

---

## 8. Motion performance

Motion should never cause jank.

### What's cheap
- `transform` (translate, scale, rotate)
- `opacity`
- `filter` (in moderation)

These are GPU-composited and don't trigger layout.

### What's expensive (trigger layout or paint)
- `width`, `height` (unless via transform scale)
- `top`, `left`, `right`, `bottom` (use `transform: translate` instead)
- `margin`, `padding`
- `box-shadow` on large surfaces
- `backdrop-filter` (GPU but costly)

### Principles

- Prefer `transform: translate3d()` over `top`/`left`.
- Animate containers; composite children in a single group.
- Use `will-change: transform, opacity` sparingly, only on actively animating elements.
- `requestAnimationFrame` for JS-driven animation; don't use `setInterval`.
- On scroll-heavy pages, debounce or throttle listener handlers.

---

## 9. Accessibility considerations beyond reduced-motion

- **Vestibular triggers** — large translations, spinning elements, 3D depth transitions. Avoid or reduce.
- **Flashing content** — do not flash more than 3 times per second. Seizure risk.
- **Auto-play** — never auto-play video with sound. Provide pause controls for any ambient motion.
- **Reading disruption** — avoid motion near body text; it pulls the eye off.
- **Cognitive load** — fewer simultaneous animations. One clear motion beats three competing ones.

---

## 10. Motion as signature move

Apex artifacts sometimes deploy motion as the single most-memorable craft element:
- A scroll-driven narrative where the chart animates in sync with the prose
- A simulation where the motion IS the data
- A micro-interaction on the primary CTA that makes the button feel physical
- A page transition that cross-fades over a shared element

When motion is the signature move, commit fully: perfect timing, perfect easing, perfect restraint in the rest of the artifact so the motion lands.

---

## 11. Cross-references

- `references/wow-taxonomy.md` — motion-based wow moves
- `references/design-tokens.md` — duration and easing token set
- `references/medium-playbooks/claude-react-artifact.md` — framer-motion usage
- `references/libraries/composition-library.md` — how motion relates to layout

---

## 12. Extending this library

Add a motion tradition or pattern when:
- It represents a genuinely distinct approach
- It has a documented history or recognized convention
- It solves a class of problem

Avoid:
- Trend-chasing (every new "website of the day" animation)
- One-off patterns without a recurring use case

The goal is a durable vocabulary, not a trend tracker.

<!-- END: references/libraries/motion-library.md -->

---


<!-- BEGIN: references/libraries/pedagogy-library.md -->

# Pedagogy Library

A platter of teaching traditions and cognitive-science findings, not a single recommended sequence. Teaching artifacts benefit enormously from deliberate pedagogical choice — but only if the choice is informed by a wide enough space of traditions to find one that genuinely fits the subject and learner.

> See `references/how-to-use-this-system.md` for the platter principle.

---

## 1. Teaching traditions

Major pedagogical traditions, their underlying assumptions, and where each fits.

### Direct instruction

Teacher states the concept, demonstrates it, gives worked examples, then has learners practice.

- **Structure:** tell → show → example → practice
- **Strengths:** efficient for novices; clear what is expected
- **Weaknesses:** can feel passive; doesn't develop autonomous problem-solving
- **Fits:** skill acquisition, exam prep, procedural knowledge, early in a learning sequence
- **Examples:** most textbooks; Khan Academy; classical apprenticeship

### Constructivism (Piaget, Dewey)

Learners build understanding by doing, reflecting, and integrating with prior knowledge.

- **Structure:** activity → reflection → integration
- **Strengths:** deeper understanding; transfers better; more engaging
- **Weaknesses:** slower; can produce misconceptions if not well-scaffolded; requires more facilitator skill
- **Fits:** concepts that resist memorization, complex skills, learners with background
- **Examples:** Montessori, Reggio Emilia, studio-based design education

### Inquiry-based learning

Learning driven by learner's questions, with the teacher facilitating rather than lecturing.

- **Structure:** question → investigation → share findings → refine
- **Strengths:** develops genuine curiosity and meta-skills
- **Weaknesses:** inefficient; risk of wrong conclusions going uncorrected
- **Fits:** research skills, advanced learners, open-ended domains
- **Examples:** problem-based learning in med school; science fair projects

### Socratic method

Teacher guides through questions; learner reasons aloud; misconceptions surface and are examined.

- **Structure:** question → learner answer → follow-up question exposing contradiction → learner refines
- **Strengths:** develops reasoning; reveals misconceptions
- **Weaknesses:** time-intensive; demanding for facilitator
- **Fits:** philosophical or conceptual topics, law school, analytical skills
- **Examples:** Plato's dialogues; law school casebook method

### Apprenticeship / cognitive apprenticeship

Learner observes expert, then does under coaching, then does solo.

- **Structure:** observe → coached practice → independent practice → reflection
- **Strengths:** transfers tacit knowledge; produces expertise
- **Weaknesses:** requires expert access; scale-limited
- **Fits:** crafts, trades, software engineering, creative work
- **Examples:** traditional trades, doctoral supervision, open-source onboarding

### Project-based learning

Learning organized around completing a significant project.

- **Structure:** authentic project → skills learned as needed → deliverable
- **Strengths:** motivating; integrates multiple skills; produces portfolio
- **Weaknesses:** can skip foundational knowledge; assessment harder
- **Fits:** applied fields, capstone work, self-directed learners
- **Examples:** design studios, maker-space education

### Spaced repetition / active recall

Based on cognitive science of memory. Learners practice retrieval at increasing intervals.

- **Structure:** learn → test after an hour → test next day → test in a week → test in a month
- **Strengths:** creates durable memory; efficient use of study time
- **Weaknesses:** tedious; focuses on retention not understanding
- **Fits:** vocabulary, facts, medical students, language learners
- **Examples:** Anki, Duolingo, SuperMemo

### Worked-example based

For novices, studying worked examples beats solving problems. Provide fully-worked examples first; then partial examples with steps to complete; then blank problems.

- **Structure:** fully-worked → faded-worked (some steps removed) → blank problem
- **Strengths:** efficient for novices; lower cognitive load than pure problem-solving
- **Weaknesses:** diminishing returns once expertise develops
- **Fits:** technical skills, physics, math, programming
- **Reference:** Sweller's Cognitive Load Theory; the worked-example effect

### Mastery learning (Bloom)

Learner demonstrates mastery of each concept before moving on. No passing with 70%.

- **Structure:** learn → test → if fail, re-learn differently → re-test → if pass, proceed
- **Strengths:** addresses prerequisites honestly; produces deeper understanding
- **Weaknesses:** time-variable; harder to schedule; needs alternative explanations
- **Fits:** cumulative subjects (math, programming), self-paced contexts
- **Examples:** Bloom's original work; Khan Academy's implementation

### Game-based learning / gamification

Use game elements (challenges, progression, feedback) to structure learning.

- **Structure:** varies; challenges with clear feedback, usually
- **Strengths:** motivating; repeated practice without fatigue
- **Weaknesses:** extrinsic motivation can displace intrinsic; often more fun than educational
- **Fits:** skill acquisition with many repetitions, learners who need novel motivation
- **Examples:** Duolingo, Brilliant, Khan Academy streaks

### Explorable explanations (Victor, Case)

Interactive essays where the learner plays with the phenomenon before/during explanation.

- **Structure:** play → observe → explain → play more with informed perspective
- **Strengths:** builds intuition powerfully; high engagement
- **Weaknesses:** expensive to produce well; can be shallow if the interaction is thin
- **Fits:** complex systems, intuitions, concept-heavy material
- **Examples:** Nicky Case's *Evolution of Trust*; Ciechanowski essays; Explorable Explanations community

### Case method

Learning through detailed case studies of real or realistic scenarios.

- **Structure:** read case → class discussion → synthesize lessons
- **Strengths:** develops judgment; transfers to novel situations
- **Weaknesses:** indirect; assumes facilitation
- **Fits:** business, law, medicine, ethics, design decisions
- **Examples:** Harvard Business School; law schools; medical education

---

## 2. Cognitive science underpinnings

### Cognitive load theory (Sweller)

Working memory is limited (~4 chunks). Instruction can impose three kinds of load:

- **Intrinsic load** — inherent difficulty of the material
- **Extraneous load** — imposed by poor instructional design (irrelevant details, split attention, redundancy)
- **Germane load** — productive work of schema formation

**Implications for artifacts:**
- Keep extraneous load low (don't decorate teaching visuals)
- Use worked examples early to reduce load during learning
- Integrate text and figures (don't force the learner to bridge)
- Present information in one channel at a time where possible (or in complementary channels deliberately)

### The testing effect

Retrieving information strengthens memory more than restudying it. A single test session after reading is worth more than re-reading.

**Implications:** in teaching artifacts, prediction prompts ("what do you think will happen?"), end-of-section self-checks, and interactive moments that require retrieval outperform passive reveal.

### Spacing effect

Distributed practice produces better long-term retention than massed practice ("cramming").

**Implications:** for longer learning experiences, revisit earlier concepts in new contexts rather than finishing them off once.

### Interleaving

Mixing different topics during practice improves discrimination and transfer.

**Implications:** for multi-concept artifacts, don't put all of topic A together, then all of B. Interleave.

### Desirable difficulty (Bjork)

Learning is enhanced by difficulty that slows immediate performance but improves retention. Too easy → shallow encoding; too hard → frustration and disengagement.

**Implications:** prediction prompts before reveals, active retrieval, spacing, interleaving — all increase desirable difficulty.

### Concrete-Pictorial-Abstract (CPA; Bruner)

Learners benefit from progressing from concrete manipulatives → pictorial representations → abstract symbols.

**Implications:** teach a concept with a concrete example before introducing symbolic notation. The Ciechanowski pattern: the picture, then the equation.

### Zone of Proximal Development (Vygotsky)

Learning happens most effectively at the edge of current ability — challenges slightly beyond what the learner can do alone but within reach with scaffolding.

**Implications:** assess the learner's current state, pitch challenges at a calibrated level, provide scaffolds that fade as ability develops.

### Dual coding theory (Paivio)

Information encoded both verbally and visually is remembered better than either alone.

**Implications:** pair prose and figures deliberately. Don't use figures as decoration; use them as the visual codes of the concepts the prose names.

### Worked-example effect

For novices, studying worked examples beats solving problems. As expertise develops, the balance shifts toward problem-solving ("expertise reversal effect").

**Implications:** calibrate the ratio of worked examples to problems based on the learner's expected level.

---

## 3. Teaching sequences

Named sequences for specific purposes.

### I-Do / We-Do / You-Do

1. **I-Do** — teacher demonstrates fully
2. **We-Do** — teacher and learner do together
3. **You-Do** — learner does alone

Simple and powerful. Works for almost any procedural skill.

### 5E Model

1. **Engage** — hook the learner
2. **Explore** — learner investigates with minimal direction
3. **Explain** — introduce concepts and vocabulary
4. **Elaborate** — extend to new contexts
5. **Evaluate** — assess understanding

Science education; widely used.

### Madeline Hunter's 7-step

1. Objective
2. Anticipatory set (hook)
3. Input (teaching)
4. Modeling
5. Checking for understanding
6. Guided practice
7. Independent practice

### Prime–Show–Explain–Invite (explainer pattern)

Documented in `references/educational-scaffold.md`. A compact four-step:
1. **Prime** — hook attention, frame the question
2. **Show** — display the phenomenon before naming it
3. **Explain** — introduce the vocabulary for what was just seen
4. **Invite** — let the learner play with it

Fits short teaching artifacts (explorable explanations, data journalism).

### Bloom's Taxonomy (revised)

Six levels of cognitive engagement, ascending:
1. Remember
2. Understand
3. Apply
4. Analyze
5. Evaluate
6. Create

**Implications:** design assessments across levels. Most teaching artifacts plateau at Understand; apex work often asks for Evaluate or Create.

### Andragogy (Knowles; adult learning)

Adults learn best when:
- They see relevance
- They can apply immediately
- They draw on existing experience
- They are self-directed
- They encounter problems, not topics

**Implications:** for adult audiences, lead with relevance and problems; let self-direction shape pacing.

---

## 4. Modalities

Different sensory / representational channels.

- **Verbal** — spoken or written language
- **Visual** — diagrams, illustrations, photographs, charts
- **Kinesthetic / manipulative** — physical or simulated manipulation
- **Auditory (sound)** — music, sonification, voice
- **Interactive** — actions with feedback

Apex teaching artifacts typically deploy at least 2-3 modalities together. Dual coding theory suggests visual + verbal is particularly effective.

---

## 5. Assessment patterns

What does the artifact ask of the learner to check understanding?

- **Prediction** — "what do you think will happen when X?" Reveals mental models.
- **Multiple choice** — quick check; limited depth.
- **Apply to a new case** — transfer test. Strongest signal.
- **Explain in your own words** — forces articulation.
- **Find the bug** — analytical skill, forces engagement with code/math/argument.
- **Design / construct** — highest Bloom level.
- **Self-check** — learner reflects on what's clear vs. unclear.

Apex teaching artifacts often integrate the assessment into the experience rather than appending a quiz.

---

## 6. Common failures in teaching artifacts

- **Dumping content.** The artifact says everything; the reader retains nothing.
- **Single-modality saturation.** All prose, or all video, or all diagrams. Dual coding is ignored.
- **No active engagement.** The reader only reads. No prediction, no retrieval, no application.
- **No misconception addressing.** Common wrong beliefs go unacknowledged.
- **Notational overload.** Introducing too many symbols before grounding them.
- **Over-prerequisiting.** Demanding too much background without signaling it.
- **Under-prerequisiting.** Assuming no background when some is actually needed, patronizing the learner.
- **Scaffolding that never fades.** Hints always present; learner never tested without them.
- **Assessment tacked on.** Quiz at the end of a lecture-style dump.

---

## 7. Teaching at different scales

### Micro (single concept, 1-5 minutes)

- Prime → Show → Explain → Invite pattern
- One new term max
- One interactive moment
- One takeaway

### Mini (topic, 10-30 minutes)

- Multiple concepts introduced sequentially
- Structured disclosure (collapsible depth)
- Prediction prompts between sections
- Concluding synthesis

### Full (course, hours-days)

- Arc across multiple concepts
- Interleaving between sub-topics
- Mastery checkpoints
- Capstone application

### Ongoing (curriculum, weeks-months)

- Spaced review of prior material
- Increasing abstraction and challenge
- Explicit meta-cognitive development
- Portfolio of produced work

---

## 10. Science and medicine education traditions

Science and medicine have developed pedagogical traditions specific to their domains — case-based reasoning, simulation, item-writing, spaced repetition for vocabulary-heavy fields. Apex educational artifacts in these domains usually draw from these traditions deliberately.

### Medical case method

The dominant teaching tradition in clinical medicine: a structured clinical scenario presented to learners, who reason through it under guidance.

**Standard structure (seven sections):**
1. **HPI (History of Present Illness)** — the presenting complaint, the timeline, the relevant positives and negatives. Written in the patient's voice as much as possible.
2. **PMH (Past Medical History)** — prior conditions, surgeries, medications, allergies, social history.
3. **PE (Physical Examination)** — observed findings, by system. Quantitative where applicable (BP, HR, RR, T).
4. **Labs and imaging** — results, often with reference ranges. Sometimes intentionally incomplete (the learner asks for them).
5. **Differential diagnosis** — the learner generates the differential before being told the diagnosis. Apex pedagogy delays the answer.
6. **Workup and management** — what tests would distinguish the differentials; what treatments are indicated.
7. **Teaching points** — the case's *pedagogical payload*. Two or three; not a comprehensive review.

The case is the artifact; the teaching points are its argument. *NEJM* Clinical Problem-Solving and *JAMA*'s Clinical Crossroads are the published apex versions.

### Problem-based learning (PBL)

A pedagogical method developed at McMaster Medical School (1969), now used widely in medical and other professional education.

**Structure:**
- Small-group (6–8 learners) tutorial format
- Tutor as facilitator, not lecturer
- Each session begins with a case (a "trigger" — sometimes a paragraph, sometimes a video, sometimes a simulated patient)
- Learners identify what they need to learn ("learning issues") to understand the case
- Self-directed study between sessions
- Next session: learners report back, integrate, refine the case understanding
- Cases span a 1–4 week arc, ending with synthesis

PBL emphasises *self-direction* and *integration* over content-delivery. The trade-off is breadth: a PBL-only curriculum can produce gaps in topics not covered by chosen cases.

### OSCE (Objective Structured Clinical Examination)

A standardised clinical-skills assessment format. Multiple short stations (5–15 minutes each), each with a specific clinical task.

**Bundle structure (four documents per station):**
1. **Candidate brief** — what the candidate sees on the station door: the scenario, the task, the time limit.
2. **Standardised-patient script** — what the simulated patient says and does; includes their backstory, their answers to specific questions, their emotional cues.
3. **Examiner checklist** — observable behaviours, scored. Each behaviour worth a defined number of points.
4. **Global rating scale** — examiner's overall judgment, usually 1–5 or 1–7. Mitigates the limits of pure checklist scoring.

OSCE is the dominant clinical-skills assessment worldwide. Designing a good OSCE station is a craft — see Harden's original (1975) work and the Medical Council of Canada's guides.

### NBME-style item-writing

The National Board of Medical Examiners' conventions for multiple-choice clinical questions. The "USMLE-style item" is the dominant exam format.

**Conventions:**
- **Clinical vignette stem.** A short patient story (age, sex, presentation, exam, labs) — typically 80–150 words. The vignette is *medically realistic*, not just an exam artefact.
- **Lead-in question** — the specific question being asked: *"Which of the following is the most likely diagnosis?"*, *"What is the next best step in management?"*, *"Which of the following is the underlying mechanism?"*
- **Four to five options**, only one of which is correct. The distractors are *plausible* — wrong for specific, learnable reasons.
- **One best answer.** Not "all of the above"; not multiple correct.
- **Avoids cluing.** No grammatical mismatches between stem and options that hint at the answer; no length cues (the correct option not consistently longer or shorter than distractors).

Good item-writing is rare and learnable. See Case and Swanson's *Constructing Written Test Questions for the Basic and Clinical Sciences* (NBME, 2002) — the canonical guide.

### Spaced repetition card design (Wozniak's 20 rules)

Piotr Wozniak (creator of SuperMemo) published in 1999 his "20 rules of formulating knowledge in learning." Adopted across the spaced-repetition community (Anki, RemNote, Mochi).

The most-cited rules:

1. **Do not learn if you do not understand.** Memorising unintegrated facts is fragile and frustrating.
2. **Build upon the basics.** Foundational concepts before details.
3. **Minimum information principle.** Each card tests *one* thing. *"What is the capital of France?"* / *"Paris."* — not a multi-part card.
4. **Cloze deletion is fine.** *"The capital of France is [...]"* with the answer revealed is structurally equivalent to a question-answer card.
5. **Use imagery.** Image occlusion (the visual equivalent of cloze) is powerful for anatomy, geography, chemistry.
6. **Use mnemonics.** Especially for arbitrary associations (drug-mechanism pairings, anatomical landmark sequences).
7. **Personalise.** A card meaningful to the learner is remembered better than a generic one.
8. **Refer to other memories.** Cards that connect to existing knowledge are remembered better.

The cards are the artifact; the *system* (Anki, SuperMemo) handles the spacing. Apex spaced-repetition decks for medicine (e.g., AnKing for USMLE Step 1) embody these rules; bad decks violate them by cramming multiple facts into single cards.

### Worked-example → faded → blank-problem progression

The pedagogical sequence underpinning much of contemporary STEM education, especially in mathematics and physics. Builds on Sweller's Cognitive Load Theory and the worked-example effect.

**Sequence:**
1. **Fully-worked example.** All steps shown, with annotations explaining *why* each step is taken. Catrambone's sub-goal labels appear at each step (*"Goal 1: isolate the variable term"*).
2. **Faded example.** The last step is removed; the learner completes it. On the next problem, the last two steps removed. Then three.
3. **Blank problem.** No steps shown; the learner solves entirely.

Each transition is a calibrated reduction in scaffolding. Worked examples are *not* a substitute for practice; they are a preparation for it. The expertise-reversal effect (Kalyuga, Sweller) tells us that as learners gain expertise, the value of worked examples decreases — and forced worked examples for advanced learners can actively interfere with learning. The artifact must adapt; the progression is part of the design.

Augmenting the sequence with **self-explanation prompts** (*"Why did we divide both sides by 3?"*) and **sub-goal labels** improves transfer significantly (Catrambone, 1998; Renkl, 1997).

### NGSS 3-Dimensional Learning

The Next Generation Science Standards (US, 2013) define science teaching as the integration of three dimensions:

1. **Science and Engineering Practices** — the activities of doing science (asking questions, developing models, analysing data, constructing explanations).
2. **Crosscutting Concepts** — patterns that recur across science (patterns, cause and effect, scale, systems, energy and matter, structure and function, stability and change).
3. **Disciplinary Core Ideas** — the content of physics, life science, earth science, engineering.

Apex K-12 science artifacts intersect all three dimensions; a lesson that is purely content (DCI) without practices or crosscutting concepts is incomplete by NGSS standards.

### Singapore math (Concrete-Pictorial-Abstract)

The pedagogical sequence dominant in Singapore's mathematics curriculum (and adopted internationally as "Singapore Math").

**Sequence:**
1. **Concrete** — physical manipulatives (counters, blocks, base-ten rods). The learner *handles* the concept.
2. **Pictorial** — drawings of the manipulatives, then bar models and other diagrammatic representations. The learner *sees* the concept.
3. **Abstract** — symbolic notation. The learner *writes* the concept.

Each stage is *bridged* into the next: the bar model is drawn over the manipulative; the equation is written under the bar model. The transitions matter as much as the stages.

Bruner's original Concrete-Pictorial-Abstract (CPA) framework underpins both Singapore Math and much contemporary mathematics-education research. See `taste-calibration.md` Appendix C for the worked-example sequence applied across tiers.

### The Feynman technique

A self-directed learning method named for Richard Feynman, who attributed it to his learning style.

**Steps:**
1. **Choose a concept.** Write it at the top of a page.
2. **Explain it as if teaching a child.** Write the explanation in plain language, no jargon.
3. **Identify gaps.** Where the explanation falters or relies on undefined terms, the learner does not yet understand.
4. **Return to source material.** Re-learn the gap; return to step 2.

The technique is at its core a *self-explanation* exercise (per the cognitive-science literature). Apex educational artifacts often build a Feynman moment into their structure — see `taste-calibration.md` Appendix C's tier-9 example.

### Cornell notes

A note-taking system developed at Cornell University in the 1950s, still widely taught.

**Page structure:**
- **Right column** (~70% of width) — primary notes during lecture/reading
- **Left column** (~25% of width, called the "cue column") — keywords, questions, and prompts written *after* the notes
- **Bottom strip** (~5–10% of height) — summary, written after the notes are reviewed

The structure forces three passes: take notes, generate cues, write summary. Each pass is a different cognitive operation; the cumulative effect is retrieval-friendly notes.

### Retrieval-practice protocols

Cognitive-science research consistently finds that *retrieval* (testing yourself) improves long-term retention more than *re-reading*. Specific protocols:

- **Free recall.** *"Without looking, write everything you remember about X."* The most demanding form.
- **Cued recall.** Question prompts the recall; learner generates the answer.
- **Recognition.** Multiple-choice or "is this true?" — less demanding than recall but still active.
- **Spaced retrieval.** Combine retrieval with spaced repetition; the cumulative effect is the strongest in the literature.

The testing effect (Roediger and Karpicke, 2006) is one of the most-replicated findings in educational psychology. Apex teaching artifacts deploy retrieval, not just exposition.

### Interleaving

Mixing different topics during practice produces better discrimination and transfer than blocked practice (all of topic A, then all of topic B).

**The trade-off:** interleaved practice *feels* worse in the moment (the learner makes more errors) and *is* better for retention. The "desirable difficulty" framework (Bjork) names this counterintuitive effect.

**Application:** in a teaching artifact covering three concepts, interleaved practice problems (A B C A B C A C B) produce better learning than blocked problems (A A A B B B C C C), even when the total problem count is equal.

Apex multi-concept educational artifacts honour interleaving in their problem-set ordering, not just their topic exposition.

### Clinical teaching micro-skills (Neher / Wolpaw / Pangaro)

The bedside, the workroom table, and the clinic doorway run on a different clock from the lecture theatre. The chief-teaching-resident's job — teaching the teachers to teach in two minutes, one-to-one, between patients — has produced its own family of named pedagogical frameworks, distinct from the broader case-method and Socratic traditions covered above.

The four most widely deployed:

- **One-Minute Preceptor** (Neher, Gordon, Meyer, Stevens, *J Am Board Fam Pract* 1992;5:419). Five sequential micro-skills the preceptor walks after a learner case presentation: *get a commitment* → *probe for supporting evidence* → *teach a general rule* → *reinforce what was right* → *correct mistakes*. The most-validated clinical-teaching micro-skill; the canonical artifact of the time-bounded precepting tradition.
- **SNAPPS** (Wolpaw, Wolpaw & Papp, *Acad Med* 2003;78:893). Six *learner-driven* steps: *Summarize* → *Narrow* → *Analyze* → *Probe preceptor* → *Plan* → *Select self-learning issue*. The chief antidote to the preceptor-asks-all-questions anti-pattern. Especially useful with senior learners.
- **RIME** (Pangaro, *Acad Med* 1999;74:1203). Developmental framework — *Reporter* → *Interpreter* → *Manager* → *Educator* — used for narrative resident evaluation and as a self-assessment scaffold. Not a four-point scale; a developmental sequence.
- **Aunt Minnie** (Cunningham, Blatt, Fuller, Weinberger, *Arch Pediatr Adolesc Med* 1999;153:114). Instant pattern-recognition for high-prevalence single-finding presentations, paired with an explicit *escape clause* for when the pattern stops fitting. Pediatrics and dermatology are its natural homes.

Apex deployments preserve the canonical order and refuse to compress steps; weak deployments collapse steps 4 and 5 of 1MP into a single "feedback" beat, treat RIME as a numerical rating, or strip Aunt Minnie's escape clause. See `references/medium-playbooks/clinical-teaching-microskills.md` for the full catalog (14 micro-skills with citation, script template, and 10/10 calibration for each).

### Critical appraisal traditions (Sackett / Guyatt / CASP)

Evidence-based medicine is taught as a discipline distinct from the clinical sciences themselves — a *meta-skill* applied to the literature the clinician encounters. The teaching tradition matured in the 1990s under David Sackett (Oxford, McMaster) and Gordon Guyatt (McMaster, who coined "evidence-based medicine"), and is now standardised across most medical and nursing curricula.

**The taught canon:**

- **PICO question construction.** Population / Intervention / Comparator / Outcome (and sometimes Time and Setting). The discipline that turns a clinical curiosity (*"is this drug any good?"*) into a searchable question (*"in adults with new-onset atrial fibrillation, does apixaban compared to warfarin reduce stroke at 12 months?"*). Without PICO the literature search cannot return useful answers.
- **Matching study type to reporting framework.** Apex critical-appraisal teaching pairs study designs with their canonical reporting frameworks: **CONSORT** for RCTs, **STROBE** for observational studies, **QUADAS-2** for diagnostic accuracy, **PRISMA** for systematic reviews, **SPIRIT** for trial protocols, **STARD** for diagnostic test reporting, **CHEERS** for economic evaluations. The learner who knows the framework can locate what the paper failed to report.
- **Risk-of-bias assessment.** Cochrane's Risk-of-Bias 2 tool (RoB 2) for RCTs; ROBINS-I for non-randomised studies; QUADAS-2 for diagnostic studies; GRADE for the body of evidence. The discipline names *specific* threats to validity rather than diffuse "limitations."
- **Effect-size and confidence-interval discipline over p-value.** The taught reflex is to ignore the headline *p* and read the effect size with its 95% CI. *"Hazard ratio 0.78, 95% CI 0.72–0.85"* is the data; *"p < 0.001"* is a coarse summary that hides whether the effect is clinically meaningful.
- **External-validity discipline.** Did the trial enrol patients like *yours*? The PICO match between the published trial and the clinician's patient is rarely perfect; the teaching tradition demands the gap be named, not glossed.
- **The "Users' Guides to the Medical Literature" canonical structure.** Guyatt et al.'s *JAMA* series (1993–2000), later collected as the JAMA Press textbook. The canonical question sequence for any study: *Are the results valid? What are the results? Will the results help me care for my patient?* This three-part frame survives across study types.

CASP (Critical Appraisal Skills Programme, Oxford) and its UK-government-funded checklists are the dominant teaching tools at the early-trainee level; the *Users' Guides* are the senior-trainee canon. Apex critical-appraisal artifacts pair a worked example with a real paper — the learner appraises the actual *JAMA* or *NEJM* paper, not a constructed teaching abstraction. See `references/medium-playbooks/clinical-teaching-microskills.md` for the precepting frameworks that surround critical-appraisal teaching (RIME-grounded narrative evaluation; SNAPPS for outpatient evidence-application discussions).

### Feedback frameworks (Pendleton / advocacy-inquiry / ALOBA / R2C2)

Feedback in clinical training has its own pedagogical canon, separate from instruction. The frameworks below are *for the post-encounter conversation*; deploying them during patient care (interrupting the procedure to "first tell me what went well") is a category error.

- **Pendleton's rules** (Pendleton, Schofield, Tate, Havelock; *The Consultation*, Oxford 1984). Four turns, in order: *learner names what went well* → *observer names what went well* → *learner names what to do differently* → *observer names what to do differently*. Learner-first on both halves; strengths-before-improvements; behavior-not-trait; typically one strength and one change. The canonical UK GP-training framework.
- **Advocacy-Inquiry** (Rudolph, Simon, Dufresne, Raemer, *Simul Healthc* 2006;1:49). The frame for debriefing: *"I noticed [observable behavior], I'm concerned because [my interpretation], I'm curious — what was going through your mind?"* The pairing of the observer's interpretation with genuine curiosity prevents both the *judgment-without-curiosity* and the *false-neutrality-trap* failure modes.
- **ALOBA** (Kurtz, Silverman, Draper; *Teaching and Learning Communication Skills in Medicine* 2nd ed. 2005). Agenda-Led Outcomes-Based Analysis — the learner sets the agenda; observation focuses on the learner's stated outcomes; feedback is keyed to that agenda; alternative phrasings are *rehearsed*, not merely described. The structural antidote to the trainer-led laundry list.
- **R2C2** (Sargeant, Lockyer, Mann, Holmboe et al., *Acad Med* 2015;90:1698). Four phases for high-stakes feedback: *Rapport* → *Reaction* → *Content* → *Coaching*. Used when feedback may be poorly received (multi-source feedback debrief, remediation, summative review). Skipping to Content before Rapport and Reaction is the canonical failure mode.
- **BARS** (Behavior-Anchored Rating Scales; Smith & Kendall, *J Appl Psychol* 1963). Each rating point is anchored to an observable behavior, not an abstract descriptor. *"5 = consistently elicits patient's understanding of diagnosis using teach-back"* rather than *"5 = excellent communication"*. The discipline that makes inter-rater reliability achievable in clinical-skills assessment.

When to choose which: Pendleton for routine observed-encounter feedback; Advocacy-Inquiry for debriefing (simulation or real); ALOBA for communication-skills group teaching; R2C2 for high-stakes feedback conversations; BARS for the assessment instrument itself. See `references/medium-playbooks/clinical-teaching-microskills.md` for the full scripts and `references/medium-playbooks/assessment-artifact.md` for the assessment-discipline context.

### Debriefing traditions (GAS / PEARLS / 3D Model)

Simulation-based education and post-event team review have produced a distinct family of debriefing frameworks, each calibrated to a different post-event context.

- **GAS** (Steinwachs, *Simul Gaming* 1992;23:186). *Gather* (the team's account) → *Analyze* (against intended performance) → *Summarize* (lessons + specific commitments). The default for routine simulation debriefs; three phases that map cleanly onto a 20-minute structured conversation.
- **PEARLS** (Eppich & Cheng, *Simul Healthc* 2015;10:106). Five phases: *Reactions* → *Description* → *Analysis* (with explicit choice of approach: learner self-assessment, focused facilitation via advocacy-inquiry, or directive feedback) → *Application & Summary*. The framework's contribution is the *blended-approach* analysis phase — the facilitator chooses the analysis mode that fits the moment, rather than committing to one stance for the whole debrief.
- **3D Model** (Zigmont, Kappus, Sudikoff, *Semin Perinatol* 2011;35:52). *Defusing* → *Discovering* → *Deepening*. Used after emotionally-charged events (simulated patient death, traumatic real-case, near-miss) where the team cannot productively analyze before they have *defused*. The sequence is structural — analysis before defusing produces shallow conclusions or defensive withdrawal.

Apex debriefing deployments share four disciplines: the framework is *named to the team* at the debrief's start so the structure is shared; psychological safety is established before content begins (the *Healthcare Simulationist Code of Ethics* is the canonical floor); advocacy-inquiry is used in the analysis phase rather than pure judgment or pure inquiry; and a *specific commitment* — one or two things the team will do differently — closes the debrief. See `references/medium-playbooks/clinical-teaching-microskills.md` for full scripts.

### After-action review (US Army)

The US Department of the Army's *Training Circular 25-20: A Leader's Guide to After-Action Reviews* (1993) defined the five-question structured retrospective that has since been adopted across healthcare quality improvement (IHI, Veterans Health Administration), aviation safety, fire service, and beyond.

**The five questions, in order.**

1. What was supposed to happen?
2. What actually happened?
3. Why was there a difference?
4. What will we do next time?
5. What will we sustain? (What did we do well that we want to keep doing?)

The asymmetry — four failure-oriented questions and one success-oriented question — is structural protection against the meeting becoming a blame inventory. Question 5 is the most-skipped move and the one whose absence converts AAR into a blame retrospective. Maps cleanly to post-call rounds debriefs, code debriefs, and M&M case structure. See `references/medium-playbooks/clinical-teaching-microskills.md` for the full script and anti-patterns.

### Communication-skills frameworks (Calgary-Cambridge / SPIKES / NURSE / Ask-Tell-Ask)

Clinical communication is its own teaching tradition with its own canonical frameworks, deployed in instruction (the encounter as it happens) rather than in feedback (the post-encounter conversation).

- **Calgary-Cambridge** (Kurtz & Silverman, *Med Educ* 1996;30:83; refined Kurtz, Silverman, Benson, Draper, *Acad Med* 2003;78:802). The dominant clinical-encounter map: five horizontal stages (*Initiating session* → *Gathering information* → *Physical exam* → *Explanation and planning* → *Closing session*) crossed with two vertical tasks (*Providing structure*; *Building the relationship*) that run through every horizontal step. The vertical tasks are what most teaching omits.
- **SPIKES** (Baile, Buckman, Lenzi, Glober, Beale, Kudelka, *Oncologist* 2000;5:302). Six-step breaking-bad-news protocol: *Setting* → *Perception* → *Invitation* → *Knowledge* → *Emotion* → *Strategy/Summary*. Cited in essentially every oncology and palliative-care curriculum. Already deployed in `templates/osce-station.md`.
- **NURSE** (Back, Arnold, Tulsky; *Mastering Communication with Seriously Ill Patients*, Cambridge 2009; originated in the Oncotalk curriculum 2002–07). Five named moves for responding to emotion in a clinical conversation: *Name* / *Understand* / *Respect* / *Support* / *Explore*. Deployed as a toolkit (one move, then silence, then listen), not as a sequential checklist.
- **Ask-Tell-Ask** (Back, Arnold, Baile, Tulsky, Fryer-Edwards, *CA Cancer J Clin* 2005;55:164). Information delivery chassis: *ask what the patient knows* → *tell in chunks of plain language* → *ask what they understood* (teach-back, not satisfaction-check). The chassis under SPIKES's K step and under most clinician information-delivery contexts.

These frameworks are integrated in practice — SPIKES deploys NURSE in its E step and Ask-Tell-Ask in its K step; Calgary-Cambridge provides the structural map all three sit inside. VitalTalk's online curriculum is the apex demonstration of integrated deployment. See `references/medium-playbooks/clinical-teaching-microskills.md` for full scripts, citations, and anti-patterns.

### Chalk talks

The chalk talk is a hospital-medicine teaching genre with its own discipline: a board-driven, 5-to-7-minute didactic delivered in the team room between admissions, on the conference whiteboard, or at the bedside chart. The chalk is not metaphorical at its origins — the Yale internal-medicine and Hopkins osler-tradition residencies treated the conference-room blackboard as a load-bearing pedagogical instrument; the digital-era successor (the whiteboard, the iPad whiteboard app) inherits the constraint.

**The Yale Aunt Minnie tradition.** Pattern-recognition chalk talks built around a single high-yield finding: *"a tender, warm, swollen first metatarsophalangeal joint in a 55-year-old man who ate steak last night and drank scotch"* — the chief draws the joint, names the finding, names the diagnosis (gout), names the next test (joint aspiration with polarised microscopy), and names the trap (don't anchor; septic arthritis can look identical). Five minutes; one image; one diagnosis; one next step; one trap. The chalk talk's job is to add one pattern to the team's gestalt library.

**The eraser test.** The chalk talk is *over* when the board is full enough that the next thing erased would matter. Concretely: if the chief has to erase the diagram of the lung to draw the diagram of the bug, the talk is two talks; split it. The eraser is the time-keeper; running it constantly is the marker of a talk that wandered. Apex chalk-talk teachers draw with one third of the board left blank, so the eraser is held in reserve for the final synthesis sketch.

**The 7-min-or-less rule.** Sawyer *et al.* (*Acad Med* 2018;93:1024 and the broader 2016–2020 chalk-talk research cluster) documented that chalk talks longer than seven minutes lose the team — pagers go off, nurses pull residents away, the listener's working memory saturates. Seven minutes is the operational ceiling; five is the apex sweet spot; ten produces a lecture in disguise. Schoolcraft & Schiller's *"How to give a great chalk talk"* (*JGIM* 2019) operationalises the constraint: pick one teaching point, one image, one mnemonic, one trap, one next-step.

**Apex structure.** *Hook* (a case in two sentences: *"forty-year-old woman with progressive dyspnoea and a normal CXR"*) → *frame* (*"three buckets of normal-CXR dyspnoea: cardiac, pulmonary, haematologic"*) → *draw* (the diagram — usually anatomical, often a vessel/airway tree, sometimes a flowchart) → *anchor* (the one fact to take away: *"PE is the can't-miss; CT-PA is the test"*) → *contrast* (one mimic that looks identical and is treated differently). Seven minutes; board half-erased at the end; one trap named; one tomorrow-morning action item.

**Anti-patterns.** *"Let me set the stage…"* (the talk has not started yet at minute two). The board entirely full at minute four (the eraser test fails; the audience is parsing density they cannot encode). Three teaching points (the team retains one; the chief who tries to teach three teaches none well). A chalk talk that becomes a journal-club presentation (different artifact, different time-budget, different rhetorical contract). No image (the chalk was not actually used as chalk; the talk could have been delivered with the board off). See `references/medium-playbooks/clinical-teaching-microskills.md` for adjacent precepting frameworks.

### Intern orientation packets

The intern orientation packet is the artifact that lands in the inbox of every PGY-1 the week before July 1 — the universal start date for US graduate medical education. Its reader is *the most anxious clinician in the building*: a sleep-deprived new graduate who is, that week, about to write their first independent admission orders, take their first solo overnight call, and be paged about their first patient deterioration. The packet's audience is not the GME office, not the residency-review committee, not the institutional risk-management lawyer; the packet's audience is the tired, anxious intern at 11pm the night before orientation, reading on their phone.

**The first-7-days vs first-30-days tier.** Apex packets separate two distinct documents. *The Day-One Survival Sheet* (one to two pages; on the badge, in the white-coat pocket): how to log into Epic, who to call for what, where the call rooms are, where coffee is, the four pagers the intern is responsible for, the three calls every intern dreads and what to do in the first minute of each. *The Month-One Reference* (eight to twenty pages, indexed): the policies the intern needs to know by the end of the first week, the workflows for common admissions, the pharmacy formulary basics, the supervision policy, the duty-hours policy, the chain of command for clinical disagreement. Mixing these is the dominant failure mode — the survival sheet diluted with policy citation; the reference fattened with welcoming prose. The intern at 2am reaches for the survival sheet; the intern on the day-three afternoon reaches for the reference. Both must exist; neither does the other's job.

**The 5-calls-every-intern-dreads pattern.** Wong *et al.* (*Acad Med* 2017) and the broader patient-safety literature converge on the five overnight cross-cover calls that consistently challenge first-year residents: *(1) hypotension in a stable-on-admission patient*; *(2) acute change in mental status*; *(3) chest pain in a non-cardiac admission*; *(4) post-operative oliguria*; *(5) the family member asking what is happening at 3am*. The apex orientation packet covers each in a one-page chassis: *first three actions in the first three minutes*, *one diagnostic frame to apply at the bedside*, *one criterion that triggers calling the senior*, *one phrase to say to the nurse*, *one phrase to say to the family*. The packet is operational; the framing is not *"learn this for the boards"* but *"you will be called about this within the first week, here is what to do."*

**Apex deployment.** The packet's voice is calm, specific, and respectful of the reader's state. The opening is not *"Welcome to the residency!"* but *"You will have a pager and a login by Monday morning. Here is what to do with each."* Page layout is operationally chunked: each topic is one page or one screen; navigation is by tab and by bookmarked PDF; the digital version is searchable. The packet ships with a *physical pocket card* for the most-frequently-used reference (telephone tree, emergency drug doses, the five-calls chassis). ACGME Common Program Requirements (Section VI.E) mandate orientation content; apex packets exceed the mandate by operationalising it for the intern, not for the auditor. See Wong *et al.* (*Acad Med* 2010;85:1425) — *"What the medical interns wished they had known: a needs assessment"* — for the empirical basis; the ABIM Foundation's *Choosing Wisely* resident curricula for an apex example.

**Anti-patterns.** *"Intern orientation packet"* that is fifty pages of policy citation with no operational chassis (the audit-document failure; see F-mode T7). A packet with the duty-hours policy on page 3 but no information about how to call the on-call senior (the wrong things ranked first). Generic *"welcome to medicine!"* prose that consumes the first two pages (the new intern has been a medical student for four years; they are not arriving at the field). Outdated workflow descriptions (the packet was last updated in 2019; the Epic version has changed twice since). See `references/medium-playbooks/clinical-handoff.md` for the I-PASS-derived sign-out chassis that should appear inside the packet.

### Curriculum blueprinting

Curriculum blueprinting is the discipline of designing a course, rotation, or training programme by working backwards from desired competencies through assessments to learning experiences. The dominant frameworks are interlocking rather than competing: each addresses a different stage of the design.

**Kern's six-step model.** Thomas, Kern, Hughes & Chen, *Curriculum Development for Medical Education: A Six-Step Approach* (Johns Hopkins University Press; 1st ed. 1998; 4th ed. 2022; "Kern 2009" cites the 2nd edition that became the de facto standard reference). The six steps, in order:

1. **Problem identification and general needs assessment.** What is the gap between current and desired performance in the field? At what scale (specialty, institution, programme)?
2. **Targeted needs assessment.** What is the gap for *this* learner population at *this* institution? Surveys, focus groups, audit data.
3. **Goals and objectives.** Goals are aspirational; objectives are specific, measurable, achievable, relevant, time-bound (SMART) and written at the cognitive / behavioural / affective level the curriculum targets.
4. **Educational strategies.** Match teaching modality to objective. Procedural skill → simulation; clinical reasoning → case-based learning; foundational science → flipped classroom; team behaviour → in-situ simulation.
5. **Implementation.** Resources, faculty development, scheduling, learner buy-in, leadership support.
6. **Evaluation and feedback.** Of learners (formative + summative) *and* of the curriculum itself (does it achieve its objectives? at what cost? for whom?).

Kern's argument: skipping or compressing any step produces a curriculum that fails predictably. Skipping step 1 produces a course that solves no problem; skipping step 3 produces teaching without targets; skipping step 6 produces a curriculum that cannot improve.

**Backwards design (Wiggins & McTighe).** *Understanding by Design* (ASCD; 1st ed. 1998; expanded 2nd ed. 2005 — the canonical *"Wiggins & McTighe 2005"* reference). Three stages, in reverse:

1. **Identify desired results.** What enduring understandings, essential questions, and discrete knowledge/skills should the learner leave with?
2. **Determine acceptable evidence.** What assessments would demonstrate those results? Performance tasks first; supplementary evidence (quizzes, observations) second. The *"acceptable evidence"* criterion is the discipline: if the assessment cannot demonstrate the desired result, the assessment is not the right assessment.
3. **Plan learning experiences and instruction.** Only now — only after the evidence is specified — does the design proceed to *what the learner will do in class*.

The reverse order is the load-bearing claim. The forward-design failure mode (*"I'll teach what I love and assess what fits at the end"*) produces curricula whose assessments do not measure their objectives; backwards design enforces alignment by construction.

**Bloom's taxonomy mapping.** The revised taxonomy (Anderson & Krathwohl, 2001) maps each curriculum objective to a cognitive level: *Remember*, *Understand*, *Apply*, *Analyse*, *Evaluate*, *Create*. The mapping is operational, not decorative — assessments are written at the level the objective targets. *"List the side effects of ACE inhibitors"* is *Remember*; *"Recommend whether to start an ACE inhibitor in this patient"* is *Apply* or *Evaluate*; the two assessments draw on different cognitive operations and produce different evidence. A curriculum whose objectives are all *Remember* and whose summative assessment requires *Evaluate* is misaligned by construction.

**Kirkpatrick's four levels of evaluation.** *Evaluating Training Programs* (1959 article; 1994 first full book — the standard *"Kirkpatrick 1994"* citation; D. L. Kirkpatrick & J. D. Kirkpatrick 4th ed. 2006). Curriculum evaluation operates at four ascending levels:

1. **Reaction.** Did the learners enjoy/value it? (Course-evaluation surveys.)
2. **Learning.** Did the learners learn it? (Pre/post knowledge tests; OSCE scores.)
3. **Behaviour.** Do the learners *do* it in practice? (Direct observation; chart audit; multi-source feedback.)
4. **Results.** Does it improve patient/organisational outcomes? (Mortality, complications, length of stay, patient experience.)

Most curriculum evaluation stops at level 1; apex evaluation reaches level 3 or 4. The asymmetry is structural — level 4 evidence is expensive, slow, and confounded — but a curriculum that cannot in principle reach level 3 is a curriculum whose value cannot be defended.

**Apex deployment.** The curriculum document opens with Kern step 1 (the problem), proceeds through SMART objectives mapped to Bloom levels (step 3), specifies assessments that produce Kirkpatrick-level-2-or-3 evidence (step 6 feeding back into step 3), and only then lists learning experiences (Wiggins & McTighe's third stage). The faculty-development plan is explicit (Kern step 5). The evaluation plan is funded (Kern step 6; Kirkpatrick level mapping). The blueprint is a table — rows are objectives, columns are *teaching session*, *assessment*, *Bloom level*, *Kirkpatrick level*, *responsible faculty*. The reader who scans the blueprint can see whether the curriculum hangs together; the reader who scans the conference schedule (the most common failure mode) cannot. See F-mode T8 for the failure pattern.

### Goals-of-care conversations as teachable skill

The goals-of-care conversation — the structured discussion in which a clinician helps a seriously-ill patient and family clarify what matters most and align treatment with those values — was for decades treated as a personality trait. The contemporary teaching tradition rejects the trait framing: goals-of-care conversation is a structured skill, learnable, assessable, and improvable through deliberate practice. The two dominant curricula are Ariadne Labs' Serious Illness Care Programme and VitalTalk.

**Ariadne Labs Serious Illness Conversation Guide (SICG).** Bernacki, Block *et al.* (*JAMA Intern Med* 2014;174:1994) reported the cluster-randomised trial that established the SICG's effect: increased goals-of-care conversations, improved documentation, increased patient and family satisfaction, no harm to hope. The guide itself is a one-page structured script with seven elements: *set up the conversation*, *assess illness understanding*, *assess information preferences*, *share prognosis*, *explore key topics* (goals, fears, sources of strength, critical abilities, trade-offs), *close the conversation*, *document*. The guide is *not* a rigid checklist; it is a scaffold that frees clinician working memory to attend to the patient. Apex deployment: the guide is on a laminated pocket card; the clinician glances at it before the conversation and refers to it when stuck; documentation uses the seven elements as headers so the receiving clinician can find the prognosis discussion at a glance.

**VitalTalk.** The web-and-workshop curriculum (vitaltalk.org; Back, Arnold, Tulsky, originated in the Oncotalk programme 2002–2007) trains clinicians in the integrated communication skills that serious-illness conversation requires. The curriculum braids the canonical frameworks already catalogued in this library's §10 (Clinical teaching micro-skills):

- **SPIKES** (Baile *et al.*, *Oncologist* 2000;5:302) as the chassis for breaking bad news, including the prognosis-disclosure step of the SICG.
- **NURSE** (Back, Arnold, Tulsky 2009) — *Name*, *Understand*, *Respect*, *Support*, *Explore* — for responding to emotion when it arises (and it will arise during the SICG's *fears* and *trade-offs* elements).
- **Ask-Tell-Ask** as the information-delivery chassis under every *share* moment.

The braid is the apex move: SPIKES provides the overall encounter scaffold; NURSE supplies the within-encounter response to emotion; Ask-Tell-Ask is the within-information-delivery chassis at every chunked-information moment. A clinician who has internalised one of the three can deliver a competent conversation; a clinician who has internalised all three can deliver a great one.

**Teaching deployment.** Apex curricula in this domain combine three modalities: didactic (read the SICG; watch VitalTalk videos; review the trial evidence), simulation (standardised-patient encounters with structured debrief using PEARLS or Advocacy-Inquiry), and supervised live practice (observed real conversations with after-action review). The deliberate-practice element is structural — Ericsson's expertise-by-deliberate-practice framework applies to communication as it does to procedural skill; one workshop does not produce competence. ACGME milestones in palliative-care fellowship and internal-medicine residency increasingly assess communication using the SICG framework's elements as observable behaviours.

**Anti-patterns.** *"Goals-of-care discussion done"* in the chart without specifying what was discussed (documentation as performance; the receiving clinician cannot use it). The conversation that becomes a code-status monologue (the AHA/AAHPM code-status form is a documentation artifact, not a conversation framework). Skipping the emotion-response phase (clinicians who have learned SPIKES but not NURSE often deliver prognosis cleanly and then leave the room when the patient cries). The conversation deferred until the patient is unable to participate (the SICG's empirical justification: the conversation is most useful when held *before* the crisis, not during it; Bernacki & Block, *JAMA Intern Med* 2014;174:1994 on timing).

### Quality improvement as a teaching modality

Quality improvement (QI) is taught — increasingly — as the dominant *project-based learning* modality in graduate medical education. The contrast with traditional research training is structural: traditional research training produces a hypothesis-tested manuscript; QI training produces a *change in the local system* with measured before-and-after performance. Both are valuable; they teach different things. ACGME Common Program Requirements now mandate every resident in every specialty lead or substantively contribute to at least one QI project before graduation.

**The taught QI canon.**

- **The Institute for Healthcare Improvement (IHI) Model for Improvement.** Langley, Nolan *et al.*, *The Improvement Guide* (1996; 2nd ed. 2009). Three questions — *What are we trying to accomplish?*, *How will we know that a change is an improvement?*, *What changes can we make that will result in improvement?* — combined with the PDSA (Plan-Do-Study-Act) iterative cycle. The IHI Open School online curriculum (free for residents and students) operationalises the framework as a 13-course sequence with certificates; programmes increasingly require completion as an orientation activity.
- **The ACGME QI Curriculum (Sponsored by IHI).** A structured curriculum mapped to the ACGME Practice-Based Learning & Improvement and Systems-Based Practice core competencies; modules cover problem identification, measurement, intervention design, run charts, and the SQUIRE 2.0 reporting framework (Ogrinc *et al.* 2015) for QI publication.

**Boonyasai *et al.*** (*JAMA* 2007;298:1023) — *"Effectiveness of teaching quality improvement to clinicians: a systematic review"* — synthesised the evidence base: QI curricula reliably improve learner knowledge and confidence; effects on system-level outcomes are less consistent and depend heavily on faculty mentorship and institutional support. Wong *et al.* (*Acad Med* 2010;85:1425) — *"Faculty-resident 'co-learning': a longitudinal exploration of an innovative model for faculty development in quality improvement"* — established the apex teaching model: faculty and residents learn together, working on a real institutional problem, with formal QI curriculum running parallel to the project.

**Apex deployment.** The resident's QI project is *not* a chart-audit exercise; it is a longitudinal, faculty-mentored, institution-relevant change effort. The project has a charter (problem, aim, measures, team, sponsor); the aim is SMART (*"reduce 30-day readmission after CHF discharge from 22% to 15% by June 2027"*, not *"improve discharge"*); the measures are split between outcome (the SMART target), process (the changes being tested), and balancing (what might worsen as the outcome improves); the PDSA cycles are documented; the run chart is the primary visualisation; the writeup follows SQUIRE 2.0. The artifact is the *change*, not the *paper* — but the SQUIRE-formatted writeup is what allows other institutions to learn from the work.

**Anti-patterns.** The chart-audit-as-QI-project (no intervention, no PDSA, no measurement of change; the project is a baseline measurement misnamed). The QI project without a sponsor (no institutional traction; the project ends at the resident's graduation). The run chart with three data points (the QI-statistics convention is a minimum of 12 baseline points; fewer cannot distinguish signal from noise). The intervention chosen before the problem is measured (the *solution-in-search-of-a-problem* failure mode). See `references/libraries/medical-artifacts.md` § Quality improvement and the SQUIRE 2.0 framework for the operational detail.

---

## 8. Cross-references

- `references/educational-scaffold.md` — operational pattern for short teaching artifacts
- `references/libraries/reader-models.md` — learner audience modeling
- `references/libraries/rhetorical-atlas.md` — structural choices for educational content

---

## 9. Extending this library

Add a pedagogical tradition or finding when:
- It has a substantive body of work behind it
- It is distinct from traditions already covered
- It has implications for artifact design

Avoid:
- Proprietary methodologies without evidence
- Fads without cognitive-science grounding

<!-- END: references/libraries/pedagogy-library.md -->

---


<!-- BEGIN: references/libraries/reader-models.md -->

# Reader Models

A platter, not a persona menu. The examples below are illustrative — dozens of possibilities drawn from a much larger space. When cold-reading an artifact, invent the persona the artifact needs, informed by the theory and the examples here, rather than picking from a fixed shortlist.

> See `references/how-to-use-this-system.md` for the platter principle.

---

## 1. Theory of audience modeling

Designing for a reader requires modeling one. A vague "the reader" produces vague outputs. A specific, named, multidimensional reader produces specific, landable outputs.

### The dimensions that matter

- **Expertise** — layperson, adjacent practitioner, specialist, deep expert. Determines jargon, definition density, assumed prior knowledge.
- **Context of arrival** — how they encountered the artifact (shared link, search result, internal doc, required reading, curious browse). Determines expectations and patience.
- **Device** — phone (subway), laptop (desk), tablet (couch), large display (conference), audio (driving). Determines interaction affordances and information density.
- **Time budget** — 10 seconds, 2 minutes, 20 minutes, an afternoon. Determines whether you're writing for scan, skim, or depth.
- **Mood** — rushed, curious, skeptical, bored, tired, alert. Determines voice and pacing.
- **Goal** — want a number, want a concept, want a decision, want entertainment, want to dismiss the topic, want to be convinced. Determines what success looks like for them.
- **Prior relationship** — never heard of this, heard once, mild interest, strong interest, existing expert in the subject. Determines how much setup you need.
- **Emotional state** — worried, hopeful, neutral, hostile, grieving, celebrating. Rarely foregrounded but often relevant.
- **Trust posture** — default-trusting, default-skeptical, default-hostile. Determines how much evidence you need to foreground.
- **Socio-cultural context** — language fluency, generational vocabulary, cultural references they carry or don't. Determines allusions and metaphors.

### The triangulation method

A well-designed artifact usually imagines **three readers**:
1. **The primary** — the single most important reader profile. Design the main path for them.
2. **The skimmer** — someone with less time, less interest. Design the skim path for them.
3. **The specialist** — someone who wants more depth than the primary. Provide progressive disclosure for them.

Apex artifacts serve all three through layered design, not by splitting into separate artifacts.

---

## 2. Persona examples

A spread of examples across domains, contexts, and sophistication levels. **Not a list to pick from.** A sense of the space.

### Technical / engineering

**Priya** — senior infrastructure engineer, 10 years experience. Deep expertise in distributed systems. Got the link from a peer in Slack with "interesting." Reading on a 27" monitor at her desk. 15 minutes before a meeting. Wants: a substantive technical claim, and methodology she can evaluate. Default-skeptical of hot takes; respects careful work.

**Marco** — junior iOS engineer, 2 years in. Found this via his team's internal docs as required reading. On a MacBook. 25 minutes. Wants: to understand the topic well enough to participate in the upcoming design review. Lacks context on some acronyms but won't admit it in the meeting.

**Dana** — SRE lead, mixed expertise (deep on Linux, light on ML). Linked from a conference talk thread. On a phone during lunch. 5 minutes. Wants: to decide if it's worth bookmarking for deeper reading later.

**Tess** — data scientist, early career. Reading on her laptop at a coffee shop. Skimmed first, now reading properly. Wants to understand a technique well enough to apply it. Has the time; has the patience.

**Jakob** — staff engineer, skeptical-by-training. Found the artifact in a roundup newsletter. Reading quickly to decide whether it's worth the full read. Will close tab in < 30 seconds if the claim doesn't hold up.

### Product / design

**Nadia** — senior product manager, seven years SaaS. Received the link in email from a peer with subject "thought you'd find this interesting." Reading on MacBook, waiting for a meeting. 8 minutes. Wants: to decide if this idea belongs in her roadmap discussion.

**Alex** — design lead at a consumer startup. Found this via the design Twitter/Mastodon community. Reading on iPad on the couch. 20 minutes. Wants: inspiration and craft examples.

**Jordan** — founder, two-person company. Reading on phone between meetings. 2 minutes. Wants: actionable tactics, not philosophy.

**Mei** — director of product, enterprise. Forwarded by a VP with "thoughts?" On laptop. 10 minutes. Wants: to form an opinion she can articulate back, and to assess the artifact's rigor.

### Executive / decision-maker

**Sandeep** — VP of engineering, 300-person org. Has 3 minutes. Wants: the top-line finding and one piece of evidence. Will not read long-form; will read headlines, charts, and the executive summary.

**Elena** — CFO. Reading a report forwarded by the CEO. Wants: implications for next quarter, and how confident the findings are. Will not evaluate methodology herself but cares whether methodology is visible.

**Morgan** — founder-CEO. Skimming on a plane. 15 minutes. Wants: strategic takeaways and uncomfortable questions.

### Academic / research

**Dr. Park** — tenured professor, computer science. Encountered this via a colleague's reference. 45 minutes. Wants: rigor, citations, and either a novel contribution or a clean synthesis. Will dismiss work that oversimplifies or overclaims.

**Valentina** — PhD candidate, biology. Reading this to orient herself to an adjacent field for her thesis committee. 1 hour. Wants: correct use of terminology, good references, and an overview she can reason with.

**Theo** — postdoc, economics. Reading on a Sunday for personal interest. 30 minutes. Wants: a well-crafted argument; is forgiving of pop register if the ideas land.

### Journalistic / editorial

**Aria** — journalist for a major publication, beat: tech & society. Reading to decide if there's a story here. 15 minutes. Wants: a counter-intuitive finding, a quotable expert, and a credible source. Deadline today.

**Ben** — newsletter writer, ~5k subscribers. Reading for material. 10 minutes. Wants: a useful anecdote, a framing he can borrow, or a data point worth citing.

**Riya** — magazine editor, commissioning features. Reading a pitch-adjacent piece. 8 minutes. Wants: to decide if the underlying idea is an assignment-worthy story.

### Consumer / general public

**Tom** — software user, not a software builder. 50 years old. Reading about a product's pricing change. 4 minutes. Wants: to know whether to switch or stay, and whether the justification is honest.

**Kira** — 22, undergraduate, history major. Clicked a link friend shared on Discord. 3 minutes. Wants: to understand the basic shape of the story. Will tune out past the first technical term.

**Retired couple** — reading together on an iPad. 10 minutes. Wants: to understand what's happening in their investment portfolio. Deep expertise in other domains; new to this one.

**Anonymous person on a phone on a subway** — 30 seconds of attention, bumpy reading conditions, small screen, casual mood. Wants: the one thing worth knowing.

### Healthcare / medical

**Dr. Patel** — pediatric cardiologist, 20 years clinical experience. Reading an explainer about a new imaging technique. 15 minutes over coffee. Wants: mechanism, evidence of efficacy, and the limitation he'll need to explain to patients.

**Nurse practitioner** — urgent care, 10 years. Reading on phone between patients. 2 minutes. Wants: a practical update she can apply this shift.

**Patient** — recent diagnosis, no medical background. Reading on a tablet at home. 30 minutes. Wants: to understand her condition well enough to ask informed questions at her next appointment. Anxious; appreciates honesty.

**Medical student** — pre-clinical. Reading on laptop. 45 minutes. Wants: concepts she can retain for board exams, ideally through interactive or visual explanation.

### Financial

**Institutional trader** — 15 years, options desk. Reading a market analysis on a Bloomberg-adjacent site. 4 minutes. Wants: a thesis he can act on by 9:30.

**Personal finance beginner** — 28, first full-time job. Reading a guide to retirement accounts. 20 minutes. Wants: a clear mental model and first-step actions. Overwhelmed by jargon.

**CFO** — small-cap public company. Reading a benchmarking report. 25 minutes. Wants: peer comparisons and acknowledgment of company-specific context.

### Scientific public communication

**Pop-science reader** — 40s, educated, not a specialist. Reading an explainer on black holes or climate or vaccines. 15 minutes. Wants: the ideas, no equations, specific examples. Appreciates analogies as long as they're honest.

**High school student** — researching for a report. 20 minutes. Wants: facts she can cite, ideally with sources.

**Amateur enthusiast** — retired engineer, hobby interest in astronomy. 45 minutes. Wants: depth beyond pop-science, but not journal-paper dense.

### Government / policy

**Policy analyst** — state legislature staffer. Reading a brief. 15 minutes. Wants: the findings, the methodology in broad strokes, and the policy-actionable recommendations.

**Agency director** — federal. 10 minutes over morning coffee. Wants: implications for her agency and confidence level.

**Advocacy organizer** — 25, nonprofit. Reading to prepare testimony. 30 minutes. Wants: evidence she can quote and statistics she can cite.

### Non-native English speakers

**Reader whose first language is Japanese** — professionally fluent in English but prefers shorter sentences and fewer idioms. Reading a technical article. Appreciates plain syntax and clear logical structure over stylistic flair.

**EU reader with English as working language** — fluent, comfortable with idiom. Appreciates American or British register depending on context. Potentially sensitive to metric vs. imperial units.

### Neurodivergent readers

**Idris** — 31, marketing manager with ADHD diagnosed in his late twenties. Three tabs open, Slack pinging, dog at the door. Reading a vendor evaluation doc his director forwarded. Will read in fragments across the day; will not read top-to-bottom in one sitting. Wants: aggressive headings (one per screen), bullet density rather than paragraph density, scannable structure that admits skipping, and a *re-entry path* on every screen so he can resume after interruption without re-reading. A TL;DR that survives standalone. No "as discussed above" — that punishes the reader who arrived sideways.

**Mira** — 29, software engineer, dyslexic since childhood; runs a dyslexia-friendly font system-wide and prefers reading in dark mode. Reading internal RFCs all day. Wants: short sentences, sans-serif body (not italic for long stretches — italic destroys her parsing), line-height 1.6 or higher, generous letter spacing, and paragraphs short enough that the eye does not lose the line. Justified text is hostile. Code blocks are easier than prose because they are spatial. Diagrams that *replace* prose are gifts; diagrams that supplement prose she has already had to read twice are not.

**Theo** — 38, archivist at a university special-collections library. Autistic; reads technical and policy material literally. Reading a vendor contract for a digital preservation system. Wants: unambiguous terminology declared once and used consistently — no synonym variation for stylistic relief. Literal language over metaphor. Explicit logical connectives ("therefore," "because," "if X then Y") rather than implied causation. Honest scope statements at the top — "this document covers A and B; it does not cover C." Hedge words ("usually," "typically," "in most cases") flagged with the conditions under which they don't hold.

### Very young readers (under 8)

**Ada** — 6, reads at picture-book level; reading the page with her parent, who is reading aloud while Ada points at things. Attention is roughly three minutes per spread. Wants: one idea per page, bold pictograms that name the thing depicted, large type (24pt+), concrete nouns ("the dog," "the cup") not categories ("the pet," "the container"). No metaphor — metaphor lands as confusion at this age. The pointing-finger interaction is primary; the page must *survive* and *reward* being pointed at. Color used to distinguish things, not to decorate them.

**Luca** — 10, fluent chapter-book reader; researching planets for a school project, self-directed at a tablet. 25 minutes of attention if the material earns it. Wants: factual claims to cite their source so he can mention it ("according to NASA…"); at most one new word per paragraph with a definition close by; a pronunciation guide for any name he might say aloud in class; a clearly marked "what to remember" box at the end of each section so he knows what made it into the report. Pictures keyed to the text — captions that say *what* the picture shows, not what to feel about it.

### Very old readers (low-vision + cognitive change)

**Margaret** — 82, widowed three weeks ago, working through the estate-settlement portal on an iPad she holds close. Cataracts, slowed cognitive pace, exhausted. Wants: 18pt+ body type, high contrast (no gray-on-gray), short *numbered* steps with one action per step, every step survivable as a stopping point. A "save and come back" path she trusts. Crucially: a phone-and-human escape hatch on every screen — a number she can call, with a name and weekday hours, large enough to read without zoom. Modal dialogs are villains; auto-logout timers are cruelty.

**Henry** — 78, retired electrical engineer, sharp but low-vision; runs the browser at 200% zoom. Reading a technical article about home solar. Wants: layouts that reflow gracefully at 200% — no horizontal scroll, no tap targets that fall off the screen, no overlapping fixed headers eating the viewport. Type that survives resize (em-based, not pixel-based). Tables that wrap into stacked cards on narrow viewports rather than scrolling sideways. Keyboard navigation that works because his hands are steadier than his eyes.

### Non-Western reading orders & RTL / vertical scripts

**Amal** — Arabic-fluent UX designer in Dubai reading a localized analytics dashboard. Reads right-to-left. Wants: mirrored layout (sidebar on the right, primary column on the left, chart axes flipped), numerals in Arabic-Indic or Eastern Arabic conventions depending on locale, and *no directional bias* in iconography — arrows must flip with the layout, "back" and "forward" reverse, progress bars fill leftward. Iconography that hard-codes Western direction (a "send" paper-plane angled to the upper-right) reads broken.

**Hiroshi** — Japanese literature professor reading a long-form essay that mixes traditional vertical and modern horizontal layouts. Wants: vertical (tategaki) layout for traditional prose, horizontal (yokogaki) for technical sections — the *switch itself* is a register signal. Line-breaking respects character boundaries (kinsoku shori); ruby annotation (furigana) is generously interlined for less-common kanji. Generous interline spacing so vertical reading does not collapse columns. Fonts that render mixed JIS-kana and Latin without baseline disagreement.

**Aanya** — 19, Hindi-medium science student reading a physics explainer in Devanagari. Wants: typography that respects the shirorekha (the horizontal line that joins characters) and renders conjuncts (yuktākṣara) correctly — many webfonts butcher both. Line-height tuned for Devanagari's vertical extent including ascenders for diacritics. Numerals in either Devanagari or Hindu-Arabic depending on context, but consistent within a section. Embedded English technical terms set in a Latin face that pairs in weight and color, not just dropped in.

### Low-literacy and second-language readers

**Adult applying for benefits** — 36, reads English at roughly fourth-grade level; reading an eligibility flyer for a state nutrition program. High motivation, low patience for being made to feel stupid. Wants: short sentences (target average 12 words), active voice ("Send the form" not "The form should be submitted"), common Anglo-Saxon vocabulary ("help" not "assistance," "ask" not "inquire," "use" not "utilize"), and pictograms supporting each step. Forms-of-address respectful and direct. No idiom — "ballpark figure," "down the line," "get the ball rolling" are barriers, not warmth.

**Yuki** — 41, civil engineer from Osaka, professionally fluent in English, translating an EPA technical specification for her team. Wants: idiom-free prose, consistent terminology with no synonym-swap (if it's "discharge" in §1, don't call it "effluent" in §2 and "outflow" in §3 — that costs her thirty seconds and a dictionary check each time), a glossary in the back, metric units alongside imperial, dates spelled out (March 4, 2026, not 3/4/26 which is locale-ambiguous), and clear logical scaffolding so she can translate structure before vocabulary.

### Screen-reader-primary readers (first-class persona, not edge case)

**Aaron** — 34, blind from birth, accessibility consultant, NVDA at roughly 1.5× speed; reads more web content in a day than most sighted people read in a week. Reading a data-rich analytics artifact a client built. Wants: a meaningful heading outline (H1 → H2 → H3 with no skipped levels) he can navigate by; chart equivalents as accessible tables (or sonification, but he'll settle for a good table); live regions that announce state changes; landmark roles (`<nav>`, `<main>`, `<aside>`) so he can jump between regions; skip links that actually skip; ARIA used conservatively rather than enthusiastically. He will recognize a sighted designer's first attempt at accessibility within ten seconds, and he is patient with it but unimpressed.

**Sofia** — 56, recently lost most of her vision to diabetic retinopathy; in week ten of NVDA training. Reading a long-form essay her daughter sent. Wants: ARIA used *conservatively* — overzealous `aria-label` that contradicts visible text confuses her, because she is still cross-referencing what NVDA reads against what her remaining vision can resolve. Progressive disclosure (`<details>`, accordions) must announce its state cleanly ("collapsed, button" / "expanded, button"). Decorative elements correctly marked `aria-hidden`. She is not looking for accessibility theater; she is looking for an artifact that survives being read by a reasonable screen reader without surprises.

### Healthcare / clinical contexts (additional)

**Caregiver at 3am** — 34, mother of a febrile toddler, on her phone in the kitchen, googling "fever 103 toddler." Anxious, mobile-first, ten seconds of patience before she calls the on-call line. Wants: action-orientation in the first viewport ("If your child has any of these, call now"), a red-flag panel that is the *most prominent thing on the page*, dosage tables in the units printed on the bottle (mL not mg/kg unless the bottle gives mg/kg), and *no* "consult your doctor" hedging where specific guidance is possible. Trust signals visible: institutional source, date last reviewed.

**Recently-diagnosed adult** — 47, just received a diagnosis of stage-II non-Hodgkin lymphoma; researching prognosis. Wants: calibrated tone — neither false hope ("you've got this!") nor doom ("five-year survival is grim"). Evidence-grade visible (this is from a 2023 meta-analysis; this is expert opinion). Uncertainty honest: confidence intervals shown, not just point estimates; the fact that "prognosis depends on subtype and stage" stated *before* numbers, not after. Glossary on hover, not in a separate document. A clear distinction between "what the average outcome is" and "what your outcome is likely to be" — they are not the same.

**Elderly patient + adult-child translator** — Bao (76, Mandarin-dominant, low vision) and her son Kevin (44, bilingual, in the room translating). The artifact must serve a *dual audience*: large type and clear visual structure for Bao; precise enough that Kevin's translation does not drift; both must be able to follow. Wants: bilingual layout where possible (Mandarin and English side-by-side, not toggled), pictograms doing the heavy work of explanation, written *and* spoken-form numerals (the Mandarin spoken number for 8 is different from how a translator might write it), and instructions structured so Kevin can read one step aloud and Bao can act on it before the next.

**Non-English-dominant patient + phone-translator** — 29, Tigrinya-speaking, recently resettled; reading an asthma-medication leaflet through Google Translate on his phone. Wants: idiom-free prose (idioms produce nonsense through machine translation), concrete nouns over abstractions, clear visual structure that survives translation (because translation strips formatting), pictograms supporting each instruction, and information chunked so a phone translation of one step is digestible before he scrolls to the next.

**ICU family at end-of-life decision** — adult children of an 81-year-old man on ventilator support after a stroke; meeting with the palliative care team in a windowless conference room. High cognitive load, grief-flooded, needs structure without bureaucracy. Wants: a one-page summary of what is happening medically (in plain words), what the options are (continued aggressive treatment, comfort care, time-limited trial), what each option would look like in practice over the coming days, and where the family's agency lies. Trust signals: the attending's name, the date, the next decision point. No "next steps" that are actually next decisions — the family chooses; the document does not.

**Resident on overnight handoff** — Maya, PGY-2 internal medicine, receiving sign-out at 7pm on twelve patients; 90 seconds per patient. Wants: SBAR-compressed (Situation / Background / Assessment / Recommendation) with critical findings first, "what to do if" prescriptive (if BP drops below 90, give 250cc bolus and call; if patient becomes confused, repeat CBC and call), and the *single most likely page* she will get tonight named explicitly. Allergies and code status above the fold. No prose — she will not read prose. Acronyms standard within the institution; no cute mnemonics.

### Science / medicine learners

**Maya (MS3)** — third-year medical student on overnight surgery call, four hours of sleep, reading on her phone in the call-room between pages. Eight minutes between this page and the next. Wants: exam-relevant facts (the boards will not ask about the long tail), high-yield over comprehensive, the one diagnostic pearl that distinguishes appendicitis from ovarian torsion when both are on the differential. Mnemonics if they are real ones in circulation; not invented for this artifact.

**Daniel** — 8, third grade, reading a science explainer about cells with his mother sitting next to him. Attention span five minutes if the artifact earns it. Wants: phenomenon to anchor (a real thing happening that he can see — a leaf, a drop of water), then concrete-pictorial scaffolding (drawings before diagrams, diagrams before abstractions), then a question he can answer aloud before the page turns. One new term per page, repeated three times in different contexts before the page ends.

**Renee** — 38, pre-bacc returning to organic chemistry after fifteen years out of school; hasn't done formal STEM since age 22, hasn't done chemistry since high school. Wants: prerequisite scaffolding that does not condescend — "here is the bit of general chem you need to remember, in three sentences" before introducing the new material. Worked examples with steps shown in full, then faded across subsequent examples. No "you should already know this" — she is *here* because she does not.

**Dr. Okafor** — 52, primary-care physician doing CME on a Saturday morning over coffee, 30 minutes. Wants: evidence-graded actionable update (what changed in guidelines this year, what to do differently Monday), case examples that match her panel (mostly adults with hypertension, type-2 diabetes, depression, low-grade musculoskeletal complaints), and the *new* literature integrated with the *old* — not a recap of what she already practices. Estimated reading-time honest; CME credit clear.

**Aaron (Step-1 candidate)** — fourth-year-ahead MD candidate, six weeks out from USMLE Step 1, in dedicated study period; reading a high-yield review at roughly 2× normal mental speed. Will skip *anything* not testable. Wants: tables, bolded keywords, mnemonics, "buzzwords" the exam writers favor (the pathognomonic finding, the classic association), and a sense of priority — what the highest-yield 20% looks like vs. the comprehensive 100%. No epidemiology unless it's a tested fact.

**Coach Patel** — 8th-grade life-science teacher prepping Monday's lesson on cells, Sunday evening. Wants: a phenomenon she can anchor the lesson on (something her students will *see* — yeast budding, pond water under a $40 microscope), a lab worksheet she can copy and adapt, a 5-minute formative assessment, and standards alignment (NGSS MS-LS1-1) visible. Vocabulary list ranked by importance. Differentiation suggestions for the three students reading two grades below and the one reading three above.

### Day-to-day clinical (resident-physician contexts)

The resident's working day generates the dense majority of in-hospital artifact reading: signouts, admit-notes, handoffs, discharge packets, consult requests. These readers are tired, time-boxed, and interruption-saturated; the artifact must survive a single 90-second pass at 2am with a pager firing in the background. None of them are learners in the artifact's moment of use — they are *operators*, and the artifact is a tool they wield through fatigue.

**Jamal** — PGY-1 internal medicine intern on night float, week 6 of the rotation. It is 2am, he has 14 admissions still to write up, and his pager rate is roughly once every eleven minutes. Reading the cross-cover handoff on a workstation-on-wheels parked in a hallway between rooms; perhaps 90 seconds per patient before the next interruption. Wants: prescriptive decision-tree-shaped artifacts; "if systolic drops below 90, give 250cc bolus and call the senior" in *exactly* those words; acronyms only if institutionally standard (no cute new ones); the single most likely page-and-response named explicitly. Under fatigue he defaults to nothing — so the artifact must make the default action obvious.

**Sofia** — PGY-3 senior resident on daytime cap-call. Carrying the admit pager, supervising two interns on a 24-patient service, and pre-rounding her own four overnight admissions. Reading the morning signout card between pages. Wants: artifacts that *triage her attention* — which intern needs eyes-on first, which page can wait fifteen minutes, which patient is about to become unstable. The signout artifact must let her prioritize across thirty patients in five minutes, not survey them. Color, density, and ordering are her primary cues; she will not read prose to find out what's urgent.

**Dr. Liang** — hospitalist attending, 25 years post-residency, receiving a one-liner on morning rounds from her senior resident. Default-trusting but verifying; she will let the resident take the floor and only interrupt for the sentence she did not believe. Wants: the structured problem representation first ("47-year-old man, day three of community-acquired pneumonia, hypoxic to 88% on 4L this morning"), then the resident's *committed assessment* ("I think this is hospital-acquired superinfection") rather than a differential parked open. The spoken artifact must hold its claim *without* the chart in front of her, because she is not opening it on rounds.

**Priya** — clinical pharmacist reviewing discharge medications at 4pm on a Friday, before the patient is wheeled out. Twenty patients in the queue, eight minutes per chart. Wants: an explicit *added / changed / stopped* table; indication for every new medication; renal and hepatic dose adjustments visible without drilling into the formulary; insurance-formulary flags before she calls the family to apologize; the anticoagulation reconciliation done before she signs. Ambiguity costs her a phone call to the attending, which costs her ten minutes she does not have. She will reject artifacts that pretend reconciliation is finished when it is not.

**Robin** — hospital case manager arranging post-discharge skilled-nursing-facility placement for a 78-year-old woman after hip fracture. Reading the discharge summary to find the four facts the SNF intake nurse will ask her. Wants: functional status (ADLs, ambulation distance, transfer assist level), code status, IV access (PICC vs. peripheral vs. none), behavioral notes (sundowning, falls, agitation), anticipated discharge date, insurance status — all on one page, not scattered through five notes. Not interested in clinical reasoning; interested in placement-relevant facts. Will rewrite the discharge summary herself if she has to, and resent it.

**Dr. Adeyemi** — palliative-care attending receiving a goals-of-care consult on a Friday afternoon for an 81-year-old man on the medical ICU service. Reads the consult note *before* entering the room, because the conversation that follows is one she cannot redo. Wants: prior code-status conversations and *who was present* for them, surrogate decision-maker named with relationship and phone number, prognosis as it was previously framed to the family, what the family has already been told (and by whom), what they have not yet been told. The artifact must let her enter the room knowing what the family knows — surprise is malpractice in her work.

**The morbidity & mortality committee** — 8–15 senior faculty plus chief residents seated around a conference table, the presenting resident standing at a podium with slides. Adversarial-but-not-hostile readers; they want the case taught, but they will pick at every decision point that could have gone differently. Wants: chronological timeline with decision points labeled, the prevailing standard-of-care at each branch, the *actual* choice made and its rationale, the counterfactual addressed honestly. The artifact must withstand scrutiny without becoming defensive — the difference between "we considered alternative X and chose against it because Y" and "I had no choice" is the difference between teaching and litigating.

**Devon** — brand-new PGY-1, three days into intern year, four hours of sleep last night, just got paged about a patient he has never met whose nurse is asking about a low blood pressure. Reading the orientation packet's hypotension algorithm at 11pm on the call-room desk. Wants: prescriptive, decision-tree-shaped, "if X then call Y" in *exactly* those words; the contact number of the senior at the top of the page, not in a directory linked from a wiki; no motivational paragraphs about "trust the process." His failure mode is freezing — the artifact's only job is to make the next action obvious enough that he will take it.

### Research and academic medicine

Researchers consume artifacts at every step of the publication and funding pipeline — and they read each one through a specific institutional lens: reviewer, editor, statistician, regulator, methodologist. None of them are the principal investigator on the project, which is precisely why their reading matters most. They are the system's quality gates.

**Dr. Chen** — NIH study-section reviewer at 11pm on a Sunday, working through R01 application #14 of 16 before Tuesday's meeting. Reading the Specific Aims page in roughly 90 seconds before deciding whether to deep-read or skim the rest of the application. Wants: the central hypothesis stated in one bolded sentence within the first 200 words; the gap-in-the-field paragraph specific to *one* unanswered question (not a generic literature lament); the schematic figure decoded in two glances; the three aims parallel-structured so she can hold them in working memory while reading the Approach section tomorrow. A Specific Aims page that requires re-reading loses its score.

**Dr. Aisha** — associate editor at a high-impact-factor journal (JAMA, NEJM, Lancet, or peer), reading the manuscript cover letter before triage. Four minutes per submission. Wants: the one sentence that says why this paper belongs in *this* journal (not "a top journal"); the novel claim in plain English a clinician outside the subspecialty will understand; pre-emption of the obvious reviewer concern (the design limitation she would otherwise raise herself); conflict-of-interest disclosures up front, not buried. A cover letter that lists the paper's findings rather than arguing for the venue gets desk-rejected; she has 200 more to read this week.

**Maya** — PhD biostatistician brought in as collaborator after data collection has finished. 90 minutes reading the protocol, the statistical analysis plan draft, and the analysis script. Wants: a data dictionary mapping every analysis variable back to a case-report-form item; the estimand declared in ICH E9 R1 vocabulary (population, treatment, endpoint, intercurrent-event handling, summary measure); a missing-data plan that names the mechanism assumed (MCAR, MAR, MNAR) and the sensitivity analysis; an analysis-deviation log if one exists. Without these she cannot defend the analysis when reviewers push back, and she will not sign her name to work she cannot defend.

**Wei** — postdoctoral fellow reviewing the PI's third manuscript draft, two days before submission. 60 minutes on a Saturday morning. Wants: every figure caption *states the finding*, not the topic ("Drug X reduces tumor volume by 47% at day 21" not "Tumor volume over time"); every claim in the Discussion cross-referenced to a panel in the Results; the limitations section honest enough that the reviewer cannot add anything Wei did not already concede. Wei knows the data nearly as well as the PI; he will catch the figure-text mismatch the PI's eye has gone blind to.

**Dr. Okwu** — clinical-trialist PI defending a Data Safety Monitoring Board charge that the independent DSMB has flagged a possible safety signal at the planned interim analysis. 30 minutes alone with the interim report before the call begins. Wants: the pre-specified stopping rule referenced explicitly, with its alpha-spending function shown; the interim p-value adjusted for the planned looks; absolute risk and relative risk both presented (not one without the other); a conditional-power calculation visible so the DSMB can judge futility honestly. A report that argues from relative risk alone reads as advocacy and will lose her the board's trust.

**Sara** — pharmaceutical-industry medical-affairs reviewer of a co-authored manuscript before the publication-steering-committee meeting. Reading for both scientific quality and regulatory exposure. 45 minutes. Wants: every claim calibrated against the approved label (and over-claims flagged in the margin); author conflicts disclosed using ICMJE format, not narrative paraphrase; the dataset traced to a specific protocol amendment so the dataset matches the analysis plan in force at collection time; nothing in the manuscript text that could later be quoted by a regulator as off-label promotion. Her veto is final and reads as institutional, not personal.

**Maria** — staff IRB analyst doing first-pass review of a new protocol submission. 25 minutes per protocol, twelve protocols this week. Wants: the consent form readable at grade 6–8 with comprehension checks where the protocol design demands them; risks and benefits balanced honestly (not "minimal risk" boilerplate against a fifteen-page risk section); populations of concern flagged in the cover page (pediatrics, prisoners, pregnant women, decisionally-impaired adults, employees of the sponsor); the data-security plan addressed with specifics, not assurances. Maria does not score the science; she scores the participant's experience.

**Helena** — Cochrane systematic-review methodologist peer-reviewing a meta-analysis submission for the Cochrane Database. 4 hours over a Saturday. Wants: PRISMA 2020 flow diagram complete with both database-search and additional-source counts at each stage; risk-of-bias assessment using ROB 2 (RCTs) or ROBINS-I (non-RCTs) with per-domain judgements and reasoning; forest plot with heterogeneity I² declared and discussed (not just reported); GRADE summary-of-findings table for the prespecified outcomes. A submission missing the SoF table reads as incomplete; she sends it back without scoring.

### Surgical contexts

The surgical artifact is read in three places: the call room (before the case), the OR (during the case, often from memory), and the conference room (after). Each has a distinct tempo and tolerance. The reader is rarely the trainee the textbook implies; far more often it is a fellowship-trained operator rehearsing a single variation, or a community surgeon doing the same case for the four-hundredth time.

**Cole** — PGY-3 on-call orthopedic resident, 2am, reading an ankle radiograph on the call-room monitor between a hip dislocation reduction and a pre-op consent. Fatigued, single-screen, needs to classify the fracture (Weber A, B, or C), decide reduction vs splint vs OR, and call the attending with a one-sentence summary. Wants: a single decision tree he can run top-to-bottom in 90 seconds; the named classification with the discriminating radiographic feature beside each branch; the institutional default for stable Weber-B in the elderly stated as a number, not a paragraph. The artifact must survive a tired pattern-matcher; ambiguity costs him a call he should not have to make.

**Dr. Vance** — fellowship-trained sports surgeon prepping a Tommy John (UCL) reconstruction for a high-school pitcher; she has done 60 of these but is rehearsing the docking-technique variation rather than her usual modified Jobe. Reading the surgical-technique guide the night before, then again in the locker room ninety minutes pre-op. Wants: step-by-step with the *specific decision points* prominent (graft tensioning sequence, suture-anchor vs bone-tunnel) and the obvious steps compressed into a single bullet. She does not need a refresher on exposure; she needs the three steps that differ.

**Dr. Hollis** — community general orthopedist doing four total hip arthroplasties a week, twelve years post-fellowship, high-volume and low-novelty. Reading the implant company's surgical-technique guide for a new femoral-stem size he has not used before. Wants: a sizing nomogram, a checklist for the trial-reduction step, and the one-page "if the femur cracks during broaching" decision-tree posted on the OR wall. Does not want exposition, does not want history of the implant. The artifact's job is to compress a known operation into the two pages he will actually reference.

**Dr. Marquez** — academic shoulder surgeon prepping a morbidity-and-mortality presentation on a failed total knee at six weeks. The audience is peers who will press. Reading the case-prep packet the night before. Wants: the chronologic timeline (pre-op clinic note → operative report → post-op course → re-presentation → revision decision), radiographs in chronological order with the relevant finding circled, the decision points labeled and the standard-of-care at each named. The artifact must let her tell the story without flipping; the M&M format rewards fluency.

**Tyler** — medical-device representative providing technique guidance intra-op, scrubbed-in at the room's side for a complex acetabular revision. He has been trained on the surgical-technique guide twice and rehearsed the sequence in cadaver lab; the guide he was trained on shapes the operation he is now coaching the surgeon through. Often invisible as a reader of the technique document. Wants: numbered steps that map to the instrument tray's numbered positions; a contraindication panel readable in scrub-blue lighting; the failure-mode escape (what to do if the cup will not seat) named without ambiguity. The artifact's hidden reader, but the one whose memory shapes the case.

**Renata** — orthopedic physical therapist receiving a post-operative rotator-cuff rehabilitation protocol from the surgeon's office. She is a clinician, not the patient. Wants: a milestone grid by week (passive range, active-assisted, active, resisted) with the radiographic or clinical criterion for advancing; contraindications listed by phase (no resisted external rotation before week 6); "call me if" thresholds the patient's symptoms must trigger a phone call to the surgeon. The protocol must let her treat without calling for clarification on every visit, and let her *know when to call*.

**Dr. Park** — trauma fellow during a polytrauma damage-control case at level-one trauma center, sharing the patient with general and vascular surgery teams making parallel decisions. Reading the institutional damage-control protocol on the OR computer while waiting for the vascular team to finish their anastomosis. Wants: *resequencing rules* — when the orthopedic ex-fix happens (now, vs after the laparotomy), when definitive fixation is acceptable (typically 7–10 days, after resuscitation endpoints are met), what to communicate to the next team. The artifact's job is to coordinate, not instruct.

**Devi** — OR scrub tech setting up the back table for a femoral-neck fracture fixation using the Synthes 4.5mm large-fragment set plus femoral-neck-specific instrumentation. Reading the one-page instrument list and tray photograph posted in the supply room before the case. Wants: every instrument named the way the surgeon will call for it (the *spoken* name, not the catalog name), the tray photograph oriented as the back table will be set, the *don't-forget* items (guide wires of three lengths, cannulated drill bits) called out in a box. The instrument-list-as-artifact: a layout document that ends in a correct count.

### Sports-medicine contexts

Sports medicine is unusual: the artifact's primary readers include sideline physicians making decisions in seconds, athletic trainers translating between physician and coach, parents balancing fear against autonomy, and coaches who are legally responsible for an emergency-action plan they did not write. The shared constraint is *real-time stakes with non-medical audiences in the loop*.

**Dr. Reeves** — team physician at a Saturday afternoon college football game, 47, primary-care sports-medicine fellowship-trained, twelve years on the sideline. Three minutes between plays, possibly less if there is a turnover. Reading the sideline injury-pattern card on his iPad after a defensive end took a helmet to the lateral knee. Wants: mechanism in (varus + rotation) → top-three differential (LCL sprain, posterolateral corner injury, peroneal stretch) → on-field distinguishing test (dial test asymmetry > 10°) → keep-in-game / hold-and-reassess / EMS decision in three taps. He will not read prose during a game; he will not tolerate a modal that asks him to confirm.

**Jess** — certified athletic trainer at a Division-I training room, 28, four years post-certification, first on the field at every practice and runs the emergency action plan. Reading the post-injury handoff template before sending an athlete to the team physician. Wants: a handoff format the physician can read in 90 seconds (mechanism, on-field exam, current symptoms, sport-specific demands); a treatment-progression note the physician can sign without rewriting; SCAT6 results that print clean for the parent and the coach without revealing protected detail. The artifact serves three downstream readers; Jess is the one who must make it serve all three.

**Coach Vega** — head coach, varsity high-school football, 51, no medical training but legally responsible under state law for the team's emergency action plan. Reading the return-to-play recommendation a sports-medicine physician faxed back after a concussion clearance visit. Wants: a yes/no clearance up front; if "yes but modified," the modification stated in one sentence ("no contact in practice for ten days"); the explicit "next physician check on [date]"; and what to do if symptoms recur ("hold from all activity; call Dr. Reeves at this number"). Coach Vega will not read paragraphs; he will read the top of the page and act on what is there.

**Maria** — parent of a 14-year-old club soccer player with her second concussion in 18 months, 39, looked up CTE on her phone last night, in clinic on a school day with the daughter and a younger sibling. Wants: honest framing of *this* concussion's actual recurrence risk (not generic CTE warnings, which she has already absorbed and amplified); a graduated return-to-play plan with calendar dates so she can plan around school and travel; a teach-back at the end where she repeats the plan in her own words; a phone number she can reach at 7pm Thursday when symptoms come back during homework. The artifact must respect her research without dismissing her fear.

**Carlos** — masters-division marathon runner, 54, software engineer, ran his fastest marathon at 50, now eight months into chronic insertional Achilles tendinopathy and here for a second opinion. Wants: a nuanced rehabilitation plan that preserves training load (he will not stop running, and the plan must acknowledge this); explicit data on eccentric heel-drop protocols vs heavy-slow-resistance vs extracorporeal shockwave (with effect sizes, not testimonials); an honest discussion of when surgery is *not* the answer; and respect for his agency as the person who will actually do the rehab. The artifact's failure mode is paternalism; he will leave the visit if he detects it.

**Priya** — 13-year-old gymnast at a growth-plate-injury consultation with her mother, six weeks out from a state-qualifying meet. Priya wants to compete; mother wants a long-term skeletal-health answer; both are listening to the same artifact. Wants: dual-audience design — the visual story of growth-plate vulnerability for Priya at 13, the long-term-injury data for the mother at 41; honest framing of the trade-off between meet attendance and physeal risk; a visible adolescent-assent + parental-permission structure so Priya is not talked over. The artifact must let both readers leave feeling they were addressed, not negotiated around.

**Wei** — sideline emergency-medicine physician at a high-school wrestling tournament, 36, EM-trained without a sports-medicine fellowship, covering the event as a favor. Wants: a physical-exam reference for the injuries he sees least often (brachial-plexus stinger, AC-joint sprain, weight-cutting-related rhabdomyolysis) and the local emergency-action plan with the venue's AED location, the nearest trauma center, and the transport call-tree. The artifact must work for a physician competent in emergency medicine but not subspecialty-fluent; condescension or jargon both fail him.

**Anika** — third-year orthopedic surgery resident on a sports rotation, 28, six weeks into the twelve-week block and currently learning when ACL injuries warrant operative vs non-operative management. Wants: side-by-side return-to-sport criteria under operative reconstruction (BPTB autograft vs hamstring vs allograft) and under structured non-operative rehabilitation, with the *non-operative* pathway given equal rigor and equal page-space. The artifact's signature failure: presenting "operative" as the default and "non-operative" as the exception. Anika is here to make the comparison honestly; the artifact must let her.

### Pathway-design and informatics

Clinical pathways are read in two different timeframes by the same artifact: by the bedside clinician in 12 seconds, and by the committee revising the artifact across six months. These readers want opposite things from the same diagram — speed vs nuance, prescriptiveness vs auditability — and the pathway artifact must serve both without collapsing into either.

**Dr. Reyes** — emergency-medicine attending at 3am, 9 years post-residency, reading the institution's adapted 2024 sepsis pathway on a workstation-on-wheels at the bedside of a hypotensive 72-year-old. Twelve seconds before the next interruption. Wants: the current decision point highlighted (lactate back, fluids hung, antibiotics to hang now); time-zero unambiguous (was it triage, recognition, or first abnormal vital?); exit criteria visible without scrolling. A pathway that requires Dr. Reyes to find his place in the diagram is a pathway he will close in favor of memory.

**Dr. Olajide** — hospitalist, chairs the institutional sepsis-pathway committee drafting version 3.0. Reconciling the SCCM 2021 update with the institutional formulary, nursing workflow constraints, and the Epic build team's calendar. Reading the working draft as a track-changes document. Needs: working-document register — track-changes between v2 and v3 explicit; recommendation-class deltas (which Class-IIa upgrades to Class-I) annotated; minority-opinion footnotes preserved from committee dissent; a voting-record sidebar so future readers can audit consensus. The pathway is a political document as much as a clinical one; the artifact must show its work.

**Priya** — clinical informaticist, MD with a master's in informatics, translating the printed pathway algorithm into an Epic SmartSet plus best-practice advisory plus order-set. Reading the algorithm node-by-node with the Epic build environment open in the other window. Needs: every node mapped to discrete EHR data (LOINC for labs, RxNorm for meds, SNOMED CT for problems); the *fired-by* logic explicit (does the BPA fire on lactate-result, on order-entry, or on documentation?); the alert-burden estimated against last quarter's encounters so the committee can predict alert fatigue before they ship. A pathway that does not specify *trigger* and *fired-by* will be built three different ways by three different analysts.

**Dr. Henrikson** — cardiologist on an ACC/AHA writing committee, in the final visual-review pass on the typeset figure proofs for the guideline document. Wants: every prose recommendation in the document has a corresponding visual node in the algorithm; every node in the algorithm carries its Class of Recommendation and Level of Evidence in the same place on every page; cross-references between pages use off-page connector symbols (not inline parentheticals that the reader must hunt). The figure is the part of the document that gets photocopied to call-room walls; it must stand alone.

**Dr. Chen** — payer plan medical director building the prior-authorization *if-then* approval algorithm for a new injectable biologic. Wants: every appealable decision point labeled as appealable (so the appeals team can find them); the medical-necessity criteria citable to the underlying guideline source by section number; step-therapy requirements traceable to a named clinical trial with effect size, not "evidence supports." The pathway is consumed by physicians who will write appeal letters citing it; Dr. Chen's job is to make those letters predictable.

**Kim** — QI nurse auditor pulling 25 charts per month against the institutional sepsis pathway for compliance reporting. Wants: the algorithm's *measurable nodes* (lactate-by-1-hour, antibiotics-by-3-hours, fluid-bolus-by-1-hour for hypotension) flagged as audit points with explicit numerators and denominators; *acceptable deviations* documented with the clinical reasoning that justifies them ("comfort-care-only after goals-of-care discussion documented" excludes from denominator). A pathway without explicit deviation-handling produces 100% non-compliance and 0% useful feedback to the clinical service.

**Dr. Suarez** — oncology medical-science liaison building a treatment-decision algorithm to share with community-oncology HCPs as part of a pharma medical-education program. Must show fair-balance — competitor regimens appear in the same boxes with the same level of detail as the sponsor's; evidence-traceability per node (every recommendation cites the trial, not the abstract summary); *off-label* nodes marked explicitly with an off-label icon and a footnote naming the practice basis. Medical-affairs governance will reject the artifact otherwise; the FDA will subpoena it otherwise.

**Yusuf** — PGY-1 internal-medicine intern at 2am, pulling up the UpToDate UTI algorithm to back-stop his uncomplicated-cystitis treatment plan before he calls the senior to staff the admission. Wants: a single-screen yes/no path he can run in under 30 seconds (uncomplicated vs complicated, allergy, pregnancy, recent antibiotic exposure); one click to the evidence (the IDSA guideline section, not the encyclopedia entry) if the attending pushes back in the morning. The pathway's job for the trainee is *confirmation under uncertainty*, not instruction.

### Hostile / skeptical readers

**Critic with a prior position** — coming to the artifact expecting to disagree. Will parse charitably if the argument is solid, harshly if it's sloppy. Apex artifacts anticipate and address their strongest objections.

**Reviewer** — assigned to critique. Looking for weaknesses to note. Respects rigor, punishes sloppiness.

**The competitor** — reads your artifact with an interest in its failure. Will not be persuaded; but the craft is observed and remembered.

### Specific contextual readers

**Reader in a noisy coffee shop** — distracted, fragmented attention, phone buzzing. Apex artifacts reward re-entry — the reader can lose the thread and pick it back up.

**Reader at 2am on a phone in bed** — tired, low patience for complexity, won't click back to previous section. Linear readability matters more than navigational sophistication.

**Reader via screen reader** — blind or low-vision. Experiences the artifact sequentially, through audio. Semantic structure, alt text, and ordering all matter.

**Reader via voice-assistant read-aloud** — commuting, listening. Can't see the figures. The prose has to carry without visual support.

---

## 3. Multi-reader artifacts

Some artifacts need to serve more than one reader simultaneously. Patterns:

- **Layered depth** — the surface layer serves the skimmer; expansions serve the specialist. `<details>` / progressive disclosure.
- **Dual narratives** — a main prose track and a sidebar technical track. Both readable; each for a different reader.
- **Cascading** — executive summary → main report → appendix. Same artifact, different depths.
- **Reader-selector** — explicit choice at the top ("I'm new to this" / "I'm an expert"). Less common; heavier.
- **Annotation layer** — the artifact has an implicit expert track you can toggle on.

---

## 4. Inventing a reader from scratch

When no example fits, build:

1. **What is the artifact's job?** (Teach, inform, persuade, entertain, tool-ify, archive.)
2. **Who would most benefit from this job being done well?** Start there.
3. **Add specificity along every relevant dimension** — expertise, context, device, time, mood, goal.
4. **Name them.** "Priya, senior infrastructure engineer, 27" monitor, 15 minutes, skeptical, wants rigor."
5. **Rehearse the first 30 seconds.** What do they see? What do they think? Where do they stop?

If the first 30 seconds doesn't serve this reader, the artifact isn't ready — regardless of how good the content is later.

---

## 5. Anti-patterns in audience modeling

- **"The reader"** — too vague. Produces defensive, noncommittal writing.
- **Writing for yourself** — the author-as-reader is the blindness cold-read exists to counter.
- **Writing for everyone** — usually means writing for no one. If the artifact must serve many, name each reader and serve each.
- **Persona from a template without re-grounding** — the templates here are examples; using them without adjusting to the actual artifact is just substituting one default for another.
- **Assuming the persona's expertise matches yours** — check.
- **Ignoring the device and context** — a 2000-word explainer on a phone at 2am is a different artifact than the same on a laptop on a workday morning.
- **Treating screen-reader users as an "accessibility carve-out"** — they are a primary persona, not a compliance afterthought. An artifact that is good for Aaron is usually good for everyone; an artifact retrofitted for him at the end is good for no one. Cold-read for screen-reader experience the first time, not the last.
- **Conflating "low literacy" with "low intelligence"** — second-language and low-literacy readers reason as capably as any other reader; the accommodation owed is reading *load*, not concept *load*. Patronizing the reader by removing nuance is a worse failure than the prose being slightly above their reading level. Lower the syntax; do not lower the thinking.
- **Defaulting to WEIRD personas** — Western, Educated, Industrialized, Rich, Democratic. Most published persona examples are WEIRD because the people generating them are. When the audience plausibly reaches beyond that — anything public-facing, anything translated, anything global, anything serving the very poor or the very old — the persona set must reach with it. Adding one non-WEIRD reader as an afterthought is worse than naming the WEIRD assumption explicitly and stating who the artifact does not yet serve.

---

## 6. Cross-references

- `references/cold-read.md` — the protocol that uses personas
- `references/editorial-voice.md` — voice calibrated to reader
- `references/libraries/pedagogy-library.md` — teaching-specific reader modeling

---

## 7. Extending this library

Add a persona when:
- It represents a context or combination not yet covered
- It is specific enough to usefully cold-read against
- It is realistic (reflects actual reader types, not hypothetical caricatures)

Do not add every demographic intersection — that's infinite. Aim for **variety of situation**, not comprehensive demographic coverage.

<!-- END: references/libraries/reader-models.md -->

---


<!-- BEGIN: references/libraries/rhetorical-atlas.md -->

# Rhetorical Atlas

A platter of structures, not a prescribed arrangement. The entries here are modes of constructing an argument or narrative drawn from many traditions. Read them as a palette to choose from, recombine, hybridize, or rebel against.

> See `references/how-to-use-this-system.md` for the platter principle.

---

## 1. Classical Western rhetoric

### Aristotelian

From *Rhetoric* (c. 350 BCE). Aristotle identified three modes of appeal:

- **Ethos** — credibility. Why the author is trustworthy.
- **Pathos** — emotion. How the argument makes the reader feel.
- **Logos** — logic. The reasoning itself.

Apex arguments balance all three. Over-reliance on logos reads as cold; over-reliance on pathos reads as manipulative; over-reliance on ethos reads as name-dropping.

### Ciceronian arrangement

The six-part classical speech structure:

1. **Exordium** — introduction; secure the reader's attention and goodwill
2. **Narratio** — background; establish the situation
3. **Partitio** — outline; state what you'll argue
4. **Confirmatio** — positive evidence for your claim
5. **Refutatio** — counter-arguments addressed and defeated
6. **Peroratio** — conclusion; summary and emotional close

Still the skeleton of many long-form arguments today. Recognizing it helps identify when an argument is missing a part.

### Stasis theory

Before arguing, identify the kind of disagreement:

- **Conjectural stasis** — did X happen? (Fact)
- **Definitional stasis** — what is X? (Definition)
- **Qualitative stasis** — is X good or bad? (Quality)
- **Translative stasis** — who should decide about X? (Jurisdiction / procedure)

Many unproductive arguments happen when participants are at different stases.

---

## 2. Contemporary structures

### Minto Pyramid (Barbara Minto, 1985)

The consultancy-favored structure:

1. **Main argument (SCQA)**:
   - **Situation** — the context
   - **Complication** — the problem in it
   - **Question** — the question the complication raises
   - **Answer** — the recommendation
2. **Supporting arguments** — 3-5 claims that support the main argument
3. **Supporting data** — evidence for each supporting argument

Every level of the pyramid must be **MECE** (mutually exclusive, collectively exhaustive) and groupable under the level above.

**Used for:** executive memos, strategic recommendations, consulting decks.

### Claim, Evidence, Reasoning (CER)

Scientific argument structure:

- **Claim** — what you're arguing
- **Evidence** — specific data supporting the claim
- **Reasoning** — why the evidence leads to the claim

Used in scientific writing, lab reports, expert testimony. Apex work makes the reasoning explicit; mediocre work treats it as self-evident.

### Toulmin model (Stephen Toulmin, 1958)

A richer argument structure:

- **Claim** — the position
- **Grounds** — evidence
- **Warrant** — the implicit link between grounds and claim
- **Backing** — support for the warrant itself
- **Qualifier** — degree of certainty
- **Rebuttal** — acknowledged counter-conditions

The Toulmin model surfaces the *warrant* (the implicit "and therefore"), which most arguments leave unspoken and most disagreements reveal.

### Inverted pyramid (journalism)

News-writing convention:

1. **Lede** — the most important information first. Who, what, when, where, why, how in one or two paragraphs.
2. **Body** — supporting detail in decreasing importance
3. **Tail** — background and context readers who stay will read

Designed so an editor can cut from the bottom without losing essential information, and so a reader can stop at any point with the most important material already absorbed.

### Wall Street Journal formula

A *Wall Street Journal* feature opens with a specific, emotionally resonant anecdote (one person's story), then broadens to the general principle or issue, then returns to the specific at the end.

- **Specific hook** — Chen's business failed last spring
- **Nut graf** — the broader pattern; why this story matters
- **Expansion** — data, context, other examples
- **Resolution** — return to Chen; what's next for him

### Three-act structure (narrative)

From Aristotelian *Poetics* through screenwriting:

- **Act I: Setup** — establish characters, world, normal state, inciting incident
- **Act II: Confrontation** — escalating complications, rising tension, crisis
- **Act III: Resolution** — climax, resolution, new equilibrium

Scaffolds stories; also scaffolds explainers with narrative elements.

### Freytag's pyramid

A five-part variant:
1. Exposition
2. Rising action
3. Climax
4. Falling action
5. Dénouement

### Save the Cat / Blake Snyder

A 15-beat screenwriting structure. Often used as an outlining tool for non-fiction narratives.

### The hero's journey (Joseph Campbell / Vogler)

Mythological structure through 12 stages:
1. Ordinary world
2. Call to adventure
3. Refusal
4. Meeting the mentor
5. Crossing the threshold
6. Tests, allies, enemies
7. Approach to the inmost cave
8. Ordeal
9. Reward
10. The road back
11. Resurrection
12. Return with the elixir

Used in product launches, company histories, personal essays.

---

## 3. Non-Western and alternative structures

### Kishōtenketsu (Japanese, also Chinese)

A four-act structure common in East Asian literature, cinema, and comics:

1. **Ki** — introduction, establish the situation
2. **Shō** — development, deepen the situation
3. **Ten** — twist, an unexpected change or new element
4. **Ketsu** — resolution, integrate the twist with what came before

Notably *lacks conflict* as a structural element. The twist is not opposition; it is reframing. Produces a different narrative feel — contemplative, surprising, often more mature-feeling than Western three-act.

### Ring composition

Ancient structure (Homer, biblical narratives, many oral traditions). The elements appear A, B, C, D, C', B', A' — mirroring around a center. The center is the thematic core.

Feels musical, memorable, meditative. Used in some contemporary essays where the writer wants the structure to feel woven.

### Indigenous oral structures

Many Indigenous storytelling traditions use non-linear structures:

- **Circular** — arriving where you started, transformed
- **Nested** — stories within stories within stories
- **Place-based** — structure follows a journey through physical places
- **Seasonal** — structure follows a year, a lifetime, a generational cycle

These resist the "conflict → resolution" Western arc and often emphasize relationships, place, and continuity over progression.

### Chinese eight-legged essay (八股文)

A highly formal historical structure used in imperial examinations:
1. Opening
2. Amplification
3. Preliminary exposition
4. Initial argument (first leg)
5. Central argument (second leg)
6. Latter argument (third leg)
7. Final argument (fourth leg)
8. Conclusion

A rhetorical structure that was eventually reformed out of use; worth knowing as a historical tradition that emphasized formal pattern.

### Haiku / poetic compression

Radical compression: juxtapose two images, suggest a third thing. Informs the aesthetic of extreme economy — a lesson any long-form artifact can apply.

### Dialectic (Hegelian)

- **Thesis** — a position
- **Antithesis** — its opposition
- **Synthesis** — resolution incorporating both

Useful for essays that want to acknowledge and integrate opposing views rather than merely defeat them.

---

## 4. Argument structures for specific purposes

### Problem-Solution

1. Describe the problem
2. Establish its importance
3. Propose the solution
4. Show how the solution addresses the problem
5. Address objections
6. Close

Workhorse structure for pitches, proposals, op-eds.

### Comparative

1. Introduce items being compared
2. Establish criteria
3. Compare along criterion 1 (all items)
4. Compare along criterion 2 (all items)
5. ...
6. Synthesize

Alternative: compare item-by-item rather than criterion-by-criterion. Each has costs; choose based on reader's likely memory demands.

### Chronological

1. Earliest event
2. Next
3. Next
4. ...
5. Present or latest
6. (Optional) future implication

Scaffolds histories, retrospectives, post-mortems.

### Spatial

Organize by physical or conceptual arrangement — moving through a space, zooming from macro to micro, scanning across a field.

### Topical

Organize by the categories inherent in the material. Works for encyclopedic, reference, or survey writing.

### Causal

1. Phenomenon
2. Cause A
3. Cause B
4. Cause C
5. Interaction
6. Conclusion

Alternative: start from the cause and trace consequences.

### Deductive

1. General principle
2. Specific case
3. Conclusion

### Inductive

1. Multiple specific cases
2. Identify pattern
3. General principle

### Abductive (inference to best explanation)

1. Observed phenomenon
2. Candidate explanations
3. Evaluate each
4. Identify best

Detective fiction and scientific reasoning.

### Socratic (question-led)

1. Pose a question
2. Offer partial answer
3. Raise objection or new question
4. Refine answer
5. ...
6. Arrive at deeper understanding

Used by Plato; adapted for modern pedagogy and essays.

### Ladder of inference

From concrete to abstract and back:
1. **Observable data** (what happened)
2. **Selected data** (what I noticed)
3. **Meaning** (what I took it to mean)
4. **Assumptions** (what I assumed)
5. **Conclusion** (what I decided)
6. **Belief** (what I now believe)
7. **Action** (what I did)

Exposes the implicit inference chain in an argument. Useful for debugging disagreement or for carefully reasoned argument.

---

## 5. Journalistic and explanatory forms

### The profile

Extended treatment of one person or entity. Structure usually alternates biography, anecdote, analysis, direct quote.

### The deep explainer

1. Establish the phenomenon
2. Walk through the mechanism
3. Illustrate with examples
4. Address common misunderstandings
5. Discuss implications

*The Atlantic*, *Vox*, *The New Yorker*'s science and politics features, Ciechanowski's technical pieces.

### The investigation

1. Anomaly / finding
2. What we knew
3. What we discovered
4. What it means
5. What happens next

### Data journalism's "scrollytelling"

1. Hook (a vivid statistic or image)
2. Zoom out (context)
3. Zoom in (detail, personal stakes)
4. Pattern reveal (the visualization that makes the argument)
5. Implication

### Reference (encyclopedic)

1. Definition
2. Etymology / history
3. Variants / types
4. Examples
5. Related concepts

### Tutorial (procedural)

1. What you'll build / know
2. Prerequisites
3. Step 1
4. Step 2
5. ...
6. Verification
7. Where to go next

### Review

1. What it is
2. What it does well
3. What it doesn't
4. Who it's for / not
5. Verdict

---

## 6. Scientific / academic structures

### IMRAD

The canonical scientific paper structure:

- **Introduction** — what's the question and why
- **Methods** — what was done
- **Results** — what was found
- **Discussion** — what it means

Recognizable across disciplines.

### Literature-review-first

1. Prior work
2. Gap in the literature
3. Our contribution
4. Evidence
5. Conclusion

Common in survey papers and empirical research write-ups.

### Technical specification

1. Purpose / motivation
2. Terminology
3. Requirements
4. Proposed design
5. Alternatives considered
6. Security / performance / scaling considerations
7. Appendices

Engineering RFC structure.

---

## 7. Structures you choose by breaking

Apex work often identifies a reader's expected structure and deviates from it deliberately:

- Opens with the conclusion (inverted pyramid in a genre that expects narrative buildup)
- Refuses synthesis at the end (dialectic that stays unresolved)
- Uses Kishōtenketsu where three-act is expected (making the reader feel the difference)
- Structures a technical piece as a personal essay

Deviation works when:
- The deviation is deliberate, not accidental
- The reader notices the difference (because they've internalized the expected structure)
- The deviation serves the argument

Deviation fails when:
- It's accidental (the author didn't have the expected structure in mind)
- The reader is too distracted to notice
- It adds nothing beyond novelty

---

## 8. Hybrid and recombinant structures

Apex artifacts often combine:

- **Minto pyramid within a narrative frame** — the pyramid is the content; the frame gives it emotional texture.
- **WSJ formula with IMRAD body** — specific opening, then research structure, then specific close.
- **Kishōtenketsu in a technical explainer** — introduce topic, deepen, introduce unexpected angle, integrate.
- **Layered IMRAD** — the paper's abstract is itself structured; the intro is itself structured; fractal.
- **Ring composition around a data visualization** — the chart is the center; everything circles it.

Don't feel bound to use exactly one structure. The best structure for most artifacts is one no reader has seen before but every reader can follow.

---

## 9. How to choose (or invent)

For any artifact:

1. **Identify the reader's expected structure.** (What convention applies? What's the genre default?)
2. **Ask whether that serves this specific argument.** Often yes. Sometimes not.
3. **If it does, use it well** — recognize its parts and deliver each.
4. **If it doesn't, identify what would serve better** — from this atlas, from combinations, from invention.
5. **Declare the structure to yourself.** Writing without knowing your structure produces slop.
6. **Serve the structure** — if it's chronological, don't leap ahead; if it's Minto, don't hide the argument behind evidence.

---

## 10. Cross-references

- `references/libraries/reader-models.md` — reader expectations shape structural choice
- `references/libraries/pedagogy-library.md` — teaching-specific sequences
- `references/libraries/composition-library.md` — visual composition sometimes echoes rhetorical structure
- `references/editorial-voice.md` — voice that supports the structure

---

## 11. Extending this atlas

Add a structure when:
- It represents a distinct approach to arrangement
- It has provenance (tradition, genre, specific practitioner)
- It is not a minor variation on an already-covered structure

The goal: enough structures that the creator has real choices; not so many that the space feels cluttered.

<!-- END: references/libraries/rhetorical-atlas.md -->

---


<!-- BEGIN: references/libraries/romantic-artifacts.md -->

# Romantic Artifacts Library

A platter for artifacts with **romantic, intimate, celebratory, commemorative, or affectionate** purposes — love letters, wedding and engagement materials, anniversary pieces, vows, elopement keepsakes, valentines, memory books, marriage-proposal artifacts, couple-history visualizations, relationship-anniversary explainers, and adjacent forms.

Romance has long design traditions — from illuminated medieval love tokens, to Victorian valentines, to Art Nouveau lettering, to contemporary wedding invitation design — and deserves treatment apart from generic celebratory register.

> See `references/how-to-use-this-system.md` for the platter principle.

---

## 1. What romantic artifacts do

Each romantic artifact carries particular weight:

- **Declarations** — a love letter, a vow, a proposal. The artifact's existence is itself the statement.
- **Commemorations** — anniversary, first-date reconstruction, memory book. Marking a moment that has happened.
- **Invitations** — to a wedding, an elopement, a commitment ceremony. Practical and emotional at once.
- **Programs** — ceremony orders, guide to the day. Document as designed object.
- **Thanks** — post-wedding notes; acknowledgment of a specific kindness. Intimate gratitude at scale.
- **Tokens** — a small gift, a bookmark, a charm, a signed book inscription. Design for preservation.
- **Narrative** — "how we met" pieces, timeline of a relationship, keepsake story of a chapter. Personal history rendered.
- **Apology or reconciliation** — rarer genre but important; tone and restraint matter.

---

## 2. Romantic design traditions

### Victorian love tokens (1830s–1900)

- Ornate calligraphy
- Decorative borders, filigree, ribbon motifs
- Lace paper (die-cut decorative papers)
- Forget-me-nots, violets, pansies, roses as symbolic flowers
- Small format, pocket-kept
- Esther Howland's American valentines (mass-produced but still decorative)
- "Language of flowers" (floriography) — each flower carried specific meaning

**Transferable moves:** small scale, preciousness, hand-lettered feel, floral symbolism, ornament as affection.

### Art Nouveau (1890–1910)

- Organic curves, flowing botanicals
- Hand-drawn lettering as image
- Muted jewel-tone palettes — moss, wine, copper, deep blue
- Alphonse Mucha's decorative posters (romantic register)
- Integration of figure, type, and ornament

**Transferable moves:** lettering as ornament, botanical integration, muted saturation, tall proportion.

### Wedding invitation tradition

Modern wedding invitation design has centuries of convention and recent expansion:

- **Traditional** — engraved or letterpress on heavy card; minimal illustration; formal typography (Trajan, Engravers, Copperplate); ivory/ecru/blush ground
- **Contemporary classic** — serif display (Didone or transitional) + fine sans, monogram, restrained palette
- **Contemporary modern** — editorial-magazine typography, unexpected palette, playful composition
- **Minimalist** — thin type, generous space, single accent color
- **Maximalist** — botanical illustration, gold foil, deckle-edge paper, multi-piece suites
- **Destination / vernacular** — location-specific motifs (Tuscan, coastal, tropical, alpine)
- **Artistic / hand-illustrated** — bespoke watercolor, line illustration, custom calligraphy
- **Editorial-magazine** — wedding as publication (Condé-Nast-inflected) with monogram masthead

**Practitioners:** Smock, Minted's guest-designer collection, Sugar Paper, Bella Figura, Papyrus's high-end archive. Historical: Crane & Co., Tiffany & Co. stationery.

### Calligraphy & hand-lettering traditions

- **Copperplate / Spencerian** — flowing formal script; American 19th-century wedding standard
- **Italic** — Renaissance-era; used in formal contemporary stationery
- **Modern calligraphy / brush lettering** — contemporary looser hand-lettering, personal voice
- **Islamic calligraphy** — thuluth, naskh, diwani, kufic; each with distinct character
- **East Asian calligraphy** — Chinese (楷书 kaishu, 草书 caoshu), Japanese (shodō), Korean
- **Celtic half-uncial** — illuminated manuscript inheritance
- **Blackletter / Fraktur** — heavy formal scripts; less common for romantic register but present in traditional German and Nordic contexts

### Letter-writing traditions

- **18th-century epistolary** — formal salutations, indented paragraphs, closing with social position ("Your most humble servant")
- **19th-century Romantic** — emotive register, lyrical excess, Byron/Keats tradition
- **Victorian** — elaborate ceremony around a letter: seal, monogram, specific paper
- **Mid-20th-century American** — typewritten letters, often tender underneath the formality
- **Contemporary intimate** — mixed register: specific memory + plain language + vulnerability

### Wedding programs & day-of materials

- **The program** — order of ceremony, often illustrated or ornamented
- **Menus** — often echo the invitation palette
- **Place cards** — calligraphy, wax seals, custom illustration
- **Signage** — directional, welcome, dedication
- **Table numbers / names** — meaningful to the couple
- **Favors** — wrapping or tag design
- **Ceremony backdrop** — stationery echoed in spatial design

### Proposal and ring artifacts

- **The proposal** itself as designed moment — scrapbook, letter, mini-book, treasure hunt
- **Ring box & ring boxes** — the object design around the moment
- **Engagement announcements** — post-proposal social communication

### Memory & anniversary

- **First-date reconstruction** — timeline, place, menu, song played
- **Year-in-review** — custom calendar, shared playlist, year's highlights
- **Anniversary gift traditions** — paper (1st), cotton (2nd), leather (3rd), through gold (50th); "modern" alternatives
- **Shared journals** — co-written over years
- **Memory books** — the couple's compiled archive

---

## 3. Romantic color registers (not a shortlist)

Romance has color families that work well, though any palette that serves the artifact's specific voice can be romantic.

### Warm romantic
- **Dusty rose + cream + champagne gold + sage** — contemporary wedding standard
- **Blush + ivory + soft terracotta** — warm Mediterranean wedding
- **Peach + cream + eucalyptus** — Southern California wedding aesthetic

### Deep romantic
- **Burgundy + gold + ivory** — autumnal, traditional
- **Navy + blush + gold** — classic, vintage-inflected
- **Forest + wine + amber** — autumn luxe
- **Plum + rose gold + slate** — modern moody

### Minimal romantic
- **Black + white** — formal, editorial, understated
- **Bone + sepia + rose** — vintage-leaning elegance
- **Taupe + cream + single accent** — contemporary minimal

### Playful romantic
- **Coral + turquoise + cream** — summer wedding joy
- **Yellow + pink + white** — happy optimism
- **Peach + mint + cream** — soft pop

### Historic romantic
- **Illuminated manuscript** — ultramarine, gold, madder red, vellum
- **Ukiyo-e romantic** — indigo, rose, soft cream, sumi ink
- **Art Nouveau** — moss, wine, copper, pearl

### Ethereal romantic
- **Soft lavender + silver + pearl white + hint of sage**
- **Misty blue + ivory + dove gray + pale blush**
- **Warm white + gold dust + champagne rose**

### Celestial
- **Deep navy + gold stars + warm cream**
- **Dusk gradient** (rose → indigo → navy)

### Cultural specificity

Romance has traditions many cultures have refined:

- **Indian wedding** — saffron, marigold, fuchsia, deep red, turmeric, gold foil. Visual maximalism as expression of joy.
- **Chinese wedding** — deep red, gold, white. Red as central color of celebration.
- **Persian wedding (aghd)** — saffron, emerald, deep red, silver and gold. Traditional sofreh elements.
- **Nigerian wedding** — brilliant saturated color, pattern-rich, specific color schemes per day (traditional, white, reception).
- **Greek and Mediterranean** — white + blue + olive + coral; Aegean palette.
- **Scandinavian** — muted natural, birch, moss, stone; restrained warmth.
- **Mexican wedding** — saturated warm palette (crimson, turquoise, marigold), papel picado, embroidery inheritance.
- **Japanese shinto wedding** — white (as mourning and rebirth), deep red, sumi black, gold. Restrained.

See `references/libraries/color-library.md` for the broader space.

---

## 4. Romantic typography

### Script faces worth knowing
- **Spencerian / Snell Roundhand / Kuenstler Script** — formal English wedding standard
- **Bickham Script** — elaborate formal
- **Copperplate** — similar register
- **Modern calligraphy** faces — Allura, Great Vibes, Alex Brush, Selima
- **Sacramento, Dancing Script** — less formal, contemporary casual

### Serif display for romance
- **Didot / Bodoni / Playfair** — editorial elegance; often with a wedding script pair
- **Cormorant** — contemporary variable free face, elegant
- **Canela, Domaine Display** (Klim) — luxury contemporary
- **Ogg (Sharp Type)** — contemporary editorial-romantic
- **Adage Script** — contemporary formal script
- **Crimson Pro** — open-source book-feel

### Body
- **Arno Pro, Garamond, Baskerville** — traditional serif bodies
- **Source Serif Pro, Lora** — contemporary accessible
- **Inter, Work Sans** — modern sans pair with a romantic display

### Pairings of character
- **Bodoni + Spencerian + quiet sans** — luxury tradition
- **Playfair Display + Lora** — accessible online romantic
- **Cormorant + Montserrat** — contemporary free pair
- **Didot + a custom calligraphic monogram** — editorial wedding
- **Sabon + Engravers + italics of both** — pure classical

### Setting considerations
- **Generous tracking** on all-caps for invitations (+0.15em is a starting point)
- **Italic for quotations, vows, poems, guest names** — carries emotional emphasis
- **Small caps** for gentle emphasis within prose — "FEBRUARY THE FOURTEENTH" rather than "February 14th"
- **Hanging punctuation** — in high-typographic-register work
- **Ligatures and swashes** — variable faces make this accessible

---

## 5. The voice of romantic writing

### Registers available

- **Intimate** — addressed specifically to the beloved; vulnerable; particular
- **Celebratory** — for gathered witnesses; buoyant; inclusive
- **Commemorative** — reflective, backward-looking, mature
- **Ceremonial** — formal; structured; ritual-paced
- **Playful** — affectionate humor; private references made public
- **Lyrical** — poetic; metaphorical; rhythm-forward
- **Quietly serious** — stripped of flourish; direct; weighty by restraint

Each is a valid register; most artifacts hold one primarily, perhaps two in tension.

### Voice principles

- **Specificity over superlative.** "The way you pour coffee" beats "your wonderful qualities."
- **Earned sentiment.** Commit to the specific memory or feeling; don't generalize.
- **The private detail that reads as universal.** Something particular to you two that resonates because it's particular.
- **Restraint against overflowing.** The letter that trusts one image can carry more than the one that piles up twenty.
- **Honesty about difficulty.** Romantic artifacts that acknowledge imperfection often land deeper than perfect-seeming ones.

### Writing exemplars
- **Keats's letters to Fanny Brawne** — feverish longing
- **Nabokov's letters to Véra** — sustained tenderness across a lifetime
- **Elizabeth Barrett Browning's *Sonnets from the Portuguese*** — sonnet form applied to the beloved
- **Pablo Neruda's love sonnets** — vivid image, specific sensory
- **Rainer Maria Rilke's *Letters to a Young Poet*** — not romantic but instructive about intimate voice
- **Agha Shahid Ali's ghazals** — formal poetic precision
- **Mary Oliver's love poems** — attentive naturalism
- **Nizar Qabbani's love poetry** — Arabic, lyrical, politically charged
- **Song of Songs** (Hebrew Bible) — ancient love poetry with radical sensual frankness
- **Ruth Padel on poetry of love** — contemporary critical
- **Louise Glück's late love poems** — restrained, adult, mature

---

## 6. Poetic forms for romantic artifacts

Different poetic forms fit different occasions:

- **Sonnet (Italian / Petrarchan or English / Shakespearean)** — 14 lines; volta between octave/sestet or at line 12. Classic love-poem container.
- **Ghazal** — Arabic / Persian / Urdu tradition; couplets with refrain. Love and longing.
- **Villanelle** — 19 lines, five tercets + quatrain, two refrains. Theodore Roethke's *The Waking*, Dylan Thomas's *Do not go gentle*.
- **Pantoum** — repeating couplet pattern; builds through repetition.
- **Haiku / senryu** — 5-7-5 or just "short form"; captures a moment.
- **Tanka** — 5-7-5-7-7; longer than haiku, often more romantic/emotional.
- **Sestina** — 39 lines with six end-words rotating. Challenge form; rewards commitment.
- **Ode** — extended praise of subject. Love ode as genre.
- **Aubade** — lovers parting at dawn. Specific mood.
- **Elegy** — mourning; applicable for romantic-commemorative artifacts after loss.
- **Prose poem** — paragraph form without line breaks, still poetic.
- **Blank verse / free verse** — no formal constraint; contemporary default.

---

## 7. Romantic artifact composition

### Stationery suite thinking
A wedding or major romantic artifact often isn't one piece but a **suite**:
- Save the date
- Invitation + response card + details card + envelopes
- Day-of materials (programs, menus, signage, place cards)
- Thank-you notes

Each echoes the suite's typography, palette, and motif — but with role-appropriate weight. The invitation is the centerpiece; the thank-you notes the coda.

### Monogram and mark
A romantic artifact often carries a mark — initials, a date, a small illustration — that identifies it across the suite. Historical inheritance from Renaissance family crests and Victorian personal cyphers.

### Illumination and ornament
Contemporary romantic design often re-engages with ornament — botanical sprays, geometric frames, custom flourishes. Not decoration for its own sake; marking an artifact as *designed for this occasion and no other*.

### Materiality
Physical romantic artifacts often depend on materiality: thick card, textured paper, foil stamping, deckle edges, wax seals, vellum overlays, ribbon. In digital-only artifacts, simulate through typography, color, imagery, and pacing — but honor that the medium matters.

---

## 8. Wedding & romantic artifact genres

Specific artifact types to know:

### Save the date
Announces the fact and date. Lighter than the invitation. Informal announcement.

### Wedding invitation
The formal ceremony. Language traditionally third-person ("Mr. and Mrs. Surname request the honor of your presence"); contemporary often first-person. Structure: hosts, request, couple's names, date, time, place, reception note.

### Wedding website URL card
Contemporary addition; sends guests to details, RSVP, registry.

### Response card (RSVP)
Traditionally a separate card + envelope; contemporary often web-based.

### Order of service / ceremony program
Guides guests through the ceremony. Readings, music, vows, rituals, people involved.

### Wedding vows
Traditional or personal. Structure: acknowledgment, promises, closing. Often the most-quoted piece of the wedding.

### Toast / speech
Maid of honor, best man, parents. Structure: greeting → origin ("I've known X since…") → characterization (specific, loving) → couple blessing → closing toast.

### Anniversary messaging
Yearly note; tradition of increasing formality (paper, cotton, leather, wood, sugar, iron…).

### Love letter
Private, unstructured, voice-driven. The oldest and most durable romantic form.

### Elopement / courthouse wedding
Minimal ceremony; often bespoke artifacts that mark it as intentional rather than casual.

### Same-sex, queer, non-traditional ceremonies
Traditions being actively written; often require inventing artifact forms rather than inheriting.

### Long-distance relationship artifacts
Shared journals, mailed cards on specific schedules, coded messages, countdown calendars. A sub-genre.

### Proposal
Range: private and quiet, public and elaborate. Artifacts from custom books to scavenger hunts to surprise gatherings. Design varies with personality.

### Divorce / separation (dark romantic)
Rare genre but real: an artifact commemorating a relationship ending with dignity. Respectful, honest, often private.

---

## 9. Cross-domain borrowing for romantic artifacts

Romance often draws productively from:

- **Medieval illumination** — gold leaf, marginalia, monogram initials
- **Japanese craft** — restraint, wabi-sabi, meaningful empty space
- **Scandinavian design** — warm minimalism, handcraft feel
- **Art Nouveau and Arts & Crafts movement** — botanical, curvilinear
- **Pre-Raphaelite painting** — lyrical figuration, literary reference
- **Cinema** — film-title typography, wedding-as-movie moment
- **Food and wine** — tasting-menu aesthetic for wedding menus
- **Music** — playlists as artifacts
- **Mapmaking** — "where we've been" as mapped narrative

---

## 10. Cross-references

- `references/libraries/color-library.md` — palette traditions, Art Nouveau, historical
- `references/libraries/type-library.md` — script faces, editorial pairings
- `references/libraries/composition-library.md` — editorial and manuscript composition
- `references/libraries/rhetorical-atlas.md` — letter-writing traditions
- `references/libraries/creative-artifacts.md` — poetry forms, prose craft
- `references/libraries/inspiration-atlas.md` — illuminated manuscripts, advertising, botanical illustration

---

## 11. Extending this library

Add when:
- A tradition, era, or culture has distinct romantic artifact conventions not yet covered
- A specific exemplar (designer, publication, historical artifact) is genuinely valuable to reference
- A contemporary form is emerging that deserves articulation

Avoid:
- Sentimentality as a substitute for craft
- Generic "romantic" styling without specific tradition
- Cultural-appropriation risk (cultural traditions should be referenced with care, not flattened into aesthetic moves)

The goal: creators of romantic artifacts have a rich cultural and historical vocabulary to draw from, combine, and transcend. Restraint and specificity usually beat ornament.

<!-- END: references/libraries/romantic-artifacts.md -->

---


<!-- BEGIN: references/libraries/scientific-artifacts.md -->

# Scientific Artifacts Library

A platter for artifacts in scientific domains — research papers, figures, lab notebooks, posters, scientific explainers, data publications, derivations, mechanism diagrams, scientific notation systems. Science has rich traditions for how information is organized, how uncertainty is shown, and how rigor is visible.

The material here expands the creative space rather than narrows it. Apex scientific artifacts often violate a tradition productively.

> See `references/how-to-use-this-system.md` for the platter principle.

---

## 1. Core scientific artifact principles

- **Uncertainty is visible.** Not hidden behind point estimates. Error bars, confidence intervals, distributions, sensitivity analyses.
- **Methodology is reproducible.** Other researchers should be able to reproduce or critique. Methods sections are load-bearing.
- **Data is traceable.** Sources, dates, preprocessing steps, code — all available.
- **Claims are calibrated.** Don't say "proves" when you mean "is consistent with." Don't say "significant" without the context.
- **Priority of discovery matters.** Prior work acknowledged, credit given, novelty bounded.
- **Skeptics are anticipated.** Apex scientific writing addresses its strongest objection.
- **Replication is honored.** Reproducibility packages, data sharing, protocol pre-registration.

Each of these is a space of choices, not a single correct move.

---

## 2. Scientific writing traditions

### IMRAD (standard research paper)

Introduction → Methods → Results → Discussion. The dominant structure in contemporary biomedical and natural-science literature. Workhorse; not the only valid form.

### The review article

Surveys a field or topic. Structure typically:
1. Scope and inclusion criteria
2. Background
3. Thematic or chronological organization of the literature
4. Synthesis / integration
5. Open questions

### The systematic review / meta-analysis

More structured than a narrative review. Follows PRISMA guidelines. Search strategy, inclusion/exclusion criteria, risk-of-bias assessment, quantitative synthesis where possible.

### The perspective / commentary

Opinion-adjacent scientific writing. Argues for an interpretation or direction. Often invited by a journal to accompany an original-research article.

### The letter / brief report

Short, focused. Often responds to a published article or presents a narrow finding.

### The case report / case series

In medicine and clinical sciences: detailed description of individual patients or small series. Hypothesis-generating, not hypothesis-testing. Distinct rhetorical genre.

### The methods paper

Introduces a new method or tool. Different conventions from research papers: emphasis on validation, benchmarking, comparison with existing methods.

### Textbook / monograph

Long-form scientific writing. Different from journal articles: more pedagogical structure, more thorough background, more integration across topics.

### The preprint / working paper

Increasingly common before formal peer review. Same rigor, less gatekeeping, open comment. arXiv, bioRxiv, SSRN, EarthArXiv.

### The science communication essay

For lay or general-scientific audiences. Quanta Magazine, Scientific American, Nautilus, Aeon, LWN, Ars Technica science.

### The explainer / primer

Technical but non-research-paper. Distill.pub articles. 3Blue1Brown videos. Bartosz Ciechanowski essays. Often the most visually ambitious scientific writing.

---

## 3. The scientific figure

Figures in scientific publications have distinct conventions.

### Figure types

- **Descriptive figures** — sample images, example data, representative specimens
- **Analytic figures** — plots, charts, statistical summaries
- **Mechanistic figures** — models, diagrams, pathways
- **Schematic figures** — experimental designs, flowcharts, decision trees
- **Composite figures** — multi-panel figures combining types

### Multi-panel conventions

Scientific figures often have panels labeled A, B, C (or a, b, c). Each panel carries one message; together they make the figure's composite argument. Standard patterns:

- **A: phenomenon → B: mechanism → C: quantification**
- **A: experimental design → B: representative data → C: group comparison**
- **A: whole → B: detail → C: comparison**

### Figure captions

Unlike general captions, scientific figure captions are dense. Structure:

1. **Title** — one-sentence description of the figure
2. **What each panel shows** — A: ..., B: ...
3. **Experimental conditions** — sample size, timing, grouping
4. **Statistical conventions** — error bars (SD? SEM? 95% CI?), symbols (*, **, *** for p-value thresholds, or exact values)

### Statistical conventions

- **Error bars** — always labeled: SD (standard deviation), SEM (standard error of the mean), or CI (confidence interval). SD and SEM differ by √n; confusing them is common and wrong.
- **Significance markers** — asterisks (*, **, ***) are conventional for p-value thresholds but increasingly deprecated in favor of exact p-values and effect sizes.
- **Distribution over boxes** — raw data shown alongside or instead of boxplots. Scatter + boxplot, or violin plots, reveal more than boxes alone.
- **Log vs. linear axes** — log for data spanning orders of magnitude; always annotated.
- **Paired vs. unpaired analysis** — indicated visually (lines connecting paired points).

### Color conventions

- **Avoid rainbow / jet** colormaps on continuous data — not perceptually uniform; introduces false boundaries.
- **Viridis, magma, plasma, cividis** — perceptually uniform, colorblind-safe colormaps.
- **Red/blue for diverging** — with white in the middle if the midpoint is meaningful (e.g., zero).
- **Series colors** — distinguishable, colorblind-safe, limited in number.
- **Heatmaps** — clustered rows/columns when meaningful; always include a color scale.

---

## 4. Uncertainty visualization

Several approaches, each surfacing uncertainty differently:

### Error bars
Simple. Indicate a summary of uncertainty (usually 1 SD, 1 SEM, or 95% CI). Fail: readers often can't distinguish which, and interpretation differs significantly.

### Confidence bands (shaded regions)
Around a fitted line or trend. Intuitive for time series and regression lines.

### Hypothetical outcome plots (HOPs)
Animation showing draws from the posterior or bootstrap distribution. Matthew Kay, Jessica Hullman's research.

### Quantile dotplots
A distribution shown as 20 (or 50, or 100) dots, each representing an equal share of the probability mass. Often easier to reason with than density plots for laypeople.

### Fan charts
Shaded probability cones for forecasts. Bank of England inflation charts.

### Violin plots
Density shape visible at each category. Useful when distribution shape matters, not just center.

### Posterior distributions
Full Bayesian posteriors, often shown with 50% and 95% credible intervals and a median line.

### Error ellipses
Two-dimensional uncertainty; common in astrophysics and GIS.

---

## 5. Scientific diagrams and models

Beyond charts — diagrams that represent mechanism, process, or structure.

### Biology

- **Pathway diagrams** — biochemical cascades, signal transduction. KEGG, Reactome.
- **Gene regulatory networks** — nodes for genes, edges for regulation.
- **Phylogenetic trees** — evolutionary relationships. Various formats (rectangular, radial, unrooted).
- **Protein structure** — ribbon diagrams, surface renderings, cartoons. PyMOL, VMD.
- **Cell diagrams** — stylized cell cross-sections showing organelles.
- **Ecosystem food webs** — trophic networks.

### Physics

- **Feynman diagrams** — particle interactions; conventions for incoming/outgoing, virtual particles, vertices.
- **Spacetime diagrams** — events in 2D (space + time) with light cones.
- **Circuit diagrams** — electrical symbols with standardized conventions.
- **Phase diagrams** — states of matter as functions of pressure/temperature.
- **Penrose diagrams** — causal structure of spacetime.

### Chemistry

- **Structural formulas** — Lewis dot, line-angle, ball-and-stick, space-filling.
- **Reaction mechanisms** — curved arrows showing electron movement.
- **Spectra** — NMR, IR, mass spec conventions.

### Earth & atmospheric science

- **Weather maps** — isobars, fronts, stylized symbols for phenomena.
- **Geological cross-sections** — pattern fills for rock types; fault indicators; fold symbols.
- **Stratigraphic columns** — vertical representation of geological layers.
- **Topographic maps** — contour lines with labeling conventions.

### Mathematics

- **Commutative diagrams** (category theory).
- **Venn and Euler diagrams** — set relationships.
- **Knot diagrams** — over/under conventions.
- **Graph theory visualizations** — nodes and edges with algorithmic layout.
- **Geometric constructions** — compass and straightedge conventions.

### Engineering

- **Exploded views** — components separated with connecting lines showing assembly.
- **Flowcharts and P&IDs** (process and instrumentation diagrams) — standardized symbols for valves, tanks, instruments.
- **Block diagrams** — systems represented as blocks with typed connections.

---

## 5b. Field-specific figure conventions

Building on §5 above — specific figure traditions with stable visual grammars worth honouring (or violating knowingly).

### Feynman diagrams (particle physics)

A graphical calculus for particle interactions. Each line and vertex has a meaning fixed by convention.

- **Lines.** Solid arrowed lines for fermions (electrons, quarks); wavy lines for photons; helical lines for gluons; dashed lines for scalar bosons; double lines for ghosts. Arrows on fermions distinguish particle from antiparticle.
- **Time direction.** Some authors run time left-to-right, others bottom-to-top. Declare the convention once; do not mix within a paper.
- **Vertices.** Where lines meet; each vertex carries a coupling constant. Vertex types are theory-specific (QED has one type; the Standard Model has many).
- **External lines (incoming/outgoing).** External lines extend off the diagram; internal lines (virtual particles) connect vertices. Internal momentum is integrated over.
- **Loops.** Closed paths of internal lines; each loop contributes a factor of `1/(4π)²` and an integration; loop count is the order in perturbation theory.

Feynman diagrams are simultaneously *pictures* and *equations*. The figure is the calculation; the prose explains the physics.

### Organic chemistry mechanism diagrams

The curved-arrow mechanism (introduced by Robinson, formalised by Ingold) is the dominant figure type in organic chemistry.

- **Curved arrows.** Full arrow head (→) for two-electron movement; half-arrow / fishhook (⇀) for one-electron (radical) movement. The tail starts at the source (a bond or a lone pair); the head ends at the destination (a new bond position or an atom).
- **Reaction conditions** over the arrow: solvent, temperature, catalyst, additional reagents. *"H₂SO₄, Δ"* over the arrow means *"with sulfuric acid, heated."*
- **Stereochemistry.** Wedge (▲) for bonds projecting toward the viewer; dash (▼) for bonds projecting away; in-plane bonds drawn as plain lines. *R/S* and *cis/trans* descriptors italicised.
- **Lone pairs.** Drawn as paired dots when the mechanism uses them; omitted otherwise. Showing all lone pairs always is pedagogically defensible; in research papers, only the mechanistically relevant ones appear.
- **Resonance.** A double-headed straight arrow ↔ between resonance structures; *not* an equilibrium arrow ⇌, which means something different.

The mechanism diagram *is* the explanation; readers parse the arrow flow before they parse the prose.

### Phylogenetic trees

Trees representing evolutionary relationships. Multiple equivalent forms.

- **Rectangular cladogram.** Right-angle branches; tips align; branch lengths uninformative. Used when topology is the focus.
- **Rectangular phylogram.** Same shape, but branch lengths scaled to evolutionary distance (substitutions per site, or time). Branch-length is data.
- **Radial / circular tree.** Tips arranged on a circle; useful for large trees where rectangular layouts become unreadable.
- **Unrooted tree.** No defined root; useful for showing relationships without a directional ancestor.
- **Time-scaled tree.** Branch lengths in calendar time; common in molecular epidemiology (SARS-CoV-2 phylogenies).
- **Bootstrap support values.** Numbers (0–100 or 0–1) at internal nodes, indicating confidence in the branching pattern. Convention: show values < 70 as unsupported (lower-confidence) or collapse them.
- **Taxon names at tips.** Italicised for species; upright for higher taxa; *"Homo sapiens"* italicised, *"Hominidae"* upright.
- **Time axis.** Geological-period bars below the tree for deep-time phylogenies; calendar dates for recent (molecular-epidemiology) trees.

### SBGN (Systems Biology Graphical Notation)

A standardised graphical language for biological networks, with three languages:

- **Process Description (PD)** — biochemical pathways as bipartite graphs of state-nodes (substances) and process-nodes (reactions, transports, modifications).
- **Entity Relationship (ER)** — interactions between molecular entities, including modulations and inhibitions.
- **Activity Flow (AF)** — signalling cascades as influences between activities.

Each language has stable glyphs: small molecules as circles, proteins as rounded rectangles, complexes as rectangles with rounded corners, reactions as small squares, processes as arrows of specific shapes. The convention is published (sbgn.github.io); software (CellDesigner, yEd) supports it.

Apex pathway figures in *Cell*, *Nature*, and major systems-biology journals increasingly conform to SBGN. Hand-drawn pathway figures with novel glyph vocabulary now read as undisciplined.

### Signalling cascade diagrams

A subset of mechanism diagrams specific to cell-biology signalling.

- **Nodes.** Receptors as transmembrane shapes spanning a horizontal line representing the membrane. Kinases as rounded rectangles; transcription factors as rounded shapes inside the nucleus; small molecules as circles.
- **Edges.** Arrows for activation; bar-headed lines (⊣) for inhibition; dashed lines for indirect effects.
- **Compartments.** A horizontal line for the cell membrane; a second oval for the nucleus; cytoplasm between. Diffusion barriers are part of the figure.
- **Phosphorylation events.** *P* in a circle attached to the kinase target; multiple phosphorylations stacked.
- **Translocation.** Arrows crossing compartment boundaries; sometimes annotated with the trafficking mechanism (active, passive, vesicular).

Sources: Kanehisa's KEGG pathway maps; the Reactome database visualisations; *Nature Reviews Molecular Cell Biology* figure standards.

---

## 6. Scientific notation systems (selected, not exhaustive)

Different fields have different conventions. A few exemplars:

- **Chemistry** — IUPAC nomenclature; standard structural drawing conventions
- **Physics** — SI units; specific conventions per subfield (four-vector notation in relativity, bra-ket in quantum)
- **Mathematics** — specific to area (∀, ∃ in logic; ⊗, ⊕ in linear algebra; ∫, ∂ in analysis)
- **Genetics** — gene names italicized, protein names upright; species-specific conventions
- **Astronomy** — coordinate systems (equatorial, galactic); magnitude scales; spectral classification
- **Linguistics** — IPA (International Phonetic Alphabet); tree diagrams for syntax
- **Music** — staff notation with clef, time, key signatures

A scientific artifact should use the conventions of the field it's addressing. Violating conventions without reason signals unfamiliarity.

---

## 7. The lab notebook tradition

Working notes distinct from published papers. Long tradition in science.

**Features:**
- Dated entries
- Experimental protocols, deviations noted
- Raw observations alongside interpretations
- Hypothesis, prediction, result, updated belief
- Failed experiments preserved (valuable data)
- Marginal sketches and drawings

**Contemporary digital forms:**
- Observable notebooks
- Jupyter lab notebooks
- Benchling for biology
- LabArchives
- RSpace

**Exemplars:**
- Darwin's notebooks (digitized at Cambridge)
- Leonardo da Vinci's notebooks
- Marie Curie's lab notebooks (still slightly radioactive)
- Richard Feynman's notebooks

---

## 8. The scientific poster

A specialized genre. Conventions:

- **Size** — commonly 36×48" or A0
- **Title strip at top** — large, with authors and affiliations
- **Abstract / summary** at upper left
- **Methods, results, discussion** flowing in columns
- **One clear "take-home" figure** that carries the main result
- **QR code / URL** for paper or supplementary material
- **Minimal text** — the poster is for a glance; the presenter elaborates in conversation

---

## 9. Scientific visualization color systems

Contemporary recommendations:

- **Sequential** — viridis, magma, inferno, plasma, cividis (perceptually uniform, colorblind-safe)
- **Diverging** — RdBu, PuOr, PRGn; Moreland's cool-to-warm
- **Categorical** — Paul Tol's palettes; Okabe-Ito palette; D3's Category10 (but with care)
- **Qualitative with constraints** — cmap, Glasbey

Avoid:
- **Jet / rainbow** (pre-2014 Matlab default) — not perceptually uniform
- **HSV** rotation without calibration
- Default Matplotlib (before viridis became default) — Jet was hostile

See `references/libraries/color-library.md` for the full color space.

---

## 10. Scientific writing style

Ethos:

- **Precision over flourish.** A well-calibrated claim beats a rhetorical one.
- **Falsifiability implicit.** The claim's shape should suggest how it could be wrong.
- **Generality appropriate to the evidence.** Don't overclaim; don't underclaim.
- **Others' work cited in good faith.** Misrepresenting cited work is an ethical failing.
- **Acknowledgment of limitations.** Present, specific, not hand-waved.

Voice:

- Passive voice has a scientific tradition ("the sample was treated with"); active voice is increasingly preferred ("we treated the sample with").
- First-person plural ("we") is standard even for single-author papers in some fields.
- Third person ("the researchers") common in some sub-disciplines.

---

## 11. The replication crisis and responses

Methodological rigor is itself a subject of scientific conversation.

- **Pre-registration** — committing to analysis plan before data collection
- **Registered reports** — peer review of protocol before data collection
- **Open data, open code** — computational reproducibility
- **Multi-lab collaborations** — Many Labs projects, ManyBabies, ManyPrimates
- **Effect size reporting** — alongside or instead of p-values
- **Bayesian reasoning** — priors made explicit; posteriors reported
- **Robustness analyses** — specification curves, multiverse analyses

A contemporary scientific artifact should engage with these when relevant, not ignore them.

---

## 12. Exemplars worth studying

- **Nature, Science, Cell, NEJM, PNAS, Physical Review Letters, Journal of the ACM** — reference journals
- **Distill.pub** — interactive scientific publication (dormant)
- **Our World in Data** — reference for data-journalism-science hybrid
- **3Blue1Brown** (Grant Sanderson) — mathematical visualization
- **SciShow / PBS Digital Studios** — video explainers
- **Kurzgesagt** — high-production science explainers
- **xkcd What-If?** (Randall Munroe) — applied-physics what-ifs
- **Quanta Magazine** — see `tear-downs/08-quanta-magazine.md`
- **Richard Feynman's *Lectures on Physics*** — the reference for pedagogical scientific writing
- **E. O. Wilson, Stephen Jay Gould** — popular biology essay traditions
- **Stephen Hawking's *A Brief History of Time*** — for lay audiences
- **Oliver Sacks** — clinical neuroscience as humanistic essay

---

## 15. Citation conventions across scientific fields

Citation style is field-specific. The dominant styles, where each applies, and how to render them in HTML are catalogued in `references/medium-playbooks/math-notation.md` under "Citation conventions" — refer there for the full table.

Summary mapping for scientific artifacts:

- **Vancouver / AMA** — clinical medicine (NEJM, JAMA, BMJ, *Lancet*; most medical specialties). Superscript numerical references.
- **CSE Name-Year** — biology, ecology, much of the natural sciences. Author-year inline; alphabetical reference list.
- **APA 7th** — psychology, behavioural science, education, parts of biomedicine. Author-year inline.
- **ACS** — chemistry (American Chemical Society journals). Numerical or italic-superscript.
- **IEEE** — engineering, computer science, electrical engineering. Bracketed numbers `[1]`.
- **Nature style** — *Nature* journals and others. Superscript numerical; specific reference formatting.
- **AIP / APS** — physics (American Institute of Physics; American Physical Society). Numerical, with specific journal-abbreviation conventions.

When the artifact is published, the journal's "Instructions for Authors" is authoritative. When the artifact is independent (preprint, blog post, explainer), pick the style of the discipline whose readers the artifact targets, and use it consistently. Mixing styles within an artifact is the tell of a non-fluent author.

Specific scientific-publication conventions to honour:

- **DOIs as the canonical link.** Every citable work has a DOI; use it. URLs to publisher pages rot; DOIs do not.
- **Preprints cited with explicit version.** *"Smith et al., 2024, bioRxiv, doi:10.1101/... (v2, accessed 2026-03-15)"* — preprints are revised; cite the version.
- **Data citations.** Datasets get DOIs (Dryad, Figshare, Zenodo). Cite the dataset DOI, not just the paper that used it.
- **Software citations.** Tools and packages get citations too. Astropy, scikit-learn, NumPy all have specific recommended citations on their project pages.
- **Pre-registrations.** When the analysis was pre-registered (OSF, AsPredicted), cite the pre-registration alongside the paper.

---

## 13. Cross-references

- `references/libraries/medical-artifacts.md` — medical subset of scientific communication
- `references/libraries/visualization-grammar.md` — chart forms for scientific data
- `references/libraries/rhetorical-atlas.md` — IMRAD and other academic structures
- `references/libraries/color-library.md` — colormaps for scientific visualization
- `references/libraries/dataset-corpus.md` — data shapes common in science
- `references/medium-playbooks/math-notation.md` — notation rendering
- `references/medium-playbooks/notebook.md` — computational notebook specifics
- `references/tear-downs/04-distill-attention.md` — interactive scientific publication
- `references/tear-downs/08-quanta-magazine.md` — science journalism

---

## 14. Extending this library

Add when:
- A field has distinct publication, figure, or notation conventions not yet covered
- New reproducibility or uncertainty-visualization practices deserve reference
- Notable exemplars or traditions merit inclusion

Avoid:
- Discipline-specific technical specifications (those live in the field's literature)
- Generic "scientific aesthetic" claims without specific tradition

The goal: a library wide enough that scientific-artifact creators have genuine creative choices within the conventions of their field — and can break conventions knowingly.

---

## 16. The Statistical Analysis Plan as commitment device

The Statistical Analysis Plan (SAP) is the document that pre-specifies, in granular detail, how a trial's data will be analysed before the analyst sees an unblinded number. Its function is *not* statistical (the analytic choices it records are mostly conventional); its function is *epistemic* — it is a commitment device that closes the garden of forking paths. The SAP is signed, dated, version-controlled, and locked before unblinding. Once locked, every analytic choice is documented; deviations require an addendum that names the deviation and the reason.

ICH E9 *Statistical Principles for Clinical Trials* (the 1998 harmonised tripartite guideline) and its 2019 addendum E9(R1) on estimands frame the SAP as a load-bearing regulatory document. The estimand framework — population, treatment, outcome variable, intercurrent-event handling, summary measure — is now the canonical scaffold for SAP construction; pre-2019 SAPs that omit estimand specification are increasingly read as incomplete.

The gap between a SAP-locked-before-unblinding analysis and an exploratory post-hoc analysis is not statistical mechanics — the same Cox regression, the same logistic model — but evidentiary weight. The first answers a question the trial was designed to answer; the second answers a question the data happened to permit. Apex trial reports distinguish them visibly: confirmatory analyses in the main figures, prespecified secondary analyses in a clearly-labelled section, exploratory analyses in a third section with explicit *"hypothesis-generating, not confirmatory"* annotation.

**Apex deployment.** Lewis (*BMJ* 2018;364:l175) — *"Statistical analysis plans: writing and version control"* — is the canonical methodological primer. The Trials Master File at most academic CTUs (Clinical Trials Units) requires SAP version 1.0 signed before first-patient-first-visit; subsequent versions are tracked with a changelog; the final locked version is the document the analyst follows verbatim. SPIRIT-Outcomes 2022 extension specifies SAP-related items required at protocol-publication time.

**Anti-patterns.** *"The SAP was written after the data were locked"* (the SAP-as-afterthought pattern; see F-mode S17). *"The primary endpoint was changed because the original was negative"* (outcome-switching; see S16). *"Multiplicity correction was applied informally"* (silent dropping of pre-specified secondary endpoints when they would have triggered correction). *"Subgroup analyses are reported but were not pre-specified"* (post-hoc subgroups dressed as planned). The COMPare Trials project (Goldacre *et al.*, *Trials* 2019) documented outcome-switching in 58 of 67 consecutive top-five-journal RCTs; the failure mode is systemic, not exotic.

**The reproducibility hook.** A locked SAP plus the analysis code that implements it is a far stronger reproducibility statement than either alone. The SAP says *what was planned*; the code says *what was run*; agreement between them is what makes the analysis trustworthy. Increasingly, journals (notably *BMJ Open*, *PLOS Medicine*) require SAP publication alongside the protocol; *NEJM* requires SAP availability as a supplement for industry-sponsored trials.

**Where the SAP-as-artifact discipline transfers.** Beyond clinical trials: pre-specified analysis plans for observational studies (the AsPredicted convention; see §18), pre-specified models for machine-learning benchmarks (the *holdout-test-set-once* discipline), pre-specified hypotheses for psychology and economics experiments (the Open Science Framework registration). The artifact's name varies; the commitment-device function is the same.

---

## 17. Data dictionaries as audit-grade artifacts

The data dictionary is the document that names every variable in the dataset, defines its type, specifies its allowed values, and cross-references its source. In clinical research the dominant standard is CDISC SDTM (Study Data Tabulation Model) controlled terminology — a hierarchy of domains (DM for demographics, AE for adverse events, LB for labs, VS for vital signs, EX for exposure, CM for concomitant medications), each with required variables, controlled vocabularies, and value-level metadata. SDTM is the format the FDA expects for clinical-trial data submissions; the FDA's *Study Data Technical Conformance Guide* is the operational specification.

The reviewer's perspective is the calibrating audience. An FDA statistical reviewer opening a submission expects: every variable in the analysis dataset traceable to a CRF (Case Report Form) field; every derivation specified in a *define.xml* document; every controlled-terminology value drawn from a published CDISC codelist or a sponsor-specific extension that is itself documented. The reviewer's failure mode — *"I cannot tell what this variable represents"* — is the failure mode the data dictionary exists to prevent.

The aphorism *"if it's not in the data dictionary, the analyst guessed"* names the underlying discipline. A variable named `BMI` without a dictionary entry could be calculated from weight-in-kg-over-height-in-metres-squared (the standard) or from weight-in-pounds-over-height-in-inches-squared-times-703 (the US clinical formula); the analyst who used it has chosen one; the reviewer cannot verify which. A categorical variable for race coded as `1, 2, 3, 4, 5` without a value-label mapping is uninterpretable; the analyst who reported subgroup analyses on it has assumed a mapping the dictionary does not assert.

**Apex deployment.** The CDISC SDTM Implementation Guide (current version 3.4) specifies variable naming conventions (≤ 8 characters, domain-prefixed: `DMAGE`, `LBSTRESN`, `AESEV`), permitted/required/expected status for each variable, and standard terminology drawn from the NCI Enterprise Vocabulary Services. The ADaM (Analysis Data Model) layer sits above SDTM and specifies derived variables for analysis; an ADaM dataset with a complete *define.xml* and an analysis-results metadata file lets a reviewer reproduce every analysis from the locked datasets without sponsor support.

**Beyond clinical trials.** The discipline transfers to any audit-bearing dataset: REDCap data dictionaries for IRB-approved observational studies; the Frictionless Data tabular-data-package specification for open-data publications; the *codebook* in survey research (Stata's `codebook` command, R's `labelled` package, Python's `pandas-profiling`); the schema documentation for an OMOP Common Data Model deployment.

**Anti-patterns.** *"The data dictionary will be added at submission"* (it will not; the analysis was already done without it). *"Variable names are self-explanatory"* (the reviewer who has not lived with the data does not find them self-explanatory). *"We follow CDISC standards"* without conformance reports (Pinnacle 21 is the standard validator; its output is the evidence of conformance). *"Free-text fields where coded fields exist"* (an `AE_TERM` field with *"headache"*, *"HA"*, *"head ache"*, *"head pain"* as four distinct values defeats every downstream analysis; MedDRA preferred-term coding is the fix).

**The audit-grade test.** Hand the dataset and the dictionary to an analyst who has never seen the study. Can they reproduce the published primary analysis from the dictionary alone, without speaking to the original analyst? If yes, the dictionary is audit-grade. If no, the dictionary is incomplete and the analyses that depend on its tacit knowledge are not independently verifiable.

---

## 18. Preregistration as the falsifiability covenant

Preregistration is the act of publicly specifying a study's hypothesis, design, and analytic plan before data collection (or, at minimum, before data inspection). Its Popperian framing is exact: a hypothesis is scientific only insofar as it is falsifiable, and a hypothesis whose form can be adjusted *after* the data are in is no longer falsifiable in any operational sense. Preregistration converts the hypothesis from a flexible narrative into a public commitment whose falsifiability is enforceable by third parties.

Karl Popper's *The Logic of Scientific Discovery* (1934, English 1959) articulated the principle; the contemporary infrastructure that operationalises it dates from the 2010s, in response to the replication crisis. The three dominant platforms:

- **Open Science Framework (OSF) Preregistration** — Centre for Open Science (Charlottesville, VA). The most flexible platform; supports preregistration templates ranging from highly structured (the AsPredicted-equivalent OSF Standard Preregistration) to fully customised. Time-stamped, citable with DOI, optionally embargoed (released only when the paper is submitted). The OSF Registries currently host > 100,000 registrations across disciplines.
- **AsPredicted** — Wharton Credibility Lab, Pennsylvania. A deliberately minimal nine-question template: *Have data been collected? What's the hypothesis? What's the dependent variable? What are the conditions? What's the analysis plan? What's the rule for excluding observations? How many observations? Any other pre-registered information? Have you previously analysed this data?* The brevity is the design: a researcher who cannot answer the nine questions concisely is not ready to preregister.
- **Registered Reports** — the strongest form. The study's introduction, methods, and analysis plan are peer-reviewed *before* data collection; if accepted in principle (Stage 1), publication is guaranteed regardless of the result. The form, introduced by *Cortex* under Chris Chambers (2013) and now offered by > 300 journals, eliminates publication bias by definition. The result is not a guarantee of replication but a guarantee that the analysis tested what it claimed to test.

Nosek *et al.* (*Proc Natl Acad Sci USA* 2018;115:2600), *"The preregistration revolution"*, is the canonical methodological argument: preregistration distinguishes confirmatory tests (those the data have not yet seen) from exploratory analyses (those the data have generated); both are valuable; only the first earns the inferential strength that significance testing assumes. The paper's section on the difference between *prediction* and *postdiction* is the conceptual core.

**Apex deployment.** The preregistration is *specific* — the test is named (*"two-sample t-test of mean RT between high- and low-load conditions"*), the inclusion criteria are operational (*"trials with RT > 200 ms and < 3 SD above the participant mean"*), the analysis script is committed to a public repository at the time of registration. The published paper labels every analysis: *Confirmatory* (matches preregistration), *Robustness* (variations on the confirmatory analysis), *Exploratory* (post-hoc; reported without inferential weight). Deviations from the preregistration are listed in a *"Deviations from preregistered analysis"* section, not hidden.

**Anti-patterns.** *"The preregistration was vague enough that any result confirmed it"* (see F-mode S20). *"We preregistered after a pilot"* (the data have already shaped the hypothesis). *"The preregistration mentions five analyses; we report the one that worked"* (selective reporting against a preregistration is worse than no preregistration, because it weaponises the credibility-signal). *"Time-stamping was post-hoc"* (the registration date is auditable; the *cynic's check* is *"would this preregistration have predicted the published result before the data were in?"*).

**Where the falsifiability covenant transfers.** Beyond psychology and biomedicine: economics (the AEA Registry for randomised trials in economics); political science (EGAP — Evidence in Governance and Politics); ecology (PREreg Reviewer's Award via *PCI Ecology*); machine learning (the increasingly-common *"frozen test set"* discipline, in spirit). The platform varies; the covenant is the same.

---

## 19. Reproducibility-as-aesthetic

The literate-analysis tradition treats the analysis document — the notebook, the Rmarkdown file, the Quarto document — as a single artifact in which prose, code, output, and figures share a substrate. The tradition's intellectual ancestor is Knuth's *Literate Programming* (Knuth, *Comput J* 1984;27:97), which proposed that programs be written as documents for humans, with the code as a secondary extraction. The contemporary scientific instantiation — `knitr`, RMarkdown, Jupyter, Quarto, Pweave, Org-mode Babel — extends Knuth's vision: the analysis is a document, the document is the analysis, and rebuilding the document re-runs the analysis.

The aesthetic claim is not decorative. A literate analysis is *reproducible by construction*: there is no separate codebase, no manual figure export, no copy-paste of numbers into prose. The numbers in the prose are inline expressions evaluated at render time; the figures in the document are generated by the chunks that precede them; the random seed is set in the first chunk and propagates. When the analysis changes, the document re-renders and every dependent figure, table, and inline number updates. The discipline that makes this possible is itself the aesthetic — the artifact's surface texture is the visible signature of its underlying rigor.

**The contemporary R stack.** Wickham & Çetinkaya-Rundel's *R for Data Science* (2nd edition, 2023; O'Reilly) is the canonical introduction; the book itself is a Quarto book and ships as a worked exemplar of its own argument. The stack:

- **`renv`** (Ushey & Wickham) — project-local package library; `renv.lock` records exact package versions; `renv::restore()` reproduces the library on a fresh machine. Replaces the *"works on my machine"* failure mode with a verifiable manifest.
- **`here`** (Müller) — project-relative paths; `here::here("data", "raw", "ballots.csv")` resolves from the project root regardless of where the script is run from. Eliminates the broken-when-rendered-from-elsewhere class of bug.
- **`targets`** (Landau) — a pipeline framework for R; tracks dependencies between analysis steps; re-runs only what changed; supports parallel execution. The R-world successor to `make` for analysis workflows.
- **Quarto** — Posit's successor to RMarkdown; multi-language (R, Python, Julia, Observable JavaScript); multi-output (HTML, PDF, slides, books, websites); native cross-references, citations, figure-numbering. The default rendering target for new literate-analysis projects.

Çetinkaya-Rundel's pedagogy papers — notably *"From data to viz to plot in 10 minutes"* (Çetinkaya-Rundel & Ellison, *J Stat Educ* 2021;29:67) and the broader Duke/OpenIntro curriculum — operationalise the literate-analysis stack at undergraduate scale; every assignment is a Quarto file; submissions are rendered HTML with embedded code chunks; grading is against the rendered artifact, which means students cannot submit numbers their code did not produce.

**The aesthetic markers.** A literate-analysis artifact is recognisable: prose paragraphs interleave with monospaced code chunks; output appears immediately below the chunk that produced it; figures carry captions cross-referenced from the prose (*"see Figure 3"*); the session info appears in an appendix (`sessionInfo()` or `sessioninfo::session_info()` in R; `watermark` in Python); the rendered document includes a build timestamp and a Git commit hash. These are not decoration; each is a visible witness to a reproducibility commitment.

**Anti-patterns.** *"The figures are exported PNGs"* (the chunk that produced them is no longer linked; if the data update, the figures do not). *"The Rmarkdown renders but the script does not run"* (rendering swallowed an error chunk's output; the analysis is silently broken). *"`install.packages()` calls scattered throughout"* (no package version pinning; the analysis is the package versions at render time, which are not the package versions at write time).

**Where the aesthetic transfers.** The literate-analysis discipline applies wherever an analysis produces a document for human readers: epidemiology surveillance reports (CDC's MMWR is increasingly Quarto-rendered); business analytics (the dbt + Quarto combination at data-mature companies); machine-learning experiment tracking (Quarto + MLflow); even policy briefs (the World Bank's PovcalNet uses literate documents for its global-poverty estimates). The medium is the message: a document that re-runs is a document that can be trusted.

---

## 20. Cover-letter discipline

The cover letter to a journal editor is a single-page artifact whose audience is *one person* — the handling editor — and whose job is to convince that person to send the manuscript out for review. It is not a marketing brochure; it is not a précis; it is not a victory lap. It is an editorial pitch to an editor.

The single-page maximum is structural. A cover letter that runs to two pages is signalling that the author cannot distinguish what matters from what merely happened. The editor of a major journal handles dozens of submissions a week; the cover letter that does not communicate its central claim in the first paragraph will not have its second paragraph read.

**The four moves, in order.**

1. **The headline claim.** One sentence. *"We report the first randomised trial demonstrating that early administration of [drug X] reduces 90-day mortality in [condition Y]; the absolute risk reduction was 8.4 percentage points (95% CI 4.1–12.6, p = 0.0003)."* The editor learns the finding before the format.
2. **Why this journal.** One short paragraph. The fit to the journal's readership; the connection to a recent editorial or thematic series; the kind of advance the work represents (definitive, hypothesis-generating, methodological). Generic *"we believe your readers will find this interesting"* is the marker of a letter the editor will not finish.
3. **What is novel and what is solid.** One short paragraph. Not a results recap — the abstract does that. A *positioning* paragraph: what was known, what is new, what is now resolved. The editor wants to know whether the manuscript would *change practice* or *change the field*.
4. **Compliance items.** Conflict of interest, prior dissemination, suggested and excluded reviewers, ethics and registration statements. Brief, accurate, complete.

Henry Gee, *Senior Editor for Communications and Senior Editor for Palaeontology, Nature* (1987–2022), in *The Accidental Species* (2013) and his *Nature* columns over three decades, repeatedly named the cover letter as the single most under-respected artifact in the submission process. His operational summary: *"Tell me, in plain English, why this paper matters enough that I should spend an hour of editorial time on it."*

The editor-of-Nature memoir tradition — Gee's writings, John Maddox's *What Remains to Be Discovered* (1998), Philip Campbell's editorial-page columns 1995–2018 — shares a refrain: the cover letter is read before the abstract; if it does not earn the abstract a reading, the abstract will not be read.

**Apex deployment.** The letter opens with the headline finding stated as a finding, not as a description (*"We show that…"*, not *"This paper concerns…"*). The journal-fit paragraph names a specific recent paper or editorial; the novelty paragraph is concrete (*"prior work [refs] established the association; this trial establishes causation"*); the compliance section is the *bottom* of the letter, not the top. The letter is signed by the corresponding author with a single contact email.

**Anti-patterns.** *"We are delighted to submit…"* (the editor does not care about your delight; see also F-mode F2). *"This is the first study to…"* applied loosely (the editor will check). Adjective stacks (*"groundbreaking, transformative, paradigm-shifting"*) — the editor reads these as compensation for thin findings. Paragraphs that recap the methods (the manuscript already does this). Letters that exceed one page (see F-mode S19).

**Where the discipline transfers.** Grant cover sheets to NIH (the cover sheet is shorter still; see `medium-playbooks/grant-application.md`); editor pitches to magazines (Quanta, Atlantic, Wired science desks expect one-page pitches with the same four-move structure); preprint server submission notes; conference-abstract title-and-abstract pairs (where the title carries the cover-letter function). The audience is always one editor; the constraint is always brevity; the artifact is always the pitch.

---

## 21. The Equator Network ecosystem

The Equator Network (Enhancing the QUAlity and Transparency Of health Research; equator-network.org, headquartered at the University of Oxford) catalogues the reporting-checklist landscape for health research. As of the 2024 update, the database lists more than 450 distinct reporting guidelines spanning trial designs, observational studies, diagnostic accuracy, systematic reviews, qualitative research, economic evaluation, mixed methods, animal research, real-world evidence, and machine learning. The ecosystem's design principle: each study type has a reporting framework whose items are the minimum information a reader needs to evaluate the work.

The major frameworks, the study types they cover, and the canonical citations:

- **CONSORT** (Consolidated Standards of Reporting Trials) — randomised controlled trials. Schulz, Altman, Moher, *BMJ* 2010;340:c332. 25 items plus the four-tier flow diagram (already specified in `visualization-grammar.md` § Clinical and epidemiological). Extensions: CONSORT-NPT (non-pharmacologic treatments), CONSORT-PRO (patient-reported outcomes), CONSORT-Cluster (cluster-randomised trials), CONSORT-AI (AI interventions), CONSORT-Outcomes 2022.
- **STROBE** (Strengthening the Reporting of Observational studies in Epidemiology) — cohort, case-control, cross-sectional studies. von Elm *et al.*, *Lancet* 2007;370:1453. 22 items; extensions for molecular epidemiology (STROBE-ME), genetic association (STREGA), nutritional epidemiology (STROBE-nut).
- **PRISMA** (Preferred Reporting Items for Systematic reviews and Meta-Analyses) — systematic reviews and meta-analyses. Page *et al.*, *BMJ* 2021;372:n71 (PRISMA 2020 update). 27 items plus the four-tier flow diagram. Extensions: PRISMA-IPD (individual participant data), PRISMA-NMA (network meta-analysis), PRISMA-DTA (diagnostic test accuracy reviews), PRISMA-S (search reporting), PRISMA-ScR (scoping reviews).
- **SPIRIT** (Standard Protocol Items: Recommendations for Interventional Trials) — clinical trial protocols. Chan *et al.*, *Ann Intern Med* 2013;158:200. 33 items; the protocol-stage counterpart to CONSORT.
- **STARD** (Standards for Reporting of Diagnostic Accuracy Studies) — diagnostic accuracy studies. Bossuyt *et al.*, *BMJ* 2015;351:h5527. 30 items.
- **CARE** (CAse REport guidelines) — case reports. Gagnier *et al.*, *J Med Case Rep* 2013;7:223. 13 items; the structured-case-report counterpart to CONSORT.
- **TRIPOD** (Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis) — prediction models. Collins *et al.*, *BMJ* 2015;350:g7594. Update TRIPOD+AI in 2024 for machine-learning prediction models.
- **CHEERS** (Consolidated Health Economic Evaluation Reporting Standards) — economic evaluations. Husereau *et al.*, *BMJ* 2022;376:e067975 (CHEERS 2022 update).
- **SRQR / COREQ** — qualitative research (Standards for Reporting Qualitative Research; Consolidated criteria for Reporting Qualitative Research).
- **ARRIVE 2.0** — animal research. Percie du Sert *et al.*, *PLOS Biol* 2020;18:e3000410.

The ecosystem is not a single document but a *culture*. A journal editor who receives a cluster-randomised trial without a CONSORT-Cluster checklist annotated to the manuscript reads it as a procedurally-deficient submission; a methodologist asked to peer-review a prediction-model paper opens TRIPOD before reading the methods section. The checklists are the shared vocabulary of methodological review.

**The "use-the-right-framework" discipline.** The most common Equator failure is *framework-mismatch* — a cohort study reported with CONSORT, a diagnostic-accuracy study reported with STROBE, a systematic review reported with the general structured-abstract framework rather than PRISMA. The Equator website's *"find the guideline"* tool maps study design to framework; the mapping is the first step before drafting begins.

**Apex deployment.** The published paper includes the completed checklist as a supplementary file, with each item annotated by page and paragraph. The flow diagram (CONSORT, PRISMA) appears in the main text as the first or second figure. The deviations from the framework are explicit (*"item 19 not applicable because…"*) rather than silent. The reader who wants to verify the report's completeness has everything they need.

**Anti-patterns.** *"We followed CONSORT"* without an annotated checklist (claim without evidence). The checklist completed *after* the manuscript is written (the framework's items did not shape the writing; gaps reveal themselves only when an external reviewer applies the checklist). A flow diagram drawn from memory rather than from the published template (boxes missing, denominators not reconciling). Mixing reporting frameworks within a single paper (CONSORT for the main trial, STROBE for the registry analysis, with no acknowledgement that the same paper uses two frameworks).

**Where the ecosystem is going.** The 2020s have seen rapid extension into AI-augmented research (CONSORT-AI, SPIRIT-AI, TRIPOD+AI, DECIDE-AI for clinical AI evaluation), real-world evidence (RECORD, RECORD-PE for pharmacoepidemiology in routinely-collected data), and translational research (the BRISQ framework for biospecimen reporting). The ecosystem is the closest contemporary analogue, in scientific publishing, to a building code: not always-loved, frequently-violated, and yet the floor below which the work is not professional.

---

## 22. Trial protocols as 100-page argument structures

A clinical-trial protocol is the document that specifies, in advance and in detail, what a trial will do, to whom, with what, measuring what, and for how long. A modern Phase III protocol routinely runs 80–150 pages; the SPIRIT 2013 statement (Chan *et al.*, *Ann Intern Med* 2013;158:200; checklist in *BMJ* 2013;346:e7586) defines 33 items spanning administrative information, introduction, methods, ethics/dissemination, and appendices. The protocol is not a description of the trial — it is the *promise* the trial makes to its participants, its regulators, its IRB, its funders, and the scientific community.

The protocol-as-promise framing is operational, not metaphorical. Every participant's informed consent rests on the protocol's enrolment criteria, schedule of procedures, risk disclosures, and stopping rules. Every IRB's approval rests on the protocol's risk-benefit analysis and consent-process specification. Every regulatory filing (IND in the US, CTA in the EU/UK, CTN in Australia) rests on the protocol's mechanistic rationale and dose-justification. Every analysis runs against the protocol's pre-specified endpoints and analytic plan. If the protocol changes, every dependent promise must be re-negotiated — which is why version control is structural, not optional.

**The SPIRIT 2013 scaffold (selected items).**

- **Background and rationale (item 6a).** The clinical question, the prior evidence, the unmet need. This is the section that ICH GCP requires to justify why the trial is worth conducting at all.
- **Objectives and hypotheses (item 7).** The primary hypothesis stated as a falsifiable claim with a specified direction and effect size; secondary hypotheses listed and prioritised.
- **Trial design (item 8).** Parallel / crossover / cluster / factorial; superiority / non-inferiority / equivalence; the design choice constrains every downstream analysis.
- **Eligibility criteria (item 10).** Inclusion and exclusion criteria, operationalised. Each criterion is a binary check at screening; ambiguous criteria produce protocol deviations.
- **Interventions (item 11).** Dose, route, schedule, modifications for adverse events, prohibited concomitant medications. For surgical and behavioural interventions, the TIDieR framework (Hoffmann *et al.*, *BMJ* 2014;348:g1687) is the canonical operationalisation.
- **Outcomes (item 12).** Primary, secondary, exploratory. Each outcome has: a measurement instrument, a time point, a definition of analysis (mean change, proportion, time-to-event). The COMET (Core Outcome Measures in Effectiveness Trials) initiative catalogues consensus core outcome sets by disease area.
- **Sample size (item 14).** The power calculation, with assumptions named: expected effect size, variability estimate, alpha (one- or two-sided), power, attrition rate, multiple-comparison adjustment.
- **Recruitment (item 15).** The plan for reaching the sample size; recent FDA and EMA guidance increasingly requires explicit diversity-of-enrolment plans.
- **Sequence generation, allocation, blinding (items 16–17).** Randomisation method, stratification factors, allocation concealment mechanism, blinding of participants/clinicians/assessors/analysts.
- **Statistical methods (item 20).** Analysis populations (ITT, modified-ITT, per-protocol), primary analytic model, handling of missing data (multiple imputation? complete-case? sensitivity analyses?), interim analyses, multiplicity adjustment. This section is the protocol-level counterpart to the SAP (§16); the SAP elaborates and operationalises what the protocol specifies in summary.
- **Data monitoring (item 21).** DMC composition, frequency of review, charter reference, stopping rules (efficacy boundary à la O'Brien-Fleming; futility boundary; safety boundary).
- **Ethics, consent, confidentiality (items 24–27).** IRB approval, informed-consent process, protocol-amendment communication, ancillary care.
- **Dissemination (item 31).** Publication policy, authorship criteria, data-sharing plan, access to the full protocol.

**Protocol amendments and version control.** Amendments are the protocol's audit trail. A *substantial* amendment (one that changes participant safety, the primary endpoint, eligibility, or analytic plan) requires IRB re-review, regulatory re-notification, and sometimes re-consent of enrolled participants. A *non-substantial* amendment (clarifications, typo fixes) is logged but not re-reviewed. Every amendment is dated, version-numbered, signed, and tracked in the Trial Master File; the protocol header carries a version table showing each version's date and the substantive change. *"Protocol v3.0, 2026-01-15, see Appendix Z for changelog"* is the apex form; *"protocol updated"* without a version is the failure form.

**Anti-patterns.** *"The protocol was finalised after enrolment began"* (the trial was operating on something; that something was not the published protocol). *"Primary endpoint changed without amendment"* (the FDA's Form 1572 makes this a regulatory violation). *"The published paper's analysis differs from the protocol's analysis without explanation"* (the COMPare Trials project's bread and butter). *"Protocol available on request"* (the contemporary expectation is publication: *Trials* journal, *BMJ Open*, the trial's ClinicalTrials.gov record; protocols are now citable documents with DOIs).

**Where the discipline transfers.** Beyond pharmaceutical trials: device trials (IDE protocols under FDA 21 CFR 812); behavioural-intervention trials (the ORBIT model for early-phase behavioural development); pragmatic trials (PRECIS-2 framework for design positioning); platform and adaptive trials (Adaptive Designs CONSORT Extension — Dimairo *et al.*, *BMJ* 2020;369:m115). The protocol's 100-page argumentative weight is proportional to the commitment it underwrites: enrol participants, allocate funding, gate the analysis, defend the findings. A protocol that does not bear that weight has not done its job.

<!-- END: references/libraries/scientific-artifacts.md -->

---


<!-- BEGIN: references/libraries/snippet-cookbook.md -->

# Snippet Cookbook

A platter of **alternative approaches** to common patterns — not a canonical set. For most problems below, several approaches are shown with different aesthetics, interaction philosophies, or technical tradeoffs. The creator picks what fits *this* artifact, or invents a fourth approach informed by the three.

All examples target the Claude React artifact environment (see `references/medium-playbooks/claude-react-artifact.md` for the environment).

> See `references/how-to-use-this-system.md` for the platter principle.

---

## 1. Tabs — three approaches

### Approach A: underline-indicator tabs (editorial, restrained)

```tsx
const [active, setActive] = useState('overview');
const tabs = ['overview', 'method', 'findings', 'discussion'];

<div role="tablist" className="border-b border-stone-200 flex gap-6">
  {tabs.map((t) => (
    <button
      key={t}
      role="tab"
      aria-selected={active === t}
      onClick={() => setActive(t)}
      className={`pb-3 text-sm font-medium border-b-2 -mb-px transition-colors ${
        active === t
          ? 'border-stone-900 text-stone-900'
          : 'border-transparent text-stone-500 hover:text-stone-700'
      }`}
    >
      {t.charAt(0).toUpperCase() + t.slice(1)}
    </button>
  ))}
</div>
```

**Feel:** newspaper, editorial, reference-grade. The underline carries the selection; nothing else.

### Approach B: pill tabs (product, modern)

```tsx
<div role="tablist" className="inline-flex rounded-md bg-stone-100 p-1 gap-1">
  {tabs.map((t) => (
    <button
      key={t}
      role="tab"
      aria-selected={active === t}
      onClick={() => setActive(t)}
      className={`px-3 py-1.5 text-sm font-medium rounded transition-all ${
        active === t
          ? 'bg-white text-stone-900 shadow-sm'
          : 'text-stone-600 hover:text-stone-900'
      }`}
    >
      {t}
    </button>
  ))}
</div>
```

**Feel:** contemporary SaaS; the selected tab "pops out" via shadow. Used by Linear, Raycast, Cursor.

### Approach C: segmented sliding indicator (physical, crafted)

```tsx
const tabRefs = useRef({});
const [indicator, setIndicator] = useState({ left: 0, width: 0 });

useEffect(() => {
  const el = tabRefs.current[active];
  if (el) setIndicator({ left: el.offsetLeft, width: el.offsetWidth });
}, [active]);

<div role="tablist" className="relative inline-flex bg-stone-100 rounded-full p-1">
  <div
    className="absolute top-1 bottom-1 bg-white rounded-full shadow-sm transition-all duration-300"
    style={{ left: indicator.left, width: indicator.width, transitionTimingFunction: 'cubic-bezier(0.2, 0, 0, 1)' }}
  />
  {tabs.map((t) => (
    <button
      key={t}
      ref={(el) => (tabRefs.current[t] = el)}
      role="tab"
      aria-selected={active === t}
      onClick={() => setActive(t)}
      className={`relative z-10 px-4 py-2 text-sm font-medium rounded-full transition-colors ${
        active === t ? 'text-stone-900' : 'text-stone-600'
      }`}
    >
      {t}
    </button>
  ))}
</div>
```

**Feel:** iOS-native, physical. The indicator slides between positions rather than switching.

---

## 2. Modal / dialog — three approaches

### Approach A: centered classic

Full-screen overlay, centered card, backdrop click to close. Simple and well-understood.

### Approach B: bottom sheet (mobile-first, intimate)

Slides up from the bottom; on desktop, can center or stay bottom-anchored. Apple-family pattern. Feels less interruptive.

### Approach C: side drawer (for navigational or form-heavy contexts)

Slides in from right (or left). Keeps context visible behind. Works well for detail views where the user might need to refer back to the list.

### Shared considerations (all approaches)
- Focus trap inside the modal
- `Escape` key closes
- Return focus to the trigger on close
- Backdrop is dismissible
- `aria-modal="true"`, `role="dialog"`, `aria-labelledby` on the title

---

## 3. Data table — three approaches

### Approach A: dense tabular (reference grade)

Tight rows, small type (13-14px), zebra-striping optional, column headers sticky. Visually similar to a financial report or scientific table.

```tsx
<table className="w-full text-sm tabular-nums">
  <thead className="bg-stone-50 border-b border-stone-200">
    <tr>
      <th className="text-left px-3 py-2 font-semibold">Ticker</th>
      <th className="text-right px-3 py-2 font-semibold">Price</th>
      <th className="text-right px-3 py-2 font-semibold">Δ 1D</th>
      <th className="text-right px-3 py-2 font-semibold">Vol</th>
    </tr>
  </thead>
  <tbody>
    {rows.map((r, i) => (
      <tr key={r.ticker} className={`border-b border-stone-100 ${i % 2 ? 'bg-stone-50/40' : ''}`}>
        <td className="px-3 py-1.5 font-mono">{r.ticker}</td>
        <td className="text-right px-3 py-1.5">{r.price.toFixed(2)}</td>
        <td className={`text-right px-3 py-1.5 ${r.change >= 0 ? 'text-emerald-700' : 'text-rose-700'}`}>
          {r.change >= 0 ? '+' : ''}{r.change.toFixed(2)}%
        </td>
        <td className="text-right px-3 py-1.5 text-stone-500">{formatVol(r.volume)}</td>
      </tr>
    ))}
  </tbody>
</table>
```

### Approach B: carded-row (editorial, breathable)

Each row a card with generous padding; more space, less information density. Suited for a portfolio view or a list of items where you want each row to feel distinct.

### Approach C: hybrid with inline sparkline

Dense rows, but each includes a small inline chart in its own column — a mini-chart in a table cell. Combines tabular precision with trend visualization.

---

## 4. Filter / search controls — three approaches

### Approach A: always-visible sidebar

Left sidebar with all filters listed, checkboxes or sliders inline. Desktop dashboard pattern. Consumes horizontal space but doesn't hide anything.

### Approach B: top bar with chips

Active filters as removable chips in a horizontal bar above the content. Inactive filters in a menu. Airbnb, Linear.

### Approach C: command-palette search

A single input (cmd/ctrl+K) that filters, navigates, and actions in one. Raycast, Linear, Obsidian's quick switcher.

---

## 5. Empty states — three approaches

### Approach A: minimal notice (reference grade)

Centered small paragraph: "No matching results." Muted color. No illustration.

### Approach B: guided empty state

Larger, with an illustration or icon, explanation of why it's empty, and a specific next action. "No filters match Q1 2026. Try broadening the date range."

### Approach C: pre-filled example

Instead of empty, show sample data with a "this is example data; your actual data will appear here" caption. Common in product tours and onboarding.

---

## 6. Loading states — three approaches

### Approach A: skeleton placeholders

Gray rectangles in the shape of the eventual content. Shimmer animation suggesting progress. Good when the eventual content shape is predictable.

### Approach B: spinner + message

Centered spinner with a descriptive message: "Aggregating 12,000 events." Good when the operation isn't quick and the reader benefits from knowing what's happening.

### Approach C: progressive reveal

Show the first data that arrives immediately; load the rest in the background. Let the reader start working with partial information. Works when data has natural priority.

---

## 7. Error states — three approaches

### Approach A: inline error

Red text or card below the failing element, specific to the operation that failed. For form validation, API failures on specific fields.

### Approach B: toast / snackbar

Brief popup at bottom or top of screen with the error and optionally a retry button. Disappears after a few seconds. Good for recoverable errors that don't block.

### Approach C: full-page error with context

When the error blocks all operation (app-level failure), a full page with: what broke, error ID (for support), timestamp, "Retry" and "Copy error" buttons. No stack trace shown to end user.

---

## 8. Progress indication — three approaches

### Approach A: linear progress bar

Classic. Shows completion percent. Good when progress is continuous and visible.

### Approach B: step indicator

Five circles with the active step highlighted. Good for multi-step flows with discrete, named steps.

### Approach C: indeterminate cycle (no known endpoint)

Animated bar or spinner when you don't know when it will finish. Honest about uncertainty.

---

## 9. Stepper / wizard — three approaches

### Approach A: horizontal step indicator

Top-of-view horizontal bar with step names. User sees the full journey.

### Approach B: progressive disclosure

Only current step visible; previous ones collapse. Airbnb-style form flows.

### Approach C: editable timeline

Steps on the left as a vertical stack. User can click back to any previous step. Preserves all their work. Used by complex product configurators.

---

## 10. Card layouts — three approaches

### Approach A: equal-density grid

CSS Grid with equal cell sizes. Every card the same. Marketplace default.

### Approach B: masonry (varied heights)

Pinterest-style. Cards wrap, heights vary. Good when content is genuinely different lengths.

### Approach C: editorial feature grid

One card breaks out as large, others small in grid around it. Magazine aesthetic.

---

## 11. Buttons — three approaches

### Approach A: solid primary, outline secondary, ghost tertiary

Classic three-tier. Clear hierarchy; well-understood.

### Approach B: tonal (subtle primary)

Primary is not solid saturated — instead a lightly tinted background. Google's Material 3 "tonal" buttons.

### Approach C: icon + label in varied arrangements

Button sometimes icon-only, sometimes icon + label, sometimes label only. Consistent across contexts but adapts to space.

---

## 12. Slider inputs — three approaches

### Approach A: plain HTML range input

`<input type="range">`. Native; keyboard-accessible; screen-reader-friendly.

### Approach B: custom track + thumb

Styled track, custom thumb, live value shown nearby. Full design control.

### Approach C: scrubbable with ticks

Notched slider with visible tick marks for key values. Good when specific values are meaningful.

---

## 13. Keyboard navigation — three approaches

### Approach A: tab-only

Standard browser tab order. Minimum viable.

### Approach B: arrow-key navigation within components

Arrow keys navigate within a list / grid / tab bar. Tab moves between components. Roving `tabindex`.

### Approach C: comprehensive shortcuts

Single-letter shortcuts for major actions, displayed in a `?` overlay. Linear, Notion, Raycast.

---

## 14. Drag-and-drop reorder — two approaches

### Approach A: dnd-kit library (or react-beautiful-dnd)

Well-battle-tested, accessible. Brings dependency weight.

### Approach B: Pointer Events + CSS transforms

Native implementation with pointer down/move/up. Lighter weight; requires more work for a11y.

For Claude artifact environment, the library availability may vary; the pointer-events approach works reliably.

---

## 15. Multi-select — three approaches

### Approach A: checkbox list

Classic. Clear. Accessible. Good for < 20 options.

### Approach B: chip-based selection

Selected items appear as chips above the input. Remove by clicking X. Good when the selection is what the user should see.

### Approach C: searchable dropdown with multi-check

Single input with checkboxes that filter as you type. Good for many options where search matters.

---

## 16. Toast notifications — notes

- Auto-dismiss after 3-5 seconds (longer for errors)
- Position: top-right or bottom-center
- Dismiss button always
- Multiple toasts stack
- Never for critical errors — those need more attention

---

## 17. Virtualized list — when and how

Use when rendering > 100 items and scrolling matters. Libraries (react-window, @tanstack/react-virtual) provide battle-tested virtualization. In Claude artifact environment, availability varies.

**Hand-rolled virtualization:** observe scroll position, render only items in viewport ± a buffer. Spacer divs preserve scroll height.

---

## 18. Disclosure / accordion — two approaches

### Approach A: native `<details>` / `<summary>`

Zero JS; keyboard accessible; reliable.

### Approach B: custom styled with animation

Controlled React state; animated height transition. More styling control; requires careful a11y.

---

## 19. Command palette — notes

```tsx
// Sketch; cmdk is the canonical implementation in React
useEffect(() => {
  const down = (e) => {
    if (e.key === 'k' && (e.metaKey || e.ctrlKey)) {
      e.preventDefault();
      setOpen((o) => !o);
    }
  };
  document.addEventListener('keydown', down);
  return () => document.removeEventListener('keydown', down);
}, []);
```

Grouped results, keyboard navigation (arrow keys), instant filter, action execution on Enter.

---

## 20. Tooltips — three approaches

### Approach A: title attribute

Browser-native. Free. Accessible to some screen readers. Very basic.

### Approach B: custom positioned tooltip

Hover or focus triggers a styled bubble. Flexible but needs positioning logic.

### Approach C: rich popover

Larger, can contain images / buttons. Triggered on hover or click. Used for feature discovery, in-context help.

---

## 21. Form validation — two philosophies

### Approach A: on-submit

Validate when the user tries to submit; show all errors at once. Less intrusive during typing.

### Approach B: on-blur with progressive

Validate each field when the user leaves it; accumulate errors as they go. More helpful but more interruptive.

**Both:** never validate as the user types the first character. That's hostile.

---

## 22. State persistence in interactive artifacts

Claude artifact environment typically lacks `localStorage`. Alternatives:

- **In-component state only** — state resets on remount; usually fine
- **URL hash** — `window.location.hash = encoded(state)`; persists across refresh
- **Export / import** — user can copy current state as JSON, paste to restore

---

## 23. Cross-references

- `references/medium-playbooks/claude-react-artifact.md` — the environment these snippets target
- `references/libraries/motion-library.md` — animation approaches for these components
- `references/libraries/composition-library.md` — where these components sit in layout

---

## 24. Extending this cookbook

Add patterns when:
- You have multiple genuinely different approaches to the same problem
- Each approach has distinct character and tradeoffs
- The problem recurs across artifacts

Avoid:
- Single-canonical implementations (this file isn't a canonical library — it's a set of alternatives)
- Overly specific one-off patterns

The goal: when faced with "I need tabs," Claude has three different aesthetics to consider, not one default to reach for.

<!-- END: references/libraries/snippet-cookbook.md -->

---


<!-- BEGIN: references/libraries/type-library.md -->

# Type Library

A platter, not a recipe. Typography is one of the most unforgiving domains of design: the difference between "fine" and "apex" is almost entirely about taste, restraint, and knowing what's possible. This library exists to widen the space of possibilities, not to prescribe pairings to reach for.

> See `references/how-to-use-this-system.md` for the platter principle.

---

## 1. Typographic theory, briefly

### Classification (tradition)

Understanding where a typeface comes from helps predict where it fits. The major classifications:

- **Humanist serif** — organic letterforms rooted in early Renaissance. Examples: Jenson, Centaur, Adobe Jenson, Arno. Warm, calligraphic, often used for long-form reading.
- **Old-style serif** — Garamond, Caslon, Janson, Sabon. The reference body typefaces of Western publishing; quiet, readable, workhorses.
- **Transitional serif** — Baskerville, Mrs. Eaves, Times, Georgia. Higher contrast, more vertical stress. More formal than old-style.
- **Modern / Didone serif** — Bodoni, Didot, Playfair, Parmigiano. Extreme stroke contrast; elegant, dramatic; often too fragile at body size.
- **Slab serif** — Clarendon, Rockwell, Archer, Roboto Slab. Block serifs, visually assertive, often editorial.
- **Humanist sans** — Gill Sans, Frutiger, Myriad, Calibri, Open Sans. Sans-serifs that retain calligraphic rhythm; warmer than grotesks.
- **Geometric sans** — Futura, Avenir, Circular, Poppins, Inter (partly). Built from geometric primitives; clean, rational, often tech-adjacent.
- **Grotesque / neo-grotesque sans** — Helvetica, Akzidenz-Grotesk, Univers, Neue Haas Grotesk, Inter (partly), Suisse. The Swiss legacy; neutral, precise.
- **Monolinear / contemporary sans** — GT America, Graphik, Söhne, ABC Diatype. Contemporary workhorses; neutral but not as identity-less as Helvetica.
- **Monospace** — JetBrains Mono, IBM Plex Mono, iA Writer Mono, Berkeley Mono, Geist Mono. Equal width. Beyond code, can be an editorial voice choice.
- **Display** — typefaces designed for headlines, not bodies. Often high-chroma, highly stylized.
- **Script** — formal (Zapfino, Bickham) or casual (Comic Sans — don't). Rare in apex work.
- **Blackletter / gothic** — Fraktur, Textura. Historical register; use carefully.

### Pairing principles

When combining typefaces, the dimensions that matter:

- **Contrast of classification** — a humanist serif with a geometric sans is a canonical pairing; two grotesque sans-serifs usually fight.
- **X-height matching** — typefaces with similar x-heights pair cleanly; mismatched x-heights require deliberate scale adjustment.
- **Weight and width compatibility** — pairs should have a range of weights; pair a typeface that has a thin and a black with a partner that has at least four weights.
- **Mood alignment** — a warm humanist body with a warm humanist sans; not a cold grotesque with a warm serif unless the contrast is intentional.
- **Hierarchy clarity** — display choice should feel unmistakably different from body; not a different weight of the same family unless that's the specific move.

### Setting details (the craft dimensions)

- **Size** — body text at 16–19px for screen; 9–11pt for print; display scales up from there. Captions 12–13px.
- **Leading (line-height)** — 1.4–1.7 for body; 1.1–1.25 for display; 1.3 for medium-size callouts.
- **Tracking (letter-spacing)** — tighten display text slightly (-0.01 to -0.03em); loosen small text slightly (+0.005 to +0.02em); loosen all-caps significantly (+0.05 to +0.1em).
- **Measure (line length)** — 45–75 characters for body; 30–50 for columns; shorter for very large type.
- **Rag vs. justify** — rag by default (screen); justify for long-form print when you can hyphenate.
- **Optical size** — use optical sizing when available (variable fonts). Body needs different shapes than display.
- **OpenType features** — ligatures, contextual alternates, small caps, oldstyle figures, tabular figures, stylistic sets. Apex typography uses them deliberately.
- **Numerals** — tabular for data tables (aligns columns); oldstyle for body text (blends with lowercase); lining for headings.

### Variable fonts (contemporary expansion)

Variable fonts expose typeface axes continuously rather than at preset weights. Common axes:
- **Weight** (wght: 100–900)
- **Width** (wdth: narrow–wide)
- **Optical size** (opsz: small text vs. display)
- **Slant / italic** (slnt or ital)
- **Grade** (GRAD: weight without changing width)
- Custom axes: mood, contrast, serif/sans crossfade

This opens design space — one typeface can play body, display, and caption roles with perfect optical tuning.

---

## 2. Pairing atlas

Examples across traditions. Treat as inspiration — many more pairings exist in the space; invent when this library doesn't fit.

### Classic editorial (serif body + sans UI)

- **Sabon + Gill Sans** — Penguin Classics tradition
- **Adobe Caslon + Avenir** — restrained American publishing
- **Garamond + Futura** — art house and museum catalog register
- **Minion + Myriad** — Adobe's own eating of its own cooking
- **Baskerville + Helvetica** — the canonical high-contrast pairing
- **Source Serif + Source Sans** — Adobe's open-source pair, clean
- **Charter + Roboto** — screen-optimized editorial

### Contemporary editorial

- **Fraunces + Inter Tight** — contemporary variable serif with contemporary variable sans
- **GT Sectra + GT America** — Grilli Type duo, magazine-contemporary
- **Canela + Söhne** — Commercial Type duo, luxury-editorial
- **Publico + Publico Headline + Publico Banner** — same family across roles (monofamily)
- **Tiempos Text + Untitled Sans** — Klim Type Foundry pair
- **Domaine Display + Söhne** — display serif + neutral sans

### Technical / product

- **Inter + JetBrains Mono** — current SaaS default (suspicion warranted)
- **Inter Tight + IBM Plex Mono** — variable, slightly warmer
- **Söhne + Söhne Mono** — same-family pair, coherent
- **SF Pro + SF Mono** — Apple's own, rigorous
- **IBM Plex Sans + IBM Plex Serif + IBM Plex Mono** — tri-pairing when you need range
- **Geist Sans + Geist Mono** — Vercel's contemporary pair
- **ABC Diatype + ABC Diatype Mono** — Swiss-modern neutral

### Warm / humanist (friendlier)

- **Freight Text + Freight Sans** — superfamily
- **FF Meta + FF Meta Serif** — Erik Spiekermann classic
- **PT Serif + PT Sans** — open-source, Cyrillic-capable
- **Lora + Source Sans** — warm serif with humanist sans

### Geometric / clean

- **Avenir + Futura** — purist geometric
- **Circular + Circular Mono** — Lineto's clean modern
- **Poppins + Space Mono** — Google Fonts accessible pairing
- **Gotham + Gotham Narrow** — H&Co classic

### Editorial display + functional body

- **Playfair Display + Source Sans** — high-contrast display with workhorse body
- **Bodoni 72 + Archivo** — display drama with functional body
- **Didot + Myriad** — fashion editorial register
- **Canela Deck + Neue Haas Grotesk** — luxury register

### Slab-serif-led

- **Archer + Archer** — Hoefler slab across roles
- **Roboto Slab + Roboto** — Google's slab pair
- **Clarendon + Helvetica** — mid-century institutional

### Monospace-as-voice

- **Berkeley Mono + Berkeley Mono** — whole design in one mono; editorial brutalism
- **JetBrains Mono + Inter** — the body is sans, but display is mono for voice
- **Space Mono + Space Grotesk** — Google's "same family" mono + sans pair

### Experimental / contemporary

- **GT Maru (humanist sans) + GT Super (contrast serif)** — contemporary editorial avant-garde
- **Migra + Neue Haas Unica** — variable contrast serif + neutral sans
- **Editorial Old + Editorial New** — Pangram-Pangram's playful pair
- **Reckless + Inter** — contemporary condensed display with neutral sans

### Historical reenactment

- **Fraktur + Garamond** — German editorial history; use sparingly
- **Cloister + Trajan** — Renaissance-Classical combination
- **Century Schoolbook + Century Gothic** — pre-war American institutional
- **ITC Novarese + ITC Stone Sans** — 80s editorial

### Japanese / CJK support

- **Noto Sans JP + Noto Serif JP** — open-source workhorse for CJK
- **Source Han Sans + Source Han Serif** — Adobe/Google CJK pair
- **Hiragino + Yu Gothic** — macOS/iOS native CJK

### Arabic / RTL

- **Tajawal, IBM Plex Arabic, Cairo** — contemporary Arabic sans
- **Amiri, Reem Kufi** — traditional Arabic serif/kufi
- Pair with Latin counterpart from the same foundry when possible

### Condensed / narrow (for dense UI or poster)

- **Oswald + Source Sans** — Google Fonts classic poster pair
- **Anton + Inter** — heavy condensed display with neutral body
- **Barlow Condensed + Barlow** — same family narrow + standard

---

## 3. Named typographers and foundries to know

Not to copy — to **recognize and reference** when building voice. Understanding "this artifact feels Spiekermann-ish" or "this voice is closer to Klim than to Commercial Type" is a power worth having.

- **Matthew Carter** — Georgia, Verdana, Charter, Bell Centennial. Screen-readability legend.
- **Erik Spiekermann** — Meta, Unit, FF Meta. Humanist information design.
- **Adrian Frutiger** — Frutiger, Univers, OCR-B. Rational clarity.
- **Hermann Zapf** — Palatino, Optima, Zapfino. Calligraphic heritage.
- **Hoefler & Co. / H&Co** — Gotham, Archer, Mercury, Sentinel. Editorial polish.
- **Commercial Type** (Paul Barnes, Christian Schwartz) — Publico, Graphik, Canela. Contemporary editorial.
- **Klim Type Foundry** (Kris Sowersby) — Tiempos, Calibre, Söhne, Domaine, Untitled.
- **Grilli Type** (Swiss) — GT Sectra, GT America, GT Walsheim, GT Maru. Swiss contemporary.
- **Dalton Maag** — Leksa, Aktiv Grotesk (with Berton Hasebe), custom work (Ubuntu, BBC Reith).
- **Pangram-Pangram** — Editorial New, Migra, PP Neue Machina. Accessible contemporary.
- **Lineto** — Circular, Akkurat. Clean Swiss modern.
- **Underware** (Dutch) — Auto, Fakir, Zeitung. Playful humanist.
- **Typotheque** — Greta, Irma, Fedra. Rigorous multi-script.
- **Nikolas Wrobel** — ABC Diatype, ABC Whyte. Neutral contemporary grotesques.

For open-source:
- **Google Fonts** — Inter, Source Sans/Serif, Fraunces, Roboto, IBM Plex, Space Grotesk/Mono.
- **Adobe Fonts** (Creative Cloud) — Source family, broader Adobe catalog.

---

## 4. Invention recipes

### The mono-family artifact
Pick one superfamily (e.g., IBM Plex — has sans, serif, mono, condensed) and use it across all roles. Visual coherence is automatic; the challenge is creating hierarchy within one family — via weight, size, and role.

### The anti-pair
Deliberately pair typefaces that are "not supposed to" pair — a humanist sans with a transitional serif; a grotesque with a slab. Can produce distinctive voice when the reasons are clear.

### The historical transplant
Use a typeface from one era in a context where another era is expected. A Bodoni-led interface is disorienting in the right way. A Fraktur-led landing page is probably wrong, but might be exactly right for a specific artifact.

### The constraint-driven choice
- Must support Cyrillic + Greek + Japanese
- Must be free / open-source
- Must have 5+ weights
- Must have tabular and oldstyle numerals

Generate candidates from the constraint set, choose the strongest character from those candidates.

### The voice-led choice
- "Serious but not stuffy" — humanist serif, not Bodoni
- "Tech but human" — humanist sans, not Helvetica
- "Warm but rigorous" — transitional serif
- "Editorial but functional" — superfamily

Choose voice-adjectives first, then typefaces that embody them.

---

## 5. Common failures

- **Google Fonts starter pack everywhere** — Inter + JetBrains Mono is solid but overexposed. Use it consciously, not by default.
- **Helvetica by default** — not wrong, but defaults away from identity. Unless Helvetica's neutrality is the point, choose.
- **Using a display face at body size** — Bodoni is gorgeous at 72pt; at 14px it's illegible.
- **Mixing three families for no reason** — one, or two well-paired. Three almost never.
- **Ignoring numerals** — tabular in data tables, oldstyle in body. Default lining figures in body look over-loud.
- **Pairing two similar sans** — Helvetica + Inter fight because they're close but not identical. Different enough to read as mismatched.
- **Free-fonts cocktail** — the "Google Fonts 10 random fonts" look.

---

## 6. Cross-references

- `references/design-tokens.md` — one canonical typographic scale; substitutable
- `references/libraries/color-library.md` — palettes that resonate with typographic choices
- `references/libraries/composition-library.md` — how typography sits in layout
- `references/libraries/inspiration-atlas.md` — typography across cross-domain references

---

## 7. Extending this library

Add a pairing or typographer when:
- It represents a tradition or foundry not yet covered
- The pairing is demonstrably paired by reputable practitioners
- You can articulate why it works

Do not add every font you've used or every pairing you like. Aim for representative breadth.

<!-- END: references/libraries/type-library.md -->

---


<!-- BEGIN: references/libraries/utilities.md -->

# Utilities Grab-Bag

A platter of pure, dependency-free helpers. Use any of these directly, adapt for the specific artifact, or write your own. Nothing here is canonical — multiple ways to do each task exist; these are workable starting points.

All utilities are ES modules, zero-dependency, and work in the Claude React artifact environment.

> See `references/how-to-use-this-system.md` for the platter principle.

---

## Number formatting

```js
// Compact (K / M / B / T)
export function compactNumber(n, precision = 1) {
  if (n === null || n === undefined || !isFinite(n)) return '—';
  const abs = Math.abs(n);
  if (abs >= 1e12) return (n / 1e12).toFixed(precision) + 'T';
  if (abs >= 1e9)  return (n / 1e9).toFixed(precision) + 'B';
  if (abs >= 1e6)  return (n / 1e6).toFixed(precision) + 'M';
  if (abs >= 1e3)  return (n / 1e3).toFixed(precision) + 'K';
  return n.toString();
}

// Percentage
export function percentage(n, precision = 1) {
  return (n * 100).toFixed(precision) + '%';
}

// Basis points (finance)
export function bps(n) {
  return Math.round(n * 10000) + ' bps';
}

// Currency (uses browser Intl)
export function currency(n, code = 'USD', locale = 'en-US') {
  return new Intl.NumberFormat(locale, {
    style: 'currency', currency: code, maximumFractionDigits: 0,
  }).format(n);
}

// Ordinal (1st, 2nd, 3rd, 4th)
export function ordinal(n) {
  const s = ['th', 'st', 'nd', 'rd'];
  const v = n % 100;
  return n + (s[(v - 20) % 10] || s[v] || s[0]);
}

// Signed delta
export function signedDelta(n, precision = 1) {
  const formatted = Math.abs(n).toFixed(precision);
  return n > 0 ? `+${formatted}` : n < 0 ? `−${formatted}` : formatted;
}

// Range
export function formatRange(min, max, unit = '') {
  if (min === max) return `${min}${unit}`;
  return `${min}–${max}${unit}`;
}

// Significant figures
export function sigFigs(n, sig = 3) {
  if (n === 0) return 0;
  const d = Math.ceil(Math.log10(Math.abs(n)));
  const power = sig - d;
  const magnitude = Math.pow(10, power);
  return Math.round(n * magnitude) / magnitude;
}

// Scientific notation
export function scientific(n, precision = 2) {
  return n.toExponential(precision).replace('e', ' × 10^').replace('+', '');
}

// Tabular alignment helpers
export function padLeft(s, length, char = ' ') {
  return char.repeat(Math.max(0, length - s.length)) + s;
}
```

## Date / time formatting

```js
// Relative time
export function relativeTime(date, now = new Date()) {
  const d = new Date(date);
  const diffMs = now - d;
  const diffSec = Math.round(diffMs / 1000);
  const diffMin = Math.round(diffSec / 60);
  const diffHour = Math.round(diffMin / 60);
  const diffDay = Math.round(diffHour / 24);

  if (Math.abs(diffSec) < 60)   return diffSec === 0 ? 'just now' : `${Math.abs(diffSec)}s ${diffSec > 0 ? 'ago' : 'from now'}`;
  if (Math.abs(diffMin) < 60)   return `${Math.abs(diffMin)}m ${diffMin > 0 ? 'ago' : 'from now'}`;
  if (Math.abs(diffHour) < 24)  return `${Math.abs(diffHour)}h ${diffHour > 0 ? 'ago' : 'from now'}`;
  if (Math.abs(diffDay) < 30)   return `${Math.abs(diffDay)}d ${diffDay > 0 ? 'ago' : 'from now'}`;
  return d.toLocaleDateString();
}

// Duration
export function formatDuration(ms) {
  if (ms < 1000) return `${ms}ms`;
  if (ms < 60_000) return `${(ms / 1000).toFixed(1)}s`;
  if (ms < 3_600_000) return `${Math.round(ms / 60_000)}m`;
  if (ms < 86_400_000) return `${(ms / 3_600_000).toFixed(1)}h`;
  return `${Math.round(ms / 86_400_000)}d`;
}

// ISO date string without time
export function isoDate(date) {
  return new Date(date).toISOString().slice(0, 10);
}

// Month-year label
export function monthYear(date, locale = 'en-US') {
  return new Date(date).toLocaleDateString(locale, { month: 'short', year: 'numeric' });
}

// Days between two dates
export function daysBetween(a, b) {
  return Math.round((new Date(b) - new Date(a)) / 86_400_000);
}

// Generate a date range
export function dateRange(start, end, stepDays = 1) {
  const dates = [];
  const current = new Date(start);
  const last = new Date(end);
  while (current <= last) {
    dates.push(new Date(current));
    current.setDate(current.getDate() + stepDays);
  }
  return dates;
}
```

## Array helpers

```js
// Group by
export function groupBy(arr, keyFn) {
  const m = new Map();
  for (const item of arr) {
    const k = keyFn(item);
    if (!m.has(k)) m.set(k, []);
    m.get(k).push(item);
  }
  return m;
}

// Sort by (stable, key function)
export function sortBy(arr, keyFn, direction = 'asc') {
  const mult = direction === 'desc' ? -1 : 1;
  return [...arr].sort((a, b) => {
    const ka = keyFn(a), kb = keyFn(b);
    if (ka < kb) return -1 * mult;
    if (ka > kb) return 1 * mult;
    return 0;
  });
}

// Unique (by key function or identity)
export function unique(arr, keyFn = (x) => x) {
  const seen = new Set();
  return arr.filter((x) => {
    const k = keyFn(x);
    if (seen.has(k)) return false;
    seen.add(k);
    return true;
  });
}

// Chunk
export function chunk(arr, size) {
  const result = [];
  for (let i = 0; i < arr.length; i += size) {
    result.push(arr.slice(i, i + size));
  }
  return result;
}

// Take / drop
export function take(arr, n) { return arr.slice(0, n); }
export function drop(arr, n) { return arr.slice(n); }

// Range (python-style)
export function range(start, end, step = 1) {
  if (end === undefined) { end = start; start = 0; }
  const result = [];
  if (step > 0) for (let i = start; i < end; i += step) result.push(i);
  else          for (let i = start; i > end; i += step) result.push(i);
  return result;
}

// Zip two arrays
export function zip(a, b) {
  const len = Math.min(a.length, b.length);
  return Array.from({ length: len }, (_, i) => [a[i], b[i]]);
}

// Sum, mean, etc.
export const sum = (arr) => arr.reduce((a, b) => a + b, 0);
export const mean = (arr) => arr.length ? sum(arr) / arr.length : NaN;

// Min / max by
export function minBy(arr, keyFn) {
  return arr.reduce((best, x) => keyFn(x) < keyFn(best) ? x : best, arr[0]);
}
export function maxBy(arr, keyFn) {
  return arr.reduce((best, x) => keyFn(x) > keyFn(best) ? x : best, arr[0]);
}
```

## Statistical helpers

```js
export function median(arr) {
  if (arr.length === 0) return NaN;
  const sorted = [...arr].sort((a, b) => a - b);
  const mid = Math.floor(sorted.length / 2);
  return sorted.length % 2 === 0
    ? (sorted[mid - 1] + sorted[mid]) / 2
    : sorted[mid];
}

export function percentile(arr, p) {
  if (arr.length === 0) return NaN;
  const sorted = [...arr].sort((a, b) => a - b);
  const idx = (p / 100) * (sorted.length - 1);
  const lo = Math.floor(idx);
  const hi = Math.ceil(idx);
  if (lo === hi) return sorted[lo];
  return sorted[lo] + (sorted[hi] - sorted[lo]) * (idx - lo);
}

export function stddev(arr) {
  if (arr.length < 2) return 0;
  const m = mean(arr);
  const variance = arr.reduce((a, x) => a + (x - m) ** 2, 0) / (arr.length - 1);
  return Math.sqrt(variance);
}

export function correlation(xs, ys) {
  if (xs.length !== ys.length || xs.length === 0) return NaN;
  const mx = mean(xs), my = mean(ys);
  let num = 0, dx2 = 0, dy2 = 0;
  for (let i = 0; i < xs.length; i++) {
    const dx = xs[i] - mx, dy = ys[i] - my;
    num += dx * dy; dx2 += dx * dx; dy2 += dy * dy;
  }
  const denom = Math.sqrt(dx2 * dy2);
  return denom === 0 ? 0 : num / denom;
}

// Linear regression (y = m*x + b)
export function linearRegression(xs, ys) {
  const n = xs.length;
  const mx = mean(xs), my = mean(ys);
  let num = 0, den = 0;
  for (let i = 0; i < n; i++) {
    num += (xs[i] - mx) * (ys[i] - my);
    den += (xs[i] - mx) ** 2;
  }
  const slope = den === 0 ? 0 : num / den;
  const intercept = my - slope * mx;
  return { slope, intercept, predict: (x) => slope * x + intercept };
}

// Moving average
export function movingAverage(arr, window) {
  const result = [];
  for (let i = 0; i < arr.length; i++) {
    const start = Math.max(0, i - Math.floor(window / 2));
    const end = Math.min(arr.length, start + window);
    result.push(mean(arr.slice(start, end)));
  }
  return result;
}

// Exponential moving average
export function exponentialMovingAverage(arr, alpha = 0.1) {
  if (arr.length === 0) return [];
  const result = [arr[0]];
  for (let i = 1; i < arr.length; i++) {
    result.push(alpha * arr[i] + (1 - alpha) * result[i - 1]);
  }
  return result;
}
```

## Color utilities

```js
// OKLCH to hex (browser-capable; use in browsers that support oklch())
// For production, use a dedicated color library.

// Hex to OKLCH approximation via hex → RGB → linear → XYZ → Oklab → OKLCH
// (full implementation omitted; consult culori or colorjs.io for production)

// Contrast ratio (WCAG-compliant approximation)
function srgbToLinear(c) {
  c /= 255;
  return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
}

export function relativeLuminance(rgb) {
  const [r, g, b] = rgb.map(srgbToLinear);
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

export function contrastRatio(rgb1, rgb2) {
  const l1 = relativeLuminance(rgb1);
  const l2 = relativeLuminance(rgb2);
  const lighter = Math.max(l1, l2), darker = Math.min(l1, l2);
  return (lighter + 0.05) / (darker + 0.05);
}

// Parse hex to RGB triplet
export function hexToRgb(hex) {
  const h = hex.replace('#', '');
  if (h.length === 3) {
    return [parseInt(h[0]+h[0], 16), parseInt(h[1]+h[1], 16), parseInt(h[2]+h[2], 16)];
  }
  return [parseInt(h.slice(0,2), 16), parseInt(h.slice(2,4), 16), parseInt(h.slice(4,6), 16)];
}

// Mix two colors (simple RGB interpolation)
export function mix(hex1, hex2, ratio = 0.5) {
  const [r1, g1, b1] = hexToRgb(hex1);
  const [r2, g2, b2] = hexToRgb(hex2);
  const r = Math.round(r1 + (r2 - r1) * ratio);
  const g = Math.round(g1 + (g2 - g1) * ratio);
  const b = Math.round(b1 + (b2 - b1) * ratio);
  return '#' + [r, g, b].map((c) => c.toString(16).padStart(2, '0')).join('');
}
```

## String / text helpers

```js
// Truncate with ellipsis
export function truncate(str, length, ending = '…') {
  if (str.length <= length) return str;
  return str.slice(0, length - ending.length) + ending;
}

// Title case
export function titleCase(str) {
  return str.replace(/\w\S*/g, (t) => t[0].toUpperCase() + t.slice(1).toLowerCase());
}

// Slugify
export function slugify(str) {
  return str.toLowerCase()
    .replace(/[^\w\s-]/g, '')
    .replace(/[\s_-]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

// Initials
export function initials(name, max = 2) {
  return name.split(' ').slice(0, max).map((w) => w[0]?.toUpperCase() || '').join('');
}

// Word count
export function wordCount(str) {
  return str.trim().split(/\s+/).filter(Boolean).length;
}

// Reading time estimate (~200 wpm)
export function readingTime(str, wpm = 200) {
  const minutes = Math.ceil(wordCount(str) / wpm);
  return `${minutes} min read`;
}

// Plural helper
export function plural(n, singular, plural = singular + 's') {
  return `${n} ${n === 1 ? singular : plural}`;
}
```

## Debounce / throttle

```js
export function debounce(fn, ms) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), ms);
  };
}

export function throttle(fn, ms) {
  let last = 0;
  let timer = null;
  return (...args) => {
    const now = Date.now();
    const remaining = ms - (now - last);
    if (remaining <= 0) {
      last = now;
      fn(...args);
    } else if (!timer) {
      timer = setTimeout(() => {
        last = Date.now();
        timer = null;
        fn(...args);
      }, remaining);
    }
  };
}
```

## DOM / geometry helpers

```js
// Clamp a number
export const clamp = (n, min, max) => Math.max(min, Math.min(max, n));

// Map from one range to another
export function mapRange(value, inMin, inMax, outMin, outMax) {
  return ((value - inMin) * (outMax - outMin)) / (inMax - inMin) + outMin;
}

// Rectangle intersect
export function rectIntersect(a, b) {
  return a.left < b.right && a.right > b.left && a.top < b.bottom && a.bottom > b.top;
}

// Get position from an event relative to an element
export function relativePosition(event, element) {
  const rect = element.getBoundingClientRect();
  return {
    x: event.clientX - rect.left,
    y: event.clientY - rect.top,
    xRatio: (event.clientX - rect.left) / rect.width,
    yRatio: (event.clientY - rect.top) / rect.height,
  };
}
```

## Easing functions

```js
export const easing = {
  linear: (t) => t,
  easeInQuad: (t) => t * t,
  easeOutQuad: (t) => t * (2 - t),
  easeInOutQuad: (t) => t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t,
  easeInCubic: (t) => t ** 3,
  easeOutCubic: (t) => (--t) * t * t + 1,
  easeInOutCubic: (t) => t < 0.5 ? 4 * t * t * t : (t - 1) * (2 * t - 2) * (2 * t - 2) + 1,
  easeOutBack: (t) => {
    const c1 = 1.70158;
    const c3 = c1 + 1;
    return 1 + c3 * Math.pow(t - 1, 3) + c1 * Math.pow(t - 1, 2);
  },
  spring: (t, stiffness = 100, damping = 10) => {
    // Simple spring approximation
    return 1 - Math.exp(-stiffness * t / 1000) * Math.cos(damping * t / 10);
  },
};
```

## Random with seed (deterministic)

```js
// Mulberry32 PRNG
export function seededRandom(seed) {
  let t = seed;
  return () => {
    t += 0x6D2B79F5;
    let r = Math.imul(t ^ (t >>> 15), 1 | t);
    r = (Math.imul(r ^ (r >>> 7), 61 | r) ^ r) >>> 0;
    return r / 4294967296;
  };
}

// Sample from array with seeded random
export function sample(arr, rng = Math.random) {
  return arr[Math.floor(rng() * arr.length)];
}

// Shuffle (Fisher-Yates)
export function shuffle(arr, rng = Math.random) {
  const result = [...arr];
  for (let i = result.length - 1; i > 0; i--) {
    const j = Math.floor(rng() * (i + 1));
    [result[i], result[j]] = [result[j], result[i]];
  }
  return result;
}
```

## Type guards (TS-adjacent)

```js
export function isDefined(x) { return x !== null && x !== undefined; }
export function isString(x) { return typeof x === 'string'; }
export function isNumber(x) { return typeof x === 'number' && !isNaN(x); }
export function isArray(x) { return Array.isArray(x); }
export function isObject(x) { return typeof x === 'object' && x !== null && !Array.isArray(x); }
```

---

## Cross-references

- `references/medium-playbooks/claude-react-artifact.md` — runtime where these are used
- `references/libraries/snippet-cookbook.md` — larger component patterns
- `references/libraries/dataset-corpus.md` — data shapes these utilities process

---

## Extending this file

Add a utility when:
- It is pure, dependency-free, and general-purpose
- It would be written fresh in most artifacts otherwise
- It is small enough to paste into an artifact inline

Avoid:
- Utilities that are trivial one-liners
- Anything requiring dependencies
- Domain-specific helpers that belong in a specific playbook

The goal: common wheel-reinvention avoided, without creating a dependency on this file.

<!-- END: references/libraries/utilities.md -->

---


<!-- BEGIN: references/libraries/visualization-grammar.md -->

# Visualization Grammar

A platter, not a decision tree. The full space of chart types is much bigger than "bar or line." This library surveys what exists — including forms that feel exotic — so Claude can reason freshly about which form fits *this artifact*.

No decision tree. The grammar below lets you compose fresh chart forms from first principles, or choose an uncommon form because the common one would flatten what's actually interesting.

> See `references/how-to-use-this-system.md` for the platter principle.

---

## 1. The grammar of graphics, briefly

Leland Wilkinson's formalization (and Hadley Wickham's accessible version in `ggplot2`) dissolves "chart types" into compositions of more primitive elements:

**A chart is a combination of:**

- **Data** — rows with variables
- **Aesthetic mappings** — which variable is mapped to which visual channel
- **Geoms** — the visual mark (point, line, bar, area, rect, polygon, text, path)
- **Scales** — how values are translated to channels (linear, log, discrete, time)
- **Coordinate system** — Cartesian, polar, geographic projection, parallel
- **Facets** — splitting into panels by a variable
- **Statistics** — transformations applied before drawing (bin, smooth, summarize)

"A bar chart" = geom_bar + discrete x + continuous y + Cartesian.
"A pie chart" = geom_bar + one category × stacked + polar coordinate.
"A polar bar chart" = geom_bar + discrete angle + continuous radius.

**The implication:** you are not picking from 30 named chart types. You are composing a chart from elements. Named charts are common compositions; uncommon compositions are often more appropriate to a specific dataset.

### Visual channels ranked by perceptual precision (Cleveland & McGill, 1984; Munzner)

When the question is "how much of X relative to Y," readers decode most accurately in this order:
1. Position on a common scale (same y-axis) — most accurate
2. Position on non-aligned scales
3. Length
4. Angle / slope
5. Area
6. Volume
7. Curvature
8. Shading / color intensity

**Upshot:** bar charts win accuracy comparisons; pies and bubble charts lose. Use the lower channels only when the top channels don't fit the data.

For categorical comparisons (which-is-which): color hue > shape > texture.

---

## 2. Chart forms — a broad survey

Not a shortlist. Each entry: what it is, strengths, weaknesses, notable exemplars.

### Comparison across categories

**Bar chart (vertical)** — position-on-common-scale for a categorical x. Default for "which is biggest." Order by value unless the categorical order is meaningful (time, ordinal).

**Bar chart (horizontal)** — identical encoding; use when labels are long (sideways labels fail).

**Dot plot** — same comparison as a bar, less ink. Cleveland's preferred form. Reads better for many categories or when baseline-at-zero would obscure small differences.

**Lollipop chart** — dot + line to baseline. Hybrid of dot and bar. Useful when baseline matters but ink should be light.

**Grouped bar chart** — multiple bars per category, spaced. Two or three levels of grouping; more and it fails. Ordering within groups matters.

**Stacked bar chart** — total + composition in one chart. Good when total is the main question and composition is secondary. Bad if comparing components across categories (the shared baseline is only for the first segment).

**Diverging bar chart** — baseline at a meaningful midpoint (zero, target). Bars extend in both directions.

**Radial bar chart (coxcomb, Nightingale)** — bars in polar coordinates. Hard to compare lengths; often symbolic more than analytical.

### Change over time

**Line chart** — position × time, continuous. Classic. Fails past ~5 lines without de-emphasis.

**Area chart** — line + filled area. Emphasizes magnitude, not just trajectory. Avoid stacking if component comparison is the point.

**Stacked area chart** — composition over time. Only interpretable if the total is meaningful and components sum to something interpretable. Streams are hard to compare against each other.

**Horizon chart (Saito)** — area chart folded into bands. Dense time series in minimal vertical space. Used for anomaly detection across many parallel series.

**Ridgeline plot / joyplot** — many distributions stacked vertically, sharing an axis. Named after Joy Division's *Unknown Pleasures* cover. Good for showing how distributions evolve across time or categories.

**Sparkline** — line chart at body-text size, no axes. Tufte's invention. Lives inline in prose: "sales ▁▂▃▂▄▅▆ climbed this quarter." Context-free by design.

**Slope graph** — two vertical axes, lines connecting points between them. Before-vs-after. Apex choice when you have two time points and want to show change per category.

**Bump chart** — ranks over time. Each line is a category's rank; the chart tracks rising and falling. Used for race-for-the-top stories.

**Calendar heatmap** — color intensity in a grid of days. GitHub contribution chart. Good for showing temporal patterns at daily granularity across a year.

**Stream graph** — variation on stacked area with a centered baseline. Organic shape; aesthetic choice more than analytical.

**Small multiples of time series** — grid of many small line charts, one per category, sharing axes. Usually better than overlaying 10 lines. Edward Tufte's strong preference for comparing many series.

### Distribution

**Histogram** — counts in bins. Most basic view of a distribution.

**Density plot (KDE)** — smoothed histogram. Reads cleaner but hides bin-level structure.

**Box plot** — five-number summary (min, Q1, median, Q3, max), plus outliers. Compact; excellent for comparing distributions across categories.

**Violin plot** — density plot reflected and filled. More information than box; less intuitive.

**Strip plot (one-dim scatter)** — every data point on a single axis. Good for ≤ 200 points; small datasets appreciate.

**Beeswarm / swarm plot** — strip plot with jitter perpendicular to avoid overlap. Retains every data point.

**Raincloud plot** — violin + box + strip, combined. The full distribution story.

**Empirical CDF** — cumulative distribution. Often more informative than histogram; underused.

### Relationship between two variables

**Scatter plot** — the default for continuous × continuous. Reveals patterns histograms can't.

**Bubble chart** — scatter + size encoding for a third variable. Area encoding is imprecise; use sparingly.

**Hex bin / 2D density** — when scatter has overdraw (many overlapping points), bin into hexagons (or squares) and color by count.

**Contour plot** — lines of constant value over a 2D continuous space. Topographic-like representation.

**Connected scatter** — scatter with lines connecting points in temporal order. Good for phase-space style plots.

**Marginal distributions** — scatter plot with histograms or densities along each axis. Context for the scatter.

### Flow / process / path

**Sankey diagram** — flows between states, width proportional to magnitude. Energy flow diagrams, conversion funnels, migration patterns.

**Chord diagram** — flows between categories arranged in a circle. Symmetric relationships (trade flows, social networks).

**Alluvial diagram** — flow variant showing how entities move between categories over time.

**Parallel coordinates** — each vertical axis is a variable; each observation is a polyline across axes. Many-dimensional data in one chart.

**Parallel sets** — categorical parallel coordinates with band widths.

**Network / node-link diagram** — nodes and edges; force-directed layout is most common. Hard to read past ~30 nodes.

**Arc diagram** — nodes on a line; edges arc above/below. One-dimensional variant of network.

**Matrix of a network (adjacency matrix)** — rows and columns are nodes; cells are edges. Readable for dense networks that spaghetti-ify as node-link.

### Composition (parts of a whole)

**Pie chart** — angles represent shares. Read via angle (low precision). Use only for ≤ 4 slices, when one clearly dominates.

**Donut chart** — pie with a hole. Marginally easier to compare arcs (people read the outer edge). Permit a center label.

**Waffle chart / isotype** — grid of small icons, each representing 1 unit or 1%. Neurath-Isotype tradition. Preserves count; accessible.

**Treemap** — nested rectangles; area = value, nesting = hierarchy. Used for hierarchical data where pie fails at depth.

**Sunburst** — radial treemap; ring segments represent hierarchy levels. Aesthetically striking; moderately readable.

**Icicle chart** — rectangular sunburst. Cleaner for reading.

**Mosaic plot / marimekko** — 2D categorical composition. Width = one variable's share, height = another's conditional.

### Geographic

**Choropleth** — color over regions. Misleading if regions vary in size without normalization (population-weight small areas).

**Proportional symbols** — bubbles sized by value placed on a map. Decouples magnitude from area.

**Dot density map** — one dot per unit. Population density, incidence mapping.

**Hex cartogram / tile grid map** — regions represented as equal-area hexagons or squares. Each state is one hex. Gives equal visual weight.

**Flow map** — arrows between geographic points. Trade, migration, shipping lanes. Minard's Napoleon is the exemplar.

**Contour / heat map** (geographic) — continuous fields over geography.

### Comparison of pairs / correlation at scale

**Scatter plot matrix (SPLOM)** — grid of pairwise scatter plots for multi-dimensional data. Grid of small multiples.

**Correlogram / correlation heatmap** — matrix of correlation coefficients, color-encoded.

### Clinical and epidemiological

A family of chart forms specific to medical, clinical-trial, and public-health communication. Each has stable conventions; deviating from them costs reader trust.

**Kaplan-Meier survival curve** — geom_step + censoring tick marks + at-risk table + (optional) shaded 95% CI band. Composition: time on x (months / years from origin), survival probability on y (0–1 or 0–100%); one stepped line per arm; vertical ticks on the line wherever a patient is censored (lost to follow-up or right-censored at study end); a table beneath the x-axis showing how many patients remain in each arm at successive time points. Hazard ratio and log-rank p-value annotated on-chart. The form's information density is high and reading it is a learned skill; do not strip the at-risk table to "simplify."

**Forest plot** — geom_point + geom_segment + diamond_summary + reference_line. Composition: studies (or subgroups) on the y-axis as rows; effect size (odds ratio, hazard ratio, mean difference) on the x-axis, usually log-scale for ratios; each study a point with horizontal whisker for its 95% CI; point area scaled to study weight (inverse variance); diamond at the bottom for the pooled estimate, its width the pooled CI; vertical line at the null (1 for ratios, 0 for differences). Convention: studies favouring intervention on one side of the null, studies favouring control on the other; this orientation is stable across the field and should not be inverted for novelty.

**Funnel plot** — geom_point + geom_line (pseudo-CI funnel) + reference_line. Composition: effect size on x; precision (often inverse SE, or 1/SE) on y; one dot per study; the "funnel" is a pair of diagonal lines representing the expected 95% scatter under no publication bias. Asymmetry (more dots on one side) suggests publication bias. The form is interpretive — small-study effects can produce asymmetry without bias — but the convention is stable.

**Epi curve (epidemic curve)** — geom_bar (or geom_histogram) + geom_vline (intervention) + annotation. Composition: time bin on x (days for outbreaks, weeks for seasonal, sometimes hours for point-source outbreaks); case count on y; one bar per time bin; vertical lines for interventions (lockdowns, vaccination rollouts, contact-tracing introductions) with date annotations. The chart's shape names the outbreak: a sharp peak → point-source; a slow rise then decline → propagated. The shape *is* the diagnostic.

**R_eff / R₀ fan chart** — geom_line + geom_ribbon (multiple intervals). Composition: time on x; effective reproductive number on y; central line for the median estimate; nested shaded bands for 50%, 80%, 95% credible intervals; horizontal line at R = 1 (the threshold above which the epidemic grows). Used by Bank of England (for inflation forecasts, the form's origin) and adapted to epidemiology during COVID. The fan widens as the projection extends — uncertainty grows with horizon, and the chart shows it.

**Lexis diagram** — geom_segment on a 2D grid + cohort lines. Composition: calendar time on x; age on y; each individual is a diagonal segment of slope 1 (aging one year per year of calendar time) running from birth to death or right-censoring; horizontal slices represent age cohorts; vertical slices represent period observations; diagonal slices represent birth cohorts. The form is dense and demographic; it makes age-period-cohort effects visible simultaneously. Rare outside demography but powerful when the data warrants.

**Age pyramid (population pyramid)** — geom_bar (horizontal, mirrored). Composition: age groups on y; population count on x; bars extend left for one sex, right for the other; bars are usually equal width per 5-year band; ordering bottom-to-top by age (youngest at the base). The form's *shape* names the population: pyramid → growing; rectangle → stable; inverted pyramid → declining; ones with a notch → a war, a famine, or a baby boom visible in the demographics decades later.

**Growth percentile curve** — geom_line (smoothed) × multiple percentiles + geom_point (the child). Composition: age on x; growth measure (weight, height, BMI, head circumference) on y; smoothed reference lines at the 3rd, 10th, 25th, 50th, 75th, 90th, 97th percentiles of a reference population; the individual child plotted as a series of dots over time, ideally connected. The clinical question is *which percentile is the child tracking*, not the absolute value; the chart makes that question visible. WHO and CDC publish the standard reference curves.

**CONSORT flow diagram** — geom_node + geom_edge (Sankey-adjacent). Composition: vertical flow of boxes representing trial stages — enrolment → allocation → follow-up → analysis — with counts at each stage and *reasons for exclusion* annotated on the diverging branches. The form's job is reproducibility: every patient assessed for the trial is accounted for, with their disposition explicit. CONSORT 2010 statement defines the convention; deviating is a methodological red flag.

**Nomogram** — geom_line × multiple parallel axes + linkage. Composition: a series of parallel horizontal scales, each representing one predictor (age, tumour stage, biomarker level); the user draws a vertical line from each predictor's value to a "points" axis at the top, sums the points, and reads the total against a "risk" axis at the bottom. The form predates computational risk calculators by a century and survives because it is *legible without computation*. Clinical nomograms are still published in oncology and cardiology.

### Specialized

**Candlestick chart** — financial; open/high/low/close in one mark.

**Gantt chart** — tasks over time with dependencies. Project management.

**Burndown chart** — scope remaining over time. Agile progress.

**Waterfall chart** — cumulative effect of sequential positive/negative changes.

**Funnel chart** — stages with decreasing magnitudes; conversion analysis.

**Radar / spider chart** — multi-variable profile in a star shape. Used for comparing profiles against each other. Angular imprecision limits analytic power.

**Polar area chart** — bar in polar coordinate, radial length fixed. Nightingale's coxcomb.

**Nightingale rose** — polar bar with variable radial length and angular width.

**Chernoff faces** — facial features encode variables. Historical curiosity; almost never correct.

**Packed bubbles** — area-filled bubbles packed. Often purely decorative.

**Word cloud** — text sized by frequency. Frequently misleading (length, character width), but can work for rough semantic impression.

### Composite / dashboard forms

**Bullet chart (Stephen Few)** — bar + target + qualitative ranges. Replaces gauge charts, more informative.

**KPI card** — single number with delta and context. Composition of text, number, trend, delta.

**Micro-chart in table cell** — sparkline or bar in a table row. Combines tabular precision with visual trend.

---

## 3. Uncommon / underused forms

Forms that deserve more daylight:

- **Slope chart** for before-vs-after — clearer than side-by-side bar charts
- **Bump chart** for rank change — underused for sports, markets, competitions
- **Dot plot** in place of bar charts — nearly always cleaner
- **Isotype / waffle** for count presentations — Neurath's vision deserves a revival
- **Horizon chart** for many parallel series — dense and beautiful
- **Cleveland dot plot** (multiple dots per category) for comparing several measures
- **Ridgeline** for distributions across categories or time
- **Parallel coordinates** for multi-dimensional profile data
- **Hex cartogram** instead of choropleth when visual weight matters more than geography
- **Marimekko** for 2D categorical data
- **Alluvial** for categorical changes over time
- **Empirical CDF** instead of histogram when shape matters

---

## 4. Common visualization failures

The patterns to actively avoid:

- **Truncated y-axis on bar chart** — makes a 2% difference look like a 200% difference
- **Dual y-axis** — almost always misleads; use small multiples instead
- **3D anything** — destroys perceptual accuracy, adds nothing
- **Pie chart with > 4 slices** — angles too hard to compare
- **Rainbow / jet colormap on continuous data** — not perceptually uniform; introduces false boundaries
- **Unordered categorical bars** (alphabetical when no meaning) — squanders ordering as an encoding channel
- **Missing axis labels or units**
- **Unexplained outliers** — if a point dominates the scale, address it
- **Legend far from the marks** — direct labeling always wins
- **Chartjunk** — ornamental grids, bevels, drop shadows, 3D effects
- **Stacked area where components don't sum to something meaningful** — random multi-tone aesthetic
- **Bubble charts where area is proportional to value you want to compare** — area is an imprecise channel
- **Word clouds for analytical claims** — impressionistic only
- **Heatmap with no ordering** — clustering matters; alphabetical rows/cols waste the grid
- **Tooltips hiding essential information** — tooltip is extra detail, not primary

---

## 5. Titles, annotations, and captions

A chart that doesn't argue is a failure. Required for every chart:

- **Title that states the finding** — "Revenue doubled after the pricing change" not "Revenue."
- **Subtitle with scope / unit context** — "weekly, Q1 2026, post-migration"
- **Axes labeled with units**
- **Annotations on relevant points** — event labels, outlier explanations, reference lines
- **Source + date + n** — provenance visible
- **Direct labels where possible** — end-of-line labels beat a legend

The chart is a miniature document. It has a title (thesis), body (marks), caption (interpretation), and footer (source).

---

## 6. Literature to recognize

References Claude can allude to or reason from:

- **Tufte** — *The Visual Display of Quantitative Information*; *Envisioning Information*; *Beautiful Evidence*. Data-ink ratio, sparklines, small multiples.
- **Cleveland** — *The Elements of Graphing Data*; *Visualizing Data*. Visual-channel precision research.
- **Bertin** — *Semiology of Graphics* (1967). The foundational taxonomy of visual variables.
- **Wilkinson** — *The Grammar of Graphics*. The composable view of charts.
- **Wickham** — `ggplot2` in R; the popularized version of Wilkinson. Extensive documentation.
- **Ware** — *Visual Thinking for Design*; *Information Visualization: Perception for Design*. The cognitive science of seeing data.
- **Few** — *Show Me the Numbers*; *Now You See It*. Dashboard design principles.
- **Cairo** — *The Truthful Art*; *How Charts Lie*. Ethics and clarity in visualization.
- **Kosara** — writings on storytelling in visualization.
- **D'Ignazio & Klein** — *Data Feminism*. Critical perspective on visualization defaults.
- **Meirelles** — *Design for Information*. Historical survey of information visualization forms.
- **Rosling** — *Factfulness*; *Gapminder* work. Motion and time in visualization for public communication.

---

## 7. How to choose (without a decision tree)

The traditional question-to-chart mapping is *a* useful heuristic, but it often produces defaults. A better approach:

1. **State the claim** you're trying to make with the chart. Not the topic; the claim.
2. **Identify the variables** (continuous / categorical / ordinal / temporal / geographic / hierarchical / network).
3. **Scan the visualization space** — not just the default, the whole grammar. What forms could represent this?
4. **Ask what each form emphasizes** — a bar chart emphasizes comparison; a line emphasizes trajectory; a dot plot de-emphasizes magnitude-from-zero.
5. **Pick the form that matches what you want the reader to notice.** If you're arguing the *shape of change*, not the *magnitude*, a slope chart may beat a bar chart.
6. **If no standard form fits cleanly, compose one** from grammar primitives. It is entirely reasonable to invent an unnamed chart form.

Two grounded heuristics:

- **If your data has a natural order (time, magnitude, rank), use a chart form that honors the order.** Don't let alphabetical categorization override.
- **If your claim is about *change*, use a form that shows change directly.** Two side-by-side bars force mental math; a slope chart or line chart shows change as slope.

---

## 7b. Clinical algorithm and pathway forms

The clinical-algorithm tradition has produced its own grammar — a vocabulary of shapes, annotations, and layout rules distinct from the generic flowchart conventions in §2. The grammar matures inside *UpToDate*, the ACC/AHA / ESC guideline traditions, the WHO and AHRQ guideline factories, and the GINA / GOLD / KDIGO disease-specific guidelines. Apex clinical algorithms honour the grammar without flattening it; algorithms that import generic flowchart conventions are read as procedurally-deficient by clinicians trained in the discipline.

### 7b.1 ANSI / ISO 5807 shape vocabulary

The shape vocabulary that distinguishes a clinical algorithm from a generic flowchart originates in ANSI X3.5-1970 *Flowchart Symbols and Their Usage in Information Processing* and was internationalised as ISO 5807-1985 *Information processing — Documentation symbols and conventions*. Five shapes carry the load:

- **Diamond** — *decision*. Two or more branches exit; each branch is labelled with the decision criterion. Apex clinical algorithms label the criterion *inside* the diamond and the branch *on the arrow* (*"NIH Stroke Scale ≥ 6?"* in the diamond; *"Yes"* and *"No"* on the arrows). The diamond is structurally distinct from the rectangle because decisions are where the algorithm's logic lives.
- **Rectangle** — *process*. A clinical action to perform (give a drug, order a test, escalate). The most common shape; the workhorse.
- **Oval (or stadium / pill shape)** — *terminator*. The start or end of the algorithm. Start ovals carry the entry condition (*"Adult with suspected acute stroke"*); end ovals carry the exit disposition (*"Admit to stroke unit"*).
- **Parallelogram** — *input / output*. Data entry or data return — a labs result, a vital-sign reading, a patient-reported symptom. Distinguishes the algorithm's *information acquisition* from its *information consumption*. Often omitted in compressed algorithms; restored in apex versions because it makes the data-dependency graph visible.
- **Pentagon (home-plate connector)** — *off-page reference*. The arrow exits the current algorithm and enters another (see § 7b.3). The pentagon's directional shape encodes *"continue here in another document"* without consuming the local diagram's space.

Generic flowchart traditions add many more shapes (cylinder for database, document for printed output, manual-operation trapezoid). Clinical algorithms are stricter — the five shapes above carry essentially all clinical-algorithm logic; introducing additional shapes (cloud, hexagon, octagon) reads as undisciplined to a clinician audience. See `templates/mermaid-clinical-algorithm.mmd` for the full vocabulary deployed in a working algorithm; `references/libraries/iconography-library.md` § Clinical algorithm glyphs for the home-plate-connector glyph specifically.

### 7b.2 ACC / AHA Class I/IIa/IIb/III + LoE annotation

The American College of Cardiology / American Heart Association recommendation-classification system is the dominant evidence-grading scheme in cardiovascular guidelines, increasingly adopted across other specialties (neurology for stroke, pulmonology for PE, GI for GIB). The system is a *typographic system*, not just a textual classification — colour, bracket pattern, and abbreviation work together so a reader scanning the algorithm reads strength-of-recommendation at a glance.

**Class of recommendation (benefit vs. risk).**

- **Class I** (green) — *should be done*. Benefit >>> risk. *"Is recommended"*, *"Is indicated"*.
- **Class IIa** (yellow-green or pale green) — *is reasonable*. Benefit >> risk. *"Is reasonable"*, *"Can be useful"*.
- **Class IIb** (yellow or orange) — *may be considered*. Benefit ≥ risk. *"May be considered"*, *"Effectiveness is unknown"*.
- **Class III: No Benefit** (red, hollow) — *do not do (no benefit)*. Benefit = risk. *"Is not recommended"*, *"Is not useful"*.
- **Class III: Harm** (red, filled) — *do not do (causes harm)*. Risk > benefit. *"Should not be performed"*, *"Causes harm"*.

**Level of evidence (data quality supporting the recommendation).**

- **LoE A** — multiple RCTs or meta-analyses of RCTs.
- **LoE B-R** — limited RCT data.
- **LoE B-NR** — non-randomised data of moderate quality.
- **LoE C-LD** — limited non-randomised data; small studies; case series.
- **LoE C-EO** — expert opinion only; no usable data.

**The typographic pattern.** Each recommendation in an algorithm is annotated with a class-LoE bracket: `[I, A]` for high-evidence strong recommendations; `[IIb, C-EO]` for weak recommendations resting on expert opinion. The bracket sits to the right of or below the recommendation; the colour-band on the rectangle's left edge encodes the class for at-a-glance scanning. The pattern is stable across ACC/AHA, ESC (which uses I/IIa/IIb/III without colour but with the same bracket convention), and the more recent KDIGO and GOLD guidelines. Apex deployment renders the class colour with WCAG-AA contrast against the rectangle's fill; under-deployment uses colour alone (failing colour-blind readers) or omits the bracket (forcing readers to consult the guideline text).

### 7b.3 The single-screen-or-off-page-connector rule

*UpToDate*'s house style — the dominant clinical-reference algorithm convention — caps each algorithm at one screen (roughly 800–1000 px tall on a contemporary laptop; one printed page). The rule is cognitive-load calibration: a clinician at the point of care is parsing the algorithm with split attention while patient care continues; an algorithm that requires scrolling loses the reader at the scroll. The fix when the algorithm cannot fit on one screen: split into a *parent algorithm* and one or more *child algorithms*, connected by pentagon off-page connectors.

**The connector convention.** The pentagon carries a label (*"Acute STEMI pathway — see Figure 2"* or *"Continue → Cardiogenic shock algorithm"*) and is the *only* element that crosses page or screen boundaries. Each child algorithm carries the parent reference (*"Entry from: Initial chest-pain algorithm"*). The connector pattern preserves the single-screen rule for each algorithm individually while permitting the cumulative pathway to span multiple algorithms.

**Why not just zoom out.** A multi-page algorithm rendered as a single sprawling diagram loses the connector discipline — readers' eyes wander; the next-step graph is harder to scan; the algorithm's branching logic is obscured by visual density. The split-with-connectors pattern preserves *local* clarity at every level. *UpToDate*'s 1990s-onward house style is the canonical demonstration; the BMJ Best Practice and AHRQ Guidelines.gov successors follow the same convention.

### 7b.4 Time-anchored algorithms

A time-anchored algorithm encodes urgency directly into the diagram by labelling steps with the time at which they should occur. Two canonical examples define the form:

- **Surviving Sepsis Hour-1 Bundle.** Evans, Rhodes *et al.* (*Crit Care Med* 2021;49:e1063 — the Surviving Sepsis Campaign 2021 update). Five actions (measure lactate, blood cultures, broad-spectrum antibiotics, 30 mL/kg crystalloid for hypotension or lactate ≥ 4, vasopressors for persistent hypotension) all anchored to *Hour 1* — the first hour from sepsis recognition or ED triage. The algorithm displays a prominent clock-badge (⏱ glyph; see `references/libraries/iconography-library.md`) at the top, anchoring the entire bundle to the time-zero event.
- **Door-to-needle stroke 4.5 hours.** The thrombolysis-eligibility window for acute ischaemic stroke is 4.5 hours from last-known-well; the AHA/ASA algorithm anchors the thrombolysis-decision diamond to a clock badge showing *"≤ 4.5 hours from LKW"*. Faster sub-targets (door-to-CT 25 min; door-to-needle 60 min) appear as time-stamps at each interim step.

**The time-anchor typography.** The clock glyph (⏱ or a custom clock SVG) sits to the left of the step's rectangle; the time appears inside the badge. Apex deployment carries the time into the documentation chassis — the post-event audit lines up actual times against the algorithm's targets; the gap between the two is the QI target. The form is structurally distinct from a non-time-anchored algorithm: the latter says *what* to do, the former says *what to do **by when***.

### 7b.5 Stepwise ladders vs branching algorithms vs sequential bundles

Three structurally distinct forms address different decision contexts. The form is the message; mismatched form-to-context produces algorithms that confuse the reader rather than guide them.

- **Stepwise ladder.** A vertical sequence of *escalation steps*, each step containing one or more interventions; the clinician moves *up* the ladder when control is inadequate, *down* when control is sustained. The canonical example: **GINA's 5-step asthma ladder** (Global Initiative for Asthma; updated annually; *gina-asthma.org*). Step 1 is as-needed low-dose ICS-formoterol; step 5 is high-dose ICS-LABA plus add-on biologic; intermediate steps are intermediate doses. Bidirectional arrows at *every* band reinforce that the ladder is climbed *and descended*. Use when the decision is *titration of an intensity-graded intervention* against a continuous control target.
- **Branching algorithm.** A flowchart whose decisions partition patients into *distinct management groups*, each receiving a different intervention. Diamond-decision shape vocabulary applies; class-LoE annotations attach to each terminal recommendation. Use when the decision is *which intervention*, not *how much*.
- **Sequential bundle.** An ordered list of actions, *all* of which must be performed (the order may be flexible but the completion is required). The canonical example: the **WHO Surgical Safety Checklist** (Haynes, Weiser *et al.*, *N Engl J Med* 2009;360:491) — 19 items across three pause points (sign-in before anaesthesia; time-out before incision; sign-out before patient leaves OR). No decision diamonds; no branches; the form is a checklist, not a flowchart. Use when the failure mode is *omission*, not *misdirection*.

The three forms can be combined within a larger pathway — a branching algorithm whose terminal management box contains a stepwise ladder, or a stepwise ladder whose first step is preceded by a sequential bundle. Apex combinations preserve each form's discipline within its sub-diagram; weak combinations blur the boundaries (decision diamonds appearing inside a checklist; bundles drawn as flowcharts).

### 7b.6 Swim-lane pathway maps

A swim-lane pathway map is a multi-stakeholder, multi-time-anchor diagram that traces a patient's path through a system of clinicians and locations. The notation is Business Process Model and Notation (BPMN 2.0; Object Management Group standard ISO/IEC 19510:2013), adopted into clinical contexts because the multi-actor, multi-handoff nature of patient care matches BPMN's design intent.

**The compositional grammar.**

- **Horizontal axis** — time (often hours, sometimes days, sometimes phase-of-care: pre-op / intra-op / post-op / discharge / community).
- **Vertical axis** — swim lanes, one per role or location (ED triage / ED physician / radiology / OR / ICU / ward / discharge planning / community provider). Lanes are stacked; their order reflects the typical flow.
- **Within each lane** — task boxes (BPMN rectangles) marking actions performed by that role at that time.
- **Across lanes** — handoff arrows marking transitions. Apex deployments place a *handoff-baton glyph* at every lane crossing (see § 7b.7 and `references/libraries/iconography-library.md` § SBAR baton).
- **Time-anchored events** — clock badges at critical-window boundaries (Hour-1 sepsis bundle deadline; ≤ 4.5 h thrombolysis window; 30-day readmission window).

**Where the form earns its complexity.** A pathway with one or two actors and a linear time-course does not need swim lanes; a basic flowchart suffices. Swim lanes pay rent when *the gaps between lanes are where the waste lives* — a patient sitting in ED for two hours waiting for radiology to read a scan that arrived 90 seconds after acquisition; a discharge delayed because community-provider hand-off has not been initiated. The visible empty space *in a lane* between handoff arrows is the quality-improvement target. NHS Improvement's *Pathway Mapping* (2005) is the canonical methodology reference; the form has spread into oncology multidisciplinary-team pathways, sepsis care bundles, and surgical patient-journey maps.

**Apex deployment.** Lanes are labelled with the role *and* the location (*"Anaesthetist (OR)"*, not just *"Anaesthetist"*); time anchors appear at the top *and* are repeated as a grid at major intervals; handoff batons (§ 7b.7) appear at every cross-lane transition; SBAR or I-PASS labels annotate the baton's content. See `templates/svg-patient-pathway-map.svg` for a realised example (sepsis pathway ED→ICU; 7 swim lanes × 7 time anchors; BPMN 2.0 notation).

### 7b.7 The handoff-baton glyph

The handoff baton is a small visible glyph — typically an SBAR-labelled token, sometimes an I-PASS-labelled badge — that marks every point in a pathway map where care transitions from one role to another. The convention originates in the Wave 11 SVG-patient-pathway-map template (`templates/svg-patient-pathway-map.svg`) and surfaces in BPMN-derived clinical pathway maps more broadly.

**Why the glyph matters.** Handoff is among the highest-risk moments in clinical care; the Joint Commission's Sentinel Event Alert 58 (2017) and the broader patient-safety literature converge on communication failures at handoff as a leading cause of preventable harm. A pathway map that traces transitions without marking them invisibly understates the risk; a pathway map that marks every transition with a labelled baton (SBAR content: *Situation / Background / Assessment / Recommendation*; or I-PASS: *Illness severity / Patient summary / Action list / Situation awareness / Synthesis*) makes the handoff content auditable. See `references/libraries/medical-artifacts.md` § Handoff for the SBAR and I-PASS specifications; `references/medium-playbooks/clinical-handoff.md` for the per-persona discipline.

**Compositional convention.** The baton glyph sits on the handoff arrow, sized large enough to read at the diagram's intended display scale; its label is the handoff framework (*SBAR* or *I-PASS*); a colour cue indicates whether the handoff is *full* (all elements documented; green), *partial* (some elements; yellow), or *minimal* (verbal only, undocumented; red). The colour cue maps to the QI target: red batons are the audit-relevant transitions. The convention pairs with the swim-lane form (§ 7b.6) but can appear in any pathway diagram with multi-actor transitions.

---

## 8. Cross-references

- `references/medium-playbooks/data-visualization.md` — operational-level guidance
- `references/libraries/color-library.md` — palette selection for charts
- `references/libraries/composition-library.md` — how charts sit in layout
- `references/apex-exemplars.md` — Tufte, NYT, Pudding, Distill as reference points
- `references/tear-downs/03-minard-napoleon.md` — deep study of multi-variable-on-one-plane

---

## 9. Extending this library

Add a chart form when:
- It has a name, a history, and a set of appropriate uses
- It is not a trivial variation on an already-covered form
- You can articulate what it does better than alternatives

Add literature when:
- It is a foundational or widely-referenced text in the field
- It represents a perspective not already covered

Do not add:
- Every minor styling variation
- Every trendy D3 example
- Chart forms you haven't verified work

The goal is a genuinely complete grammar, not a catalog of trends.

<!-- END: references/libraries/visualization-grammar.md -->

---

