# Apex-Artifacts — Wow Taxonomy (89 named signature moves)

Bundled from the apex-artifacts source repository. Each source file
is enclosed by `<!-- BEGIN: path -->` ... `<!-- END: path -->`
anchors so semantic retrieval and humans can locate the original.

## Files in this bundle

- `references/wow-taxonomy.md`

---


<!-- BEGIN: references/wow-taxonomy.md -->

# The Wow Taxonomy

"Wow factor" is aspirational and, on its own, useless as guidance. This file breaks the term into concrete categories, each with named moves you can deliberately deploy.

**The 84 moves below are examples from a much larger space, not a closed shortlist.** Treat them as a vocabulary starter — a demonstration of the kinds of moves that exist — and feel free to deploy an 85th move that isn't listed here. Apex artifacts frequently use moves no taxonomy captures yet. If the artifact warrants an unlisted move, deploy it.

**The rule:** every apex artifact deploys at least **one** signature move — from this taxonomy or invented fresh — intentionally. The signature move is the one specific, memorable craft decision the artifact is built around. Without one, the artifact is forgettable — technically correct, quickly forgotten. Name the move before you ship; if you can't, you haven't chosen one.

Deploying two or three moves is fine, provided each earns its place and they do not compete. Deploying everything in this file at once produces noise, not excellence.

> See `references/how-to-use-this-system.md` for the platter principle.

---

## 1. Visual wow

The artifact registers as "beautiful" or "striking" at first glance, before the reader has engaged with content.

### Named moves

**1.1 Editorial hero.** A single oversized headline set in a serif display face with tight leading, placed asymmetrically on the page. A newspaper front-page feeling. Example: a chart titled with a 4rem serif claim, not the metric name.

**1.2 The oversized number.** One hero number at 6-12rem. Used once, never twice in the same artifact. Often the finding itself ("**42%** is the figure that matters").

**1.3 Duotone with a single accent.** Entire artifact renders in a neutral family (stone, slate) with one accent hue used sparingly for emphasis. Apple's "Think Different" aesthetic — restraint is the statement.

**1.4 Typographic contrast.** Mix a serif display face with a geometric sans for body and a slab mono for numerics. Three faces, three jobs, each recognizable.

**1.5 The quiet moment.** A section with only whitespace and a single line of prose. Set at display size, centered, generous margin-block. Earns emphasis by denying it everywhere else.

**1.6 Editorial caption.** A figure caption set like it belongs in *The New Yorker*: italic, muted, generous leading, a line wider than the figure. The caption is a miniature essay.

**1.7 Negative space as structure.** Layout organized by empty regions, not dividers. White space is the grid.

**1.8 Hand-crafted ornamentation.** A custom rule, mark, or divider drawn specifically for this artifact. Not a Tailwind `hr`.

**1.9 Intentional grid friction.** Break the grid once, deliberately, for one element. Creates the focal point by being the only thing that refuses the system.

**1.10 Dark mode as separate design.** Not an inversion — a re-balanced palette that feels native to the dark canvas.

**1.11 Calligraphic-stroke register.** Every contour is drawn with pressure variation along its length; the line itself communicates volume, gesture, and the hand that drew it. Variable-width SVG `<path>` with hand-tuned segments, not uniform strokes. The naturalist plate tradition: Audubon's birds (1827-38), Brödel's surgical anatomy (Johns Hopkins, 1911-41), Vesalius's *De Humani Corporis Fabrica* (1543). Distinct from 1.8 hand-crafted ornamentation because this is the *entire artifact* drawn that way — every line is a calligraphic stroke — not one ornament dropped into an otherwise mechanical layout.

**1.12 Production-real material.** The artifact specifies a production-physical technique — foil, deboss, vellum, French fold, gatefold, edge-paint, letterpress bite — that exists outside the screen, *and* renders the screen approximation convincingly enough that the eye reads material rather than gradient. The Met's *Manus x Machina* catalog (2016); Pentagram's foil-spec for *The Folio Society*; Stripe Press hardcovers translated to product pages. Most attempts fail by stopping at the metaphor — a gold gradient labeled "foil" is not the move. Apex versions sell the illusion: angle-dependent specularity, paper grain visible under the foil, deboss casting a shadow that obeys the page's light source.

