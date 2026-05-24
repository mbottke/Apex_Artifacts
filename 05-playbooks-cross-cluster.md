# Apex-Artifacts — Cross-Cluster Forms (spine + 8 specializations)

Bundled from the apex-artifacts source repository. Each source file
is enclosed by `<!-- BEGIN: path -->` ... `<!-- END: path -->`
anchors so semantic retrieval and humans can locate the original.

## Files in this bundle

- `references/medium-playbooks/cross-cluster/_spine.md`
- `references/medium-playbooks/cross-cluster/gallery.md`
- `references/medium-playbooks/cross-cluster/catalog.md`
- `references/medium-playbooks/cross-cluster/retrospective.md`
- `references/medium-playbooks/cross-cluster/operating-manual.md`
- `references/medium-playbooks/cross-cluster/case-study.md`
- `references/medium-playbooks/cross-cluster/interview-artifact.md`
- `references/medium-playbooks/cross-cluster/meta-artifact.md`
- `references/medium-playbooks/cross-cluster/epistolary.md`

---


<!-- BEGIN: references/medium-playbooks/cross-cluster/_spine.md -->

# Cross-Cluster Playbooks — Shared Spine

For artifact forms whose job *crosses medium boundaries*. A gallery is essays and interactives and figures; a catalog is prose and photography and cartouches; a retrospective may include all four; an interview is transcript and editorial commentary and (sometimes) photographs of the speaker mid-sentence. These forms do not fit a single-medium playbook and are not well-served by long-form-document.md or dashboard.md or any of the 22 sibling files. This directory names what they share — the spine — and the per-form playbooks name what's distinctive.

**Read this file first.** Then read the per-form playbook for the artifact you're scaffolding. The spine carries 60% of the discipline; the per-form file carries the 40% that differs.

## Why cross-cluster?

The system's medium playbooks each cover a single medium: SVG, React, Mermaid, long-form prose, slide deck, notebook, dashboard. Each is opinionated about *that medium's* defaults. But an auction catalog is not a long-form document with figures — it is a *form* with its own conventions (lot numbers, provenance, condition reports, cartouches per item) that no single-medium playbook captures. A gallery is not a portfolio with a fancier index — it is a *form* whose curatorial argument is itself the artifact. An operating manual is not a technical document — it is a form whose adversarial reader is a tired novice at 3 a.m., not an engineer browsing decisions.

Eight such forms share one spine: each is a *selection-with-argument* — a body of items framed by an editorial voice that argues for the body of work, not the items individually.

## The shared structure

Every cross-cluster artifact has four positions. Not every position must be present; the absence of any is a deliberate move with a cost.

### Editorial framing

Every cross-cluster artifact has a *curatorial voice* — external to the contents, carrying an argument about what was selected and why. The voice is *named*: the gallery curator, the catalog editor, the retrospective committee, the manual's author, the interview's editor, the meta-artifact's writer, the epistolary's compiler. Anonymity is rare and costly; *"who selected this and why"* is the first question the reader brings, and the artifact must answer it within the first surface.

The framing voice is *external to the items*. The catalog editor's note is *not in the voice of the artists whose work is catalogued*. The interview editor's marginalia is *not in the voice of the speakers*. The epistolary compiler's footnotes are *not in the voice of the letter-writers*. The external voice is what distinguishes selection-with-argument from a dump.

### Selection discipline

What's in, what's out, what's left out *deliberately*. Every cross-cluster artifact's selection is itself the artistic act — see `wow-taxonomy.md` B.4 *artist-as-curator*. The curator's three jobs:

- **Define the scope.** "Best American essays of 2024" is a scope; "essays I liked" is not. "Pixar 1995–2020" is a scope; "Pixar movies" is not. A scope without a *cut* is not a scope.
- **Apply the cut.** Items in the scope that did not make the selection should be *acknowledged*. The reader who wonders "where is the Sebald?" must find an answer — either in the curator's note ("we considered the late Sebald essays and ultimately excluded them; the reasoning is on page xii") or in a visible omissions section.
- **Defend the cut.** The editorial framing names the principle. "We selected for argument-density, not for fame." "We chose work made during the second wave." "We took only items whose provenance is unbroken." The principle is *visible* in the surface, not buried in an afterword.

### Per-item commentary

Every item in a cross-cluster artifact carries editorial framing. The framing is *not* a summary of the item; it is the *curator's argument about why this item is in the selection*. A gallery's caption beneath an interactive is not "this is an interactive about gradient descent" — it is "this is the artifact that taught me what *parameter* means; it changed my teaching." A catalog's cartouche beneath a lot is not "Renoir, 1872, oil on canvas, 24 × 18 in" — it is *that*, plus the editor's one-paragraph claim about why this lot matters in the present sale.

The commentary is *short and load-bearing*. A miniature essay, not a paragraph of throat-clearing. See `wow-taxonomy.md` move 1.6 *editorial caption* — the convention is the same; the commentary makes a claim and lets the reader test it against the item directly above or beside it.

### Spine + leaves

The artifact's surface has a *spine* (the curatorial argument, encountered linearly) and *leaves* (the items themselves, encountered as the reader chooses). A reader can navigate spine-first (reading the editorial framing through, then jumping to items it has named) or leaf-first (jumping to items they recognize, with the editorial framing as ambient context).

The spine must be readable end-to-end without the leaves — a reader who reads only the editorial framing leaves with the artifact's argument. The leaves must be approachable without the spine — a reader who jumps directly to an item must not be lost; the per-item commentary carries enough context to stand. Both reading paths are first-class; both must be designed.

The structural test: cover the spine with your hand and read the items as a dump; if the dump still coheres, the spine is too thin. Cover the items with your hand and read the spine; if the spine reads as a list of one-line introductions, the spine is too thin in the other direction.

## Common anti-patterns

These appear across all eight forms; the per-form playbooks add specifics.

- **The dump-with-thumbnails.** No editorial argument; just a wall of items. Apparent breadth without any curatorial voice. The reader cannot tell what the curator thinks; the curator may not yet have a thought.
- **The puff-piece selection.** Every item is "great"; the editorial voice is uniformly admiring. The reader leaves unable to tell what is excellent from what is merely included. The cure is to name what was rejected and why.
- **The silent omission.** Something important is missing — a major work, a known correspondent, a known incident, a known era — but the absence is unmarked. A reader who knows the field feels the gap; a reader who doesn't is misled. Acknowledge the cut.
- **The hidden curator.** The artifact pretends to be objective ("this is the field's canonical retrospective"; "this is the standard manual") when curation is everywhere. Selection is a stance; the stance must be visible.
- **The throat-clearing commentary.** Per-item framing that summarizes the item rather than arguing for it. The reader who could read the item itself does not need a summary; they need the curator's claim.
- **The spine-only or leaves-only failure.** A surface that reads as editorial prose with the items relegated to thumbnails, or a wall of items with the curator's note buried at the end. Both readings — spine-first and leaf-first — must work.

## The eight forms

Brief sketches. Full playbooks in the per-form files.

- **Gallery / collection** (`gallery.md`). Landing page for N self-contained artifacts. Bret Victor's website; Nicky Case's index; The Pudding archive. The form earns its existence when the *order* of the items and the *editorial framing* together argue something specific about the body of work — *not* when it is a portfolio (career claim), *not* when it is a dashboard (decision), *not* when it is a long-form document (single sustained piece).

- **Curated catalog** (`catalog.md`). A bounded set of items each meriting per-item commentary, framed by an editorial voice. Christie's auction catalogs; Phaidon books of plates; Sotheby's lot lists; museum exhibit catalogs. Distinct from gallery: commissioned scope, exhaustive within scope, formal per-item conventions (cartouche, provenance, condition).

- **Retrospective / anthology** (`retrospective.md`). Career- or year-spanning selection. *Best American Essays*; MoMA *Year One*; Pixar 25-year exhibit; designer monographs; *The Believer*'s year-end issues. The editorial selection *is* the artifact; chronology is a tool, not a default.

- **Operating manual** (`operating-manual.md`). Aviation pre-flight checklists; OSHA safety manuals; restaurant opening procedures; some sections of the Google SRE Workbook. Imperatives only; safety-critical STOPs inline; the adversarial reader is a tired novice at 3 a.m., not a curious engineer.

- **Case study (business / design)** (`case-study.md`). Three-act structure (situation / decision / outcome) with quantified consequences. Heath Brothers; HBS cases; IDEO write-ups; Pudding-on-Pudding. Distinct from `clinical-case.md` (clinical reasoning) and from technical-document postmortems (incident analysis).

- **Interview / dialogue** (`interview-artifact.md`). Transcript + editorial commentary. *Paris Review*; *The Believer*; Studs Terkel oral histories; Svetlana Alexievich. Speaker labels typographically distinct; cuts marked; editor's commentary in marginalia.

- **Meta-artifact** (`meta-artifact.md`). Artifact about artifacts. Butterick *Practical Typography*; Rosenfeld *Information Architecture*; Norman *Design of Everyday Things*; this CLAUDE.md project. Every claim demonstrated *in the artifact's own surface*; the artifact is its own worked example.

- **Epistolary / correspondence** (`epistolary.md`). Letters as artifact. *Letters of Note*; *Selected Letters of Vincent van Gogh*; *Letters from Iwo Jima*; Joan Didion's letters; the published correspondence of any field's major figure. Distinct from interview: the writer is often dead, the addressee private, the document a window.

## When to invoke a cross-cluster form

The artifact's job genuinely *requires* selection-with-argument. Three tests:

1. **Is there a body of work?** If the artifact is a single sustained piece, use a single-medium playbook. Cross-cluster forms presuppose plural items.
2. **Is there a curatorial argument?** If the items can stand without editorial framing — a chart with one finding, a single essay — use a single-medium playbook. Cross-cluster forms presuppose that *what was selected and why* is itself the artistic act.
3. **Are the items heterogeneous in medium?** This is the strongest signal. A gallery of essays-and-interactives-and-figures has no single-medium home. The cross-cluster spine is the only place that handles selection-with-argument *across* media.

If yes to all three: cross-cluster. Pick the per-form playbook whose conventions best fit (catalog if exhaustive within scope; retrospective if career- or year-spanning; gallery if open-ended; operating manual if safety-critical procedural; case study if three-act; interview if dialogue-based; meta-artifact if self-referential; epistolary if letter-based).

If only two of three: probably a single-medium artifact with extra structure. Use the single-medium playbook and borrow from this spine where helpful.

## Cross-medium overlap

Many cross-cluster artifacts are *also* cross-medium (a gallery of artifacts from different media; a retrospective spanning print and web; a meta-artifact whose claims live in code and in prose). When this is the case, also read `cross-medium-patterns.md` (Wave 8) — the *artifact pair*, *series*, *campaign*, *sequel*, and *translation* patterns are independently relevant. A gallery of paired artifacts (each leaf is itself a pair of explanation + interactive) uses both this spine and the artifact-pair pattern.

## Cross-references

