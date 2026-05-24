# Artifact-Quality Standards

This project optimizes for **apex-quality artifacts**: outputs whose visual, informational, interactive, and educational density is genuinely high — not merely acceptable. These instructions apply to every artifact you produce: HTML pages, React components, SVGs, Mermaid diagrams, long-form documents, and data visualizations.

## Prime directives

**These supersede every other instruction in this file.** When any subordinate rule appears to be in tension with these, these win.

1. **Maximize quality and "wow" factor.** The goal of every artifact is not adequacy — it is output so clearly excellent that a reader is visibly affected by it. "Wow" is a concrete, shippable standard: polish that is noticed, density that is earned, craft that is felt. Ship nothing less.

2. **Never cap effort.** Time required, token cost, context used, and task difficulty are **not** reasons to reduce ambition, simplify the design, or cut scope. Apply whatever depth of thought, iteration, and revision the work requires. If a second or third pass would meaningfully improve the output, take it.

3. **Never truncate.** Do not deliver a shortened, simplified, "minimum viable," or "for brevity" version of the intended artifact and call it done. **All of the following are prohibited:**
   - `// ... rest of code similar` / `/* ... */` elisions in a shipped artifact
   - "Here's a simplified version" when the full version was asked for
   - Stopping mid-artifact because the response is getting long
   - Leaving `TODO`, `REPLACE`, or placeholder markers in final output
   - Skipping loading / empty / error states because of time pressure
   - Delivering 4 of 6 planned sections and calling it complete
   - "For the full implementation, you would also need to…" (do it)

   If scope genuinely exceeds what a single turn can hold, say so explicitly, plan the whole artifact, and execute it across coherent segments — but the *final delivered artifact* must be complete.

4. **Difficulty is a reason to slow down, not to ship less.** Unfamiliar domain, complex state, novel visualization, dense subject matter — these call for more care, not simpler output. Hard problems get the full treatment.

5. **Refuse "good enough."** When you reach what feels like "done," ask: *what is the single highest-leverage improvement I could make right now?* Make it. Ask again. Stop only when the next improvement is genuinely marginal — not when you are tired of iterating.

**Reconciliation with density.** These directives are about **effort**, not **volume**. Maximum quality is reached through restraint, density, and intentional choice — not by adding more. Spend unlimited effort to produce the *tightest, highest-density* artifact possible; do not mistake length for excellence. "Density beats decoration" below is the *means*; the prime directives are the *end*.

## Philosophy

1. **Density beats decoration.** Every pixel, every line of prose, every interaction should pay its rent in insight or utility. If it doesn't, delete it.
2. **Defaults are destiny.** The artifact's final quality is bounded by the quality of its starting point. Never start from "blank Tailwind" — start from the tokens and scaffolds in `references/`.
3. **Consistency is a feature.** Pick one type scale, one spacing unit, one palette, and commit. Apparent "variety" from mixing systems reads as noise.
4. **Accessibility is table stakes.** WCAG AA contrast, keyboard navigation, semantic HTML, respect for `prefers-reduced-motion`. Not optional.
5. **Self-review before delivery.** Run the checklist in `references/pre-delivery-checklist.md` mentally before the user sees the artifact.

## Non-negotiables

Do **not** ship an artifact that:
- Uses the unmodified default Tailwind palette (`gray-500`, `blue-500`) as a design system
- Fails WCAG AA contrast (4.5:1 body, 3:1 large text / UI)
- Lacks semantic HTML (everything-is-a-`<div>`)
- Has clickable elements without focus states
- Animates without respecting `prefers-reduced-motion`
- Uses icons or emoji purely decoratively in a professional context
- Ships with placeholder copy ("Lorem ipsum", "Click here", "Welcome to our app")
- Has console errors, warnings, or runtime failures on first render
- Uses color as the only channel to convey information

## Calibration cards (read before scaffolding)

Three direct comparisons. The default-stack version is what most artifacts ship as. The apex version is what this project requires. These cards exist because reading the principle ("titles are claims") and recognizing the pattern in your own draft are two different skills — and the second is the one that fails.

### Card 1 — Landing / opening section

**Default-stack version (do not ship):**

```html
<div class="bg-blue-500 text-white p-8 text-center">
  <h1 class="text-5xl font-bold mb-4">Welcome to Our App</h1>
  <p class="text-xl mb-6">The best way to do the thing you need.</p>
  <button class="bg-white text-blue-500 px-6 py-3 rounded">Get Started</button>
</div>
```

What this is missing: a thesis. The opening tells the reader nothing they didn't already know.

**Apex version (calibrate to this):**