**1.13 Identity-system as artifact.** The deliverable is a multi-page manual specifying rules rather than a single application of them. The system *is* the artifact; the examples in the manual are evidence, not the product. Vignelli's American Airlines manual (1967); the NASA Graphics Standards Manual (1976); Pentagram for Slack (2023). The signature is that a reader could reconstruct dozens of unseen applications from the rules alone. Distinct from a portfolio of branded examples: a portfolio shows outputs; an identity-system artifact shows the grammar that generates them.

**1.14 Cartouche-bound figure.** Title, source, date, and ornament wrap the figure in a single decorative frame carrying its metadata. The cartouche makes the figure read as *plate* rather than as *illustration* — it asserts the figure is a finished thing with provenance, not a sketch dropped into running prose. Old cartography (Blaeu, Speed, Visscher), Renaissance scientific plates, contemporary stamp design, *National Geographic* map insets. The discipline: the cartouche must carry information (scale, projection, source, date), not merely decorate the edge.

**1.15 Kinetic headline.** A headline whose numbers, words, or marks animate to specific values as the reader scrolls — the headline IS the visualization. Apple keynote credit-sequence titling; Stripe Sessions landing pages; *The Pudding*'s "How Music Taste Evolved" opening. Requires bypassing React's render cycle via `useMotionValue`, `requestAnimationFrame`, or direct DOM mutation; setting state in a scroll handler will jank. The discipline: the headline must *land* on a stable, readable value — kinesis that never settles is decoration, not communication. See `references/medium-playbooks/scrollytelling.md` for the implementation pattern.

### When to deploy
When the artifact will be encountered cold — a reader arriving without context. The first 500ms decide whether they read further.

---

## 2. Informational wow

The artifact rewards attention. Density is earned; every element adds insight.

### Named moves

**2.1 The annotated chart.** Every peak, trough, and inflection labeled directly with what happened. The chart is annotated like the first sighting of a bird.

**2.2 Multi-scale view.** An inset that zooms into a detail while the main view gives context. Used in cartography, epidemiology, micro/macro economics.

**2.3 Small multiples at speed.** Instead of one overlaid chart with six series, six tiny charts side by side. The reader's eye compares without decoding.

**2.4 Provenance transparency.** The source, sample size, collection date, and caveats are visible, not footnoted. Honesty is aesthetic.

**2.5 Unexpected chart type fits better than the default.** A slope chart instead of a bar chart for pairwise comparison. A dot plot instead of a bar when precision matters. A horizon chart for a packed time series.

**2.6 The unexpected comparison.** Year-over-year restated as "days to return to baseline." Revenue per headcount instead of gross revenue. The reframe itself is the insight.

**2.7 Data-ink ratio approaches 1.0.** The chart's ink is the data. No gratuitous grid, border, shadow, legend-you-can-remove.

**2.8 The reveal structure.** Key finding stated up front; the body earns it. Not a mystery — a confident claim supported.

**2.9 Units and magnitudes calibrated.** Not "42 kWh" but "42 kWh (a laptop for 17 days)." Numbers become intuition.

**2.10 The honest null.** Empty states, caveats, and "we don't know" moments shown instead of hidden.

**2.11 Live-bound prose-figure-equation.** A single parameter scrub updates the equation, the figure, and the surrounding prose simultaneously; all three views of the same idea remain in lockstep. The form that defines 3Blue1Brown's manim explainers, Distill's interactive papers, Bret Victor's *Tangle* essays, Bartosz Ciechanowski's scroll-bound SVGs. Distinct from 3.4 live-binding to prose because it isn't just the number that updates — the *figure* and the *equation* track in parallel, so the reader sees the same fact in three notations at once. The triple binding is the move. See `references/medium-playbooks/explorable-explanation.md`.

**2.12 Invented notation with legend.** When standard chart forms cannot capture the phenomenon, invent a stable graphical vocabulary and teach it in a legend. Cornelius Cardew's *Treatise* (1963-67) — 193 pages of invented graphic notation for sound; Rudolf Laban's movement notation (1928); Otl Aicher's Munich '72 pictograms as invented vocabulary for human activity. The discipline is internal coherence: every symbol carries one meaning, the same meaning everywhere, and the legend is exhaustive. The artifact's grammar can be entirely invented if it is coherent within itself.