- `cross-medium-patterns.md` — pairs / series / campaigns / sequels / translations across media; relevant for any cross-cluster artifact whose leaves span media.
- `editorial-voice.md` — the *Literary* register fits catalog, retrospective, interview, meta-artifact, and epistolary; *Technical* fits operating manual; *Editorial-wonder* sometimes fits retrospective; *Editorial* fits gallery and case study most often.
- `wow-taxonomy.md` — move B.4 *artist-as-curator* names the spine's central claim; move 1.6 *editorial caption* is the per-item commentary convention.
- `apex-exemplars.md` — many cross-cluster exemplars (Pudding archive, Bret Victor's site, Stripe Press) are catalogued there; the per-form files name additional exemplars specific to their form.
- `exception-registers.md` — refusal and one-take registers occasionally apply to retrospective and epistolary (a refused retrospective; a one-take catalog); declare explicitly when invoked.
- `manifesto.md` — rule 12 (*the form serves the argument*) and rule 17 (*selection is the artistic act*) are the spine's foundation.

<!-- END: references/medium-playbooks/cross-cluster/_spine.md -->

---


<!-- BEGIN: references/medium-playbooks/cross-cluster/gallery.md -->

# Cross-Cluster Playbook: Gallery / Collection

For landing pages whose job is to *present a body of self-contained artifacts* so that a reader can find what they want and the author's voice across the body is felt. Bret Victor's website is the canonical example: a list of essays-and-interactives-and-talks framed by Victor's curatorial voice, ordered so that the *order itself* argues a position about his work. Nicky Case's index page does the same job in a different register. The Pudding archive — by-year, by-author, by-topic facets over a corpus of dozens of data-essays — is a third register.

**Read `_spine.md` first.** This file names what's distinctive to galleries. The spine carries editorial framing, selection discipline, per-item commentary, and the spine+leaves architecture.

## What this is, when to use, what it is not

A gallery is a *landing page for N self-contained artifacts*. The artifacts are the content; the gallery is the curation. Use when:

- You have a body of work (5–500 items) whose primary access pattern is *discovery by a returning reader or a first-time visitor*.
- The items are heterogeneous in medium (essays, interactives, figures, talks, posts).
- The body of work is *open-ended* — new items will land here over time; the gallery is the durable surface.

A gallery is *not*:

- **A portfolio.** Portfolios make a career claim ("hire me"). Galleries make a curatorial claim ("here is what I think connects this work"). The visitor's job differs.
- **A dashboard.** No metrics being surfaced; no decision being driven.
- **A long-form document.** The gallery doesn't sustain an argument across prose; the items do that internally.
- **An archive.** Archives are complete and chronological by default. Galleries are *selected* and ordered by argument.

## Non-negotiables

1. **The order argues.** A gallery's items are presented in an order — most recent first, by theme, by reading time, by argued grouping. The order is not "newest first by default"; the order is *chosen* and the choice is *visible*. The reader can tell within five seconds why item A precedes item B. (Bret Victor groups by theme — "media for thinking the unthinkable" precedes "scientific communication" precedes "tools" — and the grouping is itself the argument that these are his three intellectual projects.)
2. **Every item carries a per-item gloss.** A title alone is not a gallery item; a title with a one- or two-sentence claim is. The gloss is the curator's argument for the item's inclusion, not a summary of the item. See spine § *per-item commentary*.
3. **Year, medium, and reading time are visible per item.** The reader scanning a long list needs three facets at a glance. A 2017 essay is a different invitation than a 2024 interactive; a 4-minute read is a different commitment than a 90-minute deep dive. Surface the facets.
4. **No dead links; no abandoned items.** Every item in the gallery is currently accessible. An item that no longer reflects the author's thinking is either *acknowledged as such* (a note under the gloss) or removed. A gallery that includes work the author has disavowed without saying so is a gallery that has lost its curator.
5. **The author's curatorial voice is present in the framing.** A bare list with no editorial copy at the top is a dump. The framing — a paragraph at the top, a section intro between groupings — names what the reader is looking at and why it is here.

## Composition pattern

The canonical gallery has four bands, in vertical order:

1. **Curator's note.** A short editorial paragraph (60–200 words) at the top of the page. Names the body of work, the curatorial principle, and the invitation. Victor's note frames his work as *"tools for understanding"*; Nicky Case's note frames theirs as *"explorables for hard ideas"*; the Pudding archive's framing names *"journalism that reads like data"*. The note is in the author's voice and is *external to the items*.

2. **The selection.** Items in chosen order. Each item is a row or a card; the row carries title, gloss, year, medium icon, reading time. Cards group thematically; rows present a linear sequence. Choose based on whether the *grouping* or the *order* is the argument.

3. **Faceting (optional, for galleries > ~20 items).** Tags, year filters, medium filters, "start here" markers. Faceting is a *tool*, not a substitute for the curatorial order — when faceting is the only navigation, the gallery has degenerated into an archive.

4. **About / colophon.** A short section at the bottom: how the gallery is maintained, when it was last updated, the technical stack if relevant, a contact path. The colophon is the gallery's *meta-claim* — the artifact about how this artifact is kept current.

## Editorial voice

Most galleries use the *Editorial* register from `editorial-voice.md` — short sentences, claim-bearing prose, no decorative adjectives. The curator's note reads like an exhibit wall text: direct, opinionated, brief.

The *Warm-familiar* register works for personal galleries where the author is a known persona (Nicky Case's gallery reads as warm-familiar; the curator addresses the reader directly). The *Literary* register can work for a writer's gallery (a novelist's website organizing essays-and-criticism) but is rare; literary curators tend to disappear into their notes, which betrays the spine's *external voice* requirement. Avoid *Technical*; the gallery is not a reference.

## Anti-patterns

1. **The reverse-chronological dump.** Every item shown as "most recent first" with no other ordering principle. The reader sees what's new but cannot tell what's *important*. Order by argument, not by date; let faceting carry the chronological access pattern.
2. **The thumbnail wall.** A grid of screenshots with no titles or glosses. Looks designed; teaches nothing. The thumbnail is a *signpost*, not a *substitute* for the gloss.
3. **The "selected work" coyness.** "Selected work" as a section header with no principle named. The reader cannot tell what was de-selected or why. Either name the selection principle or drop the qualifier.
4. **The career puff.** Every item glossed as "this was a hit"; every gloss is admiring. The reader leaves with no sense of the author's taste because the author appears to like everything they have made. Galleries earn trust by *not* including everything.
5. **The orphaned legacy item.** A 2014 piece that no longer reflects the author's thinking, sitting in the gallery with no acknowledgment. Either annotate ("I no longer agree with this; kept because the comments thread is useful") or remove.
6. **The faceting-as-navigation collapse.** The gallery is *only* tags and filters; there is no curatorial order. The reader is given a search interface, not an argument. Faceting is a tool; the order is the argument.

## What 10/10 looks like

**Bret Victor's website (worrydream.com, ongoing).** The signature move: *grouping-as-argument*. Victor's work is organized into three groups — *"media for thinking the unthinkable"*, *"scientific communication"*, *"tools"* — and the grouping is itself his claim about what his work is *for*. Within each group, items are ordered with the most argumentatively load-bearing pieces first, not the most recent. The curator's note is one paragraph; the per-item glosses are one sentence each; the visual identity is *typography only*, no decoration. The reader leaves with a precise mental map of Victor's intellectual program — which is the gallery's job. See `apex-exemplars.md` § *Bret Victor*.

**The Pudding archive (pudding.cool, ongoing).** The signature move: *facet-and-feature together*. The archive offers chronological access via year, faceted access via tag, *and* a curated front page that features specific essays the editors want the visitor to start with. The three access patterns coexist; the curatorial layer is the front-page feature, the discovery layer is the facets, the completeness layer is the archive. The reader who knows what they want gets it via facets; the first-time visitor gets the curated invitation; both readers find the same body of work through different paths. See `apex-exemplars.md` § *The Pudding*.

Also worth studying: **Nicky Case's index page** (ncase.me) for warm-familiar curatorial voice with deliberate informality; **Distill.pub's archive** (distill.pub, 2016–2021) for academic-rigor gallery conventions, including paper-style facets (author, year, topic); **Stripe Press's catalog page** (press.stripe.com) for a gallery whose every item is a book-length artifact and the gloss is the book's pitch.

**Starter pattern** — the editorial top of a Bret-Victor-register gallery:

```html
<header class="curator-note">
  <h1>Tools for thinking, mostly about systems we don't yet have words for.</h1>
  <p class="lede">Twelve pieces from the past nine years, grouped by the
    question each one tried to answer. The order is argumentative, not
    chronological — start with whichever group sounds least obvious.</p>
</header>
<nav class="groups">
  <a href="#thinking">Media for thinking the unthinkable</a>
  <a href="#comms">Scientific communication</a>
  <a href="#tools">Tools that change the work</a>
</nav>
```

The note is one sentence of claim, one sentence of orientation. The nav names the three groups; the *grouping* is the gallery's central move.

## Ship checklist

- [ ] Curator's note present at the top: 60–200 words, claim-bearing, in the author's voice.
- [ ] Selection ordered by an argued principle (theme, register, importance); the order's logic is visible to the reader within five seconds.
- [ ] Every item carries a one-or-two-sentence gloss that *argues for inclusion*, not summarizes the item.
- [ ] Year, medium, reading time visible per item; facets surface them at scan distance.
- [ ] No dead links; no orphaned legacy items without acknowledgment.
- [ ] Faceting (if present) supplements curatorial order; does not replace it.
- [ ] About / colophon section at the bottom: maintenance, last update, contact.
- [ ] If the body of work spans heterogeneous media, also read `cross-medium-patterns.md` for the artifact-series pattern.
- [ ] The gallery's first-time-visitor reading path and the returning-reader reading path are both designed.

<!-- END: references/medium-playbooks/cross-cluster/gallery.md -->

---


<!-- BEGIN: references/medium-playbooks/cross-cluster/catalog.md -->

# Cross-Cluster Playbook: Curated Catalog

For auction catalogs, museum exhibit catalogs, plate-books, lot lists, collection catalogs, and any artifact whose job is to *describe each item in a bounded set with editorial precision*. Christie's and Sotheby's auction catalogs are the apex of the commissioned-scope form: a sale's worth of lots, each one with a cartouche of bibliographic data (artist, date, medium, dimensions, provenance, condition, estimate) plus an editorial entry of one or two paragraphs arguing for the lot's significance. Phaidon's plate-books (the *Phaidon Atlas*, *The Story of Art* in its hardback editions, the *20th-Century Art Book*) are the same form for non-commercial scope.

**Read `_spine.md` first.** This file names what's distinctive to catalogs. The catalog is the cross-cluster form whose per-item conventions are *most formal* — the cartouche is load-bearing, the editorial entry is bounded, the order is rarely chronological.

## What this is, when to use, what it is not

A catalog is *exhaustive within a defined scope*. The scope is the sale, the collection, the exhibit, the period. Inside the scope, every item gets the same level of treatment — same cartouche structure, same approximate word-count for the editorial entry, same image conventions. The catalog's authority comes from its *uniformity*; the reader trusts that the editor has applied the same standard to lot 1 and lot 247.

Use when:

- A bounded set of items requires per-item editorial treatment.
- Each item has structured metadata (provenance, dimensions, condition, attribution) that the reader expects to find in a consistent location.
- The set is *commissioned* or *fixed*: a sale, a gift, an exhibit, an authoritative collection. An open-ended body of work belongs in a gallery (see `gallery.md`).

A catalog is *not*:

- **A gallery.** Galleries are open-ended; catalogs are bounded. A gallery may grow over years; a catalog ships and is then archived.
- **A long-form document.** The prose is in service of the items, not vice versa. A catalog reader reads *items*, not chapters.
- **A price list.** A price list strips the editorial entry. The catalog's identity is the entry.
- **A reference work.** A reference work is queried; a catalog is browsed and re-read.

## Non-negotiables

1. **Every lot carries a cartouche.** The cartouche is the *structured metadata block* — artist or author, date, medium, dimensions, provenance, condition, current location or estimate. The cartouche's fields are uniform across the catalog; the *order of fields is fixed* so the reader's eye finds dimensions in the same place on every page. Cartouche fields cannot be omitted; if a value is unknown, the field reads "*unknown*" or "*not recorded*", not silence.
2. **Every lot carries an editorial entry.** One or two paragraphs (typically 60–250 words) arguing for the lot's significance in this catalog. The entry is *not* a wall-text summary of the work; it is the editor's claim about why this lot belongs here, what it argues alongside the other lots, what makes it remarkable in the present sale or exhibit. The entry is signed (or initialed) when the catalog has multiple editorial voices.
3. **Provenance is exhaustive or marked.** The provenance chain is given from the artist's studio (or origin) to the present consignor, with gaps marked *"[provenance gap, c. 1940–1962]"*. A catalog that smooths over a provenance gap is a catalog complicit in opacity. The reader of a 20th-century Old Master catalog needs to see the gap *because the gap may mean what they think it means*.
4. **Condition is honest.** Condition reports name flaws specifically — "scattered foxing throughout; tear on lower edge, 3cm, restored" — not generically ("good condition"). The buyer at auction acts on the condition report; the reader of an exhibit catalog uses condition to gauge what they're seeing. Generic condition statements are catalog malpractice.
5. **The order is editorially argued.** Catalog ordering is rarely chronological. Auction catalogs group by category (paintings, prints, manuscripts, decorative arts); within category, by an editorial principle (the most important lot first, then descending; or building to the centerpiece; or the curator's preferred narrative). Phaidon plate-books often interleave epochs to argue continuities. The order's logic is named in the editor's introduction.

## Composition pattern

A catalog has six standard positions:

1. **Foreword.** A short essay (300–800 words) by the curator, editor, or department head. Frames the sale or collection: what it is, why it has been assembled, what the reader should look for. The foreword is the *spine of the spine* — the curator's argument in compressed form.
2. **Table of lots / contents.** Numbered list of lots with one-line titles and page references. A reader who wants to navigate to lot 47 must find it within seconds.
3. **Essays (optional).** For substantive catalogs, one or two scholarly essays preceding the lots. These contextualize the field; they are signed and footnoted. Essays are the move that distinguishes a *scholarly* catalog from a sale catalog.
4. **The lots.** The catalog's body. One or more lots per page; large lots get a full page or a spread. The cartouche sits in a fixed position (typically below the image or to its right); the editorial entry sits below the cartouche.
5. **Indices.** By artist or author, by provenance, by date, by subject. For substantial catalogs (> 50 lots), the indices are *non-optional* — the reader will return to the catalog for reference and must find their way back to a specific lot.
6. **Colophon.** Print run, paper stock, typography, editor and contributor credits, photographic credits, copyright. The colophon is itself a *signal* of the catalog's seriousness; a glossy catalog with no colophon reads as marketing.

## Editorial voice

The *Literary* register from `editorial-voice.md` fits most catalog entries. Christie's and Sotheby's editorial entries permit (require, even) earned adjectives — *trenchant*, *attribution-defining*, *singularly preserved* — that the Editorial register would prune. The Sullivan / Malcolm register, scaled down to two paragraphs per lot, is the form. Specific claims, named adjectives, no decoration.

Phaidon plate-books often use the *Editorial-wonder* register — the entry argues for the work's place in art history with warmth and named consequence. Museum catalogs vary by institution: MoMA tends Editorial; the Met tends Literary; the V&A tends Editorial-wonder.

Avoid *Warm-familiar* (too casual; the catalog is a formal document) and *Technical* (strips the editorial argument; turns the catalog into a database).

## Anti-patterns

1. **The provenance smoothing.** The chain reads "Private collection, Europe, 1920s; private collection, USA, present" — i.e., a 100-year gap rendered as two phrases. The buyer who acts on this catalog has been misled; the catalog's editor has chosen marketability over honesty. Name the gap; name the consignor.
2. **The generic condition statement.** "Good condition" or "as expected for age" with no specifics. A buyer at the hammer cannot inspect the lot at this distance; the condition report is their proxy. Generic condition is malpractice.
3. **The throat-clearing entry.** The editorial entry summarizes what the image already shows. *"This painting depicts a woman holding a flower in a garden setting."* The reader has eyes. The entry must *argue*, not describe.
4. **The puff-piece scholarship.** Every lot in the sale is "remarkable", "exceptionally well-preserved", "one of the finest known examples". The reader cannot calibrate; *everything* is at the top of its category. Calibrate by including ordinary lots in plain language.
5. **The hidden estimate / unsigned entry.** The estimate is in fine print at the back; the entry is unsigned. A catalog reader is buying or reading on the editor's authority; the estimate and the signature are the editor's stake in the entry.
6. **The thematic-order collapse.** All lots in date order with no editorial reordering. The order is "what we have, when it was made"; there is no curatorial argument. Catalogs whose only ordering is chronological have abdicated the central editorial move.

## What 10/10 looks like

**Christie's auction catalogs, c. 1990–present, particularly the *Important Old Master Paintings* sales and the *Magnificent Jewels* sales.** The signature move: *per-item commentary is a miniature essay*. A Constable in a 2018 sale carries a 220-word entry that names the *attribution history* (who attributed it when, on what basis), the *exhibitions* in which it has hung, the *literature* in which it has been discussed, and the editor's claim for its current significance. The entry is signed (or initialed); the cartouche is exhaustive; the provenance is given from the artist's studio. The reader of the catalog can act on the editor's argument because the editor has *staked* the argument. See `apex-exemplars.md` for catalog conventions; the Christie's *Magnificent Jewels* catalog of November 2019 (Geneva) is one to study for cartouche discipline at extreme density.

**Phaidon, *The Art Book* (1994, revised) and the *Atlas* series (Phaidon Atlas of Contemporary World Architecture, 2004).** The signature move: *the catalog itself reads as an argument about the field*. Phaidon's *Art Book* presents 500 artists in alphabetical order — but each one-page entry argues for the artist's place in a 20th-century history that is, by the end of the volume, *visible only because the catalog has been assembled this way*. Reading the catalog cover-to-cover (which Phaidon dared to expect) reveals a thesis about modernism that no single entry states. This is the Sullivan-register essay distributed across 500 cartouches. See `apex-exemplars.md` for the Phaidon house style.

Also worth studying: **the Sotheby's *Important Manuscripts* catalogs** for provenance discipline at the highest level (some lots have provenance chains to the 14th century); **MoMA's *Year One* (2019) catalog** for the museum-retrospective register (overlap with `retrospective.md`); **the Steidl plate-books** for photographic-catalog conventions; **museum exhibition catalogs from the British Museum** for scholarly-essay-plus-cartouche integration.

**Starter pattern** — a single lot entry in catalog register:

```markdown
**Lot 47.** Constable, John (1776–1837)
*Hampstead Heath, looking towards Harrow*
Oil on panel, c. 1820. 24.8 × 30.2 cm.

Provenance: the artist's studio; by descent to Isabel Constable (d. 1888);
her bequest to the National Gallery, 1888 (acc. 327); deaccessioned 1971;
private collection, London (1971–2018); the present consignor.

Condition: panel sound; surface dirt; one small loss on the lower edge,
restored 1973. Recently re-varnished. Frame: contemporary, gilt, repaired.

The Hampstead pictures of 1819–1821 are now read as Constable's transition
from topographic study to weather-as-subject. This panel — smaller than
the canonical *Hampstead Heath* of 1821 — is the *experiment* the canonical
picture refined. The brushwork in the upper third is looser than anything
he had shipped to the Academy; the Harrow tower is the rightmost vertical,
not the central anchor. Read as a study; admit it has become a painting.
                                                                      — J.M.
```

The entry is 95 words; the cartouche is exhaustive; the editor's claim is staked.

## Ship checklist

- [ ] Foreword present: 300–800 words, curator's argument for the scope and the order.
- [ ] Every lot carries a uniform cartouche with fixed field order.
- [ ] Every lot carries an editorial entry of 60–250 words that *argues for inclusion*.
- [ ] Provenance is exhaustive or its gaps are explicitly marked.
- [ ] Condition reports are specific, not generic.
- [ ] Lot order is editorially argued; the order's logic is named in the foreword.
- [ ] Indices present for catalogs > 50 lots (artist, provenance, subject, date).
- [ ] Editorial entries are signed or initialed when multiple voices contribute.
- [ ] Colophon present: print run, paper, typography, credits.
- [ ] Cross-reference `cross-medium-patterns.md` if the catalog accompanies an exhibit (the catalog and the exhibit form an artifact pair).

<!-- END: references/medium-playbooks/cross-cluster/catalog.md -->

---


<!-- BEGIN: references/medium-playbooks/cross-cluster/retrospective.md -->

# Cross-Cluster Playbook: Retrospective / Anthology

For year-end best-of volumes, career monographs, *N years of X* retrospectives, themed anthologies, and any artifact whose job is to *select across a span of time and argue what the span has been*. *Best American Essays 2024* (Houghton Mifflin, ongoing since 1986) selects 20 essays from a year of American magazine publishing and the editor's introduction argues a thesis about that year. MoMA's *Year One: 1929* retrospective (2019) selected works exhibited or acquired in the museum's first year and argued what the museum's *founding stance* was. The Pixar 25-year exhibit at the Museum of Modern Art (2005) was a career retrospective whose editorial selection was Pixar's own argument about what its first quarter-century had accomplished. A designer's monograph — Vignelli's, Rams's, Sagmeister's — is the same form for a single career.

**Read `_spine.md` first.** Retrospectives are the cross-cluster form where *editorial selection most visibly is the artifact*. The works are the field; the selection is the argument.

## What this is, when to use, what it is not

A retrospective is *selection across a span*. The span may be a year (anthology), an era (movement retrospective), a career (monograph), or an institution's life (museum retrospective). Inside the span, an editor or committee chooses a subset and argues for what the span has been. The selection is the artistic act; the introduction is its statement; the items are its evidence.

Use when:

- The span is bounded and significant: a year, a decade, an institution's history, a career.
- The audience expects an editor's argument about the span, not exhaustive coverage. A retrospective *cuts*; an archive *includes*.
- The items are heterogeneous in source — an anthology pulls from many magazines; a monograph pulls from many clients; a museum retrospective pulls from many lenders.

A retrospective is *not*:

- **A catalog.** Catalogs are bounded by a sale or an exhibit; retrospectives are bounded by *the span*. A retrospective may accompany an exhibit and become a catalog (`catalog.md`), but its central act is selection across time, not description of a specific event.
- **A gallery.** Galleries are open-ended and current. Retrospectives are *closed* — the span is fixed; the volume is finite.
- **A portfolio.** Portfolios make career claims for one person, usually directed at potential clients. Retrospectives argue what *the field*, *the year*, or *the career* has been, and the argument is internal to the field's discourse.

## Non-negotiables

1. **The editor's introduction names the thesis.** A retrospective without an editorial argument is a list. The introduction (1,500–5,000 words; longer for major monographs) names what the span has been, what the selection privileges, and what the editor has *deliberately omitted*. *Best American Essays* introductions are exemplary: Robert Atwan and the year's guest editor jointly argue what the year produced.
2. **The selection is dated and indexed.** Every item carries its original date and original source. The reader scanning the table of contents can see, in the dates, the *shape* of the span the retrospective covers. A retrospective with undated items has destroyed the span it purports to argue about.
3. **What was left out is acknowledged.** Either in the introduction or in a dedicated section, the editor names *significant omissions*. *"We considered and excluded the X conversation; the reasoning is on page xxiv."* A retrospective that pretends to be exhaustive is dishonest; the cut is what makes the selection meaningful, and the cut must be visible.
4. **The order is editorially argued.** Chronological order is *one* option, often the wrong default. Many apex retrospectives interleave — placing a recent piece next to an early one to argue a continuity, placing two pieces from different eras side by side to argue a kinship. The editor's introduction names the order's logic.
5. **Permissions and provenance are clean.** Every reprinted work credits its original publication and copyright holder. A retrospective that has not done this work is unshippable; the convention is hard-coded into the form.

## Composition pattern

A retrospective has seven standard positions:

1. **Foreword (optional).** By the series editor or institution head. Frames the volume in the larger series or program (e.g., the series editor's foreword to *Best American Essays* sets the volume's role in the annual sequence).
2. **Introduction.** The guest editor's or curator's argument. 1,500–5,000 words; longer for substantive monographs. Names the thesis, the principle of selection, the deliberate omissions, the order's logic, and the invitation. This is the spine of the spine.
3. **The selection.** Items in the editor's order. Each item gets its original full text (anthology) or its full plate(s) (monograph / museum retrospective). Editorial per-item commentary is *brief* in anthologies (a contributor's note, a date, the original venue) and *substantial* in monographs (a paragraph arguing for the work's place in the career).
4. **Contributor notes / artist's notes (anthology only).** Each contributor's bio + sometimes a short *"on this piece"* note from the author. The contributor's note is *not* in the editor's voice; it is the contributor's own.
5. **What we left out (optional but apex).** A section naming significant omissions. *"This volume excludes the Substack-era essays of 2024; we believe they warrant their own anthology; the reasoning is below."* The omissions section is the move that distinguishes a confident retrospective from a defensive one.
6. **Indices.** By contributor, by source, by date, by theme. For monographs: by client, by year, by medium. The indices let the reader re-enter the volume for reference after the linear read.
7. **Permissions and acknowledgments.** Granular: every piece credits its original venue and copyright holder; every photograph credits its photographer.

## Editorial voice

The *Literary* register from `editorial-voice.md` is the default for retrospective introductions — Sullivan, Malcolm, Als, Lockwood, Boyer. The guest editor of *Best American Essays* is expected to write at the register of the essays they have selected; the museum curator of a major retrospective writes at the register of the field they are arguing about.

The *Editorial-wonder* register can work for retrospectives whose subject is wonder-bearing — a 25-year Pixar retrospective; a Hubble photographic retrospective. The warmth and the named consequence fit naturally.

The *Editorial* register fits design monographs (Rams's *Less and More*, Vignelli's monograph) where the argument is about craft principles and the prose should serve, not compete.

Avoid *Technical* (the retrospective is not a reference) and *Warm-familiar* (the formality of the form rejects casual address).

## Anti-patterns

1. **The exhaustive retrospective.** Every important piece from the span is included. The volume has 200 entries and no argument; the editor has abdicated the cut. The cure is to halve the selection and write the introduction that justifies the halving.
2. **The puff-piece monograph.** Every project in the designer's career is "iconic"; every essay in the year's anthology is "essential". The reader cannot calibrate; the editor's taste is invisible. Include some merely-good work alongside the apex and *say which is which*.
3. **The chronological default.** The volume is ordered by date with no editorial intrusion. The order argues nothing the dates didn't already argue. Interleave deliberately; place an early piece beside a late one to make a claim.
4. **The hidden omissions.** Significant works in the span are absent and unmentioned. A reader who knows the field feels the gap; a reader who doesn't is misled. Name the omissions.
5. **The framing-by-quotation collapse.** The introduction is a sequence of admiring quotations from the included works, glued together with light editorial prose. The editor has not made an argument; they have curated quotations. Read the volume and write the thesis.
6. **The retrospective-as-marketing.** The institution's retrospective is uniformly celebratory; *Year One* is a victory lap, not a reckoning. The reader notices; the apex retrospectives reckon (MoMA's *Year One* does; the retrospectives that don't are forgotten within a decade).

## What 10/10 looks like

**Best American Essays, c. 1986–present, particularly the volumes guest-edited by Susan Sontag (1992), David Foster Wallace (2007), Adam Gopnik (2008), and Jonathan Franzen (2016).** The signature move: *the guest editor's introduction argues a thesis about the year, and the selection is the evidence*. Sontag's 1992 introduction argues that the year produced essays whose form was straining against the magazine's word limits; the selected pieces are read in that light. Wallace's 2007 introduction argues that the essay form was being deformed by the rise of long-form journalism; the selection traces the deformation. The volume's authority comes from the unity of introduction and selection — each calibrates the other. See `apex-exemplars.md` for related forms.

**MoMA, *Year One: 1929* (2019), curated by Glenn Lowry and the founding-collection committee.** The signature move: *deliberate non-chronological intrusions*. The retrospective placed objects acquired in the museum's first year next to objects acquired in subsequent years that *answered* the founding choices, arguing a continuity between 1929 decisions and 2019 collections. The catalog's introduction was a reckoning, not a celebration: *Year One* names the omissions of the original 1929 program (the absence of work by women and artists of color) and traces the museum's later corrections. The retrospective is therefore not a victory lap; it is an institutional self-criticism with curatorial evidence.

Also worth studying: **The *Vignelli: From A to Z* monograph (2007)** for design-monograph register; **The Phaidon *Pixar: 25 Years of Animation* (2005) catalog** for studio retrospective conventions (overlap with `catalog.md`); **Studs Terkel's late-career anthologies** for oral-history retrospective (overlap with `interview-artifact.md`); **The *New Yorker* annual fiction issues** for periodical-retrospective patterns; **Stripe Press's *Working in Public* (Eghbal, 2020)** for the trade-monograph register.

**Starter pattern** — the editor's-introduction opening of an anthology retrospective:

```markdown
# The year the essay learned to be a thread

*Foreword by* the series editor.
*Introduction by* the guest editor (2026 volume).

In the twelve months covered by this volume, the American essay did three
things it had not previously done. It became serialised. It became *typed
into a public space* — Substack, the long thread, the Notes apps published
as-is. It became, sometimes, collaborative.

The twenty-three pieces I have selected argue these three transitions. I
have omitted — significantly — the Substack newsletters of [author A] and
[author B]; the reasoning is below in *What I left out*. I have included
two pieces whose form would have been excluded from any previous volume:
[piece] is a thread; [piece] is a chat transcript.

The order is not chronological. The volume opens with a thread (the form
is now load-bearing) and closes with a 9,000-word *New Yorker* essay (the
form is not yet superseded).
                                                                — H.M.
```

The introduction is 165 words and has already named the thesis, the cut, and the order's logic.

## Ship checklist

- [ ] Span is bounded and named in the title or introduction.
- [ ] Editor's or guest editor's introduction names a thesis about the span.
- [ ] Selection is dated; every item shows its original date and source.
- [ ] *What was left out* section is present or the omissions are named in the introduction.
- [ ] Order is editorially argued; if non-chronological, the logic is named.
- [ ] Permissions and copyright holders credited per item.
- [ ] Indices present for retrospectives > ~20 items.
- [ ] Contributor notes (anthology) or per-item editorial paragraphs (monograph) present.
- [ ] If the retrospective accompanies a physical exhibit, read `cross-medium-patterns.md` § *artifact pair*.
- [ ] If the volume is part of an annual series, read `cross-medium-patterns.md` § *series* for cross-volume conventions.

<!-- END: references/medium-playbooks/cross-cluster/retrospective.md -->

---


<!-- BEGIN: references/medium-playbooks/cross-cluster/operating-manual.md -->

# Cross-Cluster Playbook: Operating Manual

For aviation pre-flight checklists, OSHA safety manuals, restaurant opening procedures, equipment maintenance manuals, the procedural sections of the Google SRE Workbook, and any artifact whose job is to *guide a person through a sequence of operational steps*, often under pressure. The adversarial reader is a tired novice at 3 a.m., not a curious engineer browsing decisions. The manual must hold up at that hour.

**Read `_spine.md` first.** This is the cross-cluster form whose voice is *furthest from literary*. The editorial framing is minimal; the per-item commentary is replaced by per-step imperatives; the selection discipline is "the actions necessary to accomplish the operation, in order."

## What this is, when to use, what it is not

An operating manual is a *procedural document for performing an operation safely and correctly*. The operations may be safety-critical (pre-flight checklists, lockout-tagout procedures, anesthesia checklists) or merely high-stakes (restaurant opening, deploy procedures, lab teardown). The manual's authority comes from its *imperative discipline* — declarative actions, sequential order, gates inline.

Use when:

- The task is *procedural*: a sequence of steps that produces a determinate end-state.
- The reader will perform the task *under conditions where errors compound* — pressure, fatigue, distraction, novelty.
- *Doing it correctly* is more important than *understanding why*. (Reasoning belongs in a separate document; the manual is the procedure.)

An operating manual is *not*:

- **A technical document.** Technical documents (`technical-document.md`) record decisions, propose standards, analyze incidents. Manuals execute. An ADR is for engineers; a manual is for operators.
- **A tutorial.** Tutorials teach. Manuals do not assume the reader is learning; they assume the reader has been trained and is *performing*.
- **A reference.** References are queried as needed; manuals are followed top-to-bottom in a session.
- **A runbook.** Runbooks (a sub-genre of `technical-document.md`) are emergency-response procedures for engineers; their lineage is the Google SRE Workbook. Operating manuals overlap heavily and a 3 a.m. runbook may borrow heavily from this playbook, but operating manuals also cover non-emergency procedures (the daily open-up, the equipment check) that runbooks don't.

## Non-negotiables

1. **Imperatives only.** Every step is a command: *"Set the parking brake."* *"Connect the ground strap."* *"Confirm the door is latched."* Descriptive prose ("the parking brake is then set") is banned. The Boeing checklist, the FAA pre-flight, the WHO surgical safety checklist all enforce this — the imperative form is the *procedural register*. Indicative or conditional prose adds 200 ms of reading time per step and slows a tired operator past the failure threshold.
2. **Numbered steps, sequential, no skips.** Steps are numbered (1, 2, 3 — not bulleted). The numbers are load-bearing: operators speak them aloud during checklist execution ("checklist item seven, confirm"); supervisors verify by number; trainers refer to step 12 as a fixed location. Bullets without numbers cannot be referenced and degrade procedural discipline.
3. **Safety-critical STOPs inline, not in an appendix.** When a step is a *gate* — "STOP — do not proceed if X" — the stop is *in the step's body*, not in an annex the operator may not consult. Aviation checklists print *"CAUTION"* and *"WARNING"* inline as their own marked rows. OSHA manuals use the standard *DANGER / WARNING / CAUTION / NOTICE* hierarchy with each level visually distinct. Burying a gate in an appendix is the leading cause of preventable industrial accidents; do not do it.
4. **Pre-conditions are checked before procedure begins.** The first section of the manual is *not* the first step; it is the *preconditions* — equipment present, personnel qualified, environment safe, prior checklist complete. The operator confirms preconditions before starting; a manual that drops the operator into step 1 without precondition checking is a manual that assumes a context that may not hold.
5. **Errors and rollbacks are named.** When a step *can fail*, the failure modes and the rollback are named immediately after the step, not in a separate troubleshooting section. *"Step 4: pressurize to 80 psi. If pressure does not stabilize within 30 seconds, return to step 2 and inspect seal."* The operator who fails step 4 needs the rollback at step 4, not at page 47.

## Composition pattern

An operating manual has six standard positions:

1. **Title and scope.** The operation named; the equipment, system, or context to which the manual applies. *"Pre-flight checklist, Cessna 172, normal procedures, day VFR"*. A title without scope is unsafe; the operator may apply a manual to a context it does not cover.
2. **Preconditions.** Items that must be true before step 1 begins. Equipment present and inspected; personnel qualified and rested; environment within parameters; prior checklist complete. Pre-conditions are themselves a checklist.
3. **The procedure.** Numbered steps in sequence. Each step is an imperative; each step has its expected end-state ("door is latched, indicator green"); gates and warnings are inline.
4. **Decision tables (if X then Y).** For procedures that branch — *"if pressure < 60 psi, perform sub-procedure A; if 60–80, continue to step 9; if > 80, abort"* — use tabular triage, not nested prose. The table compresses the branch logic so an operator reading under load can find their case.
5. **Abort / rollback procedure.** A named procedure for when the operation cannot complete safely. The abort is its own checklist; the operator returns to a known-safe state without improvising.
6. **Sign-off / verification.** The operator signs (initials, electronic acknowledgment, supervisor confirmation) that the manual was followed. Sign-off is the audit trail; manuals without sign-off have no record of execution.

## Editorial voice

The *Technical* register from `editorial-voice.md` is the only option. Procedural register: short imperatives, no decoration, no warmth, no humor. The manual is in service of the operator's hands, not their interest. The voice is *unaccented* — no author persona; the institution speaks.

Avoid every other register. *Warm-familiar* is unsafe (the operator stops scanning). *Editorial-wonder* is unsafe (the prose competes with the procedure). *Literary* is unsafe (the operator at 3 a.m. cannot parse a subordinate clause). *Editorial* is too long-form. The Technical register is *required*.

## Anti-patterns

1. **Descriptive prose instead of imperatives.** *"At this point in the procedure, the operator would normally engage the parking brake before proceeding."* The operator does not need narration; they need a command. Cure: replace with *"Engage the parking brake."*
2. **Gates in an appendix.** Critical *do-not-proceed* conditions are listed in a separate safety annex the operator has not opened. Cure: every gate inline in its step.
3. **Steps without expected end-states.** *"Step 5: check pressure."* The operator does not know what *correct* looks like. Cure: *"Step 5: confirm pressure is between 60 and 80 psi; indicator should be green."*
4. **Branching as nested prose.** *"If the pressure is below 60, then if the temperature is also below 40 you should..."* The reader loses the tree. Cure: a decision table.
5. **Rollback in a separate document.** The operator who has just failed step 4 has to navigate to *"Troubleshooting, page 47"* and find their case. They will not. Cure: rollback inline with the step that may fail.
6. **No sign-off.** The manual is followed and no record exists. When something goes wrong, the investigation cannot reconstruct what was done. Cure: sign-off per major section.
7. **Step numbers reused or skipped.** Step 7 appears twice; step 4 is missing. Operators reference steps by number; reused or skipped numbers cause errors of reference. Cure: number sequentially and uniquely.
8. **Apologetic warning copy.** *"Please remember to take care when..."* The reader does not need politeness; they need command. Cure: *"WARNING: pressurized line; close valve before disconnecting."*

## What 10/10 looks like

**The FAA / aviation pre-flight and emergency checklists (FAA AC 120-71, Boeing 737 QRH, Airbus FCOM volume 3).** The signature move: *imperatives only; the adversarial reader is a tired novice at 3 a.m., not an engineer*. Aviation checklists have been refined over a century of accidents and near-misses. The form is uniform: brief imperative, expected end-state, *CAUTION* / *WARNING* inline, abort procedure named explicitly. The Boeing QRH (Quick Reference Handbook) is the apex: every procedure is single-page, every step has a confirmed end-state, every branch has a decision table. Pilots execute these checklists *while flying a malfunctioning aircraft*; the form has been pressure-tested by survival. See the FAA's Human Factors Design Standard (HF-STD-001) for the underlying ergonomic principles.

**The WHO Surgical Safety Checklist (2009) and Atul Gawande's *The Checklist Manifesto* (2009).** The signature move: *radical compression*. The WHO checklist is *nineteen items* covering pre-op, time-out, and sign-out for any surgical procedure worldwide. Each item is a single imperative; each item has been adopted because evidence shows its omission causes preventable harm. Gawande's book is the manifesto for the form. The checklist's apex move is *omitting everything that is not load-bearing* — pre-procedure briefings, casual conversation, the surgeon's preferred opening line are *not* in the checklist because they do not change outcomes. The discipline of the form is what it leaves out.

Also worth studying: **OSHA's standard hazard-communication manuals** for the DANGER / WARNING / CAUTION / NOTICE hierarchy; **the Google SRE Workbook chapter on runbooks** for digital-operations procedural register (overlap with `technical-document.md`); **the NASA Apollo flight crew operations manuals** for the manual that put humans on the moon; **anesthesia manuals (e.g., *Stoelting's Anesthesia and Co-Existing Disease*)** for clinical-procedural conventions; **restaurant opening manuals (the Danny Meyer kitchens, the David Chang prep manuals)** for high-stakes hospitality procedure.

**Starter pattern** — a single procedural section:

```markdown
## Section 4 — Engine start sequence

**Preconditions:** parking brake set, fuel quantity > 30%, weather within VFR.

1. **Master switch:** ON. Confirm panel lights illuminate.
2. **Beacon light:** ON. Confirm flashing.
3. **Fuel selector:** BOTH. Confirm detent.
4. **Mixture:** RICH. Push fully forward.
5. **Throttle:** ¼ inch open. No more.
6. **Propeller area:** CLEAR. Shout "CLEAR PROP"; wait two seconds.
7. **Ignition:** START. Release to BOTH when engine fires.

**CAUTION:** if engine does not fire within 10 seconds, release ignition,
wait 60 seconds for starter cooldown before retrying. *Do not crank
continuously past 10 seconds.*

**If engine does not fire after second attempt:** STOP. Refer to
*Section 4A — Engine start troubleshooting*. Do not flood the engine.

**Sign-off:** _____ (operator initials, time)
```

Seven imperatives, one inline caution, one named branch, one sign-off. The section is complete on a card.

## Ship checklist

- [ ] Title names the operation and the scope (equipment / context / conditions).
- [ ] Preconditions section present and itself executable.
- [ ] Steps are imperatives; numbered sequentially; no narrative prose.
- [ ] Every step has an expected end-state.
- [ ] WARNINGs, CAUTIONs, and STOPs are inline with the step they gate.
- [ ] Branches use decision tables, not nested prose.
- [ ] Abort / rollback procedure named explicitly.
- [ ] Sign-off / verification field present per major section.
- [ ] Voice is exclusively Technical register from `editorial-voice.md`; no warmth, no narration.
- [ ] If the manual is safety-critical, cross-reference `hard-gates.md` for the additional procedural-safety domain mode.
- [ ] If the manual is one of a procedural family (deploy / rollback / incident), cross-reference `cross-medium-patterns.md` § *series* for cross-document conventions.

<!-- END: references/medium-playbooks/cross-cluster/operating-manual.md -->

---


<!-- BEGIN: references/medium-playbooks/cross-cluster/case-study.md -->

# Cross-Cluster Playbook: Case Study (Business / Design)

For Harvard Business School cases, IDEO project write-ups, the Heath Brothers' *Made to Stick* and *Decisive* case sections, McKinsey project retrospectives, Pudding-on-Pudding (the Pudding's own meta-cases), and any artifact whose job is to *narrate a specific situation, the decision taken in it, and the quantified consequence that followed*. The case study is the genre of *learning from a single instance*; the rigor comes from the *quantification*, the *named stakeholders*, and the *explicit alternative path*.

**Read `_spine.md` first.** This file names what's distinctive to case studies. Note also `clinical-case.md` (the clinical-reasoning teaching case is a sibling form with a different rigor); business and design case studies share structure with clinical cases but differ in voice, evidence, and reader.

## What this is, when to use, what it is not

A case study is a *three-act narrative of a decision*: the situation that created the choice; the decision and its reasoning; the outcome and its quantification. The three acts are non-negotiable. A case without the third act is a proposal; a case without the first act is a victory lap; a case without the second act is a coincidence story.

Use when:

- A specific situation has produced a quantifiable outcome.
- The decision is *transferable* — the case's reader will face structurally similar choices and the case teaches them something about how to reason through such choices.
- Named stakeholders, dated events, and concrete numbers can be cited (or can be cited under pseudonym with the editor's note explaining why).

A case study is *not*:

- **A clinical case** (`clinical-case.md`). Clinical cases teach diagnostic reasoning under uncertainty in a medical context; the rigor is *differential-diagnostic* and the reader is a clinician-in-training. Business and design case studies teach *organizational* and *strategic* reasoning; the reader is a manager, founder, or designer.
- **A postmortem** (`technical-document.md`). Postmortems are incident analyses for engineering organizations; the rigor is *contributing-factor*. Case studies overlap with postmortems when the case is *an organizational failure*, but the genres differ in voice and audience.
- **A marketing testimonial.** Testimonials select for success; cases include failure. A case study that has no friction or trade-off is propaganda.
- **A retrospective** (`retrospective.md`). Retrospectives span; case studies focus. A case is a single instance studied in depth.

## Non-negotiables

1. **Three acts, named.** Situation → Decision → Outcome. The case must explicitly contain all three; the third is the most-often-skipped and the most load-bearing. If the outcome is not yet known, the case is *not yet a case* — it is a vignette.
2. **Quantified consequence.** The outcome carries numbers. "Conversion went from 2.3% to 4.1% over six weeks; revenue per user rose from $14.20 to $19.80." A case study whose outcome is *"the team felt better about the new process"* has no rigor. If the numbers are not available, the case is unwriteable — wait for the data or pick a different case.
3. **Named stakeholders.** The CEO, the head of design, the lead engineer, the customer who complained. Names (or named pseudonyms with the substitution disclosed) make the case *real*; a case where "the team" did "the thing" is a case the reader cannot reason about. Confidentiality concerns are addressed via pseudonym, not vagueness.
4. **The alternative path is named.** *"We considered X; we chose Y; X would have cost us Z."* Every case has a counterfactual the reader must be able to evaluate. The case that presents only the chosen path teaches nothing about how to choose; it teaches only what was done.
5. **What we'd do differently.** Every apex case ends with a *retrospective frame* — the editor's or protagonists' explicit answer to *"knowing what we know now, what would have been the better play."* This frame distinguishes cases that teach from cases that brag.

## Composition pattern

A case study has eight standard positions, arranged in three acts:

**Act I — Situation (≈ 30% of length)**
1. **Hook.** A scene that drops the reader into the moment of decision. *"It was 11 p.m. on a Thursday in February when the head of growth refreshed the dashboard and saw the number."* The hook is the case's first 100 words; it must place the reader.
2. **Context.** The organization, the market, the constraints. Quantified where possible — revenue, headcount, runway, market share. The reader needs to know *what kind of decision this is*.
3. **The forcing function.** What made the decision unavoidable. A deadline; a competitor; a regulatory change; a customer threat; a financial constraint. Without a forcing function the case is *strategy in the abstract*; with one it is *strategy under load*.

**Act II — Decision (≈ 35% of length)**
4. **Options considered.** Three to five alternatives, each described with the seriousness it would have received at the table. A two-line dismissal of an alternative is a dismissal of the reader. The options are *enumerated*; the reader can map their own situation onto the list.
5. **The choice.** Which option was chosen and the reasoning. Named in active voice with a named decider. *"Sarah Chen, head of growth, chose option B."*
6. **The execution.** What was actually done — the specific actions, the timeline, the assignments. Cases often skim execution; apex cases show it because *execution is where decisions become outcomes*.

**Act III — Outcome (≈ 35% of length)**
7. **The quantified result.** Numbers over a stated period. Multiple metrics where decisions affect multiple metrics — revenue *and* churn *and* customer satisfaction, not just revenue.
8. **What we'd do differently.** The retrospective frame. The protagonists or the case editor names the counterfactual the case now sees. Apex cases include *what is still unresolved* — the questions the case raised that the protagonists have not yet answered.

## Editorial voice

The *Editorial* register from `editorial-voice.md` is the default — short sentences, claim-bearing prose, the case's argument carried by named consequence. Heath Brothers' register, Stripe Press's register, the better Pudding-on-Pudding pieces all operate here.

The *Editorial-wonder* register fits some design case studies (a case about the IDEO development of the original Apple mouse; a case about the Nest thermostat) where the consequence-of-design warrants warmth. Use sparingly; the case's evidence base is colder than wonder.

The *Literary* register fits long-form magazine cases (the *New Yorker* business profile; the *Atlantic* deep dive on a specific company). Reach for it only when the case is genuinely essay-length (8,000+ words) and the prose is itself an argumentative act.

Avoid *Warm-familiar* (cases are formal documents) and *Technical* (cases are not references; the technical register strips the narrative).

## Anti-patterns

1. **The marketing case.** Every protagonist is heroic; the company is uniformly competent; the outcome is uniformly excellent. The reader cannot learn from a case where nothing went wrong. Cure: include the failed alternative, the false start, the team conflict.
2. **The unquantified outcome.** *"We saw significant improvements in user engagement."* What numbers? Over what period? Compared to what? The reader cannot reason about *significant*. Cure: name the metrics, the baseline, the period.
3. **The unnamed team.** *"The team decided..."* Which team? Decided what? Led by whom? Cases without named deciders are cases without accountable reasoning. Cure: name them (or pseudonymize them and say so).
4. **The single-path narrative.** Only the chosen option is described; the alternatives are absent. The reader cannot evaluate the choice. Cure: name three alternatives and engage each.
5. **The hindsight-clean rationale.** The decision is presented as obvious in retrospect; the case obscures the doubt and the dispute that preceded it. Cures: include the dissenting voice; cite the meeting where the choice nearly went the other way.
6. **The unfinished case.** Outcome is "we're still measuring" or "it's too early to tell". The case isn't a case yet. Cure: wait or pick a different instance.
7. **The hagiography.** The case is uniformly admiring of the protagonists. Even the *what we'd do differently* section reads as humblebrag. Cure: include something the protagonists got wrong and would not have known to get right at the time.

## What 10/10 looks like

**Harvard Business School cases, c. 1985–present, particularly the operations and strategy cases (e.g., *Southwest Airlines: In a Different World*, *IDEO Product Development*, *Toyota: Origins, Evolution, and the Current Crisis*).** The signature move: *named stakeholders, quantified consequences, explicit counterfactual*. HBS cases are written to be discussed in class — the case must support 90 minutes of structured argument among 80 MBAs. The form has been refined since 1925; the discipline is total. Every protagonist is named; every number is sourced; every alternative is taken seriously. The case is followed by *teaching notes* (separately distributed) that name the case's pedagogical purpose and the discussion's expected arcs. Cases are the curriculum's spine; the spine has carried a century of business education.

**The Heath Brothers' *Decisive* (2013) and *Made to Stick* (2007).** The signature move: *the case as evidence for a generalizable principle*. The Heaths embed case studies inside a larger argumentative structure — the case is recruited to demonstrate a principle (*"the value of considering alternatives"*, *"the cost of confirmation bias"*) named earlier in the chapter. The cases are compressed (often 200–600 words) but rigorous: quantified outcome, named decider, alternative path, retrospective frame. The Heaths are the apex of the *teaching* case as opposed to the *examination* case (the HBS form). The teaching case earns its place by being *recruitable to a principle*; the examination case earns its place by being *complex enough to sustain disagreement*. Both forms are apex; the genre admits both.

Also worth studying: **IDEO's project write-ups** (the *Cardiogram* case; the *Cooper-Hewitt* case) for design-case register; **Pudding-on-Pudding** (the Pudding's own retrospectives of their pieces; e.g., *"How we made [piece]"*) for the meta-case register; **Stripe Press's *High Growth Handbook* (Gil, 2018)** for compressed case patterns; **McKinsey's quarterly case retrospectives** (those that are public) for consulting-firm register; **the Long Now Foundation's *Reviving Extinct Species* case archives** for sustained scientific cases.

**Starter pattern** — the opening of an HBS-register case:

```markdown
# When the dashboard refreshed: a pricing decision at Acme Logistics, Q1 2024

It was 11:14 p.m. on a Thursday in February when Sarah Chen, head of growth
at Acme Logistics, refreshed the dashboard for the fifth time and saw the
number she had been hoping not to see. Free-trial-to-paid conversion had
dropped from 18% to 11% over the four weeks since the company had moved its
starter plan from $29/month to $49/month. Twelve days remained in the quarter.

The forcing function was specific. Acme had committed to investors at the
seed extension three months earlier that Q1 ARR would close at $4.2M; the
revised conversion implied $3.6M. Sarah had two weeks to recover six
percentage points of conversion or two million dollars of forecasted ARR —
or to recommend, formally, that the company miss its commitment.

Three options were on the table by 7 a.m. the next morning. ...
```

The first 200 words have placed the protagonist, the moment, the number, the deadline, and the forcing function. The reader is in the case.

## Ship checklist

- [ ] Three acts present and structurally distinct: Situation, Decision, Outcome.
- [ ] Hook in first 100 words places the reader in the moment.
- [ ] Context is quantified (revenue, headcount, market position, runway).
- [ ] Forcing function is named explicitly.
- [ ] Three to five alternatives described with equal seriousness.
- [ ] Choice attributed to a named decider in active voice.
- [ ] Execution is shown, not skimmed.
- [ ] Outcome is quantified over a stated period with multiple metrics.
- [ ] *What we'd do differently* section present; counterfactual named.
- [ ] No marketing voice; protagonists may have been wrong; alternatives may have been right.
- [ ] If the case is part of a series (Pudding-on-Pudding, HBS teaching set), cross-reference `cross-medium-patterns.md` § *series*.
- [ ] If the case is *self-referential* (a case study of how the case was made), cross-reference `meta-artifact.md`.

<!-- END: references/medium-playbooks/cross-cluster/case-study.md -->

---


<!-- BEGIN: references/medium-playbooks/cross-cluster/interview-artifact.md -->

# Cross-Cluster Playbook: Interview / Dialogue

For *Paris Review* interviews, *The Believer* interviews, *BOMB Magazine* interviews, Studs Terkel's oral histories (*Working*, 1974; *Hard Times*, 1970), Svetlana Alexievich's polyphonic documentaries (*Voices from Chernobyl*, 1997; *Secondhand Time*, 2013), the *New York Times Magazine* by-the-book column, *Conversations with Octavia Butler* (University Press of Mississippi series), and any artifact whose primary content is *transcribed speech, framed by editorial apparatus*. The interview is the cross-cluster form whose voice is *least* the editor's: the editor curates, but the speakers speak.

**Read `_spine.md` first.** This file names what's distinctive to interview artifacts. Note also `epistolary.md` (correspondence is interview's sibling form, but the writer is often dead and the addressee private).

## What this is, when to use, what it is not

An interview artifact is *transcribed dialogue* shaped by editorial decisions about *what to include, what to cut, where to insert framing*. The interviewer's questions and the speaker's answers are the surface; the editor's selection and pacing are the spine. *Paris Review* interviews are the canonical literary form: a single speaker (a writer), several hours of recorded conversation distilled to 8,000–15,000 words, with the interviewer's questions in roman and the speaker's answers in roman of a different leading, the result reading as a polished essay-in-dialogue.

Use when:

- The speaker's *voice* — not just their information — is part of the artifact. The interview reveals *how this person thinks*, not only what they think.
- The exchange is itself the form. A monologue would have been simpler; the dialogue's friction is the point.
- The speakers are *living* (or recently living, with consent secured for posthumous publication). For non-consensual or dead speakers, see `epistolary.md` (letters) or the historical-interview conventions in academic oral history.

An interview artifact is *not*:

- **A transcript.** A raw transcript includes ums, false starts, redundancies, and the chronological order of the conversation. An interview artifact *edits*: cuts, reorders for thematic coherence, occasionally consolidates. The editing is disclosed.
- **A Q&A blog post.** Q&A formatted with bold "Q:" and "A:" labels and no editorial apparatus is the *low end* of this form. Apex artifacts have substantial editorial framing, typographic distinction, and marked cuts.
- **A profile.** Profiles (the *New Yorker* form) are essayistic; the writer is the narrator and the speaker is the subject. Interview artifacts foreground the speaker; the editor's voice retreats to apparatus.
- **A podcast.** Podcasts are audio-native; the medium is the form. An interview *transcript* of a podcast is a different artifact and is rarely apex unless re-edited with print conventions.

## Non-negotiables

1. **Speaker labels are typographically distinct.** Reader must distinguish speakers at scan distance. *Paris Review* convention: interviewer's questions in italic with the magazine's masthead caps ("INTERVIEWER:"), speaker's answers in roman. Studs Terkel's convention: speaker's name in small caps as a section heading, no interviewer voice (questions cut entirely, leaving only the monologue). Alexievich's convention: speakers identified by name and brief epithet at the head of each block (*"Anna Ivanovna, schoolteacher, age 64"*). Pick a convention and hold it across the artifact.
2. **Cuts are marked.** When material is removed mid-answer, the cut is shown — typically with bracketed ellipsis *[…]* or a section break. The reader who suspects the editor has smoothed something deserves to see where. A cut that is not marked is an *edit pretending to be a transcript*; it is the form's central dishonesty.
3. **The editor's commentary lives in marginalia or framing, not interpolated.** The editor does *not* insert paragraphs of interpretation into the dialogue. Editor's framing belongs in the introduction (before the dialogue), in footnotes (after the page), or in marginal notes (alongside, typographically distinct). The dialogue's surface is the speakers'; the editor's surface is everywhere else.
4. **Consent and provenance are disclosed.** When and where the interview was recorded; how long the conversation was; how much was cut; whether the speaker reviewed the final text; whether the speaker has been quoted accurately by their own account. *Paris Review* discloses these in the introduction. Oral histories (Terkel, Alexievich) disclose them in the front matter. An interview that elides its production conditions is an interview the reader cannot trust.
5. **The interviewer is named or deliberately effaced — never accidentally so.** *Paris Review* names every interviewer in the introduction; Alexievich erases the interviewer's voice entirely as a structural move (the speakers speak *to history*, not to her). The decision must be deliberate; *"the interviewer (an anonymous figure)"* is not a default.

## Composition pattern

An interview artifact has six standard positions:

1. **Introduction.** The editor's framing — who the speaker is, when and where the conversation took place, how it was conducted, what the reader should know to read what follows. *Paris Review* introductions are themselves miniature profiles (600–2,000 words). For oral histories, the introduction is the volume's thesis — Terkel's *Working* introduction names the question every speaker is implicitly answering.
2. **The dialogue (or polyphonic sequence).** The interview's body. For a single-speaker form: interviewer's questions and speaker's answers in alternation, typographically distinct. For a polyphonic oral history: a sequence of monologues from named speakers, organized thematically (Terkel groups by occupation; Alexievich by an emotional or chronological arc).
3. **Marginal apparatus (optional but apex).** Editor's notes alongside the dialogue: dates, clarifications, named references the reader may not catch. Conventionally in a smaller type or a marginal column.
4. **Photographs / portraits (optional).** A portrait of the speaker, often at work or at home. *Paris Review* runs facsimile manuscript pages alongside its interviews; *BOMB* runs portraits. The image is not decoration; it shows the speaker in their context.
5. **Endnotes.** Substantive editor's annotations: cited works, dated references, biographical sketches of named persons, contextual notes for the historical reader.
6. **Colophon.** Recording dates and locations; the editor's name; the transcriber's name; the speaker's review (if any); permissions for reprinted material. This is the interview's audit trail.

## Editorial voice

The *Literary* register from `editorial-voice.md` is the default for the editor's introduction and apparatus. The interview-artifact tradition is literary; the editor's prose is held to literary standards. *Paris Review* introductions are essays; Alexievich's framing is essayistic; Terkel's introductions argue.

The *Editorial-wonder* register fits oral histories whose subject is the underrepresented voice — Terkel's *Working*; Alexievich's *Voices from Chernobyl*. The warmth and the named consequence (*these voices have not been heard; here they are*) fit the form.

The *speakers' voice* is the speakers'. The editor does not regularize. Idiom, profanity, dialect, hesitation that survived the cut, the way a particular speaker uses a particular phrase — all of this is left intact. The editor's job is *to preserve the voice, not to translate it*. Alexievich is exemplary; her speakers sound like themselves, in their own Russian rendered through her translators with the originals' rhythms intact.

Avoid *Technical* (the interview is not a reference) and *Warm-familiar* in the editor's framing (the form's formality is part of its authority).

