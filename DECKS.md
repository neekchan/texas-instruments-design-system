# Decks and presentations

The slide authority for TI work. Ported from the Hoffman Agency design system's slide SOPs and layout library (v2.21.0), with TI's values substituted. Where this section and the README disagree about a slide, this section wins; where a value must be exact, `tokens.json` wins.

## 0 · Two media with different physics

Web, social and print are governed by the README and the web type group. Slides are governed by this section and the deck type group. On slides, ignore the web scale, "generous negative space", sparse imagery and max-width caps. Shared by both: colour, Arial, the signature, voice, trademarks.

Delivery format is not a medium. A deck delivered as HTML and a deck delivered as `.pptx` are both slides. An HTML deck is not a web page.

## 1 · The TI slide anatomy

Every content slide in the 2026 template has the same skeleton; keep it.

- Canvas 1920 × 1080 (the template is 10 × 5.625 in; 1pt = 2.67px).
- Title block top-left inside `deck-margin`: `deck-title` 64px Arial Bold in `title` red, one or two authored lines, line-height 85%.
- Optional lead sentence under the title in `deck-subtitle`, `ink-strong`, ≤ 30 words.
- Content area below, filling to the footer band.
- Footer band `deck-footer` 102px: the `accent` rule along its top, `deck-rule-weight` 6px (2.25pt), from the LEFT EDGE of the slide to `deck-rule-inset` 45px short of the right edge, so it ends flush with the right end of the signature beneath it; never edge to edge. The horizontal signature right-aligned at `logo-deck` 280px; page number `deck-caption-sm` bottom-right above the rule. White ground.
- Cover: one of the three `assets/Backgrounds/` files full-bleed, title in `deck-cover` red bottom-left or top-left, signature in the footer.

## 2 · Slide type scale — floors, not caps

Sizes are px on 1920 × 1080 with the template's pt in parentheses. Bias to the top of every range; the display tiers are size-to-fit.

| Tier | Token | Size |
| --- | --- | --- |
| Caption / source | `deck-caption-sm` | 24px (9pt) — the floor, never smaller |
| Icon label | `deck-caption` | 27px (10pt) |
| Body | `deck-body` | 32px (12pt) default; `deck-body-lg` 37px (14pt) on airy slides |
| Lead sentence / section strip | `deck-subtitle` 43px (16pt) / `deck-section-label` 37px |
| Slide title | `deck-title` | 64px (24pt) |
| Hero stat | `deck-stat` 75px (28pt) / `deck-stat-xl` 88px (33pt) |
| Cover title | `deck-cover` | 80px (30pt), as large as fits on two lines |

