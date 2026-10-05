# Agent workflow

How an agent (or a person) starts, builds and ships TI work with this system. Many entry points, one canon: this section routes; the README and `tokens.json` hold the values; the Decks section is the slide authority; the Delivery gate is the exit.

## Step 0 · Intake

Run before anything is built. Fold in what the user already said; never re-ask.

1. **Medium** — slides, document, web page, social tile, print, app UI. Slides: HTML or `.pptx`? Presenting live or sending a link → HTML; someone else will edit it → `.pptx` (`POWERPOINT.md`).
2. **Mode** (slides and documents) — Presenter or Document. Infer from context and state it; ask only if ambiguous.
3. **Audience, tone, language** — TI stakeholders (US English, engineer-to-customer register), Taiwan stakeholders (Traditional Chinese set in `cjk`, English report), candidates, press. Voice stays TI's; Hoffman material about TI stays third person.
4. **Colour direction** — white default. Any red or teal divider surfaces beyond the standard chrome? No dark surfaces in v1.
5. **Imagery** — real TI images, user-supplied, generated to the TI default, or placeholders; capability check first.

Then echo one line: *Building a **[medium]** in **[mode]** for **[audience]**, **[colour direction]**, with **[imagery choice]** — starting from **[layout codes / template]**.* Intake sets the brief; the system sets the build.

## Step 1 · Route by task

| User asks for | Read | Start from | Key rule |
| --- | --- | --- | --- |
| A deck, pitch, talk, read-ahead | README · Decks · Soundcheck · `tokens.json` deck group | The layout list (L01 … L51); the 2026 template when extending it | One point per slide; red chrome, teal accents; authored title breaks |
| A `.pptx` | the above + PowerPoint production | Theme table | Theme, not paint; Arial in every run |
| A document, one-pager, report | README · Soundcheck · Delivery gate | Web type group, A4 or Letter at 300dpi | Titles argue; numbers sourced; `red` sparingly |
| A web page or microsite | README · `tokens.json` web group · controls | ti.com control specs | `container` 1240, `body` 14/20, light headings, square cards with `line` borders |
| A social tile or carousel | README · Imagery | 2160 × 2160 or 1080 × 1920 | Signature on cover and closing only; 80px safe zone |
| A chart or data graphic | Decks §8 · Imagery (charts) | Data-ink rules | `red` for the point, teal for the rest, direct labels |
| Copy only | README content fundamentals · Soundcheck | — | Plain, specific, qualifiers kept, trademark rules |

## Step 2 · Build inside the system

- Load `tokens.css` (served beside `tokens.json`) and reference tokens by name; a literal hex in a build is a smell and the gate counts them.
- Start from a named layout; give every slide `data-screen-label`; keep the TI slide anatomy.
- Write titles first as a spine and run the Title Test (Soundcheck 7) before designing a single slide.
- Place assets from `assets/` by their files; never redraw a logo or an icon; never invert the signature.
- Chinese-language work: same tokens, `cjk` family, the same sizes; CJK runs in `.pptx` carry an explicit East Asian font.

## Step 3 · Ship through the gate

Run the Delivery gate, write the report (under 15 lines, evidence per line), and hand over the report with the file. A HARD fail is not shipped and is not "flagged for later".

## Precedence

The user's live brief wins for the task at hand. Then: this system's README and `tokens.json` for values · the Decks section for anything on slides · the Delivery gate for shipping · Power Design principles for craft, with the stated overrides. When a TI source (ti.com, a TI-supplied file) contradicts a value here, the TI source wins and this system is corrected, not worked around.

## Changing this system

Edit the files in this repo and open a pull request; the private Claude design-system artifact mirrors it (`SYNC.md` maps the two; the artifact's confidential overview deck never comes here). A value change goes in `tokens.json` (never in prose alone); a rule change goes in the section that owns it and is mirrored in the README if the README states it; assets are added to their group with a line in that group's README. Record what changed and why in `lastChange`. Versioning: patch for wording and fixes, minor for a new rule, layout or asset group, major when existing builds would break.


---

<sub>Texas Instruments design system — built by **Nicolas Chan**, Head of Digital & Chief Strategist, AMEA, The Hoffman Agency. Texas Instruments, the TI signature and TI DLP® are trademarks of Texas Instruments Incorporated; see `LICENSE.md`.</sub>