## Anti-patterns

1. **The unmarked smoothing.** The editor has cut redundancies and false starts without marking them. The reader cannot tell what the speaker actually said. Cure: mark cuts; in publications where heavy editing is the house style, disclose it in the introduction.
2. **The interviewer as ventriloquist.** The interviewer's questions are *leading* in ways that pre-fabricate the answers. The reader notices; the interview loses authority. Cure: edit out leading questions; replace with neutral prompts or with the longer questions that the leading version was distilling.
3. **The interviewer as character.** The interviewer interjects opinions, jokes, framings that compete with the speaker. The reader is given two performers instead of one speaker. Cure: cut the interviewer's voice to the minimum that elicits; the form is not a dialogue of equals (except in rare *Paris Review* exchanges with peers).
4. **The regularized voice.** The speaker's idiom is smoothed to the editor's house style. *"He talked good"* is corrected to *"He spoke well."* The speaker is erased. Cure: preserve idiom; gloss in a footnote if the reader will not catch it.
5. **The unmarked composite.** Multiple conversations are merged into one without disclosure. The reader believes they are reading a single session; they are reading a constructed account. Cure: disclose composites in the introduction or mark the seams.
6. **The editorial intrusion.** The editor inserts a paragraph of interpretation mid-dialogue. The form has switched from interview to essay without warning. Cure: put the interpretation in the introduction, the marginal column, or a footnote.

