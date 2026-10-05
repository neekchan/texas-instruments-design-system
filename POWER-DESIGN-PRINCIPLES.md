# Power Design principles

Twenty portable craft rules, kept separate from tokens so they travel across any brand. Tokens say what it looks like; principles say how it must behave and decide. Each rule carries a test. If you can't write a test for it, it isn't codified yet.

**Precedence.** Universal craft wins for 01, 02, 03, 06, 07, 09, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20. TI's house SOPs in the Decks section win on 04, 05, 08 and 12 (density, margin, body floor and palette ratio differ on slides). No conflict: both hold. Rule 20 is hard.

| # | Rule | Test | Why |
| --- | --- | --- | --- |
| 01 One idea | Max one headline (≤ 10 words) and at most one supporting block per slide. | Count headlines and blocks. | Reynolds; Duarte |
| 02 Glanceable | The single message is extractable in ≤ 3 seconds. | Show for 3 seconds, hide, ask what it said. | Duarte; NN/g |
| 03 Chunks | ≤ 7 distinct visual chunks per slide; aim for 3–5; group by proximity. | Count chunks at arm's length. | Miller 1956; Cowan 2001 |
| 04 Whitespace | Web: ≥ 40% of the area empty, hero ≥ 60%. Slides: overridden by "fill the frame". | Measure empty area. | Refactoring UI; Presentation Zen |
| 05 Safe zone | 5% clear margin every side (≥ 96px on 1920 × 1080). House: `deck-margin` 48px, as the TI template sets it. | Nothing but chrome inside the margin. | SMPTE/EBU title-safe |
| 06 Type scale | Pick one modular ratio and derive every size from it. TI web: ti.com's fixed scale (12/14/16/20/24/28/34/48). | Every size on the list. | Bringhurst; Tim Brown |
| 07 Four sizes | ≤ 4 distinct sizes per slide, ≤ 6 across the deck. House is stricter: ≤ 3 per slide. | Count sizes. | Refactoring UI; Müller-Brockmann |
| 08 Body ≥ 24px | Body ≥ 24px on screen, title ≥ 48px, caption ≥ 18px. House deck scale is higher: body 32px, caption 24px. | Smallest run. | Reynolds; Duarte |
| 09 Line height | Body 1.4–1.6; display 1.05–1.2 (TI's title master is 0.85 — keep it only for the red slide title). | Inspect. | Butterick; Bringhurst |
| 10 Line length | ≤ 60 characters per line; slides should have no paragraphs at all. | Count the longest line. | Bringhurst; Butterick |
| 11 Contrast | ≥ 4.5:1 body, ≥ 3:1 large; target 7:1 for projector resilience. | Ratio per pair, both themes. | WCAG 2.2 |
| 12 60-30-10 | Web and social: 60% dominant (white), 30% secondary (greys), 10% accent (red, teal). Not applied per slide. | Eyeball the area split. | Itten; Refactoring UI |
| 13 One accent | One accent colour per slide for emphasis. | Count accents. | Tufte |
| 14 No hue-only | Never encode meaning by hue alone; pair with shape, weight, label or icon; must survive grayscale. | Print in greyscale. | WCAG 1.4.1; ColorBrewer |
| 15 4/8pt grid | Every margin, padding and gap in {4, 8, 12, 16, 24, 32, 48, 64, 96}. | Inspect the spacing tokens used. | Material; Bryn Jackson |
| 16 One grid | A single 12-column grid, 24–32px gutters; every element snaps. | Overlay the grid. | Müller-Brockmann |
| 17 Proximity | Related ≤ 16px apart; unrelated ≥ 48px. | Measure. | Gestalt; Williams |
| 18 Data ink | Data-ink ≥ 80%; no 3D, gradients, drop shadows on bars, chart junk, decorative gridlines. | Strip each element and ask if data was lost. | Tufte |
| 19 F-pattern | Headline and key visual in the top band; the first 200px vertical is the primary attention zone; centred-everything fails. | Trace the eye path. | NN/g |
| 20 Mode purity (hard) | Each deck declares exactly one mode: Presenter (≤ 15 words, image-led, 1 idea) XOR Document (denser, hierarchical, short bullets). | Read the declaration; check every slide. | Tufte vs Reynolds |

Add your own with the same shape: `NN · name / Rule / Test / Fails when / Why`.


---

<sub>Texas Instruments design system — built by **Nicolas Chan**, Head of Digital & Chief Strategist, AMEA, The Hoffman Agency. Texas Instruments, the TI signature and TI DLP® are trademarks of Texas Instruments Incorporated; see `LICENSE.md`.</sub>
