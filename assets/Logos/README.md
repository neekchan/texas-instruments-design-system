# Logos

The files below are in this folder: TI's own published files (ti.com media resources and the ti.com header vector). `tools/fetch-assets.sh` re-downloads them if TI ever republishes.

The Texas Instruments signature: the Texas-shaped mark with the lower-case "ti", plus the wordmark. TI's trademark page names the stacked form the preferred signature and the horizontal form the alternate, and asks that the signature be used whole, never the mark alone.

| file | what | use |
| --- | --- | --- |
| `ti-signature-horizontal.svg` | Alternate (horizontal) signature, vector, mark in `red` #cc0000, wordmark black. ti.com's own header asset, 280 × 36 viewBox. | The default for slides (footer, `logo-deck` 280px), web headers, anything that scales. |
| `ti-stacked-red-logo.png` | Preferred (stacked) signature, red mark, black wordmark. 640 × 360 PNG from TI's media-resources page; the signature sits inside a white-padded canvas. | Covers, print, documents with room above the fold. Crop the padding or place on white. |
| `ti-red-logo.png` | Alternate (horizontal) signature, red mark, black wordmark, 640 × 360 PNG, white-padded. | Raster fallback for the SVG. |
| `ti-stacked-black-logo.png` | Preferred signature, one colour, black. 640 × 360 PNG. | One-colour print, co-branding lockups where red would fight another mark. |
| `ti-black-logo.png` | Alternate signature, one colour, black. 640 × 360 PNG. | One-colour horizontal. |

Rules

- On white (`surface`) or `grey-050`/`grey-100` only. Never over a photograph or a coloured fill; never inside a shape.
- Clear space at least the height of the mark on all four sides. Minimum width `logo-min-web` 120px on screen; the DLP guideline's print minimum of 0.875 in is a sensible print floor for the corporate signature too.
- Never recolour, outline, rotate, stretch, add effects, or separate the mark from the wordmark. The red is #cc0000; the PNGs sample at #cc0001.
- No white or reversed version is in this system, so v1 has no dark surfaces. A `red` or `teal-deck` divider carries no signature. Ask TI (mediarelations@ti.com) for the reversed files before any dark design is attempted.
- Single-ink SVG: the SVG carries its own fills (red and black); it does not inherit `currentColor`.


---

<sub>Texas Instruments design system — built by **Nicolas Chan**, Head of Digital & Chief Strategist, AMEA, The Hoffman Agency. Texas Instruments, the TI signature and TI DLP® are trademarks of Texas Instruments Incorporated; see `LICENSE.md`.</sub>