## What 10/10 looks like

**The *Paris Review* "Art of Fiction" / "Art of Poetry" / "Art of the Novel" interview series (1953–present), particularly the interviews with E. M. Forster (1953, the founding volume), Toni Morrison (1993), James Baldwin (1984), and Hilary Mantel (2013).** The signature move: *speaker labels typographically distinct; the editor's voice retreats to the introduction; the dialogue reads as a polished essay-in-dialogue without losing the speech's rhythms*. The form has been refined across seventy years. The introduction is a short profile; the dialogue is long (8,000–15,000 words) and patient; the speaker's voice is preserved with its specific cadences. *Paris Review* interviews are studied by writers for *how to listen*; they are studied by editors for *how to cut*. The signature move that makes them apex: an interviewer's question may take two pages and contain an embedded argument; the speaker's answer may contain a single image that reframes the question. The form earns each exchange.

**Svetlana Alexievich, *Voices from Chernobyl* (1997, English 2005) and *Secondhand Time* (2013, English 2016).** The signature move: *the interviewer's voice is erased; the speakers speak to history*. Alexievich's polyphonic documentary form gathers dozens of voices into a single volume, each speaker named with a brief epithet, the questions removed, the result reading as a chorus of monologues. The book is what it is *because* the editor is invisible at the surface — the speakers seem to speak unmediated, though the curatorial hand is everywhere in the selection and the order. The form earned Alexievich the Nobel Prize in Literature (2015); it is also the model for any apex artifact that uses many speakers as evidence for a historical claim. See `apex-exemplars.md` for additional polyphonic-documentary conventions.

