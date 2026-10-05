# Changelog

## 1.1.0 — 2026-10-05

PowerPoint template made fillable for team decks. 34 layouts on TI's master, in the New Slide menu: 18 TI layouts (cover, red section divider, teal appendix divider, agenda, title + body, two columns, statement, three columns, stat strip, chart + takeaway, table, image + text, timeline, team, pull quote, title only, closing, blank) and 16 structures adapted from The Hoffman Agency's 2025 AMEA template (one per colour family), rescaled to 10 in, kept above TI's footer band and remapped into TI's palette. Every box carries prompt text with its word budget. Theme named "Texas Instruments" with ten custom colours in the colour picker; new shapes default to teal, new lines to teal 1.5pt, new text boxes to Arial 12pt; new tables default to a hairline style with a grey-100 header. Slide numbers are live fields. Example slides lose their typed page numbers, and ten non-integer coordinates on slides 8–10 that could trigger PowerPoint's repair prompt are fixed. Build scripts: `tools/add_layouts.py`, `tools/port_hoffman_layouts.py`.

Removed `assets/Reference/TI_Overview_2026.pptx`: TI's company overview deck is client-confidential RFP material and was never meant to be here. The template's example slides no longer quote it (slide 8's "TI Taiwan at 55" and slide 10's three figures are now placeholders). New rule in `AGENTS.md`: client-confidential material never enters this repo; `.gitignore` blocks decks and documents under `assets/Reference/`.

## 1.0.1 — 2026-10-05

Repository made private for the Hoffman TI team. Everything in the repo, nothing to fetch: signature files, title backgrounds, TI's original deck icons, the reference deck and the DLP guidelines added under `assets/`; the PowerPoint template is the complete file (signature, backgrounds, Fluent icons). Team quick-start added to the README. `AGENTS.md` is the canonical agent entry file (`CLAUDE.md` points to it). `tools/fetch-assets.sh` kept as a refresh tool only.

## 1.0.0 — 2026-10-05

First release. Tokens from ti.com's Polaris CSS (Oct 2026) and TI's 2026 corporate deck theme; TI red fixed at #CC0000 (the deck's #DE0000 kept as `red-deck`); white-only, no dark theme until TI supplies a reversed signature; brand book, decks, Soundcheck, Power Design principles, delivery gate, PowerPoint production, imagery and icons, agent workflow; 15-slide PowerPoint template on TI's master, complete with signature and backgrounds; asset catalogues with a fetch script for the published signature files; Fluent UI System Icons adopted as the one icon library, whole library vendored (20,798 SVGs, MIT) plus a 118-icon curated TI set in teal.