**2.13 No chart.** The apex chart for this data is none — a single number, a single sentence, or a small table. A subtractive move at the figure level. Edward Tufte's "the best statistical graphic is sometimes a sentence" (*Visual Display*, 1983); the *Financial Times*' habit of leading a complex story with one number set at display size. Counters the chart-reflex — the trained instinct to visualize everything. Sometimes the apex move is *not making a chart*: when the data is one number, a chart is decoration around it.

### When to deploy
When the reader is there to *learn something*. Density matters most for reference-grade artifacts; least for marketing.

---

## 3. Interactive wow

The artifact responds in ways that teach or delight. The interaction is the payoff, not chrome.

### Named moves

**3.1 Direct manipulation on the subject.** The reader drags a node in a diagram; the diagram updates. Not a slider off to the side — the thing itself is the control.

**3.2 Linked brushing.** Selecting a range in one view highlights the corresponding items in another. Best in multi-chart dashboards.

**3.3 Scrub-to-compare.** A before/after slider. A time-slider that animates a whole system. Works when the comparison is 1-D.

**3.4 Live-binding to prose.** Change a number via slider; the number appears inline in the surrounding paragraph and updates live. The text *is* interactive.

**3.5 The satisfying micro-interaction.** A button that animates like it was designed (subtle scale, color, haptic-feeling timing). A hover that feels physical.

**3.6 Keyboard-first affordance.** Space, arrows, single-letter shortcuts. Power users reward deeply keyboardable artifacts. Document the shortcuts visibly.

**3.7 The unnecessary-but-delightful detail.** A confetti burst when the optimizer converges. A chime when the goal is reached. Rare; earn it.

**3.8 Playback with scrubbable timeline.** For simulations: play, pause, step, speed, and a timeline you can drag to any point.

**3.9 Progressive disclosure on hover / focus.** Tooltip is the summary; click-for-detail is the essay. Layered information.

**3.10 Reproducible randomness.** A "shuffle" or "new example" button that generates a fresh variation. The artifact keeps giving.

**3.11 Constraint-propagation scrub.** Multiple numbers in a sentence are mutually consistent under a model; the reader clicks one to designate it the *output*, then drags any other to back-solve. The mortgage sentence "$400k at 6% over 30 years is $2,398/mo" becomes any-to-any: click the monthly payment to lock it, drag the rate to see required principal. Bret Victor's *Tangle* (2011) sketched this; the full move — *any number can be the output* — is the version most explainers don't expose. See `templates/react-simulator-victor.tsx`. Distinct from 3.4 live-binding because in 3.4 the slider has a fixed role; here the reader chooses what is independent.

**3.12 Section-as-control.** A single architectural section through a complex system is the primary interaction surface — the reader peels layers, scrubs a depth slider, or hovers a stratum to reveal what occupies it. The control isn't beside the diagram; the diagram IS the control. Used in geology cross-sections, ship cutaways, anatomical layered viewers (Visible Human Project), London-Underground tunnel sections, semiconductor die shots with click-to-label. The discipline: the section must be honest — the geometry has to be load-bearing for the explanation, not just a backdrop with hotspots.

**3.13 Dialectical cut (Eisenstein).** Scrollytelling scenes intentionally dissonant; the meaning emerges from the reader's synthesis of two adjacent scenes that should *not* match. Most scrollytelling uses continuity editing — each scene resolves smoothly into the next. Dialectical cuts hard, in Sergei Eisenstein's *Strike* (1925) sense: shot of strikers being shot, cut to shot of cattle being slaughtered, meaning made in the reader's head. *The Pudding*'s harder pieces use this; the *New York Times* "Snow Fall" did not. Distinct from 6.4 the structural twist because the dissonance is *scene-to-scene local*, not whole-artifact.

### When to deploy
When the artifact's subject is inherently temporal, comparative, or spatial. When the reader benefits from exploration over static inspection.

---

## 4. Technical wow

A hard thing is made to look easy.

### Named moves

**4.1 Impossible-feeling performance.** A million-point scatter plot that pans smoothly. An in-browser simulation at 60fps.

**4.2 Procedural generation.** Content generated at render time from parameters, so every visit shows a slightly different (but consistent) variant.

**4.3 Physical simulation in-browser.** Springs, particles, fluid, gravity — a toy that feels like a real thing.

**4.4 Custom motion from first principles.** Animations keyed to a physics function, not a CSS preset. They feel real.

