# AGENTS.md — Texas Instruments design system

The canonical instruction file for any coding or design agent working in this repo (Codex, Cursor, Copilot, Claude Code, Gemini, Amp and the rest all read this name). `CLAUDE.md` only points here. If anything elsewhere conflicts with this file, this file wins.

## Read order

0. `LLM_ENTRYPOINT.md` — run its intake first (medium, mode, audience and language, colour direction, imagery) and echo the one-line brief.
1. `README.md` — the brand book: voice, trademarks, colour, type, layout, icons, logos.
2. `tokens.json` — every exact value; its usage notes are binding. `tokens.css` is the same, compiled for web.
3. By task: `DECKS.md` + `SOUNDCHECK.md` + `DECK-TEMPLATE.md` for slides; `POWERPOINT.md` for `.pptx`; `IMAGERY.md` for any picture or icon; `POWER-DESIGN-PRINCIPLES.md` for craft.
4. `CHECKLIST.md` before anything ships; write the delivery report it specifies.

## Hard rules that survive a partial paste

- TI red is #CC0000 and nothing else; teal #117788 for icons and lead-in phrases; black body text; white page.
- Arial everywhere, every weight. No other typeface.
- One red object per surface beyond the title and the footer rule.
- Slides: body 12pt (32px at 1920) minimum, captions 10pt, nothing under 9pt, three sizes per slide; 48px safe margin; fill the frame.
- The footer rule starts at the left edge and stops short of the right edge, flush with the signature. It never runs edge to edge.
- The signature is used whole, never the mark alone, never inverted, never on a coloured surface. No dark surfaces in v1.
- Icons: Fluent UI System Icons, regular style, from `assets/Icons/`. No emoji, no other icon family.
- Every number sourced or a visible `[REAL DATA · what · who supplies it]` placeholder. No invented quotes, clients, awards or results.
- One mode per deck: Presenter XOR Document.
- Start from `templates/powerpoint/TI_Deck_Template_v1.pptx`: add slides from its 34 layouts and type into the placeholders; no loose text boxes; never rebuild the master (`DECK-TEMPLATE.md`).

Client-confidential material never enters this repo: no RFP documents, no TI-supplied internal decks, nothing TI gave Hoffman under the pitch. It stays in Hoffman's TI client files.

This repo and Nic's private Claude Design artifact "Texas Instruments" are the system's two homes, kept in sync file by file (`SYNC.md` maps them). One exception: the artifact's `assets/TI_Overview_2026.pptx` (TI's confidential company overview) stays in the artifact and is never synced here.

Every asset is in the repo; nothing needs fetching. `tools/fetch-assets.sh` exists only to refresh the signature files from ti.com if TI republishes them.


---

<sub>Texas Instruments design system — built by **Nicolas Chan**, Head of Digital & Chief Strategist, AMEA, The Hoffman Agency. Texas Instruments, the TI signature and TI DLP® are trademarks of Texas Instruments Incorporated; see `LICENSE.md`.</sub>