Also worth studying: **Studs Terkel's *Working* (1974) and *Hard Times* (1970)** for the American oral-history form; **the *BOMB Magazine* artist interviews** for visual-arts interview conventions; **the *New York Times Magazine* "By the Book" column** for compressed-form Q&A; **the *Conversations with* series from the University Press of Mississippi** for academic-scholarly interview collections; **the *Believer* interviews, particularly the 2003–2014 issues** for the literary-magazine register; **Terry Gross's *Fresh Air* transcripts** (when print-published) for the broadcast-to-print translation problem.

**Starter pattern** — the *Paris-Review-register* opening of a single-speaker interview:

```markdown
*Hilary Mantel's house in Devon faces the sea; on the morning we spoke,
the fog had not lifted and the windows showed only the white wall of it.
Mantel was at her writing desk — a kitchen table in the front room — with
the manuscript pages of the third Cromwell book stacked in two piles. We
spoke for four hours over two days. What follows is condensed from the
recording; her permission to publish was given on 14 February 2013.*

— J.W., interviewer

INTERVIEWER

You once said the historical novelist's first job is to know what the
weather was like. Did you mean that literally?

MANTEL

Quite literally, yes. […] If I cannot tell you whether it rained on the
afternoon of 14 April 1536, I cannot write the scene. Not because the
rain is in the scene — it usually isn't — but because the rain tells me
what Cromwell smelled and what the floors of York Place would have been
like and whether the messenger arrived covered in mud or in dust. The
weather is the first lock on the door.
```