**4.5 Deep integration with the real.** Live data fetched from a real API (where the artifact medium allows). A chart that is current, not a snapshot.

**4.6 Self-contained complexity.** A full mini-application in a single file, offline-capable, no dependencies beyond the runtime.

**4.7 Responsive down to the tiniest viewport.** The artifact works on a watch as well as on a wall display. Adaptation is the feature.

**4.8 Offline-first.** No network dependency — an artifact that loads once and keeps working.

**4.9 Instant.** Zero loading states because everything is precomputed or streamed in such that perceived latency is zero.

**4.10 The production-grade detail.** Error states, loading states, empty states, edge cases — all designed. The artifact is a product, not a demo.

**4.11 Animation as uncertainty channel.** Hypothetical-outcome plots (HOPs), ensemble traces, animated draws from posteriors. The motion *is* the uncertainty — instead of static error bars, the chart cycles through plausible realizations, and the reader's eye integrates the variation. Kay, Kola, Hullman, and Munson's "When (ish) Is My Bus?" (CHI 2016) made the case; *FiveThirtyEight*'s election forecast trace plots inherit it. The discipline: the animation rate must be slow enough for the eye to register each draw (≈400-800ms per frame), and the sample count must be honest — not a smoothed loop of three favorites.

**4.12 Sonification as accessibility channel.** Web Audio binds a data series to tone — pitch to value, timbre to category, tempo to time. For some readers (blind, motor-impaired, eyes-occupied) and some data (cardiac rhythm, seismic traces, gravitational-wave chirps), the sound *is* the chart. NASA's *Sounds of the Sun* (2018); the LIGO chirp made the discovery legible to a hearing public; Florence Nightingale-trained nurses already auscultate. The discipline: sonification is not a novelty soundtrack — it is a primary representation, designed with the same care as the visual axis, with mute/replay controls and tonal range chosen for the reader's hearing, not the designer's preference.

### When to deploy
When the artifact is technical and the audience is technical. Craft is legible to them; they will notice and reward it.

---

## 5. Emotional wow

The artifact makes the reader feel something specific.

### Named moves

**5.1 Recognition.** The reader sees themselves. "Oh, that's *exactly* what it's like." Specificity beats generality.

**5.2 Earned payoff.** Buildup → pause → reveal. A moment the artifact has architected, not stumbled into.

**5.3 Quiet gravity.** Serious subjects handled with restraint. No decoration, no levity — the content is weighty and the design lets it be.

**5.4 Delight through surprise.** An unexpected move at an unexpected moment. Rare enough to land; frequent enough to make the artifact feel alive.

**5.5 Humor used sparingly.** A single funny aside, well-placed. Never a running commentary.

**5.6 The acknowledged reader.** The artifact addresses the reader as a specific person, with specific knowledge, respected. "You already know X; here's Y."

**5.7 Closure.** The artifact ends. It doesn't peter out, it doesn't end on a "thanks for reading." It ends on the strongest possible sentence.

### When to deploy
When the subject warrants it — narrative pieces, opinion pieces, retrospectives, memorials. Not appropriate for most dashboards.

---

## 6. Unexpected wow

The reader's mental model of "what this is" is disrupted in a useful way.

### Named moves

**6.1 Wrong medium, intentionally.** A schematic instead of a chart. A chart instead of a table. A timeline instead of a list. A choice that forces the reader to see the data differently.

**6.2 Uncommon chart type.** Chord diagram, Sankey, parallel coordinates, horizon, streamgraph — used because they *fit better*, not to show off.

**6.3 Vertical where horizontal is expected.** Long-scroll timeline, stacked rather than inline layout. Break the reader's preview.

**6.4 The structural twist.** The second half reframes the first. The conclusion inverts the setup.

**6.5 Data self-referentially.** The artifact analyzes itself (word counts, color usage, reading time). Light, playful, only when it fits.

**6.6 Deliberate minimalism where maximalism is the norm.** A single chart on an otherwise empty page. Where dashboards are dense by convention, the absence of density is the move.

**6.7 Deliberate density where minimalism is the norm.** A reference card or data-dense page when the reader expected a landing page. Tufte-grade density.