≤ 3 distinct sizes per slide (a stat's giant number can be a deliberate fourth). Pick three tiers (caption 27 + body 32 + title 64) and stay there; don't ladder through five. Never a 14–18px web size on a slide.

## 3 · Fill the frame

- Default safe margin is `deck-margin` 48px, not a fat uniform border. A uniform fat margin with small centred content is the first tell of an AI deck.
- Full-bleed is the default for image-led layouts; the type half keeps the margin, only the imagery bleeds.
- Fill the lower third. Dead space is a bug, not breathing room; never leave a blank half-slide.
- If a slide feels empty, the type is too small or it is missing its image.

## 4 · Titles: authored breaks

- Never truncate or clip a title. No ellipsis, no cut-off word, no `overflow:hidden`.
- Every display heading that needs more than one line carries its own `<br>` at a sense boundary. A heading whose rendered line count exceeds its `<br>` count + 1 has wrapped on its own: a build failure.
- Measure caps are px matching the slot (1776px full width, the column width in a split), never `ch`. No `text-wrap: balance` on slides.
- Size the line to the measure before writing the break. Arial Bold runs about 0.56em per character: at 64px roughly 49 characters fit the full width, about 27 on a 1000px column.
- A title that fills only the left half and leaves the right empty reads as unfinished: fill the width, size up, or treat the empty side as a slot.
- One title measure per deck. A render without Arial installed is not a check.

## 5 · One point per slide

A deck is a teleprompter for the eyes in the room, not the script in the speaker's hand.

1. One point per slide. If the single takeaway can't be said in one sentence, split it.
2. Minimum on the page; the rest is narrated. A sentence that exists only to be read aloud is cut from the slide.
3. Hierarchy is visible, not implied. A viewer knows in under two seconds what to read first; never two heroes.
4. Earn emotion with one graphic: one photograph, one chart, one icon row. Not a grid of stock icons.
5. Cut before you add, then scale up to fill the frame. Restraint means few elements, not small floating ones.

Word budgets (hard caps; the headline is a layout budget that Soundcheck may override with a flag): headline ≤ 8 words on one line where possible · eyebrow 2–4 words · supporting body ≤ 30 words per slide · bullet ≤ 6 words, max 3 per group · stat = number + ≤ 4-word label, max 3 per slide, one hero · 3–5 large elements per slide · nothing under 24px except a functional caption.

Density tiers: Airy (cover, section, statement, quote, big idea — most slides) · Standard (2–3 columns, persona, detail) · Dense (matrix, scope table, roster — only when the artefact is the point, one or two per deck). The 2026 corporate template is a Document-mode deck and sits mostly in Standard and Dense; Hoffman pitch material for TI should sit mostly in Airy.

## 6 · Presenter XOR Document

Declare one mode per deck; never mix.

- Presenter: ≤ 1 idea and ≤ 15 words per slide, image-led, the headline carries the point, the detail lives in speaker notes (one note per slide, in order). Sources, citations, methodology and legal lines go to notes.
- Document: denser and hierarchical, stands alone when read, short bullets and phrases, never paragraphs. Still capped by the budgets above.
- What does not change between modes: the visual system. Document mode is denser content, never smaller type or an airier page.
- Infer the mode from context and state the assumption: present / stage / town hall / live pitch → Presenter; leave-behind / read-ahead / board pre-read / "send it over" → Document. Ask only if ambiguous.

## 7 · Colour on slides

- The page is white. One dominant colour per slide; variety lives across slides, not within one.
- Chrome is red (title, the open-ended footer rule); content may carry one more red element at most: a hero stat, a highlighted cell, the key chart series.
- Teal is the working accent: `teal-deck` Fluent icons and bold lead-ins, `teal-deck-300` callout fills with `ink-strong` text, `teal-deck-500`/`-400` as further chart series.
- Section dividers may take a full `red` or `teal-deck` surface with white type (both ≥ 4.5:1) or one of the three title backgrounds. Content slides stay white. No dark slides in v1: there is no reversed signature. A red or teal divider carries no signature; it returns on the next white slide.
- WCAG per pair: ≥ 4.5:1 body, ≥ 3:1 large; display pairs that are the point held to 7:1. White on `red` is 5.9:1; white on `teal-deck` 5.2:1; `teal-deck` on white 5.2:1; `red` on white 5.9:1 (AA, so a red statement word should be set 64px+).

## 8 · Charts and numbers

- Data ink ≥ 80%: no 3D, gradients, shadows on bars, decorative gridlines, legend essays. Label the series directly.
- `red` for the series that matters, `teal-deck`, `teal-deck-300`, `grey-deck-light` for the rest; labels `deck-caption` in `ink`.
- Max three stats per slide; prefer one hero in `deck-stat` plus two context figures. Equal-weight stat grids only when no figure is the hero.
- A count-up animation ends on the true value; reduced-motion shows it immediately.
- Every number is sourced (speaker notes or a `deck-caption-sm` source line) or replaced with a visible `[REAL DATA · what · who supplies it]` placeholder.

## 9 · Structure and closing

- "Lean / one point" governs the content section; it does not mean a one-slide deck. A credentials run can be several slides when breadth is the argument.
- Every deck ends on a dedicated closing: a short imperative headline (≤ 6 words), a contact line, the signature. No recap, no bullets.
- Every slide carries `data-screen-label="NN Label"` in HTML builds ("01 Cover", "07 Key markets").
- Keep the layout library varied: these rules tune size, density and voice; they must never homogenise a deck into one big-type template.

## 10 · Layout library (48 layouts)

Codes are kept from the Hoffman library so briefs and manifests stay portable; the surfaces named there are re-mapped to TI (white page, red or teal dividers, the three title backgrounds). Choose from this list; build from the deck template once one exists in this system.

**Covers and dividers** — L01 Cover (eyebrow → giant headline ≤ 8 words → one-line subtitle → signature; no agenda) · L31 Cover with full-height edge bar (red) · L02 Section divider (part number + 1–2-word title on a red, teal or background surface; never a sentence) · L32 Divider with edge bar · L03 Agenda (3–5 numbered items, titles only).

**Statements** — L08 Statement + support (claim 72–96px, ≤ 30-word support) · L09 Big-idea split (text left, full-height image right, idea-name strip) · L45 Punchline giant word · L46 Two-beat statement (setup top-left, turn lower-right) · L47 Centred motif opener (one icon 120–200px + ≤ 4-word headline) · L50 Script + acronym opener.

**Diagrams** — L10 Plan-on-a-page matrix (one per deck) · L34 Orbit / ring (core + 6 parts) · L35 Highlight box + arrows (before → after; the layout for any source → tool → output flow).

**Columns** — L11 Three image cards · L12 Three icon cards (icon → heading ≤ 7 words → 2 bullets) · L13 Three audiences · L37 Numbered points with vertical rules.

**People** — L14 Persona profile · L15 Team roster · L16 Single bio (lead with the most credible fact).

**Ideas and stories** — L17 Idea detail · L18 Two stories side by side · L39 Ongoing story engagement · L40 Story + role + image.

**Data and process** — L19 Stat strip (one hero + two context) · L33 Cascade stat boxes · L38 Stat grid (6–8 equal cards) · L41 Data dashboard (donut + 3–5 bars + 3 callouts) · L20 Timeline / measurement arc (4–6 nodes) · L21 Process / journey ring · L24 Scope / deliverables table (the one place dense text is correct).

**Capability and about** — L22 Icon benefit grid (6–8 cards; TI's portfolio slide is this) · L23 Capability grid · L36 Pill rows + icon circles (highlight exactly one) · L48 Photo + numbered lists · L49 Three photos + bullets · L24b Pain ↔ solutions · L25 Map + narrative (TI's footprint slide) · L26 Values statement.

**Image and quote** — L27 Full-bleed image + 60–75% dark overlay + one line · L28 Split 50/50 · L29 Pull quote (≤ 20 words, attribution) · L42 / L43 / L44 Bento collage of 4 / 5 / 7 photos (one cell leads).

**Closing** — L30 Closing (verb + a way to reach you + signature) · L51 Q&A closer.

Full-bleed set: L01, L31, L32, L08, L09, L14, L27, L28, L40, L48 bleed imagery to at least one edge; bentos bleed inside their cells. Everything else frames its imagery inside the margin.

Quick router: open → L01/L31 · break into parts → L02/L32 · warm opener → L47/L50 · agenda → L03 · one claim → L08/L09 · hinge word → L45/L46 · strategy on a page → L10 · core + parts → L34 · before/after → L35 · compare 2–3 → L11/L12/L13/L37 · audience → L14/L13 · team → L15/L16 · one idea → L17/L40 · two stories → L18/L39 · numbers → L19/L33/L38 · data viz → L41 · process → L20/L21 · capabilities → L22/L23 · 3–5 supported points → L36 · content-rich update → L48/L49 · pain → solution → L24b · SOW → L24 · footprint → L25 · values → L26 · image-led → L27/L28 · 4–7 photos → L42–44 · quote → L29 · close → L30/L51.

## 11 · Motion (HTML decks)

Staggered entrances 12–26px rise + fade, 420–600ms, `cubic-bezier(.2,.8,.2,1)`, stagger 60–140ms, at most ~8 staged elements. Hover 140ms, state changes 300–450ms. Overshoot only on small marks, never on panels, headlines or images. Base markup is always the final visible state; honour `prefers-reduced-motion` with a global `animation:none; transition:none`. No animated emoji, no animated logo: TI's signature is static.


---

<sub>Texas Instruments design system — built by **Nicolas Chan**, Head of Digital & Chief Strategist, AMEA, The Hoffman Agency. Texas Instruments, the TI signature and TI DLP® are trademarks of Texas Instruments Incorporated; see `LICENSE.md`.</sub>
