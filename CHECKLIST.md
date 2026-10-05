# Delivery gate

This is a gate, not a tick list. Every TI deliverable passes through it before it ships. Three tiers:

- **HARD** — any FAIL blocks ship. No exceptions, no "flagged for later": content integrity · trademark and signature use · contrast · built inside the system · functional (web and app) · finished file (`.pptx`).
- **LOCKS** — everything else. Fix it, or write a one-line reason for the exception in the report. Silence is not an exception.
- **Evidence or it didn't happen** — a PASS line states what was checked and how (a count, a path, the render that was looked at). A bare "PASS" is a FAIL. A screenshot is not a render; a tick is not a check.

## Before you build

- Intake run (medium, mode, audience and language, colour direction, imagery) and the one-line brief restated. See Agent workflow.
- Imagery decided up front: real, supplied, placeholder.
- Built inside the system: `tokens.css` loaded, started from a named layout, no bespoke chrome, no re-typed hex values.

## Content integrity — HARD

- Every number is real and traceable: source in speaker notes, a `deck-caption-sm` source line, or the build note. A number with no source is cut, not kept because it looks right.
- No invented testimonials, quotes, named people, client names, logos, awards, press mentions or case-study results. TI's own figures come from TI's own documents (the 2026 overview deck, annual report, ti.com) with the date they were true.
- Unknown content is a visible labelled placeholder `[REAL DATA · what goes here · who supplies it]` in the surface itself. Stock stand-in imagery carries a visible swap flag.
- Qualifiers survive the edit: "approximately", "up to", "in pilot", "estimated", "n = 12". Repeated figures are single-sourced.
- Deck level: each slide's governing thought is supported by what is on the slide or in its notes.

## Trademark and signature — HARD

- Only the approved signature files from `assets/Logos/` (or TI-supplied vectors); never the mark alone; never recoloured, stretched, rotated, outlined, boxed or over a busy image; clear space ≥ the mark's height.
- No white/reversed signature exists in this system: no dark surfaces in v1; a `red`/`teal-deck` divider carries no signature; never invert the files.
- "Texas Instruments" in full on first mention; TI DLP® rules followed; "© 2026 Texas Instruments Incorporated." where a copyright line belongs.

## Contrast — HARD

- Every text/surface pair ≥ 4.5:1, or ≥ 3:1 at 24px+ / bold 19px+; borders, focus rings and meaningful icons ≥ 3:1; checked on every surface used.
- Display pairs that are the point of the slide held to 7:1 (`title` red on white is 5.9:1: a red statement is set 64px+ or made `ink-strong`).
- Red text only on `white`, `grey-050`, `grey-100`. `teal` text only on `white` and `grey-100`. `success`/`warning` never as text alone.

## Functional — web and app — HARD

- Every link resolves (no `href="#"`); no dead controls (acts, or visibly inert with `disabled` and a reason).
- Keyboard-reachable with the `focus-ring` visible; `prefers-reduced-motion` honoured.
- States are marked, not invented (`<!-- TODO state: loading — spec reserved -->`).
- Run before ship: opened, clicked through, console clean; the report says what was clicked.

## Finished PowerPoint file — HARD

Opens · slide count matches · 16:9 (10 × 5.625 in to match the template, or 13.333 × 7.5 in when starting fresh — one per deck, stated) · theme fonts Arial major and minor · theme colours map to the palette (`POWERPOINT.md`) · no fallback font in any run · only approved signature files, ratio within 1% · nothing in the footer band but chrome · nothing off-canvas, no stretched or over-enlarged image · every arrow connects a visible source and target · no unresolved placeholder or production note · speaker notes present in Presenter mode · advisory: ≤ 3 sizes, ≤ 15 words per slide in Presenter, square corners, layout code noted.

## LOCKS

**Deck mode and type** — one mode declared · Presenter ≤ 1 idea / ≤ 15 words, image-led · Document denser but no paragraphs · titles fill the width and break at authored `<br>`s, no `ch` caps, no `text-wrap: balance` · every content slide carries a visual · chunked, not dumped · `data-screen-label` on every slide · slide scale as floors, ≤ 3 sizes · no micro-text, 3–5 large elements · sentence case; UPPERCASE only on section strips.

**Colour and surfaces** — one dominant colour per slide · one red object beyond the chrome · teal and red never on one element · no gradients beyond ti.com's four section washes · page and card one step apart, cards keep a 1px `line` border, no shadow at rest.

`IMAGERY.md` — one image language per piece · labelled placeholders with label + hint + prompt, true to size · Fluent UI System Icons, regular style only, one colour per slide, `teal-deck` or `ink` · no emoji · no illustration or 3D unless the client supplies it.

