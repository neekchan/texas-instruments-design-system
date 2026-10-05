# Texas Instruments design system

**Version 1.1.1** · the TI brand layer for The Hoffman Agency's work on Texas Instruments: tokens, brand book, slide craft, delivery gate and a PowerPoint template, built from TI's public sources (ti.com's Polaris CSS tokens, the published signature files, TI's trademark pages) and from the brand-agnostic craft layer of the [Hoffman Agency design system](https://github.com/neekchan/hoffman-agency-design-system).

Private repository for The Hoffman Agency's TI team. It carries TI's brand assets for TI's own work; do not fork, mirror or make public.

## Making a TI deck (the team path)

1. **Download the template:** [`templates/powerpoint/TI_Deck_Template_v1.pptx`](templates/powerpoint/TI_Deck_Template_v1.pptx) (click, then "Download raw file"). It opens in PowerPoint or Keynote; for Google Slides, upload it to Drive and open with Slides. Signature, footer rule, backgrounds and icons are already in place.
2. **Write the titles first.** Read only sections 1 and 5 of `DECKS.md` and the one rule in `SOUNDCHECK.md`: every title states the slide's point, and the titles read in order should make one argument.
3. **Build from the layouts.** Home → New Slide offers 34 layouts: cover, red section dividers, a teal appendix divider, agenda, statements, columns, photo splits, stats, chart, table, programme at a glance, timeline, team, quote and closing. Type into the boxes; the grey prompt text gives each box its word budget and never prints. Need another arrangement? Home → Layout. Don't draw loose text boxes. Slide 1 explains the five rules; the example slides after it show finished versions. Delete what you don't use.
4. **Icons** come from `assets/Icons/` (teal, ready to drop in; PNGs under `assets/Icons/png/` for PowerPoint). Need one that isn't there? Search the name in `assets/Icons/catalog.json` or ask Claude.
5. **Working with Claude or another agent:** give it this repo (or paste `AGENTS.md` + `README.md` + `DECKS.md`); it routes itself. Before anything ships, run `CHECKLIST.md` and ask for the delivery report.

**Start here (agents and builders)**

1. Read this README, then `tokens.json` (values; its usage notes are binding) and `tokens.css` (the same, compiled for web).
2. `AGENTS.md` (canonical; `CLAUDE.md` points to it) → `LLM_ENTRYPOINT.md` routes every task. Slides: `DECKS.md` (+ `SOUNDCHECK.md`, `DECK-TEMPLATE.md`, `POWERPOINT.md`). Shipping: `CHECKLIST.md`.
3. Assets are in the repo: signature files under `assets/Logos/`, title backgrounds under `assets/Backgrounds/`, TI's original deck icons and the DLP guidelines under `assets/Reference/`, Fluent icons under `assets/Icons/`. `tools/fetch-assets.sh` only re-downloads the signature files from ti.com if TI republishes them.

Two media, two rule sets. Web, social and print follow the web type group and ti.com's spacing. Slides, whether delivered as HTML or `.pptx`, follow the deck type group and `DECKS.md`. Colour, Arial, the signature, voice and the trademark rules are shared.

---

## Content fundamentals

TI writes like an engineer briefing a customer: plain declarative sentences, specific numbers, no adjectives doing the work a figure should do. Real lines from the corporate deck set the register: "We design and manufacture analog and embedded semiconductors." "Our 80,000 products are the essential building blocks of all types of electronics systems." "15 manufacturing sites worldwide, including wafer fabs, assembly and test factories, and bump and probe facilities." "We bring together the world's smartest people – problem-solvers known simply as TIers."

- Voice is first-person plural ("we", "our") when TI speaks; second person ("you", "your system") when addressing a customer or candidate. Hoffman material about TI uses "TI" in the third person.
- American English. Sentence case everywhere: titles, headings, buttons, labels. UPPERCASE only on a `deck-section-label` strip ("PORTFOLIO", "AGENDA").
- Numbers carry their unit and their date: "$17.68 billion in 2025", "~33K employees", "25% reduction by year-end 2025 (vs 2015)". A figure without a source goes to speaker notes with its source or is cut; see the Delivery gate.
- Qualifiers survive editing: "approximately", "nearly", "up to", "in pilot".
- No exclamation marks, no emoji, no agency jargon ("leverage", "synergy", "best-in-class", "game-changing"). TI's own promotional words are "affordable", "reliable", "robust", "quality", "innovation", "engineering progress" — use them, don't invent new ones.
- The company is "Texas Instruments" on first mention in any document, then "TI". The website is "TI.com" in TI's own copy. People are "TIers". Product families take TI's casing: "DLP® products", "analog and embedded processing", "200-mm and 300-mm wafer fabs".
- Positioning language from the deck, usable verbatim in Hoffman material: technology leader · trusted supplier · great employer · great long-term investment. Values, in TI's order: trustworthy, inclusive, innovative, competitive, results-oriented. Ambition: "Create a better world by making electronics more affordable through semiconductors."

### Trademarks

- The signature (mark + wordmark) is used whole. TI's trademark page: "Please use the preferred or alternate signature, not TI's logo alone." Never the Texas-shaped mark by itself.
- TI DLP®: "Always place Texas Instruments or TI before DLP® in the first occurrence in headlines and body copy followed by a superscript registered trademark symbol (®) and then an approved noun" — "DLP® chip", "DLP® technology", "DLP® products"; never "DLP is a chip", never a possessive, plural, verb or abbreviation. Later mentions may drop "TI" and "®" but keep the noun. Fine print: "DLP® and the DLP logo are registered trademarks of Texas Instruments."
- Copyright line on slides and documents: "© 2026 Texas Instruments Incorporated." The DLP logo files and rules live in `assets/Reference/`; they are for DLP-specific work only.

## Visual foundations

### Colour

- The page is `surface` (white). TI's identity is white space with red punctuation; it is not a red brand. Grey tints (`surface-alt`, `grey-050`) separate sections; black is reserved for `ink-strong` and the wordmark.
- One red object per surface: the slide title, or the primary button, or the hero stat, or the footer rule — the title and the footer rule together count as the slide's chrome, so a content slide may carry one more red element at most. Red fills take `ink-on-red`; red text sits only on `white`, `grey-050` or `grey-100`.
- Red hierarchy: `red` for everything new; `red-hover` and `red-active` for button states only; `red-deck` only when extending the 2026 template so the new slides match the old.
- Teal is the second voice: `link` on the web, `teal-deck` for icons and the bold lead-in phrase on slides, `teal-deck-300` for callout fills and secondary chart series. Teal and red never share one element; on one slide red titles and teal icons is the standard pairing.
- Greys: `ink` for web text, `ink-strong` for slide text, `ink-muted` for captions, `grey-deck-caption` for icon labels at 24px+ only. `line` draws every boundary; `line-soft` separates rows.
- Status colours carry a word or an icon as well; `success` and `warning` are never text on their own. Error is `red`.
- Contrast is the floor, not the goal: body text ≥ 4.5:1, text 24px+ or bold 19px+ and every border, focus ring and icon that carries meaning ≥ 3:1, on every surface. When a pair is the point of a slide (a statement, a hero stat) hold it to 7:1. Known near-misses, kept because they are TI's values: `teal` on `grey-100` at 4.6:1, `grey-500` on `white` at 3.0:1 (borders only), `grey-deck-caption` on `white` at 3.9:1 (captions 24px+ only).
- White only in v1. There is no dark theme and no dark slide: TI supplied no reversed (white) signature and red text fails on dark grey. Dividers may use a full `red` or `teal-deck` surface with `ink-on-red` white type, or one of the three title backgrounds; everything else sits on `surface`. A dark theme returns once TI supplies reversed signature files.
- No gradients except ti.com's own 35° section washes (red `#a40000 → #cc0000`, light `#f7f7f7 → #fafafa`), used as full-width web section backgrounds only; never on slides. No glows, no three-colour washes, no blue-purple.

### Typography

- One family: Arial, every weight, everywhere (TI's deck theme sets Arial major and minor; this system standardises on it for web too, where ti.com itself leads with Roboto and falls back to Arial). Chinese text takes `cjk` (Noto Sans TC / Microsoft JhengHei) at the same sizes.
- Web headings are light (300) in `ink`; the first bold step is `h5`. Web body is `body` 14/20, `body-lg` 16/24 for reading. Buttons are `button` 14/20 600. Nothing below `small` 12px on screen.
- Slide titles are Arial Bold in `title` red at `deck-title` 64px (24pt), top-left, one or two lines broken by the author at a sense boundary, never wrapped by the box. Slide body is `deck-body` 32px (12pt) in `ink-strong` and nothing smaller than `deck-caption-sm` 24px (9pt). Bold lead-in phrases inside body copy are `teal-deck`, one per paragraph.
- Three sizes per slide at most (a hero stat may be a deliberate fourth). Headings never use `text-wrap: balance` on slides; measure caps are px, never `ch`.
- Emphasis move: on the web, weight (600) in `ink`; on slides, Arial Bold in `teal-deck` for a phrase, or the whole title in `red`. No italics for emphasis, no underlines except link hover.

### Spacing, layout, shape

- A 4px grid; preferred rhythm `space-6` / `space-12` / `space-24` (24 / 48 / 96) for gutters, blocks and sections. Web content max `container` 1240px; breakpoints at 767 and 1240.
- Slides: `deck-margin` 48px safe margin on every edge, `deck-gutter` 48px between columns, the footer band `deck-footer` 102px tall with the red rule along its top edge and the horizontal signature right-aligned inside the margin at `logo-deck` width. The rule is `deck-rule-weight` 6px (2.25pt) in `accent`, starts at the left edge of the slide and stops `deck-rule-inset` 45px short of the right edge, flush with the right end of the signature. It never runs edge to edge: the open right end is the TI tell, and a rule that touches both edges fails the gate. Only imagery bleeds past the margin. Fill the frame; dead space is a bug.
- Shape: square. `radius-0` for cards, panels, images, slide shapes; `radius-sm` 2px for buttons and inputs; `radius-pill` for tag chips only; `radius-round` for avatars and icon circles.
- Boundaries are `border-hairline` 1px `line`, not shadows. Shadows (`shadow-1`–`shadow-4`) belong to menus, popovers and dialogs. A card at rest has a border and no shadow.
- Focus: `focus-ring` 2px solid, offset 2px, plus ti.com's `shadow-focus` halo on inputs. Honour `prefers-reduced-motion`.

### Controls (ti.com, until components are built here)

- Primary button: `red` fill, `ink-on-red` text, `radius-sm`, height `control-height`, 600 weight, hover `red-hover`, active `red-active`. One per view.
- Secondary button: `white` fill, 1px `red` border, `red` text; hover inverts to `red-hover` fill with white text.
- Tertiary (text) button and links: `link` text, no fill, hover `link-hover` with a 1px underline.
- Reversed button (on a `red` section wash): `white` text, 1px `white` border, transparent; hover `white` fill with `grey-900` text.
- Inputs: height `control-height`, `space-3` inline padding, 1px `control-border`, focus `control-border-focus` + `shadow-focus`; placeholder `grey-600`; disabled `grey-200` fill with `grey-400` text.
- Disabled buttons: `grey-300` border and text on transparent.

### Imagery

- TI photographs the real thing: fabs, cleanrooms, boards, products, people at work in TI buildings. Clean, high-key, blue-white light, no filters, no stock gestures. People appear working, not posing. The deck mixes photography with outline icons and flat data graphics; it never uses illustration or 3D renders.
- Title-slide backgrounds are the three supplied files in `assets/Backgrounds/` (grey circuit, light facets, teal circuit): the circuit-trace motif is TI's own and is not redrawn. Content slides are plain white.
- Charts: data ink only, `red` for the series that matters, `teal-deck`/`teal-deck-300`/`grey-deck-light` for the rest, labels in `deck-caption`. Donuts with one headline figure inside are a TI habit; keep them.
- Any slot without a real image carries a labelled placeholder (`Type · Aspect · generate W×Hpx` + a hint + a prompt) and never a bare grey box; stock stand-ins carry a visible swap flag. The Imagery section has the full workflow.

## Iconography

- One icon library: Microsoft's Fluent UI System Icons (`@fluentui/svg-icons` 1.1.343, MIT), regular style only. The whole library is catalogued in `assets/Icons/catalog.json` (2988 names, every size and style that exists, plus the CDN pattern to fetch any of them); the 118 most useful for TI work are stored in `assets/Icons/` as teal SVGs ready to place. Nic's call, Oct 2026: Fluent replaces TI's own deck icons as the working set because it is complete, consistent and licensed; the 29 TI originals stay under `assets/Reference/` with their Fluent equivalents listed in the catalogue.
- Style: `regular` (outline) always. `filled` only as the selected state of a control. Never `color`, never mixed styles on one surface, never two libraries in one artefact.
- Colour: `teal-deck` on slides, `ink` or `link` on the web, white only on a `red` or `teal-deck` divider. Never red icons; red is for type and the rule. The stored SVGs carry `fill="#117788"` (and `-ink` copies in #333333); any other colour is a one-line edit of that attribute.
- Size: build from the 24 or 32 master, scale to `icon-deck` 120px on slides, `icon-lg` 36px beside text, `icon-md` 24px inline, `icon-sm` 18px in buttons. Icons sit above a `deck-caption` label or left of text with a `space-3` gap.
- No emoji in TI work, inline or decorative. Unicode glyphs (→ ✓ ·) are allowed inline in text.

## Logos

- Two approved signatures. TI's trademark page: the preferred signature is the stacked one ("the word 'Texas' to the right side of the logo and the word 'Instruments' under the word 'Texas'"); the alternate is horizontal ("the words 'Texas Instruments' to the right side of the logo"). Red mark + black wordmark is the primary colourway; all-black is the one-colour version. Files and sizes: `assets/Logos/README.md`.
- Never the mark alone, never recoloured, rotated, stretched, outlined, placed in a coloured shape or over a busy photo. Clear space: at least the height of the mark on all sides (TI publishes no figure for the corporate signature; the DLP rule is "the width of the letter D" and this is the stricter of the two).
- No white or reversed signature was supplied, which is why v1 has no dark surfaces. Never invert the files. A `red` or `teal-deck` divider carries no signature; the signature returns on the next white slide.
- Deck chrome: horizontal signature bottom-right inside the margin at `logo-deck` 280px wide; the `red` rule above the footer band runs from the left edge and stops 45px short of the right edge, flush with the signature's right end; page number in `deck-caption-sm` bottom-right above the rule. Internal decks carry it on every page; external carousels on cover and closing only.


---

<sub>Texas Instruments design system — built by **Nicolas Chan**, Head of Digital & Chief Strategist, AMEA, The Hoffman Agency. Texas Instruments, the TI signature and TI DLP® are trademarks of Texas Instruments Incorporated; see `LICENSE.md`.</sub>