```html
<header class="prose">
  <p class="eyebrow">A reference implementation</p>
  <h1>Rank-aggregation under partial orders, visualized.</h1>
  <p class="lede">Nine algorithms, the same 12-candidate ballot, scored on
  Kendall distance from the Condorcet winner. Hover any bar for the
  pairwise breakdown.</p>
</header>
```

Why this works:
- **Visual identity:** one neutral family, no accent splash; the type is the design
- **Information density:** subject + approach + payoff in three sentences
- **Signature move:** 1.6 editorial caption — the lede reads like the opening of a *New Yorker* piece
- **Copy quality:** every sentence carries a specific claim; nothing decorative

### Card 2 — Data visualization

**Default-stack version (do not ship):**

```js
new Chart(ctx, {
  type: 'bar',
  data: { labels: ['Jan','Feb','Mar'], datasets: [{ data: [10,20,15] }] }
});
```

What this is missing: a title that argues, units, an annotation tying numbers to events, source/date, and palette discipline.

**Apex version (calibrate to this):**

```text
MONTHLY ACTIVE USERS — Q1 2026        (thousands)

Jan    ████████████████ 84
Feb    ████████████████████████ 127   ← launched v2 Feb 9
Mar    ██████████████████████ 119

Source: internal analytics, 2026-04-01 snapshot
```

Why this works:
- **Visual identity:** one accent ink, generous whitespace, no chartjunk
- **Information density:** the title is the finding; units are explicit; annotation ties Feb's jump to the launch event
- **Signature move:** 2.1 annotation-as-argument — the chart claims something, doesn't just display
- **Copy quality:** source + date establish provenance without padding

### Card 3 — Educational reveal

**Default-stack version (do not ship):**

> Gradient descent is an optimization algorithm. It iteratively adjusts parameters by subtracting the gradient of the loss function, scaled by a learning rate, until convergence or a maximum iteration count is reached. The learning rate is a hyperparameter that controls the step size...

What this is missing: a hook, a visual, a check for understanding, a moment for the reader to act.

**Apex version (calibrate to this):**

```
[PRIME]    Where does a ball roll on this surface?
           (static 3D surface image)

[SHOW]     (animated dot rolling down gradient, dropping with trail)

[EXPLAIN]  At each step we move opposite the slope. Big slope → big step.
           The number η sets how aggressively we follow it.

[INVITE]   Drag η. Watch what happens at 0.01, 0.1, and 1.0.
           Notice anything at 1.5?
           [interactive slider]
```

Why this works:
- **Visual identity:** the figure carries the explanation; prose supports, doesn't compete
- **Information density:** four moves (prime / show / explain / invite); each does one job
- **Signature move:** 3.4 live-binding to prose — the reader's scrub becomes the lesson
- **Copy quality:** no preamble, no recap, no hedging; "notice anything at 1.5?" hands over the controls

---


## Medium-selection: React first

**Default medium: React/JSX artifact.** In Claude.ai (chat + Projects), the React artifact render environment is the highest-ceiling medium — the preloaded libraries (Recharts, lucide-react, shadcn/ui primitives, Tailwind, framer-motion) and the interactive runtime make it the natural home for the most visually and informationally dense artifacts. When a request could be served by multiple media, **choose React unless another medium is genuinely better for the specific job.**

### Carve-outs — when another medium wins

| Job                                                         | Medium           | Why                                                                     |
|-------------------------------------------------------------|------------------|-------------------------------------------------------------------------|
| Static figure, schematic, or illustration                   | SVG              | Sharper, lighter, print-friendly; React is overkill                     |
| Flow / sequence / ER / state diagram from text source        | Mermaid          | The schematic source *is* the asset; model authors + diffs cleanly      |
| Essay, report, memo, primer                                 | Long-form doc    | Prose is the primary mode; React gives no leverage                      |
| Single-file page that must work offline or share as a URL   | HTML interactive | Runs outside Claude; no React dependency                                |
| Computational narrative with executable code                | Notebook         | Execution is part of the artifact; React can't run Python               |
| Heavy Canvas / WebGL / Observable Plot work                 | HTML interactive | Non-React libraries without React wrappers                              |
| Math-notation-dense derivation or reference                 | Long-form doc + KaTeX | Rendering primitive, not component logic                           |
| Transactional email / newsletter                            | Email (HTML-tables) | Email clients reject React wholesale                                |
| Presenter-mode slides for a talk                            | Slide deck       | Specialized navigation model                                            |

If the request fits a carve-out → use that medium and its playbook. Otherwise → React, and open `references/medium-playbooks/claude-react-artifact.md` first.

## Decision tree

Before scaffolding, answer these in order:

1. **What's the primary job?** — illustrate, teach, demonstrate, persuade, tool, archive
2. **Does a carve-out apply?** — consult the table above
3. **If not → React.** — open `references/medium-playbooks/claude-react-artifact.md`
4. **Who's the reader?** — domain expert, learner, casual observer, decision-maker
5. **What's the density target?** — reference card (highest), explainer, overview, marketing (lowest)
6. **What's the interaction budget?** — static, single-path, exploratory, open-ended

Answers 4–6 shape typography scale, palette choice, information hierarchy, and the specific React patterns to apply.

## Operating loop

For every artifact request:

0. **Write the brief.** Fill `references/brief-template.md` (≤ 200 words): reader, job, success, constraints, prior art, medium lean, density target, interaction budget, proposed signature move, scope manifest. The brief is the contract. Without it, downstream steps drift.

1. **Select the medium.** Default React; apply a carve-out only when genuinely indicated.

2. **Read the relevant medium playbook**, including its "What 10/10 looks like" section for ceiling calibration. `claude-react-artifact.md` for React; otherwise the matching file.

3. **Roll for cross-pollination.** Sample a non-native tradition from `references/libraries/inspiration-atlas.md` § 0 (rolling index of 60 traditions). Declare:
   > Cross-pollination considered: **{tradition}**. Outcome: **{adopted | partially-adopted | noted-but-rejected}**. Reason: **{one specific sentence, >8 words}**.
   Required on artifacts above complexity threshold; skip silently for trivial work.

4. **Pick a signature move** from `references/wow-taxonomy.md` (or invent). Must not repeat the last visible artifact's move unless explicitly justified (anti-repetition rule). Declare it before building.

4.5. **Platter check — name one invention.** Name one thing this artifact does that is *not* in any catalog (wow-taxonomy, visualization-grammar, register list, SVG register list, etc.). If you cannot name one, you have selected entirely from the catalog and are not yet at apex; either invent past it or accept that the artifact is at 7/10 craft territory.

5. **Consult an exemplar** from `references/apex-exemplars.md` or the playbook's "What 10/10 looks like" section. Name your debt.

6. **Choose a design-token set** from `tokens/sets/*` (ft-salmon, quanta-cobalt, penguin-classic, ukiyo-e, scandi-fog, or default-cool). Pick deliberately; prefer a set different from your last artifact's register. Apply via `data-token-set="<slug>"` attribute or inline.

7. **Start from a template** — `templates/` contains concrete starters. Sibling templates per register (e.g., `react-dashboard.tsx` + `react-dashboard-tufte.tsx`) give two-axis variety; pick or invent.

8. **Follow the iteration protocol** in `references/iteration-protocol.md` — tiered floors: 3 passes absolute floor, 5 typical, 7 for substantial work (scaffold → self-critique → adversarial → cold-read → polish; substantial work adds a subtractive pass and a re-cold-read pass). Cold-read pass for reader-facing artifacts. Subtractive pass (`references/subtractive-moves.md`). Budget per `references/budget-and-stopping.md`. Declare which floor applies in the YAML's `iteration.floor_applied`.

9. **Verify hard gates** in `references/hard-gates.md` as you build, not after. If the artifact is medical or scientific in nature, declare the domain mode (`medical_mode` or `scientific_mode`) in the pre-delivery YAML; the linter will enforce the additional required fields.

10. **Run the pre-delivery checklist** and emit the required YAML block (§ 0.4 of `references/pre-delivery-checklist.md`) **after the artifact, before delivery copy**. Any `fail`, `wow_score < 8`, `iteration.passes < 3`, or unsatisfied domain-mode required field = **do not deliver; fix and re-emit.**

11. **Rate honestly (1–10).** Declare `wow_score.aim` separately from `wow_score.rating` — the aim is 9 by default (8 is a floor, not a target). Below 8: identify the highest-leverage fix using `failure-modes.md` vocabulary; apply. Do not ship below 8. Rating 9+ requires named `claimed_exemplars`. `citation_moment` is required regardless of rating (name the sentence / frame / visual moment a future writer would extract). The recency modifier in `iteration-protocol.md` adds +0.5 if the signature move is in the bottom-quintile of recent deployments (additive only). If invoking an exception register from `references/exception-registers.md`, the register-specific rubric replaces this gate.

12. **Run the linter** (`tools/artifact-lint/lint.mjs <path>`) or the mental-lint substitute (Claude.ai Projects path; see `.claude/skills/artifact-scaffold/SKILL.md` step 5b).

13. **Deliver** with tight copy — the artifact is the work; the message is the handoff. No trailing offers or self-diminishment.

## How the library-style files work

The files in `references/libraries/` and the exemplar / taxonomy references are **platters, not recipes**. They give you the full option space across history, craft, and theory — not shortlists of approved choices. Read `references/how-to-use-this-system.md` before consulting any library file. Invent past what's catalogued when the artifact warrants; the libraries give ground, not walls.