**Logo and chrome** — signature bottom-right inside the margin at `logo-deck` on slides; the `accent` footer rule starts at the left edge and stops 45px short of the right edge, flush with the signature's right end (a rule that touches both edges is a FAIL) · internal decks every page, external carousels cover and closing only · web: header signature ≥ `logo-min-web`.

**Layout** — 4px grid · `deck-margin` 48px, imagery bleeds on the full-bleed set only · square corners, `radius-sm` on controls, pills on tags only · no frosted glass, parallax or scroll-jacking · web content ≤ `container`.

**Format sizing** — deck 1920 × 1080 · square tile 2160 × 2160 (1080 min) · vertical story 1080 × 1920 · web hero 1440 × 900 · print A4 at 300dpi · social safe zone ≥ 80px from every edge.

**Voice** — reads as TI (plain, specific, engineer-to-customer) · no agency clichés · active voice, short sentences, qualifiers kept · CTA is verb + object ("Buy on TI.com", "Download the datasheet"), never "Learn more" · decks and documents reviewed with Soundcheck.

## Anti-patterns (do instead)

1. Web spacing on slides → deck scale, 48px margin, fill the frame. 2. 16–18px slide body → 32px body, 64px titles. 3. One generic big-type slide repeated → named layouts, varied composition. 4. Mixing Presenter and Document → declare one. 5. Leaving out imagery → real image, then placeholder, then an icon as the graphic beat. 6. Emoji anywhere in TI work → remove; TI uses icons. 7. Accent text on a tint → `red` only on white/`grey-100`; else `ink`. 8. White text on `teal-deck-300`, `warning`, `teal-light` → `ink-strong`. 9. Bare grey image boxes → labelled placeholder. 10. Marketing hero styling in an app → ti.com control specs. 11. Nested card dashboards → sections, panels, tables. 12. Many accents on one surface → one dominant per slide. 13. Italic emphasis → bold `teal-deck` phrase or `red` title. 14. Vague "image here" → subject, composition, mood, aspect, size. 15. Jargon → short, specific, active lines. 16. Bespoke chrome or re-typed hex → tokens and the layout list. 17. Skipping intake then rebuilding → intake first. 18. Truncated or half-width title → never clip; authored breaks; grow or fill. 19. Text-only slide with empty margins → add a visual or scale up. 20. Paragraph or six-line bullet stack → 2–4 labelled beats. 21. Two image styles in one piece → one language. 22. Slides with no identity in markup → `data-screen-label`. 23. A logo that vanishes on its own surface or an inverted logo → white page or flag it. 24. Invented statistic, quote, client, award → sourced or `[REAL DATA · …]`. 25. Stock stand-in with no swap flag → caption or tag until the real asset lands. 26. Ghost links and dead controls → resolve or mark inert. 27. A delivery report PASS with nothing behind it → evidence per line. 28. Rounded cards, drop shadows at rest, blue-purple gradients → square, bordered, white. 29. Red and teal on one element → pick one. 30. Building against a stale copy of the system → re-read the README and `tokens.json` first.

## Delivery report (write it; under 15 lines)

```
DELIVERY GATE · <deliverable> · <medium> · <Presenter|Document|n/a> · TI system v<X.Y.Z>

HARD  content integrity   PASS — 14 figures, 14 sourced in notes; 2 slots left as [REAL DATA] on slides 06, 11
HARD  trademark/signature PASS — ti-signature-horizontal.svg at 280px on 24/24 slides; "Texas Instruments" on slide 01
HARD  contrast            PASS — 9 type/surface pairs, all ≥ 4.5 or ≥ 3 at ≥ 24px
HARD  built in system     PASS — tokens.css loaded; layouts L03, L20, L35; 0 literal hex values
HARD  functional          n/a — static deck
HARD  finished file       PASS — rendered 24/24 slides at full size with Arial; 0 fallback fonts

LOCKS 31 checked · 2 exceptions — <reason each>

VERIFIED BY  <what was actually opened / rendered / read>

RESULT  SHIP   (or: DO NOT SHIP — <HARD section> FAIL, <detail>)
```

A HARD FAIL is DO NOT SHIP. A PASS without evidence is a FAIL. Exceptions get a reason, not an apology; if the reason doesn't survive being read aloud, it isn't an exception.


---

<sub>Texas Instruments design system — built by **Nicolas Chan**, Head of Digital & Chief Strategist, AMEA, The Hoffman Agency. Texas Instruments, the TI signature and TI DLP® are trademarks of Texas Instruments Incorporated; see `LICENSE.md`.</sub>