The introduction places the speaker; the dialogue's typography distinguishes the two voices; the cut at *[…]* is marked.

## Ship checklist

- [ ] Speaker labels typographically distinct; convention held across the artifact.
- [ ] Cuts marked with bracketed ellipsis or section breaks; no silent smoothing.
- [ ] Editor's commentary in introduction, marginalia, or footnotes; never interpolated into dialogue.
- [ ] Consent, recording dates, locations, and editing disclosure present in introduction or colophon.
- [ ] Interviewer is named or deliberately effaced; the decision is named.
- [ ] Speaker's idiom preserved; not regularized to editor's house style.
- [ ] Composites disclosed if any.
- [ ] Introduction is essayistic, not promotional.
- [ ] Photographs (if any) are documentary, not decorative.
- [ ] If part of a polyphonic oral history, the curatorial principle (theme, chronology, geography) is named in the introduction.
- [ ] If the interview accompanies a profile or longer feature, see `cross-medium-patterns.md` § *artifact pair*.
- [ ] Editor's register is Literary or Editorial-wonder; never Technical; rarely Warm-familiar.

<!-- END: references/medium-playbooks/cross-cluster/interview-artifact.md -->

---


<!-- BEGIN: references/medium-playbooks/cross-cluster/meta-artifact.md -->