**6.8 Inverted register.** The artifact does the opposite of what its category expects in a way that *teaches more*. A dashboard that is a single sentence ("revenue is up 7%, driven by Europe; everything else is within noise"). An explainer with no controls. A 3D scientific viz rendered as ASCII. A children's book on quantum mechanics. The discipline: the inversion has to clarify the subject, not merely surprise the reader. Cousin of 6.1 wrong-medium-intentionally, but specifically *register-inversion* (the tone, density, or interaction-level is flipped) rather than *medium-inversion* (the form factor is flipped). A dashboard rendered as a haiku is a register inversion; a dashboard rendered as a sculpture is a medium inversion.

**6.9 Register-braid.** Two or three voices held in alternation across an artifact, legibly distinct, never collapsing into a single tone. Maggie Nelson's *The Argonauts* (2015) braids autotheory and memoir; Alison Bechdel's *Fun Home* (2006) braids graphic novel and literary essay; Anne Carson's *Nox* (2010) braids elegy, translation, and scholarly apparatus. The three rules: the braid must be **legible** (the reader perceives the switches), the registers must be **distinct** enough to read as separate voices, and the switches must **not be random** — there is a logic to when each voice speaks. Distinct from 5.4 delight through surprise because the alternation is *structural*, not local; the braid is the artifact's spine. See the Literary register entry in `references/editorial-voice.md`.

### When to deploy
When the job has been done a thousand times in the default way. The unexpected move makes the artifact memorable in a category full of forgettable work.

---

## 7. Teaching (pedagogical)

The artifact teaches better than the default of its category. Where Informational moves (§ 2) reward attention with insight, Teaching moves are explicitly *pedagogical* — they assume the reader is here to learn and they engineer the learning event. The discipline is the cognitive-science literature: retrieval practice, worked examples, metacognitive calibration, generative learning. The seven moves below name the highest-leverage teaching craft moves; they are interchangeable with the moves above and can be deployed alongside them. For the underlying theory, see `references/educational-scaffold.md` and `references/libraries/pedagogy-library.md`.

### Named moves

**7.1 Commit-before-reveal.** The artifact gates the answer behind a prediction the reader must submit — a multiple choice, a guess on a slider, a sketched curve. Only after commitment does the reveal unlock. Eric Mazur's peer instruction (Harvard, 1990s); Brilliant.org's problem chains; Veritasium's "predict first" videos; *Quantum Country*'s prediction prompts. The cognitive science: forced prediction generates the desirable difficulty that converts passive reading into encoding. Distinct from 3.9 progressive disclosure because the gate is *cognitive* (the reader must produce an answer), not merely interactive (a hover or click).

**7.2 Confidence-calibrated reveal.** The reader rates confidence (low/medium/high, or a 0-100 slider) before each reveal; the artifact accumulates a Brier score across the session; the closing screen shows where the reader was overconfident versus underconfident. The metacognitive scaffold *is* the lesson — by the end, the reader has learned the subject *and* learned where their intuitions failed. Used in medical education (NBME-style confidence-weighted scoring), Forecasting Research Institute calibration trainers, the *Good Judgment Open* tutorial track. The discipline: the confidence scale must be honest (no "very confident" default) and the closing must be specific (which topics, not a global score).

**7.3 Faded scaffold.** The same problem template presented across N instances loses scaffold features one at a time: fully worked example → fade the last step → fade the last two → blank. The reader is gradually pushed onto their own resources without ever being dropped. The Renkl and Atkinson worked-examples tradition (1990s-2000s); Sweller's cognitive load theory; Catrambone's sub-goal labels. *Brilliant* and *Math Academy* are the contemporary executors. The discipline: each fade step must remove exactly one feature, and the feature removed must be the next one the reader is ready to lose — not whichever is easiest to delete.

**7.4 Section-anchored review.** Every review item (flashcard, quiz question, recall prompt) links back to the paragraph that taught it; clicking the answer scrolls the source paragraph into view. The teaching loop closes — every test of memory becomes an opportunity to re-encounter the original explanation. Andy Matuschak and Michael Nielsen's *Quantum Country* (2019) is the signature implementation; the mnemonic medium tradition. The discipline: the anchor must be paragraph-precise, not section-precise — vague back-links break the loop. See `references/medium-playbooks/mnemonic-medium.md`.

