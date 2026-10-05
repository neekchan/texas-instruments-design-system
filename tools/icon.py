#!/usr/bin/env python3
"""Pull any Fluent icon into TI colours.

  tools/icon.py <name> [--size 24] [--style regular] [--color teal|ink|white|#hex] [--png 512]

Writes assets/Icons/<name>[-color].svg (and .png with --png). Names are the library's own:
see assets/Icons/catalog.json or ls assets/Icons/fluent.
"""
import argparse, os, re, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
a = argparse.ArgumentParser()
a.add_argument('name'); a.add_argument('--size', default='24'); a.add_argument('--style', default='regular')
a.add_argument('--color', default='teal'); a.add_argument('--png', type=int, default=0)
o = a.parse_args()
col = {'teal': '#117788', 'ink': '#333333', 'white': '#ffffff'}.get(o.color, o.color)
src = f'{root}/assets/Icons/fluent/{o.name}_{o.size}_{o.style}.svg'
if not os.path.exists(src):
    sys.exit(f'not in the library: {src}')
svg = re.sub(r'fill="#?[0-9a-fA-F]{3,6}"', '', open(src).read())
svg = re.sub(r'<svg ', f'<svg fill="{col}" ', svg, count=1)
suffix = '' if o.color == 'teal' else '-' + o.color.strip('#')
out = f'{root}/assets/Icons/{o.name}{suffix}.svg'
open(out, 'w').write(svg); print('wrote', out)
if o.png:
    try:
        import cairosvg
        cairosvg.svg2png(bytestring=svg.encode(), write_to=out[:-4] + '.png', output_width=o.png, output_height=o.png)
        print('wrote', out[:-4] + '.png')
    except ImportError:
        print('pip install cairosvg for PNG output, or render the SVG in a browser')
