# PowerPoint production

How a TI deck becomes a native `.pptx` that survives someone else's laptop.

## Two paths

- **Start from the template.** `TI_Deck_Template_v1.pptx` (`DECK-TEMPLATE.md`) already carries the corrected theme, Arial and the footer chrome, 34 fillable layouts (red section dividers, teal appendix divider, prompts carrying the word budgets, live slide numbers) and one example slide per core layout. Add slides from the layouts and type into the placeholders; don't rebuild the master.

- **Path A (prefer):** build the deck as HTML from the layout list, then export an editable `.pptx` with Arial available to the exporter and the slide size set; hide HTML-only chrome; run the finished-file checks. A screenshot-mode export is not editable and does not count.
- **Path B:** hand-build with python-pptx or equivalent from this section and `tokens.json`. If the tool cannot preserve the fonts or the theme, it must say so in the delivery report.
- **Extending a deck TI supplied** (e.g. its 2026 corporate deck, kept with Hoffman's TI client files, never in this repo): open it, keep its master, add slides on its layouts ("Title Only", "Title and Content", "Two Content", "Content with Caption", "Blank"). Its red is `red-deck` and its footer rule is `#ff0000`; match the deck you are in, don't correct it mid-deck.

## Theme, not paint

Set the theme once and let every shape inherit it. Nothing is painted with a literal hex that the theme already carries.

| Office slot | Token | Hex |
| --- | --- | --- |
| dk1 (text) | `black` | #000000 |
| lt1 (background) | `white` | #ffffff |
| dk2 (titles) | `red` (template: `red-deck`) | #cc0000 (#de0000) |
| lt2 | `grey-deck-caption` | #808080 |
| accent1 | `red` | #cc0000 |
| accent2 | `grey-deck-light` | #a4a4a4 |
| accent3 | `teal-deck` | #117788 |
| accent4 | `grey-deck-dark` | #404040 |
| accent5 | `teal-deck-300` | #4abed4 |
| accent6 | `grey-deck-mid` | #7f7f7f |
| hlink | `red` | #cc0000 |
| folHlink | `grey-400` | #aaaaaa |

Major font Arial, minor font Arial (Latin, East Asian and Complex script slots all Arial; East Asian may be Microsoft JhengHei for Traditional Chinese decks). Slide size: 10 × 5.625 in (the template) or 13.333 × 7.5 in; both are 16:9. Title style: 24pt bold, `dk2`, line spacing 85%, left-aligned. Body style level 1: 18pt in the master, but the template's slides run 12pt (32px at 1920) — set body text explicitly at 12–14pt.

## Fonts: presence is not use

Arial is installed everywhere, which is the reason it was chosen; the risks are the other direction. Check every run: no Calibri, Aptos, Roboto, Times New Roman or 新細明體 left over from a copied text box (the 2026 template contains all of these in stray runs). CJK runs set their East Asian font explicitly. A preflight specimen slide with every tier is rendered before the deck is built.

## Signature geometry

- Horizontal signature ratio 280:36 (7.78:1) from the ti.com vector; the stacked PNGs are 640 × 360 canvases with the signature inside — crop or place on white only. Never set width and height independently: `height = width / ratio`; lock the aspect ratio; more than 1% off fails.
- Slide footer: horizontal signature 280 × 36 px (at 1920 wide; 1.46 × 0.19 in on the 10-in template) right-aligned inside `deck-margin`, vertically centred in the 102px footer band. The red rule: 2.25pt, from x = 0 to x = 9.765 in on the 10-in template (0 to 1875 px at 1920), 102px (0.53 in) above the bottom edge. It stops short of the right edge, flush with the signature's right end; it does not touch the right edge.
- Protected area: the signature's rectangle grown by the mark's height on every side. Nothing enters it. The footer band holds only the rule, the signature and the page number.

## Layouts are contracts; arrows connect

Each layout code names its slots and their roles. Preserve the roles or choose another code. Workflow and before → after slides use L35 with real connectors: every arrow starts at a source shape's boundary and ends at a target's boundary or centreline, drawn in the same pass as the nodes, one shared connector style across repeats. No arrow glyphs typed as text.

## Image gates

Preserve ratio, never stretch; explicit crop-to-fill or contain. No upscaling a low-resolution image past tolerance (the deck's own icon PNGs are 80–230px: at `icon-deck` 120px they are at their limit, never larger). Faces sit high in a crop (`center 20%`), not centred. Placeholders beat weak images.

## Full-size visual review

Render every slide of the finished file at full size and look at each one; a contact sheet shows rhythm, not compliance. Precondition: Arial actually installed on the rendering machine (`fc-list | grep -i arial`); otherwise stamp the review "FONTS MISSING — NOT EVIDENCE".

## The 17 hard checks

1 opens, slide count · 2 16:9 at the declared size · 3 theme colours match the table · 4 theme fonts Arial/Arial · 5 no fallback or stray font in any run · 6 approved signature files only · 7 signature ratio within 1% · 8 signature on white (no inverted file) · 9 nothing inside the protected footer area but chrome; the footer rule stops short of the right edge, flush with the signature · 10 nothing off-slide · 11 no stretched image · 12 no over-enlarged low-res image · 13 no raw Unicode emoji or symbol fonts · 14 every arrow connects · 15 no unresolved placeholder or production note · 16 speaker notes present in Presenter mode · 17 no heading has wrapped on its own.

Advisory: more than 3 sizes on a slide; Presenter slide over 15 words; more than ~7 groups; rounded rectangles; a headline with no emphasis; layout code not noted in the slide's notes.


---

<sub>Texas Instruments design system — built by **Nicolas Chan**, Head of Digital & Chief Strategist, AMEA, The Hoffman Agency. Texas Instruments, the TI signature and TI DLP® are trademarks of Texas Instruments Incorporated; see `LICENSE.md`.</sub>