**7.5 Minimum-difference example set.** The example sequence varies one feature at a time so the load-bearing variable is unambiguous. Engelmann's Direct Instruction (1960s-) — *Reading Mastery*, *Connecting Math Concepts* — is the disciplined version: two cats and a dog (not a cat and a fish), so "what makes it a cat" is isolated. The contemporary descendants are anki-style concept cards and the *Brilliant* problem progressions. The discipline: each example differs from its neighbor in exactly one dimension, and the dimension is the one being taught. Maximum-difference example sets teach nothing — they look varied but the load-bearing variable is invisible against the noise.

### When to deploy
When the artifact's primary job is to leave the reader knowing something they didn't know — not to inform, not to delight, but to *teach*. Reference cards, explainers, tutorials, courseware, clinical-pearl cards, scientific primers. A teaching move belongs in any artifact whose success is measured by the reader's later recall or transfer, not by their immediate engagement.

---

## Combining moves

- **One move** per artifact is the minimum, and usually the maximum that lands cleanly.
- **Two moves** work if they're in different categories (e.g., visual + informational) and don't compete.
- **Three or more** usually read as maximalism — chaos rather than craft. Pull back.

### Anti-pattern: the move salad
An artifact with ten signature moves feels like it's trying too hard. Restraint is itself a signature. The best artifacts have one obvious move and several quiet ones supporting it.

### How to pick
Before starting, ask:
1. What's the job? (explainer, dashboard, tool, essay, chart)
2. What's the reader's default experience with this job? (bored, impatient, skeptical, curious)
3. Which move, deployed well, would convert that default into engagement?

Pick one. Build the rest of the artifact in service of it.

---

## Anti-repetition rule

Across a session — or across the visible run of recent artifacts in your context — **do not consecutively repeat a signature move.** If your last shipped artifact's move was 2.1 (annotated chart) and the next request also calls for a chart, deploy a different informational move (2.5 unexpected chart type; 2.3 small multiples; 2.6 unexpected comparison) unless the repeat is *deliberate and earned* (e.g., the artifact is the second half of an explicitly paired set).

The point isn't variety for its own sake. The point is to fight the convergence pull: when one move worked, the trained instinct is to reach for it again. Resist. The space of moves is wider than the recently-used handful.

### End-of-turn declaration (required)

Every artifact ends with one line in the pre-delivery YAML block, even when shipped:

```yaml
signature_move_recency:
  used: "<move id>"
  last_3_visible: ["<move id>", "<move id>", "<move id>"]   # or "none-visible"
  breaks_pattern_because: "<one specific sentence>"
  # OR: repeats_by_intent_because: "<one specific sentence>"
```

A generic reason (≤ 6 words; "doesn't fit", "felt right") fails review. Be specific.

### Recency bias (additive scoring)

If the chosen signature move is in the bottom-quintile of your recently-deployed moves — or has never been deployed in the visible context — add **+0.5** to the wow-score gate. See `references/iteration-protocol.md` "Recency modifier" for the formal rule. **The modifier only relaxes the gate; it never sharpens it.** Novelty alone earns +0.5; novelty alone does not earn ship-clearance. An unfit novel move still has to pass the unmodified 8-gate on craft. Novelty is never a substitute for fit.

### Enforceability — the honest take

This rule binds in **three layers**, each weaker than the previous:

1. **In-context (always works):** within a multi-artifact conversation, Claude can see the last few moves; the end-of-turn declaration forces awareness.
2. **User-mediated ledger (opt-in, Project-scoped):** if `references/signature-move-ledger.md` is in Project Knowledge and the user appends post-delivery, Claude scans the last 10 entries on subsequent sessions.
3. **Harness-injected (Claude Code / Agent SDK only):** the `artifact-scaffold` skill reads `~/.claude/artifact-history.jsonl` (last 20 entries) and injects the move history into context automatically.

In a vanilla Claude.ai conversation with no project knowledge, Claude has no persistent cross-session memory; the anti-repetition rule depends on (a) what's visible in the current conversation and (b) the user maintaining a ledger if cross-session enforcement matters. **The end-of-turn declaration is the floor — it forces in-context awareness and creates an auditable record the user can carry forward.**

The rule's real power isn't enforcement. It's **naming**. By making "the move you used" an explicit, surfaced concept Claude must articulate at the end of every artifact, the rule changes what Claude attends to during generation. Naming creates noticing. Noticing creates the chance — not the guarantee — of choosing differently next time.

---

## Named-move registry

For quick reference when scaffolding:

