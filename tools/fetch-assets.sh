#!/usr/bin/env bash
# Re-downloads Texas Instruments' published signature files from ti.com into assets/Logos/.
# The repo already carries them; run this only if TI republishes its files.
set -euo pipefail
cd "$(dirname "$0")/../assets/Logos"
UA="Mozilla/5.0"
for f in ti-red-logo ti-stacked-red-logo ti-black-logo ti-stacked-black-logo; do
  curl -fsSL -A "$UA" -o "$f.png" "https://www.ti.com/content/dam/ticom/images/identities/ti-brand/$f.png"
  echo "fetched $f.png"
done
curl -fsSL -A "$UA" -o ti-signature-horizontal.svg "https://www.ti.com/etc/designs/ti/images/ui/ic-logo.svg"
echo "fetched ti-signature-horizontal.svg (ti.com header vector, 280x36)"
echo "Checksums (compare with assets/Logos/README.md if TI republishes):"; shasum -a 256 *.png *.svg
