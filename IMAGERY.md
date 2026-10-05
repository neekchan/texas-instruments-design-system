# Imagery and icons

## The workflow, in order

1. **Capability check.** State plainly what you can produce in this session: generate images, place supplied images, or only write placeholders. Never promise images you can't make.
2. **Ask the user:** generate · they supply · labelled placeholders. Fold in anything already said; never re-ask.
3. **If generating**, ask for 2–4 samples of the look they want and write one reusable, subject-agnostic style prompt (medium, palette, treatment of people and objects, light, composition, mood). Reuse it for every image in the piece; generate at the slot's aspect and resolution; fill the frame. Without samples, use the TI photographic default below.
4. **If you can't generate**, every slot carries a labelled placeholder, never a bare box.
5. **Priority for any slot:** real TI image → curated stock stand-in flagged for swap → labelled placeholder.

Two kinds of image, never confused: a photograph shows a real place, product or person (never generate a real named person); an illustration carries a concept. TI's corporate material uses photographs, line icons and flat charts; it does not use illustration, 3D renders or painterly styles. One image language per artefact.

## TI photographic default

Real environments: wafer fabs, cleanrooms, test floors, labs, the Dallas and Taiwan offices, products on boards. High-key, clean, cool white light with the blue-white cast of a fab; no colour grading, no vignettes, no lens flare. People at work in bunny suits or business casual, task in hand, unaware of the camera; no smiling at the lens, no arranged huddles, no symmetrical clean framing. Signage present, never legible. Image models can't typeset: never ask for headlines or labels inside the image; type is set in the deck layer.

Prompt template: `[SHOT TYPE], [SUBJECT doing what], [LIGHT], [WARDROBE/SET], documentary semiconductor-industry photograph, clean high-key, no filters, [ASPECT + W×H px]`. Standing negatives: `no text, no logo, no emblem, no stock-photo posing, no smiling at the lens, no group walking abreast, no illustration, no 3D render`.

Never let a generative model draw a brand asset. The signature is placed as the real file; put `no mark, no emblem, no logo, no text` in every negative prompt.

## Placeholder anatomy

A dotted 1px `line` border on `surface-alt`, square corners, true to the slot's size, with three lines inside:

- `__label` — `Type · Aspect · generate W×H px` (16:9 → 1920 × 1080 · 4:3 → 1440 × 1080 · 3:4 → 1080 × 1440 · 4:5 → 1080 × 1350 · 1:1 → 1280 × 1280 · 3:1 → 1800 × 600 · 2:1 → 1600 × 800 · 9:16 → 1080 × 1920).
- `__hint` — art direction for the human ("RFAB2 cleanroom, two engineers at a tool, wide").
- `__prompt` — 2–3 full sentences for a generator, click to copy.

Placeholder labels on slides are 22px, hints 17px: the one exception to the 24px floor, because they never ship. `object-fit: cover` always carries an `object-position`; faces live high (`center 18–25%`).

## Backgrounds

Three TI title backgrounds live in `assets/Backgrounds/`: `title-grey-circuit.jpg`, `title-light-facets.jpg`, `title-teal-circuit.jpg` (1920 × 1080). Cover and section slides only, full-bleed, with the title in `title` red (grey and light files) or `white` (teal file, lower-left where the teal is densest — check the pair at 4.5:1 on the actual crop). The circuit-trace motif is TI's; never redraw it, tile it or use it behind body copy.

## Icons

- The library is Fluent UI System Icons (Microsoft, MIT), `regular` style, via `@fluentui/svg-icons` 1.1.343. `assets/Icons/catalog.json` lists every icon name with its available sizes and styles and the CDN URL pattern; `assets/Icons/` holds 118 curated teal SVGs. Need another? Take it from the catalogue by name, set `fill` to the token colour, store it beside the others.
- Fluent is a flat, single-weight outline family on a 24px grid, close in spirit to TI's own thin-line deck icons; the catalogue's `ti_deck_equivalents` maps each of TI's 29 originals to its Fluent replacement (chip → `developer_board`, shield-chip → `shield_task`, support chat → `chat_multiple`, …). TI's originals are kept under `assets/Reference/` for comparison only.
- Colour: `teal-deck` on slides, `grey-900`/`link` on the web, white on a coloured divider. Never red; never `filled` or `color` styles as the working set; never emoji.
- Placement: above a `deck-caption` label, centred, in rows of 3–7 with equal gaps; or left of text at `icon-lg` 36px with a `space-3` gap. On a slide, 120px (`icon-deck`) from the 24 or 32 master; the PowerPoint template carries 512px PNG renders for this.
- In `.pptx`, place the PNG render (or the SVG where the editor keeps it vector); in HTML, inline the SVG so it takes `currentColor`.
- Unicode glyphs (→ ✓ ✗ ·) are fine inside a sentence; they are not icons.

## Charts and data graphics

Flat, data-ink only, in Arial. `red` for the series or segment that carries the point, `teal-deck` / `teal-deck-300` / `teal-deck-500` for the rest, `grey-deck-light` for context. Labels in `deck-caption` `ink`, directly on the data; no legends when direct labels fit. Donut with one headline figure inside at `deck-stat`: a TI house habit, keep it. Maps: `grey-200` land, `red` dots for sites with `deck-caption` labels, as the footprint slide does.


---

<sub>Texas Instruments design system — built by **Nicolas Chan**, Head of Digital & Chief Strategist, AMEA, The Hoffman Agency. Texas Instruments, the TI signature and TI DLP® are trademarks of Texas Instruments Incorporated; see `LICENSE.md`.</sub>
