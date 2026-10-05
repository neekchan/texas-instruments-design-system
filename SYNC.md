# Sync: this repo and the Claude Design artifact

The system has two homes, kept in sync file by file: this private repo (the team's copy, with the PowerPoint template and the tools) and Nic's private Claude Design artifact "Texas Instruments" (a Design System artifact, https://claude.ai/artifact/TKPtxfcJAXvrunGLd4aqY3). A change made in one goes to the other in the same session. The artifact names its sections by number, the repo by file name; otherwise the text is the same.

## Never synced

`assets/TI_Overview_2026.pptx` in the artifact is TI's company overview deck from the 2026 RFP: client-confidential. It stays in the private artifact only and never comes into this repo, under any name. The same goes for any other RFP document or TI-supplied internal file. `.gitignore` blocks them.

## File map

| Repo | Artifact (`project/…`) |
| --- | --- |
| `README.md` | `README.md` (the repo adds its own header, team path and start-here list) |
| `DECKS.md` | `01-decks.md` |
| `SOUNDCHECK.md` | `02-soundcheck.md` |
| `POWER-DESIGN-PRINCIPLES.md` | `03-power-design-principles.md` |
| `CHECKLIST.md` | `04-delivery-gate.md` |
| `POWERPOINT.md` | `05-powerpoint.md` |
| `IMAGERY.md` | `06-imagery-and-icons.md` |
| `LLM_ENTRYPOINT.md` | `07-agent-workflow.md` |
| `DECK-TEMPLATE.md` | `08-deck-template.md` |
| `tokens.json` | `tokens.json` (identical, whole file) |
| `assets/<Group>/README.md` | `assets/<Group>/README.md` |
| `components/Cover/preview.html` | `components/Cover/preview.html` |
| `assets/Logos`, `assets/Backgrounds`, `assets/Reference` images and PDFs | the artifact's asset store (same images; the artifact holds re-encoded, pixel-identical copies) |
| `assets/Icons/*.svg` | `assets/Icons/*.svg` |

Repo only: `AGENTS.md`, `CLAUDE.md`, `CHANGELOG.md`, `LICENSE.md`, `SYNC.md`, `tokens.css`, `package.json`, `tools/`, `templates/`, `assets/Icons/fluent/` and `assets/Icons/png/`. Artifact only: its index `design-system.json` (stamp its `lastChange` on every sync), the files it generates (`manifest.json`, `api/…`, `tokens.css`) and the confidential overview deck.

Home-specific wording stays home-specific: the repo says "`DECKS.md`" where the artifact says "the Decks section", and each home describes how it is edited.