| Category               | Move count |
|------------------------|-----------:|
| Visual                 |         15 |
| Informational          |         13 |
| Interactive            |         13 |
| Technical              |         12 |
| Emotional              |          7 |
| Unexpected             |          9 |
| Teaching (pedagogical) |          5 |

**54 named moves**, plus 5 A.x (Wave 4 sci/med), plus 5 B.x (Wave 8 body-of-work), plus 20 Wave 9 additions (1.11-1.15, 2.11-2.13, 3.11-3.13, 4.11-4.12, 6.8-6.9, 7.1-7.5) = **84 named moves**. Pick one; build the artifact around it. Invent the 85th when warranted — the taxonomy is a vocabulary starter, not a closed shortlist.

A separate **Body-of-work** dimension (B.1–B.5: signature progression; deliberate retreat; late-style turn; artist-as-curator; negative-space body) is documented further down. These are *cross-artifact* moves — not deployable in a single turn — and are tracked in `references/signature-move-ledger.md` rather than scored by the recency modifier.

---

## Additional named moves (Wave 4 additions for science/medicine creative work)

These five extend the taxonomy with moves drawn from the science-for-the-public and clinical-personal traditions. They sit alongside the 54 above and are interchangeable with them.

**A.1 Cosmic mascot.** A small recurring figure anchors scale across a long-form piece (Kurzgesagt's duck; Sagan's "pale blue dot" image). The mascot is not decoration — it's a consistency token that makes the reader feel located in the artifact's world.

**A.2 Scale-walk.** Sequence of scale-jumps from human-relatable to subject-scale (Eames *Powers of Ten*). The transitions are the argument — each jump teaches a different lesson about the orders of magnitude between us and the subject.

**A.3 Specimen plate.** Haeckel/Audubon grid composition for one taxon. Symmetry as composition; rigor visible *in* the aesthetic. Used when the artifact's job is to convey both fact and reverence at once.

**A.4 Clinical-personal dialectic.** Paragraph alternation between case detail and reflective frame (Gawande). Each clinical paragraph earns its reflective companion; each reflection earns its clinical anchor. Neither domain swallows the other.

**A.5 One pale blue dot.** A single anchor image whose interpretation is the entire argument. The image is small; the prose around it carries the weight. Sagan's eponymous passage is the canonical example — the photo is a pixel; the moral is everything.

---

## Body-of-work moves (cross-artifact)

The 54 + 5 (Wave 4) + 20 (Wave 9) = 79 moves above are *within-artifact* moves — moves an artifact deploys to be apex on its own terms. The five moves below are different: they emerge across a sustained body of work, over a career, over years. An artifact cannot deploy a body-of-work move; only a body of work can. They are named here so they can be acknowledged when present, refused when absent, and tracked across the ledger.

Apex bodies of work have shape that no single artifact can carry: a signature that hardens through repetition, a retreat that surfaces the signature's limits, a late style that violates the earlier rules, a curatorial stance, and a negative space defined by refusals. These are not optional flourishes for prolific authors — they are the dimension along which sustained work becomes coherent rather than merely numerous.