# Cross-Cluster Playbook: Meta-Artifact (Artifact About Artifacts)

For Butterick's *Practical Typography* (online book, 2013, ongoing), Rosenfeld and Morville's *Information Architecture for the World Wide Web* (1998, multiple editions), Don Norman's *The Design of Everyday Things* (1988, revised 2013), Robin Williams's *The Non-Designer's Design Book* (1994), Tufte's *The Visual Display of Quantitative Information* (1983), Stephen Few's *Show Me the Numbers* (2004), the *Brand New Classroom* book series, and any artifact whose subject *is the making of artifacts*. The meta-artifact's central discipline: *every claim must be demonstrated in the artifact's own surface*. A book about typography whose own typography is poor has self-falsified. A book about information architecture whose own IA is confusing is a *negative* worked example. The form's reflexivity is its rigor.

(Note: this project's CLAUDE.md is itself a meta-artifact about artifact-making. The discipline this playbook names applies recursively to the document that gave rise to it.)

**Read `_spine.md` first.** Meta-artifacts are the cross-cluster form whose *editorial framing* is identical to its subject matter: the curator is teaching how to be a curator.

## What this is, when to use, what it is not

A meta-artifact is *an artifact whose subject is the making of artifacts of a particular kind*. The author teaches typography by setting their own type; teaches information architecture by structuring their own pages; teaches diagramming by drawing their own diagrams; teaches research by showing their own research. The artifact is its own worked example — every chapter teaches a principle that the chapter *itself demonstrates*.

Use when:

- The subject is *craft* — typography, IA, design, research, writing, programming, illustration.
- The reader's job is to *apply* the principles in their own work. The meta-artifact is a manual whose subject is the manual's own kind.
- The author can credibly demonstrate the principles in the artifact's surface. (An author who cannot is unqualified.)

A meta-artifact is *not*:

- **A textbook.** Textbooks may discuss principles without demonstrating them. Meta-artifacts demand the demonstration.
- **A reference.** References are queried. Meta-artifacts are read linearly; the reader follows the author's structured teaching.
- **A monograph.** Monographs survey a body of work. Meta-artifacts teach a *practice*.
- **A how-to guide.** How-to guides are procedural (`operating-manual.md`). Meta-artifacts are principled — they teach *why* and *when*, not only *what next*.

## Non-negotiables

1. **Every claim is demonstrated in the artifact's own surface.** A chapter on type-size hierarchy is set with the type-size hierarchy it advocates. A chapter on color contrast meets the contrast it specifies. A chapter on figure captions has captions that perform the chapter's lesson. *No exceptions.* A meta-artifact whose surface contradicts its claims has discredited itself, and the reader notices instantly.
2. **The "how this artifact uses itself" colophon.** Somewhere in the artifact — usually at the front, sometimes at the back — the author explicitly addresses *how* the artifact instantiates its own principles. Butterick has a chapter on his own type choices. Tufte has notes on the production of his books. The colophon is the form's hallmark.
3. **The author's authority is staked.** Meta-artifacts demand expertise. The author's credentials, body of work, or evidence of expertise must be visible. *Anonymous teaching of craft is unconvincing*; the reader is being asked to adopt the author's taste.
4. **Counter-examples are honored.** A meta-artifact that shows only positive examples is incomplete. The reader needs to see *what bad looks like*, ideally rendered with the same care as the good examples (rather than a strawman). Norman's *Design of Everyday Things* is the apex: every chapter contains real bad doors, real bad teakettles, real bad telephone systems, *photographed and analyzed seriously*.
5. **The principles are *named and indexable*.** "Norman doors", "data-ink ratio", "AIDA pyramid", "small multiples", "the law of proximity". Apex meta-artifacts produce *vocabulary the field then uses*. The reader leaves with terms they can deploy in their own practice. Vague claims ("good design is consistent") do not propagate; named claims ("the data-ink ratio should approach 1") do.

## Composition pattern

Meta-artifacts have seven standard positions:

1. **Front matter / dedication.** Often a manifesto. Butterick's *Practical Typography* opens with an emphatic statement that typography is *important*; Norman's *DoET* opens with the famous Norman door. The front matter sets the artifact's *register* and its *stakes*.
2. **The colophon.** *"How this book uses itself."* Tufte's books include detailed colophons (paper stock, typography, binding). Butterick's website has a chapter named *"How this book looks."* The colophon is the artifact's transparency.
3. **The principles, named.** Chapters are organized around named principles. Each principle is *stated* (one or two sentences), *demonstrated* (in the chapter's own surface and in external examples), and *applied* (to a scenario the reader will recognize). The structure is recursive: the chapter on naming is named.
4. **Worked examples.** Real artifacts analyzed in detail. Apex meta-artifacts include both positive and negative examples; the negative examples are real and serious, not strawmen. The analysis names *what the artifact does well or poorly* against the principles the chapter has named.
5. **Exercises (optional but apex).** Tasks the reader can do that apply the chapter's principle. Williams's *Non-Designer's Design Book* has exercises at the end of each chapter. The exercise is the principle made *physical* for the reader.
6. **A glossary of named terms.** The vocabulary the artifact produces, indexable. This is the artifact's gift to the field.
7. **References / further reading.** Other meta-artifacts in the same field. The lineage is acknowledged; the author names their teachers and their peers.

## Editorial voice

The *Editorial* register from `editorial-voice.md` fits most meta-artifacts — short sentences, claim-bearing prose, the *artifact's surface* carries the argument the prose names. Butterick's voice is Editorial; Norman's voice is Editorial; Tufte's voice is Editorial (with occasional Editorial-wonder when the subject warrants).

The *Literary* register fits meta-artifacts whose subject is *writing* or *art* (Robert Bringhurst's *The Elements of Typographic Style* is in this register; James Wood's *How Fiction Works* is in this register). The craft of the prose is itself an argument for the prose's principles.

The *Editorial-wonder* register can work for meta-artifacts in fields where the wonder of the made object is part of the claim (Christopher Alexander's *A Pattern Language* drifts here; Tufte's chapter on Minard's map is in this register).

Avoid *Technical* (the meta-artifact is not a reference) and *Warm-familiar* in the artifact's surface (though authorial asides may dip into Warm-familiar; see Butterick's footnotes).

## Anti-patterns

1. **The unobservant surface.** The author writes about typography but sets the book in 11pt Times New Roman with default leading. The book's prose contradicts its surface; the reader cannot trust the author. Cure: invest in the surface; if the surface cannot be made to honor the principles, the artifact is unshippable.
2. **The strawman counter-example.** Bad examples are obviously bad — comic-sans-on-rainbow-backgrounds; cartoon-villain design. The reader is not taught to recognize *realistic* bad design. Cure: use real, serious bad examples, analyzed with the same care as good ones.
3. **The vague principle.** *"Good design is consistent."* What does the reader do with that? The principle is unnamed and unappliable. Cure: name the principle ("the law of proximity"), state it specifically, demonstrate it twice, give the reader a test.
4. **The author-as-genius.** The author's taste is invoked as authority; the reasoning is hidden behind *"in my experience"*. The reader is asked to defer rather than to learn. Cure: show the reasoning; deference is not pedagogy.
5. **The unsignaled scope.** The meta-artifact claims to teach *design* but actually teaches *web design* or *editorial design* or *system design*. The reader applies the principles to the wrong domain. Cure: name the scope precisely in the front matter.
6. **The missing exercise.** The reader leaves with vocabulary but no practice. The principles do not migrate into their work. Cure: include exercises, even short ones.
7. **The self-flattering colophon.** The "how this book uses itself" section is a brag rather than an analysis. The reader cannot tell what the author would have done differently. Cure: include the production constraints, the compromises, the things the author would change in a future edition.

## What 10/10 looks like

**Butterick, *Practical Typography* (online book, 2013, ongoing; practicaltypography.com).** The signature move: *every claim demonstrated in the artifact's own surface*. Butterick's book is set in his own Equity typeface; every typographic recommendation in the prose is visible in the prose's setting. The chapter on font choice presents fonts; the chapter on line length is set at the line length Butterick recommends; the chapter on small caps uses small caps; the *footnotes* obey the footnote conventions the book teaches. The colophon ("How this book looks") names every typographic decision. The book is the apex of the form: a meta-artifact whose surface is its own argument. See `apex-exemplars.md` for related typography references.

**Don Norman, *The Design of Everyday Things* (1988, revised 2013).** The signature move: *the vocabulary the artifact produces*. Norman's book introduced "Norman doors", "affordances", "mappings", "signifiers", "feedback loops" into the vocabulary of design. Every term is named, demonstrated against real artifacts (photographs of real bad teakettles, real bad telephones, real bad thermostats), and given a test the reader can apply. The book's revisions (1988 → 2002 paperback → 2013 revised edition) demonstrate the form's longevity: principles named correctly survive across decades. Norman's photographs of bad design are the apex of *honoring the counter-example* — each bad door is photographed seriously, analyzed under the same vocabulary as the good design.

Also worth studying: **Tufte, *The Visual Display of Quantitative Information* (1983) and *Envisioning Information* (1990)** for the meta-artifact about data graphics whose own graphics are the form's apex; **Robert Bringhurst, *The Elements of Typographic Style* (1992)** for the typographer's literary register; **Rosenfeld and Morville, *Information Architecture for the World Wide Web* (1998)** for the IA meta-artifact, whose own structure is its argument; **Christopher Alexander, *A Pattern Language* (1977)** for the pattern-as-pedagogy form, applied to architecture; **Andy Hunt and Dave Thomas, *The Pragmatic Programmer* (1999, revised 2019)** for programming meta-artifacts; **this project's CLAUDE.md** is itself a meta-artifact about artifact-making; the principles it names are, recursively, the principles of its own composition.

**Starter pattern** — a single-principle chapter in Butterick register:

```markdown
## Point size

The right point size for body text is between 10 and 12 points. Below 10,
readers slow down. Above 12, the line takes up too few words and the
reader's eye loses pace. This paragraph is set in 11pt Equity Text.

A bad point size — too small — looks like this. <span class="bad">This
paragraph is set in 7.5pt Equity Text, the kind of size you see in
contracts you did not write and are not supposed to read carefully. The
size is signaling something about how this passage expects to be treated.</span>

A bad point size — too large — looks like this. <span class="bad-large">
This paragraph is set in 18pt, larger than most book bodies and most
sentences benefit from. The line carries seven or eight words; the eye
must return to the left margin too often; the rhythm of reading is
broken.</span>

If your software's default is 12pt, try 11pt and notice. If it is 11pt,
try 10pt. Test the result against a page of body prose; the right size
is the size where you stop noticing the type.
```

The principle is named ("between 10 and 12 points"), demonstrated three times (the body text demonstrates the recommended size; the two bad examples demonstrate the failures), and given an actionable test ("try 11pt and notice").

## Ship checklist

- [ ] Every principle named in the prose is demonstrated in the artifact's own surface.
- [ ] *How this artifact uses itself* colophon present.
- [ ] Author's authority staked (credentials, body of work, evidence of expertise).
- [ ] Counter-examples are real and serious, not strawmen.
- [ ] Principles are named with terms the reader can use ("Norman doors", "data-ink ratio").
- [ ] Each chapter states the principle, demonstrates it, applies it.
- [ ] Glossary of named terms present.
- [ ] References / further reading section names the lineage and the peers.
- [ ] Scope named precisely in the front matter.
- [ ] Exercises (if present) ask the reader to *apply*, not just to recognize.
- [ ] If the meta-artifact is itself a teaching artifact for an apex-quality system (like this project's CLAUDE.md), cross-reference the *manifesto.md* and the relevant single-medium playbooks the meta-artifact draws from.
- [ ] If the meta-artifact has a sibling artifact (e.g., a website + a printed book), see `cross-medium-patterns.md` § *artifact pair* or § *translation*.

<!-- END: references/medium-playbooks/cross-cluster/meta-artifact.md -->

---


<!-- BEGIN: references/medium-playbooks/cross-cluster/epistolary.md -->

# Cross-Cluster Playbook: Epistolary / Correspondence

For *Letters of Note* (Shaun Usher, 2013, with a website preceding the book), *The Selected Letters of Vincent van Gogh* (multiple editions; the Penguin 1996 selection edited by Mark Roskill is canonical), *84, Charing Cross Road* (Helene Hanff, 1970), the published correspondence of Joan Didion, Sylvia Plath, James Baldwin, Hannah Arendt, the *Letters from Iwo Jima* historical compilations that inspired the 2006 film, the *Lyndon B. Johnson* presidential telephone recordings rendered as transcripts, the *Diary of Anne Frank* in its scholarly critical edition, and any artifact whose primary content is *the recovered written correspondence of a person or set of persons*. The form is interview's quiet sibling: the writer often dead, the addressee private, the document a window into both writer and time.

**Read `_spine.md` first.** Epistolary artifacts are the cross-cluster form whose *primary speakers cannot be re-interviewed*; the editor's job is to honor what was preserved while making it legible.

## What this is, when to use, what it is not

An epistolary artifact is *a curated collection of correspondence framed by editorial apparatus*. The letters may be a single writer's outgoing correspondence (van Gogh to Theo); a single writer's correspondence with one addressee (Helene Hanff and Frank Doel); a recovered set of letters around an event (the Iwo Jima compilations); a thematic gathering (*Letters of Note* groups letters by occasion — *"letters of complaint"*, *"letters from war"*). The editor's hand is everywhere — selection, dating, footnoting, contextualizing — but the editor's voice is *in the apparatus*, not in the letters.

Use when:

- Written correspondence exists in volume sufficient to support an editorial selection.
- The correspondents' situation, history, or context warrants the publication. (Privacy concerns are first-order; see non-negotiable 4.)
- The reader will be served by seeing the correspondence *as correspondence* — dated, addressed, signed — rather than recast as prose.

An epistolary artifact is *not*:

- **An interview** (`interview-artifact.md`). Interviews involve a present interviewer. Epistolary artifacts are recovered; the writer often did not anticipate publication.
- **A diary** in the modern published sense. Diaries are addressed to self; the published *Anne Frank* edition is on the boundary and is treated as an epistolary-adjacent form because the diary's "Dear Kitty" framing creates an addressee.
- **A novel in letters.** Fictional epistolary (Richardson's *Pamela*; *The Color Purple*; *Where'd You Go, Bernadette*) is a separate literary form; this playbook is for *non-fiction* recovered correspondence.
- **An archive.** Archives are exhaustive; epistolary artifacts are *selected*. A complete edition of Mozart's letters is an archive; a Penguin selected-letters volume is an epistolary artifact.

## Non-negotiables

1. **Dated letters; redactions visible.** Every letter carries its date (or *"undated, c. 1882"* when the date is inferred). Every redaction — for privacy, for legibility, for relevance — is *visible*, typically as bracketed ellipsis with the editor's reason where appropriate. *"[passage on family finances omitted at request of the estate]"* is honest; a silent cut is not.
2. **The letter's apparatus is preserved.** Salutation, body, closing, signature, postscript — all kept. *"Dearest Theo, … Vincent"* survives the edit; without these markers, the letter has become an essay. Address blocks may be preserved or summarized in the apparatus; the editor names the choice in the introduction.
3. **Editorial footnotes are dense and necessary.** Letters reference *named persons*, *dated events*, *contemporary works*, *prior letters*. The reader cannot follow without footnotes. The footnote convention must be clear (numbered footnotes; endnotes by letter-number; bracketed editor's notes inline — pick one and hold it). Apex editions footnote *every* named person on first appearance and re-flag where decades have passed since the last reference.
4. **Permissions and ethics are documented.** Letters are private documents. Their publication requires consent — from the writer (in life), from the estate (after death), from the addressee or their estate. Major edition introductions document the permissions explicitly. Living addressees may request redactions; the redactions are marked. An epistolary artifact that has not done this work is unshippable; the form's reader-ethics are part of its rigor.
5. **The per-correspondent index is non-negotiable for multi-correspondent volumes.** A reader who wants every letter to or from a specific person must find them via the index. *Letters of Note* has indices by sender, by addressee, by occasion. Major scholarly editions have indices that run to 20–80 pages.

## Composition pattern

An epistolary artifact has seven standard positions:

1. **Editor's introduction.** 2,000–8,000 words. Names the correspondent(s); sketches the biography; situates the correspondence in the writer's life and historical moment; names the principle of selection; discloses the editing conventions (what is preserved, what is redacted, what is silently corrected); credits the prior editions on which the present one builds.
2. **A chronology / timeline.** A separate front-matter section: dates and events relevant to the correspondence. The reader uses the chronology to place each letter in its life-context. Van Gogh's letters are unintelligible without knowing where he was living when each was written; the chronology supplies this.
3. **The letters themselves.** Usually in chronological order; some thematic volumes (*Letters of Note*) cluster by occasion. Each letter has a *header* with date, place written, addressee, and (for major editions) a unique letter-number that becomes the citation form.
4. **Editorial footnotes.** Inline (bracketed) for the briefest interjections; numbered footnotes at the page bottom or at the chapter end for substantial annotations. The footnote density is the apparatus's intensity; a major scholarly edition has more footnote-words than letter-words.
5. **Per-correspondent index.** For volumes with multiple addressees, an index by sender and by addressee, with letter-numbers. For volumes by a single writer, the index is by *person mentioned*.
6. **Subject and place indices.** For substantial volumes, indices to topics (works the writer was working on; places visited; events referenced).
7. **Bibliography and previous editions.** What earlier editors did with this material; what the present edition adds or corrects; what archives the letters live in (Van Gogh Museum, Beinecke, Bodleian).

## Editorial voice

The *Literary* register from `editorial-voice.md` is the default for the editor's introduction and footnotes. The epistolary-edition tradition is scholarly-literary; the editor's prose is held to scholarly standards while reaching for the register of essayistic criticism. The Roskill van Gogh edition's introduction is essayistic; the various Joan Didion correspondences' introductions are essayistic; *Letters of Note*'s short framing notes are aphoristic-literary.

The *Editorial-wonder* register fits introductions to correspondences whose subject is the made-thing or the historical moment — Carl Sagan's letters; Marie Curie's; the *Letters from Iwo Jima* compilations. The wonder is *located in the historical pressure on the writer*, not in the editor's prose.

The *writers' voices* are the writers'. The editor does not modernize spelling, normalize punctuation, or smooth grammar without disclosing the convention. Some editions modernize ("the present edition has silently corrected spelling and punctuation following the conventions of [X]"); the disclosure is itself the apparatus.

Avoid *Technical* (the edition is not a reference work in the database sense) and *Warm-familiar* in the editor's framing (the formality of the form is part of its authority — though Usher's *Letters of Note* sits on the boundary, with a populist register that some apex editions would reject).

## Anti-patterns

1. **The silent redaction.** Material is cut without marking. The reader cannot tell where the writer's letter ends and the editor's selection begins. Cure: mark every cut; disclose the convention in the introduction.
2. **The unfootnoted reference.** *"As you know, the matter we discussed at Worthing"* — the reader does not know what was discussed at Worthing. Cure: footnote every named person, event, prior letter, and contemporary work on first reference.
3. **The orphaned letter.** A letter is included with no chronological context; the reader cannot tell what was happening in the writer's life when it was written. Cure: the front-matter chronology must place every letter; cross-reference where helpful.
4. **The voyeuristic selection.** The selection privileges scandal, illness, or private suffering without editorial justification. The reader feels the writer has been exposed. Cure: the editor's introduction must defend the selection's principle; private suffering is included only when its inclusion serves a named claim about the writer's life or work.
5. **The hagiographic frame.** The introduction presents the writer as a flawless figure; the difficult letters are omitted; the writer's prejudices are smoothed. The edition has betrayed its subject by protecting them. Cure: include the difficult letters and name them as such in the introduction.
6. **The unsourced primary text.** The letter's source archive is not named; the reader cannot verify or extend the editor's selection. Cure: every letter cites its archival location (collection, box, folder, page).
7. **The modernized voice without disclosure.** Spelling and grammar have been silently corrected. The reader believes they are reading the writer's prose; they are reading the editor's. Cure: disclose modernization in the introduction; an apex edition often presents original spellings and footnotes the modernizations.

## What 10/10 looks like

**The Van Gogh Museum's *Vincent van Gogh: The Letters* (online and 6-volume print, 2009, edited by Leo Jansen, Hans Luijten, and Nienke Bakker).** The signature move: *the document is a window into both writer and time, supported by apparatus equal to the letters in weight*. The 2009 edition includes 902 letters across six volumes (and a comprehensive online version at vangoghletters.org), each letter dated, transcribed in the original Dutch or French with English translation alongside, every named person footnoted, every work referenced cross-linked to its catalogue raisonné entry, every prior edition's variants noted. The introduction is a 100-page essay; the chronology is 80 pages; the indices run to 200. The reader of this edition is given the *entire archive* with the curatorial argument visible at every level. Van Gogh's voice survives intact; the apparatus makes it legible. This is the apex of the scholarly-edition form.

**Shaun Usher, *Letters of Note* (book 2013, originally a website lettersofnote.com from 2009).** The signature move: *thematic selection of single letters with terse editorial framing*. Usher gathers letters across centuries and contexts — Queen Elizabeth's recipe for drop scones; a 9-year-old's letter to Roald Dahl; Hunter S. Thompson on hiring; the last letter of a Confederate soldier — and pairs each with a 100–200-word editor's note placing the letter. The form is the *opposite scale* of the Van Gogh scholarly edition: where Van Gogh aims for completeness within a single writer, *Letters of Note* aims for breadth across writers, framed by a curatorial argument about *what letter-writing has been able to do*. Both apex; the form admits both. See `apex-exemplars.md` for related curatorial collections.

Also worth studying: **Helene Hanff, *84, Charing Cross Road* (1970)** for the two-correspondent form, edited and published by one of the correspondents themselves; **the *Selected Letters of Sylvia Plath* (Vol. I 2017, Vol. II 2018, ed. Steinberg & Kukil)** for major scholarly correspondence editions of the modern era; **the published correspondence of James Baldwin and Sol Stein, *Native Sons* (2004)** for a single-relationship volume; **Hannah Arendt's correspondences (with Mary McCarthy, with Karl Jaspers, with Heinrich Blücher)** for philosophical correspondence; **the *Anne Frank: The Diary of a Young Girl* critical edition (1989, ed. Barnouw and van der Stroom)** for the diary-as-epistolary boundary case; **the *Letters from Iwo Jima* compilations** for war correspondence; **the *Library of America* presidential papers** for political-historical correspondence.

**Starter pattern** — a single letter with editorial apparatus:

```markdown
### Letter 539 — to Theo van Gogh

**Saint-Rémy-de-Provence, on or about 22 May 1889**[¹]

My dear Theo,

Many thanks for your letter from the 21st, which reached me here on the
morning of the 22nd.[²] I have, I think, settled in well at the asylum;
the room is small but sufficient and I have permission to paint in the
gardens during the day.[³] […]

Send my regards to Jo[⁴] and tell her that the small canvas of the irises
will be finished by the end of the week.

I shake your hand cordially,
Vincent.

---
¹ Date inferred from postmark on Theo's reply (letter 540, 24 May).
² Theo's letter not extant; reconstructed from internal references.
³ Saint-Paul-de-Mausole asylum; Vincent had been admitted 8 May 1889.
⁴ Johanna ("Jo") Bonger, Theo's wife (married 18 April 1889).
```

The letter's apparatus is preserved; the date is dated; the footnotes carry the apparatus; the cut at *[…]* is marked.

## Ship checklist

- [ ] Every letter dated (or with date-inference disclosed) and addressed.
- [ ] Redactions and cuts visible; convention named in the introduction.
- [ ] Letter apparatus (salutation, body, signature, postscript) preserved.
- [ ] Footnotes annotate named persons, dated events, prior letters, and contemporary works on first reference.
- [ ] Front-matter chronology places the correspondence in the writer's life.
- [ ] Per-correspondent index present for multi-correspondent volumes.
- [ ] Permissions documented in the introduction (writer's estate, addressee, archive).
- [ ] Source archive cited for every letter (collection, box, folder).
- [ ] Modernization conventions disclosed; original spellings preserved or transparently corrected.
- [ ] Editor's introduction defends the selection's principle and acknowledges what is excluded.
- [ ] If the correspondence accompanies a biography, exhibit, or film adaptation, see `cross-medium-patterns.md` § *artifact pair* or § *sequel*.
- [ ] If the form is single-correspondent and intimate (Hanff and Doel), check that the addressee's voice is preserved at equal weight, not subordinated.

<!-- END: references/medium-playbooks/cross-cluster/epistolary.md -->

---

