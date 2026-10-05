# Deck template (PowerPoint / Google Slides)

`TI_Deck_Template_v1.pptx` is the buildable form of the Decks section: TI's own 2026 master with the theme corrected to canon (dk2, accent1, hlink and the footer rule all #CC0000; Arial major and minor; 10 × 5.625 in), 34 fillable layouts in the New Slide menu, and fifteen example slides that show finished versions with slot specs and word budgets in the speaker notes. It lives at `templates/powerpoint/TI_Deck_Template_v1.pptx`, complete: TI's master with the signature in the footer of every white layout, the title backgrounds on the cover and closing layouts, and Fluent icons on the example slides. Download it and start.

## How to use it

1. Copy the template; keep slide 1 ("Start here") until the end, then delete it with the example slides you don't need.
2. Add slides with Home → New Slide and pick a layout. Type into the boxes: the grey prompt text names what goes there and its word budget, and never prints. To rearrange a slide, change its layout (Home → Layout); don't draw loose text boxes, so a later design pass can re-lay the deck from the layouts.
3. Write the title spine first and run the Title Test (Soundcheck) before touching a single slide.
4. Run the Delivery gate; the finished-file checks in PowerPoint production apply.

Google Slides: upload the .pptx to Drive and open it with Google Slides (or File → Import slides into an existing deck). Arial, the theme colours, the footer chrome and the notes survive the import; connectors become plain lines, so check the L35 arrows after importing.

## The 34 layouts

In menu order. Codes match the layout library in `DECKS.md` where one exists.

| Group | Layouts |
| --- | --- |
| Open and navigate | Cover · L01 · Section divider · L02 (red, number + 1–2 words, no signature) · Appendix divider · L02 teal · Agenda · L03 (five numbered rows) |
| Words | Title + body · Two columns (teal headings) · Statement + two panels (teal and grey-100) · Title + three points · Statement · L08 · Key point · teal (the one teal content page; no signature) |
| Columns | Three columns · L12 (icon cards) · Four columns + photos · Three photos + text · L49 · Two columns + photos |
| Numbers and plans | Stat strip · L19 (hero in red, two in black, source line) · Chart + takeaway · Table · L24 · Programme at a glance · L10 (four-stage matrix) · Timeline · L20 (five nodes) |
| Images | Image + text · L28 · Text + image half · Text + image third · Image two-thirds + text · Title + body + image band · Text + image + two stats · Image + three points · L48 · Photo collage · L42 |
| People | Team · L15 (four) · Team of 10 · L15 · Single bio · L16 |
| Close | Pull quote · L29 (teal) · Title only · Closing · L30 · Blank |

Sixteen of these are adapted from The Hoffman Agency's 2025 AMEA PowerPoint template, one per layout family (its colour repeats were skipped): rescaled from 13.33 to 10 in, kept above TI's footer band, set in Arial, and remapped into TI's palette (navy and purple panels → teal, lime and light panels → grey-100, lime text on dark → white, titles → TI red). Content pages stay white; red and teal surfaces are for dividers, the key point and the pull quote.

## The fifteen example slides

| # | Layout | What it is | Slots and caps |
| --- | --- | --- | --- |
| 1 | README | Start here: the five rules | delete before sending |
| 2 | L01 Cover | grey-circuit background, eyebrow, headline, subtitle | eyebrow ≤6 words teal caps · headline ≤8 words 30pt red · subtitle ≤14 words |
| 3 | L03 Agenda | numbered list with grey AGENDA wordmark | 3–5 items, number + ≤4-word label |
| 4 | L02 Section divider | full red surface, part number and 1–2-word title | no signature on a coloured divider |
| 5 | L08 Statement + support | 34pt claim with one red phrase, ≤30-word support, evidence slot | one stat, quote or chart |
| 6 | L12 Three icon cards | three bordered cards, Fluent icon in teal, teal heading, two bullets | heading ≤7 words, bullets ≤22 words |
| 7 | L22 Icon benefit grid | six cards alternating white / grey-100 | ≤4-word title + ≤18-word line |
| 8 | L37 Numbered points | three columns with hairline rules, first number red | ≤4-word title + one ≤14-word line |
| 9 | L35 Before → After | three boxes, middle teal, real connector arrows | eyebrow ≤3 · title ≤4 · one line |
| 10 | L19 Stat strip | hero stat 60pt red + two context 44pt black, source line | number + ≤4-word label, max 3 |
| 11 | L28 Split 50/50 | labelled photo placeholder bleeding left, eyebrow / headline / body / CTA right | body ≤30 words |
| 12 | L20 Timeline | five nodes on a hairline, one red | date + ≤2-word label + ≤15-word note |
| 13 | L24 Scope table | hairline table, grey-100 header | the one dense slide |
| 14 | L29 Pull quote | full teal surface, white 28pt quote, attribution | ≤20 words; real or `[REAL DATA]` |
| 15 | L30 Closing | light-facets background, imperative headline, contact | ≤6 words; no recap |

Layouts in the library but not yet in the template: L31/L32 edge-bar cover and divider, L09, L45–L47, L50 (statements and openers), L10, L34 (diagrams), L11, L13 (columns), L14–L16 (people), L17, L18, L39, L40 (ideas), L33, L38, L41 (data), L21 (process), L23, L36, L48, L49, L24b, L25, L26 (capability), L27, L42–L44 (image), L51 (closer). Build them on the same master when a deck needs them and add the example slide back to the template.

## Theme map (as set in the file)

Footer chrome, inherited from TI's master: red rule 2.25pt from the left edge to 9.765 in (stops 0.235 in short of the right edge, flush with the signature's right end); signature 1.71 × 0.21 in at x 8.02, y 5.23 in. Content layouts carry a live slide number (9pt, `grey-deck-caption`) right-aligned above the rule.

Theme "Texas Instruments": dk1 #000000 · lt1 #FFFFFF · dk2 #CC0000 · lt2 #808080 · accent1 #CC0000 · accent2 #A4A4A4 · accent3 #117788 · accent4 #404040 · accent5 #4ABED4 · accent6 #7F7F7F · hlink #CC0000 · folHlink #AAAAAA · fonts Arial / Arial. Custom colours in the colour picker: TI red, teal, teal 500 #2790A5, teal 400 #32B4CE, teal 300, grey dark, grey mid, grey light, hairline #CCCCCC, panel grey-100 #F7F7F7. Defaults for new objects: shapes teal with white Arial 12pt, lines teal 1.5pt, text boxes Arial 12pt; new tables use the "TI hairline" style (hairline rows, grey-100 header).

## Rebuilding the template

The layouts are generated, never hand-drawn: `python3 tools/add_layouts.py` adds the TI layouts, theme and table style to the template; `python3 tools/port_hoffman_layouts.py <Hoffman AMEA template.pptx>` adds the sixteen adapted layouts. Both skip layouts that already exist, so they are safe to re-run.

---

<sub>Texas Instruments design system — built by **Nicolas Chan**, Head of Digital & Chief Strategist, AMEA, The Hoffman Agency. Texas Instruments, the TI signature and TI DLP® are trademarks of Texas Instruments Incorporated; see `LICENSE.md`.</sub>