**B.1 Signature progression.** An author deploys one move dozens of times across years, with subtle variations. Bartosz Ciechanowski's scroll-bound SVG manipulator appears in *Watch* (2022), *GPS* (2019), *Internals of CPU* (2023), *Cameras* (2023), *Naval Architecture* (2021); each iteration teaches a different subject; the *move itself* becomes the author's signature. Trent Reznor's distinct synthesizer voicings across *The Downward Spiral*, *The Fragile*, *Year Zero*. Anish Kapoor's hollow-volume-as-form across *Cloud Gate*, *Sky Mirror*, *Descent into Limbo*. **The move:** the artist's signature is *the same move deployed at different problems*, not *different moves deployed at the same problem*. The signature isn't a brand applied on top — it is the way the artist sees, made visible by repetition. **When the move fails:** when each iteration is the move played safely; signature progression demands *subtle variation* (otherwise it's just repetition, and repetition without progression reads as a tic, not a signature).

**B.2 Deliberate retreat.** An author masters one move then publicly *refuses* it. Edward Tufte made his name on dense data viz; *Beautiful Evidence* (2006) includes things he'd previously condemned (rainbow-color landscape paintings, decorative typography in book design). David Foster Wallace's footnotes-as-second-voice in *Infinite Jest* (1996), refused entirely in *The Pale King* (2011, posthumous). Bob Dylan going electric at Newport (1965). **The move:** the retreat is *itself* a move; it surfaces the *limits* of the earlier mastery and forces the reader to ask what the earlier signature was *for*. The retreat works only against the prior signature — against the audience's settled expectation. **When the move fails:** when the retreat is unmotivated (just doing something different); apex retreat is *engaged with* the prior signature, not separate from it. A retreat that doesn't know what it is retreating from is just drift.

**B.3 Late-style turn.** Mature artists making work that violates their own earlier rules. Beethoven's late string quartets (Opp. 127-135, 1825-26) — sustained dissonance, formal idiosyncrasy, structural roughness Beethoven himself would have rejected at 30. Coltrane's *Ascension* (1965) — free-jazz density refusing the modal discipline of *A Love Supreme* (1964). Cézanne's late paintings — the surfaces visibly unfinished, the brushstrokes refusing the rendering convention. Bach's *Art of Fugue* (1742-50) — abstract, harmonically severe, refusing the affective surface of *Mass in B Minor*. Edward Said's *On Late Style* (2006) is the analytical text. **The move:** late style is *deliberate violation of your own prior signature* — and apex when the violation is *earned* by the prior mastery. The artist has the right to break the rule because the artist wrote it. **When the move fails:** when the "late style" is decline misnamed; the violation must be deliberate, not loss of facility. Real late style is harder than the early work, not easier.

**B.4 Artist-as-curator.** The artist makes a work *about other works* — the selection and ordering is the art. Bob Dylan's *Theme Time Radio Hour* (2006-2009) — Dylan as DJ; the song selection is the art. David Bowie's *Reality* tour setlist — career-spanning, deliberately ordered. MoMA's *Year One* installation — institutional curation as artistic statement. Robert Hass's *Essential Pleasures* poetry anthology (2010). Helen Vendler's *Poems, Poets, Poetry* (1996) — close-reading anthology as criticism. **The move:** *the selection itself* — what is included, what is excluded, the order, the framing — becomes the apex artistic act. The original works are the material; the curatorial act is the artifact. **When the move fails:** when the curator's hand is invisible (just a list of good things); apex curation makes the curator's argument visible through selection. A playlist without a thesis is not curation; it is inventory.

**B.5 Negative-space body.** The work an artist *refused* to make. Donald Knuth declining email after 1990 ("rewards from being deeply rooted in things outweigh rewards from disposable answers"). Cormac McCarthy refusing book tours, interviews, public readings. Sol LeWitt refusing to execute his own wall drawings (delegating execution while the instruction is the artwork). J. D. Salinger after 1965. Glenn Gould retreating from concert performance to recording-only after 1964. **The move:** the refusal *shapes* the body of work that exists. The absences are part of the artist's argument. Apex bodies of work have shape on *both sides of the line* — what they made AND what they declined. The negative space is legible; readers feel the refusal as a position. **When the move fails:** when the refusal is fear of judgment misnamed as principle; apex refusal is *more demanding* than compliance, not less. A refusal that costs the artist nothing is not a position.

### Tracking body-of-work moves

Signature progression, deliberate retreat, late style, artist-as-curator, and negative-space body are tracked in `references/signature-move-ledger.md` via a new `cross_artifact_signature` field on individual entries, and a periodic `## Body-of-work declarations` section that names which body-of-work moves the accumulated work is exhibiting. The recency modifier in `references/iteration-protocol.md` applies as usual to the *within-artifact* signature moves (the 79 above — the 54 originals, plus the 5 Wave 4 A.x, plus the 20 Wave 9 additions); the body-of-work moves are a separate dimension that doesn't trigger the +0.5 modifier — they are not artifact-level moves and can't be "deployed" in a single turn. Naming a body-of-work move in an artifact's pre-delivery YAML is *acknowledgment* of a pattern emerging across artifacts, not *deployment* of a move within one. The honest cadence is quarterly or per-milestone, not per-artifact: body-of-work moves are visible only in retrospect, against accumulation.

---

## Signature move, stated

Before shipping, complete this sentence out loud:

> The signature move of this artifact is: **______**, deployed by **______**, serving the job of **______**.

If the sentence feels forced — if the "move" is something generic like "good typography" or "clean layout" — you haven't chosen a signature. Go back and choose one.

<!-- END: references/wow-taxonomy.md -->

---

